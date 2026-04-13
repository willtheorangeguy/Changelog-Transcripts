[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[17.46 → 20.04] This episode is brought to you by DigitalOcean.
[20.38 → 25.14] DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[25.14 → 36.82] They have an intuitive control panel, predictable pricing, team accounts, worldwide availability with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[37.08 → 42.54] DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[42.90 → 46.34] Head to do.co slash Changelog to get started with a $100 credit.
[46.64 → 48.80] Again, do.co slash Changelog.
[55.14 → 65.64] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical, productive, and accessible to everyone.
[66.02 → 70.54] This is where conversations around AI, machine learning, and data science happen.
[71.02 → 75.28] Join the community and snag with us around various topics of the show at changelog.com slash community.
[75.60 → 76.44] Follow us on Twitter.
[76.54 → 78.04] We're at Practical AI FM.
[78.30 → 79.34] And now onto the show.
[79.34 → 92.54] Welcome to another fully connected episode of the Practical AI podcast, where Daniel and I keep you fully connected with everything that's happening in the AI community.
[92.74 → 98.90] We'll take some time to discuss the latest AI news, and we'll dig into learning resources to help you level up on your machine learning game.
[99.02 → 100.04] My name is Chris Benson.
[100.30 → 102.68] I'm principal AI strategist at Lockheed Martin.
[102.68 → 107.76] And with me, as always, is Daniel Whiten ack, a data scientist with SIL International.
[107.96 → 108.80] How's it going today, Daniel?
[109.34 → 110.00] It's going great.
[110.14 → 113.64] It was, you know, a cold and rainy slash snowy weekend.
[114.02 → 121.16] But on the good side, as some of our listeners will know, we had a season in our household of flu and sickness.
[121.16 → 122.54] And that's kind of ending.
[122.74 → 125.00] So very, very happy about that.
[125.24 → 126.70] You know, no coronavirus yet.
[126.96 → 127.72] Oh, yeah.
[127.92 → 130.10] Well, I was about to make a joke.
[130.14 → 131.44] Welcome back to the land of the living.
[131.44 → 137.36] But, you know, yeah, with that in the news right now, as we're recording this, that's been a big thing the last few days.
[137.36 → 137.88] Yeah.
[137.88 → 138.02] Yeah.
[138.28 → 142.56] And I know you pointed a link to me earlier, which was pretty interesting for our listeners.
[142.56 → 143.80] You want to tell people about that?
[143.80 → 147.94] I was just scanning across news articles, and it was actually on Wired.
[147.94 → 155.52] And it noted a couple of days ago, it says the title is an AI epidemiologist sent the first warnings of the Wuhan virus.
[155.74 → 161.70] And so which is the virus that started in China and is spreading to some parts around the globe as a type of coronavirus.
[161.70 → 176.20] And I think the short part of the article is that there's a company called Blue Dot who has algorithms that take a lot of data sources, you know, from health and airline ticketing data and such to predict the spread of disease.
[176.48 → 179.42] And in this case, they really kind of got there first.
[179.42 → 187.06] And it was actually on December 31st before New Year's, they actually sent out their first note that this outbreak was expected.
[187.30 → 196.20] And it was another really another week before here in the U.S., the CDC, which is the U.S. Centres for Disease Control and Prevention, got the word out.
[196.34 → 202.24] And so it was a case of I don't know the detail of their algorithm, but they refer to it as an AI driven algorithm.
[202.24 → 204.34] And they got those first reports out.
[204.46 → 206.18] So we like to talk about AI for good.
[206.30 → 210.86] That certainly seems like a good thing to get early warning of a major outbreak like this.
[211.28 → 211.78] Yeah, definitely.
[211.88 → 213.96] It's its a fascinating thing.
[214.14 → 218.20] And in some ways, it seems very much science fiction to me.
[218.36 → 218.66] Yeah.
[219.14 → 229.22] Like their kind of, you know, like movie, like over detecting all of these signals around the world and correlating them to say there's going to be this pandemic or whatever.
[229.22 → 236.62] Their article says that they scour foreign language news reports, animal and plant disease networks.
[236.74 → 238.52] I'm not quite sure what that network is.
[238.72 → 241.42] Official proclamations and other things like that.
[241.50 → 243.02] So it's its definitely pretty interesting.
[243.02 → 244.72] And they're they're really doing this.
[244.80 → 245.56] It's pretty cool.
[245.86 → 250.58] If anyone knows anyone at Blue Dot out there, we'd love to have them on the podcast to discuss that.
[250.70 → 252.44] Maybe we can make that happen sometime soon.
[252.84 → 253.70] That sounds fantastic.
[253.70 → 254.22] Yep.
[254.46 → 263.22] Timely news about AI having an effect on the world and possibly able to save lives, especially as they gain notoriety and others start really watching them.
[263.30 → 264.52] It might make a big difference.
[264.86 → 272.08] So, yeah, I mean, I think we're really over the next few years, you know, the way AI is really revolutionizing, you know, medicine at large.
[272.22 → 274.38] You know, this is one of many of those cases.
[275.00 → 275.22] Yep.
[275.22 → 285.10] So speaking of how AI is revolutionizing things, you also found an interesting thing that we're going to talk about today on our fully connected episode.
[285.10 → 296.60] The goal of these episodes, again, just being to keep in the news, the AI news and keep ourselves updated, but also our listeners and kind of dive into the topics that people are currently looking at.
[296.60 → 313.60] And Stanford's Human Centred AI Institute, in partnership with a variety of others, came out with an AI index report 2019, which kind of provided a lot of I mean, we did a sort of top five things of 2019, I think.
[314.08 → 319.02] But that wasn't really based on rigorous research and data collecting and that sort of thing.
[319.02 → 326.20] This was more of actually, you know, who published articles, what's going on in the AI world as we move into 2020.
[326.62 → 331.54] And there were some interesting things in there, I think, that would be great for us to dive into.
[331.66 → 333.04] So that's what we're going to do today.
[333.52 → 335.48] Yeah, it's quite a lengthy document.
[335.78 → 339.78] I haven't counted, but I think, you know, somewhere, what, 150-ish?
[340.08 → 341.92] I think 291 pages.
[342.14 → 343.24] I was far short.
[343.36 → 343.54] Okay.
[343.70 → 343.90] Yeah.
[344.12 → 344.94] It was quite long.
[344.94 → 349.62] I didn't look at the page line, but they had, yeah, they broke things out into a number of sections.
[349.92 → 357.20] And it was a fascinating kind of overall view of kind of the world of artificial intelligence in general.
[357.20 → 359.72] And gave a lot of statistics and facts.
[360.12 → 361.76] The breakdowns were pretty interesting, actually.
[362.44 → 362.54] Yeah.
[362.64 → 369.72] And they have, I'm just looking at the steering committee here from Stanford, also McKinsey Global Institute,
[369.72 → 375.34] Partnership on AI, Harvard, OpenAI, MIT, SRI International.
[375.86 → 378.30] So it wasn't just Stanford that put this together.
[378.56 → 382.90] They also mentioned partners of Google, PwC, and others.
[383.34 → 390.10] So yeah, it'll be interesting to see what they think were the noteworthy things that are happening now in AI.
[390.56 → 397.16] Some of which are maybe different from the things that we talked about in that, you know, first episode of the new year.
[397.34 → 399.18] So yeah, let's go ahead and dive in.
[399.18 → 403.82] And it looks like the first section of what they talk about is research and development,
[403.82 → 411.36] which I know both of us aren't professors or anything like that or involved in academic research in that context.
[411.36 → 414.30] But we both interact with research people.
[414.80 → 418.36] What, if anything, kind of surprised you by what they talked about, Chris?
[418.80 → 423.36] Well, you know, they started off kind of really focusing on how much growth there had been in the space.
[423.36 → 426.22] And I don't think that was surprising in itself.
[426.22 → 432.20] But we've really seen the rise of China in terms of just raw numbers of publications coming out.
[432.44 → 434.46] And as part of that, they finally passed Europe.
[434.74 → 437.42] They had previously passed the U.S. already.
[437.42 → 449.18] And so, you know, we're still seeing that, I guess, despite the fact that you're seeing those raw numbers, the fully weighted citation impact, though, of U.S. publications is still about 50% higher than China's.
[449.34 → 450.98] And that really rang true.
[450.98 → 456.22] I was actually in an internal artificial intelligence meeting last week with my employer.
[456.46 → 460.86] And we actually were discussing that specifically, just the fact that you're seeing more citations.
[461.20 → 463.90] The discussion was in terms of the quality.
[464.22 → 468.48] And obviously, we were speculating on why that is and when that might change going forward.
[468.48 → 476.44] Yeah, and I think actually on our next episode, we're going to be talking to someone from the Semantic Scholar team at Allen AI.
[477.16 → 485.66] And of course, that project is really concerned with discoverability of research and kind of weeding through the noise and all of that sort of thing.
[485.66 → 504.04] So that'll be interesting to talk to them about how this, you know, this giant surge in research and archive papers and all of those things has increased and in some ways made it hard to find, you know, the real, you know, notable things that are happening in some cases.
[504.04 → 517.08] I thought, you know, another thing that was interesting was that they noted several small countries that were having a relatively high increase in deep learning papers in terms of per capita.
[517.34 → 522.66] So these are countries like Singapore, Switzerland, Australia, Israel, Netherlands, Luxembourg.
[522.66 → 539.42] They're talking about these countries who, despite their small size, are really kind of, I guess, making AI research or encouraging AI research and believing in that as a future driver of economic prosperity and innovation and all of those things.
[539.72 → 540.52] Yeah, it's interesting.
[540.76 → 542.16] And we've talked about this before.
[542.30 → 545.12] You know, I know we've talked specifically about Singapore.
[545.50 → 549.46] It was very obvious to me about a year ago when I was in Switzerland for a conference.
[549.46 → 562.34] These countries have really kind of committed to some degree, maybe their national identity a little bit to saying, hey, this is something that we're going to do, you know, technology in general and specifically AI in a lot of these cases.
[562.84 → 566.10] Do you think, I mean, obviously, we're both pro AI, I think.
[566.10 → 578.74] I wonder just kind of off the top of my head if that's kind of making a dent in other research areas in terms of taking away funding or putting the focus less on other still very important areas.
[578.98 → 589.38] But now that everybody's kind of all in for AI, what effect that's having on sort of more traditional biology and medical research and those sorts of things?
[589.64 → 591.12] That's an interesting idea.
[591.12 → 591.98] Yeah, I'm not sure.
[592.18 → 597.54] I would say that obviously there's a finite amount of, you know, research and development dollars and time.
[597.84 → 599.36] Or whatever your currency is.
[599.48 → 600.94] Yeah, available and stuff.
[601.18 → 607.66] And I suspect as we look at different strategies over time, you know, AI is one of the great enablers of our time.
[607.66 → 614.26] And so I think they may be, you know, selecting certain specialties and then kind of going after AI as an enabler in this.
[614.26 → 625.72] I mean, I know that that's why, at least partly why I'm in industry versus in academia, because I originally wanted to go the sort of professor route and that sort of thing.
[625.72 → 628.42] But I was in physics in grad school.
[628.42 → 632.10] And I mean, physics as a discipline, I think it's exciting.
[632.24 → 633.90] There's a lot of people that think it's exciting.
[633.90 → 648.52] But in terms of like a paradigm shifting things that have happened in recent years, there haven't been a lot in terms of the type of paradigm shifting things in physics of, let's say, the 20s and the 30s and that sort of time period.
[648.52 → 656.78] And so, you know, physics has become a sort of I think it's plateaued in terms of its excitement to some degree.
[656.90 → 661.76] And that's made a lot of the jobs in physics research very competitive, right?
[661.78 → 668.64] Because there's no maybe not as many universities that are really filling their bench with physics people.
[668.90 → 673.72] Maybe they're now filling their bench with computer science, AI type of people.
[673.72 → 679.22] I think it's definitely will be interesting to see how that that plays out on those fronts.
[679.68 → 680.00] Interesting.
[680.22 → 695.66] You know, another interesting note there was the fact that we're seeing, especially in Western European countries, but not limited to that in countries such as the Netherlands, Denmark, Argentina, Canada, and even Iran, a relatively high presence of women that are involved in AI research.
[696.02 → 696.30] Yeah.
[696.34 → 697.66] Where's the US on that list?
[697.90 → 699.74] Yeah, I would ask the same question.
[701.20 → 702.26] What's up with that?
[702.26 → 704.44] Yeah, but it's nice to see this field.
[704.60 → 712.26] I know that that is since the very beginning of this podcast, that's been a big goal of ours is to see this field be a truly equal field in all respects.
[712.48 → 716.04] So that was a stat that caught my eye that I was really thrilled to see.
[716.68 → 723.98] Yeah, I think we need to take note of some of these countries and see what they're doing to promote that and try to increase that more.
[723.98 → 730.64] I know there's been another thing in the next section of the index report is about conferences.
[730.64 → 740.70] And one of the things maybe that has driven that change is they talk about the women in machine learning workshop that happens throughout.
[740.94 → 742.40] I'm not sure how long it's happened.
[742.70 → 749.78] They talk about 2014, but they say that has 20 times more alumni than it had in 2015.
[749.78 → 754.06] And so I think that this is one of the contributing factors.
[754.38 → 766.26] I think it's a pretty big contributing factor that there's been intentional effort to have these sorts of workshops and kind of local chapters and all of these things focused on women in machine learning and AI.
[766.68 → 767.42] Yep, I agree.
[767.72 → 768.50] It's a good sign.
[768.62 → 770.28] It's like a sign that we're moving in the right direction.
[770.28 → 779.16] And, you know, just in general, we're seeing conferences, their popularity and the number of people attending in AI related conferences just exploding.
[779.40 → 779.86] That's insane.
[780.08 → 786.88] Yeah, I mean, Neurons was, I think, upwards of well over 10,000 attendees, I believe, at this point.
[787.10 → 792.18] Yeah, I think it was like almost 14,000, 13,000 something, which is just insane to me.
[792.26 → 792.68] It is.
[793.34 → 795.32] Yeah, I mean, 13,000 people.
[795.32 → 802.48] Like, I don't know what we're going to have to start doing, like to run out like football stadiums or something for AI conferences.
[803.04 → 804.10] Like, what is the future?
[804.18 → 804.60] I don't know.
[804.60 → 809.16] I would say, I mean, one personal note on that is I would love to see.
[809.64 → 816.58] And there was, I think, some of this last year when there's a lot more effort to live stream things.
[816.76 → 821.12] And so I watched several conferences live-streamed at least some of the content.
[821.58 → 822.70] I really appreciated that.
[822.70 → 834.02] And also from an environmental standpoint, if we have 13,000 people taking plane rides to go to a conference, I would love to see that many people involved.
[834.02 → 842.32] But, you know, having live-streaming resources and better live-streaming and remote conference events would be something I would love to see.
[842.64 → 843.08] I would, too.
[843.24 → 852.22] I mean, we're seeing this explosion and being able to participate as we see so many people wanting to get to conferences and, you know, and getting visas rejected.
[852.22 → 853.70] Getting visas rejected.
[853.96 → 856.00] In a lot of cases, just not able to get in.
[856.12 → 859.38] I mean, Neurons is famous for its lottery.
[859.74 → 862.42] And, you know, so many people that would like to go cannot go.
[862.52 → 865.72] And that's despite the massive number of identities it already has.
[866.36 → 877.58] So, yeah, live-streaming would be a fantastic way of being a little bit more inclusive for those who either can't travel or are wanting to be responsible and avoid the environmental impact by getting on a plane.
[877.58 → 878.22] Yep.
[878.22 → 878.38] Yep.
[878.38 → 886.72] The next thing, which is kind of obvious that they would go into this, but the technical performance of AI models has shifted in several ways.
[887.02 → 891.64] Generally, they talk about image classification as an example task.
[891.84 → 902.58] And they talk about how it's, you know, the time required to train these sorts of models has drastically decreased and the cost to train them has drastically decreased.
[902.58 → 912.32] So, there seems to be this sort of more general availability of architecture or of compute resources in the cloud that allow you to train these systems.
[912.48 → 920.98] So, the availability of that, but also efforts to speed this up, maybe architecture or framework or language wise as well.
[920.98 → 927.32] Yeah, you know, we're seeing, you know, I know that one of the topics you and I like to talk about a lot are transformers, for instance.
[927.44 → 936.94] And I've noticed just a few weeks ago, I was talking to some folks, and you'll see these large transformer models come out and then these follow-ups that are huge performance enhancements.
[936.94 → 944.80] And they may, you know, they may reduce the size of the model, but you end up getting a dramatically faster training, you know, based on these optimizations.
[944.80 → 955.06] And I think when you counter that with the fact that we're seeing GPU, TPU and other hardware architectures really, really accelerating, you've got cloud options.
[955.06 → 961.56] You have options for being able to have one, you know, maybe have a GPU right on your desktop that you're working, whatever.
[962.04 → 967.60] And I think, you know, the combination of that has made a huge difference in accessibility for people to be able to actually do these.
[977.40 → 980.76] You like this show, so I bet you'd love listening to Go Time.
[981.06 → 981.86] Not working with Go?
[982.12 → 983.26] Don't fast-forward quite yet.
[983.26 → 989.88] Go Time covers a wide range of topics, including cloud infrastructure, distributed systems, microservices, Kubernetes, and Docker.
[990.26 → 993.84] Here's a ridiculous clip from a recent episode about the defer keyword.
[994.40 → 998.36] I think I really think that Matt missed his calling as a stand-up comedian.
[999.70 → 1000.18] Totally.
[1000.68 → 1001.32] Yeah, funny.
[1001.70 → 1002.76] I mean, he can still be one.
[1002.82 → 1005.16] He just has to choose his audience very wisely.
[1005.26 → 1006.30] It's got to be a tech audience.
[1006.88 → 1009.46] Well, he has Go Time FM.
[1009.46 → 1009.58] Yeah.
[1010.34 → 1014.04] I think the funniest low-key podcast out there.
[1014.26 → 1017.08] Thing is, in tech, no one likes a stand-up comedian.
[1017.30 → 1018.56] You just want them to get on.
[1018.64 → 1019.62] Tell us what you did yesterday.
[1019.80 → 1020.58] Tell us what you're doing today.
[1020.62 → 1022.70] And if you've got any blockers, and get off.
[1023.84 → 1024.50] You know what I mean?
[1024.72 → 1026.52] No one wants the...
[1026.52 → 1027.36] Yeah, there you go.
[1027.40 → 1027.54] See?
[1027.80 → 1028.56] That's why I didn't.
[1029.12 → 1030.24] I'll stick to programming.
[1030.92 → 1032.84] I mean, there's only three people here.
[1033.44 → 1036.20] You might have a whole audience that's live listeners that's laughing right now.
[1036.44 → 1036.74] Oh, yeah.
[1036.76 → 1037.54] Let's assume that.
[1042.34 → 1046.14] I'm pretty sure this could be edited to make me not sound like an idiot.
[1046.14 → 1047.96] You heard Carmen.
[1048.24 → 1049.88] Go Time is low-key hilarious.
[1050.42 → 1055.10] Check it out at changelog.com slash Go Time, or just search for Go Time in Apple Podcasts,
[1055.18 → 1057.30] Spotify, or your favourite podcast directory.
[1057.38 → 1057.92] You'll find it.
[1058.18 → 1060.56] Once again, that's changelog.com slash Go Time.
[1060.56 → 1077.10] So, Chris, I found one fascinating thing in the index report that is related to
[1077.10 → 1078.04] technical performance.
[1078.48 → 1084.46] And if people are following along while they're listening, this is on page 68 of the report.
[1084.62 → 1086.24] So, a good way is in there.
[1086.24 → 1092.12] But they go through and talk about the milestones that have been achieved in terms of human level
[1092.12 → 1097.00] performance and AI reaching or beating human level performance in certain tasks.
[1097.28 → 1099.32] And I hadn't seen something like this.
[1099.42 → 1101.58] Probably are things like this compiled in other places.
[1101.58 → 1107.24] But I thought the compilation and timeline that they compiled here was fascinating.
[1107.46 → 1111.88] So, this starts with Othello back in 1980.
[1111.88 → 1120.20] And it goes all the way to 2019, detecting diabetic retinopathy with specialist level accuracy.
[1120.68 → 1121.44] This is really cool.
[1121.56 → 1124.62] I don't know how many of these things were familiar to you, Chris.
[1124.84 → 1125.88] A few of them are.
[1126.12 → 1127.56] They talk about Alfaro.
[1127.78 → 1131.90] There's a number of them, especially given back when I was doing gaming when I was younger.
[1132.02 → 1135.64] A lot of the older ones, ironically, are more familiar with me than some of the newer ones.
[1135.88 → 1140.26] The ones that have been in the news a lot in terms of AI in the last few years, I'm familiar with.
[1140.26 → 1142.70] But they had some that I had not noticed before.
[1142.90 → 1145.00] The prostate cancer grading I had not seen.
[1145.60 → 1145.70] Yeah.
[1145.80 → 1152.88] So, pre-2011, there are three milestones that they list, which are Othello, Checkers, and Chess.
[1153.46 → 1158.80] And then post-1997, then we skip all the way to 2011.
[1159.10 → 1162.20] And you can kind of see this rapid advance.
[1162.20 → 1172.62] So, there's like between 2011 and 2019, I'm not going to be able to count these, but there's probably at least like 15 or something.
[1173.32 → 1174.36] Yeah, something like that.
[1174.40 → 1181.34] 15 to 20 after that, including things like, you know, Data and video games, machine translation, all of those things.
[1181.34 → 1190.28] And, you know, something I noticed just as a side comment, since it leaps from 97 to 2011, those are the years of the most recent AI winter.
[1190.60 → 1191.88] I almost said nuclear winter.
[1192.04 → 1193.48] It was not a nuclear winter.
[1194.10 → 1196.50] But yeah, the most recent AI winter was right there.
[1196.66 → 1201.60] And you saw zero progress made as everyone turned away from neural networks for those years.
[1201.60 → 1211.28] Yeah, also kind of going back to the conference thing, they have this graph in the report where they track AI conference attendance.
[1211.58 → 1214.44] And you can see, so they track back to 1985.
[1216.08 → 1225.68] And I see, so this is one of those, aside for a minute, this is one of those plots that being slightly colourblind, I have no chance of reading.
[1225.98 → 1229.78] Because all the lines are like colours that blend together for me.
[1229.78 → 1229.90] Nope.
[1230.30 → 1233.76] So just FYI, there's colour palettes out there to help with that.
[1234.02 → 1234.30] Okay.
[1234.46 → 1237.20] But maybe you can help me know which one goes back to 1985.
[1237.62 → 1238.00] Uh-oh.
[1238.00 → 1245.76] There are a couple of conferences back in 1985 that have at or over 5,000 attendees.
[1246.50 → 1252.06] And then you can kind of see as, you know, 1990, 1995, 2000, 2005.
[1252.42 → 1256.90] It actually decreases all the way to about 2010.
[1256.90 → 1259.00] Some of them start to increase again.
[1259.14 → 1265.68] And then, you know, 2015 and on, it's just like skyrocketing attendance in these conferences.
[1266.08 → 1275.26] So it is just historically interesting to see, you know, back then there were these very high profile, you know, 5,000 attendees at a conference is no joke.
[1275.68 → 1275.80] Yeah.
[1276.06 → 1277.08] That's quite a conference.
[1277.08 → 1284.76] And for those of you who haven't been to one that size, I mean, it's just you get lost in them in terms of trying to find your content and everything.
[1285.08 → 1287.06] So I actually prefer smaller conferences.
[1287.06 → 1289.32] They're a lot more intimate, a lot more fun from my standpoint.
[1289.32 → 1290.20] Yep.
[1290.44 → 1300.16] Before we leave the technical performance side of things, one of the trends that I saw them point out, which was interesting to me, and they drew it out in terms of NLP.
[1300.16 → 1317.66] But I think it's true of computer vision in some ways as well, is that in terms of benchmarks, like they had benchmarks for certain tasks in NLP or computer vision, like object recognition or like machine translation or entity recognition, reading comprehension, co-reference, all of these different benchmarks.
[1317.66 → 1332.16] And as they've reached, you know, human level performance on these, they actually had to go like they, I'm meaning the research community or those in the research community, many have had to go back and say, how can we make this more challenging?
[1332.16 → 1338.18] Because we're reaching, you know, we're reaching human level performance in so many of these tasks.
[1338.18 → 1347.12] So, for example, in the AI world, there's this benchmark called Glue, which I'm going to mess this up off the top of my head.
[1347.12 → 1350.54] I think it's general language understanding here.
[1351.02 → 1352.04] Come up with that.
[1352.14 → 1352.94] Something like that.
[1354.32 → 1355.04] Let's see.
[1355.40 → 1356.92] There's Glue and then there's Super Glue.
[1357.14 → 1359.80] So there's general language understanding evaluation.
[1360.04 → 1360.40] There we go.
[1360.76 → 1364.54] And then they had that and then that wasn't enough or that wasn't challenging enough.
[1364.60 → 1366.20] So they reached, you know, human level.
[1366.64 → 1369.64] And this graph is in the index report as well.
[1369.96 → 1377.10] So you can see kind of models surpassing human level performance in Glue, this sort of task that combines a bunch of NLP,
[1377.12 → 1379.20] tasks to make it harder itself.
[1379.42 → 1382.22] And so human level performance was beat there.
[1382.70 → 1387.24] And so then they developed this other one, which is Super Glue, which kind of ups it from there.
[1387.36 → 1394.94] And others like Allen NLP or Allen AI Institute and others are producing other benchmarks to kind of further challenge things.
[1395.08 → 1400.14] So as we've reached a lot of those milestones, now we're kind of in this season of, you know, what's next?
[1400.14 → 1402.20] How do we make this harder for computers?
[1402.44 → 1410.08] And a lot of those things are like common sense, understanding and reasoning that are really hard for computers to do.
[1410.24 → 1412.30] We still have a lot of room for growth there.
[1412.30 → 1421.40] And of course, in, you know, languages other than English and, you know, multimodal settings where we're combining video and imagery and text and all of those things.
[1421.66 → 1424.62] It'll be interesting to see what benchmarks come about there.
[1424.78 → 1425.52] I agree.
[1425.66 → 1432.60] You know, just as a side thought there, we're having a couple of interesting conversations, meaning the community at large right now.
[1432.60 → 1438.00] We're seeing these things that we're calling out here in terms of how far we're coming and having to adjust for benchmarks.
[1438.24 → 1445.92] And then you see people in the kind of artificial generalized intelligence community saying, oh, we need to have completely new models and stuff.
[1446.06 → 1448.32] And I think people tend to get caught up in one or the other.
[1448.80 → 1459.46] It's interesting that in terms of kind of the deep learning basis where we're at right now, we're really still making pretty immense progress in terms of applicability and performance improvements.
[1459.46 → 1464.44] And while that may not be AGI, I think some people tend to get caught up in one or the other conversation.
[1464.44 → 1478.22] I think it's pretty remarkable that we're in an industry where you can have both of those conversations with the specifics of whether we are going fast or whether we are not making much progress at all in the larger scheme of things.
[1478.46 → 1488.26] But I really think it shows how vastly artificial intelligence has moved into culture and society and industry at large.
[1488.26 → 1489.96] That astounds me repeatedly.
[1490.20 → 1494.08] And I think this report on the applicability of these technologies is really amazing.
[1494.26 → 1497.78] Just as you just called out, the fact that NLP is making such fast progress.
[1498.60 → 1504.30] Yeah, sometimes I think we overcomplicate the sort of how much progress are we making.
[1504.54 → 1511.82] I mean, one indication of that is economic investment in AI and application within industry.
[1511.82 → 1514.80] That's another point that they call out in the report.
[1514.80 → 1525.78] And they throw out, you know, really huge numbers like, oh, AI investment was over 70 billion with AI related startup investments over 37 billion.
[1526.04 → 1528.18] Honestly, I mean, I don't know about you, Chris.
[1528.50 → 1529.34] Those numbers don't.
[1530.00 → 1533.76] It's hard for me to grasp those numbers because I've never seen a billion dollars.
[1534.12 → 1534.24] Yeah.
[1534.24 → 1536.58] But it's a lot of money, right?
[1536.88 → 1544.30] And there's definitely they also cite different percentage increases in jobs and AI investment.
[1544.30 → 1547.96] And I'm guessing, you know, some of that may be hype, right?
[1548.16 → 1556.84] But there is actual proof that AI applications within industry are driving a lot of change and people are responding with investment.
[1556.84 → 1558.78] There was a particular stat.
[1559.00 → 1561.40] It's a US centric stat that I noticed.
[1561.56 → 1573.58] And that is the total number of jobs in the economy relative and taking that total number and looking at the share of those that are kind of AI related jobs, or at least in terms of, you know, maybe titles or tangentially.
[1573.78 → 1578.10] It's approaching nearly 1% in terms of AI jobs to total jobs.
[1578.30 → 1582.16] And that's AI jobs, meaning like humans doing AI.
[1582.42 → 1582.88] Correct.
[1583.00 → 1585.56] Not AI doing jobs.
[1585.56 → 1588.86] I'm glad you called that out just for clarity on that.
[1588.94 → 1598.34] But yeah, the number of jobs that we as humans are engaged in that are AI related compared to the total economy, it's approaching 1%.
[1598.34 → 1602.68] And that is remarkable because we're still at such an early stage in this industry.
[1602.68 → 1609.70] And so, you know, you can see, I believe back around 2015, it was just, you know, just a fraction of 1%.
[1609.70 → 1611.58] I think it might have been 0.3%.
[1611.58 → 1620.34] So we are growing so fast in terms of how AI is impacting the economy represented by the number of jobs being created to do just that.
[1621.06 → 1627.38] And job wise, they did a bunch of analysis of LinkedIn, which I found this interesting because they have a lot of.
[1627.38 → 1636.62] So they have asterisks next to like India, for example, because I think they said like 40% of workers in India are on LinkedIn.
[1636.62 → 1642.20] And so that numbers are likely not accurate in that sense.
[1642.32 → 1644.76] If anything, they're kind of diminished, I would say.
[1645.34 → 1656.14] And yet India was kind of at the top of a lot of the job statistics in terms of how many people are involved in AI and also the fastest growth in AI hiring.
[1656.14 → 1668.48] Again, these other countries that have invested heavily as part of their national strategy in AI, like Singapore, Brazil, Australia, Canada, we're right at the top of those AI hiring stats.
[1668.98 → 1673.16] And it's interesting to, I mean, it makes sense with what I've heard.
[1673.26 → 1676.50] So I've got a few people that I work with in Singapore.
[1676.50 → 1684.82] And from what I understand, you know, AI people in Singapore are pretty much snatched up instantly.
[1685.04 → 1689.78] So if you're trying to hire someone in AI in Singapore, there's just so much hiring going on.
[1689.90 → 1700.30] And there's not enough AI people to go around, which is one of the reasons why they establish some of these things like AI Singapore, which is trying to feed AI expertise into industry.
[1700.30 → 1710.24] But there's just so much hiring going on, the demand is so high that AI people, you know, could get hired pretty much right away.
[1710.44 → 1713.32] So if you're interested in getting an AI job, you know, consider Singapore.
[1713.54 → 1714.78] It's a beautiful place.
[1715.06 → 1719.76] Although I don't think it's, they may be the most extreme case, but I don't think it's a problem just for Singapore.
[1719.94 → 1721.12] We're seeing that really everywhere.
[1721.12 → 1733.00] You know, all employers that are invested in AI, which is obviously an increasing number steadily, are contending with that same issue in terms of finding qualified people who can be productive quickly.
[1733.62 → 1739.28] And, you know, so the university system, you know, they're snatching them straight out of universities that are oriented on AI.
[1739.66 → 1742.00] You know, it is just an explosive growth area.
[1742.14 → 1747.58] You mentioned all the billions of dollars a few minutes ago in terms of kind of global private AI investment.
[1747.58 → 1758.72] And, you know, along with that, I was really astounded to see that year over year, the annual growth rate being around 50% in terms of investment in startups is continuing to go.
[1758.90 → 1765.52] And that's despite, you know, various economic worries and things that people are concerned about, about life in general.
[1765.64 → 1769.08] So it's still quite staggering, the explosiveness of the field in general.
[1777.58 → 1789.54] This episode is brought to you by Brave.
[1789.90 → 1791.74] We deserve a better internet.
[1792.06 → 1795.40] That's why the team behind Brave reimagined what a browser could be.
[1795.98 → 1797.84] Brave is like Chrome, the good parts.
[1798.14 → 1799.76] Even your extensions will just work.
[1800.00 → 1803.76] It has built-in ad and tracker blocking, easy anonymization with the Tor network.
[1803.76 → 1807.28] Earn tokens while you browse and use them to tip your favourite creators.
[1807.68 → 1809.26] And did I mention it's lightning fast?
[1809.58 → 1812.18] Turns out the web is superfast when you remove all the cruft.
[1812.52 → 1817.22] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1817.22 → 1829.90] All right.
[1829.98 → 1837.06] So you kind of started into the conversation about education and me being in a university town,
[1837.06 → 1841.32] I also am kind of monitoring this and thinking about it.
[1841.32 → 1849.06] But more people are going to school to learn specifically AI-related things than ever before.
[1849.80 → 1857.30] And, you know, one of the things they talk about is international PhD students pursuing AI specialization in computer science.
[1857.30 → 1858.18] So that's up.
[1858.18 → 1871.88] But also there's this sort of interesting trend of PhDs that are graduating in AI are not going the sort of academic route in general in terms of getting professorships and that sort of thing.
[1871.88 → 1883.12] But there's kind of this drain of AI talent where a lot of these people are going into industry to work at awesome, cool places, whether that be like Google Brain or OpenAI or whatever it is.
[1883.24 → 1892.04] So much so that, you know, AI faculty are leaving academia for industry and that's continuing to accelerate.
[1892.04 → 1898.76] And so that's, you know, exciting in some ways that there's kind of this infusion of expertise into industry.
[1898.90 → 1907.18] But it's also concerning in some ways because, at least from my perspective, it seems like, you know, when I'm thinking about academia,
[1907.90 → 1917.02] this gap between how in touch academia is with industry is kind of separating more and more in certain ways.
[1917.02 → 1928.34] And so, yeah, I would love to see industry and academia be closer and people coming out of university programs, you know, really ready practically to do jobs.
[1928.34 → 1941.48] But I'm not sure that that's really happening because the people, the AI professors in academia that are interested in industry stuff are just leaving to go to industry.
[1941.48 → 1952.12] And then what's left is kind of just, you know, pure academic research, which is interesting, but maybe in some ways less connected to industry problems.
[1952.56 → 1956.58] Yeah, it's really changed both academia and industry, this trend.
[1956.74 → 1959.36] And it's changed the relationships we have.
[1959.42 → 1968.56] And one of the things that I'm involved with at my own employer at Lockheed Martin is I engage a lot of universities in terms of artificial intelligence with that.
[1968.56 → 1970.50] There's a number of us that do this.
[1970.84 → 1982.30] And the nature of those collaborations are changing, whereas once upon a time, you know, you might think of kind of the brain trust at these universities and that industry would access them to help them.
[1982.36 → 1994.20] But we're seeing so many people that, as you pointed out, might otherwise have been on an academic career path are going to industry because of the opportunities and because of the compensation that that has changed.
[1994.20 → 2004.68] And so it's interesting to see the partnerships that we're having between industry and academia where both sides are doing cutting edge research in different topics and collaborating across.
[2005.02 → 2010.98] And you're seeing, you're seeing, you know, a substantial amount of that in industry, whereas it used to be mostly an academic.
[2010.98 → 2014.66] And then industry would kind of take that and apply it to what they're doing.
[2014.78 → 2022.30] But you're this field is moving so fast and the brain drain is happening from academia into industry for those reasons that it's kind of rebalanced that.
[2022.42 → 2025.92] And I think both sides are trying to figure their way through that at this point.
[2026.16 → 2031.96] It's also driven compensation rates through the roof for AI specialties, obviously.
[2032.26 → 2036.54] And so that's and that becomes another thing where different companies are competing for the talent.
[2036.94 → 2038.12] Yeah, it will be interesting.
[2038.12 → 2051.66] I know one of the other things we've talked about before on the podcast is sort of trend to more formalization around data science and AI programs within universities.
[2051.66 → 2064.78] So to where before a lot of universities took the strategy of, you know, AI as a graduate discipline within computer science, which it definitely is and should continue to be.
[2064.86 → 2079.12] There are efforts to kind of embed data science and AI across all organizations with some universities even taking steps to establish, you know, the centre for data science or centre for AI or whatever.
[2079.12 → 2084.54] And there's kind of cross discipline collaborations that happen within those centres.
[2085.24 → 2086.42] So that's interesting.
[2086.68 → 2092.42] I think there's success stories within that and there's not so great success stories with trying to apply that.
[2092.68 → 2099.04] So, yeah, I don't know what all the solution is to this sort of balance between industry and academia.
[2099.04 → 2101.82] And maybe it kind of just flows back and forth.
[2102.00 → 2104.50] But, yeah, it'll be interesting to follow for sure.
[2104.92 → 2105.26] Absolutely.
[2105.76 → 2119.88] So other things that was emphasized in the economic point with the index, but also actually called out as a separate whole chapter in the index report were autonomous systems, specifically autonomous vehicles.
[2119.88 → 2135.50] So autonomous vehicles received the largest global share of or the largest share of global investment over the last year, followed by things like drug cancer therapy, facial recognition, video content, fraud detection, other things.
[2135.66 → 2137.88] But autonomous vehicles were at the top.
[2137.96 → 2141.44] And I know this is something that you've been involved with personally.
[2141.44 → 2144.50] And, of course, Lockheed Martin is interested in.
[2144.92 → 2149.84] But it kind of took me off guard a little bit because you hear a lot about self-driving cars and that sort of thing.
[2149.94 → 2159.58] But it doesn't seem to me to have penetrated markets as much as something, let's say, like facial recognition or computer vision.
[2159.58 → 2162.16] And yet it's at the top of investment.
[2162.58 → 2163.58] I think you will, though.
[2163.58 → 2173.88] You know, one of the things that was notable is that the state of California, you know, licensed testing for over 50 companies with an enormous number of autonomous vehicles.
[2174.40 → 2177.66] And they noted that they had already driven over two million miles.
[2177.92 → 2182.56] And when people hear autonomous vehicles, they're often thinking about cars on the road.
[2182.56 → 2185.22] But what we're really seeing here is a transformation.
[2185.22 → 2190.64] And they kind of call it out in this report that you're seeing I think we're right on the cusp.
[2191.00 → 2209.16] You know, now that California has done that, you're going to see other states and other countries as well engaging in the same thing as people recognize that these vehicles can be safely integrated into society, whether on the road or in the air or on the water, wherever we happen to be.
[2209.22 → 2210.42] And we're going to see that more and more.
[2210.42 → 2211.80] And I think we're kind of right.
[2212.04 → 2220.56] I think this action by California demonstrates that we're kind of right at that tipping point as we're recording this where we're going to see it everywhere.
[2220.74 → 2226.18] I know in the company that I work at, autonomy is a big part of it, as it is in many different industries.
[2226.18 → 2239.14] And so I think you're going to see autonomy becoming fairly common over the next few years, whether it be on our nation's roads or those of other nations or from the bottom of the ocean to the surface all the way to outer space.
[2239.14 → 2242.56] I think that it's going to become in the space force.
[2242.84 → 2244.10] Yeah, it's we have you.
[2244.22 → 2245.08] That's exactly right.
[2245.18 → 2249.72] That's another thing worth calling out is in the last few months, the U.S.
[2249.80 → 2255.60] Space Force has been created out of what had been the space command in the United States Air Force.
[2255.70 → 2259.74] So we're now at a point where it made sense to separate those out as their own concerns.
[2259.74 → 2267.48] And so I think you're going to see autonomy in every facet of transportation sooner than most people might expect.
[2267.58 → 2269.30] So I'm full of asides today.
[2269.30 → 2275.42] But just as an aside, did you see how close the kind of the Space Force logo and the Star Trek thing?
[2275.52 → 2275.92] Yeah.
[2276.92 → 2279.80] So I saw people have them like side by side on Twitter.
[2280.04 → 2282.60] And, you know, it's kind of yeah.
[2283.06 → 2286.58] I don't know what to think about that, but it's kind of interesting.
[2286.58 → 2290.76] We'll leave it to people to call out on Twitter and Slack to us.
[2290.82 → 2291.74] We welcome your comments.
[2291.94 → 2293.70] I've seen some pretty funny ones so far.
[2294.46 → 2297.88] What's your opinion about Star Trek and the Space Force?
[2298.34 → 2301.22] Anyway, I guess that perfect.
[2301.42 → 2315.68] So see, I made a perfect transition with that aside to talk about public perception and societal considerations, which were some of the last things that were talked about in the index along with national strategies.
[2315.68 → 2323.36] So they talked about public perception of AI, societal considerations around things like fairness and interpretability.
[2323.36 → 2339.26] One of the things that I thought was good in the report is they did specifically call out that there's these 17 United Nations Sustainable Development Goals, which cover a lot of things around education and climate and other things.
[2339.60 → 2340.00] Oh, yeah.
[2340.08 → 2343.08] So there's the 17 and then there are 169 targets.
[2343.44 → 2347.80] And they talk about how AI can contribute to each of these.
[2347.80 → 2364.08] And if you remember, we had another guest on the show with the AI for Good Foundation, who is directly working with the United Nations to apply AI to the Sustainable Development Goals in fascinating and amazing ways.
[2364.08 → 2368.64] And so I definitely if you're interested in that side of things, take a listen to that other episode.
[2368.82 → 2376.90] But I think that's really worth calling out is now more than ever, because we have reached so many milestones in terms of AI.
[2377.08 → 2388.74] We're at a point where we can really apply AI to all of these different problems that really matter and make a difference for the quality of life for people to give them a better life.
[2388.74 → 2394.76] So if you're interested, you know, that's really a great effort to be a part of.
[2395.08 → 2409.02] And in terms of if you're looking for side projects or just to learn about AI, why not, you know, take on, you know, some side projects related to the Sustainable Development Goals related to AI for Good?
[2409.32 → 2412.42] Yeah, I think it's a really great time to be part of that sort of thing.
[2412.42 → 2433.08] I agree completely. And, you know, it wouldn't as we talk about AI for Good and societal impact, I think is a maybe finishing up with one last point that they note in this document is they really point out kind of the rise within the context of AI fairness, interpretability, explainability, what we tend to call ethics.
[2433.08 → 2444.86] And they identified that really those topics in terms of references to AI ethical principles have become an enormous, enormous conversation that we're having globally at this point.
[2445.20 → 2451.94] And we're recognizing that we have these powerful tools and before unintended consequences could arise that we need to be thoughtful.
[2451.94 → 2460.76] I love the fact that people are engaging on this and trying to say, how can we think about fairness before we have problems?
[2460.80 → 2477.56] We've had some bumps in the road over the last few years, obviously, but I'm very optimistic as we kind of go into the 2020s here about people at least engaging on these topics, on this kind of ethical AI principles on the front end of the decade as we search forward.
[2477.56 → 2482.38] So I just wanted to end on that note of optimism and ask people to continue to do that.
[2482.56 → 2488.04] Don't just do the engineering side and the data science side of AI, but think about the world that you want.
[2488.34 → 2496.74] And AI for Good, as you mentioned, is a great place to be thinking, whether it's in your primary job or whether it's what you're doing for a side project when you go home at night.
[2497.10 → 2507.44] Yep, definitely. And we always like to share learning resources as part of these fully connected episodes and one related to what Chris was just talking about.
[2507.56 → 2515.02] Which we could share, which I've poked around a bit with is the AI Fairness 360 toolkit from IBM.
[2515.28 → 2517.56] I think we've mentioned it maybe once on the show.
[2517.56 → 2534.54] But if you just go to AIF360.mybluemix.net, there's a toolkit there where you can experiment with their tools for fairness and analyzing data sets and modifying models and all of those sorts of things.
[2534.62 → 2543.24] They have a web demo, but also as a resource, they have links to read more about bias mitigation concepts, terminology.
[2543.24 → 2547.48] They have a Slack channel where you can ask questions related to that.
[2547.90 → 2558.54] They also have tutorials that show kind of examples of code that checks bias and in different industries and different applications.
[2559.08 → 2560.68] And I think I'm scrolling down.
[2560.78 → 2566.44] It seems like there's even more here than what I remember the last time I checked it.
[2566.44 → 2568.80] So they're talking about all sorts of things.
[2568.80 → 2577.10] So disparate impact, Manhattan distance, average odds difference, equal opportunity difference, all sorts of different methods.
[2577.10 → 2583.24] Then also talking about adversarial, debasing, re-weighting, really cool stuff.
[2583.42 → 2585.02] So I would suggest checking it out.
[2585.14 → 2587.34] And of course, they have notebooks where you can try things.
[2587.34 → 2595.72] And it's easy these days to spin up a notebook on Cola or other resources to try out a toolkit like this.
[2596.02 → 2596.38] Absolutely.
[2596.60 → 2597.08] Sounds good.
[2597.76 → 2597.94] Yeah.
[2598.08 → 2598.44] Awesome.
[2598.54 → 2600.48] Well, great to go through this with you, Chris.
[2600.98 → 2608.08] Interested to see what the index looks like next year, but it was great to talk through it with you and looking forward to a great year of AI.
[2608.40 → 2608.94] As am I.
[2609.20 → 2609.74] Sounds good.
[2610.02 → 2610.78] Talk to you later, Daniel.
[2610.86 → 2611.14] Thanks.
[2613.20 → 2613.70] All right.
[2613.76 → 2616.38] Thank you for tuning into this episode of Practical AI.
[2616.38 → 2618.10] If you enjoyed this show, do us a favour.
[2618.22 → 2618.80] Go on iTunes.
[2618.92 → 2619.62] Give us a rating.
[2619.88 → 2621.74] Go in your podcast app and favourite it.
[2621.86 → 2624.56] If you are on Twitter or social network, share a link with a friend.
[2624.64 → 2627.00] Whatever you got to do, share the show with a friend if you enjoyed it.
[2627.30 → 2629.96] And bandwidth for Changelog is provided by Vastly.
[2630.08 → 2631.52] Learn more at Fastly.com.
[2631.70 → 2634.90] And we catch our errors before our users do here at Changelog because of Rollbar.
[2635.12 → 2637.52] Check them out at Rollbar.com slash Changelog.
[2637.86 → 2640.34] And we're hosted on Linde cloud servers.
[2640.68 → 2642.30] Head to Linode.com slash Changelog.
[2642.38 → 2642.84] Check them out.
[2642.92 → 2643.74] Support this show.
[2643.74 → 2647.36] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2647.78 → 2649.86] The music is by Break master Cylinder.
[2650.30 → 2653.68] And you can find more shows just like this at ChangeLog.com.
[2653.76 → 2655.82] When you go there, pop in your email address.
[2656.10 → 2660.48] Get our weekly email keeping you up to date with the news and podcasts for developers in
[2660.48 → 2662.12] your inbox every single week.
[2662.48 → 2663.30] Thanks for tuning in.
[2663.44 → 2664.18] We'll see you next week.
[2664.18 → 2664.20] We'll see you next week.
[2664.20 → 2666.30] We'll see you next week.
[2666.30 → 2668.30] We'll see you next week.
[2668.30 → 2669.30] We'll see you next week.
[2669.30 → 2670.18] We'll see you next week.
[2670.18 → 2671.24] We'll see you next week.
[2671.24 → 2672.24] We'll see you next week.
[2672.24 → 2673.18] We'll see you next week.
