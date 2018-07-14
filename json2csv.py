# _*_ coding:utf-8 _*_
import json
import sys
import os

def process(inpath, outpath):
    dir_name = inpath
    files = os.listdir(dir_name)

    out_file = outpath

    with open(out_file, "w", encoding='UTF-8') as fout:
        for f in files:
            data = open(dir_name + "/" + f, "r", encoding='UTF-8').read()

            text = json.loads(data)

            items = text["items"]

            for it in items:
                if it['discarded'] == True:
                    fout.write(it['e1'] + "\t" + it['e2'] + "\tunknown\t" + it['context'] +"\n")
                else:
                    relation = ""
                    for rel in it['rels']:
                        if relation == "":
                            relation = rel
                        else:
                            relation = relation + "," + rel

                    fout.write(it['e1'] + "\t" + it['e2'] + "\t" + relation + "\t" + it['context'] + "\n")

if __name__ == '__main__':
    process(sys.argv[1], sys.argv[2])


