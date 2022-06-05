
import pygame
from pygame import mixer

pygame.init()

#globals

WIDTH = 1400
HEIGHT = 800

#colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
this_color = ((60, 44, 62))
cylan = (194, 222, 209)
gold = ((53, 66, 89))
blue = (0, 255, 255)
dark_this_color = (50, 50 ,50)
buttom_color = (55, 226, 213)
buttom_color1 = (194, 222, 209)
hovered_color = (146, 180, 236)


print ("lalal")
Instrumants = 6

#load sounds
Hi_Hat = mixer.Sound('sounds\hi hat.WAV')
Clap = mixer.Sound('sounds\clap.WAV')
Crash = mixer.Sound('sounds\crash.WAV')
Kick = mixer.Sound('sounds\kick.WAV')
Snare = mixer.Sound('sounds\snare.WAV')
Tom = mixer.Sound('sounds\\tom.WAV')


Hi_Hat2 = mixer.Sound('sounds\kit2\hi hat.WAV')
Clap2 = mixer.Sound('sounds\kit2\clap.WAV')
Crash2 = mixer.Sound('sounds\kit2\crash.WAV')
Kick2 = mixer.Sound('sounds\kit2\kick.WAV')
Snare2 = mixer.Sound('sounds\kit2\snare.WAV')
Tom2 = mixer.Sound('sounds\kit2\\tom.WAV')

pygame.mixer.set_num_channels(Instrumants * 3)




screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.SysFont("comicsans", 32)
medium_font = pygame.font.SysFont("comicsans", 24)

fps = 60
timer = pygame.time.Clock()

def bpm_control(bpm):
    bmp_rect = pygame.draw.rect(screen, this_color, [350, HEIGHT - 150, 210, 103], 5, 5)
    pygame.draw.rect(screen, black, [350, HEIGHT - 150, 210, 103], 3, 3)

    bpm_text = medium_font.render('Beats Per Minute', True, white)
    screen.blit(bpm_text, (358, HEIGHT - 130))

    bpm_text2 = label_font.render(f'{bpm}', True, white)
    screen.blit(bpm_text2, (420, HEIGHT - 100))

    bpm_add_rect = pygame.draw.rect(screen, this_color, [567, HEIGHT - 118, 35, 35], 0, 5)
    pygame.draw.rect(screen, black, [567, HEIGHT - 118, 35, 35], 2, 3)
    bpm_sub_rect = pygame.draw.rect(screen, this_color, [300, HEIGHT - 118, 35, 35], 0, 5)
    pygame.draw.rect(screen, black, [300, HEIGHT - 118, 35, 35], 2, 3)

    add_text = medium_font.render('+', True, white)
    sub_text = medium_font.render('-', True, white)
    screen.blit(add_text, (580, HEIGHT - 120))
    screen.blit(sub_text, (312, HEIGHT - 120))

    return bpm_add_rect, bpm_sub_rect

def beat_control(beat):
    beat_rect = pygame.draw.rect(screen, this_color, [650, HEIGHT - 150, 210, 103], 5, 5)
    pygame.draw.rect(screen, black, [650, HEIGHT - 150, 210, 103], 2, 3)

    beat_text = medium_font.render('Number of beats', True, white)
    screen.blit(beat_text, (658, HEIGHT - 130))
    beat_text2 = label_font.render(f'{beat}', True, white)
    screen.blit(beat_text2, (750, HEIGHT - 100))

    beat_add_rect = pygame.draw.rect(screen, this_color, [867, HEIGHT - 118, 35, 35], 0, 5)
    pygame.draw.rect(screen, black, [867, HEIGHT - 118, 35, 35], 2, 5)
    beat_sub_rect = pygame.draw.rect(screen, this_color, [610, HEIGHT - 118, 35, 35], 0, 5)
    pygame.draw.rect(screen, black, [610, HEIGHT - 118, 35, 35], 2, 5)

    add_text = medium_font.render('+', True, white)
    sub_text = medium_font.render('-', True, white)
    screen.blit(add_text, (880, HEIGHT - 120))
    screen.blit(sub_text, (622, HEIGHT - 120))

    return beat_add_rect, beat_sub_rect

def add_box_and_text(box_text, box_x, box_y, color, box_width, box_height, text_color, font):
    rect = pygame.draw.rect(screen, color, [box_x, box_y, box_width, box_height], 0 , 5)
    pygame.draw.rect(screen, (0, 0, 0), [box_x , box_y  , box_width, box_height], 2 , 5)
    text = font.render(f'{box_text}', True, text_color)
    screen.blit(text, (box_x + 7  , box_y + 5 ))
    return rect


