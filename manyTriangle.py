import turtle

def tri(aTurtle,level):
   if level <= 0:
  	 return   
   dawOneTri(aTurtle)
   aTurtle.forward(20)
   dawOneTri(aTurtle)

   aTurtle.right(120)
   aTurtle.forward(20)

   aTurtle.left(120)
   dawOneTri(aTurtle)

   aTurtle.right(60)
   aTurtle.forward(20)
   aTurtle.left(60)

   tri(aTurtle,level-1)
  
   aTurtle.left(60)
   aTurtle.forward(40)
   aTurtle.right(60)
      
   tri(aTurtle,level-1)
   aTurtle.backward(40)
   return
  
def dawOneTri(aTurtle):
   aTurtle.begin_fill()
   aTurtle.fillcolor('green')
   for i in range(3):
     aTurtle.forward(20)
     aTurtle.right(120)
   aTurtle.end_fill()

def dawTri():
  aTurtle = turtle.Turtle()
  aTurtle.color("green")
  aTurtle.speed(10)
  aTurtle.right(60)
  tri(aTurtle,4)
dawTri()
 



