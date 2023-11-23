import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from AnalisisLexico import lexico

def cargar_archivo():
    filename = askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        analizar_texto(content)

def analizar_texto(texto):
    # Limpia la tabla antes de cargar nuevos datos
    tabla.delete(*tabla.get_children())

    for kind, value, linea in lexico(texto):
        tabla.insert('', 'end', values=(kind, value, linea))

def guardar_en_txt():
    # Abre el cuadro de diálogo para elegir la ubicación y el nombre del archivo
    filename = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if filename:
        # Abre el archivo en modo escritura
        with open(filename, 'w', encoding='utf-8') as file:
            # Obtiene todos los elementos de la tabla y escribe en el archivo
            for row_id in tabla.get_children():
                row_data = tabla.item(row_id)['values']
                file.write(f"{row_data[0]},{row_data[1]},{row_data[2]}\n")

app = tk.Tk()
app.title("Analizador Léxico")

frame = ttk.Frame(app)
frame.pack(padx=10, pady=10)

boton_cargar = ttk.Button(frame, text="Cargar Archivo", command=cargar_archivo)
boton_cargar.pack()

boton_guardar = ttk.Button(frame, text="Guardar en TXT", command=guardar_en_txt)
boton_guardar.pack()

columnas = ('Tipo', 'Valor', 'Línea')
tabla = ttk.Treeview(frame, columns=columnas, show='headings')
for col in columnas:
    tabla.heading(col, text=col)
tabla.pack()

app.mainloop()
