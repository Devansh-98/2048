# 2048 game using tkinter library of python3


from tkinter import *
import random
from tkinter import messagebox

# Class for tiles.
class tiles:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_info(self):
        return [self.x, self.y, self.text]

    def draw_tiles(self, canvas, val):
         if(val == 0):
            canvas.create_rectangle(
                self.x, self.y, self.x + 100, self.y + 100, fill="white")
         else:
            canvas.create_rectangle(
                self.x, self.y, self.x + 100, self.y + 100, fill=color[val])
            canvas.create_text((2 * (self.x) + 100) / 2,
                               (2 * (self.y) + 100) / 2, text=self.text)

# Function for all blocks up if possible.
def move_up(canvas):
    flag=False
    global void_pos
    global l
    global curr_score
    global curr_score_val
    global max_score
    global max_score_val
    for j in range(4):
        k=0
        for i in range(4):
            if(l[i*4+j]course!=0):
                l[k*4+j]=l[i*4+j]
                if(i!=k):
                    flag=True
                    l[i*4+j]=0
                k+=1
    for j in range(4):
        for i in range(3):
            if(l[i*4+j]==l[(i+1)*4+j] and l[i*4+j]!=0):
                l[i*4+j]=2*l[i*4+j]
                curr_score_val=curr_score_val+'+'+str(l[i*4+j])
                max_score_val=str(max(eval(max_score_val),eval(curr_score_val)))
                curr_score.set(str(eval(curr_score_val)))
                max_score.set(max_score_val)
                l[(i+1)*4+j]=0
                flag=True
    for j in range(4):
        k=0
        for i in range(4):
            if(l[i*4+j]!=0):
                l[k*4+j]=l[i*4+j]
                if(i!=k):
                    flag=True
                    l[i*4+j]=0
                k+=1
    if flag!=False:
        vacant=[]
        for i in range(16):
            if l[i]==0:
                vacant.append(i)
        temp=random.sample(vacant,1)[0]
        val=random.sample([2,4],1)[0]
        l[temp]=val


    for i in range(4):
        y = i * 100+100
        for j in range(4):
            x = j * 100
            tile = tiles(x, y, l[i*4+j])
            tile.draw_tiles(canvas, l[i*4+j])

# Function for all blocks down if possible.
def move_down(canvas):
    flag=False
    global void_pos
    global l
    global curr_score
    global curr_score_val
    global max_score
    global max_score_val
    for j in range(4):
        k=3
        for i in [3,2,1,0]:
            if(l[i*4+j]!=0):
                l[k*4+j]=l[i*4+j]
                if(i!=k):
                    flag=True
                    l[i*4+j]=0
                k-=1
    for j in range(4):
        for i in [3,2,1]:
            if(l[i*4+j]==l[(i-1)*4+j] and l[i*4+j]!=0):
                l[i*4+j]=2*l[i*4+j]
                curr_score_val=curr_score_val+'+'+str(l[i*4+j])
                max_score_val=str(max(eval(max_score_val),eval(curr_score_val)))
                curr_score.set(str(eval(curr_score_val)))
                max_score.set(max_score_val)
                l[(i-1)*4+j]=0
                flag=True
    for j in range(4):
        k=3
        for i in [3,2,1,0]:
            if(l[i*4+j]!=0):
                l[k*4+j]=l[i*4+j]
                if(i!=k):
                    flag=True
                    l[i*4+j]=0
                k-=1
    if flag!=False:
        vacant=[]
        for i in range(16):
            if l[i]==0:
                vacant.append(i)
        temp=random.sample(vacant,1)[0]
        val=random.sample([2,4],1)[0]
        l[temp]=val
    for i in range(4):
        y = i * 100+100
        for j in range(4):
            x = j * 100
            tile = tiles(x, y, l[i*4+j])
            tile.draw_tiles(canvas, l[i*4+j])


