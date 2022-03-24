# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
# Tem que usar algum módulo aí
from pydub import AudioSegment
from pydub.playback import play
song = AudioSegment.from_mp3('Za_Warudo_Whatsapp_VDownloader.mp3')
play(song)
