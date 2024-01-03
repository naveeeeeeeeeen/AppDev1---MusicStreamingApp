from flask import current_app as app
from flask import render_template, url_for, request, redirect, flash, session
from models import db, User, Song, Album, Playlist, check_password_hash
import matplotlib.pyplot as plt
import os

## ROUTES ##

@app.route('/')
def index():
    return render_template('index.html')

#Admin Login


@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin_login', methods=['POST'])
def admin_login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username= username).first()
    if username == '' or password == '':
        flash('Please fill out all fields.')
        return redirect(url_for('admin_login'))
    if not user:
        flash('Username does not exit')
        return redirect(url_for('admin_login'))
    if not user.check_password(password):
        flash('Incorrect password.')
        return redirect(url_for('admin_login'))
    if not user.is_admin:
        flash('You are not an admin.')
        return redirect(url_for('admin_login'))
    #login successful
    session['user_id'] = user.id
    return redirect(url_for('admin_dashboard'))


@app.route('/admin_dashboard')
def admin_dashboard():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    songs= Song.query.all()
    total_songs = len(Song.query.all())
    total_likes = sum([song.likes for song in Song.query.all()])
    total_views = sum([song.play_count for song in Song.query.all()])
    total_albums = len(Album.query.all())
    total_users = len(User.query.all())-1
    total_creators = len(User.query.filter_by(is_creator= True).all())
    play_count_graph(songs)
    genre_graph(songs)
    like_graph(songs)
    
    return render_template('admin_dashboard.html', admin= User.query.get(session['user_id']), total_songs= total_songs,total_likes= total_likes, total_views= total_views, total_albums= total_albums, total_users= total_users, total_creators= total_creators)


@app.route('/admin_dashboard', methods=['POST'])
def admin_dashboard_post():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    if request.method == 'POST':
        search_type= request.form.get('search_type')
        search_query= request.form.get('search_query')
        if search_query is None:
            flash('Please enter a search query.')
            return redirect(url_for('admin_dashboard'))
        if search_query == '':
            flash('Please enter a search query.')
            return redirect(url_for('admin_dashboard'))
        if search_type == 'songs':
            songs = Song.query.filter(Song.name.ilike('%' + search_query + '%')).all()
        elif search_type == 'albums':
            albums = Album.query.filter(Album.name.ilike('%' + search_query + '%')).all()
            songs = [song for album in albums for song in album.songs]
        elif search_type == 'artists':
            songs = Song.query.filter(Song.creator_name.ilike('%' + search_query + '%')).all()
        elif search_type == 'genres':
            songs = Song.query.filter(Song.genre.ilike('%' + search_query + '%')).all()
        else:
            flash('Invalid search query.')
            return redirect(url_for('admin_dashboard'))

        return render_template('admin_dashboard_search.html', admin=User.query.get(session['user_id']), songs=songs, search_query=search_query)




@app.route('/tracks')
def tracks():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    return render_template('tracks.html', admin= User.query.get(session['user_id']), songs = Song.query.all())


