import os

# creates necessary directories
try:
    os.mkdir("./img")
except Exception as _:
    print("La directory '/img' esiste già.")

try:
    os.mkdir("./log")
except Exception as _:
    print("La directory '/log' esiste già.")

try:
    os.mkdir("./text")
except Exception as _:
    print("La directory '/text' esiste già.")

# creates the text file
with open("text/text_example.txt", "w") as f:
    f.write(
        r"""FILE DI TESTO CON LE STRINGHE DA MOSTRARE NEL GRAFICO. 
NON MODIFICARE L'ORDINE DELLE RIGHE, NÈ AGGIUNGERE SPAZI.
LE PARTI COMPRESE TRA "$ $" SONO DA SCRIVERE IN LATEX.
#########################################################

Titolo: 


Nome asse delle ascisse: 


Nome asse delle ordinate: 


Nome dati 1:
Nome dati 2: 


Nome funzione 1: 
Nome funzione 2: 
        """
    )

with open("text/blueprint.txt", "w") as f:
    f.write(
        r"""text = g.Text("text/text.txt")

canvas = g.Canvas(text, save="test")

g.ScatterPlot().draw(canvas, text, x, y, y_err)

g.Plot().draw(canvas, text, x, lambda x: x, 5)

canvas.mainloop(show=True)
"""
    )
