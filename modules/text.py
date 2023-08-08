import re
import logging


# LOGGING
# ---------------------------------
# Crea un logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Crea un handlers
handler = logging.FileHandler("info/log.log")
handler.setLevel(logging.DEBUG)

# Formatta l'handler
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(format)

# Aggiunge l'handler al logger
logger.addHandler(handler)
# ---------------------------------


# DEFINIZIONE ESPRESSIONI REGOLARI
titoloRegex = re.compile(
    r"""
    (Titolo:)
    (\s)*
    (.*)
    """,
    re.VERBOSE,
)

ascisseRegex = re.compile(
    r"""
    (Nome)(\s)(asse)(\s)(delle)(\s)(ascisse:)
    (\s)*
    (.*)
    """,
    re.VERBOSE,
)

ordinateRegex = re.compile(
    r"""
    (Nome)(\s)(asse)(\s)(delle)(\s)(ordinate:)
    (\s)*
    (.*)
    """,
    re.VERBOSE,
)

datiRegex = re.compile(
    r"""
    (Nome)(\s)(dati)(\s)
    (\d)*
    (:)
    (\s)*
    (.*)
    """,
    re.VERBOSE,
)

funzioneRegex = re.compile(
    r"""
    (Nome)(\s)(funzione)(\s)
    (\d)*
    (:)
    (\s)*
    (.*)
    """,
    re.VERBOSE,
)


class Text:
    def __init__(self, file: str) -> None:
        logger.info("Creato oggetto 'Text'.")

        try:
            with open(file) as self.file:
                logger.debug("File di testo (sorgente) aperto.")

                self.lines = (
                    self.file.read().splitlines()
                )  # memorizza le righe del file
                self.file.close()  # chiude il file

                logger.debug("File di testo (sorgente) chiuso.")
        except Exception:
            logger.exception("Errore nell'apertura del file")

    def get_titolo(self) -> str:
        """
        Questa funzione cerca la riga con il titolo del grafico mediante
        l'oggetto `titoloRegex`. Una volta trovato, lo restituisce come
        stringa di testo.
        """

        logger.info("Chiamata funzione 'get_titolo()'.")

        for line in self.lines:
            if _ := titoloRegex.search(line):
                logger.debug(f"Trovato ed ottenuto il titolo --> {_.groups()[-1]}.")
                return _.groups()[-1]

    def get_ascisse(self) -> str:
        """
        Questa funzione cerca la riga con il nome dell'asse delle ascisse mediante
        l'oggetto `ascisseRegex`. Una volta trovato, lo restituisce come
        stringa di testo.
        """

        logger.info("Chiamata funzione 'get_ascisse()'.")

        for line in self.lines:
            if _ := ascisseRegex.search(line):
                logger.debug(
                    f"Trovato ed ottenuto il nome delle ascisse --> {_.groups()[-1]}."
                )
                return _.groups()[-1]

    def get_ordinate(self) -> str:
        """
        Questa funzione cerca la riga con il nome dell'asse delle ordinate mediante
        l'oggetto `ordinateRegex`. Una volta trovato, lo restituisce come
        stringa di testo.
        """

        logger.info("Chiamata funzione 'get_ordinate()'.")

        for line in self.lines:
            if _ := ordinateRegex.search(line):
                logger.debug(
                    f"Trovato ed ottenuto il nome delle ordinate --> {_.groups()[-1]}."
                )
                return _.groups()[-1]

    def get_dati(self, n: int) -> str:
        """
        Questa funzione cerca le righe con i nomi dei datasets che si vogliono
        mostrare mediante l'oggetto `datiRegex`. Immagazzina i nomi in una
        lista in ordine di apparizione, e restituisce l'elemento richiesto
        dall'utente.

        Parametri
        ---
        n: int
            Numero del dataset di cui si vuole ottenere il nome. Il primo
            dataset che appare nel file ha il numero 1, il secondo il 2 e
            così via.
        """

        logger.info("Chiamata funzione 'get_dati()'.")

        res = []
        counter = 0

        try:
            for line in self.lines:
                if _ := datiRegex.search(line):
                    counter += 1
                    logger.debug(
                        f"Trovato il nome del dataset {counter} --> {_.groups()[-1]}."
                    )
                    res.append(_.groups()[-1])

            logger.info(f"Ottenuto il nome del dataset {n}.")
            return res[n - 1]
        except Exception:
            logger.exception("Errore nella restituzione del nome dei dati.")

    def get_funzione(self, n: int) -> str:
        """
        Mediante l'oggetto `funzioneRegex`, questa funzione cerca le righe con i
        nomi delle funzioni che si vogliono mostrare. Immagazzina i nomi in una
        lista in ordine di apparizione, e restituisce l'elemento richiesto
        dall'utente.

        Parametri
        ---
        n: int
            Numero della funzione di cui si vuole ottenere il nome. La prima
            funzione che appare nel file ha il numero 1, la seconda il 2 e
            così via.
        """

        logger.info("Chiamata funzione 'get_dati()'.")

        res = []
        counter = 0

        try:
            for line in self.lines:
                if _ := funzioneRegex.search(line):
                    counter += 1
                    logger.debug(
                        f"Trovato il nome della funzione {counter} --> {_.groups()[-1]}."
                    )
                    res.append(_.groups()[-1])

            logger.info(f"Ottenuto il nome della funzione {n}.")
            return res[n - 1]
        except Exception:
            logger.exception("Errore nella restituzione del nome della funzione.")


if __name__ == "__main__":
    text = Text("text.txt")

    print(text.get_funzione(2))
