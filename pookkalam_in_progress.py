from joy import *
import math
def part_of_ellips(w,h,theta):
    return point(math.sin(theta)*(w),math.cos(theta)*h)


points = [point(0,0)]

w = 150 # Width of ellipse
h = 150 # Height of ellipse
part = 0.5 # 1 => full ellipse, 0.25 => quarter and so on

step = 0.01 # Increase to make ellipse smoother (will take more time) 

i = 0
while i < (3.14*(part*2)):
    points.append(part_of_ellips(w,h,i))
    i = i+step # Step size
semi = polygon(points,fill="#ff3399",x=50, y=50)| rotate(-90)

mainc = circle(stroke="blue", x=0, y=0, r=150)
#rectflower = rectangle(x=100, y=100, w=20, h=10,stoke="white",fill="#ff3399") | repeat(80,rotate(5))
petal=ellipse(x=60,y=60,w=10,h=20,fill="red")
#shape1 = circle(x=140, y=0, r=10, fill="#ff3399") | repeat(20, rotate(12))
shape2 = ellipse( x=135, y=0, w=30,h=40,fill="#ff3399") | repeat(8, rotate(20))| rotate(20)
c1=circle(fill="yellow", x=0, y=0, r=150)
flow=petal | translate(x=30, y=30) | repeat(80,rotate(5))
#petal1=ellipse(x=0,y=0,fill="")
flow1=petal | translate(x=0, y=0) | repeat(80,rotate(5))
donut = circle(r=120,fill="white")
#sidecircles
sidec1= ellipse(w=10, h=40, fill="green") | translate(x=0, y=135) | rotate(90)
sidec2= ellipse(w=10, h=40, fill="green") | translate(x=0, y=-135)| rotate(90)
shape = ellipse( x=135, y=0, w=30,h=40,fill="yellow") | repeat(8, rotate(20))| rotate(-160)

#Central portion
z = line(x1=0, y1=0, x2=20, y2=20, stroke="black", stroke_width="5")| repeat(2,rotate(-30))| rotate(-30)| translate(x=-40, y=0)
m = line(x1=0, y1=0, x2=15, y2=25,stroke="black", stroke_width="5")| translate(x=-5, y=-10)
y = line(x1=0, y1=0, x2=20, y2=20, stroke="black", stroke_width="5")| repeat(2,rotate(-30))| rotate(150)| translate(x=40, y=0)
show(c1,mainc,flow,semi,shape2, donut,shape,flow1,sidec1,sidec2,z,y,m) 
