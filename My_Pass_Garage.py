from termcolor import colored
import random
import pyfiglet


  ### >>> All rights reserverd - Amir Sillam - "My Password Garage!"  - 2021 <<< ###


## >> Print welcome screen message << ##
def run_app_screen():
    result = pyfiglet.figlet_format("     Welcome to "
                                    "-                   My Password     "
                                    "                    "
                                    "    Garage !")
    colored_result = colored(result, color= "green")
    print(colored_result)
    print("\n      ******************************************************")
    print("                Welcome to 'My Password Garage!'      ")
    print("           Made by Amir Sillam - All r!ghts res3rved!   "
          " \n    \t\t \t\tOur goal here is to check the "
          "\n\t\t   password the user has entered and check"
          " \n   \t\tit's strength and by that help to protect the user!")
    print("      *******************************************************\n")
    enter_pass()

def end_program():
    result = pyfiglet.figlet_format(" Thanks for choosing"
                                    " our app, have a \ngreat day! ")
    colored_result = colored(result, color= "green")
    print(colored_result)
    exit(1)

## >> User password input << ##
def enter_pass():
    password = input("\t\t\t\t"
                     "  Please enter your password:\n\t\t\t\t\t")
    check_password(password)

## >> Count number of each ascii characters. << ##
def check_password(password):
    count_low_char = 0
    count_upp_char = 0
    count_pass = 0
    num_count = 0
    strong_char = 0

    # > Analyze length and key varialbes lengths in your password ! < #
    for letter in password:
        count_pass+=1
        if letter.islower():
            count_low_char+=1
        elif letter.isupper():
            count_upp_char+=1
        elif letter.isdigit():
            num_count+=1
        else:
            strong_char+=1

## >> Print the Total password length and it's components << ##
    check_password_length(count_pass,password)
    print("\t\t\t\tNow, let's analyze your password.\n")
    print("\t\t\t\t****************************************")
    print(f"\t\t\t  1. Pass length is: {str(count_pass)}               ")
    print(f"\t\t\t  2. Number of lower case letters: {str(count_low_char)}  ")
    print(f"\t\t\t  3. Number of upper case letters: {str(count_upp_char)}  ")
    print(f"\t\t\t  4. Number of digits : {str(num_count)}            ")
    print(f"\t\t\t  5. Number of special char : {str(strong_char)}      ")
    print("\t\t\t\t****************************************")

    check_pass_strength_by_special_char(strong_char,count_pass)
    check_pass_strength_by_digits(num_count, count_pass)
    check_pass_strength_by_upper_case(count_upp_char, count_pass, password)


## >> Check password length  << ##
def check_password_length(count_pass,password):

    if count_pass < 17:
     print("\n           **************************************************")
     text = colored("           *  Is your personal data valuable to you or not? *\n"
                    "           *   Password should be at least 17 characters.   *"
                    , color="red")
     print(text)
     print("           **************************************************\n")
     enter_pass()

    elif count_pass > 22 and count_pass < 30:
        print(""
              "\n\t\tJust make sure you can remember your password!")
        text =colored(""
              "\n\t\tMy suggestion is password length of 17-22 chracters,\n"
              "\t\t\t\tbut you are the boss of your password!\n", color= "red")
        print(text)

    elif count_pass > 30 :
        text =colored(""
              "\n\t\t\tAre you hasing a password or writing one?\n"
              "\t\t\t\tJust try again shorter password!\n", color= "red")

        print(text)
        enter_pass()

    else:
        print("\n\t\tEverything seems in place with your password length,\n"
              "\t\t\t\t\t\t Let's continue !\n")


## >> Check password strength according to number of special symbols << ##
def check_pass_strength_by_special_char(strong_char, count_pass):
    if (strong_char*4) < count_pass:
        message = colored( "\n\tPassword is good, " 
                  "but consider adding more special chars in it.\n", color= "blue")
        print(message)

        enter_pass()


## >> Check password strength according to number of digits << ##
def check_pass_strength_by_digits(num_count, count_pass):
    if (num_count*4) < count_pass:
        message = colored("\n\tPassword can be better, "
                          "there are not enough digits in it.\n", color= "blue")
        print(message)
        enter_pass()


## >> Check password strength according to number of upper case letters << ##
def check_pass_strength_by_upper_case(count_upp_char, count_pass, password):
    if(count_upp_char*5) < count_pass:
        message = colored("\n\t\tNot enough upper case characters in your password\n" 
                        "\t\t\t\t\tPlease try again :) !\n" ,color="blue")
        print(message)
        enter_pass()
    else:
        text = colored("\n\t\t\t\t\t\t Nice imagination!\n", color="green")
        print(text)
        print("\t\t\t\t\tThat's looks balanced password.\n")
        password_shuffle(password)
        end_program()

## >> Shuffle Password - sort of salting << ##
def password_shuffle(password):
    print("\t\t\t\t\t Now let us help you a bit: ")
    new_pass = list(password)
    random.shuffle(new_pass)
    upd_pass = ''.join(new_pass)
    print("\t\t\t\t\t"+ upd_pass)
    print("\n\t\t\t\t\t"
          "Now that looks"
          " better, great job!")

run_app_screen()


  ### >>> All rights reserverd - Amir Sillam - "My Password Garage!"  - 2021 <<< ###
  ### >>> All rights reserverd - Amir Sillam - "My Password Garage!"  - 2021 <<< ###
  ### >>> All rights reserverd - Amir Sillam - "My Password Garage!"  - 2021 <<< ###

























