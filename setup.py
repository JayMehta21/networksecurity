'''
setup.py file is important because it plays an essential part in packaging and distributing python projects.
it is used by setuptools to handle configurations , such as its metadata , packages and more...  
'''

from setuptools import find_packages , setup 
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_lst:list[str] = []
    try:
        with open('requirements.txt' ,'r') as file:
            #Read lines from the file 
            lines = file.readlines()
            #process each lines
            for line in lines:
                requirement = line.strip()
                ##ignore  empty lines and -e. 
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst


##print(get_requirements())
setup(
     name="NetworkSecurity",
     version = '0.0.1',
     author = "Jay Mehta",
     author_email= "jaykalpeshmehta2gmail.com",
     packages= find_packages(),
     install_requires = get_requirements() 
 )


 