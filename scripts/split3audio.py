from pydub import AudioSegment
import os

def split_mp3_into_three(input_file, output_folder):
    # Créer le répertoire de sortie s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Charger le fichier audio
    audio = AudioSegment.from_mp3(input_file)
    
    # Calculer la durée de chaque segment
    segment_length = len(audio) // 3
    
    # Générer les segments
    segments = [
        audio[:segment_length],
        audio[segment_length:2*segment_length],
        audio[2*segment_length:]
    ]
    
    # Exporter les segments
    base_filename = os.path.splitext(os.path.basename(input_file))[0]
    for i, segment in enumerate(segments, start=1):
        output_file = os.path.join(output_folder, f"{base_filename}_part{i}.mp3")
        segment.export(output_file, format="mp3")
        print(f"Segment {i} exporté : {output_file}")

# Exemple d'utilisation
input_file = 'audio.mp3'
output_folder = 'split3'
split_mp3_into_three(input_file, output_folder)
