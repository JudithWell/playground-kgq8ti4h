# Bonus-Aufgabe: Listen im Bibliotheksverwaltungssystem

Sehr gut, du hast es bis hierher geschafft! Klasse!

Du bist beauftragt worden, ein einfaches Bibliotheksverwaltungssystem zu erstellen. Das System sollte in der Lage sein, Bücher zu **speichern**, **hinzuzufügen**, **entfernen**, **suchen** und **Informationen über vorhandene Bücher auszugeben**. Die Informationen über die Bücher (Titel, Autor, ISBN-Nummer) sollen in drei Listen `titel_liste`, `autor_liste` und `isbn_liste` gespeichert werden.

Im Beispiel unten sind die drei leeren Listen vorgegeben: `titel_liste`, `autor_liste`, und `isbn_liste`.

1. Implementiere eine Funktion `buch_hinzufuegen()`, die ein neues Buch hinzufügt. Die Informationen für ein Buch sollten in den drei Listen an denselben Indizes gespeichert werden.

2. Implementiere eine Funktion `buch_entfernen()`, die ein Buch anhand seiner ISBN aus den Listen entfernt.

3. Implementiere eine Funktion `buch_suchen()`, die nach einem Buch anhand seines Titels sucht und die relevanten Informationen ausgibt. Nutze hierfür die Methode `print()` um Titel, Author und ISBN auszugeben.

4. Implementiere eine Funktion `buch_liste_ausgeben()`, die alle Bücher in der Liste buecher mit ihren Informationen ausgibt.

    ::: Tipp zum Liste ausgeben:
    Hierfür kannst du eine for-Wiederholung verwenden. 

    Die folgenden Anweisungen führen `tueIrgendwas()` für jedes element der liste aus.

    ```python
    for element in liste:
        tueIrgendwas(element)
    ```

    Alternativ kannst du auch recherchieren, wie du die Länge einer Liste bestimmen kannst.
    :::

5. Füge weitere Testdaten hinzu und teste alle Funktionen, um sicherzustellen, dass sie wie erwartet funktionieren.

@[Implementiere ein Bibliotheksverwaltungssystem!]({"stubs": ["bibliotheksverwaltung.py"], "command": "python3 bibliotheksverwaltung.py"})
