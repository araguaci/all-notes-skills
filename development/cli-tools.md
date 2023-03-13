# CLI tools you won't be able to live without 🔧

As developers, we spend a lot of our time in the terminal. There's a lot of helpful CLI tools, which can make your life in the command line easier, faster and generally more fun.

This post outlines my top 50 must-have CLI tools, which I've come to rely on. If there's anything I'm missing - do let me know in the comments :)

At the end of the article, I've included some scripts to help you automate the installation and updating of these tools on various systems/ distros.

<details>
<summary><b>Sumary (click for expand)</b></summary>

## Table of Contents

- [Utils](#utils)
    - [`thefuck` \- Auto-correct miss-typed commands](#thefuck---auto-correct-miss-typed-commands)
    - [`zoxide` \- Easy navigation *(better cd)*](#zoxide---zoxide-easy-navigation-_better-cd)
    - [`tldr` \- Community-maintained docs *(better `man`)*](#tldr---community-maintained-docs-_better-man)
    - [`scc` \- Count lines of code *(better `cloc`)*](#scc---count-lines-of-code-_better-cloc)
    - [`exa` \- Listing Files *(better `ls`)*](#exa---listing-files-_better-ls)
    - [`duf` \- Disk Usage *(better `df`)*](#duf---disk-usage-_better-df)
    - [`aria2` \- Download Utility *(better `wget`)*](#aria2---download-utility-_better-wget)
    - [`bat` \- Reading Files *(better `cat`)*](#bat---reading-files-better-cat)
    - [`diff-so-fancy` \- File Comparisons *(better `diff`)*](#diff-so-fancy---fancydiff-so-fancy-file-comparisons-_better-diff)
    - [`entr` \- Watch for changes](#entr---watch-for-changes)
    - [`exiftool` \- Reading + writing metadata](#exiftool---reading--writing-metadata)
    - [`fdupes` \- Duplicate file finder](#fdupes---duplicate-file-finder)
    - [`fzf` \- Fuzzy file finder *(better `find`)*](#fzf---fuzzy-file-finder-better-find)
    - [`hyperfine` \- Command benchmarking](#hyperfine---command-benchmarking)
    - [`just` \- Modern command runner *(better `make`)*](#just---modern-command-runner-_better-make)
    - [`jq` \- JSON processor](#jq---json-processor)
    - [`most` \- Multi-window scroll pager *(better less)*](#most---multi-window-scroll-pager-_better-less)
    - [`procs` \- Process viewer *(better ps)*](#procs---process-viewer-_better-ps)
    - [`rip` \- Deletion tool *(better rm)*](#rip---deletion-tool-_better-rm)
    - [`ripgrep` \- Search within files *(better `grep`)*](#ripgrep---search-within-files-_better-grep)
    - [`rsync` \- Fast, incremental file transfer](#rsynchttpsrsyncsambaorg-fast-incremental-file-transfer)
    - [`sd` \- Find and replace *(better `sed`)*](#sd---find-and-replace-_better-sed)
    - [`tre` \- Directory hierarchy *(better `tree`)*](#tre---directory-hierarchy-_better-tree)
    - [`xsel` \- Access the clipboard](#xsel---access-the-clipboard)
- [CLI Monitoring and Performance Apps](#cli-monitoring-and-performance-apps)
    - [`bandwhich` \- Bandwidth utilization monitor](#bandwhich---bandwidth-utilization-monitor)
    - [`ctop` \- Container metrics and monitoring](#ctop---container-metrics-and-monitoring)
    - [`bpytop` \- Resource monitoring *(better `htop`)*](#bpytop---resource-monitoring-_better-htop)
    - [`glances` \- Resource monitor + web and API](#glances---resource-monitor--web-and-api)
    - [`gping` \- Interactive ping tool *(better `ping`)*](#gping---interactive-ping-tool-_better-ping)
    - [`dua-cli` \- Disk usage analyzer and monitor *(better `du`)*](#dua-cli---cli-disk-usage-analyzer-and-monitor-_better-du)
    - [`speedtest-cli` \- Command line speed test utility](#speedtest-cli---cli-command-line-speed-test-utility)
    - [`dog` \- DNS lookup client *(better `dig`)*](#dog---dns-lookup-client-_better-dig)
- [CLI Productivity Apps](#cli-productivity-apps)
    - [`browsh` \- CLI web browser](#browsh---orgbrowsh-cli-web-browser)
    - [`buku` \- Bookmark manager](#buku---bookmark-manager)
    - [`cmus` \- Music browser / player](#cmus---music-browser--player)
    - [`cointop` \- Track crypto prices](#cointop---shcointop-track-crypto-prices)
    - [`ddgr` \- Search the web from the terminal](#ddgr---search-the-web-from-the-terminal)
    - [`khal` \- Calendar client](#khal---calendar-client)
    - [`mutt` \- Email client](#mutthttpsgitlabcommuttmuamutt-email-client)
    - [`newsboat` \- RSS / ATOM news reader](#newsboat---rss--atom-news-reader)
    - [`rclone` \- Manage cloud storage](#rclone---manage-cloud-storage)
    - [`taskwarrior` \- Todo + task management](#taskwarrior---todo--task-management)
    - [`tuir` \- Terminal UI for Reddit](#tuirhttpsgitlabcomajaktuir-terminal-ui-for-reddit)
- [CLI Dev Suits](#cli-dev-suits)
    - [`httpie` \- HTTP / API testing testing client](#httpie---http--api-testing-testing-client)
    - [`lazydocker` \- Full Docker management app](#lazydocker---full-docker-management-app)
    - [`lazygit` \- Full Git management app](#lazygit---full-git-management-app)
    - [`kdash` \- Kubernetes dashboard app](#kdash---kubernetes-dashboard-app)
    - [`gdp-dashboard` \- Visual GDP debugger](#gdp-dashboard---visual-gdp-debugger)
- [CLI External Sercvices](#cli-external-sercvices)
    - [`ngrok` \- Reverse proxy for sharing localhost](#ngrok---reverse-proxy-for-sharing-localhost)
    - [`tmate` \- Share a terminal session via internet](#tmate---share-a-terminal-session-via-internet)
    - [`asciinema` \- Recording + sharing terminal sessions](#asciinema---recording--sharing-terminal-sessions)
    - [`navi` \- Interactive cheat sheet](#navi---interactive-cheat-sheet)
    - [`transfer.sh` \- Fast file sharing](#transfersh---fast-file-sharing)
    - [`surge` \- Deploy a site in seconds](#surge---deploy-a-site-in-seconds)
    - [`wttr.in` \- Check the weather](#wttrin---check-the-weather)
- [CLI Fun](#cli-fun)
    - [`cowsay` \- Have an ASCII cow say your message](#cowsayhttpsenwikipediaorgwikicowsay-have-an-ascii-cow-say-your-message)
    - [`figlet` \- Output text as big ASCII art text](#figlethttpwwwfigletorg-output-text-as-big-ascii-art-text)
    - [`lolcat` \- Make console output raibow colored](#lolcat---make-console-output-raibow-colored)
    - [`neofetch` \- Show system data and ditstro info](#neofetch---show-system-data-and-ditstro-info)
- [Installations and Management](#installations-and-management)
- [Conclusion](#conclusion)
    - [What wasn't included](#what-wasnt-included)
    - [Credit](#credit)
    - [Feedback](#feedback)
    - [Source](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6)
    - [Find More](#find-more)

</details>

## <a id="utils"></a>[](#utils)Utils

### <a id="-raw-thefuck-endraw-autocorrect-misstyped-commands"></a>[](#-raw-thefuck-endraw-autocorrect-misstyped-commands)[`thefuck`](https://github.com/nvbn/thefuck) \- Auto-correct miss-typed commands

> `thefuck` is one of those utilities you won't be able to live without once you've tried it. Whenever you mis-type a command and get an error, just run `fuck` and it'll auto-correct it. Use up/down to choose a correction, or just run `fuck --yeah` to just execute the most likely immediately.

<img width="678" height="362" src="https://res.cloudinary.com/practicaldev/image/fetch/s--u7SIvxke--/c_limit,f_auto,fl_progressive,q_66,w_880/https://i.ibb.co/J55hWKX/thefuck.gif"/>

[![View thefuck on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--KxN6ggWN--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/nvbn/thefuck%3Fcolor%3D232323%26label%3Dthefuck%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/nvbn/thefuck) [![Author nvbn](https://res.cloudinary.com/practicaldev/image/fetch/s--S5h3q0Nw--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/nvbn-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/nvbn)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install thefuck

# Arch Linux
sudo pacman -S thefuck

# FreeBSD
pkg install thefuck 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-zoxide-endraw-easy-navigation-better-cd"></a>[](#-raw-zoxide-endraw-easy-navigation-better-cd)[`zoxide`](https://github.com/ajeetdsouza/zoxide) \- Easy navigation *(better cd)*

> `z` lets you jump to any directory without needing to remember or specify its full path. It remembers which directories you've visited, so you can jump around quickly - you don't even need to type the full folder name. It also has an interactive selection option, using `fzf` so you can live-filter directory results

<img width="678" height="362" src="https://res.cloudinary.com/practicaldev/image/fetch/s--XDmbmZKz--/c_limit,f_auto,fl_progressive,q_66,w_880/https://i.ibb.co/6Z960jq/zoxide.gif"/>

[![View zoxide on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--M0QrGEHB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/ajeetdsouza/zoxide%3Fcolor%3D232323%26label%3Dzoxide%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/ajeetdsouza/zoxide) [![Author ajeetdsouza](https://res.cloudinary.com/practicaldev/image/fetch/s--MFq3IwSb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/ajeetdsouza-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/ajeetdsouza)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install zoxide

# Arch Linux
sudo pacman -S zoxide

# Debian / Ubuntu
sudo apt install zoxide

# FreeBSD
pkg install zoxide

# Other (via Rust Creates)
cargo install zoxide --locked 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-tldr-endraw-communitymaintained-docs-better-raw-man-endraw-"></a>[](#-raw-tldr-endraw-communitymaintained-docs-better-raw-man-endraw-)[`tldr`](https://github.com/tldr-pages/tldr) \- Community-maintained docs *(better `man`)*

> `tldr` is a huge collection of community-maintained man pages. Unlike traditional man pages, they're summarized, contain useful usage examples and nicely colourized for easy reading

<img width="678" height="362" src="https://res.cloudinary.com/practicaldev/image/fetch/s--NCt0wa_e--/c_limit,f_auto,fl_progressive,q_66,w_880/https://i.ibb.co/jTW9knx/tlfr.gif"/>

[![View tldr on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s---ow3kUG2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/tldr-pages/tldr%3Fcolor%3D232323%26label%3Dtldr%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/tldr-pages/tldr) [![Author tldr-pages](https://res.cloudinary.com/practicaldev/image/fetch/s--lqs7vHQ6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/tldr-pages-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/tldr-pages)

Install

```
# MacOS (via Homebrew)
brew install tldr

# Other (via NPM)
npm install -g tldr 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-scc-endraw-count-lines-of-code-better-raw-cloc-endraw-"></a>[](#-raw-scc-endraw-count-lines-of-code-better-raw-cloc-endraw-)[`scc`](https://github.com/boyter/scc) \- Count lines of code *(better `cloc`)*

> `scc` gives you a breakdown of number of lines of code written in each language for a specific directory. It also shows some fun stats, like estimated cost to develop and complexity info. It's incredibly fast, very accurate and has support for a wide range of languages

[![scc-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--Rx6T-QOU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/NygHWXt/scc.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--Rx6T-QOU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/NygHWXt/scc.png)

[![View scc on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--cznNqLPm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/boyter/scc%3Fcolor%3D232323%26label%3Dscc%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/boyter/scc) [![Author boyter](https://res.cloudinary.com/practicaldev/image/fetch/s--DIb0Yhou--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/boyter-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/boyter)[![Written in Go](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install scc

# Other (via go)
go install github.com/boyter/scc/v3@latest 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-exa-endraw-listing-files-better-raw-ls-endraw-"></a>[](#-raw-exa-endraw-listing-files-better-raw-ls-endraw-)[`exa`](https://github.com/ogham/exa) \- Listing Files *(better `ls`)*

> `exa` is a modern Rust-based replacement for the `ls` command, for listing files. It can display file-type icons, colors, file/folder info and has several output formats - tree, grid or list

[![exa-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--mdHy9jvg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/cTs0wQ5/exa.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--mdHy9jvg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/cTs0wQ5/exa.png)

[![View exa on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--1QGF4ma8--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/ogham/exa%3Fcolor%3D232323%26label%3Dexa%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/ogham/exa) [![Author ogham](https://res.cloudinary.com/practicaldev/image/fetch/s--QC1gNgew--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/ogham-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/ogham)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install exa

# Arch Linux
sudo pacman -S exa

# Debian / Ubuntu
sudo apt install exa 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-duf-endraw-disk-usage-better-raw-df-endraw-"></a>[](#-raw-duf-endraw-disk-usage-better-raw-df-endraw-)[`duf`](https://github.com/muesli/duf) \- Disk Usage *(better `df`)*

> `duf` is great for showing info about mounted disks and checking free space. It produces a clear and colorful output, and includes options for sorting and customizing results.

[![duf-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--ubkhFYhh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/sP59DKd/duf.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--ubkhFYhh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/sP59DKd/duf.png)

[![View duf on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--FWVId5Hh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/muesli/duf%3Fcolor%3D232323%26label%3Dduf%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/muesli/duf) [![Author muesli](https://res.cloudinary.com/practicaldev/image/fetch/s--mhF1BOG_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/muesli-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/muesli)[![Written in Go](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install duf

# Arch Linux
sudo pacman -S duf

# Debian / Ubuntu
sudo apt install duf

# FreeBSD
pkg install duf 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-aria2-endraw-download-utility-better-raw-wget-endraw-"></a>[](#-raw-aria2-endraw-download-utility-better-raw-wget-endraw-)[`aria2`](https://github.com/aria2/aria2) \- Download Utility *(better `wget`)*

> `aria2` is a lightweight, multi-protocol, resuming download utility for HTTP/HTTPS, FTP, SFTP, BitTorrent and Metalink, with support for controlling via an RPC interface. It's incredibly [feature rich](https://aria2.github.io/manual/en/html/README.html), and has tons of [options](https://aria2.github.io/manual/en/html/aria2c.html). There's also [ziahamza/webui-aria2](https://github.com/ziahamza/webui-aria2) \- a nice web interface companion.

[![aria2c-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--IpOODsJu--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/pJkkX6x/aria2c.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--IpOODsJu--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/pJkkX6x/aria2c.png)

[![View aria2 on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--iB0qdzpz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/aria2/aria2%3Fcolor%3D232323%26label%3Daria2%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/aria2/aria2) [![Author aria2](https://res.cloudinary.com/practicaldev/image/fetch/s--2EADhfq_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/aria2-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/aria2)[![Written in C++](https://res.cloudinary.com/practicaldev/image/fetch/s--tO0jFOIW--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--tO0jFOIW--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install aria2

# Arch Linux
sudo pacman -S aria2

# Debian / Ubuntu
sudo apt install aria2 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-bat-endraw-reading-files-better-raw-cat-endraw-"></a>[](#-raw-bat-endraw-reading-files-better-raw-cat-endraw-)[`bat`](https://github.com/sharkdp/bat) \- Reading Files *(better `cat`)*

> `bat` is a clone of `cat` with syntax highlighting and git integration. Written in Rust, it's very performant, and has several options for customizing output and theming. There's support for automatic piping and file concatenation

[![bat-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--hPPPnAo8--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/VND3Y9s/bat.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--hPPPnAo8--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/VND3Y9s/bat.png)

[![View bat on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--Ww4gfxNu--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/sharkdp/bat%3Fcolor%3D232323%26label%3Dbat%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/sharkdp/bat) [![Author sharkdp](https://res.cloudinary.com/practicaldev/image/fetch/s--SxH6JTRb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/sharkdp-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/sharkdp)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install bat

# Arch Linux
sudo pacman -S bat

# Debian / Ubuntu
sudo apt install bat 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-diffsofancy-endraw-file-comparisons-better-raw-diff-endraw-"></a>[](#-raw-diffsofancy-endraw-file-comparisons-better-raw-diff-endraw-)[`diff-so-fancy`](https://github.com/so-fancy/diff-so-fancy) \- File Comparisons *(better `diff`)*

> `diff-so-fancy` gives you better looking diffs for comparing strings, files, directories and git changes. The change highlighting makes spotting changes much easier, and you can customize the output layout and colors

[![diff-so-fancy-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--BahI35Zk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/RGKLhQk/diff-so-fancy.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--BahI35Zk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/RGKLhQk/diff-so-fancy.png)

[![View diff-so-fancy on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--y8GbgCuJ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/so-fancy/diff-so-fancy%3Fcolor%3D232323%26label%3Ddiff-so-fancy%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/so-fancy/diff-so-fancy) [![Author so-fancy](https://res.cloudinary.com/practicaldev/image/fetch/s---TRjUa8j--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/so-fancy-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/so-fancy)[![Written in Perl](https://res.cloudinary.com/practicaldev/image/fetch/s--4p7NP6eo--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPerl%26color%3D39457E%26logo%3Dperl%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--4p7NP6eo--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPerl%26color%3D39457E%26logo%3Dperl%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install diff-so-fancy

# Arch Linux
sudo pacman -S diff-so-fancy

# Debian / Ubuntu
sudo apt install diff-so-fancy 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-entr-endraw-watch-for-changes"></a>[](#-raw-entr-endraw-watch-for-changes)[`entr`](https://github.com/eradman/entr) \- Watch for changes

> `entr` lets you run an arbitrary command whenever file changes. You can pass a file, directory, symlink or regex to specify which files it should watch. It's really useful for automatically rebuilding projects, reacting to logs, automated testing, etc. Unlike similar projects, it uses kqueue(2) or inotify(7) to avoid polling, and improve performance

[![entr-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--7isTJ7zR--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/HHKQx2H/entr.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--7isTJ7zR--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/HHKQx2H/entr.png)

[![View entr on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--NFDMuGwi--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/eradman/entr%3Fcolor%3D232323%26label%3Dentr%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/eradman/entr) [![Author eradman](https://res.cloudinary.com/practicaldev/image/fetch/s--3k8d1ieo--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/eradman-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/eradman)[![Written in C](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install entr

# Arch Linux
sudo pacman -S entr

# Debian / Ubuntu
sudo apt install entr 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-exiftool-endraw-reading-writing-metadata"></a>[](#-raw-exiftool-endraw-reading-writing-metadata)[`exiftool`](https://github.com/exiftool/exiftool) \- Reading + writing metadata

> ExifTool is handy utility for reading, writing, stripping and creating meta information for a wide variety of file types. Never accidentally leak your location when sharing a photo again!

[![exiftool-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--R3gSjE8h--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/Gv5PN6v/exiftool.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--R3gSjE8h--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/Gv5PN6v/exiftool.png)

[![View exiftool on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--nSGITJDc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/exiftool/exiftool%3Fcolor%3D232323%26label%3Dexiftool%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/exiftool/exiftool) [![Author exiftool](https://res.cloudinary.com/practicaldev/image/fetch/s--O9Az2q4U--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/exiftool-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/exiftool)[![Written in Perl](https://res.cloudinary.com/practicaldev/image/fetch/s--4p7NP6eo--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPerl%26color%3D39457E%26logo%3Dperl%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--4p7NP6eo--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPerl%26color%3D39457E%26logo%3Dperl%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-fdupes-endraw-duplicate-file-finder"></a>[](#-raw-fdupes-endraw-duplicate-file-finder)[`fdupes`](https://github.com/jbruchon/jdupes) \- Duplicate file finder

> `jdupes` is used for identifying and/or deleting duplicate files within specified directories. It's useful for freeing up disk space when you've got two or more identical files

[![fdupes-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--u0WU9v67--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/jhSY2Nn/fdupes.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--u0WU9v67--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/jhSY2Nn/fdupes.png)

[![View jdupes on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--99_CghNS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/jbruchon/jdupes%3Fcolor%3D232323%26label%3Djdupes%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/jbruchon/jdupes) [![Author jbruchon](https://res.cloudinary.com/practicaldev/image/fetch/s--vgIP6u8c--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/jbruchon-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/jbruchon)[![Written in C](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-fzf-endraw-fuzzy-file-finder-better-raw-find-endraw-"></a>[](#-raw-fzf-endraw-fuzzy-file-finder-better-raw-find-endraw-)[`fzf`](https://github.com/junegunn/fzf) \- Fuzzy file finder *(better `find`)*

> `fzf` is an extremely powerful, and easy to use fuzzy file finder and filtering tool. It lets you search for a string or pattern across files. fzf also has [plugins](https://github.com/junegunn/fzf/wiki/Related-projects) available for most shells and IDEs, for showing instant results while searching. This [post](https://www.freecodecamp.org/news/fzf-a-command-line-fuzzy-finder-missing-demo-a7de312403ff/) by Alexey Samoshkin highlights some of it's use cases.

<img width="678" height="364" src="https://res.cloudinary.com/practicaldev/image/fetch/s---VBiXRJW--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.ibb.co/LNcwjWm/fzf.gif"/>

[![View fzf on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--X-I9wLp_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/junegunn/fzf%3Fcolor%3D232323%26label%3Dfzf%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/junegunn/fzf) [![Author junegunn](https://res.cloudinary.com/practicaldev/image/fetch/s--9-7AwB7k--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/junegunn-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/junegunn)[![Written in Go](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install fzf

# Arch Linux
sudo pacman -S fzf

# Debian / Ubuntu
sudo apt install fzf 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-hyperfine-endraw-command-benchmarking"></a>[](#-raw-hyperfine-endraw-command-benchmarking)[`hyperfine`](https://github.com/sharkdp/hyperfine) \- Command benchmarking

> `hyperfine` makes it easy to accurately benchmark and compare arbitrary commands or scripts. It takes care of warm-up runs, clearing the cache for accurate results and preventing interference from other programs. It can also export results as raw data and generate charts.

[![hyperfine-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--n63ClWNS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/tKNR5gr/hyperfine.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--n63ClWNS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/tKNR5gr/hyperfine.png)

[![View hyperfine on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--p3eYWOF1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/sharkdp/hyperfine%3Fcolor%3D232323%26label%3Dhyperfine%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/sharkdp/hyperfine) [![Author sharkdp](https://res.cloudinary.com/practicaldev/image/fetch/s--SxH6JTRb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/sharkdp-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/sharkdp)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install hyperfine

# Arch Linux
sudo pacman -S hyperfine

# Debian / Ubuntu
sudo apt install hyperfine 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-just-endraw-modern-command-runner-better-raw-make-endraw-"></a>[](#-raw-just-endraw-modern-command-runner-better-raw-make-endraw-)[`just`](https://github.com/casey/just) \- Modern command runner *(better `make`)*

> `just` is similar to `make` but with some nice additions. It let's you group your projects commands together into recopies, which can be easily listed and run. Supports aliases, positional arguments, different shells, dot env integration, string interprulation, and pretty much everything else you could need

[![View just on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--KK8XfNDy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/casey/just%3Fcolor%3D232323%26label%3Djust%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/casey/just) [![Author casey](https://res.cloudinary.com/practicaldev/image/fetch/s---zs_ps7T--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/casey-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/casey)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

Install

```
# MacOS (via Homebrew)
brew install just

# Arch Linux
sudo pacman -S just

# Debian / Ubuntu
sudo apt install just 
``` 

[⬆ back to top](#table-of-contents)

### <a id="-raw-jq-endraw-json-processor"></a>[](#-raw-jq-endraw-json-processor)[`jq`](https://github.com/stedolan/jq) \- JSON processor

> `jq` is like `sed`, but for JSON - you can use it to slice and filter and map and transform structured data with ease. It can be used to write complex queries to extract or manipulate JSON data. There's also a [jq playground](https://jqplay.org/) that you can use to try it out, or formulate queries with live feedback

[![View jq on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--lBG91BRc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/stedolan/jq%3Fcolor%3D232323%26label%3Djq%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/stedolan/jq) [![Author stedolan](https://res.cloudinary.com/practicaldev/image/fetch/s--2MCWjr-u--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/stedolan-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/stedolan)[![Written in C](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-most-endraw-multiwindow-scroll-pager-better-less"></a>[](#-raw-most-endraw-multiwindow-scroll-pager-better-less)[`most`](https://www.jedsoft.org/most/) \- Multi-window scroll pager *(better less)*

> `most` is a pager, for reading through long files or command outputs. `most` supports multi-windows and has the option to not wrap text

[![Author Jed](https://res.cloudinary.com/practicaldev/image/fetch/s--X-YeqwJj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/jed-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://www.jedsoft.org/aboutme.html) [![Written in S-Lang](https://res.cloudinary.com/practicaldev/image/fetch/s--_iwHMPfg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DS_Lang%26color%3D000000%26logo%3Dsimkl%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--_iwHMPfg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DS_Lang%26color%3D000000%26logo%3Dsimkl%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-procs-endraw-process-viewer-better-ps"></a>[](#-raw-procs-endraw-process-viewer-better-ps)[`procs`](https://github.com/dalance/procs) \- Process viewer *(better ps)*

> `procs` is an easy to navigate process viewer, it has colored highlighting, makes sorting and searching for processes easy, has tree view and updates in real-time

<img width="678" height="414" src="https://res.cloudinary.com/practicaldev/image/fetch/s--WqRp_Xe5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.ibb.co/y6qhgDX/procs-demo.gif"/>

[![View procs on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--j-vghycc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/dalance/procs%3Fcolor%3D232323%26label%3Dprocs%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/dalance/procs) [![Author dalance](https://res.cloudinary.com/practicaldev/image/fetch/s--Q8a5m3Y0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/dalance-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/dalance)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-rip-endraw-deletion-tool-better-rm"></a>[](#-raw-rip-endraw-deletion-tool-better-rm)[`rip`](https://github.com/nivekuil/rip) \- Deletion tool *(better rm)*

> `rip` is a safe, ergonomic and performant deletion tool. It let's you intuitively remove files and directories, and easily restore deleted files

[![rip-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--nAwxn-IP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.ibb.co/10DTvT2/rip.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--nAwxn-IP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.ibb.co/10DTvT2/rip.gif)

[![View rip on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--BGH30FEd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/nivekuil/rip%3Fcolor%3D232323%26label%3Drip%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/nivekuil/rip) [![Author nivekuil](https://res.cloudinary.com/practicaldev/image/fetch/s--FxIi2281--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/nivekuil-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/nivekuil)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-ripgrep-endraw-search-within-files-better-raw-grep-endraw-"></a>[](#-raw-ripgrep-endraw-search-within-files-better-raw-grep-endraw-)[`ripgrep`](https://github.com/BurntSushi/ripgrep) \- Search within files *(better `grep`)*

> `ripgrep` is a line-oriented search tool that recursively searches the current directory for a regex pattern. It can ignore the contents of `.gitignore` and skip binary files. It's able to search within compressed archives, or only search specific extension, and understands files using various encoding methods

[![ripgrep-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--CmvC7yAB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/qkMgQm9/ripgrep.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--CmvC7yAB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/qkMgQm9/ripgrep.png)

[![View ripgrep on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--HlBm8eGc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/BurntSushi/ripgrep%3Fcolor%3D232323%26label%3Dripgrep%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/BurntSushi/ripgrep) [![Author BurntSushi](https://res.cloudinary.com/practicaldev/image/fetch/s--7JP-Jeyh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/BurntSushi-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/BurntSushi)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-rsync-endraw-fast-incremental-file-transfer"></a>[](#-raw-rsync-endraw-fast-incremental-file-transfer)[`rsync`](https://rsync.samba.org/) \- Fast, incremental file transfer

> `rsync` lets you copy large files locally or to or from remote hosts or external drives. It can be used to keep files across multiple locations synced, and is perfect for creating, updating and restoring backups

[![View rsync on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--TE03uonE--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/WayneD/rsync%3Fcolor%3D232323%26label%3Drsync%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/WayneD/rsync) [![Author WayneD](https://res.cloudinary.com/practicaldev/image/fetch/s--ZHFZ704t--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/WayneD-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/WayneD)[![Written in C](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-sd-endraw-find-and-replace-better-raw-sed-endraw-"></a>[](#-raw-sd-endraw-find-and-replace-better-raw-sed-endraw-)[`sd`](https://github.com/chmln/sd) \- Find and replace *(better `sed`)*

> `sd` is an easy, fast and intuitive find and replace tool, based on string literals. It can be executed on a file, an entire directory, or any piped text

[![sd-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--5oTimteF--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/G9CfcGS/sd.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--5oTimteF--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/G9CfcGS/sd.png)

[![View sd on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--g4plX8A5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/chmln/sd%3Fcolor%3D232323%26label%3Dsd%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/chmln/sd) [![Author chmln](https://res.cloudinary.com/practicaldev/image/fetch/s--3SZhtztB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/chmln-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/chmln)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-tre-endraw-directory-hierarchy-better-raw-tree-endraw-"></a>[](#-raw-tre-endraw-directory-hierarchy-better-raw-tree-endraw-)[`tre`](https://github.com/dduan/tre) \- Directory hierarchy *(better `tree`)*

> `tre` outputs a tree stye list of files for your current or a specified directory, with colors. When running with the `-e` option, it numbers each item, and creates a temporary alias that you can use to quickly jump to that location

[![tre-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--AltLlVoH--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/CmMrZLB/tre.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--AltLlVoH--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/CmMrZLB/tre.png)

[![View tre on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--HSyAtyGc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/dduan/tre%3Fcolor%3D232323%26label%3Dtre%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/dduan/tre) [![Author dduan](https://res.cloudinary.com/practicaldev/image/fetch/s--7I0zM0fX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/dduan-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/dduan)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-xsel-endraw-access-the-clipboard"></a>[](#-raw-xsel-endraw-access-the-clipboard)[`xsel`](https://github.com/kfish/xsel) \- Access the clipboard

> `xsel` let's you read and write to the X Selection clipboard via the command line. It's useful for piping command output to the clipboard, or a copied data into a command

[![View xsel on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--uz8hh1N---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/kfish/xsel%3Fcolor%3D232323%26label%3Dxsel%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/kfish/xsel) [![Author kfish](https://res.cloudinary.com/practicaldev/image/fetch/s--It91r1bB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/kfish-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/kfish)[![Written in C](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)


## <a id="cli-monitoring-and-performance-apps"></a>[](#cli-monitoring-and-performance-apps)CLI Monitoring and Performance Apps

### <a id="-raw-bandwhich-endraw-bandwidth-utilization-monitor"></a>[](#-raw-bandwhich-endraw-bandwidth-utilization-monitor)[`bandwhich`](https://github.com/imsnif/bandwhich) \- Bandwidth utilization monitor

> Show bandwidth usage, connection information, outgoing hosts and DNS queries in real-time

[![bandwhich-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--y_6Dadgj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/8jHHBD3/Screenshot-from-2023-01-18-22-45-32.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--y_6Dadgj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/8jHHBD3/Screenshot-from-2023-01-18-22-45-32.png)

[![View bandwhich on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--YaBK0m0Q--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/imsnif/bandwhich%3Fcolor%3D232323%26label%3Dbandwhich%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/imsnif/bandwhich) [![Author imsnif](https://res.cloudinary.com/practicaldev/image/fetch/s--1jwkugBA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/imsnif-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/imsnif)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-ctop-endraw-container-metrics-and-monitoring"></a>[](#-raw-ctop-endraw-container-metrics-and-monitoring)[`ctop`](https://github.com/bcicen/ctop) \- Container metrics and monitoring

> Like `top`, but for monitoring resource usage for running (Docker and runC) containers. It shows real-time CPU, memory and network bandwidth as well as the name, status and ID of each container. There's also a built-in log viewer, and options to manage (stop, start, exec, etc) containers

<img width="678" height="352" src="https://res.cloudinary.com/practicaldev/image/fetch/s--vdKvkGu6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.ibb.co/xGjyzZ2/ctop.gif"/>

[![View ctop on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--_c0PKhrS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/bcicen/ctop%3Fcolor%3D232323%26label%3Dctop%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/bcicen/ctop) [![Author bcicen](https://res.cloudinary.com/practicaldev/image/fetch/s--D5Zufd7K--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/bcicen-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/bcicen)[![Written in Go](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-bpytop-endraw-resource-monitoring-better-raw-htop-endraw-"></a>[](#-raw-bpytop-endraw-resource-monitoring-better-raw-htop-endraw-)[`bpytop`](https://github.com/aristocratos/bpytop) \- Resource monitoring *(better `htop`)*

> `bpytop` is a fast, interactive, visual resource monitor. It shows top running processes, recent CPU, mem, disk and network history. From the interface you can navigate, sort and search - there's also support for custom color themes

<img width="678" height="351" src="https://res.cloudinary.com/practicaldev/image/fetch/s--xRcMVtCB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.ibb.co/nj9jrhr/bpytop.gif"/>

[![View bpytop on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--La1slgzg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/aristocratos/bpytop%3Fcolor%3D232323%26label%3Dbpytop%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/aristocratos/bpytop) [![Author aristocratos](https://res.cloudinary.com/practicaldev/image/fetch/s--OWZPdkTK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/aristocratos-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/aristocratos)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-glances-endraw-resource-monitor-web-and-api"></a>[](#-raw-glances-endraw-resource-monitor-web-and-api)[`glances`](https://github.com/nicolargo/glances) \- Resource monitor + web and API

> `glances` is another resource monitor, but with a different feature set. It includes a fully responsive web view, a REST API and historical monitoring. It's easily extendable, and can be integrated with other services

<img width="678" height="352" src="https://res.cloudinary.com/practicaldev/image/fetch/s--6Wp2nhqx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.ibb.co/6g65Qy4/glances.gif"/>

[![View glances on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--BiqyIr4q--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/nicolargo/glances%3Fcolor%3D232323%26label%3Dglances%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/nicolargo/glances) [![Author nicolargo](https://res.cloudinary.com/practicaldev/image/fetch/s--ngsgYxo---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/nicolargo-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/nicolargo)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-gping-endraw-interactive-ping-tool-better-raw-ping-endraw-"></a>[](#-raw-gping-endraw-interactive-ping-tool-better-raw-ping-endraw-)[`gping`](https://github.com/orf/gping) \- Interactive ping tool *(better `ping`)*

> `gping` can run ping tests on multiple hosts, while showing results in real-time graph. It can also be used to monitor execution time, when used with the `--cmd` flag

<img width="678" height="360" src="https://res.cloudinary.com/practicaldev/image/fetch/s--YMe9lAFT--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.ibb.co/CvG6xt0/gping.gif"/>

[![View gping on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--VRt0ZkHq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/orf/gping%3Fcolor%3D232323%26label%3Dgping%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/orf/gping) [![Author orf](https://res.cloudinary.com/practicaldev/image/fetch/s--BjIBTvQQ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/orf-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/orf)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-duacli-endraw-disk-usage-analyzer-and-monitor-better-raw-du-endraw-"></a>[](#-raw-duacli-endraw-disk-usage-analyzer-and-monitor-better-raw-du-endraw-)[`dua-cli`](https://github.com/Byron/dua-cli) \- Disk usage analyzer and monitor *(better `du`)*

> `dua-cli` let's you interactively view used and available disk space for each mounted drive, and makes freeing up storage easy

<img width="678" height="365" src="https://res.cloudinary.com/practicaldev/image/fetch/s--nle07K3Z--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.ibb.co/x3NbDLR/dua.gif"/>

[![View dua-cli on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--uSqjiQ8o--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/Byron/dua-cli%3Fcolor%3D232323%26label%3Ddua-cli%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/Byron/dua-cli) [![Author Byron](https://res.cloudinary.com/practicaldev/image/fetch/s--lnGYFEPy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/Byron-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/Byron)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-speedtestcli-endraw-command-line-speed-test-utility"></a>[](#-raw-speedtestcli-endraw-command-line-speed-test-utility)[`speedtest-cli`](https://github.com/sivel/speedtest-cli) \- Command line speed test utility

> `speedtest-cli` just runs an internet speed test, via speedtest.net - but straight from the terminal :)

<img width="678" height="360" src="https://res.cloudinary.com/practicaldev/image/fetch/s--qFJxYj0D--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.ibb.co/25QCbdF/speedtest-cli.gif"/>

[![View speedtest-cli on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--iSo8TCej--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/sivel/speedtest-cli%3Fcolor%3D232323%26label%3Dspeedtest-cli%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/sivel/speedtest-cli) [![Author sivel](https://res.cloudinary.com/practicaldev/image/fetch/s--ko5jqrC6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/sivel-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/sivel)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-dog-endraw-dns-lookup-client-better-raw-dig-endraw-"></a>[](#-raw-dog-endraw-dns-lookup-client-better-raw-dig-endraw-)[`dog`](https://github.com/ogham/dog) \- DNS lookup client *(better `dig`)*

> `dog` is an easy-to-use DNS lookup client, with support for DoT and DoH, nicely coloured outputs and the option to emit JSON

[![dog-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--iOnIsJRk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/48n617Q/dog.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--iOnIsJRk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/48n617Q/dog.png)

[![View dog on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--0wchjDFj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/ogham/dog%3Fcolor%3D232323%26label%3Ddog%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/ogham/dog) [![Author ogham](https://res.cloudinary.com/practicaldev/image/fetch/s--QC1gNgew--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/ogham-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/ogham)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)



## <a id="cli-productivity-apps"></a>[](#cli-productivity-apps)CLI Productivity Apps

> Surf the web, play music, check emails, manage calendars, read the news and more, all without leaving the terminal!

### <a id="-raw-browsh-endraw-cli-web-browser"></a>[](#-raw-browsh-endraw-cli-web-browser)[`browsh`](https://github.com/browsh-org/browsh) \- CLI web browser

> `browsh` is a fully interactive, real-time, and modern text-based browser rendered to TTYs and browsers. It supports both mouse and keyboard navigation, and is surprisingly feature rich for a purely terminal based application. It also mitigates battery drain issues that plague modern browsers, and with support for MoSH, you can experience faster load times due to reduced bandwidth

![browsh-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--sO3TkLzU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.ibb.co/S7nLFX5/browsh.gif)

[![View browsh on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--B0DoDYCJ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/browsh-org/browsh%3Fcolor%3D232323%26label%3Dbrowsh%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/browsh-org/browsh) [![Author browsh-org](https://res.cloudinary.com/practicaldev/image/fetch/s--T9t-an-Z--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/browsh-org-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/browsh-org)[![Written in JavaScript](https://res.cloudinary.com/practicaldev/image/fetch/s--cgqT0lN_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DJavaScript%26color%3DF7DF1E%26logo%3Djavascript%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--cgqT0lN_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DJavaScript%26color%3DF7DF1E%26logo%3Djavascript%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-buku-endraw-bookmark-manager"></a>[](#-raw-buku-endraw-bookmark-manager)[`buku`](https://github.com/jarun/buku) \- Bookmark manager

> `buku` is a terminal-based bookmark manager, with tons of configuration, storage and usage options. There's also an optional [web UI](https://github.com/jarun/buku/tree/master/bukuserver#screenshots) and [browser plugin](https://github.com/samhh/bukubrow-webext#installation), for accessing your bookmarks outside of the terminal

[![buku-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--vcrdyl0t--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/CWQsf1x/buku.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--vcrdyl0t--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/CWQsf1x/buku.png)

[![View buku on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--GfhqzUB1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/jarun/buku%3Fcolor%3D232323%26label%3Dbuku%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/jarun/buku) [![Author jarun](https://res.cloudinary.com/practicaldev/image/fetch/s--WtZ39WFW--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/jarun-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/jarun)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-cmus-endraw-music-browser-player"></a>[](#-raw-cmus-endraw-music-browser-player)[`cmus`](https://github.com/cmus/cmus) \- Music browser / player

> `cmus` is terminal music player, controlled with keyboard shortcuts. It has support for a wide range of audio formats and codecs, and allows organising tracks into playlists and applying playback settings

[![cmus-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--X-hFmnWf--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/dP6b3bd/cmus.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--X-hFmnWf--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/dP6b3bd/cmus.png)

[![View cmus on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--SrUzdOws--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/cmus/cmus%3Fcolor%3D232323%26label%3Dcmus%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/cmus/cmus) [![Author cmus](https://res.cloudinary.com/practicaldev/image/fetch/s--XhG1tvtx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/cmus-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/cmus)[![Written in C](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-cointop-endraw-track-crypto-prices"></a>[](#-raw-cointop-endraw-track-crypto-prices)[`cointop`](https://github.com/cointop-sh/cointop) \- Track crypto prices

> `cointop` show current crypto prices, and track the price history of your portfolio. Supports price alerts, historical charts, currency conversion, fuzzy searching, and much more. You can try the demo via the web at [cointop.sh](https://cointop.sh/), or by running `ssh cointop.sh`

[![cointop-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--t890F5P5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/JBf9y4y/cointop.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--t890F5P5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/JBf9y4y/cointop.png)

[![View cointop on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--FRegAPoj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/cointop-sh/cointop%3Fcolor%3D232323%26label%3Dcointop%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/cointop-sh/cointop) [![Author cointop-sh](https://res.cloudinary.com/practicaldev/image/fetch/s--HtEsM_Y1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/cointop-sh-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/cointop-sh)[![Written in Go](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-ddgr-endraw-search-the-web-from-the-terminal"></a>[](#-raw-ddgr-endraw-search-the-web-from-the-terminal)[`ddgr`](https://github.com/jarun/ddgr) \- Search the web from the terminal

> `ddgr` is like [googler](https://github.com/jarun/googler), but for DuckDuckGo. It's fast, clean and easy, with support for instant answers, search completion, search bangs, and advanced search. It respects your privacy by default, and also has HTTPS proxy support, and works with Tor

[![dggr-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--xbxemVB3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/S0H21QH/dggr.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--xbxemVB3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/S0H21QH/dggr.png)

[![View ddgr on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--H8HIfCdf--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/jarun/ddgr%3Fcolor%3D232323%26label%3Dddgr%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/jarun/ddgr) [![Author jarun](https://res.cloudinary.com/practicaldev/image/fetch/s--WtZ39WFW--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/jarun-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/jarun)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-micro-endraw-code-editor-better-raw-nano-endraw-"></a>[](#-raw-micro-endraw-code-editor-better-raw-nano-endraw-)[`micro`](https://github.com/zyedidia/micro) \- Code editor *(better `nano`)*

> `micro` is an easy to use, fast and extendable code editor with mouse support. Since it's packaged into a single binary, installation is as simple as `curl https://getmic.ro | bash`

[![micro-screenshot](https://res.cloudinary.com/practicaldev/image/fetch/s--IzOVcyTT--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/cgNcH7w/Screenshot-from-2023-01-21-19-18-04.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--IzOVcyTT--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/cgNcH7w/Screenshot-from-2023-01-21-19-18-04.png)

[![View micro on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--KRGBV_BC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/zyedidia/micro%3Fcolor%3D232323%26label%3Dmicro%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/zyedidia/micro) [![Author zyedidia](https://res.cloudinary.com/practicaldev/image/fetch/s--6uyJKAc1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/zyedidia-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/zyedidia)[![Written in Go](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-khal-endraw-calendar-client"></a>[](#-raw-khal-endraw-calendar-client)[`khal`](https://github.com/pimutils/khal) \- Calendar client

> `khal` is a terminal calendar app, which shows upcoming events, month and agenda views. You can sync it with any CalDAV calendar, and add, edit and remove events directly

[![khal-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--9YOqO5S5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/hLCdjZW/khal.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--9YOqO5S5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/hLCdjZW/khal.png)

[![View khal on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--hfkwGpeh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/pimutils/khal%3Fcolor%3D232323%26label%3Dkhal%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/pimutils/khal) [![Author pimutils](https://res.cloudinary.com/practicaldev/image/fetch/s--36DhLHOm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/pimutils-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/pimutils)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-mutt-endraw-email-client"></a>[](#-raw-mutt-endraw-email-client)[`mutt`](https://gitlab.com/muttmua/mutt) \- Email client

> `mut` is a classic, a terminal based mail client for sending, reading and managing emails. It supports all mainstream email protocols and mailbox formats, allows for attachments, BCC/CC, threads, mailing lists and delivery status notifications

[![mutt-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--VwdNaLYL--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/zVVsG3s/mutt.webp)](https://res.cloudinary.com/practicaldev/image/fetch/s--VwdNaLYL--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/zVVsG3s/mutt.webp)

[![View mutt on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--bDGB9Uh1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/muttmua/mutt%3Fcolor%3D232323%26label%3Dmutt%26logo%3Dgithub%26labelColor%3D232323)](https://gitlab.com/muttmua/mutt) [![Author muttmua](https://res.cloudinary.com/practicaldev/image/fetch/s--WUXrosd1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/muttmua-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/muttmua)[![Written in C](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-newsboat-endraw-rss-atom-news-reader"></a>[](#-raw-newsboat-endraw-rss-atom-news-reader)[`newsboat`](https://github.com/newsboat/newsboat) \- RSS / ATOM news reader

> `newsboat` is an RSS feed reader and aggregator, for reading the news, blogs and following updates directly from the terminal

[![newsboat-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--BPuEuPaC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/fvT4YzD/newsboat.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--BPuEuPaC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/fvT4YzD/newsboat.png)

[![View newsboat on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--Tou5KnGz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/newsboat/newsboat%3Fcolor%3D232323%26label%3Dnewsboat%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/newsboat/newsboat) [![Author newsboat](https://res.cloudinary.com/practicaldev/image/fetch/s--2eLnD5li--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/newsboat-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/newsboat)[![Written in C++](https://res.cloudinary.com/practicaldev/image/fetch/s--tO0jFOIW--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--tO0jFOIW--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-rclone-endraw-manage-cloud-storage"></a>[](#-raw-rclone-endraw-manage-cloud-storage)[`rclone`](https://github.com/rclone/rclone) \- Manage cloud storage

> `rclone` is a handy utility for syncing files and folders to various cloud storage providers. It can be either invoked directly from the command line, or easily integrated into a script as a replacement for heavy desktop sync apps

[![View rclone on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--Ql0VUkv2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/rclone/rclone%3Fcolor%3D232323%26label%3Drclone%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/rclone/rclone) [![Author rclone](https://res.cloudinary.com/practicaldev/image/fetch/s--9kE435sB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/rclone-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/rclone)[![Written in Go](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-taskwarrior-endraw-todo-task-management"></a>[](#-raw-taskwarrior-endraw-todo-task-management)[`taskwarrior`](https://github.com/GothenburgBitFactory/taskwarrior) \- Todo + task management

> `task` is a CLI task management/ todo app. It's both simple and unobtrusive, but also incredibly powerful and scalable, with advanced organisation and query features built in. There's also a lot (700+!) of extra [plugins](https://taskwarrior.org/tools/) for extending it's functionality and integrating with third-party services

[![task-warrior-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--QeqQw1O0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/7k6M37g/taskwarrior.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--QeqQw1O0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/7k6M37g/taskwarrior.jpg)

[![View taskwarrior on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--DZ1p5A9N--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/GothenburgBitFactory/taskwarrior%3Fcolor%3D232323%26label%3Dtaskwarrior%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/GothenburgBitFactory/taskwarrior) [![Author GothenburgBitFactory](https://res.cloudinary.com/practicaldev/image/fetch/s--qZ_quxiy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/GothenburgBitFactory-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/GothenburgBitFactory)[![Written in C++](https://res.cloudinary.com/practicaldev/image/fetch/s--tO0jFOIW--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--tO0jFOIW--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-tuir-endraw-terminal-ui-for-reddit"></a>[](#-raw-tuir-endraw-terminal-ui-for-reddit)[`tuir`](https://gitlab.com/ajak/tuir) \- Terminal UI for Reddit

> `tuir` is a great one if you want to look like you're working, while actually browsing Reddit! It's got intuitive keybindings, custom themes, and can render images and multi-media content too. There's also [haxor](https://github.com/donnemartin/haxor-news) for hacker news

[![tuir-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--QttDR9ja--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/vzSw7s5/tuir.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--QttDR9ja--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/vzSw7s5/tuir.png)

[![View tuir on GitLab](https://res.cloudinary.com/practicaldev/image/fetch/s--E80F2_ic--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/gitlab/stars/ajak/tuir%3Fcolor%3Dfc6d26%26label%3Dtuir%26logo%3Dgitlab%26labelColor%3D232323)](https://gitlab.com/ajak/tuir) [![Author ajak](https://res.cloudinary.com/practicaldev/image/fetch/s--oqGk8Nye--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/ajak-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/ajak)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)



## <a id="cli-dev-suits"></a>[](#cli-dev-suits)CLI Dev Suits

### <a id="-raw-httpie-endraw-http-api-testing-testing-client"></a>[](#-raw-httpie-endraw-http-api-testing-testing-client)[`httpie`](https://github.com/httpie/httpie) \- HTTP / API testing testing client

> `httpie` is a HTTP client, for testing, debugging and using APIs. It supports everything you'd expect - HTTPS, proxies, authentication, custom headers, persistent sessions, JSON parsing. Usage is simple with an expressive syntax and colourized output. Like other HTTP clients (Postman, Hopscotch, Insomnia, etc) HTTPie also includes a web UI

[![httpie-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--GCvEbIXw--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/Wk5S19g/httpie.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--GCvEbIXw--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/Wk5S19g/httpie.png)

[![View httpie on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--Dnl_-FV6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/httpie/httpie%3Fcolor%3D232323%26label%3Dhttpie%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/httpie/httpie) [![Author httpie](https://res.cloudinary.com/practicaldev/image/fetch/s--i8Sspvsd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/httpie-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/httpie)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-lazydocker-endraw-full-docker-management-app"></a>[](#-raw-lazydocker-endraw-full-docker-management-app)[`lazydocker`](https://github.com/jesseduffield/lazydocker) \- Full Docker management app

> `lazydocker` is a Docker management app, that lets you view all containers and images, manage their state, read logs, check resource usage, restart/ rebuild, analyse layers, prune unused containers, images and volumes, and so much more. It saves you from needing remember, type and chain multiple Docker commands.

[![lazy-docker-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--t3qjWKXi--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/MD8MWNH/lazydocker.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--t3qjWKXi--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/MD8MWNH/lazydocker.png)

[![View lazydocker on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--SXsHiDMk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/jesseduffield/lazydocker%3Fcolor%3D232323%26label%3Dlazydocker%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/jesseduffield/lazydocker) [![Author jesseduffield](https://res.cloudinary.com/practicaldev/image/fetch/s--k-sMPQEG--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/jesseduffield-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/jesseduffield)[![Written in Go](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-lazygit-endraw-full-git-management-app"></a>[](#-raw-lazygit-endraw-full-git-management-app)[`lazygit`](https://github.com/jesseduffield/lazygit) \- Full Git management app

> `lazygit` is a visual git client, on the command line. Easily add, commit and puch files, resolve conflicts, compare diffs, manage logs, and do complex operations like squashes and rewinds. There's keybindings for everything, colors, and it's easily configurable and extenable

[![lazy-git-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--rF4wSFzE--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/KLF3C6s/lazygit.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--rF4wSFzE--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/KLF3C6s/lazygit.png)

[![View lazygit on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--MPsuMx8k--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/jesseduffield/lazygit%3Fcolor%3D232323%26label%3Dlazygit%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/jesseduffield/lazygit) [![Author jesseduffield](https://res.cloudinary.com/practicaldev/image/fetch/s--k-sMPQEG--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/jesseduffield-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/jesseduffield)[![Written in Go](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-kdash-endraw-kubernetes-dashboard-app"></a>[](#-raw-kdash-endraw-kubernetes-dashboard-app)[`kdash`](https://github.com/kdash-rs/kdash/) \- Kubernetes dashboard app

> `kdash` is an all-in-one Kubernetes management tool. View node metrics, watch resources, stream container logs, analyse contexts and manage nodes, pods and namespaces

[![View kdash on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--Vzqnocxw--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/kdash-rs/kdash%3Fcolor%3D232323%26label%3Dkdash%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/kdash-rs/kdash/) [![Author kdash-rs](https://res.cloudinary.com/practicaldev/image/fetch/s--7GpSXjoX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/kdash-rs-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/kdash-rs)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-gdpdashboard-endraw-visual-gdp-debugger"></a>[](#-raw-gdpdashboard-endraw-visual-gdp-debugger)[`gdp-dashboard`](https://github.com/cyrus-and/gdb-dashboard) \- Visual GDP debugger

> `gdp-dashboard` adds a visual element to the GNU Debugger, for debugging C and C++ programs. Easily analyse memory, step through breakpoints, and view registers

[![gdp-dashboard-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--kbRmT8iS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/2g2hVLh/gdp-dashboard.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--kbRmT8iS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/2g2hVLh/gdp-dashboard.png)

[![View gdb-dashboard on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--t2fhQI36--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/cyrus-and/gdb-dashboard%3Fcolor%3D232323%26label%3Dgdb-dashboard%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/cyrus-and/gdb-dashboard) [![Author cyrus-and](https://res.cloudinary.com/practicaldev/image/fetch/s--0wBnPb3Q--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/cyrus-and-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/cyrus-and)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

## <a id="cli-external-sercvices"></a>[](#cli-external-sercvices)CLI External Sercvices

### <a id="-raw-ngrok-endraw-reverse-proxy-for-sharing-localhost"></a>[](#-raw-ngrok-endraw-reverse-proxy-for-sharing-localhost)[`ngrok`](https://ngrok.com/) \- Reverse proxy for sharing localhost

> `ngrok` safely* exposes your localhost to the internet behind a unique URL. This lets you share what you're working on with you're remote colleagues, in real-time. Usage is [very simple](https://notes.aliciasykes.com/p/RUi22QSyWe), but it's also got a lot of advanced features for things like authentication, webhooks, firewalls, traffic inspection, custom/ wildcard domains and much more

[![ngrok-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--SIjfLNwV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/4WPZNGx/ngrok.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--SIjfLNwV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/4WPZNGx/ngrok.png)

[![View ngrok on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--EkQ3uF4g--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/inconshreveable/ngrok%3Fcolor%3D232323%26label%3Dngrok%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/inconshreveable/ngrok) [![Author inconshreveable](https://res.cloudinary.com/practicaldev/image/fetch/s--XAQdMrb6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/inconshreveable-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/inconshreveable)[![Written in Go](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-tmate-endraw-share-a-terminal-session-via-internet"></a>[](#-raw-tmate-endraw-share-a-terminal-session-via-internet)[`tmate`](https://tmate.io/) \- Share a terminal session via internet

> `tmate` let's you instantly share a live terminal session with someone elsewhere in the world. It works across different systems, supports access control/ auth, can be self-hosted, and has all the features of Tmux

[![View tmate on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--HsJ28khW--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/tmate-io/tmate%3Fcolor%3D232323%26label%3Dtmate%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/tmate-io/tmate) [![Author tmate-io](https://res.cloudinary.com/practicaldev/image/fetch/s--gzhBPUaT--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/tmate-io-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/tmate-io)[![Written in C](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-asciinema-endraw-recording-sharing-terminal-sessions"></a>[](#-raw-asciinema-endraw-recording-sharing-terminal-sessions)[`asciinema`](https://asciinema.org/) \- Recording + sharing terminal sessions

> `asciinema` is very useful for easily recording, sharing and embedding a terminal session. Great to showcase something you've built, or to show the command-line steps for a tutorial. Unlike screenrecording videos, the user can copy-paste the content, change the theme on the fly and control playback

[![View asciinema on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--VrN2hZMU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/asciinema/asciinema%3Fcolor%3D232323%26label%3Dasciinema%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/asciinema/asciinema) [![Author asciinema](https://res.cloudinary.com/practicaldev/image/fetch/s--VpxT2-Ie--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/asciinema-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/asciinema)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-navi-endraw-interactive-cheat-sheet"></a>[](#-raw-navi-endraw-interactive-cheat-sheet)[`navi`](https://github.com/denisidoro/navi) \- Interactive cheat sheet

> `navi` allows you to browse through cheatsheets and execute commands. Suggested values for arguments are dynamically displayed in a list. Type less, reduce mistakes and save yourself from having to memorise thousands of commands. It integrates with [tldr](https://github.com/tldr-pages/tldr) and [cheat.sh](https://github.com/chubin/cheat.sh) to get content, but you can also import other cheatsheets, or even write your own

[![View navi on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--deBs-uAe--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/denisidoro/navi%3Fcolor%3D232323%26label%3Dnavi%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/denisidoro/navi) [![Author denisidoro](https://res.cloudinary.com/practicaldev/image/fetch/s--wZCh1Ptl--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/denisidoro-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/denisidoro)[![Written in Rust](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--QnEL4tqy--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-transfersh-endraw-fast-file-sharing"></a>[](#-raw-transfersh-endraw-fast-file-sharing)[`transfer.sh`](https://github.com/dutchcoders/transfer.sh/) \- Fast file sharing

> `transfer` makes uploading and sharing files really easy, directly from the command line. It's free, supports encryption, gives you a unique URL, and can also be self-hosted.
> I've written a Bash helper function to make usage a bit easier, you can [find it here](https://github.com/Lissy93/dotfiles/blob/master/utils/transfer.sh) or try it out by running `bash <(curl -L -s https://alicia.url.lol/transfer)`

[![transfer-sh-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--3Xa_MJUD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/cCqDb1k/transfer-sh.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--3Xa_MJUD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/cCqDb1k/transfer-sh.png)

[![View transfer.sh on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--oQoapBbc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/dutchcoders/transfer.sh%3Fcolor%3D232323%26label%3Dtransfer.sh%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/dutchcoders/transfer.sh) [![Author dutchcoders](https://res.cloudinary.com/practicaldev/image/fetch/s--04qamyZq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/dutchcoders-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/dutchcoders)[![Written in Go](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--6zXuw3Pb--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-surge-endraw-deploy-a-site-in-seconds"></a>[](#-raw-surge-endraw-deploy-a-site-in-seconds)[`surge`](https://surge.sh/) \- Deploy a site in seconds

> `surge` is a free static hosting provider, that you can deploy to directly from the terminal in a single command, just run `surge` from within your `dist` directory! It supports custom domains, auto SSL certs, pushState support, cross-origin resource support - and it's free!

[![surge-sh-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--iKFo9ur---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/NynprxZ/surge-sh.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--iKFo9ur---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/NynprxZ/surge-sh.png)

[⬆ back to top](#table-of-contents)

### <a id="-raw-wttrin-endraw-check-the-weather"></a>[](#-raw-wttrin-endraw-check-the-weather)[`wttr.in`](https://github.com/chubin/wttr.in) \- Check the weather

> `wttr.in` is a service that displays the weather in a format that's digestible in the command line. Just run `curl wttr.in` or `curl wttr.in/London` to try it out. There's URL parameters to customise what data is returned, as well as the format

[![wrrt-in-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--d24wQ08X--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/J2JWnYT/Screenshot-from-2023-01-18-21-10-54.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--d24wQ08X--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/J2JWnYT/Screenshot-from-2023-01-18-21-10-54.png)

[![View wttr.in on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--VQFj_GZA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/chubin/wttr.in%3Fcolor%3D232323%26label%3Dwttr.in%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/chubin/wttr.in) [![Author chubin](https://res.cloudinary.com/practicaldev/image/fetch/s--QLlgb-tx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/chubin-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/chubin)[![Written in Python](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--piMR3xQn--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)



## <a id="cli-fun"></a>[](#cli-fun)CLI Fun

### <a id="-raw-cowsay-endraw-have-an-ascii-cow-say-your-message"></a>[](#-raw-cowsay-endraw-have-an-ascii-cow-say-your-message)[`cowsay`](https://en.wikipedia.org/wiki/Cowsay) \- Have an ASCII cow say your message

> `cowsay` is a configurable talking cow. It's based off the [original](https://github.com/tnalpgge/rank-amateur-cowsay) by Tony Monroe

[![cowsay-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--qNjdMj8x--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/TRqW3jD/cowsay.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--qNjdMj8x--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/TRqW3jD/cowsay.png)

[![View cowsay on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--4xYaURYG--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/piuccio/cowsay%3Fcolor%3D232323%26label%3Dcowsay%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/piuccio/cowsay) [![Author piuccio](https://res.cloudinary.com/practicaldev/image/fetch/s--UybCoy_u--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/piuccio-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/piuccio)[![Written in JavaScript](https://res.cloudinary.com/practicaldev/image/fetch/s--cgqT0lN_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DJavaScript%26color%3DF7DF1E%26logo%3Djavascript%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--cgqT0lN_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DJavaScript%26color%3DF7DF1E%26logo%3Djavascript%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-figlet-endraw-output-text-as-big-ascii-art-text"></a>[](#-raw-figlet-endraw-output-text-as-big-ascii-art-text)[`figlet`](http://www.figlet.org/) \- Output text as big ASCII art text

> `figlet` outputs text as ASCII art

[![figlet-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--Jala8Oxw--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/fk4T7D0/figlet.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--Jala8Oxw--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/fk4T7D0/figlet.png)

[![View figlet on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--7zjEEvB8--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/cmatsuoka/figlet%3Fcolor%3D232323%26label%3Dfiglet%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/cmatsuoka/figlet) [![Author cmatsuoka](https://res.cloudinary.com/practicaldev/image/fetch/s--MeViFs3A--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/cmatsuoka-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/cmatsuoka)[![Written in C](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--RIZ8ybsm--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-lolcat-endraw-make-console-output-raibow-colored"></a>[](#-raw-lolcat-endraw-make-console-output-raibow-colored)[`lolcat`](https://github.com/busyloop/lolcat) \- Make console output raibow colored

> `lolcat` makes any text passed to it rainbow coloured

[![lolcat-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--AUO8rVMr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/nfp9Ycx/lolcat.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--AUO8rVMr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/nfp9Ycx/lolcat.png)

[![View lolcat on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--XIldTiim--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/busyloop/lolcat%3Fcolor%3D232323%26label%3Dlolcat%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/busyloop/lolcat) [![Author busyloop](https://res.cloudinary.com/practicaldev/image/fetch/s--CRMo5JJ0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/busyloop-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/busyloop)[![Written in Ruby](https://res.cloudinary.com/practicaldev/image/fetch/s--DaahHts3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRuby%26color%3DCC342D%26logo%3Druby%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--DaahHts3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DRuby%26color%3DCC342D%26logo%3Druby%26logoColor%3DFFFFFF)

[⬆ back to top](#table-of-contents)

### <a id="-raw-neofetch-endraw-show-system-data-and-ditstro-info"></a>[](#-raw-neofetch-endraw-show-system-data-and-ditstro-info)[`neofetch`](https://github.com/dylanaraps/neofetch) \- Show system data and ditstro info

> `neofetch` prints distro and system info (so you can flex that you use Arch btw on r/unixporn)

[![neofetch-example-usage](https://res.cloudinary.com/practicaldev/image/fetch/s--9vGUZc_0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/x1PHpFC/Screenshot-from-2023-01-18-22-44-28.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--9vGUZc_0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/x1PHpFC/Screenshot-from-2023-01-18-22-44-28.png)

[![View neofetch on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--2s91PX3a--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/dylanaraps/neofetch%3Fcolor%3D232323%26label%3Dneofetch%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/dylanaraps/neofetch) [![Author dylanaraps](https://res.cloudinary.com/practicaldev/image/fetch/s---pytlKVd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/dylanaraps-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/dylanaraps)[![Written in Bash](https://res.cloudinary.com/practicaldev/image/fetch/s--PYCRrB0c--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DBash%26color%3Dgreen%26logo%3Dgnubash%26logoColor%3DFFFFFF)](https://res.cloudinary.com/practicaldev/image/fetch/s--PYCRrB0c--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/static/v1%3Flabel%3D%26message%3DBash%26color%3Dgreen%26logo%3Dgnubash%26logoColor%3DFFFFFF)

As an example, I'm using `cowsay`, `figlet`, `lolcat` and `neofetch` to create a custom time-based MOTD shown to the user when they first log in. It greets them by their name, shows server info and time, date, weather and IP. [Here's the source code](https://github.com/Lissy93/dotfiles/blob/master/utils/welcome-banner.sh).

[![welcome](https://res.cloudinary.com/practicaldev/image/fetch/s--2Zp8xWf0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/cTg0jyn/Screenshot-from-2023-01-18-22-59-28.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--2Zp8xWf0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/cTg0jyn/Screenshot-from-2023-01-18-22-59-28.png)

[⬆ back to top](#table-of-contents)



## <a id="installations-and-management"></a>[](#installations-and-management)Installations and Management

Most of us have a core set of CLI apps and utils that we rely upon. Setting up a new machine, and individually installing each program would get tiresome very quickly. So the task of installing and updating your terminal apps is the perfect candidate for automation. [Here](https://github.com/Lissy93/dotfiles/tree/master/scripts/installs) are some example scripts I've written, which can be easily dropped into your dotfiles or just run independently to ensure you're never missing an app.

For MacOS users, the easiest method is using [Homebrew](https://brew.sh/). Just create a Brewfile (with `touch ~/.Brewfile`), then list each of your apps, and run `brew bundle`. You can keep your package list backed up, by putting it in a Git repo. Here's an example one, to get you started: https://github.com/Lissy93/Brewfile

On Linux, you usually want to use the native package manager (e.g. `pacman`, `apt`). As an example, [here's a script](https://github.com/Lissy93/dotfiles/blob/master/scripts/installs/arch-pacman.sh) to install the above apps on Arch Linux systems

Desktop apps on Linux can be managed in a similar way, via Flatpak. Again, [here's an example script](https://github.com/Lissy93/dotfiles/blob/master/scripts/installs/flatpak.sh) :)

[⬆ back to top](#table-of-contents)

## <a id="conclusion"></a>[](#conclusion)Conclusion

... So that's it - a list of handy CLI apps, and a method for installing and keeping them up-to-date across your systems.

Hopefully some of these will be useful to some of you :)

I'd love to hear what you're favourite CLI apps are, let me know in the comments below!

### <a id="additional-info"></a>[](#additional-info)Additional Info

#### <a id="what-wasnt-included"></a>[](#what-wasnt-included)What wasn't included

- This list doesn't include the basics, like Vim, Tmux, Ranger, ZSH, Git, etc - which you're likely already using
- I've also not included anything too niche, or only specific to a small number of users
- Nothing system-specific, or that isn't cross-platform (Linux/ Unix, MacOS) is included
- And I've not included apps which relate to the terminal, but are not CLI apps (like terminal emulators)
- For most of the projects listed, there's a plethora of alternatives that achieve similar things, for brevity those also weren't included

#### <a id="credit"></a>[](#credit)Credit

Huge kudos to the authors, and communities behind each of these apps. Without them and their hard work, our life in the command line would be much less awesome. Where possible, I've tried to credit the authors, but if I've missed any - let me know below, and I'll push an update

#### <a id="feedback"></a>[](#feedback)Feedback

What have I missed? I'd love to hear your favourite CLI apps, especially if there's something awesome that I've missed!

I'd also like to hear your thoughts and suggestions - I'm always looking to improve :)

#### <a id="badges"></a>[](#badges)Badges

Here's the script that I made to generate the author, language and GitHub star badges:

Repo Badge Generator

## [![GitHub logo](https://res.cloudinary.com/practicaldev/image/fetch/s--566lAguM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev.to/assets/github-logo-5a155e1f9a670af7944dd5e12375bc76ed542ea80224905ecaf878b9157cdefc.svg)](https://res.cloudinary.com/practicaldev/image/fetch/s--566lAguM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev.to/assets/github-logo-5a155e1f9a670af7944dd5e12375bc76ed542ea80224905ecaf878b9157cdefc.svg) [Lissy93](https://github.com/Lissy93) / [repo-badge-maker](https://github.com/Lissy93/repo-badge-maker) 

### 🛡️ Very, very quick script to generate repo badges for blog posts

# 🛡️ Repo Badge Generator

*Very, very quick script to quickly generate repository badges*
**[repo-badges.as93.net](https://repo-badges.as93.net)**

[![](https://camo.githubusercontent.com/c1a6e829ff32fb8eb3982555592d84a97f375c6a54f1ee1e750c76cc1eff3af8/68747470733a2f2f692e6962622e636f2f3756397837646b2f7265706f2d62616467652d67656e657261746f722d73637265656e73686f742d322e706e67)](https://repo-badges.as93.net)

## About

I made this to quickly generate the project links, for this post: [CLI tools you won't be able to live without 🔧](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6)

Just a simple script to generate markdown repo badges using the [Shields.io](https://shields.io/) and GitHub APIs.
Includes a badge for + link to the author, the repo + star count, and the language used.
Paste in the URL to a repo, hit 'Generate', and results will be copied to your clipboard.

## Deployment

It's just a static HTML page, so serve it with any web server, CDN or static host.
There's a demo hosted on GH Pages, at: [lissy93.github.io/repo-badge-maker](https://lissy93.github.io/repo-badge-maker/)

## License

> ***[Lissy93/repo-badge-maker](https://github.com/Lissy93/repo-badge-maker)** is licensed under [MIT](https://gist.github.com/Lissy93/143d2ee01ccc5c052a17) © [Alicia Sykes](https://aliciasykes.com) 2022.*
> <sup>For information, see [TLDR Legal > MIT](https://tldrlegal.com/license/mit-license)</sup>

Expand License

```
The MIT License (MIT)
Copyright (c) Alicia Sykes <alicia@omg.com&gt
Permission is hereby granted, free of charge, to
```

…

[View on GitHub](https://github.com/Lissy93/repo-badge-maker)

[![View repo-badge-maker on GitHub](https://res.cloudinary.com/practicaldev/image/fetch/s--VPee_IQV--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/github/stars/Lissy93/repo-badge-maker%3Fcolor%3D232323%26label%3Drepo-badge-maker%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/Lissy93/repo-badge-maker) [![Author Lissy93](https://res.cloudinary.com/practicaldev/image/fetch/s--br1jY6vC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://img.shields.io/badge/Lissy93-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/Lissy93)


#### <a id="find-more"></a>[](#find-more)Find More

If you were enjoying this, I recommend also checking out:

- **[terminals-are-sexy](https://github.com/k4m4/terminals-are-sexy)** by Nikolaos Kamarinakis
- **[awesome-shell](https://github.com/alebcay/awesome-shell)** by Caleb Xu
- **[awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps)** by Adam Garrett-Harris

If you're new to the command line, then **[The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)** by Joshua Levy is an excellent resource, as is the **[Bash Guide](https://github.com/Idnan/bash-guide)** by Adnan Ahmed.

[source from Alicia Sykes](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#)

[⬆ back to top](#table-of-contents)