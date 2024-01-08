# -*- coding: utf-8 -*-


def parse_failure_result(result: list):
    with open('failure_result.log', mode='w', encoding='utf-8') as f:
        f.writelines(result)
    filenameSet = set()
    for r in result:
        t_seg = r.split("]")[0]
        fname = t_seg[1:].split(".assert")[0]
        filenameSet.add(fname)

    print(len(filenameSet))
    for f in filenameSet:
        print(f)
