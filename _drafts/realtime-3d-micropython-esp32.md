---
title: Realtime 3D Graphics on a MicroPython ESP32
date: 2023-06-03 12:00
tags: python graphics embedded
---

I spent an unreasonable amount of time writing a software 3D renderer for an extremely small and low-power ESP32 device running [MicroPython](https://micropython.org/). This article details the problems I encountered, the optimisations I made, and the eventual contributions I was able to make back to the MicroPython project.

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

It's a long standing tradition at these kind of festivals to give attendees an electronic event badge.

The aim of these is to give people interesting hardware they've probably not experimented with before while being simple enough that anyone can play with it. Usually they are some kind of microcontroller running [Micropython](https://micropython.org/) allowing an easy way to start programatically interacting with all the onboard peripherals like RGB LEDs, acceleromoters, environmental sensors and GPIO pins, etc. I usually lose the next few weekends after the festival messing with them to see what they can do.

## The Badges

TODO PIC OF BADGE

This is the badge from EMF Camp 2018, which was an amazing device containing all the usual peripherals and also a GSM modem. It came with a SIM card and the event team stood up their own cell phone network on site at the festival, which was an incredible feat of organisation and from its form factor you can probably tell that it took direct inspiration from the venerable Nokia Ngage. There was also an app store where attendees could write and submit their own apps for others to download. My recollection is that by the end of the first day of the festival, there was not one, but *two* competing dating apps... 😀

Not only are these badges interesting to play with, but they are also beautiful objects in their own right usually with intricately silk-screened PCB artwork, especially on the newest device from EMF Camp 2022:

TODO PIC OF BADGE

For a variety of reasons include the pandemic and the global silicon shortage, the 2022 badge ended up being a lot smaller and built with more limiting hardware constraints than the badge team had originally hoped for. It's still a great device and has many of the same sensor periphirals as the old badge, but it does have one major advantage over the previous device and that is the speed of its screen, which is orders of magnitude faster than the 2018 badge.

## Blitting

You may recognise on the screen of the 2018 badge a version of the board game, *Settlers of Catan* and even though it's clearly not an action-packed, graphics-heavy game, when I was writing it I recall spending a huge amount of time trying to optimise it to redraw as little as possible because it took literal seconds to blit a full screen of pixels. It was just too limiting for real time graphics. So obviously I had to check out how the new 2022 badge performed and it is *lightening fast* in comparison.

