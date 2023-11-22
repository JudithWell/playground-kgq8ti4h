import einfuegen as p

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")

def test_einfuegen():
    try:
        assert len(p.einkaufsliste) == 5, "Einkaufsliste hat die falsche Länge!"
        assert p.einkaufsliste[1] == "Backpulver", '''einkaufsliste[1] ... erwartet "Backpulver", tatsächlich {}'''.format(p.einkaufsliste[1])
        
        assert len(p.mengen) == 5, "Mengen hat die falsche Länge!"
        assert p.mengen[1] == 1, '''mengen[1] ... erwartet 1, tatsächlich {}'''.format(p.mengen[1])
        success()
        send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")
        
    except AssertionError as e:
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)
        if len(p.einkaufsliste) == 5 and len(p.mengen) == 4:
            send_msg("Tipp 💡", "Denk daran, auch die Liste mengen abzuändern!")


if __name__ == "__main__":
    test_einfuegen()
