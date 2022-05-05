screen store:
    modal True
    zorder 2
    default items = toy_store.get_stock()
    default item_description = ""

    frame:
        yalign 0.04
        background "gui/store/title.png"
        xysize (550, 78)

        imagebutton:
            ycenter 0.4
            idle "gui/store/return.png"
            hover im.MatrixColor("gui/store/return.png", im.matrix.brightness(0.1))
            focus_mask True
            action [Play("sound", "audio/se/click.wav"), Hide("store"), Jump('main')]

        text "商店":
            xcenter 0.5
            ycenter 0.4
            size 50
            color "f2cfcf"
            outlines [ (absolute(5), "#fbfbfb", absolute(0), absolute(0)) ]

    vbox:
        xalign 0.9
        yalign 0.05

        add "gui/store/money.png"
        text str(player.money):
            xalign 0.5
            yoffset -70
            size 30
            color "f2cfcf"
            outlines [ (absolute(5), "#fbfbfb", absolute(0), absolute(0)) ]

    frame:
        background "gui/store/store_base.png"
        xalign 0.3
        yalign 0.3

        has grid 3 2:
            xcenter 0.6
            ycenter 0.65
            spacing 50


        for item in items:

            frame:
                background Frame("gui/store/item_base.png")
                xysize (150, 150)

                button:
                    xysize (30, 30)
                    xoffset 120
                    yoffset -10
                    background Frame("gui/store/question.png")
                    hover_background Frame(im.MatrixColor("gui/store/question.png", im.matrix.brightness(0.2)))

                    text "?":
                        xoffset 5
                        yoffset -10
                        size 20
                        color "f2cfcf"
                        outlines [ (absolute(5), "#fbfbfb", absolute(0), absolute(0)) ]
                    action SetScreenVariable("item_description", item.description)

                if toy_store.get_number(item) != float('inf'):
                    text "剩余：" + str(toy_store.get_number(item)):
                        xalign 0.2
                        yoffset 10
                        size 12
                        color "#000"
                        outlines [ (absolute(4), "#fff", absolute(0), absolute(0)) ]

                frame:
                    background Frame("gui/store/icon_base.png")
                    xysize (85, 85)
                    xalign 0.5
                    yalign 0.6

                    add item.get_icon():
                        xalign 0.5
                        yalign 0.5
                        zoom 0.1

                    if toy_store.is_sold_out(item):
                        text "SOLD OUT":
                            xalign 0.5
                            yoffset -10
                            size 30
                            outlines [ (absolute(3), "#000", absolute(2), absolute(1)) ]

                    else:
                        add Null()

                    text "价格：" + str(item.price):
                        size 12
                        xalign 0.5
                        yoffset 75
                        color "#000"
                        outlines [ (absolute(4), "#fff", absolute(0), absolute(0)) ]

                hbox:
                    imagebutton:
                        yoffset 140
                        idle "gui/store/buy.png"
                        hover im.MatrixColor("gui/store/buy.png", im.matrix.brightness(0.1))
                        insensitive im.Grayscale("gui/store/buy.png")
                        focus_mask True
                        sensitive not toy_store.is_sold_out(item)
                        action Call('checkout', item=item)


    add "images/character/No5.png":
        zoom 0.3
        xalign 0.9
        yalign -0.2

    frame:
        background Frame("gui/store/textbox.png")
        xysize(380, 200)
        xalign 0.95
        yalign 0.9

        text item_description:
            xalign 0.5
            yalign 0.5
            xysize (300, 160)
            outlines [ (absolute(4), "#000", absolute(2), absolute(0)) ]

screen get_item(item):
    zorder 3
    button:
        xysize (1280, 720)
        action Return()

    key "input_enter" action Return()

    frame:
        background Frame("gui/store/store_info_base.png")
        xysize (400, 400)
        xalign 0.5
        yalign 0.5

        text "购买成功":
            xalign 0.5
            yoffset -10
            size 50
            outlines [ (absolute(4), "#000", absolute(2), absolute(0)) ]
            at transform:
                linear 1.0 xzoom 0.95
                linear 1.0 xzoom 1.0
                repeat

        add item.get_icon():
            zoom 0.5

label checkout(item):
    if player.money < item.price:
        call screen information(msg="你没有足够的钱。")
        return

    python:
        player.money -= item.price
        toy_store.sell(item)
        player_inventory.add(item)
    call screen get_item(item=item)

    return
