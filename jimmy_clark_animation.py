"""Jimmy Clark
Basic Animation
This will move an icon from one place to another.
"""

import pygame

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Moving a wolf")

    background= pygame.image.load("spider.png")
    background = background.convert()
    
    
    wolf = pygame.image.load("howl.png")
    wolf = wolf.convert()
    
    wolf_x = 0
    wolf_y = 200 

    clock = pygame.time.Clock()
    keepGoing = True
    
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        wolf_x += 5
        if wolf_x > screen.get_width():
            wolf_x = 0
                
        screen.blit(background, (0,0))
        screen.blit(wolf, (wolf_x, wolf_y))
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()
    
    
