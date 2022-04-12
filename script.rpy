#  Lo script di gioco va in questo file.

#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define vanessa = Character("Miss. Vanessa", color="#f44")
define mike = Character("Prof Mike", color="#d3d921")

# Il gioco comincia qui.

label start:

    # Mostra uno sfondo. Al momento mostra una sagoma generica, ma puoi
    # aggiungere un file (chiamato "bg room.png" oppure "bg room.jpg")
    # alla directory 'images' per cambiarla.


    scene bg school

    # Mostra lo sprite di un personaggio.
    # Al momento mostra una sagoma generica, ma puoi aggiungere un file
    # (chiamato "eileen_happy.png") alla directory 'images' per cambiarla.

    show emily smile at left
    show personaggio base


    # Questo mostra linee di dialogo.

    "La mia storia inzia in una classe di un liceo di Ostia."

    mike "Buongiorno ragazzi e ragazze, io sono il vostro nuovo prof di storia."

    "Classe" "Benvenuto professore!"

    vanessa "Siamo felici che sia lei il nostro prof!"

    menu:
        "Spiega come inserire dei dialoghi in RenPy":
            jump lezione_dialoghi

        "Spiega come inserire le immagini in RenPy":
            jump lezione_immagini

label lezione_dialoghi:
    mike "Allora per inserire dei testi devi usare le virgolette"
    vanessa "Professore a me con le virgolette non va il programma"
    mike "Arrivo e ti do una mano"
    return

label lezione_immagini:
    mike "Inseriemo delle immagini per rendere più piacevole la nostra storia"
    return
