---
layout: post
title: Area Forms & Normals
comments: true
category: mathematics
tags: mathematics, vector calculus
---

To compute the area form of $S^3$, I used a general *formula* for $S^n \subset \mathbb{R}^{n+1}$ that I found in Lee's *Introduction to Smooth Manifolds*.

$$
\begin{equation*}
	\Omega = \sum_{i=1}^{n+1} (-1)^{i+1} x_{i} dx_0 \wedge \cdots \wedge \widehat{dx_{i}} \wedge \cdots \wedge dx_{n}
\end{equation*}
$$

is the area form of $S^n$, in terms of its coordinate functions. While trying to understand this formula, I was reminded of the cross product formula, which is an alternating sum of determinants. Well, sure, alternating forms like $$ \Gamma_i = dx_1 \wedge \cdots \wedge \widehat{dx_{i}} \wedge \cdots \wedge dx_{n+1} $$ are really determinants in disguise. Suppose $v_1, \ldots,v_n$ are tangent vectors at some point on $S^n$. Individually, 1-forms $dx_{j}(v)$ are linear functionals and act on tangent vectors $v \in T_{p}S^n$. Essentially, $dx_{j}(v_k )$ is portion of the derivative $Dx_j$ in the $v_k$ direction; the directional derivative. Alternatively, it is the action of $v_k$ on coordinate $x_j$. I summarize these two descriptions below.  <!--more-->

$$
\begin{align*}
	dx_{j}(v_k) &= v_k \star x_j = v_k \cdot Dx_j
\end{align*}
$$

The **action** of a vector on a function is denoted $\star$. Also here $v \in T_p S^n$ and $Dx_j$ are **n**-dimensional vectors. Implicitly, coordinates $x_i$ are functions of some local parameters $\theta_1, \cdots, \theta_n$. $n$ corresponds to the dimensionality of $S^n$. Then explicitly, 

$$
\begin{gather*}
	v = \sum_{k=1}^{n} c_k \frac{\partial}{\partial \theta_k} \in T_p S^n,
\end{gather*}
$$

and $Dx_j$ is just a row in the derivative of $x$, $Dx : T_pS^n \rightarrow T_q\mathbb{R}^{n+1}$. In matrix form

$$
Dx = 
\begin{pmatrix}
    \frac{\partial x_1}{\partial \theta_1} & \frac{\partial x_1}{\partial \theta_2}  & \cdots & \frac{\partial x_1}{\partial \theta_n} \\
   		                         \vdots    &                              \vdots     & \ddots &   \vdots \\
    \frac{\partial x_{n+1}}{\partial \theta_1} & \frac{\partial x_{n+1}}{\partial \theta_2} & \cdots & \frac{\partial x_{n+1}}{\partial \theta_n} \\
\end{pmatrix}.
$$

Since $\{x_i\}$ are coordinates, $Dx$ is full rank; furthermore $Dx$ an embeds $T_pS^n \subset T_q\mathbb{R}^{n+1}$.

As an $n$-form evaluated on $v_1, \ldots, v_n$

$$
\begin{equation*}
\Gamma_i(v_1, \ldots,v_n) = \frac{1}{n!}\det\Big(\Big[v_k \star x_j\Big]_{j \neq i}\Big). \\
\end{equation*}
$$

Continuing by substituting $\Gamma_i$ into the formula for $\Omega$ yields

$$
\begin{align*}
\Omega(v_1, \ldots,v_n) &= \sum_{i=1}^{n+1} (-1)^{i+1} x_{i} \Gamma_i(v_1, \ldots,v_n) \\
                        &= \sum_{i=1}^{n+1} (-1)^{i+1} x_{i} \frac{1}{n!}\det\Big(\Big[v_k \cdot Dx_j\Big]_{j \neq i}\Big). \\
\end{align*}
$$

The last expression is exactly the [recursive formula for the determinant][1] of a yet larger matrix that contains all the $v_k \cdot Dx_j$ and $x_i$ terms.

$$
\begin{align*}
\Omega(v_1, \ldots,v_n) &= \frac{1}{n!} \det
\begin{pmatrix}
           x_1  & x_2 & \cdots & x_{n+1} \\
           v_1 \star x_1 & v_1 \star x_1 & \cdots & v_1 \star x_{n+1} \\
   		      \vdots     &    \vdots     & \ddots &   \vdots \\
   		   v_n \star x_1 & v_n \star x_1 & \cdots & v_n \star x_{n+1}  \\
