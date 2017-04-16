---
layout: post
title: Parametrizing Rigid Motion Spaces
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

Applying **Lemma A** to $A \in SO(3)$, $\det(A) = 1 \times \lambda_2 \lambda_3 = 1$. Incidently, $A$ is [diagonalizable, because it is normal][5]. The immediate implication is that both eigenvalues are unit complex numbers and conjugates of each other; in general, the eigenvalues of any rotation are $1, \omega, \bar{\omega}$, where $\omega \bar{\omega} = 1$. In lay terms this means that $A \in SO(3)$ is a rotation of $\mathbb{R}^3$ about an axis by some fixed angle. Furthermore, we can decompose $A$ so that its axis of rotation is rotated up to the $z-$axis by some $P^T \in SO(3)$, followed by a rotation about the $z-axis$ by some angle $\theta$, then the $z$-axis is rotated back to the original axis of rotation by $P$. 

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
	P = R_{y}R_{x} \quad \text{where} \

	R_x = \begin{pmatrix}
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

It should be clear that $R_x,\ R_y,\ R_z$ generate $SO(3)$, and that angles $\theta, \ \phi, \ \alpha$ parametrize $SO(3)$. Said differently, there's a continuous map from the flat 3-torus onto (read surjective) $SO(3)$.

$$
\mathbb{T}^3 \longrightarrow SO(3).
$$

Continuous yes, but it isn't full rank everywhere; and hence not locally homeomorphic everywhere. With the aid of [SymPy][6] the listing below verifies this.

	from sympy import *

	so3Coeff = lambda A : [A[0,1], A[0,2], A[1,2]]

	theta = Symbol('theta', real=true)
	alpha = Symbol('alpha', real=true)
	phi = Symbol('phi', real=true)

	rz = Matrix([[cos(theta), -sin(theta),0],[sin(theta), cos(theta), 0],[0,0,1]])
	rx = Matrix([[1,0,0],[0,cos(phi), -sin(phi)],[0,sin(phi), cos(phi)]])
	ry = Matrix([[cos(alpha), 0, -sin(alpha)],[0,1,0],[sin(alpha), 0, cos(alpha)]])

	P = rx *ry
	A = trigsimp(P* rz* P.transpose())

	dA_dtheta = trigsimp(diff(A,theta))
	dA_dphi = trigsimp(diff(A,phi))
	dA_dalpha = trigsimp(diff(A,alpha))
	dA = Matrix([so3Coeff(dA_dtheta), so3Coeff(dA_dphi), so3Coeff(dA_dalpha)]).transpose()

	# so that A is Not a local homeomorphism.
	assert det(dA.subs(theta, 0)) > 0, "dA not full rank @(0, phi, alpha) !!"

And evaluating the derivative at $\theta = 0$ gives, 

	In [116]: dA.subs(theta,0)
	Out[116]:

$$
    dA = \begin{pmatrix}
	-cos(\alpha)cos(\phi) & 0 & 0 \\
	-sin(\phi)cos(\alpha) & 0 & 0  \\
	\sin(\alpha) & 0 & 0 \\
	\end{pmatrix}
$$

Though its clear that $\det(dA) = 0$, [SymPy][6] can calculate the determinant for us.

	In [117]: det(dA.subs(theta,0))
	Out[117]: 0



[1]: https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h
[2]: https://nifti.nimh.nih.gov/nifti-1/documentation/faq#Q17
[3]: https://www.cbica.upenn.edu
[4]: https://en.wikipedia.org/wiki/Euler%27s_rotation_theorem#Euler.27s_theorem_.281776.29
[5]: https://en.wikipedia.org/wiki/Normal_matrix
[6]: http://docs.sympy.org/latest/index.html

























