

def collision_for_rect(bool_position):
    if bool_position:
        return True
    else:
        return False


def write_or_delete_in_text_container(input, key, unicode):
    import pygame
    pygame.init()
    if key == pygame.K_BACKSPACE:
        input = input[:-1]
    else:
        input += unicode
    return input


def is_active(active):
    from main import color_input_active
    from main import color_input_passive
    if active:
        return color_input_active
    else:
        return color_input_passive

    
def distance(x1, y1, x2, y2):
    import math
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
