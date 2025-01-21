
"""
Input = id in string format
function = determine date of birth
output = date of birth string  - day/month(words)/year

Use the SA ID format
yymmdd1234567 - 13 character string

# step 1 identify relevant sections
year -> first 2 characters in input string
month -> 3rd and 4th characters in input string
day -> 5th and 6th character in input string

# Start
# Create Function variables
current_year
month_tuple - (January, February, March, April, May, June, July, August, September, October, November, December)
month_number of days - (31,28/29,31,30,31,30,31,31,30,31,30,31)
current_Day
1- Check if input is string and has 13 characters
if fails end program and inform user
2- if string and is 13 characters
- set year, month, day variables
3 - determine year
    a - year cannot be greater than current year
    if year greater than current year return error
4 determine month
must be a valid motnh
else return error
5 - check day
day must be valid for that month
- cannot be less than 0
- cannot be greater than number of days for that month
"""

sample_id = "2501172532521"

def get_date_of_birth_string(id_string:str) -> str:
    CURRENT_YEAR = "2025"
    MONTH_STRING_TUPLE = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    # =============================
    is_string = isinstance(id_string,str) # True or False
    if not is_string or len(id_string)!=13:
        return "Input is not in correct format."
    
    # Collect important information
    year_id = id_string[:2]
    month_id = id_string[2:4]
    day_id = id_string[4:6]
    
    # convert year to int
    year_int = int(year_id)
    if year_int >= 0 and year_int <= 25:
        year=f"20{year_id}"
    else:
        year = f"19{year_id}"

    # convert month
    month_int = int(month_id)
    if month_int > 12 or month_int == 0 or month_int < 0:
        return "Error incorrect month"
    else:
        month_string_index = month_int - 1
        month_string = MONTH_STRING_TUPLE[month_string_index]
    


print(get_date_of_birth_string("24110000000"))
