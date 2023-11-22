from entfernen import einkaufsliste, mengen
import entfernen

# Detect if entfernen index was used:
entfernenIndex_used = False

def new_entfernenIndex(idx):
    global entfernenIndex_used
    entfernenIndex_used = True
    return entfIdx(idx)

entfIdx = entfernen.entfernenIndex
entfernen.entfernenIndex = new_entfernenIndex



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")

def test_entfernen():
    try:
        assert len(einkaufsliste) == 5, "1 Einkaufsliste hat die falsche Länge!"
        assert len(mengen) == 5, "1 Mengen hat die falsche Länge!"
        
        entfernen.entfernen("Mehl")
        
        assert entfernenIndex_used == True, "Verwende in deiner Funktion entfernen() die Funktion entfernenIndex()!"        
        assert len(einkaufsliste) == 4, "2 Einkaufsliste hat die falsche Länge!"
        assert len(mengen) == 4, "2 Mengen hat die falsche Länge!"
        
        entfernen.entfernen("Zucker")
        
        assert len(einkaufsliste) == 3, "3 Einkaufsliste hat die falsche Länge!"
        assert len(mengen) == 3, "3 Mengen hat die falsche Länge!"
        assert einkaufsliste[0] == "Backpulver", "Falsches Element entfernt"
        assert mengen[0] == 1, "Falsches Element entfernt"
        
        liste = einkaufsliste.copy()
        for el in liste:
            entfernen.entfernen(el)
        
        assert len(einkaufsliste) == 0, "4 Einkaufsliste hat die falsche Länge!"
        assert len(mengen) == 0, "4 Mengen hat die falsche Länge!"
        success()
        send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")
        
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)


if __name__ == "__main__":
    test_entfernen()
