# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:
    tag menu

    add "gui/title screen/gem.png"
    add "smoke bottom"
    add "smoke top" # Add a background image for the main menu.
    add "glitch"
    add "BLAME_title" xpos 160 ypos 218

    $ y = 280 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/start/start_%s.png" xpos 140 ypos y focus_mask True action Start() #hovered# [()] unhovered [()]
    imagebutton auto "gui/start/load_%s.png" xpos 267 ypos y focus_mask True  action ShowMenu('load')# hovered [()] unhovered [()]
    imagebutton auto "gui/start/config_%s.png" xpos 394 ypos y focus_mask True action ShowMenu('preferences')# hovered [()] unhovered [()]
    imagebutton auto "gui/start/quit_%s.png" xpos 521 ypos y focus_mask True action Quit(confirm=False)# hovered [()] unhovered [()]
    textbutton "Gallery" xpos 200 ypos 400 action ShowMenu("gallery")
##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:
    $ x = 679
    imagebutton auto "gui/navi/navi_mm_%s.png" xpos x ypos 151 focus_mask True action MainMenu() at nav_t
    imagebutton auto "gui/navi/navi_save_%s.png" xpos x ypos 201 focus_mask True action ShowMenu('save') at nav_t
    imagebutton auto "gui/navi/navi_load_%s.png" xpos x ypos 251 focus_mask True action ShowMenu('load') at nav_t
    imagebutton auto "gui/navi/navi_config_%s.png" xpos x ypos 301 focus_mask True action ShowMenu('preferences') at nav_t
    imagebutton auto "gui/navi/navi_return_%s.png" xpos x ypos 350 focus_mask True action Return() at nav_t
    imagebutton auto "gui/navi/navi_quit_%s.png" xpos x ypos 441 focus_mask True action Quit() at nav_t

# The code below defines the ATL transform effects for the buttons on the game menu. These effects are triggered when we hover the mouse over them (hover and selected_hover). Effects that are triggered by idle and selected_idle events (when we stop hovering the mouse over them) ensure that the buttons are moved back to the initial state.
#begin nav_eff
init -2:
    transform nav_t:
        on idle:
            easein 0.0 xpos 679
        on selected_idle:
            easein 0.0 xpos 679
        on hover:
            easein 0.1 xpos 679
            easein 0.3 xpos 639
        on selected_hover:
            easein 0.1 xpos 679
        on insensitive:
            easein 0.0 xpos 679

#end nav_eff
## ■██▓▒░ SAVE / LOAD SLOT ░▒▓██████████████████████████████■
## This represents a load/save slot. You should customize this to ensure that the placement of the thumbnail and the slot text are as desired. Positions (x1, y1, x2 and y2) are relative to the x, y parameters, that are passed when the screen is called. To set the screenshot thumbnail size see options.rpy.
init -2 python: #we initialize x and y, so the load_save_slot screen below works at startup
    x=0
    y=0

#screen load_save_slot:
#    $ file_text = "%s\n%s" % (FileSaveName(number), FileTime(number, empty="Empty."))
#    add FileScreenshot(number) xpos x ypos y
#    $x2=x+15
#    $y2=y+345
#    text file_text xalign 0.445 ypos y2

screen load_save_slot:
    $ file_other_text = "{size=+4}%s{/size}" % (FileSaveName(number, empty="Empty.")) #displays value assigned to "save_name"
    $ file_text = "%s" % (FileTime(number, empty="Nothing to see here.")) #This is time of save
    add FileScreenshot(number) xpos x ypos y
    $x2=x+15
    $y2=y+358
    $y3=y+333
    text file_other_text xalign 0.5 ypos y3
    text file_text xalign 0.5 ypos y2

## ■██▓▒░ SAVE SCREEN ░▒▓███████████████████████████████████■
image title_save:
    "gui/sl/title_save_2.png"
    pause 0.5
    "gui/sl/title_save_1.png"
    pause 0.5
    repeat

screen save:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/ground.png" # We add the file picker background image. This image is the same for save and load screens.
    add "smoke bottom"
    add "smoke top"
    add "title_save" xpos 360 ypos 51 # We add the save title image on top of the background
    use file_picker # We include the file_picker screen

