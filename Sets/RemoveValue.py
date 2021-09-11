'''
@Author: Ariprasath
@Date: 2021-09-11 12:51:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 12:55:00
@Title : Remove a value from the set
'''



class Error(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
class EmptySetError(Error):
    def __init__(self):
        self.message="Set is Empty"
        super().__init__(self.message)

def remove_value(sample_data, val):
    '''
    Description:
        Removes a value from the set
    Parameter:
        sample_data(set): contains unique data
        val(any type): value to be removed to the sample_data 
    Return:
        sample_data(set): The set with value removed
    Raises:
        EmptySetError: When an empty set is passed
    '''
    
    if len(sample_data)==0:
        raise EmptySetError
    else:
        sample_data.remove(val)
    return sample_data

if __name__=="__main__":
    sample_data=set()
    sample_data={1,3,5,7,9,0,11,13,15,17,19}
    try:
        print(remove_value(sample_data,22))
    except EmptySetError as E:
        print(E)
    except KeyError:
        print("The given value does not exist in the set provided")
