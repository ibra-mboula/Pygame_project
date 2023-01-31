import pygame, sys


""" ------------------game init--------------------------------------- """

pygame.init() # pour initialiser pygame et ses modules (audio, video, etc...) 

WINDOW_WEIGHT = 1280 # largeur de la fenêtre
WINDOW_HEIGHT = 720 # hauteur de la fenêtre

# créer une surface
display_surface = pygame.display.set_mode((WINDOW_WEIGHT, WINDOW_HEIGHT)) # pour créer une fenêtre de 800x600 pixels
pygame.display.set_caption("Asteroid shooter") # pour donner un titre à la fenêtre

#  clock - pour gérer le temps du jeu 
clock = pygame.time.Clock() # pour créer un objet clock

""" ------------------import ship--------------------------------------- """

# importer une images vaisseau
ship_image = pygame.image.load("code/assets/ship.png").convert_alpha() # importer une image du vaisseau
#  redimensionner le vaisseau
new_width, new_height = 100, 100
ship_image = pygame.transform.scale(ship_image, (new_width, new_height))
#  positionner le vaisseau
ship_position_x = 900
ship_position_y = 800
# rect - pour créer un rectangle autour du vaisseau
ship_rect = ship_image.get_rect(center = (660, 350)) # pour créer un rectangle autour du vaisseau

""" ------------------import laser--------------------------------------- """
#todo 1 : import laser
# importer une image laser
laser_image = pygame.image.load("code/assets/laser.png").convert_alpha()
# rectangle pour le laser qui est placé au milieur du top du rectangle du vaisseau
laser_rect = laser_image.get_rect(midbottom = (660,300))

""" ------------------import bg --------------------------------------- """

# importer une images background
background_image = pygame.image.load("code/assets/background.png").convert_alpha() # importer une image de fond

""" ------------------import txt--------------------------------------- """

# importer le texte 
font = pygame.font.Font("code/assets/subatomic.ttf", 30)
text_image = font.render("G A L A X Y", True, (255,255,255)) # True pour activer l'anti-aliasing

# text rect - pour créer un rectangle autour du texte
text_rect_x = 650
text_rect_y = WINDOW_WEIGHT/2 + 25
text_rect = text_image.get_rect(center = (text_rect_x, text_rect_y)) # pour créer un rectangle autour du texte


while True: # boucle infinie

  # ! 1. input - envents (mouse click, key press, controller, etc...)
  
  for envent in pygame.event.get(): # pour récupérer les événements 
    
    if envent.type == pygame.QUIT: # si l'événement est de type QUIT (croix rouge)
      pygame.quit() # pour quitter pygame
      sys.exit() # pour quitter le programme

  #ship_rect.center = pygame.mouse.get_pos() # pour récupérer la position de la souris
  
  #  frameratelimit - pour limiter le nombre d'images par seconde donc la vitesse du ship
  clock.tick(120) # pour limiter le nombre d'images par seconde à 60
  
  #todo 3 : faire deplacer le laser
  laser_rect.y -= 2

  
  # ! 2.  update - update game state
  
  # * ordre 1 pour remplir la surface 
  display_surface.fill((0,0,0)) #fill = remplir (pour remplir la surface de la couleur (0,0,0) = noir)
  
  # * ordre 2 afficher le background sur la surface 
  display_surface.blit(background_image, (0,0)) # blit = block image transfer (pour afficher une image sur une surface)
  
  # * ordre 3 afficher le vaisseau sur la surface a la position (250,250)
  # afficher le vaisseau avec le rectangle sur la surface  
  display_surface.blit(ship_image, ship_rect) 
    

  # * : ordre 4 afficher le texte sur la surface
  display_surface.blit(text_image, text_rect)
  
  #todo 2 : afficher laser
  display_surface.blit(laser_image, laser_rect) 
  


  # ! 3. render - draw to the screen, show the player what's going on
  
  pygame.display.update() # pour mettre à jour l'affichage de la fenêtre (à mettre à la fin de la boucle) 