'''
@Author: Ariprasath
@Date: 2021-09-11 09:56:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 10:03:00
@Title : Adding a new values in a set
'''



class Error(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
class EmptySetError(Error):
    def __init__(self):
        self.message="Set is Empty"
        super().__init__(self.message)

def add_value(sample_data, val):
    '''
    Description:
        Adds a values to the set
    Parameter:
        sample_data(set): contains unique data
        val(any type): value to be added to the sample_data 
    Return:
        None
    Raises:
        EmptySetError: When an empty set is passed
    '''
    if len(sample_data)==0:
        raise EmptySetError
    else:
        sample_data.add(val)
    return sample_data

if __name__=="__main__":
    sample_data=set()
    sample_data={1,3,5,7,9,0,11,13,15,17,19}
    try:
        print(add_value(sample_data,25))
    except EmptySetError as E:
        print(E)
