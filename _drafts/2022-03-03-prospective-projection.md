---
layout: post
title: Perspective Projection 
comments: true
category: computer graphics
tags: computer graphics
typora-root-url: ../
---

![](/assets/pxfuel.com.jpeg)

The presentations of image projection, projection of a 3D scene to 2D, in books and on the web I have seen present perspective and orthographic projection without relating them. As a result the derivations of perspective projection matrix feel either overly complicated or completely lacking in detail--in some presentations the perspective projection matrix is simply just stated. At least at the level of formulas perspective and orthographic projection look similiar enough to believe perspective projection could be written in terms of orthographic projection. 

Here perspective projection is a projective transformation of the view frustum to the canonical view volume; and, abusing the term a bit, orthographic projection is an affine map from the orthographic view volume to the canonical view volume. Perspective and orthographic projection are technically methods of projecting points to screen, not really maps from the screen. I use these terms interchangeable throughout to refer to maps between [cuboids](https://en.wikipedia.org/wiki/Cuboid) and methods of projecting to the image plane.

<figure>
<div align="center">
	<img src = "/assets/pipeline.pdf">
</div>
<figcaption> Factoring the map from the frustum to the canonical view volume through the orthographic view volume. </figcaption>
</figure>

<!--more-->

In what follows I derive the perspective projection matrix by factoring it through the orthographic view volume. IMHO doing so leads to a simpler derivation of the perspective projection matrix.

## Perspective

Perspective in art and photography is about representing depth of 3D scenes in 2D. When thinking about perspective the first image that comes to mind, and it ought to be familiar to most people, is of railroad tracks running off into the distance. The tracks though parallel are rendered as angled toward each other such that they would eventually meet at some point behind the image plane called the *vanishing point*, or the *point at infinity*. Objects further away appear smaller than those closer to the eye. This is what the world looks like to us and cameras, since cameras are meant to capture the world as we see.

In a [previous post](/2022-02-26-camera-matrix.html) I dervied the camera matrix, a projective transformation of a 3D scene in front of a camera looking down the negative $z$-axis onto an image plane located behind the camera center at $z = F$. The camera projection renders the scene in perspective on the image plane. Scene points are projected onto the image plane by dividing their $x$ and $y$ coordinates by the depth coordinate $z$. This *homogenous division* scales points by there depth; consequently, scene points further away are projected to points on the image closer the image center. As a result lines (e.g. railroad tracks) in the scene which have depth will naturally angle inward, toward the image plane center; and objects in the scene will appear smaller if located further away from the origin.
$$
P = 
\begin{bmatrix}
F & 0 & 0 & 0 \\
0 & F & 0 & 0 \\
0 & 0 & F & 0 \\
0 & 0 & 1 & 0 \\
\end{bmatrix}
$$
is a basic perspective projection and it is defined on $\mathbb{A}^3 \subsetneq \mathbb{RP}^3$, the affine space of $\mathbb{RP}^3$. $P$ acts on scene points like so:
$$
\begin{bmatrix}
F & 0 & 0 & 0 \\
0 & F & 0 & 0 \\
0 & 0 & F & 0 \\
0 & 0 & 1 & 0 \\
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z \\
1 \\
\end{bmatrix}
=
\begin{bmatrix}
Fx \\
Fy \\
Fz \\
z \\
\end{bmatrix}
\sim
\begin{bmatrix}
Fx / z \\
Fy / z\\
F \\
1 \\
\end{bmatrix}.
$$

$P$ copies the $z$ cooridinate into the $w$ coordinate, and after homogenous division lines are projected onto the $z = F$ plane of $\mathbb{A}^3$. 

$P$ renders the entire scene in perspective on the image plane even though we humans, and cameras, can not perceive the whole scene. This limitation or *field of view* is modeled by a 3D view volume in front of the camera. Points and triangles outside the bounding region are filtered out before projection to the screen. 

Filtering out points and triangles outside the view volume potentially eliminates a lot of extra work and unwanted artifacts. For instance, without a near plane the rendered output might exhibit [z-fighting][2]. Choosing the near plane so it is not too close to the eye (at a distance smaller than floating point precision), or keeping the near and far plane not too far apart reduces the chance of [z-fighting][2].

Presentations of image projection in books and course notes/videos focus on two main types of view volumes: the *view frustum* and the *orthographic view volume*.

#### View Frustum

The view frustum is a pyramidal solid primarly defined by the dimensions of its near face at $z = -n$ and the location of its far face at $z = -f$. The sides are defined by projective lines through the edges of the near face. The view frustum is depicted below in Figure #1.

<figure>
<div align="center">
	<img src = "/assets/frustum.png">
</div>
  <figcaption> Figure #1. The view frustum. <a href="http://www.songho.ca/opengl/">Image courtesy of Song Ho Ahn</a>. </figcaption>
</figure>

A basic perspective projection
$$
P = 
\begin{bmatrix}
n & 0 & 0 & 0 \\
0 & n & 0 & 0 \\
0 & 0 & n & 0 \\
0 & 0 & -1 & 0 \\
\end{bmatrix}
$$
projects points in the frustum onto the near face, at $z=-n$, along lines through the origin. $P$ flattens the frustum onto the near face, eliminating the depth information. To facilate [$z$-buffering](https://de.wikipedia.org/wiki/Z-Buffer), an occlusion resolution technique, $P$ can and is [later](#map-to-box) altered to retain at least the relative ordering of depth values.

 #### Orthrographic View Volume

The [orthrographic view volume][1] is a cuboid solid and like the view frustum its shape is determined by the dimensions of the near face at $z=-n$  and the location of the far face at $z = -f$. It's depicted below in Figure #2. 

In contrast to the perspective model the orthographic model supposes light travels in lines perpendicular to the image plane. Consequently, parallel lines in the scene stay parallel in the image.

<figure>
<div align="center">
	<img src = "/assets/orthographic_volume.png">
</div>
<figcaption> Figure #2. The orthographic view volume. <a href="http://www.songho.ca/opengl/">Image courtesy of Song Ho Ahn</a>. </figcaption>
</figure>

Let the near face be the image plane, then an orthographic projection sends points in the cuboid volume along perpendicular lines to the near face; essentially the $z$-coordiante is erased and the $x,y$ coordinates are translated to the near face. When formulated as a projective matrix acting on $\mathbb{A}^3$ a basic orthographic projection is
$$
O =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & -n \\
0 & 0 & 0 & 1 \\
\end{bmatrix}.
$$
The exact matrix formulation is not so important, because when implemented the $x$ and $y$.

#### Canonical View Volume

To speed the clipping proccess the bounding volume is usually mapped to the *canonical view volume*, a cube centered at the origin depicted in Figure #3. Mapping to a canonical view volume allows for [simpler hardware][3]. Throughout this post I use the OpenGL definition of the canonical frame.  

<figure>
<div align="center">
	<img src = "/assets/canonical_volume.png">
</div>
<figcaption> Figure #3 Standard clipping volume. <a href="http://www.songho.ca/opengl/">Image courtesy of Song Ho Ahn</a>. </figcaption>
</figure>


The canonical view volume is also an orthographic volume; so when points are in the canonical frame they are orthographically projected to the screen. In the OpenGL standard the screen is located at $z = 1$. 

## Mapping the Orthographic View Volume to the Canonical View Volume

The [orthrographic view volume][1] is defined by planes: $z=-f$,  $z=-n$, $y=t$, $y=b$, $x=l$, and $x=r$. Here $l=$left, $r=$right, $t=$top, $b=$bottom, $n=$near,  and $f=$far; necessarily $r>l$, $t >b$, and $f > n$.

<figure>
<div align="center">
	<img src = "/assets/orthographic_to_canonical.pdf">
</div>
<figcaption> Figure #4. Orthographic view volume. The eye is the blue dot at the origin. </figcaption>
</figure>
Since both volumes are the same shape, with different dimensions and centers, an affine map converts the orthographic volume to the canonical volume. Specifically, the map <u>translates</u> the orthographic view center to the origin, then <u>scales</u> all the axises so the box dimension are uniform and side length is 2. For some frameworks like Vulkan the camera in the target coordinate system looks down the positive $z$-axis. Therefore, the projection must also flip the $z-$axis.

$$
\begin{align}
O_{proj}
&=
\underbrace{
\begin{bmatrix}
\frac{2}{r-l} & 0             & 0               & 0 \\
0             & \frac{2}{t-b} & 0               & 0 \\
0             & 0             & -\frac{2}{f-n}  & 0 \\
0             & 0             & 0               & 1 \\
\end{bmatrix}
}_{\text{scaling}}
\underbrace{
\begin{bmatrix}
1 & 0 & 0 & -\frac{r+l}{2} \\
0 & 1 & 0 & -\frac{t+b}{2} \\
0 & 0 & 1 &  \frac{f+n}{2} \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
}_{\text{translation}}
\\
&= 
\begin{bmatrix}
\frac{2}{r-l} & 0             & 0               &  \frac{l+r}{l-r} \\
  0           & \frac{2}{t-b} & 0               &  \frac{b+t}{b-t} \\
  0           & 0             & -\frac{2}{f-n}  & -\frac{f+n}{f-n} \\
  0           & 0             & 0               &         1        \\
\end{bmatrix}
\\
\end{align}
$$
is the *orthographic projection* expressed a projective transformation.

<a name="map-to-box"></a>

## Projecting the Frustum to the Orthographic Volume

Consider a $yz$-cross section of the frustum. Now, imagine collapsing the top and bottom of the frustrum until the frustum section looks rectangular. Deforming a frustum section in this way should straighten out lines passing through both the near face, $z = -n$, and the origin. A frustum section is draw on the left side of Figure. #3. The green arrow is a segment of a line that passes through the origin and the near face, and it is mapped to the horizontal green arrow drawn in the rectangle on right. 

<figure>
<div align="center">
	<img src = "/assets/yz_cross_section.jpg">
</div>
<figcaption> Figure #5. Deforming the frustum to a box. </figcaption>
</figure>
Naturally, both arrows intercept the near face at the same point. Therefore, the horizontal green arrow is constructed by projecting the sloping green arrow in the frustum (on the left in Figure #3) to the near face. The $y$-coordinate of the near face intercept is then the  $y$-value of the mapped horizontal green arrow (on the right in Figure #3). Since any point in the interior of the frustum section can be projected to the near face, the $y$-coordinate of every point in the frustum is mapped by the deformation to its projection on the near face; specifically, if $(y,z)$ is a point in the frustum section, then  $y \mapsto \frac{-ny}{z}$ on the near face. A derivation of the projected $y$ value can be found in my previous post on [camera matrices]({% post_url 2022-02-26-camera-matrix %}).

Moving from heuristic to implememation: Because the deformation includes a projection of the $y$ coordinate, it can be conceived of as projective transformation 
$$
M_{pp} = 
\begin{bmatrix}
n & 0  & 0 \\
0 & A  & B \\
0 & -1 & 0 
\end{bmatrix},
$$
where $A$ and $B$ are unknowns. Originally, I thought $z \mapsto z$ but constructing a linear map which is the identity on $-n < z < -f$ after division by $-z$ is only possible if $z$ is squared. Not a linear operation. While the deformation isn't in general the identity on $z$, it must fix points on the near face,
$$
\begin{equation}
\begin{bmatrix}
n & 0  & 0 \\
0 & A  & B \\
0 & -1 & 0 
\end{bmatrix}
\begin{bmatrix}
y \\
-n \\
1 \\
\end{bmatrix}
=
\begin{bmatrix}
ny \\
-n \cdot n \\
n \\
\end{bmatrix}
\sim
\begin{bmatrix}
 y \\
-n \\
1 \\
\end{bmatrix}
\end{equation}.
$$
It must also fix the $z$-coordinate of points on the far face,

$$
\begin{equation}
\begin{bmatrix}
n & 0  & 0 \\
0 & A  & B \\
0 & -1 & 0 
\end{bmatrix}
\begin{bmatrix}
y \\
-f \\
1 \\
\end{bmatrix}
=
\begin{bmatrix}
ny \\
-f \cdot f \\
f \\
\end{bmatrix}
\sim
\begin{bmatrix}
 \frac{ny}{f} \\
-f \\
1 \\
\end{bmatrix}
\end{equation}.
$$

Both of these boundary conditions can be reduced to a system of equations,
$$
\begin{cases}
-fA + B &= -f^2\\
-nA + B &= -n^2. \\
\end{cases}
$$

Solving the system, $A = n+f$ and $B=nf$. 

The same derivation could have been made for the $xz$-cross section of the frustum without any change. Indeed, $x$ values of points in the frustum must also be projected to the near face independent of $y$ and $z$. Therefore, the deformation of the frustum to the orthographic volume is projective transform
$$
M_{pp} = 
\begin{bmatrix}
n & 0 & 0 &  0 \\
0 & n & 0 &  0 \\
0 & 0 & n+f & nf \\
0 & 0 & -1 & 0 \\
\end{bmatrix}.
$$

## Putting it All Together

<figure>
<div align="center">
	<img src = "/assets/pipeline.pdf">
</div>
<figcaption> Figure #6. Mapping the frustum to the canonical clipping volume. </figcaption>
</figure>
All the pieces are in place to describe perspective projection in a pipeline fashion. By which I mean a sequence of transformations, factoring throught the orthographic view volume. Finally, the full perspective projection matrix is
$$
\begin{align}
P_{proj} &= O_{proj} M_{pp} \\
&=
\begin{bmatrix}
\frac{2}{r-l} & 0 & 0     & \frac{l+r}{l-r} \\
  0 & \frac{2}{t-b}& 0    & \frac{b+t}{b-t} \\
  0 & 0  & -\frac{2}{f-n}  & -\frac{f+n}{f-n} \\
0             & 0             & 0             & 1 \\
\end{bmatrix}
\begin{bmatrix}
n & 0 & 0   &  0 \\
0 & n & 0   &  0 \\
0 & 0 & n+f & nf \\
0 & 0 & -1  &  0 \\
\end{bmatrix}\\
&=
\begin{bmatrix}
\frac{2n}{r-l} & 0  & \frac{r+l}{r-l} & 0 \\
  0 & \frac{2n}{t-b}& \frac{t+b}{t-b} & 0 \\
  0 & 0             & \frac{n+f}{n-f} & \frac{2nf}{n-f} \\
  0 & 0             & -1               & 0 \\
\end{bmatrix}.
\end{align}
$$

Though not at all necessary I carried out these calculations in a [Juypter notebook](/perspective-projection.html).   

#### Some References

* [View Transformation and Clipping Slides](http://www.inf.ed.ac.uk/teaching/courses/cg/lectures/cg6_2013.pdf)
* [Marburg Computer Graphics Slides][4]

[1]: https://en.wikipedia.org/wiki/Orthographic_projection	"ortho_projection"
[2]: https://www.unity3dtips.com/unity-z-fighting-solutions/
[3]: https://gamedev.stackexchange.com/questions/6279/what-is-the-purpose-of-the-canonical-view-volume
[4]: https://www.mathematik.uni-marburg.de/~thormae/lectures/graphics1/graphics_6_1_eng_web.html#1
[5]: http://www.songho.ca/opengl/gl_projectionmatrix.html
