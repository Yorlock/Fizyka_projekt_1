import pygame
import func
import plot_menu
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
color_time = color_input_passive
color_repeat = color_input_passive
color_change = color_input_passive
active_r = False
active_n = False  # sprawdza czy text container zostal klikniety
active_d = False
active_eta = False
active_m = False
active_time = False
active_repeat = False
active_change = False
user_input_font = pygame.font.Font(None, 32)  #czcionki
button_font = pygame.font.SysFont('Corbel', 70)

user_input_r = '20'  #przechowuje tekst wpisany przez gracza, a dokladnie R
user_info_r = 'Promień atomów: '
user_input_rect_r = pygame.Rect(500, 70, 140, 32)
user_input_n = '20'  #przechowuje tekst wpisany przez gracza, a dokladnie N
user_info_n = 'Liczba atomów w pojemniku: '
user_input_rect_n = pygame.Rect(500, 150, 140, 32)
user_input_d = '0.5'  #przechowuje tekst wpisany przez gracza, a dokladnie d
user_info_d = 'Tolerancja zderzenia: '
user_input_rect_d = pygame.Rect(500, 230, 140, 32)
user_input_eta = '30'  #przechowuje tekst wpisany przez gracza, a dokladnie 𝜂𝐻 albo 𝜂L
user_info_eta = 'Wartość eta H i eta L: '
user_input_rect_eta = pygame.Rect(500, 310, 140, 32)
user_input_m = '10'  #przechowuje tekst wpisany przez gracza, a dokladnie R
user_info_m = 'Wartość M: '
user_input_rect_m = pygame.Rect(500, 390, 140, 32)
user_input_time = '60'  #przechowuje tekst wpisany przez gracza, a dokladnie R
user_info_time = 'Delta t: '
user_input_rect_time = pygame.Rect(500, 470, 140, 32)
user_input_repeat = '3'  #przechowuje tekst wpisany przez gracza, a dokladnie R
user_info_repeat = 'Liczba symulacji: '
user_input_rect_repeat = pygame.Rect(500, 550, 140, 32)
user_input_change = '1'  #przechowuje tekst wpisany przez gracza, a dokladnie R
user_info_change = 'Dodaj atom co symulację: '
user_input_rect_change = pygame.Rect(500, 630, 140, 32)
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
                    and user_input_n != '' and user_input_d != '' and user_input_eta != '' and user_input_m != '' and user_input_time != '' and user_input_repeat != '' and user_input_change != '':  # rozpoczyna symulację
                i = 0
                numAtoms = []
                ave_s = []
                freq = []
                while i < int(user_input_repeat):
                    s, f, at = simulation.simulation_func(int(user_input_r), int(user_input_n) + i * int(user_input_change), float(user_input_d), int(user_input_eta), int(user_input_m), int(user_input_time))
                    numAtoms.append(at)
                    ave_s.append(s)
                    freq.append(f)
                    i += 1
                plot_menu.plot_menu(numAtoms, ave_s, freq)
                pygame.quit()
                sys.exit()
            active_r = func.collision_for_rect(user_input_rect_r.collidepoint(event.pos))
            active_n = func.collision_for_rect(user_input_rect_n.collidepoint(event.pos))
            active_d = func.collision_for_rect(user_input_rect_d.collidepoint(event.pos)) #  sprawdza czy kursor jest na prostokacie + zostal wybrany
            active_eta = func.collision_for_rect(user_input_rect_eta.collidepoint(event.pos))
            active_m = func.collision_for_rect(user_input_rect_m.collidepoint(event.pos))
            active_time = func.collision_for_rect(user_input_rect_time.collidepoint(event.pos))
            active_repeat = func.collision_for_rect(user_input_rect_repeat.collidepoint(event.pos))
            active_change = func.collision_for_rect(user_input_rect_change.collidepoint(event.pos))

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
            elif active_time:
                user_input_time = func.write_or_delete_in_text_container(user_input_time, event.key, event.unicode)
            elif active_repeat:
                user_input_repeat = func.write_or_delete_in_text_container(user_input_repeat, event.key, event.unicode)
            elif active_change:
                user_input_change = func.write_or_delete_in_text_container(user_input_change, event.key, event.unicode)
    if 800 <= mouse[0] <= 1340 and 50 <= mouse[1] <= 700 and user_input_r != '' \
                    and user_input_n != '' and user_input_d != '' and user_input_eta != '' and user_input_m != '' and user_input_time != '' and user_input_repeat != '' and user_input_change != '':  # kolory button
        pygame.draw.rect(window, color_light, start_rect)
    else:
        pygame.draw.rect(window, color_dark, start_rect)
    color_r = func.is_active(active_r)
    color_n = func.is_active(active_n)  # zmienia kolor text containera
    color_d = func.is_active(active_d)
    color_eta = func.is_active(active_eta)
    color_m = func.is_active(active_m)
    color_time = func.is_active(active_time)
    color_repeat = func.is_active(active_repeat)
    color_change = func.is_active(active_change)
    pygame.draw.rect(window, color_r, user_input_rect_r, 2)
    pygame.draw.rect(window, color_n, user_input_rect_n, 2)  # rysuje text containery
    pygame.draw.rect(window, color_d, user_input_rect_d, 2)
    pygame.draw.rect(window, color_eta, user_input_rect_eta, 2)
    pygame.draw.rect(window, color_m, user_input_rect_m, 2)
    pygame.draw.rect(window, color_time, user_input_rect_time, 2)
    pygame.draw.rect(window, color_repeat, user_input_rect_repeat, 2)
    pygame.draw.rect(window, color_change, user_input_rect_change, 2)
    text_surface_r = user_input_font.render(user_input_r, True, (255, 255, 255))
    text_surface_n = user_input_font.render(user_input_n, True, (255, 255, 255))
    text_surface_d = user_input_font.render(user_input_d, True, (255, 255, 255))
    text_surface_eta = user_input_font.render(user_input_eta, True, (255, 255, 255))  # generowanie wszyskich tekstow (rownież te ktore użytkownik wprowadza)
    text_surface_m = user_input_font.render(user_input_m, True, (255, 255, 255))
    text_surface_time = user_input_font.render(user_input_time, True, (255, 255, 255))
    text_surface_repeat = user_input_font.render(user_input_repeat, True, (255, 255, 255))
    text_surface_change = user_input_font.render(user_input_change, True, (255, 255, 255))
    start_text = button_font.render('START', True, (255, 255, 255))
    text_surface_r_info = user_input_font.render(user_info_r, True, (255, 255, 255))
    text_surface_n_info = user_input_font.render(user_info_n, True, (255, 255, 255))
    text_surface_d_info = user_input_font.render(user_info_d, True, (255, 255, 255))
    text_surface_eta_info = user_input_font.render(user_info_eta, True, (255, 255, 255))
    text_surface_m_info = user_input_font.render(user_info_m, True, (255, 255, 255))
    text_surface_time_info = user_input_font.render(user_info_time, True, (255, 255, 255))
    text_surface_repeat_info = user_input_font.render(user_info_repeat, True, (255, 255, 255))
    text_surface_change_info = user_input_font.render(user_info_change, True, (255, 255, 255))
    window.blit(text_surface_r_info, (100, 80))
    window.blit(text_surface_n_info, (100, 160))
    window.blit(text_surface_d_info, (100, 240))  # wyswietl
    window.blit(text_surface_eta_info, (100, 320))
    window.blit(text_surface_m_info, (100, 400))
    window.blit(text_surface_time_info, (100, 480))
    window.blit(text_surface_repeat_info, (100, 560))
    window.blit(text_surface_change_info, (100, 640))
    window.blit(text_surface_r, (user_input_rect_r.x + 5, user_input_rect_r.y + 5))  # wyświetl teksty (rownież te ktore użytkownik wprowadza) / text containery
    window.blit(text_surface_n, (user_input_rect_n.x + 5, user_input_rect_n.y + 5))
    window.blit(text_surface_d, (user_input_rect_d.x + 5, user_input_rect_d.y + 5))
    window.blit(text_surface_eta, (user_input_rect_eta.x + 5, user_input_rect_eta.y + 5))
    window.blit(text_surface_m, (user_input_rect_m.x + 5, user_input_rect_m.y + 5))
    window.blit(text_surface_time, (user_input_rect_time.x + 5, user_input_rect_time.y + 5))
    window.blit(text_surface_repeat, (user_input_rect_repeat.x + 5, user_input_rect_repeat.y + 5))
    window.blit(text_surface_change, (user_input_rect_change.x + 5, user_input_rect_change.y + 5))
    user_input_rect_r.w = max(40, text_surface_r.get_width() + 10)
    user_input_rect_n.w = max(40, text_surface_n.get_width() + 10)
    user_input_rect_d.w = max(40, text_surface_d.get_width() + 10) # ustaw szerokośc prostokatow
    user_input_rect_eta.w = max(40, text_surface_eta.get_width() + 10)
    user_input_rect_m.w = max(40, text_surface_m.get_width() + 10)
    user_input_rect_time.w = max(40, text_surface_time.get_width() + 10)
    user_input_rect_repeat.w = max(40, text_surface_repeat.get_width() + 10)
    user_input_rect_change.w = max(40, text_surface_change.get_width() + 10)
    window.blit(start_text, (975, 335))

    pygame.display.update() #odswieżenie