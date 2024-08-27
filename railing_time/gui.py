import tkinter as tk
from tkinter import ttk
import hsr as hsr
import json

def run_hsr_script(path, mode, material):
    hsr.star_rail_dailies(path, mode, material)

def update_path_message(): 

    global update_message_var
    hsr_path = config["path"]
    update_message_var.set(f"path updated to {hsr_path}") 

def save_config(config, config_file):
    
    with open(config_file, "w") as file:
        json.dump(config, file)

def load_config(config_file):
    
    with open(config_file, "r") as file:
        return json.load(file)
    return {}

def update_config(event, key, config, config_file):
    
    value = event.widget.get()
    config[key] = value
    save_config(config, config_file)
    
def update_config_btn(key, config, config_file, widget):

    def update():
        value = widget.get()
        config[key] = value
        save_config(config, config_file)
        
    return update

def update_config_btn_message(key, config, config_file, widget):

    def update():
        value = widget.get()
        config[key] = value
        save_config(config, config_file)
        update_message_var.set(f"{key} updated to: {value}")
    return update
    

def change_mode(event=None):
    global modes, mode, combo, materials
    mode = combo.get()
    if(mode == 'crimson'):
        new_materials = ['arrow_of_the_starchaser', 'countertemporal_shot', 'divine_amber', 'exquisite_colored_draft', 'flower_of_eternity', 
                         'heaven_incinerator', 'key_of_wisdom', 'moon_rage_fang', 'obisidian_of_obsession', 'safeguard_of_amber', 'myriad_fruit', 'worldbreaker_blade']
    elif(mode == 'shadow'):
        new_materials = ['Ascendant Debris','Broken Teeth of Iron Wolf','Dream Flamer','Dream Fridge','Endotherm Chitin','Gelic Chitin','Golden Crown of the Past Shadow',
                         'Horn of Snow','IPC Work Permit','Lightning Crown of the Past Shadow','Nail of the Ape','Netherworld Token','Raging Heart','Searing Steel Blade',
                         "Shape Shifter's Lightning Staff",'Storm Eye','Suppressing Edict','Void Cast Iron']
    elif(mode == 'golden'):
        new_materials = ['Character EXP', 'Lightcone EXP']
    elif(mode == 'corrosion'):
        new_materials=['Cavalry + Valorous','Champion + Thief','Disciple + Messenger','Firesmith + Wastelander','Grand Duke + Prisoner','Guard + Genius',
                       'Hunter + Eagle','Knight + Band','Passerby + Musketeer','Pioneer + Watchmaker']    
    combo2.set(new_materials[0])
    combo2['values'] = new_materials

def change_material(event=None):
    global mode, materials, material, combo2
    '''if(mode == 'crimson'):
        material = 'crimson\\' + combo2.get()
    elif(mode == 'shadow'):
        material = 'shadow\\' + combo2.get()
    elif(mode == 'golden'):
        material = 'golden\\' + combo2.get()
    elif(mode == 'corrosion'):
        material = 'corrosion\\' + combo2.get() '''
    material = combo2.get()
    #material = combo2.get()

def main():

    global config_file, config, hsr_entry, root, message_exists, update_message_var, modes, materials, mode, material, combo, combo2

    config_file = "railing_time//config.json"
    config = load_config(config_file)
    modes = ['crimson', 'shadow', 'golden', 'corrosion']
    materials = ['select a mode first']
    mode = config["mode"]
    material = config["material"]
    message_exists = False
    root=tk.Tk()
    root.title("my scripts")
    root.geometry("800x600")
    update_message_var = tk.StringVar(value="")

    canvas = tk.Canvas(root, width=100, height=100)
    canvas.pack()

    #smile
    canvas.create_oval(25,25,75,75)
    canvas.create_line(40,40,40,45)
    canvas.create_line(60,40,60,45)
    canvas.create_line(30,60,70,60)
    canvas.create_line(30,60,30,55)
    canvas.create_line(70,60,70,55)

    tk.Label(root, text="star rail path:").pack()
    hsr_entry = tk.Entry(root)
    hsr_entry.insert(0, config["path"])
    hsr_entry.pack()
    btn_update = tk.Button(root, text="update path variable", command=update_config_btn_message("path", config, config_file, hsr_entry))
    btn_update.pack()
    
    update_message = tk.Message(root, textvariable=update_message_var)
    update_message.pack()

    btn1 = tk.Button(root, text="play star rail", command=lambda: run_hsr_script(config["path"], mode, f"{mode}//{material}")).pack()

    btn2 = tk.Button(root, text="play star rail", command=lambda: run_hsr_script(config["path"], mode, f"{mode}//{material}")).pack()

    btn3 = tk.Button(root, text="play star rail", command=lambda: run_hsr_script(config["path"], mode, f"{mode}//{material}")).pack()
    
    combo= ttk.Combobox(root, values=modes)
    combo.set(config["mode"])
    combo.pack()
    combo.bind("<<ComboboxSelected>>", lambda event: (update_config(event, "mode", config, config_file), change_mode()))
    
    combo2= ttk.Combobox(root, values=materials)
    combo2.set(config["material"])
    combo2.pack()
    combo2.bind("<<ComboboxSelected>>", lambda event: (update_config(event, "material", config, config_file), change_material()))


    root.mainloop()

if __name__ == "__main__":
    main()

