'''
配置文件
'''

config = {
    #debug模式，如果开启，则会只进行截屏而不答题，积累训练图片，请手动答题
    'debug': False,
    #表达式区域的顶部处于整张图片的位置(307/854=0.359)
    'exp_area_top_rate': 0.36,
    #表达式区域的底部处于整张图片的位置(478/854=0.559)
    'exp_area_bottom_rate': 0.56,
    #图片二值化时的阈值
    'binary_threshold': 200,
    #'binary_threshold': 150,


    # 从PC端截屏时，截取区域左上角相对桌面的x坐标
    'projection_x': 16,
    # 从PC端截屏时，截取区域左上角相对桌面的y坐标
    'projection_y': 60,
    # 从PC端截屏时，截取区域的宽度
    'projection_width': 482,
    # 从PC端截屏时，截取区域的高度
    'projection_height': 854,
    #使用PC进行截图时点击手机屏幕正确区域的x坐标
    'pc_tap_true_x':117,
    #使用PC进行截图时点击手机屏幕错误区域的x坐标
    'pc_tap_false_x':365,
    #使用PC进行截图时点击手机屏幕正确和区域的y坐标
    'pc_tap_y':760,
    #使用PC截屏时一个字符的宽度
    'pc_single_char_width':25,

    #每次截图重复时休眠的时间
    'sleep_when_repeat':0.9,
}