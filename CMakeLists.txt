cmake_minimum_required(VERSION 3.0.0)
project(bgfx_samples VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 11)

# message(@@@@@@@@@@@@${CMAKE_PROJECT_NAME})
# message(@@@@@@@@@@@@${CMAKE_GENERATOR_PLATFORM})
# message(@@@@@@@@@@@@${CMAKE_GENERATOR_PLATFORM})

if (CMAKE_GENERATOR MATCHES "Visual Studio")
    set_property(GLOBAL PROPERTY USE_FOLDERS ON)
endif()

add_subdirectory(modules)
add_subdirectory(src)


set_property(DIRECTORY PROPERTY VS_STARTUP_PROJECT ${CMAKE_PROJECT_NAME})