if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -x NNN_PLUG 'f:finder;o:fzopen;p:mocplay;d:diffs;t:nmount;v:preview-tabbed'

fish_vi_key_bindings

# commands required to run 
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
eval /home/mrxir/miniconda3/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<
starship init fish | source

fish_add_path -m /home/mrxir/.local/bin
fish_add_path -m /home/mrxir/.cargo/bin

alias cad="chezmoi add"
alias cvi="chezmoi edit --apply"
alias csts="chezmoi status"
alias cdf="chezmoi diff"
alias capl="chezmoi apply"
alias ccd="chezmoi cd"
alias cmg="chezmoi merge"
alias cmga="chezmoi diff | grep -- ^--- | grep -vE '/dev/null' | sed -e 's/^--- a\///' | xargs -r chezmoi merge"
alias pm="pacman"
alias syyu="sudo pacman -Syyu"
alias lg="lazygit"
alias py="python"
alias ali="aliyunpan"

alias ll="exa -l -g --icons"
alias lla "ll -a"
alias llt="ll --tree --level=2"
alias llta="ll --tree --level=2 -a"
alias bcat="bat"
alias du="dust"
alias psx="procs"
alias df="duf"
alias rp="ripgrep"
alias hp="httpie"
alias ra="ranger"
alias ya="yazi"

alias dk="sudo docker"
alias docker="sudo docker"
alias dkp="sudo docker pull"
alias dkr="sudo docker run"
alias dkb="sudo docker build"
alias dkps="sudo docker ps"
alias dkk="sudo docker kill"
alias dki="sudo docker images"

alias dkcp="sudo docker compose"
alias dkcpps="sudo docker compose ps"

alias afl="sudo docker run -p 4200:3000 -d ghcr.io/toeverything/affine:nightly-latest"
alias afs="sudo docker run -it --rm -p 3000:3000 ghcr.io/toeverything/affine:nightly-server-latest"
alias tl="tmux ls"
alias ta="tmux attach -t"
alias tn="tmux new -s"

alias spx="env | grep -I proxy"
alias npus="ssh xiezc@103.26.77.190 -p 14022"
alias rflt="sudo reflector -c China -a 12 -f 3 --save /etc/pacman.d/mirrorlist"
alias ts="sudo typespeed"
alias n="nnn"
alias nn="nnn"
alias 42="ssh xxc@10.68.219.148 -p 10142"
alias 43="ssh xxc@10.68.219.148 -p 10143"
alias 45="ssh xxc@10.68.219.148 -p 10145"
alias 38="ssh xzc@10.68.219.148 -p 10138"
alias pcr="ssh mrxir@10.31.164.163 -p 7324"
alias pcl="ssh mrxir@192.168.0.53 -p 7325"
alias ssh409="ssh xxc@10.68.219.148 -p"
alias bts="bluetoothctl scan on"
alias btd="bluetoothctl discoverable on"
alias btp="bluetoothctl pair"
alias btc="bluetoothctl connect"
alias bt="bluetoothctl connect 0C:AE:BD:80:62:BB"
alias backend="dk run -it -p 8080:8080 --gpus all -v /home/mrxir/Codes/rec2vqa:/rec2vqa mrxir/rec2vqa:backend-cuda9-cudnn7-ubuntu16.04-pytorch1.1-python3.6"
alias frontend="dk run -it -p 80:8080 -v /home/mrxir/Codes/rec2vqa:/rec2vqa mrxir/rec2vqa:frontend-node12.6-npm6.9-ubuntu20.04"

function epx
    export http_proxy=127.0.0.1:7890; export https_proxy=127.0.0.1:7890; export all_proxy=socks5://127.0.0.1:7890;
end
function dpx
    set -e http_proxy; set -e https_proxy; set -e all_proxy;
end
function wav
    for i in (seq 100)
       for j in (seq (math $COLUMNS - 1))
          math "ceil(6 * cos(($i + $j) * pi / 5))"
       end | spark | read sparks
       echo -n $sparks\r && sleep .1
    end
end
function tlt
    toilet $argv -w 120 | boxes -d cat -a hc -p h8 | lolcat
end
function cs
    echo $argv | cowsay | toilet --gay -f term
end


epx
export EDITOR='nvim'
neofetch | lolcat
