from moviepy.editor import *

def video_to_audio(input_video, output_audio):
    # Charger la vidéo
    video = VideoFileClip(input_video)
    
    # Extraire l'audio
    audio = video.audio
    
    # Exporter l'audio en mp3
    audio.write_audiofile(output_audio)
    print(f"Conversion terminée : {output_audio}")

# Exemple d'utilisation
input_video = 'video.mp4'
output_audio = 'video.mp3'

video_to_audio(input_video, output_audio)
