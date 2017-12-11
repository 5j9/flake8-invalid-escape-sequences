cd ..
python setup.py sdist
python setup.py bdist_wheel --universal
twine upload dist/*
rm -r dist build
read -n1 -r -p "Press any key to continue..." key