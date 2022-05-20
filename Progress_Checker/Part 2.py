# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 18097656        
  
# Date:  21/11/20

#Student Version (Validation)

#Get user inputs
def uinputs():
    #Create Variables
    global Pass 
    global Defer 
    global Fail
    Range = (0,20,40,60,80,100,120)
    "This is for get user inputs"

    while True:
        try:
            Pass = int(input("\nPlease enter your credits at Pass : "))
            if(Pass in Range):
                Defer = int(input("Please enter your credits at Defer : "))
                if(Defer in Range):
                    Fail = int(input("Please enter your credits at Fail : "))
                    if(Fail in Range):
                        if((Pass+Defer+Fail) == 120):
                            break
                        else:
                            print("\nTotal Incorrect...")
                    else:
                        print("Out of range...")
                else:
                    print("Out of range...")
            else:
                print("Out of range...")
   
        except ValueError:
            print("\nInteger required...")
        
uinputs()

#Process & Outputs
if(Pass == 120):
    print("\nProgress")
    
elif(Defer+Fail == 20):
    print("\nProgress (module trailer)")
    
elif(Defer+Fail <= 120) and (Fail < 80):
    print("\nDo not Progress – module retriever")
    
elif(Fail >= 80):
    print("\nExclude")
