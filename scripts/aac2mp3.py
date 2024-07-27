# Script Python pour convertir un fichier aac en mp3
from pydub import AudioSegment

def convert_aac_to_mp3(input_file, output_file):
    # Charger le fichier audio .aac
    audio = AudioSegment.from_file(input_file, format='aac')
    
    # Exporter le fichier audio en .mp3
    audio.export(output_file, format='mp3')
    
    print(f"Conversion terminée : {output_file}")

# Exemple d'utilisation
input_file = 'audio.aac'
output_file = 'audio.mp3'

convert_aac_to_mp3(input_file, output_file)
