# Lez.1

## Programmazione Sequenziale

- Semantica operazionale: data una Macchina Astratta si descrivono i passi di computazione come funzione M : I -> O.
- Semantica denotazionale: dato un Programma, assegno una funzione f : I -> O (= lambda calcolo).
- Semantica assiomatica: specificare le proprieta' di un programma come funzione P : I -> O, dove i dati in input vengono specificati come i valori che gli input possono assumere in termini di condizioni, e vice versa gli output.

Caratteristiche della programmazione sequenziale:
- Terminazione.
- Composizionalita': composizione funzionale f,g: `h : D(f) -> C(g) = f * g`, con `C(f) === D(g)`.

Notazione I P O, ex: {x>0} P {x<0}

### Con programmi concorrenti

P1: x = 2, {x = V} P1 {x = 2}.
P2: x = 3, {x = V} P2 {x = 3}.
P3: x += 1, {x = V} P3 {x = V}.

Esecuzione di P1 -> P2. {x = V} P1 P2 {x = 3}.
Se si mettono in parallelo: {x = V} P1 && P2 {x = 2 v x = 3}.
Con esecuzione in parallelo di P1,P2,P3: {x = V} P2 && P3 {x = 2 v x = 3 v x = 4}.

## Calculus of Communicating Systems (CCS)

- Lambda calcolo di processi concorrenti
- Communicating Sequential Processes.

Un set di programmi e' denotato come un insieme di processi che vengono composti con l'operatore di esecuzione parallela e tramite la sincronizzazione l'interazione con l'ambiente.

Equivalenza tra processi: due processi P1 e P2 sono detti equivalenti non in termini funzionali, ma "all'osservazione", cioe' se un processo esterno non e' in grado di distinguere tra i processi P1 e P2 interagendo con essi. (Liskov dei poveri).

Bisimulazione: tecnica di verifica per identificare se due processi sono dissimili.

## LTS

Sistema di Transizioni Etichettate (S, AcT, T):
- S: insieme di stati
- Act: insieme di nomi di azioni
- T: S x AcT -> S, rappresentato:
  - (s, a, s') in T
  - s -a-> s'
  - (s) --a--> (s')
- formalmente, s -w-> s' sse:
  - o) w = "" and s = s'
  - o) w = a\*x and s -a-> s'' -x-> s'

- K, insieme di nomi di Processi
- A, insieme di nomi di azioni
- B, insieme di conomi di azioni, (= b e' il reciproco di a, es: SYN e ACK)
- Act = A u B u {t}, con t not in A
- (A u B) := azioni osservabili
- t := azione di handshake tra due processi (azione che non aspetta nulla indre', ndr)

Processo P := Espressione CCS, P in K
- es: (P = a . P) := P esegue "a" e poi si comporta come P (ricorsione)
  - (P1) -a-> (P2) := sincronizzazione e mutamento
  - (P1) -a-> (P1) := ricorsione di processo


