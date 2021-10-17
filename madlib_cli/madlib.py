import re




def read_template(path):
    """ function how read file from the url
        and return  thr file data 
    """ 
    try:
      data=open(path)
      return data.read()
    except:
        raise FileNotFoundError(
         'file not found')  

def parse_template(input):
    '''
    takes a text as input (which we took from the file )and return a tuple and a string without the words
    in the tupple and uses regex to idenitify the required word 
    '''
    word_types=tuple(re.findall(r'{(.*?)}',input))

    text=re.sub('{.*?}','{}',input)

    return text,word_types



def merge(text,word):
    """
    merge function that takes in a “bare” template and a list of user entered language parts, 
    and returns a string with the language parts inserted into the template.
    """
    merged_text=text.format(*word)
    with open('assets/final_reslut.txt','w') as result:
        result.write(merged_text)
        print(merged_text)
    return merged_text

   

############################   testing  #####################################

def run_game():
   file_to_read=read_template("assets/dark_and_stormy_night_template.txt")
   text,words=parse_template(file_to_read)
   word_result=[]
   for i in words:
      user_input=input(f"Enter {i} >> ")
      word_result.append(user_input)
   madlib_result=merge(text,word_result)



# """
# print welcom message 

# note : incase of error runt the program again
# """
# print('''welcom to the  madlib_game :)''')
# run_game()



