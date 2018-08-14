#!/usr/bin/python
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For http://bitforestinfo.blogspot.com
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
from TelnetBackend import TelnetBackend

__author__ = '''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.com/

    Note: We Feel Proud To Be Indian
######################################################
'''

# ========== Configurations ====================
BUTTON_BACKGROUND = "black"
MAIN_FRAME_BACKGROUND = "cornflowerblue"
BUTTON_LOOK = "flat"  # flat, groove, raised, ridge, solid, or sunken
TOP_BAR_TITLE = "Python Virtual KeyBoard."
TOPBAR_BACKGROUND = "skyblue"
TRANSPARENCY = 0.7
FONT_COLOR = "white"


# ==============================================

# import modules
# try:
#    import Tkinter
# except:
#    import tkinter as Tkinter
def colorToFloat(t):
    nt = ()
    for v in t:
        nt += ((1 / 255) * v,)
    return nt


import sys
import imgui
from imgui.integrations.nx import NXRenderer

sys.argv = [""]  # workaround needed for runpy
FILE_COLOR = colorToFloat((41, 128, 185))
# import pyautogui


keys = [
    [
        # =========================================
        # ===== Keyboard Configurations ===========
        # =========================================

        [
            # Layout Name
            ("Function_Keys"),

            # Layout Frame Pack arguments
            ({'side': 'top', 'expand': 'yes', 'fill': 'both'}),
            [
                # list of Keys
                ('esc', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12')
            ]
        ],

        [
            ("Character_Keys"),
            ({'side': 'top', 'expand': 'yes', 'fill': 'both'}),
            [
                ('`', ',', '.', '/', '-', '=', '\\', '[', ']', 'backspace'),
                ('~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '|'),
                ('tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '{', '}', ";", '\''),
                ('capslock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':', "\"", "enter"),
                ("shift", 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', '?', "shift"),
                ("ctrl", "win", 'alt', 'space  ', 'alt', 'win', '[=]', 'ctrl')
            ]
        ]
    ],
    [
        [
            ("System_Keys"),
            ({'side': 'top', 'expand': 'yes', 'fill': 'both'}),
            [
                (
                    "printscreen",
                    "scrolllock",
                    "pause"
                )
            ]
        ],
        [
            ("Editing_Keys"),
            ({'side': 'top', 'expand': 'yes', 'fill': 'both'}),
            [
                (
                    "insert",
                    "home",
                    "pageup"
                ),
                ("delete",
                 "end",
                 "pagedown"
                 ),

            ]
        ],

        [
            ("Navigation_Keys"),
            ({'side': 'top', 'expand': 'yes', 'fill': 'both'}),
            [
                (
                    "up",
                ),
                ("right",
                 "down",
                 "left"
                 ),
            ]
        ],

    ],
    [

        [
            ("Numeric_Keys"),
            ({'side': 'top', 'expand': 'yes', 'fill': 'both'}),
            [
                ("numlock", "/", "*"),
                ("7", "8", "9", "+"),
                ("4", "5", "6", "-"),
                ("1", "2", "3", "0"),
                (".", "enter")
            ]
        ],

    ]

]


# Create key event
def create_keyboard_event(numlock, capslock, controler, key):
    return

    # Function For Extracting Data From KeyBoard Table
    # and then provide us a well looking
    # keyboard gui


class Keyboard2:
    def __init__(self, MudData):
        self.InnerMudData = MudData

    # Function For Extracting Data From KeyBoard Table
    # and then provide us a well looking
    # keyboard gui
    def create_frames_and_buttons(self):
        # take section one by one
        for key_section in keys:
            # create Sperate Frame For Every Section
            # store_section = Tkinter.Frame(self)
            # store_section.pack(side='left', expand='yes', fill='both', padx=10, pady=10, ipadx=10, ipady=10)
            # imgui.begin_group()
            for layer_name, layer_properties, layer_keys in key_section:
                # store_layer = Tkinter.LabelFrame(store_section)  # , text=layer_name)
                # store_layer.pack(side='top',expand='yes',fill='both')
                # store_layer.pack(layer_properties)
                for key_bunch in layer_keys:
                    # store_key_frame = Tkinter.Frame(store_layer)
                    # store_key_frame.pack(side='top', expand='yes', fill='both')
                    imgui.begin_group()
                    for k in key_bunch:
                        k = k.capitalize()
                        if len(k) <= 3:
                            imgui.push_style_color(imgui.COLOR_BUTTON, *FILE_COLOR)
                            if imgui.button(k):
                                self.button_command(k)
                            imgui.pop_style_color(1)
                        else:
                            imgui.push_style_color(imgui.COLOR_BUTTON, *FILE_COLOR)
                            if imgui.button(k.center(5, ' ')):
                                self.button_command(k)
                            imgui.pop_style_color(1)
                        imgui.same_line()
                        # store_button['relief'] = BUTTON_LOOK
                        # store_button['bg'] = BUTTON_BACKGROUND
                        # store_button['fg'] = FONT_COLOR

                        # store_button['command'] = lambda q=k.lower(): self.button_command(q)
                        # store_button.pack(side='left', fill='both', expand='yes')
                    imgui.end_group()
            # imgui.end_group()

    # Function For Detecting Pressed Keyword.
    def button_command(self, keyboardKeyName):
        if len(keyboardKeyName) == 1:
            self.InnerMudData['Player_text'] += keyboardKeyName
        if keyboardKeyName.lower() == "enter":
            self.InnerMudData['Player_text_changed1'] = True
        if (keyboardKeyName.lower()) == "backspace":
            self.InnerMudData['Player_text'] = self.InnerMudData['Player_text'][:-1]
        if(keyboardKeyName.lower()) == "space":
            self.InnerMudData['Player_text'] += ' '


def MudClientWindow(MudData):
    # mud content
    MudData['World_text_changed'], MudData['World_text'] = imgui.input_text_multiline(
        '\n',
        MudData['World_text'],
        5000,
        1280,
        660,
        imgui.INPUT_TEXT_READ_ONLY
    )
    imgui.begin_group()
    imgui.text("Input:")
    imgui.same_line()
    MudData['Player_text_changed'], MudData['Player_text'] = imgui.input_text(
        '\n\n',
        MudData['Player_text'],
        1920,
        imgui.INPUT_TEXT_ENTER_RETURNS_TRUE
    )
    imgui.end_group()
    if imgui.button("keyboard"):
        imgui.open_popup("select-popup")


def Empty_PlayerInfo(MudData):
    texty_text = MudData['Player_text']
    MudData['Player_text'] = ''
    return texty_text


def GuiProcess(MudData, TelnetBack):
    if (MudData['Player_text_changed1'] == True):
        MudData['Player_text_changed'] = True
        MudData['Player_text_changed1'] = False

    if (MudData['Entered_server_data'] != True):
        if (MudData['Player_text_changed'] == True):
            server_data = [x.strip() for x in MudData['Player_text'].split(',')]
            MudData['server_host'] = server_data[0]
            MudData['server_port'] = server_data[1]
            if (TelnetBack.OpenIt() == True):
                MudData['Entered_server_data'] = True
                MudData['Clear_Player_data'] = True
    else:
        if (MudData['Player_text_changed'] == True):
            TelnetBack.SendMessage()
            MudData['Clear_Player_data'] = True
        TelnetBack.UpdateWorld()
        TelnetBack.PrintWorld()


def PostGuiStuff(MudData):
    if (MudData['Clear_Player_data'] == True):
        Empty_PlayerInfo(MudData)
        MudData['Clear_Player_data'] = False


def main():
    renderer = NXRenderer()
    # My stuff

    MudData = {
        'Player_text': 'towel.blinkenlights.nl,23',
        'Player_text_changed': False,
        'Player_text_changed1': False,
        'World_text': 'Please Enter the server info like this: serverhost.port',
        'World_text_changed': False,
        'server_host': '',
        'server_port': 0,
        'Entered_server_data': False,
        'Clear_Player_data': False
    }
    keyboardInner = Keyboard2(MudData)
    TelnetSetup = TelnetBackend(MudData)
    # End Of my stuff
    while True:
        renderer.handleinputs()

        imgui.new_frame()

        width, height = renderer.io.display_size
        imgui.set_next_window_size(width, height)
        imgui.set_next_window_position(0, 0)
        imgui.begin("",
                    flags=imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_SAVED_SETTINGS)

        MudClientWindow(MudData)
        GuiProcess(MudData, TelnetSetup)
        if imgui.begin_popup("select-popup"):
            keyboardInner.create_frames_and_buttons()
            imgui.end_popup()
        imgui.end()

        imgui.render()

        renderer.render()
        PostGuiStuff(MudData)

    renderer.shutdown()


# ##  Frame Class
# class Keyboard(Tkinter.Frame):
#     def __init__(self, *args, **kwargs):
#         Tkinter.Frame.__init__(self, *args, **kwargs)
#
#         # Function For Creating Buttons
#         self.create_frames_and_buttons()
#
#     # Function For Extracting Data From KeyBoard Table
#     # and then provide us a well looking
#     # keyboard gui
#     def create_frames_and_buttons(self):
#         # take section one by one
#         for key_section in keys:
#             # create Sperate Frame For Every Section
#             store_section = Tkinter.Frame(self)
#             store_section.pack(side='left', expand='yes', fill='both', padx=10, pady=10, ipadx=10, ipady=10)
#
#             for layer_name, layer_properties, layer_keys in key_section:
#                 store_layer = Tkinter.LabelFrame(store_section)  # , text=layer_name)
#                 # store_layer.pack(side='top',expand='yes',fill='both')
#                 store_layer.pack(layer_properties)
#                 for key_bunch in layer_keys:
#                     store_key_frame = Tkinter.Frame(store_layer)
#                     store_key_frame.pack(side='top', expand='yes', fill='both')
#                     for k in key_bunch:
#                         k = k.capitalize()
#                         if len(k) <= 3:
#                             store_button = imgui.button(store_key_frame, text=k, width=2, height=2)
#                         else:
#                             store_button = imgui.button(store_key_frame, text=k.center(5, ' '), height=2)
#                         if " " in k:
#                             store_button['state'] = 'disable'
#
#                         store_button['relief'] = BUTTON_LOOK
#                         store_button['bg'] = BUTTON_BACKGROUND
#                         store_button['fg'] = FONT_COLOR
#
#                         store_button['command'] = lambda q=k.lower(): self.button_command(q)
#                         store_button.pack(side='left', fill='both', expand='yes')
#         return
#
#     # Function For Detecting Pressed Keyword.
#     def button_command(self, event):
#         pyautogui.press(event)
#         return
#

# class top_moving_mechanism:
#     def __init__(self, root, label):
#         self.root = root
#         self.label = label
#
#     def motion_activate(self, kwargs):
#         w, h = (self.root.winfo_reqwidth(), self.root.winfo_reqheight())
#         (x, y) = (kwargs.x_root, kwargs.y_root)
#         self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))
#         return
#

if __name__ == "__main__":
    main()
