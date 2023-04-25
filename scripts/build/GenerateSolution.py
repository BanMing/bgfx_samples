from ast import Sub
import subprocess
import os
import sys

print("Start Genertaeting...")

arch = sys.argv[1]
project_path = os.path.realpath(os.curdir)
cmake_build_path = project_path + "/out/bgfx_samples_" + arch
generator = sys.argv[2]
toolchain = sys.argv[3]
print(cmake_build_path)
path_test="E:/Learn/Others/emsdk/upstream/emscripten"

print("Git Sync...")
# subprocess.call("git submodule update --init --recursive")
print(toolchain)
subprocess.call(f"cmake -DCMAKE_TOOLCHAIN_FILE={toolchain} -DEMSCRIPTEN_ROOT_PATH={path_test}")
# subprocess.call(f"cmake -B {cmake_build_path} -G \"{generator}\" -A {arch} -DCMAKE_TOOLCHAIN_FILE={toolchain}")
