from turtle import *

#we want paint to house

#step 1: drave a square
speed(4)
width(10)
color("green")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square
#draving a door

forward(70)
color("orange")
begin_fill()
left(90)
forward(120)# height of the door
right(90)
forward(65)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

left(30)
forward(70)
color("blue")
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(200, 200)
pendown()

left(90)
begin_fill()
forward(70)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

# left(90)
# forward(50)
# left(90)





exitonclick()