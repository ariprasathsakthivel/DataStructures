'''
@Author: Ariprasath
@Date: 2021-09-10 08:50:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-10 21:58:00
@Title : Sort the values in a dictionary
'''

class Error(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
class EmptyDictionaryError(Error):
    def __init__(self):
        self.message="Dictionary is Empty"
        super().__init__(self.message)

def value_sort(sample_data):
    '''
    Description:
        Extracts all the values from a dictionary and sorts it in the ascending order.
    Parameter:
        sample_data(Dictionary): contains key-values pairs of any datatype.
    Return:
        sorted_data(List): contains all the values sorted in ascending order.
    Raises:
        EmptyDictionaryError: if the passed argument is empty
    '''
    sorted_data=list
    if len(sample_data)==0:
        raise EmptyDictionaryError
    else:
        sorted_list=list(sample_data.values())
        sorted_list.sort()
    return sorted_list



if __name__=="__main__":
    sample_data={1: 30, 2: 20, 3: 10, 4: 100, 5: 90, 6: 60}
    try:
        print(value_sort(sample_data))
    except EmptyDictionaryError as E:
        print(E)