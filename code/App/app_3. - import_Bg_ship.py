import pygame, sys

pygame.init() # pour initialiser pygame et ses modules (audio, video, etc...) 


WINDOW_WEIGHT = 1280 # largeur de la fenêtre
WINDOW_HEIGHT = 720 # hauteur de la fenêtre


display_surface = pygame.display.set_mode((WINDOW_WEIGHT, WINDOW_HEIGHT)) # pour créer une fenêtre de 800x600 pixels
pygame.display.set_caption("Asteroid shooter") # pour donner un titre à la fenêtre

# todo 1 : importer une image du vaisseau
ship_image = pygame.image.load("code/assets/ship.png").convert_alpha()

# todo 4 : importer une image de fond
background_image = pygame.image.load("code/assets/background.png").convert_alpha()


# todo 2 : redimensionner le vaisseau
new_width, new_height = 100, 100
ship_image = pygame.transform.scale(ship_image, (new_width, new_height))

# todo 6 : importer le texte 
font = pygame.font.Font("code/assets/subatomic.ttf", 30)
text_surface = font.render("G A L A X Y", True, (255,255,255)) # True pour activer l'anti-aliasing

while True: # boucle infinie

  # ! 1. input - envents (mouse click, key press, controller, etc...)
  
  for envent in pygame.event.get(): # pour récupérer les événements 
    
    if envent.type == pygame.QUIT: # si l'événement est de type QUIT (croix rouge)
      pygame.quit() # pour quitter pygame
      sys.exit() # pour quitter le programme
  
  # ! 2.  update - update game state
  
  # * ordre 1 pour remplir la surface de gris 
  display_surface.fill((0,0,0)) #fill = remplir (pour remplir la surface de la couleur (0,0,0) = noir)
  
  # todo 5 : ordre 2 afficher le background sur la surface 
  display_surface.blit(background_image, (0,0)) # blit = block image transfer (pour afficher une image sur une surface)
  
  # todo 3 : ordre 3 afficher le vaisseau sur la surface a la position (250,250)
  display_surface.blit(ship_image, (450,450)) 
  
  # todo 7 : ordre 4 afficher le texte sur la surface
  display_surface.blit(text_surface, (580,200))

  # ! 3. render - draw to the screen, show the player what's going on
  
  pygame.display.update() # pour mettre à jour l'affichage de la fenêtre (à mettre à la fin de la boucle) 