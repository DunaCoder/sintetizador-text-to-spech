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
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tqdm import tqdm 
import time

"""Función principal aqui se genera el audio"""
async def amain(campo_texto: tk.Text, output_file: str) -> None:
    TEXT = campo_texto.get("1.0", tk.END)  # Obtiene el texto ingresado por el usuario
    VOICE = "es-AR-ElenaNeural"

    try:
        with tqdm(desc="Convirtiendo texto a voz...", total=100) as pbar:  # Crea barra de progreso
            communicate = edge_tts.Communicate(TEXT, VOICE)
            # Simular actualización de progreso (reemplazar con lógica real)
            for i in range(101):
                time.sleep(0)
                pbar.update(i)  # Actualizar la barra de progreso
                porcentaje = int((i / 100) * 100)  # Calcular porcentaje
                etiqueta_porcentaje.config(text=f"{porcentaje}%")
                barra_progreso["value"] = porcentaje


            await communicate.save(output_file)
            pbar.update(100)  # Actualiza la barra al 100% al finalizar

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
    respuesta = msgbox.askquestion("Nuevo Archivo", "¿Deseas Abrit un nuevo Archivo?")
    if respuesta == "yes":
        campo_texto.delete("1.0", tk.END)


def funcion_abrir():
    # Implementar la acción para abrir un archivo
    print("hola Mundo!!")
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

def salir():
    respuesta = msgbox.askquestion("Salir","¿Deseas salir?")
    if respuesta == "yes":
         ventana.destroy()


def borrar_texto():
    respuesta = msgbox.askquestion("Borrar texto", "¿Deseas borrar todo el texto?")
    if respuesta == "yes":
        campo_texto.delete("1.0", tk.END)

# Creación de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Texto a voz")
ventana.geometry("500x600")

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
archivo_menu.add_separator()  # Agregar una línea separadora
archivo_menu.add_command(label="Salir", command=salir)

#lista de voces
voces_menu.add_command(label="Belkys(FEM ES)",command=funcionesVoces)
voces_menu.add_command(label="Tania(FEM ES)", command=funcionesVoces)
voces_menu.add_command(label="Nanami(FEM JA)", command=funcionesVoces)
voces_menu.add_separator()
voces_menu.add_command(label="Jorge(MA ES)", command=funcionesVoces)

etiqueta_texto = tk.Label(ventana)
etiqueta_texto.pack()



campo_texto = tk.Text(ventana, font=("Arial", 16), width=60, height=10)
campo_texto.insert(0.0, "¡Hola! Soy un programa de computadora, encantado de conocerte.\n\nSoy tu asistente de texto a voz, y estoy aquí para ayudarte en tus tareas de lectura y comunicación, incluyendo la asistencia a personas con dislexia.\n Presiona el botón \"Reproducir Texto\" para escuchar el texto convertido en voz.\nEspero serte útil en tu día a día, \n¿Qué te gustaría hacer hoy?.")
# Insertar texto en el índice 0.0
campo_texto.bind("<Button-3>", right_click_handler)
campo_texto.pack(padx=40, pady=40)


boton_reproducir = tk.Button(ventana, text="Reproducir texto", command=lambda: reproducir(campo_texto))
boton_reproducir.pack()

boton_borrar = tk.Button(ventana, text="Borrar", command=borrar_texto)
boton_borrar.pack(pady=10)

barra_progreso = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate")
barra_progreso.pack(pady=20)

etiqueta_porcentaje = tk.Label(ventana, text="0%")
etiqueta_porcentaje.pack(pady=10)

ventana.config(menu=menubar)
ventana.mainloop()
