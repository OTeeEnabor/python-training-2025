def check_eligibility(age:int) -> bool:
    eligible = False

    if age < 18:
        eligible = False
    else:
        eligible = True
    
    return eligible

for person in range(1,5):
    age = int(input("What is your age: "))
    is_eligible = check_eligibility(age)

    if is_eligible:
        print("Allowed to vote")
    else:
        print("Not allowed to vote")
