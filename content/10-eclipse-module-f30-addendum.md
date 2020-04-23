Title: Eclipse Module on F30 Addendum
Date: 2019-08-30 12:30
Modified: 2019-08-30 12:30
Category: Misc
Tags: fedora, eclipse
Slug: 10-eclipse-module-f30-addendum
Author: Mat Booth
Summary: Additional information about installing the Eclipse IDE module on F30.

![Eclipse IDE Logo]({static}/images/eclipse-logo.jpg)

As [I wrote previously](/09-eclipse-module-f30.html) Eclipse is now available as a module for [Fedora Modularity](https://docs.fedoraproject.org/en-US/modularity/).

After I wrote that blog post I received some reports of installation difficulty. Some people are experiencing this kind of error:

```
$ sudo dnf module install eclipse
Error: Problems in request:
broken groups or modules: eclipse
Modular dependency problems:

 Problem: conflicting requests
  - module eclipse:2019-06:3020190807134759:6ebe2c0f-0.x86_64 requires module(ant:1.10), but none of the providers can be installed
  - module ant:1.10:2820190409091957:819b5873-0.x86_64 is disabled
  - module ant:1.10:2820190508055149:819b5873-0.x86_64 is disabled
```

It appears that if you have previously explicitly disabled a module on which Eclipse depends, then this user action takes precedence over any implicit enablement of module dependencies. I assume this is an intentional behaviour of DNF (hopefully any DNF people reading can correct this assumption if it is not true) but IMO it should probably ask the user if they want to enable the previously disabled module since that is clearly the only way forward.

In order to fix this situation, you can use the ```dnf``` command to reset the module state so that it is no longer explicitly enabled or disabled. For example, to reset the state of all modules that Eclipse depends on:

```
$ sudo dnf module reset ant maven
Dependencies resolved.
=====================================================================================================================
 Package                           Architecture            Version                     Repository                Size
=====================================================================================================================
Resetting modules:
 ant

Transaction Summary
=====================================================================================================================

Is this ok [y/N]: y
Complete!
```

You can now [install the Eclipse module as documented previously]({filename}/09-eclipse-module-f30.html).
