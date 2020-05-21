#Characters
define c = Character("") #narrator
define p = Character("player_name", dynamic=True)
define player_name = ""
define m = Character("mascot_name", dynamic=True)
define mascot_name = "XXXX"

#Background Images
image white = "#FFF"

#Love Scene Variables ------------------------------------
image bg desert_bw = "love/bw.png"
image bg desert_med = "love/pink.png"
image bg desert_color ="love/pink_yellow.png"

image lizard_bw = "love/lizard-bw.png"
image lizard_color = "love/lizard-color.png"

image stones1_bw = "love/stones1-bw.png"
image stones1_color = "love/stones1-color.png"

image stones2_bw = "love/stones2-bw.png"
image stones2_color = "love/stones2-color.png"

image stick_bw = "love/stick-bw.png"
image stick_color = "love/stick-color.png"

image cactii_bw = "love/cactii-bw.png"
image cactii_color = "love/cactii-color.png"

define love = 0  # values are 0, 1 and 2.

define ouch.ost = "audio/ouch.mp3"


#Object Buttons

#Madlibs Variables
define colorz = ""
define scary_object = ""

#Music


label splashscreen:

    scene black
    with Pause(1)

    show text "Abigail Zhong and Katie Borg present..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "SoundScape" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:

    c "..."
    c "You feel strange, almost as if in a dream."
    c "Everything is {b}unusually quiet{/b} and eerily still."
    c "But that didn’t bother you, in fact, you felt {b}apathetic{/b} about it."
    c "You open your eyes and are greeted with the sight of…"

    scene bg desert_bw with Pause(3):
        subpixel True
        xalign 0.5
        yalign 0.0
        linear 3.0 yalign 1.0

    c "You are not sure if this is what the world was supposed to look like."
    c "Something felt off, but you didn’t let your mind linger on it."
    c "You know you should feel confused but…"
    c "{b}You don’t really feel much at all.{/b}"
    c "'Let’s explore this area and maybe I will have a better idea of where I am,' you tell yourself."

    screen ImageMenu
    # imagebutton auto "cactii-bw_%s.png" action Play("sound", ouch.ost)

    $ boolean = True
    while boolean:
        menu:
            "Look to the left.":
                $ boolean = False
                scene bg desert_bw with Pause(3):
                    subpixel True
                    yalign 1.0
                    xalign 0.5
                    linear 3.0 xalign 0.0

                show lizard_bw with dissolve:
                    xpos 80 ypos 400

                show stones2_bw with Pause(1.5):
                    xpos 730 ypos 300

                c "I wonder what these objects do?"
                c "They don't make a {b}sound{/b}."


            "Look to the right":
                $ boolean = False
