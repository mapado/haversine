from distutils.core import setup, Extension

setup(
    name='haversine',
    version='0.4.2',
    description='Calculate the distance bewteen 2 points on Earth.',
    long_description=open('README.txt').read(),
    author='Balthazar Rouberol',
    author_email=['balthazar@mapado.com'],
    maintainer='Julien Deniau',
    maintainer_email=['julien.deniau@mapado.com'],
    url='https://github.com/mapado/haversine',
    packages=['haversine'],
    license=['MIT'],
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
