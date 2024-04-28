# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution. 
# Student ID:20221590
#UoW no:1956195
# Date: 14.December.2022
progress =0 
trailer =0 
retriever=0 
exclude =0
List_of_credits = []
file = open('Student_credits_file.txt','w')
print("Welcome to the Program CW 1\n .Academic year-2022. ")
def validation (requires) : #This function used for 1st & 2nd validation requirement   
    while True:
        try:
            creditss=int(input("Please enter your credits at " +requires + ": "))
            if creditss % 20!=0  or 0>creditss or creditss>120: 
                print("Out of range.\nPlease re-enter your ",requires,"credits\n")
                continue
        except ValueError:
            print("Integer required\nPlease re-enter your ",requires,"credits\n")            
            continue        
        break        
    return creditss

def Student_Credits_outcomes():#This funtion to get Progression outcomes, and helping to versions(students/staff) when it call.
    while True:  
        Pass=validation ('pass')        
        Defer=validation('defer')        
        Fail=validation('fail')       
        
        total=Pass + Defer + Fail#For 3rd Validation requirement 
        if total != 120:
            print("Total incorrect.\nThere is an error your enterd credits. plese enter again.  ")
            continue
            
        global progress ,trailer ,exclude , retriever# to access "grade" in anywhere  
        if Pass==120:                
            grade='Progress'   
            progress+=1
        elif Pass==100:
            grade='Progress(module trailer)'
            trailer +=1 
        elif Fail==80 or Fail==100 or Fail==120:
            grade='Exclude'
            exclude+=1
        else:
            grade='progress-module retriver'
            retriever+=1
        print(grade)
        
        file.write(f'{grade}  -{Pass},{Defer},{Fail}\n')#adding data to the text file
            
        List_of_credits.append([grade ,Pass,Defer,Fail])
        break
        
while True:
    Command=print ('\nEnter "1" if you are a student:\nEnter "2" if you are a staff:\nEnter "any other  number" to exit:')   
    try:
        decision=int(input("enter your choice here : "))
    except ValueError :
        print("Integer required,Please enter 1 , 2 for your choice or any other number to exit. ")
        continue
    if decision ==1:
        print('\n\t Student Version\n\t(Only one attempt)\n')        
        file1 = open('Student_attempt_file.txt','w')        
        Student_Credits_outcomes()
        file1.close()        
        continue
        break
    
    elif decision == 2 :
        print('\n\t   Staff Version\n\t(Multipule attempts)\n')
        while True:            
            Student_Credits_outcomes()
            Multipule_outcomes=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")#Asking for multiple progression outcomes        
            print('\n')
               
            if Multipule_outcomes == 'q':
                break
            continue
        print('-'*70)
        print("\nHistogram")
        print("Progress:",progress,":","*"*progress)
        print("Trailer:",trailer,":","*"*trailer)
        print("Retriever:",retriever,":","*"*retriever)
        print("Exclude:",exclude,":","*"*exclude)
        print(progress+trailer+retriever+exclude,"outcomes in total.\n")
        print('-'*70)

        print("Part 2:")#list typing and ajesment part
        total = progress+trailer+retriever+exclude
        for i in range(total):
            print()
            print(List_of_credits[i][0]," ",end="")
            for j in range(1,3):
                print(List_of_credits[i][j],",",end="")
            print(List_of_credits[i][3]," ",end="")
        print()       
        print("\nPart 3:")
        file.close()#closing the file which opend
        file = open('Student_credits_file.txt','r')
        print(file.read())#printing the file details in "Student_credits_file.txt" to IDLE 
        file.close()
       
    else:
        print("\n\tThe End")
        break
    
    
