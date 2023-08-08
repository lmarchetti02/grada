import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from text import Text
import logging

# Matplotlib formatting
# -----------------------------------------------------------------------------
matplotlib.rcParams["text.usetex"] = True
matplotlib.rcParams.update({"font.size": 10, "font.family": "STIXGeneral"})
matplotlib.rcParams["xtick.minor.size"] = 0
matplotlib.rcParams["xtick.minor.width"] = 0
# -----------------------------------------------------------------------------


# LOGGING
# ------------------------------------------------------------------------------------
# Cancella il log precedente
with open("log.log", "w") as file:
    file.close()

# Main logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Logger per le funzioni interne a graph.py
logger_f = logging.getLogger(__name__ + ".Functions")
logger_f.setLevel(logging.DEBUG)
logger_f.propagate = False  # evita log ripetuti

# Crea un handler
handler = logging.FileHandler("log.log")
handler.setLevel(logging.DEBUG)

# Formatta l'handler
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(format)

# Aggiunge l'handler al logger
logger.addHandler(handler)
logger_f.addHandler(handler)
# ------------------------------------------------------------------------------------


# oggetto Text da creare
global_text = None

# TODO: Functions troubleshooting + logging


class Functions:
    """
    Libreria interna di funzioni utili, ma non abbastanza grandi da avere
    una libreria esterna propria.
    """

    @staticmethod
    def addensa(data):
        """
        Questa funzione prede come input un set di dati, forniti dall'utente sotto
        forma di array numpy, e restituisce un altro array con maggiore densità (più
        dati).

        In particolare, la funzione calcola la distanza minima tra due dati consecutivi
        ed aggiunge tanti dati quanti servono, affinché la distanza tra tutte le coppie di dati
        sia circa la metà di quella minima.

        Parametri
        ---
        data: numpy.ndarray
            Array che si desidera "addensare".

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
        m = data[1] - data[0]
        for i in range(1, len(data) - 1):
            if (_ := abs(data[i + 1] - data[i])) < m:
                m = _

        if m != 0:
            logger_f.debug(f"Distanza minima --> {m}")

            # addensa
            data_addensato = []
            for i in range(len(data) - 1):
                n = (
                    int(round((data[i + 1] - data[i]) / m, 0)) * 2
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
            logger_f.error("Impossibile addensare i dati")

        return res

    @staticmethod
    def allarga_campo(data, sx, dx):
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

        delta_x = max(data) - min(data)  # ampiezza campione
        m, M = min(data), max(data)  # limiti esterni
        x_all = np.empty(len(data) + 2)  # array vuoto da riempire

        # crea array con nuovi limiti esterni
        x_all[0], x_all[-1] = m - sx * delta_x, M + dx * delta_x
        x_all[1:-1] = data

        # cancella eventuali doppioni ai limiti esterni
        if sx - dx < 0:
            x_all = np.delete(x_all, 0)
        elif dx - sx < 0:
            x_all = np.delete(x_all, -1)
        elif dx + sx == 0:
            x_all = np.delete(x_all, [0, -1])

        return Functions.addensa(x_all)

    @staticmethod
    def get_text(file_txt: str) -> None:
        """
        Quando chiamata, questa funzione attacca un oggetto
        `Text` alla variabile `global_text`. In questo modo, è
        sufficiente indicare il file di testo come parametro una
        volta sola (tutte le classi fanno riferimento a `global_text`).

        Parametri
        ---
        file_txt: str
            File .txt dove sono memorizzate le stringhe di testo
            da mostrare nel grafico.
        """

        global global_text
        global_text = Text(file_txt)


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

    """

    def __init__(self, text: str, fs: tuple = (12, 8), dpi: int = 150, **kwargs):
        logger.info("Creato oggetto Canvas")

        self.fig, self.ax = plt.subplots(figsize=(fs[0], fs[1]), dpi=dpi)
        self.kwargs = kwargs

        # testo
        Functions.get_text(text)
        self.text = global_text

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

    def legenda(self) -> None:
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

    def save(self) -> None:
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

    def mainloop(self, show=True) -> None:
        self.legenda()
        self.save()
        logger.info("Fine disegno")

        # mostra il grafico s
        if show:
            plt.show()
            logger.info("Grafico renderizzato.")
        else:
            logger.info("Grafico non renderizzato.")


class ScatterPlot:
    counter = 0

    def __init__(self, color: str, marker: str):
        logger.info("Creato oggetto 'ScatterPlot'")

        self.color = color
        self.marker = marker
        self.text = global_text
        ScatterPlot.counter += 1

    def draw(self, c, x, y, yerr=None):
        c.ax.errorbar(
            x,
            y,
            yerr=yerr,
            marker=self.marker,
            color=self.color,
            ms=4,  # marker size
            zorder=2,  # layer
            ls="none",  # line size (none for disconnected dots)
            capsize=2,  # error bars ticks
            label=self.text.get_dati(ScatterPlot.counter),
        )
        logger.debug(f"Dataset {ScatterPlot.counter} disegnato.")


class Plot:
    counter = 0

    def __init__(self, color: str, ac=(0, 0)) -> None:
        logger.info("Creato oggetto 'Plot'")

        self.color = color
        self.ac = ac
        self.text = global_text
        Plot.counter += 1

    def draw(self, c, x, f):
        # Allarga il campo ed addensa
        x_new = Functions.allarga_campo(x, self.ac[0], self.ac[1])
        logger.debug("Campo della funzione allargato ed addensato.")

        c.ax.plot(
            x_new,
            f(x_new),
            color=self.color,
            zorder=1,
            lw=1.5,
            label=self.text.get_funzione(Plot.counter),
        )
        logger.debug(f"Funzione {Plot.counter} disegnata.")


if __name__ == "__main__":
    # DATI
    x = np.linspace(-5, 5, 50)
    y = x**2
    y_err = np.full(50, 0.5)

    x1 = np.linspace(-3, 3, 30)
    y1 = x1**3
    y1_err = np.full(30, 0.5)
    # ---------------------------

    canvas = Canvas("text.txt")

    scatter = ScatterPlot("firebrick", "o")
    scatter.draw(canvas, x, y)

    scatter2 = ScatterPlot("navy", "o")
    scatter2.draw(canvas, x1, y1)

    fit = Plot("black", ac=(0.01, 0.01))
    fit.draw(canvas, x, lambda x: x**2)

    fit2 = Plot("gold", ac=(0.01, 0.01))
    fit2.draw(canvas, x1, lambda x: x**3)

    canvas.mainloop(show=True)
