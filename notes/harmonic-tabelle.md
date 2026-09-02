---
title: Structure and Properties of Homogenous Polynomial Space $\mathcal{P}_d$
comments: true
category: math 
tags:  
exclude: true
typora-root-url: ../
---

Harmonic homogenous polynomials $\mathcal{H}_d \subseteq \mathcal{P}_d$ are a subspace under addition of degree $d$ homogenous polynomials.

### Lets Count!

$\mathcal{P}_d$ is the span of monomials $\lbrace x^{a}y^{b}z^{c} \ \Big\| \ d = a + b + c \rbrace$. How many basis elements are there? The equation $d = a + b + c$  sweeps out a triangle in the positive octant. Below is a scatter plot of the non-negative integer coordinates that sum to $$3$$.

![degree](/notes/assets/coords-sum-to-degree.png)

The degree $3$ scatter plot shows an equilateral triangle with side length $4$, and a total of $10$ coordinates; therefore $\dim(\mathcal{P}_3)= 10$. In general, the non-negative integer coordinates degree $d$ sweep out a triangle with side length  $d+1$ in the positive octant. Summing the rows of the triangle gives the total number of basis monomials, 



$$
\dim(\mathcal{P}_d) = 1 + 2 + \cdots + d + (d+1) = \binom{d+2}{2}.
$$



The size of the next higher polynomial space is related to the lower by, $$\dim(\mathcal{P}_{d+1}) =  \dim(\mathcal{P}_{d}) + d + 2$$.

### Indexing the Basis of $\mathcal{P}_{n}$

A slight digression. I want to index the basis monomials of $\mathcal{P}_{n}$. I do this by iterating the rows of the triangle in $\mathbb{Z}^{3}$ satisfying $n = i + j + k$, from top to bottom, and left to right. A sample of the triangle is depicted below. Each monomial is annotated with an index in <span style="color:blue">blue</span>.

<a name="triangle"></a>
$$
\begin{array}{c c c c c}
& & & \underbrace{z^n}_{\color{blue}0} \\
& & \underbrace{xz^{n-1}}_{\color{blue}1} &  & \underbrace{yz^{n-1}}_{\color{blue}2} \\
& \underbrace{x^2z^{n-2}}_{\color{blue}3} &  & \underbrace{xyz^{n-2}}_{\color{blue}4} &  & \underbrace{y^2z^{n-2}}_{\color{blue}5} \\
\underbrace{x^3z^{n-3}}_{\color{blue}6} &  & \underbrace{x^2yz^{n-3}}_{\color{blue}7} &  & \underbrace{xy^2z^{n-3}}_{\color{blue}8} &  & \underbrace{y^3z^{n-3}}_{\color{blue}9}\\
\vdots &  & \vdots &  & \vdots &  & \vdots \\
\end{array}
$$


The basis of $$\mathcal{P}_{n}$$ ordered in this way expressed as a mapping of on the exponential triples is


$$
(i,j,k) \longmapsto 
\begin{cases}
     0               & \text{if } \quad k = n \\
\binom{n+1-k}{2} + j & \it{o.w.} \\
\end{cases}
$$

### Properties of $\Delta$ and $\mathcal{P}_{n}$

Of course $\Delta$ isn't like the boundary operator, $\Delta^2 \neq 0$.


$$
\Delta^2(x^2y^2) = \Delta(2y^2 + 2x^2) \neq 0
$$


$\Delta$ isn't injective; otherwise the $\mathcal{H}_d$ would be trivial.


$$
\Delta(x^2) = \Delta(y^2) = 2\Delta(x^2) = \Delta(y^2) = 2
$$



#### $\Delta$ is Onto

On $$\Delta: \mathcal{P}_{2} \longrightarrow \mathcal{P}_{0}$$, we already showed $\Delta$ is onto. Namely,


$$
\Delta(x^2) = \Delta(y^2) = \Delta(z^2) = 2 \quad \text{and} \quad \Delta(xy) = \Delta(xz) = \Delta(yz) = 0.
$$


Earlier we already saw  $$\Delta: \mathcal{P}_{3} \longrightarrow \mathcal{P}_{1}$$ is onto.


