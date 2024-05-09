'''
    A contact list is a place where you can store a specific contact with other associated information such as a phone
    number, email address, birthday, etc.
    Write a program that first takes in word pairs that consist of a name and a phone number (both strings), separated
    by a comma.
    That list is followed by a name, and your program should output the phone number associated with that name.
    Assume the search name is always in the list.
        Ex: If the input is:
            Joe,123-5432 Linda,983-4123 Frank,867-5309
            Frank
        the output is:
            867-5309
'''
user_input = input('Enter name and phone number, separated by ",": ')
search_input = input('Enter the name you would like to search for: ')
entries = user_input.split(' ')
contacts = {}

for contact in entries:
    contact_pair = contact.split(',')
    contacts[contact_pair[0]] = contact_pair[1]

print(contacts[search_input])
