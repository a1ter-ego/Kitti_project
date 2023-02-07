''' *********************************************************
    copyright@2023浙江数智交院科技股份有限公司
    ---------------------------------------------------------
    版本描还信息:0.0.2
    文件名薪: Lib.py
    所属项目: KITTI点云数据在图像上的映射
    所属组件: KITTI点云成像
    功能简介: KITTI的二维，三维点云成像
    版本编号:
            MAJOR          (0)
            MINOR          (0)
            PATCH          (2)
    发布日期:
            YEAR           (2023)
            MONTH          (2)
            DAY            (7)
    备    注：mayavi工具建议在python3.9及以下版本使用
    ---------------------------------------------------------
    修订记录：
        时间  |   版本  |   修订人 |   修订事项    |
    —————————————————————————————————————————————————————————
             |        |         |             |
'''


file_id           = '000000'   #默认文件名称
image_path        =  r'..\..\KITTI_3d_example\data_object_image_2\data_object_image_2\training\image_2\{}.png'.format(str(file_id))  #默认路径                     #默认路径
calib_path        =  r'..\..\KITTI_3d_example\data_object_calib\training\calib\{}.txt'.format(str(file_id))                          #默认路径
bin_path          =  r'..\..\KITTI_3d_example\data_object_velodyne\data_object_velodyne\training\velodyne\{}.bin'.format(str(file_id))
PICTURE_SIZE      = [1392,512]  #原始图像的高度为1392 * 512
ZIC_get_mem       = 0           #内存中存储每个变量
ZIC_run           = 0           #算法库的主运行函数

