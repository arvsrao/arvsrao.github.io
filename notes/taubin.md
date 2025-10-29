---
title: Signal Processing Approach to Fair Surface Design by Taubin
comments: true
category: Mesh Processing 
tags: mesh, linear algebra 
typora-root-url: ../
---

The title and word choice are a bit out-of-date. Surface fairing refers to mesh smoothing and denoising. The ansatz of the paper is to cast a given mesh as a signal that can be smoothed with a low-pass filter.

The ansatz is motivated and explained in the 1D case. Curves. A discrete laplacian definition is given without proof or background. 

$$
\Delta x_i = \frac{1}{2}\Big(x_{i+1} - x_{i}\Big) + \frac{1}{2}\Big(x_{i-1} - x_{i}\Big) 
$$

The difference of differences around $x_i$ definition given is an approximation of the second derivative, and when viewing the polygon vertices as a discrete sequence, it is essentially the second finite difference of the sequence $\{x_i\}$,

$$
\begin{align}
\Delta^2 x_i &= x^{i+1} - 2 x_{i} + x^{i-1} \\
             &= \Big(x_{i+1} - x_{i}\Big) + \Big(x_{i-1} - x_{i}\Big) \\
\end{align}
$$


When written as a matrix the Laplacian of the sequence is the circulant matrix, 
$$
K = \frac{1}{2}\begin{bmatrix}
-2 & 1 & 0 & \cdots & 0 & 1\\
1  & -2 & 1 & 0 & \cdots & 0 \\
0 & 1  & \ddots & \ddots & \ddots & \vdots \\
0 & 0 & \ddots & \ddots & 1  & 0  \\
\vdots & \vdots & \ddots & 1 & -2 & 1 \\
1 & 0 & \cdots & 0 & 1  & -2 \\
\end{bmatrix}.
$$

### $\Delta \approx K$ has Real Eigenvalues 

By the Spectral Theorem $K$ can be diagonalized by some real orthogonal matrix, $\Lambda = O K O^T$. Therefore, $K$ has real eigenvalues. Though, orthogonally diagonalizing $K$ is *overkill*. 

Instead, suppose $0 \neq \lambda \in \mathbb{C}$ is an eigenvalue of $K$, for some $v \in \mathbb{C}^n$. Also define the inner product on $\mathbb{C}^n$ to be $v \cdot w := v^T \bar{w}$. The product $Kv \cdot v$ can be computed two different ways:

1. $Kv \cdot v = \lambda v \cdot v = \lambda \|v\|^2$
2. 

$$
\begin{align}
Kv \cdot v &= (Kv)^T\bar{v} \\
           &= v^TK \bar{v} \quad (\text{b/c } K = K^T)\\
           &= v^T \overline{Kv} \\
           &= \bar{\lambda} v^T \bar{v} \\
           &= \bar{\lambda} \|v\|^2 \\
\end{align}
$$

From which one must conclude $\bar{\lambda} = \lambda \ \Longrightarrow \lambda \in \mathbb{R}$.                    								$\Box$

By a similar argument, it can be shown that $v \neq w$ eigenvectors of $K$, which do not span each other, must be **orthogonal**, if they have different eigenvalues. Just compute $Kv \cdot w$ two different ways. Assuming $\lambda_v \neq \lambda_w$ then

1. $Kv \cdot w = \lambda v \cdot w = \lambda_v v \cdot w$
2. 

$$
\begin{align}
Kv \cdot w &= (Kv)^T\bar{w} \\
           &= v^TK \bar{w} \quad (\text{b/c } K = K^T)\\
           &= v^T \overline{Kw} \\
           &= \bar{\lambda_w} v^T \bar{w} \\
           &= \lambda_w v \cdot w \quad (\text{b/c } \lambda \in \mathbb{R})\\\\
\end{align}
$$

Since $\lambda_v \neq \lambda_w \ \Longrightarrow \ v \cdot w = 0$.



### What are the Eigenvalues of $\Delta \approx K$?

