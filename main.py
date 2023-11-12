from pico2d import open_canvas, close_canvas, delay, hide_cursor
import game_framework
# import title_mode as start_mode
# import play_mode as start_mode
# import archery_mode as start_mode
import climbing_mode as start_mode
# import pingpong_mode as start_mode

open_canvas(1000,600)
hide_cursor()

game_framework.run(start_mode)
close_canvas()
