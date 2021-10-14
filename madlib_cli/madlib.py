import re


def welcom() :

    """
    print welcom message 
    """
    print('''welcom to the  madlib_game :)
    
     please  fill the blanks in the words
    ''')

def read_template(path):
    """ function how read file from the url
        and return what that file have 
    """ 
    try:
      data=open(path)
      return data.read()
    except:
        raise FileNotFoundError(
         'file not found')  

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
    new_text = theText.format(*tup)

    with open('assets/test.txt', 'w') as output:
        output.write(new_text)
    return new_text






