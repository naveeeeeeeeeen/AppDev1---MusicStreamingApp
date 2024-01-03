from flask import current_app as app
from models import db, User, Song, Album


albums = [Album(creator_name = "Mohit Chauhan", name = "Rockstar", year = 2011),
          Album(creator_name = "Selena Gomez", name = "For you", year = 2014),
          Album(creator_name = "Selena Gomez", name = "When the sun goes down", year = 2011),
          Album(creator_name = "Darbuka Siva", name = "Mudhal nee mudivum nee", year = 2022),
          Album(creator_name = "A.R. Rahman", name = "Achcham Yenbadhu", year = 2016),
          Album(creator_name = "Enya", name = "A Day Without Rain", year = 2000),
          Album(creator_name = "Tom Odell", name = "Long Way Down", year = 2013),
          Album(creator_name = "Justin Bieber", name = "Father Of Asahd", year = 2019),
          Album(creator_name = "Sukhwinder Singh", name = "Madaari", year = 2016),
          Album(creator_name = "Randwimps", name = "Your Name", year = 2016)]

songs = [Song(name= "Phir se udd chala", creator_name= "Mohit Chauhan", album_id=1, lyrics= 
              """फिर से उड़ चला
                उड़ के छोड़ा है जहां नीचे
                मैं तुम्हारे अब हूँ हवाले हवा
                दूर-दूर लोग-बाग़ मीलों दूर ये वादियाँ

                कर धुंआ धुंआ तन हर बदली चली आती है छूने
                और कोई बदली कभी कहीं कर दे तन गीला ये है भी ना हो
                किसी मंज़र पर मैं रुका नहीं
                कभी खुद से भी मैं मिला नहीं
                ये गिला तो है मैं खफ़ा नहीं
                शहर एक से, गाँव एक से
                लोग एक से, नाम एक
                फिर से उड़ चला

                मिट्टी जैसे सपने ये कित्ता भी
                पलकों से झाड़ो फिर आ जाते हैं
                इत्ते सारे सपने क्या कहूँ
                किस तरह से मैंने तोड़े हैं छोड़े हैं क्यूँ
                फिर साथ चले, मुझे ले के उड़े, ये क्यूँ

                कभी डाल-डाल, कभी पात-पात
                मेरे साथ-साथ, फिरे दर-दर ये
                कभी सहरा, कभी सावन
                बनूँ रावण क्यूँ मर-मर के
                कभी डाल-डाल, कभी पात-पात
                कभी दिन है रात, कभी दिन-दिन है
                क्या सच है, क्या माया है दाता

                इधर-उधर तितर-बितर
                क्या है पता हवा लिए जाए तेरी ओर
                खींचे तेरी यादें तेरी ओर
                रंग बिरंगे वहमों में मैं उड़ता फिरूं""", genre= 'Bollywood', duration= 213, likes= 5, play_count= 12),
         Song(name= "Jo Bhi Main", creator_name= "Mohit Chauhan", album_id=1, lyrics= 
              """जो भी मैं कहना चाहूं
                बर्बाद करे अल्फ़ाज़ मेरे
                अल्फ़ाज़ मेरे

                कभी मुझे लगे की जैसे
                सारा ही ये जहाँ है जादू
                जो है भी और नही भी है ये
                फ़िज़ा, घटा, हवा, बहारें
                मुझे करे इशारे ये
                कैसे कहूँ?
                कहानी मैं इनकी

                जो भी मैं कहना चाहूं
                बर्बाद करे अल्फ़ाज़ मेरे
                अल्फ़ाज़ मेरे

                मैने ये भी सोचा है अक्सर
                तू भी मैं भी सभी है शीशे
                खुधी को हम सभी में देखें
                नहीं हूँ मैं हूँ मैं तो फिर भी
                सही ग़लत, तुम्हारा मैं
                मुझे पाना, पाना है खुद को

                जो भी मैं कहना चाहूं
                बर्बाद करे अल्फ़ाज़ मेरे
                अल्फ़ाज़ मेरे""", genre= 'Bollywood', duration= 292, likes= 4, play_count= 8),
         Song(name= "Hawaa Hawaa", creator_name= "Mohit Chauhan", album_id=1, lyrics= 
              """Chakri si pairo mein pahiya pahiya aiya aiya oho
                Aasmaan sarpat ghuma o o
                Kahiye sunaaiye hum ne toh oh
                Raani ghoome ghoome gore gore pairo se
                chik chik chik chik jara
                Rani phir nau do gyaraah
                Raati to iske aadi
                Ik din mein joote baarah
                Raja ka chadh gaya pyara
                Khabri ko paas pukara
                Ye kya hai maajra dekho.. o o

                Jaati kahaan hai woh
                Khabri ne peechha kiya
                Rani ko ghar se aata ....
                Jaate dekha
                Hava Hava..
                Hava Hava..
                Hawa Hawa..

                Shole behke (o ho)
                Rani behke (o ho)
                Naach Rangeele (o ho)
                Sab zehreele (o ho)
                Khabri chakraaya (o ho)
                Ulte paanv (o ho)
                Ruk gaya to batlaaya usne
                Hava hava
                Rani Hava
                Hawa hawa
                Hawa

                Nachi re magan
                Dhol wala sipahiya o ho
                Jo naache dhaay dhaay
                Ruke na phir paanv paanv paanv
                Hava hava
                Dheema haya
                Hava hava
                Ruke na phir paanv paanv paanv
                Raja jhallaya
                Door rozana
                Barah jooton ko ghise Rani
                Qissa hai ye aisa ho o ho

                Hava hava
                Hava hava
                Paanv ruke na kisi ke roke
                Ye toh chalenge
                Nach lenge
                Yahaan wahaan yaara masti mein""", genre= 'Bollywood', duration= 313, likes= 8, play_count= 20),
         Song(name= "Kun Faya Kun", creator_name= "Mohit Chauhan", album_id=1, lyrics= 
              """या निज़ामुद्दीन औलिया
                या निज़ामुद्दीन सलक़ा

                कदम बढ़ा ले
                हदों को मिटा ले
                आजा ख़ालीपन में पी का घर तेरा
                तेरे बिन ख़ाली, आजा, ख़ालीपन में
                तेरे बिन ख़ाली, आजा, ख़ालीपन में

                रंगरेज़ा
                रंगरेज़ा
                रंगरेज़ा
                रंगरेज़ा

                كن فيكون، كن فيكون، فيكون
                فيكون، فيكون، فيكون
                كن فيكون، كن فيكون، فيكون
                فيكون، فيكون، فيكون

                जब कहीं पे कुछ नहीं भी नहीं था
                वही था, वही था, वही था, वही था
                जब कहीं पे कुछ नहीं भी नहीं था
                वही था, वही था, वही था, वही था

                वो जो मुझ में समाया
                वो जो तुझ में समाया
                मौला वही वही माया
                वो जो मुझ में समाया
                वो जो तुझ में समाया
                मौला वही वही माया

                كن فيكون، كن فيكون
                صدق الله العلي العظيم

                रंगरेज़ा रंग मेरा तन, मेरा मन
                ले ले रंगाई चाहे तन, चाहे मन
                रंगरेज़ा रंग मेरा तन, मेरा मन
                ले ले रंगाई चाहे तन, चाहे मन

                सजरा सवेरा मेरे तन बरसे
                कजरा अँधेरा तेरी जलती लौ
                सजरा सवेरा मेरे तन बरसे
                कजरा अँधेरा तेरी जलती लौ
                क़तरा मिला जो तेरे दर पर से
                ओ मौला, मौला

                كن فيكون، كن فيكون
                كن فيكون، كن فيكون
                كن فيكون، كن فيكون، فيكون
                فيكون، فيكون، فيكون
                كن فيكون، كن فيكون، فيكون
                فيكون، فيكون، فيكون

                जब कहीं पे कुछ नहीं भी नहीं था
                वही था, वही था, वही था, वही था
                जब कहीं पे कुछ नहीं भी नहीं था
                वही था, वही था, वही था, वही था

                كن فيكون، كن فيكون
                صدق الله العلي العظيم
                صدق رسوله النبي الكريم
                صلّ الله عليه وسلم
                صلّ الله عليه وسلم

                ओ मुझपे करम सरकार तेरा
                अर्ज़ तुझे, "कर दे मुझे मुझसे ही रिहा
                अब मुझको भी हो दीदार मेरा
                कर दे मुझे मुझसे ही रिहा
                मुझसे ही रिहा"

                मन के मेरे ये भरम
                कच्चे मेरे ये करम
                लेके चाले है कहाँ
                मैं तो जानूँ ही ना

                तू है मुझमें समाया
                कहाँ लेके मुझे आया
                मैं हूँ तुझमें समाया
                तेरे पीछे चला आया
                तेरा ही मैं एक साया

                तूने मुझको बनाया
                मैं तो जग को ना भाया
                तुने गले से लगाया
                हक़ तू ही है ख़ुदाया
                सच तू ही है ख़ुदाया

                كن فيكون، كن فيكون، فيكون
                فيكون، فيكون، فيكون
                كن فيكون، كن فيكون، فيكون
                فيكون، فيكون، فيكون

                जब कहीं पे कुछ नहीं भी नहीं था
                वही था, वही था, वही था, वही था
                जब कहीं पे कुछ नहीं भी नहीं था
                वही था, वही था, वही था, वही था""", genre= 'Bollywood', duration= 381, likes= 11, play_count= 25),
         Song(name= "Come & get it", creator_name= "Selena Gomez", album_id=2, lyrics= 
              """When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na
                When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na
                When you're ready, when you're ready
                When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na
                You ain't gotta worry, it's an open invitation
                I'll be sitting right here real patient
                All day, all night, I'll be waiting standby
                Can't stop, because I love it
                Hate the way I love you
                All day, all night
                Maybe I'm addicted for life, no lie
                I'm not too shy to show I love you
                I got no regrets
                I love you much too much to hide you
                This love ain't finished yet
                This love ain't finished yet
                So baby, whenever you're ready
                When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na
                When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na
                When you're ready, when you're ready
                When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na
                You got the kind of love that I want, let me get that (let me get that, yeah)
                And baby, once I get it, I'm yours, no take-backs
                Gon' love you for life, I ain't leaving your side
                Even if you knock it, ain't no way to stop it
                Forever, you're mine
                Baby, I'm addicted, no lie, no lie
                I'm not too shy to show I love you
                I got no regrets
                So baby, whenever you're ready
                When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na
                When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na
                When you're ready, when you're ready
                When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na
                This love will be the death of me
                But I know I'll die happily
                I'll know, I'll know, I'll know
                Because you love me so
                Yeah
                When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na
                When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na (I'm gonna get it, yeah, yeah)
                When you're ready, when you're ready
                When you're ready come and get it
                Na-na-na-na, na-na-na-na, na-na-na-na""", genre= 'Pop', duration= 276, likes= 2, play_count= 15),
         Song(name= "Who Says", creator_name= "Selena Gomez", album_id=3, lyrics= 
              """I wouldn't wanna be anybody else, hey
                You made me insecure
                Told me I wasn't good enough
                But who are you to judge?
                When you're a diamond in the rough
                I'm sure you got some things
                You'd like to change about yourself
                But when it comes to me
                I wouldn't want to be anybody else
                Na-na-na-na, na-na-na-na
                Na-na-na-na, na
                Na-na-na-na, na-na-na-na
                Na-na-na-na, na
                I'm no beauty queen
                I'm just beautiful me
                Na-na-na-na, na-na-na-na
                Na-na-na-na, na
                Na-na-na-na, na-na-na-na
                Na-na-na-na, na
                You've got every right
                To a beautiful life
                Come on
                Who says, who says you're not perfect?
                Who says you're not worth it?
                Who says you're the only one that's hurting?
                Trust me, that's the price of beauty
                Who says you're not pretty?
                Who says you're not beautiful?
                Who says?
                It's such a funny thing
                How nothing's funny when it's you
                You tell 'em what you mean
                But they keep whiting out the truth
                It's like a work of art
                That never gets to see the light
                Keep you beneath the stars
                Won't let you touch the sky
                Na-na-na-na, na-na-na-na
                Na-na-na-na, na
                Na-na-na-na, na-na-na-na
                Na-na-na-na, na""", genre= 'Pop', duration= 201, likes= 0, play_count= 4), 
         Song(name= "Mudhal nee mudivum nee", creator_name= "Darbuka Siva", album_id=4, lyrics= 
              """ஆண் : ஆ… ஆஅ… ஆ…

                ஆண் : முதல் நீ முடிவும் நீ…
                மூன்று காலம் நீ…
                கடல் நீ கரையும் நீ…
                காற்று கூட நீ…

                ஆண் : மனதோரம் ஒரு காயம்…
                உன்னை எண்ணாத நாள் இல்லையே…
                நானாக நானும் இல்லையே…

                ஆண் : வழி எங்கும் பல பிம்பம்…
                அதில் நான் சாய தோள் இல்லையே…
                உன் போல யாரும் இல்லையே…

                குழு (ஆண்கள்) : தீரா நதி நீதானடி…
                நீந்தாமல் நான் மூழ்கி போனேன்…
                நீதானடி வானில் மதி…
                நீயல்ல நான்தானே தேய்ந்தேன்…

                ஆண் : பாதி கானகம்…
                அதில் காணாமல் போனவன்…
                ஒரு பாவை கால் தடம்…
                அதை தேடாமல் தேய்ந்தவன்…

                ஆண் : காணாத பாரம் என் நெஞ்சிலே…
                துணை இல்லா நான் அன்றிலே…
                நாளெல்லாம் போகும் ஆனால் நான்…

                குழு (ஆண்கள்) : உயிர் இல்லாத உடலே…

                ஆண் : ஆஅ… ஆஅ… ஆ… ஆ…

                —BGM—

                ஆண் : ஆ… ஆஅ… ஆ…

                ஆண் : முதல் நீ முடிவும் நீ…
                மூன்று காலம் நீ…
                கடல் நீ கரையும் நீ…
                காற்று கூட நீ…

                —BGM—

                ஆண் : தூர தேசத்தில்…
                தொலைந்தாயோ கண்மணி…
                உனை தேடி கண்டதும்…
                என் கண்ணெல்லாம் மின்மினி…

                ஆண் : பின்னோக்கி காலம் போகும் எனில்…
                உன் மன்னிப்பை கூறுவேன்…
                கண்ணோக்கி நேராய் பாக்கும் கணம்…

                குழு (ஆண்கள்) : பிழை எல்லாமே கலைவேன்…

                ஆண் : ஆஅ… ஆஅ… ஆ… ஆ…

                —BGM—

                ஆண் : ஆ… ஆஅ… ஆ…

                —BGM—

                ஆண் : முதல் நீ முடிவும் நீ…
                மூன்று காலம் நீ…
                கடல் நீ கரையும் நீ…
                காற்று கூட நீ…


                ஆண் : நகராத கடிகாரம்…
                அது போல் நானும் நின்றிருந்தேன்…
                நீ எங்கு சென்றாய் கண்ணம்மா…

                ஆண் : அழகான அரிதாரம்…
                வெளிப்பார்வைக்கு பூசி கொண்டேன்…
                புன்னைகைக்கு போதும் கண்ணம்மா…

                குழு (ஆண்கள்) : நீ கேட்கவே என் பாடலை…
                உன் ஆசை ராகத்தில் செய்தேன்…
                உன் புன்னகை பொன் மின்னலை…
                நான் கோர்த்து ஆங்காங்கு நெய்தேன்…""", genre= 'Tamil', duration= 336, likes= 9, play_count= 18),
         Song(name= "Rasaali", creator_name= "A.R. Rahman", album_id=5, lyrics= 
              """Male : Parakkum rasaaliye rasaaliye nillu
                Ingu nee vegama naan vegama sollu
                Gadigaram poi sollum endre naan kandennn
                Kizhakellam merkagida.. kandene

                Female : Paravai pol aaginen pol aaginen indru
                Siragum en kaigalum en kaigalum ondru

                Male : Rasaaliiiee.. pandhayama.. pandhayama..
                Nee mundhiya naan mundhiya paarpom parpomm

                Mudhalil yaar solvadhu yaar solvadhu anbai
                Mudhalil yaar eivadhu yaar Eivadhu ambai

                Male : Mounam pesamale pesamale sella
                Vaavi neeril kamalam pol aadi mella
                Kanavugal varuthe kannin vazhiye
                En thozh meethu nee
                Naan kulir kaaigindra thee

                Male : {Yettu thisai muttum yenai pagalinil
                Kottum pani mattum thunai iravinil
                Nettum oru pattu kural manathinil madiveno
                .
                Munnil oru kaatrin kali mugathinil
                Pinnil siru pachakili mudhuginil
                Vaazhvil oru payanam ithu mudinthida viduveno} (2)

                Male : Rasaaliiieee.. pandhayama aa..pandhayama..

                Mudhalil yaar solvadhu yaar solvadhu anbai
                Mudhalil yaar eivadhu yaar Eivadhu ambai
                Female : Ninnu kori.. ninnu kori..ninnu kori …ninnu koriiii… ninnu koriii….

                Female : {Veyil mazhai vetkum padi nanaivathai
                Vinmeengalum veenbai yenai thodarvathai
                Oorukoru kaatrin manam kamazhvathai maravene

                Munnum ithu pole puthu anubavam
                Kanden ena sollum padi ninaivile
                Innum ethirkaalathilum vazhi illai maravene} (2)

                Male : Rasaaliii.eee.. pandhayamaaaahh.. pandhayamaaahh
                Mudhalil yaar solvadhu yaar solvadhu anbai
                Mudhalil yaar eivadhu yaar Eivadhu ambai

                Male : Mounam pesamale pesamale sella
                Vaavi neeril kamalam pol aadi mella
                Kanavugal varuthe kannin vazhiye
                En thozh meethu nee
                Naan kulir kaaigindra thee

                Male : En thozh meethu nee
                Naan kulir kaaigindra thee
                Kulir kaaigindra thee..
                Kulir kaaigindra thee..""", genre= 'Tamil', duration= 330, likes= 9, play_count= 9),
         Song(name= "Only Time", creator_name= "Enya", album_id=6, lyrics= 
              """Who can say where the road goes
                Where the day flows
                Only time
                And who can say if your love grows
                As your heart chose
                Only time
                Who can say why your heart sighs
                As your love flies
                Only time
                And who can say why your heart cries
                When your love lies
                Only time
                Who can say when the roads meet
                That love might be
                In your heart
                And who can say when the day sleeps
                If the night keeps
                All your heart
                Night keeps all your heart
                Who can say if your love grows
                As your heart chose
                Only time
                And who can say where the road goes
                Where the day flows
                Only time
                Who knows
                Only time
                Who knows
                Only time""", genre= 'New Age', duration= 218, likes= 19, play_count= 34),
         Song(name= "Another Love", creator_name= "Tom Odell", album_id=7, lyrics= 
              """I wanna take you somewhere so you know I care
                But it's so cold, and I don't know where
                I brought you daffodils in a pretty string
                But they won't flower like they did last spring
                And I wanna kiss you, make you feel alright
                I'm just so tired to share my nights
                I wanna cry and I wanna love
                But all my tears have been used up
                On another love, another love
                All my tears have been used up
                On another love, another love
                All my tears have been used up
                On another love, another love
                All my tears have been used up
                Oh, ooh
                And if somebody hurts you, I wanna fight
                But my hands been broken, one too many times
                So I'll use my voice, I'll be so fucking rude
                Words, they always win, but I know I'll lose
                And I'd sing a song, that'd be just ours
                But I sang 'em all to another heart
                And I wanna cry I wanna learn to love
                But all my tears have been used up
                On another love, another love
                All my tears have been used up
                On another love, another love
                All my tears have been used up
                On another love, another love
                All my tears have been used up
                Oh, oh, oh
                (Oh, need a love, now, my heart is thinking of)
                I wanna sing a song, that'd be just ours
                But I sang 'em all to another heart
                And I wanna cry, I wanna fall in love
                But all my tears have been used up
                On another love, another love
                All my tears have been used up
                On another love, another love
                All my tears have been used up
                On another love, another love
                All my tears have been used up
                Oh, oh""", genre= 'Indie Rock', duration= 244, likes= 9, play_count= 26),
         Song(name= "No Brainer", creator_name= "Justin Bieber", album_id=8, lyrics= 
              """We the Best Music!
                Another one!
                DJ Khaled!
                You stick out of the crowd, baby, it's a no-brainer
                It ain't that hard to choose
                Him or me, be for real, baby, it's a no-brainer
                You got your mind unloose
                Go hard and watch the sun rise
                One night'll change your whole life
                Off top, drop-top, baby it's a no-brainer
                Put 'em up if you with me
                Yeah, yeah-eah, yeah, yeah-eah-eah
                In the middle, woah
                Woah-woah-oah, oh, oh-oh, ooh
                Put 'em high
                Put 'em high
                Yeah-eah-eah, yeah, yeah-eah-eah
                Both arms, yeah
                Woah-woah-oah, oh, oh-oh, ooh
                Put 'em high
                Quavo!
                Mama told you don't talk to strangers
                (Mama, mama, mama!)
                But when you're ridin' in the drop, you can't explain it
                (Skrrt, skrrt, skrrt-skrrt)
                What you been waitin' on this whole time? (Yeah)
                I blow the brains outta your mind (Ooh)
                And I ain't talking 'bout physically (No)
                I'm talking 'bout mentally (Talking 'bout mentally)
                She lookin', she look like she nasty (She lookin')
                She lookin', she look like she classy (She lookin')
                She lookin', just look at her dancing (Look at her)
                She lookin', I took her to the mansion (Yeah, yeah)
                You stick out of the crowd, baby, it's a no-brainer
                It ain't that hard to choose
                Him or me, be for real, baby, it's a no-brainer
                You got your mind unloose
                Go hard and watch the sun rise
                One night'll change your whole life
                Off top, drop-top, baby it's a no-brainer
                Put 'em up if you with me
                Yeah, yeah-eah, yeah, yeah-eah-eah
                In the middle, woah
                Woah-woah-oah, oh, oh-oh, ooh
                Put 'em high
                Put 'em high
                Yeah-eah-eah, yeah, yeah-eah-eah
                Both arms, yeah
                Woah-woah-oah, oh, oh-oh, ooh
                Put 'em high
                Don't look rich, I ain't got no chain (Huh)
                Not on the list, I ain't got no name
                But we in this bitch, bitch, I'm not no lame
                And I keep it Ben Franklin, I'm not gon' change
                Lot of these hoes is messy (Messy)
                I just want you and your bestie
                Y'all don't gotta answer for whenever you text me
                It's multiple choice and they all wanna test me
                She ch-ch-ch-ch-choosing the squad
                She tryna choose between me, Justin, Qua' and Asahd
                She told me that she love that I make music for God
                I told her I would love to see that booty applaud
                You stick out of the crowd, baby, it's a no-brainer
                It ain't that hard to choose
                Him or me, be for real, baby, it's a no-brainer
                You got your mind unloose
                Go hard and watch the sun rise
                One night'll change your whole life
                Off top, drop-top, baby it's a no-brainer
                Put 'em up if you with me
                Yeah, yeah-eah, yeah, yeah-eah-eah
                In the middle, woah
                Woah-woah-oah, oh, oh-oh, ooh
                Put 'em high
                Put 'em high
                Yeah-eah-eah, yeah, yeah-eah-eah
                Both arms, yeah
                Woah-woah-oah, oh, oh-oh, ooh
                Put 'em high""", genre= 'Hip Hop', duration= 266, likes= 4, play_count= 9),
         Song(name= "Masoom Sa", creator_name= "Sukhwinder Singh", album_id=9, lyrics= 
              """Palne me chand utra,
                Khoobsurat khwaab jaisa
                Godh mein usko uthata to
                Mujhe lagta tha waisa.


                Sara jahan mera hua
                Sara jahan mera hua
                Subah ki woh pehli dua yaa
                Phool resham ka.

                Masoom sa masoom sa
                Mere aas pass tha
                Masoom sa, mere aas pass tha
                Masoom sa.


                Ezoic
                Ek kamra tha magar,
                Sara zamana tha wahan
                Khel bhi the aur khushi thi,
                Dostana tha wahan,
                Chaar deewaron mein rehti
                Thi hazaaron mastiyan


                The wahi pat war bhi
                Sagar bhi the aur kashtiyan
                The wahi pat war bhi
                Sagar bhi the aur kashtiyan


                Meri to woh pehchan tha
                Meri to woh pehchan tha
                Ya yun kaho ki jaan tha woh
                Chand aagan ka..


                Masoom sa masoom sa
                Mere aas pass tha
                Masoom sa, mere aas pass tha
                Masoom sa.
                Masoom sa..ho masoom sa.""", genre= 'Bollywood', duration= 400, likes= 3, play_count= 19),
         Song(name= "Nandemonaiya", creator_name= "Radwimps", album_id=10, lyrics= 
              """[Verse 1]
                Futari no aida toorisugita kaze wa
                Doko kara sabishisa wo hakondekita no
                Naitari shita sono ato no sora wa
                Yake ni sukitootteitari shitanda
                Itsumo wa togatte tachichi no kotoba ga
                Kyou wa atatakaku kanjimashita
                Yasashisa mo egao mo yume no katarikata mo
                Shiranakute zenbu kimi wo maneta yo

                [Pre-Chorus]
                Mou sukoshi dake de ii ato sukoshi dake de ii
                Mou sukoshi dake de ii kara
                Mou sukoshi dake de ii ato sukoshi dake de ii
                Mou sukoshi dake kuttsuiteiyou ka

                [Chorus]
                Bokura taimufuraiyaa toki wo kakeagaru kuraima
                Toki no kakurenbo hagurekko wa mou iya nanda
                Ureshikute naku nowa kanashikute warau nowa
                Kimi no kokoro ga kimi wo oikoshitanda yo

                [Verse 2]
                Hoshi ni made negatte te ni ireta omocha mo
                Heya no sumikko ni ima korogatteru
                Kanaetai yume mo kyou de hyakko dekita yo
                Tatta hitotsu to itsuka koukanko shiyou
                Itsumo wa shaberanai ano ko ni kyou wa
                Houkago "mata ashita" to koe wo kaketa
                Narenai koto mo tama ni nara ii ne
                Toku ni anata ga tonari ni itara""", genre= 'Japanese', duration= 344, likes= 5, play_count= 7)]

with app.app_context():
    db.create_all()
    db.session.commit()
    #create admin if admin does not exist
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username= 'admin', password= 'admin', name = 'admin', is_admin= True)
        db.session.add(admin)
        db.session.commit()

    for album in albums:
        if not Album.query.filter_by(name= album.name).first():
            db.session.add(album)
            
    for song in songs:
        if not Song.query.filter_by(name= song.name).first():
            db.session.add(song)

    db.session.commit()
    