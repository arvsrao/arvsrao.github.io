---
layout: post
title: Parameterizing the Space of 3D Rotations
comments: true
category: mathematics
tags: applied topology, SymPy
---

3D medical images in the NifTI format store data from MRI acquisitions of some anatomy, like a human brain or heart. When I was a postdoc @Penn [my lab][3] was primarily interested in studying brains. Each image associates grayscale values ( in the simplest case ) to coordinates in a discrete coordinate system $(i,j,k)$, which describe voxel locations. And for reasons best explained by [NifTI FAQ][2] it's useful/important to align the acquired image to some other coordinate system. This alignment is stored in the image header, as a rigid motion plus an offset. Here's a bit of [NifTI documentation][1] motivating the need to keep the aligment.

	This method can also be used to represent "aligned"
	coordinates, which would typically result from some post-acquisition
	alignment of the volume to a standard orientation (e.g., the same
	subject on another day, or a rigid rotation to true anatomical
	orientation from the tilted position of the subject in the scanner).

The NifTI standard allows for orientation reversing transforms, but in this post I focus on *proper* rotations. These rigid motions must preserve volume and orientation; rigidity necessitates linearity. Being a geometric property, volume is preserved when the transformation is an isometry; for some matrix $A$, we require $A A^T = I$. Moreover, orientation preservation happens when $\det(A) > 0$. The intersection of all these requirements is the group of 3D rotations, otherwise known as the *special orthogonal group*,

$$ 
\begin{equation*}
	SO(3) = \{ A \in Mat(3, \mathbb{R}) \ | \ AA^T =A^TA =I \ \& \ \det(A)=1 \}.
\end{equation*}
$$

The final affine transform rotates and translates image coordinates and is of the form

$$
\begin{equation*}
    \vec{v} = A \vec{x} + \vec{q},  \quad \text{where } A \in SO(3), \ \vec{q}, \vec{x} \in \mathbb{Z}^3.
\end{equation*}
$$

Getting to the point, $A$ isn't what gets stored. Instead four numbers representing a unit quaternion. It seems a point in $S^3 \in \mathbb{H}$ can represent a 3D rotation. More than that, there's a surjective homomorphism from $S^3 \subsetneq \mathbb{H}$ to $SO(3)$. *Pretty amazing*. But what's going on here? To understand more we need to explore the structure of $SO(3)$ a bit.

## Topology of $SO(3)$

Lenorad Euler, [so long ago][4], discovered that $A \in SO(3)$ fixes a vector; the line through this vector is called the *axis of rotation*. Below is a lemma that recapitulates and generalizes this fact for rigid rotations in $\mathbb{R}^N$, where $N$ is odd.

<p><strong>Lemma. A</strong><em>	Suppose $A \in SO(N)$ where $N$ is odd. Then $\exists \vec{n} \in \mathbb{R}^N$ so that $A \vec{n} = \vec{n}$. Equivalently, $\lambda = 1$ is an eigenvalue of $A$.
</em></p>
<p><em>proof:</em></p>
Consider $A - I$. Because $N$ is odd $\det(-(A-I)) = -\det(A-I)$. Then

$$
\begin{align*}
    \det(A-I) & = \det(A - AA^T) = \det(A) \times \det(I - A^T)   \\
              & = \det(-(A^T - I)) \\
              & = -\det((A-I)^T) \\
              & = - \det(A-I) \\          
\end{align*}
$$

Consequently, $\det(A-I) = 0$, which implies $\lambda = 1$ is an eigenvalue of $A$.
<div align="right">
	<p><em>$\Box$</em></p>
</div>

Applying **Lemma A** to $A \in SO(3)$, $\det(A) = 1 \times \lambda_2 \lambda_3 = 1$. The immediate implication is that both of the unknown eigenvalues must be unit complex numbers and conjugates of each other; in general, the eigenvalues of any rotation are $1, \omega, \bar{\omega}$, where $\omega \bar{\omega} = 1$. In lay terms this means that $A \in SO(3)$ is a rotation of $\mathbb{R}^3$ about an axis, $[\vec{n}] \in \mathbb{RP}^2$ by some fixed angle, $\theta \in S^1$. 

