import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
  name = 'TOPSIS-Ritik-101983033',
  version = '0.3.0',
  author = 'Ritik Aggarwal',                  
  author_email = 'raggarwal1_be18@thapar.edu', 
  description = 'This package can be used to calculate the topsis score of multiple component data and rank them accordingly',   
  long_description=long_description,
  long_description_content_type="text/markdown",
  packages=setuptools.find_packages(),
  license='MIT', 
  keywords = ['TOPSIS'],  
  install_requires=[           
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ]
)
