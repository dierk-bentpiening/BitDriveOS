#!/bin/bash
echo "[PICO W] Cleaning Buildirectory..."
make BOARD=PICO_W  clean
echo "[PICO W] Make Submodules..."
make BOARD=PICO_W  submodules
echo "[PICO W] Building Firmware..."
make BOARD=PICO_W USER_C_MODULES=../../bdosmod/memmon/micropython.cmake

echo "[PICO] Cleaning Buildirectory..."
make clean
echo "[PICO] Make Submodules..."
make submodules
echo "[PICO] Building Firmware..."
make