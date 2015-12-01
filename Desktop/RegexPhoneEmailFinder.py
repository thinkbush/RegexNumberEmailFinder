#! Python3

import re, pyperclip



#TODO: Create a regex for phone numbers

phoneRegex = re.compile(r'''
\d\d\d\d\s\d\d\d\d   # Format: 3919 3001 8-digit telephone number seperated by one whitespace;
                    
''',re.VERBOSE)



#TODO: Create a regex for email addresses

emailRegex = re.compile(r'''
#sth@sth.sth.sth
[a-zA-Z0-9_.+]+    #name part
   @               # @ symbol
[a-zA-Z0-9_.+]+    # domain name part
''',re.VERBOSE)


#TODO: Get the text off the clipboard

text = pyperclip.paste()

#TODO: Extract the email/phone from this text
extractedPhones = phoneRegex.findall(text)
extractedEmails = emailRegex.findall(text)



#TODO: Copy the extracted email/phone to the clipboard and get rid of '' or ,
results = '\n'.join(extractedPhones) + '\n'*5 + ','.join(extractedEmails)
pyperclip.copy(results)

