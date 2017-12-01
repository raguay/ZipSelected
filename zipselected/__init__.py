from fman import DirectoryPaneCommand, show_alert
import os
import zipfile
from fman.url import as_human_readable
from fman.url import as_url


def zipdir(rootZip, path, ziph):
    numf = 0
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),os.path.join(rootZip,os.path.basename(file)))
            numf += 1
        for dir in dirs:
            numf += zipdir(os.path.join(rootZip,os.path.basename(dir)),os.path.join(root,dir),ziph)
    return numf

class ZipSelected(DirectoryPaneCommand):
    def __call__(self):
        selected_files = self.pane.get_selected_files()
        output = ""
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            dirPath = os.path.dirname(as_human_readable(selected_files[0]))
            dirName = os.path.basename(dirPath)
            zipName = os.path.join(dirPath, dirName + ".zip")
            numf = 0
            zipf = zipfile.ZipFile(zipName, 'w')
            for file in selected_files:
                file = as_human_readable(file)
                if os.path.isdir(file):
                    numf += zipdir(os.path.join(dirName, os.path.basename(file)),file,zipf)
                else:
                    zipf.write(file, os.path.join(dirName, os.path.basename(file)))
                    numf += 1
            output += str(numf) + " files were zipped!"
            zipf.close()
        else:
            output += "No files or directories selected"

        show_alert(output)
