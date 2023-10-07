# Lez.1 - Introduzione a ML

Types of Machine Learning:
- Supervised: actors read instances of Inputs and are given a labelled Output
- Unsupervised:  actor isn't given an output to compare with
  - Clustering: classification-baed approach in order to group objects based on similar feature values
- Reinforcement: Actor interacts with an env which gives feedback as response of decisions/actions

Some concepts:
- Regression: hashing an input x in I with a regression function f : I -> H, which will be forwarded to the rest of the chain c : H -> O.
- Underfitting: the model doens't respect minim
- Overfitting: the obtined model attains to much to training set

## Inductive Learnign

Basically function approximation (or such):
- Target: $f \in F | f : I \rightarrow O$
- Example: $x \in I \rightarrow (x, f(x))$
- Hypotesis: $h \in H | h \sim f$
- No prior knowledge about $f$
- Examples are given
- Attribute: labelled data

_Occam's razor_: experimental data suggests that usually the simplest model is more correct in terms of concrete general accuracy.

A hypotesis $h$ is consistent with a set Z or pairs (I x O) sse $h(z.I) == z.O$.

The **Hypotesis Space** is the space H of function aproximators $h$ which attempts to be consistent to training set and mimic the target function $f$.

The **Version Space** is the subspace of those h in H, the set of Hypotesis, which adhere (are consistent to) to the training set D.

## Concept Learning

This is the case of inference of a boolean function $h : I \rightarrow {0,1}$ from a training set D, which is basically a classification problem of order 2 (YES/NO classes).

Hypotesis are expressed in declarative form: $<X, Z, A ....>$, where:
- $X, Z, A ...$ are constraints of type
  - $k = X$
  - $k = ?$, every value
  - $k = \emptyset$, never (null hypotesis, no example allowed)

Given two hypotesis h1 & h2, h1 is said _more general_ ($h_1 \ge h_2$) sse $\forall x \in X | h_1(x) \rightarrow h_2(x)$, basically proper set inclusion, thus establishing a partial order relationships over H Space.

While in `Inductive` learning the assumption is never having **overfitting**, and sticking only to dataset aherence, the `Concept` learning algorithms manipulates hypotesis in H space using this $\ge \,\,\, : H \times H$ partial order in order to find the greatest result.