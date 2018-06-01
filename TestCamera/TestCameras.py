import os
import time
import ctypes


def WindowsIs64bit():
    return 'PROGRAMFILES(X86)' in os.environ

if WindowsIs64bit():
    import uEye_64 as uEye
else:
    import uEye_32 as uEye


class SimpleUEyeDriver:
    def __init__(self):
        self._hid = uEye.HIDS(0)
        self._width = 2560
        self._height = 1920
        self._bpp = 8
        self._buff = ctypes.c_char_p()
        self._buff_id = ctypes.c_int(0)

    def connect(self):
        res = uEye.is_InitCamera(ctypes.byref(self._hid), None)
        if res != uEye.IS_SUCCESS:
            print("is_InitCamera failed")
            return False

        self._buff = ctypes.c_char_p()
        self._buff_id = ctypes.c_int(0)

        res = uEye.is_AllocImageMem(
            self._hid,
            self._width, self._height, self._bpp,
            ctypes.byref(self._buff),
            ctypes.byref(self._buff_id))
        if res != uEye.IS_SUCCESS:
            print("is_AllocImageMem failed")
            return False

        res = uEye.is_SetImageMem(self._hid, self._buff, self._buff_id)
        if res != uEye.IS_SUCCESS:
            print("is_SetImageMem failed")
            return False

        return True


def disable_cpu_idle_mode():
    # Disable CPU idle mode for both AC and battery power for better USB performance
    cpu_states = ctypes.c_void_p(uEye.IS_CONFIG_CPU_IDLE_STATES_BIT_AC_VALUE |
                                 uEye.IS_CONFIG_CPU_IDLE_STATES_BIT_DC_VALUE)
    return uEye.IS_SUCCESS == uEye.is_Configuration(
        uEye.IS_CONFIG_CPU_IDLE_STATES_CMD_SET_DISABLE_ON_OPEN,
        ctypes.byref(cpu_states),
        ctypes.sizeof(cpu_states) if not WindowsIs64bit() else 4)


if __name__ == "__main__":
    if not disable_cpu_idle_mode():
        print("Failed to disable CPU idle mode")

    n = ctypes.c_int32(0)
    if uEye.is_GetNumberOfCameras(ctypes.byref(n)) == uEye.IS_SUCCESS:
        num_cameras = n.value
        print("Found %d attached camera(s)" % num_cameras)

        if num_cameras > 0:
            print("Trying to connection to cameras")

            cameras = []
            for _ in range(0, num_cameras):
                next_cam = SimpleUEyeDriver()
                if next_cam.connect():
                    cameras.append(next_cam)

            num_cameras_connected = len(cameras)
            if num_cameras_connected == num_cameras:
                print("Successfully connected to %d cameras" % num_cameras_connected)
            else:
                print("Connected to %d out of %d total cameras" % (num_cameras_connected, num_cameras))

    # Wait until the process is killed - let the camera resources leak
    print("Waiting forever...")
    while True:
        time.sleep(30)
