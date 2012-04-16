.. _differences:

Differences from `MPlayer <http://mplayerhq.hu>`_ to mplayer2
=============================================================

Improvements over MPlayer
-------------------------


Better pause handling
~~~~~~~~~~~~~~~~~~~~~

In MPlayer, executing any commands forced the player to unpause. This is
no longer the case; in mplayer2 you can change settings, seek, or
execute other commands while paused.


Better Matroska support
~~~~~~~~~~~~~~~~~~~~~~~

mplayer2 has improved support for Matroska files, including support for
ordered chapters and editions.


Much better support for VDPAU functionality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Removed limitations that prevented switching frames more than once per
  monitor refresh. With MPlayer2 you can play high-FPS content or use
  fast forward on a 60 Hz monitor without breaking playback.
* Added support for the frame timing functionality of VDPAU.
* Improved performance by better buffer handling and smarter subtitle
  texture uploads (both VDPAU hardware decoding and displaying software
  decoded video with VDPAU perform better).
* Added logic to reduce frame timing jitter in some situations.
* Handle frames added by deinterlacing properly.
* Several bugfixes.
* Various minor improvements (studio level output support, set default
  deinterlace mode, ...)


Support for precise seeks
~~~~~~~~~~~~~~~~~~~~~~~~~

It’s now possible to seek to any frame in the video; seeks are no
longer necessarily limited to keyframes.


Support for gettext-based translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The message translation support in MPlayer was basically useless for
binary Linux distributions, as the message language was hardcoded at
compile time and supporting several languages would have required a
separate program binary for every one. Runtime-switchable translations
with gettext are now supported.


No dependence on embedded FFmpeg tree or internal FFmpeg symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MPlayer required an embedded copy of FFmpeg to compile. This caused a
maintenance burden as changes in FFmpeg fairly often broke the
compilation of MPlayer. While it could link against shared FFmpeg
libraries it would still use some code from the embedded tree instead,
and also depended on internal FFmpeg symbols that are not part of the
public API, thus making any dynamic-linked binaries liable to break when
FFmpeg libraries are updated. MPlayer2 does not depend on embedded
FFmpeg library copies and uses FFmpeg only through its public API. This
eases maintenance and makes dynamic-linked binaries safe.


Miscellaneous
~~~~~~~~~~~~~

* Lots of bugfixes
* Improvements in audio/video sync handling
* Cleaned up and improved various terminal output messages
* Support for gapless playback of audio files (option
  ``--gapless-audio``)
* Better responsiveness in certain cases where MPlayer had significant
  latency before reading or completing commands
* Support modifier keys in command bindinds (currently X11-based input
  only)
* Keep fullscreen state by default when switching between files
* OSS4 volume control
* Various stuff not listed here...


Dropped features
----------------


MEncoder is no longer available
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The MEncoder codebase was thoroughly rotten and has been deleted. A
different solution to provide some encoding functionality will be added
in a future version.


Internal GUI has been removed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The bad internal GUI (gmplayer) has been deleted. Future work will
concentrate on improving the interface for external GUI implementations
instead.


Some embedded library copies have been removed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* FFmpeg libraries - already explained above; mostly no negative effects
  but some video filters which depended on internal FFmpeg code are not
  available (vf_fspp, vf_mcdeint, vf_qp, vf_spp).
* libmpeg2 - libmpeg2 support has been dropped completely. The
  libavcodec mpeg2 decoder should work for all normal uses.
* vidix - support for VIDIX video drivers has been dropped (it had
  little maintenance and didn't work with any modern graphics card).
* tremor - embedded tremor library is no longer included.
* libdvdnav, libdvdread and libdvdcss - these libraries are no longer
  included with the player. However in-tree compilation is still
  supported too if you add them in the player directory manually.


Other differences that may surprise MPlayer users
-------------------------------------------------


Subtitle rendering uses libass by default
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using libass to render subtitles gives better font rendering and styling
support, but on the other hand some subtitle options may not work as
before or at all. The video filter needed to draw libass subtitles with
video output drivers that do not directly support rendering them may
also cause problems in some rare cases (videos with unusual
colorspaces). If you encounter problems you can use the "-noass" option
to use the old subtitle rendering functionality.


libavformat demuxers are used for more file formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

libavformat demuxers are now the default for some file formats that used
internal demuxer versions by default in MPlayer (most notably AVI). This
can cause some behavior differences as the demuxers have slightly
different feature sets - sometimes better, but sometimes also worse.


The ``--fixed-vo`` option is enabled by default
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This leads to some behavior differences when playing multiple files.