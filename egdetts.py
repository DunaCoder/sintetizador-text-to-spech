#  edge-tts --text "Hello, world!" --write-media hello.mp3 --write-subtitles hello.vtt

#!/usr/bin/env python3

"""

#lista de voces
# es-PY-TaniaNeural
# ja-JP-NanamiNeural
# es-VE-PaolaNeural
# es-MX-DaliaNeural
# es-EC-AndreaNeural
# es-AR-ElenaNeural
# es-CL-CatalinaNeural
# es-DO-RamonaNeural
# es-ES-ElviraNeural
# es-GQ-TeresaNeural
# es-CU-BelkysNeural

# en-ZA-LeahNeural

"hola soy un programa de computadora, es un placer conocerte"

Basic example of edge_tts usage.

"""
import asyncio
import playsound
import edge_tts
import tkinter as tk
import os
import uuid

"""Función principal aqui se genera el audio"""
async def amain(campo_texto: tk.Text, output_file: str) -> None:
    
    TEXT = campo_texto.get("1.0", tk.END)  # Obtiene el texto ingresado por el usuario
    VOICE = "ja-JP-NanamiNeural"

    try:
        communicate = edge_tts.Communicate(TEXT, VOICE)
        await communicate.save(output_file)
        playsound.playsound(output_file)  # Reproduce el texto generado

        abrir_carpeta(output_file)  # Abre la carpeta que contiene el archivo de audio

    except Exception as e:
        print(f"Error durante la conversión de texto a voz: {e}")


def crear_carpeta():
    """Crea la carpeta 'audios' si no existe"""
    carpeta = os.path.join(os.getcwd(), "audios")
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

def reproducir(campo_texto: tk.Text):
    """Función para reproducir texto"""
    crear_carpeta()  # Crea la carpeta "audios" si no existe
    output_file = os.path.join(os.getcwd(), "audios", f"audio_{uuid.uuid4()}.mp3")  # Genera nombre de archivo único
    asyncio.run(amain(campo_texto, output_file))


def abrir_carpeta(archivo):
    """Abre la carpeta que contiene el archivo especificado"""
    ruta_carpeta = os.path.dirname(archivo)
    os.startfile(ruta_carpeta)



def funcion_nuevo():
    # Implementar la acción para crear un nuevo archivo
    print("archivo en blanco")
    pass

def funcion_abrir():
    # Implementar la acción para abrir un archivo
    print("hola Mundo!!")
    pass

def selecionar():
    # Implementar la acción para guardar un archivo
    print("selecionando")
    pass
#funciones de voz
def funcionesVoces():
    print("selecionando voz")
    pass 

def right_click_handler(event):
    # Get the current position of the mouse cursor
    x = event.x_root
    y = event.y_root

    # Create the context menu
    context_menu = tk.Menu(ventana, tearoff=0)

    # Add "Copy" and "Paste" options to the menu
    context_menu.add_command(label="Copiar", command=copy_text)
    context_menu.add_command(label="Pegar", command=paste_text)
   




    # Display the context menu at the current mouse position
    context_menu.tk_popup(x, y)

    campo_texto.bind("<Button-3>", right_click_handler)

def copy_text():
    # Get the selected text
    selected_text = campo_texto.selection_get()

    # Copy the selected text to the clipboard
    ventana.clipboard_clear()
    ventana.clipboard_append(selected_text)

def paste_text():
    # Get the text from the clipboard
    clipboard_text = ventana.clipboard_get()

    # Insert the clipboard text into the text widget
    campo_texto.insert(tk.INSERT, clipboard_text)


# Creación de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Texto a voz")
ventana.geometry("500x500")

menubar = tk.Menu(ventana)
archivo_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=archivo_menu)

voces_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Voces", menu=voces_menu)



ayuda_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ayuda", menu=ayuda_menu)


# Opciones del menú Archivo
archivo_menu.add_command(label="Nuevo", command=funcion_nuevo)
archivo_menu.add_command(label="Abrir", command=funcion_abrir)
archivo_menu.add_command(label="Selecionar Archivo", command=selecionar)
archivo_menu.add_separator()  # Agregar una línea separadora
archivo_menu.add_command(label="Salir", command=ventana.quit)

#lista de voces
voces_menu.add_command(label="Belkys(FEM ES)",command=funcionesVoces)
voces_menu.add_command(label="Tania(FEM ES)", command=funcionesVoces)
voces_menu.add_command(label="Nanami(FEM JA)", command=funcionesVoces)
voces_menu.add_separator()
voces_menu.add_command(label="Jorge(MA ES)", command=funcionesVoces)

etiqueta_texto = tk.Label(ventana)
etiqueta_texto.pack()

campo_texto = tk.Text(ventana, font=("Arial", 16), width=50, height=10)
campo_texto.insert(0.0, "¡Hola! Soy un programa de computadora, encantado de conocerte.\n\nSoy tu asistente de texto a voz, y estoy aquí para ayudarte en tus tareas de lectura y comunicación, incluyendo la asistencia a personas con dislexia. ️\n\n¿Qué puedo hacer por ti?\n\n Convertir texto en voz: Puedo leer en voz alta cualquier texto que me escribas.\n Seleccionar voces: Elige entre diferentes voces masculinas y femeninas para personalizar tu experiencia.\n Reproducir texto: Presiona el botón \"Reproducir\" para escuchar el texto convertido en voz.\n\nEspero serte útil en tu día a día. ¡No dudes en preguntarme cualquier cosa!\n\nRecuerda:\n\n Puedes escribirme todo el texto que desees leer en voz alta.\n Puedes cambiar la voz que utilizas en cualquier momento.\n Presiona el botón \"Reproducir\" para escuchar el texto convertido en voz.\n\n¡Estoy aquí para ayudarte!\n\n¿Qué te gustaría hacer hoy?")
# Insertar texto en el índice 0.0
campo_texto.bind("<Button-3>", right_click_handler)
campo_texto.pack(padx=40, pady=40)

boton_reproducir = tk.Button(ventana, text="Reproducir texto", command=lambda: reproducir(campo_texto))
boton_reproducir.pack()

ventana.config(menu=menubar)
ventana.mainloop()
