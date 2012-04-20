SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build
MANPAGE_URL   = "http://git.mplayer2.org/uau/mplayer2.git/plain/DOCS/man/en/"
			    "mplayer.rst?h=man"
# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: server website update-man clean help
.DEFAULT_GOAL := website

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  server      to start the development webserver"
	@echo "  website     to make the website"
	@echo "  update-man  to update the man from mplayer2's git repository"
	@echo "  clean       to clean the website build product"
	@echo "  help        to show this help message"

server:
	@echo "Starting webserver..."
	cd build/website && python -m SimpleHTTPServer

clean:
	-rm -rf $(BUILDDIR)/*

update-man:
	wget -O source/manpage/man.rst $(MANPAGE_URL)

website:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/website
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."
