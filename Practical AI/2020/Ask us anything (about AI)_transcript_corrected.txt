[0.00 → 1.04] This is a quick one.
[1.28 → 1.58] Okay.
[1.76 → 3.82] What laptop do I buy for deep learning?
[3.82 → 5.96] My answer is, doesn't matter.
[6.72 → 7.54] Yeah, mine too.
[8.30 → 11.54] I mean, you could buy one with a nifty GPU or something,
[11.76 → 14.70] but if you're using something like Cola Pro or something
[14.70 → 16.94] to do your initial testing
[16.94 → 19.58] and then you're deploying on some giant cluster
[19.58 → 21.82] or something that your company has,
[21.92 → 23.50] it really doesn't matter, buy a Chromebook.
[24.48 → 25.48] I'm the same.
[25.48 → 30.76] Bandwidth for Changelog is provided by Vastly.
[30.76 → 33.02] Learn more at Fastly.com.
[33.24 → 36.34] We move fast and fix things here at Changelog because of Rollbar.
[36.46 → 38.14] Check them out at Rollbar.com
[38.14 → 40.56] and we're hosted on Linde cloud servers.
[40.92 → 42.92] Head to linode.com slash Changelog.
[45.62 → 48.22] This episode is brought to you by DigitalOcean.
[48.54 → 51.80] DigitalOcean's developer cloud makes it simple to launch in the cloud
[51.80 → 53.30] and scale up as you grow.
[53.64 → 55.30] They have an intuitive control panel,
[55.48 → 57.30] predictable pricing, team accounts,
[57.54 → 61.24] worldwide availability with a 99.99 uptime SLA
[61.24 → 64.98] and 24-7, 365 world-class support to back that up.
[65.24 → 68.86] DigitalOcean makes it easy to deploy, scale, store, secure,
[69.00 → 70.70] and monitor your cloud environments.
[71.10 → 72.82] Head to do.co slash Changelog
[72.82 → 74.50] to get started with a $100 credit.
[74.90 → 76.98] Again, do.co slash Changelog.
[76.98 → 88.64] Welcome to Practical AI,
[88.98 → 92.08] a weekly podcast that makes artificial intelligence practical,
[92.38 → 94.16] productive, and accessible to everyone.
[94.46 → 97.40] This is where conversations around AI, machine learning,
[97.48 → 98.56] and data science happen.
[98.92 → 102.10] Join the community and Slack with us around various topics of the show
[102.10 → 103.58] at Changelog.com slash community,
[103.92 → 104.92] and follow us on Twitter.
[105.08 → 106.72] We are at Practical AI FM.
[106.96 → 108.44] Okay, take it away, guys.
[112.60 → 117.40] Welcome to another fully connected episode of Practical AI.
[117.40 → 121.70] This is where my co-host Chris and I keep you fully connected
[121.70 → 124.60] with everything that's happening in the AI community.
[124.80 → 128.54] We're going to take some time to talk about the latest AI news
[128.54 → 132.92] and dig into some resources to help you level up your machine learning game.
[133.28 → 134.46] My name is Daniel Whiten ack.
[134.56 → 137.44] I'm a data scientist with SIL International,
[137.76 → 140.62] and I'm joined as always by my co-host Chris Benson,
[140.92 → 144.08] who is a principal AI strategist at Lockheed Martin.
[144.36 → 145.02] How are you doing, Chris?
[145.26 → 146.64] I am doing very well, Daniel.
[146.64 → 147.44] How's it going today?
[147.76 → 148.82] It's going well.
[148.92 → 153.80] I feel like I'm a bit tired of not work necessarily,
[153.80 → 156.14] but I feel like there's been extra work recently
[156.14 → 158.30] because there's been like normal job work,
[158.30 → 160.80] and then there's been like COVID-related work,
[160.80 → 165.10] and then there's been various like things to keep up with around the house,
[165.10 → 167.90] and then there's also clear is this week,
[167.96 → 169.94] which is really cool because I can, you know,
[169.94 → 172.68] be at home, and they're doing all sorts of stuff virtually.
[172.68 → 174.70] So for listeners out there that don't know,
[174.70 → 177.68] clear is an AI research conference.
[178.10 → 179.22] So that's been a lot of fun,
[179.32 → 181.96] but then I kind of tried to be fitting that into the cracks
[181.96 → 183.20] because I don't want to miss anything.
[183.40 → 186.16] So yeah, I'm living on coffee right now.
[186.30 → 186.82] What about you?
[187.20 → 188.32] You know, about the same.
[188.70 → 189.46] It's interesting.
[189.56 → 190.40] The world has changed.
[190.88 → 193.48] And, you know, you mentioned that particular conference,
[193.48 → 197.34] but really a lot of conferences are now going virtual only,
[197.34 → 200.96] and many, many of them have announced that even after we get through
[200.96 → 204.36] at least this wave of COVID-19 and, you know,
[204.44 → 207.88] barring any future concerns that they're still going to stay virtual.
[207.88 → 210.86] And so, you know, virtual conferences, the new thing.
[211.02 → 212.62] So I guess we all need to get used to that.
[213.00 → 214.66] I've seen people go back and forth.
[214.74 → 217.14] I've also seen people call for, you know,
[217.42 → 221.56] hey, let's not do this virtual conference thing after the crisis ends.
[221.56 → 225.94] Because, yeah, I mean, some people like, you know, in-person interaction.
[225.94 → 227.42] I think that, like you say,
[227.44 → 229.26] it's definitely not going to be the same afterwards.
[229.52 → 231.28] There are a variety of, you know,
[231.34 → 234.00] people trying to make it, you know,
[234.02 → 235.94] a new type of experience at clear.
[236.52 → 239.24] There were a few guys from California.
[239.24 → 242.64] They built this little app, not just for clear, I don't think,
[242.72 → 246.62] but someone created a space for clear participants.
[246.62 → 248.02] It's called Online Town.
[248.44 → 248.56] Yep.
[248.56 → 253.88] And it's basically like you join into Online Town, clear Online Town.
[254.14 → 257.04] And you've got like a little pixel art guy,
[257.16 → 259.92] kind of like on Zelda Game Boy, if you ever played that.
[259.98 → 262.62] And you can kind of walk around Online Town.
[262.88 → 264.48] And so there's like a beach,
[264.50 → 268.22] and there's like this conference room area place,
[268.22 → 270.20] and there's like a grassy lawn.
[270.38 → 271.84] And like your kind of walk around,
[271.90 → 274.72] and then everybody else in Online Town is also walking around.
[274.72 → 275.98] As you get close to them,
[275.98 → 278.80] then their video chat opens, right?
[278.88 → 281.48] So it's kind of like you're bumping into someone in Online Town,
[281.58 → 283.66] and you can talk to them and introduce yourself.
[283.86 → 286.34] And then you can go down to the beach in Online Town and,
[286.34 → 290.46] you know, talk about things and, you know, AI or not related.
[290.68 → 292.88] So that was actually incredibly fun.
[293.36 → 293.92] So I...
[293.92 → 295.12] That sounds like a lot of fun.
[295.52 → 296.70] A great virtual world there.
[296.70 → 301.06] Yeah, it was like bumping into like random people and that sort of thing.
[301.22 → 302.06] So, yeah.
[302.62 → 306.64] You know, I host a local meetup here in Atlanta called the Atlanta Deep Learning Meetup.
[306.84 → 310.88] And like all the other meetups, we stopped meeting when COVID broke.
[310.96 → 313.34] But it is definitely making me think,
[313.48 → 315.84] what should our meetup be going forward?
[315.92 → 317.98] And as we are temporarily shut down,
[318.04 → 321.18] I'm trying to re-envision what the meetup should be,
[321.18 → 325.26] and how much is in person or virtual and how the activities might change.
[325.38 → 328.10] If conferences are very much online,
[328.22 → 330.16] maybe meetups, even if they're online,
[330.16 → 333.14] are a little bit more interactive and less about presentation.
[333.60 → 334.12] So, yeah.
[334.36 → 336.80] It'll be interesting to see how meetups come back out of this
[336.80 → 341.06] as kind of the bread and butter monthly way of people interacting in the space.
[341.38 → 341.48] Yeah.
[341.66 → 345.80] Well, you should try to create a Deep Learning Atlanta Online Town.
[346.08 → 346.64] There you go.
[346.74 → 347.48] I recommend it.
[347.54 → 348.52] It was a perfect time.
[348.66 → 349.76] So try that.
[349.76 → 352.68] I know a lot of people are innovating during this time.
[352.96 → 357.34] And I think Lockheed's doing even some COVID-related stuff.
[357.40 → 357.92] Is that right?
[358.16 → 358.94] We are indeed.
[359.20 → 361.86] I probably can't really address much of that.
[362.18 → 363.80] That has to go through official channels.
[363.96 → 366.32] That's in progress and that sort of thing.
[366.36 → 367.80] But like any company,
[367.96 → 370.74] I mean, I think every company out there is having to address
[370.74 → 374.26] a number of different challenges with how they operate going forward
[374.26 → 376.72] and how they react to a world that may change.
[376.72 → 379.24] If we have a wave coming back in the fall or whatever.
[379.24 → 381.06] So there are all sorts of stuff.
[381.50 → 383.28] We live in an interesting time.
[383.54 → 384.68] It is an interesting time.
[384.94 → 387.96] I'm not saying it's a good time in that way, but it's an interesting time.
[388.30 → 389.96] Well, there's a lot of innovation going.
[390.14 → 395.70] I know we've really ramped up translation efforts at SIL to get COVID-related information
[395.70 → 397.46] into local languages.
[397.96 → 402.70] Some people did some research at SIL and found that 30% of people on the planet
[402.70 → 407.90] don't have health information in their language to protect against COVID.
[408.24 → 410.58] So we actually kicked off a fundraiser this week.
[410.92 → 414.16] So if you're interested in that, SIL.org slash COVID fund.
[414.60 → 418.16] If you're interested in helping that information get translated.
[418.68 → 419.30] But yeah.
[419.54 → 420.68] I hope people will do that.
[420.74 → 421.82] You guys do awesome work.
[421.88 → 423.46] And I know we had a previous episode,
[423.62 → 426.42] which we'll put in the show notes where you talked a bit about that.
[426.42 → 430.60] And so I hope people will check out because Daniel does some pretty amazing work.
[430.76 → 431.68] And I'm saying that out loud,
[431.68 → 434.56] since I know you're not going to talk about your own stuff too much right now.
[434.94 → 436.92] Yeah, well, definitely check that out.
[437.02 → 441.24] There's a lot of people all across the world really trying hard to get that info out.
[441.68 → 446.48] But speaking of info, we've had a couple of recent episodes about COVID.
[446.70 → 447.48] We'll link those.
[447.98 → 453.42] But today, since everyone is interacting online and still trying to work
[453.42 → 455.00] and still trying to figure out work,
[455.00 → 457.98] it's been a while since we've done one of these fully connected episodes.
[458.50 → 462.50] We thought it might be kind of fun to just have an episode
[462.50 → 468.56] where we address some of the questions that we've run across in forums online related to AI.
[468.78 → 469.64] I think we did this.
[470.02 → 471.06] I don't know when this was.
[471.18 → 472.90] It was quite a few episodes ago.
[473.04 → 478.38] But we kind of searched around Quora and Kaggle and Stack Exchange and Reddit
[478.38 → 480.76] and tried to answer some of the questions
[480.76 → 483.76] or at least discuss some of the questions if they were ridiculous
[483.76 → 485.32] happening online.
[485.32 → 488.04] So yeah, hopefully you enjoyed this episode.
[488.18 → 489.02] We've done the same here.
[489.10 → 491.52] We've basically gone around to various places online
[491.52 → 496.52] and saw what are those questions that are popping up on the top of the list
[496.52 → 498.64] related to artificial intelligence.
[499.20 → 501.66] And we're just going to kind of rapid fire,
[501.78 → 503.92] go back and forth and discuss some of these.
[504.32 → 508.52] Chris, you reached out online and got some questions from listeners as well
[508.52 → 509.84] that we can maybe discuss.
[509.84 → 511.78] I didn't give folks a lot of time.
[512.10 → 515.68] I announced a few hours ago that we were going to do this on social media channels
[515.68 → 517.52] but got some good questions.
[517.86 → 522.38] And interestingly, some of them are from people that are not in the AI community.
[523.06 → 524.78] And they're folks in other industries
[524.78 → 529.08] and they're just wondering how AI will change the world and affect their lives.
[529.16 → 531.34] So there's going to be a couple of those that are not
[531.34 → 535.10] and then we can obviously handle some technical questions too from practitioners.
[535.10 → 536.38] Sounds great.
[536.50 → 540.32] Well, you want to kick it off with one of those questions from the community online?
[540.80 → 540.92] Sure.
[541.08 → 546.18] So a friend of mine named Jeff Pike that I used to work with at Honeywell was on LinkedIn
[546.18 → 553.22] and he pointed out that neural networks have opened up a huge surge in AI ML.
[553.72 → 556.56] And what do we think is the next big thing?
[556.82 → 563.78] Or alternatively, what problem needs a neural network-like breakthrough to make it big going forward?
[563.78 → 568.24] And I know that there's a lot of talk, especially the last few months in that area.
[568.30 → 568.92] What do you think, Daniel?
[569.64 → 571.38] Yeah, this is a hard question.
[571.56 → 572.86] What's the next big thing?
[572.96 → 575.58] I think, I forget which guest it was on here.
[575.70 → 576.36] No pressure there.
[576.50 → 581.68] That said like, you know, if you ask me to predict something, I'm 100% going to be wrong.
[581.86 → 584.74] So whatever I'm going to say is definitely going to be wrong.
[585.08 → 588.02] And no one's allowed to hold us to anything we say in the show, okay?
[589.10 → 590.62] Yeah, so I don't know.
[590.68 → 591.62] It's a good question.
[591.62 → 597.32] I mean, I think that there's no shortage of unsolved problems related to deep neural networks.
[597.50 → 602.06] So I don't think this is a situation where like deep neural networks have solved a host
[602.06 → 607.66] of problems, and we're going to kind of jump to something new and totally leave those behind.
[607.88 → 614.74] Because there's like so many open problems and interesting areas to explore with deep neural
[614.74 → 615.08] networks.
[615.08 → 616.86] But certainly they're not the only thing.
[617.00 → 620.36] You know, I'm trying to think through the things I was seeing at clear this week.
[620.36 → 623.38] There's definitely some fascinating stuff happening.
[623.38 → 629.14] A couple of things that I noticed, which again, these may or may not be trends.
[629.28 → 631.82] I'm not trying to necessarily make a prediction.
[632.06 → 637.82] But I did see a good number of things related to like graph neural networks and graph structured
[637.82 → 638.30] data.
[638.30 → 645.22] More so than when I searched for that sort of stuff, like last year at research conferences,
[645.22 → 648.72] there didn't seem to be as much as I'm seeing now.
[648.78 → 652.32] And maybe that's because of the particular makeup of the conference or something.
[652.32 → 656.22] But I think there is a sort of increased interest in that sort of stuff.
[656.22 → 662.70] I also saw some fascinating things around, you know, using ideas from physics and science,
[662.70 → 666.76] like energy based methods and Hamiltonian Lagrangian based methods.
[666.76 → 670.78] So these are like methods where you can kind of like in physics where you would model like
[670.78 → 674.84] the motion of complex objects or something and use differential equations.
[674.84 → 679.10] And a lot of people are thinking, well, what can we like bring in from that world?
[679.10 → 681.66] And how does that combine with AI?
[681.66 → 685.44] So I don't know, those are a couple of things that came to my mind.
[685.44 → 686.02] What about you?
[686.40 → 688.38] Well, I've definitely seen both of your examples.
[688.50 → 689.58] I know I've seen the same.
[689.70 → 694.00] There's been more and more physics stuff coming into it in terms of solving complex physics.
[694.18 → 696.64] And you mentioned, you know, graph neural networks.
[696.64 → 701.38] And we actually talked about that last week in reinforcement learning for chip design,
[701.48 → 706.22] our most recent episode with Anna and Azalea, where, you know, they're both in the Google
[706.22 → 708.14] brain team, and they were talking about their use of it.
[708.22 → 710.38] So that was that's a very immediate thing.
[710.38 → 717.22] I think the thing that I've really noticed, especially since New Year's, is a real focus
[717.22 → 718.50] beyond deep learning.
[718.62 → 723.10] We had several years when, you know, everything was deep learning in all capacities.
[723.42 → 729.34] And a lot of the big names, the legends in this space are really turning towards what
[729.34 → 730.68] does it take to get past that?
[730.78 → 735.86] And, you know, in terms of intelligence, and what are the core constituents that make up,
[735.86 → 739.78] you know, the idea of consciousness and the focus on attention?
[740.22 → 745.82] And, you know, what do we need to add to these architectures that take them beyond kind of the
[745.82 → 748.08] constraints or the limitations of deep learning?
[748.28 → 751.96] So there's the research perspective and there's the industry perspective.
[752.38 → 758.22] I think in industry, we're going to see deep learning models continuing to be very prolific and
[758.22 → 762.60] very productive for a long time to come because you can use them in so many different
[762.60 → 763.14] applications.
[763.68 → 767.50] But I think the research world is starting to say, OK, we've done that.
[767.60 → 768.68] How do we move past that?
[768.82 → 773.50] And so I'm really excited to see over the next year or two what kinds of research directions
[773.50 → 777.48] and potentially breakthroughs might occur to lead us beyond the world of deep learning.
[777.92 → 778.58] Yeah, definitely.
[778.94 → 781.48] So I'm going to bring in another question here.
[781.48 → 787.66] I'm going to bring us from the future prediction to something extremely practical because this is
[787.66 → 788.38] practical AI.
[788.52 → 789.20] I knew you would.
[789.20 → 794.14] The question, I forget where I pulled this one from, what tools do you personally use
[794.14 → 796.02] in your daily work as a data scientist?
[796.70 → 801.22] Chris, what tools are you using every day or maybe not every day, but often?
[801.78 → 807.70] Well, I've kind of selected my own tools or TensorFlow, you know, Python, most of the typical
[807.70 → 814.20] I really focus on staying pretty mainstream in terms of tool sets, frankly, because I'm too
[814.20 → 818.32] lazy and don't have enough time to try lots of new tools out.
[818.32 → 820.26] So I'm pretty mundane in that way.
[821.14 → 826.18] A lot of, you know, pandas, the normal Python libraries that we all use on a day to day
[826.18 → 826.52] basis.
[826.74 → 828.08] And then I really look to the folks.
[828.20 → 831.34] But I'm also not doing hands on data science every day.
[831.52 → 834.44] My job is fairly eclectic in terms of what I'm focusing on.
[834.60 → 836.18] So how about yourself, Daniel?
[836.26 → 836.74] What are you doing?
[837.50 → 841.60] Yeah, I think some things have changed in recent times for me.
[841.60 → 848.16] I know one thing that I've really started using pretty much every day is Google Cola Pro.
[848.90 → 854.96] So people might be familiar with Google Cola, which is sort of a hosted Google Docs like
[854.96 → 858.26] Jupyter Notebook on top of Google Cloud instances.
[858.76 → 865.68] They have a pro version of that where you get sort of prioritized access to GPUs and you get,
[865.68 → 869.28] I think, longer run times and some other kind of niceties.
[869.60 → 874.92] And it's only $10 a month, which is, I think, a really great deal.
[875.46 → 877.06] You know, I'm a Cola user as well.
[877.16 → 878.76] And I wasn't thinking about that.
[879.20 → 882.06] Yeah, no, I would definitely recommend upgrading for sure.
[882.34 → 885.40] So I pretty much I have two tabs open right now.
[885.40 → 892.96] So I think that's one thing like I've been using also because SIL uses Google Drive a lot.
[893.20 → 897.76] And so I'm able to kind of organize some of my own experiment stuff in with other things
[897.76 → 898.84] that people are using.
[899.20 → 904.94] But yeah, similar to you, I mean, I'm not too picky about frameworks and different tool
[904.94 → 906.08] sets and that sort of thing.
[906.16 → 911.04] It's pretty much whatever gets the work done or is state of the art in a certain area.
[911.54 → 914.66] Also, I found recently I've really enjoyed working with Streamlet.
[914.66 → 918.14] We did an episode with them, and I've played around with it since then.
[918.48 → 923.72] And Streamlet is like this really cool thing where you like a non-UI front end person like
[923.72 → 929.94] myself can build like pretty nice looking little user interfaces or demos for your models or
[929.94 → 932.54] like data labelling tools and stuff really easy.
[932.72 → 936.52] So I would definitely, you know, recommend taking a look at that as well.
[936.94 → 937.66] That sounds good.
[937.82 → 938.34] I'm just curious.
[938.42 → 944.52] I know that you when you teach your classes, you do both the TensorFlow curriculum and you
[944.52 → 945.62] also do PyTorch.
[945.78 → 948.52] I'm just curious with the religious wars there.
[948.92 → 950.54] So in past trainings, I've done both.
[950.60 → 952.72] I've done ones where I've just used one or the other.
[953.30 → 956.66] In the one I'm doing upcoming in May, I'm going to be using both.
[957.20 → 959.94] And my thought on that, we'll see, you know, how it goes, I guess.
[960.04 → 964.74] But my thought on it is, you know, me as a data scientist, I have to use both because,
[965.26 → 967.86] you know, it's like you solve one problem.
[967.86 → 971.10] And there's this great TensorFlow implementation.
[971.46 → 974.94] And it's just it just makes sense for you to grab that and maybe tweak it a little bit
[974.94 → 976.88] and use it in another case.
[976.88 → 979.22] Like there's this great PyTorch implementation.
[979.48 → 983.36] And maybe it's because I'm lazy, but I never I'm never really starting from scratch.
[983.36 → 983.62] Right.
[983.66 → 985.66] I'm starting from something someone has done.
[985.84 → 986.80] So most of us are.
[986.80 → 993.20] From my perspective, you know, it's to be sort of functioning in this space now, you
[993.20 → 997.94] you have to be willing to sort of jump around a bit unless maybe you work for Google or something.
[997.94 → 1001.74] And then like you always use TensorFlow or you work for Facebook or right.
[1002.10 → 1005.40] Whoever has like a standard of I have a lot of autonomy.
[1005.40 → 1007.48] So maybe that's a blessing in my case.
[1007.82 → 1011.90] No, but, you know, I just want to point out you make a great point there in that most of
[1011.90 → 1015.90] us start, you know, from benefiting from the work of others and that transfer learning
[1015.90 → 1018.56] effect is a powerful, powerful thing.
[1018.76 → 1021.40] And we were able to get a lot more done than we would otherwise do.
[1021.52 → 1025.18] So, yeah, no, that's a very practical, pragmatic way of looking at that.
[1032.92 → 1034.68] We deserve a better Internet.
[1034.68 → 1037.98] And the brave team has the recipe for bringing it to us.
[1038.10 → 1039.10] Start with Google Chrome.
[1039.34 → 1043.06] Keep the extensions, the dev tools and the rendering engine that make Chrome great.
[1043.28 → 1044.14] Rip out the Google bits.
[1044.26 → 1044.90] We don't need them.
[1044.90 → 1047.78] Mix in ad and tracker blocking by default.
[1048.06 → 1052.64] Quick access to the Tor network for true private browsing and an opt-in reward system.
[1052.64 → 1055.48] So you can get paid to view privacy respecting ads.
[1055.56 → 1059.42] Then turn around and use those rewards to support your favourite web creators like us.
[1059.76 → 1064.34] Download brave today using the link in the show notes and give tipping a try on changelog.com.
[1064.34 → 1079.64] So I am going to return to the non-technical questions that we got asked.
[1079.64 → 1096.34] And on one of my social media channels, a friend named Susan Feingold asked, she said, what concerns me is what can be done to prevent a hostile country or just a criminal person or a criminal enterprise from developing AI for malicious reasons.
[1096.34 → 1106.48] For instance, it seems like it seems like it would be easy to use AI for terrorism or to greatly influence or change election results or to modify digital media for nefarious purposes.
[1106.94 → 1108.62] You know, the things go on and on.
[1108.86 → 1110.16] How do you see that, Daniel?
[1110.30 → 1112.20] I know we both come from these two different sides.
[1112.34 → 1113.06] We'll start with you.
[1113.06 → 1121.64] I guess the short answer is there's nothing preventing it because, you know, those sorts of entities are using AI already.
[1122.12 → 1122.24] Sure.
[1122.72 → 1122.94] Yeah.
[1122.96 → 1125.80] I mean, of course, that's sort of demoralizing.
[1125.94 → 1141.26] But I think if you also put it into a perspective of, you know, people have been using tech for malicious purposes since there was tech, just like they use anything they can get their hands on for malicious purposes if they have those purposes.
[1141.26 → 1151.82] So, of course, there are certain things where AI gives you a specific advantage that might be even, you know, greater than that of other tech or something like that.
[1152.06 → 1159.38] I know you've been thinking a lot about ethics questions a lot and all those things and been leading in discussions in those areas in a lot of ways.
[1159.76 → 1163.08] So I know that there's really smart people working on this problem.
[1163.34 → 1168.06] And, you know, of course, there's probably regulations that will be put in place to help with that.
[1168.06 → 1169.56] There'll be other things.
[1169.74 → 1176.44] But in the end, I think it's going to be one of those technologies that's always used for that purpose.
[1176.82 → 1185.86] My hope is that there's enough AI practitioners out there using AI for good that that's, you know, that's the kind of side that, you know, has the most attention.
[1186.42 → 1186.52] Yeah.
[1186.52 → 1204.08] And that's largely where I'm at, too, in that I like to believe that the vast majority of us are using AI either for just normal business purposes, you know, with some sense of benevolence in that process or explicitly, as we like to talk about all the time, AI for good.
[1204.08 → 1213.00] There are certainly bad actors out there in the world, just as you pointed out, with technology that will use any technology, including AI, for nefarious purposes.
[1213.46 → 1229.22] I can say in a kind of broad brush stroke, nonspecific way that certainly the different aspects of Western governments in general and certainly the U.S. government, you know, as we're here in the United States, have their eye on that.
[1229.22 → 1243.48] I think the U.S. military, the defence industry, the intelligence community, and the law enforcement community are becoming very, very savvy at how to detect and understand what those threats are and trying to respond effectively to those.
[1243.84 → 1246.82] And I have, you know, some insight into that world.
[1247.30 → 1254.46] And so I think there are really, as you said, there are really, really smart people that are working very hard against that.
[1254.46 → 1270.08] So I think what I would say to Susan or anyone else is, as you learn about AI in the world and some of the capabilities that we have, just like you would with email spam and other things, be practical in how you respond to different types of interactions that you have.
[1270.14 → 1272.84] But on the larger scale, there are good folks working on that.
[1272.96 → 1275.50] And so kind of leave it to them and be supportive of that work.
[1275.72 → 1277.30] And that's where I'll stop.
[1278.28 → 1279.74] Yeah, I appreciate it.
[1279.74 → 1284.80] Yeah, give us your thoughts on that's definitely a question open for discussion.
[1285.18 → 1290.52] So let us know in our Slack channel or on Facebook or LinkedIn what your thoughts are there.
[1291.18 → 1295.32] You can join our Slack channel at changelog.com slash community.
[1295.54 → 1297.80] We'd love to hear your thoughts on things like that.
[1298.24 → 1301.06] So I'll bring us back to more practical questions.
[1301.24 → 1301.62] Absolutely.
[1301.62 → 1311.32] One of the questions I found kind of in the top areas on these sites was, as a data scientist, do you use AutoML in your job?
[1311.40 → 1312.26] If yes, how?
[1312.82 → 1315.24] So this might be a quick answer for both of us.
[1315.34 → 1316.90] Do you use AutoML in your job?
[1317.20 → 1318.34] So not in my job.
[1318.36 → 1319.32] I've played with it at home.
[1319.32 → 1323.62] So I kind of have my AI activities at home, like where I use Cola and such.
[1323.76 → 1325.50] And then I have things that I do at work.
[1326.02 → 1328.72] And playing around at home, nothing too serious yet.
[1328.72 → 1331.58] But I have personally not in my job.
[1332.14 → 1332.30] Yep.
[1332.40 → 1334.04] So this one was a quick one for me.
[1334.12 → 1335.10] I'll go with the no.
[1335.56 → 1336.10] The no.
[1336.94 → 1340.48] And if you're interested in what is AutoML, we won't necessarily cover it here.
[1340.58 → 1342.00] There is a great episode, though, on it.
[1342.24 → 1342.88] There is indeed.
[1342.94 → 1344.02] It is amazing stuff.
[1344.16 → 1345.86] See that episode from Cheryl Chen.
[1346.34 → 1348.48] That was a great episode about AutoML.
[1348.94 → 1351.26] Go for another technical one, since that was a quick one there.
[1351.46 → 1352.84] Yeah, let's go rapid fire.
[1353.18 → 1355.04] What is a CNN in machine learning?
[1355.04 → 1357.28] I think, hopefully, we know the answer to this.
[1357.42 → 1358.00] You go ahead and start.
[1358.00 → 1358.74] I want to hear yours.
[1359.34 → 1364.30] I think, if I'm correct, CNN is a convolutional neural network.
[1364.80 → 1368.84] So people have probably heard of this, or sometimes it's called a comet.
[1369.34 → 1374.08] So these episodes we do, which Chris and I are called Fully Connected, that's purposeful
[1374.08 → 1379.70] because it's actually maybe a pun or a term of art in artificial intelligence, where fully
[1379.70 → 1386.24] connected means that sort of the outputs of one node in a neural network are distributed
[1386.24 → 1388.48] across all the other nodes.
[1388.58 → 1391.84] And so the nodes are all fully connected in this sort of way.
[1391.84 → 1398.44] And so a number output coming out of one kind of goes into the inputs of the next layer.
[1398.44 → 1405.32] In a convolutional neural network, which is often used for image processing or things like object detection
[1405.32 → 1409.40] or those sorts of things where maybe people think of them mostly,
[1410.06 → 1414.10] or where maybe an image is represented by a matrix of numbers,
[1414.18 → 1419.56] or maybe multiple layers of a matrix of numbers representing various properties of the image.
[1419.56 → 1425.34] And in a convolutional neural network, it doesn't have this sort of fully connected structure.
[1425.60 → 1431.94] There's actually a filter that's applied over the image, and it kind of slides over the image
[1431.94 → 1438.90] where a portion of that image is actually input to a function in the neural network,
[1439.00 → 1440.06] which outputs a number.
[1440.18 → 1443.28] And so there's actually a dimensional change from one layer to another
[1443.28 → 1446.76] because it's only these inputs aren't fully connected in this way.
[1446.76 → 1450.68] I probably didn't describe that in an extremely logical way,
[1450.84 → 1454.18] but maybe I wouldn't pass the data science interview.
[1454.48 → 1457.08] No, I think you just did pass the data science interview.
[1457.18 → 1457.78] That was pretty good.
[1458.26 → 1461.54] I'll tackle it a slightly different way, though, quickly,
[1462.02 → 1466.82] is that if you think of a neural network in general as being many layers of these nodes,
[1466.90 → 1472.20] as Daniel described, then if you think of an image and how you break down that image,
[1472.20 → 1476.52] and that some layers start with the most basic aspects of an image,
[1476.56 → 1479.88] such as a colour gradient between two distinct colours,
[1480.38 → 1483.48] where you might get, and from that you might derive a line.
[1483.78 → 1487.70] And if you put some of those together, you might get a curve on that line,
[1487.74 → 1490.42] and then small basic objects are formed,
[1490.50 → 1493.84] and different layers in that network handle different aspects of that.
[1493.90 → 1496.98] But eventually, just as you might build something up with Legos,
[1496.98 → 1502.08] you build up an image from these very basic constituents that each build upon each other,
[1502.44 → 1505.44] all the way to the complexity of maybe a very rich photograph.
[1506.16 → 1511.18] And so that kind of breakdown or buildup is how a convolutional neural network
[1511.18 → 1515.86] kind of codes or decodes an image that it's trying to look at.
[1515.96 → 1520.72] So hopefully, between the two of us, there are two different ways of looking at the same thing.
[1521.22 → 1522.24] Yeah, yeah, for sure.
[1522.24 → 1526.58] And there's, of course, a lot of great info on those sorts of things online.
[1527.32 → 1529.96] So I have one more that I want to throw out.
[1530.26 → 1532.42] That is, it's still pretty pragmatic.
[1532.60 → 1536.10] It's not a technical one, but I think it's one a lot of people ask.
[1536.16 → 1540.76] And that is, how does one start developing an AI-enabled business solution?
[1540.88 → 1544.70] Because, you know, companies all over the world right now are trying to adopt
[1544.70 → 1548.42] and get more savvy about how they use these technologies.
[1548.42 → 1551.44] And so why don't we talk about that?
[1551.56 → 1553.04] You want to go, or you want me to first?
[1553.22 → 1555.16] So does this mean like an AI product?
[1555.42 → 1557.50] Or does this mean just like I'm in a company,
[1558.14 → 1560.80] and I think I have an AI solution to this problem,
[1560.80 → 1562.84] and I'm going to develop it within the company?
[1563.56 → 1565.60] I'm interpreting it as the former of the two,
[1565.70 → 1566.88] but you can take it any way you want.
[1566.88 → 1567.72] Like an AI product.
[1568.04 → 1568.50] There you go.
[1568.60 → 1569.56] I'm going to take it that way.
[1569.86 → 1572.82] So and what I tell people is don't start with an idea,
[1572.82 → 1574.22] and it has to be AI-enabled.
[1574.22 → 1577.86] And I've seen that mistake made multiple times in my career
[1577.86 → 1581.86] where people are obsessed with having something that's AI.
[1582.00 → 1584.46] Maybe that's the marketing imperative, you know,
[1584.48 → 1587.58] and sales imperative of putting an AI label on something.
[1588.00 → 1589.18] But it's just a tool.
[1589.34 → 1590.42] It's another tool in the toolbox.
[1591.00 → 1593.24] And different AI architectures,
[1593.28 → 1595.64] which you could think of as the thing that makes up a model,
[1595.90 → 1597.72] are good for different types of problems.
[1597.72 → 1601.86] And so what I tell people is don't start with I have a product
[1601.86 → 1603.00] and I want it to be AI.
[1603.44 → 1606.00] Say I have something in mind that I want to build,
[1606.08 → 1607.30] a solution, a product, whatever.
[1607.94 → 1611.04] And part of that creation process,
[1611.20 → 1615.30] I think would benefit from this type of problem-solving,
[1615.50 → 1619.26] which, oh, by the way, it turns out there is an AI type of architecture
[1619.26 → 1622.58] that lends itself very, very well to that particular thing.
[1622.76 → 1624.50] And so if you do that,
[1624.56 → 1626.84] you end up with kind of the Steve Jobs approach.
[1626.84 → 1630.32] You end up with a fantastic product because you had the end in mind.
[1630.80 → 1634.88] And you use AI like you would use any other technology tool
[1634.88 → 1636.30] that you might choose from.
[1636.44 → 1640.52] Is each one of those bits are good for something that it should focus on?
[1640.62 → 1644.70] I think that people go wrong when they start with the end has to be an AI thing
[1644.70 → 1647.86] and they'll do anything they can to fit AI into that.
[1647.90 → 1649.70] And they end up with a bad product or service.
[1649.86 → 1652.24] So start with the end in mind like Jobs told us
[1652.24 → 1657.46] and then figure out if and when AI might apply into that product development lifecycle.
[1658.44 → 1659.38] Yeah, yeah, definitely.
[1659.56 → 1661.98] I think, you know, just in case my boss is listening,
[1662.14 → 1667.00] he would say that, you know, how do you develop any sort of business solution?
[1667.14 → 1670.02] You just think about how you're going to satisfy your customers.
[1670.12 → 1670.78] That's great advice.
[1670.92 → 1673.22] And that's basically drives everything.
[1673.22 → 1675.40] So just satisfy your customers.
[1675.86 → 1678.54] If AI is needed to do that, then that's great.
[1678.84 → 1683.56] But there are certainly many products that don't have AI involved in them
[1683.56 → 1685.02] and they satisfy their customers.
[1685.26 → 1688.54] So, you know, it's like you say, maybe not starting with the
[1689.20 → 1692.38] I'm going to build an AI product, but I'm going to solve a problem
[1692.38 → 1694.98] is probably the better, better path.
[1695.82 → 1696.16] Sounds good.
[1696.60 → 1696.86] Yeah.
[1697.04 → 1698.08] Well, let's see.
[1698.62 → 1701.70] Let's maybe take another couple of technical ones.
[1701.82 → 1702.32] Sounds good.
[1702.32 → 1706.92] This one I pulled, it says how to save a trained CNN model.
[1707.12 → 1710.84] And I think maybe this would just be like after I train my model,
[1711.12 → 1714.38] let's say I have it in a notebook or something, you know,
[1714.60 → 1715.62] I don't want to lose it.
[1715.74 → 1716.86] So what do I do with it?
[1716.96 → 1718.62] I think that's the direction of the question.
[1718.68 → 1721.06] It's not necessarily specific to CNN models,
[1721.10 → 1722.88] even though we just talked about CNN models.
[1722.90 → 1727.18] It's basically, hey, I did the tutorial thing
[1727.18 → 1730.46] or I did the problem, or I trained a model.
[1730.46 → 1734.36] Now, like, how do I not lose that model?
[1734.50 → 1735.22] Where does it go?
[1735.34 → 1736.16] How does it live?
[1736.42 → 1737.50] I think is the question.
[1737.94 → 1741.74] And maybe even how do you deploy it to some degree in terms of how does that move into the real world?
[1741.90 → 1743.12] What's your workflow for that?
[1743.56 → 1743.74] Yeah.
[1743.82 → 1745.40] So I guess one thing to clarify here,
[1745.40 → 1751.96] a lot of people think like an AI model is some sort of magical thing floating around in space
[1751.96 → 1754.96] that kind of materializes in some way.
[1755.08 → 1758.98] So an AI model is really just a function in software, right?
[1759.02 → 1761.32] So if you think of a function in software,
[1761.32 → 1763.82] it takes input, and it gives output, right?
[1764.18 → 1766.90] So how do you save a function in software?
[1767.08 → 1769.66] You just write it in a file, right?
[1769.66 → 1774.78] The difference with an AI model versus a normal software function is a normal software function
[1774.78 → 1779.24] maybe takes up whatever, let's say, 100 lines of code or whatever.
[1779.44 → 1780.92] And it might have some inputs.
[1781.06 → 1782.22] It might have some parameters.
[1782.96 → 1784.78] Maybe it reads some environmental variables.
[1785.02 → 1787.42] Maybe it parses a query string.
[1787.52 → 1789.90] Whatever it does, there are some parameters associated with it.
[1790.60 → 1793.12] Well, an AI model is no different.
[1793.26 → 1795.06] It's just a function in code.
[1795.06 → 1801.30] It's just that the parameter set, it might be kind of big, like a billion parameters or something.
[1801.40 → 1803.14] But it's really no different in practice.
[1803.30 → 1805.82] It's just all of that stuff is saved in a file.
[1806.40 → 1808.38] And then you run it in code.
[1808.86 → 1811.28] And so often what happens if you train a model,
[1811.48 → 1815.18] you just have to output it to a file that saves all of those parameters.
[1815.66 → 1818.44] And there's a bunch of different formats for that, like TensorFlow.
[1818.78 → 1821.06] You can output like proof and other things.
[1821.48 → 1823.30] PyTorch and others have their own structure.
[1823.30 → 1828.10] There's also like standardized, semi-standardized ways of doing this.
[1828.18 → 1834.58] So there's a format called Onyx, which is kind of takes a bunch of different things from different frameworks.
[1835.14 → 1836.96] So really, it's just that saving of the file.
[1837.02 → 1841.86] Then once you have it saved in terms of deployment, then you just need to load it back into code.
[1842.02 → 1847.76] Most of the time, like a framework like PyTorch or TensorFlow has like a load model function of some type.
[1847.96 → 1849.40] And then you just load the file.
[1849.84 → 1851.14] And then you can use it.
[1851.14 → 1856.20] Of course, you know, in terms of deployment, again, it's similar to any other software code.
[1856.42 → 1857.92] At least that's how I think about it.
[1858.24 → 1866.64] You know if you're deploying your code as, or you're deploying your model, and you want it to drive an API or some web app,
[1866.92 → 1869.96] likely you're going to deploy it as like a web service.
[1869.96 → 1881.00] So whatever code you have written for your web service, you need that code to execute that function that loads the model and then takes input and gives the output.
[1881.42 → 1883.54] So there's a bunch of different ways to do that.
[1883.80 → 1885.98] But that's the basics from my perspective.
[1885.98 → 1887.66] Yeah, I think it's funny.
[1887.76 → 1896.44] We're at a moment where the major platforms, and I'll kind of tackle it a little bit more from the deployment standpoint, kind of have their own systems.
[1896.70 → 1902.84] You know, since I've already acknowledged that I tend to be in the TensorFlow ecosystem, or they have TFX, which is TensorFlow Extended,
[1902.84 → 1909.80] which is, you know, what they refer to as an end-to-end platform for deploying production ML pipelines is how they say it.
[1910.06 → 1916.36] But in general, I think there's still a great deal of variability in the industry in terms of how different organizations do it.
[1916.44 → 1923.08] And their end targets in terms of where they want to get models deployed to for use often, you know, maybe it's in a data centre,
[1923.18 → 1926.20] maybe it's out on the edge somewhere, tends to be pretty customized.
[1926.20 → 1933.44] There's a lot of we've taken a system, but now we're going to add our own special, you know, need to it.
[1933.52 → 1938.72] And I know certainly in our own organization with some fairly unusual deployment targets by most people's standards,
[1939.10 → 1944.08] you know, we definitely have to come up with an approach that works for us.
[1944.58 → 1946.50] And so I think that's pretty typical.
[1946.64 → 1949.78] I don't think the world has settled in a standard way to do that.
[1949.78 → 1957.18] But I think the one thing, it's still a little bit of a, I think a lot of people perceive it as a bit of a dark art to do deployment at this point.
[1957.34 → 1961.42] And I think the thing I always remind people is it's really just software development at that point,
[1961.48 → 1962.88] which is kind of what you were alluding to.
[1962.96 → 1968.56] At the end of the day, you have a function, you know, it may be different from other functions in the number of parameters.
[1968.56 → 1972.66] And so you may have to accommodate in your architecture that you're deploying to.
[1972.90 → 1977.70] How are you going to get all the data in if you have many, many inputs into your model?
[1977.70 → 1982.28] You know, how do you get the data on time to that through the model at the correct thing?
[1982.34 → 1985.18] So that can affect your software and system architecture a bit.
[1985.60 → 1990.16] But other than that, I know I have a strong preference for deploying in containers.
[1990.62 → 1997.72] You know, whereas we may use Python as a language in training, I often use Go, the Go programming language for deployment,
[1997.88 → 2001.10] since you can access TensorFlow models for inference there.
[2001.48 → 2003.52] I like to wrap them up in a Docker container.
[2003.52 → 2006.98] And usually, if I have the option, deploy them into a Kubernetes cluster.
[2007.28 → 2010.74] And that can be, like I said, in a lot of different locations since it's pretty.
[2011.00 → 2017.42] But for the most part, it is as soon as you get done with training, you're really moving into a software deployment world again.
[2017.64 → 2021.16] And so, which is a little bit foreign to people who are just data scientists.
[2021.78 → 2028.16] But anyway, it's good because there's a lot of good, if the data science world can kind of figure out what it wants to do with that,
[2028.20 → 2030.92] there are a lot of good options there that are fairly mature.
[2033.52 → 2038.20] What's up?
[2038.28 → 2041.82] This is Daniel Whiten ack, one of your Practical AI co-hosts.
[2041.90 → 2046.02] And I hope you're enjoying this episode and staying healthy during these crazy times.
[2046.26 → 2049.92] I'm working on some pretty cool AI stuff here from my home office.
[2050.04 → 2056.72] But I've also found that I'm having to get a bit creative and be intentional when it comes to honing my AI skills
[2056.72 → 2059.42] and virtually connecting with the AI community.
[2059.42 → 2065.34] If you're in a similar situation, or you've been inspired by the practical AI we talk about on this show,
[2065.76 → 2071.82] I want to invite you to a live online AI training event I'm hosting this May called AI Classroom.
[2072.18 → 2079.66] In AI Classroom, I'm going to teach you the practical skills I've learned over the years using the latest open source AI technology.
[2079.66 → 2085.84] You'll learn AI theory along with practical hands-on implementations in both PyTorch and TensorFlow.
[2085.84 → 2092.80] And after the training, you'll be able to understand the latest AI models, implement your own models in code,
[2093.24 → 2097.58] train computer vision and NLP models, create model inference servers,
[2097.90 → 2101.40] and experiment with state-of-the-art methods like reinforcement learning.
[2102.06 → 2104.46] AI Classroom is taking place this May.
[2104.84 → 2111.44] It'll be taking place live and completely online in a high-quality virtual classroom, so no travel is required.
[2111.44 → 2116.66] There'll also be two cohorts with convenient time zones for eastern and western hemispheres.
[2117.22 → 2122.40] Don't miss out. Tickets and more information are available at datadan.io.
[2122.92 → 2124.66] That's datadan.io.
[2125.18 → 2130.72] And practical AI listeners can use the code practicalAI10 for 10% off.
[2131.14 → 2133.04] See you online in AI Classroom.
[2141.44 → 2145.96] All right, so let's do another one.
[2146.04 → 2147.30] Maybe this is a quick one.
[2147.56 → 2147.82] Okay.
[2148.00 → 2149.24] This seemed to be at the top.
[2149.38 → 2151.28] What laptop do I buy for deep learning?
[2151.28 → 2153.42] My answer is, doesn't matter.
[2154.20 → 2155.02] Yeah, mine too.
[2155.78 → 2159.02] I mean, you could buy one with a nifty GPU or something,
[2159.24 → 2164.42] but if you're using something like Cola Pro or something to do your initial testing,
[2164.42 → 2170.40] and then you're deploying on some giant cluster or something that your company has,
[2170.58 → 2171.78] it really doesn't matter.
[2171.94 → 2172.54] Buy a Chromebook.
[2173.64 → 2174.52] I'm the same.
[2174.78 → 2182.68] I think the biggest computing I do on my laptop is running a bunch of tabs of Chrome plus Slack
[2182.68 → 2184.10] simultaneously.
[2184.88 → 2187.72] It kind of maxes out my memory usage.
[2188.06 → 2188.94] So yeah, I don't know.
[2189.02 → 2190.34] That's my quick answer to that one.
[2190.78 → 2191.64] Don't know if you disagree.
[2192.16 → 2193.46] No, I would agree with you.
[2193.46 → 2197.76] I think a few years ago when we were talking, a lot of people,
[2197.92 → 2201.24] they might have a desktop just for training that they'd stick under their desk,
[2201.38 → 2204.42] and they'd buy a GPU to do that.
[2204.48 → 2206.54] But I don't see people doing that.
[2207.08 → 2207.56] Personal heater.
[2208.02 → 2209.58] Yeah, personal heater under your desk.
[2209.64 → 2210.10] That's right.
[2210.26 → 2211.52] Just what we need here in Georgia.
[2211.98 → 2213.28] I don't see that very much anymore.
[2213.42 → 2219.20] I think everyone goes to some form of cloud, whether it be one of the public cloud providers.
[2219.48 → 2221.26] I know, as we've talked about in past episodes,
[2221.26 → 2227.22] I'm super lucky at work in that we have a lot of super computing capability on the HPC side
[2227.22 → 2229.48] in terms of DGX clusters.
[2230.40 → 2231.62] So those are available.
[2232.02 → 2235.90] But when I'm coming home and when I'm working on my charitable work,
[2236.00 → 2238.86] where I'm applying some deep learning models for that,
[2239.28 → 2242.92] I'm hopping into Cola, and I'm using Google's cloud for that kind of work.
[2242.92 → 2248.22] And I think most people do the same in AWS or Google or Microsoft or whatever.
[2248.88 → 2249.22] All right.
[2249.50 → 2250.58] Next question.
[2250.88 → 2251.26] Let's see.
[2251.78 → 2254.68] Let's do another maybe theory-related one.
[2255.16 → 2258.60] What is backpropagation usually used for in neural networks?
[2259.20 → 2260.60] What is it used for?
[2260.72 → 2262.76] What is it used for in neural networks?
[2262.82 → 2263.48] That's the question.
[2263.66 → 2266.14] I think really the question is, what is backpropagation?
[2266.34 → 2267.00] Yeah, I think so.
[2267.00 → 2270.98] Because they've probably seen this term passed around.
[2271.20 → 2275.22] And normally when you write, or at least in tutorials that I've seen,
[2275.32 → 2278.40] when you write a code to train a neural network,
[2278.50 → 2283.56] most of the time there's not the run backpropagation function or something.
[2283.76 → 2285.48] Maybe it's not specifically called out.
[2285.56 → 2286.44] So maybe that's a confusion.
[2286.68 → 2290.66] What is backpropagation usually used for in neural networks?
[2290.66 → 2298.34] So backpropagation is basically just a method that's used fairly widely and ubiquitously.
[2298.58 → 2300.10] Is ubiquitously a word?
[2300.24 → 2300.80] That's a word.
[2300.92 → 2301.48] It is a word.
[2301.60 → 2302.08] It's a good word.
[2302.24 → 2303.74] In training neural networks.
[2303.74 → 2305.80] So it's used specifically at the training time.
[2305.92 → 2309.44] So if you think of what happens in training a neural network,
[2309.50 → 2313.78] we already mentioned that a neural network is basically just a function with all of these parameters.
[2313.78 → 2320.52] But the parameters are learned or set in this training process based on a bunch of example data.
[2320.66 → 2325.02] And so what happens is you kind of initialize these parameters to some values.
[2325.14 → 2326.74] Let's say we just randomize them.
[2326.88 → 2329.78] Then we make predictions based on that initial guess.
[2330.04 → 2335.80] And then we calculate a loss based on those predictions and what we know is the right answer.
[2336.14 → 2338.90] Which is an error rate essentially at the end of that.
[2338.96 → 2339.16] Yeah.
[2339.46 → 2341.32] So we calculate a bunch of errors together.
[2341.52 → 2346.48] And then we use however we calculated those errors or the loss function
[2346.48 → 2349.78] to then update our choice of parameters.
[2349.78 → 2353.58] What might be called weights and biases based on that loss.
[2353.58 → 2359.56] And the way in which we update that is often used as a derivative of this loss function.
[2360.06 → 2362.18] And so we update those weights and biases.
[2362.18 → 2365.16] And then we loop back to the beginning and try our predictions again.
[2365.16 → 2367.38] And then we iterate over that a bunch of times.
[2367.38 → 2371.46] And that process of sort of iteratively updating the weights and the biases
[2371.46 → 2378.56] and propagating those changes back into the network is what's called back propagation.
[2378.94 → 2380.46] So it's just this methodology.
[2380.94 → 2382.12] Did I miss anything there Chris?
[2382.24 → 2383.18] No I think you got it.
[2383.24 → 2386.60] I think you mentioned randomizing in the beginning.
[2386.80 → 2392.94] And so that first time through you're definitely not optimized to solve for the thing that your network is trying to learn.
[2392.94 → 2395.72] And so it's usually substantially off.
[2395.72 → 2400.48] And you can think of each back prop when it goes back to those weights as it's tweaking all the weights
[2400.48 → 2403.08] and all the little connections in the network.
[2403.18 → 2404.16] And then it tries again.
[2404.32 → 2407.00] And each time it tweaks you know it tests.
[2407.22 → 2412.18] And through the loss function it works its way closer and closer to a low amount of error.
[2412.74 → 2417.02] And there's some point where you decide it's good enough as the person training the network.
[2417.02 → 2420.52] And you say when it gets to that low of an error rate we're good to go.
[2420.66 → 2424.52] And that's what back propagation tries to do in a feed forward network.
[2425.10 → 2425.18] Yeah.
[2425.52 → 2428.74] Well Chris what other questions seem interesting to you?
[2429.04 → 2429.42] Okay.
[2429.60 → 2430.08] Let's see.
[2430.20 → 2434.36] How about this is something that I get a lot at conferences, actually.
[2434.64 → 2439.18] And that is how will AI replace or change things in our lives?
[2439.18 → 2441.12] What does AI replace?
[2441.44 → 2446.46] And how does it take the place of or modernize other aspects of business, government,
[2446.46 → 2450.36] education, human communication, and other aspects of daily life?
[2450.44 → 2454.92] So it's a really broad wide open question with a thousand possible answers.
[2455.14 → 2456.64] But you know take a shot at it Daniel.
[2457.50 → 2462.10] I mean to me, I think that it's more of an augmentation than a replacement.
[2462.62 → 2464.82] And I mean I don't mean to minimize.
[2465.12 → 2469.80] There's certainly areas where people have been greatly affected through you know automation
[2469.80 → 2470.72] and that sort of thing.
[2470.80 → 2471.74] So not to minimize that.
[2471.74 → 2477.14] But I think on the whole it's really not so much of a replacement as an augmentation.
[2477.82 → 2484.68] You know like for me, I can now have a really super awesome autocomplete in Gmail that really
[2484.68 → 2485.94] works fast and great.
[2486.48 → 2490.12] It didn't replace even that system for me right?
[2490.20 → 2491.40] Like Gmail or email.
[2491.62 → 2494.08] It didn't replace that part of my life.
[2494.18 → 2496.64] It just kind of augmented it in a certain way.
[2496.64 → 2501.26] And I think it's similar if you look at like healthcare and the way AI is helping doctors
[2501.26 → 2502.98] and that sort of thing.
[2503.10 → 2505.44] That's my general take on it.
[2505.76 → 2506.62] No I agree with you.
[2506.70 → 2508.80] I think augmentation is the right word for it.
[2508.88 → 2513.94] And I think folks need to keep in mind that where AI is today you know as we've talked about
[2513.94 → 2518.34] you know a little while ago in this same episode you know it's primarily deep learning.
[2518.88 → 2524.80] And as we are thinking about it deep learning can be very, very good at addressing very
[2524.80 → 2526.08] specific things.
[2526.32 → 2532.90] And so the way that is realized in real life is that it will help us recognize images better
[2532.90 → 2536.50] than other algorithms we were using before you know with that convolutional neural network
[2536.50 → 2537.28] that we talked about.
[2537.62 → 2542.36] It enables us to do other mundane things faster and more efficiently and optimize.
[2542.94 → 2547.44] But each one is tackling a very specific efficiency if you will.
[2547.92 → 2553.50] And so what we're seeing is we're becoming more productive by using these models in all sorts
[2553.50 → 2554.66] of different ways in our life.
[2555.12 → 2560.04] And whether that's government education, human communication, you know education whatever
[2560.04 → 2564.92] all these things are just about how can I add this in and make it just a little bit better.
[2564.92 → 2570.16] I think you're more in danger if you're in a very specialized or mundane job you know in
[2570.16 → 2572.12] terms of a model coming to replace.
[2572.34 → 2577.22] But there's a big difference between what a human brain can do today and what any of these
[2577.22 → 2580.76] deep learning models can do in terms of comprehensiveness.
[2580.76 → 2583.94] The world may change, and maybe we'll have to revise that at some point.
[2584.04 → 2586.96] But right now you know the two it's an apple versus an orange.
[2587.10 → 2589.28] It's not it's its not a direct competition yet.
[2589.62 → 2589.80] Yep.
[2590.66 → 2591.02] Okay.
[2591.10 → 2592.00] Here's a quick one.
[2592.18 → 2592.44] Okay.
[2592.94 → 2598.18] Is it possible for a paper to report wrong accuracy or am I doing something terribly wrong?
[2598.32 → 2600.48] All of my papers probably report.
[2602.08 → 2607.58] So obviously this is someone trying to reproduce some results from an academic paper or something
[2607.58 → 2611.70] where they reported like state-of-the-art results on this or that.
[2611.90 → 2615.38] Yeah it happens, and it's you know don't feel bad.
[2615.90 → 2617.08] I don't have anything to add to that.
[2617.18 → 2617.90] That's that's it.
[2618.10 → 2618.52] That's it.
[2618.84 → 2620.02] That's the final word right there.
[2620.14 → 2623.48] So unfortunately not everything published is correct.
[2623.96 → 2625.26] So just keep that in mind.
[2626.12 → 2626.78] Let's see.
[2626.98 → 2629.32] Maybe we can move on to another fun one here.
[2629.58 → 2630.94] What sucks about AI?
[2631.28 → 2632.70] That's a question on the internet.
[2633.20 → 2634.80] What sucks about AI Chris?
[2634.80 → 2638.98] I don't know if we want to add this one into our podcast because our podcast is about AI.
[2639.28 → 2642.98] Just to note if AI sucks that doesn't mean our podcast sucks.
[2643.26 → 2644.16] Just to clarify.
[2645.04 → 2651.16] So I have one, and we've talked about this before, and you have this pardon me creepy like for
[2651.16 → 2653.10] what I'm about to say, and you know what it is now don't you?
[2653.18 → 2653.54] I do.
[2653.82 → 2654.06] Yeah.
[2654.06 → 2659.76] It's preparing data for training and trying to pull all the bits together and put them
[2659.76 → 2665.98] into a shared context and clean it up and do all the things you have to do to have
[2665.98 → 2669.36] a great training set so that you have very efficient training.
[2669.70 → 2675.74] And I know for me for every hour of delight I have at training a model that does just what
[2675.74 → 2676.20] I want.
[2676.32 → 2678.80] I have many hours of this drudgery.
[2679.26 → 2683.70] And I know that you have this strange likeness to do that.
[2683.70 → 2685.34] I do.
[2685.48 → 2686.72] I enjoy data.
[2686.92 → 2688.20] It's crazy wrangling.
[2688.52 → 2688.68] Yeah.
[2688.72 → 2689.82] I think it's fairly fun.
[2690.34 → 2690.82] I don't know.
[2690.90 → 2692.32] Not many sucks about AI.
[2692.64 → 2694.50] So maybe that's a cop out answer.
[2695.06 → 2697.52] And maybe it sucks that I don't know.
[2697.54 → 2698.96] I think things are changing with this.
[2699.04 → 2705.30] Maybe it sucks that you know a lot of people that are benefiting from AI are those in you
[2705.30 → 2712.36] know developed countries and people in you know the US or Europe or wherever it is.
[2712.84 → 2717.58] And you know it's probably not benefiting the rest of the world in the same way.
[2717.66 → 2720.60] So maybe that sucks about AI, but hopefully that's changing.
[2720.60 → 2725.70] So there's a challenge to everybody out there listening is that we need to find a way to
[2725.70 → 2732.08] democratize this amazing technology that so many of us have kind of devoted our professional
[2732.08 → 2739.04] lives to and like Daniel is doing at SIL find ways to bring AI to other people.
[2739.34 → 2744.80] I know in my case animals being the animal lover bring it to use cases and people and
[2744.80 → 2747.92] communities that need it and that are not yet receiving it.
[2748.40 → 2753.16] I know you're spending all of your time doing that, and I spend all of my spare time trying
[2753.16 → 2755.84] to do that, and I'm hoping others will do the same.
[2756.72 → 2757.28] Yeah for sure.
[2757.80 → 2758.08] All right.
[2758.08 → 2764.20] Well maybe as we wrap up there's one of these questions which is practical but also
[2764.20 → 2770.60] you know I know we get asked a lot which is recommendations for self-studying machine learning
[2770.60 → 2772.82] or self-studying AI.
[2773.96 → 2779.60] So if is any of this stuff that we've randomly talked about has been interesting for you we
[2779.60 → 2783.44] hope it has maybe you want to dive into a few of these topics.
[2783.44 → 2788.02] What are some of your go-to sources for good self-study information Chris?
[2788.08 → 2792.46] Yeah well I'll speak specifically of what my current interest is, and we've talked about
[2792.46 → 2795.90] things and this shows my bias that I'm in the TensorFlow ecosystem.
[2796.24 → 2803.68] Google has now a certificate program out there where you can go and actually get certified
[2803.68 → 2808.38] in your TensorFlow expertise, and it is not an easy certificate to get.
[2808.48 → 2813.00] I will warn you this is not an intro level thing but if you've been in this space for a
[2813.00 → 2818.44] while, and you think that you're pretty good in your usage of TensorFlow and you want
[2818.44 → 2819.82] to be able to establish it.
[2819.90 → 2823.18] I know that there have been third parties with certificates, but they're not taken very
[2823.18 → 2829.16] seriously but now with the TensorFlow team itself sponsoring this certification process
[2829.16 → 2831.44] and you actually don't have to go into a testing centre.
[2831.44 → 2837.74] It's good for a COVID-19 reality that we're all in is that you can do it from home on your laptop
[2837.74 → 2843.40] and they have a mechanism you're allowed up to five hours to get your test done, and they test you and
[2843.40 → 2848.00] everything from use of CNNs to natural language processing.
[2848.50 → 2852.02] There's a whole curriculum that you have to prove yourself on in those five hours.
[2852.54 → 2857.76] So if you really want to see how good you are I would encourage you to go give that one a shot.
[2857.76 → 2864.16] I think it's $100 which isn't too bad to go get the certification and that's a good way to go from
[2864.16 → 2868.32] kind of beginner to our intermediate level to prove that maybe you're at an intermediate to
[2868.32 → 2868.94] advanced level.
[2869.84 → 2874.74] Yeah and there's been a bunch of things we've mentioned on the podcast just to list a few of
[2874.74 → 2875.64] those as reminders.
[2876.06 → 2879.18] People really love the fast.ai content.
[2879.84 → 2886.06] If you just search for fast.ai you'll find that that seems to be pretty unanimously liked.
[2886.06 → 2886.44] It is.
[2886.44 → 2887.48] It's great content.
[2887.48 → 2891.30] By people that are in this space so that's a good recommendation.
[2891.50 → 2892.80] It's definitely not the only one.
[2893.12 → 2896.96] There's another kind of crash course that's free from Google with TensorFlow.
[2897.42 → 2900.52] There are great tutorials on PyTorch.
[2900.68 → 2908.78] There's I've been kind of exploring this dive into deep learning site recently d2l.ai and they
[2908.78 → 2913.84] have a bunch of notebooks to explore and there are other great books out there.
[2913.84 → 2921.74] One that has been always a great use to me for actually many years and has been recently
[2921.74 → 2927.62] updated is Joel Groove's book Data Science from Scratch which now includes a bunch more
[2927.62 → 2932.74] things related to deep learning and RNNs and CNNs.
[2932.74 → 2938.12] And he'll give you a lot better explanation of a CNN in his book than I gave.
[2938.12 → 2940.00] And he came on the show a while back as well.
[2940.38 → 2941.38] He did.
[2941.52 → 2941.68] Yeah.
[2941.82 → 2943.28] And I love that.
[2943.34 → 2946.12] It's a great reference for me as I do my work.
[2946.12 → 2948.06] So there are some recommendations.
[2948.36 → 2953.34] Hopefully you've enjoyed the back and forth question answering of the show.
[2953.40 → 2956.26] It's been a bit random, but some good discussion, Chris.
[2956.32 → 2956.90] I enjoyed it.
[2957.12 → 2957.84] I had a fun time.
[2957.90 → 2958.28] It was good.
[2958.60 → 2959.26] And you know what?
[2959.30 → 2965.04] Next time I'll promise listeners will ask for questions out there on social media with
[2965.04 → 2969.24] a bit more warning than we did today so that we can have a lot of people participate
[2969.24 → 2970.62] in feeding it to us.
[2971.26 → 2971.96] Sounds great.
[2972.14 → 2972.80] See you soon, Chris.
[2973.02 → 2973.32] All right.
[2973.32 → 2973.70] Thanks a lot.
[2973.76 → 2974.06] Take care.
[2976.12 → 2979.84] Thank you for listening to Practical AI.
[2980.30 → 2982.40] We appreciate your time and your attention.
[2982.94 → 2984.52] Next up, let your voice be heard.
[2984.66 → 2986.76] Please leave us a comment on the episode page.
[2986.86 → 2988.76] There's a link in your show notes for easy clickings.
[2989.10 → 2989.98] We'd love to hear from you.
[2990.64 → 2993.96] Word of mouth is the number one way people find new podcasts.
[2994.44 → 2998.02] If Practical AI has helped you on your AI journey, please do tell a friend.
[2998.14 → 2999.36] Hey, they'll thank you later.
[2999.98 → 3004.52] Special thanks to Break master Cylinder for the beats and to our awesome partners for their support.
[3004.52 → 3007.44] Shout out to Vastly, Linde, and Rollbar.
[3008.42 → 3009.34] That's all for now.
[3009.76 → 3010.96] We'll talk to you again next week.
[3010.96 → 3040.94] Thank you.
