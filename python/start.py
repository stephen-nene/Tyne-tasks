# set a variable
caps = 'STEVE'
message = 'Steve is a dev'
message2 = 'steve\'s cat is orange'
message3 = """this is a new line
but so is this"""

# print the message
print("hello world!")
print(message)
print(message2)
print(message3, message3[-1]) 
print(len(message))

# prints the first character uto but not including the 2 index
print(message[0:2])
print(message[2:])

print(caps.lower(), message.upper())
# it returns a new string
print(message.replace('Steve', 'John')) 
print(message.count('e'),message.find('is'))

name = "Nene"
greeting = 'hello there'
ask = 'how are you?'

greethim = '{}, {}. {} Welcome to Tyne!'.format(greeting, name,ask)
greethim2 = f'{greeting},{name.upper()} {ask} Welcome to Tyne!'
print(greethim,greethim2)

# print(dir(ask))
print(help(str.upper))