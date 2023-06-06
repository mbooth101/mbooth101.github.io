Title: Eclipse is Now a Module on Fedora 30
Date: 2019-08-21 14:30
Modified: 2019-08-21 14:30
Category: Misc
Tags: fedora, eclipse
Slug: 09-eclipse-module-f30
Author: Mat Booth
Summary: How to install the Eclipse IDE module on Fedora 30!

![Eclipse IDE Logo]({static}/images/eclipse-logo.jpg)

From Fedora 30 onwards, Eclipse will be available as a module for [Fedora Modularity](https://docs.fedoraproject.org/en-US/modularity/).


When you query ```dnf``` for the available modules you will see this:

```
[mbooth@fedora30 ~]$ sudo dnf module list eclipse
Last metadata expiration check: 1:28:20 ago on Wed 21 Aug 2019 12:05:22 BST.
Fedora Modular 30 - x86_64 - Updates
Name                   Stream                 Profiles                              Summary                                                       
eclipse                2019-06                java [d], c, everything               An open, extensible IDE and application platform              

Hint: [d]efault, [e]nabled, [x]disabled, [i]nstalled
```

This shows that **Eclipse 2019-06** is available to install with three different profiles from which to choose. Each profile will install the Eclipse IDE and a curated set of plug-ins for accomplishing specific tasks.

 * **java** -- This is the default profile and will install everything you need to start developing Java applications.
 * **c** -- This profile will install everything you need to start developing C/C++ applications.
 * **everything** -- This profile will install all the Eclipse plug-ins currently available in the module, including those that are a part of the above two profiles.

To install the Eclipse with the default profile, simply invoke ```dnf``` like this:

```
[mbooth@fedora30 ~]$ sudo dnf module install eclipse
```

Then you can launch Eclipse in the usual way from your desktop environment. If you later decide you need the extra plug-ins from the other profiles, you can simply do this to get them:

```
[mbooth@fedora30 ~]$ sudo dnf module install eclipse/c
[mbooth@fedora30 ~]$ # ...or...
[mbooth@fedora30 ~]$ sudo dnf module install eclipse/everything
```

You can read more about managing which modules you have installed in the [Fedora Modularity documentation](https://docs.fedoraproject.org/en-US/modularity/using-modules/).

**Public Service Announcement:** I encourage all Fedora Eclipse users to start using the Modularity version because in order to reduce my package maintenance overhead, the packages from the base distro will eventually be retired.

Thanks for your attention!
