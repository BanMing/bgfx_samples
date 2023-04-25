@echo off

py scripts\build\GenerateSolution.py Emsripten "Visual Studio 17 2022" %~dp0cmake\toolchains\Emscripten.cmake %1
