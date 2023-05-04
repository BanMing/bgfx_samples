from ast import If, Sub
import subprocess
import os
import sys

print("Start Genertaeting...")

arch = sys.argv[1]
project_path = os.path.realpath(os.curdir)
cmake_build_path = project_path + "/out/bgfx_samples_" + arch
generator = sys.argv[2]
toolchain = sys.argv[3]

print("Git Sync...")
# subprocess.call("git submodule update --init --recursive")

if arch == "emsripten":
    subprocess.call(f'emcmake.bat cmake -B {cmake_build_path}')
    subprocess.call(f'cmake --build {cmake_build_path}')
else:
    subprocess.call(
        f'cmake -B {cmake_build_path} -G "{generator}" -A {arch} -DCMAKE_TOOLCHAIN_FILE={toolchain}'
    )
