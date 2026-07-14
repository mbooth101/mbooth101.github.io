---
title: "EMF Badge Projects"
permalink: /projects/emf/
toc: true
---

This page contains a showcase of my hardware and software projects for the EMF Camp Badge family of devices.

## Tildagon

The Tildagon is a future-proof badge platform for EMF Camp 2024, 2026, and beyond.

### Screen Hexpansion

A hexpansion that supplies an auxilliary screen for the Tildagon, this is my first foray into designing hardware addons for a camp badge.

[View Repo](https://github.com/mbooth101/emf-screen-hexpansion){: .btn .btn--primary}

### Speedometer App & GPS Hexpansion Firmware

A speedometer app for the Tildagon, and accompanying firmware for the GPS Hexpansion.

<video autoplay loop muted controls>
    <source src="/assets/video/emf_speedo.webm" type="video/webm" />
</video>

This app was written to demonstrate a concept I had for the GPS Hexpansion driver firmware to send GPS events to the badge's event bus in the background, allowing any number of apps running on the badge to subscribe to events as a simple way of consuming GPS information without needing to reimplement any UART code or GPS NMEA message parsing code.

Care had to be taken to ensure this all fit within the confines of the GPS Hexpansion's 2 kilobyte EEPROM. My version of the firmware eventually became the basis of the official GPS Hexpansion driver firmware.

[View Speedometer Repo](https://github.com/mbooth101/emf-speedometer){: .btn .btn--primary}

## Older Badges

Projects for previous EMF Camp badges.

### TiDAL 3D

A prototype 3D renderer for the TiDAL, the EMF Camp 2022 badge.

It can render objects from Wavefront OBJ/MTL files, such as you might export from Blender, and crudely supports features like back-face culling, frustum culling, directional lighting, material colours, and flat shading.

<video autoplay loop muted controls>
    <source src="/assets/video/emf_tidal3d.webm" type="video/webm" />
</video>

Much of the 3D maths code had to be implemented in C rather than Python for speed reasons, which I abstracted out into a re-usable module that was compiled into the device firmware. After a lot of profiling and optimising, I eventually managed to reach a performance goal of more than 200 triangles rendered at a speed of more than 10 frames per second, making it useful for animating rudimentary real-time 3D interfaces.

This project led to the contribution of useful polygon drawing code to the [Micropython Framebuf](https://docs.micropython.org/en/latest/library/framebuf.html) library, about which [I gave a talk at FOSDEM 2023](https://archive.fosdem.org/2023/schedule/event/python_hacking_esp32/).

[View TiDAL3D Repo](https://github.com/mbooth101/tidal3d){: .btn .btn--primary}

### Settlers of EMF

A tribute to the widely loved board game "Settlers of Catan" written for the Tilda Mk4, the EMF Camp 2018 badge.

<video autoplay loop muted controls>
    <source src="/assets/video/emf_settlers_of_emf.webm" type="video/webm" />
</video>

Because blitting to the screen was so slow on this device, the area of the screen that is redrawn for each state had to be carefully minimised in order to keep responsiveness acceptible, for example by only redrawing parts of the game board affected by the selection highlight when choosing a road or settlement to build.

The code is available in the Tilda Mk4 App Store repository.

[View Tilda Mk4 Apps Repo](https://github.com/emfcamp/Mk4-Apps/tree/master/settlers_of_emf){: .btn .btn--primary}
