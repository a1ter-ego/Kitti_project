'''
    *************************************************************
    *功能描述：导出所需要的py文件
    *************************************************************
'''

from ZIC_KITTI_LIB.src.ZIC_KITTI_coordinate_init import *
from ZIC_KITTI_LIB.src.ZIC_KITTI_coordinate_transform import *
from ZIC_KITTI_LIB.src.ZIC_KITTI_coodinate_filter import *
from ZIC_KITTI_LIB.src.ZIC_KITTI_display_image import *

'''
    *************************************************************
    *功能描述：数据处理
    *************************************************************
'''
def ZIC_run(file_id,image_path,calib_path,bin_path):
    '''
        *************************************************************
        函数内部声明变量
        *************************************************************
    '''
    global image                       # 导入图像
    global label                       # 导入坐标
    global all_cam_matrix              # 所有矩阵
    global rect_cam2_matrix            # 0号相机矫正矩阵，是3*4的矩阵
    global rect_cam0_matrix            # 2号相机矫正矩阵，是4*4的矩阵
    global calib_velo_to_cam2          # 点云相机转换矩阵，是3*4的矩阵
    global load_point_cloud            # 点云数据,是列为4的矩阵
    global cam0_mapping                # 映射到0号相机坐标
    global RotationMatrix_cam0         # 生成最终图像坐标
    global y                           # 生成2d坐标
    global Z_cam                       # 生成3d坐标
    global outside_points_2d           # 2d展示
    global outside_points_3d           # 3d展示
    global cam_C2_3D                   # 生成3d颜色坐标
    global colors                      # 生成3d颜色
    ERR_list = []                      # 错误集合

    try:
        READ_image(image_path)
        image = glob_dict.get_value("image")
    except:
        ERR_list.append(READ_image(image_path))


    try:
        READ_all_cam_matrix(calib_path)
        all_cam_matrix = glob_dict.get_value("all_cam_matrix")
    except:
        ERR_list.append(READ_all_cam_matrix(calib_path))

    try:
        READ_cam2_matrix(all_cam_matrix)
        rect_cam2_matrix = glob_dict.get_value("rect_cam2_matrix")
    except:
        ERR_list.append(READ_cam2_matrix(all_cam_matrix))

    try:
        READ_cam0_matrix(all_cam_matrix)
        rect_cam0_matrix = glob_dict.get_value("rect_cam0_matrix")
    except:
        ERR_list.append(READ_cam0_matrix(all_cam_matrix))

    try:
        READ_velo_to_cam2(all_cam_matrix)
        calib_velo_to_cam2 = glob_dict.get_value("calib_velo_to_cam2")
    except:
        ERR_list.append(READ_velo_to_cam2(all_cam_matrix))

    try:
        READ_point_cloud(bin_path)
        load_point_cloud = glob_dict.get_value("load_point_cloud")
    except:
        ERR_list.append(READ_point_cloud(bin_path))

    try:
        ZIC_KITTI_RotationMatrix_cam0(load_point_cloud, calib_velo_to_cam2, rect_cam0_matrix)
        RotationMatrix_cam0 = glob_dict.get_value("RotationMatrix_cam0")
    except:
        ERR_list.append(ZIC_KITTI_RotationMatrix_cam0(load_point_cloud, calib_velo_to_cam2, rect_cam0_matrix))

    try:
        ZIC_KITTI_y(load_point_cloud, rect_cam2_matrix, RotationMatrix_cam0)
        y = glob_dict.get_value("y")
        Z_cam = glob_dict.get_value("Z_cam")
    except:
        ERR_list.append(ZIC_KITTI_y(load_point_cloud, rect_cam2_matrix, RotationMatrix_cam0))

    try:
        ZIC_KITTI_y2D(y, Z_cam, image)
        outside_points_2d = glob_dict.get_value("outside_points_2d")
    except:
        ERR_list.append(ZIC_KITTI_y2D(y, Z_cam, image))

    try:
        ZIC_KITTI_y3D(y, Z_cam, image)
        outside_points_3d = glob_dict.get_value("outside_points_3d")
    except:
        ERR_list.append(ZIC_KITTI_y3D(y, Z_cam, image))

    try:
        ZIC_KITTI_display_2Dimg(image, y, outside_points_2d, Z_cam, file_id)                 # 2d图像展示
    except:
        ERR_list.append(ZIC_KITTI_display_2Dimg(image, y, outside_points_2d, Z_cam, file_id))

    try:
        cam_C2_3D = y[outside_points_3d]
        colors = image[cam_C2_3D[:, 1].astype(np.int64), cam_C2_3D[:, 0].astype(np.int64)]   # 空间点云的颜色
        colors = np.concatenate([colors, np.ones([colors.shape[0], 1]) * 255], axis=1)
        ZIC_KITTI_display_3Dimg(load_point_cloud[outside_points_3d], colors)                 # 3d图像展示
    except:
        ERR_list.append(ZIC_KITTI_display_3Dimg(load_point_cloud[outside_points_3d], colors))

    return ERR_list