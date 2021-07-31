Create new env

```bash
conda create -n wineq python=3.7 -y
```

Activate env
```bash
conda activate wineq
```

Created a requirements.txt file
install the requirements 
```bash
pip install -r requirements.txt
```

Push data to github repository

```bash
git init
dvc init
dvc add data_given/winequality.csv
```

```bash
git add .
git commit -m "First commit"
```

```bash
git remote add origin https://github.com/veeruamma/MLOps-dvc-Demo.git
git branch -M main
git push -u origin main
```
tox command
```bash
tox
```
tox rebuilding
```bash
tox -r
```
pytest command
```bash
pytest -v
```

setup commands
```bash
pip install -e .

```
build your own package commands - builds the tar file
```bash
python setup.py sdist bdist wheel
```

```bash

```