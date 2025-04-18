---
title: Rotate Homogeneous Polynomials
layout: post
comments: true
category: mathematics 
tags: computer graphics, linear algebra
typora-root-url: ../
---

Several years ago here on my blog I presented an [algorithm for rotating homogeneous polynomials][post] ( in variables $x$, $y$, and $z$ ) by computing representations of $SO(3)$ on $\mathcal{P}_d$, homogeneous polynomials of degree $d$. These representations are matrices in $SO(\mathcal{P}_d)$ and are rotations of  $p \in \mathcal{P}_d$. While writing that [post][post] I implemented the [recursive algorithm][gist] in Python, but never visually demonstrated the rotation of harmonic homogeneous polynomials by representations on $\mathcal{P}_d$. Well, I finally got around to doing just that.

<!--more-->

On github I created a repo called [rotate_spherical_harmonics][project]. There are two scripts `harmonic-dim-2-comparison.py` and `harmonic-dim-3-comparison.py` demonstrating the effect of rotation by representations on $\mathcal{P}_2$ and $\mathcal{P}_3$, respectively, of randomly generated $SO(3)$ matrices on harmonic homogeneous polynomials:

1.  $xy$
2.  $x^2y - \frac{1}{3}y^3$

The generated figures are a visual check that the representations $\rho_d(A)$ indeed correspond to the rotations they are suppose to represent. Each figure is a side-by-side plot of a harmonic polynomial $p(x,y,z)$ in the standard x-y-z frame, and its rotation by representation $\rho_d(A)$. The colored arrows are the original and rotated frames, respectively. 

<span style="font-size: 20px; font-weight: bold"> On the Left </span>, 

* the <span style="color: red">red</span> arrow marks the positive $z$-axis.

* the <span style="color: CornflowerBlue ">blue</span> arrow marks the positive $y$-axis.

* the <span style="color: green">green</span> arrow marks the positive $x$-axis. 

Like colored arrows on the left map to like colored arrows on the right. For example, the <span style="color: red">red</span> arrow ($z$-axis) plotted on the left is rotated by $A$ to the <span style="color: red">red</span> arrow plotted on the right.

<span style="font-size: 20px;font-weight: bold">On the Right </span>, is a plot of $\rho_d(A)(p)$, the rotation of $p(x,y,z)$ by $\rho_d(A)$.

## Rotate $xy$ by $\rho_2(A)$ 

A simple example of a harmonic polynomial is $xy$. Using script `harmonic-dim-2-comparison.py` a representation on $\mathcal{P}_2$ of randomly generated $SO(3)$ matrix 

$$
A=
\begin{bmatrix}
0.357129979786826 && 0.866523063310198 && 0.348706120234463 \\
-0.619992791031964 && 0.499137036044723 && -0.605368613587527 \\
-0.698618004782196 && 0 && 0.715494852108765 \\
\end{bmatrix},
$$

with axis of rotation located at $\theta = 0.7734641469345384$ radians and $\phi = 5.234991577347525$ radians, was generated and applied to harmonic homogeneous polynomial $xy$. In the figure below, $xy$ is plotted on left in the standard frame, and on the right its rotation by $\rho_d(A)$ is plotted.

<figure>
<div align="center">
  <img src = "/assets/rotate-solid-harmonics/harmonic-dim-2-rotation.png">
</div>
  <figcaption align="left"> 
    On the left is a graph of spherical harmonic function $xy$ in the standard x-y-z frame. On the right is its rotation. The colored arrows are the original and rotated frames, respectively. The z-axis is the <span style="color: red">red</span> arrow, the y-axis is the <span style="color: blue">blue</span> arrow, and x-axis is the <span style="color: green">green</span> arrow. Like colored arrows on the left map to like colored arrows on the right.
  </figcaption> 
</figure>




## Rotate $x^2y - \frac{1}{3}y^3$ by $\rho_3(A)$

A less trivial example is harmonic polynomial $x^2y - \frac{1}{3}y^3$. Using script `harmonic-dim-3-comparison.py` a representation on $\mathcal{P}_3$ of randomly generated $SO(3)$ matrix 

$$
A = 
\begin{bmatrix}
-0.320757648736410 & -0.868123551589577 & -0.378782298890258 \\
0.561011986806716 & -0.496348163263952 & 0.662498340740323 \\
-0.763138310816768 & 0 & 0.646235188274153 \\
\end{bmatrix},
$$

with rotation axis located at $\theta = 0.8681555864627436$ radians and $\phi = 2.0901834326555337$ radians, was generated and applied to $x^2y - \frac{1}{3}y^3$. In the figure below, $x^2y - \frac{1}{3}y^3$ is plotted on left in the standard frame, and on the right its rotation by $\rho_d(A)$ is plotted.

<figure>
<div align="center">
  <img src = "/assets/rotate-solid-harmonics/harmonic-dim-3-rotation.png">
</div>
  <figcaption align="left"> 
    On the left is a graph of spherical harmonic function $x^2y - \frac{1}{3}y^3$ in the standard x-y-z frame. Its rotation by representation $\rho_d(A)$ is plotted on the right. The colored arrows are the original and rotated frames, respectively. The z-axis is the <span style="color: red">red</span> arrow, the y-axis is the <span style="color: blue">blue</span> arrow, and x-axis is the <span style="color: green">green</span> arrow. Like colored arrows on the left map to like colored arrows on the right. 
  </figcaption> 
</figure>

[post]: https://rao.im/mathematics/2019/10/25/compute-so3-repns/
[gist]: https://gist.github.com/arvsrao/637a6b6c8553d0f6ca7cc6a2884a56e2
[github]: https://github.com/arvsrao/rotate_spherical_harmonics
[project]: https://github.com/arvsrao/rotate_spherical_harmonics