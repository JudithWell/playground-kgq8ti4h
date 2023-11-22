import listeaddieren
import builtins

sum = 0
printEnabled = True

def printHack(x):
    global sum
    global printEnabled
    sum = x
    if printEnabled:
        printOrig(x)

printOrig = builtins.print
builtins.print = printHack


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")

def test_listeaddieren():
    global sum
    global printEnabled
    try:
        listeaddieren.preiseAddieren()
         
        assert sum == 18.95, "summe ist {} ... Erwarteter Wert: 18.95.".format(sum)
        
        printEnabled = False
        listeaddieren.preise = [1, 2, 3]
        try:
            listeaddieren.preiseAddieren()
        except IndexError as e:
            assert False, "Dein Code summiert Listen unterschiedlicher Länge nicht ordnungsgemäß!"
        assert sum == 6, "Dein Code summiert Listen unterschiedlicher Länge nicht ordnungsgemäß!"
        builtins.print = printOrig
        
        success()
        send_msg("Super gemacht!", "Du hast die Aufgabe gelöst!")
        
    except AssertionError as e:
        builtins.print = printOrig
        fail()
        send_msg("Das hat nicht geklappt! 🐞", e)


if __name__ == "__main__":
    test_listeaddieren()
