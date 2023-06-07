---
title: Eclipse Now Available From Flathub
date: 2020-01-20 16:00
tags: linux eclipse
---

Good news! Eclipse is now available from [Flathub](https://flathub.org/apps/search/eclipse%20ide), the central application repository for Flatpak applications.

![Eclipse IDE Logo](/assets/images/eclipse-logo.jpg)

Two flavours of Eclipse IDE are now available from Flathub:

 * [Eclipse IDE for Java Developers](https://flathub.org/apps/details/org.eclipse.Java) -- The essential tooling for any Java developer.
 * [Eclipse IDE for Eclipse Committers](https://flathub.org/apps/details/org.eclipse.Committers) -- Tooling for development of Eclipse itself at Eclipse.org.

See the TL;DR section at the bottom of this article if you want to quickly get started now!

## Why Flatpak?

If you don't already know, [Flatpak](https://flatpak.org/) is the new way to build and distribute desktop applications for Linux. You can use [Flathub](https://flathub.org/) to gain access to a growing collection of Flatpak applications, including Eclipse IDE. You just need to [follow the setup instructions](https://flatpak.org/setup/) for your Linux distribution.

I've discussed before on this blog about the [benefits of packaging software for Linux distributions]({% post_url 2015-12-09-benefits-of-distro-packaging %}) but from the upstream project's point of view, there are two big problems that distro packaging does not solve:

 * There are so many Linuxes!

After all the hard work of packaging your application, it is still only available for only one distro. Keeping Eclipse RPMs maintained in Fedora is almost a full time job, it would be almost impossible for me to duplicate that work for Ubuntu, for example, where a completely different packaging format is used.

 * Forwards and backwards compatibility.

Different Linux distributions package different versions of your dependencies, which makes it difficult to ensure that your application works on them all. Eclipse SWT supports a large range of GTK versions for this reason and it has historically been a lot of work for the SWT contributors. It would be unfair only support the latest versions of GTK on cutting edge platforms like Fedora and Ubuntu at the expense of users on slow-moving enterprise-style distros like RHEL or SLES; or vice-versa.

## Yes, but why Flatpak?

Flatpak solves both these problems whilst keeping the polished, tight integration with the host system that traditional Linux distro packaging provides. It does this by providing common runtime environments that work on every Linux distribution that supports Flatpak.

The implication this has for Eclipse is that we can make the IDE available everywhere Flatpak is supported at almost no additional cost in resources and users can even get the same shiny new version of the IDE on older versions of Linux distros where it would have been impossible to upgrade the in-distro packages. If SWT raises the draw-bridge on old versions of GTK and you can't upgrade your Linux distro, or you want to use Eclipse on a yet-to-be-released version of your Linux distro which has a version of GTK untested by Eclipse, then it's not longer a problem because the Flatpak runtime provides a stable and predictable runtime environment. No longer do we have to worry about API/ABI breakage caused by the distro upgrading dependencies too quickly, or not quickly enough, for Eclipse.

Having such a predictable runtime environment for Eclipse will also help a great deal in diagnosing reported problems. A consistent Flatpak runtime across Linux distributions will greatly reduce the chances that we are bitten, for example, by Ubuntu-specific bugs that cannot be reproduced on Fedora.

## TL;DR - Instructions for the Impatient

Enable the Flathub repository:

```
$ flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

Install the IDE:

```
$ flatpak install flathub org.eclipse.Java
```

Or:

```
$ flatpak install flathub org.eclipse.Committers
```

## Bugs?

If you encounter any bugs that you suspect are specific to the Flatpak version of Eclipse IDE, please consider [reporting them at the Github repo](https://github.com/flathub/org.eclipse.Java/issues) where it is maintained. Thanks!
