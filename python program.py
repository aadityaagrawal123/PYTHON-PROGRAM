no1 = int(input("                      Enter your age to apply for the job: "))
if no1 < 18:
    print("Oh! you are too young for the job")
elif no1 < 50 and no1 > 17:
       print("                         You are eligible for the job")
       name = input("Enter your Name here:")
       birth = int(input("Enter your birth year(YYYY):"))
       if birth < 2004 and birth > 1971:
                            education = input("Enter your education level here:")
                            interview = int(input(" available slots for the interview-"
                                                   " 10am-11am / 11am-12pm / 12pm-1pm / 1pm-2pm / 2pm-3pm / 3pm-4pm"
                                                    "     Enter the slot number you want (between 1-6): "))
                            phno = int(input("Enter your phone number (Eg- +91XXXXXXXXXX): "))
                            email = input("Enter your email address (eg- xxxxx@gmail.com) : ")
                            congratulations = print("Bravo!", name ,"see you in the interview, ALL THE BEST")
                            
       else:
           print("WRONG INFORMATION")
else:
    print("Sorry, you are too old for the job")
    