$$
\begin{array}{c c c c}
\Delta (x^3) = 6x & \Delta(x^2y) = 2y & \Delta(xz^2) = 2x & \Delta(xyz) = 0 \\
    \Delta(y^3) = 6y & \Delta(x^2z) = 2z & \Delta(y^2z) = 2z \\
    \Delta(z^3) = 6z & \Delta(xy^2) = 2x & \Delta(yz^2) = 2y \\
\end{array}
$$


Consider $$\Delta: \mathcal{P}_{n+2} \longrightarrow \mathcal{P}_{n}$$. We can prove it is onto by induction on the monomial basis elements of $$\mathcal{P}_{n}$$, as ordered by the triangular [figure](#triangle) above. The first two rows are the base cases. Specifically, each basis monomial of the first two rows of the triangle is mapped onto by some $p \in \mathcal{P}_{n+2}$.


$$
\begin{gather}
\Delta(z^{n+2}) = (n+1)(n+2){\colorbox{yellow}{$z^n$}} \\
\Delta(xz^{n+1}) = n(n+1){\colorbox{yellow}{$xz^{n-1}$}} \\
\Delta(yz^{n+1}) = n(n+1){\colorbox{yellow}{$yz^{n-1}$}} \\
\Delta(x^2z^n) = 2z^n + n(n-1)x^2z^{n-2} \Longrightarrow \Delta\Big(x^2z^n - {2z^{n+2} \over (n+1)(n+2)}\Big) = n(n-1){\colorbox{yellow}{$x^2z^{n-2}$} } \\
\Delta(xyz^n) = n(n-1){\colorbox{yellow}{$xyz^{n-2}$} } \\
\Delta(y^2z^n) = 2z^n + n(n-1)y^2z^{n-2} \Longrightarrow \Delta\Big(y^2z^n - {2z^{n+2} \over (n+1)(n+2)}\Big) = n(n-1){\colorbox{yellow}{$y^2z^{n-2}$} } \\
\Delta(x^3z^{n-1}) = 6xz^{n-1} + (n-1)(n-2)x^3z^{n-3} \Longrightarrow \Delta\Big(x^3z^{n-1} - {6xz^{n+1} \over n(n+1)}\Big) = (n-1)(n-2){\colorbox{yellow}{$x^3z^{n-3}$} } \\
\end{gather}
$$


Assume $\Delta$ is onto $x^{k-j}y^jz^{n-k}$ the $s$th monomial basis element of $\mathcal{P}_n$. Then the next basis monomial is either $x^{k-j-1}y^{j+1}z^{n-k}$ or $x^{k+1}z^{n-k-1}$, two cases. 

**Case 1**


$$
\begin{gather}
\Delta(x^{k-j-1}y^{j+1}z^{n-(k-2)}) = c_x\colorbox{orange}{$x^{k-j-3}y^{j+1}z^{n-(k-2)}$} + c_y\colorbox{orange}{$x^{k-j-1}y^{j-1}z^{n-(k-2)}$} + \\c_z\colorbox{yellow}{$x^{k-j-1}y^{j+1}z^{n-k}$}\\
\end{gather}
$$


Both the orange terms are in the $k-2$ row of the triangle arrangement of the basis, appearing two rows above the yellow term,  which means they are ordered before the yellow term. Then by the induction hypothesis the orange terms are mapped onto by $$p_a, p_b \in \mathcal{P}_{n+2}$$ and an element of $\mathcal{P}_{n+2}$ can be constructed so that it is onto the yellow term -- $(s+1)$th monomial basis term.


$$
\Delta(x^{k-j-1}y^{j+1}z^{n-(k-2)} - c_x p_a - c_y p_b) = c_z\colorbox{yellow}{$x^{k-j-1}y^{j+1}z^{n-k}$}
$$


**Case 2**


$$
\Delta(x^{k+1}z^{n-k+1}) = k(k+1)\colorbox{orange}{$x^{k-1}z^{n-k-1}$} + (n-k+1)(n-k)\colorbox{yellow}{$x^{k+1}z^{n-k}$}
$$


In the triangle arrangement of the basis, the orange term is in the row above that of the yellow term, and therefore ordered before the yellow term. Then by the induction hypothesis there is a  $$p \in \mathcal{P}_{n+2}$$ that maps onto the orange term; and an element of $$\mathcal{P}_{n+2}$$ can be constructed so that it is onto the yellow term -- $(s+1)$th monomial basis term.


$$
\Delta(x^{k+1}z^{n-k+1} - k(k+1)p) = (n-k+1)(n-k)\colorbox{yellow}{$x^{k+1}z^{n-k}$}\\
$$

​                  																				$\Box$

#### Harmonic Polynomials 

Since $$\Delta: \mathcal{P}_{n+2} \longrightarrow \mathcal{P}_{n}$$ is onto $$\mathcal{P}_{n+2} / \mathcal{H}_{n+2} \cong \mathcal{P}_{n}$$, as vector spaces. Consequently, $$\mathcal{P}_{n+2}$$ can be split into two vector spaces: $$\mathcal{H}_{n+2}$$ (harmonic polynomials ) and non-harmonic polynomials. The non-trivial coset representatives of $$\mathcal{P}_{n+2} / \mathcal{H}_{n+2}$$ are the non-harmonic elements. Furthermore, $$\mathcal{P}_{n+2}$$ is the sum of its harmonic and non-harmonic parts: $$p = q + h \in \mathcal{P}_{n+2}$$ where $$h \in \mathcal{H}_{n+2}$$ and $$q \in \mathcal{P}_{n+2}$$ is some non-harmonic polynomial.

The isomorphism $$\mathcal{P}_{n} \cong \mathcal{P}_{n+2}/\mathcal{H}_{n+2}$$ implies there is an injective map $$\iota: \mathcal{P}_{n} \longrightarrow \mathcal{P}_{n+2}$$ onto the non-harmonic polynomials . Namely, it is the inverse of $q + \mathcal{H}_{n+2} \mapsto \Delta(q)$. The non-harmonic space can be denoted $$\iota(\mathcal{P}_n)$$, and $$\mathcal{P}_{n+2} \cong \mathcal{H}_{n+2} \oplus\iota(\mathcal{P}_{n})$$. Now, with $$\mathcal{P}_{n+2}$$ decomposed, the dimension of $$\mathcal{H}_{n+2}$$ can be computed.


$$
\begin{align}
\dim(\mathcal{H}_{n+2}) &= \dim(\mathcal{P}_{n+2}) - \dim(\mathcal{P}_{n})\\
   &=  \binom{n+4}{2} - \binom{n+2}{2}\\
   &= \frac{1}{2} \Big(\cancel{n^2}+7n+12 - \cancel{n^2} -3n-2\Big)\\
   &= 2n + 5
\end{align}
$$


Substituting $n-2$ in for $n$ gives, 


$$
\boxed{\dim(\mathcal{H}_{n}) = \bf 2n + 1 \quad \text{for } n \geq 2 }
$$

#### Examples of Harmonic Polynomials Spaces

##### Case $\mathcal{H}_{2}$.


$$
\mathcal{P}_2 = \{ xy, \ xz,\ yz,\ x^2,\ y^2,\ z^2 \}
$$

 Applying the laplacian to each basis monomial of $\mathcal{P}_2$.


$$
\begin{gather}
   \Delta (xy) = 0 & \Delta(x^2) = 2  \\
    \Delta(xz) = 0 & \Delta(y^2) = 2  \\
    \Delta(yz) = 0 & \Delta(z^2) = 2 \\
\end{gather}
$$


Subtracting the quadratic monomials with the same laplacian gives three more harmonic polynomials. 


$$
\begin{gather}
   \Delta(x^2 - y^2) = 0, & \Delta(z^2 - y^2) = 0, & \Delta(z^2 - x^2) = 0 \\
\end{gather}
$$


Since $(z^2 - y^2) - (z^2 - x^2) = x^2 - y^2$, only two of the three are linearly independent. Therefore, $\dim(\mathcal{H}_2)=5$  and


$$
\mathcal{H}_2 = \{ xy, \ xz,\ yz,\ z^2 - x^2,\ z^2 - y^2 \}
$$



Modding out $\mathcal{P}_2$ by $\mathcal{H}_2$ 


$$
\begin{gather}
xy \mod \mathcal{H}_2 \equiv 0 \mod \mathcal{H}_2 \\
 xz \mod \mathcal{H}_2 \equiv 0 \mod \mathcal{H}_2 \\
 yz \mod \mathcal{H}_2 \equiv 0 \mod \mathcal{H}_2 \\
 x^2 \mod \mathcal{H}_2 \equiv z^2 \mod \mathcal{H}_2 \\
 y^2 \mod \mathcal{H}_2 \equiv z^2 \mod \mathcal{H}_2 \\
 \end{gather}
$$


The only non-trivial element is $[x^2] \simeq [y^2] \simeq [z^2]$.



##### Case $\mathcal{H}_{3}$.


$$
\mathcal{P}_3 = \{ x^3, \ x^2y,\ xy^2,\ y^3,\ x^2z,\ xyz,\ y^2z,\ xz^2,\ yz^2,\ z^3 \}
$$

 Applying the laplacian to each basis monomial of $\mathcal{P}_3$.


$$
\begin{gather}
   \Delta (x^3) = 6x & \Delta(x^2y) = 2y & \Delta(xz^2) = 2x & \Delta(xyz) = 0 \\
    \Delta(y^3) = 6y & \Delta(x^2z) = 2z & \Delta(y^2z) = 2z \\
    \Delta(z^3) = 6z & \Delta(xy^2) = 2x & \Delta(yz^2) = 2y \\
\end{gather}
$$


Subtracting monomials with the same laplacian gives a generating set of $\mathcal{H}_3$.


$$
\begin{gather}
   \Delta(x^3 - 3xz^2) = 0 & \Delta(x^3 - 3xy^2) = 0 & \Delta(xy^2 - xz^2) = 0 & \Delta(xyz) = 0 \\
   \Delta(y^3 - 3x^2y) = 0 & \Delta(y^3 - 3yz^2) = 0 & \Delta(x^2y - yz^2) = 0 \\
   \Delta(z^3 - 3x^2z) = 0 & \Delta(z^3 - 3y^2z) = 0 & \Delta(x^2z - y^2z) = 0 \\
\end{gather}
$$


Noticing that 


$$
\begin{gather}
   x^3 - 3xz^2 - (x^3 - 3xy^2) \cong xz^2 - xy^2 \\
   y^3 - 3x^2y - (y^3 - 3yz^2) \cong x^2y - yz^2 \\
   z^3 - 3x^2z - (z^3 - 3y^2z) \cong x^2z - y^2z \\
\end{gather},
$$


eliminates three linearly dependent elements from the generating set; the remaining $\dim(\mathcal{H}_3)=7$ elements form a basis,


$$
\mathcal{H}_3 = \{x^3 - 3xy^2,\ x^3 - 3xz^2,\ y^3 - 3x^2y,\ y^3 - 3yz^2,\ z^3 - 3x^2z,\ z^3 - 3y^2z,\ xyz \}
$$


Modding out $\mathcal{P}_3$ by $\mathcal{H}_3$,


$$
\begin{gather}
xyz \simeq 0 \\
 \colorbox{yellow}{$x^3 \simeq  3xy^2 \simeq 3xz^2$} \\
 \colorbox{pink}{$y^3  \simeq  3x^2y \simeq 3yz^2$} \\
 \colorbox{orange}{$z^3 \simeq  3x^2z \simeq 3y^2z$} \\
 \colorbox{yellow}{$xy^2 \simeq\frac{1}{3} x^3 \simeq xz^2$} \\
 \colorbox{pink}{$x^2y \simeq\frac{1}{3} y^3 \simeq yz^2$} \\
 \colorbox{orange}{$y^2z \simeq\frac{1}{3} z^3 \simeq x^2z$} \\
 \colorbox{pink}{$yz^2 \simeq\frac{1}{3} y^3 \simeq x^2z$} \\
 \colorbox{orange}{$x^2z \simeq\frac{1}{3} z^3 \simeq y^2z$} \\
 \colorbox{yellow}{$xz^2 \simeq\frac{1}{3} x^3 \simeq xy^2$} \\
 \end{gather}
$$


The yellow, orange, and pink highlighted equivalences are the 3 non-trivial elements of $\mathcal{P}_3 /\mathcal{H}_3$.


$$
\mathcal{P}_3 /\mathcal{H}_3 = <[x^3], [y^3], [z^3]>
$$





[notes]: https://web.math.utk.edu/~afreire/m435f07/m435sphericalharmonics.pdf
