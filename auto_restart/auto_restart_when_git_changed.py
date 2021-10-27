import subprocess
import time
import os
import threading
import argparse

"""
使代码在git分支发生变化后自动重启  
"""

parser = argparse.ArgumentParser('helper命令行传入参数 解析器', )
parser.add_argument('-s', '--start_shell_str', type=str, )
parser.add_argument('-n', '--script_name', type=str, )
command_args = parser.parse_args()  # type:argparse.Namespace

start_shell_str = command_args.start_shell_str
script_name = command_args.script_name


def restart(args=None):
    kill_str = f'''ps -aux|grep {script_name} |grep -v grep|awk '{{print $2}}' |xargs kill -9;'''
    subprocess.getstatusoutput('git pull')
    os.system(kill_str)
    threading.Thread(target=os.system, args=(start_shell_str,)).start()
    while True:
        time.sleep(20)
        try:
            r1 = subprocess.getstatusoutput('git pull')
            print(r1[1])
            if 'Already up-to-date' in r1[1] or '已经是最新的' in r1[1]:
                print('no update')
                continue
        except Exception as e:  # 只要不在205的dev分支手动修改文件，一般不会出现拉取报错。
            subprocess.getstatusoutput(kill_str)
            print(e)
            break
        # subprocess.getstatusoutput(cmd_str)
        print('git内容更新了，执行语句：', kill_str, start_shell_str)
        os.system(kill_str)
        threading.Thread(target=os.system, args=(start_shell_str,)).start()


if __name__ == '__main__':
    restart()
