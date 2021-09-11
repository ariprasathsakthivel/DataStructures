'''
@Author: Ariprasath
@Date: 2021-09-11 16:09:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 16:19:00
@Title : Removes a member
'''



class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptytupleError(Error):
    def __init__(self):
        self.message="The tuple is empty"
        super().__init__(self.message)



def remove_member(sample_data,val):
    '''
    Description:
        Removes a values
    Parameter:
        sample_data(tuple): contains members of a tuple
        val(any type): member to be removed
    Return:
        sample_data_list(tuple): a tuple without the values
    Raises:
        EmptytupleError: Thrown when the passed tuple is empty
    '''
    sample_data_list=list(sample_data)
    if len(sample_data)==0:
        raise EmptytupleError
    else:
        sample_data_list.remove(val)
    return tuple(sample_data_list)

if __name__=="__main__":
    sample_data=(2,5,1,6,2,8,2,32,4,3,2)
    # sample_data=[]
    try:
        print(remove_member(sample_data,2))
    except EmptytupleError as E:
        print(E)
    except ValueError as V:
        print("Value not found")
