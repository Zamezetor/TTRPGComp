# Imports
import random, math
import tkinter as tk
from app import mainApp


# Variables
# Classes
# Functions
def getScreen(): 
  # Spawn Tkinter window, take screen width and height, kill Tkinter window 
  try:
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height
  except Exception as e:
    print(f"Error getting screen size: {e}")
    return 1920, 1080  # Default to 1080p if there is an issue


# Code
width, height = getScreen()
application = mainApp(width, height)
#application.isRunning()
application.showApp()

