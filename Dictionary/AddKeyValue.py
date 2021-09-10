'''
@Author: Ariprasath
@Date: 2021-09-10 20:33:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-10 21:13:00
@Title : Add a key value pair to a existing dictionary
'''

class Error(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
class DuplicateKeyError(Error):
    def __init__(self):
        self.message="Key already exists"
        super().__init__(self.message)

def add_item(num_dict,key,value):
    '''
    Description:
        Takes a dictionary, key and value and adds it to the existing dictionary.
    Parameter:
        num_dict(Dictionary): The existing dictionary to which the new item needs to be added.
        key(int): The key of the new item to be added.
        value(int): The value of the new item to be added.
    Return:
        num_dict(Dictionary): A dictionary that contains the newly added item
    Raises:
        DuplicateKeyError: Thrown when the given key alreadt exists in the num_dict
    '''
    if key not in num_dict.keys():
        num_dict[key]=value
        return num_dict
    else:
        raise DuplicateKeyError
    
if __name__=="__main__":
    num_dict={0:10,1:20}
    try:
        add_item(num_dict,1,20)
    except DuplicateKeyError as D:
        print(D)
    else:
        print(num_dict)