Since $\vec{n}$ and $\theta$ completely determine $A$, it can be decomposed by a special orthogonal matrix formed from the postive frame $$\{\vec{u}, \vec{v}, \vec{n}\}$$. 

$$
A_{\theta, \vec{n}} = 
\begin{bmatrix}
	\vec{u} & \vec{v} & \vec{n}
\end{bmatrix}

\begin{bmatrix}
	\cos \theta & -\sin \theta & 0 \\
	\sin \theta &  \cos \theta & 0 \\
	0 & 0 &  1  \\
\end{bmatrix}

\begin{bmatrix}
	\vec{u}^T \\
	\vec{v}^T \\
    \vec{n}^T \\
\end{bmatrix}.
$$

$A$ is decorated to emphasize its dependence on $\theta$ and $\vec{n}$. Dependence implies the projection

$$
S^1 \times S^2 \xrightarrow{\quad pr \quad} SO(3) \quad \text{where} \quad pr(\theta, \vec{n}) = A_{\theta, \vec{n}} \in SO(3)
$$

is surjective. However, $pr$ is not 1-to-1. $A_{0, \vec{n}} = I$ for all $\vec{n} \in S^2$. Additionally, there are a few identifications that result when one or the other, or both coordinates in $S^1 \times S^2$ are negative. Consider $A_{-\theta, -\vec{n}}$. The positive frame for $A_{-\theta, -\vec{n}}$ is close but not the same as $A_{\theta, \vec{n}}$, because $-\vec{n}$ has the opposite orientation. Their positive frames differ by a permutation matrix.

$$
\begin{bmatrix}
	\vec{v} & \vec{u} & -\vec{n}
\end{bmatrix}
=
\begin{bmatrix}
	\vec{u} & \vec{v} & \vec{n}
\end{bmatrix}
\begin{bmatrix}
	0 & 1 & 0 \\
	1 & 0 & 0 \\
    0 & 0 & -1 \\
 \end{bmatrix}.
$$

Taking the determinant of the right hand side verifies the frame is positive. Now the valid matrix decomposition for

$$
A_{-\theta, -\vec{n}} = 
\begin{bmatrix}
	\vec{v} & \vec{u} & -\vec{n}
\end{bmatrix}

\begin{bmatrix}
	\cos \theta & \sin \theta & 0 \\
	- \sin \theta &  \cos \theta & 0 \\
	0 & 0 &  1  \\
\end{bmatrix}

\begin{bmatrix}
	\vec{v}^T \\ 
	\vec{u}^T \\ 
	-\vec{n}^T \\
\end{bmatrix}.
$$

It's not so apparent from the decompositions of $A_{\theta, \vec{n}}$ and $A_{-\theta, -\vec{n}}$, but they're equal. Just compute where basis elements are mapped. A similar argument shows that for $-pi \geq \theta \leq \pi$

$$
\begin{align*}
A_{\theta, -\vec{n}} & = 
\begin{bmatrix}
	\vec{v} & \vec{u} & -\vec{n}
\end{bmatrix}
\begin{bmatrix}
	\cos \theta & - \sin \theta & 0 \\
	\sin \theta &  \cos \theta & 0 \\
	0 & 0 &  1  \\
\end{bmatrix}
\begin{bmatrix}
	\vec{v}^T \\ 
	\vec{u}^T \\ 
	-\vec{n}^T \\
\end{bmatrix} \\
& =
\begin{bmatrix}
	\vec{u} & \vec{v} & \vec{n}
\end{bmatrix}
\begin{bmatrix}
	\cos \theta & \sin \theta & 0 \\
	-\sin \theta &  \cos \theta & 0 \\
	0 & 0 &  1  \\
\end{bmatrix}
\begin{bmatrix}
	\vec{u}^T \\
	\vec{v}^T \\
    \vec{n}^T \\
\end{bmatrix} \\
& =A_{-\theta, \vec{n}} \ .
\end{align*}
$$

In summary, projection $pr$ has the following properties.

---
**Identifications**

1. $A_{0, \vec{n}} = I$ for all $\vec{n} \in S^{2}$
2. $A_{\theta, \vec{n}} = A_{-\theta, -\vec{n}}$ for $\theta \in \[-\pi, \pi\]$
3. $A_{\theta, -\vec{n}} = A_{-\theta, \vec{n}}$ for $\theta \in \[-\pi, \pi\]$

