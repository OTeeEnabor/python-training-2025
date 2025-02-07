#code that accepts 13 digit id number
#extracts dob from first 6 numbers of the id num

id_num=input('enter your 13 digit id num')
dob=id_num[0:6]
print(dob)
# print(f'your date of birth is {id_num [0:7]}')

year={id_num[1:3]}
month={id_num[3:5]}
print(year, month)

# month={'11 is Nov'}
# date={id_num[5:7]}
# student_birthday=f'{year}:{month}:{date}'

# print(f'your date of birth is {student_birthday}')