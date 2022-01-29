#!/bin/bash

# the chunks need to have one overlap, so the chunksize is 
chunkflow generate-tasks -l gs://jwu-zfish/v1/20200406 -m 3 -c 200 2000 2000 -q zfish
