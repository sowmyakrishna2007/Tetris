import pygame as p
def draw_square(x,y,screen):
    p.draw.rect(screen,"red",(x,y,40,40))
class Rectangle:
        def __init__(self, grid, screen):
            self.grid = grid
            self.sections = []
            self.index_x = 5
            (x, y) = self.grid[0][5]
            self.current_x = x
            self.current_y = y
            self.index_y = 0
            self.rotations = 0
            self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x-80, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x - 40, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x+40, self.current_y, 40, 40))
            for i in self.sections:
                p.draw.rect(screen, "red", i)
            for i in self.sections:
                p.draw.rect(screen, "gray", i, 1)
        def method(self):
            return "Rectangle"

        def down(self, screen, z, other):
            i = self.check_collisions(other)
            if i:
                pass
            else:
                for i in range(2):
                    x = self.move(screen, z)
                    if x != None:
                        break
        def draw(self, screen):
            if self.rotations == 0:
                self.sections = []
                self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                self.sections.append(p.Rect(self.current_x - 80, self.current_y, 40, 40))
                self.sections.append(p.Rect(self.current_x - 40, self.current_y, 40, 40))
                self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
                for i in self.sections:
                    p.draw.rect(screen, "red", i)
                for i in self.sections:
                    p.draw.rect(screen, "gray", i, 1)
            else:
                self.sections = []

                self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y + 40, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y + 80, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y + 120, 40, 40))
                for i in self.sections:
                    p.draw.rect(screen, "red", i)
                for i in self.sections:
                    p.draw.rect(screen, "gray", i, 1)

        def move(self, screen, z):
            if self.rotations == 1:
                q = 10
            else:
                q = 13
            if self.index_y <= q and z == False:
                self.index_y += 1
                (x, y) = self.grid[self.index_y][self.index_x]
                self.current_x = x
                self.current_y = y
                self.sections = []
                if self.rotations == 0:
                    self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x - 80, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x - 40, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
                else:
                    self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x, self.current_y + 40, 40, 40))
                    self.sections.append(p.Rect(self.current_x, self.current_y + 80, 40, 40))
                    self.sections.append(p.Rect(self.current_x, self.current_y + 120, 40, 40))
                for i in self.sections:
                    p.draw.rect(screen, "red", i)
                for i in self.sections:
                    p.draw.rect(screen, "gray", i, 1)
            else:
                if self.rotations == 0:
                    return ([(self.current_x, self.current_y, "red"), (self.current_x - 40, self.current_y, "red"),
                             (self.current_x - 80, self.current_y, "red"), (self.current_x+40, self.current_y, "red")],
                            [(self.index_x, self.index_y), (self.index_x - 1, self.index_y),
                             (self.index_x + 1, self.index_y), (self.index_x-2, self.index_y)])
                else:
                    return ([(self.current_x, self.current_y, "red"), (self.current_x, self.current_y+40, "red"),
                             (self.current_x, self.current_y+80, "red"), (self.current_x, self.current_y+120, "red")],
                            [(self.index_x, self.index_y), (self.index_x, self.index_y+1),
                            (self.index_x, self.index_y+2), (self.index_x, self.index_y+3)])

        def turn(self,screen):
            if self.rotations == 0:
                self.rotations = 1
            elif self.rotations == 1:
                self.rotations = 0
            if self.rotations == 0:
                    self.sections = []

                    self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x - 80, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x - 40, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
                    for i in self.sections:
                        p.draw.rect(screen, "red", i)
                    for i in self.sections:
                        p.draw.rect(screen, "gray", i, 1)
            else:
                self.sections = []

                self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y+40, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y+80, 40, 40))
                self.sections.append(p.Rect(self.current_x, self.current_y+120, 40, 40))
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
                    self.sections.append(p.Rect(self.current_x - 80, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x - 40, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
                    for i in self.sections:
                        p.draw.rect(screen, "red", i)
                    for i in self.sections:
                        p.draw.rect(screen, "gray", i, 1)
                else:
                    self.sections = []

                    self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x, self.current_y + 40, 40, 40))
                    self.sections.append(p.Rect(self.current_x, self.current_y + 80, 40, 40))
                    self.sections.append(p.Rect(self.current_x, self.current_y + 120, 40, 40))
                    for i in self.sections:
                        p.draw.rect(screen, "red", i)
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
                    self.sections.append(p.Rect(self.current_x - 80, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x - 40, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x + 40, self.current_y, 40, 40))
                    for i in self.sections:
                        p.draw.rect(screen, "red", i)
                    for i in self.sections:
                        p.draw.rect(screen, "gray", i, 1)
                else:
                    self.sections = []

                    self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
                    self.sections.append(p.Rect(self.current_x, self.current_y + 40, 40, 40))
                    self.sections.append(p.Rect(self.current_x, self.current_y + 80, 40, 40))
                    self.sections.append(p.Rect(self.current_x, self.current_y + 120, 40, 40))
                    for i in self.sections:
                        p.draw.rect(screen, "red", i)
                    for i in self.sections:
                        p.draw.rect(screen, "gray", i, 1)
        def check_collisions(self,other):
            if self.rotations == 0:
                for j in [(self.index_x, self.index_y), (self.index_x - 1, self.index_y),
                             (self.index_x + 1, self.index_y), (self.index_x-2, self.index_y)]:
                    for i in other:
                        index_x = j[0]
                        index_y = j[1]
                        other_x = i[0]
                        other_y = i[1]
                        if other_x == index_x and other_y == index_y + 1:
                            return True
                return False
            else:
                for j in [(self.index_x, self.index_y), (self.index_x, self.index_y+1),
                            (self.index_x, self.index_y+2), (self.index_x, self.index_y+3)]:
                    for i in other:
                        index_x = j[0]
                        index_y = j[1]
                        other_x = i[0]
                        other_y = i[1]
                        if other_x == index_x and other_y == index_y + 1:
                            return True
                return False

