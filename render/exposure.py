"""相机测光：EV、亮度与百分位：待实现的核心模块。"""


def ev_scale(ev):
    """EV 转倍数。"""
    raise NotImplementedError

def luminance(rgb):
    """亮度。"""
    raise NotImplementedError

def percentile(hist, percentile):
    """直方图百分位。"""
    raise NotImplementedError

def center_weight(x, y, width, height):
    """中心测光权重。"""
    raise NotImplementedError

def adapt(current, target, speed):
    """曝光平滑。"""
    raise NotImplementedError
