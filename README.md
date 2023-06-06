# Mat's Blog-O-Matic

This repository contains the raw content and makefiles for publishing the blog using the [Pelican](http://blog.getpelican.com/) static site generator tool.

## Initial Setup on Fedora

    $ sudo dnf install python3-pelican
    $ git clone git@github.com:mbooth101/mbooth101.github.io.git
    $ cd mbooth101.github.io

## Publishing

Create articles in the __content__ directory, pages in the __content/pages__ directory and add any images to the __content/images__ directory. Articles and pages should be written in markdown. The new content can be tested and developed using a local server with live-reloading, on port 8000:

    $ make devserver

Commit everything when done:

    $ make publish
    $ git commit -am "Commit the new content"
    $ git push

Find the new content on the live site: [https://matbooth.co.uk/](https://matbooth.co.uk/)

## License

![Creative Commons License](http://i.creativecommons.org/l/by-sa/4.0/88x31.png)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
