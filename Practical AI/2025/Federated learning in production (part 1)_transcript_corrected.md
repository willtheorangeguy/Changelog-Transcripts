[0.00 → 10.06] Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 → 11.46] and accessible to all.
[11.46 → 14.48] If you like this show, you will love The Change Log.
[14.70 → 19.52] It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 → 21.38] talk show for your weekend enjoyment.
[21.84 → 25.82] Find us by searching for The Change Log wherever you get your podcasts.
[26.32 → 28.36] Thanks to our partners at Fly.io.
[28.36 → 31.10] Launch your AI apps in five minutes or less.
[31.40 → 33.40] Learn how at Fly.io.
[44.28 → 48.06] Welcome to another episode of the Practical AI podcast.
[48.56 → 50.42] This is Daniel Whiten ack.
[50.52 → 57.96] I am CEO at Prediction Guard and joined as always by my co-host, Chris Benson, who is a principal
[57.96 → 60.30] AI research engineer at Lockheed Martin.
[60.68 → 61.36] How are you doing, Chris?
[61.62 → 62.78] Doing great today, Daniel.
[62.86 → 63.46] How's it going?
[63.74 → 65.34] It's going pretty good.
[65.46 → 71.84] I would say my mind is a little bit scattered today, maybe distributed over various topics,
[72.04 → 76.00] jumping from peer to peer between different meetings.
[76.00 → 83.72] Thankfully, we're just going to continue that theme today into a little bit of a discussion
[83.72 → 89.98] on federated learning because we're really happy to have Patrick Foley here with us, who
[89.98 → 94.42] is lead AI architect who's focused on federated learning at Intel.
[94.58 → 95.28] How are you doing, Patrick?
[95.62 → 96.14] Doing great.
[96.24 → 97.12] Thanks for having me on the show.
[97.60 → 98.30] Yeah, of course.
[98.30 → 105.22] I was saying one of our engineers at Prediction Guard, Aishwarya, shout out to her.
[105.32 → 110.92] She spoke at the Flower Conference over in London not too long ago, and I think bumped into
[110.92 → 111.22] you.
[111.36 → 114.98] So it was good to get that lead.
[115.60 → 119.90] But it's been maybe a little while since we talked about federated learning, which we have
[119.90 → 121.86] talked about in previous episodes.
[121.86 → 128.96] But I'm wondering just for the audience at large, who's maybe been hearing a lot about
[128.96 → 136.84] LLMs and only LLMs or Gen AI for however long now, just circling back to that topic, could you set
[136.84 → 144.94] the stage for us and give us kind of the explainer on federated learning generally and what that
[144.94 → 145.22] means?
[145.52 → 146.20] Yeah, absolutely.
[146.42 → 150.80] And just before we continue, the views and opinions that I'm sharing today are mine alone
[150.80 → 154.44] and don't necessarily reflect the position of Intel Corporation.
[154.92 → 161.72] So the main training paradigm for machine learning has been having your data centralized and then
[161.72 → 163.96] training your model on that local data.
[164.52 → 170.80] There are a lot of cases where you can't centralize your data due to privacy concerns or maybe even
[170.80 → 172.92] the size of the data is an issue.
[173.50 → 178.98] And so there's a different technique where instead of sending your data to a central place, you
[178.98 → 182.20] send your model to where the data is, and you train it there.
[182.74 → 188.10] So it's closely related to distributed training, as you could probably tell from the description
[188.10 → 188.40] there.
[188.72 → 192.30] But there's a much higher focus on privacy concerns.
[192.62 → 201.04] And so how you can verify that the model is not encapsulating something about the data and who the
[201.04 → 205.86] threats are, because it's not just a single person that is controlling all the infrastructure,
[205.86 → 208.26] but multiple parties who might not trust each other.
[208.78 → 214.86] That's where a lot of the variance of how we need to kind of focus on those concerns comes from.
[215.80 → 219.68] And just to kind of dig in, maybe just a small bit deeper there.
[219.80 → 228.66] So if you're bringing the model to this distributed data, in what way, maybe just walk us through
[228.66 → 231.62] kind of flow, I guess, of training.
[231.62 → 235.02] So you send the model to these places that have the data.
[235.24 → 242.70] What kind of happens in that training process, or how does it iterate differently than
[242.70 → 244.86] maybe what people are used to hearing about?
[245.40 → 246.08] Yeah, absolutely.
[246.30 → 251.28] So there's a number of both closed source and open source federated learning frameworks that
[251.28 → 252.20] are out there.
[252.32 → 256.98] I lead the Open Federated Learning OpenCL open source projects.
[256.98 → 259.88] And there's a number of people that do this in the same way.
[260.04 → 266.52] But really what it involves is first having a shared notion of what that model is.
[267.02 → 273.12] And then there might be a distribution phase for the workspace or the code ahead of time so
[273.12 → 278.68] that everyone has a record of what the code is that's going to be running on their infrastructure.
[279.58 → 284.86] And so at the time that the experiment starts up, there's a server or what we call an aggregator
[284.86 → 290.28] that's the central point where everyone is communicating with that server for what tasks
[290.28 → 295.70] they should be doing or what the latest model weights are that they should be training on.
[296.26 → 300.44] And then the client side is what we term as the collaborator.
[300.88 → 304.58] So everyone has a view of what that code is.
[304.64 → 309.78] And we have this concept of a federated learning plan, which includes everything outside the
[309.78 → 310.40] code itself.
[310.40 → 315.62] So this might be hyperparameters for the model, some of the network details that you might
[315.62 → 321.94] want to know whether there's TLS being used, mutual TLS, and a lot of other things that
[321.94 → 326.62] you might care about if you're a hospital that wants to be running this software on your
[326.62 → 332.34] infrastructure and you don't want to be exposing your data because of HIPAA or GDPR considerations.
[332.94 → 336.58] So there's this vetting process that's really important to happen ahead of time.
[336.58 → 341.22] And then once this vetting has happened, then there's an opportunity to actually launch the
[341.22 → 341.62] experiment.
[341.82 → 346.98] And what this means is for the aggregator or the server is launching that application that
[346.98 → 350.96] opens a that starts a gRPC server or some kind of REST server.
[351.18 → 355.60] And then for the collaborators, they are just starting their local process and making the
[355.60 → 357.22] connections to that local server.
[357.74 → 362.76] So the flow is, this is really all the setup for the experiment actually taking place.
[362.76 → 368.82] But the aggregator has an initial model weights for the for what everyone is going to be
[368.82 → 371.50] training on for that first round of the experiment.
[372.12 → 377.24] And so then everyone receives those model weights, and it's not the entirety of the model.
[377.30 → 380.76] And the way that we divide things into this provisioning phase and then the runtime phases
[380.76 → 384.14] so that we can limit what actually gets sent across the network.
[384.28 → 389.82] We don't need to be sending Python objects, which are much higher risk in terms of being able
[389.82 → 393.30] to send code that could then exfiltrate your data.
[393.40 → 394.96] And it's not necessarily vetted ahead of time.
[395.08 → 401.78] So there's very small windows of information, and we limit that communication path to NumPy
[401.78 → 402.04] bytes.
[402.18 → 406.18] And the great thing about doing things in that way is that if you're just dealing with model
[406.18 → 411.36] weights, then that means that you can train across a bunch of these different deep learning
[411.36 → 411.74] frameworks.
[411.74 → 415.10] So we can work with PyTorch models, TensorFlow models, et cetera.
[415.52 → 418.14] And you can send those model weights across the network.
[418.14 → 423.76] You can populate your Python code that's already been shipped to you ahead of time, do your
[423.76 → 424.38] local training.
[424.74 → 431.00] And then based on the updates that you have or based on your local data, you send your
[431.00 → 435.02] updated model weights back to the aggregator, and then they get combined in some way.
[435.68 → 440.48] In the simplest case, this can be something like a weighted average based on the number
[440.48 → 444.10] of data sets that you might have locally for each of those collaborators.
[444.10 → 449.42] And then this is really what constitutes a single round of federated learning training.
[449.76 → 453.56] And then what we've seen is that just by using kind of these simple methodologies, you can
[453.56 → 459.78] get to a point where you have somewhere in the realm of 99% accuracy versus a model that's
[459.78 → 461.60] been trained on centralized data alone.
[461.60 → 468.60] I'm curious, just as you were talking about the aggregation of each of the data back to
[468.60 → 474.06] the main server, and you talked a little bit about different ways of aggregating and stuff.
[474.50 → 479.94] I'm just curious, are there a lot of different approaches algorithmically to that aggregation?
[480.08 → 483.96] Or does that tend to follow the same mechanism most of the time?
[484.14 → 487.62] And do people tend to choose different ways of aggregating data?
[487.62 → 491.70] I'm just wondering how much variability is typically found in there among practitioners.
[492.30 → 493.42] Yeah, that's a great question.
[493.72 → 498.00] So we've seen that Fed Average works pretty well in a lot of cases.
[498.34 → 503.96] But because, so Fed Average is the original aggregation algorithm for federated learning
[503.96 → 504.96] that was coined by Google.
[505.08 → 506.10] This was back in 2017.
[506.36 → 510.84] And they actually coined the term federated learning originally at that time.
[510.84 → 519.36] But there are others that are out there that deal much better with data heterogeneity between
[519.36 → 523.48] the different client sites that might have different data distributions.
[524.14 → 530.52] And so when that's the case, you might need to ignore some of the outliers or incorporate
[530.52 → 538.08] their local updates differently that allows you to capture that information or converge
[538.08 → 543.20] faster to what a global model would be that would perform well on all of these different
[543.20 → 543.88] data distributions.
[544.22 → 548.02] So there's a number that do try to capture some of this information.
[548.32 → 554.08] So Fed Opt is one of those that incorporates the loss terms of the different collaborators
[554.08 → 554.70] that are out there.
[554.82 → 556.96] And this is really a hot research area.
[557.28 → 561.32] But it really varies is what we found.
[561.32 → 567.26] But by applying some of these top methods, you can generally get to a pretty good point
[567.26 → 570.08] in convergence versus centralized data alone.
[570.90 → 577.96] So Patrick, I'm curious about if we could just talk through maybe a couple of example
[577.96 → 581.70] use cases, kind of pointing out the actors in the process.
[581.70 → 584.96] So we've talked about kind of the central aggregation.
[585.12 → 590.38] We've talked about these clients or collaborators, I believe you called them.
[590.38 → 597.74] So this distributed set of collaborators who have the model and are doing updates to the model,
[597.80 → 599.76] which are then aggregated back together.
[599.98 → 608.00] If you could just maybe highlight, hey, here's an example use case in this industry with this
[608.00 → 608.98] type of model.
[609.86 → 616.46] Here's who the party would be that would be the aggregator party and where that infrastructure
[616.46 → 617.50] would run.
[617.50 → 624.98] And here are the parties that would be the collaborators where the model would be distributed.
[625.12 → 626.14] That would be very helpful.
[626.64 → 627.30] Yeah, absolutely.
[627.50 → 633.44] So I'll take one of really the first real world deployments of federated learning that
[633.44 → 635.00] my team took part in.
[635.00 → 643.60] So back in about 2018 or so, Intel started collaborating with the University of Pennsylvania on trying
[643.60 → 648.52] to deploy federated learning in hospitals for the purpose of brain tumour segmentation.
[648.98 → 655.32] So this was very recently after Google even released their seminal paper on federated learning,
[655.44 → 660.06] showing that this had high success for text prediction on Android phones.
[660.06 → 663.62] And this was the health application of this for federated learning.
[664.34 → 669.70] And so this progressed to a point where we were able to demonstrate that we were able
[669.70 → 674.36] to achieve 99% accuracy versus a centrally trained model.
[674.36 → 681.72] And then this really spanned out to a much larger real world federation where we were able to
[681.72 → 686.22] train across roughly 70 different hospitals across the world.
[686.78 → 692.10] And so each of those hospitals represent the collaborators in the architecture that I was
[692.10 → 692.88] speaking to earlier.
[693.30 → 699.78] And then the University of Pennsylvania served as that central point for the aggregator for where
[699.78 → 702.66] the initial model was populated from.
[702.78 → 707.98] And it was a 3D convolutional neural network, a segmentation model.
[708.14 → 715.74] So coming in with DICOM data and then trying to get an estimate of where a nuroblastoma brain tumour
[715.74 → 718.44] was based on that image.
[719.92 → 722.40] And so there are the collaborators and the aggregator.
[722.66 → 727.04] And then that's really the high level of what this looks like.
[727.04 → 732.08] But then there are a lot of other details that had to be dealt with beyond just this more
[732.08 → 736.08] kind of, I would say, vanilla federated learning architecture.
[736.74 → 744.20] And really where that came from was there are a lot of issues with figuring out how to identify
[744.20 → 747.64] mislabelled data when you have privacy that's at stake.
[748.16 → 753.34] And so this really requires experts in data science or someone who has a background in federated
[753.34 → 760.38] learning to go and dive into how you're identifying these conversions issues that might pop up.
[760.92 → 764.74] And so Penn was taking on a lot of that responsibility.
[765.02 → 769.92] There were Intel engineers who were very, very involved with a lot of those calls as well
[769.92 → 773.80] and trying to get on the phone and have these Zoom calls with, I mean, these different IT
[773.80 → 778.12] admins and data owners at each of the hospitals just trying to figure out where there might be
[778.12 → 780.52] a mislabelled data set or that type of thing.
[780.66 → 786.96] But it really exposed that there were gaps in the total participants' layout.
[787.26 → 793.44] And we needed to have more of this kind of shared platform for how you can exchange this information
[793.44 → 796.68] and get access to that data securely.
[796.76 → 801.48] And that's one of the things that we've been working on ever since this study came out.
[801.48 → 817.70] Well, friends, Nordcaper is the toggle ready network security platform that's built for modern businesses.
[818.20 → 822.44] It combines all the good stuff, VPN, access control, threat protection,
[822.44 → 825.12] and it's all in one easy use platform.
[825.26 → 830.08] No hardware, no complex setup, just secure connections and full control.
[830.08 → 834.14] In less than 10 minutes, no matter if you're the business owner, the IT admin,
[834.38 → 838.06] or someone on the cybersecurity team, Nordcaper has what you need.
[838.32 → 839.18] Here are a few use cases.
[839.50 → 842.02] Business, VPN, how often are you travelling?
[842.50 → 847.62] You need to have secure connections from one endpoint to another, accessing resources,
[848.32 → 851.30] preventing online threats, preventing IP leaks.
[851.84 → 852.92] This happens all the time.
[853.26 → 854.18] What about threat protection?
[854.34 → 858.96] Being in a place where you want to prevent malware, where maybe there's a high risk.
[858.96 → 859.86] You're at a coffee shop.
[860.58 → 862.64] Malware, ransomware, phishing.
[862.80 → 865.00] These things happen every single day.
[865.42 → 868.82] And users who are not protected are the ones who get owned.
[869.36 → 870.38] And what about threat intelligence?
[870.50 → 873.08] What if you could spot threats way before they escalate?
[873.16 → 877.34] You can identify, analyze, prevent internal and external risks.
[877.80 → 879.94] This is like dark web stuff all day.
[880.30 → 883.30] Data breaches, breach management, serious stuff.
[883.30 → 886.70] Well, of course, our listeners get a super awesome deal.
[886.86 → 896.00] Up to 22% off Nordcaper yearly plans, plus an additional 10% off the top with the coupon code using practically-10.
[896.42 → 900.56] Yes, that's the word practical, then L-Y-10.
[900.76 → 902.94] So practically-10.
[902.94 → 908.26] And the first step is to go to nordlayer.com slash practical AI.
[908.90 → 913.76] Use the code practically-10 to get a bonus 10% off.
[914.02 → 917.76] Once again, that's nordlayer.com slash practical AI.
[917.76 → 930.88] Well, Patrick, I'm wondering, you know, you gave a perfect example there in terms of the healthcare use case,
[931.20 → 937.06] the distributed collaborators being these hospitals, the aggregator being the university.
[937.06 → 948.36] Certainly, there's kind of other details that are relevant in that I'm sure, you know, were a lot of difficult things to work out and research.
[948.58 → 953.92] One of the things that I'm wondering, and this might be something that's on people's mind,
[954.40 → 959.20] just in terms of the climate that we're in around AI and machine learning,
[959.44 → 965.22] is what are the types of models that are relevant to federated learning?
[965.22 → 974.88] It might be somewhat of a shock to people just coming into the AI world that, hey, there are still a lot of non-gen AI models.
[975.14 → 981.40] Actually, the majority of AI models, quote unquote, or machine learning models out there are no gen AI models.
[981.88 → 986.40] So it may come as a shock to them that there's still a lot of that going on.
[986.40 → 998.20] I assume, based on what you said before, that those types of non-gen AI models are relevant to, you know, the federated learning procedure or framework.
[998.84 → 1006.54] But could you give us a little bit of a sense of the kinds of models that are relevant and maybe tie that into some of the
[1006.54 → 1015.76] I guess, just the real world constraints of managing one of these federated learning experiments in terms of, you know,
[1015.78 → 1026.86] to compute that's available or the network overhead or whatever that is and what that kind of dictates in terms of the types of models that are currently feasible to be trained in this way?
[1027.32 → 1028.02] Yeah, absolutely.
[1028.02 → 1036.76] So I would say most of the real world deployments of federated learning have focused on non-gen AI models up to this point.
[1037.34 → 1042.48] So the example that I had was this 3D segmentation type of use case.
[1042.96 → 1046.38] There's been a lot of other deployments of these classification models.
[1046.54 → 1053.20] Really, where federated learning has focused on from the framework support perspective has been around neural networks.
[1053.20 → 1061.12] And a lot of the reason for that is not just because of all the advances that have, of course, happened for neural nets over the past 10 to 15 years.
[1061.34 → 1071.62] But it's been because you have a shared weight representation for all of those models across each of the sites where they're going to be distributed.
[1072.30 → 1076.40] And really what I mean by this, and just as a comparison point,
[1076.40 → 1087.04] So say support vector machines or random forests are going to have something that is going to be based fundamentally on the data distribution that you have locally at one of those sites.
[1087.04 → 1091.04] So with neural networks and using that for federated learning,
[1091.34 → 1102.78] that allows us to have much clearer methods for how those weights ultimately get combined for the purpose of aggregation without knowing quite as much about the data distribution ahead of time.
[1102.78 → 1108.72] I will say that there are some methods for how you perform federated learning on these other types of scenarios.
[1108.90 → 1113.56] So federated XGBoost is something we recently added support for there in OpenCL.
[1114.16 → 1118.38] There are other types of methods out there that have actually performed pretty well.
[1118.92 → 1126.72] And I mean, getting back to the Gen AI piece of this, that is, of course, a big area of interest for federated learning, too.
[1126.72 → 1140.02] And we have a number of customers who have been asking about how they can incorporate, I mean, these large foundation models, generative AI models for the purpose of federated learning and this training in a privacy preserving way.
[1140.52 → 1151.62] And to get to your point or the question around the size constraints that we run into, it's, of course, an issue for these large Gen AI models.
[1151.62 → 1164.62] We're very lucky to have techniques like LEFT and quantization that can be applied so that you don't necessarily need to be training on the entirety of, you know, 70 billion weights at a time and distributing those across the network.
[1164.62 → 1170.46] Because as you scale the federation, there's, of course, a lot of network traffic that can result from that.
[1170.46 → 1176.74] So by shrinking that in any way that you can, we can still support those types of models.
[1177.00 → 1189.82] But it's still, I would say we're having to use these additional methods instead of just base training because size and the time that it takes to actually train them is, of course, always a concern.
[1189.82 → 1212.96] Yeah. And just for listeners that are maybe more or less familiar with certain terminology, this sort of LEFT, this is parameter efficient methods where maybe only some of the parameters of a model function are updated during the training process and create some efficiencies there.
[1212.96 → 1226.24] And quantization being methods to limit the precision or the size of the total parameter set by kind of, yeah, reducing the precision of those parameters.
[1226.60 → 1236.02] I'm wondering, we've kind of naturally got into it, Patrick, but you started talking about, of course, you know, requests to add features and that sort of thing.
[1236.40 → 1240.30] Obviously, in your context, I think we're mostly talking about OpenCL.
[1240.30 → 1243.48] I'm wondering if you could just give us a little bit of an introduction.
[1243.48 → 1250.46] Now we've talked about federated learning more broadly, what it is, kind of some use cases, that sort of thing.
[1250.64 → 1257.14] Obviously, there needs to be frameworks to support this process and OpenCL being one of those.
[1257.24 → 1262.10] Could you just give us a little bit of an introduction to the project at a higher level?
[1262.52 → 1268.02] Yeah. So OpenCL, Open Federated Learning is what that stands for, has been around since about 2018.
[1268.02 → 1272.00] And it came out of this research collaboration that we had with the University of Pennsylvania.
[1272.68 → 1281.32] So what other federated learning frameworks have done is they've really started from research and then expanded into real world and production deployment.
[1281.82 → 1284.62] We kind of took this the opposite direction.
[1284.80 → 1293.64] We had to deal with the real world issues that come from deployment of this framework into hospitals and the challenges that can really result from that.
[1293.64 → 1306.38] And when I say we, I mean, this is a collaboration between, I mean, my team at Intel, which is more focused on the productization side of how you take these technologies and then bring them into products.
[1306.90 → 1311.96] University of Pennsylvania, but then also Intel's security and privacy research lab.
[1311.96 → 1322.92] So they're, of course, very focused on research as well and have been thinking about security and privacy and confidential computing for quite a long time.
[1322.92 → 1342.12] So this was really a natural collaboration to bring together research with the experts in this healthcare and brain tumour segmentation type of deployments to really bring the right features into this framework that was, that started off as largely a research project at Intel,
[1342.12 → 1361.80] but then has since become a much larger framework that's focused on how you can actually perform this in across companies or across, I mean, very large types of, of, of deployments that involve academia as well as, I mean, just how you bring different parties together.
[1361.80 → 1370.80] Yeah. And it, uh, obviously it's called open FL. I'm assuming that people can, can find it somewhere in the open source community.
[1370.80 → 1389.00] And also I see there's kind of an association with the, with the Linux foundation. If I'm, if I'm understanding correctly, could you talk a little bit about those things and just sort of the I guess the ecosystem where people can find things, but also a little bit about the kind of who is involved and, and some of how that's developed.
[1389.00 → 1398.10] Yeah, absolutely. So, so open FL started as an Intel first closed source project, and then we open sourced it around 2020.
[1398.10 → 1410.78] We've since donated it to the Linux foundation, um, the data in an AI subgroup of that. And the reason was, is that open is in the name. We wanted this to be really a community driven and own project.
[1410.78 → 1425.18] And that's the, the way that we saw this gaining the most traction and success over time. So we didn't want Intel to be in the driver's seat for having complete control over what the direction of this was going to be in order to be truly successful as an open source project.
[1425.18 → 1432.40] You need to be thinking about the community and addressing really those concerns and letting them take the wheel and steering this in many cases.
[1432.94 → 1442.76] So Intel still has a large representation on the development and roadmap for open FL, but we have a technical steering committee that's governed under the Linux foundation.
[1442.76 → 1452.34] Um, so I'm the, the chairman of that, that steering committee, but then we also have, uh, flower labs who, who supports the, the flower, um, uh, federated learning framework.
[1452.34 → 1460.42] It's also a participant on that technical steering committee. Uh, we have representatives from fate, who is actually another competitor slash, uh, collaborator of ours,
[1460.42 → 1468.24] Lidos and then University of Pennsylvania, uh, as well. Um, their, their faculty has actually since moved over to Indiana University.
[1468.24 → 1473.22] So, but they still, um, represents the, the original collaboration that we, that we had.
[1473.28 → 1481.60] And they're, they're longtime collaborators of ours who, uh, continue to have a strong vision of where federated learning is most applicable for, for research purposes.
[1481.60 → 1493.90] And I guess in terms of usage, sometimes that's a hard thing to gauge with, uh, with an open source project, but, you know, could you talk a little bit about that?
[1493.90 → 1503.28] And maybe, you know, you were just at the, the flower conference, you're, you're engaging the community in other ways, I'm sure at, at other events and, you know, online.
[1503.28 → 1530.18] Could, could you maybe talk a little bit about what you've seen over the past, however many years in terms of actual, you know, real world usage of federated learning and kind of engagement in the open FL project and kind of what that momentum has looked like, how you've seen that maybe shift in certain ways over time and how you see that kind of developing moving forward.
[1531.04 → 1531.80] Yeah, absolutely.
[1531.80 → 1535.98] So I think that it's really picked up since about 2020.
[1536.42 → 1540.68] We, we were the we had the world's largest healthcare federation, um, at that, that time.
[1540.68 → 1554.10] And we published a page, a paper in, uh, nature communications demonstrating the work that we had done, but, um, it's, it's really become evident that there's a lot of real world federated learning that other frameworks are, are starting to get into as well.
[1554.10 → 1561.64] So my involvement at the, the flower summit was we, I've actually, so my team at Intel and open FL, we've been collaborating.
[1561.64 → 1565.52] We've been collaborating with, uh, flower labs for the last three, three years or so.
[1565.52 → 1571.26] And we're, we're jointly very interested in interoperability and standards for federated learning.
[1571.26 → 1583.08] So I think that one of the things that we, we both recognized early on is that, uh, federated learning is, is pretty new compared to just deep learning as, uh, uh, as, as a, as a study.
[1583.08 → 1595.04] And we're, we've, we've, we've kind of seen that things are heading the same direction that they did with the early, um, deep learning frameworks that were out there where you have a proliferation of them at the very beginning.
[1595.04 → 1603.46] And then over time, there's more consolidation across those frameworks as one, one ecosystem becomes more mature, or they specialize in really different ways.
[1603.60 → 1616.72] So we've been working closely with flower and other groups on how we can build this interoperability between our frameworks and try to get to a point where we, we have a defined standard for some of those lower level components.
[1616.72 → 1623.36] Because ultimately we're solving, uh, the same problems over and over again between our different implementations.
[1623.62 → 1625.92] And there's not really a need to do that.
[1625.96 → 1635.54] If you've done it once then, and if you've done it the right way, then you should be able to leverage that core piece of functionality and then just import it into whatever library you want to.
[1635.68 → 1639.84] That's really the, the open source ethos is building on top of the shoulders of giants.
[1640.10 → 1643.08] So, so that's the direction that we're, we're hoping to head.
[1643.08 → 1651.58] Um, and, uh, the so at the flower summit, uh, we're, we've gotten to the point now where we can actually run flower workloads.
[1651.58 → 1661.82] And this is a competitor slash collaborator of ours, but we can run their workloads on top of open FL infrastructure and getting into the pieces where we, we specialize and we, we do have differentiation.
[1662.30 → 1667.10] Um, so flower has done a great job building a large federated learning community.
[1667.10 → 1672.30] They've done wonders, I think for, for the scaling of federated learning and the visibility that's on it.
[1672.30 → 1675.74] And they've, they have a very close research tie as well.
[1675.86 → 1683.14] So they're seeing, I think the gamut of different things that people want to do in for privacy, preserving AI open FL.
[1683.54 → 1692.08] We've had, because of our, our history in security and privacy, uh, confidential computing and how you really think deeply about.
[1692.74 → 1697.32] Preventing threats for, for federated learning and these distributed multi-party workloads.
[1697.32 → 1699.86] That's an area that we've been thinking through for quite a while too.
[1700.36 → 1707.92] And we have the benefit being from Intel of actually having invented a lot of the technologies for confidential computing, like, uh, software guard extensions.
[1707.92 → 1719.50] So you can run, uh, open FL entirely within these secure enclaves, which means that, uh, even local root users do not have visibility into what is actually happening in the application.
[1719.50 → 1729.74] And if you engage other services on top of that, um, like Intel trust authority, that allows you to actually remotely verify, um, that someone else is running the workload that they're, they're supposed to.
[1730.00 → 1738.82] So part of the vision here and the and why we're so excited to be working with flower is that now you can run as part of the flower community, this very large community.
[1738.82 → 1746.34] You can run these, these workloads now inside these confidential compute environments on Intel hardware using open FL.
[1746.50 → 1756.60] So there's, there's kind of a chain of how, how all of these things flow, but that's, that's one of the directions that we're, we're really excited to be undertaking with, uh, with the wider federated learning community that's out there.
[1757.36 → 1759.86] So Patrick, that was, that was fascinating for me.
[1759.86 → 1760.72] I'm learning a lot.
[1760.72 → 1768.86] Um, and, and you got me thinking, I'm kind of starting to think about, uh, you know, open FL in my own, in my own life and my own world.
[1768.86 → 1779.96] Um, I'm really kind of focused on kind of agentic use cases and, you know, out on the edge, uh, with, uh, kind of, you know, physical AI devices that are doing that.
[1780.18 → 1787.44] And I'm, and you really got me thinking about all the, the ways that we could apply federated learning in those environments.
[1787.44 → 1812.50] I'm, I'm kind of wondering, is there, what, what, what is that is, you know, obviously a big wave of activity we're especially seeing, you know, in the last year or so, what is kind of the story around doing federated learning across, you know, physically not, not just within, you know, different data centres and stuff like that, where you have it, but edge devices where you're storing a ton of data in those devices.
[1812.50 → 1820.98] Um, and you're, you're running agentic, you know, operations and those, and you're wanting to try to, um, to, to, to apply federated learning to that environment.
[1821.26 → 1826.90] What's the thinking about where that's going and, you know, where it's at now and where it might be, uh, going forward.
[1827.48 → 1827.60] Yeah.
[1827.74 → 1829.94] So, I mean, it's going to be a big area.
[1830.26 → 1834.68] We, we, and we're fully anticipating that this is something that we want to go out and support.
[1834.68 → 1845.12] So for agentic, you have the, the neural network is, is one of the components, and then you have the tools that are actually performing operations, um, based on whatever information is coming from that neural network.
[1845.12 → 1854.92] So at a fundamental level, we can absolutely support these agentic use cases by, by training that, that neural network and, uh, doing this in a privacy preserving way.
[1854.92 → 1870.54] Uh, so I, I think one of the areas that's not necessarily that well studied yet, and I think there's, there's, there's more and more focus on this, but how LLMs can memorize data in a way that certain other neural networks, uh, cannot.
[1870.54 → 1879.56] Um, and so that's really a hot research area, but depending on, I think how you train these models and then ultimately how they're deployed.
[1879.72 → 1895.16] So if you're using privacy enhancing technologies on top of just this architecture where you're training at the edge already where the data is, then you're going to get a lot more confidence that there's not going to be your information that somehow exposed where the model ultimately ends up going.
[1895.16 → 1916.58] Yeah. And this would be like, in terms of memorization, what you're talking about here would be like, Hey, I'm training, uh, on, you know, in, in this device, let's say it's just a bunch of people's, uh, clients and there's, uh, communications on the those clients that have personal information.
[1916.58 → 1930.58] In theory, an LLM could be trained in a distributed way, but leak that data through the centrally aggregated model. Is that, am I understanding that right?
[1930.94 → 1939.76] That's, that's exactly right. And we have customers come to us all the time and ask, how can we get assurance that my data is not leaking into the model?
[1939.76 → 1966.82] And the best thing that we have to deal with this, there's, there are different types of technologies that are, that are out there. Um, you have differential privacy that can apply noise in such a way that you're, you're trying not to expose anything fundamentally about your data. When you, when you share those, those model weights, um, you have other techniques like, uh, I mean, homomorphic encryption, where you're encrypting those, those models ahead of time before they're actually even sent for the purpose of aggregation.
[1966.82 → 1994.46] But really not all of them is completely foolproof. There's, there's no free lunch, uh, as, as we say. So, and then confidential computing, it has the benefit of you can actually train in these can, can completely constrain environments, um, where not even the root user has access to, to this, this little protected, um, encrypted memory enclave. Um, but that ultimately requires that you have hardware at the edge to go and, uh, be able to perform that, that type of thing.
[1994.46 → 2021.54] So, so that's really where the challenge lies. And there's, there are other statistical measures of how you can estimate data leakage into the model. We have, uh, support in OpenCL for a tool called, uh, privacy meter that actually lets you train a shadow model based on the local training that you've done and then get some kind of graph around what the percent risk is based on, um, the local data distribution that you have and that exact model topology that you've trained on.
[2021.54 → 2036.00] So there's, I think, there's, I think, increased visibility on how you can try to quantify that amount of data leakage, but it, there's, there are some costs, um, in the case of some of these technologies at the, the cost of accuracy for the model overall.
[2036.00 → 2050.04] So it's really on a per experiment per model and per data distribution basis that you have to tune these things. And that's where there's, there's a bit of work and recommendations that need to be made from, from people who have experience in this domain.
[2050.04 → 2079.04] Okay. And I, I have a maybe this is sort of a strange question. So humour me, humour me, uh, in, in, in this one, while you were talking, I was kind of reflecting on the fact that maybe the landscape is shifting a little bit around privacy in general, um, and AI in the sense that, you know, for whatever reason, people seem to want to, you know, send a ton of their data to third party AI providers.
[2079.04 → 2097.74] Providers now. And I think gradually people are becoming more sophisticated in that and sort of understanding the implications around sending your data to, to third parties in the sense of using third party AI model providers from, from model builders and not running that in their own infrastructure.
[2097.74 → 2117.44] But there's definitely a wider, like this has opened up the topic of privacy to a much wider audience and maybe people that aren't. So before there was sort of this, maybe this discussion around federated learning amongst data scientists, researchers, those that are trying to train models to be better and better.
[2117.44 → 2135.62] It seems like now there's this wider discussion about privacy and, you know, AI providers and a lot of people talking about this. And certainly, you know, we've seen people that we're engaging with, of course, to, to build out private AI systems of their own.
[2135.62 → 2146.54] But I'm wondering, but I'm wondering from your perspective, you're kind of in the weeds or in the, in the trenches, I guess is the best word in terms of helping people with their actual privacy concerns.
[2146.54 → 2161.32] Have you seen the landscape or perception change in one way or another around kind of AI plus privacy post the kind of, you know, ChatGPT era, if you will?
[2161.72 → 2171.38] Yeah, absolutely. So OpenCL, this is the open source project that my team directly supports, but there's another kind of division of, of where my responsibility lies.
[2171.38 → 2176.68] And that's building on top of OpenCL to really address a lot of these, these customer concerns.
[2176.88 → 2190.06] And we're, my team is actually building a service on top of OpenCL called Intel Tiber Secure Federated AI that makes it a lot easier for corporate customers to go and deploy secure federated learning.
[2190.58 → 2200.38] And so for a lot of the people that we're talking to, they're, they're really concerned about, I mean, they have these foundation models that perform really well on their, their local data sets,
[2200.38 → 2207.86] but they ultimately don't have access to the data that's being generated at the edge or some of their sub customers that they're, they're working with.
[2208.32 → 2211.40] They're not necessarily experts in federated learning ahead of time.
[2211.40 → 2223.98] And so we've, we've heard from many different parties that if there was a service that could actually provide a lot of the infrastructure and recommendations for them ahead of time to go and deploy this easily,
[2223.98 → 2233.90] then this is something that would make it just a lot easier for them to actually perform a lot of these experiments and that whether this is something that's going to work for, for them over the long-term.
[2233.90 → 2240.56] So I talked about the use of confidential computing earlier and how that can be successful for, for this type of thing.
[2240.66 → 2248.06] And that's, that's an area that we, we've been trying to really specialize in and make easier for, for a lot of our customer base.
[2248.06 → 2258.14] So if you have technologies like Intel SGX that are available across the extent of the parties that are, that are participating in this federated learning experiment,
[2258.14 → 2260.42] then that gives you some really nice properties.
[2260.42 → 2269.18] Not only can you remove these untrusted administrators from the threat boundary, but you can also verify that your model IP.
[2269.18 → 2278.18] So the model weights, but even the model topology itself is not something that is divulged to anyone that shouldn't have access to it.
[2278.30 → 2280.78] So how to protect your intellectual property.
[2280.98 → 2289.24] I mean, that being of course data, and that's really one of the main focuses of federated learning is not revealing that to prying eyes, but the model itself too.
[2289.66 → 2296.24] I think for a lot of our healthcare customers, they'll, they'll spend millions of dollars going through FDA approval.
[2296.24 → 2305.38] And so having that divulged to someone represents a risk to, to all the work that they've done prior to that point.
[2305.50 → 2313.74] So we've been hearing this from a number of customers for, for years, but I think there's a as you mentioned, more visibility on it because of generative AI.
[2313.74 → 2322.24] And I think the, the doors that it unlocks for, for what the, the benefit is of actually deploying these models in the real world.
[2322.24 → 2326.14] I'm curious as I've learned a lot as through this conversation.
[2326.34 → 2332.82] And as we, I think I probably came into it, and we've had previous federated learning conversations in the past with folks.
[2332.82 → 2339.68] And I think I was still kind of stuck a little bit on kind of distributed data being the driver of federated learning.
[2339.94 → 2358.94] And you mentioned earlier that, you know, it was that, but more than that, it seems to me in this conversation that, that these concerns around privacy, which can take many different forms, you know, from, from protecting, you know, individual personal data to IP protection, to regulation, to whatever.
[2358.94 → 2364.78] Would it be fair to say that these might be the primary drivers of federated learning?
[2364.86 → 2375.38] Because it seems like that's really where this conversation has gone over time rather than what I was expecting, which was more just distributed, you know, and I brought up the edge thing a little while ago.
[2375.66 → 2377.80] I'm just wondering, do you think, am I getting that?
[2377.88 → 2381.98] Am I on the right track or in terms of getting what the drivers are these days?
[2382.34 → 2383.34] Absolutely the right track.
[2383.34 → 2398.50] And when I talked earlier about the different participants in the architecture for OpenCL, where I mentioned the collaborators and the aggregator, that's, that's really sufficient for a single experiment when everyone inherently trusts each other or there's some central body.
[2398.68 → 2412.12] And so the, the parallel here with the University of Pennsylvania and the, the federated tumour segmentation initiative, which was this world's largest healthcare federation, everyone trusted the University of Pennsylvania that was ultimately deploying these workloads.
[2412.12 → 2422.94] As you scale federated learning, and you have people that you don't necessarily know that you're welcoming into the mix, you need to have some other way of establishing that trust.
[2423.46 → 2427.80] And so governance is really the piece that's missing from, from OpenCL.
[2428.12 → 2431.62] And that's where we built on top of this with the service that we've established.
[2431.62 → 2449.84] So the how you can vet the models ahead of time, how you have a central platform of actually recording that different parties have agreed to, to the workload that is going to run on their infrastructure and having this unmodifiable way of establishing what the data sets are.
[2449.92 → 2454.24] They're going to be training on whom the different identities are that are actually participating in the experiment.
[2454.62 → 2458.26] Governance is a huge concern for a lot of the customers that we've been talking to.
[2458.26 → 2475.08] And if you want to have, you know, cross competitive types of federations, where you might have two different pharma customers who have a lot of data they've generated internally, they have mutual benefit by working together for training either one of their models on their competitions' data.
[2475.08 → 2482.92] And they might have some kind of agreement that's set up for how, what ultimate model is, is generated that they have a revenue sharing agreement or that type of thing.
[2483.08 → 2494.08] Having a platform for being able to establish that type of collaboration in a competitive environment is really where we see federated learning going over, over the long-term.
[2494.20 → 2496.34] And we're trying to figure out a way to get there.
[2496.34 → 2507.60] And yeah, you already were kind of going to maybe a good place to end our conversation here, which is really looking towards the future.
[2508.00 → 2516.36] You've been working on OpenCL and these other efforts for some time now and been engaged with the community.
[2516.54 → 2521.06] As you look forward, what's most exciting for you in the coming years?
[2521.06 → 2533.80] Yeah, what I think is really exciting is, I mean, the collaboration between the different parties that are out there, I think right now is really, I think, motivating for me personally.
[2533.80 → 2540.30] Because there's the spirit right now where everything is new and exciting for people who are deep into this field.
[2540.52 → 2544.02] And people want to figure out how to just push everything forward.
[2544.02 → 2560.70] And I think generative AI has really been a catalyst for that in terms of figuring out how we can get access to this silo data that's out there and how we can do it in a way that actually enables industry to take up these things.
[2560.70 → 2565.16] Because we don't want for federated learning to sit in the research world forever.
[2565.16 → 2575.06] We want to actually take this forward and make it one of the main methods of how you do machine learning at scale when you have these privacy concerns that are, of course, extremely common.
[2575.22 → 2576.60] They're common for companies.
[2576.74 → 2578.60] They're common for individuals.
[2578.92 → 2586.24] So opening up those silos is really one of the things that I think there's going to be a lot of benefit by doing that.
[2586.24 → 2597.20] And it's going to come, that benefit's going to come in the form of much more, or we expect much more accurate models over the long term and much more capable models because of just the increased access to data.
[2598.00 → 2598.04] Awesome.
[2598.62 → 2601.34] Well, that is very exciting.
[2601.64 → 2606.02] I hope to have you back on the show very soon.
[2606.20 → 2613.42] You know, next year, whenever we see some of that playing out, appreciate your work and the team's work,
[2613.42 → 2617.74] the wider community's work on what you're doing.
[2618.16 → 2619.56] And yeah, keep up the good work.
[2619.66 → 2620.46] Thanks for taking time.
[2621.08 → 2622.98] Thank you for having me on the show, Daniel and Chris.
[2623.14 → 2623.88] Really appreciate it.
[2630.82 → 2631.74] All right.
[2631.98 → 2633.84] That is our show for this week.
[2634.20 → 2640.16] If you haven't checked out our Changelog newsletter, head to changelog.com slash news.
[2640.16 → 2642.62] There you'll find 29 reasons.
[2642.84 → 2646.20] Yes, 29 reasons why you should subscribe.
[2646.68 → 2648.04] I'll tell you reason number 17.
[2648.64 → 2651.40] You might actually start looking forward to Mondays.
[2651.56 → 2654.26] Sounds like somebody's got a case of the Mondays.
[2654.66 → 2659.20] 28 more reasons are waiting for you at changelog.com slash news.
[2659.40 → 2665.12] Thanks again to our partners at Fly.io, to Break master Cylinder for the Beats, and to you for listening.
[2665.50 → 2668.16] That is all for now, but we'll talk to you again next time.
[2668.16 → 2698.14] We'll be right back.
