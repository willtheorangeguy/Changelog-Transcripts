[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.72 --> 20.34]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 --> 25.10]  And we're excited to share they now offer dedicated virtual droplets.
[25.10 --> 29.04]  And unlike standard droplets, which use shared virtual CPU threads,
[29.04 --> 32.88]  their two performance plans, general purpose and CPU optimized,
[33.40 --> 36.08]  they have dedicated virtual CPU threads.
[36.42 --> 40.86]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 --> 45.20]  So if you have build boxes, CICD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.22 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.14 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 --> 88.56]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.46 --> 102.28]  And now onto the show.
[106.82 --> 111.72]  Welcome to another fully connected episode of Practical AI.
[112.24 --> 119.58]  In these episodes, Chris, my co-host, and I keep you fully connected with everything that's happening in the AI community.
[119.58 --> 128.40]  We'll take some time to discuss the latest AI news, and we'll dig into some learning resources to help you level up your machine learning game.
[128.84 --> 130.66]  So I'm Daniel Whitenack.
[130.76 --> 135.64]  I'm a data scientist with SIL International, and I'm joined by my co-host, Chris Benson,
[135.90 --> 140.42]  who's a chief strategist for AI and high performance computing at Lockheed Martin.
[140.78 --> 141.66]  How you doing, Chris?
[141.86 --> 142.42]  Doing great.
[142.46 --> 143.36]  How's it going today, Daniel?
[143.36 --> 144.98]  It's going good.
[145.10 --> 146.20]  No complaints.
[147.12 --> 156.98]  I was dealing with some CUDA version issues for a couple days, and that is in the past, so all is looking up.
[157.58 --> 158.20]  What about you?
[158.38 --> 160.80]  Well, doing similar stuff.
[161.02 --> 163.62]  I moved into a different position at Lockheed Martin.
[163.62 --> 173.28]  My boss became the chief data officer of the company, and so we're doing all sorts of cool stuff at work, and that's taking my time.
[173.82 --> 174.10]  Awesome.
[174.28 --> 175.00]  Sounds exciting.
[175.56 --> 186.98]  Well, I know we're kind of moving into summer, and I would consider kind of summer and into the fall the really heavy part of conference season.
[186.98 --> 194.10]  So I know I've been trying to figure out what I want to put on my schedule, where I want to be, what I'm involved with.
[194.62 --> 198.02]  And I know you're pretty involved in the conference circuit as well, right?
[198.32 --> 198.88]  I am.
[200.10 --> 206.24]  When we decided this was what we were going to do, I went back and looked, and I think I gave about 20 talks last year.
[207.20 --> 209.02]  Yeah, that's a lot.
[209.16 --> 212.30]  I've scaled back probably from that level.
[212.30 --> 217.78]  So I'm probably involved in a handful of conferences each year now.
[218.32 --> 219.96]  I've scaled back this year as well.
[220.08 --> 223.66]  It was getting to be a bit of a burden, a little bit too much there.
[224.10 --> 224.66]  Yeah, yeah.
[224.72 --> 236.66]  It can be too much, but since we're kind of going into conference season, what I was thinking was, you know, we've talked about a lot of technical subjects on the podcast.
[236.66 --> 244.02]  So whether that be certain types of neural nets, we've also talked about kind of overviews of infrastructure and other things.
[244.52 --> 251.08]  But we haven't really talked about, you know, what types of events happen in the AI community.
[251.08 --> 254.62]  And by events, I mean, like conferences, meetups, and things like that.
[254.62 --> 265.28]  But if you're in the AI community, how you choose which conference to go to, there's a lot of, you know, kind of hyped conferences out there.
[265.34 --> 267.10]  How do you know what's going to be valuable for you?
[267.48 --> 273.76]  And how do you get involved in these things in terms of speaking and other sorts of involvement?
[273.76 --> 280.40]  So I thought it'd be good to kind of just go around and see what your thoughts are on those subjects, Chris.
[280.60 --> 287.20]  And maybe we can kind of parse through some of this world of AI events.
[287.28 --> 287.90]  Does that sound okay?
[288.10 --> 288.98]  Sounds good to me.
[289.34 --> 289.66]  Awesome.
[289.82 --> 292.04]  Well, I'd be kind of interested.
[292.66 --> 299.22]  I'm sure our listeners would too in kind of how you went from maybe, I'm assuming at some point in your life,
[299.22 --> 305.06]  you were not giving 20 talks per year or being involved in 20 conferences.
[305.34 --> 309.60]  So kind of what does your background look like on that front?
[309.66 --> 313.02]  And how did you kind of ramp up into that just generally?
[313.74 --> 317.72]  So for me, I've done talks on and off over the years.
[317.72 --> 322.42]  But actually, as I turn toward this, I'm going to point right back at you.
[322.64 --> 325.04]  And this is something obviously you know.
[325.04 --> 331.54]  But I turned to you as I was thinking about doing some talks here and got some great advice from you.
[332.06 --> 335.32]  And then you kind of steered me into how to do it.
[335.38 --> 336.46]  And that was very welcome.
[336.60 --> 338.08]  I've used that over and over again.
[338.24 --> 347.28]  And then I kind of dived right into it and kind of built, did some stuff and kept building upon it and did a little more and building upon it.
[347.28 --> 355.58]  And after you get a little bit of experience, even if you're starting from nothing, you quickly kind of learn how to do it.
[355.84 --> 359.42]  And we'll talk about a lot of that today and kind of dive in.
[359.48 --> 364.28]  I started with meetups and moved up to doing conference talks and then eventually keynotes.
[365.14 --> 368.64]  And they all have a distinct flavor all themselves.
[369.48 --> 370.12]  Yeah, definitely.
[370.12 --> 375.24]  For me, I came originally from academia.
[375.66 --> 382.48]  And the expectation there is probably that you're going to be doing some teaching and research talks and that sort of thing.
[382.66 --> 384.06]  So I did a little bit of that.
[384.98 --> 390.76]  That sort of world is very different from a lot of events in tech.
[391.10 --> 396.92]  Maybe not so much like some of the AI events that we'll talk about here in a bit.
[397.72 --> 399.42]  So I got familiar with that.
[399.42 --> 404.26]  I actually really enjoyed teaching when I did that when I was a grad student.
[404.52 --> 411.20]  So I think I always had a desire to kind of be involved in community and teaching in some way.
[411.76 --> 421.70]  I do remember when I made my first step to giving a talk at a tech conference, which was very sort of new thing to me outside of academia.
[421.70 --> 431.72]  I was pretty terrified because I really had no idea what, you know, what it would be like, what sort of thing I should present and all of that.
[432.04 --> 436.16]  So, yeah, it can be kind of a rocky road if you're getting into it.
[436.16 --> 439.62]  So hopefully we can clarify some of that road today.
[439.72 --> 452.40]  And also, even if people aren't wanting to get involved in a speaking context, at least try to figure out, you know, what are the sorts of events that are going on in the AI world and what might bring value to them in other ways.
[452.40 --> 467.16]  So on that front, let's kind of talk through the kind of general categories of AI related events and community things that are out there for people to get involved with.
[467.24 --> 470.24]  So you mentioned, I think a first one is meetups.
[470.34 --> 472.96]  You mentioned you kind of got started getting involved in meetups.
[472.96 --> 481.80]  So could you kind of describe maybe for people that haven't ever been to a local meetup what that is, what you mean by that?
[482.14 --> 484.18]  Sure. So it is there.
[484.50 --> 485.80]  It kind of originated.
[486.04 --> 492.08]  There's a site called meetup.com that is one of it's probably the most prominent organization site, but there are others as well.
[492.58 --> 496.04]  But it kind of became a thing unto itself as a term.
[496.12 --> 500.36]  It's essentially just a local gathering of people who care about a particular topic.
[500.50 --> 501.82]  It's super casual.
[501.82 --> 504.84]  There's different things you can do.
[504.94 --> 513.46]  You may have a speaker or a group of speakers in a row, each doing short form kind of talks, or you may just have group conversations and things.
[513.54 --> 517.24]  And I've done a little bit of all that, including things having nothing to do with technology.
[518.04 --> 525.42]  Just as an incidental side thing, I happen to be a vegan and I go to vegan meetups and we explore different food and stuff.
[525.42 --> 526.96]  So it's not a tech thing strictly.
[527.14 --> 533.40]  But in this context, I had been to a bunch of different meetups in the Atlanta area, which is where I'm at.
[533.82 --> 543.68]  And I decided that there wasn't really a great meetup out there addressing AI and in particular deep learning, which was what I was most interested in.
[543.68 --> 551.80]  And so I had been to some and then I just took a wild stab in the dark and I set up a meetup for deep learning called the Atlanta deep learning meetup.
[552.38 --> 558.70]  And since I didn't, you know, first time, I just made myself the speaker with an intro to deep learning content.
[558.70 --> 561.88]  And I put it out there and I had no idea if anybody would show up.
[562.42 --> 571.66]  And I was pretty amazed that even coming into a cold and having no experience, a whole bunch of people showed up and it's gone ever since then.
[571.78 --> 577.94]  And so, you know, that's I'm always telling people, people, I say, are afraid of speaking or getting involved.
[577.94 --> 582.28]  And I say, just go to your local meetup and just offer to do something.
[582.28 --> 591.38]  And if you have no if you have an interest in a topic, but you don't actually know it, a great way to learn it is to promise in a month or two that you'll do a short talk on it.
[591.64 --> 600.58]  And even if you know nothing today, it puts the pressure on you to go learn it in that time and then show up and casually give a few minutes talk on that topic.
[600.58 --> 610.14]  It's a thing. There just really isn't a better way to learn, in my view, you know, because if you if you have to force yourself to learn well enough to teach, then you're you're going to at least understand the topic at a basic level.
[610.14 --> 613.90]  I think you draw out some probably some important points there.
[614.00 --> 619.58]  So a meetup, as opposed to a lot of other conferences, is generally like a grassroots sort of thing.
[619.58 --> 624.06]  Like you you saw that there wasn't a deep learning meetup in Atlanta, so you created one.
[624.12 --> 626.74]  So there's just kind of people creating these.
[626.86 --> 630.56]  And so you will find kind of a good bit of variability in these.
[630.62 --> 632.68]  Some are really small. Some are a lot larger.
[633.32 --> 637.16]  Some are very structured. Some are very unstructured.
[637.16 --> 641.98]  And and some, you know, have free food.
[642.08 --> 647.74]  Some don't. You'll find, you know, I think it's one of those things you have to be a little bit persistent with.
[647.74 --> 660.46]  If you're not starting your own meetup, then if you go to one and you don't like it so much, be persistent because, you know, some I would say about, you know, maybe half in my experience of meetups.
[660.46 --> 668.36]  It's kind of like you go and everybody seems like they're just there, just there for free pizza and they're not really interested in the topic.
[668.36 --> 674.86]  But then about half of them, people are really interested and really engaged and great discussions, great talks, great content.
[675.32 --> 677.22]  So don't give up after that first one.
[677.30 --> 678.78]  If you don't like it, find another one.
[678.78 --> 686.64]  There's there's a lot of different subjects around which meetups are organized.
[686.64 --> 690.70]  So some of those are around certain technologies like TensorFlow or PyTorch.
[691.16 --> 706.40]  Some of those are around certain topics like deep learning or maybe like geospatial data or, you know, other types of data, you know, distributed computing, a lot, lots of other things.
[706.40 --> 712.32]  So go to meetup.com, you know, start typing in what you what you're interested in.
[712.52 --> 721.04]  And I'm guessing if you're in a fairly populated area, there'll be something near you that that you might want to might want to attend.
[721.12 --> 724.62]  But I think this is a like you said, it's a great first step.
[724.92 --> 729.62]  If you're just getting involved in community sorts of things, go ahead.
[729.76 --> 735.02]  And, you know, even if you're not prepared to to really take a leadership role, just get involved in the community.
[735.02 --> 742.84]  Go there, meet some people, talk to people and start making some connections and volunteer even for small things.
[742.84 --> 746.78]  It makes a difference and it opens the door to meeting new people.
[747.10 --> 754.00]  And that's probably as important as any of the topics you're going to hear is meeting other people that are interested in that and forming those relationships.
[754.74 --> 754.98]  For sure.
[754.98 --> 759.22]  So there's also in addition to meetups.
[759.54 --> 769.88]  So these sort of grassroots thing in the AI community, there are a series, actually a lot now, a lot of large conferences.
[769.88 --> 778.14]  And a first group of these sort of larger conferences, I would kind of think of as large industry conferences.
[779.46 --> 787.48]  So here in a second, we'll talk about large research conferences, but there are large industry conferences.
[788.30 --> 791.74]  And I think you're probably familiar with this distinction as well.
[791.80 --> 794.50]  Chris, could you kind of give your thoughts on that?
[794.50 --> 800.42]  Yeah, and there's a level of structure that you're going to find at a large conference compared to a smaller one.
[800.52 --> 802.70]  And, you know, we can talk a little bit about both.
[802.82 --> 807.98]  But at a large conference, they're going to have a very organized way and deadlines to submit your talks.
[808.54 --> 815.40]  And they're going to have a panel, typically, of people that are going through if you're speaking or setting up various tracks.
[815.40 --> 820.42]  So they will attract, you know, hundreds or thousands of people to them.
[820.78 --> 829.20]  And, you know, so something large like, you know, I know well the O'Reilly conferences like O'Reilly AI and Strata and such.
[829.32 --> 831.76]  And those are, they'll have multiple tracks.
[831.88 --> 833.54]  And so you're not going to see everything.
[833.68 --> 837.26]  You're going to see a very small percentage, but it's very structured.
[837.26 --> 841.86]  And we'll talk a little bit about kind of strategy on getting the most out of that as we go.
[842.00 --> 852.18]  But if you contrast that with smaller ones, you may be invited to speak or invited to a keynote, that kind of thing.
[852.28 --> 857.10]  So it's the amount of structure and the amount of formality around it, the larger it gets.
[857.78 --> 857.90]  Yep.
[857.90 --> 869.22]  And I think that these, you know, conferences like you mentioned, so like O'Reilly AI, Strata, QCon, Spark Summit, MLConf, Applied Machine Learning Days.
[869.54 --> 870.64]  There's a whole bunch.
[871.18 --> 874.18]  And we won't attempt to list out all of them on this podcast.
[874.18 --> 900.42]  But this, you'll kind of get a sense of these conferences being places where people from larger companies and also people from startups as well, but mostly people from industry, are really presenting about their kind of applications of AI and their kind of unique infrastructure around AI, how they used AI to solve certain problems.
[900.42 --> 913.28]  And so it's, I would say, more tech and application focused in the industry context, which is different from some other things that we'll talk about here in a second.
[913.92 --> 914.00]  Yeah.
[914.20 --> 921.84]  Another thing, it might potentially be a downside in some of the larger ones is you'll also see a lot more commercialization these days.
[922.38 --> 922.54]  Yeah.
[922.58 --> 924.02]  Some of them are expensive, too.
[924.26 --> 924.50]  Yeah.
[924.54 --> 925.52]  They can be very expensive.
[925.52 --> 936.92]  And you really have to pick and choose what you want to because there are talks that they will, there may be a technical topic, but it's really about what a particular company is doing very specifically.
[937.16 --> 939.54]  And it's kind of, there's a little bit of branding around it.
[939.66 --> 945.56]  So I've gotten very particular in how I choose to spend my time at the larger ones.
[946.14 --> 946.30]  Yeah.
[946.44 --> 946.60]  Yeah.
[946.70 --> 953.26]  In some cases, you'll see kind of sales pitchy talks.
[953.26 --> 959.74]  But I would say there are good, large industry conferences where the content is really good.
[960.14 --> 964.52]  I think you just, like you said, you have to be aware that, you know, that that's a possibility.
[964.82 --> 965.72]  Could be the situation.
[966.26 --> 966.44]  Yeah.
[966.44 --> 966.48]  Yeah.
[967.48 --> 981.68]  I think that one, one trend that I've been seeing, which is kind of another category of industry conferences or events is kind of like smaller topical or specific.
[982.80 --> 988.10]  So topical events or events focused on particular tool sets.
[988.10 --> 988.62]  Mm-hmm.
[988.66 --> 996.06]  I've seen a lot of these pop up lately for, you know, there have already been the TensorFlow Dev Summit and PyTorch Developers Conference.
[996.06 --> 1003.26]  But I've seen things recently pop up around certain languages, of course, like the R conferences.
[1003.78 --> 1008.86]  But there's also like a Spacey Conference called IRL or In Real Life.
[1009.82 --> 1013.50]  I recently saw announced an Allen NLP Summit.
[1013.50 --> 1019.40]  There's a lot of different kind of events that are smaller.
[1019.56 --> 1023.08]  So it might be like, you know, 50 or 100 people there.
[1023.40 --> 1029.14]  But it's the 50 or 100 people that are really, really interested and in the weeds with Spacey.
[1029.14 --> 1041.76]  And so if you're that type of person that is really like into a particular topic or tool set, and that's like kind of where you live and do most of your work, that could be the most valuable thing for you.
[1041.76 --> 1061.56]  Instead of spending, you know, $2,000 or $3,000 to go to a large industry conference where there's very broad presentation of content, it might be better to just, you know, go to a place where you're going to be able to focus and hear a lot of content about the specific topic or tool set that you're focused on.
[1061.56 --> 1062.56]  Totally agree.
[1062.56 --> 1073.10]  And there's another niche that I've seen small conferences do is that there's kind of the space between where a meetup is and where a full large conference is.
[1073.22 --> 1082.12]  And I've seen it kind of as an intermediary thing to where you might have a meetup or user group that is meeting on a monthly basis in a meetup context.
[1082.12 --> 1090.00]  But then once a year, they will try to put on a larger event that still caters to their community and bring in external people and such.
[1090.34 --> 1093.66]  And so that's – I've gone to several of those.
[1094.20 --> 1096.10]  Data PsyCon in Atlanta is one.
[1097.36 --> 1101.62]  Applied Artificial Intelligence Conference in London a few months ago was another one.
[1102.20 --> 1105.12]  And, you know, it's not the massive scope.
[1105.12 --> 1113.22]  I even saw – there was a really good one that I went to that was actually put on by a group of college students at Vanderbilt called Emerge.
[1113.74 --> 1122.52]  And it particularly impressed me because it was the – they weren't – these were young adults that were not really out into industry yet.
[1122.58 --> 1125.30]  They were still taking classes, but they managed to come together and do it.
[1125.42 --> 1128.80]  And so – and it turned out to be a fantastic conference.
[1129.00 --> 1131.62]  So I've really gotten to where I like those in-between levels.
[1131.62 --> 1141.64]  They're large enough to get more than you're going to get out of a meetup, but yet they're still small enough to where you actually meet most of the people there and have a great chance to network locally.
[1142.20 --> 1142.78]  Yeah, definitely.
[1143.26 --> 1155.96]  So the last category that I think I would put on my categories of events when I'm thinking about events to get involved with or research is actual AI research conferences.
[1155.96 --> 1166.26]  So there's a set of events that are really geared towards original AI research.
[1166.26 --> 1175.66]  So this is a lot of people from academia, so from universities, but also people from industry that are from like R&D departments and other places.
[1175.66 --> 1187.34]  And places like OpenAI or maybe Hugging Face and other places that are really pushing the boundaries of what people have done with AI before.
[1187.34 --> 1207.14]  So it might be people that have a new kind of large-scale language model or people that are doing some sort of very interesting unsupervised video methods or something like that that people really haven't done in this way before.
[1207.14 --> 1219.82]  So a lot of times those things are presented at conferences like NeurIPS or EMNLP or ICLR or CVPR.
[1220.70 --> 1225.30]  So these are all kind of very big mainstream AI research conferences.
[1225.92 --> 1231.70]  A lot of times they sell out all of their tickets.
[1232.38 --> 1234.78]  You might not even get a place there.
[1234.78 --> 1238.78]  It's also kind of a high barrier to get something submitted to those.
[1239.12 --> 1242.74]  At the same time, like the things that are presented there are just mind-blowing.
[1242.98 --> 1245.44]  So it's not worth totally writing those things off.
[1246.14 --> 1252.28]  And if you want to kind of go down that research path, there's definitely chances to get involved there.
[1252.78 --> 1256.14]  Yeah, the topics are very, very advanced.
[1256.50 --> 1259.50]  And they're probably not for a general audience.
[1259.50 --> 1266.46]  You really have to already be at some level of expertise in the field to get meaningful stuff out of that.
[1266.64 --> 1276.52]  But that's also where you'll find all the big researchers around the world in the various organizations, whether it be OpenAI, Google, Microsoft, you name it.
[1276.66 --> 1277.30]  They're there.
[1277.30 --> 1284.50]  So it's a totally different type of thing than, say, one of the standard large industry like O'Reilly's and such.
[1284.50 --> 1294.20]  This episode is brought to you by StrongDM.
[1294.46 --> 1302.80]  StrongDM makes it easy for DevOps to enforce the controls InfoSec teams require, manage access to any database, server, and any environment.
[1303.28 --> 1306.80]  And in this segment, we're talking to Jim Mortco, VP of Engineering at Hearst.
[1306.80 --> 1311.40]  He's sharing how they're using StrongDM within their team of 90-plus engineers.
[1311.82 --> 1316.68]  It now takes them just 60 seconds to off-board a team member from a data source.
[1316.88 --> 1320.52]  We have an engineering team of somewhere in the area of 80 or 90 engineers.
[1320.78 --> 1327.64]  Because we've got so many services and many databases and so many developers, we need a reasonable way to manage access to them.
[1327.94 --> 1331.68]  It was a somewhat painful and labor-intensive process.
[1331.68 --> 1338.08]  Our DevOps team would literally have to manage every one of the permissions for everybody who wanted access.
[1338.86 --> 1341.72]  So StrongDM has been a real godsend in that area for us.
[1342.08 --> 1345.58]  Requests for access to specific databases were pretty much manual.
[1345.76 --> 1347.16]  Now we've adopted StrongDM.
[1347.36 --> 1349.36]  It's something that you don't even know is there.
[1349.50 --> 1350.94]  Once it's installed, it just works.
[1351.02 --> 1351.62]  It's very simple.
[1351.96 --> 1357.92]  We've set up a multitude of data sources so that when somebody's onboarded, we just give them access to StrongDM.
[1358.20 --> 1359.02]  It's pretty simple.
[1359.02 --> 1365.60]  Our DevOps team, they have a very minimal effort required to enable each data source to be connected to StrongDM.
[1365.82 --> 1369.54]  And then installing the client software is very, very simple and straightforward.
[1369.78 --> 1372.14]  You can use whatever client you want to to talk to the database.
[1372.28 --> 1373.72]  So there's really no training necessary.
[1374.22 --> 1374.52]  All right.
[1374.54 --> 1380.16]  If your team can benefit from nearly instant onboarding and off-boarding that's fully SOC2 compliant,
[1380.48 --> 1384.08]  head to StrongDM.com to learn more and request a free demo.
[1384.40 --> 1386.44]  Again, StrongDM.com.
[1389.02 --> 1400.52]  All right, Chris.
[1400.62 --> 1409.76]  So now that we have our kind of general categories of conferences, we've got research conferences and smaller topical or focused conferences.
[1409.76 --> 1412.04]  We've got larger industry conferences.
[1412.04 --> 1413.04]  We've got meetups.
[1413.76 --> 1430.14]  In your opinion, maybe we should kind of where we should go next is talking about our opinions on why we should or why we participate in these sorts of events and maybe why we would recommend other people participating in these.
[1430.20 --> 1430.96]  What are your thoughts there?
[1430.96 --> 1432.90]  It's interesting.
[1433.32 --> 1442.26]  Something I noticed both about myself and other people that I've talked to, when people are first starting to go to conferences, they tend to say, I'm going to go and I'm going to listen to all the talks.
[1442.40 --> 1445.08]  You know, they want to get their money's worth and sit through.
[1445.08 --> 1454.86]  But after you've been to some, you start, like I alluded to earlier, kind of picking and choosing and figuring out where you're going to get the biggest bang for the time that you're spending there.
[1454.86 --> 1460.24]  And so I know for me, there are a couple of different areas.
[1460.72 --> 1470.02]  And one, obviously, is that you is that at during that conference, you have a concentration of expertise about, you know, the topics that the conference covers.
[1470.02 --> 1479.38]  And so if you are doing work in a particular area or interested in a particular area, it's a great way to try to accelerate your learning process.
[1480.10 --> 1491.64]  And the way that I do that, at least, is I differentiate what can I get done on my own when I'm not at the conference versus what do I do with all these experts around that I have access to.
[1491.64 --> 1515.12]  And so I will try to pick and choose the issues and I will try to connect with people so that if I'm having trouble finding answers or how to get started on something in a certain area or maybe I've run into a difficult problem that's not well documented, that's a fantastic kind of thing where you can go up to people who have been there and done that and quickly get through those hurdles.
[1515.12 --> 1524.96]  And so that is one way. That's one of the parameters that I'll use when I am trying to figure out what talks I'm going to go to and what people I want to meet.
[1525.64 --> 1541.04]  Yeah, I think that particularly the larger industry conferences, you can kind of go into them and say, you know, instead of saying I'm going to just try to consume as much material as I can, you can be very, like you said, very targeted.
[1541.04 --> 1556.70]  So I remember going to a couple of conferences, you know, it was probably a couple of years ago now when I was thinking about the best way to run TensorFlow distributed in Docker containers.
[1557.12 --> 1559.72]  Is that possible? Are people doing that?
[1560.24 --> 1565.10]  What are best practices for utilizing GPUs when you're using Docker containers?
[1565.10 --> 1575.46]  And that might sound kind of focused, but at a larger industry conference, there were a ton of people there that were first of all using TensorFlow.
[1576.50 --> 1580.82]  Second of all, doing some sort of deploys involving Docker.
[1580.82 --> 1588.92]  There were a bunch of people there involved in GPU stuff and maybe people from NVIDIA.
[1588.92 --> 1595.68]  And so what I could do like at that time is just say, OK, who are all those sorts of people?
[1595.92 --> 1598.76]  Let me go to their talk, which is probably interesting anyway.
[1599.30 --> 1611.72]  But let me go up to them afterwards and kind of, you know, hear more about their talk, but also pick their brain on some of these things, discuss some of these topics, how they're doing certain things, what recommendations they would have.
[1612.12 --> 1616.72]  And so it's really a shortcut to very concentrated information, like you were saying.
[1617.32 --> 1617.82]  Yeah, totally.
[1617.82 --> 1625.00]  It's it's it's I use it to accelerate things and it kind of leads to the next thing that I wanted to mention.
[1625.10 --> 1627.68]  And that is a big part of conferences is networking.
[1627.68 --> 1628.94]  It's getting to know people.
[1628.94 --> 1629.80]  It's part of this.
[1629.86 --> 1637.36]  So, you know, you you kind of you may think I want to solve the problem that's been bugging me that I've spent the last two weeks trying to figure out how to deal with and I'm struggling with it.
[1637.64 --> 1643.96]  And you start with that, but then you get to know and you may keep up with people thereafter and start building relationships.
[1643.96 --> 1653.50]  And and over time, in a lot of ways, that becomes even more dominant than access to the expertise itself is having those relationships.
[1653.50 --> 1659.74]  It kind of enriches what you're doing, you know, your professional life and developing friendships and stuff.
[1659.74 --> 1689.74] 
[1689.74 --> 1694.06]  So those kinds of friendships that you you will meet people and see them over and over again.
[1694.70 --> 1705.92]  And I have I have quite a few good friendships that I that I have started at conferences of people that I've met and then we just kept up with and then periodically we'll see each other at these events.
[1706.56 --> 1709.88]  And I can't tell you how much value and enrichment I've gotten out of that.
[1709.88 --> 1722.88]  Yeah. And I think that that networking is really great for building those relationships and also just in general kind of making your life a little bit more productive.
[1722.88 --> 1728.28]  I know now I I've been working on distributed teams or as a remote worker for.
[1729.78 --> 1731.82]  Well, I'd have to count up now.
[1731.92 --> 1733.86]  It's probably at least three or four years.
[1733.86 --> 1734.30]  I forget.
[1734.30 --> 1741.84]  But but a lot of times the places where I meet with my distributed team is at conferences.
[1741.84 --> 1749.42]  So if there's a conference we're interested in, why don't we all meet there so we can both attend talks, but also have some kind of in-person time.
[1749.42 --> 1751.62]  So there's that useful bit.
[1751.62 --> 1757.52]  But also if you're involved, I mean, the AI community now is really driven by open source.
[1757.52 --> 1773.66]  So, you know, whether it be TensorFlow, PyTorch, the Onyx project, you know, things related to NVIDIA, things Microsoft is putting out, Spacey, all of these different, you know, sets of tools that are that are really driven by open source.
[1773.96 --> 1782.30]  And, you know, if you're working in AI very long, you're going to at the very minimum start using open source projects very heavily.
[1782.96 --> 1787.28]  But ideally, you'll also start contributing and being a part of those communities.
[1787.52 --> 1794.00]  Maybe you're a part of, you know, special interest groups for open source community or you're opening issues.
[1794.50 --> 1799.36]  Hopefully you're submitting PRs and that sort of thing, pull requests.
[1799.96 --> 1807.62]  And I know there have been so many instances when I've been involved in projects where, you know, I've submitted PRs.
[1807.86 --> 1810.80]  I've talked to people on Slack online or in forums.
[1810.80 --> 1820.74]  And, you know, and then I see them at conferences and it's both great to kind of put a face to that person and have empathy for them and an interaction with them.
[1820.74 --> 1833.00]  But also, you know, discuss those things like, hey, this is really what I was getting at with with this proposal or what I was thinking would be awesome to have in this module or or whatever it is.
[1833.00 --> 1840.74]  But they can also, you know, really help you and accelerate that side of your life as well.
[1840.74 --> 1851.38]  Absolutely. It's I know, like when I was at NVIDIA GTC a couple of months ago, we probably spent I work for Lockheed Martin.
[1851.50 --> 1862.14]  We probably spent as much time with a bunch of us that had come in for the conference doing Lockheed specific stuff off to the side and getting FaceTime instead of it just being, you know, conference calls and such.
[1862.14 --> 1877.20]  So that was great. And really, I think when you when you get to that point and you have, you know, the expertise available, you have the networking side of things, and then you have this this capability of getting other things done.
[1877.20 --> 1884.82]  And you really start to plan your time out in terms of how you're going to get the biggest effect, you know, for the time spent at the conference.
[1884.82 --> 1893.06]  So and I find that personally doing that, I get a lot more out of every conference than just going and just planning to sit through just talks or something.
[1893.06 --> 1907.88]  It's at this point, I'll get to the end of a conference and and it's always about, you know, did I get the most out of each out of every time spent, considering that any given hour of the day, there might be multiple options of things I would otherwise like to do.
[1907.88 --> 1923.36]  Yep, definitely. So let's so now we've kind of got our categories of of AI events, we've got some of our opinions about why we are interested in being involved in community events, whether that be conferences or meetups.
[1924.18 --> 1937.52]  Let's talk a little bit now about, you know, maybe there's listeners out there that are wanting to get involved in events and in one way or another, you know, what, what are some ways that they can jump in?
[1937.52 --> 1947.40]  And and and get involved. So, you know, I think depending on your personality and your particular interests, there's a lot of different ways to get involved.
[1947.40 --> 1954.08]  There's, of course, opportunities to give talks at events and and meetups.
[1954.88 --> 1967.40]  And those talks could just be anything from a lightning talk, which if you're not familiar with a lightning talk is, generally, that's like five to 10 minutes all the way up to like track talks and keynote talks that are maybe
[1967.40 --> 1973.18]  a little bit more high, high profile. Of course, there's ways to submit original research like we talked about.
[1973.74 --> 1981.18]  There's also ways to kind of mentor and help communities organize so you can volunteer to help,
[1981.28 --> 1985.52]  you know, at events, providing certain services,
[1987.52 --> 1992.06]  volunteering, you know, making the conference safe and accessible.
[1992.06 --> 1997.84]  There's also ways that you can help contribute by teaching.
[1998.04 --> 2004.00]  Maybe it's a workshop. You have expertise in a certain area that you'd like to kind of get out to the wider community.
[2004.00 --> 2008.88]  So there's also opportunities for for teaching and and and workshops.
[2008.88 --> 2016.06]  So depending on what of those things you're interested in, you might have to jump through certain hoops.
[2016.06 --> 2022.64]  But when you're thinking about these sort of different routes to to participation,
[2023.44 --> 2028.84]  what what do you think is some of the best ways to get started along that that route, Chris?
[2029.56 --> 2037.10]  Well, it kind of depends on where you're at the, you know, starting if you're just getting started in the field and you want to be able to go to conferences
[2037.10 --> 2039.74]  and maybe you're a college student and don't have budget.
[2039.74 --> 2046.68]  But you mentioned volunteering and that's huge. There are so many volunteer opportunities that people can do and start working their way in.
[2047.24 --> 2051.30]  And then, you know, you can get a pass because you're part of the staff there.
[2051.38 --> 2058.50]  You might manage a room. There's there's lots of different things that that you can offer up that the conference is going to need.
[2058.92 --> 2063.32]  And it's a good way of not only getting involved when you may not have the budget for it,
[2063.32 --> 2069.64]  but it's a good way of getting access to people, you know, and and and working your way in and kind of becoming part of the scene.
[2069.72 --> 2074.34]  And that's certainly something that I found is after I started getting involved in conferences,
[2074.34 --> 2079.16]  it tends to build on itself and you actually will develop a little bit of a reputation.
[2079.22 --> 2087.14]  I don't mean in terms of being famous, but in terms of within the conference community, people say, oh, you know, I I know that Chris or I know Daniel,
[2087.42 --> 2089.80]  you know, can can help us on that. They've done this in the past.
[2089.80 --> 2094.10]  They might be interested in and they'll they'll reach out to you and ask you if you want to do things and stuff.
[2094.18 --> 2096.84]  So that that's a good way of getting involved initially.
[2097.02 --> 2099.32]  How about yourself? What have you what have you seen there?
[2099.94 --> 2110.24]  Yeah, I think that, you know, in my mind, a kind of good general scaffolding or a roadmap to think about if you're if you're kind of new into the community,
[2110.24 --> 2115.98]  wanting to get involved is like we've already talked about get involved locally first at a local meetup,
[2115.98 --> 2118.60]  ask to give a talk, ask to help volunteer.
[2118.60 --> 2124.42]  And as you do that, you'll kind of find out where you're interested in being involved,
[2124.48 --> 2131.20]  whether that's speaking or on a particular topic or you have specific expertise in a certain place,
[2131.20 --> 2135.16]  like, you know, maybe it's transfer learning or maybe it's computer vision or whatever it is.
[2135.98 --> 2139.54]  And then that will kind of help you decide how you want to contribute.
[2139.54 --> 2146.86]  Once you've decided that, then go out and do some research in these different areas in the in the industry conferences,
[2146.86 --> 2149.56]  in the research conferences, in the smaller conferences.
[2150.10 --> 2154.00]  See what's coming up maybe later on down the line.
[2154.10 --> 2158.60]  Like, you know, if I'm if I'm at this point now going into summer,
[2158.60 --> 2163.20]  I might be even looking at spring of next year or into summer of next year.
[2163.20 --> 2166.48]  And what's what's further down the line that I can plan for in advance?
[2166.96 --> 2170.66]  Try to think up some ideas for talks and workshops or papers.
[2171.40 --> 2175.58]  Find out what that event that you have targeted out ahead of time.
[2175.58 --> 2177.20]  What opportunities there are?
[2177.36 --> 2178.54]  Are there talk opportunities?
[2178.54 --> 2180.30]  Are there lightning talk opportunities?
[2181.12 --> 2182.84]  Are there workshop opportunities?
[2182.84 --> 2189.56]  Document those things, you know, make sure the prices and the submission process are clear to you.
[2190.04 --> 2193.68]  And one of the biggest things that I would recommend is get get feedback.
[2193.68 --> 2201.70]  So you're already going to be involved in your local meetup and maybe you're involved online and forums or other things or open source projects.
[2202.08 --> 2210.86]  Ask some of the some of your contacts and industry to review your abstract or to listen to your talk or to review your submission.
[2210.86 --> 2218.14]  And that's that's a huge help as you're preparing to preparing to to submit.
[2218.32 --> 2234.52]  The other last thing that I'd love to mention on this front is, you know, for a lot of people, there's financial or other barriers that may kind of stifle or prevent you from participating in certain events.
[2234.52 --> 2240.58]  But I'd really encourage you if you feel like you're in that place, don't give up being be encouraged.
[2240.84 --> 2246.88]  We'd love for you to reach out to us on on our Slack team or LinkedIn page or something.
[2246.88 --> 2250.22]  So you can find us at changelog.com slash community.
[2250.22 --> 2262.86]  And there are conferences out there that are willing to give scholarships for for for minorities and for other other people coming from other communities.
[2262.86 --> 2263.84]  Maybe you're a student.
[2264.42 --> 2265.90]  Maybe you're coming from a nonprofit.
[2267.08 --> 2270.00]  There's a lot of different routes into this.
[2270.00 --> 2280.28]  So if you feel like you're having trouble finding something that fits, reach out and we would love to do our best to help connect you to those those those programs and those ideas.
[2281.74 --> 2283.64]  But there's something out there.
[2283.64 --> 2287.52]  And I'd encourage you to kind of be persistent and find that.
[2287.76 --> 2294.78]  And and hopefully you'll find a welcoming community that will really kind of help build momentum in your career.
[2300.00 --> 2305.34]  This episode is brought to you by Discover Dot Bot.
[2305.56 --> 2309.72]  Learn everything there is to know about bots at Discover Dot Bot slash Practical AI.
[2310.08 --> 2317.96]  Discover Dot Bot was built by Amazon Registry Services as an online community for bot creators and makers of all skill levels to learn from one another, to share stories.
[2317.96 --> 2328.18]  And they regularly publish guides and resources to answer questions like how to set up payments to your bot, how to stop shopping cart abandonment, what KPIs are worth measuring, how to write an engaging chat bot dialogue.
[2328.18 --> 2330.56]  You can even register Dot Bot domains there.
[2330.82 --> 2335.42]  Learn more and explore this huge library of bot resources at Discover Dot Bot slash Practical AI.
[2335.92 --> 2338.30]  Again, Discover Dot Bot slash Practical AI.
[2350.70 --> 2353.94]  Let's turn to actually what it takes to do a talk at this point.
[2354.04 --> 2357.56]  That's obviously only one of the ways to get a lot out of a conference.
[2357.56 --> 2358.98]  But or a meetup.
[2359.06 --> 2360.52]  But it's it's a big thing.
[2360.52 --> 2365.34]  And it doesn't it's not as hard as a lot of people expect it to be.
[2365.58 --> 2368.28]  There's a lot of people have fear of getting in.
[2368.34 --> 2373.20]  But honestly, you know, that's kind of everybody that's there is in the same boat.
[2373.20 --> 2381.78]  And so I I've seen people really, really blossom by deciding to to start off maybe at a meetup and give a talk.
[2381.78 --> 2384.74]  And they they do that and it works out better than they thought.
[2384.80 --> 2388.94]  And so they they decide to, hey, I'm going to try a small conference and submit.
[2389.12 --> 2392.48]  And so there's a lot that goes into those different things.
[2392.48 --> 2393.90]  And there's different types of talks.
[2393.90 --> 2401.66]  You know, we so we've talked a little bit about starting off with a small, very casual talk on a topic at a meetup.
[2401.66 --> 2416.54]  But then after you feel pretty good about that, if there's a particular topic and you feel a little bit more confident about it and you've you've spent a little bit of time working in it and you think that they that you have developed enough knowledge in that to share with people.
[2416.54 --> 2422.22]  Then I really encourage people to to go ahead and submit their first talk to a small conference.
[2423.04 --> 2429.26]  It is it's a great learning experience, a good chance that you may not get it at first.
[2429.26 --> 2436.02]  And hopefully with some of the things that we'll talk about over the next few minutes, we can talk about how you're going to increase your chances of being accepted.
[2436.78 --> 2443.50]  But if you you kind of work your way into that, you might be a lightning talk as well, which is very short in some ways.
[2444.24 --> 2445.18]  It's very different.
[2445.18 --> 2448.58]  It can be very time sensitive in terms of what you're doing.
[2449.04 --> 2454.14]  And then if you get good at it down the road, you you may find that people are inviting you to do keynotes.
[2454.44 --> 2465.00]  And so it's it's essentially working your way gradually up a kind of a natural progression of a ladder in terms of where you want to go and the types of talks that you want to give.
[2465.48 --> 2474.14]  I'd love to dive into to what you just mentioned, Chris, which is really kind of what to think about as you're preparing content.
[2474.14 --> 2478.16]  So this this may be for a track talk or all the way up to a keynote.
[2479.16 --> 2488.76]  But what what should you be thinking about, even if it's for your local meetup, what should you be thinking about as you're preparing to present some type of of content?
[2488.76 --> 2492.24]  So there's a lot of ways to go about this.
[2492.24 --> 2504.34]  One of the things that I would suggest is, you know, it's kind of like I've heard people talk about, oh, how do you, you know, how do you get started writing a book or something like that?
[2504.34 --> 2511.06]  Well, first of all, you have to, you know, read books and be familiar with with the format and all of that and what other people have done.
[2511.18 --> 2522.70]  I think it's similar here to to get familiar with, you know, what an abstract is or the format of a lot of talks and that sort of thing.
[2522.70 --> 2529.32]  Do some do some research. So go to a lot of times now for many of these conferences.
[2530.42 --> 2536.80]  Previous years talks are all online, including like the abstracts and all of those things.
[2536.80 --> 2543.70]  So one of the best ways, I think, to get started is kind of listen to some of the talks from previous years conferences.
[2543.70 --> 2548.14]  Look at some of the abstracts and look at what topics were covered.
[2548.24 --> 2550.20]  Look at the format of the abstracts.
[2550.20 --> 2560.36]  Look at the format of the talks, the pace that people are going at and kind of get a flavor for the styles of talks that that are done at a conference.
[2560.36 --> 2570.48]  And I think that can kind of, you know, not that you want to, you know, just outright copy someone's talk because that probably wouldn't get accepted anyway.
[2570.86 --> 2575.24]  But you can understand, you know, what are some good ways to format abstracts?
[2575.62 --> 2579.40]  What are some good ways to create titles for talks?
[2579.50 --> 2585.98]  What are some good ways to format your talk and kind of learn some of that from people that have doing it, been doing it for quite a while?
[2586.30 --> 2590.16]  Yeah, it's there's I have a little tie into this.
[2590.36 --> 2598.86]  As you're trying to figure out what it is that you want to talk about and how you're going to to organize your abstract so that it captures their attention.
[2599.46 --> 2608.38]  As I hope our listeners know, last week we had O'Reilly's chief scientist, chief data scientist, Ben Lorica, who was interviewed.
[2608.76 --> 2613.62]  And that was when I was at O'Reilly and off when we were not recording the interview separately.
[2614.48 --> 2617.52]  I asked him because he's the chair for the program.
[2617.52 --> 2622.98]  And I asked him, I said, you know, Ben, I've submitted talks and been accepted by O'Reilly.
[2623.14 --> 2624.76]  I've also had talks rejected.
[2625.48 --> 2627.80]  You know, what what advice would you give me?
[2627.86 --> 2629.64]  And it was just the two of us talking at this point.
[2629.64 --> 2643.38]  And he said, you know, it's amazing how many people will in their abstract will talk about the what it is they want to cover, but they don't talk about how they're solving it in the abstract.
[2643.38 --> 2648.10]  Right. And so he said it becomes a little bit too too loose.
[2648.10 --> 2650.68]  And I'm paraphrasing Ben. I'm not quoting him directly.
[2650.84 --> 2657.20]  But he said, really focus not only on the problem statement, but on how you're approaching the solution very specifically.
[2657.20 --> 2661.48]  And so that until until until I just said that that was my secret weapon.
[2661.98 --> 2664.92]  But now everybody has heard that that came straight from Ben.
[2665.38 --> 2667.42]  And that's a it was a great point.
[2667.54 --> 2673.92]  It's it's share with this share with your potential audience what problem you're trying to solve, but then talk about where you're going to go.
[2674.20 --> 2679.50]  Because you could actually have multiple talks about more or less the same thing with different types of solutions.
[2679.50 --> 2686.80]  And and and even so, those might get accepted together because they're all well thought out approaches to a given problem.
[2686.80 --> 2695.66]  So I know that for myself, I'm kind of going back through how I'm doing abstracts and being very, very solution focused in what I put out there.
[2696.24 --> 2698.52]  Yeah, I think I think you have to be specific.
[2699.00 --> 2707.98]  So, you know, if I'm thinking about submitting an abstract, let's say I'm working in machine translation for for low resource languages.
[2707.98 --> 2714.16]  If I'm thinking about that, I want to I want to grab I want to tell a story, but with specifics.
[2714.16 --> 2718.88]  So I want to grab people's attention, but not in a very general way.
[2719.00 --> 2726.86]  So the way you should not start out is like these sorts of statements like, as we know, data is the new oil or something like that.
[2726.88 --> 2732.28]  It's like everybody that that's been at these conferences and reviewed abstracts, they're tired of hearing that.
[2732.28 --> 2748.26]  What they want to hear is, you know, like like, you know, like 90 percent of the world's languages are not have no machine automatic machine translation available through Google Translate or other means.
[2748.70 --> 2760.74]  We at Company X have developed blah, blah, blah with specifics about solving this issue and, you know, really helping this target people or, you know, whatever it is.
[2760.74 --> 2764.74]  So you want to you want to be you want to grab people's attention, but be specific.
[2765.18 --> 2765.62]  Absolutely.
[2765.92 --> 2779.62]  You want to be unique and show that you have a unique way of assessing the problem and providing a solution to it so that people understand that when they come and see your talk, they're going to get something they're not going to get anywhere else.
[2779.62 --> 2787.54]  And that if you're a conference organizer, that's the reason you're looking for that is, you know, a conference is a is a is an event.
[2787.76 --> 2796.04]  It may be nonprofit oriented or commercial, but it's still something they want people to want to come to and to get a great benefit out.
[2796.04 --> 2809.92]  And if you're able to be that speaker who is going to provide the unique bit of value there, then that's going to truly, you know, grab the attention of both conference organizers and a potential audience so that people actually come to your speech.
[2810.16 --> 2810.60]  Yep.
[2810.80 --> 2815.32]  I guess, you know, maybe we should mention, too, that there's there's kind of different.
[2815.78 --> 2818.80]  Well, you've already mentioned that there's kind of different levels of talk.
[2818.80 --> 2822.16]  So a keynote talk might be a higher profile.
[2822.94 --> 2826.82]  Everybody's in the same room that's at the conference to hear this keynote talk, maybe.
[2827.40 --> 2828.90]  And then there's kind of track talk.
[2829.10 --> 2846.20]  So at maybe a larger conference, everybody together might be more than a thousand people in the room to hear a single person talk, whereas a track talk at the very same conference, it might be like 30 to 50 people in a room to hear to hear a person present.
[2846.20 --> 2860.24]  Now, most of the time, the track talk is addressing a particular, you know, like there might be a track on computer vision, or it may be even more specific than that.
[2860.30 --> 2865.30]  It might be a track on OCR, depending on the conference context.
[2865.30 --> 2868.32]  But these might be very specific tracks.
[2868.56 --> 2883.74]  And so the way that you frame your story when you're submitting to a particular track might be even more specific than it would be for for a keynote talk where you're really trying to maybe inspire and motivate and that sort of thing.
[2884.10 --> 2885.90]  I know you've done both, Chris.
[2886.00 --> 2887.28]  What's your perspective on that?
[2887.28 --> 2893.58]  I would say starting with the track talk, I would say that the larger the conference, the more specific you need to be.
[2894.30 --> 2914.00]  If you're at a very small conference, you know, and your audience are people who might just be getting into AI and machine learning, then you could potentially do a little bit less specific and talk about maybe machine vision with convolutional neural networks and provide some use cases.
[2914.00 --> 2921.36]  Because there might only be a dozen talks in the whole conference, and that's unique enough to provide that.
[2921.90 --> 2931.10]  If you go to like NVIDIA GTC, their GPU technology conference, which is a pretty big conference, you're going to be really, really specific there.
[2931.76 --> 2940.82]  It's going to have to be something where you're using CNNs in a specific use case and trying to get a specific objective.
[2940.82 --> 2942.80]  And so keep that in mind.
[2942.88 --> 2946.10]  The bigger the conference, the more specific you're going to want to be.
[2946.66 --> 2947.76]  Keynotes are a different animal.
[2948.38 --> 2954.32]  It's a larger audience, and you kind of have a job for the conference of framing the conference.
[2955.00 --> 2959.26]  And there are both opening keynotes and there are closing keynotes.
[2959.40 --> 2961.90]  And sometimes given tracks, we'll have a keynote.
[2961.90 --> 2971.04]  And so if you're going to keynote, then you really have to look at the various talks that are in a track or within the conference.
[2971.38 --> 2979.02]  And you're providing a topic that can extend out to lend themselves to those individual track speakers.
[2979.42 --> 2985.90]  So you're framing how you're starting and then a closing keynote, you're kind of framing the value they got out of it.
[2985.90 --> 2995.36]  While you're hitting a topic, but you're also trying to pull all those little track talks together and tie a bow on the end of it.
[2995.84 --> 2995.94]  Yep.
[2996.32 --> 3008.12]  And the content that you present, I would say regardless of whether it's a track talk or a keynote, there's some guidelines that I think are just generally helpful for all of these talks.
[3008.12 --> 3021.76]  And the ones that I usually keep in mind are to not assume that the audience knows very much about the subject that you're dealing with.
[3021.90 --> 3025.56]  So this is dependent on whether you're doing a track talk or a keynote.
[3025.74 --> 3036.80]  But if you're doing like a keynote at an AI conference, my general level of thought is that the audience knows maybe what AI is, but not much else.
[3036.80 --> 3048.00]  And that's where I start because you'll have a huge variance in people that are AI curious and all the way to people that are really into the weeds.
[3048.14 --> 3052.78]  But I've always found it better to err on the side of being too accessible.
[3053.10 --> 3058.78]  I've had a lot of times where I've been too detailed and I know that I've lost people.
[3058.78 --> 3069.50]  And I've had almost no times where I feel like I've been too high level or too accessible for people when I've created a talk.
[3069.58 --> 3073.44]  So I think it's better to try to err on the side of accessibility.
[3073.90 --> 3076.38]  And part of that, I think, is using pictures.
[3077.12 --> 3083.64]  And, you know, using pictures and trying to keep yourself from using too much jargon.
[3083.64 --> 3085.78]  And you're going to have to use some jargon, right?
[3085.82 --> 3098.12]  But if you're using a whole bunch of acronyms more than you really have to or other things, you know, sometimes it's better to use pictures and to not make too many assumptions.
[3098.12 --> 3101.76]  And, of course, for a track talk, maybe that's adjusted a little bit.
[3101.76 --> 3110.84]  Like if it's a track on machine translation, maybe you assume, OK, these people may have a baseline understanding of machine translation.
[3111.12 --> 3112.88]  But that's as far as I would assume.
[3113.44 --> 3118.92]  I wouldn't assume that they are even familiar with the type of machine translation that I'm going to be talking about.
[3119.02 --> 3121.18]  So I think it's better to err on that side.
[3121.72 --> 3122.88]  I completely agree with you.
[3122.94 --> 3126.30]  And if you are going to use jargon, define it along the way.
[3126.30 --> 3136.44]  Because especially these days with so many conferences having the talks on the Internet after the conference is over, you may have a large number of people.
[3136.96 --> 3142.38]  The majority of your viewers may happen after the conference is over when they're viewing it on YouTube or some other platform.
[3142.94 --> 3148.30]  And so, you know, be very conservative in what you're assuming about your audience.
[3148.30 --> 3152.38]  And there may be people who just know everything there is to know like you that are there.
[3152.38 --> 3157.10]  But there may be people, as you said, who just barely aware of the topic and they're interested in learning more.
[3157.32 --> 3164.36]  And if you don't help them through that by either not using jargon or defining it, then you're going to lose them along the way.
[3164.40 --> 3166.74]  And they're not going to get the value that you're hoping they're going to get out of it.
[3167.08 --> 3168.52]  And pictures, absolutely.
[3168.74 --> 3172.50]  I mean, this is a medium that lends itself.
[3172.64 --> 3176.24]  You're doing a talk, but you definitely.
[3176.40 --> 3180.06]  And a little bit of this is kind of is probably some of the standard stuff that we talk about.
[3180.06 --> 3183.50]  You don't want it just the same thing that you're saying.
[3183.70 --> 3185.00]  You don't want that on the screen.
[3185.08 --> 3186.70]  You certainly don't want to read off your slides.
[3187.26 --> 3194.68]  Have a picture that emphasizes what you're trying to say and is really, really focused on getting that idea across so that you you're complimenting.
[3194.74 --> 3197.36]  You have the verbal and you have the the picture.
[3197.58 --> 3201.04]  And together they help communicate what you're trying to to the audience.
[3201.04 --> 3219.74]  Yeah. And maybe we can kind of end, you know, start start to wrap up and kind of discuss one more thing, which I think is relevant even beyond the conference setting, which is the way that you present content, even if it's in your company.
[3219.74 --> 3231.90]  And I think this is relevant if you're giving an AI talk at a conference or if you're presenting your new AI driven application to stakeholders within your company.
[3232.12 --> 3241.82]  A lot of this stuff carries through like what we've already talked about, about assuming knowledge and using pictures, but also in the way that you prepare.
[3241.82 --> 3249.16]  So you've already kind of hinted at this, Chris, but in the way that you prepare, you can prevent a lot of pitfalls.
[3249.36 --> 3266.76]  So I think one of the biggest, biggest things that that people are probably making the wrong assumption about is that these keynote speakers that give really awesome and dynamic keynotes at big conferences are just naturally good at doing that.
[3266.76 --> 3275.98]  And, you know, it could be that they're used to it and it could be that they have developed some good methods, but these people practice.
[3275.98 --> 3295.24]  And the only way to present yourself as that kind of as confident and not very rambling and not very wordy, but concise and effective is to practice and know exactly what you're going to say and practice it over and over.
[3295.34 --> 3297.00]  Practice your slide transitions.
[3297.62 --> 3299.08]  Practice, practice, practice.
[3299.08 --> 3302.20]  And not only in front of yourself and not only silently.
[3302.92 --> 3304.18]  Practice out loud.
[3304.60 --> 3305.72]  Practice standing up.
[3305.98 --> 3315.26]  And I find someone, even if it's via Zoom or some remote way that you work, have someone listen to your talk and give feedback.
[3315.82 --> 3322.18]  Take note of when you are getting sort of rambling or maybe going off subject and really dial those things in.
[3322.44 --> 3327.38]  So I think, you know, people think that some people are just really good at this and others aren't.
[3327.66 --> 3330.44]  And there are people that it comes more naturally to.
[3330.44 --> 3335.98]  But for the most part, I think the people that do a good job at this put in the time to practice.
[3336.54 --> 3337.68]  I completely agree with that.
[3337.92 --> 3347.94]  One of the advantages of practicing a lot is as you go forward, it gets easier across multiple talks because you will develop a style as a speaker.
[3347.94 --> 3354.40]  And you'll come to be able to rely on your style to help understand how you're going to transition.
[3354.76 --> 3357.08]  It's not going to be your first, second, or third speech.
[3357.08 --> 3362.48]  But eventually, you kind of know how you approach a certain thing and you know how long you need and that will help.
[3362.78 --> 3363.78]  You're still going to be practicing.
[3363.78 --> 3370.62]  But it's like anything that you do a lot, you kind of have that muscle memory effect.
[3370.94 --> 3373.20]  And that will happen with giving talks as well.
[3373.88 --> 3382.42]  A couple of big gotchas that I wouldn't want to close out without mentioning are a lot of times speakers will put way too much on a given slide.
[3382.42 --> 3385.74]  All sorts of data and charts and stuff.
[3385.74 --> 3393.78]  And it is compact and the audience will be trying to figure out what each of the components on that particular visual are.
[3394.14 --> 3396.18]  And it detracts from what the speaker is saying.
[3396.54 --> 3400.04]  And so I often tell people there are two types of visuals.
[3400.46 --> 3404.56]  There are visuals for when you're speaking and there are visuals that you study when you're not speaking.
[3404.68 --> 3409.42]  That you would sit down in your office and read and try to understand and analyze.
[3409.54 --> 3410.46]  And those are very different.
[3410.46 --> 3416.68]  And so be aware of what kind of visual this is.
[3416.80 --> 3423.58]  In this case, for speaking, in my view, it's much better to separate out the points so that your audience is not confused.
[3423.80 --> 3429.54]  And then as you talk, to get to each of those slides in turn so that you can relay that.
[3430.12 --> 3431.30]  And it's a lot less clear.
[3431.92 --> 3435.92]  And the other thing that goes with that is time discipline and self-awareness as a speaker.
[3435.92 --> 3446.98]  And so a lot of people that would otherwise be really good speakers, whether it be some level of natural or maybe they've just practiced enough to get good at it.
[3447.64 --> 3448.86]  Don't start rambling.
[3449.18 --> 3455.24]  Don't get into a topic where you have side things and you let yourself be drawn into that because it chews up time.
[3455.24 --> 3457.98]  And it is not fair to your audience.
[3458.66 --> 3461.20]  So really understand where you are.
[3461.62 --> 3462.58]  Stay to your message.
[3463.32 --> 3474.80]  And always kind of know when you're supposed to be in your presentation and make sure that your sequence of slides and the things that you're saying for those lines up with where you should be time wise.
[3474.80 --> 3476.42]  Brevity is your friend.
[3477.06 --> 3477.24]  Yep.
[3477.62 --> 3479.90]  Some of the best advice I've got over time.
[3479.98 --> 3487.02]  And again, I think this really carries through, especially as we present AI information to stakeholders within our businesses.
[3487.70 --> 3491.04]  We need to be effective communicators about that.
[3491.04 --> 3506.96]  Some of the best advice I've got in terms of the things that have influenced my kind of style of content is that, you know, someone told me once that I should I should take for every slide.
[3506.96 --> 3522.80]  I should look at it and I should take out all of the like until I'm uncomfortable taking out words, I should take out as many words as I can and as much text as I can until I absolutely feel like I can't take out any more text.
[3523.00 --> 3525.76]  And then I should take out more text.
[3525.76 --> 3538.82]  So it's like that really needs to be a priority is, you know, making making that effective use of each slide.
[3538.96 --> 3551.18]  And then also, you know, I think a good thing that I do is when I'm preparing my slides, I zoom out from the slide until the slide is like pretty far away on my screen.
[3551.18 --> 3562.68]  Like if I was sitting way back at the end of the conference place or way back at the end of the conference room or whatever it is, I make it super small and then see if it's immediately clear what's on the slide.
[3562.78 --> 3564.50]  If not, I need to make things bigger.
[3564.62 --> 3567.26]  I need to remove text, all of that sort of stuff.
[3567.52 --> 3577.18]  And so this is challenging with AI sort of things where maybe you want to show this ginormous model tree or something like that.
[3577.18 --> 3600.78]  Well, that is a challenge, but you should really you should really take it this sort of challenge seriously and try to remove the urge to create, you know, a slide with this big chunk of code or this big, you know, graph that was output of TensorFlow or something.
[3601.28 --> 3606.74]  You know, resist the urge to put that on a slide because no one's going to be able to parse it anyway.
[3607.18 --> 3609.48]  So it might as well just not be on the slide.
[3610.22 --> 3614.24]  So I think that's that's some of some of my personal style.
[3614.44 --> 3619.28]  We really hope that this conversation has been useful to our listeners.
[3619.72 --> 3623.26]  It's a different sort of conversation than we've had on the podcast before.
[3623.44 --> 3624.90]  So we'd love to hear your feedback.
[3625.22 --> 3636.16]  If this sort of information is interesting to you, again, you can find out how to get in in contact with us on Slack or in LinkedIn at changelog.com slash community.
[3636.16 --> 3637.56]  Join our Slack channel.
[3637.70 --> 3646.80]  Tell us about the conferences that you're interested in, about your personal style of presenting and how that differs from ours.
[3647.26 --> 3652.12]  We're always trying to learn and we'd love to learn from from our listeners as well.
[3652.12 --> 3661.06]  So I hope this has helped everyone kind of get a sense of how to approach speaking and conferences and meetups in general.
[3661.76 --> 3672.76]  If we've given you some tips on how best to to get value out of each of these types of meetups and conferences, then we'll have we'll have done what we set out to do here.
[3672.86 --> 3673.62]  So good luck.
[3673.80 --> 3677.40]  Be bold and just get out there and do your thing.
[3677.40 --> 3680.58]  All right.
[3680.64 --> 3683.26]  Thank you for tuning into this episode of Practical AI.
[3683.52 --> 3684.98]  If you enjoyed the show, do us a favor.
[3685.10 --> 3685.68]  Go on iTunes.
[3685.80 --> 3686.50]  Give us a rating.
[3686.74 --> 3688.62]  Go in your podcast app and favorite it.
[3688.72 --> 3691.44]  If you are on Twitter or social network, share a link with a friend.
[3691.52 --> 3692.20]  Whatever you got to do.
[3692.42 --> 3693.88]  Share the show with a friend if you enjoyed it.
[3694.18 --> 3696.84]  And bandwidth for changelog is provided by Fastly.
[3696.96 --> 3698.38]  Learn more at fastly.com.
[3698.38 --> 3701.78]  And we catch our errors before our users do here at changelog because of Rollbar.
[3701.98 --> 3704.40]  Check them out at rollbar.com slash changelog.
[3704.40 --> 3709.18]  And we're hosted on Linode cloud servers at a linode.com slash changelog.
[3709.28 --> 3709.72]  Check them out.
[3709.80 --> 3710.64]  Support this show.
[3710.76 --> 3714.24]  This episode is hosted by Daniel Whitenack and Chris Benson.
[3714.66 --> 3716.72]  The music is by Breakmaster Cylinder.
[3717.08 --> 3720.56]  And you can find more shows just like this at changelog.com.
[3720.74 --> 3722.70]  When you go there, pop in your email address.
[3722.70 --> 3729.02]  Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[3729.38 --> 3730.20]  Thanks for tuning in.
[3730.34 --> 3731.12]  We'll see you next week.
[3734.40 --> 3738.68]  Bye.
[3738.68 --> 3738.96]  Bye.
[3739.18 --> 3739.38]  Bye.
[3739.38 --> 3739.44]  Bye.
[3739.44 --> 3739.98]  Bye.
[3740.10 --> 3740.28]  Bye.
[3740.34 --> 3740.96]  Bye.
[3741.20 --> 3741.30]  Bye.
[3741.36 --> 3742.36]  Bye.
[3742.36 --> 3742.46]  Bye.
[3742.70 --> 3743.44]  Bye.
[3743.44 --> 3744.30]  Bye.
[3744.30 --> 3744.38]  Bye.
[3744.38 --> 3746.34]  Bye.
[3746.34 --> 3747.28]  Bye.
[3747.38 --> 3748.36]  Bye.
[3748.36 --> 3750.54]  Bye.
[3750.66 --> 3760.42]  Bye, bye.
