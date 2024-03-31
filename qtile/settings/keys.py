# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key, KeyChord
from libqtile.command import lazy


mod = "mod4"

keys = [
    Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "mod1"], "j", lazy.layout.flip_down()),
    ([mod, "mod1"], "k", lazy.layout.flip_up()),
    ([mod, "mod1"], "h", lazy.layout.flip_left()),
    ([mod, "mod1"], "l", lazy.layout.flip_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),

    # Change window sizes (MonadTall)
    ([mod], "n", lazy.layout.shrink(), lazy.layout.decrease_nmaster()),
    ([mod], "m", lazy.layout.grow(), lazy.layout.increase_nmaster()),

    # ([mod], "n", lazy.layout.normalize()),
    # ([mod], "m", lazy.layout.maximize()),

    # Toggle floating
    ([mod], "f", lazy.window.toggle_fullscreen()),
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),

    # Restart Qtile
    ([mod, "shift"], "r", lazy.restart()),
    ([mod, "shift"], "q", lazy.shutdown()),

    # Kill window
    ([mod, "shift"], "c", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # ------------ App Configs ------------

    # Menu
    ([mod, "shift"], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "n", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("firefox")),

    # Wallpaper Change
    ([mod], "x", lazy.spawn("/home/mrxir/scripts/wp-change.sh")),

    # QuteBrowser
    ([mod], "q", lazy.spawn("qutebrowser")),

    # BlueTooth
    ([mod, "shift"], "b", lazy.spawn("/home/mrxir/scripts/blue-tog.sh")),

    # QV2ray/Clash
    ([mod, "shift"], "v", lazy.spawn("/home/mrxir/scripts/cls-tog.sh")),

    # Code
    ([mod], "c", lazy.spawn("code")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Emacs
    ([mod, "shift"], "e", lazy.spawn("emacs")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty -e fish")),
    # Dmenu
    ([mod, "shift"], "Return", lazy.spawn("dmenu_run -p 'Run: '")),
    ([mod, "control"], "Return", lazy.spawn("kitty -e fish")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "control"], "r", lazy.spawn("redshift -x")),

    # Zotero
    ([mod], "z", lazy.spawn("zotero")),

    # YesPlayMusic
    ([mod], "y", lazy.spawn("yesplaymusic")),

    # Screenshot
    ([mod], "s", lazy.spawn("flameshot gui")),
    ([mod, "shift"], "s", lazy.spawn("/home/mrxir/scripts/sck-tog.sh")),

    # Sioyek
    ([mod, "shift"], "p", lazy.spawn("sioyek")),

    # Dmenu scripts

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10% -d amdgpu_bl1")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%- -d amdgpu_bl1")),
]]
keys.append(
    KeyChord([mod], "p", [
        Key([], "e",
            lazy.spawn("dm-confedit"),
            desc='Choose a config file to edit'
            ),
        Key([], "i",
            lazy.spawn("dm-maim"),
            desc='Take screenshots via dmenu'
            ),
        Key([], "k",
            lazy.spawn("dm-kill"),
            desc='Kill processes via dmenu'
            ),
        Key([], "l",
            lazy.spawn("dm-logout"),
            desc='A logout menu'
            ),
        Key([], "m",
            lazy.spawn("dm-man"),
            desc='Search manpages in dmenu'
            ),
        Key([], "o",
            lazy.spawn("dm-bookman"),
            desc='Search your qutebrowser bookmarks and quickmarks'
            ),
        Key([], "r",
            lazy.spawn("dm-reddit"),
            desc='Search reddit via dmenu'
            ),
        Key([], "s",
            lazy.spawn("dm-websearch"),
            desc='Search various search engines via dmenu'
            ),
        Key([], "p",
            lazy.spawn("passmenu"),
            desc='Retrieve passwords with dmenu'
            )
    ])
)
