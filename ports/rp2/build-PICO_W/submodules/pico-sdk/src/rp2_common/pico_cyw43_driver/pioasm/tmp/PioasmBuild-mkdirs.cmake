# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/Users/dbpiening/git/BitDriveOS/lib/pico-sdk/tools/pioasm"
  "/Users/dbpiening/git/BitDriveOS/ports/rp2/build-PICO_W/submodules/pioasm"
  "/Users/dbpiening/git/BitDriveOS/ports/rp2/build-PICO_W/submodules/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm"
  "/Users/dbpiening/git/BitDriveOS/ports/rp2/build-PICO_W/submodules/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/tmp"
  "/Users/dbpiening/git/BitDriveOS/ports/rp2/build-PICO_W/submodules/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp"
  "/Users/dbpiening/git/BitDriveOS/ports/rp2/build-PICO_W/submodules/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src"
  "/Users/dbpiening/git/BitDriveOS/ports/rp2/build-PICO_W/submodules/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/Users/dbpiening/git/BitDriveOS/ports/rp2/build-PICO_W/submodules/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/Users/dbpiening/git/BitDriveOS/ports/rp2/build-PICO_W/submodules/pico-sdk/src/rp2_common/pico_cyw43_driver/pioasm/src/PioasmBuild-stamp${cfgdir}") # cfgdir has leading slash
endif()
