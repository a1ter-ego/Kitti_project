''' *********************************************************
    copyright@2023浙江数智交院科技股份有限公司
    ---------------------------------------------------------
    版本描还信息:0.0.1
    文件名薪: Lib.py
    所属项目: KITTI点云数据在图像上的映射
    所属组件: KITTI点云成像
    功能简介: KITTI的二维，三维点云成像
    版本编号:
            MAJOR          (0)
            MINOR          (0)
            PATCH          (1)
    发布日期:
            YEAR           (2023)
            MONTH          (1)
            DAY            (15)
    备    注：mayavi工具建议在python3.9及以下版本使用
    ---------------------------------------------------------
    修订记录：
        时间  |   版本  |   修订人 |   修订事项    |
    —————————————————————————————————————————————————————————
             |        |         |             |
'''


IMAGE_FILE     = r'..\..\..\KITTI_3d_example\data_object_image_2\data_object_image_2\training\image_2'          # 文件所在位置
LABEL_FILE     = r'.\..\..\KITTI_3d_example\\data_object_label_2\\training\\label_2'
CALIV_FILE     = r'.\..\..\KITTI_3d_example\\data_object_calib\\training\calib'
LIDAR_FILE     = r'.\..\..\KITTI_3d_example\\data_object_velodyne\\data_object_velodyne\\training\\velodyne'
FILE_ID        = '000000'                                                                                       # 文件名称/编号
PICTURE_HEITHT = 720                                                                                            # 显示图像高度
PICTURE_WIDTH  = 1280                                                                                           # 显示图像宽度


