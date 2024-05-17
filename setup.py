from setuptools import find_packages, setup


HYPHEN_E_DOT = '-e .'

def get_requirements()->list[str]:
    with open('requirements.txt') as f:
        requirements_list = f.read().splitlines()

        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)

    return requirements_list


setup(
name='sensor',
version='0.0.1',
author='Kiran',
author_email='kumarsv.kiran@gmail.com',
packages=find_packages(),
install_requires = get_requirements()
)