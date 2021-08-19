from joy import *

#maincircle
mainc = circle(stroke="blue", x=0, y=0, r=150)

#semicircle
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
petal=ellipse(x=60,y=60,w=10,h=20,fill="#CE0F3D")
shape2 = ellipse( x=135, y=0, w=30,h=40,fill="#ff3399") | repeat(8, rotate(20))| rotate(20)
c1=circle(fill="#EC9B3B", x=0, y=0, r=150)
flow=petal | translate(x=30, y=30) | repeat(80,rotate(5))
flow1=petal | translate(x=0, y=0) | repeat(80,rotate(5))
donut = circle(r=120,fill="#FA9905")

#sidecircles
sidec1= ellipse(w=10, h=40, fill="green") | translate(x=0, y=0) | rotate(90)| repeat(2, rotate(30))
sidec2= ellipse(w=10, h=40, fill="green") | translate(x=0, y=0)| rotate(90)| repeat(2, rotate(30))
shape = ellipse( x=135, y=0, w=30,h=40,fill="#EC9B3B") | repeat(8, rotate(20))| rotate(-160)


#Central portion
z = line(x1=0, y1=0, x2=20, y2=20, stroke="#000066", stroke_width="5")| repeat(2,rotate(-30))| rotate(-30)| translate(x=-40, y=0)
m = line(x1=0, y1=0, x2=15, y2=25,stroke="#000066", stroke_width="5")| translate(x=-5, y=-10)
y = line(x1=0, y1=0, x2=20, y2=20, stroke="#000066", stroke_width="5")| repeat(2,rotate(-30))| rotate(150)| translate(x=40, y=0)



#middle part


z1 = point(x=0, y=0)
z2 = point(x=85, y=0)
z3 = point(x=0, y=85)
z4 = point(x=85, y=85)
poly= polygon([z1,z2,z3,z4],fill="#FECD1A ", stroke="none", stroke_width="2")| repeat(18, rotate(30))


#circle
c4= circle(x=50, y=0, r=6,fill="white", stroke="#EC9B3B") | repeat(36, rotate(10))



#inner circles 
greencir= circle(r=85,fill="green")
donut1=circle(r=70,fill="#CE0F3D")
ellipflower = ellipse(x=60, y=60, w=20, h=10,stroke="black",stroke_width=1,fill=color(r=170, g=48, b=93, a=0.2)) | repeat(120,rotate(7))

c16 = line(x1=0, y1=0, x2=64, y2=30, stroke="#FFAAA5", stroke_width=3) | repeat(12, rotate(30))

# center  dimmed circle
c0 = circle(x=0, y=0, r=50, fill = color(r=250, g=200, b=0, a=0.5), stroke="none")

#dots
dots = circle(r=5,fill="wheat",stroke="none")
d1 = dots | translate(x=145,y=0)| repeat(20,rotate(20))



#side codeline
z1 = line(x1=20, y1=20, x2=0, y2=0, stroke="#000066", stroke_width="5")| repeat(2,rotate(-30))| rotate(-30)| translate(x=-150, y=0)
y1 = line(x1=20, y1=20, x2=0, y2=0, stroke="#000066", stroke_width="5")| repeat(2,rotate(-30))| rotate(150)| translate(x=150, y=0)


show(c1,mainc,flow,semi,shape2, donut,shape,flow1,sidec1,sidec2,poly,greencir,donut1,c16,ellipflower,c4,c0,z,y,m,d1,z1,y1)
