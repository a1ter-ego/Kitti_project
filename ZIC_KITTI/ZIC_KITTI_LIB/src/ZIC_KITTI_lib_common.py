'''
    *************************************************************
    *总功能描述：所用到的数学公式
    *************************************************************
'''

'''
    ********************************************************************************
    *功能描述：使用模块实现跨文件共享全局变量
    *输   入：
             用set_value存储全局变量
    *输   出：
             用get_value使用全局变量
    ********************************************************************************
'''

class ZIC_get_mem():
    _global_dict = {}
    def _init(self):                               # 初始化
        global _global_dict
        self._global_dict = {}

    def set_value(self,key, value):
        self._global_dict[key] = value             # 定义一个全局变量

    def get_value(self,key):
        return self._global_dict[key]              # 获得一个全局变量，不存在则提示读取对应变量失败

    def rm_value(self, key):                       # 删除变量内存
        return self._global_dict.pop(key)

glob_dict = ZIC_get_mem()                           #方便其他py文件调用