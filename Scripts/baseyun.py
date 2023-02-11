import const
import argparse

parser = argparse.ArgumentParser(description='baseyun PHP虚拟环境')

parser.add_argument('operation', help='操作名', choices=['create', 'remove','activate','show'])
parser.add_argument('-n', '--name', help='虚拟环境名称', required=False)
parser.add_argument('-v', '--version', help='PHP版本', required=False)
parser.add_argument('-o', '--output', help='输出路径', required=False)

# 关联show命令的参数
parser.add_argument('-d','--do', help='操作参数', required=False, choices=['php','env','var'])


args = parser.parse_args()

# 查看所有可用的PHP版本
if args.operation == 'show' and args.do == 'php':
    import show_package
    show_package.runit()

# 查看所有虚拟环境
if args.operation == 'show' and args.do == 'env':
    import show_package
    show_package.show_env()

# 创建虚拟环境
if args.operation == 'create' and args.name and args.version:
    import create
    create.runit(args.name, args.version)

# 删除虚拟环境
if args.operation == 'remove' and args.name:
    import remove
    remove.runit(args.name)

# 获取虚拟环境的环境变量
if args.operation == 'show' and args.do == 'var' and args.name and args.output:
    import show_package
    show_package.show_var(args.name, args.output)

