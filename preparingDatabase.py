
def poster(name,post):
    if(post==""):
        print('Your post is empty add something')
        post = input('type here: ... ')
    else:
        choice = int(input("you posted something click one to see your post and 0 to exit: "))
        if(choice==1):
            print("this is your post:\n\t\t\t",post)
        elif(choice==0):
            return 0