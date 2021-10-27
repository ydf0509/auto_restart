# 安装 pip install auto_restart



当检测到git内容发生变化后，自动重启部署，是冷部不是热部署。

建议在开发环境开发好后，代码推到测试分支。

建议安装screen, apt-get install screen，(也可以不安装这个screen，使用nohup启动脚本了那就需要)

在screen会话里面 运行以下命令:


auto_restart_tool -d /home/ydf/pycodes/auto_restart  -s  "python3  tests/test_git_change.py" -k tests/test_git_change.py

auto_restart_tool命令是自动生成的，可以直接使用这条命令。

之后，只要当前分支的git内容有更新就会自动重启。



命令行传参说明
```python
parser.add_argument('-d', '--project_root_dir', type=str, required=True)  # 你的项目的根目录
parser.add_argument('-s', '--start_shell_str', type=str, required=True)   # 启动命令，
parser.add_argument('-k', '--kill_contain_str', type=str, required=True)   # 杀死老进程，当字符串包含这个时候就当做老进程杀死。
```
