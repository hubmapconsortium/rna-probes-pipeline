#!/usr/bin/env pypy3
from argparse import ArgumentParser
from pathlib import Path
from typing import Iterable

import manhole

import correct_visium_barcodes
from common import ADJ_OUTPUT_DIR, Assay

adj_funcs = {
    Assay.VISIUM_FFPE: correct_visium_barcodes.main,
}


def main(assay: Assay, input_dirs: Iterable[Path]):
    ADJ_OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    if assay in adj_funcs:
        adj_funcs[assay](input_dirs, output_dir=ADJ_OUTPUT_DIR)
    else:
        print("No barcode adjustment to perform for assay", assay)


if __name__ == "__main__":
    manhole.install(activate_on="USR1")

    p = ArgumentParser()
    p.add_argument("assay", choices=list(Assay), type=Assay)
    p.add_argument("directory", type=Path, nargs="+")
    args = p.parse_args()

    main(args.assay, args.directory)
