def simulation_func(r, n, d, eta, M):
    import main
    import classes
    import func
    import pygame
    import random
    import sys
    import math
    # import matplotlib
    # matplotlib.use("Agg")
    width_container = r * eta
    height_container = r * eta
    up_wall = 25
    left_wall = 125
    down_wall = height_container + up_wall  # odpowiednio gorna, lewa, dolna, prawa sciana pojemnika
    right_wall = width_container + left_wall
    container = pygame.Rect(left_wall, up_wall, width_container, height_container)  # pojemnik
    atoms = []  # lista z kulkami/atomami
    red_atom = classes.Atom(r, 'red', right_wall, down_wall, up_wall, left_wall, atoms,
                            (255, 0, 0))  # tworzy czerwony atom
    atoms.append(red_atom)
    for i in range(n - 1):  # tworzy niebieskie atomy
        blue_atom = classes.Atom(r, 'blue', right_wall, down_wall, up_wall, left_wall, atoms, (0, 0, 255))
        atoms.append(blue_atom)
    # list_data_x_upper = []
    # list_data_y_upper = []
    # list_data_x_bottom = []  # lista z danymi do wykresu
    # list_data_y_bottom = []
    # plot_upper = classes.Plot(3, 3, 100, 'white', 'white', list_data_x_upper, list_data_y_upper)  # tworzy wykresy
    # plot_bottom = classes.Plot(3, 3, 100, 'white', 'white', list_data_x_bottom, list_data_y_bottom)
    screen = pygame.display.get_surface()
    pygame.display.flip()
    # Okienka z wartosciami
    value_info_time = 'Czas: '
    value_info_1 = 'Cos tam cos tam: '
    value_info_2 = 'xD: ' # zmienic wartosci
    value_info_3 = 'Testowy tekst: '
    value_info_rect_time = pygame.Rect(990, 25, 340, 40)
    value_info_rect_1 = pygame.Rect(990, 225, 340, 40)
    value_info_rect_2 = pygame.Rect(990, 425, 340, 40)
    value_info_rect_3 = pygame.Rect(990, 625, 340, 40)
    value_1 = 2
    value_2 = 2 # podmienic z danymi do wykresu
    value_3 = 2
    list_font = pygame.font.SysFont('Corbel', 32)  # czcionki wyswietlanych wartosci
    for atom in atoms:  # wyswietla wszystkie atomy
        atom.drawing_circle(main.window, atom)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        value_1 += 2  #
        value_2 += 0.005  # Wartości do testow, ostatecznie dac tutaj obliczenia ktore chcemy wyswietlic
        value_3 += 2  #
        list_1 = list_font.render(value_info_time + str(pygame.time.get_ticks())[:6] + ' ms', True, (110, 110, 110)) # liczy czas od rozpoczecia
        list_2 = list_font.render(value_info_1 + str(value_1)[:6], True, (110, 110, 110))  #
        list_3 = list_font.render(value_info_2 + str(value_2)[:6], True, (110, 110, 110))  #
        list_4 = list_font.render(value_info_3 + str(value_3)[:6], True, (110, 110, 110))  #
        # surf_u = plot_upper.update_plot(x_upper, y_upper, list_data_x_upper, list_data_y_upper, plot_upper)
        # surf_b = plot_bottom.update_plot(x_bottom, y_bottom, list_data_x_bottom, list_data_y_bottom, plot_bottom)  # aktualizacja wykresu
        pygame.display.flip()
        main.window.fill((0, 0, 0))
        # screen.blit(surf_u, (1050, 50))  # wyswietla wykres
        # screen.blit(surf_b, (1050, 400))
        pygame.draw.rect(main.window, main.color_light, container, 2)  # rysuje pojemnik
        for event in pygame.event.get():  # eventy czyli np ruszenie muszką, klikniecie czegoś, wpisanie
            if event.type == pygame.QUIT:  # klikniecie "X" = wyjscie z programu
                pygame.quit()
                sys.exit()
        pygame.draw.rect(main.window, main.color_light, value_info_rect_time, 2)
        pygame.draw.rect(main.window, main.color_light, value_info_rect_1, 2)
        pygame.draw.rect(main.window, main.color_light, value_info_rect_2, 2) # rysuje okienka na wartosci
        pygame.draw.rect(main.window, main.color_light, value_info_rect_3, 2)
        main.window.blit(list_1, (value_info_rect_time.x + 5, value_info_rect_time.y + 5))
        main.window.blit(list_2, (value_info_rect_1.x + 5, value_info_rect_1.y + 5))
        main.window.blit(list_3, (value_info_rect_2.x + 5, value_info_rect_2.y + 5))
        main.window.blit(list_4, (value_info_rect_3.x + 5, value_info_rect_3.y + 5))  # wyswietl na ekran najnowsze wartosci
        # zderzenia między kulkami
        for i in range(len(atoms)):  # przelatujemy przez wszystkie mozliwe zderzenia bez powtorzen
            atoms[i].x += atoms[i].x_speed  # testowe latanie
            atoms[i].y += atoms[i].y_speed
            for j in range(len(atoms)):
                if i > j:
                    if func.distance(atoms[i].x, atoms[i].y, atoms[j].x,
                                     atoms[j].y) <= 2 * r + math.floor(1/10 * r):  # sprawdzamy czy się zderzyly
                        tmp_x = int(atoms[i].x_speed)
                        atoms[i].x -= atoms[i].x_speed
                        atoms[j].x -= atoms[j].x_speed
                        atoms[i].x_speed = int(atoms[j].x_speed)
                        atoms[j].x_speed = int(tmp_x)
                        atoms[i].x += atoms[i].x_speed
                        atoms[j].x += atoms[j].x_speed
                        tmp_y = int(atoms[i].y_speed)
                        atoms[i].y -= atoms[i].y_speed
                        atoms[j].y -= atoms[j].y_speed
                        atoms[i].y_speed = int(atoms[j].y_speed)
                        atoms[j].y_speed = int(tmp_y)
                        atoms[i].y += atoms[i].y_speed
                        atoms[j].y += atoms[j].y_speed

        # zderzenia ze scianami
        for atom in atoms:
            if atom.x + atom.r + d >= right_wall:  # prawa
                atom.x_speed = -atom.x_speed
                atom.x = right_wall - atom.r - math.floor(1/10 * r)
            elif atom.x - atom.r + d <= left_wall:  # lewa
                atom.x_speed = -atom.x_speed
                atom.x = left_wall + atom.r + math.floor(1/10 * r)
            if atom.y - atom.r + d <= up_wall:  # gorna
                atom.y_speed = -atom.y_speed
                atom.y = up_wall + atom.r + math.floor(1/10 * r)
            elif atom.y + atom.r + d >= down_wall:  # dolna
                atom.y_speed = -atom.y_speed
                atom.y = down_wall - atom.r - math.floor(1/10 * r)
            atom.drawing_circle(main.window, atom)


        pygame.display.update()  # odswieżenie