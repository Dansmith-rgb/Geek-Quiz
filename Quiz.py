__author__ = 'thynan'
import pygame
from random import randint
from pygame.locals import QUIT, MOUSEBUTTONDOWN, K_LEFT, K_RIGHT

pygame.init()
screen = pygame.display.set_mode( (800, 600), 0, 32)
X = 0
def Win():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    winner = pygame.image.load("./fim.jpg").convert_alpha()
    voltar = pygame.Rect(500, 508, 214, 43)
    while (True):
        pygame.draw.rect(screen, [136,136,136], voltar)
        screen.blit(winner, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if voltar.collidepoint(mouse_pos):
                    Menu()
def erro():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    errou = pygame.image.load("./erro.jpg").convert_alpha()
    voltar = pygame.Rect(450, 425, 285, 75)
    while (True):
        pygame.draw.rect(screen, [136,136,136], voltar)
        screen.blit(errou, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if voltar.collidepoint(mouse_pos):
                    Menu()
def wait(segundos):

    import msvcrt
    import time

    start = time.time()

    while True:
        if msvcrt.kbhit():
            msvcrt.getch()
            break
        if time.time() - start > segundos:
            break

        time.sleep(0.2)
def Q30():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q30.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    Win()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q29():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q29.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    Q30()
def Q28():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q28.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    Q29()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q27():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q27.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    Q28()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q26():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q26.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    Q27()
def Q25():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q25.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    Q26()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q24():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q24.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    Q25()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q23():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q23.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    Q24()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q22():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q22.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    A5 = pygame.Rect(763, 574, 17, 11)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        pygame.draw.rect(screen, [136,136,136], A5)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
                if A5.collidepoint(mouse_pos):
                    Q23()
def Q21():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q21.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    Q22()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q20():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q20.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    Q21()
def Q19():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q19.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    A5 = pygame.Rect(474, 109, 274, 26)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        pygame.draw.rect(screen, [136,136,136], A5)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
                if A5.collidepoint(mouse_pos):
                    Q20()
def Q18():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q18.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    Q19()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q17():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q17.jpg").convert_alpha()
    fle = pygame.image.load("./flecha.png").convert_alpha()
    b1 = pygame.Rect(151, 195, 449, 24)
    b2 = pygame.Rect(418, 243, 382, 24)
    b3 = pygame.Rect(0, 282, 206, 26)
    b4 = pygame.Rect(401, 302, 392, 35)
    b5 = pygame.Rect(138, 357, 226, 24)
    b6 = pygame.Rect(224, 428, 274, 33)
    b7 = pygame.Rect(601, 416, 199, 39)
    b8 = pygame.Rect(151, 482, 313, 30)
    b9 = pygame.Rect(541, 493, 259, 23)
    b10 = pygame.Rect(0, 339, 129, 19)
    b11 = pygame.Rect(116, 406, 85, 66)
    x = 100
    y = 100
    pygame.mouse.set_pos(650,130)
    while (True):
        pygame.draw.rect(screen, [136,136,136], b1)
        pygame.draw.rect(screen, [136,136,136], b2)
        pygame.draw.rect(screen, [136,136,136], b3)
        pygame.draw.rect(screen, [136,136,136], b4)
        pygame.draw.rect(screen, [136,136,136], b5)
        pygame.draw.rect(screen, [136,136,136], b6)
        pygame.draw.rect(screen, [136,136,136], b7)
        pygame.draw.rect(screen, [136,136,136], b8)
        pygame.draw.rect(screen, [136,136,136], b9)
        pygame.draw.rect(screen, [136,136,136], b10)
        pygame.draw.rect(screen, [136,136,136], b11)
        screen.blit(qu1, (0,0))
        screen.blit(fle, (x-50,y-10))
        (x, y) = pygame.mouse.get_pos()
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if b1.collidepoint(x,y):
                    erro()
            if b2.collidepoint(x,y):
                    erro()
            if b3.collidepoint(x,y):
                    erro()
            if b4.collidepoint(x,y):
                    erro()
            if b5.collidepoint(x,y):
                    erro()
            if b6.collidepoint(x,y):
                    erro()
            if b7.collidepoint(x,y):
                    erro()
            if b8.collidepoint(x,y):
                    erro()
            if b9.collidepoint(x,y):
                    erro()
            if b10.collidepoint(x,y):
                    erro()
            if b11.collidepoint(x,y):
                    Q18()
def Q16():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q16.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    Q17()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q15():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q15.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    A5 = pygame.Rect(596, 573, 124, 20)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        pygame.draw.rect(screen, [136,136,136], A5)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
                if A5.collidepoint(mouse_pos):
                    Q16()
def Q14():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q14.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    Q15()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q13():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q13.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    Q14()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q12():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q12.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    A5 = pygame.Rect(742, 569, 26, 20)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        pygame.draw.rect(screen, [136,136,136], A5)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
                if A5.collidepoint(mouse_pos):
                        Q13()
def Q11():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q11.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    Q12()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q10():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q10.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    Q11()
def Q9():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q9.jpg").convert_alpha()
    fla = pygame.image.load("./flash.png").convert_alpha()
    cap = pygame.image.load("./frio.png").convert_alpha()
    gelo = pygame.image.load("./ice.png").convert_alpha()
    x = 100
    y = 100
    while (True):
        screen.blit(qu1, (0, 0))
        screen.blit(cap, (365, 0))
        screen.blit(gelo, (x-40,y-20))
        (x, y) = pygame.mouse.get_pos()

        #flash()
        x1 = 0
        y1 = 300
        su = randint (50, 600)
        if int(su) % 5 == 0:
            x2 = x1 + su
            A1 = pygame.Rect(x2, y1, 70, 100)
            pygame.draw.rect(screen, [0,0,0], A1)
            if int(x2) % 3 == 0:
                if int(x2) % 2 == 0:
                    screen.blit(fla, (x2,y1))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    wait(segundos=1)
                    Q10()
def Q8():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q8.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    Q9()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q7():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q7.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    Q8()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q6():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q6.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    Q7()
def Q5():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q5.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    Q6()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q4():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q4.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    Q2()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    Q5()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q3():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q3.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    Q4()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
def Q2():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q2.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    A5 = pygame.Rect(768, 569, 13, 20)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        pygame.draw.rect(screen, [136,136,136], A5)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    erro()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()
                if A5.collidepoint(mouse_pos):
                    Q3()
def Q1():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    qu1 = pygame.image.load("./q1.jpg").convert_alpha()
    A1 = pygame.Rect(151, 291, 216, 70)
    A2 = pygame.Rect(463, 291, 216, 70)
    A3 = pygame.Rect(151, 428, 216, 70)
    A4 = pygame.Rect(463, 428, 216, 70)
    while (True):
        pygame.draw.rect(screen, [136,136,136], A1)
        pygame.draw.rect(screen, [136,136,136], A2)
        pygame.draw.rect(screen, [136,136,136], A3)
        pygame.draw.rect(screen, [136,136,136], A4)
        screen.blit(qu1, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if A1.collidepoint(mouse_pos):
                    Q2()
                if A2.collidepoint(mouse_pos):
                    erro()
                if A3.collidepoint(mouse_pos):
                    erro()
                if A4.collidepoint(mouse_pos):
                    erro()

def Menu():
    global screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (800, 600), 0, 32)
    Men = pygame.image.load("./3.jpg").convert_alpha()
    Bplay = pygame.Rect(284, 370, 232, 65)
    Bquit = pygame.Rect(296, 459, 171, 50)
    while (True):
        pygame.draw.rect(screen, [136,136,136], Bplay)
        pygame.draw.rect(screen, [136,136,136], Bquit)
        screen.blit(Men, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if Bquit.collidepoint(mouse_pos):
                    exit()
                if Bplay.collidepoint(mouse_pos):
                    X = 1
                    Q1()

while(True):
    for e in pygame.event.get():
        if (e.type == QUIT):
            exit()
        if X == 0 :
            Menu()