# Function for all blocks left if possible.
def move_left(canvas):
    flag=False
    global void_pos
    global l
    global curr_score
    global curr_score_val
    global max_score
    global max_score_val
    for i in range(4):
        k=0
        for j in range(4):
            if(l[i*4+j]!=0):
                l[i*4+k]=l[i*4+j]
                if(j!=k):
                    flag=True
                    l[i*4+j]=0
                k+=1
    for i in range(4):
        for j in range(3):
            if(l[i*4+j]==l[i*4+j+1] and l[i*4+j]!=0):
                l[i*4+j]=2*l[i*4+j]
                curr_score_val=curr_score_val+'+'+str(l[i*4+j])
                max_score_val=str(max(eval(max_score_val),eval(curr_score_val)))
                curr_score.set(str(eval(curr_score_val)))
                max_score.set(max_score_val)
                l[i*4+j+1]=0
                flag=True
    for i in range(4):
        k=0
        for j in range(4):
            if(l[i*4+j]!=0):
                l[i*4+k]=l[i*4+j]
                if(j!=k):
                    flag=True
                    l[i*4+j]=0
                k+=1
    if flag!=False:
        vacant=[]
        for i in range(16):
            if l[i]==0:
                vacant.append(i)
        temp=random.sample(vacant,1)[0]
        val=random.sample([2,4],1)[0]
        l[temp]=val
    for i in range(4):
        y = i * 100+100
        for j in range(4):
            x = j * 100
            tile = tiles(x, y, l[i*4+j])
            tile.draw_tiles(canvas, l[i*4+j])

# Function for all blocks right if possible.
def move_right(canvas):
    flag=False
    global void_pos
    global l
    global curr_score
    global curr_score_val
    global max_score
    global max_score_val
    for i in range(4):
        k=3
        for j in [3,2,1,0]:
            if(l[i*4+j]!=0):
                l[i*4+k]=l[i*4+j]
                if(j!=k):
                    flag=True
                    l[i*4+j]=0
                k-=1
    for i in range(4):
        for j in [3,2,1]:
            if(l[i*4+j]==l[i*4+j-1] and l[i*4+j]!=0):
                l[i*4+j]=2*l[i*4+j]
                curr_score_val=curr_score_val+'+'+str(l[i*4+j])
                max_score_val=str(max(eval(max_score_val),eval(curr_score_val)))
                curr_score.set(str(eval(curr_score_val)))
                max_score.set(max_score_val)
                l[i*4+j-1]=0
                flag=True
    # print(l)
    for i in range(4):
        k=3
        for j in [3,2,1,0]:
            if(l[i*4+j]!=0):
                l[i*4+k]=l[i*4+j]
                if(j!=k):
                    flag=True
                    l[i*4+j]=0
                k-=1
    if flag!=False:
        vacant=[]
        for i in range(16):
            if l[i]==0:
                vacant.append(i)
        temp=random.sample(vacant,1)[0]
        val=random.sample([2,4],1)[0]
        l[temp]=val
    for i in range(4):
        y = i * 100+100
        for j in range(4):
            x = j * 100
            tile = tiles(x, y, l[i*4+j])
            tile.draw_tiles(canvas, l[i*4+j])


#Initializing all variables
root =  Tk()
root.geometry("400x900")

curr_score = StringVar()
max_score = StringVar()
curr_score_val=""
max_score_val="0"
all_tiles = []
canvas =  Canvas(root, width=400, height=900, bg="lightblue")
canvas.pack()

# Dictionary for deciding color
color={}
color[2]="lightblue"
color[4]="blue"
color[8]="darkblue"
color[16]="yellow"
color[32]="sienna1"
color[64]="chocolate1"
color[128]="red"
color[256]="violetred"
color[512]="orchid4"
color[1024]="purple1"
color[2048]="gray25"
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
void_pos = 0

