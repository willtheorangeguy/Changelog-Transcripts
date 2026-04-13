[0.00 → 3.96] What we are doing and specializing is kind of the model design approach,
[4.14 → 9.54] where you need to select the right model that is optimized both for the data to reach the accuracy
[9.54 → 12.66] and also for the hardware to reach the latency.
[13.20 → 18.24] And by optimizing the model specifically for the inference hardware that you're looking to use,
[18.24 → 24.20] you can get significant boost in the performance compared to having kind of an open source model
[24.20 → 29.32] or off-the-shelf model that you just took from an academic paper or from GitHub or something like that.
[30.00 → 34.56] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[34.92 → 36.98] We love Linde. They keep it fast and simple.
[37.10 → 39.46] Check them out at linode.com slash changelog.
[39.70 → 41.76] Our bandwidth is provided by Vastly.
[42.12 → 45.68] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[45.68 → 47.66] Get a demo at LaunchDarkly.com.
[48.10 → 51.52] This episode is brought to you by our friends at Rudder Stack.
[51.72 → 54.08] And we're calling all data engineers to check out Rudder Stack Cloud
[54.08 → 56.24] and start building smart customer data pipelines.
[56.74 → 59.58] Rudder Stack is warehouse first, no more silos.
[60.00 → 63.46] Rudder Stack builds your customer data lake on your data warehouse, not theirs,
[63.70 → 69.14] enabling all functionality of a CDP with more security and retaining full ownership of your data.
[69.44 → 71.90] It's open source and API first.
[72.20 → 75.68] Rudder Stack can be easily integrated into your existing development processes.
[76.26 → 78.98] And because they're open source, you can see all their code,
[79.22 → 81.62] so you don't have to worry about vendor lock-in or black boxes.
[82.18 → 83.76] And best of all, they have transparent pricing.
[83.94 → 86.20] Stop paying your CDP a premium to store your data.
[86.20 → 91.56] Rudder Stack is free up to 500,000 events and pricing scales transparently from there.
[91.96 → 94.02] Learn more and get started at RudderStack.com.
[94.28 → 96.56] Again, RudderStack.com.
[96.70 → 100.26] That's R-U-D-D-E-R-S-T-A-C-K.com.
[100.26 → 115.08] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[115.38 → 117.14] productive, and accessible to everyone.
[117.48 → 121.54] This is where conversations around AI, machine learning, and data science happen.
[121.80 → 125.30] Join the community and Slack with us around various topics of the show at
[125.30 → 127.92] change-on.com slash community and follow us on Twitter.
[128.04 → 129.66] We're at Practical AI FM.
[135.60 → 138.64] Well, welcome to another episode of Practical AI.
[139.00 → 140.66] This is Daniel Whiten ack.
[140.80 → 143.92] I am a data scientist with SIL International,
[144.22 → 147.02] and I'm joined as always by my co-host, Chris Bronson,
[147.54 → 150.02] who is a tech strategist at Lockheed Martin.
[150.30 → 150.94] How are you doing, Chris?
[151.40 → 152.64] I am doing very well.
[152.64 → 155.26] It's dog days of summer as we record this.
[155.60 → 157.58] And just try not to melt.
[157.82 → 158.36] Yeah, yeah.
[158.42 → 162.40] It's hot like you're sitting right on top of a bunch of GPUs or something.
[163.46 → 164.80] That's exactly right.
[165.24 → 165.42] Yeah.
[166.54 → 171.26] Well, speaking of hardware, today's episode is kind of connected to that.
[171.66 → 174.64] Really excited to have Jonathan German with us,
[174.72 → 178.60] who is CEO and co-founder of the deep learning company, DESI.
[178.98 → 179.66] Welcome, Jonathan.
[180.20 → 180.50] Hi.
[180.50 → 181.82] Thank you for hosting me.
[182.00 → 182.48] How are you?
[182.78 → 183.88] Yeah, doing wonderful.
[183.88 → 192.48] So I know a lot of what your company does is related to productionizing models, optimizing models.
[192.48 → 195.90] There are a bunch of things that you do related to optimizing inference.
[195.90 → 200.10] And I'd love to dive into all of that as time goes on.
[200.18 → 206.34] But maybe let's just start out by talking about why should we care so much about inference?
[206.50 → 210.98] So a lot of effort and I think screen time, if we want to put it that way,
[210.98 → 216.66] in terms of Twitter and other places is put on the training side of things and scaling up training.
[216.66 → 222.78] But why do deep learning and AI practitioners need to be concerned about inference?
[222.78 → 227.06] So actually, the first thing to be concerned with is the training.
[227.26 → 231.42] But after you finish building a model, then you need to deploy it somewhere.
[231.64 → 233.42] It could be in the cloud or in the edge.
[233.56 → 237.90] And when you are going to deploy it and do serving or inference at scale,
[238.44 → 245.06] you must be concerned or think about how this model is going to perform in terms of latency or throughput.
[245.06 → 247.38] What is the operational cost of this model?
[247.84 → 254.44] Or are you actually able to deploy it on the edge device that you want to use in order to serve the inference of that model?
[254.70 → 259.54] And it's kind of the second phase of the development cycle after you reach the accuracy.
[259.54 → 265.88] But you must think about it at the beginning when you choose the model in order to know that you are going to finish the project
[265.88 → 270.22] with a model that meets the SLA of going to production in your environment
[270.22 → 274.72] with your characteristics of performance that you are looking for in production.
[275.06 → 280.68] If you think about it, you'll see that a model is trained once or once in a while.
[280.68 → 287.58] But the inference workload is huge because it's kind of linearly scales with the amount of data in production.
[287.94 → 293.20] So if you think about an organization that, for example, develops a self-driving car,
[293.74 → 297.70] you will think about the number of data scientists that are doing the training work, building the models.
[297.80 → 301.10] Each one of them needs some amount of GPUs in order to do its work.
[301.10 → 307.04] But when you deploy these algorithms, these are deployed among huge amounts of cars.
[307.38 → 314.46] So in order to optimize the performance, you're more concerned about what type of hardware you'll need to fit into the car
[314.46 → 319.80] compared to how many GPUs you'll need to have in the cloud for your data scientists to build those models.
[319.80 → 321.40] So this is kind of the proportions.
[321.88 → 325.28] The training is kind of linearly scaled by the number of data scientists,
[325.72 → 331.12] while the inference is scaled by the amount of data, the scale of the deployment that you're going to use.
[331.62 → 335.48] And you must think about the performance when you want to go to production at scale.
[335.48 → 342.52] Yeah. And as a practitioner, you mentioned thinking about inference up front, maybe even before training,
[342.66 → 346.60] thinking about what models you might even be able to use in production.
[346.80 → 350.86] As you're working with different companies and different teams of data scientists,
[350.86 → 356.32] do you see people running into this challenge a lot where they're really happy with their model that they spent,
[356.50 → 362.18] you know, a lot of time and effort training, and they just are completely blocked in taking the model to production?
[362.18 → 369.30] And how often do you see that? And what are the main reasons like why they're not able to do inference with that model?
[369.42 → 375.22] Is it a latency thing? Is it a memory constraint thing? What are some of the challenges you see?
[375.52 → 383.90] So it is really divided into several problems, but there is a simple principle that you can always take a larger model and get better accuracy.
[384.32 → 387.06] And it's easy to get better accuracy with larger models.
[387.30 → 390.78] But this is only happening if you don't need to think about production.
[390.78 → 395.52] When you think about production, you understand that those models are not production ready, let's say.
[396.04 → 402.66] For example, if you want to deploy them in the edge, you have several constraints like the memory and the latency that you want to run probably in real time
[402.66 → 405.74] or giving some reasonable response time for the model.
[406.04 → 410.18] But in the cloud, you're more concerned about the cloud cost of serving this at scale,
[410.62 → 416.50] the amount of hardware that you will need to orchestrate in order to serve your users or your demand for inference.
[416.50 → 421.52] And this is kind of the things that you need to take into account while you develop your model.
[421.66 → 427.58] Because as I said at the beginning, going larger is easier to get accuracy, but it's not easier to get deployed.
[428.04 → 435.06] So we see companies all the time getting some huge models, trying to fit them into small devices for edge inference.
[435.06 → 441.12] Or companies that just understand that they took the largest model that they can have and get the right accuracy.
[441.12 → 446.10] But then they're starting to scale and see the costs of running these inference workloads.
[446.66 → 453.80] And then they're trying to think about, OK, how can I reduce those GPU costs or the CPU cost in running production in the cloud?
[454.04 → 455.60] And this happens all the time.
[455.60 → 460.24] So our approach is thought about these problems at the beginning while you start development,
[460.70 → 465.62] choosing the right architecture at the beginning instead of kind of having a trial and error iterations
[465.62 → 467.46] when you get to the accuracy.
[467.64 → 471.56] But then you understand that you need to change the model in order to get it productized.
[471.86 → 471.96] Yeah.
[472.06 → 477.38] And I actually have a follow-up on that, mainly because I only have a certain sphere of experience.
[477.54 → 482.10] And I only know what my organization does and what some other organizations do.
[482.10 → 491.56] Just for my own curiosity, how often are you seeing people use GPUs on the inference side versus just CPUs?
[491.92 → 495.18] Do you see that being done more and more?
[495.62 → 499.24] Or what's the majority of inference use cases that you're seeing?
[499.36 → 502.20] Is it inference on GPUs or inference on CPUs?
[502.22 → 504.56] Maybe specifically thinking about cloud deployments.
[504.74 → 506.90] Edge deployments might be somewhat differently.
[507.04 → 510.22] But thinking about cloud deployments at organizations that you work with,
[510.22 → 514.62] is it often inference on the GPU or is it often inference on a CPU?
[515.10 → 520.40] I think that it really depends on the task that you're trying to do the inference and what are you trying to achieve.
[520.52 → 525.24] I think that if we were talking about video analytics workloads, you must use GPU.
[525.54 → 526.70] You have a lot of data.
[526.82 → 529.58] You want to process the data, the images in high resolution.
[530.14 → 531.64] You need a GPU performance.
[531.64 → 538.66] If you're talking about having some queries of NLP model, you usually find those deployed on CPUs.
[538.66 → 543.26] But it doesn't matter because both of them are getting expensive when you get to scale.
[543.26 → 552.32] So if you look about, for example, prices on the cloud for having a four core CPU and a T4 GPU, it's approximately the same.
[552.64 → 556.42] So it's not like the problem is only the prices of GPU.
[556.42 → 564.44] Also, to compute of the CPU is getting expensive when you have to run in large workloads with large clusters with multiple nodes and cores.
[564.92 → 577.78] Could you talk a little bit as we've kind of touched on Edge specifically, could you touch on what some of the challenges you see about deployment to the Edge and the inference that's associated with that are, even beyond just the GPU, CPU consideration?
[577.78 → 581.28] That's certainly something that I'm involved a lot in.
[581.50 → 586.40] And more and more people are now having to deploy to Edge in all sorts of different use cases.
[586.76 → 593.96] And I think we're pretty accustomed at this point to thinking about cloud-based deployment because that's matured a lot faster.
[594.08 → 599.74] But as more and more organizations are involved in Edge deployments, I think they're trying to explore their way through that.
[599.84 → 600.92] Do you have any guidance for that?
[600.92 → 605.42] So first, there's kind of a jungle of Edge hardware types.
[605.72 → 610.22] There are a lot of types of hardware that you can use at the Edge, and it really depends on the application.
[610.38 → 629.04] It could be a mobile phone that if you deploy a mobile app with deep learning in it, you will find out that your users are spread across something like 10 or more types of hardware from iOS with the A&E of Apple and Samsung devices with the Qualcomm Snapdragon and hardware types like that.
[629.04 → 633.88] So first, you need to understand what hardware your users, or you are going to deploy on.
[634.00 → 634.88] That's the first task.
[635.38 → 640.56] Then you need to understand kind of what is the software stack that is best to use for that type of hardware.
[640.64 → 651.70] If we're talking about Apple devices and iOS, we have the Core ML, but most of the other types of hardware will probably be better running with TF Lite or those frameworks that are optimized for edge inference.
[652.04 → 657.86] And above all that, you need to understand kind of what is the limitations of the hardware that you are going to use.
[657.86 → 664.62] For example, memory constraints, memory bottleneck of loading the weights, loading the data and stuff like this.
[664.84 → 671.48] And the performance, what are you going to get if you will run, for example, an object detection model on a Jet son?
[671.62 → 674.02] How many frames per second are you going to get?
[674.12 → 677.22] How many video streams can you put on that Jet son?
[677.22 → 686.56] And this is kind of something that if you'll get to the accuracy, you'll finish building the model and only then we'll measure it on the device that you're looking to deploy on.
[686.56 → 694.36] You'll get back to Square One to redesign the model in order to get the SLA, the latency that you're looking for at the edge.
[694.78 → 700.56] And those are things that you need kind of to have a holistic approach and to see how you solve all of them together.
[700.70 → 710.50] It's kind of a multi-constrained optimization where the accuracy, the latency and the model size are things that you need to consider together when building an edge AI application.
[710.50 → 714.90] And that maybe leads me into another question about that.
[715.10 → 721.28] I do want to get into the specific methods and technology that you've been involved in developing.
[721.52 → 730.04] But it sounds like you're also sort of suggesting a different kind of workflow that people can have in their mind whereas you contrasted to like,
[730.20 → 738.60] I'm going to build my model and the environments in which I'm training my model and testing it are totally different from those where I'm going to deploy it.
[738.60 → 750.66] How can people like adjust their workflow to maybe, is it a matter of always making sure that you have a testing cycle where you're testing on the hardware that you are targeting in the end?
[750.78 → 755.28] Or how can that be integrated into data scientists workflows in a better way?
[755.28 → 767.48] So we are kind of pushing to hardware in a loop development approach when you are taking the inference hardware in the development stage very early in the model selection stage,
[767.48 → 775.86] where you're considering some models, usually based on some open source repositories and academic papers, and you have to measure them at the beginning.
[776.20 → 780.18] This is kind of the first step in understanding if you're going in the right way.
[780.18 → 788.26] After that, you need to understand or think how can you bring that model that meets the SLA to the accuracy that you're looking for.
[788.38 → 793.54] So this is kind of an opposite approach than first reaching the accuracy and then reaching the latency.
[793.70 → 798.64] And this is for edge applications with constraints about the latency and the model size,
[799.06 → 802.52] that those need to be considered at the beginning and not at the end.
[802.52 → 803.36] Makes sense.
[803.84 → 811.86] I am wondering maybe if you can just give like a broad stroke sketch of what people,
[812.32 → 816.50] like let's say that they get to a point where they have the model that they want,
[816.70 → 822.00] and it's not quite optimized for the hardware target that they have in mind.
[822.14 → 825.94] Maybe there's too much latency, or they need to shrink the model or something.
[825.94 → 835.58] What just sort of generally are people trying out there in terms of methods for optimizing their models for inference on certain hardware?
[836.02 → 840.74] There's something we call the inference stack, where at the bottom we consider the hardware itself.
[841.06 → 845.20] On top of that, we have a layer that we call the drivers and the graph compilers.
[845.50 → 849.94] So for example, the Opening for Intel CPU or the Tensor RT for GPUs.
[849.94 → 855.54] On top of that, we have like open source methods like pruning and quantization.
[856.20 → 861.10] Pruning is a method to reduce and eliminate unneeded neurons and connections in the network.
[861.24 → 866.72] And quantization is representing the weights and the activations of the network in lower bit representation,
[867.20 → 869.14] like 8-bit or something like that.
[869.48 → 876.98] So those all are kind of open source and public methods and techniques in order to build more efficient inference.
[876.98 → 882.20] On top of that, what we are doing and specializing is kind of the model design approach,
[882.38 → 887.78] where you need to select the right model that is optimized both for the data to reach the accuracy
[887.78 → 890.90] and also for the hardware to reach the latency.
[891.70 → 896.76] And what we understand today is that different hardware type prefer different types of model.
[897.34 → 898.72] I will give a simple example.
[898.72 → 908.90] If you think about GPU, which has parallelism capabilities, it will prefer large, wider layers with fewer layers in the network
[908.90 → 913.70] because it can parallelize the layer itself, but it cannot parallelize between layers.
[914.04 → 922.48] In contrast, in CPU, there's low parallelism capabilities, and you will probably prefer having narrow layers with fewer neurons,
[922.70 → 924.36] but you can have more layers.
[924.36 → 931.32] And this is kind of a general idea how the inference speed could be affected by the model structure.
[931.60 → 936.60] And by optimizing the model specifically for the inference hardware that you're looking to use,
[936.74 → 942.56] you can get significant boost in the performance compared to having kind of an open source model
[942.56 → 947.68] or off-the-shelf model that you just took from an academic paper or from GitHub or something like that.
[954.36 → 984.34] Thank you.
[984.36 → 1014.34] Thank you.
[1014.36 → 1044.34] Thank you.
[1044.36 → 1074.34] Thank you.
[1074.36 → 1075.36] Thank you.
[1075.36 → 1076.36] Thank you.
[1076.36 → 1077.36] Thank you.
[1077.36 → 1078.36] Thank you.
[1078.36 → 1079.36] Thank you.
[1079.36 → 1080.36] Thank you.
[1108.36 → 1109.36] Thank you.
[1109.36 → 1110.36] Thank you.
[1138.36 → 1139.36] Thank you.
[1139.36 → 1140.36] Thank you.
[1140.36 → 1141.36] Thank you.
[1141.36 → 1142.36] Thank you.
[1142.36 → 1143.36] Thank you.
[1143.36 → 1144.36] Thank you.
[1144.36 → 1145.36] Thank you.
[1173.36 → 1174.36] Thank you.
[1174.36 → 1175.36] Thank you.
[1175.36 → 1176.36] Thank you.
[1176.36 → 1177.36] Thank you.
[1177.36 → 1178.36] Thank you.
[1178.36 → 1179.36] Thank you.
[1179.36 → 1180.36] Thank you.
[1180.36 → 1181.36] Thank you.
[1181.36 → 1182.36] Thank you.
[1182.36 → 1183.36] Thank you.
[1183.36 → 1184.36] Thank you.
[1184.36 → 1185.36] Thank you.
[1185.36 → 1186.36] Thank you.
[1186.36 → 1187.36] Thank you.
[1187.36 → 1188.36] Thank you.
[1188.36 → 1189.36] Thank you.
[1189.36 → 1190.36] Thank you.
[1190.36 → 1191.36] Thank you.
[1191.36 → 1192.36] Thank you.
[1192.36 → 1193.36] Thank you.
[1193.36 → 1194.36] Thank you.
[1194.36 → 1195.36] Thank you.
[1195.36 → 1196.36] Thank you.
[1196.36 → 1197.36] Thank you.
[1197.36 → 1198.36] Thank you.
[1198.36 → 1199.36] Thank you.
[1199.36 → 1200.36] Thank you.
[1200.36 → 1201.36] Thank you.
[1201.36 → 1202.36] Thank you.
[1202.36 → 1203.36] Thank you.
[1203.36 → 1204.36] Thank you.
[1204.36 → 1205.36] Thank you.
[1205.36 → 1206.36] That was a great solution.
[1206.36 → 1207.36] piece of how you're approaching it and what that feels like if you're targeting inference
[1207.36 → 1208.36] on the edge ultimately?
[1208.36 → 1210.36] Yeah.
[1210.36 → 1212.76] So we have a collaboration with Intel that we recently published in ML Perth last September
[1212.76 → 1219.36] or something like that about the performance booster that we have made to image classification model,
[1219.36 → 1221.48] ResNet50 for a MacBook laptop, for example.
[1221.62 → 1223.44] We've done that for several types of hardware,
[1224.12 → 1225.80] but let's take, for example,
[1225.94 → 1227.70] the Edge use case with the MacBook Pro.
[1228.12 → 1230.36] So we're having the baseline model.
[1230.66 → 1232.22] We have three inputs to the algorithm
[1232.22 → 1233.80] of the neural architecture search.
[1233.90 → 1235.14] We're having the baseline model,
[1235.72 → 1238.22] which is, in this example, was ResNet50.
[1238.86 → 1241.22] We're having the hardware itself and the data.
[1241.22 → 1244.22] The data was ImageNet in the Alpert benchmark.
[1244.54 → 1247.38] And the Ultra algorithm kind of searching
[1247.38 → 1250.28] what types of changes
[1250.28 → 1254.92] or how can it change the original architecture of ResNet50
[1254.92 → 1257.12] in order to get a better architecture
[1257.12 → 1262.14] that preserves the accuracy of 76% of accuracy, for example,
[1262.80 → 1265.76] and minimize the latency or maximize the throughput.
[1266.10 → 1269.38] And it is very interesting to see that,
[1269.38 → 1272.14] first, it replaces some of the operations
[1272.14 → 1275.70] from dense convolution layers to depth-wise
[1275.70 → 1278.08] and some other variants of convolutional layers
[1278.08 → 1281.14] that are, let's say, less memory-bounded
[1281.14 → 1283.34] because the cache memory also limits
[1283.34 → 1284.76] the inference speed of the network.
[1285.04 → 1287.68] Second thing that we can learn from that idea
[1287.68 → 1292.60] is that some layers are more important than others.
[1292.78 → 1295.72] So, for example, if you think about what size
[1295.72 → 1298.18] to have on each layer in the network,
[1298.18 → 1301.56] we have some understanding that the initial layers
[1301.56 → 1303.26] that are doing the feature extraction
[1303.26 → 1305.36] in the image classification example
[1305.36 → 1309.02] are more important than the later layers in the network.
[1309.22 → 1311.72] So, putting kind of most of the computation
[1311.72 → 1313.18] at the beginning of the network
[1313.18 → 1317.58] seems to have better accuracy-preserving properties.
[1318.14 → 1319.64] This is kind of what we see
[1319.64 → 1321.48] when we observe on the results
[1321.48 → 1324.54] of that run of Ultra on this example.
[1325.12 → 1326.54] And we end up with a model
[1326.54 → 1329.66] that is faster in something like 3x
[1329.66 → 1333.12] compared to the baseline and having the same accuracy.
[1333.32 → 1335.96] So, this is kind of how we take an algorithm
[1335.96 → 1337.20] that is fully automatic
[1337.20 → 1340.16] and try to do a post-mortem to understand
[1340.16 → 1341.42] what happened there,
[1341.64 → 1344.46] why the output of these algorithms look like that,
[1344.56 → 1347.32] why the initial layers haven't changed
[1347.32 → 1348.70] or almost haven't changed,
[1349.02 → 1351.76] but the later layer has changed significantly,
[1352.12 → 1353.84] replaced to other types of layers,
[1354.18 → 1355.56] their size was smaller,
[1355.56 → 1358.32] and some other changes that we observe
[1358.32 → 1359.74] on the result of the algorithm.
[1359.74 → 1361.96] So, I want to actually get back to that later
[1361.96 → 1363.30] because it's really fascinating
[1363.30 → 1366.08] that you can sort of use these tools
[1366.08 → 1369.46] to learn more about the types of things
[1369.46 → 1371.94] that work well architecture design-wise
[1371.94 → 1372.94] on certain hardware.
[1373.08 → 1373.98] That's fascinating.
[1374.52 → 1377.70] But first, just to sort of bring that example into focus,
[1378.22 → 1380.82] it sounds like you had this base Reset model.
[1381.24 → 1382.90] I'm just thinking about the sort of inputs,
[1382.90 → 1387.30] outputs of the automatic network architecture search.
[1387.78 → 1389.10] Like, if I'm a practitioner
[1389.10 → 1391.40] and maybe I have my own custom model
[1391.40 → 1393.36] for object detection
[1393.36 → 1395.72] or a custom model for speech recognition
[1395.72 → 1396.48] or whatever it is,
[1396.50 → 1397.54] and I've trained that,
[1398.06 → 1399.72] then in terms of doing this
[1399.72 → 1402.10] automatic neural architecture search,
[1402.54 → 1404.66] I'm assuming one input to that
[1404.66 → 1407.60] is the sort of serialized version of my model
[1407.60 → 1409.52] in whatever format it's in.
[1409.52 → 1412.94] You also mentioned that a dataset was input to that.
[1413.44 → 1415.16] Maybe you could give some details on that.
[1415.26 → 1416.92] So, why is the dataset input?
[1417.06 → 1419.24] Is that so that you can make sure
[1419.24 → 1421.80] that you're not optimizing just for the hardware,
[1421.94 → 1423.82] but you're also optimizing to make sure
[1423.82 → 1426.22] that performance doesn't degrade
[1426.22 → 1428.12] in terms of prediction performance?
[1428.56 → 1430.64] And then also, do I need to have access
[1430.64 → 1434.12] to the specific hardware that I'm targeting?
[1434.36 → 1435.80] So, I need this dataset,
[1436.00 → 1438.26] and then do I need the specific hardware
[1438.26 → 1440.76] that I'm targeting and run the automated
[1440.76 → 1443.60] neural architecture search on that hardware?
[1443.84 → 1445.04] Or how does that work?
[1445.34 → 1446.72] Yeah, so you got it right.
[1446.90 → 1448.18] Let's formulate the equation
[1448.18 → 1449.80] that the neural architecture search
[1449.80 → 1450.80] is trying to solve.
[1451.44 → 1454.42] We are talking about minimize the latency
[1454.42 → 1456.76] of the model on a given hardware,
[1457.18 → 1459.40] subject to getting an accuracy
[1459.40 → 1461.26] that is above the given threshold.
[1461.26 → 1464.36] So, the latency of the architecture
[1464.36 → 1466.20] or the model can be measured
[1466.20 → 1468.40] without training in most of the cases
[1468.40 → 1469.36] on the hardware.
[1469.60 → 1471.40] So, we don't need the data to understand
[1471.40 → 1472.62] what is going to be the latency
[1472.62 → 1474.70] of Resonant 50 on a CPU of Intel.
[1474.98 → 1477.40] But the accuracy is data dependent.
[1477.86 → 1479.64] And if we want to put that constraint,
[1479.76 → 1481.32] and obviously we want to put that,
[1481.78 → 1483.40] we need to have the data
[1483.40 → 1485.98] and verify that the model
[1485.98 → 1488.20] that is selected by the minimization problem
[1488.20 → 1490.18] of the latency still meets
[1490.18 → 1491.48] the accuracy requirements.
[1491.62 → 1492.88] Because if we'll not put
[1492.88 → 1493.98] the accuracy constraint,
[1494.62 → 1495.88] we'll end up with a model
[1495.88 → 1498.34] with one neuron that's predicting nothing.
[1498.52 → 1500.34] So, this is kind of the composition
[1500.34 → 1501.38] between the latency
[1501.38 → 1502.66] that is measured on the hardware
[1502.66 → 1503.50] and the accuracy
[1503.50 → 1504.70] that is measured on the data.
[1504.90 → 1506.32] Could you talk a little bit more
[1506.32 → 1507.96] about kind of the output path on that
[1507.96 → 1510.20] in the sense of if, let's say,
[1510.46 → 1511.70] that you have a model
[1511.70 → 1513.96] that's doing object detection
[1513.96 → 1515.32] or it could be anything really,
[1515.32 → 1518.78] and you want to put it on maybe a platform
[1518.78 → 1520.12] that's on the edge
[1520.12 → 1522.16] that has a bunch of sensors,
[1522.26 → 1523.72] maybe a bunch of cameras pulling in.
[1524.20 → 1524.96] When you're going through
[1524.96 → 1526.18] the training process,
[1526.62 → 1527.46] how are you accounting
[1527.46 → 1529.88] for kind of that variability out there?
[1529.98 → 1531.08] You know, kind of going back to
[1531.08 → 1533.58] if you're not targeting the hardware
[1533.58 → 1536.02] in the architecture search
[1536.02 → 1537.42] that you're going to deploy to,
[1537.80 → 1539.20] how do you all account for that?
[1539.28 → 1540.18] How do you say,
[1540.58 → 1542.90] ah, there's a unique configuration
[1542.90 → 1544.94] for my output target,
[1545.04 → 1545.92] my deployment target.
[1546.24 → 1547.16] How do you approach that?
[1547.44 → 1548.48] Are you asking what happens
[1548.48 → 1549.60] when we don't know
[1549.60 → 1550.82] the hardware in production?
[1551.18 → 1552.42] Well, yeah, I guess just like
[1552.42 → 1553.20] if you're targeting
[1553.20 → 1554.66] a particular environment
[1554.66 → 1555.96] that may be customized
[1555.96 → 1557.98] fairly significantly for deployment,
[1558.34 → 1559.44] as more and more practitioners
[1559.44 → 1561.34] are now kind of getting out
[1561.34 → 1562.04] of the data centre
[1562.04 → 1564.04] and they are putting things on drones
[1564.04 → 1565.16] and they're putting things
[1565.16 → 1566.04] into automotive
[1566.04 → 1567.30] being a big one, obviously.
[1567.78 → 1568.62] Anything like that
[1568.62 → 1569.56] that's out on the edge
[1569.56 → 1571.86] and kind of has a custom environment,
[1571.86 → 1572.80] what does that look like
[1572.80 → 1574.38] from a practitioner perspective,
[1574.84 → 1575.88] kind of out of the theory
[1575.88 → 1576.96] and into the hands-on?
[1577.36 → 1579.30] So we prefer to connect
[1579.30 → 1580.38] to the actual hardware
[1580.38 → 1582.28] that the model is going to be deployed on.
[1582.40 → 1583.94] So for example, if it's Jet son,
[1584.34 → 1586.70] we connect the exact Jet son model
[1586.70 → 1588.38] to the neural architectural search.
[1588.92 → 1590.26] If we don't know that,
[1590.32 → 1591.76] we need to have some proxies.
[1592.38 → 1593.62] So a good proxy might be
[1593.62 → 1595.46] the number of floating point operation,
[1596.08 → 1596.94] but we know that
[1596.94 → 1599.14] this is not such a good proxy
[1599.14 → 1600.56] and some other methods
[1600.56 → 1602.94] like pruning target this metric,
[1603.12 → 1604.36] but this metric correlates
[1604.36 → 1606.72] to latency only on CPUs.
[1607.06 → 1608.86] So having proxies there,
[1609.00 → 1610.24] it's not the right approach
[1610.24 → 1611.34] in our perspective.
[1612.08 → 1612.92] Measuring the metric
[1612.92 → 1613.72] that really matters
[1613.72 → 1615.42] on the actual device
[1615.42 → 1616.62] is the way to go
[1616.62 → 1618.04] in my perspective,
[1618.22 → 1619.94] like measuring the actual latency,
[1620.70 → 1621.94] measuring the actual throughput
[1621.94 → 1623.38] on the device
[1623.38 → 1624.38] is the way to go
[1624.38 → 1625.44] in order to understand
[1625.44 → 1626.14] the exact performance
[1626.66 → 1627.58] that you're going to see
[1627.58 → 1628.12] in production
[1628.12 → 1630.02] because I can show examples
[1630.02 → 1631.60] where I cut the flops
[1631.60 → 1633.10] in factor of two
[1633.10 → 1634.26] and the latency
[1634.26 → 1635.22] is getting slower
[1635.22 → 1636.30] on GPU,
[1636.52 → 1637.20] on Jet son,
[1637.26 → 1638.74] on some types of devices.
[1638.88 → 1639.62] So these proxies
[1639.62 → 1641.16] are very problematic today.
[1641.60 → 1642.26] And I think that
[1642.26 → 1643.00] this is kind of
[1643.00 → 1644.08] the interesting part
[1644.08 → 1645.42] of doing hardware
[1645.42 → 1646.88] where neural architecture
[1646.88 → 1647.80] search compared
[1647.80 → 1650.00] to other compression techniques
[1650.00 → 1650.90] like I mentioned
[1650.90 → 1651.48] as pruning
[1651.48 → 1652.68] that reduces
[1652.68 → 1653.74] the number of flops
[1653.74 → 1654.90] or the number of parameters
[1654.90 → 1656.42] or any proxy
[1656.42 → 1657.40] for the size
[1657.40 → 1658.24] or the complexity
[1658.24 → 1659.08] of the network.
[1659.08 → 1660.16] So, Jet son,
[1660.32 → 1661.72] as you're working
[1661.72 → 1662.66] in this space,
[1662.82 → 1664.50] one of the big things
[1664.50 → 1665.96] that I always start thinking
[1665.96 → 1666.72] about when I think
[1666.72 → 1668.24] of optimizing networks
[1668.24 → 1668.86] in this way
[1668.86 → 1670.18] is that there's just
[1670.18 → 1671.92] so many different types
[1671.92 → 1672.48] of layers
[1672.48 → 1673.58] and custom layers
[1673.58 → 1674.88] that people are using
[1674.88 → 1676.26] and new stuff
[1676.26 → 1677.60] coming out all the time.
[1677.80 → 1679.92] So what has it been like
[1679.92 → 1681.36] sort of maintaining
[1681.36 → 1683.30] your search space
[1683.30 → 1684.16] over time
[1684.16 → 1685.80] and growing that space
[1685.80 → 1687.04] to sort of include
[1687.04 → 1688.08] new things
[1688.08 → 1688.96] as they're coming out?
[1689.02 → 1689.68] How do you approach
[1689.68 → 1690.80] that as an organization
[1690.80 → 1692.16] and figure out
[1692.16 → 1693.20] how to expand
[1693.20 → 1694.06] that search space
[1694.06 → 1694.96] and what to include
[1694.96 → 1696.12] and what not to include?
[1696.52 → 1697.90] So that's a good question
[1697.90 → 1699.34] because the research field
[1699.34 → 1700.02] of deep learning
[1700.02 → 1701.88] is progressing very fast.
[1702.18 → 1703.64] And we have
[1703.64 → 1704.82] a team of researchers
[1704.82 → 1706.46] that's sitting on
[1706.46 → 1708.66] the latest academic papers
[1708.66 → 1709.38] that propose
[1709.38 → 1710.74] all those new layers
[1710.74 → 1712.40] and those new operators.
[1712.40 → 1714.80] and kind of reproduce
[1714.80 → 1716.02] all these models
[1716.02 → 1717.12] to understand
[1717.12 → 1718.46] which type of layers,
[1718.62 → 1719.74] which types of techniques
[1719.74 → 1721.30] are worth adding
[1721.30 → 1722.52] to the search space
[1722.52 → 1724.20] of the neural architecture search
[1724.20 → 1725.48] and which are not.
[1725.62 → 1726.40] And actually,
[1726.50 → 1727.10] the result
[1727.10 → 1728.28] is very interesting.
[1728.68 → 1729.90] In most cases,
[1730.14 → 1730.60] for example,
[1730.70 → 1731.58] if we'll take
[1731.58 → 1733.16] the computer vision domain,
[1733.36 → 1734.78] the basic operators
[1734.78 → 1736.16] that are well known
[1736.16 → 1737.48] for the last five years
[1737.48 → 1738.74] or something like that
[1738.74 → 1740.08] are performing the best.
[1740.08 → 1741.44] So some of the tricks
[1741.44 → 1742.52] that we see now
[1742.52 → 1743.66] are not improving
[1743.66 → 1745.12] so much compared
[1745.12 → 1747.12] to using those blocks
[1747.12 → 1747.90] and operators
[1747.90 → 1749.68] that build Reset
[1749.68 → 1750.92] and Mobile Net
[1750.92 → 1751.76] and Efficient Net
[1751.76 → 1752.68] and those networks.
[1752.88 → 1754.74] So having the right composition
[1754.74 → 1755.78] of operators
[1755.78 → 1756.98] is more crucial
[1756.98 → 1757.74] than having
[1757.74 → 1759.34] all those fancy tricks
[1759.34 → 1760.48] that showed up
[1760.48 → 1761.72] in the last two
[1761.72 → 1762.56] or three years.
[1762.66 → 1763.26] This is something
[1763.26 → 1764.00] that we see.
[1764.34 → 1766.08] It's quite general claim.
[1766.34 → 1767.30] There are some cases
[1767.30 → 1768.16] that we see things
[1768.16 → 1769.22] that were adding
[1769.22 → 1770.20] to the search space.
[1770.36 → 1771.14] But in general,
[1771.14 → 1772.02] I would say
[1772.02 → 1773.74] that it's not so easy
[1773.74 → 1775.80] to beat a Reset model
[1775.80 → 1777.44] that is quantized
[1777.44 → 1779.18] and use the graph compiler
[1779.18 → 1780.08] like TensorFlow’t
[1780.08 → 1781.38] or something like that.
[1781.80 → 1783.00] And you need to work hard
[1783.00 → 1784.02] in order to beat it.
[1784.12 → 1785.24] So this is kind of
[1785.24 → 1786.26] how we see
[1786.26 → 1787.26] all the advancement.
[1787.98 → 1788.42] Of course,
[1788.48 → 1789.82] we have other advancement
[1789.82 → 1790.78] in other fields
[1790.78 → 1792.06] like training tricks,
[1792.34 → 1793.00] optimizers
[1793.00 → 1794.08] and stuff like this.
[1794.08 → 1795.26] And we have to be
[1795.26 → 1796.08] on the front line
[1796.08 → 1797.12] on all of those.
[1797.22 → 1797.86] And this is something
[1797.86 → 1798.62] that we are working
[1798.62 → 1799.30] really hard
[1799.30 → 1800.84] in order to reproduce
[1800.84 → 1802.14] all state-of-the-art,
[1802.28 → 1803.22] all the types of models,
[1803.38 → 1804.36] all those new models
[1804.36 → 1806.08] that just announced
[1806.08 → 1807.62] and having the results
[1807.62 → 1808.56] and the operators
[1808.56 → 1809.60] in our search space.
[1810.04 → 1811.68] And a follow-up on that,
[1811.76 → 1812.10] I guess,
[1812.16 → 1812.86] which is related
[1812.86 → 1814.16] to that approach is
[1814.16 → 1814.96] on the one side,
[1815.02 → 1815.64] you have all of these
[1815.64 → 1816.18] different types
[1816.18 → 1816.98] of architectures.
[1817.14 → 1817.96] On the other side,
[1818.02 → 1819.78] you have all of these
[1819.78 → 1821.00] different tasks
[1821.00 → 1821.96] being solved
[1821.96 → 1823.58] with deep learning models
[1823.58 → 1824.92] and AI models.
[1825.48 → 1826.76] So I'm curious,
[1826.86 → 1827.76] as you've experienced
[1827.76 → 1828.92] this over a number
[1828.92 → 1829.78] of years now,
[1830.26 → 1831.26] is it harder
[1831.26 → 1832.46] to optimize
[1832.46 → 1833.50] the inference
[1833.50 → 1835.76] of certain tasks
[1835.76 → 1836.98] versus other tasks?
[1837.02 → 1837.86] So maybe like
[1837.86 → 1839.28] NLP tasks
[1839.28 → 1841.04] versus computer vision tasks
[1841.04 → 1842.56] versus audio tasks
[1842.56 → 1843.04] versus,
[1843.64 → 1844.02] you know,
[1844.12 → 1845.28] maybe it's time series
[1845.28 → 1846.44] modelling or something.
[1846.58 → 1847.36] Are there certain
[1847.36 → 1848.52] domains
[1848.52 → 1850.48] of AI tasks
[1850.48 → 1851.16] that are harder
[1851.16 → 1851.80] to optimize
[1851.80 → 1852.44] than others?
[1852.44 → 1853.78] So at the moment,
[1853.78 → 1854.92] we are mostly focused
[1854.92 → 1855.98] on computer vision
[1855.98 → 1856.54] and NLP.
[1857.12 → 1858.36] And in those domains,
[1858.36 → 1859.50] we see that the principles
[1859.50 → 1860.36] that we are using
[1860.36 → 1861.94] that are machine learning based
[1861.94 → 1863.04] are working
[1863.04 → 1864.00] across the board.
[1864.34 → 1864.60] Yes,
[1864.66 → 1865.50] I can tell that
[1865.50 → 1866.78] there are some tasks
[1866.78 → 1867.56] in a domain
[1867.56 → 1868.58] that are a little bit
[1868.58 → 1869.34] more complex.
[1869.46 → 1869.94] For example,
[1870.10 → 1871.70] semantic segmentation networks
[1871.70 → 1872.74] are more complex
[1872.74 → 1874.88] than classification networks.
[1875.42 → 1876.82] And they have to preserve
[1876.82 → 1878.02] the information
[1878.02 → 1879.00] along the network
[1879.00 → 1879.76] in order to do
[1879.76 → 1880.50] kind of image
[1880.50 → 1881.96] to image tasks.
[1882.26 → 1883.70] But also on those
[1883.70 → 1885.72] type of neural architectures,
[1885.84 → 1887.06] we can optimize them.
[1887.12 → 1887.70] And the principle
[1887.70 → 1888.58] is very simple.
[1888.92 → 1890.12] Most of the networks
[1890.12 → 1892.00] and the new fancy algorithms
[1892.00 → 1892.96] are kind of built
[1892.96 → 1894.48] on top of three components.
[1894.68 → 1895.84] One is the stem,
[1896.30 → 1897.36] is the few layers
[1897.36 → 1898.68] connected to the input.
[1898.84 → 1899.86] The second component
[1899.86 → 1900.64] is the backbone.
[1901.52 → 1902.46] And the third component
[1902.46 → 1903.74] is the prediction block.
[1903.92 → 1905.08] In most cases,
[1905.40 → 1906.50] 80 to 90%
[1906.50 → 1907.40] of to compute
[1907.40 → 1908.32] is happening
[1908.32 → 1909.08] in the backbone.
[1909.08 → 1910.62] And usually the backbone
[1910.62 → 1911.96] are just a bunch
[1911.96 → 1913.12] of convolutional layers
[1913.12 → 1913.66] in the case
[1913.66 → 1914.68] of computer vision.
[1915.42 → 1916.36] And by optimizing
[1916.36 → 1918.34] that significant part
[1918.34 → 1919.06] of the network,
[1919.22 → 1920.40] which is similar
[1920.40 → 1921.56] across classification,
[1921.86 → 1922.88] semantic segmentation,
[1922.94 → 1923.74] and object detection,
[1924.28 → 1925.28] you can get that boost
[1925.28 → 1926.08] of performance
[1926.08 → 1926.84] that we are looking
[1926.84 → 1928.56] to have in all tasks.
[1929.22 → 1929.78] As we're talking
[1929.78 → 1930.32] about this,
[1930.42 → 1931.46] I'm just visualizing
[1931.46 → 1932.50] everything in my head.
[1932.76 → 1934.02] As you get to the output
[1934.02 → 1934.92] and you've targeted
[1934.92 → 1937.16] a particular deployment target
[1937.16 → 1938.40] and accounted
[1938.40 → 1939.14] for the hardware
[1939.14 → 1940.68] and what the capabilities are.
[1941.08 → 1941.46] I'm curious,
[1941.54 → 1942.42] how does your platform
[1942.42 → 1943.28] integrate in
[1943.28 → 1945.08] with whatever DevOps pipeline
[1945.08 → 1945.70] a practitioner
[1945.70 → 1947.24] might have put into place?
[1947.40 → 1948.62] What is a typical scenario
[1948.62 → 1949.98] for actually pushing
[1949.98 → 1950.82] the deployment out
[1950.82 → 1951.54] to the hardware
[1951.54 → 1952.58] that it's going to run on
[1952.58 → 1953.56] for inference look like?
[1953.82 → 1955.58] So we look at our platform
[1955.58 → 1956.60] as an end-to-end platform
[1956.60 → 1957.38] from development
[1957.38 → 1958.14] to production.
[1958.14 → 1960.36] We develop two production tools,
[1960.50 → 1961.76] one of them called Infer
[1961.76 → 1963.98] and the second is called RCIC.
[1964.42 → 1965.42] Infer is a lightweight
[1965.42 → 1967.72] edge inference engine
[1967.72 → 1969.00] that could be integrated
[1969.00 → 1971.72] to a monolith application easily.
[1972.60 → 1974.68] And RCIC is a containerized
[1974.68 → 1975.48] inference server.
[1975.74 → 1977.84] So if you'll take that solution,
[1978.20 → 1979.76] it could be easily deployed
[1979.76 → 1980.68] by a DevOps
[1980.68 → 1982.42] with the model inside,
[1982.84 → 1984.26] fetched from the model repository
[1984.26 → 1985.06] that we provide
[1985.06 → 1986.42] as part of our SaaS offering,
[1987.12 → 1989.10] and kind of serve the model
[1989.10 → 1990.68] in a standardized API
[1990.68 → 1991.72] that contains
[1991.72 → 1992.58] all the packages,
[1993.10 → 1993.46] libraries,
[1993.70 → 1994.60] environment details
[1994.60 → 1995.16] that you need
[1995.16 → 1996.92] in order to go over Kubernetes
[1996.92 → 1998.72] for inference and scale.
[1999.46 → 2001.10] Sometimes we see companies
[2001.10 → 2002.06] that already have
[2002.06 → 2003.22] their own infrastructure
[2003.22 → 2004.74] and don't want to change
[2004.74 → 2006.20] their existing infrastructure,
[2006.42 → 2007.22] and we provide them
[2007.22 → 2008.46] with the specific model,
[2008.72 → 2009.76] just the exact model
[2009.76 → 2011.18] that ran the optimization,
[2011.84 → 2012.44] the model after
[2012.44 → 2013.44] the optimized model
[2013.44 → 2014.96] in their format.
[2015.18 → 2016.24] We support all the types
[2016.24 → 2016.82] of formats
[2016.82 → 2017.74] from Onix
[2017.74 → 2018.48] to TensorFlow,
[2018.48 → 2019.48] PyTorch,
[2020.00 → 2020.32] Keras,
[2020.58 → 2021.56] and all of these frameworks
[2021.56 → 2023.08] that you can run inference on.
[2023.60 → 2025.32] So this is kind of the two ways
[2025.32 → 2027.18] to get DESI optimized model
[2027.18 → 2028.64] to a production environment,
[2028.78 → 2030.72] either by our deployment tools
[2030.72 → 2032.04] or getting the model
[2032.04 → 2033.52] and using your existing stack.
[2033.86 → 2035.50] I'm just kind of browsing around
[2035.50 → 2036.60] on some of the information
[2036.60 → 2037.36] about DESI
[2037.36 → 2038.98] and super fascinating.
[2039.20 → 2040.34] One of the things that I see
[2040.34 → 2042.02] is this idea of DESI nets,
[2042.42 → 2043.62] which you share about
[2043.62 → 2046.24] and share some of the sort of successes
[2046.24 → 2047.74] that you've had
[2047.74 → 2049.26] taking this approach
[2049.26 → 2051.26] in various domains
[2051.26 → 2052.90] for various types of models.
[2053.28 → 2054.08] Could you just share
[2054.08 → 2055.62] a few success stories
[2055.62 → 2056.92] in terms of
[2056.92 → 2057.82] what you've been able
[2057.82 → 2060.26] to achieve performance-wise
[2060.26 → 2061.10] with this approach?
[2061.58 → 2062.44] Yeah, so DESI nets
[2062.44 → 2063.94] is a good example for that.
[2064.12 → 2066.88] We took a few well-known tasks
[2066.88 → 2068.20] like image classification,
[2068.70 → 2069.54] object detection,
[2069.66 → 2070.94] and semantic segmentation.
[2070.94 → 2072.68] And we've taken
[2072.68 → 2073.76] the most famous
[2073.76 → 2075.04] open-source data set,
[2075.14 → 2075.62] for example,
[2075.80 → 2076.34] ImageNet,
[2076.52 → 2076.74] Coco,
[2077.38 → 2078.82] and data sets like that,
[2078.88 → 2079.68] and we built
[2079.68 → 2080.72] kind of catalogue
[2080.72 → 2082.96] of pre-optimized models
[2082.96 → 2084.42] for each and every hardware.
[2084.98 → 2085.84] And what we are doing,
[2085.96 → 2087.14] we are kind of plotting
[2087.14 → 2088.06] what we call
[2088.06 → 2089.26] an efficient frontier,
[2089.66 → 2091.16] chart with the latency
[2091.16 → 2092.14] on the x-axis
[2092.14 → 2093.62] and the accuracy
[2093.62 → 2094.48] on the y-axis,
[2094.88 → 2095.80] and plotting
[2095.80 → 2096.76] all the models
[2096.76 → 2097.62] that we know,
[2097.74 → 2098.28] the Reset,
[2098.60 → 2099.34] the YOLO,
[2099.34 → 2100.44] and those models
[2100.44 → 2101.64] on those charts
[2101.64 → 2103.42] and putting those DESI nets
[2103.42 → 2104.92] or DESI nets for detection
[2104.92 → 2106.56] and kind of seeing
[2106.56 → 2107.24] what we call
[2107.24 → 2108.20] the efficient frontier,
[2108.62 → 2109.70] how those models
[2109.70 → 2111.30] reach better accuracy
[2111.30 → 2112.28] and better latency
[2112.28 → 2113.20] and dominates
[2113.20 → 2114.50] this trade-off
[2114.50 → 2115.24] between accuracy
[2115.24 → 2115.92] and latency.
[2116.62 → 2117.56] And now we provide
[2117.56 → 2118.86] those DESI nets
[2118.86 → 2120.18] for data scientists
[2120.18 → 2121.16] in order to try
[2121.16 → 2121.64] to feed them
[2121.64 → 2122.88] to their specific data,
[2123.08 → 2123.90] fine-tune them
[2123.90 → 2125.48] for their specific data,
[2125.86 → 2126.86] and having kind of
[2126.86 → 2128.22] a pre-optimized result
[2128.22 → 2128.98] of AutoNAC
[2128.98 → 2129.54] that is ready
[2129.54 → 2130.86] for use immediately.
[2131.66 → 2132.32] And I'm wondering,
[2132.60 → 2133.74] as you plot out
[2133.74 → 2134.60] this landscape,
[2135.04 → 2136.18] I love how you term that
[2136.18 → 2138.02] like the efficiency landscape,
[2138.02 → 2139.22] it's a really cool way
[2139.22 → 2140.58] to think about space.
[2140.76 → 2142.12] As you plot this out
[2142.12 → 2143.54] and explore that space
[2143.54 → 2144.32] yourself,
[2144.88 → 2145.46] I'm wondering,
[2145.72 → 2146.74] one way to think about
[2146.74 → 2147.58] what you're doing
[2147.58 → 2148.92] and how you've expressed it
[2148.92 → 2150.26] is I'm a data scientist,
[2150.26 → 2151.52] I've trained my model,
[2151.66 → 2152.30] now I run it
[2152.30 → 2152.98] through Auto
[2152.98 → 2154.14] Neural Architecture
[2154.14 → 2154.60] Search
[2154.60 → 2155.42] and get out my,
[2155.88 → 2156.18] you know,
[2156.24 → 2157.04] better model,
[2157.04 → 2158.72] faster and more efficient
[2158.72 → 2159.76] for the architecture
[2159.76 → 2160.90] while still performing
[2160.90 → 2161.80] well for prediction.
[2162.34 → 2163.02] But I'm wondering
[2163.02 → 2164.76] if this sort of cycle,
[2164.92 → 2165.62] as you do that
[2165.62 → 2166.16] more and more,
[2166.24 → 2167.46] you start sort of
[2167.46 → 2168.52] building some intuition
[2168.52 → 2169.66] as a data scientist
[2169.66 → 2170.60] or a practitioner
[2170.60 → 2172.38] to like start
[2172.38 → 2173.50] with a better model
[2173.50 → 2174.46] in the first place.
[2174.60 → 2174.80] Like,
[2175.16 → 2176.60] if I look at your plots
[2176.60 → 2178.16] of the efficiency landscape,
[2178.78 → 2180.50] can I learn some things
[2180.50 → 2181.16] about maybe,
[2181.56 → 2182.46] maybe I start
[2182.46 → 2183.34] with better models
[2183.34 → 2184.60] in the first place
[2184.60 → 2186.06] rather than sort of
[2186.06 → 2187.64] relying as much
[2187.64 → 2189.20] on the neural architecture
[2189.20 → 2189.60] search?
[2189.68 → 2190.26] Do you think there's
[2190.26 → 2191.04] that sort of feedback
[2191.04 → 2191.88] and that learning
[2191.88 → 2192.62] that can happen
[2192.62 → 2194.32] from like what architectures
[2194.32 → 2195.00] are learned
[2195.00 → 2196.32] by the automatic
[2196.32 → 2197.88] neural architecture search?
[2198.52 → 2198.72] Yeah,
[2198.94 → 2199.50] absolutely.
[2199.66 → 2201.02] We share some information,
[2201.28 → 2202.32] intuition behind
[2202.32 → 2203.70] those architectures
[2203.70 → 2204.40] that found
[2204.40 → 2205.42] for a given hardware.
[2205.62 → 2206.06] For example,
[2206.18 → 2206.78] one of the things
[2206.78 → 2207.42] that we see
[2207.42 → 2209.72] that those architectures
[2209.72 → 2210.44] are faster
[2210.44 → 2212.06] but having more parameters,
[2212.26 → 2212.78] for example.
[2212.78 → 2213.30] So,
[2213.56 → 2214.34] this is kind of
[2214.34 → 2214.84] an intuition
[2214.84 → 2215.68] that we see
[2215.68 → 2217.12] around these models
[2217.12 → 2218.04] that can be used
[2218.04 → 2218.54] to understand
[2218.54 → 2220.40] that we not always
[2220.40 → 2221.90] look to smaller models
[2221.90 → 2223.12] but for more
[2223.12 → 2224.12] faster models
[2224.12 → 2225.18] and accurate models.
[2225.40 → 2226.74] We provide those models
[2226.74 → 2227.74] as a starting point.
[2227.86 → 2227.94] So,
[2228.06 → 2228.46] for example,
[2228.56 → 2229.28] if you're considering
[2229.28 → 2231.18] taking Reset 54Ri
[2231.18 → 2232.56] or EfficientMent B0,
[2232.94 → 2233.88] you can take
[2233.88 → 2234.88] the corresponding
[2234.88 → 2236.06] DESINENT model
[2236.06 → 2237.34] and start from that
[2237.34 → 2238.42] and tweak that
[2238.42 → 2239.78] for your application
[2239.78 → 2240.78] whether you're doing
[2240.78 → 2241.76] object detection,
[2241.98 → 2242.48] classification,
[2242.78 → 2244.36] or anything like that
[2244.36 → 2246.02] and this is kind of
[2246.02 → 2247.06] giving the ability
[2247.06 → 2249.80] to use a NAS-produced model
[2249.80 → 2250.88] compared to having
[2250.88 → 2251.70] a model that is
[2251.70 → 2252.44] off-the-shelf
[2252.44 → 2253.84] for general use.
[2254.12 → 2254.20] So,
[2254.34 → 2254.86] for example,
[2255.18 → 2255.98] Efficient Nets
[2255.98 → 2257.22] is a result by Google
[2257.22 → 2258.62] from two years ago
[2258.62 → 2259.84] or something like that
[2259.84 → 2260.76] that are supposed
[2260.76 → 2261.48] to be efficient
[2261.48 → 2262.86] but it appears to
[2262.86 → 2263.96] that Efficient Nets
[2263.96 → 2265.02] are not so efficient
[2265.02 → 2266.02] for GPUs
[2266.02 → 2267.60] even when they are
[2267.60 → 2269.12] over-quantization
[2269.12 → 2270.14] and graph compiler
[2270.14 → 2271.06] like Tensor RT.
[2271.70 → 2272.02] So,
[2272.62 → 2274.86] having a pre-optimized model
[2274.86 → 2275.78] for the given hardware
[2275.78 → 2276.82] that you're going to use
[2276.82 → 2277.54] is very crucial
[2277.54 → 2278.92] and in our example
[2278.92 → 2279.72] of DEFINES,
[2280.14 → 2281.08] we show that
[2281.08 → 2281.96] you can have
[2281.96 → 2283.50] a model that is
[2283.50 → 2284.56] something like
[2284.56 → 2285.56] three times faster
[2285.56 → 2286.86] than EfficientMent B0
[2286.86 → 2288.68] for Jet son GPU
[2288.68 → 2290.20] while having
[2290.20 → 2291.58] even better accuracy.
[2291.58 → 2292.36] So,
[2292.44 → 2293.20] this is kind of
[2293.20 → 2294.78] a result that you can take
[2294.78 → 2295.74] off-the-shelf
[2295.74 → 2296.62] instead of using
[2296.62 → 2297.66] EfficientMent B0
[2297.66 → 2299.34] you can take that model
[2299.34 → 2300.54] and train it
[2300.54 → 2301.48] to your application
[2301.48 → 2303.22] build on top of that
[2303.22 → 2305.16] some other prediction heads
[2305.16 → 2306.42] some other tasks
[2306.42 → 2307.36] that you want to solve
[2307.36 → 2308.18] with that backbone
[2308.18 → 2310.80] and get an automatic result
[2310.80 → 2312.08] without running
[2312.08 → 2314.24] all the neural architecture search
[2314.24 → 2315.86] for that specific task.
[2316.32 → 2317.34] That's very cool.
[2317.52 → 2318.70] This is so interesting
[2318.70 → 2320.20] as you were talking about
[2320.20 → 2321.28] model optimization
[2321.28 → 2322.04] and the things
[2322.04 → 2323.34] that DESI has done with it
[2323.34 → 2325.02] what are you envisioning
[2325.02 → 2326.06] as you guys are looking
[2326.06 → 2326.68] into the future
[2326.68 → 2327.38] at this point?
[2327.62 → 2328.68] What kinds of things
[2328.68 → 2329.72] are aspirational
[2329.72 → 2330.60] for DESI
[2330.60 → 2331.70] in terms of
[2331.70 → 2332.14] where you want to
[2332.14 → 2332.94] take the platform
[2332.94 → 2334.58] and what you envision
[2334.58 → 2336.32] will be the next thing
[2336.32 → 2337.18] in model optimization
[2337.18 → 2338.30] that you'd like to implement?
[2338.60 → 2339.72] I think that we feel
[2339.72 → 2340.96] at the good point
[2340.96 → 2343.06] in the model optimization space
[2343.06 → 2345.18] that now we are seeing
[2345.18 → 2346.32] that we need to expand
[2346.32 → 2348.02] to the whole development
[2348.02 → 2348.94] lifecycle.
[2349.54 → 2349.86] So,
[2350.08 → 2351.26] after you have the data
[2351.26 → 2353.02] we look on controlling
[2353.02 → 2353.94] all the training
[2353.94 → 2354.52] optimization
[2354.52 → 2355.50] and deployment
[2355.50 → 2356.80] of deep learning model
[2356.80 → 2358.04] on our platform
[2358.04 → 2359.54] whether you're using
[2359.54 → 2360.42] those Defines
[2360.42 → 2361.50] or using some
[2361.50 → 2362.68] off-the-shelf models
[2362.68 → 2364.48] and kind of having
[2364.48 → 2365.56] a full workflow
[2365.56 → 2366.92] of development,
[2367.22 → 2367.60] optimization,
[2367.60 → 2368.50] and deployment
[2368.50 → 2370.18] based on our platform.
[2370.18 → 2372.00] that's because we understand
[2372.00 → 2373.54] that there is kind of
[2373.54 → 2374.04] a triangle
[2374.04 → 2375.20] that we can draw
[2375.20 → 2377.10] that is on one edge
[2377.10 → 2378.04] we have the model,
[2378.20 → 2378.94] on the other one
[2378.94 → 2379.82] we have the data,
[2380.46 → 2381.52] and on the last one
[2381.52 → 2382.50] we have the hardware.
[2383.04 → 2383.96] And this is kind of
[2383.96 → 2385.08] a combined optimization
[2385.08 → 2386.56] that every data scientist
[2386.56 → 2387.46] need to understand
[2387.46 → 2388.60] how they solve that.
[2388.60 → 2390.02] and we are kind of
[2390.02 → 2391.18] providing the tools
[2391.18 → 2392.42] to solve this,
[2392.68 → 2393.60] optimize this triangle
[2393.60 → 2395.36] and for now
[2395.36 → 2396.48] we are mostly focused
[2396.48 → 2397.58] on the model side.
[2397.90 → 2398.96] But in the future
[2398.96 → 2400.26] we'll be also focused
[2400.26 → 2400.98] on the data
[2400.98 → 2402.40] and the hardware side
[2402.40 → 2403.46] in terms of
[2403.46 → 2404.64] not having them fixed
[2404.64 → 2406.00] but having some techniques
[2406.00 → 2407.78] for data enrichment,
[2408.22 → 2409.08] data augmentation,
[2409.82 → 2410.94] self-supervised learning,
[2411.56 → 2412.32] having some
[2412.32 → 2414.08] hardware recommendation system,
[2414.78 → 2415.82] maybe having some
[2415.82 → 2417.28] FPGA capabilities
[2417.28 → 2418.94] and having our hardware
[2418.94 → 2419.72] that is optimized
[2419.72 → 2420.78] for the given model.
[2421.22 → 2422.08] And this is kind of
[2422.08 → 2422.92] the far future
[2422.92 → 2424.30] about how I see
[2424.30 → 2426.50] optimization in its full.
[2427.00 → 2427.52] That's awesome.
[2428.08 → 2429.86] Well, I'm really excited
[2429.86 → 2430.76] that we got to talk
[2430.76 → 2431.22] through this
[2431.22 → 2432.10] because I know
[2432.10 → 2433.08] I learned a lot
[2433.08 → 2433.86] about this
[2433.86 → 2435.30] neural architecture search
[2435.30 → 2436.08] and the things
[2436.08 → 2436.66] that you're doing.
[2436.84 → 2438.04] So really impressed
[2438.04 → 2439.10] with where you're headed
[2439.10 → 2439.62] with this
[2439.62 → 2440.46] and appreciate you
[2440.46 → 2441.18] taking time
[2441.18 → 2442.16] to join us
[2442.16 → 2443.46] and chat with us about it.
[2443.70 → 2443.92] Sure.
[2444.04 → 2444.78] Thank you very much.
[2444.82 → 2445.46] It was great
[2445.46 → 2446.36] talking to you
[2446.36 → 2447.42] and I look forward
[2447.42 → 2448.78] to QD episodes.
[2451.74 → 2452.96] Thank you for listening
[2452.96 → 2454.26] to Practical AI.
[2454.80 → 2455.92] We have a bundle
[2455.92 → 2457.22] of awesome podcasts
[2457.22 → 2458.94] for you at changelog.com
[2458.94 → 2460.36] including our brand-new show
[2460.36 → 2460.96] Ship It
[2460.96 → 2462.04] with Gerhard Leon.
[2462.28 → 2463.36] A podcast about
[2463.36 → 2464.78] getting your best ideas
[2464.78 → 2465.60] into the world
[2465.60 → 2466.84] and seeing what happens.
[2467.20 → 2468.20] It's about the code,
[2468.40 → 2468.94] the ops,
[2469.06 → 2469.54] the infra
[2469.54 → 2470.30] and the people
[2470.30 → 2471.08] that make it happen.
[2471.38 → 2472.62] Yes, we focus on the people
[2472.62 → 2473.74] because everything else
[2473.74 → 2475.10] is an implementation detail.
[2475.10 → 2476.08] Subscribe now
[2476.08 → 2477.22] at changelog.com
[2477.22 → 2478.06] slash ship it
[2478.06 → 2479.28] or simply search for
[2479.28 → 2479.70] ship it
[2479.70 → 2480.82] and your favourite podcast app
[2480.82 → 2481.38] you'll find it.
[2481.54 → 2481.82] Of course,
[2481.90 → 2482.92] the galaxy brain move
[2482.92 → 2483.58] is to subscribe
[2483.58 → 2484.78] to our master feed.
[2484.92 → 2486.54] It's all changelog podcasts
[2486.54 → 2488.04] including Practical AI
[2488.04 → 2488.88] and Ship It
[2488.88 → 2490.16] in one place.
[2490.52 → 2491.92] Search changelog master feed
[2491.92 → 2492.60] or head to
[2492.60 → 2493.42] changelog.com
[2493.42 → 2494.04] slash master
[2494.04 → 2495.24] and subscribe today.
[2495.70 → 2496.46] Practical AI
[2496.46 → 2497.14] is hosted by
[2497.14 → 2497.86] Daniel Whiten ack
[2497.86 → 2498.60] and Chris Benson
[2498.60 → 2499.34] with music
[2499.34 → 2500.44] by Break master Cylinder.
[2500.66 → 2501.12] We're brought to you
[2501.12 → 2501.70] by Vastly,
[2501.90 → 2502.48] Vaughn Starkly
[2502.48 → 2503.18] and Linde.
[2503.52 → 2504.18] That's all for now.
[2504.18 → 2505.36] We'll talk to you again next week.
[2505.36 → 2505.38] We'll talk to you again next week.
[2505.38 → 2505.42] We'll talk to you again next week.
[2534.18 → 2535.42] We'll talk to you again next week.
