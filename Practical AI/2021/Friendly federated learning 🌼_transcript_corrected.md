[0.00 → 2.10] There are a ton of things that get me excited.
[2.54 → 9.08] From a practical perspective, one initiative that we are participating in is called MEDEF.
[9.22 → 14.58] The real-world impact and real-world improvements that we're going to see from this can be very profound
[14.58 → 21.18] because it's about medical AI and getting better performance estimates in medical AI is actually a very fundamental challenge.
[21.18 → 24.30] So that's something I'm quite keen on contributing to.
[24.30 → 30.30] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[30.66 → 32.72] We love Linde. They keep it fast and simple.
[32.86 → 35.22] Check them out at linode.com slash changelog.
[35.44 → 37.52] Our bandwidth is provided by Vastly.
[37.86 → 41.42] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[41.68 → 43.38] Get a demo at LaunchDarkly.com.
[43.90 → 47.26] This episode is brought to you by our friends at Rudder Stack.
[47.26 → 52.06] And we're calling all data engineers to check out Rudder Stack Cloud and start building smart customer data pipelines.
[52.06 → 55.40] Rudder Stack is warehouse first, no more silos.
[55.86 → 59.20] Rudder Stack builds your customer data lake on your data warehouse, not theirs,
[59.46 → 64.90] enabling all functionality of a CDP with more security and retaining full ownership of your data.
[65.20 → 67.66] It's open source and API first.
[67.98 → 71.42] Rudder Stack can be easily integrated into your existing development processes.
[71.98 → 74.74] And because they're open source, you can see all their code,
[74.96 → 77.38] so you don't have to worry about vendor lock-in or black boxes.
[77.58 → 79.50] And best of all, they have transparent pricing.
[79.70 → 81.92] Stop paying your CDP a premium to store your data.
[82.40 → 87.28] Rudder Stack is free up to 500,000 events and pricing scales transparently from there.
[87.72 → 89.74] Learn more and get started at RudderStack.com.
[90.06 → 92.28] Again, RudderStack.com.
[92.44 → 95.98] That's R-U-D-D-E-R-S-T-A-C-K.com.
[95.98 → 110.70] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[111.00 → 112.78] productive, and accessible to everyone.
[113.08 → 117.16] This is where conversations around AI, machine learning, and data science happen.
[117.42 → 120.92] Join the community and Slack with us around various topics of the show at
[120.92 → 122.24] change-on.com slash community.
[122.58 → 123.54] And follow us on Twitter.
[123.68 → 125.24] We're at Practical AI FM.
[131.48 → 134.50] Well, welcome to another episode of Practical AI.
[134.86 → 136.68] This is Daniel Whiten ack.
[136.80 → 139.80] I'm a data scientist with SIL International.
[140.18 → 142.88] And I'm joined, as always, by my co-host, Chris Benson,
[143.08 → 145.68] who is a tech strategist at Lockheed Martin.
[145.68 → 147.36] How was your Thanksgiving, Chris?
[147.66 → 148.70] It was U.S. Thanksgiving.
[149.02 → 152.46] For those listeners that aren't in the U.S., might not be aware.
[152.80 → 153.62] It was very good.
[153.86 → 154.92] Nice family stuff.
[155.18 → 156.68] Flew around the plane, things like that.
[156.80 → 159.32] And now we're into the holiday season.
[159.66 → 165.98] And, you know, looking forward to seeing what kind of machine learning gifts are under the tree this year.
[166.16 → 166.52] Yes.
[166.52 → 174.64] Well, in the spirit of distributing machine learning to all the boys and girls, maybe not by Santa,
[175.24 → 182.14] but a couple of weeks ago, you and I had a conversation about federated learning.
[182.66 → 188.38] Now, neither you nor I is an expert in that area or a practitioner in that area,
[188.46 → 190.30] although I think it was a good conversation.
[190.30 → 197.36] But today we're privileged to have Daniel Hotel with us, who is one of the creators of Flower,
[197.56 → 202.12] which is one of the open source federated learning frameworks that we talked about.
[202.38 → 207.46] He's a co-founder at ADAP and a visiting researcher at University of Cambridge.
[207.84 → 208.36] Welcome, Daniel.
[208.72 → 209.08] Thanks.
[209.18 → 209.92] Thanks for having me.
[210.26 → 210.60] Yeah.
[211.06 → 218.06] Well, as you heard, Chris and I were talking about federated learning without being experts in federated learning.
[218.06 → 223.24] So maybe to follow up on that conversation and maybe for people that didn't hear that conversation,
[223.80 → 229.52] could you just give us a sketch of what federated learning is?
[229.90 → 231.10] And then we can take it from there.
[231.56 → 232.18] Yeah, of course.
[232.38 → 233.00] I'm happy to.
[233.48 → 238.70] So federated learning is a way to train models across multiple data sets.
[238.94 → 241.28] That's the very easy take on it.
[241.50 → 244.06] So you might be wondering, how does this work?
[244.06 → 249.00] The way you do it in federated learning, and let's just start off by giving an example.
[249.48 → 253.64] Let's say we have, for example, a group of hospitals.
[253.98 → 261.20] They have some in-house data, but due to regulations, they cannot share this data, and they cannot put this data in the cloud.
[261.38 → 269.20] And they can't use the usual machine learning workflow where you basically collect all the data in a central repository and then train your model on it.
[269.20 → 271.38] So that's not an option for them.
[272.12 → 275.18] So they might be interested in using federated learning.
[275.58 → 279.96] And how would a federated learning setup then work in such a scenario?
[280.28 → 284.34] So the way it works is that you have your plain old machine learning model.
[284.54 → 289.64] Say it's a neural network, like, for example, a CNN that does some kind of image classification.
[289.64 → 293.48] Maybe you want to look at radiology images, for example.
[293.90 → 297.84] And you would initialize this model in a central place.
[298.06 → 299.64] Let's call this the central server.
[299.92 → 306.32] And the central server would, after initializing the model, send this model out to all the participating hospitals.
[306.72 → 308.92] So it would send the initialized model.
[309.02 → 312.56] But there are other variants of it, just to say this for the sake of completeness.
[312.56 → 319.70] But in our initial example, just to explain the very basic version of it, they would send out the initialized model.
[319.86 → 321.92] So a model that hasn't learned anything yet.
[322.14 → 328.98] The model would then be trained locally within each hospital on the data that is available locally.
[329.42 → 332.68] So each hospital obviously has a different data set.
[332.80 → 337.86] They would train the model not until convergence, but they would only train it for a little while.
[338.10 → 341.02] So let's say they would train it for one or two epochs.
[341.02 → 349.72] And after they trained the model for one or two epochs, they would send the updated model parameters or the gradients that they accumulated back to the central server.
[349.96 → 351.92] So that way, they don't have to share the data.
[352.00 → 353.88] The data stays where it originated.
[354.30 → 357.64] The data always stays within each participating hospital.
[358.06 → 361.32] And the central server would only get the refined model parameters.
[361.40 → 367.38] So the model parameters that have been trained for one or two epochs, it would get that from all the participating hospitals.
[367.38 → 372.02] And what the central server then does is it aggregates those parameters.
[372.32 → 375.90] In the simplest version, it just does a weighted average over these parameters.
[376.30 → 384.82] What I just described is a way of initializing the model, sending it out, training it locally, collecting the updated parameters, and then aggregating the parameters.
[385.10 → 387.72] That is one single round of federated learning.
[387.72 → 392.72] And then what you usually do is you perform these rounds over and over again until the model converges.
[393.68 → 401.94] And the interesting part about it is why organizations actually do this is they get access to a lot more data than they had before.
[402.18 → 410.22] So we've probably all had this experience, especially in practical AI projects, that oftentimes there is just not enough data.
[410.36 → 413.60] And having more data beats any fancy model architecture.
[413.60 → 417.24] So in this case, federated learning solves this data access problem.
[417.34 → 422.10] They can collaborate on the model training without having to share the underlying training data.
[422.40 → 423.48] Yeah, that's the gist of it.
[423.82 → 424.70] That's a good explanation.
[424.96 → 427.44] It was much better than the one we were trying a few weeks ago.
[428.10 → 433.34] Yeah, we should link this episode to that one because it took us half an hour to get there.
[433.74 → 437.16] We just need to voice over what he just said to what we said.
[437.28 → 437.86] Yeah, totally.
[438.24 → 438.44] Yeah.
[438.56 → 440.58] I mean, I left out a ton of detail, right?
[440.58 → 446.46] I get it, but we can ask you questions and find out what some of that is and looking forward to that.
[446.80 → 462.30] So as a starter, it's very clear given the data is distributed in terms of where it's located and given laws and regulations and other such things that may constrain the training process with privacy concerns and stuff.
[462.30 → 465.84] So it's very clear what the advantage is in federated learning.
[466.16 → 480.18] What also might be considered some disadvantages or maybe another way of asking it is when you do consolidate the model after you've done the federated learning and stuff, what is the delta in a trained model versus if you had not done that?
[480.18 → 487.96] If you had been able to aggregate kind of in the traditional way, all the data into one spot and train it in the traditional way we've done before federated learning.
[488.26 → 492.22] What's the difference in what you get as an output, you know, or is there much of one?
[492.48 → 493.72] Yeah, there is a difference.
[493.72 → 504.04] The biggest difference, I shall say, is obviously in convergence time because you have these rounds of communication and also the averaging process has some impact there.
[504.50 → 510.80] Often as researchers, we make these comparisons between centralized learning and federated aspects of it.
[511.18 → 520.24] The interesting bit is that this comparison is somewhat artificial because it's not something that one would face in reality very often.
[520.24 → 522.56] It's either federated learning or nothing.
[523.56 → 525.24] We've seen this in the past, right?
[525.44 → 537.78] If we look a little bit at the journey that machine learning and deep learning now took is somewhere around 2012, we realized that by making these models bigger, we suddenly get better accuracy.
[538.02 → 543.32] So there was this image net moment and then a couple of other moments like this afterwards.
[543.32 → 550.26] And we saw that we can achieve ever greater accuracy and then other performance metrics with these models.
[550.64 → 559.82] And the thing is, we always when we read a research paper, for example, and when we look at these recent advances, it's often quite fascinating.
[559.82 → 567.42] And it's often in the context of web scale companies like Google or Facebook, we have these massive amounts of data in house.
[567.42 → 573.40] But then often in practice, there's this realization that, OK, I read about this cool technique.
[573.54 → 575.36] I'm trying to apply it to my problem.
[575.36 → 579.26] And suddenly I don't get the amazing results that I expected to have.
[579.46 → 581.04] So the question is, what happened?
[581.04 → 590.28] And in many cases, the answer is really that the amount of data and the diversity that you have in your local data set is just not enough.
[590.28 → 602.38] And the interesting thing and the thing that got us very interested in federated learning was this realization that for many of those cases, you might not have a large data set on your own.
[602.68 → 610.24] But there are a lot of others just like you who are facing the same challenge and who might want to train the same model.
[610.24 → 614.50] But they also have some data, but not enough data for a very good model.
[614.50 → 623.38] I mean, we could obviously solve this if we could put all of this data in a just in a single destination, in a single cloud account and then trade a model on it.
[623.84 → 626.22] But that's something that just doesn't happen.
[626.32 → 628.64] It doesn't happen for regulatory reasons.
[628.80 → 631.72] It doesn't happen for confidentiality reasons.
[632.12 → 639.22] For example, corporations, they have a lot of financial data, and they might want to have models that predict certain aspects about these data.
[639.22 → 641.48] But again, it's a thing of confidentiality.
[642.36 → 643.94] It's something they would never share.
[643.94 → 654.10] And the types of use cases that federated learning gets used for, sometimes we are surprised ourselves where exactly these companies are hesitant to share data.
[654.42 → 661.56] For example, there was one case where a couple of manufacturing companies, they are all operating the same manufacturing machine.
[661.96 → 668.76] And they want to train a model that does predictive maintenance basically for this machine to predict whether this machine is likely going to fail.
[668.88 → 672.12] So whether they need to do some manual maintenance or something like that.
[672.12 → 681.46] And one would think that this is a case where they could just collaborate, and they could just put all of their machine sensory data in a cloud account and train a predictive maintenance model.
[681.66 → 682.50] No, they don't.
[682.54 → 684.76] Why don't they collaborate on this?
[685.02 → 698.96] Well, the reason is that the data that they have from running these machines could allow others to see how often they run these machines, which could allow others to draw some conclusions about how many parts they are producing, which is highly confidential.
[698.96 → 703.56] So even in those seemingly easy cases, in reality, it's not that easy.
[703.56 → 718.04] So that's almost a perfect lead-in for what I wanted to ask next is that federated learning, it sounds like, offers different business models from maybe some of the things we've done in the past or even among competitors directly cooperating.
[718.04 → 743.18] So have you seen this start to happen yet where maybe consortiums come into being, and they may include direct competitors who are all in the same line of business that want to protect their data so that they don't give away competitive intelligence and federated learning through a consortium or some other structure similar to that might be a way to everyone benefit from that and get the new model without giving away the secret sauce, so to speak.
[743.18 → 773.16] Do you expect to see more of that kind of thing?
[773.18 → 786.56] Really strong competitors, they get together because they see something else as a threat to their business model, and they see that this is a way to collaborate without sharing this, as you call it, the secret sauce.
[787.20 → 799.88] And the interesting bit is that the way I described federated learning in the beginning, this is really end-to-end federated learning where you initialize the model just globally, and then you train the model end-to-end with all participating parties.
[800.48 → 802.54] This is not the only model that's possible, right?
[802.54 → 810.94] I want to describe one which I think is quite interesting, especially for this case where you have sort of competing organizations collaborating.
[811.28 → 817.30] And it's one where you train a certain part of the model in a federated fashion across multiple data sets.
[817.62 → 821.96] And then other parts of the model, you just train it yourself on your local data.
[821.96 → 828.44] So this is pretty interesting because you can, in such a federation, you can, for example, train the entire backbone of a model.
[828.94 → 833.38] But then the last few layers, the head of the model, you don't train this in a federated fashion.
[833.76 → 838.02] You leave that up to each of the participating organizations to do it themselves.
[838.40 → 842.30] So everyone ends up with a similar yet different model.
[842.30 → 848.60] And everyone has something where they say, OK, we benefit from this federation, but we are not giving away everything.
[848.90 → 853.92] One important thing to mention, though, is that there are different types of federated learning.
[854.12 → 857.58] So you can roughly categorize it into two different types.
[857.90 → 863.88] One is this cross-silo type that we just talked about where different organizations collaborate with each other.
[863.88 → 874.34] The other type that we often see also in scientific literature is the cross-device setting, where you would usually, typically, you would have one organization.
[874.68 → 877.68] For example, think about Google or Apple, for example.
[877.98 → 885.90] And this organization would have access to many devices, for example, mobile devices like an Android phones or iOS phones.
[885.90 → 891.18] And the goal in this case is also to train a model, to train a model across all of these devices.
[891.18 → 896.36] And these devices, they hold data that is also where you wouldn't want to upload this data to the cloud.
[896.92 → 904.18] So this is the cross-device setting where a single organization trains these models without access to the underlying trading data.
[921.18 → 926.90] This episode is brought to you by me, myself, and AI.
[927.36 → 930.12] It's a podcast on artificial intelligence and business.
[930.28 → 934.56] And it's produced by our friends at MIT Sloan Management Review and Boston Consulting Group.
[934.86 → 939.02] The question is, why do only 10% of companies succeed with artificial intelligence?
[939.54 → 941.48] That's the question they aim to answer with this podcast.
[942.10 → 945.62] Here's Google Cloud's Will Grannies on an unusual AI challenge.
[945.62 → 950.08] When I think about what AI is, I find the algorithms mathematically fascinating.
[950.42 → 953.32] But I find the use of the algorithms far more fascinating.
[953.52 → 960.42] Because from a technical perspective, we're finding correlations in extremely high-dimensional nonlinear spaces.
[960.90 → 963.02] It's statistics at scale in some sense, right?
[963.02 → 965.50] We're finding these correlations between A and B.
[965.76 → 967.32] And those algorithms are fascinating.
[967.42 → 968.52] And I'm still teaching those now.
[968.54 → 969.04] And they're fun.
[969.44 → 973.70] But what's more interesting to me is what do those correlations mean for the people?
[973.70 → 979.22] All right, me, myself, and AI is a collaboration between MIT Sloan Management Review and Boston Consulting Group.
[979.52 → 980.94] It's available wherever you get your podcasts.
[981.08 → 983.40] Just search me, myself, and AI.
[1003.70 → 1018.10] So, Daniel, I think we've mostly talked about some of the kind of data-centric motivations for federated learning or maybe privacy-focused or whatever it is, competitive type of advantages.
[1018.74 → 1024.82] But I'm also thinking of, like, the devices on which the actual training is happening.
[1024.82 → 1039.02] So, like, if I'm thinking of the centralized model, I'm thinking of, like, oh, I'm going to spin up, like, a pod of GPUs, a really expensive pod of GPUs, and do, like, all my training there and get my data there somehow.
[1039.02 → 1054.02] So, am I correct that you could have some sort of infrastructure savings with this where the actual computation is happening on those edge devices, and you're doing a smaller amount of aggregation and updating of the model centrally?
[1054.82 → 1059.84] Could you talk to that a little bit and what people have seen and how they look at infrastructure in that way?
[1060.24 → 1062.02] Yes, that's a very interesting question.
[1062.24 → 1065.38] The answer is, as almost always in engineering, it depends.
[1065.38 → 1077.60] So, as you noted correctly, in the centralized setting, you have a pretty well-defined stack that there's not a lot that changes from one setup to another.
[1077.82 → 1084.92] You usually have some kind of x86 processor, and then you have a usually you have an NVIDIA GPU attached to that.
[1085.38 → 1086.84] You have Linux running on that machine.
[1087.22 → 1091.82] And then the biggest choice you have is whether to use TensorFlow or PyTorch or TAX nowadays.
[1092.16 → 1094.40] In the federated setting, that's quite different.
[1094.40 → 1101.48] In the federated setting, you can have anything as a client starting from even a tiny embedded device.
[1101.86 → 1103.70] There's research going on in that direction.
[1104.22 → 1111.44] Then you can have something like an Apple Watch or a mobile phone, or you can have some bigger device like a tablet or a laptop.
[1111.96 → 1118.50] You can have your standard x86 server that I just described, or you can even have a much larger compute cluster.
[1118.50 → 1128.20] If you're in the cross-silo setting where you have a ton of data and one of these organizations has massive in-house infrastructure, you can have an HPC cluster as a client.
[1128.20 → 1135.50] So this is obviously quite interesting and also challenging from an infrastructure and just a software perspective.
[1135.50 → 1146.48] In some cases, you can actually, and there is some recent research, for example, from a group in Cambridge that I'm involved with, about the CO2 impact of these workloads.
[1146.84 → 1155.52] Comparing, for example, the CO2 impact, and this is obviously quite related to your question about the CO2 impact of federated workloads versus central workloads.
[1155.52 → 1159.30] And the interesting bit is that it's not, you can't say it in general.
[1159.82 → 1170.02] Actually, it's quite an interesting thing because I originally expected federated learning to do much worse because you have these communication rounds, and it takes longer to converge.
[1170.42 → 1172.72] So obviously, it must have a higher CO2 impact.
[1172.90 → 1179.84] It turned out that that's not necessarily the case because in some situations, the reason is, once you hear it, it's quite obvious.
[1179.84 → 1188.20] But it was surprising to me, in the central setting, you have the major impact on the CO2 emissions is the cooling.
[1188.38 → 1191.20] So you have active cooling of your GPU clusters.
[1191.72 → 1195.06] In the federated setting, you don't necessarily have cooling.
[1195.20 → 1197.06] You have additional cost for communication.
[1197.60 → 1202.02] But then if you have a mobile edge device, these edge devices, they are usually passively cooled.
[1202.26 → 1208.18] So they are running the workload, and they produce the result without ever needing energy for cooling.
[1208.18 → 1210.44] So that can be quite good.
[1210.70 → 1218.04] But obviously, it depends a lot on the workload, the type of model you train, the number of communication rounds you do, and other aspects.
[1218.40 → 1222.62] In terms of infrastructure cost, this sort of answers this question as well.
[1222.74 → 1230.76] Because you can have, in some cases, if you have, for example, the cross-device setting, then obviously, if you're not the one operating these devices,
[1231.22 → 1234.00] then you don't have to pay for the energy that goes into training.
[1234.38 → 1237.98] Usually, when companies do this, they are very careful about it.
[1237.98 → 1239.78] They do it in a very careful way.
[1239.88 → 1246.42] So they wait until the device is plugged in, and the device is connected to Wi-Fi until it's fully charged and idle.
[1246.64 → 1253.26] And only then they do the federated learning to not impact the user experience or to not drain the battery or things like that.
[1253.56 → 1258.98] In the cross-silo setting, there's, I wouldn't say that there's much of a difference in terms of infrastructure.
[1259.54 → 1263.46] You need, well, each company needs the infrastructure they would need anyway.
[1263.46 → 1265.72] And then you need one additional server.
[1265.86 → 1270.48] So that's pretty similar, especially in the cross-silo setting where you often have large models.
[1270.84 → 1274.16] You do have a lot of network bandwidth that you need.
[1274.28 → 1276.30] So that's something that you should consider.
[1276.30 → 1279.12] You talked a little bit about the training time.
[1279.36 → 1281.70] You talked a little bit about what's happening on the device.
[1281.86 → 1289.48] I think what's happening in the back of my mind is I'm thinking like, okay, I've got all of these devices and there's sort of various axes along which things could change, right?
[1289.48 → 1294.06] I could have like the computational power of that edge device or the client.
[1294.50 → 1300.36] And then I've got also like the number of samples that are available for training on that device.
[1300.48 → 1303.08] I'm thinking if, and maybe you could speak to this.
[1303.14 → 1310.88] So I'm thinking like in the scenario of like a low power edge device or a phone, like I'm going to have very few samples,
[1310.88 → 1318.04] which might be a sort of quick update on that device of the model and communicate the parameters back.
[1318.16 → 1323.90] Whereas like as the kind of amount of data that you have on the client is larger,
[1323.90 → 1328.94] you sort of need more computational power, at least more time to do the update.
[1328.94 → 1332.30] Is that kind of how that trade-off happens in practice?
[1332.78 → 1333.36] Yes, absolutely.
[1333.74 → 1339.36] I mean, yeah, obviously if you have more data on a device, you need more time to train the model on the data.
[1339.36 → 1347.28] But this is actually also a very interesting aspect, not just in terms of practical things like communication bandwidth and so on.
[1347.52 → 1355.82] But it's also quite interesting from a more fundamental perspective, namely in both in the cross device setting and in the cross silo setting,
[1356.32 → 1363.40] usually the data in these partitions, as we like to call them, the data in these partitions is coming from different distributions.
[1363.40 → 1366.12] So it's what we like to call it non-IAD data.
[1366.12 → 1369.96] And this actually has an impact on the learning process.
[1370.52 → 1375.42] There are certain scenarios which are very rare in a practical setting,
[1375.56 → 1383.80] but there are scenarios actually where the data distribution within each partition can be so different that it's just not possible that these workloads converge.
[1384.08 → 1391.42] And this is something where a lot of research is going on how to make federated learning more robust towards such scenarios.
[1391.42 → 1399.02] And yeah, the practical aspects of it are also quite interesting because if you have multiple clients in the same workload,
[1399.32 → 1404.78] one of these clients just has very few data examples and another client has tons of data examples.
[1405.26 → 1411.14] For example, we all know that one type of person that takes very few photos when they're on vacation.
[1411.14 → 1415.62] And we all know that other type of person who takes a ton of photos when they're on vacation.
[1415.94 → 1420.52] So this is a very practical example for different amounts of data on each device.
[1420.80 → 1426.90] In such a scenario, when you instruct a client to do, for example, one epoch on their data,
[1427.44 → 1431.94] then obviously this one client will be the update will be coming back much, much faster.
[1431.94 → 1440.86] So what you want to have in your entire system is some robustness towards clients who either take a very long time because they have so much data
[1440.86 → 1447.28] or towards even real stragglers who, I don't know, maybe the device is suddenly getting busy with other things,
[1447.56 → 1449.58] which delays the update coming back.
[1449.88 → 1455.14] So this is something where your software infrastructure needs to be able to handle these kinds of cases.
[1455.14 → 1461.72] And it's also something where you need appropriate ways of handling it on the server side.
[1462.08 → 1469.34] So the one obvious or the easiest thing to do is obviously to discard those clients that are taking a long time,
[1469.46 → 1470.10] that are stragglers.
[1470.40 → 1474.40] But then there are more clever ways to approach this, for example, to let this client know,
[1474.56 → 1475.86] hey, your time is running out.
[1475.98 → 1477.46] We are about to close the round.
[1477.72 → 1480.02] Why don't you submit your partial update?
[1480.02 → 1486.04] But then your server side and the aggregation logic, it needs to be able to handle those partial updates coming from clients.
[1486.66 → 1493.92] So, Daniel, you've talked a little bit about certain client devices being stragglers from one perspective,
[1493.92 → 1502.20] but I'm curious in terms of how the federated learning community is thinking about things like bias in data.
[1502.34 → 1508.78] So if I'm a data scientist in a central location, I'm seeing maybe updates to my model,
[1508.78 → 1515.54] but I'm not seeing the data that is producing those updates to the weights and biases of my model.
[1515.54 → 1525.42] So if there's bias in terms of those in client devices, like maybe 97% of my client devices are being operated by males,
[1525.42 → 1529.10] and I have some gender bias in the data that's coming back.
[1529.20 → 1533.90] Are there ways that the community is thinking about that and ways to address that sort of,
[1533.98 → 1535.94] I guess maybe there's a term for it.
[1535.98 → 1537.56] I'm thinking of it like client bias.
[1537.56 → 1539.10] Yeah. Any thoughts there?
[1539.46 → 1540.10] Yes, absolutely.
[1540.46 → 1541.56] It's a very good question.
[1541.80 → 1543.70] And it's a very important question.
[1543.98 → 1545.98] There are different ways to think about it.
[1546.08 → 1553.60] One way is, or one approach that one topic that the community thinks about a lot is how to address that from an algorithmic perspective.
[1553.98 → 1560.00] So there are approaches, for example, FARE, federated learning, that tackle this from an algorithmic perspective.
[1560.00 → 1563.74] So when you collect updates, you can do this in a certain way.
[1563.90 → 1567.04] And you can try, for example, there are many different approaches.
[1567.18 → 1571.86] But one thing you could do is you could try to address that, for example, through the averaging process.
[1571.98 → 1573.00] It's a weighted averaging.
[1573.00 → 1575.14] So there are ways to influence this.
[1575.14 → 1588.92] Another perspective is more from a more intuitive and more practical perspective, in the sense that you can think of federated learning as a way compared to centralized learning to actually overcome bias.
[1588.92 → 1601.78] Because you can not overcome it completely, but that's not what I mean, but help to overcome it in the sense that you can suddenly get access to more training data and hopefully more representative training data.
[1602.14 → 1615.36] And then you can make better decisions about how to train your model and what kind of pieces of data to include in your training process, how to sample these data examples that you have on the clients, and a lot of those related questions.
[1615.36 → 1645.34] Thank you.
[1645.36 → 1675.34] Thank you.
[1675.36 → 1705.34] Thank you.
[1705.36 → 1735.34] Thank you.
[1735.36 → 1736.36] Thank you.
[1736.36 → 1737.36] Thank you.
[1765.36 → 1766.36] Thank you.
[1766.36 → 1767.36] Thank you.
[1767.36 → 1768.36] Thank you.
[1768.36 → 1769.36] Thank you.
[1769.36 → 1770.36] Thank you.
[1770.36 → 1771.36] Thank you.
[1771.36 → 1772.36] Thank you.
[1800.36 → 1801.36] Thank you.
[1801.36 → 1802.36] Thank you.
[1830.36 → 1831.36] Thank you.
[1831.36 → 1832.36] Thank you.
[1832.36 → 1834.18] but it was higher on our priority list.
[1834.52 → 1837.64] So at the time, we didn't really see any solution
[1837.64 → 1840.96] that was a fit to the requirements that we had.
[1841.18 → 1843.66] We sort of had to shift our focus a little bit
[1843.66 → 1845.68] away from building this one particular system
[1845.68 → 1846.46] that we had in mind.
[1846.80 → 1848.56] And we shifted the focus away
[1848.56 → 1850.44] to first building the infrastructure
[1850.44 → 1851.96] that we had in mind for it.
[1852.20 → 1854.36] Out of that, we built a prototype for that.
[1854.60 → 1855.92] And then out of that prototype,
[1856.28 → 1858.30] we gathered a lot of learnings, obviously.
[1858.72 → 1861.10] And eventually at the beginning of last year,
[1861.10 → 1863.60] Tanner, my co-founder and I, we said,
[1863.74 → 1866.38] okay, let's start a company and build this infrastructure
[1866.38 → 1868.44] to bring these advances that we see
[1868.44 → 1871.40] and this huge potential to make this really accessible
[1871.40 → 1872.74] for others to use as well.
[1873.06 → 1875.52] The Flower Framework is probably obvious by now
[1875.52 → 1878.36] that one of the reasons the Flower Framework is there
[1878.36 → 1882.92] is that we want to enable everyone to build such workloads
[1882.92 → 1885.60] because there are a lot of details going on under the hood
[1885.60 → 1887.26] that are not easy to implement.
[1887.66 → 1890.00] And if you just want to do federated learning,
[1890.00 → 1893.24] it would obviously be a huge hurdle for others
[1893.24 → 1894.90] to first build this infrastructure
[1894.90 → 1897.38] before they then can build their actual workload.
[1897.62 → 1898.82] We wanted to make this easy.
[1899.14 → 1901.70] We wanted to make it easy to start in research
[1901.70 → 1904.00] and then gradually enhance these workloads
[1904.00 → 1905.94] and move them to production eventually
[1905.94 → 1907.86] and then to operate them in production.
[1908.28 → 1910.24] This is also something we haven't quite seen
[1910.24 → 1910.92] in other frameworks.
[1911.04 → 1912.16] Other frameworks that we've seen
[1912.16 → 1914.54] are usually focused on one thing,
[1914.62 → 1917.94] for example, focused on being a good simulation engine,
[1917.94 → 1919.60] but then you can't take these workloads
[1919.60 → 1920.64] and move them into production.
[1921.08 → 1923.26] And the other opportunity that we saw,
[1923.56 → 1925.18] and this is part of this user journey,
[1925.30 → 1927.84] making it easy to start to prototype something,
[1928.22 → 1930.24] is the opportunity to be compatible
[1930.24 → 1932.80] with all the machine learning frameworks
[1932.80 → 1933.78] that we are seeing out there.
[1933.78 → 1937.20] So we see huge excitement about TensorFlow and PyTorch.
[1937.34 → 1940.18] Obviously, those are the dominating frameworks,
[1940.30 → 1940.78] I should say.
[1941.22 → 1944.10] Now there's a lot of excitement about TAX by many people.
[1944.48 → 1946.34] And there are these other frameworks,
[1946.46 → 1947.76] which are also relevant,
[1947.90 → 1950.14] sometimes relevant for very specific cases.
[1950.56 → 1952.32] And the opportunity that we saw is,
[1952.52 → 1954.26] well, sort of based around the story,
[1954.48 → 1956.60] you have an existing machine learning project.
[1956.98 → 1959.42] What's the minimal amount of code changes
[1959.42 → 1962.58] that you have to do in order to federate this thing?
[1962.58 → 1964.22] And we have code examples on that
[1964.22 → 1966.08] where you can take an existing workload
[1966.08 → 1969.38] and then federate it in less than 20 lines of code,
[1969.60 → 1971.70] which is actually, I still find it amazing
[1971.70 → 1973.58] given the amount of things
[1973.58 → 1975.02] that are going on under the hood.
[1975.26 → 1975.40] Yeah.
[1975.52 → 1977.56] And you mentioned supporting
[1977.56 → 1978.96] all of these different frameworks,
[1978.96 → 1980.80] which does seem like a big task.
[1980.80 → 1982.30] And I'm kind of looking through
[1982.30 → 1985.52] the flower usage examples and the documentation.
[1985.96 → 1987.74] And I also love just, you know,
[1987.96 → 1990.90] I mean, you explicitly say it's a friendly framework,
[1990.90 → 1992.00] which I think is great.
[1992.00 → 1993.22] You talked about accessibility.
[1993.90 → 1995.88] You've got a very friendly flower logo.
[1996.26 → 1998.06] And so, yeah, I think it, you know,
[1998.10 → 2000.72] it puts up an inviting front for people,
[2000.86 → 2002.44] which I think is cool because it is a
[2002.56 → 2003.64] it can be, like you said,
[2003.68 → 2007.24] a very overwhelming, complicated thing to get into.
[2007.44 → 2008.90] You were talking about supporting
[2008.90 → 2009.98] these different frameworks
[2009.98 → 2012.56] and maybe you could give a sense of like,
[2012.88 → 2014.24] it seems like a big task
[2014.24 → 2016.74] to support all of those in this way.
[2016.74 → 2019.82] And I see that the main kind of way
[2019.82 → 2022.08] in which you wrap things with flower
[2022.08 → 2024.02] is like creating this class,
[2024.16 → 2027.76] Python class, maybe that wraps certain methods.
[2028.20 → 2029.12] And within those,
[2029.18 → 2031.56] you can define your own sort of TensorFlow
[2031.56 → 2033.88] or PyTorch or whatever ways to fit
[2033.88 → 2036.44] or get parameters of a model
[2036.44 → 2037.22] or whatever it is.
[2037.38 → 2039.06] Did you purposely create that structure
[2039.06 → 2040.38] because you had this vision
[2040.38 → 2042.12] of supporting the multiple frameworks?
[2042.12 → 2044.50] And am I representing that accurately?
[2045.10 → 2045.78] Yes, absolutely.
[2046.00 → 2047.08] We call it flowered,
[2047.08 → 2048.70] friendly federated learning framework
[2048.70 → 2049.96] exactly for that reason.
[2050.18 → 2051.16] So we want to be friendly
[2051.16 → 2052.98] in many different dimensions, actually.
[2053.10 → 2053.86] We want to be friendly
[2053.86 → 2054.92] when it comes to different
[2054.92 → 2055.94] machine learning frameworks.
[2056.06 → 2056.94] We want to be friendly
[2056.94 → 2058.74] when it comes to different device types.
[2058.96 → 2059.98] We want to be friendly
[2059.98 → 2061.18] when it comes to different
[2061.18 → 2062.30] transport mechanisms.
[2062.76 → 2063.74] So we actually have,
[2063.84 → 2064.38] this is not something
[2064.38 → 2065.52] that is upfront on the website,
[2065.52 → 2066.40] but we have different
[2066.40 → 2068.06] transport mechanisms built in
[2068.06 → 2069.80] and you can swap these out, actually.
[2070.22 → 2071.60] So the building and support
[2071.60 → 2073.14] for different frameworks,
[2073.30 → 2073.94] this was something
[2073.94 → 2075.46] that we intended to do
[2075.46 → 2076.50] from the very beginning.
[2076.80 → 2078.54] And there are different layers to this
[2078.54 → 2079.84] that are important
[2079.84 → 2081.64] or at least interesting to understand.
[2081.90 → 2083.70] So one layer is the client class
[2083.70 → 2084.64] that you just described.
[2084.76 → 2087.12] So when you build your client in Python,
[2087.62 → 2088.64] then you would create
[2088.64 → 2090.62] a subclass of client.
[2090.78 → 2092.44] So flower.client.client
[2092.44 → 2094.18] is what the class is called
[2094.18 → 2097.64] or a subclass of flower.client.numpyclient,
[2098.02 → 2099.38] which is even easier to implement.
[2099.88 → 2101.36] And you basically just need to add
[2101.36 → 2102.80] these few lines of code
[2102.80 → 2105.26] that then call into your existing
[2105.26 → 2106.68] machine learning pipelines,
[2107.08 → 2108.44] which is on the one hand,
[2108.48 → 2109.38] a simple concept,
[2109.60 → 2110.44] but on the other hand,
[2110.54 → 2112.00] a very powerful concept
[2112.00 → 2113.20] because it allows you,
[2113.44 → 2114.76] when you implement these classes,
[2114.90 → 2116.44] it allows you to call
[2116.44 → 2118.22] arbitrary Python libraries.
[2118.68 → 2119.18] So for example,
[2119.48 → 2121.14] one good and one important example
[2121.14 → 2122.32] for that is the support
[2122.32 → 2123.26] for differential privacy.
[2123.68 → 2125.78] We sometimes get requests,
[2125.90 → 2127.12] hey, does flower come
[2127.12 → 2129.46] with differential privacy built in?
[2129.46 → 2131.34] And actually the answer is
[2131.34 → 2132.22] we don't have to
[2132.22 → 2133.66] because you can,
[2133.74 → 2134.04] for example,
[2134.18 → 2136.68] for a PyTorch-based workload,
[2136.86 → 2137.84] you can use this library
[2137.84 → 2138.64] called Spaces,
[2138.98 → 2140.62] which gives you a sort of
[2140.62 → 2141.86] a differential private
[2141.86 → 2142.96] STD optimizer
[2142.96 → 2144.20] that you can plug
[2144.20 → 2144.96] into your workload
[2144.96 → 2146.50] and then you can just use it.
[2146.70 → 2147.70] And the amazing thing
[2147.70 → 2148.66] about this is that
[2148.66 → 2149.76] with the flower framework,
[2149.76 → 2151.24] it doesn't even have to change.
[2151.46 → 2152.40] If there's a new library
[2152.40 → 2153.04] coming out,
[2153.08 → 2154.16] a new approach coming out
[2154.16 → 2154.80] for what you can do
[2154.80 → 2155.44] on the client side,
[2155.62 → 2156.82] you can just integrate it
[2156.82 → 2157.90] with arbitrary code.
[2158.20 → 2159.40] The other layer
[2159.40 → 2160.68] that is maybe interesting
[2160.68 → 2161.40] to understand,
[2161.56 → 2162.28] maybe not so much
[2162.28 → 2163.14] for researchers
[2163.14 → 2164.64] who do most of their
[2164.64 → 2166.08] day-to-day work in Python,
[2166.48 → 2167.12] but to others
[2167.12 → 2168.22] who want to maybe
[2168.22 → 2169.62] more deeply integrate this
[2169.62 → 2171.96] in the automotive setting
[2171.96 → 2173.32] or something similar to that,
[2173.48 → 2174.30] they wouldn't want
[2174.30 → 2175.24] to use Python
[2175.24 → 2177.36] for their on-device processing.
[2177.54 → 2179.08] So they would want
[2179.08 → 2180.54] to use a different language,
[2180.72 → 2181.26] for example,
[2181.98 → 2183.20] C to do that.
[2183.56 → 2184.86] In the automotive world,
[2184.86 → 2186.56] there's this C dialect
[2186.56 → 2187.54] called Mr. C
[2187.54 → 2188.48] that you have to use
[2188.48 → 2189.82] for safety purposes.
[2190.14 → 2190.44] For example,
[2190.48 → 2191.04] it prevents you
[2191.04 → 2192.08] from using recursion
[2192.08 → 2193.16] and other things like that,
[2193.26 → 2194.04] things that are being
[2194.04 → 2194.90] considered unsafe
[2194.90 → 2195.82] in the automotive world.
[2196.26 → 2197.60] And in those scenarios,
[2197.60 → 2199.70] you can still integrate
[2199.70 → 2201.90] your device with Flower
[2201.90 → 2204.00] by directly handling
[2204.00 → 2204.78] the events
[2204.78 → 2205.28] that are coming
[2205.28 → 2206.04] from the server.
[2206.30 → 2206.88] So in the end,
[2207.00 → 2207.68] Flower has been designed
[2207.68 → 2208.70] in a way where
[2208.70 → 2209.74] the client side
[2209.74 → 2211.18] is actually rather easy
[2211.18 → 2211.70] to implement.
[2212.08 → 2213.16] And if you have something
[2213.16 → 2214.28] that is running on C
[2214.28 → 2214.90] or C++,
[2215.32 → 2216.26] all you would have to do
[2216.26 → 2217.40] is you would have to establish
[2217.40 → 2218.62] a connection to the server.
[2218.82 → 2219.68] The server would then
[2219.68 → 2221.84] occasionally select this client.
[2222.16 → 2223.22] And when it selects the client,
[2223.34 → 2224.44] it sends it a message.
[2224.72 → 2225.48] You on the client side,
[2225.54 → 2226.68] you have to handle this message.
[2226.88 → 2227.86] You can do your processing.
[2228.02 → 2228.78] It doesn't have to be
[2228.78 → 2229.78] any of the well-known
[2229.78 → 2230.96] machine learning frameworks.
[2231.14 → 2232.48] You can hand code
[2232.48 → 2233.44] the type of model
[2233.44 → 2234.02] that you have.
[2234.24 → 2235.24] And then you send back
[2235.24 → 2236.40] a message containing
[2236.40 → 2237.22] your update,
[2237.30 → 2237.76] for example,
[2237.96 → 2238.72] the gradients
[2238.72 → 2239.32] that you collected.
[2239.84 → 2240.22] That's awesome.
[2240.38 → 2241.54] I love that sort of
[2241.54 → 2243.16] client agnostic focus.
[2243.36 → 2243.68] It's cool.
[2243.68 → 2244.56] One of the things
[2244.56 → 2245.52] I was curious about,
[2245.66 → 2246.72] because as a practitioner,
[2246.72 → 2247.86] I'm kind of in and out
[2247.86 → 2248.88] and I'll do other things
[2248.88 → 2249.56] in my job.
[2249.74 → 2251.44] And when I'm coming back in,
[2251.50 → 2252.38] I'm having to kind of go,
[2252.54 → 2253.54] how did I do that before
[2253.54 → 2253.94] and stuff?
[2254.00 → 2254.70] And one of the things
[2254.70 → 2255.36] that I've noticed
[2255.36 → 2256.24] in the industry
[2256.24 → 2257.74] is that the barriers
[2257.74 → 2260.16] to be able to access
[2260.16 → 2261.84] or utilize machine learning
[2261.84 → 2262.84] are getting lower.
[2262.90 → 2263.90] And there are a lot of tools
[2263.90 → 2265.30] around usability coming out.
[2265.68 → 2266.78] What does the story
[2266.78 → 2268.06] look like for Flower
[2268.06 → 2268.80] and maybe for
[2268.80 → 2270.02] federated learning at large
[2270.02 → 2271.18] as you have
[2271.18 → 2273.20] more users out there
[2273.20 → 2275.16] of various technical capability
[2275.16 → 2276.74] and maybe gradually,
[2276.98 → 2277.40] you know,
[2277.44 → 2279.12] having that technical requirement
[2279.12 → 2280.46] going lower and lower
[2280.46 → 2281.86] as the tooling gets better.
[2281.98 → 2283.44] How will federate learning
[2283.44 → 2284.46] fit into that world
[2284.46 → 2285.40] where more users
[2285.40 → 2286.78] with less specific skill
[2286.78 → 2287.40] in this area
[2287.40 → 2289.22] are accessing these tools
[2289.22 → 2290.44] and creating models
[2290.44 → 2291.18] of various types?
[2291.36 → 2292.26] What does that look like there?
[2292.66 → 2293.42] That's a great question.
[2293.84 → 2295.40] So I'm sometimes saying
[2295.40 → 2296.38] that we've been,
[2296.46 → 2298.06] or maybe we still are,
[2298.06 → 2299.46] I'm not perfectly sure on that,
[2299.54 → 2301.60] in a pre-TensorFlow era
[2301.60 → 2302.42] when it comes
[2302.42 → 2303.36] to federated learning.
[2303.74 → 2304.36] It was the case
[2304.36 → 2305.04] for a long time
[2305.04 → 2306.24] that if you wanted
[2306.24 → 2307.16] to build
[2307.16 → 2308.40] a federated learning workload,
[2308.74 → 2310.22] you usually had
[2310.22 → 2311.26] research scientist
[2311.26 → 2312.12] type of person
[2312.12 → 2313.94] start out to prototype this,
[2314.12 → 2315.62] make a simulation of it.
[2315.90 → 2317.14] And if that converges,
[2317.48 → 2318.52] then you could actually,
[2318.72 → 2319.60] you could make the decision
[2319.60 → 2320.92] that you want to
[2320.92 → 2322.14] have this in production,
[2322.14 → 2323.28] but then you would
[2323.28 → 2324.34] basically start from scratch
[2324.34 → 2325.50] and you would implement it
[2325.50 → 2326.54] in quote unquote
[2326.54 → 2327.64] real system
[2327.64 → 2328.84] with, I don't know,
[2329.08 → 2330.00] Java or C++
[2330.00 → 2330.86] or something like that.
[2331.24 → 2332.22] So you had to
[2332.22 → 2333.32] build these systems
[2333.32 → 2334.18] by hand.
[2334.32 → 2334.82] And there's a
[2335.00 → 2335.30] for example,
[2335.38 → 2336.52] there's a blog post
[2336.52 → 2337.66] that compares
[2337.66 → 2338.82] federated learning frameworks
[2338.82 → 2341.22] and before Flow was around,
[2341.52 → 2342.78] the conclusion was really,
[2343.08 → 2343.78] if you want to build
[2343.78 → 2344.46] this workload,
[2344.80 → 2346.20] a federated learning system
[2346.20 → 2347.66] and you want to build it
[2347.66 → 2349.22] in really a production environment,
[2349.80 → 2350.94] then your best option
[2350.94 → 2352.16] is to just build it
[2352.16 → 2353.22] from scratch by hand.
[2353.52 → 2354.36] They've recently updated
[2354.36 → 2355.14] this blog post
[2355.14 → 2355.96] to say that
[2355.96 → 2356.78] for their scenario,
[2356.78 → 2357.78] they choose to use
[2357.78 → 2358.38] Flower for that.
[2358.70 → 2358.94] Obviously,
[2358.94 → 2359.80] I'm happy about that,
[2359.90 → 2360.78] but it's still not
[2360.78 → 2361.54] a super,
[2361.66 → 2362.84] super polished experience.
[2363.02 → 2363.64] So Flower makes it
[2363.64 → 2364.42] a lot easier
[2364.42 → 2365.26] to start out
[2365.26 → 2365.86] on that journey,
[2366.30 → 2367.20] but it's still
[2367.20 → 2368.62] a couple of
[2368.62 → 2369.64] moving pieces
[2369.64 → 2370.54] that you should
[2370.54 → 2371.54] sort of
[2371.54 → 2372.38] understand
[2372.38 → 2373.36] to make
[2373.36 → 2374.28] informed decisions
[2374.28 → 2375.22] about how to
[2375.22 → 2376.12] configure your workload,
[2376.26 → 2376.74] for example.
[2377.28 → 2377.94] That's something
[2377.94 → 2379.02] that is obviously
[2379.02 → 2380.08] one of our priorities
[2380.08 → 2380.76] to make this
[2380.76 → 2381.44] even easier,
[2381.58 → 2382.40] to make it even
[2382.40 → 2383.44] less likely
[2383.44 → 2384.76] that if you are
[2384.76 → 2385.50] not an expert
[2385.50 → 2385.96] on this,
[2386.02 → 2386.76] that you are
[2386.76 → 2387.76] configuring something,
[2387.86 → 2388.46] building something
[2388.46 → 2389.38] that might not be
[2389.38 → 2389.92] a good choice
[2389.92 → 2390.44] in production.
[2391.02 → 2392.20] So one of the things
[2392.20 → 2393.24] that we take very seriously
[2393.24 → 2394.30] is that we build
[2394.30 → 2395.78] in the right defaults.
[2395.84 → 2396.76] So one of the defaults,
[2396.80 → 2397.12] for example,
[2397.20 → 2398.00] that the Flower Framework
[2398.00 → 2399.10] is following,
[2399.52 → 2400.54] that is for
[2400.54 → 2401.66] certain types of workloads,
[2401.84 → 2403.22] it's the go-to recommendation,
[2403.56 → 2404.66] is that the Flower Framework,
[2404.84 → 2406.56] when it gets updates
[2406.56 → 2407.44] from clients,
[2407.66 → 2408.82] it does not
[2408.82 → 2410.40] persist these updates
[2410.40 → 2411.40] in any way.
[2411.40 → 2412.78] So these individual
[2412.78 → 2413.98] updates from clients,
[2414.20 → 2415.52] they could allow you
[2415.52 → 2416.84] to peek into it
[2416.84 → 2418.16] and to draw some,
[2418.48 → 2419.28] at least some minor
[2419.28 → 2419.98] conclusions about
[2419.98 → 2420.68] the client's dataset.
[2421.14 → 2421.48] And therefore,
[2421.60 → 2422.02] the recommendation
[2422.02 → 2423.20] is to receive
[2423.20 → 2423.82] these updates,
[2424.00 → 2424.84] only keep them
[2424.84 → 2425.34] in memory,
[2425.48 → 2426.72] and only for the
[2426.72 → 2427.82] minimum amount
[2427.82 → 2428.30] of time
[2428.30 → 2429.54] absolutely necessary.
[2429.74 → 2430.22] So once you
[2430.22 → 2430.90] aggregated it
[2430.90 → 2431.80] with other updates,
[2432.06 → 2432.88] you can safely
[2432.88 → 2433.54] discard it.
[2433.82 → 2434.50] And another
[2434.50 → 2435.86] very related thing
[2435.86 → 2436.20] is that,
[2436.32 → 2436.60] for example,
[2436.64 → 2437.78] the server does not
[2437.78 → 2439.82] log any client-specific
[2439.82 → 2441.30] metrics by default.
[2441.40 → 2442.42] So those are things
[2442.42 → 2443.12] that we are trying
[2443.12 → 2443.98] to build in,
[2444.24 → 2445.38] that if you just
[2445.38 → 2446.42] start the server
[2446.42 → 2447.74] with all defaults,
[2447.78 → 2449.02] that it makes something
[2449.02 → 2449.92] that does take
[2449.92 → 2450.90] a sensible approach.
[2451.26 → 2451.64] But then,
[2451.74 → 2452.10] obviously,
[2452.20 → 2453.42] there are more advanced
[2453.42 → 2454.04] users and they
[2454.04 → 2455.06] want to customize it.
[2455.44 → 2456.34] So the perspective
[2456.34 → 2457.88] is make the defaults
[2457.88 → 2458.60] sort of safe,
[2458.66 → 2459.48] as safe as we can,
[2459.82 → 2460.94] and then allow
[2460.94 → 2462.08] more advanced users
[2462.08 → 2463.00] to customize
[2463.00 → 2463.76] these workloads.
[2464.48 → 2466.14] So as we close out here,
[2466.32 → 2468.08] I'm interested to hear
[2468.08 → 2469.32] about, you know,
[2469.68 → 2470.74] what is like,
[2470.74 → 2471.84] one or a couple
[2471.84 → 2472.40] of things that
[2472.40 → 2473.40] like really excites
[2473.40 → 2474.44] you about the
[2474.44 → 2476.00] future of
[2476.00 → 2477.34] FLOWER and maybe
[2477.34 → 2478.54] its applications
[2478.54 → 2479.40] within the wider
[2479.40 → 2480.40] context of
[2480.40 → 2481.28] federated learning.
[2481.62 → 2482.70] What's the one thing
[2482.70 → 2483.48] or the couple
[2483.48 → 2484.56] things that really
[2484.56 → 2485.30] get you excited
[2485.30 → 2486.20] about where this
[2486.20 → 2486.62] is headed
[2486.62 → 2488.32] or maybe sort of
[2488.32 → 2489.16] within the roadmap
[2489.16 → 2489.88] of FLOWER?
[2489.88 → 2490.90] There are a ton
[2490.90 → 2491.34] of things
[2491.34 → 2492.30] that get me excited,
[2492.74 → 2493.58] both from a
[2493.58 → 2494.76] research perspective,
[2495.04 → 2495.84] but also from
[2495.84 → 2497.50] a practical perspective.
[2497.92 → 2498.50] From a research
[2498.50 → 2499.06] perspective,
[2499.06 → 2501.28] we just launched
[2501.28 → 2501.94] a preview
[2501.94 → 2503.24] of a new feature
[2503.24 → 2504.16] that we are calling
[2504.16 → 2505.26] the virtual client
[2505.26 → 2505.64] engine.
[2505.88 → 2506.46] The virtual client
[2506.46 → 2507.26] engine is something
[2507.26 → 2508.14] that, well,
[2508.28 → 2509.48] it manages clients
[2509.48 → 2510.34] as virtual clients,
[2510.44 → 2511.20] so those clients,
[2511.36 → 2512.18] they don't actually
[2512.18 → 2512.92] exist in memory.
[2513.46 → 2514.42] And what this gives you,
[2514.62 → 2516.18] sounds pretty trivial,
[2516.18 → 2517.62] but what this gives you
[2517.62 → 2519.16] is amazing scalability
[2519.16 → 2520.50] for your research
[2520.50 → 2520.90] workloads.
[2521.20 → 2522.74] So we did a survey
[2522.74 → 2524.20] of research papers
[2524.20 → 2525.26] and looked at
[2525.26 → 2526.02] what the scale
[2526.02 → 2526.84] of these workloads
[2526.84 → 2528.26] is in the research
[2528.26 → 2529.74] of those experiments.
[2530.14 → 2530.88] And they're really,
[2531.16 → 2532.48] the vast majority
[2532.48 → 2533.42] of papers,
[2533.64 → 2534.80] they used up
[2534.80 → 2535.90] to 100 clients
[2535.90 → 2537.06] and also up
[2537.06 → 2538.38] to 100 clients
[2538.38 → 2539.24] doing work
[2539.24 → 2540.12] concurrently,
[2540.22 → 2540.78] so training
[2540.78 → 2541.44] concurrently,
[2541.46 → 2541.92] for example.
[2542.38 → 2542.88] So you can have
[2542.88 → 2543.64] a large client pool,
[2543.72 → 2544.34] you can have a large
[2544.34 → 2545.14] client pool of,
[2545.20 → 2545.58] I don't know,
[2545.58 → 2546.72] 10,000 clients,
[2547.00 → 2547.58] but then they would
[2547.58 → 2549.06] have only 100 of them
[2549.06 → 2549.80] participating
[2549.80 → 2551.02] in the same round.
[2551.56 → 2552.24] And this is something
[2552.24 → 2553.92] that is likely
[2553.92 → 2555.58] due to resource
[2555.58 → 2556.12] constraints
[2556.12 → 2557.16] because those workloads
[2557.16 → 2558.22] can get very heavy
[2558.22 → 2559.60] and the systems
[2559.60 → 2560.60] that we read about
[2560.60 → 2561.50] from industry,
[2561.90 → 2562.48] they are
[2562.48 → 2563.46] at a vastly
[2563.46 → 2564.22] different scale.
[2564.44 → 2565.02] So they have
[2565.02 → 2566.04] millions or tens
[2566.04 → 2566.50] of millions
[2566.50 → 2567.18] or even hundreds
[2567.18 → 2567.70] of millions
[2567.70 → 2568.28] of clients
[2568.28 → 2569.16] in such a workload.
[2569.60 → 2570.54] And this is
[2570.54 → 2571.18] quite interesting
[2571.18 → 2571.82] and also
[2571.82 → 2572.74] quite an important
[2572.74 → 2573.72] challenge to address
[2573.72 → 2574.98] because obviously
[2574.98 → 2576.12] we want to have
[2576.12 → 2576.78] research
[2576.78 → 2577.84] that eventually
[2577.84 → 2579.00] translates to the
[2579.00 → 2579.52] real world
[2579.52 → 2580.54] to practical setting.
[2580.90 → 2582.10] And if the scale
[2582.10 → 2582.62] in research
[2582.62 → 2583.42] is a very different
[2583.42 → 2584.38] scale from the
[2584.38 → 2585.12] practical settings,
[2585.56 → 2586.42] it's less likely
[2586.42 → 2587.14] that the research
[2587.14 → 2587.94] that we are conducting
[2587.94 → 2589.10] will translate
[2589.10 → 2590.08] into the practical
[2590.08 → 2590.48] setting.
[2590.82 → 2591.16] So the virtual
[2591.16 → 2591.74] client manager
[2591.74 → 2592.64] is one thing
[2592.64 → 2593.46] where we demonstrated
[2593.46 → 2594.62] on quite average
[2594.62 → 2595.00] hardware,
[2595.16 → 2595.48] actually.
[2595.88 → 2596.68] We ran a workload
[2596.68 → 2598.04] with 15 million
[2598.04 → 2598.90] clients in it
[2598.90 → 2600.10] and a thousand
[2600.10 → 2600.80] of these clients
[2600.80 → 2601.82] training concurrently
[2601.82 → 2602.80] and this worked
[2602.80 → 2603.44] super well.
[2603.94 → 2604.84] So I'm quite excited
[2604.84 → 2605.52] about that one
[2605.52 → 2606.18] and especially
[2606.18 → 2606.82] quite excited
[2606.82 → 2607.90] to see what the
[2607.90 → 2608.64] community is going
[2608.64 → 2609.36] to do with that.
[2609.58 → 2610.38] That's from a research
[2610.38 → 2611.30] perspective, and we have
[2611.30 → 2612.04] a couple of things
[2612.04 → 2612.58] in the pipeline
[2612.58 → 2613.48] that we are going
[2613.48 → 2613.96] to announce
[2613.96 → 2614.86] over the coming
[2614.86 → 2615.24] months.
[2615.62 → 2616.52] Also from a
[2616.52 → 2617.46] practical perspective
[2617.46 → 2618.24] that's maybe
[2618.24 → 2619.02] even more
[2619.02 → 2620.54] exciting in terms
[2620.54 → 2621.60] of the real
[2621.60 → 2622.38] outcomes that we're
[2622.38 → 2622.98] going to see
[2622.98 → 2623.78] from that.
[2624.10 → 2624.98] One initiative
[2624.98 → 2626.16] that we are
[2626.16 → 2627.10] for example
[2627.10 → 2628.70] participating in
[2628.70 → 2629.64] is called
[2629.64 → 2630.46] MEDEF
[2630.46 → 2631.06] which is
[2631.06 → 2632.70] hosted by
[2632.70 → 2633.22] ML Commons
[2633.22 → 2633.86] which is
[2633.86 → 2634.66] sort of the
[2634.66 → 2635.24] organization
[2635.24 → 2636.16] that emerged
[2636.16 → 2636.76] out of
[2636.76 → 2637.52] Alpert.
[2637.60 → 2638.10] So MEDEF
[2638.10 → 2639.00] is a way
[2639.00 → 2639.52] to use
[2639.52 → 2640.02] federated
[2640.02 → 2640.58] evaluation
[2640.58 → 2641.50] to get a
[2641.50 → 2642.54] better understanding
[2642.54 → 2643.46] of the performance
[2643.46 → 2644.36] of medical
[2644.36 → 2645.12] AI models.
[2645.62 → 2646.46] It also requires
[2646.46 → 2646.96] federated
[2646.96 → 2647.58] infrastructure.
[2648.12 → 2648.42] We put the
[2648.42 → 2648.82] paper in
[2648.82 → 2649.32] archive
[2649.32 → 2652.10] a couple
[2652.10 → 2653.04] of weeks ago.
[2653.28 → 2653.78] Fascinating
[2653.78 → 2654.06] read,
[2654.12 → 2654.68] highly recommended
[2654.68 → 2655.70] and this is
[2655.70 → 2656.30] something where
[2656.30 → 2656.82] you can really
[2656.82 → 2657.42] see that
[2657.42 → 2658.38] the real
[2658.38 → 2659.06] world impact
[2659.06 → 2659.48] and real
[2659.48 → 2660.16] world improvements
[2660.16 → 2660.48] that we're
[2660.48 → 2661.06] going to see
[2661.06 → 2661.54] from this
[2661.54 → 2662.60] can be very
[2662.60 → 2663.10] profound
[2663.10 → 2663.96] because it's
[2663.96 → 2665.08] about medical
[2665.08 → 2665.72] AI and
[2665.72 → 2666.80] getting better
[2666.80 → 2667.74] performance estimates
[2667.74 → 2668.70] in medical AI
[2668.70 → 2670.06] is actually a
[2670.06 → 2670.92] very fundamental
[2670.92 → 2671.52] challenge.
[2671.86 → 2672.34] Once we have
[2672.34 → 2672.76] these better
[2672.76 → 2673.28] estimates,
[2673.54 → 2674.02] it is much
[2674.02 → 2674.84] safer to roll
[2674.84 → 2675.66] out medical
[2675.66 → 2676.46] AI models
[2676.46 → 2676.88] much,
[2676.96 → 2677.50] much faster.
[2678.02 → 2678.74] And apart
[2678.74 → 2680.48] from MEDEF,
[2680.56 → 2681.00] there are also
[2681.00 → 2681.58] a couple of
[2681.58 → 2682.28] other initiatives
[2682.28 → 2683.38] in the
[2683.38 → 2684.10] medical AI
[2684.10 → 2684.70] space and
[2684.70 → 2685.10] the duct
[2685.10 → 2685.96] discovery space
[2685.96 → 2686.58] that I'm
[2686.58 → 2687.10] very excited
[2687.10 → 2688.14] about because
[2688.14 → 2689.42] any advance
[2689.42 → 2690.64] our infrastructure
[2690.64 → 2691.58] will help
[2691.58 → 2692.48] in generating
[2692.48 → 2693.24] can have a
[2693.24 → 2693.94] very profound
[2693.94 → 2695.08] impact on
[2695.08 → 2695.94] society as a
[2695.94 → 2696.18] whole.
[2696.46 → 2696.80] So that's
[2696.80 → 2697.56] something I'm
[2697.56 → 2698.28] quite keen
[2698.28 → 2698.98] on contributing
[2698.98 → 2699.26] to.
[2699.62 → 2699.92] Well, Daniel,
[2700.12 → 2700.90] I'm super
[2700.90 → 2701.72] excited about
[2701.72 → 2702.42] all the
[2702.42 → 2702.88] things that
[2702.88 → 2703.38] you've mentioned
[2703.38 → 2704.26] in terms of
[2704.26 → 2705.44] things on the
[2705.44 → 2706.38] roadmap of
[2706.38 → 2707.26] research with
[2707.26 → 2707.96] FLOWER or
[2707.96 → 2708.86] practical uses
[2708.86 → 2709.78] of FLOWER
[2709.78 → 2710.40] and federated
[2710.40 → 2710.72] learning.
[2711.00 → 2711.52] And really
[2711.52 → 2712.36] appreciate you
[2712.36 → 2713.14] joining us
[2713.14 → 2714.06] and talking
[2714.06 → 2714.50] us through
[2714.50 → 2715.06] everything on
[2715.06 → 2715.72] the podcast.
[2715.92 → 2716.76] Appreciate it.
[2716.76 → 2717.44] And we'll
[2717.44 → 2718.02] include some
[2718.02 → 2718.62] show notes
[2718.62 → 2719.08] in our
[2719.08 → 2720.20] show posting
[2720.20 → 2721.72] for FLOWER
[2721.72 → 2722.24] and all the
[2722.24 → 2723.00] wonderful things
[2723.00 → 2723.64] that you've
[2723.64 → 2724.16] talked about.
[2724.34 → 2724.70] But yeah,
[2724.70 → 2725.26] thank you so
[2725.26 → 2725.58] much for
[2725.58 → 2726.22] joining and
[2726.22 → 2726.90] looking forward
[2726.90 → 2728.18] to keeping
[2728.18 → 2728.72] tabs on
[2728.72 → 2729.10] FLOWER.
[2729.50 → 2729.78] Thanks for
[2729.78 → 2730.08] having me.
[2730.08 → 2734.10] that's our
[2734.10 → 2734.50] show.
[2734.72 → 2735.06] Thanks for
[2735.06 → 2735.36] listening.
[2735.86 → 2736.24] For more
[2736.24 → 2736.70] like this,
[2736.84 → 2737.20] check out
[2737.20 → 2737.82] our Master
[2737.82 → 2738.14] Feed.
[2738.36 → 2739.10] It is all
[2739.10 → 2739.42] Changelog
[2739.42 → 2740.60] podcasts in
[2740.60 → 2741.38] one easy
[2741.38 → 2741.80] to consume
[2741.80 → 2742.24] place.
[2742.58 → 2743.00] Let your
[2743.00 → 2743.92] podcast app
[2743.92 → 2744.32] snag
[2744.32 → 2744.84] everything we
[2744.84 → 2745.60] produce and
[2745.60 → 2745.96] then pick
[2745.96 → 2746.48] and choose
[2746.48 → 2747.02] which ones
[2747.02 → 2747.28] to listen
[2747.28 → 2747.50] to.
[2747.82 → 2748.12] Subscribe
[2748.12 → 2748.86] today at
[2748.86 → 2749.78] changelog.com
[2749.78 → 2750.52] slash master
[2750.52 → 2751.42] or just search
[2751.42 → 2751.86] for Changelog
[2751.86 → 2752.54] Master in
[2752.54 → 2753.16] your podcast
[2753.16 → 2753.84] app of choice.
[2754.08 → 2754.66] You'll find it.
[2755.14 → 2755.94] Special thanks
[2755.94 → 2756.60] to Break master
[2756.60 → 2757.20] Cylinder for
[2757.20 → 2757.70] providing our
[2757.70 → 2758.72] music and to
[2758.72 → 2759.22] our longtime
[2759.22 → 2760.66] sponsors Vastly,
[2760.90 → 2761.52] Launch Darkly,
[2761.74 → 2762.14] and Linde.
[2762.66 → 2763.48] That's all for
[2763.48 → 2763.98] this week.
[2764.20 → 2764.74] We'll talk to
[2764.74 → 2765.12] you again next
[2765.12 → 2765.46] time.
[2789.22 → 2794.70] Game on.
