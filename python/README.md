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

### Step #2 - I used more of Extract class to reduce the number of lines in the score method (long method). 

I notice that the method score of the new three classes is executed if a condition is met. This is a good opportunity to refactor with a Chain of Responsibility pattern in the next iteration.

### Step #3 - I started implementing Chain of Responsibility pattern

I created an abstract class ScoringService with can_handle and score methods. I changed the specific implementations so that the method signature stays the same (Liskov principle).

### Step #4 - I implemented Chain of Responsibility pattern

In the TennisGame class, I added a service_list parameter with a list of ScoringServices, where the last service is a default service to use a fallback if all other services can't handle the player scores. I refactored the score method to iterate on each service in the list, first checking if that service can_handle the player scores, then returning a new score. Cleanups include removing unnecessary return statements and result string.

I notice that the score type, a string, is central in the tennis game narrative, but still somehow hidden in the implementation (primitive obsession).