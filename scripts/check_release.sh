#python setup.py register
python setup.py sdist bdist_wheel
twine check dist/* --verbose
