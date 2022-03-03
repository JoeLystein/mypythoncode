list_inter =['paul smith','eddie Murphy', 'joseph matk', 'robbin de bois']
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

def chat(name):
    print('this is people who are available to talk with you:\n')
    print(list_inter)
    choice = int(input('choose one base on their number: '))
    print (name,'you chose to talk with',list_inter[choice-1])
    return list_inter[choice-1]
