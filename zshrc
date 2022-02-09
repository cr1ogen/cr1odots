# Created by newuser for 5.8

# Import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
# Not supported in the "fish" shell.
(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
cat ~/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
source ~/.cache/wal/colors-tty.sh

# You can create a function for this in your shellrc (.bashrc, .zshrc).
wal-tile() {
    wal -n -i "$@"
    feh --bg-tile "$(< "${HOME}/.cache/wal/wal")"
}

# Antigen Source
source /usr/share/zsh-antigen/antigen.zsh

# Load the oh-my-zsh's library.
antigen use oh-my-zsh

# Bundles from the default repo (robbyrussell's oh-my-zsh).
antigen bundle git
antigen bundle heroku
antigen bundle pip
antigen bundle lein
antigen bundle command-not-found

# Syntax highlighting bundle.
antigen bundle zsh-users/zsh-syntax-highlighting

# Load the theme.
antigen theme candy

# Tell Antigen that you're done.
antigen apply

export SPICETIFY_INSTALL="/home/cr1ogen/.spicetify"
export PATH="$SPICETIFY_INSTALL:$PATH"

# Aliases

alias ls='exa -l --icons --color=always --group-directories-first'
alias la='exa -l --all --icons --color=always --group-directories-first'
alias firefox='MOZ_ENABLE_WAYLAND=1 firefox'
### RANDOM COLOR SCRIPT ###
#colorscript random
