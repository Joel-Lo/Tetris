import pygame, sys, random, signal, shutil
from game import Game
from colors import Colors

class Font:
    BOLD = '\033[1m'
    END = '\033[0m'

class Color:
    GREEN = '\033[32m'
    RESET = '\033[0m'

print()

width = shutil.get_terminal_size().columns

print(
    f"{Color.GREEN}{Font.BOLD}"
    + '╔════════════════════════════════════════════════════════════╗'.center(width)
    + '\n'
    + '║                          Tetris                            ║'.center(width)
    + '\n'
    + '╚════════════════════════════════════════════════════════════╝'.center(width)
    + f"{Font.END}{Color.RESET}"
)

print()

song = input ("Select music: \n1. Golden (Huntr/x) \n2. Golden (BABYMONSTER) \n3. We Go Up \n4. Wild \n5. Mix \n6. Champion \n7. Dream \n8. Sugar Honey Ice Tea \n9. Random \n\nOption: ")

songRan = None

if song in ("Random", "9"):
	songRan = random.randint(1,8)

if song in ("Golden (Huntr/x)", "1") or songRan == "1":
    convsongname = "Golden"
    convsongaut = "Huntr/x"
elif song in ("Golden (BABYMONSTER)", "2") or songRan == "2":
    convsongname = "Golden"
    convsongaut = "BABYMONSTER"
elif song in ("We Go Up", "3") or songRan == "3":
    convsongname = "We Go Up"
    convsongaut = "BABYMONSTER"
elif song in ("Wild", "4") or songRan == "4":
    convsongname = "Wild"
    convsongaut = "BABYMONSTER"
elif song in ("Mix", "5") or songRan == "5":
    convsongname = "Mix"
    convsongaut = "Huntr/x & BABYMONSTER"
elif song in ("Champion", "6") or songRan == "6":
    convsongname = "Champion"
    convsongaut = "BLACKPINK"
elif song in ("Dream", "7") or songRan == "7":
    convsongname = "Dream"
    convsongaut = "BABYMONSTER"
elif song in ("Sugar Honey Ice Tea", "8") or songRan == "8":
    convsongname = "Sugar Honey Ice Tea"
    convsongaut = "BABYMONSTER"
else:
    convsongname = "Golden"
    convsongaut = "Huntr/x"


title = f"Tetris: Classic Mode | OST: {convsongname} by {convsongaut}"
pygame.display.set_caption(title)

if song in ("Golden (Huntr/x)", "1") or songRan == "1":
	pygame.mixer.pre_init(44100,-16,2,512)
	pygame.init()
	pygame.mixer.music.load("Golden - KPop Demon Hunters.ogg")
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(1)
	print("Activating Golden by Huntr/x")
	print()
	print("Loading Game...")
elif song in ("Golden (BABYMONSTER)", "2") or songRan == "2":
	pygame.mixer.pre_init(44100,-16,2,512)
	pygame.init()
	pygame.mixer.music.load("Golden - BABYMONSTER VER.ogg")
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(1)
	print("Activating Golden by BABYMONSTER")
	print()
	print("Loading Game...")
elif song in ("We Go Up", "3") or songRan == "3":
	pygame.mixer.pre_init(44100,-16,2,512)
	pygame.init()
	pygame.mixer.music.load("We Go Up.ogg")
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(1)
	print("Activating We Go Up by BABYMONSTER")
	print()
	print("Loading Game...")
elif song in ("Wild", "4") or songRan == "4":
	pygame.mixer.pre_init(44100,-16,2,512)
	pygame.init()
	pygame.mixer.music.load("Wild.ogg")
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(1)
	print("Activating Wild by BABYMONSTER")
	print()
	print("Loading Game...")
elif song in ("Mix", "5") or songRan == "5":
	pygame.mixer.pre_init(44100,-16,2,512)
	pygame.init()
	pygame.mixer.music.load("Mix.ogg")
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(1)
	print("Activating Mix by Huntr/x & BABYMONSTER")
	print()
	print("Loading Game...")
