from joy import *

#maincircle
mainc = circle(stroke="green", x=0, y=0, r=150) 

#Central portion
z = line(x1=0, y1=0, x2=20, y2=20, stroke="#000066", stroke_width="5")| repeat(2,rotate(-30))| rotate(-30)| translate(x=-40, y=0)
m = line(x1=0, y1=0, x2=15, y2=25,stroke="#000066", stroke_width="5")| translate(x=-5, y=-10)
y = line(x1=0, y1=0, x2=20, y2=20, stroke="#000066", stroke_width="5")| repeat(2,rotate(-30))| rotate(150)| translate(x=40, y=0)

#circle
c4= circle(x=50, y=0, r=6,fill="white", stroke="#EC9B3B") | repeat(36, rotate(10))
 
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
semi = polygon(points,fill="#FF284B",x=50, y=50)| rotate(-90)
c1=circle(fill="#FFC900", x=0, y=0, r=150)
upetal = ellipse( x=135, y=0, w=30,h=40,fill="#FF284B") | repeat(8, rotate(20))| rotate(20)
lpetal = ellipse( x=135, y=0, w=30,h=40,fill="#FFC900") | repeat(8, rotate(20))| rotate(-160)


#midcircle
donut = circle(r=120,fill="#FF5C77")

#petals
petal=ellipse(x=60,y=60,w=10,h=20,fill='wheat')
flow=petal | translate(x=30, y=30) | repeat(80,rotate(5))
flow1=petal | translate(x=0, y=0) | repeat(80,rotate(5))

#sidecircles
#sidec1= ellipse(w=10, h=40, fill="green") | translate(x=0, y=0) | rotate(90)| repeat(2, rotate(30))
#sidec2= ellipse(w=10, h=40, fill="green") | translate(x=0, y=0)| rotate(90)| repeat(2, rotate(30))


#middle part
z1 = point(x=0, y=0)
z2 = point(x=85, y=0)
z3 = point(x=0, y=85)
z4 = point(x=85, y=85)
poly= polygon([z1,z2,z3,z4],fill="#FECD1A ", stroke="red", stroke_width="2")| repeat(18, rotate(30))



#inner circles 
greencir= circle(r=85,fill="#FF7F52")
donut1=circle(r=70,fill="#FFC40B")
ellipflower = ellipse(x=60, y=60, w=20, h=10,stroke="none",fill=color(r=270, g=48, b=93, a=0.3)) | repeat(120,rotate(7))

c16 = line(x1=0, y1=0, x2=64, y2=30, stroke="#d74401", stroke_width=3) | repeat(12, rotate(30))

# center  dimmed circle
c0 = circle(x=0, y=0, r=50, fill = color(r=250, g=200, b=0, a=0.5), stroke="none")

#dots
dots = circle(r=5,fill="#7DB954",stroke="none")
d1 = dots | translate(x=145,y=0)| repeat(20,rotate(20))

#sidecircles
sidec1= ellipse(w=10, h=30, fill="green") | translate(x=0, y=135) | rotate(90)|repeat(20,rotate(20))
sidec2= ellipse(w=10, h=30, fill="green") | translate(x=0, y=-135)| rotate(90)
sidec=combine([sidec1+sidec2])

#side codeline
#z1 = line(x1=20, y1=20, x2=0, y2=0, stroke="#000066", stroke_width="5")| repeat(2,rotate(-30))| rotate(-30)| translate(x=-150, y=0)
#y1 = line(x1=20, y1=20, x2=0, y2=0, stroke="#000066", stroke_width="5")| repeat(2,rotate(-30))| rotate(150)| translate(x=150, y=0)

#petal1 = ellipse(x=30, y=60,w=20,h=100,stroke="#00000",stroke_width = 1,fill="#F83518")

pis = ellipse(w=80,h=10,fill="white")| repeat(60,rotate(5))

pis2 = pis | repeat(60,rotate(5))

l1 = ellipse(x = -90, y = 65, w=5,h=5,fill = 'white',stroke = 'none') + ellipse(x = 5, y = 5, r=5,stroke = 'white',stroke_width=3,fill = 'none') | repeat(20,rotate(30))


show(c1,mainc,flow,semi,lpetal, donut,upetal,flow1,l1,poly,greencir,donut1,c16,ellipflower,sidec,c4,c0,z,y,m,d1)
