'''
    *************************************************************
    *功能描述：测试函数，用pytest判断数据是否成功加载，坐标是否成功转换
    *输入：主函数的数据，和相关的判断条件
    *输出：测试结果：pass表示成功，fail表示失败
    *************************************************************
'''
import pytest
from demo.main import *

class Test_load_data():                                           #测试数据是否载入成功
    def test_load_image(self):
        print("测试图片是否成功加载")
        assert load_image is not None

    def test_load_label(self):
        print("测试标签是否成功加载")
        assert load_label is not None

    def test_load_calib_P2(self):
        print("测试2号相机矫正数据是否成功加载")
        assert load_calib_P2 is not None

    def test_load_calib_R0(self):
        print("测试R0矫正矩阵是否成功加载")
        assert load_calib_R0 is not None

    def test_load_calib_V2C(self):
        print("测试点云矩阵数据是否成功加载")
        assert load_calib_V2C is not None

    def test_load_point_cloud(self):
        print("测试点云数据是否成功加载")
        assert load_point_cloud is not None

class Test_calib_data():                                          #测试数据是否转换成功
    def test_scan_C0(self):
        print("矫正之后的0号相机坐标")
        assert scan_C0 is not None

    def test_scan_C2(self):
        print("矫正之后的2号相机坐标")
        assert scan_C2 is not None

    def test_scan_C2_3D(self):
        print("矫正之后的2号相机3维坐标")
        assert scan_C2_3D is not None

    def test_outside_points_2d(self):
        print("可以直接呈现的二维点云数据")
        assert outside_points_2d is not None

    def test_outside_points_3d(self):
        print("可以直接呈现的三维点云数据")
        assert outside_points_3d is not None




