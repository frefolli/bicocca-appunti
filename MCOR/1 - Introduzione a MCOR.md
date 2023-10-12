# Lez.1 - Introduzione a MCOR

## Programmazione Sequenziale

- Semantica operazionale: data una Macchina Astratta si descrivono i passi di computazione come funzione $M : I \rightarrow O$.
- Semantica denotazionale: dato un Programma, assegno una funzione $f : I \rightarrow O$ (= lambda calcolo).
- Semantica assiomatica: specificare le proprieta' di un programma come funzione $P : I \rightarrow O$, dove i dati in input vengono specificati come i valori che gli input possono assumere in termini di condizioni, e vice versa gli output.

Caratteristiche della programmazione sequenziale:
- Terminazione
- Composizionalita': composizione funzionale f,g: $h : D(f) \rightarrow C(g) = f * g$, con $C(f) \equiv D(g)$

Notazione `I P O`, ex: $\{x>0\}$ P $\{x<0\}$

### Con programmi concorrenti

P1: $x = 2$, allora $\{x = V\}$ P1 $\{x = 2\}$.
P2: $x = 3$, allora $\{x = V\}$ P2 $\{x = 3\}$.
P3: $x += 1$, allora $\{x = V\}$ P3 $\{x = V\}$.

Esecuzione di $P1 \rightarrow P2$. $\{x = V\}$ P1 P2 $\{x = 3\}$.
Se si mettono in parallelo: $\{x = V\}$ P1 && P2 $\{x = 2 \lor x = 3\}$.
Con esecuzione in parallelo di P1,P2,P3: $\{x = V\}$ P2 && P3 $\{x = 2 \lor x = 3 \lor x = 4\}$.

## Labelled Transition System (LTS)

Sistema di Transizioni Etichettate scritto $(S, AcT, T)$ dove:
- $S$ e' insieme di stati
- $Act$ e' insieme di nomi di azioni
- $T$ e' la funzione di transizione denotata $T: S \times AcT \rightarrow S$, dove:
  - $(s, a, s') \in T$
  - $s \xrightarrow[]{a} s'$
  - $(s) \xrightarrow[]{a} (s')$
- formalmente, $s \xrightarrow[]{w} s'$ sse:
  - o) $w = \epsilon \land s = s'$
  - o) $w = a*x \land s \xrightarrow[]{a} s'' \xrightarrow[]{x} s'$

## Calculus of Communicating Systems (CCS)

- Lambda calcolo di processi concorrenti
- Communicating Sequential Processes.

``Un set di programmi e' un insieme di processi che vengono composti con l'operatore di esecuzione parallela e tramite la sincronizzazione l'interazione con l'ambiente.``

E' un sistema di calcolo interpretato come [LTS](#labelled-transition-system-lts) che viene denotato con la seguente espressione BNF:

$$
P ::= 0 \,\,\,
  | \,\,\, a. \, P_{1} \,\,\,
  | \,\,\, A\,\,\,
  | \,\,\, P_{1} + P_{2} \,\,\,
  | \,\,\, P_{1} | P_{2} \,\,\,
  | \,\,\, P_{1} [b/a] \,\,\,
  | \,\,\, P_{1} {\backslash }a \,\,\,
$$

Che significa rispettivamente:
- il processo inattivo generico $0$
- $P$ esegue $a$ e diventa $P_1$
- definendo $A \stackrel{def}{\equiv} P_1$ si usa $A$ come identificatore
- $P$ diventa $P_1$ **o** $P_2$
- $P_1$ e $P_2$ coesistono
- a $P_1$ si rinomina l'azione $a \rightarrow b$
- a $P_1$ si rimuove l'azione $a$

Due processi P1 e P2 sono detti equivalenti non in termini funzionali, ma "all'osservazione", cioe' se un processo esterno non e' in grado di distinguere tra i processi P1 e P2 interagendo con essi. (Liskov dei poveri). La Bisimulazione e' tecnica di verifica per identificare se due processi sono dissimili.

Si denota un sistema CCS come tupla $(K, Act, T)$, dove
- $K$, insieme di nomi di Processi
- $A$, insieme di nomi di azioni
- $\overline A$, insieme di conomi di azioni, (= $\overline a \in \overline A$ e' il reciproco di $a \in A$, es: SYN e ACK)
- $Act = A \cup B \cup \{t\}$, con $t \not \in A$
- $(A \cup B)$ sono le azioni osservabili
- $t$ e' azione di handshake tra due processi (azione che non aspetta nulla indre', ndr)

Sia $P$ un processo $P \in K$, ricordando la notazione LTS:
- es: $(P = a . \ P)$ := P esegue $a$ e poi si comporta come $P$ (ricorsione)
- $(P1) \xrightarrow[]{a} (P2)$ denota sincronizzazione e mutamento
- $(P1) \xrightarrow[]{a} (P1)$ denota ricorsione di processo

### ${B^1}$

${B^1}_0 = in \; . \; {B^1}_1$
${B^1}_1 = \overline {out} \; . \; {B^1}_0$

```d2lang
B1: "{B^1}_0"
B2: "{B^1}_1"

B1 -> B2: "in"
B2 -> B1: "out"
```

### ${B^2}$

${B^2}_0 = in \; . \; {B^2}_1$
${B^2}_1 = \overline {out} \; . \; {B^2}_0 \; + \; in \; . \; {B^2}_2$
${B^2}_2 = \overline {out} \; . \; {B^2}_1$

```d2lang
B0: "{B^2}_0"
B2: "{B^2}_1"
B2: "{B^2}_2"

B0 -> B1: "in"
B1 -> B0: "out"
B1 -> B2: "in"
B2 -> B1: "out"
```

### L'esecuzione parallela ${B^1}_0 | {B^1}_0$ e' bisimile a ${B^2}_0$

```d2lang
A0: "B0 | B0"
A1: "B0 | B1"
A2: "B1 | B0"
A3: "B1 | B1"

A0 -> A1: "in"
A0 -> A2: "in"
A1 -> A3: "in"
A1 -> A0: "out"
A2 -> A3: "in"
A2 -> A0: "out"
A3 -> A1: "out"
A3 -> A2: "out"
```
