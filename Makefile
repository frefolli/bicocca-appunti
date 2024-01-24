@all: APAL/Makefile MCOR/Makefile BIOINF/Makefile ROPR/Makefile ROPR/assignments/Makefile APS/Makefile SAF/Makefile
	make -C APAL
	make -C BIOINF
	make -C MCOR
	make -C ROPR
	make -C ROPR/assignments
	make -C APS
	make -C SAF
	make -C TCOM

APAL/Makefile: skel/Makefile
	cp skel/Makefile APAL/Makefile

BIOINF/Makefile: skel/Makefile
	cp skel/Makefile BIOINF/Makefile

MCOR/Makefile: skel/Makefile
	cp skel/Makefile MCOR/Makefile

ROPR/Makefile: skel/Makefile
	cp skel/Makefile ROPR/Makefile

ROPR/assignments/Makefile: skel/Makefile2
	cp skel/Makefile2 ROPR/assignments/Makefile

APS/Makefile: skel/Makefile
	cp skel/Makefile APS/Makefile

SAF/Makefile: skel/Makefile
	cp skel/Makefile SAF/Makefile

clean:
	./clean.sh

depclean:
	./depclean.sh

start-host:
	./server.sh start

stop-host:
	./server.sh stop
