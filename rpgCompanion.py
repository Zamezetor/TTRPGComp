# Imports
import random
import guizero as gz
# Variables
# Classes
# Functions
# Code
app = gz.App(title="TTRPG Companion  ",width=1920, height=1080,layout = "grid",bg="#6C6C6C",visible=True)

info_box = gz.Box(app, grid = [0,0], width = 800, height = 1080, border = 1)
initiative_box = gz.Box(app, grid = [800,0], width = 900, height = 1080, border = 1)
options_box = gz.Box(app, grid = [1760,0], width = 220, height = 1080, border = 1)




app.display()