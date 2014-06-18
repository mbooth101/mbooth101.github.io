# Mat's Blog-O-Matic

This repository contains the raw content and makefiles for publishing the blog using the [Pelican](http://blog.getpelican.com/) static site generator tool.

## Initial Setup

    $ sudo yum install python-pelican
    $ git clone git@github.com:mbooth101/blog-o-matic.git
    $ cd blog-o-matic
    $ git clone git@github.com:mbooth101/mbooth101.github.io.git output

## Publishing

Create articles in the __content__ directory, pages in the __content/pages__ directory and add any images to the __content/images__ directory. Articles and pages should be written in markdown. The new content can be tested using a local server on port 8000:

    $ make html
    $ make serve

Commit everything when done:

    $ git commit -m "Commit the new content"
    $ git push

Then it can be published it to the live blog:

    $ make publish
    $ cd output
    $ git commit -m "Commit the generated site"
    $ git push
    $ cd ..

Find the new content on the live blog: http://mbooth101.github.io/

## License

![Creative Commons License](http://i.creativecommons.org/l/by-sa/4.0/88x31.png)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