---

$SO(3)$ *is* $S^1 \times S^2$ under the above identifications, $S^1 \times S^2 \Big/\sim$. Not very clean though. It's hard to imagine the shape of $SO(3)$ in this form. But we can try. A heuristic image of $S^1 \times S^2$ could be a curve of circles ( each representing an $S^2$ ). In accordance with Identification $$ however as the parameter on the curve approaches $0$, the circles become smaller, and finally degenerate to a point at $0$. 

<figure>
<div align="center">
	<img src = "/assets/identification1.jpg">
</div>
<figcaption>Figure #1. $S^1 \times S^2$ under identifications $1$.</figcaption>
</figure>

<figure>
<div align="center">
	<img src = "/assets/identification2.jpg">
</div>
<figcaption>Figure #2. $S^1 \times S^2$ under identifications $1$ and $2$.</figcaption>
</figure>

<figure>
<div align="center">
	<img src = "/assets/identification3.jpg">
</div>
<figcaption>Figure #3. $S^1 \times S^2 \Big/ \sim$.</figcaption>
</figure>


As stated above there's a simpler description in terms of $S^3$; specifically, the upper hemisphere of $S^3$. 

Before one maps into $S^3$ which is also constant on sets of identified points stated in **Identifications**. Specifically, we have the following lemma.

<p><strong>Lemma. B</strong><em>


	$$ \varphi(\theta, \vec{n}) = \Big(\vec{n} \cdot \sin \frac{\theta}{2}, \cos \frac{\theta}{2} \Big) \in S^{3} \quad \text{where} \quad \theta \in [-\pi, \pi) \text{ and } \vec{n} \in S^2
	$$

takes $S^1 \times S^2$ onto the upper hemisphere of $S^3$, and when the domain is restricted to $S^1 \times \{\text{ upper hemisphere}\}$, $\varphi$ is a parametrization of the upper hemisphere. Since $\varphi$ satisfies identifications equivalent to <b>1</b> though <b>3</b>, stated in <b>Identifications</b>, there is a well-defined continuous map $g$, which is s bijective on the open upper hemisphere of $S^3$. Also $g$ is onto $SO(3)$. Identification <b>4</b> on $S^3$ is equivalent to identification of antipodes on the equator of $S^3$: $(\vec{n}, 0) \sim (-\vec{n},0)$. Therefore, $g \big/ \sim$ is a homeomorphism from $\mathbb{RP}^3$ to $SO(3)$.  
</em></p>
<p><em>proof:</em></p>

Since $\cos \frac{\theta}{2} \geq 0$ for all $\theta \in [-\pi, \pi]$, $\varphi$ maps onto the upper hemisphere of $S^3$. Identification **1** states $pr(0, \vec{n}) = I$. Similarily, $\varphi(0, \vec{n}) = (\vec{0}, 1)$ for all $\vec{n} \in S^{2}$. 

Identification **2** states $pr(\theta, \vec{n}) = pr(-\theta, -\vec{n})$. The same holds for $\varphi$.

$$
\begin{align*}
	\varphi(-\theta, -\vec{n}) & = \Big( -\vec{n} \cdot \sin(-\frac{\theta}{2}),\ \cos(-\frac{\theta}{2})\Big) \\
						 & = \Big(\vec{n} \cdot \sin \frac{\theta}{2},\ \cos \frac{\theta}{2} \Big) \\
						 & = \varphi(\theta, \vec{n}). \\
\end{align*}
$$

Identification **3** states  $pr(-\theta, \vec{n}) = pr(\theta, -\vec{n})$. The same holds for $\varphi$.

$$
\begin{align*}
	\varphi(-\theta, \vec{n}) & = \Big( \vec{n} \cdot \sin(-\frac{\theta}{2}),\ \cos(-\frac{\theta}{2})\Big) \\
						& = \Big( - \vec{n} \cdot \sin \frac{\theta}{2} ,\ \cos(\frac{\theta}{2})\Big) \\
						& = \varphi(\theta, -\vec{n}). \\
\end{align*}
$$

These identifications allow us to take $(\theta, \vec{n}) \in S^1 \times S^2$ to be unique ( or the preferred representative ) when $\vec{n} \cdot e_3 \geq 0$ and $-\pi < \theta < \pi$. Also, the definition 

