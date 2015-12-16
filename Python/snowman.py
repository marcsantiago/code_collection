from turtle import *
from random import shuffle, randint, choice


def movepen(x, y):
  penup()
  setpos(x, y)
  pendown()
  return

# Global variables used to pass reference around
middle = None
radi = None

class SnowManBody(object):
  def __init__(self, radius, (x, y), multi_color=False):
    self.radius = radius
    self.start_position = (x, y)
    self.multi_color = multi_color
    # list can be edited to include more colors
    # however it is currently programmed to require at least 3 colors
    # otherwise the pop method below will throw an eror
    self.colors = ['red', 'green', 'white']
    global radi
    radi = radius

  def make_body(self):
    if not self.multi_color:
      movepen(self.start_position[0], self.start_position[1])
      circle(self.radius)
      left(180)
      circle(self.radius * 2)
      global middle
      middle = (xcor(), ycor())
      circle(self.radius * 2, 180)
      left(180)
      circle(self.radius * 2.5)
    else:
      shuffle(self.colors)
      movepen(self.start_position[0], self.start_position[1])

      begin_fill()
      pen(fillcolor=self.colors.pop(), pencolor="black", pensize=1)
      circle(self.radius)
      end_fill()

      left(180)
      begin_fill()
      pen(fillcolor=self.colors.pop(), pencolor="black", pensize=1)
      circle(self.radius * 2)
      global middle
      middle = (xcor(), ycor())
      end_fill()
      circle(self.radius * 2, 180)

      left(180)
      begin_fill()
      pen(fillcolor=self.colors.pop(), pencolor="black", pensize=1)
      circle(self.radius * 2.5)
      end_fill()
    return

class Arms(object):
  def __init__(self, color, normal_arms=True):
    #self.arm_color = color
    self.normal = normal_arms
    global middle
    global radi
    pen(pencolor=color, pensize=3)

  def left(self, starting_postion, radi):
    dirc = choice(['l', 'r'])
    rint = randint(0, 45)
    # movepen(starting_postion[0], starting_postion[1])
    # movepen(starting_postion[0], ycor() - radi)
    movepen(starting_postion[0] - radi*2, ycor() - radi)
    if dirc == 'l':
      left(rint)
    else:
      right(rint)
    forward(randint(50, 65))
    penup()
    home()
    pendown()
    return

  def right(self, starting_postion, radi):
    dirc = choice(['l', 'r'])
    rint = randint(0, 45)
    # movepen(starting_postion[0], starting_postion[1])
    right(180)
    movepen(starting_postion[0], ycor() - radi)
    movepen(starting_postion[0] + radi*2, ycor() - radi)
    if dirc == 'l':
      left(rint)
    else:
      right(rint)
    forward(randint(50, 65))
    penup()
    home()
    pendown()
    return

  def draw_arms(self):
    movepen(middle[0], middle[1])
    starting_position = (middle[0], (-1 * radi))
    movepen(middle[0], (-1 * radi))
    self.left(starting_position, radi)
    self.right(starting_position, radi)


class Face(object):
  def __init__(self):
    global middle
    global radi

  def eyes(self, size, color):
    # reset reference point
    movepen(middle[0], middle[1])
    # left eye
    movepen(middle[0], middle[1] + (radi + (radi / 3)))
    movepen(middle[0] - radi / 3 , middle[1] + (radi + (radi / 3)))
    dot(size, color)
    # right eye
    movepen(middle[0], middle[1] + (radi + (radi / 3)))
    movepen(middle[0] + radi / 3 , middle[1] + (radi + (radi / 3)))
    dot(size, color)

  def mouth(self, size, color):
    pen(pencolor=color, pensize=size)
    penup()
    home()
    movepen(middle[0], middle[1])
    movepen(middle[0], middle[1] + (radi / 3))
    circle(10, 45)
    # penup()
#     home()
#     movepen(middle[0], middle[1])
#     movepen(middle[0], middle[1] + (radi / 3))
#     right(180)
#     circle(10, 45)


  def hat(self, hat_color):
    penup()
    home()
    movepen(middle[0] - radi / 2, middle[1] + radi * 2)
    color(hat_color)
    begin_fill()
    for i in xrange(2):
      forward(20 + radi / 2)
      left(90)
      forward(30 + radi / 2)
      left(90)
      end_fill()
      
    movepen(middle[0] - radi, middle[1] + radi * 2)
    color(hat_color)
    begin_fill()
    for i in xrange(2):
      forward(40 + radi / 2)
      left(90)
      forward(2)
      left(90)
      end_fill()


class Buttons(object):
  def __init__(self):
    global middle
    global radi
  
  def buttons(self, size, colors):
    penup()
    home()
    movepen(middle[0], middle[1])
    down = 10
    for i in xrange(4):
      movepen(middle[0], middle[1] - down)
      dot(size, colors[i %len(colors)])
      down += radi
    
    down += (radi - (radi /3))
    for i in xrange(4):
      movepen(middle[0], middle[1] - down)
      dot(size, colors[i %len(colors)])
      down += radi


class Snowman(object):
  def __init__(self, radi, start_position_tuple, multi_color, arm_color, eye_size, eye_color, mouth_size, mouth_color, hat_color, botton_size, bottom_color_list):
    SnowManBody(radi, (start_position_tuple[0],start_position_tuple[1]), multi_color=multi_color).make_body()
    Arms(arm_color).draw_arms()
    Face().eyes(eye_size, eye_color)
    Face().mouth(mouth_size, mouth_color)
    Face().hat(hat_color)
    Buttons().buttons(botton_size, bottom_color_list)


class TheeSnowMen(object):
  def __init__(self):
    ###Create three snowman instances here
    ###Snowman attributes can be edited
    s1 = Snowman(25, (0, 0), multi_color=False, arm_color="black", eye_size=5, eye_color="black", mouth_size=1, mouth_color="black", hat_color="black", botton_size=7, bottom_color_list=["grey"])
    penup()
    home()
    s2 = Snowman(30, (-200, 0), multi_color=True, arm_color="brown", eye_size=5, eye_color="green", mouth_size=1, mouth_color="black", hat_color="green",botton_size=10, bottom_color_list=["green", "red"])
    penup()
    home()
    s3 = Snowman(30, (200, 0), multi_color=True, arm_color="black", eye_size=5, eye_color="grey", mouth_size=1, mouth_color="red", hat_color="green", botton_size=15, bottom_color_list=["black"])
    mainloop()

TheeSnowMen()

# SnowManBody(25, (-200, 0)).make_body()
# Arms("black").draw_arms()
# mainloop()


