import pygame

# Initialize pygame
pygame.init()

# Set the screen size
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the image file
image = pygame.image.load("image.png")

# Set the initial position of the image
x = 0
y = 0

# Set the speed of the animation
speed_x = 2
speed_y = 2

# Run the animation loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Move the image
    x += speed_x
    y += speed_y

    if x > WIDTH or x < 0:
        speed_x = -speed_x
    if y > HEIGHT or y < 0:
        speed_y = -speed_y

    # Draw the image
    screen.blit(image, (x, y))

    # Update the screen
    pygame.display.flip()

    # Delay to control the animation speed
    pygame.time.delay(20)

# Quit pygame
pygame.quit()
