import tkinter as tk

def mostrar_output():
    texto_output = "Este es un ejemplo de texto de salida."
    widget_output.config(state=tk.NORMAL)  # Habilitar la edición temporalmente
    widget_output.delete(1.0, tk.END)  # Limpiar el contenido actual
    widget_output.insert(tk.END, texto_output)  # Insertar el nuevo texto
    widget_output.config(state=tk.DISABLED)  # Deshabilitar la edición nuevamente

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Output Box")

# Crear un widget Text para el output
widget_output = tk.Text(ventana, wrap=tk.WORD, height=10, width=40, state=tk.DISABLED)
widget_output.pack()

# Crear un botón que muestra el texto en la Output Box
boton_mostrar_output = tk.Button(ventana, text="Mostrar Output", command=mostrar_output)
boton_mostrar_output.pack()

# Iniciar el bucle principal
ventana.mainloop()
