#!/home/pi/software/bin/python3

# import modules for CGI handling
import cgi, cgitb
import subprocess
import re


cgitb.enable( )

# Create instance of FieldStorage to process CGI form values
form = cgi.FieldStorage( )
condition = form.getvalue('condition')


def authorInfo() :
    print("\n")
    print("The CSSP-19 is made By: Alex Chu, Sam Cheung, and Kenenth.", end="")

# end of def authorInfo()

def endInfo() :
    print("\n")
    print("Thank You For Using CSSP-19 Screening App.", end="")

# end of def endInfo()

# Checks for the amount of condition selected
def isQuestionAnswered(condition) :

    userInput = condition[0:4]
    
    # Question 1 Unanswered
    if (userInput[0] == "None1") :

        print("\n")
        print("You Did Not Answwer Question 1\n\n", end="")
        print("Please Go Back & Answwer all 4 Questions\n\n", end="")
        print("Use the Browsers Back Button to Go Back\n\n", end="")

        # exit Program
        exit(0)
    
    # Question 2 Unanswered
    elif (userInput[1] == "None2") :

        print("\n")
        print("You Did Not Answwer Question 2\n\n", end="")
        print("Please Go Back & Answwer all 4 Questions\n\n", end="")
        print("Use the Browsers Back Button to Go Back\n\n", end="")

        # exit Program
        exit(0)

    # Question 3 Unanswered
    elif (userInput[2] == "None3") :

        print("\n")
        print("You Did Not Answwer Question 3\n\n", end="")
        print("Please Go Back & Answwer all 4 Questions\n\n", end="")
        print("Use the Browsers Back Button to Go Back\n\n", end="")

        # exit Program
        exit(0)

    elif (userInput[3] == "None4") :

        print("\n")
        print("You Did Not Answwer Question 4\n\n", end="")
        print("Please Go Back & Answwer all 4 Questions\n\n", end="")
        print("Use the Browsers Back Button to Go Back\n\n", end="")

        # exit Program
        exit(0)

# end of def isQuestionAnswered


def questionOne(condition)   :

    userInput = condition[0]

    # Q1: Are you fully vaccinated against COVID-19 ?

    if (userInput == "Yes1") :

        return True
        
    elif (userInput == "No1") :

        return False

# end of def questionOne


def questionTwo(condition)   :

    userInput = condition[1]

    # Q2: Are you experiencing any COVID-19 symptoms?
    
    if (userInput == "Yes2") :

        return True
        #print("\n")
        #print("Yes, You Do Are Experiencing COVID-19 Symptoms", end="")

    elif (userInput == "No2") :

        return False
        #print("\n")
        #print("No, You Are Not Experiencing COVID-19 Symptoms", end="")

# end of def questionTwo

def questionThree(condition)   :

    userInput = condition[2]

    # Q3: In the last 14 days, have you travelled outside of Canada?

    if (userInput == "Yes3") :

        return True

    elif (userInput == "No3") :

        return False

# end of def questionThree


def questionFour(condition)   :

    userInput = condition[3]

    # Q4: Are You Wearing a Face Mask ?
    if (userInput == "Yes4") :

        return True

    elif (userInput == "No4") :

        return False

# end of def questionFour

def questionResult() :


    if questionThree(condition) == True :

        print("\n")
        print("Because You Travelled Outside of Canada In The Last 14 Days\n\n", end="")
        print("Your Appointement will be cancelled due to COVID-19 guidelines\n\n", end="")
        print("Please Contact the Our Office to Re-Schedule Another Appointement\n\n", end="")

        exit(0)


    elif questionThree(condition) == False :


        if questionOne(condition) == True :
            print("\n")
            print("Yes, You Are Fully Vaccinated Against COVID-19", end="")


        elif questionOne(condition) == False :

            print("\n")
            print("No, You Are Not Fully Vaccinated Against COVID-19", end="")
        

        if questionTwo(condition) == True :

            print("\n")
            print("Yes, You Do Are Experiencing COVID-19 Symptoms", end="")

           

        
        elif questionTwo(condition) == False :
            
            print("\n")
            print("No, You Are Not Experiencing COVID-19 Symptoms", end="")


        print("\n")
        print("No, Have Not Travelled Outside of Canada In The Last 14 Days", end="")

   
        if questionFour(condition) == True :

            print("\n")
            print("Yes You Are Wearing a Face Mask", end="")


        elif questionFour(condition) == False :

            print("\n")
            print("No, You Are Not Wearing a Face Mask", end="")


# HTML Output
print("Content-type: text/html\n\n")

print("<html><body><pre>")

print(subprocess.check_output("date", shell=True, text=True))

isQuestionAnswered(condition)

questionResult()

authorInfo()

endInfo()

print("</pre></body></html>\n")

