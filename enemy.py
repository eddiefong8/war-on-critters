class Enemy:
    def __init__(self, type, speed, direction, x, y):
        self.type = type
        self.speed = speed
        self.direction = direction
        self.x = x
        self.y = y

    def getSprite(self):
        if self.type == 'wolf':
            return 'wolf.png'
        elif self.type == 'bear':
            return 'bear.png'
        elif self.type == 'ram':
            return 'ram.png'
        else:
            return 'snake.png'

    def move(self):
        if(self.direction == 'v'):
            if(self.y < 0):
                self.y = 600
            self.y -= self.speed
        if (self.direction == 'h'):
            if (self.x > 800):
                self.x = 0
            self.x += self.speed
            
    def checkKill(self, x, y):
        if (x - 25) < self.x < (x + 25) and (y - 25) < self.y < (y + 25):
            return True
        return False


