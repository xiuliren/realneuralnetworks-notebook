## Produce skeletonization tasks 

```
julia produce_skeleton_tasks.jl -j ~/workspace/zfish_analysis/01_data/20190415/01_consensus/consensus.valid.json -q skeleton -s 76202 
```
The 76202 neuron is the huge mauthner neuron.

## docker command
```
sudo docker run -it -v /secrets:/secrets -e AWS_ACCESS_KEY_ID=AKI
XXXXXXXXXXX -e AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXX gcr.io/
neuromancer-seung-import/chunkflow:realneuralnetworks julia -p auto skeletonize.jl -l gs://
neuroglancer/zfish_v1/consensus-20171130 -q skeleton
```

