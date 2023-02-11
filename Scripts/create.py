import os
import const
import helper
import console
import threading
import time
import json
import time

loading = False
def loadings(name):
    global loading
    s = 1
    while True:
        if loading == False:
            break
        
        time.sleep(0.1)
        if s == 1:
            print(name + '[\\]', end='\r')
            s = 2
        elif s == 2:
            print(name + '[|]', end='\r')
            s = 3
        elif s == 3:
            print(name + '[/]', end='\r')
            s = 4
        elif s == 4:
            print(name + '[-]', end='\r')
            s = 1



def runit(name,version):
    package_path = const.ROOT_PATH + '\\package\\' + version
    if not os.path.exists(package_path):
        console.console.print('%ERROR PHP版本不存在，请使用baseyun show --do php查看可使用的版本', style='bold red')
        exit()

    name = helper.get_realname(name)

    env_path = const.ROOT_PATH + '\\envs\\' + name
    if os.path.exists(env_path):
        console.console.print('%ERROR 虚拟环境已存在', style='bold red')
        exit()

    print('## baseyun PHP虚拟环境 ##\n')
    print('   虚拟环境路径: ' + env_path)
    print('   PHP版本: ' + version)

    # 扫描附加安装的包
    print('\n附加包: ')
    Extensions = const.ROOT_PATH + '\\Extensions'
    package_list = os.listdir(Extensions)
    install_it = []
    for i in package_list:
        if i.endswith('.txt'):
            # 读取版本信息，判断是否安装
            with open(Extensions + '\\' + i, 'r', encoding='utf_8_sig') as f:
                info = f.read()
                info = json.loads(info)
                if len(info['version']) == 0 or version in info['version']:
                    # print(i)
                    install_it.append(i.replace('.txt', ''))
                    print('   - ' + i.replace('.txt', '') + ' [' + info['description'] + ']')


                




    if input('\n是否创建虚拟环境[' + name + ']? [y/N] ') != 'y':
        exit()

    global loading
    loading = True
    threading.Thread(target=loadings, args=('正在创建虚拟环境',)).start()
    os.system('xcopy /e /y /i ' + package_path + ' ' + env_path + ' > nul')
    loading = False
    time.sleep(0.2)
    print('正在创建虚拟环境[√]', end='\r')
    print('正在注入配置文件')
    # edit php.ini
    php_ini_path = env_path + '\\php.ini'
    with open(php_ini_path, 'r', encoding='utf-8') as f:
        php_ini = f.read()
        php_ini = php_ini.replace('{{$realpath}}', env_path)
    
    with open(php_ini_path, 'w', encoding='utf-8') as f:
        f.write(php_ini)

    
    print('\n\n开始安装附加包：')
    install_success = []
    env_list = []
    for i in install_it:
        # loading = True
        # threading.Thread(target=loadings, args=('正在安装' + i,)).start()
        print('   - 正在安装 [' + i + ']')
        extension_path = Extensions + '\\' + i
        if not os.path.exists(extension_path):
            console.console.print('   - 安装失败，找不到安装文件 [' + i + ']', style='bold red')
            # loading = False
            time.sleep(0.2)
            continue
        else:
            install_path = env_path + '\\baseyun\\' + i 
            os.system('xcopy /e /y /i ' + extension_path + ' ' + install_path +  ' > nul')
            # 读取元数据
            with open(extension_path + '.txt', 'r', encoding='utf_8_sig') as f:
                metadata = f.read()
                metadata = json.loads(metadata)

                try:
                    if len(metadata['replace']) > 0:
                        for j in metadata['replace']:
                            with open(install_path + '\\' + j, 'r', encoding='utf-8') as f:
                                file = f.read()
                                file = file.replace('{{$realpath}}', env_path)
                                file = file.replace('{{$phppath}}', env_path )
                            with open(install_path + '\\' + j, 'w', encoding='utf-8') as f:
                                f.write(file)

                    
                    if len(metadata['register_env']) > 0:
                        for k in metadata['register_env']:
                            # env_list.append(k)
                            print(install_path)
                            env_list.append(install_path + '\\' + k)

                except:
                    print('   - 安装失败，元数据错误 [' + i + ']', style='bold red')
                    # loading = False
                    time.sleep(0.2)
                    continue


            # loading = False
            # time.sleep(0.2)
            print('   - 安装完成 [' + i + ']')
            install_success.append(i)

    print('\n\n已安装的附加包：')
    for i in install_success:
        print('   - ' + i)

    print('\n\n正在注入信息[-]')
    with open(env_path + '\\extensions.json', 'w', encoding='utf-8') as f:
        # f.write(json.dumps(install_success))
        metadata = {
            'version': version,
            'extensions': install_success,
            'register_env': env_list,
            'date': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        f.write(json.dumps(metadata))


    print('正在注入信息[√]')

    print('\n\ndone!')
    print('\n\n\t请使用baseyun activate ' + name + ' 激活虚拟环境')