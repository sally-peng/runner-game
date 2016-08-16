import pygame
import random


class Building():
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width   = width
        self.height  = height
        self.color   = color

    def draw(self, screen):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])

    def move(self, speed):

        self.x_point -= speed



class Scroller(object):

    def __init__(self, width, height, base, color, speed):
        self.width  = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.buildings = []
        self.add_buildings() # Add builings each time a new instance is created

    def add_buildings(self):
        """
        Will add a randomly generated building that fits within the width and height
        of the scroller
        """
        current_width = 0 # How wide the scroller is right now
        while current_width <= self.width:
            self.add_building(current_width)
            current_width += self.buildings[-1].width
            self.scroll_end = current_width

    def add_building(self, x_location):
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
        """
        # The building width will be a random integer between 1/20th and 1/4th of the width
        building_width = random.randint((self.width // 20), (self.width // 4))

        max_height = self.base - self.height # this sets the maximum height each building can be

        # The building width will be a random integer between 1/4th and just under the max_height
        building_height = random.randint((max_height // 4), (max_height - 1))

        y_location = self.base - building_height # This tells the building where along the y-axis to draw itself

        self.buildings.append(Building(x_location, y_location, building_width, building_height, self.color))

    def draw_buildings(self, screen):
        """
        This calls the draw method on each building.
        """
        for building in self.buildings:
            building.draw(screen)

    def move_buildings(self):
        for building in self.buildings:
            building.move(self.speed)
            if building.x_point + building.width <= 0:
                self.buildings.remove(building)

        #gets the x_point of the last building and adds it's width to place the new building right next to it.
        new_building_location = self.buildings[-1].x_point + self.buildings[-1].width
        if new_building_location <= self.width:
            self.add_building(new_building_location)