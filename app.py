import random, json, math, PIL, re
import guizero as gz
from pathlib import Path

class mainApp():
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.running = True

    self.reminders_file = ""
    self.settings_file = ""
    self.datapack_file  = ""
    self.default_datapack_file = ""
    


    self.file_check()
    if self.datapack_exist:
      self.datapack = json.load(self.datapack_file)
    self.default = json.load(self.default_datapack_file)
    self.settings = json.load(self.settings_file)


    self.weather_current = "clear.png"
    self.seasons_current = "spring.png"
    self.regions_current = "plains.png"
    self.terrain_current = "flat.png"
     
    # Opens Settings

    

    self.app = gz.App(title = "TTRPG Companion", width = width, height = height, layout = "grid", bg = self.background_check(), visible = True)
  def file_check(self):
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
        self.datapack_file = f
        print(f)
        print(dir(f))
        print(type(f))
    else:
      self.datapack_exist = False
    with open("./datapacks/data/reminders.json", "r") as f:
      self.reminders_file = f
    with open("./datapacks/data/default.json", "r") as f:
      self.default_datapack_file = f
    with open("./settings.json", "+") as f:
      self.settings_file = f
    


  def background_check(self): 
    if  (self.datapack_exist or not (re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.datapack["background"]["dark"]) and re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.datapack["background"]["light"]))): 
      if self.settings["dark-mode"]:
        bg = self.default["background"]["dark"]
      else:
        bg = self.default["background"]["light"]
    else:
      if self.settings["dark-mode"]:
        bg = self.datapack["background"]["dark"]
      else:
        bg = self.datapack["background"]["light"]
    return bg


  def adjust_size(self):
    self.width = self.app.width
    self.height = self.app.height
    self.info_width = (self.width/3)
    self.opts_width =  self.info_width/3
    self.init_width = self.width - (self.info_width + self.opts_width)
    self.update()


  def isRunning(self):
    while self.running:
      self.app.when_resized = self.adjust_size()
      

      self.weather_current = "clear.png"
      self.seasons_current = "spring.png"
      self.regions_current = "plains.png"
      self.terrain_current = "flat.png"


  def update(self):
    self.buildApp()


  def buildApp(self):
    info_box = gz.Box(self.app, grid = [0, 0], width = self.info_width, height = self.height, layout = "grid")
    init_box = gz.Box(self.app, grid = [1, 0], width = self.init_width, height = self.height, layout = "grid", border = 1, )
    opts_box = gz.Box(self.app, grid = [2, 0], width = self.opts_width, height = self.height, layout = "grid")

    time_box        = gz.Box(info_box, grid = [0, 0], width = self.info_width, height = self.info_width/4, layout = "grid")
    icon_box_1      = gz.Box(info_box, grid = [0, 1], width = self.info_width, height = self.info_width/2, layout = "grid")
    empty_box       = gz.Box(info_box, grid = [0, 2], width = self.info_width, height = (self.height-self.info_width-8), layout = "grid")
    progression_box = gz.Box(info_box, grid = [0, 3], width = self.info_width, height = self.info_width/4 , layout = "grid")

    weather_icon = gz.Picture(icon_box_1, grid = [0, 0], image = f"./datapacks/icons/weather/{self.weather_current}", width = int(self.info_width/2), height = int(self.info_width/4))
    season_icon  = gz.Picture(icon_box_1, grid = [1, 0], image = f"./datapacks/icons/seasons/{self.seasons_current}", width = int(self.info_width/2), height = int(self.info_width/4))
    region_icon  = gz.Picture(icon_box_1, grid = [0, 1], image = f"./datapacks/icons/regions/{self.regions_current}", width = int(self.info_width/2), height = int(self.info_width/4))
    terrain_icon = gz.Picture(icon_box_1, grid = [1, 1], image = f"./datapacks/icons/terrain/{self.terrain_current}", width = int(self.info_width/2), height = int(self.info_width/4))
    


  def load_save_file():
    """
    gz.PushButton(self.app, command=get_file, text="Get file")
    https://lawsie.github.io/guizero/alerts/#:~:text=**%20Example%3A%20Get%20a%20file%20name**
    file_name.value = self.app.select_file()
    file_name = Text(app)
  """


  def showApp(self):
    self.app.display()

