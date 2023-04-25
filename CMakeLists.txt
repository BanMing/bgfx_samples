cmake_minimum_required(VERSION 3.0.0)

set(CMAKE_CXX_STANDARD 11)

message("Current Platform: [${CMAKE_GENERATOR_PLATFORM}]")
set(CMAKE_PROJECT_NAME bgfx_samples_${CMAKE_GENERATOR_PLATFORM})
project(${CMAKE_PROJECT_NAME} VERSION 0.1.0)

# message("Current Platform1: [${CMAKE_CXX_COMPILER}] [${CMAKE_C_COMPILER}]")
# SET(CMAKE_CXX_COMPILER "em++")
# SET(CMAKE_C_COMPILER "emcc")
# message("Current Platform2: [${CMAKE_CXX_COMPILER}] [${CMAKE_C_COMPILER}]")

# SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -s WASM=1 -s SIDE_MODULE=1")
# SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -s WASM=1 -s SIDE_MODULE=1")

if (CMAKE_GENERATOR MATCHES "Visual Studio")
    set_property(GLOBAL PROPERTY USE_FOLDERS ON)
endif()

# if (${CMAKE_GENERATOR_PLATFORM} STREQUAL x64)
#     include(cmake/environments/WIN64.cmake)
# elseif (${CMAKE_GENERATOR_PLATFORM} STREQUAL Emsripten)
    include(cmake/environments/Emsripten.cmake)
# endif()

add_subdirectory(modules)
add_subdirectory(src)


set_property(DIRECTORY PROPERTY VS_STARTUP_PROJECT ${CMAKE_PROJECT_NAME})