---
title: Realtime 3D Graphics on a MicroPython ESP32
date: 2023-06-03 12:00
tags: python graphics embedded
---

I spent an unreasonable amount of time writing a software 3D renderer for an extremely small and low-power ESP32 device running MicroPython. This article details the problems I encountered, the optimisations I made, and the eventual contributions I was able to make back to the MicroPython project.

<video controls width="100%">
  <source src="/assets/images/tidal3d-demo.webm" type="video/webm">
</video>
*Demo of the 3D renderer running on the EMF Camp 2022 badge.*
{:style="font-size:0.75em"}

This is an article version of a 20 minute talk I gave at FOSDEM 2023. If you prefer to watch the video of the talk, [you may do so by clicking through to the FOSDEM 2023 video archive](https://fosdem.org/2023/schedule/event/python_hacking_esp32/). This article however contains more details than I was able to include in the talk.

**Note:** Although I've been a programmer for 20 years, you should know that I'm not a graphics programmer, I'm not a python programmer, and I'm not an embedded programmer; it cannot be overstated that ***this is NOT a how-to! This is a what-did!*** 😀

## Some Background

[EMF Camp](https://www.emfcamp.org/) is a weekend outdoor hacker and maker conference and festival in a similar vein to the Chaos Communication Camp and the 4 yearly dutch festival. There's robots and lasers and knitting and soldering and geodesic domes and blacksmitting and satellites and fax machines and... It's great fun for nerds of all kinds.

![Photographs of EMF Camp festival.](/assets/images/emfcamp-2022.png)
*EMF Camp photos by [Em O’Sullivan](https://www.flickr.com/people/freakatoms/) Creative Commons BY-NC-SA 2.0 Licenced*
{:style="font-size:0.5em"}

It's a long standing tradition at these kind of events to give attendees an electronic event badge.

The aim of these is to give people interesting hardware they've probably not experimented with before while being simple enough that anyone can play with it. Usually they are some kind of microcontroller running micropython allowing an easy way to start programatically interacting with all the onboard peripherals like RGB LEDs, acceleromoters, environmental sensors and GPIO pins, etc.

Not only are they interesting to play with, but as you can see they are also beautiful objects in their own right usually with intricately silk-screened PCB artwork:

