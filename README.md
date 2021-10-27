# 安装 pip install auto_restart



当检测到git内容发生变化后，自动重启部署，是冷部不是热部署。

建议在开发环境开发好后，代码推到测试分支。

安装screen, apt-get install screen，(也可以不安装这个screen，使用nohup启动脚本了那就需要)

在screen会话里面 运行以下命令:

auto_restart -d "/home/ydf/pycodes/auto_restart"  -s  "python3  tests/test_git_change.py"  -n  test_git_change.py


