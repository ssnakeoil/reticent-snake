# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# "And what if I told you that you ruined my life? How would that make you feel?"
# She's stressed, she's got mommy issues, she hates the world, and she's in absolutely no mood to entertain you.
#It's dangerous to write alone, take this:       "{i}{/i}"

init:
    define config.layers = [ 'background', 'smoke1', 'smoke2', 'master', 'transient', 'screens', 'overlay', 'excerpts' ]

# The game starts here.
label start:
    $ save_name = "Prologue"
    scene amulet onlayer background
    scene smoke top onlayer smoke1
    scene smoke bottom onlayer smoke2
    centered "The Amulet of Tinnuon."
    centered "A fabled artifact said to be imbued with magick so powerful its wearer is guaranteed eternal life... but at a terrible price."
    centered "Documented possession of the amulet is limited, and what has survived in ancient texts does not explain what this \"price\" may be."
    centered "The amulet itself disapeared hundreds of years ago."
    centered "The faeries, beings responsible for the amulet's conception, keep secrets about the arifact closely guarded."
    centered "Many witches have sought out the amulet, but have failed to find the thing of legends."
    centered "Much time has passed. Seasons have changed."
    centered "Most have forgotten the legends, in light of those that uplift the newer generations of witches."
    centered "For those such as that of the Amulet of Tinnuon serve to remind us that for great power, we must suffer great loss."
    hide amulet
    hide smoke top
    hide smoke bottom
    scene black
    window show
    define pov = Character("[povname]", ctc="ctc_animation", ctc_position="fixed", image="pov", window_left_padding=90)

    python:
        povname = renpy.input("What is your name?")
        povname = povname.strip()

        if not povname:
            povname = "Doma"

    menu:
        "[povname]?"
        "Yes.":
            pass
        "No.":
            jump start

    menu:
        "I'm a..."
        "I'm an empath.":
            pov "{i}I'm an empath.{/i}"
            $ empath = True
            pass
        "I'm a necromancer.":
            pov "{i}I'm a necromancer.{/i}"
            $ necro = True
            pass
        "I'm a healer.":
            pov "{i}I'm a healer.{/i}"
            $ heal = True
            pass
        "I'm a nature witch.":
            pov "{i}I'm a nature witch.{/i}"
            $ nature = True
            pass
    "{i}My aunt used to tell me stories like that when I was younger.{/i}"
    "{i}Stories of lost artifacts, fallen faerie princes, and forgotten cities.{/i}"
    "{i}She passed a few months ago.{/i}"
    "{i}It feels like I haven't stopped crying since receiving the news.{/i}"
    "{i}She raised me. My parents died in a spell casting accident when I was very young and I never knew them.{/i}"
    "{i}Because of that, she was more like my mom.{/i}"
    "{i}I have no memories of my parents, but she used to talk about my mom a lot. They were twins and both earth witches.{/i}"
    "{i}I never thought that I could be a nature witch like my mom or my grandmother. Something about being out in nature always made me feel like I was being watched.{/i}"

    if nature:
        "{i}Didn't stop me from trying, though. Turns out it was something that I ended up liking.{/i}"
    else:
        "{i}Doesn't really run in the family, I guess.{/i}"

    "{i}Strangely, I've felt the same feeling of being watched ever since the funeral. And when my eyes weren't so puffy, I could sometimes make out a figure that's begun to stand at the foot of my bed when I turned the lights off at night.{/i}"
    "{i}I'm lucky that it seems to just... stand there.{/i}"
    "{i}On my worst days, I've taken to speaking to the figure, and though the conversation is one-sided, it's presence often felt almost... comforting.{/i}"
    "{i}It made me feel less alone, and like I was heard.{/i}"
    "{i}Unfortunately, once my friend found out, he took to aggressively cleansing my home with white magick.{/i}"
    "{i}It's presence persisted.{/i}"
    "{i}It crossed my mind that it may have been because of the amulet that my aunt passed to me, but I doubted that she ever dabbled in darker magicks enough to conjure and bind a demon or rouse a ghost.{/i}"
    "{i}Not one so stubborn to leave, if this was indeed one of those entities.{/i}"
    pov temp "Ugh..."
    "{i}Of his own volition, Linus (my orc mage friend) was \"kind\" enough to hire a bodyguard for my troubles.{/i}"
    "{i}Something I was not very excited about.{/i}"
    "{i}Not only because I was appreciating the company of the arcane stranger, but because of the fear that I would be indebted to this man.{/i}"
    show l temp with dissolve
    l "You know I worry about you."
    pov "Yes, of course I do."
    "{i}Yes. {w}It bothered me. {w}Especially after he practiced suggestion magic on me without my knowledge. {w}But here we were after our \"amicable\" reconciliation.{/i}"
    pov "You know, Linus... you don't have to go out of your way to do this... {w}or {i}anything{/i} for me."
    "{i}He ignored the statement, like he's done many times before. I rolled my eyes.{/i}"
    "{i}Ever since I discovered his dark secret, he's done everything in his power to try and stay friends with me.{/i}"
    "{i}It was like he felt that he owed me something. {w}And he did. {w}But I wanted nothing to do with it.{/i}"
    l "I know you want to be alone right now... {w}but if I knew something like this was going on too I would have stepped in sooner."
    pov "I don't {i}want{/i} to stay with you. And I didn't {i}want{/i} you to step in. {w}Ever. {w}Stop going out of your way. I'll be fine."
    l "It's not out of the way. You're important to me. I want you to stay safe."
    pov "..."
    "{i}As horrible as it was, I was still too angry with him to care.{/i}"
    l "It doesn't have to be my place. It can be a friend's? A coworker's? My girlfriend Lileth's?"
    pov "{i}Lileth's??{/i}"
    "{i}He sighed loudly.{/i}"
    pov "It's not like this thing is going away. You already did your academy-learned white magick on it."
    "{i}He sighed again, like I was a baby that just couldn't understand.{/i}"
    l "Exactly. That's why I called in a favor."
    "{i}I rolled my eyes. {w}Again.{/i}"
    pov "You could have saved it."
    l "Look, I'm not doing any of this for myself."
    "{i}\"Of course you are,\" I thought to myself.{/i}"
    l "..."
    "{i}I felt my neck for the amulet and clutched it when my hands found it at the end of its chain. Doing so seemed to help me to calm down. I sighed.{/i}"
    pov "I just don't think you should be this involved in my life anymore. I'd.. {w}prefer {w}that you weren't."
    l "... {w}You're right... {w}We're not kids anymore."
    l "At least let this be one of the last things I do for you, [povname]."
    "{i}I nodded, hesitantly, and the conversation died down as I waited for this \"bodyguard\" to show up at work.{/i}"
    "{i}Just as I reached for my phone, Linus pulled me outside to greet a car pulling up to the curb.{/i}"
    l "He's here."
    "{i}Upon reaching the old, near vintage car, a man came around from the driver's side and leaned on the passenger side door.{/i}"
    show l temp at left with ease
    show g temp at right with dissolve
    pov "You called a vampire? For what?"
    l "I admit, he may be more than you need. But vampires can sense these kinds of things better than us witches can."
    "{i}The vampire looked tired. More than I did, and I had yet to have slept a single night without crying myself to sleep.{/i}"
    "{i}He met my eyes and held them for a moment.{/i}"
    if necro:
        "{i}I looked away when Linus grabbed my arm and pulled me in.{/i}"
        l "Please don't try anything funny."
        pov "What do you mean?"
        pov "You white witches always have such weird preconceptions of necromancy."
        pov "I wouldn't dream of doing anything to your friend... wherever he is."
        "{i}When I leaned to the side to look over Linus's shoulder, he was gone.{/i}"
        g "So you're a necromancer, are you?"
        pov "He's afraid that you'll become my puppet."
        "{i}He gave a visibly red Linus a once over.{/i}"
        l "That's not what I said!"

    if empath:
        "{i}This... feeling of endless descent. {w}Loss. {w}Solitude's embrace.{/i}"
        "{i}A sobering reminder that beings that lived longer than humans were much more closely acquianted with death than us witches.{/i}"
        "{i}I tore my eyes away from his when I started to feel the darkness consuming me.{/i}"
        pov "A lonely one, at that."
        rs "Oh! I recognize that look. You're an empath..."
        "{i}I jolted at the sudden sound of his voice. When I turned my head, he was suddenly at Linus's side.{/i}"
        rs "Loneliness is... a common trait among us, you will find."
        pov "\"Among vampires?\" I managed to ask."

    "{i}He just smiled, and I narrowed my eyes at him.{/i}"
    rs "My name is Gabriel. It's a pleasure..."
    "{i}He politely held his hand out for mine, and I gave it to him reflexively.{/i}"
    window hide
    scene image "cgs/vamp/vampire meeting.png":
        pause 2.0
    $ persistent.vcg1 = True
    window show
    "{i}I watched as he brought it to his mouth and kissed my knuckles. A practiced gesture. One that managed to take me off guard, regardless.{/i}"
    ga "...[povname]."
    "{i}I retracted my hand from his and shot Linus a glare, letting him know that I did not approve of his newest scheme.{/i}"
    scene black with dissolve
    show l temp at left
    show g temp at right
    pov temp "And what am I to do during the daytime?"
    l "The incidences have been occuring at night, right? There shouldn't be a problem."
    l "Anyway, I have to head home. {w}[povname], don't waste this favor. We'll get to the bottom of this."
    show l temp at center with ease
    "{i}He turned to leave, but turned back around to add something else.{/i}"
    l "Let me know if he gives you any trouble."
    "{i}The implication that \"trouble\" could be given gave me slight pause.{/i}"
    hide l temp with easeoutright
    show g temp at center with ease
    "{i}Then he finally left me alone... with Gabriel.{/i}"
    "{i}The vampire man didn't offer any information. {w}Nor did I ask.{/i}"
    "{i}Gabriel... a foreign name like that stood out in a small town like this. He most likely wasn't from here.{/i}"
    "{i}I discreetly gave him a once over while he was looking above at the flower shop, seemingly taken with the decorations.{/i}"
    "{i}His hands were in his pockets, and he was standing so still that he could have been a statue. He exuded such an alluring aura. Before long, I found my eyes glued to him.{/i}"
    "{i}Yes, I knew that it was rude to stare. Of course I knew that.{/i}"
    ga "Not that I don't appreciate the attention..."
    pov "Right! I'm {i}so sorry{/i}! I just got lost in thought--"
    "{i}He quietly put a hand up to stop me.{/i}"
    hide g temp
    show g temp2 at center
    ga "No need to explain. Take your time, I was just going to suggest that we should get you home soon."
    "{i}I blinked.{/i}"
    ga "Unless, of course, there was something else that you wanted to do?"
    pov "You're asking me?"
    "{i}He chuckled.{/i}"
    ga "Of course. I'm your bodyguard, not your keeper."
    pov "Well, in that case..."
    pov "...Milkshakes?"
    #gabriel surprised
    ga "You want a milkshake?"
    "{i}I nodded.{/i}"
    ga "Alright. From where?"
    pov "Just around the corner from here. There's a place that's open late."
    pov "They have aerated blood too, if you wanted..."
    "{i}He nodded as he listened to me, then gestured in the direction I had pointed to.{/i}"
    ga "Following your lead."
    "{i}There was an unmistakeable grace about him. It did well to hide his presence when he followed me. I caught myself checking behind me a few times, unsure if he was still there.{/i}"
    "{i}How peculiar that this grace that camoflauged him so well in the dark streets only served to earn him open stares in the crowded ice cream shop.{/i}"
    "{i}Yet, he was unbothered. He gently shepherded me to the end of the line while I was lost in thought yet again.{/i}"
    ga "You're..."
    pov "Hm?"
    ga "Thoughtful, aren't we?"
    pov "You don't feel the stares?"
    ga "So that's what it was about?"
    "{i}He motioned for me come closer so he could whisper something to me.{/i}"
    menu:
        "Get in close.":
            "{i}I leaned in.{/i}"
            ga "It's best to ignore them."
            "{i}He chuckled and we pulled away from each other. I got my milkshake and all was well in the world.{/i}"
            pass
        "Get in {i}real{/i} close.":
            "{i}I leaned in as closely as I possibly could.{/i}"
            show breath at panelfromtop
            $ renpy.pause(1.0)
            $ persistent.vcg2 = True
            "{i}He chuckled for the second time. A rumble that came from deep within. When he spoke again, his voice was in my ear, conspiratorial in tone.{/i}"
            ga "The secret is ignoring them."
            hide breath at panelfromtop
            "{i}I found myself quickly covering my ear from the tickle of his breath.{/i}"
            "{i}His breath? Did vampires breathe?{/i}"
            "{i}He pulled away, looking amused with my reaction. But he remained by my side. I had to admit that not being alone did make me feel better. I just couldn't tell Linus that.{/i}"
            "{i}It took a few minutes for my heartbeat to relax, finally relax, but once I'd gotten my milkshake all was well again.{/i}"
            pass
    "{i}I motioned for Gabriel to get up from one of the seats that I told him to save for us while I ordered. Then I pushed the aerated blood into his hand.{/i}"
    ga "Oh, you didn't--"
    pov "But? {w}I did. I wanna know what you think of it."
    ga "Alright."
    show lick at panelfromleft
    $ renpy.pause(1.0)
    hide lick at panelfromleft
    $ persistent.vcg3 = True
    "{i}I watched him tentatively lap at the crimson ice-cream-esque substance. For a moment, I caught a glimpse of his fangs, pointed, pearlescent in the moonlight.{/i}" #twilight type beat
    ga "O-negative? {w}Is this blood from someone in the shop?"
    pov "The cashier's. You can tell?"
    ga "The smell. It's a bit of a vampire quirk, I guess..."
    pov "Oh..."
    "{i}He lifted the paper cone up in his hand to inspect it. Could he really tell from just a sniff?{/i}"
    ga "Well, this is interesting, but I think I'd still rather have it the more conventional way."
    pov "You mean, like, ...feeding on..."
    "{i}I took a sip from my styrofoam cup, relishing in the sweetness of the thick, frozen liquid.{/i}" #thicc lmao
    ga "Well... yes."
    "{i}He breathed out his nose and smiled in slight embarrassment.{/i}"
    pov "Alright, well... {w}let's go home."
    "{i}He looked flustered at my readiness to direct him, but it didn't seem unwelcome.{/i}"
    pov "My home."
    "{i}A chuckle.{/i}"
    ga "\"Your lead.\" {i}He reminded me.{/i}"

    ###Fade to black

    "{i}Before long, we were on the freeway, heading home.{w}.. Or so I thought.{/i}"
    "{i}The seats were warm... but instead of having a soothing effect, it allowed my mind to wander to darker places.{/i}"
    "{i}I gripped the milkshake firmly as I sank back into the passenger seat.{/i}"
    "{i}Was it wise to trust a man that I didn't know to escort me home?{/i}"
    "{i}The ride was silent, save for the occassional bump in the road. It wasn't until we passed the city limit that my whole body went into high alert.{/i}"
    "{i}I didn't know this road.{/i}"
    "{i}Could he be taking us to a safehouse without telling me anything?{/i}"
    "{i}Or could he be isolating me to...{/i}"
    "{i}I examined him again and decided that he seemed like a reasonable person, and my curiosity needed to see how this ended.{/i}"
    "{i}As if he felt the air growing sticky with tension, Gabriel broke the silence.{/i}"
    ga "How do you know Linus?"
    pov "We grew up together. You?"
    ga "We were... ah, we went to university together."
    "{i}He chuckled, probably remembering something that they'd done together.{/i}"
    pov "Was that your first time at that university?"
    "{i}He went silent, considering my statement.{/i}"
    ga "A rather insightful question."
    "{i}I made a small bow and motioned with my smoothie.{/i}"
    ga "I go back every now and then. Magick and magick education evolves as much as the seasons change."
    "{i}I nodded in response, unsure if he would see the gesture, but oddly not too concerned that he would miss it either. Nothing seemed to pass him unnoticed.{/i}"
    "{i}Despite my curiosity, I wasn't really in the mood for conversation and he seemed to sense it. The conversation halted there.{/i}"
    "{i}He turned on the radio to make up for the silence.{/i}"
    "{i}I turned my attention to the window, watching the lights as we sped by.{/i}"
    "{i}It wasn't until about a half hour later that Gabriel spoke up again catching me on the brink of consciousness.{/i}"
    ga "He told me about you earlier."
    "{i}I took a moment to collect myself.{/i}"
    pov "...Linus?"
    "{i}He nodded.{/i}"
    ga "He said you weren't going to be easy to deal with."
    "{i}I scoffed. The nerve!{/i}"
    pov "...That bitch."
    "{i}The comment earned me another chuckle.{/i}"
    ga "You seem to give him... what he deserves. {w}Not that it's my business."
    menu:
        "Gabriel: \"You seem to give him... what he deserves. Not that it's my business.\""
        "He's annoying.": #out with it
            $ truthful +=1
            pov "He's annoying."
            pov "Doing things just because it makes him feel better, not because anyone needs it."
            ga "It must be an act of repentance, then."
            "{i}I realized then that I may have divulged more information than I had intended.{/i}"
            ga "Ah, I'm sorry. I don't mean to overstep."
            ga "It's just an inference, you have my word."
            pov "And how good is your word?"
            "{i}His brows furrowed briefly before his features settled back into a smile.{/i}"
            ga "You're just going to have to trust me."
        "He's overbearing.": #reserved
            $ guarded +=1
            pov "He's just... overbearing."
            "{i}Of course, it was more than that, but it's not like you were just going to out and tell him the details.{/i}"
            ga "I wager you'll be giving me a hard time too, then."
            pov "The circumstances make your overbearance excusable."
            "{i}He smiled at me, but some quality of his face left me unsettled.{/i}"
    "{i}Regardless, I was glad that he didn't press the issue, and breathed a sigh of relief.{/i}"

    scene black with dissolve

    "{i}Before I knew it, I was asleep. {w}How was I so tired? In all the months that the figure had been showing itself to me, I'd never felt so utterly in need of sleep.{/i}"
    "{i}When I woke up, I was warm. The smell of cologne was near, and I felt weightless...{/i}"
    "{i}When I roused, I felt the arms around me tighten protectively.{/i}"
    pov "...Gabriel?"
    "{i}I opened an eye to see the vampire's face above me. He flashed me a smile I couldn't seem to stop myself from reciprocating.{/i}"
    ga "I'm carrying you to your apartment. {w}I can put you down, but you'll have to wait until we're off the stairs."
    "{i}The smell of cologne continued to invade my sense of smell; it was a stress relieving fragrance. {w}Eucalyptus?{/i}"
    "{i}Eucalyptus was my personal favorite. I briefly wondered if Linus had somehow told him to wear it, or if he'd somehow picked up on it using his ...vampireness.{/i}"
    pov "Are we really at my apartment?"
    ga "Yes, [povname]."
    pov "You took us the long way."
    "{i}He peaked at me while continuing to traverse the steps up to my fourth floor apartment.{/i}"
    ga "I thought the ride might ease your nerves."
    "{i}I blinked, feeling guilty for being so suspicious of him. {w}Especially when he had been right.{/i}"
    pov "I..."
    menu:
        "I'm sorry.": #out with it
            $ truthful +=1
            pov "I'm sorry."
            "{i}He didn't look at me, but I could tell he was confused.{/i}"
            pov "I think I've unfairly judged you from the beginning."
            ga "..."
            "{i}There was a long silence, where I wondered if I did the right thing by telling him, before he quietly chuckled.{/i}"
            ga "I... Understand where you come from."
            ga "It's been a stressful journey for you. You're afforded the right to be guarded."
        "Thank you.": #reserved
            $ guarded +=1
            pov "Thank you, Gabriel."
            ga "Of course."
    "{i}I laughed, looking up at him, but I didn't expect him to look back at me. He winked when I didn't look away.{/i}"
    "{i}My face felt hot when he looked away.{/i}"
    "{i}Once he opened the door to my floor, I gave him a pat on the shoulder.{/i}"
    pov "I can take it from here."
    ga "Of course."
    "{i}He set me down slowly and gently, like he was afraid that I would break at the tiniest misstep.{/i}"
    "{i}I tried to put it out of my mind, but something about the gentleness of the gesture stuck with me.{/i}"
    "{i}After I'd led him down the hall and {u}made sure{/u} to {u}invite{/u} him into my studio apartment, I had a sudden realization.{/i}"
    pov "Where are you going to sleep?"
    "{i}His answer came swiftly.{/i}"
    ga "I won't."
    ga "Is it alright if I sit here?"
    "{i}He motioned for a seat across from my bed.{/i}"
    pov "Right across from my bed?"
    ga "I assure you that it's only so that I can catch whatever is stalking you during the night, nothing else."
    pov "..."
    ga "..."
    pov "..."
    "{i}I was trying to take a moment to deliberate silently, but the silence was deafening.{/i}"
    "{i}As panicked as I was from the ordeal as a whole, Gabriel looked more and more like the light at the end of the tunnel.{/i}"
    ga "...What is on your mind?"
    pov "I want to believe you. I'm just..."
    if truthful ==2:
        pov "I'm scared it won't change anything."
        "{i}His expression softened at my vulnerability. It was clear that he was not expecting my honest confession.{/i}"
        "{i}I looked down, a bit in shock that it had slipped passed my lips in the first place.{/i}"
        "{i}The sound of his shoes came first, then I saw his shoes come into my field of vision.{/i}"
        "{i}It was alarming how far he was willing to go to make me feel comfortable.{/i}"
        "{i}It made me wonder about what I looked like to the rest of the world.{/i}"
        "{i}Did I look like someone that constantly needed to be comforted?{/i}"
        ga "I can't make any promises but it's worth a try."
        pov "..."
        pov "It is."
        pass
    if guarded ==2:
        pov "I don't know you."
        pov "You're a strange man, a vampire no less, standing in my apartment..."
        ga "Would you like me to try and convince you?"
        "{i}It was a strange question, but truth be told, I did.{/i}"
        pov "\"Yes.\" I breathed."
        "{i}He respectfully remained standing as he thought of what to say next.{/i}"
        ga "I completely understand your apprehension. However, know that I am here to help you."
        ga "I do not know you either, but I do know Linus. So... if you can't believe that I am concerned for your well being out of sympathy for your situation, at least consider that I am doing a favor for Linus."
        pov "..."
        ga "Convincing enough?"
        menu:
            "Convincing enough?"
            "Push further.":
                $ guarded +=1
                pov "Please continue..."
                ga "If you worry about..."
                "{i}I found my eyes flickering to his fangs whenever he opened his mouth enough for them to show.{/i}"
                "{i}He definitely noticed, as he began to speak with less lip movement to conceal them better.{/i}"
                ga "I am... very... old... The oldest of my kind in this region..."
                ga "Consequently, my need for blood has reduced substantially, and I only have need for it every few months."
                ga "I made sure this would not be a hindrance. And should I need... sustenance under Linus' employ I will be sure to do so discreetly."
                pov "..."
                ga "From a willing participant, of course."
                pov "..."
                ga "Who will leave alive, you have my word."
                pov "Okay."
            "Yes.":
                pov "Yes, that's enough."
                pov "Thank you for indulging me."
                pass
    if truthful ==1:
        pov "I don't know."
        pov "Well... alright, yes."
        pass
    ga "So, the chair...?"
    pov "Yours, for sitting."
    "{i}He happily took a seat, settling in, presumably, for the night.{/i}"
    "{i}I let another moment pass before I spoke again, questions niggling me to prod him.{/i}"
    pov "There is... something I wanted to ask."
    ga "Yes?"
    pov "You... seemed to be more interested in the situation than you let on."
    ga "I did?"
    pov "I guess I... just wanted to know if you had any ideas about what might be going on."
    "{i}He was keeping up his smile, but I knew that he was thinking. Or considering how I would react to what he was about to say next.{/i}"
    ga "I do have {i}one{/i} theory."
    "{i}I nodded.{/i}"
    ga "May I see the... object?"
    "{i}Hesitantly, I lifted the amulet from around my neck and passed it to his outstretched hand.{/i}"
    pov "How did you...?"
    ga "This locket is imbued with somekind of magick... I felt it immediately in your presence."
    pov "Like some kind of hex?"
    ga "It is a possibility, but these things are not always so black and white."
    ga "And besides, this... energy... is not something one human would be able to contain in such a small artifact..."
    ga "No, this is fae magick."
    pov "What! Fae magick?"
    pov "But they hate humans! What would my grandmother have been doing with this?"
    ga "Well, it could have been given to her."
    pov "By who? By {i}what{/i}?"
    ga "She could have obtained it in any manner."
    ga "Were you close to her?"
    pov "Yes!"
    ga "So she would not have wanted anything to happen to you."
    ga "Have you ever... seen..."
    pov "I haven't, unfortunately."
    if truthful ==2:
        pov "I've been way too spooked since this all began to even muster a peak, honestly."
        ga "That is not unreasonable, [povname]."
    ga "We will see it for what it is tonight, if my suspicions are correct."
    pov "What do you suspect it is?"
    ga "Well, I {i}suspect{/i} that it's one of two things."
    ga "One of benevolent intentions, and the other... not quite as easily sorted."
    "{i}It was clear that he did not want to elaborate any further, and while I desperately wanted to know what he meant, I was {i}compelled{/i} to stop asking questions.{/i}"
    pov "Don't-don't..."
    "{i}He looked up from his train of thought, alarmed at my struggling, and I instantly felt in control of my actions again.{/i}"
    ga "What happened?"
    pov "You mean that wasn't... That wasn't you?"
    ga "What wasn't me?"
    ga "[povname]?"
    "{i}I was confused. Something had definitely tried to keep my mouth shut.{/i}"
    "{i}But it didn't matter, I was going to be getting to the bottom of this either way.{/i}"
    pov "Nevermind. I just want this all over."
    ga "Well... very well. Here you are."
    "{i}He handed back the locket and I gripped it firmly.{/i}"
    pov "I'll be getting ready for bed then."
    ga "Yes, of course."
    pov "No, I..."
    ga "Oh! Of course."
    "{i}He closed his eyes and covered them with his hands to give me my privacy.{/i}"
    if guarded ==3:
        "{i}But I still wasn't completely comfortable.{/i}"
        ga "Would you like to give me a blindfold instead?"
        "{i}He removed his hands from his eyes to look at me with inquisitive eyes.{/i}"
        pov "Yes..."
        "{i}Giving me a gentle smile, he nodded. I snatched one of the silk scarves from my dresser.{/i}"
        ga "Please tie it so that you can be sure, mademoiselle."
        "{i}He bowed his head into the scarf I had been holding out for him to take and I tied it gently.{/i}"
        ga "You may tighten it. Wouldn't want it to slip."
        "{i}I did as he advised and tightened the knot. Then I pushed him back up by the shoulder.{/i}"
        pov "Could I just... make sure there aren't any gaps?"
        "{i}He nodded again like it was a given, all while maintaining the same permissive smile from before.{/i}"
        "{i}I checked the fabric around his eyes for any thin spots or lack of coverage and finally pulled away when I was sure there was no way he could see.{/i}"
        "{i}Of course, unless...{/i}"
        ga "Vampires cannot see through things, belle."
        "{i}My voice catched.{/i}"
        ga "Another inference, I promise. No mind reading either."
        ga "Not unless you sought me out first."
        pov "Thank you."
        "{i}He nodded slightly.{/i}"
    "{i}I dressed into my pajamas and got into bed.{/i}"
    if guarded ==3:
        "{i}But not without walking over to wear Gabriel first.{/i}"
        "{i}I noticed his pointed ears quiver as I approached, his hand coming up to rest on my hip as I stopped in front of him.{/i}"
        pov "We can... we can take this off now."
        ga "At your behest."
        "{i}I gently untied the silky knot and watched as the scarf fell to his lap.{/i}"
        "{i}He was looking up at me so intently that I had to look away.{/i}"
        pov "Again, I appreciate it."
        ga "Of course."
    hide g temp with dissolve
    "{i}Once under the sheets, I exchanged awkward good nights with Gabriel and shut the lights off.{/i}"

    ###### Fade to black

    "{i}I woke in the middle of the night to a strange display.{/i}"
    "{i}Gabriel was not in the chair across from my bed anymore, and was instead standing guarded before... the figure.{/i}"
    "{i}The sound of her voice cut through the silence suddenly when Gabriel took a step forward.{/i}"
    show r temp at left with easeinbottom
    show g temp at right with easeinbottom
    tf "Search elsewhere for blood, vampire!"
    tf "She is under {i}my{/i} protection."
    ga "As she is under mine."
    "{i}She scoffed.{/i}"
    tf "And what use would she have for your company? He who traverses the shadows is ill fit for such a station."
    ga "I assure you, [povname] has sought my \"company.\" I intend to protect her from shady creatures of the night such as yourself."
    "{i}There was a pause before the figure spoke again.{/i}"
    tf "You are the only creature of the night here, vampire."
    "{i}Gabriel noticed that I had roused from sleep and shot me a look that told me to stay where I was.{/i}"

    menu:
        "Listen to Gabriel.":

            $ gabriel +=1
            "{i}I trusted that he was doing this for my good and tried to act like I was still asleep.{/i}"
            "{i}I nodded and quietly looked on at the two at the foot of my bed.{/i}"
            ga "Why are you really here?"
            tf "You speak in circles. Take your blight elsewhere."
            tf "Your ladyship [povname], there is no need to hide from me."
            "{i}She turned to meet my gaze as I lay in bed and I brought the covers up a bit by reflex.{/i}"
            "{i}Of course, it was silly to hide what she already knew, so I eventually pushed the covers away and stood up.{/i}"
            hide r temp
            show r temp2 at left with dissolve
            "{i}Swiftly, she dropped to her knee.{/i}"

        "Confront the figure.":

            $ ragna +=1
            "{i}Gabriel looked on with a mixture of emotions as I pushed away the covers and stood, then quickly looked away.{/i}"
            "{i}The one I'd called the figure turned her head slowly to see what he had been looking at.{/i}"
            "{i}She met my gaze full on, sending a shiver down my spine.{/i}"
            "{i}We stood that way for what felt like an eternity before she finally turned to face me.{/i}"
            hide r temp
            show r temp2 at left with dissolve
            "{i}She took a knee before me. The gesture was swift and her head inclined such that her hair touched the ground. It felt almost... devotional.{/i}"
            tf "Your ladyship [povname]."

    "{i}I spoke, my voice more confident than I had thought I could muster.{/i}"
    pov temp "Who are you?"
    r "Ragna, your ladyship. Elven guard."
    pov "Please illuminate me on why you are... here."
    r "I am here to protect you, my lady."
    pov "But from what?"
    pov "Or... why, if that’s easier to explain."
    "{i}She looked up at me, confusion written plainly on her face until something suddenly dawned on her.{/i}"
    r "You are... unaware of what you have in your possession. I understand. I will... explain what I can. What I am permitted."
    "{i}It was slight, but her accent bled into her sentences. The fae spoke languages that witches were unable to study. I wondered what her language sounded like?{/i}"
    pov "Also, please... please stand."
    "{i}She curtly nodded before rising to her feet.{/i}"
    "{i}Carefully, she motioned for the amulet.{/i}"
    menu:
        "I let her close the distance." if ragna ==1:
            $ ragna +=1
            "{i}I nodded to let her know it was alright to come closer.{/i}"
            "{i}She took a step forward and gently held the amulet against her palm.{/i}"
            "{i}My face was inches away from her shoulder, and because she was looking down, I could feel a few strands of her hair tickling my face.{/i}"
            "{i}This was the moment that I realized that I was the shortest person in this apartment. In MY OWN apartment.{/i}"
            "{i}Her eyes bore into me.{/i}"
            "{i}I swallowed hard involuntarily.{/i}"
            "{i}This wasn't the time to be getting nervous.{/i}"
            "{i}She lowered her gaze to the amulet once she was happy with her assessment of me.{/i}"
            r "This amulet is an ancient artifact. Your aunt was the last to guard it."

        "I waited patiently for her explanation.":
            "{i}I stared back at her, waiting for her explanation.{/i}"
            r "That amulet is an ancient artifact. Your aunt was the last to guard it."

    r "With every human guard's death, another must take up the task."
    r "To protect. To hide."
    r "In turn, a fae is appointed to protect and guide you."
    r "Your aunt's guide was an elemental, Fleur. Before her, your mother and her guide, the elemental Lamia."
    r "The amulet has changed hands, and so a new guide is appointed."
    "{i}She smiled at me then.{/i}"
    r "And I am your appointed guide."
    if ragna == 2:
        "{i}I blushed, thinking it was kind of cute... But I was getting ahead of myself...{/i}"
        "{i}She laughed softly, letting go of the amulet and taking a step away from me.{/i}"
        "{i}Some part of me missed the proximity. Her presence was so comforting and so familiar.{/i}"
        "{i}It took me a moment before I could gather my thoughts again.{/i}"
    pov "Okay, wait... slow down..."

