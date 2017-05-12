---
layout: post
title: Parametrizing Rigid Motion Spaces
date:   2017-07-17 16:16:01 -0600
comments: true
category: mathematics
tags: applied topology, SymPy
---

3D medical images in the NifTI format store data from MRI acquisitions of some anatomy, like a human brain or heart. When I was a postdoc @UPenn [my lab][3] was primarily interested in studying brains. Each image associates grayscale values ( in the simplest case ) to coordinates in a discrete coordinate system $(i,j,k)$, which describes voxel locations. And for reasons best explained by [NifTI FAQ][2] it's useful/important to align the acquired image to some other coordinate system. This alignment is stored in the image header, as a rigid motion plus an offset. Here's a bit of [NifTI documentation][1] motivating the need to keep the aligment.

	This method can also be used to represent "aligned"
	coordinates, which would typically result from some post-acquisition
	alignment of the volume to a standard orientation (e.g., the same
	subject on another day, or a rigid rotation to true anatomical
	orientation from the tilted position of the subject in the scanner).

The NifTI standard allows for orientation reversing transforms, but in this post I focus on *proper* rotations. These rigid motions must preserve volume and orientation; rigidity necessitate linearity. Being a geometric property, volume is preserved when the transformation is an isometry; for some matrix $A$, we require $A A^T = I$. Moreover, orientation preservation means $\det(A) > 0$. The intersection all these requirements means.


$$A \in SO(3) = \{ B \in Mat(\mathbb{R},3) \ | \ BB^T =I \, \ \det(B)=1 \}$$

And the final affine transform that rotates and translates image coordinates is

$$
\begin{equation*}
    \vec{v} = A * \vec{x} + \vec{q},  \quad \text{where } A \in SO(3), \ \vec{q}, \vec{x} \in \mathbb{Z}^3
\end{equation*}
$$

Getting to the point, $A$ isn't what gets stored. Rather four real numbers representing a quaternion. So there is a map

$$
	\ A \mapsto (a, b, c, d) \in \mathbb{H} \quad \text{where } a^2+b^2+c^2+d^2=1
$$

We can, it seems, represent a rotation by a point in $S^3$. Pretty amazing:) But what's going on here? To understand more we need to explore the structure of $SO(3)$ a bit.

Lenorad Euler, [so long ago][4], discovered that if $A \in SO(3)$ fixes a vector, which is called the *axis of rotation*.

<p><strong>Lemma. A</strong><em>Suppose $A \in SO(N)$ where $N$ is odd. Then $\exists x \in \mathbb{R}^N$ so that $Ax = x$. $\lambda = 1$ is an eigenvalue of $A$.
</em></p>
<p><em>proof:</em></p>
Consider $A - I$. Because $N$ is odd $\det(-(A-I)) = -\det(A-I)$. Then

$$
\begin{align*}
    \det(A-I) & = \det(A - AA^T) = \det(A) \times \det(I - A^T)   \\
              & = \det(-(A^T - I)) \\
              & = -\det((A-I)^T) \\
              & = - \det(A -I) \\          
\end{align*}
$$

Consequently, $\det(A-I) = 0$ and $A$ has a non-trival kernal.     
<div align="right">
	<p><em>$\Box$</em></p>
</div>

Applying **Lemma A** to $A \in SO(3)$, $\det(A) = 1 \times \lambda_2 \lambda_3 = 1$. Incidently, $A$ is [diagonalizable, because it is normal][5]. The immediate implication is that both eigenvalues are unit complex numbers and conjugates of each other; in general, the eigenvalues of any rotation are $1, \omega, \bar{\omega}$, where $\omega \bar{\omega} = 1$. In lay terms this means that $A \in SO(3)$ is a rotation of $\mathbb{R}^3$ about an axis, $\vec{n} \in S^2$ by some fixed angle, $\theta \in S^1$. Actually, $-\vec{n}$ and $\vec{n}$ describe the same axis (or plane), so $SO(3)$ fibers over $\mathbb{RP}^2$ with $S^1$ fibers.

$$
SO(3) \xrightarrow{\quad \pi \quad} \mathbb{RP}^2 \quad \text{where} \quad \pi(\theta, \vec{n}) =[\vec{n}] \in \mathbb{RP}^2
$$

Choosing a small enough open set, $U_{[\vec{n}]} \subset \mathbb{RP}^2$, $\pi$ factors into a local homeomorphism into the product $S^1 \times U_{[\vec{n}]}$, and a projection of the product into the [open set][8]. Globally, $SO(3)$ isn't a product, because $(\theta, \vec{n}) \sim (-\theta, -\vec{n})$ are the same rotation. However, we can take the product $S^1 \times U_{[\vec{n}]}$ and map it into $S^3/\sim \ \cong\ \mathbb{RP}^3$ like so

$$
(\theta, \vec{n}) \longmapsto (\cos(\frac{\theta}{2}) \vec{n}, \sin(\frac{\theta}{2}))  \in S^{3}.\\
$$

