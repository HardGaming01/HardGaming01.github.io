---
permalink: /SightBringer/
author_profile: true
layout: single
toc: true
title: SightBringer
---

# Overview
<!--High concept and links-->
[Steam Link](https://store.steampowered.com/app/1400110/Sightbringer/)  

[Digipen Gallery](https://games.digipen.edu/games/sightbringer)  

SightBringer is a linear side-scrolling platformer in which a bat-like child traverses dark, cavernous ruins full of monsters in order to complete a ritual to restore light.
{% include video id="cvIxXrvO1d0" provider="youtube" %}

# Team
Team UWU is a multideciplinary team consisting of 5 programmers, 4 artists, 1 audio designer and 2 game designers. I was acting as a producer & programmer role in this team. Some of my responsibilities includes:  

Producer: 
- Coordinate between different departments and build pipelines
- Setup appropriate version control for each department
- Schedule for team meetings & Summary
- Plan for each major milestone and split jobs between each member
 
Programmer:  
- Design engine structure
- Architect each major engine system with teammates
- Animation runtime implementation
- UI & tools development
- Physics development

## Team Meetings
Every week we schedule a team meeting to identify each departments progress toward milestone and possible cross decipline blockage. On top of that the tech team also have a weekly meeting to do code review.   

The team was actively using GitLab's issue list, which works similarly as a combination of trello & github issues, to keep track of our progress.
{% include figure image_path="/assets/img/SightBringer/GitLab.png" %}

# UWU Engine
UWU Engine was a custom C++ 2D game engine. It uses OpenGL as it's rendering backend.

During second half of production, we discovered that there are too much technical overhead with our previous engine architecture that a refactor becomes necessary. So a decision was made to overhaul the engine while trying to keep the original interface and pipeline.

This was the biggest refactor I did in my life. Every programmer on my team was working more than 40 hours a week on top of our school work. We've managed to finish the refactor in time and the new architecture was turning out to serve it's purpose as we expected.

## ECS(Entity Component System) Architecture
The engine follows a strict Entity Component System design philosophy. Every entity is represented with a **Entity ID**, while all the component data gets stored in a POD data structure to ensure direct access and cache coherence. While game logics like input, physics, UI, animation, etc are kept within their own **Systems**.

We made sure that all the data and logic are decoupled. Systems have free access to component data while the data containers don't handle any logic.
<!--Insert Image here-->

## Space partitioning
A nice trick we did to enforce this design is to separate components into "*Spaces*". We categorize each of our game objects into the following spaces:
- Gameplay
- Environment
- UI
- Particle
- Light
- Debug
- Transparent

Each space only contains certain types of components, like the *Environment* space only has transform and texture component, while the *GamePlay* space has all the extra components like physics, animation, behavior, tag. And the *Transparent* space will contain translucent objects that needs to be forward rendered. This design was due to the fact that not all objects need to simulate physics, or not all objects needs to be rendered. Separating objects by their functionality while keeping the component data coherent.

## CMake build system
The UWU engine was previously built as a pure visual studio solution. But later due to the need to modify some library source and have cross platform compatibility I switched the build system into CMake. Here are some thirdparty libraries & runtimes we used when making UWU Engine:
- GLFW
- GLEW
- glm
- catch2
- Dear ImGui
- rapidJson
- rttr
- magic_enum
- stb_(image, resize)
- exprtk
- FMOD
- Spine  

Some of these libraries were included as source for easy modification, some are included as packaged binaries, and some are just header only libraries that are nice and compact.

Most of these libraries are cross-platform compatible.

## Editor
The uwu Editor was based on Dear ImGui.

### Object Picker
For the object picker, there was a bit of an obstacle during it's implementation. The basic idea is easy, when mouse is clicked, do a ray cast from camera toward the pixel on the screen and capture the first hit object. 

However when I finished this basic functionality it became obvious that there's more needing to be done. Unlike 3D picker where the mesh's collision is usually defined by its geometry, in our engine the game objects collision is not defined by it's texture. This creates a problem where sometimes the picker would pick up some unwanted object because it's bounding collision is larger than the texture shows. This become significantly obvious with objects with large transparent areas.

I improved this object picker to go through transparent pixels. When a ray is traced it will output an array of objects hit with this raycast, sorted by depth, along with the baricentric coordinate of the hit location. Then for each object I check if the current texture is transparent in the texture storage(only available in editor). Then determine if this object is actually the correct one to pick.
{% include figure image_path="/assets/img/SightBringer/Picker.gif" %}

### Prefab drag and drop
To help the designers and artists with their content creation, I have implemented a simple prefab saving & loading system. Alongside with the drag and drop interaction.

Every game object in any space can be saved into a json prefab, then loaded in through simple drag and drop from the OS's file explorer. 

The drag and drop feature also works with pure textures. When a texture is dropped the editor will create an empty environment space object with the same dimensions as the texture.
{% include figure image_path="/assets/img/SightBringer/Drag.gif" %}

## Spine Animation engine
For 2D skeletal animation, we used [Spine](http://esotericsoftware.com/).  

I implemented the spine runtime instead of using exported spritesheet so the animations transitions will appear a lot smoother.
{% include figure image_path="/assets/img/SightBringer/Spine.gif" %}

## Event System
A robust event system was also developed, I wired every system event like input, action, window resize, etc into this. And every gameplay event like collision, sound, etc.
  
It ended up being only used by me in my systems due to it's complex api, which is kind of a shame...

## UI
{% include figure image_path="/assets/img/SightBringer/UI.gif" %}

### Navigation
Our game was gamepad/keyboard only, so a simple UI navigation system would be needed to link every UI element. Me and my teammate worked out this UI navigation system in a relatively short span of time. Each element have it's own 8 directional navigation alongside a backspace direction.

### Options
The options menu utilizes the navigation and event system, with these I have made some classic option elements like sliders and checkboxes.

## SAT(separating axis theorem) collision detection
For collision detection we used separating axis theorem to define more complex shaped collision than simply rectangles. Animated objects can have multiple collisions bound and switched according to the animation event posted.
{% include figure image_path="/assets/img/SightBringer/Collision.gif" %}

