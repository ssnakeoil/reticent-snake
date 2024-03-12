# shit doesn't make sense yet, but it will eventually
init python:

    g = Gallery()

    g.button("title")
    g.image("cgs/locked.png")

    g.button("vcg1")
    g.condition("persistent.vcg1")
    g.image("cgs/vamp/vampire meeting.png")

    g.button("vcg2")
    g.condition("persistent.vcg2")
    g.image("breath")

    g.button("vcg3")
    g.condition("persistent.vcg3")
    g.image("lick")

    g.transition = dissolve

screen gallery:
    tag menu

    add "gui/title screen/gem.png"
    add "smoke bottom"
    add "smoke top"
    add "gui/settings/box.png" xpos 69 ypos 150
    use navigation

    textbutton "Gabriel" xalign 0.5 yalign 0.5 action ShowMenu("gabegallery")

screen gabegallery:

    tag menu

    add "gui/title screen/gem.png"
    add "smoke bottom"
    add "smoke top"
    add "gui/settings/box.png" xpos 69 ypos 150
    use navigation

    add g.make_button("vcg1","cgs/vamp/vampire meeting small.png", locked = "cgs/locked.png", xpos=176, ypos=182)
    add g.make_button("vcg2", "cgs/vamp/breath small.png", locked = "cgs/locked.png", xpos=400, ypos=182)
    add g.make_button("vcg3", "cgs/vamp/aerated small.png", locked = "cgs/locked.png", xpos=176, ypos=300)
