import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CONTRIBUTORS = open(os.path.join(here, 'CONTRIBUTORS.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = ('voteit.core',
            'pyramid',
            'colander',
            'deform',
            'fanstatic',)

setup(name='voteit.notes',
      version='0.1dev',
      description='Personal notes on proposals for VoteIT',
      long_description=README + '\n\n' +  CONTRIBUTORS + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='VoteIT development team and contributors',
      author_email='info@voteit.se',
      url='http://www.voteit.se',
      keywords='web pyramid pylons voteit',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="voteit.notes",
      entry_points = {
          'fanstatic.libraries': {
              'voteit_notes_lib': 'voteit.notes.fanstaticlib:voteit_notes_lib'
          }
      },
  )
