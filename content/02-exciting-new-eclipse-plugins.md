Title: Exciting New Eclipse Plug-ins in Fedora
Date: 2014-08-21 14:00
Modified: 2014-08-21 14:00
Category: Misc
Tags: fedora, eclipse
Slug: 02-exciting-new-eclipse-plugins
Author: Mat Booth
Summary: TestNG and PHP Development Tools (PDT) plug-ins are now available in Fedora.

Two exciting new plug-ins are now available in Fedora, a TestNG integration plug-in and the PHP Development Tools (PDT) plug-in.

The TestNG plug-in offers integration for Java projects using TestNG as an alternative to the Junit testing framework. It allows authoring, running and debugging TestNG tests in a similar way to the way you can with Junit tests.

![TestNG Action Shot]({static}/images/testng-plugin-screenshot.png)

[Read more](http://testng.org/doc/eclipse.html) about the TestNG plug-in at the project [website](http://testng.org/doc/eclipse.html). It is available for Fedora 20 and above and may be installed with the following command:

    :::console
    $ sudo yum install eclipse-testng

The PHP Development Tools (PDT) plug-in attempts to provide a complete PHP IDE. I am not a PHP programmer so I can't tell you much about it, but at over two hundred thousand downloads from eclipse.org for this version alone, it seems pretty popular. It was added to Fedora as a maintainable replacement for the retired PHPEclipse plug-in, so if you were using that in the past please give this a try.

![PDT Action Shot]({static}/images/pdt-plugin-screenshot.png)

[Read more](http://www.eclipse.org/pdt/) about it on the project [website](http://www.eclipse.org/pdt/). PDT is also available for Fedora 20 and above and may be installed with the following command:

    :::console
    $ sudo yum install eclipse-pdt

Happy hacking!

