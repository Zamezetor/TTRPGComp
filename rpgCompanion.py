# Imports
import random, json, math, PIL
import guizero as gz
import tkinter as tk


# Variables

# Classes
class mainApp():
  def __init__(self,width,height):
    self.width = width
    self.height = height
    self.running = True
     
    # Opens Settings
    self.reminders_file = open("./datapacks/data/reminders.json", "r") 
    self.datapack_file = open("./datapacks/data/default.json", "r")
    self.settings_file = open("./settings.json", "r")
    settings = json.load(self.settings_file)
    print(settings)
    if settings["dark-mode"]:
      bg = "#6C6C6C"
    else:
      bg = "#ffffff"

    self.app = gz.App(title = "TTRPG Companion", width = width, height = height, layout = "grid", bg = bg, visible = True)


  def adjust_size(self):
    self.width = self.app.width
    self.height = self.app.height


  def isRunning(self):
    while self.running:
      self.app.when_resized = self.adjust_size()
      self.info_width = (self.width/3)
      self.opts_width =  self.info_width/3
      self.init_width = width - (self.info_width + self.opts_width)
      

      info_box = gz.Box(self.app, grid = [0, 0], width = self.info_width, height = height, layout = "grid")
      init_box = gz.Box(self.app, grid = [1, 0], width = self.init_width, height = height, layout = "grid", border = 1, )
      opts_box = gz.Box(self.app, grid = [2, 0], width = self.opts_width, height = height, layout = "grid")

      time_box        = gz.Box(info_box, grid = [0, 0], width = self.info_width, height = self.info_width/4, layout = "grid")
      icon_box_1      = gz.Box(info_box, grid = [0, 1], width = self.info_width, height = self.info_width/2, layout = "grid")
      empty_box       = gz.Box(info_box, grid = [0, 2], width = self.info_width, height = (self.height-self.info_width-8), layout = "grid")
      progression_box = gz.Box(info_box, grid = [0, 3], width = self.info_width, height = self.info_width/4 , layout = "grid")

      weather_current = "clear.png"
      seasons_current = "spring.png"
      regions_current = "plains.png"
      terrain_current = "flat.png"

      weather_icon = gz.Picture(icon_box_1, grid = [0, 0], image = f"./datapacks/icons/weather/{weather_current}", width = int(self.info_width/2), height = int(self.info_width/4))
      season_icon  = gz.Picture(icon_box_1, grid = [1, 0], image = f"./datapacks/icons/seasons/{seasons_current}", width = int(self.info_width/2), height = int(self.info_width/4))
      region_icon  = gz.Picture(icon_box_1, grid = [0, 1], image = f"./datapacks/icons/regions/{regions_current}", width = int(self.info_width/2), height = int(self.info_width/4))
      terrain_icon = gz.Picture(icon_box_1, grid = [1, 1], image = f"./datapacks/icons/terrain/{terrain_current}", width = int(self.info_width/2), height = int(self.info_width/4))

      def showApp(self):
        self.app.display()

# Functions
def getScreen(): 
  # Spawn Tkinter window, take screen width and height, kill Tkinter window
  root = tk.Tk()
  width = root.winfo_screenwidth()
  height = root.winfo_screenheight()
  root.destroy()
  return width, height

# Code
width, height = getScreen()
application = mainApp(width, height)
application.showApp()

  
