import pygame, win32api, win32gui, win32con, time

version = 0.3

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
fuchsia = (255, 0, 128)
hwnd = pygame.display.get_wm_info()["window"]

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (52, 204, 235)
orange = (242, 137, 31)
black = (0, 0, 0)
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
                        win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
  win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
  win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE)

def startLoop():     
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
  screen.fill(fuchsia)

def endLoop():
  pygame.display.update()

class Checkbox:

  def __init__(self, outsideColor, insideColor, x, y, width, height, enabledByDefault = False):
    self.outsideColor = outsideColor
    self.insideColor = insideColor
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.checkBox_enabled = enabledByDefault
    self.is_hoverable = False
    self.hover_color = gray
    self.boolMousePos = False

  def is_hovered(self, hoveredColor):
    self.is_hoverable = True
    self.hover_color = hoveredColor

  def printMousePos(self):
    self.boolMousePos = True

  def is_enabled(self):
    return self.checkBox_enabled

  def draw(self):
    pygame.draw.rect(screen, self.outsideColor, pygame.Rect(self.x - self.width/8, self.y - self.height/8, self.width + self.width/4, self.height + self.height/4))

    mouse = pygame.mouse

    if self.x + self.width > mouse.get_pos()[0] > self.x and self.y + self.height > mouse.get_pos()[1] > self.y:
      #When Hovered Over
      if self.is_hoverable:
        pygame.draw.rect(screen, self.hover_color, pygame.Rect(self.x - self.width/8, self.y - self.height/8, self.width + self.width/4, self.height + self.height/4))

      #When clicked
      if mouse.get_pressed()[0]:
        self.checkBox_enabled = not self.checkBox_enabled
        time.sleep(0.15)

    if self.checkBox_enabled:
      pygame.draw.rect(screen, self.insideColor, pygame.Rect(self.x, self.y, self.width, self.height))
      #pygame.draw.line(screen, orange, (100, 200), (150, 250), 3) #Checkmark
      #pygame.draw.line(screen, orange, (150, 250), (225, 100), 3) #Checkmark

    if self.boolMousePos:
      print(mouse.get_pos())

class Rect:
  
  def __init__(self, color, x, y, width, height):
    self.color = color
    self.x = x
    self.y = y
    self.width = width
    self.height = height
  
  def draw(self):
    pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

class Box:

  def __init__(self, color, x, y, width, height, thickness):
    self.color = color
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.thickness = thickness
  
  def draw(self):
    pygame.draw.line(screen, self.color, (self.x + self.width, self.y), (self.x, self.y), self.thickness) #Top
    pygame.draw.line(screen, self.color, (self.x, self.y + self.height), (self.x, self.y), self.thickness) #Left
    pygame.draw.line(screen, self.color, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), self.thickness) #Right
    pygame.draw.line(screen, self.color, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), self.thickness) #Bottom

