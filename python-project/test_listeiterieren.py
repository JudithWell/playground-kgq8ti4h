import listeiterieren

counterAusgabe = 0
printEnabled = True

def gibAusHack(idx):
    global printEnabled
    global counterAusgabe
    counterAusgabe += 1
    if (printEnabled):
        gibAusOrig(idx)
    
gibAusOrig = listeiterieren.gibAus
listeiterieren.gibAus = gibAusHack


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")

def test_iterieren():
    global counterAusgabe
    global printEnabled
    try:
        # check listen length
        assert len(listeiterieren.einkaufsliste) == 5, "Einkaufsliste hat die falsche Länge!"       
        assert len(listeiterieren.mengen) == 5, "Mengen hat die falsche Länge!"
        
        listeiterieren.listeAusgeben()
        
        assert counterAusgabe == 5, "Verwende die Methode gibAus() zur Ausgabe der Einträge!"
        
        printEnabled = False
        counterAusgabe = 0
        listeiterieren.einkaufsliste = ["Dies", "ist", "ein", "Test", "hier", "gibt", "es", "nichts", "zu", "sehen!"]
        listeiterieren.mengen = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
        listeiterieren.listeAusgeben()
        assert counterAusgabe == 10, "Dein Code kann nicht auf unterschiedliche lange Listen reagieren!"
        
        success()
        send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")
        
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)


if __name__ == "__main__":
    test_iterieren()
