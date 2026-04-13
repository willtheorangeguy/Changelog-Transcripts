[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com and we're hosted
[11.42 --> 17.36]  on Linode servers. Head to linode.com slash Changelog. This episode is brought to you by
[17.36 --> 23.72]  DigitalOcean. They now have CPU optimized droplets with dedicated hyper threads from best in class
[23.72 --> 29.18]  Intel CPUs for all your machine learning and batch processing needs. You can easily spin up
[29.18 --> 34.74]  their one-click machine learning and AI application image. This gives you immediate access to Python 3,
[35.20 --> 42.68]  R, Jupyter Notebook, TensorFlow, Scikit, and PyTorch. Use our special link to get a $100 credit for
[42.68 --> 51.28]  DigitalOcean and try it today for free. Head to do.co slash Changelog. Once again, do.co slash Changelog.
[59.18 --> 68.60]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[69.02 --> 74.52]  productive, and accessible to everyone. This is where conversations around AI, machine learning,
[74.56 --> 78.66]  and data science happen. Join the community and snag with us around various topics of the show
[78.66 --> 84.48]  at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[89.18 --> 94.14]  Hey there. Welcome to another episode of the Practical AI podcast. This is Chris Benson. I'm an
[94.14 --> 101.32]  AI strategist and my co-host is Daniel Whitenack, a data scientist. We have a real treat in store for
[101.32 --> 108.74]  you today. We have a special guest that we have looked forward to having on the show for a long
[108.74 --> 116.18]  time now. And I am super excited about this episode. So that guest is Bill Daly, who is the
[116.18 --> 121.96]  chief scientist and senior vice president of research for NVIDIA. He is also a professor at
[121.96 --> 127.02]  Stanford University. Welcome very much, Bill. Oh, it's great to be here. And how's it going today,
[127.10 --> 133.08]  Daniel? It's going, it's going great. I'm excited to talk to Bill. I'm, of course, a huge fan as
[133.08 --> 140.28]  everyone is of everything NVIDIA is doing in this space. So I'm excited to hear more. Yep. So the
[140.28 --> 148.22]  genesis for this episode came back earlier this year in March. I was at the NVIDIA GTC conference
[148.22 --> 154.82]  in Silicon Valley, and I got to attend a small group session called AI for Business CXO Summit.
[155.26 --> 161.94]  And in that, the NVIDIA CEO, Jensen Huang, was kind of in a small group environment. And it was just an
[161.94 --> 167.38]  amazing amount of wisdom that I got. And I was thinking, and as I sat there, that was very,
[167.38 --> 173.00]  very business oriented in a lot of ways. But I kept thinking, if we had NVIDIA's chief scientists
[173.00 --> 178.64]  come on board to talk us through kind of what NVIDIA does, but give it to us as practitioners
[178.64 --> 184.20]  of neural network technology and other AI technology, that would just be amazing. So Bill,
[184.26 --> 187.00]  thank you so much for coming on board. I really appreciate it.
[187.06 --> 187.62]  You're very welcome.
[188.10 --> 192.94]  So I wanted to real quick ask, if you could just give us a little bit of background. I mentioned that
[192.94 --> 196.58]  you were the chief scientist in NVIDIA and a professor at Stanford. Could you tell us just a
[196.58 --> 198.76]  little bit about yourself before we launch into questions?
[198.76 --> 205.52]  Sure. So I'm sort of a hardware engineer who's been working on both hardware and software for AI
[205.52 --> 210.76]  in recent years. My first experience with neural networks was in the 1980s when I took a course
[210.76 --> 216.50]  from John Hopfield at Caltech and was building Hopfield nets and things like that. I was on the
[216.50 --> 221.82]  faculty at MIT for 11 years, where I built a research group that built a number of pioneering
[221.82 --> 228.70]  supercomputers, collaborated with Cray on the design of their Cray T3D and T3E, and then moved to Stanford
[228.70 --> 235.76]  in 1997, where I continued to lead research on high-performance computing and special purpose
[235.76 --> 242.30]  processors for numerous tasks, including graphics. I first got involved with NVIDIA in 2003 when I was
[242.30 --> 248.24]  hired as a consultant to help with what was called internally the NV50, became the G80 when it was
[248.24 --> 253.90]  announced, and in particular to help on the extensions to the G80 that enabled CUDA, the ability to run
[253.90 --> 259.30]  general-purpose computing programs on GPUs. And I really got to like the folks at NVIDIA, particularly
[259.30 --> 266.10]  Jensen, and he convinced me to join full-time in 2009. So since 2009, I've been building NVIDIA
[266.10 --> 272.14]  Research, the research organization at NVIDIA, and myself doing research on numerous topics, most recently
[272.14 --> 277.84]  on some of the path planning algorithms for our self-driving cars and on very efficient AI inference.
[278.24 --> 284.60]  That's awesome. Yeah, that's an amazing background, and I'm sure, yeah, I mean, it sounds like you joined
[284.60 --> 290.86]  NVIDIA at a really exciting time. Of course, things have really kind of exploded in a good way for them,
[290.92 --> 296.26]  and I'm sure it's a lot of excitement and thrills being at the center of that.
[296.68 --> 298.08]  Yeah, it's a really fun place to be.
[298.38 --> 302.58]  Awesome. Yeah, so I was wondering, from my perspective kind of growing up,
[302.58 --> 309.72]  the context in which I heard about NVIDIA was kind of in video processing and gaming,
[309.94 --> 316.20]  which kind of led to the rise of the GPU. I was wondering if you could speak a little bit to
[316.20 --> 324.20]  how and why that transition into this very AI-oriented approach that NVIDIA is taking now,
[324.42 --> 328.54]  and kind of comment on how that evolution occurred and how you see it from your perspective.
[328.54 --> 332.78]  Sure. So NVIDIA's roots are really in graphics. Gaming is one aspect of that,
[332.86 --> 337.24]  but we've also always done professional graphics. And if you think about what the graphics problem
[337.24 --> 343.86]  is, it's basically simulating how light bounces off of a scene and appears at your eye or at a
[343.86 --> 348.98]  camera. And doing that simulation, basically rendering the scene, shading each pixel,
[349.48 --> 353.18]  is a very computationally intensive task, and it's a very parallel task.
[353.18 --> 359.40]  So GPUs evolved to be very efficient parallel computers with very high computational intensity.
[359.94 --> 364.08]  And it turns out a lot of other problems have this nature of having a lot of computational
[364.08 --> 370.82]  intensity and being very parallel. And so early on, probably in the early 2000s,
[370.86 --> 376.16]  people started trying to use GPUs for tasks other than graphics. It's sort of a movement called
[376.16 --> 380.86]  GPGPU, general purpose GPUs. And around the same time, I was leading a project at Stanford,
[380.86 --> 386.18]  what we called stream processors, which actually wound up developing the right set of programming
[386.18 --> 391.72]  tools to program GPGPUs. We were developing a language called Brook. The lead student on that
[391.72 --> 397.32]  project, Ian Buck, graduated, got his PhD, came to NVIDIA and evolved, you know, along with the
[397.32 --> 400.82]  people in NVIDIA, including John Nichols, who was heading the computer architecture group at the
[400.82 --> 406.68]  time, evolved Brook into CUDA. And that basically made it very easy for people to take the, you know,
[406.68 --> 412.44]  huge number of arithmetic units who are in GPUs and their ability to execute parallel programs very
[412.44 --> 417.82]  efficiently and apply them to other problems. And so at first they were applied to high performance
[417.82 --> 423.88]  computing problems and GPUs have continued to be very good at that. We currently provide the
[423.88 --> 428.64]  arithmetic for the number one supercomputer in the world, some at Oak Ridge National Laboratories.
[429.12 --> 432.68]  And, you know, they've been applied to things from, you know, you know, oil and gas
[432.68 --> 439.64]  reservoir modeling to simulating more efficient, you know, combustion engines to simulating how
[439.64 --> 444.08]  galaxies collide. All sorts of high performance computing problems, predicting weather, climate
[444.08 --> 450.14]  change, stuff like that are now done on GPUs. So it was very natural since we basically now had the
[450.14 --> 455.80]  platforms. This is, you know, we announced CUDA in 2006, you know, you know, a few years later,
[456.12 --> 460.10]  substantial fraction of all of the large supercomputers being built were based on,
[460.10 --> 465.06]  on GPUs. It was very natural that when other very demanding problems came along,
[465.42 --> 470.06]  that people would apply GPUs to them. And so if you look at deep learning and particularly the training
[470.06 --> 475.04]  for deep learning, it's a very computationally intensive problem. You know, it takes, you know,
[475.54 --> 480.26]  when this was first started to be done, it was taking weeks on the fastest GPUs we had,
[480.52 --> 485.94]  and it's very parallel. So it was a perfect match for GPUs. And so, you know, early on,
[485.94 --> 493.16]  you know, we saw this match and applied GPUs to that. For me and for NVIDIA, the start really came
[493.16 --> 498.00]  when I had a breakfast with my Stanford colleague, Andrew Wing, and I think it was about probably in
[498.00 --> 503.74]  2010 or early 2011. And at the time he was at Google Brain and was finding cats on the internet
[503.74 --> 509.08]  by building very large neural networks running on 16,000 CPUs. And when he described what he was
[509.08 --> 515.40]  doing to me, I said, you ought to be doing that on GPUs. And so I found somebody in NVIDIA research,
[515.40 --> 519.82]  a guy named Brian Catanzaro, who now runs our applied deep learning research group.
[520.18 --> 524.96]  At the time, he was actually a programming language researcher, but he was interested in deep learning
[524.96 --> 529.98]  and had the right background knowledge. And his assignment was to work with Andrew and move Andrew's
[530.50 --> 537.80]  neural network for finding cats to run on GPUs. We were able to take what took 16,000 CPUs and run it
[537.80 --> 543.06]  on, I think it was, you know, 48 GPUs in, you know, I think even higher performance than he was getting.
[543.06 --> 549.32]  And the software that came out of that turned into CUDA DNN, on top of which we basically ported just
[549.32 --> 553.88]  about every framework there is. Now, the other thing that happened is the first, you know, the
[553.88 --> 558.88]  GPUs we had at that time, which were, you know, our, it was right around our Fermi to Kepler transition,
[559.24 --> 563.24]  weren't originally designed to do deep pointing. They were designed to do graphics and high performance
[563.24 --> 567.98]  computing. And so they had, you know, good 32-bit floating point performance, good 64-bit floating
[567.98 --> 573.12]  point performance. But it turns out what you want for deep learning training is FP16. And what you
[573.12 --> 576.28]  want for deep learning inference is INT8. And they weren't actually particularly good at either of
[576.28 --> 582.18]  those. So as we learn more about what deep learning needed, our subsequent generations of GPUs have been
[582.18 --> 587.78]  specialized for deep learning. We've added support for FP16 for training. We've added support for INT8 and
[587.78 --> 595.20]  INT4 and INT1 for inference. And we built tensor cores, which are special purpose units that basically give us
[595.20 --> 600.96]  the efficiency of hardwired deep learning processors like the Google TPU, but without giving up the
[600.96 --> 605.92]  programmability of a GPU. So while the original GPUs were good at deep learning, now that we've
[605.92 --> 610.26]  gotten more experience with deep learning, learned what it really needs and have specialized and
[610.26 --> 615.90]  optimized GPUs for that, the GPUs today, especially, you know, Volta and Turing are really great at deep
[615.90 --> 621.50]  learning. Yeah, that's awesome. I know I was just kind of trying to soak all that up. There's so much
[621.50 --> 626.40]  context and great information that I know I didn't, I wasn't aware of before, for example,
[626.54 --> 631.66]  you know, the evolution of CUDA and how it came from this Brook language that you mentioned,
[632.04 --> 637.74]  and you know, how the classifying of cats fit in and all of that. I don't know,
[637.94 --> 643.52]  were you aware of a lot of that, Chris? A lot of that's great new context that I wasn't aware of.
[643.98 --> 649.42]  Yeah, I mean, he took topics that I now would consider a shallow understanding of up until,
[649.42 --> 654.10]  you know, at this point and went deep, which is fantastic. So be careful, Bill, because we have
[654.10 --> 657.56]  a whole bunch more questions for you. We're going to dive deep into some of these things you're
[657.56 --> 662.62]  telling us about. Okay. Yeah. So in particular, I know you mentioned a lot of things that I would
[662.62 --> 667.92]  love just a little bit of clarification on for those in our audience that may be new to them.
[668.08 --> 673.98]  So you mentioned kind of the evolution of CUDA. You also mentioned, you know, how GPUs were
[673.98 --> 681.14]  kind of integral to this scaling of the deep learning training and all of that. I was wondering
[681.14 --> 687.60]  if we could just kind of take a step back and from your perspective, kind of get your explanation of,
[687.60 --> 697.84]  you know, what a GPU is generally, why it's useful for deep learning in particular, and how CUDA fits
[697.84 --> 702.62]  fits into that, what it is, like what that interface looks like today.
[703.18 --> 710.58]  Yeah. So a GPU generally is just a very efficient parallel computer. You know, Volta has 5120,
[710.68 --> 715.54]  what we call CUDA cores, which really means 5120 separate arithmetic units that could be operating
[715.54 --> 722.56]  in parallel. And coupled to that is a very efficient system for supplying data to those units and
[722.56 --> 728.50]  accessing memory. And so, you know, for any problem that's very parallel, they are orders of magnitude
[728.50 --> 734.48]  more efficient than CPUs. CPUs, in contrast, are optimized for single thread performance and for
[734.48 --> 740.24]  very low latency. But to do that, they wind up spending enormous amounts of energy reorganizing
[740.24 --> 746.20]  your program on the fly to schedule instructions around long latency cache misses, right? So if you try
[746.20 --> 750.42]  to access memory and you're lucky, you get a number in three clock cycles. If you're not so lucky,
[750.42 --> 756.06]  it might be 200 clock cycles. And so they've got to, you know, do a lot of bookkeeping to work around
[756.06 --> 760.28]  that uncertainty. The result of that is a huge amount of energy that's spent and therefore
[760.28 --> 766.20]  performance and energy efficiency that's orders of magnitude less than a GPU. A GPU takes advantage
[766.20 --> 771.32]  of the fact that if you have a very parallel program, you can hide any memory latency with more
[771.32 --> 775.38]  parallels. You work on something else while you wait for the data to come back. So they wind up being
[775.38 --> 780.04]  extremely efficient platforms for tasks like deep learning, where you have many parallel
[780.04 --> 785.12]  operations that can be done simultaneously before you get the results of one of them back.
[785.76 --> 791.90]  And that's like for the matrix type operations that you're talking about and also the kind of
[791.90 --> 795.16]  iterative training processes? Is that right?
[795.32 --> 801.68]  Right. So, you know, at the core of deep learning are convolutions and matrix multiplies.
[801.68 --> 806.36]  And in fact, you can turn the convolutions into matrix multiplies through a process called
[806.36 --> 811.38]  lowering. So fundamentally, if you can do a very efficient matrix multiply, you can do really
[811.38 --> 816.08]  well at deep learning. And GPUs are very good at doing those matrix multiplies, both because they
[816.08 --> 821.58]  have an enormous number of arithmetic units, because they have a very highly optimized memory and on-chip
[821.58 --> 826.96]  communication system for keeping those arithmetic units busy and occupied.
[826.96 --> 834.42]  So that that is really a great explanation. And that's helping me a lot. I would like to understand
[834.42 --> 840.62]  beyond just NVIDIA's GPUs, those of us, you know, that are out here kind of consuming information in
[840.62 --> 847.66]  the space are always hearing tons of other acronyms. And if you and you know, CPUs, TPUs, ASICs, if you
[847.66 --> 853.04]  could explain to us a little bit what's different about a GPU from those other architectures that are out
[853.04 --> 857.54]  there. And what are some of the advantages and disadvantages? You know, why is it that NVIDIA
[857.54 --> 861.52]  is able to lead the way with this GPU technology that you've been bringing us for the last few
[861.52 --> 861.74]  years?
[862.00 --> 867.48]  Sure. So I already mentioned some of that by comparing CPUs and GPUs. A CPU, a central processing
[867.48 --> 874.98]  unit like, you know, an Intel, you know, Xeon or, you know, AMD's latest parts is optimized for very
[874.98 --> 880.06]  fast execution of a single computational thread. And as a result of that, it spends an enormous
[880.06 --> 886.40]  amount of energy rescheduling instructions around cache misses. And as a result, winds up burning
[886.40 --> 891.96]  something on the order of, you know, a, you know, a nanojoule per instruction where the actual
[891.96 --> 897.32]  work of that instruction maybe only takes 1% of that energy. So that you can think of them as being
[897.32 --> 903.68]  1% efficient. GPUs actually spend more than half of their energy doing the payload arithmetic on
[903.68 --> 909.98]  computational intensive problems. So they are many times more efficient than CPUs at that. Now,
[909.98 --> 916.30]  CPUs have vector extensions that try to get some of the efficiency of GPUs. But if you look at the
[916.30 --> 921.58]  core CPU, they're extremely inefficient, but very good at, you know, doing a single thread. If you
[921.58 --> 925.82]  don't have any parallelism, you need the answer quickly. A CPU is what you want. If you've got
[925.82 --> 930.32]  plenty of parallelism and you can hide your memory latency by working on something else while you're
[930.32 --> 935.96]  waiting for that result to come back from memory, then a GPU is what you want. Now, you mentioned also
[935.96 --> 941.24]  TPUs and ASICs. Well, the TPU is a type of ASIC, right? It's an application-specific integrated
[941.24 --> 947.02]  circuit. In this case, it's the application it's specific for is doing matrix multiplies. The
[947.02 --> 953.92]  Google TPU, especially the TPU1, which they just had an article in CACM about, is a big unit that
[953.92 --> 959.66]  basically has a systolic array to multiply two matrices together. And it's extremely efficient at
[959.66 --> 964.70]  that. And so all you need to do is multiply matrices. It's very hard to beat a TPU. Now,
[964.70 --> 970.22]  the approach we've taken with our latest GPUs is to put tensor cores in them. And what tensor cores are,
[970.68 --> 976.08]  are little matrix multiply units. They're very specialized to multiply matrices together.
[976.48 --> 980.60]  The difference is by specializing, by adding a unit to a general purpose processor,
[981.14 --> 986.26]  we get the efficiency of that specialization without giving up the programmability of the GPU.
[986.70 --> 990.92]  So if you need to write a custom layer to do, you know, a mask because you're doing,
[990.92 --> 996.30]  you know, a pruning and have a sparse set of weights, or if you need a custom layer to do a
[996.30 --> 1000.28]  new type of nonlinear function that you're experimenting with, or you want to do some
[1000.28 --> 1005.04]  type of concatenation between layers that is a little bit different, it's really easy to write
[1005.04 --> 1011.20]  that in CUDA, program it on the GPU, and it will execute extremely well with all the efficiency of the
[1011.20 --> 1016.28]  hardwired matrix multiply units coming from the tensor cores. Whereas in the TPU, you have that
[1016.28 --> 1020.80]  efficiency, but you don't have the flexibility. You can only do what that, you know, one unit has
[1020.80 --> 1027.22]  been, has been, you know, designed and hardwired to do. Now, the advantage of that is it's, it's about
[1027.22 --> 1031.68]  the same energy efficiency, right? So when you're not using the other features of the GPU, you're not
[1031.68 --> 1035.98]  paying for them. They don't burn any energy, but they are sitting there using up die areas. So the TPU
[1035.98 --> 1041.46]  costs a little bit less to manufacture because you don't have all of that general purpose processor
[1041.46 --> 1047.10]  sitting around it. But what you give up for that is the flexibility of being able to support new
[1047.10 --> 1051.90]  deep learning algorithms as they come out. Because if it, if it, those algorithms don't match what the
[1051.90 --> 1057.74]  TPU is hardwired for, it can't do it. Yeah. And as we've, as we've seen the, the industry isn't
[1057.74 --> 1063.08]  moving very fast at new, new neural network architectures, right? Oh, they're coming up every
[1063.08 --> 1067.20]  day. I mean, it's hard to keep up with, with all the papers on archive. Yeah, it is definitely.
[1067.20 --> 1071.70]  We, we try a little bit on this show, but we're all constantly falling behind.
[1072.46 --> 1077.82]  So quick follow-up in that case, based on the fact that you have the tensor cores in the GPUs,
[1077.94 --> 1083.72]  it's unlikely that NVIDIA then would likely go to a, you know, some sort of ASIC architecture or
[1083.72 --> 1087.40]  something else like that. Since you've, you essentially have already accounted for that
[1087.40 --> 1092.20]  value in your GPU architectures. Is that a fair say? Actually not. We actually have our own
[1092.20 --> 1099.16]  ASIC like architecture as well, in that we have something called the NVIDIA deep learning accelerator,
[1099.30 --> 1105.70]  the NVDLA, which we've actually open sourced. If you go to nvdla.org, you'll see our webpage where
[1105.70 --> 1110.48]  you can download the RTL and the programming tools and everything else for what is actually a very
[1110.48 --> 1116.06]  efficient hardwired neural network accelerator. And we use the NVDLA ourselves in our Xavier chip,
[1116.20 --> 1121.76]  which is the, the system on a chip that we have for our self-driving cars. The Xavier has a number
[1121.76 --> 1128.34]  of ARM cores of our own design. It has basically a 10th of a Volta GPU. It's, you know, 512 CUDA
[1128.34 --> 1134.06]  cores rather than 5120. And then it has the NVDLA as well as a computer vision accelerator,
[1134.06 --> 1139.96]  because in embedded processors on the edge, that area efficiency is important. We don't want to give
[1139.96 --> 1146.56]  up the die area for doing, you know, deep learning entirely on the GPU. Now there's still an awful lot
[1146.56 --> 1155.02]  of GPU performance on, on Xavier. It's, you know, over 10 tera ops on the, on the CUDA cores. But
[1155.02 --> 1160.60]  there's also another 20 tera ops on the deep learning accelerators. So you wind up being able to support
[1160.60 --> 1166.90]  very efficiently, you know, large numbers of inference tasks on, on that. So we're, we're actually doing it
[1166.90 --> 1172.60]  both ways for the embedded applications. We have a hardware deep learning accelerator for both
[1172.60 --> 1178.08]  inference and training in the data center. Yeah. After considering all options, we have decided
[1178.08 --> 1184.10]  it's just much better to put the efficient tensor cores onto a programmable engine rather than building
[1184.10 --> 1191.10]  a hardware accelerator. So you've mentioned, and this is a great lead in, you, you mentioned kind of
[1191.10 --> 1196.72]  a variety of fronts on which NVIDIA is working. And you've also mentioned a desire that you guys have
[1196.72 --> 1203.60]  to keep things programmable and, and easy to, to interface with and, and customize. Um, one of the
[1203.60 --> 1210.72]  things that, that I've definitely seen is that, um, NVIDIA is, is definitely, um, making contributions
[1210.72 --> 1217.72]  not only on, on the hardware side, but on kind of, uh, on the front of helping users be able to interface
[1217.72 --> 1222.74]  with all sorts of these, these new types of hardware. For example, I, I see, um, you know,
[1222.74 --> 1230.34]  like NVIDIA Docker and I see things related to Kubernetes and, um, and NVIDIA working to kind of
[1230.34 --> 1237.28]  help people both, uh, both program their, their hardware, but also access and manage and orchestrate
[1237.28 --> 1241.38]  things. I was wondering if you could, if, if there's anything you want to highlight on, on that side and
[1241.38 --> 1246.88]  mention, you know, where, where the different areas that you see, uh, see NVIDIA working on that
[1246.88 --> 1252.04]  are really exciting, maybe not on the hardware side, but maybe on the orchestration or software side.
[1252.04 --> 1257.62]  Yeah, no, we, um, we actually do research on, on deep learning that spans the gamut from,
[1257.62 --> 1262.78]  you know, fundamental, you know, deep learning algorithms and models, training methods to
[1262.78 --> 1267.44]  tools that make it easier for people to use deep learning all the way up, up to the hardware.
[1267.56 --> 1271.76]  The stuff that I'm actually most excited about is some of the work on, on fundamental models and,
[1271.76 --> 1277.04]  and, um, and algorithms. We, for example, right now have the world's best neural network
[1277.04 --> 1281.76]  for doing optical flow, which is a really nice hybrid of classical computer vision and deep
[1281.76 --> 1286.00]  learning because we've applied a lot of what's been learned over 30 years of doing optical flow
[1286.00 --> 1290.16]  the old way. Uh, but then it built, built that around a deep learning approach and we get the
[1290.16 --> 1295.14]  best of both worlds. We also have done enormous amount of research on generative adversarial
[1295.14 --> 1300.96]  networks. We developed a method of, uh, we're the first people to train high resolution, uh,
[1300.96 --> 1305.32]  generative networks. Um, in the past, you know, basically you just had too many free variables.
[1305.32 --> 1309.34]  If you try to train a GAN to build a high resolution image, it would just get confused
[1309.34 --> 1314.24]  and never converge. Um, we applied curricular learning where we trained the GAN first to do
[1314.24 --> 1319.22]  low resolution images. Once it's mastered that we then increased the resolution progressively,
[1319.44 --> 1323.30]  we call it progressive GAN and we're very successfully able to generate high resolution
[1323.30 --> 1330.16]  images. This, um, has been applied to, uh, to numerous, um, tasks. We've also, um, been able to
[1330.16 --> 1337.46]  build, um, coupled GANs where we, we can use them to transfer style. So for example, um, if we have a
[1337.46 --> 1342.68]  bunch of images, um, in daylight, good weather, we can change those to images at night or images in the
[1342.68 --> 1349.04]  rain or images in the snow. And this lets us augment data sets for self-driving cars. We can also use
[1349.04 --> 1354.88]  these GANs to, um, generate medical data sets, being able to, you know, take, you know, for example,
[1354.94 --> 1360.10]  brain images and tumor images and combine them in various ways to build larger training sets. And you
[1360.10 --> 1364.76]  could get by just using the raw data and then a combination of the real data and these synthetic
[1364.76 --> 1370.24]  images winds up giving you better accuracy than the one alone. So that works for exciting. We also
[1370.24 --> 1375.42]  have a number of tools. You mentioned our, our Docker platforms. We also have, um, a tool called
[1375.42 --> 1381.30]  tensor RT, which optimizes neural networks, um, for inference. So we get much more efficient execution
[1381.30 --> 1387.90]  on our GPUs than if you simply naively mapped, um, the networks on there. Um, and so across the board,
[1387.90 --> 1393.24]  we've been trying to build the whole ecosystem so that somebody who has a problem can come and draw
[1393.24 --> 1397.52]  from our collection of algorithms. They can draw from our tools and then ultimately run it on our
[1397.52 --> 1402.72]  hardware and get a complete solution for their problem. How do you, uh, how do you keep all of
[1402.72 --> 1408.74]  those wheels turning as the, uh, as, as the VP of research is a lot of different areas spanning all
[1408.74 --> 1414.78]  the way from hardware to software, to tooling, to, uh, AI research. I, I'm sure it's exciting,
[1414.78 --> 1419.30]  but, uh, a lot going on. Yeah. So I, I fortunately don't have to keep them all turning myself. I'm,
[1419.30 --> 1424.44]  I'm responsible for NVIDIA research, which is an organization of about 200 people. And we do
[1424.44 --> 1430.98]  research on topics ranging from circuit design to AI algorithms. And, um, you know, basically what
[1430.98 --> 1435.68]  we do is we hire really smart people and then we try to enable them to take all the obstacles out of
[1435.68 --> 1440.84]  their way, get them excited about the important problems. And, and the, you know, the objective of
[1440.84 --> 1445.70]  NVIDIA research is, um, is to do two things. One is to do research. There are a lot of corporate
[1445.70 --> 1449.60]  research labs that actually don't do research. They wind up really doing development because they
[1449.60 --> 1454.74]  get pulled into close to various product groups. You know, they're the product groups always wind
[1454.74 --> 1458.56]  up having some fire to put out. And so they'll pull the researchers onto the short-term development
[1458.56 --> 1462.48]  work, put the light of spire out and they wind up not, not really doing fundamental research. So
[1462.48 --> 1467.10]  our goal is to do that fundamental research. And, and we succeed in that as evidence by publishing,
[1467.10 --> 1473.26]  you know, lots of papers at leading conferences like, you know, NIPS and ICLR and ICML and CDPR.
[1473.78 --> 1477.90]  Um, and then the, the other goal is to make sure that that research is, um, beneficial to NVIDIA,
[1477.98 --> 1481.42]  that it makes a difference for the company. And again, that's another failure mode of industrial
[1481.42 --> 1485.62]  research labs. Many of them publish lots of great papers, do lots of great research, and
[1485.62 --> 1489.88]  it has absolutely no impact on their parent company. Um, I think I'd have trouble convincing
[1489.88 --> 1494.98]  Jensen to continue, uh, running the research lab if we didn't, um, have many successes, but we do.
[1494.98 --> 1500.54]  So for example, the, the ray tracing cores in Turing were originally an NVIDIA research project.
[1500.70 --> 1506.02]  QDNN, as I mentioned, um, came out of research. We are applying deep learning to graphics. We,
[1506.08 --> 1510.38]  we demonstrated with Turing something called deep learning, um, super sampling, which basically,
[1510.70 --> 1515.74]  basically anti-aliases and up, uh, samples an image, um, using neural networks and does it in
[1515.74 --> 1522.56]  a temporally stable way. Our DGX2, which includes NVSwitch, NVSwitch started as a project in NVIDIA research,
[1522.56 --> 1528.12]  as did NVLink on which, um, the switch is based. So, um, we have a long track record of taking
[1528.12 --> 1533.62]  kind of crazy ideas, you know, maturing them within NVIDIA research, and then getting the product groups
[1533.62 --> 1539.58]  to, you know, embrace them and ultimately put them into future GPUs and, um, software and systems products
[1539.58 --> 1540.20]  that we produce.
[1540.66 --> 1545.62]  So Bill, as we come back out of break, uh, I wanted to ask you, uh, kind of back out just a little bit
[1545.62 --> 1550.88]  because we've gone down some, some amazing paths. I know Daniel and I have learned so much already on the show
[1550.88 --> 1556.72]  from you, but I wanted to, to put a little context around some of that and kind of get a sense, as you've told
[1556.72 --> 1562.98]  us about all of these amazing technologies, what is NVIDIA's vision kind of for the future of AI?
[1563.50 --> 1568.76]  And, and as you've talked about some of the parts of your AI platform, you know, how are you utilizing
[1568.76 --> 1573.98]  that platform strategically to realize that? And what kind of investments are you expecting NVIDIA to make
[1573.98 --> 1578.02]  going forward? That's a really good question. So, you know, the short answer for the future of AI
[1578.02 --> 1583.14]  is continued rapid innovation. I expect to continue to have to stay up late every night reading papers
[1583.14 --> 1588.34]  on archive, and even then not be able to keep up with what's going on. But if you look at how that
[1588.34 --> 1593.02]  rapid innovation is happening, I think it's along several different axes. The first axis, I think,
[1593.06 --> 1598.08]  is breadth of applications. I think we've only begun to scratch the surface of how AI is affecting,
[1598.32 --> 1602.98]  you know, our daily lives, how we do business, how we entertain ourselves, how we, you know,
[1602.98 --> 1608.78]  practice our professions. And, and I expect more applications of AI to be occurring every day.
[1608.90 --> 1614.82]  And, and those applications to present unique demands, the type of models we need, how we curate
[1614.82 --> 1620.96]  training data, how we train the networks with that data, and so on. The next axis, I would say,
[1620.98 --> 1628.10]  is one of scale, scale of both model size and data sets. We've seen this in areas like computer vision,
[1628.10 --> 1635.00]  in speech recognition, in, in machine translation, where over time, people collect larger data sets
[1635.00 --> 1640.70]  to have the capacity to learn those data sets. They build larger models that really raises the bar for
[1640.70 --> 1645.50]  the performance you need to train those models on those large data sets in a reasonable amount of
[1645.50 --> 1652.26]  time. And then finally, the axis is probably most exciting to me is coming up with new models and new
[1652.26 --> 1659.46]  methods that basically increase the capability of, of deep learning to be more than just perception,
[1659.46 --> 1665.02]  to basically give it more cognitive ability to have it be able to reason about things, to have
[1665.02 --> 1669.38]  longer term memories, you know, to operate and interact with environments. A lot of the work in
[1669.38 --> 1675.10]  reinforcement learning, we find very exciting along that, along that axis. So seeing, you know, AI,
[1675.24 --> 1679.66]  you know, there's constant innovation along all three of these axes. Our goal with our platform is to
[1679.66 --> 1684.38]  evolve to meet these needs, to meet the needs of newer applications, to meet the needs of larger
[1684.38 --> 1689.98]  scale, and, you know, more capable, you know, models and methods. And there's a couple ways we
[1689.98 --> 1694.96]  need to do that. One is to continue to raise the bar on performance, you know, to train larger models
[1694.96 --> 1700.98]  and larger data sets requires more performance. And Moore's law is dead. We're not getting any more
[1700.98 --> 1705.18]  performance out of process technology. So it requires us to innovate with our architecture,
[1705.28 --> 1709.62]  with our circuit designs to do that. And we've done that generation to generation. If you look at
[1709.62 --> 1715.46]  the performance from, you know, Kepler, where we started working on deep learning, to Maxwell and
[1715.46 --> 1721.60]  Pascal, Volta, and now Turing, we've been able to really increase by large multiples deep learning
[1721.60 --> 1727.46]  performance on each subsequent generation, in the absence of really any help from process technology.
[1727.46 --> 1732.68]  And we expect to continue doing that. The next thing we need to do is we need to make it easier to
[1732.68 --> 1737.84]  program so that, you know, people who are not, you know, experts in AI, but are other experts in their
[1737.84 --> 1743.08]  domain can easily cultivate a data set, you know, acquire the right models and train them.
[1743.50 --> 1748.06]  And we do that, you know, through our tools, we support every framework, we have TensorRT to make
[1748.06 --> 1754.52]  it easy to map your applications onto inference platforms. And then we also have training programs,
[1754.58 --> 1758.62]  we have a deep learning institute, where we basically take people who are application experts
[1758.62 --> 1763.20]  and train them so that they can apply deep learning to their application. And then the final way we want
[1763.20 --> 1768.62]  our platforms to evolve is to remain flexible. The deep learning world is changing every day.
[1768.78 --> 1773.30]  And so we don't want to hardwire too much in and not be able to support the latest idea. In fact,
[1773.30 --> 1777.44]  we think it would inhibit people coming up with the latest idea if, you know, the platform that
[1777.44 --> 1782.08]  everybody is using was too rigid, we want to make it a very flexible platform that people can continue
[1782.08 --> 1783.90]  to experiment and develop new methods.
[1784.60 --> 1789.52]  Yeah. So in light of that, I'd be really interested to hear from your perspective,
[1789.52 --> 1795.30]  how ideas that NVIDIA actually advance from research to reality, in particularly in light
[1795.30 --> 1800.92]  of what you just said, in light of that you want to make things easier for people to program,
[1801.10 --> 1806.78]  easier for people to interface with, application people to interface with, while at the same time,
[1806.86 --> 1813.34]  you know, pushing performance forward and keeping flexible. It definitely seems like it might be
[1813.34 --> 1818.80]  hard to balance those things. But as you've already mentioned, there's been a lot of great things
[1818.80 --> 1823.76]  that you guys have come out with that do balance that really well. So I was wondering if from that
[1823.76 --> 1828.66]  perspective, how you see things advancing from research to reality in NVIDIA?
[1828.66 --> 1832.44]  Yeah, so that's a good question. And one that I'm very excited about, because it's kind of my job
[1832.44 --> 1837.86]  to make sure those things advance. So not all ideas start in NVIDIA research, many ideas start in the
[1837.86 --> 1842.60]  product groups, many ideas start, you know, with application engineers who work with the customers and see
[1842.60 --> 1847.54]  the need. But for the ideas that do start in NVIDIA research, which is an organization of about 200
[1847.54 --> 1851.68]  people, individual researchers generally just start experimenting with things, come up with a good
[1851.68 --> 1858.70]  idea. And then the goal is to find a way for that idea to have impact on the company. And so we try to
[1858.70 --> 1863.82]  make sure everybody, when they come up with an idea, identifies both a champion and a consumer who are
[1863.82 --> 1869.76]  often the same person in the product groups for that technology. And, you know, as they develop the
[1869.76 --> 1874.62]  technology further, they get some indication about, gee, does the champion care about this technology?
[1874.62 --> 1878.90]  Can they make their product better? And if it doesn't, it's often an indication they should
[1878.90 --> 1884.16]  drop the idea. In fact, to me, one of the keys of good research is to kill things quickly. Most
[1884.16 --> 1888.82]  research projects actually don't go anywhere. And there's nothing wrong with coming up with research
[1888.82 --> 1893.68]  ideas that don't work. What's wrong is spending a lot of resources on them before you give up on the
[1893.68 --> 1897.40]  ones that don't work. And so we try to kill the ideas that either aren't going to work or aren't going
[1897.40 --> 1901.20]  to have impact on the company pretty quickly. But the ones that are going to have impact on the
[1901.20 --> 1906.06]  company, one thing that's really great about NVIDIA is it's a company where it's like a big
[1906.06 --> 1910.10]  startup. There's no politics. There's no not invented here. So if there's a good idea, the
[1910.10 --> 1913.24]  product groups don't care that it came out of research. They say, that's a great idea. We want
[1913.24 --> 1917.08]  that. And very often they'll grab things out of our hands before we even think we're done with them.
[1917.18 --> 1921.38]  NB Switch was a great example of that. We wanted to actually complete a prototype and research.
[1921.52 --> 1925.88]  We didn't get the chance. They grabbed it, made it a product before we had the chance to do that.
[1925.88 --> 1930.78]  And it's really about people that the people come up with the concept are communicating with the
[1930.78 --> 1935.20]  people who will turn it into reality. And then once it sort of jumps over to that side, it becomes
[1935.20 --> 1940.28]  more of an engineering endeavor, less of a research endeavor where people have to hit goals. Things
[1940.28 --> 1944.44]  have to work. They have to be verified. But the whole process works. And ultimately, we're able to
[1944.44 --> 1950.96]  very quickly go from concept to delivering very polished, very reliable products to our end customers.
[1950.96 --> 1957.10]  So I would like to take you into a particular use case. I know when I was at GTC in March,
[1957.64 --> 1964.66]  Jensen was on stage doing his keynote and we all walked in looking at the amazing autonomous
[1964.66 --> 1969.20]  vehicles that you guys had in the lobby and stuff. And he made a comment that really struck me. And I
[1969.20 --> 1974.40]  was just wanting to get your thoughts on it. He said, everything that moves will be autonomous.
[1974.92 --> 1979.98]  And in that presentation, he went way beyond just cars. He was talking about literally everything,
[1979.98 --> 1987.78]  whether it be on the land, sea, or air. And so obviously, that would include GPUs and maybe
[1987.78 --> 1991.98]  other specialized processors that you guys put into those vehicles. But what other things are
[1991.98 --> 1995.38]  you doing to realize that vision, considering how cool it is to the rest of us?
[1995.42 --> 1999.98]  That's a great question. So one thing we're doing in a video research is we're actively pursuing
[1999.98 --> 2005.40]  both autonomous vehicles and robotics. And in fact, autonomous vehicles are a special case,
[2005.46 --> 2009.66]  in many ways, an easy case of robotics. And that all they really have to do is navigate
[2009.66 --> 2013.80]  around and not hit anything. Robots actually have a much harder task in that they have to
[2013.80 --> 2019.14]  manipulate. They have to pick things up and insert bolts into nuts. They have to hit things,
[2019.16 --> 2023.90]  but hit things in a controlled way so that they can actually manipulate the world in a way that
[2023.90 --> 2030.44]  they desire. And so I've recently started a robotics research lab at NVIDIA. It's in Seattle. We hired
[2030.44 --> 2036.24]  Dieter Fox from the University of Washington to lead that lab. And robots are just a great example of
[2036.24 --> 2041.28]  how deep learning is changing the world because historically robots have been very accurate
[2041.28 --> 2046.02]  positioning machines. If you look at how they've actually been applied in the world, auto manufacturers
[2046.02 --> 2051.24]  use them on their lines to do spot welding and to spray paint, but they're not responding to the
[2051.24 --> 2055.96]  environment. They simply have been programmed to very accurately move an actuator to a position
[2055.96 --> 2060.30]  repeatedly over and over again, do exactly the same thing. With deep learning, we're able to actually
[2060.30 --> 2067.28]  give robots perception and the ability to interact with the environment so that they can respond to a
[2067.28 --> 2071.40]  part not being in the right place, adjust, manipulate, pick that part up, move it around.
[2071.88 --> 2076.64]  They can perhaps even work with people working as a team where the robot and the person are
[2076.64 --> 2081.52]  interacting together by using deep learning to provide them with both sensory abilities and also
[2081.52 --> 2086.44]  through reinforcement learning, the ability to reason and choose actions for a given state that they
[2086.44 --> 2093.06]  find themselves in. And so our goal from this is by doing this fundamental research in robotics is to
[2093.06 --> 2098.28]  basically learn how to build future platforms that will be the brains for all of the world's robots,
[2098.36 --> 2102.22]  just like we want to build the platform that's going to be the brains for all of the world's
[2102.22 --> 2107.04]  autonomous vehicles. Hopefully this research will ultimately lead to that platform, not just the
[2107.04 --> 2113.26]  hardware, but the various layers of software and ultimately the fundamental methods that those future
[2113.26 --> 2118.02]  robots and autonomous vehicles will be using. So Bill, we've kind of transitioned into talking
[2118.02 --> 2124.26]  about, you know, use cases and you've mentioned a lot about robots and other things kind of at,
[2124.52 --> 2131.02]  quote unquote, the edge. I was wondering if you could give us a little bit of a perspective on,
[2131.10 --> 2138.66]  you know, what you, moving forward, what you see as the edge and how neural network,
[2138.66 --> 2143.50]  both training and inference will be kind of spread across, you know, centralized compute in the cloud
[2143.50 --> 2149.16]  or on premise and on, on edge devices and what those edge devices might, might look like.
[2149.50 --> 2154.84]  That's a good question. So I see deep learning is happening in sort of three ways. So the first is
[2154.84 --> 2159.98]  training, which by large takes place in the cloud. And the reason why you want it to take place in the
[2159.98 --> 2163.82]  cloud is that first of all, you need to have a large data set. So you need to have some place where
[2163.82 --> 2170.06]  you can store terabytes of data, maybe even, even, you know, more than that. And, you know,
[2170.06 --> 2174.74]  you really want to do that in a centralized location. You also, if you're gathering training
[2174.74 --> 2179.26]  data, say from a fleet of autonomous vehicles, you want them all to learn from each other's
[2179.26 --> 2183.90]  experiences, right? So you want to gather all that data, collate it in one place, curate the data to
[2183.90 --> 2188.32]  basically discard the stuff that's not very interesting, keep the stuff that is, and then train
[2188.32 --> 2192.92]  one network on, on all of the data. So, so training really wants to happen in the cloud.
[2193.32 --> 2197.84]  It requires a large data set. It has a large memory footprint, has unique requirements,
[2197.96 --> 2203.06]  requires FP 16. And then there's inference and inference happens in, in both the edge and the
[2203.06 --> 2207.34]  cloud. I think most people, if you can do inference in the cloud would prefer to do it there.
[2207.72 --> 2212.92]  There's an economy of scale. You can also share resources. You know, if you have a task where
[2212.92 --> 2219.08]  you're not doing inference constantly, but on demand, then you don't need to have a resource
[2219.08 --> 2223.46]  tied up all the time. You can only, you know, you can share it, use it when you need it. Somebody else
[2223.46 --> 2227.52]  can use it when you don't need it. So it's just more efficient to do inference in the cloud. But
[2227.52 --> 2231.04]  there are cases where you can't do inference in the cloud. And, you know, an autonomous vehicle is a
[2231.04 --> 2235.64]  great example. First of all, you may have latency requirements, right? If your camera sees,
[2235.76 --> 2240.28]  you know, the, the, you know, kid running into the street, you can't afford the latency to send that
[2240.28 --> 2244.08]  image to the cloud, do the inference there and send the braking command back. You need to have a
[2244.08 --> 2249.08]  very tight loop that, that commands the car to stop. You also may not be connected or you may have
[2249.08 --> 2253.36]  bandwidth limits. So for example, people who have networks of surveillance cameras are producing just
[2253.36 --> 2258.02]  too much data to send all of it to the cloud. They need to do some data reduction, at least locally,
[2258.02 --> 2262.88]  have some local inference that filters the data and then send only the interesting data to the cloud
[2262.88 --> 2268.26]  for, for further processing. And then finally, there may be privacy constraints that, that limit your
[2268.26 --> 2272.94]  ability to send stuff up to the cloud. You may want to handle things locally to avoid sharing data that
[2272.94 --> 2276.54]  you don't want to share. So I think there are a lot of reasons why you want to do inference in these
[2276.54 --> 2281.38]  embedded devices, almost no reason why I think you would want to do training there. And in the case
[2281.38 --> 2287.16]  where, where you are doing inference in the embedded devices, that often has very strong energy efficiency
[2287.16 --> 2292.02]  constraints. They may be battery operated, they may, you know, need to run for a long period of time
[2292.02 --> 2296.70]  without being, being recharged. And so the efficiency demands are even higher than, than for
[2296.70 --> 2302.10]  inference in the cloud. Yeah, I've actually run into that myself in terms of those, the battery
[2302.10 --> 2308.06]  constraints doing inferencing on mobile devices. You know, we we've covered so much ground. If you
[2308.06 --> 2313.54]  are a software developer, or maybe a data scientist who's doing software development and the engineering,
[2313.54 --> 2318.08]  and, and you're looking at all of these things that we have been talking about, kind of from an app
[2318.08 --> 2323.30]  dev perspective, you know, from training and the hardware working on the edge, the different tools,
[2323.30 --> 2329.44]  CUDA, you name it, what are the things that the necessary skills that people should be thinking
[2329.44 --> 2335.10]  about? So many people are kind of self training themselves into this. And there is there is so
[2335.10 --> 2341.54]  much for a person who's just trying to get into AI to learn, how would you structure that if somebody
[2341.54 --> 2345.60]  is trying to self train them into this field? Well, I think actually, what you need to know to be
[2345.60 --> 2350.86]  successful in AI falls into two categories. One is basic knowledge. And the other is very practical,
[2350.86 --> 2355.10]  how to information. For the basic knowledge, I think what's most important is having a really
[2355.10 --> 2359.96]  strong background in mathematics, and particularly in statistics and probability theory, because that's
[2359.96 --> 2365.88]  what all of AI is based on. It's, you know, you're basically, you know, doing statistical estimation of
[2365.88 --> 2371.60]  a number of things. And then the practical side of it is knowing how to use the tools that are
[2371.60 --> 2375.14]  available, whatever your favorite framework is, whether it's PyTorch, or whether it's TensorFlow,
[2375.72 --> 2380.70]  having the practical knowledge to, you know, get a model, get a data set and run the tools to
[2380.70 --> 2386.46]  train it. So since you mentioned that, I'm just just curious, because Daniel and I have used
[2386.46 --> 2391.52]  different tools. Do you have any personal favorites that you like to use? Not suggesting anything that
[2391.52 --> 2395.92]  you say is the right thing that everybody should do. But we always like to find out what people's
[2395.92 --> 2399.60]  preferences are. I don't really have any strong preferences. I have to confess that I actually
[2399.60 --> 2405.00]  don't do that much coding myself anymore. And the people I work with, often, you know, migrate to
[2405.00 --> 2408.66]  one or another for different reasons. A lot of people use PyTorch, because they like to sort of work
[2408.66 --> 2414.34]  from the Python base. Many people use TensorFlow. I think it is probably the most popular framework
[2414.34 --> 2415.36]  overall these days.
[2415.90 --> 2421.90]  Yeah. And I'm sure a lot of the frameworks that your team uses, and also the tools that they
[2421.90 --> 2426.58]  generate and the research that they generate, I'm sure a lot of that uses open source tools,
[2426.58 --> 2429.92]  like you've already mentioned. Are there any things that you'd like to highlight that, you know,
[2429.98 --> 2436.46]  NVIDIA is kind of doing on the open source front that maybe our listeners could go and check out
[2436.46 --> 2439.06]  and potentially start playing around with?
[2439.36 --> 2443.58]  So one thing I'll highlight, actually, is our deep learning accelerator. If your listeners go
[2443.58 --> 2447.92]  to nvdla.org, if they actually want to play with hardware for deep learning, they can download the
[2447.92 --> 2452.96]  RTL for that accelerator, customize it to their needs, include it into either an FPGA or an ASIC of
[2452.96 --> 2458.62]  their own design. We also open source a lot of software that comes out of our research. So,
[2458.74 --> 2464.18]  you know, for example, our work on progressive generative adversarial networks, progressive GANs,
[2464.18 --> 2469.88]  our work on networks that we use for optical flow, our work on denoising, all of those networks have
[2469.88 --> 2475.46]  been open sourced. So people can very easily replicate our results and apply those new methods
[2475.46 --> 2477.02]  that we've developed to their own problems.
[2477.88 --> 2483.86]  Awesome. Yeah, that's super helpful. And we'll make sure and include some links in our show notes
[2483.86 --> 2489.50]  to that. As we wrap up here and get to the end of our conversation, once again, I really appreciate
[2489.50 --> 2495.14]  all of the perspective on these different things. It was really helpful for me, I know. I was wondering
[2495.14 --> 2501.50]  if you have any parting thoughts or kind of inspiring thoughts for the listeners, assuming that our
[2501.50 --> 2507.44]  listeners are kind of either already in or getting into the AI field and kind of trying to find their
[2507.44 --> 2512.72]  place and find, you know, what people are working on. Do you have any parting thoughts for them or
[2512.72 --> 2513.44]  encouragements?
[2513.44 --> 2518.30]  You know, I think it's just a very exciting time to be working in AI because there are so many new
[2518.30 --> 2523.04]  developments happening every day. It's never a dull place. It's, in fact, so much stuff happening
[2523.04 --> 2526.82]  that's hard to keep up. As a hardware engineer, I think it's also very rewarding to know that this
[2526.82 --> 2531.78]  whole revolution in deep learning has been enabled by hardware. All of the algorithms, you know,
[2532.10 --> 2538.20]  convolutional nets, multi-layer perceptrons, training them using stochastic gradient descent and
[2538.20 --> 2542.74]  backpropagation, all of that has been around since the 1980s, since ICE first started playing with
[2542.74 --> 2548.38]  neural networks. But it wasn't until we had GPUs that it was really practical. GPUs basically were
[2548.38 --> 2552.82]  the spark that ignited the revolution. You know, the three ingredients were the algorithms,
[2553.32 --> 2558.40]  the large data sets. Those were both there, but then you needed the GPUs to make it work. It wasn't,
[2558.56 --> 2564.86]  you know, for computer vision, it wasn't until AlexNet in 2012, where using, you know, GPUs,
[2564.88 --> 2570.40]  he was able to train a network to win the ImageNet competition that deep learning really took off. So I think
[2570.40 --> 2574.70]  GPUs are what ignited this, and I think GPUs are still really the platform of choice,
[2575.04 --> 2580.06]  because with the TensorCores, they provide the efficiency of special purpose units, but without
[2580.06 --> 2585.70]  the inflexibility of a hardwired ASIC like a TPU. So you get the best of both worlds. You can program
[2585.70 --> 2591.04]  in CUDA, but get the efficiency of a TensorCore. Well, thank you very much, Bill. For me, I have
[2591.04 --> 2595.50]  learned so much on this episode that I'm probably going to have to go back and listen to it a couple of
[2595.50 --> 2599.82]  times to take in everything that you've taught us today. It's been really packed with incredible
[2599.82 --> 2603.88]  information. So thank you very, very much for coming on. Oh, it's my pleasure. Thank you.
[2604.24 --> 2608.96]  And with that, we'll look forward to our next episode. I hope our listeners got as much out
[2608.96 --> 2615.48]  of it as Daniel and I did. Daniel, are you doing good? Yeah, I've got a bunch of websites pulled up
[2615.48 --> 2622.50]  that I'm going to start reading afterwards. So it was a great time, and we'll talk to you again next
[2622.50 --> 2629.10]  week. Great. Thank you very much, Bill. All right. Thank you for tuning into this episode
[2629.10 --> 2633.26]  of Practical AI. If you enjoyed this show, do us a favor, go on iTunes, give us a rating,
[2633.54 --> 2637.22]  go in your podcast app and favorite it. If you are on Twitter or a social network,
[2637.32 --> 2640.66]  share a link with a friend, whatever you got to do, share the show with a friend if you enjoyed it.
[2640.96 --> 2646.06]  And bandwidth for ChangeLog is provided by Fastly. Learn more at Fastly.com. And we catch our
[2646.06 --> 2649.68]  errors before our users do here at ChangeLog because of Rollbar. Check them out at
[2649.68 --> 2655.44]  Rollbar.com slash ChangeLog. And we're hosted on Linode cloud servers. Head to Linode.com slash
[2655.44 --> 2660.44]  ChangeLog. Check them out. Support this show. This episode is hosted by Daniel Whitenack and
[2660.44 --> 2666.20]  Chris Benson. Editing is done by Tim Smith. The music is by Breakmaster Cylinder. And you can find
[2666.20 --> 2671.18]  more shows just like this at ChangeLog.com. When you go there, pop in your email address,
[2671.48 --> 2676.50]  get our weekly email, keeping you up to date with the news and podcasts for developers in your inbox
[2676.50 --> 2679.60]  every single week. Thanks for tuning in. We'll see you next week.
