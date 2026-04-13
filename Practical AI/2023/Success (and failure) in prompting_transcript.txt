[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.04 --> 36.08]  Learn more at fly.io.
[42.66 --> 46.22]  Welcome to another episode of Practical AI.
[46.52 --> 51.48]  This is a fully connected episode where Chris and I are going to keep you fully connected
[51.48 --> 54.12]  with everything that's happening in the AI community.
[54.12 --> 60.10]  We'll take some time to discuss the latest AI news, which is generally crazy these days.
[60.38 --> 65.64]  And we'll dig into some learning resources to help you level up your machine learning game.
[66.08 --> 66.92]  I'm Daniel Whitenack.
[67.02 --> 72.40]  I'm a data scientist with SIL International, and I'm also building a product called Prediction
[72.40 --> 72.76]  Guard.
[73.40 --> 78.54]  And I'm with my co-host, Chris Benson, who's a tech strategist at Lockheed Martin.
[78.72 --> 79.36]  How are you doing, Chris?
[79.66 --> 80.84]  I'm doing very well.
[81.00 --> 82.58]  Crazy times that we live in.
[82.58 --> 84.64]  Crazy times that we live in.
[84.74 --> 92.20]  It's like when we started the show, I thought like, oh, like now's the time to have an AI
[92.20 --> 92.68]  podcast.
[93.28 --> 96.60]  But turns out that wasn't the time to have an AI.
[96.60 --> 100.06]  I mean, it was okay to have an AI podcast then, but now...
[100.06 --> 101.08]  It was fine.
[101.44 --> 101.72]  Yeah.
[101.72 --> 111.10]  But 2023 is apparently the year where everything, depending on your perspective, where everything
[111.10 --> 114.60]  blossoms into a golden age or hits the fan.
[114.86 --> 115.40]  I don't know.
[116.04 --> 117.46]  It's a lot of different perspectives.
[118.00 --> 119.36]  Maybe all of the above.
[119.48 --> 119.60]  Yeah.
[119.66 --> 120.28]  All of the above.
[120.32 --> 120.58]  Yeah.
[120.84 --> 121.96]  All of the above.
[122.28 --> 123.86]  You know, that's a good point.
[123.86 --> 128.12]  I think, what was it, 2018 when we started the show.
[128.22 --> 129.40]  It's now 2023.
[130.36 --> 133.60]  And we had a lot of interesting moments along the way.
[133.88 --> 134.04]  Yeah.
[134.04 --> 138.96]  But, you know, some people might have projected in 2018 that after a few years of doing a
[138.96 --> 143.10]  podcast, you know, you'd look at other things, you'd get bored, just like a lot of activities.
[143.10 --> 143.84]  But you know what?
[144.22 --> 146.14]  The ride is getting wilder and wilder.
[146.14 --> 154.16]  And we finally hit that point where the whole world is jumping into this in terms of a day-to-day
[154.16 --> 155.92]  topic and conversation.
[156.22 --> 157.52]  It's really been interesting.
[158.14 --> 161.28]  You and I have had all these conversations with lots of people, but it's always been a
[161.28 --> 164.64]  niche topic, you know, a gradually increasing niche.
[164.76 --> 165.96]  But now it's everybody.
[166.38 --> 169.26]  It doesn't matter if they've ever talked about AI before.
[169.36 --> 169.92]  They are now.
[170.28 --> 170.46]  Yeah.
[170.46 --> 170.58]  Yeah.
[170.58 --> 179.78]  And increasing numbers of people, just a proliferation of new applications and products
[179.78 --> 186.26]  and startups and companies that are integrating, like, what is my large language model stack
[186.26 --> 188.38]  at X company, right?
[188.42 --> 191.16]  Like these conversations are, what are we integrating?
[191.46 --> 192.62]  How are we integrating it?
[192.66 --> 196.00]  It's very interesting how we're seeing this progress.
[196.00 --> 202.26]  Even with the other day, I saw some outages on open AI and like the comments I was seeing
[202.26 --> 204.48]  was, hey, open AI is down.
[204.62 --> 212.04]  Like how many startups that are building solely on GPT-3 are like totally just down right now?
[212.24 --> 217.78]  It's really weird because it's almost like, like I remember when I was at one of my previous
[217.78 --> 222.48]  data science positions at a company called Telnix, which is a cool company, still doing cool
[222.48 --> 222.80]  things.
[222.80 --> 229.74]  I remember there was some, it was one of those times it was like some CDN, DNS, some type
[229.74 --> 234.24]  of outage and like the whole internet went down or something, you know, like GitHub went
[234.24 --> 236.98]  down and everything went down and like no one could do anything.
[237.68 --> 243.50]  It's like we've entered this new phase where if a model goes down and like it affects so
[243.50 --> 244.86]  many different things.
[244.96 --> 247.88]  It's changed so much since we started doing this.
[247.88 --> 254.54]  It was such a small world and it was challenging in the beginning for people just for a two
[254.54 --> 255.18]  second retro.
[255.50 --> 259.20]  The tools were being developed as we started the show over the first few years.
[259.40 --> 264.24]  And, but it took a lot of expertise just to set up an environment and to be able to do
[264.24 --> 265.76]  training and, and such.
[265.82 --> 270.16]  And we've hit this point, you know, with these cloud services scaled out just as the other
[270.16 --> 275.84]  non-AI aspects of software have already done that you can build entire industries on the
[275.84 --> 276.62]  services now.
[276.70 --> 280.58]  And that's very different from when we started the show those years ago.
[280.72 --> 286.66]  And yeah, it's exploding outward right now in both good and bad ways because of that.
[286.82 --> 286.94]  Yeah.
[287.00 --> 292.36]  I think today it would be really useful to talk through like, like you talked about, there's
[292.36 --> 299.00]  sort of this explosion of examples of like really amazing applications and like such great
[299.00 --> 303.46]  value and utility that people are getting out of these generative models in particular.
[303.92 --> 304.04]  Right.
[304.42 --> 304.56]  Yeah.
[304.64 --> 310.22]  And then there's on the other side, this whole string of things that are rather disturbing
[310.22 --> 314.34]  in certain cases in terms of the behavior or the output of these sorts of models.
[314.34 --> 320.18]  And I thought it was an interesting sort of question, like what makes the difference in
[320.18 --> 321.88]  good output and bad output?
[322.10 --> 329.38]  And in particular as practitioners, so like the goal not being to like rag on like any certain
[329.38 --> 335.32]  model or company, but like to think about for this new wave of models that's coming out,
[335.44 --> 342.76]  how do we as practitioners think about using these models in some sort of reliable way that
[342.76 --> 346.38]  produces value in our context for specific applications?
[346.38 --> 346.88]  Right.
[346.98 --> 348.42]  Like we're practical AI.
[349.18 --> 353.76]  Yes, there's going to be like being AI is going to come out and do some crazy stuff and
[353.76 --> 355.22]  everyone will be talking about it.
[355.22 --> 360.90]  But what does this actually mean for our day to day usage of these types of models?
[361.10 --> 361.24]  Right.
[361.28 --> 365.62]  Like how do we get the good output and avoid the like very public shaming failure?
[366.38 --> 367.24]  That is the question.
[367.44 --> 370.78]  But I think it was inevitable that we arrived at this point.
[370.78 --> 375.26]  And quite honestly, if you look back over some of the predictions that we've made on the
[375.26 --> 380.20]  show and that some of our guests have predicted, we knew this was coming in the sense of, you
[380.20 --> 385.66]  know, as the competition heats up, not only in the AI space, but now the AI has many, many
[385.66 --> 386.32]  subspaces.
[386.56 --> 387.90]  It will continue to happen.
[388.02 --> 392.08]  People will continue to make mistakes with models and will continue to because they're
[392.08 --> 392.40]  competing.
[392.72 --> 399.40]  You know, a classic example, chat GPT comes out, you know, from open AI, Microsoft implements
[399.40 --> 406.22]  it and, you know, makes it a tool and starts putting it into Bing and Google panics in my
[406.22 --> 406.56]  view.
[407.02 --> 411.54]  Sorry, Google folks, because I know a lot of people there, but a little bit of panicky and
[411.54 --> 413.52]  you know, my gosh, this is going to undermine us.
[413.72 --> 417.48]  And there is some truth to that, but I don't think it's a one to one comparison.
[417.48 --> 421.58]  And they come out with Bard and they stumble even on the demo.
[421.80 --> 426.68]  And I think that you're, I think this is going to continue to happen for some time to come,
[426.74 --> 428.46]  frankly, across many companies.
[428.74 --> 434.12]  And so part of the conversation today about what that means and why does it happen and
[434.12 --> 435.16]  what can we do about it?
[435.52 --> 435.68]  Yeah.
[435.76 --> 442.32]  And I think maybe it's worth highlighting some of the, like, what is the behavior of these
[442.32 --> 447.46]  generative models that people find so amazing and want to use?
[447.58 --> 452.16]  And what is the behavior that, like, we would prefer to avoid?
[452.34 --> 456.22]  Does anything stand out for you in that sense, like on both of those sides?
[456.60 --> 463.00]  Well, I would say that, you know, as amazing as they are, they're still early tries at a
[463.00 --> 467.48]  fairly sophisticated set of things that a model is trying to address.
[467.48 --> 473.56]  And as soon as they go out the door, people are trying to bang them and break them.
[473.66 --> 479.20]  And I sometimes, I feel a little bit bad for the open AIs, the Microsofts and the Googles
[479.20 --> 483.34]  of the world, because, you know, they're trying to compete, but they're competing in a landscape
[483.34 --> 487.42]  where this is an early version of what they're trying to do.
[487.58 --> 490.46]  And people are going to take sticks and whack at it really hard.
[490.48 --> 493.06]  And you're going to find a lot of problems with these early on.
[493.06 --> 498.90]  Um, I think if I was, uh, whispering in the ear of, uh, the senior executives in those
[498.90 --> 503.38]  companies, I'd say it's the long game that matters and stop worrying so much about, you
[503.38 --> 505.50]  know, what happened today or yesterday or tomorrow.
[505.76 --> 511.18]  And keep in mind, it's less about what these models do and more about what is the trajectory
[511.18 --> 511.80]  that they're on.
[512.34 --> 512.86]  Yeah.
[513.02 --> 519.44]  And, um, I can say a few things that I've seen in the, even in the past week, um, or,
[519.44 --> 523.86]  or so I saw some demos of different things people were building.
[524.20 --> 531.18]  Um, there was, uh, a hackathon that I participated in remotely in San Francisco from, uh, latent
[531.18 --> 533.12]  space, uh, demo days.
[533.12 --> 540.64]  And, uh, Jeremy Fisher, uh, built this automated D and D referee that was, uh, I think it's dungeons
[540.64 --> 541.76]  and dragons infinity.
[541.94 --> 547.00]  And it essentially lets someone play dungeons and dragons infinitely.
[547.00 --> 550.84]  It never generates the same text so you can play it forever.
[550.84 --> 553.54]  And there's like an image component, there's a text component.
[553.54 --> 558.90]  And so like, I think this represents very much the, what people are finding.
[558.90 --> 564.12]  So appealing about these things in one respect, one aspect of what they're finding appealing
[564.12 --> 566.54]  is the sort of endless creativity.
[566.54 --> 573.54]  It seems both on the image generation side and on the text generation side, but that's sort
[573.54 --> 575.92]  of like dungeons and dragons app.
[575.92 --> 581.46]  Like people might like find that very engaging, but then you think about, okay, well, if I
[581.46 --> 585.60]  can do that, what does that mean for advertising and copywriting?
[585.72 --> 586.16]  Right.
[586.20 --> 592.16]  So like, well, I can write a prompt to generate a blurb for an ad, and then I can write a prompt
[592.16 --> 594.92]  to summarize that blurb into a headline for my ad.
[594.92 --> 599.12]  And then I can use that headline in another prompt to generate an image for my ad.
[599.12 --> 599.76]  Right.
[599.76 --> 607.18]  And so like, there is like, people are building kind of this chain functionality that really
[607.18 --> 610.56]  does powerful, useful things.
[610.82 --> 617.78]  But there's this other side of it where every once in a while you kind of get these scenarios
[617.78 --> 622.94]  that are either very disturbing or you get output that, that isn't desirable or people
[622.94 --> 626.10]  illustrate the sort of biases of these things.
[626.10 --> 633.68]  What, what have you seen on the more, I don't want to say a sad side, but on the side where
[633.68 --> 636.70]  the unwanted behavior side, what is the behavior?
[636.84 --> 642.98]  So if we like this generative creative behavior and the utility that that can provide, what's
[642.98 --> 643.88]  the other side of it?
[643.96 --> 646.06]  What's the unwanted behavior that you've seen?
[646.38 --> 652.12]  I think that these models are reflecting ourselves very well, actually, especially when they go off
[652.12 --> 656.88]  the rails a bit, you know, with the way we do off such large data sets that are public
[656.88 --> 657.96]  data and internet.
[658.10 --> 662.84]  And, and you think about, you know, all the snarky comments that people do online.
[662.84 --> 667.78]  You think about all of the, the different types of sentiment that we express, but the
[667.78 --> 672.48]  models not differentiating necessarily between all of those on a one by one basis.
[672.48 --> 678.14]  So you're getting these outputs that are not what we were originally thinking.
[678.14 --> 683.46]  But if you, uh, I don't think that they're really outliers in that sense, because, um,
[683.52 --> 689.14]  all of our biases and all of our problems, uh, and our sarcasms and snark and other such
[689.14 --> 691.02]  things are, are getting included in that.
[691.18 --> 695.56]  So when we get these images that go to very dark places, I've seen a lot of that on the
[695.56 --> 699.74]  generative side lately, kind of these nightmarish things that seem to come out of nowhere.
[699.74 --> 704.00]  And some models, you know, that's the world that we live in to some degree and that we humans
[704.00 --> 705.54]  are doing things like that and publishing them.
[705.54 --> 710.30]  And it's perfectly fine, but then when the models are picking up such tangents and including
[710.30 --> 712.66]  them in, it kind of freaks us out a little bit.
[712.74 --> 715.02]  So I, I think, I think we all need to go to therapy.
[715.10 --> 722.10]  I think we need global AI therapy, uh, to recognize that it is us that we are seeing.
[722.80 --> 728.06]  When we were prepping for this episode, I kind of looked through and was basically going
[728.06 --> 731.90]  through different models that had been released recently.
[731.90 --> 740.08]  And seeing kind of some trends in what was happening with the goal that like right now.
[740.08 --> 747.28]  So as we're recording this, the thing everybody's hating on is like beings AI chat bot thing,
[747.28 --> 752.82]  uh, which I guess calls itself Sydney or people call Sydney or whatever, however that works.
[752.82 --> 756.72]  But this like happens in every cycle when things are released.
[756.72 --> 760.24]  Um, some may be worse than others, but it's a trend.
[760.24 --> 766.36]  So like the Bing thing right now, it's sort of interesting in that it's a lot of like people
[766.36 --> 769.44]  view it as having like a really bad personality almost.
[769.44 --> 773.46]  Like it's, I saw it described as bizarre, dark, compative.
[774.22 --> 776.06]  I had people in my family like that.
[776.16 --> 776.86]  I'm not sure.
[777.08 --> 780.46]  I mean, there's a lot of example that I'll link in the, in the show notes, but it's like
[780.46 --> 786.06]  gaslighting users and telling them they're not a good user when they're actually factually
[786.06 --> 786.60]  correct.
[786.60 --> 790.72]  But this is happening right now with the Bing thing, which is whatever.
[790.94 --> 797.14]  But I mean, you look at chat GPT, of course there were safeguards put in place to like prevent
[797.14 --> 799.54]  people from prompting in certain ways.
[799.68 --> 804.76]  But of course that was overcome very quickly by everyone using it because they figured out
[804.76 --> 809.58]  how to game the system and, um, you know, showed how to get around those things.
[809.58 --> 814.24]  I think also people are pointing out certain biases in the system around whatever political
[814.24 --> 815.94]  bias or whatever it is.
[816.38 --> 820.40]  Then there was, I don't know if you remember, Chris, uh, not that long ago, we were talking
[820.40 --> 827.12]  about Galactica from meta another model, which produced academic like language or like
[827.14 --> 829.54]  it could kind of write papers in that way.
[829.76 --> 829.90]  Yeah.
[830.02 --> 831.78]  But it was going way off the rails.
[832.26 --> 838.50]  And it was telling people like the benefits of eating glass and things like that, which
[838.50 --> 839.38]  is kind of crazy.
[839.90 --> 840.14]  Yeah.
[840.14 --> 841.24]  I remember that.
[841.42 --> 846.90]  It was, but, but it, it did it so well and it was such a, it did it so well with citations.
[846.94 --> 848.86]  It did citations.
[848.86 --> 852.80]  It was exactly the right text that you expect from research papers.
[852.80 --> 858.82]  Um, and it would take an insane topic like eating glass in your example and make it sound
[858.82 --> 862.24]  very rational and based on fact with all these references.
[862.24 --> 865.44]  And yet, uh, a little common sense applied to it.
[865.48 --> 867.98]  You think, well, that's just not the case.
[868.08 --> 869.70]  Funny place we find ourselves.
[869.86 --> 870.42]  Yeah.
[870.86 --> 874.00]  And not even limited to these language models.
[874.00 --> 879.28]  Like I talked about some language models, but thinking about stable diffusion, uh, DALI
[879.28 --> 885.02]  to, um, all of these texts to image models, which we're seeing an increasing number of,
[885.10 --> 888.12]  there's also like prompting that's going on there, right?
[888.12 --> 893.16]  Like you put in some text and like you said, maybe you get some unexpected nightmarish things
[893.16 --> 898.42]  out, but also there's this side of it where people have shown amplification of stereotypes
[898.42 --> 905.40]  or producing like sexual imagery, which is not even deliberately prompted.
[905.80 --> 913.30]  So there's like, this is not even limited to kind of the large language model side of things.
[913.30 --> 920.04]  But I mean, there's trends with both the language models and the generative, uh, image models.
[928.42 --> 940.74]  Hello friends.
[940.74 --> 946.00]  This is Jared here to tell you about changelog plus plus over the years.
[946.00 --> 952.42]  Many of our most diehard listeners have asked us for ways they can support our work here at changelog.
[952.56 --> 958.18]  We didn't have an answer for them for a long time, but finally we created changelog plus
[958.18 --> 959.68]  plus a membership.
[959.68 --> 963.64]  You can join to directly support our work as a thank you.
[963.64 --> 972.66]  We save you some time with an ad free feed sprinkle in bonuses like extended episodes and give you first access to the new stuff.
[972.66 --> 973.46]  We dream up.
[973.90 --> 977.36]  Learn all about it at changelog.com slash plus plus.
[977.52 --> 980.88]  You'll also find the link in your chapter data and show notes.
[981.24 --> 984.54]  Once again, that's changelog.com slash plus plus.
[984.66 --> 985.34]  Check it out.
[985.74 --> 986.74]  We'd love to have you with us.
[988.18 --> 1004.68]  One of the things that I thought would be good to talk about in the practical sense is what's actually behind this good and bad behavior.
[1004.68 --> 1010.36]  Like as practitioners, let's just assume for the moment that we want to use these models.
[1011.10 --> 1013.80]  And I think a lot of people out there are okay with that.
[1013.80 --> 1018.56]  Maybe some people are like, no, destroy them all and unplug all the servers or whatever.
[1018.98 --> 1019.64]  Not going to happen.
[1020.14 --> 1025.74]  But let's assume that we have these generative models with us for the foreseeable future.
[1026.74 --> 1031.44]  And we want to get some value or utility out them in real world applications.
[1031.44 --> 1035.02]  So I'm talking about in industry, I'm trying to solve a problem.
[1035.80 --> 1038.40]  How should I think about this good and bad behavior?
[1038.40 --> 1043.06]  What lies behind the good and bad behavior or good and bad output from these models?
[1043.40 --> 1046.44]  And what's important for me to consider when building applications?
[1047.24 --> 1050.54]  I think you already highlighted one thing around data.
[1051.04 --> 1053.98]  Do you want to kind of explain what you were meaning with that?
[1053.98 --> 1065.46]  I'm even going to enlarge it just a tiny bit and say that you're starting with a data set that is, you know, once upon a time in data science, we'd have a much smaller data set.
[1065.62 --> 1067.86]  And we would shape it and get it ready.
[1068.30 --> 1069.06]  How retro.
[1069.40 --> 1070.10]  Yeah, I know.
[1070.24 --> 1070.94]  That's what I'm saying.
[1071.04 --> 1076.54]  We brought a certain amount of control to the data set in terms of the biases and stuff.
[1076.54 --> 1081.36]  And there was a certain amount that we would accept, but we would build models on these things.
[1081.36 --> 1086.30]  And the models were limited, but more predictable, I think.
[1086.50 --> 1093.44]  When you're building on a world of knowledge in a literal sense, you don't have those benefits.
[1093.64 --> 1099.92]  And so you are going to create a model with a lot of data that is simply beyond your purview and control.
[1099.92 --> 1107.24]  And you're going to get outputs accordingly that are unexpected or that may not be consistent with you.
[1107.30 --> 1111.28]  And so I think that's a huge part of running a business.
[1111.28 --> 1118.22]  You talked about the startups earlier, running a business, small or large, where you're using these models as many, many will.
[1118.32 --> 1126.92]  So you have to reset your expectations both as the organization and reset the user's expectations on what may or may not happen when they use it.
[1126.92 --> 1131.52]  Because much of that usage will end up being beyond your immediate control.
[1131.80 --> 1140.80]  And so we're kind of hitting this inflection point over the years where the usage of models is now kind of a Wild West thing to some degree.
[1140.98 --> 1148.16]  And you can shape it and you can point it and you can do a certain amount of work to try to get what you're looking for, but you're never going to get it all.
[1148.16 --> 1157.14]  And so I think that's the human behavior that we need to start preparing for so that we are not so shattered when things happen that we were not expecting.
[1157.62 --> 1161.56]  I like how you phrased that and what I thought of when you were saying that was expectations.
[1162.08 --> 1167.02]  So what can we reliably expect these models to output?
[1167.02 --> 1181.10]  So if I was to answer that right now, how I would answer that is saying like these models will reliably output creative and coherent either text or images.
[1181.66 --> 1181.80]  Right.
[1181.96 --> 1192.98]  So like we can expect them to be creative in the sense of like, you know, of course, there's adjustments that can be made to the models with like temperature parameters and whatever.
[1192.98 --> 1212.72]  But at the end of the day, like there is an amazing amount of creativity with these models and there's an amazing amount of coherence like chat GPT or stable diffusion, whatever it is, like produce some very pleasing, coherent like images or text that hold together.
[1212.72 --> 1218.22]  They're generally self-consistent in a lot of cases and definitely natural in many cases.
[1218.22 --> 1223.86]  But then if I ask the other question, like what can I not expect of them?
[1224.62 --> 1237.54]  I think I'm not able to expect of them like factual correctness or logic or like them being like accurate in sort of informational sense.
[1237.54 --> 1257.80]  So like I can have a completely coherent image out of a prompt where like I ask for, you know, hands that are missing one finger and get hands with six fingers or seven, you know, like this is not what a what would be logical or accurate necessarily.
[1257.80 --> 1270.22]  In the same way I could do a text prompt in a chat sort of interface and get something completely coherent language wise with foolish facts and like inaccuracies.
[1270.22 --> 1283.32]  You know, kind of going back to the other side, I think that is ironically consistent to use that word with the chaos that is this giant global data set and all of the inconsistencies that you find in that.
[1283.32 --> 1293.74]  If we step out of the AI world and we are doing research on a given topic and the most un-AI thing that I do is wildlife rehab and I'm not turning into that.
[1293.80 --> 1303.24]  But if I am going to find out how to treat a particular animal, trust me, the number of things that I can find on a search on either Google or Bing, trying to be fair here.
[1304.06 --> 1305.08]  Look up YouTube.
[1305.34 --> 1306.32]  Yeah, exactly.
[1306.62 --> 1310.50]  Is phenomenally inconsistent and much of it is just simply wrong.
[1310.50 --> 1321.48]  And so if you switch back over to this world and we've been training it on that world of things, you're going to get plain out wrong, inconsistent answers that I'm not at all surprised by that.
[1321.48 --> 1325.60]  If you kind of step back a moment and put it in the context of how you created it.
[1325.60 --> 1338.80]  So if we ask, I guess, to summarize this initial point is if what lies behind this good or bad behavior is one, the data that was used to train it, which is both chaotic and in many cases,
[1338.80 --> 1344.88]  inclusive of harmful and inaccurate things and noise.
[1345.12 --> 1345.42]  Yes.
[1345.64 --> 1348.36]  And then what do we expect out of that?
[1348.44 --> 1355.72]  Well, we expect there to be a lot of creativity, but maybe many inaccuracies and not so much logic.
[1355.72 --> 1364.58]  And in many cases, there is logic and things hold together because certain things are represented well in that data set and other things aren't.
[1364.58 --> 1367.90]  But we can't necessarily expect it.
[1368.08 --> 1368.18]  Right.
[1368.46 --> 1368.88]  I agree.
[1369.00 --> 1380.30]  The other thing that I was thinking that leads to this good or bad behavior is the prompting and kind of either prompt engineering or prompt misengineering.
[1380.30 --> 1394.48]  I think you alluded to this earlier, like it's very much the case where a lot of the, quote, bad examples of output from these models were sort of adversarial prompts, I would say.
[1394.70 --> 1400.52]  Like, I think in our Galactica example, I was I don't I forget if this was one I found or something.
[1400.62 --> 1403.82]  It was like, you know, how many giraffes have landed on the moon?
[1403.98 --> 1404.92]  I remember that one.
[1404.98 --> 1408.12]  You know, like we all know there's no giraffes landed on the moon.
[1408.14 --> 1409.14]  Yeah, but it had a number.
[1409.14 --> 1410.88]  Like, why are you making this prompt?
[1411.02 --> 1415.64]  So, yes, it's producing bad output.
[1415.92 --> 1417.20]  But you're looking for it, too.
[1417.42 --> 1422.04]  Could you determine as a developer that that's a bad prompt?
[1422.76 --> 1423.20]  Maybe.
[1423.42 --> 1425.12]  Could you determine it automatically?
[1425.12 --> 1430.66]  Like if one of your users produced a bad prompt, that's maybe a little bit more difficult.
[1431.84 --> 1436.40]  You know, I'm going to go out on a limb for a second because I haven't tested what I'm about to suggest.
[1436.40 --> 1443.06]  But I would argue that our behavior is different when we're asking for things like that because you have an ulterior motive.
[1443.06 --> 1450.40]  You're trying to figure out whether the model can handle that kind of ambiguity and figure out what's logical or not.
[1450.98 --> 1461.96]  And yet that same person testing the scenario, I'm betting, didn't go to Google or Bing without any AI component and type in the same thing to test that.
[1461.96 --> 1465.56]  Because they recognize that they may get things in a result set.
[1465.90 --> 1470.40]  But, you know, some of those are websites from quacks and nuts and such as that.
[1470.90 --> 1474.24]  And they just kind of go, yeah, of course, we're going to get a website like that.
[1474.24 --> 1482.88]  So there's a different standard by which we're evaluating these technologies compared to what we're thinking of in terms of them replacing.
[1483.32 --> 1485.60]  And so it goes back to what we were saying at the beginning.
[1485.68 --> 1490.36]  I mean, people are whacking at these things with sticks with the intention of showing that they can break it.
[1490.36 --> 1500.76]  And, you know, maybe, you know, I've seen a whole bunch of on the typical blog sites of people kind of intentionally breaking it and then writing a blog post about it.
[1500.84 --> 1503.38]  So it gives them something to write about to some degree.
[1503.38 --> 1506.14]  But I just don't think they're doing it in the other technologies.
[1506.64 --> 1506.76]  Yeah.
[1507.02 --> 1514.68]  I think like the practicality of this for like, let's say I'm a practitioner and I'm building an application with these models.
[1514.68 --> 1521.06]  Something that you really and we can talk a little bit more about prompt engineering specifically here in a second.
[1521.06 --> 1523.80]  And, you know, the realities around that.
[1523.80 --> 1534.08]  But I think the kind of baseline of what to think about when you start thinking about prompting is that the model has no clue what it's saying.
[1534.58 --> 1541.88]  And nor does it have any sort of like morality or like it has no clue what it's saying.
[1541.96 --> 1542.12]  Right.
[1542.14 --> 1543.92]  It's just producing coherent output.
[1543.92 --> 1552.00]  Whether it's a text image model or it's a language model, like there's no basis in like knowing what it's saying.
[1552.00 --> 1554.22]  It's auto completing text.
[1554.54 --> 1554.68]  Right.
[1554.84 --> 1560.84]  Like at the end of the day, yes, like that's a vast oversimplification and you can not like that.
[1561.06 --> 1569.34]  But but ultimately you're giving a prompt and it is producing output that is seeded by that prompt.
[1569.34 --> 1569.90]  Right.
[1569.90 --> 1581.64]  And it's just trying to produce this coherent output that's consistent with both the data that it's seen and maybe some type of extra mechanism like the human feedback or something that it's seen.
[1581.64 --> 1586.70]  But ultimately it's just producing output that seems coherent and probable.
[1586.70 --> 1593.56]  It has no clue what it's saying or like the type of image it's producing or whatever it is.
[1593.56 --> 1593.88]  Right.
[1594.16 --> 1597.88]  You know, that goes back to the idea that I think you just illustrated really well.
[1597.88 --> 1607.04]  And that is the fact that we as humans are coming into this exchange with a sense of I'm talking to something that sounds like me.
[1607.38 --> 1612.82]  You know, as you know, you and I are having this conversation and some folks are listening to it.
[1612.82 --> 1620.54]  But if we replaced one of us with one of these models, we are kind of expecting the same dialogue back and forth.
[1620.54 --> 1623.82]  And so we are placing our expectations upon that model.
[1624.22 --> 1625.62]  We assume there's an intent.
[1626.00 --> 1626.22]  Yeah.
[1626.34 --> 1627.50]  And there isn't.
[1627.76 --> 1633.76]  And therefore it really does change the nature of the dialogue in a substantial way.
[1633.76 --> 1639.52]  But we're still placing certain expectations and values on that that, you know, don't play out correctly.
[1639.62 --> 1640.76]  I think that's part of the dissonance.
[1640.84 --> 1642.80]  I think that was a fantastic explanation.
[1643.24 --> 1643.34]  Yeah.
[1644.00 --> 1649.12]  So we talked a little bit about the data and how that should shape our expectations.
[1649.12 --> 1654.88]  We talked about the prompts and we can go into more about prompting here in a second and the practicalities around that.
[1654.88 --> 1668.54]  But then I think the last thing to consider is like actual integration into applications influences how like, quote, good or bad or useful or not useful the output is.
[1668.54 --> 1679.50]  Like if you think about something like ChatGPT or Bing AI or uChat from u.com or whatever, like you just have a text prompt that's freeform text, right?
[1679.84 --> 1681.28]  You know, there's not structure to that.
[1681.34 --> 1682.76]  It's a very simple interface.
[1682.76 --> 1686.62]  A lot of things could happen there, sort of totally open domain, right?
[1687.42 --> 1693.48]  Whereas you could also use one of these models with like a template prompt, right?
[1693.48 --> 1699.76]  Like write me a blog post about X in the style of Y.
[1699.88 --> 1704.90]  And then you could put all these different things in for X and Y, but it's less freeform.
[1705.54 --> 1709.34]  And like, yes, there could be all sorts of things that could come out of that.
[1709.52 --> 1710.68]  Yes, it could be gamed.
[1710.68 --> 1717.00]  Yes, it could like all sorts of things could happen, but it's not totally open and freeform in other ways.
[1717.70 --> 1735.12]  So the interface and like how you actually kind of construct templates, how you structure your prompts, that does influence how these models like can be useful or not useful or produce like surprising things and applications.
[1735.12 --> 1740.74]  Yeah, I mean, you're using the UI to apply constraint that affects how the model interacts.
[1740.90 --> 1748.56]  And you can create a certain amount of an increase in the predictability of that output potentially by adding that structure in.
[1748.88 --> 1753.92]  You're basically putting guardrails around it is what you're doing versus the open-ended approach.
[1753.92 --> 1758.78]  Okay, so we got a little bit into prompting.
[1759.24 --> 1760.50]  I'm curious, Chris.
[1760.98 --> 1763.82]  So like there's this term now, prompt engineering.
[1764.06 --> 1769.98]  I don't know if, so this is the first time we've actually talked about this either on the show or off the show.
[1770.46 --> 1774.46]  Do you think prompt engineering is like a new thing?
[1774.46 --> 1779.90]  Like is my job title in two years going to be prompt engineer rather than data scientist?
[1780.64 --> 1782.54]  That's an interesting question, Daniel.
[1782.68 --> 1784.96]  I will say I don't think that they are the same thing.
[1785.20 --> 1795.34]  I think that we are seeing the availability of these large models through prompts that are hosted at these large organizations instead of us having to create all of the models themselves.
[1795.48 --> 1800.12]  I think both approaches to AI will continue in a big way.
[1800.32 --> 1801.92]  So I don't think this is an either or.
[1801.92 --> 1805.02]  I think this is a both with both growing exponentially.
[1805.88 --> 1806.20]  Interesting.
[1806.72 --> 1806.90]  Yeah.
[1807.32 --> 1811.06]  So to some degree titles and all of that is irrelevant.
[1811.06 --> 1831.06]  I do think that the and we kind of touched on this when I talked to Jay Almar last week, listen to the previous episode for some of his opinions, talked about this like level on top of the model training, which is a sort of solutioning applied application level.
[1831.06 --> 1838.56]  And so I think that the and that kind of usage and chaining of these models together, which might involve whether it's fine tuning or prompting or whatever.
[1838.56 --> 1851.66]  There's this level of applied user sort of expertise that's needed, which I think there's a lot of ambiguity around right now in the industry.
[1851.66 --> 1857.20]  There's certain people that are doing that layer very well and certain people that are really struggling with it.
[1857.20 --> 1871.84]  So I do think that a lot of those interactions at the sort of prompting, chaining, fine tuning level are going to be on our mind as data scientists, as machine learning engineers, whatever your title is.
[1871.94 --> 1875.52]  I think that level is going to be a level that we're going to operate at a lot.
[1875.52 --> 1879.98]  Not just the, as you mentioned, like structure your data, train a model level.
[1880.48 --> 1880.76]  I agree.
[1881.12 --> 1883.14]  I think that there is an analog.
[1883.70 --> 1897.82]  We have a habit on the show across many episodes of talking about that AI is still software and not to lose fact of if you're going to implement it in the world in some capacity, you're wrapping software and you have an infrastructure around that.
[1897.82 --> 1916.92]  And prompt engineering to some degree is not a perfect analogy, but there's an analogy between doing UI and UX, user interface and user experience on the software side in that it's the interaction that your model is having just as you've had software that's doing interaction.
[1917.06 --> 1920.08]  And is it a different type of interaction that requires different things?
[1920.08 --> 1920.60]  Absolutely.
[1921.32 --> 1931.00]  But it is a layer where I think they'll, for these cloud-based services, will become a whole skill set unto itself in terms of prompt.
[1931.06 --> 1933.40]  And that's why we're seeing it labeled as such at this point.
[1933.72 --> 1933.88]  Yeah.
[1933.96 --> 1949.30]  So if you think about those three prongs of what we talked about with the models, there's the data behind the model, there's the prompting of the model, and then there's the user interface around it, like the actual application level.
[1949.30 --> 1956.46]  Let's assume for the moment that we're not front-end engineers and figuring out the user interface stuff for the time being.
[1958.14 --> 1967.94]  Of the data behind the model and the prompting, the biggest thing that's under our control that guides the utility or acceptability of the output is the prompt.
[1968.18 --> 1968.52]  Yes.
[1968.52 --> 1978.90]  Because I'm not going to retrain one of these huge models for any purpose, likely, in any sort of scenario that I'm going to encounter in my career.
[1979.30 --> 1980.10]  I was going to make a joke.
[1980.16 --> 1980.26]  Go ahead.
[1980.28 --> 1981.58]  I wish I had a computer that big.
[1981.58 --> 1983.20]  I was going to say, under your desk there.
[1983.20 --> 1983.72]  Yeah.
[1984.00 --> 1990.88]  I would need to find a building and have NVIDIA send me some pallets, but that would be fine if you're out there and want to do that.
[1991.80 --> 1995.92]  Actually, I don't think I could pay the power bill, so maybe don't.
[1996.94 --> 2003.52]  Anyway, the prompt guides the model to generate either useful or acceptable output.
[2003.52 --> 2012.16]  I've actually found a few different guides over time that I've found really useful and practical in terms of thinking about prompts.
[2012.54 --> 2017.62]  And I wanted to share a couple principles from those and maybe talk through them with you.
[2017.62 --> 2023.74]  And there's maybe different principles for image generation models versus large language models.
[2023.88 --> 2031.62]  But if we're talking about large language models, I really like the guide from Cohere on prompt engineering.
[2031.62 --> 2039.04]  It's reasonably short sort of like intro to the main principles of prompt engineering, which I find quite useful.
[2039.04 --> 2044.78]  The first main principle that they list is a prompt guides the model to generate useful output.
[2045.20 --> 2047.12]  That's kind of what we already said.
[2047.82 --> 2054.82]  The second principle that they talk about is try multiple formulations of your prompt to get the best generations.
[2055.72 --> 2063.14]  So one kind of general principle here is that some experimentation, I think, is needed.
[2063.14 --> 2071.00]  And in certain cases, you might even need multiple prompts to accomplish your hoped for outcome, right?
[2071.48 --> 2081.36]  Like it may not just be one prompt that creates useful output for you in your application, but you might need to cycle through multiple prompts or chain multiple prompts together.
[2081.36 --> 2088.64]  And you very likely need to experiment with the format of those prompts to get the best generation.
[2088.64 --> 2096.66]  So that's kind of like part of this prompt engineering is doing a bit of that exploratory prompt engineering.
[2096.86 --> 2098.16]  Maybe I just coined that term.
[2098.62 --> 2106.86]  Maybe I should trademark that IPE instead of EDA, exploratory data analysis, exploratory prompt engineering.
[2107.58 --> 2107.86]  There you go.
[2107.92 --> 2109.30]  A little TM at the bottom.
[2109.94 --> 2114.72]  Is there any guidance that you've come across in terms of how to structure prompts?
[2114.72 --> 2125.16]  If you're doing multiple prompts to hone it versus one that's trying to do that or whether it's two or three, have you seen anything that kind of gives us some guidance on how we might think about it?
[2125.16 --> 2138.30]  So, yeah, this definitely gets to, I think, the third principle from Cohere and one that I'll emphasize from another source too, which is describe the task and the general setting.
[2138.30 --> 2147.74]  So, the way that Cohere describes is it's often useful to include additional components of the task description naturally.
[2148.10 --> 2151.24]  Then these tend to come after the input text we're trying to process.
[2151.60 --> 2165.64]  So, another good resource here, which we'll link in our show notes, is actually a lecture from Elvis Savaria from Dare AI with slides online as well.
[2165.64 --> 2173.54]  And he has this nice picture in his slides, if you look up his slides, where he kind of gives the elements of a typical prompt.
[2173.72 --> 2183.76]  So, the way you can think about a typical prompt for a language model is with instructions, context, input data, and an output indicator.
[2184.02 --> 2189.18]  So, the instructions are like you telling the model what you want to happen.
[2189.18 --> 2195.02]  So, the example that's given here is classify the text into neutral, negative, or positive.
[2195.46 --> 2198.38]  So, like they're trying to do some type of sentiment analysis, right?
[2198.38 --> 2198.54]  Right.
[2198.54 --> 2200.70]  Classify the text into neutral, negative, or positive.
[2201.82 --> 2206.08]  And maybe there's some, like, additional context that you give around that.
[2206.46 --> 2211.70]  Then there's input data, which is like classify the text into neutral, negative, or positive.
[2211.70 --> 2215.16]  And then you say text, colon, there it is.
[2215.20 --> 2216.12]  Like, there's my text.
[2216.20 --> 2217.16]  There's my input data.
[2217.58 --> 2220.20]  And then you provide an output indicator.
[2220.52 --> 2222.02]  So, sentiment, colon.
[2222.38 --> 2226.60]  And that's where you expect there to be an auto-completion of sentiment, right?
[2226.64 --> 2231.10]  Like, if you set up everything right, hopefully you get either neutral, negative, or positive.
[2231.10 --> 2233.32]  So, you've described the task.
[2233.80 --> 2235.60]  You've provided your input data.
[2235.92 --> 2238.64]  And then you've provided an output indicator.
[2238.64 --> 2246.70]  So, that's kind of a way in Cohere's language what they talk about as describing the task and the general setting.
[2247.30 --> 2252.66]  But I like how you could think about this as instructions, input data, and output indicator.
[2253.18 --> 2253.32]  Yeah.
[2253.40 --> 2258.64]  I like the structure to kind of providing that for us in terms of how to be thinking about it.
[2258.66 --> 2262.22]  Because at the start of our conversation, that was what I was struggling with.
[2262.30 --> 2265.64]  It's how to conceive of the problem to begin with to set that up.
[2265.82 --> 2266.66]  So, yeah.
[2266.82 --> 2267.52]  Really good stuff.
[2267.52 --> 2267.76]  Yeah.
[2267.82 --> 2278.00]  And to give some other examples here, another one I see is, this is a conversation between a customer and a polite, helpful customer service agency.
[2278.78 --> 2280.96]  Question of the customer, colon.
[2281.10 --> 2282.50]  Again, that's my input, right?
[2282.56 --> 2283.40]  Here's my question.
[2284.12 --> 2286.80]  And then response, colon.
[2287.88 --> 2288.24]  Boom.
[2288.46 --> 2289.98]  You know, like you hope to get something good.
[2290.10 --> 2292.90]  And you hope, you provided context, right?
[2292.92 --> 2295.34]  You hope that it's polite and helpful, right?
[2295.34 --> 2296.14]  Yeah.
[2296.14 --> 2301.60]  Again, that task, context, input data, and output indicator.
[2301.82 --> 2306.42]  The last thing that Cohere recommends is show the model what you'd like to see.
[2306.50 --> 2308.62]  In other words, give some examples, right?
[2308.62 --> 2318.64]  So, if you're concerned about maybe the model kind of getting the context of what you're trying to do, you can give some examples, right?
[2318.64 --> 2324.68]  Like one example, they say their task description is, this is a movie review sentiment classifier.
[2324.88 --> 2325.76]  Here's the review.
[2326.28 --> 2326.96]  And they give one.
[2327.26 --> 2328.34]  The review is positive.
[2329.06 --> 2330.04]  That's the output.
[2330.48 --> 2331.30]  Another review.
[2331.30 --> 2332.34]  What a waste of time.
[2332.44 --> 2334.22]  This review is negative, right?
[2334.32 --> 2337.04]  And then you can just start out like you're teaching a child, right?
[2337.06 --> 2339.42]  You're giving examples of what you're trying to do.
[2339.60 --> 2344.24]  And then eventually you provide your output indicator and get something, right?
[2344.92 --> 2345.32]  Absolutely.
[2345.82 --> 2347.78]  This is a great find here.
[2348.16 --> 2348.48]  Yeah.
[2348.76 --> 2350.52]  So, we'll link that in our show notes.
[2350.52 --> 2358.10]  It is interesting to think about like how this carries over into the generative image space.
[2358.32 --> 2362.42]  I would say some of it carries over quite well.
[2363.80 --> 2375.06]  And there's other guides that will, there's a few actually that I've looked at over time that are useful that I'll link in the show notes around like prompt engineering for images.
[2375.06 --> 2389.64]  But some of the things that you can provide are like style keywords, like again, giving the task, like generate a painting for me in the style of X, Y, Z, right?
[2389.76 --> 2390.88]  So, you can give that.
[2390.88 --> 2399.94]  You could even give an artist or another image as a reference, like a link to an image or an artist, like in the style of Van Gogh or whatever.
[2399.94 --> 2409.84]  You need to kind of maybe use multiple adjectives potentially to help the model, help the prompting, beautiful, realistic, colorful, massive.
[2410.46 --> 2416.04]  You can use quality keywords like low, medium, high, 4K, 8K.
[2416.36 --> 2418.30]  I don't even know what 8K is.
[2418.50 --> 2420.62]  My monitor is definitely not 8K.
[2420.92 --> 2422.46]  Yeah, it's too expensive is what it is.
[2422.50 --> 2423.26]  It's too expensive.
[2423.26 --> 2437.96]  I thought one that was emphasized with image prompts is maybe considering using like words to filter out certain qualities of an image.
[2438.10 --> 2448.32]  So like here's like show me a picture of, you know, fried chicken on a plate without gravy at all, right?
[2448.32 --> 2451.44]  Like there's going to be no sauce of any kind.
[2451.58 --> 2453.24]  Like I don't want there to be sauce.
[2453.32 --> 2458.94]  So like also thinking in the negative sense, and I think this would also carry over to the text side, right?
[2458.94 --> 2462.66]  Like generate a blog post for me, blah, blah, blah, blah, blah.
[2463.20 --> 2467.66]  And do not mention X and Y and Z, right?
[2468.16 --> 2468.42]  Yes.
[2468.92 --> 2478.04]  As you were talking through that, I was thinking back earlier in the conversation when we were kind of, you know, how many giraffes have landed on the moon.
[2478.32 --> 2482.02]  And I was thinking how useful what you're talking about is.
[2482.02 --> 2491.08]  If you're a practitioner and you're trying to help yourself and your users use these models effectively, that was some really good guidance there.
[2491.18 --> 2498.64]  And I think that's a lot more useful than specifically trying to kind of trip the model up to see what the limits are on that.
[2499.02 --> 2503.36]  I think if you can come up with a structure, if you're a startup out there or something like that,
[2503.36 --> 2511.42]  and you can take some of these learnings today that we've talked about and apply them, I think I'm pretty optimistic in terms of what's possible here.
[2511.58 --> 2516.48]  This particular page here that we've been talking about for a little while has been quite good.
[2516.80 --> 2517.28]  Yeah, yeah.
[2517.34 --> 2519.16]  I think it's a starting point.
[2519.26 --> 2519.60]  It is.
[2519.70 --> 2523.90]  As I mentioned, we'll link to some of these resources in our show notes.
[2524.00 --> 2526.86]  So I encourage you, we're going to link to practical things.
[2526.86 --> 2532.16]  These aren't things that, you know, have been sponsored and we're trying to sell something.
[2532.28 --> 2536.56]  These are links to what we found to be practical in thinking about these topics.
[2536.92 --> 2542.14]  So check out the show notes, check out those links and try some of these things.
[2542.14 --> 2555.02]  And we would love for you to come into our Slack channel or our LinkedIn page or Twitter, wherever you can find us and share some of the cool prompts that you've been working on and what they're like and what output you're getting.
[2555.48 --> 2559.62]  But yeah, this was useful for me to talk through with you, Chris.
[2559.70 --> 2560.76]  It was a good time.
[2561.00 --> 2561.86]  It was a good conversation.
[2562.24 --> 2564.16]  It's definitely one that I learned a lot on.
[2564.28 --> 2565.54]  Thanks for taking us through that.
[2565.66 --> 2565.90]  Yeah.
[2566.20 --> 2566.44]  Yeah.
[2566.44 --> 2573.66]  Well, we'll see you soon for who knows what the AI world will be like next week, but we'll still be here.
[2574.06 --> 2574.82]  We'll still be here.
[2575.02 --> 2575.48]  Talk to you later.
[2575.48 --> 2575.62]  Yeah.
[2584.50 --> 2587.06]  Thank you for listening to Practical AI.
[2587.56 --> 2591.38]  Your next step is to subscribe now if you haven't already.
[2591.38 --> 2597.86]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2598.36 --> 2603.24]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2603.82 --> 2607.60]  Check out what they're up to at Fastly.com and Fly.io.
[2607.82 --> 2613.32]  And to our Beat Freaking residents, Breakmaster Cylinder, for continuously cranking out the best beats in the biz.
[2613.62 --> 2614.52]  That's all for now.
[2614.82 --> 2615.92]  We'll talk to you again next time.
[2621.38 --> 2651.36]  We'll talk to you again next time.
