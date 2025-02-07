# Write a CLI program that checks whether a person is eligible to vote in RSA.
# Input
# output is Yes and No

# input()


"""
PSEUDO CODE - decide if they can vote
What is the criteria? Age

Ask age
if age is voting age
can vote
else
cant vote

end program

"""
def check_eligibility(age:int) -> bool:
    eligible = False

    if age < 18:
        eligible = False
    else:
        eligible = True
    
    return eligible

    
# age = int(input("What is your age: "))
# eligible = False

# if age < 18:
#     eligible = False
# else:
#     eligible = True

# if eligible:
#     print("Allowed to vote")
# else:
    print("Not allowed to vote")

# 100 people
# for loop 
# for person in range(1,5):
#     age = int(input("What is your age: "))
#     eligibility


#     print(person)