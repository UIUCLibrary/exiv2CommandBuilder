PYTHON      ?= python
PIP         ?= pip
TOX         ?= tox
current_dir = $(shell pwd)

all:
	$(PYTHON) setup.py build

clean:
	@$(PYTHON) setup.py clean

	@if [ -d docs/build ]; then \
	    	echo 'deleting generated documentation'; \
		rm -R docs/build; \
    	fi

	@if [ -d build ]; then \
	    	echo 'deleting build'; \
    		rm -R build; \
    	fi

	@if [ -d dist ]; then \
		echo 'deleting dist'; \
		rm -R dist; \
	fi

	@if [ -d .cache ]; then \
		echo 'deleting cache'; \
		rm -R .cache; \
	fi

	@if [ -d .tox ]; then \
		echo 'deleting tox cache'; \
		rm -R .tox; \
	fi

	@if [ -d .eggs ]; then \
		echo 'deleting .egg cache'; \
		rm -R .eggs; \
	fi

	@if [ -d .cache ]; then \
		rm -R .cache; \
	fi

	@if [ -d exiv2Driver.egg-info ]; then \
		echo 'Deleting exiv2Driver.egg-info.'; \
		rm -R exiv2Driver.egg-info; \
	fi
