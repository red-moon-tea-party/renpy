init -99 python:
    class GalleryHandler:
        SLOT_PER_PAGE = 6
        def __init__(self, buttons):
            ## 画廊处于第几页
            self.index = 0
            self.buttons = buttons

        ## 初始化画廊设置
        def init_gallery(self, gallery):
            for b in buttons:
                gallery.button(b.name)
                if b.condition:
                    gallery.condition(b.condition)

                if b.transform:
                    gallery.transform(b.transform)

                for cg in b.images:
                    gallery.unlock_image(cg)

        ## 拿到当前页面的画廊按钮
        def get(self):
            start = self.index * GalleryHandler.SLOT_PER_PAGE
            end = start + GalleryHandler.SLOT_PER_PAGE
            return self.buttons[start:end]

        def get_total_pages(self):
            return (len(self.buttons) + GalleryHandler.SLOT_PER_PAGE - 1) // GalleryHandler.SLOT_PER_PAGE

    class GalleryButtonEntry:
        SLOT_HEIGHT=150
        SLOT_WIDTH=300
        def __init__(self, name, images, condition=None,
            transform=None, thumbnail=None):

            ## 按钮的名字
            self.name = name
            ## 可能有一张或者多张cg
            self.images = images
            ## 解锁条件，可以没有
            self.condition = condition
            ## 多张图的转场效果，可以没有
            self.transform = transform

            ## 按钮的缩略图，可以没有，会缺省用第一张图的缩略图
            if thumbnail:
                self.thumbnail = thumbnail
            else:
                self.thumbnail = im.Scale("images/{:s}.jpg".format(self.images[0]),
                    GalleryButtonEntry.SLOT_WIDTH,
                    GalleryButtonEntry.SLOT_HEIGHT)
