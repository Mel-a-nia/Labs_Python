# python-bs

## Лабораторная работa 2

### Задание 1.1

<lab 2/image/foto_1.1.png/>

```
def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, (tuple, list)) or len(rec) != 3:
        raise ValueError("rec debe contener (fio, group, gpa)")
    fio, group, gpa = rec
    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("fio y group deben ser str")
    if not isinstance(gpa, (int, float)):
        raise TypeError("gpa debe ser numérico")
    fio = " ".join(fio.split())
    group = group.strip()
    if not fio or not group:
        raise ValueError("fio y group no pueden estar vacíos")
    parts = fio.split()
    if len(parts) < 2:
        raise ValueError("fio debe contener фамилию и имя")
    surname = parts[0].capitalize()
    initials = "".join(n[0].upper() + "." for n in parts[1:3])
    gpa_str = f"{float(gpa):.2f}"
    return f"{surname} {initials}, гр. {group}, GPA {gpa_str}"
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("сидорова анна сергеевна", "ABB-01", 3.999)))

```

<![alt text](foto_1.1_resultado.png) />

### Задание1.2

<

```
def min_max(nums: list [float | int])-> tuple [float | int, float | int]:
    if not nums: 
        raise ValueError ("пустой список")
    return(min(nums), max(nums))
def unique_sorted (nums:list [float | int])-> list [float | int]:
    return sorted(set(nums))
def flatten(mat:list[list | tuple])-> list:
    result=[]
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("строка не является ни списком, ни кортежем")
        result.extend(row)
    return result 
print(min_max([]))

```

< ![alt text](foto_1.2_resultado.png)/>

### Задание 2b.1

<![alt text](foto_2B.1.png) />

```
from typing import List, Union
Number = Union[int, float]
def _check_rectangular(mat: List[List[Number]]) -> None:
    if not mat:
        return
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError("рваная матрица")
def transpose(mat: List[List[Number]]) -> List[List[Number]]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
def row_sums(mat: List[List[Number]]) -> List[float]:
    _check_rectangular(mat)
    return [float(sum(row)) for row in mat]
def col_sums(mat: List[List[Number]]) -> List[float]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [float(sum(mat[i][j] for i in range(len(mat)))) for j in range(len(mat[0]))]
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))

```

<![alt text](foto_2B.1_resultado.png) />
### Задание 2b.2

<![alt text](foto_2B.2.png) />


```
from typing import List, Union
Number = Union[int, float]
def _check_rectangular(mat: List[List[Number]]) -> None:
    if not mat:
        return
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError("рваная матрица")
def transpose(mat: List[List[Number]]) -> List[List[Number]]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
def row_sums(mat: List[List[Number]]) -> List[float]:
    _check_rectangular(mat)
    return [float(sum(row)) for row in mat]
def col_sums(mat: List[List[Number]]) -> List[float]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [float(sum(mat[i][j] for i in range(len(mat)))) for j in range(len(mat[0]))]
print(transpose([[1, 2], [3]]))

```

<![alt text](foto_2B.1_resultado.png) />

### Задание 2b.3

<![alt text](foto_2B.3.png) />


```
from typing import List, Union
Number = Union[int, float]
def _check_rectangular(mat: List[List[Number]]) -> None:
    if not mat:
        return
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError("рваная матрица")
def transpose(mat: List[List[Number]]) -> List[List[Number]]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
def row_sums(mat: List[List[Number]]) -> List[float]:
    _check_rectangular(mat)
    return [float(sum(row)) for row in mat]
def col_sums(mat: List[List[Number]]) -> List[float]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [float(sum(mat[i][j] for i in range(len(mat)))) for j in range(len(mat[0]))]
print(row_sums([[1, 2], [3]]))

```

<![alt text](foto_2B.3_resultado.png) />
### Задание 2b.4

<![alt text](foto_2B.4.png) />


```
from typing import List, Union
Number = Union[int, float]
def _check_rectangular(mat: List[List[Number]]) -> None:
    if not mat:
        return
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError("рваная матрица")
def transpose(mat: List[List[Number]]) -> List[List[Number]]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
def row_sums(mat: List[List[Number]]) -> List[float]:
    _check_rectangular(mat)
    return [float(sum(row)) for row in mat]
def col_sums(mat: List[List[Number]]) -> List[float]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [float(sum(mat[i][j] for i in range(len(mat)))) for j in range(len(mat[0]))]
print(col_sums([[1, 2], [3]]))

```

<![alt text](foto_2B.4_resultado.png) />
### Задание c

<![alt text](foto_c.png) />


```
def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, (tuple, list)) or len(rec) != 3:
        raise ValueError("rec debe contener (fio, group, gpa)")
    fio, group, gpa = rec
    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("fio y group deben ser str")
    if not isinstance(gpa, (int, float)):
        raise TypeError("gpa debe ser numérico")
    fio = " ".join(fio.split())
    group = group.strip()
    if not fio or not group:
        raise ValueError("fio y group no pueden estar vacíos")
    parts = fio.split()
    if len(parts) < 2:
        raise ValueError("fio debe contener фамилию и имя")
    surname = parts[0].capitalize()
    initials = "".join(n[0].upper() + "." for n in parts[1:3])
    gpa_str = f"{float(gpa):.2f}"
    return f"{surname} {initials}, гр. {group}, GPA {gpa_str}"
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("сидорова анна сергеевна", "ABB-01", 3.999)))
```

<![alt text](foto_c_resultado.png) />

