#####################################################################################################################################################################################
## Cole Goodrich's FNaF Story Collection                                                                                                                                           ##
## Please use this code for inspirational and educational purposes rather than directly copying and pasting.                                                                       ##
#####################################################################################################################################################################################

# Transitions #######################################################################################################################################################################
define eyesclose = ImageDissolve(image="Blinking.png", time=2, ramplen=64)
define fastblinkclose = ImageDissolve(image="Blinking.png", time=0.1, ramplen=256, reverse=False)
define fastblinkopen = ImageDissolve(image="Blinking.png", time=0.1, ramplen=256, reverse=True)
define longdissolve = Dissolve(3.0)
define monitoroff = ImageDissolve(image="Monitor On.png", time=0.2, reverse=True)
define monitoron = ImageDissolve(image="Monitor On.png", time=0.2)

# Transforms ########################################################################################################################################################################
transform camera_pan:
    xalign 0.0
    pause 2
    linear 5.0 xalign 1.0
    pause 2
    linear 5.0 xalign 0.0
    repeat

transform middle:
    zoom 0.67
    xalign 0.5 yalign 0.5

transform middle_close:
    zoom 1.0
    xalign 0.5 yalign 0.0

transform overlay:
    xalign 0.5 yalign 0.5

transform right:
    zoom 0.67
    xalign 1.0 yalign 0.5

transform sceneblur:
    xalign 0.5 yalign 0.5
    blur 10

# Styles #########################################################################################################################################################################
style camtext:
    font "fonts/Pixel Digivolve.otf"
    text_align 0.5
    size 50

style splash:
    font "fonts/Typo.ttf"
    size 50
    color "#ffffff"
    text_align 0.5
    justify True
    layout "subtitle"

# Characters #####################################################################################################################################################################
define alice = Character("Alice", image="alice", what_prefix='"', what_suffix='"')
define baby = Character("Baby", image="baby", what_prefix='"', what_suffix='"', what_italic=True)
define ballora = Character("Ballora", image="ballora", what_prefix='"', what_suffix='"', what_italic=True)
define bonbon = Character("Bon-Bon", image="bonbon", what_prefix='"', what_suffix='"', what_italic=True)
define carmen = Character("Carmen", image="carmen", what_prefix='"', what_suffix='"')
define chuck = Character("Chuck", image="chuck", what_prefix='"', what_suffix='"')
define cleo =  Character("Cleo", what_prefix='"', what_suffix='"', what_italic=True)
define clara =  Character("Clara", image="clara", what_prefix='"', what_suffix='"', what_italic=True)
define cop = Character("Cop", image="cop", what_prefix='"', what_suffix='"')
define courtney = Character("Courtney", image="courtney", what_prefix='"', what_suffix='"')
define eric = Character("Eric", image="eric", what_prefix='"', what_suffix='"')
define fun_freddy = Character("Funtime Freddy", image="funtime_freddy", what_prefix='"', what_suffix='"', what_italic=True)
define guy = Character("Guy", image="guy", what_prefix='"', what_suffix='"')
define jack = Character("Jack", image="jack", what_prefix='"', what_suffix='"')
define jacob = Character("Jacob", image="jacob", what_prefix='"', what_suffix='"')
define jamie = Character("Jamie", image="jamie", what_prefix='"', what_suffix='"')
define jane = Character("Jane", image="jane", what_prefix='"', what_suffix='"')
define jasmine = Character("Jasmine", image="jasmine", what_prefix='"', what_suffix='"')
define jeremy = Character("[jName]", image="jeremy", what_prefix='"', what_suffix='"')
define kenzie = Character("Kenzie", image="kenzie", what_prefix='"', what_suffix='"')
define macey = Character("Macey", image="macey", what_prefix='"', what_suffix='"')
define manager = Character("Manager", image="manager", what_prefix='"', what_suffix='"')
define me = Character("Me", what_prefix='"', what_suffix='"')
define mike = Character("Mike", image="mike", what_prefix='"', what_suffix='"')
define morado = Character("[mName]", image="morado", what_prefix='"', what_suffix='"')
define mr_fitz = Character("Dad", image="mr_fitz", what_prefix='"', what_suffix='"')
define mr_schmidt = Character("Dad", image="mr_schmidt", what_prefix='"', what_suffix='"')
define mrs_fitz = Character("Mom", image="mrs_fitz", what_prefix='"', what_suffix='"')
define mrs_schmidt = Character("Mom", image="mrs_schmidt", what_prefix='"', what_suffix='"')
define narrate = nvl_narrator
define phone = Character("[pgName]", what_prefix='"', what_suffix='"', what_italic=True)
define plushtrap = Character("[ptName]", what_prefix='"', what_suffix='"', what_italic=True)
define tyler = Character("Tyler", image="tyler", what_prefix='"', what_suffix='"')
define vlad = Character("Vlad", image="vlad", what_prefix='"', what_suffix='"', what_italic=True)

