set(png_INCLUDE_DIRS $ENV{REZ_PNG_ROOT}/include)

if(UNIX AND NOT APPLE)
	set(png_LIBRARY_DIRS $ENV{REZ_PNG_ROOT}/lib64)
elseif(APPLE)
	set(png_LIBRARY_DIRS $ENV{REZ_PNG_ROOT}/lib)
endif()

if(png_STATIC)
	set(png_LIBRARIES ${png_LIBRARY_DIRS}/libpng.a)

else()
	if(UNIX AND NOT APPLE)
		set(png_LIBRARIES ${png_LIBRARY_DIRS}/libpng.so)
	elseif(APPLE)
		set(png_LIBRARIES ${png_LIBRARY_DIRS}/libpng.dylib)
	endif()
endif()
