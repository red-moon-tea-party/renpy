# 使用规则
# 教程中的代码可以用于非商用/商用的游戏，不需要和本人联系，但是需要在发布的时候署名。
# 署名信息：
#
# Black Pineapple
# blue.pepper.2019@gmail.com
#
# 禁止事项
# 非代码素材，比如美术，声音等，未经过本人许可，都禁止使用。
# 代码禁止用于非游戏的商用场合，比如在付费的教程中使用本代码，再比如加工后单纯出售代码。
#
# 视频效果 https://www.bilibili.com/video/BV1Z5411R7c7
# 程序：本人
# 背景图：自购
# UI：风华
# 立绘：自购，二改
# 物品icon：Stock Material

default player = Player(name="pineapple")
default toy_store = Shop()
default player_inventory = Inventory()

# 游戏在此开始。

label start:
    scene bg store
    call refresh_store
    jump main
    return

label main:
    menu:
        "商店界面":
            jump store
        "商店刷新":
            call refresh_store
            "商店刷新成功！"
            jump main
        "物品界面":
            jump player_inventory

    return

label refresh_store:
    python:
        renpy.random.shuffle(TOY_STORE_ITEMS)
        toy_store.refresh(TOY_STORE_ITEMS[:6])

    return

label store:
    scene bg store
    show screen store
    pause
    jump store
    return

label player_inventory:
    show screen player_inventory_screen
    pause
    jump player_inventory
    return
