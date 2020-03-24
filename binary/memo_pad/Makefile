.PHONY: all
all: build
.PHONY: build
build: memo_pad

memo_pad: memo_pad.c
	gcc memo_pad.c -o memo_pad -fno-stack-protector -fno-toplevel-reorder  -fno-zero-initialized-in-bss -no-pie
