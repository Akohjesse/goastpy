from setuptools import setup, find_packages

setup(
    name="goastpy",
    version="0.1.10",
    include_package_data=True,
    packages=find_packages(),
    package_dir={"": "."},
    package_data={"goastpy": ["*.h", "*.so"]},
    install_requires=[],
    description='Python Wrapper for Go AST Parser',
    author='Itay Gersten',
    author_email='Itay.Gersten@gmail.com',
    url='https://github.com/itayg25/goastpy',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=['GO', 'GOLANG', 'PYTHON', 'AST',
              'GOPY', 'PYGO', 'PARSER', 'ASTPARSER', 'goastpy', 'astpy','pyast','goast','gopy', 'golangast','abstract syntax tree'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Golang",
    ],
    python_requires=">=3.6",
)
