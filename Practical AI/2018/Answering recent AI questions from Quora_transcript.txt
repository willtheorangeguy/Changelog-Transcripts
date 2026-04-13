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
[89.18 --> 96.26]  All right. I'm really excited to be here at O'Reilly AI with some of the Intel innovators in AI and ML.
[96.40 --> 102.40]  Really excited to ask these guys some questions today and hear from them. But before we do that,
[102.46 --> 106.48]  let's kind of go around and introduce who's in the room. So I'll start with you, Vinay.
[106.84 --> 111.56]  Thank you, Daniel. I'm a huge fan of Practical AI. Your podcast have listened to every one of your
[111.56 --> 118.96]  episodes. My name is Vinay Rao. I'm the CEO of RocketML. We make a distributed machine learning platform.
[118.96 --> 122.92]  To help data scientists do experimentation much faster.
[123.38 --> 128.54]  Awesome. And maybe everyone could share something that they're excited about in the world of AI,
[128.72 --> 129.80]  too. What about you, Vinay?
[130.04 --> 137.54]  I think the market opportunity for AI, whether it's doing machine learning or putting out products,
[137.62 --> 141.58]  AI products, is very, very large. Everybody's underestimating the market size.
[142.24 --> 147.70]  My own prediction is that, I'm going to go on a limb here, it's going to be a trillion dollar market size.
[147.70 --> 149.88]  Awesome. So let's go on there, Peter.
[150.38 --> 154.68]  So thanks for having me, Daniel. My name is Peter Mond. I'm working on a project called Clean Water AI.
[154.92 --> 159.96]  It uses computer vision and artificial intelligence to detect the bacterias and the harmful particles
[159.96 --> 160.44]  in the water.
[160.76 --> 161.76]  Awesome. That's really exciting.
[162.14 --> 168.32]  So what I'm really excited about AI is that what it can do and how it can apply into the current world
[168.32 --> 173.30]  right now from self-driving down to pretty much repetitive healthcare tasks.
[173.92 --> 179.92]  And I think in the very near future, we're pretty much going to have using it to reduce all the costs
[179.92 --> 184.42]  on the healthcare that a lot of doctors pretty much, they're just for simple screening.
[184.80 --> 187.38]  At least in the United States, that's going to be very helpful.
[187.88 --> 193.64]  Yeah. Yeah. AI is going to make a large difference for good, as well as all the malicious things that we see
[193.64 --> 196.50]  kind of advertised in industry. Yeah. It's great to get that perspective.
[196.84 --> 197.44]  What about you, Dave?
[197.72 --> 201.66]  Hey, thanks for having me. So I'm Dave. This is actually my first time on Practical AI.
[201.88 --> 205.72]  So it's very exciting to be here. So I'm a research assistant or research affiliate.
[206.06 --> 208.56]  It's a new position I just got at the University of Florida.
[208.88 --> 210.20]  I recently just finished my PhD.
[210.76 --> 211.38]  Thank you.
[211.74 --> 213.86]  So on this side, I'm also looking at other projects.
[214.02 --> 215.68]  I'm one of the Intel innovators.
[215.68 --> 220.80]  We had a demo at Intel booth today on applied AI in real retail.
[221.02 --> 223.88]  What am I excited about? I'm going to say FPGAs.
[224.04 --> 227.86]  So FPGAs are essentially like GPUs for acceleration.
[228.48 --> 233.68]  And I do know if I'm heavily into GPUs, right, with RocketML, I'm more into FPGAs for inferencing.
[233.78 --> 236.84]  So I do see a very large market for inferencing.
[237.28 --> 243.48]  My personal thing three years ago was when scientists were really going hard to develop ML models.
[243.48 --> 247.58]  And we're in the era right now, we're trying to take those ML models and put them into production.
[247.74 --> 250.70]  So there's a much larger market space in that area, for sure.
[250.70 --> 251.40]  Awesome. Yeah.
[251.78 --> 252.04]  Ali?
[252.28 --> 254.28]  Yeah, this is Ali with Netraulics.
[254.36 --> 256.84]  It's my first time with Practical AI.
[257.26 --> 260.14]  Netraulics, we're excited to use AI in the network.
[260.20 --> 265.46]  Network field, we control the traffic engineering of our core, utilizing deep learning.
[265.98 --> 268.70]  And I agree, GPU and both.
[268.84 --> 272.34]  Because we're pushing FPGA also to the edge of the network.
[272.34 --> 276.12]  We're working on pushing the AI to the edge of the network.
[276.32 --> 277.34]  So thanks for having me, Dan.
[277.52 --> 278.84]  I'm also with Netraulics.
[279.00 --> 281.96]  And I asked Ali to join because he's much smarter than I am.
[282.06 --> 284.24]  And the more I learn about this, the more I realize I don't know.
[284.60 --> 289.08]  And that being said, I like what we're doing because we're kind of the underlying technology
[289.08 --> 291.92]  to support all of the AI initiatives, which is the network.
[292.24 --> 296.78]  And optimizing the network and creating a neural behavior and self-correcting behavior in the network,
[296.92 --> 298.82]  which is 90% internet.
[299.00 --> 301.50]  And even more so as we grow into IoT and other things like that.
[301.50 --> 305.32]  What excites me about AI is actually pretty simple, the adoption of it.
[305.44 --> 309.60]  How quickly people are going to start trusting it and actually not being scared of a Skynet
[309.60 --> 314.44]  or something ridiculous, but actually putting faith in it like we do here, the group of us.
[314.60 --> 315.18]  So thanks, Dan.
[315.18 --> 315.26]  Awesome.
[315.50 --> 315.68]  Yeah.
[315.92 --> 320.04]  And Ali and Wes, just to kind of clarify, because we do talk about networks a lot,
[320.04 --> 326.04]  but you guys are talking about networks in the sense of the internet and interconnected infrastructure,
[326.26 --> 326.38]  right?
[326.42 --> 330.90]  Not necessarily neural networks, although you're using neural networks on the network, right?
[331.40 --> 331.72]  That's right.
[331.76 --> 332.94]  So it's funny.
[333.08 --> 336.70]  I say kind of tongue in cheek to people that we've harnessed the internet, right?
[336.78 --> 339.98]  But what that really means is that we're leveraging about 20,000 sensors,
[339.98 --> 344.48]  plus a footprint of about 68 data centers globally, only 22 of which are in North America.
[344.92 --> 348.84]  And essentially we just collect data, performance data, latency, jitter, packet loss, throughput,
[348.96 --> 353.06]  availability, and hundreds of other metrics that we as humans will not even think to account
[353.06 --> 355.94]  for that impact network performance over the internet.
[356.12 --> 359.04]  We take that same intelligence and apply that into security as well.
[359.04 --> 363.30]  So our security posture is equally as strong powered by AI as well, all over the internet
[363.30 --> 364.40]  as an OTT software.
[364.86 --> 368.68]  So a little bit disruptive to the service provider or equipment space, but it's fun.
[368.68 --> 369.70]  Yeah, that's awesome.
[369.94 --> 373.40]  So I have something maybe a little bit special for you guys today.
[373.80 --> 378.90]  Normally we just kind of do a standard interview, but since this is a panel and you guys are all
[378.90 --> 383.22]  experts in the field, I thought it would be fun to just pull some of the recent questions
[383.22 --> 387.12]  from Quora about artificial intelligence and machine learning.
[387.46 --> 392.42]  Get your guys' perspective to hear from some of the experts about how they would answer some
[392.42 --> 396.78]  of these questions that people are really asking as they're diving into the field.
[396.78 --> 398.44]  So does that sound okay for you guys?
[398.68 --> 399.48]  You up for the challenge?
[399.76 --> 399.92]  Yeah.
[400.12 --> 400.40]  Awesome.
[400.72 --> 406.60]  So the first of these questions is, what do I do next when I've achieved a machine learning
[406.60 --> 410.32]  program at 97% accuracy and good fit?
[410.68 --> 413.34]  And I think really, you guys are laughing a little bit.
[413.68 --> 413.78]  Stop.
[414.46 --> 414.94]  Stop.
[414.94 --> 415.02]  Stop.
[415.14 --> 417.14]  So this is the point that I was alluding to, right?
[417.26 --> 423.26]  So a few years ago, researchers were working so hard to develop models that would meet 97%,
[423.26 --> 424.24]  98%.
[424.24 --> 425.88]  But what's next after that, right?
[426.18 --> 429.64]  And so we're in the area right now, we're trying to productionize machine learning models.
[429.64 --> 434.24]  And it's very exciting to see startups that are coming up almost every day with a workflow
[434.24 --> 439.10]  to let you take machine learning models, put it into production in a more scalable fashion.
[439.24 --> 442.20]  So I really think that's the next phase of ML and AI.
[442.46 --> 444.78]  It's how do you put it into production at the edge, right?
[445.00 --> 446.26]  Or some IoT device.
[446.48 --> 446.62]  Yeah.
[446.62 --> 451.94]  So what's different, maybe to follow up on that, what's different about production or
[451.94 --> 457.86]  utilizing a model after you've kind of trained it to get a particular evaluation metric that
[457.86 --> 458.94]  you might be after?
[459.30 --> 462.30]  I think about your original question a little bit differently.
[462.74 --> 467.82]  97% might be at a particular level of problem statement.
[468.12 --> 472.42]  But as humans, we know how to split the problem into minute pieces.
[472.42 --> 476.04]  So something underneath that may not be 97%.
[476.04 --> 483.52]  As we collect more data, as companies collect more data, the new problems will start to emerge.
[483.90 --> 487.06]  Again, accuracy within that would be like 70%.
[487.06 --> 488.32]  So you'd have to increase it.
[488.36 --> 492.96]  For example, if you take translation as a problem, you know, 96% accuracy, whatever.
[493.28 --> 495.26]  But maybe some languages it's not.
[495.26 --> 503.62]  So the problem will shift as the AI practitioners will be chasing unsolved problems all the time.
[503.96 --> 504.32]  I agree.
[504.52 --> 506.08]  I think we just need to get out of the way.
[506.40 --> 511.74]  I think we learn so much as soon as we got out of the way and let that machine learning and those
[511.74 --> 514.22]  algorithms do what they do and what we designed them to do.
[514.36 --> 517.60]  And we keep getting away and we put a number like 97%.
[517.60 --> 518.86]  Who am I to define that?
[519.10 --> 525.04]  In my own mind, I can't comprehend or factualize what the 90% looks like or 97%, right?
[525.04 --> 525.80]  And you said other languages.
[526.10 --> 528.04]  We can't assume that it will be that.
[528.26 --> 531.08]  It has to, if you get to a certain level, like we say, what, 85%?
[531.22 --> 533.60]  We get to 85%, we're super excited.
[534.00 --> 537.32]  And then the rest, we kind of manage that 15%, that variable, right?
[537.66 --> 540.82]  But you have to always view it as a variable, not a static, I reached 97%, you know?
[541.08 --> 544.68]  Just to add on that, for example, self-driving car, if you take self-driving car,
[545.16 --> 552.40]  the accuracy of whatever the little functionality within self-driving car could be 90 plus in daytime,
[552.54 --> 552.90]  for example.
[552.98 --> 554.42]  But in nighttime, it may not be.
[554.42 --> 557.54]  So there will always be challenges in the area.
[558.34 --> 564.38]  Yeah, I think something I always tell people as well is to think about these accuracy or other evaluation metrics.
[564.56 --> 569.52]  It's really on a case-by-case basis because, like you said, Wes, it's not always 97%.
[569.52 --> 576.32]  If I'm in an actual real-world scenario and all we need is 80%, I would get fired if I spent, you know,
[576.40 --> 578.98]  six months trying to get anywhere past that, right?
[579.10 --> 581.44]  So you definitely have to take it case-by-case.
[581.44 --> 586.36]  Just to add a little bit to that, too, I think it's also left to us, the community, AI community,
[586.52 --> 588.54]  to sort of define what a standard is.
[588.62 --> 594.56]  So there are efforts like MLPuff, where folks from Google, Facebook, Amazon, IBM actually come together
[594.56 --> 596.94]  to define what a set of metric is.
[597.02 --> 597.82]  Like, what is the accuracy?
[597.82 --> 599.76]  What is the throughput and latency?
[600.24 --> 604.52]  So I think such efforts actually could help propel a standard benchmarking in ML.
[605.24 --> 605.58]  Awesome.
[605.90 --> 607.40]  Well, let's go on to the next one of these.
[607.52 --> 614.06]  The next one is, if I can't afford to buy a GPU, like me, maybe, for deep learning,
[614.06 --> 620.34]  what does it mean, does that mean that I can't do any serious neural network training?
[620.62 --> 621.20]  What do you guys think?
[621.48 --> 621.70]  Peter?
[622.22 --> 627.28]  So I started the entire AI without a GPU.
[627.76 --> 630.32]  I actually just got my entire GPU recently.
[630.68 --> 634.26]  There is a lot of resources online, including Intel's AI Academy,
[634.88 --> 638.52]  which gives you, you know, using CPU Xeon servers that you can train.
[638.52 --> 642.68]  And also, there's a lot of schools that you can leverage their GPU servers.
[643.12 --> 647.08]  But, you know, you have to wait a little bit online that they're generally available,
[647.40 --> 649.44]  the resources available for you to go train.
[650.08 --> 652.76]  And for the most part, when you're starting with the AI,
[652.90 --> 654.36]  I don't even recommend you go training.
[655.36 --> 659.58]  There's thousands and thousands of pre-trained models that you can actually start practicing.
[659.96 --> 664.80]  And a lot of times, those are models are like some of the models I used right in the beginning.
[664.94 --> 667.24]  I still have not beaten their benchmark.
[667.24 --> 671.78]  You know, so that's the way I see if you want to get into AI, deep learning,
[672.00 --> 673.80]  just use pre-existing models first.
[674.18 --> 677.72]  And then once you cross that threshold, you have a really, you know, you can go through AI Academy.
[677.92 --> 682.36]  And then Intel's AI Academy, once you go through that, you can get funding.
[682.56 --> 684.56]  I mean, you're already an AI expert by then.
[685.44 --> 686.56]  Yeah, I agree.
[686.80 --> 692.36]  And the new development in FPGA and in the neural network cores,
[692.36 --> 697.26]  including that core support inside the new CPUs, making it a lot different.
[697.48 --> 703.48]  You will be able to see a lot of neural network applications existing today on your smartphone.
[703.96 --> 705.88]  Android and iOS already support.
[706.00 --> 707.36]  The SDK is already in there.
[707.36 --> 712.06]  And you're actually training on a small set, of course, small data set.
[712.22 --> 714.42]  You're training on the CPU.
[714.58 --> 718.54]  You're doing inverse quickly without worrying about the CPU power.
[718.74 --> 725.14]  So probably $50, $60 Raspberry Pi-like product will help a lot.
[725.14 --> 727.02]  And there is a lot out there in the market.
[727.76 --> 729.78]  Intel Movidius is another good example.
[730.02 --> 734.00]  It's a neural computer stick that you can actually get for under $70.
[734.62 --> 738.74]  And using the resources on the AI Academy, Intel AI Academy,
[739.10 --> 743.30]  you can actually start with a pre-trained model, as you basically mentioned.
[743.48 --> 745.20]  But you still don't have to go GPU.
[745.60 --> 750.24]  GPU, unless you already figured out the model size and what you're doing,
[750.74 --> 752.70]  you're working on a larger scale of data.
[752.98 --> 754.22]  That's when you need GPU.
[754.22 --> 756.54]  So it's not really to start with.
[756.76 --> 759.76]  It's a very advanced stage with AI.
[760.18 --> 761.82]  I'd like to add a point there.
[761.92 --> 767.80]  So we specialize in distributing machine learning load for training.
[768.38 --> 769.98]  That's what we specialize in.
[770.46 --> 773.92]  And we're working with Intel team to show,
[774.02 --> 777.30]  actually we have benchmark data that it's already there,
[777.40 --> 780.86]  but I'm letting the cat out of the bag here a little bit prematurely.
[780.86 --> 789.64]  We're co-writing a paper with Intel that one can do training faster than GPU,
[790.26 --> 793.90]  cheaper than GPU for sure, just with a commodity CPU.
[794.40 --> 798.48]  That's RocketML, Intel combination paper is coming out.
[798.48 --> 803.78]  So far, you know, there is inferencing and there is training,
[804.16 --> 807.72]  where you consume a lot of the hardware compute resources.
[808.36 --> 812.12]  So far, CPUs outperform GPUs in the inference.
[812.90 --> 817.06]  But that wasn't the case in the training space.
[817.06 --> 823.92]  But the reason for that was that most of the software people use on top of the hardware is bloated.
[824.28 --> 827.32]  For example, Apache Spark is great software.
[827.72 --> 830.94]  For some other purpose, for training, it's a bloated software.
[831.18 --> 836.90]  It comes with a lot of barrier that's not required for machine learning training.
[836.90 --> 841.28]  So we have built a system that can overcome that barrier.
[841.62 --> 845.02]  And now we are hitting a benchmark below the GPU speeds.
[845.50 --> 847.30]  So it's much faster than GPU speeds.
[847.54 --> 850.66]  So that's an interesting thing that we found out.
[851.04 --> 852.88]  Awesome. Yeah, that's exciting to hear about.
[852.96 --> 854.52]  I'll look forward to seeing that paper.
[854.76 --> 855.00]  Thank you.
[855.06 --> 857.04]  Yeah, I appreciate all of your guys' perspective on that.
[857.10 --> 861.00]  I think that a lot of people see that as a barrier when it doesn't have to be.
[861.00 --> 868.76]  And I think I would emphasize as well that training isn't the only bit of the AI workflow in general, right?
[868.78 --> 877.32]  Even if you're thinking of training only, there's a lot to learn about the fundamentals, about pre-processing, about inference, like you said, Peter.
[877.68 --> 878.74]  So there's a lot you can learn.
[878.90 --> 881.16]  And we'll post some of those resources in the show notes.
[881.64 --> 881.92]  Okay.
[882.22 --> 883.98]  So this next one's kind of interesting.
[884.18 --> 885.18]  Hear your guys' perspective.
[885.18 --> 893.30]  This question is, why is there a sudden craze of programmers with little math background jumping onto machine learning,
[893.44 --> 896.96]  which requires a much different skill set than traditional programming?
[897.36 --> 898.04]  What do you guys think?
[898.28 --> 910.04]  I mean, SDK tools that we see out today made it a lot easier to consume and build and utilize training models
[910.04 --> 914.02]  compared to start doing everything on your own using Python, for example.
[914.02 --> 915.56]  I mean, this way, yeah.
[915.68 --> 921.88]  I mean, if there is a ready-to-use machine learning model tools that I can go to AWS, for example,
[922.46 --> 927.40]  and just pull it and immediately start using it and have prediction ready to go, yeah.
[927.52 --> 933.66]  You will see a lot of people without mathematical background trying to get into that, but you will face issues.
[933.76 --> 934.34]  You will fail.
[934.66 --> 936.28]  You'll need that mathematical background.
[936.62 --> 936.84]  Okay.
[936.98 --> 940.78]  So as a hacker, I basically build prototypes a lot.
[940.78 --> 946.60]  So that's one of the trends is that you follow where the entrepreneurs generally follow what the trend is.
[947.12 --> 950.50]  And the latest trend is basically, you know, blockchain and AI.
[950.94 --> 955.66]  Blockchain is still a really difficult program, but people get into it because there's one or two really good applications.
[955.94 --> 959.62]  Like Bitcoin is, you know, they see Bitcoin as one of the things that's going to change the world.
[959.86 --> 961.84]  All the programmers get into study blockchain.
[961.84 --> 963.48]  And they see self-driving car.
[963.58 --> 965.78]  They start seeing this as being deployed in the real world.
[965.90 --> 972.26]  They're like, okay, this is a time where you have emerging technology that's being applied in the real world now.
[972.62 --> 979.72]  And this is a time for me to invest my time to understand and to execute and to find opportunities within the space.
[980.04 --> 981.10]  It's happened back in mobile.
[981.24 --> 985.64]  When mobile started getting into people's hand, all of a sudden, all the programmers started jumping on mobile.
[985.64 --> 987.56]  Because I jumped in before that.
[987.88 --> 992.20]  And I remember just being one of the independent Android developers.
[992.60 --> 995.18]  I was invited to, you know, to give a talk at TED Global.
[995.38 --> 999.08]  That was, you know, really rare because, you know, people didn't get into it.
[999.14 --> 1005.64]  But as soon as that tipping point has been passed through, like we have current applications that are being deployed in the real world now.
[1005.94 --> 1007.74]  That's when the programmers all want to jump in.
[1007.80 --> 1009.24]  And this is where opportunity is.
[1009.24 --> 1010.46]  That's such a great point.
[1010.58 --> 1019.70]  Because if you think about it, you know, if they started from square one when they found out what was hot on the market right now, like blockchain or AI, they would never catch up.
[1019.82 --> 1026.52]  The ideas or where they think the application would be would be two years out by the time they caught up in calculus, right?
[1026.86 --> 1029.74]  And then understanding derivatives or, you know, that's messy.
[1029.90 --> 1032.26]  So what they do is, you're right, they go in and advance.
[1032.34 --> 1034.48]  They say, hey, I'm just going to, and then I'll backtrack.
[1034.60 --> 1037.90]  And then I'll try to figure out that actual knowledge down the road.
[1037.90 --> 1040.14]  And to Ali's point, you know, that can be dangerous.
[1040.60 --> 1040.96]  Absolutely.
[1041.48 --> 1043.40]  So I think I would caution those.
[1043.52 --> 1047.66]  Don't not innovate and don't not jump into it.
[1047.92 --> 1048.32]  Absolutely.
[1048.70 --> 1056.82]  Because I will say something that will spawn the rest of your minds here much better than anything I could come up with on my own, regardless of what my mathematical history is.
[1057.08 --> 1057.24]  Right.
[1057.36 --> 1059.16]  And I think that's what we need to spawn is innovation.
[1059.16 --> 1059.70]  But be careful.
[1059.84 --> 1060.94]  I totally agree with that.
[1060.98 --> 1061.90]  They're following a trend.
[1062.48 --> 1066.06]  Yeah, I think there's definitely a balance to be had there.
[1066.06 --> 1074.26]  I think, you know, we've had guests previously on the show that don't have a math background, but are still, you know, innovating in a really great way in AI.
[1074.90 --> 1080.52]  And so I think that, yeah, I would love to encourage people to get in the field, get their hands dirty.
[1080.52 --> 1083.20]  Like Peter said, get some pre-trained models, try out some things.
[1083.20 --> 1087.20]  This is a new layer in the software stack that people can experiment with.
[1087.50 --> 1096.12]  But then, you know, once you start getting into it more, you're going to naturally be drawn into these ideas around the theory behind neural networks and other things.
[1096.62 --> 1098.84]  And, you know, you don't have to have a math.
[1098.92 --> 1099.50]  I don't know.
[1099.62 --> 1102.62]  Do any of you guys have a math PhD or something like this?
[1102.88 --> 1103.86]  Far from it.
[1103.86 --> 1104.76]  Yeah, yeah.
[1105.00 --> 1109.06]  So I definitely don't.
[1109.20 --> 1114.50]  And so I think the math is important, like you guys have said, and people will get into it.
[1114.56 --> 1120.94]  But you don't have to feel like if you don't have a math PhD, then you can't get into AI and start innovating.
[1121.14 --> 1125.70]  One quick point I want to make is also a question you have to ask yourself as a developer.
[1126.10 --> 1128.70]  When the software stack do you see yourself, right?
[1128.82 --> 1131.34]  You know, the machine learning software stack is pretty complex and deep.
[1131.34 --> 1135.60]  You can look at the analogy of, say, an assembly language developer or a Java developer.
[1135.80 --> 1137.28]  Like where in that start do you want to be?
[1137.36 --> 1138.94]  Do you want to be writing drivers?
[1139.14 --> 1140.84]  Do you want to be writing assembly language programming?
[1141.32 --> 1144.78]  Because very soon, AI is really going to be a box, essentially.
[1144.96 --> 1146.78]  You're just going to be talking to APIs, right?
[1146.86 --> 1151.86]  So do you want to be writing applications for this box or you want to actually build the box, right?
[1152.00 --> 1152.14]  Yeah.
[1152.26 --> 1154.58]  So that's one question the developer has to answer himself.
[1154.90 --> 1155.22]  Great point.
[1155.24 --> 1155.92]  That is so true.
[1155.92 --> 1156.66]  Very good point.
[1157.18 --> 1157.66]  Awesome.
[1157.66 --> 1161.46]  So this next one is probably somewhat controversial.
[1161.98 --> 1168.04]  So I talked actually to Wojcik Zaremba yesterday about general intelligence.
[1168.36 --> 1172.30]  What is your guys' take on how intelligent is AI now?
[1172.54 --> 1174.84]  So the question is, how intelligent is AI now?
[1174.90 --> 1178.40]  This was in July, but now we're a little bit later.
[1178.56 --> 1179.96]  So maybe it's more intelligent now.
[1180.12 --> 1181.28]  But what do you guys think?
[1181.48 --> 1181.98]  Very dumb.
[1181.98 --> 1191.70]  So AI right now, because everything is called AI now because of the buzz I explained earlier.
[1192.04 --> 1194.74]  But right now it mostly consists of inferencing.
[1195.00 --> 1196.30]  That's what I consider deep learning.
[1196.56 --> 1199.22]  That's what spawned the entire industry.
[1199.74 --> 1204.52]  It becomes a sensor rather than intelligence itself, right?
[1204.56 --> 1207.56]  Because a computer doesn't know what a cat is before 2012.
[1207.94 --> 1210.92]  And the whole point that right now computers are this is a cat and this is a dog.
[1210.92 --> 1213.80]  That's what intelligence and this is all it can do.
[1214.18 --> 1221.26]  But, you know, with all the other programming of human intelligence that we have combined with, you know, what's so-called deep learning artificial intelligence.
[1221.34 --> 1224.28]  This is where the creating the real intelligence is.
[1224.70 --> 1227.06]  And that can go into some danger field, right?
[1227.06 --> 1240.28]  Like if you think about not just what how it can benefit a human being, but what technology can do, it gets into very, very dark sides of humans as well as, you know, dark sides of the machine itself.
[1240.74 --> 1245.10]  For example, you know, you can easily target people using droplet bombs.
[1245.10 --> 1247.02]  That's just that's just something.
[1247.02 --> 1253.96]  So as we develop the AI, I think this is a thing we have to consider is that right now it is everything is dictated by human intelligence.
[1254.18 --> 1260.28]  So we have to decide whether we want to, like, build something that can just drop bomb because they see it's human.
[1260.36 --> 1267.58]  Because at the end of the day, if you train that model just detecting humans, you have to figure you have to have, you know, you have to have something to back in.
[1267.68 --> 1269.42]  So you cannot use this to drop bombs.
[1269.42 --> 1270.86]  Can I summarize your answer?
[1271.02 --> 1274.34]  The answer is yes and no good and bad, smart and not so smart.
[1274.82 --> 1274.98]  Right.
[1275.10 --> 1291.70]  And as an example, if I apply AI in a retail architecture and I want to do RFID tracking to push advertisement or just to track foot traffic generally in a store or motion tracking for, you know, for my AC, I'm saving power.
[1291.78 --> 1292.56]  Simple things like that.
[1292.60 --> 1292.72]  Right.
[1293.08 --> 1294.06]  AI is super smart.
[1294.30 --> 1295.32]  AI is brilliant.
[1295.72 --> 1297.34]  And I see an ROI immediately.
[1297.34 --> 1303.26]  But if you take it to a more complex model, like what you're saying, where it can get really scary, you think about simple things like an autonomous vehicle.
[1303.36 --> 1304.78]  Everybody talks about autonomous vehicles.
[1305.26 --> 1310.14]  But let's say I'm in a car and let's say I'm in an autonomous vehicle that tracks vitals now because it's self-driving.
[1310.42 --> 1311.36]  Maybe it's tracking vitals.
[1311.66 --> 1312.62]  Maybe I have a heart attack.
[1312.94 --> 1314.18]  Maybe the car needs to pull over.
[1314.50 --> 1318.38]  Does the car understand, which we just taught it, what a road is?
[1318.66 --> 1321.68]  Does the car even understand the density of the gravel on the side of the road?
[1321.68 --> 1326.98]  How far to pull over, how to look over your shoulder and see how much traffic you're going to cause by pulling over here versus 10 feet ahead?
[1327.34 --> 1328.16]  It's that consciousness.
[1328.56 --> 1330.54]  And so it requires so much more.
[1331.02 --> 1333.18]  And so in that instance, it's not very smart.
[1333.56 --> 1333.88]  Not yet.
[1334.16 --> 1342.64]  Instead, I would argue that it's not autonomous at all in vehicles, but rather automated, programmed, based on a set of parameters, not autonomous at all.
[1342.90 --> 1343.82]  And I don't think we're there yet.
[1343.82 --> 1346.22]  There are two ways to think about it.
[1346.40 --> 1350.00]  One is a very simple statement is easy is hard.
[1350.24 --> 1351.12]  Hard is easy.
[1351.32 --> 1353.64]  What is hard for humans is easy for machines.
[1354.18 --> 1364.22]  Like if you want to ask someone, a data scientist or, you know, whatever, take Larry Page also and say that, hey, what does the recommendation engine look like?
[1364.54 --> 1366.18]  He won't be able to answer that question.
[1366.32 --> 1370.14]  But whereas machine learning can do that much better than humans.
[1370.14 --> 1377.72]  On the other hand, what's easy for humans, that is, you know, cat is a cat or whatever it is, that's a lot easier for humans.
[1377.86 --> 1379.36]  But for machines, it's harder.
[1379.84 --> 1381.16]  But it's getting better and better.
[1381.76 --> 1388.26]  Andrew Ng, one of the key guys in the AI segment, we almost worship him.
[1388.72 --> 1395.16]  He says that anything, I can't remember, I think he said one second for humans to do an inferencing.
[1395.16 --> 1398.96]  This is a badge or whatever, this is a human being or this is a mic.
[1399.66 --> 1402.38]  If it takes one second, machine can do it at the moment.
[1402.62 --> 1407.14]  But I think that that threshold is increasing very rapidly.
[1407.72 --> 1411.42]  We increase the compute capacity, data quality.
[1411.88 --> 1415.12]  And, of course, there is algorithms, the math behind it.
[1415.14 --> 1423.78]  As people invent more new math ways of representing the real world, it's all getting faster rapidly at an exponential rate.
[1423.78 --> 1427.38]  And I think there is some threat because of that.
[1427.48 --> 1431.66]  And also, at the same time, you could solve significant problems.
[1432.30 --> 1439.68]  For example, in cardiology or in radiology, medical spaces, you can literally make a huge difference to the human beings.
[1440.02 --> 1440.20]  Awesome.
[1440.34 --> 1440.48]  Yeah.
[1440.54 --> 1441.74]  Thanks for your perspective on that.
[1442.08 --> 1445.34]  So this one probably builds on that one.
[1445.52 --> 1448.38]  And maybe this is a point of confusion for a lot of people.
[1448.38 --> 1453.62]  So the question is, is a neural network actually a good model of how the brain works?
[1454.32 --> 1455.54]  So we...
[1455.54 --> 1465.54]  I mean, if you look at a perceptron as an example, I mean, the way your brain actually gets signal from sensor in your fingers and the way you react to it.
[1465.94 --> 1472.58]  Just building that same model in a neural network, it may look easy and it may work for a lot of application.
[1472.58 --> 1476.72]  As we said, we can actually have machine learning as models.
[1477.14 --> 1487.54]  But putting these models together, the sensors together, to actually make an intelligence decision based on all these, I don't think this is how the brain works.
[1487.70 --> 1496.72]  I mean, the way you may sometimes think about a smell or you hear a music, it reminds you of something.
[1497.32 --> 1499.28]  You don't actually know how that worked.
[1499.28 --> 1502.08]  You don't have any idea how it worked with the machine.
[1502.52 --> 1503.80]  The consciousness is not there.
[1503.96 --> 1509.20]  You don't expect it to be able to do that or come up with new ideas on its own.
[1509.34 --> 1509.94]  It's hard.
[1511.32 --> 1512.82]  I would just add on that.
[1513.22 --> 1527.02]  I think there is a symbiotic relationship between neuroscience and neural machine, neural network, people who are trying to hack, biohack, you know, what they think, the way the brain works into machines.
[1527.02 --> 1537.08]  I've heard neuroscientists say that, you know, by reading the papers of mathematicians writing about neural network, they learn a lot about the brain.
[1537.40 --> 1541.32]  So there's still a large area of how the brain works.
[1541.56 --> 1548.32]  We don't understand, even though neuroscience is improving quite a bit.
[1548.32 --> 1554.36]  So this is an interesting, definitely a very intriguing area to keep an eye on.
[1554.36 --> 1555.94]  So I just want to add something.
[1556.08 --> 1559.66]  It's like I think the neural network is just one part of the brain, right?
[1559.86 --> 1561.54]  As a part of the brain, we have a lot of things.
[1561.62 --> 1567.02]  We have memory, which computer have, you know, built a hard drive that's specifically just simulating our memory.
[1567.42 --> 1569.96]  And neural network is basically just classification, object detection.
[1570.18 --> 1571.24]  And that is part of that.
[1571.24 --> 1582.62]  And as we do more computer science and more AI in the future, we're going to uncover different parts of the brain that's, you know, some of them is going to react to smell that currently is hardwired.
[1583.12 --> 1584.88]  But is human hardwired?
[1585.00 --> 1585.54]  Is that learned?
[1585.88 --> 1590.32]  These are things that we're going to come, like, is going to be very interesting in the next few years.
[1590.32 --> 1596.30]  So kind of building on what we were talking about, about what a neural network is, I'll jump into this next question.
[1596.50 --> 1601.18]  The question is, in a neural network, each neuron is a hidden layer.
[1601.60 --> 1604.56]  In a hidden layer is said to focus on a certain feature.
[1604.74 --> 1606.54]  Take an eye, for an example.
[1606.96 --> 1610.18]  But how does it deduce that an eye is an eye?
[1610.36 --> 1618.48]  Or since it can contain a combination of things like an eyebrow and, you know, other parts of the face and the pupil and all of those things.
[1618.48 --> 1622.08]  So any one of you guys want to take a stab at describing that?
[1622.42 --> 1626.32]  I think it depends on how much data we provide the machines.
[1626.94 --> 1632.84]  You know, with enough data, a machine is able to parse out those similarities.
[1633.44 --> 1637.00]  Everything that machine does is just trying to match a pattern.
[1637.72 --> 1642.22]  And every layer helps match one little pattern at a time.
[1642.22 --> 1648.82]  And so that's how the neural nets, deep neural net, keep adding layers and layers.
[1649.30 --> 1655.40]  And each layer has a quite interesting set of information that you can make use of for some other purpose, too.
[1655.62 --> 1658.08]  Yeah, so maybe a follow-up on that.
[1658.16 --> 1660.78]  I mean, there's a lot of talk about deep neural networks now.
[1660.78 --> 1667.14]  Is the purpose of all of these hidden layers in the deep neural networks to detect these more complex patterns?
[1667.34 --> 1671.52]  Or why have the deep neural networks kind of advanced so far?
[1672.06 --> 1677.54]  It's basically like in your brain, the way your brain have a receptor field.
[1677.80 --> 1683.46]  Like when you think about the way your brain reacts to caffeine, for example, or to nicotine.
[1683.60 --> 1689.46]  I mean, it binds with certain perceptron and neurons in your brain to actually feel that.
[1689.46 --> 1691.18]  And now the same thing.
[1691.36 --> 1694.38]  I mean, with these layers, you got a lot of filtering.
[1695.00 --> 1697.56]  You got a lot of control that happening in there.
[1697.86 --> 1701.38]  And part of that is basically having multiple receptor fields.
[1701.58 --> 1706.52]  So you're actually going faster because if the receptor field doesn't match, you're skipping.
[1706.78 --> 1711.06]  You're actually not going in that neural network, completely going through it.
[1711.44 --> 1716.96]  And remember, you're doing that thousands and thousands and thousands of times during the training level.
[1716.96 --> 1722.22]  So basically, adding the receptor fields in there, it changed the way we see it.
[1722.30 --> 1723.78]  It changed the way we control it.
[1724.28 --> 1734.22]  But it's still, it's the way neural network will work is going to go more about distribution than just as a single node network that work together.
[1734.30 --> 1737.42]  You're going to have multiple nodes making decisions together.
[1737.54 --> 1739.56]  That's just what makes sense, basically.
[1739.56 --> 1746.42]  I mean, distributing the decision making instead of deciding on one type of neurons, for example.
[1746.64 --> 1749.88]  With certain sigmoid control, you're going to have multiple.
[1750.24 --> 1754.38]  Based on the decision of the first one, which one to trigger, which one to attack.
[1754.62 --> 1756.02]  That's how the eye works, actually.
[1756.28 --> 1762.54]  There is multiple layers of filtration that happen and sensitivity that change with the lights around you.
[1762.54 --> 1764.36]  So we're far away from that.
[1764.52 --> 1767.18]  But cameras will have these technologies slowly.
[1767.36 --> 1771.04]  As we understand more, we'll build more into the neural network.
[1771.56 --> 1775.34]  You know, there's that constant debate if machine learning is actually science or arts.
[1775.80 --> 1782.62]  You know, so I think it's really hard for a data scientist or a non-machine learning expert to kind of figure out what layer should I put where?
[1782.76 --> 1785.22]  How many neurons should a single layer have, right?
[1785.22 --> 1792.64]  But I think efforts like AutoML are actually trying to solve that problem so you can install AutoML or Search 2 and you're ready to go.
[1792.82 --> 1793.58]  But time will tell.
[1793.78 --> 1798.46]  Really see how far we get close to getting accurate models based on Search 2.
[1798.74 --> 1802.52]  Yeah, and just describe AutoML a little bit because people might not be familiar.
[1803.18 --> 1805.44]  I think Wes was going to say something about it.
[1806.22 --> 1810.80]  I was actually just going to say these questions are so presumptuous, right?
[1810.80 --> 1815.84]  Again, they're human questions about a non-human platform and they're presumptuous, right?
[1816.04 --> 1816.58]  Peter, right?
[1816.68 --> 1822.90]  You mentioned about, you know, how neurons or Ali perceptrons and how those impact the whole model, right?
[1823.14 --> 1827.20]  And now we're only focusing on maybe two elements of our brain, storage, right?
[1827.44 --> 1829.24]  And potentially some reasoning, right?
[1829.30 --> 1830.18]  Yeah, some decision making.
[1830.58 --> 1840.12]  But the fact is maybe AI will evolve even past that to where it will define that maybe our brain isn't connected the way it's most optimal in a compute environment.
[1840.12 --> 1841.82]  And so the questions are presumptuous.
[1841.92 --> 1844.78]  So when you answer some of these questions, we have to answer based on unknowns.
[1845.18 --> 1850.06]  It's the easiest analogy I like to use is when you say, oh, that planet can't support life.
[1850.24 --> 1855.16]  Who are you to define what life is and what another life form requires to exist, right?
[1855.20 --> 1857.14]  How would you even perceive to know that, right?
[1857.34 --> 1865.16]  And so some of these questions, they have to be open-ended and you have to keep your mind open to what is a much larger picture than what we can even think can exist.
[1865.56 --> 1869.42]  I'm glad that we've covered the full gamut between neural networks and aliens.
[1869.42 --> 1871.32]  So I'm happy that we made it there.
[1871.34 --> 1871.98]  I did that for you.
[1873.20 --> 1880.42]  So, yeah, just briefly before we go on, I'll circle back to Dave and let him mention what AutoML is so people can...
[1881.00 --> 1889.80]  Yeah, so typically when you train a machine learning model, you're tuning a bunch of parameters or hyperparameters, like, you know, batch size, learning rate, iteration, and whatnot.
[1889.80 --> 1897.20]  So AutoML lets you sort of tune those knobs here and there and then gives you, like, a way to accelerate the process, essentially.
[1897.66 --> 1900.54]  The other tool is like AutoML, but that's one of my favorites.
[1901.00 --> 1901.26]  Awesome.
[1901.64 --> 1901.76]  Yeah.
[1901.76 --> 1906.50]  Just to add on that, you know, great models are built through iterations.
[1906.82 --> 1913.30]  Iterations are very tedious and taxing for data scientists to do it.
[1913.84 --> 1918.86]  AutoML reduces that extra effort quite a bit.
[1919.40 --> 1920.76]  It's a machine learning on machine learning.
[1921.32 --> 1921.84]  Yeah.
[1922.10 --> 1922.94]  Makes sense.
[1923.22 --> 1926.74]  And we'll put some links in the show notes, of course, to some of those resources.
[1926.74 --> 1940.32]  So, the next question, if deep learning is the future, which maybe everyone says it is, what is the need for machine learning methods like SVM, decision trees, Bayesian methods, Markov chains, et cetera?
[1940.78 --> 1944.50]  I mean, each accelerate in a different field.
[1944.74 --> 1952.34]  I mean, deep learning will not work for a lot of mathematical equations that we deal with in the network field today.
[1952.34 --> 1958.52]  Because the data type, the way it behaves, it changes with a lot of factors that is not fitted in a table.
[1958.68 --> 1961.62]  I cannot just fit it in a table and have parameters define it.
[1961.62 --> 1974.50]  So, there is a lot of fields in AI where deep learning may be good to actually predict a model based on tree size, information that you can fit easily in tables.
[1974.50 --> 1983.48]  And also, like pictures, if you look at pictures, it will take in pictures and actually turning that into a model that's basically looking at the pixels inside.
[1983.58 --> 1984.40]  It's the same idea.
[1984.86 --> 1993.50]  So, yeah, the other machine learning models still exist, and it's actually a lot faster in performance and in behavior, especially supervised behavior.
[1994.50 --> 1999.16]  When you control that, deep learning doesn't have all of that built into it.
[1999.28 --> 2003.40]  But, again, it accelerates into pattern recognition a lot, a lot faster.
[2003.40 --> 2005.54]  Yeah, not everything is a nail.
[2005.76 --> 2007.22]  You need a hammer for a nail.
[2007.34 --> 2010.02]  But if you have a screw, you need a screwdriver.
[2010.70 --> 2015.96]  All methods have value and a good fit in different areas.
[2016.48 --> 2020.86]  Deep learning turns out to be quite versatile, but it has its own weaknesses, too.
[2021.50 --> 2027.10]  Yeah, on that note, for people kind of getting into the field, they probably hear a lot about deep learning.
[2027.10 --> 2030.68]  But there are so many methods to learn about.
[2031.06 --> 2035.06]  What would you guys recommend as far as a person getting into the field?
[2035.52 --> 2039.34]  What sorts of things might they want to learn about before deep learning?
[2039.52 --> 2045.64]  And how quickly should they kind of make that leap to learning about these deep neural networks?
[2045.64 --> 2050.52]  I mean, you start with machine learning basics before you go to deep learning.
[2050.84 --> 2051.84]  What is machine learning?
[2051.96 --> 2053.20]  What are you trying to achieve?
[2053.26 --> 2057.74]  And you understand, basically, how you're taking parameters, what training means.
[2058.20 --> 2060.56]  You actually get familiar with the framework.
[2060.70 --> 2063.78]  So there's a lot of frameworks you will get introduced to.
[2064.14 --> 2067.64]  Each of them got a powerful side that you can use in certain systems.
[2067.64 --> 2068.36]  systems.
[2068.84 --> 2072.56]  Yet, before all of this, in my opinion, distributed systems.
[2072.78 --> 2078.22]  You need to be able to, you know, run around, know your way around as a distributed system engineer.
[2078.50 --> 2080.28]  Because AI need a lot of that.
[2080.38 --> 2082.58]  You're going to have models sitting in the cloud.
[2082.68 --> 2085.16]  You're going to have inverse happening on the edge.
[2085.24 --> 2088.74]  You're going to have training maybe happening on the edge in some cases.
[2089.14 --> 2095.54]  So to get into this, I would recommend somebody just first, just this is how I got into it.
[2095.54 --> 2098.12]  Just basically first figure out what is a cat and what is a dog.
[2098.44 --> 2100.18]  I'm sure all of us have went through that.
[2100.56 --> 2105.12]  Once you go through that, you know, because it's the goal that's pushing you to keep learning, right?
[2105.20 --> 2108.34]  First, first, like, okay, how do I determine elephant from dog and cat?
[2108.72 --> 2110.78]  And from there, I was like, okay, I need photos of elephant.
[2110.96 --> 2112.92]  So I have to basically Google a bunch of photos of elephant.
[2113.32 --> 2116.36]  It was like, okay, from there, I basically said, okay, what framework to use?
[2116.72 --> 2117.98]  And I actually select a framework.
[2118.14 --> 2119.42]  I select a couple of them.
[2119.50 --> 2120.46]  I'm not going to say which one.
[2120.46 --> 2123.42]  I basically choose the easiest route that I was able to train my model.
[2123.42 --> 2129.90]  And this is a limitation of a person's imagination is what will keep their curiosity going.
[2130.30 --> 2133.40]  We'll keep them Googling for, like, you know, a stack overflow for information.
[2133.74 --> 2136.88]  And when they get stuck, and then each step, you learn a little more.
[2137.08 --> 2140.40]  And eventually, pretty much how your own way would work.
[2140.56 --> 2143.74]  That's a good way for learning, getting into deep learning.
[2144.22 --> 2145.30]  That's a very good advice.
[2145.48 --> 2148.42]  I agree with him that, you know, it's a complex topic.
[2148.42 --> 2150.36]  The next topic is math involved.
[2150.48 --> 2153.06]  There is domain knowledge involved.
[2153.22 --> 2158.10]  And there is ability to define a good problem is very critical, too.
[2158.36 --> 2161.76]  And then you have the tools, like TensorFlow one day, PyTorch the other day.
[2162.04 --> 2162.54]  There is so much.
[2162.70 --> 2167.74]  I would agree with Peter in saying that just get in there.
[2168.14 --> 2169.32]  Start with a simple problem.
[2169.76 --> 2175.18]  You don't have to worry about defining a problem when you're trying to make the machine identify cat versus dog.
[2175.18 --> 2181.60]  So you kind of minimize the buttons you have to push and start small.
[2182.24 --> 2193.44]  And as you gain confidence and curiosity kicks in and your goals change and you learn new methods, new complicated approaches, that's the best way to do it.
[2193.68 --> 2196.76]  The other quick thing I want to add is it also depends on how deep you want to go.
[2196.92 --> 2200.80]  So if you're in academia, then you probably want to do statistics and probability.
[2200.80 --> 2205.94]  Or if you're not, if you're in the industry, you probably want to build prototypes as fast as possible.
[2206.06 --> 2209.22]  Then you want to use frameworks like TensorFlow, Keras especially.
[2209.36 --> 2210.08]  It's one of my favorites.
[2210.64 --> 2211.58]  It's very easy to go.
[2211.76 --> 2212.62]  Four lines of code.
[2212.80 --> 2214.08]  You have your model trained.
[2214.62 --> 2215.84]  And then it's doing inferencing.
[2216.02 --> 2220.84]  So it really depends on the user, the developer, where you see yourself being in that machine learning stack.
[2221.26 --> 2221.62]  Awesome.
[2221.74 --> 2221.90]  Yeah.
[2222.00 --> 2226.42]  One of the things that we've emphasized before is kind of in line with what you guys are saying.
[2226.70 --> 2229.08]  Find a problem that you're passionate about.
[2229.08 --> 2233.36]  Find some data that you're interested in and just try to start answering those questions.
[2233.36 --> 2238.06]  And that will lead you to the right frameworks and the right methods and the right things to learn about.
[2238.22 --> 2239.02]  It's a great point.
[2239.12 --> 2240.54]  Like just start where you want to start.
[2240.76 --> 2241.54]  Find interest in it.
[2241.54 --> 2248.34]  Because if you're trying to do static tasks A, B, and C to get to the end result, I think you're following a set of steps.
[2248.40 --> 2250.42]  I think you have to have a passion about what it is.
[2250.44 --> 2251.26]  What do you want to solve for?
[2251.50 --> 2252.12]  What do you want to do?
[2252.16 --> 2254.72]  And then the excitement and the motivation behind that pushes you further.
[2254.72 --> 2259.66]  But I think, yeah, as soon as if you're just trying to give someone a guideline, do this, do that, do this, do that.
[2259.92 --> 2260.50]  That's boring.
[2260.84 --> 2263.52]  That sends me back to school when you just had to get your homework done.
[2263.64 --> 2264.46]  That's not fun.
[2264.72 --> 2264.86]  Right.
[2264.86 --> 2267.02]  But I think everybody at this table is super excited about what we do.
[2267.12 --> 2268.18]  And we follow our own paths.
[2268.22 --> 2269.32]  That's why we're all doing different things.
[2269.60 --> 2269.86]  Right.
[2270.04 --> 2270.20]  So.
[2270.60 --> 2270.84]  Awesome.
[2270.84 --> 2273.92]  So I don't know if all of you guys primarily work in Python.
[2274.38 --> 2278.74]  I think we could extend this next question to whatever language you guys work in.
[2279.04 --> 2286.70]  But apparently the internet wants to know what is the coolest thing that you've done with Python slash whatever language you're interested in.
[2286.70 --> 2292.90]  So maybe if you guys just want to highlight one of the cool things that you've done to give a little bit of inspiration to the audience.
[2293.40 --> 2296.38]  So my kind of project is just going back again to what excites me.
[2296.62 --> 2297.22]  It's FPGA.
[2297.40 --> 2299.06]  So field, programmable, gitarrays.
[2299.06 --> 2303.18]  So FPGs are pretty low level and they don't really operate at a level of Python.
[2303.42 --> 2305.72]  But as you know, the frameworks operate at a level of Python.
[2305.90 --> 2310.38]  So what I typically would do is create wrappers around the FPGA low level APIs.
[2310.82 --> 2310.94]  Right.
[2311.04 --> 2318.88]  So I would work with CC++ and then create wrappers for Python so you can easily plug in the device to such frameworks.
[2319.52 --> 2319.56]  Awesome.
[2319.76 --> 2323.66]  Are any of those kind of wrappers and that tooling, is that available to the public?
[2324.00 --> 2325.02]  Typically, no.
[2325.32 --> 2325.58]  Okay.
[2325.58 --> 2328.46]  Because those are very low level driver API stuff.
[2328.46 --> 2329.02]  Right.
[2329.12 --> 2329.48]  Exactly.
[2329.82 --> 2333.56]  I don't even think the users would be interested in knowing what goes on at that level.
[2333.72 --> 2333.96]  Right.
[2334.14 --> 2335.86]  So Python is the way to go, I would say.
[2336.14 --> 2336.42]  Awesome.
[2336.54 --> 2336.70]  Yeah.
[2336.78 --> 2341.26]  And is any of that stuff that you've done public to where people could take a look?
[2341.58 --> 2342.62]  Cruelly, they're not public.
[2342.98 --> 2343.12]  Yeah.
[2343.70 --> 2344.00]  Awesome.
[2344.74 --> 2348.54]  I know that Intel, for example, is putting out a lot around FPGAs.
[2348.60 --> 2348.76]  Right.
[2348.76 --> 2351.42]  Are there resources out there or webinars or anything?
[2351.42 --> 2356.44]  So yes, Intel has done quite a lot in terms of enabling FPGAs for data scientists and machine
[2356.44 --> 2356.74]  learning.
[2356.74 --> 2359.78]  There's actually a tool called CBSDK.
[2359.98 --> 2362.24]  It was recently released not too long ago.
[2362.44 --> 2367.36]  So CBSDK would allow you to take your trained model and run it through what is called a model
[2367.36 --> 2368.04]  optimizer.
[2368.04 --> 2369.56]  It's actually a Python script.
[2369.88 --> 2374.32]  And then from that, you would get an intermediate representative, which you can then use to
[2374.32 --> 2377.96]  port against pretty much any hardware that Intel makes today.
[2378.38 --> 2381.18]  You know, more videos, FPGAs, CPUs.
[2381.60 --> 2383.52]  So OpenVINO, used to be OpenVINO.
[2383.78 --> 2384.90]  Is it OpenCBSDK?
[2385.04 --> 2385.94]  It's the same thing.
[2386.38 --> 2387.78]  It's integrated together.
[2387.86 --> 2388.14]  Right.
[2388.22 --> 2388.44]  Right.
[2388.44 --> 2390.38]  So CBSDK is what it's mostly called today.
[2390.52 --> 2393.96]  That's the tool that you can use if you're using Intel's hardware.
[2394.22 --> 2395.18]  It's pretty easy to use.
[2395.26 --> 2396.08]  It's Python-based.
[2396.86 --> 2397.30]  Awesome.
[2397.48 --> 2398.24]  Yeah, I appreciate that.
[2398.34 --> 2400.48]  I definitely want to dive in more myself on that.
[2400.60 --> 2400.70]  Yeah.
[2400.76 --> 2406.00]  And the most exciting thing, I mean, FPGA is a very exciting thing for me right now.
[2406.36 --> 2413.00]  But I believe Python control of SDR and FPGA together, that's what's going to change
[2413.00 --> 2414.88]  the way we push AI to the edge.
[2414.88 --> 2420.50]  Because imagine, I mean, you don't have the limit of a certain technology that already
[2420.50 --> 2421.64]  sit on this device.
[2422.12 --> 2427.74]  Just because the technology changed in a few weeks or we found a silicon-level issue with
[2427.74 --> 2431.24]  the design itself, since FPGA, it's easy to rearrange.
[2431.58 --> 2437.08]  It's just a firmware that you can actually push, make it easier and make it a lot easier
[2437.08 --> 2437.58]  to control.
[2437.76 --> 2441.58]  SDR also, pushing SDR, which is software-defined radio, basically.
[2441.58 --> 2448.82]  That's going to make 5G technology, LTE technology, and IoT technologies without being stuck in
[2448.82 --> 2449.24]  a limit.
[2449.62 --> 2455.90]  And imagine if you actually let the machine decide the control of the waves and the control
[2455.90 --> 2461.72]  of which band to actually use to make sure like a swarm of drones, for example, stay always
[2461.72 --> 2462.18]  connected.
[2462.50 --> 2464.38]  So AI is going to get pushed to that.
[2464.38 --> 2471.24]  And I believe FPGA, I mean, as an industry, we've been in the network industry for a while.
[2471.94 --> 2477.40]  It started with FPGA, especially on the network side, because it's easier than building a complete
[2477.40 --> 2477.88]  ASIC.
[2478.00 --> 2479.02]  Go to the market.
[2479.38 --> 2485.36]  But with FPGA pricing going extremely down in the last five, six years, until introduction
[2485.36 --> 2490.66]  of a new type of FPGAs that actually built for intermediate devices.
[2490.66 --> 2493.80]  It's not just basic input and output features.
[2493.92 --> 2497.62]  You have more cores from the technology that's available to you.
[2497.82 --> 2503.96]  I believe for me, seeing Python being able to actually utilize to control SDR and FPGA,
[2504.08 --> 2506.70]  and we did some research on that on the edge of the network.
[2506.84 --> 2508.04]  It's extremely amazing.
[2508.26 --> 2511.50]  It can push AI capabilities a lot more to the edge.
[2511.82 --> 2517.50]  And use more sensors capabilities, utilizing that FPGA and sensor fusion.
[2517.50 --> 2518.84]  You don't need a lot of sensors.
[2519.30 --> 2524.92]  You can use less channels by fusing your data together and having like, we refer to it as
[2524.92 --> 2530.72]  the edge of the network, which is, we refer to it as Mac today, multi-access edge compute.
[2530.90 --> 2532.82]  But we also believe there's another layer.
[2533.02 --> 2534.98]  So it's not everything going to be in the cloud.
[2535.24 --> 2540.30]  It's in the edge, but also furthermore on the device itself, there will be some decision
[2540.30 --> 2543.86]  making happening there to eliminate the amount of bandwidth we use.
[2543.86 --> 2548.86]  Otherwise, these all connected devices will send so much data, no matter what technology
[2548.86 --> 2550.82]  we have, it's not going to be enough to process it.
[2551.06 --> 2551.32]  Awesome.
[2551.74 --> 2556.52]  Well, any other thoughts around interesting things you've done with Python or other languages
[2556.52 --> 2557.36]  that you want to highlight?
[2557.62 --> 2562.78]  We work at the infrastructure level, just bare metal up, silicon up level.
[2562.94 --> 2569.34]  So we kind of try to be hardware agnostic, be it CPUs or FPGAs, whatever it is.
[2569.34 --> 2573.62]  So we work at C++ level, not so much on the Python.
[2573.62 --> 2573.76]  Sure.
[2574.42 --> 2574.60]  Yeah.
[2574.70 --> 2577.90]  Well, what have you been doing recently at the C++ layer?
[2578.06 --> 2584.88]  And also maybe I'd love to hear you speak towards the role of C and C++ in ML and AI.
[2585.04 --> 2591.74]  A lot of people see Python as kind of the only player, but I think that's kind of a facade
[2591.74 --> 2592.74]  in some ways.
[2592.84 --> 2594.06]  So maybe you could speak to that.
[2594.06 --> 2598.46]  At the infrastructure level, you need compiler language like C++.
[2599.18 --> 2606.76]  And then at the user level, we put a wrapper and allow people to use our product with Python
[2606.76 --> 2607.74]  interface.
[2608.34 --> 2611.34]  The Jupyter notebook, they can call our libraries and make use of it.
[2611.58 --> 2613.72]  So all languages have value there.
[2613.88 --> 2618.00]  But I think a lot of the models will get built in Python only.
[2618.00 --> 2620.14]  That's the fact.
[2620.62 --> 2627.16]  But when it comes to distributing to consume compute, you need something else underneath.
[2627.60 --> 2627.70]  Gotcha.
[2628.10 --> 2634.82]  So kind of on that note, maybe the last thing that we can end with is there's a lot of people
[2634.82 --> 2639.18]  kind of getting into, like you said, training with Python.
[2639.18 --> 2644.26]  And maybe they're hitting some blockers as they're trying to scale things or they're trying
[2644.26 --> 2650.08]  to build up an AI team and maybe not knowing how to productionize models and that sort of
[2650.08 --> 2650.34]  thing.
[2650.54 --> 2655.12]  What general recommendations would you guys have around kind of the team that you build
[2655.12 --> 2660.48]  up around that you're trying to put together to build AI models and kind of some of the
[2660.48 --> 2664.88]  tooling that you might need to consider, the methodologies that you might need to consider
[2664.88 --> 2667.00]  as you're actually trying to scale AI?
[2667.00 --> 2672.38]  I would add by saying it depends on if you want to be a machine learning developer or
[2672.38 --> 2674.24]  an infrastructure engineer, right?
[2674.32 --> 2677.26]  Or you want to be both, which is great because I'm sort of somewhere in between.
[2677.52 --> 2678.84]  A little bit of this, a little bit of that.
[2679.36 --> 2684.74]  Tools that I would recommend are Dockers, maybe Kubernetes to then manage Docker containers that
[2684.74 --> 2687.32]  are running these ML models across multiple nodes.
[2687.74 --> 2690.86]  But again, like I said, it really depends on what you really want to do.
[2690.86 --> 2690.90]  Yeah.
[2691.30 --> 2695.94]  On that note, do you think like as far as teams that people are trying to build up, maybe
[2695.94 --> 2698.40]  you're trying to start an AI effort in your company?
[2698.94 --> 2703.08]  Do you need to kind of have both of these components or do you think there's people out there that
[2703.08 --> 2705.70]  can fulfill both of the roles themselves?
[2706.12 --> 2706.56]  Right.
[2706.76 --> 2710.10]  So it turns out they're actually really nice DevOps tools you could use.
[2710.20 --> 2715.24]  I would say maybe just a team of one person should be able to manage the infrastructure that
[2715.24 --> 2716.58]  runs these ML models.
[2716.58 --> 2722.78]  And really you can deploy Docker containers and Kubernetes, Mesos, for example, to kind
[2722.78 --> 2723.88]  of manage these models.
[2724.22 --> 2726.42]  It's a different thing if you're running it at scale.
[2726.66 --> 2730.22]  Then you may need a large engineering team to kind of make sure that business is running
[2730.22 --> 2731.84]  up and going.
[2732.22 --> 2732.30]  Yeah.
[2732.54 --> 2739.48]  The most time consuming part about building an AI, great AI product isn't necessarily the
[2739.48 --> 2740.32]  deployment piece.
[2740.32 --> 2746.04]  It's thinking right about the domain, about the problem you're trying to solve, especially
[2746.04 --> 2748.58]  if the team is being built in a bigger company.
[2749.02 --> 2754.52]  The problem definition itself requires a lot of multiple levels of agreements and consensus.
[2755.24 --> 2756.96]  That is a challenging thing.
[2757.08 --> 2760.44]  So you need people who can build consensus.
[2760.74 --> 2762.96]  You need people who can do critical thinking.
[2762.96 --> 2768.24]  And then you need great data scientists who can translate those problem statements into
[2768.24 --> 2769.40]  some kind of a model.
[2769.52 --> 2769.68]  Okay.
[2770.02 --> 2773.26]  It's a classification problem or a clustering problem, whatever.
[2773.68 --> 2779.40]  Somebody who is familiar with that kind of semantics to be able to translate that and
[2779.40 --> 2781.76]  hack together an experiment, put out a prototype.
[2782.24 --> 2785.12]  You should be able to get to a prototype really fast.
[2785.32 --> 2786.50]  That should be the goal.
[2786.94 --> 2789.72]  And that requires a multidisciplinary team.
[2790.04 --> 2791.08]  I think that's a good point.
[2791.08 --> 2793.44]  I like to say you need translators.
[2793.82 --> 2796.98]  You need people because the folks that are doing the dirty work and getting their hands
[2796.98 --> 2800.20]  dirty and the programmers and developers, those aren't the people with the cash a lot
[2800.20 --> 2800.60]  of times.
[2800.80 --> 2802.32]  And those aren't the people making the business decisions.
[2802.84 --> 2807.14]  And so you kind of need someone in between that's savvy enough to get the idea, be able
[2807.14 --> 2810.54]  to communicate with those that are really putting the rubbers on the road, but also
[2810.54 --> 2812.96]  communicate what the why is, right, Vinay?
[2813.16 --> 2814.96]  What the end result is going to be.
[2815.14 --> 2817.68]  And even bigger, what's the ROI?
[2817.92 --> 2818.60]  What's the return on it?
[2818.92 --> 2820.26]  How many sales am I going to get?
[2820.26 --> 2823.36]  I mean, you almost have to dumb it down and it's almost insulting.
[2823.56 --> 2827.12]  That's why, you know, you hear that the joking tagline, don't let the engineer make the
[2827.12 --> 2828.10]  product, right?
[2828.12 --> 2829.16]  Because you'll keep fixing it.
[2829.20 --> 2830.22]  You'll keep getting better and better.
[2830.26 --> 2833.98]  And that doesn't scale for enterprises or for a product to go to market, right?
[2834.12 --> 2837.74]  And so while we constantly want to do better things and we can never deliver something
[2837.74 --> 2839.68]  because it's never done, it will always be better.
[2840.16 --> 2841.36]  I think you got to have that buffer.
[2841.64 --> 2845.44]  Someone in the middle that can translate from the tech to the business side.
[2845.44 --> 2849.08]  Because if you don't have that, there's a huge gap between the business guy and the people
[2849.08 --> 2851.50]  that like folks at the same level, like you guys that are actually doing it, right?
[2851.90 --> 2852.26]  Awesome.
[2852.76 --> 2857.34]  Well, just to kind of end things here, I want to thank you guys for taking time out of the
[2857.34 --> 2857.68]  conference.
[2857.80 --> 2859.36]  I know there's a lot of great talks going on.
[2859.42 --> 2861.36]  So thank you guys for taking time to talk.
[2861.42 --> 2862.70]  It was really some great perspective.
[2862.70 --> 2868.00]  And thank you to Intel AI for helping arrange a range of this panel.
[2868.34 --> 2869.10]  I really appreciate it.
[2869.18 --> 2870.46]  And thank you guys so much.
[2870.90 --> 2871.46]  Thanks for having us.
[2871.46 --> 2871.70]  Thank you, Daniel.
[2871.76 --> 2872.48]  Thank you for having us.
[2875.24 --> 2875.76]  All right.
[2875.80 --> 2878.44]  Thank you for tuning into this episode of Practical AI.
[2878.70 --> 2880.16]  If you enjoyed this show, do us a favor.
[2880.28 --> 2880.86]  Go on iTunes.
[2881.00 --> 2881.66]  Give us a rating.
[2881.98 --> 2883.80]  Go in your podcast app and favorite it.
[2883.88 --> 2886.62]  If you are on Twitter or a social network, share a link with a friend.
[2886.70 --> 2889.04]  Whatever you got to do, share the show with a friend if you enjoyed it.
[2889.34 --> 2892.02]  And bandwidth for ChangeLog is provided by Fastly.
[2892.14 --> 2893.56]  Learn more at Fastly.com.
[2893.66 --> 2896.96]  And we catch our errors before our users do here at ChangeLog because of Rollbar.
[2897.16 --> 2899.56]  Check them out at Rollbar.com slash ChangeLog.
[2899.56 --> 2902.38]  And we're hosted on Linode Cloud Servers.
[2902.66 --> 2904.36]  Head to Linode.com slash ChangeLog.
[2904.44 --> 2904.90]  Check them out.
[2904.98 --> 2905.82]  Support this show.
[2906.12 --> 2909.40]  This episode is hosted by Daniel Whitenack and Chris Benson.
[2909.88 --> 2911.32]  Editing is done by Tim Smith.
[2911.58 --> 2913.62]  The music is by Breakmaster Cylinder.
[2913.96 --> 2917.46]  And you can find more shows just like this at ChangeLog.com.
[2917.46 --> 2919.58]  When you go there, pop in your email address.
[2919.88 --> 2923.70]  Get our weekly email keeping you up to date with the news and podcasts for developers
[2923.70 --> 2925.90]  in your inbox every single week.
[2926.28 --> 2927.06]  Thanks for tuning in.
[2927.24 --> 2928.00]  We'll see you next week.
[2929.56 --> 2930.54]  We'll see you next week.
[2930.54 --> 2932.80]  Bye.
[2932.82 --> 2934.22]  Bye.
