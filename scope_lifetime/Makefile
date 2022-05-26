all: lifetime scope_ne_lifetime

lifetime: lifetime.cpp Makefile
	clang++ -O0 -g lifetime.cpp -o lifetime -Wno-return-stack-address
scope_ne_lifetime: scope_ne_lifetime.cpp Makefile
	clang++ -O0 -g scope_ne_lifetime.cpp -o scope_ne_lifetime

clean:
	rm -f core lifetime a.out scope_ne_lifetime
