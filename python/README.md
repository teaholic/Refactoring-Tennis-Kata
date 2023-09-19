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

## 1. Smelling the Code

These implementations in `tennis1.py` have a bad smell:
- `tempScore` (line 19) is a *temporary field* (object-orientation abuser)
- lines 20-48 have nested *switch statements* (object-orientation abuser)
- `score` method is quite a *long method* (bloater). I believe solving the first two smells will greatly improve this bloater already.

## 2. Finding Possible Treatments

### Switch statements

From [Refactoring Guru](https://refactoring.guru/smells/switch-statements):

> - To isolate switch and put it in the right class, you may need **Extract Method** and then **Move Method**.
>- If a switch is based on type code, such as when the program’s runtime mode is switched, use **Replace Type Code with Subclasses** or **Replace Type Code with State/Strategy**.
> - After specifying the inheritance structure, use **Replace Conditional with Polymorphism**.
> - If there aren’t too many conditions in the operator and they all call same method with different parameters, polymorphism will be superfluous. If this case, you can break that method into multiple smaller methods with **Replace Parameter with Explicit Methods** and change the switch accordingly.
> - If one of the conditional options is null, use **Introduce Null Object**.

### Temporary Fields

From [Refactoring Guru](https://refactoring.guru/smells/switch-statements):

- Temporary fields and all code operating on them can be put in a separate class via **Extract Class**. In other words, you’re creating a method object, achieving the same result as if you would perform **Replace Method with Method Object**.
- Introduce **Null Object** and integrate it in place of the conditional code which was used to check the temporary field values for existence.

## My refactoring process

### Step #1 - I used Extract class to treat a temporary field tempScore. 

After this step, I noticed that tempScore is repeated twice now. Also, p1points and p2points are temporary values too. Finally, the result type is anemic - hidden in the switch statements of the score method (primitive obsession).