## ■██▓▒░ LOAD SCREEN ░▒▓███████████████████████████████████■
image title_load:
    "gui/sl/title_load_2.png"
    pause 0.5
    "gui/sl/title_load_1.png"
    pause 0.5
    repeat

screen load:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/ground.png"
    add "smoke bottom"
    add "smoke top"
    add "title_load" xpos 350 ypos 51
    use file_picker

## ■██▓▒░ SAVE / LOAD FILE PICKER ░▒▓███████████████████████■
## Since saving and loading are so similar, we combine them into a single screen, file_picker. We then use the file_picker screen from simple load and save screens.
screen file_picker:
    use navigation # We include the navigation/game menu screen
    add "gui/sl/info_box.png" xpos 188 ypos 462
    add "gui/sl/sl_lines.png" xpos 200 ypos 470
    text "Pages" xpos 62 ypos 189 size 30
    #add "gui/sl/title_pages.png" xpos 69 ypos 189
    # Buttons for selecting the save/load page:
    imagebutton auto "gui/sl/filepage_%s.png" xpos 68 ypos 240 focus_mask True action FilePage(1)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 68 ypos 260 focus_mask True action FilePage(2)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 68 ypos 280 focus_mask True action FilePage(3)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 68 ypos 300 focus_mask True action FilePage(4)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 68 ypos 320 focus_mask True action FilePage(5)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 68 ypos 340 focus_mask True action FilePage(6)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 68 ypos 360 focus_mask True action FilePage(7)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 68 ypos 380 focus_mask True action FilePage(8)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 68 ypos 400 focus_mask True action FilePage(9)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 68 ypos 420 focus_mask True action FilePage(10)

    imagebutton auto "gui/sl/filepage_%s.png" xpos 99 ypos 240 focus_mask True action FilePage(11)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 99 ypos 260 focus_mask True action FilePage(12)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 99 ypos 280 focus_mask True action FilePage(13)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 99 ypos 300 focus_mask True action FilePage(14)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 99 ypos 320 focus_mask True action FilePage(15)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 99 ypos 340 focus_mask True action FilePage(16)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 99 ypos 360 focus_mask True action FilePage(17)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 99 ypos 380 focus_mask True action FilePage(18)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 99 ypos 400 focus_mask True action FilePage(19)
    imagebutton auto "gui/sl/filepage_%s.png" xpos 99 ypos 420 focus_mask True action FilePage(20)

    for i in range(0, 1): # This repeats the block below 3 times (counts from 0 to 2), for the 3 save slots. We could also copy/paste the block below 3 times, but we are too lazy to do that.
        imagebutton auto "gui/sl/fileslot_%s.png" xpos 200 ypos 151 focus_mask True action FileAction(i)
        use load_save_slot(number=i, x=200, y=151) # This calls the load_save_slot screen defined above. We pass variable i as the slot number and x, y coordinates.

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
image settings:
        "gui/settings/title.png"
        pause 0.5
        "gui/settings/title_cursor.png"
        pause 0.5
        repeat

