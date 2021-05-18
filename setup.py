from distutils.core import setup
setup(
  name = 'naverscrap',
  packages = ['naverscrap'],
  version = '1.0.0',      
  license='MIT',    
  description = 'A Naver News Scraping tool',
  author = 'Brendon Lim',  
  author_email = 'brendonlim96@hotmail.com',   
  url = 'https://github.com/brendonlch/naverscrap',   
  download_url = 'https://github.com/brendonlch/naverscrap/archive/refs/tags/1.0.0.tar.gz',
  
  keywords = ['naver', 'korea', 'news', 'article', 'newspaper', 'web scrapping'],
  install_requires=[
          'datetime',
          'beautifulsoup4',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)