elif song in ("Champion", "6") or songRan == "6":
	pygame.mixer.pre_init(44100,-16,2,512)
	pygame.init()
	pygame.mixer.music.load("Champion.ogg")
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(1)
	print("Activating Champion by BLACKPINK")
	print()
	print("Loading Game...")
elif song in ("Dream", "7") or songRan == "7":
	pygame.mixer.pre_init(44100,-16,2,512)
	pygame.init()
	pygame.mixer.music.load("Dream.ogg")
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(1)
	print("Activating Dream by BABYMONSTER")
	print()
	print("Loading Game...")
elif song in ("Sugar Honey Ice Tea", "8") or songRan == "8":
	pygame.mixer.pre_init(44100,-16,2,512)
	pygame.init()
	pygame.mixer.music.load("Sugar Honey Ice Tea.ogg")
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(1)
	print("Activating Sugar Honey Ice Tea by BABYMONSTER")
	print()
	print("Loading Game...")
else:
	pygame.mixer.pre_init(44100,-16,2,512)
	pygame.init()
	pygame.mixer.music.load("We Go Up.ogg")
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(0.1)
	print("Activating We Go Up by BABYMONSTER")
	print()
	print("Loading Game...")

def sigint_handler(sig, frame): 
	if song in ("Golden (Huntr/x)", "1") or songRan == "1":
		print("\nStopping game...")
		print()
		print("Deactivating Golden by Huntr/x...") 
		print()
		print("Game & Music deactivated")
		pygame.quit() 
		sys.exit(0) 
	elif song in ("Golden (BABYMONSTER)", "2") or songRan == "2":
		print("\nStopping game...")
		print()
		print("Deactivating Golden by BABYMONSTER...")
		print()
		print("Game & Music deactivated")
		pygame.quit() 
		sys.exit(0) 
	elif song in ("We Go Up", "3") or songRan == "3":
		print("\nStopping game...")
		print()
		print("Deactivating We Go Up by BABYMONSTER...")
		print()
		print("Game & Music deactivated")
		pygame.quit() 
		sys.exit(0)
	elif song in ("Wild", "4") or songRan == "4":
		print("\nStopping game...")
		print()
		print("Deactivating Wild by BABYMONSTER...") 
		print()
		print("Game & Music deactivated")
		pygame.quit() 
		sys.exit(0)
	elif song in ("Mix", "5") or songRan == "5":
		print("\nStopping game...")
		print()
		print("Deactivating Mix by Huntr/x & BABYMONSTER...") 
		print()
		print("Game & Music deactivated")
		pygame.quit() 
		sys.exit(0)
	elif song in ("Champion", "6") or songRan == "6":
		print("\nStopping game...")
		print()
		print("Deactivating Champion by BLACKPINK...") 
		print()
		print("Game & Music deactivated")
		pygame.quit() 
		sys.exit(0)
	elif song in ("Dream", "7") or songRan == "7":
		print("\nStopping game...")
		print()
		print("Deactivating Dream by BABYMONSTER...") 
		print()
		print("Game & Music deactivated")
		pygame.quit() 
		sys.exit(0)
	elif song in ("Sugar Honey Ice Tea", "8") or songRan == "8":
		print("\nStopping game...")
		print()
		print("Deactivating Sugar Honey Ice Tea by BABYMONSTER...") 
		print()
		print("Game & Music deactivated")
		pygame.quit() 
		sys.exit(0)
	else:
		print("\nStopping game...")
		print()
		print("Deactivating We Go Up by BABYMONSTER...") 
		print()
		print("Game & Music deactivated")
		pygame.quit() 
		sys.exit(0)
	
signal.signal(signal.SIGINT, sigint_handler)

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if game.game_over == True:
				game.game_over = False
				game.reset()
			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
				game.update_score(0, 1)
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()
		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()

	score_value_surface = title_font.render(str(game.score), True, Colors.white)

	screen.fill(Colors.dark_blue)
	screen.blit(score_surface, (365, 20, 50, 50))
	screen.blit(next_surface, (375, 180, 50, 50))

	if game.game_over == True:
		screen.blit(game_over_surface, (320, 450, 50, 50))

	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
		centery = score_rect.centery))
	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
	game.draw(screen)

	pygame.display.update()
	clock.tick(60)