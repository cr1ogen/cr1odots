# ~/.config/zsh/prompt.zsh

# Prevent Python virtualenv from polluting the prompt
export VIRTUAL_ENV_DISABLE_PROMPT=1

FUNCNEST=100

# eval "$(starship init zsh)"
eval "$(oh-my-posh init zsh -c  /home/cr1ogen/.cache/oh-my-posh/themes/gruvbox.omp.json)"
