import random, pygame



class Game:
    def __init__(self):
        self.gamestate='Menu'
        self.elapsed=0
        self.running=False
        self.start_time= 0

    def total_time(self):
        if self.running:
            return self.elapsed + ((pygame.time.get_ticks()) - self.start_time)
        return self.elapsed
    
    def main(self):
        self.gamestate='Main'
        if not self.running:
            self.running=True
            self.start_time= pygame.time.get_ticks()
    def pause(self):
        self.gamestate='Pause'
        if self.running:
            self.elapsed += ((pygame.time.get_ticks()) - self.start_time)
            self.running=False

    def end(self):
        self.gamestate='END'
        self.pause()
        
        return self.total_time()

    




class enemy:
    def __init__(self, mini, maxi):
        self.strength= random.randint(mini, maxi)








class session:
    def __init__(self, game, surplus):
        #self.troops = ((game.total_time())/60)
        self.troops = 0
        self.surplus = surplus
        
    def result(self, enemy):
        if ((self.troops + self.surplus) > enemy.strength):
            round_result= 'WIN'
            self.surplus = ((self.troops + self.surplus)- enemy.strength)
        elif ((self.troops + self.surplus) == enemy.strength):
            round_result= 'DRAW'
            self.surplus = 0
        else:
            round_result= 'LOSE'
            self.surplus = 0
        return round_result, self.surplus

        
'''
if __name__ == "__main__":
    g= game()

    minim=int(input((f"{g.gamestate}\n Enter the min focus amount for your session:\t")))
    maxim= int(input("Enter max:\t"))

    e= enemy(minim, maxim)
    print("\nEnemy strength is:\t", e.strength)

    ch= int(input("Enter 0 to start:\t"))
    
    if ch==0:
        tim= int(input("Enter mins focused:\t"))
        sesh = session(g, 0)
        sesh.troops= tim
        result, surplus = sesh.result(e)
        print(result, surplus)
'''