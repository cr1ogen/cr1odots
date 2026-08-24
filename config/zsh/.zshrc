
# Set up the prompt
eval "$(starship init zsh)"

export STARSHIP_CONFIG=~/.config/zsh/starship/starship.toml


## autosuggstions
source ~/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh

setopt histignorealldups sharehistory

# Use emacs keybindings even if our EDITOR is set to vi
bindkey -e

# Keep 1000 lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=5000
SAVEHIST=5000
HISTFILE=~/.zsh_history



# aliases

alias ls='eza -l --icons --color=always --group-directories-first'
alias la='eza -l --all --icons --color=always --group-directories-first'
alias CrealityPrint='CrealityPrint.AppImage'

# Personal binaries/scripts
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"
