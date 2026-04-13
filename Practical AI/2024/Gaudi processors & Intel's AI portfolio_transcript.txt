[0.00 --> 8.66]  Welcome to Practical AI.
[9.18 --> 19.54]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[19.86 --> 24.94]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.94 --> 32.38]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.80 --> 35.44]  So you can launch your app near your users.
[35.84 --> 37.84]  Learn more at Fly.io.
[44.24 --> 49.04]  What's up friends? Intel Innovation 2024 is right around the corner.
[49.04 --> 56.48]  Accelerate the Future. Registration is now open and it takes place September 24th and 25th in San Jose, California.
[56.92 --> 64.78]  This event is all about you, the developer, the community, and the critical role you play in tackling the toughest challenges across the industry.
[65.22 --> 67.60]  Ignite your passion for AI and beyond.
[67.88 --> 76.44]  Grow your skills to maximize your impact and network with your peers as they unleash the next wave of advancements in technology.
[76.44 --> 88.12]  Here's what you can expect. Understand the emerging innovation and trends in dev tools, languages, frameworks, and technologies in AI and beyond to empower you and the solutions you're building.
[88.60 --> 97.12]  Get in-depth technical experience doing hands-on workshops, labs, meetups, and hackathons to collaborate and solve problems in real time.
[97.44 --> 100.70]  You can explore featured partner and Intel solutions.
[100.70 --> 111.76]  They have partners there, startups there, customers there, and Intel is showcasing the latest in products, services, and solutions across keynotes, tech sessions, and the show floor to help you meet your development needs.
[112.12 --> 125.50]  Collaborate with experts, learn and have fun, engage in interactive sessions to connect, get certified, gain unique ideas and perspectives, build long-lasting networks, and of course, have fun.
[125.50 --> 140.14]  And get inspired, hear from leading industry experts, technologists, startup entrepreneurs, and fellow developers, along with Intel leadership, CEO Pat Gelsinger, and CTO Greg Lavender, as they take you through the latest advancements in technology.
[140.56 --> 143.10]  Don't miss this chance to be at the forefront of innovation.
[143.50 --> 146.82]  Take advantage of early bird pricing right now until August 2nd.
[147.10 --> 148.80]  Register using the link in our show notes.
[149.02 --> 152.40]  Or to learn more, go to intel.com slash innovation.
[152.40 --> 155.32]  Once more, that's intel.com slash innovation.
[155.78 --> 157.58]  Or go to the show notes and click that link.
[166.74 --> 169.88]  Welcome to another episode of Practical AI.
[170.22 --> 171.78]  My name is Daniel Whitenack.
[171.86 --> 174.80]  I am founder and CEO at Prediction Guard.
[175.04 --> 181.42]  I'm joined as always by my co-host, Chris Benson, who is a principal AI research engineer at Lockheed Martin.
[181.42 --> 182.38]  How are you doing, Chris?
[182.40 --> 183.84]  Doing great today, Daniel.
[183.90 --> 184.34]  How's it going?
[184.76 --> 185.72]  It's going well.
[185.90 --> 196.62]  I am really happy to bring a little bit of content to the show today that is from a little bit of the world that I've been operating in.
[196.62 --> 208.80]  And some of the groups that I've been collaborating with at Intel, which I think is a really kind of cool set of stuff that maybe people are, maybe they're less aware of it.
[208.86 --> 209.74]  Maybe they're aware of it.
[209.80 --> 217.82]  But really happy to have with us today Benjamin Consalvo, who is an AI engineering manager at Intel.
[217.82 --> 224.90]  And then also Greg Siraki, who is a developer ecosystem manager at Intel Gaudi.
[225.14 --> 225.36]  Welcome.
[225.96 --> 226.72]  Yeah, thank you.
[226.92 --> 227.52]  Thanks for having us.
[227.92 --> 228.06]  Yeah.
[228.16 --> 242.08]  Well, like I say, I think, you know, people are, of course, aware of Intel and that, you know, Intel is sort of everywhere in one degree or another and in cloud providers and PCs and all of that.
[242.08 --> 251.14]  But I think some people might not be aware of kind of the strategic moves that Intel is making in the AI space and what they're focusing on.
[251.50 --> 261.18]  Ben, I'm wondering if you could give us a little bit of a high level sense of what Intel is doing as related to AI and how that's kind of featuring in their strategy right now.
[261.46 --> 268.78]  Yeah, no, I think a lot of people don't know Intel in terms of our, you know, our strategy with AI.
[268.78 --> 271.90]  And so I'm happy to talk through that a little bit.
[271.90 --> 282.02]  So, you know, both in terms of hardware and software, we're really aimed at AI, you know, with in terms of the hardware front, which people are more perhaps more familiar with.
[282.02 --> 293.46]  We have our Xeon product line, which is, you know, a data center CPU that we use for inference in a lot of cases for AI workloads.
[293.46 --> 309.58]  And then more recently, we've, you know, announced the AI PC and kind of started that whole category, which includes, you know, the machine has a CPU, a GPU, and then what's called an NPU, a neural processing unit.
[309.58 --> 312.06]  And so that's exciting.
[312.20 --> 316.14]  That's kind of to optimize workloads on your local machine.
[316.54 --> 329.54]  And then back to the data center side, we have the Gaudi product line, which is really a really good performance substitute for a lot of the modern, you know, GPUs that are out there.
[329.54 --> 335.22]  So that's really exciting as well, really powerful data center hardware that we have.
[335.76 --> 338.54]  So that covers some of our hardware.
[339.44 --> 351.34]  I guess the other big one that I want to emphasize as well is we have Falcon Shores coming out in the future, which is an all purpose, you know, GPU, a data center GPU as well.
[351.34 --> 358.26]  So kind of leading into that is Gaudi, and we'll get more into that in the episode.
[358.48 --> 362.70]  But on the hardware front, we have, you know, multiple products for AI.
[363.10 --> 364.26]  So that's really exciting.
[364.48 --> 375.26]  And then on the software front, there's, you know, Intel, again, spans kind of the whole gamut of software for AI, for enabling workloads in AI.
[375.26 --> 382.04]  But rather than kind of going through the whole software stack that we have, I'll just talk about a couple things that I'm excited about.
[382.70 --> 389.84]  So the PyTorch 2.4 release, you know, includes support for the Intel GPU.
[390.42 --> 395.42]  So right now is the Mac series GPU and will be Falcon Shores.
[395.68 --> 403.22]  So that's really exciting that the upstreamed, you know, mainstream version of PyTorch has now support for that.
[403.22 --> 411.98]  And then coming soon, PyTorch 2.5 will have support for the Arc GPU, which forms a part of the discrete GPU product line that we have.
[412.12 --> 414.24]  And that's also included in the AI PC.
[414.92 --> 418.40]  So those are a couple of exciting things with PyTorch that are happening.
[419.30 --> 424.46]  And then we also have the OPEA ecosystem.
[424.86 --> 428.48]  That's the open platform for enterprise AI.
[428.48 --> 444.82]  And it's kind of this open framework that we have that multiple people can contribute to for Gen AI workloads, such as chat Q&A, code copilot, and different other Gen AI examples.
[445.32 --> 449.42]  So yeah, those are a few of the things that I'm excited about on the software front.
[449.42 --> 455.76]  I'm wondering if you could talk a little bit about how Intel is uniquely positioned in the AI landscape.
[455.76 --> 458.54]  You have both some very large competitors out there.
[458.68 --> 461.30]  There's a bunch of smaller ones in the space.
[461.38 --> 463.04]  How do you guys see yourselves?
[463.42 --> 467.12]  And what's your, you know, how do you approach that point of differentiation?
[467.56 --> 467.82]  Yeah.
[467.82 --> 476.80]  So, you know, I think where we can really compete well in this space is, you know, cost and performance, like, and availability.
[477.28 --> 484.90]  So when, you know, you're running out of availability or don't have the ability to rent that GPU you need from the cloud from NVIDIA.
[485.46 --> 490.94]  And, you know, you need something cheaper that also, yeah, runs AI workloads really well.
[491.16 --> 496.50]  I can, yeah, say with confidence there are some good options coming out of Intel that I've used personally.
[496.50 --> 502.44]  And, you know, I come from a background in AI engineering where I was only using NVIDIA GPUs.
[502.50 --> 511.56]  And I have gotten to work at Intel and to, you know, to try out our Gaudi products for training AI, you know, deep learning AI models.
[511.80 --> 523.04]  And then I've also gotten to run inference on our Xeon products and even run training as well on our Xeon data center products quite a bit to do more fine tuning.
[523.04 --> 537.70]  So, yeah, I would position Intel in terms of those things, just being able to have good options for, you know, out of the box performance hardware that people might not be aware of.
[538.56 --> 538.64]  Yeah.
[539.12 --> 542.62]  Could you take just a moment, just a quick follow up to what you were saying?
[542.62 --> 552.10]  You brought up the big competitor being NVIDIA out there and a lot of folks out there, just as you were, had been on their hardware using their GPUs and such.
[552.32 --> 554.36]  What was, you talked about that transition.
[554.90 --> 567.26]  Could you talk a little bit about what is it like coming over to Intel when historically maybe you were on NVIDIA as a platform and you guys are now coming, you know, as a real powerhouse.
[567.26 --> 573.62]  What does that migration and transition look like and feel like if you decide to go for that?
[574.00 --> 584.68]  Yeah, no, I think I can relate in terms of my background in, you know, in deep learning as I was first working on with TensorFlow and then with PyTorch mainly.
[584.94 --> 592.90]  And then now since I've been at Intel, there's been a lot on, you know, Hugging Face and Transformers and those libraries as well.
[592.90 --> 597.56]  And what I'd say in general is that the transition is not difficult.
[598.32 --> 610.54]  You know, a lot of the same tools that I'm used to using for development on the NVIDIA platforms, I can use those same tools with some slight code modifications for the Intel products.
[610.82 --> 614.70]  So in terms of like a software leap, it hasn't been too difficult.
[614.70 --> 629.38]  And Intel actually historically has had, we have both the upstream support into those, you know, those frameworks where we have our own developers and the community developing for Intel in the, you know, in the mainstream frameworks.
[629.56 --> 633.92]  But we've also in the past had, you know, Intel extensions where there are gaps.
[633.92 --> 642.54]  So for example, you know, Intel has had Intel extension for PyTorch where, you know, there's not yet support in the mainstream framework.
[642.54 --> 650.64]  You can, you know, install this extra package to get, you know, all the support that you need, again, with just a couple lines of code change.
[650.80 --> 660.28]  But we're constantly aiming to get our, you know, our changes into the, you know, into the mainstream framework so that it's just easy for developers to use.
[660.28 --> 668.20]  But yeah, in terms of software development, I haven't had huge obstacles for, you know, transitioning over to different hardware.
[668.88 --> 684.56]  Yeah. And you mentioned kind of some of those, those important open ecosystem projects, whether that be things that Intel is maybe driving more directly, like the OPEA stuff, or it's kind of more community things.
[684.56 --> 704.54]  Greg, I know being kind of developer ecosystem manager for part, I know you're focused more on the Gaudi side, but we were talking before the show even about like our team is utilizing a lot of these great, great packages that actually aren't even in, you know, an Intel repository on GitHub.
[704.54 --> 717.38]  There may be a big one that we've used, but there's other frameworks like TGI, I know that are important for what Intel is trying to do.
[717.38 --> 732.46]  So maybe we'll, of course, get into more details later, but just at that kind of open source level for those out there that are not only wanting to utilize these great packages, but also contribute to them.
[732.94 --> 735.82]  How has Intel engaged in that open source community?
[736.28 --> 740.84]  Right. The key thing here is wanting to maintain as much of that connection with the open source.
[740.84 --> 750.74]  And this really started with, with Gaudi when the project was introduced four years ago, where we started with TensorFlow and PyTorch and now we've moved, you know, the industry has moved to PyTorch and so have we.
[751.52 --> 757.06]  And as Ben said, our, our goal here is to have full PyTorch support in native PyTorch.
[757.14 --> 758.16]  So we're working towards that.
[758.56 --> 763.30]  The same thing with, with DeepSpeed and with Megatron DeepSpeed for large language models.
[763.80 --> 768.10]  So we, we engaged with the full ecosystem to support those things.
[768.10 --> 771.74]  So we can talk specifically about our support for PyTorch.
[771.92 --> 778.08]  So a customer can run their PyTorch models and migrate them directly onto Gaudi.
[778.52 --> 792.98]  And so, for instance, we have a tool that takes a model that maybe was running on a GPU architecture and in real time migrate some of those things and move some of that code that was for GPUs and change them over to things that, that Gaudi can understand.
[792.98 --> 798.10]  But the key thing is if you're running on PyTorch, you can bring your PyTorch models over to Gaudi.
[798.56 --> 809.20]  If you've been using Optimum, if you've been using Hugging Face, we've partnered very closely with Hugging Face and have a dedicated library called Optimum Havana or Optimum for Intel Gaudi.
[809.20 --> 824.90]  And that is a dedicated set of fully performant and fully documented examples of Lama 2, Lama 3, OPT, Minstrel, Mixtrel, all the important models that people are using today for both fine tuning and inference in Hugging Face.
[824.90 --> 830.22]  So if you're taking advantage of using Hugging Face, then it's really easy to bring those models over.
[830.76 --> 845.60]  And then we look at, again, for training, we have our partnership with, we're using DeepSpeed, specifically using Megatron DeepSpeed, which is really optimized for doing those large scale, large language model training,
[845.60 --> 857.44]  where we're taking advantage of the tensor parallelism, pipeline parallelism, and data parallelism that Megatron provides to be able to really get customers to scale and start using our product very quickly and very easily.
[857.44 --> 875.46]  I know one of the things that was really cool for me, and I know a lot of people have been working on this and contributing a lot, but I just love the, because the reality for us when we were building Prediction Guard is we had a bunch of transformer-based code running.
[875.46 --> 892.70]  And one of the things I liked about the examples when I was trying out this stuff was you sort of had the example of loading a model in with Optimum or with Transformers and then kind of the after, and it was just sort of like you'd see a Git diff in a repo.
[892.92 --> 898.40]  It's like, hey, change this line to this line, and then you're basically pretty good to go.
[898.40 --> 913.40]  I remember I was actually on a plane to India during like a hackathon back last June and had got access to some of these Gaudi hardware, these Gaudi processors in Intel Developer Cloud.
[913.60 --> 916.40]  And I remember doing that and going through those examples.
[916.70 --> 927.46]  And by the time I had landed in Bangalore, I had the models up and running on the Gaudi processors for what we needed to have, which was pretty cool.
[927.46 --> 938.54]  So yeah, great work to you all and the whole team in terms of providing some of that sort of functionality and tying in very closely with that ecosystem.
[939.10 --> 950.36]  Yeah, it's really important that, you know, because Hugging Face is so huge and so pervasive, we wanted to make sure it was really easy for people to migrate over and just even take advantage of the models that we have already optimized.
[950.36 --> 962.58]  You know, so a lot of the work we do there is really managing at the lowest level of managing some of the static shapes and managing the bucketing and making sure that we have the most optimized models.
[962.74 --> 965.82]  And as you said, Daniel, they're fully documented, right?
[965.82 --> 984.18]  So it's really easy for people to go into the repository on GitHub and you will see examples of running something as simple as doing text generation with GPT on one card or going and running full, a full Llama 3 70 billion parameter model on eight cards.
[984.18 --> 990.80]  Or if you have access to more nodes up to 16 or 32 cards and everything is fully documented.
[990.98 --> 994.74]  So like you say, you get off the plane and you're already running.
[995.02 --> 1009.96]  And it's a great starting point for people to begin their development, either to take, you know, their existing model and fine tuning it with Gaudi and taking advantage of that performance or being able to run inference and applying that to their applications.
[1009.96 --> 1012.04]  Just like, like you've done with prediction guard.
[1012.24 --> 1018.14]  So we've, we've kind of dived into talking a bit about Gaudi, but I'd like to, I'd like to pull us back.
[1018.22 --> 1039.94]  And for those of us that are out there listening and are not familiar with it, could you possibly kind of give us a, a, what is Gaudi and kind of introduce the whole platform in the, in the broad and talk about kind of where it came from, how it came about, you know, what Gaudi is versus maybe some of the other things that Intel.
[1039.94 --> 1045.56]  Has that are not specifically Gaudi and just kind of give us a context setting about what Gaudi looks like.
[1046.02 --> 1047.04]  Yeah, Chris, that's a great question.
[1047.56 --> 1054.02]  So let's talk a little bit about what Ben has mentioned a moment ago about the overall Intel product roadmap.
[1054.48 --> 1056.98]  And you look at sort of three key areas.
[1057.18 --> 1062.12]  You think about the PC and we have the AI PC that Benjamin was talking about.
[1062.12 --> 1068.62]  Then we have the edge where we, you know, the edge has huge latency requirements and performance requirements.
[1068.84 --> 1075.94]  And there's great solutions there with, with Xeon to, to handle those low latency, you know, on-premise requirements.
[1075.94 --> 1096.54]  And then the final is, is really that large language model training and inference in the data center where we're looking at fine tuning and pre-training models, as well as running inference on large batch loads or batch sizes or, or large batches or dealing with users that running application where we have multiple, multiple, multiple users trying to take advantage.
[1096.54 --> 1105.14]  And the reason why we have Gaudi and the reason why Gaudi exists really is to give the ecosystem a choice.
[1105.70 --> 1116.94]  One thing we've been hearing from customers over and over is they want an alternative to the standard mainstream GPU solutions because of cost and because of availability.
[1117.48 --> 1124.38]  So Gaudi really is that low cost alternative to the standard NVIDIA GPU solutions that are in the market today.
[1124.38 --> 1135.44]  So in a little bit of a history, the company Habana was an independent company and Intel really saw the value in, in the product they were building the performance.
[1135.72 --> 1143.10]  So Intel made an initial investment in 2016, 2017, and then fully purchased the company in 2019.
[1143.68 --> 1146.94]  So it was a small company and they really needed to scale.
[1146.94 --> 1153.12]  So Intel invested in the company and brought them inside of Intel and brought many Intel employees.
[1153.28 --> 1157.74]  I was one of them into the structure within, within the Gaudi team.
[1158.14 --> 1161.06]  So we started to build the product and started to ship.
[1161.20 --> 1166.02]  And so the first real milestone there was launching the first generation of Gaudi on AWS.
[1166.40 --> 1169.62]  So today that's available in the DL one instance on AWS.
[1169.62 --> 1170.82]  It's still available today.
[1170.82 --> 1176.06]  And the next step was in Gaudi 2 and Gaudi 2 launched a year and a half ago.
[1176.26 --> 1184.44]  And one of the key real key milestones with Gaudi 2 was the submission for MLperf on training and inference.
[1185.36 --> 1195.98]  And, you know, you look at, for those that don't know, MLperf is, is a benchmark that the larger ecosystem uses today to measure these really standardized benchmarks.
[1195.98 --> 1203.18]  And so the way that you run those MLperf benchmarks makes it easy to have a direct comparison from product to product.
[1203.84 --> 1210.16]  And one of the really key benchmarks was the large language model training benchmark for MLperf.
[1210.54 --> 1218.32]  And Gaudi was one of the only products other than NVIDIA that submitted an actual benchmark for MLperf, showcasing the performance.
[1219.12 --> 1220.40]  So why Gaudi?
[1220.54 --> 1221.24]  What is Gaudi?
[1221.42 --> 1222.64]  Is Gaudi a GPU?
[1223.50 --> 1225.08]  No, Gaudi is not a GPU.
[1225.08 --> 1236.60]  It is a dedicated AI processor that is used to manage and train and run inference on today's largest and most complex workloads for both training and inference.
[1237.16 --> 1245.90]  Could you differentiate a little bit for me as I'm learning as we go here, when you say a dedicated AI processor versus a GPU, could you kind of distinguish between those?
[1246.30 --> 1251.98]  Well, from a, you know, in some cases, a GPU still has the ability to do some other things.
[1251.98 --> 1256.72]  You know, it's got additional programmability to do other types of workloads.
[1257.06 --> 1264.22]  Whereas Gaudi as a dedicated AI accelerator is built specifically for AI training and inference.
[1264.86 --> 1268.84]  So we don't have those additional, it's specifically built for AI.
[1268.84 --> 1279.50]  So it's a product where if you're wanting to go run these workloads in the cloud, on the edge, or in an on-premise solution in your on-premise data center, Gaudi really is that low-cost solution.
[1279.92 --> 1290.40]  As an analogy with a potential competitor that people may know just to transition, Google has their TPUs, which sound sort of similar to that, where it doesn't have all the extra stuff that a GPU has.
[1290.40 --> 1296.78]  Is it, and I get Gaudi as its own thing, but is it just for people to make that connection a little bit similar to that?
[1297.10 --> 1298.02]  Yeah, it's somewhat similar.
[1298.22 --> 1306.68]  And, you know, I had one more thing that really is a great differentiator in Gaudi is, as part of the hardware architecture, we provide two things.
[1306.68 --> 1312.86]  One is 96 gigabytes of on-board, on-card HBM memory.
[1313.44 --> 1328.36]  And for those in the audience that really know about training and inference, having that local HBM memory is critical for storing your weights or your parameters, the things that actually are stored when you're actually running the inference or running the training.
[1328.36 --> 1333.26]  So having that large HBM memory allows you to do one of two things.
[1333.36 --> 1339.42]  You can either run a larger model on a single card, or you're more efficient as you scale out to more cards.
[1340.16 --> 1344.84]  And the other thing that really is a key differentiator for Gaudi is the on-board networking.
[1345.70 --> 1351.72]  So on DAI, Gaudi offers 24 100 gigabit Ethernet ports.
[1351.72 --> 1371.92]  So instead of relying on the latency of having to use a third-party network controller to scale to multiple nodes in a rack, for example, these dedicated Ethernet ports allow, in some cases, a direct all-to-all connection for eight Gaudis in a node or a single server.
[1371.92 --> 1383.36]  And then the additional Ethernet ports then can go to the other nodes in a rack and then scale out to a switch to go to multiple nodes and then a full pod.
[1383.54 --> 1392.22]  So what you end up with is a virtual all-to-all connection, which significantly improves the scalability when looking at large workloads.
[1392.22 --> 1411.20]  Ben, you were talking a little bit about your prior work in deep learning, in training models, and doing inference, and how you've transitioned a bit and also done some projects with training on Gaudi and various other hardware that we've already talked about.
[1411.20 --> 1426.98]  Could you speak a little bit more to that practical side and just to give people a sense of the kinds of projects that are possible on this hardware, just so they can form in their mind both the scale and possibilities with what can be done?
[1427.50 --> 1428.00]  Yeah, no.
[1428.00 --> 1441.48]  Well, and my use cases might not be the full expanse of what's possible on our hardware, but I can certainly speak to the things I've been able to work on and had some fun with over the last few years.
[1442.30 --> 1455.14]  So one of them is working with OpenAI's Whisper model, which is a translation and transcription model that works very, very well out of the box.
[1455.14 --> 1458.06]  And so I speak both English and French.
[1458.16 --> 1469.72]  And so I tested this, you know, the abilities of this model, you know, to transcribe my own voice, English to English, and then also its ability to transcribe from English to French and then going the other way as well.
[1470.30 --> 1472.76]  And yeah, first of all, the model does a really great job.
[1472.80 --> 1479.42]  I was really impressed with the fidelity of the model that's been trained that OpenAI has released in the open source.
[1479.42 --> 1494.30]  So that's great. And then what I was able to do was to run this model, you know, on our Xeon product line to run inference on Xeon and run that really, really quickly and kind of put together a notebook and a workshop around that.
[1494.30 --> 1505.18]  So that's been something that's been fun for me to work on, on this generative AI model that is, you know, used for translation and transcription.
[1505.76 --> 1506.98]  Yeah, that's one.
[1506.98 --> 1533.68]  Another one that has been exciting for me to work on is with my, I have a background in imaging and computer vision kind of prior to working at Intel, where I was applying a number of different techniques like pixel segmentation and image classification, object detection to different problems in computer vision, especially around geophysical imaging, where we're imaging the subsurface.
[1533.68 --> 1537.64]  So I kind of describe it like an ultrasound for the earth.
[1537.86 --> 1547.22]  So if you know what an ultrasound is, looking at imaging, you know, the subsurface of the earth to try to find, extract and find certain minerals and that kind of thing.
[1547.40 --> 1560.38]  So where I've applied some of the techniques there is to help, you know, get some of those images more quickly and both in fine tuning models and also in inference.
[1560.38 --> 1569.84]  And so I've been able to use, you know, some of our Xeon again, product line to fine tune some of those models as well as run inference.
[1570.14 --> 1571.92]  So that's, that's been exciting.
[1572.60 --> 1572.72]  Yeah.
[1573.12 --> 1575.44]  You know, I'll add this to, just to add onto that.
[1575.64 --> 1582.12]  One area that's really getting a lot of focus now is, is the use of RAG, retrieval augmented generation.
[1582.38 --> 1584.36]  We've invested a lot of effort there.
[1584.36 --> 1597.64]  You'll see that in the OPEA project where we have a lot of RAG based examples, but not only for just general RAG usage, which is important, but also transitioning into multimedia.
[1597.64 --> 1607.42]  So we're, we're seeing a huge request for, and we see this in the market for both video, audio and text all coming together.
[1607.42 --> 1624.70]  So whether it's a prompt of, of text to get a picture or a prompt for text to get now a video or to use a RAG type of usage to be able to parse through not only text, but parsing also through video and then get a response.
[1624.70 --> 1630.98]  So those are all of the, so types of things that we have available for use on Gaudian and the products.
[1630.98 --> 1634.40]  Yeah. And actually that's something I'll pick up on too.
[1634.98 --> 1648.92]  Cause yeah, I've been working on some multimodal, you know, models on the AIPC actually running, running some multimodal smaller, you know, 2 billion parameter multimodal models.
[1648.92 --> 1660.34]  Um, and actually successfully ran one on the NPU, the neural processing unit to, to run inference and to extract essentially some information about an, an image, um, into text.
[1660.34 --> 1662.98]  So using that multimodal capability.
[1662.98 --> 1692.96]  Hey friends, outshift Cisco's incubation engine merges innovation with the art of possible, a launch pad for transformative emerging tech outshift blends startup agility with corporate strength to develop next gen technologies from the ground up in AI quantum technologies.
[1692.96 --> 1694.96]  Cloud native and more.
[1694.96 --> 1695.96]  Their newest AI innovation.
[1695.96 --> 1696.96]  And more their newest AI innovation.
[1696.96 --> 1705.82]  Motific addresses a critical challenge in the rapidly advancing world of gen AI, bridging the gap between concept and deployment.
[1705.82 --> 1713.82]  This model and vendor agnostic solution supports the entire gen AI journey from assessment and experimentation.
[1714.70 --> 1731.64]  Motific accelerates deployment from months to days while safeguarding against gen AI security, trust, compliance, and cost risks, all while empowering business function and IT teams to rapidly configure end user assistance powered by organizational data.
[1731.64 --> 1741.98]  Motific provides advanced, customizable policy controls to prevent unauthorized access to sensitive data and helps ensure compliance throughout the entire process.
[1742.28 --> 1751.78]  With deep visibility into operational and business metrics, Motific enables you to track ROI, optimize costs, and make informed decisions.
[1751.78 --> 1759.72]  By offering a centralized view, Motific deters shadow AI usage and empowers teams to innovate responsibly.
[1760.20 --> 1776.32]  So move beyond the traditional constraints of AI implementation, utilizing AI deployment that is both responsible and is revolutionary, ensuring your projects are not just quickly launched, but built on a foundation of trust and efficiency.
[1776.32 --> 1778.68]  Visit Motific.ai.
[1778.94 --> 1783.46]  That is M-O-T-I-F-I-C dot A-I.
[1795.88 --> 1803.78]  So Ben and Greg, we've talked about a lot of interesting things, both on the kind of software and migration side,
[1803.78 --> 1806.70]  but also on the hardware and what that hardware enables.
[1807.18 --> 1811.00]  People might though be out there and be wondering, this is cool.
[1811.10 --> 1812.64]  I'd love to experiment with this stuff.
[1812.88 --> 1818.12]  How can I get hands-on with some of this hardware that I'm hearing about?
[1818.58 --> 1826.80]  What are some of those ways that people can, they might have an Intel processor in their PC or likely many do,
[1826.96 --> 1831.24]  but they don't have a Gaudi or a Xeon sitting around at the moment.
[1831.24 --> 1838.82]  So if they were to want to kind of explore this ecosystem and get hands-on, try some things, how might they do that?
[1839.12 --> 1839.80]  Yeah, I can start.
[1839.92 --> 1843.04]  And then Greg, you can fill in anything, Greg, that I'm missing.
[1843.20 --> 1850.22]  But I think the best way is to get onto the Intel Tiber developer cloud, which is a way,
[1850.22 --> 1858.74]  it's kind of our Intel cloud where developers can come and try out both our hardware and our software that's set up right there for them.
[1858.90 --> 1863.68]  And we'll offer kind of our latest, whatever we have, you know, on that platform.
[1863.90 --> 1867.26]  So we'll offer, you know, we have our Xeon product, we have our Gaudi product.
[1867.26 --> 1873.18]  We even are going to be having like a dev kit kind of for the AIPC, a simulated environment,
[1873.28 --> 1876.26]  even though it's not a, you know, a local machine, it's still a cloud.
[1876.46 --> 1880.56]  So that's, I think, the best way to get started is the Intel Tiber developer cloud.
[1880.68 --> 1882.58]  And Greg, did you have anything to add there?
[1882.74 --> 1883.98]  That is the best way.
[1884.12 --> 1888.72]  You know, we're going to have some pretty soon some free access to Gaudi.
[1888.86 --> 1890.78]  So right now you need a developer credit.
[1890.78 --> 1896.16]  We're working to get some nodes available for free on the developer cloud.
[1896.26 --> 1900.52]  So people will have the ability to try out our tutorials and examples and code examples
[1900.52 --> 1905.68]  and be able to see and experience the Gaudi usage and see how easy it is to run.
[1906.28 --> 1906.92]  Yeah, that's awesome.
[1907.06 --> 1912.62]  And I mentioned earlier some of the experimentation on my end, even on the plane.
[1912.80 --> 1915.62]  But a lot of that was enabled by this developer cloud.
[1915.62 --> 1921.46]  And I think there are, you all can correct me if I'm wrong, but people can sign up on the site,
[1921.58 --> 1926.06]  get access to, and there's also some like training resources.
[1926.40 --> 1928.84]  People can spin up notebooks, try a variety of things.
[1929.00 --> 1933.14]  Maybe if they're not as familiar or they're learning, get access to various things.
[1933.32 --> 1938.40]  But there's also a kind of transition to, within that environment,
[1938.66 --> 1944.98]  utilize these powerful products in a production sense or in an enterprise sense,
[1944.98 --> 1949.44]  rather than just a kind of developer experimentation sense,
[1949.52 --> 1954.38]  which is definitely the transition that Prediction Guard has taken.
[1954.66 --> 1961.00]  So we've been able to operate very price performant at scale with our LLM engine AI platform
[1961.00 --> 1966.10]  on top of Gaudi and running that in Intel Tiber Cloud.
[1966.68 --> 1968.64]  So I don't know if there's anything you'd want to highlight,
[1968.76 --> 1974.34]  whether that be kind of success stories or just commenting on that kind of transition
[1974.34 --> 1979.68]  to production, that there kind of are people running this stuff in production,
[1980.18 --> 1983.46]  not just in a kind of developer experimentation sense.
[1983.56 --> 1984.90]  Anything you'd want to highlight there?
[1985.52 --> 1986.60]  Yeah, Daniel, that's a great point.
[1987.02 --> 1990.64]  You know, the Tiber Developer Cloud is really meant to do two things.
[1991.12 --> 1994.88]  One is just to give people the access to our products.
[1994.88 --> 1999.36]  And so they have the ability to experience and run them and test them.
[1999.80 --> 2004.44]  But Daniel, to your point, it is also a place for people running a business
[2004.44 --> 2008.38]  to be able to have really easy access to our products as well.
[2009.20 --> 2015.54]  And specifically with Gaudi, you know, we're enabling customers now with very large scale out
[2015.54 --> 2019.84]  to be able to do full production workloads and use the Tiber Developer Cloud
[2019.84 --> 2021.26]  as a baseline for their business.
[2021.26 --> 2027.98]  So we invite those, you know, listening to be able to reach out to your sales contacts
[2027.98 --> 2034.06]  in Intel and really be able to talk about how we can help those people really using this
[2034.06 --> 2036.12]  for business to be able to scale as a real product.
[2036.62 --> 2041.46]  And also, as we look to, you know, Gaudi 3, which is our new product that we've announced
[2041.46 --> 2047.54]  at previous events, and we're going to make a very large announcement at Intel Innovation
[2047.54 --> 2053.62]  in September, is really, that's also going to be a place where we'll see Gaudi 3 also begin to scale.
[2054.08 --> 2062.20]  So it's definitely a place where it makes it easy to partner directly with Intel or with partners in the future.
[2062.20 --> 2068.94]  Yeah, I'm curious on whether it is existing or maybe a roadmap item.
[2068.94 --> 2076.94]  Could you talk a little bit about Gaudi at the edge and when you're not in the cloud and you're out maybe wanting to use Gaudi
[2076.94 --> 2082.48]  in devices that are out there or platforms that are out moving about, what's the roadmap look like on that?
[2083.14 --> 2083.26]  Right.
[2083.36 --> 2088.94]  So going forward, we're going to, so today it is a, you know, OCP compliant part.
[2089.06 --> 2090.78]  So it's on a mezzanine card.
[2090.96 --> 2093.46]  So it's meant for data center, right?
[2093.46 --> 2099.36]  So today the Gaudi platform is in a, you know, 6U or 8U rack mount server.
[2099.90 --> 2101.40]  That's the form factor it has today.
[2102.06 --> 2106.80]  And that OCP form factor of spec is eight Gaudis on a single baseboard.
[2107.18 --> 2114.74]  And as you noticed, if you may have noticed at Intel Vision a few months ago, we announced full packages that you can buy.
[2114.80 --> 2120.54]  So you can buy a Gaudi 2 baseboard or a Gaudi 3 baseboard that has the full baseboard that's OCP compliant.
[2120.54 --> 2125.20]  So you can drop that into a chassis from Supermicro or WeWin or other products.
[2125.74 --> 2130.50]  But in the future, we're also going to have a standalone PCIe card that will be available.
[2131.02 --> 2135.72]  And that's going to be exactly for those type of more on-prem sensitive solutions.
[2135.90 --> 2142.08]  Chris, like you said, at the edge where people can take advantage of a single Gaudi 3 and its capability on the edge.
[2142.20 --> 2144.04]  So you'll see that PCIe card coming soon.
[2144.62 --> 2144.70]  Yeah.
[2144.70 --> 2149.06]  And maybe that's a good transition to talk a little bit.
[2149.26 --> 2158.22]  Like we've talked a lot about the things that are kind of the now of what's available and kind of tooling or hardware wise with Intel.
[2158.52 --> 2164.16]  But both of you have alluded to kind of the future to one degree or another.
[2164.38 --> 2167.02]  So maybe, Ben, I'll start with you.
[2167.02 --> 2174.36]  But I know you mentioned certain things, whether it be the Falcon Shores or some cool things that are happening with AI PCs and that sort of thing.
[2174.50 --> 2190.80]  But what kind of strategy wise and kind of positioning wise is Intel really thinking about and investing in moving kind of into the next phase of what AI is becoming and where Intel thinks the market is going, I guess?
[2190.80 --> 2192.36]  Yeah, no, thanks.
[2192.92 --> 2199.48]  Probably the best place to start on this is and what I'm excited about is Falcon Shores, like you pointed out.
[2199.68 --> 2211.48]  So Falcon Shores will be kind of the culmination of combining the Gaudi product line with the GPU, with our current Max series GPU.
[2211.48 --> 2215.94]  And it will be a GPU graphics processing unit.
[2216.00 --> 2225.48]  So it will be a full GPU capable of not only the AI workloads, but also graphics and other applications that people want to use GPUs for.
[2225.64 --> 2234.62]  And so I think that's probably the most exciting thing that we're kind of aiming at, that we know the market needs.
[2234.62 --> 2238.86]  And then, yeah, iterations on the, as you mentioned, the AI PC.
[2239.66 --> 2247.78]  So we'll be in the future, we'll also have a new, more powerful AI PC with the Lunar Lake chip coming out.
[2247.96 --> 2263.54]  And again, it will include the CPU, GPU, NPU, but it'll be a much more powerful, more memory form factor that where developers will get even more out of their local, you know, their local machine.
[2263.54 --> 2266.68]  So, yeah, those are, those are a couple of things.
[2266.80 --> 2277.72]  And then the other thing that I'm excited about just as an AI software developer myself is the integrations with, like, like I pointed out at the beginning, the integrations with PyTorch.
[2277.72 --> 2294.28]  Like, I think it's huge that we're aiming at getting all of our, you know, our optimizations and our everything we can into this, this framework that is, you know, by far one of the most popular deep learning frameworks and one that I use on a regular basis.
[2294.28 --> 2307.82]  So that's, that's really exciting to me as well, that just natively, I'll be able to, you know, work with PyTorch and say, hey, I want to use the XPU, which is, you know, for the, for the Intel, Intel GPU.
[2308.20 --> 2311.86]  And, and same with the AI PC, just have that direct integration.
[2312.22 --> 2316.82]  So, yeah, those are, those are a couple of things that are exciting for me coming out soon.
[2316.82 --> 2321.34]  And I'll add to that to say, you know, the key, the key thing here is forward compatibility, right?
[2321.40 --> 2331.14]  So people that are using our products today saw specifically speak to Gaudi, you know, if you're running workloads on Gaudi two, you'll be able to run those workloads directly on Gaudi three.
[2331.46 --> 2335.16]  And that same architecture will, will move forward into Falcon Shores.
[2335.50 --> 2339.10]  So people that make their, their technological investments.
[2339.10 --> 2343.86]  Now, those will remain viable and relevant far into the future.
[2343.86 --> 2359.64]  Yeah. And I guess one other piece of this, which, you know, Greg, you, you mentioned kind of in passing the, one of the things that, that people are really interested in with, with Gaudi, of course, is the fact that there's some diversity in the market.
[2359.88 --> 2363.24]  And there's another choice, right, for hardware out there.
[2363.24 --> 2373.94]  I think one of the other interesting things that I don't know if, I know you, you two are kind of only in, in pieces of, of Intel and focused on certain things.
[2373.94 --> 2387.42]  But I found it really interesting how, how Intel is very much investing in chip production kind of diversity as well outside in, in various geographies around the world as a key part of their business.
[2387.42 --> 2400.48]  And I don't know if you have any comment on that or, or thoughts on, on how that influences the, the market as a whole and availability or supply chain sorts of robustness that that could build in.
[2400.62 --> 2408.78]  But I know we've seen, you know, we've seen some interesting things over the years, both in terms of availability and supply chain issues with, with hardware.
[2408.78 --> 2413.50]  Yeah. And you could talk about, let's talk about this at a, at a macro level and maybe at an AI level, right?
[2413.56 --> 2425.78]  At a, at a macro level, you look at what, what our CEO, Pat Gelsinger has talked about when we promoted the Chips Act, for example, that we, we need, Daniel, to your point, we need that, we need to be able to build that infrastructure worldwide.
[2425.78 --> 2442.90]  So you can see from an Intel perspective, our investments in our fab in Ohio and our fabs in, and now in Germany, as well as just our fab worldwide, we have that worldwide capability to support significant growth and expansion as the world continues to need more and more silicon.
[2442.90 --> 2452.46]  From an AI perspective, you know, the, the growth and the need for AI compute is insatiable and will continue to be that way for the foreseeable future.
[2453.22 --> 2459.20]  So again, this goes back to, you know, why we've invested in, in Gaudi and brought that as a product as part of Intel.
[2459.98 --> 2471.00]  And as part of just growing the broader AI portfolio, we really want to be able to give the ecosystem an alternative to getting access to AI compute as they need it today.
[2471.00 --> 2483.30]  So as, as we start closing up, I would, I would really love to hear kind of from each of you and you guys can decide who wants to, to go first, but kind of where, where do you see it going?
[2483.30 --> 2498.24]  Where Gaudi is going and where the overall ecosystem and these technologies are going and just, you know, kind of, this is a moment where you can kind of take a little bit of poetic license and speculate a bit.
[2498.24 --> 2506.74]  I would love to see what you think will unfold and happen in the times ahead and, and, and how each of you may see it a little bit differently as individuals.
[2507.20 --> 2508.84]  Sure. Yeah, I can, yeah, I can start.
[2509.04 --> 2522.02]  So I think, yeah, just looking at kind of AI broadly and, and, you know, what's happening, it, it, it seems like things progress with these incremental, you know, these incremental changes.
[2522.02 --> 2526.02]  And sometimes there's a leap, but there's, there's often just these incremental changes.
[2526.02 --> 2534.72]  And one of the questions I, I often get from friends, maybe you guys do too, as you're working in AI is like, you know, is AI going to take over?
[2534.72 --> 2538.76]  And, you know, are we going to have kind of robots controlling everything we do?
[2538.98 --> 2543.88]  And, you know, so that's, that seems to come up a lot as I, as I say that I work in AI.
[2544.02 --> 2554.80]  Sometimes I regret saying I work in AI and just say, I should just say software engineering, but, but, but no, it's, it's, it's always an interesting conversation that I have with, with different friends.
[2554.80 --> 2565.42]  And, you know, my perspective is, is that like the internet, the, the, the coming of the internet, AI has come along and has changed the way we work and changed the way we operate.
[2565.42 --> 2570.78]  But just like the internet, we have people behind building these things.
[2571.46 --> 2583.04]  And as, you know, these technologies evolve, you know, we, we will have safeguards and we will have things in place to, to help, you know, regulate, you know, the, the different technologies of AI that come out.
[2583.04 --> 2596.92]  And, you know, lately with the AI agents, I think is one of the, you know, the most recent things where you have the agent kind of do more things for you than, than maybe previously where you had to ask it to do more things.
[2596.92 --> 2607.76]  So that's been a really interesting part of AI that's, that's kind of come out and, and that I think is going to see a lot more adoption in the future to, you know, to answer your question about the future.
[2607.76 --> 2621.16]  I think just getting the AI tools to, to build more things and to be able to kind of do more complex tasks in sequence is something that's, that's evolving and happening.
[2621.52 --> 2621.96]  Yeah.
[2622.00 --> 2624.18]  Greg, did you have some more to add?
[2624.56 --> 2629.86]  There's, I'd love, I'm so excited about the personal, personalization of AI.
[2629.86 --> 2639.26]  You know, I see cases where now things we didn't have when we went to college, but now, you know, you can have your phone or your AI PC open in your college classroom.
[2639.26 --> 2647.82]  And, you know, the AI will summarize and, and create notes for a lecture or quiz you on a lecture and create all that content for you automatically.
[2647.82 --> 2648.62]  I love that.
[2648.62 --> 2657.74]  I want to see AI do better with my email and be able to organize my email better, do searches better, make my life better.
[2657.94 --> 2660.74]  Those are things I'm really excited to see from a general perspective.
[2661.46 --> 2673.10]  You know, from an Intel perspective, I think you're, you're going to continue to see us lean in on giving customers what they need, which is being able to have more and more compute for, for fine tuning.
[2673.10 --> 2679.74]  And for, for inference, be either on-prem or on the edge, supporting the world's largest models.
[2679.74 --> 2683.86]  And as we see, you know, innovation happening on a monthly basis that used to take a year.
[2684.06 --> 2685.30]  Now we're on a monthly basis.
[2685.86 --> 2687.66]  We will keep up with that innovation.
[2688.00 --> 2695.06]  Just as an example, Meta just launched their Llama 3 400 billion parameter model in the market last week.
[2695.06 --> 2703.30]  So, you know, we already been running that model and we've supported that model and we wrote a blog on it a couple of days ago.
[2703.70 --> 2710.84]  So we're going to continue to support the most bleeding edge, latest and greatest technology that's coming out again on a monthly basis.
[2711.64 --> 2719.02]  Thank you both for taking time out of a lot of things going on in a fast moving ecosystem to come and chat with us.
[2719.02 --> 2728.06]  And I would definitely recommend to all the listeners to check out some of the show notes and the links and go try some things hands on and have some fun and start building.
[2728.38 --> 2729.64]  Thank you both, Greg and Ben.
[2729.74 --> 2731.18]  I appreciate you taking time.
[2731.44 --> 2732.04]  Yeah, thank you.
[2732.20 --> 2733.12]  Thank you, Daniel and Chris.
[2733.24 --> 2733.54]  Thank you.
[2741.02 --> 2741.98]  All right.
[2742.28 --> 2744.66]  That is Practical AI for this week.
[2745.46 --> 2746.48]  Subscribe now.
[2746.48 --> 2758.06]  If you haven't already, head to PracticalAI.fm for all the ways and join our free Slack team where you can hang out with Daniel, Chris and the entire ChangeLog community.
[2758.64 --> 2763.28]  Sign up today at PracticalAI.fm slash community.
[2763.84 --> 2770.82]  Thanks again to our partners at Fly.io, to our Beat Freaking Residence, Breakmaster Cylinder, and to you for listening.
[2771.18 --> 2772.94]  We appreciate you spending time with us.
[2773.30 --> 2774.46]  That's all for now.
[2774.72 --> 2776.36]  We'll talk to you again next time.
[2776.48 --> 2806.46]  We'll talk to you again next time.
