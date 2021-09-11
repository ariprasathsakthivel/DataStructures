'''
@Author: Ariprasath
@Date: 2021-09-11 14:45:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 14:50:00
@Title : Find the maximum and minimum number
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



def max_min(sample_data):
    '''
    Description:
        Finds the maximum and minimum number
    Parameter:
        sample_data(list): contains integer values
    Return:
        max(int): Maximum number in the sample_data
        min(int): Minimum number in the sample_data
    Raises:
        EmptyListError: Thrown when the passed list is empty
        NonIntError: Thrown when the list contains non-integers
    '''
    max=int()
    min=int()
    if len(sample_data)==0:
        raise EmptyListError
    elif non_int(sample_data):
        raise NonIntError
    else:
        sample_data.sort()
        return sample_data[0],sample_data[len(sample_data)-1]

if __name__=="__main__":
    sample_data=[2,5,1,6,2,8,2,32,4,3,2]
    # sample_data=[]
    try:
        print(f"Maximum number-->{max_min(sample_data)[0]}\nMinimum number-->{max_min(sample_data)[1]}")
    except EmptyListError as E:
        print(E)
    except NonIntError as I:
        print(I)