# Character Images ################################################################################################################################################################
layeredimage macey:
    always:
        "Characters/Macey/MaceyBase.png"
    group mouth:
        attribute blank:
            "Characters/Macey/MaceyMouthBlank.png"
        attribute smile:
            "Characters/Macey/MaceyMouthSmile.png"
    group eyes:
        attribute straight:
            "Characters/Macey/MaceyEyesStraight.png"
        attribute left:
            "Characters/Macey/MaceyEyesLeft.png"
        attribute right:
            "Characters/Macey/MaceyEyesRight.png"
    group eyebrows:
        attribute mad:
            "Characters/Macey/MaceyEyebrowsMad.png"
        attribute sad:
            "Characters/Macey/MaceyEyebrowsSad.png"
        attribute level:
            "Characters/Macey/MaceyEyebrowsLevel.png"
        attribute raised:
            "Characters/Macey/MaceyEyebrowsRaised.png"
        attribute normal:
            "Characters/Macey/MaceyEyebrowsNormal.png"

layeredimage manager:
    always:
        "Characters/Manager/ManagerBase.png"
    group mouth:
        attribute frown:
            "Characters/Manager/ManagerMouthFrown.png"
        attribute smile:
            "Characters/Manager/ManagerMouthSmile.png"
    group eyebrows:
        attribute normal:
            "Characters/Manager/ManagerEyebrowsNormal.png"
        attribute mad:
            "Characters/Manager/ManagerEyebrowsMad.png"
        attribute sad:
            "Characters/Manager/ManagerEyebrowsSad.png"

image mike = Placeholder("boy")

# Animations ########################################################################################################################################################################
image camera_static:
    size(1920, 1080)
    alpha 0.2
    "Animations/Camera Static/01.png"
    pause 0.05
    "Animations/Camera Static/02.png"
    pause 0.05
    "Animations/Camera Static/03.png"
    pause 0.05
    "Animations/Camera Static/04.png"
    pause 0.05
    "Animations/Camera Static/05.png"
    pause 0.05
    "Animations/Camera Static/06.png"
    pause 0.05
    "Animations/Camera Static/07.png"
    pause 0.05
    "Animations/Camera Static/08.png"
    pause 0.05
    repeat

image fnaf1_fan:
    "Animations/FNaF 1 Fan/Fan 01.png"
    pause 0.05
    "Animations/FNaF 1 Fan/Fan 02.png"
    pause 0.05
    "Animations/FNaF 1 Fan/Fan 03.png"
    pause 0.05
    repeat

image recording:
    zoom 1.5
    alpha 1.0
    "Recording.png"
    pause 0.5
    linear 0.0 alpha 0.0
    pause 0.5
    linear 0.0 alpha 1.0
    repeat

image title:
    "gui/main_menu.png"
    choice:
        pause 1.5
    choice:
        pause 1.5
    choice:
        pause 2.5
    choice:
        pause 2.5
    choice:
        pause 0.5
    choice:
        pause 0.5
    choice:
        "Title/Circus Baby.png"
        pause 0.25
        "gui/main_menu.png"
        pause 0.5
    choice:
        "Title/Freddy.png"
        pause 0.25
        "gui/main_menu.png"
        pause 0.5
    choice:
        "Title/Golden Freddy.png"
        pause 0.25
        "gui/main_menu.png"
        pause 0.5
    choice:
        "Title/Nightmare Fredbear.png"
        pause 0.25
        "gui/main_menu.png"
        pause 0.5
    choice:
        "Title/Scrap Baby.png"
        pause 0.25
        "gui/main_menu.png"
        pause 0.5
    choice:
        "Title/Springtrap.png"
        pause 0.25
        "gui/main_menu.png"
        pause 0.5
    choice:
        "Title/Toy Freddy.png"
        pause 0.25
        "gui/main_menu.png"
        pause 0.5
    repeat

