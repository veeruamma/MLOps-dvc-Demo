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
dvc addd data_given/winequality.csv
```

```bash
git add .
git commit -m "First commit"
```
