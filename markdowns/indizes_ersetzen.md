# Lesen und Ersetzen

Um auf einzelne Elemente aus der Liste zuzugreifen, können wir eine laufende Nummer nutzen. Diese Nummer nennen wir **Index** eines Elements.

Die Elemente sind in der Reihenfolge, in der sie in den eckigen Klammern stehen **von 0 an** durchnummeriert. Der Zugriff auf einen Eintrag ist mit dem Index in eckigen Klammern hinter dem Listennamen möglich.

```python runnable
einkaufsliste = ["Mehl", "Zucker", "Butter", "Eier"]
mengen = [400, 250, 250, 4]

print(einkaufsliste[0])     # gibt "Mehl" aus
print(mengen[3])            # gibt "4" aus
print(einkaufsliste[4])     # IndexError: list index out of range
```