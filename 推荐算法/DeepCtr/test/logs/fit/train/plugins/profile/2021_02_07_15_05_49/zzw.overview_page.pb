?	??(\??}@??(\??}@!??(\??}@	@?o??h??@?o??h??!@?o??h??"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$??(\??}@?K7?ADy@A?t?NR@Y????????*	     \?@2S
Iterator::Model::ParallelMap??n????!???'e_J@)??n????1???'e_J@:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMapV-???!???TW?>@)-??????1??P???/@:Preprocessing2n
7Iterator::Model::ParallelMap::Zip[0]::FlatMap::Prefetch{?G?z??!Я???,@){?G?z??1Я???,@:Preprocessing2F
Iterator::ModelJ+???!<2Jrp?M@)㥛? ???1??iSZH@:Preprocessing2s
<Iterator::Model::ParallelMap::Zip[0]::FlatMap::Prefetch::Map??MbX??!??Q`?!@)L7?A`???1r??+?@:Preprocessing2?
JIterator::Model::ParallelMap::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeatL7?A`???!r??+?@)X9??v???1u??}R@:Preprocessing2X
!Iterator::Model::ParallelMap::ZipV-???!?i???@)9??v????1???̸??:Preprocessing2?
QIterator::Model::ParallelMap::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeat::Range????Mb`?!@&6s?
??)????Mb`?1@&6s?
??:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate????Mb`?!@&6s?
??)????Mb`?1@&6s?
??:Preprocessing2?
MIterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice????MbP?!@&6s?
??)????MbP?1@&6s?
??:Preprocessing2_
LIterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate[1]::FromTensor:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 0.2% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*high2B84.5 % of the total step time sampled is spent on All Others time.#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?K7?ADy@?K7?ADy@!?K7?ADy@      ??!       "      ??!       *      ??!       2	?t?NR@?t?NR@!?t?NR@:      ??!       B      ??!       J	????????????????!????????R      ??!       Z	????????????????!????????JCPU_ONLY2black"?
device?Your program is NOT input-bound because only 0.2% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2?
=type.googleapis.com/tensorflow.profiler.GenericRecommendationN
nohigh"B84.5 % of the total step time sampled is spent on All Others time.:
Refer to the TF2 Profiler FAQ2"CPU: 