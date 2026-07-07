# Habilitar zplug 
source ~/.zplug/init.zsh

# Prompt

export STARSHIP_CONFIG=~/.config/starship.toml
eval "$(starship init zsh)"

setopt histignorealldups sharehistory

# Use emacs keybindings even if our EDITOR is set to vi
bindkey -e

# History
HISTSIZE=5000
SAVEHIST=5000
HISTFILE=~/.zsh_history

# Use modern completion system
autoload -Uz compinit
compinit

zstyle ':completion:*' auto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete _correct _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' menu select=2
eval "$(dircolors -b)"
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true

zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'

# Zplug plugins

zplug "zsh-users/zsh-autosuggestions"
zplug "zsh-users/zsh-history-substring-search"
zplug "zsh-users/zsh-syntax-highlighting"

# Instalar y cargar los plugins
zplug load

# aliases

alias ls='eza -l --icons --color=always --group-directories-first'
alias la='eza -l --all --icons --color=always --group-directories-first'
alias CrealityPrint='CrealityPrint.AppImage'

# Keybindings

# Up/Down -> history search by substring (^[[A/^[[B are up/down arrow escape codes)
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down

bindkey '^p' history-search-backward
bindkey '^n' history-search-forward

# Personal binaries/scripts
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"

