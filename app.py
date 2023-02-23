from screeninfo import get_monitors
import pygame 
import time
import os

monitors = get_monitors()
tm = time.time()
ww = monitors[0].width 
hh = monitors[0].height

pygame.init()

screen = pygame.display.set_mode([ww, hh], pygame.FULLSCREEN)

w, h = screen.get_size()

pygame.mouse.set_visible(False)

lock_img = pygame.image.load('./1.png')
lock_img = pygame.transform.scale(lock_img, (ww, hh))

# print("Locker is running !")

running = True
while running:
    if time.time() > tm + 7:
        screen.fill((0, 0, 0))
    else:
        screen.blit(lock_img, (0, 0))

    pygame.mouse.set_pos(ww - 100, hh - 100)
    # Did the user click the window close button?
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN or ((event.type == pygame.MOUSEMOTION) and (x != ww - 100) and (y != hh - 100)):
            tm = time.time()
        if event.type == pygame.QUIT:
            running = False
    # Flip the display
    pygame.display.flip()
    if pygame.mouse.get_focused() == 0:
        os.system('pmset displaysleepnow')
        # Done! Time to quit.
        pygame.quit()
        exit()
