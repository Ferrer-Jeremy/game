import pygame

M_LEFT = 1
M_MIDDLE = 2
M_RIGHT = 3


def get_events(events):
    """
    Use a dict to stock the event
    Each value correspond to the number of frame continuous since the first event of this type
    Ex:  events[pygame.K_UP] == 3 --> the key UP is pressed continuously since 3 frames
    :param events: dict
    :return: dict
    """
    # For each frame we add 1 to the events still in progress
    for key, value in events.items():
        if value > 0:
            events[key] = value + 1

    # Iter events
    for e in pygame.event.get():
        # print(e)
        if e.type == pygame.QUIT:
            events[pygame.QUIT] = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            events[pygame.QUIT] = True

        # Keyboard single key
        if e.type == pygame.KEYDOWN and (e.key == pygame.K_UP or e.key == pygame.K_z):
            events[pygame.K_UP] = 1
        if e.type == pygame.KEYDOWN and (e.key == pygame.K_DOWN or e.key == pygame.K_s):
            events[pygame.K_DOWN] = 1
        if e.type == pygame.KEYDOWN and (e.key == pygame.K_RIGHT or e.key == pygame.K_d):
            events[pygame.K_RIGHT] = 1
        if e.type == pygame.KEYDOWN and (e.key == pygame.K_LEFT or e.key == pygame.K_q):
            events[pygame.K_LEFT] = 1

        if e.type == pygame.KEYUP and (e.key == pygame.K_UP or e.key == pygame.K_z):
            events[pygame.K_UP] = 0
        if e.type == pygame.KEYUP and (e.key == pygame.K_DOWN or e.key == pygame.K_s):
            events[pygame.K_DOWN] = 0
        if e.type == pygame.KEYUP and (e.key == pygame.K_RIGHT or e.key == pygame.K_d):
            events[pygame.K_RIGHT] = 0
        if e.type == pygame.KEYUP and (e.key == pygame.K_LEFT or e.key == pygame.K_q):
            events[pygame.K_LEFT] = 0

        # test buttons
        if e.type == pygame.KEYDOWN and (e.key == pygame.K_e):
            events[pygame.K_e] = 1
        if e.type == pygame.KEYUP and (e.key == pygame.K_e):
            events[pygame.K_e] = 0

        if e.type == pygame.KEYDOWN and (e.key == pygame.K_a):
            events[pygame.K_a] = 1
        if e.type == pygame.KEYUP and (e.key == pygame.K_a):
            events[pygame.K_a] = 0

        if e.type == pygame.KEYDOWN and (e.key == pygame.K_r):
            events[pygame.K_r] = 1
        if e.type == pygame.KEYUP and (e.key == pygame.K_r):
            events[pygame.K_r] = 0

        # Mouse
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == M_LEFT:
            events[M_LEFT] = 1

        if e.type == pygame.MOUSEBUTTONUP and e.button == M_LEFT:
            events[M_LEFT] = 0

    return events
