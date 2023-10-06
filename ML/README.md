# Lez.1

- Supervised: actors read instances of Inputs and are given a labelled Output
- Unsupervised:  actor isn't given an output to compare with
- Clustering: ?
- Reinforcement: Actor interacts with an env which gives feedback as response of decisions/actions

- Regression: hashing an input x in I with a regression function f : I -> H, which will be forwarded to the rest of the chain c : H -> O.
- Underfitting: the model doens't respect minim
- Overfitting: the obtined model attains to much to training set

## Inductive Learnign

Basically function approximation (or such):
- Target: `f in F | f : I -> O`
- Example: `x in I -> (x, f(x))`
- Hypotesis: `h in H | h ~ f`
- No prior knowledge about `f`
- Examples are given
- Attribute: labelled data

Experimental data suggests that usually the simplest model is more correct in terms of concrete general accuracy.

A function `h` is consistent with a set Z or pairs (I x O) sse `assert h(z.I) == z.O`.

The **Version Space** is the subspace of those h in H, the set of Hypotesis, which adhere (are consistent to) to the training set D.

## Concept Learning

Inference of a boolean function `h : I -> {0,1}` from a training set D. 

Hypotesis are expressed in declarative form: `<X, Z, A ....>`, where:
- X, Z, A ... are constraints of type
  - k = X, only = X
  - k = ?, every value
  - k = $, never (null hypotesis, no example allowed)

While in `Inductive` learning the assumption is never having **overfitting**, and sticking only to dataset aherence.

Given two hypotesis h1 & h2, h1 is said *more general* (`h1 >= h2`) sse `Vx in X | h1(x) -> h2(x)`, basically proper set inclusion, thus establishing a partial order relationships over H Space.

The `Concept` learning algorithms will manipulate hypotesis in H space using this `>=` partial order in order to find the greatest result.
