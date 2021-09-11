'''
@Author: Ariprasath
@Date: 2021-09-11 19:05:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 19:15:00
@Title : Reverse a string and print it
'''

class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptyStringError(Error):
    def __init__(self):
        self.messgae="The string is empty"
        super().__init__(self.message)

def counts(sample_data):
    '''
    Description:
        calculates the count of all the characters in the string
    Parameter:
        sample_data(string): a strings containing letters, numbers etc,..
    Return:
        items_count(Dictionary): contains the counts of each characters as values and each characters as a key
    Raises:
        EmptyStringError: Thrown when the passed string is empty
    '''
    items_count=dict()
    if len(sample_data)==0:
        raise EmptyStringError
    else:
        for element in sample_data:
            items_count[element]=sample_data.count(element)
    return items_count

if __name__=="__main__":
    sample_data="google.com"
    try:
        print(counts(sample_data))
    except EmptyStringError as E:
        print(E)