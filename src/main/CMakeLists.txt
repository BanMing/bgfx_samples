set(MAIN_EXE_NAME main)

add_executable(${MAIN_EXE_NAME} main.cpp)

target_link_libraries(${MAIN_EXE_NAME} PRIVATE module app_helloworld)

if(EMSCRIPTEN)
    target_link_options(
                ${MAIN_EXE_NAME}
                PRIVATE
                -sALLOW_MEMORY_GROWTH=1
                -sMAX_WEBGL_VERSION=2
                -sMIN_WEBGL_VERSION=2
                -sLLD_REPORT_UNDEFINED)
endif()

