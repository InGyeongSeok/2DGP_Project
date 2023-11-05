from pico2d import open_canvas, close_canvas, delay
import game_framework
# import title_mode as start_mode
# import play_mode as start_mode
# import climing_mode as start_mode
import pingpong_mode as start_mode

open_canvas(1000,600)
game_framework.run(start_mode)
close_canvas()
