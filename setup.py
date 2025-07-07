from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version= '0.0.1',
    author='harsh kumar',
    author_email='harshkumarsingh4343@gmail.com',
    install_requires=["openai","langchain","streamlit", "python-dotenv","pyPDF2"],
    packages=find_packages(),
)