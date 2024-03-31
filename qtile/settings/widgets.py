from libqtile import widget
from .theme import colors
from libqtile import qtile

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='grey'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=25, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=39,
        padding=-4
    )


def workspaces(): 
    return [
	separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='SauceCodePro Nerd Font',
            fontsize=27,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=25, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    #powerline('color4', 'dark'),

    #icon(bg="color4", text=' '), # Icon: nf-fa-download
    #
    #widget.CheckUpdates(
    #    distro = "Arch_checkupdates",
    #    background=colors['color4'],
    #    colour_have_updates=colors['text'],
    #    colour_no_updates=colors['text'],
    #    display_format='Updates: {updates}',
    #    update_interval=900,
    #    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e sudo pacman -Syu')},
    #),

    powerline('color4', 'grey'),

    #icon(bg="color1", text='﬙'),  # Icon: nf-mdi-chip
    
    widget.CPU(**base(bg='color4'), format='CPU {freq_current}GHz {load_percent}%'),

    powerline('color2', 'color4'),

    #icon(bg="color2", text=''),  # Icon: nf-mdi-fan
    
    widget.NvidiaSensors(**base(bg='color2'), threshold=60, foreground_alert='ff6000', format='GPU {temp}°C {perf}', 
	mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e nvtop')}
    ),

    powerline('color3', 'color2'),

    #icon(bg="color3", text=''),  # Icon: nf-mdi-memory
    
    #widget.CPU(**base(bg='color3'),
    widget.Memory(
	**base(bg='color3'),
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')},
        fmt = 'Mem{}',
        padding = 5
    ),

    powerline('color4', 'color3'),

    icon(bg="color4", text=' '),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color4'), interface='wlan0', format = '{down} ↓↑ {up}', prefix='M',  mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e ip link')}),

    powerline('color2', 'color4'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%m/%d(%A)%H:%M'),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5, icon_size=40),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'SauceCodePro Nerd Font',
    'fontsize': 25,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
