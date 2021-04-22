import pygame

class Sounds:
    def __init__(self):
        pygame.init()
        self.jump_sound = pygame.mixer.Sound('checkers/assets/jump_sound.wav')
        self.king_sound = pygame.mixer.Sound('checkers/assets/make_king.wav')
        self.music = pygame.mixer.music.load('checkers/assets/music1.wav')
        self.voice = True
    def sounds_off(self):
        self.voice = False
    def sounds_on(self):
        self.voice = True
    def make_jump_sound(self, voice = True):
        if voice:
            self.jump_sound.play()
    def make_king_sound(self, voice = True):
        if voice:
            self.king_sound.play()
    def play_music(self, ID = 0):
        pygame.mixer.music.play(-1)
    def stop_music(self, ID = 0):
        pygame.mixer.music.stop()