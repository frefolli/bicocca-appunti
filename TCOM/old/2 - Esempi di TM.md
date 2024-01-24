# Lez.2 - Esempi di TM

## Esempio di TM #1: Incremento

Input: un numero naturale _x_, rappresentato in binario
Output: _x+1_, rappresentato in binario

Attenzione: la soluzione per un numero del tipo "1111....." sembra essere spostare il simbolo di start ">", ma non va assolutamente fatto. Bisogna trovare un altro modo per ottenere lo stesso risultato. Il simbolo di start non deve essere (sovra)scritto ne' spostato.

- prima scorro fino alla fine del numero
- (q0, 0/1) |- (q0, 0/1, ->)
- (q0, " ") |- (q1, " ", <-)
- quindi inizio ad aggiungere 1 in coda
- (q1, 1) |- (q1, 0, <-)
- (q1, >) |- (q3, >, ->)
- (q1, 0) |- (q2, 1, <-)
- (q3, 0) |- (q4, 1, ->)
- (q4, 0) |- (q4, 0, ->)
- (q4, " ") |- (q2, 0, -)

Le configurazioni per "100":
- (q0, 1, >, 00)
- |- (q0, 0, >1, 0)
- |- (q0, 0, >10, "")
- |- (q0, " ", >100, "")
- |- (q1, 0, >10, "")
- |- (q2, 1, >10, "")

Le nozioni di Computazione e Configurazione di TM sono fondamentali per formalizzare l'algoritmo come Computazione.

## Esempio di TM #2

Input: stringa _w_
Output: (palindromap w)

es: "abba"

generics: x, y
- (q0, x) |- (q1, " ", ->)
- (q1, a/b) |- (q1, a/b, ->)
- (q1, " ") |- (q2, " ", <-)
- (q2, x) |- (q3, " ", <-)
- (q3, y) |- (q4, " ", <-)
- (q4, " ") |- (q5, " ", ->)
- (q5, y) |- (q0, " ", ->)

In alternativa si potrebbe tornare direttamente indietro senza ottimizzare il ritorno e ripartire da q0.
