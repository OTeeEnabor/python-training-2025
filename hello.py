def greet_user()-> None:
    print("hello guys")

def check_age_function():
    age = input('Enter Your Age:')

    if int(age) >= 18 and int(age) < 21:
        print('Welcome to a diploma degree')
    elif int(age) >= 21:
        print('Welcome to a uni degree')   
    else:
        print('Not allowed')
    
# greet_user()

check_age_function()
