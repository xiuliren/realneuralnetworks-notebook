#!/bin/bash
export PROCESS_NUM=1


#seq "$PROCESS_NUM" | parallel -j "$PROCESS_NUM" --delay 120 --ungroup echo Starting worker {}\; \

chunkflow --mip 3 fetch-task -q zfish -v 600 \
    cutout -v gs://jwu-zfish/v1/20200406 --fill-missing --expand-margin-size 1 1 1 \
    mask-out-objects --selected-obj-ids "gs://jwu-zfish/v1/20200406/all_neuron_ids.json" --dust-size-threshold 100\
    skeletonize --voxel-size 45 40 40 --output-path gs://jwu-zfish/v1/20200406/skeleton-fragments \
    delete-task-in-queue
