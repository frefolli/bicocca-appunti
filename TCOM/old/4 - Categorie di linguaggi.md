# Lez.4 - Categorie di Linguaggi

## MT con alfabeto binario vs MT con alfabeto non binario

Data M con $\sigma$ t.c. $|\Sigma| > 4$, esiste una MT che puo' risolvere gli stessi problemi di una macchina con $|\Sigma'| = 4$, quindi equivalente.
Con una opportuna funzione di codifica $C : \Sigma \rightarrow \Sigma^{'*}$, si puo' rappresentare l'input di $M$ per $M'$ in modo equivalente (cioe' composizione di funzione $M = C * M'$).
La codifica non e' altro che una riduzione polinomiale.

Detto il tempo di lettura e scrittura di $M$ e $M'$ rispettivamente $T_{M}$ e $T_{M'}$, allora $T_{M'} = k * T_{M}$, con $k = \lceil {log_{|\Sigma'|}{|\Sigma|}} \rceil$. Quindi $T_{M'} = O(k * T_{M}) = O(T_{M})$, quindi asintoticamente la stessa complessita' polinomiale.

Come con la trasformazione di una macchina multi nastro in una a singolo nastro, e' possibile costruire un'algoritmo meccanico che effettua queste conversioni.

## Simulazione di TM

Esiste na MT U t.c. $\forall \sigma, x \in \Sigma^{'*}$, $U(\sigma, x) = M_{\sigma}(x)$, ovvero e' la MT rappresentata da $\sigma$.
In particolare e' una macchina a tre nastri
- un nastro per la descrizione di $M_{\sigma}$
- un nastro per il nastro di lavoro simulato di $M_{\sigma}$
- un nastro per mantenere lo stato simulato di $M_{\sigma}$

Complessita' $T_{U} = O(|\sigma| * T_{M_{\sigma}})$

In particolare questo lavoro puo' essere simulato anche con un nastro singolo costruito cosi':

$work(M') \equiv status(M) \lll desc(M) \lll start \lll work(M)$

## Categorie di linguaggi 

- linguaggi decidibili (o ricorsivi) se esiste una MT $M$ t.c. $\forall x \in \Sigma^*$, $M(x) = 1$ se $x \in L$, o $M(x) = 0$ se $x \not \in L$.
  - se esiste una MT $M$ t.c. $\forall x \in \Sigma^*$, $M(x) = 1$ se $x \in L$, o $M(x) = 0$ se $x \not \in L$.
  - si dice che "M decide L"
- linguaggi semidecidibili (o ricorsivamente enumerabili)
  - se esiste una MT $M$ t.c. $\forall x \in \Sigma^*$, $M(x) = 1$ se $x \in L$, e $M(x) = 0 \lor NaN$ se $x \not \in L$
  - $NaN$ := la macchina non termina
  - si dice che "M accetta L"

detti $RIC(X)$ la proprieta' X e' ricorsivo, e $RE(X)$ la proprieta' X e' ricorsivamente enumerable.

- $RIC(L) \Rightarrow RE(L)$
- $RIC(L) \Rightarrow RIC(\overline L)$
- $RIC(L) \Leftrightarrow RE(L) \land RE(\overline {L})$ 
