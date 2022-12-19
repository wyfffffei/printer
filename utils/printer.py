from PIL import ImageWin
import win32print
import win32ui


def printer(bmp):
    """
    @param@ bmp: Image Object
    """
    printer_name = win32print.GetDefaultPrinter()
    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)
    # 打开图片并缩放
    bmp = bmp.rotate(90)
    # printable_area = (300, 270)  # 打印纸尺寸
    # printer_size = (300, 270)
    # if bmp.size[0] >= bmp.size[1]:
    #     bmp = bmp.rotate(90)
    # ratios = [1.0 * printable_area[0] / bmp.size[1], 1.0 * printable_area[1] / bmp.size[0]]
    # scale = min(ratios)
    scale = 1.4

    hDC.StartDoc("output")
    hDC.StartPage()
    dib = ImageWin.Dib(bmp)
    scaled_width, scaled_height = [int(scale * i) for i in bmp.size]
    x1 = 0  # 控制位置
    y1 = 0
    y2 = x1 + scaled_width
    x2 = y1 + scaled_height
    dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))
    # dib.expose(hDC.GetHandleOutput())  # 原图输出
    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()
