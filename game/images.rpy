# continue animation
image smoke bottom:
        "gui/title screen/smoke bottom.png"
        xalign 1.0
        linear 100.0 xalign 0.0
        repeat

image smoke top:
        "gui/title screen/smoke top.png"
        xalign 1.0
        linear 180.0 xalign 0.0
        repeat

image glitch:
        "gui/title screen/mc.png"
        pause 50.0
        "gui/title screen/glitch1.png"
        pause 0.5
        "gui/title screen/glitch2.png"
        pause 0.5
        "gui/title screen/glitch1.png"
        pause 0.5
        repeat

image BLAME_title:
        "gui/title/0blank.png"
        pause 0.5
        "gui/title/0cursor.png"
        pause 0.5
        "gui/title/0blank.png"
        pause 0.5
        "gui/title/0cursor.png"
        pause 0.5
        "gui/title/0blank.png"
        pause 0.5
        "gui/title/0cursor.png"
        pause 0.5
        "gui/title/0blank.png"
        pause 0.5
        "gui/title/0cursor.png"
        pause 0.5

        "gui/title/1b_cursor.png"
        pause 0.2
        "gui/title/1b.png"
        pause 0.1

        "gui/title/2bspace_cursor.png"
        pause 0.3
        "gui/title/2bspace.png"
        pause 0.1

        "gui/title/3bl_cursor.png"
        pause 0.2
        "gui/title/3bl.png"
        pause 0.1

        "gui/title/4blspace_cursor.png"
        pause 0.3
        "gui/title/4blspace.png"
        pause 0.1

        "gui/title/5bla_cursor.png"
        pause 0.2
        "gui/title/5bla.png"
        pause 0.1

        "gui/title/6blaspace_cursor.png"
        pause 0.3
        "gui/title/6blaspace.png"
        pause 0.1

        "gui/title/7blam_cursor.png"
        pause 0.2
        "gui/title/7blam.png"
        pause 0.1

        "gui/title/8blamspace_cursor.png"
        pause 0.3
        "gui/title/8blamspace.png"
        pause 0.1

        "gui/title/9blame_cursor.png"
        pause 0.5
        "gui/title/9blame.png"
        pause 0.5
        "gui/title/9blame_cursor.png"
        pause 0.5
        "gui/title/9blame.png"
        pause 0.5
        "gui/title/9blame_cursor.png"
        pause 0.5
        "gui/title/9blame.png"
        pause 0.5
        "gui/title/9blame_cursor.png"
        pause 0.5
        "gui/title/9blame.png"
        pause 0.5
        "gui/title/9blame_cursor.png"
        pause 0.5
        "gui/title/9blame.png"
        pause 0.5
        "gui/title/9blame_cursor.png"
        pause 0.5
        "gui/title/9blame.png"
        pause 0.5
        "gui/title/9blame_cursor.png"
        pause 0.5
        "gui/title/9blame.png"
        pause 0.5
        "gui/title/9blame_cursor.png"
        pause 0.5
        "gui/title/9blame.png"
        pause 0.5
        "gui/title/9blame_cursor.png"
        pause 0.5
        "gui/title/9blame.png"
        pause 0.5
        "gui/title/9blame_cursor.png"
        pause 0.5
        "gui/title/9blame.png"
        pause 0.5

        ## REVERSE ##
        "gui/title/9blame_cursor.png"
        pause 0.1
        "gui/title/8blamspace_cursor.png"
        pause 0.1
        "gui/title/7blam_cursor.png"
        pause 0.1
        "gui/title/6blaspace_cursor.png"
        pause 0.1
        "gui/title/5bla_cursor.png"
        pause 0.1
        "gui/title/4blspace_cursor.png"
        pause 0.1
        "gui/title/3bl_cursor.png"
        pause 0.1
        "gui/title/2bspace_cursor.png"
        pause 0.1
        "gui/title/1b_cursor.png"
        pause 0.1

        repeat

image ctc_animation = Animation("gui/ctc/ctc_11.png", 0.1, "gui/ctc/ctc_10.png", 0.1, "gui/ctc/ctc_9.png", 0.1, "gui/ctc/ctc_8.png", 0.1, "gui/ctc/ctc_7.png", 0.1, "gui/ctc/ctc_6.png", 0.1, "gui/ctc/ctc_5.png", 0.1, "gui/ctc/ctc_4.png", 0.1, "gui/ctc/ctc_3.png", 0.1, "gui/ctc/ctc_2.png", 0.1, "gui/ctc/ctc_1.png", 0.1, "gui/ctc/ctc_2.png", 0.1, "gui/ctc/ctc_3.png", 0.1, "gui/ctc/ctc_4.png", 0.1, "gui/ctc/ctc_5.png", 0.1, "gui/ctc/ctc_6.png", 0.1, "gui/ctc/ctc_7.png", 0.1, "gui/ctc/ctc_8.png", 0.1, "gui/ctc/ctc_9.png", 0.1, "gui/ctc/ctc_10.png", 0.1, xpos=632, ypos=567)

#sprites
image r temp = im.Scale("sprites/elf/elf_placeholder.png", 364, 534)
image r temp2 = im.Scale("sprites/elf/elf_placeholder2.png", 436, 534)
image g temp = im.Scale("sprites/vampire/vampire_placeholder.png", 276, 575)
image g temp2 = im.Scale("sprites/vampire/vampire_placeholder2.png", 263, 566)
image l temp = im.Scale("sprites/side/linus_placeholder.png", 414, 486)
image side pov temp = im.Scale("sprites/mc/mc_placeholder.png", 210, 291)
#image l temp = "sprites/other/linus_placeholder.png"

transform panelfromleft:
    delay 1.0

    on show:
        yalign 0.5 #y coord of image 0.5 is the center of the screen
        xalign -1.5 #starting x coord of image
        linear 0.3 xalign 0.5 #takes 0.3 s to align image to 0.6 on the x axis
    on hide:
        linear 0.5 xalign 1.0 alpha 0.0 #takes 0.5 second to move image to 1.0 and fade

transform panelfromtop:
    delay 1.0

    on show:
        yalign -2.5
        xalign 0.5
        linear 0.3 yalign 0.5
    on hide:
        linear 0.5 yalign 1.0 alpha 0.0

image amulet = "gui/title screen/gem.png"
image lick = im.Scale("cgs/vamp/aerated.png", 450, 393)# onlayer smoke1
image breath = im.Scale("cgs/vamp/breath.png", 322, 480)
