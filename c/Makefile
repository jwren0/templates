## User configuration ##
CC ?= gcc
CCFLAGS ?= -march=native -O2 -pipe

BIN_DIR ?= /usr/bin

EXEC := example


## Developer configuraton ##
CCFLAGS := $(CCFLAGS) -Werror -Wall -Wextra -Wformat-security \
	   -Wpedantic -pedantic-errors -std=c18

SRC_FILES := $(shell find . -regex ".*\.c")
OBJ_FILES := ${SRC_FILES:.c=.o}


## User targets ##
.PHONY: build install uninstall clean

build: $(EXEC)
build_debug: $(EXEC)_debug
build_static: $(EXEC)_static

install: build
	@install -m 755 -v $(EXEC) $(BIN_DIR)/

uninstall:
	@rm -f $(BIN_DIR)/$(EXEC)

clean:
	@rm -rf $(OBJ_FILES) $(EXEC) \
		$(EXEC)_debug $(EXEC)_static


## Developer targets ##
$(EXEC): $(OBJ_FILES)
	@printf "LD      $@\n"
	@$(CC) $(CCFLAGS) -Xlinker --strip-all -o $@ $^

$(EXEC)_debug: $(OBJ_FILES)
	@printf "LD      $@\n"
	@$(CC) $(CCFLAGS) -g -o $@ $^

$(EXEC)_static: $(OBJ_FILES)
	@printf "LD      $@\n"
	@$(CC) $(CCFLAGS) -static -g -o $@ $^

src/%.o: src/%.c src/%.h
	@printf "CC      $@\n"
	@$(CC) $(CCFLAGS) -c -g -o $@ $<

src/%.o: src/%.c
	@printf "CC      $@\n"
	@$(CC) $(CCFLAGS) -c -g -o $@ $<
