import tkinter as tk
from tkinter import messagebox

class WeightApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Application de Poids")

        self.grid_columnconfigure(0, weight=1)

        # Affichage du poids actuel
        self.weight_label = tk.Label(self, text="Poids actuel: 0 g", borderwidth=1, relief="solid")
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

    def tare(self):
        # Effectuer l'opération de tarage
        self.show_message("Tarage", "Tarage en cours...")

    def calibrate(self):
        # Effectuer l'étalonnage
        self.show_message("Étalonnage", "Étalonnage en cours...")

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

if __name__ == "__main__":
    app = WeightApp()
    app.mainloop()
