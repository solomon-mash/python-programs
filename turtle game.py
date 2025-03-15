import turtle
import random

t1 = turtle.Turtle()
t1.color('green')
t1.shape('turtle')


t2 = t1.clone()
t2.color('blue')
t3 = t1.clone()
t4 = t2.clone()

def start_pos():
    t1.penup()
    t2.penup()
    t3.penup()
    t4.penup()
    t3.goto(-75, 190)
    t3.pendown()
    t3.circle(45)
    t3.penup()
    t3.goto(-75, 175)
    t3.pendown()
    t3.write('home')
    t3.penup()
    t3.hideturtle()
    t4.goto(100, 190)
    t4.pendown()
    t4.circle(45)
    t4.penup()
    t4.goto(100, 170)
    t4.pendown()
    t4.write('home')
    t4.penup()
    t4.hideturtle()
    t1.goto(-70, -250)
    t2.goto(100, -250)
    game_logic()


def dice(x):
    for i in range(x):
        num = random.randrange(5, 10)
        return num

def game_logic():
    for i in range(20):
        if t1.pos() >= (-70, 190):
            print("Player 1 won")
            break
        elif t2.pos() >= (100, 190):
            print("player 2 won")
            break
        else:
            prev1 = -250
            prev2 = -250
            p1num = int(input("player 1 please enter any number from 1 to 9 to move the turtle. choose wisely: "))
            print("Number entered is: ", p1num)
#            print(dice())
            prev1 = prev1 + 50*dice(p1num)
            t1.goto(-70, prev1)
            print("now is player 2 turn")
            p2num = int(input("player 2 please enter any number from 1 to 9 to move the turtle. choose wisely: "))
            print("player 2 press enter to roll the dice ")

            print("Number entered is: ", p2num)
#            print(dice())
            prev2 = prev2 + 50 * dice(p2num)
            t2.goto(100, prev2)


start_pos()

turtle.mainloop()