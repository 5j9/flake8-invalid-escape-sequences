cd ..
python setup.py sdist
python setup.py bdist_wheel --universal
twine upload dist/*
rm -r dist build flake8_invalid_escape_sequences.egg-info
read -n1 -r -p "Press any key to continue..." key