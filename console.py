import tcod as tcod


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

font_path = 'dejavu16x16_gs_tc.png'
font_flag = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
tcod.console_set_custom_font(font_path, font_flag)

window_title = 'LASM'
fullscreen = False
root_console = tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)
tcod.sys_set_fps(LIMIT_FPS)

while not tcod.console_is_window_closed():
    tcod.console_set_default_foreground(0, tcod.white)
    # tcod.console_put_char(0, 1, 1, '@', tcod.BKGND_NONE)
    root_console.print_(10, 5, "Player")

    tcod.console_flush()


