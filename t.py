# !/usr/bin/env python3

from xpinyin import Pinyin
import os
import shutil

pin = Pinyin()


def rename(src, sp, dst, dp):
    spath = os.path.join(src, sp)  # folder
    dpath = os.path.join(dst, dp)  # folder

    if not os.path.exists(dpath):
        os.mkdir(dpath)

    arr = os.listdir(spath)
    for i in range(len(arr)):
        f = arr[i]
        try:
            sfile = os.path.join(spath, f)
            pinyin_name = pin.get_pinyin(f, "")
            if os.path.isfile(sfile):
                print(f"Process {sfile}")
                dfile = os.path.join(dpath, pinyin_name)
                shutil.copyfile(sfile, dfile)
                print(f"\t=> {dfile}")
            elif os.path.isdir(sfile):  # recursive
                rename(src, os.path.join(sp, f), dst, os.path.join(pinyin_name))
        except Exception as e:
            print(f"{f}:{e}")
            continue


if __name__ == "__main__":
    rename("./file/", "", "./dist/", "")
