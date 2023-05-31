@echo off

py scripts\build\GenerateSolution.py emsripten "MinGW Makefiles" %~dp0cmake\toolchains\Emscripten.cmake %1

pause