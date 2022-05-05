init -1 python:
    def get_hovered(name):
        return im.MatrixColor(ImageReference(name), im.matrix.brightness(0.1))


screen information(msg):
    zorder 3

    button:
        xysize (1280, 720)
        action Return()

    frame:
        background Frame("gui/store/store_info_base.png")
        xysize (400, 400)
        xalign 0.5
        yalign 0.5

        text msg:
            xalign 0.5
            yalign 0.5
            outlines [ (absolute(4), "#000", absolute(2), absolute(0)) ]
