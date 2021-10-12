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


