screen player_inventory_screen:
    modal True
    zorder 2
    default items = player_inventory.get_items(filter_empty=True)
    default num_fill = GridHelper.get_num_fill(total=len(items))
    default num_row = GridHelper.get_num_row(total=len(items))

    frame:
        yalign 0.04
        background "gui/store/title.png"
        xysize (550, 78)

        imagebutton:
            ycenter 0.4
            idle "gui/store/return.png"
            hover im.MatrixColor("gui/store/return.png", im.matrix.brightness(0.1))
            focus_mask True
            action [Play("sound", "audio/se/click.wav"),
                Hide("player_inventory_screen"), Jump('main')]

        text "物品":
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
        xalign 0.5
        yoffset 150

        has viewport id "inventory":
            area (100, 50, 640, 380) #(xpos, ypos, width, height)
            draggable True
            mousewheel True
            child_size 1600, 2200

            grid GridHelper.NUM_COLUMN num_row:
                spacing 20

                for item in items:
                    frame:
                        background Frame("gui/store/item_base.png")
                        xysize (150, 150)

                        if player_inventory.get_num_item(item) != float('inf'):
                            text "数量：" + str(player_inventory.get_num_item(item)):
                                xalign 0.2
                                yoffset 10
                                size 12
                                color "#000"
                                outlines [ (absolute(4), "#fff", absolute(0), absolute(0)) ]

                        button:
                            background Frame("gui/store/icon_base.png")
                            hover_background Frame(im.MatrixColor("gui/store/icon_base.png", im.matrix.brightness(0.1)))
                            xysize (85, 85)
                            xalign 0.5
                            yalign 0.6
                            hovered Play("sound", "audio/se/item.mp3")


                            add item.get_icon():
                                xalign 0.5
                                yalign 0.5
                                zoom 0.1

                            action [Show("use_item_screen", item=item)]

                for i in range(num_fill):
                    frame:
                        background Frame("gui/store/item_base.png")
                        xysize (150, 150)

    vbar value YScrollValue("inventory"):
        xpos 1022
        ypos 151
        unscrollable "hide"
        xmaximum 40
        ymaximum 430
        base_bar "gui/store/bar.png"
        thumb Frame("gui/store/candy.png", xysize=(50,50))
        thumb_offset 20

    frame:
        yoffset 200
        background None
        xysize (300, 600)
        style_prefix "use_item"
        vbox:
            text "fitness: [player.fitness]"
            text "intelligence: [player.intelligence]"
            text "charisma: [player.charisma]"

screen use_item_screen(item):
    zorder 3

    style_prefix "use_item"

    frame:
        background Frame("gui/store/store_info_base.png")
        xysize (400, 400)
        xalign 0.5
        yalign 0.5

        text "是否要使用":
            xalign 0.5
            yoffset -10
            size 50
            at transform:
                linear 1.0 xzoom 0.95
                linear 1.0 xzoom 1.0
                repeat

        add item.get_icon():
            zoom 0.5

        hbox:
            yalign 0.75
            xalign 0.5
            text item.description:
                size 30

        hbox:
            spacing 100
            ypos 0.8
            xalign 0.5
            textbutton "是":
                text_style "use_item_text"
                hovered Play("sound", "audio/se/item.mp3")
                action [Hide('use_item_screen'), Call("use_item", item=item)]

            textbutton "否":
                text_style "use_item_text"
                hovered Play("sound", "audio/se/item.mp3")
                action Hide('use_item_screen')

style use_item_text:
    color "#fff"
    hover_color "#F37459"
    size 30
    outlines [ (absolute(4), "#000", absolute(2), absolute(0)) ]

label use_item(item):
    python:
        item.use(player)
        player_inventory.remove(item)

    call screen information(msg=item.description)
    return
