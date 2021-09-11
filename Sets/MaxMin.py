'''
@Author: Ariprasath
@Date: 2021-09-11 13:07:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 13:15:00
@Title : Maximum and minimum value in the set
'''



class Error(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
class EmptySetError(Error):
    def __init__(self):
        self.message="Set is Empty"
        super().__init__(self.message)

def max_min_value(sample_data):
    '''
    Description:
        Finds the maximum and minimum value in a set
    Parameter:
        sample_data(set): contains unique data
    Return:
        max_value(any type): Maximum value
        min_value(any type): Minimum value
    Raises:
        EmptySetError: When an empty set is passed
    '''
    sample_data_list=list(sample_data)
    if len(sample_data)==0:
        raise EmptySetError
    else:
        sample_data_list.sort()
        min_value=sample_data_list[0]
        max_value=sample_data_list[len(sample_data_list)-1]
    return min_value,max_value

if __name__=="__main__":
    sample_data=set()
    sample_data={1,3,5,7,9,0,11,22,15,50,19}
    try:
        print(f"Minimum value-->{max_min_value(sample_data)[0]}\nMaximum values-->{max_min_value(sample_data)[1]}")
    except EmptySetError as E:
        print(E)