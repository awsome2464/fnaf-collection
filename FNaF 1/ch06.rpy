label how_it_went:
    $persistent.story1Chapters["ch6"] = True
    $currentStory = "FNaF"
    nvl show dissolve
    nvl clear
    narrate """
    I arrived back home.

    I still couldn't believe what had just taken place within the last 6 hours.

    That contract...

    Those animatronics...

    I still felt like I was dreaming.
    """
    nvl hide
    with dissolve
    nvl clear
    pause 1
    play music movement
    play sound door_open
    scene bg apartment_dining with longdissolve
    window show dissolve
    "I opened up the fridge to see what I could grab for a quick breakfast.{w=0.2} Or dinner, I suppose."
    macey "Good morning!"
    "I nearly jumped a foot in the air at the sudden greeting!"
    show macey straight sad blank at middle_close
    macey "Ah, sorry;{w=0.2} didn't mean to spook ya."
    mike "It's alright."
    "It's not like I haven't had my fair share of those tonight."
    macey normal smile "So, how'd it go?"
    mike "..."
    nvl show dissolve
    narrate """
    I suppose I kinda figured that this question would come up.

    But what exactly am I supposed to tell her?

    {i}\"It was great except for the robots that walk around and could possibly kill me.\"{/i}

    There's no way in Hell she'd believe me.

    She'd think I'm just trying to complain to get out working.

    Speaking of which, I should probably not mention the fact that I quit after the first shift...
    """
    nvl hide
    with dissolve
    nvl clear
    window show dissolve
    mike "It was...{w=0.5} uneventful."
    macey level "Well, I'm sure that's the best kind of night for a security guard, right?"
    mike "I guess, but it was so {i}boring{/i}!"
    "A half-truth."
    mike "I mean, I know it's a paycheck and all, but time goes really slow when you've got nothing going on around you."
    macey sad blank "I suppose that's a fair point."
    mike "I just hope things are better tonight."
    macey normal "Wait, you're actually going to go back?"
    mike "Uh, yeah...?"
    macey "Wow.{w=0.2} Usually, you give up on something the instant things don't go exactly your way. After hearing those negatives, I figured you were going to tell me you quit."
    macey smile "I'm actually pretty proud of you."
    "Why must she hurt me in this way?"
    macey level "Anyway, speaking of jobs, I better get ready for mine.{w=0.2} There's some leftover lasagna in the fridge if you want it."
    mike "Thanks."
    hide macey with dissolve
    "With that, she got ready for work while I reheated the leftovers."
    "I'm obviously going to have to break the news to her eventually."
    "But now it's going to be significantly harder."
    window hide dissolve
    stop music fadeout(5)
    pause 1
    scene bg black with longdissolve
    pause 2
    jump fnaf_night_2
