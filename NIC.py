# A program to extract data from NIC

import datetime
now = datetime.datetime.now()
current_year = int(now.year)

NIC = input("Please type your NIC number: ")

# Defining a function for the output
def output(id, newORold, birth_year, gen, voteORnot):
    print(f"You are NIC number: {id}")
    print(f"NIC Type: {newORold}.")
    print(f"You were born on {birth_year}.")
    print(f"You are a {gen}.")
    print(f"You are a {voteORnot}.")

# User input validation
if len(NIC) != 12 and len(NIC) != 10 :
    print("Invalid NIC")
else:
    
    # new or old ID
    NewOrOld = NIC[-1] # -1 iterate from right to left
    if NewOrOld == "V" or NewOrOld == "X":
        
        # For Old IDs
        type = "Old"
        birthYear = int(NIC[0:2]) # String Slicing
        birthYear = 1900 + birthYear    # !!! Birth years older than 1900 are not mentioned in the problem statement !!!

        # male of female
        genderNum = int(NIC[2:5])
        if 1 <= genderNum <= 366:
            gender = "male"
        elif 501 <= genderNum <= 866:
            gender = "female"

        # voter or note
        age = current_year - birthYear
        if age >= 18:
            voter_or_not = "voter"
        else:
            voter_or_not = "none-voter"
        output(NIC, type, birthYear, gender, voter_or_not)

    else:
        if NewOrOld == "v" or NewOrOld == "x" :
            print("Invalid NIC")
        else:
            # for new IDs
            type = "New"

            # birth year
            birthYear = int(NIC[0:4])

            # male of female
            genderNum = int(NIC[4:7])
            if 1 <= genderNum <= 366:
                gender = "male"
            elif 501 <= genderNum <= 866:
                gender = "female"

            # voter or not
            age = 2021 - birthYear
            if age >= 18:
                voter_or_not = "voter"
            else:
                voter_or_not = "none-voter"
            output(NIC, type, birthYear, gender, voter_or_not)