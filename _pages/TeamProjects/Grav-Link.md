---
permalink: /Grav-Link/
author_profile: true
layout: single
toc: true
title: Grav-Link
---

# Overview

Grav-Link is a 3D true first person fast-paced action parkour game that features a soldier waking up from a cryo-chamber in an alien planet and trying to find help with his/her gravity gun. 

{% include video id="DMauu9CuKic" provider="youtube" %}

# Team
Team Monster Lab is a multi-deciplinary team consisting of 5 programmers, 6 artists, 1 audio designer and 3 game designers. I am the tech lead of this team.

In this game I have worked on:
- Game mechanic development
- Interactive Prop implementation
- Animation implementation
- UI implementation
- Audio implementation
- Cinematic Creation
- VFX implementation
- World Map Clipping

# Pipeline
## Source Control
We used SVN for this projects' version control. Partially because we couldn't find a easy way to access perforce, and also unreal has pretty good svn integration with a mature lock working pipeline.
## C++ vs Blueprint
The decision on whether to use C++ or blueprint was hard to make. On one hand none of our programmers has any experience with Unreal blueprint, and we like do have our code logic mergeable (didn't know about Unreal's built-in blueprint merge tool). So in the first half of production we decided to try implement all important functionalities in C++, while having things that needs rapid iteration in blueprint.

This decision turned out to create a lot of problems.   

First of all, Unreal editor doesn't have a way to check whether the C++ code needs to be recompiled or not, so sometimes when our designer or artists pull from source control the editor won't say if there's any problems. But due to inconsistency of C++ and Blueprint implementation random bugs will happen all over the place. This wouldn't be a problem if we are a team that's dedicated on engine development, but we are still a game team that primarily focuses on content creation.

Secondly, we tried to mitigate this by uploading the built binary to source control so everyone can directly open the project without recompiling. That was not feasible as the built binaries are always too huge that it would take half an hour to pull everytime a slight thing is changed.  

So after 4 months into development, we decided to leave the matured, performance heavy systems in C++ without being touched, while migrating most code logic into Blueprint. This has brought a lot of benefits to the production. The designers can now access, understand and modify some of the logics. The bug reports became significantly less so more time to work on actual production. And the iteration speed is much faster due to not having to recompile for half a minute for every minor code change.

# Wwise Audio
This project used Wwise unreal plugin to create responsive sound & music. 

# Deprecated features
There are a lot of deprecated features that was not included in the gameplay footage shown above. Some are completely thrown away, some are further iterated upon. These includes:

- Projectile Preview
{% include video id="9Ywp2NyH56s" provider="youtube" %}
- Flying Projectile
{% include video id="23Swe5htrsI" provider="youtube" %}
- Wall Summon
{% include video id="RBSqJHd8q-w" provider="youtube" %}
- Gravity Gun
{% include video id="mOwd-6lGr-o" provider="youtube" %}
- Tripmine + Wall Summon
{% include video id="N0SRep45jSY" provider="youtube" %}
- Shiny Mascot (Dynamic Material)
{% include video id="C60l7CYEBiE" provider="youtube" %}
- Flip Flop Trigger
{% include video id="tx_GgGqkUVY" provider="youtube" %}
- Held Trigger
{% include video id="sEjYLhIs_y8" provider="youtube" %}
- Full Body Animation Blending
{% include video id="wUzZQ0zgzko" provider="youtube" %}

And some Unreal techniques I learned after the project that did not end up being used
- Mesh Painting
{% include video id="UOLfB_DnZ7M" provider="youtube" %}
- Snow Deformation
{% include video id="D6df5dACnH4" provider="youtube" %}
