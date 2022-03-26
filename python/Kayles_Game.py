#nothing important just to quit if the input is quit
import sys

#Just saying hello
print("\n")
print("Welcome to Kayles game!")
print("\n")


# we are going to use some global values to break the loop
#---------Global Variables----------

current_player=""
position=""
game_running=True
position1=0
position2=0
position=0
winner=None
double_position=False

#This is the main function that is going to call the others 

def main():
  global current_player
  if check_if_want_to_play():
    display_board()
    print("\n")
    player_number()
    while game_running==True:
      current_player_play()
    
      

#We are going to give the user some info if he needs or if he want to quit

def check_if_want_to_play():
  ans=input("To get Info Enter:info , To Quit Enter:quit , To Play Enter: Play :")
  yes=True
  while yes:
   if ans.lower()=="info":
    print("each player can remove either one or two adjacent numbers in each of his turns") 
    print("the one to pick the last number is the winner. ")
    print(" \n")
    ans=input("To get Info Enter:info , To Quit Enter:quit , To Play Enter: Play :")
    continue

   elif ans.lower()=="quit":
    sys.exit(0)
    
   elif ans.lower()=="play":
    yes=False
    return True

   else:
      ans=input("To get Info Enter:info , To Quit Enter:quit , To Play Enter: Play :")
      continue
       



#first display the board that consists of numbers

board=[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,0 ,1 ,2 ,3 ,4 ]


def display_board():
    for i in (board):
      print(i, end=" ")



#who is the player who is going to play first

def player_number():
    global current_player
    current_player=input("who is the first player to start (1 / 2): ")
    yeah=True
    while yeah:
        if current_player=="1":
            yeah=False

        elif current_player=="2":
             yeah=False

        else:
            current_player=input("who is the first player to start (1 / 2): ")
            continue




#if he chose to play one time in this turn and make sure if its a valid input

def player_single_position():
    global position,game_running
    board_values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] #just to make sure the input is in that range
    position=int(input("please enter the token that you want to choose: ")) 
  
    Valid=True
    while Valid:
      if game_running==True:
       if position not in board_values:
         print("please enter a valid number from (1 to 24)" )
         position=int(input("please enter the token that you want to choose: ")) 
         continue
       else:
         Valid=False
         return True

       

#if he chose two places in this turn and make sure its a valid input

def player_double_position():
    global position1,position2, double_position
    board_values= range(1, 25)
    position1 =int(input("please enter the first position from (1 to 24)"))
    position2 =int(input("please enter the second position from (1 to 24)"))
    
    
    while True:
     result=position1-position2
     if game_running==True:
      if abs(result)==1: #i dont know why it not woking so i can try using the abs of their subtruction
       truee=True
       while truee:
        if  (position1 not in board_values) or (position2 not in board_values) or ((position1 and position2) not in board_values):
         print("please enter a valid number from (1 to 24)" )
         player_double_position()
         double_position=False
        
        elif (position1 and position2 ) in board_values:
          double_position=True
          return True
         
      else:
        print("Please enter two adjacent numbers!!!")
        player_double_position()
       
#see if the input is going to delete one or two adjacent numbers, also cant play in a already played place

def current_player_play():
  global current_player, game_running, position1,position2,position,board,winner,double_position

  num_plays=input("Are you going to choose (1 \ 2) tokens: ")
  true=True
  while true:
    if num_plays=="1":
        if player_single_position():
          check_position()
          board[position-1]="-"
          display_board()
          if check_winner():
            game_running=False
            true=False
            print("\n")
            print(f"***The winner is {winner}")
            sys.exit(0)
          else:
            switch_player()
    
    elif num_plays=="2":
       if No_adjacent():
        player_double_position()
        if double_position==True:
          check_position1()
          check_position2()
          board[position1-1]="-"
          board[position2-1]="-"
          display_board()
          if check_winner():
            game_running=False
            true=False
            print("\n")
            print(f"***The winner is {winner}")
            sys.exit(0)
          else:
            switch_player()

         

    else:
      print("please choose 1 or 2 ")
      num_plays=input("Are you going to choose (1 \ 2) tokens: ")
      continue 
    

#check if the position is free or not

def check_position():
  global position
  yess=True
  while yess:
   if board[position-1]=="-":
    print("please enter a number that is not taken before!")
    player_single_position()
    continue
   else:
    yess=False
    return True

def check_position1():
  global position1
  yesss=True
  while yesss: 
   if board[position1-1]=="-" :
    print("please enter a number that is not taken before!")
    player_double_position()
    continue
   else:
     yesss=False
     return True
def check_position2():
  global position2
  yessss=True
  while yessss:
   if board[position2-1]=="-":
    print("please enter a number that is not taken before!")
    player_double_position()
    continue
   else:
     yessss=False
     return True

    



#switch players

def switch_player():
    global current_player
    if current_player=="1":
        print(" \n player two turn ")
        current_player="2"
        current_player_play()

    elif current_player=="2":
        print(" \n player one turn ")
        current_player="1"
        current_player_play()
    
def check_winner():
   global game_running,winner,board
   result=board.count(board[0])==len(board)
   
   if result:
        winner=current_player
        return True
   else:
        return False

#imagine only one number in the list, and player choose to play two times that will make a big problem
#so lets restrict him :)

def No_adjacent():

  global board
  
  for i in range(0,23):
    count=0
    board_values2=range(1,25)
    if (board[i] in board_values2) and (board[i+1] in board_values2):
      count+=1
    elif (board[i] not in board_values2) and (board[i+1] not in board_values2):
      count+=1
      
  if count>0:
    
        return True

  elif count==0:
         print("you dont have a choice, there is no two adjacent numbers!!!")
         current_player_play()
         return False
         
    
  



#Calling the main function

main()
#check the whole positiob in just one function
