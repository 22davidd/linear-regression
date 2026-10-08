# linear-regression

un model care invata singur sa transforme grade celsius in fahrenheit. nu i-am dat formula, doar 6 exemple, iar el a gasit-o.

![python](https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white)
![libraries](https://img.shields.io/badge/librarii-zero-2ea44f)
![epochs](https://img.shields.io/badge/epochs-1.500.000-8957e5)

## ideea

o dreapta e definita de doua numere:

```
fahrenheit = w * celsius + b
```

- `w` = cat de repede creste dreapta (panta)
- `b` = de unde porneste (fahrenheit cand celsius = 0)

modelul porneste cu `w = 0` si `b = 0`, adica nu stie nimic, si le ajusteaza putin cate putin pana prezice bine toate exemplele.

formula reala e `F = C * 9/5 + 32`, deci tinta lui e `w = 1.8` si `b = 32`.

## datele

| celsius | fahrenheit |
|--------:|-----------:|
| 7  | 44.6  |
| 8  | 46.4  |
| 13 | 55.4  |
| 19 | 66.2  |
| 24 | 75.2  |
| 43 | 109.4 |

## cum invata

dupa **fiecare** exemplu (nu dupa tot setul) modelul isi corecteaza `w` si `b`, si asta se repeta de 1.500.000 de ori peste cele 6 exemple:

```mermaid
flowchart LR
    A["prezice: w*x + b"] --> B["eroare: real - prezis"]
    B --> C["ajusteaza w si b"]
    C --> A
```

in cod:

```python
pred = w*x + b
err = y - pred
w = w - lr * (-2*err*x)
b = b - lr * (-2*err)
```

daca predictia e prea mica, `err` e pozitiv si `w` si `b` cresc (la datele de aici, unde toate valorile sunt pozitive). daca e prea mare, scad. `lr = 0.0003` decide cat de mari sunt pasii.

## rezultat

```text
weight: 1.8000000000000915
bias: 31.999999999996422
46 degrees celsius is equal to 114.80F for example
```
## limitari

- 6 exemple pare putin, dar relatia e perfect liniara si fara zgomot, deci nu apare overfitting
- 1.500.000 de epochs e probabil mai mult decat ar trebui

## rulare
```bash
python3 linear_regression.py
```
made by 22davidd all rights reserved 
