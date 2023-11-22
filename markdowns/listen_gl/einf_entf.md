# Elemente in die Liste einfügen

Bevor sie einkaufen geht, stellt Annabel fest, dass ihr noch Backpulver fehlt. Sie möchte gerne eine Packung Backpulver auf ihrer Liste ergänzen.

Recherchiere im Internet wie die beiden eingebauten Funktionen `insert()` und `append()` Funktionen dabei helfen könnten, den Eintrag in die Liste einzufügen.
**Tipp:** Um gute Ergebnisse zu erhalten, suche nach "python list append" oder benutze ein KI-System wie ChatGPT. 

?[`insert()` und `append()` ...](multiple)
- [ ] ... unterscheiden sich in ihrem Ergebnis nicht und sind austauschbar.
- [x] ... fügen ein neues Element in die Liste ein.
- [x] bei `insert()` kann man den Index (also die Position) für den neuen Eintrag angeben.
- [ ] ... haben beide nur einen Funktionsparameter, nämlich den neuen Eintrag.
- [ ] Die Liste `liste` hat 3 Elemente. Die Aufrufe `liste.append("element")` und `liste.insert("element", 3)` haben dasselbe Ergebnis.
- [x] Die Liste `liste` hat 3 Elemente. Die Aufrufe `liste.append("element")` und `liste.insert(3, "element")` haben dasselbe Ergebnis.
- [ ] Der Aufruf `append("element")` fügt `"element"` am Anfang der Liste ein.
- [x] Der Aufruf `append("element")` fügt `"element"` am Ende der Liste ein.

Füge im Code-Beispiel das Backpulver nach dem Mehl in die Einkaufsliste ein und ergänze die Menge 1.

@[Ergänze das Backpulver!]({"stubs": ["ersetzen.py"], "command": "python3 test_ersetzen.py"})

# Elemente entfernen

Das Entfernen einzelner Elemente aus einer Liste kann auf zwei Arten erreicht werden:

- Mit `liste.pop(index)` wird das Element mit Index `index` aus der Liste `liste` entfernt.
- Der Aufruf `liste.remove(element)` entfernt den Eintrag `element` aus der Liste.

Die nachfolgende Funktion möchte Annabel verwenden, um während dem Einkaufen Dinge aus der Liste zu entfernen, die sie bereits in ihren Korb gelegt hat.

```python
def entfernen(produkt):
    einkaufsliste.remove(produkt)
```

Welche Probleme können hier entstehen?

?[Welche Probleme mit dieser Funktion entstehen?]
- [ ] Die Funktion fügt aus versehen neue Elemente in die Liste ein.
- [ ] Weil remove() einen Index und kein Element erwartet, sind Aufrufe wie `entfernen("Mehl")` ungültig!
- [x] Es wird nur die Liste `einkaufsliste` verändert, aber nicht die Mengenliste.
- [ ] Gar keine Probleme, Annabel kann die Funktion so verwenden und immer noch Mengen und Produkte einander zuordnen.
- [x] Wird nicht der letzte Eintrag entfernt, ist es nicht mehr möglich den Produkten die Mengen zuzuordnen.

Als Lösung programmiert Annabel stattdessen eine Methode, die abhängig vom Index die Einträge aus beiden Listen entfernt.

```python
def entfernenIndex(index):
    einkaufsliste.pop(index)
    mengen.pop(index)
```

Leider muss sie sich hierfür immer merken, an welcher Stelle in der Liste welches Produkt steht. **Recherchiere**, wie du dir den Index eines Listenelements in Python ausgeben lassen kannst. Ergänze anschließend die Methode `entfernen(produkt)`, die den Index von `produkt` ermittelt, `entfernenIndex(index)` aufruft und damit das Element `produkt` und die dazugehörige Menge entfernt.

::: Hilfestellung, falls Recherche nicht klappt:

Die Methode `index()` liefert den Index eines Listeneintrags.

Verwendung: `idx = liste.index("abc")` speichert den Index des Eintrags `"abc"` in der Variable `idx`.

:::

@[Entfernen von Produkten]({"stubs": ["entfernen.py"], "command": "python3 test_entfernen.py"})

