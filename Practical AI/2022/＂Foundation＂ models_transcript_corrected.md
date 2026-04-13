[0.00 → 1.68] But then there's this idea of misuse.
[2.10 → 8.46] You can create a really flexible, extremely powerful model, which lets you do a whole
[8.46 → 10.88] variety of downstream things much easier.
[10.88 → 16.76] So in other words, you can do named entity recognition, sentiment analysis, create fake
[16.76 → 19.32] news or target marginalized groups.
[19.80 → 25.00] On the one side, we're creating these large language models that we would like to be more
[25.00 → 30.76] accessible to people because we don't want the concentration of power around these foundation
[30.76 → 33.22] models being with just a few entities.
[33.70 → 34.22] So I don't know.
[34.28 → 36.68] I don't know what the right balance is there.
[45.72 → 46.78] Hello, friends.
[46.94 → 51.80] Jared here to tell you about Changelog++, our membership program for those of you who want
[51.80 → 53.44] to directly support our work.
[53.44 → 58.42] Your Plus membership gets you closer to the metal with extended episodes, makes
[58.42 → 63.66] the ads disappear, and takes our audio to the next level with higher bitrate MP3s.
[63.80 → 67.42] You can join today at changelog.com slash plus.
[67.42 → 85.20] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[85.20 → 86.84] and accessible to everyone.
[87.20 → 91.52] This is where conversations around AI, machine learning, and data science happen.
[91.52 → 97.26] Join us at practicalai.fm slash community and follow the show on Twitter.
[97.46 → 99.62] We're at practicalai.fm.
[99.86 → 104.48] Thank you to our partners at Vastly for shipping our pods superfast all around the world.
[104.72 → 106.56] Check them out at fastly.com.
[106.56 → 118.06] Welcome to another fully connected episode of the Practical AI podcast.
[118.12 → 123.14] In these episodes, Chris and I keep you fully connected with everything that's happening
[123.14 → 124.30] in the AI community.
[124.54 → 129.52] We'll take some time to discuss some of the latest AI news, and then we'll dig into some
[129.52 → 133.06] learning resources to help you level up your machine learning game.
[133.06 → 134.54] I'm Daniel Whiten ack.
[134.66 → 137.84] I'm a data scientist with SIL International.
[138.16 → 143.30] I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed
[143.30 → 143.56] Martin.
[143.84 → 144.42] How are you doing, Chris?
[144.60 → 145.58] Doing great, Daniel.
[145.66 → 146.32] How are you doing today?
[146.58 → 147.58] Doing pretty good.
[147.78 → 149.46] How's the strategy world?
[149.84 → 154.42] After that, our last fully connected when we were talking about innovation teams and
[154.42 → 159.24] stuff, a lot of those ideas have been swirling around in my mind, and I just figure that's
[159.24 → 163.68] what the life of a strategist, you're thinking about those things all the time.
[163.86 → 167.90] So I've been thinking about you over the past week as you've been strategizing.
[168.24 → 170.60] We pretend like we know what's going to happen next.
[170.88 → 172.38] It's a great gig if you can get it.
[172.66 → 172.82] Yeah.
[172.90 → 173.80] Well, that's the thing.
[174.00 → 178.78] Isn't the saying, if you try to predict the future, that's the one thing you can be
[178.78 → 179.82] sure you're going to get wrong?
[180.04 → 180.30] Yeah.
[180.46 → 180.64] Yeah.
[180.70 → 180.90] Yeah.
[180.94 → 182.52] I'm pretty okay being wrong too.
[182.64 → 183.08] I just say it.
[183.08 → 183.10] Yeah.
[183.10 → 184.38] You sort of embrace that.
[184.38 → 190.30] We did the strategy win, and then I know we've talked about data fabric recently, and that's
[190.30 → 191.72] also been another interesting thing.
[191.80 → 196.52] I'm still working on that pretty intensely and some stuff that I'm doing and having a
[196.52 → 197.76] good time because you know what?
[197.92 → 200.06] This whole AI thing keeps rolling forward.
[200.30 → 200.56] Yeah.
[200.72 → 201.40] Yeah, definitely.
[201.74 → 207.54] And there's something I wanted to bring up in this episode and sort of talk through with
[207.54 → 207.86] you.
[208.38 → 211.56] It's not like an extremely recent thing.
[211.56 → 216.74] It was back in, I think, August that some of this came out, but we haven't talked about
[216.74 → 217.06] it yet.
[217.22 → 219.18] And I realized we haven't talked about it yet.
[219.26 → 225.30] And at the time, there was a lot of language floating around that I didn't really know what
[225.30 → 227.98] people were meaning when they said this stuff.
[228.40 → 233.48] I've kind of circled back to some of that and kind of figured out what we're talking about
[233.48 → 234.74] at least a little bit.
[235.12 → 236.60] And I'd love to talk through that with you.
[236.64 → 240.48] And that's around the topic of foundation models.
[240.48 → 249.10] So this is something that was work done at Stanford University, actually in a centre for research
[249.10 → 254.34] on foundation models, CRFM at Stanford University.
[254.34 → 261.92] And they came out with a fairly lengthy and very interesting report on this topic, which
[261.92 → 264.36] they're calling foundation models.
[264.36 → 271.90] And I remember at the time, people were sort of like responding to, I think, mostly the
[271.90 → 274.52] name foundation models.
[274.84 → 277.08] Like, oh, well, what are you like?
[277.14 → 282.60] Maybe there's some hubris around like saying, hey, we're working on foundation models, which
[282.60 → 284.62] are the foundation of AI.
[285.16 → 289.64] I think clearly they've also released some articles around this or blog posts.
[289.64 → 293.04] And I think that clearly wasn't, you know, at least their intention.
[293.60 → 295.66] But it's a fascinating article.
[295.66 → 302.30] So the article that they wrote is on the opportunities and risks of foundation models.
[302.50 → 305.80] First off, I guess, Chris, have you come across this term?
[306.58 → 307.80] I have come across it.
[307.92 → 311.58] And I, too, have found it confusing in the same way.
[311.86 → 314.98] And so this is an interesting article that you found here.
[315.12 → 316.22] You want to give us a definition?
[316.22 → 323.56] Well, I figure that being in the good spirit of a programmer, I would just rather copy and
[323.56 → 325.62] paste than create my own.
[326.12 → 329.54] So we'll go for the definition from Stanford.
[330.00 → 334.08] And that's actually, I think, a good thing to start with just sort of parsing through.
[334.56 → 343.88] So they say, we define foundation models as models trained on broad data in parentheses,
[343.88 → 352.50] generally using self-supervision at scale that can be adapted to a wide range of downstream
[352.50 → 353.12] tasks.
[353.60 → 356.44] So let's sort of take a step back and parse through that.
[356.82 → 361.74] I think most of our listeners are familiar with some type of models, that jargon.
[362.10 → 368.78] By this, probably we're meaning mostly like neural network type of models, modern model architecture,
[368.78 → 376.26] but basically some sort of parameterized function in code, right, that is trained based on some
[376.26 → 381.58] data using training algorithm of some type, an iterative training process.
[382.26 → 383.24] And so that's a model.
[383.46 → 391.50] And it is, they're saying foundation models are trained on broad data, generally using self-supervision
[391.50 → 393.10] at scale.
[393.10 → 400.30] So some of those terms, particularly self-supervision, might not be the most familiar to people.
[400.44 → 402.64] Have you run across this in your own work, Chris?
[402.90 → 403.50] Yes.
[403.68 → 409.96] In terms of different levels of supervised learning and the fact that we are now more and more
[409.96 → 416.12] training models that are either unsupervised or at some level between that, self-supervised.
[416.48 → 422.76] The thing that I am curious about here is how should I think about this in terms of transfer
[422.76 → 423.16] learning?
[423.16 → 427.40] Is this something that I would use as a base for transfer learning to build upon?
[427.68 → 434.74] Yeah, I think that when they're doing their report, two things or the two kind of pillars
[434.74 → 441.32] on which foundation models that they're calling them are built, if I'm remembering right, they
[441.32 → 444.50] talk about transfer learning and scale.
[445.28 → 452.10] So for those that are maybe familiar to transfer learning, that's where you have some sort of pre-training
[452.10 → 452.94] that goes on.
[452.94 → 458.12] And that's on a task that's maybe related to the task that you want to eventually do.
[458.26 → 465.02] But then you sort of transfer and learn or fine tune that model for the actual downstream
[465.02 → 470.10] task, which you're interested in, which is different from the one, the pre-training task.
[470.54 → 475.36] And so I think this gets, it does get to that, Chris, because they're talking about a variety
[475.36 → 478.20] of downstream tasks.
[478.20 → 484.56] So this is the scenario where you had some pre-training that happened on one of these foundations
[484.56 → 492.24] models, a large model, and then your transfer learning, or maybe in a zero shot or few shot
[492.24 → 496.20] way, that model is able to perform a variety of downstream tasks.
[496.20 → 502.24] So it fit into that zone of like transfer learning, zero shot, few shot type of scenarios.
[502.62 → 505.88] So that's one side of it, that pillar of transfer learning.
[506.08 → 507.68] The other side is scale.
[507.88 → 515.74] Now, the interesting, I think, connection between scale and self-supervision is that in the sort
[515.74 → 522.94] of, I guess, more traditional supervised machine learning world that we kind of started with,
[522.94 → 530.26] you always had a data set that was annotated or labelled for the task that you're interested
[530.26 → 531.06] in, right?
[531.28 → 534.70] And then you trained your model on that data set.
[534.86 → 539.46] The problem with that, right, is that that's hard to scale, right?
[539.50 → 545.94] It's hard to scale sort of across a wide variety of tasks because you have to have a data set for
[545.94 → 547.10] each of those tasks.
[547.10 → 551.10] And it's very expensive and time-consuming to create those labelled data sets.
[551.10 → 556.88] But also, if you think of the size of even one of those data sets, the more data you need
[556.88 → 561.84] or the more complex task it is, you might need to label a lot of data.
[561.98 → 567.80] So for example, the question answering task in natural language processing, I've learned
[567.80 → 569.78] because I'm working with some of that data now.
[569.94 → 576.64] It's really time-consuming to build those data sets or like conversational AI data sets.
[576.64 → 581.32] Sometimes a lot of very hard and difficult work goes into making those.
[581.44 → 588.88] So if you want to scale your data sets for training in that sense, self-supervision is
[588.88 → 595.02] actually really kind of another important feature here of these models because let's say you had
[595.02 → 598.68] just a bunch of text, just like blah, a bunch of text, right?
[598.68 → 606.70] Well, you can actually, in a self-supervised way, create your own training data to train this
[606.70 → 613.32] foundational model or this large language model by let's just take some sentences, remove words,
[613.70 → 617.60] and say the task is, tell me what word went here.
[617.96 → 622.30] And since you are the one that took the word out, right, you know what word should go there.
[622.30 → 630.00] So you're self-supervising this pre-training task, which is much more scalable in terms
[630.00 → 631.52] of preparing the data for training.
[632.14 → 633.42] So I misused the term earlier.
[633.56 → 636.36] I was conflating unsupervised with self-supervised.
[636.62 → 637.52] Pardon my confusion there.
[637.84 → 640.36] Yeah, no, it's confusing terminology, right?
[640.52 → 645.26] There's the semi-supervised, self-supervised, unsupervised, supervised.
[645.48 → 648.48] There's a lot of supervision going on of different types.
[648.62 → 650.86] So yeah, it's a worth kind of diving into those.
[650.86 → 656.54] But yeah, I think the idea is we're really talking about scale, and you can't build large
[656.54 → 662.44] data sets, at least not in a cost-efficient, time-efficient way if you're always thinking
[662.44 → 664.72] just in terms of supervised learning.
[665.22 → 665.82] Yeah, fair enough.
[666.06 → 669.40] So how might you think about implementing this?
[669.44 → 674.04] If you're out there, and you're interested in moving into this as a new skill set that
[674.04 → 677.50] you want to develop for your organization, what would a good first step be?
[677.50 → 684.86] Yeah, well, I think that that's a fascinating question in this work.
[685.14 → 689.26] Because actually, one of the things that they talk about, because they're talking about
[689.26 → 697.24] opportunities and risks with foundation models, is that accessibility and homogeneity are things
[697.24 → 699.48] that come up with foundation models.
[699.48 → 705.92] Meaning that actually me, like my team working, I might not be able to create one of these
[705.92 → 707.20] foundation models, right?
[707.36 → 708.84] Because I don't have the resources.
[709.62 → 714.44] So just to give a kind of couple examples, we're talking about here things, maybe that
[714.44 → 721.84] certain things that people might be familiar with are things like BERT or GPT-3 in the language
[721.84 → 722.34] space.
[722.34 → 729.46] But then there's other computer vision models and other sort of modalities, speech models,
[729.72 → 732.60] like thinking of Wave2Vec or other things.
[733.14 → 740.50] So if you imagine like tasks in computer vision, tasks in natural language processing, tasks in
[740.50 → 747.04] speech technology, and you look at what people are doing now, very often a bulk of the things
[747.04 → 753.20] that people are doing are sort of homogeneous in the sense that they're all built on one
[753.20 → 759.94] of these foundation models, whether it's BERT or Wave2Vec or one in the GPT variety, or
[759.94 → 763.74] you know, all of these are sort of built on one of these foundation models.
[763.74 → 769.16] Like we fine-tuned BERT to do this, or we, you know, transfer learned this foundation model
[769.16 → 769.88] to do that.
[770.40 → 776.86] And so this is one of the things that they bring up in the paper as a risk is that there's
[776.86 → 778.82] sort of two things that come out from this, right?
[779.20 → 785.54] One is not all researchers and practitioners can create their own foundational model because
[785.54 → 792.52] I don't have like racks of GPUs maybe, or the computational resources, the manpower to
[792.52 → 794.30] actually create a model on the scale.
[794.44 → 797.24] So that's one thing is like, hey, is it bad?
[797.54 → 799.34] Is that necessarily a bad thing?
[799.60 → 805.92] I think it is concerning that like this sort of concentration of people that can actually
[805.92 → 807.56] create this state-of-the-art work.
[807.56 → 813.34] But then the other side of that is like, if there's an unexpected behaviour or bias in
[813.34 → 819.22] that foundation model, then that actually filters through down to a huge number of downstream
[819.22 → 824.38] tasks and applications because no one's retraining that foundation model, right?
[824.40 → 826.94] It's just there and everybody's using it, right?
[827.26 → 829.04] And so that's another risk.
[829.24 → 834.56] So I think the implications are really what should be on the mind of practitioners in terms of this
[834.56 → 835.22] trend maybe.
[835.70 → 840.42] You know what that reminds me of just as an analogy, as you were saying that is if we
[840.42 → 846.42] look at the software world in parallel, there are some software bits out there that you find
[846.42 → 850.22] in open source that are in just about everything, you know, and they flow downstream.
[850.70 → 855.10] And if you get a bug, you know, thinking about the bias in the model or something, but if you get a
[855.10 → 861.34] bug in the software, something unintended, it can have fairly substantial consequences as it flows
[861.34 → 865.38] downstream. And I, is that the right way of thinking about this is that since you're relying
[865.38 → 870.40] on this so much that if you do go awry, it's going to multiply itself many times?
[870.82 → 876.44] Yeah, definitely. I think that that is exactly the it's not an exact parallel because we're
[876.44 → 882.16] thinking of like mostly issues maybe stemming from data and bias in data maybe or something
[882.16 → 888.50] like that. But it is parallel in the sense that like, Hey, if everybody imports this one package
[888.50 → 894.24] and it, and it breaks upstream, then there's a huge consequence downstream, right? And the
[894.24 → 899.84] parallel here would be everybody's using, let's say BERT to create all of these different NLP
[899.84 → 907.52] applications. Well, what happens if there's this bias in BERT, and we've seen examples of failures of
[907.52 → 914.36] these large models, right? And so, yeah, I think that is a that is a good parallel. So Chris, I think
[914.36 → 920.62] maybe one of the things that I remember when, when this came out is that people were kind of thrown
[920.62 → 928.12] off by the terminology. I think even in the blog posts that I was reading, which I'll link in our
[928.12 → 935.66] show notes, they say the name foundation model has also drawn significant attention. And given that
[935.66 → 939.62] they want to clarify it. So there's a whole clarification in this article. I'll link in the
[939.62 → 943.78] show notes. They threw me off at the beginning of the show. Yeah. I mean, naming is difficult,
[943.78 → 950.16] right? It is. So like, what is that? Like naming, naming variables is the most difficult part of
[950.16 → 954.54] software engineering. In the software world, there's nothing harder than naming variables. Well,
[954.74 → 962.18] yeah. So I do feel for them and I think that they were making a, a good attempt at this. And I've,
[962.36 → 969.02] I've actually felt this tension maybe in our previous conversations, because, you know, I come from the NLP
[969.02 → 974.76] world, and we have this like term large language model, right? Which is essentially what they're
[974.76 → 982.24] calling a foundation model for our space, right? But the thought process around that type of model
[982.24 → 988.16] and the way it's used downstream, the way it's trained, that is pervasive across other modalities,
[988.32 → 996.38] right? In computer vision, in audio, even in areas where people are doing like biological structures
[996.38 → 1004.82] and other things, this idea of having a large base model that's trained in a self-supervised way at
[1004.82 → 1011.64] scale and, and used in a variety of downstream tasks, that idea is, is kind of pervasive. So I,
[1011.66 → 1016.98] I do like the fact that like in the past, I felt this tension, even when I've taught classes,
[1016.98 → 1023.98] like, what do I call this? Like thing, we're doing this, this like new trend in how we're operating.
[1023.98 → 1029.04] And I think you could talk about it under the heading of transfer learning, under the heading of
[1029.04 → 1036.82] like few shot, zero shot or self-supervision. But I do appreciate the attempt to create a term
[1036.82 → 1042.44] that sort of encompasses all of these things that are at play, because there's definitely this,
[1042.54 → 1046.60] this trend. So I don't know if you have any thoughts on that. I'm not opposed to the name,
[1046.64 → 1050.74] actually. I, I kind of like having a name to refer to this as, but I don't know.
[1050.74 → 1057.08] I don't know if it's catching on. I don't hear like tons of people using it out there. So maybe
[1057.08 → 1062.00] it's not catching on, but I kind of wish that it or something like it would, right?
[1062.36 → 1067.44] I had heard the term, but just like self-supervised learning, I don't think I had really gotten the
[1067.44 → 1072.38] correct meaning right on. Its interesting is in the article here, they, they kind of talk about
[1072.38 → 1077.82] this trend, as you pointed out and where it's going and whether, what the implications are. And they,
[1077.82 → 1083.40] they talked to that a little bit lower in the article and they specifically kind of address
[1083.40 → 1089.78] the pace of technological process, the entrenchment of the models themselves, because of, you know,
[1089.78 → 1095.20] some of the limitations that you pointed out earlier and the demand of kind of this, the human
[1095.20 → 1101.80] social side of it and technology. And it raises a good point. I mean, they empower us to be able to
[1101.80 → 1105.44] use these things because it gives us a capability we might not otherwise have,
[1105.44 → 1111.86] but there are definitely some pitfalls there, you know, especially in terms of, you know,
[1111.86 → 1116.68] bias in the data that you pointed out. Where do you think, I mean, as someone who is using large
[1116.68 → 1122.20] models on a regular basis yourself and the work, do you think that this is probably where things will
[1122.20 → 1127.10] continue going for some time or do you see any alternative? I think it's kind of a necessary evil
[1127.10 → 1132.78] to have foundational models, you know, what by that name or otherwise to build work upon,
[1132.78 → 1137.66] you know, shoulders of giants kind of idea. Any thoughts there or whether that's, are the risks
[1137.66 → 1145.76] too great? Yeah. I think that as you mentioned in my own work, like we don't train for the most part,
[1145.92 → 1152.70] we're training a lot of downstream task models and few, maybe what would be considered foundational
[1152.70 → 1159.22] models or in a this sort of self-supervised pre-training way, although we have done it a bit.
[1159.22 → 1166.68] So I've benefited a lot in my own work from, from this trend. And I think it does come with risks
[1166.68 → 1172.88] though. I think when I was going through this article and thinking things through a lot of it
[1172.88 → 1180.16] centred around sort of concentration of power and other kind of trends in the AI world, especially
[1180.16 → 1186.80] because I work at a nonprofit that works with minority language communities. For the most part,
[1186.80 → 1192.08] local languages, minority languages are left out of foundational models in the NLP world,
[1192.34 → 1199.12] right? So I, I already view this as an issue, and they bring this up in terms of, they talk about,
[1199.12 → 1207.30] you know, supporting diverse research. And I think regardless of the modality that we're working
[1207.30 → 1212.88] with, it's important that we consider whether it's geographic diversity, language diversity,
[1212.88 → 1219.40] but also diversity of those creating the data sets and training the models and having representation.
[1220.04 → 1225.72] All of those things I think are both are really critical. If this trend continues, and we don't
[1225.72 → 1233.88] think about that side of things, then this sort of marginalized groups in terms of how they're able
[1233.88 → 1238.40] to use these foundational models and the implications of the applications that are produced,
[1238.40 → 1244.08] they're only going to become more marginalized because if foundational models are a key piece,
[1244.34 → 1250.52] or I keep calling them foundational, foundation models are a key piece of this sort of new tech
[1250.52 → 1257.24] stack that we're building for the digital sphere. And those groups are just left out or there's bias
[1257.24 → 1263.10] in the models against those groups in various ways. Then that's a real problem in terms of their own
[1263.10 → 1265.14] sort of flourishing in the digital sphere.
[1265.14 → 1270.30] I think that's a fantastic insight that you just made there. And that is that, you know,
[1270.36 → 1275.66] from an economic standpoint, people who make these large models, these foundation models
[1275.66 → 1281.84] are invented to solve the problems, which are probably being done by kind of what is current
[1281.84 → 1287.92] mainstream, you know, kind of current top of the power stack, if you will, you know, in terms of
[1287.92 → 1295.50] companies and countries even. And so there is an incentive to unintentionally perpetuate inequality
[1295.50 → 1302.70] with these. And so it's a real, I think that would be a real dilemma. How might you tackle that
[1302.70 → 1309.52] going forward to where if, if we're looking at foundation models as being somewhat core to most
[1309.52 → 1315.16] workflows in the AI space, because they're available, and they accelerate where you're trying to go,
[1315.16 → 1322.90] but that they are built on imperfect data that has bias that leaves out marginalized groups.
[1323.08 → 1327.74] Do you just iterate and add those in and redo that? There's a certain investment, obviously,
[1327.74 → 1334.72] to be made in that. Do you have any thoughts on least evil path forward to get the best foundation
[1334.72 → 1338.66] model with the least amount of unintended consequence over time?
[1338.66 → 1346.12] Yeah, it's a difficult question. My sense is that that is why Stanford created the centre,
[1346.28 → 1350.12] although I wasn't, I haven't, we would love to have someone from the centre on the podcast,
[1350.12 → 1355.52] but I haven't talked in detail about the motivation to them. So I'm not putting words in their mouth,
[1355.64 → 1362.24] but I think there are multiple sides to this. I think one side of it is having, you know, think tanks
[1362.24 → 1368.64] or research groups that are really thinking about the problem and how foundation models,
[1368.64 → 1376.90] large language models, you know, computer vision models and other pre-trained models are influencing
[1376.90 → 1382.86] society more generally and the risks, the opportunities with that, because there's clear opportunities,
[1382.86 → 1389.42] but there's also, there's also risks. So having that research side of things, I think is a key piece,
[1389.42 → 1397.08] but also I think as practitioners, this needs to be part of our thought process when we're using
[1397.08 → 1405.80] these models. And I mentioned this fairly frequently on the podcast, but the idea of kind of probing the
[1405.80 → 1411.66] behaviour of the models that you're releasing into production, I think is a key piece of this. So
[1411.66 → 1418.88] not just trusting that like, Hey, Google or open AI created this great model. I'm going to fine tune
[1418.88 → 1425.00] it on this task. Okay. It does great on my test data set. So, you know, push it up to production.
[1425.22 → 1432.56] I think of behavioural testing, where you actually probe, how does my model respond to these
[1432.56 → 1438.20] changes in my data? What if I perturb my data in this way? What if I switch out this for that?
[1438.58 → 1444.34] What if I make this change, which should be invariant in the output? Is it actually invariant in the
[1444.34 → 1450.72] output and creating that sort of test suite of behavioural tests for your model, I think is, is a
[1450.72 → 1457.26] big thing that practitioners can keep in mind in terms of how these foundational models might impact
[1457.26 → 1467.04] their downstream customers. The report actually does, they talk about the social impact, but they have
[1467.04 → 1472.92] this mindset. There's a figure three in the paper. Their figures are really nice. I wish I could make
[1472.92 → 1480.34] figures that nice. They talk about this sort of almost like a value chain or something of usage of
[1480.34 → 1485.74] these foundation models, starting from data creation through data curation, through training and
[1485.74 → 1494.66] application and deployment. And they think about the impacts of those models along that chain. So like
[1494.66 → 1501.56] there are real people on either side of that chain, right? What is the diversity that's represented in
[1501.56 → 1509.76] those groups, and what might be the impact of having biases in this sort of data producers or the
[1509.76 → 1516.06] consumer side, the makeup of the consumers? So I think that's a perfect way of thinking about it and
[1516.06 → 1522.22] having that more holistic picture in mind is helpful. Yeah. You know, as you were going through that,
[1522.48 → 1529.70] it struck me that in addition to kind of accounting for the unintended consequences behaviourally,
[1529.70 → 1536.12] as you perturb data and stuff that the flip side of that coin becomes vulnerabilities from a security
[1536.12 → 1543.18] standpoint in terms of affecting the outcomes of foundation models or any model for that matter
[1543.18 → 1549.48] by doing that. And so it just has a greater multiplier, you know, associated with the foundation
[1549.48 → 1554.86] since you're building so much on top of that. So as we look at this in the days ahead, it will be
[1554.86 → 1561.90] interesting to see as well what the security implications are of protecting the end users
[1561.90 → 1568.50] that are impacted by this. Meaning, you know, the model will change the behaviour of lots of different,
[1568.50 → 1573.88] you know, executions on that where people are using it for various use cases that affect people.
[1574.04 → 1578.54] I would conclude by noting that in all of this that we're talking about, it's starting with human
[1578.54 → 1583.48] beings, and it's ending with human beings. And we are a little bit at the mercy of the models as
[1583.48 → 1588.58] we're trying to make improvements in other ways in our lives to do things productive in the world.
[1588.84 → 1591.08] It's a curious set of problems that we face going forward.
[1591.08 → 1598.62] Okay, Chris. So in continuing our way through this material that Stanford has put out,
[1599.14 → 1604.84] they actually do have, I think your point made around like people on either side of this,
[1604.90 → 1609.78] they talk about emphasizing the role of people. So I think they're very much with you in that.
[1609.78 → 1617.46] They also use this terminology in terms of how to mitigate some of this risk and vulnerability stuff.
[1618.02 → 1626.50] They talk about how foundation models can and increasingly should be grounded. Now, that was
[1626.50 → 1634.24] also a term that I wanted to make sure that I sort of dug into a little bit because maybe it could mean
[1634.24 → 1638.36] a variety of things. Is that terminology you've come across?
[1638.74 → 1643.48] No, I ran across that in the article a moment ago, just before you said it. And I was wondering,
[1643.82 → 1648.48] and then you went there, I was wondering, what do they mean by grounded? So what do they mean by
[1648.48 → 1649.10] grounded, Daniel?
[1649.30 → 1656.86] So it is interesting that there's sort of a couple of ways that you could come at this. And I found people
[1656.86 → 1664.12] talking about this idea of grounded models coming from the vision perspective, but also coming from
[1664.12 → 1671.78] the NLP perspective. Both, I think you can kind of get to the same idea from both directions. If you're
[1671.78 → 1679.48] coming from the computer vision side, you might want to look up some things about CLIP, which is a model
[1679.48 → 1686.42] that's being talked about or a methodology that's being talked about quite a bit. But from the language side,
[1686.42 → 1695.42] the interesting thing about language is that language is sort of a way to encode knowledge
[1695.42 → 1703.12] about the real world in some sort of concrete way, right? Like even the words that I'm talking about
[1703.12 → 1709.06] right now, I have thoughts and ideas in my mind. I have perceptions of the real world, and I'm encoding
[1709.06 → 1719.28] them in a concrete set of symbol representations, right? And so there's a set of symbols that aren't really like
[1719.28 → 1731.34] the set of symbols DOG, you know, conjures up ideas in my mind about what that set of symbols mean. And I know it does
[1731.34 → 1739.00] for you as well, having 10 or more of them at any given time. But those symbols are representative of things that are
[1739.00 → 1745.26] grounded in the real world, right? It's just a sort of symbolic representation of things that are grounded in the real world.
[1745.26 → 1756.78] And so this idea of grounding is thinking about more widely like, well, instead of, you know, always just having a labelled data set that says like,
[1757.22 → 1767.88] oh, here's DOG, here's dog in my text, and that's an entity, I'm going to label it as an entity of some type and, you know, do name entity recognition or something.
[1767.88 → 1785.28] Well, thinking about a language model being grounded is a much broader way to look at this where you realize, oh, well, that has other representations that are actually grounded in kind of multiple modalities of how people experience DOG.
[1785.64 → 1795.36] And language is just one of those, right? Or textual language is just one of those. There's also a way to say DOG, right? In audio.
[1795.36 → 1811.22] And there are all sorts of, of course, the internet is filled with images and videos of DOG, and there are drawings of DOG. And so there's not a single sort of element that's representative DOG in any modality, right?
[1811.28 → 1820.18] You could do the same from vision, right? If you have a single picture of DOG in your data set, your model is going to assume that's the only way you can represent DOG, right?
[1820.18 → 1833.54] And so when you see a different type of DOG, it might cause your model to have a vulnerability because it's not used to classifying a pug as a DOG when all it's seen is a golden retriever, right?
[1833.54 → 1851.96] And so the idea of grounding, and if anyone wants to correct me, our listeners can correct me, but it really has to do with pulling together these modalities of data to ground our model in more than just a sort of single symbolic representation of an idea,
[1851.96 → 1869.66] but building multimodal models that can ground our ideas or our perception of these ideas in this sort of multiple modalities to increase robustness and flexibility, especially if we're using these on a variety of downstream tasks.
[1870.22 → 1873.56] I feel like I said a lot there. I don't know if any of that came true.
[1873.56 → 1881.66] If I'm understanding you correctly, correct me if I'm not, but you're basically saying having that diversity to achieve what the model is representing.
[1881.96 → 1894.44] So the representation is built on diversity, gives it that robustness, it gives it that ability to recognize all the things that that representation might take the form of. Is that a good way of summarizing?
[1894.44 → 1924.42] Yeah, yeah.
[1924.44 → 1954.42] That's a good way of summarizing.
[1954.44 → 1984.42] That's a good way of summarizing.
[1984.42 → 1991.10] You, sir, you, sir, are grounded. That's what I usually hear. So yours is a much better definition in my book.
[1991.50 → 1997.52] Yeah, yeah. And you can think of how this would create or could create vulnerabilities, right?
[1997.52 → 2004.40] Like we, based on our perception of the world, we know that like a bird belongs in a tree, right?
[2004.40 → 2017.50] But then if I put like a car in a tree, we have the sort of common sense to reason that like based on all our experience in all of our modalities of existence, we know that that's odd.
[2017.50 → 2018.00] It is.
[2018.00 → 2024.60] And that's not quite right. But that's not what how machine learning and AI systems typically work.
[2024.60 → 2027.90] They would just know, hey, there's a tree here and there's a car here.
[2028.18 → 2028.34] Yeah.
[2028.40 → 2030.22] And, you know, that can create an issue.
[2030.62 → 2032.66] If it's not a whomping willow, it should not have a car.
[2032.74 → 2033.08] Right.
[2033.08 → 2036.26] That is definitely true.
[2036.72 → 2039.86] OK, well, I'm really interested in this idea of grounding.
[2040.10 → 2054.14] I think I don't know if you remember back when we talked with Jeff Adams, who was the was on the team or helped lead the team that created a lot of speech technology at Amazon related to Alexa.
[2054.14 → 2055.22] Yeah, I did.
[2055.36 → 2066.88] And other things. So he talked about what he was really excited by in the future was thinking more holistically about language that particularly what he's interested.
[2067.16 → 2073.10] But when he said that, what he kind of expressed was that we experienced language in all sorts of modalities.
[2073.78 → 2082.94] So language models and speech technology moving forward is going to be very multimodal was kind of how he was thinking about that.
[2082.94 → 2084.70] And that was something really exciting to him.
[2084.86 → 2088.72] So, yeah, I think this is something that I'm really excited about.
[2088.86 → 2092.36] And, yeah, this idea of grounding is fascinating.
[2092.80 → 2094.66] It is. It'll be interesting to see how it develops.
[2095.06 → 2101.68] I know that in the past, as we've hit in interesting ideas, we tend to have multiple shows that include them in the discussion.
[2101.68 → 2107.08] So I suspect that grounding is one of the new things and probably foundation is another one, though.
[2107.08 → 2118.54] So I might ask our larger community, please be better at naming because these are we've spent a good bit of the show defining some confusing terms as you come into it until you get used to it.
[2118.68 → 2127.70] Yeah. So I would say you and I are only just even touching on this idea of foundation models and the other implications of them.
[2127.70 → 2140.22] Just to give listeners a sense of this, there are other things that are discussed in the work from Stanford, their report, including what I thought was a fascinating one around misuse.
[2140.22 → 2147.94] So we've talked about kind of the vulnerability of these foundation models, one being that there's sort of a single point of failure.
[2148.10 → 2161.16] And then we've talked about this idea of grounding where maybe these foundation models don't always have the common sense that they should or aren't grounded in multiple modalities of how we experience the world.
[2161.36 → 2169.28] So that's one. But then there's this idea of misuse, which means that, and I thought maybe you would find this one intriguing, Chris, particularly,
[2169.28 → 2185.84] that the idea that you can create a really flexible, extremely powerful model, which lets you do downstream things, a whole variety of downstream things much easier means that you can do a whole variety of downstream things much easier.
[2185.84 → 2191.68] Right. So in other words, you can do named entity recognition, sentiment analysis, other things.
[2191.68 → 2201.66] But you can also do other things like create fake news or target marginalized groups or, you know, whatever that you can do those things much easier, too.
[2202.22 → 2205.68] So, you know, I think that's a that's a difficult one.
[2205.68 → 2221.26] Like on the one side, we're creating these large language models that we would like to be more accessible to people because we don't want them sort of the concentration of power around these foundation models being with just a few kind of entities.
[2221.54 → 2233.78] But the wider you distribute these, maybe the more possibility there is for misuse in the community, which is, I think, why we saw open AI kind of restrict usage of GPT-3 for so long.
[2233.78 → 2238.74] So I don't know. I don't know what the right balance is there or if there is a right balance.
[2239.00 → 2245.50] It's interesting. I think that you, you know, when we have a while back, you know, way back early in the show, there were really only data scientists.
[2245.76 → 2253.58] And then as this industry has matured, and we've gotten many different roles with different names, we've got deep learning engineers, we've got all sorts of different names.
[2253.58 → 2258.26] Now, I think that you just pointed out that there's yet another one there that has come into being.
[2258.34 → 2271.44] And that is, you know, like the foundation model security analyst, you know, who is a person charged with evaluating downstream intended consequences of a by a malicious actor.
[2271.64 → 2276.96] So there's probably a whole cybersecurity industry that you just coined now, Daniel.
[2277.28 → 2278.98] Well, I'll take credit for it.
[2279.06 → 2281.92] There you go. It's yours. It's a resumable thing.
[2281.92 → 2286.18] Yeah. It's like coming up with like voice first or.
[2286.54 → 2286.76] That's right.
[2286.90 → 2288.34] I don't know. Yeah. Some of those other things.
[2289.04 → 2291.66] They'll call you Daniel father of dot, dot, dot.
[2292.28 → 2295.60] Father of the foundation model security.
[2295.76 → 2296.32] That's right.
[2296.56 → 2296.94] That's right.
[2296.94 → 2297.68] I'll take that.
[2297.86 → 2303.90] So as we finish up here, just to tie in a learning resource to this whole discussion of foundation models.
[2303.90 → 2310.92] I don't really know a better one than this, but I have mentioned it before, and it keeps, you know, growing.
[2311.14 → 2315.06] And I think becoming better is the hugging face course.
[2315.06 → 2319.50] So if you just look up hugging face course, and of course, we'll mention it on our show notes.
[2319.98 → 2320.52] Hugging face.
[2320.70 → 2325.50] Maybe people think it's just natural language processing, but it has grown far beyond that.
[2325.50 → 2343.80] And really, like if you want to get a sense of like, what is it like to use foundation models and import them and fine tune for a downstream task, fine tune a pre-trained model or use these big data sets or portions of these data sets that are being used in foundation models.
[2343.80 → 2356.04] Hugging face and the model hub, the data set hub and their, you know, training API is really the best way to start into that topic, at least in my opinion.
[2356.04 → 2357.32] And they have their own course.
[2357.42 → 2358.32] It includes videos.
[2358.60 → 2366.94] And, you know, just looking at the thing here, they have already on the left-hand side, they talk about, you know, give an introduction.
[2366.94 → 2373.58] They talk about transformers, which is their library, but you can access all sorts of model architectures.
[2373.74 → 2378.10] And then they talk about fine-tuning a pre-trained model, sharing models and tokenizers.
[2378.20 → 2382.28] These are all sort of themes that we've talked about in this episode.
[2382.70 → 2384.68] So definitely take a look.
[2385.04 → 2392.98] I feel the need to tell people that you're not paid to do that because you've offered them up as a fantastic learning resource, which they are a number of times.
[2393.16 → 2396.20] So if our listeners haven't gone there, they really, really should.
[2396.20 → 2397.06] They really should.
[2397.16 → 2397.34] Yeah.
[2397.46 → 2402.94] And they're, they continue to just boost our own work at SIL.
[2403.16 → 2406.62] So, yeah, I don't feel bad at all about, about giving them another plug.
[2406.86 → 2408.46] When you're good, you're good, you know, and they're good.
[2408.46 → 2409.08] Yeah, I know.
[2409.44 → 2412.90] Well, Chris, I appreciate you talking through this subject with me.
[2412.96 → 2413.64] It's been fun.
[2413.92 → 2414.52] Thanks for teaching.
[2414.72 → 2416.56] And yeah, on to the next.
[2416.68 → 2419.26] Hope you have a good evening and, and rest of the week.
[2419.42 → 2420.02] Sounds good.
[2420.12 → 2420.88] See you next time.
[2421.02 → 2421.22] Bye.
[2424.46 → 2425.34] All right.
[2425.34 → 2427.44] That is Practical AI for this week.
[2427.74 → 2436.02] If this is your first time listening, subscribe now at practicalai.fm or just search for Practical AI in your favourite podcast app.
[2436.22 → 2436.74] We're in there.
[2437.04 → 2440.30] And if you're a longtime listener, please do share the show with your friends.
[2440.48 → 2443.18] It is the best way you can help Practical AI succeed.
[2443.68 → 2449.56] Thanks again to Vastly for shipping our shows superfast all around the world to Break master Cylinder for the Beats.
[2449.74 → 2450.76] And to you for listening.
[2450.98 → 2451.70] We appreciate you.
[2452.04 → 2453.16] That's all for this week.
[2453.16 → 2454.42] We'll talk to you again next time.
[2455.34 → 2485.32] We'll be right back.
[2485.32 → 2486.26] Noon, what will I do?
[2487.18 → 2493.14] No reason to injustice is especially Tier
[2493.62 → 2499.12] and not no72, which teaches a society
[2500.12 → 2502.34] and a Constitutional, although not only
[2502.76 → 2508.84] like this is a whole story of controversy
[2509.30 → 2512.22] is concerning by the UK
