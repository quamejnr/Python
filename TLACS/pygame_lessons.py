import pygame


def main():
    pygame.init()
    surface_size = 480

    main_surface = pygame.display.set_mode((surface_size, surface_size))
    small_rect = (165, 165, 150, 100)
    color = (255, 0, 0)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # Data structures and algorithms for game

        main_surface.fill((0, 200, 255))
        main_surface.fill(color, small_rect)
        pygame.display.flip()

    pygame.quit()


main()



