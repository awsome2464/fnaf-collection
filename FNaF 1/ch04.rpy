label fnaf_night_1:
    $currentStory = "FNaF"
    window show dissolve
    "It was eerily quiet in here."
    "The only real sound I could hear was coming from the fan on my desk and the old lights above me."
    "I decided to focus away from that by actually doing my job."
    "I pressed the power button on the monitor in front of me."
    window hide
    play sound cam_up
    scene cam freddys_stage default at camera_pan
    show screen cam_feed
    hide screen nose_honk
    pause 1
    window show dissolve
    "The 3 animatronics were on the stage, completely lifeless."
    "If they didn't look unsettling before, they certainly do now."
    "Just for kicks, I switched to another cam."
    window hide
    play sound blip
    show cam freddys_pas default at camera_pan
    pause 1
    window show dissolve
    "This looks like it's backstage."
    "There's something a bit unnerving about seeing all of these robotic parts and costumes laid around like this..."
    play sound fnaf_phone_ring loop
    "Suddenly, the phone in my office started to ring!"
    "After calming myself down from that unexpected surprise, I asked myself who that could possibly be."
    "Well, I suppose there's only one way to find out."
    play sound2 cam_down
    scene bg freddys_office
    hide screen cam_feed
    show screen nose_honk
    queue sound fnaf_phone_pickup
    "I turned off the monitor and answered the phone."
    mike "Hello?"
    phone "Uh, hello? Hello?"
    phone "Uh, I wanted to record a message for you to help you get settled in on your first night."
    "It was a man, sounding about maybe middle-aged.{w=0.2}\nBut it wasn't a voice I recognized; who was he?"
    phone "You see, I worked in that office before you.{w=0.2}\nI'm finishing my last week now, as a matter of fact."
    "Ah.{w=0.2} So it's my predecessor."
    $pgName = "Phone Guy"
    phone "So, I know it can be a bit overwhelming, but I'm here to tell you that there's nothing to worry about;{w=0.2} you'll be fine!"
    phone "So let's just focus on getting you through your first week."
    play sound paper_phone
    "I could hear some papers rustling through the phone as he continued to talk."
    phone "Uh, let's see...{w=0.2} There's this introductory greeting from the company that I'm supposed to read...{w=0.5}\nIt's kind of a legal thing, ya know?"
    play sound phone_guy_throat
    "He cleared his throat before reading:"
    phone "{u}Welcome to Freddy Fazbear's Pizza, a magical place for kids and grown-ups alike, where fantasy and fun come to life.{/u}"
    phone "{u}Fazbear Entertainment is not responsible for damage to property or person.{/u}"
    phone "{u}Upon discovering that damage or death has occurred, a missing persons report will be filed within 90 days, or as soon as the property and premises has been thoroughly cleaned and bleached, the carpets have been replaced...{/u}"
    phone "Blah, blah, blah; you get the idea."
    "I could feel my heart drop for a moment."
    "\"Damage or death\"?? And won't file a missing persons report until...{w=0.5}\nWhat the actual fuck kind of legal notice is that??"
    phone "Now, that might sound bad, I know, but there's really nothing to worry about."
    phone "Uh, that being said, the animatronic characters here do get a bit quirky at night."
    "\"Quirky\"...?"
    phone "But do I blame them?{w=0.2} No!"
    phone "If I were forced to sing those same stupid songs for 20 years and I never got a bath, I'd probably be a bit irritable at night, too."
    phone "So remember:{w=0.2} these characters hold a special place in the hearts of children, so we need to show them a little respect, okay?"
    "I'm not quite sure I follow this guy."
    "The way he keeps talking about these robots, he's almost giving off the impression that they're real creatures or something."
    "But before I could think too much harder about it, he dropped a massive bombshell:"
    phone "So just be aware that the characters do tend to wander a bit."
    phone "They're left in some kind of \"free-roaming\" mode at night.{w=0.2} Something about their servos locking up if they're turned off for too long."
    "Wandering?{w=0.2} Free-roaming?{w=0.2} Like, as in they can {i}walk{/i}??"
    phone "You see, they used to be allowed to walk around during the day, but then there was \"The Bite of '87\"..."
    "The BITE??"
    "I could then hear him softly sigh before mumbling to himself:"
    phone "It still amazes me that the human body can live without the frontal lobe."
    "What the actual hell is going on in this place??"
    play sound phone_guy_throat
    "He then cleared his throat and began speaking to me again."
    phone "Now, concerning your safety:"
    phone "The only real risk to you as a night watchman here, if any, is the fact that these characters..."
    phone "Well, if they happen to see you after hours, they probably won't recognize you as a {b}person{/b};{w=0.5} they'll most likely see you as a metal endoskeleton without its costume on."
    "Wait, so they can walk around {i}and{/i} recognize things?{w=0.5}\nWhy are simple entertainment robots so advanced?"
    phone "Now, since it's against the rules for bare endoskeletons to be in public here at Freddy Fazbear's Pizza, they'll probably try to, uh...{w=0.5} forcefully stuff you inside a Freddy Fazbear suit."
    mike "..."
    phone "Now, that wouldn't be so bad if the suits themselves weren't filled with crossbeams and wiring and animatronic devices, especially around the facial area."
    phone "So you can imagine how having your head forcefully pressed inside one of those could cause a bit of discomfort.{w=1} And death."
    phone "Uh, the only parts of you that would likely see the light of day again would be your eyeballs and teeth poking out the front of the mask, heh."
    mike "..."
    phone "Yeah, they don't tell you these things when you sign up.{w=0.5} But hey, the first day should be a breeze!{w=0.2} I'll chat with you tomorrow."
    phone "Just check those cameras and remember to close the doors only if {b}absolutely necessary{/b};{w=0.2} gotta conserve power."
    phone "Alright, good night!"
    window hide
    play sound fnaf_phone_hangup
    pause 2
    window show dissolve
    "I slowly placed the receiver back with a giant grin."
    "I get it now:{w=0.2} he was just fucking with me."
    "He had me going there for a while, but come on.{w=0.5}\nGrabbing me and shoving me inside a suit?{w=0.5}\nSeeing me as an endoskeleton?{w=0.5}\nBeing able to move, at all??"
    "He's clearly just trying to fuck with the new guy and freak him out on his first shift.{w=0.5} Well, joke's on you, buddy; it ain't gonna happen."
    "Though, just out of curiosity, I turned the security feed back on."
    window hide
    play sound cam_up
    scene cam freddys_stage default at camera_pan
    show screen cam_feed
    hide screen nose_honk
    pause 1
    window show dissolve
    "As suspected, all three of them were still there."
    "I chuckled to myself for believing anything that guy said and shut off the monitor."
    window hide
    play sound cam_down
    scene bg freddys_office
    show screen nose_honk
    hide screen cam_feed
    pause 1
    window show dissolve
    "I gave a small yawn as I stretched in my seat."
    "All day, I tried to mentally prepare myself for 6 hours of boring nothingness, but I clearly didn't do it well enough, as it suddenly hit me how long this night was going to be."
    "I wasn't lying to Macey about me not getting enough sleep, but transitioning from a daytime schedule to a nighttime one is definitely something that takes time."
    window hide dissolve
    pause 1
    scene bg black with fastblinkclose
    pause 0.05
    scene bg freddys_office with fastblinkopen
    pause 1
    scene bg black with fastblinkclose
    pause 0.01
    scene bg freddys_office with fastblinkopen
    pause 0.01
    scene bg black with fastblinkclose
    pause 0.01
    scene bg freddys_office with fastblinkopen
    pause 1
    scene bg freddys_office at sceneblur with longdissolve
    pause 2
    window show dissolve
    "I'm sure I'll be fine if I close my eyes for just a minute..."
    window hide dissolve
    pause 1
    stop ambience fadeout(5)
    scene bg black with eyesclose
    pause 5
    play sound fnaf_footsteps
    pause 1
    play ambience fnaf1_office_ambience
    scene bg freddys_office with fastblinkopen
    window show
    "What was that??"
    "I looked over at the clock on the wall."
    "3:30??{w=0.5}\nI didn't think I'd be out for that long!"
    "I quickly turned on the monitor to see what was happening."
    "What I saw when I did made my heart stop for a second."
    window hide
    play sound cam_up
    scene cam freddys_stage nobon at camera_pan
    show screen cam_feed
    hide screen nose_honk
    play music fnaf1_moving_ambience fadein 2
    pause 2
    window show dissolve
    "There was a brown bear and a yellow bird, but no purple bunny!"
    "I looked around nearby cameras to see if I could find him."
    window hide dissolve
    pause 0.2
    play sound blip
    show cam freddys_pas default at camera_pan
    pause 1.5
    play sound blip
    show cam freddys_restroom default at camera_pan
    pause 1.5
    play sound blip
    show cam freddys_dining bon at camera_pan
    pause 2
    window show dissolve
    "There he was, right in the dining area!"
    "How the hell did he get there??"
    "..."
    "There's no way that the guy on the phone was telling the truth."
    "There's no way in hell that it used a \"free-roaming mode\" to get over there."
    play sound cam_down
    scene bg freddys_office
    show screen nose_honk
    hide screen cam_feed
    "I turned off the monitor and tried to calm myself down."
    mike "Come on, Mike.{w=0.2} Don't freak out here."
    mike "All it's doing is standing there.{w=0.2} It won't hurt you."
    mike "And even if it somehow makes its way over here, it's not gonna grab you and shove you in a costume.{w=0.2} That's just crazy!"
    play sound fnaf_footsteps
    pause 1.5
    "At the sound of those footsteps, I turned the monitor back on!"
    play sound cam_up
    scene cam freddys_dining chica at camera_pan
    show screen cam_feed
    hide screen nose_honk
    pause 1
    "Oh, shit;{w=0.2} not only is he gone, but now Chica is moving, too??"
    "Well, I should at least try to find Bonnie...{w=0.2} He couldn't have gotten far."
    window hide dissolve
    pause 0.2
    play sound blip
    show cam freddys_piratecove_01 at camera_pan
    pause 1.5
    play sound blip
    show cam freddys_pas bonnie at camera_pan
    pause 1.5
    window show dissolve
    "Gotcha."

    return