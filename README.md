# bulkRenamePythonTool
Ever wished you could bulk-rename a list of files with a decent text editor like notepad++?

Place the two python files in the same directory as your list of files.

The first python script 'makerename.py' creates a file called rename.txt in the same folder which you can edit however you like.

The format of rename.txt is

`[existing file name]   :[your new file name]`

You specify your change by leaving the existihg file name column as-is, and editing the filename after the colon character. If you dont want to change a file's name, you can simply delete the line in the text file or leave it as is.

The second script 'rename.py' implements your edits on the filesystem.

Warnings:
No checking is done to see if
-- A rename.txt file already exists; it will simply be overwritten every time maerename.py is run.
-- You have specified duplicate file names
-- If any of the files are in use by other software
-- If you use characters that are not permitted.