\end{pmatrix} \\
&= \frac{1}{n!} \det
\begin{pmatrix}
   x_1 \ x_2 \ \cdots x_{n+1} \\
    \begin{bmatrix}
		v_1 \\
		v_2 \\
		\vdots \\
		v_n \\
	\end{bmatrix}
	\begin{bmatrix}
		Dx_1 & Dx_2  & \ldots & Dx_{n+1} \\
	\end{bmatrix}
\end{pmatrix}
\end{align*}
$$

The final $n+1 \times n+1$ matrix description above I think shows more clearly that the rows are $n+1$ vectors, $$\{\tilde{v_1},\  \tilde{v_2}, \cdots, \tilde{v_n}, \ x \}$$, where the $\tilde{v_k} = Dx \cdot v_k$ represent $T_pS^n$ as a co-dimension $1$ plane/subspace of $T_q\mathbb{R}^{n+1}$. To be a proper area-form $\Omega_p(\tilde{v_1},\  \tilde{v_2}, \cdots, \tilde{v_n})$ must always be positive, which, in particular means 

$$
\Omega_p(\tilde{v_1},\  \tilde{v_2}, \ldots, \tilde{v_n}) = \frac{1}{n!} \det
	\begin{bmatrix}
   		   x \\
		\tilde{v_1} \\
		\tilde{v_2} \\
		\vdots \\
		\tilde{v_n} \\
	\end{bmatrix}
> 0.
$$

For clarity I have written $\Omega$ as a form on a subspace $V^n \subset \mathbb{R}^{n+1}$. The $\det > 0$ condition implies that $$\{\tilde{v_1},\  \tilde{v_2}, \cdots, \tilde{v_n}, \ x \}$$ are mutually independent. Great! This $\det > 0$ condition forces $x$ to at least have a normal component. Though it's easy to see that $x$ is orthogonal to $T_pS^n$; I prove this in an appendix at the end of this post. However, the cross product makes this connection between the normal of $T_pS^n$ and $\Omega$ explicit.


## Cross Products

I mentioned the cross product formula above because in computing a determinant one can also compute a normal vector. Lets review. Take a distinguished vector $a \in \mathbb{R}^{n+1}$, and vectors $v_1, v_2, \cdots, v_n$ which form a basis of $V^n \subset \mathbb{R}^{n+1}$, a codimension $1$ subspace/plane. So basically the situation we have above for tangent spaces of $S^n$. Arranging these vectors into a matrix we can relate the determinant of the matrix to the inner product of $a$ and a special vector that is only dependent on the $\lbrace v_k\rbrace$. 

$$
\begin{align*}
	\det
	\begin{bmatrix}
		a \\
		v_1 \\
		v_2 \\
		\vdots \\
		v_n 
	\end{bmatrix}
	& = \sum^{n+1}_{i=1}a_i (-1)^{i+1}M_{1,i} = \langle a, \eta \rangle,\\
\end{align*}
$$

where $\eta = \( M_{1,1}, \ -M_{1,2}, \cdots, (-1)^{n+1}M_{1,n+1}\)$. The $M_{1,i}$ are [called $(1,i)$-minors][2], they are determinants of submatrices, which only involve terms from the $v_k$. Okay so we've converted a determinant ( or rather rewritten ) it as an inner product which is very helpful. Simply take $a = v_k$; then vectors $v_k, v_1, v_2, \cdots, v_n$ are no longer mutually independent and 

$$
\begin{align*}
0 =
	\det
	\begin{bmatrix}
		v_k \\
		v_1 \\
		v_2 \\
		\vdots \\
		v_n 
	\end{bmatrix}
	& = \sum^{n+1}_{i=1}a_i (-1)^{i+1}M_{1,i} = \langle v_k, \eta \rangle \\
\end{align*}
$$

Boom!! $\langle v, \eta \rangle = 0$ for any $v \in V^n \$. $\eta$ is the normal we seek--the cross product. With this in mind, lets return to $\Omega$ by noting that $\Omega$ evaluated on $V^n \subset \mathbb{R}^{n+1}$ has the same expression as the left hand side of the equation above that relates $V^n$ to the cross product; therefore

$$
\begin{align*}
\Omega_p(\tilde{v_1},\  \tilde{v_2}, \ldots, \tilde{v_n}) = \frac{1}{n!} \det
	\begin{bmatrix}
   		   x \\
		\tilde{v_1} \\
		\tilde{v_2} \\
		\vdots \\
		\tilde{v_n} \\
	\end{bmatrix}
	&= \frac{1}{n!} \langle x, \eta \rangle > 0
