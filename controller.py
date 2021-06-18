import pygame

class Collision:
    '''
        Collision class
            implements functions relevant to collision checking
    '''
    pass

class KeyEvents:
    '''
        KeyEvents class
            implements functions relevant to key events
    '''
    def check_events():
        ''' A controller of sorts.  Looks for Quit, several simple events.
            Returns: True/False for if a Quit event happened.
        '''
        quit = False
        up = down = left = right = False
        up_up = down_up = left_up = right_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit = True
                if event.key == pygame.K_ESCAPE:
                    quit = True
                if event.key == pygame.K_w:
                    up = True
                if event.key == pygame.K_s:
                    down = True
                if event.key == pygame.K_a:
                    left = True
                if event.key == pygame.K_d:
                    right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    up_up = True
                if event.key == pygame.K_s:
                    down_up = True
                if event.key == pygame.K_a:
                    left_up = True
                if event.key == pygame.K_d:
                    right_up = True
        return quit, up, down, left, right, up_up, down_up, left_up, right_up
