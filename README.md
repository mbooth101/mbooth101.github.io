# Mat's Blog-O-Matic

This repository contains the raw content and makefiles for publishing the blog using the [Pelican](http://blog.getpelican.com/) static site generator tool.

## Initial Setup

    $ sudo yum install python-pelican
    $ git clone git@github.com:mbooth101/blog-o-matic.git
    $ cd blog-o-matic
    $ git clone git@github.com:mbooth101/mbooth101.github.io.git output

## Publishing

Create articles in the '''content''' directory, pages in the '''content/pages''' directory and add any images to the '''content/images''' directory. Articles and pages should be written in markdown. Commit everything when done:

    $ git commit -am "Commit the new content"

The new content can be tested using a local server on port 8000:

    $ make html
    $ make serve

Before publishing it to the live blog:

    $ make publish
    $ cd output
    $ git commit -am "Commit the generated site"
    $ git push
    $ cd ..

