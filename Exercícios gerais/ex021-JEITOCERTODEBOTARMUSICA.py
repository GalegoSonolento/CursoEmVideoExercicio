import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(r"C:\Users\henri\Music\Musicão do faustão\zawarudowhatsapp.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
print('funciona?')
