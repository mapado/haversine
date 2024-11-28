from setuptools import setup

setup(
    name='haversine',
    version='2.9.0',
    description='Calculate the distance between 2 points on Earth.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires='>=3.5',
    author='Balthazar Rouberol',
    maintainer='Julien Deniau',
    maintainer_email='julien.deniau@mapado.com',
    url='https://github.com/mapado/haversine',
    packages=['haversine'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: GIS'
    ],
)
