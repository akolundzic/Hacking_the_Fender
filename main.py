# 1 
import csv
# 12 
import json
# 2 
compromised_users = []
# 3 
with open('passwords.csv') as password_file:
# 4 
  password_csv = csv.DictReader(password_file)
#5,6 
# 7 
  compromised_users = [password_row['Username'] for password_row in password_csv ]

# 8 
with open('compromised_users.txt','w') as compromised_user_file:
# 9 
  for user in compromised_users:
# 10 
      compromised_user_file.write(user)

# 14 
boss_message_dict = {
  "recipient":"The Boss",
  "message":"Mission Success"
}
# 13 
with open('boss_message.json','w') as boss_message:
# 15 Write out boss_message_dict to boss_message 
  json.dump(boss_message_dict,boss_message)
# 17 
slash_null_sig = '''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
'''
# 16 
with open('new_passwords.csv','w') as new_passwords_obj:
# 18 
  new_passwords_obj.write(slash_null_sig)






  


  








