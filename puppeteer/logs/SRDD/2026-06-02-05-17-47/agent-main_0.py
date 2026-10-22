import pygame
import sys
import json
import os

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 50
PLAYER_SIZE = 50

# Set up some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the player and blocks
class Player:
    def __init__(self):
        self.x = 100
        self.y = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

# Create a player and some blocks
class Game:
    def __init__(self):
        self.player = Player()
        self.blocks = []
        self.level_data = self.load_level_data()

    def load_level_data(self):
        try:
            with open('level_data.json', 'r') as f:
                level_data = json.load(f)
                blocks = []
                for block_data in level_data["blocks"]:
                    blocks.append(Block(block_data["x"], block_data["y"]))
                return {
                    "level": level_data["level"],
                    "blocks": blocks
                }
        except FileNotFoundError:
            print("Level data file not found. Creating a new level.")
            return {
                "level": 1,
                "blocks": [
                    {"x": 200, "y": 200},
                    {"x": 300, "y": 200},
                    {"x": 400, "y": 200}
                ]
            }

    def draw(self, screen):
        screen.fill(WHITE)
        for block in self.blocks:
            block.draw(screen)
        pygame.draw.rect(screen, (0, 0, 255), (self.player.x, self.player.y, PLAYER_SIZE, PLAYER_SIZE))
        text = font.render("Player X: " + str(self.player.x) + ", Player Y: " + str(self.player.y), True, (0, 0, 0))
        screen.blit(text, (10, 10))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(-50, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(50, 0)
                elif event.key == pygame.K_UP:
                    self.player.move(0, -50)
                elif event.key == pygame.K_DOWN:
                    self.player.move(0, 50)

        # Check for collisions with blocks
        for block in self.blocks:
            if (self.player.x < block.x + BLOCK_SIZE and
                self.player.x + PLAYER_SIZE > block.x and
                self.player.y < block.y + BLOCK_SIZE and
                self.player.y + PLAYER_SIZE > block.y):
                print("Collision detected!")

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

    def run(self):
        while True:
            self.update()
            self.draw(screen)

if __name__ == "__main__":
    game = Game()
    game.run()