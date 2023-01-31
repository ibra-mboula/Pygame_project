import pygame, sys

pygame.init() # pour initialiser pygame et ses modules (audio, video, etc...) 


WINDOW_WEIGHT = 1280 # largeur de la fenêtre
WINDOW_HEIGHT = 720 # hauteur de la fenêtre


display_surface = pygame.display.set_mode((WINDOW_WEIGHT, WINDOW_HEIGHT)) # pour créer une fenêtre de 800x600 pixels

pygame.display.set_caption("Asteroid shooter") # pour donner un titre à la fenêtre


 
while True: # boucle infinie
    
  # todo : 1. input - envents (mouse click, key press, controller, etc...)
  
  for envent in pygame.event.get(): # pour récupérer les événements 
    
    if envent.type == pygame.QUIT: # si l'événement est de type QUIT (croix rouge)
      pygame.quit() # pour quitter pygame
      sys.exit() # pour quitter le programme
  
  # todo : 2.  update - update game state
  
  
  
  # todo : 3. render - draw to the screen, show the player what's going on
  
    pygame.display.update() # pour mettre à jour l'affichage de la fenêtre (à mettre à la fin de la boucle) 