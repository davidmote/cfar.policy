from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(
    name='cfar.policy',
    version=version,
    description="The collection of products required for the CFAR website",
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
    keywords='',
    author='BEAST Core Development Team',
    author_email='beast@ucsd.edu',
    url='https://github.com/beastcore/cfar.policy',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'':'src'},
    namespace_packages=['cfar'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
        'PIL',
        'collective.uploadify',
        'collective.indexing',
        'five.grok',
        'jyu.z3cform.datepicker',
        'plone.app.ldap',
        'Products.PloneFormGen',

        'avrc.cfar.coreservice',
        'avrc.cfar.grant',
        'avrc.cfar.masterbook',
        'avrc.cfar.theme',
        ],
    extras_require=dict(
        test=['plone.app.testing'],
        ),
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
