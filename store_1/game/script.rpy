## 今天我们来写一个商店界面。
## 首先把之前写过的商店界面里的，0shop_items.rpy,0shop_list.rpy, InventoryClass.rpy
## ItemClass.rpy, ShopClass.rpy 复制到新建的文件夹下面。

##  定义三个商店，分别是宠物，服装和食物。
default pet_store = Shop()
default outfit_store = Shop()
default food_store = Shop()

## 正常这些变量应该是封装在一个类里面，今天为了图方便，就直接写外面了。
## 如果大家做一个大程序，请注意自己设计这个类。
## 定义三个变量，第一个是类比，用来记录现在显示的是哪个商店。
default category = "pet"

## 索引，因为我们要做翻页功能，这个变量用来记录是第几页。
default index = 0

## 选中的物品。
default selected_item = None

label start:
    ## 增加一个背景图作为底图
    scene bg store
    python:
        pet_store.refresh(PET_STORE_ITEMS)
        outfit_store.refresh(OUTFIT_STORE_ITEMS)

    jump shop
    return

label shop():
    ## 这样写就不会因为按键打断界面。可以去参考之前写过的别的界面流程。
    ## 显示shop界面
    show screen shop

    ## 暂停
    pause

    ## 跳转到商店界面
    jump shop
    return

screen shop():
    style_prefix "mall"
    ## 刚才中间那块是透明的，为了增加一个商店图片装饰。
    ## 这里用了一个遮照，显示一个图片作为装饰。
    add AlphaMask(Frame("images/bg store.jpg", xysize=(573, 236)),
        Solid("#fff")):
            pos (145, 145)

    ## 商店的底图。
    add "gui/store/bg.png"

    ## 不同的商店，正常也应该封装起来，这里我就图省事了。
    $ categories = ["pet", "outfit", "food"]

    ## 选择商店按钮
    ## hbox可以让一组可是组建横着排列。
    hbox:
        ## 位置
        pos (160, 385)
        ## 间距，负数可以缩小间距
        spacing -15
        for c in categories:
            button:
                ## 背景
                background "gui/store/idle.png"
                ## 悬浮背景
                hover_background "gui/store/hover.png"
                ## 当按钮被选中的时候的背景
                selected_background "gui/store/selected.png"
                ## 大小
                xysize (201, 31)

                ## 按钮上的字
                ## _() 是为了等一下用翻译功能
                ## 现在显示的都是英文字母，等下翻译功能可以变成汉字
                text _(c):
                    align (0.5, 0.5)

                ## 一个bool表达式，下面条件为true的时候，
                ## 表示这个按钮被选中
                selected category == c

                ## 如果选中这个按钮，商店类型设置为现在选中的类型。
                ## 商店索引，从0开始。
                ## 程序里不从1开始，都是从0开始。
                action [SetVariable('category', c),
                    SetVariable('index', 0)
                ]

    ## 这个方法可以拿到某一个store的对象。有兴趣可以去看下如何使用globals() 这个函数。
    $ current_shop = globals()[category+"_store"]

    use item_view(current_shop, current_shop.get_stock()[index*6:(index+1)*6])

    ## 下面是翻页用的箭头
    hbox:
        pos (400, 610)
        spacing 30
        button:
            background "gui/store/left_idle.png"
            hover_background "gui/store/left_hover.png"
            ## 可以把原图的黑色变成红色。
            ## 这个是按钮不能点的时候的背景
            insensitive_background im.MatrixColor(
                "gui/store/left_idle.png",
                im.matrix.colorize('#f00', '#00f')
            )
            xysize (27, 18)
            ## bool 判断：什么时候可以点这个按钮。
            ## 因为这个是向前翻页，如果现在是第0页，就不可以点。
            sensitive index != 0
            action SetVariable('index', index-1)

        button:
            background "gui/store/right_idle.png"
            hover_background "gui/store/right_hover.png"
            ## 可以把原图的黑色变成红色。
            ## 这个是按钮不能点的时候的背景
            insensitive_background im.MatrixColor(
                "gui/store/right_idle.png",
                im.matrix.colorize('#f00', '#00f')
            )
            xysize (27, 18)
            ## bool 判断：什么时候可以点这个按钮。
            ## 因为这个是向前翻页，如果现在是第0页，就不可以点。
            ## 这个是已经在最后一页，就不能往后翻页。
            sensitive index < (len(current_shop.get_stock())-1) // 6
            action SetVariable('index', index+1)

    ## 下面添加返回按钮
    button:
        background "gui/store/return_idle.png"
        hover_background "gui/store/return_hover.png"
        xysize (95, 37)
        pos (115, 633)
        ## 这里先不写了，因为并不知道要return到哪里去。
        ## 也许是jump或者是return
        ## 请根据自己情况去写
        action [None]

    ## 下面是商品信息显示
    frame:
        background Solid("#000")
        xysize (228, 329)
        pos (745, 90)

        if selected_item:
            add selected_item.img:
                xysize (200, 200)
                align (0.5, 0.5)

            vbox:
                xalign 0.5
                ypos 350
                text _(selected_item.name)
                hbox:
                    xalign 0.5
                    text _("price")
                    text _(": ")
                    ## 本来数值是一个int，需要用str函数转换为字符串
                    text str(selected_item.price)

                text _(selected_item.description)

        ## 购买按钮
        button:
            background "gui/store/buy_idle.png"
            hover_background "gui/store/buy_hover.png"
            xysize (234, 40)
            pos (745, 615)
            ## 这里也先不写了，想知道如何写的，去看前面一期专门讲商店的专栏
            action [None]

screen item_view(shop, items):
    frame:
        pos (145, 417)
        background "gui/store/item_frame.png"
        xysize (588, 188)

        ## 建立一个 2 X 3 的格子
        grid 2 3:
            ## 间距
            xspacing 20
            yspacing 10
            align (0.5, 0.5)
            for item in items:
                button:
                    xysize (262, 44)
                    background "gui/store/item_idle.png"
                    selected_background "gui/store/item_selected.png"
                    selected item == selected_item

                    text _(item.name):
                        align (0.5, 0.5)
                        size 30
                        color "#000"
                    tooltip item
                    action [SetVariable('selected_item', item)]

            ## 这里因为用了grid，grid需要填满，所以需要计算
            ## 有多少没有物品，但是我们需要放格子
            $ n = 6 - len(items)

            ## 这里就是放格子
            for i in range(n):
                add "gui/store/item_idle.png"

    ## 工具提示
    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            ## 显示商品的相关信息
            frame:
                background Solid("#0005")
                xalign 0.5
                vbox:
                    add tooltip.img:
                        xysize (100, 100)
                    text tooltip.name:
                        color "#fff"
                        size 30
                        outlines [(3, "#fff5"), (2, "#000")]


## 通用的文字样式
## 这样就不需要每个文字都设置一下。
style mall_text:
    color "#000"
    xalign 0.5
