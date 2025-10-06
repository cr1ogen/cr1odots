# Created by newuser for 5.9

# Linux antigen file
source /usr/share/zsh-antigen/antigen.zsh
# Load the oh-my-zsh's library.
antigen use oh-my-zsh
# Load the theme
antigen theme https://github.com/denysdovhan/spaceship-zsh-theme spaceship
# Bundles from the default repo (robbyrussell's oh-my-zsh).
antigen bundle git
antigen bundle heroku
antigen bundle pip
antigen bundle lein
antigen bundle command-not-found
antigen bundle autojump
antigen bundle common-aliases
antigen bundle compleat
antigen bundle git-extras
antigen bundle git-flow
antigen bundle npm
antigen bundle web-search
antigen bundle z
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-history-substring-search ./zsh-history-substring-search.zsh
# NVM bundle
export NVM_LAZY_LOAD=true
antigen bundle lukechilds/zsh-nvm
antigen bundle Sparragus/zsh-auto-nvm-use
# Syntax highlighting bundle.
antigen bundle zsh-users/zsh-syntax-highlighting
# Tell Antigen that you're done.
antigen apply
# Setup zsh-autosuggestions
#source "$HOME/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh"
# Load custom aliases
[[ -s "$HOME/.bash_aliases" ]] && source "$HOME/.bash_aliases"
# Load NVM
export NVM_DIR="$(realpath $HOME/.nvm)"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion


# Aliases

alias ls='eza -l --icons --color=always --group-directories-first'
alias la='eza -l --all --icons --color=always --group-directories-first'
alias ProtonUp='ProtonUp-Qt-2.9.1-x86_64.AppImage'
alias richfetch='python3 /usr/local/bin/richfetch'
alias aptgrade='sudo apt update && sudo apt upgrade'
### RANDOM COLOR SCRIPT ###
#colorscript random


export PATH="/home/cr1ogen/.local/bin:$PATH"
