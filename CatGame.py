import pygame  
import sys    
import random  
pygame.init()  
pygame.mixer.init()  

# ---------------- MUSIC ----------------
pygame.mixer.music.load("sounds/CatMusic.wav")  
pygame.mixer.music.set_volume(0.5)          
pygame.mixer.music.play(-1)                  

# ---------------- WINDOW ----------------
screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE) 
pygame.display.set_caption("Catch the Fish!")  

# ---------------- ASSETS ----------------
cat_images_raw = [pygame.image.load(f"Box3-{i}.png.png") for i in range(1, 5)] 
fish_image_raw = pygame.image.load("Goldfish.png").convert_alpha()  

# ---------------- SETTINGS ----------------
FPS = 30              
CAT_FPS = 5           
fish_spawn_delay = 15 
fish_base_speed = 4    
GAME_TIME = 60       

clock = pygame.time.Clock() 

# ---------------- SCALING ----------------
def scale_cat_images():
    scaled = []  
    w = screen.get_width()  
    factor = max(2.2, 3.2 - (w / 600)) 
    for img in cat_images_raw:
        scale = (w / factor) / img.get_width()  
        scaled.append(
            pygame.transform.scale(
                img,
                (int(img.get_width() * scale),  
                 int(img.get_height() * scale)) 
            )
        )
    return scaled  

def scale_fish_image():
    scale_factor = screen.get_width() / 600 
    extra_size = 1.5  
    w = int(fish_image_raw.get_width() * scale_factor * extra_size) 
    h = int(fish_image_raw.get_height() * scale_factor * extra_size)  
    return pygame.transform.scale(fish_image_raw, (w, h))  

def get_font(base=20):
    scale = max(1, screen.get_width() / 600)  
    return pygame.font.Font("PixelOperatorHB8.ttf", int(base * scale))  

# ---------------- GAME STATE ----------------
cat_images = scale_cat_images()  
fish_image = scale_fish_image()  
font = get_font(20)             
big_font = get_font(25)        

cat_frame = 0  
cat_timer = 0 

fish_list = []  
fish_timer = 0  

score = 0       
start_ticks = 0  

state = "start" 
first_start = True 

# ---------------- RESET ----------------
def reset_game():
    """Resets game variables to start a new round."""
    global score, fish_list, fish_timer, start_ticks
    global cat_frame, cat_timer, state

    score = 0           
    fish_list = []      
    fish_timer = 0      
    cat_frame = 0       
    cat_timer = 0       
    start_ticks = pygame.time.get_ticks()  
    state = "game"      

# ---------------- CAT ANIMATION ----------------
def draw_cat():
    global cat_frame, cat_timer
    dt = clock.get_time() 

    cat_timer += dt  
    if cat_timer >= 1000 / CAT_FPS: 
        cat_frame = (cat_frame + 1) % len(cat_images)  
        cat_timer = 0 

    cat_img = cat_images[cat_frame]  
    x, _ = pygame.mouse.get_pos()  
    rect = cat_img.get_rect(midbottom=(x, screen.get_height() - 10))  
    screen.blit(cat_img, rect)  
    return rect  

# ---------------- START SCREEN ----------------
def start_screen():
    global state, screen, cat_images, font, big_font, fish_image

    while state == "start":
        clock.tick(FPS)  
        screen.fill((255, 180, 190))  

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  
                pygame.quit()
                sys.exit()

            elif event.type == pygame.VIDEORESIZE:  
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                cat_images[:] = scale_cat_images()  
                font = get_font(18)               
                big_font = get_font(20)
                fish_image = scale_fish_image()   

            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if start_button.collidepoint(event.pos): 
                    reset_game()  

        title = big_font.render("Catch the Fish!", True, (0, 0, 0))  
        screen.blit(title, title.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4)))

        label = font.render("START", True, (255, 255, 255)) 
        label_rect = label.get_rect()
        scale = screen.get_width() / 600  
        padding_x = int(30 * scale)  
        padding_y = int(14 * scale)  
        start_button = pygame.Rect(
            screen.get_width() // 2 - (label_rect.width + padding_x * 2) // 2, 
            screen.get_height() // 2,
            label_rect.width + padding_x * 2,
            label_rect.height + padding_y * 2
        )

        mouse_pos = pygame.mouse.get_pos()  
        color = (255, 130, 200) if start_button.collidepoint(mouse_pos) else (255, 105, 180)  
        pygame.draw.rect(screen, color, start_button, border_radius=12) 
        screen.blit(label, label.get_rect(center=start_button.center))  

        draw_cat() 
        pygame.display.flip()  

