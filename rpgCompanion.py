# Imports
import random, json, math, PIL
import tkinter as tk
from app import mainApp


# Variables
# Classes
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
application.isRunning()
application.showApp()

  