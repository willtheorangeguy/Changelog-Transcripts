[0.00 --> 3.64]  The big picture with causal inference, essentially, it's exactly as it sounds.
[3.74 --> 6.10]  I guess I'm going to use the word and the definition, which I know you're not supposed
[6.10 --> 6.38]  to do.
[6.46 --> 10.88]  But if you're trying to answer a causal question, so does something cause something else, which
[10.88 --> 15.16]  often most of the questions we're interested in are in that framework, although it is distinct
[15.16 --> 17.70]  from something like prediction, which would be a different kind of space.
[17.70 --> 22.34]  But in the inference space, when we're trying to determine the relationship between different
[22.34 --> 27.44]  factors or different variables, a lot of times we talk about associations as a way to sort
[27.44 --> 31.42]  of describe relationships that we know maybe are correlated, but we don't want to go as
[31.42 --> 32.60]  far as to say they're causal.
[32.82 --> 38.36]  But I would argue in most cases, the human instinct is to want to talk about things causally.
[38.60 --> 42.36]  That's most of the time when we're studying relationships between variables, it's often
[42.36 --> 45.10]  because we want to know if there's a causal connection.
[45.10 --> 49.48]  So in randomized trials, like the ones that we're talking about with Pfizer and Moderna,
[49.58 --> 53.26]  looking at different vaccines, they're not just interested in whether or not getting
[53.26 --> 56.74]  a vaccine is somehow related to whether or not you get COVID.
[56.74 --> 60.08]  But they want to know if getting the vaccine will actually cause you to not get COVID.
[60.22 --> 64.36]  So this is sort of the relationship that we are focused on in causal inference.
[66.72 --> 69.02]  Bandwidth for ChangeLog is provided by Fastly.
[69.32 --> 71.20]  Learn more at Fastly.com.
[71.44 --> 73.72]  Our feature flags are powered by LaunchDarkly.
[73.72 --> 75.80]  Check them out at LaunchDarkly.com.
[76.04 --> 77.90]  And we're hosted on Leno cloud servers.
[78.30 --> 81.82]  Get $100 in hosting credit at Leno.com slash ChangeLog.
[82.48 --> 83.58]  What up, friends?
[83.58 --> 87.62]  You might not be aware of, but we've been partnering with Leno since 2016.
[87.98 --> 88.92]  That's a long time ago.
[88.92 --> 94.28]  Way back when we first launched our open source platform that you now see at ChangeLog.com,
[94.78 --> 96.30]  Leno was there to help us.
[96.72 --> 98.38]  And we are so grateful.
[98.92 --> 103.70]  Fast forward several years now, and Leno is still in our corner behind the scenes,
[103.84 --> 107.86]  helping us to ensure we're running on the very best cloud infrastructure out there.
[108.38 --> 109.02]  We trust Leno.
[109.02 --> 111.74]  They keep it fast, and they keep it simple.
[112.06 --> 115.26]  Get $100 in free credit at Leno.com slash ChangeLog.
[115.40 --> 121.30]  Again, $100 in free credit at Leno.com slash ChangeLog.
[121.30 --> 141.86]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[142.18 --> 143.94]  productive, and accessible to everyone.
[144.22 --> 148.34]  This is where conversations around AI, machine learning, and data science happen.
[148.34 --> 153.06]  Join the community and Slack with us around various topics of the show at ChangeLog.com slash
[153.06 --> 154.70]  community, and follow us on Twitter.
[154.84 --> 156.46]  We're at Practical AI FM.
[163.00 --> 166.30]  Welcome to another episode of Practical AI.
[166.66 --> 168.42]  This is Daniel Whitenack.
[168.54 --> 174.76]  I'm a data scientist with SIL International, and I'm joined, as always, by my co-host, Chris
[174.76 --> 179.40]  Benson, who is a principal emerging technology strategist at Lockheed Martin.
[179.64 --> 180.30]  How are you doing, Chris?
[180.70 --> 182.00]  I am doing very well, Daniel.
[182.04 --> 182.60]  How are you today?
[183.10 --> 184.48]  I can't complain.
[184.78 --> 186.20]  No complaints from this end.
[186.78 --> 188.84]  I had a good, restful weekend.
[189.36 --> 197.20]  As listeners might remember, I recently downloaded the new Tony Hawk Pro Skater for Xbox, and that's
[197.20 --> 204.78]  been filling my waking moments as I try to increase my combo scores to ridiculous numbers.
[204.94 --> 206.00]  I'm so jealous.
[206.18 --> 207.86]  You had a much better weekend than me.
[207.96 --> 210.30]  I had a weekend full of honeydew lists and stuff.
[210.40 --> 214.06]  I mean, I've just, I was exhausted and happy to return to work on Monday morning.
[214.88 --> 216.14]  I've got a pretty cool wife.
[216.24 --> 217.78]  She, she played with me.
[217.88 --> 222.84]  So there are things on my honeydew list, but it was okay because we were, you know, we were
[222.84 --> 225.58]  spending that quality Tony Hawk time together, so.
[225.78 --> 228.92]  Yeah, I have like, I kept hammering my thumb and things like that.
[228.92 --> 229.64]  It's just terrible.
[229.96 --> 232.00]  Oh, it was, yeah, horrible.
[232.34 --> 233.14]  That's rough, man.
[233.18 --> 233.86]  I'm just wounded.
[234.22 --> 235.90]  I'm the walking wounded now, man.
[235.96 --> 236.52]  That's terrible.
[236.60 --> 237.26]  Anyway, go ahead.
[237.66 --> 238.46]  You keep talking.
[239.22 --> 244.66]  Yeah, well, I won't, you know, go into the cause of you hitting your thumb with a hammer,
[244.66 --> 249.42]  but we are going to talk a lot about causes today and causal thinking.
[249.42 --> 256.80]  Today, we're really lucky to have with us Lucy D'Agostino-McGowan, and she is an assistant
[256.80 --> 260.54]  professor in statistics at Wake Forest University.
[260.90 --> 266.68]  She's also very involved in the R conference and giving a talk at the upcoming government
[266.68 --> 272.66]  and public sector R conference, which actually Practical AI is a media sponsor of.
[273.20 --> 274.82]  So welcome, Lucy.
[274.90 --> 276.54]  It's really great to have you here with us.
[277.08 --> 277.32]  Thanks.
[277.36 --> 278.46]  I'm excited to be here.
[278.46 --> 281.98]  Yeah, it's wonderful to collaborate with you on this.
[282.24 --> 286.72]  We should say, too, that you are also the co-host of a podcast.
[287.04 --> 287.98]  I think you're the co-host.
[288.12 --> 289.76]  There's another host of a podcast.
[290.40 --> 291.32]  Ellie Murray and I.
[291.70 --> 293.92]  Yes, of causal inference.
[294.34 --> 296.26]  So casual, casual inference.
[296.70 --> 297.10]  I'm sorry.
[297.34 --> 299.56]  I'm getting mixed up with our topic for the day.
[299.68 --> 300.70]  Good call.
[301.18 --> 301.66]  That's right.
[302.04 --> 303.02]  Casual inference.
[303.52 --> 303.76]  Yes.
[303.78 --> 304.66]  Yes, it's a pun.
[304.82 --> 305.10]  We got to.
[305.74 --> 306.60]  Yeah, all good.
[306.60 --> 312.30]  I kept trying to pitch pun names for our podcast and none of them made it through the filter.
[312.56 --> 313.48]  So I don't know.
[313.58 --> 316.68]  I don't know what the reason is for that, but I'm all for pun names.
[317.00 --> 318.24]  So they just weren't very punny.
[318.70 --> 319.42]  Oh, OK.
[322.12 --> 323.14]  Yeah, I love a good pun.
[323.20 --> 325.48]  We have some segments that have pun names as well.
[325.56 --> 326.98]  It's a good a good time.
[326.98 --> 327.74]  Yeah.
[327.86 --> 329.22]  Yeah, yeah, for sure.
[329.40 --> 331.66]  So we will put a link to that in our show notes.
[331.80 --> 332.18]  Definitely.
[332.50 --> 336.88]  I encourage our listeners to check out the podcast and see what they have of those really
[336.88 --> 337.60]  good content.
[337.60 --> 342.54]  But before we jump into all of the great things that you're involved with and that you're
[342.54 --> 347.54]  passionate about in terms of data science and R and causal inference and casual inference,
[347.54 --> 353.34]  if you could just let us know a little bit about your background, how you got interested
[353.34 --> 358.40]  in data science and R and other things and how you ended up where you're at right now
[358.40 --> 359.50]  and what you're working on.
[359.86 --> 360.10]  Yeah.
[360.54 --> 363.30]  So my background is in biostatistics.
[363.30 --> 366.62]  So I have a PhD in biostatistics from Vanderbilt.
[366.98 --> 370.28]  And so that's essentially statistics for the medical field.
[370.28 --> 376.82]  But while I was doing the work there, I had an internship with RStudio for six months.
[377.00 --> 380.98]  And so as part of that, I mean, biostatistics is a pretty applied statistical field.
[380.98 --> 385.78]  And so there's lots of kind of programming and data science-like things involved with the
[385.78 --> 386.38]  training there.
[386.70 --> 391.12]  But then the software component was something that really interested me kind of further
[391.12 --> 393.08]  than even what we were doing already.
[393.24 --> 395.10]  And so I pursued it more.
[395.10 --> 400.22]  I got heavily involved with RLadies and did this internship under Jenny Bryan.
[400.28 --> 404.84]  RStudio, which really kind of built up some of my coding chops and being able to actually
[404.84 --> 407.08]  do software development and things like that.
[407.48 --> 409.70]  And RLadies, if you could describe that.
[409.74 --> 410.66]  That's what I was going to ask.
[411.04 --> 411.16]  Yeah.
[411.28 --> 411.76]  Oh, yeah.
[412.10 --> 412.36]  Yeah.
[412.40 --> 416.90]  So RLadies is basically an organization, a global organization that there's the global
[416.90 --> 417.96]  kind of aspect of it.
[418.00 --> 422.44]  But then they're also, it's mostly run by local meetups in different communities.
[422.44 --> 426.56]  And the idea is to sort of increase the gender diversity in the R community.
[426.56 --> 432.94]  And so I had started one in Nashville and they exist kind of all over the world.
[433.14 --> 437.04]  And they do really excellent work in trying to sort of increase that diversity.
[437.30 --> 438.20]  And it's been great.
[438.28 --> 439.50]  It's been actually really successful.
[439.66 --> 443.26]  There's some really fun plots that you can see as sort of the first couple.
[443.38 --> 448.30]  It started in San Francisco and then it really has taken off since then in the past couple
[448.30 --> 448.66]  years.
[449.20 --> 449.30]  Yeah.
[449.30 --> 451.64]  It's kind of all over the place now, isn't it?
[451.72 --> 452.28]  It is.
[452.40 --> 452.58]  Yeah.
[452.94 --> 453.68]  It's so wonderful.
[453.68 --> 454.16]  Yeah.
[454.16 --> 455.38]  It's definitely international.
[455.68 --> 460.26]  So that was excellent and really formative for my interest in R.
[460.36 --> 464.90]  I was interested in R kind of before that, but that really kind of solidified that this
[464.90 --> 470.38]  was a community that kind of in addition to being, you know, a language that offers the
[470.38 --> 474.96]  type of statistical tooling that I'm going to need, it also had that community aspect
[474.96 --> 479.72]  where there was a lot of support for learning and for developing and things like that.
[479.72 --> 484.78]  And so that kind of was some of what branched me into this interest in sort of data science
[484.78 --> 485.44]  more broadly.
[486.08 --> 490.08]  And then I went on to do a postdoc at Johns Hopkins and Jeff Leak's lab.
[490.20 --> 494.94]  And so my dissertation is very causal inference related and a big arm of what I do is still
[494.94 --> 495.70]  causal inference.
[496.14 --> 499.96]  But then through my postdoc, I added a bit on data science pedagogy.
[500.06 --> 505.00]  And so thinking about how to teach data science and how that can integrate in with kind of medical
[505.00 --> 506.24]  applications in particular.
[506.24 --> 511.06]  And so I worked on some of that and that sort of branched into this thinking about human
[511.06 --> 514.66]  data interaction problem, which is another big arm of my research right now, where we
[514.66 --> 519.88]  think about kind of how people interact with data and how they conduct data analyses and
[519.88 --> 525.50]  sort of how we can potentially think about interventions to nudge people towards conducting
[525.50 --> 529.06]  a correct data analysis as opposed to one that maybe would be incorrect in different ways,
[529.12 --> 534.40]  or maybe getting kind of alignment between stakeholders and producers of data analyses and things
[534.40 --> 534.80]  like that.
[534.80 --> 538.94]  And so this was all kind of what brought me into the more data science type space.
[539.52 --> 539.62]  Yeah.
[540.26 --> 547.90]  I think that human data interaction is, yeah, it seems to me to be like the really the tough
[547.90 --> 552.38]  problems that data scientists deal with kind of live at that boundary.
[552.62 --> 555.56]  With the tooling now, there's so much great tooling around.
[555.98 --> 562.26]  And it's fairly, I mean, of course, you know, you need some context and some background knowledge
[562.26 --> 564.46]  and some domain knowledge and all that to solve problems.
[564.46 --> 570.60]  But in tooling wise, it's fairly easy to actually create somewhat sophisticated systems.
[570.60 --> 578.06]  But that communication part and that interaction, the human data interaction, all is for not if
[578.06 --> 581.24]  that's not properly taken into account and managed.
[581.48 --> 581.84]  Right.
[581.84 --> 583.42]  It's such a big deal, too.
[583.52 --> 588.90]  As you were talking about that a moment ago, every single day in my job, I run into issues
[588.90 --> 592.30]  where there are challenges between how people are interacting with data and stuff.
[592.30 --> 596.44]  So I'm very excited to hear what you have to teach us in the minutes ahead.
[596.98 --> 597.20]  Yeah.
[597.44 --> 598.24]  No, it's a huge.
[598.24 --> 603.68]  It's kind of neat because it builds on, I think, the kind of foundation for this field
[603.68 --> 607.28]  of human data interaction, you know, it kind of builds on what people would talk about,
[607.50 --> 609.62]  you know, before they were talking about human computer interaction.
[609.62 --> 612.78]  And I feel like in some ways we've mastered that.
[612.92 --> 614.44]  In a lot of ways, there's still a lot to learn.
[614.54 --> 618.50]  But I think, you know, that was happening a lot when things like Apple were coming about
[618.50 --> 622.92]  and there is and Google and sort of thinking about how we can help people interact with computing
[622.92 --> 627.86]  systems to make it that they're, you know, for some people using a terminal is like a
[627.86 --> 628.76]  great way to interact.
[628.82 --> 631.44]  And I personally love interacting via a terminal.
[631.44 --> 636.06]  But to kind of get like the Internet and everything into the hands of the average consumer, someone
[636.06 --> 639.76]  had to figure out that, no, we need to have something that has pictures and words and people
[639.76 --> 644.14]  can click things and they don't have to be just sort of interacting via this text module.
[644.56 --> 650.10]  And so, you know, that really launched a huge revolution, I think, when we were able to bring
[650.10 --> 652.94]  what computing had to offer to the average person.
[652.94 --> 656.60]  And I think that this human data interaction is sort of the next step on that.
[656.64 --> 660.30]  So now we've got the computing and we know how to get that into the hands of people who,
[660.44 --> 664.66]  you know, maybe otherwise wouldn't have been able to implement these different things.
[664.66 --> 668.76]  But making sure that now that they can do it, that they're kind of doing it correctly,
[669.20 --> 674.48]  that they're interacting with the data the way that is going to get to kind of a result
[674.48 --> 680.04]  that is correct and also aligns with the incentives of everybody involved, I think, is really crucial.
[680.10 --> 687.46]  Yeah. And I think it's not only that's deeper sort of data interaction, but there's there's a lot of
[687.46 --> 695.08]  communication about data now in the media as well. And, you know, how people perceive that is
[695.08 --> 700.44]  very different depending on on who you talk to. So I know even in the last week, I think it's
[700.44 --> 707.12]  happened all in one week. There is like two or three companies that announced these sort of
[707.12 --> 712.14]  statistics about how good their COVID vaccines are going to be. So this happened, you know,
[712.14 --> 717.36]  like days ago or maybe it was even I forget if it was it this morning. The last one came out or
[717.36 --> 723.10]  yesterday or something yesterday. Yesterday. Yeah. Yeah. Yeah. 95, I think, was the thing they were
[723.10 --> 728.28]  throwing around in the news. Ninety five percent. Yeah. So I think one was ninety five percent. And
[728.28 --> 735.02]  the way it was communicated on the other one that I noticed was like 90 percent or higher or something
[735.02 --> 739.80]  like that. Ninety percent. Above ninety percent. OK, yeah. And just as a real clarification for
[739.80 --> 745.40]  listeners that we at the point where we're recording, we just heard the first two vaccine
[745.40 --> 750.62]  initial results and those and everyone's talking about that. So you're probably beyond us and you know
[750.62 --> 755.46]  more than we do by the time you hear this. Yeah. This is late November 2020. There you go. Yeah.
[755.46 --> 761.08]  When you hear that sort of communication come out, do you get the sense that people are
[761.08 --> 769.04]  consuming that in a way that they are understanding the implications of those types of numbers or what
[769.04 --> 773.32]  is your thought on that? Yeah. Oh, this is such a good question. And it actually like it bridges
[773.32 --> 779.80]  essentially all of my research interests. Perfect. Yeah. Because we're talking about to the Pfizer and
[779.80 --> 784.76]  Moderna, I think, are the two big ones that came out relatively recently. And these were both
[784.76 --> 788.48]  randomized controlled trials. And so obviously the question of interest is a causal question.
[788.76 --> 794.36]  It definitely covers my causal inference kind of framing. And then we also it covers the human
[794.36 --> 798.66]  data interaction and also communication of statistical kind of concepts. And so it bridges
[798.66 --> 803.32]  it really nicely. But one thing to mention in all of this, well, first, I think you said that it was
[803.32 --> 808.74]  95 percent for the for Moderna, which is what a lot of outlets are reporting. The actual interim
[808.74 --> 812.66]  analysis reported 94.5. And the thing that's interesting. Just round up.
[812.74 --> 817.36]  I know. Also, what's very interesting about this is that there's been, you know, just from a
[817.36 --> 821.76]  communication perspective, even that has been a little bit controversial because they're giving
[821.76 --> 827.46]  a sense of precision where there really isn't that kind of precision. So the number of participants in
[827.46 --> 833.60]  this trial that received the placebo that got sick, it was there were, I think there were 90 that
[833.60 --> 839.18]  received the placebo and five that received the treatment that ended up getting COVID. And so
[839.18 --> 845.68]  94.5 implies that there's this real precision, but we actually don't even have 100 participants that
[845.68 --> 851.04]  have reached that end point of getting. Right. It makes you think that there's like tens of thousands
[851.04 --> 857.64]  and they were able to get like really, really granular data. Right. Right. Yeah. And giving,
[857.78 --> 861.92]  I mean, I'm sure that there were, well, I shouldn't say I'm sure. I don't know. Maybe there wasn't
[861.92 --> 866.32]  someone that thought about if they said 94.5, that everyone would round up to 95 and then
[866.32 --> 871.68]  that this would sort of give some kind of sense of things that maybe wasn't exactly what was being
[871.68 --> 876.36]  represented by the data. And the other thing with these that's really challenging to make sure
[876.36 --> 881.84]  is well understood is that both in both cases, these are interim analyses. And so they're not the
[881.84 --> 887.08]  final result. And we wouldn't as, you know, as a statistician involved on data safety monitoring
[887.08 --> 891.60]  boards or these different groups that actually come out with these estimates. First of all,
[891.60 --> 897.60]  it's not common. I mean, in other circumstances, often interim analyses don't get the same kind of
[897.60 --> 902.30]  press that these are getting. I mean, sometimes they will get a press release and they will see
[902.30 --> 905.50]  a little bit of a market change, but only for people who are really, really paying attention.
[905.86 --> 909.42]  And of course, now it's very different because the whole world is paying attention. And so
[909.42 --> 915.28]  kind of how we communicate it has to be even more clear. But, you know, interim and it's not unusual to
[915.28 --> 920.88]  get a different result than an interim analysis as a final analysis. You know, certainly you would
[920.88 --> 926.26]  expect, especially in both cases, because they're closer to the kind of what their final endpoint
[926.26 --> 930.42]  is, then they're closer to that than they are far away. So this isn't like a first look. It's,
[930.42 --> 935.96]  you know, they're closer to what the final result likely will be. So probably it's going to be in the
[935.96 --> 941.14]  ballpark of what we're seeing, but it probably won't be exactly 94.5%, for example. It would be
[941.14 --> 947.46]  really surprising if it was. And some of the concern is when those kind of precise numbers are reported
[947.46 --> 952.68]  in the news. And then, you know, it comes out that, oh, in the end, it was 80% effective,
[952.68 --> 956.82]  which is actually really great. People kind of can start getting concerned.
[957.16 --> 963.20]  Yeah. And then they can kind of come up with a storyline of their own and one that maybe they're
[963.20 --> 968.12]  not comfortable with taking the vaccine for whatever reasons, because these people can't
[968.12 --> 973.72]  get their numbers right or, you know, whatever it is. Yeah. Which could cause actual health and
[973.72 --> 980.42]  safety issues? So having said all that, it raises kind of an ethical question in my mind, at least,
[980.58 --> 985.84]  to, you know, clearly this is done for, you know, kind of the marketing benefit. You know,
[985.86 --> 991.06]  the first one comes out, the second one gets out there to persuade the public. And yet, you know,
[991.06 --> 997.54]  as you just instructed us, it might reasonably fall to 80 hypothetically, but that does change the
[997.54 --> 1003.22]  way people are thinking about it. And so, you know, any thoughts on using data in that way? I mean,
[1003.22 --> 1006.82]  there's a certain amount of manipulation potentially involved in that.
[1007.24 --> 1011.70]  Yeah, for sure. And it's really challenging to know what the right thing to do is because,
[1012.12 --> 1017.00]  I mean, I think one thing that can certainly help, and I know some of the reporting that I've read has
[1017.00 --> 1021.64]  been, you know, they've been careful to include in their text. Like I was reading the New York Times
[1021.64 --> 1026.46]  piece on Moderna yesterday and, you know, they did include that this is an interim analysis and we
[1026.46 --> 1031.74]  expect these results to change. But unfortunately, and, you know, maybe to no fault of the author,
[1031.74 --> 1035.62]  but that ends up being like paragraph four. And, you know, the headline says something very
[1035.62 --> 1041.04]  different and people tend not to read past headlines. And so it's kind of hard to figure
[1041.04 --> 1045.82]  out the right balance of getting people to be able to consume this information because it is good to
[1045.82 --> 1048.74]  sort of have people see a light at the end of the tunnel. I think there's definitely a benefit.
[1048.76 --> 1049.86]  It's a need for optimism.
[1050.22 --> 1050.32]  Yeah.
[1050.42 --> 1054.80]  Yes. There's definitely a benefit to that. But then being able to balance it with the reality
[1054.80 --> 1060.22]  and kind of being able to articulate the uncertainty in such a way that when the numbers slightly change,
[1060.22 --> 1065.42]  it doesn't cause people to sort of lose trust. And I don't know the perfect answer to this. This has
[1065.42 --> 1070.44]  been something that my lab has been studying. I have a student that's been running a study that's
[1070.44 --> 1076.52]  been looking at kind of if we randomize people to see kind of health recommendations qualified with
[1076.52 --> 1081.68]  uncertainty versus ones that are sort of said definitively. When a follow-up recommendation
[1081.68 --> 1086.94]  is made that maybe reverses the previous one, but gives kind of the full context, are they more or less
[1086.94 --> 1092.68]  likely to trust it if they saw things with kind of the proper uncertainty the first time or kind of
[1092.68 --> 1097.30]  with just like a clear certain statement. And it turns out we're still in the process of analyzing
[1097.30 --> 1104.70]  this data, but it's challenging because the first result, when you just look at people randomized to
[1104.70 --> 1110.86]  seeing a certain versus kind of qualified recommendation, on average, people do tend to
[1110.86 --> 1115.60]  prefer the certain recommendation. Like they just want to be told what to do. They don't want to be told
[1115.60 --> 1122.16]  the like, you know, roundabout, this came from a small study and we aren't actually quite sure and this is
[1122.16 --> 1127.32]  the best that we know right now, but we're going to be taking in more information as it comes. And so if you
[1127.32 --> 1133.50]  knew for sure that the recommendation or the numbers wouldn't change, that actually is the easier way to go
[1133.50 --> 1138.36]  to get people to do kind of what would be in their best interest from a public health perspective. But of course,
[1138.40 --> 1142.66]  we don't know for sure if we only had a small study, we really don't know that that evidence isn't going to
[1142.66 --> 1147.84]  change. And so if you have to think about kind of hedging against that possibility and in the kind
[1147.84 --> 1151.88]  of secondary piece, if you've said something with certainty and then you turn back and say the
[1151.88 --> 1157.90]  opposite, the lack of public trust, I think, is a real potential to be lost in that and that can
[1157.90 --> 1163.42]  really be negative. And so sort of thinking about this in the long run as opposed to in the short run
[1163.42 --> 1165.22]  is also really important.
[1165.22 --> 1172.00]  So Lucy, I'm curious. We talked a little bit about these numbers that are thrown around and
[1172.00 --> 1178.44]  obviously coming from statistical analysis of some type. And what I was thinking in my mind was there
[1178.44 --> 1185.62]  have been those times in my data science career where I felt maybe a little bit uncomfortable with
[1185.62 --> 1192.12]  how some of the numbers that I've communicated kind of up the chain to stakeholders have been used.
[1192.12 --> 1198.44]  Like, you know, oh, maybe I have this new speech recognition model. And for this particular
[1198.44 --> 1206.78]  language, like it performs whatever, you know, 5% better than the Google one from and then, you know,
[1206.80 --> 1213.62]  up the chain, maybe it starts to be like used in marketing that like our speech recognition is 5%
[1213.62 --> 1219.04]  better than, you know, Google's version or, you know, there's situations where there's just like,
[1219.04 --> 1227.72]  I never intended for my work to be sort of taken in that way. Do you have any general
[1227.72 --> 1234.20]  recommendations for data scientists and statisticians and analysts in terms of how they
[1234.20 --> 1240.02]  deal with those interactions where you've done some analysis and now you're communicating to a
[1240.02 --> 1245.62]  different sort of audience and it's maybe going up the chain? Any recommendations or general principles
[1245.62 --> 1250.32]  that you think should be kept in mind in that type of situation? So we don't have to be hostage to the
[1250.32 --> 1257.04]  marketing machine? This is such a good question. And it's so hard because, you know, in your example,
[1257.50 --> 1261.44]  the marketing team is at least within your own company. So you have like kind of constant
[1261.44 --> 1266.60]  communication with them. And often, you know, what I see on the on the medical side, at least is like
[1266.60 --> 1271.98]  someone will publish something. And actually, there's a there are a lot of examples from this from early
[1271.98 --> 1276.78]  kind of COVID data where there were papers that were published in our very top medical journals that
[1276.78 --> 1281.82]  people, some of the reviewers missed things. And I think the scientific community came together and
[1281.82 --> 1286.86]  found them pretty quickly. And the articles were either updated or retracted. And it worked, but it
[1286.86 --> 1292.88]  worked on the scientific side. But the media ran with some of that. And, you know, the articles that ran
[1292.88 --> 1299.52]  headlines based on the original data often would get much more press than the updated ones, for example.
[1299.52 --> 1304.96]  So I think that this problem is not unique to kind of the setting where that you described,
[1305.06 --> 1309.00]  where you're trying to kind of help a marketing committee understand the numbers in such a way
[1309.00 --> 1312.72]  that they can market them accurately. But it also happens sometimes where it's like not even
[1312.72 --> 1317.70]  in your control in the sense that it's like someone outside, totally outside of your organization is
[1317.70 --> 1322.78]  the one kind of running with it. I have this talk that I've been working on for a while and
[1322.78 --> 1326.42]  have some aspirations of sticking it in like a short course or something. But
[1326.42 --> 1330.74]  basically, it's I think of statistical communication and probably just scientific
[1330.74 --> 1337.74]  communication in general, as on this kind of two by two grid, where you have like, you could imagine
[1337.74 --> 1345.10]  this like a x y axis where you have maybe on the y axis, whether or not something is true or not,
[1345.10 --> 1349.28]  and on the x axis, whether it's interesting or not. And so you have this quadrant of like,
[1349.50 --> 1354.40]  interesting and true, which is kind of where we want all of our communication to be. So something that
[1354.40 --> 1361.16]  kind of is interesting to the marketing folks, but also conveys the actual truth. And kind of next
[1361.16 --> 1366.12]  to that, you have a quadrant that is not true, but still interesting, which sort of falls into what
[1366.12 --> 1372.52]  you were describing, where you, you saw that there was a 5% improvement in your speech recognition
[1372.52 --> 1377.14]  versus this other one in this one specific case. And the marketing committee kind of ran with it and
[1377.14 --> 1383.28]  sort of implied that that was, but exactly, generalized it beyond it. Anyway, so the kind of picture that I try
[1383.28 --> 1387.78]  to paint is moving from interesting to, or from not interesting to interesting is one kind of
[1387.78 --> 1392.18]  dimension that we want to move across. But then the other one that sort of describes what you're
[1392.18 --> 1397.22]  talking about is moving from not true to true and sort of what are the pieces there. And so the ones
[1397.22 --> 1404.40]  that I've sort of defined as on this like journey to truth would be that it has to be mathematically
[1404.40 --> 1408.58]  correct, marketed correctly, disseminated correctly, and the audience has to interpret it correctly.
[1408.58 --> 1414.30]  And so those are kind of the four main pieces that I think determine whether or not it's true.
[1414.38 --> 1419.36]  So that one that you just said there fits in my second category of being marketed correctly.
[1419.64 --> 1423.80]  And I guess from my perspective, even just naming that these are the things that need to happen
[1423.80 --> 1428.38]  with statistical communication is moving us forward because I think that I haven't answered your
[1428.38 --> 1432.90]  question on how to get people to market it correctly, but I've at least named that these are things that can
[1432.90 --> 1437.42]  go wrong when you're trying to communicate statistics. And I feel like that's potentially a step in the
[1437.42 --> 1442.90]  right direction is just knowing that that could happen. And so being cognizant that even if the
[1442.90 --> 1447.78]  thing that you do is statistically correct, you need to make sure when you're passing it on to people
[1447.78 --> 1452.48]  and when you yourself are marketing it, that you're marketing it kind of in the right way.
[1452.90 --> 1457.78]  Will you take a second and rename those four things? Because you started down and I got caught
[1457.78 --> 1461.30]  on the mathematical and I missed the other three. So I want to do that.
[1461.40 --> 1463.08]  Chris is always stuck in the math.
[1463.08 --> 1468.46]  I constantly, it's terrible. And then I also wanted to see, I actually want to like follow
[1468.46 --> 1473.44]  up on Dan's thing because I know you're going to do it anyway, but can you take your grid and
[1473.44 --> 1478.30]  kind of give us an example of how to use it? Because selfishly when we are done recording
[1478.30 --> 1482.36]  this podcast and this is going to go out for release, I want to use this as a tool myself.
[1482.84 --> 1484.24]  So you've just given me hope.
[1484.64 --> 1485.04]  Yes.
[1485.30 --> 1490.04]  So can you kind of walk us through like how you would use the tool itself, what the four
[1490.04 --> 1494.08]  principles are and then like how we can use it day to day. So someone can listen to this
[1494.08 --> 1498.20]  and then they can go off and actually use it because I have the same set of issues. I work
[1498.20 --> 1502.72]  for a big company and there's lots of different audiences and they may use information in all
[1502.72 --> 1505.62]  sorts of different ways like any other company. So I am all ears.
[1506.16 --> 1511.82]  Yes. Okay. So, so the four that I had mentioned are that it's mathematically correct, that it's
[1511.82 --> 1517.66]  marketed correctly so that you have kind of given the correct marketing, that it's disseminated
[1517.66 --> 1523.70]  correctly. And so that's slightly different than the marketing. So you could sort of yourself
[1523.70 --> 1528.22]  market it correctly, but then the way that it gets kind of disseminated after you've provided
[1528.22 --> 1529.12]  that marketing could be.
[1529.12 --> 1531.38]  Kind of delivery outward, you know, the mechanism.
[1531.62 --> 1531.76]  Okay.
[1532.02 --> 1536.32]  Yeah, exactly. And then the third part or the fourth part rather, which I think this is one
[1536.32 --> 1542.00]  of the hardest parts is that the audience interprets it correctly. And the example that I like to
[1542.00 --> 1547.12]  give for that is that, you know, just because you've done all these other parts, right? If your audience
[1547.12 --> 1552.58]  misinterprets your result, then maybe you really need to be thinking about communicating it
[1552.58 --> 1558.26]  differently, even if you've actually communicated it in a correct way. And so somewhat relevant
[1558.26 --> 1563.62]  example for that, that made some rounds, you know, it's hard to know. I think I'm in an insular
[1563.62 --> 1567.00]  Twitter sphere, so it's hard to know how much this made outside of my world.
[1567.00 --> 1573.66]  Yes. But in my world, this made kind of a splash that back a while ago, back in July,
[1573.66 --> 1578.88]  there was a dashboard that was going around from Georgia where they plotted these figures,
[1578.88 --> 1582.06]  it was a map of the cases per 100,000 people.
[1582.28 --> 1585.84]  Yeah, I'm in Georgia. Trust me, that impacted us in a bit. That was what we were talking about.
[1585.94 --> 1590.72]  Okay. So it's not just my Twitter story. This is good to know. And so the intention behind this map
[1590.72 --> 1596.70]  was it was looking at kind of which counties relative to the others are the worst. So that's
[1596.70 --> 1601.14]  what this map was trying to do is one of these maps that had, you know, it highlighted basically the
[1601.14 --> 1606.76]  ones that were in the top percentile. But how audiences were using this, a lot of people were
[1606.76 --> 1612.32]  visiting this site every day and taking a screenshot of this map, and they were comparing this over time.
[1612.44 --> 1617.50]  And this particular visualization is really not meant to be compared over time because the bins
[1617.50 --> 1622.46]  are going to change every time because they're percentiles, they're quantiles. And so those bins
[1622.46 --> 1627.96]  are calculated relative to all the other ones. And so they're not telling, this map doesn't tell you
[1627.96 --> 1633.70]  if things are getting worse overall in the state, it just tells you basically which counties are getting
[1633.70 --> 1638.76]  worse or better by these different. And when I first saw this, people were a little bit outraged
[1638.76 --> 1644.20]  because they were like, look, they've changed the bins. And so, you know, in the past two months,
[1644.20 --> 1648.26]  it looks like we're the same, but we're actually way worse, even though these two plots look the same.
[1648.56 --> 1652.62]  And when I first saw this, I'm like, yeah, but the people that made those maps did the right thing.
[1652.94 --> 1657.32]  That's how you make those maps. How could you possibly guess what bins to use two months in the future?
[1657.32 --> 1661.54]  Or, you know, how could you guess how many cases there might be so that you could set the colors,
[1661.78 --> 1665.98]  you know, in the past based on what you might see in the future so that you could be showing
[1665.98 --> 1672.90]  this graph over time unless you retrospectively did it? How could anybody do that? But the fact that
[1672.90 --> 1678.28]  so many people, the way they were consuming this information was via looking at this once a day,
[1678.36 --> 1683.26]  taking a screenshot and comparing over time, you know, that was an important piece of information.
[1683.26 --> 1688.04]  Yeah. Would it be fair to say it wasn't being interpreted correctly because
[1688.04 --> 1694.86]  it wasn't being disseminated with enough communication of how it should be consumed
[1694.86 --> 1698.16]  to ensure that interpretation was occurring correctly?
[1698.16 --> 1704.66]  Exactly. Yeah. And I think that the solution here as an analyst is that either you need to
[1704.66 --> 1708.82]  very explicitly say these maps are not meant to be looked at over time in, you know, somewhere
[1708.82 --> 1714.18]  where it's like in the screenshot that will end up on the screen. There was also a problem with if
[1714.18 --> 1718.18]  you were viewing it on mobile or a desktop, if it was on a desktop, it was a little bit clearer that
[1718.18 --> 1722.08]  these weren't meant to be viewed over time. If you're viewing on mobile, there was a line that said
[1722.08 --> 1727.22]  you can look at things over time that was corresponding to a different plot that ends up not being in view on
[1727.22 --> 1732.74]  mobile. So there were other pieces communication wise that made this challenging. But what I saw from
[1732.74 --> 1737.38]  this was that either you need to make that explicit or you need to just take away this map and use a
[1737.38 --> 1743.44]  different form of trying to show this result because people are going to be doing what they're doing.
[1743.54 --> 1749.04]  I mean, people are going to consume information as they consume it. And, you know, I think it's outside
[1749.04 --> 1752.82]  of Georgia. I've heard from lots of people that the way that they've been consuming information from
[1752.82 --> 1758.00]  like the Johns Hopkins maps and things that they take screenshots and record this over time because
[1758.00 --> 1761.54]  there's some kind of fear that we're going to lose information. And so they need to be holding it.
[1761.90 --> 1767.38]  And so this is like it's sort of a sociological kind of study. But just looking at this is how
[1767.38 --> 1771.02]  people are consuming this information that we're putting out. And it's not necessarily how the people
[1771.02 --> 1774.32]  who are putting out the information would have consumed it themselves. But they need to recognize
[1774.32 --> 1778.68]  that if the masses are consuming it like this, we need to be adjusting because the whole point of
[1778.68 --> 1783.98]  putting out these dashboards is to make them consumable. So yeah. So we totally need to get
[1783.98 --> 1789.64]  you on a consulting job as a side gig for the Georgia Department of Public Health, because we
[1789.64 --> 1796.16]  have 12 million Georgians who are we're in our doubting that. So we just need you there. We can fix Georgia.
[1796.56 --> 1801.10]  I know it's so it's a hard problem. I think it's not just Georgia. Get ready to come down here.
[1801.10 --> 1803.44]  I'm not too far in North Carolina. So there you go.
[1803.44 --> 1810.30]  It is interesting what you said about like people don't trust that they'll be able to like they think
[1810.30 --> 1813.86]  that they're going to lose this data or something or they're going to lose this information.
[1814.66 --> 1821.40]  It's like this thing was generated by some experts somewhere. And who knows how long this website's
[1821.40 --> 1826.60]  going to be around or whatever. So I want to they're basically trying to do some data gathering
[1826.60 --> 1834.78]  of their own and come up with their own sort of self service, you know, data dashboard or something
[1834.78 --> 1842.28]  that they think that they need. Yeah. I mean, that's a really interesting psychological thing.
[1842.54 --> 1847.52]  I don't know what the solution to that is in terms of giving people more trust that they'll have access
[1847.52 --> 1853.66]  to things if it's like giving people the ability to, you know, self serve themselves data more more
[1853.66 --> 1859.12]  frequently or I don't know. So it's funny. I just know that in this particular example that we're
[1859.12 --> 1865.64]  discussing, that has happened that that lack of trust has happened where like lots of local media
[1865.64 --> 1872.10]  stations and other organizations in Georgia have been pulling data from like John Hopkins because they
[1872.10 --> 1877.24]  weren't trusting the Georgia data and doing a whole bunch of graphing instead of pointing people at the
[1877.24 --> 1882.20]  institution that's supposed to be doing that, you know, there have been a whole bunch of surrogates out
[1882.20 --> 1887.66]  there. So it's been interesting to see how trust affects that in a pretty, pretty big way.
[1888.34 --> 1892.74]  Yeah. Well, and I know, I mean, I I'm not sure about in Georgia, but I know in other states,
[1892.74 --> 1897.00]  there have been cases where things were on a dashboard one day and then they were not made
[1897.00 --> 1901.38]  available the next day. And obviously here that kind of, yeah, so I guess that's what happened there
[1901.38 --> 1906.32]  too. And so I think that that kind of thing happening also can make the trust kind of that can
[1906.32 --> 1908.14]  erode it a little bit too.
[1917.86 --> 1924.74]  Change log plus plus is the best way for you to directly support practical AI. Join today and
[1924.74 --> 1930.86]  unlock access to a private feed that makes the ads disappear, gets you closer to the metal and help
[1930.86 --> 1937.70]  sustain our production of practical AI into the future. Simply follow the change log plus plus link
[1937.70 --> 1943.96]  in your show notes or point your favorite web browser to change log.com slash plus plus. Once
[1943.96 --> 1947.44]  again, that's change log.com slash plus plus.
[1947.44 --> 1951.18]  Change log plus plus. It's better.
[1960.80 --> 1973.94]  All right. So we, we started talking into these, these COVID related numbers with the,
[1973.94 --> 1979.40]  the vaccines and then also talked a lot about data communication, all of that super useful.
[1979.98 --> 1985.02]  But I do want to get a chance to talk a little bit more about that kind of third piece that you
[1985.02 --> 1990.90]  mentioned was mixed into that original problem we talked about of the vaccine numbers, which was
[1990.90 --> 1996.52]  causal inference. And I know that at the upcoming our conference, this is the first our conference
[1996.52 --> 2001.64]  that's going to be focused on government and public sector, which is super exciting. Chris and I are
[2001.64 --> 2006.86]  going to moderate a panel there, which will be a lot of fun for us to join, but you're giving a
[2006.86 --> 2012.96]  workshop there on causal inference. Of course, that name has also inspired your, your podcast. And I
[2012.96 --> 2018.50]  see that sprinkled around throughout, you know, your, your web presence. So could you just give us a
[2018.50 --> 2026.38]  little bit of context for what causal inference means, why it's different than some of the other types of
[2026.38 --> 2031.94]  inference or prediction that we might perform as data scientists? I'd love to hear that. Cause I
[2031.94 --> 2037.22]  definitely think that we have not had that specific conversation on this podcast as of yet.
[2037.58 --> 2042.30]  Yeah. Great. I love talking about causal inference. So the, the big picture with causal inference,
[2042.38 --> 2045.84]  essentially it's exactly as it sounds, I guess I'm going to use the word and the definition,
[2046.00 --> 2049.68]  which I know you're not supposed to do, but if you're trying to answer a causal question, so does
[2049.68 --> 2054.02]  something cause something else, which often most of the questions we're interested in
[2054.02 --> 2058.24]  are in that framework. Although it is distinct from something like prediction, which would be a
[2058.24 --> 2062.62]  different kind of space. But in the inference space, when we're trying to determine the relationship
[2062.62 --> 2070.14]  between different factors or different variables, a lot of times we talk about associations as a way
[2070.14 --> 2074.58]  to sort of describe relationships that we know maybe are correlated, but we don't want to go as far
[2074.58 --> 2080.50]  as to say they're causal. But I would argue in most cases, the kind of human instinct is to want to
[2080.50 --> 2085.34]  talk about things causally. That's most of the time when we're studying relationships between
[2085.34 --> 2090.20]  variables, it's often because we want to know if there's a causal connection. So, you know,
[2090.30 --> 2095.20]  in randomized trials, like the ones that we're talking about with Pfizer and Moderna, looking at
[2095.20 --> 2100.16]  different vaccines, they're not just interested in whether or not getting a vaccine is somehow
[2100.16 --> 2104.44]  related to whether or not you get COVID. They want to know if getting the vaccine will actually
[2104.44 --> 2110.42]  cause you to, to not get COVID. So this is sort of the relationship that we are focused on
[2110.42 --> 2116.78]  in causal inference. And so randomized trials kind of often are the, what people think of as the
[2116.78 --> 2122.28]  gold standard, although there are several ways that causal estimates can get skewed or biased in a
[2122.28 --> 2128.00]  randomized trial as well. So there are ways that you can actually need to do some more sophisticated
[2128.00 --> 2133.60]  analyses to get at a causal effect even in the randomized setting. But then where my work mostly is,
[2133.60 --> 2138.64]  is more in observational data where we don't have a formal randomized trial. We're just sort of
[2138.64 --> 2143.66]  observing things, for example, in electronic health records, or you can think of all different types
[2143.66 --> 2148.22]  of data sets that have already been collected, but you want to try to determine if there's some kind
[2148.22 --> 2155.48]  of causal effect between different elements. And so to do so, you kind of have to build this framework
[2155.48 --> 2161.68]  that involves both kind of statistical modeling, but then also a lot of assumptions. And so a lot of times,
[2161.78 --> 2166.90]  like the way that we build these kind of causal, we build up this causality is being able to
[2166.90 --> 2172.06]  kind of state assumptions about our data that we're making. And should these assumptions be true,
[2172.06 --> 2176.70]  then we can assume that the effect that we're seeing is actually a causal effect and not just
[2176.70 --> 2181.38]  kind of an association between two things. Does that kind of answer your broad question about causal
[2181.38 --> 2188.30]  inference? Yeah, yeah, it definitely does. It's very useful because I do think that it is the natural
[2188.30 --> 2196.76]  human reaction when we're doing any sort of modeling to assume like if these features that are fed
[2196.76 --> 2204.40]  into our model allow us to predict, you know, whatever it is, Y1, Y2, whatever those things out,
[2204.48 --> 2211.84]  then those things are somehow causing that response or those labels or whatever it is. It's a very natural
[2211.84 --> 2218.92]  reaction to think that. One of the things I'm curious about is, so you mentioned this sort of process of
[2218.92 --> 2226.36]  defining your assumptions, being very careful about how you do that. I'm sure there's a number of
[2226.36 --> 2233.26]  things, but what are some of the kind of common tools that people use in causal inference that
[2233.26 --> 2240.36]  maybe are, are there kind of gold standard tools or very common tools that people use in this case?
[2240.80 --> 2244.98]  Yeah, so there's a lot of kind of underlying assumptions and there's ways that people try to
[2244.98 --> 2251.22]  kind of help get at them. So my work uses something often called propensity scores. And so
[2251.22 --> 2256.10]  what that basically means it's in the kind of observational setting where we don't have
[2256.10 --> 2262.84]  a randomization to an exposure to some treatment. And so you try to kind of construct what we call a
[2262.84 --> 2269.18]  counterfactual framework. Like all I know is that you got, for example, if I'm looking at diabetes,
[2269.18 --> 2274.58]  drugs, and heart disease, all I know is that you received diabetes drug X. And I don't know what
[2274.58 --> 2279.52]  would have happened if you had received diabetes drug Y, for example, but I could try to construct what I
[2279.52 --> 2285.32]  think may have happened. And so I could basically look at all of the different baseline characteristics.
[2285.32 --> 2292.62]  I could adjust for all of those and then kind of adjust for other people who have the same baseline
[2292.62 --> 2297.46]  characteristics you could imagine on the other drug and sort of assume that those two, if you were to
[2297.46 --> 2302.56]  measure all potential characteristics, so there's nothing unmeasured that might be confounded, then you
[2302.56 --> 2307.16]  could compare those two kind of groups or maybe those two groups on average to each other to sort of
[2307.16 --> 2311.82]  be able to build that counterfactual that we couldn't actually observe. And so in the randomized
[2311.82 --> 2316.30]  setting, because we're randomly assigning you to one or the other, the counterfactual is much easier
[2316.30 --> 2321.70]  to deal with because we assume that all of those baseline characteristics kind of on average are
[2321.70 --> 2328.08]  going to end up being just, they're going to be balanced because we end up kind of randomly assigning
[2328.08 --> 2334.08]  to one group or another. But in the observational space, you don't have that luxury. So actually kind of
[2334.08 --> 2338.26]  constructing something that can help you achieve that balance between the two via something like
[2338.26 --> 2344.78]  propensity score is the tool that I use most often. And that's essentially, it's just a summary score of
[2344.78 --> 2350.26]  your baseline characteristics to, and so you essentially are estimating the propensity that
[2350.26 --> 2354.44]  you would get one treatment versus the other. And then you can use that as an adjustment tool in
[2354.44 --> 2359.88]  various ways, like weighting or matching to be able to get comparable groups. And then once you have
[2359.88 --> 2363.48]  comparable groups, then you can start making some more causal assumptions. But of course,
[2363.88 --> 2369.00]  the big piece here is that there's, you can't have anything unmeasured, which in a randomized setting,
[2369.00 --> 2373.66]  you're less worried about because we assume that things are going to kind of be balanced in the long
[2373.66 --> 2378.88]  run. And in observational setting, you have to either feel very certain you don't have anything
[2378.88 --> 2383.90]  unmeasured or do some sensitivity analyses to see kind of how bad things would be if you were missing
[2383.90 --> 2391.32]  an important variable. Where do most people go wrong with this? Maybe they don't, aren't thinking
[2391.32 --> 2395.92]  explicitly enough about it. They might be an experienced data scientist, but aren't really
[2395.92 --> 2400.96]  focused on, you know, like implementing a counterfactual framework that's not part of their
[2400.96 --> 2406.44]  thinking. Where do you see people go wrong where it kind of takes that process off the rails a little
[2406.44 --> 2414.26]  bit? I think the first place where people kind of, it depends because people kind of of all levels of
[2414.26 --> 2418.22]  experience go wrong on this. And so it's not even just beginners, but I think that the folks on the
[2418.22 --> 2422.72]  beginner side, it tends to be this unmeasured confounding piece and thinking about the plausibility
[2422.72 --> 2428.28]  of it. I think it's really easy to do kind of a sophisticated analysis that adjusts for many things
[2428.28 --> 2433.30]  and assume that you're really capturing all of the variability. And you see this a lot with
[2433.30 --> 2438.44]  electronic health records or that's where, because I do biased statistics, that's kind of the data
[2438.44 --> 2443.46]  source that I tend to be thinking about. But, you know, you've got tons of information in electronic
[2443.46 --> 2447.48]  health records, but that doesn't mean you have everything that's important. And it also doesn't
[2447.48 --> 2451.02]  mean that you're going to end up with an unbiased result. And so I think that there can sometimes be
[2451.02 --> 2456.10]  confusion between I adjusted for lots and lots and lots of things and I have everything that's
[2456.10 --> 2463.22]  important. Like those are two kind of potentially distinct pieces of information. So the example that
[2463.22 --> 2468.38]  we talk about in healthcare a lot is for a long time, there were studies that looked at hormone
[2468.38 --> 2473.98]  replacement therapy and heart disease. And people, it used to be recommended that hormone replacement
[2473.98 --> 2478.00]  therapy was actually protective against heart disease. And this was based on several large
[2478.00 --> 2483.44]  observational studies that were all kind of conducted around the same time and that did adjust for
[2483.44 --> 2487.60]  several things. And they were seeing kind of these consistent results. And so you could do a meta
[2487.60 --> 2491.70]  analysis across all of these studies and they all were sort of showing that it looked like it was
[2491.70 --> 2496.26]  probably protective. And then a randomized trial came about and it showed that it wasn't really
[2496.26 --> 2500.60]  protective. And in fact, there was a chance it could have even been harmful. And so this sort of
[2500.60 --> 2506.12]  threw a bit of a wrench in things and more studies were done. And it turned out there's some nice plots
[2506.12 --> 2510.58]  that you can sort of look at for this, but the observational studies that adjusted for socioeconomic
[2510.58 --> 2515.76]  status were showing null effects or even potentially harmful effects. And the ones that didn't were showing
[2515.76 --> 2521.36]  protective effects. And so essentially the whole effect of, or the large part of the effect of this
[2521.36 --> 2525.28]  hormone replacement therapy on heart disease that was being thought to be protective was mostly
[2525.28 --> 2529.70]  driven by socioeconomic status, which just wasn't adjusted for in these original models. So while
[2529.70 --> 2533.72]  they adjusted for other things, they didn't adjust for that important variable. And it turned out that
[2533.72 --> 2539.44]  was actually a huge driver. So women who had access to kind of, they were from kind of higher socioeconomic
[2539.44 --> 2544.32]  categories, they had access to different healthcare. And so they were less likely to get heart attacks or
[2544.32 --> 2549.34]  have these cardiovascular events that it didn't have anything to do with the hormone replacement therapy
[2549.34 --> 2554.86]  itself. And so sort of this, I think that type of example is what the first, you know, relying on
[2554.86 --> 2559.70]  previous knowledge in an area doesn't always save you from this unmeasured confounder piece. And I think
[2559.70 --> 2565.48]  that people who are first new to a kind of discipline, your default might be, okay, well, everybody that's
[2565.48 --> 2570.54]  fit this model before has included these variables and this is what we do. And it looks like we're getting
[2570.54 --> 2576.34]  the same kind of effect that people see. So it must be right. And I think that's kind of not always the case.
[2576.34 --> 2579.28]  I like the term for that too. Unmeasured confounder.
[2579.52 --> 2581.50]  Yes. Unmeasured confounder. I know.
[2582.04 --> 2585.62]  That'd be a good podcast name if anyone else is wanting to start it.
[2586.18 --> 2589.72]  That's what I'm going to be next Halloween. I'm going to be an unmeasured confounder for Halloween.
[2589.88 --> 2594.66]  Yeah, that would be a great Halloween. Yeah. It'd be a good one. On that note, not the Halloween
[2594.66 --> 2600.90]  costume, but the confounder note. I'm curious. I could see myself getting into a state where I'm like,
[2600.90 --> 2608.88]  I'm a little bit gun shy in the sense of like, oh, I'm like in this situation. I'm trying to do
[2608.88 --> 2617.74]  some causal inference, but I'm like, how do I know when I've, you know, I could see myself always
[2617.74 --> 2621.44]  thinking there's going to be another confounder out there. How do I know when I'm ready to pull
[2621.44 --> 2627.30]  the trigger and like actually give some results to someone? There's so many different, you know,
[2627.30 --> 2631.78]  things at play in here in this situation. And I'm just, you know, I think I've accounted for
[2631.78 --> 2635.66]  everything, but I don't know if I've accounted for everything. How do I know when I've accounted
[2635.66 --> 2640.92]  for everything or at least enough things to where I can have some confidence? You have any thoughts
[2640.92 --> 2646.80]  there? Yeah, it's a great question. And unfortunately there's not like a test or something for have you
[2646.80 --> 2650.18]  accounted for all the things, you know, unmeasured confounding is one that's specifically
[2650.18 --> 2655.78]  onerous because there's not a way to know for sure. One of my dissertation papers was on
[2655.78 --> 2659.94]  building tipping point sensitivity analyses for unmeasured confounding. And so the idea
[2659.94 --> 2665.42]  is that you can do your analysis and you do the best you can. You state the assumptions that you're
[2665.42 --> 2670.90]  making. And then at the end, you can do one of these tipping point analyses that we basically show
[2670.90 --> 2675.42]  mathematically. It's pretty simple formulation. There's an R package called tipper that can do it
[2675.42 --> 2681.22]  for you. But essentially what it will do is it'll take your effect that you're assuming to be causal,
[2681.22 --> 2685.38]  and it'll tell you the size of an unmeasured confounder that would be needed to tip that analysis.
[2685.78 --> 2690.10]  And so I think that that's kind of the best case scenario for what you can do. If you've done all
[2690.10 --> 2694.82]  that you can to account for what you have, then you can just explicitly state that, you know,
[2694.88 --> 2699.16]  we think that this effect, we feel like we've done what we can. These are the assumptions that we've
[2699.16 --> 2704.50]  made. If there were an unmeasured confounder out there like this that, you know, was related to the
[2704.50 --> 2709.68]  exposure and outcome in this manner, it would make our result no longer significant. It would make it,
[2709.74 --> 2715.72]  it would nullify our result or make it inconclusive. And so I think that's kind of the best that people can do
[2715.72 --> 2720.20]  and I think just doing that would really move the field forward in a lot of ways. You know, one thing
[2720.20 --> 2726.04]  that that can do is once that's been stated explicitly kind of in a paper or write-up or
[2726.04 --> 2730.46]  whatever it is that you're doing about this causal estimate that you're working on, then content matter
[2730.46 --> 2736.64]  experts that come in, you know, from all different areas can see that. And some may say, hey, that
[2736.64 --> 2741.90]  actually is plausible because I actually have seen that this particular variable that you didn't account
[2741.90 --> 2747.98]  for can have that kind of impact on your exposure or have that impact on your outcome that really
[2747.98 --> 2754.36]  would tip your analysis. And so sort of doing that work for them where they can see what a confounder
[2754.36 --> 2758.30]  like that would need to look like and then they could sort of map that back to their own content
[2758.30 --> 2765.42]  expertise I think is what can help with this. And so that's my best recommendation on that,
[2765.56 --> 2766.28]  friend. It's very helpful.
[2766.28 --> 2772.36]  That's pretty good. Excellent. So I guess as we wind up, what are things that you're excited about?
[2772.50 --> 2776.36]  You know, it could be an R, it could be about causal inference, it could be trends that you're seeing.
[2776.76 --> 2781.60]  What are the things that you're looking forward to doing over the next couple of years versus the
[2781.60 --> 2782.84]  stuff that you have been working on?
[2783.46 --> 2785.12]  Let's see, I'm excited about so many things.
[2785.90 --> 2787.96]  That's fine. Let's hear it. Go for it.
[2788.50 --> 2793.22]  I think, well, so I think on the causal side, I'm excited that this has been getting a lot of
[2793.22 --> 2797.66]  attention recently. I think that we had Roger Pang, he hosts a podcast called Not So Standard
[2797.66 --> 2802.04]  Deviations with Hillary Parker. He also hosts one called The Alpha Report with Elizabeth Matsui. And
[2802.04 --> 2806.24]  I had him on our podcast a little bit ago to kind of talking about his thoughts on causal inference.
[2806.34 --> 2810.16]  And he talked about how he sort of, at one point he had implied that maybe it's a fad, but
[2810.16 --> 2813.96]  essentially that like people are interested in this. And I think that it's true. I think that it's
[2813.96 --> 2818.40]  something that people are gaining more and more interest in, in terms of understanding the methods,
[2818.40 --> 2821.66]  as opposed to just trying to make causal claims. I think people,
[2821.66 --> 2825.60]  like as we've discussed, human instinct is to want to make causal claims. And so that's something
[2825.60 --> 2830.08]  that people have always been interested in, but the interest in sort of incorporating the more
[2830.08 --> 2834.78]  rigorous methods has been going up. So I'm really excited for that to continue. I think in that
[2834.78 --> 2840.62]  space, I think we're starting to see a better and better kind of introductory level information on
[2840.62 --> 2846.42]  how to conduct causal type analyses. And I think the gap still is sort of in that intermediate spot.
[2846.42 --> 2851.08]  I think that we have lots of people who are very competent on the heavy, heavy methods and lots of
[2851.08 --> 2855.40]  people who are working on the introductory. And I think we've got this nice middle spot that has
[2855.40 --> 2859.84]  a lot to be left to be contributed. So I'm excited about that because I think that there's potential
[2859.84 --> 2864.46]  there. And then kind of going back to the science communication piece that we were talking about
[2864.46 --> 2870.32]  before, I'm also excited. I think that a lot of the scientific process has been brought to the
[2870.32 --> 2876.22]  forefront and with just the pandemic response and sort of thinking about how this was done and how it
[2876.22 --> 2882.82]  was communicated. And so I think that we have a lot of data and information now on kind of how people
[2882.82 --> 2886.86]  have tried to communicate things and where that has potentially failed or maybe where it succeeded.
[2887.42 --> 2893.36]  And so I think going forward, we have a good horizon for being able to sort of improve on how we're
[2893.36 --> 2898.10]  communicating results, which I think is only going to be something that's better for everyone,
[2898.26 --> 2903.02]  both on the scientist side and on the general public side. So those are two things I'm excited about.
[2903.02 --> 2907.24]  Could probably come up with others. It was good. You've made me definitely excited about those
[2907.24 --> 2914.22]  things as well. And if our listeners are, I'm sure they are also excited about causal inference and
[2914.22 --> 2919.96]  these things that we've talked about, I would encourage you very much to check out the upcoming
[2919.96 --> 2929.06]  R conference. You can go to rstats.ai.gov and find out all of the info there. Lucy's giving a
[2929.06 --> 2935.08]  workshop there on causal inference. So it's a really great opportunity to dig deeper than we can during
[2935.08 --> 2941.34]  this period on the subject. The conference is December 2nd through the 4th. The workshops are
[2941.34 --> 2947.92]  on the 2nd and the conference is December 3rd through the 4th. And our listeners have a special
[2947.92 --> 2956.72]  discount code. So make sure you use PracticalAI 20 is the discount code, PracticalAI 20. And you'll get 20%
[2956.72 --> 2963.18]  off all of the ticket types, including the workshop that Lucy's giving. So make sure and check that out.
[2963.26 --> 2968.06]  Chris and I will be there as well, moderating a panel. So it's going to be a great time. I would
[2968.06 --> 2974.20]  encourage everyone that our community is so welcoming and awesome. And I really encourage people to check
[2974.20 --> 2980.82]  that out and hopefully see Lucy and both of us there. Thank you so much, Lucy, for joining. It's been a
[2980.82 --> 2984.80]  pleasure. Yes, thank you. It's been great. I'm so excited that you mentioned that workshop.
[2984.80 --> 2990.22]  The propensity scores that we talked about, you'll learn how to fit those types of models. You'll
[2990.22 --> 2993.68]  also learn about counterfactuals and things. And so exactly the methods that we talked about today,
[2993.74 --> 2996.92]  you'll be able to actually implement from the comfort of your R consoles.
[2997.68 --> 3004.64]  Awesome. That's so perfect. Yeah, great timing. It was great timing, this discussion, because
[3004.64 --> 3010.84]  those numbers came out just then for the vaccines just a couple of days ago. And then we've got the
[3010.84 --> 3016.96]  R conference coming up and people can just follow this whole story arc and get get trained up in
[3016.96 --> 3022.34]  causal inference and go do all of these exciting things that we talked about. So thank you so much,
[3022.40 --> 3024.00]  Lucy. Thanks for having me.
[3028.26 --> 3034.56]  Come hang out with Daniel, Chris and hundreds of other AI practitioners in our community slack.
[3034.56 --> 3039.90]  It's a cool place to be not a lot of noise, some great signal and best of all, it's totally free.
[3040.28 --> 3045.56]  Check it out at changelog.com slash community. And don't forget to follow the show on Twitter for AI
[3045.56 --> 3051.28]  news and links, highlights from past episodes and more. We are at practical AI FM. We'd love to have
[3051.28 --> 3056.58]  you following along. Thanks to Daniel and Chris for hosting practical AI weekend and week out to the
[3056.58 --> 3061.80]  mysterious Breakmaster Cylinder for the excellent beats you hear on all changelog podcasts to our sponsors
[3061.80 --> 3067.40]  who have our back Fastly, Linode and LaunchDarkly. And to you for listening. We appreciate your time
[3067.40 --> 3073.20]  and attention. That's all for now. On the next episode, the guys chat with the team at Unsplash
[3073.20 --> 3078.00]  all about their huge open data release. So stay tuned for that one next week.
