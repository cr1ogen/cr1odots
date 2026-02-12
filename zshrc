
# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration

# Import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
# Not supported in the "fish" shell.
(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
cat ~/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
source ~/.cache/wal/colors-tty.sh


# Aliases

alias ls='eza -l --icons --color=always --group-directories-first'
alias la='eza -l --all --icons --color=always --group-directories-first'
alias CrealityPrint='CrealityPrint.AppImage'
alias richfetch='python3 /usr/local/bin/richfetch'
alias aptgrade='sudo apt update && sudo apt upgrade'

# Executables Paths

export PATH="/home/cr1ogen/.local/bin:$PATH"

eval "$(starship init zsh)"
