import tkinter as tk
from tkinter import messagebox
import serial
import threading
import re

def parse_arduino_msg(data_txt):
    pattern = r"masse: (.+),tension position: (.+)"
    match = re.search(pattern, data_txt)

    # If match is found, extract values and return them
    if match:
        masse = match.group(1)
        tension = match.group(2)
        return {"masse":masse, "tension": tension}
    else:
        return {"masse":0, "tension": 0}
    

class WeightApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Application de Poids")

        self.grid_columnconfigure(0, weight=1)

        self.masse = 0
        self.tension_pos = 0
        self.ardu_serial = None # serial connection. if none, arduino is not connected.
        
        self.connect_arduino()
        
        data_thread = threading.Thread(target=self.read_arduino_data_loop, args=())
        data_thread.start()

        # create a StringVar class
        self.weight_str_var = tk.StringVar(self)

        # Affichage du poids actuel
        self.weight_label = tk.Label(self, textvariable=self.weight_str_var, borderwidth=1, relief="solid")
        self.weight_label.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Bouton de Tarage
        self.tare_button = tk.Button(self, text="Tarage", command=self.tare, borderwidth=1, relief="solid")
        self.tare_button.grid(row=1, column=0, sticky="ew")

        # Bouton d'Étalonnage
        self.calibrate_button = tk.Button(self, text="Étalonnage", command=self.calibrate, borderwidth=1, relief="solid")
        self.calibrate_button.grid(row=1, column=1, sticky="ew")

        # Section de comptage des pièces
        self.coin_label = tk.Label(self, text="Comptage des Pièces", borderwidth=1, relief="solid")
        self.coin_label.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.coin_type_label = tk.Label(self, text="Sélectionnez le type de pièce:", borderwidth=1, relief="solid")
        self.coin_type_label.grid(row=3, column=0, sticky="ew")

        self.coin_type_var = tk.StringVar(self)
        self.coin_type_var.set("Sélectionner une pièce")
        self.coin_dropdown = tk.OptionMenu(self, self.coin_type_var, "Centime", "Nickle", "Dime", "Quart")
        self.coin_dropdown.grid(row=3, column=1, sticky="ew")

        self.coin_count_label = tk.Label(self, text="Nombre de pièces: 0", borderwidth=1, relief="solid")
        self.coin_count_label.grid(row=4, column=0, columnspan=2, sticky="ew")

    def connect_arduino(self):
        port = '/dev/cu.usbmodem1301' # change this later
        try:
            self.ardu_serial = serial.Serial(port, 115200)
            return True
        except serial.SerialException:
            messagebox.showerror("Error", "No available Arduino found. "\
                                    "Remember to disconnect Arduino IDE")
            return False

    def read_arduino_data_loop(self):
        while(True):
            self.read_arduino_data()
            self.update_labels()

    def read_arduino_data(self):
        # readline() blocks until a whole line is returned by the arduino
        data_txt = self.ardu_serial.readline().decode().strip()
        data = parse_arduino_msg(data_txt)
        self.masse = data["masse"]
        self.tension_pos = data["tension"]

    def update_labels(self):
        self.weight_str_var.set(f"Poids actuel: {self.masse}g")


    def tare(self):
        # Effectuer l'opération de tarage
        # commande "1": tarage
        self.ardu_serial.write(bytes("1", 'utf-8'))
        self.show_message("Tarage", "Tarage en cours...")

    def calibrate(self):
        # Effectuer l'étalonnage
        self.show_message("Étalonnage", "Étalonnage en cours...")

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
    

if __name__ == "__main__":
    app = WeightApp()
    app.mainloop()
