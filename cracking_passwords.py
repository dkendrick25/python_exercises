## Bonus: Exercise 4 - Cracking Passwords

# You hacked into a high-security system and found a database of user accounts. The only problem is the passwords have been encrypted. You know that md5 is a popular but weak hashing scheme that is used by many companies to encrypt user passwords. If you are lucky, you can use a rainbow table attack using common english words from a dictionary to recover the plain-text passwords.
#
# You have access to a list of the most common words common_words.txt, and the user accounts: accounts.json. Read up on how to use md5:
#
# https://docs.python.org/2/library/md5.html

import md5
import json
common_words = open("common_words.txt")
content = common_words.read()
content = content.split('\n')
encrypted_common_words = {}
for word in content:
    plaintext_password = word
    m = md5.new()
    m.update(plaintext_password)
    encrypted_password = m.hexdigest()
    encrypted_common_words[encrypted_password] = word
# print encrypted_common_words

file = open('accounts.json', 'r')
accounts = json.loads(file.read())
count = 0
for account in accounts:
    password = account.get('password')
    username = account.get('username')
    if password in encrypted_common_words:
        count = count + 1
        print username +  ": " + encrypted_common_words[password]

print count "accounts cracked"
