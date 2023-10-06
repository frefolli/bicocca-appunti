# Lez.1

## Distinzione tra:

- Problema trattabile: problemi con algoritmi polinomiali
- Problema non trattabile: problemi senza algoritmi polinomiali
  - dimostrabilmente intrattabile
  - forse intrattabile
  - probabilmente intrattabile
- Problema indecidibile: problema "impossibile"
- Algoritmi galattici: algoritmi polinomiali ma impraticabili

Se si trova un algoritmo polinomiale per i *forse/probabilmente* intrattabili implica l'esistenza di un algoritmo polinomiale per gli altri, fatta eccezione per i *dimostrabili*.

### Esempio di P.N.T. dimostrabile

- Input: insieme di elementi V di n elementi
- Output: enumerare tutti i sottoinsiemi di V
- e' impossibile risolvere il problema senza iterare in esponenziale, per la dimensione dell'output.

### Esempio: Primality

- Input: numero natuale n in N
- Output: if (n e' primo) then TRUE else FALSE
- esiste un algoritmo esaustivo (n % (1 -> sqrt(n)) == 0)
- O(2^(k/2)), con k = nbit(n)
- esistono algoritmi probabilistici (test di primalita' di non-ricordo)
- E' un problema trattabile, e' stato trovato un algoritmo polinomiale in O(k^12) o cosi'

## Macchina di Turing

Sistema di controllo a stati finiti che opera su un nastro con transazioni (spostamenti / scritture / letture).

Tesi di Church-Turing: un qualsiasi algoritmo puo' essere rappresentato come una macchina di Turing (e vice versa).
E' enunciato formale non dimostrabile ma accettato come valido, ha come conseguenza tutti i modelli di calcolo che godono di questa proprieta' sono equivalenti.

### Formalmente

Una macchina di Turing `M = (Q, Z, q0, S)`, dove:
- Q e' l'insieme finito degli stati (stato zero = q0)
- Z e' l'insieme finito dei simboli (Alfabeto), che si assume contenga ">", " " (caratteri di controllo).
- S e' la funzione di transizione `S : (Q, x Z) -> (Q x Z x {<-,->,-})`.
- L'input e' sul nastro.
- Se la funzione S non e' definita per la coppia corrente (Q, Z), la macchina termina.
- Si possono aggiungere degli stati di accettazione per distinguere tra arresto e rigettazione.
- Lo stato globale e' chiamato *configurazione*:
  - stato
  - simbolo sotto la testina
  - stringa sul nastro a sinistra della testina
  - stringa sul nastro a destra della testina
- Una computazione e' una *sequenza di Configurazioni*.

### Esempio

Input: stringa *x*
Output: scrivere "Hello"

`M = (Q, Z, q6, S)`
- Z = {"H", "e", "l", "o", ">", " "}
- Q = {q0, q1, q2, q3, q4, q5, q6, q7}
- S
  - Si inizia cancellando l'input *x*
  - (q6, h/e/l/o) -> (q6, " ", ->)
  - E si torna indietro
  - (q6, " ") -> (q7, " ", <-)
  - (q7, " ") -> (q7, " ", <-)
  - (q7, ">") -> (q0, ">", ->)
  - Quindi si scrive "Hello"
  - (q0, " ") -> (q1, "H", ->)
  - (q1, " ") -> (q2, "e", ->)
  - (q2, " ") -> (q3, "l", ->)
  - (q3, " ") -> (q4, "l", ->)
  - (q4, " ") -> (q5, "o", <-)
  - E si torna indietro
  - (q5, h/e/l) -> (q5, h/e/l, <-)

Le configurazioni
- (q6, " ", ">", "")
- (q7, ">", "", " " ...)
- (q0, " ", ">", "")
- (q1, " ", ">H", "")
- (q2, " ", ">He", "")
- (q3, " ", ">Hel", "")
- (q4, " ", ">Hell", "")
- (q5, "l", ">Hel", "o")
- (q5, "l", ">He", "lo")
- ...
- (q5, ">", "", "Hello")

# Lez.2

## Esempio di TM #1: Incremento

Input: un numero naturale *x*, rappresentato in binario
Output: *x + 1*, rappresentato in binario

Attenzione: la soluzione per un numero del tipo "1111....." sembra essere spostare il simbolo di start ">", ma non va assolutamente fatto. Bisogna trovare un altro modo per ottenere lo stesso risultato.

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

Input: stringa *w*
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
