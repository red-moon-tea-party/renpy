init python:

    buttons = [
        ## 只有一张图的cg
        GalleryButtonEntry(name="dawn", images=["dawn1"]),

        ## 多张cg，有转场效果
        GalleryButtonEntry(name="dark", images=["bigbeach1",
            "beach1 mary", "beach2", "beach3"], transform=slideawayleft),

        ## 需要unlock_1是true才会解锁
        GalleryButtonEntry(name="end1",
        images=["transfer", "moonpic", "girlpic"],
        condition="persistent.unlock_1"),

        ## 需要unlock_2是true才会解锁
        GalleryButtonEntry(name="end2",
        images=["transfer1", "moonpic", "girlpic"],
        condition="persistent.unlock_2"),

        ## 需要unlock_3是true才会解锁
        GalleryButtonEntry(name="end3",
        images=["transfer", "moonpic", "girlpic"],
        condition="persistent.unlock_3"),

        ## 需要unlock_4是true才会解锁
        GalleryButtonEntry(name="end4",
        images=["transfer", "moonpic", "girlpic"],
        condition="persistent.unlock_4"),

        ## 单一图的cg
        GalleryButtonEntry(name="p1",
        images=["p1"]),

        GalleryButtonEntry(name="p2",
        images=["p2"]),

        GalleryButtonEntry(name="p3",
        images=["p3"]),

        GalleryButtonEntry(name="p4",
        images=["p3"]),

        GalleryButtonEntry(name="p5",
        images=["p3"]),

        GalleryButtonEntry(name="p6",
        images=["p3"]),

        GalleryButtonEntry(name="p7",
        images=["p3"]),

        GalleryButtonEntry(name="p8",
        images=["p3"]),
    ]

    ## 创建Gallery对象。
    g = Gallery()

    ## 设置没有解锁的图片
    g.locked_button = Composite(
        (GalleryButtonEntry.SLOT_WIDTH,
        GalleryButtonEntry.SLOT_HEIGHT),
        (0, 0), Solid("#000"),
        (50,30), Text("未解锁", size=30, color="#fff"))

    g.button("beach3")
    g.unlock_image("beach3")

    # 用于图像切换使用的转场(transition)。
    g.transition = dissolve

    gh = GalleryHandler(buttons)
    gh.init_gallery(g)

# 我们使用的画廊界面。
screen gallery:

    # 确保画廊界面替换主菜单。
    tag menu

    # 背景图。
    add "gui/gallery/bg.jpg"

    text _("画廊"):
        size 30
        color "#fff"
        align (0.1, 0.1)

    use gallery_slots(gh.get())

    ## 翻页逻辑
    hbox:
        xalign 0.5 yalign 0.8
        frame:
            textbutton _("上一页"):
                sensitive gh.index > 0
                action SetField(gh, 'index', gh.index-1)

        for i in range(gh.get_total_pages()):
            frame:
                textbutton str(i):
                    action SetField(gh, 'index', i)

        frame:
            textbutton _("下一页"):
                sensitive gh.index < gh.get_total_pages()-1
                action SetField(gh, 'index', gh.index+1)

    # 用于响应后返回主菜单的界面。
    # 也能用于导航到其他画廊界面。
    textbutton "Return" action Return() xalign 0.1 yalign 0.8


screen gallery_slots(buttons):
    # 按钮网格(grid)。
    grid gui.gallery_slot_cols gui.gallery_slot_rows:
        align (0.5, 0.5)
        xysize (1600, 1200)
        xspacing 30
        yspacing 30

        for b in buttons:
            frame:
                foreground Frame("gui/gallery/idle.png")
                xysize (GalleryButtonEntry.SLOT_WIDTH, GalleryButtonEntry.SLOT_HEIGHT)

                # 调用make_button显示具体的按钮。
                add g.make_button(name=b.name, unlocked=b.thumbnail,
                    xalign=0.5, yalign=0.5)

        ## 如果格子不满，需要补上空白
        for i in range(gh.SLOT_PER_PAGE - len(buttons)):
            null
