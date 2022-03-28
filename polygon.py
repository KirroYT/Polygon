import pygame, sys
from pygame.math import Vector2 as Vector2

class Polygon():
    def __init__(self, points):
        self.points = []
        for point in points:
            self.points.append(Vector2(point[0], point[1]))
    def collidepoint(self, point):
        collision = False
        nextV = 0
        for current in range(len(self.points)):
            nextV = current + 1
            
            if nextV == len(self.points):
                nextV = 0

            VertexC = self.points[current]
            VertexN = self.points[nextV]

            if (((VertexC.y >= point.y and VertexN.y < point.y) or (VertexC.y < point.y and VertexN.y >= point.y)) and (point.x < (VertexN.x - VertexC.x) * (point.y - VertexC.y) / (VertexN.y - VertexC.y) + VertexC.x)):
                collision = not(collision)
        return collision
    def collidepoly(self, poly):
        collisions = []
        for point in poly.points:
            collisions.append(self.collidepoint(point))
        for point in self.points:
            collisions.append(poly.collidepoint(point))
        return any(collisions)
    def draw(self, screen, color):
        pygame.draw.polygon(screen, color, self.points)
