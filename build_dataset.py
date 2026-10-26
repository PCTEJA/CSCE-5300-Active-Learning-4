import hashlib
import re
from io import StringIO
from pathlib import Path
from urllib.request import urlopen

import pandas as pd

SOURCE_URL = 'https://openml.org/data/v1/download/16826755/Titanic.arff'
with urlopen(SOURCE_URL, timeout=60) as response:
    raw = response.read()
assert hashlib.md5(raw).hexdigest() == '60ac7205eee0ba5045c90b3bba95b1c4'
text = raw.decode('utf-8')
header, records = text.split('@data', 1)
columns = re.findall(r"@attribute\s+'([^']+)'", header)
source = pd.read_csv(StringIO(records.strip()), names=columns, na_values='?', escapechar='\\')
assert source.shape == (1309, 14)

dataset = source[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']].copy()
dataset['class'] = dataset['pclass'].map({1: 'First', 2: 'Second', 3: 'Third'})
dataset['who'] = dataset['sex'].map({'male': 'man', 'female': 'woman'})
dataset.loc[dataset['age'] < 16, 'who'] = 'child'
dataset['adult_male'] = dataset['who'].eq('man')
dataset['deck'] = source['cabin'].str[0]
dataset['embark_town'] = dataset['embarked'].map({'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'})
dataset['alive'] = dataset['survived'].map({0: 'no', 1: 'yes'})
dataset['alone'] = dataset['sibsp'].add(dataset['parch']).eq(0)

expected_columns = ['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked',
                    'class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone']
assert dataset.columns.tolist() == expected_columns
assert dataset.shape == (1309, 15)
assert dataset['survived'].value_counts().to_dict() == {0: 809, 1: 500}
dataset.to_csv(Path(__file__).with_name('titanic.csv'), index=False)
print('Saved 1,309 passenger records with exactly 15 Seaborn-style columns.')
print('Complete age, fare and survived rows:', len(dataset[['age', 'fare', 'survived']].dropna()))
