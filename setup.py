from distutils.core import setup
setup(
  name = 'pyroman',         # How you named your package folder (MyLib)
  packages = ['pyroman'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Convert Integer to Roman Number and Vice Versa.',   # Give a short description about your library
  author = 'Phani Pavan K',                   # Type in your name
  author_email = 'kphanipavan@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/kphanipavan',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4+',
  ],
)
