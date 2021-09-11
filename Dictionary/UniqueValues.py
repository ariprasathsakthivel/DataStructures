'''
@Author: Ariprasath
@Date: 2021-09-11 08:04:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 08:25:00
@Title : Print the unique values from a list containing multiple dictionary objects
'''

class Error(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
class EmptyListError(Error):
    def __init__(self):
        self.message="List is Empty"
        super().__init__(self.message)
class NotListError(Error):
    def __init__(self):
        self.message="Input argument is not a list"
        super().__init__(self.message)


def uniques_values(sample_data):
    '''
    Description:
        Returns a set containing unique values.
    Parameter:
        sample_data(list): Contains multiple dictionary objects(contains only one key-values pair)
    Return:
        unique_data(set): Contains the uniques values filtered from the sample_data
    Raises:
        EmptyListError: In case of empty list is passed
        NotLisrError: If the passed argument is not of the type list
    '''
    unique_data=set()
    if len(sample_data)==0:
        raise EmptyListError
    elif type(sample_data)!=list:
        raise NotListError
    else:
        for element in sample_data:
            unique_data.add(list(element.values())[0])
    return unique_data

if __name__=="__main__":
    sample_data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    try:
        print(uniques_values(sample_data))
    except EmptyListError as E:
        print(E)
    except NotListError as N:
        print(N)
    