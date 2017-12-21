---
layout: post
title: Super Simple Primality Testing
category: mathematics 
comments: true
tags: prime numbers, algorithms
---

*Awhile ago I was asked how to determine if an integer is prime*, which is an important problem. Much of today's internet security relies on prime numbers--for generating public & private encryption keys. There are [other uses][2] too. So, labeling a number *prime* is well studied. What I want to do in this post is to cover basic algorithms, which rely on testing divisibility of a given number among a list of possible divisors--a search space; and if none divide, the number is *prime*. By investigating the relationship between a number and its divisors we can reduce the space of possible divisors, and write down a nice sub-linear primality testing algorithm.  

Following first principles, an integer $N$ is prime if $\exists a < N$ so that $a\ \|\ N$. We could then simply try dividing $N$ by all numbers less than $N$. Here's our version $0$ algorithm: <!--more-->

	def isPrime(N):
		if type(N) is not int:
			raise ValueError("N must be a positive integer")
		if N < 2:
			return False
		for x in range(2,N):
			if N % x == 0: 
				return False
		return True

Run this code on a few low integer values, and you'll see that *isPrime* is correct and fast. But for large integers 
not so fast--*just try it on 12312345451; your IPyhon shell will hang*. But no worries, we can reduce the search space. Consider the number
$12$ and its divisors $\{1,2,3,4,6\}$, or $25$ and its divisors $\{1, 5\}$. Each divisor is at most half the number it divides. 
Let's formalize this.

<p><strong>Lemma. A</strong> <em>Let $a,b, N \in \mathbb{Z}^{+}$, and $N = a \cdot b$ -- both $a$ and $b$ divide $N$. Then $a$ and $b$ are both less than $\frac{N}{2}$ </em></p>
<p><em>proof:</em></p>
Suppose $a > \frac{N}{2}$, then 
$$
	N = a \cdot b > \frac{N}{2} \cdot b \ \Longrightarrow b < 2.
$$
Since $b$ is an integer, $b = 1$, a contradiction because $b$ is assumed to be a non-trivial divisor.     

<div align="right">
	<p><em>q.e.d.</em></p>
</div>

Okay, we cut the number of comparisons in half. Great! But we can do better. Note that *large* divisors of $N$ are necessarily paired with *small* divisors. Based on the lemma, these *large* divisors are near $\frac{N}{2}$. Clearly, $\frac{N}{2}$ is a sharp upper bound on divisors. Instead we want an upper bound on *small* divisors, or at least show that if $N$ has divisors, at least one is bounded sub-linearly in $N$. Which we can do.

<p><strong>Lemma. B</strong> <em>Let $a,b, N \in \mathbb{Z}^{+}$, and $N = a \cdot b$ -- both $a$ and $b$ divide $N$. Then either $a \leq \sqrt{N}$ or $b \leq	 \sqrt{N}$. </em></p>
<p><em>proof:</em></p>
Suppose not. Both $a$ and $b$ are greater than $\sqrt{N}$. Then, $a \cdot b > N$.

<div align="right">
	<p><em>q.e.d.</em></p>
</div>

Now this is great! The preceding lemma reduces our search space considerably--e.g. if $N$ has order $1 \times 10^9$, then we only need to check divisibility for $\sim 1 \times 10^5$ numbers. Here's the version $1$ algorithm, which uses the insight provided by <strong>Lemma. B</strong>:

	def isPrime(N):
		if type(N) is not int:
			raise ValueError("N must be a positive integer")
		if N < 2:
			return False
		x = 2
		while x*x <= N:
			if N % x == 0: 
				return False
			x+=1	
		return True

Since I don't have a ground truth set of primes, I used a [web based][1] app I found, to find a few known large primes. I confirmed that the above algorithm correctly identified them as prime.

[1]: http://primes.utm.edu/curios/includes/primetest.php
[2]: http://en.wikipedia.org/wiki/Generating_primes