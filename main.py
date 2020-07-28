total=0
#functions
def addOne():
  total+=1
#def() end
def addTwo():
  total+=2
#def() end

running= True
#Choose player to go first
while(running==True):
  first= input("Who is going first?(SAY 'Me') ")
  if (first=="Me"):

    a= int(input("Player1: add..."))
    if(a==1):
      total+=1
      print(total)
    else:
      
      print(total)

    b= int(input("player2: add..."))
    if(b==1):
      total+=1
      print(total)
    else:
      addTwo()
      print(total)
    
    if(total>=20):
      running= False
#while(0 end)

if(total>=20  ):
  print("PLAYER1 WINS!!!!")     
else:
  print("PLAYER2 WINS!!")