def simulation_func(r, n, d, eta, M):
    import main
    import classes
    import func
    import pygame
    import random
    import sys
    import math
    import matplotlib
    matplotlib.use("Agg")
    width_container = r * eta
    height_container = r * eta
    up_wall = 25
    left_wall = 125
    down_wall = height_container + up_wall  # odpowiednio gorna, lewa, dolna, prawa sciana pojemnika
    right_wall = width_container + left_wall
    container = pygame.Rect(left_wall, up_wall, width_container, height_container) # pojemnik
    atoms = [] #  lista z kulkami/atomami
    red_atom = classes.Atom(r, 'red', right_wall, down_wall, up_wall, left_wall, atoms, (255, 0, 0))  # tworzy czerwony atom
    atoms.append(red_atom)
    for i in range(n - 1): #  tworzy niebieskie atomy
        blue_atom = classes.Atom(r, 'blue', right_wall, down_wall, up_wall, left_wall, atoms, (0, 0, 255))
        atoms.append(blue_atom)
    list_data_x_upper = []
    list_data_y_upper = []
    list_data_x_bottom = [] #  lista z danymi do wykresu
    list_data_y_bottom = []
    plot_upper = classes.Plot(3, 3, 100, 'white', 'white', list_data_x_upper, list_data_y_upper) # tworzy wykresy
    plot_bottom = classes.Plot(3, 3, 100, 'white', 'white', list_data_x_bottom, list_data_y_bottom)
    screen = pygame.display.get_surface()
    pygame.display.flip()
    x_upper = 2  #  podmienic z danymi do wykresu
    x_bottom = 2  #
    y_upper = 2
    y_bottom = 2
    list_font = pygame.font.SysFont('Corbel', 16)
    while True:
        x_upper += 0.005  #
        y_upper += 2  #
        x_bottom += 0.005  #
        y_bottom += 2  # podmienic z danymi do wykresu
        list_u_x = list_font.render(str(x_upper)[:6] + ' s', True, (110, 110, 110))
        list_u_y = list_font.render(str(y_upper)[:6], True, (110, 110, 110)) # najnowsza wartosc obok wykresu
        list_d_x = list_font.render(str(x_bottom)[:6] + ' s', True, (110, 110, 110))
        list_d_y = list_font.render(str(y_bottom)[:6], True, (110, 110, 110))
        surf_u = plot_upper.update_plot(x_upper, y_upper, list_data_x_upper, list_data_y_upper, plot_upper)
        surf_b = plot_bottom.update_plot(x_bottom, y_bottom, list_data_x_bottom, list_data_y_bottom, plot_bottom) #  aktualizacja wykresu
        pygame.display.flip()
        main.window.fill((0, 0, 0))
        screen.blit(surf_u, (1050, 50)) #  wyswietla wykres
        screen.blit(surf_b, (1050, 400))
        pygame.draw.rect(main.window, main.color_light, container, 2) #  rysuje pojemnik
        for event in pygame.event.get():  # eventy czyli np ruszenie muszką, klikniecie czegoś, wpisanie
            if event.type == pygame.QUIT:  # klikniecie "X" = wyjscie z programu
                pygame.quit()
                sys.exit()
        main.window.blit(list_u_x, (1293, 334))
        main.window.blit(list_u_y, (1055, 50))
        main.window.blit(list_d_x, (1293, 684)) #  najnowsza wartosc zostanie wyswietlona obok wykresu
        main.window.blit(list_d_y, (1055, 400))
        for atom in atoms: #  wyswietla wszystkie atomy
            atom.drawing_circle(main.window, atom)
            
        #zderzenia ze scianami
        for atom in atoms:
            atom.x += atom.x_speed              #testowe latanie
            atom.y += atom.y_speed
            if atom.x + atom.r + d >= right_wall:    #prawa
                atom.x_speed = -atom.x_speed
            elif atom.x - atom.r + d <= left_wall:    #lewa
                atom.x_speed = -atom.x_speed
            if atom.y - atom.r + d <= up_wall:    #gorna
                atom.y_speed = -atom.y_speed
            elif atom.y + atom.r + d >= down_wall:    #dolna
                atom.y_speed = -atom.y_speed

        #zderzenia między kulkami
        for i in range(len(atoms)):             #przelatujemy przez wszystkie mozliwe zderzenia bez powtorzen
            for j in range(len(atoms)):
                if i > j:
                    if distance(atoms[i].x, atoms[i].y, atoms[j].x, atoms[j].y) <= 2*r:     #sprawdzamy czy się zderzyly
                        tmp_x = int(atoms[i].x_speed)
                        atoms[i].x_speed = int(atoms[j].x_speed)
                        atoms[j].x_speed = int(tmp_x)
                        tmp_y = int(atoms[i].y_speed)
                        atoms[i].y_speed = int(atoms[j].y_speed)
                        atoms[j].y_speed = int(tmp_y)
        
        pygame.display.update()  # odswieżenie
