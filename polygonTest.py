import polygon, pygame, sys

pygame.init()

screen = pygame.display.set_mode((640, 640))

polygon1 = polygon.Polygon([[400, 130], [200, 100], [240, 240], [360, 300]])
polygon1color = (255, 255, 255)

polygon2 = polygon.Polygon([[0, 0], [50, 10], [40, 30], [10, 40]])

pygame.mouse.set_visible(False)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    polygon1.draw(screen, polygon1color)
    polygon2.draw(screen, (0, 0, 255))

    for index, point in enumerate(polygon2.points):
        if index == 0:
            point.x = 0 + pygame.mouse.get_pos()[0]
            point.y = 0 + pygame.mouse.get_pos()[1]
        elif index == 1:
            point.x = 50 + pygame.mouse.get_pos()[0]
            point.y = 10 + pygame.mouse.get_pos()[1]
        elif index == 2:
            point.x = 40 + pygame.mouse.get_pos()[0]
            point.y = 30 + pygame.mouse.get_pos()[1]
        elif index == 3:
            point.x = 10 + pygame.mouse.get_pos()[0]
            point.y = 40 + pygame.mouse.get_pos()[1]

    if polygon1.collidepoly(polygon2):
        polygon1color = (255, 0, 0)
    else:
        polygon1color = (255, 255, 255)
    pygame.display.update()
