import cv2
import mediapipe as mp
import time
import numpy as np
import random 
from shapely.geometry import Polygon
import pygame, sys
from button import Button


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
 
#-----Official Game Code Starts Here-----
def check_intersection(coords1, coords2):
	# Then, define a function that takes in two sets of coordinates and returns 
	# a boolean indicating whether the polygons they define intersect
	# Create two Shapely Polygon objects from the input coordinate lists
	poly1 = Polygon(coords1)
	poly2 = Polygon(coords2)
	
	# Check if the polygons intersect and return the result
	return poly1.intersects(poly2)

	# Test the function using the two lists of coordinates defined above
	print(polygons_intersect(coords1, coords2)) # Should print True

def posScreen(corner_swordX,corner_swordY):
	#Todo:
	#width = picture.get(cv2.CAP_PROP_FRAME_WIDTH )
	#height = picture.get(cv2.CAP_PROP_FRAME_HEIGHT )

	#--For regular computers--#
	#width=640
	#height=480
	#-------------------------#
	#------For macbooks-------#
	height=1080
	width=1920
	#--------------------------#
	corner_swordX = round(width*corner_swordX)
	corner_swordY = round(height*corner_swordY)
	return corner_swordX,corner_swordY

#------LIGHTSABER HERE------ 
def drawsword(hand,picture,i):
	#hand - array of landmarks
	
	#Defining the colors for the sabers
	if i == 0:
		color=(255,0,0)
	else:
		color=(255,0,0)
	
	#height,width,dimensons= picture.shape
	#print (height,width)#480 640

	#corner_swordX = (hand[5].x+(hand[5].x-hand[17].x)/2)
	ApointX=(hand[6].x+hand[10].x+hand[14].x+hand[18].x)/4
	ApointY=(hand[6].y+hand[10].y+hand[14].y+hand[18].y)/4
	
	#ApointX,ApointY=posScreen(ApointX,ApointY)
	
	BpointX=(ApointX*3+hand[0].x)/4
	BpointY=(ApointY*3+hand[0].y)/4

	swordHalfLengthX=(ApointX-hand[18].x)*1.2 #.5
	swordHalfLengthY=(ApointY-hand[18].y)*1.2 #.5

	# width of sword derived from model
	swordWidthX=(BpointX-ApointX) * 0.6
	swordWidthY=(BpointY-ApointY) * 0.6

	CpointX=(BpointX+swordHalfLengthX)
	CpointY=(BpointY+swordHalfLengthY)

	DpointX=(CpointX+swordWidthX)
	DpointY=(CpointY+swordWidthY)
	
	EpointX=(DpointX-swordHalfLengthX*2)
	EpointY=(DpointY-swordHalfLengthY*2)

	FpointX=(EpointX-swordWidthX)
	FpointY=(EpointY-swordWidthY)

	# define handle points relative to frame
	pointC=posScreen(CpointX, CpointY)
	pointD=posScreen(DpointX, DpointY)
	pointE=posScreen(EpointX, EpointY)
	pointF=posScreen(FpointX, FpointY)


	C2X=(CpointX+swordHalfLengthX*9)
	C2Y=(CpointY+swordHalfLengthY*9)

	D2X=(C2X+swordWidthX*1.2)
	D2Y=(C2Y+swordWidthY*1.2)

	#save handle points in array
	handlePts = [pointC,pointD,pointE,pointF]

	#draw handle black
	cv2.fillPoly(picture, np.array([handlePts]),(20,0,0))

	#top two points for end of sword
	C2=posScreen(C2X, C2Y)
	D2=posScreen(D2X, D2Y)

	#display sword color
	bladePts = [pointC,pointD,D2,C2]
	cv2.fillPoly(picture, np.array([bladePts]),(color))

	#Print sword coordinates to terminal
	#print("Handle Points: ", handlePts)
	#print("Blade Points: ", bladePts)
	#print("\n")

	return picture, bladePts 

