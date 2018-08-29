#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from solc import compile_source, compile_files, link_code

def compile_multiminttoken():
    with open("./MultiMintToken.sol", "r") as fo:
        content = fo.read()
        result = compile_source(content)["<stdin>:MultiMintToken"]
        with open("MultiMintToken.cpl", "w+") as wfo:
            wfo.write(json.dumps(result, indent=2))
        with open("MultiMintToken.json", "w+") as wfo:
            wfo.write(json.dumps(result["abi"], indent=2))
        with open("MultiMintToken.bin", "w+") as wfo:
            wfo.write(result["bin"])

def compile_testtoken():
    # wiVth open("./TestToken.sol", "r") as fo:
    #     content = fo.read()
    #     print(len(content))
    #     result = compile_source(content)["<stdin>:TestToken"]
    #     with open("TestToken.cpl", "w+") as wfo:
    #         wfo.write(json.dumps(result, indent=2))
    #     with open("TestToken.json", "w+") as wfo:
    #         wfo.write(json.dumps(result["abi"], indent=2))
    #     with open("TestToken.bin", "w+") as wfo:
    #         wfo.write(result["bin"])
    result = compile_files(["TestToken.sol", ])
    result = result["TestToken.sol:TestToken"]
    with open("TestToken.cpl", "w+") as wfo:
        wfo.write(json.dumps(result, indent=2))
    with open("TestToken.json", "w+") as wfo:
        wfo.write(json.dumps(result["abi"], indent=2))
    with open("TestToken.bin", "w+") as wfo:
        wfo.write(result["bin"])

def compile_gatewayvote():
    result = compile_files(["GatewayVote.sol", ])
    result = result["GatewayVote.sol:GatewayVote"]
    with open("GatewayVote.cpl", "w+") as wfo:
        wfo.write(json.dumps(result, indent=2))
    with open("GatewayVote.json", "w+") as wfo:
        wfo.write(json.dumps(result["abi"], indent=2))
    with open("GatewayVote.bin", "w+") as wfo:
        wfo.write(result["bin"])

def compile_wbchtoken():
    result = compile_files(["WBCHToken.sol", ])
    result = result["WBCHToken.sol:WBCHToken"]
    with open("WBCHToken.cpl", "w+") as wfo:
        wfo.write(json.dumps(result, indent=2))
    with open("WBCHToken.json", "w+") as wfo:
        wfo.write(json.dumps(result["abi"], indent=2))
    with open("WBCHToken.bin", "w+") as wfo:
        wfo.write(result["bin"])

if __name__ == '__main__':
    compile_wbchtoken()
    # compile_testtoken()
    compile_gatewayvote()
    # compile_multiminttoken()


