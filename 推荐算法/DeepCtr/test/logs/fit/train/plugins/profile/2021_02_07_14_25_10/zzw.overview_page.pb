?	?l???}@?l???}@!?l???}@	z???????z???????!z???????"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$?l???}@)\???hk@A9??v??n@YZd;?O??*	     ,?@2S
Iterator::Model::ParallelMap???K7???!D?vMrM@)???K7???1D?vMrM@:Preprocessing2n
7Iterator::Model::ParallelMap::Zip[0]::FlatMap::Prefetch?????K??!??G?*@)?????K??1??G?*@:Preprocessing2F
Iterator::Model㥛? ???!????Q@)??S㥛??1?G݊?'@:Preprocessing2s
<Iterator::Model::ParallelMap::Zip[0]::FlatMap::Prefetch::Map??Q???!O?m??Z(@)??~j?t??1?[q?wo@:Preprocessing2?
JIterator::Model::ParallelMap::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeatbX9?ȶ?!??ip?E@)X9??v???1D?vM@:Preprocessing2?
QIterator::Model::ParallelMap::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeat::Range???S㥛?!?#?n????)???S㥛?1?#?n????:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate????????!?? 2???)????????1?? 2???:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMapX9??v???!D?vM@)?~j?t???1?X>b?V??:Preprocessing2X
!Iterator::Model::ParallelMap::ZipˡE?????!.A?~?4@){?G?z??1??3?????:Preprocessing2j
3Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat????Mb`?!??)?????)????Mb`?1??)?????:Preprocessing2`
MIterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice:Preprocessing2_
LIterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate[1]::FromTensor:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 0.2% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*high2B47.1 % of the total step time sampled is spent on All Others time.#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	)\???hk@)\???hk@!)\???hk@      ??!       "      ??!       *      ??!       2	9??v??n@9??v??n@!9??v??n@:      ??!       B      ??!       J	Zd;?O??Zd;?O??!Zd;?O??R      ??!       Z	Zd;?O??Zd;?O??!Zd;?O??JCPU_ONLY2black"?
device?Your program is NOT input-bound because only 0.2% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2?
=type.googleapis.com/tensorflow.profiler.GenericRecommendationN
nohigh"B47.1 % of the total step time sampled is spent on All Others time.:
Refer to the TF2 Profiler FAQ2"CPU: 