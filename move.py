import os
import shutil
import time

inputsource = input('Source Path:')
inputdestination = input('Destination Path:')
root_src_dir = inputsource
root_dst_dir = inputdestination
extension_list = ('.downloading', '.jpeg', '.jpg', '.htm', '.dmg', '.tmp', '.txt', '.html')


count = 1
while count <12306:

    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                # in case of the src and dst are the same file
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
            if not file_.endswith(extension_list) :
                shutil.move(src_file, dst_dir)
                print("Moved", file_, "to", dst_dir)

    time.sleep(1)

    folders = list(os.walk(root_src_dir))
    for path, _, _ in folders[::-1]:
        if len(os.listdir(path)) == 0:
            os.rmdir(path)

    for k in range(60):
        print("Wait", 60-k , "s" , "\r" , end='')
        time.sleep(1)
