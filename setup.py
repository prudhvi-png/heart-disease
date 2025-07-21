from setuptools import setup,find_packages


DOTENV = "-e ."
def install_requirements(file_path):
    requiremets = []
    with open(file_path,'r') as file:
        requiremets = file.readlines()
        requiremets = [req.replace("\n", "") for req in requiremets]
    if DOTENV in requiremets:
        requiremets.remove(DOTENV)
    
    return requiremets



setup(

    name="Ml-Project",
    version="0.0.1",
    author="prudhvi",
    author_email='prudhviredrouth143@gmail.com',
    packages=find_packages(),
    install_requires = install_requirements("requirements.txt")
)


