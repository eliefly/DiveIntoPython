import sys

class RedirectStdoutTO:
    def __init__(self, out_new):
        self.out_new = out_new # 流文件 a_file 初始化 self.out_new 

    def __enter__(self):
        self.out_old = sys.stdout # 把当前 sys.stdout 的值保存在 self.out_old 内
        sys.stdout = self.out_new # 把 self.out_new 赋给sys.stdout 重定向标准输出

    def __exit__(self, *args):
        sys.stdout = self.out_old # 退出时恢复标准输出 sys.stdout


print('A')
# with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTO(a_file):
#     print('B')
with open('out.log', mode='w', encoding='utf-8') as a_file:
    with RedirectStdoutTO(a_file):  //a_file 传参给 out_new
        print('B')

print('C')