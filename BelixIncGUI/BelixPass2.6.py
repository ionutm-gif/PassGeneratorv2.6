import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generator_randomizat(lungime):
    caractere = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}"
    return ''.join(secrets.choice(caractere) for _ in range(lungime))

def generator_logic(nume, data_nastere):
    try:
        zi, luna, anul = data_nastere.split(".")
        parola = f"{nume.capitalize()}{anul}{secrets.choice(['!', '#', '@', '_'])}"
        return parola
    except:
        return "Format dată invalid (folosește DD.MM.YYYY)"

def generator_numerical(lungime):
    return ''.join(secrets.choice(string.digits) for _ in range(lungime))

def genereaza_random():
    try:
        lungime = int(entry_random.get())
        parola = generator_randomizat(lungime)
        messagebox.showinfo("Parola generată", parola)
    except:
        messagebox.showerror("Eroare", "Introdu un număr valid!")

def genereaza_logic():
    nume = entry_nume.get()
    data = entry_data.get()
    parola = generator_logic(nume, data)
    messagebox.showinfo("Parola generată", parola)

def genereaza_numerical():
    try:
        lungime = int(entry_numeric.get())
        parola = generator_numerical(lungime)
        messagebox.showinfo("Parola generată", parola)
    except:
        messagebox.showerror("Eroare", "Introdu un număr valid!")

# Fereastra principală
root = tk.Tk()
root.title("Belix Inc. Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# Titlu
tk.Label(root, text="Belix Inc. Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# --- Modul Randomizat ---
tk.Label(root, text="Modul 1: Randomizat").pack()
entry_random = tk.Entry(root)
entry_random.pack()
tk.Button(root, text="Generează Random", command=genereaza_random).pack(pady=5)

# --- Modul Logic ---
tk.Label(root, text="Modul 2: Logic").pack()
entry_nume = tk.Entry(root)
entry_nume.insert(0, "Nume")
entry_nume.pack()

entry_data = tk.Entry(root)
entry_data.insert(0, "DD.MM.YYYY")
entry_data.pack()

tk.Button(root, text="Generează Logic", command=genereaza_logic).pack(pady=5)

# --- Modul Numeric ---
tk.Label(root, text="Modul 3: Numerical").pack()
entry_numeric = tk.Entry(root)
entry_numeric.pack()
tk.Button(root, text="Generează Numeric", command=genereaza_numerical).pack(pady=5)

root.mainloop()
