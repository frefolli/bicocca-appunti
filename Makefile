@all: APAL/Makefile ROPR/Makefile BIOINF/Makefile ROPR/assignments/Makefile
	make -C APAL
	make -C BIOINF
	make -C ROPR
	make -C ROPR/assignments

APAL/Makefile: skel/Makefile
	cp skel/Makefile APAL/Makefile

BIOINF/Makefile: skel/Makefile
	cp skel/Makefile BIOINF/Makefile

ROPR/Makefile: skel/Makefile
	cp skel/Makefile ROPR/Makefile

ROPR/assignments/Makefile: skel/Makefile2
	cp skel/Makefile2 ROPR/assignments/Makefile

clean:
	./clean.sh

depclean:
	./depclean.sh

host:
	static-server -p 8080

async-host:
	static-server -p 8080 > /dev/null &
