import tkinter as tk
from tkinter import ttk
import hsr as hsr

def run_hsr_script(path, mode, material):
    hsr.star_rail_dailies(path, mode, material)

def update_paths(): 
    global update_message_var
    hsr_path = hsr_entry.get()
    save_path(hsr_path=hsr_path)
    update_message_var.set(f"path updated to {hsr_path}") 

def save_path(hsr_path):
    with open("railing_time//path_config.txt", "w") as file:
        file.write(hsr_path)

def load_path():
    with open("railing_time//path_config.txt", "r") as file:
        return file.read().strip()

def change_mode(event=None):
    global modes, mode, combo, materials
    mode = combo.get()
    if(mode == 'crimson'):
        new_materials = ['arrow_of_the_starchaser', 'countertemporal_shot', 'divine_amber', 'exquisite_colored_draft', 'flower_of_eternity', 'heaven_incinerator', 'key_of_wisdom', 'moon_rage_fang', 'obisidian_of_obsession', 'safeguard_of_amber', 'myriad_fruit', 'worldbreaker_blade']
    elif(mode == 'shadow'):
        new_materials = ['dream_flamer', 'raging_heart', 'IPC_work_permit']
    elif(mode == 'golden'):
        new_materials = ['none']
    elif(mode == 'corrosion'):
        new_materials=['hackerspace']    
    combo2['values'] = new_materials

def change_material(event=None):
    global mode, materials, material, combo2
    if(mode == 'crimson'):
        material = 'crimson\\' + combo2.get()
    #material = combo2.get()

def main():

    global hsr_path, hsr_entry, root, message_exists, update_message_var, modes, materials, mode, material, combo, combo2

    modes = ['crimson', 'shadow', 'golden', 'corrosion']
    materials = ['select a mode first']
    mode = 'crimson' #default selections
    material = 'dream_flamer'

    message_exists = False
    root=tk.Tk()
    root.title("my scripts")
    root.geometry("800x600")

    canvas = tk.Canvas(root, width=100, height=100)
    canvas.pack()

    #smiley
    canvas.create_oval(25,25,75,75)
    canvas.create_line(40,40,40,45)
    canvas.create_line(60,40,60,45)
    canvas.create_line(30,60,70,60)
    canvas.create_line(30,60,30,55)
    canvas.create_line(70,60,70,55)

    tk.Label(root, text="star rail path:").pack()
    hsr_entry = tk.Entry(root)
    hsr_entry.insert(0, load_path())
    hsr_entry.pack()
    btn_update = tk.Button(root, text="update path variable", command=update_paths).pack()
    update_message_var = tk.StringVar()
    update_message = tk.Message(root, textvariable=update_message_var).pack()

    btn1 = tk.Button(root, text="play star rail", command=lambda: run_hsr_script(load_path(), mode, material)).pack()

    btn2 = tk.Button(root, text="play star rail", command=lambda: run_hsr_script(load_path(), mode, material)).pack()

    btn3 = tk.Button(root, text="play star rail", command=lambda: run_hsr_script(load_path(), mode, material)).pack()
    
    combo= ttk.Combobox(root, values=modes)
    combo.pack()
    combo.bind("<<ComboboxSelected>>", change_mode)
    
    combo2= ttk.Combobox(root, values=materials)
    combo2.pack()
    combo2.bind("<<ComboboxSelected>>", change_material)


    root.mainloop()

if __name__ == "__main__":
    main()