# ---------------- GAME LOOP ----------------
def game_loop():
    """Main gameplay loop handling fish, collisions, score, and timer."""
    global state, screen, cat_images, font, fish_timer, score, start_ticks, fish_image

    while state == "game":
        clock.tick(FPS) 
        screen.fill((255, 180, 190))  

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                state = "game_over"  

            elif event.type == pygame.VIDEORESIZE: 
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                cat_images[:] = scale_cat_images() 
                font = get_font(20)                
                big_font = get_font(25)
                fish_image = scale_fish_image()     

        cat_rect = draw_cat()  

        # --- Spawn Fish ---
        fish_timer += 1
        if fish_timer >= fish_spawn_delay:  
            fish_timer = 0
            x = random.randint(0, screen.get_width() - fish_image.get_width())  
            fish_list.append(pygame.Rect(x, -fish_image.get_height(), fish_image.get_width(), fish_image.get_height()))  

        # --- Update Fish ---
        scaled_fish_speed = fish_base_speed * (fish_image.get_height() / fish_image_raw.get_height()) 

        for fish in fish_list[:]: 
            fish.y += scaled_fish_speed  
            screen.blit(fish_image, (fish.x, fish.y)) 

            if fish.colliderect(cat_rect):  
                score += 1  
                fish_list.remove(fish)  
            elif fish.y > screen.get_height():  
                fish_list.remove(fish)

        # --- Timer ---
        seconds = GAME_TIME - (pygame.time.get_ticks() - start_ticks)//1000  
        if seconds <= 0:
            state = "game_over"  

        # --- UI ---
        screen.blit(font.render(f"SCORE:{score}", True, (0,0,0)), (12,12))  
        time_text = font.render(f"TIME:{max(0,seconds)}", True, (0,0,0))  
        screen.blit(time_text, time_text.get_rect(topright=(screen.get_width()-12,12)))

        pygame.display.flip()  

# ---------------- GAME OVER ----------------
def game_over_screen():
    global state, screen, font, big_font

    while state == "game_over":
        clock.tick(FPS)  
        screen.fill((255, 180, 190))  

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()
                sys.exit()

            elif event.type == pygame.VIDEORESIZE:  
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                font = get_font(18)  
                big_font = get_font(25)

            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if play_button.collidepoint(event.pos):  
                    reset_game() 

        text = big_font.render(f"Time's up! Your score: {score}", True, (0, 0, 0))  
        screen.blit(text, text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4)))

        label = font.render("PLAY AGAIN", True, (255, 255, 255))  
        label_rect = label.get_rect()
        scale = screen.get_width() / 600  
        padding_x = int(30 * scale)
        padding_y = int(14 * scale)
        play_button = pygame.Rect(
            screen.get_width() // 2 - (label_rect.width + padding_x * 2) // 2, 
            screen.get_height() // 2,
            label_rect.width + padding_x * 2,
            label_rect.height + padding_y * 2
        )
        mouse_pos = pygame.mouse.get_pos() 
        color = (255, 130, 200) if play_button.collidepoint(mouse_pos) else (255, 105, 180)
        pygame.draw.rect(screen, color, play_button, border_radius=12)  
        screen.blit(label, label.get_rect(center=play_button.center))  

        pygame.display.flip() 

# ---------------- MAIN ----------------
while True: 
    if first_start:
        start_screen()  
        first_start = False
    game_loop()       
    game_over_screen()  