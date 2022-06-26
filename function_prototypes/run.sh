#!/bin/bash

echo "(UB) No optimizations:"
./build/PrototypeUB
echo "(UB) Optimizations:"
./build/PrototypeUBOpt
echo "No optimizations:"
./build/Prototype
echo "Optimizations:"
./build/PrototypeOpt
