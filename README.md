# Website Source

This repository contains the source files for publishing the [https://matbooth.co.uk](matbooth.co.uk) site using the [https://jekyllrb.com/](Jekyll) static site generator tool and GitHub Pages.

## Initial Setup on Fedora

    $ sudo dnf install ruby ruby-devel rubygem-bundler
    $ git clone git@github.com:mbooth101/mbooth101.github.io.git
    $ cd mbooth101.github.io
    $ bundle update

## Publishing

Create non blog pages in the root directory. Work on draft blog articles in __\_drafts/__ so they won't be published by GitHub Pages until they are ready. Move drafts into __\_posts/__ and prefix with the filename with the date for publication.

Add images and media to the __assets/__ directory. Pages and blog articles pages should be written in markdown. The new content can be tested and developed using a local server on port 4000:

    $ bundle exec jekyll serve
    $ bundle exec jekyll serve --drafts # To test publish draft articles

GitHub Pages does not support the Jekyll Archives plugin, so if an article is given a brand new tag that has not been used before, a new tag page should be added to the __\_pages/tags/__ directory.

Commit everything when done:

    $ git commit -am "Commit the new content"
    $ git push

Find the new content on the live site: [https://matbooth.co.uk/](https://matbooth.co.uk/)

## License

![Creative Commons License](http://i.creativecommons.org/l/by-sa/4.0/88x31.png)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
