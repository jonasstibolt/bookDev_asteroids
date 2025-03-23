import pygame, constants, player, asteroid, asteroidfield

def main():
	pygame.init()
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	updateables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	asteroidfield.AsteroidField.containers = (updateables)
	player.Player.containers = (updateables, drawables)
	asteroid.Asteroid.containers = (updateables, drawables, asteroids)

	asteroidfield.AsteroidField()
	player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
	
	dt = 0

	#start game loop
	print("Starting Asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	while True:
		screen.fill((0, 0, 0))
		for obj in updateables:
			obj.update(dt)
		for obj in drawables:
			obj.draw(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = clock.tick(60) / 1000
		pygame.display.flip()

if __name__ == '__main__':
	main()