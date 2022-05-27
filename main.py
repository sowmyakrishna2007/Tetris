import pygame as p
from shapes import Rectangle,Square
from more_shapes import Shape1
import random
import time

def setup():
    global screen, clock
    p.init()
    screen = p.display.set_mode((540, 730))
    clock = p.time.Clock()

def create_grid():
    global grid, screen
    grid = []
    y = 80
    for i in range(15):
        temp_list = []
        x = 50
        for i in range(11):
            temp_list.append((x, y))
            x += 40
        grid.append(temp_list)
        y += 40
    for i in grid:
        for j in i:
            p.draw.rect(screen, "black", (j[0], j[1], 40, 40))
            p.draw.rect(screen,"gray",(j[0],j[1],40,40),1)


def main():
    setup()
    create_grid()

    done = False
    z = False
    taken_points = []
    taken_indexes = []
    x = random.choice(["Square", "Shape", "Rectangle"])
    if x == "Square":
        r = Square(grid, screen)
    elif x == "Rectangle":
        r = Rectangle(grid, screen)
    elif x == "Shape":
        r = Shape1(grid, screen)
    font = p.font.SysFont('Arial Black', 30)
    text1 = font.render("Play Tetris!", True, 'white')
    screen.blit(text1, (170, 20))
    count = 0
    p.display.flip()
    screen.fill(p.Color("black"))
    while not done:
        screen.fill(p.Color('black'))
        create_grid()
        screen.blit(text1, (170, 20))

        for event in p.event.get():
            if event.type == p.QUIT:
                done = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:
                    r.move_left(screen)
                if event.key == p.K_RIGHT:
                    r.move_right(screen)
                if event.key == p.K_UP:
                    r.turn(screen)
                if event.key == p.K_DOWN:
                    r.down(screen,z,taken_indexes)
        z = r.check_collisions(taken_indexes)

        for (x,y) in taken_indexes:
            if y == 0:
                done = True
        if not done:
            if r.method() == "Rectangle" and r.rotations == 1:
                if r.index_y <= 10 and z == False:
                    if count % 15 == 0:
                        r.move(screen, z)
                    else:
                        r.draw(screen)
                elif r.index_y > 10 or z == True:
                    r.draw(screen)
                    x, y = r.move(screen, z)
                    taken_points.extend(x)
                    taken_indexes.extend(y)
                    x = random.choice(["Square","Shape","Rectangle"])
                    if x == "Square":
                        r = Square(grid,screen)
                    elif x == "Rectangle":
                        r = Rectangle(grid,screen)
                    elif x == "Shape":
                        r = Shape1(grid,screen)
                    count = 0

            elif r.method() == "Shape1" and r.rotations == 1:
                if r.index_y <= 12 and z == False:
                    if count % 15 == 0:
                        r.move(screen, z)
                    else:
                        r.draw(screen)
                elif r.index_y > 12 or z == True:
                    r.draw(screen)
                    x, y = r.move(screen, z)
                    taken_points.extend(x)
                    taken_indexes.extend(y)
                    x = random.choice(["Square", "Shape", "Rectangle"])
                    if x == "Square":
                        r = Square(grid, screen)
                    elif x == "Rectangle":
                        r = Rectangle(grid, screen)
                    elif x == "Shape":
                        r = Shape1(grid, screen)
                    count = 0
            else:
                if r.index_y <= 13 and z==False:

                    if count % 15 == 0:
                        r.move(screen,z)
                    else:
                        r.draw(screen)
                elif r.index_y > 13 or z==True:
                    r.draw(screen)
                    x,y = r.move(screen,z)
                    taken_points.extend(x)
                    taken_indexes.extend(y)
                    x = random.choice(["Square", "Shape", "Rectangle"])
                    if x == "Square":
                        r = Square(grid, screen)
                    elif x == "Rectangle":
                        r = Rectangle(grid, screen)
                    elif x == "Shape":
                        r = Shape1(grid, screen)
                    count = 0
            for i in taken_points:
                (x,y) = (i[0],i[1])
                color = i[2]
                p.draw.rect(screen,color,(x,y,40,40))
                p.draw.rect(screen,"gray",(x,y,40,40),1)

            for i in grid:
                new = [(i[0], i[1]) for i in taken_points]
                status = True
                l = []
                for j in i:
                    y = j[1]
                    if j not in new:
                        status = False
                    else:
                        l.append(j)
                if status:
                    for k in l:
                        p.draw.rect(screen,"yellow",(k[0],k[1],40,40))
                        p.display.flip()
                        t = new.index(k)
                        new.remove(k)
                        taken_points.remove(taken_points[t])
                        taken_indexes.remove(taken_indexes[t])
                    for (a,b,c) in taken_points:
                        if b < y:
                            q = taken_points.index((a,b,c))
                            taken_points[taken_points.index((a,b,c))] = (a,b+40,c)
                            (c,d) = taken_indexes[q]
                            taken_indexes[q] = (c,d+1)
                    time.sleep(1)
        count += 1
        p.display.flip()
        clock.tick(20)
    p.quit()


if __name__ == "__main__":
    main()