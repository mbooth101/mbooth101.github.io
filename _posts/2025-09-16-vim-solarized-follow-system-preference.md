---
title: Configuring Vim Solarized to Follow the System Dark Mode Preference
date: 2025-09-16 11:00
tags: linux bash
---

I like to switch my system between light and dark modes as lighting conditions change, and I want my terminal windows to always respect my current system preference. This article shows how to configure vim to automatically change between light and dark variants of the Solarized colour scheme, to match the current system dark mode preference.

<video width="100%" autoplay loop muted>
  <source src="/assets/video/vim_working.webm" type="video/webm" />
</video>

I usually go years and years between OS re-installs, so I've forgotten how to do this. Hopefully this article will be useful for future me. The first thing to do after installing Fedora on a new machine however, is to switch the default editor back to vim, because I have no muscle memory for nano and I refuse to change. 😅

```text
$ sudo dnf swap nano-default-editor vim-default-editor
```

Now onto the main business of configuring the terminal and vim to use my favourite colour palette, [Solarized by Ethan Schoonover](https://ethanschoonover.com/solarized/).

## Solarize The Terminal

Ptyxis, the new default terminal in Fedora Workstation Edition, has an excellent set of colour palette options. From the hamburger menu drop-down, select the **Follow System Style** button from the three options at the top. This causes Ptyxis to switch between light and dark modes when you change the system dark mode preference instead of being in dark mode all the time. Then open the **Preferences** dialog to select the Solarized colour palette from the options listed there:

![Screenshot of terminal preferences dialog.](/assets/images/vim_terminal_prefs.png)

## Solarize Vim

This works well for normal terminal operation, but vim's own default colours can clash terribly with the terminal colour scheme. Sometimes the foreground and background colours are either the same or extremely low contrast, which results in impossible to read text, as shown here after performing a search for the string "init":

![Screenshot of search result highlights in vim making text unreadable.](/assets/images/vim_bad_colours.png)

Fortunately Ethan provides a vim-specific implementation of the Solarized colour palette in his [vim-colors-solarized](https://github.com/altercation/vim-colors-solarized) repository. This can be installed by [downloading the provided vim script](https://raw.githubusercontent.com/altercation/vim-colors-solarized/refs/heads/master/colors/solarized.vim) into your `.vim/colors` directory:

```text
$ mkdir -p ~/.vim/colors
$ wget https://raw.githubusercontent.com/altercation/vim-colors-solarized/refs/heads/master/colors/solarized.vim \
    -o ~/.vim/colors/solarized.vim
```

And then configuring the colour scheme in your `.vimrc` file by adding the following lines:

```vim
" Enable Solarized Theme
syntax enable
colorscheme solarized
```

New vim sessions will now use the correct colours, and are even able to detect whether to use the light or dark variant of Solarized.

## Dark Mode Detection

However, vim is ***only*** able to detect whether to use the light or dark variant ***at start up.*** This means if I switch the system dark mode preference while vim is open, then I have to close and reopen all my open vim sessions before they will use the correct Solarized variant:

<video width="100%" autoplay loop muted>
  <source src="/assets/video/vim_not_working.webm" type="video/webm" />
</video>

Not even re-sourcing the `.vimrc` using the `:so` command corrects the colours. We can however edit it such that re-sourcing *does* fix the colour scheme variant in use without needing to exit and reload vim.

```vim
" Enable Solarized Theme
syntax enable
let sys_colors=system('gsettings get org.gnome.desktop.interface color-scheme')
if sys_colors =~ 'dark'
    set background=dark
else
    set background=light
endif
colorscheme solarized
```

Expanding upon the previous `.vimrc` snippet, this explicitly sets vim's `background` setting depending on the output of a `gsettings` query for the current system dark mode preference. Now the `:so ~/.vimrc` command can be used to fix the colours without having to close and reopen vim.

## Vimterprocess Communication

It would be even better of course, to have vim automatically re-source the `.vimrc` automatically when the system dark mode preference changes.

Vim has a kind of interprocess communication mechanism built in. If it's started with the `--servername {NAME}` option then vim can accept commands from another vim processes running on your machine. To ensure vim is always started with this option, just add this line to your `.bashrc` file to create a command alias:

```bash
# Always start vim as a server
# with a unique name
alias vi='vi --servername VIM-$(date +%s)'
```

Now when you run vim (or vi) the session will be named with `VIM-<SOME_NUMBER>`. Commands can be sent to such named sessions using a specially crafted invocation of vim:

```text
$ vim --servername VIM-<SOME_NUMBER> --remote-send ":so ~/.vimrc<CR>"
```

So all we need to do is write a small shell script to find all running vim processes, determine their session names, and execute the above command for each one. Create the script in your user's local bin directory, e.g. `~/.local/bin/vsignal.sh` and make it executable with `chmod +x ~/.local/bin/vsignal.sh`:

```bash
#!/bin/bash

function signal_vim() {
	# Signal all running instances of vim
	PIDS=$(pgrep -u $USER vim)
	for PID in $PIDS ; do
		VIM_ID=$(ps --no-headers -p $PID -o args | cut -d' ' -f3)
		vim --servername $VIM_ID --remote-send ":so ~/.vimrc<CR>"
	done
}

# Wait for color-scheme change
gsettings monitor org.gnome.desktop.interface color-scheme | \
while read -r COLOR_SCHEME ; do
	signal_vim
done
```

Piping the `gsettings monitor` command into `read` will cause the script to block until the system dark mode preference is changed. When it does, it will issue a call to the `signal_vim` function, perform the magic, and then go back to blocking. Now while ever the `vsignal.sh` script is running, all active vim sessions will immediately switch to the appropriate Solarized colour scheme variant when the system dark mode preference is changed.

## A Systemd Theme Sync Service

It's a bit incovenient to have to start a script whenever you open a terminal though. The best way to have this script always running is by letting systemd handle it. A new, user-specific service can be created with the following command:

```text
$ systemctl edit --user --force --full theme-sync.service
```

The following service definition will cause systemd to start the script when you log into your Gnome session:

```ini
[Unit]
Description=Dark Mode Sync Service

[Service]
ExecStart=%h/.local/bin/vsignal.sh

[Install]
WantedBy=gnome-session.target
```

And finally, enable and start the service with the following commands:

```text
$ systemctl --user enable theme-sync.service
$ systemctl --user start theme-sync.service
```

Now we can switch between light and dark modes to our heart's content, safe in the knowledge that vim will follow suite. 😌

<video width="100%" autoplay loop muted>
  <source src="/assets/video/vim_working.webm" type="video/webm" />
</video>
