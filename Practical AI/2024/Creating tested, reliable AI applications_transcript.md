[0.00 --> 22.52]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[23.00 --> 23.92]  and accessible to all.
[24.24 --> 26.98]  If you like this show, you will love the changelog.
[26.98 --> 32.00]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[32.00 --> 33.86]  talk show for your weekend enjoyment.
[34.32 --> 38.30]  Find us by searching for The Changelog wherever you get your podcasts.
[38.80 --> 40.80]  Thanks to our partners at Fly.io.
[41.18 --> 43.56]  Launch your AI apps in five minutes or less.
[43.86 --> 45.82]  Learn how at Fly.io.
[56.98 --> 58.54]  What's up, friends?
[58.74 --> 61.72]  I'm here with Kurt Mackey, co-founder and CEO of Fly.
[61.90 --> 63.04]  As you know, we love Fly.
[63.32 --> 65.88]  That is the home of changelog.com.
[66.26 --> 68.52]  But Kurt, I want to know how you explain Fly to developers.
[68.84 --> 70.26]  Do you tell them a story first?
[70.54 --> 71.02]  How do you do it?
[71.34 --> 76.22]  I kind of change how I explain it based on almost like the generation of developer I'm
[76.22 --> 76.72]  talking to.
[76.72 --> 80.86]  So like for me, I built and shipped apps on Heroku, which if you've never used Heroku
[80.86 --> 83.74]  is roughly like building and shipping an app on Vercel today.
[83.94 --> 86.58]  It's just it's 2024 instead of 2008 or whatever.
[86.78 --> 89.72]  And what frustrated me about doing that was I didn't, I got stuck.
[90.02 --> 94.74]  You can build and ship a Rails app with a Postgres on Heroku, the same way you can build and
[94.74 --> 96.64]  ship a Next.js app on Vercel.
[96.98 --> 101.04]  But as soon as you want to do something interesting, like as soon as you want to, at the time, I
[101.04 --> 104.90]  think one of the things I ran into is like I wanted to add what used to be like kind
[104.90 --> 106.30]  of the basis for Elasticsearch.
[106.38 --> 108.14]  I want to do full text search in my applications.
[108.64 --> 112.86]  You kind of hit this wall with something like Heroku where you can't really do that.
[113.08 --> 117.22]  I think lately we've seen it with like people wanting to add LLMs kind of inference stuff
[117.22 --> 122.22]  to their applications on Vercel or Heroku or Cloudflare or whoever these days, they've
[122.22 --> 125.34]  started like releasing abstractions that sort of let you do this.
[125.34 --> 130.62]  But I can't just run the model I'd run locally on these black box platforms that are very
[130.62 --> 131.18]  specialized.
[131.52 --> 134.80]  For the people my age, it's always like, oh, Heroku was great, but I outgrew.
[134.90 --> 138.78]  And one of the things that I felt like I should be able to do when I was using Heroku was
[138.78 --> 141.86]  like run my app close to people in Tokyo for users that were in Tokyo.
[141.86 --> 143.04]  And that was never possible.
[143.46 --> 147.48]  For modern generation devs, it's a lot more Vercel based.
[147.66 --> 151.50]  It's a lot like Vercel is great right up until you hit one of their hard line boundaries.
[151.82 --> 152.82]  And then you're kind of stuck.
[152.92 --> 153.54]  There's the other one.
[153.64 --> 155.04]  We've had someone within the company.
[155.28 --> 158.96]  I can't remember the name of this game, but the tagline was like five minutes to start
[158.96 --> 159.86]  forever to master.
[160.20 --> 164.04]  It's sort of how our pitching fly is like you can get an app going in five minutes, but there's
[164.04 --> 167.22]  so much depth to the platform that you're never going to run out of things you can do
[167.22 --> 167.62]  with it.
[167.62 --> 175.30]  So unlike AWS or Heroku or Vercel, which are all great platforms, the cool thing we love
[175.30 --> 181.10]  here at ChangeLog most about Fly is that no matter what we want to do on the platform, we
[181.10 --> 187.18]  have primitives, we have abilities, and we as developers can charge our own mission on
[187.18 --> 187.50]  Fly.
[187.82 --> 190.28]  It is a no limits platform built for developers.
[190.76 --> 192.00]  And we think you should try it out.
[192.00 --> 194.68]  Go to fly.io to learn more.
[195.18 --> 196.56]  Launch your app in five minutes.
[196.88 --> 197.56]  Too easy.
[198.00 --> 200.06]  Once again, fly.io.
[212.68 --> 216.38]  Welcome to another episode of the Practical AI Podcast.
[216.38 --> 222.22]  In this fully connected episode of the show, Chris and I will keep you fully connected with
[222.22 --> 229.28]  everything that's happening in the world of AI and discuss some of the latest trends and
[229.28 --> 234.86]  share some learning resources for you to level up your machine learning and AI game.
[235.18 --> 236.12]  I'm Daniel Whitenack.
[236.22 --> 242.06]  I am CEO at Prediction Guard, where we're creating a private secure AI platform.
[242.06 --> 248.70]  And I'm joined, as always, by my co-host, Chris Benson, who is a principal AI research
[248.70 --> 250.16]  engineer at Lockheed Martin.
[250.46 --> 251.14]  How are you doing, Chris?
[251.32 --> 252.54]  Doing very well, Daniel.
[252.82 --> 254.32]  I know you're out traveling.
[254.78 --> 259.80]  And ironically, I think I'll be where you are next week, but I think you'll be gone by
[259.80 --> 259.94]  then.
[260.28 --> 261.12]  Swapping places.
[261.22 --> 261.72]  There you go.
[261.86 --> 263.68]  We're trading geographies here.
[263.98 --> 264.72]  Yeah, yeah.
[264.72 --> 275.08]  It's, I don't know why, November always seems to be heavy conference, event, summit, on-site
[275.08 --> 276.48]  month for me.
[276.60 --> 279.28]  I don't know exactly why that is.
[279.30 --> 283.52]  It's sort of the last little bit before the end of the year, maybe.
[283.70 --> 284.10]  I don't know.
[284.20 --> 287.42]  It's to make you earn that vegan turkey that you're going to enjoy, you know?
[287.66 --> 288.78]  Exactly, exactly.
[288.78 --> 291.04]  Yeah, I got it all picked out.
[291.24 --> 295.02]  So we're ready for Tofurky on Thanksgiving, for sure.
[295.14 --> 295.56]  Excellent.
[296.96 --> 303.02]  And speaking of other things to celebrate, I wanted to mention before we hop into other
[303.02 --> 311.12]  discussions today that our good friends over at the ML Ops community, so Demetrius and his
[311.12 --> 315.44]  crew, they've run a series of virtual conferences.
[315.44 --> 322.32]  One about LLMs and production, and another about data engineering and AI.
[323.00 --> 328.90]  And their latest in the series is called Agents in Production, which sounds very exciting.
[329.26 --> 335.00]  As you're listening to this episode, if you're listening to it right when it goes live, you
[335.00 --> 340.42]  can still probably catch the event live, but you can also catch the content afterwards,
[340.42 --> 346.82]  I'm sure as it's recorded, it looks like an amazing conference talking about AI agents
[346.82 --> 349.60]  moving from R&D to reality.
[350.26 --> 350.92]  Are you ready?
[351.12 --> 351.78]  Question mark.
[352.30 --> 353.76]  So go check it out.
[353.86 --> 355.88]  Their events are always great.
[356.02 --> 359.48]  So I wanted to mention that up front at the beginning of the show.
[360.38 --> 365.40]  Chris, do you have any active AI agents in your life?
[365.76 --> 366.30]  You know what?
[366.30 --> 369.24]  I actually don't right now, but I probably should.
[369.42 --> 372.34]  I feel bad that I can't say yes to you on that.
[372.76 --> 373.46]  But you know what?
[373.50 --> 380.44]  I've also read recently that the uptake on agents has been a lot slower than was expected.
[380.70 --> 384.42]  You know, it was kind of one of those hype things, and I think it's pretty hard.
[384.62 --> 386.82]  So maybe something to discuss.
[386.82 --> 393.86]  Yeah, maybe along those same veins, I see a lot of news articles, especially as related
[393.86 --> 400.34]  to, I think, what, you know, over the past, I guess, couple weeks or whenever it was that
[400.34 --> 406.02]  people realized that OpenAI wasn't going to release GPT-5.
[406.02 --> 411.46]  I don't know if there's expected this year and not really, anyway, not released on the
[411.46 --> 413.30]  timeline that people thought.
[413.54 --> 420.30]  And also some indications that maybe that next jump in the functionality of these AI models
[420.30 --> 425.04]  is proving more difficult than was originally thought.
[425.04 --> 433.70]  One question I had as related to that, Chris, was let's say we never get GPT-5.
[434.08 --> 436.88]  We're just stuck with all the models that we have now.
[437.12 --> 441.00]  So no more models were made in the world.
[441.68 --> 448.38]  What do you think the value of AI and kind of its integration across the enterprise and
[448.38 --> 454.64]  business and our personal lives, do you think it would still have the, you know, hype transformative
[454.64 --> 457.24]  effect that people are talking about?
[457.68 --> 462.46]  No, I mean, we've talked a little bit about that, you know, in terms of hype cycles and
[462.46 --> 463.86]  stuff on previous episodes.
[464.22 --> 469.46]  If you postulate that we're hitting a ceiling right there, I don't think it's no more models.
[469.60 --> 475.36]  I think what happens is that there's more open source that comes along and, you know, kind
[475.36 --> 480.44]  of at least catches up to where some of the leading ones are out there and you end up having
[480.44 --> 487.02]  the value of a commercial model is less because you have more open source options that are
[487.02 --> 487.44]  out there.
[487.56 --> 489.18]  And we're seeing that in industry anyway.
[489.30 --> 494.48]  I mean, you know, not everybody wants to pipe their data out to open AI or, you know,
[494.50 --> 496.80]  some of the other organizations doing the same thing.
[496.88 --> 503.64]  And so I think the availability of open models is going to happen regardless in terms of the
[503.64 --> 504.32]  uptake on that.
[504.32 --> 509.44]  And I think that would just kind of force that to happen sooner rather than you, if the
[509.44 --> 513.66]  leading models are no longer, you know, new ones coming out that are better and better
[513.66 --> 518.00]  to chase, they catch up and it kind of commoditizes the whole space even faster.
[518.84 --> 518.98]  Yeah.
[519.26 --> 526.26]  I think one of the things I was wondering was, let's say that regardless of whether it's an
[526.26 --> 527.76]  open model or closed model.
[527.76 --> 535.32]  So if I told you, Chris, you're an AI engineer actively integrating Gen AI functionality, and
[535.32 --> 540.78]  I told you the best model you're ever going to get on the open side, if you're using open
[540.78 --> 543.18]  models, maybe Lama 3.1 or whatever.
[543.68 --> 552.98]  And on the closed source side, maybe it's the latest Clod or GPT 4.0 or whatever that might
[552.98 --> 553.20]  be.
[553.70 --> 560.34]  So if that were the case, would that be like, man, I don't think we're going to be able to
[560.34 --> 562.32]  do all of what we had hoped to do with AI?
[562.60 --> 568.20]  Or do you think it's more of a, yeah, what is the level of transformation that you think
[568.20 --> 571.78]  we could still get with the current generation of models, let's call it?
[571.78 --> 576.00]  So it's kind of funny, and I know we've talked about this, you know, and some of our listeners
[576.00 --> 580.30]  will remember some of the previous conversations, but there's a lot more to AI than just the
[580.30 --> 581.12]  Gen AI models.
[581.30 --> 585.00]  You know, they've gotten all the spotlight the last couple of years, but there's a lot
[585.00 --> 585.62]  you can do.
[585.76 --> 590.94]  And honestly, you know, without going into detail, the things I think about all day every
[590.94 --> 593.48]  day, Gen AI is not the center of it.
[593.54 --> 596.82]  It's not the stuff in AI that I care the most about.
[596.92 --> 598.66]  It's not what's making me most productive.
[598.66 --> 603.18]  So are there many things you can do with Gen AI to be productive?
[603.50 --> 603.72]  Sure.
[604.20 --> 605.78]  And we're still learning how to do that.
[606.02 --> 609.70]  And I think that's harder than people realized to get there.
[609.94 --> 614.96]  And I think that's one of the reasons it's plunging down into the trough of disillusionment
[614.96 --> 617.12]  in the hype cycle as people are frustrated.
[617.30 --> 619.84]  But we will have lots of Gen AI things.
[620.00 --> 626.60]  But I think it reminds us, as we've said recently, to look at the larger landscape of AI capabilities
[626.60 --> 631.10]  out there and other things that we used to be excited about are incredibly productive
[631.10 --> 631.72]  these days.
[632.28 --> 634.34]  And yet we're not talking a lot about them.
[634.60 --> 639.68]  You know, deep reinforcement learning remains amazing in what it can do.
[639.86 --> 645.04]  And, you know, if you combine that with robotics and other areas, there's lots of really productive
[645.04 --> 646.24]  work being done out there.
[646.24 --> 648.36]  But it's not getting much media attention.
[648.80 --> 654.38]  Where my mind goes is that the current models that are available, if you think about that
[654.38 --> 663.08]  general purpose reasoning Gen AI model, are good enough, in my opinion, to do kind of most
[663.08 --> 666.24]  tasks at the sort of orchestration layer.
[666.34 --> 671.76]  And what I mean by that is, let's say that you wanted to do time series forecasting.
[671.76 --> 677.84]  I don't think that, you know, whatever model you look at on the Gen AI side, it's not the
[677.84 --> 679.48]  best time series forecaster.
[679.98 --> 684.56]  However, you know, there's really good tools for that that already exist.
[684.96 --> 687.50]  So, you know, Facebook Profit or something like that.
[687.72 --> 694.18]  And you can use the Gen AI model as almost the front end to tools like that, right?
[694.20 --> 699.96]  You can say, hey, I want to know what my revenue is going to be in six months, do a forecast
[699.96 --> 704.86]  or something like that, and use the model to extract the data that's needed to make that
[704.86 --> 711.56]  forecast and maybe call a tool like Profit or something to actually do the forecast and
[711.56 --> 712.84]  get something back.
[712.84 --> 719.70]  So I think even if we got stuck with the models as they're out there, to your point, there's
[719.70 --> 724.86]  a variety of purpose-built tools and non-Gen AI tools out there.
[724.86 --> 731.88]  Whether they be just rule-based tools or APIs or machine learning models or statistical models
[731.88 --> 738.38]  or whatever, that can do a variety of the really important tasks that we want to do.
[739.02 --> 745.36]  And the Gen AI models that we have now could serve as a way to orchestrate between those
[745.36 --> 753.00]  tasks and to, you know, create some really appealing workflows and automations and flexible
[753.00 --> 755.84]  interfaces and all of this stuff.
[756.50 --> 762.76]  So where my mind was going with that is I'm not that concerned if it takes a while for
[762.76 --> 764.60]  GPT-5 or the next.
[764.60 --> 770.82]  In my opinion, when I think about the rest of the time, I'll have to be a developer, an
[770.82 --> 771.72]  AI practitioner.
[772.28 --> 777.42]  For the rest of my career, I could keep myself busy, no problem with all of the things I have
[777.42 --> 783.02]  access to and create some really interesting products and tools and features and integrations
[783.02 --> 784.10]  and et cetera.
[784.10 --> 789.94]  I think that's a great insight right there is the fact that if you look at all of the different
[789.94 --> 795.88]  jobs and workflows people have out there in their careers and, you know, if you think of
[795.88 --> 800.66]  all these tools that we currently have today, like without having to go forward, I would argue
[800.66 --> 807.08]  that it would be a very practical next step, you know, for practical AI to be able to start
[807.08 --> 812.16]  assessing your workflows, assessing where these different tools and the models we have can
[812.16 --> 817.38]  make a difference and doing some process reengineering to figure out how you can do that.
[817.46 --> 822.28]  And I think that the vast majority of organizations out there have not done that sufficiently.
[822.52 --> 826.88]  They might've done that with a workflow or two, but they haven't gone through, you know,
[826.88 --> 831.34]  if they're especially large corporations have thousands and thousands of them, there are
[831.34 --> 837.24]  so many places where productivity can be enhanced by finding the places where people are struggling
[837.24 --> 842.64]  through their own workflows and where those align well with the capabilities in these models.
[842.94 --> 846.82]  That might be a place they want to invest a little bit and get a great long-term benefit
[846.82 --> 847.30]  out of it.
[847.80 --> 852.20]  But the next model coming, whatever model we're talking about, whichever line of models, family
[852.20 --> 857.44]  models always gets the attention rather than the kind of grunge work of going through your
[857.44 --> 861.92]  processes and finding where you can save a whole bunch of effort, a whole bunch of time
[861.92 --> 865.88]  in a matter of moments, you know, to increase productivity.
[866.64 --> 871.10]  Yeah, I think that there will be just a dry parallel, maybe.
[871.46 --> 878.50]  I know that people have drawn comparisons between this wave of AI technology and the onset of the
[878.50 --> 880.54]  internet and the web, that sort of thing.
[880.54 --> 890.18]  I think you could see that the basic components or many and many of the most impactful web-based
[890.18 --> 895.00]  technologies that have shaped culture and shaped our lives.
[895.42 --> 900.58]  The building block components of those were around from the very early days of the web.
[901.06 --> 904.26]  And there are sort of generational jumps, right?
[904.34 --> 910.22]  Like the, you know, the advent of streaming and all of what we now consume via streaming would
[910.22 --> 914.96]  not have been possible over certain types of internet connections and technology, right?
[915.04 --> 917.48]  So there's certainly generational shifts.
[917.86 --> 920.96]  But the building blocks were enough.
[921.08 --> 926.42]  And probably some of the people in those early days working with those building blocks could
[926.42 --> 932.12]  not have imagined the transformative and kind of culture-defining effects of those basic
[932.12 --> 932.92]  building blocks.
[932.92 --> 938.52]  And so I think we're in a similar scenario where the building blocks of what we have
[938.52 --> 945.10]  with AI, whether that be gen AI or non-gen AI, are enough to, I don't think it would be too
[945.10 --> 948.08]  far to say transform certain elements of our culture.
[948.34 --> 951.72]  Sounds sort of grandiose, but I think that's sort of what's coming.
[952.44 --> 960.14]  But there will likely be the kind of generational jumps, whether that be GPT-5 or another language
[960.14 --> 965.04]  family or whatever, there will likely be generational jumps that we also don't anticipate yet.
[965.56 --> 971.48]  But the tooling that we already have, the building blocks we already have are enough to create
[971.48 --> 975.12]  transformative technologies and products and systems.
[975.54 --> 976.42]  I would agree.
[976.56 --> 980.28]  I think maybe there's another show where we talk about what we think the transformation
[980.28 --> 983.92]  of society and culture is in the future.
[984.06 --> 985.76]  I don't think that's this show right now.
[985.76 --> 987.36]  But I would agree with you.
[987.60 --> 990.22]  With what we have today, we can go a long way.
[990.38 --> 993.74]  And to your point, I was in college when the web came into being.
[994.44 --> 1001.16]  So I do remember exactly those very early building blocks and trying to imagine.
[1001.44 --> 1004.44]  And this is not the same world that we live in today that it was then.
[1004.44 --> 1020.50]  Okay, friends, I'm here with a new friend of ours over at Timescale Avthar.
[1020.78 --> 1025.06]  So Avthar, help me understand what exactly is Timescale.
[1025.28 --> 1026.82]  So Timescale is a Postgres company.
[1027.30 --> 1032.60]  We build tools in the cloud and in the open source ecosystem that allow developers to do
[1032.60 --> 1033.46]  more with Postgres.
[1033.74 --> 1038.60]  So using it for things like time series, analytics, and more recently, AI applications like RAG
[1038.60 --> 1039.64]  and Search and Agents.
[1039.64 --> 1045.86]  Okay, if our listeners were trying to get started with Postgres, Timescale, AI application development,
[1046.40 --> 1047.06]  what would you tell them?
[1047.40 --> 1048.06]  What's a good roadmap?
[1048.44 --> 1053.36]  If you're a developer out there, you're either getting tasked with building an AI application,
[1053.64 --> 1057.10]  or you're interested and you're seeing all the innovation going on in the space and want
[1057.10 --> 1058.04]  to get involved yourself.
[1058.04 --> 1064.54]  And the good news is that any developer today can become an AI engineer using tools that
[1064.54 --> 1065.64]  they already know and love.
[1065.88 --> 1070.56]  And so the work that we've been doing at Timescale with the PGAI project is allowing developers
[1070.56 --> 1075.78]  to build AI applications with the tools and with the database that they already know, and
[1075.78 --> 1076.60]  that being Postgres.
[1076.94 --> 1081.06]  What this means is that you can actually level up your career, you can build new interesting
[1081.06 --> 1085.94]  projects, you can add more skills without learning a whole new set of technologies.
[1085.94 --> 1091.84]  And the best part is it's all open source, both PGAI and PG Vector Scale are open source.
[1091.98 --> 1096.38]  You can go and spin it up on your local machine via Docker, follow one of the tutorials on the
[1096.38 --> 1102.08]  Timescale blog, build these cutting edge applications like RAG and Search without having to learn 10
[1102.08 --> 1106.82]  different new technologies and just using Postgres in the SQL query language that you will probably
[1106.82 --> 1108.26]  already know and are familiar with.
[1108.58 --> 1109.64]  So yeah, that's it.
[1109.72 --> 1110.46]  Get started today.
[1110.46 --> 1116.50]  It's a PGAI project and just go to any of the Timescale GitHub repos, either the PGAI
[1116.50 --> 1121.40]  one or the PG Vector Scale one and follow one of the tutorials to get started with becoming
[1121.40 --> 1123.26]  an AI engineer just using Postgres.
[1123.72 --> 1124.10]  Okay.
[1124.60 --> 1131.34]  Just use Postgres and just use Postgres to get started with AI development, build RAG, Search,
[1131.64 --> 1133.84]  AI agents, and it's all open source.
[1133.84 --> 1142.82]  Go to timescale.com slash AI, play with PGAI, play with PG Vector Scale, all locally on your
[1142.82 --> 1143.28]  desktop.
[1143.44 --> 1144.34]  It's open source.
[1144.72 --> 1148.00]  Once again, timescale.com slash AI.
[1163.84 --> 1177.58]  I've been usually teaching workshops again.
[1177.58 --> 1181.20]  I'll be at QCon SF next week.
[1181.60 --> 1186.14]  So those of you that are around QCon, I'll look forward to seeing you.
[1186.20 --> 1187.46]  It looks like a good event.
[1187.46 --> 1196.56]  But some of what's come up, I think, in workshops for me recently is how to think kind of about
[1196.56 --> 1203.58]  your AI workflows going from prototype to some level of production.
[1204.10 --> 1211.52]  And I think these are things that we've talked about on the show before prior to Gen AI in terms
[1211.52 --> 1219.90]  of how you want to be testing and monitoring and thinking about deployment of AI-based workflows.
[1220.42 --> 1226.34]  But I'm guessing there's a lot of people maybe joining the show from different backgrounds
[1226.34 --> 1228.68]  after this Gen AI phase.
[1228.82 --> 1235.34]  And I connect this to the sentiment that people often with this technology are able to get to
[1235.34 --> 1241.56]  a point really quickly where they see an amazing workflow kind of come to shape, right?
[1241.88 --> 1247.04]  And it works amazing in like some of the time, like half the time.
[1247.22 --> 1251.28]  And then the other half of the time, it fails miserably, right?
[1251.40 --> 1253.74]  But they get sort of the taste of the goodness.
[1254.54 --> 1258.56]  And they maybe don't know how to get the rest of the way.
[1258.56 --> 1265.76]  And I thought of an interesting parallel because some people are using these kind of low-code,
[1265.84 --> 1268.90]  no-code AI workflow builder tools, right?
[1269.00 --> 1275.70]  Whether that be something like FlowWise or Gumloop, Diffy, which is like, you know, these
[1275.70 --> 1277.64]  little interfaces you can string things together.
[1277.64 --> 1282.42]  Or it's like built into tools like AlterX or something like that that's maybe a little bit
[1282.42 --> 1283.64]  more enterprise-y focused.
[1283.64 --> 1288.06]  But they build out this workflow and it sort of does this thing.
[1288.16 --> 1291.76]  It works like half of the time and not the other half of the time.
[1291.98 --> 1295.02]  And maybe they're using AI calls as part of that.
[1295.60 --> 1302.16]  And it struck me that this is sort of like, I don't know if you remember, Chris, back in
[1302.16 --> 1309.86]  the day, we had a phase of our AI podcast life where we were really trying to convince
[1309.86 --> 1313.08]  people that they shouldn't run notebooks in production.
[1313.64 --> 1317.32]  Do you remember these days of data science?
[1317.76 --> 1318.52]  Yeah, I do.
[1318.68 --> 1319.84]  That's a little ways back.
[1319.94 --> 1321.06]  But yes, I do.
[1321.24 --> 1321.52]  Indeed.
[1322.06 --> 1326.82]  So for those that aren't familiar, when I say notebook, I'm referring to like a Jupyter
[1326.82 --> 1327.64]  notebook.
[1327.80 --> 1332.58]  So this is an interactive web-based code editor.
[1332.84 --> 1338.92]  And if you imagine, maybe some of you that have used Mathematica in the past is similar,
[1338.92 --> 1341.40]  but you kind of go into the screen.
[1341.54 --> 1344.04]  There's a cell that you can put code in.
[1344.10 --> 1345.32]  You can execute that cell.
[1345.44 --> 1346.44]  You can take notes.
[1346.54 --> 1348.56]  You can execute another cell of code.
[1348.96 --> 1351.36]  And all of that state is saved.
[1351.36 --> 1356.98]  So you can like execute cell one and then go down to cell five and re-execute cell five
[1356.98 --> 1361.26]  and then go up to cell three and re-execute cell three and then go down to cell seven and
[1361.26 --> 1362.74]  re-execute cell seven.
[1363.26 --> 1370.92]  And what happens is, so if we just rewind our mind back to the olden days, I'm a data scientist.
[1370.92 --> 1375.16]  I'm building a model or creating a workflow and I'm doing this in a notebook.
[1375.64 --> 1386.24]  That sort of workflow generally is good for experimentation and produces really, really terrible code just by its nature.
[1386.68 --> 1388.14]  So it's really good for experimentation.
[1388.14 --> 1393.08]  But if I'm hopping around all the time, I don't really understand what the state in the background is.
[1393.60 --> 1396.38]  I'm like hopping around between cells.
[1396.38 --> 1401.36]  I can give you the same notebook and you could never reproduce what I did.
[1401.86 --> 1406.22]  Even though it's the same exact code, you could never reproduce my exact sort of steps.
[1406.94 --> 1415.74]  And I just was struck by the fact that the way that people, it's almost like we forgot that that doesn't work that well.
[1415.88 --> 1418.24]  And now we're just doing it not in notebooks.
[1418.24 --> 1424.92]  We're doing it in these low code, no code tools or with agents that jump around between various tasks.
[1424.92 --> 1437.28]  Right. And part of this is the same reason why notebooks are really terrible at producing good, reliable code is the is the same reason.
[1437.48 --> 1446.80]  I think why people are taking these AI workflows from tools that they're using and aren't able to make them robust and reliable.
[1446.80 --> 1448.56]  So that's my hot take for the day.
[1448.90 --> 1449.98]  What's your thought, Chris?
[1449.98 --> 1456.72]  No, I think that's great. First of all, I got to say, boy, it's already making me feel aged again in a different way.
[1456.78 --> 1463.84]  The fact that it wasn't that long ago that it was all the hotness of Jupyter Notebooks, you know, that we were talking about.
[1463.96 --> 1465.20]  And that was the cool thing.
[1465.44 --> 1469.76]  Yeah. And even like products managing all your notebooks and such.
[1469.76 --> 1474.56]  Yeah. It feels like you just gave a eulogy, you know, for Jupyter Notebooks to some degree.
[1474.70 --> 1477.76]  And so it's a reminder that things are changing constantly.
[1478.00 --> 1487.70]  So you bring a great point that, you know, we're taking some of the same challenges that we had in that environment and we're just recreating them in the newer tools that are out there.
[1488.26 --> 1489.74]  There was another company I worked at.
[1489.74 --> 1492.38]  I won't name the company before I was at Lockheed.
[1492.80 --> 1504.88]  And at that company, I remember thinking there were people at the time that knew they knew the AI modeling bit and there were people that knew the software bit, but they never seemed to cross over.
[1504.88 --> 1517.60]  And when you raise the point about your kind of in-process development workflow and then how do you actually get that to some level of production, I think there's a lot of people out there that aren't going to know that.
[1517.76 --> 1524.18]  And unless times have really changed in that area, and my gut says they probably haven't, people tend to focus on the thing that they want to do.
[1524.86 --> 1528.98]  What is the right development workflow and how do you start getting to that production environment?
[1529.12 --> 1532.90]  I know you've gotten tons and tons of experience at that in recent years.
[1533.38 --> 1534.34]  How do you think about it?
[1534.34 --> 1536.68]  Can you frame it a little bit before you dive into it?
[1537.20 --> 1553.32]  Yeah, well, I was thinking about it in light of this parallel to what we went through in the data science world with notebooks and these kind of ad hoc workflows that execute some of the time and not other times, depending on how you execute them.
[1553.32 --> 1565.74]  And in reality, the answer to running that code in production is not the file download as Python script thing.
[1565.84 --> 1571.20]  Because that just will never work because the state and the workflow is not preserved.
[1571.20 --> 1587.84]  How that actually gets productionized or would be productionized in the past is taking the logical steps that are being executed in that workflow and taking those out of the notebook and embedding them in actual code.
[1587.84 --> 1592.32]  In this case, you know, Python code in functions or classes.
[1592.32 --> 1601.22]  And attaching tests to those functions or classes just like a software engineer would do because this is software engineering.
[1601.22 --> 1617.28]  And then figuring out, you know, again, doing the testing on the front end of that, whether that's a UI system or that's an API or whatever it is, to make sure that the behavior that you were testing in your notebook actually works.
[1617.28 --> 1622.56]  And that kind of sucks because it's a re-implementation, right?
[1622.70 --> 1625.46]  To some degree, maybe you don't have to throw everything out.
[1625.54 --> 1629.92]  Like you got something working in your notebook and you can bring it through and have it work.
[1630.04 --> 1636.10]  But it does take actual work to go from that notebook state to the production code.
[1636.76 --> 1647.02]  And so I think if you just look at one of these tools, and I do think some of these tools, the kind of low code, no code, assistant builders, workflow builders,
[1647.28 --> 1658.54]  with AI stuff are useful and can be useful in your maybe building out nice workflows for your personal life, right?
[1658.54 --> 1670.96]  Like email assistant stuff or automations to, you know, turn news articles into podcasts or whatever the thing is, right, that you want to do.
[1671.30 --> 1677.10]  But ultimately, these tools have their own opinionated way of tracing and testing and you debugging.
[1677.28 --> 1677.82]  Right.
[1678.44 --> 1687.56]  The same way that like debugging a Jupyter notebook, you have slightly different tooling, you have a slightly different workflow than if you were debugging regular code.
[1688.16 --> 1705.52]  And so I think part of the answer, unfortunately, and I guess this is my hot take if there is one, is I think that we're going to see a similar dynamic in the AI engineering world where like a business person,
[1705.52 --> 1706.52]  except I think the roles are different here.
[1706.52 --> 1725.52]  So similar way to like before the data scientist would build a workflow in a Jupyter notebook and maybe a software engineer would integrate that in to actual code that's tested and has some form that resembles actual code.
[1725.52 --> 1729.52]  And the data scientist is probably interacting with the business person.
[1729.52 --> 1735.52]  In this case, it's slightly different role wise because the data scientist almost isn't there.
[1735.52 --> 1757.32]  But the business person might go into a tool like Gumloop or Flowwise or Diffie or whatever and build out a tool that takes market analysis things and generates, I don't know, articles or summaries that go into some emails that are sent out to the company or whatever workflow that they created.
[1757.32 --> 1768.92]  Right. And it has a series of steps and they're like, yeah, this like this works, but it kind of does work, but it kind of doesn't work because they haven't thought about all the edge cases and it's hard to debug.
[1769.18 --> 1775.44]  It's hard to know when it's down. And so I think now it's like that business person bringing that workflow.
[1775.44 --> 1790.58]  So if it really truly does need to be scaled across an organization or released as a product on its own, you just sort of have to take those steps out and actually put them in functions, put them in classes in your code that can be tested.
[1790.68 --> 1794.76]  And we can talk about like the methodology of testing here in a second.
[1794.76 --> 1803.22]  So I think that the low code, no code things are cool and awesome and have their place just like notebooks have their place.
[1803.32 --> 1809.76]  And I still use primarily Google Colab, not Jupyter locally, but Google Colab notebooks.
[1810.46 --> 1813.90]  I still use notebooks. I just realize their limitations.
[1814.72 --> 1822.48]  Right. Maybe sometimes better than other times, but I realize their limitations and then I eventually write software.
[1822.48 --> 1836.54]  So I think it's a similar thing with these tools that are up and coming is they're great and they allow for quick prototyping and business people to get their workflows and their ideas into a workflow that operates.
[1837.20 --> 1846.70]  But ultimately, this has to become software if the intention is to make it a feature that you release or something that scales across your organization or something like that.
[1846.70 --> 1855.74]  Let me ask you, I'm just curious, when you're in Colab and you're doing that and you decide it's time to write software, how do you make your own transition?
[1855.98 --> 1860.34]  What do you do? Having done this for so long, what's your transition look like?
[1860.58 --> 1865.30]  Are you staying in Python? Are you converting some of that over into Go or something else?
[1865.44 --> 1866.86]  Or how do you think about it?
[1866.86 --> 1879.20]  I think if it's, it depends, of course, case by case, but generally I would say if I'm doing it in Colab, it probably means that I'm doing something that requires Python.
[1880.20 --> 1886.56]  And so that's, you know, I don't know, doing something in Langchain or PyTorch or whatever the thing is.
[1886.56 --> 1893.84]  Then I think when I'm ready, I essentially have two ideas in my head of where that's going to live.
[1894.08 --> 1902.46]  Either it's going to live in a REST API because you're going to have to make this functionality available to the rest of your software.
[1902.70 --> 1905.20]  So it's either going to live in a REST API.
[1905.64 --> 1910.20]  It's going to be integrated into some software you're already supporting, right?
[1910.20 --> 1919.50]  So that already has a code base or it's going to be run as a script, kind of an offline script at a certain, you know, K insert or something like that.
[1920.20 --> 1927.24]  And so if it's the API scenario, you know, I have a bunch of code that I've written over time with fast API.
[1927.82 --> 1937.68]  I can just copy one of those projects, rip out the stuff that is irrelevant and put in the stuff that's relevant, kind of copying over from the notebook.
[1937.68 --> 1942.76]  So if it's more of the native software integration, I think that really depends on.
[1943.36 --> 1948.74]  So if it's what kind of application it is, what the architecture is, that sort of thing.
[1948.82 --> 1959.66]  And so that might involve a change of language or a change of the type of infrastructure that you're using or the type of database you're connecting to or whatever that might be.
[1959.66 --> 1974.32]  And that's an area that I'm keenly interested in because, you know, historically we have we've been, you know, developing these models in Python and then deploying them in Python, mainly because that's where the tools and stuff are still at.
[1974.32 --> 1987.88]  But there's a number of use cases, especially as we go forward and we're looking at autonomy and we're looking at robotics and things like that, where in many of those cases, Python is not the best language for the platform that you're deploying to.
[1988.52 --> 1997.84]  And so you have this incongruity between the development environment in a distinctly different production or deployment environment that you're trying to target.
[1997.84 --> 2008.56]  And so, you know, in my world, there are many things that might start in Python that probably should end in something like Rust, given what we're, you know, what we're trying to accomplish here.
[2008.84 --> 2015.78]  So I think that that still remains a very immature deployment kind of arena to work in.
[2015.78 --> 2028.30]  And I'm rather hoping that in the years to come, maybe we see more tools from tool providers and open source in that arena that can actually cross over from one language to another to make sure that it's always the right one for what you're dealing with.
[2045.78 --> 2049.92]  What's up, friends?
[2050.06 --> 2051.70]  I love my 8sleep.
[2051.78 --> 2053.60]  Check them out, 8sleep.com.
[2053.68 --> 2055.38]  I've never slept better.
[2055.72 --> 2057.30]  And, you know, I love biohacking.
[2057.46 --> 2058.96]  I love sleep science.
[2059.16 --> 2065.66]  And this is all about sleep science mixed with AI to keep you at your best while you sleep.
[2065.88 --> 2069.54]  This technology is pushing the boundaries of what's possible in our bedrooms.
[2070.14 --> 2073.74]  Let me tell you about 8sleep and their cutting edge pod for ultra.
[2073.74 --> 2076.18]  So what exactly is the pod?
[2076.36 --> 2081.40]  Imagine a high-tech mattress cover that you can easily add to any bed.
[2081.72 --> 2084.24]  But this isn't just any cover.
[2084.50 --> 2091.16]  It's packed with sensors, heating and cooling elements, and it's all controlled by sophisticated AI algorithms.
[2091.76 --> 2098.48]  It's like having a sleep lab, a smart thermostat, and a personal sleep coach all rolled into one single device.
[2098.48 --> 2104.86]  And the pod uses a network of sensors to track a wide array of biometrics while you sleep.
[2105.10 --> 2110.04]  It tracks sleep stages, heart rate variability, respiratory rate, temperature, and more.
[2110.48 --> 2111.90]  And the really cool part is this.
[2112.04 --> 2115.56]  It does all this without you having to wear any devices.
[2116.18 --> 2120.84]  The accuracy of this thing rivals what you would get in a professional sleep lab.
[2120.84 --> 2123.10]  Now, let me tell you about my personal favorite thing.
[2123.28 --> 2124.16]  Autopilot recap.
[2124.36 --> 2129.50]  Every day, my 8sleep tells me what my autopilot did for me to help me sleep better at night.
[2129.80 --> 2130.74]  Here's what it said last night.
[2131.20 --> 2135.68]  Last night, autopilot made adjustments to boost your REM sleep by 62%.
[2135.68 --> 2136.54]  Wow.
[2136.54 --> 2137.84]  62%.
[2137.84 --> 2151.16]  That means that it updated and changed my temperature to cool, to warm, and helped me fine-tune exactly where I wanted to be with precision temperature control to get to that maximum REM sleep.
[2151.58 --> 2155.36]  And sleep is the most important function we do every single day.
[2155.48 --> 2159.12]  As you can probably tell, I'm a massive fan of my 8sleep, and I think you should get one.
[2159.12 --> 2167.92]  So go to 8sleep.com slash changelog, and right now they have an awesome deal for Black Friday going from November 11th through December 14th.
[2168.10 --> 2175.56]  The discount code changelog will get you up to $600 off the Plug4Ultra when you bundle it.
[2175.80 --> 2181.12]  Again, the code to use is changelog, and that's from November 11th through December 14th.
[2181.78 --> 2185.08]  Once again, that's 8sleep.com slash changelog.
[2185.26 --> 2186.24]  I know you'll love it.
[2186.24 --> 2189.14]  I sleep on this thing every night, and I absolutely love it.
[2189.32 --> 2191.58]  It's a game changer, and it's going to change your game.
[2191.84 --> 2195.18]  Once again, 8sleep.com slash changelog.
[2203.88 --> 2213.74]  Well, Chris, I kind of started talking about the testing and integration of some of these workflows and how I see that playing out.
[2213.74 --> 2220.74]  From my experience in talking with people, there's some general confusion around how to...
[2221.78 --> 2231.90]  So let's assume that you're convinced that I want to rip out these various pieces of workflow that have maybe been prototyped in a low-code, no-code tool,
[2231.90 --> 2239.86]  and I want to put them into some software that's an API or a UI or a script, a data pipeline, whatever that is.
[2240.34 --> 2242.02]  Let's assume that you're convinced of that.
[2242.78 --> 2252.76]  Then the question comes, well, okay, now I have this function or I have this class in code that executes some sort of AI call, a call to an AI model.
[2252.76 --> 2260.00]  How do I test that and what sort of considerations might need to be in place around that?
[2260.36 --> 2263.58]  And I often find that this sort of breaks people's mind.
[2263.58 --> 2273.58]  And this is also something that I think we've dealt with for a long time in the data science world, which is...
[2274.14 --> 2274.90]  It's just very...
[2274.90 --> 2280.78]  I guess overall it's very interesting to me that these same types of things are popping up, but with a new audience.
[2280.78 --> 2293.92]  So I don't know if you remember back in the days of data science, when there were data scientists, they would create a model and that model has a certain level of performance, right?
[2293.98 --> 2296.62]  Like at 90% accuracy or something, right?
[2296.62 --> 2298.32]  So it's going to be wrong some of the time.
[2298.98 --> 2301.18]  So you put that model into...
[2301.18 --> 2303.68]  Maybe it's a fraud detection model.
[2303.92 --> 2305.34]  Fraud or not fraud, right?
[2305.34 --> 2311.38]  You put that model into production, you integrate it into a software function.
[2312.18 --> 2315.26]  And now the question comes, well, how do you test that model?
[2315.28 --> 2319.92]  Because it's not always going to give the same response and it's not always going to be right.
[2320.34 --> 2325.72]  I don't know if you remember these discussions happening a lot in the data science world.
[2326.24 --> 2329.08]  Yeah, I think you just wrote a eulogy for data science as well.
[2329.82 --> 2331.24]  The way you phrase it.
[2332.08 --> 2333.36]  Oh my goodness.
[2333.36 --> 2340.38]  But this one always really intrigued me because my background is in physics.
[2341.14 --> 2345.30]  And so if we said, oh, this model is not deterministic, right?
[2345.38 --> 2347.44]  So we can't test it.
[2347.60 --> 2358.76]  If we took that approach in physics, we basically wouldn't have any of the technology that we have today because it's all based on quantum mechanics and everything is a probability distribution.
[2358.76 --> 2365.98]  So there is a way to test things that behave non-deterministically like AI models.
[2366.28 --> 2371.04]  And maybe that people just sort of need a bit of a reminder about that.
[2371.38 --> 2376.60]  And I often kind of break this down into a few categories.
[2376.60 --> 2378.16]  But yeah, I don't know.
[2378.24 --> 2386.32]  Do you come across people with this sort of mindset, especially in integrating kind of LLMs or something like this?
[2386.46 --> 2387.14]  All the time.
[2387.50 --> 2389.28]  I think there's a lot of people out there.
[2389.86 --> 2392.88]  I think everyone's still kind of figuring that out, quite honestly.
[2392.88 --> 2404.30]  If they're not in the business that you're in where you're dealing with that constantly, I think that's one of the big unknowns with folks in general is how do I go about testing this?
[2404.34 --> 2405.16]  I want to get in the workflow.
[2405.66 --> 2406.54]  I don't think people know.
[2406.84 --> 2411.34]  At least you can only do so much in a 45-minute podcast.
[2411.34 --> 2423.10]  But at least to sketch out maybe a good framework for people to think about is, number one, I think you should have tests in your code for each step of the process, right?
[2423.14 --> 2431.54]  So if you have an LLM-based workflow and the first step of that is translating something into Spanish.
[2431.74 --> 2434.64]  And then the next step is summarizing it in one sentence.
[2434.82 --> 2438.24]  And the next step is embedding that one sentence in a template.
[2438.24 --> 2446.36]  And then the next thing is generating an image for whatever kind of string of things you have going on.
[2446.92 --> 2461.16]  You should have tests for each of those kind of subtasks in the chain of processing, which partially also gets to why testing agents is hard, which is, I think, an interesting thing to maybe circle back to at the end.
[2461.44 --> 2464.72]  I think that's just good software engineering, what you're describing.
[2464.72 --> 2476.94]  And, you know, if you took it out of the AI world and talked about software functions, you want to, each one is a discrete function that does something and you want to test it on its own, even though they're all connected together to do something.
[2477.06 --> 2478.92]  I think that's just really sensible.
[2479.44 --> 2479.58]  Yeah.
[2479.70 --> 2485.84]  And the, you know, the agent stuff makes this maybe a little bit more difficult, which we can come back to.
[2485.84 --> 2494.40]  But let's assume that you have a workflow that you just want to execute over and over again, which is probably most enterprise use cases.
[2494.76 --> 2496.96]  So you split that up into subtasks, right?
[2497.02 --> 2499.22]  You have subtasks that you can test.
[2499.66 --> 2509.36]  The next thing I would recommend is to have people think about creating a set of tests in three categories.
[2509.36 --> 2513.96]  And this comes kind of from the ideas of behavioral testing.
[2514.76 --> 2520.42]  And this is like, just take the fraud detection piece for a second.
[2520.62 --> 2523.68]  So you're asking fraud or not fraud, right?
[2523.90 --> 2535.34]  So the first category of tests you want to think about is minimum functionality tests, which would be this, you know, is the most fraudulent thing I can think of.
[2535.34 --> 2546.00]  It should always, like, be most fraudulent Russian characters, you know, Nigerian prints, whatever, you know, take your pick, right?
[2546.64 --> 2548.58]  Should always be labeled fraud, right?
[2548.70 --> 2551.78]  100% of the time, that is a minimum functionality.
[2552.48 --> 2560.62]  These are not the most in-depth of tests, but they should pass 100% of time, no matter what you do to the model, no matter what you do to your system.
[2561.00 --> 2563.18]  These are like 100% pass.
[2563.18 --> 2575.78]  And you can do the same thing with LLMs, you know, even though it's not a classifier, you can say, I'm creating a bot that asks, you know, it gives all the information about prediction guard.
[2576.00 --> 2581.24]  If I ask who is the CEO of prediction guard, they should always return the same name, right?
[2581.52 --> 2582.90]  That's a minimum functionality.
[2583.16 --> 2584.34]  That's a pretty easy question.
[2584.44 --> 2585.86]  It should be embedded in the knowledge.
[2585.86 --> 2593.20]  You know, these are things that should 100% be returned and that you could test for deterministically, right?
[2593.36 --> 2595.62]  Like, does that name appear in the response?
[2595.90 --> 2596.54]  That sort of thing.
[2597.04 --> 2609.70]  The second category would be, in fancy terms, might be called invariant perturbations, but basically in non-fancy terms, changes in the input that don't produce a change in the output.
[2609.70 --> 2617.28]  So the classic example of this is if I ask an LLM maybe to do a sentiment analysis of a statement.
[2618.16 --> 2620.90]  And the statement is, I love the United States.
[2621.00 --> 2621.88]  It is so amazing.
[2622.24 --> 2623.18]  It is so great.
[2623.70 --> 2625.60]  I get positive sentiment return.
[2626.02 --> 2631.14]  If I change the United States to Turkey, I say, Turkey is so great.
[2631.22 --> 2631.88]  It is amazing.
[2632.04 --> 2632.72]  It is wonderful.
[2632.72 --> 2633.44]  Right.
[2633.50 --> 2642.68]  In theory, regardless of what you think about, what you personally think about the United States or Turkey, that should always return positive sentiment.
[2642.98 --> 2643.10]  Right.
[2643.44 --> 2645.62]  That is invariant change in the input.
[2645.62 --> 2648.00]  So you can make changes in the formatting.
[2648.26 --> 2650.18]  You can make changes in the ordering of things.
[2650.40 --> 2652.62]  And all of these should produce invariant changes.
[2652.62 --> 2663.80]  And then, of course, the final one would be the necessarily variant changes, meaning a change in the input should definitely produce a change in the output.
[2664.46 --> 2664.64]  Right.
[2664.82 --> 2673.16]  Like if I change I love the United States to I do not love the United States, I should actually have a change in the output.
[2673.16 --> 2675.44]  And that's a very easy thing to see.
[2675.44 --> 2675.80]  Right.
[2676.16 --> 2684.68]  And so what you do is you create a table of minimum functionality tests, a table of invariant tests, a table of variant tests.
[2685.14 --> 2694.88]  And if you have those full tables, you can basically probe the behavior of the model and the sensitivity of your model to changes.
[2695.56 --> 2699.96]  And this sensitivity is really the thing that people get hung up on with these workflows.
[2699.96 --> 2705.40]  They don't realize how sensitive the models are to small changes in the input.
[2705.94 --> 2715.36]  And so this allows you to gauge the sensitivity of your system to a real number from passing these tests and then work systematically to improve that.
[2716.72 --> 2720.62]  So I'm trying to just kind of put all that together for my own learning purpose.
[2720.62 --> 2723.96]  And I'm trying to think how how we can apply that to workflow directly.
[2723.96 --> 2729.68]  Like how how do you how do you actually fit that in to the nuts and bolts of moving it into production?
[2729.88 --> 2731.50]  Where do you do that in your workflow?
[2731.78 --> 2731.92]  Yeah.
[2732.04 --> 2733.92]  So I would take kind of the steps.
[2734.36 --> 2736.92]  Let's say I have a workflow with five steps.
[2737.10 --> 2743.80]  I take each of those steps and I produce, you know, five functions or five classes or however that fits into your code.
[2743.80 --> 2744.32]  Right.
[2744.72 --> 2755.10]  And for function one corresponding to step one, I create a table of each of those tests with table meaning just input equals output.
[2755.22 --> 2756.82]  The same as you are testing an API.
[2757.04 --> 2760.72]  Like if I get this input into my API, I should definitely return this.
[2760.84 --> 2761.00]  Right.
[2761.00 --> 2778.62]  And so you create that table and a set of unit tests or whatever testing framework you use to go over each one of those examples in your table and check the output to make sure it corresponds with what you expect to get either a passing or a not passing score.
[2778.62 --> 2782.60]  So the steps would be I have my five steps of my workflow.
[2782.86 --> 2788.18]  I split each of those up into a function or class or whatever the relevant programming object is.
[2788.34 --> 2792.48]  And then I develop these sorts of tests for each of those functions or classes.
[2793.10 --> 2798.82]  Now, the one question that might come up here is, well, should my model always pass?
[2799.26 --> 2799.40]  Right.
[2799.54 --> 2802.48]  Or should that function always pass all of those tests?
[2802.48 --> 2812.20]  And what I tell people is, well, should always pass 100 percent of the minimum functionality tests because you've defined those from the start as minimum functionality.
[2812.44 --> 2816.58]  So if you're not having minimum functionality, then your software shouldn't be released.
[2817.08 --> 2817.20]  Right.
[2817.48 --> 2823.34]  And then the other ones, basically, I would say you should never be regressing in those.
[2823.58 --> 2823.78]  Right.
[2823.96 --> 2829.62]  They give you a sense of what the sensitivity of your model is in those variations.
[2830.04 --> 2832.06]  And you would not want to regress.
[2832.06 --> 2834.48]  You would want to systematically make those better.
[2835.28 --> 2842.34]  So some people might treat those as a certain percentage or a threshold that needs to be above that or something like that.
[2842.96 --> 2843.08]  Gotcha.
[2843.38 --> 2845.76]  That takes us back to your point earlier.
[2846.02 --> 2848.76]  It just sounds like data science, good data science right there.
[2849.46 --> 2849.70]  Yeah.
[2849.98 --> 2850.24]  Yeah.
[2850.40 --> 2854.02]  Well, it's interesting because the roles have shifted.
[2854.22 --> 2854.44]  Right.
[2854.44 --> 2864.94]  I think we went through those phases of data science being very Wild West to all the way up to like good engineering practices and testing and all of that.
[2864.94 --> 2874.22]  And we kind of now throw out the data scientists in the middle and we have business people developing these workflows and trying to integrate them into software.
[2874.22 --> 2879.64]  And yeah, there's a lot of reminders and learning, I think, that needs to be done.
[2879.64 --> 2885.62]  And that connects, you know, to where we started out the day, which is agents and production.
[2886.20 --> 2889.44]  Agents are hard to test because you don't know the workflow up front.
[2889.96 --> 2890.08]  Right.
[2890.08 --> 2895.10]  An agent determines what steps it's going to accomplish on the fly.
[2895.78 --> 2902.34]  And so if you don't know that workflow up front, then there's some interesting things that you might need to do to test those.
[2902.44 --> 2904.48]  But maybe we'll save that for another episode.
[2905.16 --> 2912.86]  And or people could join the great learning opportunity that is the agents and production event from the ML Ops community.
[2913.42 --> 2913.98]  Oh, absolutely.
[2914.84 --> 2915.08]  Yeah.
[2915.12 --> 2915.68]  You know what?
[2915.68 --> 2921.04]  You started the show asking what agents I had now and I had to I had to say, no, I didn't have any going.
[2921.44 --> 2922.60]  You got me thinking.
[2923.06 --> 2929.14]  And now that we're talking about workflow and testing and getting those agents working, we're going to have to come back to this topic.
[2929.26 --> 2931.24]  I'm going to have to bring something, though, to discuss.
[2931.92 --> 2936.46]  Yeah, we'll come up with some agent ideas and maybe maybe work through the testing of those.
[2936.60 --> 2937.02]  I like that.
[2937.24 --> 2937.78]  Sounds good.
[2937.98 --> 2940.28]  OK, thanks a lot for the insights today.
[2940.50 --> 2941.36]  Yeah, thanks, Chris.
[2941.36 --> 2947.72]  Hope you have a good rest of the day and we'll swap places geographically next week.
[2948.02 --> 2948.56]  There you go.
[2948.58 --> 2950.06]  Work our way towards Tofurby.
[2950.48 --> 2951.24]  That's perfect.
[2951.44 --> 2952.28]  Sounds like a November.
[2952.28 --> 2960.64]  All right.
[2960.94 --> 2962.82]  That is our show for this week.
[2963.18 --> 2969.12]  If you haven't checked out our ChangeLog newsletter, head to changelog.com slash news.
[2969.36 --> 2971.60]  There you'll find 29 reasons.
[2971.82 --> 2975.02]  Yes, 29 reasons why you should subscribe.
[2975.46 --> 2977.02]  I'll tell you reason number 17.
[2977.60 --> 2980.36]  You might actually start looking forward to Mondays.
[2980.36 --> 2983.24]  Sounds like somebody's got a case of the Mondays.
[2983.64 --> 2988.20]  28 more reasons are waiting for you at changelog.com slash news.
[2988.40 --> 2994.10]  Thanks again to our partners at Fly.io to Breakmaster Cylinder for the beats and to you for listening.
[2994.52 --> 2997.14]  That is all for now, but we'll talk to you again next time.
