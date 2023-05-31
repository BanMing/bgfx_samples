set(
	DEBUG_DRAW_SAPMLE_SOURCES
	debug_draw_sample.cpp
	debug_draw_sample.h
)

add_library(app_debug_draw_sample STATIC ${DEBUG_DRAW_SAPMLE_SOURCES})

target_link_libraries(app_debug_draw_sample PRIVATE app_interface)

set_target_properties(app_debug_draw_sample PROPERTIES FOLDER "apps")