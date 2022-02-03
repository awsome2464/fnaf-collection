label orientation:
    $persistent.story1Chapters["ch3"] = True
    $currentStory = "FNaF"
    "{i}A few days later...{/i}"
    scene bg apartment_tv
    show macey normal straight blank at middle
    with dissolve
    window show dissolve
    macey "You sure you got enough sleep for tonight?"
    mike "I certainly hope so."
    macey level "Come on, Mike.{w=0.2} It's your first day at your first job. I don't want you to screw it up by falling asleep at work."
    mike "I'll be fine, Mace."
    macey sad "I'm sure you will, but I just wanna make sure you don't make a bad first impression."
    mike "I got the job, so clearly they like me."
    mike "Anyway, it's about time for me to head out for the night."
    macey smile "Alright, I suppose I shouldn't hold you back, then."
    mike "See ya tomorrow!"
    macey normal "See ya tomorrow.{w=0.2} Good luck!"
    window hide dissolve
    pause 1
    scene bg black with longdissolve
    pause 1
    scene bg freddys_outside_night with longdissolve
    pause 2
    window show dissolve
    "Well, I'm back again.{w=0.2}\nOnly this time, I'm an employee!"
    "Though, I gotta be honest, the place looks a lot less cheerful at night."
    "I walked past the only other car in the parking lot and entered the pizzeria."
    window hide dissolve
    pause 1
    play sound pizza_door
    play music fnaf1_idle_ambience
    scene bg freddys_dining_night with dissolve
    pause 1
    window show dissolve
    "With the place now devoid of customers, it gives a very different feeling."
    "My eyes then naturally turned towards the show stage."
    scene cg fnaf_nighttime_performance with dissolve
    "When I had seen these 3 characters on the day of my interview, they seemed unsettling, but still innocent enough."
    "But now that the lights are off and they're staying completely still..."
    "...well, it's just a little bone-chilling."
    play sound manager_footsteps
    "I could hear footsteps approaching from one of the hallways.{w}\nHopefully it's not a burglar or something;{w=0.2} I'm still off duty!"
    scene bg freddys_dining_night with dissolve
    pause 1
    show manager normal smile at middle with longdissolve
    pause 1
    manager "Good evening, Mr. Schmidt!{w=0.2}\nHere a bit early, I see."
    mike "Well, I'd rather be a bit early than a bit late."
    manager "That's a good mindset to have.{w=0.2} Well, let me show you to your office, then."
    hide manager with dissolve
    play sound manager_footsteps
    "He then led me down the hallway he had appeared from."
    scene bg freddys_lefthall with dissolve
    "Between the darkness and echoes, going down this hallway was actually making my hands shake a bit."
    "I'm not even usually one to get scared that easily, yet something about this atmosphere is really getting to me."
    "The manager seemed to have read my mind, because he then began talking."
    manager "I know it can be a bit scary here without the light. There's just no point in having them on if no one is here, you know?"
    mike "Sure.{w=0.2} Makes sense."
    manager "But don't worry, though;{w=0.2} there's plenty of light in your office."
    "He then pointed to the end of the hall, where light could be seen from what looked like a doorway and window."
    "That's definitely a relief..."
    "Eventually, we made our way to the security office."
    window hide dissolve
    pause 1
    play ambience fnaf1_office_ambience fadein(3)
    scene bg freddys_office with longdissolve
    show screen nose_honk
    pause 1
    window show dissolve
    manager "There's your seat right there in the middle."
    "Taking the hint, I sat down in the chair."
    "I gotta admit, it's a bit cramped in here, all things considered."
    "It doesn't exactly look clean, either.{w=0.2} Must be day shift's mess."
    manager "Now, there {i}is{/i} something very important I should tell you."
    $fnaf1OfficeXAlign = 0.0
    show bg:
        ease 0.5 xalign fnaf1OfficeXAlign
    pause 0.5
    mike "Yeah?"
    hide screen nose_honk
    scene bg freddys_leftdoor
    show manager sad frown at middle
    with dissolve
    manager "As I alluded to during your interview, we're not in the best financial situation."
    manager "So, during your shift, the building will be running on a power generator that, when utilized properly, will last you over 6 hours."
    mike "Well, that shouldn't be a problem, right?"
    manager normal "Correct.{w=0.2} But the more electrical objects are used, the faster it will drain, and you may end up using a lot of said objects during a shift."
    manager "The cameras use power, the security doors use power, the door lights use power...{w}\nHeck, even the lights in your room use power!"
    mike "Oh."
    "When he puts it all like that, it sounds rather concerning.{w=0.2} Am I really going to have enough power to last the whole night...?"
    manager smile "Don't fret, however;{w=0.5} there's a meter on your desk that will tell you what percentage the generator is at."
    show screen nose_honk
    scene bg freddys_office:
        xalign fnaf1OfficeXAlign
    with dissolve
    "I looked back at the desk and saw the meter he was referring to."
    "It's currently at 100\%, so that's a bit of a relief."
    scene bg freddys_leftdoor
    show manager normal frown at middle
    with dissolve
    manager "So just be mindful of your power consumption.{w=0.5}\nNobody wants to be here alone in total darkness, heh..."
    "Noted."
    manager smile "Oh, yeah.{w=0.2} One more thing:"
    "He then pointed to a piece of paper and pen on the middle of the desk."
    manager "I just need you to sign that, please."
    mike "What is it?"
    manager "It's just a basic employee contract."
    manager sad "There's nothing serious to it.{w=0.2} It's just you agreeing that you will be present at all times during your shift, won't break anything, steal anything, yadda yadda."
    mike "Ah.{w=0.2} Alright, then."
    "I then picked up the pen and skimmed through the contract."
    "There were paragraphs upon paragraphs of stuff, but it was only one page long, and it all seemed to have the general gist of what he had just stated."
    "So I signed the contract and handed the stuff to him."
    manager normal "Great!"
    "He then looked at his watch."
    manager "Well, it's just about time for your shift.{w=0.2} Have a good night, Mr. Schmidt."
    mike "You, too."
    play sound manager_footsteps
    hide manager with longdissolve
    pause 1
    "It was as if he disappeared immediately into the dark hallway."
    $fnaf1OfficeXAlign = 0.5
    show screen nose_honk
    scene bg freddys_office with dissolve
    "That was certainly a lot to take in all at once."
    "But I'm sure everything will be just fine."
    play sound fnaf_chime
    "I then heard a clock chime right above me."
    "It's officially midnight and the start of my shift."
    "Let's hope it'll be an easy and quick night..."
    stop music fadeout(3)
    window hide dissolve
    pause 4
    jump fnaf_night_1
