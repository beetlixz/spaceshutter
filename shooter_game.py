        #Створи власний Шутер!
from models import *


clock = time.Clock()

display.set_caption('Шутер крутий')
background = transform.scale(image.load('galaxy.jpg'), WIN_SIZE)

player = Player('rocket.png', WIN_SIZE[0] / 2 - SPRITE_SIZE[0] / 2, WIN_SIZE[1] - SPRITE_SIZE[1], 5)

mixer.init()
space = mixer.music.load('space.ogg')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

enemies = sprite.Group()
for i in range(5):
    enemies.add(Enemy('asteroid.png', randint(0, WIN_SIZE[0] - SPRITE_SIZE[0]), randint(-100, 0), randint(3, 5), DOWN))

ufo = sprite.Group()
for i in range(3):
    ufo.add(Enemy('ufo.png', randint(WIN_SIZE[0], WIN_SIZE[0] + 100), randint(0, WIN_SIZE[1] - (SPRITE_SIZE[1] * 2 - 20)), 5, LEFT))

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background,(0, 0))

        player.move()
        player.reset()
        player.fire()

        bullets.update()
        bullets.draw(window)

        enemies.draw(window)
        enemies.update()
        ufo.draw(window)
        ufo.update()

        for enemy in enemies:
            for bullet in bullets:
                if sprite.collide_rect(enemy, bullet):
                    enemy.kill()
                    bullet.kill()
                    counter.died_enemy += 1
        
                    enemies.add(Enemy('asteroid.png', randint(0, WIN_SIZE[0] - SPRITE_SIZE[0]), randint(-100, 0), randint(3, 5), DOWN))

        counter.show()

        if counter.died_enemy >= 10:
            finish = True
            window.blit(win, (WIN_SIZE[0] / 2, WIN_SIZE[1] / 2))
        elif counter.lost_enemy >= 10 or sprite.spritecollide(player, enemies, False):
            finish = True
            window.blit(lose, (WIN_SIZE[0] / 2, WIN_SIZE[1] / 2))
    
    
    display.update()
    clock.tick(FPS)


