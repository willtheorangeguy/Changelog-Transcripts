[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.04] And unlike standard droplets, which use shared virtual CPU threads,
[29.04 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.42 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.20 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 → 88.56] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.16 → 102.28] And now onto the show.
[107.10 → 110.18] Welcome to another episode of the Practical AI podcast,
[110.58 → 115.36] where we make artificial intelligence practical, productive, and accessible to everyone.
[115.94 → 118.18] I am one of your co-hosts, Chris Benson.
[118.18 → 121.24] I am Principal AI Strategist at Lockheed Martin.
[121.78 → 127.84] And with me today, as usual, is my co-host, Daniel Whiten ack, who is a data scientist at SIL International.
[127.98 → 128.78] How's it going today, Daniel?
[129.12 → 130.06] It's going great.
[130.20 → 134.26] It seems like the past week or so has been the week of messy data for me.
[134.26 → 144.24] So I've been dealing with a bunch of missing rows and weird data issues, it seems like, for the past week,
[144.28 → 148.38] which maybe that's, like, typical for every person in AI.
[148.48 → 150.46] And everyone's like, oh, that's my week every week.
[150.56 → 154.06] But it seems particularly to have hit me this last week.
[154.62 → 155.48] But what about you?
[155.56 → 156.76] You're at GTC, right?
[156.76 → 157.26] I am.
[157.34 → 162.40] I'm at NVIDIA GTC, which is their GPU technology conference in Washington, D.C.
[162.62 → 166.46] It's going on now, although right now I'm hanging out in the hotel room so we can do this.
[166.66 → 167.64] But a lot of fun.
[167.74 → 171.88] I came to Washington at the beginning of this weekend for the Alpha Pilot race.
[171.98 → 174.06] And, you know, we've had a recent episode on Alpha Pilot.
[174.32 → 175.80] And that was the second of four.
[176.22 → 177.62] Super cool doing that.
[177.82 → 179.20] And I had a lot of fun.
[179.46 → 181.54] Did some various things on stage.
[181.78 → 184.66] And then today at GTC, I've got a session coming up that I'm leading.
[184.66 → 189.38] It's kind of a fireside chat where I'm kind of both moderator and panellist together
[189.38 → 192.32] with a couple of others really, really smart people.
[192.96 → 194.00] Yes, that sounds great.
[194.10 → 199.16] I hope that maybe some of that will be available at some point where people can access it.
[199.36 → 199.52] Yep.
[199.68 → 201.18] I think they put it all online afterwards.
[201.74 → 202.10] Awesome.
[202.36 → 208.58] If you want to follow up on that or are interested in other things related to NVIDIA,
[209.00 → 211.46] you can definitely connect with us on our Slack channel.
[211.46 → 217.50] If you go to changelog.com slash community, you can join us on a public Slack and or on LinkedIn
[217.50 → 223.94] and ask some of those questions and follow up on guests and all of those different things.
[224.96 → 226.26] Well, today we got a treat.
[226.40 → 232.44] We have a guest by the name of James Fletcher, who is principal scientist at Graven Labs.
[232.90 → 237.70] And I think we're going to talk all about intelligent systems and knowledge graphs in the minutes ahead.
[237.86 → 238.74] Welcome to the show, James.
[238.74 → 241.70] Hi, guys. Thanks very much for having me along.
[242.20 → 246.88] So I noticed on your LinkedIn as we were prepping for the show, it said a couple of things.
[247.00 → 249.82] And one of them is a little bit, but the first one it said is it says that you're presently
[249.82 → 253.68] leading research on machine intelligence and cognition at graken.ai.
[254.02 → 257.42] But it also, and anyone that listens to the show many knows I'm an animal nut.
[257.54 → 258.76] I just own that moniker.
[259.20 → 264.64] It says that you are an entrepreneur with a background in computer vision for automated veterinary
[264.64 → 265.50] diagnostics.
[265.58 → 269.28] And I just, before we got into the main topic, I just wanted to ask you about that.
[269.34 → 272.36] If you could take just a second as a tangent and tell us what that means.
[272.68 → 273.30] Yeah, absolutely.
[273.70 → 276.04] So that was quite a fun project.
[276.46 → 282.20] And that was my first foray into machine vision, which actually started when I was studying.
[282.20 → 290.30] I was studying general engineering at university and ended up in this specialization in machine
[290.30 → 290.66] vision.
[290.84 → 292.08] And I really didn't see that coming.
[292.18 → 295.72] I always thought I was going to head towards mechanical engineering or something like that.
[296.24 → 300.62] And then when I saw the capabilities that were coming out in machine learning at the
[300.62 → 303.52] time, I was like, okay, wow, this is perfect stuff.
[303.90 → 306.08] This is disruptive, right?
[306.10 → 308.78] You can really do something new with this and no one's using this.
[308.92 → 310.16] This is clear in industry.
[310.16 → 316.32] I was studying under Professor Andrew Fisherman at the time, who's quite a big name in computer
[316.32 → 316.66] vision.
[317.52 → 319.14] And we got on well.
[319.56 → 325.22] And coming out of that course, I said to him, you know, is it okay if I look at actually
[325.22 → 326.70] commercializing some of these algorithms?
[326.86 → 331.06] This stuff is clearly enough to warrant a whole company around it.
[331.56 → 333.92] And so off I went and started doing that.
[334.22 → 335.58] That was actually a family business.
[336.24 → 337.46] My dad is also an engineer.
[337.46 → 341.46] And so the two of us decided, you know what, actually, let's give this thing a shot.
[342.08 → 342.68] How was it?
[342.90 → 348.32] Because I know like the transition of research out of university into the commercial world
[348.32 → 351.22] can be kind of an interesting journey.
[351.44 → 354.20] Was that awkward and trying to convince the right people?
[354.94 → 356.60] That's a good summary of the journey.
[357.30 → 358.08] Awkward, you mean?
[358.42 → 359.64] Well, no, I wouldn't say no.
[359.64 → 363.72] I wouldn't say it was awkward, but we weren't knowledgeable on IP and all of that kind of
[363.72 → 363.88] thing.
[363.96 → 367.18] But I mean, at the end of the day, it was released open source by the university.
[367.68 → 369.00] That was actually really pretty trivial.
[369.58 → 371.16] No, so but that actually formed.
[371.56 → 375.24] That was an interesting conversation also, because it had been implemented and released
[375.24 → 376.64] open source in MATLAB.
[376.72 → 379.34] But you know, that wasn't actually commercially useful to us.
[379.34 → 383.46] So that was a rewrite job from the start to put it into Python so that we could actually,
[383.58 → 385.02] you know, productionize that.
[385.50 → 389.14] And then it was really happenstance and things that put a lot of things together for us.
[389.20 → 391.00] We had these generic algorithms.
[391.00 → 392.84] We wanted to find a place to use them.
[393.04 → 398.44] And as a family, actually, there's a hobby farm involved here, which my parents have.
[398.74 → 402.74] And we happen to have connections with the veterinary college nearby.
[402.92 → 405.24] So we went to them, and we said, you know, we need a vertical.
[405.24 → 411.06] We need a special, a specific task that we can hone in on to actually, you know, prove
[411.06 → 413.60] the usefulness of these algorithms and what they can do.
[414.00 → 415.98] And so we were looking at veterinary science.
[415.98 → 417.70] And they said, yeah, that's exactly what we need.
[417.74 → 421.68] We don't have anyone who's actually being able to help us at the university do this stuff
[421.68 → 422.18] at the moment.
[422.42 → 424.72] So we launched this whole research effort with them.
[425.04 → 430.10] What was interesting, actually, as that developed was, and this is a lesson in being an entrepreneur,
[430.10 → 437.28] I guess, is that the core value of the business actually moved sideways from the AI algorithms
[437.28 → 442.32] that we were working with, from the machine vision, and into the actual hardware and robotics
[442.32 → 445.06] that we needed to actually fully automate the process.
[445.34 → 450.32] Because it's all very well having a machine vision algorithm that automates, you know, the
[450.32 → 451.82] skill of looking through a microscope.
[452.46 → 457.24] But if you don't have a machine that puts the microscope slide on the microscope, essentially,
[457.24 → 461.88] right, I mean, that's, I'm really simplifying it, but I'm sure you got the idea, then, you
[461.88 → 463.82] know, how many samples can you actually run?
[463.92 → 466.66] Like, what's the actual improvement you get to that whole system?
[467.16 → 469.38] And so actually, that was the area that was much harder.
[469.46 → 471.50] Once you had an image on a computer, you were kind of laughing.
[471.86 → 474.80] But getting to that point was actually a little bit, a little bit more tricky.
[475.12 → 481.72] But yeah, the end goal was actually trying to control parasite burdens in animals, particularly
[481.72 → 482.98] grazing livestock.
[482.98 → 486.70] But the but that translates sideways actually into human health.
[487.34 → 493.80] Because rough statistic is that 2 billion of the world's population actually has this
[493.80 → 495.22] parasitic worm infection.
[495.46 → 498.40] There are a number of different reasons why you might want to work on this particular problem.
[499.00 → 500.58] And there are a lot of samples to run.
[501.04 → 502.86] There are a lot of samples to run.
[503.00 → 504.10] Exactly, exactly.
[504.56 → 505.40] You hit it in a nutshell.
[506.04 → 507.22] Well, that's pretty fascinating.
[507.22 → 511.58] And I just as a way to close that off, I run an American nonprofit charity called the
[511.58 → 515.76] Animal Institute, which brings technology like AI and computer vision and such to solve
[515.76 → 517.00] problems in animal welfare.
[517.28 → 522.84] So if you ever have any interest in discussing these topics further, I definitely have a playground
[522.84 → 523.48] to play in.
[523.62 → 524.80] Well, absolutely.
[524.96 → 526.52] Sounds like we should definitely go there.
[526.76 → 528.48] I was just thinking while you're talking about it.
[528.56 → 531.50] I mean, the application is definitely interesting and valuable.
[531.50 → 536.54] But I also think it illustrates, I get asked all the time, and maybe you do as well, like,
[536.66 → 541.20] what should I start working on to get into machine learning or get into AI?
[541.56 → 543.32] What kind of problems should I start looking at?
[543.38 → 549.02] And I think like the best thing that you can do is start working in an area where you have
[549.02 → 550.94] some connection or where you're passionate about.
[551.04 → 555.00] So for you, this was kind of a connection between what you studied at university and worked
[555.00 → 560.48] on in research along with your family and engineering along with like this hobby farm and the
[560.48 → 562.56] connections you had with the veterinary school.
[562.72 → 566.58] So it made a lot of sense to go into that vertical.
[566.84 → 571.84] So yeah, that's what I think, you know, people should consider is trying, just try something
[571.84 → 576.40] out that you're passionate about, because those are usually the things that you stick with long
[576.40 → 580.64] enough to learn and to experiment and to level up.
[580.78 → 582.22] I totally agree with that.
[582.28 → 583.34] I think that's a perfect point.
[583.40 → 587.44] Because what you're really saying there is that you will exceed yourself better in things
[587.44 → 589.66] where you are motivated, right?
[589.66 → 590.10] Right?
[590.10 → 591.38] Yeah, yeah, definitely.
[591.68 → 593.26] Not just learning machine learning, but everything.
[593.40 → 596.62] So if you've got that motivation, the more motivation you can summon and put in the one
[596.62 → 599.86] place, then like, absolutely, you'll double down on it, right?
[600.08 → 602.80] The passion will get you through the hard times, right?
[602.98 → 605.62] When you're missing all those rows in your data set, right?
[606.08 → 607.14] Yeah, yeah, for sure.
[607.66 → 609.34] Thanks for the extra motivation this week.
[609.44 → 612.74] I was going to say, this is turned into completely a motivational show.
[612.92 → 614.34] Totally unexpected in this area.
[614.50 → 617.08] And we haven't even hit the main stuff we were expecting to talk about.
[617.36 → 618.32] So no, there you go.
[618.32 → 624.58] Well, speaking about that, I mean, like, how do you get from robotics and microscope slides
[624.58 → 626.46] to knowledge graphs?
[626.66 → 628.76] What's that kind of journey like?
[629.10 → 632.68] Yeah, well, unfortunately, I don't have some twisting rollercoaster to tell you.
[632.74 → 638.54] Only that when I wanted to move out of doing the technical work on that project, I was looking
[638.54 → 640.28] around for the next challenge.
[640.28 → 647.00] I suppose one of the things that I really like to be is sort of like impact driven, in
[647.00 → 648.88] terms of the choice of where I wanted to work.
[648.96 → 653.20] I wanted to see something where you can, you know, where you get that value actually disposed.
[653.28 → 657.24] And so you could see that project with the same as you had like, you could see where you were
[657.24 → 658.34] going to actually make some impact.
[658.34 → 663.86] And looked around all the roles and had this really great conversation with Seiko Prasad,
[663.98 → 665.26] the CEO here at Graven.
[665.26 → 670.98] And we were a really overexcited conversation when we first met where he was explaining to
[670.98 → 674.82] me all the ethos about Graven and the vision that the company has.
[675.14 → 679.04] And I was pretty sold to work here straight off the bat from that conversation.
[679.52 → 680.66] So really just a pivot.
[680.88 → 687.26] His ethos is to take on people that have demonstrated themselves within the scope of what they do,
[687.40 → 691.18] not necessarily that they have to be people who've worked on, you know, knowledge graphs
[691.18 → 694.56] or graphs at all in the past, right?
[694.62 → 699.10] So he's very open-minded about which field you're coming from, coming from robotics himself,
[699.22 → 699.48] actually.
[700.06 → 701.66] So there's a bit of a resonance there.
[702.54 → 702.70] Cool.
[702.92 → 705.30] Well, maybe you could just define.
[705.62 → 712.34] So if I go to like the Graven website, which is graken.ai, we'll put it in the show notes.
[712.72 → 715.20] You talk about a couple of things which you've already mentioned.
[715.44 → 718.88] And I think it'd be great to kind of dig into those terms a little bit more.
[718.88 → 722.94] So one of the things you mentioned is intelligent systems on the website.
[723.12 → 724.78] And then you just mentioned knowledge graphs.
[724.96 → 729.92] So maybe you could start out by just kind of sharing what Graven means by intelligent
[729.92 → 734.48] systems and what sorts of intelligent systems people are developing out there.
[734.88 → 735.52] Yeah, absolutely.
[736.10 → 740.76] So the terminology that's being used at the moment is an interesting and kind of hot topic
[740.76 → 741.48] of its own.
[742.28 → 745.84] Naturally, you're going to get a Graven biased spin while you're talking to me.
[745.84 → 749.08] But the general ethos, I think it's better to start with knowledge graph.
[749.74 → 749.92] Okay.
[750.50 → 755.30] It's good if we also start with how we describe Graven and what that does for people, right?
[755.40 → 759.00] So Graven itself is a database, right?
[759.18 → 763.02] And typically, when you're talking about knowledge graphs, that's what you're talking about.
[763.08 → 766.70] You're talking about some sort of actually large store of knowledge.
[766.70 → 773.30] Now, knowledge graph itself is essentially totally synonymous with knowledge base, which
[773.30 → 778.86] would be like the mathematically correct terminology that's been abused on the web a lot for other
[778.86 → 779.20] things.
[779.30 → 781.16] So we tend to go with knowledge graph.
[781.34 → 782.26] It's a little bit sexier.
[782.62 → 788.26] And also immediately gives someone without experience in knowledge bases an idea of the
[788.26 → 791.84] shape of the data, which is a graph in the computer science sense.
[791.84 → 796.58] So what do we actually mean by like knowledge graph as opposed to just graph?
[797.12 → 800.50] So there are all sorts of different graph types of format all over the place.
[800.62 → 807.76] But what we're trying to build here is a system which takes you from you want to make that leap
[807.76 → 811.18] from a graph full of data to a graph full of knowledge.
[811.86 → 815.52] Yeah, I was just going to jump in and say, I think that's maybe the part where I struggle.
[815.52 → 818.36] I think a lot of people have dealt with databases.
[819.20 → 824.28] And maybe some people are familiar with graph structured data like, oh, I've got this node,
[824.36 → 827.46] which is a person and another node, which is another person.
[827.46 → 833.70] And they're connected by I think the terminology is some edge that like is like this person is
[833.70 → 836.14] friends with this person or, you know, something like that.
[836.14 → 844.64] When does like a database or graph data go from being just a database to being a knowledge graph?
[844.82 → 845.96] What's the idea around that?
[846.38 → 846.50] Yeah.
[846.58 → 850.86] So the idea is that the way that we built the system up is how can we capture all
[850.86 → 852.96] of these different kinds of knowledge, right?
[853.12 → 857.82] And so what we have is we built a knowledge representation system.
[858.92 → 859.12] Right.
[859.12 → 866.20] So Graven itself is actually everything that's in Graven is actually built on top of a graph
[866.20 → 866.60] database.
[866.94 → 868.64] That's actually the start of the innovation.
[868.76 → 870.44] I think that helps people understand what we're doing.
[870.44 → 874.38] So we started if you start with a clean slate, and you're going to build a project, we started
[874.38 → 877.86] with a graph database, and then we built other things on top of that.
[878.16 → 878.28] Right.
[878.64 → 884.38] Can you talk a little bit about what the difference when most people probably think database, they're
[884.38 → 889.06] probably thinking of a relational database, kind of more of the classical Postgres and those
[889.06 → 889.70] kind of databases.
[890.32 → 895.12] As you explain here, could you differentiate between what a graph database and a relational
[895.12 → 898.58] database are so that people can, if they're not already familiar, they can kind of make
[898.58 → 898.92] that jump?
[899.32 → 899.94] Yeah, exactly.
[899.94 → 901.52] So as we were already talking about, right?
[901.80 → 907.58] So we've got a graph in the computer science sense as opposed to in the XY plot sense in
[907.58 → 910.72] that we've got nodes and edges interconnected, right?
[910.80 → 913.82] So in a typical graph, a node might represent anything.
[913.94 → 915.12] For instance, I like your example.
[915.12 → 919.72] From one node, which is a person to another node, which is a person you'd have, like has
[919.72 → 922.90] friends as the label of the edge in between those two nodes, right?
[923.12 → 928.38] So what we can do is rather than a relational database forces you to store everything in
[928.38 → 929.70] tables, right?
[929.74 → 930.44] That's what you've got.
[930.48 → 935.62] You've got a set of filing cabinets and each file in those respective cabinets may have
[935.62 → 939.38] a reference written on it that links you to a file in another cabinet, right?
[939.58 → 942.74] That's the kind of structure of the data that you've got available to you.
[942.74 → 947.02] But what we find is that as soon as we're dealing with data that's more representative
[947.02 → 952.06] of a network, then dealing with it in this kind of tables gets really messy really, really
[952.06 → 952.54] fast.
[953.06 → 955.84] Because as soon as you've got like one thing which is connected to eight other things
[955.84 → 959.02] and eight different file cabinets, and all of those are also connected to eight different
[959.02 → 962.20] things, you know, you get into a big mess with that starting structure.
[962.64 → 964.70] Doesn't scale well there across laterally.
[964.94 → 965.26] Exactly.
[965.48 → 969.58] And what the idea is that when you're actually trying to build some kind of application with
[969.58 → 976.26] those things, the complexity that you as the user of the database has is enormous, right?
[976.42 → 981.62] Suddenly you have to try and control this structure that wasn't really designed for the data that
[981.62 → 982.08] you have.
[982.30 → 987.06] So then you go a layer up, and you say, okay, now I need a graph structure to actually more
[987.06 → 990.08] naturally represent my data, right?
[990.34 → 992.72] And so that's where graph databases are kind of born.
[992.72 → 997.28] And when you say kind of more naturally, other than that it reflects the data, the relationships
[997.28 → 1000.70] between the data very accurately, are there any other advantages?
[1001.22 → 1004.80] A big going graph, if somebody is trying to make that decision today, and they're looking
[1004.80 → 1009.36] at that, maybe they're looking at Graven, is what are the benefits of going graph database
[1009.36 → 1011.02] versus relational database?
[1011.56 → 1017.40] I mean, I think you kind of say it in a nutshell in that the idea is to be able to naturally represent
[1017.40 → 1019.58] a network data as it is.
[1019.58 → 1024.60] Is it easier to get to the data though in that way and not having to do giant SQL, classical
[1024.60 → 1025.00] SQL?
[1025.46 → 1026.28] Exactly, right?
[1026.38 → 1030.30] And we go a level more natural again when we actually come to the knowledge graph element
[1030.30 → 1032.40] that Graven builds on top, right?
[1032.86 → 1040.08] So once you've got your data in like a graph form, now you want to be able to concisely refer
[1040.08 → 1044.50] to and search your data and reference what you're looking for, right?
[1044.50 → 1050.04] So the major innovation, I would say there are two major parts that you need to understand
[1050.04 → 1052.30] to figure out what Graven is and why it helps you.
[1052.82 → 1057.98] The first thing is we've got this knowledge representation system, and we have this flexible
[1057.98 → 1058.42] model.
[1058.72 → 1063.10] I don't think we want to talk in like technical depth on all the intricacies of that.
[1063.28 → 1063.56] Yeah, yeah.
[1063.58 → 1066.60] You can basically make entities, relations and attributes.
[1066.74 → 1070.46] We make these three things, these three kind of characters, right, that you have in the story
[1070.46 → 1075.54] of building a Graven schema and entities are, you know, things like people, things like
[1075.54 → 1079.18] companies, even things like abstract concepts in the world, right?
[1079.38 → 1083.10] But then when someone references an entity, you immediately know roughly what they're talking
[1083.10 → 1083.44] about.
[1084.42 → 1087.86] Relations are the kind of glue that sit in between these things, right?
[1087.88 → 1092.06] So that's what you would use as edges in the graph that we were talking about before,
[1092.16 → 1092.38] right?
[1092.38 → 1100.48] But relations are probably the most standout concept in terms of what we do because these
[1100.48 → 1105.06] relations allow you a huge, huge volume of flexibility.
[1105.88 → 1111.66] They say that not only can I have a friendship between two people, right, and say that person
[1111.66 → 1116.44] A is friends with person B, but I can say that they're also friends with person C, person
[1116.44 → 1117.44] D, person E.
[1117.96 → 1119.96] I can do that with one relationship.
[1120.50 → 1121.94] We used to know that as an edge.
[1121.94 → 1126.94] So in this case, what we're saying is these relations are hyper edges, right?
[1127.38 → 1132.16] And you can see there, so immediately we're starting to introduce like big concepts at
[1132.16 → 1136.04] the low level of the structure that we define, right?
[1136.34 → 1141.20] We say basically we want to upgrade how you can represent your domain.
[1141.58 → 1146.82] We want to give you this toolbox, which we're calling the schema in Graven, that lets you model
[1146.82 → 1151.74] your domain in all the complexity that it has, right?
[1152.26 → 1157.08] And that then means that you've now got this format, this structure that can govern your
[1157.08 → 1160.36] data, that can look after your data for you.
[1160.42 → 1162.92] It can make sure that you haven't done anything that's logically invalid.
[1163.08 → 1166.58] It can make sure that everything is cohesive within your database.
[1166.58 → 1173.28] So when you start adding facts, right, you now know also what the context of those facts is
[1173.28 → 1177.50] because we heavily label all the elements that go into the graph.
[1177.92 → 1183.12] For instance, you could insert a company, a charity, and a university.
[1183.12 → 1190.18] All of them, all of those types that we've described, that we can describe, have inherited from
[1190.18 → 1192.54] organization, right?
[1192.80 → 1198.64] What that now means is that when I want to search my data, I can search for either companies,
[1199.16 → 1205.74] for charities, or for universities, and I could search for those individually, or I can just
[1205.74 → 1211.52] ask more generic questions and I can say, just tell me about organizations in my data, right?
[1211.52 → 1217.88] And so what we're trying to do there is to get this really natural way to actually interact
[1217.88 → 1224.04] with your data so that you're using your own domain terminology to actually access what
[1224.04 → 1228.72] you're looking for, rather than having to say, to sort of imagine what are my nodes and what
[1228.72 → 1231.64] are my edges in my graph and how do they fit together, right?
[1231.88 → 1236.10] Instead, we try and bring that to the user and reduce the burden on them when it comes to
[1236.10 → 1238.04] assessing what's going on in their knowledge graph.
[1241.52 → 1249.08] What is up, Practically I listeners?
[1249.30 → 1252.54] We're working with Infinite Red to promote their free AI mini course.
[1252.84 → 1254.28] It's called AI Demystified.
[1254.60 → 1257.82] Learn more and enrol at learn ai.infinite.red.
[1257.98 → 1263.78] This free five-day mini course is a great introduction to the most important concepts, types, and business
[1263.78 → 1266.10] applications for AI and machine learning.
[1266.10 → 1271.80] Each day of the course includes a lesson, a quiz, and an assignment to submit your learning.
[1272.26 → 1276.60] And after you've completed the course, you'll also get a certificate of completion for your
[1276.60 → 1278.46] LinkedIn profile or for your portfolio.
[1279.08 → 1283.14] If you've been feeling lost in the world of AI and hearing lots of buzzwords, then by the
[1283.14 → 1287.08] end of this mini course, you'll be able to speak intelligently about AI and machine
[1287.08 → 1289.34] learning and their practical business applications.
[1289.88 → 1291.92] Again, this course is completely free.
[1292.30 → 1295.34] Learn more and enrol at learn ai.infinite.red.
[1295.34 → 1298.46] Again, learn ai.infinite.red.
[1310.86 → 1317.72] So James, I appreciate kind of where the conversation has landed in that there are natural ways of representing
[1317.72 → 1323.66] your data and that can be modelled well on top of a graph.
[1323.66 → 1330.18] I've tried kind of graph databases in certain scenarios with more or less success and some
[1330.18 → 1331.56] have been really useful.
[1332.00 → 1337.38] But something I always find is like it seems really hard to build a quote unquote knowledge
[1337.38 → 1344.12] graph in the sense of kind of developing your schema can be hard because you may know what
[1344.12 → 1347.80] entities you have, but not like might be multiple ways to represent them.
[1347.80 → 1353.10] Or you may have just like a bunch of unstructured data, and you're not totally sure what entities
[1353.10 → 1354.04] to choose.
[1354.04 → 1361.70] So like how do you recommend if people are interested in creating this sort of representation of
[1361.70 → 1367.98] knowledge, where should they maybe start thinking about the data that they have and how to develop
[1367.98 → 1368.46] a schema?
[1368.46 → 1371.12] So that's a really great question.
[1371.40 → 1376.42] I don't have a short answer, but essentially that has been a huge part of what I've been
[1376.42 → 1382.34] doing here at Graven and what we do overall with members of the Graven community.
[1382.90 → 1389.14] We try and help people to actually understand the principles of what is an entity, a relation
[1389.14 → 1389.72] and an attribute.
[1389.88 → 1391.08] How do they best fit together?
[1391.08 → 1395.90] And actually what's fascinating about that is that that's a really great meeting
[1395.90 → 1400.88] of philosophy and technology, which I found incredibly interesting.
[1401.56 → 1409.12] And that essentially my thoughts on this is that we now see knowledge engineering and knowledge
[1409.12 → 1414.88] representation as entire careers that are actually coming around now, right?
[1414.90 → 1419.12] That you actually have someone who's a specialist, an ontologist, I've also heard them called,
[1419.12 → 1419.36] right?
[1419.72 → 1423.64] The body of knowledge of the best way to do this is not yet set upon.
[1424.38 → 1430.28] And we have our own ways of doing that here at Graven and those ways and how we think that
[1430.28 → 1436.74] things should be done informs the design decisions that we make in the language that we provide
[1436.74 → 1438.10] for the knowledge graph.
[1438.62 → 1442.76] So at the moment, it's actually been on my to-do list a long time to actually write some
[1442.76 → 1447.74] best practice for knowledge representation and building your schema in Graven.
[1447.74 → 1450.72] We have snippets here and there, and we have examples here and there.
[1451.22 → 1456.32] And it's very difficult to give really generic guidance, but we do have some that we would
[1456.32 → 1456.70] give out.
[1457.08 → 1460.18] That's a little bit long-winded for here, but maybe we can link to that in the future.
[1460.88 → 1461.32] Yeah, no worries.
[1461.46 → 1464.14] I actually want you to extend that just a little bit.
[1464.24 → 1469.10] I'm kind of curious, what can you do with a knowledge graph that you would not be able
[1469.10 → 1472.80] to do if you didn't have one as you're talking about kind of design and thinking about,
[1472.90 → 1474.40] you know, what best practices are?
[1474.48 → 1475.30] What comes to mind?
[1475.30 → 1482.10] So the main thing that anyone who's interacted with me in a professional context will know
[1482.10 → 1487.14] is that what I harp on about is trying to get to the point of true-to-domain modelling,
[1487.40 → 1488.34] right?
[1488.50 → 1493.40] What I really want is to see people building a knowledge graph where they start with a
[1493.40 → 1499.88] schema where one person who builds the schema could show it to their colleague and their
[1499.88 → 1505.64] colleague will immediately understand what elements of data are where in the knowledge
[1505.64 → 1506.72] graph, right?
[1506.88 → 1507.58] That makes sense.
[1507.88 → 1507.98] Yeah.
[1508.06 → 1512.46] And just to clarify, to make it super clear for listeners, when you're talking about the
[1512.46 → 1517.58] schema, you would basically, like we gave the example before of like person is friend with
[1517.58 → 1518.16] person.
[1518.16 → 1523.54] So like there's a person type entity in this knowledge graph, but there could also be like
[1523.54 → 1530.30] country type entities or organizations or like different metrics, websites, resources,
[1530.50 → 1531.28] all sorts of things.
[1531.44 → 1535.72] That's the sort of schema or ontology that you're talking about, right?
[1535.78 → 1540.84] The definition of what things are we going to put in our knowledge graph, and how are we
[1540.84 → 1541.58] going to label them?
[1541.66 → 1543.18] Is that the best way to think about the schema?
[1543.18 → 1544.70] That is absolutely correct.
[1544.86 → 1550.20] And what I think is also really nice is to make some analogies to OOP, to your object
[1550.20 → 1551.38] oriented programming, right?
[1551.50 → 1555.56] So anyone who's familiar with OOP, and there's a lot of people out there, I imagine you have
[1555.56 → 1557.54] quite a lot of listeners who are familiar with OOP.
[1558.02 → 1560.80] Then what we're saying here is we're defining the class.
[1561.44 → 1562.88] We define a class, right?
[1562.94 → 1564.66] And those are our schema elements.
[1565.00 → 1569.16] And then when we actually insert data, we're inserting like instances or instantiating objects
[1569.16 → 1570.08] of that class.
[1570.08 → 1574.46] And just a quick interjection for those who don't know what OOP is, he's talking about
[1574.46 → 1575.76] object-oriented programming.
[1575.92 → 1580.40] It's a technique for representing real world concepts in code as well.
[1580.50 → 1581.12] Just keep going.
[1581.22 → 1582.88] I just wanted to let anyone know that didn't know that.
[1583.38 → 1584.26] Yeah, yeah, yeah, absolutely.
[1584.72 → 1590.20] So the idea is that all the elements that we would have, as you say, we have this schema
[1590.20 → 1594.66] and you can update that over time, but that is the map for your data, right?
[1594.66 → 1600.28] That tells you what things are present in our knowledge graph and how can they be connected
[1600.28 → 1601.28] to one another.
[1601.74 → 1605.98] So for instance, we can immediately say in that example where you had like a person entity
[1605.98 → 1611.08] and also an organization entity, we can then also define the friendship relation that you
[1611.08 → 1612.04] talked about, right?
[1612.08 → 1615.94] And we can say, okay, a person can be in a friendship with other people.
[1616.70 → 1617.78] That makes sense.
[1618.32 → 1621.42] Can a person be in a friendship with an organization?
[1621.42 → 1626.74] Now, maybe that's philosophically debatable, but I would probably say the answer is no.
[1627.06 → 1630.96] In which case, that should not be permitted by your schema, and you should write a schema
[1630.96 → 1632.22] that disallows that.
[1632.84 → 1635.80] And what that means is that takes some weight off your shoulders because when someone tries
[1635.80 → 1640.94] to add some piece of data inadvertently that says that there's a friendship between a person
[1640.94 → 1645.12] and an organization, then Graven can automatically reject it and say, no, that's rubbish.
[1645.24 → 1645.88] That can't exist.
[1645.88 → 1654.34] So I think maybe there's a bit of a misconception and maybe parts of time that I've been thinking
[1654.34 → 1658.40] about knowledge graphs and maybe other people too, where there's kind of this sense that
[1658.40 → 1663.10] like when you hear about, oh, Google's knowledge graph or something, it's just like information
[1663.10 → 1664.78] is all over the internet.
[1664.98 → 1669.74] And like if you create a knowledge graph, then all that, you just suck in all that information
[1669.74 → 1671.84] and then you automatically know a bunch of stuff.
[1671.84 → 1678.08] But there is actually a lot of work in terms of developing a schema that represents the
[1678.08 → 1682.86] types of things that you're interested, the types of knowledge that you're interested in.
[1682.92 → 1687.66] It's not just like automated thing where you just like to crawl a bunch of websites and then
[1687.66 → 1689.98] you have a knowledge graph on a certain subject.
[1690.10 → 1690.88] Would that be accurate?
[1691.30 → 1692.52] Yeah, I mean, absolutely.
[1692.70 → 1694.92] You can go in any number of ways that you want to.
[1695.56 → 1700.96] So you can start trying to scrape information from the internet, but you know, the quality of
[1700.96 → 1704.98] the information that you get may not be that high in terms of, you know, kind of, can I
[1704.98 → 1708.66] ensure validity of the kind of facts that I've pulled from that?
[1709.44 → 1711.78] And there's plenty of people that are trying to do that.
[1711.84 → 1716.44] So that would be automatic, like entity recognition and this kind of thing.
[1716.70 → 1723.88] Our focus is more on building these things from the ground up so that, you know, if you've,
[1723.96 → 1727.68] someone's got proprietary data, or they've got a particular data set that actually they can
[1727.68 → 1733.58] realize an enormous amount of extra benefit from just managing the data that they have
[1733.58 → 1738.98] very carefully rather than maybe trying to augment it with just all data from the internet.
[1739.16 → 1743.00] You know, probably you can take a more targeted approach and just bring in elements where you're
[1743.00 → 1745.22] fairly aware of what that information even is, right?
[1745.78 → 1750.40] So I wanted to kind of delve into a different area given that we're an AI podcast.
[1750.40 → 1756.94] And so I wanted to ask, you know, how is artificial intelligence related to knowledge graphs and
[1756.94 → 1761.66] are knowledge graphs a source of data that might be available for AI models or is there
[1761.66 → 1762.50] some other connection there?
[1763.06 → 1763.16] Yeah.
[1763.20 → 1764.08] I mean, where to start?
[1764.22 → 1771.02] So, I mean, the way we see it is that knowledge graphs are going to be central to the effort
[1771.02 → 1774.22] towards, well, intelligent systems, as we put earlier, right?
[1774.22 → 1779.42] So that's our nice way of trying to avoid using AI to make systems more intelligent than
[1779.42 → 1780.08] they are today.
[1780.26 → 1782.88] We want to empower them with as much as we can.
[1783.88 → 1788.92] And so the idea here is to, you know, much of the world is still using relational databases.
[1788.92 → 1794.44] And as we talked about before, you know, structurally, they present themselves, present us with some
[1794.44 → 1797.40] challenges when that format isn't natural.
[1797.40 → 1804.84] So instead, what we want to do is we want to actually be able to capture the full complexity
[1804.84 → 1806.48] of the world, right?
[1806.54 → 1811.60] Actually capture all of our knowledge in one place and then be able to present that to,
[1811.86 → 1814.02] for instance, learning models for them to learn over it.
[1814.68 → 1820.82] But what we also provide is actually the artificial intelligence of the 80s.
[1821.42 → 1823.18] That is automated reasoning.
[1823.18 → 1832.00] So what we have at Graven built into the open source core product is an automated reasoner
[1832.00 → 1840.50] that allows you to infer new data based on the data that you already have and sets of
[1840.50 → 1842.52] logical rules that you know must be true.
[1843.72 → 1846.16] So this is fascinating, right?
[1846.16 → 1853.44] Because in the day to day, we all use our deductive logical skills any number of times.
[1853.44 → 1857.40] And we essentially just don't notice because it's so second nature to us.
[1857.96 → 1865.30] But if you actually try to point to any tools that anyone technical is using right now, about
[1865.30 → 1870.14] the only thing that people have heard of, and they did like a week on it at uni or something
[1870.14 → 1870.90] is Prologue.
[1871.70 → 1875.90] That's about the only tool out there for logical programming, right?
[1875.90 → 1879.34] And it sounds like something computers should be able to do easily, right?
[1879.66 → 1883.48] Like a small set of facts and figuring out a new fact based on a rule just sounds like
[1883.48 → 1884.88] an if-else blocks, right?
[1885.04 → 1885.16] Sure.
[1885.34 → 1890.44] But when you actually try and scale that and make that work and be able to have any number
[1890.44 → 1894.70] of possible rules that you might want to be able to write and bring that into the database
[1894.70 → 1898.00] level, that's when things start to get a bit interesting there.
[1898.00 → 1902.42] Because now we can say when A and B and C are true, then D is true.
[1903.26 → 1907.14] And what's nice about this is that your database then whenever you ask for something that fits
[1907.14 → 1912.44] the bill for D, it's going to give you that regardless of whether you ever even
[1912.44 → 1913.62] stored that in the database.
[1913.62 → 1917.70] So I just had a it's almost a tangent of a question.
[1918.04 → 1923.32] Would you talk about Prologue and using automated reasoning, which was kind of before
[1923.32 → 1925.76] the days of machine learning as we know it today?
[1925.90 → 1929.06] And I just want to ask, is there any tie-in maybe today?
[1929.50 → 1933.30] I know you were saying that you're kind of including that in your approach.
[1933.44 → 1939.94] But today, I guess if we were going to tackle that with the current set of technologies, we'd
[1939.94 → 1944.28] probably use things like generative adversarial networks and along with natural language
[1944.28 → 1947.88] processing to try to create things new from what you already had.
[1948.02 → 1948.82] Is there any tie-in to that?
[1948.98 → 1952.28] And just as a random side question, is there any similarity maybe in the two?
[1952.90 → 1953.92] Well, great question.
[1954.06 → 1961.32] So I think our ethos is when you have facts, if you can write a rule that definitively tells
[1961.32 → 1966.50] you that a new fact must be true based on what you have, like that's absolutely fundamental.
[1966.50 → 1970.36] Well, you can use that, then you should use that because, why is that true?
[1970.74 → 1975.86] Well, because firstly, it generalizes perfectly, right, any new set of A, B, and C, and you
[1975.86 → 1976.84] know that D will be true.
[1977.50 → 1982.60] And secondly, it's explainable that when you see D, then you can say, well, why did I see
[1982.60 → 1982.98] D?
[1983.12 → 1986.00] And the database can tell you, well, because A, B, and C.
[1986.66 → 1991.54] Now, what's fascinating, and this is the crossover space that's happening right
[1991.54 → 1998.50] now, is, as you said, how do we see that complementing the other tools that we want to use?
[1998.88 → 2003.20] How do we see that complementing, you know, any other machine learning approach?
[2003.90 → 2007.82] And so essentially, the border for me is to describe it as well.
[2007.94 → 2013.60] You're either, if you were a human approached with a particular problem, you would probably
[2013.60 → 2017.94] decide whether to use one of kind of two major skill sets that you have.
[2017.94 → 2022.50] Either how you deduce things in your logic, or your intuition.
[2023.88 → 2027.84] And so essentially, what we need is we need to start figuring out, okay, when do we need
[2027.84 → 2032.18] to deduce things logically, versus when do we need to use a machine learning approach,
[2032.20 → 2036.26] which gives us some kind of intuition based on experience, right?
[2036.42 → 2041.20] And so that's actually the centre of my work here at Graven, is how do we actually build
[2041.20 → 2048.44] learners on top of a logical reasoner on top of a knowledge graph, in order to, like, get
[2048.44 → 2051.34] to the next level of intelligence of our machines, right?
[2051.40 → 2056.20] How do we make an iterative process between those two that ingest new facts that have been
[2056.20 → 2058.36] learned, and then reasons over them?
[2058.68 → 2062.12] Or how do we reason over facts and then learn from them, right?
[2062.12 → 2066.80] So this is very much an unsolved region, and it's super invigorating at the moment to be
[2066.80 → 2067.46] in that space.
[2067.98 → 2075.76] And what do you think are the sorts of tasks that are kind of low-hanging fruit for learning
[2075.76 → 2077.58] on top of a knowledge graph?
[2077.72 → 2083.66] For example, one thing that comes to mind is question answering sort of tasks or something
[2083.66 → 2084.14] like that.
[2084.20 → 2090.54] Are there other tasks that have been explored in AI, maybe in a non-knowledge graph way that
[2090.54 → 2095.06] you think are particularly relevant to explore on top of a knowledge graph?
[2095.44 → 2095.80] Absolutely.
[2096.12 → 2100.04] I mean, as I said, that's actually kind of the whole remit of the research division here
[2100.04 → 2104.16] at Graven, is to try and fulfill those end-user problems.
[2104.24 → 2104.80] And what are they?
[2104.84 → 2107.94] Well, I actually wrote a whole blog post on all the kinds of problems that we see there.
[2108.38 → 2110.04] So you're absolutely right.
[2110.10 → 2116.34] Question-answer systems is, I mean, that's what that 80s logical reasoning AI systems were
[2116.34 → 2118.52] all about, was building expert systems.
[2118.52 → 2121.56] But they didn't really work because you had to hand-code everything.
[2122.10 → 2127.10] Well, now we can maybe use machine learning to derive some of it automatically, right?
[2127.14 → 2128.92] And we do question-answer systems.
[2129.12 → 2133.40] And you see that with Google's knowledge graph and this sidebar that they have, right, when
[2133.40 → 2137.64] you type in a search, it may just directly find the thing that you're interested in, not
[2137.64 → 2138.16] just links.
[2138.72 → 2145.18] But then besides that, we see a lot of applications in, for instance, well, we can talk about knowledge
[2145.18 → 2145.96] graph completion.
[2146.84 → 2152.64] So that's maybe I want to find new links in between elements of my graph that I'm interested
[2152.64 → 2152.90] in.
[2153.22 → 2158.94] So for instance, if I ingest a lot of biomedical data, then maybe I want to try and predict
[2158.94 → 2162.30] new links between a drug and a disease, right?
[2162.40 → 2163.68] I want to infer new treatments.
[2164.30 → 2169.68] Or maybe I want to, you know, enrich my whole graph before I try and make those as well.
[2169.68 → 2174.70] So I can, you know, find other relations, interactions between genes, proteins, et cetera,
[2174.80 → 2174.96] right?
[2175.58 → 2177.76] But then there are other tasks on a totally different spectrum.
[2177.76 → 2186.84] So what about NLP systems and computer vision systems when you apply background knowledge to
[2186.84 → 2188.22] them, right?
[2188.26 → 2193.72] Well, as humans, when we approach understanding a person who says a sentence, we have behind
[2193.72 → 2198.46] us however many years we've been on the planet of experience of hearing people say sentences.
[2198.46 → 2202.04] We often don't really bring that, but we also have more than that.
[2202.10 → 2204.78] We also have our knowledge of the world, right?
[2204.98 → 2210.54] We often hear someone say something and we, we mishear what they say and what they said
[2210.54 → 2213.44] sounded ridiculous given our knowledge of the world.
[2213.44 → 2217.06] And so we correct ourselves, or we nudge them, and you say, did you just really say that?
[2217.40 → 2220.56] Because that, that doesn't like align with my understanding of the world.
[2221.24 → 2223.26] That's what we hope that then a knowledge graph can do.
[2223.34 → 2228.38] And we've got, you know, I've had a number of conversations with people who want to improve
[2228.38 → 2234.88] for instance, uh, their company's customer service platforms where they know the body
[2234.88 → 2235.34] of knowledge.
[2235.48 → 2237.04] They know quite a lot about a customer.
[2237.86 → 2241.98] They know a lot about their products and the kind of things that they offer.
[2242.22 → 2247.16] And, you know, if a customer says my connection is broken, can we immediately infer what they're
[2247.16 → 2247.68] talking about?
[2247.74 → 2250.76] Because we actually know products that's that customer has.
[2250.88 → 2250.96] Okay.
[2250.96 → 2253.10] They have a home broadband connection with us.
[2253.10 → 2255.74] So they're probably talking about that, right?
[2256.38 → 2261.64] In machine vision, as we've already talked about a little bit from my past, then often
[2261.64 → 2264.94] we just present a learner with a, with a flat image.
[2265.02 → 2267.72] We try and get it to guess what's in the image based just on the pixels.
[2268.48 → 2273.54] But, you know, again, if the learner starts to see things that are nonsensical in the image
[2273.54 → 2278.66] or things that go, that are often seen together, that would be a, you know, a big help for it
[2278.66 → 2284.12] to be able to understand and identify when it might be wildly wrong based on the other
[2284.12 → 2287.70] things, the other context, the surrounding context of the, of the problem that it's trying
[2287.70 → 2288.12] to solve.
[2301.00 → 2303.90] This episode is brought to you by Brave.
[2304.06 → 2305.74] Big news from the Brave team.
[2305.94 → 2307.74] Version 1.0 is official.
[2307.74 → 2312.86] That means our favourite open source, privacy focused, blazing fast browser is ready for
[2312.86 → 2313.38] prime time.
[2313.80 → 2317.00] Their brand-new iOS app landed just in time for the announcement.
[2317.30 → 2322.20] And the Brave team is celebrating by granting 8 million basic attention tokens to the community.
[2322.54 → 2326.66] That means when you download the iOS app, you get 20 bats absolutely free.
[2327.02 → 2331.92] Put it to good use by heading to changelog.com, hitting the triangle icon in the upper right
[2331.92 → 2333.88] hand corner and flipping us a tip.
[2337.74 → 2355.68] So you started to get into a little bit of the details of where you think certain tasks
[2355.68 → 2359.74] like computer vision or other things could be augmented by a knowledge graph.
[2359.74 → 2363.82] And it seemed like in some of those cases, it was a matter of like, okay, you have the
[2363.82 → 2369.58] image, and you have this other information that goes along with the image that helps you reason
[2369.58 → 2371.50] about the image or predict something.
[2371.60 → 2377.48] Is that where you see kind of the near term of knowledge graph augmented AI?
[2377.48 → 2381.36] I don't know what the proper term for that is, but is that kind of where you see the near
[2381.36 → 2381.62] term?
[2381.74 → 2387.60] I know that there's also people exploring or doing AI with graph structured data itself
[2387.60 → 2393.64] rather than just kind of extracting features from the graph as new features in a model,
[2393.64 → 2400.62] but actually using graph structured features or sub graphs or other things in AI models.
[2400.76 → 2402.04] Are you familiar with that at all?
[2402.04 → 2408.04] How do you see maybe as a person who says, okay, well, this sounds cool.
[2408.14 → 2414.66] I'd love to try to augment some of my AI systems with knowledge from a graph.
[2414.80 → 2418.38] Where might they start looking in terms of methods and next steps?
[2418.92 → 2419.02] Right.
[2419.10 → 2419.92] I mean, great question.
[2420.14 → 2421.88] So I totally agree.
[2421.94 → 2429.30] What we don't want to do is just stick with the status quo of sort of taking essentially sort
[2429.30 → 2432.64] of square shaped data as inputs to machine learning pipelines.
[2433.08 → 2433.26] Right.
[2433.46 → 2435.06] That's like the status quo at the moment.
[2435.12 → 2435.28] Right.
[2435.32 → 2438.88] Is we have our data is stored in these filing cabinets.
[2439.12 → 2443.28] And so what do we put into our machine learning model while it's data that looks like filing
[2443.28 → 2443.70] cabinets.
[2444.02 → 2444.46] Right.
[2444.50 → 2445.32] And what do we get out?
[2445.60 → 2446.32] Surprise, surprise.
[2446.56 → 2446.74] Right.
[2447.24 → 2447.52] Yeah.
[2447.52 → 2450.26] And I think it's probably confusing to people.
[2450.40 → 2454.96] Sometimes it has been for me where like TensorFlow talks about a graph.
[2455.10 → 2455.24] Right.
[2455.24 → 2457.10] So it's not a graph of the data.
[2457.32 → 2463.14] It's more of a graph of the computation and how it's executed on a certain architecture
[2463.14 → 2465.46] or the logic of that computation.
[2465.46 → 2472.02] Whereas what we're talking about here is actually data that is structured like a graph being processed
[2472.02 → 2477.12] through one of these systems as a graph would be different from just putting a tensor in.
[2477.36 → 2477.46] Right.
[2477.84 → 2478.96] That's absolutely true.
[2479.06 → 2479.22] Yeah.
[2479.22 → 2485.80] So that's one of the fundamentals that makes learning over, well, anything except just
[2485.80 → 2491.36] like a matrix or vector representation difficult is that all the frameworks are set up to
[2491.36 → 2492.48] take those things in.
[2492.58 → 2498.58] And as you say, in the case of these pipelines, the shape of the processing is a graph, but
[2498.58 → 2501.42] we don't really need to worry about that compared to the input and output.
[2501.52 → 2504.32] And as you say, what we're here, we're saying is, what do we do?
[2504.40 → 2507.62] How do we move from these square inputs to something else?
[2507.62 → 2513.00] So that's actually a big body of work that I've been doing over the last year is being
[2513.00 → 2516.34] looking at what are the approaches that have been done around that.
[2517.20 → 2521.98] And some of the first approaches, which is still quite common, is to do, for instance,
[2522.22 → 2523.30] walks through the graph.
[2523.72 → 2526.72] Like I'm interested in some particular entity in my graph.
[2526.96 → 2531.48] So why don't I start there within my graph and then just walk randomly and see what I
[2531.48 → 2533.58] encounter, record what I encounter.
[2533.58 → 2539.44] And then maybe I use that as like a row and a vector or something and feed that into my
[2539.44 → 2539.74] model.
[2540.06 → 2541.68] That's one way of doing it, right?
[2541.78 → 2544.44] But you're kind of hoping for some serendipity there.
[2544.58 → 2548.78] You're kind of hoping that I'm going to encounter things in my graph that are important, right?
[2548.80 → 2553.30] Because I'm just sort of walking around, I'm literally randomly walking is what is the
[2553.30 → 2554.84] approach through the graph.
[2554.84 → 2556.30] So, okay, so the next thing.
[2557.20 → 2561.32] And so from this, there was a really nice piece of research that came out of Stanford.
[2561.90 → 2566.12] They called their paper Graph Sage, or at least their approach was called Graph Sage.
[2566.48 → 2569.68] And we actually implemented that here over the knowledge graph.
[2570.02 → 2575.42] And the idea of that was to essentially not just take these single walks, but to actually
[2575.42 → 2581.10] look at all of your neighbours, take a subset, a random subset of all of your neighbours, but
[2581.10 → 2585.28] then also look at their neighbours and their neighbours and their neighbours and sort of have
[2585.28 → 2589.70] this more like spider web shape of the graph that you would analyze, right?
[2590.12 → 2595.54] And sort of in some way, without going into all the technical detail, basically roll
[2595.54 → 2599.10] that information inwards towards the entity that you are interested in.
[2599.48 → 2604.26] So you kind of gain some information as you move from that, like the outer radius of
[2604.26 → 2607.26] a like outer circumference of a circle, like inwards.
[2608.34 → 2609.92] And that's also really nice, right?
[2609.92 → 2614.00] So what that's also doing is still kind of putting your data into a box shape because
[2614.00 → 2615.92] you're still dealing with a tree now.
[2616.34 → 2619.16] So we've gone from a line, which was the walk, to then a tree.
[2619.86 → 2622.40] And we still didn't find what was really difficult about this.
[2622.44 → 2627.82] So we tried using this, but what it doesn't manage to capture, say we are trying to do something
[2627.82 → 2628.54] really difficult.
[2628.54 → 2632.56] We're trying to find a new drug to treat a disease.
[2632.56 → 2639.34] Now, if we try and do this, if we just look at like generally what does a drug look like
[2639.34 → 2644.18] and what's nearby to it, and also generally what does a disease look like and what's near
[2644.18 → 2650.12] to it, when we then try and match those two things, we haven't actually looked at any of
[2650.12 → 2655.24] the common connections that exist between a drug, that drug and that disease specifically.
[2655.24 → 2660.12] Like we haven't actually figured out what are the like logically, what are the paths that
[2660.12 → 2661.18] actually connect these things?
[2661.24 → 2662.82] We should probably be interested in those.
[2663.00 → 2666.40] Those are probably like the most important features in this graph.
[2666.50 → 2669.14] Instead, we've just looked at roughly what they look like.
[2669.54 → 2675.36] And then you end up with just like some generic answer, like paracetamol treats lots of diseases
[2675.36 → 2678.48] because lots of diseases exhibit pain, right?
[2678.48 → 2681.02] So what we want is, again, a more targeted approach.
[2681.12 → 2683.30] And that leads us to, no, we have to do the hard thing.
[2683.36 → 2687.24] We actually have to learn over a graph shape, right?
[2687.24 → 2689.36] We actually have to take in graph data.
[2690.22 → 2690.62] Yeah.
[2690.76 → 2695.76] So I'm kind of thinking about natural language processing because that's the world I live
[2695.76 → 2695.94] in.
[2696.02 → 2700.74] And, you know, some of what we've learned recently is that, you know, it's very useful
[2700.74 → 2708.46] to have your algorithm learn the proper representation of text taking into the context of the
[2708.46 → 2714.64] context of, you know, context around just like a single token, for example, in order to actually
[2714.64 → 2719.36] learn a good representation of text for a certain task.
[2719.36 → 2724.66] It sounds like what you're saying is it would be useful to do similar things for graphs in
[2724.66 → 2730.94] that we need to learn how to represent graph structure data in a neural network because it
[2730.94 → 2736.32] might not be like if we just take all the nearest neighbours and put them in kind of
[2736.32 → 2743.38] standard row structure and use that as a representation, then we might miss that actually the predictive
[2743.38 → 2746.14] thing is beyond the nearest neighbours, right?
[2746.20 → 2749.72] And like a bunch of links away, even though it's not a nearest neighbour, that's like the
[2749.72 → 2753.86] thing that's indicative of the thing that we're trying to predict.
[2753.96 → 2755.88] Is that kind of along the right track?
[2756.10 → 2756.48] Absolutely.
[2756.68 → 2761.18] What I see you describing there in NLP is definitely what we're aiming for here, right?
[2761.18 → 2766.58] And not just in graphs, but I think in the industry in general, is where we're now seeing like beyond
[2766.58 → 2768.06] curve fitting, it's called, right?
[2768.40 → 2773.06] And like, how do we move beyond where we are right now to a point where the machine is actually
[2773.06 → 2774.00] understanding?
[2774.18 → 2776.44] It actually learns to understand what's going on.
[2776.62 → 2780.14] So like we already talked about that with like NLP based on a knowledge graph.
[2780.20 → 2781.24] It understands the context.
[2781.32 → 2782.44] You were just talking about that there.
[2782.44 → 2788.52] In a machine vision problem, also understanding the context of what's actually in the image.
[2788.80 → 2792.78] All of these things mean that the learner can not just sort of learn by rote or learn
[2792.78 → 2796.04] by exact examples, but can actually understand what's going on.
[2796.52 → 2798.96] What's really interested in graph is that you have exactly that.
[2799.04 → 2802.16] You might have like one particular feature that you find.
[2802.26 → 2807.90] Like if I see some particular thing that's in some particular way related to what I'm interested
[2807.90 → 2809.32] in, that's a huge indicator.
[2809.32 → 2812.84] But you might also just see a general structure that occurs.
[2813.84 → 2817.80] That when the, you know, I want to have these five elements, these five entities all connected
[2817.80 → 2820.58] together in a particular way, they all have particular types.
[2821.14 → 2827.54] That is a very typical structure for a really effective drug, right?
[2828.02 → 2832.50] That those combinations come up again and again, but in like a generic sense.
[2832.54 → 2833.60] And maybe we want to learn that.
[2833.68 → 2835.16] We want to learn some kind of structure.
[2835.42 → 2838.90] So then what we were faced with was we were faced with the problem of, okay,
[2838.90 → 2841.06] no, we actually need to learn over graphs.
[2841.74 → 2846.74] And to our luck, we're not, you know, we don't have the budget to do like, and the manpower
[2846.74 → 2848.54] to do these huge research efforts ourselves.
[2848.72 → 2853.62] But our neighbours over here in London, DeepMind, released a paper last year.
[2854.02 → 2858.16] And they also released a library to support what they were doing, where they've gentrified
[2858.16 → 2864.56] a lot of the concepts of graph learning and how to do learning over graphs in this really
[2864.56 → 2865.14] neat way.
[2865.62 → 2869.40] Given they were acquired by Google, I mean, it makes sense that they also figured out how
[2869.40 → 2870.82] to do this in TensorFlow.
[2870.82 → 2870.94] TensorFlow.
[2871.66 → 2878.38] So what they've got there is a pipeline that now actually lets you input a graph into TensorFlow
[2878.38 → 2888.60] as the data and get that same graph back out as an output, but with updates made to every
[2888.60 → 2889.80] element of that graph.
[2889.80 → 2895.58] So that means that essentially what we can use is we can use that as a little toolbox that
[2895.58 → 2901.44] allows us to perform any number of different tasks over a graph structure.
[2901.76 → 2905.90] And obviously, we've tailored that here at Graven to work over the knowledge graph.
[2906.20 → 2911.90] But what we can do is we can just carefully frame the kind of problem that we have so that
[2911.90 → 2915.10] this toolbox can help us to solve that.
[2915.66 → 2917.68] And is that the Graph Nets library?
[2917.82 → 2918.58] That's exactly the one.
[2918.58 → 2919.26] Yeah, that's the one.
[2919.82 → 2920.02] Okay.
[2920.18 → 2923.36] Yeah, we'll definitely link that in the show notes as well, because it seems like they
[2923.36 → 2928.64] have a good usage example and notebooks and such that people can play with that.
[2928.64 → 2930.10] So you've totally won me over.
[2930.32 → 2933.26] And I'm looking forward to jumping in and playing with this.
[2933.34 → 2934.30] And I know Daniel is too.
[2934.82 → 2938.60] Could you start walking us through what it is like to actually build a knowledge graph
[2938.60 → 2939.18] with Graven?
[2939.44 → 2940.80] And what do you need?
[2941.08 → 2943.12] What languages do you need to know?
[2943.50 → 2947.84] And also, I noticed on the website, you talk about, is it Gravel?
[2947.84 → 2949.64] Am I pronouncing that right?
[2949.80 → 2950.36] And if you can...
[2950.36 → 2950.72] So that's Gravel.
[2950.82 → 2951.38] That's Gravel.
[2951.42 → 2951.82] Gravel.
[2951.94 → 2952.32] I'm sorry.
[2952.48 → 2953.20] My apologies.
[2953.30 → 2953.80] No, no worries.
[2954.40 → 2955.06] So yeah.
[2955.16 → 2958.62] So yeah, I can give you the whole overview of what you would do, right?
[2959.00 → 2959.40] Fantastic.
[2959.40 → 2963.76] Actually, to close down what we were talking about just there, the whole learning approach
[2963.76 → 2969.38] that we've been building and all the research that we do on top of knowledge graphs, right?
[2969.52 → 2970.50] I'll emphasize that.
[2970.86 → 2975.76] We release all of that as code available via our GitHub.
[2976.40 → 2978.76] Specifically, we have a library called Glib.
[2979.34 → 2982.34] So that's our knowledge graph library for machine learning.
[2982.34 → 2984.98] So Glib is the centre of those projects.
[2985.16 → 2989.10] And the main one that we're running right now is knowledge graph convolutional networks.
[2989.82 → 2994.26] So that's how do we apply these learners on top of both the Reasoner and the knowledge
[2994.26 → 2995.60] graph shaped data.
[2995.94 → 2998.48] The starting point is how do you actually get a knowledge graph, right?
[2998.58 → 3000.10] How do I actually get my knowledge graph together?
[3001.04 → 3006.24] Now, the components that you have there, as you pointed out, is something we should start
[3006.24 → 3006.40] with.
[3006.46 → 3008.14] So you have Graven itself, right?
[3008.14 → 3010.96] So Graven core is released open source.
[3011.18 → 3014.36] You can download that from GitHub or install it with a package manager.
[3014.80 → 3016.40] And that's a database which is going to run.
[3016.52 → 3019.90] You can install that on your local machine and get it up and running or put it in the
[3019.90 → 3020.24] cloud.
[3021.20 → 3023.78] And so you need that backend service running.
[3024.50 → 3030.12] Now, when it comes to actually accessing that, we have three officially supported drivers
[3030.12 → 3030.60] at the moment.
[3030.80 → 3033.08] We have Python, Node.js, and Java.
[3033.90 → 3037.24] So we make sure that all of those are up-to-date and working with the latest Graven.
[3037.24 → 3041.46] What's fascinating there, actually, is the communication protocol between those
[3041.46 → 3045.88] clients and Graven is called GRPC.
[3046.48 → 3052.48] So that's something from Google, Google's remote procedural call, that has replaced using
[3052.48 → 3053.36] REST services.
[3054.34 → 3059.08] So what's really nice about this, the actual end goal that that gets you to, is it means
[3059.08 → 3065.34] that when I'm accessing the database in Python, with Python, I get to actually use native Python
[3065.34 → 3065.76] functions.
[3065.76 → 3069.02] All I have to do is import the package that talks to Graven.
[3069.64 → 3072.70] Import the Graven client in Python at the top of my script, right?
[3073.08 → 3079.78] And then I can just instantiate a communicator that will talk to Graven and make queries to
[3079.78 → 3082.18] the database just out of my native Python.
[3082.82 → 3084.64] I can just launch them straight from my application.
[3085.04 → 3088.04] And it doesn't feel like you're talking to a database anymore, right?
[3088.04 → 3092.76] It just feels like you're making function calls, which comes back with information that's
[3092.76 → 3094.16] pertinent to your knowledge graph.
[3094.16 → 3095.12] That's great.
[3095.12 → 3096.42] And would you use that?
[3096.64 → 3102.20] So would you use that client tool to help you build your knowledge base?
[3102.26 → 3107.72] Like, let's say that I have a bunch of text data, and I'm like pulling entities out of
[3107.72 → 3114.46] it that I work or classifying that in a certain way to store it as a certain type of entity.
[3114.46 → 3121.24] Would I kind of be doing that in Python and then push that to Graven via the Python library?
[3121.88 → 3127.44] Are there like bulk upload techniques or like ways to get data, let's say, from relational
[3127.44 → 3128.26] to graph?
[3128.40 → 3130.22] What's the sort of range of what people do?
[3130.68 → 3131.30] Yeah, absolutely.
[3131.44 → 3131.84] Great question.
[3131.84 → 3133.88] So basically, you're absolutely on the money.
[3134.16 → 3139.50] The idea is that we give the users these clients in their native language because that's their
[3139.50 → 3140.12] strength, right?
[3140.16 → 3143.92] We already know that they know how to speak that, and they get all the freedom that
[3143.92 → 3144.94] that language offers.
[3145.96 → 3152.58] And then the way that you're actually interacting with Graven is through Graven's query language,
[3152.94 → 3154.04] Gravel, right?
[3154.08 → 3155.58] You can probably see where the name comes from, right?
[3155.58 → 3159.90] So the Graven's got this query language called Gravel, and the idea is that that's this
[3159.90 → 3161.98] really concise, really expressive language.
[3162.36 → 3167.86] But then what you would do is that is your one-stop shop for how you actually talk to the
[3167.86 → 3170.18] knowledge graph in terms of what your intentions.
[3170.74 → 3174.62] So if I want to either retrieve something, then I make what we call a match query.
[3174.90 → 3177.90] If I want to insert something, then I use an insert query.
[3177.90 → 3183.96] And if I want to, wherever I see a particular pattern, insert something that's a match insert,
[3184.08 → 3185.16] I'm sure you get the idea, right?
[3185.16 → 3188.30] So you have all of these different ways that you can read and write from the database,
[3188.30 → 3191.62] and you do all of them in the same way through your application.
[3191.94 → 3195.54] You just, you know, you call, ask the client, you say dot query, right?
[3195.56 → 3199.38] And make this query, and then the response you get back will be the answer, right?
[3199.44 → 3201.50] Either you insert something or read.
[3202.10 → 3206.76] Now then what we've got, we've got a number of, we've got a repository of examples so that
[3206.76 → 3207.82] people can have a look on there.
[3208.20 → 3213.18] You know, very typically people are, as you say, they're migrating from either SQL data or
[3213.18 → 3219.64] from CSV data, in which case it's a matter of just writing what we call an ETL pipeline.
[3219.64 → 3224.60] So something that will just traverse over all of that data that you have and make the appropriate
[3224.60 → 3229.08] queries in Grackle to get that data shifted over into Grackle itself.
[3229.08 → 3235.44] Now, one of the questions that people ask me really often, and definitely comes in on our community
[3235.44 → 3239.86] Slack quite often, is can I like automatically build my knowledge graphs?
[3239.94 → 3242.84] And we kind of talked about that a bit earlier in the call.
[3243.24 → 3249.58] The problem is that, like, it's possible to automatically ingest a relational database
[3249.58 → 3250.76] into a knowledge graph.
[3250.76 → 3254.86] But the problem is, you just end up with the same structure that you had in your relational
[3254.86 → 3255.42] database.
[3255.56 → 3258.68] But in the knowledge graph, you know, you still end up with something broken, because
[3258.68 → 3265.18] you need to apply that human understanding that you have of the data that you have in
[3265.18 → 3266.22] these table formats.
[3266.52 → 3268.28] You need to say, what's that actually mean?
[3268.84 → 3270.08] What does my domain look like?
[3270.14 → 3274.00] So what you do is you first, well, it's an iterative process, of course, like a lot of
[3274.00 → 3277.60] engineering, but you're going to start out by saying, here's my schema.
[3277.60 → 3279.48] Here's what I think my domain looks like.
[3279.94 → 3287.30] Okay, now when I go over this file, what parts of that schema can I infer from the particular
[3287.30 → 3288.72] row I'm dealing with right now?
[3289.58 → 3294.48] So I guess if somebody wants to get into this, I know we're both very excited about it.
[3294.72 → 3297.66] And I've learned a lot that I didn't know before the conversation.
[3298.14 → 3303.54] Where can they go and learn more and actually start digging into using Grackle themselves and
[3303.54 → 3303.92] Grackle?
[3304.06 → 3305.84] Any specific links that you want to recommend?
[3305.84 → 3309.30] Well, we have the docs available on our website.
[3309.42 → 3310.86] People seem to think those are quite fun.
[3311.60 → 3316.16] And we also have, so there are also some in-depth examples there on, for instance, how to do
[3316.16 → 3320.06] data migration into Grackle so that you've got, you know, get that knowledge graph up and
[3320.06 → 3321.94] started so you've got something to play with.
[3322.36 → 3325.58] We then have an examples' repository on our GitHub.
[3326.26 → 3331.44] And also for those who really like to jump in at the deep end, then the Glib repo is quite
[3331.44 → 3335.50] a good place to, if you want to see immediately from the top, how are you going to then do
[3335.50 → 3336.70] the machine learning over it?
[3337.24 → 3340.76] And then I suppose the other thing to majorly encourage is to check out our blog.
[3341.14 → 3343.16] So that's blog.grackle.ai.
[3343.74 → 3348.98] So we have a lot of stuff there that will give people an idea and give them a flavour of what
[3348.98 → 3353.26] you can achieve with the knowledge graph and how succinct it could be to get you motivated
[3353.26 → 3355.60] to actually move your data over and give it a try.
[3355.60 → 3361.28] Well, James, thank you very, very much for coming on the show and just kind of schooling
[3361.28 → 3361.98] us in all this.
[3362.08 → 3364.52] It's been really fascinating, and we appreciate it.
[3364.64 → 3366.78] So thank you, and we'll talk to you soon.
[3367.46 → 3369.68] Thank you very much for having me, both of you.
[3371.98 → 3372.40] All right.
[3372.46 → 3375.06] Thank you for tuning into this episode of Practical AI.
[3375.32 → 3379.26] If you enjoyed the show, do us a favour, go on iTunes, give us a rating, go in your podcast
[3379.26 → 3380.44] app and favourite it.
[3380.56 → 3384.00] If you are on Twitter or social network, share a link with a friend, whatever you got to do,
[3384.00 → 3385.70] share the show with a friend if you enjoyed it.
[3386.00 → 3388.66] And bandwidth for Changelog is provided by Vastly.
[3388.78 → 3390.22] Learn more at Fastly.com.
[3390.40 → 3393.60] And we catch our errors before our users do here at Changelog because of Rollbar.
[3393.82 → 3396.22] Check them out at Rollbar.com slash Changelog.
[3396.34 → 3399.02] And we're hosted on Linde cloud servers.
[3399.38 → 3400.98] Head to Linode.com slash Changelog.
[3401.08 → 3401.54] Check them out.
[3401.62 → 3402.44] Support this show.
[3402.82 → 3406.06] This episode is hosted by Daniel Whiten ack and Chris Benson.
[3406.48 → 3408.54] The music is by Break master Cylinder.
[3408.94 → 3412.38] And you can find more shows just like this at ChangeLog.com.
[3412.38 → 3416.58] When you go there, pop in your email address, get our weekly email, keeping you up to date
[3416.58 → 3420.82] with the news and podcasts for developers in your inbox every single week.
[3421.08 → 3422.00] Thanks for tuning in.
[3422.16 → 3422.88] We'll see you next week.
