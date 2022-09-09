# ## 这个代码是辅助找位置的，可以参考我前面发的视频。
# init python:
#     config.always_shown_screens.append("debug")
#     config.layers.append("debug_layer")
#     config.top_layers.append("debug_layer")
#
# transform debug_mode_t():
#     alpha 0.2
#
# screen debug():
#     layer "debug_layer"
#     add "gui/book/all_idle.png" at debug_mode_t
#
# ## 这个就算找完位置了，一般应该先从ps里找到正确位置，再去细微调整。
# ## 找位置的时候注意ps和renpy会有些许不同。把这个代码注释掉，就可以看效果了。
