import string
import random


# function to Collect details first name, last name, email.
def get_employee_details():
  first_name = input('Enter your firstname: ')
  last_name = input('Enter your lastname: ')
  email_address = input('Enter your email address: ')
  employee_details = [ first_name, last_name, email_address]
  return employee_details
# print(get_employee_details())


def generate_employee_password(employee_details):
  # Generate random password for the user joining the first 2 letters of the first name and last 2 letters of the last name with a random string of length 5. This makes your password 9 letters long.
  length_to_generate = 5
  get_random_str_length_five = ''.join(random.choice(string.ascii_lowercase) 
            for i in range(length_to_generate))
  employee_random_password = str(employee_details[0][0:2] + employee_details[1][-2:] + get_random_str_length_five)
  return employee_random_password


state = True
# dict to store user data
users_data = {}
user_data_key = 1

while state:
  user_info = get_employee_details()
  
  display_password = generate_employee_password(user_info)
  print('Your password is: ' + str(display_password))
  
  is_pass_ok = input(str('Are you satisfied with this password. If yes enter Yes If no, enter No then please supply password: '))
  break
  
  
  while True:
    if is_pass_ok == 'Yes':
      user_info.append(display_password)
      users_data[user_data_key] = user_info
      break
      
    else:
      user_password = input(str('Enter password greater than or equal to 7: '))
      break

      while True:
        if len(user_password) >= 7:
          user_info.append(user_password)
          users_data[user_data_key] = user_info
          break
          
        else:
          print('Your password is less than 7')
          user_password = input(str('Enter password greater than or equal to 7: '))
          
          
  new_employee = input(str('Would you like to enter a new employee? Yes or No: '))
  if (new_employee == 'No'):
    state = False
    for employee in users_data:
      print(users_data.get(employee))
        
  else:
    state = True
    user_key = user_key + 1