screen preferences:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/ground.png" # We add the image that is shown in the background of the preferences screen.
    add "smoke bottom"
    add "smoke top"
    add "gui/settings/box.png" xpos 69 ypos 150
    add "settings" xpos 327 ypos 51
    add "gui/settings/settings_overlay.png" xpos 164 ypos 182
    use navigation # We include the navigation screen (game menu)
    # Display windowed/full screen:
    imagebutton auto "gui/settings/fullscreen_%s.png" xpos 217 ypos 332 focus_mask None action Preference('display', 'fullscreen') hovered [()] unhovered [()] #at config_eff
    imagebutton auto "gui/settings/windowed_%s.png" xpos 204 ypos 362 focus_mask None action Preference('display', 'window') hovered [()] unhovered [()] #at config_eff
    # Transitions on/off:
    imagebutton auto "gui/settings/notransitions_%s.png" xpos 398 ypos 332 focus_mask None action Preference('transitions', 'none') hovered [()] unhovered [()] #at config_eff
    imagebutton auto "gui/settings/alltransitions_%s.png" xpos 399 ypos 362 focus_mask None action Preference('transitions', 'all') hovered [()] unhovered [()] #at config_eff
    # Skip all/seen text
    imagebutton auto "gui/settings/skipseen_%s.png" xpos 205 ypos 412 focus_mask None action Preference('skip', 'seen') hovered [()] unhovered [()] #at config_eff
    imagebutton auto "gui/settings/skipall_%s.png" xpos 222 ypos 442 focus_mask None action Preference('skip', 'all') hovered [()] unhovered [()] #at config_eff
    # Stop/continue skipping after choices
    imagebutton auto "gui/settings/stopafter_%s.png" xpos 388 ypos 412 focus_mask None action Preference('after choices', 'stop') hovered [()] unhovered [()] #at config_eff
    imagebutton auto "gui/settings/skipafter_%s.png" xpos 391 ypos 442 focus_mask None action Preference('after choices', 'skip') hovered [()] unhovered [()] #at config_eff
    # Button to begin skipping. Only active/visible if the game is started. Image config_begin_skipping_insensitive.png is used when the button is not active.
    #imagebutton auto "gui/config_begin_skipping_%s.png" xpos 420 ypos 117 focus_mask True action Preference('begin skipping') hovered [ Play ("test_one", "sfx/click.wav") ] unhovered [()]
    # imagebutton auto "gui/config_skip_all_%s.png" xpos 591 ypos 345 focus_mask True action Preference('skip', 'all') at config_eff hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_go_skip.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
    # bar sliders for volume control, text speed and auto-forward time
    frame xpos 104 ypos 203:
        style_group "pref"
        has vbox
        bar value Preference("music volume")
    frame xpos 334 ypos 203:
        style_group "pref"
        has vbox
        bar value Preference("sound volume")
    frame xpos 124 ypos 263:
        style_group "pref"
        has vbox
        bar value Preference("text speed")
    frame xpos 354 ypos 263:
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time")


init -2 python:
    # Styling for the bar sliders:
    # Aleema's Customizing Menus tutorial: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
    # Bar style properties documentation: http://www.renpy.org/doc/html/style.html#bar-style-properties
    style.pref_frame.background = None
    style.pref_slider.left_bar = "gui/settings/full_idle.png" #full
    style.pref_slider.right_bar = "gui/settings/empty_idle.png"
    style.pref_slider.hover_left_bar = "gui/settings/full_hover.png" #full
    style.pref_slider.hover_right_bar = "gui/settings/empty_hover.png"
    style.pref_slider.thumb = "gui/settings/thumb.png"
    style.pref_slider.hover_thumb = "gui/settings/thumb.png"
    style.pref_slider.thumb_shadow = None
    style.pref_slider.thumb_offset = 0
    style.pref_slider.xmaximum = 186
    style.pref_slider.ymaximum = 19

## ■██▓▒░ YES/NO PROMPT ░▒▓█████████████████████████████████■
## Screen that asks the user a yes or no question. You'll need to edit this to change the position and style of the text.
## http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    #on "show" action Play("sound", "sfx/alert.wav")
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.

    add "gui/yn/yesno_ground.png"
    imagebutton auto "gui/yn/yesno_yes_%s.png" xpos 363 ypos 320 action yes_action at yn_y_t
    imagebutton auto "gui/yn/yesno_no_%s.png" xpos 363 ypos 360 action no_action at yn_n_t

    if message == layout.ARE_YOU_SURE:
        add "gui/yn/yesno_are_you_sure.png"
    elif message == layout.DELETE_SAVE:
        add "gui/yn/yesno_delete_save.png"
    elif message == layout.OVERWRITE_SAVE:
        add "gui/yn/yesno_overwrite_save.png"
    elif message == layout.LOADING:
        add "gui/yn/yesno_loading.png"
    elif message == layout.QUIT:
        add "gui/yn/yesno_quit.png"
    elif message == layout.MAIN_MENU:
        add "gui/yn/yesno_main_menu.png"

init -2:
    transform yn_y_t:
        on idle:
            easein 0.0 ypos 320
        on hover:
            easein 0.0 ypos 320
            easein 0.0 ypos 316

    transform yn_n_t:
        on idle:
            easein 0.0 ypos 360
        on hover:
            easein 0.0 ypos 360
            easein 0.0 ypos 356


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
