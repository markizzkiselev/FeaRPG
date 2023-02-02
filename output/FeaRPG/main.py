from sprite_classes import *
from board_class import *
from sprite_lists import *


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('FeaRPG')

    screen = pygame.display.set_mode(DIMENSIONS)

    board = Board(DIMENSIONS, screen)

    pygame.mixer.music.load("Music/blocks.mp3")
    pygame.mixer.music.play(-1)

    w_pressed = False
    s_pressed = False
    d_pressed = False
    a_pressed = False
    c_pressed = False

    ANIMATION = pygame.USEREVENT + 1
    pygame.time.set_timer(ANIMATION, 100)
    WAIT = pygame.USEREVENT + 2
    pygame.time.set_timer(WAIT, 5000)

    filedark = resizer('Sprites/dark.png', DIMENSIONS[0], DIMENSIONS[1], 'new_dark')
    dark = Dark(filedark, dark_list)
    inventory = Inventory(all_sprites_list)
    dad = Dad(all_sprites_list)
    question = Question(question_list)
    c_button = Button_C(question_list)
    zero_button = Button_0(all_sprites_list)
    filestartscreen = resizer('Sprites/main.png', DIMENSIONS[1],
                              DIMENSIONS[1], 'new_startscreen')
    startscreen_list = pygame.sprite.Group()
    startscreen = StartScreen(filestartscreen, startscreen_list)
    endscreen_list = pygame.sprite.Group()

    state = 0

    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    pygame.display.flip()
    pygame.display.update()
    while running:
        if state == 0:
            for event in pygame.event.get():
                if event.type == WAIT:
                    state = 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            screen.fill((0, 0, 0))
            startscreen_list.draw(screen)
            pygame.display.flip()
            pygame.display.update()
        if state == 1:
            dad.run = True
            board.draw_map()
            if w_pressed and d_pressed:
                board.up_and_right()
                dad.right()
            elif s_pressed and d_pressed:
                board.down_and_right()
                dad.right()
            elif w_pressed and a_pressed:
                board.up_and_left()
                dad.left()
            elif s_pressed and a_pressed:
                board.down_and_left()
                dad.left()
            elif w_pressed and s_pressed:
                pass
            elif a_pressed and d_pressed:
                pass
            elif w_pressed:
                board.up()
            elif s_pressed:
                board.down()
            elif d_pressed:
                dad.right()
                board.right()
            elif a_pressed:
                dad.left()
                board.left()
            else:
                dad.run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == ANIMATION:
                    dad.anim()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        w_pressed = True
                    if event.key == pygame.K_s:
                        s_pressed = True
                    if event.key == pygame.K_d:
                        d_pressed = True
                    if event.key == pygame.K_a:
                        a_pressed = True
                    if event.key == pygame.K_c:
                        c_pressed = True
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        w_pressed = False
                    if event.key == pygame.K_s:
                        s_pressed = False
                    if event.key == pygame.K_d:
                        d_pressed = False
                    if event.key == pygame.K_a:
                        a_pressed = False
                    if event.key == pygame.K_c:
                        c_pressed = False

            dark_list.draw(screen)

            if board.is_find():
                question_list.draw(screen)
                if c_pressed:
                    board.open()

            board.inventory_list.draw(screen)
            all_sprites_list.draw(screen)
            board.draw_text()
            pygame.display.flip()
            pygame.display.update()
            if board.end:
                state = 2
        if state == 2:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        board = Board(DIMENSIONS, screen)
                        state = 0
            screen.fill((0, 0, 0))
            font1 = pygame.font.Font('Fonts/FearFont.ttf', 96)
            text1 = font1.render(f"Thanks for passing!",
                                 True, (255, 255, 255))
            screen.blit(text1,
                        (DIMENSIONS[0] // 2 - text1.get_width() // 2,
                         DIMENSIONS[1] // 2 - text1.get_height() // 2))
            endscreen_list.draw(screen)
            pygame.display.flip()
            pygame.display.update()

