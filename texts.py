import pygame
from credits_imena import *
credits_font = pygame.font.SysFont('Consolas', 30)

credits_text_developer = credits_font.render(f"Developer : {developer}", True, (255, 255, 255))
credits_text_daniil = credits_font.render(f"Pygame teacher : {pygame_teacher}", True, (255, 255, 255))
credits_text_tata = credits_font.render(f"Programming teacher : {programming_teacher}", True, (255, 255, 255))