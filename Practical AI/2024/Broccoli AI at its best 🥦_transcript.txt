[0.00 --> 8.66]  Welcome to Practical AI.
[9.34 --> 19.54]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.24 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 32.38]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.80 --> 35.44]  So you can launch your app near your users.
[35.84 --> 37.86]  Learn more at Fly.io.
[44.26 --> 49.02]  What's up friends? Intel Innovation 2024 is right around the corner.
[49.02 --> 56.48]  Accelerate the Future. Registration is now open and it takes place September 24th and 25th in San Jose, California.
[56.94 --> 64.82]  This event is all about you, the developer, the community, and the critical role you play in tackling the toughest challenges across the industry.
[65.22 --> 67.60]  Ignite your passion for AI and beyond.
[67.88 --> 76.46]  Grow your skills to maximize your impact and network with your peers as they unleash the next wave of advancements in technology.
[76.46 --> 88.12]  Here's what you can expect. Understand the emerging innovation and trends in dev tools, languages, frameworks, and technologies in AI and beyond to empower you and the solutions you're building.
[88.60 --> 97.12]  Get in-depth technical experience. Join hands-on workshops, labs, meetups, and hackathons to collaborate and solve problems in real time.
[97.44 --> 100.70]  You can explore featured partner and Intel solutions.
[100.70 --> 111.76]  They have partners there, startups there, customers there, and Intel is showcasing the latest in products, services, and solutions across keynotes, tech sessions, and the show floor to help you meet your development needs.
[112.14 --> 125.50]  Collaborate with experts, learn and have fun, engage in interactive sessions to connect, get certified, gain unique ideas and perspectives, build long-lasting networks, and of course, have fun.
[125.50 --> 140.14]  And get inspired, hear from leading industry experts, technologists, startup entrepreneurs, and fellow developers, along with Intel leadership, CEO Pat Gelsinger, and CTO Greg Lavender, as they take you through the latest advancements in technology.
[140.56 --> 143.10]  Don't miss this chance to be at the forefront of innovation.
[143.50 --> 146.82]  Take advantage of early bird pricing right now until August 2nd.
[147.10 --> 148.80]  Register using the link in our show notes.
[149.08 --> 152.40]  Or to learn more, go to intel.com slash innovation.
[152.40 --> 155.32]  Once more, that's intel.com slash innovation.
[155.70 --> 157.56]  Or go to the show notes and click that link.
[166.64 --> 170.22]  Welcome to another episode of the Practical AI Podcast.
[170.68 --> 172.04]  This is Daniel Whitenack.
[172.16 --> 175.18]  I am founder and CEO at Prediction Guard.
[175.18 --> 184.14]  And this is a pretty special and fun episode for me because I get to kick back with an old friend of mine.
[184.74 --> 191.54]  We went to the same university, for those that haven't heard of it, Colorado School of Mines in Golden, Colorado.
[191.86 --> 196.90]  Of course, a shout out to all the ore diggers out there that are listening.
[196.90 --> 207.50]  But yeah, we have with us today Bing-Sing Chua, who is a data scientist now and working in the energy sector.
[208.06 --> 214.96]  I was really fascinated to talk over the years with Bing-Sing about all the things he's doing.
[215.20 --> 221.96]  And in particular, his kind of approach and learnings around active learning and NLP models.
[221.96 --> 227.46]  And yeah, I wanted to invite him on the show to talk through some of that and learn a little bit from him.
[227.62 --> 228.74]  So welcome to the show.
[229.02 --> 229.44]  How are you doing?
[229.90 --> 231.16]  Hi, Daniel. Thanks for having me.
[231.58 --> 236.18]  Yeah, it's been a while since the days in Colorado School of Mines in Golden.
[236.18 --> 236.66]  Good old days.
[237.02 --> 244.76]  And now you're working as a data scientist in the energy sector and also working in Asia, which is super cool.
[244.76 --> 264.44]  I'm wondering if you could give us a little bit of a sense of some of the unique things about doing data science and machine learning type of things in the context of like the energy sector, in the context of like an actual enterprise, real world kind of situation.
[264.44 --> 271.52]  Because we talk a lot about recently, we've been talking a lot about all of these Gen AI models and APIs and such.
[271.76 --> 272.98]  And that is super cool.
[273.16 --> 281.36]  But also there's a lot of on the ground work going on in data science that maybe looks quite a bit different than that.
[281.76 --> 282.48]  Yeah, thanks.
[282.90 --> 290.46]  So, I mean, I work in the energy sector and it's pretty much a traditional type of sector.
[290.46 --> 304.46]  A lot of the companies, as you go around, at least in Asia, or at least over here where I'm at, we do not actually even have things like cloud services or subscription and stuff like that due to different reasons and stuff.
[304.98 --> 311.22]  But at the same time, there's an appetite for machine learning, AI, data, and all of those things.
[311.56 --> 313.62]  You see people talk about Gen AI as well.
[313.62 --> 324.14]  But I think the ones that I've noticed, at least for me personally, that has really brought a lot of values are kind of what you guys were talking about in the previous episode of Broccoli AI.
[324.78 --> 325.66]  Broccoli AI.
[326.00 --> 326.58]  I love it.
[327.76 --> 332.96]  Yeah, not so sexy, but still really important, really brings value.
[333.48 --> 340.02]  Particularly, I guess what we're going to talk about is active learning in the context of NLP, natural language processing.
[340.02 --> 345.24]  And so I think that's a pretty exciting place to be in, to do.
[345.56 --> 348.54]  I mean, it kind of translates into Jenny to a certain degree.
[349.22 --> 361.44]  But at the same time, I think to at least the context that I'm in as well, in the sector that I'm in, we do not have things like cloud services ready for us.
[361.44 --> 362.04]  Right.
[362.10 --> 370.94]  And so you have to figure out ways to kind of bring that about in an on-prem server VM.
[371.28 --> 372.84]  So how do you work around with that?
[372.96 --> 381.50]  And how do you actually bring in cloud native modern technologies within a traditional kind of structure?
[381.50 --> 382.66]  So, yeah.
[383.06 --> 383.24]  Yeah.
[383.40 --> 401.74]  And from at least my impression, even though there's sort of not this, whether it be for security reasons or legacy reasons or just connectivity, you know, there's not the type of connection to cloud services like you're talking about that others might be working with.
[401.74 --> 415.68]  But at the same time, at least my impression is that this sort of sector and maybe others, there's other related verticals where they have been sort of data driven to some degree for some time.
[415.68 --> 427.08]  And I don't know if you could speak to that, like the types of data that people, you know, have been processing or storing or are available in those contexts.
[427.08 --> 440.12]  But yeah, I mean, that's a good point, because a lot of these traditional industries, at least, you know, in the energy sector that we see, we have sensors that are constantly flowing in data all the time.
[440.56 --> 441.42]  The data is there.
[441.66 --> 443.32]  I mean, we are collecting data.
[443.98 --> 444.16]  Right.
[444.22 --> 450.86]  And then going a little bit deeper, then you find that a lot of us have been collecting a lot of unstructured data, too.
[450.86 --> 460.14]  And so at least within, you know, where in my experience, at least what was happening was when I came in, I was pretty much the only data scientist.
[460.52 --> 465.84]  And so I had to make my existence justified in a sense.
[465.92 --> 471.10]  And so I knew that I had to be something about like bring value within this organization.
[471.84 --> 478.66]  And like I'll be able to have proof that, hey, look, data science actually does work and does bring value.
[478.66 --> 487.40]  But the quickest, I guess, low hanging fruit that I've found within, at least in the context of where I'm at, is the whole unstructured data.
[487.94 --> 492.60]  So we have been collecting thousands and thousands, hundreds of thousands of unstructured data.
[493.16 --> 498.26]  But there has never been a way to really analyze that at scale.
[498.60 --> 500.40]  So people have been analyzing it.
[500.54 --> 504.80]  They've been able to do some sort of a human analysis on it.
[504.80 --> 512.38]  But there's never been someone who's able to like say, hey, what's been happening in the past 10 years that we've been collecting all this data?
[512.46 --> 513.34]  What's it telling you?
[514.04 --> 515.88]  Nobody has really been able to do that.
[515.88 --> 524.04]  So I thought, OK, you know, maybe that could be one thing that we could actually bring in is that like you have all this data that's ready for you.
[524.36 --> 529.92]  That has all the insight, that has all the information that is locked up, right?
[530.02 --> 532.14]  Waiting to be unearthed pretty much.
[532.58 --> 535.28]  Waiting there for us to just extract it or mine it.
[535.28 --> 547.32]  So I did a quick POC for one of the departments, a company and said, hey, guys, like you've been doing a Power BI, Tableau Power BI kind of thing.
[547.96 --> 551.28]  You've been able to do stuff with your structured data, right?
[551.34 --> 555.24]  And you've been able to plot it on beautiful graphs and stuff.
[555.32 --> 557.36]  I could be able to analyze in that sense.
[557.44 --> 560.44]  What about all the unstructured data that you've been collecting over the years?
[560.44 --> 562.48]  And they said, there's no way we could do it, right?
[562.56 --> 564.42]  I mean, like you've got thousands, thousands.
[565.56 --> 568.22]  There's no possible way for you to put it in RBI.
[568.56 --> 579.80]  And so I said, like, well, maybe we could explore ways that we could actually get into machine learning to actually help you to scale that analysis from an open standpoint.
[580.62 --> 581.60]  Thankfully, they bought it.
[581.68 --> 583.00]  And that's what we took off from there.
[583.10 --> 584.92]  And it was pretty cool.
[585.12 --> 586.32]  I mean, it was a journey for sure.
[586.56 --> 587.26]  Journey to learn.
[587.26 --> 587.74]  Yeah.
[587.74 --> 587.86]  Yeah.
[588.44 --> 596.82]  So like when you say unstructured data, give people a sense of like the kinds of files or not maybe the specifics.
[597.08 --> 603.06]  But, you know, I'm imagining a file store with some type of files in it that contain something.
[603.38 --> 604.80]  Give people a sense of that.
[605.20 --> 605.66]  Yeah, for sure.
[605.80 --> 609.72]  I mean, I guess unstructured data typically would think about it as like text, right?
[609.88 --> 612.98]  It could be text or it could be something that's just out of structure.
[612.98 --> 616.98]  And in like Microsoft docs or...
[618.82 --> 625.10]  So we have been storing all of those data within SharePoint, Microsoft SharePoint, right?
[625.18 --> 631.66]  And so what I've seen is these unstructured data is usually, it usually comes in a tablet form, right?
[631.66 --> 636.34]  You have a table that is collecting all of the structured data.
[636.68 --> 643.42]  But alongside with it, there's always a comment or that additional things that you have to actually tell the story of what you're actually collecting.
[643.42 --> 648.84]  And those are the ones that I think it's always locked up.
[649.44 --> 661.68]  And you would see it's very typical in any kind of industry where you have a tablet data that collects, you know, sensor data and everything or like reports of what's been happening.
[661.86 --> 663.42]  And those are like structured.
[663.42 --> 673.06]  But then there's also a column that would bring in some sort of remarks, you know, observation or actions taken, whatever it is.
[673.30 --> 673.68]  Comments.
[674.06 --> 674.78]  Comments, yeah.
[675.02 --> 682.24]  But more often than not, we just kind of like play through it and kind of like not really put too much attention to it.
[682.24 --> 695.82]  At least within the data set that we were looking at, we had found that there were a lot more insight in those data than the structured data that they've been collecting.
[696.06 --> 697.66]  I'm talking about like safety data.
[698.00 --> 705.34]  So we've been collecting like safety reports every single day, a couple hundred sometimes, tens of them every day over the years.
[705.34 --> 709.88]  And so these data has some sort of insight, right?
[709.94 --> 715.20]  And it brings in an insight of how is the safety condition operations.
[715.68 --> 725.14]  And so with that, like the people usually see the categories or what the reports are being reported for.
[725.34 --> 734.60]  But then like when you look at the categories, you realize that sometimes it doesn't really jive with the stories that they're actually trying to bring in in the structured data.
[734.60 --> 742.22]  And so that's where the part where we felt like it's going to bring in additional insight to the structured data that we see.
[742.74 --> 742.76]  Yeah.
[742.90 --> 752.94]  And so like there's this, we've talked a little bit about like the data that you was there, the potential insights in that around safety and maybe other insights.
[752.94 --> 767.74]  But as you kind of came into this industry and kind of were getting an understanding of like, let's say that you built the coolest data science app that was out there and had a cool model in it to do some analysis.
[768.12 --> 771.48]  Like what is the reality of how that would have to run?
[772.02 --> 777.12]  Like what is in production mean or in your context?
[777.46 --> 777.70]  Yeah.
[778.16 --> 779.16]  So many things.
[779.16 --> 780.62]  I mean, just start from the data.
[780.78 --> 782.84]  We don't even have labeled data to start with.
[783.34 --> 787.42]  Say you want a classification app or model.
[787.98 --> 790.22]  You need to have some sort of a label, right?
[790.32 --> 791.82]  And we don't have that.
[791.82 --> 797.68]  And so you have to figure out ways to bootstrap your labeling process to start off and stuff.
[798.46 --> 802.76]  And then all the way down to like, of course, training the model is pretty easy these days, right?
[802.76 --> 809.68]  And, but then you have to think about things like, hey, what does that look like to put it on the server?
[810.16 --> 813.20]  Most of our servers are running Windows server.
[813.58 --> 819.04]  And so I've had experiences putting production, some apps on Windows server and that was painful.
[819.04 --> 828.72]  And so like, we have to figure out ways that like work with the ITs and stuff and said, hey, can you deploy a Linux server for us instead?
[828.96 --> 831.56]  And just work it up from there and set it up from there.
[831.92 --> 834.94]  Like being said, like that's just the overall picture of it.
[834.94 --> 838.88]  And then you get into details of like, how do you actually store your model?
[839.40 --> 858.28]  You've got to have some sort of a infrastructure to kind of hold that, which, you know, in our case, felt like MLflow is pretty good model registry experimentation, tracking and stuff to keep track of what type of models that I'm using and stuff like that.
[858.28 --> 869.42]  And then so many things, honestly, gosh, and then like, how do you actually put it on an orchestration kind of service?
[869.84 --> 876.88]  You could use cron jobs, but then, you know, it may not be so flexible, then you kind of need to work something out.
[877.12 --> 884.26]  And so you have to get some sort of orchestrator to spin it up and kind of like make that a service for your infrastructure as well.
[884.26 --> 902.74]  I love this discussion because I think it fits the theme of the show so well around being practical and the fact that, yeah, I'm sure that there's actually a good number of listeners out there who are really wanting to do machine learning, AI, data science type of things.
[902.74 --> 923.86]  And they are sort of in a similar situation in their company, because actually, I think probably more of the majority of companies are in this sort of situation than sort of infrastructure wise, extremely modern and just cranking everything out on Kubernetes in the cloud and that sort of thing.
[923.86 --> 926.62]  So, yeah, I love this.
[927.26 --> 947.34]  So you were talking a little bit about the sort of problem of, so you have all of this tabular data with extra comments and unstructured data and, you know, certain things you want to do like extract insights or classify maybe some of the unstructured data.
[947.70 --> 950.04]  But then also nothing has been labeled over time.
[950.12 --> 951.36]  It's just unstructured data.
[951.36 --> 961.68]  So talk a little bit about that bootstrapping problem and how you've thought about that in terms of, I've got all this stuff, I want to create a model, but I have no starting point.
[962.14 --> 971.22]  When we were going through that whole labeling process or data preparation process, it was pretty interesting because we really didn't have anything, no labelers or anything.
[971.52 --> 976.62]  And I didn't have a budget to get an external labeler annotator for me.
[976.78 --> 979.90]  Just hire thousands of people online?
[979.90 --> 980.40]  Right.
[980.40 --> 980.70]  Right.
[980.76 --> 981.00]  I know.
[981.10 --> 982.90]  I could just do that maybe.
[983.36 --> 988.66]  But then again, even that, like I've thought of it and our data is sensitive to start with.
[988.96 --> 994.56]  But at the same time, it's so nuanced and it's so nuanced to the context of our company.
[994.78 --> 999.66]  And so a lot of data that every company has is just so nuanced to their own context, you know.
[999.66 --> 1006.74]  And at the same time, one of the nuances is the way that like these texts are being written.
[1007.48 --> 1023.06]  And so a lot of code switching happening, you know, which means code switching, which means like in Asia, a lot of times we speak in English, but we will kind of put in some, you know, native languages that we know or that we grew up with.
[1023.06 --> 1028.76]  And so it's just kind of like you go back and forth, back and forth, and it's just kind of a common thing, especially in Southeast Asia.
[1028.76 --> 1036.76]  Right. And so you can't just hire somebody online and just kind of label it for you because you just can't.
[1037.00 --> 1040.14]  I don't even know how to bring in the context of these guys.
[1040.32 --> 1040.50]  Right.
[1040.50 --> 1050.94]  But thankfully, I mean, I would say that the part that really helped was I happen to have a really good sponsor for the project.
[1051.70 --> 1055.46]  And these sponsors, they were super on board.
[1055.76 --> 1056.56]  They were not technical.
[1057.32 --> 1060.24]  They were SMEs in their own departments.
[1060.24 --> 1074.42]  And they knew this stuff, but they know enough of machine learning and data and AI that, hey, it's, you know, kind of a model that predicts not necessarily making 100% accuracy yet go.
[1074.42 --> 1076.76]  And so they understand those nuances in a sense.
[1076.90 --> 1086.56]  And so they kind of supported that and understood the kind of things that we have to go through, you know, as a practitioner that we have to go through.
[1086.62 --> 1088.28]  They kind of understand that part of it.
[1088.28 --> 1095.78]  So that was really helpful for my part because having a good sponsor means you get really good support for the project.
[1096.44 --> 1108.02]  But that also means that there's a product that I'm working on, the app that I'm working on is for their people, you know, their subordinates and their people.
[1108.40 --> 1109.76]  And people are reporting on them.
[1110.12 --> 1114.52]  And what happens is they said to them and say, hey, guys, this is your app.
[1114.52 --> 1115.80]  I want you to help.
[1115.98 --> 1117.84]  Thanks for now with building this app.
[1118.28 --> 1126.06]  And so having the users themselves on board from the foundational bootstrap level really helped us.
[1126.82 --> 1134.14]  So because we didn't have any labels, they had the guys to actually be the ones who label for us.
[1134.36 --> 1135.58]  They were the labelers.
[1135.68 --> 1138.20]  And so the users themselves were the labelers.
[1138.20 --> 1143.82]  So honestly, I was really blessed to even just have that kind of worked out together.
[1144.76 --> 1147.30]  I think that kind of worked so much in my favor.
[1147.30 --> 1147.70]  Yeah.
[1147.76 --> 1148.32]  Yeah.
[1148.32 --> 1165.50]  And in that labeling process, how did you develop your sort of set of instructions for like how you like explaining the problem to them or helping them define the problem and the categories, for example, in a classification model?
[1165.50 --> 1166.74]  How was it for you?
[1166.76 --> 1174.76]  Because I've also had the experience personally, probably, and been burned a couple times where I'm like, oh, this problem makes sense to me.
[1174.76 --> 1176.10]  I set up the labeling thing.
[1176.10 --> 1191.70]  I release a bunch of labelers in there and either the instructions don't make sense or I've biased this in some way or, you know, likely because I like you had mentioned, I wasn't super close maybe to the to the users in that situation.
[1191.70 --> 1194.70]  But yeah, any learnings from that experience?
[1195.16 --> 1198.00]  I think it's a lot of iteration with them.
[1198.82 --> 1202.20]  I had so many times like I would travel to see them.
[1202.44 --> 1204.52]  They work in our operations.
[1204.70 --> 1207.74]  So I literally traveled there to see them in person.
[1207.86 --> 1212.62]  And I said, we would just go through, hey, these are the labels that we want to label.
[1213.12 --> 1215.96]  We kind of get a general idea of what they are.
[1215.96 --> 1227.28]  But when you get into the weeds of it, like when you get into the details of it, you're like, you would think in this situation, that label should be here, should be number one.
[1227.40 --> 1229.58]  But then now somebody else said, no, it's two.
[1230.36 --> 1234.70]  So the way I worked it out was there will always be contention.
[1234.90 --> 1240.68]  I noticed no matter how tightly knit your labelers or your team are, there will always be contention.
[1241.08 --> 1244.20]  And you just got to work around with it, at least in my experience.
[1244.20 --> 1246.18]  I just had to work around with it.
[1246.36 --> 1252.86]  And the way I worked around with it was I just kind of had a voting system, you know, and I set up an account.
[1253.08 --> 1260.96]  So the technical side of this is I could have just given them Excel sheets and they could just label them on an Excel sheet.
[1261.06 --> 1267.74]  But I find that, you know, they are doing for me a favor and a thing.
[1267.94 --> 1272.94]  But I want them to have a really good user experience instead of just going through Excel sheets and stuff.
[1272.94 --> 1278.46]  And so I used Arjila back in the days and when they started.
[1279.18 --> 1280.80]  Pre-hugging face days.
[1281.00 --> 1282.18]  Yeah, yeah, exactly.
[1283.06 --> 1288.78]  And I noticed that Arjila is amazing in the sense that it allows you to set up different users.
[1289.48 --> 1294.06]  And you could, I mean, even other kind of interfaces I've used labels to as well.
[1294.06 --> 1299.84]  But Arjila was able to, I could use the API and just kind of like set up each user, right?
[1299.94 --> 1304.14]  And then for each user, I would just kind of like sample the same data for them.
[1304.70 --> 1314.36]  So I had to actually go through the first round, the same number of set of data for them to label, say 500 of them, I think I remember.
[1314.36 --> 1317.00]  And they would all label within two weeks.
[1317.74 --> 1323.04]  And at the end of that two weeks, I'll collect them and I'll find which one of, which are the most contentious ones.
[1323.68 --> 1334.70]  And so the ones that are the most contentious, the ones that have the least percentage of the majority, I would pull it up and I said, hey guys, what do you think about this?
[1335.02 --> 1336.50]  This is contentious for you guys.
[1336.68 --> 1337.74]  Why is it contentious?
[1337.74 --> 1339.62]  And you work it up from there, right?
[1339.68 --> 1344.64]  Because chances are you're going to see the same kind of a label again, the same kind of a data again.
[1345.50 --> 1351.48]  And if you talk it out, hopefully when you see a similar thing and you said, hey, I actually, we already talked about this.
[1351.58 --> 1353.82]  We all agreed that we're going to go with this.
[1354.32 --> 1355.16]  And so that's the first round.
[1355.24 --> 1359.00]  We had the same labels, the same data set for everyone.
[1359.30 --> 1364.22]  It's a bit inefficient to a certain degree, but I think it's important to actually get into that space.
[1364.48 --> 1367.28]  So you understand the contentions of each person.
[1367.74 --> 1373.56]  And then the second round I have everyone just kind of like label that scale pretty much.
[1374.28 --> 1376.68]  And yeah, we collect that from there pretty much.
[1377.30 --> 1377.60]  Interesting.
[1377.88 --> 1378.00]  Yeah.
[1378.08 --> 1386.98]  So you did in this process, you did a initial sort of offline bootstrapping of labels, right?
[1386.98 --> 1387.82]  And did that.
[1387.82 --> 1394.18]  So like scale wise, like what sort of scale when you're solving.
[1394.36 --> 1402.14]  So here we're talking about an NLP problem, creating a classification model on some labels of this unstructured data.
[1402.32 --> 1404.80]  Of course, this would vary by domain.
[1404.80 --> 1413.48]  But sort of what scale of labels did you shoot for when you were doing that initial trying to get to that place where you could start up and train your first model?
[1413.48 --> 1418.42]  We did just about 1,800 to 2,000 labels.
[1418.58 --> 1418.86]  Okay.
[1419.20 --> 1420.96]  Or rows of data, basically.
[1421.58 --> 1423.32]  And then we start training our first model.
[1423.68 --> 1429.72]  That probably means you're not training like a 400 billion parameter model with 1,800 samples.
[1430.42 --> 1433.28]  You don't even have infrastructure to be able to train that.
[1434.08 --> 1434.40]  Yeah.
[1436.30 --> 1437.30]  No, we don't.
[1437.30 --> 1441.02]  So what does a broccoli AI model look like?
[1441.36 --> 1443.76]  I mean, this is all text, right?
[1443.86 --> 1449.94]  And so we were going with like the simplest you can find on Hugging Face at that time.
[1450.36 --> 1456.40]  I think at the time, sentence transformers were really making it big, you know, for different reasons.
[1456.40 --> 1459.64]  Like whether it's topic modeling or classification.
[1459.64 --> 1470.14]  And at the same time, too, I remember they came up with the set fit model, which is fine tuning the sentence transformer, which was honestly revolutionary for me.
[1470.52 --> 1470.62]  Yeah.
[1470.68 --> 1471.16]  Amazing.
[1471.54 --> 1483.12]  And I thought it was amazing that like you're able to do something that was meant for similarity, but then you could actually fine tune it for classification and with pretty good performance.
[1483.12 --> 1489.02]  And it's supposed to be something that is a few shot classification model, a few shot kind of fine tuning.
[1489.64 --> 1492.44]  And so I thought 2000 should be enough for me to start somewhere.
[1492.74 --> 1492.94]  Right.
[1493.10 --> 1501.40]  And in fact, when I trained that, I tried some other models, but I think sentence transformers were the ones that actually gave the best performance out of all.
[1502.24 --> 1503.12]  It still wasn't that good.
[1503.44 --> 1508.84]  You know, talking about like 60 something, 70% kind of thing in terms of F1 score.
[1509.16 --> 1516.48]  But when I talked to my sponsors about this, I said, hey, guys, like, you okay with like me deploying this at like 60, 70%?
[1516.92 --> 1518.64]  And I said, no, actually, that's fine.
[1518.64 --> 1519.08]  Right.
[1519.20 --> 1534.30]  Because the objective for this was number one, to bring visibility of these reports to the users is one of the pain points that they said was for us to be able to know what people have been reporting.
[1534.30 --> 1542.94]  At least in the past 24 hours, they had to get on SharePoint and just different hoops and loops to try to find out, you know, filtering and stuff.
[1543.36 --> 1549.68]  But to be able to get that sent out in the email with the classification was already a win.
[1549.68 --> 1552.60]  And so I thought, okay, let's do that.
[1552.74 --> 1554.34]  But let's not stop that, right?
[1554.42 --> 1556.64]  I mean, we should actually create a pipeline.
[1556.78 --> 1558.24]  That's where the active learning comes in.
[1558.60 --> 1567.50]  And it really helped because I'm glad that I actually used Argyla to start with the bootstrapping of our data set.
[1567.50 --> 1574.08]  And having that Argyla, which means our users are already used to the interface and they already have an account.
[1574.08 --> 1579.16]  And so I was able to kind of hack around with the Argyla as a Python API.
[1579.58 --> 1593.36]  And basically, I was able to create a loop where pretty much what this model does every day, it will bring in the new data that people have been reporting for the last 24 hours.
[1593.36 --> 1600.60]  And make some prediction on it at about 60%, 70% F1 score, accuracy, whatever it is.
[1600.86 --> 1602.26]  And then send it out to the users.
[1602.44 --> 1603.74]  And these users will see it.
[1604.16 --> 1609.28]  And at the end of that email, they will say, hey, I don't think this is that signal.
[1609.64 --> 1610.72]  It should be this signal.
[1611.00 --> 1611.66]  I want to give a feedback.
[1611.66 --> 1620.78]  And at the end of it, they're able to click on a link that brings them to their profile in Argyla that will allow them to give a feedback for the particular data set.
[1620.78 --> 1624.00]  And so over time, now it's in production every day.
[1624.74 --> 1627.98]  I would get from time to time, I'll get people giving their feedback.
[1628.66 --> 1637.78]  And we've gotten like close to 4,000 data sets now labeled from this active learning.
[1638.04 --> 1648.58]  And so we will train a model periodically, not on what I could have done it automated, but I didn't really want to like just, I didn't feel the need for it yet to put it on automation.
[1648.58 --> 1654.78]  But then at the same time, like, you know, you're just collecting an event and we're just training it from time to time.
[1654.78 --> 1684.76]  Let's do it.
[1684.78 --> 1693.12]  Their newest AI innovation, Motific, addresses a critical challenge in the rapidly advancing world of Gen AI.
[1693.52 --> 1702.38]  Bridging the gap between concept and deployment, this model and vendor agnostic solution supports the entire Gen AI journey.
[1702.78 --> 1713.22]  From assessment and experimentation, Motific accelerates deployment from months to days while safeguarding against Gen AI security, trust, compliance, and cost risks.
[1713.22 --> 1721.22]  All while empowering business function and IT teams to rapidly configure end user assistance powered by organizational data.
[1721.22 --> 1732.10]  Motific provides advanced, customizable policy controls to prevent unauthorized access to sensitive data and helps ensure compliance throughout the entire process.
[1732.44 --> 1741.88]  With deep visibility into operational and business metrics, Motific enables you to track ROI, optimize costs, and make informed decisions.
[1741.88 --> 1749.86]  By offering a centralized view, Motific deters shadow AI usage and empowers teams to innovate responsibly.
[1749.86 --> 1760.04]  So move beyond the traditional constraints of AI implementation, utilizing AI deployment that is both responsible and is revolutionary.
[1760.64 --> 1766.46]  Ensuring your projects are not just quickly launched, but built on a foundation of trust and efficiency.
[1767.02 --> 1768.84]  Visit Motific.ai.
[1768.84 --> 1773.60]  That is M-O-T-I-F-I-C dot A-I.
[1792.98 --> 1797.84]  So Bingsoon, it's super interesting to hear kind of how the...
[1797.84 --> 1798.50]  You were able to...
[1798.50 --> 1806.02]  You were able to engage the users of the application through this like reporting process, essentially.
[1806.02 --> 1813.66]  That they were, you know, had some of the right incentives in place to respond and to give you updated labels.
[1813.66 --> 1820.40]  And you mentioned also the model repository, saving models, getting them out with MLflow.
[1820.54 --> 1825.08]  In the context of, you know, you deploying your model on-prem, you updating the model.
[1825.08 --> 1827.84]  You just mentioned kind of retraining the model.
[1827.84 --> 1837.64]  What does that look like for you right now in terms of that cycle of when you would want to push out a new model after gathering this data?
[1838.30 --> 1851.64]  How you would judge that to be worthwhile or useful in any sort of testing that is relevant to that cycle of getting in new labels, retraining, you know, evaluating that sort of thing?
[1851.64 --> 1856.86]  What does that look like for you and how do you kind of put in the right...
[1856.86 --> 1860.58]  Or how have you thought about the right metrics to understand when to update the model?
[1860.90 --> 1863.14]  At this point, honestly, we keep it simple.
[1863.36 --> 1868.02]  We just kind of like periodically do it at a cadence, you know, a couple months or two.
[1868.48 --> 1876.40]  But I did think about like, what does it look like to actually measure the drift of the data and stuff like that of the model predictions?
[1876.40 --> 1878.88]  That could be one of the ways that we could do it too.
[1879.32 --> 1888.66]  But what I'm seeing is actually the model is doing its job fairly well, well enough to actually solve the business problem.
[1889.28 --> 1896.68]  And so we don't see a need to actually implement a more sophisticated monitoring unless we need to, you know.
[1897.06 --> 1898.62]  That's where we're at with it.
[1898.62 --> 1899.18]  Yeah.
[1899.18 --> 1905.78]  And when you push your model, sort of like you update it, you had mentioned the model repository.
[1906.30 --> 1909.86]  How are you shipping your model out to the application?
[1909.86 --> 1914.62]  Because I think, like you had mentioned, you know, you only have so many resources.
[1914.62 --> 1923.62]  I think there's also a lot of people out there in your situation where I think it was Kristen Lum on a previous episode.
[1923.84 --> 1938.46]  She had talked about kind of that data scientist out there that is maybe one of very few or the only data scientist in potentially a large organization and having to like do all of these things.
[1938.46 --> 1940.34]  They're not like an ML ops person.
[1940.56 --> 1942.06]  They're not a model trainer.
[1942.20 --> 1944.58]  They're not a observability person.
[1944.76 --> 1945.98]  They're doing all of that.
[1946.04 --> 1946.20]  Right.
[1946.24 --> 1951.88]  So there are limitations to, you know, how much sophistication you can put in place.
[1951.88 --> 1957.52]  And I think that like some people go way too far and they're like, oh, I'm going to implement all of this stuff.
[1957.52 --> 1965.44]  And it actually makes their life as a practitioner less happy than otherwise.
[1965.84 --> 1967.58]  So, yeah, how have you found that balance?
[1967.58 --> 1981.00]  And like, what does it look like for you to do these cycles in terms of tooling and the things maybe that you, like you say, you mentioned you thought at some point maybe it's relevant to implement some of this observability stuff.
[1981.00 --> 1982.42]  But maybe not yet.
[1982.42 --> 1983.60]  Or there's other priorities.
[1983.60 --> 1991.96]  So what does that look like for you in terms of how you decide what level of sophistication is right and how you push things out?
[1992.24 --> 1996.50]  And I'm 100% with that, honestly, because it is a matter of priority.
[1997.08 --> 1998.02]  My customers are happy.
[1998.14 --> 1998.60]  I'm happy.
[1998.88 --> 2001.62]  And I'm not going to like change what's, you know, what's good.
[2001.86 --> 2003.72]  I don't want to break what's been working.
[2003.90 --> 2004.08]  Right.
[2004.28 --> 2004.76]  So to speak.
[2005.34 --> 2012.48]  But that being said, like I, you know, when it comes to like all of that, I think I have a general idea of what would be the minimum thing.
[2012.48 --> 2018.80]  So now I'm working on some other things as well, like anomaly detection and stuff like that, which needs to be deployed.
[2019.46 --> 2028.50]  So having gone through that, that kind of like set up like a pseudo infrastructure for me to know what kind of infrastructure that I'm going to be looking for, for whatever else that I'm working on.
[2028.50 --> 2033.86]  And at the bare minimum, I think model registry is super important.
[2034.58 --> 2043.28]  And being able to call the different versions that you've been training and being able to track that and being able to call it through an API, through a function.
[2044.08 --> 2047.28]  You know, MLflow has this great Python connection with it.
[2047.42 --> 2050.48]  And so being able to do that is just amazing.
[2051.10 --> 2052.30]  I mean, it keeps my life sane.
[2052.64 --> 2052.74]  Right.
[2052.74 --> 2056.08]  I don't have to like figure out where I store my model pretty much.
[2056.52 --> 2064.90]  So I would be doing exactly the same things with whatever that I'm working on next, which I've since moved on from that project.
[2064.90 --> 2066.66]  And I'm just kind of like maintaining it.
[2066.94 --> 2068.70]  That project's kind of non-maintenance.
[2068.76 --> 2074.00]  And now I've moved on to a different project to solve a different part of the business, you know, in that sense.
[2074.00 --> 2080.56]  But that project kind of set, like I said, set the foundation and knowing what kind of things that needs to be done.
[2080.82 --> 2083.32]  So, sorry, I'm kind of going ahead of myself.
[2083.56 --> 2089.80]  So one is MLflow being the most important thing for me in terms of this sort of scenario.
[2090.18 --> 2096.52]  The other one is orchestrator is also really important, having a really robust orchestrator.
[2097.06 --> 2103.06]  So for me, I think Prefect was perfect for me, you know, and I was able to do different things and stuff.
[2103.06 --> 2103.30]  Yeah.
[2103.54 --> 2106.84]  The types of things that you're orchestrating are what types of things?
[2107.16 --> 2109.78]  You could do it real time with Prefect at the same time.
[2109.84 --> 2111.16]  You could also be listening and stuff.
[2111.48 --> 2118.94]  But at the same time, you could also just do running on schedule, calling different functions, sub functions and things like that.
[2119.34 --> 2122.02]  So that was really cool to be able to have that.
[2122.24 --> 2123.68]  That's pretty much what we do right now.
[2123.78 --> 2127.12]  We're not really going into real time monitoring yet.
[2127.44 --> 2130.58]  Until we do that, then we'll have to figure out something else more sophisticated.
[2130.90 --> 2131.00]  Yeah.
[2131.00 --> 2131.40]  Yeah.
[2131.40 --> 2132.00]  Yeah.
[2132.14 --> 2138.88]  And are you just shipping your models sort of as part of a Docker container or something like that?
[2138.98 --> 2139.40]  Pretty much.
[2139.48 --> 2139.62]  Yeah.
[2139.78 --> 2146.26]  We do use Docker containers and just so that we can keep it contained in that sense.
[2146.52 --> 2146.72]  Yeah.
[2146.96 --> 2147.52]  That's awesome.
[2148.08 --> 2152.54]  I think you had mentioned in one of our conversations something about DuckDB.
[2153.54 --> 2155.72]  Where does that fit into some of this?
[2155.72 --> 2160.58]  So the raw data that we get from is from SharePoint.
[2161.20 --> 2169.20]  But if you have anyone who has any experience with SharePoint in terms of wrangling and data stuff, it's so painful.
[2169.76 --> 2169.90]  Yeah.
[2169.90 --> 2178.04]  So I thought that would be good to actually have some sort of a middle layer, mini lake house of data lake kind of thing.
[2178.04 --> 2182.66]  And I didn't want to bother my IT guys too much.
[2182.82 --> 2185.38]  So I thought DuckDB is a great thing for it.
[2185.50 --> 2185.64]  Right.
[2185.64 --> 2187.32]  I don't need a VM for it.
[2187.54 --> 2191.42]  And you can have an embedded SQL service that you can use.
[2191.42 --> 2195.50]  So that's being pulled every day, pulling the data into DuckDB.
[2195.78 --> 2200.38]  And DuckDB will be the one that actually cleans up the data, preparing the data to send it to the model.
[2201.10 --> 2210.02]  And that becomes like a pipeline for me to be able to work around the whole complexity of SharePoint, really.
[2210.02 --> 2226.26]  Yeah, I personally found a lot of use for DuckDB even in the past year on the more Gen AI stuff where you're doing sort of like text to SQL or like queries and that sort of thing.
[2226.26 --> 2233.48]  And every company we're working with has different crazy sets of data or different configurations of this or that.
[2233.62 --> 2247.68]  And that layer of having a kind of unified analytics layer, but also not sort of, you know, easy to pull in to Python, easy to spin up, easy to like test with locally and then like deploy with.
[2248.18 --> 2249.24]  Yeah, that's been really useful.
[2249.62 --> 2253.78]  I remember you talked about LensDB, you know, for Rack and things like that.
[2253.94 --> 2255.22]  And it's the same thing.
[2255.22 --> 2257.56]  I love like embedded database.
[2257.86 --> 2265.40]  I think it just works well, you know, and like it's kind of scalable eventually, you know, and I think I really like that.
[2265.84 --> 2275.40]  I think there was one blog post I've always referred back to because I also went through the, you know, you and I were at Mines at the same time.
[2275.40 --> 2277.70]  And then like there was like data science hype.
[2277.70 --> 2287.26]  And then there was like the big data period where everybody was in Hadoop and Spark and all this stuff, which I know a good number of people still use Spark.
[2287.42 --> 2291.70]  But there's a blog post by the Mother Ducker company.
[2291.70 --> 2292.70]  Yeah.
[2292.70 --> 2292.88]  Yeah.
[2292.88 --> 2301.72]  But I think the title is big data is dead or something that basically goes through some of the discussion around like, hey, we all thought we had big data.
[2301.72 --> 2308.44]  But like the actual query problem, like the types of queries that we need to run, these aren't like big data problems.
[2308.82 --> 2310.32]  What's needed is different.
[2311.00 --> 2315.66]  So, yeah, for those shout out to whoever wrote that blog post, because it was really, really good.
[2315.66 --> 2319.06]  If you ever want to come on the show and talk about it, that would be awesome.
[2319.74 --> 2319.90]  Yeah.
[2319.98 --> 2333.80]  Well, as you kind of look back on this process and some of the things that you've learned, like what are you what are you looking forward to in terms of like the future of the process of your own work or of the things you're learning?
[2333.80 --> 2338.24]  Or maybe like as you go into this next phase, it sounds like you're working on some new things.
[2338.78 --> 2343.28]  You'll want to reuse some of the tooling and kind of process that you have used.
[2343.50 --> 2352.52]  But, you know, what's different or what are you excited about kind of for this next phase in light of what you've kind of learned over the past years?
[2352.98 --> 2359.56]  Generally speaking, I think MLObs is just so nuanced, you know, in different contexts.
[2360.26 --> 2362.60]  Everyone has a say of what should be done.
[2362.60 --> 2368.24]  And I think if I learned something from this was nobody really knows everything.
[2368.80 --> 2377.58]  So you kind of have to figure out from there and you kind of take a risk on certain things that you decide in terms of your system design and stuff.
[2378.04 --> 2385.06]  What I'm excited for is actually to be able to take this and see what it looks like to for other things.
[2385.06 --> 2391.20]  Right. And in other applications, like whether it's a anomaly detection or whatever it is.
[2391.20 --> 2404.80]  In a broader sense, I think I'm excited to see things like embedded database, you know, getting more and more mainstream, especially in the context of LLM and Gen AI and stuff.
[2405.12 --> 2408.18]  I'd love to see that getting more and more mainstream as well.
[2408.18 --> 2424.74]  One of the things I'm always thinking about is scale is one thing because we a lot of the applications that we talk about today, especially in the context of Gen AI, we always talk about like the bigger compute and bigger scale.
[2424.74 --> 2437.16]  I would love to see that getting smaller, which it is happening now, getting more accessible on different devices and stuff, being able to do more cool stuff on device and the band stuff on there.
[2437.42 --> 2438.28]  I'm excited for that, too.
[2438.28 --> 2454.16]  Yeah, I think there's a lot of people excited for that and sort of this new phase of AI where people talk about AI everywhere or this sort of thing, which in reality, you know, there's been machine learning and data science sort of everywhere for some time.
[2454.16 --> 2465.06]  But that sort of wave of these newer generation of models kind of being runnable in more practical scenarios is exciting.
[2465.76 --> 2471.28]  But yeah, thanks for joining Beansoon to talk about a little bit of your broccoli AI.
[2471.70 --> 2473.76]  It's been fun.
[2474.38 --> 2475.60]  Love it. Thanks for indulging me.
[2475.60 --> 2476.48]  Yeah, yeah.
[2476.64 --> 2483.56]  You and I can can hype the broccoli AI and I'm sure we can get Demetrius to help us hype it, too.
[2483.70 --> 2483.88]  Yeah.
[2484.70 --> 2486.80]  I don't know if he trademarked that term.
[2487.48 --> 2489.72]  He's got it in his hype cycle now.
[2490.10 --> 2491.32]  So yeah.
[2492.12 --> 2495.24]  Thanks so much for joining and hope to talk to you again soon.
[2495.68 --> 2495.98]  Thanks.
[2496.04 --> 2496.38]  Thanks, man.
[2504.38 --> 2505.26]  All right.
[2505.26 --> 2507.92]  That is Practical AI for this week.
[2508.70 --> 2509.76]  Subscribe now.
[2509.92 --> 2514.90]  If you haven't already, head to practicalai.fm for all the ways.
[2515.38 --> 2521.30]  And join our free Slack team where you can hang out with Daniel, Chris, and the entire Changelog community.
[2521.90 --> 2526.52]  Sign up today at practicalai.fm slash community.
[2527.12 --> 2534.06]  Thanks again to our partners at fly.io, to our Beat Freakin' Residence, Breakmaster Cylinder, and to you for listening.
[2534.06 --> 2536.20]  We appreciate you spending time with us.
[2536.50 --> 2537.72]  That's all for now.
[2537.96 --> 2539.66]  We'll talk to you again next time.
