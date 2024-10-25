from setuptools import setup, find_packages

setup(
    name='car_simulation',
    version='0.1.0',
    description='A simulation application for automatic driving cars.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Srinivas Reddy',
    author_email='bsreddyb@hotmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    package_data={
        'car_simulation': ['localize/*.yaml']
    },
    include_package_data=True,
    install_requires=[
        'PyYAML',
    ],
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'run-simulation=car_simulation.main:main',
        ],
    },
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
