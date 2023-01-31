import pygame, sys


#todo 6 : 
def laser_update(laser_list, speed = 300):
  for laser in laser_list:
      laser.y -= speed * delta_time
      if laser.bottom < 0:
        laser_list.remove(laser)
        print("laser removed") 

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
ship_position_x, ship_position_y = 900,800
# rect - pour créer un rectangle autour du vaisseau
ship_rect = ship_image.get_rect(center = (660, 350)) # pour créer un rectangle autour du vaisseau


""" ------------------import laser--------------------------------------- """
#todo 1 : import laser
# importer une image laser
laser_image = pygame.image.load("code/assets/laser.png").convert_alpha()
# rectangle pour le laser qui est placé au milieur du top du rectangle du vaisseau
laser_rect = laser_image.get_rect(midbottom = (660,300))

laser_list = [] # pour stocker les lasers #todo 3 : list of laser

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


""" ------------------drawing--------------------------------------- """
#todo 1 :  dessiner un rect
test_rect = pygame.Rect(text_rect_x-150, text_rect_y-26,280,50)
    

while True: # boucle infinie

  # ! 1. input - envents (mouse click, key press, controller, etc...)
  
  for envent in pygame.event.get(): # pour récupérer les événements 
    
    if envent.type == pygame.QUIT: # si l'événement est de type QUIT (croix rouge)
      pygame.quit() # pour quitter pygame
      sys.exit() # pour quitter le programme

  ship_rect.center = pygame.mouse.get_pos() # pour récupérer la position de la souris et deplacer le ship
  
  # pour limiter le nombre d'images par seconde (120) et 1000 pour avoir le temps en secondes (delta_time)
  delta_time = clock.tick(200) /1000 
  
  #faire deplacer le laser
  #laser_rect.y -= round(200 *delta_time) # pour faire déplacer le laser vers le haut  
  
  #todo 4 :  laser list 
  if envent.type == pygame.MOUSEBUTTONDOWN: # si l'événement est de type MOUSEBUTTONDOWN (click gauche)
    print("click")
    laser_rect = laser_image.get_rect(midbottom = ship_rect.midtop) # pour créer un rectangle autour du laser
    laser_list.append(laser_rect)
    print(laser_list)


  
  # ! 2.  update - update game state
  
  laser_update(laser_list) # pour faire déplacer le laser vers le haut
  
  # pour remplir la surface 
  display_surface.fill((0,0,0)) #fill = remplir (pour remplir la surface de la couleur (0,0,0) = noir)
  
  # afficher le background sur la surface 
  display_surface.blit(background_image, (0,0)) # blit = block image transfer (pour afficher une image sur une surface)
  
    # todo 2 :  draw rect on displat surf
  pygame.draw.rect(display_surface,'white',text_rect.inflate(30,30) ,width = 5, border_radius = 6 )
   #pygame.draw.lines(display_surface,'red','False',[(10,10),(200,10)], width = 1)
  
    # afficher le texte sur la surface
  display_surface.blit(text_image, text_rect)
  
  # afficher le vaisseau avec le rectangle sur la surface  
  display_surface.blit(ship_image, ship_rect) 

  # #todo 5 :  afficher laser
   
  for laser_rect in laser_list: 
    display_surface.blit(laser_image, laser_rect) 
    #laser_rect.y -= round(200 *delta_time) 

  # ! 3. render - draw to the screen, show the player what's going on
  
  pygame.display.update() # pour mettre à jour l'affichage de la fenêtre (à mettre à la fin de la boucle) 
  print(len(laser_list))