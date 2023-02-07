'''
    *************************************************************
    *功能描述：定义函数将点云数据中无效的点去除，用于完成最终的映射
    *输入： 点云数据，矫正数据
    *输出： 可以直接在图像上成像的点云数据
    *************************************************************
'''

from ZIC_KITTI_LIB.include.ZIC_KITTI_type import *
from ZIC_KITTI_LIB.src.ZIC_KITTI_lib_common import glob_dict

'''
    *************************************************************
    *功能描述：定义函数将点云数据中无效的点去除，用于完成最终的映射
    *输入： 
           y                      I  最终映射得到的图像坐标
           Z_cam                  I  得到齐次坐标的形式的除数     
           image                  I  导入的图像数据
    *输出：
           y2D(outside_points_2d) O    二维点云去除无用点之后的点云集合
    *************************************************************
'''

def ZIC_KITTI_y2D(y,Z_cam,image):                                                         # 二维点云去除无用点之后的点云集合
    outside_points_2d = 0
    try:
        outside_points_2d = y[:, 0] > 0                                                   # outside_points_2d是2D图像中有用的点
        outside_points_2d = np.logical_and(outside_points_2d, y[:, 0] < image.shape[1])
        outside_points_2d = np.logical_and(outside_points_2d, y[:, 1] > 0)
        outside_points_2d = np.logical_and(outside_points_2d, y[:, 1] < image.shape[0])
        outside_points_2d = np.logical_and(outside_points_2d, Z_cam > 0)
        glob_dict.set_value("outside_points_2d",outside_points_2d)
        return STATUS_OK
    except:
        return ERR_y2D

'''
    *************************************************************
    *功能描述：定义函数将点云数据中无效的点去除，用于完成最终的映射
    *输入： 
           y                      I/O   最终映射得到的图像坐标
           Z_cam                  I/O   得到齐次坐标的形式的除数     
           image                  I/O   导入的图像数据
    *输出： 
           y3D(ouside_points_3d)  O     三维点云去除无用点之后的点云集合
    *************************************************************
'''
def ZIC_KITTI_y3D(y,Z_cam,image):                                                         # 三维点云去除无用点之后的点云集合
    outside_points_3d = 0
    try:                                                                                  # outside_points_3d是2D图像中有用的点
        ouside_points_3d = Z_cam > 0
        ouside_points_3d = np.logical_and(ouside_points_3d, y[:, 0] > 0)
        ouside_points_3d = np.logical_and(ouside_points_3d, y[:, 0] < image.shape[1])
        ouside_points_3d = np.logical_and(ouside_points_3d, y[:, 1] > 0)
        ouside_points_3d = np.logical_and(ouside_points_3d, y[:, 1] < image.shape[0])
        glob_dict.set_value("outside_points_3d", ouside_points_3d)
        return STATUS_OK
    except:
        return ERR_y3D