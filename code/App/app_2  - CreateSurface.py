import pygame, sys

pygame.init() # pour initialiser pygame et ses modules (audio, video, etc...) 


WINDOW_WEIGHT = 1280 # largeur de la fenêtre
WINDOW_HEIGHT = 720 # hauteur de la fenêtre


display_surface = pygame.display.set_mode((WINDOW_WEIGHT, WINDOW_HEIGHT)) # pour créer une fenêtre de 800x600 pixels
pygame.display.set_caption("Asteroid shooter") # pour donner un titre à la fenêtre

# todo : cree une surface
test_surface = pygame.Surface((300, 100)) # pour créer une surface de 500x200 pixels

# todo : attacher la surface à la fenêtre dans  !update


 
while True: # boucle infinie
    
  #  1. input - envents (mouse click, key press, controller, etc...)
  
  for envent in pygame.event.get(): # pour récupérer les événements 
    
    if envent.type == pygame.QUIT: # si l'événement est de type QUIT (croix rouge)
      pygame.quit() # pour quitter pygame
      sys.exit() # pour quitter le programme
  
  #  2.  update - update game state
  
  # todo : remplir la surface de gris
  display_surface.fill("gray") # pour remplir la surface de gris 
  
  # todo : couleur de la surface
  test_surface.fill((186,120,39)) # pour remplir la surface 
  
  # todo : attacher la surface à la fenêtre et la positionner
  display_surface.blit(test_surface, (WINDOW_WEIGHT-300, 250)) # pour attacher la surface à la fenêtre et la positionner
  
  
  #  3. render - draw to the screen, show the player what's going on
  
  pygame.display.update() # pour mettre à jour l'affichage de la fenêtre (à mettre à la fin de la boucle) 