@all:
	make -C APAL
	make -C BIOINF
	make -C ROPR

clean:
	make -C APAL clean
	make -C BIOINF clean
	make -C ROPR clean

host:
	static-server -p 8080
