---
title: What are the Eigenvalues & Eigenvectors of $C$ a Circulant Matrix?
comments: true
category: math
tags: DSP, linear algebra
exclude: true 
typora-root-url: ../
---



Each row of $C$ is the same sequence permuted. Specifically, circular shifted in discrete time. Such a matrix is called [circulant](https://courses.physics.illinois.edu/ece401/fa2023/slides/lec23.pdf). In DSP circular convolution of a finite discrete time input signals $\{x_i \}$ with a system with response $\{c_i \}$ is represented as matrix multiplication

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
Where $P$ is the permutation $\big((n-1),(n-2), \cdots,1,0\big)$.
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
From the decomposition of $C$ into a linear composition, we see that their is a 1-to-1 relationship between eigenvalues and eigenvectors of $P$ and $C$.

**Lemma**

The spectrum of $C$ is the same as the permutation $P$.

***proof***  

If $Pv = \lambda v$, thento
$$
\begin{align}
Cv &= c_0Iv + c_1Pv + c_2 P^2v +\cdots + c_{n-1}P^{n-1}v \\
   &= c_0v + c_1\lambda v + c_2 \lambda^2 v +\cdots + c_{n-1}\lambda^{n-1} v \\
   &= \big(c_0 + c_1\lambda + c_2 \lambda^2 +\cdots + c_{n-1}\lambda^{n-1}\big) v \\
\end{align}
$$
And the other way; note that both $C$ and $P$ simultaneously diagonalizable. Suppose $P = A^*DA$, where $D$ is a diagonal matrix. 
$$
\begin{align}
C &= c_0I + c_1P + c_2 P^2 +\cdots + c_{n-1}P^{n-1} \\
   &= c_0I + c_1(A^*DA) + c_2(A^*DA)(A^*DA) +\cdots + c_{n-1}(A^*DA)^{n-1} \\
   &= c_0A^*IA + c_1A^*DA + c_2 A^*D^2A +\cdots + c_{n-1}A^*D^{n-1}A \\
   &= A^*(c_0 I + c_1D + c_2 D^2 +\cdots + c_{n-1}D^{n-1})A \\
\end{align}
$$
Suppose $C = A^*\Lambda A$,
$$
\begin{align}
 \Lambda &=ACA^* \\ 
   &= A (c_0I + c_1P + c_2 P^2 +\cdots + c_{n-1}P^{n-1})A^* \\
   &= c_0AA^* + c_1APA^* + c_2 AP^2A^* +\cdots + c_{n-1}AP^{n-1}A^* \\
   &= c_0I + c_1(APA^*) + c_2(APA^*)(APA^*) +\cdots + c_{n-1}(APA^*)^{n-1} \\
   &= c_0I + c_1 APA^* + c_2 (APA^*)^2 +\cdots + c_{n-1}(APA^*)^{n-1} \\
   &= c_0 I + c_1D + c_2 D^2 +\cdots + c_{n-1}D^{n-1} \\
\end{align}
$$
​																					$\square$



$Cw = \lambda w$, then it is in the span of the $n$ eigenvectors of $P$. 
$$
\begin{align}
\lambda w &= Cw \\
          &= c_0w + c_1Pw + c_2 P^2w +\cdots + c_{n-1}P^{n-1}w \\
\end{align}
$$
 Are $P^iw \perp P^j w $ for all $i \neq j$. 
$$

$$

$$
\begin{align}
(\lambda - c_0)w &= c_1w_1 + c_2 Pw_1 +\cdots + c_{n-1}P^{n-2}w_1 \\
\end{align}
$$


#### Eigenvalues of Permutation $P=\big((n-1),(n-2),\cdots 1,0\big)$

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

The sub-matrices $P_{0,0}$ and $P_{i,n-1}$ are lower triangular and upper triangular, respectively; so their determinants are easy to compute--just multiply the diagonal elements. Continuing the calculation,
$$
\begin{gather}
0 = \det(P - \lambda I) = (-1)^{n}\lambda^n + (-1)^{n-1}\\
\end{gather}
$$
Therefore, any eigenvalue of $P$ satisfies $1 - \lambda^n$= 0, which means the eigenvalues are the roots of unity:
$$
1, \ \omega, \ \omega^2,\ \cdots,\ \omega^{n-1} \text{  where } \omega = e^{i\frac{2\pi}{n}}.
$$

#### Eigenvectors of Permutation $P=\big((n-1),(n-2),\cdots 1,0\big)$

The associated eigenvectors can be solved by determining the null space of $P - \lambda I$.
$$
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
$$

Finally, each eigenvalue, $e^{i\frac{2\pi k}{n}}$, corresponds to a specific eigenvector.

$$
e^{i\frac{2\pi k}{n}} \ \Longleftrightarrow \ 
\begin{bmatrix}
  e^{i\frac{2\pi k(n-1)}{n}} \\
  e^{i\frac{2\pi k(n-2)}{n}} \\
  \vdots \\
   e^{i\frac{2\pi k(2)}{n}}  \\
   e^{i\frac{2\pi k}{n}}  \\
  1 \\
\end{bmatrix}
$$


### References

1. Harvard lecture [notes][1] on the spectral theorem. 
2. MIT lecture [notes][2] on properties of circulant matrices with some python code. 



[1]: https://people.math.harvard.edu/~knill/teaching/math22b2019/handouts/lecture17.pdf
[2]: https://web.mit.edu/18.06/www/Spring17/Circulant-Matrices.pdf

