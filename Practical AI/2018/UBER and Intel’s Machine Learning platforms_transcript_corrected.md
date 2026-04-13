[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com, and we're hosted
[11.42 → 17.36] on Linde servers. Head to linode.com slash changelog. This episode is brought to you by
[17.36 → 23.72] DigitalOcean. They now have CPU optimized droplets with dedicated hyper threads from best in class
[23.72 → 29.18] Intel CPUs for all your machine learning and batch processing needs. You can easily spin up
[29.18 → 34.74] their one-click machine learning and AI application image. This gives you immediate access to Python 3,
[35.20 → 42.68] R, Jupyter Notebook, TensorFlow, Sci kit, and PyTorch. Use our special link to get a $100 credit for
[42.68 → 51.30] DigitalOcean and try it today for free. Head to do.co slash changelog. Once again, do.co slash changelog.
[59.18 → 68.60] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[69.02 → 74.52] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[74.56 → 78.66] and data science happen. Join the community and snag with us around various topics of the show
[78.66 → 84.48] at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[89.18 → 93.94] Cormac, thanks for joining me here at O'Reilly AI. It's great to have the chance to talk to you. I
[93.94 → 98.38] know you just got out of your talk a little bit earlier. You talked about portability and performance
[98.38 → 103.52] in embedded deep learning. Can we have both? So I want to dig into that a little bit more later,
[103.52 → 108.52] but first I'd love to hear. I know you work and help lead the Movies group at Intel,
[108.70 → 113.40] and I'd love for you to just kind of let the audience know what Movies is, if they haven't heard
[113.40 → 117.16] about it, what you're doing, and what you're working on now. Yeah. Hey, thanks, Daniel. And yeah,
[117.16 → 123.02] good to talk. I guess, yeah, my name is Cormac Brick. I lead kind of CPU architecture at Movies
[123.02 → 128.48] as part of Intel. CPU for us is a kind of visual processing unit, and that's the kind of the key
[128.48 → 133.12] engine we have in our kind of product line. So yeah, I kind of lead that architecture. And at
[133.12 → 138.32] Movies, we're very passionate about, you know, machine learning and computer vision at the edge.
[138.70 → 142.26] This is something we've been at for a long time, going back, you know, kind of five, six years,
[142.26 → 146.08] even before we were part of Intel. And we have kind of multiple products now in the field.
[146.08 → 151.78] And yeah, we've learned a lot as a result of all of that interaction with customers over the years.
[152.46 → 157.26] And yeah, the goal of the talk this morning was to really kind of reflect some of that
[157.26 → 164.14] knowledge, as in what have we learned about, you know, tuning neural networks for embedded silicon,
[164.58 → 168.36] and then also tuning embedded silicon for neural networks, right? To kind of just reflect
[168.36 → 174.24] what some of the realities are when you go to take a network to the edge, what's kind of really
[174.24 → 180.06] required to make that run really, really well. Awesome. Yeah. So just to kind of dig into that
[180.06 → 185.38] a little bit deeper, when you're talking about, you know, customers that are tuning neural networks
[185.38 → 190.28] for the edge on things like CPUs, which you mentioned, what are some of the kind of customer
[190.28 → 194.90] use cases around this and people that have found a lot of value in going down that road?
[194.90 → 202.08] Yeah, sure. So we at Movies, like we have customers who are engaged heavily in things like
[202.08 → 208.88] digital security and kind of smart city type use cases, where really making more intelligent cameras.
[209.34 → 214.54] That's that's one big use case. We've also shipped a lot of products on drones. That's another use case,
[214.54 → 221.28] as well as a lot of things around, you know, robotics and smart devices and camera devices as well.
[221.28 → 225.62] So, you know, there are things like the Google clips products that's on the market now that uses our
[225.62 → 232.56] kind of Myriad 2 silicon. A lot of the DJI drones have used the Myriad 2 silicon as well. And they
[232.56 → 237.30] have things like you can wave at the drone using your hands to control it and then protect your palm
[237.30 → 241.74] and the drone can land on the palm of your hand. So really, really compelling use cases that have
[241.74 → 246.36] been enabled through our silicon through the use of, I guess, both vision and AI kind of working hand in
[246.36 → 252.16] hands. Awesome. Yeah. And just to kind of confirm that I was actually at Gopher Con last week and one
[252.16 → 257.04] of the keynotes, I think on the second day or something, they used the drone with a Myriad chip
[257.04 → 263.32] in it to do some facial recognition and all of that is some cool stuff. So let's kind of dive into a
[263.32 → 268.08] little bit more about what you talked about. Is there in these types of use cases where you're wanting
[268.08 → 274.24] to run your neural network in a drone or in a camera or whatever it is, explain a little bit the
[274.24 → 279.62] tension between kind of portability and performance that we've seen in the past and the state of it now?
[280.04 → 286.34] Yeah, sure. So I guess what we've seen is a lot of, you know, if you go on Archive or if you go to
[286.34 → 292.06] NIPS or clear or this sort of conferences or CVP or like leading academic vision conferences, we'll bind
[292.06 → 297.46] of find there that people are, there's a lot of work being done to kind of optimize neural networks for
[297.46 → 303.50] things like kind of ImageNet or MS Cocoa or kind of academic data sets. And that's awesome in terms of
[303.50 → 308.54] pushing the envelope of the fields and, you know, advancing the science, and it's moving superfast,
[308.62 → 313.10] right? So then, you know, typically when embedded engineers will start off a problem, they've access
[313.10 → 316.68] to that sort of research and this sort of models. And then they kind of want to do something that's
[316.68 → 320.92] going to work for them and their device, right? And one of the things they would find is a lot of
[320.92 → 324.88] the models that are available out there were tuned on ImageNet, which is great at recognizing,
[324.88 → 329.60] you know, a thousand classes of images, you know, and it can differentiate one sort of
[329.60 → 333.68] whale from a different type of porpoise and this sort of stuff, right? Very, very fine-grained
[333.68 → 335.68] classification on specific tasks.
[335.68 → 336.32] Important problems, yeah.
[336.32 → 340.72] Yeah, not so much in the real world, right? We have different problems to solve. So then in the
[340.72 → 345.44] real world, we may care about, hey, like my robot wants to be able to recognize, you know,
[345.44 → 350.48] a hundred common objects found in the home or with this sort of, in this security camera,
[350.48 → 353.76] we want to be able to recognize these different types of objects that are happening.
[353.76 → 358.72] Yeah, so different problems. And often those problems are simpler than the thousand class problem
[358.72 → 362.80] from ImageNet. So one of the things we were talking about this morning is using techniques
[362.80 → 368.88] like model pruning and scarification to, you know, if you're doing what we would call domain
[368.88 → 373.52] transfer, so you go from your thousand class problem, you know, let's say if you were taking Reset 50,
[373.52 → 378.08] and you're now retraining that for your home robot, which wants to recognize a hundred images,
[378.08 → 383.28] you'll find that you can get away with a much simpler network with less representational capacity
[383.28 → 386.96] to solve that hundred image problem than the one you started off in the thousand image problem.
[386.96 → 391.12] So we were sharing some results in some techniques specifically around channel pruning,
[391.12 → 396.08] which is very, very powerful technique when you are doing domain transfer to a simpler problem domain,
[396.40 → 401.76] and also looking at techniques like scarification, which is introducing more zeros into a neural network,
[401.76 → 408.16] because that's great in terms of on platforms that support, you know, memory compression
[408.16 → 414.40] of neural network models. It'll enable those models to run much faster in bandwidth limited
[414.40 → 417.68] devices such as those typically found on the edge.
[417.68 → 418.56] Yeah.
[418.56 → 423.68] Awesome. So in terms of like, let's say that I'm working on, you know, I'm working on one of these
[423.68 → 429.20] robotics problems or whatever it is, and I'm using a neural network and I want to pursue some of these
[429.20 → 434.64] methods to kind of prune it down or optimize it for that setting or for that architecture.
[434.64 → 439.36] What's kind of the process and the barriers that I would face as of now going into that? And what's
[439.36 → 443.76] kind of the state of the usability of these tools and that sort of thing?
[443.76 → 448.96] Yeah, that's a great question. Because for sure, we were presenting a lot of work this morning
[448.96 → 453.68] saying, hey, you know, we're able to take a network and do this sort of pruning and quantization and
[453.68 → 457.92] scarification and then go from eight bit weights to four bit weights and this sort of stuff.
[457.92 → 462.32] But, you know, straight up today, pretty non-trivial to repeat the results that we were kind of showing
[462.32 → 467.84] this morning. To bridge that gap, you know, working, we now work in Intel as part of the AI
[467.84 → 471.76] products group. As part of the Intel AI products group, there is an open source project called
[471.76 → 477.52] Distiller. It's one of the resources listed in my slides, I think on the final slide, and I believe
[477.52 → 479.60] they'll get posted to O'Reilly at some point.
[479.60 → 481.52] Yeah. We'll put them in the show links here as well.
[481.52 → 486.08] So yeah, there's a link to something in GitHub called Distiller. And there, one of the things we're
[486.08 → 490.24] doing is, you know, if you went back maybe kind of 12 months ago, you'd have found, oh, like,
[490.24 → 494.64] this is an awesome quantization technique that somebody published, you know, some grad student
[494.64 → 499.36] kind of put this, you know, published a PyTorch fork or something with this, right? And then here's
[499.36 → 503.52] something else that was available in TensorFlow for quantization. And here is something else that
[503.52 → 507.76] was available in a different framework. What we were doing is really kind of taking all of those
[507.76 → 513.52] techniques that are available in a fairly fragmented way across the internet and trying to put them,
[513.52 → 518.48] you know, under one roof in a way that's kind of a little bit easier to access. And that was kind of
[518.48 → 523.04] the goal of the Distiller project is really to show that. And it's an ongoing project at Intel
[523.04 → 530.32] within AIG to have this kind of set of tools. So they were available in PyTorch. And that's great
[530.32 → 535.44] because PyTorch can export to Onyx, which is then widely available. But in addition to the work we're
[535.44 → 540.00] doing, it's entirely appropriate though to give a shout-out to the work the TensorFlow team are doing.
[540.00 → 545.76] So there's under TensorFlow cont rib. Yeah, there are a bunch of useful tools there on both quantization
[545.76 → 551.36] and on pruning as well, right? And there's a pretty strong ecosystem there also showing a variety of
[551.36 → 557.60] techniques. Okay. Yeah. So it is at least to a point where I could, you know, get a model off of
[557.60 → 564.64] some repository, maybe in PyTorch or wherever, and have some tooling that's publicly available to
[564.64 → 569.84] to prune that down for certain architectures. Yeah. Yeah. What about prepping the model for
[569.84 → 575.88] certain maybe specialized hardware? You mentioned like CPUs. And I know there's a lot of other people
[575.88 → 581.40] pursuing things around, of course, GPUs, but also FPGAs and other things. What is kind of the state
[581.40 → 585.70] of the art? Are this kind of pruning methods and all of that tied into that world? Or is that
[585.70 → 591.26] something totally separate? Yeah. And that's also a good question. And it was one of the kind of the
[591.26 → 598.00] goals of the talk today was to show that, hey, you know, here's kind of four key techniques that
[598.00 → 604.14] you can use that will work well on any hardware. And on some hardware will work extra well. But if you
[604.14 → 608.70] employ these techniques, you're not going to hurt your model's ability to run across a broad range
[608.70 → 614.04] of silicon, right? So those techniques specifically are kind of model pruning, scarification, using
[614.04 → 618.84] fewer, using, you know, quantizing a network to eight bits, and then doing further quantization on
[618.84 → 622.78] weights to use kind of a lower bit depth, right? So if you employ this kind of four techniques,
[623.18 → 627.54] you will still have a model, you know, if you take a model, and you represent it in Onyx or in
[627.54 → 632.38] TensorFlow, you'll still have a model that can work well on a wide variety of devices. But on some
[632.38 → 636.80] devices, it's going to work extra well, right? Because different silicon will have different
[636.80 → 642.30] abilities to run quantized models, you know, at varying degrees of acceleration. And also different
[642.30 → 646.98] silicon will have varying degrees of, let's say, weight compression and technology.
[646.98 → 652.62] So, and even in extreme cases, you know, for sparsity, there's some silicon out there that can
[652.62 → 658.36] process sparse networks directly and in an accelerated fashion, right? So, again,
[658.44 → 662.66] so a variety of silicon, you can employ these four techniques and get really, perfect results
[662.66 → 666.54] across a range of silicon and even better results in some silicon. So that was the core point, right?
[666.82 → 671.42] But to answer the second part of your question, in the final slide, we're making the point as well
[671.42 → 678.30] that, hey, if you set out to have a single network, and you know the piece of silicon you're running on,
[678.52 → 683.94] absolutely, there are other techniques you can employ to really fit that piece of silicon as best as you
[683.94 → 688.42] can to really make this one network shine on this combination of this network and this silicon.
[688.74 → 692.28] And there's been some very interesting work published on that in the last couple of months.
[692.48 → 697.56] And it's a pretty, pretty hot research topic now is showing how to like using, you may be familiar
[697.56 → 701.56] with kind of auto ML, right? So being able to use that type of techniques to kind of,
[701.66 → 706.96] to refine a model or to learn a model that works really, really well on a particular version of
[706.96 → 711.72] silicon with these types of performance claves and trade-offs. Yeah. So it's a that's a pretty
[711.72 → 716.76] active area of, of research that's pretty interesting. Awesome. Awesome. And I know that,
[716.88 → 721.78] uh, one of the things that I've appreciated as kind of like, uh, as I'm hacking on things at home is
[721.78 → 726.54] that, you know, a lot of the stuff that you've come out with through Movies makes it really easy to
[726.54 → 731.04] experiment with, you know, neural networks on, on a lot of different types of devices through like
[731.04 → 735.52] the, uh, neural compute stick and other things. I was wondering if you had any, um, interesting
[735.52 → 741.62] stories or, uh, customer experiences that you've heard about of, of people enabling new sorts of
[741.62 → 746.30] things with these devices. Yeah. We really enjoyed the experience of launching the first version of
[746.30 → 750.70] the neural compute stick based on Myriad 2. And it was great to get out there and meet lots of developers.
[750.98 → 755.66] And also, you know, when we launched that, I guess it was kind of, we announced it some time before
[755.66 → 761.22] and we really launched it then at CVPR last year. Yeah. It was great to see what everybody was
[761.22 → 764.96] doing, but also to kind of show them, Hey, you know, AI at the edge is possible, right? If you
[764.96 → 769.92] go back 15 months, people, you know, or two years ago, people really associated AI with the cloud,
[770.00 → 775.20] right? So, so our first goal was to kind of, you know, break down those, the perceived barriers and
[775.20 → 780.00] for people to, and, and for more people to be able to use AI and to see, Hey, AI at the edge is
[780.00 → 784.18] possible, right? So that was our initial goal. And it was great experience, very enjoyable talking to all the
[784.18 → 790.06] developers. A couple of things we've seen, we've seen, we've seen people use this, one of the
[790.06 → 796.20] software ambassadors for Intel use this to do, to do a prototype kind of water filter. So kind of
[796.20 → 802.74] taking a the guts of a microscope, putting that up to a camera into a Raspberry Pi with the video's
[802.74 → 808.06] neural compute stick connected and being able to show that you could actually use this to detect
[808.06 → 815.32] water impurities. So to have an entirely offline water impurity detection device that could be used,
[815.46 → 820.24] you know, effectively like on premises, you know, at the edge with no cloud connection or anything
[820.24 → 824.62] like this, super cool idea, right? And be able to show that that's possible. Equally, we have people
[824.62 → 829.80] putting them on a drone to detect sharks in the water, also doing kind of prototype medical imaging
[829.80 → 835.12] to detect melanoma on skin, also kind of driven by image classification. And yeah, so there,
[835.12 → 840.10] there are just a few things, but there's been a lot of others, you know, fun projects posted on GitHub.
[840.44 → 845.82] And I don't have a link to our model zoo site and example site, but I can provide you with them for,
[845.94 → 850.60] for the blog page also. Awesome. Yeah. Well, we'll make sure that gets in our show notes for sure.
[851.00 → 854.96] Yeah. Well, I appreciate you taking time again, kind of to wrap things up here. I was wondering,
[855.06 → 858.44] you know, from your perspective, since you've been working in this space for a while,
[858.76 → 863.66] what can we look forward to, you know, over the next couple of years with performing AI at the edge?
[863.66 → 867.56] What are you excited about, and what do you think we'll see over the next couple of years?
[867.98 → 872.82] Yeah, I think, I think we're definitely going to see a lot more silicon become available,
[873.06 → 877.44] both from, both from the videos Intel, also from a bunch of competitors. And I think that's going
[877.44 → 882.24] to be fascinating as inference silicon, you know, there's kind of metrics business people
[882.24 → 887.28] would track like the number of like ops per watt we can deliver or the number of ops per dollar
[887.28 → 893.30] we can deliver. And we'll expect both of those metrics to progress at a really, really fast pace
[893.30 → 897.22] over the next number of years. And if I look at what people are able to do with the first version
[897.22 → 902.54] of the neural compute stick with the capabilities that has, and while I can't disclose product
[902.54 → 907.02] roadmaps with some visibility of the type of things we're going to see in terms of the volume of compute
[907.02 → 912.26] we can, that various people can bring to market at much lower price points and much lower power
[912.26 → 916.50] points, I'm really excited to see what's, how that's going to play out and the type of things
[917.28 → 919.98] that I think it's going to be very exciting space to watch in the next few years.
[920.30 → 923.68] Awesome. Well, thank you again for taking time and enjoy the rest of the conference.
[923.86 → 924.24] Thanks Tyler.
[933.12 → 937.92] I'm Tim Smith and my show away from keyboard explores the human side of creative work.
[937.92 → 943.90] You'll hear stories sometimes deeply personal about the triumphs and struggles of doing what you love.
[944.24 → 947.08] Jumping off into the abyss is kind of my skill.
[947.28 → 954.94] And so I'm not saying that it's not scary. I'm saying that perhaps my skill is just not
[954.94 → 957.80] being able to estimate how scary it will be.
[958.36 → 960.56] New episodes premiere every other Wednesday.
[960.90 → 965.20] Find the show at changelog.com slash AFK or wherever you listen to podcasts.
[965.20 → 983.64] Well, thanks for joining us, Mike. It's great to chat with you and meet you here at O'Reilly AI.
[983.86 → 987.82] I've heard about Michelangelo, this ML platform that you guys have developed at Uber.
[988.20 → 991.98] And I'd love to hear a little bit more about it. But first, give us a little background of who you are,
[991.98 → 993.12] or how you ended up where you are.
[993.12 → 998.84] Yeah, thanks. Happy to be here. Yeah, so I currently am the product lead for ML infrastructure at Uber.
[999.38 → 1004.74] And that encompasses a lot of things, most notably the Michelangelo platform.
[1005.06 → 1008.98] A little bit of background on me is I'm an electrical engineer by training.
[1008.98 → 1016.68] And out of school, I worked at Google. And one of the kind of places I got my ML chops, so to speak,
[1017.00 → 1022.78] which is weird to say, is I worked on the ads team at Google, specifically the ads auction group.
[1023.04 → 1029.44] And I was the product manager for all the ML signals that go into the ads auction there.
[1029.44 → 1036.70] So these really like real-time, high-scale, super-productionized ML systems that predict if you're going to click an ad,
[1036.82 → 1039.68] and if this ad's going to be relevant and stuff like that.
[1040.02 → 1047.60] So that's kind of like where I learned how to do ML right, and probably best in industry in terms of productionized machine learning.
[1048.16 → 1054.54] And then about three years ago, I joined Uber, where we started the Michelangelo, which is not named after me in any way.
[1055.50 → 1055.98] That's a shame.
[1055.98 → 1057.92] Yeah, and people get that question all the time.
[1058.30 → 1065.56] We started the Michelangelo platform, which helps people, which helps data scientists and engineers across the company build ML systems,
[1065.98 → 1071.72] kind of prototype, explore ML systems, build them, and then deploy them into production and serve predictions at scale.
[1072.06 → 1078.20] Yeah, so why, if you're in a company that's trying to build up their AI presence within the company,
[1078.28 → 1080.16] why would they need an ML platform?
[1080.36 → 1084.40] Why isn't like Jupyter Notebooks everywhere just fine for people?
[1084.40 → 1092.88] One of the things, so kind of like the state of Uber's ML stuff about three years ago was that a lot of people were trying to do that, right?
[1092.94 → 1099.42] So there was a lot of people, you know, grad students learn how to build their ML models in their grad school classes and whatever,
[1099.58 → 1100.82] and they have their own ways to do it.
[1100.84 → 1101.84] Everybody has their own.
[1102.22 → 1103.00] I use R.
[1103.00 → 1115.06] I use Python, and what we saw was that people were trying to, either trying to productionize like an R model and run an R runtime in production at high, at low latency,
[1115.38 → 1120.14] which is just like very challenging, and kind of people will cringe when they hear that today.
[1120.14 → 1126.12] Secondly, you would see like teams that did have, data scientists that did have engineer support,
[1126.56 → 1135.80] they would build up these bespoke like towers of infrastructure at a per-use case basis that would tend to be less well-built just because they had lower resources,
[1136.34 → 1143.78] but like duplicative of different pieces of infrastructure that people would build to serve these models in production across all the different ML use cases the company has.
[1143.78 → 1149.34] And then kind of the scariest is people just wouldn't get started at all because they wouldn't have a way to,
[1149.74 → 1152.40] some people wouldn't have a way to get their models into production.
[1152.60 → 1160.96] So we saw the opportunity to build a common platform to help people have a unified way to build models and to,
[1161.48 → 1166.98] and this is the trickiest part, put those same models that they prototyped on into production to make those predictions.
[1166.98 → 1175.18] And along the way, bring a lot of data science best practices, build into the system reproducibility, common analyses,
[1175.90 → 1184.98] and all of that kind of like versioning and all that kind of good stuff that is kind of like these data science best practices that aren't yet really well established.
[1185.20 → 1190.14] You know, we have a lot of really well established software engineering best practices that everybody knows,
[1190.62 → 1193.66] CCD and, you know, version control and stuff like that.
[1193.66 → 1198.40] And that stuff's not as well appreciated in the data science community.
[1198.62 → 1203.18] And it's just because a lot of this work is new, and it's not like these guys don't understand the importance of it,
[1203.26 → 1207.60] but it's just like the best processes and the best patterns for building this stuff have not yet,
[1207.90 → 1209.52] we have not really converged on those yet.
[1209.64 → 1213.88] So kind of spent a lot of effort to focus on where we think this stuff is going to go
[1213.88 → 1221.44] and to help build the tools to enable, to like empower data scientists to kind of do the right thing from the beginning.
[1221.44 → 1224.74] Awesome. So how many people are using Michelangelo at Uber?
[1224.84 → 1226.46] That's really hard to say.
[1226.64 → 1231.80] I would say we probably have more than, so this platform supports machine learning use cases across the company.
[1232.06 → 1238.72] So everything from like fraud related things to predicting how long it's going to take a car to get to you,
[1238.90 → 1242.50] to even like Uber Eats, like ranking dishes in the Uber Eats app.
[1242.76 → 1246.18] All the main ML stuff runs through this platform now.
[1246.18 → 1252.66] But this is just like an interesting kind of platform development challenge is, you know,
[1252.68 → 1254.36] we have a lot of people who like kind of use it.
[1254.42 → 1256.32] They're like, hey, I kind of want to build an ML thing.
[1256.38 → 1259.72] And they dabble in, explore a couple of little models they want to make.
[1260.10 → 1264.58] But maybe they haven't, they never end up fully deploying that model to production.
[1264.90 → 1265.00] Right.
[1265.08 → 1271.46] And so it's kind of tricky to say like how many actual use cases do you, like, do you have on this system?
[1271.46 → 1275.98] We know it's well over 100, but, you know, it's hard for us in the platform to say,
[1276.08 → 1279.52] is this something that this team is just using this as an experiment?
[1279.76 → 1282.94] Or is it like fully productionized and deployed across the whole company?
[1283.12 → 1286.28] And that's just like an area that we've just underinvested in a little bit.
[1286.36 → 1288.58] But we think there's a lot more to do there.
[1289.16 → 1289.26] Yeah.
[1289.50 → 1292.94] Is there, like, as you've seen people start to use the system,
[1293.10 → 1299.70] are there features of it that you thought that kind of surprised you in the sense of how people relied on them
[1299.70 → 1302.82] or things that people needed that you didn't expect that they would need or other things?
[1303.16 → 1304.24] Yeah, that's a perfect question.
[1304.38 → 1306.20] And I've been reflecting on this a lot recently.
[1306.52 → 1309.20] And, you know, I'm the product manager, so it's kind of my job.
[1309.46 → 1316.38] But the thing that I would say that kind of has gotten disproportionate adoption,
[1316.72 → 1320.00] given our maybe even like underinvestment into this,
[1320.06 → 1322.50] where we could have, we still could do a lot more in this space,
[1322.50 → 1325.76] but our users just adopted this overwhelmingly, and they love it,
[1325.82 → 1328.54] is our feature store, which is part of the platform.
[1328.54 → 1335.74] And what that allows, so, you know, common problems for managing features related for ML workflows
[1335.74 → 1340.30] are that you have to clean your data and transform your data and combine it all,
[1340.50 → 1344.26] and also historically, into a training data set so you can train your model.
[1344.44 → 1349.82] But then once your model's created, how do you do all of those same transforms in the same way,
[1349.90 → 1353.88] the same preprocessing to that data in real time when you deploy your model?
[1353.88 → 1359.98] So there's kind of this like dual type of ETL that happens in different compute environments that's really tricky.
[1360.38 → 1362.70] And possibly on a variety of resources.
[1363.34 → 1363.52] Yeah.
[1363.70 → 1366.64] And I mean, we see a lot of like vendor solutions here,
[1366.72 → 1369.90] but I feel like we don't see anybody really tackling that kind of stuff.
[1369.94 → 1373.22] And I think it's partially because it's not sexy at all to work on that stuff.
[1373.26 → 1375.30] And also because it's just super hard to do properly.
[1375.30 → 1381.78] And we've provided some nice ways for people to define their feature transforms to the platform
[1381.78 → 1388.22] and then be confident that those transforms will happen consistently across both computer environments,
[1388.62 → 1389.86] you know, real time and offline.
[1390.30 → 1396.06] But I think the other interesting thing is we saw, let's take the Uber Eats world, for example.
[1396.36 → 1403.56] They probably have more than 10 different models that they use to predict to rank dishes and whatever they do.
[1403.56 → 1405.76] And a lot of those models use the same kind of features.
[1406.30 → 1409.38] And before this feature store, data scientists didn't have any insight into,
[1409.64 → 1413.42] hey, other people that were working on similar problems, what kind of feature pipelines had they built?
[1413.84 → 1418.46] And then when this feature store came along, now when a data scientist wants to start a new model,
[1418.52 → 1422.08] they can just look and see what features exist that are relevant for me.
[1422.46 → 1425.68] Let me just like start including or start off,
[1425.76 → 1432.92] warm start with my model exploration process with the X features that are most relevant to this problem from the beginning.
[1432.92 → 1440.22] So there's a whole new element of collaboration, visibility, feature sharing that was previously not there.
[1440.32 → 1445.00] And I really don't see many solutions in that space in industry today either.
[1445.20 → 1447.02] So I think that's a really promising area.
[1447.28 → 1449.30] Cool. Yeah, I look forward to hearing more about that.
[1449.42 → 1455.72] And definitely if you publish anything about that, we'll be happy to post that on the show links here.
[1455.96 → 1456.08] Cool.
[1456.08 → 1465.52] Yeah. The other thing I was curious about just from the fact that, you know, you mentioned before that the incentives for data scientists are kind of different and not always aligned with producing,
[1465.76 → 1468.76] you know, production ready models and all of those things.
[1468.86 → 1478.42] How do you how do you build up a team to build an ML platform where really you kind of need a software engineering experience to be able to build something that's production ready?
[1478.42 → 1485.34] But you need the knowledge and the expertise around machine learning to be able to understand, you know, what to build.
[1485.46 → 1488.08] So you're it's going to be relevant to the people you're building it for.
[1488.32 → 1500.18] Yeah. So I think one of the nice things is that we've had a little bit of the leadership in our organization has been a relatively forward-thinking to be willing to fund an ML platform,
[1500.26 → 1505.16] the development of an ML platform much earlier than I think is common in industry.
[1505.16 → 1509.64] And that's allowed us to get it wrong a couple of times before we got it right.
[1509.74 → 1512.30] But we feel like we really got it really right now.
[1512.52 → 1520.56] And there's like a tension between data scientists want this nimbleness and flexibility throughout their exploration and prototyping stages.
[1521.32 → 1524.92] And, you know, if you think of any productionized system, it's super stable.
[1524.92 → 1529.58] And so how do you kind of accomplish both of those constraints?
[1529.78 → 1534.56] It's a challenge. And so what we some of the design philosophy that we're taking, and we're you know,
[1534.56 → 1543.60] this is always developing is we're trying to allow data scientists to work within our system using the tools that are most relevant for them.
[1543.60 → 1550.70] So we'd love for them to work in Jupyter notebooks and write all their models the way they normally would.
[1550.80 → 1562.74] We can provide some helpful APIs for them, for example, the feature store stuff to pull in their data so they don't have to reimplement a bunch of work that already exists in terms of like enterprise intelligence, you know, that's already been done.
[1562.74 → 1572.90] But after a certain point, when the kind of prototyping stage is complete through, if you think of like this machine learning lifecycle where it's like now I want to actually use this in production.
[1572.90 → 1579.50] And maybe it doesn't mean you're going to launch it to the whole company, and it's going to be, and you're done with the project could just be like, I want to experiment with this on live traffic.
[1579.50 → 1595.04] We focus on making it relatively low activation energy to take your prototype and transform it into something that can go into these productionized, well engineered, hardened systems that we can be confident will be stable from a systems' perspective.
[1595.04 → 1611.00] And we still want to give data scientists the ability to monitor these models that are in production for not just, you know, systems issues like whatever applies to typical microservices, but also like the data science monitoring, how accurate is this model over time?
[1611.42 → 1613.36] Are there any model drift, stuff like that?
[1613.42 → 1618.18] And so there's a story for data scientists throughout the lifecycle and a story for engineers throughout the lifecycle.
[1618.18 → 1626.92] And then the balance is, and the challenge is like, how do you balance between those at the different stages, taking into account all the priorities for both stakeholders throughout?
[1627.32 → 1629.44] Awesome. Yeah, that gives some great perspective.
[1629.88 → 1639.28] Well, to kind of end things out here, are there places online where people can find out more about what you guys have done and maybe also some things that you put out there that you might want to share?
[1639.44 → 1640.48] Yeah, that's a good question.
[1640.48 → 1644.34] We've published a blog post about Michelangelo in I think October 2017.
[1644.84 → 1652.40] And it's pretty easy if you just search Michelangelo ML platform on Uber, on Google rather, you can find that.
[1652.74 → 1657.18] And we've published a lot of other pieces about related ML work we've done.
[1657.24 → 1661.64] And I think we're likely to, in the near future, open up the kimono a little bit more on Michelangelo.
[1661.76 → 1662.28] So stay tuned.
[1662.54 → 1663.12] Cool. Awesome.
[1663.22 → 1663.98] We'll look forward to that.
[1664.06 → 1667.22] Well, thanks for joining and enjoy the rest of the conference.
[1667.34 → 1667.84] Appreciate it.
[1670.48 → 1671.36] All right.
[1671.42 → 1674.02] Thank you for tuning into this episode of Practical AI.
[1674.30 → 1675.76] If you enjoyed this show, do us a favour.
[1675.88 → 1677.24] Go on iTunes and give us a rating.
[1677.56 → 1679.40] Go in your podcast app and favourite it.
[1679.50 → 1682.22] If you are on Twitter or social network, share a link with a friend.
[1682.28 → 1684.64] Whatever you got to do, share the show with a friend if you enjoyed it.
[1684.94 → 1687.62] And bandwidth for changelog is provided by Vastly.
[1687.74 → 1689.16] Learn more at fastly.com.
[1689.26 → 1692.56] And we catch our errors before our users do here at changelog because of Rollbar.
[1692.76 → 1695.18] Check them out at rollbar.com slash changelog.
[1695.48 → 1697.98] And we're hosted on Linde cloud servers.
[1697.98 → 1699.96] Head to linode.com slash changelog.
[1699.96 → 1700.50] Check them out.
[1700.58 → 1701.42] Support this show.
[1701.54 → 1705.04] This episode is hosted by Daniel Whiten ack and Chris Benson.
[1705.50 → 1706.94] Editing is done by Tim Smith.
[1707.08 → 1709.22] The music is by Break master Cylinder.
[1709.56 → 1713.04] And you can find more shows just like this at changelog.com.
[1713.12 → 1715.18] When you go there, pop in your email address.
[1715.48 → 1719.30] Get our weekly email keeping you up to date with the news and podcasts for developers
[1719.30 → 1721.50] in your inbox every single week.
[1721.88 → 1722.66] Thanks for tuning in.
[1722.80 → 1723.58] We'll see you next week.
[1723.58 → 1724.90] What's the final?
[1733.14 → 1733.34] Bye.
