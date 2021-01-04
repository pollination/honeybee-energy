#!/usr/bin/env python
import setuptools
# add these line to integrate the queenbee packaging process
# into Python packaging
from queenbee_dsl.package import PackageQBInstall, PackageQBDevelop
name = 'pollination-honeybee-energy'
PackageQBInstall.__queenbee_name__ = name
PackageQBDevelop.__queenbee_name__ = name

# normal setuptool inputs
setuptools.setup(
    cmdclass={
        'develop': PackageQBDevelop,
        'install': PackageQBInstall
    },
    name=name,
    author='chris',
    author_email='chris@ladybug.tools',
    setup_requires=['setuptools_scm'],
    packages=setuptools.find_packages('pollination_honeybee_energy'),
    keywords=['honeybee', 'energy', 'ladybug-tools'],
    license='PolyForm Shield License 1.0.0'
)