@app.route('/tracks/view_lyrics/<int:song_id>')
def view_lyrics(song_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    song = Song.query.get(song_id)
    return render_template('view_lyrics.html', admin= User.query.get(session['user_id']), song= song)

@app.route('/tracks/delete_song/<int:song_id>')
def delete_song(song_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    song = Song.query.get(song_id)
    return render_template('delete_song.html', admin= User.query.get(session['user_id']), song= song)
    
@app.route('/tracks/delete_song/<int:song_id>', methods=['POST'])
def delete_song_post(song_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    song = Song.query.get(song_id)
    db.session.delete(song)
    db.session.commit()
    flash('Song deleted successfully.')
    return redirect(url_for('tracks'))



@app.route('/albums')
def albums():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    return render_template('albums.html', admin= User.query.get(session['user_id']), albums= Album.query.all())


@app.route('/albums/view_songs/<int:album_id>')
def view_songs(album_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    album = Album.query.get(album_id)
    songs = album.songs
    return render_template('view_songs.html', admin= User.query.get(session['user_id']), songs= songs, album = album)




@app.route('/albums/delete_album/<int:album_id>')
def delete_album(album_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    album = Album.query.get(album_id)
    return render_template('delete_album.html', admin= User.query.get(session['user_id']), album = album)

@app.route('/albums/delete_album/<int:album_id>', methods=['POST'])
def delete_album_post(album_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    album = Album.query.get(album_id)
    songs = album.songs
    for song in songs:
        db.session.delete(song)
    db.session.delete(album)
    db.session.commit()
    flash('Album deleted successfully.')
    return redirect(url_for('albums'))



@app.route('/creators')
def creators():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    return render_template('creators.html', admin= User.query.get(session['user_id']), users= User.query.filter_by(is_creator= True).all())


@app.route('/creators/blacklist_creator/<int:user_id>')
def blacklist_creator(user_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    user = User.query.get(user_id)
    return render_template('blacklist_creator.html', admin= User.query.get(session['user_id']), user = user)

@app.route('/creators/blacklist_creator/<int:user_id>', methods=['POST'])
def blacklist_creator_post(user_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    user = User.query.get(user_id)
    if user.is_blacklisted:
        flash('Creator is already blacklisted. They cannot be blacklisted again.')
        return redirect(url_for('creators'))
    user.is_blacklisted = True
    db.session.commit()
    flash('Creator blacklisted successfully. They cannot upload new songs anymore.')
    return redirect(url_for('creators'))



@app.route('/creators/whitelist_creator/<int:user_id>')
def whitelist_creator(user_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    user = User.query.get(user_id)
    return render_template('whitelist_creator.html', admin= User.query.get(session['user_id']), user = user)

@app.route('/creators/whitelist_creator/<int:user_id>', methods=['POST'])
def whitelist_creator_post(user_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    user = User.query.get(user_id)
    if not user.is_blacklisted:
        flash('Creator is already whitelisted. They cannot be whitelisted again.')
        return redirect(url_for('creators'))
    user.is_blacklisted = False
    db.session.commit()
    flash('Creator whitelisted successfully.')
    return redirect(url_for('creators'))



@app.route('/creators/delete_creator/<int:user_id>')
def delete_creator(user_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    user = User.query.get(user_id)
    songs = Song.query.filter_by(creator_name= user.username).all()
    tracks = [song.name for song in songs]
    return render_template('delete_creator.html', admin= User.query.get(session['user_id']), user = user, tracks= tracks)



@app.route('/creators/delete_creator/<int:user_id>', methods=['POST'])
def delete_creator_post(user_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('admin_login'))
    user = User.query.get(user_id)
    songs = Song.query.filter_by(creator_name= user.username).all()
    for song in songs:
        db.session.delete(song)
    albums = Album.query.filter_by(creator_name= user.username).all()
    for album in albums:
        db.session.delete(album)
    user.is_creator = False
    db.session.commit()
    flash('Creator deleted successfully.')
    return redirect(url_for('creators'))



#User Login

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username= username).first()
    if username == '' or password == '':
        flash('Please fill out all fields.')
        return redirect(url_for('login'))
    if username == 'admin':
        flash('Invalid Username')
        return redirect(url_for('login'))
    if not user:
        flash('Username does not exit. Please register.')
        return redirect(url_for('register'))
    if not user.check_password(password):
        flash('Incorrect password.')
        return redirect(url_for('login'))
    #login successful
    session['user_id'] = user.id
    return redirect(url_for('user_dashboard'))


@app.route('/user_dashboard')
def user_dashboard():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    songs = Song.query.all()
    playlists = Playlist.query.filter_by(user_id= session['user_id']).all()
    playlist_songs = [ [song.name for song in playlist.songs] for playlist in playlists]
    return render_template('user_dashboard.html', user= User.query.get(session['user_id']), songs= songs, playlists= playlists, playlist_sonsg= playlist_songs)

@app.route('/user_dashboard', methods=['POST'])
def user_dashboard_post():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        search_type= request.form.get('search_type')
        search_query= request.form.get('search_query')
        if search_query is None:
            flash('Please enter a search query.')
            return redirect(url_for('user_dashboard'))
        if search_query == '':
            flash('Please enter a search query.')
            return redirect(url_for('user_dashboard'))
        if search_type == 'songs':
            songs = Song.query.filter(Song.name.ilike('%' + search_query + '%')).all()
        elif search_type == 'albums':
            albums = Album.query.filter(Album.name.ilike('%' + search_query + '%')).all()
            songs = [song for album in albums for song in album.songs]
        elif search_type == 'artists':
            songs = Song.query.filter(Song.creator_name.ilike('%' + search_query + '%')).all()
        elif search_type == 'genres':
            songs = Song.query.filter(Song.genre.ilike('%' + search_query + '%')).all()
        else:
            flash('Invalid search query.')
            return redirect(url_for('user_dashboard'))

        return render_template('user_dashboard_search.html', user=User.query.get(session['user_id']), songs=songs, search_query=search_query)





@app.route('/create_playlist')
def create_playlist():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    songs = Song.query.all()
    return render_template('create_playlist.html', user= User.query.get(session['user_id']), songs= songs)

@app.route('/create_playlist', methods=['POST'])
def create_playlist_post():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    playlist_name = request.form.get('playlist_name')
    selected_songs = request.form.getlist('selected_songs')
    if playlist_name == '':
        flash('Please fill out all fields.')
        return redirect(url_for('create_playlist'))
    if len(selected_songs) == 0:
        flash('Please select at least one song.')
        return redirect(url_for('create_playlist'))
    user = User.query.get(session['user_id'])
    new_playlist = Playlist(name= playlist_name, user_id= user.id)
    for song_id in selected_songs:
        song = Song.query.get(song_id)
        if song:
            new_playlist.songs.append(Song.query.get(song_id))
        else:
            flash('Song does not exist.')
            return redirect(url_for('create_playlist'))
    db.session.add(new_playlist)
    db.session.commit()
    flash('Playlist created successfully.')
    return redirect(url_for('user_dashboard'))
    

@app.route('/user_dashboard/delete_playlist/<int:playlist_id>')
def delete_playlist(playlist_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    playlist = Playlist.query.get(playlist_id)
    return render_template('delete_playlist.html', user= User.query.get(session['user_id']), playlist= playlist)

@app.route('/user_dashboard/delete_playlist/<int:playlist_id>', methods=['POST'])
def delete_playlist_post(playlist_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    playlist = Playlist.query.get(playlist_id)
    db.session.delete(playlist)
    db.session.commit()
    flash('Playlist deleted successfully.')
    return redirect(url_for('user_dashboard'))

@app.route('/user_dashboard/open_playlist/<int:playlist_id>')
def open_playlist(playlist_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    playlist = Playlist.query.get(playlist_id)
    songs = playlist.songs
    return render_template('open_playlist.html', user= User.query.get(session['user_id']), playlist= playlist, songs= songs)


@app.route('/user_dashboard/all_songs')
def all_songs():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    songs = Song.query.all()
    return render_template('all_songs.html', user= User.query.get(session['user_id']), songs = songs)


@app.route('/user_dashboard/play/<int:song_id>')
def play(song_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    song = Song.query.get(song_id)
    song.play_count += 1
    db.session.commit()
    return render_template('play.html', user= User.query.get(session['user_id']),song= song)


@app.route('/user_dashboard/like/<int:song_id>')
def like(song_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    
    if 'liked' not in session:
        session['liked'] = []  

    liked_songs = set(session['liked'])

    if song_id not in liked_songs:
        song = Song.query.get(song_id)
        song.likes += 1
        liked_songs.add(song_id)
        session['liked'] = list(liked_songs)  
        db.session.commit()
        flash('You liked the song.')
    else:
        flash('You have already liked the song.')
    
    return redirect(url_for('user_dashboard'))



@app.route('/user_dashboard/dislike/<int:song_id>')
def dislike(song_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    
    if 'disliked' not in session:
        session['disliked'] = set()

    disliked_songs = set(session['disliked'])

    if song_id not in disliked_songs:
        song = Song.query.get(song_id)
        song.likes -= 1
        disliked_songs.add(song_id)
        session['disliked'] = list(disliked_songs)  
        db.session.commit()
        flash('You disliked the song.')
    else:
        flash('You have already disliked the song.')
    
    return redirect(url_for('user_dashboard'))




@app.route('/user_profile')
def user_profile():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    return render_template('user_profile.html', user= User.query.get(session['user_id']))

@app.route('/user_profile', methods=['POST'])
def user_profile_post():
    cpassword = request.form.get('cpassword')
    password = request.form.get('password')
    user = User.query.get(session['user_id'])
    if cpassword == '' or password == '':
        flash('Please fill out all fields.')
        return redirect(url_for('user_profile'))
    if not check_password_hash(user.passhash, cpassword):
        flash('Incorrect password.')
        return redirect(url_for('user_profile'))
    #set new password
    user.password = password
    db.session.commit()
    flash('Password changed successfully.')
    return redirect(url_for('user_profile'))



#CREATOR

@app.route('/creator_dashboard')
def creator_dashboard():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    songs = Song.query.all()
    user = User.query.get(session['user_id'])
    total_uploads = len(Song.query.filter_by(creator_name= user.username).all())
    total_likes = sum([song.likes for song in Song.query.filter_by(creator_name= user.username).all()])
    total_albums = len(Album.query.filter_by(creator_name= user.username).all())
    return render_template('creator_dashboard.html', user= user, songs = songs, total_uploads= total_uploads, total_likes= total_likes, total_albums= total_albums)   


@app.route('/creator_register')
def creator_register():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    if User.query.get(session['user_id']).is_creator:
        return redirect(url_for('creator_dashboard'))
    return render_template('creator_register.html', user= User.query.get(session['user_id']))


@app.route('/creator_register', methods=['POST'])
def creator_register_post():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    user= User.query.get(session['user_id'])
    password = request.form.get('password')
    if not check_password_hash(user.passhash, password):
        flash('Incorrect password.')
        return redirect(url_for('creator_register'))
    #set user as creator
    user.is_creator = True
    db.session.commit()
    return redirect(url_for('creator_dashboard'))



@app.route('/upload')
def upload():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    if not User.query.get(session['user_id']).is_creator:
        flash('You are not a creator. Please register as a creator to upload songs.')
        return redirect(url_for('creator_register'))
    if User.query.get(session['user_id']).is_blacklisted:
        flash('You have been blacklisted. You cannot upload new songs.')
        return redirect(url_for('creator_dashboard'))
    return render_template('upload.html', user= User.query.get(session['user_id']))

@app.route('/upload', methods=['POST'])
def upload_post():
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    title = request.form.get('title')
    artist = user.username
    album = request.form.get('album')
    genre = request.form.get('genre')
    year = request.form.get('year')
    duration = request.form.get('duration')
    lyrics = request.form.get('lyrics')
    file = request.files['myfile']

    new_album = Album(creator_name= artist, name= album, year= year)
    new_song = Song(name= title, creator_name= artist, lyrics= lyrics, genre= genre, duration= duration)
    save_audio_file(file, title)

    A = Album.query.filter_by(name= album).first()
    if A:
        flash('Album already exists. Song added to existing album.')
        A.songs.append(new_song)
    else:
        new_album.songs.append(new_song)
        db.session.add(new_album)

    db.session.commit()
    flash('Song uploaded successfully.')
    return redirect(url_for('creator_dashboard'))

    
@app.route('/creator_dashboard/delete_upload/<int:song_id>')
def delete_upload(song_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    song= Song.query.get(song_id)
    return render_template('delete_upload.html', user= User.query.get(session['user_id']), song= song)


@app.route('/creator_dashboard/delete_upload/<int:song_id>', methods=['POST'])
def delete_upload_post(song_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    song= Song.query.get(song_id)
    audio_file= 'static/audio/' + song.name + '.mp3'
    db.session.delete(song)
    db.session.commit()
    os.remove(audio_file)
    flash('Song deleted successfully')
    return redirect(url_for('creator_dashboard'))


@app.route('/creator_dashboard/edit_upload/<int:song_id>')
def edit_upload(song_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    song= Song.query.get(song_id)
    return render_template('edit_upload.html', user= User.query.get(session['user_id']), song= song)

@app.route('/creator_dashboard/edit_upload/<int:song_id>', methods=['POST'])
def edit_upload_post(song_id):
    if 'user_id' not in session:
        flash('Please login to continue.')
        return redirect(url_for('login'))
    song= Song.query.get(song_id)
    audio_file= 'static/audio/' + song.name + '.mp3'

    title = request.form.get('title')
    album = request.form.get('album')
    genre = request.form.get('genre')
    year = request.form.get('year')
    duration = request.form.get('duration')
    lyrics = request.form.get('lyrics')


    if song.name != title:
        song.name = title
        os.rename(audio_file, 'static/audio/' + title + '.mp3')
    if song.album.name != album:
        check_album = Album.query.filter_by(name = album).first()
        if check_album:
            flash('Album name already exists. Please give some other name')
            return redirect(request.referrer)
        else:
            song.album.name= album

    song.album.year= year
    song.genre= genre
    song.duration= duration
    song.lyrics= lyrics
    
    db.session.commit()
    flash('Song updated successfully.')
    return redirect(url_for('creator_dashboard'))




#Register

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form.get('username')
    password = request.form.get('password')
    name = request.form.get('name')
    if username == '' or password == '' or name == '':
        flash('Please fill out all fields.')
        return redirect(url_for('register'))
    if username == 'admin':
        flash('Invalid Username. Please choose another.')
        return redirect(url_for('register'))
    if User.query.filter_by(username= username).first():
        flash('Username already taken. Please choose another.')
        return redirect(url_for('register'))
    user = User(username= username, password= password, name= name)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful. Please login.')
    return redirect(url_for('login'))

    
#Logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))





## HELPER FUNCTIONS ##


def like_graph(songs):
    likes = [song.likes for song in songs if song.likes > 4]
    song_names = [song.name for song in songs if song.likes > 4]
    
    plt.figure(figsize=(6,3))
    plt.barh(song_names, likes , color='green')
    plt.xlabel('No. of likes', fontweight='bold')
    plt.tight_layout()
    # Save the graph as an image file in static folder
    plt.savefig('static/like_graph.png')


def genre_graph(songs):
    genre_set = set([song.genre for song in songs])
    genre = list(genre_set)
    genre_count = [len(Song.query.filter_by(genre= g).all()) for g in genre]

    plt.figure(figsize=(6,3))
    plt.barh(genre, genre_count , color='blue')
    plt.xlabel('No. of songs', fontweight='bold')
    plt.tight_layout()
    # Save the graph as an image file in static folder
    plt.savefig('static/genre_graph.png')


def play_count_graph(songs):
    play_count = [song.play_count for song in songs]
    song_names = [song.name for song in songs]

    plt.figure(figsize=(10,8))
    plt.bar(song_names, play_count , color='aqua')
    plt.ylabel('No. of times played', fontweight='bold')
    plt.xticks(rotation=90)
    plt.tight_layout()
    # Save the graph as an image file in static folder
    plt.savefig('static/play_count_graph.png') 


def save_audio_file(file, title):
    file.save('static/audio/' + title + '.mp3')
