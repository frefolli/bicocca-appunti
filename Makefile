@all:
	make -C APAL
	make -C BIOINF
	make -C ROPR

clean:
	./clean.sh

host:
	static-server -p 8080
