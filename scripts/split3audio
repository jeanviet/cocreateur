from pydub import AudioSegment

def split_mp3_into_three(input_file):
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
    for i, segment in enumerate(segments, start=1):
        segment.export(f"{input_file[:-4]}_part{i}.mp3", format="mp3")
        print(f"Segment {i} exporté : {input_file[:-4]}_part{i}.mp3")

# Exemple d'utilisation
input_file = 'audio.mp3'
split_mp3_into_three(input_file)
