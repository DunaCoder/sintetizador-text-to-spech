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

async def amain(campo_texto: tk.Text, output_file: str) -> None:
    """Función principal"""
    TEXT = campo_texto.get("1.0", tk.END)  # Obtiene el texto ingresado por el usuario
    VOICE = "es-CU-BelkysNeural"

    try:
        communicate = edge_tts.Communicate(TEXT, VOICE)
        await communicate.save(output_file)
        playsound.playsound(output_file)  # Reproduce el texto generado

        # Eliminar el archivo de audio después de la reproducción (opcional)
        # os.remove(output_file)
    except Exception as e:
        print(f"Error durante la conversión de texto a voz: {e}")

def reproducir(campo_texto: tk.Text):
    """Función para reproducir texto"""
    output_file = f"audio_{uuid.uuid4()}.mp3"  # Generar nombre de archivo único
    asyncio.run(amain(campo_texto, output_file))


# Creación de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Texto a voz")
ventana.geometry("500x500")

etiqueta_texto = tk.Label(ventana)
etiqueta_texto.pack()

campo_texto = tk.Text(ventana, font=("Arial", 16), width=50, height=10)
campo_texto.pack(padx=40, pady=40)

boton_reproducir = tk.Button(ventana, text="Reproducir texto", command=lambda: reproducir(campo_texto))
boton_reproducir.pack()

ventana.mainloop()
