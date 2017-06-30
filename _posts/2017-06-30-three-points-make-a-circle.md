---
layout: post
title: 3 Points Make a Circle
date:   2017-06-30
comments: true
category: mathematics
tags: applied topology, SymPy
---

While learning about Voronoi diagrams from [Computational Geometry][1], I had trouble justifying a single statement a proof regarding the complexity of Voronoi diagrams. For completeness I'll restate the theorem here.

<p><strong>Theorem. </strong><em> For $n \geq 3$, the number of vertices in the Voronoi diagram of a set of $n$ point sites in the plane is at most $2n-5$ and the number of edges is at most $3n-6$.
</em></p>

To establish the stated bounds, the proof hinges on the constancy of the [*Euler's characteristic*][2] of graphs (that embed in $S^2$) and every vertex in the Voronoi diagram has *degree* at least three. Really? At the point in the proof when this fact is invoked we know that all the $n$ sites are not colinear; so given any pair of sites there's a third site that does not lie on the line passing through them. Three points induce a vertex, but why?? Voronoi vertices have a specific meaning/interpretation; they are equidistant from sites, which means that a Voronoi vertex is the center of circle that passes through at least three sites.

Which to me begs the question: *Is it possible to find a circle that passes through any three non-colinear points in the plane?*

Well it's **true**. Up to rotation and scaling three given points can be positioned like

![helpful graphic]({{ site.url }}/assets/triangle.jpeg)

Draw imaginary lines bisecting the edges $AB$ and $BC$. Because our points form a proper triangle, these bisectors intersect.

![helpful graphic]({{ site.url }}/assets/bisectors.jpeg)

Voila! The intersection of the two bisectors is the center of a circle which passes through $A, B,C$.

![helpful graphic]({{ site.url }}/assets/circle-sln.jpeg)

[1]: https://www.amazon.de/Computational-Geometry-Applications-Mark-Berg/dp/3540779736
[2]: http://www.math.caltech.edu/%7E2014-15/2term/ma006b/09%20Planar2.pdf
