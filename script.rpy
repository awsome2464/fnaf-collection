define macey = Character("Macey", image="macey", what_prefix='"', what_suffix='"')
define mike = Character("Mike", what_prefix='"', what_suffix='"')
define narrate = nvl_narrator

define config.menu_include_disabled = True
default persistent.storiesUnlocked = {"FNaF": True, "GF": False, "GR": False, "FF": False, "LN": False, "SL": False, "TF": False}
default persistent.story1Chapters = {"ch1": False, "ch2": False}

# Character Images
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

image mike = Placeholder("boy")

# Backgrounds

image bg black = "#000000"

# FNaF
image bg apartment_dining = "#007021"
image bg apartment_tv = "#007cc6"

label splashscreen:
    if not persistent.firstTime:
        menu:
            "WARNING: This game contains mature content."
            "Okay.":
                $persistent.firstTime = True
    return

# CGs

image cg help_wanted = "CGs/Help Wanted.png"

# Audio

# Music
define audio.movement = "audio/Music/Movement.mp3"

# Sound Effects
define audio.door_close = "audio/se/door_close.mp3"
define audio.shower = "<loop 3>audio/se/shower.mp3"

# Transforms
transform middle:
    zoom 0.67
    xalign 0.5 yalign 0.5

transform middle_close:
    zoom 1.0
    xalign 0.5 yalign 0.0

transform right:
    zoom 0.67
    xalign 1.0 yalign 0.5

# Transitions
define longdissolve = Dissolve(3.0)

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

        "Back":
            jump start

    return
