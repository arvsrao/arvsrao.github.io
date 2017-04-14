---
layout: post
title: Parametrizing Rigid Motion Spaces
category: mathematics 
tags: applied topology, SymPy
---

3D medical images in the NifTI format, represent MRI acquisitions of some anatomy, like a human brain or heart. When I was a postdoc @UPenn [my lab][3] was primarly interested in studying brains. An image associates grayscale values ( in the simplest case ) to coordinates in a discrete coordinate system $(i,j,k)$, which describes voxel locations. And for reasons best explained by [NifTI FAQ][2] it's useful/important to align the acquired image to some other coordinate system. This alignment is stored in the image header, as a rigid motion plus an offset. Here's a bit of [NifTI documentation][1] motivating the need to keep the aligment.

	This method can also be used to represent "aligned"
	coordinates, which would typically result from some post-acquisition
	alignment of the volume to a standard orientation (e.g., the same
	subject on another day, or a rigid rotation to true anatomical
	orientation from the tilted position of the subject in the scanner).

The NifTI standard allows for orientation reversing transforms, but in this post I focus on *proper* rotations. These rigid motions must preserve volume and orientation; rigidity necessitate linearity. Being a geometric property, volume is preserved when the transformation is an isometry; for some matrix $A$, we require $A A^T = I$. Moreover, orientation preservation means $\det(A) > 0$. The intersection all these requirements means. 


$$A \in SO(3) = \{ B \in Mat(\mathbb{R},3) \ | \ BB^T =I \, \ \det(B)=1 \}$$

And the final affine transform that rotations and translates image coordinates is

$$
\begin{equation*}
    \vec{v} = A * \vec{x} + \vec{q},  \quad \text{where } A \in SO(3), \ \vec{q}, \vec{x} \in \mathbb{Z}^3 
\end{equation*}
$$

[1]: https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h
[2]: https://nifti.nimh.nih.gov/nifti-1/documentation/faq#Q17
[3]: https://www.cbica.upenn.edu