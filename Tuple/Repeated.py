'''
@Author: Ariprasath
@Date: 2021-09-11 16:30:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 16:26:00
@Title : Find the repeated items
'''


class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptytupleError(Error):
    def __init__(self):
        self.message="The tuple is empty"
        super().__init__(self.message)



def repeats(sample_data):
    '''
    Description:
        finds the repeated items in a tuple
    Parameter:
        sample_data(tuple): contains members of a tuple
    Return:
        repeated_items(Dictionary): contains the repeated tuple members as keys and their counts a values 
    Raises:
        EmptytupleError: Thrown when the passed tuple is empty
    '''
    repeated_items=dict()
    if len(sample_data)==0:
        raise EmptytupleError
    else:
        for element in sample_data:
            if sample_data.count(element)>1:
                repeated_items[element]=sample_data.count(element)
            else:
                continue
    return repeated_items

if __name__=="__main__":
    sample_data=(2,5,1,6,2,8,2,32,4,3,2,1,1,2,3,4,4,4,5,5,6,7,7,7,8,8)
    # sample_data=[]
    try:
        print(repeats(sample_data))
    except EmptytupleError as E:
        print(E)
    except ValueError as V:
        print("Value not found")
