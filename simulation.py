def simulation_func(r, n, d, eta, M, time):
    import main
    import classes
    import func
    import pygame
    import sys
    import math
    width_container = r * eta
    height_container = r * eta
    up_wall = 25
    left_wall = 125
    down_wall = height_container + up_wall
    right_wall = width_container + left_wall
    container = pygame.Rect(left_wall, up_wall, width_container, height_container)
    atoms = []
    red_atom = classes.Atom(r, 'red', right_wall, down_wall, up_wall, left_wall, atoms,
                            (255, 0, 0))  # tworzy czerwony atom
    atoms.append(red_atom)
    for i in range(n - 1):  # tworzy niebieskie atomy
        blue_atom = classes.Atom(r, 'blue', right_wall, down_wall, up_wall, left_wall, atoms, (0, 0, 255))
        atoms.append(blue_atom)
    pygame.display.flip()
    value_info_time = 'Czas: '
    value_info_1 = 'Śr. droga swobodna: '
    value_info_2 = 'Liczba zderzeń: '
    value_info_3 = 'Liczba atomów: '
    value_info_rect_time = pygame.Rect(990, 25, 360, 40)
    value_info_rect_1 = pygame.Rect(990, 225, 360, 40)
    value_info_rect_2 = pygame.Rect(990, 425, 360, 40)
    value_info_rect_3 = pygame.Rect(990, 625, 360, 40)
    sr_droga = 0
    droga_swobodna = 0
    tab_droga_swobodna = []
    DeltaN = 0
    list_font = pygame.font.SysFont('Corbel', 32)
    for atom in atoms:  # wyswietla wszystkie atomy
        atom.drawing_circle(main.window, atom)
    clock = pygame.time.Clock()
    loop_time = 0
    time_time = 0  # wyswietlany czas co kazdą klatkę np: (1 sek / 60 odswiezen) = 0.016667
    while M > loop_time:
        droga_swobodna += func.distance(0, 0, atoms[0].x_speed, atoms[0].y_speed)
        clock.tick(time)
        time_time += 1 / time
        list_1 = list_font.render(value_info_time + str(time_time)[:6] + ' s', True, (110, 110, 110)) # liczy czas od rozpoczecia
        list_2 = list_font.render(value_info_1 + str(sr_droga)[:6], True, (110, 110, 110))  #
        list_3 = list_font.render(value_info_2 + str(DeltaN)[:6], True, (110, 110, 110))  #
        list_4 = list_font.render(value_info_3 + str(n)[:6], True, (110, 110, 110))  #
        pygame.display.flip()
        main.window.fill((0, 0, 0))
        pygame.draw.rect(main.window, main.color_light, container, 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(main.window, main.color_light, value_info_rect_time, 2)
        pygame.draw.rect(main.window, main.color_light, value_info_rect_1, 2)
        pygame.draw.rect(main.window, main.color_light, value_info_rect_2, 2)
        pygame.draw.rect(main.window, main.color_light, value_info_rect_3, 2)
        main.window.blit(list_1, (value_info_rect_time.x + 5, value_info_rect_time.y + 5))
        main.window.blit(list_2, (value_info_rect_1.x + 5, value_info_rect_1.y + 5))
        main.window.blit(list_3, (value_info_rect_2.x + 5, value_info_rect_2.y + 5))
        main.window.blit(list_4, (value_info_rect_3.x + 5, value_info_rect_3.y + 5))
        # zderzenia między kulkami
        for i in range(len(atoms)):  # przelatujemy przez wszystkie zderzenia
            atoms[i].x += atoms[i].x_speed  #ruch atomow  
            atoms[i].y += atoms[i].y_speed
            for j in range(len(atoms)):
                if i > j:
                    if func.distance(atoms[i].x, atoms[i].y, atoms[j].x,
                                     atoms[j].y) <= 2 * r + math.floor(1/10 * r):  # sprawdzamy czy się zderzyly 
                        if j == 0:
                            DeltaN += 1
                            tab_droga_swobodna.append(droga_swobodna)
                            droga_swobodna = 0
                            sr_droga = sum(tab_droga_swobodna) / DeltaN
                        tmp_x = int(atoms[i].x_speed)  #zamiana wektorow predkosci
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
        loop_time += 1
    czestosc_zderzen = DeltaN * M / time
    return sr_droga, czestosc_zderzen, n # zwracamy wartosci do tablicy ( 1) srednia droga, 2) czestosc zderzen, 3) liczba atomow)
