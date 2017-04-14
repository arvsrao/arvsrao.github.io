---
layout: post
title: Representing Rigid Motions Without Locking Up 
category: mathematics 
tags: mathematics, topology
---

3D medical images in the NifTI format, represent MRI acquisitions of some anantomy, like a human brain or heart. When I was a postdoc @UPenn our lab was primarly interested in studying brains. The image stores the grayscale values ( in the simplest case ) in a discrete coordinate system $(i,j,k)$, which describes voxel locations. A for reasons best described by [NifTI FAQ][2] it's useful/important to align the acquired image to some other coordinate system. This alignment is stored in the image header, as rigid motion plus an offset. Here's a bit of [NifTI documentation][1] motivating the need to keep the aligment.

   This method can also be used to represent "aligned"
   coordinates, which would typically result from some post-acquisition
   alignment of the volume to a standard orientation (e.g., the same
   subject on another day, or a rigid rotation to true anatomical
   orientation from the tilted position of the subject in the scanner).

$$
\begin{equation*}
    \vec(v) = A * \vec(x) + \vec(q) \\
\end{equation*}
$$



[1] : https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h
[2] : https://nifti.nimh.nih.gov/nifti-1/documentation/faq#Q17