import re

print("Welcome You are in the Madlib Game")

def read_template(path):
    """ function how read file from the url
        and return what that file have 
    """ 
    a=open(path)
    return a.read()

def parse_template(input):
    '''
    takes a text as input and return a tuple and a string without the words
    in the tupple and uses regex to idenitify the required word 
    '''
    actual_stripped=''
    actual_parts=[]

    x=input.split(' ')
    print(x)
    reg=r"^{\w+}|\.$"
    for i in x:
        if re.match(reg,i)==None :
            actual_stripped+=f"{i} "
        else :
            if i==x[-1]:
                actual_stripped+='{}.'
                actual_parts+=[i[1:-2]]
            else:
                actual_parts+=[i[1:-1]]
                actual_stripped+='{} '

    actual_parts=tuple(actual_parts)
    return (actual_stripped,actual_parts)


def merge(theText,tup):
    '''
    takes 2 inputs text and a tuple and joins the tuples elemnts with the string insted of 
    { } in the string
    '''
    return theText.format(*tup)


def create_file(result):

    '''
    takes in text and creat a file with that  details and then writes to that file 
    the arguments of that text 
    '''
    with open("assets/make_me_a_video_game_output_from_user.txt", "w") as f:
        f.write(result)

