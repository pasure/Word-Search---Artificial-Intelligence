#import necessary lib
import pygame
import os 
import random
import time
#import puzzel generetor
from word_search_puzzle.utils import display_panel
from word_search_puzzle.algorithms import create_panel

pygame.font.init()
myfont = pygame.font.SysFont("comicsans",40)


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)


WIDTH,HEIGHT = 800,800
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")

blockSize = 80 #Set the size of the grid block
table = [['C','O','N','N','E','C','T','I','O','N'],
            ['F','C','E','L','L','P','H','O','N','E'],
            ['A','R','Z','T','S','P','E','E','C','H'],
            ['C','B','T','M','A','L','U','J','G','G'],
            ['I','A','L','I','F','I','U','G','B','I'],
            ['A','S','E','N','I','H','C','A','M','P'],
            ['L','L','H','P','B','E','J','O','S','H'],
            ['K','R','G','R','J','S','I','R','I','O'],
            ['M','G','Z','D','E','E','P','S','M','N'],
            ['D','I','N','T','E','R','N','E','T','E'] ]
words = ['AI','FACIAL','SPEECH','CONNECTION','INTERNET',
            'IPHONE','SIRI','CELLPHONE',]               #'MACHINES','SPEED'
visited = []

class DFS():
    def __init__(self):
        self.run = True #initial with running state
        self.rootx = 0 #just for keeping root
        self.rooty = 0
        self.x = 0  #for keeping recent search
        self.y = 0
        self.string = ''
        self.dir = 0 #0-3 for directory
        self.directory = ['NorthEast','East','SouthEast','South']
        self.path = []  #in case of highlighting word
    
    def nextRoot(self):
        if(self.rooty < 9):
            self.rooty += 1
        elif(self.rootx < 9):
            self.rooty = 0
            self.rootx += 1
        else:
            self.run = False
            
        #print('Root' + ':' + table[self.rootx][self.rooty])
        self.redraw()

    def search(self):
        #print('x =',self.x,'y = ',self.y,'dir = ',self.dir)
        if(self.x >= 0 and self.x <= 9):
            if (self.y >= 0 and self.y <= 9):
                #print(self.directory[self.dir] + ':' + table[self.x][self.y])
                self.string = self.string + table[self.x][self.y]
                #print(self.string)
                self.redraw()
                if self.string in words:
                    print("------------------------------------------------------")
                    self.path.append(self.string)
                    words.remove(self.string)
                    visited.append(self.string)
                    print(visited)
                    self.dir += 1 
                    if(self.dir > 3):
                        self.dir = 0
                        self.nextRoot()
                    self.x,self.y = self.rootx,self.rooty
                    self.string = ''
                    if(len(words) <= 0):
                        self.run = False
                if (self.dir == 0):
                    #search(PosX-1, PosY+1, string, dir, position)
                    self.x,self.y =  self.x-1,self.y+1
                elif (self.dir == 1):
                    #search(PosX, PosY+1, string, dir, position)
                    self.y =  self.y+1
                elif (self.dir == 2):
                    #search(PosX+1, PosY, string, dir, position)
                    self.x,self.y =  self.x+1,self.y+1
                elif (self.dir == 3):
                    #search(PosX + 1, PosY+1, string, dir, position)
                    self.x =  self.x+1
                
            else:
                self.dir += 1 
                if(self.dir > 3):
                    self.dir = 0
                    self.nextRoot()
                self.x,self.y = self.rootx,self.rooty
                self.string = ''
        else:
            self.dir += 1
            if(self.dir > 3):
                    self.dir = 0
                    self.nextRoot()
            self.x,self.y = self.rootx,self.rooty
            self.string = ''

    def circle(self):
        pygame.draw.circle(SCREEN, (0,0,255), (self.rooty*blockSize+blockSize//4+2,self.rootx*blockSize+blockSize//4+5), blockSize//4,2)
        pygame.draw.circle(SCREEN, (0,255,0), (self.y*blockSize+blockSize//4+2,self.x*blockSize+blockSize//4+5), blockSize//4,2)
  
    def redraw(self):
        SCREEN.fill(BLACK)
        drawGrid()
        self.circle()

        pygame.display.update()

def main():
    FPS = 60
    CLOCK = pygame.time.Clock()
    timer = pygame.time.get_ticks()

    dfs = DFS()

    while True:
        CLOCK.tick(FPS)
        t = pygame.time.get_ticks() - timer
        #print(t)
        if(dfs.run):
            dfs.search()
            timer = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def drawGrid():
    for x in range(10):
        for y in range(10):
            #rect = pygame.Rect(x*blockSize, y*blockSize,blockSize, blockSize)
            #pygame.draw.rect(SCREEN, WHITE, rect, 1)
            textsurface = myfont.render(table[x][y], True, (255, 255, 255)) #text / Anti aliasing / color (in this case it's white)
            SCREEN.blit(textsurface,(y*blockSize+15,x*blockSize+15))

def puzzle_gen():
    global words,table
    words = ['cat', 'bear', 'tiger', 'lion']
    table = [['0' for i in range(10)] for i in range(10)]
    result = create_panel(height=10, width=10, words_value_list=words)

    display_panel(result.get('panel'))
    #convert into 2d array
    for i in range(0,10):
        for j in range(0, 10):
            table[i][j] = result.get('panel').cells[i,j]
    


def s():
    for i in range(0,5):
        for j in range(0, 5):
            print('Root:',i,j)
            DFS(i,j,"")

class IDFS()
    def __init__(self):
        self.run = True #initial with running state
        self.rootx = 0 #just for keeping root
        self.rooty = 0
        self.x = 0  #for keeping recent search
        self.y = 0
        self.string = ''
        self.dir = 0 #0-3 for directory
        self.directory = ['NorthEast','East','SouthEast','South']
        self.path = []  #in case of highlighting word
        self.tmp_round = 0
        self.last_round = 0
    
    def nextRoot(self):
        if(self.rooty < 9):
            self.rooty += 1
        elif(self.rootx < 9):
            self.rooty = 0
            self.rootx += 1
        else:
            self.run = False
        self.redraw()

    def IDDFSSearch(self):
        if(self.tmp_round <= self.last_round):
            if(self.x >= 0 and self.x <= 9):
                if (self.y >= 0 and self.y <= 9):
                    
                    self.string = self.string + table[self.x][self.y]    #Stack
                    print(self.string)
                    time.sleep(0.5)
                    
                    if self.string in words:                     #หาว่า string(stack)ที่ได้จากการ Search ตรงกับคำที่อยู่ใน list หรือไม่
                        global position
                        if self.string not in position:          #ใช้ในการเลือก Save ประโยคที่่ไม่ซ้ำกับประโยคที่มีอยู่แล้ว
                            if(self.dir == 'NorthEast'):
                                position = position + self.string + " at " + str(self.x+len(self.string)-1) + ',' + str(self.y-len(self.string)+1) + ' direction: NorthEast' +'\n'
                            if(self.dir == 'East'):
                                position = position + self.string + " at " + str(self.x) + ',' + str(self.y - len(self.string) + 1) + ' direction: East' +'\n'
                            if(self.dir == 'South'):
                                position = position + self.string + " at " + str(self.x - len(self.string)+1) + ',' + str(self.y) + ' direction: South' +'\n'
                            if (self.dir == 'SouthEast'):
                                position = position + self.string + " at " + str(self.x - len(self.string) + 1) + ',' + str(self.y - len(self.string) + 1) + ' direction: SouthEast' +'\n'
                    if(self.dir == 'NorthEast'):
                        IDDFSSearch(self.x -1, self.y +1, self.string, self.dir, self.tmp_round+1,self.last_round)
                    if (self.dir == 'East'):
                        IDDFSSearch(self.x, self.y+1, self.string, self.dir, self.tmp_round+1, self.last_round)
                    if (self.dir == 'South'):
                        IDDFSSearch(self.x+1, self.y, self.string, self.dir, self.tmp_round+1, self.last_round)
                    if (self.dir == 'SouthEast'):
                        IDDFSSearch(self.x + 1, self.y+1, self.string, self.dir, self.tmp_round+1, self.last_round)
    
    
    def circle(self):
        pygame.draw.circle(SCREEN, (0,0,255), (self.rooty*blockSize+blockSize//4+2,self.rootx*blockSize+blockSize//4+5), blockSize//4,2)
        pygame.draw.circle(SCREEN, (0,255,0), (self.y*blockSize+blockSize//4+2,self.x*blockSize+blockSize//4+5), blockSize//4,2)
  
    def redraw(self):
        SCREEN.fill(BLACK)
        drawGrid()
        self.circle()

        pygame.display.update()
            
main()
