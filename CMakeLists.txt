cmake_minimum_required(VERSION 3.0.0)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_PROJECT_NAME bgfx_samples)
project(${CMAKE_PROJECT_NAME} VERSION 0.1.0)

if (EMSCRIPTEN)
    include(cmake/environments/Emsripten.cmake)
elseif(APPLE)
    include(cmake/environments/MAC.cmake)
else()
    include(cmake/environments/WIN64.cmake)
endif()

message("Current Platform: [${PLATFORM}]")

add_subdirectory(modules)
add_subdirectory(src)

if (CMAKE_GENERATOR MATCHES "Visual Studio")
    set_property(GLOBAL PROPERTY USE_FOLDERS ON)
    set_property(DIRECTORY PROPERTY VS_STARTUP_PROJECT ${MAIN_EXE_NAME})
endif()