# Backgrounds #######################################################################################################################################################################

image bg black = "#000000"
image bg white = "#ffffff"

# FNaF
image bg apartment_dining = "#007021"
image bg apartment_tv = "#007cc6"
image bg freddys_dining_day = "#6b30a4"
image bg freddys_dining_night = "#3d1b5e"
image bg freddys_leftdoor = "#102e22"
image bg freddys_lefthall = "#623a3a"
image bg freddys_manager = "#004a52"
layeredimage bg freddys_office:
    always:
        "Backgrounds/FNaF 1 Office Empty.png"
    group lights:
        attribute left_empty:
            "Backgrounds/FNaF 1 Office Left Empty.png"
        attribute left_bonnie:
            "Backgrounds/FNaF 1 Office Left Bonnie.png"
        attribute right_empty:
            "Backgrounds/FNaF 1 Office Right Empty.png"
        attribute right_chica:
            "Backgrounds/FNaF 1 Office Right Chica.png"
    always:
        "fnaf1_fan"

image bg freddys_outside_day = "#c77bd0"
image bg freddys_outside_night = "#8f5a96"

image cam freddys_dining bon:
    zoom 1.5
    choice:
        "Backgrounds/FNaF 1 Dining Bonnie 01.png"
    choice:
        "Backgrounds/FNaF 1 Dining Bonnie 02.png"
image cam freddys_dining chica:
    zoom 1.5
    choice:
        "Backgrounds/FNaF 1 Dining Chica 01.png"
    choice:
        "Backgrounds/FNaF 1 Dining Chica 02.png"
image cam freddys_dining default:
    zoom 1.5
    "Backgrounds/FNaF 1 Dining Default.png"
image cam freddys_pas bonnie:
    zoom 1.5
    "Backgrounds/FNaF 1 PaS Bonnie.png"
image cam freddys_pas default:
    zoom 1.5
    "Backgrounds/FNaF 1 PaS Default.png"
image cam freddys_piratecove_01:
    zoom 1.5
    "Backgrounds/FNaF 1 Pirate Cove 01.png"
image cam freddys_restroom chica:
    zoom 1.5
    choice:
        "Backgrounds/FNaF 1 Restrooms Chica 01.png"
    choice:
        "Backgrounds/FNaF 1 Restrooms Chica 02.png"
image cam freddys_restroom default:
    zoom 1.5
    "Backgrounds/FNaF 1 Restrooms Default.png"
image cam freddys_stage nobon:
    zoom 1.5
    "Backgrounds/FNaF 1 Stage NoBon.png"
image cam freddys_stage default:
    zoom 1.5
    "Backgrounds/FNaF 1 Stage Default.png"
image cam freddys_stage freddy:
    zoom 1.5
    "Backgrounds/FNaF 1 Stage Freddy.png"

# CGs ################################################################################################################################################################################

image cg fnaf_daytime_performance = "CGs/FNaF Daytime Performance.png"
image cg fnaf_nighttime_performance = "CGs/FNaF Nighttime Performance.png"
image cg help_wanted = "CGs/Help Wanted.png"

# Misc Images ########################################################################################################################################################################        
image fnaf_nose_honk_idle:
    alpha 0.0
    "#ffffff"
    size(31, 17)
image fnaf_nose_honk_hovered:
    alpha 0.0
    "#ffffff"
    size(31, 17)
image splashtext = ParameterizedText(style="splash")

# Audio ##############################################################################################################################################################################

# Custom Channels
init python:
    renpy.music.register_channel("ambience", "music", loop=True)
    renpy.music.register_channel("ambience2", "music", loop=True)
    renpy.music.register_channel("kitchen", "sound", loop=False)
    renpy.music.register_channel("sound2", "sound", loop=False)
    renpy.music.register_channel("sound3", "sound", loop=False)

