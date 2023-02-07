'''
    *************************************************************
    *功能描述：导入所需要的python外部包
    *************************************************************
'''
import os
import time
import psutil
import numpy             as np
import seaborn           as sns
import matplotlib.pyplot as plt
import mayavi.mlab       as mlab
from   skimage           import io
from   matplotlib.lines  import Line2D

'''
    *************************************************************
                             宏开关
    *************************************************************
'''
# def _DEGUG
# def _USE_SCIKI_IMAGE
# def _USE_MAYAVI
'''
    *************************************************************
                            定义状态码
    *************************************************************
'''
STATUS_OK            = 0                   #状态正常
STATUS_ERR           = 1                   #状态异常
'''
    *************************************************************
                            定义错误码
    *************************************************************
'''
ERR_INIT                   = 0x00000000         #错误码初始值
ERR_LOAD_image             = 0x00000001         #数据导入错误
ERR_LOAD_cam_matrix        = 0x00000002         #矩阵运行错误
ERR_LOAD_cam0_matrix       = 0x00000003         #0号相机矫正矩阵运行错误
ERR_LOAD_cam2_matrix       = 0x00000004         #2号相机矫正矩阵运行错误
ERR_LOAD_velo_to_cam2      = 0x00000005         #点云相机转换矩阵运行错误
ERR_LOAD_point_cloud       = 0x00000006         #点云数据导入错误
ERR_RotationMatrix_cam0    = 0x00000007         #映射到0号相机坐标错误
ERR_y                      = 0x00000008         #生成最终图像坐标错误
ERR_y2D                    = 0x00000009         #生成2d坐标错误
ERR_y3D                    = 0x0000000A         #生成3d坐标错误
ERR_display_2Dimg          = 0x0000000B         #2d展示错误
ERR_display_3Dimg          = 0x0000000C         #3d展示错误
'''            
    *************************************************************
                            定义结构体
    *************************************************************
'''
class  ZIC_image:
    def __int__(self):
        self.file_id           = '000007'
        self.fig_2D            = plt.figure(figsize=(14, 5))                          # 二维图片刻度比例
        self.fig_3D            = mlab.figure(bgcolor=(0, 0, 0), size=(1280, 720))     # 三维像素大小
        self.colors            = sns.color_palette('Paired', 9 * 2)                   # 色彩种类

class ZIC_matrix:
    def __int__(self):
        self.load_point_cloud  = 0                                                    # 导入的列为4的点云矩阵
        self.calib_velo_to_cam2= 0                                                    # 2号相机和激光雷达之前的坐标转换，是3*4的矩阵
        self.rect_cam0_matrix  = 0                                                    # 雷达到0号相机的旋转矩阵，是4*4的矩阵
        self.RotationMatrix_cam= 0                                                    # 点云坐标映射到了0号相机坐标系之后的矩阵坐标，是4*1矩阵
        self.rect_cam2_matrix  = 0                                                    # 2号相机的矫正矩阵，是3*4的矩阵
        self.y                 = 0                                                    # 最终映射得到的图像坐标，是一个3行1列的列向量
'''           
    *************************************************************
                            定义内部常量
    *************************************************************
'''

image                   = 0                                                          #导入图像
label                   = 0                                                          #导入坐标
all_cam_matrix          = 0                                                          #所有矩阵
rect_cam2_matrix        = 0                                                          #0号相机矫正矩阵，是3*4的矩阵
rect_cam0_matrix        = 0                                                          #2号相机矫正矩阵，是4*4的矩阵
calib_velo_to_cam2      = 0                                                          #点云相机转换矩阵，是3*4的矩阵
load_point_cloud        = 0                                                          #点云数据,是列为4的矩阵
cam0_mapping            = 0                                                          #映射到0号相机坐标
RotationMatrix_cam0     = 0                                                          #生成最终图像坐标
y                       = 0                                                          #生成2d坐标
Z_cam                   = 0                                                          #生成3d坐标
outside_points_2d       = 0                                                          #2d展示
outside_points_3d       = 0                                                          #3d展示
fig_2D                  = plt.figure(figsize=(14, 5))                                # 二维图片刻度比例
fig_3D                  = mlab.figure(bgcolor=(0, 0, 0), size=(1280, 720))           # 三维像素大小
colors                  = sns.color_palette('Paired', 9 * 2)                         # 色彩种类