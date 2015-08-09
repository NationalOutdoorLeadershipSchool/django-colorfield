from distutils.core import setup

version = '0.2.0'

setup(
    name="django-colorfield",
    version=version,
    keywords=["django", "color"],
    author='Sean Marlow',
    author_email='kodemaven@gmail.com',
    license='MIT',
    long_description="A small app providing a colorpicker field for django",
    description="A small app providing a colorpicker field for django",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    packages=['colorfield'],
    package_data={
        'colorfield': ['static/colorfield/colorpicker/*', 'templates/colorfield/*'],
    },
    install_requires=['django>=1.7'],
    requires=['django (>=1.7)'],
)

