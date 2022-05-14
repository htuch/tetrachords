all:
	aspell -p "${PWD}"/.aspell.pws -c README.md
	pytype --disable=pyi-error scales/*.py
	yapf -i scales/*.py
	python3 scales/diagrams.py
