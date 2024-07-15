import random

import pygame, win32api, win32gui, win32con, time

# A storage dict, stores all buttons, checkboxes.
# Enabled draw_gui function, which draws all elements in the dict.
# And the major update --- Callback function.
# Now, instead of manually checking the status and run a function,
# which would lead to code duplication and stability problems
# You can just assign a function to the element's "callback" attribute,
# and it will be called ONCE when the element is altered.
#
# It stores all the objects

widgets = []

version = 0.4

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
fuchsia = (255, 0, 128)
hwnd = pygame.display.get_wm_info()["window"]

programIcon = pygame.image.load('icon.png')

pygame.display.set_icon(programIcon)

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (52, 204, 235)
orange = (242, 137, 31)
black = (0, 0, 0)
yellow = (255, 255, 0)
gray = (61, 61, 61)
lightgray = (110, 110, 110)
darkgray = (41, 41, 41)
purple = (133, 55, 250)


def init():
    pygame.init()
    pygame.display.set_caption('oGUI window')
    print('')
    print(f'OverlayGUI {version}')
    print('oGUI package by EthanEDITS')
    print('')


win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd,
                                              win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TOOLWINDOW)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE)


def startLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    screen.fill(fuchsia)


def endLoop():
    pygame.display.update()


class WidgetBasics:
    def __init__(self, is_hidden=False):
        global widgets
        widgets.append(self)

    def hide(self):
        self.is_hidden = True

    def show(self):
        self.is_hidden = False


class Rect(WidgetBasics):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.callable = False
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


class Box(WidgetBasics):

    def __init__(self, color, x, y, width, height, thickness):
        super().__init__()
        self.callable = False
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.thickness = thickness

    def draw(self):
        pygame.draw.line(screen, self.color, (self.x + self.width, self.y), (self.x, self.y), self.thickness)  # Top
        pygame.draw.line(screen, self.color, (self.x, self.y + self.height), (self.x, self.y), self.thickness)  # Left
        pygame.draw.line(screen, self.color, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height),
                         self.thickness)  # Right
        pygame.draw.line(screen, self.color, (self.x, self.y + self.height),
                         (self.x + self.width, self.y + self.height), self.thickness)  # Bottom


class Text(WidgetBasics):

    def __init__(self, color, x, y, FontSize, textStr, dropShadowEnabled=True, textAlign=0, verticalAlign=0):
        super().__init__()
        pygame.font.init()
        self.callable = False
        self.color = color
        self.x = x
        self.y = y
        self.FontSize = FontSize
        self.textStr = textStr
        self.FontString = 'Roboto'
        self.dropShadowColor = black
        self.dropShadowOffset = 2
        self.dropShadowEnabled = dropShadowEnabled
        self.textAlign = textAlign
        self.verticalAlign = verticalAlign

    def font(self, fontStr):
        self.FontString = fontStr

    def dropShadow(self, color, offset):
        self.dropShadowEnabled = True
        self.dropShadowColor = color
        self.dropShadowOffset = offset

    def setTextAlign(self, textAlign):
        self.textAlign = textAlign

    def setVerticalAlign(self, verticalAlign):
        self.verticalAlign = verticalAlign

    def draw(self):
        myfont = pygame.font.SysFont(self.FontString, self.FontSize)
        textSurface = myfont.render(self.textStr, True, self.color)  # Main Text
        text_w, text_h = myfont.size(self.textStr)
        textRect = textSurface.get_rect()

        if self.textAlign == 0:
            x = self.x  # Left Align
        elif self.textAlign == 1:
            x = self.x - text_w // 2  # Center
        elif self.textAlign == 2:
            x = self.x - text_w  # Right Align

        if self.verticalAlign == 0:
            y = self.y  # Top Align
        elif self.verticalAlign == 1:
            y = self.y - text_h // 2  # Center
        elif self.verticalAlign == 2:
            y = self.y - text_h  # Bottom Align

        textRect = (x, y)

        if self.dropShadowEnabled:
            textSurface2 = myfont.render(self.textStr, True, black)  # DropShadow
            textRect2 = (textRect[0] + self.dropShadowOffset, textRect[1])
            screen.blit(textSurface2, textRect2)  # DropShadow

        screen.blit(textSurface, textRect)  # Text


