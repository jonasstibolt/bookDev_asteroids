import pygame, constants, player

def main():
	pygame.init()
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	player_obj = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
	dt = 0

	#start game loop
	print("Starting Asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	while True:
		screen.fill((0, 0, 0))
		player_obj.update(dt)
		player_obj.draw(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = clock.tick(60) / 1000
		pygame.display.flip()

if __name__ == '__main__':
	main()