from composable import pipeable
from glob import glob as base_glob
from inspect import getdoc

@pipeable
def glob(pathname,
         *,
         root_dir=None,
         dir_fd=None,
         recursive=False,
         include_hidden=False,
        ):
    getdoc(base_glob)
    return base_glob(pathname=pathname,
                     root_dir=root_dir,
                     dir_fd=dir_fd,
                     recursive=recursive,
                     include_hidden=include_hidden,
                    )
    