import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='altair_dashboard',
    version='0.1',
    description='Create dashboards with altair on the fly',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sauercrowd/altair-dashboard',
    author='sauercrowd',
    packages=setuptools.find_packages()
)