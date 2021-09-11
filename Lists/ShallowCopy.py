'''
@Author: Ariprasath
@Date: 2021-09-11 15:20:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 15:25:00
@Title : print the list after removing the 0th, 4th and 5th elements
'''



class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptyListError(Error):
    def __init__(self):
        self.message="The list is empty"
        super().__init__(self.message)


def copy_list(sample_data):
    '''
    Description:
        Copies or clones a list
    Parameter:
        sample_data(list): contains list members
    Return:
        sample_data_copy(list): contains all the list members of sample_data
    Raises:
        EmptyListError: Thrown when the passed list is empty
    '''
    sample_data_copy=list()
    if len(sample_data)==0:
        raise EmptyListError
    else:
        sample_data_copy=sample_data.copy()
    return sample_data_copy

if __name__=="__main__":
    sample_data=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print(id(sample_data))
    try:
        print(id(copy_list(sample_data)))
    except EmptyListError as E:
        print(E)
