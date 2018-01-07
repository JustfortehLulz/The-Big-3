# The script of the game goes in this file.

### https://docs.google.com/document/d/180n5TEu1NCGBvrj-0DUVwJsbXUUeACyrNRCwimkfGRM/edit

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# Can also define images here such as expressions and pictures

### MAIN CHARACTERS
define s = Character("Simon", color = "#ff0000")

define j = Character("Johnston", color = "#2600ff")
### pictures 446 x 753

define prof = Character("Professor", color = "#878787")


# The game starts here.

label start:


    ### intialize all variables under the start label
    $ jpoints = 0
    $ spoints = 0
    $ ensc1First = False
    $ bus1First = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    ############# TEST IMAGES AND BACKGROUNDS ################
    ############# TEST IMAGES AND BACKGROUNDS ################
    
    scene bg check

    ############# TEST IMAGES AND BACKGROUNDS ################
    ############# TEST IMAGES AND BACKGROUNDS ################

    "What is your name?"

    $ playerName = renpy.input("What is your name?")

    $ playerName = playerName.strip()

    if playerName == "":
        $ playerName = "Christine"

    define mc = Character("[playerName]", color = "#d780f2")

    define mom = Character("[playerName]'s Mom", color = "#f8afff")

    ### play musics plays it
    ### queue waits until current song is done playing can take fadeout
    ### to play the next song in the queue
    ### stop statement stops the current song can take fadeout
    ### sounds only play once and can multiple can be queued up
    
    ###play music "Lose Yourself.mp3" fadeout 1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    ### can shift the picture using xalign and yalign
    

    # These display lines of dialogue.
####################### ACT 1 ####################
### beginning of day in act 1

    ### Bedroom picture

    scene bg bedroom
    with fade

    "Today marks the day when I start my attendance at Dancuck University. Just graduated from high school, and attending such a low-class university, I’m honestly so ashamed."

    "But...  It’s my fault anyway for not taking my classes in high school as seriously as I should have."

    mc "\"I can’t believe I’m actually going to this school...\""

    "*sigh*"

    ". . ."

    "And perfect."

    "Can't slack off on my morning routine, now."
    "No matter how bad my school situation looks, I'm gonna give it my all now!"

    ### Kitchen picture

    scene bg kitchen 
    with fade

    mom "\"Have a nice day, [playerName]!\""

    mc "\"Bye, mom!\""

    ### Streets picture
    scene bg streets
    with fade

    "As I got on the train towards my new university, my mind wandered about my current situation, something that I found myself doing more often than not these days."

    "I mean, not only am I new in school, I’m also new to this whole town… One month isn’t enough to adapt."

    "It feels alien at best and without my friends, I just feel… alone. But you know what? I think I’ll do great! I’ll make some great friends here! I just know it."

    ### Arrives at school picture
    scene bg school
    with fade
    "Wow… This place looks so much better than I expected."

    "Heh, don’t get too excited now, [playerName]. You’ve heard the stories of this place."

    "It’s beautiful, but… This school isn’t the lowest rated university for nothing."

    ". . ."

    "Eek!"

    "It’s 9:28 already! Oh god, where is my class?"

    "A campus map! Okay, okay, okay..."


menu:

    "Wait, what even is my first class?"

    "Engineering Class":
        jump Engineering

    "Business Class":
        jump Business

    "The Gym":
        jump Class3

