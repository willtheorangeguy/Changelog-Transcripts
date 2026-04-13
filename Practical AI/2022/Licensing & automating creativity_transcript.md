[0.00 --> 6.84]  One of the big areas that we're seeing just kind of explode is, I mean, in one sense,
[6.92 --> 13.66]  AI and creativity, but in a sort of broader sense, like an expansion of the things that
[13.66 --> 22.02]  AI is doing in a creative sphere that is paralleling, you know, a lot of what humans
[22.02 --> 22.50]  could do.
[22.58 --> 26.98]  And particularly, I think the most obvious one that we've seen recently is this DALI,
[26.98 --> 34.12]  stable diffusion, all of these models that are sort of text to image models.
[34.34 --> 41.44]  It brings up really interesting questions around the ability of maybe non-artistic people
[41.44 --> 47.84]  like myself, who I'm not a designer, I'm not a painter, but the things that I could do creatively
[47.84 --> 50.64]  with these tools is amazing and fun.
[50.94 --> 55.54]  From my perspective, there's this sort of really fun, positive element about it.
[56.98 --> 72.14]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[72.44 --> 73.46]  and accessible to everyone.
[73.84 --> 75.52]  Subscribe now if you haven't already.
[75.74 --> 78.62]  Head to practicalai.fm for all the ways.
[78.98 --> 83.96]  Special thanks to our partners at Fastly for delivering our shows super fast to wherever
[83.96 --> 84.62]  you listen.
[84.94 --> 86.76]  Check them out at fastly.com.
[86.98 --> 89.18]  And to our friends at fly.io.
[89.54 --> 93.12]  We deploy our app servers close to our users, and you can too.
[93.48 --> 95.38]  Learn more at fly.io.
[101.38 --> 105.94]  Well, welcome to another fully connected episode of Practical AI.
[106.32 --> 111.86]  This is where Chris and I keep you fully connected with everything that's happening in the AI
[111.86 --> 112.36]  community.
[112.56 --> 118.32]  We'll take some time to dissect the latest news in the AI world and dig into some learning
[118.32 --> 121.58]  resources to help you level up your machine learning game.
[122.24 --> 123.16]  I'm Daniel Whitenack.
[123.26 --> 128.76]  I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[128.76 --> 131.68]  Benson, who is a tech strategist with Lockheed Martin.
[132.00 --> 132.64]  How are you doing, Chris?
[132.98 --> 134.36]  I'm very well today, Daniel.
[134.36 --> 140.10]  It's been an interesting week in various types of AI news, and I've noticed some themes that
[140.10 --> 145.28]  we can jump into along the way of some fairly substantial concerns, I'd say.
[145.44 --> 145.66]  Yeah.
[145.76 --> 146.60]  The world evolves.
[146.94 --> 147.40]  Yes.
[147.62 --> 155.88]  Well, I mean, on a slightly less on-topic note, but definitely newsworthy, I don't know if you're
[155.88 --> 160.06]  going to watch Rings of Power today or tomorrow, or you've already watched it.
[160.18 --> 160.70]  Not yet.
[160.90 --> 161.10]  Yeah.
[161.26 --> 164.78]  So neither of us have watched it, so you're not going to spoil anything for me because
[164.78 --> 165.72]  I haven't watched it either.
[166.40 --> 173.00]  But tomorrow, our family, we're going to have a bit of a marathon and watch through Peter
[173.00 --> 174.50]  Jackson's Lord of the Rings.
[174.72 --> 175.14]  Oh, good.
[175.14 --> 177.12]  And then we're going to watch Rings of Power.
[177.12 --> 184.28]  So it's going to be an all-day affair, and I'm sort of basically ignoring anything I'm
[184.28 --> 189.46]  trying to hear, you know, trying to ignore anything I'm hearing about whether Rings of
[189.46 --> 193.26]  Power is good or bad, reserving judgment until I see it.
[193.54 --> 198.78]  But so, yeah, that is, I don't know that we've ever talked about this because it's not directly
[198.78 --> 203.18]  in the AI world, but that I grew up as a fanatical Tolkien fan.
[203.30 --> 203.42]  Right.
[203.42 --> 208.62]  And not only Lord of the Rings and obviously The Silmarillion and all the other stories
[208.62 --> 211.36]  that most people don't ever want to read.
[211.60 --> 212.94]  I've read them all.
[213.02 --> 214.12]  I've read them all multiple times.
[214.20 --> 218.54]  So I'm one of those a little bit slightly nutjob types on that.
[218.74 --> 221.24]  It's my favorite set of stories in the world.
[221.76 --> 223.90]  So yes, here's the conflict.
[224.08 --> 227.90]  My wife and my daughter aren't as enthusiastic as I am.
[228.22 --> 230.84]  So they like it, but not like I do.
[230.84 --> 233.50]  Neither is, yeah, anyone in my life, really.
[233.94 --> 234.26]  Yeah.
[234.40 --> 239.86]  So the big thing about Rings of Power coming out was like, do I just watch them or do we
[239.86 --> 240.50]  do it as a family?
[240.56 --> 243.46]  And my wife's like, yeah, we'd like to watch it together, but they don't have the urgency.
[244.08 --> 249.56]  So now that it was released last night, Daniel, as we are recording this, I am sitting here
[249.56 --> 253.40]  waiting like, when are they going to be ready to do this?
[253.72 --> 256.16]  Part of me wants to selfishly just go watch it.
[256.28 --> 256.90]  But no, no.
[256.94 --> 257.20]  Right.
[257.20 --> 258.78]  I'm going to be a good family man.
[259.02 --> 263.56]  I mean, for someone like you with that sort of background, you're getting this like visual
[263.56 --> 268.22]  sense of things we haven't seen in other movies like the Dwarf Kingdoms and such, which is
[268.22 --> 270.06]  going to be really interesting.
[270.26 --> 272.52]  I mean, I hope it's really awesome, but it's different.
[272.66 --> 273.50]  It's definitely different.
[274.16 --> 274.98]  So there's a lot.
[275.20 --> 276.12]  They've taken license.
[276.38 --> 277.26]  Oh, yeah, sure.
[277.48 --> 277.88]  With the story.
[278.46 --> 280.94]  Which one would probably expect.
[281.20 --> 281.58]  I agree.
[281.68 --> 284.42]  And Peter Jackson, though, he did a great job.
[284.42 --> 287.26]  He took some license with the story, but he pulled it off pretty well, in my view.
[287.64 --> 290.30]  They've taken more license at Amazon with this story.
[290.78 --> 295.60]  So I'm one of those people who has read The Silmarillion many times and I know all the
[295.60 --> 295.98]  detail.
[295.98 --> 301.70]  And I'm going to be trying so hard not to let it just irritate the crap out of me.
[301.78 --> 306.16]  But I'm looking forward to it because of the scope and level of quality that it's supposed
[306.16 --> 306.54]  to have.
[306.54 --> 307.06]  Yes.
[307.20 --> 314.44]  Well, speaking of creativity and license and all of those things, I mean, I think and
[314.44 --> 316.16]  this is one of the topics you brought up to me.
[316.28 --> 323.46]  One of the big areas that we're seeing just kind of explode is I would say, I mean, in
[323.46 --> 325.58]  one sense, AI and creativity.
[325.58 --> 334.06]  But in a sort of broader sense, like an expansion of the things that AI is doing in a creative
[334.06 --> 339.92]  sphere that is paralleling, you know, a lot of what what humans could do.
[340.02 --> 345.12]  And particularly, I think the most obvious one that we've seen recently is this both DALI,
[345.48 --> 352.34]  stable diffusion, all of these models that are sort of text to image models.
[352.34 --> 357.10]  So, yeah, there's this it brings up really interesting questions around.
[357.74 --> 361.98]  Well, I think really fun things, first of all, really like positive and fun things around
[361.98 --> 369.50]  like just like the ability of maybe non artistic people like myself, who I'm not a designer.
[369.50 --> 372.24]  I'm not a painter necessarily.
[372.24 --> 374.76]  I mean, I took art in high school.
[374.76 --> 375.28]  Right.
[375.36 --> 380.92]  But the things that I could do creatively with these tools is amazing and fun.
[380.92 --> 386.18]  And like that's a really from my perspective, there's this sort of really fun, positive
[386.18 --> 387.62]  element about it.
[387.70 --> 388.30]  I don't know.
[388.68 --> 390.48]  Do you see that side of things?
[390.68 --> 390.90]  Yeah.
[391.04 --> 395.62]  And by the way, I'm looking forward to, you know, you know, going and touring the Louvre at
[395.62 --> 401.82]  some point in future years and seeing, you know, a Daniel Whitenax AI original, you know,
[401.92 --> 404.16]  yeah, because, you know, that's going to happen.
[404.16 --> 409.72]  Well, what do you think is the attribution of these works?
[410.00 --> 416.90]  Like how should one attribute one of these AI augmented artworks, I guess?
[417.28 --> 419.38]  So I don't know that I have the answer.
[419.50 --> 424.62]  And I can see both sides as we talk about this, because I as we are talking about some
[424.62 --> 430.22]  of these articles that we've seen, one of them, which was a little maybe on vice.com
[430.22 --> 436.80]  is an AI generated artwork won first place at a state fine arts competition and artists
[436.80 --> 437.74]  are pissed.
[438.24 --> 440.66]  So I think that's going to happen a lot.
[440.66 --> 446.34]  I think the question then becomes, if you want to talk about artwork, you have to be specific.
[446.50 --> 452.00]  I mean, I'm so biased coming from this AI community, but, you know, it's a set of tools,
[452.28 --> 457.50]  you know, just like Adobe Photoshop, you know, was for many years, you know, in the digital
[457.50 --> 457.98]  space.
[458.24 --> 460.68]  And now AI is another set of tools.
[460.68 --> 464.04]  And I personally see it as perfectly legitimate.
[464.22 --> 471.84]  But there may have to be competitions that specify, you know, and by the human hand, you
[471.84 --> 473.98]  know, in a non digital format kind of thing.
[473.98 --> 474.72]  I don't know.
[474.82 --> 475.60]  It's not just coming.
[475.74 --> 476.08]  It's here.
[476.14 --> 478.26]  And it's here in a big way and only more of it.
[478.62 --> 478.72]  Yeah.
[478.82 --> 482.78]  And I think to I mean, we are practical AI here.
[482.88 --> 486.62]  So people are wondering how they can practically do some of these things.
[486.62 --> 488.20]  One of the examples is Dali.
[488.44 --> 495.06]  You can, you know, request access and use Dali, which now includes sort of extra features
[495.06 --> 497.22]  around in painting and other things.
[497.56 --> 502.68]  There's also I think it's funny, Chris, you know, we talked about Dali recently.
[502.68 --> 508.40]  It almost seems like we've moved on from Dali and now stable diffusion is the thing.
[508.48 --> 512.54]  And, you know, you can see how things fast things move in the AI world.
[512.54 --> 517.86]  Now, at the time we're recording, this stable diffusion is is the new new.
[518.62 --> 523.54]  And you can use there's actually from from stability.
[523.92 --> 532.12]  There's a dream studio dot AI, which is a you can sign up and do this sort of also AI
[532.12 --> 535.82]  assisted creativity work within that dream studio app.
[535.82 --> 540.92]  So if you're wanting to get hands on in a practical way with these models, it's not that hard at
[540.92 --> 545.90]  this point, whether you're doing that on a hugging face space or in dream studio or in
[545.90 --> 546.80]  the Dali interface.
[546.90 --> 549.10]  There's multiple on ramps to this.
[549.32 --> 550.24]  Yeah, I agree.
[550.42 --> 551.48]  And it's interesting.
[551.62 --> 554.88]  I mean, I do think that this is going to open up the spaces in a big way.
[555.18 --> 556.26]  Can you talk a little bit?
[556.30 --> 559.96]  Because I know we've talked about Dali quite a lot over recent episodes.
[559.96 --> 564.36]  And so listeners probably are fairly familiar with it if they've been with us for a short
[564.36 --> 564.90]  while, at least.
[565.38 --> 568.44]  Can you talk a little bit about stable diffusion at a high level?
[568.54 --> 570.00]  Like what what what do you know of?
[570.04 --> 570.46]  It's different.
[570.56 --> 571.68]  I know it may not be your specialty.
[572.00 --> 574.86]  Yeah, it isn't really my specialty.
[574.86 --> 582.24]  I think that there are differences with the sort of modeling technique and the and the data
[582.24 --> 583.78]  and the way they did it.
[583.78 --> 591.36]  I think, though, one of the interesting things is with stable diffusion being more, I guess,
[591.46 --> 598.06]  more of an open approach where Dali was sort of released in a very, very guarded way with
[598.06 --> 601.46]  the sort of waitlist type thing that we've seen from open AI.
[602.10 --> 609.70]  I mean, like last last time we talked, I think I used just used public hugging face space to
[609.70 --> 613.22]  generate stable diffusion output on hugging face.
[613.22 --> 614.80]  There's a stream studio thing.
[614.96 --> 622.76]  So I think it is a kind of it's in the same stream as Dali and other diffusion models that
[622.76 --> 623.34]  we've seen.
[623.34 --> 626.84]  So there's we're still in this sort of stream of diffusion models.
[626.84 --> 637.06]  But I think the power of like openness and community is part of what has driven the stable
[637.06 --> 642.86]  diffusion model to just like explode and kind of in some senses, people move on from Dali
[642.86 --> 644.52]  to stable diffusion.
[644.52 --> 653.32]  So that's a that's a really interesting point in terms of of openness and how openness drives
[653.32 --> 656.18]  adoption of things as well, I guess.
[656.32 --> 656.44]  Yeah.
[656.44 --> 661.78]  So to turn a little bit, you know, as we've been talking about kind of the this new intrusion,
[661.78 --> 668.56]  if you will, into into artistic output and the fact that the the folks that have have
[668.56 --> 672.36]  been doing it the traditional way aren't so keen about it at this point.
[672.48 --> 677.78]  It has implications in a much larger way than just whether we like the art and whether we
[677.78 --> 678.92]  care about it being AI driven.
[678.92 --> 681.16]  And it affects people's livelihoods.
[681.16 --> 682.24]  It affects jobs.
[682.24 --> 686.06]  And we this is a recurring theme that we've that we've talked about over time that I don't
[686.06 --> 687.96]  think is a thing going away anytime soon.
[687.96 --> 693.08]  I mean, that's, you know, how these things intrude into livelihood that were that were
[693.08 --> 697.16]  previously very human centric and start affecting jobs.
[697.24 --> 701.16]  So we there was another article that I ran across in the register.
[701.66 --> 702.88]  The article's title is goodbye.
[702.88 --> 708.30]  Why humans call centers could save 80 billion dollars by switching to AI.
[708.66 --> 710.86]  And I don't think that's news to anybody.
[710.96 --> 715.30]  Quite honestly, I think that we've seen automation occurring for quite some time.
[715.40 --> 718.40]  It would be natural to have AI models moving into those situations.
[718.76 --> 725.38]  It calls out the fact that all of these things are driven by economics is AI is ever increasingly
[725.38 --> 730.34]  present in, you know, the automation of previously human jobs.
[730.42 --> 731.78]  It's going to be the economics driving that.
[731.78 --> 735.38]  I don't have anything up in front of me, but I remember in a very different industry,
[735.80 --> 739.56]  there was the thing we talked about briefly about McDonald's automating their the food
[739.56 --> 740.60]  service a while back.
[740.86 --> 741.90]  So we're going to see it everywhere.
[742.30 --> 748.22]  So as we do this, I think one of the challenges in front of us are is recognizing it's hitting
[748.22 --> 749.36]  almost every industry.
[749.44 --> 750.86]  It hits medical doctors.
[751.58 --> 755.62]  You know, one of the earliest things was radiographs, but it's it's there's so many other areas,
[755.72 --> 756.50]  cancer diagnosis.
[756.76 --> 758.10]  We've talked about many of these.
[758.38 --> 761.22]  We've talked about, obviously, airline pilots.
[761.22 --> 763.54]  We've talked about fast food.
[763.72 --> 766.98]  This is really hitting the gamut of industry.
[767.28 --> 768.60]  There's really no safe place.
[768.82 --> 770.08]  I was kind of surprised.
[770.60 --> 774.82]  So as you know, Chris, I'm my wife and I are vegetarians.
[774.82 --> 779.96]  So when we're traveling, we have our sort of quick spots where we know there's something
[779.96 --> 782.66]  that is not meaty.
[782.66 --> 788.48]  And one of those places is White Castle, which has been interesting over time.
[788.58 --> 794.00]  I've noticed they've sort of adopt been early adopters of things like the impossible meats
[794.00 --> 800.02]  sort of plant or non meat alternative meats, which was kind of surprising for me when I
[800.02 --> 800.38]  did that.
[800.48 --> 805.32]  But the last one of the last times I was coming down from Chicago, I was going through the
[805.32 --> 811.14]  drive through and now they have like in the drive through an AI assistant that does some
[811.14 --> 815.74]  of the drive through interactions at certain times of the day.
[815.94 --> 819.16]  I think like not at all times, but at certain times of the day.
[819.78 --> 822.52]  And I was just totally I shouldn't have been shocked.
[822.52 --> 822.86]  Right.
[822.86 --> 829.90]  Because we talk about this every week, but I was sort of surprised at just the yeah,
[830.00 --> 832.36]  I mean, it's it's there and they're using it.
[832.54 --> 836.52]  And this is like in rural Indiana, right?
[836.82 --> 838.92]  Like AI drive through.
[839.12 --> 840.74]  It's been happening for a while.
[840.82 --> 843.46]  It's just gradually trickling through every industry.
[843.68 --> 847.86]  And it's funny that you say that because I had a fact I actually went through a Chick-fil-A.
[848.06 --> 851.30]  Sorry, Chick-fil-A people, because I'm about to say something not nice.
[851.30 --> 856.42]  But I was in the drive through and they had done this where they have the human teenagers
[856.42 --> 859.22]  trying to optimize the drive through to handle the traffic.
[859.22 --> 860.82]  And they're they're walking around.
[861.10 --> 862.66]  It's like parallel processing.
[863.08 --> 863.24]  Yeah.
[863.64 --> 864.00]  Yeah.
[864.02 --> 869.36]  And coming from coming from this that we do, I was sitting in the car going, yeah,
[869.36 --> 871.58]  you're all going to get automated away pretty soon in my head.
[871.66 --> 872.72]  I mean, I wasn't saying that to them.
[872.94 --> 875.10]  That's literally what I was thinking in the drive through.
[875.18 --> 877.74]  I was like, yeah, this isn't going to last as long as you think.
[878.18 --> 880.30]  But we're seeing that and we're seeing it everywhere.
[880.30 --> 886.40]  I mean, software developers, we who develop software are now have some tools that are
[886.40 --> 888.88]  AI driven by GitHub, for instance.
[889.16 --> 890.82]  That is one step toward that.
[890.94 --> 893.04]  So where do we go from here, Daniel?
[893.16 --> 897.52]  Just to ask a really hard, giant global question.
[897.88 --> 899.96]  At some point, people are going to start to notice.
[900.42 --> 903.16]  I don't know that I have the answer.
[903.16 --> 909.02]  I think I think we're still, though, at a point where, yeah, there's certain things that
[909.02 --> 912.62]  fit within the distributions that models know.
[912.62 --> 913.00]  Right.
[913.02 --> 917.36]  Like we talked about sort of apparent coherence in models recently.
[917.36 --> 921.44]  And I think there's things that fit within the distribution of what models know about.
[921.44 --> 924.48]  So there's there's probably two things.
[924.56 --> 930.54]  One is like, what are those areas where we don't have good data sets and models don't know
[930.54 --> 933.52]  the distributions of things to put together?
[933.52 --> 939.78]  And those are still very those will be where we shift sort of human focus, I think.
[939.78 --> 945.38]  But then also there even where we do have data sets and we're automating, you know, call centers
[945.38 --> 952.98]  or something there, it even stresses more the biases and the openness of data and models,
[952.98 --> 958.96]  because those biases are going to hit really hard when they start affecting people's lives.
[969.78 --> 987.82]  So another thing that I noticed this last week was there was a lot of interesting things
[987.82 --> 993.74]  having to do with AI interactions that had to do with government.
[994.44 --> 999.60]  And we're seeing that because, as we have talked about a number of times, the political
[999.60 --> 1006.18]  social, cultural and legal frameworks that we all live within, which are all have a lot
[1006.18 --> 1011.60]  of commonality even across different countries, they still haven't kept up with the technology.
[1012.38 --> 1021.56]  And so we have another big question going forward is, what is the role of AI when it comes to the
[1021.56 --> 1028.04]  different types of feedback loops that are present in between government and its its citizens?
[1028.04 --> 1029.54]  And how does that affect?
[1029.64 --> 1035.44]  And one thing that was sort of humorous, I suppose, especially if it's not happening to you,
[1035.92 --> 1041.18]  was that there were some articles out about in France, they've released a model, not released,
[1041.26 --> 1047.62]  but they're using a model in the French government to identify swimming pools from satellite imagery.
[1047.84 --> 1053.72]  And apparently, I did not know this, apparently if you're in France and have a pool, that pool is taxed.
[1053.72 --> 1059.50]  And so it affects the tax base and it affects how many. And apparently, there were tens of thousands
[1059.50 --> 1062.26]  of undeclared pools in France.
[1062.50 --> 1062.96]  How dare they?
[1063.24 --> 1065.38]  How dare they not declare their pool?
[1065.50 --> 1066.68]  How dare they swim?
[1067.40 --> 1072.90]  So apparently, there were more than a few French citizens that were a little surprised to receive
[1072.90 --> 1078.22]  a tax notification that we're now taxing your pool that they had not previously declared.
[1078.22 --> 1082.42]  And, you know, it's a little funny to me because I don't have a pool and I'm not in France.
[1082.50 --> 1089.26]  I'm in the US. But, you know, it does raise the question of such tools could be used anywhere
[1089.26 --> 1094.60]  by any government and for pretty much anything that they can do with the data set.
[1094.78 --> 1096.00]  So that was one thing.
[1096.06 --> 1096.96]  What do you think of that?
[1097.08 --> 1098.12]  You don't have a pool, do you?
[1098.34 --> 1099.02]  It is interesting.
[1099.18 --> 1103.70]  I think we were just talking about how AI models are affecting people's lives.
[1103.70 --> 1108.30]  But these very practical things about how the model is built show up almost immediately.
[1108.58 --> 1115.42]  So I'm in one of the articles that we can include in our show notes is talking about this pool model
[1115.42 --> 1123.94]  that at first the system confused solar panels for swimming pools with an error rate of 30%.
[1123.94 --> 1129.94]  But DGFIP, I'm assuming that's the government agency or whatever that's doing this,
[1129.94 --> 1133.66]  says that it has since increased the accuracy.
[1133.92 --> 1140.64]  So I think that's one of these cases where can a model, I mean, in a very practical sense,
[1140.66 --> 1147.48]  outside of the implications of it in a government rule sense, a model can do this, no doubt.
[1147.90 --> 1149.92]  But it doesn't do it perfectly, right?
[1150.00 --> 1155.60]  So as a practitioner in the French government, if you are one of those practitioners,
[1155.60 --> 1163.70]  how do you anticipate and deal with those biases in the system and your understanding of your data?
[1163.70 --> 1170.18]  I would say that if you do some work up front to sort of understand behavior,
[1170.56 --> 1174.98]  also do some human evaluation to understand how the model is behaving.
[1175.32 --> 1177.96]  If you analyze the biases in your data set,
[1177.96 --> 1185.86]  and then you release in a way that is taking into account those behaviors of your model,
[1186.12 --> 1188.40]  then people might still be angry,
[1188.40 --> 1192.06]  but they're going to be angry that the government is taxing them for their pool.
[1192.06 --> 1195.16]  They're not necessarily going to be as angry as,
[1195.64 --> 1198.82]  hey, the government is taxing me for my pool that doesn't exist
[1198.82 --> 1204.22]  and only is thought to exist because I have solar panels on my house
[1204.22 --> 1206.24]  and I'm trying to save the environment.
[1206.24 --> 1210.04]  You know, that's probably a different scenario, right?
[1210.14 --> 1215.08]  So I don't know the full details of what they did in terms of that side of things.
[1215.08 --> 1220.80]  But I think as a practitioner, there's a lesson here that as you release these models
[1220.80 --> 1224.34]  and they are influencing people's lives,
[1224.72 --> 1231.38]  the very fact that these won't behave in maybe the way that you always assume that they will,
[1231.48 --> 1233.34]  that has to be factored in up front.
[1233.34 --> 1234.20]  Yeah, I agree with you.
[1234.28 --> 1236.46]  And not only that, but, you know, we tend to,
[1236.76 --> 1241.66]  as we've been tracking, you know, what's happening in the world over the years we've been doing this show,
[1242.10 --> 1247.32]  and we tend to gravitate naturally toward kind of the new stuff coming out and all that.
[1247.32 --> 1251.40]  And what I was struck about this is this is, I don't know the details,
[1251.52 --> 1256.26]  but this looks to me like probably a fairly simple, by today's standards,
[1256.38 --> 1260.80]  old-fashioned convolutional model, I would guess, you know, that was doing this.
[1261.26 --> 1265.82]  I don't think it's necessarily the most cutting-edge deep learning of 2022.
[1266.60 --> 1268.38]  But, and I'm not being critical of those.
[1268.46 --> 1271.80]  If we happen to have listeners, I'm just saying you're being very practical
[1271.80 --> 1275.52]  and that you're using a technology that's been around for a while to do that,
[1275.64 --> 1281.60]  but with, you know, that it's really mundane, but with some fairly substantial effect,
[1281.90 --> 1284.88]  it probably did not cost very much to put this model together,
[1285.38 --> 1289.88]  train it, and get it better compared to many of the things we talk about now.
[1289.88 --> 1298.48]  And yet, they note that a 30-square-meter swimming pool will result in about 200 euros of extra taxes per year.
[1298.64 --> 1301.56]  So every pool is another 200 euros that they can do.
[1301.64 --> 1306.46]  And apparently that that has amassed something along the order of 10 million euros
[1306.46 --> 1308.74]  in new revenue for the French government.
[1309.28 --> 1314.08]  So, you know, enough to easily pay for the time of your data scientists
[1314.08 --> 1316.90]  that are working on that plus quite a bit more.
[1317.06 --> 1319.32]  So I would not be surprised to see a lot more.
[1319.32 --> 1324.54]  Well, and yeah, I wonder too, the, so if you're generating that amount,
[1324.68 --> 1328.58]  I'm thinking of, you know, the model that I'm thinking of, Chris, is,
[1328.72 --> 1331.22]  I don't know if you had this happen in your town,
[1331.32 --> 1337.56]  but the like bird scooters or these electric scooters that like are in cities, right?
[1337.70 --> 1338.32]  Yeah, I've used them.
[1338.44 --> 1340.68]  I mean, I can't comment on their whole strategy,
[1340.68 --> 1343.28]  but my impression of their strategy was,
[1343.48 --> 1346.44]  we're going to show up overnight in your town
[1346.44 --> 1349.46]  and drop hundreds of scooters on the streets, right?
[1349.90 --> 1352.66]  And we'll deal with the legal implications later.
[1352.66 --> 1358.14]  So they're prioritizing adoption above the legal implications of the problems that they might see.
[1358.50 --> 1359.66]  And I think it worked, right?
[1359.78 --> 1363.06]  The companies that did that, they saw the trend coming
[1363.06 --> 1365.44]  and they received a lot of adoption up front
[1365.44 --> 1371.28]  and they likely received a bump in revenue versus the legal implications of what they're doing.
[1371.28 --> 1376.74]  So maybe in a more pessimistic sense, like one could take the perspective,
[1377.20 --> 1381.80]  if you're the French government, well, you say your thing's 70% accurate.
[1382.34 --> 1385.74]  Well, just release it because we'll get enough revenue
[1385.74 --> 1392.32]  that we can take care of any of the legal things that come up from us doing this.
[1392.32 --> 1399.58]  So, I mean, that's maybe a more cynical view of the practicalities of it,
[1399.66 --> 1404.04]  but it's a business, that's a very much a business decision, right?
[1404.28 --> 1404.62]  It is.
[1405.12 --> 1405.74]  It's funny.
[1405.92 --> 1410.00]  I think I'm usually the more cynical of the two of us in terms of what we bring,
[1410.10 --> 1411.62]  but you raised a great point.
[1412.10 --> 1416.74]  Speaking of cynical, did you see the NVIDIA news over this past week?
[1416.74 --> 1423.60]  NVIDIA has been having kind of an ongoing, very public conversation with the US government
[1423.60 --> 1430.58]  about whether or not they can have A100 and H100 chips in China,
[1430.80 --> 1438.50]  which is relevant because there is a little concealed kind of competition in many areas,
[1438.64 --> 1444.32]  economically, militarily, all sorts of implications between China and the West,
[1444.32 --> 1446.84]  with the US probably being kind of the center of that.
[1447.38 --> 1452.84]  And so for national security reasons, there is this ongoing whether or not they can do that.
[1453.06 --> 1453.64]  I won't jump.
[1453.82 --> 1454.92]  What do you think of that?
[1455.42 --> 1457.00]  I'm kind of biased.
[1457.14 --> 1458.46]  I'm already in the defense industry.
[1458.62 --> 1460.50]  So I have some thoughts on that.
[1460.74 --> 1461.96]  But what do you think?
[1462.12 --> 1465.32]  How did that strike you when you found out this was going on?
[1465.76 --> 1468.88]  I mean, I see a variety of perspectives here, I guess.
[1468.88 --> 1474.22]  I know like the supply chain stuff is all messed up around the world.
[1474.44 --> 1480.00]  And so to some degree, people are just looking for what jurisdictions do I need to partner
[1480.00 --> 1484.50]  with business wise to run my business, right?
[1484.84 --> 1490.22]  But there are a lot of other implications there too around security things and that sort of thing.
[1490.22 --> 1499.24]  And I know in listening to the IRL podcast from Mozilla recently talking about sort of balances of power
[1499.24 --> 1506.20]  that are happening with different countries around the world, that's something to consider as well.
[1506.34 --> 1506.68]  I don't know.
[1506.78 --> 1508.12]  What did it trigger in your mind?
[1508.50 --> 1511.44]  Well, I can see, like you, I can see multiple sides to this.
[1511.74 --> 1514.04]  You know, I'm part of this AI community.
[1514.04 --> 1520.34]  And I certainly, you know, that part of me goes, well, that's not a very sensible thing to, you know, to go do that.
[1520.40 --> 1522.74]  And it impacts a lot of livelihoods and all that.
[1523.18 --> 1526.54]  The defense side of me is very aware of that competition.
[1526.88 --> 1532.12]  And so as a strategic move that I don't think could last, if that were to stand,
[1532.20 --> 1534.32]  the Chinese would go and create their own capability.
[1534.32 --> 1536.42]  But that might take time.
[1536.62 --> 1540.02]  So there is a, I can see all sides of the story.
[1540.02 --> 1548.06]  I don't know that this particular move, the way it's being done is the most effective way for the U.S. to secure its interests in the long term.
[1548.44 --> 1558.12]  But I'm not, I wasn't at all surprised that that was, I mean, right now we've talked about, you know, multiple shows that AI is a power lever in the world.
[1558.26 --> 1559.26]  It is for governments.
[1559.26 --> 1560.44]  It is for companies.
[1560.64 --> 1561.92]  It is for individuals.
[1562.34 --> 1568.84]  It is one of the key ways of filling power vacuums now and changing who has the power.
[1568.84 --> 1574.68]  So I think we're going to see all sorts of things all over the place with, you know, across the way.
[1574.76 --> 1578.52]  And you see the same thing in a non-government sense with between corporations.
[1578.94 --> 1582.34]  So, and we saw with artists this week, as we talked about a little while ago.
[1584.46 --> 1587.28]  Yeah, it is one of the things I think is interesting.
[1587.40 --> 1591.10]  I guess this gets to some of the power dynamics.
[1591.10 --> 1607.50]  One of the things that was surprising to me, and I don't know the stats on DALI, but I saw on Twitter that stable diffusion, the new stable diffusion model, they were talking about pricing in terms of the kind of market value of that training.
[1607.50 --> 1617.96]  And I'm seeing that tweet from one of the team is that they use 256 A100s in the cloud for 150K hours.
[1618.64 --> 1623.02]  So the market price stable diffusion costs 600K.
[1623.70 --> 1635.06]  So 600K is by no means a small amount of money for most individual humans, but 600K in a government sense or in a large company sense is nothing, right?
[1635.06 --> 1637.18]  It's not even a rounding error.
[1637.32 --> 1638.22]  Right, exactly.
[1638.54 --> 1656.24]  So I do find it interesting that like this sort of, because of how the infrastructure around this is being commoditized and the tooling around workflows and ML Ops and distributed training and all of these things is getting better.
[1656.24 --> 1678.92]  In some degrees, I see this sort of also a positive shift, I guess, in terms of what's possible maybe for smaller teams that can still like make an impact, release a thing that like takes the industry by storm for a number that's not like something that's restricted to nation states, right?
[1678.92 --> 1691.56]  Like before, I think you have these sort of models that were being released where this is out of reach of anyone but big tech and a nation state, right?
[1691.82 --> 1705.32]  And I think that it's very interesting to me that something like stable diffusion, again, not a small amount of money for like, if I'm myself and I'm an independent researcher, 600K is a lot of money.
[1705.38 --> 1706.92]  You don't have that in your checking account right now?
[1706.92 --> 1707.86]  I wish I did.
[1708.32 --> 1718.28]  But it's reasonable to think like, well, if I really wanted to and maybe I live in the Bay Area, I could sell my house for 600K and train a model, right?
[1718.52 --> 1720.06]  There's like a route.
[1720.20 --> 1727.20]  There's a route to that sort of money for or a small amount of seed funding in terms of a startup or something like that.
[1727.44 --> 1727.54]  Yeah.
[1727.60 --> 1729.56]  If you really are motivated, it's attainable.
[1729.70 --> 1729.86]  Yeah.
[1730.08 --> 1735.58]  And I realize that also I'm kind of revealing my Western biases here.
[1735.58 --> 1741.06]  That sort of money is not, yeah, is not within reach for basically the majority of the world.
[1741.18 --> 1752.52]  But it is encouraging to me that this sort of innovation can happen from small teams and not isn't restricted to sort of nation state actors or big tech.
[1752.52 --> 1755.22]  So that's, yeah, that's encouraging.
[1755.58 --> 1756.40]  It's a great point.
[1756.72 --> 1758.28]  That would be expected over time.
[1758.44 --> 1762.76]  You know, with all technologies, they come out, they're most expensive and they're most inaccessible.
[1763.02 --> 1766.76]  And then eventually, you know, they become cheaper and more accessible.
[1767.20 --> 1768.76]  And we're seeing that happen.
[1768.76 --> 1798.74]  We're seeing that happen.
[1798.76 --> 1826.26]  Well, Chris, I think there's a number of things that I ran across that are in some way related to the things that we've been talking about in one way or another.
[1826.26 --> 1837.34]  One of the interesting articles that I think everyone should take a look at was posted on the Hugging Face blog in August 31st of this year, 2022.
[1838.04 --> 1841.46]  And it's talking about the Open Rail licensing.
[1841.46 --> 1845.24]  So toward open and responsible AI licensing frameworks.
[1845.24 --> 1848.90]  And I think this is really, really relevant for people.
[1849.02 --> 1864.22]  And people should take note because this is the licensing mechanism that was used in the recent releases of the Big Science Bloom model, which is kind of the latest, greatest large language model.
[1864.22 --> 1868.88]  And stable diffusion, which we've been talking about the whole episode.
[1869.10 --> 1879.04]  So you can actually go in this blog post and you can see the links to the Open Rail licenses for Bloom and for stable diffusion.
[1879.04 --> 1900.28]  And what I think they argue here is basically machine learning models or AI models have in one way or another been licensed under licenses that are mostly having have been applied in the past to either software content.
[1900.28 --> 1908.18]  So like software on GitHub, I might license as MIT or Apache 2, something like that.
[1908.28 --> 1910.02]  There's various implications of that.
[1910.48 --> 1917.28]  And if I release content like set up pictures or something, I could do that under Creative Commons, for example.
[1917.50 --> 1924.70]  But this sort of or like a book, if I wanted to make it more permissively licensed under Creative Commons, something like that.
[1924.70 --> 1929.12]  And over time, people are like, well, which of these do I use for models?
[1929.50 --> 1929.70]  Right.
[1929.84 --> 1932.14]  Because a model is sort of like an asset.
[1932.50 --> 1933.20]  It's files.
[1933.46 --> 1938.34]  And in some way, it has relations or similarities to content.
[1938.48 --> 1944.16]  And in other ways, well, it does have a code associated with it, training.
[1944.54 --> 1945.72]  There's a model definition.
[1946.24 --> 1947.12]  There's config.
[1947.34 --> 1950.42]  That's sort of a similarity with code.
[1950.58 --> 1950.74]  Right.
[1950.74 --> 1954.46]  So do one or both of these fit better?
[1954.70 --> 1961.44]  And I think there's additional things with models that maybe don't fit either one of those cases.
[1961.64 --> 1961.76]  Right.
[1961.84 --> 1966.78]  This sort of things around biases, the use of the model, the limitations of the model.
[1967.16 --> 1969.80]  That's really not in common with code.
[1969.88 --> 1970.06]  Right.
[1970.10 --> 1979.98]  Because in code, generally, if it's deterministic, like you have an API endpoint and it does a thing and you can look at the code and understand what it does.
[1979.98 --> 1980.92]  Like it does a thing.
[1981.04 --> 1981.98]  That's all it does.
[1981.98 --> 1988.50]  But with a model, it's sort of like behavioral and bias things that aren't in common.
[1988.50 --> 2002.50]  And I don't know over time if you've run across these sorts of licensing things with models in terms of the fit of sort of data sets, code models and what's licensed where.
[2003.04 --> 2003.34]  I have.
[2003.48 --> 2007.08]  I mean, and I think a lot of people in the community at large have.
[2007.24 --> 2008.92]  It's a natural question to ask.
[2008.92 --> 2014.24]  You and I are fond of saying, you know, you have to have software with your model to get stuff out there.
[2014.36 --> 2018.42]  And software is pretty well established, as you just pointed out, with the open source models.
[2018.42 --> 2019.36]  And you have some choices.
[2019.62 --> 2021.56]  And I think they're fairly well understood today.
[2021.92 --> 2022.58]  Not so.
[2022.68 --> 2025.84]  And even especially with Creative Commons and such as that as well.
[2025.84 --> 2029.92]  Well, this has been a big ambiguous area for a lot of people not understanding.
[2030.08 --> 2032.48]  So I think it's I think it's long overdue.
[2032.62 --> 2038.46]  Glad to see it came from Hugging Face because they always put out fantastic stuff, as we're often fond of talking about.
[2038.98 --> 2044.52]  How would you describe that a little bit of the differences like recognizing bias?
[2044.52 --> 2052.46]  Like how would they approach kind of doing the licensing that accommodates bias for those who haven't had a chance to to look at the article?
[2052.60 --> 2054.70]  What's what's different or what's new there?
[2054.82 --> 2059.38]  They might not have seen in those other categories of open source licensing of some sort.
[2059.38 --> 2059.86]  Yeah.
[2060.10 --> 2071.40]  So I think that there's commonalities with other open licensing structures or mechanisms that maybe we're used to from the from the AI world.
[2071.40 --> 2077.42]  But there's here there's really two kind of pieces of what makes this interesting.
[2077.42 --> 2078.76]  One is is open.
[2078.96 --> 2081.56]  So that's that's like one aspect of it.
[2081.60 --> 2082.32]  Open access.
[2082.58 --> 2084.46]  So that's like an access thing.
[2084.52 --> 2088.32]  But then the other side of it is responsible use.
[2088.32 --> 2091.68]  And that's really kind of where this rail component comes in.
[2091.68 --> 2096.44]  So they build off of this idea of rail or responsible AI licenses.
[2097.46 --> 2100.28]  And these you can go to the also the rail.
[2100.28 --> 2114.52]  There's a rail page which talks about the rail licensing effort, which is been talked about in an ACM paper behavioral use licensing for responsible AI.
[2114.52 --> 2125.62]  But basically, these rail licenses say they include behavioral use clauses, which grant permissions for specific use cases and or restrict certain use cases.
[2125.62 --> 2135.96]  So if you think of a model, again, it has similarities with open data or open code, but it also has this behavioral aspect to it.
[2136.62 --> 2149.18]  And so what the open rail license kind of does is it grants sort of permissive access and redistribution and that sort of thing, as you might expect with an open license.
[2149.18 --> 2154.94]  But then it has these clauses which talk about responsible use.
[2155.26 --> 2157.36]  So for I can give an example here.
[2157.66 --> 2158.00]  That'd be good.
[2158.06 --> 2159.58]  That's the one thing I'm wondering about.
[2159.70 --> 2159.90]  Yeah.
[2160.24 --> 2161.62]  Responsible is kind of an ambiguous.
[2162.14 --> 2162.66]  It is.
[2162.66 --> 2173.30]  Well, and I think that the structure, really, the open rail license is, I think, a structure and the open rail license that you would adopt for your model.
[2174.10 --> 2181.56]  Maybe you could adopt sort of stable diffusions open rail model if you're if you have a similar model.
[2181.76 --> 2184.42]  But other models are going to have other implications.
[2184.42 --> 2184.88]  Right.
[2184.88 --> 2190.74]  So you have some flexibility in the responsible use clauses for the stable diffusion license.
[2190.74 --> 2191.94]  I'm just looking here.
[2192.12 --> 2195.08]  There's sort of attachment A all the way at the bottom.
[2195.24 --> 2197.40]  And it talks about use restrictions.
[2197.64 --> 2204.10]  And this is really this kind of clause that, in my understanding, is is really important here.
[2204.28 --> 2209.42]  And they talk about you agree to not use the model or derivatives of the model.
[2209.86 --> 2211.54]  And then they have a bunch of things.
[2211.54 --> 2217.40]  So one of those things is in any way that violates applicable laws.
[2217.64 --> 2218.30]  That's OK.
[2218.46 --> 2219.50]  So kind of boring.
[2219.60 --> 2222.74]  But if you go down a little bit, it's very interesting ones.
[2222.80 --> 2222.94]  Right.
[2223.02 --> 2230.22]  I you agree to not use the model to defame, disparage or otherwise harass others.
[2230.38 --> 2238.18]  And there's other kind of interesting ones, maybe specific to behaviors that they anticipated use of the model that they wanted to avoid.
[2238.18 --> 2246.48]  So there's one that says you agree to not use the model to provide medical advice and medical results interpretation.
[2247.32 --> 2256.76]  So obviously, you could generate images with stable diffusion or maybe interpret images with such a model that are medical related.
[2257.02 --> 2257.24]  Right.
[2257.34 --> 2259.60]  The medical imagery is a type of imagery.
[2259.60 --> 2260.14]  Right.
[2260.14 --> 2265.36]  So maybe that's a use that they anticipated and had internal discussions about.
[2266.06 --> 2274.08]  And so there's all of these use restrictions or clauses that go into the sort of rail part of the open rail license.
[2274.08 --> 2279.34]  So it's still open in terms of access and distribution type of things.
[2279.34 --> 2285.00]  But then there's these clauses around responsibility that are explicitly included.
[2285.56 --> 2286.12]  It's interesting.
[2286.30 --> 2294.92]  Whereas I know you and I are very focused on kind of AI ethical topics and the responsibilities associated with that.
[2294.92 --> 2303.44]  I find the explicit call out potentially short sighted in terms of unexpected outcomes and consequences.
[2303.82 --> 2313.74]  So I'll have to go through that in depth after the show and just kind of and see what I think about some of those ideas and see if I can come up with any that I think maybe weren't what they were thinking.
[2314.16 --> 2315.90]  Just as a as a fun exercise.
[2316.28 --> 2316.40]  Yeah.
[2316.76 --> 2317.00]  Yeah.
[2317.00 --> 2323.16]  And I think that that's always a it's probably I mean, it's a pre-existing problem with any licenses.
[2323.16 --> 2323.56]  Right.
[2323.58 --> 2325.52]  You can only anticipate so much.
[2325.64 --> 2331.88]  I'm reading some of the frequently asked questions from the Bloom Open Rail license.
[2332.46 --> 2339.84]  And they have one of the one of the explicit frequently asked questions is does the license cover every harmful use case?
[2340.52 --> 2341.76]  And so this is their response.
[2341.84 --> 2343.50]  Maybe that's useful for this discussion.
[2343.50 --> 2353.52]  And they say, no, we recognize that the list of use based restrictions does not conceivably represent everything one could possibly do with our work.
[2353.68 --> 2358.60]  We focus on use cases which could be feasible for the model at this time.
[2359.02 --> 2365.98]  The license is a start by us at exploring how such rail licenses could be used to mitigate harm.
[2366.06 --> 2372.96]  And we hope that these first set of provisions can evolve into more comprehensive provisions over time with community engagement.
[2372.96 --> 2377.32]  So I think they also recognize this explicitly.
[2377.66 --> 2377.78]  Right.
[2377.80 --> 2379.30]  You can never anticipate everything.
[2379.84 --> 2387.08]  I think in some of the discussions we've had on the podcast over time around responsible use of AI and ethics.
[2387.08 --> 2400.54]  I think there's this obligation on the developer's part to reasonably try to anticipate harmful uses of what they're doing with the understanding that you're not going to anticipate anything.
[2400.54 --> 2410.24]  But at least if you made an effort to anticipate some things, then some of those things are anticipated and you're not just sort of chucking your thing out into the world and seeing what happens.
[2410.68 --> 2416.80]  I think for each item, they need to have a little parentheses behind it and says, and the kinds of things that you know I'm referring to.
[2417.02 --> 2419.10]  Et cetera, dot, dot, dot, dot.
[2419.40 --> 2420.82]  Yeah, that sort of thing.
[2421.14 --> 2421.30]  Yeah.
[2421.30 --> 2423.62]  So, I mean, I think this is really.
[2424.00 --> 2424.72]  It's a good start.
[2424.80 --> 2425.58]  It's a good start.
[2425.70 --> 2430.72]  I think it opens a opens dialogue as well, which we're on my team.
[2430.72 --> 2436.10]  We're thinking a lot about these things in terms of data sets and models that we release.
[2436.10 --> 2442.12]  So it's really good to have some sort of open dialogue around these things, I think.
[2442.60 --> 2442.86]  I agree.
[2442.86 --> 2453.54]  I think if this is a start and the conversation can kind of evolve, as did open source licenses on the software side, that was an ongoing, that, you know, there was a many iterations.
[2453.54 --> 2454.34]  Well, there's still not agreement.
[2454.88 --> 2459.32]  And there's still no agreement, but it's much more mature than it was, say, early in my career.
[2459.96 --> 2463.52]  And so hopefully this is the start of the conversation on the model side.
[2463.52 --> 2478.72]  At the end here, I think, I mean, what we've been talking about is hopefully very practical, but we can provide people with a couple of practical learning resources that have come across our desks over the past week.
[2478.72 --> 2495.42]  One that I think fits right into our theme of practical AI and the things that we care about is an upcoming conference that actually started, I think, out of a sort of viral tweet on Twitter called NormConf.
[2495.90 --> 2508.28]  This is a completely, as far as I understand, a completely free and online event, but with an amazing list of speakers, like the really, really great list of sort of AI, machine learning,
[2508.28 --> 2510.30]  data science, data science, tech speakers.
[2510.96 --> 2525.82]  And what they say is, what if there was a conference all about the mundane, behind the scenes, how the sausage is made, middle brow, unsexy, norm core stuff in the data and ML parts of the tech world.
[2525.82 --> 2535.92]  And so that's the goal, to sort of talk about all of those things that aren't probably what is the latest diffusion model.
[2535.92 --> 2546.30]  But I tried to train this diffusion model and I'm having trouble with my infrastructure and data and can't make it work sort of problems.
[2546.52 --> 2552.34]  So you can see even people that we've had on the show here are represented.
[2552.34 --> 2552.90]  Yeah, I was recognizing that.
[2552.90 --> 2556.38]  Yeah, are represented in the list of speakers.
[2556.88 --> 2560.86]  And future guests for our show are surely coming from this list.
[2561.10 --> 2562.82]  I certainly hope future guests.
[2562.98 --> 2567.46]  Yeah, if you're out there and you're speaking at NormConf, let us know.
[2567.74 --> 2568.96]  But just reach out to us.
[2569.16 --> 2574.56]  This, I think, is just a great, focused, practical thing that will be happening.
[2574.56 --> 2576.20]  And I hope it continues to happen.
[2576.40 --> 2583.26]  But I'm certainly excited to listen in and see the set of content that they're putting together.
[2583.76 --> 2584.20]  Me too.
[2584.28 --> 2585.20]  I'm all over this.
[2585.38 --> 2587.04]  So I'm going to register right now.
[2587.78 --> 2588.46]  Yeah, cool.
[2589.06 --> 2598.38]  Well, Chris, I've enjoyed chatting through things as always with you and hope that you have a good Labor Day.
[2598.50 --> 2600.26]  It's about Labor Day here in the US.
[2600.26 --> 2602.40]  So we've got a long, long weekend.
[2602.78 --> 2606.42]  But enjoy the holiday and good to chat as always.
[2606.90 --> 2607.50]  You too, Dan.
[2607.54 --> 2608.22]  You'll have a good weekend.
[2608.50 --> 2608.82]  Take care.
[2617.46 --> 2618.38]  All right.
[2618.52 --> 2620.10]  That is our show for this week.
[2620.28 --> 2622.72]  If you dig it, don't forget to subscribe.
[2623.30 --> 2625.90]  Head to practicalai.fm for all the ways.
[2625.90 --> 2631.84]  And if practical AI has benefited your life, pay it forward by sharing the show with a friend or a colleague.
[2632.18 --> 2635.16]  Word of mouth is the number one way people find shows like ours.
[2635.56 --> 2641.18]  Thanks again to Fastly for fronting our static assets, to Fly.io for backing our dynamic requests,
[2641.72 --> 2644.42]  to Breakmaster Cylinder for the beats, and to you for listening.
[2644.66 --> 2645.32]  We appreciate you.
[2645.58 --> 2646.52]  That's all for now.
[2646.72 --> 2648.22]  We'll talk to you again on the next one.
[2648.22 --> 2678.20]  We'll talk to you again on the next one.
