[0.00 --> 13.56]  Just last night, Ethan Douglas, one of our contestants, at the start of the season, he kind of just described himself as a data analyst and didn't have a tremendous amount of experience as a professional data scientist writing predictive models.
[14.20 --> 25.84]  And he shared with me, he has really matured as a data scientist more in the last couple months through Sliced than he has in the last few years as a self-taught coder.
[26.46 --> 29.10]  And he considers himself now a data scientist.
[29.10 --> 36.44]  So it's potential embarrassment in front of a worldwide audience watching you live code is a very strong forcing function to learn.
[36.76 --> 45.60]  So I think for folks out there who are hoping to glean the same thing from Sliced, I think the message is to just put yourself out there and set some time boxed goals for yourself.
[45.92 --> 50.60]  And this is a great set of motions to go through to learn how to do data science end to end.
[53.36 --> 56.00]  Big thanks to our partners, Linode Fastly and LaunchDarkly.
[56.38 --> 56.92]  We love Linode.
[57.00 --> 58.42]  They keep it fast and simple.
[58.42 --> 60.92]  Check them out at Linode.com slash changelog.
[61.22 --> 63.18]  Our bandwidth is provided by Fastly.
[63.54 --> 64.88]  Learn more at Fastly.com.
[65.18 --> 67.12]  And get your feature flags powered by LaunchDarkly.
[67.38 --> 69.08]  Get a demo at LaunchDarkly.com.
[69.58 --> 72.42]  This episode is brought to you by our friends at RudderStack.
[73.18 --> 77.68]  And we're calling all data engineers to check out RudderStack Cloud and start building smart customer data pipelines.
[78.18 --> 79.92]  RudderStack is warehouse first.
[80.08 --> 81.10]  No more silos.
[81.56 --> 84.90]  RudderStack builds your customer data lake on your data warehouse, not theirs.
[84.90 --> 90.60]  Enabling all functionality of a CDP with more security and retaining full ownership of your data.
[90.60 --> 93.38]  It's open source and API first.
[93.38 --> 97.14]  RudderStack can be easily integrated into your existing development processes.
[97.14 --> 100.42]  And because they're open source, you can see all their code.
[100.66 --> 103.08]  So you don't have to worry about vendor lock-in or black boxes.
[103.64 --> 105.20]  And best of all, they have transparent pricing.
[105.40 --> 107.64]  Stop paying your CDP a premium to store your data.
[108.12 --> 110.56]  RudderStack is free up to 500,000 events.
[111.02 --> 112.98]  And pricing scales transparently from there.
[113.40 --> 115.44]  Learn more and get started at RudderStack.com.
[115.44 --> 118.00]  Again, RudderStack.com.
[118.14 --> 121.70]  That's R-U-D-D-E-R-S-T-A-C-K.com.
[131.42 --> 138.56]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[138.90 --> 142.98]  This is where conversations around AI, machine learning, and data science happen.
[142.98 --> 148.06]  Join the community and Slack with us around various topics of the show at ChangeOn.com slash community.
[148.40 --> 149.36]  And follow us on Twitter.
[149.50 --> 151.10]  We're at Practical AI FM.
[156.76 --> 160.00]  Well, welcome to another episode of Practical AI.
[160.36 --> 161.88]  This is Daniel Whitenack.
[162.00 --> 165.14]  I am a data scientist with SIL International.
[165.74 --> 170.90]  I'm joined, as always, by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[171.44 --> 172.08]  How are you doing, Chris?
[172.08 --> 174.04]  I am doing very well today, Daniel.
[174.10 --> 174.52]  How are you doing?
[174.86 --> 183.70]  I am doing awesome because I think, like, my favorite new data science thing is this thing called Sliced.
[183.84 --> 190.16]  And today we have Nick Wan and Meg Rizdahl with us from Sliced.
[190.26 --> 191.44]  So I am so excited.
[191.56 --> 194.48]  I almost feel like I'm on Sliced seeing both of your faces.
[194.86 --> 196.66]  I've gotten that a few times, yeah.
[196.86 --> 201.98]  Yeah, we don't have the, you know, the podcast that just has the audio, but we're seeing your faces now.
[202.08 --> 202.86]  So welcome.
[203.36 --> 203.76]  Thank you.
[204.04 --> 204.30]  Yeah.
[204.34 --> 205.44]  Super excited to be here.
[205.48 --> 206.28]  Thanks for having us.
[206.28 --> 206.76]  Yeah.
[207.18 --> 216.48]  Well, some of our listeners, I don't know how they could not know about Sliced, but let's just suppose that maybe some of them don't know about Sliced.
[216.48 --> 219.56]  Can one of you just give a little bit of an intro for what it is?
[220.14 --> 220.80]  Go for it, Nick.
[221.44 --> 222.06]  All right.
[222.76 --> 228.98]  Sliced is a competitive data science game show that we have on my Twitch channel.
[228.98 --> 237.30]  And it's four data scientists and they receive a data set that they've never seen before.
[237.30 --> 251.92]  And they have two hours to create predictive models, data visualization, find good coding practices or random things that me and Meg have deemed important to do in the data set.
[251.92 --> 255.10]  And all these things earn them points.
[255.10 --> 266.88]  And at the end of the night, depending on how well your model performed, how good your data visualization was based off me and Meg's qualitative judging.
[266.88 --> 267.68]  Yeah.
[269.02 --> 281.02]  And how many of these things that we've buried in the data set that you find, which we call golden features, these all add up and the person with the most points wins.
[281.36 --> 282.24]  That's awesome.
[282.44 --> 283.78]  So I have two follow ups.
[283.92 --> 287.36]  One, why is this not yet on network TV?
[288.32 --> 288.86]  Great question.
[290.60 --> 296.08]  And two, maybe, yeah, could you give us just a little bit of a background?
[296.08 --> 298.58]  I know, Meg, you work with Kaggle.
[298.90 --> 306.02]  So I know that there's some background in sort of competitive data science leaderboard type things.
[306.14 --> 308.08]  Is that part of the inspiration?
[308.26 --> 311.52]  How did the collaboration come about and get started?
[312.08 --> 312.18]  Yeah.
[312.18 --> 313.14]  Where did the idea come from?
[313.58 --> 313.82]  Yeah.
[314.02 --> 316.64]  So I think there's like a few questions to unpack there.
[317.12 --> 319.46]  Where the idea came from is really fun.
[319.56 --> 320.96]  So I'll talk about that first.
[320.96 --> 325.18]  But yeah, so Nick has had the stream on Twitch that he's been doing.
[325.18 --> 337.86]  And a while back, he invited folks for these kind of like data science roundtables on Wednesdays where he just invites like people like me to come kind of chat about whatever is current on our minds, etc.
[337.86 --> 341.98]  And we kind of joked about, you know, we both like cooking.
[342.22 --> 354.36]  And so we kind of joked like what if there was something like Chopped, like the TV show, network TV show Chopped, but for data science where, you know, instead of, you know, a basket of ingredients, you've got a data set.
[354.36 --> 362.22]  And instead of, you know, an hour to create like a meal or whatever recipe, you know, they're creating predictive models.
[362.68 --> 368.46]  And, you know, we kind of like laughed about it, but then we're like, well, why the hell not do it?
[368.54 --> 375.72]  So, you know, we decided to do the like a pilot season on Nick's stream and that was really well received and it was a ton of fun.
[375.72 --> 380.22]  So, yeah, that was kind of the impetus and where the idea came from.
[381.10 --> 383.78]  And then, you know, how does it kind of relate to Kaggle?
[384.42 --> 387.16]  You know, I think like Nick and I are both really interested in data science community.
[387.48 --> 393.90]  So, you know, I do obviously work at Kaggle, very, you know, involved in like competitive data science.
[394.14 --> 396.68]  But for me, the bigger thing is the data science community.
[396.68 --> 404.86]  And I think that's what has really excited me about Slice and what's excited me about working with Nick on Slice because he's just as excited as I am about that.
[404.86 --> 410.50]  So, but I'll let you like elaborate on that answer, Nick, because I know you've got, I'm sure you have your own thoughts.
[411.26 --> 414.46]  No, that's pretty much all of it.
[414.58 --> 427.42]  I think the big thing in terms of coming together was also like, I don't know, I identified that there was like this missing sense of community in some ways.
[427.42 --> 437.62]  Like when it comes to like, you know, something that really, I don't know if it's annoying, but something that kind of annoyed me was all these like virtual conferences.
[437.62 --> 445.24]  And like the thing that I loved about conferences was like the networking and the meeting new people and being able to like catch up with old friends and stuff.
[445.36 --> 455.32]  But when like all these conferences moved virtual for the pandemic, a lot of that like stuff that I really liked about conferences got like taken away.
[455.32 --> 464.08]  And so all of this stuff that I typically liked about, you know, tech and data science and all the different conferences that I went to kind of disappeared.
[464.08 --> 471.64]  And so I've been like desperately seeking out like what was that sort of alternative and there was really no good one.
[471.64 --> 497.38]  And so I figured, well, let's just make one and bring together something that everyone can kind of rally around and cheer for people and get really become fans of people and data science and things that you would typically find at like conference socials or conference networking events, things that people can like get behind.
[497.54 --> 499.40]  And for whatever reason, it's worked.
[499.76 --> 500.92]  It's working so far.
[501.64 --> 504.02]  So that begs the question.
[504.16 --> 514.54]  So for someone who has not seen sliced, can you describe the experience a little bit, both for the viewer and also for the person who's participating directly?
[515.02 --> 518.74]  Yeah, I could talk about it from at least the viewer perspective.
[518.96 --> 520.82]  I'll have Meg do the contestant perspective.
[521.20 --> 521.56]  But sure.
[522.10 --> 525.76]  But from the viewer, you know, I've been running my stream for a while now.
[525.90 --> 530.30]  I've been streaming since I was in grad school back in 2015.
[530.30 --> 534.78]  So it's been a while for streaming and the community in chat.
[534.78 --> 536.94]  They just really want interaction.
[537.72 --> 544.82]  They go into these streams and like a really fun thing to do is being able to interact with the content creator, the streamer.
[544.82 --> 552.30]  And having that almost immediate response back and having like almost some say as to what's going on.
[552.30 --> 556.16]  It's really fun and clearly is like directly engaging.
[556.16 --> 566.84]  So when you put things in the context of like game shows or events and you have this like you almost feel like you're a fan at like a sporting event.
[566.84 --> 574.04]  And like if you have like front row seats or whatever, you're able to like almost talk to the people like doing doing the event.
[574.16 --> 574.38]  Right.
[574.38 --> 583.74]  Like being able to see like LeBron James and having like front row seats and like, you know, maybe he like gives you a ball or like falls on you or something.
[583.74 --> 586.88]  Like it's exciting just to be that close.
[587.18 --> 598.88]  And this is one of those like things that I feel that people kind of respond to in chat is like they're so close to like being able to interact with the content that's happening live.
[598.88 --> 602.88]  And not only like interact, but they actually are able to participate live as well.
[602.88 --> 606.62]  So they we have the data sets available in Kaggle.
[606.80 --> 614.48]  The contestants are using the Kaggle platform to submit and get scored by the competition as well as anyone participating.
[614.86 --> 618.02]  So they're quite literally doing all the same things as the contestants.
[618.02 --> 629.30]  And they're able to like kind of joke around with each other and find each other and make friends through chat, make friends through like the Twitter hashtag and and all sorts of fun stuff like that.
[629.30 --> 640.42]  So from the viewer perspective, I feel like there's a lot of engagement and it's like pretty natural because of just how the platform Twitch exists as it is today.
[640.94 --> 649.68]  Yeah, I would say I love kind of like the interactive, like different ways of like interacting with sliced as a viewer is pretty cool.
[649.82 --> 654.02]  But yeah, the perspective from the contestant is pretty different, of course.
[654.80 --> 655.94]  It's probably really stressful.
[655.94 --> 663.90]  Well, huge props to our our 16 contestants this season for putting themselves out there and, you know, live coding in front of.
[664.04 --> 664.46]  That's scary.
[664.86 --> 667.12]  A worldwide audience is what I like to call it.
[668.80 --> 675.32]  So, yeah, the kind of like contestant experience, you know, Nick and I put a lot of work into recruiting contestants.
[675.66 --> 678.06]  And so we've got 16 folks.
[678.06 --> 685.20]  So kind of like a little bit of maybe I don't know, the behind the scenes, I suppose, is we do everything through like Discord.
[685.44 --> 687.36]  So they're just doing like screen sharing and Discord.
[687.86 --> 694.58]  And we have like a little bit of like kind of like a green room experience, like 30 minutes where we do like kind of like set up.
[694.66 --> 697.28]  And I get kind of like the vibe check from the contestants.
[697.28 --> 706.32]  And I know it's like some nerves and they're kind of like swapping like tips and, you know, some ways that they're going to like, you know, plan to approach the challenge for the evening.
[706.54 --> 709.42]  So that's that's kind of cool, like behind the scenes to see.
[709.74 --> 711.90]  And then they kind of go dark.
[711.90 --> 716.74]  So it's like two hours, you know, live coding, which they can be fairly isolated.
[716.74 --> 718.88]  So they are they can't hear anything.
[718.94 --> 719.64]  They can't see anything.
[719.72 --> 722.12]  We don't let them watch the stream, et cetera.
[722.12 --> 726.44]  We do let them stream to their own channels if they have like Twitch or YouTube.
[726.88 --> 736.02]  So folks like Jesse Mostapak and David Robinson, you know, for instance, did their own streams on Twitch and YouTube, respectively.
[736.74 --> 738.18]  Emote only mode on Twitch.
[739.40 --> 749.22]  And so they can be fairly like in their own kind of lane for those two hours of live coding, all while knowing that, you know, their screen is visible to chat.
[749.22 --> 755.42]  So there is sometimes like I think a cool dynamic is like the one way kind of communication that we see from the contestants.
[755.42 --> 763.90]  So they'll sometimes like write like comments in there, like markdown or a big thing, a big like meta, I guess, for Slice has been memes.
[764.48 --> 768.96]  So one component of their points is chat vote.
[768.96 --> 776.72]  So basically, like I think it's like five or 10 points has varied throughout the season that they can earn through winning a chat vote.
[776.78 --> 781.10]  So we pull our audience basically at the end of the episode and say, who's your favorite, basically.
[781.96 --> 791.38]  So our contestants are doing things like throwing up really funny memes that they know the viewers can see, even though they can't like, you know, necessarily two way interact.
[791.38 --> 796.58]  So it's definitely like a little bit of like a performance that they're putting on in some sense.
[796.92 --> 797.68]  So, yeah.
[797.76 --> 803.42]  So then they live code, which is probably really stressful and nerve wracking, I imagine, as far as like the experience goes.
[803.70 --> 813.74]  And meanwhile, you know, I'm relaying kind of messages and time checks to them in Discord just to make sure that they don't go totally off the rails and, you know, get in their own head.
[813.74 --> 817.72]  And then, yeah, we invite them back to watch the stream at the end of two hours.
[818.14 --> 823.56]  And so that's always fun to kind of like they'll watch us, you know, do the judging portion.
[823.76 --> 827.94]  You know, Nick mentioned that there's like the points that we allocate for things like data visualization.
[828.82 --> 830.24]  Nick does like the leaderboard reveal.
[830.72 --> 833.32]  We sum up all the modeling points so they can watch that.
[833.56 --> 842.02]  And so it's kind of funny to see them then hop into chat and, you know, kind of start to interact with each other, interact with chat, interact with us.
[842.02 --> 844.46]  So that's pretty, pretty cool to see.
[844.74 --> 849.20]  And then, of course, you know, Nick has alluded to like the community on like things like Twitter, et cetera.
[849.36 --> 860.90]  So our contestants, you know, even outside of the show on Tuesday nights are also a big part of the community on things like Twitter through their own YouTube and Twitch channels, blogs, et cetera.
[861.02 --> 867.56]  So there's, you know, lots of participatory aspects, not just for our viewers, but for our contestants we've seen through the season.
[867.56 --> 879.20]  So one thing you said very early on as you started going through it was you talked about this spending all the time in your recruitment process, which makes me wonder, can you profile a little bit about what you're looking for?
[879.74 --> 887.72]  So, you know, you have all these, we have all these data folks that are listening to you as this goes out there and some of them want to be on your show.
[887.84 --> 890.82]  And so can you give them some tips about what your profiling is?
[891.14 --> 891.32]  Yeah.
[891.34 --> 892.20]  Nick, do you want to take that one?
[892.80 --> 893.18]  Sure.
[893.18 --> 893.22]  Sure.
[893.88 --> 900.80]  So we are looking for folks who understand what predictive modeling is.
[901.06 --> 916.40]  So being able to take a data set and being able to put that through some sort of statistical or machine learning model package and come out with predictions, whether they're regression problems or classification problems.
[916.64 --> 921.80]  So be able to go from beginning to end with a data set into predictions.
[921.80 --> 927.48]  And then also be able to have some sort of data visualization skills.
[927.48 --> 948.26]  So whether that's really basic, like if you're in base R or using matplotlib or whatever it might be, or if you are, you know, really fancy doing things in Plotly or doing things in Boca or whatever it might be, crafting like amazing interactive stuff, whatever your data visualization skill set is, just have some.
[948.26 --> 963.48]  And with those two components that typically, at least like, like, that usually qualifies most like folks as like a, you know, data analyst or above kind of skill set.
[963.48 --> 966.26]  So that's sort of what we're looking for.
[966.44 --> 972.14]  The, of course, the, the big component of all of this is, you know, you only have two hours to do all of it.
[972.14 --> 987.08]  So whether you're, you know, a 20 year vet in tech doing software engineering and deep learning, or if you, you know, are a student, the time is really, you know, the, the limiting factor for everyone.
[987.08 --> 991.06]  So you can't really get so deep into the, you know, neural net architecture.
[991.36 --> 995.38]  You can't, you know, really develop like a full end to end shiny app.
[995.38 --> 999.40]  But, uh, that does serve as sort of like, what can you do then?
[999.78 --> 1007.74]  So on top of all of that, we are always looking for people who are interested in participating for, for the next shows.
[1007.90 --> 1009.36]  And we have that on our site.
[1009.64 --> 1018.04]  So it's not too dissimilar from like a problem set you might get from, uh, like a job interview.
[1018.28 --> 1018.72]  Yeah.
[1018.72 --> 1028.18]  Um, but it really is just a, you know, double check to make sure that, you know, you have the skills that's, that, that would qualify you into, into sliced.
[1028.18 --> 1039.86]  And also, you know, you don't want to bring in people who are just going to like do nothing or do like, you know, maybe they, they think it's one thing and it's not, and they have a tough time getting through an episode.
[1040.04 --> 1044.16]  We don't want to like put people in a situation where they might be embarrassed or something.
[1044.16 --> 1056.64]  So we just really want to make sure that, you know, if you could get through some of the more basic problems or basic issues we've seen that most likely will, will, you know, we most likely will have confidence that you'll be able to get through the season.
[1057.16 --> 1057.22]  Yeah.
[1057.28 --> 1068.86]  And I would say if people are interested, they can always follow along in one of our, you know, upcoming episodes, you know, after this, this podcast comes out, but they can also take any of the previous, uh, weeks.
[1068.86 --> 1079.52]  Data sets on Kaggle and download the data set, make submissions and, you know, really like walk in the literal steps that our contestants did during the show and try to do that in two hours.
[1079.52 --> 1084.62]  And that'll give them a very real feel whether sliced is something that, uh, they might be interested in.
[1085.10 --> 1085.16]  Okay.
[1085.26 --> 1093.12]  So I watched some even last night and I have to say, we were talking about choosing some of the contestants and that sort of thing.
[1093.12 --> 1099.76]  And from my perspective in data science land, there were some like LeBrons there as part of the competition.
[1099.76 --> 1104.28]  So maybe you could just describe a little bit about some of those people in the roster.
[1104.28 --> 1117.86]  And also, I mean, these might be names some people have heard of, but maybe you could also comment about things you've been surprised or felt like you learned about these people in the competition that maybe you don't get from just their public persona.
[1117.86 --> 1117.90]  Yeah.
[1118.40 --> 1118.62]  Yeah.
[1118.70 --> 1124.44]  I think, um, so some of the names you're probably alluding to is folks like Julia Silge, David Robinson.
[1124.72 --> 1129.88]  I would put Jesse Mostapak up there as like a, you know, rising star, certainly on Twitch.
[1130.10 --> 1136.84]  I think we were able to recruit Julia Silge and David Robinson actually through like Twitter.
[1137.22 --> 1142.24]  Um, I think, you know, it got around that we were recruiting for sliced on Twitter.
[1142.24 --> 1148.72]  There was some hype from the pilot season and somebody kind of like egged on somebody else.
[1148.78 --> 1154.46]  I forget who started the egging on, you know, either Nick or I kind of jumped in and be like, yeah, we'd love to have you.
[1154.46 --> 1159.48]  And then it kind of just like rolled from, you know, kind of snowballed from there that they were both up for it.
[1159.88 --> 1164.28]  Um, they already, I think, you know, had started with some exchange of like some meme banter.
[1164.40 --> 1166.14]  So I was like, got some good vibes from this.
[1166.18 --> 1166.76]  This will be good.
[1166.76 --> 1169.70]  And, you know, I've worked with Julia Silge in the past.
[1169.80 --> 1174.04]  Her and I overlapped in some time at, uh, while we were both at Stack Overflow.
[1174.74 --> 1177.38]  Uh, David Robinson has also spent time at Stack Overflow.
[1177.50 --> 1178.26]  I've worked with Julia Silge.
[1178.34 --> 1180.26]  They've authored, uh, Tidy Tucks together.
[1180.52 --> 1182.28]  So certainly some, you know, networking.
[1182.44 --> 1184.44]  I also worked with Jesse Mostapak.
[1184.52 --> 1185.86]  She was at Kaggle for some time.
[1186.18 --> 1191.30]  So yeah, definitely, you know, just some reaching into our networks, um, to recruit some folks.
[1191.62 --> 1192.18]  Oh yeah.
[1192.20 --> 1196.74]  The other part of the question was, um, what did we learn about some of these?
[1196.76 --> 1198.08]  These folks, um.
[1198.22 --> 1200.84]  Maybe surprising things that you didn't expect.
[1201.10 --> 1201.44]  Yeah.
[1202.24 --> 1206.84]  I learned, I learned that D-Rob will stop at nothing to learn something.
[1207.24 --> 1207.58]  Yeah.
[1207.78 --> 1210.54]  You know, like, uh, he didn't know how to meme.
[1210.86 --> 1216.10]  And then he spent like a week, like studying memes.
[1217.50 --> 1219.10]  Literally studying memes.
[1221.66 --> 1223.12]  So can he meme now?
[1223.12 --> 1223.46]  Oh yeah.
[1223.46 --> 1223.76]  Oh yeah.
[1223.76 --> 1228.52]  I think I'm pretty sure I saw some, some great examples last night.
[1228.54 --> 1229.70]  He's a powerful memer.
[1229.94 --> 1230.20]  Yeah.
[1230.48 --> 1230.68]  Yeah.
[1230.78 --> 1231.22]  Yeah.
[1231.60 --> 1232.04]  Yeah.
[1232.04 --> 1232.42]  Yeah.
[1232.42 --> 1233.52]  And maybe he wasn't before.
[1233.64 --> 1234.48]  He definitely is now.
[1234.72 --> 1236.82]  He went from novice memer to master memer.
[1236.84 --> 1237.04]  Yeah.
[1237.04 --> 1237.66]  Just like that.
[1237.76 --> 1239.64]  Some might call him like a 10X memer.
[1240.02 --> 1240.14]  Yeah.
[1240.14 --> 1241.22]  He's a 10X memer.
[1241.50 --> 1241.66]  Yeah.
[1241.68 --> 1242.28]  Oh, for sure.
[1242.28 --> 1242.62]  Who knew?
[1242.84 --> 1243.98]  We didn't, we didn't know before.
[1244.46 --> 1244.64]  Yeah.
[1245.52 --> 1246.68]  A full stack memer.
[1247.02 --> 1247.40]  Yeah.
[1247.68 --> 1248.86]  A full stack memer.
[1248.86 --> 1249.22]  Yes.
[1249.86 --> 1253.20]  I don't know if it's so much that, you know, this is something that I learned, but was maybe
[1253.20 --> 1258.42]  rather like reinforced for me, but just like how much some of these folks like Julia
[1258.42 --> 1263.88]  Silge and D Rob, David Robinson are willing to just give back to the data science community.
[1263.88 --> 1267.72]  Like, you know, and Jesse Mossback too, you know, just give back to each other.
[1267.72 --> 1273.10]  Like they've like, speaking of memeing, you know, Jesse, I think offered like her coaching
[1273.10 --> 1276.42]  and memes, meme skills to David.
[1277.56 --> 1282.12]  And I think, you know, they had some like back and forth on, you know, like different
[1282.12 --> 1283.46]  memes approach, meme approaches.
[1283.78 --> 1290.14]  And, you know, they have all kind of piggybacked off of slice to create content and share content
[1290.14 --> 1293.68]  learning and educational kind of materials with their communities.
[1293.68 --> 1299.58]  And so it wasn't, you know, that's not necessarily surprising for those folks, but it's definitely
[1299.58 --> 1303.88]  reinforced, I think what is, you know, makes them really kind of like great members of
[1303.88 --> 1305.36]  the data science community.
[1305.88 --> 1308.68]  And I'm glad that, you know, slice has been a platform for them to do that.
[1309.32 --> 1314.48]  I do think like one thing that's pretty, I guess, like just universally interesting is
[1314.48 --> 1320.86]  like through slice, being able to see like some of like these rock stars of data science
[1320.86 --> 1325.02]  communication, being able to compete in something that's really foreign to everyone.
[1325.26 --> 1331.36]  I feel like it's really like leveling or like normalizing or like humanizing even a situation
[1331.36 --> 1337.40]  because a lot of the times folks, maybe people listening to the pod right now, like will know
[1337.40 --> 1343.06]  these names only through content or know these things through tutorials or books or whatever
[1343.06 --> 1343.84]  it might be.
[1344.16 --> 1348.80]  And, you know, they, they think of them as like these, you know, masters of data science
[1348.80 --> 1349.98]  or masters of engineering.
[1349.98 --> 1355.86]  And it's really hard to think like, well, I'll never be able to do what, you know, D-Rob
[1355.86 --> 1360.96]  or what Julia or what Jussie or what whomever is on the, like whoever is making a hunt out
[1360.96 --> 1361.16]  there.
[1361.46 --> 1362.88]  I'll never be able to get to that point.
[1362.88 --> 1364.86]  Like I'm all the way down here or whatever.
[1364.86 --> 1371.68]  And through the show, at least like being able to see like them not necessarily come in first
[1371.68 --> 1376.72]  place all the time, I think has been like really eyeopening because that's at least
[1376.72 --> 1378.74]  encouraging to some of the folks.
[1378.90 --> 1384.02]  I mean, not just the contestants, which like they've definitely thought that I'm going
[1384.02 --> 1384.84]  up against D-Rob.
[1384.96 --> 1385.62]  I'm going to win.
[1386.32 --> 1387.82]  You make a great point there.
[1387.94 --> 1392.36]  And, and, you know, that's, if you think about it, but kind of pre-pandemic conferences when
[1392.36 --> 1397.94]  we were going and meeting and so much of the conference was not, you know, just the talk
[1397.94 --> 1401.00]  or anything, but all the things that happened in the hallway and dinners and everything.
[1401.00 --> 1406.18]  It kind of that same point is that they gives you that chance to realize that these, these
[1406.18 --> 1410.90]  people you've aspired to are human and they have to go through a thought process too.
[1411.22 --> 1415.94]  And sometimes, you know, as, as you're pointing out, you get to see them in, in action doing
[1415.94 --> 1419.70]  it and it kind of humanizes and also teaches you along the way.
[1419.78 --> 1421.28]  So, I mean, that's a fantastic benefit.
[1421.46 --> 1422.86]  I do have a follow-up question.
[1422.92 --> 1428.98]  I'm curious about recognizing that these people clearly have, have the resources to do the
[1428.98 --> 1431.78]  job that they do for the purpose of the contest.
[1431.88 --> 1437.00]  Do they bring their own GPUs, so to speak, or is there any sort of leveling of infrastructure
[1437.00 --> 1437.64]  and equipment?
[1438.16 --> 1439.12]  How do you approach that?
[1439.62 --> 1439.78]  Yeah.
[1439.90 --> 1443.90]  So one of the things that we kind of put together in advance of the show is a little bit of
[1443.90 --> 1448.74]  like contestant guidelines and, you know, a slice being a pretty new concept.
[1448.74 --> 1454.48]  We didn't want to get super rigid with kind of like every single like minutia and kind
[1454.48 --> 1458.36]  of detail, but rather we wanted to provide some kind of like higher level guidance.
[1458.36 --> 1464.16]  And one of the pieces of guidance was just like, don't bring your supercomputer.
[1464.62 --> 1469.24]  Don't, you know, fire up TPUs for, you know, these kind of like putsy little things, like,
[1469.68 --> 1471.26]  and just kind of like asking.
[1471.80 --> 1472.02]  Yeah.
[1472.34 --> 1472.68]  Yeah.
[1472.72 --> 1473.38]  Just asking.
[1473.52 --> 1478.00]  You can't bring your own DGX, you know, to the contest just for yourself, you know?
[1478.36 --> 1478.70]  Yeah.
[1478.78 --> 1483.16]  So just kind of like asking kind of like, you know, we're sharing, here's the spirit of
[1483.16 --> 1483.50]  Slice.
[1483.60 --> 1485.24]  This is the spirit of the competition.
[1485.24 --> 1490.28]  We just ask that you kind of like keep that in mind when you think about like, yeah, what
[1490.28 --> 1491.12]  is your workstation?
[1491.22 --> 1491.74]  What's your setup?
[1491.82 --> 1493.46]  What are you going to use as far as resources?
[1494.12 --> 1498.94]  And, you know, if we ever get to a point where Sliced is on network television and,
[1499.10 --> 1506.32]  you know, we do have like literal, like LeBron James becomes a machine learning engineer and
[1506.32 --> 1512.68]  competes on Sliced, you know, and then maybe we will have to, you know, get a little stricter.
[1513.48 --> 1518.52]  Maybe we can provide resources to literally level that playing field.
[1518.76 --> 1524.44]  But for now, it's, we really wanted to invest in really solidifying what is the spirit of
[1524.44 --> 1524.98]  the competition?
[1525.10 --> 1526.28]  What is the spirit of Slice?
[1526.36 --> 1528.28]  To make sure we convey that above all else.
[1528.78 --> 1530.10]  And yeah, so far it hasn't been a problem.
[1530.10 --> 1536.08]  We've got a lot of people who are using resources already, like Colab, which does, you know,
[1536.66 --> 1543.44]  resources like that do help to level the playing field and kind of like equalize access to data
[1543.44 --> 1547.18]  science resources, not just to our contestants, but for folks who are following along.
[1547.80 --> 1551.88]  I also should mention, mention you folks could be using, you know, Kaggle notebooks as well,
[1551.94 --> 1554.90]  which provides free resources for compute.
[1554.90 --> 1559.08]  Um, but, uh, yeah, that's, that's been our thought process.
[1559.32 --> 1561.78]  Um, hasn't been a problem so far that I'm aware of.
[1561.92 --> 1566.14]  I mean, the thing, the thing about the resources in general, like even if you will have like
[1566.14 --> 1571.34]  supercomputing at your fingertips, because like, you know, one of our contestants, uh, Landon
[1571.34 --> 1573.96]  Buechner, uh, he just graduated.
[1573.96 --> 1576.98]  And so it's not in like, he just graduated as an undergrad.
[1576.98 --> 1582.10]  So it's not insane to think that if a student is on a campus that has access to a supercomputer
[1582.10 --> 1589.14]  and knows a little Linux and has, you know, access to whatever supercomputer cluster they
[1589.14 --> 1590.42]  have, that's fine.
[1590.42 --> 1593.88]  And like fine and dandy, but you only have two hours.
[1594.54 --> 1600.34]  So at the end of the day, like if you get to a point where your, you know, training is
[1600.34 --> 1605.06]  going to cost you like hours and you can like limit that to minutes through supercomputer,
[1605.06 --> 1610.50]  then okay, fair, that that's kind of, that might be a little overpowered, but our data
[1610.50 --> 1617.00]  sets are also curated in a way that the training is never going to usually be more than minutes.
[1617.00 --> 1623.78]  So like we, me and Meg do a lot on the backend to make sure that the data sets are a particular
[1623.78 --> 1624.32]  flavor.
[1624.32 --> 1626.32]  We're looking at tens of thousands of rows.
[1626.38 --> 1628.56]  We're not looking at millions of rows.
[1628.56 --> 1630.76]  We're looking at tens of columns.
[1630.76 --> 1633.44]  We're not looking at hundreds or thousands of columns.
[1633.44 --> 1639.36]  So, so even the nature of the data that folks are receiving doesn't necessarily lend itself
[1639.36 --> 1645.00]  to things like supercomputer where like in essence, if you did try to do that, you'd actually be
[1645.00 --> 1645.84]  losing time.
[1646.00 --> 1651.48]  So a lot of it is, you know, me and Meg making sure the QA on the backend is pretty good.
[1651.70 --> 1653.90]  A shout out to the engineers doing QA practice.
[1653.90 --> 1663.58]  So, um, lots of QA, uh, but, uh, also that plus the time definitely limits the resources and how powerful
[1663.58 --> 1664.40]  they could really be.
[1664.46 --> 1668.30]  We'll see when we do the, uh, sliced computer vision spinoff though.
[1668.70 --> 1669.36]  Oh yeah.
[1669.50 --> 1671.16]  That could be, that could be good.
[1671.28 --> 1672.36]  Self-driving slice.
[1672.82 --> 1673.20]  Oh yeah.
[1673.20 --> 1683.34]  Um, speaking of those, those tasks themselves, I know the one last night, Chris, Chris is going
[1683.34 --> 1684.74]  to love if he doesn't already know about it.
[1684.74 --> 1689.18]  Cause he's a, he's an animal lover, but could you describe, maybe just highlight a couple
[1689.18 --> 1694.24]  of the tasks to give a sense of what are these tasks that, um, the contestants are working
[1694.24 --> 1694.44]  on?
[1695.12 --> 1695.24]  Yeah.
[1695.24 --> 1702.00]  Uh, so last night's data set was our first multi-class classification challenge that we
[1702.00 --> 1703.36]  gave our contestants this season.
[1703.36 --> 1709.64]  So we gave them a data set of, uh, animals that were in animal shelters and they had to
[1709.64 --> 1713.18]  predict the outcome, meaning was the animal adopted?
[1713.42 --> 1716.42]  Was it transferred or was it something else?
[1716.68 --> 1719.08]  Um, so there's three classes that they had to predict.
[1719.44 --> 1723.82]  Um, and it was a data set of, I think about like 70,000 or so, you know, it was in tens of
[1723.82 --> 1729.22]  thousands of observations and they had information about what, uh, type of animal.
[1729.50 --> 1731.38]  So most of them were cats or dogs.
[1731.38 --> 1735.32]  They had, um, information about the coat color, whether the animal was spayed or neutered,
[1735.32 --> 1738.82]  uh, it, how old the animal was, uh, et cetera.
[1738.82 --> 1741.78]  So yeah, that was the data set from last night.
[1741.94 --> 1745.48]  Um, maybe I'll talk about one other, one of my favorites and then Nick, maybe you want
[1745.48 --> 1750.58]  to share one of your favorites or something, but, uh, one that was a big fan favorite, uh,
[1750.58 --> 1755.94]  as well as a contestant favorite was a data set about Airbnbs, uh, in New York city.
[1755.94 --> 1759.30]  So, um, and they were predicting, this is a regression task.
[1759.30 --> 1762.06]  So they were predicting the Airbnb price.
[1762.32 --> 1766.50]  I believe this was, uh, a fan favorite for a few reasons.
[1766.50 --> 1772.96]  So, um, really the diversity of the data set and the types of, um, the data types in the
[1772.96 --> 1778.76]  data set are really great fodder for creativity, which really plays out in things like data
[1778.76 --> 1780.76]  visualization, but also feature engineering.
[1780.76 --> 1785.72]  So this data set had, uh, text fields, it had geospatial fields.
[1786.24 --> 1790.54]  Um, so there's just a lot of like really kind of like rich data types in the data set that
[1790.54 --> 1792.20]  our contestants had a lot of fun with.
[1792.36 --> 1798.30]  And I believe this is also the challenge where we used RMSLE as our evaluation metric for the
[1798.30 --> 1798.80]  first time.
[1799.00 --> 1804.24]  So our contestants and folks following along in the audience as well, um, had to write,
[1804.24 --> 1809.76]  uh, custom, uh, evaluation metrics for this, um, for this challenge, which apparently a
[1809.76 --> 1816.30]  lot of folks found really, really fun and interesting and led to some great content outside
[1816.30 --> 1817.50]  of sliced as well.
[1817.50 --> 1823.50]  Um, like implementing RMSLE in tidy models was a blog post that Julia Silge published,
[1823.50 --> 1824.16]  I believe.
[1824.40 --> 1828.22]  And so that was a, that was a great data set just for, you know, it's richness it's in
[1828.22 --> 1829.44]  the creativity that it enabled.
[1829.44 --> 1834.30]  And yeah, any, any favorites from your end, Nick, in terms of tasks?
[1834.82 --> 1838.70]  I, you know, I see it more like a big picture thing.
[1838.80 --> 1843.84]  I feel like all the data sets are, you know, we've done, we're going to be doing 12 episodes.
[1844.00 --> 1845.22]  We did four episodes before.
[1845.22 --> 1852.02]  And like, for me, it's like the consistency that we're hitting on data sets is like the
[1852.02 --> 1853.12]  global thing for me.
[1853.12 --> 1859.98]  And that every show has been pretty close to the same, like competitive spirit, competitive
[1859.98 --> 1861.98]  advantage for everyone.
[1862.54 --> 1868.22]  And so there's not any particular data set that I have, like my personal investment in.
[1868.34 --> 1870.80]  I'm, you know, my previous line of work was baseball.
[1871.38 --> 1875.74]  And so last week we had a, uh, predict home runs data set.
[1875.74 --> 1878.30]  So that was like near and dear to my heart.
[1878.30 --> 1878.76]  That was cool.
[1879.02 --> 1884.80]  But, um, for the most part, they're all, they're all really fun data sets and, you know, the
[1884.80 --> 1889.84]  QA and all the drama at the end in terms of judging, that's like the, that's where I get
[1889.84 --> 1890.80]  my energy from.
[1891.00 --> 1893.80]  So no, no real particular favorite, I would say.
[1905.74 --> 1935.72]  Thank you.
[1935.74 --> 1941.12]  Once again, that's changelog.com slash plus plus.
[1954.18 --> 1959.58]  So we've been talking about the competition and these contestants and, and, you know, the
[1959.58 --> 1964.80]  way they're doing it, but, uh, we haven't talked in depth about how you're doing your
[1964.80 --> 1969.10]  scoring and how the winners, I know that they have two hours to do it, but you have these
[1969.10 --> 1971.82]  amazing data scientists that are competing against each other.
[1971.98 --> 1976.36]  I imagine that some of them are everyone solving or multiple people are solving.
[1976.60 --> 1979.28]  So how do you get to that winner in this game?
[1979.38 --> 1982.14]  How do you come out on top against these other superstars?
[1982.14 --> 1989.18]  You know, so many people have different approaches to modeling and just like any game, just like
[1989.18 --> 1996.28]  any sport, there's like a meta or like whatever your most, most effective tactic available.
[1996.54 --> 1997.92]  I believe that's what meta stands for.
[1997.92 --> 2005.42]  Um, so, um, whatever the best strategy is usually is like what many of the people will do.
[2005.56 --> 2011.32]  And right now, like we've seen like a progression from gradient boosted models out of the box to
[2011.32 --> 2013.52]  like grid search and gradient boosted models.
[2013.52 --> 2023.06]  And then now we're in this like, like Bayesian optimization grid search, like meta where, uh,
[2023.06 --> 2029.24]  the best models tend to be like models that have like Bayesian parameters, like on top of
[2029.24 --> 2032.14]  the grid search, your typical grid search parameters.
[2032.76 --> 2039.78]  So right now, like in terms of the modeling side, you see a lot of like heavy duty grid searching,
[2039.78 --> 2044.56]  which to be completely honest, I didn't think we'd ever seen sliced when we did the pilot season.
[2044.68 --> 2048.92]  I thought people were just going to be like out of the box models and like try a bunch of them and
[2048.92 --> 2049.58]  see what works.
[2049.68 --> 2054.94]  But now, you know, people are diving really hardcore into like model tuning in the show,
[2055.10 --> 2056.84]  which is pretty impressive to me.
[2057.08 --> 2064.24]  And then usually it's like splitting hairs at the end, you know, like, uh, we've seen everything
[2064.24 --> 2069.72]  from like arbitrary weights and ensembling model, uh, predictions that just,
[2069.78 --> 2075.02]  like gains a slight point advantage in your log loss above someone else.
[2075.16 --> 2081.00]  And so people will try some like risky, maybe not exactly best coding practice,
[2081.00 --> 2085.42]  but like maybe good for the contest ways to like reduce loss.
[2085.66 --> 2089.62]  And so on the modeling side, there's that, but then like, you know, there's this whole
[2089.62 --> 2091.98]  data visualization judging side of things.
[2091.98 --> 2094.80]  And that's where things get like really tough for me and Meg.
[2094.80 --> 2100.70]  Can it get subjective in the sense of like, you can have different strategies from different
[2100.70 --> 2103.62]  contestants and at the end they have different visualizations.
[2103.86 --> 2106.10]  So you're how, I mean, that has to be tough.
[2106.10 --> 2110.00]  And, and when you're, you know, doing it live on the spot, how do you manage that?
[2110.24 --> 2111.04]  It's very stressful.
[2111.30 --> 2111.86]  I imagine.
[2112.12 --> 2115.62]  It's super stressful because like, we're watching them, like we're watching them like,
[2115.92 --> 2117.84]  you know, paint it in front of us.
[2117.84 --> 2118.10]  Right.
[2118.10 --> 2122.40]  And like, it's very different than like just walking into a museum and seeing it there,
[2122.40 --> 2127.26]  like opening a textbook and seeing them there, like the layering and the iteration,
[2127.26 --> 2130.48]  it really gives you this other appreciation of this data viz.
[2130.58 --> 2138.96]  And so like, at the end you do get pretty, pretty, uh, differing or even polarizing opinions
[2138.96 --> 2141.42]  as to who has better visualization and others.
[2141.58 --> 2146.46]  And like me and Meg, although maybe like half the time we're kind of in sync with points.
[2146.46 --> 2150.48]  There's a lot of the time where me and, me and Meg will like differ and, uh, I'll let
[2150.48 --> 2153.10]  Meg like kind of tell you all about it.
[2153.20 --> 2154.32]  How do you guys resolve that?
[2154.38 --> 2155.36]  I mean, that's, it sounds like.
[2155.36 --> 2156.66]  We don't, we don't, we just move on.
[2158.78 --> 2161.64]  I think over time we have become more in sync.
[2161.88 --> 2166.52]  Uh, I want to say, I don't know, maybe that's just a wishful thinking or something, but, um,
[2167.04 --> 2172.30]  yeah, I mean, it's a hundred percent subjective and, you know, we have written out in the,
[2172.30 --> 2176.44]  the contestant guidelines that I mentioned earlier, we have given them some sense of
[2176.44 --> 2177.62]  like the things that we look for.
[2177.98 --> 2182.44]  But really, I think there's like three approaches overall that I've seen our contestants take
[2182.44 --> 2184.02]  to the data visualization portion.
[2184.52 --> 2187.70]  The easiest is probably just like volume.
[2188.10 --> 2192.16]  So some contestants just go for like, I'm just going to go for like basic all over the
[2192.16 --> 2196.92]  board, kind of like EDA kind of stuff, like just looking at different cuts of the data
[2196.92 --> 2201.26]  in visualizations and kind of otherwise keep things very basic.
[2201.26 --> 2207.08]  The second approach I would say is people who really go for the insights, which I think
[2207.08 --> 2210.44]  those are the, those are the folks that are looking for the data visualization points.
[2211.10 --> 2216.90]  So, uh, I would say people who stand out in this regard are folks like David Robinson, also
[2216.90 --> 2222.52]  one of our contestants, Josh Polkamp-Hart, who competed, uh, in, uh, yesterday's episode
[2222.52 --> 2228.02]  really do a lot of work to iterate and draw out true insights from the data, um, which is
[2228.02 --> 2229.70]  something that we look for and really appreciate.
[2229.70 --> 2234.12]  And, you know, they spend time kind of like customizing their plots to really make them
[2234.12 --> 2238.54]  really readable and following best practices as far as data visualization.
[2239.24 --> 2243.76]  And then there's the third, I think category, which is folks who are driven to look for golden
[2243.76 --> 2244.20]  features.
[2244.42 --> 2247.18]  And we haven't talked a ton about golden features yet.
[2247.50 --> 2253.96]  Um, but, um, golden features are another way our contestants earn points, which is basically
[2253.96 --> 2259.54]  a couple of like things that Nick and I have buried, so to speak in the dataset, um, Easter
[2259.54 --> 2264.88]  eggs, like, yeah, they're like Easter eggs kind of, um, like what's a good example, golden
[2264.88 --> 2265.50]  feature.
[2266.08 --> 2271.28]  Speaking of like the Airbnb dataset, one of the golden features was to take some of the
[2271.28 --> 2275.80]  metadata about the Airbnb listings and extract the number of bedrooms and bathrooms.
[2276.06 --> 2278.22]  Um, so it was to do a little bit of like text processing.
[2278.54 --> 2281.80]  Other times it's to create, um, some kinds of data visualization.
[2281.80 --> 2286.48]  So once one dataset, we had them create like a bump plot, or that's like something we wanted
[2286.48 --> 2290.16]  them to look for, bump plot of like a rank, uh, dataset.
[2290.50 --> 2294.38]  And so if they've, they happen through the course of their two hours of live coding to
[2294.38 --> 2299.00]  create one of these plots or these, the engineer their features in a certain way or whatever,
[2299.58 --> 2300.66]  that will earn extra points.
[2300.84 --> 2304.80]  So a lot of folks are really just kind of going for this like scattershot approach of
[2304.80 --> 2308.40]  like, I'm just going to find some golden features and hope that Nick and Meg want to
[2308.40 --> 2313.86]  see me facet or want to see me use polar coordinates or want to see me, you know, do this or that
[2313.86 --> 2314.42]  with a dataset.
[2314.58 --> 2317.74]  So it's kind of like a little bit like that you can tell that they're getting creative.
[2318.02 --> 2323.60]  And sometimes you see them sort of like bend some rules of data visualization, uh, where
[2323.60 --> 2327.90]  it's like, uh, that's not maybe the most intuitive way to display that data, but you're just kind
[2327.90 --> 2333.42]  of trying to like fit a square dataset into a round golden feature hole or something like
[2333.42 --> 2335.18]  that, uh, just to earn some points.
[2335.32 --> 2339.94]  So I would say that kind of like summarizes the strategies that I think I've seen from
[2339.94 --> 2343.44]  our contestants as far as trying to earn points from data visualization.
[2343.86 --> 2351.12]  But I like it best when we see folks, um, really looking for insights because, um, I think
[2351.12 --> 2355.96]  that's the purpose of data visualization in the same way that, you know, modeling the modeling
[2355.96 --> 2361.14]  portion, the purpose is to get the lowest log loss or the, you know, whatever the metric is.
[2361.14 --> 2366.62]  I have a little bit of a tongue in cheek follow-up and that is for, for the contestants, which
[2366.62 --> 2368.70]  one of you are they most worried about?
[2368.78 --> 2369.28]  Do you think?
[2369.48 --> 2370.10]  Oh, it's Meg.
[2370.76 --> 2372.24]  We know it's Meg.
[2372.80 --> 2373.06]  Yeah.
[2373.22 --> 2379.14]  I think I, I somehow earned some reputation early on that was, I think, yeah, reinforced
[2379.14 --> 2384.54]  through chat, like that, uh, I want to say I gave one of our contestants like just one point,
[2384.54 --> 2385.88]  uh, in data visualization.
[2385.88 --> 2391.24]  So we have at that point, maybe we had like 15 points to allocate across the four contestants.
[2391.24 --> 2393.62]  Now we allocate 20 points across to contestants.
[2393.94 --> 2396.02]  And I gave one of our contestants one point.
[2396.02 --> 2402.10]  And I think I said something like you did data visualization, you checked a box, you created
[2402.10 --> 2402.86]  like one plot.
[2402.86 --> 2407.32]  So it was kind of like a conciliatory, like just one point for doing it, but otherwise
[2407.32 --> 2407.94]  it was crap.
[2409.28 --> 2410.34]  So, um.
[2410.46 --> 2411.04]  What's the guy's name?
[2411.12 --> 2411.94]  Simon Cowell.
[2412.42 --> 2412.62]  Yeah.
[2412.96 --> 2415.60]  A little bit like that, maybe just, just a tiny bit.
[2415.60 --> 2416.66]  Meg is the Simon.
[2416.88 --> 2418.28]  Meg is the Gordon Ramsey.
[2419.84 --> 2420.24]  Yeah.
[2421.28 --> 2426.88]  There was another time that was very painful for me to give, I think it was Julia Silge.
[2426.98 --> 2431.20]  I had to give her two points and I said, I'm going to have nightmares about this to give
[2431.20 --> 2435.26]  Julia Silge, who is like, I, you know, I revere her.
[2435.44 --> 2436.70]  She's, you know, incredible.
[2436.98 --> 2439.48]  She creates such beautiful data visualizations.
[2439.66 --> 2442.86]  You know, when I worked with her, she's incredible.
[2443.14 --> 2445.26]  Her blogs are, you know, such beautiful.
[2445.26 --> 2449.92]  And then I ended up, you know, like I'm evaluating on your performance tonight and sliced two
[2449.92 --> 2450.38]  points.
[2450.62 --> 2453.04]  I feel terrible, but, uh, yeah.
[2453.16 --> 2457.68]  So I'm willing to be harsh, a harsh grader, I think when it comes to data visualization.
[2457.68 --> 2464.04]  So you mentioned that there's like some unique aspects of learning that have come out of sliced.
[2464.24 --> 2469.26]  And I actually like how you tied, you know, the inspiration of this came out of chopped
[2469.26 --> 2475.56]  because even in the past, I think here with Chris on the show, I've thought I've sort of more compared
[2475.56 --> 2482.16]  data science or AI development, like in the real world, more to, to cooking than to like,
[2482.16 --> 2486.72]  people think you're sort of in your room with the chalkboard and you're writing like really
[2486.72 --> 2489.24]  cool equations on like the chalkboard or whatever.
[2489.24 --> 2493.64]  But I've always found it much more like cooking in the sense that like, hey, here are your
[2493.64 --> 2494.08]  ingredients.
[2494.08 --> 2500.16]  And like a set of tools that are some good, some maybe not good, like figure out how to
[2500.16 --> 2502.18]  bake something that's not terrible.
[2502.18 --> 2507.64]  And the thing about industry is like, it's always in a given period of time, right?
[2507.72 --> 2514.08]  You have a milestone or like, you're likely not going to have like six or 12 months to
[2514.08 --> 2519.46]  like refine the first version of your like predictive model or something like that.
[2519.60 --> 2520.40]  Cause you have a boss.
[2520.78 --> 2520.96]  Yeah.
[2521.10 --> 2522.12]  You, you have a boss.
[2522.12 --> 2529.20]  So I don't know how, how has the community engaged with that element of the learning?
[2529.20 --> 2533.08]  Like the ones that are off, you know, not, not featured as contestants.
[2533.08 --> 2538.04]  Have you heard anything from them as they're also participating in this challenge in that
[2538.04 --> 2538.86]  timed way?
[2539.18 --> 2540.62]  That's a great question.
[2541.10 --> 2547.68]  I mean, I know anecdotally from Twitter, like Nick and I religiously follow the, the sliced
[2547.68 --> 2548.26]  hashtag.
[2548.26 --> 2552.06]  It's probably embarrassing if I were to admit how much we follow it.
[2552.12 --> 2558.30]  But, um, I mean, yeah, I certainly see people are, you know, learning from the show and kind
[2558.30 --> 2559.82]  of going through the motions themselves.
[2560.12 --> 2565.70]  I think though, we are seeing the same thing from our contestants too.
[2565.82 --> 2567.38]  And I think that is actually significant.
[2567.66 --> 2573.04]  Um, and, uh, you know, it's bigger than I could have guessed or imagined.
[2573.04 --> 2578.12]  Like just last night, Ethan Douglas, one of our contestants at the start of the season,
[2578.12 --> 2580.36]  you know, we're in the playoffs now at the start of the season.
[2580.36 --> 2585.96]  And he kind of just described himself as a data analyst and didn't have a tremendous amount
[2585.96 --> 2590.36]  of experience as a professional data scientist writing predictive models.
[2591.02 --> 2599.24]  And he shared with me in kind of like the pre-show green room, so to speak, that, um, he
[2599.24 --> 2605.22]  has really matured as a data scientist more in the last like couple months through sliced
[2605.22 --> 2608.66]  than he has in the last few years as a self-taught coder.
[2609.30 --> 2612.28]  And, um, he considers himself now a data scientist.
[2612.92 --> 2617.34]  So he has really evolved and learned a ton, you know, from the show.
[2617.52 --> 2622.04]  I think, you know, our contestants are doing a lot of like, some of them are doing a lot
[2622.04 --> 2625.90]  of like practice, um, in between episodes where they're making appearances.
[2625.90 --> 2631.82]  And it's obviously a very strong potential embarrassment in front of a worldwide audience watching you
[2631.82 --> 2635.08]  live code is a very strong forcing function to, to learn.
[2635.64 --> 2640.88]  And so I think, you know, for folks out there who are, you know, hoping to kind of glean the
[2640.88 --> 2645.58]  same thing from sliced, like, I think the message is to just like put yourself out there and set
[2645.58 --> 2651.42]  some like time boxed goals for yourself and yeah, go through this apparently is a great set of
[2651.42 --> 2657.48]  motions to go through to, to, to learn how to do data science, um, end to end, or, you know,
[2657.48 --> 2658.08]  it's a motivator.
[2658.08 --> 2658.48]  Yeah.
[2658.92 --> 2659.46]  That's awesome.
[2659.46 --> 2662.30]  So you have a championship coming up.
[2662.44 --> 2663.00]  Is that right?
[2663.28 --> 2663.52]  Yes.
[2663.54 --> 2666.58]  When is the, when is the, uh, slice championship?
[2667.52 --> 2669.76]  That is August 17th.
[2669.94 --> 2674.84]  And how do people find, I mean, I don't know how they could not find sliced on Twitter,
[2674.84 --> 2681.34]  at least in my, in my feed, but how do people find sliced and make sure that they, they tune
[2681.34 --> 2682.46]  into the championship?
[2682.94 --> 2686.28]  Um, you can tune in to slice on Tuesdays.
[2686.36 --> 2688.08]  Uh, we have the semifinals next week.
[2688.08 --> 2689.06]  That's August 10th.
[2689.06 --> 2691.72]  And then we have the championship on August 17th.
[2692.30 --> 2698.20]  And that is twitch.tv slash Nick Wann underscore data side.
[2698.86 --> 2699.30]  Awesome.
[2699.78 --> 2702.02]  And we'll put that link in our show notes as well.
[2702.02 --> 2707.08]  So make sure and, and click and watch and go to the previous competitions too.
[2707.08 --> 2709.22]  And the data sets as well, for sure.
[2709.22 --> 2710.66]  Like, like has been mentioned.
[2710.98 --> 2716.78]  And can we look forward to future seasons of, of sliced is, will this continue?
[2716.94 --> 2718.28]  Can you give us a little insight there?
[2718.28 --> 2719.00]  Yeah.
[2719.00 --> 2719.18]  Yeah.
[2719.46 --> 2722.76]  Um, we have some stuff in the works right now.
[2722.94 --> 2727.16]  Uh, and hopefully we will be able to share that, uh, really soon with everyone.
[2727.46 --> 2733.74]  Uh, so we're looking forward to not just, uh, slice season two, but different forms of
[2733.74 --> 2734.50]  sliced, even.
[2735.00 --> 2735.68]  Sliced in space.
[2735.68 --> 2737.28]  He's talking about sliced in space.
[2738.50 --> 2740.10]  I assume that.
[2740.52 --> 2742.08]  Just wanted to make sure it was clear.
[2742.22 --> 2744.40]  Do you go slice in space?
[2744.40 --> 2748.16]  Maybe you could help, you know, yeah.
[2748.22 --> 2751.02]  Hook us up with some Lockheed Martin help, you know, to get us there.
[2751.40 --> 2751.94]  There you go.
[2752.06 --> 2752.68]  Maybe so.
[2752.88 --> 2752.96]  Yeah.
[2753.82 --> 2760.40]  Um, but yeah, um, we got some slice news probably in the very near future and slice season two.
[2760.62 --> 2765.10]  Uh, we'll, uh, we'll take a breather and then we'll, we'll regroup and we'll figure
[2765.10 --> 2767.78]  out when we're going to launch that sometime next year.
[2768.12 --> 2768.52]  Yeah.
[2768.56 --> 2772.30]  I think needless to say, like Nick and I have been really like blown away by the reception
[2772.30 --> 2774.52]  to sliced and having a lot of fun.
[2774.68 --> 2777.46]  So, I mean, I want to keep doing sliced season two.
[2778.30 --> 2778.46]  Awesome.
[2778.62 --> 2780.30]  Well, I hope you both do.
[2780.42 --> 2784.12]  And I know I will tune in and I'm excited to tune in for the championship.
[2784.78 --> 2787.10]  Um, it's, uh, uh, really exciting.
[2787.10 --> 2788.56]  So thank you both.
[2788.68 --> 2795.16]  Um, appreciate you joining us after a big day yesterday with, uh, with quarterfinals and,
[2795.16 --> 2795.72]  uh, yeah.
[2795.84 --> 2797.20]  See you, see you on Twitch.
[2797.48 --> 2798.20]  Thanks y'all.
[2798.48 --> 2798.94]  Thank you.
[2802.30 --> 2804.56]  Thank you for listening to practical AI.
[2804.84 --> 2810.20]  We have a bundle of awesome podcasts for you at changelog.com, including our brand new
[2810.20 --> 2815.80]  show, ship it with Gerhard Lezou, a podcast about getting your best ideas into the world
[2815.80 --> 2817.08]  and seeing what happens.
[2817.20 --> 2821.30]  It's about the code, the ops, the infra and the people that make it happen.
[2821.58 --> 2821.82]  Yes.
[2821.84 --> 2825.32]  We focus on the people because everything else is an implementation detail.
[2825.46 --> 2830.36]  Subscribe now at changelog.com slash ship it or simply search for ship it and your favorite
[2830.36 --> 2831.02]  podcast app.
[2831.02 --> 2831.58]  You'll find it.
[2831.70 --> 2834.98]  Of course, the galaxy brain move is to subscribe to our master feed.
[2835.10 --> 2840.38]  It's all changelog podcasts, including practical AI and ship it in one place.
[2840.70 --> 2845.46]  Search changelog master feed or head to changelog.com slash master and subscribe today.
[2845.92 --> 2850.64]  Practical AI is hosted by Daniel Whitenack and Chris Benson with music by Breakmaster Cylinder.
[2850.86 --> 2853.36]  We're brought to you by Fastly, LaunchDarkly and Linode.
[2853.66 --> 2854.38]  That's all for now.
[2854.58 --> 2855.54]  We'll talk to you again next week.
[2861.02 --> 2891.00]  We'll talk to you again next week.
