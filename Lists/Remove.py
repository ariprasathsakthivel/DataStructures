'''
@Author: Ariprasath
@Date: 2021-09-11 14:55:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 15:13:00
@Title : print the list after removing the 0th, 4th and 5th elements
'''



class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptyListError(Error):
    def __init__(self):
        self.message="The list is empty"
        super().__init__(self.message)


def remove_specific_indexes(sample_data):
    '''
    Description:
        Removes 0th, 4th, 5th elements in a list
    Parameter:
        sample_data(list): contains list members
    Return:
        sample_data(list): sample_data parameter without the 0th, 4th, 5th elements
    Raises:
        EmptyListError: Thrown when the passed list is empty
    '''

    if len(sample_data)==0:
        raise EmptyListError
    elif len(sample_data)>=6:
        sample_data.pop(5)
        sample_data.pop(4)
        sample_data.pop(0)
    elif len(sample_data)<6:
        sample_data.pop(4)
        sample_data.pop(0)
    else:
        sample_data.pop(0)
    return sample_data

if __name__=="__main__":
    sample_data=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    try:
        print(remove_specific_indexes(sample_data))
    except EmptyListError as E:
        print(E)
