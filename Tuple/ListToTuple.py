'''
@Author: Ariprasath
@Date: 2021-09-11 15:246:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 15:50:00
@Title : converts a list to tuple
'''



class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptytupleError(Error):
    def __init__(self):
        self.message="The tuple is empty"
        super().__init__(self.message)




def list_to_tuple(sample_data):
    '''
    Description:
        Converts a list to tuple
    Parameter:
        sample_data(list): contains various members
    Return:
        sample_data_tuple(tuple): contains members that are in the reversed order
    Raises:
        EmptytupleError: Thrown when the passed tuple is empty
    '''
    sample_data_tuple=tuple()
    if len(sample_data)==0:
        raise EmptytupleError
    else:
        sample_data_tuple=tuple(sample_data)
    return tuple(sample_data_tuple)


if __name__=="__main__":
    sample_data=[2,5,1,6,2,8,2,32,4,3,2]
    # sample_data=[]
    print(type(sample_data))
    try:
        print(type(list_to_tuple(sample_data)))
    except EmptytupleError as E:
        print(E)
