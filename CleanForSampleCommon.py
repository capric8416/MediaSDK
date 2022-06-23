import os
import shutil
import subprocess


paths = (
    '.github',
    '_studio',
    'android',
    'builder',
    'contrib',
    'doc',
    'tests',
    'tools',
    'tutorials',
    'Android.mk',
    'CHANGELOG.md',
    'CMakeLists.txt',
    'CODEOWNERS',
    'CONTRIBUTING.md',
    'LICENSE',
    'mfxconfig.h.in',
    'MODULE_LICENSE_MIT',
    'NOTICE',
    'README.rst',

    'api/Android.bp',
    'api/Android.mk',
    'api/mfx_dispatch/linux',
    'api/mfx_dispatch/Android.mk',

    'samples/Android.mk',
    'samples/CMakeLists.txt',
    'samples/sample_camera',
    'samples/sample_encode',
    'samples/sample_hevc_fei_abr',
    'samples/sample_plugins',
    'samples/sample_fei',
    'samples/sample_misc',
    'samples/sample_vpp',
    'samples/metrics_monitor',
    'samples/sample_decode',
    'samples/sample_hevc_fei',
    'samples/sample_multi_transcode',
    'samples/sample_common/Android.mk',
    'samples/sample_common/CMakeLists.txt',
    'samples/sample_common/include/vaapi_allocator.h',
    'samples/sample_common/include/vaapi_device.h',
    'samples/sample_common/include/vaapi_utils.h',
    'samples/sample_common/include/vaapi_utils_android.h',
    'samples/sample_common/include/vaapi_utils_drm.h',
    'samples/sample_common/include/vaapi_utils_drm.h',
    'samples/sample_common/include/vaapi_utils_x11.h',
    'samples/sample_common/include/vpp_ex.h',
    'samples/sample_common/src/vaapi_allocator.cpp',
    'samples/sample_common/src/vaapi_device.cpp',
    'samples/sample_common/src/vaapi_utils.cpp',
    'samples/sample_common/src/vaapi_utils_android.cpp',
    'samples/sample_common/src/vaapi_utils_drm.cpp',
    'samples/sample_common/src/vaapi_utils_x11.cpp',
    'samples/sample_common/src/vpp_ex.cpp',
)

if __name__ == '__main__':
    for p in paths:
        # test existing
        if not os.path.exists(p):
            continue

        # remove and commit
        if os.path.isdir(p):
            shutil.rmtree(p, ignore_errors=True)
            subprocess.run(['git', 'add', f'{p}/*'])
        else:
            os.remove(p)
            subprocess.run(['git', 'add', p])
