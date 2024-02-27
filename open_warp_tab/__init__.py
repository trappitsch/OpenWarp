import subprocess

from fman import DirectoryPaneCommand
from fman.url import as_human_readable


class OpenWarpTab(DirectoryPaneCommand):
    def __call__(self):
        current_dir = as_human_readable(self.pane.get_path())
        uri = f"warp://action/new_tab?path={current_dir}"
        subprocess.run(["xdg-open", uri])
