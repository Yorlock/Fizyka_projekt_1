
class Plot: #  wykres

    def __init__(self, size_x, size_y, dpi_u, face_color, patch_color, data_x, data_y):  # stworz wykres
        import pylab
        fig = pylab.figure(figsize=[size_x, size_y], dpi=dpi_u)
        ax = fig.gca()
        ax.set_facecolor(face_color)
        fig.patch.set_facecolor(patch_color)
        ax.plot(data_x, data_y)
        self.fig = fig
        self.ax = ax

    def update_plot(self, data_x, data_y, plot): #  aktualizacja wykresu
        import matplotlib.backends.backend_agg as agg
        import pygame
        plot.ax.plot(data_x, data_y)
        canvas = agg.FigureCanvasAgg(plot.fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        return surf



class Atom:  # stworz kulke
    def __init__(self, r, color, right, down, up, left, atoms, rgb):
        import random
        import math
        self.m = 1
        self.r = r
        self.color = color
        self.rgb = rgb
        if color is 'red':
            self.x = left + r + 2
            self.y = up + r + 2
        else:
            is_fine = False
            helper_x = 0
            helper_y = 0
            while not is_fine:
                repeat_loop = False
                helper_x = random.randint(left + r + 1, right - r - 1)
                helper_y = random.randint(up + r + 1, down - r - 1)
                for atom in atoms:
                    if not math.sqrt(abs(atom.x - helper_x)**2 + abs(atom.y - helper_y)**2) > 2 * r:
                        repeat_loop = True
                        break
                if not repeat_loop:
                    break
            self.x = helper_x
            self.y = helper_y
        self.x_speed = random.randint(-5, 5)
        self.y_speed = random.randint(-5, 5)
        while self.x_speed == 0 and self.y_speed == 0:
            self.x_speed = random.randint(-5, 5)
            self.y_speed = random.randint(-5, 5)

    def drawing_circle(self, where, atom): #  narysuj kulkę
        import pygame
        pygame.init()
        pygame.draw.circle(where, atom.rgb, (atom.x, atom.y), atom.r)
