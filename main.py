import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rising Star')

clock = pygame.time.Clock()
FPS = 60

moving_left = False
moving_right = False
moving_up = False
moving_down = False


BG = (33, 26, 30)
def draw_bg():
    screen.fill(BG)



class Player:
    def __init__(self, x, y, scale, health=100):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.health = health
        self.player_img = pygame.image.load('img/player.png')
        self.player_img = pygame.transform.scale(self.player_img, (50, 50))
        self.vel = 1

    def draw(self):
        screen.blit(self.player_img, (self.x, self.y))

    def move(self, moving_left = False, moving_right = False, moving_up = False, moving_down = False):
        # Reset movement variables
        dx = 0
        dy = 0

        print(self.x, self.y)

        # Assign movement variables if moving left or right
        if moving_left:
            dx = -self.vel
        if moving_right:
            dx = self.vel
        if moving_up:
            dy = -self.vel
        if moving_down:
            dy = self.vel

        if self.x + dx < 0:
            dx = 0
        if self.x + 50 + dx > SCREEN_WIDTH:
            dx = 0
        if self.y + dy < 0:
            dy = 0
        if self.y + 50 + dy > SCREEN_HEIGHT:
            dy = 0
        
        


        # Update player coordinates
        self.x += dx
        self.y += dy

player = Player(200, 200, 1)

run = True
while run:
    draw_bg()
    player.draw()
    player.move(moving_left, moving_right, moving_up, moving_down)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moving_up = True
                print('up')
            if event.key == pygame.K_a:
                moving_left = True
                print('left')
            if event.key == pygame.K_s:
                moving_down = True
                print('down')
            if event.key == pygame.K_d:
                moving_right = True
                print('right')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                moving_up=False
            if event.key == pygame.K_a:
                moving_left=False
            if event.key == pygame.K_s:
                moving_down=False
            if event.key == pygame.K_d:
                moving_right=False

        
    pygame.display.update()
pygame.quit()
