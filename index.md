---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: splash
title: Welcome to my playground

excerpt: "Allow me to present myself"
header:
    overlay_image: /assets/img/Header.jpg
    overlay_color: "#66CCFF"

team_projects:
    - image_path: /assets/img/SightBringer/cover.png
      title: SightBringer
      excerpt: SightBringer is a Sophomore team project created in a custom engine.
      url: /SightBringer/
      btn_class: "btn--info"
    - image_path: /assets/img/Grav-Link/cover.jpg
      title: Grav-Link
      excerpt: Grav-Link is a Junior team project created in Unreal Engine. 
      url: /Grav-Link/
      btn_class: "btn--info"
    - image_path: /assets/img/FPSChess/cover.png
      title: FPS Chess
      excerpt: FPSChess is a Senior team project created in Unreal Engine.
      url: /FPSChess/
      btn_class: "btn--info"

game_projects:
    - image_path: /assets/img/CubeGame.gif
      title: Sponge Man
      excerpt: Freshman year game made in a custom C engine, testing around with classic platformer abilities like jump height and run speed modifier, double jump, wall jump, dash, etc
      url: /SpongeMan/
      btn_class: "btn--info"
    - image_path: /assets/img/Dandelion.gif
      title: Journey of Dandelion
      excerpt: Made in global game jam 2018 with Unity3D. A android platformer game that utilizes phone gyroscope and microphone functionalities.
      url: /JourneyOfDandelion/
      btn_class: "btn--info"

graphics_projects:
    - title: Skeletal Animation
      image_path: /assets/img/Graphics/SkeletalAnimation.gif
      excerpt: Hierarchical bone interpolation and bone weight blending.
    - title: Path traveling
      image_path: /assets/img/Graphics/PathTravel.gif
      excerpt: Path interpolation with custom spline editor and various numerical integration methods
    - title: Inverse Kinematics
      image_path: /assets/img/Graphics/InverseKinematic.gif
      excerpt: Using the CCD(cyclic coordinate descent) method for bottom up IK bone interpolation.

    - title: Path Tracing
      image_path: /assets/img/Graphics/PathTracer/PathTracer.png
      excerpt: A CPU path tracer using Micro facet BRDF with SIMD optimizations.
      
    - title: Deferred Shading
    - title: Bounding Volumes
       
ai_projects:
    - title: Covid Simulation
    - title: A* Path finding
    - title: Interest Map generation
---

# Team Projects:  
{% include feature_row id="team_projects" %}  
<pre>


</pre>
# Personal Projects:  


## Graphics
{% include feature_row id="graphics_projects" %}  
## AI
{% include feature_row id="ai_projects" %}
## Games
{% include feature_row id="game_projects" %}
