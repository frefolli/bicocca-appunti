# Lez.6 - Classi di complessita'

## Problema SAT

Input: espressione booleana in Forma Normale Congiuntiva.
Output: l'espressione ammette soluzione? 

**IDEA**: Il certificato e' l'assegnamento delle variabili $v_k \in \{0,1\}$.
- Il certificato e' lineare nel numero di variabili quindi e' polinomiale.
- devo dimostrare che esiste un verificatore che lavora in tempo polinomiale
  - costruisco la macchina di turing non deterministica che forka in tempo polinomiale i certificati per il verificatore
- $SAT \in NP$

## NP

NP e' la classe dei problemi che possono:
- essere risolti in tempo polinomiale da una $M \in NDTM$
- essere verificati in tempo polinomiale da una $M \in DTM$

- $P \subseteq NP$
- $P \stackrel{?}{=} NP$, non e' stato dimostrato ne' $=$ ne' $\not =$.
  - La conseguenza sarebbe $co \; NP = NP$

## dTSP

Dato $TSP$ si crea un problema di decisione $dTSP$ che ha come input un'istanza di TSP e un valore K: come output decide se quel input ha soluzione in TSP con al massimo costo K.

### $dTSP \in NP$

**IDEA**: Il certificato e' la sequenza di nodi (il cammino, il ciclo) $v_i,v_j \in V | (v_i, v_j) \in w \subseteq (V \times V)$.
- Il certificato e' lineare nel numero di nodi quindi e' polinomiale.
- devo dimostrare che esiste un verificatore che lavora in tempo polinomiale
- il verificatore controlla la sequenza di nodi e valida i collegamenti, l'unicita' dei nodi e il costo massimo, in tempo polinomiale
- esiste una macchina NDTM che genera i certificati in modo combinatorio e parallelo, in tempo polinomiale rispetto al numero di nodi del grafo

## Decisione su linguaggi

## $co \; P$

- $co \; P = \{L | \overline {L} \in P \} \not \equiv \overline {P}$
  - $co \; P$ e' insieme dei linguaggi il cui complemento e' decidibile da una macchina di turing deterministica in tempo polinomiale.
  - $\overline P$ e' l'insieme dei linguaggi non decidibili da una macchina di turing deterministica in tempo polinomiale.

- $co \; P \equiv P$
  - $L \in P \Rightarrow M$ decide L in tempo polinomiale
  - $\forall x \in \Sigma ^ {\star} \;\; x \in L \Rightarrow M(x) = Y \;\; x \not \in L \Rightarrow M(x) = N$
  -
  - $\overline {L} \in P \Rightarrow M'$ decide $\overline {L}$ in tempo polinomiale
  - $\forall x \in \Sigma ^ {\star} \;\; x \in \overline {L} \Rightarrow M'(x) = Y \;\; x \not \in \overline {L} \Rightarrow M'(x) = N$
  - $M' = \neg M$
  -
  - $\forall L \in P \Rightarrow L \in co \; P$
  - e vice versa
  - $P \equiv co \; P$

## $co \; NP$

- $co \; NP = \{L \; | \; \overline {L} \in NP \}$
  - insieme dei linguaggi il cui complemento e' ricorsivamente enumerabile
  - $co \; NP \stackrel{?}{=} NP$, non e' stato dimostrato ne' $=$ ne' $\not =$.
  - $P \subseteq NP \land P \subseteq co \; NP \;\; \Leftrightarrow \;\; P \subseteq (NP \cap co \; NP)$

## Riducibilita' dei problemi

esiste $NP_{intermedio}$ tale che:
- ${NP}_{intermedio} \subseteq NP$
- ${NP}_{intermedio} \not \subseteq {NP}_{hard}$

Pirola disse:
- ${NP}_{intermedio} \not \subseteq {co \; NP}$

Ma le altre fonti indicano:
- ${NP}_{intermedio} \not \subseteq {P}$

  mi so mia

### Riduzione polinomiale

$\exists$ Funzione di riduzione $f : \Sigma^{\star} \rightarrow \Sigma^{\star}$ tale che:
- $\forall x \in \Sigma^{\star} \Rightarrow x \in L_a \Leftrightarrow f(x) \in L_b$

Allora, se chiamo $f \; \equiv \; \leq_p$ una riduzione in tempo $O(f(n))$:
- $L_a \leq_p L_b \; \land \; L_b \in P \; \Rightarrow \; L_a \in P$
- $L_a \leq_p L_b \; \land \; L_b \leq_p L_c \; \Rightarrow \; L_a \leq_p L_c$

Per definizione di ${NP}_{hard}$:
- $L \in {NP}_{hard} \; \Leftarrow \; \forall L' \in NP \; | \; L' \leq_p L$
  - sono difficili almeno tanto i linguaggi in $NP$.

Per definizione di ${NP}_{completo}$:
- $L \in {NP}_{completo} \; \Leftarrow \; L \in NP \; \land \; L \in {NP}_{hard}$

$L_a {\leq}_{p} L_b \; \land \; L_a \in {NP}_{hard} \; \Rightarrow \; L_b \in {NP}_{hard}$
$L_a {\leq}_{p} L_b \; \land \; L_a \in NP \; \Rightarrow \; L_b \in NP$

### Teoriema di Cook-Levim

Il teorema permette di dimostrare che SAT e' ${NP}_{completo}$.

Per il teorema C.L.:
- $\forall L \in NP \; \Rightarrow \; \exists \leq_p \; | \; L \leq_p SAT$
- quindi per definizione di ${NP}_{hard}$, si dice che $SAT \in {NP}_{hard}$
- quindi posso dire che $SAT \in NP \; \land \; SAT \in {NP}_{hard} \; \Rightarrow \; SAT \in {NP}_{completo}$
