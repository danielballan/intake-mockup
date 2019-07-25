from setuptools import setup


setup(
    name='intake_mockup',
    pymodules='intake_mockup',
    entry_points={
        'intake.drivers':
            ['mockup = intake_mockup.MockupDataSource']}
    )
