import turtle
import math
import random


#Set up screen
wn=turtle.Screen()
wn.bgcolor("lightblue")

#create scoreboard
pen=turtle.Turtle()
pen.color=("black")
pen.pensize(5)
pen.hideturtle()

pen2=turtle.Turtle()
pen2.color=("black")
pen2.pensize(5)
pen2.hideturtle()

#create score variable
score1=0
score2=0

#create player turtle
player=turtle.Turtle()
player.color("orange")
player.shape("turtle")
player.turtlesize(1)
player.penup()
player.speed(0)
player.score1=0

# #create 2. player
player2=turtle.Turtle()
player2.color("purple")
player2.shape("turtle")
player2.turtlesize(1)
player2.penup()
player2.speed(0)
player2.score2=0
#create goal
goal=turtle.Turtle()
goal.color("black")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-270,270),random.randint(-270,270))

#Set variables
speed=3

#finisher
finish = turtle.Turtle()
finish.color("black")
finish.penup()
finish.setposition(-50,0)
finish.hideturtle()
#Function defines

def turnleft():
    player.left(30)
    
def turnright():
    player.right(30)
    
def turnleft2():
    player2.left(30)
    
def turnright2():
    player2.right(30)
    

#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(turnleft2,"A")
turtle.onkey(turnright2,"D")
turtle.onkey(turnleft2,"a")
turtle.onkey(turnright2,"d")




while True:
 if score2 == 10:
  finish.write("Player2 won!", False, align="left",font=("Arial",14,"normal"))
  break
 elif score1 == 10:
  finish.write("Player1 won!", False, align="left",font=("Arial",14,"normal"))
  break
 player.forward(speed)
 player2.forward(speed)
 #Boundary checking
 if player.xcor()>320 or player.xcor()<-320:
     player.right(180)
     
 if player.ycor()>280 or player.ycor()<-280:
     player.right(180)
     
 if player2.xcor()>320 or player2.xcor()<-320:
        player2.right(180)
        
 if player2.ycor()>280 or player2.ycor()<-280:
        player2.right(180)

#collision
 d=math.sqrt(math.pow(player.xcor()-goal.xcor(),2)+math.pow(player.ycor()-goal.ycor(),2))
 if d<20:
  goal.setposition(random.randint(-220,220),random.randint(-220,220))
  score1+=1
  pen.undo()
  pen.penup()
  pen.hideturtle()
  pen.setposition(-210,250)
  scorestring="player1:%s" %score1
  pen.write(scorestring, False, align="left",font=("Arial",14,"normal"))
  
 d=math.sqrt(math.pow(player2.xcor()-goal.xcor(),2)+math.pow(player2.ycor()-goal.ycor(),2))
 if d<20:
  goal.setposition(random.randint(-220,220),random.randint(-220,220))
  
#draw the score on screen
  score2+=1
  pen2.undo()
  pen2.penup()
  pen2.hideturtle()
  pen2.setposition(-210,210)
  scorestring2="player2:%s" %score2
  pen2.write(scorestring2, False, align="left",font=("Arial",14,"normal"))
