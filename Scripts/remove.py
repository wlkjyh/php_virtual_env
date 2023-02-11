import os
import const
import helper
import console

def runit(name):
    name = helper.get_realname(name)
    env_path = const.ROOT_PATH + '\\envs\\' + name
    if not os.path.exists(env_path):
        console.console.print('%ERROR 虚拟环境不存在', style='bold red')
        exit()

    print('## baseyun PHP虚拟环境 ##\n')
    print('   虚拟环境路径: ' + env_path + '\n\n')

    if input('确定删除吗？(y/n): ') == 'y':
        os.system('rd /s /q ' + env_path)
        console.console.print('%SUCCESS 删除成功', style='bold green')
    else:
        console.console.print('%ERROR 操作取消', style='bold red')