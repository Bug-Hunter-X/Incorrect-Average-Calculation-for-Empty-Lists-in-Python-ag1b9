# Python Average Calculation Bug

This repository demonstrates a common bug in Python functions that calculate the average of a list of numbers: the incorrect handling of empty lists.  The `calculate_average` function in `bug.py` returns 0 when the input list is empty.  This behavior may not always be desired; a more robust approach might raise an exception or return a special value indicating an empty input.

The solution, provided in `bugSolution.py`, addresses this issue by explicitly checking for an empty list and raising a ValueError if one is encountered.