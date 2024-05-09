import pygame
import random
from pygame import *
from pygame.locals import *

WIDTH, HEIGHT = 800, 700
MAP_SIZE = 30
ROWS, COLS = 21,10
#FPS = 60

mixer.init()
pygame.mixer.music.load('music_efects/menu_music.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.3)
remove_row_music = pygame.mixer.Sound('music_efects/remove_row.mp3')
congratulations_music = pygame.mixer.Sound('music_efects/congratulations.mp3')
game_over_music = pygame.mixer.Sound('music_efects/game_over.mp3')
game_over_music.set_volume(0.4)
congratulations_music.set_volume(0.4)
#win_music = pygame.mixer.music.load("music_efects/window_music.mp3")

GRAY = (128, 128, 128) 
SADDLE_BROWN = (139,69,19) 

#текст
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#блоки
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GOLDENROD  = (218,165,32)
DARK_GOLDENROD = (184,134,11)
LIMEGREEN = (50,205,50)
DARKGREEN = (0,100,0)
YELLOW = (255,255,0)
BLUEVIOLET = (138,43,226)
ORANGERED = (255,69,0)
MIDNIGHTBLUE = (25,25,112)
SILVER = (192,192,192)


frame = image.load('images/pngwing.com.png')
#btn_menu= image.load('images/free-icon-menu-5949637.png')
bg_game = image.load('images/Wall 800 x 800, 6c24e0ce-9a4f-40e0-9ed7-abbb6b5e453b.png')
control_settings_bg = image.load('images/control_settings_bg.png')
#row_anim = image.load('images\abstract-surface-and-textures-of-white-concrete-stone-wall.jpg')

blur = pygame.Surface((WIDTH, HEIGHT))
frame_blur = pygame.transform.smoothscale(frame, (WIDTH // 10, HEIGHT // 10))
frame_blur = pygame.transform.smoothscale(frame_blur, (WIDTH, HEIGHT))

# file = open("results", "r")
# init_best_result = int(file.readline())
# file.close()
# best_result = init_best_result
# file = open("results", "r")
# init_best_result = int(file.readline())
# file.close()

class Images(sprite.Sprite):
    def __init__(self, filename, x, y, speed, w, h):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
    def reset(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Sprite(sprite.Sprite): #назва класу
    def __init__(self,sprite_img,width,height,x,y): #властивості 
        super().__init__()
        self.image = transform.scale(sprite_img,(width,height)) #розширення спрайтів
        self.rect = self.image.get_rect() #отримання значення
        self.rect.x = x #присвоєння значення x
        self.rect.y = y #присвоєння значення y

    
class Button:
    def __init__(self, text, x, y, width, height, text_color, font_size):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_color = text_color
        self.font_size = font_size

    def reset(self, window):
        #pygame.draw.rect(window, self.text_color, [self.x, self.y, self.width, self.height])
        font = pygame.font.Font('fonts/arcade.TTF', self.font_size)
        text_render = font.render(self.text, True, self.text_color)
        text_rect = text_render.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        window.blit(text_render, text_rect)
        
class Title(Button):
    def __init__(self, text, x, y, width, height, text_color, font_size):
        super().__init__(text, x, y, width, height, text_color, font_size)

    def reset(self, window):
        font = pygame.font.Font('fonts/gomarice_mix_bit_font.ttf', self.font_size)
        text_render = font.render(self.text, True, self.text_color)
        text_rect = text_render.get_rect()
        text_rect.center = (self.x + self.width / 2, self.y + self.height / 2)
        window.blit(text_render, text_rect)

        
class Frame(Sprite):
    def __init__(self, sprite_img,width,height,x,y):
        super().__init__(sprite_img,width,height,x,y)
        
    
frame = Frame(frame,340,670,210,10)
#btn_menu = Frame(btn_menu,55,70,20,10)
        
def create_blocks():
    blocks = [
        [[1,1],
         [1,1]],

        [[2,2]],

        [[3,3,3]],

        [[4]],

        [[5,5,5,5]],

        [[6,6,6],
         [0,6,0]],

        [[7,7,7],
         [0,0,7]],

        [[8,8,8],
         [0,0,8],
         [0,0,8]],

        [[9,9,9],
         [9,0,0]],

        [[10,10,10],
         [10,0,0],
         [10,0,0]],

        [[11,11,11],
         [11,11,11],
         [11,11,11]],

        [[12,12],
         [12,0]],

        [[13,13],
         [0,13]],

        [[14,14],
         [0,14],
         [0,14]],

        [[15,15],
         [15,0],
         [15,0]],

        [[16,0,0],
         [16,16,16]],

        [[0,17,0],
         [17, 17,17]],

        [[0,0,18],
         [18,18,18]],

        [[19,0,0],
         [19,0,0],
         [19,19,19]],

        [[0,0,20],
         [0,0,20],
         [20,20,20]],

        [[21, 0],
         [21, 0],
         [21, 21]],

        [[0, 0,22],
         [0,0,22],
         [22,22,22]],
        
        [[23],
         [23],
         [23]],
        
        [[24],
         [24]]
    ]
    return random.choice(blocks)

def create_board(points):
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]
    points = 0

def can_move(block, board, row, col):
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] != 0:
                if row + i >= ROWS or col + j < 0 or col + j >= COLS or board[row + i][col + j] != 0:
                    return False
    return True

# def draw_box(window):
#     pygame.draw.rect(window, MIDNIGHTBLUE, [0,0,800,800], 2, 10)# вікно,колір, розмір, товщина, заукруглення
#     point_text = TEXT_FONT.render(f'Score: {result}', True, GRAY)
#     best_result_text = TEXT_FONT.render(f'Hight score: {hight_score}', True, YELLOW)
#     window.blit(point_text, (600, 510))
#     window.blit(best_result_text, (600, 550))

def draw_board(window, board, current_block, current_row, current_col, block_color,points=0, best_result=0):
    window.blit(frame.image, (frame.rect.x, frame.rect.y))
    #window.blit(btn_menu.image, (btn_menu.rect.x, btn_menu.rect.y))
    font = pygame.font.Font('fonts/arcade.ttf', 39)
    points_lb = font.render('POINTS', True, (255, 255, 255))
    points_value_lb = font.render(str(points), True, (255, 255, 255))
    best_result_lb = font.render('BEST  RESULT', True, (255, 255, 255))
    best_result_value_lb = font.render(str(best_result), True, (255, 255, 255))
    window.blit(points_lb,(575,30))
    window.blit(points_value_lb,(575,80))
    window.blit(best_result_lb,(575,160))
    window.blit(best_result_value_lb,(575,210))

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != 0:
                pygame.draw.rect(window, block_color[board[row][col]], (col * MAP_SIZE + 230, row * MAP_SIZE + 20, MAP_SIZE, MAP_SIZE ))
                pygame.draw.rect(window, BLACK, (col * MAP_SIZE + 230, row * MAP_SIZE+20, MAP_SIZE , MAP_SIZE), 4)
    if current_block:
        
        for i in range(len(current_block)):
            for j in range(len(current_block[i])):
                if current_block[i][j] != 0:
                    pygame.draw.rect(window, block_color[current_block[i][j]]  , ((current_col + j) * MAP_SIZE + 230, (current_row + i) * MAP_SIZE + 20, MAP_SIZE , MAP_SIZE))
                    pygame.draw.rect(window, WHITE, ((current_col + j) * MAP_SIZE + 230 , (current_row + i) * MAP_SIZE +20, MAP_SIZE , MAP_SIZE), 3)
    pygame.display.update()


def update_board(block, row, col, board):
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] != 0:
                if row + i >= 0 and row + i < ROWS and col + j >= 0 and col + j < COLS:
                    board[row + i][col + j] = block[i][j]
    return board


def remove_rows(board):
    fill_rows = [row for row in range(ROWS) if 0 not in board[row]]
    for row in fill_rows:
        del board[row]
        board.insert(0, [0] * COLS)
        remove_row_music.play()
    return len(fill_rows)

# def menu_pause(window,Button):
#     pygame.draw.rect(window, blur_win(), [0, 0, 800, 700], 0 , 4)
#     menu_btn = Button("M E N U", 60, 15, 70, 70, BLACK, 60) 
def draw_settings_pause(window,sound_play):
    font = pygame.font.Font('fonts/arcade.ttf', 65)
    music_lb = font.render('M U S I C ', True, (255, 255, 255))
    on_music_lb = font.render('ON',True,(255, 255, 255))
    off_music_lb = font.render('OFF',True,(255, 255, 255))
    window.blit(music_lb , (155,266))
    if sound_play:
        pygame.mixer.music.unpause()    
        window.blit(on_music_lb , (385,266))
    else:
        pygame.mixer.music.pause()
        window.blit(off_music_lb , (385,266))

def draw_control_settings(window):
    window.blit(control_settings_bg ,(0,0))
    font = pygame.font.Font('fonts/arcade.ttf', 65)
    right_move_text = font.render('            Move right',True,(255,255,255))
    left_move_text = font.render('            Move left', True ,(255,255,255))
    turn_move_text = font.render('            Turn 90 degrees',True,(255,255,255))
    window.blit(right_move_text , (170,180))
    window.blit(left_move_text, (170,280))
    window.blit(turn_move_text , (170,380))


def draw_restart_stop(window,text_font,mini_text_font,points = 0):
    game_over_text = text_font.render("GAME  OVER",True,WHITE)
    restart_text = mini_text_font.render("Press  SPACE  to  restart",True,WHITE)
    menu_text = mini_text_font.render("Press  ESCAPE  to  enter  the  menu ",True,WHITE)
    final_points_text = text_font.render('POINTS    ' + str(points), True, WHITE)
    window.blit(final_points_text , (190 , 470))
    window.blit(game_over_text, (210, 160))
    window.blit(restart_text, (130, 270))
    window.blit(menu_text,(70,370))
    
    
def update_points(new_score):
    points = get_max_score()

    with open('results', 'w') as file:
        if new_score > points:
            file.write(str(new_score))
        else:
            file.write(str(points))
            
def get_max_score():
    with open('results', 'r') as file:
        lines = file.readlines()        
        points = int(lines[0].strip())   

    return points 
    
# def set_volume_music(sound_play):
#     if sound_play:
#         pygame.mixer.music.pause()
#         sound_play = False
#     else:
#         pygame.mixer.music.unpause()
#         sound_play = True

        
#     pygame.mixer.music.load(win_music)
#     mixer.music.set_volume(0.3)
#     mixer.music.play(-1)
    

def blur_win(window):
    window.blit(blur, (0, 0))
    pygame.display.update()

def levels(points,fall_time,clock):
    if points >= 300:
        fall_time = 0.8
    if points >= 700:
        fall_time = 1.3
    if points >= 1000:
        fall_time = 1.6
    if points >= 1500:
        fall_time = 2.0
    if points >= 2000:
        fall_time = 2.5

def new_best_result(window,text_font,best_result=0):
    new_best_result_text = text_font.render('New  Best  Result ' + str(best_result),True,YELLOW)
    congratulations_text = text_font.render('CONGRATULATIONS',True,YELLOW)
    window.blit(congratulations_text , (112 , 160))
    window.blit(new_best_result_text , (80,310))
    congratulations_music.play()

def main(): 
    global sound_play
    logo = Images('images/photo_5310251252598300299_x.jpg',400,400,0,780,780)         
    #global init_best_result
    points = 0
    best_result = get_max_score()
    #init_best_result = points
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    TEXT_FONT = pygame.font.Font('fonts/arcade.ttf',70)
    MINI_TEXT_FONT = pygame.font.Font('fonts/arcade.ttf',45)
    
    block_color = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(25)]
    line_color = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(25)]
    pause_bg = Images('images/pause_bg.png',0,0,0,800,800)
    settings_bg = Images('images/settings.png',0,0,0,800,800)
    menu_bg = Images('images/picture 800 x 8 4f5795c0-6a9e-41f5-bba1-06ec9ba43fd5.png',0,0,0,800,700)
    left_move_img = Images('images/control_left.png',135,280,0,70,65)
    new_best_result_bg = Images('images/new_best_result_menu.png',0,0,0,800,700)
    right_move_img = Images('images/control_right.png',135,180,0,70,65)
    turn_move_img = Images('images/control_turn.png',135,380,0,70,65)
    settings_menu_bg = Images('images/settings_menu_bg.png',0,0,0,800,700)
    on_volume_btn = Images('images/soundOnWhite.png',495,264,0,63,63)
    off_volume_btn = Images('images/soundOffWhite.png',495,264,0,63,63)
    game_over_bg = Images('images/game_over_bg.png',0,0,0,800,700)
    gray_bg = Images('images/gray_bg.jpg',220,30,0,310,650)
    sound_play = True 
    volume_changed = False
    btn_play = Button(" S  t  a  r  t", 270, 180, 220, 170, WHITE, 75)
    return_btn = Button("R E T U R N", 285, 460, 150, 150, WHITE, 65)
    control_settings_btn = Button("C O N T R O L", 282, 320, 150, 150, WHITE, 65)
    btn_settings = Button("S  E  T  T  I  N  G  S", 275, 300, 220, 170, WHITE, 72)
    btn_title = Title(" T  E  T  R  I  S", 255, 2, 220, 170, BLACK, 75)
    control_settings_title = Title("C O N T R O L", 278, 2, 220, 170, YELLOW, 75)
    pause_title = Title( " P A U S E ",260,-5 ,220,170 , YELLOW , 80)
    settings_menu_title = Title( "S E T T I N G S",270,-5 ,220,170 , YELLOW , 80)
    btn_pause = Button("P A U S E", 65, 15, 70, 70, YELLOW, 60)
    menu_pause_btn = Button("M E N U", 300, 120, 150, 150, BLACK, 65) 
    menu_settings_btn = Button("M  E  N  U", 290, 450, 150, 150, WHITE, 65) 
    settings_pause_btn = Button("S E T T I N G S", 300, 220, 150, 150, BLACK, 65) 
    restart_pause_btn = Button("R  E S T A R  T", 310, 300, 150, 150, BLACK, 65) 
    continue_pause_btn = Button("C O N T I N U E", 300 , 390 , 150 , 150 , BLACK ,65)
    quit_menu_btn = Button("Q  U  I  T", 40 , 560 , 150 , 150 , WHITE ,65)
    quit_pause_btn = Button("Q  U  I  T", 40 , 560 , 150 , 150 , BLACK ,65)
    quit_new_best_result_btn = Button("Q  U  I  T", 40 , 500 , 150 , 150 , YELLOW ,60)
    menu_new_best_result_btn = Button("M E N U", 270 , 500 , 150 , 150 , YELLOW ,60)
    restart_new_best_result_btn = Button("R E S T A R T", 550 , 500 , 150 , 150 , YELLOW ,60)




    
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    run = True
    current_block = None
    current_row, current_col = 0, 0
    fall_time = 0
    screen = 'menu'
    while run:
        if screen == 'menu':            
            #board = create_board()
            pygame.time.wait(1000)
            menu_bg.reset(window)
            btn_play.reset(window)
            btn_settings.reset(window)
            btn_title.reset(window)
            quit_menu_btn.reset(window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if btn_play.x <= x <= btn_play.x + btn_play.width and btn_play.y <= y <= btn_play.y + btn_play.height:
                        screen = 'run'
                    if btn_settings.x <= x <= btn_settings.x + btn_settings.width and btn_settings.y <= y <= btn_settings.y + btn_settings.height:
                        screen = 'menu_settings'
                    if quit_menu_btn.x <= x <= quit_menu_btn.x + quit_menu_btn.width and quit_menu_btn.y <= y <= quit_menu_btn.y + quit_menu_btn.height:
                        run = False
                    
            pygame.display.update()

        if screen == 'run':
            window.blit(bg_game,(0,0))
            gray_bg.reset(window)    
            btn_pause.reset(window)   
            levels(points,fall_time,clock)
            
            #points = 0
            draw_board(window, board, current_block, current_row, current_col, block_color,points,best_result)
            if current_block is None:
                current_block = create_blocks()
                current_row = 0
                current_col = random.randint(0, COLS - len(current_block[0]))
                points += remove_rows(board) * 100
                update_points(points)         
                               
                
            if not can_move(current_block, board, current_row, current_col):
                screen = 'restart'
                
            
                
                    
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_LEFT] and current_col > 0 and can_move(current_block, board, current_row, current_col - 1):
                current_col -= 1
            if key_pressed[pygame.K_RIGHT] and current_col + len(current_block[0]) < COLS and can_move(current_block, board, current_row, current_col + 1):
                current_col += 1
            if key_pressed[pygame.K_DOWN] and current_col + len(current_block[0]) < COLS and can_move(current_block, board, current_row, current_col + 1):
                current_block = list(zip(*current_block[::-1]))
             
        # if fall_time >= 1000 / (FPS * FALL_SPEED):
        #     print("рух")
            if can_move(current_block, board, current_row + 1, current_col):
                current_row += 1 
            else:
                board = update_board(current_block, current_row, current_col, board)
                current_block = None
            fall_time += clock.tick(5) / 1000
            # if points >= 0:
            #     fall_time += clock.tick(50) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if btn_pause.x <= x <= btn_pause.x + btn_pause.width and btn_pause.y <= y <= btn_pause.y + btn_pause.height:
                        screen = 'pause'
                        # board = create_board()
                        #current_block = None
            
            pygame.display.update()
        if screen == 'menu_settings':
            settings_menu_bg.reset(window)
            settings_menu_title.reset(window)
            menu_settings_btn.reset(window)
            control_settings_btn.reset(window)
            draw_settings_pause(window,sound_play)
            #return_btn.reset(window)
            #on_volume_btn.reset(window)
            if sound_play:
                on_volume_btn.reset(window)
                if volume_changed:
                    off_volume_btn.kill()  # Видаляємо кнопку вимкненого звуку
                    volume_changed = False
            else:
                off_volume_btn.reset(window)
                if volume_changed:
                    on_volume_btn.kill()  # Видаляємо кнопку включеного звуку
                    volume_changed = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if menu_settings_btn.x <= x <= menu_settings_btn.x + menu_settings_btn.width and menu_settings_btn.y <= y <= menu_settings_btn.y + menu_settings_btn.height:
                        screen = 'menu'
                        points = 0
                    if on_volume_btn.rect.x <= x <= on_volume_btn.rect.x + on_volume_btn.rect.width and on_volume_btn.rect.y <= y <= on_volume_btn.rect.y + on_volume_btn.rect.height:
                        sound_play = not sound_play
                        volume_changed = True
                        if sound_play:
                            pygame.mixer.music.unpause()
                        else:
                            pygame.mixer.music.pause()
                    if control_settings_btn.x <= x <= control_settings_btn.x + control_settings_btn.width and control_settings_btn.y <= y <= control_settings_btn.y + control_settings_btn.height:
                        screen = 'control_settings'
                    # if return_btn.rect.x <= x <= return_btn.rect.x + return_btn.rect.width and return_btn.rect.y <= y <= return_btn.rect.y + return_btn.rect.height:
                    #     screen = 'menu'
            pygame.display.update()

        if screen == 'control_settings':
            draw_control_settings(window)
            control_settings_title.reset(window)
            left_move_img.reset(window) 
            right_move_img.reset(window)
            turn_move_img.reset(window)
            return_btn.reset(window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if return_btn.x <= x <= return_btn.x + return_btn.width and return_btn.y <= y <= return_btn.y + return_btn.height:
                        screen = 'menu_settings'
            
            pygame.display.update()
        if screen == 'pause':
            pause_bg.reset(window)
            menu_pause_btn.reset(window)
            settings_pause_btn.reset(window)
            continue_pause_btn.reset(window)
            pause_title.reset(window)
            quit_pause_btn.reset(window)
            restart_pause_btn.reset(window)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if settings_pause_btn.x <= x <= settings_pause_btn.x + settings_pause_btn.width and settings_pause_btn.y <= y <= settings_pause_btn.y + settings_pause_btn.height:
                        screen = 'settings_pause'
                    if menu_pause_btn.x <= x <= menu_pause_btn.x + menu_pause_btn.width and menu_pause_btn.y <= y <= menu_pause_btn.y + menu_pause_btn.height:
                        screen = 'menu'
                        board = create_board(points)
                        current_block = None
                    if continue_pause_btn.x <= x <= continue_pause_btn.x + continue_pause_btn.width and continue_pause_btn.y <= y <= continue_pause_btn.y + continue_pause_btn.height:
                        screen = 'run'
                    if quit_pause_btn.x <= x <= quit_pause_btn.x + quit_pause_btn.width and quit_pause_btn.y <= y <= quit_pause_btn.y + quit_pause_btn.height:
                        run = False
                    if restart_pause_btn.x <= x <= restart_pause_btn.x + restart_pause_btn.width and restart_pause_btn.y <= y <= restart_pause_btn.y + restart_pause_btn.height:
                        current_block = None
                        create_board(points)
                        screen = 'run'
                        
            pygame.display.update()
            

        if screen == "settings_pause":
            settings_bg.reset(window)
            settings_menu_title.reset(window)
            return_btn.reset(window)
            draw_settings_pause(window,sound_play)
            control_settings_btn.reset(window)
            #on_volume_btn.reset(window)
            if sound_play:
                on_volume_btn.reset(window)
                if volume_changed:
                    off_volume_btn.kill()  # Видаляємо кнопку вимкненого звуку
                    volume_changed = False
            else:
                off_volume_btn.reset(window)
                if volume_changed:
                    on_volume_btn.kill()  # Видаляємо кнопку включеного звуку
                    volume_changed = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if on_volume_btn.rect.x <= x <= on_volume_btn.rect.x + on_volume_btn.rect.width and on_volume_btn.rect.y <= y <= on_volume_btn.rect.y + on_volume_btn.rect.height:
                        sound_play = not sound_play
                        volume_changed = True
                        if sound_play:
                            pygame.mixer.music.unpause()
                        else:
                            pygame.mixer.music.pause()
                    if return_btn.x <= x <= return_btn.x + return_btn.width and return_btn.y <= y <= return_btn.y + return_btn.height:
                        screen = 'pause'
                    if control_settings_btn.x <= x <= control_settings_btn.x + control_settings_btn.width and control_settings_btn.y <= y <= control_settings_btn.y + control_settings_btn.height:
                        screen = 'control_settings'
            
            pygame.display.update()

            

        if screen == 'restart':
            game_over_music.play()
            board = create_board(points)
            game_over_bg.reset(window)
            draw_restart_stop(window, TEXT_FONT, MINI_TEXT_FONT,points)
            if best_result < points:
                best_result = points
                screen = 'new_best_result'
            # if points > init_best_result:
            #     init_best_result = points
            #     with open("results", "w") as file:
            #         file.write(f'{points}\n')

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                create_board(points)  
                points = 0
                screen = 'run'
                pygame.time.wait(900)
            elif keys[pygame.K_ESCAPE]:
                create_board(points)  
                points = 0
                screen = 'menu'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
        
        if screen == 'new_best_result':
            new_best_result_bg.reset(window)
            new_best_result(window,TEXT_FONT,best_result)
            quit_new_best_result_btn.reset(window)
            menu_new_best_result_btn.reset(window)
            restart_new_best_result_btn.reset(window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if quit_new_best_result_btn.x <= x <= quit_new_best_result_btn.x + quit_new_best_result_btn.width and quit_new_best_result_btn.y <= y <= quit_new_best_result_btn.y + quit_new_best_result_btn.height:
                        run = False
                    if menu_new_best_result_btn.x <= x <= menu_new_best_result_btn.x + menu_new_best_result_btn.width and menu_new_best_result_btn.y <= y <= menu_new_best_result_btn.y + menu_new_best_result_btn.height:
                        screen = 'menu'
                        board = create_board(points)
                        current_block = None
                        points = 0
                    if restart_new_best_result_btn.x <= x <= restart_new_best_result_btn.x + restart_new_best_result_btn.width and restart_new_best_result_btn.y <= y <= restart_new_best_result_btn.y +restart_new_best_result_btn.height:
                        screen = 'run'
                        board = create_board(points)
                        current_block = None
                        points = 0
            pygame.display.update()
        
        window.fill(GRAY)
    pygame.quit()


if __name__ == "__main__":
    main()
