[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.04 --> 36.08]  Learn more at fly.io.
[43.56 --> 47.44]  Well, welcome to a very special episode.
[47.86 --> 53.54]  I'll say this is an episode of a podcast, actually of two podcasts, Chris.
[53.54 --> 58.94]  This is a different kind of episode than we normally do because we're privileged to be
[58.94 --> 64.88]  joined by Dimitrios and Mikhail from the ML Ops Community Podcast.
[65.46 --> 66.10]  Welcome, guys.
[66.44 --> 69.58]  Yeah, we're hiding over here in the shadows.
[70.04 --> 71.36]  In the ML Ops Community.
[71.54 --> 73.42]  The shadows of the ML Ops Community.
[74.60 --> 76.80]  We don't really have a guest this week.
[76.86 --> 78.06]  We have four hosts.
[78.16 --> 78.72]  That's what we have.
[79.94 --> 81.28]  This will be interesting.
[81.28 --> 83.26]  It's a lot of chefs in the kitchen right now.
[83.46 --> 84.26]  Yeah, that's right.
[84.54 --> 87.30]  Which is obviously what listeners want more of.
[90.04 --> 92.98]  We're just going to answer each question with more questions.
[93.56 --> 96.68]  I don't know if we have the hosts with the most, but we have the most hosts.
[97.20 --> 98.04]  There we go.
[98.16 --> 98.68]  There we go.
[98.82 --> 99.28]  There we go.
[99.92 --> 102.62]  The real question is who's going to ask the first question?
[102.62 --> 105.84]  Oh, I was going for it, but now you can.
[106.00 --> 107.96]  But technically, that was a question.
[108.20 --> 108.88]  I'm not sure.
[109.28 --> 112.82]  So maybe I'll answer your first question with my first question.
[113.68 --> 115.56]  ML Ops and Community.
[115.72 --> 119.40]  I love everything you all are doing with the community over there.
[119.48 --> 125.50]  Of course, the podcast, which we'll link to, and the meetups and the content that you're
[125.50 --> 126.10]  putting out there.
[126.10 --> 133.78]  My sort of basic question, though, is we have heard ML Ops however many times on this podcast,
[133.90 --> 134.64]  Practical AI.
[135.54 --> 141.20]  And we've heard even conflicting statements about what that even is.
[141.46 --> 144.32]  So you're branded the ML Ops community.
[144.72 --> 147.38]  So from your perspective, what does that mean?
[147.60 --> 148.64]  Who's in the community?
[148.80 --> 149.72]  How is it defined?
[150.04 --> 151.12]  All that stuff.
[151.12 --> 156.78]  So at a really high level, ML Ops, it's an abbreviation of machine learning and operations.
[157.46 --> 162.74]  And one really quick, easier way to think about what ML Ops does, it's fundamental about
[162.74 --> 167.50]  the question of how do we take machine learning that you typically see in research and deliver
[167.50 --> 168.94]  that in the real world.
[169.48 --> 174.58]  So until relatively recently, I want to say the last few years, machine learning was starting
[174.58 --> 175.18]  to get really hot.
[175.64 --> 180.72]  Maybe it really kicked off in 2012, 2013, right, is when we had this resurgence of deep learning
[180.72 --> 181.94]  that really picked up.
[182.04 --> 186.80]  And people got excited about image recognition systems, speech, you know, ASR systems.
[187.48 --> 191.48]  And for a long period of time, a lot of machine learning, even cutting edge machine learning
[191.48 --> 195.42]  still happened in the lab, right, in the research lab, either at big institutions or even just
[195.42 --> 196.70]  at actual academic institutions.
[197.48 --> 201.26]  And so it was around, you know, I want to say around the time that TensorFlow came out,
[201.58 --> 205.64]  when we started really getting this effort to standardize the processes of going from something
[205.64 --> 210.60]  that you see in like research, new models, new AI systems, and try to actually
[210.60 --> 211.90]  put it out in front of people, right?
[211.92 --> 214.98]  How do we get these systems to the point where they can start delivering real value to real
[214.98 --> 215.32]  people?
[216.18 --> 221.24]  And MLOps is pretty much a set of frameworks and tools and systems that people have developed
[221.24 --> 226.66]  that are based a lot in software engineering, as well as DevOps, to make that translation
[226.66 --> 230.24]  process from research into production much easier.
[230.70 --> 235.24]  And so it's really just a set of like principles and techniques and tools that a lot of the communities
[235.24 --> 238.48]  developed to make that translation possible.
[238.48 --> 245.14]  Yeah, I think around the time, like we started this, Chris, I think one of our feelings was,
[245.20 --> 250.96]  and now we're, you know, a good ways in, but I still feel this way that like, it's not an
[250.96 --> 256.64]  easy leap to sort of just start learning like, oh, I'm going to do the fast AI course or something.
[256.64 --> 264.16]  And then like, okay, let's say you get a position as a data scientist or like whatever the title is,
[264.64 --> 271.46]  like, okay, whatever is happening, like in that position, like there are overlaps between what
[271.46 --> 275.42]  you learned in like a fast AI or whatever, like certainly that's like wonderful stuff.
[275.42 --> 283.56]  But like, it is only like a very small component of a larger, like system of like practicalities that
[283.56 --> 286.34]  are not that easy to access and learn about.
[287.02 --> 287.10]  Totally.
[287.32 --> 293.84]  And they're still trying to standardize like the other pieces, depending on your use case,
[294.08 --> 296.72]  MLOps might be one thing or another thing to you.
[296.80 --> 300.12]  It's really not super clear right now.
[300.20 --> 303.56]  Like if you're using deep learning, that's one type of MLOps that you're doing.
[303.56 --> 309.24]  And if you're doing a recommender system and you like to play in the trees and the decision
[309.24 --> 313.62]  trees, those random forests, then it's a different type of MLOps that you're doing.
[313.92 --> 319.12]  So like, I think we should dive as we go here, we should dive into the weeds on what those are.
[319.32 --> 324.52]  But I actually want to throw a hand grenade into the conversation and say like,
[324.52 --> 330.82]  DevOps or DevSecOps, depending on where you're coming from, you know, and like the differences
[330.82 --> 332.90]  and MLOps, how does it integrate?
[333.08 --> 334.22]  Is it some of the same?
[334.60 --> 338.64]  This is the show where we can clarify all of these things between us here.
[338.94 --> 340.42]  We should just dive in.
[340.74 --> 342.80]  By DevOps, do you mean a Docker, Chris?
[342.98 --> 343.54]  Oh, yeah.
[345.84 --> 347.96]  What do you mean by DevOps?
[348.18 --> 349.56]  Something you put in the container?
[349.86 --> 353.36]  Well, once again, I mean, I don't want to put my definition.
[353.72 --> 357.60]  These are the things that have Ops at the end that everyone is talking about.
[357.60 --> 362.90]  Now, if you are out there in the world and you're doing models of various types, it might
[362.90 --> 365.74]  be deep learning, might not be deep learning, you know, Dimitri's those points.
[366.30 --> 368.66]  But, you know, it also integrates in with software.
[368.98 --> 372.22]  And so where does one stop and the other start?
[372.44 --> 376.44]  You know, if we can start sorting through what we think these things are, I think that
[376.44 --> 381.64]  would be useful because you put a bunch of data scientists and software people in a room
[381.64 --> 386.04]  and they still today don't necessarily know what each other means when they're having these
[386.04 --> 386.56]  conversations.
[386.56 --> 392.92]  I aired a bit of my dirty laundry and my pet peeve of like people saying a Docker or
[392.92 --> 393.60]  Dockers.
[394.14 --> 395.22]  I deployed a Docker.
[395.78 --> 400.56]  But yeah, I think that's like the minds that you hit when you put a software engineer and
[400.56 --> 401.88]  a data scientist together.
[402.12 --> 406.18]  I think it touches on a really astute point, which is that the definitions are a little
[406.18 --> 406.58]  fuzzy.
[407.12 --> 411.46]  They are, to be perfectly honest, they're very fuzzy in terms of where does the domain
[411.46 --> 413.12]  of one begin and the domain of another?
[413.26 --> 414.70]  Like, how do we cross these territories?
[414.70 --> 415.82]  Where are the fiefdoms?
[415.98 --> 417.46]  Where are the boundaries set up?
[418.06 --> 423.04]  And fundamentally, like, MLOps has been and is a very interdisciplinary field.
[423.46 --> 427.86]  And so maybe one of the easiest visuals that we like to sort of discuss when we try and
[427.86 --> 433.02]  explain what MLOps is, is like imagine like a three-circle Venn diagram where one is data
[433.02 --> 436.44]  science, the other is software engineering, and the third is DevOps.
[436.44 --> 442.06]  And MLOps sits kind of squarely right in that little intersection area of those three circles.
[442.50 --> 447.50]  Because a lot of the stuff that makes MLOps and the way people use it does touch on pretty
[447.50 --> 449.20]  much every single one of those three circles.
[449.52 --> 450.68]  There's modeling, right?
[450.76 --> 453.10]  There's fundamentally you're building models, you're training systems.
[453.50 --> 456.42]  You have these data concerns that really falls out of the data science category.
[456.80 --> 457.88]  You have software engineering, right?
[457.88 --> 461.40]  Because you're trying to actually build out good systems that have to be engineered.
[461.56 --> 462.38]  You have to write code.
[462.38 --> 465.36]  It has to be well-tested, unit-tested code.
[465.82 --> 469.46]  And then the DevOps is really about how do you streamline that process of going, you know,
[469.50 --> 472.76]  doing this once, putting it in a Docker, and then doing it multiple times.
[472.90 --> 476.44]  And then just repeating that over and over and over and doing it systematically so that,
[476.54 --> 481.84]  hey, I have 100% ideally uptime on the machine learning systems I put out into production.
[482.38 --> 483.68]  And that's really the DevOps component.
[483.84 --> 486.68]  And so really it borrows a little bit from every single one of those circles.
[487.00 --> 488.18]  I see what you did there.
[488.18 --> 494.46]  And just shout out to Docker Compose because you can do so much with that.
[494.86 --> 501.54]  Let's just not forget the unsung hero of this whole thing and give a huge shout out to Docker Compose.
[501.68 --> 502.90]  Or the Bash script.
[503.56 --> 504.68]  Or the Bash script.
[505.02 --> 507.28]  The true OG hero.
[508.42 --> 509.64]  Yeah, exactly.
[509.84 --> 511.92]  The unsung hero in reality.
[511.92 --> 524.36]  But there's, you know, like Michael was saying too, I think that it's not only one person that should be tasked with this ML Ops title.
[524.92 --> 535.66]  And a lot of times you can get yourself into a lot of trouble if you're trying to build out something that is going to productionize your machine learning.
[535.66 --> 539.72]  And you expect your data scientist to be able to do everything.
[540.10 --> 547.86]  Or you have a very like naive sense of what it takes to actually productionize machine learning.
[548.08 --> 554.94]  And not just like productionize it in a way where you get a model out, but really make a process out of it.
[554.94 --> 563.96]  And I really enjoy an idea which is ML Ops is not just putting a model out there once.
[564.16 --> 567.36]  It's the act of N plus one.
[568.16 --> 574.66]  So ML Ops is a machine learning model in production, but not just one, N plus one.
[574.86 --> 579.18]  And that's when you get into how are the processes around this?
[579.22 --> 583.88]  And what do we really need to be thinking of when we're productionizing our machine learning?
[583.88 --> 587.06]  I have a question for you just straight off of that.
[587.56 --> 597.60]  Can you talk about like when you're talking about getting that out in that N plus one model, how is ML Ops in that capacity like kind of late in the process there?
[597.76 --> 606.26]  As you're kind of getting it out into wherever your environment, the cloud or wherever it is that you're putting the model, where does that differ from the DevOps world?
[606.50 --> 613.86]  Because it's easier to see it at the front end because you're kind of starting with two different things that you're trying to put out there in the world, you know?
[613.88 --> 617.12]  In one case, you're starting by training a model of some type.
[617.50 --> 619.76]  In the other case, you're working on software and all that.
[620.02 --> 622.12]  And you're, you know, you say, OK, we're ready to go.
[622.52 --> 627.14]  But somewhere down those pipelines, they start looking very similar in a lot of ways.
[627.66 --> 628.74]  How do you look at that?
[628.82 --> 630.60]  How do you differentiate what those are?
[631.20 --> 631.88]  Do they merge?
[631.98 --> 632.72]  Do they not merge?
[632.80 --> 633.34]  How do you see it?
[633.82 --> 638.08]  So it's the fun one that we talk about a lot in the ML Ops community, right?
[638.08 --> 640.24]  Like, isn't ML Ops just DevOps?
[640.74 --> 648.70]  And the dirty secret, I think, is that, yes, it is just DevOps, but then you sprinkle a little bit of data on it.
[649.04 --> 651.18]  And so magically, it's not DevOps.
[651.50 --> 655.74]  And I think Mikhail can really like add a lot of great insight to this.
[655.74 --> 659.56]  But we were just talking about this probably like a few hours ago when we met.
[660.10 --> 671.18]  And it was very much like ML Ops is more about software engineering than it is about the modeling piece, I think.
[671.44 --> 682.74]  Like, it's much easier for someone who knows about software engineering to get into ML Ops than it is for like a machine learning researcher to get into ML Ops.
[682.74 --> 686.60]  And that's what I think we've seen over the years.
[686.60 --> 699.64]  And we really have recognized in the past couple of years that there's been a very clear engineering discipline that comes with ML Ops as opposed to in the beginning.
[699.64 --> 701.28]  It wasn't so clear.
[701.38 --> 703.56]  It was like, oh, data scientists should be doing this.
[703.72 --> 709.86]  And now it's a little bit like, hmm, maybe it's not the easiest thing in the world to teach data scientists how to code.
[709.86 --> 711.90]  You know, it's funny that you say that.
[712.08 --> 713.34]  And I'll leave the company unnamed.
[713.48 --> 717.00]  But a few years ago, I worked at a different place.
[717.94 --> 720.68]  And I had a team for a first AI team.
[720.72 --> 722.16]  And I had a team of data scientists.
[722.54 --> 726.94]  And I was like the only one to come from kind of a software development background.
[727.16 --> 730.26]  And everybody else was kind of straight data science.
[730.90 --> 732.44]  And that was what we found.
[732.54 --> 738.78]  It was a struggle a little bit to try to figure out how to create that ML Ops line.
[738.78 --> 746.12]  And I was like, there's an entire engineering skill set that I think people come into it without realizing it up front.
[746.26 --> 752.06]  I think it's like an insight that they have that you just stated that takes them a little while to realize that.
[752.60 --> 761.52]  And the interesting thing is when we look at how ML Ops, the evolution of ML Ops over the last few years, because it seems to have been born a little bit in the wrong way,
[761.52 --> 765.74]  in that data scientists started learning these principles and these software engineering practices.
[766.44 --> 769.30]  So we had these data scientists that are like, oh, yeah, unit testing for data.
[769.38 --> 770.14]  That's super novel.
[770.62 --> 777.36]  And then the moment you had any person that came from DevOps or traditional software engineering start entering these conversations, they're like, what are you guys talking about?
[777.44 --> 779.02]  This has been a thing for decades.
[779.36 --> 781.00]  What do you mean testing your model code?
[781.06 --> 783.66]  What do you mean testing different parts of your software engineering stack?
[783.80 --> 785.46]  What do you mean using a Docker?
[785.46 --> 791.00]  Like, what do you mean by making it seem like this is some profound insight you guys have really found?
[791.82 --> 796.44]  And yeah, in a way there was, I don't want to say there was tension, but there was definitely like a WTF.
[796.56 --> 797.38]  What are you guys talking about?
[797.48 --> 800.62]  Like, this is not as special as you guys make it seem.
[801.16 --> 803.30]  Yeah, you have the different sides of the spectrum, right?
[803.56 --> 809.14]  Where coming at it from this engineering point and they're like, this is just DevOps.
[809.14 --> 821.38]  And then you have the data scientists coming at it from the opposite end of the spectrum where they're saying, like, wow, this is so much different than anything that's ever been out there before.
[821.66 --> 825.36]  And so we need to build a whole new discipline around it.
[825.94 --> 826.04]  Yeah.
[826.16 --> 833.96]  Also, I think that the part of the confusion is, like, just like everything else, like labeling and naming.
[833.96 --> 839.36]  Like some of, I think there's been data scientists and researchers over time that are like, yeah, this sounds great.
[839.46 --> 842.76]  Like machine learning plus ops.
[843.08 --> 847.08]  And what that ends up being is experiment tracking, right?
[847.18 --> 856.16]  Which actually is something that also is not new because, like, people have been doing this in high performance computing for, like, decades and decades, right?
[856.16 --> 864.36]  But this sort of solution around, like, let's say weights and biases, ClearML, like, I love these tools.
[864.50 --> 865.52]  We use ClearML.
[866.22 --> 880.08]  Like, the value I get out of that is experimenting at scale, tracking experiments, making sure I know, like, what assets are what, like, maybe logging data sets and, like, input, output, all of that stuff.
[880.16 --> 884.46]  But that's all, like, experiment tracking and production of the model.
[884.46 --> 889.70]  I sort of tend to think about ML Ops as, like, everything after that, right?
[889.78 --> 890.74]  Like, you have a model.
[890.84 --> 891.48]  That's all great.
[891.62 --> 900.92]  Like, whatever happened before, even if you want, like, lineage about what data was input to your training, which output, what model, like, that's all tracked.
[901.02 --> 901.52]  That's great.
[901.52 --> 918.68]  There's still some huge hurdles to get over in terms of, like, this model being called from within a software application that has, like, real users on the other end and, like, all of the potential implications around that.
[918.68 --> 923.58]  So, in my mind, that sort of distinction is really confusing for people.
[923.70 --> 929.22]  And I don't know, maybe you can comment on this because it's maybe something that's come up on your podcast.
[929.32 --> 929.88]  I'm not sure.
[930.36 --> 937.04]  Have you also seen that confusion of, like, ops versus experiment tracking?
[937.04 --> 948.00]  And the fact that a lot of data scientists might think they're, it's, like, I think that word that you're saying doesn't mean what you think it means or, like, whatever.
[948.72 --> 950.10]  Little princess bride in there.
[950.24 --> 951.14]  Yeah, exactly.
[951.50 --> 952.84]  I think that word doesn't.
[952.84 --> 955.62]  That's so classic.
[955.74 --> 963.18]  It reminds me of the meme, too, where you have the little girl who's standing in front of the burning house.
[963.70 --> 966.76]  And it's, like, worked fine in my Jupyter notebook.
[967.02 --> 968.46]  It's an ops problem now.
[969.40 --> 970.86]  I love Jupyter and all that.
[970.86 --> 980.40]  But when I, like, when someone told me there was, like, an export to Python script function in Jupyter notebooks, like, it absolutely frightened me to, like, no end.
[980.40 --> 982.78]  Like, I'm, like, why does this feature exist?
[982.92 --> 986.54]  This is, like, I guess I understand, like, where it could have come from.
[986.64 --> 999.94]  But it just, like, frightens me that maybe it's the evidence of, like, you know, the disconnect between, oh, I wrote some code and did this thing between that and, like, software development and integration.
[1000.30 --> 1002.86]  I think it's evidence of that gap for sure.
[1003.16 --> 1008.72]  I've kind of been perusing your goods on your podcast, which is awesome.
[1008.72 --> 1014.14]  You know, various inflammatory titles such as Airflow Sucks for ML Ops.
[1014.68 --> 1016.40]  We learned from you guys, though.
[1016.50 --> 1028.50]  Let me just tell you that I learned from you on the title or the naming conventions when Luis was on and it was, like, ML Ops doesn't exist or something like that or ML Ops is a lie.
[1028.82 --> 1029.24]  Oh, yeah.
[1029.72 --> 1032.34]  I was, like, these guys went and did it.
[1032.42 --> 1032.98]  Oh, man.
[1032.98 --> 1034.44]  And, like, my lifeblood.
[1036.10 --> 1041.22]  It's amazing that we went from that title to having the ML Ops community on the podcast.
[1041.22 --> 1047.60]  Yeah, that's why, yeah, I knew we needed to have a conversation because it was, like, all right, I like it.
[1047.68 --> 1055.70]  And I think most people that if anyone knows me, they know that the most critical of ML Ops is myself.
[1055.70 --> 1057.50]  And I feel like I kind of have to be.
[1057.50 --> 1061.40]  And that's why I love when Luis says that kind of stuff.
[1061.52 --> 1070.10]  And we went and we grilled him hard when he came on our podcast, too, because it was very much like, okay, what do you mean by that?
[1070.10 --> 1071.26]  And why is that?
[1071.26 --> 1081.94]  And I'm very much trying to see at every juncture what is going on with ML Ops and is there something new?
[1082.00 --> 1087.02]  Like, my new favorite thing to ask people is, is ML Ops going to get Hadooped?
[1087.02 --> 1100.96]  And that is, like, with chat GPT or with foundational models, is ML Ops going to become obsolete or it's going to become something that old legacy companies use?
[1101.24 --> 1110.02]  And so that's my big question right now and what I love thinking about and those thought exercises that are going through my head.
[1110.02 --> 1115.80]  And so I almost feel like the pressure of needing to do that.
[1115.80 --> 1123.48]  By the way, you realize that there's a very, very current version of Hadooped, you know, that a certain large company has a big fear of.
[1123.68 --> 1127.62]  Right now, I think the big fear is instead of Hadooped, would it be Googled?
[1128.06 --> 1128.34]  Yeah.
[1128.58 --> 1129.78]  Because of chat GPT.
[1130.30 --> 1137.18]  You know, you've seen all the stuff in the last few days about, you know, is the search algorithm going to be gone?
[1137.48 --> 1138.44]  Is it done for?
[1138.52 --> 1138.92]  Is it done for?
[1139.46 --> 1142.14]  I've got a bit of a contrarian stance on that.
[1142.22 --> 1143.06]  Okay, go for it.
[1143.06 --> 1150.44]  When I see that coming up a lot, I'm just kind of like, there's no way it's going to be replaced.
[1150.44 --> 1160.24]  Because first of all, I said it once and I'll say it again on this podcast, like my New Year's resolution was to be as confident as chat GPT.
[1160.34 --> 1161.42]  I saw that.
[1161.62 --> 1162.48]  I saw that.
[1162.48 --> 1168.44]  Because let's be honest, like it's the amount of bullshit that it spews out is incredible.
[1169.32 --> 1175.20]  I want that kind of confidence when I'm spewing bullshit at people, you know, like give me that, please.
[1175.20 --> 1179.20]  And so that's the first thing, like you don't know if you can trust it.
[1179.26 --> 1182.64]  But the other thing is, there's a lot of stuff on there.
[1182.72 --> 1185.60]  Like I just see them as two completely separate uses.
[1185.94 --> 1189.84]  And it's going to definitely take parts of what you would Google.
[1189.84 --> 1198.34]  And that is for a good cause because a lot of the stuff that you do Google right now, it seems like the user experience isn't that good.
[1198.42 --> 1202.24]  And so I would like to have a better experience when I'm doing that.
[1202.30 --> 1210.32]  Like, for example, if I just want to know the recipe of whatever my favorite vegan bean burger, I can ask chat GPT.
[1210.32 --> 1217.32]  I don't have to get like this verbose, fully SEO optimized with a ton of ads and pop ups and everything.
[1217.60 --> 1219.06]  That user experience is horrible.
[1219.26 --> 1221.90]  And so please, like, don't make me have to go through that.
[1222.18 --> 1224.56]  But I'm feeling some bro love here, by the way, as a vegan.
[1224.68 --> 1226.44]  I'm just saying thank you for using that example.
[1226.82 --> 1227.12]  All right.
[1227.14 --> 1227.68]  There we go.
[1227.96 --> 1228.58]  There we go.
[1228.70 --> 1229.00]  Nice.
[1229.42 --> 1236.58]  But yeah, then there's going to be a lot of other use cases where it just isn't the right medium, in my opinion.
[1236.86 --> 1239.36]  I don't know about you all, but that's my take on it.
[1239.36 --> 1242.66]  Just bringing it back to the ops perspective here.
[1242.76 --> 1261.58]  It's this weird, like, because even with like fine tuned or like transfer learned models where you have this like foundation model type of workflow, generally up until recently, the thought process was, okay, well, I'm still performing a task.
[1261.58 --> 1266.28]  And that task, like I can generate like a table of tests for that task, right?
[1266.28 --> 1272.44]  And like minimum functionality, I can put that as part of like my automation for when I release this model.
[1272.64 --> 1278.42]  Like however you do that, whether that's like, you know, whatever ML Ops tools you want to use for that.
[1278.42 --> 1294.46]  And now you've sort of got this, like everybody's thinking about these generative models and like, okay, well, if I'm completely open domain, how do I mitigate risk in those situations with these sort of open domain models?
[1294.46 --> 1298.14]  And I think there's, so I think there are ways.
[1298.76 --> 1307.86]  And I think that some of the same workflows will apply, but I do think it does kind of tweak your mindset a little bit to think about some of these things.
[1307.94 --> 1314.80]  I don't know if that's, that's something that you all have been thinking about with the kind of most recent wave of like generative models.
[1314.80 --> 1320.90]  It's interesting because they do change the paradigm quite a bit in a lot of ways.
[1321.10 --> 1328.82]  There was a hackathon, so I'm based in the Bay Area, and there was a hackathon when it was like last week hosted by Scale where people were just hacking on different things related to AI.
[1329.06 --> 1332.70]  But a lot of them naturally because gen AI, generative AI is a hot thing to do.
[1333.06 --> 1335.92]  There were a lot of applications built around generative AI use cases.
[1335.92 --> 1342.30]  And one of them was actually someone tried to basically build an entire backend using nothing but LLM calls.
[1342.50 --> 1348.44]  Like they were basically just making calls and updating literally data structures in the backend fully using generative models.
[1349.06 --> 1350.72]  Naturally, this wasn't like amazing, right?
[1350.80 --> 1359.38]  I mean, in a sense, it was a little bit hacky to try and update dictionaries or, you know, like literally objects via these API calls using things like codecs and whatnot.
[1359.38 --> 1365.00]  But it does force you to ask this question of like, well, okay, now it's maybe not great.
[1365.10 --> 1366.12]  Maybe now it's a little bit brittle.
[1366.32 --> 1367.84]  But we see this out.
[1367.98 --> 1371.16]  Like let's, you know, imagine for a second what 10 years from now looks like.
[1371.20 --> 1373.84]  I mean, the 60s computers took an entire room, right?
[1373.92 --> 1375.72]  And there was only IBM that had them.
[1375.82 --> 1379.52]  But here we are with them like literally on my wrist, you know, or in my pocket.
[1379.64 --> 1385.62]  And so it's not unreasonable to expect that like some of the ways we even do some of these workflows are going to be touched by this, right?
[1385.62 --> 1388.68]  It's going to change how we operate with our software engineering systems.
[1388.68 --> 1390.74]  And by extension, by our machine learning systems.
[1391.26 --> 1398.76]  I mean, what can be done away with once we have the only interaction being like language to language style, you know, kind of translations?
[1399.40 --> 1414.36]  I also wonder if there's like a meta layer here where like part of the question is how do we test and like set up the ops around large language models and generative models?
[1414.62 --> 1416.50]  I think that's one question that can be asked.
[1416.50 --> 1418.56]  And are those the same or are they different?
[1418.68 --> 1420.54]  This is one of the I was going to ask that anyway.
[1420.80 --> 1421.84]  How do they relate?
[1421.92 --> 1423.04]  How are they not the same?
[1423.80 --> 1423.96]  Sure.
[1424.06 --> 1426.60]  And how can one feed into the other?
[1426.70 --> 1426.92]  Right.
[1426.92 --> 1436.40]  Like what you were talking about just now, Mikhail, is that there's this idea of like how could generative models help me with my ML ops, right?
[1436.74 --> 1447.42]  Like let's say I'm trying to put a model into production and I'm trying to test that well or like I'm like searching through logs and other things and trying to parse that out.
[1447.42 --> 1456.32]  Like if I can ask an agent to like help me do some of those things, which to be honest are fairly predictable if I've seen them before.
[1456.92 --> 1457.94]  Yeah, it's very meta.
[1458.16 --> 1458.40]  I know.
[1458.56 --> 1461.68]  But there's like the one side, like how do I put these things into production?
[1461.68 --> 1465.26]  And as you say, Chris, like are there differences with that?
[1465.40 --> 1474.50]  And the second place, like, well, could I actually like bring those around the other side and help them do my have those models help me do my ML ops tasks?
[1474.68 --> 1474.82]  Right.
[1474.82 --> 1478.66]  So I am 100% in the same boat as you.
[1478.84 --> 1482.32]  I know the CEO of you.com.
[1482.56 --> 1489.12]  He posted on Twitter like what is the best use of a large language model in your mind?
[1489.48 --> 1493.74]  Of course, I instantly thought like YAML fluency.
[1494.30 --> 1494.86]  Oh, man.
[1495.84 --> 1499.08]  That would be incredible if it could do that.
[1499.08 --> 1507.92]  Like, let's just be honest, how much time would it save if it could just go and set up my Kubernetes cluster for me?
[1508.12 --> 1511.86]  And I've talked to a lot of smart people about that.
[1511.92 --> 1516.68]  And I think a lot of people are like, no, that's not going to happen.
[1516.74 --> 1518.10]  Like that's too far.
[1518.22 --> 1524.92]  But I also am a little bit like, yeah, well, there's a lot of other stuff that we thought wasn't going to happen and it's happening right now.
[1525.08 --> 1526.82]  So I don't think that's too far.
[1526.82 --> 1528.66]  Like that is my pain point.
[1528.66 --> 1532.28]  Like we are this far into Kubernetes and that still hurts.
[1532.56 --> 1536.48]  Like if you're not just using someone else's implementation, you're going to set up your own cluster.
[1536.80 --> 1537.92]  It's still painful.
[1538.18 --> 1541.42]  And like that this is known stuff.
[1541.44 --> 1542.78]  It's just a pain in the butt.
[1543.12 --> 1544.82]  That's a great thing, right?
[1544.90 --> 1546.10]  I don't think that's too far at all.
[1546.14 --> 1546.94]  And I want it now.
[1547.36 --> 1547.88]  Yeah, exactly.
[1548.00 --> 1550.32]  Maybe it's just like a fine tune away.
[1550.52 --> 1551.16]  Let's be honest.
[1551.28 --> 1552.38]  Maybe that's all it is.
[1552.42 --> 1553.88]  And somebody needs to think about that.
[1553.88 --> 1556.36]  I'm sure I'm not the only one that has thought about that.
[1556.36 --> 1560.60]  But I'll let Mr. Eric chime in too.
[1560.70 --> 1562.56]  I know he has some strong thoughts.
[1562.78 --> 1576.12]  And I'll preempt his thoughts on this with his idea of an incredible app on top of generative models was stealing somebody else's IP.
[1576.12 --> 1579.30]  You want to tell us about what you've created, Mr. Eric?
[1579.66 --> 1580.68]  Oh, that sounds perfect.
[1581.08 --> 1586.52]  And by the way, just disclaimer, I'm not implicating myself in any of the following conversation.
[1589.16 --> 1590.86]  This is not hacking advice.
[1591.44 --> 1592.16]  Oh, goodness.
[1592.38 --> 1593.82]  This show just took a turn.
[1594.56 --> 1595.42]  Oh, boy.
[1595.94 --> 1601.56]  I didn't realize I was going to be basically implicating myself criminally by coming on this podcast.
[1601.66 --> 1602.90]  But we're going to edit this out, right?
[1602.96 --> 1603.86]  This is edited out.
[1603.86 --> 1605.14]  Sure, sure.
[1605.22 --> 1606.22]  We'll say that now.
[1606.42 --> 1608.48]  But we didn't sign a contract of any type.
[1608.94 --> 1611.92]  And there are no intelligence agencies listening, I promise.
[1612.52 --> 1613.22]  Absolutely not.
[1613.34 --> 1613.48]  Right.
[1614.00 --> 1614.84]  Absolutely not.
[1615.40 --> 1615.62]  Yeah.
[1615.78 --> 1623.06]  I mean, I guess I'll maybe spend a little bit of time talking about the use case that I think Demetrius is referring to, which is a little bit of a toy use case.
[1623.40 --> 1626.38]  We didn't do it because we were trying to get sued.
[1626.50 --> 1627.34]  That wasn't the goal.
[1627.48 --> 1629.88]  But hopefully it should spur a little bit of creativity.
[1630.20 --> 1630.80]  What a start.
[1630.80 --> 1631.32]  Sure.
[1633.88 --> 1634.64]  Well, okay.
[1634.70 --> 1634.98]  Maybe.
[1635.04 --> 1636.82]  Maybe like 10% we were trying to get sued.
[1637.32 --> 1637.48]  No.
[1637.76 --> 1647.72]  The use case, to give an idea of what has become possible outside of, you know, yes, the really practical use cases, generating YAML, generating unit tests.
[1647.92 --> 1651.68]  I think these are all, on a very serious note, these are things that are going to be possible.
[1651.88 --> 1654.04]  I actually don't see this being as too far off.
[1654.12 --> 1655.44]  And I don't know, you know, not even like a decade out.
[1655.44 --> 1659.92]  And I see this being like the next few years, being able to spin off things like that is just going to be totally feasible.
[1660.40 --> 1663.56]  You know, this is like language-based kind of generation, generative modeling.
[1664.00 --> 1670.30]  The other one that we haven't really touched on as much, which is also really capturing people's interest, has been more of the image-based, right?
[1670.30 --> 1676.12]  Like vision-based, whether that's a single static image or that's an entire video or, you know, in some cases even audio.
[1676.26 --> 1678.56]  Just like different modalities besides pure text.
[1679.10 --> 1686.02]  And so one that has certainly become really interesting because of the rise of things like DALI from OpenAI and then stability, you know, stable diffusion.
[1686.02 --> 1693.58]  It has these incredible photorealistic images in different styles that you can just prompt with literally human text, right?
[1693.58 --> 1696.88]  Which has never been possible before, or at least not at this level of quality.
[1697.78 --> 1700.96]  And so one of the things that my co-founder and I actually...
[1700.96 --> 1701.54]  Here it comes.
[1702.02 --> 1707.40]  Yeah, that we were working on was this little toy application that we called Rick and Mortify.
[1707.40 --> 1712.12]  And the basic use case was we were big fans of the Rick and Morty TV show.
[1712.74 --> 1714.06]  And, you know, we love it.
[1714.12 --> 1716.90]  We think it's super, like, it's very great, great, great content.
[1717.28 --> 1720.08]  That did not stop a cease and desist letter from coming.
[1722.58 --> 1727.90]  There's a backstory here that I found out after we released the application, which if you guys are curious, I'll go into.
[1728.14 --> 1734.00]  But we were really trying to test this hypothesis of like, okay, you have these vision-based models that are incredible.
[1734.18 --> 1736.18]  You have these language-based models that are incredible.
[1736.18 --> 1741.30]  How can we, like, merge them to actually try and do something between, like, kind of at the intersection of them two?
[1741.36 --> 1745.38]  And so what we came up with was like, well, can we personalize episodes of Rick and Morty?
[1745.48 --> 1756.02]  Like, if I, as a super fan of the show, want to imagine a new episode, if I provided a premise, if I provided, you know, a set of characters that I wanted, maybe myself eventually.
[1756.18 --> 1758.38]  But let's just start with the basic characters that are in the show already.
[1758.54 --> 1763.34]  Rick, Morty, Summer, you know, Poopy Butthole, Mr. Meeseeks, like all these folks.
[1764.14 --> 1765.46]  That is an actual character name.
[1765.46 --> 1767.00]  I just want to point out for the audience.
[1767.16 --> 1769.14]  I did not just make up a name to try and be profane.
[1769.26 --> 1771.32]  That is a character, Mr. Poopy Butthole.
[1771.96 --> 1778.46]  And I'm not sure we've ever had that word on the show before, actually.
[1780.40 --> 1782.34]  I didn't know it was a word until the show.
[1782.54 --> 1783.98]  So, you know, we're both in this.
[1784.08 --> 1785.32]  We're all new to this game.
[1785.32 --> 1788.72]  What we essentially built out was you could come into this application.
[1788.94 --> 1791.60]  You could provide a premise of what you would like the episode to look like.
[1791.72 --> 1796.68]  So, Rick and Morty go to the Practical AI podcast and have a great conversation about generative AI.
[1797.08 --> 1798.02]  And then you pick your characters.
[1798.60 --> 1805.54]  And using a combination of vision-based generative systems, Stable Diffusion, DALI, and then the GPT-3s, right?
[1805.54 --> 1807.86]  You know, these kind of latest generation GPT models.
[1807.98 --> 1810.06]  We were able to generate not only the visuals.
[1810.42 --> 1813.78]  We were able to generate like a script of effectively a storyboard for a new episode.
[1814.60 --> 1815.78]  This is just like a first use case.
[1815.86 --> 1818.08]  Like, well, we're literally getting new episodes.
[1818.28 --> 1820.54]  You know, maybe there's like five, ten frames of this episode.
[1820.54 --> 1825.40]  But you're seeing some flavor of a plot with dialogue, with accompanying visuals.
[1825.56 --> 1826.94]  And, you know, sure, it's a little bit rough.
[1827.38 --> 1829.74]  But extend this out to the future, right?
[1829.78 --> 1830.68]  Like, what happens then?
[1830.74 --> 1833.20]  Like, this has become literally a fully-fledged episode.
[1834.34 --> 1835.80]  And that's where this could become, right?
[1835.84 --> 1837.88]  And so, no cease and desist yet.
[1838.22 --> 1839.34]  But people did play with it.
[1839.40 --> 1840.36]  People had a lot of fun with it.
[1840.40 --> 1841.50]  We're not making any money on it.
[1841.58 --> 1843.56]  So, you know, don't worry, Dan and Justin.
[1843.80 --> 1846.38]  Like, it's just for, it's Fan Art Friday.
[1846.38 --> 1848.76]  We're just trying to show our appreciation for the show.
[1848.76 --> 1850.54]  So, you raise something.
[1850.70 --> 1854.58]  It's kind of funny because when, just in day-to-day conversations about AI topics.
[1855.28 --> 1857.28]  And, like, new model comes out.
[1857.48 --> 1862.86]  And you see all the media stuff where people are just kind of bashing it and telling you all the problems with it and everything.
[1863.60 --> 1865.10]  And to your point, you just said this.
[1865.20 --> 1866.28]  That's why I bring it up.
[1866.66 --> 1869.84]  It's like, but think of what we can do with this tomorrow.
[1870.06 --> 1871.64]  Like, today we have this.
[1871.70 --> 1872.50]  And it's imperfect.
[1872.94 --> 1875.38]  And yesterday we didn't have any such thing.
[1875.84 --> 1876.58]  Think about it.
[1876.64 --> 1878.04]  If today we have the imperfect thing.
[1878.04 --> 1879.56]  Tomorrow's going to be pretty amazing.
[1880.14 --> 1884.92]  And to your point there, like, what you're doing there is, like, way out there.
[1885.06 --> 1887.08]  But it's not far from being very mainstream.
[1887.50 --> 1896.66]  So, my question about that is, like, you have the training data and you have the base show that a human made, right?
[1896.66 --> 1901.82]  And so, without that, like, I'm trying to extrapolate 10 years in the future.
[1901.82 --> 1910.28]  And if it's just going to be us remaking a bunch of shows that we made back when we used to do it all by hand.
[1910.34 --> 1914.44]  Or is it, like, that's kind of my question there, right?
[1914.44 --> 1916.66]  I think that's a generative function right there.
[1916.66 --> 1930.12]  I don't think that you have to start with where you were in the sense of part of that function at the very front end of that workflow is going to be generating different possibilities that are not directly linked to the training data.
[1930.22 --> 1931.68]  And then, like, carrying it from there.
[1931.88 --> 1933.80]  I think it's the future of entertainment.
[1933.80 --> 1946.56]  Hello, friends.
[1946.90 --> 1950.22]  This is Jared here to tell you about Changelog++.
[1950.92 --> 1958.40]  Over the years, many of our most diehard listeners have asked us for ways they can support our work here at Changelog.
[1958.58 --> 1961.12]  We didn't have an answer for them for a long time.
[1961.12 --> 1968.22]  But finally, we created Changelog++, a membership you can join to directly support our work.
[1968.54 --> 1979.44]  As a thank you, we save you some time with an ad-free feed, sprinkle in bonuses like extended episodes, and give you first access to the new stuff we dream up.
[1979.92 --> 1983.30]  Learn all about it at changelog.com slash plus plus.
[1983.52 --> 1986.86]  You'll also find the link in your chapter data and show notes.
[1987.24 --> 1990.50]  Once again, that's changelog.com slash plus plus.
[1990.50 --> 1991.36]  Check it out.
[1991.70 --> 1992.80]  We'd love to have you with us.
[2000.74 --> 2005.64]  What I think is kind of disconcerting is the right term.
[2006.02 --> 2014.34]  I don't know with the time scale on this or whatever, but, like, imagine, like, all these data sets around language models especially are scraped from the internet, right?
[2014.34 --> 2019.44]  And, like, a lot of these image data sets are scraped from the internet, right?
[2019.80 --> 2027.64]  So there's a proliferation of these models, and the internet is being filled with computer-generated content, right?
[2027.64 --> 2039.72]  So the next scraped versions of the internet, like, the next common crawl, the next whatever, like, what proportion of that data set is coming out of generative AI models?
[2039.72 --> 2047.16]  Now, I think there's interesting things going on, of course, with, like, detecting what is AI-generated and what isn't.
[2047.24 --> 2051.98]  I think I've seen, like, what OpenAI came out with for their own system.
[2052.18 --> 2056.16]  And, of course, like you say, Chris, everybody has, like, criticisms of that already.
[2056.16 --> 2067.78]  But there's, like, many other people exploring this as well, like GPT-0 and, like, other things that are exploring, like, how do we determine what is AI-generated and not?
[2068.42 --> 2075.44]  And so that's where, like, I don't know what the implications of that are for these large-scale data sets down the road.
[2075.44 --> 2085.76]  But that's sort of where my mind is going more so than, oh, should we be populating the internet with a lot of this generative art and other things, even if it's terrible?
[2086.16 --> 2088.18]  Well, I'm having a lot of fun with it right now.
[2088.44 --> 2090.90]  But there's sort of second-order effects, I guess.
[2091.38 --> 2092.56]  No worries then, man.
[2092.80 --> 2093.06]  Yeah.
[2093.58 --> 2095.30]  Well, I'll be dead by that time.
[2095.34 --> 2095.68]  I don't know.
[2095.74 --> 2095.94]  Maybe.
[2097.62 --> 2099.02]  No, no, no, no.
[2099.04 --> 2099.90]  This will be soon.
[2100.30 --> 2102.04]  It's a really interesting thought experiment.
[2102.04 --> 2105.42]  And, again, one that is closer than I think we believe.
[2105.90 --> 2111.18]  This idea of what happens when the bulk of these data sets are actually generated by systems.
[2111.48 --> 2115.92]  And I can see, you know, some positive effects and some that you would be like, okay,
[2115.92 --> 2117.26]  this might be a questionable downside.
[2117.74 --> 2121.40]  On the positive side, you know, these models, like the generative ones, especially the language
[2121.40 --> 2122.52]  variety, are, like, very good.
[2122.62 --> 2124.20]  I mean, grammatically correct, right?
[2124.22 --> 2127.16]  They're, like, very semantically good in terms of what they output.
[2127.40 --> 2130.82]  Does this mean that now the bulk of the data that's being trained on is just going to be,
[2130.94 --> 2134.70]  like, way higher quality writing than you would typically find in a typical Reddit post,
[2134.80 --> 2137.34]  right, or something just in the deepest corners of the web?
[2137.98 --> 2141.86]  And then now if you're training on data that's significantly better, you have this compounding effect of,
[2141.96 --> 2144.48]  like, well, now the data I'm training on is better, so the model is only going to get even better
[2144.48 --> 2147.72]  at writing of some kind, and then we mix it in with some other more diverse writing,
[2147.78 --> 2150.44]  and then it's going to continue to compound on itself in terms of quality.
[2150.94 --> 2155.80]  The downside, I mean, one, you could hypothesize is that, like, these models are only able to
[2155.80 --> 2157.98]  generate certain kinds of distributions of data, right?
[2158.02 --> 2160.22]  Only certain kinds of things they can write about or talk about.
[2160.34 --> 2164.74]  So now when you're just injecting all of these training sets with, like, a very skewed distribution
[2164.74 --> 2170.58]  of topics, of ideas on these topics, et cetera, how do you ensure that actually you're still
[2170.58 --> 2175.04]  giving your model enough of a versatility in what it sees, these next generations that are then trained
[2175.04 --> 2179.10]  on these data sets, to ensure that it's still a general purpose model, right?
[2179.16 --> 2183.20]  Like, what if 90% of the content that's put out there is just really bad marketing copy,
[2183.78 --> 2185.40]  you know, Facebook ads or something?
[2185.48 --> 2186.06]  You overfit.
[2186.46 --> 2189.84]  Yeah, it'll overfit exactly to that, and then what happens to these next generation systems,
[2189.92 --> 2191.36]  they actually might be hurt in the long run.
[2192.06 --> 2193.50]  Yeah, it's like we're in the golden era.
[2193.50 --> 2199.76]  Yeah, I think that you can have an MO ops community, in my opinion, for a long time,
[2199.76 --> 2204.16]  because there's such a wide variety of problems that people are still dealing with.
[2204.24 --> 2207.52]  So on this, like, very far end, we're talking about generative AI.
[2208.04 --> 2213.66]  Being part of, like, my day job as part of an international NGO, like, we're dealing with
[2213.66 --> 2218.60]  problems still, like, where, hey, there's no internet in this place, and, like, we're running
[2218.60 --> 2221.82]  our model on, like, an Android tablet or, like, whatever.
[2221.82 --> 2228.12]  Like, there's this range of, like, okay, what's the problem that happens when I scrape the
[2228.12 --> 2233.64]  whole internet again, all the way down to, like, how do I run this small model on an
[2233.64 --> 2234.40]  Android tablet?
[2234.68 --> 2238.62]  And I don't actually see that changing for some time.
[2238.74 --> 2244.24]  Yes, the world's, like, changing a lot, but there's still, like, such a wide variety of
[2244.24 --> 2250.54]  issues and, like, I think fun challenges to, like, wrestle with around this concept of,
[2250.54 --> 2254.20]  like, operations plus AI and machine learning.
[2254.72 --> 2259.68]  And so, yeah, it is sort of hard to define in that sort of way, but it's also really exciting
[2259.68 --> 2263.08]  because of the wide variety of things that you could be involved with.
[2263.22 --> 2270.52]  Like, as a DevOps person or software engineer or data scientist, like, there's plenty of problems
[2270.52 --> 2278.64]  that have to do with, like, running even, like, a much older language model on your phone and,
[2278.74 --> 2283.94]  like, other problems that have to do with, like, various different scales or different
[2283.94 --> 2286.08]  modalities of data, all these things.
[2286.42 --> 2286.86]  Yeah.
[2286.86 --> 2292.08]  And that goes back to kind of in the pre-show that our listeners were not there for.
[2292.16 --> 2294.94]  We kind of talked a little bit about that level of diversity.
[2295.58 --> 2297.44]  Like, how do you guys see that?
[2297.54 --> 2302.62]  So, I mean, Daniel, you've kind of talked about almost an extreme case of kind of edge
[2302.62 --> 2306.80]  concept, you know, being your target, you know, and having this slow Android thing.
[2306.80 --> 2312.68]  And yet we're used to being just, like, gluttonously resourced in the cloud, you know, everything
[2312.68 --> 2313.84]  you could possibly want there.
[2313.96 --> 2314.80]  Ramp it up, ramp it up.
[2314.84 --> 2316.02]  You've got all the stuff you want there.
[2316.16 --> 2318.64]  And you have this incredible diversity.
[2319.22 --> 2325.36]  So, for you guys thinking about ML Ops, you know, so much and how do you deal with that?
[2325.46 --> 2331.98]  Like, when you go from big company to one person struggling to work at all, how does ML Ops
[2331.98 --> 2336.40]  look when you're talking about diversity of use cases plus diversity of users?
[2336.40 --> 2339.36]  And that you're serving, how do you make it a thing?
[2339.64 --> 2340.98]  You know, how do you keep it all together there?
[2341.84 --> 2343.50]  A few answers to this question, actually.
[2343.62 --> 2348.44]  So, the first part of the diversity of use cases, and in a sense, we've gone a little
[2348.44 --> 2352.30]  bit backwards from something we said before, where on the one hand, we're like, oh, generative
[2352.30 --> 2354.08]  systems are just going to do it with all of this.
[2354.76 --> 2358.06]  And then now we're back at like, well, but it's, there's like enough stuff that we still
[2358.06 --> 2359.44]  need to solve that it'll probably be around.
[2359.92 --> 2360.26]  Both and.
[2360.58 --> 2361.68]  We're not quite there yet.
[2362.04 --> 2362.76]  Exactly, exactly.
[2362.76 --> 2367.96]  And to that point, I actually, I was actually asked this in a podcast once a few weeks ago,
[2367.96 --> 2371.32]  where I was asked, like, what do I believe will be the position, like the role that will
[2371.32 --> 2372.66]  exist 10 years from now?
[2372.76 --> 2376.00]  And I was asked, like, will it be like a data scientist, a prompt engineer, an ML Ops engineer,
[2376.08 --> 2377.10]  like, where would I put my money?
[2377.34 --> 2381.12]  And I still answered ML Ops engineer, like machine learning engineer, you know, like kind
[2381.12 --> 2382.34]  of in a similar category.
[2382.34 --> 2389.76]  Because I do believe that these same problems will persist, whether or not they're for old
[2389.76 --> 2393.78]  school decision tree based models, discriminative models that we use, you know, maybe five,
[2393.88 --> 2401.92]  10 years ago, even pre deep learning, or these new GPT 500, whatever will come later models,
[2402.08 --> 2403.84]  stable diffusion 10,000, you know what I mean?
[2403.90 --> 2405.30]  Like the same problems will persist.
[2405.44 --> 2407.06]  How do we, how do we operationalize it?
[2407.26 --> 2408.28]  How do we make it scalable?
[2408.62 --> 2411.30]  How do we keep uptime on models so that people interact with this?
[2411.30 --> 2414.82]  These are all questions that machine learning, you know, that ML Ops is fundamentally trying
[2414.82 --> 2416.30]  to solve and address.
[2416.62 --> 2423.36]  And whether or not you're using Kubernetes today, or some prompt engineering based Kubernetes
[2423.36 --> 2429.60]  tomorrow, or, you know, make it even more concrete, like airflow today versus like an airflow
[2429.60 --> 2434.02]  for prompt engineering, right, which is what people are actually developing today.
[2434.40 --> 2437.78]  The same sort of principles and the same concerns are going to apply.
[2438.48 --> 2440.72]  And so I don't see that going away anytime soon.
[2440.72 --> 2443.84]  And as long as there's a machine learning system, as long as, you know, we, I would assume all
[2443.84 --> 2447.42]  of us here in this room, in this virtual room, anyone who's listening here believes that AI
[2447.42 --> 2452.30]  is going to be the future, it's going to be here for decades, then the same questions
[2452.30 --> 2453.10]  will still have to apply.
[2453.92 --> 2457.82]  And so that's like the first part I want to just like throw out there is there's, ML Ops
[2457.82 --> 2462.50]  is here to stay, whether or not it's Kubernetes or whatever comes after Kubernetes, we hope
[2462.50 --> 2463.36]  it comes soon.
[2463.36 --> 2465.02]  We hope it comes soon.
[2467.10 --> 2468.52]  Someone needs to get it soon.
[2469.28 --> 2471.66]  I have a tip there that I'll provide later.
[2471.88 --> 2472.06]  Yeah.
[2472.34 --> 2477.84]  I don't know if you all have seen what Eric Bernardson is doing with Modal and Modal Labs.
[2478.24 --> 2479.84]  I've been playing around with that recently.
[2479.92 --> 2481.54]  I've been pretty floored by it.
[2481.64 --> 2485.90]  But anyway, that's a whole nother side topic and episode, which hopefully we can have soon.
[2486.28 --> 2486.52]  Totally.
[2486.52 --> 2490.40]  But I think to maybe the second part of the question, which was how do different organizations
[2490.40 --> 2494.94]  think about maybe the ML Ops question and something that we do want to address here,
[2495.00 --> 2496.46]  which is it does depend.
[2496.72 --> 2503.64]  It really does depend in terms of the maturity of the organization and budget, time, et cetera.
[2503.72 --> 2509.46]  These are all different axes that fundamentally define how a team or a business should think
[2509.46 --> 2511.12]  about its approach to ML Ops.
[2511.78 --> 2514.72]  And there's different axes that we can go into exactly what they are.
[2514.72 --> 2518.10]  But open source versus not open source.
[2518.76 --> 2521.72]  Are you going to stitch together a bunch of open source tools or are you going to use
[2521.72 --> 2523.02]  SageMaker out of the box?
[2523.68 --> 2524.96]  How much money do you have?
[2525.40 --> 2528.18]  Can you get by with just spinning everything up on your own?
[2528.68 --> 2531.36]  All these different axes different organizations have to think through.
[2532.02 --> 2534.20]  And it becomes not a one size fits all.
[2534.54 --> 2539.24]  It really is like it's a function of all these different parameters to really tailor the
[2539.24 --> 2540.56]  right solution to the organization.
[2541.24 --> 2541.94]  And there you go.
[2541.94 --> 2547.22]  You didn't realize that Mr. Michael has a little consultant in his blood.
[2548.06 --> 2549.80]  Do I get to put another plug here?
[2549.84 --> 2550.70]  Another shameless plug?
[2550.78 --> 2551.60]  Is that what this is?
[2551.78 --> 2552.14]  No.
[2552.56 --> 2553.68]  As many as you want.
[2553.90 --> 2554.04]  Yeah.
[2554.12 --> 2555.10]  As many as you want.
[2556.94 --> 2560.66]  That is the most consulting answer you can possibly give to any question.
[2560.78 --> 2565.48]  It's like, well, for this rate, I can tell you more details on what comes after.
[2565.68 --> 2566.44]  Yeah, exactly.
[2566.92 --> 2567.86]  You want to go at it.
[2567.86 --> 2574.86]  But I think I just will add a quick piece to that, which is there was a time in the MLOps
[2574.86 --> 2582.98]  community that like a week wouldn't go by in our Slack where someone would not share the
[2582.98 --> 2585.40]  you are not Google blog post.
[2585.40 --> 2595.82]  And it's like the amount of people that try and go at it and try and get that, especially because Google puts out so much great thought leadership on MLOps.
[2595.82 --> 2603.30]  And they have the level zero, level one, level two, or they have the like ML test score, all that stuff.
[2603.30 --> 2611.42]  And people think that straight out from zero to one, you need to be creating everything automated.
[2611.66 --> 2619.06]  It needs to be like the most high performance bulletproof system that you can think of.
[2619.30 --> 2622.50]  And it was just setting up a lot of people for failure.
[2622.50 --> 2637.70]  And I think we've moved past that because I haven't seen the you are not Google blog post being shared as much in the community, which makes me think people recognize and they're a little bit more self-aware when they're trying to create their systems at their jobs.
[2638.06 --> 2639.74]  You don't think they're just off in the corner crying?
[2639.74 --> 2644.70]  Or they just don't think being Google is a good thing anymore, just objectively given.
[2646.08 --> 2647.70]  Yeah, that might be it too.
[2648.04 --> 2657.50]  I think I was listening to I don't know if you all listen to the Indie Hackers podcast, but a recent episode, like I think they made this good point.
[2657.58 --> 2662.46]  They were talking about like because they talk about a lot about like bootstrap startups and stuff like that.
[2662.46 --> 2677.92]  And one of the points they made was like, you know, whenever like Basecamp was around or like starting up in that sort of thing, like they made such inflammatory statements about like, like taking venture capital is stupid.
[2677.92 --> 2682.08]  Like, why would you ever do like there was a need for that voice to be in there?
[2682.30 --> 2682.50]  Right.
[2682.70 --> 2686.24]  That voice is still there with the founder, you know, it's not changed.
[2686.24 --> 2699.58]  But now like you hear less of that, I think, and it's sort of like normalized in that like there's still different perspectives, but there's not like as much like it's become more normalized to have these like more nuanced discussions.
[2699.58 --> 2712.34]  I think with MLOps, there's sort of like, you know, we've all made our sort of inflammatory like podcast titles, like whatever it was, MLOps is dead or, you know, I forget what it was.
[2712.34 --> 2734.22]  Um, and so there is probably like still this, we're kind of feeling out where like the normal is and where things settle down to and providing like a balanced perspective where, yeah, like you probably shouldn't be doing MLOps the same way Google is, but you also should probably be doing MLOps.
[2734.40 --> 2740.34]  It's just like where on that spectrum do you land and what type of tools make sense for you?
[2740.34 --> 2743.62]  You know, in real life, I don't think it's you probably should not be.
[2743.72 --> 2747.26]  I think it's you can't do MLOps the way Google does.
[2747.74 --> 2754.14]  I mean, just from a resource standpoint, you know, most companies don't have that team available and that set of tools.
[2754.36 --> 2766.26]  And, you know, I like the fact that we're talking it in a more realistic context here, you know, for the vast majority of us out there that are not, you know, accessing the best of the best in all the categories.
[2766.26 --> 2768.34]  It's not possible for many of us.
[2768.64 --> 2770.20]  We have to settle for something that's doable.
[2770.30 --> 2775.28]  Kind of going to Demetrius's point, you know, you have to find that level that you can do it and you can sustain it.
[2775.38 --> 2779.70]  And yet it's still incredibly productive, even if it's not the Google version.
[2779.70 --> 2799.42]  Yeah. And one thing I'm fascinated by, just because there is almost this open source, you've got one person trying to hack something together and looking out there and seeing what's on the market that they can get for a price point between free and cheap.
[2799.42 --> 2807.32]  And then you've got the Googles that have built everything and have so much time and ability to do that.
[2807.32 --> 2816.48]  And in between those two points, you have a lot of companies that popped up and they popped up in the last like three to five years.
[2816.72 --> 2823.24]  And as Mikhail was saying, we came at MLOps from this data science perspective.
[2823.24 --> 2827.50]  And so I think in the beginning a lot, we're trying to cater to them.
[2827.66 --> 2831.72]  And then some were like, whoa, wait a minute, there's like platform engineers.
[2831.72 --> 2833.86]  And so they try to cater to them.
[2833.86 --> 2849.46]  And then you're seeing now, I almost wanted to like change my title for what I do on LinkedIn as I'm just going to be like the I ride hype waves because MLOps was a complete hype wave.
[2849.46 --> 2855.02]  And we felt it. And especially like I just got lucky because the pandemic hit.
[2855.14 --> 2859.08]  And right when it hit, I was working for a company that was trying to sell MLOps tools.
[2859.62 --> 2863.48]  And that company went out of business, but I was in the MLOps world.
[2863.48 --> 2867.34]  So I figured I would start this Slack community and then it took off.
[2867.34 --> 2873.60]  Right. And so I was able to ride that hype wave and we really felt it over the last two, three years.
[2873.60 --> 2877.54]  And now it's like, all right, now there's this generative AI hype wave.
[2877.72 --> 2888.42]  And so if you talk to VCs and the ones that poured a boatload of cash into the MLOps market, they're now like, yeah, that's kind of not really that big of a deal anymore.
[2888.58 --> 2890.50]  We're not going to follow up on all those investments.
[2890.66 --> 2894.84]  What we're going to do is invest in the next AI tool.
[2894.84 --> 2906.62]  And so I love thinking about that and how now what is the new hype cycle of the AI and generative AI, large language models?
[2906.88 --> 2908.46]  Like, where's that going to play out?
[2908.68 --> 2910.14]  You know, we've been talking about it.
[2910.30 --> 2913.96]  There's a lot of potential out there, but where are we going to go with that?
[2913.96 --> 2917.14]  And is it like just a bunch of money pouring into it?
[2917.14 --> 2919.62]  And who knows what's actually going to happen?
[2919.82 --> 2921.36]  It's kind of funny when you say that.
[2921.36 --> 2928.44]  And it's like there's an oversimplification, you know, when the market observes these things, you know, and, you know, MLOps.
[2928.60 --> 2929.74]  Well, now we're past that.
[2929.82 --> 2931.06]  You know, that's been solved.
[2931.22 --> 2935.36]  You know, we're going to Web3, you know, whichever hype cycle it is.
[2936.12 --> 2944.86]  But I think when you look at what's happening, it takes all these things to have gotten, you know, right now we're saying generative because that's kind of the sexiest part of the puzzle.
[2945.22 --> 2946.86]  But it's not just generative.
[2946.86 --> 2952.38]  It's the fact that you have MLOps now that's matured a little bit and is supporting all that.
[2952.78 --> 2956.38]  You have the large language models that people like Daniel have been working on.
[2957.00 --> 2959.36]  You have all the transformers that are well-established.
[2959.56 --> 2967.08]  If you didn't have all of those components, the current hype that's now being attributed to generative would not be happening.
[2967.08 --> 2972.56]  And so it's once again an oversimplification by the market on the sexy piece.
[2973.06 --> 2978.56]  But it's that whole ecosystem that's evolved over the last few years that enabled all that to happen.
[2979.10 --> 2981.54]  And so we're seeing a really cool moment, definitely.
[2982.30 --> 2986.24]  But it's really the fusion of it all as opposed to just being generative.
[2986.96 --> 2989.42]  You couldn't have generative today without that.
[2989.80 --> 2991.24]  I think that's such a fantastic point.
[2991.24 --> 3000.76]  I just want to sit on that a little bit longer because when the GPT-3 paper came out, this was, I guess, toward the end of 2020, maybe middle to end of 2020.
[3001.36 --> 3004.26]  You know, this is like a long thing that I remember reading.
[3004.60 --> 3012.60]  And the most interesting, in my mind, achievements of that whole system was not even anything about modeling, right?
[3012.66 --> 3019.10]  Like the fundamentally the building blocks of the AI architecture, if you want to call it that, was just we've been using these systems for years in some sense.
[3019.10 --> 3037.92]  It was really the fact that they had built this incredibly good software infrastructure to build out, train large systems at this scale over this many GPUs at this latency to make sure that, you know, the updates for the gradients could happen fast enough that this wasn't going to take 50 years to train.
[3038.52 --> 3041.84]  And they did that all, which fundamentally was really like an MLOps challenge.
[3041.84 --> 3042.66]  I mean, at its core.
[3042.92 --> 3043.26]  Agreed.
[3043.28 --> 3046.02]  You know, being able to architect that kind of a system is the complexity.
[3046.02 --> 3050.56]  It's not the fact that there was this new scientific achievement that we really came up with.
[3050.60 --> 3051.88]  It was really like an engineering achievement.
[3052.04 --> 3055.66]  And so in that way, it totally was a layering on of things that we had seen before.
[3056.28 --> 3058.22]  But, you know, now they're like old hat, right?
[3058.24 --> 3062.42]  Like now we have open source repos that can literally approximate the same effect.
[3062.52 --> 3065.84]  Like deep speed from Microsoft has become really fast and been very used.
[3066.36 --> 3068.16]  You can train large systems at that scale.
[3068.56 --> 3072.78]  But the people that pioneered those systems really had to solve some MLOps challenges in their own right.
[3073.02 --> 3074.22]  It's all right there.
[3074.22 --> 3075.42]  They haven't gone away.
[3075.74 --> 3077.68]  You know, it's still right there.
[3077.82 --> 3082.90]  It's a team effort for all of those different parts, constituent parts to put the whole together.
[3083.10 --> 3088.90]  But at this moment, the word generative is the front man, apparently, you know, as we record this today.
[3089.40 --> 3099.54]  It's pretty amazing that it's that MLOps take that has put that all together and kept it together, kept them in lockstep so that you can create the new things of today.
[3099.54 --> 3106.26]  Yeah. I mean, another example of that is like all that we're hearing about, about language model chaining and that sort of thing.
[3106.26 --> 3111.12]  Like this is like if you look at each step of that process, right?
[3111.22 --> 3116.14]  Langchain or whatever it is, those are things we've been talking about for a long time.
[3116.14 --> 3123.76]  Like there is an operational burden, though, to like chain these things together and make them work well, like in concert.
[3124.00 --> 3128.22]  Right. That's really like one of the fundamental things that we learn.
[3128.22 --> 3142.42]  Like when we talked about chat GPT, right, like the like the language model existed, reinforcement learning existed, human feedback existed, like all of these things existed, like the chaining of them together in a certain workflow is the real interesting piece.
[3142.42 --> 3151.52]  So I do think that's really exciting where a lot of those sort of chaining operations and like bringing things together in unique ways.
[3151.66 --> 3155.20]  That is a lot more possible because the tooling has gotten better.
[3155.38 --> 3157.60]  It doesn't like move us past MLOps.
[3157.70 --> 3161.30]  Actually, it just like we use MLOps slightly differently.
[3161.30 --> 3167.14]  And if anything, I think it becomes more crucial because there's so many moving pieces, right?
[3167.50 --> 3169.28]  Shoulders of giants all the way through.
[3169.28 --> 3174.36]  You combine that with the Einstein turtles all the way down kind of thing, it's shoulders of giants all the way down.
[3174.74 --> 3175.06]  Yeah.
[3175.22 --> 3186.28]  The one thing to add maybe to that is very often when I have described sort of the progression of MLOps over time, like people often like to use the Gardner hype cycle, right, to describe trends and technology, right?
[3186.28 --> 3192.38]  You have kind of the initial hype, then the waiting and the kind of the trough of just disillusionment and then this gradual climb upwards, right?
[3192.98 --> 3195.58]  I've often said that right now where we are, we're at that gradual climb upwards.
[3195.58 --> 3202.16]  Like the MLOps systems and the technology developed are like standardized and they're becoming more commonplace and people are using them.
[3202.46 --> 3209.76]  But the thing is that linear climb upward, while it is where a lot of value is extracted, is not really what a VC would look for.
[3209.88 --> 3210.80]  They would want this.
[3210.96 --> 3212.86]  They want something that's like exponential in growth.
[3212.86 --> 3219.40]  And so they're never going to ride a hype train that's like a linear climb upwards, even if that's where people are actually deriving value.
[3219.62 --> 3225.60]  They're like, well, what about how do we get to the next thing in the next Gardner hype cycle where there's the next big inflection point up that we need to ride?
[3225.66 --> 3229.70]  Because that's where you get real 100x gains if, you know, that's the kind of thing they're looking for.
[3229.90 --> 3237.36]  You know, and ironically, the place where you find all that value there after that initial hype is from the trough of disillusionment.
[3237.36 --> 3240.70]  You know, that's where you kind of go, now I understand.
[3241.10 --> 3242.68]  Now I know what we really need to do.
[3242.72 --> 3245.06]  And you get that really good growth after that.
[3245.36 --> 3245.88]  That's a great point.
[3246.00 --> 3246.44]  That's a great point.
[3247.04 --> 3247.24]  Yeah.
[3247.48 --> 3248.30]  This has been amazing.
[3248.48 --> 3249.46]  Yeah, this has been awesome.
[3250.52 --> 3255.08]  I have not needed to carry the conversation at all.
[3255.08 --> 3259.42]  So I appreciate you all doing the heavy lifting for me.
[3259.58 --> 3262.50]  Usually I am constantly thinking about that.
[3262.64 --> 3265.24]  And you made it very easy today.
[3265.24 --> 3266.22]  So I appreciate that.
[3266.22 --> 3267.66]  This was a fun conversation.
[3268.04 --> 3268.74]  This is awesome.
[3268.92 --> 3269.58]  We should do this more often.
[3269.80 --> 3270.70]  Yeah, we should.
[3270.78 --> 3276.92]  We should circle back and see if any of the things that we said actually are true next year.
[3277.46 --> 3281.06]  Which maybe some of them, I'm going for like 25%.
[3281.06 --> 3282.24]  If I get there, I'm good.
[3282.46 --> 3285.08]  Well, I didn't put my money on any of these predictions.
[3285.40 --> 3286.50]  So I don't really care.
[3286.78 --> 3287.12]  Right.
[3287.28 --> 3289.72]  You've already explained that you're not culpable.
[3290.28 --> 3291.20]  I'm not culpable.
[3291.62 --> 3293.34]  On the hook for anything.
[3293.82 --> 3295.08]  Rick and Mortify.
[3295.08 --> 3296.66]  It's just a toy project.
[3296.80 --> 3297.80]  Don't worry about it.
[3298.16 --> 3299.06]  I come in peace.
[3300.02 --> 3303.18]  I keep waiting, you know, because we can see each other on video.
[3303.40 --> 3308.84]  I know it's an audio recording, but I keep waiting for the feds to bust in behind you on your screen there.
[3308.94 --> 3311.50]  You know, the door goes flying back.
[3311.50 --> 3314.24]  It's a different sort of BBC kid moment.
[3316.02 --> 3316.46]  Yeah.
[3316.50 --> 3320.00]  And then my mic just goes out and it's like, well, he'll be back probably.
[3320.38 --> 3320.68]  Maybe.
[3321.00 --> 3321.64]  He'll be back.
[3321.94 --> 3322.62]  That's right.
[3323.28 --> 3325.42]  But then Demetrius would have to carry the conversation.
[3325.88 --> 3326.20]  Yeah.
[3326.48 --> 3327.66]  That would not be good.
[3327.90 --> 3329.22]  I'd be looking for you.
[3329.22 --> 3336.90]  Well, next year we'll see if this or any of the other things come true on Practical AI plus MLOps community.
[3337.32 --> 3342.60]  Definitely check out the show notes for those Practical AI listeners out there.
[3342.92 --> 3347.32]  We're going to include links to all the great things going on in the MLOps community.
[3347.54 --> 3352.54]  Slack channel, podcast, events, newsletter, all sorts of amazing stuff.
[3352.96 --> 3353.60]  And yeah.
[3353.76 --> 3354.36]  Thanks, guys.
[3354.42 --> 3355.76]  It's been awesome to have you on the show.
[3356.10 --> 3356.40]  Likewise.
[3356.40 --> 3356.76]  Thank you.
[3356.94 --> 3357.26]  Pleasure.
[3357.26 --> 3368.92]  Thank you for listening to Practical AI.
[3369.42 --> 3373.24]  Your next step is to subscribe now, if you haven't already.
[3373.70 --> 3379.72]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[3380.18 --> 3385.10]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[3385.10 --> 3389.48]  Check out what they're up to at Fastly.com and Fly.io.
[3389.88 --> 3395.20]  And to our Beat Freakin' Residence Breakmaster Cylinder for continuously cranking out the best beats in the biz.
[3395.48 --> 3396.38]  That's all for now.
[3396.64 --> 3397.82]  We'll talk to you again next time.
[3397.82 --> 3408.84]  Hit five.
[3409.66 --> 3412.40]  Charm Madness Breakthrough
[3412.40 --> 3415.14]  Talk about Twitter.
[3415.20 --> 3416.20]  .
