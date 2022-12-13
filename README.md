# Hacking the Fender 
## Description
### This is an exercise from the Python3 Codecademy course
The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to The Fender‘s systems, you must update his "passwords.txt" file to scramble the secret data. The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat.

Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice. Work with CSV files and other text files in this exploration of the strength of Python file programming.

## Steps
1. Are you there? We’ve opened up a communications link to The Fender‘s secret computer. We need you to write a program that will read in the compromised usernames and passwords that are stored in a file called "passwords.csv".First import the CSV module, since we’ll be needing it to parse the data.
2. We need to create a list of users whose passwords have been compromised, create a new list and save it to the variable compromised_users.
3. Next we’ll need you to open up the file itself. Store it in a file object called password_file.
4. Pass the password_file object holder to our CSV reader for parsing. Save the parsed csv.DictReader object as password_csv.
5. Now we’ll want to iterate through each of the lines in the CSV.Create a for loop and save each row of the CSV into the temporary variable password_row.
6. Inside your for loop, print out password_row['Username']. This is the username of the person whose password was compromised. Run your code, do you see a list of usernames?
7. Remove the print statement. We want to add each username to the list of compromised_users. Use the list’s .append() method to add the username to compromised_users instead of printing them.
8. Exit out of your with block for "passwords.csv". We have all the data we need from that file. Start a new with block, opening a file called compromised_users.txt. Open this file in write-mode, saving the file object as compromised_user_file.
9. Inside the new context-managed block opened by the with statement start a new for loop. Iterate over each of your compromised_users.
10. Write the username of each compromised_user in compromised_users to compromised_user_file.
12. Your boss needs to know that you were successful in retrieving that compromised data. We’ll need to send him an encoded message over the internet. Let’s use JSON to do that.First we’ll need to import the json module.
13. Open a new JSON file in write-mode called boss_message.json. Save the file object to the variable boss_message.
14. Create a Python dictionary object within your with statement that relays a boss message. Call this boss_message_dict. Give it a "recipient" key with a value "The Boss". Also give it a "message" key with the value "Mission Success".
15. Write out boss_message_dict to boss_message using json.dump().
16. Now that we’ve safely recovered the compromised users we’ll want to remove the "passwords.csv" file completely. Create a new with block and open "new_passwords.csv" in write-mode. Save the file object to a variable called new_passwords_obj.
17. Enemy of the people, Slash Null, is who we want The Fender to think was behind this attack. He has a signature, whenever he hacks someone he adds this signature to one of the files he touches. Signature, look at the main.py slash_null_sig.
18. Write slash_null_sig to new_passwords_obj. Now we have the file to replace passwords.csv with!
