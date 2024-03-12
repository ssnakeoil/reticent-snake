
#characters

define narrator = Character(None, ctc="ctc_animation", ctc_position="fixed")
define ga = Character('Gabriel', ctc="ctc_animation", ctc_position="fixed")
define j = Character('Julia', ctc="ctc_animation", ctc_position="fixed")
define l = Character('Linus', ctc="ctc_animation", ctc_position="fixed")
define r = Character('Ragna', ctc="ctc_animation", ctc_position="fixed")
define rs = Character('???', ctc="ctc_animation", ctc_position="fixed")
define tf = Character('figure', ctc="ctc_animation", ctc_position="fixed")

init:

    $ gabriel = 0
    $ ragna = 0

    $ truthful = 0
    $ guarded = 0

    $ trusting = 0
    $ independent = 0
    $ compliant = 0

    $ amulet = False
    $ aunt = False
    $ mom = False
    $ flesh = True
    $ oldguides = False
    $ likeness = False
    $ accident = False

    $ empath = False
    $ necro = False
    $ heal = False
    $ nature = False
