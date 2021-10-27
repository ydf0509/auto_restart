import subprocess
import time
import os
import threading
import argparse

"""
使代码在git分支发生变化后自动重启  
"""

parser = argparse.ArgumentParser('helper命令行传入参数 解析器', )
parser.add_argument('-d', '--project_root_dir', type=str, )  # 你的项目的根目录
parser.add_argument('-s', '--start_shell_str', type=str, )
# parser.add_argument('-n', '--script_name', type=str, )
command_args = parser.parse_args()  # type:argparse.Namespace

start_shell_str = command_args.start_shell_str
# script_name = command_args.script_name
project_root_dir = command_args.project_root_dir


def restart(args=None):
    os.system(f'cd {project_root_dir};git pull')
    # kill_str = f'''ps -aux|grep {script_name} |grep -v grep|grep -v auto_restart_when_git_changed |grep -v  auto_restart_tool|awk '{{print $2}}' |xargs kill -9;'''
    kill_str = f'''ps auxww | grep '{start_shell_str}' | grep -v grep|grep -v auto_restart_when_git_changed |grep -v  auto_restart_tool | awk '{{print $2}}' | xargs kill;'''
    os.system(kill_str)
    start_shell_str_full = f''' cd {project_root_dir};export PYTHONPATH=./:$PYTHONPATH;{start_shell_str}'''
    threading.Thread(target=os.system, args=(start_shell_str_full,)).start()
    while True:
        time.sleep(20)
        try:
            r1 = subprocess.getstatusoutput(f'cd {project_root_dir};git pull')
            print(r1[1])
            if 'Already up-to-date' in r1[1] or '已经是最新的' in r1[1]:
                print('no update')
                continue
        except Exception as e:  # 只要不在205的dev分支手动修改文件，一般不会出现拉取报错。
            subprocess.getstatusoutput(kill_str)
            print(e)
            break
        # subprocess.getstatusoutput(cmd_str)
        print('git内容更新了，执行语句：', kill_str, start_shell_str_full)
        os.system(kill_str)
        threading.Thread(target=os.system, args=(start_shell_str_full,)).start()


if __name__ == '__main__':
    restart()
