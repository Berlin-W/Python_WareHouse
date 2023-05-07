"""
程序异常处理
学习目标：知道程序进行异常处理的完整格式
except 和 else 下的代码只能操作一个
"""

"""
try:
    可能发生异常的代码
except:
    处理异常的代码
else:
    没有发生异常，except不满足执行else
finally:
    不管有没有异常，最终都要执行
"""

# print('************************* 示例1 *************************')
# try:
#     print('====================')
#     f = open('xxx.txt','w',encoding='utf8')
#     print('====================')
# except:
#     print('try里面的代码出现异常')
# else:
#     print('try里面的代码没有出现异常')
# finally:
#     print('不管try里的代码有没有异常,最终finally下面的代码一定会执行')




"""
异常捕获的应用：打开文件示例
"""

print('************************* 示例2 *************************')
try:
    f = open('xxx.txt','w')
    res = f.read()
    print(res)
except:
    print('文件操作失败')
else:
    print('文件操作成功')
finally:
    print('不管文件操作成功还是失败,打开的文件都要关闭!')
    f.close()