# Function to be called at every restart of game.
def start():
    global all_tiles
    global void_pos
    global curr_score,max_score
    global curr_score_val
    global max_score_val
    curr_score_val="0"
    curr_score.set(curr_score_val)
    # high_score.set(max(curr_score,high_score))
    all_tiles.clear()
    count = 0
    for i in range(16):
        l[i]=0;
    x,y=random.sample(range(0,15),2)
    l[x]=2
    l[y]=2
    for i in range(4):
        y = i * 100+100
        for j in range(4):
            x = j * 100
            tile = tiles(x, y, l[i*4+j])
            tile.draw_tiles(canvas, l[i*4+j])
            all_tiles.append(tile)
start()

canvas.create_text(80,50,font=("Helvetica", 40, "bold italic") ,text="2048")

curr_score_field = Entry(canvas, textvariable=curr_score)
max_score_field = Entry(canvas, textvariable=max_score)
canvas.create_text(200, 30,font=("Helvetica", 20),text="Score")
canvas.create_text(300, 30, font=("Helvetica", 20), text="HS")
canvas.create_window(200, 80,height=30,width=50, window=curr_score_field)
canvas.create_window(300, 80,height=30,width=50, window=max_score_field)


canvas.create_rectangle(150, 600, 150 + 100, 600 + 100, fill="lightblue")
canvas.create_text((2*150 + 100)/2, (2*600 + 100)/2, text="UP")

canvas.create_rectangle(150, 700, 150 + 100, 700 + 100, fill="lightblue")
canvas.create_text((2 * 150 + 100) / 2, (2 * 700 + 100) / 2, text="DOWN")

canvas.create_rectangle(50, 700, 50 + 100, 700 + 100, fill="lightblue")
canvas.create_text((2 * 50 + 100) / 2, (2 * 700 + 100) / 2, text="LEFT")

canvas.create_rectangle(250, 700, 250 + 100, 700 + 100, fill="lightblue")
canvas.create_text((2*250 + 100)/2, (2*700 + 100)/2, text="RIGHT")

#Function to initiate moves according to click on the position of dashboard.
def callback(event):
    if event.x > 150 and event.x < 250 and event.y > 600 and event.y < 700:
        move_up(canvas)
    if event.x > 150 and event.x < 250 and event.y > 700 and event.y < 800:
        move_down(canvas)
    if event.x > 50 and event.x < 150 and event.y > 700 and event.y < 800:
        move_left(canvas)
    if event.x > 250 and event.x < 350 and event.y > 700 and event.y < 800:
        move_right(canvas)
    won_or_not()
    for i in range(4):
        print(l[i*4],l[i*4+1],l[i*4+2],l[i*4+3])
    print("\n")

canvas.bind("<Button-1>", callback)


#Fucntion to check if game finished or not.
def won_or_not():
    global l
    is_done = False
    for i in range(1,16):
        if(l[i]==2048):
            is_done=True;
    if (is_done):
        messagebox.showinfo("Won", "congratulation you won")
        l = random.sample(range(16), 16)
        start()
    else:
        for i in range(16):
            if l[i]==0:
                is_done = True
                break

        for j in range(4):
            for i in range(3):
                if(l[i*4+j]==l[(i+1)*4+j] and l[i*4+j]!=0):
                    is_done=True;

        for j in range(4):
            for i in [3,2,1]:
                if(l[i*4+j]==l[(i-1)*4+j] and l[i*4+j]!=0):
                    is_done=True;

        for i in range(4):
            for j in range(3):
                if(l[i*4+j]==l[i*4+j+1] and l[i*4+j]!=0):
                    is_done=True;

        for i in range(4):
            for j in [3,2,1]:
                if(l[i*4+j]==l[i*4+j-1] and l[i*4+j]!=0):
                    is_done=True;

    if (is_done==False):
        messagebox.showinfo("Game Over",  "you Loose")
        l = random.sample(range(16), 16)
        start()

won_or_not()
root.mainloop()
