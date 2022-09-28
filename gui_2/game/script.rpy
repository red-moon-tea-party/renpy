label start:
    jump notebook
    return

label notebook():
    show screen notebook
    ## 必须有这个pause， 才会显示这个自定义的界面
    pause
    ## 如果玩家和界面交互，就会按掉这个pause，于是需要jump回这个label
    jump notebook
    return

screen notebook():
    ## 这个是底图
    add "images/notebook/frame.png"

    ## 因为我们这个界面有三个按钮，于是定义一个界面变量，要记录现在是那个按钮被选中了。
    ## 我们的三个按钮是，角色，位置，线索。
    ## 缺省是线索。
    default category = "clue"

    ## 角色按钮
    button:
        ## 按钮的背景图
        background "images/notebook/character_idle.png"
        ## 被选中的时候的背景
        selected_background "images/notebook/character_selected.png"
        ## 被选中的条件，如果现在category是角色，就是这个按钮被选中。

        selected category == "character"
        ## 悬浮的时候的按钮背景，这里使用了renpy的图像器，可以参考我前面有一起教程。
        ## 这个是会加亮效果。
        hover_background im.MatrixColor("images/notebook/character_idle.png",
            im.matrix.brightness(0.3))

        pos (954, 114)
        xysize (110, 83)
        ## 这个是可以改变这个界面变量category的数值。
        action SetScreenVariable('category', 'character')

    ## 位置按钮
    button:
        ## 按钮的背景图
        background "images/notebook/location_idle.png"
        ## 被选中的时候的背景
        selected_background "images/notebook/location_selected.png"
        ## 被选中的条件，如果现在category是角色，就是这个按钮被选中。

        selected category == "location"
        ## 悬浮的时候的按钮背景，这里使用了renpy的图像器，可以参考我前面有一起教程。
        ## 这个是会加亮效果。
        hover_background im.MatrixColor("images/notebook/location_idle.png",
            im.matrix.brightness(0.3))

        pos (960, 213)
        xysize (96, 78)
        ## 这个是可以改变这个界面变量category的数值。
        action SetScreenVariable('category', 'location')

    ## 线索
    button:
        ## 按钮的背景图
        background "images/notebook/clue_idle.png"
        ## 被选中的时候的背景
        selected_background "images/notebook/clue_selected.png"
        ## 被选中的条件，如果现在category是角色，就是这个按钮被选中。

        selected category == "clue"
        ## 悬浮的时候的按钮背景，这里使用了renpy的图像器，可以参考我前面有一起教程。
        ## 这个是会加亮效果。
        hover_background im.MatrixColor("images/notebook/clue_idle.png",
            im.matrix.brightness(0.3))

        pos (972, 301)
        xysize (90, 90)
        ## 这个是可以改变这个界面变量category的数值。
        action SetScreenVariable('category', 'clue')


    ## 下面来加页面上的内容
    ## 这里只做一个线索页面，剩下的大家可以仿照例子来做
    if category == "clue":
        ## 增加了一个新的图片
        frame:
            background "images/notebook/picture_frame.png"
            xysize (394, 362)
            pos (100, 50)

            add AlphaMask(Frame("images/bg undersea.jpg", xysize=(349, 240)),
                "images/notebook/mask.png"):
                    xalign 0.5
                    ypos 80

        text "字数字数字数字数字数字数字数字数字数字数字数字数字数字数字数字数字数字数字数字数":
            ## 字的大小
            size 50
            ## 字颜色
            color "#000"
            ## 可以让字在一个范围内显示
            xysize (300, 100)
            pos (600, 100)
