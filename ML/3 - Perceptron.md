# Lez.3 - Perceptron

A **perceptron** is a processor unit $p : I -> O$ which is composable with other perceptrons in order to build neural network.

Within a **perceptron**:
- x is the vector of inputs $x_i$
- $w$ is the vector of weights $w_i$
- $b$ is the bias weight (sometimes noted as $w_0$)
- $\delta$ is the transition function
- $f$ is the feed of a perceptron, $f = \Sigma_{i=0} w_i \cdot x_i$
- $o$ is the output of a perceptron, $o = \delta(f)$

  In this course we cited two trantition functions:
  - $sign : R \rightarrow \{\top, \bot\}$
      - $f \geq 0 \Rightarrow sign = \top$
      - $f < 0 \Rightarrow sign = \bot$
  - $sigmoid : R \rightarrow R \; = \; \frac 1 {1 + e^{-x}}$

## Learning

For each training case, the perceptron is applied to it and weights are updated proportionally to a learning rate $\eta$ and to the proper error, computed as difference of expected value and obtained one.

## Convergence Theorem

If the dataset is partitionable, then randomly given the initial weights the learning algorithm is able to do that in a finite number of steps.

## Minsky-Papert Theorem

The class of datasets partitionable by a perceptron is limited to the one linearly divisible.

For example $xor$ isn't recognizable by a single perceptron.
