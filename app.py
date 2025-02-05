import random, json, re
import guizero as gz
from pathlib import Path

class mainApp():
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.startup()
    self.app = gz.App(title = "TTRPG Companion", width = width, height = height, layout = "grid", bg = self.background_check(), visible = True)
    self.adjust_size()
    #self.app.when_resized = self.adjust_size()

  def file_check(self):
    # Check for Crucial files (reminders, default datapack,settings)
    if not Path("./datapacks/data/reminders.json").is_file():
      print("missing reminders file")
      quit()
    if not Path("./datapacks/data/default.json").is_file():
      print("missing default datapack file")
      quit()
    if not Path("./settings.json").is_file():
      print("missing settings file")
      quit()
    if Path("./datapacks/data/datapack.json").is_file():
      with open("./datapacks/data/datapack.json", "r") as f:
        self.datapack = json.load(f)
        self.datapack_exist = True
    else:
      self.datapack_exist = False
    with open("./datapacks/data/reminders.json", "r") as f:
      self.reminders = json.load(f)
    with open("./datapacks/data/default.json", "r") as f:
      self.default = json.load(f)
    with open("./settings.json", "r") as f:
      self.settings = json.load(f)


  def startup(self):
    self.running = True
    self.file_check()

    # Set up initial weather/season/region/terrain
    self.weather_current = "clear.png"
    self.seasons_current = "spring.png"
    self.regions_current = "plains.png"
    self.terrain_current = "flat.png"

    


  def background_check(self): 
    if self.datapack_exist and (re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.datapack["background"]["dark"]) and re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.datapack["background"]["light"])): 
      if self.settings["dark-mode"]:
        bg = self.datapack["background"]["dark"]
      else:
        bg = self.datapack["background"]["light"]
    else:
      if self.settings["dark-mode"]:
        bg = self.default["background"]["dark"]
      else:
        bg = self.default["background"]["light"]
    return bg


  def adjust_size(self):
    self.width = self.app.width
    self.height = self.app.height
    self.info_width = (self.width/3)
    self.opts_width =  self.info_width/3
    self.init_width = self.width - (self.info_width + self.opts_width)
    self.update()


  """def isRunning(self):
    pass
      
      

"""

  def update(self):
    self.buildApp()


  def buildApp(self):
    info_box = gz.Box(self.app, grid = [0, 0], width = self.info_width, height = self.height, layout = "grid")
    init_box = gz.Box(self.app, grid = [1, 0], width = self.init_width, height = self.height, layout = "grid", border = 1, )
    opts_box = gz.Box(self.app, grid = [2, 0], width = self.opts_width, height = self.height, layout = "grid")

    # Information
    time_box        = gz.Box(info_box, grid = [0, 0], layout = "grid", width = self.info_width, height = self.info_width/4)
    icon_box_1      = gz.Box(info_box, grid = [0, 1], layout = "grid", width = self.info_width, height = self.info_width/2)
    progression_box = gz.Box(info_box, grid = [0, 3], layout = "grid", width = self.info_width, height = self.info_width/4)
    empty_box       = gz.Box(info_box, grid = [0, 2], layout = "grid", width = self.info_width, height = (self.height-self.info_width-8))

    # Information Icons
    weather_icon = gz.Picture(icon_box_1, grid = [0, 0], image = f"./datapacks/icons/weather/{self.weather_current}", width = int(self.info_width/2), height = int(self.info_width/4))
    season_icon  = gz.Picture(icon_box_1, grid = [1, 0], image = f"./datapacks/icons/seasons/{self.seasons_current}", width = int(self.info_width/2), height = int(self.info_width/4))
    region_icon  = gz.Picture(icon_box_1, grid = [0, 1], image = f"./datapacks/icons/regions/{self.regions_current}", width = int(self.info_width/2), height = int(self.info_width/4))
    terrain_icon = gz.Picture(icon_box_1, grid = [1, 1], image = f"./datapacks/icons/terrain/{self.terrain_current}", width = int(self.info_width/2), height = int(self.info_width/4))
    
    # Initiative

    # Options
    load_button = gz.PushButton(opts_box, grid=[0, 2], width = self.opts_width/2, height = self.height/6, command = self.load_save_file, text = "Load Save")
    save_button = gz.PushButton(opts_box, grid=[1, 2], width = self.opts_width/2, height = self.height/6, command = self.load_save_file, text = "Save Save")


  def load_save_file(self):
    # https://lawsie.github.io/guizero/alerts/#:~:text=**%20Example%3A%20Get%20a%20file%20name*
    print((self.app.select_file()).value)
    
    



  def showApp(self):
    self.app.display()

