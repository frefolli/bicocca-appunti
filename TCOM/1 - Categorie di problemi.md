# Lez.1 - Categorie di Problemi

## Distinzione tra:

- Problema trattabile: problemi con algoritmi polinomiali
- Problema non trattabile: problemi senza algoritmi polinomiali
  - dimostrabilmente intrattabile
  - forse intrattabile
  - probabilmente intrattabile
- Problema indecidibile: problema "impossibile"
- Algoritmi galattici: algoritmi polinomiali ma impraticabili

Se si trova un algoritmo polinomiale per i _forse/probabilmente_ intrattabili implica l'esistenza di un algoritmo polinomiale per gli altri, fatta eccezione per i _dimostrabili_.

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
- Lo stato globale e' chiamato _configurazione_:
  - stato
  - simbolo sotto la testina
  - stringa sul nastro a sinistra della testina
  - stringa sul nastro a destra della testina
- Una computazione e' una _sequenza di Configurazioni_.

### Esempio

Input: stringa _x_
Output: scrivere "Hello"

`M = (Q, Z, q6, S)`
- Z = {"H", "e", "l", "o", ">", " "}
- Q = {q0, q1, q2, q3, q4, q5, q6, q7}
- S
  - Si inizia cancellando l'input _x_
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