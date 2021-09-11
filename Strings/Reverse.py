'''
@Author: Ariprasath
@Date: 2021-09-11 18:55:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-11 19:03:00
@Title : Reverse a string and print it
'''

class Error(Exception):
    def __init__(self,message):
        super().__init__(self.message)
class EmptyStringError(Error):
    def __init__(self):
        self.messgae="The string is empty"
        super().__init__(self.message)

if __name__=="__main__":
    try:
        sample_data="abcdefg"
        sample_data_list=list(sample_data)
        sample_data_list.reverse()
        sample_data="".join(sample_data_list)
    except EmptyStringError as E:
        print(E)
    else:
        print(f"Reversed string-->{sample_data}")