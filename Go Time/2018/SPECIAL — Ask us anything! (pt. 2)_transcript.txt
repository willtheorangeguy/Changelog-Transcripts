[0.00 --> 2.88]  Bandwidth for ChangeLog is provided by Fastly.
[3.22 --> 5.30]  Learn more at Fastly.com.
[5.64 --> 7.18]  Error monitoring is provided by Rollbar.
[7.56 --> 9.28]  Check them out at Rollbar.com.
[9.58 --> 11.56]  And we're hosted on Linode servers.
[11.98 --> 14.00]  Head to linode.com slash changelog.
[14.00 --> 34.10]  It's Go Time, a weekly podcast where we discuss interesting topics around the Go programming language, the community, and everything in between.
[34.44 --> 38.46]  If you currently write Go or aspire to, this is the show for you.
[44.00 --> 54.72]  The document should be up to date for all of the questions we've got.
[55.06 --> 56.30]  Up to when?
[56.80 --> 58.64]  Up until just a couple minutes ago.
[58.88 --> 65.24]  So we'll take the 3 p.m. mark in Slack as anything that comes in after that is new questions.
[65.24 --> 68.82]  And we will try to pay attention as best as we can.
[69.50 --> 70.22]  Or not.
[70.30 --> 71.50]  If you're late, too bad.
[72.30 --> 72.58]  Right.
[72.74 --> 73.80]  You had a chance.
[74.88 --> 77.04]  So, AMA episode.
[77.50 --> 79.74]  This is going to be our second shot at that.
[80.38 --> 84.92]  And if you're listening right now, please let us know whether you like these or don't.
[85.46 --> 89.54]  And if you do like them, we'll try to do them more frequently.
[89.92 --> 93.68]  I don't know whether that'll be monthly or every other month or something like that.
[93.68 --> 95.68]  But we can come up with kind of a consistent schedule.
[96.62 --> 102.50]  And we will, like, maybe set something up where we can just take questions all the time.
[102.94 --> 107.16]  So whenever you think of a question, just throw it in and we can address it the next AMA.
[107.28 --> 114.04]  That way you don't have to be kind of so in sync with us like the day or the day before we do an AMA.
[114.04 --> 114.08]  Okay.
[114.96 --> 117.44]  So who's ready to answer some questions?
[118.60 --> 119.00]  Yay.
[119.36 --> 120.24]  Let's do this thing.
[120.72 --> 121.72]  Questions are awesome.
[122.38 --> 125.92]  I think I actually saw some Go questions this time, which is awesome.
[126.56 --> 127.92]  It's important, too.
[127.92 --> 137.88]  Yeah, especially if you're getting started in the Go community, like, feel free to throw us Go questions or, you know, what our preferences are, things like that.
[138.66 --> 138.86]  Okay.
[138.94 --> 143.34]  So anybody in particular want to do the question reading?
[144.04 --> 145.72]  We're going to do these in order.
[145.84 --> 148.48]  We're just going to kind of pick them out in fun.
[149.14 --> 152.16]  I think in order is easier for us.
[152.16 --> 154.86]  Other than that, I don't have an opinion.
[156.10 --> 156.36]  Okay.
[156.56 --> 167.72]  Well, then I will read the first question from Freddie V on Twitter, who asks, what are your favorite resources for learning the idiomatic way of doing things in Go?
[167.72 --> 171.12]  I guess this is an interesting question for me.
[172.12 --> 186.54]  I don't know whether I look for new resources nowadays, but I tend to look through the Go standard library a lot because usually that's where the idioms kind of start and then they sort of spread from there.
[187.48 --> 189.30]  Anybody else have different ways?
[189.30 --> 199.70]  I had a slide in my training deck that said, use the source, Luke, and it absolutely agreed with that because the standard library is idiomatic Go for the most part.
[200.40 --> 206.32]  And reading through the standard library is the best way to see how to write really good Go code.
[207.36 --> 216.28]  I used to obsess with trying to find out the idiomatic way to write Go code when I started learning Go.
[216.28 --> 220.18]  And I never really found a specific resource that said this.
[220.24 --> 222.04]  It's the idiomatic way to write Go code.
[222.44 --> 225.66]  And actually, there is a website that attempts to do that.
[225.92 --> 229.58]  It was done by someone at Sourcegraph, and I need to find the link.
[230.00 --> 231.52]  I actually tried to find the link the other day.
[231.68 --> 232.46]  I don't have it.
[232.94 --> 236.02]  If I find it, I'll put it on the show notes.
[237.10 --> 242.84]  But there isn't much really to it.
[242.84 --> 249.64]  And the best way that I learned was by having code reviews done by coworkers.
[250.38 --> 253.12]  But, of course, not everybody is in that position.
[253.40 --> 258.10]  But other than that, it really is just compare your code to what's out there.
[259.20 --> 262.32]  Yeah, there's a channel in our Slack called Go Reviews.
[262.32 --> 268.96]  And if you don't have coworkers who are strong in Go, you can always come into that Go Reviews channel.
[269.12 --> 276.66]  And there are lots of people who are very willing to give you some good advice, and they're friendly about it, too.
[277.38 --> 278.34]  Yeah, that's a good point.
[279.10 --> 280.52]  Yeah, that's actually a really good point, too.
[280.58 --> 282.06]  Just contributing to open source.
[282.28 --> 285.18]  Like, find a really popular project that's maintained.
[286.14 --> 290.82]  And you can kind of learn idioms organically through code review.
[290.82 --> 294.06]  Okay, so next question.
[295.00 --> 296.42]  This one comes from Marwan.
[296.54 --> 301.34]  He says, what do you like to see the core Go team focus their effort on?
[302.48 --> 303.72]  Oh, that's a good question.
[304.48 --> 315.88]  So the core Go team, I think, should be focusing on making Go faster, making the compiler faster, making CGo easier.
[318.24 --> 319.20]  That's about it.
[319.20 --> 327.58]  Well, I am willing to bet that this question meant to ask about technical efforts.
[328.00 --> 342.70]  But I'm going to go out on a limb here and say that the thing that I would like to see the core Go team focus on is onboarding of developers who are new to Go, either because they're new to programming or new to Go.
[342.70 --> 348.62]  And just give them a map for where to start.
[348.62 --> 352.00]  Because the starting point for different people is in different places.
[352.32 --> 354.34]  And I think that we don't have that.
[354.34 --> 362.46]  But do you think that that's somewhere the community should really kind of jump in and kind of handle those things?
[362.84 --> 365.80]  Or, you know, because the Go team is only so big, right?
[366.80 --> 367.86]  Maybe they should be bigger.
[368.30 --> 370.70]  I think that's exactly what the Go team should do.
[370.88 --> 372.92]  They should at least lead the effort.
[372.92 --> 376.14]  And the community definitely should jump in and help.
[376.72 --> 380.30]  But we need to have some sort of authoritative...
[380.30 --> 382.38]  That sounded bad.
[382.80 --> 388.58]  But some sort of, like, confidence source of direction.
[388.92 --> 390.68]  Like, okay, this is a good resource.
[391.06 --> 395.18]  A resource with which people feel confident.
[395.18 --> 396.92]  Okay, this is legit.
[397.06 --> 402.10]  This is validated, endorsed by the Go team or whoever.
[403.32 --> 407.02]  And I think the Go team is a great entity to do that.
[408.18 --> 412.16]  At least to infer that validation.
[413.62 --> 416.94]  Yeah, I mean, having something endorsed by the Go team, I think, would be good.
[417.02 --> 423.60]  But I also think that as people who have been in the Go community, all of us here on the show included,
[423.60 --> 432.14]  I think we're too close to the problem sometimes to really be connected with the areas that newcomers struggle.
[432.34 --> 436.28]  So we really need help there in figuring out what those things are.
[436.70 --> 438.54]  You know, I have the same problem in the Rails world.
[438.86 --> 442.92]  You know, I was like, oh, Rails is easy until the first time I had to sit with somebody to get them set up.
[442.98 --> 446.06]  And I'm like, okay, maybe not so easy to get started.
[446.78 --> 447.42]  Yeah, absolutely.
[447.42 --> 450.16]  It has to be a collaborative effort.
[450.80 --> 454.08]  And people who will do it need to know how to do it.
[454.62 --> 458.76]  It's not just, oh, I'm putting this up here and that's what it is, right?
[458.90 --> 460.92]  It's work.
[461.26 --> 461.74]  It's work.
[461.80 --> 462.40]  It's a lot of work.
[462.46 --> 464.24]  And like you're saying, they are a small team.
[464.84 --> 466.82]  But I think this is important.
[467.52 --> 471.26]  Because if they don't take the lead on this, yes, it can come from the community.
[471.26 --> 477.96]  But then what ends up happening is that we have 10 resources and people are like asking, where should I be looking?
[479.24 --> 479.52]  Right?
[480.42 --> 481.18]  Yeah, that's true.
[481.24 --> 482.64]  There should be a canonical place.
[483.82 --> 484.98]  Okay, next question.
[485.82 --> 494.08]  We have Jamie Stackhouse says, do you have any examples of a code base that uses plain database SQL for a larger size code base,
[494.74 --> 499.78]  particularly looking for patterns to share internally of good practice for scalable dev practices?
[499.78 --> 501.88]  That's a great question.
[502.40 --> 504.52]  I have one that I remember.
[504.74 --> 506.86]  Let me dig really quick while I describe it.
[506.98 --> 509.98]  It's in the Go Micro repositories.
[511.08 --> 515.36]  And I wouldn't go as far as to say it was large.
[516.12 --> 526.86]  But it looks like it was built from someone who's been doing large scale DB SQL work and followed those practices.
[526.86 --> 536.42]  So the repo itself isn't big, but the practices looked to me like those that came from scaling experience in terms of size.
[536.52 --> 538.14]  So let me dig it really, really quick.
[538.26 --> 547.04]  It had most of the queries built as constants at the top of the database package.
[547.04 --> 551.20]  And it was just an interesting pattern.
[551.32 --> 551.66]  I'm digging.
[551.90 --> 552.12]  Sorry.
[553.42 --> 554.00]  Still digging.
[555.00 --> 560.36]  Yeah, and my answer for this would be that I've been pretty disconnected from database SQL.
[560.76 --> 564.44]  In my early Go years, I did a lot of stuff with database SQL.
[565.14 --> 568.24]  And that was before a lot of idioms existed in Go.
[568.24 --> 573.46]  And now I haven't really touched it in a couple of years.
[574.16 --> 576.72]  So I don't feel like I would have a good example.
[577.30 --> 578.44]  How about you, Carlicia?
[579.40 --> 582.68]  I don't know of any code base that's public.
[582.68 --> 595.50]  But I would say take a look at the drivers out there and see how they are accessing database with just the raw using the standard library.
[595.96 --> 598.04]  If I understood the question correctly.
[598.60 --> 604.66]  I think the question is, I don't want to use a third party library and just use the standard library.
[605.46 --> 608.56]  And then what are the ways to organize that?
[608.56 --> 618.02]  So I just pasted the db.go file from the micro slash user dash SRV library into our Slack.
[618.44 --> 625.00]  The thing that stands out here is that it uses a map or a list of all of the queries that can be executed.
[625.74 --> 629.24]  So each query has a name and then a SQL statement.
[629.52 --> 635.46]  And then at the beginning in the init, it parses those queries and prepares them.
[635.46 --> 641.68]  So that it runs the db.prepare so you don't have the two round trips to the server when you make a query.
[642.00 --> 646.16]  So everything is pre-prepared, which saves a lot of time during runtime.
[646.16 --> 656.66]  I don't know if it's any more or less elegant than any other solution I've seen, but I do like the idea of all of the queries being in a single map.
[656.78 --> 659.04]  So they're easy to find in the source code.
[659.14 --> 660.74]  They're not littered through functions.
[660.74 --> 667.16]  And I do very much like the idea of preparing them ahead of time so that they're faster.
[667.28 --> 677.98]  Because in case you aren't aware, when you write a query in Go using db.sql, I think at least my SQL, and I'm not sure about the other drivers,
[678.62 --> 683.24]  they in the background will run a prepare on the query first and then execute it.
[683.28 --> 686.08]  So it's two round trips to the server even when you think you're making one.
[686.68 --> 689.16]  So preparing them in advance saves quite a bit of time.
[689.16 --> 691.88]  Okay, next question.
[692.56 --> 696.46]  It looks like the next two are GopherCon related maybe.
[697.06 --> 705.58]  Okay, so Chris Short asks, as GopherCon organizers, have you ever considered a panel talk for how Go has helped people overcome obstacles in their organizations?
[706.80 --> 708.08]  Or lives for that matter.
[708.82 --> 711.58]  I don't know whether we've ever considered a panel talk.
[712.24 --> 718.82]  But we definitely do look for CFP submissions that demonstrate this.
[718.82 --> 721.76]  I think it's always interesting to hear these types of stories.
[722.64 --> 731.46]  Yeah, I think in general, since we only have a small vote on the CFP submissions, I'm generalizing this probably more than I should.
[731.46 --> 734.92]  But the audience of GopherCon is already sold on Go.
[734.92 --> 746.48]  And a talk like that or a panel like that talking about how Go helps people overcome obstacles is selling to the people that are already sold.
[747.16 --> 754.04]  And that I think is maybe the wrong audience and probably why we haven't seen anything like that yet.
[754.50 --> 755.22]  But that's a guess.
[755.22 --> 757.66]  Yeah, and I mean, I guess that's true.
[757.80 --> 762.88]  Like, as you know, the very first GopherCon, there was a lot of advocacy talks like that.
[763.68 --> 772.86]  But nowadays, people are dipping their toe into the Go world through attending meetups and more regional events.
[772.86 --> 778.18]  So I think that there'd be a bigger impact there probably for a lot of these discussions.
[779.06 --> 779.22]  Yeah.
[780.06 --> 786.50]  If what they want to do is just sort of get an idea, there's a really great talk from GopherCon 2015.
[787.14 --> 790.04]  I don't remember the name of the guy who gave the talk.
[790.16 --> 791.66]  I saw the talk and I remember the talk.
[791.80 --> 797.60]  It was the guy from, oh my gosh, that company that Facebook bought.
[797.60 --> 799.96]  It's not Purge.
[800.22 --> 801.28]  What's the name of the company?
[801.54 --> 801.96]  Help me.
[802.42 --> 802.86]  Periscope?
[803.74 --> 805.00]  No, it's two syllables.
[806.74 --> 807.14]  Oh, great.
[807.30 --> 807.98]  Never mind then.
[808.16 --> 808.92]  I can't remember.
[811.94 --> 812.38]  Snapchat?
[813.42 --> 815.00]  No, it's no.
[816.00 --> 816.38]  WhatsApp?
[817.82 --> 818.00]  No.
[820.78 --> 822.14]  Corey Linu will buy a vowel.
[822.72 --> 823.60]  Is there an A, Vanna?
[824.28 --> 825.56]  It starts with a P.
[826.34 --> 826.74]  Parse.
[827.60 --> 828.28]  Oh, yeah, yeah, yeah.
[828.94 --> 829.96]  Is it Parse?
[830.72 --> 833.46]  Parse is the only one that they bought that starts with a P.
[834.22 --> 834.56]  Okay.
[834.76 --> 835.42]  Then that's it.
[835.84 --> 842.70]  Yeah, there was somebody in 2015 that did a talk on rebuilding all of Parse and Go.
[843.50 --> 844.36]  Yes, exactly.
[844.44 --> 844.84]  That's it.
[845.56 --> 846.14]  Thank you.
[847.06 --> 847.54]  Okay.
[847.88 --> 848.84]  Next question.
[849.46 --> 855.26]  James Lovato asks, if I took my Kindle to GopherCon and pulled up Go in action, would you sign the display?
[855.82 --> 856.12]  Yes.
[856.12 --> 856.56]  Yes.
[857.46 --> 857.76]  Yes.
[858.56 --> 860.86]  If you print a copy, we will sign that, too.
[861.82 --> 862.22]  Yes.
[863.24 --> 863.58]  Okay.
[864.04 --> 866.56]  Corey Linu asks, what was the most unexpected?
[866.94 --> 867.06]  Wait.
[867.22 --> 869.08]  We skipped Scott Mansfield's question.
[869.36 --> 872.58]  How many total hours does it take to organize GopherCon Denver?
[873.36 --> 873.76]  Wow.
[874.32 --> 875.26]  Total hours.
[875.66 --> 876.24]  Oh, ouch.
[876.32 --> 877.56]  On a man hour basis?
[877.56 --> 878.50]  I don't even know.
[878.88 --> 879.06]  Yeah.
[879.16 --> 884.62]  So if they're man hours, probably 6,000, but at woman hours, probably 30 or 40.
[884.62 --> 902.48]  So the very first year, we spent a year of the two of us working several hours a night every night for almost a year.
[902.48 --> 903.36]  Yeah.
[903.36 --> 903.40]  Yeah.
[905.00 --> 916.84]  Nowadays, I mean, we have waves of time where we don't do things a couple months right after and between, like, when we announce in January.
[916.84 --> 921.50]  I mean, I feel like we're not working on it daily anymore.
[921.50 --> 929.84]  If we are, it's less than an hour, and then, you know, some weeks we get hectic, like during CFPs where, you know, we're working several hours a day reviewing them.
[930.36 --> 945.62]  But in order for our sanity and the sustainability of the conference, we have hired vendors to do a lot of the things that we didn't have time for or are not so good at, like selling sponsorships and things like that.
[946.14 --> 948.88]  So I guess it'd be really hard to estimate now.
[948.88 --> 958.36]  If I had to guess, I'd say over the course of the entire year, probably 500 hours for each of us.
[959.26 --> 961.64]  And that's, you know, just pull that out of the air.
[962.44 --> 964.50]  This year, 500 hours for each of us.
[964.60 --> 969.50]  The first couple of years, it was more like 1,000 hours for each of us.
[969.54 --> 971.88]  It was definitely a halftime job the first year.
[971.88 --> 986.26]  I'd say now it's more like it probably averages 10 or 15 hours a week, where some weeks are closer to five hours and some weeks are closer to 30 or 40 hours, just depending on the time of year and what's going on.
[987.54 --> 994.34]  Corey Linu asks, what was the most unexpected good thing you learned slash encountered slash discovered when you joined Microsoft?
[994.34 --> 996.60]  Oh, this is a good one.
[997.98 --> 999.40]  Unexpected good thing.
[1001.06 --> 1002.36]  Microsoft isn't evil.
[1003.14 --> 1006.28]  Of course, I learned that before I joined, which is why I joined.
[1006.28 --> 1017.32]  But I think going into Microsoft, going on campus and seeing all of the people who are just extremely passionate about technology and helping others.
[1017.50 --> 1022.30]  And, you know, it's it's not just a marketing pitch that Microsoft has changed.
[1022.30 --> 1024.90]  It's real and it's top down.
[1025.06 --> 1025.84]  It's kind of awesome.
[1026.38 --> 1029.28]  And there's just so many amazing smart people that work there.
[1029.82 --> 1032.10]  And I look forward to doing it every day.
[1032.10 --> 1036.32]  Ashley is the best thing that's ever happened to Microsoft.
[1036.48 --> 1036.96]  How's that?
[1038.30 --> 1039.02]  There we go.
[1039.64 --> 1041.94]  She just jumped in on Slack and reminded us of that.
[1042.56 --> 1044.08]  And literally, he's not kidding.
[1044.28 --> 1047.26]  She says, me, I'm the best thing that happened.
[1048.14 --> 1049.64]  In capital, all capital.
[1049.84 --> 1050.76]  Yeah, in all caps.
[1051.10 --> 1051.92]  I love Ashley.
[1052.88 --> 1062.08]  I guess for me, I was surprised to find out that there were divisions of Microsoft that have actually been doing open source.
[1062.10 --> 1063.84]  For a very long time.
[1064.36 --> 1067.74]  As parts of like the Apache Foundation and things like that.
[1068.34 --> 1074.84]  And also how just how quickly the CDA team kind of scaled up.
[1075.42 --> 1079.84]  So for most of you that are kind of aware of like Brian and I joining and Ashley McNamara.
[1080.48 --> 1081.82]  And Jess Rizal.
[1082.40 --> 1083.68]  And Bridget.
[1083.96 --> 1085.20]  And some of these people that work.
[1085.34 --> 1088.20]  We work directly with and like the Go Linux containers groups.
[1088.20 --> 1092.72]  And we are actually kind of the minority.
[1092.88 --> 1095.72]  The team itself is like close to 70 people now, Brian.
[1096.76 --> 1098.12]  I think that's about right.
[1098.18 --> 1098.32]  Yeah.
[1098.82 --> 1099.78]  So, yeah.
[1099.78 --> 1100.80]  There's .NET people.
[1101.00 --> 1102.02]  There's Python people.
[1102.28 --> 1105.32]  There's IoT and AI and ML people.
[1105.62 --> 1109.08]  Like the actual team is actually pretty large.
[1109.08 --> 1112.38]  So, that was really, really exciting to learn too.
[1113.14 --> 1117.84]  Which makes for fun little projects where Brian and I come up with some kind of crazy idea.
[1118.64 --> 1120.56]  Or anybody on the team for that matter.
[1120.76 --> 1122.86]  And you're like, I really like a cool front end.
[1123.08 --> 1125.68]  Or to make this do some AI stuff or whatever.
[1126.04 --> 1128.16]  And you can just reach out to other people.
[1128.28 --> 1129.90]  And they're like, yeah, I'll help with those bits.
[1130.98 --> 1131.14]  Yeah.
[1131.24 --> 1132.08]  It's kind of awesome.
[1132.08 --> 1132.72]  I don't remember.
[1133.32 --> 1146.84]  It was either Ashley or Jess who said in a blog post or Twitter that the best part of it was being able to just reach out and hit an expert on any topic.
[1147.46 --> 1148.40]  And that was so cool.
[1148.70 --> 1149.32]  It is.
[1149.40 --> 1149.92]  It's amazing.
[1150.06 --> 1150.78]  You know, you need AI.
[1150.98 --> 1151.80]  We have that expert.
[1152.40 --> 1152.90]  You need this.
[1152.98 --> 1154.62]  We have the person who wrote the book on that.
[1155.04 --> 1155.60]  It's all here.
[1155.60 --> 1161.26]  Well, the best thing I learned when I joined Microsoft was nothing.
[1164.70 --> 1165.54]  Spoiler alert.
[1165.76 --> 1168.54]  Carlicia just quit fastly live on air now.
[1171.20 --> 1172.96]  I did not join Microsoft.
[1175.74 --> 1177.16]  But thank you for asking.
[1177.74 --> 1181.30]  If you did, we'd have to hit them up for official sponsorship at that point.
[1181.50 --> 1183.08]  You're here in spirit, Carlicia.
[1184.08 --> 1184.44]  Yeah.
[1185.60 --> 1185.80]  Okay.
[1185.86 --> 1191.12]  So also from Corey, Go has been out for a while now, but I'm sure you still get the question, why Go?
[1191.58 --> 1197.54]  After using it as long as you have, what is your answer now and what was it four or five years ago?
[1198.18 --> 1199.80]  That's a great question.
[1200.84 --> 1203.78]  Yeah, that is a very, very good question.
[1203.78 --> 1211.82]  I guess for me now, it feels like a cloud-first language.
[1211.82 --> 1217.36]  A lot of the ecosystem in the cloud and distributed systems world.
[1217.80 --> 1218.30]  What does that mean?
[1219.62 --> 1220.68]  What the hell does that mean?
[1220.72 --> 1221.34]  That's a cop-out.
[1221.62 --> 1222.80]  What is a cloud-first language?
[1223.04 --> 1223.76]  It's really...
[1224.48 --> 1226.32]  Answer it without the marketing buzz.
[1226.66 --> 1226.98]  Come on.
[1226.98 --> 1227.88]  Yeah.
[1227.88 --> 1227.90]  Yeah.
[1227.90 --> 1236.96]  So it's because almost every cloud provider has or is working on a really good SDK for it.
[1236.96 --> 1242.08]  A lot of the tools like Docker and Kubernetes that everybody's using.
[1242.08 --> 1254.36]  Leverage Go, a lot of the distributed systems tools that we're all using now for observability and distributed tracing, all that are all written in Go and have really solid libraries for it.
[1254.36 --> 1259.38]  It makes it really easy to build distributed systems in cloud applications with.
[1260.02 --> 1268.34]  That's not to say that that overshadows all the reasons I originally loved Go, but it is a good reason to do it, right?
[1268.54 --> 1271.76]  There's projects that you want to build that maybe integrate with Kubernetes.
[1271.76 --> 1279.42]  If you want help from the open source community, that's the language people who work on Docker and Kubernetes speak.
[1280.32 --> 1284.30]  Four or five years ago, I mean, it was concurrency.
[1285.92 --> 1289.40]  The language was easy to reason about and fit in your head.
[1290.46 --> 1292.80]  I guess this would be the kind of core points.
[1292.94 --> 1298.14]  You know, there were parts of the language that I loved, but it kind of fell into those bits.
[1298.14 --> 1305.36]  I still firmly believe that, but I think the cloud aspect is another reason why Go should be a language of choice now.
[1306.28 --> 1307.58]  I will go next.
[1308.42 --> 1311.10]  So I would start with four or five years ago.
[1311.40 --> 1316.62]  I guess for me it was, I don't know, not quite five years, maybe four, three or four years.
[1316.80 --> 1317.66]  I don't remember.
[1318.06 --> 1318.48]  Let me see.
[1318.80 --> 1321.46]  Three years ago when I started looking into Go.
[1321.46 --> 1328.50]  It was the promise of speed that got me mesmerized.
[1329.54 --> 1339.14]  Speeds as far as running apps, you know, because easier to use concurrency, but also speed in running tests.
[1340.16 --> 1345.92]  And actually going back to that talk by the guy who worked at Parse, that was very appealing.
[1345.92 --> 1355.94]  He was saying, well, the Parse app that they had before took 30 minutes to run tests and then they converted to Go and it took three minutes.
[1356.54 --> 1358.00]  And I was mesmerized.
[1358.20 --> 1359.68]  So that was what hooked me.
[1361.00 --> 1366.38]  And so today what I think is that, yeah, maybe that's like old news for me.
[1366.50 --> 1368.00]  It's like, okay, yeah, it's fast, whatever.
[1368.00 --> 1378.50]  But for me, what really gets me every day that I work with Go is how easy to read, how productive I can be.
[1378.70 --> 1384.86]  Like I can hold a lot more code in my head because I don't have to figure out what I'm reading.
[1385.02 --> 1385.98]  It's just so clear.
[1386.12 --> 1388.20]  It's like reading a written language.
[1388.38 --> 1390.76]  It's so easy to understand.
[1390.76 --> 1398.58]  And so my thinking is if you have a small project, use whatever language you want, who cares?
[1398.72 --> 1410.90]  But as you start having a bigger application, really think about how much more productive the developers will be if the language is easier to read, right?
[1410.96 --> 1413.62]  If you're trying to make a choice there.
[1414.30 --> 1418.72]  So that's my top feature for Go at the moment.
[1418.72 --> 1420.98]  I couldn't have said that better.
[1421.10 --> 1429.34]  That's exactly what I would have said or was planning on saying is that four or five years ago, I would have said the same thing Eric would have said four or five years ago.
[1429.66 --> 1432.56]  Concurrency, you know, all of the speed and whatever.
[1432.56 --> 1447.66]  But now 100% my favorite feature of Go is how easy it is to read and how easy it is for a large team to know what's going on in a big Go repository compared to other languages.
[1447.66 --> 1449.74]  It's drastically different.
[1450.28 --> 1460.02]  I think also another thing we're missing today that we could say a little bit when we first started four or five years ago is the community.
[1460.14 --> 1466.86]  The community is so much bigger, but also still kind of tight knit in a lot of ways.
[1468.14 --> 1474.06]  And I think the popularity and success of a language also lies heavily on the community.
[1475.28 --> 1475.64]  Agree.
[1475.64 --> 1475.68]  Absolutely.
[1476.22 --> 1476.62]  Absolutely.
[1478.20 --> 1480.72]  Also, Corey, I guess he sent us a list.
[1481.52 --> 1482.10]  He did.
[1482.16 --> 1483.28]  He sent us like six in a row.
[1483.86 --> 1489.10]  What is the biggest thing that we, the community, can do slash continue to do to help Go adoption?
[1490.22 --> 1490.58]  Hmm.
[1490.90 --> 1492.16]  I have an answer for that.
[1494.12 --> 1494.56]  Okay.
[1494.66 --> 1495.14]  I do too.
[1496.22 --> 1496.96]  In my opinion.
[1497.68 --> 1499.00]  Do you want to go first, Carlos?
[1499.00 --> 1499.50]  Go ahead.
[1499.50 --> 1506.76]  In my opinion is, so I'm assuming he's talking about people who are already in the community.
[1508.02 --> 1514.34]  Step up and take leadership of whatever efforts you can relate with.
[1514.34 --> 1516.04]  It might be women who go.
[1516.16 --> 1518.34]  It might be Go Bridge.
[1518.46 --> 1521.36]  Or it might be like the Go Working Group.
[1521.56 --> 1521.98]  Anything.
[1522.76 --> 1526.52]  Because this stuff has been going on.
[1526.52 --> 1529.10]  But people get burned out.
[1529.10 --> 1533.62]  Everybody who's doing this stuff, they're doing it on a volunteer basis.
[1533.62 --> 1538.20]  And, you know, take the baton, basically.
[1538.62 --> 1546.44]  I can't hardly think of anything that would have more impact in the adoption of Go than that.
[1546.44 --> 1551.68]  Because that helps bring in people, bring in new people, bring people from diverse backgrounds.
[1552.04 --> 1552.68]  Or not.
[1552.74 --> 1553.28]  It doesn't matter.
[1553.94 --> 1558.62]  But, you know, teaching workshops, doing things like that.
[1558.66 --> 1561.16]  Just take the leadership of something.
[1561.64 --> 1565.34]  So people who are doing that, they can breathe and take a break.
[1566.00 --> 1572.06]  And also, you know, the more people who are out there taking leadership of these things, the more these initiatives can grow.
[1572.28 --> 1573.94]  And these things are usually free.
[1573.94 --> 1582.70]  It's very appealing for people who are joining to have that portal to go through to learn Go and, you know, adopt Go, basically.
[1583.72 --> 1584.68]  That's a good answer.
[1585.46 --> 1587.16]  Mine is similar.
[1587.70 --> 1595.82]  I would say that one of the things that I still love more than anything else about the Go community is the Go community.
[1595.82 --> 1604.08]  And that as far as communities go, it hasn't changed a lot over the last seven, eight years.
[1604.30 --> 1609.56]  You know, it started off being a very welcoming and friendly and helpful community.
[1609.84 --> 1613.36]  And it still is, even though it's grown exponentially.
[1613.36 --> 1625.24]  So my suggestion or advice would be that we make a conscious effort to continue that welcome openness.
[1625.24 --> 1633.44]  I remember in the Ruby world, they had the minus one thing, which meant Matt's is nice, so we are nice.
[1633.66 --> 1634.90]  And that didn't really last long.
[1635.46 --> 1639.14]  You know, Ruby hit big and hard in 2004, 2005.
[1639.14 --> 1643.02]  And Matt's was still nice, but a lot of other people weren't.
[1643.02 --> 1646.14]  And the Ruby community was less than friendly.
[1646.78 --> 1659.14]  And one of the things that Eric and I talked about very early on was how much we wanted to take action to make the Go community continue to be welcoming and friendly.
[1659.14 --> 1662.48]  And that was part of our motivation behind Go4Con.
[1662.94 --> 1670.38]  I guess from my standpoint, it mirrors a lot of what both Brian and Carlicia said, the community aspect and always being welcoming.
[1671.18 --> 1679.38]  I think that we need more resources for beginners and onboarding and kind of bridging that gap.
[1679.38 --> 1692.10]  And then I think we also need more people to speak at local meetups and things because now we've kind of hit the catalyst point of Go's adoption growth.
[1692.42 --> 1699.76]  Now we're starting to have more people come on and people who aren't necessarily traveling to conferences and things like that.
[1700.10 --> 1705.64]  So we need more people speaking on the local fronts to get more people introduced to the language.
[1705.64 --> 1709.90]  Yeah, and really, that's our farm team for Go4Con.
[1710.10 --> 1715.90]  So go practice at the meetups and get polished well so you can come and present on the big stage at Go4Con.
[1716.56 --> 1716.92]  Okay.
[1717.58 --> 1719.00]  All right, next question.
[1720.58 --> 1727.40]  Corey again, my goodness, Corey, asks, if you could add one thing to the standard library, what would it be?
[1728.02 --> 1729.88]  I don't know whether I would add anything.
[1730.16 --> 1731.54]  I think I would remove stuff.
[1732.02 --> 1732.76]  Mm-hmm.
[1732.76 --> 1735.82]  Same.
[1735.98 --> 1737.28]  My answer would be a delete button.
[1737.38 --> 1738.10]  There is a question.
[1738.28 --> 1739.84]  That question is coming up, though.
[1740.72 --> 1741.30]  Oh, yeah.
[1742.10 --> 1742.54]  Okay.
[1742.66 --> 1747.74]  So Corey asks, what is the hardest thing you've ever had to write in Go?
[1749.28 --> 1750.64]  That is a good question.
[1750.74 --> 1753.32]  The hardest thing you've ever had to write.
[1753.32 --> 1760.84]  For me, I don't even remember the project, but it was really extensive reflection.
[1760.84 --> 1770.66]  There was a whole lot of reflection, and it had to do with moving a bunch of data around between different structures and different systems over a queue.
[1770.66 --> 1783.24]  And I just remember piles and piles and piles and thinking that this would be so much easier in a language that was less strict about types.
[1783.24 --> 1786.04]  I guess for me, similar.
[1786.04 --> 1787.04]  Sure.
[1787.04 --> 1789.94]  Probably this was like pre-GRPC.
[1790.32 --> 1796.72]  Brian and I had this grand vision of like a framework for building distributed systems.
[1796.72 --> 1800.82]  And I wrote an RPC layer.
[1801.62 --> 1808.70]  And I forget what bits that I had to implement, but I remember there being a lot of issues with Big Indian, Little Indian.
[1809.12 --> 1817.24]  And then probably the hardest part was like all the reflection crap from deserializing those RPC requests.
[1818.36 --> 1819.50]  Long live Skynet.
[1819.50 --> 1824.76]  Steve mentioned SkyDNS and James says SkyDNS is dead.
[1826.30 --> 1827.84]  I mean, not quite yet.
[1827.98 --> 1829.72]  It is used inside Kube DNS.
[1830.88 --> 1836.56]  They haven't converted Kube DNS to use CoreDNS yet, but it probably will be a thing.
[1837.62 --> 1838.78]  How about you, Carlicia?
[1838.84 --> 1840.76]  What's the hardest thing you've ever written in Go?
[1841.86 --> 1843.34]  Yeah, I was trying to remember.
[1843.34 --> 1857.14]  I don't remember enough to be articulate, but I will say that the hardest aspect of Go for me is concurrency.
[1857.90 --> 1860.98]  So I never have to read code that has concurrency.
[1861.30 --> 1864.24]  It's just because I don't do it all the time.
[1864.24 --> 1869.96]  And I think people think, you know, concurrency is such a great feature of Go.
[1870.32 --> 1872.88]  And if you're a Go developer, you use it all the time.
[1872.88 --> 1873.74]  And that's not true.
[1874.94 --> 1876.62]  So that's my answer.
[1877.54 --> 1878.46]  That's a good answer.
[1878.70 --> 1881.06]  Absolutely don't use concurrency all the time.
[1882.78 --> 1883.26]  Yeah.
[1883.80 --> 1888.90]  It's one of those things that you sprinkle on sparingly, like salt in a good kitchen.
[1888.90 --> 1890.20]  And I definitely don't use it all the time.
[1890.20 --> 1897.20]  So when I have to read it, I do have a little bit of trouble and I have to like really pay attention to understand what it is doing.
[1898.14 --> 1900.92]  But, you know, there are concurrency patterns out there.
[1901.20 --> 1910.54]  And actually, Bill Kennedy has a really good blog post explaining the different types, the different types of problems, the different types of use cases.
[1911.36 --> 1916.26]  And accompanying patterns of concurrency that you can use for each type is really good.
[1916.98 --> 1919.60]  So that's my go-to reference to understand it.
[1920.20 --> 1921.04]  Nice.
[1922.16 --> 1922.60]  Okay.
[1923.46 --> 1923.76]  All right.
[1923.82 --> 1926.08]  Scott Manfield asks the next question.
[1926.18 --> 1930.06]  Do you think the Go 1.0 compatibility promise has already been broken?
[1931.56 --> 1932.64]  I'll answer yes.
[1934.10 --> 1942.04]  They intentionally broke it at least once that I can think of to fix a big error in something or other.
[1942.04 --> 1947.22]  And so it was kind of a, and that was a couple, several releases ago.
[1947.28 --> 1956.16]  I just don't remember the bug, but it broke backwards compatibility and they announced it in monotonic time.
[1956.24 --> 1957.26]  Yeah, that's definitely one.
[1957.26 --> 1959.60]  But there was another.
[1960.26 --> 1961.40]  So at least twice, yes.
[1961.50 --> 1967.26]  But I think the spirit of the Go 1.0 compatibility promise they've adhered to religiously.
[1968.10 --> 1970.44]  And I approve of that and appreciate it a lot.
[1970.86 --> 1971.82]  Yeah, I'd agree.
[1971.82 --> 1977.42]  I can't think of some concrete examples, but I know there's been, you know, one or two instances.
[1977.74 --> 1989.82]  But, you know, considering the Go 1.0 came out five or six years ago, they've been pretty strict on the compatibility promise.
[1989.82 --> 1997.68]  And even the ones that did break, I can't remember any being like super, super severe as far as having to refactor your code to work.
[1998.42 --> 1998.94]  All right.
[1998.98 --> 2002.34]  Pascal Dennerly asks, what keeps you excited about Go?
[2003.90 --> 2005.84]  I think, you know, you got to keep it fresh.
[2005.92 --> 2007.18]  You got to go out on date nights.
[2007.58 --> 2011.04]  You got to bring flowers and surprise people every once in a while.
[2011.18 --> 2016.24]  If you don't, if you don't, you know, make that effort, then things get stale after a while.
[2016.88 --> 2017.74]  Go is the same way.
[2017.74 --> 2021.12]  For me, it's things like GopherJS, WebAssembly.
[2021.48 --> 2024.84]  You got to kind of branch out a little bit and try some new things.
[2025.80 --> 2027.56]  Richard Musial, is that right?
[2027.92 --> 2035.28]  The guy who made GopherJS or started GopherJS is very deeply busy right now working in the WebAssembly branch.
[2035.58 --> 2041.10]  And it looks like it's darn close to being ready to go.
[2041.26 --> 2042.98]  You know, that really excites me about Go.
[2042.98 --> 2047.22]  The idea that we can build insanely fast client-side stuff.
[2047.74 --> 2050.26]  In Go, I'm all over that.
[2051.20 --> 2060.42]  So even though I was a little snarky in the beginning, I did mean the idea of keeping things fresh and interesting just by trying new stuff, learning new things in Go.
[2060.80 --> 2061.58]  How about you, Carlycia?
[2061.58 --> 2063.90]  Yeah, that's a great answer, Brian.
[2064.30 --> 2065.10]  It's insightful.
[2067.04 --> 2081.16]  For me, it's knowing that Go is growing and there are a ton more people joining the community, which means there's more people to relate to and more people that will understand when we say, Go is awesome.
[2081.16 --> 2084.96]  There's more people out there now saying, yes, it is.
[2087.22 --> 2091.64]  It really excites me to see that more people are adopting Go, and that is true.
[2092.62 --> 2101.08]  Yeah, watching the number of conferences pop up and just the number of people who are coming on to Go year after year is just insane.
[2101.08 --> 2107.26]  Five years ago, me knew that Go was really awesome and that it would be a thing.
[2107.50 --> 2111.62]  I don't think five years ago, me thought that it would be this big this quick.
[2112.72 --> 2112.82]  Yeah.
[2112.82 --> 2115.86]  So I think it's exciting to keep watching it grow.
[2116.44 --> 2126.54]  And then similar to Brian's point, too, I love seeing all the things that are happening on the fringe of what the past couple of years we've been using Go for.
[2126.70 --> 2133.88]  Everybody from microservices and CLI tools, there's no surprise when somebody's like, oh, I wrote that in Go.
[2133.88 --> 2145.82]  But I get really excited when I see stuff like the WebAssembly stuff or people messing with embedded systems with Go or, you know, like GoCV doing computer vision stuff with Go.
[2146.26 --> 2158.46]  Even though that's still CGO, but watching people write like Nintendo emulators and all that stuff, I just I geek out on seeing people do like interesting things with Go that is kind of outside the norm.
[2159.20 --> 2160.48]  Yeah, and learn a lot from that, too.
[2161.76 --> 2162.44]  I agree.
[2162.44 --> 2162.58]  Yeah.
[2163.88 --> 2164.34]  All right.
[2164.36 --> 2166.94]  This is a troll question, but we're going to answer it anyway.
[2168.12 --> 2173.54]  Do any of you know how Russ Cox's mystic quest to understand generics is going?
[2173.90 --> 2177.16]  Let me just say, I love the way this question was asked.
[2177.50 --> 2179.66]  I appreciate the nuance.
[2179.94 --> 2180.70]  It was great.
[2181.20 --> 2182.26]  Good job doing that.
[2183.22 --> 2184.74]  And I think the answer to that is no.
[2184.74 --> 2185.08]  No idea.
[2185.26 --> 2185.90]  Nobody knows.
[2185.90 --> 2186.58]  Yeah.
[2186.58 --> 2187.08]  Yeah.
[2187.08 --> 2204.20]  I mean, all I can remember basically was that we've moved from the was a 2014 maybe where it was like, go doesn't need generics to, you know, generics could and should be a thing.
[2204.20 --> 2214.32]  But they want to come up with concrete use cases to make sure that they solve those properly and don't introduce any more complexity into the language they need to.
[2214.32 --> 2218.60]  But outside of that, and I could be remembering incorrectly, too.
[2218.70 --> 2220.60]  That's that's all I remember.
[2220.60 --> 2221.04]  Yes.
[2221.88 --> 2229.68]  When we last left our hero, he was standing in front of a scroll, reading it diligently, trying to understand what his future quest would be.
[2229.68 --> 2232.98]  All right.
[2233.02 --> 2233.64]  Next question.
[2234.86 --> 2237.40]  Marco, I don't even know how to say your last name.
[2237.46 --> 2238.02]  I apologize.
[2240.20 --> 2240.64]  Mudrinich.
[2240.92 --> 2243.42]  I don't know what the C with the accent over it does.
[2243.70 --> 2244.44]  Mudrinich, maybe.
[2245.04 --> 2247.96]  As far as I know, you're working on organizing GopherCon events.
[2248.06 --> 2254.54]  As somebody who would love to become a speaker one day, do you have some recommendations on where to get started and how?
[2254.64 --> 2258.14]  Any tips or tricks for newbies mostly interested in Go events?
[2258.28 --> 2258.56]  Thanks.
[2258.56 --> 2260.30]  Yes, we just hit this a moment ago.
[2260.42 --> 2261.54]  Go to your local meetups.
[2261.66 --> 2269.04]  Talk in front of 10 or 15 or 30 people and get help from the local meetup organizers in preparing your talks.
[2269.04 --> 2274.62]  And it will definitely help you to prepare for a bigger venue.
[2275.92 --> 2278.56]  Also tweet about the fact that you're working on content.
[2278.98 --> 2288.18]  There's a lot of people in the Go community who are willing to review slides or talk proposals and things of that nature and help you molt them.
[2288.56 --> 2297.90]  The other thing I would say is pick a topic you're really excited about versus kind of just picking something you think people might be interested in hearing.
[2298.74 --> 2304.62]  It'll be easier for you, especially getting started because kind of that excitement and passion will come out.
[2304.62 --> 2305.44]  Yes.
[2305.44 --> 2305.50]  Yes.
[2305.70 --> 2310.72]  And the 1400th time you rehearse the talk, you can still be excited about it.
[2311.44 --> 2312.12]  Yeah, absolutely.
[2312.30 --> 2314.84]  I second everything that was said.
[2314.84 --> 2318.22]  And also, don't we have a speaker channel on Go for Slack?
[2318.32 --> 2319.34]  I'm not finding it.
[2319.58 --> 2320.82]  I think we do.
[2321.60 --> 2322.20]  Oh, yes.
[2322.34 --> 2323.20]  It's called Speaking.
[2324.20 --> 2324.62]  So there.
[2324.76 --> 2325.04]  Speaking.
[2325.24 --> 2325.40]  Good.
[2325.40 --> 2339.46]  And I do know on Twitter, not too long ago, there was a thread of people who were offering mentorship for people who wanted to prepare CFP responses.
[2340.68 --> 2341.50]  Oh, yes.
[2341.54 --> 2344.18]  There was a workshop in various cities.
[2345.02 --> 2347.80]  There is a good resource to keep track of.
[2348.12 --> 2350.78]  And it was Russ who tweeted that.
[2350.88 --> 2351.68]  Wasn't it, Russ?
[2352.42 --> 2353.40]  You're absolutely right.
[2353.50 --> 2354.14]  It was Russ.
[2354.14 --> 2354.80]  It was the.
[2356.60 --> 2359.58]  Oh, well, I don't remember the name of it, but yes, you're right.
[2359.76 --> 2360.36]  It was Russ.
[2360.38 --> 2361.94]  I'll get a link and put it in the show notes.
[2362.58 --> 2362.74]  Cool.
[2362.98 --> 2371.06]  So this is apparently an organization that offers these workshops to teach people how to be how to become speakers.
[2372.02 --> 2374.32]  And so it's recurring.
[2375.00 --> 2379.78]  They'll put out put out dates and you just have to keep track and find out if there is anything going on.
[2379.78 --> 2380.52]  They are you.
[2381.08 --> 2381.20]  Yeah.
[2381.20 --> 2388.74]  And then if you want just the generic public speaking advice, you know, everybody's more nervous than you think they are.
[2388.92 --> 2390.64]  So being nervous is normal.
[2391.52 --> 2396.46]  And if you really want practice, you can always do local Toastmasters.
[2396.46 --> 2408.88]  And I have not done this yet, but I've heard people say that improv classes are a lot of fun and get you kind of used to being up in front of people and and kind of improv on the spot and not getting nervous about it.
[2409.94 --> 2410.24]  Yes.
[2410.92 --> 2412.06]  That sounds like a good idea.
[2412.06 --> 2415.14]  I want to do it just for fun, because improv sounds like fun.
[2417.70 --> 2418.18]  All right.
[2418.18 --> 2424.28]  This next question, it was also a joke, but it came with the kindergarten cop picture.
[2424.28 --> 2431.46]  So if you remember the movie kindergarten cop, it was Penelope Ann Miller and Arnold Schwarzenegger.
[2431.66 --> 2434.46]  And he's a cop who goes undercover as a kindergarten teacher.
[2435.30 --> 2440.00]  And he's trying to discover who the bad guy is.
[2440.06 --> 2442.54]  And he's teaching in front of the kindergartners.
[2442.54 --> 2446.44]  And he says, all right, now we're going to play a game called Who is Your Daddy and What Does He Do?
[2446.44 --> 2450.54]  And it was a cute scene in the movie.
[2451.30 --> 2452.88]  So I will start.
[2453.20 --> 2454.96]  My daddy is Robert.
[2455.86 --> 2463.52]  And he owned and ran restaurants for most of my youth and then moved out of restaurants and into accounting.
[2464.22 --> 2471.52]  And now he is retired and lives just a few miles down the road and brings his hairy dog down the street to my house frequently.
[2471.52 --> 2472.72]  So I have to vacuum a lot.
[2474.90 --> 2475.96]  Which is a good thing.
[2475.96 --> 2477.50]  Yeah, that sounded very complaining.
[2477.64 --> 2478.04]  It's not.
[2479.56 --> 2484.62]  My dad did a bunch of odd jobs.
[2486.94 --> 2497.06]  The job that he had the longest that I can remember was as a bus driver doing interstate travel.
[2498.32 --> 2500.40]  But his dream was to be a fisherman.
[2500.40 --> 2513.06]  And he used to go and hunt and bring all sorts of weird animals to the house and just not make us eat, but make it available for us to eat.
[2513.14 --> 2515.80]  So I've eaten some pretty strange things.
[2518.12 --> 2518.60]  Nice.
[2519.22 --> 2520.04]  That's kind of cool.
[2520.14 --> 2520.40]  Yeah.
[2520.40 --> 2520.88]  Okay.
[2520.88 --> 2521.52]  Okay.
[2521.52 --> 2526.30]  So mine is, I guess you could say, semi-retired now.
[2526.42 --> 2532.32]  He mostly does odd things to, you know, make a living now.
[2532.32 --> 2540.56]  But growing up, he was a DJ, which is part of the reason I am not freaked out by having a microphone in front of my face.
[2541.06 --> 2544.06]  Or I could be potentially more freaked out.
[2544.06 --> 2548.82]  And also why I have a love for, like, all kinds of music.
[2549.38 --> 2555.72]  And I'm very, very good at being the person where you're like, that one song by those two people that had these three words.
[2555.78 --> 2556.34]  Who is that?
[2556.38 --> 2557.72]  And I can tell you the name of the artist.
[2558.10 --> 2558.26]  Yeah.
[2558.40 --> 2558.98]  Billy Vanilli.
[2558.98 --> 2563.36]  Oh, so my dad is also retired now.
[2563.54 --> 2568.50]  And I always forget that we owned, like, this is back in Brazil, right?
[2568.56 --> 2570.02]  Because that's where I grew up.
[2570.66 --> 2579.24]  He owns a bar slash restaurants slash ice cream parlor for years.
[2579.60 --> 2582.32]  So that was pretty fun, too, for me.
[2582.32 --> 2583.32]  Nice.
[2585.36 --> 2585.48]  Yeah.
[2585.54 --> 2589.14]  My dad had an ice cream parlor, too, called Happy Joe's.
[2589.84 --> 2592.76]  And it was an ice cream parlor and pizza.
[2593.60 --> 2595.64]  And they had the first video games.
[2595.90 --> 2598.18]  We had Pac-Man before anybody else.
[2598.18 --> 2599.46]  And he had the key to the thing.
[2599.56 --> 2601.00]  So I played a lot of Pac-Man.
[2602.42 --> 2604.12]  Oh, you know what I played a lot?
[2604.54 --> 2610.86]  My dad had a foosball table at this bar that we had.
[2610.86 --> 2613.74]  And I used to play all the time.
[2613.84 --> 2618.68]  That's why when I go to Goldberg Con, you find me by the foosball table.
[2618.82 --> 2621.80]  Because I don't go to a lot of places that has foosball table.
[2622.26 --> 2628.30]  So when we have that party at the punch bowl, I'm like, yeah, bring it.
[2628.40 --> 2629.94]  I'm going to kick your butt.
[2630.26 --> 2630.76]  Oh, yeah.
[2632.28 --> 2634.20]  And last year, there was this woman.
[2634.50 --> 2636.92]  And I didn't connect with her, unfortunately.
[2637.58 --> 2639.42]  She was kicking everybody's butt.
[2639.42 --> 2640.66]  I was impressed.
[2641.68 --> 2643.26]  She was just...
[2643.26 --> 2645.70]  Nobody would win against her.
[2645.90 --> 2646.52]  That's pretty cool.
[2647.52 --> 2648.36]  Not a chance.
[2648.88 --> 2649.72]  Nobody had a chance.
[2650.58 --> 2650.82]  Okay.
[2650.98 --> 2652.84]  Next question is...
[2652.84 --> 2653.80]  Matt Reier asks,
[2654.04 --> 2657.94]  If you could remove one thing from the Go language, what would it be and why?
[2658.44 --> 2659.06]  Oh, yeah.
[2660.84 --> 2662.16]  I got this.
[2662.16 --> 2669.68]  There's probably some stuff I feel like could be removed out of the standard library because it begs the argument, is it part of the language?
[2670.02 --> 2673.14]  And should it adhere to the compatibility guarantees?
[2673.14 --> 2679.22]  We could improve on some of them by being able to break that compatibility guarantee.
[2679.22 --> 2683.78]  But as far as language itself, I'd say new.
[2683.78 --> 2685.18]  I just...
[2685.18 --> 2686.54]  I don't feel like...
[2686.54 --> 2693.24]  I feel like there's enough ways of declaring variables and just taking the address of it.
[2693.50 --> 2694.38]  We just don't need it.
[2695.08 --> 2696.42]  We don't need make and new.
[2696.42 --> 2698.50]  I would agree with that.
[2698.54 --> 2701.66]  Although the thing that I would say now would be the Go path.
[2701.82 --> 2707.22]  You know, when the idea of the Go path first came out, I kind of scratched my head quizzically.
[2707.72 --> 2709.42]  And then I went all in.
[2709.60 --> 2710.24]  100%.
[2710.24 --> 2711.88]  Everything was in my Go path.
[2711.88 --> 2717.12]  And it wasn't for many years until the Go path bit me a couple times.
[2717.12 --> 2719.50]  And now I'm kind of anti-Go path.
[2719.66 --> 2721.76]  So I would remove the Go path.
[2722.10 --> 2722.70]  I have one.
[2722.78 --> 2723.30]  I have one.
[2724.04 --> 2724.46]  What's yours?
[2724.74 --> 2724.92]  Go.
[2725.16 --> 2725.88]  No, not go.
[2726.92 --> 2727.30]  Okay.
[2728.62 --> 2730.50]  You guys didn't get that.
[2730.62 --> 2730.82]  Okay.
[2731.70 --> 2733.68]  It is Naked Returns.
[2734.94 --> 2735.38]  Oh.
[2736.34 --> 2736.96]  Very good.
[2737.00 --> 2737.54]  We don't need that.
[2738.54 --> 2738.94]  Yeah.
[2739.06 --> 2741.62]  I mean, I could see the convenience in it when they were there.
[2741.62 --> 2743.68]  But I don't think anybody is going to miss them.
[2744.60 --> 2745.00]  But yeah.
[2745.64 --> 2745.90]  No.
[2746.68 --> 2748.04]  Nobody even uses it.
[2748.04 --> 2748.20]  No.
[2748.24 --> 2750.84]  And I think it's almost always an anti-pattern.
[2751.26 --> 2751.58]  Yeah.
[2752.06 --> 2757.42]  One of the few parts of the language where you're almost guaranteed to put yourself at
[2757.42 --> 2759.20]  risk of doing something foolish.
[2760.40 --> 2763.36]  So Matt Reier also asks, what do gophers eat?
[2763.78 --> 2767.56]  And I don't know much about the animal gopher.
[2767.72 --> 2769.18]  So I couldn't answer there.
[2769.18 --> 2772.04]  I think the best I could do is tell you what I eat.
[2773.10 --> 2774.68]  Gophers eat burritos.
[2776.20 --> 2776.94]  Gophers eat.
[2777.00 --> 2777.14]  Yeah.
[2777.20 --> 2777.58]  Yes.
[2777.84 --> 2778.80]  Gophers eat burritos.
[2779.06 --> 2779.78]  That's it.
[2780.68 --> 2780.86]  Yeah.
[2780.96 --> 2781.36]  Barbecue.
[2781.66 --> 2783.30]  Gophers love barbecue.
[2783.94 --> 2784.20]  Yeah.
[2784.34 --> 2784.62]  Definitely.
[2784.74 --> 2785.10]  Barbecue.
[2785.10 --> 2787.10]  All right.
[2787.14 --> 2787.50]  Next.
[2787.76 --> 2790.72]  This sounds more like a statement than a question.
[2791.02 --> 2791.78]  But Nick Jackson.
[2792.42 --> 2793.28]  Sorry, Eric.
[2794.28 --> 2794.66]  Actually.
[2794.92 --> 2797.36]  So I don't know if you, if I'm, well, not everybody knows.
[2797.44 --> 2797.84]  I'm sure.
[2797.98 --> 2801.10]  There is a Twitter handle called GoLangFur.
[2802.10 --> 2802.54]  Yeah.
[2802.54 --> 2805.94]  And it's the best Twitter account ever.
[2805.94 --> 2808.04]  If you are a gopher.
[2808.72 --> 2811.94]  It's a, so we need to find out who's behind it.
[2812.06 --> 2813.98]  It's a, it's anonymous.
[2814.32 --> 2814.94]  We don't know.
[2815.28 --> 2818.76]  But so Matt Reier put this question out there on Twitter.
[2818.76 --> 2828.50]  And this, this, uh, gopher tweeted that gophers eat bugs for breakfast and they also eat lots
[2828.50 --> 2829.30]  of go-roots.
[2831.00 --> 2834.18]  I love the go-roots answer.
[2834.62 --> 2835.36]  That was clever.
[2835.52 --> 2841.94]  Lots, lots of good, uh, go puns in the GoLangFur Twitter account.
[2842.22 --> 2846.52]  Some of them are a real stretch, but some of them are pretty good.
[2847.24 --> 2847.86]  Okay.
[2847.86 --> 2848.46]  Okay.
[2848.46 --> 2856.70]  So Nick Jackson asks or says rather, did you know that go spelled G-O-H in Farsi means poo?
[2857.10 --> 2858.40]  And I did not.
[2858.70 --> 2862.84]  And I also find it ironic that question came in right after the what do gophers eat?
[2865.00 --> 2865.52]  Yes.
[2865.96 --> 2866.48]  Strange.
[2866.72 --> 2868.00]  I did not know that either.
[2868.26 --> 2870.82]  So no, I didn't know that.
[2871.20 --> 2871.84]  Thank you, Nick.
[2872.76 --> 2873.66]  Now we do.
[2873.96 --> 2874.92]  Now everybody does.
[2876.88 --> 2877.46]  All right.
[2877.46 --> 2878.06]  Next question.
[2878.06 --> 2879.84]  Omar Khawaja.
[2880.62 --> 2881.28]  Sorry, Omar.
[2881.78 --> 2883.64]  Uh, how do you handle dependencies in Go?
[2883.78 --> 2887.96]  Def is pretty popular, but I've seen projects place other packages inside the vendor folder
[2887.96 --> 2890.10]  for a hundred percent reproducible builds.
[2890.40 --> 2895.10]  Would like to hear some of your insights on the best practices in that area.
[2895.38 --> 2896.84]  That's what depth does, isn't it?
[2896.98 --> 2898.40]  Can we, can we punt that one?
[2898.52 --> 2899.42]  Just not answer it.
[2899.42 --> 2903.82]  No, but, but this question is, uh, I'm not sure.
[2904.54 --> 2910.16]  So just to clarify when you do, when you use depth, depth puts everything under the vendor
[2910.16 --> 2912.88]  directory or is this optional?
[2913.88 --> 2914.10]  Yeah.
[2914.14 --> 2920.42]  So I think what, um, Omar might be alluding to, and I've seen this too, is where people
[2920.42 --> 2924.36]  will like get sub module, all their dependencies in like a vendor.
[2924.36 --> 2924.80]  Yeah.
[2924.80 --> 2925.68]  So if you're a vendor, you're a vendor, you're a vendor.
[2925.68 --> 2925.84]  Yeah.
[2925.84 --> 2928.78]  Or they've manually kind of set that.
[2929.28 --> 2929.76]  Yeah.
[2929.86 --> 2934.92]  Or, or whether they actually strip the get stuff out and just check in vendor.
[2934.92 --> 2937.00]  I saw one this week that did that.
[2937.62 --> 2938.10]  Yeah.
[2938.28 --> 2938.58]  Wow.
[2938.68 --> 2939.40]  Good luck with that.
[2939.72 --> 2940.20]  I don't know.
[2940.70 --> 2946.26]  So I guess over the couple of past couple of years, I've changed, um, which dependency
[2946.26 --> 2951.28]  management tool I've used sometimes because it was, uh, the company I worked for is choice.
[2951.28 --> 2952.32]  What tool we use.
[2952.56 --> 2955.00]  Sometimes it was, I was ready for a new thing.
[2955.16 --> 2960.56]  I feel like each of them kind of, um, has things I love about them and things I hate about
[2960.56 --> 2960.90]  them.
[2961.20 --> 2964.50]  Um, more recently it's depth for everything that I do.
[2964.92 --> 2965.44]  Yeah.
[2965.78 --> 2968.92]  But I think, I think as a community, everybody's still trying to get consensus.
[2969.10 --> 2972.18]  I think glide is still a really popular choice as well.
[2972.46 --> 2973.96]  And a good solution too.
[2974.86 --> 2985.98]  In terms of how to handle dependencies, um, I only vendor dependencies in commands and
[2985.98 --> 2988.54]  executables and never in packages.
[2988.54 --> 2994.08]  And that's, that's one of the things I'm pretty sure it was Peter Bergon that, that shouted
[2994.08 --> 2995.34]  that from the mountaintop.
[2995.50 --> 3001.12]  And I agree with wholeheartedly packages should never check in their dependencies.
[3001.12 --> 3005.10]  They can declare them, but they should never check them in because at that point you risk
[3005.10 --> 3012.20]  having, um, uh, the, the type is declared in a different package problem because the vendor
[3012.20 --> 3015.24]  directory becomes part of the go path for that package.
[3015.24 --> 3016.60]  And that's just yucky.
[3016.60 --> 3017.22]  Yeah.
[3017.22 --> 3021.18]  And recursive dependencies are always a problem too.
[3021.44 --> 3026.60]  And I think there needs to be a way for like libraries to declare, I need these things
[3026.60 --> 3030.32]  and be looser probably in their versioning.
[3030.32 --> 3035.84]  Um, like I, one dot one X, right.
[3036.16 --> 3041.86]  And, you know, then the, the main, whatever package main is can declare a specific one
[3041.86 --> 3043.64]  dot one dot three or something.
[3043.64 --> 3047.60]  But I tend to, I tend to find that everybody is like super, super strict.
[3047.88 --> 3051.18]  And then you end up having, and this comes from other languages too.
[3051.24 --> 3057.60]  Then you end up where one of your, your imports requires one version of the library and another
[3057.60 --> 3060.44]  one requires a different one and dependence.
[3060.54 --> 3061.78]  We're back to dependency hell.
[3062.06 --> 3065.70]  And I think dependency management has always been kind of a pain in the ass.
[3066.48 --> 3066.78]  Yes.
[3066.96 --> 3067.36]  Yes.
[3068.42 --> 3070.82]  Does anybody know?
[3070.96 --> 3071.90]  Next question.
[3072.16 --> 3072.84]  No, really.
[3072.96 --> 3080.12]  Does anybody know if we will ever end up with a central repository like Ruby has for Ruby
[3080.12 --> 3080.46]  gems?
[3081.04 --> 3081.96]  You know what I mean?
[3081.96 --> 3084.04]  You just never know.
[3084.26 --> 3086.50]  I mean, somebody would have to build it.
[3086.74 --> 3088.22]  It's probably inevitable.
[3088.70 --> 3092.88]  Um, and you know, well, but we'll have to see.
[3092.98 --> 3097.18]  I mean, I think we're still trying to figure out how the tool should work first and then
[3097.18 --> 3098.66]  move on to that.
[3099.36 --> 3099.78]  True.
[3100.78 --> 3101.16]  Okay.
[3101.26 --> 3106.16]  So Ashley McNamara asks, what do you still struggle with when writing go?
[3106.26 --> 3107.40]  What still trips you up?
[3107.40 --> 3111.48]  She's obviously never watched me live stream anything.
[3111.70 --> 3112.72]  Everything trips me up.
[3112.72 --> 3114.60]  I never remember writing go.
[3115.60 --> 3116.08]  Yes.
[3116.64 --> 3117.72]  The answer is programming.
[3117.72 --> 3123.54]  You know, not one of those people that can just write code without looking things up and
[3123.54 --> 3124.56]  thinking things through.
[3124.80 --> 3132.32]  I, I have to look up the definitions of functions, the parameters, the return, all of that all the
[3132.32 --> 3132.60]  time.
[3132.60 --> 3140.60]  And so I struggle with remembering how switch statements are, are built every single time
[3140.60 --> 3141.44]  I write a switch statement.
[3141.44 --> 3142.56]  I have to look it up.
[3142.70 --> 3144.84]  So yeah, all of it.
[3145.24 --> 3149.96]  I don't have to look up the arguments and the function so much in the function so much
[3149.96 --> 3154.26]  because a visual studio code is so awesome at doing that for me.
[3154.92 --> 3160.26]  Uh, if I were to do a switch state switch statements, I would definitely have to look it up too.
[3160.26 --> 3167.58]  And one thing that I keep forgetting to do is, uh, you know, when you check for, um, let's
[3167.58 --> 3171.18]  say you was checking for an error and that's the only thing that is being returned from the
[3171.18 --> 3171.64]  function.
[3172.74 --> 3173.62]  It's better.
[3173.76 --> 3174.60]  It's more readable.
[3174.60 --> 3179.56]  If you, if you in line the whole thing, the error check, you know what I'm talking about?
[3179.68 --> 3180.80]  I don't know how to describe it better.
[3180.88 --> 3181.52]  Yeah, exactly.
[3181.60 --> 3186.46]  With the, if at the end on the same line, I'll, I'll always forget to do that.
[3186.46 --> 3189.30]  And I don't want to forget, but I forget.
[3190.96 --> 3196.24]  See, I consciously choose not to do it very often because I'd like all of my error handling
[3196.24 --> 3197.12]  to look the same.
[3197.36 --> 3203.94]  And you can't always do that because sometimes that introduces a scope that you don't want
[3203.94 --> 3204.50]  to introduce.
[3205.58 --> 3206.92]  Yeah, that is a good point.
[3208.36 --> 3211.24]  I'm so, I'm going to say that what I do is intentional from now on.
[3211.62 --> 3212.22]  There you go.
[3212.34 --> 3213.44]  That's the way I do it on purpose.
[3213.88 --> 3214.64]  Thank you, Brian.
[3214.64 --> 3216.56]  A wizard is never late.
[3216.74 --> 3219.06]  A wizard always arrives when he intends to arrive.
[3220.00 --> 3222.36]  You just magically made my code look better.
[3222.78 --> 3223.40]  Thank you.
[3224.12 --> 3224.92]  Glad I could help.
[3225.12 --> 3228.52]  So for me, I guess I would say testing.
[3229.48 --> 3235.96]  Not, not the basic stuff, but there's still a lot of things where, especially because in
[3235.96 --> 3241.02]  recent years, I've been doing a lot of stuff that interacts with the Kubernetes client libraries
[3241.02 --> 3242.04]  and things like that.
[3242.10 --> 3249.10]  And it's just, it feels painful to try and write cohesive test suites where I don't actually
[3249.10 --> 3254.60]  have to have a Kubernetes cluster for this, whatever I'm building to connect to.
[3255.38 --> 3260.24]  I know there's some stuff in there to mock out stuff, but it's just, it feels like more
[3260.24 --> 3261.24]  work than it needs to.
[3261.24 --> 3265.36]  And then I often end up just being like, I'll test that later.
[3265.76 --> 3266.88]  And later never comes.
[3269.60 --> 3270.20]  Later.
[3270.70 --> 3270.98]  Okay.
[3271.12 --> 3273.44]  So next question by Michael Panzer.
[3273.66 --> 3277.18]  We did not, we did not escape the dependency discussion.
[3277.18 --> 3282.66]  How often has dependency handled you to spend way too much time when you didn't intend to?
[3283.26 --> 3283.80]  A lot.
[3285.64 --> 3292.08]  This happens a lot, especially in like the different versions of dependencies needed or
[3292.08 --> 3300.94]  when different nested dependencies use a different dependency manager or when certain
[3300.94 --> 3307.98]  repositories use SIM links to other places within their own.
[3307.98 --> 3308.38]  Oh, Kubernetes.
[3311.20 --> 3318.10]  The one that bit me the hardest in the last several months was Uber's Jaeger tracing library.
[3318.42 --> 3318.80]  Oh my God.
[3318.84 --> 3326.48]  When they first released it, they had pinned versions to something or other inside their,
[3326.48 --> 3329.10]  their example, their demo apps.
[3329.10 --> 3336.36]  And it was almost impossible to get your computer into a state where all of those versions were
[3336.36 --> 3337.22]  good.
[3337.36 --> 3343.24]  And I ended up creating a virtual machine just to play with Jaeger because everything was
[3343.24 --> 3344.48]  just so crazy.
[3344.88 --> 3347.60]  And that was far more work than it should have been.
[3347.68 --> 3351.78]  I don't know what the state Jaeger's in now, but it definitely soured me on the whole plan.
[3353.12 --> 3353.68]  Okay.
[3353.68 --> 3355.72]  So we made it through all of the questions.
[3356.84 --> 3357.70]  Go us.
[3358.20 --> 3358.96]  We are awesome.
[3359.10 --> 3359.60]  Okay.
[3359.60 --> 3366.56]  So if we didn't have any more questions from the live listeners, we may have a couple of
[3366.56 --> 3369.30]  minutes to go through some interesting projects and news.
[3369.30 --> 3370.60]  All right.
[3370.60 --> 3378.36]  I've got one project that's really exciting for me personally, and that's github.com slash
[3378.36 --> 3381.14]  Dave slash JS go.
[3381.14 --> 3381.24]  Go.
[3381.64 --> 3386.34]  It is a hosted go for JS solution.
[3386.34 --> 3387.32]  And it's open source.
[3387.32 --> 3388.34]  So you can do your own.
[3388.34 --> 3391.76]  But the idea is that you, um, enter.
[3392.14 --> 3394.06]  I think he's hosting it at JS go.io.
[3394.06 --> 3399.28]  I'm not sure you'd have to go to the repo and see, but you, you enter the package path at
[3399.28 --> 3405.56]  the end of the URL and it will automatically serve that up as a go for JS app.
[3405.56 --> 3410.88]  What's particularly cool about it is that, uh, one of the weaknesses of go for JS is that it,
[3410.88 --> 3414.08]  it compiles the whole standard library down to JavaScript.
[3414.08 --> 3416.06]  And that's a gigantic download.
[3416.06 --> 3423.66]  Every time you do a page refresh, however, um, Dave figured out some way to do code splitting
[3423.66 --> 3429.20]  on that so that only the individual packages that are used get served to you and they're
[3429.20 --> 3429.64]  cached.
[3429.94 --> 3431.96]  So it speeds things up dramatically.
[3431.96 --> 3437.04]  And it's just a really fun, interesting project from a learning perspective for me.
[3437.78 --> 3439.62]  I think you had the next one too.
[3440.40 --> 3443.36]  Yeah, but I was going to skip it because we just talked about a web assembly.
[3443.36 --> 3452.78]  So Nelance slash go N E E L A N C E slash go on GitHub is Richard Musial's, uh, fork of
[3452.78 --> 3455.24]  the go language where he's adding web assembly support.
[3455.48 --> 3458.16]  We already talked about how damn excited I am about that.
[3459.06 --> 3460.62]  Yeah, that's going to be awesome.
[3461.38 --> 3461.90]  Okay.
[3462.08 --> 3471.14]  So, um, what about pop pop, uh, Mark Bates pop the library that, um, Buffalo uses to manage,
[3471.14 --> 3473.02]  uh, database access.
[3473.60 --> 3476.30]  Added association support in the last week.
[3476.60 --> 3481.18]  I can't remember the name of the person that added the pull request, but holy cow, something
[3481.18 --> 3484.22]  that was awesome just became significantly more awesome.
[3484.22 --> 3486.64]  And I love pop a lot.
[3486.78 --> 3488.16]  It got a lot better.
[3488.78 --> 3489.94]  It's just a great thing.
[3489.94 --> 3496.64]  So if you are looking for some way to do a database stuff, uh, bigger than db SQL, that
[3496.64 --> 3501.16]  feels a lot like active record and rails pop is the answer to that.
[3501.16 --> 3504.30]  GitHub.com slash Mark Bates slash pop.
[3504.38 --> 3507.62]  It's got migrations and, and all of the good stuff.
[3508.26 --> 3508.82]  Nice.
[3508.82 --> 3514.36]  So then on the news front, I think it was only a couple of days ago or something.
[3514.56 --> 3516.70]  One nine four came out for go.
[3516.70 --> 3525.22]  And then I think, um, one 10, um, is really going to be released sometime today or within
[3525.22 --> 3526.38]  the next couple of days.
[3526.38 --> 3531.90]  So definitely by the time you hear, um, this, if you're listening to it recorded one,
[3531.96 --> 3532.78]  10 should be out.
[3532.78 --> 3535.18]  And I'm trying to remember some of the stuff.
[3535.32 --> 3536.80]  And one that tends to be awesome.
[3537.66 --> 3540.84]  And then the next one you had terminal UI stuff.
[3541.30 --> 3542.32]  Oh, this one's cool.
[3542.40 --> 3543.80]  I don't know how I missed it before.
[3543.90 --> 3545.08]  It's not a new project.
[3545.08 --> 3553.34]  GitHub.com slash Revo R I V O slash T V I E W T view, uh, really cool looking terminal
[3553.34 --> 3560.08]  UI widgets for people who are building, uh, terminal applications that want that, um, old
[3560.08 --> 3563.88]  BBS DOS ANSI term kind of feel to it.
[3563.92 --> 3565.16]  Really cool looking stuff.
[3565.74 --> 3567.92]  Um, I, I have to go build something with it.
[3567.96 --> 3568.88]  It just looks so cool.
[3569.08 --> 3571.00]  It brought me back to the old DOS days.
[3571.00 --> 3575.72]  And I was trying to ask Eric, I couldn't remember the name of the, um, the UI toolkit
[3575.72 --> 3582.60]  that we used way back in, in early DOS days that made those ANSI, uh, screens.
[3582.60 --> 3586.38]  So you listeners out there can remember that if you're as old as me.
[3586.70 --> 3586.80]  Yeah.
[3586.90 --> 3588.78]  So I was, I was thinking about that.
[3588.78 --> 3590.80]  Um, was it turbo vision?
[3591.54 --> 3592.06]  No.
[3592.60 --> 3593.84]  Because, uh, what was it?
[3593.86 --> 3598.02]  Turbo Pascal and the Borland C++ compiler did that.
[3599.02 --> 3600.70]  And that was like nineties.
[3600.70 --> 3601.50]  I want to say.
[3602.02 --> 3602.50]  Yeah.
[3602.58 --> 3604.22]  You're, you're 10 years too late.
[3604.74 --> 3605.28]  Oh, okay.
[3605.28 --> 3606.80]  Early, early eighties.
[3607.88 --> 3615.24]  So listeners, this is like basically like curses for DOS way back in the day.
[3616.00 --> 3618.00]  I just can't remember what it was called.
[3618.78 --> 3619.26]  Oh, well.
[3620.22 --> 3626.42]  I'm sure we have some people who, who like really know their nostalgia or, or used it.
[3626.94 --> 3630.60]  And, uh, no, all the people old enough to remember it are taking a nap right now.
[3630.60 --> 3631.42]  I should be.
[3631.42 --> 3633.90]  All right.
[3634.54 --> 3637.00]  So did we have anything else we want to talk about?
[3637.12 --> 3639.64]  I think we are just about out of time.
[3640.16 --> 3640.58]  Yeah.
[3640.58 --> 3642.76]  We're over and we're over.
[3643.12 --> 3643.72]  All right.
[3643.90 --> 3644.34]  We're over.
[3644.60 --> 3647.18]  I didn't have anything for free software Friday this week.
[3647.24 --> 3651.70]  I've been traveling a bunch, so I haven't really used anything to think about anything.
[3651.86 --> 3652.28]  Me neither.
[3652.82 --> 3653.86]  Did anybody have?
[3653.86 --> 3655.32]  I mean, I did, but I forgot.
[3655.68 --> 3656.58]  So now I can't remember.
[3656.78 --> 3657.90]  So I'm going to say no.
[3659.62 --> 3660.02]  Yeah.
[3660.08 --> 3664.24]  The only thing that really made a big impact on my life this week was Unison.
[3664.38 --> 3665.46]  And I've already mentioned Unison.
[3665.80 --> 3672.18]  Great way to synchronize folders between computers on a, on a scheduled sort of basis.
[3672.18 --> 3675.90]  I've used it several times this week and, and marveled at how damn fast it is.
[3675.90 --> 3676.34]  Okay.
[3677.50 --> 3681.20]  So with that, um, time to wrap up our show.
[3681.70 --> 3683.56]  So, uh, thanks everybody for listening.
[3683.94 --> 3686.58]  Um, check us out on Twitter at gotimefm.
[3686.86 --> 3693.96]  As always hit us up on github.com slash gotimefm slash ping, um, with comments, questions, uh,
[3694.40 --> 3696.12]  suggestions for topics or guests.
[3696.56 --> 3701.26]  Um, definitely let us know if you like, um, these AMAs and we'll try and start doing them
[3701.26 --> 3706.40]  more regularly and, uh, come up with a way to kind of consistently take questions, uh,
[3706.40 --> 3710.10]  for future AMAs, uh, with that, uh, goodbye, everybody.
[3710.16 --> 3710.80]  We'll see you next week.
[3711.14 --> 3711.80]  This was fun.
[3712.16 --> 3712.44]  Bye.
[3712.50 --> 3713.12]  Thanks for listening.
[3713.64 --> 3714.08]  Bye.
[3716.82 --> 3717.34]  All right.
[3717.34 --> 3719.40]  That's it for this episode of Go Time.
[3719.40 --> 3722.36]  Tune in live on Thursdays at 3 p.m.
[3722.72 --> 3723.18]  U.S.
[3723.30 --> 3725.62]  Eastern at changelog.com slash live.
[3726.16 --> 3728.88]  Join the community and Slack with us in real time during the shows.
[3728.88 --> 3731.30]  Head to changelog.com slash community.
[3731.58 --> 3732.52]  Follow us on Twitter.
[3732.68 --> 3733.88]  We're at gotimefm.
[3734.84 --> 3737.22]  Special thanks to Fastly, our bandwidth partner.
[3737.68 --> 3739.08]  Head to fastly.com to learn more.
[3739.50 --> 3740.28]  Also Linode.
[3740.40 --> 3742.80]  We host everything we do on Linode servers.
[3743.20 --> 3745.06]  Head to linode.com slash changelog.
[3745.48 --> 3749.76]  Go Time is edited by Jonathan Youngblood and the theme music for Go Time is produced by
[3749.76 --> 3751.20]  the mysterious Breakmaster Cylinder.
[3751.66 --> 3752.66]  We'll see you again next week.
[3752.98 --> 3753.54]  Thanks for listening.
[3758.88 --> 3759.88]  Bye.
[3760.02 --> 3760.88]  Bye.
[3760.92 --> 3762.02]  Bye.
[3762.76 --> 3762.88]  Bye.
[3763.38 --> 3763.56]  Bye.
[3763.82 --> 3764.40]  Bye.
[3764.40 --> 3764.66]  Bye.
[3765.08 --> 3765.38]  Bye.
[3765.68 --> 3766.56]  Bye.
[3766.88 --> 3767.70]  Bye.
[3767.96 --> 3768.84]  Bye.
[3769.10 --> 3770.22]  Bye.
[3770.24 --> 3772.00]  Bye.
[3774.96 --> 3775.28]  Bye.
[3775.34 --> 3777.26]  Bye.
[3777.34 --> 3777.40]  Bye.
[3777.42 --> 3777.98]  Bye.
[3777.98 --> 3778.34]  Bye.
[3782.50 --> 3786.90]  Bye.
[3786.90 --> 3787.20]  Bye.
