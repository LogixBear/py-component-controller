from setuptools import setup, find_packages


setup(
    name='pcc',
    description='PCC is an opinionated framework for structuring selenium tests. This project depends on pyselenium-js.',
    version='0.0.1',
    url='https://github.com/neetjn/py-component-controller',
    author='John Nolette',
    author_email='john@neetgroup.net',
    license='Apache2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7'
    ],
    install_requires=[
        'selenium',
        'pyseleniumjs',
    ],
    packages=['pcc']
)
