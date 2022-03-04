import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    x_pos = 0
    running = True
    v = 20  # пикселей в секунду
    clock = pygame.time.Clock()
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
        x_pos += v * clock.tick() / 1000  # v * t в секундах


        # обновление экрана
        pygame.display.flip()
    pygame.quit()