import pygame
import datetime


class PygameWindow:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 500, 500
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Voice Assistant")
        self.font = pygame.font.SysFont("courier", 12)
        self.clock = pygame.time.Clock()
        self.running = True
        self.output_label = ""
        self.input_label = ""
        self.bg_color = (255, 255, 255)
        self.text_color = (0, 0, 0)

    def render_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.text_color)
        self.screen.blit(text_surface, (x, y))

    def update_output_label(self, text):
        self.output_label = f"{text} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    def update_input_label(self, text):
        self.input_label = f"{text} - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(self.bg_color)
            self.render_text(self.output_label, 10, 50)
            self.render_text(self.input_label, 10, 100)
            pygame.display.flip()

            self.clock.tick(30)

        pygame.quit()
