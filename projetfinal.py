import pygame
import math
from game import Game
pygame.init()
clock = pygame.time.Clock() # démarer une horloge



#génerer la fenetre de notre jeu
pygame.display.set_caption("space invadors")
pygame.display.set_mode((1500,1000))
 

#permet d'importer et de changer l'arriere plan de notre jeu
background = pygame.image.load('assets/SPACES_BG-2.png')
screen_x = 1500
screen_y = 1000
screen = pygame.display.set_mode((screen_x , screen_y)) 
scroll_x = 0

print(screen_x, screen_y)
print(pygame.display.Info())

#importer notre boutton pour lancer partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (300, 200))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.8) #arrondi a l'entier suivant
play_button_rect.y = math.ceil(screen.get_height() / 2)


#charger notre jeu
game = Game()

scroll = True
 
while scroll:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           scroll = False 
    clock.tick(60)
    scroll_x -= 2
    if scroll_x < -screen_x:
        scroll_x = 0
    screen.blit(background, (scroll_x, 0))
    screen.blit(background, (scroll_x + screen_x, 0))
  

# x_background = -500

# running = True

#boucle tant que cette condition est vrai
# while running:
#     x_background -= 5
#     # appliquer arriere plan du jeu
#     if x_background < 10000:
#         screen.blit(background, (x_background, -300))
#         screen.blit(background, (x_background -500, -300))
#     else:
#         x_background = -500
#         screen.blit(background, (x_background, -300))
#running = True
# i = 0
# boucle tant que cette condition est vrai
# while running:
#     x_background -= 5
#     # appliquer arriere plan du jeu
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     screen.fill((0,0,0))

#     #on crée un arrière-plan en continu
#     screen.blit(background, (i, 0))
#     screen.blit(background, (1080+i, 0))
#     if i == - 1080:
#         screen.blit(background, (1080+i, 0))
#         i = 0
#     i -= 1

    
    
    
    if game.is_playing:
        #declencher les instructions de notre partie
        game.update(screen)
    #verifier si notre jeu n'a pas commencé
    else:
        #ajouter ecran de bienvenue
        screen.blit(play_button,play_button_rect)


    #mettre a jour notre ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get() :
        #pour verifier que l'evenement est fermeture fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type== pygame.MOUSEBUTTONDOWN:
            #savoir si le joueur appuie sur le boutton jouer
            if play_button_rect.collidepoint(event.pos):
            #lancer le jeu
                game.is_playing = True