def enemyAttack(picture, bladeNum, black, red):
	#randomNum = random.randint(0,6)

	#----------------------For regular computers----------------------------------#
	""" #Vader Blade 1
	opponentPoints1 = [(514, 334), (532, 333), (585, 407), (567, 408)]
	opponentBladePoints1 = [(514, 334), (532, 333), (296, 4), (275, 5)]
	#Vader Blade 2
	opponentPoints2 = [(135, 401), (141, 407), (97, 489), (91, 484)]
	opponentBladePoints2 = [(135, 401), (141, 407), (338, 37), (331, 30)]
	#Vader Blade 3
	opponentPoints3 = [(155, 232), (148, 247), (51, 249), (58, 233)] 
	opponentBladePoints3 = [(155, 232), (148, 247), (582, 242), (591, 223)] 
	#Vader Blade 4
	opponentPoints4 = [(190, 146), (179, 159), (108, 102), (119, 90)] 
	opponentBladePoints4 = [(190, 146), (179, 159), (497, 416), (510, 401)] 
	#Vader Blade 5
	opponentPoints5 = [(190, 282), (193, 300), (103, 345), (99, 327)]
	opponentBladePoints5 = [(190, 282), (193, 300), (601, 99), (598, 77)] 
	#Vader Blade 6
	opponentPoints6 = [(323, 359), (303, 370), (303, 500), (323, 490)] 
	opponentBladePoints6 = [(323, 359), (303, 370), (299, -216), (322, -228)]
	#Vader Blade 7
	opponentPoints7 = [(277, 199), (259, 180), (9, 326), (28, 345)] 
	opponentBladePoints7 = [(277, 199), (259, 180), (1378, -481), (1400, -458)] 
 """
    #------------------------------------------------------------------------------#

	#------------------------For macbooks------------------------------------------#
	#Vader Blade 1
	opponentPoints1 = [(1792, 764), (1767, 806), (1868, 961), (1893, 918)]
	opponentBladePoints1 = [(1792, 764), (1767, 806), (1305, 120), (1335, 69)]
	#Vader Blade 2
	opponentPoints2 = [(265, 497), (300, 514), (442, 735), (408, 717)]
	opponentBladePoints2 = [(265, 497), (300, 514), (-334, -474), (-375, -496)]
	#Vader Blade 3
	opponentPoints3 = [(1442, 60), (1456, 113), (1678, 127), (1665, 75)] 
	opponentBladePoints3 = [(1442, 60), (1456, 113), (458, 57), (442, -6)] 
	#Vader Blade 4
	opponentPoints4 = [(737, 947), (765, 925), (939, 1018), (911, 1039)] 
	opponentBladePoints4 = [(737, 947), (765, 925), (-12, 506), (-45, 532)] 
	#Vader Blade 5
	opponentPoints5 = [(1191, 618), (1175, 621), (1186, 765), (1202, 762)]
	opponentBladePoints5 = [(1191, 618), (1175, 621), (1123, -28), (1142, -31)] 
	#Vader Blade 6
	opponentPoints6 = [(442, 191), (403, 235), (162, 125), (201, 81)] 
	opponentBladePoints6 = [(442, 191), (403, 235), (1479, 738), (1526, 685)]
	#Vader Blade 7
	opponentPoints7 = [(873, 554), (822, 553), (677, 797), (728, 798)] 
	opponentBladePoints7 = [(873, 554), (822, 553), (1464, -546), (1526, -544)] 
	#------------------------------------------------------------------------------#

	#Vader Attacks in an array
	opponentPoints = np.array([opponentPoints1,opponentPoints2,opponentPoints3,opponentPoints4,opponentPoints5,opponentPoints6,opponentPoints7])
	opponentBladePoints = np.array([opponentBladePoints1,opponentBladePoints2,opponentBladePoints3,opponentBladePoints4,opponentBladePoints5,opponentBladePoints6,opponentBladePoints7])

	cv2.fillPoly(picture, np.array([opponentPoints[bladeNum]]),black)#This is where the handle from the enemyAttack function is drawn 
	cv2.fillPoly(picture, np.array([opponentBladePoints[bladeNum]]),red)#This is where the blade from the enemyAttack function is drawn 
	return opponentBladePoints[bladeNum]

