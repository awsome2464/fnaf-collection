define macey = Character("Macey", what_prefix='"', what_suffix='"')
define mike = Character("Mike", what_prefix='"', what_suffix='"')
define narrate = nvl_narrator

define config.menu_include_disabled = True
default persistent.storiesUnlocked = {"FNaF": True, "GF": False, "GR": False, "FF": False, "LN": False, "SL": False, "TF": False}

# Character Images
image macey = Placeholder("girl")
image mike = Placeholder("boy")

# Backgrounds

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
        "Back":
            jump start

    return
