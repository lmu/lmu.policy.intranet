from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='lmu.policy.intranet',
      version=version,
      description="Plone Ploicy for LMU ZUV-Intranet",
      long_description=open("README.rst").read() + "\n" +
      open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='Plone policy',
      author='Alexander Loechel',
      author_email='Alexander.Loechel@lmu.de',
      url='https://github.com/loechel/lmu.policy.intranet',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['lmu', 'lmu.policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'lmu.contenttypes.blog',
          'lmu.contenttypes.pinnwand',
          'lmu.theme.intranet',
          'pas.plugins.shibboleth_headers',
          'Pillow',
          'Plone',
          'plone.api',
          'Products.LongRequestLogger',
          'setuptools',
          'z3c.jbot',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'mock',
              'plone.app.testing',
              'plone.app.robotframework[debug]',
              'fake-factory',
          ],
          'develop': [
              'coverage',
              'flake8',
              'i18ndude',
              'Sphinx',
              'zptlint',
          ],
          'release': []
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
