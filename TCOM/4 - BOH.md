# Lez.4 - 

## MT con alfabeto binario vs MT con alfabeto non binario

Data M con $\sigma$ t.c. $|\Sigma| > 4$, esiste una MT che puo' risolvere gli stessi problemi di una macchina con $|\Sigma'| = 4$, quindi equivalente.
Con una opportuna funzione di codifica $C : \Sigma \rightarrow \Sigma' * $, si puo' rappresentare l'input di $M$ per $M'$ in modo equivalente (cioe' composizione di funzione $M = C * M'$).

Detto il tempo di lettura e scrittura di $M$ e $M'$ rispettivamente $T_{M}$ e $T_{M'}$, allora $T_{M'} = k * T_{M}$, con $k = \ceil {log_{|\Sigma'|}{|\Sigma|}}$. Quindi $T_{M'} = O(k * T_{M}) = O(T_{M})$, quindi asintoticamente la stessa complessita' polinomiale.

Come con la trasformazione di una macchina multi nastro in una a singolo nastro (vedi [Lez3](Lez3)), e' possibile costruire un'algoritmo meccanico che effettua queste conversioni.

## 

Esiste na MT U t.c. $\forall \sigma, x \in \Sigma^* $, $U(\sigma, x) = M_{\sigma}(x)$, ovvero e' la MT rappresentata da $\sigma$.
In particolare e' una macchina a tre nastri
- una nastro per la descrizione di $M_{\sigma}$
- un nastro per il nastro di lavoro simulato di $M_{\sigma}$
- un nastro per mantenere lo stato simulato di $M_{\sigma}$

Complessita' $T_{U} = O(|\sigma| * T_{M_{\sigma}})$

## Categorie di linguaggi 

- linguaggi decidibili (o ricorsivi) se esiste una MT $M$ t.c. $\forall x \in \Sigma* $, $M(x) = 1$ se $x \in L$, o $M(x) = 0$ se $x \not \in L$.
  - se esiste una MT $M$ t.c. $\forall x \in \Sigma* $, $M(x) = 1$ se $x \in L$, o $M(x) = 0$ se $x \not \in L$.
  - si dice che "M decide L"
- linguaggi semidecidibili (o ricorsivamente enumerabili)
  - se esiste una MT $M$ t.c. $\forall x in \Sigma* $, $M(x) = 1$ se $x \in L$, e $M(x) = 0 \or NaN$ se $x \not \in L$
  - $NaN$ := la macchina non termina
  - si dice che "M accetta L"

- Se $L$ e' Ricorsivo allora $L$ e' Ricorsivamente Enumerabile
- Se $L$ e' ricorsivo allora $\overline L$ e' Ricorsivo
