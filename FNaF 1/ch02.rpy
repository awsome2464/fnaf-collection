label interview:
    $currentStory = "FNaF"
    "{i}The next day...{/i}"
    play sound mike_phone
    pause 5
    stop sound
    mike "Hello?"
    "???" "\"Yes, hello.{w=0.2} Is this Mike Schmidt?\""
    mike "It is."
    "???" "\"I'm the manager at Freddy Fazbear's Pizza.{w=0.2} I was calling to see if you were still interested in the security guard position.\""
    mike "I am, indeed."
    manager "Perfect!{w=0.5} Then I would like to set up an interview with you tomorrow afternoon.{w=0.2} Is there a time that would work best for you?"
    mike "Any time would be great!"
    manager "Wonderful!{w=0.5} Then we'll have the interview at 2:00 PM tomorrow."
    mike "Then I'll be there!"
    manager "Excellent to hear! See you then, Mr. Schmidt!"
    play sound car_approach
    pause 5
    scene bg freddys_outside_day with longdissolve
    pause 2
    window show dissolve
    "Well, time for my first job interview."
    python:
        renpy.music.set_volume(volume=0.25, delay=0, channel='music')
        renpy.music.set_volume(volume=0.25, delay=0, channel='sound')
        renpy.music.set_volume(volume=0.25, delay=0, channel='sound2')
    play music round_and_round fadein(3.0)
    play sound crowd fadein(3.0) loop
    play sound2 children_playing fadein(3.0) loop
    nvl clear
    window hide dissolve
    nvl show dissolve
    narrate """
    Even from out here, I could hear the noise going on inside.

    That alone makes me grateful that I'll be working during closing hours should I end up getting the job.

    The restaurant itself looks pretty well-maintained for the most part, though you can tell that it's not exactly a new establishment.

    This place has been here longer than Macey and I have been alive, yet I don't recall us ever coming here as children.

    It was something about how we were \"too good\" for such primitive establishments.

    Right, because Happy Meals have nothing on a Freddy Fazbear Pizza.
    """
    nvl hide
    with dissolve
    pause 1
    play sound3 pizza_door
    python:
        renpy.music.set_volume(volume=1.0, delay=3, channel='music')
        renpy.music.set_volume(volume=1.0, delay=3, channel='sound')
        renpy.music.set_volume(volume=1.0, delay=3, channel='sound2')
    scene bg freddys_dining_day with dissolve
    pause 1
    nvl clear
    nvl show dissolve
    narrate """
    Upon entering the pizzeria, I told the woman behind the counter I was here for the interview.

    After she told me where to find the manager's office, I thanked her and entered the main dining area.

    {nw}

    The place was pretty packed.{w=0.2} More than I'd expect, to be honest.

    Children could be seen running around, though most seemed to be sitting in their seats and eating the pizza.

    But the main thing that everyone's eyes seemed to be drawn to was a show stage that could be spotted at the far end of the room.
    """
    nvl hide
    with dissolve
    scene cg fnaf_daytime_performance with dissolve
    pause 1
    window show dissolve
    "Three animatronic animals could be seen performing a show for the crowd."
    "The brown bear with the top hat and microphone was easily recognized as the titular Freddy Fazbear."
    "To his right, there was a purple rabbit playing a guitar, and to his left was a yellow duck-looking thing holding a cupcake.{w=0.2} I guess it's the backup vocalist."
    "Altogether, they all played their song while the kids cheered with excitement."
    "I gotta be honest; those robots definitely look a bit creepy and outdated, but I suppose they still get the job done."
    scene bg freddys_dining_day with dissolve
    "Alright, time to get to the manager's office before I'm late.{w=0.2} Macey will kill me if I fuck up this interview."
    stop music fadeout(3.0)
    stop sound fadeout(3.0)
    stop sound2 fadeout(3.0)
    window hide dissolve
    pause 1
    scene bg freddys_manager with longdissolve
    pause 1
    play sound door_knock
    pause 3
    play sound door_open
    pause 2
    show manager normal smile at middle_close with dissolve
    window show dissolve
    manager "Ah, you must be Mike Schmidt!"
    mike "Yes, sir!"
    "We then shook hands and he offered me the seat in front of his, which I accepted."
    show manager at middle with dissolve
    play music get_the_groove
    manager "So, you wish to work as a nighttime security guard at Freddy's?"
    mike "That's right, sir."
    manager frown "And why is that, exactly?"
    manager sad "After all, and do forgive my bluntness, but it seems like this is the first job you've ever applied for."
    mike "Well, er, that's because it is, sir."
    manager normal smile "Please, you don't need to keep calling me \"sir\".{w=0.2} I know you must be nervous, but I encourage you to relax a bit."
    mike "Um...{w=0.5} Th-Thank you."
    mike "Look, to be perfectly honest, I applied here because it was the only job available that I qualified for."
    manager frown "I see."
    "I certainly hope that wasn't the \"wrong\" answer."
    mike "Uh, but I know I can handle the job well.{w=0.2} I've been told that what's required of me is my greatest skill."
    manager mad "So you're aware of what you'll need to do, then...?"
    "He suddenly looked a tad more serious."
    mike "Well, uh, the ad said I'd just need to watch the security cameras and ensure everything's safe, so it can't be that bad, can it?"
    manager sad smile "Ah.{w=0.5} Well, yes, it really is that simple."
    "And just like that, he went back to normal.{w=0.2} Was I just imagining things there?"
    manager normal "Yes, as the ad stated, your duties essentially boil down to you sitting in a security office at the back of the restaurant and watching the security feed."
    manager "There's really no need to be concerned about anyone breaking in, mind you, but we'd rather be safe than sorry."
    mike "That makes sense."
    manager frown "Now, that being said, should you get this position, your primary focus should be on the animatronic characters we have on stage."
    mike "Why's that?"
    manager "They're our biggest money-makers, for starters.{w=0.2} Plus, as I'm sure you may have noticed, they're not as new as they used to be."
    manager "Essentially, we just want to make sure nothing bad happens to them.{w=0.2} Those particular models are irreplaceable."
    manager sad "We would invest in some newer models, but it's not financially possible for us at the moment."
    mike "Ah.{w=0.2} I see."
    "I suppose that makes sense; I can't imagine even one of those things being cheap, let alone three of them."
    manager smile "So as I said, we just want every precaution possible to make sure they stay in good condition.{w=0.2} Kinda hard to have a show without ol' Freddy, Bonnie, and Chica on stage."
    "Freddy, Bonnie, and Chica, eh?{w}\nFreddy Fazbear and Bonnie the Bunny makes sense, I suppose, but Chica the Duck?{w=0.2} I don't get that one."
    manager normal "Well, Mr. Schmidt, I'll be honest with you:"
    manager "You definitely seem like the responsible type based on what I've seen from you just in this interview, and the job is fairly simple to handle."
    manager "While I won't make any promises, I'd say your chances are great."
    "Well, that's certainly relieving!"
    manager "I'll be sure to give you a call, regardless of my decision."
    mike "Thank you."
    hide manager with dissolve
    "We shook hands again and I left the office."
    "Well, it doesn't feel like I bombed it, so that's good news!"
    "Still, I did find it odd how little about myself I really needed to give him.{w=0.2} Surely they wouldn't let just anyone have such a responsibility...?"
    "Well, either way, I'm sure Macey will be excited to hear about how well the interview went!"
    window hide dissolve
    stop music fadeout(5)
    pause 2
    scene bg black with longdissolve
    pause 3
    $persistent.story1Chapters["ch2"] = True
    jump orientation
