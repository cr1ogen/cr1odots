# Created by newuser for 5.9


eval "$(starship init zsh)"

# Import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
# Not supported in the "fish" shell.
(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
cat ~/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
source ~/.cache/wal/colors-tty.sh

# Linux antigen file
#source /usr/share/zsh-antigen/antigen.zsh
# Load the oh-my-zsh's library.

source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /home/cr1ogen/.zsh/zsh-history-substring-search/zsh-history-substring-search.zsh
source /home/cr1ogen/.zsh/zsh-autocomplete/zsh-autocomplete.plugin.zsh


alias ls='eza -l --icons --color=always --group-directories-first'
alias la='eza -l --all --icons --color=always --group-directories-first'
alias CrealityPrint='CrealityPrint_Ubuntu2404-V6.3.0.3420-x86_64-Release.AppImage'
alias richfetch='python3 /usr/local/bin/richfetch'
alias aptgrade='sudo apt update && sudo apt upgrade'
### RANDOM COLOR SCRIPT ###
#colorscript random


export PATH="/home/cr1ogen/.local/bin:$PATH"
