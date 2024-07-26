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
import os
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
    VOICE = "es-CL-CatalinaNeural"
    

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

            os.startfile(output_file)
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
def funcionesVoces(voz):
    global VOICE 
    VOICE = voz
    print("selecionando voz")
    pass 

# ... (resto del código)

def seleccionar_Belkys():
    global VOICE
    VOICE = "es-CU-BelkysNeural"
    # Aquí puedes agregar código adicional, por ejemplo, para mostrar un mensaje al usuario indicando que se ha seleccionado la voz de Belkys

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

def poema():
    campo_texto.delete("1.0", tk.END)  # Limpiar el campo
    campo_texto.insert(tk.INSERT, "Bosque verde y fresco,Susurra el viento entre las hojas, Llega la paz y calma.")

def tigres():
    campo_texto.delete("1.0", tk.END)  # Limpiar el campo
    campo_texto.insert(tk.INSERT, "Tres tristes tigres tragaban trigo en un trigal.")

def relatividad():
    campo_texto.delete("1.0", tk.END)
    campo_texto.insert(tk.INSERT, "La teoría de la relatividad general, propuesta por Albert Einstein en 1915, revolucionó nuestra comprensión del espacio, el tiempo y la gravedad.")

def puntuacion():
    campo_texto.delete("1.0", tk.END)  # Limpiar el campo
    campo_texto.insert(tk.INSERT, "¡Hola! ¿Cómo estás? Me gusta mucho comer pizza, ¿y a ti?")

cuento = """El Laberinto de Cristal
En una ciudad donde los edificios se alzaban como gigantes de acero y vidrio, existía un lugar apartado, un jardín secreto donde la naturaleza desafiaba la urbanidad. Era un laberinto de cristal, una estructura compleja y luminosa que se erigía en el corazón del parque. Cada panel era una obra de arte, un mosaico de colores que cambiaban con la luz del sol, reflejando el cielo como un caleidoscopio gigante.
Dentro del laberinto, un camino sinuoso invitaba a perderse. Las paredes de cristal, pulidas hasta la perfección, creaban un efecto hipnótico. Las plantas, exuberantes y variadas, trepaban por las estructuras, transformando el lugar en una selva de cristal. El aire era húmedo y perfumado, una mezcla de tierra mojada y flores exóticas.
Un joven llamado Alex, curioso por naturaleza, decidió adentrarse en el laberinto. A cada paso, nuevos colores y formas se revelaban ante sus ojos. Las sombras danzaban en el suelo, creando patrones cambiantes que lo hipnotizaban. El sonido del agua, que brotaba de una pequeña fuente oculta entre las plantas, lo acompañaba en su recorrido.
Al llegar al centro del laberinto, Alex encontró una pequeña habitación de cristal. En el centro, flotaba una esfera luminosa que proyectaba imágenes cambiantes en las paredes. Eran paisajes de otros mundos, galaxias lejanas y criaturas fantásticas. El joven se quedó fascinado, contemplando las maravillas que se desplegaban ante él.
De repente, la esfera comenzó a emitir una suave melodía. Era una música celestial, que lo envolvió en una sensación de paz y armonía. Los colores de las imágenes se intensificaron, creando una experiencia sensorial única. Alex se sintió como si estuviera flotando en el espacio, explorando los confines del universo.
Cuando la música cesó, Alex abrió los ojos y se encontró de nuevo en la habitación de cristal. La esfera había dejado de brillar y las imágenes habían desaparecido. Sin embargo, la experiencia que había vivido lo había marcado para siempre. Salió del laberinto con un corazón lleno de asombro y una nueva perspectiva del mundo."""

def historia():
    campo_texto.delete("1.0",tk.END)
    campo_texto.insert(tk.INSERT, cuento)

# Creación de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Texto a voz")
ventana.geometry("500x600")

menubar = tk.Menu(ventana)
archivo_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=archivo_menu)

voces_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Voces", menu=voces_menu)



ejemplo_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ejemplos", menu=ejemplo_menu)


# Opciones del menú Archivo
archivo_menu.add_command(label="Nuevo", command=funcion_nuevo)
archivo_menu.add_command(label="Abrir", command=funcion_abrir)
archivo_menu.add_separator()  # Agregar una línea separadora
archivo_menu.add_command(label="Salir", command=salir)

#lista de voces
voces_menu.add_command(label="Belkys (FEM ES)", command=lambda: funcionesVoces("es-CU-BelkysNeural"))
voces_menu.add_command(label="Tania(FEM ES)", command=funcionesVoces)
voces_menu.add_command(label="Nanami(FEM JA)", command=funcionesVoces)
voces_menu.add_separator()
voces_menu.add_command(label="Jorge(MA ES)", command=funcionesVoces)

ejemplo_menu.add_command(label="haiku", command=poema)
ejemplo_menu.add_command(label="tigres", command=tigres)
ejemplo_menu.add_command(label="relactividad", command=relatividad)
ejemplo_menu.add_command(label="puntuacion", command=puntuacion)
ejemplo_menu.add_command(label="historia", command=historia)


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
