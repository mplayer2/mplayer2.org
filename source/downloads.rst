Downloads
=========

.. warning::
    The mplayer2 team doesn't provide official binaries of the software.
    We recommend you to *build it yourself* from the current git HEAD or
    download one of the unofficial binaries.


Source code
-----------

There are two main alternatives to build the player. First is to use
system libraries for all dependencies. Since the FFmpeg/Libav versions
available on many Linux distributions are old, in many cases this will
either not produce an optimal result or will require extra manual work
to update the libraries first.

For this reason there exists a separate build helper repository that
first builds an up-to-date version of Libav libraries and libass and
then builds the player statically linked against those.

.. note::
    See :ref:`this FAQ entry <faq-1>` about interaction with
    existing MPlayer installations.

.. csv-table::
    :header: "Git repository", "Description"
    :widths: 20, 80

    "`mplayer2.git <http://git.mplayer2.org/mplayer2/>`_", "Player only"
    "`mplayer2-build.git <http://git.mplayer2.org/mplayer2-build/>`_", "Helper that automatically builds new Libav and some other dependencies too.
    **Recommended for most users.**"


Unofficial binaries
-------------------

These binaries are provided by third parties. Use at your own risk!

.. csv-table::
    :header: "Platform", ""
    :widths: 10, 90

    "Windows", "`binaries by lachs0r <http://mplayer2.srsfckn.biz/>`_ (may contain untested extra functionality)"
    "Mac OS X", "`binaries by pigoz <http://code.google.com/p/mplayerosx-builds/>`_ (may contain untested extra functionality)"
    "Linux", "Provided through each distribution’s package repositories."

.. warning::
    Packages provided by some Linux distributions are really old (2.0
    release). It is not recommended to use such an old version of
    mplayer2, and you should notify the distro maintainers to help
    getting this resolved.


Previous releases
-----------------

You can find an archive of our releases via `HTTP <http://ftp.mplayer2.org/pub
/archive/release/>`_ or `FTP <ftp://ftp.mplayer2.org/pub/archive/release/>`_.
