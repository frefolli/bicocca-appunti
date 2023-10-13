# Lez.5 - Problemi indecidibili e RIC/RE

## Halting problem

$I$: $TM$ codificata e un input $I$
$O$: $TM(I) \not \equiv NaN$

In altre parole, si decide se una $TM$ termina su un input $I$.

### E' indecidibile.

#### TEO. $\overline {RIC(L_H)}$

#### DIM. Per assurdo sia $RIC(L_H) \Rightarrow \exists M_H \;\; decide \;\; L_H$ 

Allora posso costruire una macchina $C(M)$

- $C(M) = Y$ sse $M_H(M,M) = N$
- $C(M) = NaN$ sse $M_H(M,M) = Y$

  Ovvero la macchina che riconosce le macchine che accettano la propria codifica.

- $C(C) = Y \Rightarrow M_H(C, C) = N \Rightarrow C(C) = NaN$
- - Cioe', se C accetta se stesso, cioe' se C(C) non termina, ma alloca C(C) non termina: contraddizione
- $C(C) = NaN \Rightarrow M_H(C, C) = Y \Rightarrow C(C) = Y$
- - e vice versa

## $RE(L_H)?$

#### TEO. $RE(L_H)$

#### DIM. $\exists M_A \;\; accetta \;\; L_H \Rightarrow M_A(M, X) = Y \Leftrightarrow M(X) \not \equiv NaN$

La macchina di Turing universale simula una macchina $M$ su $X$ e termina sse $M(X) \not \equiv NaN$.

## $\overline{L_H}$

Chiaramente $\overline {RE(\overline{L_H})}$.

Dimostrazione per assurdo: sia per assurdo $RE(\overline{L_H})$.

Essendo $RE(L_H)$ allora $RE(L) \land RE(\overline {L}) \Leftrightarrow RIC(L)$ , tuttavia sappiamo che $\overline {RIC(L_H)}$.
Quindi $\overline{RE(\overline{L_H})}$

# Lez.5 - Complessita'

## Tempo

- $DTIME(f(n))$: L'insieme dei linguaggi $\{L c \Sigma^* | \exists M$ decide $L$ in tempo $O(f(n))\}$
- $DTIME(n)$: Insieme dei problemi di decisione chepossono essere risolti con un algoritmo in tempo $O(n)$.
- $DTIME(n^2) \subseteq DTIME(n)$
- $DTIME(2^n) \subseteq DTIME(n)$
- $P = {U}_{c \in N} DTIME(n^c)$
- $EXPTIME = {U}_{c \in N} DTIME(2^{n^c})$
- $P \subseteq EXPTIME$

## Spazio

- $s_M(x)$ = numero di celle del nastro usate nella computazione di $M(X)$, meno $|X|$ (ovvero oltre all'input)
- $S_M = {max}_{x \in \Sigma^*} \{ s_M(X) \; | \; |X| = n \}$
- $S_M(n) \leq T_M(n) + n$

Se $M$ usa spazio limitato $K$, $\exists M' \equiv M$ che termina per tutti gli input.
Se lo spazio sul nastro e' limitato, allora il numero di configurazioni $(Q \times usize \times \Sigma)$ e' finito.
Per cui $M'$rileva che $M$ e' finita in Loop e si ferma (magari rifiutando).