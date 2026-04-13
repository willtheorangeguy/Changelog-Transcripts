[0.00 → 4.08] So now we have this new NVIDIA DGX A100.
[4.42 → 5.34] Maybe you'll get one.
[5.42 → 6.60] I don't know if I'm going to get one.
[7.80 → 8.82] But we'll see.
[8.92 → 9.24] We'll see.
[9.42 → 10.08] Yeah, yeah.
[10.36 → 14.18] Sadly, I'm not in charge of procurement, and I am certainly not in charge of procuring
[14.18 → 16.20] one for my own personal use.
[16.40 → 17.06] We'll see.
[17.22 → 19.54] I'm guessing that my nonprofit's not going to get one.
[19.66 → 25.78] But if you happen to be getting your DGX A100, and you'd like me to run my training on it,
[25.78 → 28.62] I would be more than happy to do some benchmarking for you.
[30.00 → 34.32] Bandwidth for Changelog is provided by Vastly.
[34.68 → 36.58] Learn more at Fastly.com.
[36.82 → 39.90] We move fast and fix things here at Changelog because of Rollbar.
[40.02 → 41.70] Check them out at Rollbar.com.
[41.96 → 44.14] And we're hosted on Linde Cloud Servers.
[44.48 → 46.48] Head to Linode.com slash Changelog.
[49.18 → 52.18] Linde makes cloud computing simple, affordable, and accessible.
[52.38 → 56.18] Whether you're working on a personal project or managing your enterprise's infrastructure,
[56.18 → 60.70] Linde has the pricing, support, and skill you need to take your ideas to the next level,
[60.98 → 63.82] we trust Linde because they keep it fast, and they keep it simple.
[64.12 → 66.60] Check them out at Linode.com slash Changelog.
[66.60 → 79.56] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[79.90 → 81.64] productive, and accessible to everyone.
[81.94 → 86.04] This is where conversations around AI, machine learning, and data science happen.
[86.40 → 90.52] Join the community and Slack with us around various topics of the show at Changelog.com
[90.52 → 92.42] slash community and follow us on Twitter.
[92.56 → 94.20] We're at Practical AI FM.
[94.46 → 95.94] Okay, take it away, guys.
[95.94 → 104.74] Welcome to another Fully Connected episode where Daniel and I keep you fully connected
[104.74 → 107.00] with everything that's happening in the AI community.
[107.24 → 111.56] We'll take some time to discuss the latest AI news, and we'll dig into learning resources
[111.56 → 114.10] to help you level up your machine learning game.
[114.22 → 116.12] So welcome to the Practical AI podcast.
[116.76 → 117.76] My name is Chris Benson.
[118.00 → 120.16] I'm Principal AI Strategist at Lockheed Martin.
[120.40 → 124.86] And with me as always is Daniel Whiten ack, data scientist at SIL International.
[125.02 → 125.62] How's it going, Daniel?
[125.94 → 127.14] It's going great.
[127.24 → 128.76] It's a beautiful day outside.
[128.94 → 131.64] Hopefully I can take a walk after this.
[131.80 → 136.90] And I've been staring at my screen most of the day since like 7 a.m.
[136.90 → 139.54] So I'm ready for a walk around the block or something.
[140.08 → 141.38] That sounds like a good idea.
[141.52 → 144.00] I am bleary-eyed from screen time as well.
[144.16 → 146.40] So get outside and enjoy it.
[146.40 → 150.98] Especially now that at least where I'm at in Atlanta, the worst of the pollen seems to be
[150.98 → 151.36] passed.
[152.06 → 153.08] So that's good.
[153.22 → 156.16] No more yellow cars from pine pollen everywhere.
[156.88 → 157.76] Yeah, that's rough.
[157.94 → 163.92] We need like an AI model that like takes in pictures of cars in people's driveways and
[163.92 → 168.50] like tells you whether it's safe to go outside yet because of the pollen levels.
[168.76 → 169.26] There you go.
[169.26 → 171.18] I'm sure there are easier ways to do that.
[171.40 → 172.40] But that's right.
[172.50 → 174.12] So we'll have to prep people next year.
[174.26 → 179.46] So we'll just ask everybody in the audience next year to send us your images of your cars
[179.46 → 181.14] covered in pine pollen with a date.
[181.24 → 181.50] Yeah.
[181.64 → 182.88] A date time attached to it.
[182.92 → 185.12] And we will have a great project to go on this.
[185.32 → 186.08] Yeah, exactly.
[186.60 → 190.32] So and before we get going, I know that you've been doing some training classes.
[190.50 → 191.32] How have those been going?
[191.48 → 193.08] They went really well.
[193.08 → 196.80] It was interesting because normally, by the way, not, not taking.
[197.22 → 197.40] Yeah.
[197.58 → 202.88] So normally when I do like AI trainings in industry or like at conferences or something,
[203.00 → 206.56] obviously there's, you know, normally like a whiteboard there.
[206.68 → 212.86] There's a lot of kind of changes as the class goes on because there's a lot of easy kinds of
[212.86 → 213.56] back and forth.
[213.72 → 218.94] So it was interesting to figure out the virtual dynamic with everybody being at home.
[218.94 → 226.34] I think actually it ended up having some benefits because it sort of forced me like normally
[226.34 → 228.28] I kind of write things at the whiteboard.
[228.38 → 230.24] I'm able to like to make changes as I go.
[230.36 → 238.84] But to be able to or to have to sit down and work things out in a strict set of slides that
[238.84 → 245.02] I'm showing made me really think about like what is the proper flow to explain this idea
[245.02 → 247.20] and like show certain things.
[247.20 → 251.30] So in that respect, actually, it was a learning experience for me.
[251.30 → 256.52] I'll bet because it helped clarify some of that logic and even in my own mind.
[256.52 → 257.92] So but it went really well.
[257.98 → 264.56] And the students had some great questions and went, you know, all the way from what is
[264.56 → 269.22] AI to convolutional layers and recurrent layers and training cool things.
[269.36 → 271.14] And so, yeah, it was a good time.
[271.70 → 276.10] You know, I've always found that no matter what the topic you teach, it forces you to assess
[276.10 → 279.26] everything that you think about because you got to explain it to other people and answer
[279.26 → 279.74] all that.
[279.88 → 283.94] And you all every time I've done that, I've learned so much more about whatever it was
[283.94 → 284.68] I was going to teach.
[284.92 → 285.60] So for sure.
[285.70 → 285.90] Yeah.
[285.90 → 291.90] And people ask questions that just have never come into your mind, not because they're bad
[291.90 → 292.30] questions.
[292.30 → 293.70] It's just a different point of view.
[293.70 → 298.54] So it forces you to like backtrack yourself and kind of look at things from different directions.
[298.54 → 299.62] Yeah.
[299.76 → 301.28] Well, that sounds interesting.
[301.60 → 306.10] I guess you probably looked out, you got through your training classes right before
[306.10 → 313.66] NVIDIA this year at their GPU technology conference, GTC, made all their new hardware
[313.66 → 314.32] announcements.
[314.76 → 315.48] That's true.
[315.48 → 316.16] And the things that go with that.
[316.54 → 317.84] And you know, it's interesting.
[318.76 → 323.36] I actually was spending the evening yesterday with my brothers-in-law who are living with
[323.36 → 323.56] us.
[323.56 → 327.90] So we aren't like social gathering yet, but my brothers-in-law are living with us right
[327.90 → 330.02] now while they're back from college.
[330.58 → 335.08] And so they don't work in, they're not like in computer science or anything like that,
[335.08 → 336.62] but they are pretty heavy gamers.
[337.38 → 342.64] And they were both like, we started talking about some of this stuff, and they had even
[342.64 → 347.50] seen the keynote from the NVIDIA conference even before I started talking about, even though
[347.50 → 353.54] it was mostly AI related, it was like a, you know, already a sort of general meme.
[353.56 → 360.34] That like the NVIDIA CEO was like presenting all of this cool GPU stuff from his kitchen,
[360.48 → 365.34] which was like, you know, you could see the spatulas in the background and some very interesting
[365.34 → 369.18] like fresco above his oven and such.
[369.76 → 375.52] So it was fascinating in that sense that there was like, like people, even people
[375.52 → 381.12] that aren't in this space, like it made some impact on their life, which was fascinating.
[381.12 → 384.10] You know, that's a great point.
[384.18 → 385.18] It's worth talking about.
[385.32 → 391.52] I mean, you know, we talk about NVIDIA and Google and other major players in this space
[391.52 → 397.52] often because you can't really talk about AI in a lot of cases without talking about the
[397.52 → 398.32] the biggest influencers.
[398.66 → 404.94] And in NVIDIA's case, they were this gaming company and GPUs were originally to promote
[404.94 → 408.92] graphics and, you know, computer gamers, you know, were constantly using it.
[408.92 → 411.40] And now we're doing this in the AI space, you know.
[411.50 → 416.32] So any thoughts on how or insight into how that evolution came about and why we're using
[416.32 → 417.58] GPUs for all this stuff?
[418.34 → 418.46] Yeah.
[418.54 → 424.20] And actually also demand from the Bitcoin mining space as well.
[424.36 → 428.68] So it's very interesting that like if you look at NVIDIA's rise over time, of course,
[428.74 → 431.92] they existed for quite some time.
[431.92 → 436.92] But it's almost like so they existed for a reason, and they were perfect at this reason.
[437.14 → 441.42] And then all of a sudden, like the things that they were good at became like the most
[441.42 → 442.88] important things in the world.
[443.20 → 444.66] That's how it kind of how it seems.
[444.78 → 447.08] And then they just like they were already there.
[447.24 → 449.28] So it's like they just exploded.
[449.84 → 451.08] So, yeah, you're right.
[451.08 → 454.68] So if you think about like video gaming and that sort of thing or like things you would
[454.68 → 460.72] want to do in video processing or graphics, for example, like you might want to apply
[460.72 → 465.50] a filter to some image or frame of a video, right?
[465.52 → 472.22] Like to darken it or to apply a gradient of colour or, you know, something like this.
[472.22 → 477.58] And so you're essentially applying some operation to the pixels of an image, which are set up
[477.58 → 482.76] in a matrix and have like even some depth because there is a colour dimension.
[482.96 → 483.52] Right.
[483.54 → 489.68] So you have like this matrix of numbers, and then you apply some operation on the elements
[489.68 → 496.74] of this matrix or really this volume, this input volume in AI, of course, with convolutional
[496.74 → 501.88] layers like you are doing almost that exact same thing because you're applying like
[501.88 → 509.58] a series of weights and bias and, you know, functions like activation functions to individual
[509.58 → 511.92] elements of a matrix or an input volume.
[512.54 → 517.00] But even in like recurrent layers or like fully connected neural networks and that sort
[517.00 → 522.10] of thing, the types of networks that might be relevant to other things like text or just
[522.10 → 529.84] like general classification problem, even those take some input vector or matrix and just
[529.84 → 536.06] apply a series of weights to those apply functions like activation functions like tangent and sigmoid
[536.06 → 539.82] and all of these in an element wise way.
[540.32 → 547.34] And so you're really doing the sort of matrix operations that graphics cards were always good
[547.34 → 547.64] at.
[547.84 → 553.74] And so it turns out that it's perfect to use those sorts of graphics cards for those
[553.74 → 558.36] sorts of operations, which are done in specifically in AI training.
[558.36 → 560.82] Of course, we're going to talk maybe about inference today, too.
[560.90 → 566.00] But I think it came about because these are the sorts of things that happen iteratively
[566.00 → 570.96] thousands and thousands and millions of times when you do training for an AI model.
[571.96 → 577.42] You know, that has to be the most accessible explanation to that evolution that I think I've
[577.42 → 578.28] heard anyone say.
[578.50 → 581.92] I think you did it better than NVIDIA actually says it.
[582.34 → 583.24] So that was well done.
[583.24 → 584.66] They can pay me if they like.
[585.06 → 590.24] I mean, or they could send me a graphics card if it's that would probably actually be better.
[590.54 → 590.78] I would.
[592.32 → 596.24] NVIDIA, if you're listening, hint, hint, hint, you know, Titan RTX.
[597.02 → 598.76] I won't even take the newest one.
[599.04 → 600.56] Don't even give me like a 100.
[600.94 → 601.96] Give them the newest one.
[603.24 → 605.02] I don't just small potatoes.
[605.38 → 605.56] Yeah.
[605.56 → 607.82] That $5,000 or what?
[607.92 → 609.54] I don't even know how much it is.
[609.86 → 610.76] Titan RTX.
[611.54 → 617.76] Well, now that we have been pleading for free stuff, let's move on to some of the things
[617.76 → 623.38] that they announced, which many organizations around the world are going to be trying to
[623.38 → 629.02] evaluate and figure out how they're going to incorporate, buy into and basically utilize
[629.02 → 632.64] this new hardware and the supporting software capabilities that go with it.
[632.92 → 633.52] Yeah, definitely.
[633.52 → 639.78] So, you know, I guess one of the things to talk about here is even before we get to
[639.78 → 645.44] announcements are the types of GPUs that are currently available and what forms, you know,
[645.50 → 650.02] what kind of off brand GPUs are out there because NVIDIA isn't the only player in the
[650.02 → 650.44] space.
[650.56 → 651.78] Any insight into that?
[652.40 → 656.76] Yeah, I mean, it's probably worth distinguishing a few things here.
[656.82 → 661.32] I guess first is like accelerators that are out there and types of GPUs that are out there
[661.32 → 668.14] and also like access patterns to those, whether that be like locally or in the cloud or whatever,
[668.74 → 670.40] at least from my perspective.
[670.40 → 675.16] And I'm by no means an expert on this on the graphics card front.
[675.24 → 678.70] Actually, probably my brother-in-law could do a better job.
[678.70 → 685.22] But there has been a progression and most of the time you'll see like graphics cards referred to by some
[685.22 → 687.70] series of numbers and acronyms.
[687.94 → 694.26] So like recent ones have been like something like 1080 RTX or Titan RTX or something.
[694.66 → 700.10] So those are the graphics processing unit that you would like buy.
[700.10 → 704.50] And then you have to plug it into like some computer, right?
[704.58 → 709.72] So some people say like, okay, I'm going to develop AI models.
[709.72 → 715.30] And so I'm going to buy like a computer, like a tower, a desktop computer.
[715.52 → 722.60] And then I'm going to buy a graphics GPU, like one of these RTX GPUs or something.
[722.60 → 726.00] And I'm going to put it in like my PCI slot and my motherboard.
[726.68 → 730.62] And then when I do AI training, then I'm going to like offload the training,
[730.96 → 737.88] some of those training operations to the graphics card or GPU that's input to my computer.
[737.88 → 743.84] So that's sort of a one of the first ways you might think about doing this is like,
[743.90 → 748.36] I'm going to do AI development so I can buy a computer, and then I'm going to buy a graphics card
[748.36 → 749.62] and just put it in there.
[749.70 → 752.32] And a lot of those, of course, come from NVIDIA.
[752.32 → 760.98] They make a lot of those cards, but there's off-brand ones that kind of are similar to
[760.98 → 763.80] the models that NVIDIA has.
[763.80 → 769.18] And then there's also like other brands that have their own style of graphics card and that
[769.18 → 769.68] sort of thing.
[770.02 → 775.12] Have you ever built or thought about building this sort of like workstation for your home
[775.12 → 777.44] to like to sit by your desk or something?
[777.98 → 779.90] I think I'm way too lazy to do that.
[779.90 → 785.66] At this point, I'd much rather go to a cloud provider if I'm at home and use what they've
[785.66 → 785.90] built.
[786.40 → 791.28] I've noticed that most of the people that had workstations specifically for their AI workflows
[791.28 → 795.92] seem to have moved off those in recent years, either in the cloud or if they're big enough
[795.92 → 800.50] into more of a data centre or at least a, you know, like a workstation level, you know,
[800.60 → 803.64] where they're buying a workstation versus buying individual GPUs.
[803.64 → 807.94] It was one of the things I was thinking as you were just talking about that was we had
[807.94 → 814.04] one of our early episodes, which was episode 15 called Artificial Intelligence at NVIDIA.
[814.14 → 820.00] We had NVIDIA's chief scientist, Bill Dally on the show and he absolutely schooled us.
[820.00 → 820.88] Yeah, definitely.
[821.08 → 823.08] In the hardware, do you remember that?
[823.22 → 824.84] He really schooled us in the hardware.
[824.98 → 827.02] Much deeper than we'll go on this episode.
[827.20 → 828.46] So we definitely take a look at that.
[828.58 → 828.66] Yeah.
[828.66 → 829.14] Yes.
[830.32 → 834.78] If you're wanting, and we asked him to against other architectures, you know, and he went
[834.78 → 836.34] there and described it.
[836.44 → 841.12] So if that aspect of it, not just the NVIDIA architectures, but how they compare to other
[841.12 → 845.70] things, I would encourage listeners to listen to that episode, and he will absolutely school
[845.70 → 847.22] you in the fundamentals there.
[847.50 → 848.22] Yeah, for sure.
[848.22 → 853.54] Because there's not only so like I described like the graphics card or GPU, which is what
[853.54 → 861.10] a lot of times what people think of when they think of GPU or accelerator in the AI world,
[861.18 → 863.90] they think of one of these GPUs or a series of them.
[864.18 → 865.72] But there are other options too.
[865.88 → 871.40] So there's like the TPU or tensor processing unit from, is it tensor processing unit or tensor
[871.40 → 872.08] flow process?
[872.14 → 873.40] I don't know if they put the brand in there.
[873.46 → 874.96] I think it's tensor processing unit.
[875.24 → 876.10] I believe it is.
[876.10 → 882.08] The TPU from the Google developed, which is another type of accelerator.
[882.24 → 887.12] But there's even other architectures out there other than CPU, GPU, TPU.
[887.36 → 889.76] There's FPGA and other things.
[889.92 → 892.76] And yeah, there are a lot of options out there.
[892.80 → 894.92] And like you said, there are options also.
[895.22 → 900.60] So I kind of described like, OK, if you're developing AI, you could just like create just
[900.60 → 902.50] buy one of these computers to have at your desk.
[902.50 → 909.66] But there's also just like how other forms of compute have been commoditized via the cloud.
[909.84 → 914.18] There's easy access to cloud resources for GPUs too.
[914.36 → 922.26] And in all the clouds and in even special built GPU, like cloud services, like paper space
[922.26 → 922.86] and others.
[923.00 → 928.10] I know when I was looking around a while back for a project, I don't know if it's still
[928.10 → 933.00] the case, but I was trying to find like, what is the cheapest way to use a GPU in the cloud?
[933.56 → 936.30] And I ended up going with paper space.
[936.38 → 937.84] I don't know if it's the cheapest anymore.
[938.28 → 942.12] I do use like Google Cola, as I've mentioned a lot of times on the podcast.
[942.38 → 945.38] And of course, you can have access to a free GPU there.
[945.46 → 948.02] There are tradeoffs because it's in a notebook and that sort of thing.
[948.12 → 953.62] But anyway, there are a lot of ways to access them, which aren't buying a computer and setting
[953.62 → 954.44] it is on your desk.
[954.66 → 955.30] That's true.
[955.78 → 956.78] That's definitely nice.
[956.78 → 962.98] So why don't we dive into some of the announcements that NVIDIA made at GTC?
[963.14 → 967.74] As we're recording this, I think it was about roughly a week ago that they made the announcement
[967.74 → 970.38] and it'll be another week as it rolls out.
[970.70 → 977.14] But I'll start us off with, they started in, I'm going to probably butcher the pronunciation,
[977.50 → 979.46] the NVIDIA Ampere architecture.
[979.92 → 981.00] Did I get that right?
[981.04 → 982.80] I've read it, but I haven't watched the video to see.
[982.86 → 983.18] Ampere?
[983.30 → 983.78] There you go.
[984.16 → 985.22] How he's pronouncing it.
[985.22 → 989.06] I think in reference to like Amp in electronics, I think.
[989.20 → 989.86] There you go.
[990.00 → 991.10] I didn't get the connection there.
[991.26 → 991.46] Okay.
[991.98 → 993.14] So I don't know.
[993.26 → 994.68] At least that's how I was saying it.
[994.68 → 1002.04] So yeah, I know that essentially this is what they've used to replace kind of the existing
[1002.04 → 1003.32] architecture and expand it.
[1003.38 → 1009.52] They're really focusing on, I think, a more realistic in the sense of kind of, I say cloud,
[1009.68 → 1013.00] but when I say cloud, I don't necessarily strictly mean cloud providers.
[1013.00 → 1018.68] I mean, if you're putting together a data centre with a bunch of GPUs or GPU servers in it,
[1018.88 → 1024.30] you know, they're really focusing on not only the performance sides, but the usability as I was reading through it.
[1024.84 → 1024.94] Yeah.
[1025.06 → 1030.10] And I think that what I was gathering also in talking with some other people about this is,
[1030.10 → 1037.04] so the generation before this latest one was focused more on the ray tracing elements,
[1037.14 → 1042.98] which is the RTX in a lot of these cards, which to be honest, I'm not a big expert on ray tracing.
[1043.34 → 1043.78] Nor am I.
[1044.26 → 1048.04] That has implications, of course, in graphics and that sort of thing.
[1048.04 → 1054.78] But it wasn't like a huge advance in terms of like the size and capabilities of the graphics processing unit itself.
[1054.88 → 1059.48] It was more of this kind of generation of additional ray tracing capabilities.
[1059.66 → 1066.92] Whereas this next architecture, which they're releasing, which they're calling the A100 or the Ampere architecture,
[1066.92 → 1071.30] which includes this A100 card or GPU,
[1071.30 → 1080.50] that this is a fairly significant jump in the like size and capabilities of the graphics processing unit itself.
[1080.66 → 1088.68] I think part of that has to do with, I guess, the way that they've laid out the transistors and all of that on the substrate,
[1088.98 → 1091.36] that it's much denser in my understanding.
[1091.94 → 1092.08] Yeah.
[1092.44 → 1097.40] Am I recalling it was something like 20 times performance improvement over the V100?
[1097.40 → 1098.76] Well, yeah.
[1098.88 → 1108.50] So it's 20 times greater flops, which is like a measure of actually you probably are better versed in the acronyms.
[1108.64 → 1115.80] But this is like a common way to like measure the performance of like computers, like supercomputers and that sort of thing.
[1116.24 → 1125.14] So 20x greater flops for AI, although they do give some benchmarks, which is pretty nice just for reference.
[1125.14 → 1131.30] And what I was looking at, they give some benchmarks for training BERT large scale language models,
[1131.48 → 1135.94] which we have an episode on BERT as well, if you'd like to learn more about that.
[1136.70 → 1137.14] Yes, we do.
[1137.24 → 1138.56] We've mentioned in several, actually.
[1138.98 → 1141.58] Yeah, it's good that we ended up having that conversation.
[1142.18 → 1152.34] But the BERT models are these very large language related models, NLP models that have just tons of parameters.
[1152.34 → 1156.96] And actually, these large language models have even billions of parameters now.
[1157.10 → 1158.16] I forget how many BERT has.
[1159.10 → 1165.36] But they give some benchmarks both for the training and inference on speed-ups on training BERT.
[1165.36 → 1166.12] Mm-hmm.
[1166.42 → 1171.80] So on BERT itself, they're saying that above the V100.
[1172.14 → 1177.96] So the V100, if you go to like Google Cloud or if you go to Paper space or one of these platforms,
[1178.62 → 1184.16] at least right now, I think the best GPU that you can get access to is called a V100,
[1184.78 → 1186.02] which is a previous generation.
[1186.28 → 1187.90] And it's pretty wicked fast.
[1187.90 → 1197.78] I mean, I've used this in a couple of projects, and it's quite astoundingly faster than the sort of entry-level GPU.
[1198.48 → 1198.74] Yes.
[1199.52 → 1203.38] And it's the basis for the DGX line of servers as well.
[1203.38 → 1203.90] Yeah, I think so.
[1203.96 → 1205.80] Or was prior to this release.
[1205.90 → 1206.70] Prior to this, yeah.
[1206.70 → 1217.38] And they're saying that there's a speed-up between three and six times in the training for the BERT large-scale training.
[1217.38 → 1224.98] And the difference between the three to six X has to do with the precision of the floating point numbers that you're using in the model.
[1224.98 → 1234.04] So I'm stepping way beyond my bounds into like computer science land where I don't deserve to step.
[1234.04 → 1241.88] But in the models, obviously, you have all these weights and parameters and the matrices that you're transforming in these models.
[1242.18 → 1248.74] And computers work with numbers, and those numbers have to be represented in some form, in some precision.
[1248.96 → 1256.50] You can't, like if you're representing pi, you're not going to represent like all digits of pi in pi.
[1256.60 → 1258.92] You're going to have to cut it off somewhere, right?
[1259.24 → 1259.48] Yeah.
[1260.18 → 1262.42] This is having to do with that precision of the numbers.
[1262.42 → 1270.30] And you can actually, if you reduce the precision of how you represent numbers, you can sometimes speed up your performance.
[1270.74 → 1276.18] And so that's what they're talking about there with that difference to three to X, three X to six X.
[1276.18 → 1276.86] Three to six X, yeah.
[1277.20 → 1282.88] And I think I'm looking at their inference, and I know they're saying it's a seven times speed up on inference.
[1283.34 → 1285.34] So it's substantial in that case.
[1285.34 → 1293.10] So they say like this card, this A100 accelerator, they bring up this idea of, what do they call it?
[1293.16 → 1295.38] I don't know if you say it, MIG.
[1295.50 → 1301.90] I'm thinking of like the fighter jet, but the multi-instance GPU, which is a really intriguing idea.
[1302.32 → 1303.88] Do you work for us now in that way?
[1304.28 → 1304.62] Yeah.
[1304.62 → 1312.84] They're saying it's multi-instance GPU, which in my understanding, are they saying like you can basically treat the GPU as seven GPUs?
[1312.90 → 1313.58] Is that what they're saying?
[1313.58 → 1316.78] So I was wondering that myself.
[1317.06 → 1327.84] And so a big topic that I spend my time at work is around multi-tenancy in your workflows and the accessibility of compute in those.
[1327.84 → 1335.78] And I was taking it in that way, but I'm not sure because they're a little bit ambiguous in the way they use some of the terms.
[1336.76 → 1341.70] Another one that I noticed is they talked about the need for no code changes.
[1341.70 → 1349.66] And I'm assuming that's CUBA code changes in this case, but they weren't always as specific as they might have been in terms of their explanations here.
[1349.74 → 1351.24] I was wondering about that as well.
[1351.34 → 1357.38] Of course, there certainly are ways to make changes like this transparent, but there's a change somewhere, right?
[1357.38 → 1364.30] It's just maybe at the abstraction level you're working with in TensorFlow or something, you don't have to make a change in TensorFlow.
[1364.62 → 1369.48] But in the underlying libraries somewhere, it seems like there's some type of change.
[1369.48 → 1373.64] Yeah, it talks on the multi-instance GPU as I'm looking through that.
[1373.76 → 1379.44] It's talking about seven different isolated GPU instances running different applications simultaneously.
[1379.86 → 1379.98] Yeah.
[1380.32 → 1392.94] So it seems like when they say 7x speed up for BERT large inference, and they have under there in parentheses 7MIG or 7 multi-instance GPU.
[1393.26 → 1394.16] They're using them all?
[1394.16 → 1410.24] What I'm assuming that is meaning is they basically are running seven inferences in parallel on the 7 GPU, which seems to be the same performance that they're indicating for as the V100.
[1410.24 → 1426.10] So for inference-wise, it seems like the change is that you're able to run things in this parallel way, whereas on a V100 or something, maybe you couldn't do that.
[1426.22 → 1428.02] And so there wasn't that speed up.
[1428.52 → 1429.94] I'm making some assumptions here.
[1430.26 → 1430.90] That's true.
[1431.34 → 1434.52] I know for a fact that there are folks in NVIDIA that listen to the podcast.
[1434.52 → 1437.04] So hopefully if we're getting this wrong, they can't-
[1437.04 → 1437.88] Yeah, clear us up.
[1438.04 → 1438.24] Yeah.
[1438.38 → 1443.46] They can clarify for us, and we'll come back at a later time on a later episode and say, we were wrong.
[1443.56 → 1444.38] We're happy to do that.
[1444.48 → 1446.02] So we're making the best of it.
[1446.26 → 1447.22] We were wrong.
[1447.36 → 1453.36] And if you send us a GPU, then we'll prove that we were wrong on our own local system.
[1453.82 → 1454.64] You're back to begging.
[1455.08 → 1456.00] Oh, oh.
[1456.48 → 1457.42] It seems pretty cool.
[1457.42 → 1477.72] I mean, I like the idea that if you've gone from a stage of training to inference, basically, whereas before maybe you had this full, like, powerful GPU that you were basically running inference on, but not, like, soaking up all the goodness of the GPU and to compute.
[1477.72 → 1488.36] Here, they're basically saying, okay, well, you can sort of parallelize the inference over that and still utilize this whole computes capability.
[1488.70 → 1493.08] But now you just have this ability to split it up in nice ways.
[1493.64 → 1495.46] So I definitely think that's pretty cool.
[1496.08 → 1496.92] And, yeah.
[1497.30 → 1500.26] It's interesting with the parallelization of this.
[1500.26 → 1507.80] There was an image that I saw NVIDIA had put out where they were kind of comparing the old architecture with the new A100 architecture.
[1508.44 → 1512.44] And they basically had, you know, one little server for the new that was the equivalent.
[1512.58 → 1516.90] They were showing, you know, rows of racks of servers in terms of its productivity.
[1517.22 → 1518.62] But it was definitely an impact.
[1518.76 → 1521.62] It was something that me and some folks I work with were passing around.
[1521.84 → 1523.26] And so, yeah.
[1523.48 → 1527.64] Got to keep up with times, I guess, if you're going to keep driving forward on compute.
[1527.64 → 1535.04] Anything else on the architecture at large before we talk about DGXs or dive into the processors themselves?
[1535.30 → 1539.28] I think the one thing that you mentioned , like, the speed-up without code change.
[1539.38 → 1547.64] I think they do introduce this new idea where, as people before had talked about floating point 16 and 32 numbers.
[1548.42 → 1548.60] Yeah.
[1548.76 → 1554.12] Where, again, these are having to do with the sort of precision with which you're representing numbers.
[1554.12 → 1558.50] They introduced this new idea of, like, tensor float 32.
[1558.82 → 1559.84] I saw that.
[1560.04 → 1566.42] Which apparently, with float 32, obviously, if you have more digits, you can represent more numbers.
[1566.90 → 1567.04] Right?
[1567.58 → 1569.54] There's, like, this kind of range.
[1570.04 → 1574.68] But, you know, it's not as fast as using floating point 16 in some cases.
[1574.82 → 1577.74] So what they're saying is they're trying to balance the two, I think,
[1577.74 → 1583.10] in that they have a wider range of numbers they can represent in this representation,
[1583.10 → 1588.66] but with lower precision such that they can, you know, speed up training.
[1589.02 → 1593.56] So, you know, again, hopefully I've represented that well in terms of how they're thinking about it.
[1593.56 → 1599.52] There's an image of this on a blog post that we'll link in our show notes if you want to kind of understand
[1599.52 → 1606.70] how the floating point 16, 32 and tensor float 32 compares.
[1607.10 → 1615.48] But this is definitely a new representation on this chip that I don't think has happened on any other architecture yet.
[1616.04 → 1617.92] So that might be worth pointing out.
[1618.80 → 1619.24] Yeah, totally.
[1619.36 → 1625.30] Another thing that we probably should mention from the architecture is that they've gone to the new third generation
[1625.30 → 1627.90] for NV Link and NV Switch.
[1628.24 → 1628.64] Oh, yeah.
[1629.04 → 1633.16] And that manages the network scaling of how you're moving, you know,
[1633.20 → 1635.28] your data around through the chips and stuff.
[1635.74 → 1639.46] And I think that it's something like a 10 times bandwidth, if I recall,
[1639.84 → 1642.34] in terms of what it can do compared to,
[1642.54 → 1646.48] or it may have been 10 times more than PCIe generation 4.
[1646.62 → 1648.82] I think that was what it was that I was recalling reading.
[1649.40 → 1650.90] I'm going to get the number wrong,
[1650.90 → 1656.82] but they said there was like so many terabytes per some insanely small time.
[1657.14 → 1663.14] So it was like a bunch of data you could transfer back and forth very, very quickly via these links.
[1663.88 → 1664.30] Absolutely.
[1664.72 → 1671.68] So the NV Link, that has to do with communication of data between GPUs.
[1672.12 → 1672.84] Is that the idea?
[1673.44 → 1674.84] That's what I've always assumed.
[1674.84 → 1680.86] I don't have the opportunity too often to run my training on like 32 GPUs.
[1680.90 → 1684.20] So this is where I'm kind of getting to the edge of my understanding.
[1684.46 → 1686.36] But I did watch a YouTube video.
[1687.34 → 1689.48] And I think that's what they implied.
[1689.90 → 1691.96] Is that like staying at a Holiday Express?
[1692.46 → 1694.56] Yeah, I've stayed at a Holiday Inn Express.
[1694.80 → 1694.92] Exactly.
[1694.92 → 1695.32] There you go.
[1695.44 → 1695.58] Yeah.
[1695.66 → 1697.68] So I've watched the YouTube video.
[1698.02 → 1699.36] My understanding was like,
[1700.24 → 1703.78] because people also build these Bitcoin mining rigs, right?
[1703.78 → 1707.68] And they have all these GPUs on top, and they're running all the time.
[1708.70 → 1713.36] And the way they do that is they basically connect a bunch of them to PCI slots on a motherboard.
[1714.22 → 1719.44] And to do that, they have these little adapters called risers that like come out of the motherboard.
[1719.68 → 1723.80] But apparently those are very slow in terms of communication between the GPUs.
[1723.90 → 1724.32] Yeah.
[1724.46 → 1726.62] And PCI is slow in that way.
[1726.62 → 1738.84] And so at least that's what they're implying that like NV Link and some of these other things from NVIDIA help facilitate that communication of data.
[1738.92 → 1745.24] And like you're saying, it helps scale out to like now if you have 32 GPUs in your data centre, you know,
[1745.24 → 1751.38] and you're trying to run some computation across them, you're going to need to have very quick communication.
[1751.38 → 1751.86] Yeah.
[1752.00 → 1758.72] For like scientific applications or AI applications that are not just Bitcoin mining, which is just running operations.
[1759.18 → 1761.32] There's actually communication that's needed.
[1762.02 → 1762.14] Yeah.
[1762.20 → 1768.42] If I recall correctly, and it's been a while since I've delved into those back when they originally released the architecture.
[1768.42 → 1772.62] I believe that NV Link connects GPU to GPU.
[1772.94 → 1774.78] It gives you that interconnect between the two.
[1775.36 → 1783.86] And then that, you know, essentially that mesh is something that NV Switch then connects at a higher level, combining the different NV Links too.
[1783.94 → 1784.42] Ah, I see.
[1784.54 → 1787.74] So NV Links, GPU to GPU and NV Switch.
[1787.92 → 1789.22] We'll call that now.
[1789.38 → 1794.70] But if listeners, if you know we're wrong, let us know, and we'll put a note in the show notes or something.
[1795.06 → 1796.32] That's good to make that connection.
[1796.72 → 1797.04] Okay.
[1797.04 → 1797.48] Yeah.
[1798.48 → 1821.72] And of course, these, because they're connectable and scalable in this way, it seems like this is their new way of replacing what they did have in the DGXs, which the DGXs were the sort of boxes that they put in data centres, GPU data centres to like scale up like an AI supercomputer of some type.
[1822.34 → 1822.64] Correct.
[1822.76 → 1823.98] Or a cluster of them.
[1824.14 → 1824.54] Okay.
[1824.54 → 1826.42] Which is becoming more and more common.
[1826.42 → 1835.68] And in the earlier days, you know, people would get like when the original DGX1 came out, and it had eight GPUs in it and people would get that.
[1835.76 → 1838.32] And that, that in itself, people were calling a supercomputer.
[1838.66 → 1840.86] And, you know, we talked like that such a long time ago.
[1840.92 → 1842.22] It's only been a couple of years.
[1842.22 → 1844.58] But then they moved to DGX2.
[1844.82 → 1846.60] And then that was 16.
[1846.96 → 1849.06] And then they've actually scaled back.
[1849.22 → 1851.00] And in just a moment, let's talk about that.
[1851.00 → 1862.04] The changelog is deep discussions in and around the world of software.
[1862.26 → 1863.90] And it's been going for over a decade.
[1863.90 → 1867.60] We interview hackers like Chris Anderson from 3D Robotics.
[1867.60 → 1872.58] At the time, drones were like predators and global hawks and military industrial.
[1872.74 → 1876.50] And they were classified and super, you know, $10 billion things.
[1876.50 → 1882.68] And we had just built a drone with Lego pieces around the dining room table programmed by a nine-year-old.
[1882.90 → 1885.20] And it's like, okay, that should not be possible.
[1885.50 → 1896.46] You know, when a nine-year-old can do something that is classified, that literally export control as munition with Lego, with toy pieces, it was something important in this world has changed.
[1896.46 → 1899.60] Leaders like Devin Fuel from GitHub.
[1900.16 → 1908.18] In the like 10 to 15-year range or 20-year range, what I would really like is for if you have like three 12-year-olds hanging out.
[1908.36 → 1910.20] And one of them's like, I want to be a firefighter.
[1910.28 → 1911.84] Another one's like, I want to be a lawyer.
[1911.98 → 1914.30] I want one of them to say that I want to be an open source developer.
[1914.92 → 1916.60] And innovators like Amal Hussain.
[1917.12 → 1920.34] I've yet to kind of see applications at scale that don't use multiple languages.
[1920.34 → 1926.40] That don't have just arcane stories behind why this weirdo thing exists, you know?
[1926.46 → 1931.82] Like, all right, when you open this file, you're going to have to turn around three times and tap your nose once.
[1934.32 → 1937.52] Like, it's just the most hilarious story, you know?
[1937.60 → 1939.78] But applications are living, breathing.
[1940.08 → 1941.26] They have craft.
[1941.64 → 1942.72] That's normal.
[1942.96 → 1949.20] So I want to normalize weirdness because that's just how applications evolve over time.
[1949.68 → 1951.40] Welcome to the changelog.
[1951.74 → 1955.74] Please listen to an episode from our catalogue that interests you and subscribe today.
[1955.74 → 1957.34] We'd love to have you with us.
[1969.24 → 1976.82] So now we have this new NVIDIA DGX A100, which they've kind of broken the paradigm of their labelling.
[1977.06 → 1982.48] So they went from DGX 1 originally to DGX 2, and now they've gone to DGX A100.
[1982.72 → 1983.70] Maybe you'll get one.
[1983.70 → 1984.94] I don't know if I'm going to get one.
[1986.16 → 1987.18] But we'll see.
[1987.28 → 1987.58] We'll see.
[1987.78 → 1988.42] Yeah, yeah.
[1988.68 → 1994.60] Sadly, I'm not in charge of procurement, and I am certainly not in charge of procuring one for my own personal use.
[1994.80 → 1995.46] We'll see.
[1995.62 → 1997.94] I'm guessing that my nonprofit's not going to get one.
[1997.94 → 2007.64] But if you happen to be getting your DGX A100, and you'd like me to run my training on it, I would be more than happy to do some benchmarking for you.
[2008.32 → 2008.68] Gotcha.
[2009.18 → 2012.04] I'll talk to my boss's boss's boss's boss.
[2012.24 → 2012.54] Exactly.
[2012.80 → 2013.56] See what's possible.
[2013.86 → 2014.08] Yeah.
[2014.08 → 2015.36] I'm there for you, my friend.
[2015.60 → 2017.14] I'm really into the mooching today.
[2017.74 → 2017.90] Yeah.
[2018.18 → 2018.54] Totally.
[2018.64 → 2019.12] I got it.
[2019.18 → 2019.70] I'm good.
[2019.78 → 2020.64] We're there to support you.
[2020.72 → 2021.24] I'm there for you.
[2021.78 → 2028.66] But yeah, I mean, with this new architecture, it's much more performant, but they've actually cut the number of GPUs in the server back down to eight from 16.
[2028.66 → 2034.14] But it has the enhancements that we just talked about that are at the processor level architecturally.
[2034.56 → 2042.00] So it's interesting that they kind of cut that down, but they have this multi-instance GPU capability.
[2042.20 → 2052.84] So actually, they say you can run 56 applications, GPU applications, seven per GPU times the DGX.
[2052.84 → 2064.92] Yeah, and like you were saying, even though there's fewer here, because the size increase of A100, they kind of showed this picture in the keynote, which people can watch.
[2065.08 → 2076.46] But supposedly, you can kind of reduce the size and footprint of your data centre because you're doing more computation per box per DGX than you were before.
[2077.50 → 2078.92] And this is interesting.
[2078.92 → 2086.50] They were saying like, you know, each box, let's say, I think the price they said was like a million dollars, right?
[2086.60 → 2093.74] So this is not what I'm going to be putting on my desk, but certainly within the range of like compute budgets for some companies.
[2094.42 → 2102.82] So like each one was that expensive, but you could do the same that you could if you spent previously like $11 million on your data centre.
[2102.82 → 2109.20] So like scaling wise, you can do more with less, I think is the idea.
[2110.04 → 2110.16] Yeah.
[2110.30 → 2118.40] When I was originally looking at these announcements as they came out, I think one of the call-outs here, and this architecture does start to address that.
[2118.78 → 2129.30] But I think people in organizations that can't afford to get DGX systems, and they do choose to invest in those, they underestimate what it takes to get productive with them.
[2129.30 → 2129.74] Hmm.
[2130.26 → 2135.92] And so they kind of just think, oh, I can go buy a DGX and just everything's going to work out after that.
[2136.32 → 2139.44] And then all my training will complete in three days, and I'm done.
[2139.98 → 2140.34] Exactly.
[2141.00 → 2141.68] Nothing to do it.
[2141.68 → 2152.74] But I think the challenge is when you're scaling up to one or more DGX systems, then you are talking about an overall – I'm not just talking about a DGX architecture.
[2152.88 → 2166.06] You're talking about an overall systems and software architecture in your organization and specifically data architecture that can support moving a lot of data around through training in an organized way that flows in with your business processes.
[2166.06 → 2168.18] And that is a big challenge.
[2168.18 → 2175.84] And I think – and being able to make all that work in your own organization is where a lot of organizations are struggling.
[2176.18 → 2178.44] And I know NVIDIA works hard to throw them a bone.
[2178.54 → 2179.18] They work hard.
[2179.30 → 2180.28] They recognize that.
[2180.36 → 2184.60] And there are a lot of tools that they put out there to try to help you through that process.
[2184.60 → 2206.72] But I think this architecture has kind of accounted for some of those pain points of the past, and they're trying to make it easier to utilize N number of GPUs across multiple DGXs, which is good because there are cases – there are very highly scaled cases where you might be doing a lot of experimentation with like hyperparameter optimization.
[2206.72 → 2220.38] And you want to try just an insane number of different possibilities when you're doing your training and have the ability not just to train one time but to train many, many, many times and thousands or millions even.
[2220.38 → 2227.12] And I think they've understood that and that this architecture is starting to address that highly scaled use case.
[2227.12 → 2241.82] Yeah, I think that gets to the point of sort of, you know, maybe something that is on people's mind as they listen to this is like why not just the cloud and like use GPUs in the cloud, which you can certainly do.
[2241.82 → 2252.38] So like you could, you know, if you wanted to run a thousand experiments to test all your hyperparameters, you could spin up a thousand GPU nodes in Google Cloud or Amazon or wherever.
[2252.38 → 2263.44] But if you're doing that at any sort of frequency or length, that's going to – the bill is going to add up pretty crazy fast on that.
[2263.60 → 2279.38] So if this is something that like a company actually wants to do and, you know, AI is central to their strategy, to their products, and they want to get that very best model, and they want to do that experimentation over and over and over again.
[2279.38 → 2294.36] And if this sort of DGX system is capable of supporting, you know, the usability side of things like you're talking about, then they could run those over and over again as much as they are able to usability wise.
[2294.36 → 2298.04] And so I think that that kind of gets to the point.
[2298.18 → 2313.72] For some people, like, you know, I keep joking that I'd love to have access to this, but I probably wouldn't, you know, just me myself, since I'm the AI person doing a lot of the AI things on my team, and I don't have a team of 40 different people trying to run things all the time.
[2313.72 → 2325.70] Then, you know, I'm pretty okay with using, like, a GPU instance in the cloud when I need it because I might run a training for 48 hours or even four days or something.
[2326.00 → 2328.10] But I do that not very often.
[2328.42 → 2329.16] And it's just me.
[2329.48 → 2337.70] But if you've got, like, a team of 40 people, or you've got multiple teams throughout your organization, and they all need to run that stuff, that adds up really, really quick.
[2337.70 → 2338.92] It does.
[2339.06 → 2340.24] I have been pleased.
[2340.40 → 2358.46] Just in general, when you combine the advances in NV Link and Switch, when you combine that with the multi-instance GPUs that these A100s are at this point, the scalability technology, which without diving into it, is called Eleanor Connect X-6, if I'm saying that right.
[2358.58 → 2362.06] It's a nice blend of architectural considerations to get you there.
[2362.36 → 2366.34] And, you know, we haven't even talked yet about advancements on the edge.
[2366.48 → 2366.80] Yeah.
[2366.80 → 2369.70] And that is a huge, huge area at this point.
[2370.12 → 2381.22] I'm glad you bring that up because it's probably, even though, you know, I may not get access to the sort of DGX system, I am thinking about various applications at the edge.
[2381.22 → 2387.00] And, in fact, I had a conversation earlier today with another guy who's working on totally different stuff in manufacturing.
[2387.00 → 2397.34] But they're not a large company, but they do stuff at the edge in the manufacturing setting with low-power devices already.
[2397.56 → 2399.80] Like, think like a Raspberry Pi and that sort of thing.
[2399.80 → 2414.38] But if you could bring the power of, like, this sort of GPU to, like, right to the edge to a machine where you're doing computer vision to detect, like, anomalies in your manufacturing process or something like that, that's a pretty major advantage.
[2414.38 → 2424.38] And that brings that sort of capability to those sorts of people that are working on smaller teams and have that specific use case for running AI at the edge.
[2424.38 → 2426.30] They have the NVIDIA.
[2426.64 → 2435.06] So, along with the A100, they have the EX A100, which they're releasing, which seems to benefit from some of these things that we talked about with the A100.
[2435.38 → 2437.40] But they also talk a lot about security.
[2438.14 → 2442.64] Security and an end-to-end, an encryption of AI models, encrypt all the things.
[2442.64 → 2448.62] And I have some ideas about why, you know, that may be important at the edge.
[2448.78 → 2450.30] But you have any thoughts on that?
[2450.86 → 2455.64] Well, we live in a time when, you know, we've had so many episodes where we talk about malicious actors.
[2456.00 → 2463.50] And they could be anywhere from, you know, state level all the way down to teenagers that are savvy and having some fun.
[2463.92 → 2469.28] And we're in a world nowhere you just can't really assume that you can put anything that's not secure out of the edge.
[2469.28 → 2472.20] And that doesn't have to be in the defence world, you know, where I live.
[2472.20 → 2474.74] That can be really anywhere, any industry at this point.
[2475.26 → 2479.98] So, they have had, obviously, their previous kind of edge-oriented offerings.
[2480.42 → 2484.86] And we like to, you know, there's the smaller-scaled stuff that we like to play with.
[2485.14 → 2486.58] You know, they have the NO out now.
[2486.72 → 2489.22] They've had NATO's out the last couple of years and so like that.
[2489.30 → 2498.34] But as industry really gets serious about pushing inference out to the edge and having it both widespread and pervasive,
[2498.34 → 2506.36] having kind of a comprehensive and sophisticated security model that they can deploy onto these platforms is pretty key.
[2506.36 → 2509.78] And I think that's really, at this point, it's no longer a specialty thing.
[2509.86 → 2512.52] It's now something we're all having to acknowledge.
[2512.52 → 2519.12] Yeah, because, like, if you think about products, some products that have come out over the past years,
[2519.20 → 2528.96] like if you think about a drone that's kind of come out, I think there are multiple drones now that have come out that have some sort of AI model running on them that, you know,
[2528.98 → 2533.14] does something like it follows you around or like whatever the thing is.
[2533.14 → 2536.52] It does some operation, object detection or something.
[2537.24 → 2546.16] If you're thinking about releasing a product that has, like, this sort of edge GPU running inside of it,
[2546.22 → 2551.72] whether that be in a manufacturing sense or like the drone or robot sense or something,
[2552.26 → 2556.56] really the AI model that you're releasing with that is part of your IP, right?
[2556.68 → 2559.48] And you've spent hundreds of thousands of dollars into it.
[2559.48 → 2563.30] So you got, like, the malicious actor side of thing, but you've also got the fact that, like,
[2563.94 → 2570.92] oh, if I buy a cool thing to strap on my manufacturing machine that has one of these GPUs in it,
[2571.48 → 2574.38] and it's, like, doing something sophisticated,
[2575.30 → 2579.50] well, if they're giving me the model in this product that I'm buying,
[2579.50 → 2586.04] why don't I just, like, unscrew the hatch and, like, plug my computer in and just take the model off of it,
[2586.08 → 2589.34] and now I don't have to pay them for that product anymore, right?
[2589.34 → 2597.50] So we've gotten to a point where the actual AI model is a piece of IP and is extremely valuable.
[2597.80 → 2605.18] So you wouldn't want, like, your client or your, you know, competitor especially
[2605.18 → 2608.94] to just be able to buy one of your products, unscrew the thing,
[2609.12 → 2617.88] and, like, you know, copy, you know, commode.PB from the machine over to their machine,
[2617.88 → 2621.82] and then they've ridded themselves of their need for buying your product, right?
[2622.20 → 2623.42] So, yeah.
[2623.74 → 2625.16] I was just going to say, it's funny.
[2625.16 → 2630.98] I've noticed this a lot lately, and that when we talk about the fact that you're now seeing models
[2630.98 → 2637.84] being deployed to the edge, you know, just in massively parallel, deeply pervasive in whatever your business is,
[2638.10 → 2640.84] you know, as you know, I have a daughter who's young.
[2640.84 → 2647.40] We just went through a birthday, and the toys that you can buy these days are now incorporating this stuff in.
[2647.54 → 2651.34] It is, you can actually buy toys that have convolutional neural networks in them.
[2651.42 → 2655.84] You can buy them that have NLP capability, and I think that's the moment where I find myself surprised
[2656.40 → 2659.98] because we're so used to talking about it in this kind of business-oriented contexts.
[2660.36 → 2660.44] Yeah.
[2660.44 → 2666.16] But then, you know, that's also someone else's business is to make these toys, and I, you know,
[2666.28 → 2670.86] I keep being surprised at these toys that she unwraps, and they have these capabilities.
[2671.10 → 2675.08] Of all people, I should not be surprised, I suppose, but I am just to see it in that context.
[2675.28 → 2675.30] Yeah.
[2675.46 → 2680.94] Well, and especially in that case, like, at least depending on the age of the child, you know,
[2681.56 → 2688.98] it would be important for that AI model to run offline on the device, and like, let's just keep that thing offline,
[2688.98 → 2695.64] and it's good if it acts as a toy, but let's not connect it to the wild west of the internet just yet.
[2695.76 → 2699.94] So, yeah, I definitely see, you know, you'd want to run that sort of model at the edge itself
[2699.94 → 2701.62] and upload it to the device, I think.
[2702.02 → 2705.60] The other thing I wanted to mention is, so I was going, you mentioned the NATO.
[2705.60 → 2714.00] So, if people are thinking about, like, Raspberry Pi, and this gets down maybe where it does bring some accessibility to a lot of people.
[2714.00 → 2721.48] So, there's, like, Raspberry Pi devices, which are, like, single board computer devices, which have been, of course, wildly popular.
[2722.28 → 2732.62] But NVIDIA released a Jet son NATO, which is like a single board computer with a little GPU on it.
[2732.62 → 2739.54] And I was actually thinking about getting one of those, but I don't know if it was in this series of releases or just very recently.
[2739.82 → 2746.00] They released this Xavier NO, which is, like, a next greater version of this.
[2746.06 → 2748.92] They actually call it, like, a little AI supercomputer.
[2749.32 → 2751.00] And it is a single board computer.
[2751.14 → 2757.28] It's got, like, something like a 10X computer or something like that of the NATO.
[2757.28 → 2762.28] And so, when I was going to get that one, I just ended up getting the other because it seemed pretty awesome.
[2762.48 → 2765.18] And I think that a couple of things struck me about this.
[2765.32 → 2772.46] One is, I'm always trying to think of, you know, like, for example, the cases that we work with
[2772.46 → 2779.40] and the people that work in our organization around the world, of course, work in a disconnected setting a lot of times
[2779.40 → 2780.44] because they're out in the field.
[2780.70 → 2783.70] And, of course, a lot of people around the world don't have Internet.
[2783.70 → 2789.56] But then also, you know, we're not flowing with money.
[2790.04 → 2797.26] So, like, what is a way to, like, get things running at the edge reasonably, in a disconnected offline way,
[2797.26 → 2800.48] but also at a cost-effective way?
[2800.56 → 2805.76] And I find it fascinating that some of these things are coming out that have sort of a GPU capability.
[2805.76 → 2812.70] And the Xavier in X, it's interesting that it's got the GPU and you can run inference on it,
[2812.74 → 2814.84] but you can actually update your models as well.
[2814.96 → 2819.28] So, they talk about doing transfer learning, which is like an update of a model.
[2819.38 → 2820.70] So, you're redoing some of the training.
[2820.88 → 2825.64] Maybe you're training some of the layers, or you're training additional layers that you add on to your model.
[2826.22 → 2828.08] So, I'm really curious when this comes in.
[2828.26 → 2830.60] I actually, it should be coming in today.
[2830.76 → 2832.80] So, I'm kind of watching out my window right now.
[2832.80 → 2838.34] Yeah, I'm going to reveal, before we started the episode, when Daniel and I were talking,
[2838.78 → 2842.52] he's waiting, he's watching out the window for UPS to show up with it.
[2842.52 → 2843.76] I'm stationed right by my front window.
[2843.98 → 2848.42] We might get a package opening here on air, you know, with that new NO.
[2848.48 → 2849.14] Fingers crossed.
[2850.54 → 2850.80] Yeah.
[2851.48 → 2859.02] So, I'm curious to kind of try, what I want to try, actually, is just to, like, start with a small model
[2859.02 → 2866.64] and see, like, how the training compares to, like, in some, like, with a better GPU and paper space or something.
[2866.74 → 2872.72] And then, like, try it all the way up to, like, how far can I push the training on the NO?
[2872.86 → 2877.38] Can I actually train, like, how big of a model can I train from scratch on it?
[2877.38 → 2881.22] And then, like, how big of a model can I do transfer learning on?
[2881.48 → 2884.26] Because, yeah, I find that incredibly interesting.
[2884.26 → 2888.96] The other thing that they talk about with the NO is cloud-native things at the edge.
[2889.26 → 2891.82] And I know both you and I are huge fans of Docker.
[2892.06 → 2898.94] So, I find it interesting, whereas before, I didn't see them emphasize a lot of things about using Docker at the edge
[2898.94 → 2902.16] to run, like, AI-related workflows.
[2902.28 → 2905.88] And now, they're saying, well, this is how you should do it in this device.
[2905.98 → 2907.04] I find that fascinating.
[2907.80 → 2907.94] Yeah.
[2908.08 → 2910.24] And not only Docker, but Kubernetes as well.
[2910.24 → 2914.84] It's, you know, I mean, and we've talked, I know we've talked about this on other episodes
[2914.84 → 2916.32] when we were hitting slightly different topics.
[2916.48 → 2923.34] But we really, this whole kind of AI revolution that's happened over the especially if you're
[2923.34 → 2929.28] looking at the last three to five years, we really, really benefited from what had, the
[2929.28 → 2934.50] revolution that had just swept through the software development world and software systems
[2934.50 → 2940.34] deployment world out there and that Docker and Kubernetes became the systems to build on.
[2940.88 → 2943.28] And we landed on top of that and just took that over.
[2943.42 → 2949.34] So, it's perfect to see all the hardware, whether you're talking about, you know, the lower-end
[2949.34 → 2955.40] GPUs, such as, you know, the NATO that you talked about, all the way up to, you know, the latest
[2955.40 → 2960.36] here, this, you know, DGX A100, all using that same architecture.
[2960.36 → 2965.24] And so, if you learn at one place, you can use it from the most scaled down to the most scaled-up
[2965.24 → 2965.58] version.
[2965.98 → 2968.44] And you can use it in the data centre, and you can use it in the edge.
[2968.56 → 2971.26] And that is a wonderful, wonderful thing that we've inherited.
[2971.70 → 2972.94] Yeah, I totally agree.
[2973.54 → 2975.42] I've really enjoyed talking about all of these things.
[2975.48 → 2977.30] I've got a lot to learn on all of these fronts.
[2977.52 → 2983.46] And if you're thinking like, oh, all of this GPU stuff and like accelerated AI is very new,
[2984.00 → 2985.28] don't be afraid.
[2985.28 → 2994.00] I didn't come from a sort of computer science background, but there is tooling that's accessible
[2994.00 → 2997.02] for you to, you know, get into some of these topics.
[2997.62 → 3002.38] And one learning resource, a lot of times in these fully connected episodes, we like to
[3002.38 → 3003.46] mention learning resources.
[3004.16 → 3010.46] So, actually, NVIDIA themselves have what they call the I think it's the Deep Learning
[3010.46 → 3013.18] Institute, NVIDIA Deep Learning Institute.
[3013.18 → 3019.20] And they have a series of courses that talk about everything from like getting started
[3019.20 → 3020.52] with AI on the Jet son NATO.
[3020.66 → 3025.88] That's that little single board guy that we were talking about all the way to, you know,
[3025.94 → 3030.82] more advanced topics with high performance computing, high performance computing with
[3030.82 → 3031.42] containers.
[3031.42 → 3037.68] They talk about various GPU accelerated frameworks like Rapids and AI in the data centre and all
[3037.68 → 3038.64] sorts of topics.
[3038.64 → 3044.34] So, if you're interested in this sort of accelerated AI topic, you know, you might check that out.
[3044.42 → 3047.56] We'll definitely link it in the show notes as well.
[3047.62 → 3049.60] I know I have a lot to learn there myself.
[3050.64 → 3056.48] So, I'm going to go slightly off-topic, but it just occurred to me as we were talking about
[3056.48 → 3056.78] this.
[3057.10 → 3061.30] For the learning resource I'm going to throw out there, it's going to be one that a friend
[3061.30 → 3063.58] of mine mentioned just earlier today.
[3063.58 → 3064.22] Good.
[3064.22 → 3065.72] That he has utilized.
[3066.36 → 3072.44] For those of you who may be familiar with the learning site Udemy, U-D-E-M-Y.com, there
[3072.44 → 3076.98] is a course on their called Docker and Kubernetes, the complete guide.
[3077.30 → 3080.38] It's not expensive, especially there are a lot of coupons.
[3080.48 → 3083.44] You can get it at a very low price, like 10, 12, $13.
[3083.44 → 3089.42] And so, this person had gone through that course and was like halfway, two-thirds of
[3089.42 → 3092.44] the way through and just thought it was fantastic to ramp up on it.
[3092.60 → 3096.24] So, given that recommendation, I'm going to recommend that to everybody, and we will put
[3096.24 → 3097.32] a link in the show notes.
[3097.54 → 3102.10] Because if you're going to be in the AI world, it really pays to understand Docker and Kubernetes
[3102.10 → 3102.46] well.
[3103.18 → 3103.54] Awesome.
[3103.84 → 3104.02] Yeah.
[3104.18 → 3105.80] Well, check those things out.
[3106.18 → 3111.30] Reach out to us on our Slack channel or on LinkedIn or Twitter with any questions or thoughts
[3111.30 → 3114.44] that you have and hope that this has been a fun episode.
[3114.56 → 3115.22] It has for me.
[3115.86 → 3116.32] It has been.
[3116.58 → 3118.62] We will see you next week.
[3118.70 → 3119.18] See you, Chris.
[3119.48 → 3120.10] See you later.
[3120.28 → 3124.66] And I apologize to the NVIDIA people who are going, oh my gosh, those guys, they need to
[3124.66 → 3125.90] know more about it before they talk.
[3125.90 → 3132.12] We accept feedback and the show notes and everything is on GitHub so you can submit a PR.
[3132.54 → 3133.40] So, yeah.
[3133.56 → 3133.84] Okay.
[3133.92 → 3134.60] Feedback welcome.
[3135.62 → 3136.68] See you next time, Daniel.
[3136.88 → 3137.20] Bye.
[3141.30 → 3143.30] Thank you for listening to Practical AI.
[3143.74 → 3145.84] We appreciate your time and your attention.
[3146.54 → 3149.84] Word of mouth is the number one way people find new podcasts.
[3150.34 → 3153.90] If Practical AI has helped you on your AI journey, please do tell a friend.
[3154.02 → 3155.26] Hey, they'll thank you later.
[3155.82 → 3160.06] Special thanks to Break master Cylinder for the beats and to our awesome partners for their
[3160.06 → 3160.42] support.
[3160.82 → 3163.32] Shout out to Vastly, Linde, and Rollbar.
[3163.92 → 3169.50] If you and your organization would benefit by speaking directly to the AI community, you should
[3169.50 → 3170.74] sponsor Practical AI.
[3171.34 → 3174.94] Podcast advertising is highly effective, and we would love to work with you.
[3174.94 → 3178.00] Head to changelog.com slash sponsor to learn more.
[3178.88 → 3179.90] That's all for now.
[3180.20 → 3181.56] We'll talk to you again next week.
