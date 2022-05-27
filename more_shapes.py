import pygame as p
class Shape1:
    def __init__(self, grid, screen):
        self.grid = grid
        self.sections = []
        self.index_x = 5
        (x, y) = self.grid[1][5]
        self.current_x = x
        self.current_y = y
        self.index_y = 1
        self.rotations = 0
        self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
        self.sections.append(p.Rect(self.current_x - 40, self.current_y-40, 40, 40))
        self.sections.append(p.Rect(self.current_x, self.current_y-40, 40, 40))
        self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
        for i in self.sections:
            p.draw.rect(screen, "green", i)
        for i in self.sections:
            p.draw.rect(screen, "gray", i, 1)
    def add_0(self):
        self.sections = []
        self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
        self.sections.append(p.Rect(self.current_x - 40, self.current_y - 40, 40, 40))
        self.sections.append(p.Rect(self.current_x, self.current_y - 40, 40, 40))
        self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
    def add_1(self):
        self.sections = []
        self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
        self.sections.append(p.Rect(self.current_x, self.current_y + 40, 40, 40))
        self.sections.append(p.Rect(self.current_x+40, self.current_y-40, 40, 40))
        self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
    def method(self):
        return "Shape1"

    def down(self,screen,z,other):
        x = self.move(screen,z)
        s = True
        if x != None:
            s = False
        if s:
            x = self.move(screen, z)


    def draw(self, screen):
        if self.rotations == 0:
            self.sections = []
            self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x - 40, self.current_y - 40, 40, 40))
            self.sections.append(p.Rect(self.current_x, self.current_y - 40, 40, 40))
            self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
            for i in self.sections:
                p.draw.rect(screen, "green", i)
            for i in self.sections:
                p.draw.rect(screen, "gray", i, 1)
        else:
            self.sections = []

            self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x, self.current_y + 40, 40, 40))
            self.sections.append(p.Rect(self.current_x + 40, self.current_y - 40, 40, 40))
            self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
            for i in self.sections:
                p.draw.rect(screen, "green", i)
            for i in self.sections:
                p.draw.rect(screen, "gray", i, 1)

    def move(self, screen, z):
        if self.rotations == 0:
            q = 13
        else:
            q =12
        if self.index_y <= q and z == False:
            self.index_y += 1
            (x, y) = self.grid[self.index_y][self.index_x]
            self.current_x = x
            self.current_y = y
            self.sections = []
            if self.rotations == 0:
                self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                self.sections.append(p.Rect(self.current_x - 40, self.current_y - 40, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y - 40, 40, 40))
                self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
            else:
                self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y + 40, 40, 40))
                self.sections.append(p.Rect(self.current_x + 40, self.current_y - 40, 40, 40))
                self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
            for i in self.sections:
                p.draw.rect(screen, "green", i)
            for i in self.sections:
                p.draw.rect(screen, "gray", i, 1)
        else:
            if self.rotations == 0:
                return ([(self.current_x, self.current_y, "green"), (self.current_x-40, self.current_y-40, "green"),
                         (self.current_x, self.current_y-40, "green"), (self.current_x + 40, self.current_y, "green")],
                        [(self.index_x, self.index_y), (self.index_x - 1, self.index_y-1),
                         (self.index_x, self.index_y-1), (self.index_x+1, self.index_y)])
            else:
                return ([(self.current_x, self.current_y, "green"), (self.current_x, self.current_y + 40, "green"),
                         (self.current_x+40, self.current_y - 40, "green"), (self.current_x+40, self.current_y, "green")],
                        [(self.index_x, self.index_y), (self.index_x, self.index_y + 1),
                         (self.index_x+1, self.index_y -1), (self.index_x+1, self.index_y)])

    def turn(self, screen):
        if self.rotations == 0:
            self.rotations = 1
        elif self.rotations == 1:
            self.rotations = 0
        if self.rotations == 0:
            self.sections = []

            self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x - 40, self.current_y - 40, 40, 40))
            self.sections.append(p.Rect(self.current_x, self.current_y - 40, 40, 40))
            self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
            for i in self.sections:
                p.draw.rect(screen, "green", i)
            for i in self.sections:
                p.draw.rect(screen, "gray", i, 1)
        else:
            self.sections = []

            self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x, self.current_y + 40, 40, 40))
            self.sections.append(p.Rect(self.current_x + 40, self.current_y - 40, 40, 40))
            self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
            for i in self.sections:
                p.draw.rect(screen, "red", i)
            for i in self.sections:
                p.draw.rect(screen, "gray", i, 1)

    def move_right(self, screen):
        if self.index_x < 11:
            self.index_x += 1
            (x, y) = self.grid[self.index_y][self.index_x]
            self.current_x = x
            self.current_y = y
            if self.rotations == 0:
                self.sections = []

                self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                self.sections.append(p.Rect(self.current_x - 40, self.current_y - 40, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y - 40, 40, 40))
                self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
                for i in self.sections:
                    p.draw.rect(screen, "green", i)
                for i in self.sections:
                    p.draw.rect(screen, "gray", i, 1)
            else:
                self.sections = []

                self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y + 40, 40, 40))
                self.sections.append(p.Rect(self.current_x + 40, self.current_y - 40, 40, 40))
                self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
                for i in self.sections:
                    p.draw.rect(screen, "green", i)
                for i in self.sections:
                    p.draw.rect(screen, "gray", i, 1)

    def move_left(self, screen):
        if self.index_x > 0:
            self.index_x -= 1
            (x, y) = self.grid[self.index_y][self.index_x]
            self.current_x = x
            self.current_y = y
            if self.rotations == 0:
                self.sections = []

                self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                self.sections.append(p.Rect(self.current_x - 40, self.current_y - 40, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y - 40, 40, 40))
                self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
                for i in self.sections:
                    p.draw.rect(screen, "green", i)
                for i in self.sections:
                    p.draw.rect(screen, "gray", i, 1)
            else:
                self.sections = []

                self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y + 40, 40, 40))
                self.sections.append(p.Rect(self.current_x + 40, self.current_y - 40, 40, 40))
                self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
                for i in self.sections:
                    p.draw.rect(screen, "green", i)
                for i in self.sections:
                    p.draw.rect(screen, "gray", i, 1)

    def check_collisions(self, other):
            if self.rotations == 0:
                for j in [(self.index_x, self.index_y), (self.index_x - 1, self.index_y-1),
                             (self.index_x, self.index_y-1), (self.index_x+1, self.index_y)]:
                    for i in other:
                        index_x = j[0]
                        index_y = j[1]
                        other_x = i[0]
                        other_y = i[1]
                        if other_x == index_x and other_y == index_y + 1:
                            return True
                return False
            else:
                for j in [(self.index_x, self.index_y), (self.index_x, self.index_y + 1),
                             (self.index_x+1, self.index_y -1), (self.index_x+1, self.index_y)]:
                    for i in other:
                        index_x = j[0]
                        index_y = j[1]
                        other_x = i[0]
                        other_y = i[1]
                        if other_x == index_x and other_y == index_y + 1:
                            return True
                return False