[0.00 → 4.94] There's literally billions of ways in which you can compile the same model on the same hardware target.
[5.28 → 7.20] The question is, how do you pick the fastest one?
[7.46 → 9.82] You cannot try them all because that will take too long.
[10.12 → 11.82] So you have to use intuition.
[12.20 → 13.88] That's what software engineers do.
[14.16 → 18.42] We replace that intuition with machine learning-based optimizations
[18.42 → 21.78] that learn about how the hardware behaves in the press of optimization
[21.78 → 24.58] and uses those models of how the hardware behaves to tune
[24.58 → 28.28] and search the right way of optimizing and compiling your model to the hardware target.
[30.00 → 33.92] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[34.28 → 36.34] We love Linde. They keep it fast and simple.
[36.48 → 38.84] Check them out at linode.com slash changelog.
[39.06 → 41.14] Our bandwidth is provided by Vastly.
[41.48 → 45.04] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[45.30 → 47.00] Get a demo at LaunchDarkly.com.
[49.98 → 52.50] This episode is brought to you by our friends at O'Reilly.
[52.86 → 55.46] Many of you know O'Reilly for their animal tech books and their conferences,
[55.46 → 59.00] but you may not know they have an online learning platform as well.
[59.00 → 63.82] The platform has all their books, all their videos, and all their conference talks.
[64.16 → 68.34] Plus, you can learn by doing with live online training courses and virtual conferences,
[68.84 → 73.00] certification practice exams, and interactive sandboxes and scenarios
[73.00 → 74.94] to practice coding alongside what you're learning.
[75.20 → 79.94] They cover a ton of technology topics, machine learning, AI, programming languages,
[80.48 → 84.62] DevOps, data science, cloud, containers, security,
[84.62 → 88.88] and even soft skills like business management and presentation skills.
[89.00 → 90.78] You name it, it is all in there.
[91.10 → 94.34] If you need to keep your team or yourself up to speed on their tech skills,
[94.44 → 96.26] then check out O'Reilly's online learning platform.
[96.80 → 100.36] Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[100.52 → 102.76] Again, O'Reilly.com slash changelog.
[102.76 → 116.60] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[116.90 → 118.64] productive, and accessible to everyone.
[119.06 → 123.04] This is where conversations around AI, machine learning, and data science happen.
[123.42 → 126.60] Join the community and Slack with us around various topics of the show
[126.60 → 129.42] at changelog.com slash community and follow us on Twitter.
[129.42 → 131.16] We are at Practical AI FM.
[132.76 → 140.54] Welcome to another episode of Practical AI.
[140.94 → 142.96] This is Daniel Whiten ack.
[143.06 → 146.44] I am a data scientist with SIL International,
[146.74 → 149.64] and I'm joined as always by my co-host, Chris Benson,
[149.90 → 154.00] who is a principal emerging technology strategist at Lockheed Martin.
[154.32 → 154.98] How are you doing, Chris?
[155.38 → 156.62] I'm doing very well.
[156.68 → 158.38] A little bit chilly here in Atlanta.
[158.38 → 159.56] I don't know what's going on with that.
[159.62 → 161.44] Mid-May, we're supposed to be sweltering heat.
[161.44 → 164.02] Yeah, it's a little bit chilly here as well.
[164.18 → 164.66] I don't know.
[164.84 → 166.50] What's chilly for Atlanta, though?
[166.60 → 167.96] Depends on your reference frame.
[168.22 → 168.58] I don't know.
[168.62 → 171.82] I'm guessing it's like 60 out there or something like that, you know.
[171.94 → 172.20] Okay.
[172.32 → 174.46] That sounds pretty delightful to me, actually.
[175.32 → 180.30] I mean, if it's not 85 by now, it's just not normal.
[180.66 → 180.96] So yeah.
[180.96 → 182.92] Well, what are you keeping busy with these days?
[182.92 → 186.84] Just lots of technology stuff at work, having a good time with it.
[187.00 → 193.28] And I'm super excited to pause in my day job so that we can have a good conversation about AI ML.
[193.58 → 194.22] Yeah, yeah.
[194.32 → 201.92] And specifically, I know in my job recently, we've been working on a few different deployments of the same model.
[201.92 → 206.54] One to like an edge device, which is disconnected from the internet.
[207.00 → 208.54] One cloud deployment.
[208.90 → 211.48] And then another one for an on-prem system.
[211.96 → 217.56] And that carries with it, of course, all sorts of joy in terms of fitting into resource constraints,
[217.56 → 221.44] but also optimizing a model for different deployments.
[222.00 → 226.98] And I think that's definitely one thing that I don't know if anyone ever pitched being a data scientist to me,
[226.98 → 231.34] but I don't know if that was part of the pitch, like optimizing for certain hardware and all that.
[231.58 → 235.10] It's cool, but it's definitely sometimes laborious and hard.
[235.48 → 237.12] I don't know if you've run into this in your past.
[237.30 → 241.18] Yeah, you have to be a data scientist and a software engineer to do that, right?
[242.30 → 244.46] You know what struck me as you were saying that, Daniel?
[244.54 → 249.26] The thing is, is I'm kind of doing a similar thing, but being in the defence industry,
[249.26 → 252.38] we have a completely UN-software-like name for it.
[252.40 → 254.58] We call that joint all-domain operations.
[254.58 → 257.64] Nobody outside this world would ever, they're like, that's software?
[258.00 → 258.22] Really?
[258.44 → 259.16] That's AI?
[259.40 → 259.62] Really?
[259.82 → 261.04] Wait, what acronym is that?
[261.40 → 262.56] Yeah, that's what we call it.
[262.60 → 263.40] We call it JADE.
[263.86 → 264.42] JADE.
[264.60 → 266.46] We call it JADE and stuff.
[266.64 → 267.46] But you'd never know.
[267.58 → 272.20] I don't think anyone outside my industry would ever associate JADE or joint all-domain operations
[272.20 → 274.26] with software and Kubernetes and AI deployment.
[275.08 → 279.26] I would have no idea what that meant if you gave those words to me.
[279.62 → 283.30] But I think we'll both be enlightened today quite a bit on this subject.
[283.30 → 290.42] I'm really excited because we have Luis Cede with us, who is co-founder and CEO of Octal
[290.42 → 293.50] and professor at University of Washington.
[293.98 → 294.68] Welcome, Luis.
[294.88 → 295.24] Thank you.
[295.34 → 296.48] Thanks for having me on the show.
[296.58 → 298.04] It sounds like you guys are fun to talk to.
[298.12 → 299.66] Can't wait for the conversation here.
[300.12 → 303.02] And it's a nice sunny day in Seattle, by the way.
[303.16 → 305.08] We don't take ourselves too seriously, trust me.
[305.38 → 305.88] Oh, good.
[305.92 → 306.54] I love that.
[306.60 → 307.84] That makes it even better.
[307.84 → 313.12] Just to finish the weather theme of the conversation, it's a nice sunny day in Seattle in the 70s,
[313.18 → 316.20] you know, so I'm wearing shorty shirts here.
[316.88 → 317.68] What's up with that?
[317.74 → 321.40] He's in Seattle, and he's having the great weather and, you know, Seattle's famous for rain.
[321.48 → 324.44] And we're here in these other parts of the country, and it's just kind of, eh.
[324.62 → 325.22] Isn't it though?
[325.32 → 326.78] I mean, Luis, correct me if I'm wrong.
[326.88 → 330.80] I mean, summer times in the Pacific Northwest are quite delightful, aren't they?
[330.80 → 333.66] It's just like the winter, like rain and fog.
[333.86 → 334.94] That does sound nice.
[335.10 → 335.26] Yeah.
[335.36 → 335.58] Yeah.
[335.64 → 336.22] That's great.
[336.70 → 336.86] Yeah.
[336.94 → 338.64] Winters are long, but the summers are awesome.
[338.76 → 342.50] So there's some balance in the universe and nature here, especially for a native Brazilian
[342.50 → 344.08] like me, that matters, you know?
[344.28 → 347.18] So happy and nice summer.
[347.38 → 347.48] Yeah.
[347.86 → 349.32] Well, thanks again for having me on the show.
[349.38 → 352.70] It sounded like from your adventures with machine learning model deployments, we're going
[352.70 → 354.02] to have a lot to talk about here.
[354.38 → 354.40] So.
[354.66 → 355.66] Yeah, for sure.
[356.02 → 360.40] So before we get into all that, maybe you could just give us a bit of a background on yourself
[360.40 → 364.78] and how you got interested in this topic and ended up working in the areas that you're
[364.78 → 367.80] working now from your moment of birth right up until this recording.
[368.24 → 368.64] Exactly.
[368.80 → 369.00] Great.
[369.10 → 369.28] Perfect.
[369.38 → 371.44] So as I was mentioning before, I grew up in Brazil.
[371.66 → 375.56] And the funny thing is, I like to joke that I'm in the 20th year of a three-month internship
[375.56 → 376.30] in the US.
[376.40 → 377.64] I was in school in Brazil.
[378.00 → 379.68] I was recruited by IBM Research.
[380.10 → 382.66] This is in the early 2000s to work on the Blue Gene Project.
[382.94 → 387.54] There was a three-month internship that became a year-long co-op that one thing leads to an
[387.54 → 387.72] accident.
[387.72 → 390.74] I went to grad school in Campaign-Urbana, Illinois, close to where you are.
[390.94 → 393.24] And then after that, I came to University of Washington as a professor.
[393.44 → 395.34] And next thing I know, 20 years have gone by.
[395.92 → 399.02] So anyway, at IBM, I worked on hardware software co-design.
[399.20 → 402.98] We were part of this team building the Blue Gene machine, the first Blue Gene machine.
[403.54 → 408.16] And this was like hardware and software design for, you know, very high-performance
[408.16 → 409.52] molecular dynamics simulation.
[409.88 → 414.10] And a lot of it, like if you look at the kind of workloads that we ran there, was high-performance
[414.10 → 415.54] linear algebra, right?
[415.58 → 421.52] And then you have HPC systems with all sorts of internal communications, reductions, pair-wise
[421.52 → 422.82] communication, and so on.
[422.82 → 424.76] So after IBM, I went to grad school.
[424.88 → 429.90] In grad school, I did work on hardware and compiler support for speculative parallelization,
[430.04 → 434.06] essentially making it easier for folks to write parallel code by not having to prove that
[434.06 → 435.18] the code is actually parallel.
[435.40 → 436.34] And then I came to UW.
[436.54 → 439.14] At UW, I started in my faculty career.
[439.14 → 442.68] I started working on, you know, hardware software co-design for emerging applications.
[443.28 → 445.46] So I had done a bunch of work on approximate computing.
[445.90 → 450.14] Essentially, the idea is to take advantage of the fact that some applications don't have
[450.14 → 453.00] to have perfect execution to have a meaningful and useful answer.
[453.70 → 455.12] So, right, simulations are like that.
[455.16 → 456.50] There are multiple valid outputs.
[456.90 → 459.62] And of course, machine learning is a huge workload in that category.
[459.74 → 460.88] That's how it started, actually.
[460.96 → 465.02] So I started working on hardware and software optimized for machine learning, for energy
[465.02 → 466.40] efficiency, better performance.
[466.40 → 472.76] And then about six years or so ago, I started collaborating with folks in the core machine
[472.76 → 473.86] learning group here at UW.
[474.42 → 478.60] Carlos Gaston, who's a friend of mine, also Brazilian, you know, Brazilian transplant to
[478.60 → 479.14] the U.S.
[479.44 → 482.60] Although he's Brazilian, Argentinian, transplanted to the U.S.
[482.60 → 484.88] and, you know, has a long history in machine learning systems.
[485.26 → 489.96] And we were chatting six years ago, so there was already a growing set of machine learning
[489.96 → 493.18] models that people are interested in and a growing set of hardware targets.
[493.18 → 497.60] You know, it's kind of crazy to think about that, you know, six years ago, GPUs were just
[497.60 → 499.42] starting to get popular for machine learning.
[499.74 → 501.32] It feels like that has always been the case.
[501.46 → 504.84] But, you know, six years ago, that was just like, kind of like picking up, right?
[505.16 → 506.22] And people were starting to think about it.
[506.36 → 507.44] A lot's happened since then.
[507.56 → 508.22] I know, yeah.
[508.36 → 511.38] So, and then now we had those CPUs, you know, GPUs are picking up.
[511.44 → 514.76] People started talking about the FPGAs they had for a while, but at that time was getting
[514.76 → 515.60] heated again.
[515.60 → 518.24] And then people started talking about building accelerators.
[518.44 → 523.16] So we were wondering like, oh, kind of interesting that there is this growing set of models already
[523.16 → 527.54] starting to fragment ecosystem with TensorFlow, PyTorch doesn't quite exist yet, but there
[527.54 → 530.28] was already some fragmentation going on and a growing set of hardware targets.
[530.38 → 534.30] So now imagine this cross product of models, frameworks, and hardware targets.
[534.30 → 537.78] It's already becoming a pretty complex cross product.
[537.78 → 541.82] So we started thinking about, oh, wouldn't it be nice if we had a common intermediate
[541.82 → 546.66] representation that allows you to do high level model optimization, do, and generate
[546.66 → 550.58] special, specialized code for that model on specific hardware targets.
[551.40 → 557.32] So, and TNC Chen, who's an incredible machine learning systems researcher, was Carlos's grad
[557.32 → 558.08] student at that time.
[558.24 → 560.22] And Carlos and I started co-advising TNC.
[560.40 → 565.76] And that's, that was the genesis of, you know, let's look at machine learning model optimization
[565.76 → 569.30] and compilation as a way to actually optimizing the machine learning models.
[569.30 → 574.76] And I had other grad students there, Terry Moreau, who was working on specialized architectures
[574.76 → 576.36] for machine learning, got interested as well.
[576.54 → 581.04] So he quickly became part of the mix and started working on FPGA backends for machine learning
[581.04 → 581.98] models as part of this mix.
[582.04 → 583.20] So that's how I got into that.
[583.50 → 586.94] In the end, everything boils down to high-performance linear algebra, say for machine learning.
[587.00 → 591.18] And I had a history with that at IBM and everything kind of came together, approximate
[591.18 → 595.66] computing, high-performance linear algebra, and machine learning in this, in the genesis of the
[595.66 → 596.36] TVM project.
[596.80 → 597.36] Awesome.
[597.92 → 600.84] And maybe we could just sort of take a step back.
[600.90 → 603.44] You talked about like machine learning compilers.
[603.60 → 605.38] We talked about intermediate representation.
[605.68 → 611.62] Maybe for that person out there that has taken the Coursera course, and they went through the
[611.62 → 616.86] Coursera course on deep learning something and, hey, it never talked about machine learning
[616.86 → 617.50] compilers.
[617.50 → 623.38] They learned maybe how to do a training thing, and they created an image classifier and then
[623.38 → 627.92] they learned how to do an NLP thing and do autocomplete or something.
[628.42 → 632.98] And then they end the course, and they know how to use TensorFlow and do some data preprocessing
[632.98 → 635.98] stuff and maybe even a little bit about GPUs.
[636.06 → 638.64] But they never heard this machine learning compiling.
[638.80 → 641.62] Could you just sort of, yeah, where does that fit in?
[641.90 → 642.12] Yeah.
[642.30 → 643.56] I'm going to translate all of that.
[643.62 → 646.34] You're basically saying, wow, I'm really missing the audience here.
[646.42 → 648.08] Like, let me translate all of that here.
[648.30 → 648.60] So, all right.
[648.60 → 652.88] When you write a typical machine learning model, by the way, I'm really glad that machine
[652.88 → 654.92] learning tools are becoming more and more accessible.
[655.10 → 659.62] More and more people can build meaningful and useful machine learning models, either starting
[659.62 → 661.84] from an existing one or tweaking and creating new ones.
[662.18 → 664.74] I'm so glad that the tools are getting much better for that.
[665.08 → 668.22] But now when you create a machine learning model, though, in the end, you need this model
[668.22 → 671.94] to actually run well on whatever hardware device you want them to run, right?
[671.94 → 678.74] So today, this is typically done by having a set of libraries that implement parts of
[678.74 → 683.58] your model, like, you know, different layers will have different, often hand-coded implementations.
[683.68 → 688.30] And then your high-level framework, like TensorFlow or PyTorch, just gets your model and calls
[688.30 → 693.54] these hand-tuned libraries that either NVIDIA provided or AMD or Intel.
[693.86 → 695.72] The hardware vendors typically provide those libraries.
[695.96 → 700.54] And then the frameworks stitch everything together to produce the thing that runs on your
[700.54 → 701.26] hardware, right?
[701.26 → 703.50] So, which is all well and good.
[703.60 → 707.94] It's nice and easy as being, you know, being able to build pretty complex systems that way.
[708.34 → 713.48] Except that now, as we build richer and richer and more complex machine learning models that
[713.48 → 718.34] really need to make the most out of the hardware they are deployed to, which is great.
[718.46 → 723.54] Like, so it's kind of crazy that you can build gigantic language models or very complex computer
[723.54 → 725.74] vision models that do a ton of computation.
[725.94 → 731.24] That's really pushing the limit of how fast you could run, you know, just by writing on more
[731.24 → 731.90] software's law, right?
[731.94 → 734.72] So we need to be able to squeeze much more performance out of that.
[735.32 → 737.58] So that's where a machine learning compiler comes into play, right?
[737.64 → 742.38] So when you write a piece of code in a language like C, for example, you run through a compiler
[742.38 → 743.98] and you run it on your hardware.
[744.06 → 745.82] You don't even think about, yeah, you run through a compiler, you run it.
[745.82 → 747.84] But for machine learning, we don't do that, right?
[747.88 → 749.38] So you just interpret the model.
[749.94 → 754.46] What a machine learning compiler does is essentially treats this process of going from your model
[754.46 → 756.98] to what runs on your hardware as a compiler problem.
[757.50 → 758.36] What do you mean by that?
[758.40 → 763.98] I mean, by translating your model into a representation, as we call it, intermediate representation, that
[763.98 → 766.26] enables optimizations of your model.
[766.26 → 772.82] For example, you could fuse a layer with an X one, say a fully connected layer, which would
[772.82 → 776.24] be matrix multiplication followed by a convolution that you choose in your model.
[776.36 → 782.24] Potentially, you can fuse them, treat them as a unit and generate nice, new, fresh code
[782.24 → 785.58] that specialize to your model to run on your hardware target.
[786.00 → 790.14] So, and then as a machine learning compiler, what you get as an end user, the benefit that
[790.14 → 794.72] you get is your model becomes a highly optimized executable for your target hardware.
[794.72 → 800.42] And the difference of performance can be huge, like two, three, sometimes 30, 50 X better
[800.42 → 806.26] performance than your stock high level framework execution time and speed, right?
[806.36 → 807.28] So does that make sense?
[807.36 → 811.00] Essentially, you treat that basically what you take for granted in writing regular software,
[811.18 → 813.90] you know, it does that for you in machine learning, right?
[813.94 → 817.36] So it produces a fresh, highly optimized binary for your model.
[817.80 → 817.88] Yeah.
[818.04 → 819.62] And that makes a lot of sense.
[819.62 → 826.60] And it sounds like a lot of what we're talking about here is performance in the sort of maybe
[826.60 → 829.60] latency and resource consumption type realm.
[829.76 → 834.10] When we're thinking about compiling, is that mostly what we're concerned with?
[834.10 → 840.90] Or do some of these compilations, like for example, does the actual performance of like
[840.90 → 845.48] the model's predictions, does that ever come into play when you're doing this sort of optimization
[845.48 → 846.12] as well?
[846.36 → 846.88] Great question.
[846.88 → 848.66] So performance here is ambiguous.
[848.86 → 852.38] For a computer systems person, performance typically means how fast it runs.
[852.58 → 856.38] But for a data scientist, performance also means how good is statistical properties of
[856.38 → 857.00] your model, right?
[857.08 → 861.32] So by and large, machine learning compilers do not change the accuracy of your model.
[861.50 → 862.54] There are optimizations.
[862.66 → 864.44] For example, you can do automatic quantization.
[864.84 → 868.34] You can quantize parameters in your model that can change the behaviour of your model.
[868.72 → 874.30] In that case, you do trade off some accuracy for better execution time or for better system
[874.30 → 875.56] performance, right?
[875.56 → 880.46] But for the most part, in fact, what we focus on in Apache TVM, our transformation optimization
[880.46 → 883.06] do not change the accuracy of your model at all.
[883.16 → 887.28] Even though we do support quantization and so on, by and large, the way it's used is it
[887.28 → 891.60] just compiles our model faithfully to run without any changes in accuracy, right?
[891.76 → 897.00] So to tie back to your comment earlier of deploying multiple hardest, say, you know, deploying on
[897.00 → 902.28] the edge, getting the right performance and using the right amount of resources that fits in
[902.28 → 905.88] your heart is something that's an extremely laborious task, right?
[905.88 → 910.14] So if you have a model that's going to run on a Raspberry Pi-like device, say it's computer
[910.14 → 915.52] vision, and the first version of your model runs at half a frame per second, right?
[915.60 → 921.24] And uses too much memory and doesn't leave any other computer resources for the other things
[921.24 → 922.32] you need to run on your device.
[922.32 → 924.02] You can't really deploy it, right?
[924.14 → 928.56] So, and our experience has been with several users and customers is that the process of
[928.56 → 932.88] getting a model that is ready from a data science point of view, from the accuracy point of
[932.88 → 937.88] view to being able to be deployed, it could take weeks to months of hardcore software engineering
[937.88 → 938.26] work.
[938.32 → 941.86] And that's what we want to automate with Apache TVM.
[942.12 → 944.08] And other machine learning compilers do similar things.
[944.32 → 948.76] But, you know, Apache TVM is just especially good at doing that because it uses essentially
[948.76 → 953.96] machine learning for machine learning, the process of translating your model to an executable,
[954.04 → 955.26] like a deployable artifact.
[955.80 → 957.14] It's a search problem.
[957.14 → 961.62] So there's literally billions of ways in which you can compile the same model on the same
[961.62 → 962.20] hardware target.
[962.54 → 964.46] The question is, how do you pick the fastest one?
[964.72 → 967.08] You cannot try them all because they'll take too long.
[967.50 → 969.08] So you have to use intuition.
[969.40 → 971.14] That's what software engineers do.
[971.28 → 977.10] We replace that intuition with machine learning based optimizations that learn about how the
[977.10 → 981.44] harder behaves in the press of optimization and uses those models of how the harder behaves
[981.44 → 985.70] to tune and search the right way of optimizing and compiling your model to the harder target.
[990.64 → 994.10] This episode is brought to you by Snowplow Analytics.
[994.68 → 998.42] Snowplow is the behavioural data management platform for data teams.
[998.88 → 1004.60] Maximize the value of your behavioural data using Snowplow Insights, a managed data platform
[1004.60 → 1009.48] that's built on leading open source tech leveraged by tens of thousands of users.
[1009.88 → 1014.44] Capture and process high quality behavioural data from all your platforms and your products
[1014.44 → 1017.08] and deliver that data to your cloud destination of choice.
[1017.42 → 1021.88] When marketing needs to make data informed decisions, when product needs next level understanding,
[1022.26 → 1026.84] and when analytics needs rich and accurate data, Snowplow is the solution for data teams
[1026.84 → 1031.80] who want to manage the collection, processing, and warehousing of data across all their platforms
[1031.80 → 1036.80] and products, get started and experience Snowplow data for yourself at snowplowanalytics.com.
[1037.12 → 1039.74] Again, snowplowanalytics.com.
[1053.96 → 1055.82] So Luis, I'm curious.
[1056.06 → 1059.96] There's one of the hardest problems in running this podcast, I think,
[1059.96 → 1064.94] is just the wide variety of jargon that is used throughout all sorts of different areas of ML.
[1065.08 → 1069.18] And I know that on this podcast, we've talked before about model serialization.
[1069.80 → 1075.58] So we've got something like an Onyx project, for example, where, you know, maybe I could,
[1076.06 → 1083.86] quote, save a model to Onyx and maybe like load it into PyTorch or a PyTorch model into TensorFlow.
[1084.18 → 1087.38] It's this sort of overlapping serialization format.
[1087.38 → 1092.20] So as people are thinking about kind of saving and serializing their models,
[1092.54 → 1097.56] where does maybe this compilation fit in terms of the developer workflow?
[1097.76 → 1103.00] Like, let's say that I have my model created, or I've trained it.
[1103.12 → 1107.08] Let's say I'm in TensorFlow, and I've decided on a way to serialize it.
[1107.08 → 1112.36] So I've created a, I've output a file that corresponds to my serialized model.
[1112.56 → 1113.60] What happens next?
[1113.70 → 1119.86] What's the workflow look like after that in terms of Apache TVM and the compilation process?
[1120.08 → 1120.52] Great question.
[1120.70 → 1124.36] So there are many ways in which Apache TVM ingests your model.
[1124.52 → 1126.42] One is exactly what we talked about.
[1126.42 → 1132.44] So there's a front end to Apache TVM that ingests a model that has been serialized into Onyx, right?
[1132.50 → 1137.10] So you just import some model, and then you specify the hardware targets, and then you wait for a little bit
[1137.10 → 1139.26] and then you get your artifact ready.
[1139.38 → 1143.02] You're executable for your model and packaged in various ways.
[1143.36 → 1148.76] But there are also ways in which you can call TVM directly from the code that specifies your model.
[1148.76 → 1153.50] So you can do that from TensorFlow, from PyTorch, from Monet or Keras and so on that you do.
[1153.86 → 1159.14] Essentially, it imports TVM, and then you import, you load your model graph into the TVM representation
[1159.14 → 1161.82] and then you choose your hardware target, and then you compile, right?
[1161.90 → 1167.58] So there's these two ways in which you can interface with TVM, either via, you know, serialized model
[1167.58 → 1170.76] or by just embedding a few lines of code to call TVM.
[1170.92 → 1173.72] So in the flow or from data to your deployed model, right?
[1173.76 → 1177.90] You create the data, curate the data, create a training set, specify your model architecture.
[1177.90 → 1179.58] Sometimes it's a little bit of architecture search.
[1179.88 → 1184.44] You arrive at your model architecture, you train it, and then you're able to actually test and validate your model.
[1184.52 → 1185.44] Then you're happy with it.
[1185.54 → 1188.76] So at that point, your model has the right statistical properties.
[1188.90 → 1190.80] You know it does what it's supposed to do and what you want to do.
[1190.92 → 1192.24] You want to make it run fast, right?
[1192.30 → 1193.68] So now you have a trained model.
[1193.94 → 1199.88] At that point, that's what you hand off to, say, Apache TVM, either via ONIX, serialized models
[1199.88 → 1202.02] or via calling directly the second.
[1202.20 → 1206.46] Then you specify your hardware targets, and then you click compile, right?
[1206.46 → 1210.82] So you call compile, that's when CVM does its high-level and low-level optimization magic
[1210.82 → 1216.14] and also uses this machine learning for machine learning engine to tune the code for your specific
[1216.14 → 1217.42] model on your hardware target.
[1217.84 → 1218.66] So I'm curious.
[1218.96 → 1222.50] I got maybe several questions that I'm going to try to combine into one a little bit.
[1222.52 → 1224.20] And you can segment them any way you want.
[1224.58 → 1228.30] If you go through that optimization process, A, what does that output look like?
[1228.30 → 1234.06] How is that different from the model before you took it through the optimization process
[1234.06 → 1236.88] in terms of how you approach inference on it?
[1237.18 → 1242.60] And what are the limits in terms of that target architecture that you're trying to hit?
[1242.64 → 1243.90] You mentioned the Raspberry Pi.
[1244.06 → 1249.96] And in this day and age, there are tons and tons of kind of low capability or low power targets
[1249.96 → 1253.22] that you might want to run a model that otherwise would have been impossible.
[1253.22 → 1258.68] Can you describe kind of what that looks like after that optimization and what the limits are on it?
[1259.06 → 1259.44] Yeah, great.
[1259.54 → 1261.50] Okay, so let me tell first what it looks like.
[1261.64 → 1265.08] So the output is really an executable.
[1265.26 → 1267.72] It's just an executable code for your model.
[1267.84 → 1272.22] That includes, you know, your model, executable for your model plus a runtime.
[1272.58 → 1276.92] Like the runtime would be like support for your model that's tuned for that hardware target.
[1277.02 → 1281.02] And with CVM, you get a custom packaged binary for your model.
[1281.02 → 1284.08] The way you call it, you load that binary and then there's an API to call.
[1284.38 → 1285.32] It could be a shared library.
[1285.40 → 1290.86] For example, one way of packaging this whole thing up is a .so library or a DLL in Windows
[1290.86 → 1295.10] where your model is just fresh executable code with an API that you call to do inference on.
[1295.26 → 1295.94] Does that answer your question?
[1296.04 → 1297.62] This is what it looks like as the output.
[1297.72 → 1299.14] And then there are many ways of making it standard.
[1299.38 → 1302.56] Like you can put it in a Python wheel and have Python bindings for it.
[1302.66 → 1304.92] There are many ways to make it easy to call it.
[1305.06 → 1305.86] Yeah, it does.
[1306.00 → 1309.08] Like as a follow-up, and I'm going to say something extreme,
[1309.08 → 1311.78] as we're building bigger and bigger models, and we're taking, you know,
[1311.80 → 1315.18] things like GPT-3 and things that are very large.
[1315.58 → 1321.44] And we have this once upon a time unrealistic expectation of putting them into places that you would be like.
[1321.52 → 1324.40] I think Chris wants to run GPT-3 on his smartwatch.
[1324.56 → 1327.10] You are closer than you realize on that one.
[1328.10 → 1329.00] So absolutely.
[1329.14 → 1331.10] And we had people asking about this.
[1331.18 → 1332.46] Yeah, there's a limit to that, right?
[1332.48 → 1335.20] So you can't get around physics, right?
[1335.20 → 1338.68] So even if you compress a maximum, if it doesn't fit in the memory that you have, it just doesn't fit.
[1338.80 → 1339.04] Understood.
[1339.18 → 1343.82] Or if it uses, you know, so much compute that it's going to take too long to do the inference,
[1344.14 → 1346.20] you know, that it's not going to be a useful output, right?
[1346.32 → 1349.68] And of course, in the process of searching what hardware makes sense,
[1350.10 → 1351.86] you can use a tool like the Optimizer.
[1352.06 → 1353.52] Let me just put a quick plug in here.
[1353.70 → 1357.40] So Optimizer is a software-as-a-service platform that Ottoman built
[1357.40 → 1359.56] that uses Apache TVM as its engine.
[1359.56 → 1364.32] And it's like a very easy-to-use, you know, TVM, as you can tell, business conversation.
[1364.54 → 1370.02] It's likely to be a more sophisticated stack for, you know, more general data scientists, right?
[1370.14 → 1373.66] So in general data scientists already have enough to worry about.
[1373.78 → 1376.32] Making models that do the right thing is what they should focus on.
[1376.52 → 1379.98] With the Optimizer, we are raising level abstraction to match that.
[1380.12 → 1381.10] So you can upload your model.
[1381.20 → 1383.98] It's a nice graphical user interface where you upload your model.
[1384.10 → 1385.28] It tells you what the layers are.
[1385.40 → 1386.34] You tell what the input layer is.
[1386.38 → 1387.98] You can click on the harder targets that you want.
[1387.98 → 1390.98] Or you can have it choose for you by running across them all
[1390.98 → 1393.36] and see which ones it runs best at.
[1393.44 → 1395.22] So you can get the highest throughput per dollar.
[1395.60 → 1398.74] Or you can hit the, you know, we do support Raspberry Pis now.
[1398.84 → 1400.06] So you said, does it run a Raspberry Pi?
[1400.14 → 1402.32] If it doesn't, it's just going to say, hey, I couldn't run this model there.
[1402.50 → 1406.94] So then you know that even doing all this magic, it does not run at a higher target, right?
[1407.04 → 1409.10] So anyway, so back to what you're asking.
[1409.24 → 1410.78] So now on the limits, how do we know?
[1411.00 → 1412.26] We can get around physics, right?
[1412.26 → 1415.60] So there's only so much compute resources that you can afford in an edge setting.
[1415.60 → 1420.08] But there are plenty of new techniques that actually can twist and turn your model to
[1420.08 → 1420.58] make it fit.
[1420.72 → 1424.24] One, for example, specifically for language models that you brought up, something that
[1424.24 → 1427.70] we've done quite a bit of work on, is support for sparsity, right?
[1427.76 → 1431.22] So these language models are giant, but there are a lot of zeros in it.
[1431.34 → 1433.94] So as we all know, lots of zeros, easy to compress, right?
[1434.02 → 1437.62] So if you're going to multiply something by zero, you don't even need to multiply it, right?
[1437.72 → 1441.36] So, and if it's a bunch of zeros, why are you going to write a bunch of zeros in memory?
[1441.44 → 1444.52] Just say like, hey, you know, only write the non-zero values.
[1444.52 → 1445.94] Sure, you can do that.
[1446.00 → 1450.40] And that actually goes a long ways in using less memory and using less compute.
[1450.84 → 1455.40] I wouldn't go as far as saying that we can quite run GPT-3-like models on Cine device,
[1455.56 → 1460.42] but we're getting close to running pretty large models because of good sparse computing supports
[1460.42 → 1465.18] and also, you know, other forms of compression and quantization that makes big models fit in
[1465.18 → 1465.78] edge devices.
[1466.14 → 1469.16] So just to follow up on the inference side of things.
[1469.16 → 1474.46] So maybe this is part of what you're building with Octal, because like you were saying,
[1474.54 → 1477.98] Apache TVM, maybe it's a lower level thing for real experts.
[1478.16 → 1480.08] Octal maybe is some-
[1480.08 → 1480.92] More accessible, yeah.
[1480.98 → 1482.76] Has a bunch of convenience built in.
[1482.84 → 1482.98] Yeah.
[1483.34 → 1487.64] So I'm curious on that inference side, maybe you could contrast the two.
[1487.88 → 1493.86] Like if I compile a model with Apache TVM, you mentioned sort of Python wrappings around
[1493.86 → 1497.54] that output model, and maybe there are other language wrappings.
[1498.10 → 1502.58] Is that as simple as sort of importing a Python library and then importing your compiled
[1502.58 → 1504.84] model and running an inference?
[1505.18 → 1511.84] Or what other sort of workflow changes might you have to do to run Apache TVM compiled model
[1511.84 → 1516.44] in terms of the Python ways that people sort of are used to doing things?
[1516.70 → 1517.80] No, it's exactly what you said.
[1517.86 → 1518.64] It's two lines of code.
[1518.94 → 1523.32] So the results in Python will, you import it, and you call inference on it and that's it.
[1523.32 → 1524.18] That's awesome.
[1524.40 → 1524.54] Yeah.
[1525.06 → 1527.54] And that's the experience that we offer with the Optimizer.
[1527.74 → 1530.84] And then the Optimizer also has an API call, by the way.
[1530.92 → 1536.42] So if you want to embed the model optimization compilation to your workflow, you can use the
[1536.42 → 1537.02] Optimizer.
[1537.40 → 1538.46] I don't mean to give a hard sell here.
[1538.48 → 1539.28] I'm just saying it's super easy.
[1539.40 → 1545.14] Like TVM itself, you have to set up your task framework, have to spin up some instances
[1545.14 → 1549.50] to run this auto-tuning and this optimization tuning component.
[1549.50 → 1553.90] You have to collect the data for the machine learning model-based optimizations and so
[1553.90 → 1554.16] on.
[1554.36 → 1554.94] And it's work.
[1555.04 → 1557.16] It pays off, but it's work you have to put up front, right?
[1557.24 → 1561.06] So with the Optimizer, you can replace that with two lines of code in the API.
[1561.22 → 1567.44] You upload the model via the API, and then you specify your harder targets and then you
[1567.44 → 1568.70] start the optimization process.
[1568.70 → 1573.08] And then when it's ready, you can download the resulting wheel that you can import into
[1573.08 → 1574.32] your workflow, right?
[1574.32 → 1579.26] So you can do all of that either via the web interface or via this API.
[1579.70 → 1579.76] Awesome.
[1579.94 → 1580.12] Yeah.
[1580.22 → 1585.74] So I know I'm super interested in Octal and I know that you're kind of in beta now.
[1585.90 → 1587.58] It doesn't have such a long history.
[1587.76 → 1592.56] So maybe you could tell us, you know, how that came about if it was sort of natural feeling
[1592.56 → 1598.30] some of these pains of the lower level things, you know, expertise in Apache TVM and the desire
[1598.30 → 1601.88] to have that be more automated and have some convenience around it.
[1601.88 → 1604.94] Could you give us a little bit more of the motivation there and your thought process
[1604.94 → 1605.84] with Octal?
[1606.04 → 1606.66] Yeah, absolutely.
[1606.96 → 1607.16] Yeah.
[1607.24 → 1609.92] So maybe I can do a quick once upon a time on Octal as well.
[1610.00 → 1613.92] So we had to work hard on Apache TVM, you know, started as a research project, and it got quite
[1613.92 → 1617.60] a bit of traction, and we've been deployed in, you know, Amazon, Facebook, Microsoft, and
[1617.60 → 1617.96] so on.
[1618.02 → 1621.66] And when running one of our conferences, we're like, oh, wow, there's quite a bit of interest
[1621.66 → 1621.92] here.
[1622.02 → 1626.80] But the folks that were attending were really, you know, machine learning researchers, engineers,
[1626.80 → 1630.14] or, you know, folks that have data science and machine learning experience as well
[1630.14 → 1631.20] as software engineering experience.
[1631.20 → 1633.12] We said, oh, it's cool.
[1633.22 → 1634.58] We want more people to use it.
[1635.04 → 1638.40] And of course, we're going to continue catering and growing the open source community.
[1638.58 → 1643.92] So that's why we formed Octal to invest in Apache TVM and grow the community, grow the
[1643.92 → 1649.30] ecosystem, work closely with hardware vendors to enable more hardware targets on TVM.
[1649.68 → 1653.32] TVM today, you know, has a pretty broad set of hardware targets.
[1653.48 → 1658.88] Like it has, you know, server CPUs from Intel and AMD and ARM CPUs and mobile and server,
[1658.88 → 1659.18] right?
[1659.18 → 1665.80] So NVIDIA GPUs, ARM GPUs, Intel GPUs, AMD GPUs, AMD GPUs.
[1665.80 → 1667.62] We have FPGA support, have a broad set.
[1667.78 → 1672.80] And a lot of these were done with us in partnership with hardware vendors and some hardware vendors
[1672.80 → 1675.06] that go and put the work into the open source package.
[1675.06 → 1679.90] And the reason that I keep emphasizing open source here is that I don't think you'll be
[1679.90 → 1686.74] sustainable to have a project of the diversity that TVM needs or any sort of machine learning
[1686.74 → 1688.06] compiler needs to thrive.
[1688.22 → 1692.50] You want diversity of models that it supports, frameworks and harder targets.
[1692.84 → 1697.00] The only way you make the diversity manageable, in my opinion, is by having an open and welcoming
[1697.00 → 1699.32] community that even competitors can collaborate.
[1699.70 → 1700.90] Kind of like Linux, you know.
[1700.98 → 1702.34] So Linux is a great story of success.
[1702.34 → 1704.84] And that's what we went with TVM.
[1704.98 → 1708.76] So, and what we wanted to do with Octal is enable more hardware targets and work with
[1708.76 → 1713.10] hardware vendors, but then also make the power of TVM and machine learning model optimization
[1713.10 → 1718.12] and compilation accessible to the broadest set of users possible, right?
[1718.18 → 1722.86] And the way we approach that is by building a high-level service that makes it very, very
[1722.86 → 1726.86] easy and fully, you know, so natural that you'd never choose not to use it, right?
[1726.86 → 1729.30] So, and that's really the goal of the Optimizer.
[1729.74 → 1734.86] And we made it into a SaaS offering because machine learning moves fast, as you know, right?
[1734.92 → 1738.68] So models change fast and there's new harder targets almost every other week, right?
[1738.78 → 1742.50] So the best way to do is actually package that into a service because then we can take care
[1742.50 → 1747.36] of all the, you know, complicated lower level things that you don't want your data
[1747.36 → 1748.52] scientists spending time on.
[1748.86 → 1751.68] So you've gotten me pretty excited about it as we've gone through this.
[1751.68 → 1757.30] And how with different people having their practical workflows that they're using and,
[1757.42 → 1761.98] you know whether it's TensorFlow or PyTorch, and they have a deployment string attached to
[1761.98 → 1762.12] it.
[1762.40 → 1765.16] And I know that you've mentioned it targets several frameworks.
[1765.28 → 1767.66] We've talked about, you know, the kind of the two biggies and stuff.
[1768.08 → 1773.42] Can you talk a little bit about how first on the Apache TVM side and then talk about where
[1773.42 → 1779.08] we optimally can use Octal, but try to give me a sense, a practical sense of how do I get
[1779.08 → 1780.12] that into my work stream?
[1780.20 → 1780.78] What do I need?
[1780.78 → 1781.54] What are limitations?
[1782.10 → 1782.94] What should I avoid?
[1783.04 → 1783.72] What should I do?
[1783.90 → 1786.24] I'm just trying to get a sense of how do I get started?
[1786.34 → 1790.08] If I'm listening, you've sold us on what to do here and rubber meets the road kind of
[1790.08 → 1790.30] moment.
[1790.70 → 1791.12] Yeah, absolutely.
[1791.24 → 1796.20] So if you are so inclined, and you want to do some software engineering adventures, you
[1796.20 → 1798.00] should definitely go to tvm.ai.
[1798.22 → 1800.64] There are plenty of tutorials there on how you can get started.
[1801.28 → 1802.44] You know, there's a TensorFlow example.
[1802.56 → 1803.54] There's a PyTorch example.
[1803.70 → 1804.74] There's an Onyx example.
[1805.20 → 1805.88] And you can just go there.
[1805.94 → 1808.30] That's how you use the open source offering there, right?
[1808.30 → 1814.02] So now there are many ways in which you can use open source Apache TVM, right?
[1814.02 → 1818.08] So you can use just as a compiler and know what we call auto-tuning.
[1818.24 → 1822.38] Auto-tuning is the machine learning-based magic that I told you about that searches for better
[1822.38 → 1823.08] implementations.
[1823.58 → 1825.42] For that, you have to do a little bit more work, right?
[1825.42 → 1828.12] So you have to set up a benchmark infrastructure.
[1828.12 → 1831.12] It could be just your machine, but then it takes a little bit longer because it needs to run
[1831.12 → 1832.02] a bunch of experiments.
[1832.48 → 1832.64] It's funny.
[1832.74 → 1834.20] There are tutorials for that.
[1834.56 → 1839.10] If you have more experience with the lower level parts of your framework, and you're ready
[1839.10 → 1843.14] to use, you know, a stack like Apache TVM, I'll start with that route.
[1843.22 → 1844.86] Try and run through the examples there.
[1844.86 → 1850.40] Now, if you have some work to do, and you want to get your model ready quickly, and you want
[1850.40 → 1854.84] to enjoy some automation, you can use the Optimizer because it's a full SaaS offering.
[1855.08 → 1859.12] Then what you do today, the way you support this is you serialize your model to Onyx, you
[1859.12 → 1863.06] upload the model, and then once you upload it, there are all sorts of hardware targets that
[1863.06 → 1863.50] you can click.
[1863.58 → 1867.50] There's a checkbox for NVIDIA GPUs, Intel CPUs, and Raspberry Pi.
[1867.58 → 1871.90] You can choose the ones that you want, and then you click Optimize, and then you get a notification
[1871.90 → 1873.26] when your workflow is done.
[1873.26 → 1877.52] You get all the performance comparison across all the hardware targets and across even different
[1877.52 → 1879.22] ways of compiling your model.
[1879.60 → 1885.44] So between the Optimizer and the, you know, having the baseline open source project, you
[1885.44 → 1889.56] can kind of choose the level of abstraction that you want to get into for what your workflow
[1889.56 → 1889.92] is.
[1890.06 → 1892.08] So you have choice that way, right?
[1892.20 → 1893.18] You do have choice, yes.
[1893.20 → 1895.18] You have choice of how you want to take advantage of that.
[1895.28 → 1899.08] You can go through the Apache TVM routes, you know, then you do it, and we'll support that.
[1899.12 → 1900.66] There's a thriving community that will help you.
[1900.66 → 1904.82] Now, if you really want to get started from day zero and not have to worry about that,
[1904.96 → 1909.28] then you go to the Optimizer, either using the web interface or the API, and then you
[1909.28 → 1910.42] can use our support.
[1910.64 → 1915.62] And you also, you get access to our ready-to-go machine learning models for the hardware targets
[1915.62 → 1916.48] that you care about.
[1916.48 → 1933.28] Changelog++ is the best way for you to directly support practical AI.
[1933.82 → 1939.54] Join today and unlock access to a private feed that makes the ads disappear, gets you closer
[1939.54 → 1944.20] to the metal and help sustain our production of practical AI into the future.
[1945.02 → 1950.94] Simply follow the Changelog++ link in your show notes or point your favourite web browser
[1950.94 → 1953.26] to changelog.com slash plus.
[1953.62 → 1957.46] Once again, that's changelog.com slash plus.
[1959.06 → 1961.22] Changelog++ is better.
[1961.22 → 1975.60] So, Luis, this is fascinating.
[1975.60 → 1979.60] What I'm wondering, one of the things that we mentioned a few times is Onyx.
[1979.80 → 1985.58] And I think that sounds like some of what you're sort of centralizing around with Octal
[1985.58 → 1989.40] is Onyx maybe as a recommendation since you've mentioned it a couple of times.
[1989.40 → 1993.62] Could you maybe just give those who aren't familiar a brief definition of what we're
[1993.62 → 1994.72] talking about with Onyx?
[1994.92 → 2000.58] And also, maybe from your perspective, as someone maybe not working on Onyx day-to-day,
[2000.66 → 2007.12] but working on something that depends on that, how you see that project progressing and the
[2007.12 → 2007.96] momentum with that?
[2008.24 → 2009.26] Great question.
[2009.40 → 2013.74] I want to emphasize that even though I use Onyx several times, we do support directly.
[2013.92 → 2017.30] If you go through TensorFlow or PyTorch and so on, there's no...
[2017.30 → 2022.96] I do tend to like what Onyx aims to do because Onyx is just a way of representing your model.
[2023.52 → 2025.66] Essentially, at the high side, it's a description language.
[2025.86 → 2029.48] So, you can have your model, you built it in memory, you just specify it in whatever framework
[2029.48 → 2030.52] you like to use.
[2030.60 → 2031.74] And you can...
[2031.74 → 2033.18] You want to store it, right?
[2033.20 → 2034.46] So, you need to describe it somehow.
[2034.68 → 2039.58] So, Onyx is an agreed-upon way by, you know, multiple players in the space that this is a
[2039.58 → 2042.08] good way in which you can describe a machine learning model.
[2042.08 → 2047.86] So, that includes the computational structure, your layers, what each operator does, as well
[2047.86 → 2051.86] as all of your parameters gets, you know, serialized in one single package, right?
[2051.98 → 2055.16] So, Onyx is evolving and it has its ups and downs.
[2055.22 → 2058.86] And I think right now, you know, people are getting more excited, and they're so excited
[2058.86 → 2059.20] about it.
[2059.26 → 2059.82] And then there's this...
[2059.82 → 2060.92] I think it's an uptick now.
[2061.20 → 2065.38] I'm sure there'll be other model description languages and exchange formats, right?
[2065.38 → 2069.06] So, that would pop up, and we are ready to support those as well.
[2069.28 → 2074.82] I do think that it's good to have at least one format of storing models that is generally
[2074.82 → 2078.90] adopted, like widely adopted, because then, you know, if you keep your models that way,
[2079.06 → 2083.88] chances are that the software components that you need in your workflow will support your
[2083.88 → 2084.36] model, right?
[2084.48 → 2085.12] So...
[2085.12 → 2087.72] This field is evolving so rapidly right now.
[2087.94 → 2093.04] And you have not only each framework's kind of way of doing things, but like I'm looking
[2093.04 → 2097.30] through the tvm.ai website that you referenced and going through and there's like the Get
[2097.30 → 2100.50] Started with TVM and there are so many different options.
[2100.74 → 2105.42] And I can't help but wonder, you're covering so many architectures and with all those changes
[2105.42 → 2109.24] happening and this is happening at light speed all the time, we're constantly getting
[2109.24 → 2110.36] bombarded with new things.
[2110.62 → 2114.42] And I know that I, as a practitioner, struggle to keep up at times with all the things.
[2114.54 → 2115.28] How do you do that?
[2115.36 → 2119.56] How do you keep the project going, keep it current, keep all these new things coming out?
[2119.88 → 2120.96] I'm assuming you don't sleep.
[2120.96 → 2122.52] Yeah, it's a great question.
[2122.52 → 2129.44] I do sleep and one thing that makes me sleep, yeah, is that I have to keep my natural neural
[2129.44 → 2130.30] network working.
[2130.46 → 2134.44] The way we do that is by having good sleep and a glass of wine on Fridays, you know, so...
[2134.44 → 2136.02] Glass of wine, a very important part of that too.
[2136.04 → 2136.66] Very, very important, yeah.
[2137.64 → 2138.00] Absolutely.
[2139.32 → 2140.80] So the answer is, how do we keep up?
[2141.10 → 2145.74] It's really having a strong community and nurturing it and being a player in it, encouraging
[2145.74 → 2146.94] more folks to participate.
[2147.84 → 2151.24] And looking back, I mean, I'm very grateful to the community and I think we were lucky to
[2151.24 → 2156.58] have been involved in helping catalyze that community because somehow, luckily, TVM was
[2156.58 → 2161.36] able to capture the interest of folks that build the frameworks, folks that build models
[2161.36 → 2163.14] because new classes of models.
[2163.28 → 2166.46] Say when there were recurrent neural networks, we had to go support that in TVM.
[2166.54 → 2170.32] Once you have dynamic models with dynamic shapes, all these things that you don't need to know
[2170.32 → 2174.50] what it is, but essentially different aspects of your model that makes them more powerful and more
[2174.50 → 2176.70] general needs to be supported in TVM.
[2176.78 → 2180.74] All of that were actually contributed by community members, and we help make that happen.
[2180.86 → 2182.56] We put a lot of work ourselves too.
[2183.02 → 2186.52] But then the hardware vendors, you know, so the hardware vendors are the ones that actually
[2186.66 → 2191.68] really feel the pain, to be honest, of this growing complexity of the ecosystem that you put
[2191.68 → 2197.20] very well, Chris, you know, so hardware vendors today, they have to write libraries, low level
[2197.20 → 2201.36] libraries that are tuned for their hardware targets for each one of the major operators
[2201.36 → 2202.02] in these models.
[2202.14 → 2204.16] Every time models change, they have to go and tune it again.
[2204.46 → 2206.54] So they're always like having to update the net.
[2206.66 → 2208.04] That's not sustainable, right?
[2208.04 → 2213.62] So that's why TVM automating a lot of that made it very attractive for them to contribute
[2213.62 → 2214.16] to TVM.
[2214.26 → 2219.26] And they want it to be open source because they also want to enjoy this amplification effect
[2219.26 → 2220.30] that the community has.
[2220.30 → 2227.54] So since we incubated Apache TVM into the Apache Software Foundation, there was even more interest
[2227.54 → 2232.62] and industry became more comfortable in contributing because now there is professional independent
[2232.62 → 2233.90] governance of the project.
[2233.90 → 2238.00] Because before it was, you know, a few grad students and a couple of folks in, you know,
[2238.04 → 2242.32] some contributors sitting in a room or, you know, sitting in a virtual room or folks at
[2242.32 → 2243.44] the University of Washington too.
[2243.98 → 2249.10] Anyway, so that was a long answer to your question, but basically it is by having an open source
[2249.10 → 2253.12] community and having the right incentive, technical incentives for folks to contribute to it.
[2253.22 → 2255.16] That's how we deal with the growing diversity.
[2255.56 → 2258.98] So I'm curious more about that open source side.
[2259.18 → 2264.76] So could you give, maybe there's people out there listening that are working on what they
[2264.76 → 2271.54] feel like might be the next really cool AI practitioner tooling or data science developer
[2271.54 → 2272.92] tool or something.
[2272.92 → 2275.42] They want to get this project out there.
[2275.86 → 2281.10] They want to have it be an open source project and get other people involved.
[2281.44 → 2286.00] Do you have any tips for those sorts of people out there that are working on tooling, working
[2286.00 → 2291.52] on new things in terms of helping them understand how they might foster a community around those
[2291.52 → 2293.98] things and maybe get a little bit of momentum going?
[2294.10 → 2296.20] What are some maybe the key points with that?
[2296.20 → 2297.32] That's a great question.
[2297.64 → 2302.20] I'll say first, recruit early users and truly listen to them and make them feel like they're
[2302.20 → 2303.66] part of your adventure here.
[2303.68 → 2306.70] And then you're helping them succeed, and their success is your success, right?
[2306.76 → 2311.80] So let's say like we got lucky, and we're fortunate that we had early users that were very involved
[2311.80 → 2312.70] in giving us feedback.
[2312.84 → 2315.80] And we, you know, by showing that you care about their feedback and implement it quickly,
[2315.80 → 2318.08] and then that catalyzes the process, right?
[2318.16 → 2321.88] So you kind of like have to treat them as customers paid with love, right?
[2321.94 → 2325.54] So they're giving you feedback, and you respond to that by making their lives easier,
[2325.54 → 2325.78] right?
[2325.88 → 2331.14] So that's the first thing, you know, really treat your community as well as possible and
[2331.14 → 2332.02] respond fast.
[2332.22 → 2337.22] And then second, you know, whenever picking the general theme, try hard and find what are
[2337.22 → 2341.78] all the other open source tools or maybe not open source tools that exist there that are
[2341.78 → 2343.32] very adjacent to what you do.
[2343.58 → 2348.82] And, you know, have a lot of clarity on what is your differentiation there, you know?
[2348.86 → 2350.40] So what kind of new problem are you solving?
[2350.48 → 2351.72] How do you communicate that?
[2351.72 → 2356.04] And if it's related to research project, it might be a little bit easier because you write
[2356.04 → 2359.10] a paper about it and, you know, people read the paper, and it's like, oh, you're solving
[2359.10 → 2359.58] a cool problem.
[2359.64 → 2361.80] They come and take a look at your work, right?
[2361.88 → 2368.20] So those are two things, you know, clear differentiation and then recruiting users as early as possible
[2368.20 → 2369.28] so you can iterate fast.
[2369.36 → 2372.04] And if you solve their problem, chances are they're going to tell their friends and colleagues
[2372.04 → 2373.10] and they start using it too.
[2373.16 → 2374.24] That's how you catalyze it.
[2374.24 → 2380.58] I'm kind of curious, kind of in the same strain of that last question, you're affecting so
[2380.58 → 2384.88] many other communities out there that, you know, may be commercially based with a hardware
[2384.88 → 2385.24] vendor.
[2385.72 → 2390.30] There are a lot of communities involved in the targets that you're compiling to.
[2390.98 → 2395.24] And I can't help but wonder, how do you see those types of communities getting involved?
[2395.30 → 2401.86] Because you are essentially a pretty significant influencer in how those targets get used.
[2401.86 → 2407.54] Because if the compiling is working, if it's really awesome, that benefits them in a big
[2407.54 → 2407.88] way.
[2408.24 → 2410.04] How do they choose to engage you?
[2410.34 → 2413.46] Do you need more engagement from those target communities to do better?
[2413.56 → 2415.12] And what kind of value can they add?
[2415.26 → 2419.46] I just, as you're hitting Raspberry Pi, I would imagine the Raspberry Pi community would
[2419.46 → 2422.04] have to be keenly interested in working with you on this.
[2422.38 → 2423.94] Yes, it's a great question, Chris.
[2424.08 → 2427.06] So ARM is already fully bought into the TVM ecosystem.
[2427.20 → 2430.88] They've built their CPU, GPU and NPU compilers on top of TVM.
[2430.88 → 2433.92] They're a very active contributor to the open source community.
[2434.18 → 2436.48] And they work closely with us at Octal as well.
[2436.94 → 2440.62] So some of the big players, of course, like, for example, let's say, NVIDIA, right?
[2440.66 → 2446.34] NVIDIA has a very mature, probably the most mature system software stack for machine learning
[2446.34 → 2446.84] on their hardware.
[2447.30 → 2449.16] And arguably, that's a good chunk of their success.
[2449.32 → 2450.98] And even NVIDIA is interested in working with TVM.
[2451.04 → 2452.32] You see some commits from them.
[2452.66 → 2454.32] You know, we support NVIDIA pretty well.
[2454.70 → 2456.28] And the point I wanted to make here is the following.
[2456.38 → 2459.36] For hardware that's really popular, the community is going to do anyway.
[2459.36 → 2461.84] Even if the hardware vendors themselves are not involved.
[2462.30 → 2466.24] So we have perfect support for NVIDIA because we did a bunch of work.
[2466.30 → 2468.52] The community did a bunch of work because NVIDIA hardware matters.
[2468.84 → 2472.38] In terms of how we have, we have very good performance on NVIDIA hardware because of that.
[2472.66 → 2476.56] And the point here is not to just say compete with QDNN and Tensor RT.
[2476.92 → 2478.06] Of course, they know they're hardware.
[2478.20 → 2478.68] They do well.
[2478.72 → 2480.66] In many cases, we do really well.
[2480.70 → 2482.40] Some other cases that was not in their radar.
[2482.40 → 2486.64] And we want to offer users a choice of which one to use.
[2486.74 → 2489.14] And sometimes even choose it automatically for them.
[2489.68 → 2492.16] So in TVM, there's something called best of both worlds.
[2492.26 → 2496.42] When you process a model through TVM, you can choose to either use QDNN or TVM native code.
[2496.46 → 2498.14] And it picks the best of each part of your model.
[2498.44 → 2500.12] And you compose this for the end user.
[2500.22 → 2501.84] What you care is your model runs fast, right?
[2502.12 → 2505.34] So the point here to make is that for this big hardware, the community supports it.
[2505.58 → 2509.92] For emerging hardware vendors, honestly, I don't know if they have an alternative.
[2509.92 → 2511.82] The alternative is to build everything in-house.
[2512.36 → 2512.80] So think of it.
[2512.84 → 2517.52] Let's say you are a new AI chip company, and you have a great idea for a hardware mechanism
[2517.52 → 2519.82] that's going to make a certain class of models run really well.
[2519.88 → 2520.54] And that's your business.
[2520.62 → 2522.04] Or you're going to cater to this set of users.
[2522.20 → 2523.40] So it's not really hard.
[2523.50 → 2527.10] Then you're going to look at the ecosystem, and you say, oh, now I have to support PyTorch,
[2527.20 → 2528.34] TensorFlow, Keras, and Magnet.
[2528.38 → 2529.48] I have to support this type of models.
[2529.56 → 2533.26] You start looking at everything they need support to connect with the rest of the ecosystem.
[2533.46 → 2534.80] It's a daunting task.
[2535.22 → 2538.64] So that's a huge incentive for them to come and use TVM.
[2538.64 → 2543.96] Because if they support a very clean code generation interface that we made very easy
[2543.96 → 2548.94] for new hardware vendors to come and be part of the ecosystem, I don't think they'll find
[2548.94 → 2551.04] a more compelling alternative, to be honest.
[2551.14 → 2555.88] Because how are you going to spin up a team of 15 compiler engineers to go and build your
[2555.88 → 2556.60] own internal compiler?
[2557.52 → 2559.30] It's just hard to imagine, right?
[2559.42 → 2565.18] So basically, what I'm trying to say in a long way is that the way we made it easy to
[2565.18 → 2567.74] add new hardware target and the fact there's a community around it and the fact there's
[2567.74 → 2571.10] a lot of momentum already, it sells itself to the new hardware vendors.
[2571.36 → 2576.44] And we see that by having hardware vendors come wanting to work with us to do some enablement
[2576.44 → 2577.26] work for them directly.
[2577.34 → 2579.04] We do some of that for some hardware targets.
[2579.62 → 2583.96] But a lot of times we just see hardware vendors going directly to the new, smaller,
[2584.08 → 2585.88] emerging ones going directly to the Apache TVM.
[2586.18 → 2587.48] So does that answer your question, Chris?
[2587.56 → 2587.68] Are you?
[2587.84 → 2588.42] No, it does.
[2588.48 → 2590.06] That was a perfect answer, actually.
[2590.38 → 2591.38] It satisfied it.
[2591.40 → 2591.74] Thank you.
[2591.74 → 2592.46] Yeah, definitely.
[2592.60 → 2593.20] I agree.
[2593.42 → 2598.10] I have sort of a strange question as we get more towards the end here.
[2598.52 → 2605.32] What else out there sort of across the AI industry do you have your eyes on in terms of things
[2605.32 → 2611.68] that really excite you in terms of where the industry is going or maybe particular groups
[2611.68 → 2615.38] that are innovating or particular technology that you have your eye on?
[2615.44 → 2620.04] What else do you have your eye on as you're looking kind of towards the future of the AI
[2620.04 → 2620.40] industry?
[2620.40 → 2623.02] Yeah, well, there's just so many things.
[2623.14 → 2624.88] Let me start with the shorter term, and then it goes longer term.
[2625.00 → 2629.30] So in the shorter term, I think it's really exciting what's going on in doing more and
[2629.30 → 2631.94] harder aware network architecture search.
[2632.08 → 2633.10] There are some companies doing it.
[2633.16 → 2637.38] But essentially, as we evolve how your model looks like with network architecture search,
[2637.38 → 2638.68] you do that in a harder way.
[2638.78 → 2642.20] I think it's super important because it's complementary to everything that we talked about here.
[2642.52 → 2642.76] Right.
[2642.84 → 2646.54] So what we're talking about here is having a model that is ready to be deployed.
[2646.62 → 2647.36] You just go and compile it.
[2647.36 → 2651.50] But now having the model in the first place to actually be better to do for your hardware
[2651.50 → 2651.80] is great.
[2651.88 → 2652.82] So that's one of them.
[2653.38 → 2656.64] The other one is more automations in the data management side.
[2656.74 → 2661.46] For example, I love what those Norco.ai folks are doing, which essentially, as if you've
[2661.46 → 2666.44] heard of them, but they essentially have tools that enable you to construct synthetic data
[2666.44 → 2671.46] sets in a programmatic way that essentially automates a lot of the work that's required
[2671.46 → 2674.18] for you to start building a data set to train models.
[2674.42 → 2677.46] And then on the hardware side, what I think is happening right now that's really exciting
[2677.46 → 2681.96] is just to see more and more reconfigurable architectures coming into the mix.
[2682.08 → 2682.20] Right.
[2682.26 → 2684.68] So I'm sure you've heard of CPUs, GPUs, right?
[2684.74 → 2686.32] And CPUs like accelerators.
[2686.72 → 2691.38] You've probably heard of FPGAs as well, which is essentially a hardware fabric that you can
[2691.38 → 2697.04] program very much the same way that you design hardware, but it's not quite as fast as a
[2697.04 → 2700.24] truly application-specific chip, but it's pretty general.
[2700.36 → 2702.50] And then you can do a lot of meaningful things with it.
[2702.84 → 2707.46] I find it exciting that those FPGAs are getting more and more tuned for machine learning.
[2707.86 → 2709.78] So Filing has offerings that way.
[2710.20 → 2714.82] You know, Alter is having, you know, enriching their FPGAs with more blocks that are more suitable
[2714.82 → 2715.58] for new models.
[2715.58 → 2717.66] I find this exciting in the short term.
[2717.66 → 2721.92] So now in the medium to long term, I just love what's going on in between machine learning
[2721.92 → 2723.22] and life sciences, you know?
[2723.34 → 2729.78] So just seeing machine learning enabling, you know, very large scale genomics studies that
[2729.78 → 2734.24] can just create the amount of data to go and make sense of data that is incredibly complex
[2734.24 → 2735.96] because nature is a complex beast, right?
[2736.06 → 2740.08] So, and then also using machine learning to design systems, you know?
[2740.18 → 2742.74] So people are using machine learning to design molecular systems.
[2742.84 → 2745.32] People are using machine learning to design aircraft.
[2745.32 → 2748.12] People are using a reverse engineer, like what was it again?
[2748.20 → 2751.20] Reverse design where you give the properties, and you synthesize something that has those
[2751.20 → 2752.32] properties using machine learning.
[2752.76 → 2757.86] These are all things that I find really, really exciting to think about because machine learning
[2757.86 → 2758.94] itself is also a system.
[2759.16 → 2763.26] So using machine learning for machine learning improvements is pretty interesting.
[2763.34 → 2766.52] We do that to some extent, but I feel like we're just scratching the surface, right?
[2766.58 → 2770.56] So you can use machine learning to design machine learning chips, right?
[2770.60 → 2773.00] You can use machine learning to optimize machine learning training systems.
[2773.00 → 2779.60] And when you close the loop there, that's when you should embrace and let it evolve, right?
[2779.76 → 2784.16] So I remember a while back, we had some guests from Intel, and they were talking about just
[2784.16 → 2786.98] what you just said, using machine learning for chip design.
[2787.10 → 2790.44] And yeah, the sky's the limit that you can use it for so many different things at this
[2790.44 → 2790.66] point.
[2791.12 → 2791.64] Yeah, absolutely.
[2791.80 → 2796.00] And machine learning itself, going back full circle now, you know, as a workload, it's so
[2796.00 → 2799.24] tolerant to what we call noisy execution, right?
[2799.24 → 2802.84] So by that, I really mean if you have flaky hardware and then there's just no way around
[2802.84 → 2806.60] it, as you go to two nanometre technologies, you know, which I don't know if you heard
[2806.60 → 2811.14] IBM just announced they're getting, you know, two nanometre process, kind of make a lot of
[2811.14 → 2811.72] progress with it.
[2811.78 → 2813.46] That's kind of crazy to think about, right?
[2813.60 → 2816.64] And it's likely to be very, very noisy and have very flaky transistors.
[2816.90 → 2821.22] And the way we make use of that is not just by doing the typical systems design of layering,
[2821.62 → 2823.50] error correcting, no, we should do that too.
[2823.50 → 2827.86] But with machine learning, you can use that directly because it's so tolerant to noisy
[2827.86 → 2831.34] execution that there are many interesting possibilities there.
[2831.52 → 2835.44] So for better energy efficiency and such that machine learning wouldn't get as much bad rep
[2835.44 → 2837.58] by using a lot of energy, right?
[2837.82 → 2839.70] I'm sure you've heard that before, right?
[2839.94 → 2844.66] Well, that's a whole topic of a whole other conversation, you know, so.
[2844.98 → 2847.14] Yeah, and I hope we can have that conversation sometime.
[2847.14 → 2855.16] Well, Luis, I appreciate you taking time to help Chris and I fully optimize our discussion
[2855.16 → 2858.64] on the podcast to maximize interest.
[2858.84 → 2860.28] It's been great.
[2860.50 → 2861.44] I've really enjoyed it.
[2861.80 → 2866.78] And we'll have links to TVM and Octal and all the things in our show notes.
[2866.78 → 2870.34] So definitely encourage our listeners to check those things out.
[2870.76 → 2873.46] I know I'll be playing around a bit after the episode.
[2873.78 → 2874.98] So thanks much, Luis.
[2875.08 → 2876.40] Really appreciate you taking time.
[2876.40 → 2877.40] Thank you, Luis.
[2877.42 → 2878.42] You guys are really, really fun.
[2878.50 → 2881.24] I can't wait to hear your other episodes for other topics as well.
[2881.36 → 2882.78] So you and Chris are really fun.
[2882.84 → 2883.26] Thank you.
[2886.74 → 2888.74] Thank you for listening to Practical AI.
[2889.08 → 2891.08] We appreciate your time and your attention.
[2891.56 → 2895.16] If you enjoyed this episode, help us out by spreading the word.
[2895.72 → 2896.48] Think of a friend.
[2896.68 → 2897.36] Think of a colleague.
[2897.66 → 2900.46] Somebody who would benefit from listening to it and send them a link.
[2900.80 → 2901.82] We'd really appreciate it.
[2902.16 → 2905.52] Practical AI is hosted by Chris Benson and Daniel Whiten ack.
[2905.52 → 2909.30] It's produced by Jared Santo with music by Break master Cylinder.
[2909.68 → 2912.88] Thanks again to our sponsors, Vastly, Linde, and Launch Darkly.
[2913.20 → 2913.84] That's our show.
[2914.28 → 2915.24] We hope you enjoyed it.
[2915.32 → 2916.98] And we'll talk to you again next week.
[2917.58 → 2923.98] We'll be right back.
[2924.08 → 2936.82] We'll be right back.
[2941.26 → 2943.02] We'll be right back.
[2944.30 → 2944.98] We'll be right back.
[2944.98 → 2946.20] Game on.
