import pytube
import msvcrt
video_url = input("Insertar la URL del video: ")
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download(r'Descargas')
msvcrt.getch()