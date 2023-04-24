add_library(module INTERFACE)

set(BGFX_MODULE_FOLDER "module/bgfx")

add_subdirectory(bgfx.cmake)

target_link_libraries(module INTERFACE bgfx bimg bx example-common)
