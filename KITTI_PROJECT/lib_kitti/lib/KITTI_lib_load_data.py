'''
    *************************************************************
    *功能描述：导入KITTI图片，矫正，标注，点云数据
    *************************************************************
'''

from lib_kitti.lib.KITTI_lib_load_package import *
from lib_kitti.lib.KITTI_type             import *

@ time_logging
def LOAD_IMAGE(IMAGE_PATH):                                                              # 导入图片
    IMAGE = np.array(io.imread(IMAGE_PATH), dtype=np.int32)
    return IMAGE

@ time_logging
def LOAD_LABEL(LABEL_PATH):                                                              # 导入标注数据
    with open(LABEL_PATH, 'r') as f:
        LABEL = f.readlines()
    return LABEL

@ time_logging
def LOAD_CALIB_P2(CALIB_PATH):                                                           # 导入左边彩色相机矫正数据
    with open(CALIB_PATH, 'r') as f:
        lines = f.readlines()
        P2    = np.array(lines[2].strip().split(' ')[1:], dtype=np.float32).reshape(3, 4)
    return P2

@ time_logging
def LOAD_CALIB_R0(CALIB_PATH):                                                           # 加载0号相机的修正矩阵
    with open(CALIB_PATH, 'r') as f:
        lines = f.readlines()
        R0    = np.array(lines[4].strip().split(' ')[1:], dtype=np.float32).reshape(3, 3)
    return R0

@time_logging                                                                            # 点云位置坐标投影到相机坐标系前，需要转换到世界坐标系下，对应的矩阵为外参矩阵。
def LOAD_CALIB_V2C(CALIB_PATH):                                                          # 外参矩阵为Tr_velo_to_cam ，大小为3x4，
    with open(CALIB_PATH, 'r') as f:
        lines = f.readlines()
        V2C   = np.array(lines[5].strip().split(' ')[1:], dtype=np.float32).reshape(3, 4)
    return V2C

@ time_logging
def LOAD_POINT_CLOUD(LIDAR_PATH):                                                        # 加载点云数据
    POINT_CLOUD = np.fromfile(LIDAR_PATH, dtype=np.float32).reshape(-1, 4)
    return POINT_CLOUD