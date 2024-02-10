# from setuptools import find_packages, setup
from setuptools

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()


def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



__version__ = "0.0.1"

REPO_NAME = "DeepLearningProject1"
AUTHOR_USER_NAME = "FUZZZZI"
SRC_REPO = "Xray"                  #ProjectName
AUTHOR_EMAIL = "lalwnisaurabh9@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    # long_description=long_description,
    # long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    # package_dir={"": "src"},
    # install_requires = [],    
    # #or
    install_requires = get_requirements(),
    packages=setuptools.find_packages()
)