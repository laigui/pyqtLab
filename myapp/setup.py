from setuptools import setup

requirements = [
    # TODO: put your package requirements here
]

setup(
    name='myapp',
    version='0.0.1',
    description="SMCB hardware tester",
    author="Mike Qin",
    author_email='laigui@gmail.com',
    url='https://github.com/laigui/smcbtester',
    packages=['myapp', 'myapp.images',
              'myapp.tests'],
    package_data={'myapp.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'SmcbTesterApp=myapp.myapp:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='myapp',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
