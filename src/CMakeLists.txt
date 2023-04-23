
include_directories(${PROJECT_SOURCE_DIR}/src/)


file(GLOB_RECURSE MAIN_FILES main.cpp)

add_executable(${PROJECT_NAME} ${MAIN_FILES})
