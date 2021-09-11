'''
@Author: Ariprasath
@Date: 2021-09-11 15:29:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 15:44:00
@Title : Reverse the tuple
'''



class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptytupleError(Error):
    def __init__(self):
        self.message="The tuple is empty"
        super().__init__(self.message)

def non_int(sample_data):
    '''
    Description:
        checks whether any non-integer value is there in the tuple passed or not
    Parameter:
        sample_data(tuple): tuple containing member to be checked
    Return:
        boolean value(bool): True if the tuple contains non-integers and False if the tuple contains only integers
    '''
    for element in sample_data:
        if type(element)==int:
            pass
        else:
            return True
            break
        return False



def reverse_tuple(sample_data):
    '''
    Description:
        Reverses a tuple
    Parameter:
        sample_data(tuple): contains integer values
    Return:
        sample_data(tuple): contains members that are in the reversed order
    Raises:
        EmptytupleError: Thrown when the passed tuple is empty
    '''
    sample_data_list=list(sample_data)
    if len(sample_data)==0:
        raise EmptytupleError
    else:
        sample_data_list.reverse()
    return tuple(sample_data_list)

if __name__=="__main__":
    sample_data=(2,5,1,6,2,8,2,32,4,3,2)
    # sample_data=[]
    try:
        print(reverse_tuple(sample_data))
    except EmptytupleError as E:
        print(E)
