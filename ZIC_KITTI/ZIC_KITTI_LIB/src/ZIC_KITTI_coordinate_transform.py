'''
    *************************************************************
    *总功能描述：定义函数将点云数据转换为相机的具体坐标，方便映射
    *************************************************************
'''

from ZIC_KITTI_LIB.include.ZIC_KITTI_type import *
from ZIC_KITTI_LIB.src.ZIC_KITTI_lib_common import glob_dict

'''
    ************************************************************************************
    *功能描述： 通过矩阵映射，将点云坐标被映射到了0号相机坐标系里
    *输   入： 
           load_point_cloud       I   导入的列为4的点云矩阵
           calib_velo_to_cam2     I   2号相机和激光雷达之前的坐标转换，是3*4的矩阵
           rect_cam0_matrix       I   雷达到0号相机的旋转矩阵，是4*4的矩阵
    *输   出： 
           cam0_mapping           O   点云坐标映射到了0号相机坐标系之后的过渡坐标
           RotationMatrix_cam0    O   点云坐标映射到了0号相机坐标系之后的矩阵坐标，是4*1矩阵
    ************************************************************************************
'''

def ZIC_KITTI_RotationMatrix_cam0(load_point_cloud,calib_velo_to_cam2,rect_cam0_matrix):                                # 通过矩阵映射，将点云坐标被映射到了0号相机坐标系里
    try:                                                                                                                # 点云坐标映射到了0号相机坐标系之后的过渡坐标                                                                                           # 点云坐标映射到了0号相机坐标系之后的矩阵坐标
        cam0_mapping        = np.hstack((load_point_cloud[:, :3], np.ones((load_point_cloud.shape[0], 1), dtype=np.float32)))
        RotationMatrix_cam0 = np.dot(cam0_mapping, np.dot(calib_velo_to_cam2.T, rect_cam0_matrix.T))
        glob_dict.set_value("cam0_mapping",cam0_mapping)
        glob_dict.set_value("RotationMatrix_cam0",RotationMatrix_cam0)
        return STATUS_OK
    except:
        return ERR_RotationMatrix_cam0

'''
    ************************************************************************************
    *功能描述：将点云从camera0坐标转换为camera2坐标 
    *输入： 
           load_point_cloud       I   导入的列为4的点云矩阵
           rect_cam2_matrix       I   2号相机的矫正矩阵，是3*4的矩阵
           RotationMatrix_cam0    I   点云坐标映射到了0号相机坐标系之后的矩阵坐标，是4*1矩阵
    *输出： 
           y                      O   最终映射得到的图像坐标，是一个3行1列的列向量
           Z_cam                  O   为了变换成齐次坐标的形式，需要做一个归一化，除以Z_cam   
    ************************************************************************************
'''
def ZIC_KITTI_y(load_point_cloud,rect_cam2_matrix,RotationMatrix_cam0):
    cam0_mapping = 0                                                                                                    # 点云坐标映射到了0号相机坐标系之后的过渡坐标
    y = 0                                                                                                               # y最终映射得到的图像坐标，是一个3行1列的列向量
    Z_cam = 0                                                                                                           # 转为齐次坐标的除数因子
    try:
        cam0_mapping        = np.hstack((RotationMatrix_cam0, np.ones((load_point_cloud.shape[0], 1), dtype=np.float32)))
        y                   = np.dot(cam0_mapping, rect_cam2_matrix.T)
        Z_cam               = y[: , 2]
        y                   = (y[: , :2].T/Z_cam).T                                                                     # 为了变换成齐次坐标的形式，需要做一个归一化，除以Z_cam
        glob_dict.set_value("cam0_mapping",cam0_mapping)
        glob_dict.set_value("y",y)
        glob_dict.set_value("Z_cam",Z_cam)
        return STATUS_OK
    except:
        return ERR_y



