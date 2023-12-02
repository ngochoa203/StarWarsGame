import pygame
import sys
import random

class StarWars:
    class Enemy:
        def __init__(self, x, y, speed_x, speed_y, enemy_type):
            self.enemy_type = enemy_type

            if enemy_type == "normal":
                self.img = pygame.image.load("D:\VKU\ComputerGraphic\Code Graphic\GamePython\StarWars\Image\plane_enemy.png")
                self.img = pygame.transform.scale(self.img, (50, 50))
                self.hp = 1
            elif enemy_type == "strong":
                self.img = pygame.image.load("D:\VKU\ComputerGraphic\Code Graphic\GamePython\StarWars\Image\plane_enemy_strong.png")
                self.img = pygame.transform.scale(self.img, (60, 60))
                self.hp = 2
            elif enemy_type == "fast":
                self.img = pygame.image.load("D:\VKU\ComputerGraphic\Code Graphic\GamePython\StarWars\Image\plane_enemy_fast.png")
                self.img = pygame.transform.scale(self.img, (40, 40))
                self.hp = 1
            elif enemy_type == "heavy":
                self.img = pygame.image.load("D:\VKU\ComputerGraphic\Code Graphic\GamePython\StarWars\Image\plane_enemy_heavy.png")
                self.img = pygame.transform.scale(self.img, (70, 70))
                self.hp = 3
            elif enemy_type == "agile":
                self.img = pygame.image.load("D:\VKU\ComputerGraphic\Code Graphic\GamePython\StarWars\Image\plane_enemy_agile.png")
                self.img = pygame.transform.scale(self.img, (45, 45))
                self.hp = 1
            elif enemy_type == "boss":
                self.img = pygame.image.load("D:\VKU\ComputerGraphic\Code Graphic\GamePython\StarWars\Image\plane_enemy_boss.png")
                self.img = pygame.transform.scale(self.img, (100, 100))
                self.hp = 20
                
            self.bullet_color = (255, 255, 255)
            self.bullets = []
            self.bullet_speed = 1
            self.last_bullet_time = pygame.time.get_ticks()
            self.bullet_delay = 2000

            self.rect = self.img.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed_x = speed_x
            self.speed_y = speed_y

        def shoot_bullet(self):
            bullet_x = self.rect.x + self.rect.width // 2 - 3
            bullet_y = self.rect.y + self.rect.height
            return [bullet_x, bullet_y]

    class Item:
        def __init__(self, x, y, item_type):
            if item_type == "heart":
                self.img = pygame.image.load("D:\VKU\ComputerGraphic\Code Graphic\GamePython\StarWars\Image\heart.png")
                self.img = pygame.transform.scale(self.img, (30, 30))
            elif item_type == "double_bullets":
                self.img = pygame.image.load("D:\VKU\ComputerGraphic\Code Graphic\GamePython\StarWars\Image\double_bullets.png")
                self.img = pygame.transform.scale(self.img, (30, 30))
            self.rect = self.img.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.item_type = item_type

    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.white = (255, 255, 255)
        self.blue = (0, 128, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)

        self.background_img = pygame.image.load("D:\VKU\ComputerGraphic\Code Graphic\GamePython\StarWars\Image\Background.jpg")
        self.background_img = pygame.transform.scale(self.background_img, (self.width, self.height))

        self.player_img = pygame.image.load("D:\VKU\ComputerGraphic\Code Graphic\GamePython\StarWars\Image\plane.png")
        self.player_img = pygame.transform.scale(self.player_img, (100, 100))
        self.player_rect = self.player_img.get_rect()
        self.player_rect.x = self.width // 2 - self.player_rect.width // 2
        self.player_rect.y = self.height - 2 * self.player_rect.height
        self.player_speed = 5

        self.bullet_size = 8
        self.bullet_speed = 10
        self.bullets = []
        self.bullet_delay = 300
        self.last_bullet_time = pygame.time.get_ticks()
        self.double_bullet_duration = 0

        self.enemies = []

        self.item_size = 30
        self.items = []

        self.score = 0
        self.max_hp = 2
        self.hp = self.max_hp
        self.font = pygame.font.Font(None, 36)
        self.score_text = self.font.render("Score: {}".format(self.score), True, self.blue)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.topleft = (10, self.height - 40)

        self.hp_text = self.font.render("HP: {}".format(self.hp), True, self.red)
        self.hp_rect = self.hp_text.get_rect()
        self.hp_rect.topleft = (10, self.height - 80)
        
    def draw_bullet(self, x, y, color):
        pygame.draw.rect(self.screen, color, (x, y, self.bullet_size, self.bullet_size))
        
    def draw_enemy(self, enemy):
        self.screen.blit(enemy.img, enemy.rect)

    def draw_item(self, item):
        self.screen.blit(item.img, item.rect)

    def draw_score(self):
        self.screen.blit(self.score_text, self.score_rect)
        self.screen.blit(self.hp_text, self.hp_rect)

    def spawn_enemy(self):
        if len(self.enemies) < 5:
            enemy_type = random.choice(["normal", "strong", "fast", "heavy", "agile"])
            enemy_x = random.randint(0, self.width - 50)
            enemy_y = -50
            enemy_speed_x = random.uniform(-1, 1)
            enemy_speed_y = random.uniform(0.5, 1)
            self.enemies.append(self.Enemy(enemy_x, enemy_y, enemy_speed_x, enemy_speed_y, enemy_type))

    def spawn_boss(self):
        if len([enemy for enemy in self.enemies if enemy.enemy_type == "boss"]) < 1:
            boss_x = self.width // 2 - 50
            boss_y = -50
            boss_speed_x = 0
            boss_speed_y = random.uniform(0.5, 1)
            self.enemies.append(self.Enemy(boss_x, boss_y, boss_speed_x, boss_speed_y, "boss"))

    def show_game_over_screen(self):
        game_over_font = pygame.font.Font(None, 64)
        game_over_text = game_over_font.render("Game Over", True, self.red)
        game_over_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2))

        press_enter_font = pygame.font.Font(None, 36)
        press_enter_text = press_enter_font.render("Press Enter to play again", True, self.white)
        press_enter_rect = press_enter_text.get_rect(center=(self.width // 2, self.height // 2 + 50))

        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(press_enter_text, press_enter_rect)
        pygame.display.flip()

        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting_for_key = False

            self.clock.tick(5)
    def reset_game(self):
        self.bullets = []
        self.enemies = []
        self.items = []
        self.score = 0
        self.hp = self.max_hp
        self.score_text = self.font.render("Score: {}".format(self.score), True, self.blue)
        self.hp_text = self.font.render("HP: {}".format(self.hp), True, self.red)
        self.player_rect.x = self.width // 2 - self.player_rect.width // 2
        self.player_rect.y = self.height - 2 * self.player_rect.height

    def run(self):
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.reset_game()

            if not playing:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.player_rect.x > 0:
                self.player_rect.x -= self.player_speed
            if keys[pygame.K_RIGHT] and self.player_rect.x < self.width - self.player_rect.width:
                self.player_rect.x += self.player_speed
            if keys[pygame.K_UP] and self.player_rect.y > 0:
                self.player_rect.y -= self.player_speed
            if keys[pygame.K_DOWN] and self.player_rect.y < self.height - self.player_rect.height:
                self.player_rect.y += self.player_speed

            current_time = pygame.time.get_ticks()
            if current_time - self.last_bullet_time > self.bullet_delay:
                bullet_x = self.player_rect.x + self.player_rect.width // 2 - self.bullet_size // 2
                bullet_y = self.player_rect.y
                self.bullets.append((bullet_x, bullet_y))
                if self.double_bullet_duration > 0:
                    self.bullets.append((bullet_x - 10, bullet_y))
                    self.bullets.append((bullet_x + 10, bullet_y))
                self.last_bullet_time = current_time

            if self.double_bullet_duration > 0:
                self.double_bullet_duration -= self.clock.get_rawtime()

            self.bullets = [(x, y - self.bullet_speed) for x, y in self.bullets if 0 <= y <= self.height]

            if random.randint(0, 100) < 2:
                self.spawn_enemy()

            if self.score >= 1 and self.score % 10 == 0 and not any(enemy.enemy_type == "boss" for enemy in self.enemies):
                self.spawn_boss()

            for enemy in self.enemies:
                enemy.rect.x += enemy.speed_x
                enemy.rect.y += enemy.speed_y
                if enemy.rect.x < 0:
                    enemy.rect.x = 0
                    enemy.speed_x = abs(enemy.speed_x)
                elif enemy.rect.x > self.width - enemy.rect.width:
                    enemy.rect.x = self.width - enemy.rect.width
                    enemy.speed_x = -abs(enemy.speed_x)

                if enemy.rect.y > self.height:
                    self.enemies.remove(enemy)

                if enemy.enemy_type == "boss" and current_time - enemy.last_bullet_time > enemy.bullet_delay:
                    enemy.bullets.append(enemy.shoot_bullet())
                    enemy.last_bullet_time = current_time

                for enemy in self.enemies:
                    if enemy.enemy_type == "boss":
                        bullets_to_remove = []
                        for i in range(len(enemy.bullets)):
                            bullet_x, bullet_y = enemy.bullets[i]
                            pygame.draw.rect(self.screen, enemy.bullet_color, (bullet_x, bullet_y, self.bullet_size, self.bullet_size))
                            bullet_y += enemy.bullet_speed
                            enemy.bullets[i] = (bullet_x, bullet_y)
                            if bullet_y > self.height:
                                bullets_to_remove.append(i)
                            if self.player_rect.colliderect(pygame.Rect(bullet_x, bullet_y, self.bullet_size, self.bullet_size)):
                                bullets_to_remove.append(i)
                                self.hp -= 1
                                self.hp_text = self.font.render("HP: {}".format(self.hp), True, self.red)
                        for index in reversed(bullets_to_remove):
                            enemy.bullets.pop(index)

            if random.randint(0, 1000) < 1:
                item_x = random.randint(0, self.width - self.item_size)
                item_y = -self.item_size
                item_type = random.choice(["heart", "double_bullets"])
                self.items.append(self.Item(item_x, item_y, item_type))

            for item in self.items:
                item.rect.y += 2

                if self.player_rect.colliderect(item.rect):
                    self.items.remove(item)
                    if item.item_type == "heart":
                        self.hp = min(self.hp + 1, self.max_hp)
                        self.hp_text = self.font.render("HP: {}".format(self.hp), True, self.red)
                    elif item.item_type == "double_bullets":
                        self.double_bullet_duration = 1000

            bullets_to_remove = []
            enemies_to_remove = []
            for bullet in self.bullets:
                for enemy in self.enemies:
                    if enemy.rect.colliderect(pygame.Rect(bullet[0], bullet[1], self.bullet_size, self.bullet_size)):
                        bullets_to_remove.append(bullet)
                        enemy.hp -= 1
                        if enemy.hp <= 0:
                            if enemy.enemy_type == "boss":
                                enemies_to_remove.append(enemy)
                            else:
                                self.enemies.remove(enemy)
                                self.score += 1
                                self.score_text = self.font.render("Score: {}".format(self.score), True, self.blue)
                                if enemy.bullet_color:
                                    self.draw_bullet(bullet[0], bullet[1], enemy.bullet_color)

            self.bullets = [bullet for bullet in self.bullets if bullet not in bullets_to_remove]
            self.enemies = [enemy for enemy in self.enemies if enemy not in enemies_to_remove]

            for enemy in self.enemies:
                if self.player_rect.colliderect(enemy.rect):
                    self.enemies.remove(enemy)
                    self.hp -= 1
                    self.hp_text = self.font.render("HP: {}".format(self.hp), True, self.red)

            if self.hp <= 0:
                self.show_game_over_screen()
                waiting_for_key = True
                while waiting_for_key:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            playing = False
                            waiting_for_key = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                waiting_for_key = False
                                self.reset_game()

            self.screen.blit(self.background_img, (0, 0))
            for bullet in self.bullets:
                self.draw_bullet(bullet[0], bullet[1], (255, 0, 0))
            for enemy in self.enemies:
                self.draw_enemy(enemy)
            for item in self.items:
                self.draw_item(item)
            for enemy in self.enemies:
                if enemy.enemy_type == "boss":
                    for bullet in enemy.bullets:
                        bullet_x, bullet_y = bullet
                        pygame.draw.rect(self.screen, enemy.bullet_color, (bullet_x, bullet_y, self.bullet_size, self.bullet_size))
            self.screen.blit(self.player_img, self.player_rect)
            self.draw_score()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = StarWars()
    game.run()
