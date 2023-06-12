# Create an INTERFACE library for our C module.
add_library(memmon INTERFACE)

# Add our source files to the lib
target_sources(memmon INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}/memmon.c
)

# Add the current directory as an include directory.
target_include_directories(memmon INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}
)

# Link our INTERFACE library to the usermod target.
target_link_libraries(usermod INTERFACE memmon)
