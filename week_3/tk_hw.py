Id_number = input(9802115987084)
    if len(id_number) != 13 or not id_number.isdigit():
        return "invalid ID number. It should be exactly 13 digits long."
    return "ID number valid"



dob_str = id_number[0:6]


year = int(dob_str[0:2])
month = int(dob_str[2:4])
day = int(dob_str[4:6])

id_number = input(9802115987084)
dob = extract_dob_from_id(id_number)

print("your date of birth is" , dob)