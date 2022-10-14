@all: APAL/Makefile ROPR/Makefile BIOINF/Makefile
	make -C APAL
	make -C BIOINF
	make -C ROPR

APAL/Makefile:
	cp skel/Makefile APAL/Makefile

BIOINF/Makefile:
	cp skel/Makefile BIOINF/Makefile

ROPR/Makefile:
	cp skel/Makefile ROPR/Makefile

clean:
	./clean.sh

depclean:
	./depclean.sh

host:
	static-server -p 8080

async-host:
	static-server -p 8080 > /dev/null &
