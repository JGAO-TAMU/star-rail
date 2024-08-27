import gui 
import hsr
import tkinter  as tk
from tkinter import ttk
import json


import gui

global config_file, config 
config_file = "railing_time//config.json"
config = gui.load_config(config_file)
print(config["Honkai: Star Rail"]["path"])



root = tk.Tk()
root.title("Config Updater")

combo= ttk.Combobox(root, values=["option 1", "option 2"])
combo.pack()
combo.bind("<<ComboboxSelected>>", lambda event: gui.update_config(event, "extra", config, config_file))


config_label = ttk.Label(root, text="Enter new configuration (JSON format):")
config_label.pack(pady=5)

config_entry = ttk.Entry(root, width=50)
config_entry.pack(pady=5)

status_label = ttk.Label(root, text="")
status_label.pack(pady=5)


root.mainloop()