def play():
	black = (20,0,0)
	red = (0,0,255)
	white = (255, 255, 255)

	#------For regular computers-----#
	#darth = cv2.imread('darth.jpg')
	#--------------------------------#
	#---------For macbooks-----------#
	darth = cv2.imread('darthSize2.jpeg')
	#--------------------------------#

	img2gray = cv2.cvtColor(darth, cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
	font = cv2.FONT_HERSHEY_SIMPLEX
	font_size = 0.5

	# Define the coordinates where the text will be drawn on the image
	x = 10
	y = 50
	
	# Define the value to be written on the image
	text = "Score: "
	speedText = "Speed Increased!"
	livesText = "Lives: " 

	pTime = 0
	plocX, plocY = 0, 0
	clocX, clocY = 0, 0

	mp_drawing = mp.solutions.drawing_utils
	mp_drawing_styles = mp.solutions.drawing_styles
	mp_hands = mp.solutions.hands

	# For webcam input:
	cap = cv2.VideoCapture(0)
	#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
	#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
	cyclesBeforeSwitch = 30
	numCycles = 0
	swordNumber = 0
	playerScore = 1000
	scoreColor = white
	printVal = 0
	numLives = 3
	switchCatch = False
	gameKill = False
	with mp_hands.Hands(
		model_complexity=0,
		min_detection_confidence=0.5,
		min_tracking_confidence=0.5) as hands:
			while cap.isOpened() and not gameKill:
				pygame.display.update()
				success, image = cap.read()
				#----ENEMY LIGHTSABER HERE--\
				#generate virtual opponents attacks that the player will have to block
				
				#----ENEMY LIGHTSABER HERE--
				if not success:
					print("Ignoring empty camera frame.")
					# If loading a video, use 'break' instead of 'continue'.
					continue
				# To improve performance, optionally mark the image as not writeable to
				image.flags.writeable = False

				#Pull current frame from video to process on
				image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

				#Process image to extract hand landmark data
				results = hands.process(image)

				# Draw the hand annotations on the image, convert image to bgr colorscheme
				image.flags.writeable = True
				image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


				# If multiple hands detected
				if results.multi_hand_landmarks:
					#print (results)

					#Starting with first hand, cycle through detected hands
					i=0
					for hand_landmarks in results.multi_hand_landmarks:
						roi = image
						roi[np.where(mask)] = 0
						roi += darth
						#------LIGHTSABER HERE------ 
						attackBladePts = enemyAttack(image, swordNumber, black, red)
						#generate new image with user sword drawn
						image, bladePts = drawsword(hand_landmarks.landmark,image,i)

						intersection = check_intersection(attackBladePts, bladePts)
				
						if not intersection:
							scoreColor = red
							# Draw the border on the image
							#--For regular computers--#
							#image = cv2.rectangle(image, (0, 0), (639, 479), red, 2)
							#--For macbooks--#
							image = cv2.rectangle(image, (0, 0), (1919, 1079), red, 2)
						else:
							scoreColor = white
						#print(intersection)
						i=i+1
						#------LIGHTSABER HERE------ 

						
						#print(
						#	f'Middle finger tip coordinates: (',
						#	f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x}, '
						#	f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y})'
						#)	xz

						mp_drawing.draw_landmarks(
							image,
							hand_landmarks,
							mp_hands.HAND_CONNECTIONS,
							mp_drawing_styles.get_default_hand_landmarks_style(),
							mp_drawing_styles.get_default_hand_connections_style())
					numCycles += 1
					

					if numCycles == cyclesBeforeSwitch:
						if intersection == True:#This occurs if the player succesfully blocks the opponents attack
							pygame.mixer.Sound.play(pygame.mixer.Sound('ClashSound.wav'))
							playerScore += 250
						else: #This occurs if the player couldn't block the opponents attack and gets hit
							pygame.mixer.Sound.play(pygame.mixer.Sound('DeathSound.wav'))
							playerScore -= 250
							numLives -= 1
							cyclesBeforeSwitch -= 10
							printVal = 20 #number of cycles the speed increased text is active


						numCycles = 0
						if swordNumber == 6:
							swordNumber = 0
						else:
							swordNumber += 1
						switchCatch = True
				
				flippedImage = cv2.flip(image, 1)

				if(printVal > 0):
					cv2.putText(flippedImage, speedText, (x, y+75), font, 1, white , 2)
					printVal -= 1

				# Flip the image horizontally for a selfie-view display.
				cv2.putText(flippedImage, livesText + str(numLives), (x+475, y), font, 1, scoreColor , 2)

				cv2.putText(flippedImage, text + str(playerScore), (x, y), font, 1, scoreColor , 2)
				

				cv2.imshow('OPENCV DUEL', flippedImage)

				if numLives == 0:
					
					#--------------For regular computers----------#
					#gameOver = cv2.imread('gameover.png')
					#---------------------------------------------#
					#---------------For macbooks------------------#
					gameOver = cv2.imread('gameoverSize2.png')
					#---------------------------------------------#

					roi = flippedImage
					roi[np.where(mask)] = 0
					roi += gameOver
					cv2.putText(flippedImage, "Final Score: " + str(playerScore), (200, 390), font, 1, white , 2)
					cv2.putText(flippedImage, "Press any key to quit", (200, 430), font, 0.75, white , 2)
					cv2.imshow('OPENCV DUEL', flippedImage)
					gameKill = True
					cv2.waitKey(0)

				if cv2.waitKey(5) & 0xFF == 27:
					break
			cap.release()
	return gameKill

#-----Official Game Code Ends Here-------

#-----Main Menu Code Starts Here---------

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("OPENCV Duel 2022")

BG = pygame.image.load("Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

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
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(pygame.mixer.Sound('MainGameTheme.wav'))
                    SCREEN.fill("black")
                    gameState = play()
                    if gameState == True:
                       pygame.quit()
                       sys.exit()
                    
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

#-----Main Menu Code Ends Here----------

main()



