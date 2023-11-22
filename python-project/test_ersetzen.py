import ersetzen as p
import builtins

print(p.einkaufsliste)

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")

def test_ersetzen():
    try:
        assert len(p.einkaufsliste) == 4, "Einkaufsliste hat die falsche Länge!"
        assert p.einkaufsliste[2] == "Margarine", '''einkaufsliste[2] ... erwartet "Margarine", tatsächlich {}'''.format(p.einkaufsliste[2])
        
        assert len(p.mengen) == 4, "Mengen hat die falsche Länge!"
        assert p.mengen[2] == 200, '''mengen[2] ... erwartet 200, tatsächlich {}'''.format(p.mengen[2])
        success()
        
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)
        if p.mengen[2] == "200":
            send_msg("Tipp 💡", "Denk daran, dass die Einträge von mengen Zahlen und keine Zeichenketten sind.")
            
if __name__ == "__main__":
    test_ersetzen()
