import sidemain, pygame


if __name__ == "__main__":
    
    pygame.init()

    clock = pygame.time.Clock()

    g= sidemain.Game()


    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    pygame.display.set_caption("AFK simulator")

    menu_bg = pygame.image.load("assets/menu_bg.png").convert()
    menu_bg = pygame.transform.scale(menu_bg, (1280, 720))







    while True:

        screen.blit(menu_bg, (0,0))

        pygame.draw.rect()

        for event in pygame.event.get():


            if event.type==pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE) and g.gamestate=='Main':
                    g.pause()
                    

        

        
        pygame.display.flip()

        clock.tick(60)