def draw_manu_stuff(playing, color, clear_color, save_color, load_color):

    play_pause = pygame.draw.rect(screen, (color), [50,HEIGHT - 150, 200, 100], 0 , 5)
    pygame.draw.rect(screen, (black), [50,HEIGHT - 150, 200, 100], 2 , 5)
    play_text = label_font.render('play/pause', True, black)

    screen.blit(play_text, (70, HEIGHT - 135))
    if playing:
        play_text2 = medium_font.render('Playing', True, black)
    else:
        play_text2 = medium_font.render('Paused', True, black)
    screen.blit(play_text2, (70, HEIGHT - 90))

    save_buttom = add_box_and_text('save beat', 1000, HEIGHT - 150, save_color, 120, 50, black, medium_font)
    load_buttom = add_box_and_text('load beat', 1000, HEIGHT - 90, load_color, 120, 50, black, medium_font)
    clear_buttom = add_box_and_text('clear', 1200, HEIGHT - 90, clear_color, 69, 50, black, medium_font)


    return play_pause, save_buttom, load_buttom, clear_buttom, color, clear_color, load_color


def play_notes(clicked, active_beat, drums):
    for i in range(len(clicked)):
        if clicked[i][active_beat] == True:
            globals()[drums[i]].play()

def put_drum_text(drums):
    position_x, position_y = 50, 30
    for i, text in enumerate(drums):
        text = label_font.render(drums[i], True, white)
        screen.blit(text, (position_x, position_y))
        pygame.draw.line(screen, black, (0, (i + 1) * 100), (195, (i + 1) * 100), 2)
        position_y += 100

