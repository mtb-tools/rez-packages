CMAKE_MINIMUM_REQUIRED(VERSION 3.1)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)

ProcessorCount(ncpus)


set(jpeg_version ${JPEG_VERSION})
set(url_jpeg "https://github.com/libjpeg-turbo/libjpeg-turbo/archive/${jpeg_version}.zip")

if(${REZ_BUILD_INSTALL})
    set(install_cmd make -j ${ncpu} install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    jpeg
    URL ${url_jpeg}
    PREFIX jpeg
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
    BUILD_IN_SOURCE 1
)

install(
    FILES cmake/jpeg.cmake cmake/FindJPEG.cmake
    DESTINATION cmake
)
