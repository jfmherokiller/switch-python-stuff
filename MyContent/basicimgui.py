# -*- coding: utf-8 -*-
from typing import Dict, Union
from MyContent.TelnetBackend import TelnetBackend

import os

os.environ["PYSDL2_DLL_PATH"] = "C:/Users/peter/PycharmProjects/SwitchStuff"
from sdl2 import *
import ctypes
import OpenGL.GL as gl

import imgui

from imgui.integrations.sdl2 import SDL2Renderer
import string


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
                ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'),
                ('tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '{', '}', ";", '\''),
                ('capslock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':', "\"", "enter"),
                ("lshift", 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', '?', "rshift"),
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
]



def colorToFloat(t):
    nt = ()
    for v in t:
        nt += ((1 / 255) * v,)
    return nt


FILE_COLOR = colorToFloat((41, 128, 185))


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
                            if not self.InnerMudData['Shift_enabled']:
                                k = k.lower()
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
        if self.InnerMudData['Shift_enabled']:
            self.InnerMudData['Shift_enabled'] = False
        if len(keyboardKeyName) == 1:
            self.InnerMudData['Player_text'] += keyboardKeyName
        if keyboardKeyName.lower() == "enter":
            self.InnerMudData['Player_text_changed1'] = True
        if (keyboardKeyName.lower()) == "backspace":
            self.InnerMudData['Player_text'] = self.InnerMudData['Player_text'][:-1]
        if (keyboardKeyName.lower()) == "space  ":
            self.InnerMudData['Player_text'] += ' '
        if (keyboardKeyName.lower() == "lshift") or (keyboardKeyName.lower() == "rshift"):
            self.InnerMudData['Shift_enabled'] = True



def MudClientWindow(MudData):
    # mud content
    MudData['World_text_changed'], MudData['World_text'] = imgui.input_text_multiline(
        '\n',
        MudData['World_text'],
        50000,
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

def PostGuiStuff(MudData):
    if (MudData['Clear_Player_data'] == True):
        Empty_PlayerInfo(MudData)
        MudData['Clear_Player_data'] = False

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

        TelnetBack.UpdateWorld()
        TelnetBack.PrintWorld()

def main():
    window, gl_context = impl_pysdl2_init()
    renderer = SDL2Renderer(window)
    # My stuff

    MudData = {
        'Player_text': '',
        'Player_text_changed': False,
        'Player_text_changed1': False,
        'World_text': 'Please Enter the server info like this: serverhost.port',
        'World_text_changed': False,
        'server_host': '',
        'server_port': 0,
        'Entered_server_data': False,
        'Clear_Player_data': False,
        'Shift_enabled': False
    }
    keyboardInner = Keyboard2(MudData)
    TelnetSetup = TelnetBackend(MudData)
    # End Of my stuff
    running = True
    event = SDL_Event()

    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break
            renderer.process_event(event)
        renderer.process_inputs()

        imgui.new_frame()

        if imgui.begin_main_menu_bar():
            if imgui.begin_menu("File", True):

                clicked_quit, selected_quit = imgui.menu_item(
                    "Quit", 'Cmd+Q', False, True
                )

                if clicked_quit:
                    exit(1)

                imgui.end_menu()
            imgui.end_main_menu_bar()

        # imgui.show_test_window()

        imgui.begin("Mudlet Window")
        MudClientWindow(MudData)
        GuiProcess(MudData, TelnetSetup)
        if imgui.begin_popup("select-popup"):
            keyboardInner.create_frames_and_buttons()
            imgui.end_popup()
        imgui.end()

        gl.glClearColor(1., 1., 1., 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()

        SDL_GL_SwapWindow(window)
        PostGuiStuff(MudData)
    renderer.shutdown()
    SDL_GL_DeleteContext(gl_context)
    SDL_DestroyWindow(window)
    SDL_Quit()


def impl_pysdl2_init():
    width, height = 1920, 1050
    window_name = "minimal ImGui/SDL2 example"

    if SDL_Init(SDL_INIT_EVERYTHING) < 0:
        print("Error: SDL could not initialize! SDL Error: " + SDL_GetError())
        exit(1)

    SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1)
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24)
    SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 8)
    SDL_GL_SetAttribute(SDL_GL_ACCELERATED_VISUAL, 1)
    SDL_GL_SetAttribute(SDL_GL_MULTISAMPLEBUFFERS, 1)
    SDL_GL_SetAttribute(SDL_GL_MULTISAMPLESAMPLES, 16)
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_FLAGS, SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG)
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 4)
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 1)
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE)

    SDL_SetHint(SDL_HINT_MAC_CTRL_CLICK_EMULATE_RIGHT_CLICK, b"1")
    SDL_SetHint(SDL_HINT_VIDEO_HIGHDPI_DISABLED, b"1")

    window = SDL_CreateWindow(window_name.encode('utf-8'),
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              width, height,
                              SDL_WINDOW_OPENGL | SDL_WINDOW_RESIZABLE)

    if window is None:
        print("Error: Window could not be created! SDL Error: " + SDL_GetError())
        exit(1)

    gl_context = SDL_GL_CreateContext(window)
    if gl_context is None:
        print("Error: Cannot create OpenGL Context! SDL Error: " + SDL_GetError())
        exit(1)

    SDL_GL_MakeCurrent(window, gl_context)
    if SDL_GL_SetSwapInterval(1) < 0:
        print("Warning: Unable to set VSync! SDL Error: " + SDL_GetError())
        exit(1)

    return window, gl_context


if __name__ == "__main__":
    main()
