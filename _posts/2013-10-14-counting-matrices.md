---
layout: post
title: Counting Matrices
category: mathematics 
tags: puzzles
---

Counting problems abound in mathematics. Often, they are easy to state, but hard to solve. Being easy to understand is what makes them so attractive, and that much more vexing when one gets stuck trying to solve them. Here's a matrix counting problem I recently encountered.

<h2 id="problem">Problem:</h2>
<p><strong><em>How many $ N $ by $ N $ matrices with entries $ 0 $ or $1$, and odd row and column sums, are there?
</strong></em></p>	

What do these matrices look like? Let $A = [a_{ij}]:$ 

\[
	A = \begin{pmatrix}
		0  & 1  & \cdots & 1 \\
		1  & 1 &  \cdots & 0 \\
		\vdots & \vdots & \ddots & \vdots \\
		1  & 1 &  \cdots & 0 \\
	\end{pmatrix}		
\]

The row and column sums are odd: 
\[
	\sum_{i} a_{ij} \mod 2  \equiv 1  \quad \& \quad \sum_{j} a_{ij}\mod 2 \equiv 1 \text{ for each } i, j
\]

Starting with a blank $N \times N$ matrix, populate the $N-1 \times N-1$, $(1,1)$-minor with any matrix with zeros and ones: 

\[
	A = \begin{pmatrix}
		0  & 1  & \cdots & 1                         & y_1  \\
		1  & 1 &  \cdots & 0                         & y_2  \\
		\vdots & \vdots & \ddots & \vdots   & \vdots  \\
		1  & 1 &  \cdots & 0                         & y_{N-1}  \\
		x_1 & x_2  & \cdots  & x_{N-1}                     & ?   \\		
	\end{pmatrix}		
\]

Now, no matter what the parity of the rows and columns in the $N-1 \times N-1$ minor, we can find $x_i$ and $y_j$ so that the parity of each row and column sum, in the larger matrix, is odd. The only thing left to consider is the uniqueness of $a_{NN} = ?$. Right. It's totally conceivable that

\[
	\sum x_i \mod 2 \neq \sum y_j \mod 2. 
\] 

However, this in fact doesn't happen. 
<p><strong>Lemma. </strong> <em>Suppose $A$ is a matrix of zeros and ones. Let $x_i$ and $y_j$ be the bit-wise complement ( $1 + 1 \equiv 0 $ and $ 0 + 1 \equiv 1$ ) of the $i$th row and $j$th column, respectively. Then,
\[ 
	\sum x_i \mod 2 \equiv \sum y_j \mod 2. 
\]
</em></p>

<p><em>proof:</em></p>
\begin{align*}
	\sum x_i  \mod 2 &  \equiv \sum (x_i  \mod 2)  \\
								& \equiv \sum_{j} (\sum_{i} a_{ij} \mod 2) \\  
								& \equiv \sum_{j} \sum_{i} (a_{ij} \mod 2). \\  
\end{align*}

Which is the same as the bit-wise sum of the $y_i$'s
\begin{align*}
	\sum y_j  \mod 2 &  \equiv \sum (y_j  \mod 2)  \\
								& \equiv \sum_{i} (\sum_{j} a_{ij} \mod 2) \\  
								& \equiv \sum_{i} \sum_{j} (a_{ij} \mod 2) \\  
\end{align*}

And we get, 
\[ 
	\sum x_i \mod 2 \equiv \sum y_j \mod 2. 
\]
<div align="right">
	<p><em>q.e.d.</em></p>
</div>
With the above lemma in hand, we know that $a_{NN}$ is uniquely determined. Moreover, 

\[ 
	a_{NN} \equiv 1 \mod 2  + \sum_{i} \sum_{j} a_{ij} \mod 2     
\]

What we've shown is that our initial construction/choice of the $N-1 \times N-1$ minor uniquely determines the remaining entries of the larger matrix, the $y_i$'s, $x_i$'s, and $a_{NN}$. So, the count we want is equal to the number of $N-1 \times N-1 $ matrices with zeros and ones:

\[
	\boxed{ \mathbf{2^{(N-1)^2} }}
\]