Antipodes are preserved, so the map is well-defined.

$$
\begin{gather*}
	(\theta, \vec{n})   \longmapsto \Big(\cos(\theta / 2) \vec{n}, \sin(\frac{\theta}{2}))  \in S^{3}\\
	(-\theta, -\vec{n}) \longmapsto \Big(-\cos(\frac{\theta}{2}) \vec{n}, -\sin(\frac{\theta}{2})).
\end{gather*}
$$


Furthermore, we can decompose $A$ so that its axis of rotation is rotated up to the $z-$axis by some $P^T \in SO(3)$, followed by a rotation about the $z-axis$ by some angle $\theta$, then the $z$-axis is rotated back to the original axis of rotation by $P$.

$$
	A = P R_{z} P^T \quad \text{where} \quad

	R_z = \begin{pmatrix}
		\cos(\theta) & -\sin(\theta) & 0 \\
		\sin(\theta) &  \cos(\theta) & 0 \\
		0 & 0 &  1  \\
	\end{pmatrix}.
$$

$P$, itself, can be thought of as a rotation of $A$'s axis of rotation into the $zx$-plane, followed by rotation about the $y$-axis taking the axis of rotation into the $z$-axis.

$$
	P = R_{z}R_{y} \quad \text{where} \

	R_z = \begin{pmatrix}
		0 & \cos(\phi) & -\sin(\phi) \\
		0 & \sin(\phi) &  \cos(\phi) \\
		1 & 0 &  0  \\
	\end{pmatrix}

	\ \text{and} \

    R_y = \begin{pmatrix}
		\cos(\alpha) & 0 & -\sin(\alpha) \\
		0 & 1 &  0  \\
		\sin(\alpha) & 0 & \cos(\alpha) \\
	\end{pmatrix}

$$

Similarily, rotations about the $x$-axis can be parametrized by $S^1$, $R_x(\beta)$. It should be clear that $R_x,\ R_y,\ R_z$ generate $SO(3)$, and that angles $\theta, \ \phi, \ \alpha$ parametrize $SO(3)$. Said differently, there's a continuous map from the flat 3-torus onto (read surjective) $SO(3)$.

$$
\mathbb{T}^3 \xrightarrow{\quad f \quad} SO(3).
$$

Lets investigate this map by representing elements of $SO(3)$ by an axis, $x \in S^2$ and an angle of rotation, $\theta$.

$$

f(\theta, \alpha, \phi) = (\theta, \cos(\alpha) cos(\phi), \cos(\alpha) \sin(\phi) , sin(\alpha))

$$

The listing below implements the above map.

	from sympy import *

	theta = Symbol('theta', real=true)
	alpha = Symbol('alpha', real=true)
	phi = Symbol('phi', real=true)

	f = Matrix([theta, cos(alpha)*cos(phi), cos(alpha)*sin(phi), sin(alpha)])

Continuous yes, but $f$ isn't full rank everywhere; and hence not locally homeomorphic everywhere. To prove this compute the derivative, $df$. We do this with the aid of [SymPy][6].

	df_dtheta = map(lambda ll: ll.pop(), trigsimp(diff(f,theta)).tolist())
	df_dphi = map(lambda ll: ll.pop(), trigsimp(diff(f,phi)).tolist())
	df_dalpha = map(lambda ll: ll.pop(), trigsimp(diff(f,alpha)).tolist())
	df = Matrix([df_dtheta, df_dphi, df_dalpha])

	#f is Not a local homeomorphism.
	df.subs(alpha, 0)

And evaluating the derivative at $\alpha = \frac{\pi}{2} $ gives,

	In [63]: df.subs(alpha,pi/2)
	Out[63]:
	Matrix([
	[1,         0,         0, 0],
	[0,         0,         0, 0],
	[0, -cos(phi), -sin(phi), 0]]) ,

And $df$ isn't full rank; $f$ isn't a parametrization. There is only one degree of freedom, at this point. Evaluating $f$ at $\alpha = \frac{\pi}{2}$ gives $(\theta,0,0,1)$, this $phenomenon is called [gimbal lock][7]. We haven't stricitly translated gimbal motion into $XYZ$-rotations as in [ref][7], but nonetheless there maps from $\mathbb{T}^3$ fail to cover $\mathbb{RP}^3$. Its worth asking if there is any


[1]: https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h
[2]: https://nifti.nimh.nih.gov/nifti-1/documentation/faq#Q17
[3]: https://www.cbica.upenn.edu
[4]: https://en.wikipedia.org/wiki/Euler%27s_rotation_theorem#Euler.27s_theorem_.281776.29
[5]: https://en.wikipedia.org/wiki/Normal_matrix
[6]: http://docs.sympy.org/latest/index.html
[7]: https://en.wikipedia.org/wiki/Gimbal_lock#Loss_of_a_degree_of_freedom_with_Euler_angles
[8]: https://en.wikipedia.org/wiki/Fiber_bundle
