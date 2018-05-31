from setuptools import setup, find_packages


setup(
    name='swiftspace',
    version="0.2.0",
    packages=find_packages(),
    install_requires=['numpy', 'scikit-optimize', 'scikit-learn', 'mpi4py'],

    # metadata for upload to PyPI
    author="Todd Young",
    author_email="youngmt1@ornl.gov",
    description="Pairing Swift-t with Distributed Bayesian model-based optimization with Scikit-Optimize",
    license="MIT",
    keywords="parallel optimization smbo",
    url="https://github.com/yngtodd/hyperspace",
)
