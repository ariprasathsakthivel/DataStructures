'''
@Author: Ariprasath
@Date: 2021-09-11 19:43:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 19:55:00
@Title : Swap the case of the input string
'''

class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptyStringError(Error):
    def __init__(self):
        self.messgae="The string is empty"
        super().__init__(self.message)
class NonAlphabetError(Error):
    def __init__(self, message):
        self.message="The entered values contains values other than alphabets"
        super().__init__(self.message)
    
def case_swap():
    '''
    Description:
        Takes a string from the user and swaps the upper and lower case characters
    Parameter:
        None
    Return:
        sample_data(string): string that's case swapped
    Raises:
        EmptyStringError: Thrown when the passed string is empty
        NonAlphabetError: Thrown when non-alphabets are given as an input
    '''

    sample_data=input("Please enter a string that has only alphabets")
    if len(sample_data)==0:
        raise EmptyStringError
    elif not(sample_data.isalpha()):
        raise NonAlphabetError
    else:
        sample_data=sample_data.swapcase()
    return sample_data

if __name__=="__main__":
    sample_data="restart"
    try:
        print(case_swap())
    except EmptyStringError as E:
        print(E)