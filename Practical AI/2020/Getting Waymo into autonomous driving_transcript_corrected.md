[0.00 → 5.50] So if you look at generally the stacks of modern autonomous driving companies,
[6.06 → 11.88] a large part of them use all three sensors or a subset, which is camera, ladder, and radar.
[12.30 → 17.86] Some also use thermal cameras, occasionally even more creative sensors, sonar, and so on.
[17.86 → 19.46] But those three are the mainstay.
[19.86 → 23.52] And I think each of them brings something unique and powerful to the table.
[25.90 → 28.32] Bandwidth for Changelog is provided by Vastly.
[28.32 → 30.58] Learn more at Fastly.com.
[30.82 → 33.90] We move fast and fix things here at Changelog because of Rollbar.
[34.02 → 35.72] Check them out at Rollbar.com.
[35.96 → 38.12] And we're hosted on Linde cloud servers.
[38.48 → 40.48] Head to linode.com slash Changelog.
[43.46 → 45.28] Linde is our cloud server of choice.
[45.82 → 48.74] Grab the NATO plan for just $5 a month, just $5.
[49.12 → 54.30] That gets you a gig of RAM, a blazing fast 25 gig SSD, and one terabyte of transfer.
[54.60 → 57.06] Let's be honest, you can go a long ways on that $5.
[57.06 → 61.94] When you do need to scale up, their prices are predictable, so you can put your calculator down.
[62.06 → 62.60] You won't need it.
[62.90 → 68.08] We've been running ChangeLog.com on Linde for years, and we've always impressed by their award-winning support team.
[68.62 → 71.32] Check them out at linode.com slash changelog.
[71.52 → 74.70] Once again, that's linode.com slash changelog.
[74.70 → 91.22] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[91.48 → 95.62] This is where conversations around AI, machine learning, and data science happen.
[95.70 → 101.98] Join the community and Slack with us around various topics of the show at changelog.com slash community, and follow us on Twitter.
[102.12 → 103.70] We're at Practical AI FM.
[103.70 → 113.42] Welcome to another episode of the Practical AI podcast.
[114.40 → 117.66] Hopefully today we're going to have some fun stuff that we haven't covered before.
[117.82 → 118.84] My name is Chris Benson.
[119.46 → 124.68] I work at Lockheed Martin, and with me is Daniel Whiten ack, a data scientist at SIL International.
[124.88 → 125.68] How's it going today, Daniel?
[126.06 → 127.04] Oh, it's going great.
[127.04 → 129.20] It was an interesting weekend.
[129.44 → 133.64] I actually got to get out of the house, which was a good thing, you know, during COVID.
[134.00 → 141.48] My pastor and his wife took us out on a little boat, and it was quite an adventurous time because we went, we got to get outside.
[141.76 → 142.44] It was beautiful.
[142.44 → 148.24] But then the boat broke down, and we had to, like, get a tow back to the dock and all that.
[148.32 → 149.82] So it was an interesting weekend.
[150.16 → 156.68] Nice, like, you know, away from the computer, out in nature, but it was an adventure.
[156.92 → 157.98] So what about yourself?
[158.38 → 160.44] I think yours was much more adventurous than mine.
[160.44 → 165.32] We managed to adopt out one of our foster dogs.
[165.50 → 169.36] So we're down to only seven dogs now in the house.
[169.78 → 170.76] Only seven dogs.
[171.56 → 173.00] Went into the weekend with eight.
[173.14 → 174.22] So that's good.
[174.72 → 177.24] And so that's always a nice little family weekend in that way.
[177.52 → 178.96] Yeah, yeah, for sure.
[179.10 → 180.98] Now back to some fun AI stuff.
[181.06 → 182.52] I've got a few things going.
[182.64 → 185.96] Actually, I got a new project I'm working on, which hopefully I can.
[186.38 → 189.46] Right now, I can't share everything about it.
[189.46 → 191.78] But hopefully I'll be able to share some soon.
[192.00 → 197.36] It's speech related, and it's some pretty fun stuff with local languages here at SIL.
[197.58 → 199.64] So hopefully I'll be able to share that at some point.
[200.16 → 205.14] But I know today we're doing something with, you know, I was just talking before the show
[205.14 → 210.28] that after even 100 or more episodes, there's still things on the show.
[210.38 → 215.96] So many interesting topics going on with AI that we haven't had full shows devoted to certain things.
[216.10 → 217.64] And we've got one of those today, right?
[217.64 → 219.74] And it's a big one as well.
[220.00 → 221.74] I'm just, you know, I was kind of shocked.
[222.28 → 224.80] How did, yeah, over 100 episodes and we missed this one.
[224.86 → 225.74] This is insane.
[226.22 → 226.38] Yeah.
[226.50 → 232.82] And so today I wanted to welcome on to the show, if I get your name correct, it's Drag
[232.82 → 233.60] Anglo.
[233.70 → 235.00] Did I come anywhere close there?
[235.24 → 236.38] Sounds good, actually.
[236.48 → 236.88] Thank you.
[236.98 → 238.00] Yeah, that was quite good.
[238.10 → 238.26] Yeah.
[238.56 → 239.50] Thanks for having me.
[239.50 → 243.34] You are a principal scientist and head of research at Waymo.
[244.02 → 247.14] And we're going to talk a bit today about autonomy, I believe.
[247.24 → 247.76] Is that correct?
[248.74 → 250.46] Sounds like a good topic for me.
[250.68 → 251.48] I enjoy it.
[251.74 → 252.98] A topic I love too.
[253.14 → 255.40] It's one that I touch in my work life.
[255.56 → 259.58] And so can't believe we haven't talked about it on the show in the depth it deserves.
[259.80 → 259.90] Yeah.
[260.12 → 262.50] Chris is going to nerd out today quite a bit.
[262.56 → 263.30] Oh, yeah.
[263.42 → 264.24] This is great.
[264.24 → 266.44] We've been talking about NLP too much.
[266.74 → 267.52] We need a break.
[268.62 → 272.92] It's a very quickly developing area with a lot of great technology coming out.
[273.02 → 274.00] So it's not surprising.
[274.50 → 274.76] Yeah.
[274.88 → 276.46] And some good systems too.
[276.94 → 277.18] Yeah.
[277.18 → 279.44] He's just schooling me on NLP on every episode.
[279.80 → 281.04] So I don't know about that.
[281.18 → 283.68] How many GPT-3 episodes have you had so far?
[283.90 → 287.38] Well, I think it's come up in a number of them.
[287.52 → 289.94] We had Hugging Face on not too long ago.
[290.06 → 292.12] So that was a good like Transformer episode.
[292.72 → 293.56] Yeah, it is.
[293.56 → 297.10] Like you say, I'm a little bit biased in that way.
[297.20 → 298.18] But I'm excited.
[298.40 → 303.08] It's so cool to also see, like I mentioned at the beginning, I'm starting to work on some
[303.08 → 303.78] speech stuff.
[304.10 → 309.40] Because it works a lot with male spectrograms and other things, there's a lot of overlap
[309.40 → 311.88] with sort of computer vision types of models.
[312.10 → 315.52] And so it's cool for me to kind of dip back into some of that stuff.
[315.64 → 319.12] And it'll be awesome to discuss some of the computer vision things today.
[319.56 → 321.42] You know, Daniel was mentioning they couldn't talk about it.
[321.46 → 322.18] I'm suspicious.
[322.18 → 324.70] Maybe he's going to release GPT-4 for the world.
[325.72 → 326.66] Yeah, that must be it.
[326.72 → 328.46] Maybe that's next week's episode, right?
[328.86 → 332.84] With all of my GPU clusters in my house here.
[333.14 → 334.26] Right behind you.
[334.34 → 334.62] Yes.
[334.70 → 335.24] In the picture.
[335.30 → 335.86] Yeah, exactly.
[336.16 → 336.38] Yeah.
[336.38 → 339.34] So for listeners, since you don't have the visual, we're on the Zoom call.
[339.34 → 341.04] I think we've mentioned this a couple of times.
[341.40 → 342.00] Yeah, we have.
[342.08 → 345.44] But Daniel always has the data centre in the background behind him there.
[345.56 → 349.22] And so, you know, I think I'd be shocked to see something more domestic there.
[349.40 → 352.58] You know, I just figure you go home and go to bed in the data centre and get the air
[352.58 → 353.24] conditioner going.
[353.80 → 359.04] Well, before we go too deep down the rabbit hole of virtual Zoom backgrounds, Drag, could
[359.04 → 363.70] you give us a little bit maybe just about your background and how you got into self-driving
[363.70 → 365.30] cars and that whole world?
[365.30 → 367.46] What's your background, and how did you get into AI?
[367.96 → 372.74] I'm by nature a machine learning researcher and engineer.
[372.92 → 374.24] That's how I think of myself.
[375.08 → 380.86] And when I started learning about those fields, I was always drawn to robotics.
[381.58 → 388.84] And as such, I ended up doing a PhD at Stanford in machine learning, but with a focus on perception,
[389.48 → 390.90] 3D perception at the time.
[390.90 → 395.78] I was actually Daphne Killer's first PhD student that was focusing on perception.
[396.56 → 402.40] And as such, I had a very interesting overlap with Professor Sebastian Thrun because Daphne
[402.40 → 407.76] met him at a conference and sent me to his lab because we had no robots or any way to
[407.76 → 409.08] collect sensor data.
[409.54 → 410.60] And Sebastian did.
[410.98 → 415.12] Daphne sent me to Pittsburgh to collect some data with his robots.
[415.70 → 419.18] And that was my first more serious exposure to robotics.
[419.18 → 422.66] What really happened, though, was I spent three weeks in Pittsburgh.
[423.02 → 427.30] But unfortunately, just at the time when I went there, Sebastian's whole team got to
[427.30 → 428.08] go to Hawaii.
[428.66 → 430.36] I think something that he organized.
[430.64 → 432.36] So you were left alone with the robots?
[432.78 → 434.22] I was left alone with the robots.
[434.42 → 440.16] And since I'm primarily a software guy, I managed to short the main robot with which I was supposed
[440.16 → 442.40] to collect the data in fairly short order.
[442.62 → 444.10] So it was interesting times.
[444.10 → 449.20] Not too much data got collected, but we were lucky for Sebastian to come to Stanford.
[450.04 → 452.62] And so he became an unofficial advisor of sorts.
[452.62 → 454.56] And I got exposed to a lot of his work.
[455.10 → 459.30] It took me a while to get into self-driving, but I had been exposed to robotics and concepts
[459.30 → 462.58] there since 2000, I would say.
[463.54 → 467.02] And slowly but surely, my path led into this field.
[467.02 → 472.34] So can you tell us a little bit about going from Stanford and getting to Waymo and what
[472.34 → 476.90] some of those steps that kind of led you there along the way?
[477.42 → 481.78] I initially focused more on computer vision and 3D perception.
[482.00 → 483.20] That was my bread and butter.
[484.18 → 488.54] That was a great field that clearly would be empowered by machine learning.
[489.38 → 493.04] Originally, in those times, deep learning was not really that popular.
[493.04 → 498.16] Neural nets were considered to be the second-best thing to do anything, as they said in
[498.16 → 499.30] the Stanford AI lab.
[499.38 → 500.20] It was just a saying.
[500.30 → 502.44] People were just kind of jokingly saying that.
[503.10 → 507.92] And probably genetic engineering was the third-best way of doing anything, right?
[508.00 → 509.64] And we did a lot of graphical models.
[509.98 → 512.66] I was lucky to have a great advisor, Daphne Killer.
[512.72 → 514.02] That was my primary advisor.
[514.70 → 519.34] And she's a very accomplished professor with a lot of seminal work in graphical models.
[519.34 → 521.82] And those were the models at the time that actually worked.
[521.82 → 524.10] And so I did a lot of work in that.
[524.60 → 530.92] But when I graduated from Stanford, I felt that I would go into a startup.
[531.84 → 538.48] And so I spent two years in a computer vision startup, RIA, and later was known as lag.com,
[538.78 → 543.34] where we did face recognition in photo albums, and we did visual search for shopping.
[543.34 → 551.46] Eventually, though, it became too much of a website and the computer vision became more of a second
[551.46 → 552.22] class citizen.
[552.22 → 555.16] And I felt that it might be a great idea to join Google.
[555.64 → 561.46] And so I spent eight years at Google, never in self-driving at the time, but in areas that
[561.46 → 562.94] are very, very closely related.
[563.08 → 564.46] So one of them was Street View.
[564.46 → 571.76] At Street View, I learned a lot about nonlinear least squares and feature matching and bundle
[571.76 → 574.80] adjustment, structure from motion, SLAM.
[575.16 → 579.62] I had to because I was tech lead for pose estimation and three division at Street View.
[579.74 → 583.14] So that was the field I really got to exercise a lot.
[583.14 → 589.48] After doing quite a lot of very interesting work at Street View, which culminated in 2010,
[589.60 → 592.84] we did actually this, I don't know how much you guys follow this type of the literature,
[593.46 → 599.78] loop closing of the world, which are you took all the poses of all trajectories Street View
[599.78 → 600.94] cars ever drove.
[601.46 → 606.10] And we built a system with a guy called Samir Agarwal, who later developed a very popular
[606.10 → 614.10] solver called Ceres to register all of these runs of all the cars using the lighter sensor
[614.10 → 614.48] data.
[614.70 → 620.56] And later we tried the cameras, compute constraints between them and bring them into joint global
[620.56 → 621.48] coordinate systems.
[621.66 → 626.04] So after we accomplished this for all of Street View data, I felt, OK, it's time to go back
[626.04 → 626.86] to ML.
[627.64 → 629.66] You literally built the world.
[630.22 → 631.98] We loop closed the world, I would say.
[631.98 → 632.96] Yeah, loop closed the world.
[633.48 → 633.72] Right.
[633.82 → 635.82] And after you loop closes, you have all this sensor data.
[635.82 → 636.98] You can really map it well.
[637.52 → 637.64] Yeah.
[637.92 → 645.00] And afterwards, I switched to ML again, to a more experimental research team, which ended
[645.00 → 646.40] up in Google Research eventually.
[646.40 → 651.80] And what we did was initially Google Goggles, which was not the glass, which everyone knows,
[651.88 → 656.04] but it used to be a little app in your phone that you can take pictures, and it would tell
[656.04 → 657.20] you what the pictures are of.
[657.28 → 661.90] And at the time, it didn't work too well, but it pioneered a lot of the core concepts and
[661.90 → 662.74] even technologies.
[662.74 → 670.48] In fact, in around 2012, we were already doing quite serious deep nets at the time, only they
[670.48 → 674.00] weren't working as well because the neural net architectures were not very good.
[674.44 → 676.08] And then came Alex Net.
[676.26 → 681.14] And it was much better than anything we had that was not deep net based, as most people
[681.14 → 683.00] in the field also found out.
[683.30 → 684.70] And we found it very early.
[684.70 → 690.78] And so we switched to deep learning, and we developed a lot of this early neural net architectures
[690.78 → 695.48] for detection and classification that became quite popular afterwards.
[695.48 → 698.16] And we started working on annotating Google Photos.
[698.26 → 699.28] So I worked a lot on that.
[699.74 → 702.02] This is large scale image recognition and detection.
[702.72 → 706.76] And a lot of these skills are also very relevant for self-driving.
[706.76 → 712.58] And around 2015, I said, OK, this perception thing, we're starting to get the hang of it,
[712.92 → 715.72] at least for cameras, at least for images.
[716.18 → 718.86] It probably is finally time to go and do self-driving.
[719.02 → 721.22] And so in 2015, I got involved in self-driving.
[721.40 → 722.52] And so I'm here today.
[723.06 → 723.28] Gotcha.
[723.72 → 727.54] This is really the first focus episode we've had on self-driving.
[727.54 → 731.92] And it is one of those things that when people think of AI, one of the first things that
[731.92 → 737.50] come to mind is, oh, you know, self-driving is an example of applications of AI.
[738.16 → 745.26] Maybe you could just give us a sort of state of self-driving cars in terms of like for people
[745.26 → 750.06] looking from the outside, they might have a variety of perceptions and expectations all
[750.06 → 755.44] the way from, oh, yeah, we have self-driving cars now that work great to I'm not convinced
[755.44 → 758.52] that any car could self-drive, you know, where are we at?
[758.68 → 763.12] It just sort of generally, what's the sort of state of where we're at with self-driving
[763.12 → 764.38] cars in industry?
[764.92 → 769.14] Overall, I feel the industry has made a lot of progress and this progress is accelerating.
[769.68 → 773.18] At Waymo, we have been at this for over 10 years now.
[773.68 → 779.68] And even in 2010, 2011, when I was not directly with Waymo, they still had a lot of awesome
[779.68 → 785.32] demos and very impressive driving and behaviours that they were doing there, right?
[786.00 → 792.72] It's just the level and the complexity of what you need to do to launch safely, fully driverless
[792.72 → 797.64] product is unlike most products that have ever been launched.
[798.28 → 803.44] And so it takes a lot of time and iteration and understanding of all the details and corner
[803.44 → 803.94] cases.
[804.50 → 809.26] And so at Waymo, we've been working on improving the systems and we've been steadily improving.
[809.26 → 815.74] So we're now giving thousands of rides a week in Phoenix metro area.
[815.96 → 820.04] And before COVID, 5 to 10 percent of them were fully autonomous.
[820.64 → 825.58] This is quite a large area and quite general driving that we support there.
[825.72 → 830.88] So that to me is something that people don't talk as much about, but to me is a tremendous
[830.88 → 832.14] accomplishment already.
[832.14 → 840.52] And we're quite good currently at taking a specific area of interest, going out there
[840.52 → 842.46] and learning how to drive it.
[842.46 → 850.18] A lot of work, though, needs to go into making the system really scale to the variety of areas,
[850.76 → 857.62] diversity of situations, and even conditions in the types of intersections that you see,
[857.98 → 861.56] to the long tail of scenarios, to weather, right?
[861.56 → 866.68] And you want a system that scales quite seamlessly, the more you give it data.
[867.34 → 869.98] And this, machine learning has a very big role to play.
[870.86 → 873.84] And to me, that's an exciting multiplier.
[874.10 → 878.86] And so this will help bring this technology to much more areas further.
[879.48 → 882.80] You've kind of alluded to it and stuff, but as you're looking at this field,
[882.98 → 888.28] and especially as it's grown over the last few years and their new entrance, and it's maturing,
[888.28 → 891.48] what are those components that make up the field?
[891.60 → 897.72] What are all the kinds of areas of concern that you have to address when you're doing
[897.72 → 898.88] this kind of work in autonomy?
[899.12 → 904.98] There is actually two levels of, or two areas in which work needs to be done.
[905.06 → 909.58] And I would split it into a technological area and product and policy, right?
[909.64 → 914.08] And maybe it's easier to, if we're starting from a broader and then starting to narrow,
[914.20 → 916.32] maybe the latter is a good thing to describe.
[916.56 → 916.86] Sure.
[918.28 → 922.26] An autonomous driving product has not been created in the past, right?
[922.64 → 926.02] And the legislation for it is work in progress.
[926.44 → 930.38] And so this is an area where, you know, all the companies are focused a lot,
[930.46 → 934.16] working with governments at all levels and city councils and so on,
[934.18 → 940.74] to make sure that this product is developed to really serve the needs of the people that are using it,
[940.84 → 945.36] that they really work for the various interests and needs in the specific communities,
[945.36 → 952.28] that it has the right features because it's a different nature product than a car with a driver.
[952.92 → 960.64] And so this, all this area around compliance, regulation, product details is something that requires more work.
[960.64 → 970.32] Also, just to build the hardware at scale is a non-trivial effort that needs to be set up so that you can produce these vehicles at a good price point.
[970.66 → 974.30] Automotive companies have existed for over 100 years perfection.
[974.30 → 981.60] And they've been perfecting how to build vehicles efficiently, how to put these boxes together and integrate all the components.
[982.20 → 983.76] Now we have a lot more components.
[984.00 → 992.34] There is all the sensors in the compute and the safety features that we put into the vehicles that we need to learn to integrate efficiently.
[992.34 → 995.94] So that's on the policy side and the non-technological side.
[996.22 → 1001.16] On the technological side, there are a lot of interesting challenges in regard to,
[1001.88 → 1005.30] indeed, how do you handle the long tail, the rare events?
[1005.36 → 1006.98] How do you get to be robust to them?
[1007.56 → 1011.96] How do you efficiently, having, say, learned to drive in Phoenix,
[1012.12 → 1016.96] how do you easily adapt all of this stack to a new area and prove to yourself that you are safe there?
[1016.96 → 1021.70] How do you efficiently handle rare events in new areas and weather?
[1022.54 → 1029.80] Because each weather and condition leads to different behaviours and performance of both of your sensors
[1029.80 → 1034.84] and potentially of the other actors that react to the conditions that you need to be adapting to.
[1035.34 → 1039.64] So all of this is very fruitful areas for research.
[1039.80 → 1042.64] And I think this is all of these areas in technology.
[1042.64 → 1049.38] There is a lot of great base and there is a lot of great robotics and probabilistic robotics
[1049.38 → 1053.84] of the kind that Sebastian Iron used to do, modelling that has gone in it.
[1054.12 → 1058.38] What's really changing this area a lot is the advent of machine learning
[1058.38 → 1062.92] and its rapid development, which makes more and more things possible.
[1063.48 → 1067.44] And most of the companies, I think, we're reinventing our stack as we go,
[1067.54 → 1069.82] as these new capabilities that become possible.
[1069.82 → 1072.56] A lot of them we try to create ourselves with our research.
[1073.64 → 1076.08] This makes your system more and more adaptable.
[1077.22 → 1077.34] Right?
[1077.54 → 1083.08] And right now, machine learning, the true successes, I mean, already for over five years
[1083.08 → 1084.78] have been a lot in supervised learning.
[1085.88 → 1092.54] So you have a reasonable way to design these neural net architectures for specific tasks.
[1092.72 → 1096.60] They're universal function approximates, but it helps to have a good architecture.
[1097.32 → 1097.76] Right?
[1097.76 → 1100.92] And when you have this good architecture, and you define a good supervised problem
[1100.92 → 1104.80] and you label all the data you ever wanted, which may be hundreds of millions of boxes,
[1104.94 → 1105.68] we're really great.
[1107.72 → 1110.26] But that doesn't scale very well.
[1110.42 → 1110.76] Right?
[1110.76 → 1115.86] And so there are a lot of new paradigms over the last few years that have become very popular
[1115.86 → 1121.02] in how to make each step of this progress a lot more seamless and a lot more automatic.
[1121.02 → 1125.24] And when I got into this head of research role, I kept dreaming like,
[1125.34 → 1127.52] what's the dream system that I want to build?
[1128.36 → 1131.34] And to me always has been, okay, I want to go to a new city.
[1131.62 → 1135.10] We would just deploy a bunch of vehicles there with our drivers.
[1135.10 → 1139.22] We will tell them how we want them to drive so that they're way more like driving.
[1139.76 → 1141.74] Then we collect data maybe for months.
[1142.40 → 1147.06] And we just take all this data, and we put it in our systems, and they just improve and
[1147.06 → 1147.98] adapt to the city.
[1148.96 → 1150.66] And that can be in terms of perception.
[1150.98 → 1152.56] It can be in terms of behaviour prediction.
[1152.90 → 1154.44] It can be in terms of better planning.
[1154.96 → 1155.24] Right?
[1155.30 → 1157.16] By observing how everyone does everything.
[1158.00 → 1160.22] And hopefully almost all the way there.
[1160.22 → 1167.38] Of course, that's not yet necessarily realizable that just with a system that just observes,
[1167.48 → 1168.34] you can go all the way.
[1168.60 → 1172.92] Of course, there's always in a serious domain like this, a lot of room for great engineering
[1172.92 → 1174.86] and modelling as well to complement it.
[1175.32 → 1177.88] So it's usually an amalgamation of these two approaches.
[1178.62 → 1183.50] But you want also the first part to be possible because that really makes your system global.
[1184.68 → 1187.50] And so I think a lot of our projects are motivated by this vision.
[1187.50 → 1193.02] How do you take a piece that maybe has some heuristic or some too many assumptions that
[1193.02 → 1195.84] may not generalize to a very different environment?
[1196.28 → 1202.58] And how do we relax them with ML such that the system becomes able to handle a larger diversity
[1202.58 → 1207.02] of situations without people necessarily going in and coding it all?
[1217.50 → 1227.80] Changelog News is the best way to keep up with the fast-moving software world.
[1228.20 → 1234.34] We track, log, and contextualize the coolest projects, the best practices, and the biggest
[1234.34 → 1236.16] stories each and every week.
[1236.60 → 1241.40] Make changelog.com your daily destination or hit the snooze button and subscribe to our
[1241.40 → 1244.30] weekly newsletter that hits inboxes on Sunday mornings.
[1244.30 → 1247.86] Join more than 15,000 enthusiastic readers.
[1248.12 → 1250.26] It'll cost you exactly zero dollars.
[1250.62 → 1254.30] And you can subscribe right now at changelog.com slash weekly.
[1265.08 → 1271.20] So you started getting into the data side of things a second ago in terms of collecting
[1271.20 → 1273.56] certain types of data and what was needed.
[1273.68 → 1278.98] Maybe we could just kind of start breaking down the basic problem in terms of what data
[1278.98 → 1279.86] you're collecting.
[1280.48 → 1284.86] And then we could move on to talk about the various modular components, like you're saying,
[1284.96 → 1286.18] that drive the system.
[1286.98 → 1292.80] So in a Waymo self-driving car, at least, or maybe it's kind of standardized now, I'm not
[1292.80 → 1293.06] sure.
[1293.18 → 1296.98] But what are the main data inputs that you're working off of?
[1296.98 → 1299.76] I'm assuming cameras, but you mentioned LiDAR, I think.
[1299.86 → 1302.46] What's the combination of sensors that you're working with?
[1303.04 → 1310.72] So if you look at generally the stacks of modern autonomous driving companies, a large part of
[1310.72 → 1315.64] them use all three sensors or a subset, which is camera, LiDAR, and radar.
[1315.64 → 1323.40] Some also use thermal cameras, occasionally even more creative sensors, sonar, and so on.
[1323.64 → 1325.24] But those three are the mainstay.
[1326.20 → 1329.94] And I think each of them brings something unique and powerful to the table.
[1330.54 → 1334.46] For anyone who doesn't know what LiDAR is, because that tends to be used in this particular
[1334.46 → 1340.10] area, could you also just quickly say what that is for those that are not familiar with
[1340.10 → 1340.34] LiDAR?
[1340.46 → 1344.24] I think everyone knows radar, everyone knows cameras, but maybe not everyone knows LiDAR.
[1344.24 → 1347.70] So LiDAR stands for light detection and ranging.
[1348.56 → 1356.00] The LiDAR is a laser unit that sends out a laser pulse that then gets returned from the
[1356.00 → 1360.62] environment, and you can measure the time travel and potentially add attributes of the signal,
[1360.84 → 1363.72] like the intensity of the object that you measured.
[1364.22 → 1367.66] And so it gives a very accurate depth estimate to objects.
[1368.50 → 1372.26] Of course, radar also does give you depth estimate to objects.
[1372.26 → 1378.44] Radar has antenna that send out RF signal, and then the signals come back.
[1378.90 → 1385.14] But the radar signal is not quite as localized in its lower, typically, resolution.
[1385.86 → 1391.26] LiDAR is able to, especially the high-end LiDAR, is able to image the scene at very high resolutions
[1391.26 → 1392.36] with a single...
[1392.36 → 1395.86] So usually if the lighters are spinning or their imaging lighter, depending...
[1395.86 → 1397.46] Currently, there are different kinds.
[1397.90 → 1405.42] You can have up to a million returns in a spin of this or in this range image that it forms
[1405.42 → 1405.88] for you.
[1405.88 → 1411.28] And that's extremely rich description of the shape of all the objects and also their reflectance
[1411.28 → 1411.80] property.
[1411.80 → 1417.50] So if you're with Waymo or any of these other companies with their stacks that all have
[1417.50 → 1423.36] kind of these common three sensors in a generalized way, what is the advantage of camera?
[1423.68 → 1425.16] What is the advantage of LiDAR?
[1425.28 → 1426.46] What is the advantage of radar?
[1427.04 → 1432.82] How do you choose to apply the input you're getting from each of these types of sensors to
[1432.82 → 1433.44] form...
[1434.16 → 1437.64] I don't know what you would call it, but you're operating of your vehicle?
[1437.90 → 1440.94] How do they each contribute optimally to the overall picture there?
[1440.94 → 1447.98] So let me say first that now that I'm at Waymo, I am just amazed by the quality of our sensors.
[1449.06 → 1455.82] Waymo, one of the strengths of Waymo among many, and we can talk about them, is that Waymo
[1455.82 → 1462.28] has been already existing for 10 years, and it builds both its own sensor hardware and the
[1462.28 → 1464.84] software that then uses the sensor data.
[1465.96 → 1470.22] And so the sensors are top of the industry, I believe.
[1470.94 → 1476.94] And the setup is built such that both the hardware and software engineers can work together on the
[1476.94 → 1481.98] requirements that contribute to the operation domain requirements.
[1483.00 → 1486.38] And so that is, you know, privilege.
[1487.04 → 1493.42] Now, one caveat is that for each different self-driving company, the balance of these sensors is a bit
[1493.42 → 1495.06] different because everyone uses...
[1495.06 → 1497.56] Some of these have somewhat different characteristics, right?
[1497.56 → 1500.58] But overall, now let's generalize a bit.
[1501.06 → 1503.72] Camera is a standard sensor, very popular.
[1503.98 → 1504.76] It's very mature.
[1505.76 → 1507.88] It's the sensor that comes in the highest resolution.
[1508.06 → 1509.74] It has the highest amount of information.
[1510.52 → 1511.76] It's a passive sensor.
[1511.76 → 1519.90] So traditionally, we knew that all the information there in the camera is great to use, but before
[1519.90 → 1524.72] deep learning could not really take into use a lot of it for two reasons.
[1524.88 → 1529.68] Not only that the models themselves did not exist, but also to compute to really effectively
[1529.68 → 1532.42] process these large images did not really exist.
[1532.42 → 1534.68] And so now that's no longer true.
[1534.80 → 1538.74] So camera is an extremely powerful sensor, and you can do a lot with cameras.
[1539.88 → 1547.08] LiDAR became potentially historically over the last 10 years, the most popular sensor for
[1547.08 → 1547.64] self-driving.
[1547.98 → 1553.24] It is an unparalleled sensor in the sense that it combines really accurate dense depth.
[1553.24 → 1559.28] And it's an active sensor, which is important because it has additional benefit for safety.
[1559.80 → 1564.74] And honestly, if you start comparing the performance of these sensors, especially in areas of some
[1564.74 → 1570.28] reasonable proximity to the vehicle, which can be up to 100 meters, in terms of accuracy that
[1570.28 → 1576.52] you can obtain for your object modelling, at least at a geometric level, LiDAR dominates still,
[1576.94 → 1577.24] right?
[1577.60 → 1580.64] And the radar is also very popular for other reasons.
[1580.64 → 1587.66] It's really a great sensor for weather because the RF waves can travel reasonably well.
[1588.04 → 1596.84] They don't degrade as much as LiDAR and potentially camera in fog and rain, right?
[1596.92 → 1604.06] Also, radar is very complementary to cameras because cameras, they're really great at semantics
[1604.06 → 1606.50] and understanding what is there qualitatively.
[1606.50 → 1613.00] They're perfect at estimating the relative position, the lateral position of things and
[1613.00 → 1613.98] the lateral motion.
[1614.28 → 1619.08] But they're really not so good at estimating depth or velocity in the longitudinal relative
[1619.08 → 1621.70] to the ray in which you observe the object.
[1622.14 → 1626.98] And that's exactly what radar is good at because what radar does is, especially for metal objects,
[1627.42 → 1629.44] it measures super well the distance to it.
[1629.44 → 1637.06] And it also directly measures velocity, which for camera, it's a very derivative concept,
[1637.16 → 1639.08] which is yet more inaccurate.
[1639.60 → 1642.44] Radar really decreases the uncertainty in this measurement.
[1642.56 → 1645.20] So it really complements the strengths of cameras.
[1645.86 → 1647.62] And so that is a good property.
[1647.76 → 1649.10] Also, radars are very cheap.
[1649.10 → 1653.16] But they also have their shortcomings.
[1653.32 → 1657.22] Things like resolution and especially vertical resolution.
[1657.38 → 1660.54] Often, you need a lot of antennas to get vertical resolution.
[1661.36 → 1665.34] So things like overpasses and so on, you cannot tell if the object is potentially, especially
[1665.34 → 1669.74] for static objects above you or at your level, given the vertical resolution.
[1669.86 → 1671.08] And that's problematic, right?
[1671.10 → 1673.42] And this is something that radar, for example, can do well.
[1673.42 → 1679.84] And so each of these sensors, when put together, there is a case where one more sensor is good,
[1680.52 → 1680.82] right?
[1680.88 → 1685.68] And that's how at Waymo we have arrived to this combination of the three.
[1686.20 → 1689.98] And of course, ideally, you would say, oh, isn't it great to just have one sensor?
[1690.10 → 1690.64] What simplicity?
[1691.26 → 1697.56] But if you think about safety and ability to generalize to all conditions well, these three
[1697.56 → 1700.68] historically have proven very powerful together.
[1700.68 → 1707.12] And so Waymo's stack has evolved like this and a lot of the main manufacturers as well
[1707.12 → 1708.32] of self-driving systems.
[1709.02 → 1715.04] So before we jump into the actual models that are processing this data, it strikes me as we're
[1715.04 → 1719.52] talking about all of this, we have these various rich sources of data.
[1720.28 → 1724.92] And those are being combined, and I'm guessing pre-processed in various ways.
[1724.92 → 1730.92] And you're also running, in my understanding, a variety of models in the unit, in the car.
[1731.36 → 1739.04] What sort of compute is available to you like in the car itself to be able to, you know, respond
[1739.04 → 1740.36] in real time?
[1740.36 → 1745.40] What do your constraints compute wise and power wise and all of those things?
[1745.40 → 1747.54] I would think, you know, running in the car.
[1747.68 → 1753.14] Of course, it's not like a drone maybe where you're in the air and weights like a huge.
[1753.50 → 1757.04] I mean, it's still an issue, but it may not be as huge of an issue.
[1757.04 → 1760.06] But what are the constraints there and what sort of hardware are you working with?
[1760.10 → 1763.38] Do you have to have accelerators at the edge, or what are you working with?
[1763.56 → 1765.04] So let me just say a few things.
[1765.04 → 1771.26] I don't think I can really disclose the details of the Waymo compute in the car.
[1771.38 → 1772.10] And that's fine.
[1772.24 → 1773.36] Yeah, we're not surprised.
[1773.70 → 1774.04] All right.
[1774.08 → 1777.66] But I can describe roughly the considerations when you think about this.
[1777.94 → 1778.38] That's great.
[1778.64 → 1785.48] First, outdoors, you need to understand often objects up to quite a distant range.
[1786.08 → 1786.28] Yeah.
[1786.72 → 1791.92] Where maybe 300 meters in front of you, if you have a truck, you need to detect a cone or
[1791.92 → 1795.70] an obstacle that may cause you to start slowing down, right?
[1796.44 → 1801.14] And so you need to understand things over fairly long distances and also quite crowded scenes.
[1801.88 → 1807.26] If you're, say, in downtown San Francisco, I live in San Francisco, you go down, there
[1807.26 → 1811.46] could be hundreds of different people and dozens of vehicles all around you.
[1811.66 → 1817.48] And you need to make sense of the scene and be able to ultimately anticipate which parts
[1817.48 → 1819.40] of it are relevant for you and make decisions.
[1819.40 → 1828.02] This results in fairly large requirement for compute compared to most systems.
[1828.70 → 1836.48] Also, as we want to run more and more deep networks, and as you guys probably know, there's
[1836.48 → 1844.04] this nice trade-off in deep networks is more compute equals somewhat more quality, right?
[1844.04 → 1849.28] You generally want a compute stack that is perfect at running these machine learning models.
[1849.42 → 1852.02] Of course, CPU is also important that you have a good amount.
[1852.16 → 1856.24] You can't do everything in parallel neural network computations.
[1856.68 → 1860.54] So we want a lot of parallel compute for low wattage.
[1861.68 → 1867.30] Ideally, also certified system that is robust to shaking and the treatment it gets out there
[1867.30 → 1867.92] in the wild.
[1867.92 → 1875.56] And so you do want something like GPUs or TPUs, ideally, because that's what makes running
[1875.56 → 1877.64] these models tractable and possible.
[1877.82 → 1881.06] And of course, you can do dedicated hardware as well.
[1881.40 → 1883.10] So it's a bit evolving.
[1883.38 → 1889.62] I think the field starts with benefiting from a more flexible architecture that you can run
[1889.62 → 1897.74] more different models on, and then as we mature and hone down on the specific architectures and final
[1897.74 → 1904.06] models that work really well, still a work in progress, then I think the hardware will become
[1904.06 → 1908.08] more and more custom to those and gain more and more efficiency over time.
[1908.38 → 1909.96] So there's just a natural evolution.
[1910.14 → 1914.18] But you do want a lot of compute in parallel for low wattage.
[1914.18 → 1919.00] And this is the systems that most of our companies like ours are really looking at.
[1919.72 → 1922.38] So I'm wondering if you could kind of give us an overview.
[1922.86 → 1926.10] We know that you have your modular autonomous driving system.
[1926.78 → 1929.10] And if you could kind of describe what that is.
[1929.28 → 1937.18] And just from other organizations, including the one that I work for, most of them have kind of a way of
[1937.18 → 1940.34] approaching that, and they have a lot of commonalities across it.
[1940.50 → 1943.20] And you don't need to give – obviously, we're not asking for anything proprietary.
[1943.20 → 1943.64] Right.
[1943.64 → 1943.78] Right.
[1943.90 → 1949.16] I'm happy to go over the architecture, typical architecture of an autonomous driving system.
[1949.18 → 1949.40] Okay.
[1949.60 → 1950.26] That'd be great.
[1950.48 → 1950.62] Yeah.
[1950.64 → 1951.36] That'd be fantastic.
[1951.52 → 1951.60] Yeah.
[1951.60 → 1956.12] And this would be the onboard version because there are also a lot of key off-board systems
[1956.12 → 1962.28] that come into play which are crucial to being able to make progress on the problem.
[1963.32 → 1966.14] And so the onboard stack, it all starts probably with maps.
[1966.70 → 1971.86] It's really helpful to have a map of the environment already available to you.
[1972.66 → 1977.76] This can be obtained, of course, by surveying the environment ahead of time, collecting sensor
[1977.76 → 1978.56] data from it.
[1978.56 → 1984.52] And from the sensor data, you can build a representation of the environment and store it.
[1985.28 → 1986.24] Why is this important?
[1986.44 → 1989.18] Some people can say, oh, wouldn't it be nice to not have a map?
[1989.66 → 1994.10] I think map is a really important safety feature and, in a sense, an additional sensor.
[1994.96 → 1997.76] It gives you a lot of prior information about the environment.
[1997.96 → 2002.40] Often, big parts of the environment end up being occluded, especially in crowded scenes.
[2002.40 → 2010.02] And it really helps you anticipate and understand better the cues in this data-limited regime
[2010.02 → 2013.10] where you cannot easily see everything with your sensors, for example.
[2013.68 → 2016.90] So that's almost like a fourth sensor is your map.
[2017.30 → 2021.68] Could you say it enhances kind of the situational understanding of the environment as a kind of
[2021.68 → 2025.92] as a constraint of, you know, your sensor, regardless of what the other sensors are saying,
[2025.98 → 2029.04] the map says if there is a road or not a road there.
[2029.04 → 2033.20] Yeah, and here's roughly these lanes, and they used to go at least to these lanes before.
[2033.72 → 2036.04] And afterwards, there will be something in 50 meters.
[2036.16 → 2039.02] You should know that there is some other road merging in.
[2039.24 → 2040.22] And you know all this.
[2040.30 → 2042.18] You don't have to just find it along the way.
[2042.24 → 2043.16] You know what to expect.
[2043.76 → 2048.64] Now, when you use maps, one core property is you can just assume the map is true.
[2049.66 → 2053.80] Also, ideally, it will not make the map so high fidelity and density.
[2054.36 → 2056.14] Just model every pixel in the map.
[2056.22 → 2057.26] That's probably unnecessary.
[2057.26 → 2060.64] You just want the high-level semantic gist of the scene, right?
[2060.70 → 2063.82] And then you transfer this understanding into your models as an aid.
[2064.02 → 2067.62] But it's knowledge that you need to be able to change as you observe the world.
[2067.72 → 2071.76] For example, maybe you believe there's a traffic light over here, and then someone moved it,
[2072.08 → 2072.38] right?
[2072.84 → 2077.80] Your system needs to be able to now understand that whatever the traffic light that in the
[2077.80 → 2080.04] map was telling you is no longer relevant.
[2080.04 → 2086.18] And you need to detect any new one and figure out what it means for you and execute, well,
[2086.26 → 2089.92] the allowed behaviours in the scene relative to this new object.
[2090.40 → 2094.62] And so that's a key requirement to be able to maintain the map is you need to track which
[2094.62 → 2099.26] parts of it are correct and use those to age your models, right?
[2099.26 → 2101.68] But that comes from part one of the system.
[2102.18 → 2107.84] And again, some people make a big deal out of, oh, you may not need this high fidelity map.
[2107.90 → 2109.62] You need some map, right?
[2109.70 → 2112.68] And it's a bit open question, and everyone has a different answer.
[2113.02 → 2118.06] But some information about the environment that you can just collect, it's a great safety feature.
[2118.12 → 2118.88] So it starts there.
[2119.28 → 2122.90] Now, to use the map, you need now a system that's called localization system.
[2122.90 → 2128.42] This is a system, as you drive through this environment, you need to know how you're positioned
[2128.42 → 2129.62] relative to your map.
[2130.42 → 2135.48] Once you know that, then all this knowledge stored in the map has direct transfer to your
[2135.48 → 2139.62] own representations from your sensors, and now it can really enrich them.
[2139.72 → 2141.04] So that's the prerequisite.
[2141.86 → 2143.20] Then you have perception.
[2144.00 → 2149.16] Perception, you have the map, the localized map, you have the sensor data, and you are
[2149.16 → 2150.82] reconstructing a model of the world.
[2150.82 → 2154.78] And this model of the world is actually very interesting.
[2155.22 → 2156.58] It can be quite rich.
[2157.26 → 2162.86] So you can understand and detect and track many different kinds of objects in the environment,
[2163.00 → 2164.78] all the vehicles, pedestrians, cyclists.
[2164.90 → 2172.58] You can detect signs and traffic lights and lanes on the road and borders of the road, the
[2172.58 → 2175.28] drivable surface, and so on.
[2175.28 → 2180.76] So flares, police cars, ambulances, gestures of people.
[2181.16 → 2183.08] It goes quite rich, right?
[2183.16 → 2188.86] And this kind of predicates having several models running in perception to obtain this
[2188.86 → 2190.80] data from the three available sensors.
[2190.80 → 2200.36] And so once you have this representation of the world that you agree on, right, that now is
[2200.36 → 2206.78] fed to your behaviour prediction model for the objects that are ultimately behaving in the
[2206.78 → 2208.36] environment on their own volition.
[2208.36 → 2212.76] So in addition to things like pedestrians and vehicles, which are a lot of the things that make self-driving
[2212.76 → 2220.30] hard, is the ability to anticipate uncertain, potentially, behaviours of the people around you, right?
[2220.32 → 2221.68] Whether they're in vehicles or walking.
[2221.88 → 2223.78] It's not a deterministic behaviour.
[2223.78 → 2225.88] It's not something you can project for sure.
[2226.26 → 2234.26] You need to be prepared for a diverse set of potential outcomes and drive an optimal policy relative to that.
[2234.26 → 2241.58] So you have a behaviour prediction system that gives you a representation of these beliefs about what other agents are going to do.
[2242.60 → 2250.04] And now with input from perception, which also can include things like you understanding which parts of the world are occluded and not occluded.
[2250.44 → 2252.86] So it's not just about detecting and tracking an object.
[2253.04 → 2257.48] You need to understand which things you don't even know, because that's important knowledge in itself.
[2257.48 → 2269.34] And the predictions and all the tracked objects and all the obstacles you've detected, this now goes into the planner, which needs to plan a good, safe trajectory that gets you to the goal comfortably, right?
[2269.36 → 2272.34] That's ultimately roughly the gist of what is required.
[2272.34 → 2278.08] So you need to trade off all of these requirements in an optimal way to get a good behaviour, right?
[2278.12 → 2282.16] And then the planner executes or makes the decisions of how to drive.
[2282.16 → 2292.98] Often those decisions need to be translated into acceleration and steering wheel motions, which a controller can do.
[2293.88 → 2301.04] And this is the whole system working in unison with all these modules, maintaining the mapping from observe the environment to act in the environment.
[2301.64 → 2305.40] So that is roughly my overview of the onboard system as a set of modules.
[2312.16 → 2334.28] That was a fantastic explanation that you just gave us there.
[2334.44 → 2336.68] And I just want to kind of follow up a little bit on that.
[2336.68 → 2351.84] You know, you covered so many of the components that go into the process of the vehicle figuring out, you know, what's happening and where it's going down the road from behavioural prediction model to the planner, the perception from the sensors, your world model.
[2352.06 → 2362.18] As you put all of that together, and you are having a vehicle that is moving down the street, that's a fairly complicated situation to try to resolve.
[2362.56 → 2364.70] It's a wonderful integration problem.
[2364.70 → 2374.16] I mean, self-driving cars is a robot, and you need to integrate all of these systems, which also, of course, includes all the hardware and sensors and so on into one coherent whole.
[2374.26 → 2374.94] It's fascinating.
[2375.64 → 2380.84] That's really where I was wanting to go with it was, you know, it is a very complicated situation.
[2381.48 → 2389.40] And for any one of the various things that you covered, you have to have a strategy that, you know, that the planner is going to come up with and stuff.
[2389.40 → 2408.66] If you're starting with, you know, maybe the mapping or the world model that, you know, from that, and you have the sensors to give you the real time data, how does the behavioural prediction model and the planner, how do they kind of take those things in a generalized sense and be able to deviate from what otherwise?
[2408.66 → 2412.56] You know, you if you're is you're starting with, well, I have a map of roads and therefore.
[2412.78 → 2419.38] But as you said, they may have moved the traffic light or there may be a pedestrian or a dog that's about to dart out into the road.
[2419.66 → 2421.38] How does that integrate in?
[2421.50 → 2429.16] Is there do you kind of have a path that you're typically taking and then those are all exception cases or is it more integrated than that?
[2429.16 → 2431.30] I think it's more integrated than that.
[2431.42 → 2440.78] Generally, there is high level principles or understanding of how to build this thing and how it's supposed to fit together.
[2441.26 → 2445.44] So operationally, we'll talk operationally and then technologically operationally.
[2445.44 → 2461.48] In these areas, there's a lot of these vertical cross-functional work groups that ultimately tailor a set of capabilities and algorithmic system designs to handle the specific types of behaviours in the environment.
[2462.20 → 2471.96] I think also ultimately there is a lot of interesting high level choices you do that are a bit more general, which is what is a good representation to power behaviour prediction?
[2471.96 → 2476.48] And I think this may different companies may have different answers.
[2476.80 → 2486.74] And a lot of this can be tried by trying deep learning models on different types of inputs and seeing what gains you get.
[2486.94 → 2491.84] This is one interesting way to understand what kind of attributes and representation is so important.
[2491.96 → 2497.26] I will give you some examples from our recent work that we published this year's CVPR.
[2497.26 → 2513.10] Traditionally, and this is some of the early Waymo work that we published maybe early last year, 2019, early 2019, we had a paper called Chauffeur Net, which was based on end-to-end or mid-to-mid as we call it, learning to drive.
[2513.54 → 2517.20] That was based on the presentation of the world as an image.
[2517.20 → 2520.24] So your map, you rasterize it to an image.
[2521.06 → 2532.44] Then you can use your favourite computer vision models to process the image with the convolutional net and then make whatever predictions you want on top, maybe some kind of heat maps of where it's going to be or trajectories or so on.
[2533.66 → 2538.46] That is one type of representation, but it also has a significant set of weaknesses.
[2539.22 → 2540.98] Typically, that's a dense representation.
[2541.22 → 2543.52] You're quantizing potentially continuous signal.
[2543.52 → 2550.22] You lose structure that you had because you just rasterized something and the structure is maybe getting lost.
[2550.98 → 2556.56] And conventional neural nets also are good for certain types of processing, but not others.
[2556.66 → 2560.32] You have these local kernels, maybe a 3x3 or 5x5 or so on.
[2560.66 → 2562.12] That's a very local thing.
[2562.22 → 2566.96] And often you need to reason two agents maybe 100 meters from here will merge.
[2566.96 → 2576.42] That's not so obvious to model out well, at least in a more precise way with the deep net, with small kernels.
[2576.84 → 2580.98] And so that leads to the question of, well, maybe there's other representations possible.
[2581.22 → 2585.16] Also, there's a question of, and of course, that's clearly not the full answer.
[2585.66 → 2587.98] Do you do prediction just based on bounding boxes?
[2587.98 → 2594.78] So if you treat every person and every vehicle as a box and all you do is observe how the boxes move,
[2595.02 → 2596.98] can you do accurate behaviour prediction?
[2597.98 → 2601.80] Well, you can be pretty good, but probably you can do even better.
[2601.94 → 2609.42] Humans have a lot of different cues, gestures, gaze, appearance, behaviour of the body, body language, right?
[2609.82 → 2610.52] And so on.
[2610.56 → 2616.42] That also matters, especially in the more complex environments in the dense urban downtowns.
[2616.42 → 2619.08] So there is a bit of this interesting open question.
[2619.22 → 2620.86] There are a lot of different things you can do.
[2621.28 → 2625.84] One of the things we found in a paper called Vector Net that we published in CVPR this year
[2625.84 → 2631.34] was that if you model all the map information such as polylines
[2631.34 → 2638.38] and you model the agent behaviour, also the past history of the agent is also a polyline of sorts.
[2638.94 → 2643.94] And now you have a model that processes all of these, computes features from these polylines,
[2643.94 → 2651.04] puts a graphical neural network or transformer in this specific case on top to reason about all their relationships
[2651.04 → 2656.78] and produces predictions, that works better and often more efficiently than rendering everything in an image.
[2657.24 → 2663.26] So it's a little bit of how your models are in behaviour prediction and their capabilities depend on this interface.
[2663.58 → 2665.36] And there are a lot of things that can be tried.
[2666.18 → 2670.12] And potentially just rendering things as an image and putting a neural net is not it.
[2670.12 → 2673.44] But it's also not just a bunch of bounding boxes moving around.
[2673.58 → 2681.22] The world is rich, and you need a lot of these attributes, or potentially you can go even from the raw pixels in an end-to-end fashion, of course,
[2681.30 → 2683.14] but then you run into different challenges.
[2683.50 → 2686.94] So this is one of the exciting areas of engineering design, right?
[2686.98 → 2688.44] And each company makes a decision.
[2688.82 → 2689.70] What is our API?
[2689.90 → 2690.74] What do we put there?
[2690.80 → 2694.88] What is the predictive features that we're going to be reconstructing with these models?
[2694.88 → 2699.36] Yeah, it's interesting that you're talking about kind of how things are related.
[2699.62 → 2702.32] I also saw, so I watched your talk at CVPR.
[2702.54 → 2703.56] It was great.
[2703.68 → 2710.36] I also saw you were doing other things, tracking, predicting trajectories with these graph neural networks.
[2711.02 → 2714.30] And it kind of strikes me as a bit of a trend I saw.
[2714.52 → 2717.98] I think I mentioned this on one of our last episodes,
[2717.98 → 2725.76] but I saw Sasha Rush was giving some statistics about like the number of keywords he saw being mentioned at CLR.
[2726.42 → 2729.22] And graph neural networks was way high up on there.
[2729.42 → 2732.80] It is definitely a trend in robotics now.
[2733.24 → 2734.34] And for good reason, I think.
[2734.38 → 2736.72] I think ultimately you want models that generalize.
[2737.46 → 2737.64] Yeah.
[2737.64 → 2749.28] And just the first principle of computer vision networks from some sensor grid to controls is not a very generalized model for such a complex space.
[2749.92 → 2753.02] And so I need to introduce structure in this model judiciously.
[2753.10 → 2766.00] And a lot of the structure ultimately about which we can even have models and reasoning and humans can understand it better is things about objects and relationships and interactions and trajectories.
[2766.00 → 2770.54] And these are the things that things like transformers can model well.
[2770.64 → 2777.90] They can model all the inter-object interactions directly as opposed to using an image medium as a proxy.
[2778.44 → 2778.58] Right.
[2779.14 → 2780.22] And that's powerful.
[2780.46 → 2783.16] And I think that's not to say you cannot have the...
[2783.16 → 2784.86] So it's not like you can have it.
[2784.98 → 2786.26] You can have it both ways.
[2786.30 → 2786.64] You could.
[2786.76 → 2786.92] Right.
[2786.96 → 2792.70] You can have some of the basic processing go in a general model and then still have all this structure tacked on.
[2792.70 → 2806.64] And if this is a good generalizable property, it's typically having more outputs in the model is nowadays likely a good idea that allows you to self-supervise them, that adds additional structure.
[2806.86 → 2811.58] It constrains you better to generalize to cases where you don't have as much data.
[2812.14 → 2813.46] So these are good trends, I think.
[2813.56 → 2813.74] Right.
[2813.78 → 2817.18] And I think GNNs are popular for a reason.
[2817.30 → 2819.78] They're quite flexible in what they can do.
[2819.78 → 2820.18] Right.
[2820.22 → 2824.58] And transformers is one of the most popular versions currently of graph neural nets.
[2824.78 → 2824.90] Yeah.
[2825.00 → 2837.78] One of the other things I noticed in that research you were showing was the temporal piece of this that, you know, we've talked about perception and objects and relationships, but there's also, you know, trajectories.
[2838.56 → 2843.92] And as you're processing this data, it's all coming at you as a time series, I assume.
[2844.26 → 2844.56] Correct.
[2844.56 → 2863.04] Could you explain this sort of element of the I think you called them temporal anchor proposals and like, how does this temporal and like projecting back in the past and projecting forward trajectories, how does that fit into the flow of controlling the car?
[2863.04 → 2871.18] So I'm not sure exactly which aspect of the work you're talking about, because I showed several that might be interpreted in this way.
[2871.66 → 2874.34] Yeah, it was very, you're doing a lot.
[2874.50 → 2878.36] So it was hard to, it was hard to narrow down questions here.
[2878.72 → 2888.00] But yeah, I think the one I was thinking, you had a little guy walking and I think you had projected his historical trajectory or something like that.
[2888.00 → 2889.60] So that's your evidence, right?
[2889.74 → 2895.90] You have a scene, which is a static context, and you have the behaviour of the agent so far.
[2896.48 → 2901.60] And you want to produce a distribution over the future behaviours of this agent, right?
[2902.38 → 2908.40] And one of the popular ways to represent that is what I call a mixture of trajectory Gauss ins.
[2908.40 → 2914.94] We wrote a paper on this last summer in 2019, a paper called Multipath, which was one instantiation of it.
[2915.10 → 2919.12] At its core, you're going to say, hey, each agent can have some intents.
[2919.30 → 2923.36] It's a bit hard to say how many there should be, but let's assume we have some intents.
[2923.46 → 2927.06] And for each intent, they're roughly to do a specific behaviour, a trajectory.
[2927.74 → 2931.88] And maybe you have some uncertainty about how exactly this trajectory will play out.
[2931.88 → 2938.04] It's a simplification, but a way to get very accurate behaviours for fairly long time horizons.
[2938.40 → 2943.62] Now, the complexity there is that let's say an agent can have maybe some number of intents, let's say a dozen.
[2944.04 → 2946.74] And for each, you need a trajectory and some uncertainties.
[2946.86 → 2948.64] And maybe these intents change over time.
[2948.76 → 2955.24] So if you're somewhere almost stopped and about to start driving in the parking lot, there's some set of intents you can have.
[2955.28 → 2958.52] And then you come to some intersection with some constraints, and you can have another.
[2959.36 → 2960.92] And then yet, maybe you have another.
[2960.92 → 2962.24] Yeah, and different numbers.
[2962.46 → 2962.58] Right?
[2962.70 → 2962.88] Yeah.
[2962.92 → 2965.14] How do you know which one to apply when, right?
[2965.52 → 2966.86] And where do you get this knowledge?
[2966.86 → 2973.02] Now, maybe you start hard coding based on the road graph, but that maybe makes you too dependent on the road graph.
[2973.12 → 2974.58] Well, the road graph has a mistake.
[2975.00 → 2975.24] Right?
[2975.68 → 2984.22] So we ended up with a concept at the time that was called static anchors, which says, hey, I'm going to enumerate.
[2984.48 → 2987.24] Just look at the data historically all vehicles have ever driven.
[2988.12 → 2990.34] And you can see all the potential things they could do.
[2990.34 → 2992.90] So let's just discretize this into bins.
[2993.06 → 2995.52] And maybe there are 128 bins now or more.
[2995.60 → 3000.08] But at least, you know, for each type of behaviour, now you can classify which one you're doing.
[3000.18 → 3003.06] And then, of course, you adjust the specific trajectory for that behaviour.
[3003.16 → 3005.24] And it's a very simple, very straightforward model.
[3005.68 → 3007.58] And it turns out very easy to learn.
[3008.06 → 3011.52] And so it's probably the simplest behaviour prediction model for multiple trajectories.
[3011.52 → 3014.84] And when we did it, we just got inspired by object detection literature.
[3015.04 → 3016.58] I used to do object detection before.
[3016.70 → 3020.68] We had a paper called SSD, which was a fast single shot detector.
[3020.68 → 3022.20] That was way back in 2014.
[3022.96 → 3029.96] And so it's a bit similar to this where you're saying, hey, I'm just going to enumerate all the things I could roughly do.
[3030.06 → 3033.08] There might be a few, quite a few, but at least it's fixed set.
[3033.42 → 3036.64] I now can train which ones get activated when and adjust them.
[3036.64 → 3038.88] And that works really well.
[3039.86 → 3043.46] So that, of course, is not the only way you can do this.
[3043.84 → 3045.16] But it's one of the simplest.
[3045.34 → 3048.24] And it reduces behaviour prediction much closer to object detection.
[3048.38 → 3050.28] And it reduces it to a supervised problem.
[3050.98 → 3052.26] It's very friendly.
[3053.12 → 3055.10] I mean, that's what machine learning does great, right?
[3055.82 → 3057.18] So it's great to use it.
[3057.46 → 3062.78] It's considerably friendly also to production systems as opposed to a sample system that just does sampling.
[3062.78 → 3067.06] A lot of academia work is on variational autoencoders or CAES and so on.
[3067.62 → 3069.94] And those need to sample your set of trajectories, right?
[3070.00 → 3071.58] And that's how they generate a distribution.
[3072.12 → 3074.50] Sampling is expensive, and it's not that deterministic.
[3075.08 → 3077.74] And it's not that easy to get probabilities for it.
[3078.54 → 3084.16] And so while it's very nice and powerful paradigm, maybe this anchor thing is simpler.
[3084.36 → 3089.32] Of course, it doesn't actually stop with anchors because now there is powerful anchorless models.
[3089.32 → 3096.68] And we have some exciting work that we're hoping to put out on archive that does some interesting things in this space as well soon.
[3097.12 → 3098.46] So maybe you guys should stay tuned.
[3098.62 → 3100.92] But there are a lot of interesting things you can do with this.
[3101.12 → 3102.46] We'll be on the edge of our seat.
[3102.82 → 3103.84] It's a little tease there.
[3103.94 → 3107.30] But one last thing I would say is why do this thing, the anchors?
[3107.72 → 3111.22] Typically in object detection also in early time when we were working on it,
[3111.22 → 3115.66] The problem with and the reason why we introduced the concept of anchors ourselves,
[3115.76 → 3119.86] we did it at the time probably in parallel with Faster RCNN, which also did it.
[3120.24 → 3121.30] It's a reasonable concept.
[3121.42 → 3122.44] Many people invent it.
[3122.76 → 3123.48] It's logical.
[3123.86 → 3124.78] I think it's the following.
[3124.96 → 3128.70] Neural nets, if you train with the L2 loss, right?
[3129.22 → 3134.10] And you don't have many different modes at output, it starts doing mode averaging.
[3134.64 → 3135.40] So it's hedging.
[3135.40 → 3141.22] If there are two different eventualities that potentially overlap, and you have a single output,
[3141.34 → 3142.68] it will average between the two.
[3142.80 → 3144.78] That's the best thing you can do with L2 norm.
[3146.00 → 3153.38] And so there is this traditional trick, and by now it's perfectly standard to do these continuous regression problems,
[3153.52 → 3155.18] is to do discrete continuous.
[3155.44 → 3160.56] So you discretize in slightly coarse bins, and then within each bin you regress.
[3160.68 → 3163.32] And that's dramatically better than just doing directly regression.
[3163.32 → 3164.64] That does not work so well.
[3165.40 → 3165.80] Right?
[3166.08 → 3169.88] And now, of course, it's 2020, and people have even more things that they can do.
[3169.94 → 3173.50] But this is probably one of the simple things you can do if you do regression,
[3173.70 → 3175.42] is to discretize parts of your output.
[3175.50 → 3176.42] And usually it does better.
[3176.86 → 3183.86] So I guess to finish up, if you could tell us what kinds of things are you most excited about
[3183.86 → 3188.12] as you're looking here at the future of this industry, at the future of self-driving cars,
[3188.12 → 3192.58] with your special insight in there, what's getting you excited?
[3192.58 → 3194.80] What keeps you up feeling like a kid?
[3195.40 → 3196.58] About what's going to happen next.
[3196.58 → 3201.94] First, I'm excited by the product and the possibility of helping society with it.
[3202.08 → 3202.26] Right?
[3202.36 → 3205.18] And I think that goes in multiple different directions.
[3206.14 → 3209.90] And you probably have heard them before, but that does not make it any less valid.
[3210.82 → 3212.36] There is safety aspect.
[3212.70 → 3217.68] Right now, in the US, I think more than a million people die a year.
[3217.68 → 3221.58] I had heard a kind of comparison to this.
[3221.68 → 3228.64] It's as if a Boeing plane with 150 people crashes every hour all year.
[3229.54 → 3230.02] Right?
[3230.10 → 3231.24] This is the amount of...
[3231.24 → 3233.24] It's in the world, though, not just in the United States.
[3233.32 → 3238.12] In the world, about 1.3 million people die from automotive accidents,
[3238.12 → 3239.88] and 50 million people get injured.
[3239.88 → 3244.62] And a lot of those are due to human error.
[3245.12 → 3246.54] I think over 90%.
[3246.54 → 3254.62] And so with autonomous driving systems, the hope is to be able to reduce the consequences of...
[3254.62 → 3256.18] And the possibility of human errors.
[3256.44 → 3258.68] As you're addressing this, and I don't want to cut you off.
[3258.74 → 3259.44] I want you to continue.
[3259.60 → 3263.46] But as you're addressing this, can you envision a world at some point in the future
[3263.46 → 3269.26] where humans are not driving at all anymore, and it is 100% everything we do is autonomous?
[3269.88 → 3271.78] I think it may take a while to get there.
[3272.26 → 3277.22] People are attached to their cars, and I think generally penetration will happen in a thoughtful,
[3277.80 → 3279.00] steady way over time.
[3279.62 → 3286.58] There is the hope and the advantages of autonomous driving that people will hopefully get attracted to.
[3286.58 → 3288.52] We've had very enthusiastic reception.
[3289.08 → 3293.44] Originally, you think, okay, we're going to roll out this self-driving product in Phoenix,
[3293.46 → 3294.84] and how is it going to go?
[3295.40 → 3300.48] A lot of people are really excited users, and especially for the fully driverless rides,
[3301.38 → 3305.58] which there's no one in the car, and it's driving you throughout Phoenix.
[3306.34 → 3308.54] We got a lot of five stars.
[3308.68 → 3311.26] People get super excited once they experience it.
[3311.30 → 3313.04] It's a big thrill, and they're very positive.
[3313.04 → 3316.38] So I think it may take some time for people to get exposed,
[3316.58 → 3320.70] and we work a lot of outreach and working with key groups and representations
[3320.70 → 3326.06] to get people to be more informed and hopefully give people more chances to try this.
[3326.54 → 3330.74] But I think it still will take some time, but I'm very optimistic about it.
[3331.32 → 3337.28] Some advantages of self-driving cars, in addition to safety, is economics as well.
[3337.36 → 3342.10] I think it can make it easier for a lot of people that currently cannot drive.
[3342.10 → 3349.10] There's a lot of disabled people or people otherwise limited to what they can do to more affordably do so.
[3349.82 → 3354.42] I think it often potentially can change how cities are designed.
[3355.26 → 3357.34] There might be fewer parking lots.
[3357.54 → 3359.50] There might be more green spaces.
[3360.44 → 3361.94] There might be less congestion.
[3363.12 → 3364.18] That's another aspect.
[3364.18 → 3367.70] I think fourth, I'm personally excited about it.
[3367.92 → 3372.88] Self-driving cars go really well with electric cars, whether it needs to be hybrid or electric.
[3373.50 → 3382.62] And I think larger adoption of self-driving technology will also contribute to larger adoption of electric vehicles over time.
[3382.70 → 3383.72] That's my personal opinion.
[3384.32 → 3390.58] I think that it's a natural progression that is likely to happen as well.
[3390.58 → 3394.38] And so it has all these beneficial consequences.
[3394.62 → 3400.76] There is an interesting question about with COVID, what have we learned and is it changing transportation?
[3401.44 → 3406.90] At least so far with the virus, it's problematic to have many people in a small space.
[3407.56 → 3412.98] And autonomous driving has the chance to remove the driver and have you be in a vehicle by yourself.
[3413.80 → 3419.24] And I hope this COVID problem, I mean, it's a pandemic, it's terrible and soon.
[3419.24 → 3423.46] But ultimately, I'm not sure what the patterns and preferences of people would be.
[3424.16 → 3428.04] But autonomous driving can help there potentially as well in some shape.
[3428.30 → 3430.30] And I think it will start little by little.
[3430.42 → 3435.48] Maybe people will not get their second car and just use autonomous driving because it's convenient.
[3435.72 → 3439.84] We see this already in our pilot service Waymo 1 in Phoenix.
[3440.68 → 3443.14] There is a lot of, this is, for example, a popular way.
[3443.14 → 3447.60] It's much easier to just get the Waymo, especially if you need a children's child seat.
[3447.82 → 3450.58] It's already installed in the back and so on.
[3450.78 → 3452.02] I think it's only the beginning.
[3452.38 → 3456.72] And ultimately, the possibilities are great, but it will not happen overnight.
[3457.04 → 3457.14] Yeah.
[3457.52 → 3457.74] Yeah.
[3458.10 → 3461.76] Well, thank you so much for diving into all of these topics with us.
[3461.98 → 3465.14] I know that there's so much to discuss here.
[3465.22 → 3468.26] I definitely recommend people check out your CVPR talk.
[3468.26 → 3473.70] We'll make sure that the link to that is in our show notes so that you can explore more of the great research topics.
[3474.16 → 3481.62] I hope the people that listen to your podcast are somewhat technical because that talk was aimed at a research conference.
[3482.16 → 3482.56] Yeah.
[3483.16 → 3485.12] So hopefully it's still interesting, right?
[3485.20 → 3487.82] It starts general, but then it goes into a bunch of models.
[3488.06 → 3492.36] Well, I think it was, yeah, that's what I enjoyed about it actually was that it started general.
[3492.36 → 3495.16] And actually, it kind of eases you into it.
[3495.26 → 3503.94] And people can go as far as they want looking at the papers or just hopping off to the Waymo website and the blog and all of those things and reading there.
[3504.06 → 3505.96] We'll make sure and include those links as well.
[3506.46 → 3513.94] But yeah, I know I'm fascinated by so much of what you're doing and really appreciate also your passion and how much you're pouring into this.
[3513.94 → 3515.24] It's really great to see.
[3515.44 → 3517.92] So thank you so much for joining us.
[3518.04 → 3524.52] And I hope someday we're able to meet, we're able to take the same autonomous car somewhere and have a chat.
[3524.74 → 3525.72] That would be wonderful.
[3526.42 → 3530.16] Well, after COVID, hopefully let's go a little bit.
[3530.84 → 3532.82] Fingers crossed that it will be a possibility.
[3533.16 → 3538.10] So it would be good to, well, be able to give you guys a test ride.
[3538.34 → 3539.52] Maybe that would be interesting.
[3539.76 → 3540.58] Oh, absolutely.
[3540.90 → 3541.54] We'll do that.
[3541.74 → 3543.04] We'd definitely be in for that.
[3543.04 → 3543.32] Yeah.
[3543.46 → 3544.76] So thank you so much.
[3545.12 → 3546.74] We really appreciate you being here.
[3546.98 → 3547.34] Thank you.
[3547.48 → 3554.32] And we're hoping to put more of our work out there in this year and going forward.
[3554.84 → 3558.36] A lot of the work you see now comes out of our lab.
[3559.02 → 3563.88] A lot of it was done last year because that's how long usually the publication process takes.
[3564.06 → 3566.46] But we have a lot of other great things in the pipe.
[3566.46 → 3568.86] So I hope to share them with the community soon.
[3569.42 → 3569.80] Cool.
[3569.98 → 3570.84] Thank you so much.
[3571.26 → 3571.86] Thank you.
[3573.04 → 3581.00] Do you have questions, praise, or constructive criticism about the conversation you just heard?
[3581.66 → 3586.30] Comment on this and every episode of Practical AI on changelog.com.
[3586.84 → 3592.46] Just open your show notes, follow to discuss on changelog news link, and let your voice be heard.
[3592.46 → 3597.72] Practical AI is hosted by Daniel Whiten ack and Chris Benson.
[3598.16 → 3599.60] It's produced by Jared Santo.
[3599.92 → 3600.42] That's me.
[3600.68 → 3603.44] And our music is provided by the mysterious Break master Cylinder.
[3604.40 → 3606.52] We're brought to you by some amazing sponsors.
[3606.76 → 3609.24] Special thanks to Vastly, Linde, and Rollbar.
[3609.48 → 3613.64] And a special shout out to those listening on our ad-free changelog++ feed.
[3614.08 → 3615.70] If that's you, you're awesome.
[3615.70 → 3618.16] If that's not you, well, you're awesome too.
[3618.44 → 3621.66] But you can learn all about it at changelog.com slash plus.
[3622.74 → 3623.74] That's all for now.
[3624.02 → 3625.40] We'll talk to you again next week.
[3625.40 → 3655.38] We'll see you again next week.
