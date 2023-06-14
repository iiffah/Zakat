"""
Program: Zakat Calculator 
Author: Anas Tawalbeh
Terminal-based calcuator that help user calculate the amount of zakat for thier various type of wealth including:
Cash, Gold, Silver,Agrichulture, Livestock and more
Significant constants
         there is no constants
 2. The inputs are
         Type of wealth
         Amount of wealth
 3. Computations:
         
 4. The outputs are
         zakat amount
"""
#functions definitions

while True:
    x =  input("select the type (cash,Gold,Silver, Plantation): ")
       
    try:
        number1 = float(input("Input  the amount:"))     #we need to put 'int' before the code if u dont put the result will be string not numeric ex '5'+'5'=55 not 10    
    except ValueError:
        print("Pleas enter the correct value")
        continue

     #calculate 
    if x=='cash': 
        if number1>=150000:
            print(number1*2.5/100)
        else:
            print("you don't have to pay zakat, but donations are recommend")
    elif x.upper() == 'GOLD':            #โค้ดupperและlowerมีไว้เพื่อให้สรุปว่าuserจะพิมพ์ตัวเอล็กหรือใหญ่ ก็ยังสามารถรันต่อได้
        if number1 >= 85:
            print(number1*2.5/100)
        else:
            print('u dont need to pay zakat')
    elif x.lower() == 'silver': 
        if number1 >= 595:
            print(number1*2.5/100)
        else:
            print('u dont need to pay zakat')
    elif x.lower()=="plantation":
            d= input("""select the option:
            1.water the plant by your self
            2. use rain for water the plant""")
            if d =='1':
                if number1>=653:
                    print(number1*5/100)
                    #calculation for crops Zakat 
                    
                else:
                    print("U dont need to pay zakat")
            elif d=='2':
                if number1>=653:
                    print(number1*10/100)
                    #calculation for crops Zakat
                    print("calculation for crops Zakat")
                else:
                    print("U dont need to pay zakat")
            else:
                print("Choose between 1 or 2")
    else:
        print("select the type (cash,Gold,Silver, Plantation)")  
   
    # dont need to pay zakat")
       
    
# check if user wants another calculation
# break the while loop if answer is no
    next_calculation = input("Do you want to calculate again? (yes/no): ")
    if next_calculation.lower == "no":
        break
    else:
        print("Welcome")
#functions definitions
#def main():
#print('something')
#print()   
if __name__ == "__main__":
    main()
    """
Program: Zakat Calculator 
Author: Anas Tawalbeh
Terminal-based calcuator that help user calculate the amount of zakat for thier various type of wealth including:
Cash, Gold, Silver,Agrichulture, Livestock and more
Significant constants
         there is no constants
 2. The inputs are
         Type of wealth
         Amount of wealth
 3. Computations:
         
 4. The outputs are
         zakat amount
#functions definitions

while True:
    try:
        x = input("select the type (cash,Gold,Silver, Plantation): ")
        if x=="Plantation":
            print("select the option: ")
            print("1.water the plant by your self")
            print('2. use rain for water the plant')
            d= print (input("Please choose this option 1 or 2: "))  
        else:
            print("Please choose 1 or 2")  
        number1 = float(input("Input  the number:"))     #we need to put 'int' before the code if u dont put the result will be string not numeric ex '5'+'5'=55 not 10    
    except ValueError:
        print("Pleas enter the correct value")

        continue

     #calculate 
    if x=='cash': 
        if number1>=150000:
            print(number1*2.5/100)
        else:
            print("you don't have to pay zakat, but donations are recommend")
    elif x == 'gold':
        if number1 >= 85:
            print(number1*2.5/100)
        else:
            print('u dont need to pay zakat')
    elif x == 'silver':
        if number1 >= 595:
            print(number1*2.5/100)
        else:
            print('u dont need to pay zakat')
    elif d =='1':
        if number1>=653:
            if d=="1":
                print(number1*5/100)
            elif d=='2':
                print(number1*10/100)
        else:
            print("U dont need to pay zakat")     
    else:
        print("u might try later")  
   
    # dont need to pay zakat")
       
    
# check if user wants another calculation
# break the while loop if answer is no
    next_calculation = input("Do you want to calculate again? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        print("Welcome")
#functions definitions
#def main():
#print('something')
#print()   
if __name__ == "__main__":
    main()
"""
