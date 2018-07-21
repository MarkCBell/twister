@OS = $(shell echo %OS%)

ifeq ($(OS),Windows_NT)
	OUTPUT = twister.exe
	OS_ENVIRONMENT = 0
else
	OUTPUT = twister.out
	OS_ENVIRONMENT = 1
endif

CC = g++
MAIN = ./twister/kernel/*.cpp
HEAD = ./twister/kernel/*.h
CFLAGS = -D OS_ENVIRONMENT=$(OS_ENVIRONMENT) -W -Wall

all : $(MAIN)
	$(CC) -o $(OUTPUT) $(MAIN) $(CFLAGS)

.PHONY : all
