'''
@Author: Ariprasath
@Date: 2021-09-11 19:43:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 20:12:00
@Title : sepearte the multiple strings based on comma. sort all the uniques string alphabetically
'''

class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptyStringError(Error):
    def __init__(self):
        self.messgae="The string is empty"
        super().__init__(self.message)

def split_sort(sample_data):
    '''
    Description:
        sepearte the multiple strings based on comma. sort all the uniques string alphabetically
    Parameter:
        sample_data(string): a strings containing letters, numbers etc,..    
    Return:
        sample_data_list(list): A list that contains all the unique strings sorted alphabetically
    Raises:
        EmptyStringError: Thrown when the passed string is empty
    '''

    sample_data_list=list(set(sample_data.split(",")))
    sample_data_list.sort()
    return sample_data_list

if __name__=="__main__":
    sample_data="red,white,black,red,green,black"
    try:
        print(split_sort(sample_data))
    except EmptyStringError as E:
        print(E)