# Ambience
define audio.fnaf1_cam_noise = "audio/ambience/fnaf1_cam_noise.ogg"
define audio.fnaf1_idle_ambience = "audio/ambience/fnaf1_idle_ambience.ogg"
define audio.fnaf1_moving_ambience = "audio/ambience/fnaf1_moving_ambience.ogg"
define audio.fnaf1_office_ambience = "audio/ambience/fnaf1_office_ambience.ogg"

# Music
define audio.get_the_groove = "audio/music/Get the Groove.mp3"
define audio.happy_birthday = "audio/music/Happy Birthday.mp3"
define audio.movement = "audio/music/Movement.mp3"
define audio.music_box = "audio/music/Music Box.ogg"
define audio.night_stalker = "audio/music/Night Stalker.mp3"
define audio.round_and_round = "audio/music/Round and Round We Go.mp3"

# Sound Effects
define audio.blip = "audio/se/blip.wav"
define audio.cam_down = "audio/se/cam_down.wav"
define audio.cam_up = "audio/se/cam_up.wav"
define audio.car_approach = "audio/se/car_approach.mp3"
define audio.children_playing = "audio/se/children_playing.wav"
define audio.crowd = "audio/se/crowd.mp3"
define audio.door_close = "audio/se/door_close.mp3"
define audio.door_knock = "audio/se/door_knock.mp3"
define audio.door_light = "audio/se/door_light.ogg"
define audio.door_open = "audio/se/door_open.mp3"
define audio.fnaf_chime = "audio/se/fnaf_chime.ogg"
define audio.fnaf_footsteps = "audio/se/fnaf_footsteps.wav"
define audio.fnaf_phone_hangup = "audio/se/fnaf_phone_hangup.ogg"
define audio.fnaf_phone_pickup  = "audio/se/fnaf_phone_pickup.ogg"
define audio.fnaf_phone_pickup_short = "audio/se/fnaf_phone_pickup_short.ogg"
define audio.fnaf_phone_ring = "audio/se/fnaf_phone_ring.ogg"
define audio.manager_footsteps = "audio/se/manager_footsteps.ogg"
define audio.mike_phone = "audio/se/mike_phone.mp3"
define audio.paper_phone = "audio/se/paper_phone.ogg"
define audio.paper_rip = "audio/se/paper_rip.mp3"
define audio.phone_guy_throat = "audio/se/phone_guy_throat.ogg"
define audio.pizza_door = "audio/se/pizza_door.mp3"

# Screens #############################################################################################################################################################################
screen ambient_sounds():
    if currentStory == "FNaF":
        timer circusTimer repeat True action [Play("ambience2", "audio/ambience/circus.ogg", None, loop=False), SetVariable("circusTimer", renpy.random.choice([60, 120, 180]))]

screen cam_feed():
    if currentCam != "bg black":
        add "cam [currentCam]" at camera_pan
    else:
        add "bg black"
    if currentCam != "bg black":
        add "camera_static"
    add "Camera Border.png" size(1920, 1080)
    add "recording" xalign 0.03 yalign 0.05
    if currentCam == "bg black":
        text "CAMERA DISABLED\nAUDIO ONLY" style "camtext" xalign 0.5 yalign 0.05

screen nose_honk():
    if currentStory == "FNaF":
        if fnaf1OfficeXAlign == 0.5:
            imagebutton auto "fnaf_nose_honk_%s":
                pos(655, 335)
                action Play("sound", "audio/se/nose_honk.ogg")
        elif fnaf1OfficeXAlign == 0.0:
            imagebutton auto "fnaf_nose_honk_%s":
                pos(848, 335)
                action Play("sound", "audio/se/nose_honk.ogg")
        elif fnaf1OfficeXAlign == 1.0:
            imagebutton auto "fnaf_nose_honk_%s":
                pos(463, 335)
                action Play("sound", "audio/se/nose_honk.ogg")

