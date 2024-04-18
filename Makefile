SDIR = ./src
CPC=g++
CC=gcc

BDIR = ./build
PDIR = ./psrc
TDIR = ./test
NTHREADS = 2
NITERS = 20000

CFLAGS= -Wall -ggdb -I$(SDIR) -fPIC 
CPFLAGS= -Wall -ggdb -I$(SDIR) -fPIC 

DEPS = 
PSRCS = $(PDIR)/cimpl.pyx $(PDIR)/setup.py
TOBJ = $(BDIR)/test_impl.o
MOBJ = $(BDIR)/main_exe.o

$(BDIR)/%.o: $(SDIR)/%.c $(DEPS)
	$(MKDIR_P) $(dir $@)
	$(CC) -c -o $@ $< $(CFLAGS)

$(BDIR)/%.o: $(TDIR)/%.cpp $(DEPS)
	$(MKDIR_P) $(dir $@)
	$(CPC) -c -o $@ $< $(CPFLAGS)

$(BDIR)/test_executable: $(TOBJ)
	$(CPC) $(TOBJ) -g -pthread $(GSL_LIBS) -lgtest_main -lgtest -o $(BDIR)/test_executable

$(BDIR)/main_exe: $(MOBJ)
	$(CC) $(MOBJ) $(GSL_LIBS) -o $(BDIR)/main_exe

test: $(BDIR)/test_executable
	$(BDIR)/test_executable --gtest_print_time=1

vtest: $(BDIR)/test_executable
	valgrind --leak-check=full --error-exitcode=1 $(BDIR)/test_executable --gtest_print_time=1

main: $(BDIR)/main_exe
	$(BDIR)/main_exe

.PHONY: clean

clean:
	rm -rf $(BDIR) *~ core $(SDIR)/*~ *.so psrc/cimpl.c $(PDIR)/*~ $(PDIR)/static/*~ $(PDIR)/templates/*~

submit: 
	git commit -m "final submission" -a
	git push

MKDIR_P ?= mkdir -p
