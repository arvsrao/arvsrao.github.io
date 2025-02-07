---
title: Divisibility Rule of 9
layout: post
comments: true
category: math
tags: math
typora-root-url: ../
---

While chatting with my son about how to determine all the factors of an integer he (or maybe my wife) said 9 must be a factor because the digits of the integer sum to 9. Which really surprised me. I don't recall learning this fact in school. Which I can only blame on my poor American education...

Anyway, define $a_1a_0 := a_1 \times 10 + a_0$ where $a_i \in \{0,1, \cdots, 9 \}$. Suppose $a_0 + a_1 = 9$, then

1. $a_1a_0 \ \| \ 9$
2. $a_1a_0 = (a_1 + 1) \times 9$.

<!--more-->

Lets look at an example, like $27$, to see why it might be true. First of all we know immediately that $27 = 3 \times 9$. If $27$ isn't factorized all at once, a pattern emerges. 

$$
\begin{align*}
  27 &= 18 + 9 \\
     &= 9  + (9 + 9) \\
\end{align*}
$$

At each stage of the division a $9$ is removed. Notice that the digits of the remainder (what I am terming the remainder is the left most summand of the right hand side) always sum to $9$. Taking a closer look we see at each stage that ${\bf{1}}$ is subtracted from the tens place of the remainder and at the same time ${\bf{1}}$ is added to the ones place of the remainder.

$$
\begin{align*}
  27 &= (2-{\bf{1}}),(7+{\bf{1}}) + 9 \\
     &= \cancel{(2-{\bf{2}})},(7+{\bf{2}})  + (9 + 9) \\
\end{align*}
$$

Applying these insights to any integer $a_1a_0$ satisfying the divisibility rule conditions above and iteratively removing $9$, both assertions are proved. 

$$
\begin{align*}
  a_1a_0 &= (a_1 - 1)(a_0 + 1) + 9 \\
         &= (a_1 - 2)(a_0 + 2) + 2 \times 9 \\
         &\ \  \vdots \\
         &= \cancel{(a_1 - a_1)}(a_0 + a_1) + a_1 \times 9\\
         &= (a_1 + 1) \times 9 \\
\end{align*}
$$

We could consider the generalization $a_0 + a_1 \ \| \ 9$. But since $99$ is the only two digit number whose digits sum are a non-trival multiple of $9$, I don't think it is useful to consider. One could remove $9$ leaving a remainder satisfying the rule above. The extra division stage increases the end quotient by $1$.

$$
\begin{align*}
  99 &= 90 + 9 \\
     &= 81  + (9 + 9) \\
     &= 82  + (9 + 9 + 9) \\
     &\ \  \vdots \\
     &= (9 + 2) \times 9 \\
\end{align*}
$$

## Prologue

The statment I made and proved above can of course be extended to integers of arbitrary word length.

Let $a_{n}a_{n-1} \ldots a_1a_0 := a_n \times 10^n + a_{n-1} \times 10^{n-1} + \cdots + a_1 \times 10 + a_0$. Further suppose $a_n + a_{n-1} + \cdots + a_1 + a_0 \ \| \ 9$. 


Let's consider $675$ and see what happens.
$$
\begin{align*}
  675 &= (6-{\bf{1}}),(7+{\bf{1}}),(5) + 90 \\
      &\ \  \vdots \\
      &= \cancel{(6-{\bf{6}})},(7+{\bf{6}}),(5) + (6\times 90) \\
      &= (0),(7 + 6 - {\bf{1}}),(5+{\bf{1}}) + (6\times 90) + 9 \\
      &\ \  \vdots \\
      &= (0),\cancel{(7 + 6 -{\bf{13}})},(5+7+6) + (6\times 90) + (7 + 6) \times 9\\
      &= (2 + 6\times 10 + 7 + 6) \times 9\\
\end{align*}
$$

Replacing each digit with symbols a pattern emerges.

$$
\begin{align*}
  a_2a_1a_0 &= (a_2-{\bf{1}}),(a_1+{\bf{1}}),(a_0) + 90 \\
      &\ \  \vdots \\
      &= \cancel{(a_2-{\bf{a_2}})},(a_1+{\bf{a_2}}),a_0 + (a_2\times 90) \\
      &= (0),(a_1 + a_2 - {\bf{1}}),(a_0+{\bf{1}}) + (a_2\times 90) + 9 \\
      &\ \  \vdots \\
      &= (0),\cancel{(a_1 + a_2 -{\bf{a_1 + a_2}})},(a_1 + a_2 + a_0) + (a_2\times 90) + (a_1 + a_2) \times 9\\
      &= a_1 + a_2 + a_0 + (a_2\times 10 + a_1 + a_2) \times 9\\
\end{align*}
$$

What's happening in general is still a bit fuzzy to me. Consider a $n$-digit number.

$$
\begin{align*}
  a_n a_{n-1} \cdots a_1a_0 &= (a_n-{\bf{a_n}}),(a_{n-1}+{\bf{a_n}}), \cdots a_1, a_0 + 9a_n 10^{n-1} \\
      &= (0),(a_{n-1} + a_n), \cdots a_1, a_0 + 9 a_n 10^{n-1} \\
      &= (0),(0), (a_{n-2} + a_{n-1} + a_n) \cdots a_1, a_0 + 9(a_n 10^{n-1} + (a_{n-1} + a_n)10^{n-2}) \\
      &\ \  \vdots \\
      &= (0),(0), \cdots , (a_{n-i} + \cdots + a_{n-1} + a_n), a_{n-i-1}, \cdots ,a_1, a_0  \ + \\
      & 9(a_n 10^{n-1} + (a_{n-1} + a_n) 10^{n-2} + \cdots + (a_{n - i +1} + \cdots + a_n)10^{n-i}) \\
      &\ \  \vdots \\
      &= (0),(0), \cdots , (0),(\sum^{n}_{i=0} a_i) + 9\sum^{n}_{i=1}\sum^{n}_{j=n-i+1} a_j 10^{n - i} \\
      &= \sum^{n}_{i=0} a_i + 9\sum^{n}_{i=1}\sum^{n}_{j=n-i+1} a_j 10^{n - i} \\
\end{align*}
$$

And there it is. $ a_n a_{n-1} \cdots a_1a_0$ is factored into two summands that are clearly divisible by $9$.
