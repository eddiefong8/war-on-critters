# Names/IDS: Tejas Charaipotra (wzk5we), Eddie Fong(vgw3fr)
# Game name: War on the critters
# Description: Our game is like Whack-A-Mole. Different enemies will appear at various points on the screen at
# various times. The player's job is to hit(click) the enemies and will be rewarded with points each time they
# accurately "hit" an enemy.

# 3 basic features:
# 1. User Input: The user will click the screen to kill the enemies.
# 2. Game Over: There is a timer and the game ends when the time runs out. Once the time runs out you lose.
# 3. Graphics/Images: The "enemies" you are killing will be images of different animals.

# 4 additional features:
# 1. Restart from Game Over- When you lose/run out of time you can restart the game with one simple click of a button
# 2. Enemies- The enemies are moving around the screen and you try to kill them to increase your points.
# The enemies move to try and hinder your ability to gain points.
# 3. Timer- There will be a timer letting the user know how much time they have left to kill enemies.
# TODO 4. Object-Oriented Code- (changed from sprite animation) our enemies with different attributes are made from the enemy class
import uvage, random, enemy

camera = uvage.Camera(800, 600)
def setup():
    #sets up game by initializing instances of enemy class and also setting variables to default start value
    global running, time, timeDisplay, tickNum, score, scoreDisplay, enemies, options, enemy1, enemy2, enemy3, enemy4, title
    running = True
    time = 30
    tickNum = 0
    score = 0
    scoreDisplay = uvage.from_text(50, 50, str(score), 50, 'red', True)
    enemy1 = enemy.Enemy('wolf', random.randint(5, 20), 'h', random.randint(50,750), random.randint(50,550))
    enemy2 = enemy.Enemy('snake', random.randint(5, 20), 'v', random.randint(50,750), random.randint(50,550))
    enemy3 = enemy.Enemy('ram', random.randint(5, 20), 'h', random.randint(50,750), random.randint(50,550))
    enemy4 = enemy.Enemy('bear', random.randint(5, 20), 'v', random.randint(50,750), random.randint(50,550))
    enemies = [enemy1, enemy2, enemy3, enemy4]
    options = [
    ['wolf', 'snake', 'ram', 'bear'],
    ['h', 'v']
    ]
    title = uvage.from_text(400, 50, 'WAR ON CRITTERS', 50, 'red', True)

def moveEnemies():
    #uses enemy class to move each enemy and get picture of animal from local file
    global enemies
    for i in enemies:
        i.move()
        mole = uvage.from_image(i.x, i.y, i.getSprite())
        mole.scale_by(0.5)
        camera.draw(mole)

def timer():
    #increments number of ticks and loop ticks 30 times per second, therefore when tickNum is a multiple of 30,
    # it will subtract one from the timer
    global time, timeDisplay, tickNum
    tickNum += 1
    if tickNum % 30 == 0:
        time -= 1
    timeDisplay = uvage.from_text(750, 50, str(time), 50, 'red', True)
    camera.draw(timeDisplay)

def update_score():
    #checks if mouse click occurs, if it occurs it checks if the mouse position overlaps with the enemy
    #using method from the enemy class, then kills enemy, increments score, and spawns new random enemy,
    #displaying new updated score
    global score, scoreDisplay, enemies, options, newEnemy
    if camera.__getattr__('mouseclick'):
        for i in enemies:
            if i.checkKill(camera.mousex, camera.mousey):
                enemies.remove(i)
                score += 1
                newEnemy = enemy.Enemy(options[0][random.randint(0,3)], random.randint(5, 20),
                                       options[1][random.randint(0,1)], random.randint(50,750), random.randint(50,550))
                enemies.append(newEnemy)
    scoreDisplay = uvage.from_text(50, 50, str(score), 50, 'red', True)
    camera.draw(scoreDisplay)

def gameover():
    #checks if time has run out, if it has, game stops and displays gameover and restart option
    global time, running
    if time == 0:
        running = False
        camera.draw(uvage.from_text(400, 300, 'GAME OVER', 50, 'red', True))
        camera.draw(uvage.from_text(400, 355, 'Press Any Mouse Key to Restart!', 50, 'red', True))

def restart():
    #restarts game and changes values to default start values
    global running, score, time, enemies
    if camera.__getattr__('mouseclick'):
        running = True
        score = 0
        time = 30
        enemies = [enemy1, enemy2, enemy3, enemy4]
def tick():
    #calls all functions needed to run game
    if running:
        camera.clear('black')
        moveEnemies()
        timer()
        update_score()
        gameover()
        camera.draw(title)
    else:
        #calls restart method only if game is not running
        restart()
    camera.display()

setup()
uvage.timer_loop(30, tick)
