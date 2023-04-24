from ast import Sub
import subprocess
import os
import sys

print("Start Genertaeting...")

arch = sys.argv[1]
project_path = os.path.realpath(os.curdir)
cmake_build_path = project_path + "/out/bgfx_samples_" + arch
generator = sys.argv[2]
print(cmake_build_path)


print("Git Sync...")
# subprocess.call("git submodule update --init --recursive")

subprocess.call(f"cmake -B {cmake_build_path} -G \"{generator}\" -A {arch}")
