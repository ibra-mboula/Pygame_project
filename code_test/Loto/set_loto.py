import random

class Loto:

    def generateNumber():
        loto_numbers = set()
        while (len(loto_numbers) < 6):

            rand = random.randint(1,45)   
            loto_numbers.add(rand)    
                  
        a = list(loto_numbers)     

        for i in range(0, len(a)):
          a[i] = int(a[i])  
        print(a)
        return a
            
    def readNumber():
        listUser=set()
        
        while len(listUser) < 6:
            
            a = input("Enter a number between 1 and 45 : ")
            
            while ((a) == ""):  
                print("get focus") 
                a = input("Enter a number between 1 and 45 : ")
                
   
            if (int(a) >= 0 & int(a) <= 45):    
                listUser.add(a)    
                   
        l= list(listUser)  
        
        b=([int(x) for x in l])
        
        return b

    def compareNumber():
        a = Loto.generateNumber()
        b = Loto.readNumber()
        print(a)
        print(b)
        c = set(a) & set(b)
        print(f"you got {len(c)} numbers right")
        
        if len(c) >= 3:
            print("You won the jackpot")
        else: print("You lost")
     

Loto.compareNumber()