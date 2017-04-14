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

Lenorad Euler, [so long ago][4], discovered that if $A \in SO(3)$ fixes a vector, this is called the *axis of rotation*.

<p><strong>Lemma. A</strong> <em>Suppose $A \in SO(N)$ where $N$ is odd. Then $\exists x \in \mathbb{R}^N$ so that $Ax = x$. $\lambda = 1$ is an eigenvalue of $A$. 
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


[1]: https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h
[2]: https://nifti.nimh.nih.gov/nifti-1/documentation/faq#Q17
[3]: https://www.cbica.upenn.edu
[4]: https://en.wikipedia.org/wiki/Euler%27s_rotation_theorem#Euler.27s_theorem_.281776.29