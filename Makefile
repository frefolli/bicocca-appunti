@all: LIT/Makefile SDL/Makefile ADS/Makefile REV/Makefile IR/Makefile CC/Makefile INFO/Makefile TELE/Makefile ARCH/Makefile SCMT/Makefile MCOR/Makefile TCOM/Makefile APAL/Makefile BIOINF/Makefile ROPR/Makefile ROPR/assignments/Makefile APS/Makefile SAF/Makefile
	make -C APAL
	make -C BIOINF
	make -C ROPR
	make -C ROPR/assignments
	make -C APS
	make -C SAF
	make -C MCOR
	make -C TCOM
	make -C TELE
	make -C ARCH
	make -C SCMT
	make -C INFO
	make -C ADS
	make -C REV
	make -C IR
	make -C CC
	make -C LIT
	make -C SDL

%/Makefile: skel/Makefile
	cp skel/Makefile %/Makefile

clean:
	./clean.sh

depclean:
	./depclean.sh

start-host:
	./server.sh start

stop-host:
	./server.sh stop
