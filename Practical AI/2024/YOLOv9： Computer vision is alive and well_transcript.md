[0.00 --> 8.66]  Welcome to Practical AI.
[9.14 --> 17.12]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing
[17.12 --> 19.58]  the world, this is the show for you.
[20.22 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 30.94]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions
[30.94 --> 35.44]  on six continents, so you can launch your app near your users.
[35.84 --> 37.84]  Learn more at Fly.io.
[42.66 --> 48.50]  Welcome to another fully connected episode of the Practical AI podcast.
[48.84 --> 54.50]  In these fully connected episodes, Chris and I keep you fully connected with everything
[54.50 --> 57.76]  that's happening in the AI and machine learning world.
[57.88 --> 66.44]  We'll take some time to dig into the latest news articles and releases from the AI community
[66.44 --> 71.62]  and hopefully share some learning resources that'll help you level up your machine learning
[71.62 --> 71.98]  game.
[72.58 --> 74.40]  My name is Daniel Whitenack.
[74.48 --> 80.26]  I am the founder and CEO at Prediction Guard, and I'm joined as always by my co-host, Chris
[80.26 --> 83.06]  Benson, who is a tech strategist at Lockheed Martin.
[83.06 --> 84.10]  How are you doing, Chris?
[84.10 --> 85.20]  Doing great, Daniel.
[85.26 --> 85.74]  How's it going?
[86.32 --> 87.02]  It's going great.
[87.12 --> 94.60]  I'm spending a few weeks in the UK, which is a lot of fun and have got enough sleep to
[94.60 --> 98.74]  not be jet lagged quite as much, so that's encouraging.
[99.68 --> 102.78]  Okay, so we have a transatlantic podcast going here today.
[102.96 --> 103.46]  Exactly.
[103.84 --> 104.40]  Worldwide.
[104.56 --> 105.06]  That's right.
[105.28 --> 106.16]  Across the pond.
[106.60 --> 108.24]  Practical AI worldwide.
[108.60 --> 110.74]  21st century incorporated.
[111.04 --> 111.34]  I don't know.
[111.38 --> 112.20]  We need rebranding.
[112.20 --> 113.12]  Exactly.
[113.56 --> 113.76]  Yeah.
[113.98 --> 114.24]  Yeah.
[114.70 --> 120.16]  Well, Chris, one of the things I was going through, I don't know how often people are
[120.16 --> 127.08]  flying these days, but one of the things that stood out to me as I took my flight across
[127.08 --> 133.94]  the pond was now when you board at least some flights, you don't even give them your ticket,
[134.10 --> 134.32]  right?
[134.32 --> 140.28]  You just go up and there's a little, I guess you would call it a kiosk, a little edge device
[140.28 --> 147.06]  that takes a picture of your face and matches it, I assume, with what was your scanned passport,
[147.30 --> 151.44]  which you scanned at the time of check-in and you board your plane, of course.
[151.44 --> 154.74]  And it was really, really fast as well.
[154.82 --> 160.02]  And the same thing happened, you know, crossing into the border, into the UK.
[160.46 --> 165.80]  As long as you have a certain passport, you just go up to the little machine and scan your
[165.80 --> 167.58]  passport and then it takes your picture.
[167.88 --> 170.94]  And I'm assuming I could do a little bit of research.
[170.94 --> 176.54]  I'm assuming what's happening under the hood is that it's matching your actual facial features
[176.54 --> 185.68]  up with the image on your passport and computing some score of shadiness or something like that,
[185.68 --> 189.98]  or risk associated with you not being the person in the end.
[190.06 --> 192.52]  But I was amazed at how fast it was.
[193.02 --> 195.12]  And I'm assuming I could be wrong.
[195.28 --> 200.80]  I'm assuming maybe some of that's running at the edge, not reliant on an internet connection.
[200.94 --> 202.76]  To do that facial recognition.
[202.90 --> 207.38]  I'm not sure if you know or if you've had also this experience, Chris.
[207.62 --> 211.96]  I don't know what they're using algorithmically, but I definitely partake of the technology.
[211.96 --> 218.14]  It's an area that I forgo privacy and always buy my way into expeditious processing.
[218.38 --> 219.46]  So yes, I'm curious.
[219.80 --> 222.00]  Well, I don't know in that case if you have a choice.
[222.24 --> 225.56]  Maybe there is an opt-out situation or something.
[225.70 --> 226.20]  I'm not sure.
[226.80 --> 230.78]  But it's pretty cool that some of this technology is being applied.
[230.94 --> 238.78]  At the edge and in a very seemingly efficient way, such that you could use it on a mass scale
[238.78 --> 239.50]  like that.
[239.58 --> 243.62]  Or I don't know if you'd consider that a mass scale, but it's definitely in use for many.
[244.18 --> 247.06]  You know, there's a huge flood of people going through those stalls.
[247.56 --> 253.56]  And the computation happens very quickly and reliably enough to make a judgment.
[253.56 --> 261.16]  In the midst of all the hype around generative AI, one of the things that stood out to me over this
[261.16 --> 266.70]  last news cycle, Chris, was the release of YOLO V9.
[267.12 --> 270.94]  So we're on the ninth iteration of this YOLO model.
[271.50 --> 277.08]  Did you happen to see any of the videos of YOLO 9 in action, Chris?
[277.08 --> 280.12]  I haven't seen the YOLO 9 one, but I'm kind of stunned.
[280.36 --> 283.62]  You know, when you think about it, YOLO has been around a long time, I was occurring to
[283.62 --> 289.58]  me, because we actually had some conversations about YOLO back in the very first days of this
[289.58 --> 292.74]  podcast, which has been, you know, closing in on six years now.
[293.26 --> 295.68]  So it's V9 is a long time coming.
[295.92 --> 299.64]  And we haven't really gone back and touched such models in quite a while.
[299.72 --> 300.68]  It's we're long overdue.
[300.68 --> 301.90]  Yeah, yeah.
[302.04 --> 308.94]  So as everyone is freaking out and enjoying the hype over large language models and other
[308.94 --> 315.04]  generative types of models, Sora and all the things coming out in the background somewhere,
[315.22 --> 320.70]  there's these amazing computer vision people that are just really cranking and innovating
[320.70 --> 326.18]  actually at the architecture level of neural networks in really interesting ways.
[326.26 --> 329.56]  So it might be good to set a little bit of background for this.
[329.56 --> 335.00]  Chris, you mentioned we've been kind of talking about YOLO for some time.
[335.54 --> 342.32]  So if people just search for YOLO, Y-O-L-O object detection, you'll see, you know, a huge
[342.32 --> 347.30]  set of articles and GitHub and everything about YOLO.
[347.62 --> 355.44]  YOLO actually kind of made a splash because it processed entire images in a single pass for
[355.44 --> 358.22]  object detection and bounding box detection.
[358.22 --> 364.02]  So if you think about if you've ever seen one of those videos of like a street with a
[364.02 --> 370.04]  bunch of people walking around and cars and dogs and shops and scooters and whatever.
[370.50 --> 371.60]  With their boxes around them.
[371.74 --> 371.90]  Yeah.
[371.92 --> 376.28]  And they have their boxes around them and they they're labeled person or whatever.
[376.60 --> 378.14]  That's likely YOLO.
[378.14 --> 384.44]  So what happens is that single image in a YOLO model goes into the model and then outcomes
[384.44 --> 390.42]  the bounding boxes and the actual classification of those bounding boxes, which is interesting
[390.42 --> 393.78]  because previous models previous to YOLO.
[393.78 --> 400.88]  I'm still sure some models do this in a multi stage way, which is more computationally expensive.
[400.88 --> 405.98]  So they actually take multiple passes through a model or multiple models to compute both the
[405.98 --> 408.42]  bounding boxes and the classes.
[408.58 --> 414.68]  Yeah, I remember way back when we were first starting and I was at a different employer.
[414.68 --> 417.90]  I was at Honeywell leading AI there at the time.
[417.90 --> 423.06]  I remember just as YOLO 2 came out, we were using that for a couple of projects that we
[423.06 --> 424.90]  were working on way back in the day.
[424.98 --> 428.98]  But that seems I mean, that's like before dinosaurs were in the earth by standards.
[429.18 --> 430.44]  But yeah, way back.
[430.80 --> 430.96]  Yeah.
[431.08 --> 439.18]  And I think even we had a podcast episode maybe about fast our CNN or whatever it's called
[439.18 --> 440.92]  the fast version of our CNN.
[441.36 --> 441.90]  Good memory.
[442.52 --> 442.88]  Yeah.
[442.88 --> 443.20]  Yeah.
[443.22 --> 443.58]  Good memory.
[444.02 --> 444.94]  That one's cool.
[444.94 --> 451.98]  I mean, that one, I think how that one worked was you pass your image in and then it detects
[451.98 --> 454.08]  the bounding boxes of objects.
[454.08 --> 462.26]  And then in a second pass, it then classifies each kind of sub section of the image as its
[462.26 --> 468.06]  class, which also is very effective, but it's less efficient computationally than the YOLO
[468.06 --> 470.28]  kind of single pass thing.
[471.02 --> 473.64]  And as you mentioned, there've been multiple versions of this.
[473.64 --> 479.92]  So between YOLO and now version two, version three, all the way up to version nine, kind
[479.92 --> 487.80]  of each version of these in some ways has, and not just in a kind of more train with more
[487.80 --> 493.80]  data way, they've actually made kind of very significant discoveries and improvements in
[493.80 --> 499.88]  neural network architecture, training methodologies, this sort of thing that has led it to be kind
[499.88 --> 507.00]  of the go to solution for at least real time object detection in images, which is why you see all
[507.00 --> 511.54]  these videos of the bounding boxes around, around people and such.
[511.92 --> 516.02]  They've at least gotten the visual bit a little bit nicer than they used to where you had the
[516.02 --> 518.12]  big clunky boxes overlaying everything.
[518.36 --> 519.02]  That was correct.
[519.36 --> 519.52]  Yeah.
[519.52 --> 519.80]  Yeah.
[519.80 --> 520.08]  Yeah.
[520.08 --> 528.32]  Well, the V9 version of the project, which dropped, at least if the date on the archive
[528.32 --> 536.08]  article link is right, that would have been the 21st of February of 2024, as we're recording
[536.08 --> 536.44]  this.
[537.10 --> 543.96]  So not that long ago, but it was developed by an open source team and kind of built on top
[543.96 --> 548.58]  of a code base from Ultralytics YOLO version five.
[549.24 --> 555.46]  And it's released, I believe, under the GPL three license is the code that they released.
[555.62 --> 564.20]  But it seems like what they focused on with YOLO V9 was continued focus on efficiency to
[564.20 --> 570.18]  where you can do real time object detection, meaning as the frames of a video are coming in,
[570.18 --> 573.84]  you can process those in real time with the model.
[574.02 --> 577.54]  So efficiency is really key in these types of applications.
[578.18 --> 584.78]  And then they focused on one of the fundamental challenges of deep learning models of these
[584.78 --> 592.44]  deep neural network models, which is called the information bottleneck principle, which happens
[592.44 --> 598.44]  because especially as you kind of propagate, if you think about a neural network, what it is
[598.44 --> 600.62]  is a big data transformation, right?
[600.66 --> 607.46]  You take a bunch of matrix data in the front end, maybe representative of an image, and that
[607.46 --> 611.06]  gets processed through successive layers of processing.
[611.72 --> 616.50]  And then out the other end comes maybe these indication of classes or other things.
[616.66 --> 624.92]  And the information bottleneck principle talks about the errors or the lack of information or
[624.92 --> 631.32]  the loss of information that you lose as you process an input through the successive layers
[631.32 --> 638.86]  of the feedforward process of that neural network, which in some ways can be addressed by having
[638.86 --> 641.26]  bigger networks and more data.
[641.82 --> 648.14]  Maybe you're less prone to these informational problems, but it's more of a problem when you're
[648.14 --> 654.18]  dealing with these very efficient, lightweight networks like the YOLO networks, because you have
[654.18 --> 658.70]  less layers to deal with and you don't want to lose any information that might be relevant
[658.70 --> 661.48]  to the classification of the outputs.
[662.10 --> 668.20]  I notice within YOLO's nine docs, they talk about also reversible functions as well.
[668.74 --> 675.06]  Does that feed into, no pun intended, does that feed into the ability to not lose data by reversing
[675.06 --> 677.54]  that feedforward through a function backward?
[677.72 --> 679.42]  How do you see that utility?
[679.42 --> 680.10]  Yeah.
[680.34 --> 685.96]  So the interesting way that they dealt with this or kind of address this, at least in
[685.96 --> 691.88]  this version of the model, is something that they're calling programmable gradient information
[691.88 --> 693.58]  or PGI.
[694.26 --> 702.68]  And the PGI portion of their research and advancement relies on a couple of things.
[702.68 --> 710.56]  But one of the main things is this focus on, again, improving the informational efficiency
[710.56 --> 712.16]  of the network.
[712.50 --> 717.86]  And one of the ways that they've done this is with what they call an auxiliary reversible
[717.86 --> 718.68]  branch.
[718.96 --> 722.32]  And this gets to these reversible functions that you mentioned.
[722.54 --> 728.80]  So the concept of a reversible function for those that maybe that's new to them means that
[728.80 --> 735.28]  the function and the inverse of the function can transform data without the loss of information.
[735.88 --> 738.88]  And so, again, there's that loss of information piece there.
[739.00 --> 744.18]  And so it's a little bit hard to describe this on the podcast without having a whiteboard or
[744.18 --> 744.66]  a visual.
[745.28 --> 750.84]  But if you think about this PGI functionality that they've added into the network, it's kind
[750.84 --> 757.86]  of like they're bolting on this auxiliary reversible branch, which helps deal with this information
[757.86 --> 762.66]  loss as gradients are calculated during the training process.
[762.66 --> 770.26]  And so during the training process, this reversible branch helps not lose that gradient information
[770.26 --> 776.26]  as during the forward pass and during the calculation of the updates of the weights of the model.
[776.26 --> 780.46]  And that helps it be very efficient during the training process.
[780.46 --> 787.08]  But it's called auxiliary, which is key because you can actually unbolt it and take it off for
[787.08 --> 793.22]  inference, which means I think part of the problem in the past with these reversible branches and
[793.22 --> 800.58]  efforts at this were helped with the information loss, but it also decreases the efficiency in terms
[800.58 --> 803.64]  of computational efficiency of the model during inference.
[803.64 --> 809.10]  I'm going to throw a question at you, and I realize this is not your thing, but just in
[809.10 --> 814.58]  case, is you're using a reversible function in that programmable gradient information process
[814.58 --> 815.70]  that you're talking about.
[815.98 --> 820.10]  And in a normal feed forward network, you know, you're maintaining the weights as they're going
[820.10 --> 822.00]  through and change those are changed.
[822.26 --> 828.54]  And are you reversing functions to maintain that back in the same space to where you're actually
[828.54 --> 829.54]  maintaining a new weight?
[829.54 --> 834.22]  And you're keeping that that gradient information for maybe future feed forward passes?
[834.22 --> 836.94]  Or do you have any sense of what the purpose of that is?
[836.94 --> 843.14]  Yeah, I think that so definitely we'll link some of the papers and the explanations and
[843.14 --> 843.88]  the show notes.
[843.88 --> 850.28]  So feel free to to look at that for accurate information and let us know if we get it wrong.
[850.28 --> 857.36]  But yeah, I think that the idea is that and the reason why this is especially useful in the
[857.36 --> 864.62]  training side of what they're trying to do, and it's kind of unbolted during the inference side,
[864.62 --> 871.52]  is that during the training time, it's really crucial that as you're calculating the updates to your
[871.52 --> 877.46]  weights, you can do that in a very informationally accurate, precise manner,
[877.46 --> 884.08]  especially for these lightweight networks, which have fewer parameters to train.
[884.08 --> 889.64]  And so maintaining that information, especially as you're calculating updates based on the gradients
[889.64 --> 890.60]  is really important.
[890.60 --> 891.20]  Gotcha.
[907.46 --> 910.68]  This is a changelog news break.
[911.36 --> 914.56]  Shipping quality software in hostile environments.
[915.22 --> 916.84]  Luca Klederic writes, quote,
[916.84 --> 923.22]  I once had the opportunity to work for a startup that had fallen from tech debt into tech bankruptcy.
[923.70 --> 926.44]  Bankruptcy, Michael, is nature's do-over.
[926.96 --> 927.92]  It's a fresh start.
[928.06 --> 928.90]  It's a clean slate.
[929.36 --> 931.02]  Like the witness protection program.
[931.40 --> 931.68]  Exactly.
[931.68 --> 932.32]  Not at all.
[932.32 --> 937.16]  Although we managed to get it back on the right track, it made me rethink the concept of tech debt
[937.16 --> 940.70]  and how we ship software, especially in hostile environments.
[941.14 --> 941.48]  End quote.
[941.90 --> 947.72]  He goes on to tell this true story in great detail, which is horrifying, yet echoes so many of our
[947.72 --> 948.22]  experiences.
[948.66 --> 951.96]  Here's just one of the many horror scenes Luca describes.
[952.34 --> 952.68]  Quote,
[952.68 --> 959.16]  There is also a handcrafted build server, a Jenkins box hosted in the office, but no record of how
[959.16 --> 960.60]  it's provisioned or configured.
[960.96 --> 965.14]  If something were to happen to it, the way you build software would just be lost.
[965.66 --> 969.28]  Each job on it is subtly different, even for the same tech.
[969.52 --> 974.70]  You have an Android source code that you build three instances out of, but each of them builds
[974.70 --> 975.80]  in a different way.
[976.06 --> 976.54]  End quote.
[976.54 --> 983.02]  This is a solid essay replete with warnings and a plea at the end to ditch the tech debt
[983.02 --> 984.26]  concept altogether.
[984.66 --> 989.86]  You just heard one of our five top stories from Monday's Changelog News.
[990.24 --> 994.76]  Subscribe to the podcast to get all of the week's top stories and pop your email address
[994.76 --> 1001.12]  in at changelog.com slash news to also receive our free companion email with even more developer
[1001.12 --> 1002.62]  news worth your attention.
[1002.62 --> 1006.52]  Once again, that's changelog.com slash news.
[1011.32 --> 1018.76]  We talked a little bit about YOLO version 9's programmable gradient information.
[1019.10 --> 1023.46]  I had to remind myself, PGI, programmable gradient information.
[1023.86 --> 1027.46]  The other piece of the architecture, and I think this is just really interesting.
[1027.46 --> 1034.50]  You've sort of got all of this going on on the LLM side where things are getting very interesting
[1034.50 --> 1038.94]  ways to fine tune and preference tune and all these families of models.
[1039.10 --> 1044.74]  On the computer vision side, man, they're really, really thinking deeply about the architectures
[1044.74 --> 1049.42]  going into these models, which have made them so, so efficient.
[1049.42 --> 1054.82]  The other thing that kind of is a combination of things that have come in the past that they're
[1054.82 --> 1060.70]  utilizing in this YOLO v9 is a generalized Elon architecture.
[1061.54 --> 1068.70]  So this is kind of a progression of a couple of things that have been in YOLO models in previous
[1068.70 --> 1072.42]  generations, but they've combined them in kind of a unique way.
[1072.42 --> 1077.94]  This stands for Generalized Efficient Layer Aggregation Network, or GELON.
[1078.60 --> 1087.06]  And this combines a couple of things from previous generations of YOLO and from things like CSP
[1087.06 --> 1087.60]  net.
[1087.96 --> 1094.48]  This has to do with how features are aggregated and gradients are aggregated through the model
[1094.48 --> 1095.82]  in a very efficient way.
[1095.82 --> 1103.82]  Again, leading to a very parameter efficient model, meaning a smaller set of parameters
[1103.82 --> 1111.42]  in YOLO v9 will have similar performance to maybe models with many more parameters.
[1111.76 --> 1114.04]  So this leads to the efficiency overall.
[1114.46 --> 1115.24]  It's pretty interesting.
[1115.52 --> 1121.10]  They talk about being able to adapt to a much wider range of applications without sacrificing
[1121.10 --> 1122.80]  speed or accuracy.
[1122.80 --> 1125.52]  Is that a form of fine tuning the model?
[1125.82 --> 1129.66]  Or something that they're doing ahead of time that you're then fine tuning on top of that?
[1130.30 --> 1137.08]  At least how I read some of that flexibility in was, yes, there's kind of a parameter efficient.
[1137.48 --> 1145.22]  This is a parameter efficient setup for fine tuning maybe to a variety of types of scenarios
[1145.22 --> 1152.56]  or even training a new model from scratch in an entirely new domain and doing that very
[1152.56 --> 1152.96]  efficient.
[1152.96 --> 1160.32]  And some of the things that I've seen, people have already quantized this model using things
[1160.32 --> 1167.34]  like OpenVINO, which is very popular for these kind of edge vision cases, and running this
[1167.34 --> 1168.12]  very efficient.
[1168.38 --> 1174.94]  So real-time object detection on even desktop or laptop CPUs.
[1174.94 --> 1180.52]  So the new architecture developments are both geared towards, yeah, that efficiency, but
[1180.52 --> 1186.38]  also squeezing every ounce of performance out of parameter efficient models, both in terms
[1186.38 --> 1189.54]  of training and flexibility across different use cases.
[1190.04 --> 1190.10]  Yeah.
[1190.20 --> 1195.02]  I think there's great applications for this on the edge where you're not in one of the
[1195.02 --> 1199.58]  giant clouds with essentially, if you're willing to pay for it, infinite compute available
[1199.58 --> 1202.72]  to you, whether it be training or for inference either way.
[1202.72 --> 1206.96]  So the fact that this can run on just about anything, I mean, back in the early days, we
[1206.96 --> 1212.84]  could do YOLO v2 on smaller equipment, but it didn't run smoothly.
[1213.06 --> 1216.26]  You'd have points where it would overwhelm the computational cycle.
[1216.50 --> 1219.82]  And so it's nice seeing something like this has come this far.
[1220.06 --> 1221.50]  It's quite an open source library.
[1221.50 --> 1222.26]  Yeah.
[1222.50 --> 1229.32]  And there's a link that we'll add into the show notes, which includes a notebook for running
[1229.32 --> 1234.88]  YOLO v9 in a collab notebook, even like I say, on CPUs.
[1235.56 --> 1243.58]  So in terms of the efficiency, one of the things that I saw was YOLO v9 operates with 42% fewer
[1243.58 --> 1252.92]  parameters and 21% less computational demand than YOLO v7, yet it achieves comparable accuracy.
[1253.66 --> 1256.76]  So, you know, it was already fairly accurate, right?
[1256.82 --> 1262.10]  And kind of an industry standard, but now with much fewer parameters.
[1262.10 --> 1267.54]  And I think that that is definitely a trend that we've been seeing not only in computer
[1267.54 --> 1275.78]  vision, but in other cases where you see things like OLAMA or other things that LAMA CPP that
[1275.78 --> 1281.54]  are allowing you to run large language models on a variety of hardware, including just on
[1281.54 --> 1283.42]  your local laptop.
[1283.42 --> 1292.74]  And, you know, quantization type of libraries like bits and bytes and optimum and big DL and
[1292.74 --> 1299.80]  these libraries that allow you to run maybe 7 billion parameter large language models or
[1299.80 --> 1306.86]  other generative AI models, but in lower precisions so that you can run them on a variety of hardware
[1306.86 --> 1308.82]  or optimize them for a variety of hardware.
[1308.82 --> 1316.48]  We also had Neural Magic on the show a little while back now, who has a set of libraries for
[1316.48 --> 1320.06]  optimizing models to run on CPUs.
[1320.62 --> 1325.84]  And yeah, so there's a lot of kind of precision and quantization that can happen even on top
[1325.84 --> 1328.92]  of the use of these parameter efficient models.
[1329.26 --> 1336.52]  One of the interesting things also that I saw this last new cycle, which at least in the circles
[1336.52 --> 1342.22]  that I run in with large language models, people were talking about a lot, which is this release
[1342.22 --> 1348.56]  from Microsoft or a paper from Microsoft that I think is titled something like the era of
[1348.56 --> 1354.68]  one bit LLMs, which is interesting because, you know, a lot of people have talked about going
[1354.68 --> 1360.88]  from maybe float 32 to float 16 and eight and four bit precision, that sort of thing.
[1360.88 --> 1368.54]  And this kind of brings in this idea of one bit LLMs with this architecture bit net.
[1369.34 --> 1376.20]  And so I found it interesting that we got both YOLO v9, but now comes on the LLM side, this
[1376.20 --> 1377.90]  one bit architecture.
[1378.62 --> 1381.46]  And it seems like a similar thing is happening.
[1381.58 --> 1387.16]  I don't know if you remember back when we were talking about our CNN and some of the larger
[1387.16 --> 1393.62]  computer vision models, we've seen the progression to more and more parameter efficiency and flexibility
[1393.62 --> 1395.74]  across deployment scenarios.
[1396.52 --> 1403.74]  And now we're seeing that maybe in a more rapid way with LLMs and this, you know, one bit
[1403.74 --> 1409.08]  LLM, but also all the other quantization and that sort of stuff that we've seen on the generative
[1409.08 --> 1409.54]  side.
[1410.08 --> 1414.22]  Do you have any sense from an application standpoint, like where you might go with these one bit
[1414.22 --> 1414.74]  LLMs?
[1414.88 --> 1417.04]  Like what are some of the use cases that come to mind for you?
[1417.58 --> 1419.02]  Yeah, I think it's interesting.
[1419.02 --> 1427.02]  So this one bit LLM that was released, they talk about it having similar performance to
[1427.02 --> 1434.00]  a model of the same parameter size, but more computational efficiency, because of course, these parameters
[1434.00 --> 1437.84]  are bits are actually not just zero and one.
[1438.08 --> 1442.20]  We can talk about that here in a second, but more computational efficiency.
[1442.20 --> 1449.16]  So I think that this is really interesting for cases where you do want to run maybe an LLM
[1449.16 --> 1455.94]  on an edge device in a scenario like think about disaster relief and you have a device out
[1455.94 --> 1463.06]  in the field that's giving help to first responders or something, giving them information or processing
[1463.06 --> 1465.88]  information from training documents or something.
[1465.88 --> 1468.76]  And you're using an LLM to provide answers.
[1469.02 --> 1473.18]  It's likely very spotty internet connection in that case.
[1473.34 --> 1479.48]  And so having something that could run on device in a variety of scenarios would be quite
[1479.48 --> 1479.90]  relevant.
[1479.90 --> 1483.78]  So one scenario would be lack of connectivity.
[1484.36 --> 1492.54]  I think another scenario would be very latency sensitive scenarios where you want a response very quickly.
[1492.76 --> 1499.10]  You don't want to have to rely on network overhead or things going out of a network that you're operating
[1499.10 --> 1500.60]  in for security reasons.
[1500.80 --> 1503.20]  That sort of thing might be a good use of these.
[1503.20 --> 1503.80]  Yep.
[1504.06 --> 1505.02]  That sounds interesting.
[1505.22 --> 1510.00]  They have a term in here that I'm curious about referring to BitNet.
[1510.30 --> 1518.24]  They talk about it being a 1.58 bit LLM and hugging face in their paper notes that all large
[1518.24 --> 1519.80]  language models are 1.58.
[1520.10 --> 1521.64]  Do you have any comment about that?
[1521.84 --> 1522.54]  What that means?
[1523.00 --> 1526.58]  The reality is if you, I think they talk about this in the paper.
[1526.58 --> 1535.16]  If you go down to a truly 1-bit LLM, each weight of your model is either 0 or 1, right?
[1535.70 --> 1540.58]  Then, yeah, you would expect to lose a lot of information that might be important.
[1541.06 --> 1543.86]  And so they make a slight compromise in here.
[1544.52 --> 1546.32]  Maybe it's unfair to call it a compromise.
[1546.32 --> 1555.56]  They make an astute conversion from bytes, in other words, 0 to 1 or bits, to what they
[1555.56 --> 1557.96]  call ternaries.
[1558.56 --> 1564.66]  So these are basically triplets or three bits together.
[1564.92 --> 1569.66]  So you have, for example, weight could be minus 1, 0, 1 or something like that.
[1569.66 --> 1574.66]  So you've got three numbers that represent certain information.
[1574.86 --> 1578.98]  And that's where they kind of get this 1.58 bit.
[1579.26 --> 1579.38]  Gotcha.
[1579.72 --> 1586.96]  So this is also why it's kind of, they release this new type of architecture that processes
[1586.96 --> 1593.98]  these ternary bits or ternaries, these combinations of three bits.
[1594.24 --> 1597.82]  And that's presented in the Microsoft paper.
[1597.82 --> 1600.68]  But yeah, I think this is only the kind of latest.
[1600.94 --> 1607.04]  I think we'll see, my prediction would be that we'll see many more things like this where
[1607.04 --> 1612.14]  people are trying to be parameter and compute efficient with large language models.
[1612.78 --> 1618.58]  We've seen models getting more and more efficient and more compact over time.
[1619.22 --> 1626.16]  And as we're looking at so many smaller, very capable models being used out on edge devices,
[1626.16 --> 1631.64]  do you envision something like this where they're really targeting efficiency in terms of being
[1631.64 --> 1634.38]  able to do that in something like small electronics?
[1634.76 --> 1639.64]  Or is that a little bit overly ambitious for where this might take us in a reasonably foreseeable
[1639.64 --> 1639.98]  future?
[1640.62 --> 1646.56]  Yeah, it's actually a good question because one of the things that we saw also, I don't know
[1646.56 --> 1654.12]  if it was this week, but recently at least, was Qualcomm's announcement and release of a huge number of,
[1654.22 --> 1660.46]  I forget how many, a whole bunch of models on what they're calling the Qualcomm AI hub
[1660.46 --> 1669.10]  for models that run on device on their Snapdragon processors and other things at the edge on small devices.
[1669.10 --> 1677.06]  So these wouldn't be like the small devices of like a microcontroller or something like that.
[1677.18 --> 1683.68]  There's still a good bit of power in these processors, but it is super interesting that
[1683.68 --> 1689.64]  Qualcomm has made the effort to make these types of models, whether that be object detection or
[1689.64 --> 1697.42]  large language models or other things available in optimized forms to run on very small devices.
[1697.42 --> 1700.30]  And I think it's a trend that we'll keep seeing.
[1714.00 --> 1721.78]  It seems somehow like in computer vision, it took maybe what, five years we've been doing,
[1722.22 --> 1724.54]  five or six years we've been doing this podcast.
[1724.54 --> 1730.18]  And over that time, we've seen computer vision models shrink down and down and become faster
[1730.18 --> 1731.46]  and more parameter efficient.
[1732.04 --> 1737.62]  It almost seems like that's happening much faster on the large language model side and
[1737.62 --> 1738.96]  generative model size.
[1739.30 --> 1746.74]  It's like shrunk from five years to one year where a lot of that's coming out for on device usage.
[1746.74 --> 1752.56]  When we and the rest of the changelog team are looking at what content to bring onto the show,
[1753.06 --> 1757.22]  and there are various guests and there are all sorts of topics and advancements going out,
[1757.70 --> 1763.70]  it's become quite challenging to narrow it down to just what we can cover in these shows.
[1763.84 --> 1767.98]  And largely that's because of what Daniel was just saying, that tremendous acceleration
[1767.98 --> 1773.14]  and the advancement of this technology is very hard to keep up with and report on,
[1773.52 --> 1779.32]  especially trying to figure out what folks are most in need of hearing or being pointed to.
[1779.32 --> 1784.62]  So on any given week, which of the dozens of things that are happening do you want to do?
[1784.62 --> 1790.58]  And I would say for those out there listening, like in this episode, we've talked a lot about
[1790.58 --> 1799.16]  parameter efficient models and whether it be the Qualcomm AI models or the one bit LLMs or YOLO
[1799.16 --> 1803.48]  and running these on device and at the edge, it might be natural to think,
[1803.64 --> 1807.90]  oh, the news cycle is totally switched to local models, running all the models locally,
[1807.90 --> 1810.58]  and that'll solve all the problems.
[1810.58 --> 1816.58]  And I think the reality is in the future, it's going to be kind of both and, right?
[1816.74 --> 1825.00]  You're not going to serve, let's say that you integrate a model into some social media application
[1825.00 --> 1833.26]  or whatever mobile application, or you're serving a web app and it's got some AI integration or something
[1833.26 --> 1833.76]  like that.
[1833.76 --> 1839.76]  It's very unlikely, I think, that you're going to want to serve up millions and millions of
[1839.76 --> 1842.76]  requests using only local models.
[1843.36 --> 1848.90]  And in the same way, if you've got an enterprise batch use case, right, and you want to process
[1848.90 --> 1855.70]  1.5 million documents through a large language model, you likely don't want that running on your
[1855.70 --> 1858.12]  Mac M2 or something like that.
[1858.18 --> 1860.98]  Like that's not the deployment strategy for that scenario.
[1861.28 --> 1865.58]  But yet you will see a lot of models running at the edge or locally.
[1865.58 --> 1872.36]  And I think the reality is that we'll go into kind of a both and sort of scenario where,
[1872.98 --> 1875.42]  yes, a lot of things you'll be able to run locally.
[1875.84 --> 1880.40]  But the same as like, I mean, you can run a lot of software locally, but it doesn't mean
[1880.40 --> 1882.66]  that you're also not running software in the cloud.
[1883.24 --> 1887.24]  You know, AI is just a new layer in your kind of software stack.
[1887.26 --> 1888.40]  So we're going to run it locally.
[1888.90 --> 1889.28]  Yeah.
[1889.30 --> 1890.82]  And we're going to run it in the cloud.
[1890.82 --> 1892.56]  That's exactly right.
[1893.20 --> 1894.48]  That was where I was going to go.
[1894.68 --> 1895.96]  Anyway, you just hit it.
[1896.00 --> 1899.68]  And that was, it's following the maturity trend of software.
[1899.68 --> 1905.34]  And just as we have huge software systems that you can only run in the cloud and are massive
[1905.34 --> 1910.42]  scale, and you have apps on your phone, and you have also very small microelectronics,
[1910.42 --> 1916.86]  which have even smaller software functions on them integrated in maybe in the BIOS, all these
[1916.86 --> 1917.50]  different areas.
[1917.50 --> 1919.62]  And we're seeing models doing the same thing.
[1919.62 --> 1924.20]  So one of the things that we're often asked to address, and we have done repeatedly over
[1924.20 --> 1929.58]  the years, is what's the current way to do training and deployment?
[1929.80 --> 1935.64]  And I think to your point, Daniel, there are now, now that we're maturing rapidly in this
[1935.64 --> 1940.20]  industry, there are many ways, and there's not one right way to do it anymore.
[1940.38 --> 1946.64]  It's kind of figuring out your use case, figuring out what mixture of different model types need
[1946.64 --> 1951.60]  to contribute into that and what the architecture for all those models and how they communicate
[1951.60 --> 1954.80]  through the software and what hardware is available to them.
[1955.16 --> 1957.08]  So it's become quite complicated.
[1957.08 --> 1963.92]  There's no longer the way, you know, to borrow the Mandalorian saying it's now many ways.
[1964.26 --> 1967.26]  Do you have any thoughts on how people might approach that?
[1967.34 --> 1970.82]  How do you think about it when you're doing things in prediction guard and trying to help
[1970.82 --> 1972.64]  your customers move forward?
[1973.06 --> 1980.74]  Basically, you kind of have to split things up a little bit by stage of your project and
[1980.74 --> 1984.22]  also the use case that you're considering.
[1985.02 --> 1990.92]  So what I mean by stage of your project is I really encourage people, like especially if
[1990.92 --> 1997.14]  they have a generative AI use case, the best thing you can do to get a sense of like, let's
[1997.14 --> 2004.14]  say that I want to summarize news articles related to stocks that I want to trade on, you know,
[2004.14 --> 2005.26]  or something like that.
[2005.58 --> 2010.48]  The very best thing you can do is not jump right to, okay, I'm going to fine tune a model for
[2010.48 --> 2015.48]  that or spin up some crazy GPU infrastructure or something like that.
[2015.56 --> 2019.52]  The best thing you can do is just get some off the shelf models.
[2019.52 --> 2025.86]  And if you want to either run them, the easiest cloud way to run those would be to run them,
[2026.22 --> 2031.28]  you know, if they're small enough and just a collab notebook or a hosted notebook environment
[2031.28 --> 2036.06]  like that, that's more than enough to figure out if they're going to work for your use case,
[2036.18 --> 2036.40]  right?
[2036.86 --> 2043.44]  Or if you want to go the more local deployment route, there's things like I already mentioned,
[2043.78 --> 2048.02]  you know, of course, if you want to run YOLO, that's easier now than ever.
[2048.02 --> 2053.82]  And there's quantized versions of that that you can run on a CPU, even you don't need even a special
[2053.82 --> 2055.16]  type of hardware.
[2055.64 --> 2062.12]  But then for the generative side of things, there's things like OLAMA and LM Studio and
[2062.12 --> 2067.90]  LAMA CPP and these things that will allow you to prompt models and figure out if they'll work for
[2067.90 --> 2069.18]  your use case locally.
[2069.18 --> 2072.00]  So that's kind of exploration stage.
[2072.48 --> 2079.18]  Then you have to decide, OK, well, if this project is a work project, right, I figured out maybe that I can
[2079.18 --> 2082.36]  prototype this and figure out it might work.
[2082.62 --> 2085.62]  Then you kind of have to play through the scenarios in your mind.
[2085.74 --> 2091.00]  Well, oh, if this is a mobile app and I'm processing customers' private data,
[2091.00 --> 2097.06]  maybe it makes sense to try to run a model at the edge in my mobile app on their device, you know,
[2097.12 --> 2101.80]  a Qualcomm AI model from their AI hub on their mobile device.
[2101.92 --> 2102.98]  And that would be really good.
[2103.42 --> 2109.52]  But if it's a web app application and there's not as aggressive of a security posture,
[2109.72 --> 2115.62]  probably you want to figure out how you're going to run and host that model in a way that makes sense to you.
[2115.62 --> 2124.12]  Even from a public endpoint, that's just a product like, you know, together AI or Mistral or something like that.
[2124.12 --> 2140.98]  Or you're going to figure out how to run it in a secure local environment with either a product that can host that model in a secure environment in your own cloud or in your own network or your own kind of self-deployment of that model.
[2140.98 --> 2147.92]  Using things in your cloud infrastructure like SageMaker and AWS or other things like that.
[2148.36 --> 2153.24]  Yeah, it's increasingly, it's becoming part of the software and your larger architecture.
[2153.48 --> 2161.56]  As you, you know, we've seen in, you know, the recent couple of years, especially the strong rise of ML Ops, you know,
[2161.60 --> 2166.40]  which kind of corresponds to DevOps in terms of deployment and all those things.
[2166.40 --> 2176.32]  Do you tend to think of it in more of an integrated way or do you still at this point in time as we're in 2024, think of it as separate approaches, you know, from the software?
[2176.54 --> 2178.82]  How do you parse those two sides of that coin?
[2179.30 --> 2179.80]  It's interesting.
[2179.96 --> 2190.24]  I think I, at least in my own mind, I tend to separate them out maybe depending on some of what's involved in a project.
[2190.24 --> 2204.30]  So if it's the use of a pre-trained model, I think the burden is a lot more in kind of the traditional DevOps monitoring, testing, uptime, automation, deployment, that sort of thing.
[2204.30 --> 2210.74]  Because likely you're just interacting with the model via an API, like you would integrate any other API.
[2210.74 --> 2221.08]  Now there's certain things that can help you like versioning prompts and testing for model drift or data drift and that sort of thing.
[2221.22 --> 2226.68]  But it's not so dissimilar, I would say, to traditional software development.
[2226.68 --> 2249.62]  Whereas if you really have a unique scenario and you're fine-tuning a model for a unique scenario, you're likely going multiple iterations on curating your data set, on training your model, on evaluating your model, on versioning your model, releasing it in your model servers, updating it with new data that comes in.
[2249.62 --> 2263.58]  And I think some of that specific ML ops type of software will likely appeal to the people that are doing that process, which are usually data scientists and not software engineers.
[2263.58 --> 2280.38]  And versioning your model, versioning your model, and the way that those systems are set up, like weights and biases or clear ML and these types of things are quite useful in terms of versioning your model out when you're training it like that.
[2280.44 --> 2282.48]  So I think ML ops is alive and well.
[2282.48 --> 2297.92]  But I also think that with the rise of this kind of API driven AI development, a lot of that does or can fit into more of the DevOps side of things.
[2298.36 --> 2298.48]  Yeah.
[2298.64 --> 2308.08]  When you're using an API that somebody else is hosting, maintaining, has fine-tuned, all that, you're basically using it as a service like any other service that would not be AI.
[2308.36 --> 2311.10]  And so you just treat it as an API along the way.
[2311.10 --> 2312.12]  Yeah, yeah.
[2312.26 --> 2334.18]  And where that's maybe slightly different is you are getting kind of some variability out of that API, both in terms of performance and latency, which are maybe common across software projects, but also in terms of the performance output of the model, especially if you're using like a closed model product, like an open AI or Anthropic or something like that.
[2334.68 --> 2339.88]  They're making improvements to their underlying model under the hood all the time.
[2339.88 --> 2341.68]  And it is really more of a product.
[2342.10 --> 2343.66]  It's not just you're hitting the model.
[2344.22 --> 2350.12]  There's layers around the model, which are product layers that can influence the behavior of that model.
[2350.26 --> 2355.96]  I mean, you just kind of look at what's happened with Gemini over the past three or four weeks.
[2355.96 --> 2359.58]  We don't need to get into all of the details of that.
[2359.96 --> 2361.86]  If people want to look it up, they can.
[2362.08 --> 2380.22]  But I think a lot of those issues that that product had were actual product issues that were at the product layer surrounding the model, not performance necessarily or biases in the actual model, but in the filters around the model and how things are modified in and out of the model.
[2380.22 --> 2396.38]  And so that actual product that you're interacting with can really cause small changes in how things go into the model on the product level can make huge changes in the quality of the outputs of the model.
[2396.38 --> 2400.74]  That sounds like some pretty good practical AI advice right there.
[2400.98 --> 2409.44]  I think for me, at least, that very much helps me to kind of contextualize the different things that we may be doing at work for myself.
[2409.44 --> 2413.22]  And as we're making choices and decisions and how we're going to tackle different problems.
[2413.22 --> 2416.32]  So I appreciate you sharing that guidance there.
[2416.78 --> 2416.94]  Yeah.
[2417.32 --> 2421.28]  And I guess we're talking about the MLOps side of things.
[2421.28 --> 2428.04]  And we've talked about practicalities of deployment schemes and quantization and all of that this episode.
[2428.04 --> 2435.86]  And in terms of a learning resource for people, if they want to dive into some of this, there's a lot of great ones out there.
[2435.86 --> 2446.06]  One is to follow the MLOps community podcast, which is a podcast that Chris and I love and have collaborated with over time.
[2446.58 --> 2449.08]  Dimitrios, shout out to the great things you're doing.
[2449.48 --> 2450.44]  Funniest guy in AI.
[2451.30 --> 2451.86]  Yeah.
[2451.96 --> 2453.94]  Check out everything that they're doing over there.
[2454.08 --> 2461.08]  I also ran across this Intel MLOps professional certification from Intel.
[2461.08 --> 2468.98]  If you just search for Intel MLOps certification, this is totally free as far as I can tell.
[2469.54 --> 2473.06]  There's seven modules and eight hands-on labs.
[2473.72 --> 2486.52]  And I'm talking about software solution architectures for machine learning and AI, API and endpoint design, principles of MLOps, optimizing the full stack.
[2486.52 --> 2496.96]  So really seems to be a good set of things to look at if you're wanting to think more about the practicalities of these deployments and other things.
[2497.66 --> 2497.92]  All right.
[2498.08 --> 2498.86]  Sounds good.
[2499.26 --> 2501.50]  Well, thanks for sharing your wisdom again today.
[2501.88 --> 2502.80]  Really good episode.
[2503.08 --> 2507.86]  I'm going to, I guess I'll see you in the UK for the next few weeks to come.
[2508.26 --> 2508.78]  Sounds good.
[2508.98 --> 2509.20]  Yeah.
[2509.28 --> 2509.90]  Thanks, Chris.
[2510.00 --> 2510.68]  We'll see you soon.
[2510.92 --> 2511.42]  See you later.
[2516.52 --> 2519.88]  All right.
[2520.12 --> 2522.60]  That is Practical AI for this week.
[2523.40 --> 2524.46]  Subscribe now.
[2524.62 --> 2529.60]  If you haven't already, head to practicalai.fm for all the ways.
[2529.60 --> 2536.02]  And join our free Slack team where you can hang out with Daniel, Chris, and the entire Changelog community.
[2536.56 --> 2541.22]  Sign up today at practicalai.fm slash community.
[2541.22 --> 2548.76]  Thanks again to our partners at fly.io, to our beat freaking residents, Breakmaster Cylinder, and to you for listening.
[2549.12 --> 2550.88]  We appreciate you spending time with us.
[2551.24 --> 2552.42]  That's all for now.
[2552.66 --> 2554.38]  We'll talk to you again next time.
[2554.38 --> 2554.44]  Bye.
[2554.44 --> 2555.44]  Bye.
[2555.44 --> 2556.44]  Bye.
[2556.44 --> 2557.44]  Bye.
[2557.44 --> 2558.44]  Bye.
[2558.44 --> 2559.44]  Bye.
[2559.44 --> 2560.44]  Bye.
[2560.44 --> 2561.44]  Bye.
[2561.44 --> 2562.44]  Bye.
[2562.44 --> 2563.44]  Bye.
[2563.44 --> 2564.44]  Bye.
[2564.44 --> 2565.44]  Bye.
[2565.44 --> 2565.48]  Bye.
[2565.48 --> 2565.52]  Bye.
[2565.52 --> 2565.56]  Bye.
