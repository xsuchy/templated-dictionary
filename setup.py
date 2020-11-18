import setuptools

setuptools.setup(
    name="templated-dictionary",
    version="1.0",
    author="Miroslav Suchý",
    author_email="msuchy@redhat.com",
    description="Dictionary with Jinja2 expansion",
    long_description="""Dictionary where __getitem__() is run through Jinja2 template.""",
    long_description_content_type="text/markdown",
    url="https://github.com/xsuchy/templated-dictionary",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    license='GPLv2+',
    packages=['templated_dictionary'],
    include_package_data=True,
    zip_safe=False,
    install_requires = [
        'jinja2',
    ]
)
