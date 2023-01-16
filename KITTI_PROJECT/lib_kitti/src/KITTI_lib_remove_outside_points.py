'''
    *************************************************************
    *功能描述：定义函数将点云数据中无效的点去除，用于完成最终的映射
    *输入： 点云数据，矫正数据
    *输出： 可以直接在图像上成像的点云数据
    *************************************************************
'''
from lib_kitti.src.KITTI_lib_coordinate_transform import *

@ time_logging
def OUTSIDE_POINTS_2D(scan_C2,scan_C2_depth,load_image):                                                 # 二维点云去除无用点之后的点云集合
    outside_points_2d = scan_C2[:, 0] > 0
    outside_points_2d = np.logical_and(outside_points_2d, scan_C2[:, 0] < load_image.shape[1])
    outside_points_2d = np.logical_and(outside_points_2d, scan_C2[:, 1] > 0)
    outside_points_2d = np.logical_and(outside_points_2d, scan_C2[:, 1] < load_image.shape[0])
    outside_points_2d = np.logical_and(outside_points_2d, scan_C2_depth > 0)
    return outside_points_2d

@ time_logging
def OUTSIDE_POINTS_3D(scan_C2,scan_C2_depth,load_image):                                                 # 三维点云去除无用点之后的点云集合
    ouside_points_3d = scan_C2_depth > 0
    ouside_points_3d = np.logical_and(ouside_points_3d, scan_C2[:, 0] > 0)
    ouside_points_3d = np.logical_and(ouside_points_3d, scan_C2[:, 0] < load_image.shape[1])
    ouside_points_3d = np.logical_and(ouside_points_3d, scan_C2[:, 1] > 0)
    ouside_points_3d = np.logical_and(ouside_points_3d, scan_C2[:, 1] < load_image.shape[0])
    return ouside_points_3d