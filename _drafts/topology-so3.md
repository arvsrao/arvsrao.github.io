---
layout: post
title: Topology of $SO(3)$
comments: true
category: mathematics
tags: applied topology, SymPy
---

Pointwise and locally $SO(3)$ looks like a product, but actually it fibers over $\mathbb{RP}^2$ with $S^1$ fibers.

$$
SO(3) \xrightarrow{\quad \pi \quad} \mathbb{RP}^2 \quad \text{where} \quad \pi(\theta, [\vec{n}]) =[\vec{n}] \in \mathbb{RP}^2
$$

Choosing a small enough open set, $U_{[\vec{n}]} \subset \mathbb{RP}^2$, $\pi$ factors into a local homeomorphism into the product $S^1 \times U_{[\vec{n}]}$, and a projection of the local product into the [open set][8], $U_{[\vec{n}]}$. Globally, $SO(3)$ isn't a product, because $(\theta, \vec{n}) \sim (-\theta, -\vec{n})$ are the same rotation. However, we can take the product $S^1 \times U_{[\vec{n}]}$ and map it into $S^3/\sim \ \cong\ \mathbb{RP}^3$ like so

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
