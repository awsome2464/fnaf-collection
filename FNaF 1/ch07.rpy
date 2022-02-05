label fnaf_night_2:
    $persistent.story1Chapters["ch7"] = True
    $currentStory = "FNaF"
    $pgName = "Phone Guy"
    play sound fnaf_chime
    pause 3
    play music fnaf1_idle_ambience fadein(3)
    play ambience fnaf1_office_ambience fadein(3)
    scene bg freddys_office with longdissolve
    show screen nose_honk
    pause 3
    window show dissolve
    "Well, I'm back."
    "When I arrived, the manager didn't say a word to me;{w=0.2} he just gave a quick nod and then left."
    "Now that the shift started, I took a quick look at the stage."
    call fnaf_cam_up("freddys_stage default")
    pause 2
    "Freddy, Bonnie, and Chica..."
    "They were kind to me last night;{w=0.2} let's hope they keep that up."
    play sound fnaf_phone_ring loop
    "Suddenly, the phone rang."
    "Even though I was half-expecting it, it still startled me."
    call fnaf_cam_down
    queue sound fnaf_phone_pickup
    "I picked up the phone."
    if renpy.music.get_playing("sound"):
        play sound fnaf_phone_pickup_short
    phone "Uh, hello?"
    phone "Well, if you're hearing this and you made it to day 2, congrats!"
    "I'm glad he had faith in me."
    phone "Now, I won't talk quite as long this time since Freddy and his friends tend to become more active as the week progresses."
    phone "It might be a good idea to peek at those cameras while I talk just to make sure everyone is in their proper place, ya know?"
    "Well, last night, they didn't move until around 3:30, but..."
    call fnaf_cam_up("freddys_stage default")
    pause 1
    "That's a relief."
    phone "You know, interestingly enough, Freddy himself doesn't leave the stage very often."
    phone "I've heard he becomes a lot more active in the dark, though, so hey!{w=0.2}\nThat's just one more reason to not run out of power, right?"
    "...that's a relief."
    call fnaf_cam_down
    phone "Oh, I also wanted to emphasize the importance of using your door lights."
    phone "You see, there are blind spots in your camera view, and those blind spots happen to be right outside your doors."
    "What convenient planning..."
    "I went over to press one of my door lights."
    $fnaf1OfficeXAlign = 1.0
    show bg:
        ease 0.5 xalign fnaf1OfficeXAlign
    pause 1
    play sound2 door_light loop
    show bg freddys_office right_empty
    pause 1
    "It seemed to light up the area pretty well."
    "Though I did notice it was using up a good amount of power."
    stop sound2
    $fnaf1OfficeXAlign = 0.5
    show bg freddys_office -right_empty:
        ease 0.5 xalign fnaf1OfficeXAlign
    pause 0.5
    phone "So, if you can't find something,{w=0.2} or someONE,{w=0.2} on your cameras, try checking the door light.{w=0.5}\nYou might only have a few seconds to react..."
    phone "Er, not that you would be in any danger, of course.{w=0.2} I'm not implying that."
    "Whatever you say, pal."
    phone "Oh, also, check on the curtain in Pirate Cove from time to time."
    "Pirate Cove?{w=0.2} I thought it was closed;{w=0.2} why would I need to check that?"
    phone "The character in there is unique in that he tends to become more active when the cameras remain off for long periods of time."
    phone "I guess he doesn't like being watched.{w=0.2} I dunno."
    "Wait.{w=0.2}\"The character in there\"...?!"
    call fnaf_cam_up("freddys_stage nobon")
    play music fnaf1_moving_ambience
    show screen ambient_sounds
    pause 1
    "Oh, shit; good thing I checked the cams when I did!"
    pause 0.5
    call fnaf_cam_switch("freddys_dining bon")
    pause 0.5
    "There you are."
    "Okay, now Pirate Cove..."
    call fnaf_cam_switch("freddys_piratecove_01")
    pause 1
    "No sign of anyone, but I'm still incredibly nervous."
    "Why am I only just now finding out that someone is active at a closed attraction??"
    "Just one more thing to the list of things I found out too late, I suppose..."
    phone "Anyway, I'm sure you have everything under control.{w=0.2} Talk to ya soon!"
    play sound fnaf_phone_hangup
    "He then hung up, as did I."
    call fnaf_cam_down
    "Okay, so on top of Bonnie and Chica moving, I've now learned that Freddy hardly moves and there's a fourth character to be on the lookout for!"
    "But as long as I check on the cameras, I should be fine, right?"
    call fnaf_cam_up("freddys_piratecove_01")
    "It really makes me wonder who exactly is behind there...{w=0.2}\nI hadn't seen any poster or something for a 4th character."
    "Oh, well.{w=0.2} I better hope I never find out."
    "For now, let's check up on everyone else."
    call fnaf_cam_switch("freddys_stage freddy")
    pause 1.5
    "Well, Chica's on the move now..."
    call fnaf_cam_switch("freddys_dining bon")
    pause 1.5
    "She's not in the dining area..."
    call fnaf_cam_switch("freddys_restroom chica")
    pause 1.5
    "Alright, there's she is."
    call fnaf_cam_down
    "Okay, Mike, you'll be fine.{w-0.2} It should be just like last night."
