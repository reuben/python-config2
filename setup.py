
# =========================================
#       IMPORTS
# --------------------------------------

import os
import setuptools

# DISABLED/BUG: this line fails when `pip install config2` but works `pip install .`
# from config2 import __version__


# =========================================
#       MAIN
# --------------------------------------

name = 'config2'
version = '0.3.2'
description = 'Python application configuration - highly inspired by `node-config`.'
keywords = [
    'config',
    'configuration',
    'configurations',
    'settings',
    'env',
    'environment',
    'environments',
    'application',
    'node-config',
    'python-config',
]

packages = setuptools.find_packages(".")
requirements = [
    "rootpath >= 0.1.1",
    "attributedict @ git+https://github.com/reuben/python-attributedict.git@e4ffbdbcb3b24113ab344c56c0174c3056b8c2d9#egg=attributedict",
    "inspecta >= 0.1.3",
    "mybad @ git+https://github.com/reuben/python-mybad.git@b46ce8b44b5dabf5e0c560d2814b983c297b84e1#egg=mybad",
    "deepmerge >= 0.0.5",
    "pyyaml >= 5.1",
    "six >= 1.12.0",
]
with open("README.md") as fin:
    readme = ''.join(fin.readlines())

config = {
    'name': name,
    'version': version,
    'description': (description),
    'keywords': keywords,
    'author': 'Jonas Grimfelt',
    'author_email': 'grimen@gmail.com',
    'url': 'https://github.com/grimen/python-{name}'.format(name = name),
    'download_url': 'https://github.com/grimen/python-{name}'.format(name = name),
    'project_urls': {
        'repository': 'https://github.com/grimen/python-{name}'.format(name = name),
        'bugs': 'https://github.com/grimen/python-{name}/issues'.format(name = name),
    },
    'license': 'MIT',

    'long_description': readme,
    'long_description_content_type': 'text/markdown',

    'classifiers': [
        'Topic :: Software Development :: Libraries',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    'packages': packages,
    'package_dir': {
        name: name,
    },
    'package_data': {
        '': [
            'MIT-LICENSE',
            'README.md',
        ],
        name: [
            '*.*',
        ],
    },
    'include_package_data': True,
    'zip_safe': True,

    'install_requires': requirements,
    'setup_requires': [
        'setuptools_git >= 1.2',
    ],
}

setuptools.setup(**config)
