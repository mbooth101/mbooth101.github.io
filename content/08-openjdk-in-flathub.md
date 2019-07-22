Title: The State of Java in Flathub
Date: 2019-07-22 16:00
Modified: 2019-07-22 16:00
Category: Misc
Tags: fedora, eclipse
Slug: 08-openjdk-in-flathub
Author: Mat Booth
Summary: What's the deal with Java in Flathub?

### "Latest" versus "LTS" OpenJDKs

I am now maintaining two streams of OpenJDK SDK extensions in Flathub:

* **```org.freedesktop.Sdk.Extension.openjdk11```** -- this is supplying the **LTS** (long-term support) OpenJDK 11.
* **```org.freedesktop.Sdk.Extension.openjdk```** -- this is supplying whatever the current short-lived **Latest** OpenJDK is; it is currently OpenJDK 12. (Note the ommission of a version number suffix in the extension ID, this is intentional.)

When OpenJDK 13 is released, OpenJDK 12 will be deprecated and the **```org.freedesktop.Sdk.Extension.openjdk```** extension will be re-based to OpenJDK 13 -- this is why the version number suffix is omitted from the extension ID.

The idea of this is to satisfy two use-cases:

* **Stability** -- if you want stability, you may continue rely on the on the **LTS** version supplied by the **```org.freedesktop.Sdk.Extension.openjdk11```** extension.
* **Early Adopters** -- if you want to take advantage of the latest and greatest features and enhancements in OpenJDK, then you can consume the **Latest** version supplied by the **```org.freedesktop.Sdk.Extension.openjdk```** extension, which will have periodic major updates when new major versions are released by the OpenJDK project.

For maintainers of Java-based applications in Flathub, it's worth noting that even if you consume the **Latest** OpenJDK extension in your application, users will not be broken by major updates because OpenJDK is bundled into your Flatpak. The implication of this for users is that they won't see updates to their Java version until the application maintainer rebuilds the application in Flathub.

If you maintain a Java-based Flatpak application on Flathub, you can consume the latest version of your chosen OpenJDK stream (either **LTS** or **Latest**) simply by rebuilding; the latest version of that OpenJDK steam will be pulled in automatically.

### New OpenJDK Version Updates

Speaking of updates, I recently updated OpenJDK 11 to version **11.0.4** and the OpenJDK 12 to version **12.0.2**; these versions are available now from Flathub.

It's easy to check which version of Java is shipped with a Flatpak application, using BlueJ as an example:

```
$ flatpak run --command='java' org.bluej.BlueJ -version
openjdk version "11.0.2" 2019-01-15
OpenJDK Runtime Environment (build 11.0.2+9)
OpenJDK 64-Bit Server VM (build 11.0.2+9, mixed mode)
```

From the above we can see that BlueJ contains **11.0.2**, an old version of the **LTS** stream. The application needs rebuilding to take advantage of bug fixes in version **11.0.4**.

I recommend that all Java-based Flatpak applications are rebuilt to take advantage of fixes in the latest builds of OpenJDK.

### Using OpenJDK in a New Application

I suspect most people figure it out by looking at existing Flatpak manifests, but it's probably worth quickly mentioning how to go about using the OpenJDK platform extensions to ship a Java application in Flathub. In the vast majority of cases, it is probably sufficient to add the SDK extension to the manifest and calling the JRE installation script. For example:

```
{
  "id" : "org.example.MyApp",
  "branch" : "1.0",
  "runtime" : "org.freedesktop.Platform",
  "runtime-version" : "18.08",
  "sdk" : "org.freedesktop.Sdk",
  "sdk-extensions" : [ "org.freedesktop.Sdk.Extension.openjdk11" ],
  "modules" : [ {
    "name" : "openjdk",
    "buildsystem" : "simple",
    "build-commands" : [ "/usr/lib/sdk/openjdk11/install.sh" ]
  }, {
    "name" : "myapp",
    "buildsystem" : "simple",
    ....
  } ]
  ....
  "finish-args" : [ "--env=PATH=/app/jre/bin:/usr/bin" ]
}
```

And the JRE will be available in the ```/app/jre``` directory. (In this example, ```/app/jre/bin``` has also been added to the PATH environment variable.)

Alternatively, if your application requires a full JDK rather than a JRE, then you can substitute ```installjdk.sh``` for ```install.sh``` and the JDK will be available in the ```/app/jdk``` directory.

### Deprecated OpenJDKs

And finally...

If your Flatpak application was built against either the **```org.freedesktop.Sdk.Extension.openjdk9```** extension or the **```org.freedesktop.Sdk.Extension.openjdk10```** extension and therefore ships OpenJDK 9 or 10, then you should know that since the release of OpenJDK 11, these are ***DEPRECATED***. These JDKs are no longer receiving any maintenance or security updates and are considered ***EOL*** by the upstream OpenJDK project.

Please ***DO NOT*** use these OpenJDKs for new applications being submitted to Flathub, and please migrate any existing applications to a newer, more supported OpenJDK, preferably 11 or 12 as appropriate.

At some point I will probably go through Flathub and file bugs against any applications that are still shipping deprecated OpenJDKs, but I would appreciate it if I didn't have to file any. Thanks in advance!

