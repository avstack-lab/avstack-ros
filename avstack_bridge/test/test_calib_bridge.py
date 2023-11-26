import sys

from sensor_msgs.msg import CameraInfo

from avstack_bridge.calibration import CameraCalibrationBridge


sys.path.append("tests/")
from utilities import camera_calib


def test_calib_to_caminfo():
    c_bridge = CameraCalibrationBridge()
    caminfo = c_bridge.calib_to_caminfomsg(camera_calib, timestamp=1.0)
    assert isinstance(caminfo, CameraInfo)