Each row of $K$ is the same sequence permuted. Specifically, circular shifted in discrete time. Such a matrix is called [circulant](https://courses.physics.illinois.edu/ece401/fa2023/slides/lec23.pdf). In DSP circular convolution of a finite discrete time input signals $\{x_i \}$ with a system with response $\{c_i \}$ is represented as matrix multiplication


$$
C x = \begin{bmatrix}
c_0 & c_{n-1} & \cdots & c_2 & c_{1}\\
c_1 & c_0     & \cdots & c_3 & c_{2}\\
\vdots & \vdots & \ddots & \vdots & \vdots\\
c_{n-2} & c_{n-3} & \ddots & c_0 & c_{n-1}\\
c_{n-1} & c_{n-2} & \cdots & c_{1} & c_0\\
\end{bmatrix}
\begin{bmatrix}
x_0\\
x_1\\
x_2\\
\vdots\\
x_{n-2}\\
x_{n-1}
\end{bmatrix}\\
$$


When writing out the multiplication the convolution becomes clear
$$
y_k = \sum^{n-1}_{i=0} c_{[(k-i) \mod n]}x_{i}
$$
For example 
$$
\begin{align}
y_1 &= \sum^{n-1}_{i=0} c_{[(1-i) \mod n]}x_{i} \\
    &= c_{[1 \mod n]}x_0 + c_{[0 \mod n]}x_1 + c_{[-1 \mod n]}x_2 + c_{[-2 \mod n]}x_3 + \cdots + c_{[2-n \mod n]}x_{n-1}\\
    &= c_1x_0 + c_0x_1 + c_{n-1}x_2 + c_{n-2}x_2 +\cdots +  c_{2}x_{n-1} \\
\end{align}
$$
Since each row of $C$ is a permutation of $\{c_0, c_1, \cdots, c_{n-1}\}$, $C$ can be written as linear combination of permutation matrices. 
$$
C = c_0I + c_1P + c_2 P^2 +\cdots + c_{n-1}P^{n-1}
$$
Where $P$ is the permutation $(0123\ldots (n-1) 1)$.
$$
P =
\begin{bmatrix}
 e_1 & e_2 & \cdots & e_{n-1} & e_0\\
\end{bmatrix}
=
\begin{bmatrix}
 0 & \cdots & \cdots & 0 & 1\\
 1 & 0 &  & \huge0 & 0\\
  & 1 & \ddots &  & \vdots\\
  & \huge0 & \ddots &\ddots & \vdots \\
  &  & & 1 & 0\\ 
\end{bmatrix}
$$
From the decomposition of $C$ into a linear composition, we see that their is a 1-to-1 relationship between eigenvalues of $P$ and $C$. If $Pv = \lambda v$, then
$$
\begin{align}
Cv &= c_0Iv + c_1Pv + c_2 P^2v +\cdots + c_{n-1}P^{n-1}v \\
   &= c_0v + c_1\lambda v + c_2 \lambda^2 v +\cdots + c_{n-1}\lambda^{n-1} v \\
   &= \big(c_0 + c_1\lambda + c_2 \lambda^2 +\cdots + c_{n-1}\lambda^{n-1}\big) v \\
\end{align}
$$
And the other way; Suppose $Cv = \lambda v$.
$$
\begin{align}
Cv &= c_0Iv + c_1Pv + c_2 P^2v +\cdots + c_{n-1}P^{n-1}v \\
   &= c_0v + c_1\lambda v + c_2 \lambda^2 v +\cdots + c_{n-1}\lambda^{n-1} v \\
   &= \big(c_0 + c_1\lambda + c_2 \lambda^2 +\cdots + c_{n-1}\lambda^{n-1}\big) v \\
\end{align}
$$
To compute the eigenvalues of $P$, solve $\det(P-\lambda I)=0$.
$$
\require{color}
\begin{align}
\det(P - \lambda I) &=
\det\begin{bmatrix}
 -\lambda & \cdots & \cdots & 0 & 1\\
 1 & -\lambda &  & \huge0 & 0\\
  & 1 & \ddots &  & \vdots\\
  & \huge0 & \ddots &\ddots & \vdots \\
  &  & & 1 & -\lambda\\ 
\end{bmatrix}\\
&= -\lambda \det\big(P_{0,0}\big) + (-1)^{n-1}\det\big(P_{0,n-1}\big)\\
&= -\lambda 
\det\begin{bmatrix}
   -\lambda &  & & \huge0 \\
   1 & -\lambda & & \\
    & \ddots &\ddots & \\
   \huge0 & & 1 & -\lambda\\ 
\end{bmatrix}
+ (-1)^{n-1}
\det\begin{bmatrix}
 1      & -\lambda &        & \huge0 \\
        & 1        & \ddots &  \\
        &          & \ddots & -\lambda \\
 \huge0 &          &        & 1 \\ 
\end{bmatrix}\\
\end{align}
$$

The sub-matrices $P_{0,0}$ and $P_{i,n-1}$ are lower triangular and upper triangular, respectively; so their determinants easy to compute--just multiply the diagonal elements. Continuing the calculation,
$$
\begin{gather}
0 = \det(P - \lambda I) = (-1)^{n}\lambda^n + (-1)^{n-1}\\
\end{gather}
$$
Therefore any eigenvalue of $P$ satisfies $1 - \lambda^n$= 0, which means the eigenvalues are the roots of unity:
$$
1, \ \omega, \ \omega^2,\ \cdots,\ \omega^{n-1} \text{  where } \omega = e^{i\frac{2\pi}{n}}.
$$

The associated eigenvectors can be solved by determining the null space of $P - \lambda I$.

\[
\begin{align}
(P - \lambda I) v
&=
\begin{bmatrix}
-\lambda &        &       &  && 1\\
1       & -\lambda &      & \Huge0  &  &  \\
       &     1   &  -\lambda     & & &  \\
  &        & \ddots      & \ddots&  &  \\
  &     \Huge0   &   &   \ddots  & \ddots &  \\
  &    &       &  &  1 & -\lambda \\
\end{bmatrix}
\begin{bmatrix}
  \lambda^{n-1} \\
  \lambda^{n-2} \\
  \vdots \\
  \lambda^2  \\
  \lambda  \\
  1 \\
\end{bmatrix}
&=
\begin{bmatrix}
  1 - \cancelto{1}{\lambda^{n}} \\
  \lambda^{n-1} - \lambda^{n-1}  \\
  \vdots \\
  \lambda^{3} - \lambda^{3} \\
  \lambda^{2} - \lambda^{2}  \\
  \lambda - \lambda \\
\end{bmatrix}\\
&= \vec{0}
\end{align}
\]

Finally, each eigenvalue, $e^{i\frac{2\pi k}{n}}$, corresponds to a specific eigenvector.

\[
e^{i\frac{2\pi k}{n}} \ \Longleftrightarrow \ 
\begin{bmatrix}
  e^{i\frac{2\pi k(n-1)}{n}} \\
  e^{i\frac{2\pi k(n-2)}{n}} \\
  \vdots \\
   e^{i\frac{2\pi k(2)}{n}}  \\
   e^{i\frac{2\pi k}{n}}  \\
  1 \\
\end{bmatrix}
\]








