import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="deepsurvivalmachines",
    version="0.0.1",
    description="Provides an API to train the Deep Survival Machines and associated models for problems in survival analysis.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/autonlab/DeepSurvivalMachines",
    author="Chirag Nagpal",
    author_email="chiragn@cs.cmu.edu",
    maintainer=["Chirag Nagpal"],
    maintainer_email=["chiragn@cs.cmu.edu"],
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=["torch", "numpy", "pandas", "tqdm", "scikit-learn"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
