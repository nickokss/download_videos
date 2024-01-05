import flet as ft
from pytube import YouTube
import os
import threading

def main(page):
    texto = ft.Text("Descarga tus videos de YouTube aquí")
    url = ft.TextField(label="URL del Video", autofocus=True)
    path = ft.TextField(label="Ruta de Guardado", value=os.getcwd())
    submit = ft.ElevatedButton("Descarga")
    mensaje_descarga = ft.Text("")

    def descargar_video():
        try:
            yt = YouTube(url.value)
            video = yt.streams.get_highest_resolution()
            video.download(output_path=path.value)
            mensaje_descarga.value = "Descarga completada con éxito."
        except Exception as ex:
            mensaje_descarga.value = f"Error: {str(ex)}"
        page.update()

    def btn_click(e):
        mensaje_descarga.value = "Descargando..."
        page.update()
        threading.Thread(target=descargar_video).start()

    submit.on_click = btn_click

    page.add(
        texto,
        url,
        path,
        submit,
        mensaje_descarga
    )

ft.app(target=main)
