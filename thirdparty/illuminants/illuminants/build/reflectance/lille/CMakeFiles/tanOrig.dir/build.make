# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/fausto/IBTSFIF-master/illuminants

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/fausto/IBTSFIF-master/illuminants/build

# Include any dependencies generated for this target.
include reflectance/lille/CMakeFiles/tanOrig.dir/depend.make

# Include the progress variables for this target.
include reflectance/lille/CMakeFiles/tanOrig.dir/progress.make

# Include the compile flags for this target's objects.
include reflectance/lille/CMakeFiles/tanOrig.dir/flags.make

reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o: reflectance/lille/CMakeFiles/tanOrig.dir/flags.make
reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o: ../shell/main.cxx
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/tanOrig.dir/__/shell/main.cxx.o -c /home/fausto/IBTSFIF-master/illuminants/shell/main.cxx

reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tanOrig.dir/__/shell/main.cxx.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/shell/main.cxx > CMakeFiles/tanOrig.dir/__/shell/main.cxx.i

reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tanOrig.dir/__/shell/main.cxx.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/shell/main.cxx -o CMakeFiles/tanOrig.dir/__/shell/main.cxx.s

reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o.requires:

.PHONY : reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o.requires

reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o.provides: reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o.requires
	$(MAKE) -f reflectance/lille/CMakeFiles/tanOrig.dir/build.make reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o.provides.build
.PHONY : reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o.provides

reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o.provides.build: reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o


reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o: reflectance/lille/CMakeFiles/tanOrig.dir/flags.make
reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o: reflectance/lille/tanOrig/tanOrig_modules.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille/tanOrig/tanOrig_modules.cpp

reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille/tanOrig/tanOrig_modules.cpp > CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.i

reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille/tanOrig/tanOrig_modules.cpp -o CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.s

reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o.requires:

.PHONY : reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o.requires

reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o.provides: reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o.requires
	$(MAKE) -f reflectance/lille/CMakeFiles/tanOrig.dir/build.make reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o.provides.build
.PHONY : reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o.provides

reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o.provides.build: reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o


# Object files for target tanOrig
tanOrig_OBJECTS = \
"CMakeFiles/tanOrig.dir/__/shell/main.cxx.o" \
"CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o"

# External object files for target tanOrig
tanOrig_EXTERNAL_OBJECTS =

bin/tanOrig: reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o
bin/tanOrig: reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o
bin/tanOrig: reflectance/lille/CMakeFiles/tanOrig.dir/build.make
bin/tanOrig: reflectance/lille/liblille-lib.a
bin/tanOrig: reflectance/iic_commands/libiic_commands-lib.a
bin/tanOrig: reflectance/iic_eval/libiic_eval-lib.a
bin/tanOrig: reflectance/iic_misc/libiic_misc-lib.a
bin/tanOrig: reflectance/iic_estimator/libiic-lib.a
bin/tanOrig: reflectance/illumestimators/libillumestimators-lib.a
bin/tanOrig: modules/computational_geometry/libcomputational_geometry-lib.a
bin/tanOrig: modules/superpixels/libsuperpixels-lib.a
bin/tanOrig: reflectance/rbase/librbase-lib.a
bin/tanOrig: core/storage/libcache-lib.a
bin/tanOrig: /home/fausto/boost/lib/libboost_filesystem.so
bin/tanOrig: /home/fausto/boost/lib/libboost_serialization.so
bin/tanOrig: /home/fausto/boost/lib/libboost_system.so
bin/tanOrig: core/common/libcommon-lib.a
bin/tanOrig: /opt/opencv/lib/libopencv_videostab.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_ts.a
bin/tanOrig: /opt/opencv/lib/libopencv_superres.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_stitching.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_contrib.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_nonfree.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_ocl.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_gpu.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_photo.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_objdetect.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_legacy.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_video.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_ml.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_calib3d.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_features2d.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_highgui.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_imgproc.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_flann.so.2.4.9
bin/tanOrig: /opt/opencv/lib/libopencv_core.so.2.4.9
bin/tanOrig: /home/fausto/boost/lib/libboost_program_options.so
bin/tanOrig: /usr/lib/x86_64-linux-gnu/libQtCore.so
bin/tanOrig: /usr/lib/x86_64-linux-gnu/libQtGui.so
bin/tanOrig: libcommon-optional-lib.a
bin/tanOrig: reflectance/lille/CMakeFiles/tanOrig.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable ../../bin/tanOrig"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tanOrig.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
reflectance/lille/CMakeFiles/tanOrig.dir/build: bin/tanOrig

.PHONY : reflectance/lille/CMakeFiles/tanOrig.dir/build

reflectance/lille/CMakeFiles/tanOrig.dir/requires: reflectance/lille/CMakeFiles/tanOrig.dir/__/shell/main.cxx.o.requires
reflectance/lille/CMakeFiles/tanOrig.dir/requires: reflectance/lille/CMakeFiles/tanOrig.dir/tanOrig/tanOrig_modules.cpp.o.requires

.PHONY : reflectance/lille/CMakeFiles/tanOrig.dir/requires

reflectance/lille/CMakeFiles/tanOrig.dir/clean:
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille && $(CMAKE_COMMAND) -P CMakeFiles/tanOrig.dir/cmake_clean.cmake
.PHONY : reflectance/lille/CMakeFiles/tanOrig.dir/clean

reflectance/lille/CMakeFiles/tanOrig.dir/depend:
	cd /home/fausto/IBTSFIF-master/illuminants/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/fausto/IBTSFIF-master/illuminants /home/fausto/IBTSFIF-master/illuminants/lille /home/fausto/IBTSFIF-master/illuminants/build /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille /home/fausto/IBTSFIF-master/illuminants/build/reflectance/lille/CMakeFiles/tanOrig.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : reflectance/lille/CMakeFiles/tanOrig.dir/depend

