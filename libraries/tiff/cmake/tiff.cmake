set(tiff_INCLUDE_DIRS $ENV{REZ_TIFF_ROOT}/include)

if(UNIX AND NOT APPLE)
  set(tiff_LIBRARY_DIRS $ENV{REZ_TIFF_ROOT}/lib64)
  set(tiff_LIBRARIES ${tiff_LIBRARY_DIRS}/libtiff.so)
elseif(APPLE)
  set(tiff_LIBRARY_DIRS $ENV{REZ_TIFF_ROOT}/lib)
  set(tiff_LIBRARIES ${tiff_LIBRARY_DIRS}/libtiff.dylib)
endif()


