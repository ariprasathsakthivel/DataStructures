'''
@Author: Ariprasath
@Date: 2021-09-11 19:19:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 19:40:00
@Title : Replace a charater into $
'''

class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptyStringError(Error):
    def __init__(self):
        self.messgae="The string is empty"
        super().__init__(self.message)
    
def char_replace(sample_data):
    '''
    Description:
        Checks the first character in a string throughout the string and replaces it with $
    Parameter:
        sample_data(string): a strings containing letters, numbers etc,..
    Return:
        sample_data(string): string that is replaced with the $ character
    Raises:
        EmptyStringError: Thrown when the passed string is empty
    '''

    replace_val=sample_data[0]
    sample_data=sample_data[1:].replace(sample_data[0],"$")
    return replace_val+sample_data

if __name__=="__main__":
    sample_data="restart"
    try:
        print(char_replace(sample_data))
    except EmptyStringError as E:
        print(E)