class Square:
    def __init__(self,grid,screen):
        self.grid = grid
        self.sections = []
        self.index_x = 5
        (x,y) = self.grid[1][5]
        self.current_x=x
        self.current_y=y
        self.index_y = 1
        self.sections.append(p.Rect(self.current_x - 40, self.current_y, 40, 40))
        self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
        self.sections.append(p.Rect(self.current_x - 40, self.current_y - 40, 40, 40))
        self.sections.append(p.Rect(self.current_x, self.current_y - 40, 40, 40))
        for i in self.sections:
            p.draw.rect(screen,"blue",i)
        for i in self.sections:
            p.draw.rect(screen,"gray",i,1)
    def method(self):
        return "Square"
    def down(self,screen,z,other):
        k = False
        for j in [(self.index_x, self.index_y), (self.index_x - 1, self.index_y - 1), (self.index_x - 1, self.index_y),
         (self.index_x, self.index_y - 1)]:
            for i in other:
                index_x = j[0]
                index_y = j[1]
                other_x = i[0]
                other_y = i[1]
                if other_x == index_x and other_y == index_y + 2:
                    k = True

        if k:
            pass
        else:
            self.move(screen, z)
            k = False
            for j in [(self.index_x, self.index_y), (self.index_x - 1, self.index_y - 1),
                      (self.index_x - 1, self.index_y),
                      (self.index_x, self.index_y - 1)]:
                for i in other:
                    index_x = j[0]
                    index_y = j[1]
                    other_x = i[0]
                    other_y = i[1]
                    if other_x == index_x and other_y == index_y + 2:
                        k = True
            if k:
                pass
            else:
                self.move(screen, z)

    def draw(self,screen):
        for i in self.sections:
            p.draw.rect(screen,"blue",i)
        for i in self.sections:
            p.draw.rect(screen,"gray",i,1)
    def move(self,screen,z):

        if self.index_y <= 13 and z == False:
            self.index_y += 1
            (x, y) = self.grid[self.index_y][self.index_x]
            self.current_x = x
            self.current_y = y
            self.sections = []
            self.sections.append(p.Rect(self.current_x - 40, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x - 40, self.current_y - 40, 40, 40))
            self.sections.append(p.Rect(self.current_x, self.current_y - 40, 40, 40))
            for i in self.sections:
                p.draw.rect(screen,"blue",i)
            for i in self.sections:
                p.draw.rect(screen,"gray",i,1)
        else:
            return ([(self.current_x,self.current_y,"blue"),(self.current_x-40,self.current_y-40,"blue"),(self.current_x-40,self.current_y,"blue"),(self.current_x,self.current_y-40,"blue")],
                    [(self.index_x,self.index_y),(self.index_x-1,self.index_y-1),(self.index_x-1,self.index_y),(self.index_x,self.index_y-1)])
    def move_right(self,screen):
        if self.index_x < 11:
            self.index_x += 1
            (x, y) = self.grid[self.index_y][self.index_x]
            self.current_x = x
            self.current_y = y
            self.sections = []
            self.sections.append(p.Rect(self.current_x - 40, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x - 40, self.current_y - 40, 40, 40))
            self.sections.append(p.Rect(self.current_x, self.current_y - 40, 40, 40))
            for i in self.sections:
                p.draw.rect(screen, "blue", i)
            for i in self.sections:
                p.draw.rect(screen, "gray", i, 1)

    def move_left(self,screen):
        if self.index_x > 0:
            self.index_x -= 1
            (x, y) = self.grid[self.index_y][self.index_x]
            self.current_x = x
            self.current_y = y
            self.sections = []
            self.sections.append(p.Rect(self.current_x - 40, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x, self.current_y, 40, 40))
            self.sections.append(p.Rect(self.current_x - 40, self.current_y - 40, 40, 40))
            self.sections.append(p.Rect(self.current_x, self.current_y - 40, 40, 40))
            for i in self.sections:
                p.draw.rect(screen, "blue", i)
            for i in self.sections:
                p.draw.rect(screen, "gray", i, 1)

    def check_collisions(self, other):
        for j in [(self.index_x, self.index_y), (self.index_x - 1, self.index_y - 1), (self.index_x - 1, self.index_y),
         (self.index_x, self.index_y - 1)]:
            for i in other:
                index_x = j[0]
                index_y = j[1]
                other_x = i[0]
                other_y = i[1]
                if other_x == index_x and other_y == index_y + 1:
                    return True
        return False
    def turn(self, screen):
        pass
