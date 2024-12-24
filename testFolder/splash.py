import pygame, sys
from button import Button
import time

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("OPENCV Duel 2022")

BG = pygame.image.load("Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        SCREEN.fill("black")
        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(30).render("This is how to play the game.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        INSTRUCTION_TEXT1 = get_font(15).render("Arm yourself with a lightsaber to fight your virtual opponent", True, "Black")
        INSTRUCTION_RECT1 = INSTRUCTION_TEXT1.get_rect(center=(640,230))
        SCREEN.blit(INSTRUCTION_TEXT1, INSTRUCTION_RECT1)

        INSTRUCTION_TEXT2 = get_font(15).render("Keep your hand in frame of the screen and you will wield your weapon", True, "Black")
        INSTRUCTION_RECT2 = INSTRUCTION_TEXT2.get_rect(center=(640,270))
        SCREEN.blit(INSTRUCTION_TEXT2, INSTRUCTION_RECT2)

        INSTRUCTION_TEXT3 = get_font(15).render("Defend yourself from the opponents attacks", True, "Black")
        INSTRUCTION_RECT3 = INSTRUCTION_TEXT3.get_rect(center=(640,310))
        SCREEN.blit(INSTRUCTION_TEXT3, INSTRUCTION_RECT3)

        INSTRUCTION_TEXT4 = get_font(15).render("But be warned challenger", True, "Black")
        INSTRUCTION_RECT4 = INSTRUCTION_TEXT4.get_rect(center=(640,350))
        SCREEN.blit(INSTRUCTION_TEXT4, INSTRUCTION_RECT4)

        INSTRUCTION_TEXT5 = get_font(15).render("Your opponent is a true master swordsman", True, "Black")
        INSTRUCTION_RECT5 = INSTRUCTION_TEXT5.get_rect(center=(640,390))
        SCREEN.blit(INSTRUCTION_TEXT5, INSTRUCTION_RECT5)

        INSTRUCTION_TEXT6 = get_font(15).render("With one good hit, you will meet your end.", True, "Black")
        INSTRUCTION_RECT6 = INSTRUCTION_TEXT5.get_rect(center=(640,430))
        SCREEN.blit(INSTRUCTION_TEXT6, INSTRUCTION_RECT6)

        OPTIONS_BACK = Button(image=None, pos=(100, 660), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="INSTRUCTIONS", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                    
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def main():
    pygame.mixer.music.load('TitleScreenTheme.wav')
    pygame.mixer.music.play(-1)
    main_menu()

main()