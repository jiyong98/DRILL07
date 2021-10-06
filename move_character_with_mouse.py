from pico2d import *
from random import randint
KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    # fill here
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


# fill here
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
handDraw = True
handx = randint(0, KPU_WIDTH - 1)
handy = randint(0, KPU_HEIGHT - 1)
rad = 1
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if handDraw:
        hand.draw(handx, handy)

    character.clip_draw(frame * 100, 100 * rad, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    if x <= handx:
        x += 5
        rad = 1
    if y <= handy:
        y += 5
    if x >= handx:
        rad = 0
        x -= 5
    if y >= handy:
        y -= 5

    delay(0.01)

    handle_events()

close_canvas()




