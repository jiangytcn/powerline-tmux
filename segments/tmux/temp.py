# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

import subprocess
from subprocess import PIPE, STDOUT

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info, requires_filesystem_watcher


@requires_filesystem_watcher
@requires_segment_info
class TempSegment(Segment):

    divider_highlight_group = None

    def __call__(self, pl, segment_info, create_watcher):
        temp_output = subprocess.run(['~/.tmux/plugins/tmux-cpu/scripts/cpu_temp.sh'],
                                     stdout=PIPE, stderr=STDOUT, check=True)
        cpu_temp = _canonical_temp(temp_output.stdout)
        return [{
          'contents': f'CPU: {cpu_temp}',
          'highlight_groups': ['information:regular'],
          }]


def _canonical_temp(temperature):
    """return canonical temperature.

    :temperature: temperature in bytes from  external utility
    :returns: TODO

    """
    return temperature.decode('utf-8')


holistic = with_docstring(TempSegment(), '''Return a tmux temperature segment.''')
