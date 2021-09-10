'''
@Author: Ariprasath
@Date: 2021-09-10 22:04:30
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-10 22:17:00
@Title : converting a string into a dictionary where keys are the letters and values are the counts of each letters
'''

class Error(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
class EmptyStringError(Error):
    def __init__(self):
        self.message="String is Empty"
        super().__init__(self.message)


# name='w3resource'
name=str()
string_count=dict()
try:
    if len(name)==0:
        raise EmptyStringError
    else:
        for element in set(name):
            string_count[element]=name.count(element)
except EmptyStringError as E:
    print(E)
else:
    print(string_count)