$$
	g\Big(\varphi(\theta, \vec{n})\Big) = pr(\theta, \vec{n})
$$ 

must bijective.

<figure>
<div align="center">
	<img src = "/assets/s3_so3.jpg">
</div>
<figcaption>Figure #1. Mapping $S^1 \times S^2 \Big/ \sim$ into upper hemisphere of $S^3$</figcaption>
</figure>

It's easy to check that $S^1 \times S^2$ under the first 3 equalivances map bijectively onto the open upper hemisphere of $S^3$. Figure #1 is a picture I drew of how $\varphi$ maps $S^1 \times S^2 \Big/ \sim$ into the upper hemisphere of $S^3$. I think of  $\theta$ parameterizing a series of $S^2$ upper hemispheres, examplars are drawn as half circles in black (when the angle is positive) & red ( for when the angle is negative) in Figure #1. As the parameter $\theta$ increases from $-\frac{\pi}{2}$, I imagine a hemisphere, drawn as a half circle in Figure #1, tracing out the upper hemisphere of $S^3$; rising up from left, becoming smaller as $\theta$ approaches $0$ from the left, degenerating to a point at $\theta = 0$, then reappearing on the right and becoming larger as $\theta$ approaches $\frac{\pi}{2}$.

The equatorial $S^2$ is mapped onto from $(\pm \pi, \vec{n}) \in S^1 \times S^2$ by $\varphi$. 

$$ 
\varphi(\pm \pi, \vec{n}) = \Big(\sin(\pm \frac{\pi}{2})\vec{n}, \cos(\pm \frac{\pi}{2})\Big) =  (\pm \vec{n}, 0).
$$

Identification **3** can be extended  that $pr(\pi, -\vec{n}) = pr(-\pi, \vec{n})$, which requires that antipodes in the equatorial $S^2$
of $S^3$ be identified. Then $S^3 \Big/ \sim \ \cong \mathbb{RP}^3 \cong SO(3)$. Here $\mathbb{RP}^3$ is realized as an $\mathbb{RP}^2$ attached to the boundary of a 3-cell, the upper hemisphere of $S^3$.  
<div align="right">
	<p><em>$\Box$</em></p>
</div>

<figure>
<div align="center">
	<img src = "/assets/rp3so3.jpg">
</div>
<figcaption>Figure #2. Direct mapping $S^1 \times S^2 \Big/ \sim$ into the Ball Model of $\mathbb{RP}^3$</figcaption>
</figure>

There's [actually a pretty slick way of showing $SO(3) \cong \mathbb{RP}^3$][7] by mapping $S^1 \times S^2 \Big/ \sim$ into $B_3(\vec{0}, \pi)$, the 3-ball of radius $\pi$. It's simply $(\theta, \vec{n}) \mapsto \theta \cdot \vec{n}$. Figure #2 is a picture I drew to visualize this map. Identifications **1** through **3** ensure the map is bijective inside the ball. On the boundary the antipodes are identified, in accordance with identification **4**. 


## Connections between $SU(2)$ and $SO(3)$

Rotations in $2$-dimensions, $SO(2)$, look like $S^1$. Indeed, $S^1 \cong SO(2)$ is a homeomorphism via

$$
  \theta \mapsto
  \begin{bmatrix} 
	\cos \theta & -\sin \theta \\
	\sin \theta &  \cos \theta \\
  \end{bmatrix}.
$$

