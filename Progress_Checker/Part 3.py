# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 18097656        
  
# Date:  21/11/20

#Staff Version with Histogram

def outputs(P_Count,T_Count,R_Count,E_Count):
    "This is for Histogram outputs"
    
    print("\n----------------------------------------------------")
    print("Horizontal Histogram")
    print("Progress ",P_Count,":","*"*P_Count)
    print("Trailer  ",T_Count,":","*"*T_Count)
    print("Retriever",R_Count,":","*"*R_Count)
    print("Excluded ",E_Count,":","*"*E_Count)
    print(P_Count+T_Count+R_Count+E_Count,"outcomes in total.")
    print("----------------------------------------------------")

#Create Variables
Pass  = 0
Defer = 0
Fail = 0
Range = (0,20,40,60,80,100,120)
choice = ""
P_Count = 0
T_Count = 0
R_Count = 0
E_Count = 0

#Get user inputs
while True:
    choice = input("\nDo you wish to continue?\nEnter 'y' for yes or 'q' to quit and view results: ")
    if(choice == "y") or (choice == "Y"):
        while True:
            try:
                Pass = int(input("\nPlease enter your credits at Pass : "))
                if(Pass in Range):
                    Defer = int(input("Please enter your credits at Defer : "))
                    if(Defer in Range):
                        Fail = int(input("Please enter your credits at Fail : "))
                        if(Fail in Range):
                            if((Pass+Defer+Fail) == 120):
#Process & Outputs
                                if(Pass == 120):
                                    print("\nProgress")
                                    P_Count += 1
    
                                elif(Defer+Fail == 20):
                                    print("\nProgress (module trailer)")
                                    T_Count += 1
    
                                elif(Defer+Fail <= 120) and (Fail < 80):
                                    print("\nDo not Progress – module retriever")
                                    R_Count += 1
    
                                elif(Fail >= 80):
                                    print("\nExclude")
                                    E_Count += 1
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
            break
#Histogram    
    elif(choice == "q") or (choice == "Q"):

        outputs(P_Count,T_Count,R_Count,E_Count)
        break


