# Online Poker Deck Shuffle Validation

using Secret Sharing Scheme

## Abstract
Permainan poker online sering menimbulkan kecurigaan, apakah pembagian kartu dilakukan dengan adil atau tidak. Dengan menggunakan secret sharing scheme, verifikasi pembagian kartu dapat dilaksanakan. Karena setiap pemain tidak ingin membagikan isi kartu tangan mereka, maka kartu tangan setiap pemain dapat dianggap sebagai share. Kemudian di akhir permainan, share seluruh pemain dapat digabungkan untuk memverifikasi pembangkit bilangan acak semu yang digunakan untuk melakukan pembagian kartu.

## Requirements
- Python 3.6+
- PrimePy 1.3+

## Installing Requirements
### Linux
```bash
python -m virtualenv -p python3 venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### Windows
```bash
python -m virtualenv -p python venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Running Program
### Linux
```bash
source venv/bin/activate
python main.py
```

### Windows
```bash
venv\Scripts\activate
python main.py
```

## Running tests
```bash
source venv/bin/activate
python tests.py
```

### Windows
```bash
venv\Scripts\activate
python tests.py
```

## Publication
-

## Author
[Jonathan Yudi Gunawan](https://github.com/JonathanGun/)
