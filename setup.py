from setuptools import setup


setup(
    name='intake_mockup',
    pymodules='intake_mockup',
    entrypoints={
        'intake.drivers':
            ['mockup = intake_mockup.MockupDataSource']}
    )
