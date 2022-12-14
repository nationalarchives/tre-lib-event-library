import setuptools
import os

build_version = os.environ['BUILD_VERSION']

setuptools.setup(
    name='tre-event-lib',
    version=build_version,
    description='TRE Events Library',
    packages=['tre_event_lib.tre_schemas', 'tre_event_lib'],
    package_data={'tre_event_lib.tre_schemas': ['*.json'],
                  'tre_event_lib': [
                      'about.json'
                  ]},
    python_requires='>=3.8'
)
