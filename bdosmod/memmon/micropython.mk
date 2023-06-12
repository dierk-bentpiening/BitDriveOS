MEMMON_MOD_DIR := $(memmon)

# Add all C files to SRC_USERMOD.
SRC_USERMOD += $(MEMMON_MOD_DIR)/memmon.c

# We can add our module folder to include paths if needed
# This is not actually needed in this example.
CFLAGS_USERMOD += -I$(MEMMON_MOD_DIR)
CEXAMPLE_MOD_DIR := $(USERMOD_DIR)
