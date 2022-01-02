CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(version $ENV{REZ_BUILD_PROJECT_VERSION})
set(name $ENV{REZ_BUILD_PROJECT_NAME})
string(REPLACE "." "_" release_version ${version})
set(url https://github.com/libexpat/libexpat/releases/download/R_${release_version}/expat-${version}.tar.xz)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)


if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd echo "skip install step")
endif()

ExternalProject_add(
    ${name}
    URL ${url}
    PREFIX ${name}
    CONFIGURE_COMMAND cmake
        -DCMAKE_INSTALL_PREFIX=$ENV{REZ_BUILD_INSTALL_PATH}
        -DYAML_CPP_BUILD_TESTS=OFF
        ../${name}
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND ${install_cmd}
)

install(CODE "message(STATUS Dummy Install Target)")
