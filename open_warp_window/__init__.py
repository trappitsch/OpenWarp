import subprocess

from fman import DirectoryPaneCommand
from fman.url import as_human_readable


class OpenWarpWindow(DirectoryPaneCommand):
    def __call__(self):
        current_dir = as_human_readable(self.pane.get_path())
        uri = f"warp://action/new_window?path={current_dir}"
        subprocess.run(["xdg-open", uri])
