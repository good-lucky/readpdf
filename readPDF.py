import sys
import importlib
import lib.reload(sys)
from pdfminer.pdfparser import  PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def readPdf(self, path, callback=None, topath = ""):
    #以二进制方式打开pdf文件
    f = open(path, "rb")

    #创建一个pdf 文档分析器
    parser = PDFParser(f)

    #创建pdf文档
    pdfFile = PDFDocument()

    #连接分析器与文档对象
    parser.set_document(pdfFile)
    #pdf 连接解析器反向关联
    pdfFile.set_parser(parser)

    #提供初始化密码
    pdfFile.initialize("")

    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #解析数据
        manage = PDFResourceManager()
        #创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(manage, laparams = laparams)
        #解释器对象
        interpreter = PDFPageInterpreter(manage, device)
        #开始处理，没次处理一页
        for page in pdfFile.get_pages():
            interpreter.progcess_page(page)
            layout = device.get_reault()
            for x in layout:
                if(isinstance(x, LTTextBoxHorizontal)):

                    if toPath =="":
                        #处理行数据
                        str = x.get_text()
                        if callback !=None:
                            #回调函数   main 方法
                            callback(str)
                        else:
                            print("处理文件")
                    else:
                        print("写文件   toPath 写入文件的路径")
'''
                    with open(toPath, "a") as f:
                        str = x.get_text()
                        #以获取pdf 行数据处理数据
                        #print()
                        f.write(str + "\n")
'''




#文件路径
path = r""
#读到的内容写到文件内
toPath = r""

readPdf(path, toPath)

