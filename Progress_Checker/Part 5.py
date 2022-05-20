# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 18097656        
  
# Date:  21/11/20

#Alternative Staff Version

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

#Create List & Variables
marksList = [[120,0,0],
             [100,20,0],
             [100,0,20],
             [80,20,20],
             [60,40,20],
             [40,40,40],
             [20,40,60],
             [20,20,80],
             [20,0,100],
             [0,0,120]]
P_Count = 0
T_Count = 0
R_Count = 0
E_Count = 0

#Process & Outputs
for item in marksList:
    if(int(item[0]) == 120):
        print("\nProgress",end="")
        P_Count += 1
    
    elif(int(item[1]+item[2]) == 20):
        print("\nProgress (module trailer)",end="")
        T_Count += 1
    
    elif(int(item[1]+item[2]) <= 120) and (item[2] < 80):
        print("\nDo not Progress – module retriever",end="")
        R_Count += 1
    
    elif(int(item[2]) >= 80):
        print("\nExclude",end="")
        E_Count += 1

#Histogram
print()
outputs(P_Count,T_Count,R_Count,E_Count)
