---
layout: post
title: Asteroids
comments: true
category: c++
tags: c++
typora-root-url: ../

---

<figure>
<div align="center">
	<img src = "/assets/asteroids-spiel-demo.gif">
</div>
  <figcaption> 
    Example game play was captured using a gif maker from 
    <a href="https://giphy.com/create/gifmaker">GIPHY</a>.
  </figcaption> 
</figure>

**I made a game!**

Maybe re-made is a better description. I coded my own *multithreaded* version of [Asteroids][asteroids], the classic arcade game. Following the link takes you to the [GitHub][asteroids] repo of the game.

<!--more-->

The player defends against oncoming asteroids as it navigates a star field in the Starship Enterprise. New asteroids are spawned at random times on a background thread. Also each asteroid manages a thread that detects collisions with the player and any phaser blasts shot by the player. I used the SDL library to detect user input and render images and text (like the score) to the screen.

The game is actually my C++ Nanodegree capstone project. While not a C++ novice, taking the course brought me up speed on the recent standard -- C++17 when I took the course. Some of the major topics covered: RAII, OOP, smart pointers, templates, interfaces, and the concurrency API. Each chapter of the course culminated in a project, and I describe them [here]({{ site.baseurl }}{% link udacity/c++-description.html %}).

While developing the game, I had trouble figuring out when to stop and just submit the project, because I have so many ideas for new features. Like a menu system, an animation system, a thread pool, a moving background ...



[asteroids]: https://github.com/arvsrao/Asteroids
[gif_maker]: https://giphy.com/create/gifmaker