Amazingly, the map shown above doubles as a group isomorphism. Implicit in that statement is that $S^1$ is a group, and that we can think of $\theta \in S^1$ acting on vectors $v \in \mathbb{R}^2$. Now, $S^2$ has no group structure because it carries no non-vanishing vector fields--[a consequence of Brouwer's Fixed Point Theorem][8]. If $S^2$ was a group the left and right group actions would generate diffeomorphisms, from which non-vanishing vector fields could be extracted; see [proposition 5.1.1][9]. The same argument can be generalized to show even dimensional spheres, $S^{2n}$, carry no group structure. Okay. So there's that. But there is hope for $S^3$. Consider the matrix group

$$
	SU(2) = \Big\{ 
		\begin{bmatrix}
			a & b \\
			c & d \\
		\end{bmatrix} 
		\in 
		GL(n,, \mathbb{C})
		\quad \Big\vert \quad 
		AA^{\dagger} = A^{\dagger} A = I  
	\Big\}.
$$ 

The condition $AA^{\dagger} = I$ in terms of the elements is 

$$
\begin{align*}
		\begin{bmatrix}
			1 & 0 \\
			0 & 1 \\
		\end{bmatrix} 
		&=
		\begin{bmatrix}
			\lvert a \rvert^2 + \lvert b \rvert^2 & a\bar{c} + b\bar{d} \\
			c\bar{a} + d\bar{b} & \lvert c \rvert ^2 + \lvert d \rvert ^2 \\
		\end{bmatrix} 
\end{align*}
$$

The constraint on the off diagonal elements is equivalent to orthogonality of $\(c\ d\)$ and $\(a \ b\)$. So, we can choose $c = a$ and $d = -\bar{b}$; an equivalent definition of $SU(2)$ is 

$$
	SU(2) = \Big\{ 
		\begin{bmatrix}
			a & -\bar{b} \\
			b & \bar{a}  \\
		\end{bmatrix} 
		\ \Big\vert \ 
		 \lvert a \rvert^2 + \lvert b \rvert ^2 = 1
		 \text{ for } a,b \in \mathbb{C}
	\Big\}.
$$

Therefore, $S^3$ has the group structure $SU(2)$. In order to define a proper action of $A \in SU(2)$ on vectors in $\mathbb{R}^3$, it's necessary to introduce the lie algebra of $SU(2)$, $\mathfrak{su}(2)$.


<p><strong>Lemma. C</strong><em> 
	The Lie Algebra of $SU(N)$, denoted $\mathfrak{su}(N)$, is the space of skew-symmetric matrices, an $n$-dimensional real vector space. When $N=2$, $\mathfrak{su}(2)$ is a $3$-dimensional vector space with basis

	$$
	e_1 = 
	\begin{bmatrix}
	i & 0 \\
	0 & -i \\
	\end{bmatrix}
	\quad
	e_2 = 
	\begin{bmatrix}
	0 & -1 \\
	1 &  0 \\
	\end{bmatrix}
	\quad
	e_3 = 
	\begin{bmatrix}
	0 & i \\
	i & 0 \\
	\end{bmatrix}.
$$
</em></p>
<p><em>proof:</em></p>	

$\mathfrak{su}(2)$ is the tangent space of $SU(2)$ at $I$, the identity. So, let $A(t) : (-\epsilon, \epsilon) \longrightarrow SU(N)$ be a curve such that $A(0) = I$ and $\frac{\partial A}{\partial t}(0) = B$, some complex $n \times n$ matrix. Take the derivative of $I = A(t)A(t)^{\dagger}$ at $t=0$.

$$
\begin{align*}
0 &= \frac{\partial A}{\partial t}(0) A^{\dagger}(0) + A(0) \frac{\partial A}{\partial t} A^{\dagger}(0) \\
  &= B \cdot I + I \cdot B^{\dagger} \\
  & \Longrightarrow B = -B^{\dagger}
\end{align*}.
$$

Then, 

$$
\mathfrak{su}(N) = \Big\{ B \in Mat(N, \mathbb{C}) \ \Big\vert \ B = -B^{\dagger} \Big\}.
$$

The skew-symmetric condition on matrixes in $\mathfrak{su}(2)$ directly leads to the general form

$$
\begin{bmatrix}
	i a    & -c + i b  \\
	c +i b  & -ia \\ 
\end{bmatrix}
= 
a\cdot e_1 + c \cdot e_2 + b \cdot e_3
\quad \text{here } a,b,c \in \mathbb{R}
$$
<div align="right">
	<p><em>$\Box$</em></p>
</div>

Consider the conjugation action on $SU(2)$. Differentiation gives exactly the action of $S^3 \cong SU(2)$ on vectors in a $3$-dimensional real vector space, the lie algebra $\mathfrak{su}(2)$, which we seek. Letting $\nu \in \mathfrak{su}(2)$, the action is

$$
	A \cdot \nu = A^{\dagger} \nu A \quad \text{for fixed } A \in SU(2).
$$

It may not look like it but the action is an isometry ( a rotation ) of $\mathfrak{su}(2)$. Suppose $v,w \in \mathfrak{su}(2)$, then by properties of the trace

$$
   \langle A \cdot v, A \cdot w \rangle = \frac{1}{2}Tr(A^{\dagger}vAA^{\dagger}w^{\dagger}A) = \frac{1}{2}Tr(A^{\dagger}vw^{\dagger}A) = \frac{1}{2}Tr(vw^{\dagger}) = \langle v, w \rangle.
$$

Okay. So the action is orthogonal; but does it preserve orientation? With the help of [SymPy][5], a wonderful symbolic manipulation library, it's possible to [explicitly compute a matrix representation of the $ SU(2)$ action][11] on all of $\mathfrak{su}(2)$. For $a^2 + b^2 + c^2 + d^2 = 1$ the matrix is

$$ 
	B = 
	\begin{bmatrix}
	a^2 + b^2 - c^2 - d^2 &             2ad + 2bc &            -2ac + 2bd \\
	           -2ad + 2bc & a^2 - b^2 + c^2 - d^2 &             2ab + 2cd \\
	            2ac + 2bd &            -2ab + 2cd & a^2 - b^2 - c^2 + d^2 \\
	\end{bmatrix}. 
$$

The determinant via the [SymPy][5] api

	In [51]: f = a**2 + b**2 + c**2 + d**2

	In [52]: factor(B.det()).subs(f, 1) == 1
	Out[52]: True

Another way of verifying orthogonality 

	In [337]: factor(simplify(B * B.transpose())).subs(f,1)
	Out[337]:
	Matrix([
	[1, 0, 0],
	[0, 1, 0],
	[0, 0, 1]])

	In [338]: factor(simplify(B.transpose() * B)).subs(f,1)
	Out[338]:
	Matrix([
	[1, 0, 0],
	[0, 1, 0],
	[0, 0, 1]])

Indeed, the action of $S^3 \cong SU(2)$ on $\mathfrak{su}(2)$ generates a homomorphism from $S^3 \cong SU(2)$ onto $SO(3)$. A bit more work and it's possible to show that the homomorphism is surjective. Earlier it was shown that each rotation in $\mathbb{R}^3$ is completely determined by some axis $\vec{n}$ and an angle of rotation $\theta$. Let $\vec{n} = b \cdot e_1 + c\cdot e_2 + d\cdot e_3$. Again with [SymPy][5] we can verify $B * \vec{n} = \vec{n}$ for all $\vec{n} \in \mathbb{R}^3$. 

	In [340]: simplify(B * Matrix([[b],[c],[d]])).subs(f, 1)
	Out[340]:
	Matrix([
	[b],
	[c],
	[d]])

That is to say there's always a $A \in SU(2)$ that generates an action which fixes a given line through the origin in $\mathbb{R}^3$. $a = \cos \theta$ encodes the rotation angle. All the entries in $B$ are homogenous polynomials of degree $2$ so it follows that $\pm A \in SU(2)$ generate the same action.

<!-- The Adjoint map for $SU(2)$ is

$$
	SU(2) \ni B \longmapsto A^{\dagger} B A \in SU(2) \quad \text{ for fixed } A \in SU(2)
$$
 -->



[1]: https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h
[2]: https://nifti.nimh.nih.gov/nifti-1/documentation/faq#Q17
[3]: https://www.cbica.upenn.edu
[4]: https://en.wikipedia.org/wiki/Euler%27s_rotation_theorem#Euler.27s_theorem_.281776.29
[5]: http://docs.sympy.org/latest/index.html
[6]: https://en.wikipedia.org/wiki/Gimbal_lock#Loss_of_a_degree_of_freedom_with_Euler_angles
[7]: https://en.wikipedia.org/wiki/Rotation_group_SO(3)#Topology
[8]: http://www.digizeitschriften.de/dms/img/?PID=GDZPPN002264021
[9]: http://maths-people.anu.edu.au/~andrews/DG/DG_chap5.pdf
[10]: http://www.math.columbia.edu/~woit/notes3.pdf
[11]: https://gist.github.com/arvsrao/b3423f8404d9e59e7819dae5b6c601fa