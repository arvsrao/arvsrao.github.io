---
layout: post
title: Functional Prime Number Sieve
comments: true
category: mathematics
tags: haskell
---

In a [post a few years ago][1] I discussed primality testing. For some reason I thought I described the basic prime number sieve (I'm pretty sure there is only one) there, but apparently I didn't. No worries. The prime number sieve solves a different problem; that of generating a list of the first $N$ primes. One could use a primality testing method to do this as well; namely filter a list of numbers with the primality test as a predicate; but sieve based methods are faster and conceptually much easier.

The prime number sieve iteratively filters out all the composite numbers, with the caveat that the leading number in the input is a prime. For $$\{ 2,3,4,5,6,7,8,9,10 \}$$, we put aside $2$, the smallest number, and filter out all multiples of $2$; then put aside $3$ and filter out multiples of $3$, and so on. This process, shown below as a decreasing sequence, terminates with a set of primes. <!--more-->

$$
\begin{gather*}
\{ 2,3,4,5,6,7,8,9,10 \} \supseteq \{2\} \cup \{ 3,5,7,9 \} \supseteq \{2,3\} \cup \{ 5,7 \} \\
\supseteq \{2,3,5\} \cup \{ 7 \} \supseteq \{2,3,5,7\}
\end{gather*}
$$ 

At each stage we have a list of some primes and a residual set, which if it is nonempty must be filtered; this process terminates when the residual set is empty. Filtering $$\{2,3,4,\ldots \} $$ and subsequent residuals sort of defines the set of all primes; however it is an infinite process.

$$
\begin{align*}
  \{2,3,4,\ldots \} & \Longrightarrow \{ 2 \} \cup \{ x \in S \ | \ x \mod 2 \neq 0 \ \}  \\
          & \Longrightarrow \{ 2\} \cup \{ 3 \} \cup \{ x \in A_3 \ | \ x \mod 3 \neq 0 \ \} \\
          & \quad \vdots\\
          & \Longrightarrow \{p_0, \cdots, p_n \} \cup \{ x \in A_{p_n} \ | \ x \mod p_n \neq 0 \ \} \\
          & \quad \vdots \\
\end{align*}
$$

When $n$ primes have been filtered the state looks like $$ \{p_1, \cdots, p_n \} \cup A_{p_{n+1}} $$. Here we denote the residual set $A_{p_i}$ where $p_i$ is the leading/smallest number of the residual set. Consecutive residuals are related by

$$
A_{p_{n+1}}  = \{ x \in A_{p_n} \ | \ x \mod p_n \neq 0 \ \}.
$$

Anyone schooled in imperative programming ( which I guess is most of the world ;)) would go about implementing a function which returns the first $N$ primes by iteratively filtering and collecting primes in a loop. I should emphasize that when I write **iteratively**, I mean that the instructions for filtering and collecting primes are done *eagerly*.

Putting aside the computation for the first $N$ primes, all primes ( [which is an infinite set][2] ) can be expressed as a mathematical set, without really specifying how to compute the next prime.

$$
\{ 2, 3, 5, 7, \cdots \} \quad \text{ or } \quad \{ x \in \mathbb{N} \ | \ x \text{ is prime} \}.  
$$

Okay, the second set from above is practically a tautology...but I digress. The point here is that in mathematical notation we are free to declare an expression for the set all primes, even if there is [no set notation for it][3]. Generally in mathematics it's common to express and manipulate infinite sequences and series. Being somewhat aware of [Haskell's][4] declarative nature, I wondered at the outset if I could create an expression for all primes and subsequently generate finite lists of primes as needed. As you might guess the answer is Yes :)

For the uninitiated, referencing Haskell may seem like a non sequitur. Haskell codes are composed of expressions, which are meant to be true statements, as opposed to instructions for the computer to execute in sequence. Expressions in a [Haskell][4] program ( or any pure functional language for that matter) are executed as needed, **lazily**. As opposed to **eagerly**. Computing the set of all primes via the iterative/imperative prime number sieve implementation would be an infinite loop. Which would never end... And that's the key difference: declaring/expressing the set of all primes versus computing all primes.

We can easily adapt the sieve described earlier. Haskell is nothing if not functional, so we define the following function,

$$
f(S) = \{ p \} \cup \{ x \in S \ | \ x \mod p \neq 0 \ \} \quad \text{ where } p = \min S.
$$

I first tried to explicitly iterate through a finite list of consecutive numbers; as I was developing I was trying to get a feel for haskell. But I couldn't see how to generate the whole collection; and doing an infinite loop seemed wrong somehow--the idea of finding the analog of generators in haskell hadn't occurred to me. Also, probably not idiomatic haskell anyway.

The proper way to express all primes is to recurse, by calling $f$, within its definition, on the residual set. This elegant solution is actually shown ( at the time of this post was written ) on the upper right of the [*haskell.org*][4] landing page. Let $$S \subseteq \mathbb{N} - \{ 1 \}$$, then

$$
f(S) = \{p\} \cup f(\{ x \in S \ | \ x \mod p \neq 0 \ \}) \quad \text{ where } p = \min S.
$$

When $S$ is infinite, the $RHS$ is also infinite. However the infinite recursion is never realized because of lazy evaluation. In particular the set of all primes is expressed by $$f(\mathbb{N} - \{ 1 \})$$. To me this recursive definition is a sort of set builder notation. The listing below is the Haskell implementation of $f$, declaration of all primes, and a request for a finite subset of $primes$. 

    Prelude> filterPrime (p:xs) = p : filterPrime [x | x <- xs, (mod x p) /= 0]
    Prelude> primes = filterPrime [2..]
    Prelude> take 30 primes
    [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]

[1]: http://www.rao.im/mathematics/2014/04/20/super-simple-primality-testing/
[2]: https://en.wikibooks.org/wiki/Famous_Theorems_of_Mathematics/Euclid%27s_proof_of_the_infinitude_of_primes
[3]: https://math.stackexchange.com/questions/456383/what-is-the-standard-notation-to-represent-the-set-of-primes
[4]: https://haskell.org
