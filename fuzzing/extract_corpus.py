import json
import itertools
import pathlib

def extract_blobs(filename):
    with open(filename) as fd:
        data = json.load(fd)

    return (bytes.fromhex(tc["blob"]) for tc in data)


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "files", metavar="FILE", nargs="+",
        help="JSON test file to parse"
    )

    args = parser.parse_args()
    blobs = set(itertools.chain.from_iterable(
        extract_blobs(filename) for filename in args.files
    ))

    testcase = pathlib.Path("corpus/XXX.raw")
    testcase.parent.mkdir(exist_ok=True)

    for i, blob in enumerate(blobs):
        testcase.with_stem(f"tc{i:03}").write_bytes(blob)
