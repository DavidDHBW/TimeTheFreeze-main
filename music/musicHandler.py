import pygame
class MusicHandler:

    def __init__(self):
         self.tracks = [
            "./music/dark-sanft-final.wav", #music in levels
            "./music/horrer_synths.wav"     #music im start screen
        ]
    def playMusic(self):
        pygame.mixer.music.load(self.tracks[0])
        pygame.mixer.music.play()
    def updateMusic(self):
        if not pygame.mixer.music.get_busy():
            MusicHandler.playMusic(self)