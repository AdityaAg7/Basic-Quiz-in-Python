b=input("plz enter ur name    ")
print("welcome to quiz ,simply answer 2 question and win jackpot")
print("do u want to play(yes/no)")
a=input("")
score=0
if(a=="no"):
    print("thank let me know when u want to play")
    
if (a=="yes"):
    print(b,"okay, lets play:)")
    c=input("best scientist in world  :  ")
    d=input("full form of cpu    ")
    if(c=="albert einstein"):
        score+=1
        print("you are right your score in 1st question is",score)
    else:
         score-=1
         print("oopps!!!!!.,you are wrong 1st question",score)
    if(d=="central processing unit"):
         score+=1
         print("wow!!! you got the answer right ur score is in 2nd question",score)
    else: 
        score-=1
        print("oops!!!! you are a donkey 2nd question",score)
print("total score ",score)        
print("REMAKS")
if(score==2):
        print("u won a jackpot")
if(score==1):
        print("u arew avg")
if(score<=0):
        print("shame on you")             
        
    