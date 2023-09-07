import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import logging
import re
import os
from typing import Optional, Tuple, Callable, Pattern, List, TypeVar

# Matplotlib formatting
# -----------------------------------------------------------------------------
matplotlib.rcParams["text.usetex"] = True
matplotlib.rcParams.update({"font.size": 10, "font.family": "STIXGeneral"})
matplotlib.rcParams["xtick.minor.size"] = 0
matplotlib.rcParams["xtick.minor.width"] = 0
# -----------------------------------------------------------------------------


# TEXT
# ------------------------------------------------------------------------------------
# DEFINIZIONE ESPRESSIONI REGOLARI
titoloRegex: Pattern[str] = re.compile(
    r"""
    (Titolo:)
    (\s)*
    (.*)
    """,
    re.VERBOSE,
)

ascisseRegex: Pattern[str] = re.compile(
    r"""
    (Nome)(\s)(asse)(\s)(delle)(\s)(ascisse:)
    (\s)*
    (.*)
    """,
    re.VERBOSE,
)

ordinateRegex: Pattern[str] = re.compile(
    r"""
    (Nome)(\s)(asse)(\s)(delle)(\s)(ordinate:)
    (\s)*
    (.*)
    """,
    re.VERBOSE,
)

datiRegex: Pattern[str] = re.compile(
    r"""
    (Nome)(\s)(dati)(\s)
    (\d)*
    (:)
    (\s)*
    (.*)
    """,
    re.VERBOSE,
)

