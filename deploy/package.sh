#!/bin/sh
set -e
rm -rf projpicker_gui* build dist README.md LICENSE setup.py deploy.sh
test "$1" = "clean" && exit

cp -a ../projpicker_gui ../README.md .
cp -a ../COPYING LICENSE

cat<<EOT > setup.py
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
EOT

cat<<EOT > deploy.sh
#!/bin/sh
set -e
pip3 install --user --upgrade twine
twine upload dist/*
EOT
chmod a+x deploy.sh

pip3 install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
