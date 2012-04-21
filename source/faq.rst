FAQ
===

.. _faq-1:

#. **I've used MPlayer. Can I easily switch to mplayer2?**

   In most cases yes. Most of the commandline/configuration options,
   keyboard commands etc from MPlayer are still available and work the
   same way. For some information about the differences see
   :ref:`this comparison <differences>`.

   Currently mplayer2 uses the same binary and directory names as
   MPlayer. This makes it easy for users to switch to mplayer2; it can
   be treated as another new MPlayer version, though one that brings
   more new stuff than usual (no need to move configuration,
   reconfigure GUIs to use a different binary name etc). On the other
   hand this means that installing mplayer2 to the default location
   will overwrite an existing MPlayer installation there, and vice
   versa. If you for some reason want to have both installed
   simultaneously, it's possible to install to different directories or
   run one or both binaries without installing (both are able to run
   without using any external installed data files). The names used may
   change in a future version.

#. **Can I use GUIs originally written for MPlayer with mplayer2?**

   Yes. The protocol is compatible and most of the functionality
   differences do not cause problems for the GUIs. MPlayer GUIs may
   have workarounds for certain MPlayer misbehavior which can lead to
   trouble when it has been fixed in mplayer2.

#. **Why was MEncoder removed? Some people were still using it.**

   The MEncoder codebase was in very bad shape. The code quality and
   architecture was bad in general, and there were lots of known bugs
   that caused failures or more or less subtly corrupt output in a
   variety of circumstances. Fixing it would have required a lot of
   effort, and nobody was working on it. MEncoder duplicated various
   parts of the playback functionality and did that badly; adding some
   encoding support on top of the player side is overall less work than
   fixing all the flaws in MEncoder (see next question).

   Letting MEncoder stay around in its semi-broken state was less of an
   issue in MPlayer as it could mostly be ignored; changes in mplayer2
   meant that keeping MEncoder compiling at all would have required
   active work, and this wasn't really worth it considering that
   MEncoder development was a dead end.

#. **I was using MEncoder before. What can I do now?**

   There's a development branch which adds some encoding functionality
   to mplayer2. The functionality will likely be merged to the main
   repository before releasing version 2.1. You can see the current
   status `here <http://git.mplayer2.org/mplayer2/?h=tmp_encode>`_.
   This is not meant to be an exact duplicate of MEncoder functionality
   with bugs fixed, but it should be suitable for some of the same uses
   (and some things that were not possible with MEncoder).

   Other alternatives are programs like libav/FFmpeg and
   format-specific muxing applications (typically a lot more reliable
   than MEncoder in cases where they can be used). And it's still
   possible to build MEncoder from the MPlayer tree if you really need
   some specific functionality which isn't available elsewhere.
