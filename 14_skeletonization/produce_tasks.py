#!/usr/bin/env python


from chunkflow.lib.aws.sqs_queue import SQSQueue

import json
import os

queue = SQSQueue('skeleton')

DATASET_DIR = os.path.expanduser('../../01_data/')

# exclude some extra neurons, such as mauthner cell 76202
EXCEPTIONAL_NEURON_IDS = set([76202,])

with open(os.path.join(DATASET_DIR, 'all_neuron_ids.json')) as f:
    neuron_ids = json.load(f)

neuron_ids = set(neuron_ids).difference( EXCEPTIONAL_NEURON_IDS )
neuron_ids = [str(nid) for nid in neuron_ids]

queue.send_message_list(neuron_ids)
