#!/bin/bash

for i in {0..9} 
do
    echo "manifest {$i}";
    chunkflow aggregate-skeleton-fragments --fragments-path "gs://jwu-zfish/v1/20200406/skeleton-fragments" --output-path "gs://jwu-zfish/v1/20200406/skeleton" -p $i
done
