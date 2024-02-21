# Day 2: 30 Days of python programming

# variables
first_name = 'Sachin'
last_name = 'Tendulkar'
full_name = 'Sachin Tendulkar'
country = 'India'
city = 'Mumbai'
age = 50
year = 2024
is_married = True
is_true = True
is_light_on = True

# multiple variables on one line
national_team, ranchi_team, ipl_team = 'INDIA', 'Maharastra', 'Mumbai Indians'

# datatype of the variables
type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)

# length of the first name
print(len(first_name))

# comparing the length of first_name and last_name
first_name_length = len(first_name)
last_name_length = len(last_name)
print(first_name_length, last_name_length)


num_one = 5
num_two = 4
total = num_one + num_two                   # sum
diff = num_one - num_two                    # difference
product = num_two * num_one                 # multiply
division = num_one / num_two                # division
remainder = num_two % num_one               # modulus
exp = num_one ** num_two                    # power
floor_division = num_one // num_two         # integer division


radius = 30

# area of a circle
area_of_circle = 3.14 * radius ** 2
print("Area of a circle", area_of_circle)

# circumference of a circle
circum_of_circle = 2 * 3.14 * radius
print("Circumference of a circle", circum_of_circle)

# area of a circle with the user input
r = float(input('enter the radius'))
area = 3.14 * r ** 2
print("Area of the circle with the given radius is", area)

