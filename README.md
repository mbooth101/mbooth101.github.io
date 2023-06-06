# Website Source

This repository contains the source files for publishing the matbooth.co.uk site using the Jekyll static site generator tool and GitHub Pages.

## Initial Setup on Fedora

    $ sudo dnf install ruby ruby-devel rubygem-bundler
    $ git clone git@github.com:mbooth101/mbooth101.github.io.git
    $ cd mbooth101.github.io
    $ bundle update

## Publishing

Create pages in the root directory and blog articles in the __\_posts/__ directory. Add images and media to the __assets/__ directory. Pages and blog articles pages should be written in markdown. The new content can be tested and developed using a local server on port 4000:

    $ bundle exec jekyll serve

Commit everything when done:

    $ git commit -am "Commit the new content"
    $ git push

Find the new content on the live site: [https://matbooth.co.uk/](https://matbooth.co.uk/)

## License

![Creative Commons License](http://i.creativecommons.org/l/by-sa/4.0/88x31.png)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