label Engineering:
    
    ### changing dialogue depending on which class was first
    ### changing dialogue depending on which class was first
    $ ensc1First = True


    "Ah, right! Engineering!"
    $ name = str(playerName)
    $ b = str.upper(name)
    "RUN, [b], RUN!"

    ### Inside the class picture
    scene bg classroom
    with fade

    prof "\"Okay, all of you, let’s get started!\""

    prof "\"I know most of you are first years, so let’s go over some things . . .\""

    "Ugh, all this first year introduction nonsense."

    "All this information is so basic, even for me… Okay, this is an engineering class, it’s not going to be easy. Let’s get some of this down."

    "Open up the notebook, pen out. Info down on paper… Wait, what’s the first reading?"

    "That was the exam date wasn’t it?"

    "Why is this prof talking so fast?!?!"

    "Ahhhh!!"

    scene bg black 
    with wiperight
    ### Black screen picuture
    "Okay, MC, calm down."

    "This is university. This is all new."

    "Maybe this is just the level of challenge we have to step up to."

    "So let’s do it. Reset. Breath. Okay."

    ### Inside the class picture
    scene bg classroom
    with wipeleft

    prof "\"...And your second TA for this semester, if you’ll look to the front here. Johnston Yang!\""

    "Girls" "Ahhhh!\nOh my god!\nLook at him!"

    mc "\"Huh?\""

    j "\"Hey, everyone, as you heard, it’s me, Johnston Yang.\""

    show johnston2:
        xalign 1.0
        yalign 1.0
        zoom 0.50

    j "\"I’m currently doing my fourth year, but even though I’ll seem busy…\""
    j "\"I look forward to being your TA, so don’t disappoint me!\""


    "Whoa, a fourth year TA. Isn’t that a little unusual?"
    "Sounds like he became a TA really early. But something is just a little weird here. Something I just can’t seem to -"

    "Girl 1" "\"He seems to be a little too… mature. I mean, like for a fourth year, you know!\""

    "Girl 2" "\"Ha ha, he does seem to be pretty old. But, does it matter though? He’s actually hot as fuck!\""

    "Girl 1" "\"Mmmm, I know, right?\""

    j "\"And that’ll be all from me. Turning it back to your great ol’ prof.\""

    hide johnston2

    "Oh, god."

    "Yep, that was it. The other guys in this engineering class are all so plain, it’s no wonder this TA stood out so much."

    "Heh heh, I guess now I have a reason to pay attention. With how difficult this class is going to be, I’m going to ne- wait, why is he coming this way?!"

    "OH MY GOD."

    "Why, why did I have to be almost late to this class?! Why- my cheeks, oh my, why is this happening to me?"

    "Why is he sitting here?! Why-"

    ### move character right to left or something

    show johnston2:
        xalign 0.0
        yalign 1.0
        zoom 0.50
        linear 2.0 xalign 1.0 

    j "\"Um, excuse me, miss. Are you alright?\""

    j "\". . .\""

    j "\"Hello?\""

    mc "\"Huh? Oh yeah, I'm just fine!\""

    mc "\"Nothing wrong here, ha ha!\""

    "Fuck"

    "That was so awkward. One of my first classes in university and I run into a guy like this!"

    "Such an attractive guy sitting next to me. He might be a TA all but... I really needed some more practice before this."

    "I hope he doesn't think I'm weird."

    j "\"Well, if you say so.\""

    j "\"I know how daunting these classes can be for a first years with how hard they are and all.\""

    j "\"Ah, you are a first year, right?\""



###################################################
menu:

    "Yes, yes, I’m a first year! Let’s see, how to say this?"

    "Joke about your youth":
        mc "\"Yes, I am. Did my youthful looks make it too obvious?\""
        j "\"Hm, well, yeah. I guess you do look pretty young.\""
        mc "\"Ha ha, of course. My friends always said that I looked young and cute for my age.\""
        j "\"Nice to know you don’t have liars for friends.\"" 

        "Ah! He thinks I'm cute!"

        $ jpoints += 1
        
    "Straight Answer":
        mc "\"Yes, I am. First year, and it’s my first day today as well!\""
        j "\"Of course, it would be the first day for every first year here as well.\""
        j "\"I hope your first day’s gone well enough.\""
        mc "\"Thanks! It hasn’t been too bad actually.\""

    "Joke about the age difference":
        mc "\"Yeah! It's easy for to tell, isn't it?\""
        j "\"It wasn't too hard.\""
        mc "\"As expected from a fourth year TA! You know what they say, with age comes wisdom!\""
        mc "\"I wish I was old enough to have your smarts!\""
        j "\"I'm only fourth year, you know... Not that old.\""
        mc "\"Ah, right, right!\""

        $ jpoints -= 1

label afterMenuensc:

    prof "\"With that, I'm going to conclude our first class.\""

    prof "\"Make sure you guys do your readings before the next one.\""

    prof "\"And of course, welcome to Engineering 101!\""

    j "\"Well, I hope you were paying attention to all of that, Ms. um, what was your name?\""

    mc "\"I'm [playerName]. It was nice to meet you, Mr. Yang!\""

    j "*heh* \"Please, just call me Johnston. It was nice to meet you as well, [playerName].\""

    j "\"Maybe we'll see each other next class. Have a nice day, [playerName]\""

    mc "\"You too. See ya!\""

    hide johnston2

