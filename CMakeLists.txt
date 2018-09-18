cmake_minimum_required (VERSION 2.6)
project(test)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(OPEN_SLP_SRC /home/kim/test_project/thirdparty/openslp-2.0.0)
set(TEST_LIB_SRC /home/kim/test_project/thirdparty/c-test-library)

#find_library(OPEN_SLP slp /home/kim/test_project/thirdparty/openslp-1.0.0/libslp/.libs)
find_library(TEST_LIB hello ${TEST_LIB_SRC})

include_directories(${TEST_LIB_SRC})
#link_directories(${TEST_LIB_SRC})
#set_target_properties(open_slp PROPERTIES LINKER_LANGUAGE C)


include_directories(src/myproject/include)

add_executable(Test src/myproject/main.cpp)


target_link_libraries(Test 
	#	${OPEN_SLP}
		${TEST_LIB})









#add_library(open_slp 
#	${OPEN_SLP_SRC}/libslp/libslp_delattrs.c
#	${OPEN_SLP_SRC}/libslp/libslp_dereg.c
#	${OPEN_SLP_SRC}/libslp/libslp_findattrs.c
#	${OPEN_SLP_SRC}/libslp/libslp_findscopes.c
#	${OPEN_SLP_SRC}/libslp/libslp_findsrvs.c
#	${OPEN_SLP_SRC}/libslp/libslp_findsrvtypes.c
#	${OPEN_SLP_SRC}/libslp/libslp_handle.c
#	${OPEN_SLP_SRC}/libslp/libslp_knownda.c
#	${OPEN_SLP_SRC}/libslp/libslp_network.c
#	${OPEN_SLP_SRC}/libslp/libslp_parse.c
#	${OPEN_SLP_SRC}/libslp/libslp_property.c
#	${OPEN_SLP_SRC}/libslp/libslp_reg.c
#)
