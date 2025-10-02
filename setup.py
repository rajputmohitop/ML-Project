from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]
        
        if '-e .' in requirement:
            requirement.remove('-e .')
    return requirement        
setup(
    name="ML Project",
    version="0.0.1",
    author="Mohit",
    author_email="Mohit.rajput010105@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)