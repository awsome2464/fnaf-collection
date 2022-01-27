# Characters #####################################################################################################################################################################
define macey = Character("Macey", image="macey", what_prefix='"', what_suffix='"')
define manager = Character("Manager", image="manager", what_prefix='"', what_suffix='"')
define mike = Character("Mike", what_prefix='"', what_suffix='"')
define narrate = nvl_narrator

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

image manager = Placeholder("boy")
image mike = Placeholder("boy")

# Animations ########################################################################################################################################################################
image fnaf1_fan:
    "Backgrounds/FNaF 1 Fan/Fan 01.png"
    pause 0.05
    "Backgrounds/FNaF 1 Fan/Fan 02.png"
    pause 0.05
    "Backgrounds/FNaF 1 Fan/Fan 03.png"
    pause 0.05
    repeat

# Backgrounds #######################################################################################################################################################################

image bg black = "#000000"

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
    always:
        "fnaf1_fan"
image bg freddys_outside_day = "#c77bd0"
image bg freddys_outside_night = "#8f5a96"

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

# Audio ##############################################################################################################################################################################

# Custom Channels
init python:
    renpy.music.register_channel("sound2", "sound", loop=False)
    renpy.music.register_channel("sound3", "sound", loop=False)
    renpy.music.register_channel("ambience", "music", loop=True)

# Ambience
define audio.fnaf1_idle_ambience = "audio/ambience/fnaf1_idle_ambience.ogg"
define audio.fnaf1_office_ambience = "audio/ambience/fnaf1_office_ambience.ogg"

# Music
define audio.get_the_groove = "audio/music/Get the Groove.mp3"
define audio.happy_birthday = "audio/music/Happy Birthday.mp3"
define audio.movement = "audio/music/Movement.mp3"
define audio.round_and_round = "audio/music/Round and Round We Go.mp3"

# Sound Effects
define audio.car_approach = "audio/se/car_approach.mp3"
define audio.children_playing = "audio/se/children_playing.wav"
define audio.crowd = "audio/se/crowd.mp3"
define audio.door_close = "audio/se/door_close.mp3"
define audio.door_knock = "audio/se/door_knock.mp3"
define audio.door_open = "audio/se/door_open.mp3"
define audio.fnaf_chime = "audio/se/fnaf_chime.ogg"
define audio.manager_footsteps = "audio/se/manager_footsteps.ogg"
define audio.mike_phone = "audio/se/mike_phone.mp3"
define audio.pizza_door = "audio/se/pizza_door.mp3"

# Screens #############################################################################################################################################################################
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

# Transforms ##########################################################################################################################################################################
transform middle:
    zoom 0.67
    xalign 0.5 yalign 0.5

transform middle_close:
    zoom 1.0
    xalign 0.5 yalign 0.0

transform right:
    zoom 0.67
    xalign 1.0 yalign 0.5

# Transitions #########################################################################################################################################################################
define longdissolve = Dissolve(3.0)

# Variables ###########################################################################################################################################################################
define config.menu_include_disabled = True
default persistent.storiesUnlocked = {"FNaF": True, "GF": False, "GR": False, "FF": False, "LN": False, "SL": False, "TF": False}
default persistent.story1Chapters = {"ch1": False, "ch2": False, "ch3": False, "ch4": False}
default currentStory = None
default fnaf1OfficeXAlign = 0.5

# Labels ##############################################################################################################################################################################
label splashscreen:
    if not persistent.firstTime:
        menu:
            "WARNING: This game contains mature content."
            "Okay.":
                $persistent.firstTime = True
    return

label start:
    menu:
        "Five Nights at Freddy's":
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

        "Back":
            jump start

    return
