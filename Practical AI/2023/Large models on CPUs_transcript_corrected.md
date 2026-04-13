[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.24 → 24.38] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.38 → 24.68] listen.
[24.94 → 26.78] Check them out at Fastly.com.
[26.78 → 32.02] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.04 → 36.08] Learn more at fly.io.
[43.30 → 46.42] Welcome to another episode of Practical AI.
[46.76 → 48.52] This is Daniel Whiten ack.
[48.62 → 52.02] I'm a data scientist building a tool called Prediction Guard.
[52.02 → 60.52] And I am not joined today by my co-host Chris, but I am joined by an amazing guest who is
[60.52 → 67.66] an expert in all things model optimization and efficiency and running on CPUs, which is super
[67.66 → 68.18] exciting.
[68.42 → 72.76] I've got Mark Kurtz, whose director of machine learning at Neural Magic.
[73.00 → 73.56] Welcome, Mark.
[74.36 → 74.98] Thank you, Daniel.
[75.06 → 75.80] Thanks for having me on.
[75.80 → 77.78] Yeah, yeah, of course.
[77.94 → 87.22] So let's maybe just start out with a kind of like state of model optimization right now.
[87.34 → 92.72] So first off, could you kind of describe like when you're talking about model optimization
[92.72 → 97.68] or that set of tooling, what do you mean by that?
[97.68 → 103.94] And like, how does that fit within maybe the things that a data scientist or an AI person
[103.94 → 104.78] would want to do?
[104.78 → 110.50] So whenever we're looking at model optimization, we usually focus on a few different techniques,
[110.50 → 115.66] but the ultimate goal is to make the overall model smaller and faster, right?
[115.72 → 120.68] Neural networks known to be very large models, especially compared to more traditional machine
[120.68 → 121.00] learning.
[121.58 → 127.60] And it turns out the size of those models is the important part in terms of exploring a
[127.60 → 132.28] large dimensionality of a space, but actually doesn't use all of those pathways at inference
[132.28 → 132.50] time.
[132.50 → 138.50] So what we specialize in is specifically pruning, where we're going to remove connections within
[138.50 → 143.80] that network, quantization, where we're going to reduce the precision of those connections
[143.80 → 144.28] of the network.
[144.28 → 149.52] So going from, you know, the typical FP32 down to Nt8, and then additionally distillation,
[149.64 → 156.38] where we're taking larger models and trying to teach a smaller model to mimic the capability
[156.38 → 159.00] and the functionality of that larger model.
[159.44 → 161.16] So it's kind of, you know, overall high level.
[161.50 → 164.06] And yeah, it's a very exciting space right now.
[164.18 → 168.70] It's kind of exponential in terms of the number of research papers that are constantly coming
[168.70 → 169.56] out on the topic.
[169.70 → 175.30] Everybody's very excited about sparsity specifically, mainly because you can turn these large models
[175.30 → 181.86] and get rid of up to 95, even 97% of the weights are actually useless in these.
[182.18 → 187.18] Obviously, you can use that for a lot of efficiencies around performance and energy.
[187.18 → 191.38] And that's specifically where we've been focusing in at Neural Magic and what I've been focusing
[191.38 → 192.08] in on my work.
[192.08 → 192.68] Awesome.
[192.98 → 197.16] Yeah, that's, I definitely have felt this problem.
[197.40 → 202.92] So I'm sort of asking this question maybe for others out there that maybe haven't felt this
[202.92 → 204.18] problem as much.
[204.36 → 209.58] Why is it important to like to make models smaller or make them more efficient?
[209.74 → 217.14] Like how does that fit within what enterprises or like even users running smaller applications?
[217.14 → 220.44] Like why is that important for people, I guess is the question.
[220.44 → 226.06] Generally, there's going to be two cases that we're looking at in terms of deployment.
[226.24 → 230.38] One would be an embedded space where we're running on the edge and trying to work there.
[230.54 → 235.98] So generally you want real-time latency and optimizing the accuracy as best as possible.
[236.08 → 239.72] So if you're using an object detection model, you want to make sure that, you know, for example,
[239.72 → 243.80] you're on a security camera trying to draw object detection and make sure that you know when
[243.80 → 249.20] a person walks in a frame and whether that's alarming or not versus a dog or something
[249.20 → 249.66] like that.
[249.66 → 256.74] So in general on that edge application, what you can do is use a larger model, remove a
[256.74 → 258.72] lot of the pieces from that larger model.
[258.72 → 263.08] So you can keep the accuracy of the larger model, but take up the space of the smaller
[263.08 → 263.34] model.
[263.34 → 269.46] So significant improvement in terms of accuracy on that edge device while still maintaining,
[269.46 → 274.28] you know, the constraints that were set for you in terms of memory and latency that you
[274.28 → 275.82] need to request back with.
[275.82 → 279.26] And then the second one would be on the server side.
[279.26 → 284.76] And that's generally where we're looking at, you know, more throughput based applications
[284.76 → 290.74] and potentially also latency if they're shipping the data up to some server to be processed either
[290.74 → 293.38] on NLP or computer vision.
[293.38 → 299.96] But overall there, what we're looking at is, especially whenever people get into larger
[299.96 → 306.90] deployments on ML and neural networks, the cost significantly shifts, not from training,
[306.90 → 308.12] but to deployment.
[308.12 → 315.04] So for a lot of larger enterprises that are actively deploying 80, 90% of their costs is
[315.04 → 317.14] purely in deployment on these machines.
[317.14 → 323.70] So what you can do is take the exact same model that you have, reduce again, the amount
[323.70 → 327.30] of compute that you need to run it so that one, it'll run faster.
[327.30 → 330.62] But two, ultimately what that means is that it's going to run significantly cheaper.
[330.62 → 331.18] Right.
[331.18 → 337.10] And we have a cost savings on the order of, you know, 10 X, 20 X, even larger if you're
[337.10 → 338.90] really trying to specialize and optimize.
[338.90 → 342.30] There can be a significant reduction once you're at that scale.
[342.30 → 347.06] I would say definitely if, you know, you don't have anything deployed yet, don't worry about
[347.06 → 347.94] optimizing the model.
[348.10 → 351.50] Worry about getting a use case that works and something that you can prove out.
[351.62 → 357.10] As soon as you go into deployment, model optimization is a great thing to start because it's essentially
[357.10 → 362.08] just free performance that's left on the table that can significantly affect your bottom line.
[362.84 → 368.22] We've mostly been talking about kind of like model size and optimizations.
[368.22 → 374.20] And I do want to get sort of down and get into the nerdy stuff around like how some of this works.
[374.20 → 383.14] But before we do that, I'm also curious about this element of deployment on GPUs versus CPUs.
[383.14 → 388.24] It seems like some of what's indicated, at least in like the tooling that you're building,
[388.24 → 395.78] is like the potential to take a large model, which might require a GPU at inference time
[395.78 → 402.34] and potentially run that on cheaper commodity hardware that only has a CPU, maybe doesn't
[402.34 → 403.04] have a GPU.
[403.30 → 405.66] Like what is the state of that now?
[405.66 → 409.04] And like how far can you push that?
[409.04 → 415.64] Or maybe also like how could people best think about that in terms of like when and when
[415.64 → 417.38] that might not be possible, I guess.
[418.22 → 422.88] As you said, we specialize almost entirely on CPU performance.
[423.58 → 430.96] And in that, actually our latest ML imprints results on Alpert have come out.
[430.96 → 438.00] So in that we show that we're running faster than T4s and A40s and things like that on this
[438.00 → 438.64] commodity CPU.
[438.84 → 443.20] So server-based CPUs, stuff that you have in your laptop, desktop, things like that.
[443.46 → 450.20] And it's very surprising that what's thought of as these little CPUs can outperform the GPU.
[450.74 → 454.98] And we see this generally across every domain that we've tackled.
[454.98 → 459.94] And that's been across image classification, object detection, segmentation.
[460.48 → 465.18] And now we're working in the NLP and NLG space and actively coming out with that.
[465.30 → 470.78] But overall, we're seeing the same use case where these models are over-parameterized.
[471.12 → 472.74] We can take away a lot of that compute.
[473.02 → 477.66] And what that means is that you can actually get the CPU and the GPU about equivalent in
[477.66 → 478.64] terms of compute throughput.
[478.64 → 485.48] Because with the sparsity and the dynamic setup of CPUs, we can run and skip all those zero
[485.48 → 486.94] multiplications, right?
[487.08 → 489.36] So significant reduction compute, they're about even.
[489.68 → 495.12] But then the CPU has a unique cache hierarchy, which means that we can reuse that cache more
[495.12 → 497.16] often than what you can get on a GPU.
[497.32 → 502.68] L1 and L2 being extremely quick, faster than GPUs main memory, and L3 being about equivalent.
[502.68 → 508.44] So overall, what we do on our performance optimization is skipped all to compute to get even and then
[508.44 → 514.50] use that cache hierarchy as efficiently as possible on the CPUs so we can get faster memory
[514.50 → 516.16] access than even you can get on a GPU.
[516.66 → 519.84] And we pay a little bit more by doing a little bit more compute by doing that.
[520.08 → 524.02] But overall, it works out that you can actually beat the GPUs and that setup with just pure
[524.02 → 524.46] software.
[525.32 → 531.02] I anticipate this is maybe a question that you sometimes get, but it's like you hear so much
[531.02 → 536.40] about the necessity of GPUs for running these large models.
[536.40 → 544.96] Do you find generally practitioners are just unaware of this possibility of running these
[544.96 → 547.74] large models on CPUs?
[547.86 → 552.72] And how has that been for you and those that you work with that are actually doing this
[552.72 → 554.92] amazing work and have these awesome tools?
[555.12 → 561.00] How has that been in terms of overcoming that barrier of perception that people have?
[561.02 → 567.12] It was a barrier that we hit, especially early on, a couple of years back where it took
[567.12 → 571.06] a lot of convincing to even get in the door to talk to anyone because they just didn't
[571.06 → 572.38] believe what we were saying.
[572.62 → 577.64] Now it's gotten to be quite a bit better, especially with the newer software that's been pushed out
[577.64 → 579.96] of the newer chipsets on CPUs.
[579.96 → 582.82] They're getting a little bit more even in terms of GPUs.
[582.82 → 587.66] So it's, you know, within a stone's throw to try and match GPUs.
[587.66 → 590.24] So people are a little bit more accepting of it.
[590.56 → 597.00] But yeah, whenever we show them the numbers, generally the first reaction is, well, let me
[597.00 → 600.14] try that on my hardware because you guys got to be doing something weird.
[600.26 → 601.54] Let me try to do that.
[601.60 → 602.54] Let me replicate that.
[602.54 → 607.02] And as soon as they do, then the next question is, okay, well, how do I do this to my model?
[607.36 → 613.06] And that's usually where the tricky part comes in is model optimization hasn't always been
[613.06 → 614.42] the easiest thing to do.
[614.72 → 618.48] It can take a lot of research to enable new architectures and things like that.
[618.76 → 622.74] But that's what we've been also specializing on at Neural Magic is making all the research
[622.74 → 628.08] that we're doing, being able to put that into open source and also building out a SaaS platform
[628.08 → 633.50] on top of it, so everyone can easily play with hyperparameters and get something that is
[633.50 → 634.06] consumable.
[634.48 → 638.90] But I would say that's probably been the biggest gap in terms of trying to get people off of
[638.90 → 644.72] GPUs onto CPUs is the model optimization that needs to take place first to be able to run
[644.72 → 645.90] faster than the GPUs.
[646.44 → 650.86] You talked a little bit about sparsity, which I want to dive into overtime.
[650.86 → 653.26] And I want to get to those tools and open source stuff.
[653.26 → 658.88] You mentioned these large models and people are probably used to hearing these numbers,
[659.40 → 666.56] 3 billion, 7 billion, 13 billion, however up from there these models have in terms of
[666.56 → 667.64] numbers of parameters.
[667.80 → 673.54] Could you describe a little bit what you mean when you say 90 to 95% of these connections
[673.54 → 681.88] or maybe less than that, but a high percentage in some models have no impact on the actual
[681.88 → 684.64] forward pass or inference in the model?
[684.74 → 687.10] Could you describe a little bit more by what you mean by that?
[687.62 → 688.16] Yeah, definitely.
[688.34 → 690.46] And I'll take two steps to doing that.
[690.60 → 694.78] One is just covering kind of the 90, 95% class, at least where we've been able to get to
[694.78 → 695.60] on those.
[695.68 → 699.32] And the second is looking specifically at large language models.
[699.48 → 703.44] So for the first one, whenever we're looking at getting rid of 95% of the weights, let's
[703.44 → 705.06] take ResNet50 as an example.
[705.50 → 706.98] This is our toy benchmark model.
[707.10 → 711.86] This is essentially what we prove out all of our technology on because it's a common feature
[711.86 → 714.26] in Alpert and for most performance tests.
[714.82 → 718.82] So what we can do coming in is looking at those convolutional layers.
[719.32 → 724.48] It has, I forget how many million parameters within it, but it's definitely not the 3 billion,
[724.58 → 726.94] 7 billion or up on top of that.
[727.30 → 729.48] But within that, we can actually zero out.
[729.60 → 733.30] So what we're doing is taking all, imagine taking all those parameters, dumping them into
[733.30 → 734.90] a giant array.
[735.18 → 738.62] And we're just going to zero out the ones that are not important.
[738.62 → 741.96] And figuring out the ones that are not important is part of the research.
[742.36 → 748.18] The easiest assumption is just saying that the weights that are the largest are the ones
[748.18 → 748.88] that you want to keep.
[749.24 → 751.50] So the ones that are furthest from zero are the ones that you want to keep.
[751.86 → 753.56] Generally, you can think of this in two ways.
[753.72 → 758.22] One is that as the model is training and being regularized, the weights that don't matter are
[758.22 → 758.96] going to move towards zero.
[758.96 → 763.74] And then the other thing is during that forwards pass, the weights that are higher magnitude
[763.74 → 766.74] have more an effect on the output, right?
[766.96 → 768.72] And everything else is going to be noise in between.
[769.26 → 774.66] So we're able to essentially get rid of just our, whenever I say get rid of, I mean, setting
[774.66 → 777.76] those parameters to zero within 95% of them.
[777.82 → 780.46] So you're left with 5% of your weights that are non-zero.
[780.84 → 786.14] And that's actually all that you need to preserve the accuracy on ImageNet for Reset
[786.14 → 791.98] 50, for example, and some quick kind of intuition in terms of how I've been able to think about
[791.98 → 793.88] this and why it works and things like that.
[794.22 → 800.88] You can see as we increase the size of our dimensionality in our optimization space, what
[800.88 → 804.94] we're doing is, and there are a few research papers out on it, that we're able to connect
[804.94 → 807.04] more of the local men, right?
[807.14 → 812.38] So the optimization process will slowly converge further and further down because more of the
[812.38 → 813.38] local men are connected.
[813.38 → 818.02] Generally though, there are only a few of those pathways that you actually need to connect
[818.02 → 818.68] those local men.
[819.04 → 822.90] So all that we're doing is we're following down that most optimized pathway and removing
[822.90 → 825.64] everything else around us in terms of that dimensionality.
[826.06 → 830.18] So it's kind of one of those things that as you're training, it's slowly selecting the
[830.18 → 832.34] weights that matter that gets you down to that local men.
[832.86 → 834.10] And there's very few.
[834.20 → 838.72] So the important part was that large dimensionality of the optimization space, but not every direction
[838.72 → 839.48] mattered, right?
[839.50 → 840.50] So then we can get rid of it.
[840.50 → 848.28] And then diving in on the LLM side and large language models, we actually have a recent
[848.28 → 854.90] paper that came out from one of our principal research scientists, Dan Alistair, called Sparse GPT.
[854.90 → 866.30] And that's where we're looking at taking OPT and Bloom models all the way up to 175 billion parameters and be able to optimize those and remove as many weights as possible.
[866.30 → 868.50] All in this case, in one shot.
[868.96 → 875.26] So just using the model without any retraining, we're able to get rid of around 60% of the weights without doing anything.
[875.26 → 880.56] And there's a new paper out of Cerebral, actually, that was looking at the LLM story.
[880.98 → 886.18] And they're able now to get to 80% sparsity on these LLMs with retraining.
[886.42 → 892.18] So that's kind of the research direction that we're headed down now is proving out how optimized we can make these models.
[892.80 → 896.94] Because there's also a lot of interesting stuff that happens with the large language models,
[896.94 → 901.88] specifically because it's generating one token at a time, very latency bound.
[902.10 → 905.78] And that means that it's a lot of memory access to load those weights.
[905.84 → 915.00] So if you can quantize those and then get rid of half of them, you're already at, you know, anywhere from a 4 to 6x speed up just on your inference times.
[915.12 → 920.56] And that's generally where we're focused and looking at currently to try and get those LLMs to run faster.
[920.86 → 926.00] The other thing to call out for those two is, you know, 7 billion parameters and 175 billion parameters.
[926.00 → 928.40] Those don't fit in a single GPU.
[928.90 → 932.66] So now you have, you know, clusters of GPUs to serve one model.
[933.02 → 940.98] And a lot of that compute is just completely wasted because all that it's going to is trying to maximize the memory on the GPUs.
[941.18 → 945.14] For CPUs, you can throw a few terabytes on there, and it works out fine.
[945.38 → 949.84] So that's the other thing to call out with the LLMs in terms of GPU versus CPU.
[956.00 → 963.02] This is fascinating, Mark.
[963.08 → 968.72] I want to follow up on what you were just talking about, which I think is a really, it's sort of a subtle point.
[968.72 → 979.50] But it's fascinating in that I think if I understood you right in what you're saying, like, let's say that I have one of these large models, 175 billion parameters or whatever.
[979.50 → 989.36] And even for inference, I have the necessity to have multiple GPUs just to load that model into the memory of the cards.
[989.72 → 994.38] Whereas on a CPU, you can have terabytes of memory.
[994.38 → 1001.46] What I'm assuming is like you could load that in as long as you're able to execute it quickly, which I guess is the other piece.
[1001.46 → 1002.40] So am I right?
[1002.46 → 1011.96] You sort of have to have both like the ability to load it into memory, and you have a bit more space in that on the CPU side.
[1011.96 → 1021.38] But then you also have to be able to execute it very quickly, which I guess is like why you would think about both space and sparsity.
[1021.56 → 1022.98] Is that an accurate way to put it?
[1022.98 → 1029.98] But as you said, you know, you have a total space you need to take up and then a minimum latency that you want to respond to the user at, right?
[1030.26 → 1032.14] And that's going to set the constraints for your hardware.
[1032.70 → 1038.48] And for CPUs currently, at least for the smaller models, you can get to a usable speed on those.
[1038.58 → 1045.76] If you've seen like llama.CPP, they're doing int4 and things like that on smaller models, and they're usable, but they're less accurate.
[1045.76 → 1054.76] So what we're trying to do and what we're actually working on right now is making sure we can get that GPU class speed while maintaining the large memory advantage of CPUs.
[1055.40 → 1062.78] So you can deploy this 175 billion parameter model on something local, and you don't have to worry about data privacy, anything like that.
[1062.98 → 1066.38] It's just there working and available and highly accurate for you.
[1066.38 → 1084.58] I definitely heard people that I've talked to who have like tried various optimization techniques and have maybe been dissatisfied with the performance hit that they're getting, not in terms of compute, but in terms of like actual model performance or accuracy or whatever.
[1084.58 → 1098.82] Does that performance hit often come about because of the quantization that's maybe part of the optimization techniques or are there multiple sources of that like performance hit?
[1098.90 → 1100.36] How should people think about that?
[1101.12 → 1109.76] I think the biggest thing there is honestly just the amount of choices that people have to apply and not knowing when to apply them.
[1109.76 → 1120.52] Because generally for quantization, for example, you can apply quantization to pretty much anything at end to eight for both activations and weights and have it recover.
[1120.88 → 1125.84] But there are definitely cases where, for example, we've been quantizing efficient.
[1125.98 → 1127.76] That's quite a bit on our image classification side.
[1128.08 → 1135.32] There's one or two layers in some of these that are extremely sensitive for whatever reason to quantization that you can't quantize those.
[1135.40 → 1138.58] So removing those, then you get 100% recovery, right?
[1138.58 → 1145.32] So it's a lot of this kind of little things that researchers know intuitively in terms of having used this constantly.
[1145.54 → 1146.36] What will work?
[1146.46 → 1146.90] What won't?
[1147.14 → 1150.12] But that's not really coded into software anywhere, right?
[1150.14 → 1151.42] To make it easy for people to use.
[1151.64 → 1155.68] So generally they'll go through, try and quantize, and there's no feedback loop.
[1155.76 → 1157.06] There's no methodology.
[1157.22 → 1162.30] It's just, hey, I was able to apply it in one shot, but it lost 5% accuracy.
[1162.64 → 1163.76] Talking about quantization.
[1163.76 → 1169.06] But if you do, you know, a quantization or a training scheme, generally you'll recover all of that back.
[1169.40 → 1171.54] And it generally works completely for that.
[1171.82 → 1172.72] Same thing on pruning.
[1173.00 → 1181.46] Pruning, you'll definitely see more of a drop, and it's much more of a requirement to do training aware on the pruning side, at least to get to really high sparsities.
[1181.46 → 1187.58] But you definitely will see this kind of the choices that are made in the hyperparameters that are chosen.
[1187.74 → 1190.68] Those can significantly affect the recovery and the quality.
[1191.12 → 1202.12] So generally I'd say, you know, if they were seeing drops in performance, it's primarily because of those choices and those issues and just the wide breadth that's available right now and not knowing how to narrow it down.
[1202.46 → 1204.52] And that's, you know, what we're actually working on.
[1204.70 → 1205.10] Does that make sense?
[1205.10 → 1209.28] Yeah, yeah, that's good for people to myself.
[1209.28 → 1218.74] I want to develop a little bit more intuition around these things because, like you say, sometimes you're just like, oh, here's the command that I run on the command line.
[1219.12 → 1223.08] And, like, I get this file out that is smaller, right?
[1223.14 → 1228.24] But I don't have a great intuition about, like, similar to hyperparameter tuning, right?
[1228.24 → 1237.02] Like, that takes time to figure out, like, okay, how should I think about changing my learning rate if this happens or if that happens, that sort of thing.
[1237.54 → 1249.78] You mentioned one thing which I think would also be good to kind of clarify and help people understand is, like, training aware optimization versus just non-training, I guess, optimization.
[1250.14 → 1252.90] Or I don't know what the counter to that is.
[1253.18 → 1255.70] Could you talk about those, like, how they're differentiated?
[1255.70 → 1263.80] Some people might guess what that means, but, like, how are they differentiated, and how does that work out in practice in terms of how you would optimize a model?
[1264.50 → 1267.70] Technically, we have three categories generally available.
[1268.18 → 1270.56] And the two you're going through is, one, training aware.
[1271.20 → 1274.44] And then we have post-training or one-shot, which are kind of interchangeable.
[1274.78 → 1281.62] And then we additionally have on sparse transfer, which is something that we've been pushing a lot because the research has worked out quite a bit for it.
[1281.92 → 1284.26] So I'll cover all three of those in a little bit more depth.
[1284.26 → 1294.92] So for training aware, what we're doing is taking the exact same model that you're wanting to deploy in the exact same data set it was trained on and continuing the training process further.
[1295.46 → 1298.96] So while we're continuing that training process, we could be continuing it.
[1299.06 → 1300.48] This is where the hyperparameters come in.
[1300.86 → 1305.22] But generally, it'll be about half the time that it originally took to train it.
[1305.50 → 1306.82] We'll train it for that much longer.
[1306.82 → 1313.26] And as we're doing that training, we're iteratively pruning away, or we're applying quantization or both.
[1313.80 → 1322.76] And the reason we're continuing that training is because as we're iteratively applying these optimizations, we're slowly moving the model away from its local min, right?
[1322.84 → 1324.58] And it has to adapt and adjust back.
[1324.94 → 1335.54] So by slowly doing that and training over some time, we allow small jumps that the optimizer can recover from and adjust the remaining weights for rather than doing it all at once.
[1335.54 → 1341.82] And the all at once piece is where we get into post-training in one shot, where we're not going to try and retrain the model at all.
[1341.88 → 1343.94] We're going to take a small calibration data set.
[1343.94 → 1357.44] And then we're going to use some heuristics or algorithms to figure out, using that calibration data set, how to optimize that model and remove weights or quantize.
[1357.56 → 1361.60] So the most common case would be static quantization.
[1361.78 → 1367.90] We're using a calibration data set to figure out the activation ranges for each layer, right?
[1367.90 → 1377.14] And once you have the activation ranges for each layer, you can set up a simple quantization scheme to say, given that it's going from this layer is going from negative six to six.
[1377.24 → 1383.14] Now I need to fit that range into an intake scale of zero to 255, right?
[1383.16 → 1384.28] And be able to map that in.
[1384.74 → 1388.36] So that would be a simple post-training or one-shot application.
[1388.36 → 1396.24] And then the final one is sparse transfer, which works exactly the same as transfer learning or fine-tuning.
[1396.56 → 1399.70] It's just we're starting with a sparse model to run through.
[1399.86 → 1412.08] And that's a lot of what we've pushed up in neural magic into our sparse zoo are these open source sparse models that we have, you know, sparse Beats and REST 50s and YOLO V5s, things like that.
[1412.08 → 1422.30] And you can just take those, plug in your data set and transfer over to it, so the sparsity mass stays in place, and it just adjusts the remaining weights to fit your data set.
[1422.54 → 1428.98] We have a few papers out on that as well that shows that sparse transfer works just as well as regular transfer.
[1429.30 → 1431.06] Yeah, that's fascinating.
[1431.48 → 1439.40] I guess this would somewhat depend on like if I'm just thinking of like the average practitioner out there, right?
[1439.40 → 1454.74] Like probably in a lot of the space that I work in, in like the larger language model area, then like I'm not going to be able to retrain one of these large models on the original data set, right?
[1454.76 → 1458.94] Or even half of that or for half of the epochs or whatever.
[1459.20 → 1462.66] But these other things are certainly things that I do all the time, right?
[1462.70 → 1464.46] Like fine-tuning, transfer learning.
[1464.46 → 1469.30] So it's cool to understand that there are options out there.
[1469.42 → 1478.90] Am I correct in assuming that like you mentioned the zoo, the sparse zoo that people can find on your website, and we'll link in here too,
[1479.36 → 1492.36] that like researchers, your team, practitioners, whoever are the people out there are also putting in work to actually release some of these sparse models publicly to the community
[1492.36 → 1496.12] so that I can take those and then maybe do fine-tune on that.
[1496.18 → 1500.16] Or maybe it's just good enough from what's released in the community.
[1500.32 → 1504.64] Could you tell us a little bit about that community and like what's being released?
[1505.12 → 1512.36] So on the open source side, pretty much everything that we have on the sparse zoo currently has either been from our lab.
[1512.36 → 1518.08] We have a few that are from Intel's lab up as well and some hugging face examples and things like that.
[1518.30 → 1527.14] Primarily because a lot of the scarification research is all built around a few models like Reset 50, BERT and things like that.
[1527.18 → 1530.48] And they don't expand it out past those models to prove out their algorithms.
[1530.64 → 1531.90] So we have the best of those.
[1532.12 → 1535.16] And then, yeah, that's exactly what our team is working on.
[1535.26 → 1541.18] And well, we get some community contributions in every once in a while for sparse models that people have generated or transferred.
[1541.18 → 1546.72] So our goal is to be able to push these up so that, as you said, anyone can come in from the community
[1546.72 → 1550.74] and be able to pull those down and get value out of those models.
[1550.92 → 1555.36] So you can think of them as sparse foundational models rather than the dense foundational models.
[1555.36 → 1574.60] Mark, in addition to the sparse zoo, which is really cool,
[1574.76 → 1581.88] I know that Neural Magic is producing some pretty interesting and useful tooling otherwise as well
[1581.88 → 1585.80] in terms of actually doing some of this optimization themselves.
[1586.42 → 1589.48] And I see certain things, deep sparse, sparse ML.
[1589.66 → 1598.18] Could you describe a little bit about if I'm a practitioner, I have a model and I want to do optimization.
[1598.18 → 1602.36] What does that look like for me right now with the tooling that's available?
[1603.20 → 1607.58] So we have sparse ML, which is our open source model optimization framework.
[1607.58 → 1610.92] It's built primarily on top of PyTorch.
[1611.02 → 1616.88] And then we have integrations with Torch Vision, Hugging Face, YOLO, Ultrasonics, YOLO v5,
[1617.30 → 1619.92] pretty much all the common repos that most people are using.
[1620.06 → 1625.40] We've already integrated with, so you can use our integrations and just plug in your model and go along with that.
[1625.52 → 1628.04] And then the other part is that we have recipes.
[1628.24 → 1629.66] And I'll go through recipes in a second.
[1630.04 → 1633.14] But we have this kind of pre-coded integrations, or you can create your own integration.
[1633.14 → 1635.12] Usually it only takes a few lines of code.
[1635.52 → 1640.48] We've done all the hard work in terms of making sure that whenever we want to optimize a model,
[1640.76 → 1643.12] that you just have to wrap the optimizer in PyTorch.
[1643.44 → 1647.02] Essentially wrap the model and the optimizer, which is what our code handles.
[1647.20 → 1649.56] And then it's going to go through and handle the optimization past that.
[1649.60 → 1655.20] So there's no coding really from your side or from the practitioner's side on implementation.
[1655.92 → 1661.14] And then the other part is then coming up with an optimization recipe that people want to use.
[1661.14 → 1666.16] And what that's going to lay out is saying that I want to prune from this epoch to this epoch, for example,
[1666.26 → 1671.50] and then apply quantization and target these layers and at this sparsity level, things like that.
[1671.80 → 1677.34] We have automated ways to generate those, as well as examples on the sparsity and in other places.
[1677.64 → 1680.76] That's generally what it would look like is, you know, get up and running.
[1680.86 → 1682.88] We definitely recommend checking out the sparsity first,
[1683.26 → 1686.94] seeing if there's anything that you can do to just transfer the model onto your dataset,
[1687.12 → 1689.30] because those are the quickest and fastest ways.
[1689.30 → 1693.22] And then otherwise, if you do have a specific model architecture that you're looking at,
[1693.48 → 1697.76] then you can start going down this integration pathway and generating your own recipes.
[1698.06 → 1699.76] And that's the current state that we're at.
[1699.94 → 1704.42] The other thing that I wanted to call out is that we're working on a SaaS platform right now
[1704.42 → 1706.08] to make all of this more intuitive.
[1706.08 → 1711.66] So you have a UI to be able to predict where that model is going to end up before you start optimizing it.
[1711.94 → 1716.12] And then additionally, actively benchmark it across your different deployment scenarios.
[1716.44 → 1717.56] So this is called Sparsity.
[1717.56 → 1717.68] Sparsity.
[1718.00 → 1722.04] We've had an old kind of alpha state for a while that was downloadable.
[1722.56 → 1725.80] And we're actually going through alpha testing right now.
[1725.94 → 1728.94] So anyone that is interested in trying that out, definitely reach out.
[1729.26 → 1733.60] We're going through alpha currently looking to go to beta in probably the next month, two months,
[1733.60 → 1735.98] and then GA following up after that.
[1736.12 → 1737.94] So definitely check that out as well.
[1738.28 → 1738.42] And yeah.
[1738.92 → 1739.88] Yeah, that's great.
[1739.88 → 1745.04] Yeah, I love how you're thinking towards usability as well around these things.
[1745.04 → 1753.58] Because I do see this as something that kind of blocks people on optimization a lot because they get stuck.
[1753.66 → 1756.74] Like you say, it's like, well, what recipe do I use here?
[1756.78 → 1758.26] It seems like there's a million options.
[1758.26 → 1759.94] Like, where do I start?
[1759.94 → 1762.12] So that's really awesome to hear.
[1762.32 → 1767.42] Just so people can understand, like, there are options available in the Spars Zoo.
[1767.54 → 1769.32] I'm kind of scrolling through there now.
[1769.40 → 1776.20] There's a lot, even ones that I know that I use, like Distillery, which is fine-tuned on squad.
[1776.20 → 1779.12] Like, I use that all the time for question-answer.
[1779.50 → 1786.44] And apparently I should use the Sparse one because, yeah, that would help out a lot, both in terms of compute and speed.
[1786.86 → 1788.86] Let's say that a model is not there.
[1789.10 → 1795.96] And in particular, like, people, of course, are interested in, like, all of these things being rapidly released all the time.
[1795.96 → 1807.12] So one of the things I know that I've seen in optimization platforms over time is, like, it's hard to maybe support new architectures as they come out.
[1807.26 → 1809.74] So how are you all approaching that?
[1809.82 → 1819.70] And, like, what is the state of, like, being able to be flexible with these optimization schemes for a variety of architectures?
[1819.70 → 1830.64] Looking at the base framework that we have pushed out in Sparse ML, for example, everything's implemented such that it's supposed to be able to run with any model architecture.
[1831.14 → 1839.82] So there's no real big assumptions on their other than you have convolutions, and you have linear layers inside your model somewhere that we can target for optimizations.
[1839.82 → 1850.86] So everything's set up very generically, which means that whenever there is a new architecture that comes out or new weights, things like that, it's going to take some time for, you know, us to tackle that.
[1850.92 → 1854.64] And that's if it gets onto the list of, you know, top used models, things like that.
[1854.98 → 1860.76] But that is the nice thing about having an open source community is that people are welcome to come in.
[1860.76 → 1864.54] The tooling and the framework there should work out of the box with everything.
[1864.54 → 1870.18] And they're more than welcome to be able to commit or push up, you know, whatever they're working on.
[1870.42 → 1875.80] And we have an active Slack community and GitHub community for people to come in.
[1875.90 → 1877.34] Our engineers are actively on that.
[1877.66 → 1882.04] They can come in, look at it, and easily get support on any issues they're running into.
[1882.60 → 1883.04] Awesome.
[1883.20 → 1883.36] Yeah.
[1883.42 → 1893.40] And we'll make sure for the listeners who are wanting to get plugged into this, we'll make sure and include the links to the Slack group and the GitHub in our show notes.
[1893.40 → 1899.38] So make sure you visit there and get plugged in and start optimizing your models.
[1899.76 → 1905.92] As we kind of get a little bit closer to the end here, I'm wondering about a couple of things.
[1905.92 → 1911.52] One is I know that, like you're saying, you're actively involved in research in this space.
[1911.52 → 1915.66] What trends are you seeing in research around optimization?
[1915.66 → 1925.34] And in particular, like, what are the directions that your team is sort of excited to go into in the near future in terms of the research side of this?
[1925.90 → 1929.24] So I would say there are two big trends right now.
[1929.24 → 1932.84] One is around the focus on post-training.
[1933.34 → 1945.26] Our principal research scientist, Dan Alistair, he came, him, along with his lab, came up with this algorithm called OBC-BBQ, which actually we have a webinar, which we'll have already aired by the time that this comes out.
[1945.44 → 1946.68] It's airing tomorrow.
[1946.68 → 1958.74] But that algorithm specifically is where a lot of effort's going around, which is requiring as little data as possible and no retraining and trying to increase sparsity as much as possible.
[1959.14 → 1963.86] So that's one of the key things that people are trending down is trying to do that.
[1964.24 → 1971.04] The second one, I would say, is a large push around quantization in terms of getting to lower bits.
[1971.04 → 1984.36] And that's something that's been around for a while, but it's something that's becoming more and more prevalent as we're looking at the larger models, mainly because their execution time is mainly dominated by trying to pull in these large matrices of weights.
[1984.58 → 1995.30] So there's been a big push there now around trying to get down to, you know, pass in a down to int4, int3, int2 quantization on these active representations.
[1995.58 → 1996.78] I'd say that's the other trend.
[1996.78 → 2004.76] The final kind of bonus trend that I'd throw in there, because I said too, the third one would be more research around sparse training.
[2005.36 → 2016.98] So specifically trying to figure out how to start with an unoptimized and untrained model and be able to make it sparse from the start and then keep sparsity throughout training.
[2016.98 → 2027.16] Because generally what we do to guarantee accuracy, we'll start from a dense converge model and then iteratively print on top of that, which adds training time.
[2027.54 → 2027.66] Right.
[2027.74 → 2037.36] So now there's a lot of research going into trying to figure out how quickly the model can be pruned and then be able to carry that over as training.
[2037.36 → 2039.92] So that's where the other big, big pieces.
[2040.20 → 2048.42] And all three of these are definitely active areas that we've been investing heavily in, especially looking at the generative AI space now going through that.
[2049.36 → 2049.50] Yeah.
[2049.66 → 2049.86] Yeah.
[2049.92 → 2056.74] I know it must be a crazy time for you all, just like it is a crazy time for everyone.
[2056.74 → 2060.64] But yeah, I think this is a really important piece of it.
[2060.70 → 2071.60] I know one of the trends we've even talked here on the show about, it seems like a lot of people are talking about like serverless deployments of machine learning, deep learning models.
[2071.90 → 2079.18] And I know a lot of the issues related to that and things that people are dealing with is cold start time and loading models into memory.
[2079.40 → 2084.06] I don't know if that's impacted you all at all, but it seems definitely relevant.
[2084.06 → 2089.16] Like if you're going to run your model serverless, you probably want it as small as possible, I would imagine.
[2089.76 → 2090.62] Yeah, absolutely.
[2090.96 → 2091.42] Absolutely.
[2092.28 → 2097.86] So you mentioned where people can find out about neural magic on Slack, on GitHub.
[2098.14 → 2100.24] I would really encourage people to do this.
[2100.38 → 2106.38] As we close out here, what are you kind of personally excited about during this?
[2107.12 → 2112.40] I mean, like I say, it's a crazy time for everyone right now with generative AI and the way things are trending.
[2112.40 → 2118.10] What's exciting to you right now about the AI community and certain things you're seeing?
[2118.30 → 2121.28] What do you see as kind of positive trends, I guess?
[2121.28 → 2129.36] The part that I'm most excited about is that generative AI space specifically in being able to augment humans.
[2129.74 → 2143.96] Obviously, there are a lot of privacy concerns and data concerns and bias issues and things like that in this, which I don't want to see, you know, LLMs deployed everywhere become a default response for like Google search or something like that.
[2143.96 → 2154.16] But it is really exciting to see, even in my day to day, starting to use these actively to augment what I'm doing around content generation and framing and things like that.
[2154.26 → 2156.88] So that's one piece that I'm really excited for.
[2156.88 → 2165.06] And with the work that we're doing on Neural Magic, we're especially looking at these because, one, we want to see that continue to grow to open source.
[2165.14 → 2173.64] And I think that's been the other push that's been huge and really exciting to see is that whenever GPT-4 came out, it was completely privatized.
[2173.74 → 2177.64] They put out, you know, a little white paper on it that had no details about it at all.
[2177.96 → 2180.24] A lot of data concerns and things like that within that.
[2180.24 → 2190.04] But the open source community has already released, I mean, I can name probably 10 models so far that have been released since then that are chat GPT-like or GPT-4-like.
[2190.36 → 2191.68] So it's really exciting to see that.
[2191.78 → 2197.74] I think the next stage from those open source models is going to be making them runnable anywhere, right?
[2197.76 → 2201.88] So you don't need this big GPU cluster farm to get something that is usable.
[2201.94 → 2203.88] And that's where we're really looking at going.
[2203.88 → 2213.56] We're actually working on the LLM deployment issue right now and hope to have something out in the next few weeks, the next few months that people can start actively using.
[2213.96 → 2214.58] Download it.
[2214.68 → 2219.08] They can run it anywhere they want on any CPU, and it'll be just as fast as GPUs.
[2219.62 → 2220.14] Cool.
[2220.36 → 2220.56] Yeah.
[2220.66 → 2221.88] Well, keep us posted.
[2222.06 → 2224.40] I know I'm personally interested in that one.
[2224.58 → 2225.32] So, yeah.
[2225.32 → 2227.32] Thank you so much for joining us, Mark.
[2227.42 → 2229.72] This is a really fun conversation.
[2229.72 → 2240.98] I love getting into the weeds of these practicalities because this is a topic where people get stuck a lot is on the deployment side and the optimization side.
[2241.50 → 2241.90] So, yeah.
[2241.96 → 2246.96] Thank you for all that you and your team are doing at Neural Magic in this area.
[2247.32 → 2249.10] And, yeah, keep up the good work.
[2249.20 → 2250.26] We're excited to see it.
[2250.48 → 2251.36] So thanks for joining.
[2252.14 → 2252.72] Thanks, Daniel.
[2252.92 → 2253.70] It's great talking with you.
[2253.70 → 2253.72] Thank you.
[2253.72 → 2253.94] Thank you.
[2253.94 → 2254.00] Thank you.
[2254.00 → 2254.02] Thank you.
[2254.02 → 2254.04] Thank you.
[2254.04 → 2254.10] Thank you.
[2254.10 → 2254.16] Thank you.
[2254.16 → 2254.18] Thank you.
[2254.18 → 2254.68] Thank you.
[2254.68 → 2255.18] Thank you.
[2255.18 → 2255.68] Thank you.
[2255.68 → 2255.74] Thank you.
[2255.74 → 2255.76] Thank you.
[2255.76 → 2255.78] Thank you.
[2255.78 → 2255.80] Thank you.
[2255.80 → 2255.84] Thank you.
[2255.84 → 2255.86] Thank you.
[2259.72 → 2264.88] Thank you for listening to Practical AI.
[2265.44 → 2269.20] Your next step is to subscribe now, if you haven't already.
[2269.64 → 2275.68] And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2276.16 → 2281.06] Thanks once again to Vastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2281.64 → 2285.44] Check out what they're up to at Fastly.com and Fly.io.
[2285.44 → 2291.16] And to our beat-freaking residents, Break master Cylinder, for continuously cranking out the best beats in the biz.
[2291.44 → 2292.34] That's all for now.
[2292.62 → 2293.76] We'll talk to you again next time.
