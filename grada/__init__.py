import os

# creates necessary directories
try:
    os.mkdir("./img")
    os.mkdir("./log")
    os.mkdir("./text")
except Exception as e:
    print(e)

# creates the text file
with open("text/text_example.txt", "w") as file:
    file.write(
        r"""
FILE DI TESTO CON LE STRINGHE DA MOSTRARE NEL GRAFICO. 
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
