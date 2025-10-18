from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    # On reading all the lines separately it will also read \n that is used for read lines
    # so in order to remove that we will replace \n with an empty space
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in requirements]
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version='0.0.1',
    author="Keshav Garg",
    author_email="keshugarg292005@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
