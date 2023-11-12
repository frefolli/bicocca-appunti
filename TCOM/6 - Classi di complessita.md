# Lez.6 - Classi di complessita'

## Problema SAT

Input: espressione booleana in Forma Normale Congiuntiva.
Output: l'espressione ammette soluzione? 

__IDEA__: Il certificato e' l'assegnamento delle variabili $v_k \in \{0,1\}$.
- Il certificato e' lineare nel numero di variabili quindi e' polinomiale.
- devo dimostrare che esiste un verificatore che lavora in tempo polinomiale
  - costruisco la macchina di turing non deterministica che forka in tempo polinomiale i certificati per il verificatore
- $SAT \in NP$

## dTSP

Dato $TSP$ si crea un problema di decisione $dTSP$ che ha come input un'istanza di TSP e un valore K: come output decide se quel input ha soluzione in TSP con al massimo costo K.

### $dTSP \in NP$

__IDEA__: Il certificato e' la sequenza di nodi (il cammino, il ciclo) $v_i,v_j \in V | (v_i, v_j) \in w \subseteq (V \times V)$.
- Il certificato e' lineare nel numero di nodi quindi e' polinomiale.
- devo dimostrare che esiste un verificatore che lavora in tempo polinomiale
- il verificatore controlla la sequenza di nodi e valida i collegamenti, l'unicita' dei nodi e il costo massimo, in tempo polinomiale
- esiste una macchina NDTM che genera i certificati in modo combinatorio e parallelo, in tempo polinomiale rispetto al numero di nodi del grafo

## Decisione su linguaggi

## $co \; P$

- $co \; P = \{L | \overline {L} \in P \} \not \equiv \overline {P}$
  - insieme dei linguaggi il cui complemento e' decidibile
  - l'insieme dei linguaggi non decidibili

- $co \; P \equiv P$
  - $L \in P \Rightarrow M$ decide L in tempo polinomiale
  - $\forall x \in \Sigma ^ {*} \;\; x \in L \Rightarrow M(x) = Y \;\; x \not \in L \Rightarrow M(x) = N$
  -
  - $\overline {L} \in P \Rightarrow M'$ decide \overline {L} in tempo polinomiale
  - $\forall x \in \Sigma ^ {*} \;\; x \in \overline {L} \Rightarrow M'(x) = Y \;\; x \not \in \overline {L} \Rightarrow M'(x) = N$
  - $M' = ! M$
  -
  - $\forall L \in P \Rightarrow L \in co \; P$
  - e vice versa
  - $P \equiv co \; P$

## $co \; NP$

- $co \; NP = \{L \; | \; \overline {L} \in NP \}$
  - insieme dei linguaggi il cui complemento e' ricorsivamente enumerabile
  - non e' stato dimostrato se $NP \equiv co \; NP$
  - $P \subseteq NP \land P \subseteq co \; NP \;\; \Leftrightarrow \;\; P \subseteq (NP \cap co \; NP)$

## Riducibilita' dei problemi

esiste $NP_{intermedio}$ tale che:
- ${NP}_{intermedio} \subseteq NP$
- ${NP}_{intermedio} \not \subseteq {NP}_{hard}$
- ${NP}_{intermedio} \not \subseteq {co \; NP}$

### Riduzione polinomiale

$\exists$ Funzione di riduzione $f : \Sigma^{\*} \rightarrow \Sigma^{\*}$ tale che:
- $\forall x \in \Sigma^{\*} \Rightarrow x \in L_a \Leftrightarrow f(x) \in L_b$

Allora, se chiamo $f \; \equiv \; \leq_p$:
- $L_a \leq_p L_b \; \land \; L_b \in P \; \Rightarrow \; L_a \in P$
- $L_a \leq_p L_b \; \land \; L_b \leq_p L_c \; \Rightarrow \; L_a \leq_p L_c$

Per definizione di ${NP}_{hard}$:
- $L \in {NP}_{hard} \; \Leftarrow \; \forall L' \in NP \; | \; L' \leq_p L$
  - sono difficili almeno tanto i linguaggi in $NP$.

Per definizione di ${NP}_{completo}$:
- $L \in {NP}_{completo} \; \Leftarrow \; L \in NP \; \land \; L \in {NP}_{hard}$

$L_a {\leq}_{p} L_b \; \land \; L_a \in {NP}_{hard} \; \Rightarrow \; L_b \in {NP}_{hard}$

### Teoriema di Cook-Levim

Il teorema permette di dimostrare che SAT e' ${NP}_{completo}$.

Per il teorema C.L.:
- $\forall L \in NP \; \Rightarrow \; \exists \leq_p \; | \; L \leq_p SAT$
- quindi per definizione di ${NP}_{hard}$, si dice che $SAT \in {NP}_{hard}$
- quindi posso dire che $SAT \in NP \; \land \; SAT \in {NP}_{hard} \; \Rightarrow \; SAT \in {NP}_{completo}$
