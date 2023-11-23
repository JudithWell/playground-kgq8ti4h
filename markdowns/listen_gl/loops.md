# Listen und Wiederholungen - Ein perfektes Paar!

## Wiederholung(en)

Wir haben zuletzt **Wiederholungen mit fester Anzahl** und **Wiederholungen mit Bedingung** kennengelernt. Gerade die Wiederholung mit fester Anzahl (auch for-Loop oder for-Wiederholung genannt) ist super für die Arbeit mit Listen geeignet!

Noch einmal zur Wiederholung ... der for-Wiederholung:

```python runnable
for loop in range(5):
    print("blabla")
    print("Ich wiederhole mich!")
```

Der eingerückte Code unter dem "Kopf" der Wiederholung wird fünfmal ausgeführt.
Doch was genau passiert hier unter der Haube?

Betrachten wir zunächst die Funktion `range`. Der Aufruf erstellt im Hintergrund (so etwas wie) eine Liste. Das können wir sichtbar machen, indem wir Python mit der Funktion `list()` die Range als Liste interpretieren und ausgeben lassen. Probier's gleich aus:

```python runnable
print(list(range(5)))
```

`range(5)` generiert uns also ein Intervall von Zahlen zwischen 0 (eingeschlossen) und 5 (ausgeschlossen).

Ein weiterer Teil der Wiederholung, den wir noch nicht unter die Lupe genommen haben ist das `loop`. Hier könnte tatsächlich jeder beliebiger gültiger Variablenname stehen, es muss also nicht immer `loop` sein.

```python 
for loop in range(5):
    print("blabla")

for baum in range(5):
    print("blabla")

for satanarchaeoluegenialkohoellischerWunschpunsch in range(5):
    print("blabla")
```

Wir können diese Variable - auch Laufvariable, Schleifenvariable oder Index - jetzt auch im Rumpf der Wiederholung verwenden und z.B. ausgeben:

```python runnable
for index in range(5):
    print(index)
```

Dieses Programm gibt uns die Zahlen von 0 bis 4 aus. Also genau die Indizes, die wir bräuchten, um jedes Element in einer Liste mit fünf Elementen zu bearbeiten!

## Iterieren von Listen über den Index

Nun zurück zu Annabels Einkaufsliste: Hilf ihr die Methode `listeAusgeben()` zu schreiben, die die ganze Einkaufsliste einmal durchläuft (wir nennen das auch "iterieren") und jedes Element mit `gibAus()` ausgibt.

Nutze dabei für die Anzahl der Wiederholungen die Funktion `len`, der Ausdruck `len(liste)` liefert die Anzahl der Elemente in liste zurück. Dein Code sollte auch funktionieren, wenn die Liste mehr oder weniger als fünf Elemente enthält!

@[Ausgeben der Einkaufsliste]({"stubs": ["listeiterieren.py"], "command": "python3 test_listeiterieren.py", "project": "python"})

## Iterieren von Listen direkt über die Elemente

Neben der Iteration mithilfe des Index, die im obigen Beispiel nützlich war, um auf beide Listen an der gleichen Stelle zuzugreifen, gibt es auch noch eine andere Art die Liste zu durchlaufen. Diese kennen wir tatsächlich auch schon von der for-Wiederholung. Ersetzen wir zur Verdeutlichung die Range durch eine normale Liste:

```python runnable
indizes = [0, 1, 2, 3, 4]
for index in indizes:
    print(index)
```

Dieser Code liefert dasselbe Ergebnis wie die Variante mit `range(5)`. Es wäre also plausibel, den Kopf `for index in indizes` der Wiederholung so zu lesen:

> Für jeden **index** in **indizes**:  

Statt jetzt eine Liste mit Zahlen zu verwenden, könnten wir zumindest die Einkaufsliste auch so ausgeben:

```python runnable
einkaufsliste = ["Mehl", "Backpulver", "Zucker", "Margarine", "Eier"]
mengen = [400, 1, 250, 200, 4]

for produkt in einkaufsliste:
    print(produkt)
```

Wir wollen dieses Konzept jetzt nutzen, um eine Liste von Preisen, die Annabel von ihrem letzten Einkauf noch hat, zusammenzuzählen.

Die Methode `preiseAddieren` soll alle Einträge von `preise` zusammen addieren, in `summe` speichern und dann ausgeben. Der Code soll auch mit Listen unterschiedlicher Länge funktionieren.

::: Hinweis
Eine Summe nach und nach aufzubauen kann wie folgt umgesetzt werden.
Die beiden Aufrufe `sum = sum + 1` und `sum += 1` weisen jeweils der Variable den um eins erhöhten Wert zu.

```python
sum = 0
sum = sum + 1
sum += 1
print(sum) # sum ist jetzt gleich 2!
```
:::

@[Summieren von Preisen]({"stubs": ["listeaddieren.py"], "command": "python3 test_listeaddieren.py", "project": "python"})
