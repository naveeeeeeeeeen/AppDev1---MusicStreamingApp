from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

## MODELS ##

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80), unique= True, nullable= False)
    passhash = db.Column(db.String(100), unique= True, nullable= False)
    name = db.Column(db.String(100), nullable= True)
    is_creator = db.Column(db.Boolean, default= False)
    is_admin = db.Column(db.Boolean, default= False)
    is_blacklisted = db.Column(db.Boolean, default= False)


    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')
    @password.setter
    def password(self, password):
        self.passhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passhash, password)

class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable= False)
    creator_name = db.Column(db.String(80), nullable= False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))
    lyrics = db.Column(db.String, nullable= True)
    genre = db.Column(db.String(50), nullable = False)
    duration = db.Column(db.Integer, nullable= False) #duration in seconds
    likes = db.Column(db.Integer, default= 0)
    play_count = db.Column(db.Integer, default= 0)
    

class Album(db.Model):
    __tablename__ = 'album'
    id = db.Column(db.Integer, primary_key= True)
    creator_name = db.Column(db.String(80), nullable= False)
    name = db.Column(db.String(100), unique= True, nullable= False)
    year = db.Column(db.Integer, nullable= False)
    ##relationship
    songs = db.relationship('Song', backref='album', lazy= True)



#Association table for many to many relationship between playlist and song
playlist_song_table = db.Table('playlist_song', 
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id'), primary_key= True), 
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key= True)
    )

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    songs = db.relationship('Song', secondary= playlist_song_table, backref='playlist', lazy= True, primaryjoin=(id == playlist_song_table.c.playlist_id))