################ Hallway BG ################
    
    scene bg hallway 
    with fade

    "I'm glad the TA there seems great."

    "But... What was the prof talking about again?"

    ### making sure you get the correct amount of points from an option
    if jpoints == 1:
        "j [jpoints]"
    elif jpoints == -1:
        "j [jpoints]"
    elif jpoints == 0:
        "j [jpoints]"


    if (not bus1First):
        "THROUGH IF STATEMENT TO BUSINESS"
        jump Business

    #### jump to end of day code here

label Business:
    $ bus1First = True
    #if !(ensc1First):


    ### changing dialogue depending on which class was first
    ### changing dialogue depending on which class was first

    ### inside classroom picture
    scene bg classroom
    with fade

    "I made it!"
    "But this business class is pretty full..."
    "What the heck was that snicker?"

    "Wow, what's that guy's problem?"
    "He's actually pretty cute, if only he didn't look like such a dick"
    "With that thought, time to find a seat. Preferably, away from him {b}and{/b} the professor."
    "Oh no... That was definitely from the professor. Oh my God, first day and I'm already stepping on the wrong toes."
    "..."

    prof "\"Miss [playerName] where do you think you're going?\""

    "Why does everyone feel the need to look at me. It's already plenty embarrassing enough, thank you very much. Ugh, my throat feels so dry."

    mc "\"I-I was just going to find a seat.\""

    prof "\"I guess you didn't read the e-mail that I sent you beforehand. Well, seeing as though you are all too important to read up on the classes you're taking, I'll just have to spoon feed it to you.\""
    prof "\"I have already assigned the seats, and you are sitting beside Mister Pan over there\""

    "Do you remember those moments in the movies where you see the main character slowly turn in horror then find out about a horrifying moment?"
    "Yeah, this was one of those moments."
    "I hate this class."
    "I hate this professor."
    #Black screen picture
    scene bg black
    with wipeleft
    "I have to admit, with much regret, the professor actually knew how to teach and was somewhat easy to follow."
    "Now if only he didn’t glare at me like I was the spawn of Hell every other second, he would be perfect."

    "My new seatmate, on the other hand, was a bundle of joy."

    "I mean, I already made a mistake, does he have to remind me by laughing throughout the lecture?"

    "Alright, as soon as the professor dismisses us, I’ll make a break for it."

    scene bg classroom
    with wiperight

    "Wow, does this guy {b}not know{/b} personal boundaries? He does have soft hands though… Not that I noticed or anything!"
    "Maybe a glare would send a message."

    s "\"Yo, calm down girl! Calm your tits!\""

    "What?"
    "Oookay?"

    mc "\"Umm, ok...\""

    s "\"Name's Simon, guess we're stuck together now, eh?\""

    menu:
        "I don't really want to give him my name..."

        "Give him your name":
            
            mc "\"It's [playerName], if you weren't listening earlier.\""
            ##########################################
            s "\"Oh, so you're one of those girls\""
            s "\"Ayt,ayt, it's cute how you run your mouth.\""
            s "\"Maybe chill out next time we meet. I'll make this class fun for both of us.\""
            $ spoints += 1

        "Smile uncomfortably":
            
            mc "\"...\""
            mc "\"That's nice?\""
            s "\"Oh I see how it is,cool cool.\""
            s "\"Trust me, you'll see the benefits in being my friend\""
            s "\"I mean, at least try not to be a bitch all semester. See ya around\""
            $ spoints -= 1

    label afterMenuBus:

        "That was... incredibly random. Well, that's a great preview of this semester. I bet things are gonna be soooo fuuun..."
        "Ughh..."

    if (not ensc1First):
        "THROUGH IF STATEMENT TO ENGINEERING"
        jump Engineering


    #### jump to end of day code here



label Class3:
    
    mc "God damn."
    mc "How did I end up walking to the gym?"
    mc "I'll just drink those vegan protein shakes"
    jump end

label end:

    mc "im gay"
    scene bg bedroom
    with fade

    "End"

    return
    # This ends the game.