\end{align*}
$$.

$x$ must have a positive normal component--which we knew. I think it's clearer from the above expression that $\eta$ and the $\Omega$ are *dual*. For me, this duality reinforces the picture of $\Omega$ as a density, and its relationship with $\eta$ gives a way to graph this density in the ambient space. 

## Appendix: Computing the Normal to $S^n$

To make things easy take coordinates $x = \(x_1, x_2, \ldots, x_n, \sqrt{1 - r^2} \)$ where $r^2 = x^2_1 + x^2_2 + \cdots + x^2_n$. The cross product formula for these coordinates yields the normal $\eta = (\eta_i)$ where 

$$
\eta_i = (-1)^{i+1}\det
\begin{bmatrix}
     -     & -     & \cdots &     -         & \cdots & - & - \\
	1      & 0      & \cdots &   \bf{0}     & \cdots &     0 & -\frac{x_1}{x_{n+1}} \\
	0      & 1      & \cdots &   \bf{0}     & \cdots &     0 & -\frac{x_2}{x_{n+1}} \\
	\vdots & \vdots & \ddots &  \bf{\vdots} & \ddots &     0 & \vdots \\
		0      & 0      & \cdots &   \bf{1}     & \cdots &     0 & -\frac{x_i}{x_{n+1}} \\
	\vdots & \vdots & \ddots &  \bf{\vdots} & \ddots &     0 & \vdots \\
	0      & 0      & \cdots & \underbrace{\bf{0}}_{\bf{i-th\ column}}       &    \cdots &     1 & -\frac{x_n}{x_{n+1}} \\
\end{bmatrix}.
$$

Hopefully it's clear the matrix above, let's call it $A_i$, is $n \times n$. The $i$-th column and first row are distinguished because they are *missing*. When $i \leq n$ it's easier to compute the determinant of $A_i$ if the $i$-th row and first row are swapped, by say permutation $P_{1i}$. The bulk of 

$$
P_{1i} A_i = 
\begin{bmatrix}
    0      & 0      & \cdots &   0    & 0    & \cdots &     0 & -\frac{x_i}{x_{n+1}} \\
	1      & 0      & \cdots &   0     & 0     & \cdots &     0 & -\frac{x_1}{x_{n+1}} \\
	0      & 1      & \cdots &   0    & 0    & \cdots &     0 & -\frac{x_2}{x_{n+1}} \\
	\vdots & \vdots & \ddots &  \vdots &  \vdots & \ddots &     0 & \vdots \\
	0      & 0      & \cdots &   1    & 0    & \cdots &     0 & -\frac{x_{i-1}}{x_{n+1}} \\
	0      & 0      & \cdots &   0    & 1    & \cdots &     0 & -\frac{x_{i+1}}{x_{n+1}} \\
	\vdots & \vdots & \ddots &  \vdots & \vdots & \ddots &     0 & \vdots \\
	0      & 0      & \cdots &  0      & 0      &    \cdots &     1 & -\frac{x_n}{x_{n+1}} \\
\end{bmatrix}
$$

is an $n-1 \times n-1$ identity matrix, in the lower left. Which makes our life easy. Knowing $\det(P_{1i}) = \det(P_{1i}^T) = (-1)^{i+1}$ and using the [recursive formula for the determinant][1], 

$$
\begin{align*}
	\det(P_{1i} A_i) = (-1)^{n}\frac{x_i}{x_{n+1}} & \Longrightarrow \det(A_i) = (-1)^{i+1}(-1)^{n}\frac{x_i}{x_{n+1}} \\
	                                               & \Longrightarrow \eta_i = (-1)^{i+1}(-1)^{i+1}(-1)^{n}\frac{x_i}{x_{n+1}} \\
\end{align*}
$$

for $i \leq n$ and $\eta_{n+1} = (-1)^n$. 

$$
	\eta = \Big((-1)^n \frac{x_1}{x^{n+1}}, \cdots ,(-1)^n \frac{x_n}{x^{n+1}}, (-1)^n\Big)
$$ 

looks like it's in homogeneous coordinates. Anyway, it's easy to see that $x = (-1)^n x_{n+1} \eta$. I wonder why for these coordinates the orientation of $\eta$, the normal, alternates depending on the parity of dimension.  

[1]: https://en.wikipedia.org/wiki/Laplace_expansion
[2]: https://en.wikipedia.org/wiki/Minor_(linear_algebra)