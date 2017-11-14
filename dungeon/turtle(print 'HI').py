
#texte schreiben mit import turtl










import turtle

qwerty = turtle.Turtle()
qwerty.penup()

qwertz = turtle.Turtle()
qwertz.penup()


#-------------------------text 1 HI----------------------------------
for durchlauf in range (1):
      for x,y in [ (-100,-100),(-100,100), (-100,0), (-25,0), (-25,100), (-25,-100)]:

          qwerty.goto (x,y)
          qwerty.pendown()
          
          qwertz.goto(50,-100)
          qwertz.pendown()
      
      
      for x,y in [(50,-100), (50,100)]:
          qwertz.goto(x,y)
          


turtle.exitonclick()

