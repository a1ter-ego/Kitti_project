'''
    *************************************************************
    *功能描述：主函数，呈现二维和三维点云图在图像上的映射
    *输入：导入定义过的函数和参数
    *输出：二维和三维点云图在图像上的映射
    *************************************************************
'''
from lib_kitti.src.KITTI_lib_output_package import *

#FILE_ID          = '000000'
FILE_ID           = input().zfill(6)                                                                 # 用户输出查看的图片                                                                                                    # 导入路径
image_path        = IMAGE_PATH(FILE_ID)                                                              # 导入图片路径
label_path        = LABEL_PATH(FILE_ID)                                                              # 导入标注数据路径
calib_path        = CALIB_PATH(FILE_ID)                                                              # 导入相机矫正数据路径
lidar_path        = LIDAR_PATH(FILE_ID)                                                              # 导入点云数据路径
                                                                                                     # 加载数据
load_image        = LOAD_IMAGE(image_path)                                                           # 导入图片
load_label        = LOAD_LABEL(label_path)                                                           # 导入标注数据
load_calib_P2     = LOAD_CALIB_P2(calib_path)                                                        # 导入左边彩色相机矫正数据
load_calib_R0     = LOAD_CALIB_R0(calib_path)                                                        # 加载0号相机的修正矩阵
load_calib_V2C    = LOAD_CALIB_V2C(calib_path)                                                       # 加载外参矩阵
load_point_cloud  = LOAD_POINT_CLOUD(lidar_path)                                                     # 加载点云数据

scan_C0           = SCAN_C0(load_point_cloud,load_calib_V2C,load_calib_R0)                           # 将点云数据转换为0号相机坐标
scan_C2_temp      = SCAN_C2_TEMP(load_point_cloud,load_calib_P2,scan_C0)
scan_C2_depth     = SCAN_C2_DEPTH(scan_C2_temp)                                                      # 2号相机的深度
scan_C2           = SCAN_C2(scan_C2_temp)                                                            # 转换为2号相机的矩阵坐标

outside_points_2d = OUTSIDE_POINTS_2D(scan_C2,scan_C2_depth,load_image)                              # 生成2d的点云
outside_points_3d = OUTSIDE_POINTS_3D(scan_C2,scan_C2_depth,load_image)                              # 生成3d的点云

scan_C2_3D        = scan_C2[outside_points_3d]                                                       # 2号相机的空间矩阵坐标
scan_in_img       = load_point_cloud[outside_points_3d]                                              # 相机在图片上的空间映射
scan_not_in_img   = load_point_cloud[np.logical_not(outside_points_3d)]                              # 点云数据在图片上的映射

colors            = load_image[scan_C2_3D[:, 1].astype(np.int64), scan_C2_3D[:, 0].astype(np.int64)] # 空间点云的颜色
colors            = np.concatenate([colors, np.ones([colors.shape[0], 1]) * 255], axis=1)



if __name__ == "__main__":
    plt.imshow(load_image)                                                                           # 生成2维点云映射图
    plt.scatter(scan_C2[outside_points_2d, 0], scan_C2[outside_points_2d, 1],
                c= -scan_C2_depth[outside_points_2d],
                alpha=0.5, s=1, cmap='viridis')
    plt.title(FILE_ID)
    plt.axis('off')                                                                                  # 去除横纵坐标
    plt.tight_layout()
    plt.show()
                                                                                                     # 使用mayavi进行3D点云图绘制

    plot           = mlab.points3d(scan_in_img[:, 0], scan_in_img[:, 1],scan_in_img[:, 2],
                                   np.arange(len(scan_in_img)),
                                   mode="point", figure=fig_3D)
    plot.module_manager.scalar_lut_manager.lut._vtk_obj.SetTableRange(0, colors.shape[0])
    plot.module_manager.scalar_lut_manager.lut.number_of_colors = colors.shape[0]
    plot.module_manager.scalar_lut_manager.lut.table = colors
    mlab.view(azimuth=230, distance=50, elevation=60,focalpoint=np.mean(scan_in_img, axis=0)[:-1])
    mlab.show()