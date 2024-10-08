@all: ADS/Makefile REV/Makefile IR/Makefile CC/Makefile #TELE/Makefile ARCH/Makefile SCMT/Makefile MCOR/Makefile TCOM/Makefile APAL/Makefile BIOINF/Makefile ROPR/Makefile ROPR/assignments/Makefile APS/Makefile SAF/Makefile
	# make -C APAL
	# make -C BIOINF
	# make -C ROPR
	# make -C ROPR/assignments
	# make -C APS
	# make -C SAF
	# make -C MCOR
	# make -C TCOM
	# make -C TELE
	# make -C ARCH
	# make -C SCMT
	make -C ADS
	make -C REV
	make -C IR
	make -C CC

APAL/Makefile: skel/Makefile
	cp skel/Makefile APAL/Makefile

BIOINF/Makefile: skel/Makefile
	cp skel/Makefile BIOINF/Makefile

TCOM/Makefile: skel/Makefile
	cp skel/Makefile TCOM/Makefile

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

TELE/Makefile: skel/Makefile
	cp skel/Makefile TELE/Makefile

ARCH/Makefile: skel/Makefile
	cp skel/Makefile ARCH/Makefile

SCMT/Makefile: skel/Makefile
	cp skel/Makefile SCMT/Makefile

ADS/Makefile: skel/Makefile
	cp skel/Makefile ADS/Makefile

REV/Makefile: skel/Makefile
	cp skel/Makefile REV/Makefile

IR/Makefile: skel/Makefile
	cp skel/Makefile IR/Makefile

CC/Makefile: skel/Makefile
	cp skel/Makefile CC/Makefile

clean:
	./clean.sh

depclean:
	./depclean.sh

start-host:
	./server.sh start

stop-host:
	./server.sh stop
