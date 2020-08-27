def plot_menu(numAtoms, ave_s, freq):
    import main
    import simulation
    import classes
    import pygame
    import matplotlib
    import sys
    pygame.init()
    matplotlib.use("Agg")
    plot_left = classes.Plot(5, 5, 100, 'white', 'white', numAtoms, ave_s)  # tworzy wykresy
    plot_right = classes.Plot(5, 5, 100, 'white', 'white', numAtoms, freq)
    surf_left = plot_left.update_plot(numAtoms, ave_s, plot_left)
    surf_right = plot_right.update_plot(numAtoms, freq, plot_right)
    pygame.display.flip()
    clock = pygame.time.Clock()
    FPS = 60
    info_font = pygame.font.SysFont('Corbel', 16)
    ave_s_info = 'Średnia droga'
    freq_info = 'Częstość zderzeń'
    numAtoms_info = 'Liczba atomów'
    exit_info = 'WYJDŹ'
    text_ave_s = info_font.render(ave_s_info, True, (0, 0, 0))
    text_numAtoms = info_font.render(numAtoms_info, True, (0, 0, 0))
    text_freq = info_font.render(freq_info, True, (0, 0, 0))
    while True:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 575 <= mouse[0] <= 775 and 650 <= mouse[1] <= 710:
                    pygame.quit()
                    sys.exit()
        if 575 <= mouse[0] <= 775 and 650 <= mouse[1] <= 710:
            text_exit = main.button_font.render(exit_info, True, (255, 255, 255))
        else:
            text_exit = main.button_font.render(exit_info, True, (155, 255, 155))
        pygame.display.flip()
        main.window.fill((0, 0, 0))
        main.window.blit(surf_left, (125, 100))
        main.window.blit(surf_right, (725, 100))
        main.window.blit(text_exit, (575, 650))
        main.window.blit(pygame.transform.rotate(text_ave_s, 90), (130, 305))
        main.window.blit(text_numAtoms, (330, 580))
        main.window.blit(text_numAtoms, (930, 580))
        main.window.blit(pygame.transform.rotate(text_freq, 90), (730, 305))
        pygame.display.update()
