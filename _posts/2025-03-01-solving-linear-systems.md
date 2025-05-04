---
title: Solving Overdetermined Linear Systems
layout: post
comments: true
category: mathematics 
tags: computer graphics, linear algebra
typora-root-url: ../
---

An overdetermined linear system is a linear system of $n$ equations in $m$ unknowns, where $n > m$. 

$$
\begin{align*}
  a_{11}x_{1} + a_{12}x_{2} + \cdots + a_{1m}x_{m} &= y_1 \\
  a_{21}x_{2} + a_{22}x_{2} + \cdots + a_{2m}x_{m} &= y_2 \\
  \vdots   \hspace{2.5cm} &= \vdots \\
  a_{n1}x_{2} + a_{n2}x_{2} + \cdots + a_{nm}x_{m} &= y_n \\
\end{align*}
$$

<!--more-->

The unknowns are $x_{i} \in X$ and the range / observation values are $y_{j} \in Y$. The system can be represented compactly in matrix form as $ A \vec{x} = \vec{y} $. Where $A: X \to Y$ is a linear map defined as $A = [a_{ij}]$.

### No Solution but We Still Want a Solution

<figure>
<div align="center">
  <img src = "/assets/overdetermined-systems/sympy-figure2.png">
</div>
<figcaption> Figure #1. Overdetermined system with a solution. </figcaption>
</figure>

Overdetermined linear systems are usually not solvable, because among the $n$ equations (**NOT** the rows of $A$) it is most likely that there is no subset of $m$ independent equations which spans/explains all the remaining $n-m$ equations. Only in the rare circumstance where there is a set of $m$ independent equations spanning the remaining $n-m$ equations can the system be solved. An example of such a system would be

$$
\begin{align*}
   x - y &= 0 \\
   x + y &= 0 \\
  2x - y &= 0. \\
\end{align*}
$$

This system is pictured above in Figure #1. Any two equations of the system explain the other. For example the third equation can be eliminated because $\rho_3 = \frac{1}{2}(3\rho_1 + \rho_2)$. Leaving a system of two independent equations in two unknowns, which is solvable. 

More common are systems like the one listed and pictured below.

$$
\begin{align*}
   x - y &= 0 \\
   x + y &= 0 \\
       y &= 1. \\
\end{align*}
$$

<figure>
<div align="center">
  <img src = "/assets/overdetermined-systems/sympy-figure1.png">
</div>
<figcaption> Figure #2. Overdetermined system without a solution. </figcaption>
</figure>
**See [gist][1] for code to generate the figures.**

Unlike the solvable system all the three equations (**NOT** the rows of the matrix representing the LHS) are independent. No two equations spans the other. 

Expecting a solution or what I will call a *strict solution* is too much to hope for. However, for many applications a solution is wanted and needed. So what to do? Well, the definition of equality can be weaken to minimizing the distance the between $y \in Y$ and $Ax$,

$$
  \min_{x \in X}{\left\lVert A x - y \right\rVert}.
$$

The singular value decomposition ([SVD][svd]) of $A$ will allow us to express the minimizer in closed form.

### SVD

Decomposing $A$ using [SVD][svd] we get 

$$
A = U\Sigma V^{*}.
$$

Where both $U$ and $V$ are unitary matrices and $dim(U) = n \times n$, $dim(\Sigma) = n \times m$, and $dim(V) = m \times m$. Because $rank(a) = \rho \leq m$, $\Sigma$ has the general form

$$
\left[
\begin{array}{cccc|c}
\sigma_1 &          &          &               &         \\
         & \sigma_2 &          & \huge0        &         \\
         &          & \ddots   &               &  \huge0 \\
         & \huge0   &          & \sigma_{\rho} &         \\
         &          &          &               &         \\
         \hline
         &          & \huge0   &               &  \huge0 \\
\end{array}
\right]
$$


The solution $\vec{x} \in X$ is where $\min_{\vec{x} \in X} \left\lVert A \vec{x} - \vec{y} \right\rVert$. Substituting $A = U\Sigma V^{*}$ into
the minimization we get a new minimization in terms of $\Sigma$.

