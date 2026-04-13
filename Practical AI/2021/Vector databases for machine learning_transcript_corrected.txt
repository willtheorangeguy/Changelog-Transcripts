[0.00 → 7.22] I personally try to push the boundary and try to figure out what's the next huge milestone we as a society can hit.
[7.34 → 26.82] For Pine cone specifically, for us as a community, I think that really starting to think about not only the model that I trained and how do I put it in a container and ship it to some place in my app, but rather like, okay, we now have this complete wealth of data that we can now use.
[26.82 → 32.86] And how do we integrate intelligence with compute and memory and storage?
[32.98 → 37.88] How do we make that behave a lot more like a brain and not like a neural net?
[40.54 → 43.20] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[43.42 → 44.16] We love Linde.
[44.22 → 45.64] They keep it fast and simple.
[45.78 → 48.14] Check them out at linode.com slash changelog.
[48.36 → 50.44] Our bandwidth is provided by Vastly.
[50.78 → 54.34] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[54.60 → 56.30] Get a demo at LaunchDarkly.com.
[56.82 → 68.40] With advancements in AI and deep learning evolving at lightning pace, it's more important now than ever to research the best options suited to your unique needs.
[68.78 → 73.72] This is particularly true when building custom systems and those systems that are GPU heavy.
[73.76 → 81.36] Not only do the applications running on the system matter, but your AI infrastructure and budget constraints need to be front of mind as well.
[81.36 → 95.08] PSSC Labs, which is an HPC and AI custom solutions provider based in California, has been creating high performance computing systems to meet their clients' unique enterprise computing challenges for more than 25 years.
[95.08 → 109.02] And with cloud computing costs growing at astronomical rates, plus companies increasingly losing control of their data security, it is no wonder that enterprises and government agencies need to continually look for ways to take back control of their data.
[109.02 → 119.28] Solutions from PSSC Labs provide a cost-effective, highly secure, and performance guarantee that organizations need to reach their AI and machine learning goals.
[119.68 → 126.18] For more information and a free consultation, please visit PSSCLabs.com slash practical AI.
[126.66 → 130.88] Once again, that's PSSCLabs.com slash practical AI.
[130.88 → 146.28] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[146.62 → 150.68] This is where conversations around AI, machine learning, and data science happen.
[151.04 → 155.74] Join the community and Slack with us around various topics of the show at changelabs.com slash community.
[155.94 → 157.04] And follow us on Twitter.
[157.18 → 158.76] We are at Practical AI FM.
[160.88 → 167.92] Welcome to another edition of the Practical AI Podcast.
[168.28 → 169.54] My name is Chris Benson.
[169.76 → 171.82] I am a tech strategist at Lockheed Martin.
[172.38 → 179.00] Sadly, my co-host, Daniel Whiten ack, is not with me today, but we have a really, perfect show lined up.
[179.54 → 187.54] Today, we're going to be talking about how AI is changing the nature of data, the data that we have, and what we might need to do about that.
[187.54 → 192.42] With me today, I have Ido Liberty, who is the founder and CEO of Pine cone.
[192.56 → 193.18] Welcome to the show.
[193.62 → 193.96] Thank you.
[194.10 → 194.78] Happy to be here.
[195.32 → 196.90] Hey, I'm glad to have you.
[196.98 → 201.34] I'm really excited about our conversation here today because I think I'm going to learn a little bit about it.
[202.00 → 204.32] I'm wondering if you will start us off.
[204.36 → 211.66] Instead of doing the normal bio that we do with everyone, tell me something interesting, really cool, that kind of led you into this.
[211.66 → 218.68] What's the kind of thing that you'd want listeners to know that's kind of a cool thing about your background that's kind of helped you get where you're at today?
[219.20 → 223.20] You know, I can tell you in kind of what got me into like big data.
[223.52 → 229.54] I know big data is already kind of like not cool to say anymore, but it was 2005.
[229.54 → 232.20] I was working on what's called hyperspectral images.
[232.74 → 237.10] So those are images instead of RGB, you'd have like 150 different spectra.
[237.10 → 239.62] So different wavelengths, right?
[240.14 → 251.18] And so you can analyze them much more deeply with computer vision, even though to our naked eye, of course, they look the same because we only have three spectra to consume images with in our eyes.
[251.56 → 251.68] Right.
[251.84 → 259.12] But each image itself was about a gigabyte and our computers had 512 megabytes of memory.
[260.56 → 263.98] So one image was already big data, and we had like a thousand of them.
[263.98 → 271.68] And so as a PhD student, we kind of like even like just even a few images were already like big data.
[271.82 → 279.22] So even to do like basic computer vision, you already had to think about algorithms on how to get more from less with computers.
[279.32 → 284.18] I ended up doing my PhD in theoretical computer science and working on algorithms and numerical linear algebra.
[284.18 → 291.92] But it's funny how I got there was really just trying to figure out how to do like basic computer vision on a single image.
[292.20 → 298.32] But the machine was too small and you just kind of had to figure out better algorithms and just loading everything into memory.
[299.00 → 309.08] So it sounds like that was almost if you're working on that, it sounds like the move into kind of the current deep learning, you know, phase coming out of past winters and stuff really fit well.
[309.08 → 313.68] It sounds like you were really well situated for that in terms of what you had been doing in school.
[314.66 → 315.38] Yes and no.
[315.46 → 330.74] So I the beginning of my PhD was maybe like or maybe unlike other PhDs was like a period of about almost two and a half or two plus years when I experimented with different topics almost every few months.
[330.74 → 340.22] Like I would dive into like functional analysis and then like really into computer vision and then NLP and then like go into like numerical linear algebra and come back to, you know, whatever.
[340.64 → 346.44] And then it felt really chaotic and very wasteful in terms of resources, to be honest.
[346.44 → 356.68] But funny enough, over the years, as I became a director at Yahoo and then at Amazon, I actually found it to be incredibly useful because I could talk to all of these people.
[356.82 → 363.56] I could talk to the computer vision folks and I could talk to the NLP folks and I could talk to the like algorithm missions and I could talk to the, you know, engineers.
[363.74 → 364.40] And so it was fun.
[364.48 → 370.04] So all these like time wasted somehow came back in like a different life and served me really well.
[370.14 → 373.30] So it's kind of like maybe a lesson to the ages with PhD students.
[373.48 → 375.62] You know, time-wasting is not necessarily a bad thing.
[375.62 → 376.48] That's true.
[377.26 → 381.40] When you mentioned AWS, do I recall that you had something to do with SageMaker while you were there?
[381.76 → 382.08] Correct.
[382.20 → 384.70] I was the research director in charge of SageMaker.
[384.88 → 386.48] We built that platform.
[386.78 → 393.10] I led the big creation of all the algorithms components in that and kind of spearheaded most of the effort there.
[393.78 → 394.30] Very cool.
[394.58 → 396.44] And were you doing AI stuff at Yahoo?
[396.62 → 396.92] Correct.
[397.06 → 400.28] I was heading the Scalable Machine Learning Algorithms group.
[400.28 → 409.94] That was the group in charge of the infrastructure that supported like spam classification, ad ranking, you know, everything.
[410.14 → 414.48] Like personalization, ranking, threat detection, everything.
[414.60 → 417.72] Everything kind of was led by machine learning.
[417.80 → 420.90] It was done with a centralized group that was in charge of that infrastructure.
[421.10 → 423.32] Yahoo at the time was a real pioneer in machine learning.
[423.42 → 424.50] I don't know if people know that.
[424.50 → 426.60] But it used to be a real powerhouse.
[427.08 → 427.16] Gotcha.
[427.56 → 437.18] I guess as you went through those experiences at First Yahoo and AWS and they kind of shaped, you know, where you were going and the way that you would be thinking about AI.
[437.58 → 441.80] I alluded at the beginning of the episode about the changing nature of data.
[442.32 → 451.48] Can you share some of your thoughts along those lines and kind of how the world is evolving and how AI and the tools that we use in and around AI are starting to affect that?
[451.48 → 452.64] A hundred percent.
[452.94 → 456.34] So I kind of give a historical tour on machine learning.
[456.48 → 458.72] I think maybe the listeners would appreciate that.
[458.98 → 459.42] Absolutely.
[460.02 → 465.60] We have been doing machine learning basically on vectors as inputs.
[465.74 → 467.64] So there's like an array of numbers.
[467.86 → 472.00] And we used to think about them as features that we would handcraft.
[472.00 → 478.10] Like it would take like feature number one is like whatever the ratio between the volume and the price.
[478.38 → 482.74] And the feature number two is like the number of minutes it's been on the website and so on.
[483.16 → 494.94] As time passed since deep learning gained more and more traction, more and more centrality in the AI world, crafting those features became in and of itself a machine learning problem.
[495.52 → 495.76] Yes.
[495.76 → 498.44] And so now you have embeddings.
[498.70 → 512.82] So these embeddings are these like auto-generated features, like semantically deep features for objects, not only for like images and free text that we are kind of used to with NLP and computer vision models.
[513.18 → 516.18] But it's also kind of the lingua franca now for all data.
[516.34 → 520.58] So like user behaviour and threat vectors on some network and so on.
[520.62 → 523.66] So this is how we generate features this way, like nowadays.
[523.66 → 541.04] And so suddenly when you look at the world of just kind of what data infrastructure is able to digest, like we used to think about like databases and search engines kind of being kind of the main workhorses of like data, like in the data infrastructure in companies.
[541.18 → 541.32] Right.
[541.90 → 543.06] In applications in general.
[543.06 → 555.98] But they really know how to deal with like tabular data or like text and like terms and documents, you know, but they're very limited and nothing really knew how to deal with that just blob of numbers.
[556.24 → 558.60] You know, this like embedding, this like feature vector.
[559.04 → 559.08] Right.
[559.08 → 560.84] And still nothing knows how to deal with it.
[560.84 → 561.32] Right.
[561.84 → 564.74] But here's kind of the amazing thing to me.
[564.78 → 576.94] And one of the main things that led me to start Pine cone was that if you look at any projection and any current statistic already on data in the world, the vast majority of it is not in tables.
[577.18 → 580.06] The vast majority of it is not schematized.
[580.14 → 581.26] It doesn't fit in the database.
[581.38 → 582.70] You can't run SQL for it.
[582.70 → 589.78] The vast majority of it is audio and video and free flowing text and like user behaviour, which is very amorphous.
[589.98 → 593.20] A lot of like unstructured data, but it's much more than unstructured.
[593.38 → 594.54] It's like really unstructured.
[594.78 → 596.70] It's like really unruly.
[597.14 → 597.30] Right.
[597.84 → 601.60] But today with these deep learning tools, we can actually feature them.
[601.60 → 604.30] We can represent them as these high dimensional vectors.
[604.60 → 606.88] And suddenly we have something to work with.
[606.98 → 608.48] Like we have an object.
[608.80 → 610.74] Can you dive into that a little bit in terms of like,
[610.74 → 619.80] as we made this transition out of the tabular data world, you know, kind of where you had a database at the, you know, centre of every website and all that.
[619.86 → 622.12] And it was, you know, we look back, it's very quaint.
[622.32 → 632.42] And these days, as you're talking about that huge volume of unstructured data, how have we adjusted to meet that as we've moved into the modern era of machine learning?
[633.02 → 634.20] We haven't yet.
[634.38 → 638.00] We are at just the beginning of the journey, I think, on that front.
[638.00 → 641.16] So maybe let me maybe take you on a short detour.
[641.22 → 641.46] Okay.
[641.74 → 646.82] On basically how our visual system, our human visual system works.
[646.94 → 647.46] Sounds good.
[647.60 → 650.06] In a very, you know, simplified way.
[650.30 → 655.00] And maybe by analogy that would explain where we are today and what systems exist.
[655.00 → 666.60] So in a very, very schematized way, when you look at the world, you, Chris, all right, light hits your retina, activates a few neurons, a lot of neurons.
[666.72 → 671.72] That signal is sent back through a few channels and organs like neural organs in your brain.
[671.72 → 677.40] But the main one that right in the back of your neck, just above the back of your neck is your visual cortex.
[677.88 → 684.92] Six layers of neural processing that you can think about as a very, very sophisticated computer vision model.
[685.38 → 688.48] It really does look like a convolutional neural net.
[688.82 → 693.64] In some sense, it was kind of the motivation or maybe the inspiration to create neural nets the way they are.
[694.10 → 698.12] It takes local neighbourhoods and aggregates them and takes averages and activations.
[698.12 → 700.32] And every layer builds on the layer above.
[700.96 → 706.98] And in the output of that, you have an activation surface of a few million, of several million neurons.
[707.34 → 716.42] And that processing is identical no matter if you read a book or drive a car or look at your children.
[716.70 → 717.92] It does the same thing.
[717.98 → 719.48] It's pre-processing, right?
[719.52 → 720.98] It's the hardware, okay?
[720.98 → 728.04] When I think about where computer vision is today, we are mostly focused on that layer.
[728.14 → 730.46] How do we build a better visual cortex?
[730.66 → 739.94] How do we process images such that the semantic representation, that activation, enables me to do all these different tasks, right?
[740.72 → 746.74] What nobody is really doing yet is looking at how do we do the rest of the brain?
[746.74 → 750.10] So, looking at stuff doesn't end there.
[750.26 → 763.56] You know, the output of the visual cortex actually flows most of the temporal lobes, which is kind of above your ear, both ears, where you do things like, remember that when you see your children, you know them, they're your children.
[764.68 → 764.86] You know?
[765.26 → 765.72] It helps.
[766.12 → 766.92] Yeah, it helps.
[767.24 → 768.28] They're not just a person.
[768.56 → 770.30] And you know that because you've seen them before.
[770.30 → 776.62] And so, a huge part of what it means to live in the world is memory.
[776.84 → 777.12] Yes.
[777.24 → 778.04] It's inference.
[778.32 → 779.36] It's analogy.
[779.66 → 780.62] It's association.
[781.18 → 791.96] It's things that have to do with the storage and retrieval and analysis of those high-dimensional vectors and all the billions of those that you've accumulated over your entire lifetime, right?
[792.42 → 794.50] And so, it's not about processing.
[794.68 → 795.46] It's not about classification.
[795.46 → 805.34] It's about how do I store everything that I've ever seen and make it accessible to me as a person when I see something, I know what to do with it because I've seen it before.
[805.42 → 808.20] I might have seen it last time 20 years ago, but I still know what it is.
[808.34 → 809.62] I still know what it is, right?
[809.86 → 818.84] Let me ask you a quick question because we tend to talk about deep learning in terms of compute all the time, you know, in terms of the processing and stuff like that.
[818.84 → 829.62] And as you're reframing it there in terms of it's a memory, it's a memory problem, it's a memory thing to be thinking about, are we looking at it the wrong way or am I mixing two things up inappropriately?
[829.94 → 830.88] No, 100%.
[830.88 → 836.32] I think that I kind of broke the processing into two main steps, right?
[837.00 → 844.24] There is the crunching of the raw signal to bring it to a semantic representation that your brain knows how to work with.
[844.24 → 844.80] Right.
[845.22 → 854.72] And to it, I mean, maybe surprising or maybe unsurprising to you, by the way, everything that you see and remember and know kind of is those neural representations.
[854.96 → 858.94] Your brain doesn't have access to your retina directly.
[859.14 → 861.34] Like you never actually remember the actual image.
[861.50 → 864.16] The actual image is the vector representation of it, right?
[864.52 → 871.68] All I'm saying is that once you've done the kind of hardware processing of that, which is very like, you know, compute heavy.
[871.88 → 872.34] Yeah.
[872.34 → 872.82] Right.
[873.26 → 874.28] But it's stateless.
[874.88 → 875.12] Okay.
[875.48 → 879.66] Once you're done with that, you have the rest of the brain to care about.
[879.80 → 880.76] You have memory.
[881.06 → 895.54] You have things like analogy and retrieval and search and comparison and like things that have to do a lot more with kind of how a database works or what you would expect from a database of data of that kind.
[895.94 → 900.08] The reason why I started Pine cone was because no database like that existed.
[900.08 → 902.22] Like nobody knew what the hell to do with it.
[902.34 → 914.98] So it sounds like before we dive into Pine cone, though, that we're still developing the tools and infrastructure that we need to be able to handle that evolving, that changing nature of data.
[914.98 → 925.56] And as we get better at doing that, as we start accounting for the fact that we have this memory paradigm that we're trying to get used to, we need tools and infrastructure that will address that.
[925.66 → 926.76] Am I on the right track?
[926.76 → 927.56] Exactly.
[927.56 → 927.60] Exactly.
[956.76 → 963.46] And process high-quality behavioural data from all your platforms and your products and deliver that data to your cloud destination of choice.
[963.46 → 978.76] When marketing needs to make data-informed decisions, when product needs next-level understanding, and when analytics needs rich and accurate data, Snowplow is the solution for data teams who want to manage the collection, processing, and warehousing of data across all their platforms and products.
[979.10 → 983.18] Get started and experience Snowplow data for yourself at SnowplowAnalytics.com.
[983.18 → 986.12] Again, SnowplowAnalytics.com.
[986.12 → 987.12] Okay.
[1007.40 → 1008.00] Okay.
[1008.22 → 1016.10] So, you know, I know that Pine cone, when I look at the very front page of your website, it talks about managed vector,
[1016.10 → 1017.32] vector similarity search.
[1017.68 → 1023.34] And I'm assuming this is how you're approaching the issues that we were just discussing a few minutes ago.
[1023.46 → 1029.86] Can you start us off by telling me what is vector similarity search, and where does it apply?
[1030.02 → 1031.36] What does it mean to my world?
[1031.94 → 1032.04] Sure.
[1032.44 → 1037.88] Tying back to the end of the last segment, you know, we painted a very grand picture.
[1037.88 → 1042.20] But when you need to work with infrastructure, you know, you need like an API.
[1042.50 → 1044.54] You need something very, very crisp, right?
[1044.54 → 1049.08] One of the things that we started working on was say, what's the most basic thing?
[1049.30 → 1062.28] Let's say I have a very large collection of those vectors, say a billion embeddings of like all the, you know, pieces of content on Facebook or all of the web pages in the world, all the images that I've ever seen.
[1062.28 → 1067.26] What's the most basic thing you would expect to be able to do with that?
[1067.54 → 1067.66] Okay.
[1068.32 → 1071.36] And the most immediate thing is retrieval, right?
[1071.58 → 1074.54] Basically answering the question, have I seen this before?
[1074.96 → 1075.24] Right.
[1075.34 → 1076.56] It's a very basic question.
[1076.92 → 1076.96] Right.
[1077.04 → 1077.14] Sure.
[1077.14 → 1085.22] Now, unlike strings or some IDs, you know, they're not identically matching ever, right?
[1085.32 → 1085.54] Right.
[1085.66 → 1091.62] Nothing they've ever seen is an identical like, you know, photon to photon match.
[1091.68 → 1092.46] I mean, it's not.
[1092.54 → 1094.26] It's a different, you know, it's slightly different.
[1094.44 → 1097.22] So, what does kind of the same mean, you know?
[1097.22 → 1103.48] So, when you translate to these semantic vectors, you have the semantic similarity in the world.
[1103.68 → 1103.78] Okay.
[1103.88 → 1108.18] What we humans experience is this is the same thing, right?
[1108.42 → 1111.90] It just translates to proximity of those vectors.
[1112.04 → 1115.62] They are, on average, the values are close.
[1115.74 → 1116.92] They're not identical.
[1117.16 → 1121.12] But if you sum up all the differences, the differences are not large.
[1121.12 → 1125.26] So, as an example of that, we were talking about recognizing our children earlier.
[1125.26 → 1131.92] So, if I'm looking at my daughter at any given point and I have the array of values that represent,
[1132.04 → 1136.44] you know, all of those activations that are occurring, and then I look at her another time
[1136.44 → 1140.84] and those are not the same, and yet I still am recognizing her to be my daughter, is that
[1140.84 → 1142.68] a practical example that would be a place?
[1142.68 → 1143.26] Yes, exactly.
[1143.56 → 1143.82] Okay.
[1144.06 → 1144.70] A hundred percent.
[1144.70 → 1151.00] And if you look at the neural activation of the output of that network, whether it be
[1151.00 → 1156.90] a computer vision network that you trained for, like, facial recognition, or whether it
[1156.90 → 1162.44] be your actual neural network in your brain, the output is going to be similar in the sense
[1162.44 → 1169.10] that most of the neurons are going to have roughly similar activations, right?
[1169.42 → 1169.66] Okay.
[1169.78 → 1172.64] Still, some of them are going to have very different activations because maybe the background
[1172.64 → 1173.18] is different.
[1173.88 → 1177.56] You know, many of them are going to, even those that match are not going to match exactly,
[1177.56 → 1181.14] but on average, it's going to be very, it's going to be close-in, right?
[1181.14 → 1181.30] Okay.
[1181.58 → 1185.62] And so, the very first thing you have to be able to do is take a very, very large collection
[1185.62 → 1187.74] of vectors, billions of them maybe, right?
[1188.34 → 1193.76] And take a new vector and say, okay, give me everything that just correlates with this.
[1194.04 → 1194.40] Okay.
[1194.52 → 1194.76] Okay.
[1195.08 → 1198.94] Has a high correlation with it, or has a low, what's called Euclidean norm.
[1199.08 → 1202.66] So, I sum up all the square differences and take the square root of that.
[1203.06 → 1203.42] Okay.
[1203.54 → 1203.74] Right.
[1204.14 → 1205.50] So, you're normalizing it essentially.
[1205.50 → 1205.86] Yeah.
[1206.28 → 1208.22] Or maybe just think about it as a ball in space.
[1208.32 → 1210.00] So, think about a high dimensional vector.
[1210.32 → 1213.82] You can think about a two-dimensional vector as two numbers, right?
[1213.92 → 1214.08] Okay.
[1214.08 → 1216.04] So, two numbers I can put on an x, y-axis.
[1216.22 → 1217.90] I can plot them on a piece of paper, right?
[1218.24 → 1221.98] So, a three-dimensional vector would be like a point in a three-dimensional space.
[1222.70 → 1225.08] A four dimensional vector is going to be in four dimensional space.
[1225.20 → 1228.00] It becomes a little, kind of hurts your brain to think about it.
[1228.04 → 1229.58] But the math is the same, you know?
[1229.68 → 1232.30] And you can take four to five to a thousand, right?
[1232.62 → 1233.74] And that is exactly the same.
[1233.74 → 1235.34] So, you can think about Euclidean distance.
[1235.98 → 1238.40] Thinking about a ball in two dimension is a circle.
[1238.80 → 1239.02] Yep.
[1239.30 → 1240.88] A ball in three dimension is a sphere.
[1241.46 → 1244.60] And a ball in a thousand dimensions is a ball in a thousand dimensions.
[1244.60 → 1249.28] It's all the points in distance less than something from the centre.
[1249.82 → 1250.16] Okay.
[1250.16 → 1255.48] And you can ask yourself, what are all the points that are in this sphere?
[1255.82 → 1256.12] Okay.
[1256.60 → 1262.66] Which is that all the points whose distance to the image that I'm looking at right now is
[1262.66 → 1263.88] smaller than some threshold.
[1264.36 → 1264.88] Okay.
[1264.88 → 1269.72] Which, if you remember, proximity of those vectors translates to similarity.
[1270.02 → 1270.18] Okay.
[1270.30 → 1271.14] In the real world.
[1271.68 → 1276.38] And so, looking at your daughter, again, this would be converted to a neural signal.
[1276.82 → 1277.08] Okay.
[1277.44 → 1281.20] You will then go to a very large bank of everything you've seen before and say,
[1281.28 → 1283.90] give me everything that looks like this.
[1284.26 → 1286.08] That is similar to this, close to this.
[1286.42 → 1286.56] Right.
[1286.82 → 1290.86] What you would retrieve are mostly your daughter's face.
[1291.32 → 1291.80] Right.
[1291.80 → 1295.64] Which is the answer, in some sense, to what am I looking at?
[1295.88 → 1299.16] So, there's a very different architecture in the sense of, just to draw a comparison,
[1299.70 → 1304.16] if we look at this vector database concept that you're discussing, and for a moment,
[1304.34 → 1308.70] we look back for a moment at the relational databases, and you talked about having those
[1308.70 → 1310.54] strings as IDs and stuff.
[1310.70 → 1315.72] Clearly, we have a significantly different way of retrieving data across those.
[1315.72 → 1320.82] Rather than having an exact match with a specific record, you're looking at generalizing
[1320.82 → 1325.94] across those billions of different records in the vector database for that kind of commonality,
[1326.04 → 1327.62] even if none of them are exact matches.
[1327.94 → 1328.06] Correct.
[1328.76 → 1329.10] Correct.
[1329.20 → 1329.36] Okay.
[1329.66 → 1330.92] And how do you approach that?
[1331.00 → 1332.26] How do you architect such a thing?
[1332.90 → 1333.06] Good.
[1333.34 → 1339.10] So, retrieving or solving this problem efficiently is incredibly challenging.
[1339.10 → 1344.62] And it's also like, it's a very well-known and hard problem because there are tens of open
[1344.62 → 1345.88] source solutions for it.
[1346.18 → 1352.38] Each one of them has many different algorithms with tens of internal parameters and so on.
[1352.44 → 1357.54] And they all excel at different regimes and dimensionalities and statistics of the data.
[1357.54 → 1364.20] And they trade off, like, how often do you miss stuff and how fast it is and so on.
[1364.26 → 1366.08] It's a really gnarly problem.
[1366.66 → 1371.42] For me as a scientist, that's exciting because that means we have hard problems to solve.
[1371.98 → 1375.14] But for practitioners, that's often daunting.
[1375.66 → 1381.24] And so, when you work with something like Pine cone, we can alleviate that.
[1381.42 → 1385.04] We can at the very least delegate that to the experts and just say, hey, you know,
[1385.04 → 1389.30] just do the right thing for my data, I just need to, like, build an application right now.
[1389.38 → 1389.60] Okay.
[1389.84 → 1394.16] Maybe down the line, I would want to choose exactly which algorithm does what.
[1394.26 → 1397.08] And, like, I would want to fine-tune the parameters.
[1397.28 → 1400.10] But for now, just give me kind of the plain vanilla.
[1400.24 → 1402.48] Give me just something that usually works, right?
[1402.76 → 1408.16] So, yeah, the algorithms themselves are, like I said, I'm happy to dive as deep as you want,
[1408.38 → 1410.40] like, all the way down to the nuts and bolts.
[1410.50 → 1413.38] I don't know how much, you know, you want to go there.
[1413.38 → 1415.90] Because I don't think we've said it explicitly.
[1416.32 → 1419.52] Is it fair to say Pine cone is a vector database for machine learning?
[1419.82 → 1420.36] It is fair.
[1420.48 → 1423.06] I think technically that's the right thing to say.
[1423.40 → 1425.58] I think it's also like a search engine.
[1426.10 → 1426.96] It's its own thing.
[1427.04 → 1429.96] I think if you call it a database, it's in some sense an analogy.
[1430.36 → 1431.72] It's also like a search engine.
[1432.06 → 1435.66] Can you differentiate what those two labels, saying database or search engine,
[1436.04 → 1440.28] can you talk about what the implications are for each of those and how it fits in?
[1440.28 → 1443.66] And I will forecast, you don't have to go kind of explain the concepts,
[1443.66 → 1448.96] but I'll also ask you about some kind of use cases on where you might use those in a moment.
[1448.96 → 1451.26] So, if you can kind of conceptually address it,
[1451.28 → 1454.64] and then let's dive into something really practical about how you might do that.
[1454.64 → 1458.80] Sure. So, I think that as a whole, when you tell somebody,
[1458.96 → 1466.12] when just the word database is loaded usually with concepts like joins and analytical workloads
[1466.12 → 1472.08] and like transactivity and consistency, and we don't do any joins,
[1472.22 → 1475.36] but we do care about consistency and persistence and so on.
[1475.42 → 1479.02] So, we have, you know, it requires some properties of a database,
[1479.14 → 1480.30] but it isn't really a database.
[1480.44 → 1482.88] It's definitely not an SQL engine in any way.
[1482.88 → 1483.48] Gotcha.
[1483.84 → 1489.68] A search engine is usually more focused on retrieval of relevant items quickly,
[1490.24 → 1496.58] small set of relevant items quickly, which is much more aligned with what we do right now,
[1496.86 → 1501.10] right? But search engines are also confusing because people really strongly associate them
[1501.10 → 1501.84] just with text.
[1502.10 → 1502.34] Right.
[1502.46 → 1504.20] Right. So, people assume, oh, it's a search engine.
[1504.28 → 1506.40] It's a text. You put in like text queries and, you know.
[1506.62 → 1507.92] Another loaded term, really.
[1507.92 → 1514.02] Right. Exactly. We're just like so branded to think about like Google and Bing and whatnot.
[1514.38 → 1519.18] So, I think both of those terms, like in terms of infrastructure, we overlap a lot
[1519.18 → 1522.14] and we have to provide the same primitives.
[1522.30 → 1525.34] In terms of just terminologies, they're both bad.
[1527.50 → 1529.70] Equally bad and equally good, by the way, you know.
[1529.90 → 1533.00] If you're willing, actually dive into that a little bit. I'm really curious.
[1533.00 → 1537.60] I'm fascinated by this because it's something I don't know much about. How do you store the data?
[1538.08 → 1542.66] We've talked about the storage a little bit, and we've talked about retrieval. What does that look
[1542.66 → 1546.30] like? You know, as you said that you can kind of dive a little bit, dive for us a little bit and
[1546.30 → 1550.58] tell us, you know, because I think when people think databases and search engines, as you just
[1550.58 → 1555.66] pointed out, they have a preconceived idea in their mind. How do you implement those terms?
[1555.68 → 1559.96] When you're taking the phrase database and the phrase search engine, and you're saying,
[1559.96 → 1564.98] it's not the way you were thinking before, what's different about it? Tell us a little bit about
[1564.98 → 1565.86] what that looks like.
[1566.28 → 1572.42] So, first, because of the nature of the data, basically the only way to implement this
[1572.42 → 1576.52] efficiently is to have everything in memory. Okay. So, first, we're an in-memory database.
[1576.86 → 1577.08] Okay.
[1577.54 → 1584.38] The second thing is that retrieval, okay, so there's like similarity search or nearest neighbour search,
[1584.38 → 1590.20] it's also called, this retrieval of close vectors or correlated vectors from a very large collection,
[1590.56 → 1598.70] is a very compute-heavy operation. Okay. You really have to oftentimes touch and do some basic
[1598.70 → 1604.38] computation on very large portions of your data. So, this is a compute-heavy process. Like, of course,
[1604.46 → 1610.38] the goal of the infrastructure is to make it as lightweight as possible, right? But it still is
[1610.38 → 1616.20] significantly more tasking. So, let me kind of maybe explain very roughly how you'd even approach
[1616.20 → 1617.98] such a thing. Okay.
[1617.98 → 1622.42] I'm going to try to convince you that you can think about a thousand-dimensional space like a
[1622.42 → 1624.14] three-dimensional space right now. Okay.
[1624.14 → 1626.06] Okay. I'll buy into it. I'll try.
[1627.14 → 1632.12] You know, I'm going to put warning signs where the math doesn't work. But for most concepts,
[1632.30 → 1638.74] the math kind of, the intuition is actually okay. Okay. So, the first thing you want to do is to
[1638.74 → 1646.00] be able to just carve out chunks of space and to say, oh, if I'm here, then my close neighbours are
[1646.00 → 1653.10] usually within the same part of the space, right? So, think about partitioning the universe into,
[1653.10 → 1657.06] like, galaxies and, you know, like, solar systems and so on. So, you say, oh, you know,
[1657.56 → 1661.64] maybe it's good to start searching for my nearest star in my galaxy, right?
[1661.76 → 1662.00] Sure.
[1662.22 → 1663.16] It's a good guess, right?
[1663.28 → 1663.46] Right.
[1663.46 → 1669.06] So, usually you'd have a partitioning of the whole set of points into these, like, clusters,
[1669.74 → 1674.42] right? Such that in real time, you have to figure out, oh, I'm not going to search everything. I'm
[1674.42 → 1681.70] just going to search through these subsets of clusters. These are the areas of space that are
[1681.70 → 1687.74] going to more likely contain my memories, like the thing that, like, the closest neighbours, right?
[1687.74 → 1688.22] Sure.
[1688.58 → 1694.18] Within those clusters, you have a more compute-heavy process that actually kind of combs
[1694.18 → 1699.78] through everything, right? And figures out what's close. But it does that very efficiently. It
[1699.78 → 1706.38] doesn't actually compute everything. It kind of has very, very efficient rules to kind of discard
[1706.38 → 1711.90] things that are not really close, right? So, you kind of have to raise the flag when you see something
[1711.90 → 1717.74] that's suspicious. Like, oh, this is, like, maybe highly correlated, but you have to rule out things
[1717.74 → 1722.50] that are not relevant very, very quickly. So, you have this, like, second comb of everything that
[1722.50 → 1727.68] rules out everything that's impossible, that's irrelevant, and just leaves a small look, an even
[1727.68 → 1734.40] smaller candidate set. And then you have a final layer that just goes over that and really fine
[1734.40 → 1738.52] combs through and really does compute all the distances. Oh, you know what? From those,
[1738.52 → 1745.16] you know, here are the actual, like, 10 or 100, most of the 11 points. Now, if that process sounds
[1745.16 → 1748.90] like lossy to you, that you might actually have missed something, you're absolutely right.
[1749.34 → 1754.24] It's not foolproof. And so, that's one of those properties that people kind of are confused about
[1754.24 → 1758.76] or surprised about with the analogy to the database. What do you mean it's not always accurate?
[1759.16 → 1762.98] Yeah, you're missing, you know, in that relational world, which is addressing a different
[1762.98 → 1767.76] problem. You don't have that exactness that you have with those IDs tied to something. It's a
[1767.76 → 1772.86] different thing you're trying to achieve here. Right. And so, you kind of have trade-off between
[1772.86 → 1779.08] how quickly you need to retrieve the results versus how accurate you want them to be, right?
[1779.50 → 1784.98] Because I can just fine comb through everything. Like, I can just decide to just brute force that
[1784.98 → 1790.36] just kind of search my entire memory, you know, front to back. That will take an hour, but it would
[1790.36 → 1795.82] be 100% accurate. Yeah. Or you can be very, very picky. So, I'm not going to, you know, I'm going to
[1795.82 → 1799.78] set all my thresholds really high. I'm not going to touch anything unless it's like very likely a
[1799.78 → 1805.42] good match. Well, you might miss some stuff, but it's going to be very fast. And so, and not only
[1805.42 → 1809.50] not getting in the point that there are like 5,000 different ways to do each one of those three
[1809.50 → 1816.44] stages. Yeah. I think that's maybe as deep as we want to go, but you can see how that is very,
[1816.56 → 1821.40] very different from like a key value lookup or a B-tree. It's just a whole different thing.
[1821.40 → 1827.42] That was a perfect explanation. I truly have that now in my head as to what the difference is.
[1827.88 → 1833.54] I know that there are lots of different ways to apply that in the real world to get productive
[1833.54 → 1840.36] solutions. Could you talk a bit about different areas that you can take this technology that you
[1840.36 → 1845.52] have at Pine cone, the vector database technology and the retrieval, and where will we put that to
[1845.52 → 1848.24] get value out of it in the world and to help us solve our other problems?
[1848.24 → 1853.82] So, interestingly enough, we can talk about very concrete situations, very concrete solutions.
[1854.00 → 1860.22] Some of them built with Pine cone, some of them built by big companies building their own technologies.
[1861.14 → 1868.64] And frankly, we as consumers of technology, we use these algorithms all the time. If you use Facebook,
[1869.32 → 1877.70] your feed is ranked by the embedding that Facebook has of you as a user. All of your
[1877.70 → 1885.42] tendencies and interests and everything are encoded as a high dimensional vector. And the topics and
[1885.42 → 1889.90] contents of a piece of content, whatever it is, like a piece of text or an image or whatnot,
[1890.66 → 1896.00] is encoded in the same way. And the ranking is decided based on the similarity of those encodings,
[1896.20 → 1901.58] right? The same is true for pretty much every social network out there. It's the same way in
[1901.58 → 1908.26] LinkedIn and so on. If you search on Google, you know, if you just search any long query,
[1908.60 → 1911.22] right? That doesn't match directly like word to word.
[1911.66 → 1911.88] Yeah.
[1912.14 → 1917.58] You might be looking for an answer to something that the right page that contains the...
[1918.48 → 1924.58] So, you type the question, but oftentimes the answer doesn't contain the question verbatim,
[1924.58 → 1926.92] right? It just contains the answer. Yeah.
[1927.72 → 1934.54] You know? And so, like text search doesn't make any sense. Like you shouldn't be looking for the
[1934.54 → 1940.38] words in the query. So, what should you be looking for? And what you're looking for is an encoding of
[1940.38 → 1948.68] the query with NLP models into a high dimensional vector. And you're searching through the web where each
[1948.68 → 1955.98] paragraph was also encoded into high dimensional vectors such that, you know, it's still close if
[1955.98 → 1960.82] the paragraph might have contained the right information or the answer to that query. And
[1960.82 → 1967.40] same in retail recommendation for shopping, same as threat detection, anomaly detection,
[1967.66 → 1970.68] you name it. I mean, in some sense, all of it works this way nowadays.
[1971.18 → 1976.16] I'm going to kind of throw something in kind of randomly. Could you think of it as a proxy
[1976.16 → 1982.16] for identifying intent possibly in some of these cases by comparing high dimensional vectors
[1982.16 → 1987.46] to where, you know, what Facebook wants to know, or what Google wants to know is what is my intent
[1987.46 → 1992.58] with my search? Less about the exact words I'm using and more about what is Chris Benson trying
[1992.58 → 1998.44] to get to? What is that thing that he's trying to unlock? Is intent one of the possible things that
[1998.44 → 2004.70] it's proxying for there? So, the main question is basically what do your embeddings represent?
[2004.70 → 2010.50] You train those models, you know? We talked about vision a lot in this session, you know,
[2010.60 → 2015.68] that probably encodes like visual similarity. But when you do feed ranking, then yeah, I mean,
[2015.74 → 2021.04] you would encode for intent and interest. When you do for maybe search, it would be more intent,
[2021.20 → 2025.46] maybe. And feed ranking is more like interest or maybe also intent. I'm not even sure.
[2025.46 → 2033.14] Yeah. So, yeah, I mean, those are, it's, you can encode a lot of semantically deep properties of the
[2033.14 → 2039.16] object that you're using, whether it be, you know, person's actions on your website or an image or a
[2039.16 → 2041.16] piece of text. I mean, it's the same in some sense.
[2041.58 → 2046.14] Okay. Well, let me ask you another question. With a lot of folks listening to us here being
[2046.14 → 2050.62] practitioners and, you know, in their day job, they're maybe creating convolutional neural networks.
[2050.62 → 2055.00] They might be involved in NLP, like my co-host Daniel is, you know, deeply all the time.
[2055.56 → 2061.74] Are there certain algorithmic approaches within deep learning that vector databases and retrieval
[2061.74 → 2066.96] lend themselves to more than others? Or is it more, it can be used across any of these different
[2066.96 → 2071.32] algorithms? Should people always be thinking about it? Or are there certain areas where it will be
[2071.32 → 2072.40] more productive than others?
[2072.40 → 2077.94] I think they can be applied pretty widely, but there are patterns. So, you know, you said Daniel
[2077.94 → 2083.44] is an NLP practitioner. I saw you interviewed the folks from Hugging Face, for example. So a pattern
[2083.44 → 2090.76] that we see is people use models like Hugging Face, like Bert and others to transform their text to
[2090.76 → 2097.26] high dimensional vectors and maybe just produce semantic search on top of their corpus of documents
[2097.26 → 2102.46] with an engine like Pine cone, right? So they would say, I would, instead of encoding,
[2103.02 → 2108.12] taking the tokens and putting them in Elasticsearch, I would convert them to high dimensional vectors
[2108.12 → 2113.12] and put them in Pine cone and search through the vectors themselves. And then I'll be searching
[2113.12 → 2118.92] through the semantic meaning of the document rather than the words themselves, right? That is very common.
[2119.44 → 2125.40] Now, usually if you do just that, exactly what I just said, you don't get the best results.
[2125.40 → 2130.32] You probably want to tweak your algorithm or retrain it, or you might need to do a few extra steps.
[2130.70 → 2135.16] But even if you do just that, you already get something interesting, which is very different
[2135.16 → 2137.98] than traditional text search, right?
[2138.22 → 2144.04] Can you also maybe give us what your kind of your classical or whatever feels right to you,
[2144.22 → 2149.88] but kind of classical workflow. So if somebody is out there, and they're using TensorFlow or PyTorch or,
[2150.12 → 2154.30] you know, whatever the tool that they want to use, and they're listening to this, and they're
[2154.30 → 2157.48] starting to think, oh, I definitely need to incorporate this into my workflow.
[2158.02 → 2162.84] How do they do that? How do people start to get Pine cone and take advantage of that
[2162.84 → 2166.44] in doing whatever they're doing? What does it look like in a very, you know,
[2166.76 → 2168.76] fingers on the keyboard practical sense?
[2169.28 → 2173.00] It's incredibly simple. So we offer Pine cone as a fully managed service.
[2173.72 → 2178.86] And so all it takes is like asking for an API key on the website, which is free,
[2178.86 → 2184.32] and you get it like a minute later in your inbox. And after that, you can literally go to our
[2184.32 → 2190.68] tutorial section and run notebooks and go play with, you know, all the APIs and all the capabilities
[2190.68 → 2197.44] are open to you. You know, after a few weeks, you can either, you'll probably decide whether that's
[2197.44 → 2203.18] the right tool for you to use, right? Most projects end up being like very cheap to be able to run
[2203.18 → 2210.48] sustain workload. Usually less than a hundred bucks a month is typical for most like non-enterprise
[2210.48 → 2214.70] users. And yeah, I mean, it's right there, and it's available to you. You can use it as a like
[2214.70 → 2220.68] microservice in your application or as a part of like your developer pipeline. Yeah. All the APIs
[2220.68 → 2223.68] are open. They're all documented. They're pretty simple in my opinion.
[2224.32 → 2228.94] Very cool. So I'm curious, I want to go back for a moment. You were talking about some of the social
[2228.94 → 2235.08] media applications, you know, with Facebook. Are there any other areas specific to call out that
[2235.08 → 2239.88] are really notable for using these technologies? Are there any things that people might go, oh,
[2239.98 → 2243.04] I hadn't thought about, you know, the fact that this makes sense to use there.
[2243.26 → 2244.96] Yeah. Any other use cases to call out?
[2245.68 → 2251.66] So we definitely see text embeddings a lot, especially because that the models for embedding
[2251.66 → 2257.78] text are quite easy to get a hold of, and they're pretty good already. We do see that with images,
[2257.78 → 2264.00] searching for images, searching for near duplicates of images for fraud, for social networking and so
[2264.00 → 2269.30] on. So people, you know, upload, you know, maybe slightly more of images you might already have
[2269.30 → 2274.88] in your network, and you just want to flag that. Right. So think about like, I've seen this before
[2274.88 → 2281.66] function, right. But it's not the same file. It's just a slightly distorted or slightly intentionally
[2281.66 → 2289.62] changed image, right? We see that with fraud and like kind of fraud and anomaly detection are very
[2289.62 → 2296.30] heavy use cases where you encode some normal behaviour and then like in real time, you'd retrieve,
[2296.48 → 2302.16] you know, out of a hundred million events that I've seen, you know, does this kind of look like
[2302.16 → 2308.68] a good thing or a bad, you know, what does this look like, you know, and should I be looking at this
[2308.68 → 2315.52] now? Should I flag this to my analysts or whatnot? I think those are the main patterns, but, and
[2315.52 → 2319.86] recommendation, by the way, and I forgot to say recommendation and personalization are a big thing
[2319.86 → 2326.66] for shopping, for social networks and so on. I think those are kind of the main four, if I had to guess,
[2326.80 → 2332.36] but I'm probably missing something. Sounds good. As we wind up here, I want to take us back for a
[2332.36 → 2337.62] moment to something you said early on. And you talked about how we were early on in the stage as we're
[2337.62 → 2343.12] starting to move into this new way of approaching technology solutions. And, you know, this is early
[2343.12 → 2348.50] days. And as someone who is working in this field, you know, all day, every day and building your
[2348.50 → 2353.50] company based on these technologies, where do you think it will go and what would you like to see?
[2353.82 → 2360.58] And how will this set of technologies evolve in the years ahead in your view? What do you,
[2360.74 → 2363.90] when you're thinking, when you're laying at bed at night before you go to sleep, and you're thinking,
[2363.90 → 2367.50] that's the thing I'm aiming for down the road? What does that look like?
[2367.86 → 2373.58] It's a fantastic question. I think that it's hard to pinpoint exactly. Again, I was trained as a
[2373.58 → 2379.96] scientist. We started off by talking about my meandering trip through my PhD. I think my
[2379.96 → 2386.42] professional life is sort of like a scaled out version of the same, you know? I personally try to
[2386.42 → 2392.80] push the boundary and try to figure out what's kind of what's the next huge milestone we as a society can
[2392.80 → 2399.62] hit. For Pine cone specifically, you know, for us as a community, I think that really starting to think
[2399.62 → 2406.26] about not only the model that I trained and how do I put it in a container and ship it to some place in
[2406.26 → 2415.84] my app, but rather like, okay, we now have this like just complete wealth of data that we can now use.
[2415.84 → 2424.42] And how do we integrate intelligence with, you know, compute and memory, you know, and storage?
[2424.54 → 2431.04] How do we make that behave a lot more like a brain and not like a neural net, you know? And I think that
[2431.04 → 2438.82] we are many years away from that. One of my favourite books on AI has this quote that says that saying that
[2438.82 → 2444.42] humanity is getting close to a general AI is like saying a monkey climbing a tree is getting close to the
[2444.42 → 2450.78] moon. I hadn't heard that, but that's good. You know, it's true. It's true technically. So I don't
[2450.78 → 2457.16] know if we're as hopeless as that monkey climbing the tree in getting to the moon, that is, but we are
[2457.16 → 2462.64] very, very far away. It's far away when we look at application when you really dig in, and you try to
[2462.64 → 2467.32] solve even very basic problems. You understand how little we know. Like we don't even know how to train
[2467.32 → 2473.54] neural nets. So I'm going to spin that in a way that I think that that's going to make for a lot of
[2473.54 → 2478.44] great episodes for us to talk about. We'll have to have you back on the show to discuss some of
[2478.44 → 2483.54] those steps along the way there. I'm happy to do that. Well, you know, thank you so much for coming
[2483.54 → 2487.36] on Practical AI. It's been a really fascinating conversation. I have learned a lot personally,
[2487.36 → 2492.10] and I appreciate you answering all these questions I have for you. So thanks. And I hope to have you on
[2492.10 → 2493.68] again sometime. It's a lot of fun. Thank you, man.
[2493.68 → 2502.22] Thank you for listening to Practical AI. We appreciate your time and your attention. If you
[2502.22 → 2507.70] enjoyed this episode, help us out by spreading the word. Think of a friend, think of a colleague,
[2508.00 → 2512.14] somebody who would benefit from listening to it, and send them a link. We'd really appreciate it.
[2512.50 → 2518.72] Practical AI is hosted by Chris Benson and Daniel Whiten ack. It's produced by Jared Santo with music by
[2518.72 → 2523.20] Break master Cylinder. Thanks again to our sponsors, Vastly, Linde, and Launch Darkly.
[2523.38 → 2527.30] That's our show. We hope you enjoyed it, and we'll talk to you again next week.
[2527.30 → 2557.28] We'll see you again next week.
