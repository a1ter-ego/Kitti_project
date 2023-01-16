'''
    *************************************************************
                            导入Python Package
    *************************************************************
'''
from lib_kitti.lib.KITTI_lib_load_package            import *

'''
    *************************************************************
                                宏开关及状态判断
    *************************************************************
'''
def time_logging(func):                                             #用时间修饰器来判断函数是否能正确运行
    def wrapper(*args,**kwargs):
        s_time = time.time()
        result = func(*args,**kwargs)
        e_time = time.time()
        print("The function {} costs time is {}".format(func,e_time-s_time) + "   函数正常运行！")
        return result
    return wrapper

'''
    *************************************************************
                                定义结构体
    *************************************************************
'''

@ time_logging
def IMAGE_PATH(FILE_ID):
    IMAGE_PATH = r'..\..\KITTI_3d_example\data_object_image_2\data_object_image_2\training\image_2\{}.png'.format(str(FILE_ID))
    return IMAGE_PATH

@ time_logging
def LABEL_PATH(FILE_ID):
    LABEL_PATH = r'..\..\KITTI_3d_example\data_object_label_2\training\label_2\{}.txt'.format(str(FILE_ID))
    return LABEL_PATH

@ time_logging
def CALIB_PATH(FILE_ID):
    CALIB_PATH = r'..\..\KITTI_3d_example\data_object_calib\training\calib\{}.txt'.format(str(FILE_ID))
    return CALIB_PATH

@ time_logging
def LIDAR_PATH(FILE_ID):
    LIDAR_PATH = r'..\..\KITTI_3d_example\data_object_velodyne\data_object_velodyne\training\velodyne\{}.bin'.format(str(FILE_ID))
    return LIDAR_PATH

fig_2D         = plt.figure(figsize=(12, 6))                           # 二维图片刻度比例
fig_3D         = mlab.figure(bgcolor=(0, 0, 0), size=(1280, 720))      # 三维像素大小
colors         = sns.color_palette('Paired', 9 * 2)                    # 色彩种类