def draw_beat(active_beat, beats, instrumants):
    active = pygame.draw.rect(screen, blue, [active_beat * ((WIDTH - 200)) // beats + 200, 0, ((WIDTH - 200)//beats), instrumants * 100], 5, 3)

def draw_boxes(beats, instrumants, boxes, clicked):
    for i in range(beats):
        for j in range(instrumants):
            if not clicked[j][i]:
                color = this_color
            else:
                color = cylan

            pygame.draw.rect(screen, color, [(i  * (WIDTH -200) // beats) + 200, 
            (j * 100) + 5, (WIDTH - 200) // beats - 10, ((HEIGHT - 200) // instrumants) - 10], 0, 3)
            pygame.draw.rect(screen, black, [(i  * (WIDTH -200) // beats) + 200, 
            (j * 100) + 5, (WIDTH - 200) // beats - 10, ((HEIGHT - 200) // instrumants) - 10], 1, 3)

            pygame.draw.rect(screen, gold, [(i  * (WIDTH -200) // beats) + 200, 
            (j * 100), (WIDTH - 200) // beats, ((HEIGHT - 200) // instrumants)], 5, 5)
            pygame.draw.rect(screen, black, [(i  * (WIDTH -200) // beats) + 200, 
            (j * 100), (WIDTH - 200) // beats, ((HEIGHT - 200) // instrumants)], 2, 5)

            boxes.append(((pygame.draw.rect(screen, black, [(i  * (WIDTH -200) // beats) + 200, 
            (j * 100), (WIDTH - 200) // beats, ((HEIGHT - 200) // instrumants)], 2, 5)) , (i, j)))
    
    return boxes

def draw_grid(beats, instrumants, clicked, active_beat, drums):
    left_box = pygame.draw.rect(screen, this_color, [0,0 , 200, HEIGHT - 195],0, 5)
    pygame.draw.rect(screen, black, [0,0 , 200, HEIGHT - 195], 2, 5)
    bottom_box = pygame.draw.rect(screen, this_color, [0, HEIGHT -200, WIDTH, 200], 5)
    pygame.draw.rect(screen, black, [0, HEIGHT -200, WIDTH, 200],3, 4)

    boxes = []
    colors = [this_color, white, this_color]
    put_drum_text(drums)
    boxes = draw_boxes(beats, instrumants, boxes, clicked)
    draw_beat(active_beat, beats, instrumants)
    return boxes

def save_func(exit_buttom_color):
    pygame.draw.rect(screen, (50, 50, 50), [0, 0, WIDTH, HEIGHT])
    back_button = add_box_and_text('<---',  100, 50, exit_buttom_color, 55, 50, black, medium_font)
    return back_button


def load_func(load_manu):
    saved_beats = []
    with open("saved_beats.txt",'r') as f:
        for line in f:
            saved_beats.append(line)

def main():
    exit_buttom = False
    save_manu = False
    load_manu = False
    active_beat, active_length = 1, 0
    clear_color_selector = buttom_color1
    save_color_selector = buttom_color1
    load_color_selector = buttom_color1
    exit_buttom_color = buttom_color1
    playing = True
    beat_changed = True
    beats = 8
    instrumants = Instrumants 
    bpm =  240
    bpm_up = False
    bpm_down = False
    clicked = [[False for _ in range(100)] for _ in range(instrumants)]
    boxes = []
    run = True
    kit_selector = False
    
    color = this_color
    

    while run:
        timer.tick(fps)
        screen.fill((75, 93, 103))

        for _ in range (pygame.mixer.get_num_channels()):
            pygame.mixer.Channel(_).set_volume(0.8)
    
        send_drums = []
        
        drums1 = ['Hi_Hat','Snare','Kick','Crash','Clap','Tom']
        drums2 = ['Hi_Hat2','Snare2','Kick2','Crash2','Clap2','Tom2']

        if kit_selector:
            send_drums = drums1
        else:
            send_drums = drums2


        boxes = draw_grid(beats, instrumants, clicked, active_beat, send_drums)
        play_pause, save_buttom, load_buttom, clear_buttom, color, clear_color_selector, load_color_selector = draw_manu_stuff(playing, color, 
        clear_color_selector, save_color_selector, load_color_selector)
        bpm_add_rect, bpm_sub_rect = bpm_control(bpm)
        beat_add_rect, beat_sub_rect = beat_control(beats)

        if save_manu:
            playing = False
            exit_buttom = save_func(exit_buttom_color)
            if exit_buttom.collidepoint(pygame.mouse.get_pos()):
                exit_buttom_color = hovered_color
            else:
                exit_buttom_color = buttom_color1
  

        if bpm_up:
            bpm += 1
        elif bpm_down:
            bpm -= 1

        #hover effects:

        if play_pause.collidepoint(pygame.mouse.get_pos()):
            color = hovered_color
        else:
            color = buttom_color1

        if clear_buttom.collidepoint(pygame.mouse.get_pos()):
            clear_color_selector = hovered_color
        else:
            clear_color_selector = buttom_color1

        if save_buttom.collidepoint(pygame.mouse.get_pos()):
            save_color_selector = hovered_color
        else:
            save_color_selector = buttom_color1
        
        if load_buttom.collidepoint(pygame.mouse.get_pos()):
            load_color_selector = hovered_color
        else:
            load_color_selector = buttom_color1

        if beat_changed:
            play_notes(clicked, active_beat, send_drums)
            beat_changed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    kit_selector = not kit_selector

            #all mouse down actions
            if event.type == pygame.MOUSEBUTTONDOWN and not save_manu and not load_manu:
                if bpm_add_rect.collidepoint(event.pos):
                    bpm_up = True
                elif bpm_sub_rect.collidepoint(event.pos):
                    bpm_down = True
                elif play_pause.collidepoint(event.pos):
                    color = black
                elif clear_buttom.collidepoint(event.pos):
                    clear_color_selector = black
                elif save_buttom.collidepoint(event.pos):
                    save_color_selector = black
                elif load_buttom.collidepoint(event.pos):
                    load_color_selector = black
                elif exit_buttom.collidepoint(event.pos):
                    exit_buttom_color = black
                

                for i in range(len(boxes)):
                    # boxes is a tuple, boxes = ((rect1, pos1) , (rect1, pos1) . . . ) | 
                    # so box [0] = (rect1, pos1) and box[0][0] will be (pos1)
                    if boxes[i][0].collidepoint(event.pos):
                        coords = boxes[i][1]
                        clicked[coords[1]][coords[0]] = not (clicked[coords[1]][coords[0]])
                    
            #all mouse up actions
            if event.type == pygame.MOUSEBUTTONUP and not save_manu and not load_manu:
                bpm_up = False
                bpm_down = False
                if play_pause.collidepoint(event.pos):
                    playing = not playing
                elif beat_add_rect.collidepoint(event.pos):
                    beats +=1
                elif beat_sub_rect.collidepoint(event.pos):
                    beats -=1
                elif clear_buttom.collidepoint(event.pos):
                    clicked = [[False for _ in range(100)] for _ in range(instrumants)]
                elif save_buttom.collidepoint(event.pos):
                    save_manu = True
                elif load_buttom.collidepoint(event.pos):
                    load_manu = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if exit_buttom:
                    save_manu = False
                    load_manu = False
                    playing  = True
      
        beat_length = fps * 60 // bpm # for a second, means how fast do we move to the next beat considering the fps

        if playing: #checks if we are in the same beat
            if active_length < beat_length:
                active_length += 1 
            else:
                active_length = 0
                if active_beat < beats - 1: #counts the number of beats, we are now on 8/4
                    active_beat += 1
                    beat_changed = True
                else:
                    active_beat = 0
                    beat_changed = True
                    


        pygame.display.flip()
    pygame.quit()

main()

