[0.00 → 9.04] You know if I could go back, that is the one thing I would change about if I don't go off and do a Docker container for pure ease of learning and ease of training.
[9.24 → 10.76] Nothing beats Cola in my view.
[11.06 → 11.16] Yeah.
[11.26 → 15.86] They have the best simplified interface that has everything that you need there.
[16.00 → 19.78] And so, yes, given that option, I will often use Cola to go do that.
[22.88 → 25.56] Bandwidth for Change Log is provided by Vastly.
[25.88 → 27.82] Learn more at Fastly.com.
[27.82 → 31.16] We move fast and fix things here at Change Log because of Rollbar.
[31.28 → 32.96] Check them out at Rollbar.com.
[33.20 → 34.82] And we're hosted on Linde cloud servers.
[35.70 → 37.70] Head to linode.com slash Change Log.
[40.74 → 42.54] Linde is our cloud server of choice.
[43.06 → 46.00] Grab the NATO plan for just $5 a month, just $5.
[46.38 → 51.54] That gets you a gig of RAM, a blazing fast 25 gig SSD, and one terabyte of transfer.
[51.84 → 54.30] Let's be honest, you can go a long ways on that $5.
[54.30 → 59.20] When you do need to scale up, their prices are predictable, so you can put your calculator down.
[59.30 → 59.86] You won't need it.
[60.16 → 65.32] We've been running Change Log.com on Linde for years, and we've always impressed by their award-winning support team.
[65.86 → 68.58] Check them out at linode.com slash changelog.
[68.76 → 71.96] Once again, that's linode.com slash changelog.
[71.96 → 88.52] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[88.82 → 92.90] This is where conversations around AI, machine learning, and data science happen.
[93.26 → 97.94] Join the community and Slack with us around various topics of the show at changeog.com slash community,
[97.94 → 99.28] and follow us on Twitter.
[99.48 → 101.06] We're at Practical AI FM.
[101.96 → 110.84] Welcome to another fully connected episode of Practical AI,
[111.18 → 115.48] where Daniel and I keep you fully connected with everything that's happening in the AI community.
[115.94 → 121.90] We're going to take some time to discuss the latest AI news and dig into some learning resources to help you level up on your machine learning game.
[122.44 → 123.52] My name is Chris Benson.
[123.52 → 127.70] I'm a principal AI strategist at Lockheed Martin, and with me as always is Daniel Whiten ack,
[127.82 → 130.60] who is a data scientist at SIL International.
[130.86 → 131.86] Hey, how's it going today, Daniel?
[132.50 → 133.38] It's going very good.
[133.44 → 138.96] It's hot here, but I guess I'm in the Midwest of the United States, and you are in the South.
[139.10 → 145.08] I'm sure what I'm experiencing is nothing compared to Georgia heat.
[145.34 → 147.92] I think that the thing that really gets you in Georgia is the humidity.
[148.24 → 148.44] Yeah.
[148.44 → 151.74] So it tends to be very humid here, and that's what usually gets people.
[151.80 → 152.86] It's not terribly hot today.
[153.04 → 153.22] Yeah.
[153.34 → 157.08] I think we're around 80 degrees Fahrenheit, so it's not too bad.
[157.18 → 158.60] It's quite humid outside, though.
[158.78 → 159.26] Oh, wow.
[159.28 → 160.66] I think it's warmer here then.
[160.68 → 161.20] It might be.
[161.20 → 161.32] Yeah.
[161.88 → 164.42] I think we're pushing 90, I think, Fahrenheit.
[164.42 → 165.72] I think that's where we're going to be tomorrow.
[165.92 → 169.58] I think we're popping back up with you tomorrow, but we have some weather that's come through
[169.58 → 170.86] and cool things out.
[171.18 → 171.70] So yeah.
[171.78 → 172.84] But that's the way it is.
[172.86 → 173.60] It's summer, man.
[173.94 → 174.24] Yeah.
[174.50 → 177.48] I've also got a few boxes sitting right next to me.
[177.70 → 181.26] I finally decided to build a computer.
[181.66 → 183.64] I know we talked about this a couple of times.
[184.00 → 190.30] I have fond memories of building computers earlier on in my life when I was in grad school
[190.30 → 193.36] and then before that and college and other times.
[193.52 → 197.66] But ever since being a data scientist, I've always just had a laptop, you know?
[198.00 → 198.28] Right.
[198.28 → 199.30] I don't know.
[199.40 → 205.52] It's definitely not necessary in any sort of way to have your own personal, you know,
[205.60 → 206.52] AI machine.
[206.68 → 210.86] But since I talk about this stuff so much, it's almost like a rite of passage, I guess.
[211.02 → 213.16] I feel like I should have that experience.
[214.24 → 215.52] So I don't know.
[215.58 → 215.90] We'll see.
[215.96 → 217.64] I've got the boxes.
[217.86 → 221.88] I've got case, RAM, hard drive and GPU.
[222.24 → 222.90] There you go.
[222.96 → 226.56] But the rest is on its way and currently not functional.
[227.30 → 227.46] Yeah.
[227.46 → 231.92] So for listeners, though, I know you can't see this, but Daniel and I are talking over
[231.92 → 236.10] Zoom, and he has the data centre background up behind him.
[236.34 → 238.18] The Zoom virtual background.
[238.38 → 238.86] There you go.
[238.92 → 241.28] You're building out the DGX rack there behind you.
[241.34 → 248.76] I'm not quite in the server room yet, although I do expect the room I'm in will warm up quite
[248.76 → 252.04] a bit when I turn my computer on whenever it gets going.
[252.04 → 256.56] But yeah, I'll have to make sure and have the fan going.
[256.76 → 260.30] And maybe, you know, eventually it will be cold here in Indiana.
[260.50 → 261.88] So maybe that will be a benefit.
[262.04 → 262.44] I don't know.
[262.76 → 264.90] I'm just glad to know you're not living in the server room there.
[265.06 → 267.26] You know, sheltering in place in the data centre.
[267.26 → 270.02] I'm bringing the server to me.
[270.10 → 270.68] That's right.
[270.76 → 273.16] I'm just that sitting on my dining room table.
[273.82 → 279.44] Not even in my office because we have a family member staying in my office as a bedroom
[279.44 → 281.82] right now during the quarantine.
[282.16 → 283.26] So gotcha.
[283.62 → 284.52] Yeah, it should be fun.
[284.52 → 290.62] So one more person in our house and one more computer portable heater coming soon.
[291.20 → 291.32] Gotcha.
[291.56 → 295.78] You know, actually, you and I are doing something a little bit similar there in that today I'm
[295.78 → 302.14] going to buy three Amazon instances to build a Kubernetes cluster for my animal protection
[302.14 → 303.18] charity.
[303.34 → 304.02] Oh, sweet.
[304.12 → 304.84] That I work on.
[305.22 → 305.78] So sweet.
[305.92 → 308.10] I got to get the new Kubernetes cluster up and running.
[308.52 → 309.54] Yeah, that's exciting.
[309.98 → 311.86] It will always be an interesting experience.
[311.86 → 315.80] Are you going the sort of manage your own deployments sort of thing?
[315.86 → 319.98] Are you doing the EKS managed by Amazon type thing?
[320.42 → 321.60] So it's not my budget.
[321.76 → 322.88] It's the charity's budget.
[323.04 → 325.66] And it is a very small charity with a very tight budget.
[325.80 → 332.52] So I'm simply buying the instances at rock bottom reserve prices and then doing everything
[332.52 → 333.00] myself.
[333.46 → 333.74] Yeah.
[333.96 → 335.48] To try to keep that as low as possible.
[336.06 → 338.74] Look into the tool COPS.
[339.16 → 339.68] K-O-P-S.
[339.68 → 341.00] That's exactly what I'm using.
[341.00 → 341.82] Yeah, yeah.
[341.96 → 346.60] I've used that a good bit in the past, and it saves a lot of trouble.
[347.28 → 348.08] That's what I'm going with.
[348.20 → 348.54] Exactly.
[349.06 → 349.22] Yeah.
[349.32 → 353.18] And COPS itself is an open source tool that's out there.
[353.30 → 358.32] And, you know, since Chris is working with the charity, and I'm also work with a nonprofit,
[358.32 → 362.96] so open source things are a lot of times very nice to use.
[363.28 → 364.14] They are.
[364.14 → 369.94] And I thought today maybe we could discuss that a bit, but more in the context of AI,
[370.04 → 370.42] I guess.
[370.42 → 377.06] So open source and AI contributing to AI open source, open data.
[377.32 → 383.06] There are a lot of different related things there, generally under like open source AI or open
[383.06 → 384.56] AI things.
[384.56 → 388.60] Not to be confused with open AI, the company.
[388.92 → 389.30] There you go.
[389.94 → 390.16] Yep.
[390.52 → 390.72] Yeah.
[390.74 → 391.20] I don't know.
[391.30 → 392.24] Does that sound interesting?
[392.70 → 393.64] No, that sounds perfect.
[394.26 → 398.90] Ironically, our talk of building things and Kubernetes clusters leads kind of right into
[398.90 → 404.26] it because, you know, with modern AI tooling, it's largely built on Docker and Kubernetes these
[404.26 → 405.04] days and such.
[405.10 → 407.54] So that's a perfect timing on that.
[407.54 → 407.98] Yeah.
[408.10 → 410.98] So maybe we just start by, I guess, talking about that.
[411.14 → 420.08] Like on the show, we mentioned certain things very often, and I could think of many of those
[420.08 → 425.16] off the top of my head that are all open sources because I think that's probably the more standard
[425.16 → 425.50] case.
[425.68 → 433.32] So like TensorFlow, PyTorch, Docker, Spacey, Kubernetes itself.
[433.60 → 434.16] What else?
[434.16 → 437.72] A lot of these things are all open source, right?
[438.06 → 438.24] They are.
[438.36 → 443.42] I mean, the software of artificial intelligence is largely built on open source and, you know,
[443.66 → 447.34] people end up paying for hardware or services for hardware.
[447.62 → 448.16] Yeah.
[448.52 → 450.96] You know, that's kind of how the divvy is.
[451.08 → 454.50] You know, you budget for the hardware or the services to gain access to compute.
[454.88 → 455.08] Yeah.
[455.18 → 458.80] And maybe we should clarify as well what we mean by open source.
[458.96 → 462.36] Maybe people are more familiar with that term or not familiar.
[462.36 → 464.62] And there are some confusing things around it.
[464.68 → 471.46] Actually, maybe one of the confusing things is open source doesn't necessarily mean free
[471.46 → 472.16] either.
[472.46 → 475.94] So I guess my background isn't in computer science, software engineering.
[476.08 → 479.48] So I'll probably have some like computer science people get mad at me.
[479.64 → 480.98] There's like a proper definition.
[480.98 → 488.20] But I mean, open source, I think mainly its etymology derives from the fact that like you
[488.20 → 490.68] can see all the code that is there.
[490.82 → 495.82] The code is available for you to obtain and or modify use.
[496.20 → 503.54] So like with TensorFlow, for example, you can go to GitHub.com slash TensorFlow.
[503.88 → 506.00] I think that's still the link unless, you know.
[506.00 → 510.82] Yeah, I think it's really defined by the fact that when you distribute the code, if it's
[510.82 → 515.58] open source software, and you're distributing that code around, you have to distribute the
[515.58 → 520.02] code of the programs or programs themselves with your distribution.
[520.02 → 522.16] So you don't just get the executable that you're running.
[522.38 → 522.86] Right.
[522.94 → 523.72] Just a binary.
[523.98 → 525.04] You don't get just the binary.
[525.18 → 527.12] You get the source code along with that.
[527.52 → 532.84] And typically, and I'm saying this strictly from personal experience, the vast majority of
[532.84 → 537.48] open source software, I would argue, is freely available for people to use.
[537.90 → 543.18] And then the way it ends up is a lot of times that licensing allows companies to integrate
[543.18 → 547.14] open source software into their own proprietary packages.
[547.14 → 550.38] And they do have to distribute the source code for that part of it.
[550.38 → 556.18] But they may also have proprietary code depending on the licensing available as well or as a service.
[556.32 → 557.22] You know, that's another thing.
[557.22 → 557.66] Yeah.
[557.82 → 563.36] So it should be said, too, that like if you go to TensorFlow slash TensorFlow on GitHub,
[563.78 → 569.82] you can see all the code that makes up TensorFlow, at least the core part of TensorFlow there.
[570.52 → 576.00] Then there is an enterprise version of TensorFlow that Google came out with recently.
[576.10 → 578.78] And some of those elements may not be open.
[579.28 → 579.40] Right.
[579.52 → 580.50] Some of them might be open.
[580.56 → 581.04] I'm not sure.
[581.04 → 585.82] But you'll see this pattern a lot, too, where you have liked I think they call it open core,
[586.06 → 593.16] where you have a core part of a tool or software that is open and you can use.
[593.34 → 599.92] And then there might be a set of additional functionalities or maybe even like an upgraded
[599.92 → 605.52] version that you have to pay for that has some extra features or maybe more robustness or maybe it
[605.52 → 612.14] supports multiple users, or maybe it supports, you know, specific access controls or like other
[612.14 → 614.40] things that are more enterprise, I guess.
[614.90 → 616.36] So that's another pattern that you'll see.
[616.46 → 622.18] But on the TensorFlow slash TensorFlow, you'll see that there's the code if you go to that
[622.18 → 622.46] link.
[622.56 → 627.26] And then there's about, you know, a little ways down in the code listing, there's a license.
[627.92 → 632.26] And you'll see that this license is an Apache 2.0 license.
[632.46 → 634.38] It's a very common open source license.
[634.38 → 635.52] It's a very permissive one.
[635.98 → 637.12] Yeah, very permissive.
[637.24 → 639.50] So it allows you to do a lot of things with the code.
[639.68 → 643.10] But there are a bunch of other licenses as well out there.
[643.76 → 646.64] There's the MIT license.
[647.34 → 648.48] Which is also permissive.
[649.18 → 649.78] Yeah, yeah.
[649.78 → 655.18] So actually, there's probably a guide out there that details all the different ones.
[655.28 → 659.02] And I think they're actually on GitHub when you're choosing a license for a project, they
[659.02 → 660.14] have a way to compare them.
[660.14 → 665.26] But yeah, some of these are more permissive than others and allow you to do certain things
[665.26 → 670.18] with the code that you're not doing with other projects that have a different license or something
[670.18 → 670.70] like that.
[671.14 → 671.44] Right.
[671.76 → 673.10] So that's one thing to be aware of.
[673.10 → 678.42] But I think a lot of where people might get hung up with that is like if you suck that code
[678.42 → 684.52] into your own project and, you know, it's part of your suite of software, and then you sell
[684.52 → 688.68] that or something, you know, there might be certain implications to that.
[688.74 → 694.42] But in general, a lot of people, you know, might use TensorFlow, for example, to train a model.
[694.80 → 698.92] And then that model is what they ship with their product or something like that.
[699.34 → 699.48] Right.
[699.64 → 702.48] And that model, which may not be proprietary in any way.
[702.74 → 704.92] I mean, it is proprietary to that company.
[705.44 → 706.28] Yeah, to that company.
[706.28 → 711.12] And also the code that is running or doing the inference for that model and even actually
[711.12 → 712.94] the training code for that.
[713.06 → 718.88] It is using TensorFlow like you're not just copying TensorFlow itself and selling TensorFlow.
[718.88 → 725.54] You are using TensorFlow to create custom code in the same way you would import other libraries
[725.54 → 726.44] and that sort of thing.
[726.44 → 734.22] So this is a whole world of thought around open source software and what licenses are good
[734.22 → 734.84] and not good.
[734.94 → 740.04] And certain actually certain companies have restrictions around if like you're using an
[740.04 → 747.72] open source project, they might allow you to use code that has a certain license versus
[747.72 → 751.62] code that has a different license.
[751.80 → 755.22] That might be something you want to be aware of with your own company as well.
[755.72 → 756.04] Absolutely.
[756.04 → 761.04] And depending on policy, they may orient on the license in terms of approvals or they
[761.04 → 764.70] may focus on specific software itself along with its license.
[765.04 → 767.42] But all this is really relevant now to AI.
[767.66 → 773.60] And I think a lot of people that have come into AI from routes other than software, particularly
[773.60 → 777.30] open source software, are having to learn this as they go along, which I thought was
[777.30 → 781.12] one of the great reasons that we should talk about this today when you suggested it, is that
[781.12 → 785.94] as we see the field of AI maturing and evolving very rapidly,
[785.94 → 792.58] it is becoming integrated into what is essentially a software stack that different organizations
[792.58 → 793.90] have and their workflows.
[794.40 → 799.16] And it is how they productively enable some of their software.
[799.70 → 803.08] And so it's really being wrapped into the software lifecycle itself.
[803.08 → 805.30] And so it's now affecting people.
[805.30 → 809.70] And as we talk about this, as software developers, we might be talking about how would we contribute
[809.70 → 812.00] to open source code and open source projects.
[812.24 → 816.52] But now it makes a lot of sense to talk about how do we contribute to open source artificial
[816.52 → 818.30] intelligence and open data?
[818.30 → 819.26] Yeah.
[819.26 → 826.50] I mean, as opposed to sort of normal software engineering workflows, data really drives how
[826.50 → 828.92] code operates in the world of AI.
[829.16 → 835.92] So how you get the data and distribute data associated with your AI project is very relevant.
[836.56 → 841.82] Before we move on, I'll just mention too, there's an episode 322 from our friends at the
[841.82 → 842.76] Changelog podcast.
[842.76 → 849.98] They talked to Manish from Graph about licensing and relicensing and all those sorts of things
[849.98 → 850.54] they did with that.
[850.62 → 853.40] And I found that episode very enlightening on these topics.
[853.40 → 856.48] So if you're interested, they dive a lot deeper into that.
[856.92 → 860.84] I had no idea you're going to mention Graph, but that's my current hot topic for myself.
[861.40 → 862.84] So Graph's awesome.
[863.22 → 865.88] I'm moving into Graph right now for what I'm doing.
[866.02 → 866.58] Side note.
[866.72 → 866.84] Yeah.
[866.94 → 868.44] Graph is a graph database.
[868.44 → 869.90] It's really, really great.
[869.98 → 876.44] Actually, the queried language that you use on top of it is GraphQL, which makes it really
[876.44 → 877.64] nice in a lot of ways.
[877.78 → 879.20] And it's very performant.
[879.44 → 882.24] And yeah, anyway, if you're interested in graph databases, check it out.
[882.32 → 887.60] I'll give a shameless plug because I do like that project, which is another open source project.
[888.10 → 888.32] It is.
[888.38 → 889.08] It's open source.
[889.18 → 894.38] And it's a project that I'm integrating into my AI workflow at this point for the charity
[894.38 → 895.10] that I spoke of.
[895.34 → 895.88] Oh, awesome.
[896.28 → 898.10] Yeah, that's definitely so.
[898.10 → 898.32] Cool.
[898.44 → 899.06] And she mentioned it.
[899.32 → 899.58] Definitely.
[899.84 → 905.00] I love plugging the projects that we both use here on the podcast, especially if they're
[905.00 → 908.72] open source and, you know, there's a community around it like Graph.
[909.30 → 910.50] But I guess that's one thing.
[910.62 → 911.92] Graph is a database.
[912.34 → 919.06] And so you're using it in your AI project, but it's not AI software necessarily, but it's
[919.06 → 921.98] the data store associated with the AI software.
[922.40 → 922.68] Right.
[922.80 → 923.66] And that's how I'm using it.
[923.66 → 927.02] This sort of auxiliary or I don't know what we want to call it.
[927.02 → 931.42] Supplemental infrastructure things are often driven by open source as well, right?
[931.96 → 932.22] Right.
[932.30 → 936.52] I mean, to describe if people are wondering how that fits in, and it's not really specific
[936.52 → 937.18] to what I'm doing.
[937.30 → 942.74] This could be for a lot of different possibilities that if you are operating an
[942.74 → 947.72] organization, and you have operational data, things that you're doing with whatever your
[947.72 → 950.24] organization is, and you need a data store to keep that.
[950.62 → 953.26] But you may also want to provide analytics on that.
[953.36 → 957.74] You may want to provide, you know, apply some AI modelling to some of that data.
[957.92 → 962.76] And so it really all comes down to the fact that you are integrating AI into your software
[962.76 → 963.18] workflow.
[963.38 → 964.22] That's a good sign.
[964.30 → 965.14] That's a sign of maturity.
[965.14 → 978.20] We deserve a better internet and the brave team has the recipe for bringing it to us.
[978.32 → 979.32] Start with Google Chrome.
[979.56 → 983.28] Keep the extensions, the dev tools and the rendering engine that make Chrome great.
[983.48 → 984.36] Rip out the Google bits.
[984.48 → 985.14] We don't need them.
[985.48 → 988.00] Mix in ad and tracker blocking by default.
[988.00 → 993.04] Quick access to the Tor network for true private browsing and an opt-in reward system so
[993.04 → 995.68] you can get paid to view privacy respecting ads.
[995.78 → 999.62] Then turn around and use those rewards to support your favourite web creators like us.
[999.98 → 1004.54] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1015.72 → 1020.78] So we were just getting into the topic, and you mentioned something that was really important
[1020.78 → 1026.46] about AI not just being about code, but being about data.
[1027.24 → 1032.50] And I think along with that data, a certain piece of data, which is the model itself, which
[1032.50 → 1034.16] is really just another piece of data.
[1034.70 → 1038.36] So there's the code piece, but then there's the data piece.
[1038.56 → 1044.36] And oftentimes there's this weirdness because code is open sourced on GitHub.
[1044.36 → 1052.70] But then to me, it seems like, oh, like there's this very structured sort of way to go about
[1052.70 → 1055.66] finding open source code and things.
[1055.90 → 1060.00] And then open data is just sort of like all over the place.
[1060.10 → 1062.44] It's like totally scattered and weird.
[1062.50 → 1065.24] And like, I don't know if you have a similar experience.
[1065.40 → 1065.82] No, I do.
[1065.92 → 1070.80] I think that there's been a lot of great work trying to address that problem recently.
[1070.80 → 1075.62] Um, and we'll talk about some of those, uh, you know, as we go forward in terms of how
[1075.62 → 1076.30] to find data.
[1076.50 → 1080.88] But yeah, I think the fortunate side is a lot of people that are already working in open
[1080.88 → 1084.54] source software are recognizing that they need code, and they have the same problem.
[1084.54 → 1087.26] And so it's getting tackled fairly, fairly quickly.
[1087.84 → 1088.32] Yeah.
[1088.50 → 1094.52] Maybe before we talk about how to find data, I guess there's also could be licenses associated
[1094.52 → 1095.88] with data, right?
[1095.96 → 1096.26] Sure.
[1096.54 → 1099.30] You aren't able to repost it in another place.
[1099.30 → 1101.70] You are, aren't able to use it for these purposes.
[1101.70 → 1106.28] You are, aren't able to do certain things with the data.
[1106.62 → 1111.34] Recently, I downloaded some audio data from Mozilla's common voice project.
[1111.46 → 1116.14] So their workflow, like you find the data set you want, and you put in your email to download
[1116.14 → 1116.46] it.
[1116.52 → 1118.44] And when you do that, you also have to agree.
[1118.56 → 1124.22] I think the agreement was that you wouldn't try to identify, like personally identify the
[1124.22 → 1127.70] people whose voices are represented in the data.
[1128.20 → 1128.34] Yeah.
[1128.34 → 1134.66] So like that stipulation is very specific to that data set.
[1134.80 → 1139.56] But I guess it is kind of common in the sense that there are a lot of data sets that you could
[1139.56 → 1145.12] potentially try to identify people within data sets, which is the issue.
[1145.12 → 1152.72] It's an interesting juxtaposition of kind of licensing plus responsible AI, you know, ensuring
[1152.72 → 1157.92] that things principles like protecting PII, personally identifiable information are all
[1157.92 → 1158.66] integrated in.
[1158.80 → 1161.12] So I find that interesting that they did it that way.
[1161.58 → 1161.90] Yeah.
[1162.06 → 1162.30] Yeah.
[1162.30 → 1166.46] And I guess as well, you know, models being another piece of data.
[1166.68 → 1172.42] So just as a reminder for people, like when AI people refer to a model, they're basically
[1172.42 → 1177.34] just referring to a representation of a network architecture usually.
[1177.64 → 1183.32] So like this number gets fed into this operation and then gets fed into this, et cetera, along
[1183.32 → 1187.32] with the parameters associated with those operations, which are called weights and biases.
[1187.32 → 1187.80] Yeah.
[1187.80 → 1193.04] And all of that can be represented in data, especially if your model has, you know, 300 million parameters,
[1193.04 → 1197.24] you're going to put that into a data file and store it somewhere.
[1197.24 → 1197.40] Yeah.
[1197.40 → 1201.68] But it is just a it is essentially a complex data structure.
[1202.00 → 1202.22] Yeah.
[1202.24 → 1203.08] It's a data set.
[1203.38 → 1203.62] Yeah.
[1203.68 → 1205.20] That is the output of your modelling.
[1205.48 → 1205.74] Yeah.
[1205.90 → 1209.34] And so data in software operates on it, data out.
[1209.60 → 1209.88] Yep.
[1210.44 → 1212.92] There are a lot of pre-trained models out there.
[1212.92 → 1219.52] And so like if, if I'm in a GitHub repo, and it's like a repo for this project, someone
[1219.52 → 1222.76] did a project to do like an object recognition or something, I don't know.
[1222.84 → 1224.36] And they have a license in their repo.
[1224.36 → 1227.08] So it's like Apache 2.0 or whatever.
[1227.26 → 1227.72] I don't know.
[1228.20 → 1233.64] But then in their README, they say, you can download a pre-trained model from this link.
[1233.64 → 1239.96] And then the link is just a link to like an S3 bucket link to download the model.
[1240.26 → 1248.62] I'm not actually sure like what is legally implied by, if anything, by like what you can
[1248.62 → 1250.64] do with that downloaded pre-trained model.
[1250.64 → 1255.24] Now there are certain sites where maybe that's more specific in terms of what you download.
[1255.56 → 1260.74] But in that case, which I think is actually a very common case, the sort of here's my
[1260.74 → 1262.80] GitHub repo and here's a link to my model.
[1263.30 → 1270.32] I don't actually know if there are legal implications to what you can or can't do with that.
[1270.80 → 1270.90] Yeah.
[1270.90 → 1273.96] So not being an attorney, but playing one on a podcast.
[1274.32 → 1274.60] Yeah.
[1274.68 → 1281.92] I would say that that data was still distributed, and it was distributed under a legal condition,
[1282.04 → 1283.84] probably represented by a license.
[1284.00 → 1290.88] And so even if that license is shortcut, meaning it's not included in the link because they
[1290.88 → 1295.40] didn't download the whole repo or something, then I would expect that that data would still
[1295.40 → 1297.66] fall under whatever license it was distributed under.
[1297.66 → 1298.86] Yeah, it's a good question.
[1299.02 → 1302.68] So if there's anyone that knows more about this out there, I would be curious.
[1302.94 → 1306.92] So hit us up on Slack or LinkedIn or Twitter and let us know.
[1307.12 → 1310.72] Maybe our friends at Amu ta, who we had early on in the podcast.
[1310.86 → 1311.42] That's true.
[1311.56 → 1313.92] I don't know if you saw, but they got a bunch of funding.
[1314.10 → 1316.04] Wasn't it like 40 million or something?
[1316.32 → 1317.24] It was substantial.
[1317.42 → 1318.60] I don't remember what the number was.
[1318.60 → 1321.14] Yeah, led by I think Intel Capital or something.
[1321.38 → 1323.62] So Amu ta we had on early in the podcast.
[1323.62 → 1328.34] So not only that they have a data product, which is very interesting, but they're also
[1328.34 → 1331.32] very many legal experts in these sorts of things.
[1331.46 → 1334.72] So if you're listening out there, let us know your thoughts.
[1335.18 → 1345.74] Maybe we should turn to how to find and search for open source tools and code and data and models.
[1346.04 → 1348.24] What are your go-to for that?
[1348.24 → 1353.36] Probably for me, the same as most other people, certainly that are in the software world.
[1353.66 → 1358.96] Obviously, just Googling for certain terms, you know, Googling for some particular function
[1358.96 → 1364.12] and saying open source along with that, going to GitHub, going to blog entries that focus
[1364.12 → 1367.62] on open source ratings and distributions and such.
[1368.00 → 1372.18] Usually it's not hard, especially in the software world, because that's been going for such a long
[1372.18 → 1375.00] time, and it's, you know, we kind of have our inroads there.
[1375.00 → 1380.02] So I can usually find something that is more or less what I want within just a moment or
[1380.02 → 1381.66] two of an initial search.
[1381.88 → 1383.44] And then there's diving into the tool.
[1383.56 → 1386.66] For a while, it was a lot harder on the data side to do that.
[1387.00 → 1389.98] But the tools there are all are starting to come about as well.
[1390.64 → 1396.88] Yeah, it seems like in my workflow a lot, I'll almost start from known trusted sources and
[1396.88 → 1398.32] then kind of branch out from that.
[1398.36 → 1403.46] And what I mean by that is like I can go to TensorFlow or PyTorch.
[1403.46 → 1406.44] They have extensive documentation online.
[1406.60 → 1411.78] So if you just search for TensorFlow documentation or PyTorch documentation, or sometimes I'll
[1411.78 → 1416.78] search for, you know, TensorFlow transfer learning tutorial, let's say.
[1417.14 → 1418.28] And there's one of those, right?
[1418.34 → 1419.36] So I go there.
[1419.42 → 1421.62] I want to do transfer learning with TensorFlow.
[1421.94 → 1424.32] TensorFlow is open source so I can install it.
[1424.70 → 1429.18] And if I find the TensorFlow docs, then it'll tell me how usually there's like a getting
[1429.18 → 1435.20] started, you know, install TensorFlow, or they'll tell you, hey, you can try it on, you know,
[1435.28 → 1436.10] Cola or whatever.
[1436.84 → 1437.38] I'm the same.
[1437.58 → 1443.96] Another one kind of hitting these, what are kind of the forces, the big names in AI that
[1443.96 → 1448.34] are reputable and that you know that their legal teams have looked at things and all
[1448.34 → 1448.62] that.
[1448.72 → 1450.38] And you kind of there's a trust factor.
[1450.38 → 1456.60] Another one that I use a lot, especially at work is NVIDIA because they have a huge amount
[1456.60 → 1457.84] of documentation online.
[1457.98 → 1459.76] So I'll start from them and see what they have.
[1459.80 → 1464.94] And they have a bunch of partners as well as just Google, as does Microsoft, as does Facebook,
[1465.36 → 1466.42] which is PyTorch.
[1467.18 → 1467.28] Yeah.
[1467.42 → 1471.56] So there are a lot of good documentation pages out there.
[1471.56 → 1477.40] And I guess in order to find those, you kind of have to have a little bit of domain knowledge
[1477.40 → 1480.58] of like what are the key tools out there.
[1480.76 → 1484.54] I mean, you've already heard us mention a few like TensorFlow and PyTorch, but there's
[1484.54 → 1489.68] other ones like Chris mentioned NVIDIA tools that I think they have various tool sets out
[1489.68 → 1489.96] there.
[1490.18 → 1493.12] There's Spacey and the NLP world.
[1493.40 → 1498.94] There's, of course, the kind of data science-y Python toolkit, which is like Pandas and Sci kit
[1498.94 → 1500.16] Learn and all of that stuff.
[1500.16 → 1504.18] I feel like we have an advantage because we know about those things.
[1504.18 → 1511.32] So like when I'm searching, for example, to do like a maybe a traditional quote unquote
[1511.32 → 1517.86] machine learning thing on a smaller data set, I might go to the Scikit-learn documentation
[1517.86 → 1520.44] and search for like how to do this thing or that.
[1520.56 → 1525.42] Whereas if I'm trying to do like a thing that I know is like an AI thing, I might search like
[1525.42 → 1529.72] on TensorFlow or PyTorch examples or tutorials on that particular thing.
[1530.16 → 1536.52] And find certain open tutorials and how to install the right toolkit and that sort of thing.
[1536.62 → 1543.38] But I feel like I do have that advantage, and I'm not sure what the best way is to get that
[1543.38 → 1545.10] exposure to the main toolkit.
[1545.54 → 1546.76] I don't know if you have thoughts on that.
[1547.40 → 1548.18] That's a great point.
[1548.30 → 1553.18] And that is that we all, based on whatever problem that we're tackling at any point,
[1553.32 → 1555.56] we don't necessarily just use a single tool.
[1555.56 → 1560.22] It's, there's not a single go-to thing that you're always going to use for every project.
[1560.34 → 1564.60] If you're a TensorFlow person, you may use a lot of TensorFlow, but you probably also use
[1564.60 → 1567.56] some tools from NVIDIA, use some Python tools.
[1567.72 → 1572.84] You know, there are a lot of different possibilities on how you might combine a tool chain together
[1572.84 → 1574.00] to solve the particular problem.
[1574.02 → 1575.70] And it may change as you go from problem to problem.
[1575.78 → 1578.36] So I think that domain knowledge is hard to come by.
[1578.36 → 1582.92] So probably you either need to be really focused on self-learning and trying to follow
[1582.92 → 1585.52] reputable sites around or get into a course.
[1585.62 → 1588.92] There are a bunch of online courses that we, and I know we've talked about, we have some
[1588.92 → 1595.46] episodes that specifically address learning, but it helps to start not at square one when
[1595.46 → 1598.32] you're doing this so that you can be a little bit more efficient quicker.
[1598.88 → 1599.48] Yeah, for sure.
[1599.62 → 1600.54] I agree with that.
[1600.70 → 1606.90] If you're trying to really level up to kind of state-of-the-art things, I would highly recommend
[1606.90 → 1608.66] the website papers with code.
[1609.28 → 1609.36] Yeah.
[1609.66 → 1610.74] You can actually search.
[1610.88 → 1615.74] And there's also leaderboards for common AI tasks, whether that be, you know, image
[1615.74 → 1624.12] recognition or visual reasoning stuff or other things, speech recognition, and actually search
[1624.12 → 1629.12] through the sort of leaderboard of papers and then see the actual links to the tools that
[1629.12 → 1631.68] they use and also the code implementation.
[1632.06 → 1632.86] So that's a good idea.
[1632.86 → 1637.88] You know, even if you just browse around that site, I think, and look at the various things,
[1637.94 → 1643.20] you'll get a sense of like, these are the main things that people are using to do this
[1643.20 → 1643.88] sort of stuff.
[1643.96 → 1647.18] These are the main things people are using to do that sort of stuff.
[1647.56 → 1649.06] So I think that could be useful.
[1649.70 → 1650.36] Yeah, it is.
[1650.40 → 1651.00] It's interesting.
[1651.20 → 1654.94] You bring up a great point that there are different types of things that you may be looking
[1654.94 → 1655.32] for.
[1655.32 → 1660.56] On one side, you might be looking for just raw data, and you might go to, for instance,
[1661.04 → 1665.50] Google's dataset search that they released last year, which is fantastic because they
[1665.50 → 1669.16] have indexed many, many, many data sources and you can start looking.
[1669.24 → 1671.04] And that's one of many ways to enter into it.
[1671.06 → 1671.76] It's not the only one.
[1672.00 → 1675.82] But you might also be looking for domain expertise as well.
[1676.22 → 1679.20] And so we've had Semantic Scholar on the show before.
[1679.34 → 1683.86] And you might go look for some of the scientific papers that are relevant to the things that you're
[1683.86 → 1687.10] about to tackle, or you might be building on top of one of those papers.
[1687.68 → 1694.00] And so developing that domain expertise in the specific area, and then also having a
[1694.00 → 1698.34] diversity of data to tackle the problem with is really important.
[1698.54 → 1703.24] I think that's a really hard thing for people that are new into AI is understanding all these
[1703.24 → 1707.44] different pieces you have to put together into your workflow to be productive as quickly
[1707.44 → 1707.98] as possible.
[1708.64 → 1709.28] Yeah, for sure.
[1709.28 → 1715.72] It's a challenge, but I think the situation is better now, I think, than even a couple
[1715.72 → 1716.76] of few years ago.
[1716.88 → 1717.26] Oh, yeah.
[1717.38 → 1719.84] So that's encouraging.
[1720.26 → 1722.96] There are a lot of tutorials out there for various things.
[1723.30 → 1727.94] We've had the benefit of standing on top of the software development community's shoulders.
[1728.46 → 1734.34] So many of these problems that had we not had that privilege of doing would have definitely
[1734.34 → 1735.64] slowed down the process.
[1735.64 → 1741.48] So we are seeing warp speed in the AI world in terms of its evolution, largely because
[1741.48 → 1746.42] we can look to other places that are associated, that are related, and say, oh, that's how
[1746.42 → 1748.04] it was solved, something very similar.
[1748.04 → 1763.96] Changelog News is the best way to keep up with the ever-changing world of software.
[1764.68 → 1770.94] We track, log, and contextualize the coolest projects, the best practices, and the biggest
[1770.94 → 1772.78] stories each and every week.
[1772.78 → 1778.00] Make changelog.com your daily destination, or hit the snooze button and subscribe to our
[1778.00 → 1780.92] weekly newsletter that hits inboxes on Sunday mornings.
[1781.52 → 1784.46] Join more than 15,000 enthusiastic readers.
[1784.72 → 1790.56] It'll cost you exactly zero dollars, and you can subscribe right now at changelog.com slash
[1790.56 → 1790.88] weekly.
[1790.88 → 1791.00] Thank you.
[1802.78 → 1807.82] All right.
[1807.88 → 1813.12] Well, we've talked a good bit about the tooling and the code and everything that is out there.
[1813.12 → 1818.52] I'm curious for you, like, let's say that you're approaching a problem, and you're using
[1818.52 → 1823.18] a new toolkit, like the maybe it's the D graph thing that you're talking about, like
[1823.18 → 1824.96] you're wanting to get into that.
[1825.02 → 1829.22] Or, you know, for me recently, I was doing some speech related things.
[1829.22 → 1834.04] There's like some new speech related stuff out of NVIDIA that's pretty interesting.
[1834.48 → 1838.44] So there's this new toolkit of things that you have access to.
[1838.66 → 1846.20] But one of the things that I see people struggling with is integrating that toolkit of stuff into
[1846.20 → 1852.56] your, you know, local machine to experiment with might not actually always be the easiest
[1852.56 → 1859.90] thing because, you know, oh, this new toolkit, it actually requires this version of NumPy.
[1860.18 → 1862.08] And you have this version of NumPy.
[1862.18 → 1866.76] But if you change this version of NumPy on your local system, then you break these 14 other things
[1866.76 → 1868.04] that you use locally, right?
[1868.26 → 1870.86] So I'm curious how you go about that, Chris.
[1871.52 → 1874.70] So a couple of ways of entering into that answer.
[1874.80 → 1876.92] One is I start with the end in mind.
[1877.24 → 1881.80] Am I just trying to learn something new in terms of like a new skill or a new workflow?
[1881.80 → 1886.32] And if I'm doing something like that, then I might stick much closer to that tutorial
[1886.32 → 1887.76] specifics and stuff.
[1888.00 → 1893.82] And if I want to do that, I might do it in a Docker container entirely where I can control
[1893.82 → 1895.62] the environment and the versions of everything.
[1895.74 → 1900.06] If they haven't done that for me, then as I get into the tutorial, I'll scan through the
[1900.06 → 1904.48] tutorial, see what they're using and go ahead and set myself up a Docker container for
[1904.48 → 1905.14] that process.
[1905.14 → 1910.64] And that way I have a constrained environment that exactly meets the tutorial's focus and
[1910.64 → 1912.50] can get through it with fewer problems.
[1912.50 → 1916.00] It's worth the investment of Voucherizing it ahead of time if they haven't done that for
[1916.00 → 1916.18] you.
[1916.62 → 1917.58] So that's one thing.
[1917.98 → 1923.14] But in general, if I'm not just doing a pure learning spike, you know, where I'm just trying
[1923.14 → 1928.38] to figure out how to do this thing that I care about, if I'm doing it with more of production
[1928.38 → 1932.96] or productivity in mind, then I think what is the environment this has to meet?
[1933.02 → 1938.32] And if I'm maybe looking at a tutorial, but then I'll translate it into what are the constraints
[1938.32 → 1939.00] that I have?
[1939.10 → 1940.88] What are the resources that I have available?
[1941.06 → 1945.40] And I'll take a little bit of time to try to transfer what they're trying to show me
[1945.40 → 1947.76] there into the world that I'm living in.
[1947.82 → 1952.18] Because at the end of the day, if I'm not just doing a pure learning spike, and I'm doing
[1952.18 → 1956.30] it to deploy somewhere eventually, then it needs to fit into my world.
[1956.36 → 1960.22] And so there's a little bit of prep time there to try to get a smooth workflow on my side
[1960.22 → 1960.50] going.
[1960.50 → 1962.00] Yeah, for sure.
[1962.36 → 1968.00] One of the things that I do a lot is if I'm just trying to see, well, like, let's say that
[1968.00 → 1972.74] I'm trying to solve a problem, like it's a speech recognition problem or something.
[1973.00 → 1977.80] And I see there's like three different things that people are talking about using out there,
[1978.32 → 1979.92] three different ways of going about it.
[1980.10 → 1984.04] What I might do is just spin up three different Google Cola notebooks.
[1984.26 → 1984.52] Yeah.
[1984.52 → 1987.58] Because whatever I do there, it's going to get blown away.
[1987.78 → 1989.88] It doesn't affect my local environment at all.
[1989.98 → 1994.26] But it is persisted, like in the sense of like the code is persisted.
[1994.56 → 1995.56] It is a notebook.
[1995.56 → 2000.86] So you sometimes have sort of weird state, and you're not guaranteed that it's going to run
[2000.86 → 2002.64] exactly the same way again.
[2002.64 → 2007.90] But it does give you a very quick way of like knowing, OK, I have this environment, TensorFlow,
[2008.12 → 2013.62] PyTorch, Pandas, you know, Spacey, a lot of other things are already installed.
[2013.62 → 2019.66] And so there may be a couple of things I need to install via pip or something, but I can
[2019.66 → 2024.94] generally run through and get the flavour of how something is going to feel very quickly.
[2025.58 → 2029.82] And oftentimes what I'll do is I'll spin up three different notebooks and try to get this
[2029.82 → 2032.80] thing to run in the way they're saying, and it doesn't work.
[2032.84 → 2036.96] And then I try a different thing to get it running in the way they say, and then it's kind
[2036.96 → 2037.36] of annoying.
[2037.66 → 2043.08] And then I try a third thing, and then it seems like not exactly what I want, but it seems like
[2043.08 → 2044.32] the workflow is kind of nice.
[2044.40 → 2046.36] So then I'll start adjusting from there.
[2046.44 → 2050.74] So even just finding the good starting point where you want to put your flag in the ground
[2050.74 → 2054.42] tool kit wise, it can be useful to do it in that way.
[2054.46 → 2055.18] From what I've seen.
[2055.58 → 2059.52] You know if I could go back, that is the one thing I would change about if I don't go
[2059.52 → 2064.40] off and do a Docker container for pure ease of learning and ease of training.
[2064.88 → 2066.42] Nothing beats Cola in my view.
[2066.42 → 2066.86] Yeah.
[2067.02 → 2071.84] They have the best simplified interface that has everything that you need there.
[2072.00 → 2075.72] And so, yes, given that option, I will often use Cola to go do that.
[2075.84 → 2079.40] And I know a lot of other people besides you and me that feel the same way.
[2079.58 → 2083.94] Sometimes I find myself wishing that other tools would look at Cola, recognize the ease
[2083.94 → 2086.52] that they've created for their own user and go implement that.
[2086.58 → 2088.28] I'd like to see that kind of ease of use everywhere.
[2088.70 → 2088.90] Yeah.
[2088.90 → 2095.18] Well, it would be unfair, I think, to talk about all the great things that people are
[2095.18 → 2101.70] putting out there in the open in terms of data and code and not talk about how you can
[2101.70 → 2104.82] contribute to that or help out a project.
[2105.18 → 2108.96] Or maybe it's your own project, and you want to open it up.
[2108.96 → 2119.22] What are the kind of flavours or categories of contributions that you think people getting
[2119.22 → 2122.58] into contributing to open source AI?
[2123.18 → 2127.86] What are the sorts of things that they might have in their mind that would be maybe useful
[2127.86 → 2130.00] things to think about contributing to?
[2130.70 → 2137.14] So, I mean, some of the common categories of contribution would be obviously the code itself
[2137.14 → 2139.16] that is the core for that software.
[2139.72 → 2142.42] But code alone is often not enough.
[2142.54 → 2148.30] I can't count the number of times that I've tried to work with code that without great
[2148.30 → 2153.46] documentation and without great examples, I've found to be extremely hard to utilize in
[2153.46 → 2154.08] a productive way.
[2154.20 → 2159.80] And so if you don't feel that code is where you should make your contribution, then going
[2159.80 → 2165.98] and figuring out how to use the tool or offering up your insights from using the tool into
[2165.98 → 2167.66] documentation or create examples.
[2167.66 → 2170.30] I love it when people create examples.
[2170.92 → 2175.54] And so if I'm coming in cold, and I really don't understand the tool, a lot of times that's
[2175.54 → 2179.48] the best way for me to ramp up is I go to an example, and then I refer to the docs from
[2179.48 → 2181.16] there to try to get there.
[2181.30 → 2183.30] And so those are some of the obvious things.
[2183.44 → 2188.20] And another thing that I would suggest people do is reach out to the maintainer of the project
[2188.20 → 2190.64] and ask them and say, what do you need?
[2190.80 → 2192.86] A lot of times there's a Slack team or something.
[2192.86 → 2193.14] Absolutely.
[2194.06 → 2198.76] And tell them you love what they're doing, and you would like to contribute and tell them
[2198.76 → 2203.50] what you think you're good at contributing with and ask them for some guidance on that
[2203.50 → 2204.38] and they will love you.
[2204.54 → 2209.54] I mean, open source projects, there are cases where you have paid teams that are maintaining,
[2209.72 → 2210.04] obviously.
[2210.66 → 2215.64] But if you look at the vast numbers, the majority of maintainers out there are maintaining it
[2215.64 → 2216.34] for free.
[2216.42 → 2219.08] They're not being paid to do that on most projects.
[2219.34 → 2220.58] And so they love it.
[2220.58 → 2223.00] And be sure to tell them how much you love their software as you do it.
[2223.36 → 2224.14] Help them with data.
[2224.48 → 2227.48] Is there data that I could go out, and we can make links to or find data?
[2228.08 → 2228.40] Whatever.
[2229.16 → 2229.30] Yeah.
[2229.50 → 2230.70] I think that's a good point.
[2231.02 → 2235.38] Some of the larger projects like we've been talking about, you know, TensorFlow and others
[2235.38 → 2236.86] have a large team behind them.
[2237.26 → 2237.56] Right.
[2237.56 → 2243.40] But there's a lot of really great tooling out there, you know, smaller tools that are actually
[2243.40 → 2252.72] pretty key in the workflow that are developed and maintained by maybe one or two unpaid
[2252.72 → 2255.88] people that are doing it because they think that this thing is useful.
[2255.88 → 2258.02] So that's one thing to keep in mind.
[2258.30 → 2264.48] Also, as you're using open source software, that when you're using something, and it doesn't
[2264.48 → 2270.14] do quite the thing you want, or maybe it breaks in a certain way, the way that you go about
[2270.14 → 2277.76] raising that to the maintainers shouldn't be coming from a place of why does your tool
[2277.76 → 2279.06] suck so bad?
[2279.42 → 2282.52] You are terrible and need to do a better job.
[2282.52 → 2288.30] So the better way to go about it is to say, hey, thank you so much for, you know, creating
[2288.30 → 2289.04] this thing.
[2289.44 → 2291.88] I've noticed this to raise an issue on GitHub.
[2292.08 → 2293.16] You could definitely do that.
[2293.24 → 2299.40] But I think the even better way to go about it is to say, okay, this thing might need a
[2299.40 → 2300.64] slight modification here.
[2300.76 → 2305.00] Maybe I could reach out to the maintainer and see if they would accept a contribution to
[2305.00 → 2306.42] add that feature in.
[2306.42 → 2312.88] And then you could actually create a pull request and contribute that in.
[2313.32 → 2319.22] It's a much more productive way of going about interacting with open source projects.
[2319.64 → 2324.94] And for those who don't know what a pull request is, it is a mechanism by which you essentially
[2324.94 → 2329.86] offer up your code to be integrated into a larger code base.
[2329.86 → 2335.02] And it gives the maintainer of that code base the chance to review what you're doing and
[2335.02 → 2336.40] choose to integrate it or not.
[2336.46 → 2338.46] And if they don't, there might be a perfect reason.
[2338.54 → 2340.94] And they'll give you feedback typically on what that is.
[2341.02 → 2342.32] But they're already spending their time.
[2342.44 → 2346.36] So I love what you said, Daniel, about don't just say I need a feature.
[2346.50 → 2349.84] Open source is democratized software to some degree.
[2350.30 → 2355.40] Go out there, talk to them ahead of time, and then say, I'd like to take a stab at writing
[2355.40 → 2357.02] code for this and offer it up.
[2357.02 → 2358.42] And they can choose to take it or not.
[2358.56 → 2360.78] And they may give you some guidance if they're grateful for it.
[2361.14 → 2362.78] Yeah, I like what you say as well.
[2363.04 → 2366.64] There is a contribution process that's common to GitHub.
[2367.04 → 2368.74] There's a lot of jargon around that.
[2369.20 → 2375.16] And what we'll do is we'll include as a learning resource on this episode, there's a couple of
[2375.16 → 2380.52] perfect blog posts out there about this whole process where there's a repo on GitHub.
[2381.34 → 2383.02] You maybe want to contribute.
[2383.46 → 2386.62] When we're saying contribute, it could be something small, right?
[2386.62 → 2395.82] If you see in a project's documentation that they have this error in their documentation
[2395.82 → 2398.92] and it's just a wording change, right?
[2399.04 → 2403.28] Or maybe a change of a variable name or whatever it is in their documentation.
[2403.48 → 2404.24] It's a small thing.
[2405.06 → 2409.90] You, of course, could create an issue on GitHub and say, hey, you need to fix this.
[2409.90 → 2419.30] But it's super quick and not that hard to just go to their repo, see how they have their documentation
[2419.30 → 2420.88] laid out in their repo.
[2421.24 → 2427.96] And then it's a matter of forking that or making a copy of that repo, pulling that down to your
[2427.96 → 2433.24] local machine, you know, making the change, pushing that back up to GitHub and then creating
[2433.24 → 2435.54] this thing, like Chris said, like the pull request.
[2435.54 → 2438.30] And so that's like a no-brainer.
[2438.44 → 2442.70] You know, you don't need to know that the contributors are going to want that change.
[2442.88 → 2443.94] They may reject it.
[2444.06 → 2448.10] But I think more than likely, they're going to be just happy that people found something
[2448.10 → 2450.08] wrong with their documentation and fixed it.
[2450.40 → 2453.38] So, yeah, I think that that workflow will give a good link.
[2453.52 → 2457.86] If you're new to GitHub, if you're new to Git and this process of pull requests and all
[2457.86 → 2461.20] of that, we'll put a link in so that you can learn a little bit about that.
[2461.20 → 2462.40] Yeah, absolutely.
[2462.52 → 2468.32] Another way to contribute is if you're using that software, and it's working for you well
[2468.32 → 2473.38] and you're solving something that's important to you, share that process, not just what you're
[2473.38 → 2477.22] doing, but how you did it, how you use the software in a blog post.
[2477.74 → 2482.56] And so that doesn't actually directly require interacting with the maintainer of the software,
[2482.56 → 2484.56] but it is showing appreciation.
[2484.66 → 2489.30] It is giving back to the community by showing how to use it effectively and may inform them
[2489.30 → 2491.68] about not only what you've done, but your workflow.
[2492.00 → 2495.34] And all of that is really useful to other people and very community minded.
[2495.98 → 2501.60] Yeah, actually, there's a couple of perfect blog posts out there about building AI
[2501.60 → 2504.76] workstations like personal computer with the GPU and all.
[2504.90 → 2511.02] And I relied on those very, very heavily because it's been so long since I put together a computer
[2511.02 → 2512.14] of my own.
[2512.14 → 2519.82] Like my reference frame was like way back when stuff was named differently and like processors
[2519.82 → 2521.54] were not near what they are now.
[2521.68 → 2526.44] And so just like getting a bearing of like, what range of things do I need to be looking
[2526.44 → 2526.94] at here?
[2527.02 → 2529.60] And what configurations are people going after?
[2529.68 → 2531.42] That was really useful.
[2531.42 → 2539.08] So even if it's like a guide like that, installing CUBA and getting your new GPU running, you
[2539.08 → 2541.30] know, that sort of stuff is really useful.
[2541.80 → 2546.72] And of course, there's a lot of that particular blog post out there probably, but there's other
[2546.72 → 2547.68] things that aren't.
[2547.84 → 2549.98] I'm a Packet Arm user, and we've had them on the show.
[2550.12 → 2554.04] And there's this new GitHub actions thing that people might be familiar with where you can
[2554.04 → 2557.44] kind of automate tests and deployments through GitHub.
[2557.44 → 2563.94] And I asked in their Slack, like, has anyone tried to do like a data pipeline from GitHub
[2563.94 → 2564.56] actions?
[2565.20 → 2568.86] And like, and there were a couple of people that responded in Slack, like, no, but I've
[2568.86 → 2570.66] been thinking about trying it and that sort of thing.
[2570.74 → 2575.38] So like, if I end up doing that, I think that would be something that would be really great.
[2575.60 → 2580.88] It's probably not something that they're going to pull into their main repo, maybe because
[2580.88 → 2582.28] it's sort of an auxiliary thing.
[2582.74 → 2587.10] But it would be something that would be really nice for a blog post so that those people out
[2587.10 → 2592.06] there that are trying to do that thing could find a resource and do that.
[2592.54 → 2592.60] Yeah.
[2592.72 → 2597.36] You know, as you say that, a thought occurred to me that I think is something that hasn't
[2597.36 → 2599.56] matured in the AI world that needs to.
[2600.08 → 2604.28] And that is the fact that by comparison, if you look in the software world, not only do
[2604.28 → 2612.16] you have communities around specific software packages that are developed, but you also at
[2612.16 → 2617.44] the same time have a general sense of community around open source software that even transcends
[2617.44 → 2619.72] the specific language and libraries that you're in.
[2620.06 → 2624.92] You can go from one language to another and there may be little changes and stuff and how
[2624.92 → 2626.96] that the sub communities work.
[2627.06 → 2630.50] There is an understanding and what is expected in open source in general.
[2630.72 → 2633.04] I think that we're not there yet with AI.
[2633.04 → 2636.98] And I think that would be something I know from our conversations that we'd both love
[2636.98 → 2644.08] to see is instead of just having specific data sets or specific software packages, a
[2644.08 → 2648.88] sense of open AI and a larger community sense being built in a sense of community.
[2648.88 → 2655.58] So whether you're using, you know, PyTorch with a particular data set or TensorFlow or whatever
[2655.58 → 2658.64] or NVIDIA stuff, it doesn't matter.
[2658.64 → 2662.92] There is an overall sense as you move through these communities on what to expect in that
[2662.92 → 2663.38] AI world.
[2663.54 → 2668.24] And I think I've met so many people in AI that did not come from the software world and did
[2668.24 → 2672.84] not already have that built into it that we have some integration to do on that.
[2672.94 → 2675.38] So I'd like to see that happen going forward here.
[2676.20 → 2676.28] Yeah.
[2676.36 → 2680.32] And there have been some, you know, encouraging signs on that front.
[2680.64 → 2687.52] I think both TensorFlow and PyTorch have developed their various hub sorts of environments where
[2687.52 → 2693.48] you can share, you know, setups and models and configuration and all of that.
[2693.64 → 2694.84] So that's kind of nice.
[2694.88 → 2697.56] Like there's this kind of sense that people are building these hubs.
[2697.56 → 2703.72] And I also think about, of course, the Hugging Face team that now has just tons of models
[2703.72 → 2706.28] that are available in their open source project.
[2706.48 → 2707.18] I saw a tweet.
[2707.26 → 2713.32] I was just pulling it up from Clem, who was on the show quite a while back from Hugging Face.
[2713.32 → 2714.62] We'll link to that episode.
[2714.82 → 2721.02] But his tweet was 25 team members plus 400 open source contributors plus machine learning
[2721.02 → 2725.90] equals fastest technology building I've ever seen, which I think is definitely true.
[2726.00 → 2730.44] You just look at the pace with which they're developing, you know, being, I guess what he's
[2730.44 → 2734.90] saying, 25 actual team members now, but 400 open source contributors.
[2735.14 → 2738.60] There's sort of these pockets of the community like you're talking about.
[2738.80 → 2741.20] And so I hope that we see that growing.
[2741.20 → 2742.08] I do too.
[2742.16 → 2743.40] I think that's a great way to finish.
[2743.68 → 2745.76] I mean, it's not just about your team.
[2745.94 → 2750.72] You're really standing on the shoulders of an entire community of people out there that
[2750.72 → 2753.70] have contributed to tools and made data available and all that.
[2753.82 → 2755.26] All of us are in that position.
[2755.96 → 2760.20] So as folks move forward, be thinking about how you can give back to this community and
[2760.20 → 2761.30] build that sense of community.
[2761.56 → 2762.86] Great conversation today, Daniel.
[2763.26 → 2764.00] Yeah, for sure.
[2764.16 → 2765.12] That was a great idea.
[2765.22 → 2766.28] Thank you for coming up with it.
[2766.60 → 2767.30] Yeah, definitely.
[2767.74 → 2770.98] Hope you enjoyed the hot weather and stay safe.
[2770.98 → 2773.38] Stay inside, and we'll talk to you soon.
[2773.74 → 2774.14] Will do.
[2774.28 → 2774.68] Take care.
[2775.00 → 2775.16] Bye.
[2778.72 → 2782.00] Thank you for listening to this episode of Practical AI.
[2782.36 → 2783.60] People ask us all the time.
[2783.72 → 2785.32] They say, hey, how can I support your work?
[2785.86 → 2789.68] One easy way is to leave a five-star review on Apple podcasts.
[2790.46 → 2792.76] Tell folks why you listen and why they should too.
[2792.90 → 2794.20] It only takes about 30 seconds.
[2794.36 → 2798.98] And believe it or not, those ratings and reviews really do help us rank higher in AI related
[2798.98 → 2799.68] search results.
[2800.28 → 2803.12] Practical AI is hosted by Daniel Whiten ack and Chris Benson.
[2803.60 → 2804.78] It's produced by Jared Santo.
[2805.06 → 2805.54] That's me.
[2805.98 → 2808.94] And our music is brought to you by the one and only Break master Cylinder.
[2809.48 → 2812.58] We are sponsored by amazing people at companies who get it.
[2812.80 → 2814.74] Thanks again to Vastly, Linde and Rollbar.
[2815.20 → 2817.80] Did you know we have a master feed of all Change Dog podcasts?
[2818.14 → 2818.62] We do.
[2819.04 → 2820.92] It's your one-stop shop for everything we produce.
[2820.92 → 2824.40] If you like this show, you'll love the Change Log, Brain Science and Go Time.
[2824.60 → 2828.86] Check it out at changelog.com slash master or search for Change Log Master in your favourite
[2828.86 → 2829.58] podcast app.
[2829.84 → 2830.50] You'll find us.
[2830.88 → 2831.68] That's it for now.
[2831.88 → 2833.08] We'll talk to you again next week.
