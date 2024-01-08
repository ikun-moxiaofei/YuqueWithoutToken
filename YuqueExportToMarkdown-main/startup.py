# import sys
import argparse
from lake.lake_setup import start_convert


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-i', '--meta', help="lake文件的meta.json路径", type=str)
    # parser.add_argument('-o', '--output', help="生成markdown的根路径", type=str)
    # parser.add_argument('-d', '--downloadImage', help="是否下载图片", type=bool, default=True)
    # args = parser.parse_args()
    # print("输入命令：%s,%s,%s" % (args.meta, args.output, args.downloadImage))
    #
    # # 添加检查，确保 args.meta 不为 None
    # if args.meta is None:
    #     print("错误：meta路径不能为空。请提供有效的路径。")
    # else:
    #     start_convert(args.meta, args.output, args.downloadImage)
    if __name__ == '__main__':
        # 直接定义参数的值
        # TODO  json文件地址
        meta_path = r"D:\zhuomian\ac136b8617047280039362984135"
        # TODO  输出文件地址
        output_path = r"D:\zhuomian\yuque_dome"
        download_image = True

        print("输入命令：%s,%s,%s" % (meta_path, output_path, download_image))

        # 添加检查，确保 meta_path 不为 None
        if meta_path is None:
            print("错误：meta路径不能为空。请提供有效的路径。")
        else:
            start_convert(meta_path, output_path, download_image)

# python .\startup.py -i D:\zhuomian\ac136c3517047263779407752134 -o D:\zhuomian\yuque_dome