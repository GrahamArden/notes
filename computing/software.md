# Software

Things I like to have installed, whether I'm working on [Arch Linux](../arch_linux/README.md) , [macOS](../macos/README.md) or Windows (which I use for [work](../work/README.md))

- The web browser [Firefox](https://wiki.archlinux.org/title/Firefox) (hardened using [arkenfox/user.js](https://github.com/arkenfox/user.js/)), although I'm condering swapping over to [LibreWolf](https://librewolf.net/) which is available via the [AUR](https://aur.archlinux.org/packages/librewolf)
- [Thunderbird](https://wiki.archlinux.org/title/Thunderbird) (I still haven't found anything I prefer for email, although it should be set to [use plain text](https://useplaintext.email/))

- zsh, and obviously, [oh-my-zsh](https://ohmyz.sh/)
  - I like using the [command line](./command_line.md), particularly if I can use [oh-my-zsh](https://github.com/ohmyzsh/wiki/blob/main/Cheatsheet.md)
  - I'm currently looking at [Atuin](https://meyer-laurent.com/atuin-the-magical-shell) to share shell history across different machines
- I keep most of my [dotfiles](https://github.com/webpro/awesome-dotfiles) in a [git repository](https://github.com/GrahamArden/dotfiles), and use [GNU Stow](https://www.gnu.org/software/stow/) to share them between machines.
  - Hint: `cd ~/dotfiles/` then `stow .`
  - My _old_ dotfiles were stored [here](https://bitbucket.org/trigfa/dotfiles/src/master/). This may be a useful starting point where rewriting them.
  - See this useful [YouTube video](https://www.youtube.com/watch?v=y6XCebnB9gs)

## Coding
- [Anaconda Python](https://www.anaconda.com/) for (almost) all your of scientific computing needs on Windows and Mac. Note that it is *not* recommended to install Anaconda on Arch as it can break things . For Arch I just install the packages I need using pacman.
- I really like [NeoVim](https://neovim.io/) which works well in [tmux](https://github.com/tmux/tmux/wiki) on both Linux and Mac. It also now [works](https://github.com/github/copilot.vim) with [copilot](https://github.com/features/copilot)
  - A useful series of videos on setting up NeoVim is available [here](https://www.youtube.com/watch?v=zHTeCSVAFNY)

- On my Windows machine in work I use [Visual Studio Code](https://code.visualstudio.com/) [(AUR)](https://aur.archlinux.org/packages/visual-studio-code-bin) which, surprisingly, has now become my second favourite code editor
  - It's also pretty good for working with [Jupyter](https://jupyter.org/)[ notebooks/lab](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

- For virtual Python environments, just use [venv](../python/virtual_environments.md) 

- When releasing code, it's a good idea to use [semantic versioning](https://semver.org/)

## Presentations

- I'm currently looking at [Quarto](https://quarto.org) particularly for using notebooks for [presentations](https://quarto.org/docs/presentations/) 
- Plugins are available for [Neovim](https://quarto.org/docs/get-started/hello/neovim.html), [Jupyter](https://quarto.org/docs/get-started/hello/jupyter.html) and [Visual Studio Code](https://quarto.org/docs/get-started/hello/vscode.html)
- Unfortunately the Arch Liux [AUR package](https://aur.archlinux.org/packages/quarto-cli-bin) is currently broken so, for the time being, I'm building the [development version](https://github.com/quarto-dev/quarto-cli) from the project's GitHub page. Alternatively, if you don't like living dangerously, you could just install the release version [tarball](https://quarto.org/docs/download/tarball.html)

## Photography
- Organise my photos using [Shotwell](https://en.wikipedia.org/wiki/Shotwell_(software))
- [Sync](https://aur.archlinux.org/packages/gphotos-sync) from [Google Photos](https://photos.google.com/)
- I'd quite like to get into Astrophotography. Must look at [Siril](https://siril.org/)

## Music
- I keep my music library organised using [beets](https://beets.io/). See also the [Arch Wiki](https://wiki.archlinux.org/title/Beets)

## Books
- [Calbre](https://calibre-ebook.com/) works great with Kindle, especially if you [jailbreak](https://kindlemodding.org/) it

## File sharing
- Google Drive.
  - using [rclone](https://archlinux.org/packages/extra/x86_64/rclone/), particulary the [rclone mount](https://rclone.org/commands/rclone_mount/) command
  - [rclone/rclone: "rsync for cloud storage" (github.com)](https://github.com/rclone/rclone)
  - [How To Mount Google Drive Locally Using Rclone In Linux (ostechnix.com)](https://ostechnix.com/mount-google-drive-using-rclone-in-linux/)

- I can also [use rclone](https://rclone.org/dropbox/) for  [Dropbox](https://aur.archlinux.org/packages/dropbox)
- .... and probably Micrososoft [OneDrive](https://rclone.org/onedrive/)

- [Syncthing](https://docs.syncthing.net/intro/getting-started.html)
  - I use Syncthing for storing anything I'd like to keep a bit more secure as I don't have to put trust in Google. It runs on Linux, Mac and theres now a reasonably good Android implementation.

[up](README.md)
[top](../README.md)
