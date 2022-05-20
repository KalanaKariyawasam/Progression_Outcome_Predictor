# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 18097656        
  
# Date:  21/11/20


#Student Version

#Create Variables
Pass  = 0
Defer = 0
Fail = 0

#Get user inputs
Pass = int(input("Please enter your credits at Pass : "))
Defer = int(input("Please enter your credits at Defer : "))
Fail = int(input("Please enter your credits at Fail : "))

#Process & Outputs
if(Pass > 100):
    print("\nProgress")

elif(Defer+Fail == 20):
    print("\nProgress (module trailer)")

elif(Defer+Fail <= 120) and (Fail < 80):
    print("\nDo not Progress – module retriever")

elif(Fail >= 80):
    print("\nExclude")
    
