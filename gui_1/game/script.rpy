## 最后可以用style，把重复的属性写在一起，改的时候也比较容易改。
## 以及在action的地方填写正确的行为。
## 感谢观看。﻿


# 游戏在此开始。
## 加了这句之后，就不出现主菜单了。
label main_menu:
    return

## 因为如果和界面交互，需要让界面停留，就需要用pause，
## 但是如果玩家点击了界面，这个pause就会被点没，于是就需要在jump start。
## 正常作业的时候，可以另外写一个label，不要用start。
label start:
    show screen gui1
    pause
    jump start
    return


## 在这里定义一个界面，一般如果是比较大的工程。
## 可以把界面和脚本分开存在不同文件。
screen gui1():
    ## 增加了这个界面的底图。
    ## 一般底图可以用jpg，jpg会比png占更小的地方。
    add "gui/book/background.png"

    ## 联系人按钮
    button:
        ## 按钮的空闲图片
        idle_background "gui/book/contacts_idle.png"

        ## 按钮的悬停图片
        hover_background "gui/book/contacts_hover.png"

        ## 按钮的大小
        xysize (158, 98)

        ## 按钮位置
        pos (295, 140)

        ## 设置这个会让透明区域不会选中。
        focus_mask True

        ## 这样写的话，这个按钮的hover效果才会显示。
        action [None]

    ## leads按钮
    button:
        ## 按钮的空闲图片
        idle_background "gui/book/leads_idle.png"

        ## 按钮的悬停图片
        hover_background "gui/book/leads_hover.png"

        ## 按钮的大小
        xysize (165, 99)

        ## 设置这个会让透明区域不会选中。
        focus_mask True

        pos (295, 365)

        ## 这样写的话，这个按钮的hover效果才会显示。
        action [None]

    ## 地点按钮
    button:
        ## 按钮的空闲图片
        idle_background "gui/book/locations_idle.png"

        ## 按钮的悬停图片
        hover_background "gui/book/locations_hover.png"

        ## 按钮的大小
        xysize (163, 85)

        ## 设置这个会让透明区域不会选中。
        focus_mask True

        pos (298, 263)

        ## 这样写的话，这个按钮的hover效果才会显示。
        action [None]

    ## 返回按钮
    button:
        ## 按钮的空闲图片
        idle_background "gui/book/return_idle.png"

        ## 按钮的悬停图片
        hover_background "gui/book/return_hover.png"

        ## 按钮的大小
        xysize (257, 109)

        ## 设置这个会让透明区域不会选中。
        focus_mask True

        pos (230, 495)

        ## 这样写的话，这个按钮的hover效果才会显示。
        action [None]
