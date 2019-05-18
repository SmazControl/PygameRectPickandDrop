"""
Pygame Pick'n'Drop Example
base from code
Pygame Drag'n'Drop Example
http://old.bytemuehle.de/Drag%20and%20Drop/

"""

import pygame
import pygame.locals as loc


def main():
    # standard init stuff
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption("pygame drag'n'drop example - by jug")
    clock = pygame.time.Clock()

    # create a rect as simple object to drag'n'drop
    rect = pygame.Rect(10,10,50,50)

    # in this variable we will save the offset from the topleft of our rect
    # to the mouse pointer
    offset = None
    onclick = False
    # start the mainloop
    while 1:
        # limit fps to 40
        clock.tick(40)

        # handle events
        for event in pygame.event.get():
            # standard events to exit the program
            if event.type == loc.QUIT:
                return
            elif event.type == loc.KEYDOWN:
                if event.key == loc.K_ESCAPE:
                    return
            # if a button is pressed above the rect,
            # save the offset and start dragging
            elif (event.type == loc.MOUSEBUTTONDOWN
                  and rect.collidepoint(event.pos)):
                if onclick:
                    onclick = False
                    offset = None
                else:
                    onclick = True
                    mouse_x, mouse_y = event.pos
                    my_x, my_y = rect.topleft
                    offset = mouse_x - my_x, mouse_y - my_y
        # if we have an offset, ie if we are dragging, calculate the new
        # position with the current mouse position and our offset
        if offset:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            off_x, off_y = offset
            rect.topleft = mouse_x - off_x, mouse_y - off_y

        # fill the screen, draw the rect and flip it
        screen.fill((200,200,200))
        screen.fill((0,0,0), rect)
        pygame.display.flip()

if __name__ == '__main__': main()
