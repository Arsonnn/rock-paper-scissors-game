human_turn = input('input human turn')
computer_turn = input("input computer turn: ")

if human_turn == computer_turn:
    print("Draw!") 
if human_turn == 'rock' and computer_turn == 'scissors' : 
    print('Pelmenis wins!')
elif human_turn == 'paper' and computer_turn == 'rock' : 
    print('Pelmenis wins!')
elif human_turn == 'scissors' and computer_turn == 'paper' : 
    print('Pelmenis wins!')
else: 
    print ("Computar wins!")
   