class Button(WidgetBasics):
    # since the term 'press' emphasizes the hold action, and click is more appropriate for a single action,
    # the handle-anti-multi-trigger-per-click variables is names after 'press', while the callback is names after click
    def __init__(self, color, clickedColor, x, y, width=None, height=30, text='', clicked_callback=None):
        super().__init__()
        self.type = 'button'
        self.clicked_callback = clicked_callback
        self.callable = True
        self.last_frame_pressed = False
        self.color = color
        self.clickedColor = clickedColor
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        w, h = pygame.font.SysFont('Roboto', int(self.height)).size(text)
        if not self.width:
            self.width = w + 10
        self.text_widget = Text(self.clickedColor, self.x + self.width // 2, self.y + self.height // 2, self.height,
                                text, verticalAlign=1, textAlign=1)

        self.is_hoverable = True
        self.hover_color = (self.clickedColor[0] / 2, self.clickedColor[1] / 2, self.clickedColor[2] / 2)
        self.pressed = False

    def is_enabled(self):
        return self.pressed

    def is_hovered(self, hoveredColor):
        self.is_hoverable = True
        self.hover_color = hoveredColor

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        mouse = pygame.mouse

        if self.x + self.width > mouse.get_pos()[0] > self.x and self.y + self.height > mouse.get_pos()[1] > self.y:
            if self.is_hovered:
                pygame.draw.rect(screen, self.hover_color, pygame.Rect(self.x, self.y, self.width, self.height))

            if mouse.get_pressed()[0]:
                self.pressed = True
                pygame.draw.rect(screen, self.clickedColor, pygame.Rect(self.x, self.y, self.width, self.height))
            else:
                self.pressed = False


class Checkbox(WidgetBasics):
    def __init__(self, outsideColor, insideColor, x, y, width, height, text=None, checked_callback=None,
                 toggled_callback=None, checkedByDefault=False):
        super().__init__()
        self.callable = True
        self.checked_callback = checked_callback
        self.toggled_callback = toggled_callback
        self.type = 'checkbox'
        self.last_frame_checked = checkedByDefault
        self.outsideColor = outsideColor
        self.insideColor = insideColor
        self.x = x
        self.y = y
        self.mouse_holding = False
        self.width = width
        self.height = height
        self.checked = checkedByDefault
        self.is_hoverable = True
        self.hover_color = (self.insideColor[0] / 2, self.insideColor[1] / 2, self.insideColor[2] / 2)
        self.boolMousePos = False

        w, h = pygame.font.SysFont('Roboto', int(self.height)).size(text)
        self.text_widget = Text(self.insideColor, self.x + 10 + self.width, self.y + self.height // 2, self.height,
                                text, verticalAlign=1, textAlign=0)

    def is_hovered(self, hoveredColor):
        self.is_hoverable = True
        self.hover_color = hoveredColor

    def printMousePos(self):
        self.boolMousePos = True

    def is_enabled(self):
        return self.checked

    def draw(self):
        pygame.draw.rect(screen, self.outsideColor,
                         pygame.Rect(self.x - self.width / 8, self.y - self.height / 8, self.width + self.width / 4,
                                     self.height + self.height / 4))

        mouse = pygame.mouse

        if self.x + self.width > mouse.get_pos()[0] > self.x and self.y + self.height > mouse.get_pos()[1] > self.y:
            # When Hovered Over
            if self.is_hoverable:
                pygame.draw.rect(screen, self.hover_color,
                                 pygame.Rect(self.x - self.width / 8, self.y - self.height / 8,
                                             self.width + self.width / 4, self.height + self.height / 4))

            # When clicked + check if mouse was continuously held in the previous frames
            if mouse.get_pressed()[0]:
                if not self.mouse_holding:
                    self.checked = not self.checked
                self.mouse_holding = True
            else:
                self.mouse_holding = False

        if self.checked:
            pygame.draw.rect(screen, self.insideColor, pygame.Rect(self.x, self.y, self.width, self.height))

        if self.boolMousePos:
            print(mouse.get_pos())


def update_gui():
    # the startLoop and endLoop would not be included in this function. 
    # In case the use creates something else not via this library but using pygame itself,
    # they can use the startLoop and endLoop to wrap around their own code
    for i in widgets:
        i.draw()
    handle_gui_alter()


def handle_checkbox_callback(checkbox_object):
    if checkbox_object.last_frame_checked != checkbox_object.checked:
        if checkbox_object.toggled_callback:
            checkbox_object.toggled_callback()  # this line executes the callback function while the last detects if there is one
        if checkbox_object.checked:
            if checkbox_object.checked_callback:
                checkbox_object.checked_callback()

        checkbox_object.last_frame_checked = checkbox_object.checked


def handle_button_callback(button_object):
    if button_object.last_frame_pressed != button_object.pressed:
        if button_object.pressed:
            if button_object.clicked_callback:
                button_object.clicked_callback()
        button_object.last_frame_pressed = button_object.pressed


def handle_gui_alter():
    for i in widgets:
        if i.callable:
            if i.type == 'checkbox':
                handle_checkbox_callback(i)
            if i.type == 'button':
                handle_button_callback(i)
