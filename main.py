import pygame
import func
import classes
import math
import random
import time
import sys
import simulation

# R - promień
# N - liczba atomow
# 𝜂 - "eta"
# H = 𝜂𝐻 * R wysokość pojemnika
# L = 𝜂L * R szerokość pojemnika
# pamiętać, że N <= 1/4 * 𝜂𝐻 * 𝜂L
# d - tolerancja zderzenia, przy czym d <= 1/10 * R
# t - czas, przy czym 𝛿𝑡 ≈ 1/𝜅V ; 𝜅 >= min(𝜂𝐻,𝜂𝐿) i 𝑡𝑖=𝑖 𝛿𝑡
# proporcje zbiornika 𝜂 = H/L = 𝜂𝐻/𝜂𝐿 = 1
# Δ𝑡=𝑀 𝛿𝑡 - czerwony atom doznaje Δ𝑁 zderzeń z innymi cząstkami, M >= 10
# 𝜆̅ - srednia droga
# 𝑛 = Δ𝑁/Δ𝑡 - Częstość zderzeń na jednostkę czasu
# zmienne do wprowadzenia - R, 𝜂𝐻, 𝜂L, N, d - z czego  𝜂𝐻 = 𝜂L


pygame.init()

color_light = (155, 155, 155)
color_dark = (15, 15, 15)
color_input_active = pygame.Color('lightskyblue3')  # rozne kolory
color_input_passive = pygame.Color('gray15')

color_r = color_input_passive
color_n = color_input_passive  # kolory text containerow
color_d = color_input_passive
color_eta = color_input_passive
color_m = color_input_passive
active_r = False
active_n = False  # sprawdza czy text container zostal klikniety
active_d = False
active_eta = False
active_m = False
user_input_font = pygame.font.Font(None, 32)  #czcionki
button_font = pygame.font.SysFont('Corbel', 70)

