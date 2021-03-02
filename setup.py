import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='sust_phy_abcd',  
     version='0.1',
     scripts=['sust_phy_abcd'] ,
     author="Tahmidul Azom Sany",
     author_email="tasanyphy01773@gmail.com",
     description="A simple package for ray transfer matrix",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/tasanyphy01773/sust_phy_abcd",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
