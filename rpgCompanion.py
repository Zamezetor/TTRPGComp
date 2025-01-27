# Imports
import random
import json
import guizero as gz
# Variables
# Classes
# Functions
# Code
reminders_file = open("./datapacks/data/reminders.json", "r") 
datapack_file = open("./datapacks/data/default.json", "r")
settings_file = open("./settings.json", "r")



app = gz.App(title = "TTRPG Companion", width = 1920, height = 1080, layout = "grid", bg = "#6C6C6C", visible = True)

info_box = gz.Box(app, grid = [0,0], width = 800, height = 1080, border = 1, layout = "grid")
init_box = gz.Box(app, grid = [800,0], width = 900, height = 1080, border = 1, layout = "grid")
opts_box = gz.Box(app, grid = [1760,0], width = 220, height = 1080, border = 1, layout = "grid")



time_box = gz.Box(info_box, grid = [0,0], align = "top", width = 800, height = 150, border = 1, layout = "grid")
icon_box_1 = gz.Box(info_box, grid = [0,100], align = "top", width = 800, height = 400, border = 1, layout = "grid")

weather_current = "clear.png"
season_current = "spring.png"
region_current = "plains.png"
terrain_current = "flat.png"

weather_icon = gz.Picture(icon_box_1, grid = [0, 0], image = f"./datapacks/icons/weather/{weather_current}", width = 400, height = 200)
season_icon  = gz.Picture(icon_box_1, grid = [400, 0], image = f"./datapacks/icons/seasons/{season_current}", width = 400, height = 200)
region_icon  = gz.Picture(icon_box_1, grid = [0, 200], image = f"./datapacks/icons/regions/{region_current}", width = 400, height = 200)
terrain_icon = gz.Picture(icon_box_1, grid = [400, 200], image = f"./datapacks/icons/terrain/{terrain_current}", width = 400, height = 200)







app.display()