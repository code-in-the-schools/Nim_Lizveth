#functions
def addOne():
  return(i+1)
#def() end
def addTwo():
  return(i+2)
#def() end

i=0
running= True

while(running==True):
  a= int(input("Player1: add..."))
  if(a==1):
    print(addOne(a))
  else:
    print(addTwo(a))

  b= int(input("player2: add..."))
  if(b==1):
    print(addOne(b))
  else:
    print(addtwo(b))

  if(i==20 or i>=20):
    running= False