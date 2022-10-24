## 定义画廊里按钮的高度和宽度。
define gui.gallery_slot_height = 100
define gui.gallery_slot_width = 200
define gui.gallery_slot_cols = 3
define gui.gallery_slot_rows = 2

init python:
    if persistent.unlock_1 == None:
        persistent.unlock_1 = False

    if persistent.unlock_2 == None:
        persistent.unlock_2 = False

    if persistent.unlock_3 == None:
        persistent.unlock_3 = False

    if persistent.unlock_4 == None:
        persistent.unlock_4 = False

# 游戏在此开始。

label start:
    scene beach3
    "测试"
    scene bigbeach1
    "测试"
    show beach1 mary
    "测试"
    menu:
        "结局1":
            jump b_1

        "结局2":
            jump b_2

        "结局3":
            jump b_3

        "结局4":
            jump b_4
    return

label b_1:
    $ persistent.unlock_1 = True
    scene transfer
    "测试"
    scene moonpic
    "测试"
    scene girlpic
    "测试"
    "解锁结局1"
    return

label b_2:
    $ persistent.unlock_2 = True
    scene p1
    "unlock_2"
    return

label b_3:
    $ persistent.unlock_3 = True
    scene p2
    "unlock_3"
    return

label b_4:
    $ persistent.unlock_4 = True
    scene p3
    "unlock_4"
    return
