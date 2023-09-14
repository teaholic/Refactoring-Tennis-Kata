# Tennis Kata - Refactoring

## Contributor guide

On Windows, please run the following from Git Bash terminal:

### Setup environment
```bash
python -m venv venv
source ./venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Run tests
```bash
python -m pytest
```

## Code Smells

These implementations in `tennis1.py` have a bad smell:
- `tempScore` (line 19) is a *temporary field* (object-orientation abuser)
- lines 20-48 have nested *switch statements* (object-orientation abuser)
- `score` method is quite a *long method* (bloater)