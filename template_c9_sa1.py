import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
bird=pygame.Rect(100,250,30,30)

# Create a variable 'groundx' and initialize to 0.


while True:
    
  screen.blit(images["bg"],[0,0])
  # Decrement 'groundx'by 5
  
  # Check if 'groundx' becomes less than -550
  
      # Reset the value of 'groundx' back to 0
      
  # Display the ground image at [groundx,550]    
  
  
  screen.blit(images["bird"],bird)
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
        
  
  pygame.display.update()
  pygame.time.Clock().tick(30)
