import re


def welcom() :

    """
    print welcom message 
    """
    print('''welcom to the  madlib_game :)
    
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
    merged_text=text.format(*tup)
    with open('assets/result.txt','w') as result:
        result.write(merged_text)
        print(merged_text)
    return merged_text

   


if __name__== "__main__":

    file_to_read=read_template("assets/dark_and_stormy_night_template.txt")
    text,words=parse_template(file_to_read)
    word_result=[]
    for i in words:
        user_input=input(f"Enter {i} >> ")
        word_result.append(user_input)
    madlib_result=merge(text,word_result)


