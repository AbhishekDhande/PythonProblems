import random
l1=["stone","paper","scissor"]
print("..................WELCOME TO STONE PAPER SCISSORS............... ")
print("Enter the first player name")
p1=input()
print("Enter the second player name")
p2=input()
ch=1
while(ch==1):
    p1c=random.choice(l1)
    p2c=random.choice(l1)
    print(p1,"choice: ",p1c)
    print(p2,"choice: ",p2c)
    if(p1c==p2c):
        print("Its a Tie")
    elif(p1c=="stone" and p2c=="paper"):
        print("congratulations ",p2)
    elif(p2c=="stone" and p1c=="paper"):
        print("congratulations ",p1)
    elif(p1c=="stone" and p2c=="scissor"):
        print("congratulations ",p1)
    elif(p2c=="stone" and p1c=="scissor"):
        print("congratulations ",p2)
    elif(p1c=="paper" and p2c=="scissor"):
        print("congratulations ",p2)
    elif(p2c=="paper" and p1c=="scissor"):
        print("congratulations ",p1)
    print()    
    print("DO u want to continue press 1 else 0 : ")
    ch=int(input())