user_input_r = '20'  #przechowuje tekst wpisany przez gracza, a dokladnie R
user_info_r = 'Promień atomów: '
user_input_rect_r = pygame.Rect(500, 65, 140, 32)
user_input_n = '20'  #przechowuje tekst wpisany przez gracza, a dokladnie N
user_info_n = 'Liczba atomów w pojemniku: '
user_input_rect_n = pygame.Rect(500, 215, 140, 32)
user_input_d = '0.5'  #przechowuje tekst wpisany przez gracza, a dokladnie d
user_info_d = 'Tolerancja zderzenia: '
user_input_rect_d = pygame.Rect(500, 365, 140, 32)
user_input_eta = '30'  #przechowuje tekst wpisany przez gracza, a dokladnie 𝜂𝐻 albo 𝜂L
user_info_eta = 'Wartość eta H i eta L: '
user_input_rect_eta = pygame.Rect(500, 515, 140, 32)
user_input_m = '10'  #przechowuje tekst wpisany przez gracza, a dokladnie R
user_info_m = 'Wartość M: '
user_input_rect_m = pygame.Rect(500, 665, 140, 32)
start_rect = pygame.Rect(800, 50, 540, 650)
window = pygame.display.set_mode((1400, 750)) #tworzymy screen
while True:
    mouse = pygame.mouse.get_pos()  # pozycja myszki
    window.fill((0, 0, 0))  # background
    for event in pygame.event.get():  #eventy czyli np ruszenie muszką, klikniecie czegoś, wpisanie
        if event.type == pygame.QUIT:  #klikniecie "X" = wyjscie z programu
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 800 <= mouse[0] <= 1340 and 50 <= mouse[1] <= 700 and user_input_r != '' \
                    and user_input_n != '' and user_input_d != '' and user_input_eta != '' and user_input_m != '':  # rozpoczyna symulację
                simulation.simulation_func(int(user_input_r), int(user_input_n), float(user_input_d), int(user_input_eta), int(user_input_m))
                pygame.quit()
                sys.exit()
            active_r = func.collision_for_rect(user_input_rect_r.collidepoint(event.pos))
            active_n = func.collision_for_rect(user_input_rect_n.collidepoint(event.pos))
            active_d = func.collision_for_rect(user_input_rect_d.collidepoint(event.pos)) #  sprawdza czy kursor jest na prostokacie + zostal wybrany
            active_eta = func.collision_for_rect(user_input_rect_eta.collidepoint(event.pos))
            active_m = func.collision_for_rect(user_input_rect_m.collidepoint(event.pos))

        if event.type == pygame.KEYDOWN:  # pisanie w text containerze
            if active_r:
                user_input_r = func.write_or_delete_in_text_container(user_input_r, event.key, event.unicode)
            elif active_n:
                user_input_n = func.write_or_delete_in_text_container(user_input_n, event.key, event.unicode) #  dopisz/usun tekst
            elif active_d:
                user_input_d = func.write_or_delete_in_text_container(user_input_d, event.key, event.unicode)
            elif active_eta:
                user_input_eta = func.write_or_delete_in_text_container(user_input_eta, event.key, event.unicode)
            elif active_m:
                user_input_m = func.write_or_delete_in_text_container(user_input_m, event.key, event.unicode)
    if 800 <= mouse[0] <= 1340 and 50 <= mouse[1] <= 700 and user_input_r != '' \
                    and user_input_n != '' and user_input_d != '' and user_input_eta != '' and user_input_m != '':  # kolory button
        pygame.draw.rect(window, color_light, start_rect)
    else:
        pygame.draw.rect(window, color_dark, start_rect)
    color_r = func.is_active(active_r)
    color_n = func.is_active(active_n)  # zmienia kolor text containera
    color_d = func.is_active(active_d)
    color_eta = func.is_active(active_eta)
    color_m = func.is_active(active_m)
    pygame.draw.rect(window, color_r, user_input_rect_r, 2)
    pygame.draw.rect(window, color_n, user_input_rect_n, 2)  # rysuje text containery
    pygame.draw.rect(window, color_d, user_input_rect_d, 2)
    pygame.draw.rect(window, color_eta, user_input_rect_eta, 2)
    pygame.draw.rect(window, color_m, user_input_rect_m, 2)
    text_surface_r = user_input_font.render(user_input_r, True, (255, 255, 255))
    text_surface_n = user_input_font.render(user_input_n, True, (255, 255, 255))
    text_surface_d = user_input_font.render(user_input_d, True, (255, 255, 255))
    text_surface_eta = user_input_font.render(user_input_eta, True, (255, 255, 255))  # generowanie wszyskich tekstow (rownież te ktore użytkownik wprowadza)
    text_surface_m = user_input_font.render(user_input_m, True, (255, 255, 255))
    start_text = button_font.render('START', True, (255, 255, 255))
    text_surface_r_info = user_input_font.render(user_info_r, True, (255, 255, 255))
    text_surface_n_info = user_input_font.render(user_info_n, True, (255, 255, 255))
    text_surface_d_info = user_input_font.render(user_info_d, True, (255, 255, 255))
    text_surface_eta_info = user_input_font.render(user_info_eta, True, (255, 255, 255))
    text_surface_m_info = user_input_font.render(user_info_m, True, (255, 255, 255))
    window.blit(text_surface_r_info, (100, 70))
    window.blit(text_surface_n_info, (100, 220))
    window.blit(text_surface_d_info, (100, 370))  # wyswietl
    window.blit(text_surface_eta_info, (100, 520))
    window.blit(text_surface_m_info, (100, 670))
    window.blit(text_surface_r, (user_input_rect_r.x + 5, user_input_rect_r.y + 5))  # wyświetl teksty (rownież te ktore użytkownik wprowadza) / text containery
    window.blit(text_surface_n, (user_input_rect_n.x + 5, user_input_rect_n.y + 5))
    window.blit(text_surface_d, (user_input_rect_d.x + 5, user_input_rect_d.y + 5))
    window.blit(text_surface_eta, (user_input_rect_eta.x + 5, user_input_rect_eta.y + 5))
    window.blit(text_surface_m, (user_input_rect_m.x + 5, user_input_rect_m.y + 5))
    user_input_rect_r.w = max(40, text_surface_r.get_width() + 10)
    user_input_rect_n.w = max(40, text_surface_n.get_width() + 10)
    user_input_rect_d.w = max(40, text_surface_d.get_width() + 10) # ustaw szerokośc prostokatow
    user_input_rect_eta.w = max(40, text_surface_eta.get_width() + 10)
    user_input_rect_m.w = max(40, text_surface_m.get_width() + 10)
    window.blit(start_text, (975, 335))

    pygame.display.update() #odswieżenie