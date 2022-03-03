# from preparingDatabase import poster
import preparingDatabase
print('this is my first file')
name = input('enter your name : ')
number = input('enter your phone number: ')
print('your name is ',name,' and your phone number is ',number)
post = "Bonjour mes fans je suis la pour vous. "
preparingDatabase.poster(name,post)
intervenant = preparingDatabase.chat(name)

