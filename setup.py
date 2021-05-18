from setuptools import setup

setup(
    name='haversine',
    version='2.3.1',
    description='Calculate the distance between 2 points on Earth.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=['enum34;python_version<"3.4"'],

    author='Balthazar Rouberol',
    author_email='balthazar@mapado.com',
    maintainer='Julien Deniau',
    maintainer_email='julien.deniau@mapado.com',
    url='https://github.com/mapado/haversine',
    packages=['haversine'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
)
