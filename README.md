## ZipSelected

Plugin for [fman.io](https://fman.io) to zip files that have been selected in fman.

Install by uploading "ZipSelected" to your [data directory](https://fman.io/docs/customizing-fman)`/Plugins`.

### Usage

Select one video file and press **Shift+z** (I'm using my Vim Keymappings)

**Warning**: Currently it runs in the same process/thread so be aware that running properties on a large dir will cause the UI to hang while calculating size

### Features

 - Zips all selected files into a zipfile based on the current directory name.