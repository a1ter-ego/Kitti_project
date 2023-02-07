'''
    *************************************************************
    *功能描述：展示给用户的图像界面
    *输入：ZIC_run 主函数
    *输出：二维和三维点云图在图像上的映射
    *************************************************************
'''
'''
    *************************************************************
    *功能描述：导入函数ZIC_run
    *************************************************************
'''
from ZIC_KITTI_LIB.src.ZIC_KITTI_output import *

'''
    *************************************************************
    *功能描述：用户可以随意替换或者查询想看的图片
    *************************************************************
'''
file_id           = '000010'   #默认文件名称
image_path        =  r'..\..\KITTI_3d_example\data_object_image_2\data_object_image_2\training\image_2\{}.png'.format(str(file_id))  #默认路径                     #默认路径
calib_path        =  r'..\..\KITTI_3d_example\data_object_calib\training\calib\{}.txt'.format(str(file_id))                          #默认路径
bin_path          =  r'..\..\KITTI_3d_example\data_object_velodyne\data_object_velodyne\training\velodyne\{}.bin'.format(str(file_id))

'''
    *************************************************************
    *功能描述：运行主函数ZIC_run
    *************************************************************
'''
if __name__ == "__main__":
    ERR_list = ZIC_run(file_id,image_path,calib_path,bin_path)

    if len(ERR_list) == 0:                                                               #错误排查
        print("run successfully！")
    else:
        print('number of errors：' ,len(ERR_list),'\nlist of error code: ', ERR_list)

    plt.show()                                                                            #图像展示
    mlab.show()

