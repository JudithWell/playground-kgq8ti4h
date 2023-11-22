# Lesen von Listeneinträgen

Um auf einzelne Elemente aus der Liste zuzugreifen, können wir eine laufende Nummer nutzen. Diese Nummer nennen wir **Index** eines Elements. (Plural: mehrere Indizes)

Die Elemente sind in der Reihenfolge, in der sie in den eckigen Klammern stehen **von 0 an** durchnummeriert. Der Zugriff auf einen Eintrag ist mit dem Index in eckigen Klammern hinter dem Listennamen möglich.

```python
einkaufsliste = ["Mehl", "Zucker", "Butter", "Eier"]
mengen = [400, 250, 250, 4]

print(einkaufsliste[0])     # gibt "Mehl" aus
print(mengen[3])            # gibt "4" aus
print(einkaufsliste[4])     # IndexError: list index out of range
```

?[Warum tritt in der letzten Zeile ein Fehler auf?]
- [ ] 4 ist kein Eintrag von `einkaufsliste`, der Aufruf `mengen[4]` hätte funktioniert.
- [ ] Bei den Eiern handelt es sich um Eier aus Bodenhaltung statt um Eier aus Freiland- (range-) Haltung.
- [x] Die Indizes von Listen beginnen bei 0, deshalb hat das vierte Element den Index 3. Ein Element mit Index 4 existiert nicht.

# Ändern bzw. Ersetzen von Einträgen

Annabel ist wieder eingefallen, dass ihre Freundin keine Milchprodukte verträgt und möchte deshalb die Butter auf ihrer Liste durch Margarine ersetzen.

```python runnable
einkaufsliste = ["Mehl", "Zucker", "Butter", "Eier"]
mengen = [400, 250, 250, 4]

einkaufsliste[2] = "Margarine"
```

Von der Margarine braucht Annabel jetzt aber nur 200 g, hilf ihr dabei, den Eintrag in der Liste `mengen` entsprechend zu verändern!

@[Reduziere die Menge der Margarine auf 200 g!]({"stubs": ["ersetzen.py"], "command": "python3 test_ersetzen.py"})