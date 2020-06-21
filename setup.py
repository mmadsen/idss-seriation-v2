import os
from setuptools import setup


# get __version__ from _version.py
version: dict = {}
ver_file = os.path.join("idss_seriation", "_version.py")
with open(ver_file) as f:
    exec(f.read(), version)


setup(
    name="idss_seriation_v2",
    maintainer="Mark Madsen and Carl Lipo",
    maintainer_email="mark@madsenlab.org",
    description="Library and executables for performing Iterative Deterministic seriation solutions (Lipo et al. 2015, PlosOne)",
    packages=["idss_seriation"],
    version=version["__version__"],
)
