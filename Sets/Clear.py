'''
@Author: Ariprasath
@Date: 2021-09-11 13:07:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 13:25:00
@Title : clears the entire set
'''



class Error(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
class EmptySetError(Error):
    def __init__(self):
        self.message="Set is Empty"
        super().__init__(self.message)

def clear_set(sample_data):
    '''
    Description:
        clears the set
    Parameter:
        sample_data(set): contains unique data
    Return:
        sample_data(set): contains no members. an empty set
    Raises:
        EmptySetError: When an empty set is passed
    '''
    if len(sample_data)==0:
        raise EmptySetError
    else:
        sample_data.clear()
    return sample_data

if __name__=="__main__":
    sample_data=set()
    sample_data={1,3,5,7,9,0,11,22,15,50,19}
    try:
        print(len(clear_set(sample_data)))
    except EmptySetError as E:
        print(E)