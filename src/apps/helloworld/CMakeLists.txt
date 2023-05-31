set(
	HELLOWORLD_APP_SOURCES
	helloworld.cpp
	helloworld.h
)

add_library(app_helloworld STATIC ${HELLOWORLD_APP_SOURCES})

target_link_libraries(app_helloworld PRIVATE app_interface)

set_target_properties(app_helloworld PROPERTIES FOLDER "apps")