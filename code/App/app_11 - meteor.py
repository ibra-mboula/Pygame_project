import pygame, sys
from random import randint,uniform


def laser_update(laser_list, speed = 300):
  for laser in laser_list:
      laser.y -= speed * delta_time
      if laser.bottom < 0:
        laser_list.remove(laser)
        print("laser removed") 

def display_score():
  score_text = f"S C O R E : {pygame.time.get_ticks() // 1000}" # # // pour avoir un entier
  text_image = font.render(score_text, True, (255,255,255)) # True pour activer l'anti-aliasing
  text_rect = text_image.get_rect(center = (text_rect_x, text_rect_y)) # pour créer un rectangle autour du texte
  display_surface.blit(text_image, text_rect) # pour afficher le texte
  pygame.draw.rect(display_surface,'white',text_rect.inflate(30,30) ,width = 5, border_radius = 6 )

#laser delay  - pour gérer le temps entre chaque tir
def laser_timer(can_shoot, shoot_delay):
  if can_shoot == False:
    current_time = pygame.time.get_ticks() # pour récupérer le temps en millisecondes depuis le début du jeu 
    if current_time - shoot_timer > shoot_delay:
      can_shoot = True

  return can_shoot

# todo 3 - créer une fonction pour créer des météores
def meteor_update(meteor_list, speed = 200):
  for meteor_tuple in meteor_list:
      direction = meteor_tuple [1]
      meteor_rect = meteor_tuple [0]
      meteor_rect.center += direction * speed * delta_time* 1.2
      if meteor_rect.top > WINDOW_HEIGHT:
        meteor_list.remove(meteor_tuple)
        print("meteor removed")
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
# import laser
# importer une image laser
laser_image = pygame.image.load("code/assets/laser.png").convert_alpha()
# rectangle pour le laser qui est placé au milieur du top du rectangle du vaisseau
laser_rect = laser_image.get_rect(midbottom = (660,300))

laser_list = [] # pour stocker les lasers # list of laser

# laser timer
# laser timer
can_shoot = True
shoot_timer = None

""" ------------------import bg --------------------------------------- """

# importer une images background
background_image = pygame.image.load("code/assets/background.png").convert_alpha() # importer une image de fond

""" ------------------import txt--------------------------------------- """

# importer le texte 
font = pygame.font.Font("code/assets/subatomic.ttf", 30)
text_image = font.render(f"S C O R E : {pygame.time.get_ticks()}", True, (255,255,255)) # True pour activer l'anti-aliasing

text_rect_x = 650
text_rect_y = WINDOW_WEIGHT/2 + 25

""" ------------------drawing--------------------------------------- """
#  dessiner un rect
test_rect = pygame.Rect(text_rect_x-150, text_rect_y-26,280,50)
    
""" ------------------Meteor--------------------------------------- """  
#todo1: créer un timer pour faire apparaître les météorites  
meteor_image = pygame.image.load("code/assets/meteor.png").convert_alpha()
meteor_image = pygame.transform.scale(meteor_image, (100, 100))
meteor_List = [] # list of meteor

meteor_timer = pygame.event.custom_type() # pour créer un événement personnalisé
pygame.time.set_timer(meteor_timer, 500) # pour créer un timer qui va déclencher l'événement meteor_timer toutes les 1000 millisecondes

""" ------------------game loop--------------------------------------- """

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
  
  # laser list 
  # laser timer MAJ can_shoot = False     
  if envent.type == pygame.MOUSEBUTTONDOWN and can_shoot: # si l'événement est de type MOUSEBUTTONDOWN (click gauche)
    
    #laser
    laser_rect = laser_image.get_rect(midbottom = ship_rect.midtop) # pour créer un rectangle autour du laser
    laser_list.append(laser_rect)
    
    #timer
    can_shoot = False
    shoot_timer = pygame.time.get_ticks() 
    

  #todo2: si l'événement est de type meteor_timer, créer un météorite et l'ajouter à la liste des météorites
  if envent.type == meteor_timer:
    
    rand_x = randint(-100, WINDOW_WEIGHT+100)
    rand_Y = randint(-100, -50)
    
    meteor_rect = meteor_image.get_rect(center = (rand_x, rand_Y)) # pour créer un rectangle autour du meteor
    direction = pygame.math.Vector2(uniform(-0.5,0.5), 1) # pour créer un vecteur direction
    meteor_List.append((meteor_rect,direction))
    print(direction)
    
  
  # ! 2.  update - update game state
  
  laser_update(laser_list) # pour faire déplacer le laser vers le haut
  # todo4: faire déplacer les météorites vers le bas
  meteor_update(meteor_List) # pour faire déplacer le meteor vers le bas
  # laser timer MAJ can_shoot = True 
  can_shoot = laser_timer(can_shoot, 100) # pour limiter le nombre de tirs par seconde (1000 = 1 seconde) 
  
  #print(pygame.time.get_ticks()) # pour afficher le temps en millisecondes
  
  # pour remplir la surface 
  display_surface.fill((0,0,0)) #fill = remplir (pour remplir la surface de la couleur (0,0,0) = noir)

  # afficher le background sur la surface 
  display_surface.blit(background_image, (0,0)) # blit = block image transfer (pour afficher une image sur une surface)
 
   #pygame.draw.lines(display_surface,'red','False',[(10,10),(200,10)], width = 1)

  # afficher le vaisseau avec le rectangle sur la surface  
  display_surface.blit(ship_image, ship_rect) 
  
  
  
  display_score() # pour afficher le score

  #  afficher le score
  
  #  afficher laser
  for laser_rect in laser_list: 
    display_surface.blit(laser_image, laser_rect) 
    #laser_rect.y -= round(200 *delta_time) 

#todo 5 : afficher les météorites
  for meteor_tuple in meteor_List:
    display_surface.blit(meteor_image, meteor_tuple[0]) 
    #meteor_rect.y += round(200 *delta_time)
    
  # ! 3. render - draw to the screen, show the player what's going on
  
  pygame.display.update() # pour mettre à jour l'affichage de la fenêtre (à mettre à la fin de la boucle) 
  #print(len(laser_list))