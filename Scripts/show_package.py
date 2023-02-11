import os
import const
import json
import helper
def runit():
    package_list = os.listdir(const.ROOT_PATH + '/package')
    print('# baseyun PHP版本列表:')
    print('#')
    for package in package_list:
        realpath = const.ROOT_PATH + '\\package\\' + package
        print('# ' + package + '\t\t[' + realpath + ']' )
    exit()

def show_env():
    env_list = os.listdir(const.ROOT_PATH + '/envs')
    print('# baseyun 虚拟环境列表:')
    print('#')
    for env in env_list:
        try:
            realpath = const.ROOT_PATH + '\\envs\\' + env
            print('# ' + env + '\t\t[' + realpath + ']' )
            # # 读元数据
            # with open(realpath + '\\extensions.json', 'r', encoding='utf-8') as f:
            #     info = json.loads(f.read())
            #     print('  - PHP版本: ' + info['version'])
            #     print('  - 附加包: ' + ', '.join(info['extensions']))
        except:
            continue

    exit()

def show_var(name,out):
    try:
        env_path = const.ROOT_PATH + '\\envs\\' + helper.get_realname(name)
        if not os.path.exists(env_path):
            with open(out, 'w', encoding='utf-8') as f:
                f.write('1')
                exit()

        # 读元数据
        with open(env_path + '\\extensions.json', 'r', encoding='utf-8') as f:
            info = json.loads(f.read())
            register_env = info['register_env']
            print(register_env)
            # 去重
            register_env = list(set(register_env))
            if len(register_env) == 0:
                jo = ''
            else:
                jo = ';'.join(register_env)


            data = env_path + ';' + jo + ';' + os.getenv('PATH')
            with open(out, 'w', encoding='utf-8') as f:
                f.write(data)




    except Exception as e:
        with open(out, 'w', encoding='utf-8') as f:
            f.write('1')