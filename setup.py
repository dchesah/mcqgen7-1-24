from setuptools import find_packages, setup

setup(
    name='mcqgenarator',
    version='0.0.1',
    author='sunny savita',
    author_email='chesah94@gmail.com',
    install_requres=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)