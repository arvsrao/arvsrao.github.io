---
layout: post
title: 3 Points Make a Circle
date:   2017-06-30
comments: true
category: mathematics
tags: applied topology, SymPy
---

While learning about Voronoi diagrams from [Computational Geometry][1], I had trouble justifying a single statement from a proof regarding the complexity ( as a function of $n$ sites ) of Voronoi diagrams. For completeness I'll restate the theorem here.

<p><strong>Theorem. </strong><em> For $n \geq 3$, the number of vertices in the Voronoi diagram of a set of $n$ point sites in the plane is at most $2n-5$ and the number of edges is at most $3n-6$.
</em></p>

To establish the stated bounds, the proof hinges on the constancy of the [*Euler's characteristic*][2] of graphs (that embed in $S^2$) and every vertex in the Voronoi diagram has *degree* at least three. Really? At the point in the proof when this fact is invoked we know that all the $n$ sites are not colinear; so given any pair of sites there's a third site that does not lie on the line passing through them. Three points induce a vertex. But why?? Voronoi vertices have a specific meaning/interpretation; they are equidistant from sites, which means that a Voronoi vertex is the center of circle that passes through at least three sites. <!--more-->

Which, to me, begs the question: *Is it always possible to find a circle that passes through three non-colinear points in the plane?*

Well it's **true**. Up to rotation and scaling the three given points can be positioned like so in the picture below.

<figure>
<div align="center">
	<img src = "/assets/3-points-make-a-cirle/triangle.jpeg">
</div>
<figcaption> Figure #1. 3 non-colinear points in the plane. </figcaption>  
</figure>

Edges $AB$ and $BC$ each have a line that bisects them; because the points form a proper triangle, these bisectors intersect.

<figure>
<div align="center">
	<img src = "/assets/3-points-make-a-cirle/bisectors.jpeg">
</div>
<figcaption> Figure #2. Bisectors of $AB$ and $BC$ intersect at a single point. </figcaption>  
</figure>


Voila! The intersection of the two bisectors is the center of a circle which passes through $A$, $B$, and $C$. The picture below shows the circle segment I constructed with a compass.

<figure>
<div align="center">
	<img src = "/assets/3-points-make-a-cirle/circle-sln.jpeg">
</div>
<figcaption> Figure #3. Compass constructed circle segment through $A$, $B$, and $C$. The circle is centered at the intersection of the dashed lines. </figcaption>  
</figure>

The circle segment above looks really good. Just a bit off the points $A$, $B$, and $C$; but all equally so. This is a proof by compass and ruler construction, and an elegant one at that. The alternative would be to compute the intersection of the bisectors in terms of coordinates and then verify a circle based there passes through all the points. [As a check I did just that][3] with the help of [SymPy][4], a wonderful symbolic manipulation library. I drew Figure #4 below to help read [the gist][3]. When I ran [the code][3], I showed, specifically, $d0 = d1 = d2$. Therefore, the circle of radius $d0$ passes through points $A$, $B$, and $C$.

<figure>
<div align="center">
	<img src = "/assets/3-points-make-a-cirle/triangle_pts_annotated_for_code.jpg">
</div>
<figcaption> Figure #4. Reference figure for <a href="https://gist.github.com/arvsrao/1d3895013fa2a87b45396676c8f508d0">gist</a> </figcaption>  
</figure>


[1]: https://www.amazon.de/Computational-Geometry-Applications-Mark-Berg/dp/3540779736
[2]: http://www.math.caltech.edu/%7E2014-15/2term/ma006b/09%20Planar2.pdf
[3]: https://gist.github.com/arvsrao/1d3895013fa2a87b45396676c8f508d0
[4]: http://docs.sympy.org/latest/index.html
