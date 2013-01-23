from setuptools import setup


setup(
        name='haversine',
            version='0.1',
            description='Calculate the distance bewteen 2 points on Earth.',
            long_description=open('README.txt').read(),
            author='Balthazar Rouberol',
            author_email=['balthazar@mapado.com'],
            url='https://github.com/mapado/haversine',
            packages=['haversine'],
            license=['GPLv3'],
            classifiers=[
                'Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2.6',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.1',
                'Programming Language :: Python :: 3.2',
                'Programming Language :: Python :: 3.3',
                'Topic :: Scientific/Engineering :: Mathematics'
            ]
)
