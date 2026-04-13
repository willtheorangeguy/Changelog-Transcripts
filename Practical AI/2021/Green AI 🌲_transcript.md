[0.00 --> 3.72]  We're researchers. We mostly communicate with the research community, but I mean,
[3.72 --> 8.22]  there's stuff to be done everywhere. Thinking about efficiency, you don't have to persuade
[8.22 --> 13.88]  anybody that if all other things being equal, if your tool runs twice as fast or takes half
[13.88 --> 20.22]  the amount of memory, everybody wins. BAM with for change log is provided by Fastly.
[20.52 --> 25.70]  Learn more at Fastly.com. Our feature flags are powered by LaunchDarkly. Check them out
[25.70 --> 31.28]  at LaunchDarkly.com. And we're hosted on Leno cloud servers. Get $100 in hosting credit at
[31.28 --> 38.00]  leno.com slash change log. We deserve a better internet and the brave team has the recipe for
[38.00 --> 42.46]  bringing it to us. Start with Google Chrome, keep the extensions, the dev tools and the rendering
[42.46 --> 47.58]  engine that make Chrome great. Rip out the Google bits. We don't need them. Mix in ad and tracker
[47.58 --> 52.76]  blocking by default. Quick access to the Tor network for true private browsing and an opt-in
[52.76 --> 57.60]  reward system. So you can get paid to view privacy respecting ads, then turn around and use those
[57.60 --> 62.36]  rewards to support your favorite web creators like us. Download brave today using the link in
[62.36 --> 77.42]  the show notes and give tipping a try on change log.com. Welcome to practical AI, a weekly podcast that
[77.42 --> 82.36]  makes artificial intelligence, practical, productive, and accessible to everyone. This is where
[82.36 --> 87.56]  conversations around AI, machine learning and data science happen. Join the community and Slack with
[87.56 --> 92.66]  us around various topics of the show at change log.com slash community and follow us on Twitter. We're at
[92.66 --> 107.16]  Practical AI FM. Welcome to another episode of Practical AI. This is Daniel Whitenack. I am a data scientist
[107.16 --> 113.50]  at SIL International and I'm joined as always by my co-host Chris Benson, who is a principal emerging
[113.50 --> 117.26]  technology strategist at Lockheed Martin. How are you doing, Chris?
[117.66 --> 119.46]  I am doing very well. How's it going, Daniel?
[119.82 --> 124.42]  It's going great. It's warmer now in the US. A lot of people have been having some issues,
[124.74 --> 130.08]  particularly down in Texas and other areas. So this is for those listening later in the podcast,
[130.08 --> 136.66]  this is February of 2021. A lot of snow and cold weather in the US here.
[137.12 --> 142.98]  So a couple of people on our team at work are in Texas and we've been getting all the stories
[142.98 --> 148.26]  when they're able to connect and stuff. So I think they're getting through it finally. Thank goodness
[148.26 --> 154.62]  it was pretty horrible. But in the meantime, I am enjoying my 70-something, you know, my 70-degree
[154.62 --> 159.92]  plus weather outside, spring-like, and I'm kind of sticking my tongue out on them on Zoom meetings.
[160.48 --> 164.94]  Yeah, it's always interesting during these particular types of events because you kind of
[164.94 --> 171.18]  just assume that people have all this like redundant fault-tolerant like infrastructure
[171.18 --> 177.10]  going on for like their APIs and other things. And these sorts of events really reveal like that
[177.10 --> 183.66]  is not the case. Like I know like one of the APIs we frequently use is like apparently on a
[183.66 --> 190.50]  on-prem server in Dallas and they did not have power. And, you know, you learn new and interesting
[190.50 --> 196.52]  things like that. You know what? After the past year, there's nothing that surprises me anymore.
[196.52 --> 202.08]  Not now. Global pandemics, all sorts of strife, you name it. I mean, I'm just, yeah,
[202.36 --> 208.88]  nothing. Nothing phases me now. Yeah, I'm glad to hear you've built a lot of robustness into your
[208.88 --> 213.46]  personal life there, Chris. There we go. I laugh a lot. I snicker a lot. That's how I cope.
[213.66 --> 220.28]  Yeah. Well, a few months ago, actually, I think it was one of the researchers at SIL that I work with
[220.28 --> 228.54]  called Gary Simons. He's been a linguist and programmer, computational linguist, translator
[228.54 --> 235.86]  type researcher for decades. And he sent me this link in our Skype communication and said,
[235.96 --> 239.82]  hey, this is a really cool article. You should think about having this on your podcast. And
[239.82 --> 246.52]  there's an article called Green AI from Communications of the ACM. And I'm really happy
[246.52 --> 253.60]  today because we get to materialize what Gary saw and what he recommended to me. And we've got
[253.60 --> 260.56]  Roy Schwartz and Jesse Dodge with us. Roy is a senior lecturer at Hebrew University of Jerusalem.
[261.32 --> 266.18]  And Jesse Dodge is a postdoc at the Allen Institute for AI. And they were both authors on
[266.18 --> 271.46]  that article. Welcome, guys. Thanks for having us. Thank you. Yeah. If both of you could just
[271.46 --> 276.18]  give us a little bit of a background about yourselves, that'd be great. Why don't we start
[276.18 --> 284.36]  with Jesse? Sure. So I finished my PhD from Carnegie Mellon in the Language Technologies Institute last
[284.36 --> 291.90]  year in 2020 in the pandemic. Although I spent most of my PhD at the University of Washington in Seattle.
[291.90 --> 298.98]  And part of that time I spent working at the Allen Institute for AI, where after I graduated,
[299.22 --> 307.14]  now I'm back as a postdoc full time. So we wrote this article, I think, back in, we were thinking
[307.14 --> 317.60]  about this for quite a while and then wrote this back in 2019 and really got it out in 2020. So yeah,
[317.60 --> 325.28]  now here, even though the offices are closed, I'm still here in Seattle. And I am on the Allen and LP
[325.28 --> 331.22]  team once again. Awesome. And what are you specifically working on? So my research sort of
[331.22 --> 337.80]  falls under two broad umbrellas. The first is related to efficiency, similar to this green AI idea that
[337.80 --> 346.00]  we'll get into. I work on making models more efficient along the number of dimensions that they have
[346.00 --> 354.50]  in terms of the complexity, in terms of inference, generally related to any way that you can measure
[354.50 --> 361.44]  like the total computational cost of getting some kind of experimental result. And then the second
[361.44 --> 366.72]  pillar of my research relates to reproducibility, where I created the natural language processing
[366.72 --> 373.82]  reproducibility checklist that was used at, I think, four major NLP conferences now. And I've published
[373.82 --> 379.48]  some work on how we can make the science of machine learning and natural language processing
[379.48 --> 380.58]  more reproducible.
[381.28 --> 387.66]  Yeah, that's awesome. Well, you're working on two things that are just like desperately needed
[387.66 --> 394.08]  in terms of focus. So yeah, I commend you in terms of that. And yeah, it's really great. Great to hear.
[394.46 --> 395.54]  Roy, what about yourself?
[395.82 --> 401.32]  Hi, so I'm Roy Schwartz. I'm a senior lecturer, which is an equivalent to assistant professor at the
[401.32 --> 406.86]  Hebrew University of Jerusalem. I'm currently in Jerusalem. I joined the Hebrew University last
[406.86 --> 411.74]  summer. And before that, I spent four years in Seattle, where I got to meet Jesse, fortunately.
[412.40 --> 417.78]  And I was a postdoc and then a research scientist at the University of Washington and the Allen Institute
[417.78 --> 424.44]  for AI. And these were four wonderful years. But now I'm back home. Similar to Jesse, to some extent,
[424.44 --> 433.44]  I also came from the university where I did my PhD and took a break and came back. My research also
[433.44 --> 441.92]  spans two or maybe three dimensions. One of them is similar to Jesse, efficiency and trying to think
[441.92 --> 448.74]  about ways to reduce the cost of AI and NLP in particular. And the other is trying to get better
[448.74 --> 454.10]  understanding of this technology. Now that we have models that are becoming so big and so good at what
[454.10 --> 459.14]  they're doing. But at the same time, it's very hard to know why they're doing certain things, why
[459.14 --> 466.76]  some things work and some don't. Why do models reach certain decisions? I'm particularly interested
[466.76 --> 472.20]  in the role of data in all of this. How do our data sets look? What do they contain? What kind of
[472.20 --> 477.52]  phenomena are encoded in them? And I like to make connections between all of these goals,
[477.76 --> 481.40]  between understanding and between understanding our data and between making things more efficient.
[482.08 --> 483.96]  And these are some of the things that I'm most excited about.
[484.64 --> 490.82]  Awesome. Before we move on, what is your general impression about sort of progress in this process
[490.82 --> 496.78]  of trying to make our models more interpretable and understand more about them? Obviously, you're doing
[496.78 --> 501.78]  work in the field. So hopefully, like you see progress in that. But as an industry as a whole,
[501.78 --> 504.00]  where do you think we are on that journey?
[504.84 --> 511.10]  That's a great question. So as you said, on one end, we're making tons of progress. I mean,
[511.38 --> 517.30]  lots of very smart people are working towards developing method to probe models to kind of
[517.30 --> 522.74]  kind of poke them and ask them, I mean, do you know syntax? Do you know world knowledge? Do you know
[522.74 --> 528.18]  this? Do you know that? And we're developing methods that are more and more sophisticated to get this
[528.18 --> 533.70]  information? At the same time, the core questions that I think will make a huge impact if we're able
[533.70 --> 537.78]  to solve them. And I'm not sure if these questions are even solvable to some extent, and I'm happy to
[537.78 --> 543.28]  talk about it, even though it's not the topic of today's talk is, how do we get models to explain
[543.28 --> 549.10]  what they're doing? To explain it in a reliable way? In a way that's, I mean, I'll just say one thing.
[549.16 --> 554.66]  I mean, when you ask a person, why did they do something like that? That he did. The explanations are often
[554.66 --> 561.84]  also not, I mean, they might be post rationale of things that it's hard even for us to say what we're,
[561.94 --> 568.28]  why we're doing certain things and we're conscious creatures. So machines are, it's much harder to get
[568.28 --> 574.50]  this, but we're trying. I appreciate that. As we, as we look at this, we're talking, I'm looking at
[574.50 --> 581.64]  your green AI article here again, and I'm just kind of curious, you know, what was your motivation for
[581.64 --> 587.74]  putting this out? And probably I should ask as part of that, you know, what is green AI, you know,
[587.78 --> 593.84]  initially? And how did you decide that this was the thing that you needed to get out there to the
[593.84 --> 600.04]  world? And because it's, this is a topic that often gets left out of AI ethics and such, having
[600.04 --> 603.68]  worked in that field for a while. We can go back to that in a little bit. I'm curious what your
[603.68 --> 609.00]  motivation was though. Yeah. So I think part of it was some conversations that Roy and I had,
[609.00 --> 615.78]  again, this was back in 2019 when we were both at the Allen Institute for AI. And we noticed that
[615.78 --> 622.28]  there was this increasing trend of larger and larger computational budgets used for some of the
[622.28 --> 629.18]  research papers that were published in NLP. We looked around and found, not only did we notice this,
[629.24 --> 634.62]  but there were a couple other pieces of work that had also noticed this trend. So back, you know,
[634.62 --> 643.10]  when I started my PhD back in 2013, I could run my experiments often on a used laptop that I had
[643.10 --> 648.38]  purchased off of Amazon. And it was kind of slow, but I would, you know, I could run most of my,
[648.64 --> 654.24]  I could train my models in a few minutes or an hour maybe. And it worked and that was okay. And then
[654.24 --> 660.78]  we noticed in, you know, in 2019, we were like, wow, a lot of these models don't even fit on a single
[660.78 --> 667.88]  GPU. And we have to like rent like cloud instances to be able to actually use some of these models.
[668.38 --> 674.96]  Plus in some cases, papers would do, for example, a tremendous amount of hyperparameter optimization,
[674.96 --> 681.08]  or they would train on a huge amount of data well beyond what we could do, even at, you know,
[681.08 --> 687.20]  a good institution, like, like the university of Washington or AI2. And one interesting thing,
[687.20 --> 693.68]  and this has really been followed up by some concrete research is that we do find significant
[693.68 --> 700.60]  improvements in performance across a lot of tasks, just by scaling up these models. So language
[700.60 --> 709.10]  modeling, for example, has been a pretty foundational task in NLP. What we found is that training models
[709.10 --> 716.62]  to do well at this task of language modeling, if you train a large enough model on enough language data,
[716.62 --> 722.76]  then that model can do some other tasks that we're interested in as well. So it somehow learns
[722.76 --> 729.22]  some kind of representation of language that's useful across a wide variety of tasks. But to get there,
[729.22 --> 736.60]  we saw just huge computational budgets used for a number of these papers. And interestingly,
[736.80 --> 742.02]  I mean, we wrote this a while ago, but the trend has not slowed down. So this is something like Roy
[742.02 --> 750.62]  and I are still working on similar motivated pieces about how this is really driving a lot of research
[750.62 --> 756.04]  in our field, like these, these massive scaling laws, for example, are pushing state of the art and
[756.04 --> 761.80]  also getting a lot of attention and having, you know, our field is interesting. You can view our field
[761.80 --> 765.34]  through that lens now and see some interesting results.
[765.34 --> 772.94]  Yeah. So I'm curious. I have my own thoughts about how I might answer this question, but I also
[772.94 --> 779.84]  haven't done the amount of thinking that both of you have. So I don't know, maybe Roy, if you want to
[779.84 --> 786.58]  comment on this or kick it back to Jesse. So that trend has been continuing and like we're seeing those
[786.58 --> 793.30]  sort of improved results in some areas along that trend, like in language modeling. So why is that
[793.30 --> 798.02]  a problem or like what sorts of problems or red flags does that bring up? I guess.
[798.78 --> 803.92]  Yeah. I mean, I think there, it's interesting because Jesse and I bring complimentary motivations
[803.92 --> 808.50]  for tackling this problem. So, I mean, when I started thinking about these things, I mean, yes,
[808.54 --> 813.60]  I was having discussions with Jesse about this, but I'm a person that cares about the environment and I
[813.60 --> 818.84]  try to make personal choices that, you know, I, I ride my bike to work because it's healthy, but also
[818.84 --> 823.88]  because it allows me to not drive my car. And I try to, you know, turn the light off when I leave
[823.88 --> 828.42]  the room, you know, do these things that don't, you know, don't matter much at the global scale,
[828.46 --> 833.66]  but, you know, I make my personal choices. And then I go to my office and I, I don't know if you've ever
[833.66 --> 840.48]  seen a GPU, but this is a very loud machine, very, a machine that's emits a lot of heat.
[840.48 --> 846.20]  Yeah. Yeah. And kind of running stuff, you know, like, okay, let's just push a button and suddenly,
[846.20 --> 852.60]  you know, five degrees or 10 degrees up in your room, maybe, but not in your planet, hopefully.
[853.12 --> 856.90]  And kind of, it's been something I've, I've been thinking about quite a bit. I mean,
[856.90 --> 862.38]  what's the total impact of our field? And, uh, Jesse and I have been talking about this and then
[862.38 --> 868.28]  I think in mid 2019 or early mid 2019, a paper came out from the university of Massachusetts,
[868.28 --> 875.78]  led by Emma Struble and her colleagues that tried to quantify the CO2 impact of a large scale NLP
[875.78 --> 880.68]  experiments. And she came to the, she and her colleagues came to the conclusions that one of
[880.68 --> 885.74]  the most expensive experiments that's run the trainer model in a process called the neural
[885.74 --> 890.86]  architecture search, which basically means we're going to train a bunch of models and select the
[890.86 --> 896.28]  best one. Uh, but when I say a bunch, I'm talking about thousands or tens of thousands of experiments.
[896.28 --> 904.28]  And she computed, uh, using some rough estimations, uh, to, to, to be said that, uh, the amount of CO2
[904.28 --> 911.90]  emitted by this process is equivalent to the amount of, uh, the life term, uh, omission of five cars,
[911.90 --> 917.08]  um, or, uh, several flights, or I don't, I don't remember the full detail, but I mean,
[917.08 --> 921.28]  something that I think it was five parts. I remember this coming out and I was also shocked.
[921.28 --> 926.40]  Yeah. Daniel and I actually talked about this in an episode way back when that came out. I remember
[926.40 --> 930.52]  us just commenting on it. Yeah. Everybody was talking about it and really hit me in a place
[930.52 --> 935.16]  that I, this is something that I was thinking about and I was really happy to, I mean, I was sad to see
[935.16 --> 940.32]  that, that my intuitions were right in some sense. I was kind of hoping that maybe it's, you know,
[940.32 --> 945.40]  it's not that bad, but, and, and kind of then Jesse and I were having discussions along with other
[945.40 --> 950.32]  people at AI2 and kind of, we were saying that, you know, this is something we need to do something
[950.32 --> 955.08]  about or, you know, to make the community more aware of it. And we were thinking about, I mean,
[955.08 --> 959.20]  AI2 is an institution that our goal is, uh, I mean, I'm not, I'm no longer working there,
[959.20 --> 963.80]  but at the time I was working there, uh, to do AI for the common good. And, you know, this feels like
[963.80 --> 969.88]  a natural fit, uh, for the goals of their organizations. And we got, um, Ornizioni,
[969.88 --> 976.92]  the CEO and Noah Smith, who was, uh, my manager and Jesse's, uh, advisor at the time, um, on board.
[976.92 --> 983.24]  And, you know, we wrote this piece and, uh, just hoping to get people, um, you know, thinking about
[983.24 --> 988.68]  this, you know, not necessarily thinking about this in terms of, uh, finding more accurate ways to
[988.68 --> 995.08]  quantify, uh, how much energy and, uh, is, uh, omitted and, uh, how much are the costs of these
[995.08 --> 999.80]  experiments and, uh, trying to encourage the community to work on more efficient solutions.
[999.88 --> 1001.72]  That would allow us to reduce these costs.
[1002.92 --> 1008.04]  Yeah. That's one way that Roy and I think like one thing that Roy just mentioned, um, is that we
[1008.04 --> 1012.68]  brought different perspectives to this. I completely agree with everything that Roy just said. Like,
[1012.68 --> 1017.56]  that's super motivational. I think that's, you know, very important going forward that we keep track of
[1017.56 --> 1023.16]  CO2 estimates and we do a great job at that. There's another, um, side to this also, which we write
[1023.16 --> 1029.56]  about in our green AI paper, uh, where we talk about the, the sort of research inequality or
[1029.56 --> 1035.72]  inequality in the research community where some of these, uh, experiments really could only be done
[1035.72 --> 1043.08]  by sort of the 1% of the research community, those that have access to tremendous numbers of GPUs or
[1043.08 --> 1051.88]  just like lots of machines. So one question that we address in our paper is, is this valuable research
[1051.88 --> 1057.72]  that we should treat on the same level as like other types of research that can be done primarily
[1057.72 --> 1066.12]  motivated by just a good idea rather than really expensive experiments? And so both of these are
[1066.12 --> 1071.96]  sort of negative consequences of this increasing trend that we observed. And one interesting thing,
[1071.96 --> 1077.72]  I think this is an interesting thing, sort of back in 2019, going back to that Struble et al paper,
[1078.60 --> 1085.64]  I found that through a number of conversations that I had had, and also just like the general information I saw
[1085.64 --> 1093.56]  online, when before Emma and her colleagues wrote that paper estimating the CO2 emissions, there was an
[1093.56 --> 1100.28]  understanding of like how some work was very expensive, how some work was quote boiling the ocean, for
[1100.28 --> 1106.92]  example, just to get a 1% improvement or half a percent improvement on some task. And so when Emma
[1106.92 --> 1114.60]  wrote that paper, I was surprised. But again, I mean, I felt similarly to Roy, I was surprised, I wish it,
[1114.60 --> 1120.60]  I hadn't been, you know, surprised by the results that I saw. I wish they had claimed that people were
[1120.60 --> 1126.92]  emitting less CO2. But it really did capture like her paper, and then our paper as well. I think these got
[1126.92 --> 1131.80]  so much traction, partly because we were outlining a trend that other people had also noticed.
[1132.44 --> 1136.60]  And yeah, like I said, that trend really does, I think we focus on two facets, there are probably
[1136.60 --> 1143.32]  others, but the CO2 emissions, and also the sort of this research inequality are both direct consequences
[1143.32 --> 1147.00]  of that, that increasing trend.
[1147.00 --> 1161.32]  Hey friends, this episode of Practical AI is brought to you by Codeish, a podcast from the
[1161.32 --> 1166.76]  team at Heroku that explores code, technology, tools, tips, and developer life. There's tons of
[1166.76 --> 1171.64]  great conversations on the Codeish podcast, so I would encourage you to check it out and subscribe. But
[1171.64 --> 1177.96]  in particular, I wanted to bring to your attention two episodes, episode 98 and 99, where Julien Duque
[1178.28 --> 1184.44]  explores the ethical and technical sides of deep fakes. The rise of manipulated pictures and videos and
[1184.44 --> 1190.04]  other forms of computer-generated media are able to cause uncertainty and doubt in what we see and hear
[1190.04 --> 1195.64]  online. So how are we able to use these tools for good, if at all? Here's a sneak peek.
[1195.64 --> 1202.68]  Let's say we want to do a deep fake of my voice, and we train the model and we have enough data and
[1202.68 --> 1212.76]  everything. This will be also able to imitate my accent, for example, like how I pronounce English and the
[1212.76 --> 1216.76]  strong pieces of my accent, or is not there yet?
[1216.76 --> 1223.88]  It really depends. If there would be a person with similar accent on the input, then it would be fine,
[1223.88 --> 1229.24]  but it's kind of cheating. You can think it's cheating because we're reusing accent of a different
[1229.24 --> 1235.80]  person that's similar to your accent. But if it would be like an American native speaker or a British,
[1235.80 --> 1244.44]  a person with a British accent, or like whatever other accent, then it will kind of be a mixture on
[1244.44 --> 1251.16]  the output. So we're not there yet in terms of converting accents. It's a little bit more
[1251.16 --> 1255.08]  difficult than we initially anticipated because when we started the company, we thought it would be,
[1255.08 --> 1259.96]  you know, we'll kind of solve it in a year or something. But then it turned out that, oh no,
[1261.32 --> 1262.92]  we're here for much longer.
[1262.92 --> 1269.64]  Check these episodes out. Links are in the show notes to both episodes or head to heroku.com
[1269.64 --> 1276.20]  slash podcasts to listen and subscribe. Again, check the shows for links or go to heroku.com
[1276.20 --> 1288.04]  slash podcasts.
[1292.04 --> 1298.04]  So you brought up something that really kind of got my brain really going there for a minute. And I was,
[1298.04 --> 1304.20]  it was thinking about the fact that, you know, this really can matter a lot, even if not a lot of
[1304.20 --> 1311.16]  practitioners, you know, the number of practitioners in AI relative to all the people producing CO2 is
[1311.16 --> 1316.36]  quite small. But you mentioned going through all these models. And when we're doing things like
[1316.36 --> 1321.64]  hyperparameter optimization and trying, you know, little adjustments to architectures all the way
[1321.64 --> 1328.44]  through, and then one practitioner doing work is essentially, you know, being thousands of
[1328.44 --> 1334.12]  practitioners on a per model basis, as they're trying to hone in on that, it really amplifies
[1334.12 --> 1341.08]  the impact of what can happen. I mean, so I guess, you know, it's not, it's less of a problem that a
[1341.08 --> 1347.72]  very few people are doing and more of a problem that, that because that amplification is, is quite
[1347.72 --> 1352.44]  outsized relative to the number of people doing it. Am I getting that right? Am I understanding the
[1352.44 --> 1355.56]  problem in the way that you're thinking about it? Or am I missing something there?
[1355.56 --> 1356.52]  Am I missing something there?
[1356.52 --> 1360.28]  Am I missing something there? So I'm not 100% sure that I understood you. So let me try to
[1360.28 --> 1367.24]  sure to say where I think this is going. So, I mean, so I'm assuming you're talking about the
[1367.24 --> 1373.64]  environmental, uh, because, uh, because the inequality aspect, I think is pretty clear that,
[1373.64 --> 1380.68]  I mean, a very small proportion of the community can afford to run these experiments. Um, and kind of,
[1380.68 --> 1386.60]  when we're thinking about the environmental, uh, effect, then some people argue, and I'm not sure
[1386.60 --> 1393.08]  I disagree even that it's not so bad because these experiments are being run just a handful of time.
[1393.64 --> 1398.60]  And I might agree on that. I must say there are different ways in which the AI community is
[1398.60 --> 1406.68]  contributing so-and-so quote-unquote to the omission of CO2 to the atmosphere. And probably the one that's
[1406.68 --> 1411.96]  easiest to measure is the most expensive experiments. That's perhaps one dimension.
[1411.96 --> 1416.92]  You can also think about, I mean, the entire, uh, the amount of training being done by the entire
[1416.92 --> 1423.08]  community and probably most influential in this sense is the, the cost of inference of cost of taking
[1423.08 --> 1430.12]  a model that's been trained and running it. And this is one operation is very cheap, uh, especially
[1430.12 --> 1434.84]  obviously compared to training a model, but this is something that happens at scale. Uh, if you think
[1434.84 --> 1439.40]  about, I don't know, the amount of Google search queries that are being run per day or the
[1439.40 --> 1446.20]  translation or the number of videos being edited or recommendations and in various websites.
[1446.20 --> 1450.44]  So there's different dimensions to these problems. And I think what we're trying to promote is not
[1450.44 --> 1456.92]  so necessarily to say, uh, look, we're boiling the ocean as Jesse said, quote unquote, but I mean,
[1456.92 --> 1462.36]  we don't know exactly what is it that we're doing and let's be more honest about it. Let's do a better
[1462.36 --> 1468.92]  job at reporting and let's try to reduce these costs. I mean, and I mean, it's hard to argue
[1468.92 --> 1475.08]  against, uh, I mean, who doesn't want cheaper models, right? It's obviously that, uh, other things
[1475.08 --> 1480.84]  are, uh, and you know, if, if cheaper models perform slightly worse and maybe this slightly worse
[1480.84 --> 1487.72]  translates to slightly less revenue than maybe cheaper. There are different ways to define cheap.
[1487.72 --> 1491.80]  So I think what we're trying to promote is to get more people thinking about it and not just
[1491.80 --> 1498.12]  improving another Epsilon on the accuracy level. Yeah. That's super helpful. I think,
[1498.68 --> 1506.76]  you know, one of the things that's running through my mind is, um, uh, I guess like talking about,
[1506.76 --> 1513.48]  you know, what are the other options? What does it mean to do green AI? And I have this parallel in my mind.
[1513.48 --> 1518.28]  So I come from a physics background and like, if you're in high energy physics now, like there's
[1518.28 --> 1523.40]  just been a progression of larger and larger particle accelerators. Right. And now if you want
[1523.40 --> 1528.60]  to do high energy physics, you're going to spend some time at CERN, um, in Switzerland or whatever,
[1528.60 --> 1534.12]  just because no one has another CERN, right? Like they're, they're just not there. So like,
[1534.12 --> 1539.88]  is there another option for, and I'm thinking particularly Jesse of what you were highlighting in
[1539.88 --> 1546.04]  terms of the research inequality, I think that's a really great point. Like what can we do in terms
[1546.04 --> 1551.96]  of reducing that inequality? And is there something more that we can say other than like tough luck,
[1551.96 --> 1555.96]  go work at Google or somewhere that has these like amazing resource, you know,
[1557.16 --> 1560.20]  seemingly endless resources to do these massive experiments?
[1560.20 --> 1564.44]  Yeah. So that's a great question. I think this is something that comes up a lot is sort of the
[1564.44 --> 1569.48]  relationship. When we talk about green AI, sometimes somebody will say to us, oh, but in biology,
[1569.48 --> 1575.64]  it costs so much to do any experiment because you need a wet lab and because you need, you know,
[1575.64 --> 1581.00]  some equipment and you just can't do it without that equipment. So is it bad that some experiments
[1581.00 --> 1587.48]  in our field are expensive? And I think the answer here is really that in the computational sciences
[1587.48 --> 1592.92]  and in machine learning and NLP in particular, we really can, there are a few things that we can do
[1592.92 --> 1600.52]  that make future comparisons against our work with smaller budgets easier. So one example of that
[1600.52 --> 1608.36]  might be sure. I train a model on all of the language data on the entire internet, right? But I can also
[1609.24 --> 1615.96]  evaluate that same model after training on only a fraction of that data. And if I do this, let's say I
[1615.96 --> 1623.32]  train and evaluate evaluation in this case is typically pretty inexpensive. So your evaluation
[1623.32 --> 1629.00]  set, your data set that you evaluate on is often much smaller than it's like, you know, a 10th or
[1629.64 --> 1637.32]  even smaller of your training size. So one thing that we can do is just checkpoint our model or evaluate
[1637.32 --> 1644.20]  it regularly throughout training. And then a future researcher will be able to come up with a new idea.
[1644.20 --> 1650.20]  Let's say they have a new model that they want to evaluate. And they can compare against some of
[1650.20 --> 1657.80]  those sort of smaller budget evaluations. So for us, the point here is that in our field, we really do
[1657.80 --> 1664.60]  have a few ways that we can sort of build in these sort of low budget comparison opportunities.
[1665.48 --> 1671.56]  And that enables not just future comparisons, but that really drives the sort of competitive nature of
[1671.56 --> 1678.36]  our field where instead of trying to improve just the absolute best found performance,
[1678.36 --> 1684.20]  somebody could try to find a better performance efficiency trade-off where at a low budget,
[1684.20 --> 1690.28]  their new idea, a low budget for, you know, the number of parameters in your model or the total
[1690.28 --> 1695.00]  number of experiments of hyperparameter tuning or the amount of training data you use along any of those
[1695.00 --> 1702.44]  dimensions, somebody else might come along and try to compare against your work specifically in those
[1702.44 --> 1708.04]  sort of low budget regimes. And so I think here, that's a key difference between our field and,
[1708.04 --> 1713.00]  you know, physics, like you mentioned, or we often hear biology. And really, if you think about it,
[1713.00 --> 1717.48]  if you're training a model and it costs you, say, a million dollars to train on all of the internet,
[1717.48 --> 1723.88]  spending an extra $10,000 on just evaluating that model, spending an extra, you know,
[1723.88 --> 1731.00]  tenth of 1% or some small fraction of your total budget so that other people in the future, they can
[1732.28 --> 1738.60]  have an opportunity, they've got that hook to compare against. That is what one way that we can
[1738.60 --> 1742.76]  help drive the overall cost down by promoting that kind of competition.
[1742.76 --> 1749.96]  Yeah, I totally agree with what Jesse said. I think presenting another angle of this.
[1749.96 --> 1754.28]  So currently, there are certain norms in our community and kind of, I mean, there are certain
[1754.28 --> 1760.92]  ways of, I mean, topics of research that gets, you know, more visibility and more credit from the
[1760.92 --> 1767.96]  community while others aren't. And I don't want to say the naive assumption is, you know, go work at
[1767.96 --> 1772.44]  Google, as you said. I mean, but I mean, the fact is that when we were thinking about this
[1772.44 --> 1778.60]  paper, a couple of years back, we were doing a short survey of papers in ACL, that's the top
[1778.60 --> 1785.16]  venue for our field and in other similar venues in other fields of AI. And we found we had a very
[1785.16 --> 1789.80]  hard time finding papers that focused on efficiency. Most of the papers we were looking at were trying
[1789.80 --> 1793.64]  to say, okay, we did this and this and that, and we got some better improvement here and this and
[1793.64 --> 1800.20]  that and we got some, you know, tenth of a percent better on some accuracy or answering questions,
[1800.20 --> 1807.48]  a tenth of a percent better or translating a fraction of a percent better there. And what we're
[1807.48 --> 1813.16]  trying to argue that this is not a good balance. We want to see, it's good that people are working to
[1813.16 --> 1817.16]  make our models more accurate. We're not arguing that this is not important. And similarly, we're not
[1817.16 --> 1821.40]  arguing that the big models aren't important. They're making huge contributions to our field.
[1821.40 --> 1827.88]  But we think that a larger chunk of the research efforts should go towards trying to find solutions
[1827.88 --> 1836.60]  that are not epsilon better, but are twice as fast or take 10% of the memory or what have you.
[1837.24 --> 1845.72]  And we're trying to work with the research community by providing ways to publish this work. For instance,
[1845.72 --> 1852.52]  we've established tracks and tracks are kind of like, you can think of it as topics in major conferences,
[1852.52 --> 1858.76]  where when we were working on some of our work that tried to promote efficiency or presented an efficient
[1858.76 --> 1865.32]  solution, as I said, that works five times faster, but doesn't improve the performance. We had a hard
[1865.32 --> 1874.12]  time deciding where to send this paper to and where we would get the best audience to appreciate it.
[1874.12 --> 1881.80]  And what we were able to do in the past year is to set up a green NLP track or an efficient NLP track
[1881.80 --> 1889.00]  in our conferences that allow works that focus on that to get published and to get the visibility that
[1889.00 --> 1889.40]  they deserve.
[1889.40 --> 1895.96]  Yeah, that's great. And I think another thing to build on what Roy just said is our community,
[1895.96 --> 1901.24]  like the, I think one strength of the research community is really that it's just a collection
[1901.24 --> 1908.60]  of individuals all trying to do the best work that they can. There is no overall governing body.
[1908.60 --> 1914.28]  So when we think about like, how can we get our community to focus on more efficient approaches?
[1914.28 --> 1920.52]  It's kind of tricky, you know, we can't, it's just not possible for us to say like some fraction of
[1920.52 --> 1926.20]  the work should cover this, this topic. So instead we thought a lot about the types of incentive
[1926.20 --> 1932.92]  structures that impact people in our field and creating this track, as Roy just mentioned,
[1932.92 --> 1938.28]  is one of the ways that we can promote this and provide an opportunity sort of lowering barriers
[1938.28 --> 1952.84]  for publishing work on work that promotes efficiency.
[1957.24 --> 1962.44]  Have you heard about Knowable? It is an awesome new platform for learning from the world's best minds,
[1962.44 --> 1969.56]  anytime, anywhere, at your own pace, through audio. Learn about the performance benefits of a plant-based
[1969.56 --> 1976.28]  lifestyle from NBA all-star Chris Paul, or how to launch a startup from Reddit co-founder Alexis Ohanian.
[1976.28 --> 1980.68]  There's even a 10 lesson course from astronaut Scott Kelly. Here's a sneak peek.
[1982.60 --> 1988.52]  We learned a lot up there, but what can you learn from a life in space? The answers might surprise you.
[1988.52 --> 1993.64]  In this knowable course, I want to share some of the things I've learned that you might not expect.
[1994.84 --> 1999.64]  Lessons about leadership on a dark night on an aircraft carrier in the middle of a churning sea.
[2000.60 --> 2005.72]  Lessons about the fear you feel with 7 million pounds of thrust exploding underneath you.
[2007.24 --> 2011.08]  And most of all, there's an idea out there that astronauts are always perfect.
[2011.88 --> 2017.56]  Failure is not an option, right? That's why I want to take you through some of my life experiences to
[2017.56 --> 2025.00]  show you how that's just not true. I believe every day, regular human failure, if we handle it right,
[2025.00 --> 2029.00]  can be one of our greatest opportunities to learn, grow, and succeed.
[2029.80 --> 2035.08]  Knowable is accessible on your phone and on the web, and each audio course is broken out into
[2035.08 --> 2040.04]  individual lessons, usually around 15 minutes long. As a changelog listener, you can get an
[2040.04 --> 2046.68]  annual membership to Knowable for 20% off. Get unlimited access to every Knowable audio course right now.
[2046.68 --> 2053.96]  Just download the Knowable app or visit knowable.fyi and use code changelog for that 20% discount.
[2054.28 --> 2059.96]  We put a link in your show notes for easy click-ins. Check out Knowable today and start learning from
[2059.96 --> 2065.24]  hundreds of top experts from around the world. Once again, that's knowable.fyi, code changelog.
[2065.24 --> 2080.92]  So this is really interesting to me. As I'm listening to you, I'm trying to think how I'm going to
[2080.92 --> 2089.08]  implement. So can you kind of describe some of the good examples of how Green AI has been implemented
[2089.08 --> 2097.16]  before and any kind of guidance? So if I'm a practitioner, you know, you've hit on some of the
[2097.16 --> 2103.00]  practices, but either go through someone else's example or something that you've described to
[2103.00 --> 2106.92]  people because I'm just trying to really make it to where when I walk out of here, I want to be able
[2106.92 --> 2112.52]  to go ahead and implement that. Yeah, so I guess I can, I'll talk a little bit about this. So one thing
[2112.52 --> 2119.08]  that I mentioned already was performance efficiency trade-offs. And I think that the key idea here,
[2119.08 --> 2124.60]  and one thing that we found when we did this survey that Roy mentioned of papers in our field is that
[2125.56 --> 2133.80]  most papers just don't report anything. They don't report any efficiency-related metrics at all.
[2134.84 --> 2141.16]  Most papers in our field invent some new model or some new, you know, loss function, some new
[2141.16 --> 2146.68]  training scheme, something like that, and then claim in a table, here's our better performance,
[2146.68 --> 2152.76]  we beat our baselines. But they don't report, for example, training curves or, you know,
[2153.72 --> 2159.08]  some other measure where you can trade off efficiency and performance. Maybe accuracy could
[2159.08 --> 2165.24]  be one measure of performance. So an example of this, and I guess the first thing that I would say here is
[2165.24 --> 2172.44]  is what we hope everyone in the research community starts to do, and we are seeing this happen now,
[2172.44 --> 2179.08]  is just report something. Report some measure of how maybe it's going to be the floating point
[2179.08 --> 2184.28]  operations to run your model. Maybe it's going to be a training curve. Maybe it's going to be
[2185.24 --> 2191.72]  the results from your hyperparameter optimization search, right? So one example of this
[2191.72 --> 2197.40]  I can point to is a paper, and I think this is, I use this as a positive example of how somebody can
[2197.40 --> 2204.68]  report this kind of information. So Roy and I wrote a paper on that used early stopping. So we
[2205.32 --> 2214.52]  partway processed an example and then potentially had our model stop early. So instead of feeding the
[2214.52 --> 2219.40]  example all the way through our model and then coming up with a prediction at the end, we had ways for our
[2219.40 --> 2225.96]  model to stop this computation early and make a decision quickly. And this method allowed us to
[2226.52 --> 2233.40]  show performance efficiency trade-offs, these smooth curves, which anyone can then compare against at
[2233.40 --> 2239.08]  any point. And what I would hope to see is other work come along and show a better curve rather than
[2239.08 --> 2245.64]  just a single point on this performance efficiency trade-off. They can report just here's how efficient my
[2245.64 --> 2251.64]  model was and here's the performance, potentially beating our entire curve or just a single point,
[2251.64 --> 2257.40]  you know, better along one of those dimensions. In this way, like just reporting more information
[2258.04 --> 2263.80]  allows others to compete along either of those dimensions or potentially draw a better curve.
[2263.80 --> 2269.40]  So I'm curious, I think a lot of what we've talked about has been focused on like,
[2269.40 --> 2276.84]  what are ways in which we can still explore this regime of like large models, but potentially be
[2276.84 --> 2282.60]  responsible about how we're reporting the cost of it and or how we're allowing others to build on top
[2282.60 --> 2290.44]  of what we're building. I'm wondering how maybe another side of this fits into this whole discussion,
[2290.44 --> 2297.08]  which is just plain smaller and more and or more efficient or different models. So I'm thinking of
[2297.08 --> 2305.32]  things like recently I was playing around with like QuartzNet, which is this end-to-end speech
[2305.32 --> 2313.88]  recognition model from NVIDIA, which is very compact based on these like 1D time separable convolutions.
[2313.88 --> 2320.12]  And it's like, like the whole model like on disk is like 90 megabytes or something like that. And like,
[2320.68 --> 2326.92]  it shows like really good performance, almost like comparable or comparable to like these really large
[2326.92 --> 2333.32]  speech recognition models. So I'm curious, maybe that also has some advantages in terms of like some
[2333.32 --> 2338.68]  of the interpretability things, Roy, that you're interested in. Where do you see that this whole
[2339.48 --> 2345.56]  regime of new and different, more efficient models fitting into this? And do you see momentum in that
[2345.56 --> 2352.76]  area or good examples in that area as well? Yeah, I think there's been a lot of, I mean, I think the thing that I
[2352.76 --> 2359.24]  said a few minutes ago about seeing that we saw very little work that focuses on efficiency. I think
[2359.24 --> 2364.36]  in the last couple of years, there's been more and more work that focuses on that. And we're delighted to
[2364.36 --> 2368.92]  see that. It's probably has nothing to do with us. It's probably something that would have happened
[2368.92 --> 2375.56]  anyway. And I think that the main ideas that are being mostly explored are ways to make inference more
[2375.56 --> 2381.16]  efficient. And this makes sense, at least in the environmental aspect, but also, you know, just in
[2381.16 --> 2388.52]  terms of you want to put a speech recognition or an image processing or a text processing machine on
[2388.52 --> 2393.56]  your phone. And then you need for it to be, you know, small in terms of number of parameters or
[2393.56 --> 2399.48]  the amount of space it requires, or, you know, it doesn't require much energy, so it doesn't drain your
[2399.48 --> 2405.64]  battery and so on. So there has been a lot of efforts along these dimensions. And I think that the main
[2405.64 --> 2411.32]  governing technology there is to train a big model, you know, train it as big as you can,
[2411.32 --> 2418.20]  and then train another model to imitate this model to some extent, or to take the large model and get
[2418.20 --> 2423.24]  the same performance using fewer resources. There are different techniques of doing that, but that's
[2423.24 --> 2428.92]  probably the most common thing that we've seen. What I think is very interesting, and people aren't putting
[2428.92 --> 2436.20]  that much effort into is to make the other parts of the process more efficient, namely training and
[2436.20 --> 2441.56]  what we call model selection, basically hyperparameter tuning, or other ways of selecting your best model.
[2442.12 --> 2448.12]  And I think this is the exciting direction that relates to the motivation. I mean, it's not like,
[2448.12 --> 2452.84]  I mean, it's not like there's Jesse's thing and Mike's thing, and we're both excited about both of these
[2452.84 --> 2460.04]  these motivations. And I think that this is a really one way to improve the ability of the entire
[2460.04 --> 2465.32]  community to conduct cutting edge experiments by reducing the cost of these processes.
[2465.96 --> 2470.36]  So in those other parts of our process that you're talking about, I can just imagine like
[2470.36 --> 2476.28]  there have been times, and I will totally confess to this, that like, whether it be hyperparameter
[2476.28 --> 2483.24]  tuning or like model selection or something like the logically the easiest way to go about that
[2483.24 --> 2488.68]  sometimes is just to say, oh, well, I can have this run for like a week and a half and like go through
[2488.68 --> 2498.20]  all these things. You know, there may be a more like a smarter or better efficient way to find the right
[2498.20 --> 2503.32]  zone that I should be in. But I can just like get this running and like come back to it in a week and a
[2503.32 --> 2509.00]  half or, or whatever. Do you also find that to be a sort of like a thing that you're talking to
[2509.00 --> 2513.72]  people about and a thing that you're running into? Is that just sort of like, I don't want to call
[2513.72 --> 2518.68]  people lazy. We're kind of spoiled in that way. Yeah, that's what I was thinking, actually, you know,
[2518.68 --> 2525.40]  programmers and researchers are often lazy, right? They have like a machine, let's just run it for a
[2525.40 --> 2530.68]  while. Yeah, I think I mean, the thing is, this is super common. Like there absolutely is a trade off
[2530.68 --> 2537.16]  between how much time you put in as an engineer or as a researcher. As any kind of practitioner,
[2537.16 --> 2542.36]  there's definitely a trade off, you could really carefully narrow down your hyper parameter ranges,
[2542.36 --> 2552.52]  and then spend less in GPU hours to find some good optimum. Or you could just set it up to be a super
[2552.52 --> 2558.72]  broad search, let it run for a week. And it'll, you know, it'll take you personally, like two days less
[2558.72 --> 2564.96]  time to run those experiments of your own hours, right? This is the thing is, this happens,
[2565.20 --> 2572.16]  everyone does this, there is some way to often reduce the amount of time that you have to manually
[2572.16 --> 2576.96]  engineer something. And you know, another way this can happen is, you'll think of some algorithm to,
[2578.32 --> 2582.16]  say implement to do inference in your model. And then later, you'll be like, Oh, you know what,
[2582.16 --> 2589.36]  I could make that faster by maybe 5%. If I spent a full working day rewriting all of that code.
[2590.24 --> 2596.48]  Sometimes, like, it's just not worth it. The key idea, I think, behind our green AI paper is that
[2596.48 --> 2604.00]  this happens all the time with people. And often, we just don't report that. So one analogy that I use
[2604.00 --> 2610.40]  is, is that we in our field, we don't keep lab notebooks. We just don't record a lot of the
[2610.40 --> 2616.40]  experiments that we run. And we treat those as like negative experiments, experiments that don't
[2616.40 --> 2621.04]  show what we're looking for. And then we only report the positive experiments at the end, right?
[2621.04 --> 2625.68]  So we just report the single best performance that we found. But with our green AI paper,
[2625.68 --> 2631.92]  what we argue is that we should be reporting, even if it's not always like the most optimized,
[2631.92 --> 2636.96]  the most efficient approach, the best thing that we can do right now is just report something.
[2636.96 --> 2642.48]  You know, it's a really good point there. And I want to ask Roy, I want to bring you back into it
[2642.48 --> 2647.44]  for a moment. The one of the things that you say in your paper is you say, finally, we know that the
[2647.44 --> 2652.28]  trend of releasing pre trained models publicly is a green success. And we'd like to encourage
[2652.28 --> 2657.74]  organizations to continue to release their models, in order to save others the cost of retraining them.
[2657.74 --> 2663.58]  So, you know, how far can you really get with pre trained models? Do you feel that that will do
[2663.58 --> 2668.94]  that? And is that kind of the way we should get people to start thinking about it? Because it seems
[2668.94 --> 2675.50]  like there's certainly a training component here in terms of driving people down the right path.
[2675.50 --> 2682.22]  Yeah, that's a great point. I mean, so again, this, we struggled a lot in the paper,
[2682.22 --> 2688.14]  when we're writing it, how to not, you know, I mean, what we call red AI kind of,
[2688.94 --> 2696.62]  there is a kind of the negative connotation there. But I mean, basically, I think there's tons of value
[2696.62 --> 2703.82]  in these large pre trained models. And definitely, I mean, once you release them, other people can train
[2704.38 --> 2710.46]  models much more efficiently. Because if you build up models like, I don't know if the name's Bert or Bert,
[2710.46 --> 2715.26]  I mean, you know, lots to many of the listeners. But I mean, these are typical models that are
[2715.26 --> 2720.06]  pre trained. I mean, some company in this case, Google or Facebook, put a lot of efforts into
[2720.06 --> 2724.30]  training them. And now they release them and other people can take them and use them for their own
[2724.30 --> 2728.86]  tasks. And the result will be much cheaper than if people train their own model from scratch.
[2729.42 --> 2735.10]  So this is definitely something that we encourage companies to do. I say companies because
[2735.10 --> 2741.02]  companies are basically the only entities that are can afford to, to do this. And again,
[2741.02 --> 2746.94]  kind of what our point is that these organizations shouldn't stop training these huge models, but we
[2746.94 --> 2751.50]  should be thinking about the negative consequences. And one way to mitigate the negative consequences is
[2751.50 --> 2757.58]  to make these models public, again, to reduce the overall costs for everyone to run these in their
[2757.58 --> 2758.06]  experiments.
[2758.06 --> 2765.18]  Yeah, so that has a huge benefit for those that are able to use those pre trained models and utilize
[2765.18 --> 2770.94]  model hubs and that sort of thing. But of course, there's like this element of companies where,
[2770.94 --> 2777.82]  of course, they're driven by by money, companies make money, and they often want to keep their models
[2777.82 --> 2783.98]  proprietary or something like that. But I think also, like, some of the things you highlighted earlier is
[2783.98 --> 2790.46]  that they're, you know, in terms of like commercial benefit and cost savings, there's also a cost
[2790.46 --> 2797.90]  saving element to being able to utilize something that's pre trained and maybe fine tune it. And
[2797.90 --> 2804.14]  that's a huge saving in labor, right. But also in utilizing these more efficient or smaller models,
[2804.14 --> 2810.78]  like maybe for inferencing, like you, you get less latency, or you have less computational costs,
[2810.78 --> 2819.82]  all those things. Do you think there is that sort of commercial or cost based argument to be made to
[2819.82 --> 2820.46]  companies?
[2820.46 --> 2826.86]  I think so. There's one thing that we saw recently, there was a citation, I think it was from Nvidia,
[2827.50 --> 2835.42]  that claimed about 90% of the cloud cost for machine learning was for inference, and only 10 to 20%
[2835.42 --> 2843.02]  was for training. So if you can spend a bit extra during the training phase, but end up with a model
[2843.02 --> 2848.54]  that's a bit more computationally efficient for inference, then potentially that could lead to
[2848.54 --> 2854.86]  savings in terms of like the amount of dollars spent renting instances in the cloud or GPU hours
[2854.86 --> 2861.34]  for inference, for example. I think that a lot of our focus has been on the research community. So you
[2861.34 --> 2867.42]  asked a question about like, are companies motivated to keep their pre trained models proprietary?
[2868.62 --> 2875.26]  While that's true, to some extent, my guess is the it's hard to know, it's hard for me to know if a
[2875.26 --> 2880.38]  company has done that, it's definitely possible, it's almost surely happened that some company has
[2880.38 --> 2885.90]  spent a lot of money training a model and then hasn't released it, because it's part of their business.
[2885.90 --> 2889.82]  At the same time, what we do know about is the research community. And this has grown
[2890.46 --> 2894.54]  exponentially, like not just the size of our experiments has grown dramatically in recent
[2894.54 --> 2899.90]  years, but the number of people in our field, and also the number of papers that are written,
[2899.90 --> 2906.38]  and the size of our conferences. So across, you know, we are already seeing such a tremendous growth
[2906.38 --> 2912.46]  there, I think it's very worth it to focus on helping save computational costs across inference,
[2912.46 --> 2917.82]  training, what have you. Yeah, yeah, I guess I think I'm the only person on the call working at a
[2917.82 --> 2923.66]  for profit, you know, commercial entity. And certainly, there are times when we aren't releasing
[2923.66 --> 2928.70]  that, you know, the way you would in the research community. So maybe I'm kind of curious, you know,
[2929.82 --> 2934.78]  would it make sense for us to, you know, yeah, you still have a group of people working in the
[2934.78 --> 2939.10]  organization that want to do the right thing always, you know, you so they're, you know, they're,
[2939.10 --> 2944.06]  they're no different in that way. So maybe still having internal targets for efficiency,
[2944.06 --> 2948.30]  kind of like what you talked about earlier, and those internal metrics, so that even if you
[2948.30 --> 2953.58]  aren't publishing them, publishing them for competitive reasons, or whatever, it may be that
[2953.58 --> 2959.98]  you're, you have a set of metrics that you're trying to achieve. And that might be that might be
[2959.98 --> 2964.14]  something they could spread through the commercial space, even when they're not willing to, to do a full
[2964.14 --> 2968.90]  release. Does that sound like a reasonable, you know, plan, you know, for those of us who,
[2969.02 --> 2973.14]  who do want to strive toward that, but maybe don't have the freedom to just release?
[2973.50 --> 2977.98]  Yeah, definitely. I mean, people have reached out to us from for crop for profit companies,
[2977.98 --> 2983.82]  and with similar stories to what you're telling, and they want to, you know, they work in a for profit
[2983.82 --> 2988.54]  company, so they are limited in what they can do, but they want to promote this, they they
[2988.54 --> 2994.62]  sympathize with the motivation, and they want to do the right thing within the scope of their,
[2994.62 --> 2996.86]  you know, what they can do inside a company.
[2996.86 --> 2998.78]  Within commercial constraints. Yeah, exactly.
[2999.10 --> 2999.82]  Yeah, I get it.
[2999.98 --> 3004.22]  So yeah, I mean, you know, as Jesse said, I mean, most of us, we're researchers, we're not part of,
[3004.22 --> 3010.94]  I mean, any company is different, I guess, with its own set of norms and rules. But we mostly
[3010.94 --> 3015.42]  communicate with the research community. But I mean, you know, there's stuff to be done everywhere,
[3015.42 --> 3019.66]  you know, thinking about, you know, thinking about efficiency, you don't have to persuade anybody
[3019.66 --> 3026.94]  that, you know, if all other things being equal, if your tool runs twice as fast, or takes half the
[3026.94 --> 3032.62]  amount of memory, then it's, you know, everybody wins. Great point. It's harder when you say,
[3032.62 --> 3040.38]  okay, I want to give up a fraction of percent or 1% or 10% and get it to run twice as fast. And
[3040.38 --> 3046.22]  there, you know, it's hard to go into, you know, questions of politics and regulations. And then
[3046.22 --> 3052.70]  what do these companies, what is the price of, for them to have expensive models running? Again,
[3052.70 --> 3057.58]  more on the environmental side, because this is not doesn't relate to the research community,
[3057.58 --> 3062.62]  because it's not open anyway. Yeah, I think another thing to build on that one thing that we're hoping
[3062.62 --> 3067.74]  with our, for example, the track that we have at these upcoming conferences, and the conferences that
[3067.74 --> 3075.18]  have happened, is a place where you can look for research that does directly aim to improve
[3075.18 --> 3081.10]  efficiency metrics. So as Roy mentioned earlier, distillation is one approach that's pretty popular
[3081.10 --> 3087.82]  about taking a large model and making it smaller and more efficient. There are a ton of ways to do
[3087.82 --> 3094.14]  this. So model compression using the lottery ticket hypothesis, or like Roy and I had a model
[3094.14 --> 3100.70]  compression paper. There's a lot of ways that people are taking existing work and making it more
[3100.70 --> 3106.14]  efficient. And with this track at these conferences, or just in general, you know, promoting these ideas,
[3106.14 --> 3113.50]  hopefully one thing that you can take away from this is a snapshot of ways that you can improve
[3113.50 --> 3120.38]  efficiency that have a good track record in the research community. Awesome. As we kind of close out here,
[3120.38 --> 3127.90]  I'm curious, since you both have like a very close pulse on the research community, in particularly your own
[3127.90 --> 3134.30]  areas of research, but also sort of more generally, I'm curious if we were to imagine in the future, and there's a
[3134.30 --> 3144.38]  world where, like green AI is the thing that that everyone's doing. So some of we've reached some of those goals. What else in the AI
[3144.38 --> 3153.26]  AI research world, or maybe like things, ways in which people are applying AI? What gets you excited
[3154.30 --> 3158.94]  as you look to the future of the industry? That's a great question. You know,
[3160.62 --> 3167.34]  something that keeps me busy thinking about, I mean, you know, thinking about the horizon of where I want to take my
[3167.34 --> 3174.54]  work and where would I like to be in 10, 20, 30 years. So I'm excited about a few things. One, I think
[3174.54 --> 3180.70]  I started with and to, you know, taking these, this amazing technology that does things that are far
[3180.70 --> 3186.78]  beyond our reach. And, and we, we seriously, I mean, as someone who's been around, you know, not a ton of
[3186.78 --> 3193.10]  time, but I mean, even five, seven years back, nobody would even imagine that we'd be anywhere close to
[3193.10 --> 3198.30]  solving the tasks that we're currently solving very successfully. And the questions that remain
[3198.30 --> 3203.18]  open are, how are we doing this? I mean, are we doing this because the models are very good at
[3203.18 --> 3207.82]  memorizing and they're just learning everything and kind of are very good at retrieving the information
[3207.82 --> 3214.46]  that they've learned? Are they really doing some sort of inference that requires some logic or some,
[3215.58 --> 3219.34]  you know, I don't want to use the word thinking, but you know, something that requires some processing
[3219.34 --> 3227.02]  that requires things that we as humans do. And could we generate models that explain why they
[3227.02 --> 3232.06]  reached a certain conclusion rather than others? And could we trust, I mean, we obviously can do whatever
[3232.06 --> 3237.82]  we can generate an explanation, but is this explanation faithful? And another thing that's, you know,
[3237.82 --> 3243.02]  gets me excited is to use this technology for all the good things that it can do. And in particularly
[3243.02 --> 3251.50]  thinking about doctors nowadays, that's, you know, how can we take things off their plate,
[3251.50 --> 3257.58]  allow them to do more of what they're, you know, there's tons of applications of, you know,
[3257.58 --> 3265.66]  starting from doing better analysis of x-rays for radiologists and to, you know, to transcribe their
[3266.86 --> 3272.38]  patient summaries in a more efficient ways and to be able to extract information from that. There are tons of
[3272.38 --> 3278.62]  applications here that this technology can be used to make things better for lots of people. So that's
[3279.58 --> 3280.62]  things that I'm excited about.
[3280.62 --> 3287.26]  Awesome. Yeah, us too. I know Chris and I both resonate with those points. So what about yourself, Jesse?
[3287.26 --> 3292.94]  There's a lot of things I'm excited about. I think Roy, I mean, things Roy brought up, I even just now,
[3292.94 --> 3297.42]  I'm like, those are all really cool. I want to work on that stuff too. I think for me, you know,
[3297.42 --> 3301.66]  continuing to work in these sort of two pillars of my research so far, which has been
[3301.66 --> 3309.34]  reproducibility and efficiency. These are pretty broad categories. So along the efficiency line,
[3309.34 --> 3314.86]  one thing that I have been continuing to think about is at least in NLP, what we've seen is like
[3314.86 --> 3320.78]  larger and larger language models, which are pre-trained on tremendous amounts of data. And then
[3320.78 --> 3326.06]  right now, what we've been doing is fine tuning these models. So updating all of the weights in the model
[3326.06 --> 3332.22]  so that we can perform well on some downstream task. That could be, you know, sentiment analysis or
[3332.86 --> 3338.06]  some kind of other types of text classification or whatever. My guess is as these models become
[3338.70 --> 3344.38]  larger and larger, there's probably going to be some other way that we can apply them to problems that
[3344.38 --> 3350.14]  we're interested in. An example of this that has recently been popular is adapters. So that's like
[3350.14 --> 3355.74]  adding a small number of parameters to one of these large pre-trained models, and then only updating that
[3355.74 --> 3361.10]  small fraction of the total number of parameters. I think the high level motivation here
[3362.78 --> 3369.74]  is that if these models are huge and we want to take a, you know, one massive pre-trained model and
[3369.74 --> 3373.98]  adapt it to a hundred different tasks, we don't want to have to have a hundred different copies of this
[3373.98 --> 3380.38]  model. We want to have some smaller fraction. So I think that that is a pretty motivational idea,
[3380.38 --> 3387.90]  exactly what the next big thing in NLP is going to be. The next, you know, big idea about how we take
[3388.54 --> 3392.94]  our pre-trained models and apply them to many different tasks in a relatively efficient way.
[3393.74 --> 3400.46]  I'm excited to see what that is. I think one similar idea, one way that we might do that is through
[3400.46 --> 3406.06]  um, probing tasks. So being able to probe our models without updating the weights in them
[3406.78 --> 3412.62]  to understand the kinds of inferences that they can make. I think that's a particularly interesting
[3412.62 --> 3417.74]  topic that's very active right now. I've seen, you know, too many papers to read just in the last
[3417.74 --> 3422.86]  month and a half on, um, trying to probe existing models. And then on the reproducibility side,
[3423.66 --> 3429.82]  you know, we've had the reproducibility checklist now used, um, for every submission at, I think,
[3430.38 --> 3435.18]  four conferences. That's a huge success. I'm pretty happy with, um, the way that's worked out.
[3435.18 --> 3438.38]  The reproducibility checklist, I guess, to give a little more information on that
[3439.02 --> 3444.38]  is a checklist that's designed to remind authors of the kinds of information they should include
[3444.38 --> 3449.42]  to make their work reproducible. So it has like, did you include the number of parameters in your
[3449.42 --> 3455.58]  model? And did you include the, you know, what the size of your data sets, for example, I'm excited
[3455.58 --> 3462.46]  and thinking about what we can do next with that information and also with the checklist. So now
[3462.46 --> 3467.18]  conferences are adopting it on their own. I've had to advocate in the past, you know, reaching out to
[3467.18 --> 3473.02]  the conference chairs and saying, Hey, I think we should do this. Now conferences have picked it up
[3473.02 --> 3478.70]  on their own, which is pretty exciting. So, you know, I'm thinking a lot about how we can continue
[3478.70 --> 3485.50]  to measure the sort of quality of the research that the community produces at that community-wide
[3485.50 --> 3491.42]  level, um, and what we can do going forward. What's the next iteration of the checklist going to be,
[3491.42 --> 3497.02]  for example. So that's what I'm thinking about. That's awesome. Yeah. And congrats on the, uh,
[3497.02 --> 3502.06]  the success with that and getting that out there and sort of self-propagating at this point.
[3502.06 --> 3506.30]  I also agree with you. There's a lot of papers, even you've mentioned in this conversation,
[3506.30 --> 3511.66]  too many papers for, for me to read in a, in a lifetime. Uh, there's, there's so much, uh,
[3511.66 --> 3517.02]  exciting stuff going on, but really appreciate both of you taking time to join us and discuss
[3517.02 --> 3522.54]  this really important topic. I hope, um, that people check out your, your paper, which we'll,
[3522.54 --> 3527.50]  uh, link in our show notes and, um, we'll link a bunch of the other things that Roy and Jesse,
[3527.50 --> 3533.82]  uh, talked about. So be sure to check those things out and, um, definitely, uh, spend some time. Uh,
[3533.82 --> 3539.82]  hope our listeners spend some time thinking about this topic and how it influences their workflow and
[3539.82 --> 3544.54]  other things. So thank you both. And, um, hope to, uh, talk to you again soon.
[3544.54 --> 3547.02]  Thank you so much. It was so much fun. Thanks for having us.
[3547.02 --> 3548.06]  Thanks for coming on the show.
[3551.90 --> 3557.58]  Thank you for listening to practical AI. If this is your first time, make sure you subscribe so you
[3557.58 --> 3563.90]  don't miss a thing. Head to practical AI.fm to subscribe or find us in Apple podcasts,
[3563.90 --> 3569.18]  Spotify, or wherever you listen to podcasts. And if you get value from the show,
[3569.18 --> 3573.02]  please do share it with a friend or a colleague. We appreciate you spreading the word.
[3573.82 --> 3578.70]  Practical AI is hosted by Daniel Whitenack and Chris Benson. It's produced by Jared Santo,
[3578.70 --> 3583.98]  and our music is provided by Breakmaster Cylinder. We are brought to you by some awesome sponsors.
[3583.98 --> 3589.82]  Shout out to Fastly, Linode, and LaunchDarkly. That is our show. We hope you enjoyed it,
[3589.82 --> 3602.54]  and we'll talk to you again next week.
[3602.54 --> 3604.54]  Bye.
[3604.54 --> 3606.54]  Bye.
[3606.54 --> 3608.54]  Bye.
[3608.54 --> 3610.54]  Bye.
[3610.54 --> 3612.54]  Bye.
