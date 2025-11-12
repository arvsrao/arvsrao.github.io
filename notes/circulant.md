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
For example,


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

The spectrum of $C$ is the same as permutation $P$. Moreover, they are simultaneously diagonalizable.

***proof***  

First note that $CP = PC$, which follows from $C$s representation as a linear combination of permutation matrices.


$$
\begin{align}
CP &= c_0IP + c_1P^2 + c_2 P^2 +\cdots + c_{n-1}P^{n} \\
   &= P\big(c_0I + c_1P + c_2 P^2 +\cdots + c_{n-1}P^{n-1}\big) \\
   &= PC \\
\end{align}
$$


Suppose $Pv = \lambda v$, then 


$$
PCv = CPv = C\lambda v \quad \Longrightarrow \quad P\underbrace{Cv}{} = \lambda \underbrace{Cv}{}. 
$$


Which means that $Cv$ and $v$ are both eigenvectors of $P$ corresponding to the same eigenvalue, $\lambda$. In the next section we learn that $P$ has $n$ distinct eigenvalues, implying that $Cv$ is a multiple of $v$. Specifically, there is $\exists \alpha$ s.t. $Cv = \alpha v$. Therefore, 

1. $C$ and $P$ have the same eigenvectors.
2. If $A^{-1}PA$ is a diagonal matrix, for some matrix $A$, then $A$ also diagonalizes $C$.

<div style="text-align: right"> <span style='font-size:20px;'>&#9634;</span> </div>

​                                                                                                                                                                           


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

### Eigenvalues of $C$

Because $C$ can be written as linear combination of permutation matrices, its eigenvalues are of the form


$$
\begin{equation}
\lambda_C = c_0 + c_1 \lambda_P + c_2 \lambda_P^2 +\cdots + c_{n-1}\lambda_P^{n-1} \\
\end{equation}
$$


where $\lambda_P = e^{i\frac{2\pi k}{n}}$  is an eigenvalue of $P$. Substituting further,


$$
\begin{equation}
\lambda_C = c_0 + c_1 e^{i\frac{2\pi k}{n}} + c_2 e^{i\frac{4\pi k}{n}} +\cdots + c_{n-1}e^{i\frac{2\pi k(n-1)}{n}} \\
\end{equation}
$$




### References

1. Harvard lecture [notes][1] on the spectral theorem. 
2. MIT lecture [notes][2] on properties of circulant matrices with some python code. 



[1]: https://people.math.harvard.edu/~knill/teaching/math22b2019/handouts/lecture17.pdf
[2]: https://web.mit.edu/18.06/www/Spring17/Circulant-Matrices.pdf

