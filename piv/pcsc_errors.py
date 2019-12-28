#!/usr/bin/env python3

with open("pcsc_errors") as f:
    data = f.read()

name = ""
val = 0
desc = ""

with open("pcsc_errors.go", 'w+') as f:
    print("""package piv

// https://golang.org/s/generatedcode

// Code generated by errors.py DO NOT EDIT.

var pcscErrMsgs = map[int64]string{""", file=f)
    for line in data.split("\n"):
        if not line.strip():
            continue
        if line.startswith("SC"):
            name = line.split()[0][len("SCARD_E_"):]
            name = "".join([s[0] + s[1:].lower() for s in name.split("_")])
            name = "rc" + name
            val = line.split()[1]
        else:
            desc = line[:-1]
            desc = desc[0].lower() + desc[1:]
            desc = desc.replace("\"", "\\\"")
            print("\t%s: \"%s\"," % (val, desc), file=f)
    print("}", file=f)
