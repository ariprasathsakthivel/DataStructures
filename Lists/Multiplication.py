'''
@Author: Ariprasath
@Date: 2021-09-11 14:33:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 14:40:00
@Title : multiplies all the members in a list
'''



class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptyListError(Error):
    def __init__(self):
        self.message="The list is empty"
        super().__init__(self.message)
class NonIntError(Error):
    def __init__(self):
        self.message="The list contains non-integers"
        super().__init__(self.message)

def non_int(sample_data):
    '''
    Description:
        checks whether any non-integer value is there in the list passed or not
    Parameter:
        sample_data(list): list containing member to be checked
    Return:
        boolean value(bool): True if the list contains non-integers and False if the list contains only integers
    Raises:
        EmptyListError: Thrown when an empty list is passes
        NonIntError: Thrown when the list contains non-integers
    '''
    for element in sample_data:
        if type(element)==int:
            pass
        else:
            return True
            break
        return False



def multiple_members(sample_data):
    '''
    Description:
        Multiplies all the members in the list
    Parameter:
        sample_data(list): contains integer values
    Return:
        Multiple(int): multiplied value of all the members in the given list
    Raises:
        EmptyListError: Thrown when the passed list is empty
        NonIntError: Thrown when the list contains non-integers
    '''
    multiple=int()
    multiple=1
    if len(sample_data)==0:
        raise EmptyListError
    elif non_int(sample_data):
        raise NonIntError
    else:
        for element in sample_data:
            multiple*=element
    return multiple

if __name__=="__main__":
    sample_data=[2,3]
    # sample_data=[]
    try:
        print(f"Multiple-->{multiple_members(sample_data)}")
    except EmptyListError as E:
        print(E)
    except NonIntError as I:
        print(I)
