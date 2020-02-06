Title: Eclipse and Handling Content Types on Linux
Date: 2020-02-06 15:00
Modified: 2020-02-06 15:00
Category: Misc
Tags: fedora, eclipse
Slug: 13-eclipse-handling-content-types
Author: Mat Booth
Summary: Getting deep desktop integration on Linux.

One of the ways we achieve nice desktop integration on Linux by packaging Eclipse in RPMs or as a Flatpak application is by providing a desktop entry file (using the Freedesktop [Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry-spec/latest/)) to allow desktop environments to list Eclipse in their application launchers and menus.

In this file we may also declare what content types Eclipse supports so that we also get nice integration with file managers. This results in users discovering that files may be edited with Eclipse before they even start up their IDE. For example, if you install the [Flatpak version of Eclipse](https://flathub.org/apps/details/org.eclipse.Java), you may now see this nice context menu entry when you right-click on Java, Maven POM or Gradle Build files:

![Open with Eclipse]({static}/images/open_with.png)

However there seems to be (surprisingly to me, at least) no Freedesktop standard way to do any post-installation manipulation of the information supplied by desktop entry files; an application that has the ability to install plug-ins through it's own integral Marketplace client like Eclipse does has no ability to tell the host system about the new content type support that new plug-ins add.

Apparently this is not really a common use-case, and applications generally do one of two things:

## Thing 1 (Be Greedy)

Just declare that they support all the file types, and fail gracefully if the support is missing. E.g. a video player will just declare that it supports all the different kinds of videos and if a codec is missing it just warns the user when it fails. The user can then install that codec at their leisure and try again.

In Eclipse's case, I don't think we can know up front all the possible content types for which people can author plug-ins, however each Marketplace entry advertises (or should advertise) what content types are supported by its plug-ins. By collecting this information for Marketplace entries that support the release of Eclipse we are building (e.g., 2019-12) we could generate a monster desktop file that contains all the types the Marketplace knows about at that time.

### Pros:

This allows users to discover that Eclipse can support a type even before the user has even opened Eclipse, or installed any plug-ins, simply by attempting to open a file in their file manager.

### Cons:

New Marketplace entries created after Eclipse is built would be omitted from this list, but that might not a be big problem in real life. A rebuild would be required to update the content type list.

We also would not be able to generate this list at build time for RPM or Flatpak type distributions of Eclipse since these build environments allow no connection to the outside world -- it would require the packager to maintain/pre-build such a list.

It might be okay for e.g., VLC to do this since it only "claims" audio/video files, but there would be no limit to the kinds of files that Eclipse might "claim" and this might be too intrusive or annoying for the user.

## Thing 2 (Be Honest)

When installed, extensions deliver additional desktop entry files that contain the additional content types and actions to open them, but are with a flag set to make them "hidden" to allow file managers to present it as an option when opening files but avoid duplicate entries in the desktop environment's applications menu. This means an application will only advertise its current capabilities. For example, even though you have the ```libreoffice-core``` package installed, you might not get an "open with" option for spreadsheets until you install ```libreoffice-calc```.

In Eclipse's case we know what content types a plug-in supports because each one contributes to the extension registry about which file extensions it knows, so Eclipse could be taught to generate new desktop entries file after a p2 install/uninstall operation.

### Pros:

No need to know about all the content types up-front, so saves on packaging work and not all Marketplace entries are correctly annotated with their supported content types anyway.

Wouldn't clutter up the user's file manager with options they might not ever care about for files they might never edit in Eclipse and after all, Eclipse can still prompt users to install plug-ins from the Marketplace when it detects a content type for which a plug-in is available.

Plug-in installation is user-specific for read-only installations like RPM and Flatpak, so this has the nice side-effect on multi-user systems of showing the option to open a file with Eclipse only to users who have the relevant plug-ins installed.

### Cons:

Eclipse needs to know how to generate new desktop files when a plug-in is installed that adds support for a new content type.

Users have to actually open a file in Eclipse before discovering there is a Marketplace entry that supports that content type, instead of being prompted by their file manager before Eclipse is launched. Eclipse is still doing plug-in discovery, so this isn't a huge concern for me.

## Feedback

If you would like to see more nice desktop integrations like this, [let me know on Twitter](https://twitter.com/FOSS_mbooth) or by [filing a bug against Eclipse on Flathub](https://github.com/flathub/org.eclipse.Java/issues).