funzioneRegex: Pattern[str] = re.compile(
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
    def __init__(self, text_file: str, **kwargs) -> None:
        # logging
        self.log = kwargs.get("log_file", False)

        if self.log:
            try:
                os.remove("log/self.log")
            except Exception as _:
                print(f"Il file {self.log} non esiste.")
            Functions.activate_logging(log_file=self.log)
        else:
            try:
                os.remove("log/log_graphs.log")
            except Exception as _:
                print("Il file log.log non esiste.")
            Functions.activate_logging()

        logger_t.info("Creato oggetto 'Text'.")

        try:
            with open(text_file) as self.file:
                logger_t.debug("File di testo (sorgente) aperto.")

                self.lines = (
                    self.file.read().splitlines()
                )  # memorizza le righe del file
                self.file.close()  # chiude il file

                logger_t.debug("File di testo (sorgente) chiuso.")
        except Exception:
            logger_t.exception("Errore nell'apertura del file")

        self.titolo: str = ""
        self.ascisse: str = ""
        self.ordinate: str = ""
        self.dati: List[str] = []
        self.funzioni: List[str] = []

    def get_titolo(self) -> str:
        """
        Questa funzione cerca la riga con il titolo del grafico mediante
        l'oggetto `titoloRegex`. Una volta trovato, lo restituisce come
        stringa di testo.
        """

        logger_t.info("Chiamata funzione 'get_titolo()'.")

        for line in self.lines:
            if _ := titoloRegex.search(line):
                logger_t.debug(f"Trovato ed ottenuto il titolo --> {_.groups()[-1]}.")
                self.titolo = _.groups()[-1]

        return self.titolo

    def get_ascisse(self) -> str:
        """
        Questa funzione cerca la riga con il nome dell'asse delle ascisse mediante
        l'oggetto `ascisseRegex`. Una volta trovato, lo restituisce come
        stringa di testo.
        """

        logger_t.info("Chiamata funzione 'get_ascisse()'.")

        for line in self.lines:
            if _ := ascisseRegex.search(line):
                logger_t.debug(
                    f"Trovato ed ottenuto il nome delle ascisse --> {_.groups()[-1]}."
                )
                self.ascisse = _.groups()[-1]

        return self.ascisse

    def get_ordinate(self) -> str:
        """
        Questa funzione cerca la riga con il nome dell'asse delle ordinate mediante
        l'oggetto `ordinateRegex`. Una volta trovato, lo restituisce come
        stringa di testo.
        """

        logger_t.info("Chiamata funzione 'get_ordinate()'.")

        for line in self.lines:
            if _ := ordinateRegex.search(line):
                logger_t.debug(
                    f"Trovato ed ottenuto il nome delle ordinate --> {_.groups()[-1]}."
                )
                self.ordinate = _.groups()[-1]

        return self.ordinate

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

        logger_t.info(f"Chiamata funzione 'get_dati({n})'.")

        counter: int = 0

        try:
            for line in self.lines:
                if _ := datiRegex.search(line):
                    counter += 1
                    logger_t.debug(
                        f"Trovato il nome del dataset {counter} --> {_.groups()[-1]}."
                    )
                    self.dati.append(_.groups()[-1])

            logger_t.info(f"Ottenuto il nome del dataset {n}.")
            return self.dati[n - 1]
        except Exception:
            logger_t.exception("Errore nella restituzione del nome dei dati.")

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

        logger_t.info("Chiamata funzione 'get_dati()'.")

        counter = 0

        try:
            for line in self.lines:
                if _ := funzioneRegex.search(line):
                    counter += 1
                    logger_t.debug(
                        f"Trovato il nome della funzione {counter} --> {_.groups()[-1]}."
                    )
                    self.funzioni.append(_.groups()[-1])

            logger_t.info(f"Ottenuto il nome della funzione {n}.")
            return self.funzioni[n - 1]
        except Exception:
            logger_t.exception("Errore nella restituzione del nome della funzione.")


# ------------------------------------------------------------------------------------


# INIZIO PROGRAMMA
# ------------------------------------------------------------------------------------
# variabili globali
# global_text: Text = None
logger: logging.Logger = None
logger_f: logging.Logger = None
logger_t: logging.Logger = None
counter_scatter_plots: int = 0
counter_plots: int = 0


class Functions:
    """
    Libreria interna di funzioni utili, ma non abbastanza grandi da avere
    una libreria esterna propria.
    """

    @staticmethod
    def addensa(data: np.ndarray, d: int) -> np.ndarray:
        """
        Questa funzione prede come input un set di dati, forniti dall'utente sotto
        forma di array numpy, e restituisce un altro array con maggiore densità (più
        dati).

        In particolare, la funzione calcola la distanza minima tra due dati consecutivi
        ed aggiunge tanti dati quanti servono, affinché la distanza tra tutte le coppie di dati
        sia circa quella minima diviso 'd'.

        Parametri
        ---
        data: numpy.ndarray
            Array che si desidera "addensare".
        d: int
            Numero di volte in cui si vuole dividere la distanza minima.

        Esempio
        ---
        >>> data = np.array([1, 1.2, 3])
        >>> print(addensa(data))
        [1.         1.1        1.2        1.30588235 1.41176471 1.51764706
        1.62352941 1.72941176 1.83529412 1.94117647 2.04705882 2.15294118
        2.25882353 2.36470588 2.47058824 2.57647059 2.68235294 2.78823529
        2.89411765 3.        ]
        """

        logger_f.info("Chiamata funzione 'addensa()'.")

        res = data
        logger_f.debug(f"Dataset iniziale:\n {data}")

        # trova la distanza minima tra due dati consecutivi
        m = abs(data[1] - data[0])
        for i in range(1, len(data) - 1):
            if (_ := abs(data[i + 1] - data[i])) < m:
                m = _

        if m != 0:
            logger_f.debug(f"Distanza minima --> {m}")

            # addensa
            data_addensato = []
            for i in range(len(data) - 1):
                n = (
                    int(round(abs(data[i + 1] - data[i]) / m, 0)) * d
                )  # calcola il numero di dati da aggiungere all'intervallo

                if i < len(data) - 2:
                    data_addensato.append(
                        list(np.linspace(data[i], data[i + 1], n, endpoint=False))
                    )
                else:
                    data_addensato.append(list(np.linspace(data[i], data[i + 1], n)))

            res = np.array([i for sublist in data_addensato for i in sublist])
            logger_f.debug(f"Dataset finale:\n {res}")
        else:
            logger_f.error(f"Impossibile addensare i dati: distanza minima --> {m}")

        return res

    @staticmethod
    def allarga_campo(data: np.ndarray, sx: float, dx: float, dens: int) -> np.ndarray:
        """
        Questa funzione prede come input un array numpy e lo allunga. Serve per
        allargare il campo dei fit.

        L'allungamento, a sinistra ed a destra, dev'essere dato in numeri come
        all = x/100, dove x ∈ [0, ∞).

        Fa uso della funzione `addensa(data)` per addensare automaticamente l'array
        che viene restituito (quello allungato).

        Parametri
        ---
        data: numpy.ndarray
            Array contenente il set di dati da allargare.
        sx: float
            Percentuale di allungamento a sinistra dell'array.
        dx: float
            Percentuale di allungamento a destra dell'array.
        dens: int
            Corrisponde al parametro di 'd' della funzione `addensa()`.

        Esempio
        ---
        >>> data = np.array([1, 1.2, 3])
        >>> print(allarga_campo(data, 0.2, 0.1))
        [0.6        0.7        0.8        0.9        1.         1.1
        1.2        1.30588235 1.41176471 1.51764706 1.62352941 1.72941176
        1.83529412 1.94117647 2.04705882 2.15294118 2.25882353 2.36470588
        2.47058824 2.57647059 2.68235294 2.78823529 2.89411765 3.        ]
        """

        logger_f.info("Chiamata funzione 'allarga_campo()'.")
        logger_f.debug(f"Dataset iniziale:\n {data}")

        delta_x = max(data) - min(data)  # ampiezza campione
        m, M = min(data), max(data)  # limiti esterni
        x_all = np.empty(len(data) + 2)  # array vuoto da riempire

        # crea array con nuovi limiti esterni
        if sx >= 0 and dx >= 0:
            x_all[0], x_all[-1] = m - sx * delta_x, M + dx * delta_x
            x_all[1:-1] = data

            # cancella eventuali doppioni ai limiti esterni
            if sx + dx == dx and dx != 0:
                x_all = np.delete(x_all, 0)
            elif sx + dx == sx and sx != 0:
                x_all = np.delete(x_all, -1)
            elif dx + sx == 0:
                x_all = np.delete(x_all, [0, -1])

            logger_f.debug(f"Dataset allargato da addensare:\n {x_all}")
        else:
            raise Exception(
                logger_f.exception(f"Impossibile allargare l'array: sx={sx}, dx={dx}.")
            )

        if dens > 1:
            return Functions.addensa(x_all, dens)
        elif dens == 1:
            return x_all
        else:
            raise Exception(logger_f.exception("La densità non può essere negativa."))

    @staticmethod
    def activate_logging(log_file: str = "log_graphs.log") -> None:
        """
        Questa funzione attiva il logging della libreria propagazione.

        Parametri
        ---
        log_file: str
            File .log dove viene memorizzato il log. Di default è
            'log.log', ma può essere cambiato.
        """

        global logger, logger_f, logger_t

        # Cancella il log precedente
        with open(f"log/{log_file}", "w") as f:
            f.close()

        # Main logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False

        # Logger per le funzioni interne a graph.py
        logger_f = logging.getLogger(__name__ + ".Functions")
        logger_f.setLevel(logging.DEBUG)
        logger_f.propagate = False  # evita log ripetuti

        # Logger per Text
        logger_t = logging.getLogger(__name__ + ".Text")
        logger_t.setLevel(logging.DEBUG)
        logger_t.propagate = False  # evita log ripetuti

        # Crea un handler
        handler = logging.FileHandler(f"log/{log_file}")
        handler.setLevel(logging.DEBUG)

        # Formatta l'handler
        format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(format)

        # Aggiunge l'handler al logger
        logger.addHandler(handler)
        logger_f.addHandler(handler)
        logger_t.addHandler(handler)


class Canvas:
    """
    Inizializza un piano cartesiano su cui è possibile disegnare dataset e
    funzioni.

    Parametri
    ---
    text: str
        Nome del file .txt in cui è memorizzato il testo da mostrare
        nel grafico.
    fs: tuple
        Tupla contenente le dimensioni dell'immagine. Se non viene
        specificata, `fs=(12,8)`.
    dpi: int
        'Dots per inches' dell'immagine (vedi documentazione matplotlib).
        Se non viene specificata, `dpi=150`.

    Parametri opzionali
    ---
    save: str
        Se passata come parametro, l'immagine creata viene salvata nella
        cartella ~/img con il nome indicato da tale parametro.
    log_file: str
        Specifica dove si vuole salvare il log della libreria.


    """

    # __instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = super().__new__(cls)
    #     else:
    #         print("Esiste già un oggetto Canvas.")
    #         plt.close()

    #     return cls.__instance

    def __init__(
        self,
        text: Text,
        fs: Optional[Tuple[int, int]] = (12, 8),
        dpi: Optional[int] = 150,
        **kwargs,
    ) -> None:
        logger.info("Creato oggetto Canvas")

        global counter_scatter_plots, counter_plots
        counter_scatter_plots = 0
        counter_plots = 0

        # def proprietà grafico
        self.fig, self.ax = plt.subplots(figsize=(fs[0], fs[1]), dpi=dpi)
        self.kwargs = kwargs

        # testo
        # Functions.get_text(text)
        self.text = text

        # griglia
        self.ax.grid(color="darkgray", alpha=0.5, linestyle="dashed", lw=0.5)

        try:
            # nome assi
            self.ax.set_xlabel(self.text.get_ascisse())
            self.ax.set_ylabel(self.text.get_ordinate())

            # titolo
            plt.title(self.text.get_titolo(), y=1)

            logger.debug("Testo del canvas inserito.")
        except Exception:
            logger.exception("Errore nell'ottenimento del testo relativo al canvas.")

    def __legenda(self) -> None:
        """
        Quando chiamata, questa funzione mostra la legenda nel grafico.
        Fa parte del mainloop dell'oggetto `Canvas`.
        """
        try:
            self.ax.legend(loc=0)
            plt.legend(labelspacing=1)

            logger.debug("Mostrata la legenda.")
        except Exception:
            logger.exception("Errore nel mostrare la legenda.")

    def __save(self) -> None:
        """
        Se l'utente lo vuole, questa funzione salva l'immagine
        nella cartella 'img'.

        Fa parte del mainloop dell'oggetto `Canvas`.
        """

        if "save" in self.kwargs.keys():
            self.fig.savefig(f"img/{self.kwargs['save']}")
            logger.debug("File salvato.")
        else:
            logger.warning("File non salvato.")

    def mainloop(self, show: Optional[bool] = True) -> None:
        """
        Funzione necessaria per renderizzare il grafico voluto. Ciò
        che viene dopo questa funzione non modifica in alcun modo il
        grafico.
        """

        self.__legenda()
        self.__save()
        logger.info("Fine disegno")

        # mostra il grafico s
        if show:
            plt.show()
        elif not show:
            plt.close()


class ScatterPlot:
    """
    Inizializza uno scatter plot dei dati sperimentali forniti
    dall'utente.

    Parametri
    ---
    color: str
        Il colore (matplotlib) dello scatter plot. Di default
        è impostato su 'firebrick'.
    marker: str
        Il tipo di marker (matplotlib) che si vuole utilizzare.
        Di default è impostato su 'o'.
    ms: float
        Dimensione dei markers dello scatter plot. Di default
        viene impostato su 4.
    """

    def __init__(
        self,
        color: Optional[str] = "firebrick",
        marker: Optional[str] = "o",
        ms: Optional[float] = 4,
    ) -> None:
        logger.info("Creato oggetto 'ScatterPlot'")

        self.color = color
        self.marker = marker
        self.ms = ms

        global counter_scatter_plots
        counter_scatter_plots += 1

    def draw(
        self,
        c: Canvas,
        text: Text,
        x: np.ndarray,
        y: np.ndarray,
        yerr: Optional[np.ndarray] = None,
    ) -> None:
        """
        Una volta creata una istanza di 'Scatterplot', utilizzare questa
        funzione per assegnare lo scatter plot generato al canvas su cui
        lo si vuole mostrare.

        Parametri
        ---
        c:
            Istanza di canvas su cui si vuole disegnare lo scatter plot.
        text:
            Istanza di Text in cui è salvato il testo da mostrare.
        x: numpy.ndarray
            Valori delle ascisse dei punti dello scatter plot.
        y: numpy.ndarray
            Valori delle ordinate dei punti dello scatter plot.
        yerr: numpy.ndarray
            Incertezze sui valori di y. Di default viene impostato su None,
            ovvero non vengono mostrati gli errori.
        """

        c.ax.errorbar(
            x,
            y,
            yerr=yerr,
            marker=self.marker,
            color=self.color,
            ms=self.ms,  # marker size
            zorder=2,  # layer
            ls="none",  # line size (none for disconnected dots)
            capsize=2,  # error bars ticks
            label=text.get_dati(counter_scatter_plots),
        )
        logger.debug(f"Dataset {counter_scatter_plots} disegnato.")


class Plot:
    """
    Inizializza una curva (tendenzialmente un fit dei dati sperimentali
    forniti dall'utente).

    Parametri
    ---
    color: str
        Il colore (matplotlib) della curva. Di default è impostato
        su 'black'.
    ac: tuple
        La percentuale di allargamento del campo del fit a dx e sx.
        Di default è (0,0), ovvero non c'è allargamento di campo.
    lw: float
        Spessore della linea che rappresenta la funzione. Di default
        viene impostato su 1.5.
    """

    def __init__(
        self,
        color: Optional[str] = "black",
        ac: Optional[tuple] = (0, 0),
        lw: Optional[float] = 1.5,
    ) -> None:
        logger.info("Creato oggetto 'Plot'")

        self.color = color
        self.ac = ac
        self.lw = lw

        global counter_plots
        counter_plots += 1

    def draw(
        self,
        c: Canvas,
        text: Text,
        x: np.ndarray,
        f: Callable[[np.ndarray], np.ndarray],
        dens: Optional[int] = 2,
    ) -> None:
        """
        Una volta creata una istanza di 'Plot', utilizzare questa
        funzione per assegnare lo scatter plot generato al canvas su cui
        lo si vuole mostrare.

        Parametri
        ---
        c:
            Istanza di Canvas su cui si vuole disegnare lo scatter plot.
        text:
            Istanza di Text in cui è salvato il testo da mostrare.
        x: numpy.ndarray
            Valori delle ascisse dei punti su cui si vuole costruire
            la funzione.
        f: function
            Funzione da disegnare.
        dens: int
            Corrisponde al parametro 'd' della funzione `addensa()`. Di
            default è impostato su 2.
        """

        # Allarga il campo ed addensa
        x_new = Functions.allarga_campo(x, self.ac[0], self.ac[1], dens)
        logger.debug("Campo della funzione allargato ed addensato.")

        c.ax.plot(
            x_new,
            f(x_new),
            color=self.color,
            zorder=1,
            lw=self.lw,
            label=text.get_funzione(counter_plots),
        )
        logger.debug(f"Funzione {counter_plots} disegnata.")


if __name__ == "__main__":
    pass
