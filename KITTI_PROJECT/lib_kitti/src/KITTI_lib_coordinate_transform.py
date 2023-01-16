'''
    *************************************************************
    *功能描述：定义函数将点云数据转换为相机的具体坐标，方便映射
    *输入： 点云数据，矫正数据
    *输出： 彩色相机（2号）的深度数据和矫正之后的矩阵
    *************************************************************
'''

from lib_kitti.lib.KITTI_lib_load_data     import *
from lib_kitti.lib.KITTI_type              import *
from lib_kitti.lib.KITTI_lib_load_package  import *

@ time_logging
def SCAN_C0(load_point_cloud,load_calib_V2C,load_calib_R0):                                                     # 将点云从 velodyne 坐标转换为相机 0 坐标
    scan_hom = np.hstack((load_point_cloud[:, :3], np.ones((load_point_cloud.shape[0], 1), dtype=np.float32)))  # 矩阵大小4*4
    scan_C0 = np.dot(scan_hom, np.dot(load_calib_V2C.T, load_calib_R0.T))                                       # 矩阵大小3*3
    return scan_C0

@time_logging                                                                                                   # 将点云从camera0坐标转换为camera2坐标
def SCAN_C2_TEMP(load_point_cloud,load_calib_P2,scan_C0):
    scan_C0_hom = np.hstack((scan_C0, np.ones((load_point_cloud.shape[0], 1), dtype=np.float32)))               # 矩阵大小4*4
    scan_C2 = np.dot(scan_C0_hom, load_calib_P2.T)                                                              # 矩阵大小3*3
    return scan_C2

@ time_logging
def SCAN_C2_DEPTH(scan_C2_temp):                                                                                # 2号相机的深度
    scan_C2_depth = scan_C2_temp[:, 2]
    return scan_C2_depth

@ time_logging
def SCAN_C2(scan_C2_temp):                                                                                      # 转换为2号相机的矩阵坐标
    scan_C2 = (scan_C2_temp[:, :2].T / scan_C2_temp[:, 2]).T
    return scan_C2

