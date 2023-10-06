import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import sqlite3

def add_researcher(name, contribution):
    conn = sqlite3.connect('researchers.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO researchers (name, contribution) VALUES (?, ?)", (name, contribution))
    conn.commit()
    conn.close()

def generate_statement():
    conn = sqlite3.connect('researchers.db')
    c = conn.cursor()
    researchers = c.execute("SELECT * FROM researchers").fetchall()
    conn.close()
    
    statement = ""
    for researcher in researchers:
        statement += researcher[0] + " " + researcher[1] + "\n"
    
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        with open(filepath, 'w') as file:
            file.write(statement)

def on_contribution_selected(event):
    if dropdown_var.get() == "Other":
        new_contribution = simpledialog.askstring("New Contribution", "Enter the new contribution:")
        if new_contribution:
            contributions.append(new_contribution)
            dropdown['menu'].delete(0, 'end')
            for contribution in contributions:
                dropdown['menu'].add_command(label=contribution, command=tk._setit(dropdown_var, contribution))
            dropdown_var.set(new_contribution)

app = tk.Tk()
app.title('Researcher Contributions')

name_label = tk.Label(app, text="Researcher's Name")
name_label.pack(pady=10)
name_entry = tk.Entry(app)
name_entry.pack(pady=10)

contributions = ["Contribution 1", "Contribution 2", "Contribution 3", "Other"]
dropdown_var = tk.StringVar(app)
dropdown_var.set(contributions[0])

dropdown = tk.OptionMenu(app, dropdown_var, *contributions, command=on_contribution_selected)
dropdown.pack(pady=10)

def add_clicked():
    name = name_entry.get()
    contribution = dropdown_var.get()
    if name and contribution:
        add_researcher(name, contribution)
        name_entry.delete(0, 'end')

add_button = tk.Button(app, text="+", command=add_clicked)
add_button.pack(pady=10)

generate_button = tk.Button(app, text="Generate Statement", command=generate_statement)
generate_button.pack(pady=20)

app.mainloop()
