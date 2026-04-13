[0.00 --> 8.66]  Welcome to Practical AI.
[9.14 --> 17.12]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing
[17.12 --> 19.58]  the world, this is the show for you.
[20.22 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 30.94]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions
[30.94 --> 35.44]  on six continents, so you can launch your app near your users.
[35.84 --> 37.84]  Learn more at Fly.io.
[42.12 --> 47.90]  Hello and welcome to another fully connected episode of the Practical AI podcast.
[47.90 --> 53.76]  In these fully connected episodes, we keep you connected with everything that's happening
[54.92 --> 60.32]  to the world and help you find some resources to level up your machine learning game.
[60.72 --> 62.12]  My name is Daniel Whitenack.
[62.22 --> 66.68]  I'm founder and CEO at Prediction Guard, where we're safeguarding private AI models.
[67.02 --> 73.70]  And I'm joined, as always, by my co-host, Chris Benson, who is a principal AI research engineer
[73.70 --> 74.80]  at Lockheed Martin.
[75.12 --> 75.80]  How are you doing, Chris?
[76.04 --> 77.28]  I'm doing good today, Daniel.
[77.34 --> 78.06]  How's it going with you?
[78.06 --> 80.24]  It's all good.
[80.36 --> 86.46]  Yeah, I got the chance last week to visit Boston and see a bunch of cool stuff, tour
[86.46 --> 89.90]  a few labs around MIT, which was a lot of fun.
[90.26 --> 99.30]  I toured a couple labs where they're using AI to make proteins, like drug candidate proteins.
[99.52 --> 100.08]  Very cool.
[100.08 --> 104.72]  So the idea is one of the companies literally named AI proteins.
[104.94 --> 106.80]  Hopefully we can have them on the show sometime.
[107.38 --> 110.16]  I requested their CEO while I was there.
[110.44 --> 111.48]  He was giving us the tour.
[111.76 --> 119.62]  But yeah, the idea being that you can use various AI-driven methodologies to explore the
[119.62 --> 123.58]  space of proteins for drug candidates.
[123.78 --> 126.28]  And they're kind of binding to certain stuff.
[126.34 --> 129.22]  I'm not a biologist or anything like that.
[129.22 --> 135.66]  But then they take those and then synthesize them in the lab and test them and eventually
[135.66 --> 142.66]  hope to get them into drug candidates and through FDA testing and all of that stuff.
[142.78 --> 143.60]  So it's pretty cool.
[143.94 --> 145.20]  I would love to have them on the show.
[145.68 --> 151.96]  I've loosely followed that field over the last couple of years, largely because someone
[151.96 --> 159.06]  that I used to work for is a chemistry PhD from Harvard, but is very familiar with biotech.
[159.06 --> 161.40]  So he's kind of kept me up to date on some of that.
[161.86 --> 162.76]  It sounds fascinating.
[163.06 --> 168.04]  I know that drug discovery is really all about AI these days.
[168.14 --> 170.10]  I think that's where all the action is happening in that field.
[170.58 --> 170.70]  Yeah.
[170.78 --> 176.40]  And it's pretty amazing, at least from what I've heard from a couple of those companies,
[176.50 --> 182.62]  just the hopefully the speed, like the orders of magnitude faster that they'll be able to
[182.62 --> 186.20]  explore the solution space, I guess.
[186.20 --> 194.74]  So testing thousands and thousands of drug candidates very quickly rather than maybe a
[194.74 --> 201.80]  postdoc or a PhD testing only a handful over the course of many weeks or even years.
[201.92 --> 205.32]  They're able to do things much faster, which is really interesting.
[205.32 --> 212.14]  And of course, they're exploring that really useful application of that technology.
[212.28 --> 218.04]  But I guess this is one of the reasons that some people might have sort of ethical concerns
[218.04 --> 223.88]  with some of this stuff, because it's kind of like you can apply the technology in a really
[223.88 --> 226.50]  positive way and explore drug candidates.
[226.98 --> 232.58]  I'm sure you could also think about things that would be harmful to humans and even think
[232.58 --> 238.06]  about like biological weapons and that sort of thing and explore that solution space in
[238.06 --> 238.64]  the same way.
[238.76 --> 241.96]  And those sorts of things don't need FDA approval.
[242.68 --> 248.36]  So, yeah, I imagine that there's people smarter than me that have thought more deeply about
[248.36 --> 249.26]  those concerns.
[249.26 --> 255.84]  And I know it was mentioned, I think, in our last round of interviews about Mozilla's report
[255.84 --> 257.04]  on AI this last year.
[257.10 --> 258.14]  We had an episode on that.
[258.24 --> 260.04]  But yeah, I was thinking about that while I was there.
[260.14 --> 261.88]  It sort of cuts both ways, I guess.
[261.88 --> 262.70]  It does.
[262.90 --> 267.96]  It's just since you mentioned that, I know in kind of the defense and intelligence world
[267.96 --> 275.30]  with AI capabilities being the great equalizer, the idea of malignant forces in the world
[275.30 --> 280.44]  deciding to focus on such things, which incidentally is very illegal under international law.
[280.60 --> 280.80]  Right.
[280.90 --> 283.90]  But certain places in the world don't care so much about that.
[284.42 --> 286.04]  And so we'll have to see.
[286.04 --> 292.48]  I've had a lot of conversations about the very good and the very bad about AI with folks
[292.48 --> 296.84]  lately and what an uncharted world we're moving into at this point.
[297.22 --> 297.34]  Yeah.
[297.54 --> 297.80]  Yeah.
[297.86 --> 299.08]  Well, I'm very happy.
[299.18 --> 305.18]  At least the people that I've run across are quite ethical and moving towards things that
[305.18 --> 307.58]  will hopefully benefit us all.
[307.58 --> 315.46]  But speaking of benefit to many people, there was something rolled out this week that definitely
[315.46 --> 323.22]  caused a bit of a stir and also instantly appeared on a bunch of people's phones and devices.
[323.22 --> 332.58]  And that was the next GPT, GPT-40, standing for OMNI, if I got that right.
[332.72 --> 335.00]  GPT-40 OMNI.
[335.30 --> 341.22]  I don't know the full background of that naming, if it's meant to evoke omniscience or...
[342.22 --> 346.08]  I think the explanations I've seen have been about multimodality.
[346.30 --> 346.54]  Yes.
[346.54 --> 350.70]  You know, just the fact that it can photographic, video, voice, everything.
[351.40 --> 354.02]  And yes, it was quite a release.
[354.48 --> 359.44]  You know, everybody's been talking about upcoming, the expected release in the summer, potentially,
[359.62 --> 360.52]  of GPT-5.
[361.12 --> 364.88]  You know, interestingly enough, this came out and was quite...
[364.88 --> 367.90]  Even though it's still part of that four family, it's had quite an impact.
[368.06 --> 373.62]  I know that in the last week, I will say that it's been the most open app on my phone,
[373.78 --> 375.38]  pretty much around the clock.
[375.66 --> 375.92]  Yeah.
[375.92 --> 380.30]  It's starting to feel like a family member because it's involved in all of our family
[380.30 --> 382.28]  decisions, trying to...
[383.84 --> 388.48]  Things like getting a leak in the drywall and trying to use it to do something as mundane
[388.48 --> 390.30]  as figure out the plumbing concerns.
[390.86 --> 395.32]  And it seems to be, you know, when my wife and I are talking about household things, we
[395.32 --> 398.36]  now have ChatGPT as a third party and all those conversations.
[398.70 --> 400.56]  It seems to have supplanted my daughter.
[400.70 --> 402.08]  I'm not sure she likes it very much.
[402.72 --> 403.16]  Yeah.
[403.16 --> 410.52]  Well, since you have been getting hands-on and using GPT-4.0 quite a bit, for you either
[410.52 --> 415.44]  in the announcement or in your own use of it, what are those things that stand out as
[415.44 --> 422.16]  the things that have changed from, let's say, GPT-4 to GPT-4.0?
[422.16 --> 426.00]  Well, I don't have a list of things in front of me at this moment or anything, but things
[426.00 --> 430.96]  that I've certainly experienced is it is much faster than just GPT-4 had been.
[431.38 --> 435.74]  It's able to respond very quickly in any of the modalities that we're talking about.
[436.16 --> 441.48]  And when you say modalities, you're meaning sort of text, speech, image.
[441.48 --> 442.50]  That's correct.
[442.50 --> 443.84]  It seems much faster.
[443.96 --> 448.56]  I haven't measured it across the board, but I think the thing that's been notable in my
[448.56 --> 454.60]  own workflow of it is that I'm not having to wait around and kind of figure it out.
[454.82 --> 459.80]  And, you know, before this week, I'd kind of say, okay, I'm going to get onto GPT-4 and
[459.80 --> 460.66]  ask it a question.
[460.78 --> 463.16]  I kind of stop everything when I'm doing and do that.
[463.16 --> 467.88]  Um, and I think the difference is the thing that's really impacted me the most is maybe
[467.88 --> 473.30]  the subtleness of no longer waiting around, being able to do it just by speaking and being
[473.30 --> 474.10]  spoken to.
[474.54 --> 478.70]  And it's no longer a stop and do something kind of activity.
[478.70 --> 483.88]  It's now as I'm doing it, uh, as we're in the middle of conversation, it just becomes
[483.88 --> 484.78]  part of the conversation.
[485.06 --> 487.12]  I don't tell my wife, uh, hold on one second.
[487.22 --> 491.24]  Um, I'm going to check real quick on this question with GPT-4 and let's see what it says.
[491.24 --> 493.42]  And then we can, you know, take that into account as we talk.
[493.50 --> 496.08]  Now it's just like right there at the kitchen table.
[496.18 --> 496.86]  We just do it.
[497.20 --> 499.30]  So third party in the conversation.
[499.50 --> 500.68]  Dueling GPTs.
[501.02 --> 501.74]  Yeah, that's right.
[502.30 --> 502.98]  That's right.
[502.98 --> 503.54]  Yeah.
[503.80 --> 510.08]  I think that some of the main features, uh, if, if people haven't been following it quite
[510.08 --> 515.64]  as much in the news, which I'm sure a lot of, a lot of our listeners have been following
[515.64 --> 516.80]  it quite closely.
[517.16 --> 519.62]  One thing that they focused on was speed.
[519.62 --> 528.36]  So in particular with the voice response, when your voice is kind of recorded in, then they're
[528.36 --> 533.84]  talking about responding in milliseconds rather than I think before it was a few seconds, something
[533.84 --> 537.00]  like that, which of course, uh, is much faster.
[537.26 --> 543.14]  I think in general, it's a fast model, uh, in my understanding, in terms of response and
[543.14 --> 545.16]  streaming across the modalities.
[545.16 --> 555.12]  Also it's in terms of access, both account wise and cost wise, another drop in costs as
[555.12 --> 558.46]  far as the cost for the performance goes.
[558.66 --> 561.08]  So that's a trend that I think continues.
[561.32 --> 568.82]  And also one of the things I was happy to see was most of the GPT models over time have
[568.82 --> 575.10]  penalized you basically in terms of token count for putting in languages other than English,
[575.10 --> 578.32]  because you would get higher token counts.
[578.68 --> 583.64]  And if you're charged by how many tokens you put in or generate out, and let's say you're
[583.64 --> 588.80]  putting in Korean or something like that, then it's actually more expensive to use the
[588.80 --> 590.52]  tool in those other languages.
[590.52 --> 595.14]  So I think they, at least in my understanding from what I've read, I don't know if that's
[595.14 --> 598.30]  fully equitable at this time.
[598.56 --> 605.26]  Um, but there was a, an effort to kind of correct some of those issues as they came up.
[605.26 --> 605.58]  Yeah.
[606.04 --> 608.22]  Have you used the video features much?
[608.22 --> 613.88]  I've, I have a bit and it's very good compared to things that have come before, but sometimes
[613.88 --> 617.62]  it seems to get amazing context and occasionally it struggles a little bit.
[617.62 --> 621.38]  I think it depends on how much context it's able to get out of the imagery.
[621.88 --> 621.96]  Yeah.
[622.06 --> 626.78]  I've mostly used this sort of image related stuff, uh, versus video.
[626.92 --> 634.42]  So, uh, audio and text and image is kind of what I've done, but yeah, they show a good
[634.42 --> 643.52]  number of things in the demo videos related to, uh, video and also even kind of combining
[643.52 --> 650.80]  one version of this running with another version and having interactions between the two and
[650.80 --> 654.82]  interview prep with the tool and all sorts of cool stuff.
[654.98 --> 660.00]  So if people haven't seen it, I definitely recommend that people go and check out the
[660.00 --> 663.26]  demos to kind of get a sense of the performance.
[663.26 --> 665.50]  But yeah, it's overall quite impressive.
[665.50 --> 671.04]  The subtlety of being able to do these things with that reduced time and across modalities,
[671.26 --> 677.30]  you know, while it might not be whatever giant jump that upcoming GPT-5 would be, the fact
[677.30 --> 682.08]  that it's changing our behaviors and the way that we're using it in this last week and enabling
[682.08 --> 684.04]  things that just weren't practical before.
[684.04 --> 690.46]  I think that really makes a difference going forward to the point where, um, I work with, uh, here in the
[690.46 --> 694.24]  Atlanta area, I work with some of the local universities in their various computer science
[694.24 --> 696.22]  colleges and schools and such.
[696.42 --> 702.88]  And, uh, I was at one on Friday for a kind of a day long, uh, strategic planning meeting on computer
[702.88 --> 705.02]  science and where they were going with it.
[705.02 --> 710.00]  And we were talking about this while we've been talking about AI's impact, obviously at any kind of
[710.00 --> 716.24]  computer science program, this may change not only what you can do, but education as well in a,
[716.28 --> 720.84]  in a pretty fundamental way in terms of teaching and being able to do it in real time and stuff.
[720.84 --> 727.46]  And we had, uh, quite a rich conversation around, it lasted quite a while, uh, around how we might
[727.46 --> 732.24]  be able to utilize these new capabilities in the classroom going forward and also how it might
[732.24 --> 732.90]  change curriculum.
[732.90 --> 738.26]  So I think we're really starting to get to a point where I think a lot of new capabilities in
[738.26 --> 739.96]  education are right around the corner.
[740.00 --> 757.68]  If you're anything like me, you have a certain tendency to put things off until the very last
[757.68 --> 758.28]  minute.
[758.40 --> 764.44]  Seeing the dentist, going to the doctor, home improvements, that never ending chore list of
[764.44 --> 764.88]  yours.
[765.36 --> 769.28]  And while most of the time it works out just fine, the one thing in life that you really
[769.28 --> 773.88]  cannot afford to wait on is setting up term coverage, life insurance.
[774.14 --> 778.60]  You've probably seen life insurance commercials on TV and thought, yeah, I'll look into that
[778.60 --> 779.20]  later.
[779.66 --> 781.08]  No, later doesn't come.
[781.36 --> 782.74]  This really isn't something you can wait on.
[783.02 --> 785.62]  Choose life insurance through a ladder today.
[786.02 --> 787.78]  Here's what we love about ladder.
[787.96 --> 793.08]  And while we allow them as a sponsor, they are a hundred percent digital, no doctors, no needles,
[793.08 --> 794.08]  no paperwork.
[794.08 --> 798.56]  When you apply for $3 million in coverage or less, just answer a few questions about your
[798.56 --> 799.74]  health in an application.
[800.32 --> 804.40]  Ladder's customers rate them 4.8 out of five stars on Trustpilot.
[804.78 --> 807.58]  And they made Forbes best life insurance 2021 list.
[807.94 --> 810.76]  You just need a few minutes and a phone or laptop to apply.
[811.12 --> 813.58]  Ladder's smart algorithm works in real time.
[813.64 --> 816.72]  So you'll find out if you're instantly approved, no hidden fees.
[816.72 --> 822.54]  You can came to any time, get a full refund if you change your mind in the first 30 days.
[822.94 --> 828.52]  Ladder policies are issued by insurers with long proven histories of paying claims.
[828.90 --> 832.20]  They're rated A and A plus by A.M.
[832.28 --> 832.66]  Best.
[833.02 --> 836.54]  Finally, since life insurance costs more as you age now.
[836.98 --> 837.60]  Yeah, right now.
[837.88 --> 839.58]  Now's the time to cross it off your list.
[839.58 --> 846.92]  So go to ladderlife.com slash practical AI today to see if you're instantly approved.
[847.20 --> 851.64]  Again, that's ladder.com slash practical AI.
[851.78 --> 857.16]  L-A-D-D-E-R life.com slash practical AI.
[869.58 --> 882.90]  I'm having a discussion with my podcast co-host Chris about the new GPT-4.0 model.
[883.38 --> 884.66]  What do you think we should talk about?
[884.66 --> 887.30]  That sounds like a great topic for your podcast.
[887.70 --> 891.18]  You could discuss how GPT-4.0 compares to previous versions,
[891.62 --> 894.28]  especially in terms of its capabilities and improvements.
[894.84 --> 897.52]  Delve into its applications across different industries,
[897.52 --> 900.78]  like healthcare, creative arts, or customer service,
[901.12 --> 903.32]  and consider exploring the ethical implications,
[903.86 --> 906.64]  including privacy concerns and bias in AI.
[906.98 --> 910.06]  It might also be interesting to discuss real-world case studies
[910.06 --> 913.48]  or predictions about how AI will evolve in the future.
[913.48 --> 917.14]  What do you think your listeners would be most interested in hearing about?
[917.60 --> 919.90]  Well, a lot of that seems pretty interesting.
[920.38 --> 921.36]  You mentioned healthcare.
[921.82 --> 923.80]  What were you thinking in relation to healthcare?
[925.38 --> 927.36]  Sorry, I'm having issues right now.
[927.52 --> 929.54]  Our systems are experiencing heavy load.
[929.86 --> 931.00]  Please try again later.
[931.20 --> 933.22]  Well, at least I'm not the only one having issues.
[933.38 --> 938.28]  At least I know that Chad GPT-4.0 has issues itself at times.
[938.46 --> 941.86]  There's something slightly satisfying about that, I must say.
[942.40 --> 945.16]  Yeah, well, it was doing pretty good there
[945.16 --> 949.10]  until it had volume issues or whatever they're experiencing,
[949.36 --> 950.68]  and I got cut off.
[950.80 --> 952.04]  I'm going to call it a mental blank.
[952.20 --> 953.78]  You know, I have those from time to time.
[953.78 --> 955.44]  You know, I'm just going to say it.
[956.12 --> 962.80]  So what do you, Chris, our friend over in the chat GPT world,
[963.10 --> 970.70]  chat GPT-4.0, suggested some things about privacy concerns as related to AI.
[970.88 --> 973.62]  I probed a little bit healthcare-related things,
[973.62 --> 976.78]  but it wasn't able to give me an answer and got bogged down.
[976.78 --> 979.50]  But it also mentioned privacy concerns.
[980.36 --> 984.12]  Yeah, have you thought about that as you've obviously been using the system?
[984.38 --> 991.26]  What changes now in terms of privacy now that we have 4.0 and not 4?
[991.34 --> 992.64]  How is it different, if at all?
[992.64 --> 993.96]  I think it is.
[994.08 --> 998.86]  And this is a topic that has come up quite a bit this past week in various online forums.
[999.12 --> 1003.72]  There was a particular LinkedIn post, I'll try to find it and include it in the show notes if I can,
[1004.14 --> 1005.10]  that brought it up.
[1005.22 --> 1010.38]  And with us now talking to it and receiving it back, how does that impact?
[1010.52 --> 1011.50]  Is this recording?
[1011.70 --> 1012.70]  Is it not recording?
[1013.00 --> 1015.38]  How does this qualify under different state laws?
[1015.56 --> 1018.92]  When we were busy typing it in and getting our questions back,
[1018.92 --> 1024.70]  while there were privacy concerns, it wasn't extending now to audio recording of voices,
[1025.00 --> 1029.34]  which is covered under state laws of all states in the U.S. at least,
[1029.42 --> 1031.44]  and I'm sure many countries out there.
[1031.98 --> 1032.56]  What do you think?
[1032.62 --> 1033.22]  I'm just curious.
[1033.40 --> 1039.46]  Neither of us are attorneys, but now that we're leaving our phones open to chat GPT
[1039.46 --> 1043.14]  and capturing people, I'm sure, I've done it in public places a bunch this week.
[1043.74 --> 1045.44]  So how do you think that impacts?
[1045.74 --> 1047.22]  Do we need to tell everyone we're doing it?
[1047.28 --> 1048.22]  Okay, everyone, quiet.
[1048.22 --> 1050.68]  Everyone, okay, I'm starting chat GPT-4.
[1051.14 --> 1054.94]  It's weird because it's some of the same feelings I think people had originally
[1054.94 --> 1058.90]  when they started bringing Alexa's or Google Homes into their home,
[1059.04 --> 1062.88]  and it was sort of always supposedly not listening,
[1063.24 --> 1066.52]  but it had to be listening at least to get the wake word, right?
[1066.76 --> 1066.94]  Yep.
[1066.96 --> 1071.36]  So there was this awkwardness there in terms of what's actually being recorded
[1071.36 --> 1073.48]  and that sort of thing.
[1073.48 --> 1078.36]  I think the difference here, you kind of almost got there when you were talking about
[1078.36 --> 1080.46]  how you were using it in your everyday life.
[1080.56 --> 1084.82]  I think people can see that this technology because there's a quick response.
[1085.44 --> 1089.46]  So there's, as I was playing that, like you could tell the first response that I got from
[1089.46 --> 1091.98]  chat GPT was pretty quick.
[1091.98 --> 1094.58]  I would say it's still not quite like you and me talking.
[1094.78 --> 1096.10]  It's not natural, right?
[1096.18 --> 1097.80]  But it's pretty quick.
[1098.36 --> 1101.44]  And so there's this tendency then to think,
[1101.54 --> 1103.68]  oh, well, I can leave this on at certain times.
[1103.68 --> 1106.92]  Or like you say, have it as part of the dinner table conversation.
[1106.92 --> 1111.86]  You kind of then bring in these devices like the meta AI glasses.
[1112.22 --> 1118.20]  And like, maybe I just have chat GPT watching what I'm watching through my meta AI glasses
[1118.20 --> 1120.40]  and telling me about this or that.
[1120.52 --> 1123.56]  And so you've got all of these modalities coming together.
[1123.56 --> 1128.26]  It's recording in your kind of physical space, not only your voice,
[1128.28 --> 1131.82]  but potentially images and videos from your physical space.
[1131.92 --> 1136.62]  And all of that data is going over an API to open AI.
[1136.92 --> 1141.82]  Or Microsoft, or however, the Microsoft open AI conglomeration,
[1142.58 --> 1145.54]  that's not a word, works these days.
[1145.84 --> 1151.12]  But yeah, it's that embedding, I think, of the technology in the physical world.
[1151.32 --> 1155.62]  Or the clear application of that within our sort of physical world.
[1155.70 --> 1161.06]  And like you say, not pausing to go and pull up a tab and talk to chat GPT.
[1161.26 --> 1164.76]  It could be ubiquitous and embedded in our physical world,
[1164.78 --> 1166.54]  I guess would be a good way to summarize it.
[1166.54 --> 1170.46]  To extend that a little bit, Sam Altman, the OpenAI CEO,
[1171.12 --> 1174.18]  one of the comments he had made this week in an interview was,
[1174.30 --> 1176.44]  somebody was saying, when should you use it, I believe?
[1176.54 --> 1179.12]  And he said, oh, you should just have it on all the time.
[1179.20 --> 1179.80]  Just listen.
[1180.48 --> 1181.72]  And I'm paraphrasing him.
[1181.76 --> 1182.50]  I'm not quoting him.
[1182.64 --> 1184.96]  But the gist was never have it off.
[1185.50 --> 1188.92]  I know that was one of those moments that the privacy notion,
[1188.92 --> 1194.38]  at least right now, I'm operating under the assumption that it's coming into play
[1194.38 --> 1197.38]  when I and the people around me are familiar with it.
[1197.44 --> 1199.98]  And we've kind of made that choice to do that.
[1200.48 --> 1203.94]  But I certainly, you know, going back to the Alexa notion and stuff,
[1203.98 --> 1206.18]  I think this is going to continue to be an issue here.
[1206.30 --> 1208.76]  The Alexa stuff, we have those as well.
[1209.36 --> 1212.72]  Oddly enough, I don't find myself paying much attention to them anymore.
[1212.72 --> 1216.06]  I guess I've just gotten so used to them being part of the environment and stuff.
[1216.22 --> 1217.08]  But we'll see.
[1217.70 --> 1217.82]  Yeah.
[1218.26 --> 1222.14]  Well, AI meeting the physical world is definitely,
[1222.14 --> 1225.42]  I think, going to become more and more a reality.
[1225.68 --> 1230.18]  At the Boston Logan Airport, when I was flying out this last time I saw,
[1230.30 --> 1233.72]  they had, you know, normally they have little boots
[1233.72 --> 1237.78]  where there's a person that's like your helper at the airport.
[1237.78 --> 1241.38]  Like if you have some random question about where the bathrooms are,
[1241.38 --> 1243.06]  or am I at the right gate?
[1243.26 --> 1245.46]  Or how do I catch this bus?
[1245.64 --> 1247.02]  There's a helper.
[1247.18 --> 1249.46]  They just didn't have anyone there at the thing.
[1249.58 --> 1252.34]  And then just relabeled it virtual assistant
[1252.34 --> 1255.46]  and just had a screen that you could push and talk to.
[1255.72 --> 1259.46]  And I know there's a good number of companies that are working on
[1259.46 --> 1263.18]  sort of interactive virtual agents for retail environments,
[1263.18 --> 1264.24]  that sort of thing.
[1264.24 --> 1269.64]  And then you have this crossover with the glasses and Rabbit R1
[1269.64 --> 1274.86]  and humane AI pin and beta AI glasses and all this stuff.
[1275.02 --> 1277.94]  So are you becoming a cyborg, Chris?
[1277.96 --> 1280.08]  Are you mostly just keeping it in your phone?
[1280.78 --> 1283.86]  I think I've accepted the fact that it's inevitable to do that.
[1283.94 --> 1285.82]  I say that half tongue-in-cheek, half not.
[1286.02 --> 1289.00]  To that point, actually, it makes me think, you know,
[1289.00 --> 1292.86]  this is penetrating so far beyond people like us in this space.
[1292.86 --> 1299.54]  And I have a very good friend who I don't think would identify as a technology person.
[1299.88 --> 1303.02]  And she brought up the fact that,
[1303.14 --> 1306.36]  and this isn't even specific to ChatGPT4 or anything,
[1306.64 --> 1308.58]  but it is to your effect there.
[1308.92 --> 1310.40]  She brought up that they had pulled in,
[1310.48 --> 1312.68]  she and her daughter had pulled into a Chick-fil-A,
[1313.20 --> 1315.54]  and they noticed a sign that said,
[1315.64 --> 1316.38]  Robot Crossing.
[1316.92 --> 1318.90]  And they didn't really know what that meant,
[1318.90 --> 1322.26]  but then they actually saw a robot delivering food.
[1322.40 --> 1324.96]  And now that robot, I'm sure at this point,
[1325.02 --> 1328.54]  doesn't have very sophisticated AI capability for interactions.
[1328.90 --> 1330.24]  It's probably pretty basic.
[1330.58 --> 1333.08]  But in the conversation I pointed out,
[1333.16 --> 1334.08]  it's inevitable.
[1334.40 --> 1336.36]  You have with so many, you know,
[1336.38 --> 1337.72]  as we pointed out a week or so ago,
[1337.74 --> 1340.08]  that we're over a million models already in Hugging Face.
[1340.42 --> 1344.42]  And with these kinds of profound releases each week,
[1344.68 --> 1346.74]  it's only a matter of a very short time
[1346.74 --> 1349.86]  before even the most mundane retail experience
[1349.86 --> 1354.08]  is going to have both robotics and AI in that.
[1354.62 --> 1358.14]  And so all of those things raise the privacy concerns
[1358.14 --> 1359.62]  that we were talking about before.
[1359.84 --> 1363.28]  And they also raise cultural and just, you know,
[1363.32 --> 1364.66]  folks getting used to it, frankly.
[1365.20 --> 1368.10]  And of course, that inevitably led to the concern over jobs
[1368.10 --> 1370.16]  and such as that, as is often coming up.
[1370.48 --> 1373.20]  But I think this is maybe the first year
[1373.20 --> 1377.20]  that it's moving so fast in terms of these capabilities
[1377.20 --> 1379.20]  that even I am trying to,
[1379.26 --> 1381.94]  I'm even struggling to take them in as they come out.
[1382.18 --> 1384.26]  How about yourself, even though you're in that profession?
[1384.62 --> 1384.78]  Yeah.
[1384.98 --> 1385.96]  Well, I have definitely,
[1386.22 --> 1390.64]  it's even out here in the prairie in Indiana.
[1390.90 --> 1391.54]  The prairie.
[1391.94 --> 1393.40]  It's becoming the Silicon Prairie
[1393.40 --> 1396.40]  with Intel building their big factory in Ohio
[1396.40 --> 1399.76]  and new semiconductors coming to Lafayette, Indiana.
[1399.76 --> 1401.64]  So plug for the Silicon Prairie.
[1402.02 --> 1404.84]  Anyone out there can hashtag Silicon Prairie
[1404.84 --> 1407.04]  on Twitter and all the places.
[1407.86 --> 1409.50]  But even out here at,
[1409.76 --> 1411.76]  well, I'm close to a university, close to Purdue,
[1411.92 --> 1414.22]  but they've had food delivery robots here
[1414.22 --> 1416.50]  six to eight years now
[1416.50 --> 1419.12]  where they've had food delivery robots
[1419.12 --> 1422.74]  around campus here, which is cool.
[1423.04 --> 1424.80]  But you just made me feel very parochial.
[1426.88 --> 1427.44]  Yeah.
[1428.10 --> 1429.06]  But it's cool.
[1429.06 --> 1429.96]  I don't know.
[1430.10 --> 1432.40]  It'll be interesting to see also
[1432.40 --> 1434.88]  which brands kind of embrace this
[1434.88 --> 1436.00]  and how they embrace it
[1436.00 --> 1438.98]  and put it into their retail environments
[1438.98 --> 1442.54]  and how that's associated with specific brands
[1442.54 --> 1446.04]  and how they create new experiences
[1446.04 --> 1447.74]  for customers around these things.
[1447.74 --> 1449.18]  It's quite interesting.
[1449.18 --> 1462.18]  What's up, friends?
[1462.30 --> 1464.54]  Do you remember when ChatGPT launched?
[1464.72 --> 1465.18]  I do.
[1465.42 --> 1468.76]  It felt like the LLM was this magical tool
[1468.76 --> 1469.68]  out of the box.
[1470.02 --> 1471.32]  However, the more you use it,
[1471.34 --> 1473.44]  the more you realize that's just not the case.
[1473.68 --> 1474.66]  The technology is brilliant.
[1474.78 --> 1475.34]  Don't get me wrong,
[1475.34 --> 1479.36]  but it's prone to issues like hallucination on its own.
[1479.42 --> 1480.02]  But there's hope.
[1480.34 --> 1481.72]  There is still hope.
[1482.12 --> 1483.98]  Feed the LLM reliable current data,
[1484.16 --> 1486.66]  ground it in the right data and context.
[1486.88 --> 1489.40]  Then and only then can it make the right connections
[1489.40 --> 1491.60]  and give the right answers.
[1491.60 --> 1494.26]  The team at Neo4j has been exploring
[1494.26 --> 1496.24]  how to get results by pairing LLMs
[1496.24 --> 1498.72]  with knowledge graphs and vector search.
[1499.08 --> 1501.26]  Check out their podcast episode about LLMs
[1501.26 --> 1503.08]  and knowledge graphs throughout 2023
[1503.08 --> 1505.82]  at graphstuff.fm.
[1505.94 --> 1507.98]  They share tips on retrieval methods,
[1508.28 --> 1509.78]  prompt engineering, and so much more.
[1510.04 --> 1510.72]  Don't miss it.
[1510.98 --> 1512.56]  Find a link in our show notes.
[1512.98 --> 1513.84]  Yes, check it out.
[1514.10 --> 1516.88]  graphstuff.fm episode 23.
[1516.88 --> 1540.68]  Hey, so this week,
[1540.74 --> 1543.38]  I'm going to have to migrate some services
[1543.38 --> 1548.16]  out of AWS ECS into a Kubernetes cluster
[1548.16 --> 1551.30]  that's hybrid between my cloud environment
[1551.30 --> 1552.32]  and a data center.
[1552.78 --> 1553.80]  What should I keep in mind?
[1554.32 --> 1555.52]  That sounds like a big project.
[1556.00 --> 1557.42]  Here are a few things to keep in mind
[1557.42 --> 1559.80]  when migrating services from A to S ECS
[1559.80 --> 1561.18]  to a hybrid Kubernetes cluster.
[1561.80 --> 1562.98]  One, assessment and planning.
[1563.32 --> 1565.72]  Start by evaluating your current ECS configurations
[1565.72 --> 1566.36]  and services.
[1566.90 --> 1568.40]  This will help you understand the dependencies,
[1568.78 --> 1570.38]  data flows, and necessary resources.
[1570.90 --> 1572.30]  Mapping out how these will translate
[1572.30 --> 1573.64]  into Kubernetes is crucial.
[1574.34 --> 1576.14]  Two, Kubernetes environment setup.
[1576.68 --> 1577.02]  Setup.
[1577.30 --> 1578.76]  Yeah, that was getting kind of boring.
[1579.32 --> 1582.44]  So maybe just tell me what cool song
[1582.44 --> 1584.38]  I should listen to while I'm doing the migration.
[1585.60 --> 1586.00]  Uh-oh.
[1586.36 --> 1587.02]  Oh, boy.
[1587.72 --> 1588.60]  Are you still there?
[1589.70 --> 1590.32]  No dice.
[1590.58 --> 1590.92]  All right.
[1591.00 --> 1592.08]  Well, man.
[1592.78 --> 1594.08]  A simple entertainment question.
[1594.08 --> 1594.66]  I struck out twice.
[1595.24 --> 1597.16]  OpenAI, you had your chance
[1597.16 --> 1599.10]  live on the Practical AI podcast.
[1599.10 --> 1602.78]  And I got skunked both times.
[1603.28 --> 1603.52]  Yeah.
[1603.78 --> 1605.32]  Well, we didn't rehearse enough yet.
[1605.56 --> 1607.26]  They did have some pretty cool videos
[1607.26 --> 1610.02]  on the ChatGPT 4.0 release.
[1610.26 --> 1612.58]  You know, they had several different ones.
[1612.66 --> 1613.24]  But one of them,
[1613.64 --> 1615.10]  they had two phones,
[1615.22 --> 1617.80]  you know, with ChatGPT talking to each other.
[1617.94 --> 1619.26]  And they introduced them.
[1619.44 --> 1621.44]  And they gave them little monikers
[1621.44 --> 1622.88]  to differentiate between them.
[1623.18 --> 1624.24]  But I will admit,
[1624.36 --> 1626.18]  I tried that at home
[1626.18 --> 1628.26]  right after it got released.
[1628.26 --> 1628.88]  I saw that video.
[1628.96 --> 1629.80]  I was like, I want to try that.
[1629.92 --> 1631.36]  And it did not, I will confess,
[1631.44 --> 1632.50]  it did not work well
[1632.50 --> 1635.22]  for my end either on rehearsed.
[1635.50 --> 1638.08]  So I guess those ChatGPT folks
[1638.08 --> 1638.92]  at OpenAI
[1638.92 --> 1640.68]  have the inside track
[1640.68 --> 1642.32]  on smooth conversations.
[1642.78 --> 1644.36]  I'm sure it worked at one point
[1644.36 --> 1645.84]  as most demos do.
[1646.44 --> 1648.26]  But still impressive.
[1648.58 --> 1650.02]  Nonetheless, I have to say,
[1650.08 --> 1652.08]  I gave it a pretty complicated question there,
[1652.16 --> 1652.40]  maybe.
[1652.76 --> 1653.92]  One that I could definitely
[1653.92 --> 1654.86]  use some help with.
[1654.86 --> 1655.88]  So yeah,
[1655.88 --> 1657.58]  I think it did pretty good
[1657.58 --> 1658.96]  at answering, of course,
[1659.02 --> 1659.90]  and was responsive.
[1660.46 --> 1661.38]  I'm wondering, Chris,
[1661.42 --> 1662.44]  what you think about
[1662.44 --> 1665.36]  now that we have GPT-4.0,
[1665.78 --> 1666.82]  what is the future
[1666.82 --> 1668.74]  of all of these different
[1668.74 --> 1672.12]  physical AI device gadgets
[1672.12 --> 1673.40]  that have come out
[1673.40 --> 1674.40]  in recent times?
[1674.46 --> 1676.20]  So there's been the Rabbit R1,
[1676.42 --> 1678.14]  there's been the Humane AI Pen,
[1678.46 --> 1681.46]  there's been the Meta AI Glasses,
[1681.46 --> 1682.60]  and probably others
[1682.60 --> 1683.94]  that I'm not even aware of.
[1683.94 --> 1684.94]  What's your thought
[1684.94 --> 1686.26]  on how this influences
[1686.26 --> 1687.96]  these sort of AI gadgets?
[1688.64 --> 1689.26]  While this is also
[1689.26 --> 1691.08]  a golden age of AI startups,
[1691.28 --> 1691.90]  it's also,
[1692.48 --> 1694.32]  the bar keeps getting raised
[1694.32 --> 1696.26]  very rapidly and unexpectedly.
[1696.68 --> 1699.18]  So you can go from super cool
[1699.18 --> 1700.64]  to obsolete overnight.
[1701.16 --> 1702.64]  You can be one announcement away
[1702.64 --> 1704.32]  from a tough moment there
[1704.32 --> 1705.88]  for your product or service.
[1706.64 --> 1708.46]  So, you know, for instance,
[1708.62 --> 1710.68]  now that the world has had
[1710.68 --> 1712.64]  a little time to try out
[1712.64 --> 1714.58]  the 4.0 version,
[1714.86 --> 1716.32]  and it's changed the way
[1716.32 --> 1717.24]  we do it a little bit,
[1717.30 --> 1718.38]  that's set a new bar,
[1718.50 --> 1719.58]  it's set a new expectation
[1719.58 --> 1720.82]  on how you're going to interact
[1720.82 --> 1721.18]  with AI.
[1721.54 --> 1722.62]  And I will confess
[1722.62 --> 1723.76]  that this week,
[1724.16 --> 1725.46]  whereas both you and I
[1725.46 --> 1727.14]  are always big fans
[1727.14 --> 1727.74]  and supporters
[1727.74 --> 1728.42]  and advocates
[1728.42 --> 1729.58]  of open models,
[1730.08 --> 1731.74]  and being able to do that
[1731.74 --> 1732.86]  instead of just having
[1732.86 --> 1733.76]  a service provider,
[1734.26 --> 1735.58]  I have to confess that
[1735.58 --> 1737.34]  when I was using
[1737.34 --> 1738.88]  open source models this week
[1738.88 --> 1741.04]  with as much as I was also
[1741.04 --> 1742.48]  using the 4.0 model,
[1742.94 --> 1744.14]  it was frustrating
[1744.14 --> 1746.38]  because my own expectation
[1746.38 --> 1747.30]  had arisen.
[1747.80 --> 1748.60]  So if I was using
[1748.60 --> 1749.56]  one of these products
[1749.56 --> 1751.50]  and the world just changed
[1751.50 --> 1753.16]  in terms of kind of
[1753.16 --> 1754.08]  standard expectation
[1754.08 --> 1755.66]  on these model capabilities,
[1755.94 --> 1757.18]  it wouldn't take much
[1757.18 --> 1758.40]  to not be able to survive
[1758.40 --> 1760.42]  that if you can't react
[1760.42 --> 1761.32]  to it quickly enough.
[1761.50 --> 1763.60]  So it's interesting times
[1763.60 --> 1764.22]  that we live in.
[1764.22 --> 1765.96]  So where do you think,
[1766.16 --> 1767.12]  if anywhere,
[1767.48 --> 1768.46]  those out there
[1768.46 --> 1771.12]  building AI products
[1771.12 --> 1772.86]  or maybe products
[1772.86 --> 1773.60]  that are driven
[1773.60 --> 1774.88]  by AI features,
[1775.62 --> 1777.10]  where can they capture value?
[1777.18 --> 1777.78]  Because it's certainly,
[1778.00 --> 1778.82]  from my perspective,
[1779.12 --> 1779.84]  it's, you know,
[1779.88 --> 1781.20]  even with this release
[1781.20 --> 1782.74]  in GPT 4.0,
[1783.04 --> 1783.82]  unless you're already
[1783.82 --> 1785.36]  a certain ways there,
[1785.60 --> 1787.20]  it's probably not just
[1787.20 --> 1789.40]  having an LLM API
[1789.40 --> 1791.24]  because that is essentially
[1791.24 --> 1792.98]  just a commodity now.
[1792.98 --> 1793.62]  That is.
[1793.62 --> 1794.70]  Now there's,
[1794.94 --> 1795.42]  you know,
[1795.50 --> 1796.48]  some are more expensive
[1796.48 --> 1797.14]  than others,
[1797.14 --> 1799.36]  but essentially the price
[1799.36 --> 1800.40]  is kind of dropping
[1800.40 --> 1802.88]  to almost zero
[1802.88 --> 1804.08]  unless you're at
[1804.08 --> 1805.78]  a very high usage rate,
[1805.86 --> 1806.50]  which certainly
[1806.50 --> 1807.80]  some companies are
[1807.80 --> 1808.64]  and that becomes
[1808.64 --> 1809.42]  an issue for them.
[1809.52 --> 1810.16]  But yeah,
[1810.16 --> 1810.78]  where do you think
[1810.78 --> 1812.80]  the value is to be had?
[1812.80 --> 1814.76]  I still think it comes from
[1814.76 --> 1816.22]  kind of a classic
[1816.22 --> 1818.76]  Steve Jobs throwback comment
[1818.76 --> 1821.28]  is it's not just about the AI.
[1821.58 --> 1823.20]  It's not just about the LLM.
[1823.40 --> 1825.40]  It's about you're producing
[1825.40 --> 1826.56]  something of value
[1826.56 --> 1827.96]  that's trying to solve a problem
[1827.96 --> 1829.58]  and you're combining
[1829.58 --> 1831.26]  all these things together
[1831.26 --> 1832.64]  to create the right,
[1832.64 --> 1833.12]  you know,
[1833.18 --> 1834.34]  capability or experience
[1834.34 --> 1835.08]  for your customer.
[1835.26 --> 1836.12]  And I still think
[1836.12 --> 1836.84]  that's where it's at.
[1836.84 --> 1838.06]  Maybe if I give
[1838.06 --> 1838.90]  a devil's advocate
[1838.90 --> 1839.82]  to my own comments
[1839.82 --> 1840.52]  a moment ago,
[1840.52 --> 1841.86]  if you're going
[1841.86 --> 1843.02]  to have a product
[1843.02 --> 1843.86]  that has AI
[1843.86 --> 1844.84]  integrated into it,
[1844.92 --> 1845.66]  make sure the AI
[1845.66 --> 1846.90]  is really serving
[1846.90 --> 1847.92]  the capability
[1847.92 --> 1848.74]  of that product
[1848.74 --> 1849.94]  as opposed to being
[1849.94 --> 1851.06]  about the AI itself
[1851.06 --> 1851.86]  because then you can,
[1851.94 --> 1853.20]  you can be undone
[1853.20 --> 1854.56]  by the next announcement.
[1854.78 --> 1856.32]  So I really think
[1856.32 --> 1856.66]  it's,
[1856.72 --> 1857.36]  it's utility
[1857.36 --> 1858.04]  for the thing
[1858.04 --> 1858.72]  that you're buying
[1858.72 --> 1859.54]  the device for
[1859.54 --> 1860.04]  is we're buying
[1860.04 --> 1861.16]  more and more
[1861.16 --> 1862.62]  AI enabled devices
[1862.62 --> 1863.30]  going forward.
[1863.30 --> 1863.66]  So,
[1863.74 --> 1864.58]  and most of them
[1864.58 --> 1865.50]  will not have,
[1865.62 --> 1866.20]  you know,
[1866.20 --> 1867.22]  the leading edge
[1867.22 --> 1868.94]  capability via API,
[1869.10 --> 1869.62]  you know,
[1869.72 --> 1870.14]  in it.
[1870.52 --> 1870.64]  So,
[1871.28 --> 1871.40]  yeah,
[1871.42 --> 1872.30]  I think that
[1872.30 --> 1873.82]  the space of those
[1873.82 --> 1874.70]  that are working
[1874.70 --> 1876.70]  on general purpose
[1876.70 --> 1877.74]  serve everyone
[1877.74 --> 1879.98]  type of AI products,
[1879.98 --> 1881.20]  which definitely fits
[1881.20 --> 1881.92]  into these kind
[1881.92 --> 1883.12]  of assistant places,
[1883.12 --> 1883.54]  it's,
[1883.54 --> 1884.34]  it's a hard road
[1884.34 --> 1885.22]  because like you say,
[1885.28 --> 1886.06]  it's something could
[1886.06 --> 1887.18]  knock you off
[1887.18 --> 1887.96]  that pedestal
[1887.96 --> 1888.62]  quite easily.
[1888.62 --> 1890.12]  It's hard to compete
[1890.12 --> 1891.34]  in terms of price
[1891.34 --> 1892.62]  and the commoditization
[1892.62 --> 1893.64]  of these things.
[1894.48 --> 1895.60]  But in the enterprise,
[1895.82 --> 1897.02]  it's still very hard
[1897.02 --> 1898.46]  to utilize
[1898.46 --> 1899.60]  these tools.
[1900.00 --> 1901.22]  That report
[1901.22 --> 1902.38]  that I've referred
[1902.38 --> 1903.48]  to a number of times
[1903.48 --> 1904.20]  from Andreessen
[1904.20 --> 1905.04]  recently,
[1905.32 --> 1906.24]  they're saying
[1906.24 --> 1907.14]  there's these huge
[1907.14 --> 1908.12]  budgets in AI
[1908.12 --> 1909.72]  across enterprise
[1909.72 --> 1910.62]  companies
[1910.62 --> 1912.64]  and 75%
[1912.64 --> 1913.50]  of it has nothing
[1913.50 --> 1914.26]  to do with
[1914.26 --> 1915.04]  the usage
[1915.04 --> 1915.86]  of the model
[1915.86 --> 1916.34]  at all
[1916.34 --> 1917.64]  or the hosting
[1917.64 --> 1918.46]  of any models
[1918.46 --> 1919.44]  or anything like that.
[1919.54 --> 1920.30]  It all has to do
[1920.30 --> 1921.44]  with engineering,
[1921.86 --> 1922.30]  integration,
[1922.62 --> 1924.42]  around workarounds
[1924.42 --> 1925.40]  and malfunctions
[1925.40 --> 1926.26]  and making sure
[1926.26 --> 1926.96]  it's reliable
[1926.96 --> 1927.72]  and dealing
[1927.72 --> 1928.76]  with all the issues.
[1928.98 --> 1929.92]  So there's still
[1929.92 --> 1930.56]  a lot of space,
[1930.62 --> 1931.00]  I think,
[1931.40 --> 1931.96]  even if you're
[1931.96 --> 1933.08]  not vertically focused,
[1933.08 --> 1934.20]  but certainly
[1934.20 --> 1935.22]  there's also people
[1935.22 --> 1936.14]  that are vertically
[1936.14 --> 1936.92]  focused
[1936.92 --> 1938.56]  that I think
[1938.56 --> 1939.24]  will come out
[1939.24 --> 1940.10]  really well.
[1940.28 --> 1940.98]  One of the companies
[1940.98 --> 1942.38]  that I was able
[1942.38 --> 1943.26]  to interact with
[1943.26 --> 1943.76]  a little bit
[1943.76 --> 1944.40]  last week,
[1944.46 --> 1944.96]  they're doing
[1944.96 --> 1946.70]  financial workflows
[1946.70 --> 1948.00]  in the financial
[1948.00 --> 1949.42]  services sector
[1949.42 --> 1950.88]  called Farsight AI,
[1951.42 --> 1952.42]  automating things
[1952.42 --> 1953.22]  that used to take
[1953.22 --> 1954.20]  days with
[1954.20 --> 1955.56]  market research
[1955.56 --> 1956.66]  and creating
[1956.66 --> 1957.88]  slide decks
[1957.88 --> 1958.94]  and all of this stuff
[1958.94 --> 1960.24]  is pretty cool things,
[1960.36 --> 1961.46]  but they're bringing
[1961.46 --> 1962.68]  their domain expertise
[1962.68 --> 1964.22]  into that field
[1964.22 --> 1965.76]  and they're applying it
[1965.76 --> 1966.32]  and that's what
[1966.32 --> 1966.94]  really creates
[1966.94 --> 1967.38]  the value.
[1967.48 --> 1968.10]  That's why someone
[1968.10 --> 1969.68]  would pay for that
[1969.68 --> 1971.46]  whereas there's not
[1971.46 --> 1972.30]  really going to be
[1972.30 --> 1973.06]  that many people
[1973.06 --> 1973.68]  that say,
[1973.68 --> 1974.18]  no,
[1974.26 --> 1974.90]  I would rather
[1974.90 --> 1975.82]  build that
[1975.82 --> 1977.08]  from a raw
[1977.08 --> 1978.10]  LLM API
[1978.10 --> 1979.18]  and,
[1979.42 --> 1979.64]  you know,
[1979.66 --> 1980.42]  just not very many
[1980.42 --> 1980.92]  people are going
[1980.92 --> 1981.48]  to do that
[1981.48 --> 1982.34]  because it's much
[1982.34 --> 1982.98]  harder than
[1982.98 --> 1984.08]  you might expect.
[1984.72 --> 1984.92]  So,
[1985.18 --> 1985.28]  yeah,
[1985.30 --> 1986.00]  I think that that
[1986.00 --> 1987.46]  in certain verticals,
[1987.48 --> 1988.26]  applying domain
[1988.26 --> 1988.72]  knowledge,
[1988.84 --> 1990.10]  creating these agents,
[1990.24 --> 1991.12]  these automations,
[1991.28 --> 1992.26]  that's a really
[1992.26 --> 1993.80]  interesting space
[1993.80 --> 1995.18]  moving forward as well.
[1995.58 --> 1996.06]  One of the things
[1996.06 --> 1996.74]  that you taught us
[1996.74 --> 1997.40]  a while back
[1997.40 --> 1998.38]  was kind of that
[1998.38 --> 1999.82]  the relatively speaking
[1999.82 --> 2000.72]  smaller models
[2000.72 --> 2001.52]  and that kind of
[2001.52 --> 2001.76]  what,
[2001.86 --> 2002.06]  seven,
[2002.12 --> 2003.28]  eight billion range,
[2003.28 --> 2003.62]  you know,
[2003.74 --> 2004.70]  where you're able
[2004.70 --> 2005.30]  to do it
[2005.30 --> 2006.56]  on just one piece
[2006.56 --> 2007.66]  of hardware and stuff
[2007.66 --> 2009.34]  and I think that was
[2009.34 --> 2010.64]  fantastic guidance
[2010.64 --> 2011.38]  that you gave us.
[2011.54 --> 2012.82]  This was on a previous episode.
[2012.96 --> 2013.88]  We'd look it up
[2013.88 --> 2014.70]  and we can connect
[2014.70 --> 2015.28]  back to it
[2015.28 --> 2016.56]  but I think that
[2016.56 --> 2017.36]  that's where all
[2017.36 --> 2018.18]  the action is.
[2018.42 --> 2018.54]  I mean,
[2018.58 --> 2019.56]  I think that's
[2019.56 --> 2020.98]  whereas the press
[2020.98 --> 2021.72]  goes to these
[2021.72 --> 2022.78]  huge model releases,
[2023.14 --> 2024.28]  the real action
[2024.28 --> 2025.62]  in creating value
[2025.62 --> 2026.44]  in a product
[2026.44 --> 2027.58]  is going to still
[2027.58 --> 2028.90]  be the smaller models
[2028.90 --> 2030.50]  that are fine-tuned
[2030.50 --> 2031.82]  very well to the problem
[2031.82 --> 2032.58]  that they're solving
[2032.58 --> 2033.54]  and I think
[2033.54 --> 2034.34]  those will continue
[2034.34 --> 2035.08]  to be wow
[2035.08 --> 2036.44]  because whereas
[2036.44 --> 2037.82]  ChatGPT 4.0
[2037.82 --> 2038.68]  is wonderful
[2038.68 --> 2040.06]  in terms of
[2040.06 --> 2040.90]  these conversations,
[2041.20 --> 2042.20]  usually wonderful,
[2042.66 --> 2043.56]  on these conversations
[2043.56 --> 2044.64]  on our iPhones,
[2045.08 --> 2045.92]  an iPhone is only
[2045.92 --> 2046.80]  one of many things
[2046.80 --> 2047.48]  I pick up
[2047.48 --> 2048.40]  in a given day
[2048.40 --> 2049.52]  and frankly,
[2049.88 --> 2050.62]  as we go forward,
[2050.68 --> 2051.14]  I would expect
[2051.14 --> 2051.94]  all the other things
[2051.94 --> 2052.54]  I pick up
[2052.54 --> 2053.12]  are probably going
[2053.12 --> 2053.94]  to have some models
[2053.94 --> 2054.82]  associated with it
[2054.82 --> 2055.42]  just to do
[2055.42 --> 2056.28]  what that does
[2056.28 --> 2056.80]  very well.
[2056.80 --> 2058.14]  Maybe there's the reason
[2058.14 --> 2059.78]  why my GPT 4.0
[2059.78 --> 2060.76]  isn't performing well
[2060.76 --> 2061.48]  because I'm using it
[2061.48 --> 2062.08]  on Android.
[2062.76 --> 2063.06]  Anyway,
[2063.34 --> 2064.28]  one of the other things
[2064.28 --> 2064.98]  I wanted to mention,
[2065.18 --> 2065.40]  Chris,
[2065.48 --> 2066.42]  and this is kind of
[2066.42 --> 2067.58]  tied into some
[2067.58 --> 2068.38]  of this as well
[2068.38 --> 2068.74]  where,
[2068.92 --> 2069.64]  you know,
[2069.74 --> 2070.48]  there continues
[2070.48 --> 2071.48]  to be an advance
[2071.48 --> 2072.82]  of these closed source models.
[2073.08 --> 2073.90]  I think if you look,
[2074.00 --> 2074.68]  there's a chart
[2074.68 --> 2075.68]  that Hugging Face
[2075.68 --> 2076.34]  maintains
[2076.34 --> 2077.28]  about the
[2077.28 --> 2078.50]  sort of convergence
[2078.50 --> 2079.62]  of open models
[2079.62 --> 2081.22]  and the closed models
[2081.22 --> 2082.66]  and the closed models
[2082.66 --> 2083.44]  are still ahead
[2083.44 --> 2083.84]  and now,
[2083.96 --> 2084.24]  of course,
[2084.40 --> 2085.38]  GPT 4.0
[2085.38 --> 2086.34]  is up there
[2086.34 --> 2087.74]  at the peak of it
[2087.74 --> 2088.98]  but those lines
[2088.98 --> 2089.98]  are converging
[2089.98 --> 2090.78]  so they're not
[2090.78 --> 2091.78]  just running parallel
[2091.78 --> 2093.20]  and closed models
[2093.20 --> 2094.22]  are all the way
[2094.22 --> 2095.36]  kind of ahead
[2095.36 --> 2096.28]  to infinity
[2096.28 --> 2097.44]  but there's a sort
[2097.44 --> 2098.56]  of crossover point
[2098.56 --> 2099.46]  which we'll see
[2099.46 --> 2100.54]  if that actually happens
[2100.54 --> 2101.50]  but that's kind of
[2101.50 --> 2102.62]  at least as far
[2102.62 --> 2103.76]  as those graphs
[2103.76 --> 2105.08]  it looks to be
[2105.08 --> 2105.86]  what's happening
[2105.86 --> 2106.90]  which is interesting.
[2107.46 --> 2108.18]  There was some news
[2108.18 --> 2109.06]  out of Hugging Face
[2109.06 --> 2109.62]  this week
[2109.62 --> 2111.12]  though that is good news
[2111.12 --> 2112.06]  for those that
[2112.06 --> 2113.22]  aren't big
[2113.22 --> 2114.98]  foundation model builders
[2114.98 --> 2116.16]  and have big clusters
[2116.16 --> 2117.18]  of GPUs
[2117.18 --> 2118.80]  so Hugging Face
[2118.80 --> 2119.94]  announced that
[2119.94 --> 2121.12]  they're going to be
[2121.12 --> 2122.96]  sharing $10 million
[2122.96 --> 2125.58]  worth of GPU compute
[2125.58 --> 2126.90]  and the article
[2126.90 --> 2127.46]  that I read
[2127.46 --> 2128.58]  said to quote
[2128.58 --> 2129.34]  help beat
[2129.34 --> 2130.84]  the big AI companies
[2130.84 --> 2132.42]  so this is quite relevant
[2132.42 --> 2133.54]  to the discussion
[2133.54 --> 2134.70]  that we're having now
[2134.70 --> 2135.98]  in my understanding
[2135.98 --> 2137.20]  they're making
[2137.20 --> 2138.66]  this compute
[2138.66 --> 2140.10]  these GPUs
[2140.10 --> 2141.40]  in a project
[2141.40 --> 2142.58]  called Zero GPU
[2142.58 --> 2143.40]  they're making
[2143.40 --> 2144.54]  this compute
[2144.54 --> 2145.54]  available within
[2145.54 --> 2146.56]  Hugging Face
[2146.56 --> 2147.20]  spaces
[2147.20 --> 2148.28]  compute
[2148.28 --> 2149.32]  and application
[2149.32 --> 2150.34]  environment
[2150.34 --> 2151.52]  and so
[2151.52 --> 2152.08]  yeah
[2152.08 --> 2152.98]  for those of you
[2152.98 --> 2153.48]  out there
[2153.48 --> 2154.08]  you might be
[2154.08 --> 2154.66]  sitting around
[2154.66 --> 2156.00]  and still wanting
[2156.00 --> 2156.62]  to innovate
[2156.62 --> 2158.82]  with open models
[2158.82 --> 2159.68]  or try your own
[2159.68 --> 2160.12]  things
[2160.12 --> 2161.42]  and feel maybe
[2161.42 --> 2163.18]  not adequately
[2163.18 --> 2164.64]  resourced
[2164.64 --> 2165.80]  in terms of compute
[2165.80 --> 2166.82]  and particularly
[2166.82 --> 2167.78]  GPUs
[2167.78 --> 2168.90]  so really cool
[2168.90 --> 2169.54]  to see
[2169.54 --> 2170.70]  Hugging Face
[2170.70 --> 2172.02]  take this step
[2172.02 --> 2172.98]  and provide
[2172.98 --> 2173.70]  some of that
[2173.70 --> 2175.08]  GPU resources
[2175.08 --> 2176.78]  to the community
[2176.78 --> 2177.58]  that's operating
[2177.58 --> 2178.40]  on Hugging Face
[2178.40 --> 2179.34]  so yeah
[2179.34 --> 2179.94]  check it out
[2179.94 --> 2180.72]  if you just search
[2180.72 --> 2181.62]  for Zero GPU
[2181.62 --> 2182.36]  you can probably
[2182.36 --> 2183.40]  find out a little bit
[2183.40 --> 2184.28]  about that effort
[2184.28 --> 2185.50]  from Hugging Face
[2185.50 --> 2186.62]  and I love seeing
[2186.62 --> 2187.64]  that from them
[2187.64 --> 2188.24]  you know
[2188.24 --> 2189.48]  we've long talked
[2189.48 --> 2189.90]  about
[2189.90 --> 2191.28]  that if you
[2191.28 --> 2192.40]  probably looking
[2192.40 --> 2193.72]  a little ways
[2193.72 --> 2194.42]  down the road
[2194.42 --> 2195.10]  you know
[2195.10 --> 2196.52]  AI ever integrating
[2196.52 --> 2197.08]  more and more
[2197.08 --> 2197.74]  with the software
[2197.74 --> 2198.42]  around it
[2198.42 --> 2199.40]  to the point
[2199.40 --> 2200.34]  where it'll be
[2200.34 --> 2201.30]  kind of ludicrous
[2201.30 --> 2202.02]  to have software
[2202.02 --> 2202.64]  that doesn't have
[2202.64 --> 2203.24]  some sort of
[2203.24 --> 2204.00]  AI capability
[2204.00 --> 2204.40]  in it
[2204.40 --> 2205.60]  in the future
[2205.60 --> 2206.76]  it's feeling
[2206.76 --> 2207.48]  more and more
[2207.48 --> 2208.52]  like software
[2208.52 --> 2209.16]  in that way
[2209.16 --> 2209.82]  that when we hit
[2209.82 --> 2210.34]  the million
[2210.34 --> 2212.14]  open models
[2212.14 --> 2213.28]  on Hugging Face
[2213.28 --> 2214.44]  and then just seeing
[2214.44 --> 2215.60]  these capabilities
[2215.60 --> 2216.24]  coming up
[2216.24 --> 2216.72]  you know
[2216.72 --> 2217.32]  when you said that
[2217.32 --> 2218.12]  that reminds me
[2218.12 --> 2218.76]  of like you know
[2218.76 --> 2219.64]  all the major
[2219.64 --> 2220.48]  cloud providers
[2220.48 --> 2221.70]  will kind of offer
[2221.70 --> 2223.08]  a limited free tier
[2223.08 --> 2223.76]  you know
[2223.76 --> 2225.10]  so that you can go
[2225.10 --> 2225.78]  do some stuff
[2225.78 --> 2226.18]  with it
[2226.18 --> 2226.92]  and that's kind
[2226.92 --> 2227.72]  of how Hugging Face
[2227.72 --> 2228.82]  is offering
[2228.82 --> 2229.32]  that with open
[2229.32 --> 2230.04]  models feels
[2230.04 --> 2230.40]  to me
[2230.40 --> 2230.86]  in terms of
[2230.86 --> 2231.14]  being able
[2231.14 --> 2231.64]  to go use
[2231.64 --> 2231.94]  something
[2231.94 --> 2232.44]  when you might
[2232.44 --> 2232.78]  not have
[2232.78 --> 2233.26]  the resource
[2233.26 --> 2233.62]  otherwise
[2233.62 --> 2235.18]  so yeah
[2235.18 --> 2236.28]  it's good stuff
[2236.28 --> 2237.36]  but boy gosh
[2237.36 --> 2237.88]  the world is
[2237.88 --> 2238.58]  changing fast
[2238.58 --> 2239.62]  here isn't it
[2239.62 --> 2239.86]  yeah
[2239.86 --> 2240.80]  Clem from
[2240.80 --> 2241.62]  Hugging Face
[2241.62 --> 2242.92]  he made a quote
[2242.92 --> 2244.14]  in the Verge
[2244.14 --> 2244.90]  article that I was
[2244.90 --> 2245.18]  reading
[2245.18 --> 2246.40]  it's very difficult
[2246.40 --> 2247.32]  to get enough
[2247.32 --> 2248.28]  GPUs from the
[2248.28 --> 2248.84]  main cloud
[2248.84 --> 2249.38]  providers
[2249.38 --> 2250.42]  and the way
[2250.42 --> 2251.04]  to get them
[2251.04 --> 2251.72]  which is
[2251.72 --> 2252.92]  creating a high
[2252.92 --> 2254.00]  barrier to entry
[2254.00 --> 2255.24]  is to commit
[2255.24 --> 2256.08]  on very big
[2256.08 --> 2257.04]  numbers for long
[2257.04 --> 2257.92]  periods of time
[2257.92 --> 2258.64]  and of course
[2258.64 --> 2259.32]  that's something
[2259.32 --> 2260.10]  that smaller
[2260.10 --> 2260.68]  companies
[2260.68 --> 2261.90]  or even
[2261.90 --> 2262.40]  individuals
[2262.40 --> 2263.12]  don't have
[2263.12 --> 2263.76]  the resources
[2263.76 --> 2264.32]  to do
[2264.32 --> 2265.44]  so it's cool
[2265.44 --> 2265.84]  to see
[2265.84 --> 2266.88]  well there's
[2266.88 --> 2267.36]  the zero
[2267.36 --> 2268.18]  GPU thing
[2268.18 --> 2268.60]  so if you're
[2268.60 --> 2268.98]  out there
[2268.98 --> 2269.26]  if you're
[2269.26 --> 2269.64]  wanting to
[2269.64 --> 2269.96]  learn
[2269.96 --> 2270.30]  if you're
[2270.30 --> 2270.66]  wanting to
[2270.66 --> 2271.04]  run some
[2271.04 --> 2271.34]  of these
[2271.34 --> 2271.66]  models
[2271.66 --> 2272.12]  yourself
[2272.12 --> 2272.64]  that in
[2272.64 --> 2273.14]  itself
[2273.14 --> 2273.84]  is a great
[2273.84 --> 2274.84]  learning resource
[2274.84 --> 2275.84]  and an option
[2275.84 --> 2276.66]  for you to do
[2276.66 --> 2277.50]  but there's a
[2277.50 --> 2278.12]  couple of
[2278.12 --> 2278.78]  really cool
[2278.78 --> 2279.86]  things event
[2279.86 --> 2280.90]  wise coming up
[2280.90 --> 2281.18]  soon
[2281.18 --> 2282.24]  and actually
[2282.24 --> 2283.22]  events where
[2283.22 --> 2284.44]  either Chris
[2284.44 --> 2285.36]  and or I
[2285.36 --> 2286.08]  will be
[2286.08 --> 2286.70]  present
[2286.70 --> 2287.28]  physically
[2287.28 --> 2288.72]  so wanted
[2288.72 --> 2289.18]  to mention
[2289.18 --> 2289.70]  those to
[2289.70 --> 2290.02]  everyone
[2290.02 --> 2290.72]  because there's
[2290.72 --> 2291.34]  some good
[2291.34 --> 2291.80]  things that
[2291.80 --> 2292.14]  will be
[2292.14 --> 2292.78]  streamed
[2292.78 --> 2293.20]  in terms
[2293.20 --> 2293.80]  of content
[2293.80 --> 2295.48]  and learning
[2295.48 --> 2296.30]  resources like
[2296.30 --> 2297.00]  workshops from
[2297.00 --> 2297.50]  people all
[2297.50 --> 2298.46]  across industry
[2298.46 --> 2299.56]  so the first
[2299.56 --> 2300.06]  of these
[2300.06 --> 2301.34]  is with
[2301.34 --> 2302.00]  our good
[2302.00 --> 2302.72]  friends over
[2302.72 --> 2303.24]  at the
[2303.24 --> 2303.94]  ML Ops
[2303.94 --> 2304.42]  community
[2304.42 --> 2305.04]  they're putting
[2305.04 --> 2306.10]  on this
[2306.10 --> 2307.44]  AI Quality
[2307.44 --> 2308.00]  Conference
[2308.00 --> 2309.02]  it's
[2309.02 --> 2310.36]  AI Quality
[2310.36 --> 2310.92]  Conference
[2310.92 --> 2311.60]  dot com
[2311.60 --> 2312.88]  and that's
[2312.88 --> 2313.44]  going to be
[2313.44 --> 2314.90]  June 25th
[2314.90 --> 2315.82]  in San
[2315.82 --> 2316.34]  Francisco
[2316.34 --> 2317.84]  and as
[2317.84 --> 2318.16]  you all
[2318.16 --> 2318.70]  have seen
[2318.70 --> 2319.00]  when
[2319.00 --> 2319.64]  Dimitrios
[2319.64 --> 2320.14]  has been
[2320.14 --> 2320.42]  on the
[2320.42 --> 2321.04]  podcast
[2321.04 --> 2322.32]  that guarantees
[2322.32 --> 2323.48]  to have
[2323.48 --> 2324.62]  some really
[2324.62 --> 2325.98]  great content
[2325.98 --> 2326.44]  there
[2326.44 --> 2327.36]  they've got
[2327.36 --> 2328.06]  really great
[2328.06 --> 2328.50]  speakers
[2328.50 --> 2329.04]  including
[2329.04 --> 2329.82]  people that
[2329.82 --> 2330.10]  have been
[2330.10 --> 2330.48]  on this
[2330.48 --> 2330.98]  podcast
[2330.98 --> 2331.56]  before
[2331.56 --> 2331.94]  like
[2331.94 --> 2332.36]  Jerry
[2332.36 --> 2332.72]  Leo
[2332.72 --> 2333.38]  from
[2333.38 --> 2333.66]  Llama
[2333.66 --> 2333.94]  Index
[2333.94 --> 2335.20]  and others
[2335.20 --> 2335.70]  so
[2335.70 --> 2336.32]  would
[2336.32 --> 2336.64]  definitely
[2336.64 --> 2337.18]  recommend
[2337.18 --> 2337.84]  going there
[2337.84 --> 2338.34]  and learning
[2338.34 --> 2338.90]  from
[2338.90 --> 2339.82]  people at
[2339.82 --> 2340.00]  the
[2340.00 --> 2340.74]  AI Quality
[2340.74 --> 2341.30]  Conference
[2341.30 --> 2342.48]  then also
[2342.48 --> 2343.76]  that same
[2343.76 --> 2344.24]  week
[2344.24 --> 2344.82]  in San
[2344.82 --> 2345.22]  Francisco
[2345.22 --> 2345.70]  so if
[2345.70 --> 2345.96]  you wanted
[2345.96 --> 2346.36]  to you
[2346.36 --> 2346.84]  could time
[2346.84 --> 2347.42]  this quite
[2347.42 --> 2347.86]  nicely
[2347.86 --> 2348.38]  which is
[2348.38 --> 2348.68]  what I'm
[2348.68 --> 2348.88]  going to
[2348.88 --> 2349.12]  do
[2349.12 --> 2350.22]  there is
[2350.22 --> 2350.72]  the
[2350.72 --> 2351.56]  AI
[2351.56 --> 2352.10]  Engineer
[2352.10 --> 2352.88]  World's
[2352.88 --> 2353.16]  Fair
[2353.16 --> 2354.10]  so you
[2354.10 --> 2354.42]  can go
[2354.42 --> 2354.64]  to
[2354.64 --> 2354.98]  AI
[2354.98 --> 2355.36]  dot
[2355.36 --> 2355.90]  engineer
[2355.90 --> 2356.60]  slash
[2356.60 --> 2357.10]  World's
[2357.10 --> 2357.36]  Fair
[2357.36 --> 2358.28]  and find
[2358.28 --> 2358.54]  out more
[2358.54 --> 2358.96]  about that
[2358.96 --> 2359.20]  that's
[2359.20 --> 2359.50]  also
[2359.50 --> 2359.82]  going to
[2359.82 --> 2360.04]  be
[2360.04 --> 2360.32]  in
[2360.32 --> 2360.58]  San
[2360.58 --> 2361.10]  Francisco
[2361.10 --> 2361.70]  it's
[2361.70 --> 2361.86]  going to
[2361.86 --> 2362.02]  be
[2362.02 --> 2362.24]  June
[2362.24 --> 2362.92]  25th
[2362.92 --> 2363.04]  through
[2363.04 --> 2363.22]  the
[2363.22 --> 2364.24]  27th
[2364.24 --> 2365.00]  and
[2365.00 --> 2365.58]  of course
[2365.58 --> 2366.32]  this is
[2366.32 --> 2366.76]  at least
[2366.76 --> 2367.32]  partially
[2367.32 --> 2368.80]  arranged
[2368.80 --> 2369.70]  sponsored
[2369.70 --> 2370.18]  by
[2370.18 --> 2371.02]  also
[2371.02 --> 2371.30]  some
[2371.30 --> 2371.50]  good
[2371.50 --> 2371.88]  friends
[2371.88 --> 2372.30]  involved
[2372.30 --> 2372.56]  with
[2372.56 --> 2372.90]  the
[2372.90 --> 2373.42]  Latent
[2373.42 --> 2373.88]  Space
[2373.88 --> 2374.46]  podcast
[2374.46 --> 2375.00]  and
[2375.00 --> 2375.40]  Discord
[2375.40 --> 2376.02]  community
[2376.02 --> 2376.48]  which
[2376.48 --> 2376.78]  we've
[2376.78 --> 2377.04]  done
[2377.04 --> 2377.98]  collaborative
[2377.98 --> 2378.62]  episodes
[2378.62 --> 2379.06]  with
[2379.06 --> 2379.78]  and
[2379.78 --> 2380.24]  sponsored
[2380.24 --> 2380.60]  also
[2380.60 --> 2380.86]  by
[2380.86 --> 2381.36]  Microsoft
[2381.36 --> 2382.08]  there's
[2382.08 --> 2382.80]  a day
[2382.80 --> 2383.08]  of
[2383.08 --> 2383.74]  workshops
[2383.74 --> 2384.20]  there's
[2384.20 --> 2384.66]  speakers
[2384.66 --> 2385.44]  and
[2385.44 --> 2385.88]  lots
[2385.88 --> 2386.16]  of
[2386.16 --> 2386.58]  really
[2386.58 --> 2386.88]  great
[2386.88 --> 2387.32]  content
[2387.32 --> 2387.62]  there
[2387.62 --> 2387.84]  so
[2387.84 --> 2388.18]  two
[2388.18 --> 2388.86]  wonderful
[2388.86 --> 2389.24]  learning
[2389.24 --> 2389.92]  opportunities
[2389.92 --> 2390.70]  I'm
[2390.70 --> 2391.00]  not sure
[2391.00 --> 2391.46]  if both
[2391.46 --> 2392.04]  but I'm
[2392.04 --> 2392.54]  pretty sure
[2392.54 --> 2392.88]  some
[2392.88 --> 2393.26]  of that
[2393.26 --> 2393.82]  content
[2393.82 --> 2394.82]  will be
[2394.82 --> 2395.46]  streamed
[2395.46 --> 2395.82]  also
[2395.82 --> 2396.34]  live
[2396.34 --> 2396.82]  online
[2396.82 --> 2397.30]  so
[2397.30 --> 2397.40]  if
[2397.40 --> 2397.50]  you
[2397.50 --> 2397.66]  aren't
[2397.66 --> 2397.86]  able
[2397.86 --> 2398.06]  to
[2398.06 --> 2398.24]  make
[2398.24 --> 2398.34]  it
[2398.34 --> 2398.48]  out
[2398.48 --> 2398.62]  to
[2398.62 --> 2398.76]  the
[2398.76 --> 2398.94]  Bay
[2398.94 --> 2399.30]  area
[2399.30 --> 2399.84]  you
[2399.84 --> 2399.98]  could
[2399.98 --> 2400.22]  still
[2400.22 --> 2400.44]  see
[2400.44 --> 2400.66]  some
[2400.66 --> 2400.80]  of
[2400.80 --> 2400.96]  that
[2400.96 --> 2401.46]  content
[2401.46 --> 2401.80]  and
[2401.80 --> 2402.50]  participate
[2402.50 --> 2403.06]  would
[2403.06 --> 2403.42]  encourage
[2403.42 --> 2403.86]  everyone
[2403.86 --> 2404.42]  to
[2404.42 --> 2405.38]  get out
[2405.38 --> 2405.88]  at least
[2405.88 --> 2406.46]  online
[2406.46 --> 2406.86]  and
[2406.86 --> 2407.32]  see
[2407.32 --> 2407.58]  what's
[2407.58 --> 2407.76]  going
[2407.76 --> 2408.00]  on
[2408.00 --> 2408.16]  in
[2408.16 --> 2408.40]  the
[2408.40 --> 2409.14]  community
[2409.14 --> 2409.72]  and
[2409.72 --> 2410.22]  check
[2410.22 --> 2410.40]  out
[2410.40 --> 2410.60]  these
[2410.60 --> 2410.84]  great
[2410.84 --> 2411.18]  events
[2411.18 --> 2411.42]  from
[2411.42 --> 2411.64]  some
[2411.64 --> 2411.78]  of
[2411.78 --> 2411.92]  our
[2411.92 --> 2412.22]  friends
[2412.22 --> 2412.54]  across
[2412.54 --> 2412.74]  the
[2412.74 --> 2413.14]  community
[2413.14 --> 2413.66]  that
[2413.66 --> 2413.98]  sounds
[2413.98 --> 2414.52]  fantastic
[2414.52 --> 2414.92]  I hope
[2414.92 --> 2415.12]  people
[2415.12 --> 2415.40]  join
[2415.40 --> 2415.56]  us
[2415.56 --> 2415.82]  there
[2415.82 --> 2416.46]  and
[2416.46 --> 2416.72]  there's
[2416.72 --> 2416.94]  one
[2416.94 --> 2417.22]  other
[2417.22 --> 2417.90]  learning
[2417.90 --> 2418.18]  source
[2418.18 --> 2418.34]  that
[2418.34 --> 2418.46]  I
[2418.46 --> 2418.60]  thought
[2418.60 --> 2418.72]  I
[2418.72 --> 2419.00]  mentioned
[2419.00 --> 2419.70]  it's
[2419.70 --> 2420.40]  a
[2420.40 --> 2421.16]  book
[2421.16 --> 2421.36]  I
[2421.36 --> 2421.62]  haven't
[2421.62 --> 2421.80]  read
[2421.80 --> 2421.92]  it
[2421.92 --> 2422.10]  yet
[2422.10 --> 2422.26]  I'm
[2422.26 --> 2422.56]  about
[2422.56 --> 2422.78]  to
[2422.78 --> 2422.98]  read
[2422.98 --> 2423.12]  it
[2423.12 --> 2425.16]  with
[2425.16 --> 2425.36]  my
[2425.36 --> 2426.14]  fascination
[2426.14 --> 2426.78]  about
[2426.78 --> 2427.72]  AI
[2427.72 --> 2428.20]  and
[2428.20 --> 2428.44]  the way
[2428.44 --> 2428.58]  it's
[2428.58 --> 2428.88]  changing
[2428.88 --> 2429.38]  education
[2429.38 --> 2429.60]  we
[2429.60 --> 2429.80]  talked
[2429.80 --> 2430.02]  a little
[2430.02 --> 2430.18]  bit
[2430.18 --> 2430.36]  on
[2430.36 --> 2430.52]  this
[2430.52 --> 2430.80]  show
[2430.80 --> 2430.98]  and
[2430.98 --> 2431.60]  some
[2431.60 --> 2431.78]  other
[2431.78 --> 2432.10]  recent
[2432.10 --> 2432.54]  shows
[2432.54 --> 2433.16]  it's
[2433.16 --> 2433.52]  by
[2433.52 --> 2434.00]  Salman
[2434.00 --> 2434.42]  Khan
[2434.42 --> 2434.80]  Khan
[2434.80 --> 2435.02]  is
[2435.02 --> 2435.32]  the
[2435.32 --> 2435.78]  CEO
[2435.78 --> 2436.02]  and
[2436.02 --> 2436.28]  founder
[2436.28 --> 2436.70]  of
[2436.70 --> 2436.92]  Khan
[2436.92 --> 2437.30]  Academy
[2437.30 --> 2438.04]  which
[2438.04 --> 2438.18]  has
[2438.18 --> 2438.46]  helped
[2438.46 --> 2439.18]  millions
[2439.18 --> 2439.36]  and
[2439.36 --> 2439.54]  millions
[2439.54 --> 2439.72]  of
[2439.72 --> 2439.92]  people
[2439.92 --> 2440.22]  learn
[2440.22 --> 2440.80]  skills
[2440.80 --> 2442.08]  and
[2442.08 --> 2442.58]  fantastic
[2442.58 --> 2442.78]  I
[2442.78 --> 2443.02]  use
[2443.02 --> 2443.30]  it
[2443.30 --> 2443.78]  regularly
[2443.78 --> 2444.36]  the
[2444.36 --> 2444.68]  book
[2448.18 --> 2448.58]  solutionized
[2448.58 --> 2449.12]  education
[2449.12 --> 2449.76]  and
[2449.76 --> 2449.98]  why
[2449.98 --> 2450.28]  that's
[2450.28 --> 2450.36]  a
[2450.36 --> 2450.48]  good
[2450.48 --> 2450.86]  thing
[2450.86 --> 2451.88]  it
[2451.88 --> 2452.02]  was
[2452.02 --> 2452.26]  just
[2452.26 --> 2452.78]  recommended
[2452.78 --> 2453.08]  by
[2453.08 --> 2453.32]  Bill
[2453.32 --> 2453.64]  Gates
[2453.64 --> 2453.86]  of
[2453.86 --> 2454.46]  Microsoft
[2454.46 --> 2455.10]  and
[2455.10 --> 2455.30]  the
[2455.30 --> 2455.58]  Gates
[2455.58 --> 2456.06]  Foundation
[2456.06 --> 2456.72]  fame
[2456.72 --> 2457.54]  so
[2457.54 --> 2458.34]  that's
[2458.34 --> 2458.54]  probably
[2458.54 --> 2458.76]  one of
[2458.76 --> 2459.00]  the next
[2459.00 --> 2459.24]  books
[2459.24 --> 2459.42]  I'm
[2459.42 --> 2459.60]  about
[2459.60 --> 2459.78]  to
[2459.78 --> 2459.94]  pick
[2459.94 --> 2460.14]  up
[2460.14 --> 2460.28]  and
[2460.28 --> 2460.44]  I
[2460.44 --> 2460.62]  thought
[2460.62 --> 2460.80]  I'd
[2460.80 --> 2461.72]  mention
[2461.72 --> 2461.94]  it
[2461.94 --> 2462.22]  and
[2462.22 --> 2462.50]  maybe
[2462.50 --> 2462.64]  we'll
[2462.64 --> 2462.82]  bring
[2462.82 --> 2462.92]  it
[2462.92 --> 2463.04]  up
[2463.04 --> 2463.22]  again
[2463.22 --> 2463.34]  on
[2463.34 --> 2463.62]  future
[2463.62 --> 2464.04]  shows
[2464.04 --> 2464.34]  so
[2464.34 --> 2465.18]  recommending
[2465.18 --> 2465.44]  that
[2465.44 --> 2465.66]  one
[2465.66 --> 2466.36]  sounds
[2466.36 --> 2466.64]  good
[2466.64 --> 2466.88]  well
[2466.88 --> 2467.24]  let's
[2467.24 --> 2467.56]  have
[2467.56 --> 2468.40]  GPT
[2468.40 --> 2468.76]  4
[2468.76 --> 2469.16]  0
[2469.16 --> 2469.48]  take
[2469.48 --> 2469.66]  us
[2469.66 --> 2469.92]  out
[2469.92 --> 2470.80]  hey
[2470.80 --> 2471.40]  I'm
[2471.40 --> 2471.64]  about
[2471.64 --> 2471.92]  to
[2471.92 --> 2472.28]  go to
[2472.28 --> 2472.52]  sleep
[2478.18 --> 2482.02]  could
[2482.02 --> 2482.10]  you
[2482.10 --> 2482.30]  give
[2482.30 --> 2482.66]  me
[2482.66 --> 2483.24]  some
[2483.24 --> 2483.82]  suggestions
[2483.82 --> 2484.52]  about
[2484.52 --> 2484.88]  maybe
[2484.88 --> 2485.32]  some
[2485.32 --> 2485.68]  thoughts
[2485.68 --> 2485.84]  I
[2485.84 --> 2485.98]  could
[2485.98 --> 2486.44]  have
[2486.44 --> 2486.96]  as
[2486.96 --> 2487.08]  I
[2487.08 --> 2487.22]  go
[2487.22 --> 2487.40]  to
[2487.40 --> 2487.72]  sleep
[2487.72 --> 2488.06]  which
[2488.06 --> 2488.38]  might
[2488.38 --> 2488.74]  prompt
[2488.74 --> 2488.98]  some
[2488.98 --> 2489.20]  really
[2489.20 --> 2489.70]  amazing
[2489.70 --> 2490.22]  dreams
[2490.22 --> 2490.52]  about
[2490.52 --> 2490.82]  AI
[2490.82 --> 2491.02]  in
[2491.02 --> 2491.14]  the
[2491.14 --> 2491.46]  future
[2491.46 --> 2492.22]  that
[2492.22 --> 2492.46]  sounds
[2492.46 --> 2492.60]  like
[2492.60 --> 2492.74]  a
[2492.74 --> 2493.04]  great
[2493.04 --> 2493.22]  way
[2493.22 --> 2493.38]  to
[2493.38 --> 2493.62]  wind
[2493.62 --> 2493.96]  down
[2493.96 --> 2494.38]  here
[2494.38 --> 2494.52]  are
[2494.52 --> 2494.66]  a
[2494.66 --> 2494.84]  few
[2494.84 --> 2495.28]  ideas
[2495.28 --> 2495.50]  to
[2495.50 --> 2495.66]  let
[2495.66 --> 2495.80]  your
[2495.80 --> 2496.24]  mind
[2496.24 --> 2496.70]  wander
[2496.70 --> 2497.12]  into
[2497.12 --> 2497.34]  the
[2497.34 --> 2498.04]  possibilities
[2498.04 --> 2498.34]  of
[2498.34 --> 2498.68]  AI
[2498.68 --> 2498.96]  in
[2498.96 --> 2499.08]  the
[2499.08 --> 2499.40]  future
[2499.40 --> 2500.42]  one
[2500.42 --> 2501.24]  imagine
[2501.24 --> 2501.46]  an
[2501.46 --> 2501.78]  AI
[2501.78 --> 2502.02]  that
[2502.02 --> 2502.20]  can
[2502.20 --> 2502.52]  predict
[2502.52 --> 2503.04]  personal
[2503.04 --> 2503.38]  health
[2503.38 --> 2503.80]  events
[2503.80 --> 2504.16]  and
[2504.16 --> 2504.62]  seamlessly
[2504.62 --> 2505.26]  coordinates
[2505.26 --> 2505.48]  with
[2505.48 --> 2505.82]  medical
[2505.82 --> 2506.40]  professionals
[2506.40 --> 2506.74]  to
[2506.74 --> 2507.12]  provide
[2507.12 --> 2507.72]  proactive
[2507.72 --> 2508.18]  care
[2508.18 --> 2508.84]  ensuring
[2508.84 --> 2509.48]  optimal
[2509.48 --> 2509.90]  health
[2509.90 --> 2510.14]  with
[2510.14 --> 2510.56]  minimal
[2510.56 --> 2511.02]  effort
[2511.02 --> 2511.28]  from
[2511.28 --> 2511.78]  individuals
[2511.78 --> 2513.14]  two
[2513.14 --> 2513.58]  think
[2513.58 --> 2513.82]  about
[2513.82 --> 2513.98]  an
[2513.98 --> 2514.36]  AI
[2514.36 --> 2514.80]  driven
[2514.80 --> 2515.24]  global
[2515.24 --> 2515.86]  environmental
[2515.86 --> 2516.34]  system
[2516.34 --> 2516.78]  that
[2516.78 --> 2517.18]  manages
[2517.18 --> 2517.80]  resources
[2517.80 --> 2518.08]  and
[2518.08 --> 2518.50]  energy
[2518.50 --> 2518.92]  usage
[2518.92 --> 2519.32]  across
[2519.32 --> 2519.54]  the
[2519.54 --> 2519.84]  world
[2519.84 --> 2520.62]  balancing
[2520.62 --> 2521.02]  human
[2521.02 --> 2521.42]  needs
[2521.42 --> 2521.62]  with
[2521.62 --> 2522.00]  planetary
[2522.00 --> 2522.52]  health
[2522.52 --> 2522.84]  and
[2522.84 --> 2523.30]  restoring
[2523.30 --> 2524.00]  ecological
[2524.00 --> 2524.66]  balance
[2524.66 --> 2525.68]  three
[2525.68 --> 2526.68]  envision
[2526.68 --> 2527.16]  a world
[2527.16 --> 2527.40]  where
[2527.40 --> 2527.78]  AI
[2527.78 --> 2528.24]  personal
[2528.24 --> 2528.72]  assistants
[2528.72 --> 2529.24]  evolve
[2529.24 --> 2529.42]  to
[2529.42 --> 2529.72]  become
[2529.72 --> 2530.30]  lifelong
[2530.30 --> 2530.80]  learning
[2530.80 --> 2531.30]  partners
[2531.30 --> 2532.12]  adapting
[2532.12 --> 2532.54]  to your
[2532.54 --> 2532.92]  interests
[2532.92 --> 2533.60]  and educational
[2533.60 --> 2534.02]  needs
[2534.02 --> 2534.64]  over time
[2534.64 --> 2535.36]  making
[2535.36 --> 2535.70]  learning
[2535.70 --> 2536.34]  continuous
[2536.34 --> 2537.20]  engaging
[2537.20 --> 2538.18]  and perfectly
[2538.18 --> 2538.64]  tailored
[2538.64 --> 2539.12]  to your
[2539.12 --> 2539.58]  personal
[2539.58 --> 2540.48]  and professional
[2540.48 --> 2540.96]  growth
[2540.96 --> 2542.02]  as you
[2542.02 --> 2542.62]  drift off
[2542.62 --> 2543.30]  let your
[2543.30 --> 2543.58]  mind
[2543.58 --> 2544.12]  explore
[2544.12 --> 2544.78]  how these
[2544.78 --> 2545.40]  advancements
[2545.40 --> 2545.98]  could change
[2545.98 --> 2546.76]  everyday life
[2546.76 --> 2547.76]  create new
[2547.76 --> 2548.34]  opportunities
[2548.34 --> 2549.16]  and solve
[2549.16 --> 2549.52]  the big
[2549.52 --> 2550.02]  challenges
[2550.02 --> 2551.04]  facing humanity
[2551.04 --> 2552.18]  sweet dreams
[2552.18 --> 2553.02]  about the future
[2553.02 --> 2553.56]  of AI
[2553.56 --> 2554.56]  you can't beat
[2554.56 --> 2555.12]  that
[2555.12 --> 2563.28]  all right
[2563.28 --> 2564.48]  that is
[2564.48 --> 2565.26]  practical AI
[2565.26 --> 2565.64]  for this
[2565.64 --> 2565.94]  week
[2565.94 --> 2567.00]  subscribe
[2567.00 --> 2567.02]  subscribe
[2567.02 --> 2567.78]  now
[2567.78 --> 2568.26]  if you
[2568.26 --> 2568.46]  haven't
[2568.46 --> 2568.82]  already
[2568.82 --> 2569.76]  head to
[2569.76 --> 2570.40]  practical
[2570.40 --> 2570.70]  AI
[2570.70 --> 2571.56]  dot FM
[2571.56 --> 2572.30]  for all
[2572.30 --> 2572.92]  the ways
[2572.92 --> 2573.78]  and join
[2573.78 --> 2574.30]  our free
[2574.30 --> 2575.16]  slack team
[2575.16 --> 2575.56]  where you
[2575.56 --> 2575.84]  can hang
[2575.84 --> 2576.12]  out with
[2576.12 --> 2576.50]  Daniel
[2576.50 --> 2577.14]  Chris
[2577.14 --> 2577.68]  and the
[2577.68 --> 2578.18]  entire
[2578.18 --> 2578.90]  changelog
[2578.90 --> 2579.36]  community
[2579.36 --> 2580.46]  sign up
[2580.46 --> 2580.96]  today
[2580.96 --> 2581.50]  at
[2581.50 --> 2582.04]  practical
[2582.04 --> 2582.38]  AI
[2582.38 --> 2583.26]  dot FM
[2583.26 --> 2584.06]  slash
[2584.06 --> 2584.56]  community
[2584.56 --> 2585.88]  thanks again
[2585.88 --> 2586.14]  to our
[2586.14 --> 2586.54]  partners
[2586.54 --> 2586.86]  at
[2586.86 --> 2587.20]  fly
[2587.20 --> 2587.82]  dot IO
[2587.82 --> 2588.64]  to our
[2588.64 --> 2588.86]  beat
[2588.86 --> 2589.10]  freaking
[2589.10 --> 2589.74]  residents
[2589.74 --> 2590.18]  break
[2590.18 --> 2590.44]  master
[2590.44 --> 2590.90]  cylinder
[2590.90 --> 2591.54]  and to
[2591.54 --> 2591.82]  you for
[2591.82 --> 2592.08]  listening
[2592.08 --> 2592.60]  we
[2592.60 --> 2593.00]  appreciate
[2593.00 --> 2593.32]  you
[2593.32 --> 2593.60]  spending
[2593.60 --> 2593.80]  time
[2593.80 --> 2593.94]  with
[2593.94 --> 2594.22]  us
[2594.22 --> 2595.02]  that's
[2595.02 --> 2595.18]  all
[2595.18 --> 2595.30]  for
[2595.30 --> 2595.74]  now
[2595.74 --> 2596.40]  we'll
[2596.40 --> 2596.62]  talk
[2596.62 --> 2596.82]  to you
[2596.82 --> 2596.98]  again
[2596.98 --> 2597.16]  next
[2597.16 --> 2597.70]  time
[2597.70 --> 2599.14]  transparent
[2599.14 --> 2599.46]  about
[2599.46 --> 2601.24]  the
[2601.24 --> 2601.58]  bell
[2601.58 --> 2602.74]  heart
[2602.74 --> 2604.10]  chamber
[2604.10 --> 2605.06]  Adapt
[2606.54 --> 2607.24] iels
[2607.24 --> 2608.68]  in
[2608.68 --> 2608.74] 증
[2608.74 --> 2609.42]  hashtag
