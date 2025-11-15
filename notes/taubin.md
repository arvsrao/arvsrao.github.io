---
title: Signal Processing Approach to Fair Surface Design by Taubin
comments: true
category: Mesh Processing 
tags: mesh, linear algebra 
exclude: true
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
K = -\frac{1}{2}\begin{bmatrix}
-2 & 1 & 0 & \cdots & 0 & 1\\
1  & -2 & 1 & 0 & \cdots & 0 \\
0 & 1  & \ddots & \ddots & \ddots & \vdots \\
0 & 0 & \ddots & \ddots & 1  & 0  \\
\vdots & \vdots & \ddots & 1 & -2 & 1 \\
1 & 0 & \cdots & 0 & 1  & -2 \\
\end{bmatrix}.
$$

<a name="eigenvalues"></a>

### $\Delta \approx K$ has Real Eigenvalues 

By the Spectral Theorem $K$ symmetric implies that it can be diagonalized by some real orthogonal matrix, $\Lambda = O K O^T$. Therefore, $K$ has real eigenvalues. Though, orthogonally diagonalizing $K$ is *overkill*. 

*Alternate proof*:

Suppose $0 \neq \lambda \in \mathbb{C}$ is an eigenvalue of $K$, for some $v \in \mathbb{C}^n$. Also define the inner product on $\mathbb{C}^n$ to be $v \cdot w := v^T \bar{w}$. The product $Kv \cdot v$ can be computed two different ways:

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

Then, one must conclude $\bar{\lambda} = \lambda \ \Longrightarrow \lambda \in \mathbb{R}$.                    								$\Box$

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

Eigenvectors of $K$ belonging to the same eigenspace are also orthogonal. For a proof checkout these [notes][1].

<div style="text-align: right"> <span style='font-size:20px;'>&#9634;</span> </div>

### The Eigenvalues of $\Delta \approx K$ 

$K$ is a circulant matrix so we can calculate eigenvalues. In my [notes on circulant matrices][2], I did just that. In general the eigenvalues have the following form.


$$
\begin{equation}
\lambda_C = c_0 + c_1 e^{i\frac{2\pi k}{n}} + c_2 e^{i\frac{4\pi k}{n}} +\cdots + c_{n-1}e^{i\frac{2\pi k(n-1)}{n}}
\end{equation}
$$
For $\Delta \approx K$, all coefficients $c_i$ are zero except for $c_0 = -2$, $c_1 = 1$, and $c_{n-1} = 1$. Substituting those specific coefficients into the eigenvalue formula and simplifying gives,


$$
\begin{align}
\lambda_k &= -2 + e^{i\frac{2\pi k}{n}} + e^{i\frac{2\pi k(n-1)}{n}} \\
&= -2 + e^{i\frac{2\pi k}{n}} + \cancelto{1}{e^{i2\pi k}} + e^{-i\frac{2\pi k}{n}} \\
&= -1 + 2\cos\big(\frac{2\pi k}{n}\big)

\end{align}
$$

Based on the [previous](#eigenvalues) section, we expected the eigenvalues of $K$ to be real, and they are indeed real.






[1]: https://people.math.harvard.edu/~knill/teaching/math22b2019/handouts/lecture17.pdf
[2]: ../circulant/











