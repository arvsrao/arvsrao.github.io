---
title: Reading Petersen's Riemannian Geometry
comments: true
category: math
tags: differential geometry
exclude: true
typora-root-url: ../
---



## When is $X=\nabla f$ ?

Let $(M^n,g)$ be a $n$ dimensional real Riemannian manifold and $\theta \in TM^{\ast}$ be a 1-form. 



<strong>Definition. </strong> <u>Closed Forms</u>

We say $\theta$ is **closed** if $d\theta = 0$ a.e.



<strong>Definition. </strong> <u>Path Independence</u>

Let $p, q$ $\in M^n$ be any two points. Denote all simple curves between $p$  and $q$ by 


$$
\Omega_{pq} = \{ \alpha: I \longrightarrow M  \ \Big| \ \alpha(0) = p \text{ and } \alpha(1) = q \}.
$$


Then we say a 1-form  $\theta \in TM^{\ast}$ is *path independent* if


$$
\alpha \longmapsto \int_{\alpha}\theta = c_{pq}, \text{ some constant}, \ \forall \alpha \in \Omega_{pq}.
$$





<a name="closed-form-lemma"></a>

<strong>Lemma. $\theta$ Path Independence and Closure Equivalence.</strong>


The follow three statements are equivalent.

​	(A) $\theta$ is **closed**.

​	(B) for all simple closed curves $\gamma \subset M^n$,  


$$
\gamma \longmapsto \int_{\gamma}\theta = 0.
$$

​        (C) $\theta$ is path independent.

<em>proof:</em>

($A \Longrightarrow B$ ) Let $\gamma \subset M$ be a simple closed curve. By Stokes theorem,


$$
0 = \int_{A} d\theta  = \int_{\gamma}\theta,  \quad \text{where }A\text{ is the region bounded by }\gamma.
$$


($B \Longrightarrow C$) Let $\gamma \subset M$ be a simple closed curve. Any closed curve $\gamma$ can be factored into the path product of curves, like $\gamma = \alpha * -\beta$. Here $\alpha$ and $\beta$ are paths between any two points $p, q$ $\in \gamma$. The minus sign in front of $\beta$ simply denotes path $\beta$ parametrized with the opposite orientation, e.g. $-\beta = \beta(-t)$. 

![](/notes/assets/path-independence/paths.png)

Let $p, q \in \gamma$ and $\alpha, \beta \in \Omega_{pq}$ be simple curves. Then $\gamma = \alpha * -\beta$. Since


$$
\begin{align}
0 &= \int_{\gamma}\theta  = \int_{\alpha * -\beta}\theta = \int_{\alpha}\theta - \int_{\beta}\theta \quad \Longrightarrow \quad 
  \int_{\alpha}\theta = \int_{\beta}\theta = c_{pq}.
\end{align}
$$


$(C \Longrightarrow A)$ $\theta$ is path independent implies


$$
\begin{align} 
\int_{\alpha}\theta = \int_{\beta}\theta = c_{pq} &\quad \Longrightarrow \quad 0 = \int_{\alpha}\theta - \int_{\beta}\theta \\
&\quad \Longrightarrow \quad  0 = \int_{\alpha *-\beta}\theta \\
&\quad \Longrightarrow \quad  0 = \int_{\gamma}\theta \ .
\end{align}
$$


By Stokes Theorem,


$$
0= \int_{\gamma}\theta = \int_{A} d\theta, \quad \text{where }A\text{ is the region bounded by }\gamma.
$$


Since $A$ is arbitrary, $d\theta = 0$ almost everywhere.

<div style="text-align: right"> <span style='font-size:20px;'>&#9634;</span> </div> 



In Petersen's Riemannian Geometry, towards motivating the connection he states but does not prove the following.



<a name="converse-grad-thm"></a>

<strong>Lemma. $X = \nabla f$  if $\theta_X$ is Closed. </strong>


If $\theta \in TM^{\ast}$ is closed, then there is a function $f: M \longrightarrow \mathbb{R}$ whose gradient, $\nabla f$, generates $\theta$.

<p><em>proof:</em></p>

$\theta = g(X, \cdot)$ for some vector field $X$. By the [previous lemma](#closed-form-lemma), path independence applies as much to $\theta$ as is it does to $X$. In particular, for any fixed $p \in M$ any $\alpha \in \Omega_{px}$ the function


$$
\begin{align} 
f(x) = c_{px} = \int_{\alpha}\theta & = \int_{\alpha} \langle X, d\alpha \rangle_g, \\
\end{align}
$$


is well defined. Compute the directional derivative of $f$. 


$$
\begin{align}
\langle \nabla f, v \rangle & = \lim_{t \rightarrow 0} \frac{f(\gamma(t)) - f(x)}{t} \\
                 & = \lim_{t \rightarrow 0} \frac{1}{t} \Bigg(\int_{\beta_t} \langle X, d\beta_t \rangle_g - \int_{\alpha} \langle X, d\alpha \rangle_g\Bigg) \\
\end{align}
$$


Here $\gamma(0) = x$ and $\dot\gamma(0) = v$.



![](/notes/assets/path-independence/converse.png)



Because $X$ is path independent


$$
\lim_{t \rightarrow 0} \frac{1}{t} \Bigg(\int_{\beta_t} \langle X, d\beta_t \rangle_g - \int_{\alpha} \langle X, d\alpha \rangle_g\Bigg) 
                  = \lim_{t \rightarrow 0} \frac{1}{t}\int_{\gamma} \langle X, d\gamma \rangle_g \\
$$


Then computing the directional derivative boils down to


$$
\begin{align}
\langle \nabla f, v \rangle_g & = \lim_{t \rightarrow 0} \frac{1}{t}\int_{\gamma} \langle X, d\gamma \rangle_g \\
\end{align}.
$$


Define the antiderivative


$$
\begin{align}
F(s) = \int_{-\epsilon}^{s} \langle X \circ \gamma, d\gamma \rangle_g\\
\end{align}.
$$


Then the limit in $t$ looks like $F^{\prime}(0)$.


$$
\begin{align}
\lim_{t \rightarrow 0} \frac{1}{t}\int_{0}^{t} \langle X \circ \gamma, d\gamma \rangle_g &= \lim_{t \rightarrow 0} \frac{F(t) - F(0)}{t} = F^{\prime}(0)\\
\end{align}.
$$


This is some version of fundamental theorem of calculus.


$$
\begin{align}
\frac{dF}{dt}\Bigg|_{t=0} &= \frac{d}{dt}\int_{0}^{t} \langle X \circ \gamma, d\gamma \rangle_g \Bigg|_{s=0} \\
&= \langle X \circ \gamma(0), \dot\gamma(0) \rangle_g \\
&= \langle X(x), v \rangle_g
\end{align}.
$$


Therefore at $x \in M$, $\langle \nabla f, v \rangle_g = \langle X(x), v \rangle_g$. For reference, see a [proof][1] of the lemma in euclidean space.

<div style="text-align: right"> <span style='font-size:20px;'>&#9634;</span> </div> 



[1]: https://en.wikipedia.org/wiki/Gradient_theorem
