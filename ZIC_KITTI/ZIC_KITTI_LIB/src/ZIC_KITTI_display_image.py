from ZIC_KITTI_LIB.include.ZIC_KITTI_type import *
'''
    *************************************************************
    *功能描述：在2d图像上画出点云图
    *输入： y                      最终映射得到的图像坐标
           y2D                    去除无效点之后的坐标
           Z_cam                  得到齐次坐标的形式的除数     
           file_id                图像的名称
    *输出： 2d图像上的点云图
    *************************************************************
'''

def ZIC_KITTI_display_2Dimg(image,y,y2D,Z_cam,file_id):
    try:
        plt.imshow(image)                                                                                                   # 生成2维点云映射图
        plt.scatter(y[y2D, 0], y[y2D, 1], c= -Z_cam[y2D],alpha=0.5, s=1)
        plt.title(file_id)
        plt.axis('off')                                                                                                     # 去除横纵坐标
        plt.tight_layout()
    except:
        return ERR_display_2Dimg

'''
    *************************************************************
    *功能描述：在3d图像上画出点云图
    *输入： cam_in_img             2号相机对应图片的坐标
           colors                 获取图像数据（image）上面的颜色
    *输出： 3d图像上的点云图
    *************************************************************
'''
def ZIC_KITTI_display_3Dimg(cam_in_img,colors):
    try:
        plot = mlab.points3d(cam_in_img[:, 0], cam_in_img[:, 1], cam_in_img[:, 2],np.arange(len(cam_in_img)),mode="point", figure=fig_3D)
        plot.module_manager.scalar_lut_manager.lut._vtk_obj.SetTableRange(0, colors.shape[0])
        plot.module_manager.scalar_lut_manager.lut.number_of_colors = colors.shape[0]
        plot.module_manager.scalar_lut_manager.lut.table = colors
        mlab.view(azimuth=230, distance=50, elevation=60, focalpoint=np.mean(cam_in_img, axis=0)[:-1])
    except:
        return ERR_display_3Dimg

'''
    ************************************************************************************
    *功能描述： 自身内存占有空间的函数
    *输出： 
           info    O   所占内存的大小
    ************************************************************************************
'''

def get_current_memory_gb() -> int:
    pid    = 0                                                  # 程序自己的进程识别标识符
    info   = 0                                                  # 内存的信息
    pid    = os.getpid()
    info   = psutil.Process(pid).memory_full_info()
    return info.uss / 1024. / 1024. / 1024.                     # 单位转换为GB