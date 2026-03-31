import time, random

class timer():

    def __init__(self):
        self.elapsed=0
        self.running=False
        self.start_time= 0

    def start(self):
        if not self.running:
            self.running=True
            self.start_time= time.time()

    def pause(self):
        if self.running:
            self.elapsed += ((time.time()) - self.start_time)
            self.running=False

    def get_time(self):
        if self.running:
            return self.elapsed + ((time.time()) - self.start_time)
        return self.elapsed

class game():
    def __init__(self):
        self.gamestate='Menu'
        self.timer= timer()

class enemy():
    def __init__(self, mini, maxi):
        self.strength= random.randint(mini, maxi)


e = enemy(50, 70)
print(e.strength)
    
