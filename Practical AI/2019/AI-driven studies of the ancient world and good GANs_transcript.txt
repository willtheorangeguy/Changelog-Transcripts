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
[41.34 --> 45.20]  So if you have build boxes, CI, CD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.18 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.14 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 --> 88.56]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.22 --> 102.28]  And now onto the show.
[106.54 --> 113.30]  Welcome to another Fully Connected episode where Daniel and I keep you fully connected with everything that's happening in the AI community.
[113.54 --> 116.22]  We'll take some time to discuss the latest AI news,
[116.22 --> 120.46]  and we'll dig into learning resources to help you level up on your machine learning game.
[120.86 --> 121.98]  My name is Chris Benson.
[122.24 --> 128.82]  I am a chief AI strategist at Lockheed Martin, focusing on artificial intelligence, high performance computing, and AI ethics.
[128.98 --> 134.54]  And with me is my co-host, Daniel Whitenack, who is a data scientist working with various NGOs and nonprofits.
[134.70 --> 135.48]  How's it going today, Daniel?
[135.86 --> 136.86]  It's going great.
[136.86 --> 144.48]  Great to talk again after the July 4th holiday and get back into all AI goodness.
[144.90 --> 146.32]  Lots of good family stuff, right?
[146.66 --> 149.20]  Yeah, lots of good family stuff.
[149.36 --> 156.28]  Lots of, you know, family stuff is always good and great and awkward and all of those things at the same time.
[156.38 --> 159.82]  But it was great to see family and have a couple days off.
[159.90 --> 160.76]  So what about you?
[161.62 --> 163.04]  It's pretty much the same.
[163.22 --> 164.88]  As you know, I have all these dogs.
[165.06 --> 170.22]  So for us, fireworks, you know, twice a year on the July 4th holiday and at New Year's Eve.
[170.62 --> 175.00]  We try to have a little bit of fun early in the day and then hunker down with terrified dogs.
[175.32 --> 176.46]  Yeah, that's rough.
[176.60 --> 177.36]  Yeah, it was our usual.
[177.58 --> 178.24]  It wasn't bad.
[178.60 --> 180.38]  And I'm excited.
[180.56 --> 189.02]  As we were recording, I'm about to head to Boston to participate in the developer workshop for Alpha Pilot,
[189.02 --> 196.90]  which is a venture that Lockheed Martin is partnering up with NVIDIA and MIT and the Drone Racing League,
[197.34 --> 202.34]  where we have teams from major universities all over that are coming together.
[202.48 --> 208.04]  And they're going to be starting the process of creating various neural network models
[208.04 --> 213.24]  that are going to drive some really serious drones around a race course at high speed.
[213.48 --> 216.92]  So I'm going to get a chance to meet a whole bunch of smart people this week.
[216.98 --> 218.42]  I'm really looking forward to that process.
[218.42 --> 219.36]  It should be a lot of fun.
[219.72 --> 220.76]  That sounds really exciting.
[220.94 --> 224.78]  Is there a place people can follow up with that?
[225.24 --> 228.66]  Do you know if there'll be like videos or recordings of this stuff going on?
[228.90 --> 231.68]  As far as this one, this is kind of the developer workshop.
[232.06 --> 234.04]  And we'll see about what can come out.
[234.12 --> 239.42]  There's going to be a whole series of Alpha Pilot drone races going on through the end of the year.
[240.02 --> 243.96]  And I'll put a link in the show notes where people can kind of connect in if they're interested.
[243.96 --> 249.90]  But every time I think about this, I'm sure the people doing it will roll their eyes.
[250.12 --> 256.34]  But you know in that in Star Wars Episode I, when the young Anakin's flying around through the desert,
[256.52 --> 258.28]  that's the thing that always teases my brain.
[258.40 --> 260.54]  I think it's a little bit more down to earth than that.
[260.74 --> 265.22]  But I'm looking forward to having fun with my version of Star Wars this coming week.
[265.22 --> 266.44]  Yeah, yeah.
[266.62 --> 268.84]  No, that sounds like a lot of fun.
[268.94 --> 269.86]  It sounds very exciting.
[270.20 --> 272.94]  And it's always cool to see AI.
[273.70 --> 279.06]  You know, a lot of times we're just focused on, like I'm staring at my monitor on my computer and doing quote unquote AI.
[279.24 --> 288.66]  But it's cool to see like AI and machinery of some type interact, whether that be robots or drones or little cars or whatever it is.
[289.22 --> 293.20]  So that's always fun and kind of connects it to the real world, I think.
[293.56 --> 294.12]  It does.
[294.12 --> 301.18]  I mean, it's going to be interesting to see this as AI that most definitely has a tangible real world impact, you know,
[301.18 --> 303.58]  that people can enjoy as sport and as televised.
[303.80 --> 307.20]  So looking forward to the start of that process this week.
[307.82 --> 313.86]  And, you know, you and I had not done a show where we're really focusing on current events in a while.
[314.00 --> 322.40]  And as we were talking, we decided let's do that this time around because there's been so much news out that we have kind of gone right by in the weeks.
[322.40 --> 332.30]  And so we're hoping listeners will sit down and enjoy us as we kind of go through this process of talking about some of the more interesting things we found in AI news lately.
[332.30 --> 334.62]  There's been a ton going on.
[334.82 --> 338.38]  I feel like we've done the topical shows, which have been really good.
[338.44 --> 343.98]  And I'm glad that we've kind of, you know, done that and got gotten deep in some of the subjects.
[343.98 --> 347.44]  But there's just been so much accumulating in the news.
[347.62 --> 350.80]  I think it'd be great to cover some of those things.
[350.98 --> 363.10]  Now, for our listeners, there's been actually so much going on in the AI community that it's really hard to narrow down into a number of topics that we can discuss in this format only in 45 minutes or whatever we have.
[363.10 --> 365.58]  So we've done our best to highlight a few things.
[365.76 --> 374.58]  But if you find anything interesting that you're interested in or involved with in the AI community, please share that with us on our Slack channel.
[375.08 --> 380.86]  You can find that at changelog.com slash community and or on our LinkedIn page.
[381.22 --> 387.40]  And we're happy to hear about what you're doing and also maybe feature some of that on the show in the future.
[387.80 --> 390.62]  We've done that in the past and hope to do it more in the future.
[390.62 --> 395.38]  All right. Well, you want to kick us off with the first article that you had brought to our attention?
[395.92 --> 400.90]  Yeah. So this is actually like a series of articles that I've seen recently.
[400.90 --> 405.32]  I tried to think about some trends that I've been seeing in the AI community.
[405.58 --> 420.18]  And one of the things kind of this spring, moving into like very recently, a trend that I've seen starting to develop is various AI techniques that are impacting studies of the ancient world.
[420.18 --> 433.32]  So I'm thinking of like things like studying ancient languages or archaeology or preservation of artifacts or making discoveries about the ancient world.
[433.46 --> 444.58]  There's been various things that are happening where the AI community is kind of intersecting and worlds are colliding with archaeology and linguistics and other things.
[444.58 --> 446.92]  So I saw a couple of these things recently.
[447.18 --> 451.54]  One that seems to have gotten a lot of attention was a study.
[451.72 --> 455.98]  So I read about this in the MIT Technology Review.
[456.54 --> 459.96]  But there's an article on the archive as well.
[460.52 --> 468.56]  And the title of the article is machine learning has been used to automatically translate long lost languages, which seems pretty cool.
[468.84 --> 469.94]  Does it seem cool to you, Chris?
[469.94 --> 471.50]  It seems very cool to me.
[471.60 --> 472.52]  There's so much happening.
[472.92 --> 475.96]  We keep calling out how much is happening in NLP these days.
[476.12 --> 478.54]  And that is natural language processing.
[478.80 --> 483.32]  For those not familiar, it's just been huge over the last year.
[483.72 --> 483.92]  Yeah.
[484.06 --> 491.20]  And this in particular, it's like all of those recent discoveries kind of mixed with Indiana Jones a little bit.
[491.28 --> 493.62]  So it makes it even more awesome, I think.
[493.96 --> 496.56]  But there was a study.
[496.56 --> 502.06]  So apparently, there are these ancient kind of lost languages.
[502.42 --> 504.38]  And I guess there's a number of them.
[504.80 --> 512.78]  But archaeologists have discovered kind of tablets and other things with these languages that date back to various times.
[513.00 --> 521.02]  In fact, there's this kind of language called Linear A, apparently, which dates from like 1800 to 1400 BC.
[521.02 --> 527.48]  And then there's another one called Linear B, which dates, you know, along the same time period.
[528.40 --> 531.84]  And Linear A actually hasn't, I guess, hasn't been deciphered.
[531.90 --> 534.24]  But Linear B has been deciphered.
[534.26 --> 539.92]  It was deciphered only like, I forget what the article said, not that long ago.
[539.92 --> 549.58]  But the article basically shows how these researchers, which are from, let me see here, from MIT and Google.
[550.00 --> 552.62]  So Google Brain and MIT.
[552.62 --> 571.06]  What they did was they basically showed how they could utilize similar words or similarities between various languages and how they were historically derived to kind of automatically decipher this Linear B language, which is actually a lost language.
[571.06 --> 580.90]  And they showed that they could basically do it in a way that, you know, didn't rely on like parallel data.
[581.02 --> 584.18]  So it's like a real deciphering of this language, which is pretty cool.
[584.74 --> 585.56]  That sounds really neat.
[585.64 --> 591.10]  I mean, so they're not basically looking for common words, for lack of a better description.
[592.18 --> 595.76]  They're almost common approach to how language would be formed at the time.
[595.76 --> 606.82]  Yeah, so there's this idea of like cognates, which I guess, and I'm not a linguist, so I apologize to all linguistic people out there where I'm butchering things.
[607.18 --> 611.02]  But these are kind of words that look similar in multiple languages.
[611.52 --> 616.54]  So you're probably familiar with this, definitely in English and other languages.
[617.00 --> 622.54]  But they utilize these kind of similar looking words, I guess, or these corresponding cognates.
[622.54 --> 625.56]  And then they do a sort of character matching thing.
[625.90 --> 632.52]  And they have a pretty cool diagram in their paper where kind of lost language characters come in.
[632.64 --> 640.32]  And they use like LSTMs and attention and softmax and kind of, you know, known characters come out.
[640.32 --> 656.88]  And so they do this kind of translation between linear B, which is this lost language, and Greek, based on these also utilizing these corresponding cognates and this cognate mapping sort of stuff.
[657.02 --> 659.28]  So they don't really use, you know, parallel.
[659.50 --> 663.32]  They don't need parallel data between linear B and Greek.
[663.42 --> 668.04]  They're really treating it as a lost language, but they're utilizing these similar looking things.
[668.04 --> 670.02]  That seems really cool.
[670.22 --> 677.56]  I love the fact that there are so many applications that we're able to apply neural network technology of today to.
[677.74 --> 680.80]  It's impacting just about everything you can imagine.
[680.96 --> 689.30]  I can now, going back to your Indiana Jones, I can imagine Indiana just, you know, sighing wistfully, putting down its whip, and sitting down at his laptop to get the real work done.
[689.30 --> 697.96]  Yeah, and there's this other article, which I think very much fits within that, you know, that framework.
[698.24 --> 706.86]  There's this other article, which I actually also read on MIT Tech Review, which I guess I get a lot of things from there, it seems like.
[707.32 --> 710.38]  But this has to do not with language, but with games.
[710.38 --> 725.84]  So I guess there's medieval manuscripts that include these representations of games, whether that's like games played on horseback or games like played like table games or dice games or these other games.
[726.72 --> 735.74]  And up till now, there wasn't really, I guess there wasn't really a field of like study around ancient games.
[735.74 --> 750.32]  And so there's this researcher in the Netherlands who's kind of proposing that there's this new field of study of ancient games, which I'm probably going to mispronounce this, archaeoludology.
[750.78 --> 756.00]  And anyway, he has these pictures of these ancient games that are represented in manuscripts.
[756.00 --> 773.34]  And he's proposing and has shown some evidence that using machine learning and AI, we could use things like computer vision, but also evolutionary algorithms and other things to actually learn about how these games evolved, about their rules.
[773.68 --> 784.04]  And even like take the whole of games that have been, you know, developed through time and use their kind of basic elements to generate new games.
[784.04 --> 795.66]  So there's also this idea of using all of these basic elements of games through history and then using AI to take those components and generate new games that we might, I guess that we might want to play.
[795.76 --> 796.78]  I guess that's the goal.
[797.28 --> 799.86]  Yeah, I flipped up the webpage that you're referring to.
[799.86 --> 811.00]  And like they have a picture of kind of an image of an old game with, you know, that looks like a plus sign sort of with various squares on it and images.
[811.26 --> 814.66]  And then they have what I assume is a modern version of the same game.
[814.78 --> 817.16]  So it seems, let me ask you this.
[817.20 --> 817.90]  I'm kind of curious.
[818.66 --> 822.04]  There seems to be a little bit of commonality potentially between these two.
[822.04 --> 829.06]  I mean, in one case, we're talking about looking at old games to try to derive, you know, how they came about and what their rules are.
[829.22 --> 832.54]  And yet we just talked about, you know, lost languages as well.
[832.64 --> 837.90]  And going back, would you consider that to be somewhat similar approach as NLP being used in both areas?
[838.48 --> 843.12]  I think maybe the commonality is maybe even a little bit higher.
[843.36 --> 849.40]  Like I know one thing that you're going to talk about later in our chat today is unsupervised learning.
[849.40 --> 868.14]  And I think the connection that's happening in a lot of different areas of AI is really the kind of transition to these like semi-supervised methods and methods that kind of start from some data, but not really like labeled data or annotated data and like try to learn something.
[868.14 --> 878.82]  So in the lost language case, they're really starting with, you know, text or characters from these languages and, you know, learning and deciphering these lost languages.
[879.04 --> 891.10]  In the games case, they're starting with these images and maybe rules and they're kind of doing some sort of evolutionary thing to learn about how those evolved or to generate new things.
[891.30 --> 896.36]  So I think we're definitely seeing a lot of that all over the AI community.
[896.36 --> 898.18]  So I'm kind of curious.
[898.70 --> 904.72]  Do you think that there's any particular work that is interesting to you at this point that this might be applied to in other areas?
[904.86 --> 911.64]  Like if you were, you know, you're looking, I know, and I know you're deeply involved in doing work with languages in your day job.
[911.96 --> 922.10]  What other areas do you think may this be, you know, very applicable to in terms of, you know, going and rediscovering things from the past or taking something we're already doing and thinking about what's next?
[922.10 --> 927.42]  Yeah, I mean, I was really excited when I saw the lost languages article.
[927.42 --> 930.50]  I think that I only have a certain perspective.
[930.66 --> 933.52]  So I'm sure there's there's other things that are happening.
[933.52 --> 941.28]  But, you know, in the in the language space, I mean, there's a ton of languages where we don't have good machine translation technology.
[941.28 --> 949.46]  But there's also a ton of languages where, you know, these languages exist and they represent a certain view of the world and they're endangered.
[949.70 --> 956.38]  And, you know, UNESCO has said, like, we need to preserve these languages and and other organizations have said that.
[956.82 --> 964.08]  But a lot of these languages don't they may not even have written languages or written scripts or anything like that.
[964.12 --> 965.24]  They're just spoken languages.
[965.24 --> 979.32]  And so the fact that we could maybe use some of these techniques to document languages, to learn about languages or even sign languages using computer vision and other things, all of those are are pretty exciting to me.
[979.80 --> 980.54]  That sounds pretty cool.
[980.54 --> 996.38]  The Data Engineering Podcast is a weekly deep dive on modern data management with the engineers and entrepreneurs who are shaping the industry.
[996.38 --> 1004.96]  Go behind the scenes on the tools, techniques and difficulties of data engineering so you can learn and keep up with the knowledge to make you and your business successful.
[1004.96 --> 1012.84]  Can you give a bit of an outline about the motivation for choosing Jupyter Notebooks in particular as the core interface for your data teams?
[1013.22 --> 1019.30]  Yeah. And actually, when I first joined Netflix, it was sort of tossed at me and I was definitely like, well, are we crazy?
[1019.52 --> 1021.20]  And the answer was like, we might be a little crazy.
[1021.70 --> 1028.02]  Go to dataengineeringpodcast.com to listen, subscribe and share it with your friends and colleagues.
[1034.96 --> 1051.84]  So we were talking a few minutes ago about kind of NLP techniques being applied in particular to deriving the rules from, you know, kind of ancient games and such.
[1052.22 --> 1057.88]  And I'm going to take that as a rough segue into some of the things that are currently happening in games.
[1058.14 --> 1060.80]  There were two things in particular that I noticed.
[1060.80 --> 1062.90]  One has to do with DeepMind.
[1063.20 --> 1075.34]  And there is an article that Ars Technica has called DeepMind AI is secretly lurking on the public StarCraft 2 1v1 ladder.
[1076.24 --> 1086.96]  And, you know, over the last few years, talking about DeepMind and StarCraft and that link in terms of, you know, them having StarCraft being played by DeepMind a few years ago.
[1086.96 --> 1090.20]  And now they're kind of doing a second version of it that's really interesting.
[1090.80 --> 1100.48]  In that article, they're talking about the fact that they're having AlphaStar playing it, play the game in an anonymous fashion.
[1101.10 --> 1107.78]  And they've done a bunch of limitations on it to make it more like the way the human would play it.
[1107.78 --> 1119.06]  Some of the things that they had noted in it was the fact that the last time around, DeepMind was able to utilize the entire game all at the same time.
[1119.06 --> 1124.60]  So it kind of had an unfair advantage over the humans in that it could do anything and see everything at the same time.
[1124.60 --> 1134.10]  And one of the things that they're talking about now is they're talking about limiting it on what it can do from an action standpoint, you know, in terms of acting.
[1134.50 --> 1138.52]  They're limiting it so that it essentially cannot outact humans.
[1138.52 --> 1145.76]  And they're also focusing really on the camera view for the game instead of having that kind of holistic view of the game.
[1145.92 --> 1150.12]  So I thought that was really interesting in that there is they implement these characters.
[1150.12 --> 1151.46]  And, you know, you may or may not.
[1151.70 --> 1158.68]  When you have a group of people in the game, you may be playing with obviously humans, but you also may be playing with non-humans now and have no idea.
[1159.34 --> 1160.52]  What do you think of that, Daniel?
[1160.52 --> 1162.98]  I think it's really interesting.
[1163.34 --> 1166.06]  I wonder in the game.
[1166.36 --> 1175.88]  So other than maybe like the screen name or something, I wonder if there's any way, like if they're making it known that this is a bot or anything.
[1175.88 --> 1176.38]  Do you know?
[1176.66 --> 1179.26]  What they said in the article was explicitly no.
[1179.40 --> 1181.22]  They were deliberately doing it anonymously.
[1182.06 --> 1183.66]  And I don't know.
[1183.72 --> 1188.80]  I mean, if you were to say, you know, if you were to communicate and say, you know, are you a human or are you a bot?
[1188.80 --> 1191.64]  If they're just going to lie, if it's a bot says, of course, I'm human.
[1191.96 --> 1193.50]  You know, what a stupid question.
[1193.60 --> 1194.16]  That kind of thing.
[1194.24 --> 1195.72]  I don't know how they're handling that.
[1195.94 --> 1196.16]  Yeah.
[1196.36 --> 1197.90]  I wonder what the perception.
[1198.20 --> 1199.02]  I don't know.
[1199.06 --> 1205.46]  I'd be interested to like read forums and different things around the perception of this, because I definitely think there could be that.
[1205.62 --> 1209.66]  You know, I have brother-in-laws who are really into gaming.
[1209.82 --> 1217.58]  I'm not quite as much, but I know, you know, there's that like when you're playing, especially like ranked games and that sort of thing.
[1217.58 --> 1227.68]  Like, you know, if you're playing against someone that has an unfair advantage, like you were saying, you know, I know that they've tried to limit that, but that could not come off so well.
[1228.40 --> 1234.24]  Like, especially if this player is moving up in the rankings or something like that.
[1234.36 --> 1238.14]  I don't know that that would be accepted very, very well.
[1238.14 --> 1250.78]  Yeah, it explicitly was noting, you know, the fact that they're really putting all those restrictions on and they refer to the previous time around a couple of years back as an unfair, unrestricted view of the game.
[1250.78 --> 1258.82]  And so, you know, as they do that, I find that fascinating, first of all, just because, you know, gaming is a great, obviously a great way to do that.
[1258.82 --> 1266.00]  But there are so many things I could see moving beyond the gaming world, you know, that are out there in terms of general use cases.
[1266.00 --> 1276.46]  I mean, we keep hearing that this we are at this moment where we're going to start interacting with different types of AI models as just a standard course.
[1276.56 --> 1279.06]  And, you know, the first thing that comes to mind is medicine.
[1279.36 --> 1288.44]  You know, and I know we've reported in the past about, you know, that you'll have bots as your primary care physician in within the next few years, like less than five years from now.
[1288.44 --> 1302.10]  And so if they're able to insert these alpha star driven, you know, bot players and they're indistinguishable from the regular player in terms of how you're interacting and what they're capable of doing.
[1302.92 --> 1314.12]  Once again, it really brings us into that that world of of that collaboration, you know, between the human and the AI that we that we see going forward for for some period to come, at least.
[1314.12 --> 1325.06]  Yeah. The one interesting thing about a lot of these video games that they're getting into, and I know this was a topic of discussion, I forget with which with which video game they were talking about this.
[1325.18 --> 1332.40]  But the fact that these video games, there's like multiple, like really interesting problems to solve from the AI perspective.
[1332.40 --> 1341.04]  So if we think about a game that has like character selection, that's like one thing that needs to be solved that like a human would normally do.
[1341.04 --> 1343.76]  There's also like the game play elements.
[1343.96 --> 1353.18]  But then there's even other things like if you really want this agent to behave like a human in a game, there's also like the chat and interaction element, right?
[1353.22 --> 1363.20]  Like, especially in a team play game, if this if this if an agent is playing as a member of a team, there's communication between the team often as well.
[1363.20 --> 1366.36]  So this intersects with a lot of different areas.
[1366.36 --> 1384.26]  And I would actually be pretty surprised, given the state of conversational AI and other things like if, you know, really an AI covering all of those elements at the same time is really in our near term, you know, future.
[1384.26 --> 1388.70]  But but but maybe it is I might be too too skeptical.
[1389.18 --> 1401.26]  Yep. I think I got to say, I would love to to have somebody from from DeepMind who is directly working with with this AlphaStar implementation onto the show and just talk through some of the details of this.
[1401.34 --> 1405.50]  But I just it feels like the implications of how this could be used.
[1405.60 --> 1411.02]  This is a great test case, but I just it really feels like we're turning a corner at this point.
[1411.02 --> 1421.04]  And and I guess while we're mentioning turning a corner, I there was another article that I ran across that has to do with the article is on Polygon dot com.
[1421.32 --> 1426.76]  It was entitled an unbeatable poker bot offers glimpses of video game AI's future.
[1427.12 --> 1430.42]  And really, I saw a lot about this on Twitter.
[1430.80 --> 1433.24]  Oh, good. People were talking about this a lot.
[1433.62 --> 1437.56]  What did you hear before before I leap into my part? I'm kind of curious what the social media side said.
[1437.56 --> 1440.92]  Uh, so I don't remember exactly what they said.
[1441.24 --> 1443.20]  And I didn't look a ton into this.
[1443.24 --> 1444.24]  So you'll have to brief me.
[1444.34 --> 1453.86]  But I just remember seeing as I scroll down on my Twitter feed a bunch of GIFs with this like flow chart of how this thing worked and like poker imagery and all of this stuff.
[1453.88 --> 1456.48]  So it seemed like something that really caught people's attention.
[1457.14 --> 1462.64]  Yeah. The thing that the article really raises is that they kind of took a different approach with this bot.
[1462.64 --> 1474.46]  Um, and so instead of the model kind of having the long term, you know, strategic game view, they limit it to thinking only, you know, two or three moves ahead.
[1474.90 --> 1479.86]  Um, so once again, it's in a sense, it's almost coming down to some human limitations that we have.
[1479.96 --> 1486.24]  But the thing that really jumped out about this was they trained this bot to be able to bluff effectively.
[1486.24 --> 1489.92]  And, um, what I didn't know, and I'm not, uh, I'm not generally.
[1490.06 --> 1492.22]  What does that mean in an electronic sense?
[1492.52 --> 1493.94]  Like it has no face, right?
[1494.30 --> 1496.64]  Yeah, I, I'm actually, it's a good question.
[1496.72 --> 1497.26]  I'm not sure.
[1497.46 --> 1510.48]  Um, I think what they were kind of talking about in it though, was that, um, I think it's just based on the action, you know, so that even if you're not sitting around a table, seeing faces, you know, whatever, someone out there is saying, whether they're holding or, or doing whatever.
[1510.48 --> 1523.44]  And I'm not a poker player, so I, I don't want to humiliate myself by trying to, uh, to jump into that, but, uh, basically it's indicating that by only looking two or three moves ahead, it changes how bluffing would occur.
[1523.66 --> 1531.26]  Uh, and there was, there was something in the article saying that if, if it had taken a longer view of the game, the way it would bluff would be different and it would be distinguishable.
[1531.26 --> 1538.00]  It's different from human action because it's taken a different view than what humans would do, which are typically looking just a few, uh, a few moves ahead.
[1538.00 --> 1548.30]  Um, and so this could accommodate, it could bluff, it could, it could accommodate, um, what humans that are playing against it are doing, whether they're bluffing or not.
[1548.40 --> 1556.14]  And so I think that was what really made it stand out as a different type of model from some of these that we've seen before and reported on in some cases.
[1556.68 --> 1561.82]  Um, but yeah, uh, so we're, we're teaching AI to, uh, to bluff its way through, to lie.
[1562.64 --> 1563.12]  Interesting.
[1563.12 --> 1575.28]  Is it, uh, is this like active in some type of, uh, you know, some type of online poker play site or is it just kind of an experiment at this point?
[1575.62 --> 1577.34]  I didn't see it.
[1577.46 --> 1579.12]  I'm looking back through the article right now.
[1579.26 --> 1581.90]  I didn't see it being deployed.
[1581.92 --> 1584.50]  So I'm assuming it's in a very controlled environment.
[1584.90 --> 1591.82]  Um, but, but who knows, you know, sometimes, uh, sometimes I, I go out to Vegas for various conferences and such,
[1591.82 --> 1599.26]  and you never know, you may walk into a casino at some point, uh, and be playing against the bot or at least one of the, one of the, that'd be one of the players up there.
[1599.34 --> 1600.50]  That's the new, the new gimmick.
[1601.10 --> 1601.26]  Yeah.
[1601.26 --> 1610.92]  Uh, I'm also struck in the article I was kind of reading through as you were, as you were talking and they say that, uh, there was also like an advantage they saw.
[1610.92 --> 1619.68]  So they, they trained the model, I guess, on a 64 core server with less than 512 gigabytes of RAM.
[1619.68 --> 1625.28]  Um, the saying that the cloud servers to train up the program would cost only $150.
[1625.86 --> 1630.28]  So I think that that's a really interesting point and consistent with some other things.
[1630.48 --> 1636.88]  Um, so I, I've seen, uh, of course, fast.ai and, and Rachel Thomas and other people talking.
[1637.38 --> 1638.78]  Um, I think it was her.
[1638.90 --> 1645.18]  I saw it recently with a slide about, you know, how to do innovative AI things.
[1645.18 --> 1654.08]  It doesn't, you know, requiring a lot of compute isn't always necessary and we shouldn't have that really as a precursor in our mind.
[1654.08 --> 1668.48]  And I really liked that both because, you know, there's a lot of people in the world that just don't have access to train a model on a TPU pod and spend like $7,000 on compute costs to train one model.
[1668.48 --> 1678.24]  Right. Um, so like, I think that that's encouraging that there's some cool stuff like this that's happening with very little cost as far as compute goes.
[1678.74 --> 1686.38]  Um, but also of course, like, you know, these huge large scale, uh, NLP models and other things happening these days.
[1686.38 --> 1689.54]  Um, like the compute cost is, is pretty ridiculous.
[1689.54 --> 1693.58]  And also like the environmental impact of that is, is massive.
[1693.98 --> 1697.66]  Um, which is kind of depressing that like, yeah, I saw that as well.
[1697.72 --> 1709.16]  Along with Bitcoin, we're just like, you know, uh, destroying, uh, you know, racking up all of these energy costs, uh, because of these models that we're training.
[1709.16 --> 1721.50]  Which I don't know that that's like, I, I forget if there's like a study that shows the total percentage of our, of our energy usage or something like that, but it's definitely, you know, something that's contributing a lot.
[1721.50 --> 1731.62]  And in some cases more than it really has to be, because we don't always have to throw a, you know, a TPU pod or a V100 or something at, uh, at a model.
[1731.62 --> 1739.82]  I think there's a lot of interesting things that we can do with limited architecture, which is something that I'm really interested in exploring for sure.
[1739.96 --> 1740.40]  Totally.
[1740.74 --> 1744.26]  Um, and I'm going, you know, I know we're sharing articles, so I'm going off script slightly.
[1744.66 --> 1754.76]  Um, but I've seen the same kind of thing about the amount of compute being just, you know, kind of crazy levels, you know, in terms of environmental damage relative to the benefit we're getting.
[1754.76 --> 1761.66]  I was talking to, uh, and I don't have any of my notes in front of me, um, but I was talking to a professor.
[1761.66 --> 1774.28]  I'm in, I'm in the Atlanta area, uh, at Georgia state, uh, who had been working on, um, basically taking complex models and finding the key, uh, important nodes in them.
[1774.28 --> 1777.64]  He has a technique where it goes through that and it can kind of compress a model way down.
[1777.64 --> 1786.84]  So you can, you can take a really sophisticated model, um, and, and once it's trained, at least to inference much more cheaply than you would have been able to before.
[1787.22 --> 1794.14]  Um, and I know that there's that, that he's doing, and there's a lot of other similar initiatives to try to bring the cost of compute down.
[1794.50 --> 1803.32]  Um, and, you know, I, at some point it might even be worth doing a show on that as pulling some of these different techniques together, um, or talking to some of the experts on this.
[1803.32 --> 1817.02]  But, um, I, I do think that that, that is a giant area of research that, that we're, that the world at large is focusing on is, is being able to do effective, uh, inference at least, uh, and maybe, maybe training without such a catastrophic cost.
[1817.02 --> 1828.96]  Yeah. You make a great point that there's that cost, but also things are moving towards us running AI on more like in the browser and on edge devices on mobile devices.
[1828.96 --> 1835.78]  Um, and at least for the foreseeable future, um, you know, those devices are, are limited hardware wise.
[1835.94 --> 1853.70]  So I think that, you know, privacy wise, it makes sense to run those things in a more optimized way on edge devices, um, in a, in a lot of cases, but also, you know, we should, we should be careful that we're not using, uh, all of this compute as a, as a crutch in some ways.
[1853.70 --> 1868.46]  Um, I was just listening to, uh, our, uh, partner podcast, the, the change log, they had the pragmatic programmers on the, uh, on the show, which, uh, there's this pragmatic programming book, which is, is quite, um, famous.
[1868.46 --> 1880.34]  And, uh, they were having an interesting discussion about hardware limitations and some things like that, that, you know, just, uh, uh, in some ways are, are good and in some ways are, are bad.
[1880.56 --> 1892.92]  Um, and I've talked to, you know, a lot of more experienced programmers that are really glad that they were forced to consider some of those things around like memory constraints and other things like that.
[1892.92 --> 1898.20]  Whereas now we kind of take it for granted, but if we want more, if we want more power, it's just there in the cloud.
[1898.64 --> 1901.64]  Um, and maybe that's not always a great thing.
[1902.14 --> 1914.66]  No, I, it's, uh, we do tend to get very, uh, tunnel visioned, uh, in terms of, you know, we, we're, I know that we have this bias where we're so convinced that, you know, this is world changing stuff and amazing things can come of it and all.
[1914.86 --> 1918.90]  And we tend to forget that, boy, we're using a lot of electricity there, uh, in the background.
[1918.90 --> 1923.50]  So, um, yeah, we need to have a better, uh, more holistic view of the world in that way.
[1931.56 --> 1932.92]  Well, hello there listeners.
[1933.24 --> 1933.68]  How are you?
[1933.84 --> 1935.60]  This is Adam Stachowiak.
[1935.72 --> 1939.36]  If you haven't heard yet, we're launching a new show called Brain Science.
[1939.60 --> 1941.68]  It's a podcast for the curious.
[1941.80 --> 1942.50]  Are you curious?
[1943.00 --> 1948.76]  Because if so, we're exploring the inner workings of the human brain to understand things like behavior,
[1948.76 --> 1953.06]  change, habit formation, mental health, and what it means to be human.
[1953.48 --> 1955.42]  It's brain science applied.
[1955.80 --> 1961.92]  Not just how does the brain work, but how do we apply what we know about the brain that can transform our lives?
[1962.52 --> 1966.80]  Learn more about the show and subscribe at changelog.com slash brain science.
[1966.98 --> 1969.84]  Until then, here's a preview of episode number two.
[1970.04 --> 1971.88]  We're talking about how we're all designed for relationships.
[1971.88 --> 1977.52]  I think about it like scaffolding that as our kids grow and, and it doesn't matter.
[1977.52 --> 1985.72]  Like, I just always want people to have this sense of hope and optimism around like, look, it's not over if you didn't get it in childhood or it didn't fully grow.
[1985.72 --> 1994.20]  Like, neuroplasticity is one of the most amazing and hope-filled things because we can continue to build this and grow all throughout our lives.
[1994.82 --> 2003.82]  And so having another person participate in the development of our own mind, it's sort of helping build neural networks that say,
[2003.82 --> 2011.74]  Hey, I totally understand that you're upset as a three-nager because you did not get ice cream and you think your world is now ending.
[2012.16 --> 2018.86]  But to actually, you can still empathize, but that doesn't mean you necessarily give them that desire, right?
[2019.16 --> 2029.12]  Because I don't want them to be conditioned, i.e. I don't want them to have the perpetual feedback that when they're upset, that they just get to have the ice cream that they want.
[2029.12 --> 2038.80]  Right. Let's also say we're using children as an example here because for the audience, that's our breeding ground for research, basically.
[2039.18 --> 2048.38]  You know, I can give an example where my son, you know, he just, I can't recall the exact scenario, but there was a moment where I was like to my wife, I said,
[2048.46 --> 2055.02]  Hey, it's not that he's misbehaving because we were both sort of like in this crazy mode with him and he wasn't behaving.
[2055.02 --> 2062.62]  And I was like, you know what? It's not that he's misbehaving. It's just that he, he can't right now. He's just too far gone. He's too tired. He's too exhausted.
[2063.02 --> 2072.94]  He's overstimulated and his brain is just not developed enough to really get that we're asking him to behave and desiring and expecting him to, but he's just not capable.
[2072.94 --> 2083.48]  So that moment we both sort of just curled into ourselves and just cuddled him and just was just, you know, loving to him rather than like, why can't you get this? Come on, three major, do this.
[2083.60 --> 2088.72]  You know what I mean? Like, you know, so our breeding ground and research is our children.
[2090.08 --> 2100.42]  Right. Exactly. And, you know, I, in my line of work, I mean, I will see the people where this sense of attachment and connection and feedback loop didn't go so well.
[2100.42 --> 2104.92]  And so they've learned, I always say it's sort of like they jerry-rig things.
[2105.38 --> 2110.66]  Like they learned how to best function in their lives as well as they could.
[2110.76 --> 2116.52]  But we, we know this whenever we jerry-rig something and don't actually fix it the way it was supposed to be, what happens?
[2116.94 --> 2117.96]  It breaks down.
[2118.74 --> 2122.64]  Well, if you like what you hear, you should go to changelog.com slash brain science.
[2122.74 --> 2125.30]  The show is not out yet, so don't get too excited.
[2125.30 --> 2130.34]  But you can subscribe and be notified as soon as the show launches.
[2130.90 --> 2133.92]  Once again, changelog.com slash brain science.
[2133.92 --> 2159.52]  I wanted to follow up on one thing that we talked about in a recent episode and a fully connected episode, actually, which was deep fakes.
[2159.52 --> 2169.80]  And I think in that episode, and of course, in general around this topic, there's pretty much a negative view of this technology.
[2170.62 --> 2176.44]  You know, GANs are bad and like they're destroying everything that's real in the world sort of viewpoint.
[2176.44 --> 2185.80]  And in that show, we talked about like, oh, well, what are some of the potentially beneficial things that this technology could do?
[2185.86 --> 2187.84]  And I remember talking through a couple things.
[2187.94 --> 2190.60]  We weren't like totally sure on what those were.
[2190.60 --> 2198.78]  But I saw an article, a recent article that took a really good perspective on this.
[2199.04 --> 2200.28]  And I remember it.
[2200.46 --> 2204.82]  I forget what the article was titled, but I remember seeing it mentioned like good GANs.
[2205.36 --> 2215.58]  And for listeners that, you know, want more info on GANs or regenerative adversarial networks, you can listen to our episode on that.
[2215.58 --> 2228.60]  But this article is basically saying that a research group is using GANs and kind of the technology behind deep fakes to actually improve cancer detection.
[2228.60 --> 2235.70]  So the detection of tumors and abnormalities in x-rays and CT scans and MRIs.
[2235.70 --> 2244.92]  So the basic idea is that you would take kind of existing imagery of cancerous tissue.
[2245.16 --> 2247.26]  And you only have so much of that, right?
[2247.32 --> 2250.10]  Like there's only so much data that exists in a nice form.
[2250.40 --> 2253.24]  And so your models are kind of limited to that data.
[2253.36 --> 2263.90]  And similar to what we were talking about at the beginning of the show, people are much more considering kind of semi-supervised and unsupervised methods intersecting various things.
[2263.90 --> 2265.28]  In this case, computer vision.
[2265.28 --> 2283.84]  So what this group did was to use GANs to actually generate new cancerous tissue imagery in the same sort of style to where it like looked pretty much like what a different cancerous imagery would look like.
[2283.84 --> 2297.80]  And so they're kind of using this to create this new data set of simulated data that can help them in training models for what potentially cancerous things will look like, which I think is really cool.
[2298.30 --> 2298.92]  I do too.
[2299.04 --> 2312.28]  And, you know, I'm glad you mentioned that because I think going into that episode where we talked about deep fakes in particular, I know for me, I had just finished watching the congressional hearing on deep fakes and the danger from a national security and all that stuff.
[2312.28 --> 2318.26]  And I think I was definitely in a dark place mentally in terms of going, whoa, and then we sat down and recorded.
[2318.46 --> 2322.42]  So I apologize to listeners if that was a very ominous show.
[2323.48 --> 2328.78]  GANs in particular, I mean, not only, you know, you're talking about the medical application there with cancer.
[2328.78 --> 2331.18]  And I think I actually remember running across that article.
[2331.34 --> 2339.02]  But, you know, in the past, we've talked about lots of different use cases, including, you know, the various types of creativity that can arise from it.
[2339.06 --> 2341.78]  You know, we certainly talked about that Christie's had auctioned.
[2342.66 --> 2344.46]  You can get rich with new artwork.
[2344.74 --> 2345.40]  Yeah, absolutely.
[2345.58 --> 2346.74]  Well, you know, I don't know.
[2346.84 --> 2348.96]  I don't know why we're not focusing on that considering that.
[2349.00 --> 2349.12]  Yeah.
[2349.12 --> 2349.88]  What are we doing, Chris?
[2350.02 --> 2350.96]  What are we doing, man?
[2350.98 --> 2353.54]  We could be making a ton of money with GAN-based artwork.
[2353.54 --> 2360.40]  I guess maybe it's more meaningful to cure cancer, although I guess, you know, there's no cure for cancer but to help treat cancer.
[2360.90 --> 2361.80]  You know what?
[2362.08 --> 2366.54]  Okay, I'm going to give up my greedy fascination with AI-based artwork.
[2366.56 --> 2367.42]  Which one is better?
[2367.88 --> 2368.02]  Yeah.
[2369.14 --> 2372.40]  So, but it's interesting as we're seeing these leaps ahead.
[2373.38 --> 2378.70]  So I think the GANs are going to be a big area of growth over the next few years.
[2378.70 --> 2386.86]  And I think that, you know, while some deepfake use cases are certainly on the negative side, I think we'll also see deepfakes that are being used in pretty creative ways.
[2387.26 --> 2389.62]  It is a learning – it was pointed out to me after that episode.
[2389.76 --> 2402.74]  I was talking to somebody at the Atlanta Deep Learning Meetup, and they were pointing out that, you know, gaming and that there's lots of educational uses where you change up use cases to teach somebody, you know, kind of dynamically on the fly.
[2402.74 --> 2408.38]  And, you know, there are tons of good potential uses as well.
[2408.78 --> 2417.44]  So it may just be that, you know, we've had our attention draw to some of the early nefarious things where bad actors have grabbed onto a new technology and done some naughty things with it.
[2417.54 --> 2424.02]  So I think we'll see some pretty good uses of the technology as well, aside from the kind of things that we covered in the previous show.
[2424.02 --> 2431.50]  Yeah, I wasn't really thinking as much about, like, simulated data when we were talking about that, having that discussion.
[2431.76 --> 2437.28]  But now that, like, this – I read through this article and thought through it.
[2437.28 --> 2456.34]  But that's kind of at the forefront of my mind around this topic because, you know, the idea of simulated data, similar to, you know, things we've even already talked about in this podcast, is really valuable as we kind of move into this phase of really focusing on semi-supervised and unsupervised methods.
[2456.72 --> 2462.40]  And I think one of the things that you also found this week had to do with unsupervised learning.
[2462.46 --> 2462.86]  Is that right?
[2463.14 --> 2463.62]  Yeah.
[2463.86 --> 2466.62]  So let me flip over to that one real fast.
[2466.62 --> 2469.72]  They're also in MIT Technology Review.
[2469.84 --> 2471.24]  Wow, we've done a lot of stuff.
[2471.38 --> 2474.12]  Yeah, it's an MIT Technology Review week.
[2474.52 --> 2482.48]  So plug for the great work that they're doing, which is apparently giving us all the information that we're looking at.
[2482.52 --> 2486.78]  Maybe not all the information, but it's certainly – they've been on a roll.
[2486.96 --> 2487.42]  They have.
[2487.54 --> 2488.92]  We keep referring to them here.
[2489.02 --> 2490.46]  So good job to that group there.
[2490.46 --> 2497.68]  One of their articles was called The AI Technique That Could Imbue Machines With the Ability to Reason.
[2497.68 --> 2503.40]  And in it, they had talked to Jan LeCun, who is Facebook's chief AI scientist.
[2503.40 --> 2518.76]  And he has for some time been talking about the fact that the field at large is going to find the future great evolutions of the field in unsupervised learning as opposed to supervised learning.
[2518.76 --> 2535.82]  And he mentions – I'm scrolling down to it – that if we are going to think about kind of how the way humans learn and the fact that we start off being born with a very limited set of knowledge, obviously, coming out of the womb.
[2535.82 --> 2543.28]  And that babies are really – they're not – it's not – they're very little of what a human learns in their process is through supervised learning.
[2543.46 --> 2557.78]  And he also pointed out that very little is done through reinforcement learning in the scheme of things and that it's really self – kind of self-supervised, unsupervised learning, meaning it's self-regulated.
[2558.70 --> 2562.76]  Unsupervised learning is how the vast majority of human knowledge comes about.
[2562.76 --> 2565.84]  And I got to say that I agree with it.
[2566.04 --> 2585.28]  And I actually got interviewed myself a while back by Thomas Reuters, and I was saying essentially the same thing, is that some of the really tough things that we have in this field, such as having the data that we need to train with and accumulating it, you know, are much harder than the actual AI work itself that we're trying to do.
[2585.28 --> 2594.32]  Unsupervised learning presumably gives us a whole world to start exploring out there without these giant obstacles to overcome before we ever get started.
[2594.84 --> 2595.36]  Yeah.
[2596.24 --> 2604.92]  I'm actually working with an intern this summer, and we're working on a sort of language-related graph-based method.
[2605.16 --> 2608.62]  But anyway, we're kind of – what is this?
[2608.70 --> 2611.10]  Like halfway through the summer, I guess, at this point?
[2611.34 --> 2612.14]  Roughly, yeah.
[2612.14 --> 2615.98]  And, you know, we're still on the data issues of the problem.
[2616.14 --> 2620.00]  And I'm sure everyone that's actually worked on these problems can sympathize.
[2620.16 --> 2625.80]  Those are really – the bulk of the issues is often the data side of things.
[2625.80 --> 2643.82]  I'm thinking about another conversation I had with someone just yesterday where we were talking about, you know, how we basically just all, like, lost any confidence in any data that we ever receive or confidence in having good data.
[2643.82 --> 2653.16]  Because, like, regardless of the process behind the data, like, even if there's a good process in place, humans are generating data and they're, like, biased in how they do it.
[2653.16 --> 2663.66]  And so almost any data set that we get, even if it's, like, nicely formatted, I kind of just lost confidence in all of that, which is kind of – it's kind of depressing.
[2663.90 --> 2674.42]  But it's also kind of encouraging that people are really saying at this point, well, maybe we should focus on that less and focus more on this sort of semi-supervised or unsupervised approach.
[2674.42 --> 2681.52]  Yeah, before turning to that, I'll agree with – I've been spending a lot of time focused on AI ethics lately at work.
[2681.72 --> 2688.40]  And I think it is a fair statement to say that an enormous amount of data out there is inherently biased in various ways.
[2688.72 --> 2693.26]  And so we're certainly going to need to address with tooling how we approach that.
[2693.90 --> 2695.60]  We can talk about more of that later.
[2695.68 --> 2697.58]  I know we're going to have that as a topic in the future.
[2697.76 --> 2700.08]  Yeah, biased or even just, like, bad.
[2700.08 --> 2704.66]  Like, in some cases, data sets I've got, like – and it looks good.
[2704.84 --> 2707.00]  Like, there's a field labeled this.
[2707.26 --> 2709.52]  And, like, it's a good name for the field.
[2709.92 --> 2713.96]  And it's, like, you know, language identifier or something like that.
[2713.98 --> 2715.86]  I'm, like, oh, that's what this field means.
[2715.92 --> 2717.20]  And that's how everybody used it.
[2717.26 --> 2721.42]  But then I find out, like, later on, oh, that didn't mean the same thing to everybody.
[2721.42 --> 2724.64]  And they input all sorts of crap into that field, right?
[2724.68 --> 2726.40]  So it's, like, it's bias.
[2726.58 --> 2727.50]  It's, like, bad data.
[2727.60 --> 2729.22]  It's, like, everything's messy.
[2729.22 --> 2738.40]  So if everything's already messy, like, you know, unsupervised methods and these other things, you know, maybe that's where we need to put more focus.
[2738.86 --> 2738.96]  Yeah.
[2739.12 --> 2743.98]  And as Lacoon points out, he notes, and I'll quote, he said,
[2743.98 --> 2769.04]  And he has a great point there.
[2769.04 --> 2777.96]  We have these amazing biological models that have inspired us, but we're actually not very close to them currently in the vast majority of work we're doing.
[2778.10 --> 2782.62]  And maybe some of the work that comes out of that will lead to some pretty big breakthroughs.
[2782.68 --> 2783.74]  I'm rather hopeful there.
[2784.16 --> 2785.44]  Yeah, it's good to be hopeful.
[2785.66 --> 2788.34]  And a great point to end on.
[2788.34 --> 2796.74]  As we do in these fully connected episodes, we like to go through some of this news stuff and updates and all of that good stuff.
[2797.06 --> 2803.42]  But also, part of what we want to do in these episodes is point you to some good learning resources that we run across.
[2803.42 --> 2816.48]  So as you're trying to learn about these methods that we're talking about, I'm always looking for new things, new ways to learn things, because there's so much information and so many methods to learn.
[2817.06 --> 2823.58]  So we'll spend the last couple minutes here just going through some good learning resources that we've found recently.
[2824.08 --> 2831.58]  Chris, have you found anything recently that's been interesting, either that you've gone through or that you're interested in exploring a little bit more?
[2831.58 --> 2839.96]  Yeah, so one that I saw was Google Cloud on their blog had a blog that is deep learning containers.
[2839.96 --> 2844.34]  And then the subtitle says build your deep learning project quickly on Google Cloud, obviously.
[2844.74 --> 2858.54]  And what they're really focusing on there is if you're in their ecosystem, and obviously there's the pull that each of the major providers has, that they have a number of containers that are Docker containers that give you complete environments.
[2858.54 --> 2863.40]  And the purpose there is to be able to have a standardized environment.
[2863.96 --> 2866.24]  And I know the other providers are doing that as well.
[2866.34 --> 2880.20]  And I really wanted to call that out, is that standardization on the same thing that the software development world is on Docker containers kind of becoming the de facto atom of work, if you will, about how people are getting things done.
[2880.46 --> 2881.62]  Everything cloud native.
[2881.62 --> 2882.38]  Yeah, really.
[2882.38 --> 2887.12]  And so, and you can pull them onto your laptop and have the same environment.
[2887.46 --> 2901.20]  And in this case, Google is just talking about the fact that they have a bunch of deep learning containers of various configurations with different frameworks and different configurations that they found that their data scientists and deep learning engineers are needing on a regular basis.
[2901.20 --> 2910.82]  And so, I really, the reason I wanted to talk about this today and draw it out as a learning resource is the fact that this is really how things are getting done.
[2911.06 --> 2917.44]  Most of the organizations I've been in have been container-based over the last couple of years, last two or three years.
[2917.58 --> 2920.54]  And they're really focused on how do we want to do it?
[2920.58 --> 2921.90]  And they develop a standard.
[2921.90 --> 2931.80]  And so, if you're not doing that, if it's something that you need to ramp up on, maybe you're stronger on the data science side and containers are still feeling kind of newish to you, this is a good area to jump into.
[2931.94 --> 2932.60]  Read this article.
[2932.92 --> 2936.84]  There's similar ones out there from AWS and Microsoft.
[2937.32 --> 2944.14]  And understand how you can accelerate what you're doing by using standardized containers that give you a full environment.
[2944.14 --> 2956.08]  Well, in looking and thinking about learning resources, what stuck in my mind was a conversation we had with Joel Gruse, which I think is the previous episode to this episode and how they'll be released.
[2956.54 --> 2962.54]  But he wrote this book, Data Science from Scratch, which we've referenced actually quite a few times on the show, I believe.
[2962.96 --> 2964.18]  So, that's a great learning resource.
[2964.18 --> 2970.76]  But along with that, I was kind of looking at other things online that were from scratch.
[2970.94 --> 2974.36]  So, kind of this idea of learning things by coding things from scratch.
[2974.52 --> 2982.40]  And I ran across this NumPy ML repo on GitHub, which seems to have drawn quite a bit of attention.
[2982.58 --> 2988.76]  But I really hadn't seen since, you know, until I ran across it just in the last couple of days.
[2989.18 --> 2991.62]  And there is a ton of stuff in there.
[2991.62 --> 2997.72]  So, it's basically a bunch of things that are implemented from scratch with NumPy.
[2997.92 --> 3001.68]  So, if you're working in Python, there's this library called NumPy.
[3001.88 --> 3008.42]  And you can do, like, matrix-y things and other sort of operations with it, mathematical operations.
[3009.22 --> 3012.36]  And there's just a ton of stuff implemented there.
[3012.80 --> 3013.98]  So, hidden...
[3013.98 --> 3014.62]  Yeah, you're kidding.
[3014.62 --> 3015.58]  Yeah, it's crazy.
[3015.72 --> 3016.36]  I pulled it up.
[3016.42 --> 3017.00]  I'm just, whoa.
[3017.20 --> 3017.44]  Okay.
[3017.88 --> 3020.18]  Yeah, it kind of took me off guard, for sure.
[3020.18 --> 3030.80]  There's, like, you know, LDA, topic modeling, hidden Markov models, neural networks of all types, pre-processing methods, reinforcement learning.
[3031.34 --> 3032.68]  There's various utilities.
[3033.58 --> 3035.44]  Now, I'm sure, like, some of this...
[3035.44 --> 3038.28]  Surely, there's multiple people contributing to this.
[3038.34 --> 3039.76]  It looks like there's six contributors.
[3040.38 --> 3041.44]  So, I'm not sure.
[3041.58 --> 3044.48]  I haven't gone through and looked at, like, the quality of all these things.
[3044.48 --> 3047.40]  But there's definitely a lot of attention that this has received.
[3047.50 --> 3048.92]  There's, like, 5,000 stars.
[3049.20 --> 3055.30]  So, it seems like a reasonable place to go to just check out some things from scratch.
[3055.42 --> 3057.44]  So, I'm definitely going to be checking this out.
[3057.52 --> 3065.24]  And probably, you know, trying to learn from it and pull some of this into workshops and other things that I give.
[3065.58 --> 3068.90]  Yeah, I am bookmarking it even as we speak right now.
[3068.90 --> 3069.70]  Good stuff.
[3069.90 --> 3077.26]  I was convinced by Joel that doing things from scratch is maybe not where you always want to do things.
[3077.38 --> 3080.74]  But it's a good exercise when trying to learn something.
[3080.88 --> 3083.20]  So, I think this is a great resource.
[3084.04 --> 3087.52]  The other things I wanted to mention were a couple of new-ish.
[3087.80 --> 3091.10]  So, one new-ish, one new NLP-related things.
[3091.10 --> 3098.76]  So, as our listeners probably know by this point, I'm trying to learn more about NLP and work in that space a little bit.
[3099.30 --> 3108.26]  But there's a really great course that's free on advanced NLP with Spacey from one of the developers there.
[3108.44 --> 3116.18]  And it looks like a really, really great course and a really nice interface that's all integrated with nice notebooks and all of those things.
[3116.18 --> 3124.58]  And also, Fast.ai, which has just a ton of other great resources, have introduced an NLP course.
[3125.06 --> 3137.68]  So, a code-first introduction to NLP, which covers a lot of different things, but including things like transfer learning, issues of bias, text generation, attention, and the transformer.
[3138.32 --> 3140.32]  So, all sorts of great stuff there.
[3140.50 --> 3143.88]  So, check that out if you're interested in those topics as well.
[3144.32 --> 3145.28]  Great finds, Daniel.
[3145.28 --> 3152.46]  Yeah, it's great that people are releasing such amazing quality material for free as well.
[3152.78 --> 3164.14]  And in really great interfaces, there's a lot you can do without having to pay for a college course or pay for expensive books and other things.
[3164.40 --> 3166.72]  There's a lot of good stuff out there.
[3166.72 --> 3174.30]  Yeah, we had – and I wanted to call out that we had an episode just a few episodes back where we talked about how to get into the field.
[3174.52 --> 3181.80]  And we had a long list of educational resources, courses, books, videos, a lot of which were free.
[3181.88 --> 3186.24]  There were some really top-tier things in there that cost nothing other than your time and attention.
[3186.24 --> 3189.58]  And so, we can add a link to that in the show notes as well.
[3190.16 --> 3191.54]  But, yeah, great finds here.
[3192.12 --> 3204.74]  There's never been a better time to jump into this field right now because you can – even if you're tied down, you're working full-time, you have a family, anytime you can get on your laptop to focus on these, you can log into a course.
[3204.88 --> 3205.98]  It doesn't cost anything.
[3206.08 --> 3207.14]  Keep working through it and stuff.
[3207.14 --> 3208.20]  So, it's a good time to do it.
[3208.42 --> 3211.86]  Well, I don't know a better way to end than with that pitch.
[3212.44 --> 3218.62]  So, thank you for – thanks so much for walking through some recent news with me, Chris.
[3218.68 --> 3220.84]  It was great to talk again, as always.
[3221.36 --> 3224.06]  And I wish you luck with your drones.
[3224.46 --> 3226.12]  We're going to go have some fun flying them.
[3226.22 --> 3227.54]  I'll see you next week.
[3229.58 --> 3230.08]  All right.
[3230.14 --> 3232.74]  Thank you for tuning into this episode of Practical AI.
[3232.74 --> 3234.48]  If you enjoyed the show, do us a favor.
[3234.60 --> 3235.18]  Go on iTunes.
[3235.32 --> 3235.98]  Give us a rating.
[3235.98 --> 3238.12]  Go in your podcast app and favorite it.
[3238.24 --> 3240.94]  If you are on Twitter or social network, share a link with a friend.
[3241.02 --> 3243.38]  Whatever you got to do, share the show with a friend if you enjoyed it.
[3243.68 --> 3246.34]  And bandwidth for ChangeLog is provided by Fastly.
[3246.46 --> 3247.90]  Learn more at Fastly.com.
[3248.08 --> 3251.28]  And we catch our errors before our users do here at ChangeLog because of Rollbar.
[3251.56 --> 3253.90]  Check them out at Rollbar.com slash ChangeLog.
[3254.22 --> 3256.70]  And we're hosted on Linode cloud servers.
[3257.04 --> 3258.68]  Head to Linode.com slash ChangeLog.
[3258.78 --> 3259.22]  Check them out.
[3259.30 --> 3260.12]  Support this show.
[3260.48 --> 3263.74]  This episode is hosted by Daniel Whitenack and Chris Benson.
[3263.74 --> 3266.28]  The music is by Breakmaster Cylinder.
[3266.70 --> 3270.10]  And you can find more shows just like this at ChangeLog.com.
[3270.20 --> 3272.20]  When you go there, pop in your email address.
[3272.50 --> 3276.86]  Get our weekly email keeping you up to date with the news and podcasts for developers in
[3276.86 --> 3278.52]  your inbox every single week.
[3278.86 --> 3279.68]  Thanks for tuning in.
[3279.80 --> 3280.60]  We'll see you next week.
[3280.60 --> 3280.70]  Bye.
[3280.70 --> 3281.16]  Bye.
[3281.16 --> 3281.68]  Bye.
[3281.68 --> 3282.16]  Bye.
[3282.16 --> 3282.22]  Bye.
[3282.22 --> 3282.68]  Bye.
[3282.68 --> 3282.78]  Bye.
[3282.78 --> 3283.22]  Bye.
[3283.74 --> 3283.84]  Bye.
[3283.84 --> 3284.22]  Bye.
[3284.22 --> 3284.80]  Bye.
[3284.80 --> 3284.86]  Bye.
[3284.86 --> 3285.36]  Bye.
[3285.48 --> 3285.80]  Bye.
[3285.80 --> 3285.84]  Bye.
[3285.84 --> 3286.28]  Bye.
[3286.28 --> 3286.42]  Bye.
[3286.42 --> 3286.90]  Bye.
[3286.90 --> 3286.98]  Bye.
[3286.98 --> 3287.48]  Bye.
[3287.48 --> 3287.80]  Bye.
[3287.80 --> 3287.96]  Bye.
[3287.96 --> 3288.94]  Bye.
[3288.94 --> 3289.62]  Bye.
[3289.62 --> 3290.00]  Bye.
[3290.00 --> 3290.02]  Bye.
[3290.02 --> 3290.66]  Bye.
[3290.66 --> 3291.54]  Bye.
[3291.54 --> 3291.92]  Bye.
[3291.92 --> 3292.06]  Bye.
[3292.06 --> 3292.62]  Bye.
