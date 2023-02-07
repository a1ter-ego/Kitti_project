'''
    ********************************************************************************
    *功能描述：将导入的数据，转换为可以用的全局常量
    ********************************************************************************
'''

from ZIC_KITTI_LIB.include.ZIC_KITTI_type import *
from ZIC_KITTI_LIB.src.ZIC_KITTI_lib_common import glob_dict

'''
    ********************************************************************************
    *功能描述：导入KITTI图片
    *输   入：
             image_path I      图片路径
    *输   出：
             image      O      图片数据
    ********************************************************************************
'''
def READ_image(image_path):
    image = 0
    try:
        image = np.array(io.imread(image_path), dtype=np.int32)
        glob_dict.set_value("image", image)
        return STATUS_OK
    except:
        return ERR_LOAD_image

'''
    ********************************************************************************
    *功能描述：导入所有相机的矫正矩阵数据
    *输   入：
             calib_path         I      矫正数据路径
    *输   出： 
             all_cam_matrix     O      相机矫正数据
    ********************************************************************************
'''

def READ_all_cam_matrix(calib_path):
    all_cam_matrix = 0
    try:
        with open(calib_path, 'r') as f:
            all_cam_matrix = f.readlines()
            glob_dict.set_value("all_cam_matrix", all_cam_matrix)
        return STATUS_OK
    except:
        return ERR_LOAD_cam_matrix

'''
    ********************************************************************************
    *功能描述：导入左边彩色相机矫正数据
    *输   入：
             all_cam_matrix       I      相机矫正数据
    *输   出： 
             rect_cam2_matrix     O      2号相机的矫正矩阵，是3*4的矩阵
    ********************************************************************************
'''

def READ_cam2_matrix(all_cam_matrix):
    rect_cam2_matrix = 0
    try:
        rect_cam2_matrix = np.array(all_cam_matrix[2].strip().split(' ')[1:], dtype=np.float32).reshape(3, 4)
        glob_dict.set_value("rect_cam2_matrix",rect_cam2_matrix)
        return STATUS_OK
    except:
        return ERR_LOAD_cam2_matrix
'''
    ********************************************************************************
    *功能描述：加载0号相机的修正矩阵
    *输   入：
             all_cam_matrix       I      相机矫正数据
    *输    出：
             rect_cam0_matrix     O      雷达到0号相机的旋转矩阵，是4*4的矩阵
    ********************************************************************************
'''

def READ_cam0_matrix(all_cam_matrix):
    rect_cam0_matrix = 0
    try:
        rect_cam0_matrix    = np.array(all_cam_matrix[4].strip().split(' ')[1:], dtype=np.float32).reshape(3, 3)
        glob_dict.set_value("rect_cam0_matrix",rect_cam0_matrix)
        return STATUS_OK
    except:
        return ERR_LOAD_cam0_matrix

'''
    ********************************************************************************
    *功能描述：点云位置坐标投影到相机坐标系前，需要转换到世界坐标系下，对应的矩阵为外参矩阵。
    *输   入：
             all_cam_matrix         I      相机矫正数据
    *输   出：
             calib_velo_to_cam2     O      2号相机和激光雷达之前的坐标转换，是3*4的矩阵
    ********************************************************************************
'''
def READ_velo_to_cam2(all_cam_matrix):
    calib_velo_to_cam2 = 0
    try:
        calib_velo_to_cam2    = np.array(all_cam_matrix[5].strip().split(' ')[1:], dtype=np.float32).reshape(3, 4)
        glob_dict.set_value("calib_velo_to_cam2",calib_velo_to_cam2)
        return STATUS_OK
    except:
        return ERR_LOAD_velo_to_cam2

'''
    ********************************************************************************
    *功能描述：加载点云数据
    *输   入：
             bin_path               I      bin文件路径
    *输   出：
             load_point_cloud       O      点云数据，列为4的矩阵
    ********************************************************************************
'''

def READ_point_cloud (bin_path):
    load_point_cloud = 0
    try:
        load_point_cloud    = np.fromfile(bin_path, dtype=np.float32).reshape(-1, 4)
        glob_dict.set_value("load_point_cloud",load_point_cloud)
        return STATUS_OK
    except:
        return ERR_LOAD_point_cloud

