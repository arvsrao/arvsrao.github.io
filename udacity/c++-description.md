---
layout: dnr
---

# C++ Nanodegree

I really enjoyed working my way through Udacity's [C++ Nanodegree Program](https://www.udacity.com/course/c-plus-plus-nanodegree--nd213). Each lesson culminated in a final project. My final project submissions are described below; all submissions are, of course, implemented in C++.

## Final Projects

* [OSM Route Planner](https://github.com/arvsrao/CppND-Route-Planning): Plot a path between two points on a map using real map data from [OpenStreetMap](https://www.openstreetmap.org/). I implemented the core route finding logic, which is the `A*` algorithm. 

- [System Monitor](https://github.com/arvsrao/CppND-System-Monitor): A system monitor is a program that shows a real-time view of running processes on a computer. The focus of this project was to practice object oriented programming (OOP) and the use of   `std` library data structures and functions. Classes were used to define and implement parsers and renderable entities, like processes. I used the `std` library to read and parse system files containing information about running processes. 
- [Memory Management - Chatbot](https://github.com/arvsrao/CppND-Memory-Management-Chatbot): The chatbot answers simple questions about memory management. I refactored the project to use smart pointers to enforce specific resource ownership policies, and to use move semantics wherever object instances and pointers were returned or passed. Related to the later objective, every class needed to adhere to the rule of 5; so in additional to whatever base constructors a given class had, copy / copy-assignment and move / move-assignment constructors were also defined.
- [Concurrent Traffic Simulation](https://github.com/arvsrao/CppND-Program-a-Concurrent-Traffic-Simulation): I completed key portions of a *multithreaded* traffic simulator. Cars, intersections, and traffic lights are all simulated on separate threads. To prevent collisions I used promises and futures, condition variables, and message queues to ensure orderly queuing of cars at intersections, and proper notification of a green light for cars waiting at intersections.
- [Capstone - Asteroids Game](https://github.com/arvsrao/Asteroids): I chose to make my own *multithreaded* version of Asteroids, the classic arcade game. The player must defend against oncoming asteroids as it navigates a star field in the Starship Enterprise. New asteroids are spawned at random times on a background thread. Also each asteroid manages a thread that detects collisions with the player ship and phaser blasts. The SDL library was used to detect user input and render images and text (like the score) to the screen.

## Graduation Certificate 🎉🎉

[Link to Verified Certificate](https://www.udacity.com/certificate/e/b8cfeb5a-30cb-11ed-b2b2-37d55a081cf3)

![Nanodegree Certificate](/assets/udacity-c++-certificate.png "Certificate")

