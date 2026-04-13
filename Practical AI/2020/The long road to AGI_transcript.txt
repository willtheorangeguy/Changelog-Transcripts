[0.94 --> 4.64]  Hello, this is your podcast co-host, Daniel Whitenack.
[5.06 --> 11.00]  I wanted to give a quick disclaimer before we jump into the content for this week, and
[11.00 --> 17.36]  that is that Chris and I recorded this episode a few weeks ago prior to when we had both
[17.36 --> 24.00]  seen the George Floyd video and all of the protests and calls for justice have happened
[24.00 --> 26.92]  in our country and really all around the world.
[26.92 --> 32.36]  The tone of this episode didn't really match what we thought would be appropriate for
[32.36 --> 36.36]  that particular week, and so we held off on releasing the content.
[36.90 --> 43.26]  We also shifted focus a little bit and recorded a new episode on explainability and bias in
[43.26 --> 45.74]  AI, and we released that last week.
[46.60 --> 53.54]  We're going to continue to try to bring a focus on explainability and bias and fairness
[53.54 --> 55.92]  in AI algorithms to the podcast.
[55.92 --> 61.78]  We both think that that's incredibly important, especially as more governments and police
[61.78 --> 65.78]  forces start using things like facial recognition in some cases.
[66.36 --> 72.18]  But we also want to make sure that we keep getting AI content out there, and so we're going
[72.18 --> 74.20]  to go ahead and release this episode.
[74.86 --> 81.82]  If you have questions about anything related to AI and policing and fairness and bias and
[81.82 --> 86.28]  all of those things, we'd love to have a discussion with you about that.
[86.78 --> 93.02]  You can reach out to us anytime on Twitter or on our Slack channel or on our LinkedIn page,
[93.52 --> 96.02]  and we'd love to have those discussions.
[96.26 --> 101.76]  I'd love to hear what you are thinking about our content and about AI and fairness and bias
[101.76 --> 102.36]  in general.
[102.36 --> 108.36]  So please reach out, and I hope that this episode is useful and beneficial for you.
[108.36 --> 114.32]  Bandwidth for Changelog is provided by Fastly.
[114.52 --> 116.60]  Learn more at Fastly.com.
[116.82 --> 119.92]  We move fast and fix things here at Changelog because of Rollbar.
[120.04 --> 121.72]  Check them out at Rollbar.com.
[121.96 --> 124.14]  And we're hosted on Linode Cloud servers.
[124.50 --> 126.48]  Head to linode.com slash Changelog.
[126.48 --> 131.78]  This episode is brought to you by DigitalOcean.
[132.24 --> 136.58]  DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you
[136.58 --> 136.88]  grow.
[137.24 --> 142.06]  They have an intuitive control panel, predictable pricing, team accounts, worldwide availability
[142.06 --> 148.56]  with a 99.99 uptime SLA, and 24-7, 365 world-class support to back that up.
[148.82 --> 154.28]  DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[154.28 --> 158.10]  Head to do.co slash Changelog to get started with a $100 credit.
[158.48 --> 160.56]  Again, do.co slash Changelog.
[168.06 --> 175.92]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[176.30 --> 177.26]  and accessible to everyone.
[177.56 --> 181.66]  This is where conversations around AI, machine learning, and data science happen.
[181.66 --> 186.14]  Join the community and Slack with us around various topics of the show at Changelog.com
[186.14 --> 188.04]  slash community, and follow us on Twitter.
[188.20 --> 189.80]  We're at Practical AI FM.
[196.38 --> 203.46]  Welcome to another fully connected episode of Practical AI, where Chris and I keep you fully
[203.46 --> 206.78]  connected with everything that's happening in the AI community.
[206.78 --> 212.88]  We'll take some time to discuss some of the things in the latest AI news, and we'll be
[212.88 --> 217.40]  digging into some learning resources to help you level up your machine learning game.
[218.12 --> 219.04]  I'm Daniel Whitenack.
[219.12 --> 224.56]  I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[224.56 --> 228.90]  Benson, who is a principal AI strategist at Lockheed Martin.
[229.32 --> 230.04]  How are you doing, Chris?
[230.08 --> 230.98]  How was the long weekend?
[231.58 --> 232.14]  I'm good.
[232.24 --> 234.18]  We're just coming out of Memorial Day weekend.
[234.64 --> 236.26]  You get to get outside a little bit.
[236.26 --> 237.26]  Did you stay socially distanced?
[237.26 --> 237.66]  I did.
[237.96 --> 240.26]  Of course, socially distanced, but outside?
[240.98 --> 246.10]  I did, and I was staying socially distanced, and I did that despite the fact that officially
[246.10 --> 248.20]  Georgia was the first state to open up.
[248.90 --> 249.88]  Yeah, that's true.
[250.10 --> 251.02]  And it was something weird.
[251.10 --> 254.04]  It was like pool halls and tattoo parlors or something.
[254.52 --> 255.90]  Everything about it was weird.
[256.46 --> 258.88]  And so, yeah, I mean, it really, really was.
[259.18 --> 262.10]  You look at the things and go, why did they choose that?
[262.28 --> 262.58]  Yeah.
[262.58 --> 262.66]  Yeah.
[263.20 --> 265.02]  Once upon a time pool halls, but no more.
[265.14 --> 266.04]  Not many a year.
[266.30 --> 266.82]  Yeah, yeah.
[266.86 --> 268.92]  I don't do tattoos, at least not yet.
[269.00 --> 270.36]  So maybe I should.
[270.74 --> 271.10]  Yeah.
[271.32 --> 273.00]  It's been a while on the pool hall.
[273.18 --> 279.54]  I think my advisor when I was at NCAR, after my undergrad, I did a high performance computing
[279.54 --> 285.74]  internship at NCAR in Boulder, and he was like all into pool and had, like he carried his
[285.74 --> 292.90]  like case with his pool cue, I guess that's what it's called, around at the lab and everything.
[293.16 --> 295.12]  So anyway, that's bringing back some memories.
[295.42 --> 296.66]  We have a pool table in our basement.
[296.82 --> 298.10]  So usually that's where we go for.
[298.10 --> 298.22]  Oh, wow.
[298.60 --> 300.60]  Sadly, you'd think that would make us quite good.
[300.66 --> 301.02]  We're not.
[301.22 --> 302.02]  But recreational.
[302.64 --> 302.78]  Yeah.
[302.78 --> 307.70]  It's strictly recreational and usually it is accompanied with plenty of lubrication in
[307.70 --> 308.56]  the alcoholic sense.
[309.08 --> 309.82]  Oh, gotcha.
[310.16 --> 310.38]  Yeah.
[310.44 --> 311.92]  It's kind of like we've had a couple of drinks.
[312.02 --> 313.96]  We're like, hey, let's go get a game of pool.
[314.10 --> 315.56]  And so, yeah, that's what we do.
[315.84 --> 316.04]  Yeah.
[316.34 --> 317.96]  Anything else exciting over the weekend?
[318.40 --> 321.24]  I had kind of a weird thing happen to me before we get started.
[321.24 --> 323.42]  So, you know, I do all this animal rescue stuff.
[323.58 --> 324.46]  You know, we've talked about that.
[324.90 --> 326.22]  And so I get a call.
[326.60 --> 329.28]  I'm probably the only person, you know, that has a snake hotline.
[329.28 --> 334.74]  So for our local area, so I go and help with that's one of the things I do is help out
[334.74 --> 337.16]  because people are afraid of venomous snake and other things.
[337.20 --> 341.94]  And I get a weird call about a garter snake, which is non-venomous, but it was it turned
[341.94 --> 346.00]  out to be quite a big one, about three feet, which is very large for that, that was stuck
[346.00 --> 348.90]  in netting, like yard netting that would keep straw down.
[349.32 --> 352.58]  And it was going to die because it was thoroughly entangled in it.
[352.76 --> 355.18]  And so I went to rescue without any gear.
[355.36 --> 356.12]  It was non-venomous.
[356.16 --> 357.06]  I wasn't too worried about it.
[357.06 --> 361.18]  But the snake, I forgot the fact the snake would be thinking I'm a hundred foot giant,
[361.32 --> 362.00]  relatively speaking.
[362.14 --> 366.80]  So as I spent 15 minutes cutting it out of the thing it was trapped in, it constantly
[366.80 --> 368.34]  bit me over and over again.
[368.70 --> 372.54]  And so they have tiny little teeth, but just enough to get blood.
[372.62 --> 373.54]  It doesn't really hurt.
[374.02 --> 375.70]  But he chewed on me for 15 minutes.
[375.80 --> 381.14]  So by the time I got him free, I looked like I was like an axe murderer with blood running
[381.14 --> 381.94]  all down my hand.
[382.04 --> 385.86]  So it was really, you know, it didn't hurt, but I was just, I looked at it, I was kind of
[385.86 --> 387.86]  going, this is just kind of a bizarre moment.
[388.06 --> 389.56]  So that was my Memorial Day.
[389.70 --> 393.18]  But here we are talking about AI now that I've dragged listeners through that.
[393.52 --> 396.22]  Speaking of snakes, this is an AI podcast.
[396.90 --> 398.36]  And this is a fully connected episode.
[398.36 --> 402.42]  So we can, you know, talk about whatever is on our mind in the AI world.
[402.60 --> 405.48]  I know there's been a variety of things going on.
[405.60 --> 408.36]  You know, some COVID things, some not COVID things.
[408.36 --> 409.66]  There's been conferences.
[409.66 --> 415.60]  iClear was recently around that was interesting that we just talked about the NVIDIA stuff,
[415.72 --> 418.08]  I think, in our last episode, which was interesting.
[418.20 --> 422.36]  My NVIDIA Xavier NX did come to my house, which I ordered.
[422.86 --> 425.16]  I'm excited to play with that, which I haven't yet.
[425.40 --> 430.28]  So maybe I'll give an update in a following episode about my experiences with that.
[430.44 --> 432.48]  But what else is on your mind?
[432.54 --> 434.36]  What's crossed your path in the AI world?
[434.36 --> 439.88]  Well, before we even go there on your NX thing, we should ask listeners about things
[439.88 --> 444.28]  that they are doing, interesting projects at some point, and maybe have an episode where
[444.28 --> 448.60]  we kind of talk about really interesting things people are doing, not really work related necessarily,
[448.86 --> 452.82]  but just things that are cool that they're doing that are very creative on how I would
[452.82 --> 454.26]  love to hear what people out there are doing.
[454.64 --> 454.72]  Yeah.
[454.80 --> 459.88]  If you have an interesting side thing or interesting, unique project, let us know.
[460.16 --> 460.82]  Reach out to us.
[460.86 --> 462.28]  We'd love to talk about it.
[462.28 --> 463.80]  It gives me some inspiration.
[464.68 --> 464.92]  Yep.
[464.96 --> 468.48]  We're on Slack and LinkedIn and Twitter and everywhere.
[468.68 --> 470.42]  You can reach us just about anywhere you might be.
[471.24 --> 472.00]  Yeah, for sure.
[472.16 --> 472.58]  For sure.
[473.16 --> 474.74]  So what else is on your mind, Chris?
[474.98 --> 478.90]  Well, I'll tell you what I was thinking about when we knew that we were going to start planning
[478.90 --> 479.26]  this.
[479.26 --> 483.36]  I've had something on my mind for a while, and that is that we've started to allude to
[483.36 --> 485.22]  it in recent episodes this year.
[485.80 --> 491.60]  And that is the fact that we're kind of getting to a turning point in the entire field of artificial
[491.60 --> 492.30]  intelligence.
[492.30 --> 498.34]  While we have been so very focused on deep learning for the last few years and pretty
[498.34 --> 502.66]  much the entire time we've been doing this podcast, we're starting to get to a point where
[502.66 --> 507.04]  a lot of the big advancements seem to have come out and we're seeing a lot of incremental
[507.04 --> 507.40]  stuff.
[507.50 --> 511.90]  And that's not to say we won't see some big advancements continue going forward, but it's
[511.90 --> 518.60]  kind of becoming a little bit mature in terms of there are models of various types, CNNs
[518.60 --> 520.10]  and in the NLP space.
[520.22 --> 523.28]  We've talked about BERT and all the others, GPT-2 and everything.
[523.92 --> 529.90]  But we're kind of finding ourselves focusing heavily on the next version of the same model
[529.90 --> 532.14]  to some degree and the variants that are there.
[532.64 --> 532.66]  Yeah.
[532.72 --> 534.86]  More data, more performance, sort of.
[534.86 --> 535.50]  Yeah, exactly.
[535.72 --> 539.98]  And I've been thinking, I've been hearing more and more about like truly advancing the
[539.98 --> 542.00]  state of the art on the research side.
[542.18 --> 547.86]  And that was really brought to the forefront a few months ago at the NURPS conference when
[548.46 --> 554.06]  I always butcher his name, but Yoshua Bengio, if I'm saying it correctly, and I apologize
[554.06 --> 554.92]  if I'm not.
[555.30 --> 561.42]  But he did a keynote at the open of the conference kind of talking about advancing the state of
[561.42 --> 564.48]  the art from kind of where we are now to where we could go.
[564.58 --> 566.70]  And he had one way of looking at that.
[566.94 --> 572.92]  And then separately in the work that I do at my employer, you know, we often have interactions
[572.92 --> 574.12]  and stuff with DARPA.
[574.32 --> 578.54]  And I've been really becoming very aware of the way DARPA is looking at the future.
[578.68 --> 582.52]  And I probably should, for those listeners who are not aware of it, I probably should real
[582.52 --> 583.84]  quick say what DARPA is.
[583.84 --> 588.44]  And that is DARPA is the Defense Advanced Research Projects Agency.
[588.80 --> 590.20]  And everyone calls it DARPA for short.
[590.20 --> 591.86]  Just rolls off the tongue.
[591.96 --> 592.28]  That's right.
[592.34 --> 592.96]  It's quite a name.
[593.36 --> 595.78]  But it's been around for over 60 years.
[596.06 --> 602.16]  It is the original organization that invented the internet, which was the very first incarnation
[602.16 --> 607.80]  of the internet as we know it today, was four nodes that were connected by the earliest
[607.80 --> 609.22]  version of the internet protocol.
[609.62 --> 612.86]  And the idea was distributed computing across a wide area.
[613.36 --> 615.26]  These were all happened in the test case.
[615.38 --> 616.62]  They were all in the same facility.
[616.62 --> 622.72]  But the idea was that it could survive nuclear holocaust and all that by having nodes go down
[622.72 --> 625.82]  and still have the overall system, the network itself operating.
[626.34 --> 628.78]  And so DARPA has always been incredibly cutting edge.
[629.04 --> 635.68]  And they're the ones that kind of lead at least the US government's military interests into
[635.68 --> 639.88]  the future, typically on a horizon that's like 15 to 20 years.
[639.88 --> 642.76]  So, you know, you'll see something happen.
[642.86 --> 643.98]  It'll get developed over time.
[644.02 --> 646.02]  And eventually it gets out there.
[646.22 --> 648.90]  And the internet's one really, that's the most famous example of it.
[649.00 --> 653.60]  So they are really looking forward from what we're, and we can describe all this later,
[653.72 --> 660.12]  but the idea of what they call wave two that we're in now to wave three, which is kind of
[660.12 --> 661.00]  the next incarnation.
[661.00 --> 665.82]  And between the NeurIPS talk and the DARPA perspective and a bunch of others that I've
[665.82 --> 670.04]  read from other sources, I just thought it was time for us to start thinking about what
[670.04 --> 671.06]  the future looks like.
[671.48 --> 673.46]  So I know we're practical AI.
[673.66 --> 678.42]  In this context, it may not be the practical of pulling out your pie torch and starting to
[678.42 --> 680.08]  work on a model on this episode.
[680.54 --> 685.78]  But I thought us talking about what we think it might mean to move into the future and where
[685.78 --> 690.92]  we might go and what we think of the current conversation might be a fun conversation to have.
[691.00 --> 691.66]  You up for it?
[691.92 --> 692.48]  Yeah, definitely.
[692.68 --> 696.32]  And I guess I can bring the practical side in here.
[696.48 --> 705.22]  I will admit that, you know, with any sort of conversation about like AGI or general intelligence
[705.22 --> 714.14]  or like next things, I often come in with a good amount of cynicism and probably don't
[714.14 --> 718.00]  give it the respect that it's deserved in terms of the discussion.
[718.00 --> 723.28]  But I will say that some of the stuff that you afford me and also the NeurIPS keynote,
[723.46 --> 726.26]  which we'll link to in our show notes, but it's definitely interesting.
[726.42 --> 732.62]  And there were elements of what he's talking about as far as system to AI and that sort
[732.62 --> 738.28]  of thing that are sort of rooted in things that are being explored and experimented with
[738.28 --> 739.58]  and that sort of thing.
[739.58 --> 747.58]  So it's not so much like Terminator scenario or like singularity talk, but more kind of
[747.58 --> 755.44]  like you're saying, pushing beyond the sort of very limited task oriented models to maybe
[755.44 --> 760.06]  something slightly differently or at least things that operate in a slightly different
[760.06 --> 760.36]  way.
[760.94 --> 766.88]  So, yeah, I'll try to get off of my limited imagination a little bit to discuss things.
[766.88 --> 768.78]  That's funny.
[769.10 --> 771.26]  People throw around this sort of term AGI.
[771.74 --> 777.08]  So your AI to AGI or artificial intelligence to artificial general intelligence.
[777.08 --> 782.62]  I know I was looking up some while you were talking, I was looking up some definitions that
[782.62 --> 784.86]  people kind of have out there for AGI.
[785.40 --> 788.66]  Probably a lot of them are fairly ridiculous.
[789.56 --> 790.08]  Not surprising.
[790.86 --> 794.92]  Open AI always talks about pursuing artificial general intelligence.
[794.92 --> 800.22]  And of course, OpenAI has been criticized in various ways.
[800.80 --> 807.16]  But I think that they're generally having good intentions in terms of how they're going
[807.16 --> 810.18]  about trying to push the state of the art and that sort of things.
[810.38 --> 810.58]  I agree.
[810.70 --> 811.50]  And we need that.
[811.72 --> 812.22]  We need that.
[812.28 --> 812.84]  Yeah, definitely.
[813.04 --> 813.70]  That aspiration.
[814.12 --> 814.48]  Exactly.
[814.68 --> 816.66]  So no organization is perfect.
[816.66 --> 823.96]  But I think they do a really good job at trying to get people thinking about new things and
[823.96 --> 825.46]  creative ways of going about things.
[825.56 --> 830.72]  And anyway, on their page, their sort of about page, they talk about artificial general
[830.72 --> 831.38]  intelligence.
[832.04 --> 839.66]  And what they mean by it is highly autonomous systems that outperform humans at most economically
[839.66 --> 841.06]  valuable work.
[841.06 --> 847.86]  I've seen other so I saw other definitions about how like or that sort of horizon of where
[847.86 --> 856.92]  we're shooting towards is intelligence that is able to learn across, you know, human tasks
[856.92 --> 863.94]  at human level, which right now we're at a very sort of specific task oriented model stage
[863.94 --> 869.06]  where like I have a really good machine translation model that translates, you know, English to French
[869.06 --> 870.06]  or something like that.
[870.60 --> 870.78]  Right.
[871.14 --> 874.18]  Not in all cases, but generally it's very specific.
[874.18 --> 879.54]  Like that model is very specifically limited to that specific task and it's not going to
[879.54 --> 880.42]  do anything else.
[880.42 --> 880.68]  Right.
[880.70 --> 889.50]  It's not going to sort of easily generalize to any sort of other human task other than translating
[889.50 --> 891.14]  English to French.
[891.14 --> 893.94]  And, you know, of course, there's multilingual models and all that.
[894.06 --> 895.56]  I totally realize that now.
[895.56 --> 901.78]  Um, but I think in general, like the, the things that we focused on as a community have
[901.78 --> 904.06]  been those sort of task oriented things.
[904.06 --> 908.42]  I don't know if you have a thought on AGI and what that means, but I do.
[908.54 --> 912.42]  And another, just to throw a couple of other buzzwords we hear associated with these as I
[912.42 --> 916.92]  answer this is the kind of narrow modern deep learning is often called weak AI, whereas
[916.92 --> 920.20]  the idea of AGI is strong.
[920.20 --> 925.56]  And so I think both you and I have had a habit of kind of scoffing over time a little bit
[925.56 --> 926.20]  at the AGI.
[926.94 --> 927.44]  We'll admit it.
[927.50 --> 928.20]  Yeah, we do.
[928.36 --> 930.16]  And part of it comes from working in this field.
[930.32 --> 936.28]  And that is, you know, as working people in artificial intelligence, the sex appeal quickly,
[936.34 --> 939.48]  you know, drops away that it appears to be from the outside.
[939.48 --> 946.16]  And you are grinding through working with data and you are trying to create models and testing
[946.16 --> 947.46]  them and trying to fix it.
[947.54 --> 950.30]  And it's no different from any other type of engineering.
[950.62 --> 952.62]  You know, essentially you're getting work done.
[952.94 --> 957.90]  And I know both of us are also software developers and there's a lot in common.
[958.04 --> 962.20]  You know, it's, it's a very bread and butter kind of thing, which most people don't think
[962.20 --> 965.16]  of AI as about, but when you're working in the field, it really is.
[965.16 --> 970.54]  Yeah, I tell people like, it's not like you stick your laptop in a corner and sprinkle
[970.54 --> 974.84]  some fairy dust over it and it becomes sentient and like starts learning, right?
[975.16 --> 978.20]  Essentially what we're doing is a very dumb thing.
[978.30 --> 979.82]  We're doing trial and error, right?
[980.04 --> 980.36]  Absolutely.
[980.64 --> 984.12]  We have a bunch of data, a bunch of examples for a specific task.
[984.46 --> 990.10]  And even though the models are very sophisticated in the definition and the way that people have
[990.10 --> 994.22]  defined the model from sort of input data to output data.
[994.22 --> 998.72]  At the end of the day, it's a bunch of parameters that we're training by trial and error in most
[998.72 --> 999.58]  cases, right?
[999.66 --> 1000.42]  Not all cases.
[1000.76 --> 1001.42]  Totally agree with that.
[1001.88 --> 1007.54]  And I think, and it's easy to lose sight of that because it is a very practical hands-on,
[1007.72 --> 1011.56]  you know, scientific job that we're doing here in its various forms.
[1011.70 --> 1017.16]  And so, you know, historically we look at AGI, artificial generalized intelligence, and we
[1017.16 --> 1021.40]  kind of go, oh my gosh, you know, robots that are talking to us the way they do in Hollywood
[1021.40 --> 1022.76]  movies that's so far away.
[1022.88 --> 1027.50]  We all know that because we know, we understand exactly what needs to happen and stuff to get
[1027.50 --> 1030.26]  there in the sense of, I shouldn't even say what needs to happen.
[1030.62 --> 1032.38]  We know that there's a lot that we don't know.
[1032.48 --> 1033.30]  I should put it that way.
[1033.40 --> 1036.22]  There's so many things that we're just not there yet on.
[1036.44 --> 1038.54]  And so it looks like a very distant horizon.
[1039.16 --> 1045.36]  But what we sometimes leave sight of as engineers working with the here and now of our tool set
[1045.36 --> 1050.44]  is that it is coming and we are actually very rapidly moving in that direction.
[1050.64 --> 1054.80]  There may be a long road from here to there, but we are moving along that road quite rapidly.
[1055.28 --> 1056.88]  And it's an evolutionary process.
[1057.08 --> 1060.74]  And there's a whole bunch of baby steps that get us from here to there.
[1061.24 --> 1064.66]  And if you lose sight of the baby steps, you're like, oh my God, that's science fiction.
[1064.76 --> 1065.46]  We're never going to get there.
[1065.52 --> 1067.06]  But we are slowly working our way.
[1067.30 --> 1070.98]  And in the short time you and I have been doing this podcast, you know, we're almost to
[1070.98 --> 1073.18]  a couple hundred episodes as we're having this one.
[1073.40 --> 1078.22]  We're now into the 90s and the field has changed dramatically in the time that you and I have
[1078.22 --> 1079.44]  been doing this show.
[1079.98 --> 1083.70]  And so as we look at that and try to figure out where we're going, and we're getting a
[1083.70 --> 1088.18]  call from luminaries now about turning that page into the next things.
[1088.48 --> 1094.00]  So that was really what I wanted to start talking a little bit about on this episode is just give
[1094.00 --> 1098.12]  us a little bit of context for the future and where we would go next.
[1100.98 --> 1130.96]  Thank you.
[1130.98 --> 1134.92]  Join more than 15,000 enthusiastic readers.
[1135.20 --> 1137.34]  It'll cost you exactly zero dollars.
[1137.70 --> 1141.38]  And you can subscribe right now at changeball.com slash weekly.
[1141.38 --> 1163.16]  So one of the things that I enjoyed about some of the material that I was looking at when
[1163.16 --> 1167.10]  you pointed me to the NURPS talk and then I followed some additional links after that and
[1167.10 --> 1172.78]  was exploring things is this idea of system one versus system two thinking.
[1173.04 --> 1179.76]  I think this is an idea that was developed in a book by leading economists thinking fast
[1179.76 --> 1180.30]  and slow.
[1180.44 --> 1188.48]  This idea of system one thinking, which are those things that we as humans think about or
[1188.48 --> 1193.80]  the tasks that we do that don't really require any sort of slow thinking or we don't have
[1193.80 --> 1195.24]  to slow down to figure it out.
[1195.24 --> 1195.48]  Right.
[1195.48 --> 1200.42]  Like I have my coffee cup by my desk and I want to take a drink.
[1200.42 --> 1203.32]  So I just pick up the cup and I and I take a drink.
[1203.32 --> 1208.62]  I don't have to think about like spend, you know, take a moment, get out the chalkboard,
[1208.86 --> 1213.26]  like write out how I'm going to think how I'm going to pick up the coffee cup, you know,
[1213.32 --> 1218.12]  write some papers and academic journals about my unique method for doing it.
[1218.22 --> 1219.38]  And, you know, then do it.
[1219.48 --> 1221.30]  It's just kind of something that I just pick up.
[1221.54 --> 1223.04]  I don't even have to expend.
[1223.04 --> 1228.06]  Like I have to have the thought to pick it up and I have to do the motion, but I don't
[1228.06 --> 1231.16]  have to slow down my life to think about how to do it.
[1231.26 --> 1231.42]  Right.
[1231.74 --> 1232.26]  That's true.
[1232.82 --> 1233.50]  Thank goodness.
[1233.62 --> 1233.92]  System two.
[1234.30 --> 1234.56]  Yeah.
[1235.04 --> 1242.04]  Well, in most cases, maybe in system two thinking, some of the words that were used as related
[1242.04 --> 1251.10]  to that in Yeshua's talk and in other articles were slow, logical, sequential, conscious, linguistic,
[1251.10 --> 1253.08]  algorithmic planning, reasoning.
[1253.40 --> 1258.86]  So this idea that there are those times in our lives as humans where hopefully most of
[1258.86 --> 1263.48]  us do think about more complicated things than picking up a coffee cup.
[1263.70 --> 1270.16]  We have to reason through certain problems to come up with a solution that is a sort of
[1270.16 --> 1274.06]  unique solution, maybe something we haven't experienced before.
[1274.06 --> 1281.76]  It's expressed in terms of, you know, maybe linguistic elements or, you know, logical steps
[1281.76 --> 1283.86]  or a sequence of things.
[1283.86 --> 1291.02]  And of course, some of these words, like the sequential side of things, the logical side
[1291.02 --> 1297.86]  of things, of course, these are associated with some of these ideas that, you know, like
[1297.86 --> 1300.10]  I mentioned, OpenAI and others are exploring.
[1300.10 --> 1308.94]  Like if you think of a sequential series of steps that you have to put some logic into and
[1308.94 --> 1314.12]  execute with sort of not that much feedback, well, we're starting to think about like reinforcement
[1314.12 --> 1321.00]  learning, which is a sort of sequential decision making process where you get rewards from your
[1321.00 --> 1326.02]  environment and you actually can modify your environment in some cases.
[1326.02 --> 1331.70]  And so some of these words definitely get to those things that, you know, people are trying
[1331.70 --> 1333.64]  to push the boundaries of.
[1334.24 --> 1338.00]  Was that idea of the different ways of thinking, did that resonate with you as well?
[1338.28 --> 1339.08]  It did.
[1339.22 --> 1343.42]  And it's funny, that book in particular, I've had it on my Kindle for a while and I need
[1343.42 --> 1344.36]  to dive into it.
[1344.42 --> 1344.62]  Yeah.
[1344.78 --> 1346.28]  Knowing I keep hearing how good it is.
[1346.54 --> 1348.12]  You need to think slow about it.
[1348.22 --> 1350.04]  I need to think slow about the book.
[1350.12 --> 1350.54]  There you go.
[1350.58 --> 1352.08]  And I'll read the slow through as well.
[1352.08 --> 1357.86]  But we definitely are at a moment where we've done amazing things in deep learning over the
[1357.86 --> 1358.56]  last few years.
[1358.78 --> 1364.28]  But I think we're all pretty aware that it is clearly nothing like we act as humans in
[1364.28 --> 1366.02]  terms of the way we process information.
[1366.78 --> 1372.96]  And you named a lot of that is the idea of something that requires your attention and your
[1372.96 --> 1376.78]  consciousness, both of which are core ingredients for system two.
[1376.78 --> 1382.54]  As we define what those mean, like with attention, it's the ability to focus on one or just a
[1382.54 --> 1383.74]  few elements at a time.
[1383.98 --> 1389.10]  And we've seen that now crop up in a variety of deep learning algorithms at a kind of a
[1389.10 --> 1389.58]  basic level.
[1389.70 --> 1395.50]  It's definitely in some NLP areas and you're seeing it pop up in others as well based on
[1395.50 --> 1396.08]  those successes.
[1396.72 --> 1401.54]  And so, and the ability to kind of have, you know, what they're referring to as soft attention,
[1401.54 --> 1407.48]  which essentially allows you to focus on the things that you need, but they also evolve
[1407.48 --> 1408.10]  over time.
[1408.10 --> 1411.16]  And it's very much kind of encompassed by the idea of short-term memory.
[1411.50 --> 1417.34]  And Yeshua notes that attention is an internal action and it needs a learned attention policy.
[1417.48 --> 1423.98]  And so, you know, all this kind of starts also feeding into consciousness in terms of
[1423.98 --> 1429.30]  if you think of consciousness not as a wishy-washy thing, and I'm just horrified, by the way,
[1429.30 --> 1433.54]  as an aside, at how poorly I'm doing explaining this after seeing his amazing keynote.
[1434.76 --> 1435.84]  You're doing beautiful.
[1435.98 --> 1436.66]  Oh my gosh.
[1436.80 --> 1439.20]  I'm taking a master's work and just killing it.
[1439.94 --> 1444.62]  But he talks about the need for consciousness to be defined computationally.
[1444.68 --> 1450.44]  And so not to be this kind of wishy-washy, ethereal idea, you know, that we think of it as typically
[1450.44 --> 1454.78]  in our daily life, but something that you can identify algorithmically.
[1455.06 --> 1457.94]  You know, the nature of consciousness is very short-term in memory.
[1457.94 --> 1459.36]  It requires attention.
[1459.62 --> 1464.18]  You look at something and the fact that we are going from moment to moment there, if
[1464.18 --> 1469.04]  you put that into a neuroscientific context, that that is what allows us to do what we're
[1469.04 --> 1472.92]  doing right now, you know, to have this conversation and to do all the things that make us human
[1472.92 --> 1473.80]  in our daily lives.
[1473.94 --> 1481.60]  But we are approaching a time when we can, with a very strict definition, potentially
[1481.60 --> 1486.86]  define what consciousness is and understand how attention and consciousness relate in a neuroscientific
[1486.86 --> 1487.70]  and human standpoint.
[1487.70 --> 1493.22]  And that is what is being codified as the idea of system two in a machine learning context where
[1493.22 --> 1494.22]  we're starting to track that.
[1494.34 --> 1500.12]  So as I listened to that keynote a few months ago when he gave it in December, I was really
[1500.12 --> 1507.38]  struck by the fact that the science that we've put our careers into is really shooting
[1507.38 --> 1507.86]  along.
[1507.86 --> 1512.86]  And we're not that far from certain areas that we may be able to computationally understand
[1512.86 --> 1514.34]  in a strict manner.
[1514.90 --> 1520.34]  And so that's, like I said, one of those first evolutionary steps that might take us toward
[1520.34 --> 1521.68]  that longer path toward AGI.
[1521.68 --> 1530.10]  Yeah, I was kind of struck when he started talking about consciousness and then brought in this idea
[1530.10 --> 1530.74]  of attention.
[1531.24 --> 1541.06]  And I think that it's certainly useful to think about sort of how to build a machine or intelligence
[1541.06 --> 1549.72]  that is conscious of the things it needs to be conscious of to do more complicated tasks,
[1549.72 --> 1552.84]  like the system two sorts of learnings and that sort of thing.
[1553.64 --> 1559.86]  So personally, and, you know, this is partly my own opinions and partly my faith and my own
[1559.86 --> 1565.78]  values is that, you know, I think that that sort of smaller scale consciousness, which can
[1565.78 --> 1571.20]  be quantified, is still vastly different than what, you know, makes a human a human.
[1571.56 --> 1573.70]  And that's another discussion that we can have.
[1573.70 --> 1581.46]  So I think that there is, you know, human value that's separate from that sort of small scale
[1581.46 --> 1585.40]  consciousness that allows you to do these more complicated tasks.
[1585.86 --> 1588.32]  So that's my own sort of thought on that.
[1588.44 --> 1597.20]  But I do think it is really useful to define some measure, whatever we want to call that,
[1597.28 --> 1601.42]  whether, you know, consciousness is a loaded term for some people or not,
[1601.42 --> 1607.30]  to define some sort of entity, which is that sort of entity that allows us to push
[1607.30 --> 1612.44]  machine intelligence to these sort of larger scale problems.
[1612.68 --> 1617.38]  I think that, you know, like you say, practitioners who work in this every day,
[1617.72 --> 1625.72]  there's such a long road to like intelligence that would even generalize to many of these
[1625.72 --> 1631.52]  sort of system two tasks that, you know, I don't think we're in any danger of like these sort of
[1631.52 --> 1635.40]  apocalyptic scenarios that people like to think about.
[1635.60 --> 1641.66]  But, you know, I think it is useful to think about like, what is that entity that helps us build up
[1641.66 --> 1643.58]  these more complicated tasks?
[1644.02 --> 1644.30]  I agree.
[1644.50 --> 1651.68]  It's a matter of fact, just as a note, the time horizon to get to AGI has so many steps between
[1651.68 --> 1657.18]  here and there, and it will likely be long enough out, whatever that time length is.
[1657.50 --> 1662.52]  I can totally understand why people would doubt that we're ever going to get there.
[1662.74 --> 1665.80]  And a while back, you know, I do this Atlanta deep learning meetup.
[1665.96 --> 1671.50]  And a while back, we had dueling sessions where I was kind of arguing toward
[1671.50 --> 1674.24]  why we would get to the concept of AGI.
[1674.70 --> 1680.08]  Another friend of mine there took a different session and argued why that was just fantasy.
[1680.08 --> 1683.16]  And I still think I'm right on that, no surprise.
[1683.50 --> 1688.76]  But I can totally get why he would not think that that is a realistic thing.
[1688.94 --> 1693.98]  And that is because as we do what we do as practitioners, it is so many steps out.
[1694.12 --> 1695.02]  It feels infinite.
[1695.16 --> 1697.34]  It feels like that thing that you're never going to reach.
[1697.80 --> 1699.56]  And so I'm sympathetic to people.
[1699.78 --> 1703.26]  I think that the work we're doing right now and all the work we've done in deep learning,
[1703.26 --> 1709.12]  as different as that is from the neuroscience of a human brain, that it's still incremental
[1709.12 --> 1710.18]  steps to get us there.
[1710.26 --> 1713.20]  We are learning from what is working and what is not working.
[1713.40 --> 1717.38]  And we are learning from the unexpected, you know, side effects and things like that.
[1717.38 --> 1721.14]  And every little bit of that pushes us farther down that road.
[1721.86 --> 1724.68]  So I do think we're eventually going to get there.
[1724.74 --> 1728.78]  And I think there's giant implications, which we can talk about a little bit later in this episode,
[1728.78 --> 1733.00]  about what that means and, you know, legal aspects and all that other stuff around it.
[1733.88 --> 1739.40]  Yeah, I think that one other example, which I think good to talk about examples here too
[1739.40 --> 1743.02]  and make things concrete is I work with our chief research officer.
[1743.02 --> 1744.30]  His name is Gary Simons.
[1744.42 --> 1746.76]  And he's just a really fascinating guy.
[1746.76 --> 1753.22]  He was actually the first linguist to take a computer into the field to do linguistics,
[1753.42 --> 1756.78]  which was like basically a suitcase computer that he built himself.
[1756.78 --> 1759.34]  And then there was no word processor, right?
[1759.38 --> 1764.38]  So he programmed his own word processor to do linguistics, you know, in the field in Papua
[1764.38 --> 1765.86]  New Guinea on this computer.
[1766.26 --> 1771.62]  Like he's been in the game a long time and has continually just innovated over time.
[1771.76 --> 1778.12]  But, you know, I was talking to him and showing him some of these things when GPT-2 came out
[1778.12 --> 1786.34]  from OpenAI and like the text generation capability of those large scale language models and, you know,
[1786.42 --> 1792.28]  paragraphs of generated text that were logical and made sense and like connected certain points.
[1792.28 --> 1798.32]  And again, this is using this attention mechanism, which is popular in these sorts of models and was referenced
[1798.32 --> 1800.84]  in the keynote at NeurIPS and all of that.
[1800.84 --> 1807.60]  And, you know, he made the comment to me like he thought this sort of thing was impossible.
[1807.60 --> 1813.52]  Like, you know, this sort of generation of text by a machine in this sort of logical way
[1813.52 --> 1817.54]  was something beyond what he would see in his lifetime for sure.
[1817.66 --> 1822.16]  And so I definitely think you're right that these sort of mechanisms and that comes about
[1822.16 --> 1827.78]  by thinking of, OK, you know, what sort of mechanism do we need to push things further?
[1827.78 --> 1833.52]  Well, attention was developed and this, you know, self-attention and transformers.
[1833.86 --> 1837.06]  And that pushed those systems to this new sort of level.
[1837.62 --> 1842.66]  And so I think that there's going to be continue to be those things that are developed and it
[1842.66 --> 1844.60]  requires a different way of thinking.
[1845.20 --> 1846.36]  So, yeah, it's a good point.
[1846.36 --> 1859.46]  We deserve a better Internet and the Brave team has the recipe for bringing it to us.
[1859.62 --> 1860.60]  Start with Google Chrome.
[1860.84 --> 1864.54]  Keep the extensions, the dev tools and the rendering engine that make Chrome great.
[1864.76 --> 1865.62]  Rip out the Google bits.
[1865.76 --> 1866.40]  We don't need them.
[1866.76 --> 1869.26]  Mix in ad and tracker blocking by default.
[1869.54 --> 1874.14]  Quick access to the Tor network for true private browsing and an opt-in reward system.
[1874.14 --> 1876.96]  So you can get paid to view privacy respecting ads.
[1877.06 --> 1880.92]  Then turn around and use those rewards to support your favorite web creators like us.
[1881.26 --> 1885.82]  Download Brave today using the link in the show notes and give tipping a try on ChangeDog.com.
[1896.86 --> 1900.88]  So I wanted to talk about the other thing that we introduced at the beginning,
[1900.88 --> 1903.02]  and that was the DARPA perspective.
[1903.30 --> 1907.24]  And I introduced DARPA for the purpose of making sure everybody was on board with what that was.
[1907.66 --> 1911.86]  But it's really interesting to see them kind of looking out.
[1912.02 --> 1916.14]  And so it's a great lens, you know, to read up on what DARPA is doing
[1916.14 --> 1920.42]  and what kinds of solicitations and announcements they're making out there in the public space.
[1920.42 --> 1926.76]  Because you may be able to infer kind of where things are going over the next decade or two in doing that.
[1926.76 --> 1927.68]  Because that's their mission.
[1927.90 --> 1931.54]  And it's kind of funny, you know, kind of the Hollywood-ish version of DARPA
[1931.54 --> 1934.52]  is though it was another like a spy agency or something.
[1934.76 --> 1936.90]  And, you know, I was reading...
[1936.90 --> 1938.12]  Men in Black sort of stuff.
[1938.24 --> 1938.80]  Yeah, really.
[1939.14 --> 1939.92]  There was a...
[1939.92 --> 1940.78]  I won't name the book.
[1940.90 --> 1942.06]  I'm not sure if I can remember it.
[1942.06 --> 1943.56]  But a friend of mine asked me to read a book.
[1943.56 --> 1948.28]  And I stopped at the first chapter because the whole premise of the book was like DARPA,
[1948.46 --> 1952.78]  which was like this spy agency, was sending agents out into the field to do nefarious things.
[1952.82 --> 1953.96]  And I was like, I just can't take that.
[1953.96 --> 1954.70]  It's just...
[1954.70 --> 1955.36]  It's so far from...
[1955.36 --> 1955.42]  Yeah.
[1955.84 --> 1958.54]  What DARPA is essentially, and this is almost...
[1958.54 --> 1961.10]  It probably will offend them to dumb it down this much,
[1961.42 --> 1964.20]  but it's essentially a giant project management office.
[1964.82 --> 1969.94]  And, you know, their mission is to look at what are the next great technologies
[1969.94 --> 1972.14]  that are going to lead us into the future.
[1972.54 --> 1976.42]  And many of those things, even though they may be looking with a military view,
[1976.70 --> 1979.62]  end up out in the general population just as the internet did.
[1979.70 --> 1982.78]  And so it really does affect our daily life eventually.
[1982.78 --> 1987.10]  And so they have a $3.5 billion annual budget,
[1987.24 --> 1991.34]  which is a nice hefty little sum of cash to go try to figure out the future with.
[1991.58 --> 1997.54]  And another really cool thing that they do is that it's impossible to be a career DARPA manager.
[1997.86 --> 1998.62]  They do rotations.
[1999.02 --> 2001.74]  And I forget what the exact time limit is.
[2001.88 --> 2003.42]  I think it's four years, might be three.
[2003.80 --> 2006.84]  But you never can bet your career on your DARPA performance.
[2007.08 --> 2010.12]  And the reason they do that is they want people to take risks.
[2010.12 --> 2016.70]  They want people to be willing to make big bets without it being something that will destroy their career.
[2016.86 --> 2019.80]  So it's the safe place to do really revolutionary work.
[2020.36 --> 2021.04]  And that happens.
[2021.34 --> 2025.50]  And they essentially, the entire organization is a bunch of project management offices and stuff.
[2025.50 --> 2032.32]  So the reason I say all that is that they have kind of, it's been, it's actually not terribly recent.
[2032.40 --> 2033.54]  It was back in 2018.
[2034.24 --> 2037.68]  They released a PDF that's open to the public.
[2037.78 --> 2040.06]  Anybody can look it up called the Three Waves of AI.
[2040.20 --> 2041.74]  And you can Google it and find it instantly.
[2041.74 --> 2048.98]  And it basically segregates the history as they see it of what AI is and is going toward.
[2048.98 --> 2053.72]  And the Three Waves, and if you think of the past one, is what they call handcrafted knowledge.
[2054.18 --> 2055.28]  And I'll talk about that in a moment.
[2055.50 --> 2058.10]  The kind of the current one that we're in is statistical learning.
[2058.42 --> 2064.02]  And then the future that they're talking about, the third wave of AI, is called contextual adaptation.
[2064.02 --> 2080.60]  And I think that the short, quick version of each of those is that if you have a set of attributes about how sophisticated you're getting with your AI in terms of perceiving, learning, abstracting, and reasoning, and how far each technology can go that we're at.
[2080.92 --> 2087.48]  And if you think like an example of first wave, which was previous before we got to the current deep learning period, would be like an expert system.
[2087.82 --> 2091.58]  And that's where you eventually capture a whole bunch of rules into a system.
[2092.12 --> 2093.80]  And you have a flow that goes through them.
[2093.80 --> 2095.04]  But it's a rule-based system.
[2095.14 --> 2096.14]  So it's not inference.
[2096.14 --> 2099.00]  It's not prediction in the way that we think of it today.
[2099.42 --> 2100.34]  It's not statistical.
[2100.34 --> 2101.90]  It's following a set of rules.
[2102.38 --> 2112.08]  And then, you know, we eventually got to this point that we're at now where we've been in this amazing deep learning revolution of recent years, which they refer to as the second wave of AI.
[2112.36 --> 2116.28]  And in particular, things like perception and learning have come a long way of that.
[2116.42 --> 2119.26]  We haven't made so much progress in abstracting and reasoning.
[2119.26 --> 2123.16]  But, you know, the idea is that we are learning.
[2123.36 --> 2133.32]  And we have been, even in the short time we've been doing this over the last few years, we've come a very, very long way in terms of what we can do with those statistical capabilities.
[2133.32 --> 2140.76]  But as we started this episode with, we're starting to get a little bit mature about, you know, where we've gotten to.
[2140.82 --> 2145.32]  And we're starting to see many versions of the same models and technology coming out.
[2145.32 --> 2160.80]  So what DARPA is really looking for are organizations, academic, industry, within the military itself, that are interested in this idea of contextual adaptation, where you're essentially pushing all of those characteristics as far as you can.
[2160.80 --> 2177.26]  And you're able to perceive, form a contextual model and learn, abstract, reason, and really all of those concepts that really lead eventually to the AGI concept that we've been talking about are seeing at least the next stage of realization.
[2177.52 --> 2179.40]  There may be many waves after this potentially.
[2179.40 --> 2188.22]  But it's kind of taking us from where we are now in 2020 as we record this into the next, you know, some odd years of what this is likely to be.
[2188.36 --> 2193.10]  And so that framework, I keep coming back to that in my own professional life.
[2193.10 --> 2201.56]  And I think it's really important that we start recognizing that maybe we're seeing a fairly mature statistical learning, you know, marketplace, if you will.
[2201.56 --> 2204.68]  And people are able to put into production all these great deep learning models.
[2204.68 --> 2214.02]  But a lot of the really cool research, as we saw with that Neurop's keynote, are now focused on what in this context would be third wave and what in that context was system two.
[2214.84 --> 2215.00]  Yeah.
[2215.26 --> 2224.06]  Since we're talking a lot about generalization and also perceiving an environment and making sequential series of decisions.
[2224.06 --> 2235.52]  So solving these sort of longer or thinking slow type problems, it seems like a lot of the time when they're referring to these things, my mind seems to go to reinforcement learning.
[2235.92 --> 2238.96]  And I know that that's something, obviously, that OpenAI is working on.
[2239.02 --> 2244.04]  But it also strikes me that like reinforcement learning is not a new thing.
[2244.04 --> 2244.56]  Right.
[2244.60 --> 2249.02]  It's been around since whatever the 1950s, I think, even as an idea.
[2249.02 --> 2268.88]  So I wonder, like, if that's a big piece of this sort of third wave or system two thinking or whatever, however it's framed, if that's so valuable, why has it not pushed forward more rapidly into kind of standard practice and practical implementations?
[2268.88 --> 2278.94]  And it's still like playing Atari sort of scenario and maybe not as practical as a lot of data scientists using it and that sort of thing.
[2279.56 --> 2284.56]  You think that's because of the models that are being used within the reinforcement learning framework?
[2284.56 --> 2287.90]  Or is it because, you know, attention wasn't placed on it or?
[2287.90 --> 2295.90]  Well, actually, before we go too far, and I'll answer that, but we probably should note, you want to real quick define what reinforcement learning is for anyone out there that doesn't know?
[2295.90 --> 2309.06]  Yeah. So reinforcement learning is where you have an agent and an environment and your agent executes what's called a policy to make actions in an environment.
[2309.06 --> 2326.30]  So if you imagine, like, trying to play a game or if you imagine, like, you're trying to, you know, route a car through traffic from destination A to B, this is a scenario where you have a kind of goal or there's something you're trying to do, but it's not clear.
[2326.30 --> 2331.82]  There might be multiple sort of routes that get you there with the same sort of reward.
[2332.34 --> 2337.76]  And also the actions that you take actually influence your environment around you, right?
[2337.76 --> 2343.18]  Like if I change lanes to my right, then, you know, other people respond in traffic, right?
[2343.22 --> 2347.58]  So you've got this agent, which is acting in an environment which it can actually influence.
[2347.58 --> 2359.98]  And so at each time step of reinforcement learning, when you're performing reinforcement learning, the agent makes an action based on a policy that tries to determine its future reward.
[2360.64 --> 2366.92]  And then the environment, you know, responds to that action with a reward and a next state of the environment.
[2366.92 --> 2369.36]  And you kind of loop through this cycle.
[2369.36 --> 2373.48]  And so this is used in robotics and other places.
[2373.68 --> 2385.56]  But, you know, it seems like most data scientists I talk to that are even applying some of these more advanced AI models are not yet really thinking about reinforcement learning.
[2385.56 --> 2401.90]  I guess my question is kind of getting towards like if that's to become a more pillar of this sort of new way of thinking, is that just because we haven't been trying to solve those types of problems or the models applied within reinforcement learning weren't good enough yet?
[2401.90 --> 2407.90]  Well, it's only my opinion, but my sense of it is that we're still early days on reinforcement learning.
[2408.40 --> 2425.42]  And this current incarnation, by the way, that we talk to take any confusion away from people is called deep reinforcement learning, where we're applying, you know, the traditional deep learning ideas, such as having, you know, a bunch of nodes that are connected and you have a, you know, like back propagation that is doing error control.
[2425.42 --> 2434.26]  And applying that within this learning model, which we call reinforcement learning, which wasn't always had it originally had nothing to do with deep learning.
[2434.40 --> 2435.86]  So we took something that existed.
[2436.10 --> 2438.38]  Yeah, it's independent of what type of model you use.
[2438.62 --> 2449.98]  And we've retrofitted it with deep learning capabilities in that, which gives it this statistical, you know, graph of possibilities, which basically extends what's possible with the model, makes it a lot more granular.
[2449.98 --> 2451.80]  And I think we're very early days.
[2451.90 --> 2461.04]  I think that like you and I have been in a unique position to see as part of this podcast, even all of the different uses that you could use deep learning for.
[2461.18 --> 2465.64]  You know, we had guests from Google that were using it in ways that I had not thought about.
[2466.00 --> 2467.14]  Obviously, there's robotics.
[2467.40 --> 2473.24]  We just heard about, I recall there was a Pac-Man example where Pac-Man had been observed for a while.
[2473.34 --> 2478.18]  And then was it Pac-Man or that was essentially reinventing the game from just observing it for a period of hours.
[2478.18 --> 2480.46]  But I think we're really early days.
[2480.56 --> 2486.80]  And I think it's a transitional technology, a transitional type of model that takes us a little bit forward.
[2487.00 --> 2496.84]  I don't think it lines up perfectly with like the deep learning versions of NLP and, you know, CNNs, which are kind of the deep learning version of machine vision.
[2497.24 --> 2504.68]  So this is one of those evolutionary moments where we're having a technology that helps us take, you know, half a step forward from where we already were.
[2504.84 --> 2506.10]  And we'll keep building on it.
[2506.10 --> 2509.66]  So I think we're going to see a lot more happening in reinforcement learning in the years ahead.
[2509.76 --> 2510.88]  And at least that's my expectation.
[2510.88 --> 2513.64]  Yeah, yeah, I definitely am looking forward to it.
[2513.72 --> 2520.36]  I know it was at a event in Chicago before all everything got locked down.
[2520.36 --> 2536.50]  And in that event, a guy was presenting about application of reinforcement learning in a marketing context to manage like how they executed their marketing campaigns in terms of do we use this campaign combination with this campaign?
[2536.50 --> 2539.66]  And how is that going to influence next week's sales?
[2539.84 --> 2541.92]  And then this campaign with that campaign.
[2542.06 --> 2546.08]  And they're managing like seven different campaigns and over weeks and weeks.
[2546.20 --> 2550.96]  And this is a sort of sequential thing they have to manage and figure out and simulate.
[2551.22 --> 2552.44]  And I found it interesting.
[2552.44 --> 2556.92]  So I haven't heard a lot of that sort of filtering into those.
[2557.28 --> 2561.38]  And that was a more, I guess, practical industry application event.
[2561.62 --> 2566.22]  And I was kind of surprised to see it filtering in there, which was really interesting.
[2566.70 --> 2572.04]  So, yeah, there definitely are a good number of those use cases out there that people are exploring.
[2572.22 --> 2575.48]  And I think they are starting to filter into the real world.
[2575.48 --> 2580.96]  You know, there's one other topic I know we're getting short on time here that I thought we should talk about.
[2581.10 --> 2586.30]  And I know you mentioned earlier that I believe we're at the is it the two year anniversary of GDPR?
[2586.50 --> 2587.12]  Two years.
[2587.36 --> 2587.90]  Happy birthday.
[2588.20 --> 2589.76]  So happy birthday, GDPR.
[2589.94 --> 2595.86]  And we're in this wave right now of AI ethics is a really, really big topic in the world.
[2595.86 --> 2596.86]  And what does that mean?
[2596.86 --> 2613.58]  And if you look at what we've just been talking about these past few minutes and the vast difference between kind of today's AI and tomorrow's AI and then the day after tomorrow's AGI and what are the context of each of those means.
[2613.58 --> 2623.60]  So we are still very much lagging in terms of applying legal and regulatory constraint around that because we're still trying to understand it ourselves.
[2623.60 --> 2626.14]  And it's a very fast moving target.
[2626.14 --> 2629.92]  Yeah, even for wave two or system one AI.
[2630.24 --> 2630.76]  Absolutely.
[2631.12 --> 2634.88]  We are way behind even in system one or wave two, as you said.
[2635.04 --> 2643.00]  And so as that starts to evolve toward way of system two and wave three, we are still trying to figure out what that means.
[2643.00 --> 2645.24]  And that fast change makes it even harder.
[2645.48 --> 2647.18]  So it's really interesting.
[2647.34 --> 2651.12]  And that has a lot to do with how these technologies are going to interact with us.
[2651.12 --> 2657.42]  You know, it's the human actors that are being used side by side with all this working together as a system.
[2657.42 --> 2673.74]  And so it's going to be interesting in the years ahead to see how the evolution of human culture, be it laws, be it regulations, be it ethics, starts to constrain or shape the future of these technologies as they evolve.
[2673.80 --> 2678.94]  It's not strictly a technical conversation, which we have a habit as engineers to fall back into.
[2678.94 --> 2708.92]  Yeah, for sure.
[2708.92 --> 2709.74]  All of those things.
[2710.10 --> 2713.72]  Then, you know, it's strictly an academic pursuit.
[2713.90 --> 2718.24]  So I think you are seeing a lot of that friction these days with regulation.
[2718.82 --> 2721.82]  I think as we close up, I wanted to, you know, just share.
[2722.00 --> 2726.12]  We always try to share some learning resources here in these fully connected episodes.
[2726.12 --> 2732.76]  A couple that I just wanted to mention, of course, we'll link to the talks and such that we talked about.
[2732.98 --> 2737.40]  But that book that we mentioned was the title is Thinking Fast and Slow.
[2737.82 --> 2744.74]  So if you want to learn more about that kind of different ways of thinking system one and two, it's definitely something that I want to look into and read a bit.
[2744.74 --> 2748.50]  The other thing I was going to mention, we talked a bit about reinforcement learning.
[2748.84 --> 2766.30]  And I think one kind of fun thing that you can do on the side and also learn about reinforcement learning is using OpenAI's gem to do some sort of simple reinforcement learning problems like the card and pole problem or, you know, racing a car around a little track or something.
[2766.30 --> 2772.30]  It's really easy to use the OpenAI gem that creates these environments for reinforcement learning.
[2772.46 --> 2781.82]  And TensorFlow has a tutorial with their TF agents framework that's built in TensorFlow to use OpenAI gem.
[2782.00 --> 2784.80]  PyTorch also has an example using the gem.
[2784.96 --> 2790.02]  So I would recommend if you're wanting to learn more about that subject, you can get hands on in that way.
[2790.40 --> 2794.56]  So I have a learning resource of a very different type from usual.
[2794.56 --> 2797.22]  Within a particular reason why I'm recommending it.
[2797.38 --> 2817.96]  So one of the things when you work in the defense industry and you also give, you know, a lot of conference talks like I do prior to the COVID-19 situation, you're often asked about, you know, the concern of AI and autonomy and their intersection with weapons and war and things like that.
[2817.96 --> 2823.68]  And it's a topic that scares probably most people that think about it, I would imagine.
[2823.68 --> 2834.18]  And so I get asked about that so often that I wanted to point everyone to a public document that is, I would argue, a pretty good news thing.
[2834.18 --> 2843.94]  That if that's really something that you're worried about, about the future as we talk about AGI and all these things going forward and what happens in our world, there is a document.
[2844.10 --> 2850.06]  It's called the Department of Defense Directive 3000.09.
[2850.06 --> 2853.14]  That's 3000.09.
[2853.14 --> 2855.28]  Autonomy and weapon systems.
[2855.28 --> 2859.28]  And what it does is actually quite an old document.
[2859.28 --> 2860.10]  It's from 2012.
[2860.56 --> 2869.58]  But some really smart thinkers before the day of deep learning were kind of thinking through what are the implications and constraints that need to be applied to autonomy.
[2870.18 --> 2872.18]  And so you can go out and Google this.
[2872.26 --> 2874.32]  It's publicly available from the Department of Defense.
[2874.32 --> 2880.94]  And if you read through it, you realize they have handled so many of the use cases before we ever got to this modern day and age.
[2881.20 --> 2882.70]  You know, this is legally binding.
[2882.92 --> 2887.42]  This is what governs us in the United States, at least, about how we do this stuff.
[2887.56 --> 2897.18]  And the first time I read that document, which was coming into this career I met, I had a sense of relief that smart people had come along before and been very good about thinking.
[2897.18 --> 2905.52]  So if this is a topic, it's a little bit of a dry document, I'll confess, but it has some really interesting things in it in terms of how we are keeping people safe.
[2905.64 --> 2907.36]  And it was one of the very first things I had to learn.
[2907.52 --> 2911.82]  And I didn't think to recommend it a while back, but I keep getting asked about that over and over.
[2912.16 --> 2916.40]  So if you want to understand how we think about that, it's a really good document.
[2916.54 --> 2922.48]  And I suspect, despite the name of the document, you'll go to bed sleeping a little sounder knowing that this is the reality.
[2922.66 --> 2923.72]  So I just thought I'd offer that.
[2923.80 --> 2925.40]  I know it's a little bit unusual selection.
[2926.34 --> 2926.40]  Awesome.
[2926.62 --> 2927.16]  Good pick.
[2927.52 --> 2936.86]  And thanks for putting up with all my opinions and cynicism and optimism and, you know, all the emotions that went into today's episode.
[2937.82 --> 2938.32]  No worries.
[2938.66 --> 2938.98]  Yeah.
[2939.42 --> 2942.10]  If we're going to really be practical, we have to keep our eye on the future.
[2942.34 --> 2942.58]  Yeah.
[2942.82 --> 2947.90]  And so sometimes we got to set TensorFlow and PyTorch aside and figure out what direction we're going.
[2948.08 --> 2949.04]  This was a fun talk today.
[2949.18 --> 2949.76]  Thanks for doing it.
[2949.76 --> 2950.86]  Yeah, for sure.
[2951.04 --> 2951.60]  Talk to you later.
[2951.82 --> 2952.18]  Take care.
[2952.18 --> 2958.36]  Thank you for listening to Practical AI.
[2958.36 --> 2960.92]  We appreciate your time and your attention.
[2961.56 --> 2964.92]  Word of mouth is the number one way people find new podcasts.
[2964.92 --> 2968.98]  If Practical AI has helped you on your AI journey, please do tell a friend.
[2969.10 --> 2970.34]  Hey, they'll thank you later.
[2970.34 --> 2975.52]  Special thanks to Breakmaster Cylinder for the beats and to our awesome partners for their support.
[2975.88 --> 2978.38]  Shout out to Fastly, Linode, and Rollbar.
[2978.38 --> 2985.92]  If you and your organization would benefit by speaking directly to the AI community, you should sponsor Practical AI.
[2986.42 --> 2990.02]  Podcast advertising is highly effective and we would love to work with you.
[2990.30 --> 2993.04]  Head to changelog.com slash sponsor to learn more.
[2993.32 --> 2994.10]  That's all for now.
[2994.50 --> 2995.70]  We'll talk to you again next week.
[2995.70 --> 3025.68]  We'll see you again next week.
