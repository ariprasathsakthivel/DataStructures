'''
@Author: Ariprasath
@Date: 2021-09-11 09.:37:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 09:50:00
@Title : Creating a set and iterating through it
'''



class Error(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
class EmptySetError(Error):
    def __init__(self):
        self.message="Set is Empty"
        super().__init__(self.message)

def set_iterator(sample_data):
    '''
    Description:
        Takes a set, iterate it and prints each item
    Parameter:
        sample_data(set): contains unique data
    Return:
        None
    Raises:
        EmptySetError: When an empty set is passed
    '''
    if len(sample_data)==0:
        raise EmptySetError
    else:
        for elements in sample_data:
            print(elements)

if __name__=="__main__":
    sample_data=set()
    sample_data={1,3,5,7,9,0,11,13,15,17,19}
    try:
        set_iterator(sample_data)
    except EmptySetError as E:
        print(E)
