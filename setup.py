import setuptools

with open("README.md") as f:
    long_description = f.read().rstrip()

with open("projpicker_gui/VERSION") as f:
    version = f.read().rstrip()

setuptools.setup(
    name="projpicker_gui",
    version=version,
    license="GPLv3+",
    author="Owen Smith and Huidae Cho",
    author_email="grass4u@gmail.com",
    description="ProjPicker GUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HuidaeCho/projpicker-gui",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    package_data={"projpicker_gui": ["VERSION", "map.html"]},
    entry_points={"console_scripts": ["projpicker-gui=projpicker_gui:main"]},
)
