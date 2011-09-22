from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(name='cfar.policy',
      version=version,
      description="The collection of products required for the CFAR website",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cfar'],
      package_dir={'':'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'avrc.cfar.theme',
          'collective.uploadify',
          'collective.indexing',
          'jyu.z3cform.datepicker',     
          'beast.cache',
          'avrc.cfar.coreservice',
          'avrc.cfar.masterbook',
          'avrc.cfar.grant',
          'webcouturier.dropdownmenu',
          'plone.app.ldap',
          'Products.PloneFormGen'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
