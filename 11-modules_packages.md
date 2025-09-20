# Python Packages & Modules

### GREAT resource: https://www.youtube.com/watch?app=desktop&v=2DRPBUiqmV4

---

#### Modules

A **module** is any `.py` file that defines variables, functions, and classes. Importing executes the file once, creates a **module object**, and caches it in `sys.modules`.

```python
BASE_BOUNTY = 300_000_000

def total_bounty(base: int, crew_bonus: int) -> int:
    return base + crew_bonus

class Pirate:
    def __init__(self, name: str, role: str, bounty: int):
        self.name = name
        self.role = role
        self.bounty = bounty
```

Use:

```python
import bounty_utils as bu

luffy = bu.Pirate("Monkey D. Luffy", "Captain", 3_000_000_000)
print(bu.total_bounty(bu.BASE_BOUNTY, 50_000_000))
```

Import styles & namespaces:

```python
import bounty_utils                     # binds module; use bounty_utils.Pirate
from bounty_utils import Pirate         # binds specific names
from bounty_utils import total_bounty as tb  # local alias
# Avoid: from bounty_utils import *  (namespace pollution)
```

Script vs module (`__name__ == "__main__"`)

```python
# file: sail.py
def main():
    print("Setting sail for the Grand Line")

if __name__ == "__main__":
    main()  # runs only when executed directly: python sail.py
```

Where Python looks (`sys.path`)

```python
import sys
print(sys.path)  # search paths: stdlib, cwd/package roots, site-packages, etc.
```

Import cache & `.pyc`
A module executes **once** per interpreter and is cached in `sys.modules`. Bytecode is stored in `__pycache__/module.cpython-XY.pyc`.

```python
import importlib, bounty_utils
importlib.reload(bounty_utils)  # force re-exec after edits during development
```

---

#### Package

A **package** is a directory hierarchy that Python can import. Classic packages include an `__init__.py` (may be empty).

```
strawhat/                    # top-level package
├── __init__.py
├── crew.py                  # strawhat.crew
├── bounty.py                # strawhat.bounty
└── abilities/
    ├── __init__.py          # subpackage: strawhat.abilities
    └── devil_fruits.py      # strawhat.abilities.devil_fruits
```

Example:

```python
# strawhat/__init__.py
__all__ = ["crew", "bounty", "abilities"]   # controls `from strawhat import *`
VERSION = "1.0"
# Optional public API surface:
from .bounty import calculate_bounty



# strawhat/crew.py
CREW = [
    {"name": "Luffy", "role": "Captain"},
    {"name": "Zoro",  "role": "Swordsman"},
    {"name": "Nami",  "role": "Navigator"},
]



# strawhat/bounty.py
def calculate_bounty(name: str) -> int:
    table = {
        "Luffy": 3_000_000_000,
        "Zoro": 1_111_000_000,
        "Nami":   366_000_000,
    }
    return table.get(name, 0)



# strawhat/abilities/devil_fruits.py
DEVIL_FRUITS = {"Luffy": "Gomu Gomu no Mi", "Robin": "Hana Hana no Mi"}
def has_devil_fruit(name: str) -> bool:
    return name in DEVIL_FRUITS
```

Using the package:

```python
import strawhat
from strawhat import bounty
from strawhat.abilities.devil_fruits import has_devil_fruit

print(strawhat.VERSION)
print(bounty.calculate_bounty("Zoro"))
print(has_devil_fruit("Luffy"))
```

###### Absolute vs. relative imports (inside packages)

Absolute (recommended):

```python
# strawhat/abilities/devil_fruits.py
from strawhat.bounty import calculate_bounty
```

Relative (only inside packages):

```python
# strawhat/abilities/devil_fruits.py
from ..bounty import calculate_bounty
```

###### Avoid circular imports

Problem `captain.py` imports `swordsman.py` at top level, and `swordsman.py` imports `captain.py` at top level.
Fix it:

```python
# captain.py
def orders():
    from .swordsman import style
    return f"Captain orders: {style()}"
```

Extract shared code to a third module (e.g., `strawhat/shared.py`) and import that from both.

###### `__init__.py` as API façade

Expose a clean top-level API:

```python
# strawhat/__init__.py
from .bounty import calculate_bounty
from .crew import CREW
__all__ = ["calculate_bounty", "CREW"]
```

```python
from strawhat import calculate_bounty, CREW
```