$$
\begin{align*}
\left\lVert A \vec{x} - \vec{y} \right\rVert &= \left\lVert U\Sigma V^{*} \vec{x} - \vec{y} \right\rVert \\
 &= \left\lVert U(\Sigma V^{*} \vec{x} - U^{*}\vec{y}) \right\rVert \\
 &= \cancelto{1}{\left\lVert U \right\rVert} \left\lVert \Sigma V^{*} \vec{x} - U^{*}\vec{y} \right\rVert .\\
\end{align*}
$$

Now, the original minimization problem is equivalent to

$$
  \min_{\tilde{x} \in X}{\left\lVert \Sigma \tilde{x} - \tilde{y} \right\rVert}
$$

where $$\tilde{x} = V^{*} \vec{x}$$ and $$\tilde{y} = U^{*} \vec{y}$$. As a system of linear equations $\Sigma \tilde{x} = \tilde{y}$ is

$$
\begin{align*}
  \sigma_{1}\tilde{x}_{1}        &= \tilde{y}_1 \\
  \sigma_{2}\tilde{x}_{2}        &= \tilde{y}_2 \\
  \vdots &= \vdots \\
  \sigma_{\rho}\tilde{x}_{\rho}  &= \tilde{y}_{\rho} \\
  0                              &= \tilde{y}_{\rho + 1} \\
  \vdots                         &= \vdots \\
  0                              &= \tilde{y}_{n} .\\
\end{align*}
$$

Clearly the system is inconsistent, but solving for $\tilde{x}_{i}$ up to $\rho$ and setting the remaining coordinates to zero gives a potential minimum/solution. 

$$
\tilde{x}_{i} = 
\begin{cases} 
  \frac{1}{\sigma_{i}} \tilde{y}_i & i \leq \rho \\
          0 &  \rho < i \leq m \\
\end{cases}
$$

In matrix form the solution is $\Sigma^{+}\tilde{y}$, where

$$
\Sigma^{+} = 
\left[
\begin{array}{cccc|c}
\frac{1}{\sigma_{1}}&                      &          &               &         \\
         & \frac{1}{\sigma_{2}} &          & \huge0        &         \\
         &                      & \ddots   &               &  \huge0 \\
         & \huge0               &          & \frac{1}{\sigma_{\rho}} &         \\
         &                      &          &               &         \\
         \hline
         &                      & \huge0   &               &  \huge0 \\
\end{array}
\right]
$$

The norm to be minimized has a lower bound purely in last $n - \rho$ coordinates of $\tilde{y}$.

$$
\begin{equation*}
\left\lVert \Sigma \tilde{x} - \tilde{y} \right\rVert^2 = \sum^{\rho}_{i=1} \Big(\sigma_{i}\tilde{x}_{i} - \tilde{y}_i\Big)^2 + \sum^{n}_{i=\rho + 1} \Big(0 - \tilde{y}_i\Big)^2 \geq 
\left\lVert (\tilde{y}_{\rho + 1}, \tilde{y}_{\rho + 2}, \cdots, \tilde{y}_n)\right\rVert^2 
\\
\end{equation*}
$$

Substituting in the proposed solution makes the first summand zero and
the norm difference reaches the lower bound.

$$
\begin{gather*}
\left\lVert \Sigma \tilde{x} - \tilde{y} \right\rVert^2 = \cancelto{0}{\sum^{\rho}_{i=1} \Big(\sigma_{i} (\frac{1}{\sigma_{i}} \tilde{y}_i)  - \tilde{y}_i\Big)^2} + \sum^{n}_{i=\rho + 1} \Big(0 - \tilde{y}_i\Big)^2
\ \Longrightarrow \\
\left\lVert \Sigma \tilde{x} - \tilde{y} \right\rVert^2 = 
\left\lVert (\tilde{y}_{\rho + 1}, \tilde{y}_{\rho + 2}, \cdots, \tilde{y}_n)\right\rVert^2 
\\
\end{gather*}
$$

Therefore the mimimum is achieved at the proposed solution 

$$
\tilde{x}_{i} = 
\begin{cases} 
  \frac{1}{\sigma_{i}} \tilde{y}_i & i \leq \rho \\
          0 &  \rho < i \leq m \\
\end{cases}
$$

### Summary

The *solution* of a general overdetermined system $Ax = y$ is $x = V\Sigma^{+} U^{*}y$.


[1]: https://gist.github.com/arvsrao/11c3dfae9e301de0cee8ac63a43c45b3
[svd]: https://en.wikipedia.org/wiki/Singular_value_decomposition

