set( APP_SOURCES
	application.cpp
	application.h
)


add_library(app_interface STATIC ${APP_SOURCES})

target_link_libraries(app_interface PRIVATE bx bimg bgfx example-common)

set_target_properties(app_interface PROPERTIES FOLDER "apps")

add_subdirectory(helloworld)