Title: Eclipse Luna for Fedora 20
Date: 2014-08-22 13:00
Modified: 2014-08-22 13:00
Category: Misc
Tags: fedora, eclipse
Slug: eclipse-luna-for-fedora-20
Author: Mat Booth
Summary: Eclipse Luna is now available for Fedora 20 as a software collection.

If you are a Fedora Eclipse user, then you're probably saddened since the release of Eclipse Luna (4.4) because you are still using Eclipse Kepler (4.3) on Fedora 20.

Well, be saddened no longer because Eclipse Luna is now available for Fedora 20 as a software collection!

A software collection is simply a set of RPMs whose contents are isolated from the rest of your system such that they do not modify, overwrite or otherwise conflict with anything in the main Fedora repositories. This allows you install multiple versions of a software stack side-by-side, without them interfering with one another. More can be read about this mechanism on the [software collections website](https://www.softwarecollections.org/en/).

The Eclipse Luna software collection lives in a separate yum repository [hosted by COPR](http://copr.fedoraproject.org/coprs/mbooth/eclipse-luna/), which must be configured by clicking on [this link](http://copr-be.cloud.fedoraproject.org/results/mbooth/eclipse-luna/fedora-20-x86_64/eclipse-luna-1.0-11.fc21/eclipse-luna-release-1.0-11.fc20.noarch.rpm) to install the [release package](http://copr-be.cloud.fedoraproject.org/results/mbooth/eclipse-luna/fedora-20-x86_64/eclipse-luna-1.0-11.fc21/eclipse-luna-release-1.0-11.fc20.noarch.rpm).

Then you can install the whole collection by doing:

    :::console
    $ sudo yum install eclipse-luna

This will install everything you need to run Eclipse Luna (including a bunch of useful plug-ins for Java and C/C++ development) on your Fedora 20 machine. After installation is complete, you may notice Eclipse Luna's shiny new icon appear next to the old one in GNOME.

![Luna Launcher]({filename}/images/eclipse-luna-f20-launcher.png)

Alternatively, if you ever need to launch Eclipse from a terminal, you can do so with the following command:

    :::console
    $ scl enable eclipse-luna eclipse

And that will launch the specific version of Eclipse from the Eclipse Luna software collection instead of the default Eclipse that comes with Fedora 20.

Happy hacking!

