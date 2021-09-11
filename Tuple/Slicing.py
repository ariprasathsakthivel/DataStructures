'''
@Author: Ariprasath
@Date: 2021-09-11 16:31:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 16:40:00
@Title : Slice a tuple
'''



class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptytupleError(Error):
    def __init__(self):
        self.message="The tuple is empty"
        super().__init__(self.message)



def slice_tuple(sample_datal,lower_limit,upper_limit):
    '''
    Description:
        Slice a tuple excluding the upper limit
    Parameter:
        sample_data(tuple): contains members of a tuple
        lower_limit(int): lower index for strating the slicing operation
        upper_limit(int): upper index for stoping the slicing operation
    Return:
        sample_data_sliced(tuple): sliced values
    Raises:
        EmptytupleError: Thrown when the passed tuple is empty
    '''
    sample_data_sliced=tuple()
    if len(sample_data)==0:
        raise EmptytupleError
    else:
        sample_data_sliced=sample_data[lower_limit:upper_limit]
    return sample_data_sliced

if __name__=="__main__":
    sample_data=(0,1,2,3,4,5,6,7,8,9)
    # sample_data=[]
    try:
        print(slice_tuple(sample_data,1,6))
    except EmptytupleError as E:
        print(E)
