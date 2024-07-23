from setuptools import setup, find_packages

setup(
    name='snake_game_py',
    version='0.1.0',
    description='A simple Google search tool using Google Custom Search API',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/google_search_tool',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
