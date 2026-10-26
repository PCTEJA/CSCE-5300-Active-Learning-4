# CSCE: 5300 Active-Learning-4

This dataset contains 1,309 real Titanic passenger records in exactly the same 15-column layout as Seaborn's Titanic CSV. No passenger rows are generated or resampled.

[Download the CSV](https://raw.githubusercontent.com/PCTEJA/CSCE-5300-Active-Learning-4/main/titanic.csv)

## Sources

Passenger records: [OpenML Titanic, dataset 40945, version 1](https://www.openml.org/d/40945), credited to Frank E. Harrell Jr. and Thomas Cason, with Vanderbilt Biostatistics and Encyclopedia Titanica provenance.

Column layout: [Michael Waskom's Seaborn Titanic dataset](https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv). This file reformats the larger OpenML dataset; it is not the original 891-row Seaborn file.

## Columns

`survived`, `pclass`, `sex`, `age`, `sibsp`, `parch`, `fare`, `embarked`, `class`, `who`, `adult_male`, `deck`, `embark_town`, `alive`, `alone`.

The first eight fields come directly from the passenger records. Age is in years; fare is in British pounds. The survival target is 0 for did not survive and 1 for survived.

- `class`: First, Second, or Third from `pclass`.
- `who`: child for age below 16; otherwise man or woman from `sex`. Missing ages follow the sex-based category.
- `adult_male`: whether `who` is man.
- `deck`: the first letter of the recorded cabin; missing cabins stay missing.
- `embark_town`: Cherbourg, Queenstown, or Southampton from `embarked`.
- `alive`: yes or no from `survived`.
- `alone`: whether `sibsp + parch` equals zero.

Missing source values are preserved. Selecting age, fare, and survived and removing missing values retains 1,045 rows. The activity uses only age and fare as features and survived as the target.

Run `python build_dataset.py` with pandas installed to reproduce the CSV from the versioned OpenML source.