# Variables ###########################################################################################################################################################################
define config.menu_include_disabled = True
default persistent.storiesUnlocked = {"FNaF": True, "GF": False, "GR": False, "FF": False, "LN": False, "SL": False, "TF": False}
default persistent.story1Chapters = {"ch1": False, "ch2": False, "ch3": False, "ch4": False, "ch5": False, "ch6": False, "ch7": False, "ch8": False}
default circusTimer = renpy.random.choice([60, 120, 180])
default currentCam = "freddys_stage default"
default currentStory = None
default fnaf1OfficeXAlign = 0.5
default fnafAmbientSongChance = 0
default jName = "Hobo"
default kitchen = 0
default mName = "Manager"
default pgName = "???"
default ptName = "???"

# Labels ##############################################################################################################################################################################
label splashscreen:
    play music "audio/music/Title Intro.ogg"
    pause 0.5
    show splashtext "{color=#db0000}{size=+20}Notice:{/size}{/color}\nThe following is a collection of {color=#db0000}fan made stories{/color} that have no affiliation with Scott Cawthon or the Five Nights at Freddy's brand.\n\nThese stories also contain mature themes and content and are {color=#db0000}intended for mature audiences{/color}." at truecenter with longdissolve
    pause 5
    hide splashtext with longdissolve
    pause 1
    return

label before_main_menu:
    play sound "audio/se/static.wav"
    return

label start:
    menu:
        "Five Nights at Freddy's":
            stop music fadeout(3)
            jump fnaf_options
        "The Golden Freddy" if persistent.storiesUnlocked["GF"]:
            pass
        "Grand Reopening" if persistent.storiesUnlocked["GR"]:
            pass
        "Fazbear Fright" if persistent.storiesUnlocked["FF"]:
            pass
        "Living Nightmares" if persistent.storiesUnlocked["LN"]:
            pass
        "Sister Location" if persistent.storiesUnlocked["SL"]:
            pass
        "The Finale" if persistent.storiesUnlocked["TF"]:
            pass
    return

label fnaf_options:
    menu:
        "Five Nights at Freddy's"
        "Read Story":
            jump getting_a_job
        "Chapter Select" if persistent.story1Chapters["ch1"]:
            menu:
                "Getting a Job":
                    jump getting_a_job
                "Interview" if persistent.story1Chapters["ch2"]:
                    jump interview
                "Orientation" if persistent.story1Chapters["ch3"]:
                    jump orientation
                "Night 1" if persistent.story1Chapters["ch4"]:
                    jump fnaf_night_1
                "Confrontation" if persistent.story1Chapters["ch5"]:
                    jump confrontation
                "How it Went" if persistent.story1Chapters["ch6"]:
                    jump how_it_went
                "Night 2" if persistent.story1Chapters["ch7"]:
                    jump fnaf_night_2
                "Research" if persistent.story1Chapters["ch8"]:
                    pass

        "Back":
            jump start

    return

# Common Events

# FNaF
label fnaf_cam_up(startingCam):
    window hide dissolve
    $currentCam = startingCam
    play sound2 cam_up
    queue sound2 fnaf1_cam_noise loop
    scene bg white with monitoron
    show screen cam_feed
    hide screen nose_honk
    return

label fnaf_cam_down:
    play sound2 cam_down
    show screen nose_honk
    hide screen cam_feed
    scene bg freddys_office with monitoroff
    window show dissolve
    return

label fnaf_cam_switch(newCam):
    $currentCam = newCam
    play sound2 blip
    return

label fnaf_kitchen:
    if renpy.get_screen("cam_feed"):
        $renpy.music.set_volume(volume=1.0, channel="kitchen")
        $renpy.music.set_pan(pan=0, delay=0, channel="kitchen")
    else:
        $renpy.music.set_volume(volume=0.25, channel="kitchen")
        $renpy.music.set_pan(pan=1, delay=0, channel="kitchen")

    $kitchen = renpy.random.randint(1,4)

    if kitchen == 1:
        play kitchen "audio/se/kitchen_01.wav"
    elif kitchen == 2:
        play kitchen "audio/se/kitchen_02.wav"
    elif kitchen == 3:
        play kitchen "audio/se/kitchen_03.wav"
    elif kitchen == 4:
        play kitchen "audio/se/kitchen_04.wav"
    return
