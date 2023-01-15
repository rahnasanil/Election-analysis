temperature=int(input("What is the temperature outside? "))
if temperature>80:
   print("turn on th ac")
else:
   print("open the windows")

   #What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


# What is the score?
score=int(input("wats ur test score?") )
# determine the grade
if score>=90:
   print("grade is A")
elif score>=80:
   print('drade is B')
elif score>=70:
   print('grade is C')
elif score>=60:
   print('grade is D')
else:
   print('grade is E')

 # Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
