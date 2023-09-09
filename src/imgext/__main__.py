""" ImgExt main """

import os

from tkinter.filedialog import askopenfilename
from imgext import extract_img


FILE_TYPE_ALLOWED = (
        ('PDF file', (
            '*.pdf'
            )
        ),
        # ('All files', '*.*')
    )


def main() -> int:
    file_path = ''
    if len(os.sys.argv) < 2:
        file_path = askopenfilename(
            filetypes=FILE_TYPE_ALLOWED
        )
    else:
        file_path = os.sys.argv[1]

    dir_path, _ = os.path.split(file_path)
    img_files = extract_img(file_path, dir_path)
    print("\nimage files list:")
    for file_path in img_files:
        print(f"  * saved at {file_path}", flush=True)

    return 0


if __name__ == '__main__':
    try:
        os.sys.exit(main())
    except KeyboardInterrupt:
        print("\033[91mCanceled by user.\033[0m")
        os.sys.exit(125) 
