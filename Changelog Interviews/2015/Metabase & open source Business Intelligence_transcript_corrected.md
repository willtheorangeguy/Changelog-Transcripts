[0.00 → 0.88] I'm Samir Al-Wakrah.
[1.12 → 3.72] And I'm Tom Robinson, and you're listening to The Changelog.
[13.92 → 14.84] Welcome back, everyone.
[14.96 → 17.54] This is The Changelog, and I'm your host, Adam Stachowiak.
[17.62 → 19.80] This is episode 182.
[20.54 → 25.62] And on today's show, Jared and I are joined by two of the guys behind Metabase, Samir
[25.62 → 32.86] Al-Wakrah, and also Tom Robinson, and Metabase aims to be the simplest, fastest way to get
[32.86 → 36.66] business intelligence and analytics to everyone in your company.
[37.08 → 41.94] We dove deep into what the tool is, how SQL fits into it, the technology behind it all,
[42.04 → 43.02] Clojure, JavaScript.
[43.62 → 45.58] A lot of fun having these guys on the call today.
[46.12 → 52.16] We had four awesome sponsors for this show, Code Ship, Total, Harvest, and also Digital
[52.16 → 52.60] Ocean.
[52.60 → 55.68] Our first sponsor for today's show is Code Ship.
[56.02 → 60.96] If you haven't checked out the blog from Code Ship, go check it out, blog.codeship.com.
[61.48 → 65.24] And there was a recent post I want to mention from Barry Jones titled, Why Docker?
[65.74 → 70.86] And he dives deep into why Docker became a household name, why Docker set up VMs.
[71.20 → 76.78] He even goes into how Docker enables consistent environments, and even the fact that Docker
[76.78 → 80.22] isn't going away, he makes that hypothesis that it's not going away.
[80.22 → 83.10] There's also an e-book mentioned in that article.
[83.30 → 83.76] It's free.
[84.08 → 85.38] It's from Code Ship.
[85.84 → 87.20] Super awesome e-book.
[87.34 → 89.52] It's titled, Why Containers in Docker are the Future.
[89.98 → 91.06] This book is awesome.
[91.16 → 91.78] Go check it out.
[92.12 → 96.06] The link is in the article, and I'm going to put a link to the article in the show notes.
[96.14 → 99.48] So check out the show notes, changelog.com slash 182.
[99.94 → 101.26] And now, on to the show.
[101.26 → 109.54] Howdy, everyone.
[109.68 → 115.28] We are here today, Jared and I, with these awesome dudes behind Metabase, Samir Alcorcón
[115.28 → 116.38] and Tom Robinson.
[116.58 → 117.98] So, fellows, welcome to the show.
[118.56 → 118.80] Thank you.
[119.12 → 119.72] Thank you, guys.
[120.60 → 121.84] And, Jared, what do you think?
[121.90 → 122.34] Are you excited?
[122.98 → 123.92] I'm very excited.
[125.02 → 127.60] Metabase recently launched, made a splash.
[127.96 → 128.20] Yeah.
[128.20 → 132.98] And this hit my radar because, frankly, because of Tom.
[133.84 → 134.74] Tom's so cool.
[135.12 → 135.74] I know, right?
[136.58 → 136.96] Well, thank you.
[136.96 → 137.62] Tom, first question.
[137.68 → 138.48] How did you get so cool?
[140.94 → 142.20] That's a very good question.
[142.40 → 143.14] I really have no idea.
[143.58 → 144.62] Yeah, you don't have to answer that.
[144.78 → 145.38] Put you on the spot.
[145.84 → 153.28] But, yeah, I think Tom was one-third of 280 North, which made a splash back in the day.
[153.32 → 154.62] I'm not sure what year that was anymore.
[155.02 → 156.82] It was around 2006, I'm going to guess.
[157.40 → 157.66] Okay.
[158.20 → 160.12] The company started around 2006.
[160.32 → 162.14] We publicly launched 2008.
[162.54 → 163.06] There you go.
[163.64 → 169.82] So, 280 North, famous in the open source community for Cappuccino and Objective-J, which many people
[169.82 → 170.72] thought was brilliant.
[170.84 → 172.84] Other people thought was crazy.
[174.08 → 175.88] I thought it was a typo.
[176.30 → 177.50] What was Objective-C?
[177.78 → 178.08] Wrong.
[178.70 → 179.18] I'm just kidding.
[179.58 → 181.66] But I happen to be one of those people that thought it was pretty cool.
[181.66 → 189.60] I think 280 slides, which was basically keynote inside a browser way back in 2007, 2008,
[189.68 → 193.30] was quite the tech demo showing off what Cappuccino could do.
[194.30 → 195.58] And, yeah, I went into it.
[195.58 → 200.40] I was writing some Cappuccino, and I actually didn't know Objective-C, which made learning
[200.40 → 201.66] Objective-J very difficult.
[201.66 → 204.66] But for those who don't know, Objective-J was...
[204.66 → 206.94] Well, Tom, why don't you explain what Objective-J is?
[206.94 → 212.30] Yeah, so Objective-J was sort of a language extension to JavaScript.
[213.80 → 221.58] But sort of stepping back to the reason why we did that was we saw these cool web applications
[221.58 → 229.46] being built by Google and mostly Google back in 2005 or so.
[230.30 → 232.14] Gmail, Google Maps, that kind of thing.
[232.56 → 233.92] And we wanted to build this kind of things.
[233.92 → 237.84] And you really had to do everything from scratch.
[238.36 → 243.26] There wasn't really a full-fledged framework sort of analogous to Coco.
[245.60 → 246.92] So we...
[247.68 → 251.82] And we had been Coco developers, so we sort of took a lot of the ideas from that
[251.82 → 254.04] and built this framework we called Cappuccino.
[254.76 → 259.36] And at some point, we decided it might be cool to have sort of a language extension
[259.36 → 263.50] that gave us some of the things that Objective-C gave you on top of C.
[263.50 → 266.70] But put it on top of JavaScript so it could run in web browsers.
[267.52 → 271.52] And so it added things like modules and classical inheritance and that kind of thing.
[272.26 → 272.36] Right.
[272.74 → 277.32] And somewhat famous in the open source community for its divisiveness.
[278.14 → 278.56] Yeah.
[278.70 → 282.56] But no doubt interesting what it allowed to produce.
[282.56 → 288.04] And then 280 North, eventually you guys sold, correct?
[289.18 → 289.66] Yeah, yeah.
[289.72 → 292.40] So we worked on Cappuccino for a couple of years.
[292.60 → 295.72] We started working on some developer tools around Cappuccino.
[296.08 → 296.26] Right.
[296.26 → 305.34] And we ended up being acquired by Motorola in 2010 to work on similar kinds of things there.
[306.14 → 306.88] There you go.
[307.06 → 312.42] So 280 North, no longer a thing or at least consumed by Motorola.
[312.42 → 316.34] And then you start to ask yourself over time, what happened to those guys?
[316.42 → 316.92] Where are they?
[316.92 → 318.50] And I think I had followed Tom on Twitter.
[320.88 → 322.74] Then all of a sudden outcomes Metabase.
[322.92 → 326.28] And I think you said, if you've been wondering what I've been up to lately, this is it.
[326.52 → 330.60] And so that was kind of the genesis of this call.
[330.60 → 336.08] Also, we had a few people, Changelog members, chatting about Metabase on launch day saying,
[336.24 → 337.34] oh, we've got to get these guys on.
[338.28 → 339.48] And here we are.
[340.14 → 340.56] Here we are.
[341.16 → 341.80] Here we are.
[341.80 → 343.82] But let's learn a little bit about Samir.
[344.42 → 345.26] Samir is CEO.
[345.50 → 346.68] Tom, are you CTO?
[347.42 → 348.94] No, our CTO is Alan.
[349.36 → 349.56] Okay.
[350.06 → 351.02] He couldn't be on today.
[351.30 → 351.82] Fair enough.
[352.36 → 353.54] So Tom is an engineer.
[354.88 → 355.94] Chief Robbie Rouser.
[356.78 → 357.92] Chief Robbie Rouser.
[358.04 → 358.64] I like that.
[359.18 → 363.50] Samir, why don't you give our audience a little bit of introduction to who you are and where you're coming from?
[364.12 → 367.20] I guess I've been coding since I was in middle school.
[367.20 → 375.80] I spent a lot of my earlier career just dealing with some of the crazier sections around machine learning, engineering.
[376.70 → 379.70] I think my first couple of jobs all revolved around ML.
[380.32 → 383.14] And at some point I started doing Hadoop before Hadoop was cool.
[383.62 → 391.08] And a couple of years into that, most of my life was spent either cleaning crappy data, pushing crappy data around,
[391.22 → 394.34] or displaying the net results of pushing crappy data around.
[394.34 → 401.76] And so it became less about algorithms, more about just presenting information to normal human beings.
[401.98 → 404.66] I think that's been the main theme of the last couple of years of my life.
[405.72 → 405.88] Interesting.
[406.20 → 407.24] How did you find that?
[407.40 → 419.56] Like you thought you were going to be doing more advanced algorithms, but was it your exposure to like real business problems where you realized it's just a bunch of crappy data, and now I have to maintain it?
[419.56 → 431.58] I think a big part of it is that most companies, most teams, most organizations are at a much lower level of Maslow's hierarchy of data needs than they think they are.
[432.06 → 437.50] And then what it really comes down to is most people just want to add up some numbers and show a pretty picture to someone.
[438.30 → 440.50] And so now you kind of get on board.
[440.66 → 443.86] There's all this talk about all the crazy things that everyone wants to do.
[443.86 → 451.70] And then when you actually sit down at your desk and realize, well, none of the stuff that lets you build the crazy stuff, the crazy things are actually around.
[452.66 → 462.84] And so there was this definite moment of moving from, I guess, the first thing I did at my first real startup job was just optimizing memory patterns.
[463.18 → 465.18] And so it was, hey, here's this recommendation algorithm.
[465.18 → 470.04] It's running on a single core and, you know, I think it was four gigabytes of RAM back then.
[470.38 → 477.24] And I spent the first three months just trying to stuff more training samples into that four gigs.
[477.92 → 481.10] And then Hadoop came about, and it was more, it switched gears.
[481.24 → 490.94] I switched gears from being kind of a memory sort of hash map weaker to just adding up numbers for label reporting.
[490.94 → 501.96] And so a lot of the sexy stuff that Hadoop unlocked was just being able to add up, you know, plays of who played which track for how long, faster and better.
[502.90 → 504.38] I think that's an interesting insight.
[504.52 → 508.06] I have a friend here locally in Omaha who's kind of an operational consultant.
[509.08 → 513.32] And he's very much at the same level as you were with many with small businesses.
[513.32 → 524.10] I think we all focus a lot on large businesses and enterprise and corporations with huge, you know, data systems and many large problems they're trying to solve.
[524.52 → 535.00] And there are thousands, if not tens of thousands of small businesses out there that just have no handle at all on their data and no insights whatsoever.
[535.00 → 545.12] Maybe just a series of spreadsheets on a shared network storage that, you know, they're trying to share access to or this kind of things.
[546.72 → 550.88] So, man, I mean, that seems like a very good lead in to Metabase, right?
[551.38 → 551.92] Sure does.
[552.32 → 553.74] So glad you guys teach it up for me.
[555.08 → 556.96] Tell us, Samir, what is Metabase?
[556.96 → 569.80] At the end of the day, Metabase is a way to take all the stuff you have lying around in a database somewhere, whether it's a data warehouse and you've paid Vertical a bunch of money, or whether it's just a MySQL box you have running on your desk.
[571.38 → 580.48] And let normal human beings get at it in the sense that, you know, for most people aren't engineers.
[580.70 → 584.20] Most people, and even if they are engineers, they don't necessarily want to write SQL all day.
[584.20 → 590.82] At some point, you just get tired of banging out yet another view of a data with a chart attached to it.
[591.70 → 608.80] And so the primary kind of purpose of Metabase is just to take a table or database and then render it in a real way, and then also to let someone interact with that data and that visualization and kind of get to what they're looking for.
[608.80 → 622.04] And at least on its face, it's meant to feel more like clicking through something and kind of exploring as opposed to I'm showing up, I have a question, I know exactly what I want, and here are the parameters.
[622.58 → 629.10] It's more that, I mean, I could say most of my professional life, I've not known exactly what I wanted when I sat down.
[629.10 → 641.00] So even in situations where there was a very concrete request from someone, or we knew what we were building, when you actually sit down to write the queries, it's like, so I think I want to see what's in this table.
[641.48 → 644.30] I want to do a select whatever limit 10.
[644.76 → 646.10] I want to Fitz around with it.
[646.14 → 647.86] I want to see what the various values are.
[648.34 → 650.42] I don't remember what this field was called.
[650.52 → 652.58] I don't remember whether this was a string or an enum.
[652.58 → 669.84] And rather than having to look all that up or memorize it or just spend that first half an hour with a bunch of selects, Metabase really just created to let me sit down or let someone who is not nearly as technical sit down and get to the kinds of questions they want to ask.
[669.84 → 675.16] I know when we first looked at Metabase, I was thinking, okay, what is the purpose of this?
[675.18 → 683.38] Because on one side, it's like, you know, your tagline is an easy way for customers to, or sorry, companies to ask questions and learn from data.
[683.50 → 690.40] So I was wondering if it was like a Quora thing, you know, that was open sourced or was it something you pointed at a database?
[690.72 → 693.22] So you seem to kind of answer that in a bit of a way.
[693.88 → 696.76] Yeah, I think we're still struggling to kind of describe what it really is.
[696.76 → 701.56] Most of the vocabulary in the space has been overloaded and made almost meaningless.
[702.34 → 708.78] So like we're analytics, we're business intelligence, we're reporting, we're data access, we're, I don't know.
[709.30 → 719.04] And there have been thousands of products that do fundamentally the same thing we're doing, which is taken a database and let someone visualize it and look at it and play with it.
[719.04 → 730.50] But yeah, so like I get, I get the I get your confusion about the word questions and I don't think we've found a perfect way to describe fully what we are.
[730.50 → 736.22] Yeah, I thought it was going to be like, you know, open it up to the company if you've got questions.
[736.92 → 739.34] Very Quora-like, you know, internally, so to speak.
[739.34 → 741.28] And I've seen some of those come and go.
[741.76 → 743.06] And I was like, well, is that what it is?
[743.08 → 746.18] But then as we dug deeper, it was like, okay, it seems like you pointed at a database.
[746.18 → 750.92] So you can, you know, to jump the gun a little bit, we can, we have several different ways we can play with it.
[750.92 → 755.86] And one of the ways is if you're on a Mac, you can download sort of a wrapped version that's just for play only.
[756.20 → 766.02] I guess maybe you can do some personal production stuff, but it's not like collaborative, you know, but you can point it at a database locally and start to discern some of the data.
[766.02 → 767.08] There's that word again, Samir.
[767.74 → 771.42] You know, you're checking out some of your data and visualizing it and, you know, running queries.
[771.50 → 773.66] It seems like it's, you know, a layer on top of that.
[774.12 → 777.60] But the ask questions part was very confusing to me.
[778.48 → 778.78] Point taken.
[778.78 → 783.30] Yeah, and even once you get into it, I have been running a few things.
[783.52 → 795.46] And, of course, I'm, you know, as an Apple developer, as an app developer, like queries and selects and, right, like SQL, you know, you start to think in relational models.
[796.26 → 804.28] And so I'm immediately thinking, okay, this is a query builder, but the interface and the I see what you're trying to do.
[804.34 → 805.74] It's like create a new question.
[805.74 → 808.24] And it's like you're trying to provide an insight or something.
[808.72 → 813.76] But then once you start building a question, really it is like kind of like describing what you want to see.
[814.14 → 819.62] And so there's a bit of a there's a bit of an impedance mismatch between the word question and I think what's going on.
[819.66 → 824.24] But I definitely see how that's a difficult thing to describe and where you guys are trying to get with.
[824.24 → 833.86] You're trying to simplify the cognitive space necessary to actually like to construct these things so that everybody can do it and not people like us.
[833.86 → 850.52] Just to jump the gun a little bit, I think when you really get down to it, like the fundamental problem we're solving is in our current state is what someone's mental model is of their application or their data set or their business or whatever it is they have data about.
[850.52 → 855.86] And letting them work in that model as opposed to the model of their schema on disk.
[855.86 → 871.60] And so on of the interesting things about Metabase is we're also starting to kind of nudge in the direction of rather than formulating a question, rather than telling us what you want, you just kind of poke around, and you're like, you can double-click on a cell and filter by it.
[871.60 → 876.36] You can follow an ID to that records detail.
[876.46 → 877.36] You can follow connections.
[878.04 → 886.60] And in general, the overall sort of user idiom we're going for is I can look at the data, I can play around with it.
[886.84 → 892.36] And then rather than having to format the question precisely, it just emerges from me clicking around.
[893.48 → 900.84] Yeah, I think that would be a nice extension of that or perhaps eventually a replacement altogether.
[900.84 → 903.44] It's just kind of an exploratory thing.
[905.74 → 909.50] So the first question that Adam and I started asking is like, what exactly is this?
[909.52 → 910.78] I think we've covered that pretty well.
[911.34 → 915.74] The other question we had was like, why is this open source?
[915.88 → 924.46] But I think that's even assuming we have some knowledge, which is, you know, as we intro'd you guys, Samir, you're the CEO of Metabase.
[924.78 → 927.06] So this is not just an open source project.
[927.06 → 931.02] This is a company, which we're seeing more and more of this.
[931.40 → 939.02] I think just last week, Adam, we had Slave Schumacher on with Rethink DB, which is both an open source project and it's also a company.
[939.52 → 941.96] And it's a growing trend in open source.
[942.70 → 951.38] So maybe let's rewind a bit and just get an idea of what Metabase the company is, where you guys come from and the business side of things.
[951.38 → 957.12] Yeah, so Metabase was originally part of Expo, which is a startup studio in San Francisco.
[957.88 → 959.92] I'd spent about a year and a half there.
[960.24 → 972.12] And we'd originally built out this huge, crazy custom analytics system for all of our companies that spanned everything from collecting events to stuffing them in a data warehouse to running transformations on them.
[972.12 → 978.12] And then finally to visualizing both the data and queries on top of the data.
[978.88 → 984.84] And about a year ago, we'd reached the point where we definitely wanted to work on it full-time.
[984.98 → 988.22] We definitely thought that it had legs and that it was something the community would want.
[988.22 → 997.78] And that rather than it being something that was used by 10 companies internally, we could open up to the world and have potentially anyone use it.
[999.38 → 1002.30] And so that's kind of where it emerged from.
[1002.80 → 1010.34] I'd say the other thing it emerged from was just I've wanted something like it for about seven or eight years now.
[1010.34 → 1027.94] And every couple of years, I'd poke my head out of the ground, look around, check out the usual suspects in the open source BI world, try to install them, hate the process, and just write my own query builder or add inventory planner or customer record lookup or something of that sort.
[1028.60 → 1031.66] And so kind of jumping the gun to your question of like, why is it open source?
[1031.66 → 1039.34] I think one of the starting points is just I think there should be something like it in the open source community and the ecosystem.
[1040.74 → 1044.70] And had someone else built it three or four years ago, I probably would never have started on it.
[1044.96 → 1048.40] But it just feels like something that's missing and something that I've always wanted.
[1049.28 → 1054.12] On the business side of things, I think we're still figuring out exactly how that'll play out.
[1054.12 → 1060.88] But the general sense is we will be offering a Metabase itself for free, open source, forever.
[1061.20 → 1061.96] It's production grade.
[1062.50 → 1063.92] We're never going to hold anything back.
[1064.60 → 1070.06] And then the things around the usage of Metabase in a company, we'll start to charge money for.
[1070.06 → 1079.50] Okay, so we actually have a tweet from probably Jared, one of the fellow Changelog members that you mentioned, Justin Dorfman.
[1079.58 → 1086.24] He asked a question on Twitter, just tweeting to you, Tom, and then at Metabase and said, looks awesome.
[1086.40 → 1089.26] And, you know, in reference to Metabase, came with a try it out.
[1089.36 → 1090.28] How do you plan to sustain it?
[1090.28 → 1095.12] So you seem like you answered that to a degree because his question was, will there be a pro version?
[1095.12 → 1112.20] Now, Jared mentioned that's sort of the way that we've seen more and more companies like Rethink DB or others create an open source version and a supported version or a pro version that's on top of it that's, you know, much more robust.
[1112.50 → 1114.52] So is that something we could talk about here today?
[1114.60 → 1116.20] Do you have a lot of details around that?
[1117.26 → 1120.74] I mean, we have a couple rough prototypes we've played around with.
[1120.82 → 1122.78] We have a couple themes we're exploring.
[1122.78 → 1133.66] Now, I'd characterize it less as a pro version that's somehow better than the open source version and more the supporting scaffolding that lets you use it in big, hairy, complex places.
[1134.52 → 1137.52] And so there are lots of things that most people don't really care about until they do.
[1138.00 → 1148.90] So like compliance or data governance or auditing who saw what or maintaining institutional knowledge across 10 years' worth of analysts and being able to disseminate that.
[1148.90 → 1158.78] And while that's something that, you know, Comcast would pay money for, it's unlikely that someone who, you know, does a Git clone or eventually an app get would ever care about.
[1159.16 → 1175.50] And so as usage at a company or someplace that is commercial takes off, and you go from having 10 people on it to 20 analysts and 100 end users, there are a lot of problems that emerge that we will offer solutions for that we'll charge money for.
[1175.50 → 1180.92] You mentioned that if there was an open source version out there, you probably wouldn't have done it.
[1181.66 → 1185.82] Maybe it's an obvious question, but why open source?
[1186.00 → 1188.24] What makes sense to make Metabase open source?
[1188.32 → 1189.58] What's your plans for open source?
[1189.58 → 1197.56] In some way, it's just how I think this kind of software should be available.
[1197.56 → 1223.10] And I characterize kind of the starter BI kit for most companies as being the same class of things as WordPress or Nginx or an app server or, you know, WSGI, where it feels like such a basic component of most modern stacks that it's kind of weird that there isn't an open source starting point there.
[1223.10 → 1227.24] And so in some ways, it's kind of ideological.
[1228.40 → 1239.52] In some ways, it's just a sense that the entire data infrastructure ecosystem is all open source or sorry, the part that I care about, the part that I'm engaged with and the part that I've worked in has been open source.
[1239.78 → 1247.94] And I both want to contribute to that commons and just my own belief that a better product will result as at the end of it all.
[1247.94 → 1251.96] All right. Well said. Well, it's time to take a break.
[1252.30 → 1258.24] On the other side, we're going to talk about SQL, how that plays in and what you all might be thinking.
[1258.60 → 1261.52] That's what SQL was made for. So we'll be right back.
[1263.18 → 1275.56] Our friends at Total launched a scholarship program for female developers to support aspiring female computer scientists, developers and software engineers to help achieve their goals through financial support and also mentorship.
[1275.56 → 1283.60] Each scholarship winner will receive a $5,000 scholarship that can be used towards education and professional development goals.
[1283.60 → 1290.04] You can spend this money on anything you want from coding boot camps to online programming courses, textbooks, you name it.
[1290.48 → 1297.84] You also get one on one mentoring, an entire year of weekly one on one mentoring with a Total senior developer.
[1297.84 → 1305.84] And this person is going to help you with topics like project guidance, choosing an academic or career path and also preparing for interviews.
[1306.04 → 1309.90] Head to TopTal.com slash scholarships to learn more and also to apply.
[1313.52 → 1319.14] All right. We are back again with Tom and Samir diving deep into what Metabase is.
[1319.14 → 1327.06] For those of you out there listening along got questions like this, you may be thinking that that's what SQL was meant to be and what it should solve.
[1327.20 → 1336.40] So Tom, Samir, I'm not sure who wants to take this, but it seems like this is some of what SQL was meant to solve.
[1336.58 → 1344.86] And I get it. A better user experience, you know, maybe even platform-agnostic, web UI, more flexibility, things like that.
[1344.86 → 1347.60] But, you know, why is this better than plain old SQL?
[1348.36 → 1352.82] So I have a long rant about that. But Tom, if you want to chime in first, maybe you can.
[1354.40 → 1368.28] Sure. Yeah. I mean, so SQL is fantastic for developers, for anyone who's, you know, able to parse and really understand the syntax of SQL,
[1368.28 → 1374.08] which, you know, a lot of us probably take for granted, you know, how easy it is to use.
[1374.34 → 1378.82] It's if you're familiar with programming languages, it's not difficult to pick up.
[1378.96 → 1387.32] But if you're not, you know, it's just a lot more difficult to format everything correctly, know exactly what you're supposed to say.
[1387.32 → 1397.92] And so Metabase offers sort of a more graphical way of expressing a lot of the same types of things and more powerful things as well.
[1399.24 → 1401.00] Well, Samir, you said you had a rant. What's your rant?
[1401.88 → 1406.30] So I think it's interesting to look at SQL in the context of the 70s when it came out.
[1406.30 → 1418.14] And I and there's kind of this, you know, every five or 10 years, there's always some new citizen BI movement or product or marketing campaign.
[1418.56 → 1427.38] And if you look back and think about what it was like to write database access modules or code or just queries before SQL,
[1427.38 → 1433.20] you had some variant of assembly language or C and you were hitting DB or DB2 directly.
[1433.20 → 1438.76] And so when SQL came out, it's kind of in many ways a bombshell in the sense that it looked like English.
[1439.30 → 1441.98] Normal human beings could probably understand it in a couple of days.
[1442.30 → 1448.56] And if you were smart and numerical and just at all inclined, it was not that hard to pick up.
[1448.86 → 1448.90] Right.
[1450.04 → 1454.08] And I'd say that, you know, even it was a categorical huge success.
[1454.94 → 1459.80] And I can't say enough good things about SQL overall and just the RDB mess.
[1459.80 → 1468.70] But what else has happened is there's been just these waves of accessibility where you start out with just I'm going to write some crappy assembly code.
[1468.84 → 1470.30] Then to I'm going to write SQL.
[1471.04 → 1473.44] And then you get spreadsheets and spreadsheets are magic.
[1473.82 → 1478.58] And, you know, Excel is kind of one of those transformative technologies in our world.
[1478.58 → 1484.48] And then you kind of get into the world of like maybe access counts, and then you get Tableau in the mid 2000s.
[1485.10 → 1492.70] And in each of those, there's been this significant widening of the pool of people that have creativity and questions.
[1492.92 → 1500.30] And honestly, just like are informally what they want to know and are the people that should be asking the underlying questions.
[1500.30 → 1504.80] And this lets them do that as opposed to requiring them to also learn how to be programmers.
[1505.12 → 1513.86] Yeah, it does seem to remove the barrier to be, you know, in quotes, a programmer, a developer, someone who is familiar with or even comfortable with it.
[1514.24 → 1522.04] And I can think of many people who are had creative minds that you're like, man, you should be in these meetings with us asking these questions because that's a great question.
[1522.80 → 1522.94] Yeah.
[1523.04 → 1525.26] Seems like you're wanting to put a great tool in their hands.
[1525.26 → 1536.84] And some of it is just even if you are a programmer, even if you are inclined in that way, like, and I mean, I don't know how good I am at SQL when all of a sudden done.
[1536.92 → 1544.80] I think I have at least a working knowledge of it, but I've definitely hung out with people that are much more proficient at it than I am.
[1545.46 → 1549.80] There's still days when you don't want to type, or you don't want to think in that way.
[1549.80 → 1563.94] Or, you know, if you're fundamentally in a creative headspace, you're thinking about what people are doing and how they've done it, you know, whether it's dropping down Map Reduce, whether it's writing SQL, whether it's, you know, writing R scripts or Python scripts.
[1564.38 → 1566.96] There are days when that's not how your brain's wired up.
[1567.90 → 1573.32] And I think it's useful to be able to approach problems from different directions using different tools.
[1573.32 → 1578.56] And so, like, every once in a while, I'll fire a Tells, or I'll, you know, pull up R or MATLAB.
[1579.04 → 1585.24] But there are days when you just want to see a pretty picture or a graph, and you don't want to deal.
[1586.10 → 1586.58] So, right.
[1587.64 → 1594.54] And the flip side of this is given that most of us don't work in isolation, there's other people in the room that are doing all kinds of stuff that is hopefully useful.
[1595.50 → 1598.58] You don't necessarily want them banging on your door every time they have a question.
[1598.58 → 1616.50] I can think of things like, too, where you're in, you know, you're in marketing, you're in product development, and you don't feel like going and messing with the people in ops or infrastructure or somebody that's got, you know, way more things to do and to answer your questions about, you know, data, basically.
[1617.66 → 1619.98] Yeah, because, I mean, they have stuff they're doing in real life, too.
[1620.08 → 1621.78] Like, you know, we all have jobs, presumably.
[1622.30 → 1622.52] Right.
[1622.52 → 1626.48] Or we all have things we do for fun or passion or to pay the rent.
[1626.48 → 1629.40] And usually there's only so many hours in the day.
[1629.82 → 1639.64] And if rather than having an ops person or a DBA spend 30 hours a week fielding all this kind of recurring ad hoc.
[1639.80 → 1641.10] Internal support questions, even.
[1641.54 → 1642.14] It seems like.
[1642.66 → 1643.14] Precisely.
[1643.32 → 1643.56] You know.
[1644.18 → 1645.06] Like, how do I do this?
[1645.18 → 1646.12] Where's this data coming from?
[1647.00 → 1648.18] Or what does this field mean?
[1648.30 → 1651.26] It's like, what does is underscore test underscore count mean this week?
[1651.58 → 1651.86] Right.
[1652.54 → 1654.08] That's my favourite rant, actually.
[1654.08 → 1659.78] Maybe it would be clarifying to the listening audience because they can't see it.
[1660.18 → 1662.58] They can't feel it right while we're here talking about it.
[1662.62 → 1671.10] Could one of your kind of verbally go through what the user experience is of asking a question and kind of formulating some things you can do in Metabase?
[1671.16 → 1674.46] Can you kind of walk us through what the UI looks like and this user experience looks like?
[1675.12 → 1676.12] Sure, I could take that.
[1676.12 → 1679.02] So you load up Metabase.
[1679.94 → 1689.46] If you haven't edited a database, you can add all the connection details for the host name, port, password, all that stuff.
[1689.70 → 1693.88] And then basically just click create a new question or ask a new question.
[1693.88 → 1702.20] And it presents you with this sort of graphical editor for expressing queries.
[1702.86 → 1707.72] You first select the database that you want to ask a question about.
[1708.62 → 1716.66] And then it gives you a bunch of options on filters, aggregations, sorting.
[1717.02 → 1719.68] You know, a lot of the same kind of things that you could express in SQL.
[1719.68 → 1733.82] But we try to, you know, limit your choices to things that make sense and give you special interfaces for different data types.
[1733.98 → 1741.52] So if it's a numerical column, you can filter by greater than equals, you know, those kinds of things.
[1741.52 → 1748.24] If it's a date or timestamp, you can filter by like a special date picker.
[1749.50 → 1760.52] And then you can aggregate the results in various ways, like counting sums of certain columns, grouping by different columns.
[1760.52 → 1767.66] And so the idea is you start by picking a table.
[1768.26 → 1770.74] Maybe you just view the raw table to begin with.
[1770.84 → 1781.70] And then you can pick an aggregation, view it, aggregate it some way, and then add filters and that sort of thing as you sort of decide what direction you want to go with the query.
[1781.70 → 1788.68] And for somebody who's kind of getting antsy, I've got to ask, is it read and write only, or can you write back to it or is it just read only?
[1789.00 → 1789.92] It's read only.
[1790.44 → 1793.50] All the connections to the databases are read only.
[1793.72 → 1801.22] And, you know, if you want to create a special account on your database that's read only, we recommend you do that as well.
[1802.10 → 1803.92] About 10,000 people just wiped their brow.
[1804.12 → 1806.46] They had some sweat on their brow, and they're like, whew, nice.
[1806.46 → 1814.54] Yeah, you probably don't want to be issuing queries against your production database anyway, so you might set up a replica or something like that.
[1815.76 → 1824.62] Yeah, I guess because that would be kind of shared traffic, internal traffic, and then actually, you know, real writing and reading from the database would make some sense.
[1825.56 → 1829.66] I also have some notes that you can still do SQL when you need it.
[1829.68 → 1831.84] Can you talk about what that user experience is like?
[1831.84 → 1843.54] So if you're doing this questioning, and you're kind of diving into your data, if you do have that kind of superpower like being able to write SQL and query the database, how do you access that piece?
[1844.18 → 1844.40] Sure.
[1845.02 → 1856.32] Yeah, so in this query editor, when you start a new question, there's a little toggle button in the top right-hand corner that you can flip over to SQL mode.
[1856.32 → 1867.84] And yeah, we just give you a fairly basic SQL editor, but it does have auto-completion for all the various operators and table names and that kind of thing.
[1868.66 → 1873.70] Is the hope with that feature to get both sides of the fence using the same tool?
[1873.80 → 1881.24] So if you've got the superpower to be able to do SQL and write SQL, you're in the same thing that the other users are in?
[1881.24 → 1885.24] Is that the idea or is it just simply to give quick access?
[1886.32 → 1898.10] So, you know, we have that in there because we're trying to create this editor that can express any sort of query you want within reason.
[1898.10 → 1906.32] But at least, especially in the early days, we couldn't express a lot of the queries that our users wanted to ask.
[1906.62 → 1913.68] So having the SQL editor allows you to drop into SQL to express more queries.
[1913.68 → 1917.98] And some people are just more comfortable with SQL, and that's fine as well.
[1918.16 → 1925.08] So once you save a question, you know, you can add either one to a dashboard and that sort of thing.
[1925.14 → 1929.92] It doesn't matter if it's a SQL query or built with our graphical editor.
[1929.92 → 1941.70] One of the things it lets you do is, like, for the kinds of questions our interface can express, it lets someone with a secret power do it for others, and then they can reuse that.
[1941.70 → 1952.32] So most people, even if they can't write SQL, are very comfortable taking this wall of text and replacing 714 to go from weekly to 14-day averages.
[1953.04 → 1958.64] And so people are willing to edit and remix them, but they wouldn't have the ability to create them from scratch.
[1958.64 → 1968.64] Tom, going back to something you mentioned earlier, it was just when you're actually asking that the process of asking gets smarter based on the actual data fields in the database.
[1969.10 → 1973.58] Does association detection require the proper foreign keys, or is it smarter than that?
[1974.46 → 1983.74] So we try to detect as much as we can base on, yeah, foreign keys that you have set up and the field types and all that.
[1983.74 → 1992.62] And if we don't do a perfect job, you can edit all the metadata that we've captured about your schema in the settings page.
[1993.06 → 1995.76] So yes and no.
[1996.72 → 2002.54] And being a little more in the weeds, even if something doesn't have constraints, you can still use them in join statements.
[2002.54 → 2017.32] And so if you go in and manually say, this field is a foreign key to that table, then all of our kind of relationship or has one relationship aspects of our query builder still work.
[2018.40 → 2024.48] And we're trying to get smarter around auto-detecting things like that, but it's an ongoing process.
[2024.48 → 2027.72] Can we talk about database support?
[2027.88 → 2030.32] You got support for MySQL.
[2030.42 → 2035.74] Let me go back to the list because I didn't have it, and I'm bringing up that topic, and I'm not perfectly ready to ask the question.
[2035.84 → 2038.58] But you got MySQL, Postgres, Congo.
[2039.32 → 2041.38] And then I had to ask Jared, I'm like, hey, what is Redshift?
[2041.48 → 2045.10] Because I'd actually never used that, so I had to go look that up, and it's actually pretty cool.
[2045.16 → 2045.58] It's from Amazon.
[2045.78 → 2048.86] So if you didn't know about Redshift, Amazon makes it, and it seems pretty interesting.
[2049.06 → 2051.36] So I don't deal with big data enough, so that's why.
[2051.36 → 2055.06] Let's talk about the support for various databases.
[2055.24 → 2057.12] Obviously, MySQL makes sense, Postgres, Congo.
[2057.80 → 2060.56] What's the process to support that from a technical standpoint?
[2061.30 → 2069.66] So we have a query language that all of our queries built using the interface are serialized as,
[2070.10 → 2078.06] and then we have a separate step which converts those to either SQL or the Congo query language or whatever else we support.
[2078.06 → 2086.46] And so adding additional drivers is what we call them internally, is just creating another driver for a specific target,
[2086.68 → 2089.86] either SQL dialect or a completely different database driver.
[2090.38 → 2094.54] So we had Slave Schumacher on recently, Rethink DB.
[2094.74 → 2102.14] So if he wanted to support Rethink and Metabase, it's simply forking, writing the own driver, and boom, goes to Dynamite?
[2102.58 → 2103.10] Yeah.
[2103.64 → 2104.42] That's awesome.
[2104.42 → 2108.00] If you know a guy who knows a guy, we'd love it if they would help us out with that.
[2108.36 → 2109.42] Well, we do know a guy.
[2109.86 → 2113.86] But I'm sure maybe the guy's listening, so just do it, Slave.
[2114.24 → 2114.42] Yeah.
[2114.50 → 2122.30] And in general, we're committing to writing a bunch ourselves, but the primary determinant of which ones we write is just what people ask for.
[2122.30 → 2128.02] And so we've been funnelling people to the GitHub issues in question and just trying to get a gauge for,
[2128.66 → 2131.74] of the folks that have found us, of the folks that are using us, what do they want?
[2132.56 → 2138.92] And so, for example, we're working on both SQL Server, which apparently a lot of people wanted,
[2139.28 → 2142.94] which I didn't expect, and Redshift drivers.
[2142.94 → 2153.84] And there's a couple other open issues for, just off the top of my head, Elasticsearch, BigQuery, Spark, Presto, maybe Impala.
[2154.48 → 2157.64] And just if enough people want one of those, we'll do it.
[2158.22 → 2164.08] But we don't want to just write 50 drivers for every different dialect without having there be someone who's,
[2164.52 → 2167.74] who cares enough to complain about it and just cast their vote.
[2167.74 → 2169.08] So, good stuff.
[2169.96 → 2171.84] Well, it's time for another break.
[2171.94 → 2175.32] When we get back from this break, we're going to dive deeper into getting started with Metabase,
[2175.80 → 2178.48] moving on from the Mac app, and getting into production.
[2178.70 → 2179.86] So, stay tuned.
[2180.48 → 2181.20] We'll be right back.
[2182.78 → 2185.90] If you thought Harvest was only about time tracking, check again.
[2186.34 → 2187.84] Fast invoicing and payments.
[2187.84 → 2192.80] You can easily create and send invoices and accept payments with PayPal, Stripe, and many more.
[2193.36 → 2195.02] You got expense tracking without the mess.
[2195.02 → 2201.00] You got an iPhone or an Android app to go on the go with you, snap photos or receipts, and store them in the Harvest app.
[2201.46 → 2206.24] You can also connect favourite tools like Slack and use chat commands to start and stop your timers.
[2206.72 → 2209.16] Head to GetHarvest.com and start your free trial.
[2209.64 → 2214.62] And once that trial is over, use our code CHANGE LAW to save 50% off your first month.
[2217.74 → 2218.58] We're back.
[2219.00 → 2223.40] And we still have these two awesome fellas, Thomas Amir with us and Jared.
[2223.40 → 2225.60] Jared, we're dealing with a little tiny bit of lag with Jared.
[2225.74 → 2229.62] So, if for some reason, I'll edit this good, but Jared, you sound beautiful, man.
[2229.62 → 2230.10] I love it.
[2230.30 → 2230.76] You sound great.
[2230.96 → 2231.74] Edit it good, man.
[2231.86 → 2232.42] Edit it good.
[2232.60 → 2233.14] Edit it good.
[2234.06 → 2239.46] You know, and before the break, I said, let's come in talking about platform and, you know, how we can get this production.
[2239.54 → 2244.88] But I want to ask one more question real quick that's more on the general side before we go into the deep tech side.
[2244.88 → 2250.78] You know, we're in the days of Slack, real-time communications, things like that.
[2250.84 → 2259.68] And I'm just wondering how this kind of things play together when you actually communicate with your team, and then you're actually, you know, kind of digging into your data.
[2260.16 → 2263.32] Is there ever a plan to sort of do some Slack integrations?
[2263.32 → 2271.42] It's funny you mention that because that's exactly what we're working on right now.
[2271.80 → 2272.28] Right now.
[2272.54 → 2272.82] Okay.
[2272.90 → 2273.22] Awesome.
[2274.22 → 2275.02] Can you talk about that a bit?
[2275.10 → 2277.10] What can we expect?
[2278.04 → 2278.38] Sure.
[2278.38 → 2278.42] Sure.
[2279.30 → 2281.74] So we're working on this feature called pulses.
[2282.74 → 2290.56] The idea is you pick a few of the questions you've already asked and saved and up to five questions.
[2291.00 → 2294.26] And you can send those out to various channels.
[2295.34 → 2298.14] The two we're supporting initially are Slack and email.
[2298.14 → 2307.12] And so you can pick five questions, pick a channel or two channels, and pick a schedule.
[2307.62 → 2317.10] And we will automatically run those queries, you know, run those questions and send out the results to the channels that you selected.
[2317.78 → 2319.88] I can think of how that's going to be so useful.
[2319.88 → 2328.88] I mean, you know, for one, taking, you know, all this data knowledge and putting it in the hands of people who are creative enough to ask, you know, these creative questions, as Samir mentioned earlier.
[2329.32 → 2339.06] And now you're allowing them to craft questions that dig through this data and sort of snapshot it back to the internal team, I guess, anywhere.
[2339.30 → 2340.20] Slack is supported, really.
[2340.94 → 2342.28] Even open channels.
[2342.52 → 2349.14] It's just been one of those things I've seen at every single job I've ever had where at some point someone walks up and wants to find the email.
[2349.88 → 2350.32] Yeah.
[2351.04 → 2353.62] So it just kind of, it's the generalization of that.
[2353.88 → 2357.86] And then that person spends so much time, like, crafting these emails for people just to keep them updated.
[2358.26 → 2359.90] And that's just, that's just dumb.
[2360.10 → 2360.24] Yeah.
[2360.28 → 2360.76] Don't do that.
[2361.94 → 2364.88] Something like this makes me want, you know, maybe even a step further.
[2364.92 → 2368.74] And I'm wondering if, you know, perhaps these thoughts, you probably have had these thoughts for sure.
[2369.08 → 2374.70] But it's like, you talk about asking questions, but then we structure a query, basically.
[2374.70 → 2384.36] Um, it's almost like we need to take it the next level where you can actually have maybe categorized or formalized question styles that you can actually ask a question.
[2384.36 → 2390.16] Because once we start dealing with, like, you know, Slack integrations and, and, you know, email me every day.
[2390.22 → 2392.44] What, well, why don't I just be able to ask this thing a question?
[2392.48 → 2393.50] And it just gives me the answer.
[2393.50 → 2399.20] Just today, I was, I was wondering if there's a Slack bot way of saying, you know, how many people are on the website right now?
[2400.08 → 2407.60] Um, and it's like, I don't even want to go take that, turn it into a query and then, you know, do that extra step.
[2407.68 → 2415.44] It seems like even with this tool, which is definitely, you know, lowering things for many people to have access to data that wouldn't otherwise.
[2415.44 → 2424.42] It seems like, you know, you could, the Siri, the Verification of querying, um, if I could just move with a ridiculous term.
[2424.80 → 2425.96] It seems like that would be awesome.
[2426.16 → 2426.94] Like, what do you guys think about that?
[2426.94 → 2427.66] I like the term, dude.
[2427.82 → 2428.20] It's a good term.
[2428.28 → 2429.26] Verification.
[2429.78 → 2432.34] You know, we wanted to start with something pretty simple.
[2432.58 → 2438.10] Uh, you know, the, the minimum viable thing that we could do that's useful, um, for Slack integration.
[2438.10 → 2439.94] So that's, that's where we're starting.
[2439.94 → 2451.06] But, uh, I could definitely see us, you know, adding something like that in the future, uh, where you can just sort of type a free form question, and we try to parse it and, and give you the results back.
[2451.62 → 2455.22] That, I guess that Jared, your, your suggestion there assumes they have a long runway.
[2455.22 → 2462.84] And I guess maybe one more question before we dive deep into the tech side of things is, is we talked a bit earlier about pro versions and sustainability.
[2462.84 → 2470.16] Like how important is getting to some part where you all are making money as a company?
[2470.26 → 2471.00] Does that matter?
[2471.24 → 2472.06] Do you have funding?
[2472.34 → 2473.06] Do you have runway?
[2473.28 → 2474.84] Are we, are we concerned about things like that?
[2475.36 → 2481.02] So we have a bit of funding and I think it'll see us through, I mean, definitely in next year.
[2481.86 → 2485.98] Um, we're still trying to piece together exactly what it looks like from a company perspective.
[2485.98 → 2494.10] Um, I think one of the, you know, one of the strong reasons we are open sourcing all of it is we want to have a life outside just our company.
[2494.44 → 2502.88] Um, and so while, you know, in terms of my landlord needing me to pay rent, it's quite important that we somehow do make a living from all this.
[2503.14 → 2511.46] Um, I think there is, we expect to make money in ways that are not related to the actual core product and the user experience itself.
[2511.46 → 2516.38] How soon will we hear about a Metabases Cone?
[2518.26 → 2523.24] Um, as soon as there's 10 people that want to get together at an open bar.
[2523.48 → 2523.86] There you go.
[2524.08 → 2524.76] At a city near you.
[2525.76 → 2528.10] So it's, it's meet up first, then, uh, Cone next.
[2528.10 → 2528.52] Exactly.
[2529.08 → 2529.48] Exactly.
[2529.94 → 2533.70] We can call it, uh, Metafont, even when it's just an open bar, actually.
[2534.64 → 2535.78] I like, I like it.
[2536.20 → 2541.28] And this might be a good place to plug, well, it's mostly a joke right now, but we're talking about
[2541.28 → 2543.20] creating a, a microbrewery.
[2543.70 → 2544.06] Oh.
[2544.58 → 2548.86] And I forget the exact, um, beer names you've come up with, but Tom, do you remember what?
[2549.64 → 2555.04] Uh, well, there was a Meta Brewery or Meta, Meta Beer was the name of the brewery.
[2556.50 → 2558.02] Yeah, there was like actual, anyway.
[2558.02 → 2562.44] So yes, coming soon to a micro, to a Metafont near you.
[2562.44 → 2567.66] Uh, it kind of reminds me, I mean, it's a tangent, so forgive me, but when we were at
[2567.66 → 2574.74] Gopher Con, uh, this past July at the, uh, uh, Wine Coop Brewery, which is where the after
[2574.74 → 2579.48] party was for 1300 Gophers, um, you had to do something special, right?
[2579.50 → 2582.18] So they actually had a, uh, a special beer.
[2582.28 → 2584.84] Jared, do you recall what the beer was called for Gopher Con?
[2585.36 → 2586.98] I can only recall that it was delicious.
[2587.38 → 2587.96] It was delicious.
[2588.22 → 2588.72] That's true.
[2588.72 → 2590.64] What was it called?
[2591.26 → 2591.82] I don't know.
[2591.98 → 2592.44] I don't know.
[2592.72 → 2593.48] I can't remember.
[2593.58 → 2595.26] That's why I asked you, but it was good.
[2595.40 → 2596.00] I liked it.
[2596.08 → 2597.82] We're all striking out on beer names now.
[2597.90 → 2598.58] Oh man.
[2598.96 → 2599.42] All right.
[2599.42 → 2602.48] Well, let's get to the things we actually do know about, which is technology.
[2602.56 → 2603.28] At least I think so.
[2603.28 → 2608.08] So Samir, Tom, whoever wants to take this, uh, take us through some of, uh, what this
[2608.08 → 2608.70] is actually written.
[2608.78 → 2613.66] And I can understand 46% closure, 40% JavaScript, you know, what were some of the choices you had
[2613.66 → 2614.42] to make and why?
[2615.58 → 2618.58] Um, so it's had quite a few incarnations.
[2618.72 → 2620.30] And I guess I'll just kind of rattle them off.
[2620.30 → 2622.84] Um, and if anything's interesting, we can drill into them.
[2623.50 → 2630.14] Um, so it started off life as just a big ball of Python, um, with literally jQuery charts
[2630.14 → 2630.72] in the front end.
[2631.52 → 2637.98] Um, and at some point, uh, just brain damage of dealing with async in the Python world just
[2637.98 → 2638.98] got to be a little too much.
[2639.26 → 2644.78] Um, that plus we've always had the idea of making sure that it was super easy to install
[2644.78 → 2645.28] and deploy.
[2645.28 → 2650.96] And for all its flaws, the JVM is kind of awesome in that regard.
[2651.62 → 2655.66] Uh, there's something just magical about a single file you, you push around, whether
[2655.66 → 2659.28] it's Go or a JAR file, but there's something just compelling about that.
[2659.86 → 2662.56] Um, and so we played around with different options.
[2662.56 → 2665.24] We wrote little mini prototypes in a couple languages.
[2665.24 → 2670.34] I think at one point we settled on Scala, and we're in the process of rewriting it.
[2670.34 → 2675.52] Um, and just, just some of the associated brain damage for the team was just too much.
[2675.52 → 2676.60] And we switched to Clojure.
[2676.98 → 2680.82] And so that happened approximately January through March.
[2681.00 → 2686.84] It was kind of a rolling migration, and it's pretty much entirely in Clojure these days.
[2686.84 → 2692.40] There was a shred of Java for our migrations' framework, but, um, that's since imported.
[2693.06 → 2697.54] I know when I installed the Mac app to play with it a bit, um, I had to run Java.
[2697.66 → 2700.86] So is that the piece kind of lingering then to support the Mac app?
[2701.38 → 2707.62] Um, so actually the Mac app is ironically, um, all right, let me back up a second.
[2708.28 → 2712.72] So at this point in time, it's the Clojure app, which compiles down to a JAR file, which is
[2712.72 → 2715.34] run on the JVM, which is the Java virtual machine.
[2715.34 → 2721.76] Um, one of the, the main impetus for the Mac app originally was that it was a pain in the
[2721.76 → 2726.82] ass to install the Java, either the JRE, which is the Java runtime environment or the
[2726.82 → 2728.30] Java development kit on a Mac.
[2728.52 → 2735.68] And having watched a couple of my analyst coworkers or ex-coworkers or friends try to do it, it
[2735.68 → 2736.76] just became more and more painful.
[2736.96 → 2743.26] And so the original vision of the Mac app was just bundle the JRE with the actual JAR file
[2743.26 → 2745.22] and slap a web view on top of that.
[2745.34 → 2747.38] And it's kind of grown a little from there.
[2747.92 → 2752.70] So what you're seeing is just the JVM spinning up or sorry, the JRE spinning up in that separate
[2752.70 → 2754.86] little window you see with like core or something up.
[2755.14 → 2755.24] Yeah.
[2755.88 → 2756.90] I'd actually closed it.
[2756.92 → 2757.82] I was like, I don't want that running.
[2757.94 → 2760.90] And then, uh, yeah, you kind of want that.
[2761.70 → 2762.34] It's needed.
[2762.46 → 2763.06] It's important.
[2763.20 → 2763.40] Yeah.
[2763.86 → 2765.52] I could just go back a quick second.
[2765.52 → 2770.70] Sorry, Tom, if I could just, uh, wind you back to something you said there, Samir, uh,
[2770.70 → 2776.78] the switch from Scala to Clojure script, you said that the problem was all the associated
[2776.78 → 2777.60] brain damage.
[2777.68 → 2780.58] Could you just, could you, uh, unpack that for us?
[2782.12 → 2785.68] Um, so I've kind of blacked out a lot of that portion of my life to be perfectly honest,
[2785.68 → 2792.22] but of the bits that I recall, um, and it was, you know, obviously I had relative little
[2792.22 → 2793.78] to do with that change.
[2793.78 → 2798.16] It was Alan who Tom mentioned and Cam, another one of the backend guys.
[2798.70 → 2805.68] Um, so one of, one of the core sticking points was just a the fact that Scala, most of Scala
[2805.68 → 2810.58] SQL DSLs are strongly typed, which if you're generating dynamic queries is exactly what you
[2810.58 → 2815.26] don't want, because there's no way in which you can actually construct a type system that
[2815.26 → 2820.50] will know what some arbitrary user, uh, created query will, will have.
[2821.14 → 2825.74] Um, the other bit was just, it just felt, I don't know how to describe it.
[2825.76 → 2827.14] It just didn't feel fun.
[2827.14 → 2833.92] Um, and when Cam essentially just said, Hey, we want to do Clojure and wrote a prototype
[2833.92 → 2840.10] over a couple of days, it got to where about a week and a half worth of dedicated Scala
[2840.10 → 2842.80] coding, um, took us.
[2843.40 → 2848.32] And so that was like maybe a day or two of actual disclosure work by him at that point.
[2848.50 → 2852.48] And so, you know, kind of went around and around on it for a couple of days, or I think
[2852.48 → 2858.58] a week or two, and eventually just felt like a and more natural, um, language to express
[2858.58 → 2859.06] all of a sudden.
[2859.66 → 2865.34] And what I briefly mentioned our query language and how we kind of compile or transpire that
[2865.34 → 2866.60] to SQL or Congo.
[2867.20 → 2873.30] And that looks and feels a lot like just straight stream manipulation, which I've always found
[2873.30 → 2876.14] easier to do in a list rather than Scala.
[2877.14 → 2877.54] Yeah.
[2877.54 → 2881.70] I'd love it if you can dive a little bit deeper into the query language and kind of talk about
[2881.70 → 2882.40] what that's all about.
[2883.20 → 2883.72] All right.
[2883.72 → 2887.04] So I'm at least like a decade out of my compilers class.
[2887.04 → 2890.84] So if I misspeak, um, I hope no one flames me too hard.
[2891.56 → 2900.62] Um, but what we, what we tried to create is, um, a language you can express, um, a large
[2900.62 → 2907.42] set of interesting queries in, um, it, it's kind of like SQL, but, um, one of the one of
[2907.42 → 2909.94] the primary differences was it's meant to be composable.
[2909.94 → 2914.92] And so you can do things like save snippets and pass them around and that each snippet
[2914.92 → 2917.48] or subtree is pretty much uniquely determined.
[2917.88 → 2921.50] And so it's, it's really hard to slice up SQL and then pass it around.
[2922.14 → 2927.16] Um, it looks and feels a little like the AST you get if you, if you parse SQL.
[2927.70 → 2934.30] Um, and so a lot of, a lot of just my mental model for this comes from back in the day when
[2934.30 → 2939.16] I was doing genetic programming, where you do tree manipulations, and you express, uh, programs
[2939.16 → 2941.24] or designs in trees and you Fitz with them.
[2942.12 → 2946.28] And so we have essentially a query language that starts off with here's a bunch of operators.
[2946.94 → 2950.54] Here's, um, the various clauses in a, in a, in a query.
[2951.20 → 2955.92] Um, and here's ways to reference fields, to reference eventually macros, to reference,
[2955.92 → 2959.84] um, just aggregations and constants and operators.
[2960.50 → 2967.52] And that tree then gets passed to Coma or passed to the Congo driver and executed.
[2968.26 → 2969.02] Very cool.
[2969.02 → 2971.98] Well, it sounds like the back ends had a lot of, uh, work done to it.
[2972.02 → 2973.46] Let's, let's hear about the front end.
[2973.50 → 2977.90] Tom sounds like that's your playground with, uh, your history and building front ends.
[2977.98 → 2979.46] Can you tell us how that's all put together?
[2980.24 → 2980.60] Yeah, sure.
[2980.74 → 2989.14] Uh, so, uh, when I joined, uh, we were in process of transitioning from, uh, an angular front
[2989.14 → 2990.58] end to react.
[2990.58 → 2998.14] And, um, it's pretty early on in that process, uh, started with just the query editor, um,
[2998.42 → 3000.70] being, you know, built in, in react.
[3001.24 → 3006.90] And, uh, it was actually pretty easy to sort of drop in little pieces of, of React, uh,
[3006.90 → 3009.40] into a larger angular application.
[3009.40 → 3016.84] Um, and, uh, you know, since, since then we've ported more and more of the application over
[3016.84 → 3017.38] to react.
[3017.86 → 3024.42] Um, and we're almost at the point where there's no angular code left except for, uh, the routing
[3024.42 → 3026.54] and, uh, some controllers.
[3027.42 → 3032.84] Um, but we would really like to get rid of the rest of that, that angular code and, and,
[3032.96 → 3037.78] uh, do completely, complete, uh, react front on the front end.
[3038.40 → 3040.36] Um, but we're not quite there yet.
[3040.84 → 3041.24] Yeah.
[3041.26 → 3045.00] It seems like if you're not using too much of angular, having that as part of your payload
[3045.00 → 3047.28] is something that you definitely want to.
[3047.96 → 3048.36] Yeah.
[3048.46 → 3049.50] For yourself from at this point.
[3049.56 → 3049.72] Yeah.
[3050.44 → 3051.90] What about, uh, data transport?
[3052.00 → 3053.68] Like how's the front end and the backend talk?
[3053.68 → 3058.86] I know there's been a lot of, uh, hubbub around moving away from rest and onto these,
[3058.86 → 3063.22] uh, Falcon and Facebook's, uh, idea, which GraphQL.
[3063.90 → 3064.02] Relay.
[3064.70 → 3065.14] Yeah.
[3065.22 → 3065.50] Relay.
[3065.54 → 3065.90] Thank you.
[3066.44 → 3067.82] Any move in that direction?
[3068.54 → 3073.52] Uh, so right now it's just, uh, pretty much restful JSON APIs.
[3074.06 → 3079.16] Um, but those are definitely interesting ideas, uh, that I've been looking at.
[3079.46 → 3080.62] Uh, yeah.
[3080.62 → 3083.26] It'd be fascinating to, to see if we could apply those.
[3083.68 → 3085.00] Uh, to Metabase.
[3085.30 → 3089.80] Um, but for now, yeah, it's, it's pretty vanilla rest JSON.
[3090.74 → 3095.42] Just curious your thoughts on React in general as a person who's, you know, seen a lot of
[3095.42 → 3097.86] tools over the years in the JavaScript space.
[3099.02 → 3100.40] Uh, I, I love React.
[3100.64 → 3106.54] Um, the thing I've sort of been struggling with is, uh, you know, React is, is great for
[3106.54 → 3109.62] taking some data, turning it into UI.
[3110.34 → 3113.24] Um, but it's not, it's not the whole picture.
[3113.60 → 3117.60] Uh, you know, you need, you need something else to sort of manage that state.
[3117.92 → 3124.02] Um, whether it's Flux or something like Relay or, um, or what have you.
[3124.02 → 3131.60] But we're, uh, we're starting to look at using Redux, which is a, uh, it's, it's Flux-like.
[3131.76 → 3135.84] I don't know if it's technically considered Flux, but, uh, it's, it's sort of a unidirectional,
[3135.84 → 3138.24] uh, data flow framework.
[3138.24 → 3145.82] It's very functional and, uh, focused on immutable, uh, objects and that sort of thing.
[3145.98 → 3150.96] So, um, we've been using that in bits and pieces of, of the front end.
[3151.04 → 3156.86] Uh, but it's not, we're not using it for the entire application state.
[3156.86 → 3159.28] It's more like little silos within the application.
[3160.14 → 3162.50] Um, yeah, Redux is interesting.
[3162.50 → 3166.86] Actually, we just had a, a ping on our ping repo, which is kind of our open inbox where
[3166.86 → 3168.40] people can give us show suggestions.
[3168.80 → 3169.20] Yeah.
[3169.34 → 3173.32] Dan, uh, I think Dan Abrams, Abrams, uh, Abrams.
[3173.48 → 3173.88] Yeah.
[3174.44 → 3174.66] Yeah.
[3174.72 → 3175.76] He'd be a great person to have.
[3176.48 → 3176.68] Yeah.
[3176.70 → 3177.76] He actually agreed to come on.
[3177.82 → 3178.84] We just haven't scheduled it yet.
[3178.96 → 3181.56] So look forward to that everyone.
[3181.56 → 3190.56] And, um, let's get back to databases again, because we have, uh, Postgres, MySQL, uh, Redshift,
[3190.66 → 3192.34] which I think is like planned, but not yet supported.
[3193.24 → 3196.70] Um, H2, which could you explain H2?
[3196.70 → 3198.06] For us non-Java people?
[3199.68 → 3202.96] Um, H2 is just an embedded database in Java land.
[3203.18 → 3206.96] It's morally equivalent to SQLite in many ways.
[3207.80 → 3208.30] Okay.
[3208.62 → 3211.62] So it's there just for a, a nice default, basically.
[3211.62 → 3218.28] We use that as our, our default, uh, database for Metabase's own data.
[3218.84 → 3222.50] Uh, so you don't need to set up, uh, Postgres or MySQL.
[3222.50 → 3222.58] Cool.
[3222.88 → 3223.40] Very cool.
[3223.64 → 3228.76] And anything else, uh, technology-wise that you guys are using in part of your stack that
[3228.76 → 3229.58] we haven't touched on?
[3230.14 → 3232.30] Uh, I see that you got an Xcode project in there.
[3232.36 → 3237.32] Obviously there's a little Mac app, which appears to be a web view, um, which makes a lot of sense.
[3237.64 → 3239.80] Anything else that you're doing technologically that's noteworthy?
[3239.80 → 3240.28] Yeah.
[3240.72 → 3242.76] I mean, I'm, I think there's some other interesting stuff.
[3242.82 → 3245.24] I'm not sure exactly what it is off the top of my head.
[3245.78 → 3251.24] Um, so switching back in, there are some interesting things we're doing around just fingerprinting
[3251.24 → 3254.58] columns and trying to infer the semantic model.
[3254.58 → 3261.46] Um, what we've shipped to date is really just, uh, sort of the minimum by minimum usable,
[3261.46 → 3267.70] um, set of rules and heuristics, but we're hoping to really push those as far as possible.
[3267.70 → 3273.40] At some point, you know, my pipe dream is I load it up, I point it to a data warehouse
[3273.40 → 3277.98] and it automatically knows everything that I could tell it about the underlying data model.
[3277.98 → 3285.94] Um, obviously that's, you know, years or decades away, but that at least is the hope, um, rather
[3285.94 → 3292.16] than having to sort of point a database and spend hours or days restructuring data, uh,
[3292.32 → 3297.12] annotating things and just moving it from like, Hey, it's kind of cool out of the box to this
[3297.12 → 3298.90] measures everything that I want it to measure.
[3299.96 → 3305.78] One more question before we break is we mentioned earlier, um, you know, the thing about meetups
[3305.78 → 3311.90] and comps, and we've talked about why Metabase is open source, but even inside open source,
[3311.90 → 3313.86] there are different kinds of open source.
[3313.86 → 3318.24] And I'm curious, um, what kind of open source project you want this to be?
[3318.42 → 3322.40] One hint that you gave is that you were very excited if somebody would submit everything
[3322.40 → 3323.20] DB driver.
[3323.76 → 3329.38] Um, are you hoping this becomes a large community effort or is this an open source product that,
[3329.38 → 3332.34] you know, Metabase employees are going to work on in the open?
[3332.34 → 3334.98] I think initially it's going to be the latter.
[3335.70 → 3340.52] Um, and part of the reason is we're trying to be really meticulous and thoughtful about
[3340.52 → 3345.84] the front end and specifically on the design side and making sure that, uh, what comes out
[3345.84 → 3350.96] of the process looks and feels like an application that you use today.
[3351.48 → 3356.88] Um, and one of the one of the things that the open source community has been, um, has had
[3356.88 → 3359.40] mixed results in is just creating end user interfaces.
[3359.40 → 3364.86] And so at least on the front end of things, we're going to be pretty OCD and pretty meticulous
[3364.86 → 3367.18] and just very ordinary about that.
[3367.86 → 3374.40] Um, and so, you know, while we definitely would love people to help out, we, you know,
[3374.40 → 3375.58] we want a vibrant community.
[3375.58 → 3380.24] We're primarily, we're in the open source because we want to give back and not so much
[3380.24 → 3383.62] because we're looking for contributions or fishing for people to help us out.
[3383.62 → 3384.26] Okay.
[3384.90 → 3387.98] Actually, I mean, I, I agree with everything Samir said.
[3388.24 → 3394.96] Um, I think there are very specific, you know, integration points that would be perfect for
[3394.96 → 3398.16] open source, uh, contributors to, to help out with.
[3398.22 → 3399.90] And I mean, drivers are definitely one of them.
[3400.46 → 3405.60] Um, I think we, we don't have a great API for it yet, but this, this pulses thing that,
[3405.60 → 3410.24] uh, we were talking about earlier, you know, different integrations, uh, with different
[3410.24 → 3418.10] external services, um, and maybe eventually different charting, uh, charts and graphics
[3418.10 → 3419.24] and that sort of thing.
[3419.24 → 3424.90] So there are a bunch of different areas that I think, uh, it would be great for, for us
[3424.90 → 3433.38] to sort of document and, uh, expose very clean APIs that external developers could use to extend
[3433.38 → 3434.02] Metabase.
[3434.88 → 3435.08] Very cool.
[3435.12 → 3438.78] Well, let's take a quick moment here from another one of our sponsors on the other side of the
[3438.78 → 3439.04] break.
[3439.10 → 3442.80] We will talk about getting started, how you can actually get Metabase up and running
[3442.80 → 3445.84] today, pointing at your company's databases.
[3446.68 → 3449.50] Um, and we will also ask our closing questions.
[3449.50 → 3450.36] So stay tuned for that.
[3450.42 → 3451.00] And we'll be right back.
[3452.92 → 3458.16] Digital ocean has expanded their reach even further into Canada startup and developer scene
[3458.16 → 3459.80] with the launch of Tor one.
[3459.94 → 3461.32] That's T O R one.
[3461.32 → 3468.24] Their first Canadian data centre in Toronto, head to digital ocean.com and use the code change
[3468.24 → 3470.16] law to get a $10 hosting credit.
[3470.26 → 3476.32] When you sign up again, digital ocean.com use the code change law to get a $10 hosting
[3476.32 → 3476.66] credit.
[3476.80 → 3477.90] When you sign up.
[3480.96 → 3484.36] All right, we are back talking about how do you get started with Metabase?
[3484.40 → 3490.06] So I'm out there, I'm a developer or, um, an interested person with some technical chops
[3490.06 → 3495.54] and I want to get Metabase deployed maybe, uh, on some personal projects or maybe for my company.
[3495.54 → 3500.30] Um, take us beyond the Mac app and the just the plane with the dummy data.
[3500.58 → 3504.20] How do you actually get this thing set up and running in kind of production capacity?
[3504.94 → 3510.08] So our primary production platform these days is, uh, elastic beanstalk on AWS.
[3511.00 → 3515.32] Um, in theory, anywhere you can run a jar, you can run Metabase.
[3515.32 → 3520.46] And so depending on what world you live in, um, we also have a Heroku deployed, uh, which
[3520.46 → 3524.66] is very functional, but I wouldn't say it's quite production grade yet.
[3525.22 → 3531.02] Um, and so if you're actually trying thinking about doing it for real, I'd say either, um,
[3531.30 → 3539.22] use the jar, pass in SSL, um, pass in your SSL key store, uh, or reverse proxy it and, uh,
[3539.22 → 3542.46] terminate there, um, or set it up on beanstalk.
[3542.58 → 3548.98] And we have a set of, we have both a, a button that will pre-fill a lot of the beanstalk settings
[3548.98 → 3552.78] for you, but that'll take something in the neighbourhood of 15 to 30 minutes.
[3553.20 → 3553.94] Kind of get that up.
[3554.50 → 3558.90] Um, and if you just want to play around with things in it without putting in that much effort,
[3558.98 → 3563.60] you can just download the jar, uh, slap it on instance or, uh, server somewhere.
[3563.60 → 3571.06] And just do a java dash jar at Metabase.jar and then log into it, um, on port 3000.
[3571.60 → 3573.30] And it should quote unquote, just work.
[3574.04 → 3575.36] It should quote unquote, just work.
[3575.42 → 3578.30] And where do you go when it quotes unquote, doesn't just work?
[3578.40 → 3581.24] Like where, where do we go for support or help, or what have you?
[3582.28 → 3585.28] Um, so Twitter always works at Metabase.
[3585.44 → 3593.56] Um, we also have, um, at discourse.metabase.com, uh, forum for our users to kind of chime in and
[3593.56 → 3595.74] talk shit or get help.
[3596.32 → 3601.76] Um, and then if it's something that you think is actually a bug or a feature request to get
[3601.76 → 3603.40] up issues as a place to get in touch with us.
[3604.38 → 3604.92] Very good.
[3604.94 → 3606.74] We'll be sure to link all those up in the show notes.
[3606.82 → 3608.30] This is episode 182, by the way.
[3608.30 → 3614.26] So if you're not listening inside some sort of podcast client, uh, go to changelog.com slash
[3614.26 → 3615.88] one eight two for the show notes.
[3616.06 → 3619.34] If you're in a podcast client, well, you probably know where the show notes are.
[3620.10 → 3620.90] Um, very cool.
[3620.92 → 3622.44] Well, let's briefly touch on the future.
[3622.44 → 3623.58] I think we've done that a little bit.
[3623.66 → 3625.40] I think the Slack integration is exciting.
[3625.96 → 3630.08] I think we talked far future where I can just shoot you a question and Metabase answers
[3630.08 → 3630.92] them like a genie.
[3631.48 → 3634.16] Um, what else, what else do you have?
[3634.20 → 3634.88] What are you planning?
[3635.00 → 3636.78] What does Metabase look like in three years?
[3636.84 → 3637.84] What does it look like in five years?
[3637.84 → 3645.84] Um, I think in five years we expect to build just the standard open source BI platform.
[3645.84 → 3653.44] Um, we're currently very useful for companies that are, you know, in the five to 50 person
[3653.44 → 3654.88] employee range.
[3654.88 → 3663.46] Um, and we're just trying to build the foundation for data access just for all companies, uh,
[3663.46 → 3664.80] in the three to five year timeframe.
[3664.80 → 3669.14] So, you know, there's nothing we don't lack for ambition.
[3669.26 → 3672.86] We don't lack for, um, kind of crazy pie in the sky stuff.
[3672.86 → 3679.90] I mean, I'll throw out one of my, one of my pet projects is just trying to give people
[3679.90 → 3682.04] a really simple way to do graph traversal.
[3682.82 → 3686.08] Um, and so it's not something that most people talk about in the concept analytics, but there's
[3686.08 → 3692.28] a lot of really common, really useful, really natural questions to ask, um, that are really
[3692.28 → 3695.28] just, uh, walking a couple edges in a graph.
[3695.28 → 3700.92] And so having the ability to do things like, Oh, I want to see who complained about, um,
[3701.52 → 3705.12] this album last week and how do they feel about these other albums?
[3705.30 → 3708.80] How did those albums they're complaining about do in other reviews?
[3709.02 → 3713.24] And it's the ability to kind of take those questions, which in conversational English
[3713.24 → 3718.62] sound very innocent, but if you try to encode them in SQL, it rapidly gets pretty annoying.
[3719.36 → 3722.46] Um, and make that something that's one or two clicks away.
[3723.08 → 3723.48] Awesome.
[3723.48 → 3727.90] I think I have time, so I'm going to, I'm going to pull a quote that I got off of Twitter.
[3728.00 → 3735.86] I think this was a fellow by the handle EDW519, a very interesting developer with lots of interesting
[3735.86 → 3736.42] little quips.
[3736.54 → 3741.82] One thing he said, which I thought of when we started this call is he tweeted, no, no one
[3741.82 → 3744.64] would pay seven figures for a very fancy report writer.
[3745.08 → 3750.76] So they had to rename it business intelligence, which I thought was kind of funny and true to
[3750.76 → 3751.36] a certain degree.
[3751.36 → 3757.38] So that got me thinking, you know, if Metabase is successful, you know, um, I want to hear
[3757.38 → 3762.38] your thoughts on perhaps eliminating an entire job title inside many organizations.
[3763.34 → 3771.88] Um, this is perhaps a little, um, inflammatory, but I don't think job ever disappear.
[3771.88 → 3776.42] I just think that as time opens up, we find new and creative ways to fill them.
[3777.36 → 3785.30] And so what I, what I think will happen is that, you know, the roughly 20 to 40% of an
[3785.30 → 3789.98] analyst's day, which is fielding these ad hoc questions will go away.
[3789.98 → 3794.76] But A, they'll have more time to do the stuff they actually enjoy and the creative sort of
[3794.76 → 3802.20] deeper explorations and just the more intricate, um, the more intricate question and hypothesis
[3802.20 → 3804.86] testing and exploration they do.
[3805.58 → 3811.00] Um, the flip side of this is I don't, in most places, it's really hard to get numbers
[3811.00 → 3811.34] right.
[3811.34 → 3817.42] And so if you're, you know, one developer with a database that backs an app and you
[3817.42 → 3822.00] want to create a few graphs for yourself, it's really easy to, to sort of say those are the
[3822.00 → 3822.72] numbers that were cool.
[3823.08 → 3827.28] Um, if you're in a complicated place with, you know, dozens of different data sources
[3827.28 → 3833.44] with different views of the same data in different places, different roll-ups, a lot of what sort
[3833.44 → 3837.80] of business intelligence analysts at big companies do is not create those reports or create those
[3837.80 → 3838.24] dashboards.
[3838.46 → 3844.12] It's trying to figure out why, you know, this revenue number or this DAU is not the
[3844.12 → 3845.48] same as this other report.
[3845.86 → 3847.56] And I don't think that's ever going to go away.
[3848.56 → 3852.26] We hope to make that simpler and easier, but fundamentally, there's just a lot of human
[3852.26 → 3859.34] labour involved that we're at least one main, you know, one generational AI advanced away
[3859.34 → 3861.76] from being able to tackle or even hope to tackle.
[3862.34 → 3862.40] Yeah.
[3863.46 → 3864.80] No, I like that perspective.
[3864.80 → 3869.90] You're not replacing people, you are taking people and making them more effective in what
[3869.90 → 3874.06] their role is and allowing them to free up time that they would be doing manual labour
[3874.06 → 3877.88] and asking and answering more interesting questions.
[3878.98 → 3883.16] Um, and for those who were just dead weight, you know, you all are just dead weight.
[3883.36 → 3886.86] So you have to find something else to do.
[3887.00 → 3888.84] Well, it's, it's true.
[3889.04 → 3889.80] It happens.
[3890.36 → 3891.16] Jeez, dude.
[3892.28 → 3892.68] Yeah.
[3892.68 → 3897.80] That's what they keep saying, you know, the pretty soon the computers will just write
[3897.80 → 3898.86] the programs for us.
[3899.44 → 3901.44] Um, and we'll all keep hoping.
[3901.82 → 3902.16] Yeah.
[3902.20 → 3904.62] And it's like, well, I'll just go get a margarita at that point, I guess.
[3906.70 → 3907.06] Okay.
[3907.28 → 3913.88] Any other salient points, uh, Adam or, uh, Samir or Tom, you guys would like to make before
[3913.88 → 3915.24] we switch to our closing questions?
[3917.18 → 3919.60] Um, just go download it.
[3919.88 → 3920.64] Tell us what you think.
[3921.34 → 3921.74] Complain.
[3922.64 → 3924.20] Um, let us know how to make things better.
[3925.00 → 3927.78] I have one side note before we continue.
[3927.86 → 3932.06] And it's, it's just because I have to ask because I put it in the notes, and I'm just curious
[3932.06 → 3938.24] if by any chance you borrowed from the playbook of WordPress when it came to the user experience
[3938.24 → 3941.26] of connecting to a database with Metabase.
[3942.32 → 3946.80] Um, I think I've had WordPress in my mind for a large part of the journey.
[3947.42 → 3953.50] Um, but not like I'm honestly not, I've never used WordPress that heavily, but there is a
[3953.50 → 3957.56] certain magical instant gratification angle that they've worked out.
[3957.56 → 3962.20] Um, and in the times that I've had to set up WordPress instances for other people,
[3962.20 → 3966.74] um, it's been remarkably pain-free compared to other things I've done.
[3966.74 → 3974.36] Um, so there's always the intention of providing some sort of instant gratification in like under
[3974.36 → 3979.42] five minutes that I, that we definitely were inspired by WordPress on that front.
[3979.42 → 3988.70] Um, it seemed like that was the if it wasn't on purpose, it seemed like maybe it was by happenstance,
[3988.70 → 3994.44] but, uh, just the, the process of like, there's a database either created by you recently that you're
[3994.44 → 3998.46] pointing to or one out there that's, you know, obviously there you've got credentials, and you're
[3998.46 → 4002.08] pointing it to, and it just seemed very familiar when I was reading those docs, and I was like,
[4002.10 → 4002.94] I have to ask that question.
[4002.94 → 4008.04] Um, I don't think any of us have used WordPress lately.
[4008.04 → 4014.78] So if it was something we again, were inspired by, it was something very subconscious.
[4016.14 → 4016.50] Totally.
[4016.64 → 4017.98] And it wasn't meant like, Oh, you stole that.
[4018.00 → 4020.02] It was just more like, cause because you're right.
[4020.02 → 4024.34] Like they, the instant gratification of setting up WordPress is pretty painless.
[4024.38 → 4025.60] It's been a while since I've done it too.
[4025.64 → 4031.50] We, we use WordPress, uh, here at the changelog for our site, but you know, it's been years since
[4031.50 → 4032.90] I've set up a WordPress install.
[4032.94 → 4035.98] But I know the, the process and it seemed similar.
[4036.76 → 4037.32] All right.
[4037.34 → 4039.88] Now we, uh, now we're going into the closing questions here.
[4039.92 → 4041.00] Which one do you ask first, man?
[4041.30 → 4043.04] Hero, radar or what?
[4043.74 → 4043.84] Yeah.
[4043.88 → 4046.90] I think we should ask programming hero because it gives me an opportunity to mention.
[4047.32 → 4050.38] We just launched season two of beyond code.
[4050.48 → 4050.68] True.
[4050.82 → 4051.22] Programming.
[4051.38 → 4054.06] Who is your programming hero is one of the feature questions on beyond code.
[4054.44 → 4056.12] Uh, season two now out there.
[4056.20 → 4056.64] Check it out.
[4056.72 → 4059.56] Beyond code.tv slash space city JS.
[4059.56 → 4065.90] For those of you who are out there in Houston, uh, you can now go there and watch your beyond
[4065.90 → 4069.32] code interviews and find out who your programming heroes were.
[4069.44 → 4070.94] So quick shout out to that.
[4071.28 → 4073.44] And now fellows, we'll turn the question on you.
[4073.68 → 4076.94] Uh, let's toss this one to Samir and then Tom can take the next question.
[4077.94 → 4082.04] So Samir, who, if you had to name it would be your programming hero and why?
[4082.04 → 4085.80] I mean, on some level I've always wanted to be Jeff Dean.
[4086.94 → 4090.30] Jeff Dean, please, uh, explain, explain.
[4091.46 → 4096.86] Uh, I'm sure I'm going to get a lot of this wrong, but he was one of the, um, four programmers
[4096.86 → 4097.46] at Google.
[4097.94 → 4104.64] Um, so he, and I'm not sure exactly how credit is distributed, but he had a piece in a lot
[4104.64 → 4107.10] of the foundational technologies that made Google, Google.
[4107.10 → 4115.16] So Map Reduce, Bistable, um, and just by all accounts, he's a really nice guy, really, really
[4115.16 → 4121.02] humble, perfect to talk to, and has had his fingers in some of the biggest projects
[4121.02 → 4124.80] and some of the most impressive things that have happened in the last couple of decades.
[4125.68 → 4130.70] Well, it's no wonder why, uh, I'm jumping the gun, but in your email, you mentioned TensorFlow,
[4131.14 → 4134.68] which is also credited to him or to some point.
[4134.68 → 4139.10] Um, yeah, I'm not actually sure exactly if it worked on that.
[4139.30 → 4144.24] I know, um, Vincent, and I'm going to mangle his name despite the fact that we're, I know
[4144.24 → 4147.52] the guy, um, has worked on it.
[4147.76 → 4150.84] Um, I, yeah, I'm not sure who worked on it.
[4150.86 → 4151.70] I think it's very interesting.
[4151.84 → 4157.82] I think it's, there's a lot around the open source ML world that I've been following for
[4157.82 → 4158.10] a while.
[4158.16 → 4160.34] And there are a lot of reference implementations.
[4160.34 → 4162.78] There's a lot of, um, execution platforms.
[4162.78 → 4167.10] Uh, one of the things I really liked about it was the fact that there is this, this visual
[4167.10 → 4170.84] kind of inspector and debugger and just kind of anchor.
[4171.70 → 4174.96] Um, and I have not fully internalized it.
[4175.02 → 4179.96] I haven't run any, any real, any, um, classifications, any real data I have yet.
[4180.34 → 4183.92] Um, but it's definitely something I'm kind of poking and prodding and staring at for the
[4183.92 → 4184.50] last couple of days.
[4184.50 → 4190.78] That might be a little bit inside baseball, even for our audience, um, because TensorFlow
[4190.78 → 4193.24] just like, just was announced yesterday.
[4193.56 → 4197.18] So, uh, it's on his Wikipedia on, uh, is it on Jeff Dean's Wikipedia?
[4197.18 → 4201.58] That's why I mentioned it because career at Google, it's the last one on the list, you
[4201.58 → 4205.84] know, Spanner, Big Table, Map Reduce, Google Brain, Level DB and TensorFlow.
[4205.84 → 4210.74] So I just, I, I jumped the gun, but I assume that may have been another reason why you chose
[4210.74 → 4210.86] Jeff Dean.
[4210.86 → 4214.18] I didn't even know that, but yeah, I mean, that, that only makes it more impressive in
[4214.18 → 4214.58] my eyes.
[4215.72 → 4221.42] This, uh, look, just TensorFlow, the new machine learning, uh, framework that Google announced
[4221.42 → 4223.22] at the end of 2015.
[4223.78 → 4228.98] Uh, looking at their GitHub, there's only two contributors, a guy named Kievan and somebody
[4228.98 → 4236.24] named BRV, but those could be, this whole thing may not have been on Git eventually or originally.
[4237.50 → 4239.82] Anyway, now I'm getting into the weeds.
[4240.50 → 4243.04] Do we want to give the hero question to Tom too or no?
[4244.60 → 4250.84] Actually, Jeff Dean was on my list as well, but, um, yeah, uh, John Carmack would be another
[4250.84 → 4251.20] one.
[4252.20 → 4254.94] The classic, uh, game.
[4255.42 → 4256.08] John Carmack.
[4256.26 → 4256.30] Yes.
[4256.30 → 4261.88] So Jeff, I think Jeff Dean is probably unique to you guys as far as I had never even heard
[4261.88 → 4262.30] of Jeff.
[4262.88 → 4265.20] Um, my fault, not his, I'm sure.
[4265.42 → 4268.72] But John Carmack is kind of an old favourite lot.
[4268.82 → 4270.72] He's, he's the programming hero of many folks.
[4270.84 → 4274.26] So, um, one, one new one and one old one there.
[4274.32 → 4275.68] Why, why John Carmack?
[4276.02 → 4278.58] Maybe self-explanatory, but if you could just humour us.
[4278.92 → 4285.96] Uh, I mean, he's, he's, uh, got incredible history with, you know, game programming as well
[4285.96 → 4288.36] as, uh, just programming in general.
[4288.68 → 4292.38] Um, yeah, uh, there's not, not, not too much else to say.
[4293.32 → 4295.88] So his reputation precedes him, and he's awesome.
[4296.04 → 4296.54] Long story short.
[4296.66 → 4296.80] Yeah.
[4296.90 → 4300.24] I mean, he, I, he, he gives great talks as well.
[4300.32 → 4303.34] Um, or at least, or blog posts and that sort of thing.
[4303.34 → 4308.12] So trying to remember Jared, who, who else may have mentioned John Carmack.
[4308.60 → 4309.46] Can you recall?
[4309.64 → 4310.56] There's been multiples.
[4311.06 → 4311.76] Karen Meyer.
[4311.98 → 4314.02] I think, I think for some reason she mentioned him.
[4314.78 → 4315.26] Yeah.
[4315.26 → 4318.84] I'm pretty sure he's been mentioned three or four times over, over the years.
[4320.20 → 4325.50] He's also very kind of open and out forthright on Twitter, which is very interesting.
[4325.56 → 4330.24] There seems to be very little filter between his brain and, uh, the, the Twitter submit
[4330.24 → 4330.64] box.
[4330.64 → 4332.54] Because he'll just throw stuff out there anyway.
[4333.72 → 4334.24] All right.
[4334.24 → 4337.74] Let's, uh, let's talk about the open source radar.
[4338.50 → 4343.86] Um, so either of you guys, I guess we'll go with Samir first, but you know if you had
[4343.86 → 4347.50] a week in the hack, and it wasn't on Metabase, and it was totally for fun, and you were like,
[4347.54 → 4349.26] man, I've been dying to play with this.
[4349.48 → 4350.10] What would it be?
[4350.82 → 4351.66] You can't pick TensorFlow.
[4352.62 → 4355.16] Oh, uh, Tom, what do you think?
[4355.40 → 4356.96] Give me a few seconds to think about that.
[4356.96 → 4364.46] Um, so I mentioned some of, some of the we've talked about, um, was it, uh, Facebook's
[4364.46 → 4372.16] relay net, net, this is Falcon and Ohm next are all sorts of rethinking the way you,
[4372.22 → 4377.16] you do client server, uh, communications and web apps.
[4377.16 → 4381.98] And, uh, those are all pretty interesting where you, you sort of describe exactly the
[4381.98 → 4384.20] data that your UI components need.
[4384.88 → 4391.62] And, uh, you send one big request to the server, and it sends everything back in one request.
[4391.72 → 4397.10] And, uh, it's very unrestful, but it's, uh, you know, it simplifies things because you don't
[4397.10 → 4402.50] need to add a new endpoint to your backend every time you want to add a new feature to your front
[4402.50 → 4402.78] end.
[4402.78 → 4405.76] That just reminds me of something that I forgot to ask.
[4405.94 → 4410.14] So while we're, while we're doing this, um, one thing that I thought of is, well, you got
[4410.14 → 4415.02] closure on the backend, but, uh, is there any interest or thought of closure script on the
[4415.02 → 4417.34] front end just to unify your languages across the code base?
[4417.74 → 4418.18] Yeah.
[4418.34 → 4420.92] Um, I, I think that's, that's an interesting idea.
[4420.92 → 4427.14] Uh, you know, closure script in, and Ohm is, uh, basically a React binding or a closure
[4427.14 → 4428.38] script binding to react.
[4428.38 → 4430.18] Um, right.
[4431.04 → 4432.96] So I think that'd be fascinating.
[4433.10 → 4438.22] I mean, one, one advantage of sticking with JavaScript is, uh, it's a little more accessible
[4438.22 → 4443.34] to, um, broader range of developers as well as designers.
[4443.58 → 4450.00] Um, you know, designers can look at JSX and see, you know, that it's basically HTML.
[4450.00 → 4457.62] Um, so, you know, we have our, our designers on our team are able to, uh, do a lot of work
[4457.62 → 4462.88] on, on components, uh, in react and JSX and JavaScript.
[4463.26 → 4467.02] Whereas, uh, closure script would add a little bit more overhead to that.
[4467.02 → 4469.56] So, yeah, that's interesting.
[4469.66 → 4476.72] When we had Facebook on, we asked specifically about JSX and if that was, um, heart, unapproachable
[4476.72 → 4481.80] from a designer's perspective, because they're so used to, you know, working with HTML and
[4481.80 → 4485.02] CSS as separate things and staying away from JavaScript, perhaps.
[4485.66 → 4488.60] Um, but they said internally they haven't found that to be an issue.
[4488.76 → 4493.28] And that you, when you think that you're just not giving designers enough credit or something,
[4493.28 → 4497.26] um, have you found, so it sounds like you found that to be the similar where your designers
[4497.26 → 4500.90] are just fine working with react and JSX and no big deal.
[4501.28 → 4501.38] Yeah.
[4501.52 → 4501.70] Yeah.
[4501.84 → 4508.30] Uh, I mean, certainly they, they're able to, uh, implement basic components and, or tweak
[4508.30 → 4510.94] existing components, um, just fine.
[4510.94 → 4514.02] So, but maybe that's, uh, an anomaly among our designers.
[4514.02 → 4519.60] So, well, it sounds like at least you met a base on Facebook, at least, uh, corroborating
[4519.60 → 4520.22] evidence there.
[4520.34 → 4522.36] All right, Samir, we stalled for as long as we could.
[4522.36 → 4525.44] Have you thought of something besides TensorFlow that's on your radar?
[4526.44 → 4530.30] Um, I think, I mean, this is just me speaking from my own kind of background.
[4530.64 → 4539.34] I'm really curious where speech recognition and, um, uh, NLP libraries have gotten to in
[4539.34 → 4540.10] certain years.
[4540.42 → 4545.50] So I think if I actually had a couple of hours to bang away on a weekend, I'd probably just
[4545.50 → 4550.78] throw together something that, you know, try to take our voices and going back to your
[4550.78 → 4555.42] idea about sort of the verification of Metabase, playing around with that.
[4556.28 → 4560.34] Not as much in the context of a feature for Metabase, but just to see where that world has
[4560.34 → 4560.76] gone to.
[4561.28 → 4561.60] Yeah.
[4561.64 → 4564.08] Perhaps proof of concept or at least just to explore.
[4564.40 → 4564.66] Yep.
[4564.66 → 4566.46] All right.
[4566.52 → 4568.74] Well, Tom and Samir, it's been a blast having you on the show.
[4568.84 → 4571.64] Thanks so much for taking the time to join us today.
[4572.18 → 4575.76] I'm sure it's got to feel pretty awesome to be a couple of years into this project and
[4575.76 → 4579.90] just kind of get the chance to come on a show like this and share with the open source
[4579.90 → 4582.70] world what's going on with Metabase and get people pretty excited.
[4582.70 → 4585.10] So I want to turn it back over to you though, guys.
[4585.36 → 4588.64] Is there anything else you want to cover before we head on out of the show?
[4590.00 → 4590.98] It's been a blast.
[4591.10 → 4591.92] Thanks for having us.
[4592.06 → 4596.20] I've really enjoyed it and looking forward to hearing more from you guys.
[4597.24 → 4599.70] And so listeners go to Metabase.com.
[4600.48 → 4601.62] That's an awesome dot com, by the way.
[4601.70 → 4602.18] I love it.
[4602.48 → 4605.90] And at Metabase on Twitter, which is super cool.
[4607.48 → 4612.40] I want to thank our sponsors for sponsoring the show, Code Chip, Top Tile, Harvest, and also
[4612.40 → 4613.06] Digital Ocean.
[4613.40 → 4617.68] And of course, our listeners, we would not go to show without thanking you and those
[4617.68 → 4621.14] members who support us and wear and rock the Change Log T.
[4621.36 → 4622.06] You are awesome.
[4622.60 → 4623.64] And I owe you a hug.
[4624.00 → 4625.34] But for now, fellas, say goodbye.
[4626.10 → 4626.64] Thanks, guys.
[4626.70 → 4627.38] Really appreciate it.
[4627.82 → 4628.22] Thank you.
[4628.44 → 4628.82] Thank you.
[4628.82 → 4628.90] Thank you.
[4642.40 → 4662.78] Thank you.
