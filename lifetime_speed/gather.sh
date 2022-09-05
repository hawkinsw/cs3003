#!/bin/env bash

echo "empty, local, static"
for i in `seq 100`; do
  ./build/LifetimeSpeed
done
