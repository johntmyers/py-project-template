from distutils.core import setup

setup(
    name='MyNewProject',
    version='0.1.0',
    author='YourName',
    # any new packages you add in your project package dir should go here as proj.whatever
    packages=[
        'proj'
    ],
    # scripts that get installed to a "bin" directory
    scripts=[
    ],
    # proj deps
    install_requires=[
        'redis'
    ]
)
