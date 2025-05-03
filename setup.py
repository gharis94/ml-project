from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            print('Removing -e . from requirements')
            requirements.remove(HYPHEN_E_DOT)

    return list(filter(None,requirements))


setup(
    name='mlproject',
    version='0.0.1',
    author='Gharis Bin Qasim',
    author_email='gharisbinqasim@gmail.com',
    description='A small example package',
    long_description='A small example package for learning purposes',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)