CMAKE_MINIMUM_REQUIRED(VERSION 3.12)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
set(url https://github.com/AcademySoftwareFoundation/openexr/archive/v${version}.tar.gz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()


ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    #SOURCE_DIR ${PROJECT_BINARY_DIR}/${name}/src/${name}
    # UPDATE_COMMAND ./bootstrap
    #CONFIGURE_COMMAND cd OpenEXR && export CXXFLAGS=-pipe\ -g0\ -O3\ -std=c++14 && ./configure
    CONFIGURE_COMMAND cmake  -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)

install(CODE "message(STATUS Running Phony install)")