label amuletquestions1:
    menu:
        "[povname]: \"Wait... slow down...\""
        "What's the significance of the amulet?" if amulet == False:

            pov "What's the significance of the amulet? It's clearly fae in origin, why would it willingly be passed on to human hands?"
            r "Yes! Of course. The amulet contains great power. Power easily detected by most magical beings but it can be concealed by human flesh. We wish for its existence to remain hidden. Thus, we choose a human to conceal it."
            r "Witches exclusively. The relationship is symbiotic. You keep our artifact concealed, and we teach you to harness its power."
            $ flesh = False
            $ amulet = True
            jump amuletquestions1

        "Why human flesh?" if flesh == False:

            pov "What about human flesh conceals its... power readings?"
            ga "Vampires were once humans, could we conceal it as well?"
            "{i}I half expected her to be annoyed at Gabriel's intrusion, but she answered rather calmly.{/i}"
            r "It needs to be {i}living{/i} flesh. It has a tendency to absorb the energy in a way that ours cannot."
            r "In non-humans, the effects are outward. Magickal signal is amplified and easier to find. The opposite in humans."
            $ flesh = True
            jump amuletquestions1

        "My aunt?" if aunt == False:

            pov "You said my aunt was the last one to guard the amulet?"
            r "Yes. She was well respected."
            r "She told me quite a lot about you. I've looked forward to our meeting."
            pov "You spoke with her?"
            r "Quite a few times. I apprenticed under Fleur to become the next amulet guide."
            r "She spoke often of you as well. Though you've never met her, she knew you quite well."
            pov "What did she..."
            r "Anything interesting from that day. When she was training me, considerations I should take for when the amulet was passed to you."
            "{i}I got a bit choked up thinking about my aunt again.{/i}"
            "{i}Gabriel stirred where he stood, shooting me a concerned look.{/i}"
            "{i}I nodded at him to let him know I was okay.{/i}"
            "{i}Ragna's hand rose from her sword in response, but she quickly replaced it around the hilt of her sword.{/i}"
            r "Take your time."
            $ aunt = True
            jump amuletquestions1

        "My mom?" if mom == False:

            pov "You mentioned my mom... Does that mean that you met her?"
            "{i}She paused, seemingly assessing me for a moment before answering.{/i}"
            r "Yes."
            r "You have questions about her."
            pov "Well..."
            label momqs:
                menu:
                    "What was she like?" if likeness == False:
                        pov "What was she like?"
                        r "From my observations... she was bright. Hopeful in bleak situations."
                        pov "Any stories of her?"
                        r "I spoke to her twice. Both very brief encounters."
                        r "Those who were closer to her only had nice things to say."
                        pov "Anyone that I could talk to?"
                        r "I know someone that you could speak to, yes."
                        pov "When can you take me?"
                        r "Whenever you decide, [povname]."
                        $ likeness = True
                        jump momqs

                    "The casting accident?" if accident == False:
                        pov "Do you have any information about... how she died?"
                        r "I only know as much as you do on the topic."
                        "{i}For some reason, I doubted that.{/i}"
                        r "You suspect that there is information I withold from you. I assure you that there is not."
                        r "She and your father casted a very powerful spell knowing the consequences if they were not successful."
                        r "Your mother was fatally wounded and your father's body was found miles away from your mother's."
                        r "The nature of the spell is unknown."
                        pov "That's enough then."
                        $ accident = True
                        jump momqs
            $ mom = True
            jump amuletquestions1

        "Fleur and Lamia?" if oldguides == False:
            pov "Could you tell me more about Fleur and Lamia?"
            r "Your aunt's and your mother's guides, respectively."
            r "Twins as well. Perfect for their predicament. Fleur passed with your aunt."
            pov "What about Lamia?"
            if likeness:
                r "I mentioned her before, just not by name."
                r "Whenever you are ready, I can take you to her."
            pov "She's still alive?"
            r "Yes."
            pov "Do you mind if I ask how Fleur..."
            r "We are sacrificed when our amulet holder passes."
            r "When it's your time, my time will come as well."
            r "Our fates are bound."
            "{i}The inside of my mouth dried at the thought.{/i}"
            $ oldguides = True
            jump amuletquestions1

        "I don't have any other questions.":
            pov "I don't have any more questions."
            r "Very well."
            pass

    pov "Also... Please just call me [povname]."
    r "As you wish, [povname]."
    pov "Now that all of that is sorted away, this is Gabriel. My... {i}other{/i} bodyguard."
    "{i}Ragna wrinkled her nose at the introduction, but seemed to be considering what I had just said.{/i}"
    "{i}Gabriel took the opportunity to pull me away for a moment.{/i}"
    ga "You call that sorted, huh?"
    pov "Well, we got to the bottom of things, didn't we?"
    ga "The bottom? You're satisfied with that explanation?"
    pov "For now..."
    ga "You're bound to this amulet for life. That's what I got."
    ga "You're okay with that?"
    pov "Well, it doesn't seem like there's anything I need to do besides conceal it."
    ga "There's always a catch."
    "{i}Gabriel started to pull back, signalling the end of the conversation.{/i}"
    "{i}Goosebumps pricked my arms.{/i}"
    "{i}It was a simple warning, but he didn't have to make it sound like I was making a bad decision.{/i}"
    r "I see"
    ##also the blighter
    pov "Well, because..."
    ga "Because of you!"
    "{i}She closed her eyes, visually annoyed, but said nothing, ignoring Gabriel.{/i}"
    o "You do not deserve for the blighted one to speak for you, lest he blight your words as well. I will heed your word only, my lady."
    "{i}I shot Gabriel a questioning look, and he shot the same look at me.{/i}"
    pov "A figure has been appearing here at night."
    o "I am the figure."
    pov "Yes."
    o "If that is the reason, then you are released, old blood."
    "{i}She went to unsheathe the sword at her hip, but I lurched forward to try and stop her, much to her surprise.{/i}"
    pov "No, wait wait!"
    ga "Did you intend to strike me?"
    o "Of course! If you are not in her employ, then you are a threat!"
    menu:
        "Ombre: \"Of course! If you are not in her employ, then you are a threat!\""
        "He's not a threat, Ombre.":
            pass
        "{i}You{/i} are the threat!":
            pass


    return
