---
layout: post
title: Counting Matrices
category: mathematics 
comments: true
tags: puzzles
---

Counting problems abound in mathematics. Often, they are easy to state, but hard to solve. Being easy to understand is what makes them so attractive, and that much more vexing when one gets stuck trying to solve them. Here's a matrix counting problem I recently encountered.

## Problem:
*How many $N$ by $N$ matrices with entries $ 0 $ or $1$, and odd row and column sums, are there?*

What do these matrices look like? Let $A = [a_{ij}]$. For example <!--more-->

$$
	A = \begin{pmatrix}
		0  & 1  & \cdots & 1 \\
		1  & 1 &  \cdots & 0 \\
		\vdots & \vdots & \ddots & \vdots \\
		1  & 1 &  \cdots & 0 \\
	\end{pmatrix}.		
$$

Define the column and row sums respectively

$$
 	x_i = \sum_{j} a_{ji} \quad \text{and} \quad y_j = \sum_{i} a_{ji}.
$$

Then constraint on the row and column sums can be stated as  

$$
	x_i \mod 2  = 1 \text{ for each } i \quad \& \quad y_j \mod 2 = 1 \text{ for each } j.
$$

Starting with a blank $N \times N$ matrix, populate the $N-1 \times N-1$, $(1,1)$-minor with any matrix with zeros and ones: 

$$
	A = \begin{pmatrix}
		0  & 1  & \cdots & 1                         & y_1  \\
		1  & 1 &  \cdots & 0                         & y_2  \\
		\vdots & \vdots & \ddots & \vdots   & \vdots  \\
		1  & 1 &  \cdots & 0                         & y_{N-1}  \\
		x_1 & x_2  & \cdots  & x_{N-1}                     & ?   \\		
	\end{pmatrix}
$$

Now, no matter what the parity of the rows and columns in the $N-1 \times N-1$ minor, we can find $x_i$ and $y_j$ so that the parity of each row and column sum, in the larger matrix, is odd. The only thing left to consider is the uniqueness of $a_{NN} = ?$. Right. It's totally conceivable that

$$
	\sum_{i} x_i \mod 2 \neq \sum_{j} y_j \mod 2. 
$$ 

However, this in fact doesn't happen. 
<p><strong>Lemma. </strong> <em>Suppose $A$ is a matrix of zeros and ones. Let $x_i$ and $y_j$ be the bit-wise complement ( $0 \mapsto 1$ and $1 \mapsto 0$) of the $i$th columns and $j$th rows, respectively. Then,

$$
	\sum x_i \equiv \sum y_i  . 
$$
</em></p>

<p><em>proof:</em></p>

In words, the sums of ${x_i}$ and ${y_j}$ are both the sum of all elements of $A$ modulo $2$, just order differently.

$$
\begin{align*}
	\Big( \sum x_i \Big) \mod 2 = &  \sum_{i} \Big(\Big(\sum_{j} a_{ji}\Big) \mod 2\Big) \mod 2 \\
								= &  \Big( \sum_{i,j} a_{ji} \Big) \mod 2. \\  
\end{align*}
$$

Which is the same as the bit-wise sum of the $y_i$'s

$$
\begin{align*}
	\Big( \sum y_i \Big) \mod 2 = &  \sum_{j} \Big(\Big(\sum_{i} a_{ji}\Big) \mod 2\Big) \mod 2 \\
								= &  \Big( \sum_{i,j} a_{ji} \Big) \mod 2. \\  
\end{align*}
$$

And we get, 

$$ 
	\sum x_i  \equiv \sum y_j 
$$

<div align="right">
	<p><em>q.e.d.</em></p>
</div>
With the above lemma in hand, we know that $a_{NN}$ is uniquely determined. Moreover, 

$$ 
	a_{NN} \equiv \Big( 1  + \sum_{i,j} a_{ij} \Big) \mod 2     
$$

What we've shown is that our initial construction/choice of the $N-1 \times N-1$ minor uniquely determines the remaining entries of the larger matrix, the $y_i$'s, $x_i$'s, and $a_{NN}$. So, the count we want is equal to the number of $N-1 \times N-1 $ matrices with zeros and ones:

$$
	\boxed{ \mathbf{2^{(N-1)^2} }}
$$