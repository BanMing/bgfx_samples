@echo off

py scripts\build\GenerateSolution.py x64 "Visual Studio 17 2022" %~dp0cmake\toolchains\WIN64.cmake %1
