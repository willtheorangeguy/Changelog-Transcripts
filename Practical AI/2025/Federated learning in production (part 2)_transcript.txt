[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.46 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[26.32 --> 28.36]  Thanks to our partners at Fly.io.
[28.36 --> 31.10]  Launch your AI apps in five minutes or less.
[31.40 --> 33.40]  Learn how at Fly.io.
[44.48 --> 48.40]  Welcome to another episode of the Practical AI podcast.
[48.80 --> 50.60]  This is Daniel Whitenak.
[50.70 --> 56.88]  I am CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who
[56.88 --> 60.16]  is a Principal AI Research Engineer at Lockheed Martin.
[60.54 --> 61.18]  How are you doing, Chris?
[61.76 --> 63.02]  Doing great today, Daniel.
[63.14 --> 67.80]  It's a beautiful spring day here in Atlanta, Georgia, and I got to say, the flowers are
[67.80 --> 68.40]  coming out.
[68.62 --> 70.84]  It's a nice day to talk.
[71.22 --> 75.54]  They're probably distributed all over the various lawns.
[75.76 --> 76.22]  Everywhere.
[76.70 --> 77.54]  Federated even.
[77.70 --> 78.54]  Yes, yes.
[78.54 --> 81.64]  Well, Chris, this reminds me.
[81.64 --> 90.56]  Last week, we had a kind of part one intro to federated learning and some details about
[90.56 --> 93.78]  that with Patrick from Intel.
[94.28 --> 102.78]  He mentioned recently that he was at the Flower Labs conference and the flower framework around
[102.78 --> 103.60]  federated learning.
[103.72 --> 105.10]  He mentioned quite a few times.
[105.10 --> 110.28]  Well, we're privileged to kind of carry on the conversation around federated learning
[110.28 --> 117.44]  into a kind of part two on the subject because we've got Chong Shen with us, who is a research
[117.44 --> 119.14]  engineer at Flower Labs.
[119.36 --> 119.88]  Welcome, Chong.
[120.02 --> 120.48]  How are you doing?
[120.96 --> 121.26]  Hi.
[121.60 --> 123.38]  I'm doing very well.
[123.54 --> 124.44]  Thanks for having me.
[124.82 --> 125.48]  Yeah, yeah.
[125.52 --> 128.12]  And actually, we were talking before the show.
[128.12 --> 136.30]  So this is the second time that we've got to chat about Flower on the podcast back in 2021.
[137.32 --> 145.48]  So even before AI was invented with ChatGPT, apparently we were having conversations about
[145.48 --> 145.82]  AI.
[145.98 --> 149.08]  And one of those was with Daniel from Flower.
[149.60 --> 154.24]  That's episode 160 titled Friendly Federated Learning.
[154.24 --> 156.66]  It took me a second to say that one.
[157.10 --> 163.76]  But I'm sure a lot has changed and updated and advanced in that time, of course.
[164.46 --> 170.38]  Maybe just to start things out, Chong, could you give us a little bit of a context of your
[170.38 --> 176.50]  background and how you got kind of introduced to this idea of federated learning and eventually
[176.50 --> 179.06]  ended up kind of working with Flower?
[179.66 --> 180.28]  Yeah, absolutely.
[180.92 --> 183.08]  Well, thanks again for having me.
[183.08 --> 186.98]  So my background is in computational physics.
[187.16 --> 193.72]  So I spent many years working, doing research in the computational physics field, both my
[193.72 --> 194.76]  PhD and a postdoc.
[195.22 --> 199.16]  So I worked a lot on parallel computing, on super computing classes.
[199.78 --> 203.54]  I was also very interested in machine learning and deep learning in general.
[204.18 --> 210.12]  So when I pivoted away from academia to go into what they call industry, there was this
[210.12 --> 213.20]  space where you have distributed learning.
[213.92 --> 216.70]  So that was in 2021.
[217.10 --> 223.76]  So when I started my career back then, it started as a sort of a data science consulting business,
[223.76 --> 225.42]  but specializing in federated learning.
[225.42 --> 231.70]  And I saw lots of projects that were very interested to adopt federated learning or this distributed
[231.70 --> 234.96]  learning approach to solve some specific problems that they have.
[235.56 --> 239.24]  But I also came across the Flower framework.
[239.24 --> 243.60]  And open source development is a big passion of mine.
[243.60 --> 256.02]  So being able to develop a framework that is used effectively with a very permissible license, I think it's a pretty cool thing to do.
[256.50 --> 262.60]  So that's why I decided to join Flower Labs and become a core contributor to the framework itself.
[262.60 --> 263.32]  Yeah.
[263.66 --> 263.90]  Yeah.
[264.00 --> 272.28]  And I feel already connected with you because my background is in physics as well.
[272.38 --> 280.60]  It's always good to have other physicists on the show that have somehow migrated into the AI world.
[280.72 --> 288.08]  I'm wondering in that transition, like, you know, one of you mentioned this transition kind of academic to industry.
[288.08 --> 291.82]  You were getting into even consulting around federated learning.
[291.96 --> 299.66]  Was that idea of federation or distributed, you know, computing or however you thought about that?
[299.72 --> 307.08]  Was that kind of a key piece of what you were doing in academia, which led you kind of into that interest?
[307.18 --> 316.08]  Or was it something else that kind of sparked the desire to really dig in there as you were kind of going into, quote, industry as you mentioned?
[316.08 --> 316.52]  Yeah.
[316.88 --> 317.20]  Yeah.
[318.10 --> 321.04]  It wasn't something I came across in academia, surprisingly.
[321.98 --> 328.18]  But somehow when I stepped into the data science world, I came across people who are looking into it.
[328.38 --> 334.64]  And that became an approach that back then we sort of adopted to try and solve some problems.
[334.96 --> 337.14]  So we saw that, you know, federated learning could be a way to solve it.
[337.26 --> 339.48]  And then it sort of, it was very coincidental.
[339.66 --> 341.08]  It was like, ah, okay, it's distributed learning.
[341.18 --> 341.98]  It's distributed computing.
[342.28 --> 344.28]  So it resonated with me quite strongly.
[344.90 --> 345.12]  Yeah.
[345.12 --> 358.18]  And was that related to working with sensitive data or in regulated industries or something like in those, you know, consulting projects or, you know, just, yeah, interested in kind of that progression?
[358.64 --> 362.62]  Yeah, actually, there are, I would say, two broad categories.
[362.62 --> 366.54]  One where the data is incredibly sensitive.
[367.60 --> 377.88]  And we usually refer to them as really siloed data, you know, data that should not absolutely leave the boundaries of where it was generated.
[377.88 --> 385.44]  And then the second group or second cluster is the problems where the data sources are so massive.
[385.60 --> 398.46]  The point at which the data is generated generates so much data every second of the day that they just can't do any useful or meaningful analysis on this kind of raw data.
[398.46 --> 400.14]  And they have to do a lot of downsampling.
[400.88 --> 411.88]  So they try to look into pushing competition to the edge and try to see if they could apply some sort of machine learning approach or deep learning approaches on this sort of massively generated data without needing to downsample them.
[411.88 --> 412.88]  That makes sense.
[412.88 --> 428.08]  And yeah, if I guess I should explicitly mention as well that in the kind of part one of this two parter with Patrick, Patrick did provide a kind of detailed introduction to the idea of federated learning.
[428.08 --> 430.76]  And we discussed that at length.
[431.06 --> 438.00]  So if people want to go back to the previous episode and listen through that, that may provide some context.
[438.20 --> 451.64]  But it probably would be worthwhile just to give, you know, your sort of 30 second or couple minute view on federated learning and how you would describe it at a high level.
[451.70 --> 454.16]  And then maybe we can jump into some other things.
[454.62 --> 454.84]  Sure.
[454.92 --> 455.30]  Absolutely.
[455.30 --> 461.66]  The easiest way to think about it is looking at your classical machine learning approach, right?
[463.24 --> 466.98]  Classically, you need to bring all the data into a single location.
[467.48 --> 472.36]  Think of a database or on disk, and then you train your model on that data.
[473.24 --> 482.84]  But sometimes it's not so easy to actually bring all the data into one location just because of the privacy reasons about moving your data,
[482.84 --> 488.24]  some geopolitical considerations surrounding it, and also the data volume that's been generated.
[488.76 --> 500.18]  So instead of bringing all the data to one spot and training a machine learning model on that, what you do is you move the machine learning models to the point at which the data is generated.
[500.18 --> 505.58]  And then you train these local machine learning models at these sources.
[505.58 --> 514.60]  And instead of moving the data across, you move the model weights to a central server, which is much, much smaller.
[515.10 --> 520.00]  And you can then aggregate the model weights to learn from these various data sources.
[520.00 --> 531.62]  And then over time, as you repeat many, many rounds of this, you end up with a globally aggregated model that has learned from this variety of data sources without needing to move the data source across.
[532.00 --> 534.34]  That's the essence of federated learning.
[534.34 --> 549.32]  I'm curious, as you guys have worked on the framework and you have new users coming into it, what usually prompts a typical user from your perspective to move into federated learning?
[549.32 --> 564.66]  Like, you know, before they're really fully into it and they understand the benefits and they're sold on it, if you will, what's usually in your experience the impetus that kind of gets them into that mindset and kind of drives them in that direction initially?
[565.16 --> 567.56]  What causes the change in the way they're thinking?
[567.72 --> 572.48]  So they go, I definitely need to get into federated learning and go use flower specifically.
[573.06 --> 573.54]  Yeah, absolutely.
[573.54 --> 580.16]  I think from my experience, the biggest driver is when they realize they can't move their data, right?
[580.36 --> 584.48]  But when they speak to all the parties involved, they say, oh, I have this data set.
[584.60 --> 585.50]  Oh, you have this data set.
[585.64 --> 586.92]  But I don't really want to share them.
[587.34 --> 594.42]  And then, okay, this is where, you know, federated learning or FL comes to the picture and decided, okay, we really need to do this.
[594.76 --> 596.04]  This is one aspect of it.
[596.28 --> 601.64]  And the other aspect is when there's this big company who has, you know, let's just say many, many data sources.
[601.64 --> 610.14]  They say like, okay, it's super difficult to coordinate all our databases together so that we can have a cohesive way to train a machine learning model.
[610.58 --> 614.22]  And this is also when you try to look for all distributed machine learning systems.
[614.54 --> 616.70]  Then they realize, oh, they come across federated learning.
[616.86 --> 621.50]  So there's these two vectors that drive the typical use cases.
[622.36 --> 626.44]  Curious if I can follow up on that because I have a personal curiosity.
[626.44 --> 631.52]  I happen to work for one of these big companies that has data in lots of different places.
[632.40 --> 639.48]  And in addition to that, and we kind of in the previous – last week when we were talking, we talked a little bit about some of the privacy issues as well.
[639.96 --> 641.44]  I'm curious what you think about this.
[641.96 --> 649.88]  Like in our case, and we're not the only one, lots of that data is stored at different levels of security and privacy.
[650.16 --> 654.10]  There are different enclaves, if you will, where you're trying to do that.
[654.10 --> 666.10]  And how does that ramp up the challenge of federated learning when you have different security concerns around the different data enclaves that you're trying to bring together through federated learning?
[666.40 --> 677.94]  How does one go – instead of saying all different locations for distributed data are equal, when you're dealing with different security concerns, do you have any ways of starting to think about that?
[677.94 --> 683.64]  Because as I come into it as a newbie on this, that seems like quite a challenge for me.
[683.84 --> 686.26]  Do you have any advice or guidance on how to think about it?
[686.76 --> 687.42]  Yeah, yeah.
[687.66 --> 697.64]  I think this is – from my experience is that the complexity of the solution scales with a number of data stakeholders involved.
[697.64 --> 713.70]  And when you mentioned about different levels of the enclaves, that to me sort of signals that there are many data owners who manage their data a bit differently.
[713.70 --> 725.40]  So the primary – the key to solving that is to harmonize the data standards first, to be able to get on to a federation.
[725.90 --> 730.52]  And then from then onward, the implementation becomes much, much easier.
[730.98 --> 732.56]  I think it's one of the key things that I've seen.
[732.56 --> 745.00]  And we've kind of talked about your background, the sort of introduction to federated learning, some of those motivations.
[745.92 --> 755.56]  Maybe before we get into flower specifically and some of the more production use, from your perspective as kind of being a central –
[755.56 --> 762.36]  you're at a kind of central place within the ecosystem of federated learning, I guess.
[763.04 --> 768.68]  What at a – just very honestly, sort of – because we had that last episode in 2021.
[769.16 --> 779.90]  From 2021 until now, like how is the state of adoption of federated learning kind of in industry different maybe now than before?
[779.90 --> 787.60]  Or how has that grown or how has that matured as a kind of ecosystem, I guess?
[788.34 --> 788.60]  Yeah.
[788.98 --> 790.26]  It's a very – yeah.
[790.62 --> 791.88]  It's a very good question.
[792.64 --> 804.08]  If I want to – if I were to put a number to it, and this is really arbitrary, I think there's 100x difference from 2021 when the flower framework sort of existed and now.
[804.08 --> 814.98]  And one of the key changes in the usage of federated learning is the ability to train foundational models and large language models.
[815.48 --> 820.16]  And this has been a significant change and driving force.
[820.16 --> 835.20]  So previously, when we talked about using the flower framework, you may be confined to models that are not super large, you know, small by today's standards of the order of hundreds, you know, millions of model parameters.
[835.20 --> 847.60]  But these days, when we're talking about making use of text data, image data for these foundational models, you are thinking about models at the order of billions of parameters.
[848.50 --> 860.60]  And there is a fundamental change in also how we have structured the architecture of our framework and also to increase the ability to stream large model weights.
[860.60 --> 865.94]  So all of these things are happening right now as we speak, and there's some exciting new progress.
[866.22 --> 868.66]  Hopefully, we release a new version in a couple of weeks.
[869.48 --> 873.44]  And for the users, the usage is identical.
[873.62 --> 874.52]  Nothing has changed.
[874.86 --> 878.60]  But what has been unlocked is the ability to then train very large models.
[879.58 --> 886.78]  So all of these really increases the appeal of using federated learning or the flower framework for, you know, a larger variety of use cases.
[890.60 --> 904.50]  It was beautiful about good code.
[904.64 --> 905.54]  It just works.
[905.54 --> 906.52]  No fuss.
[907.04 --> 909.84]  No five-hour debugging sessions at 2 a.m.
[909.84 --> 913.12]  That's exactly what NordLayer brings to business security.
[913.50 --> 919.32]  While you're busy shipping features and fixing bugs, NordLayer handles your network security in the background.
[919.32 --> 928.22]  It's like having a senior DevOps engineer who never sleeps, never takes vacation, and never accidentally deletes the production database.
[928.60 --> 929.56]  Zero trust architecture?
[930.02 --> 930.24]  Check.
[930.52 --> 934.40]  VPN that doesn't make your team want to work from the coffee shop instead?
[934.88 --> 935.38]  Double check.
[935.72 --> 939.10]  Deploy in under 10 minutes with no hardware to rack and stack?
[939.44 --> 940.14]  Triple check.
[940.62 --> 947.92]  Built on the same foundation as NordVPN, but designed for teams who need granular access control and compliance reporting.
[947.92 --> 952.52]  Because apparently it works on my machine is not sufficient for the auditors.
[952.52 --> 960.44]  The good news is our friends get up to 22% off plans, plus an additional 10% with the code practically10.
[960.74 --> 962.82]  That's practically-10.
[963.08 --> 968.84]  That's less than your monthly GitHub Copilot subscription, but infinitely more useful when the security team comes knocking.
[969.00 --> 971.74]  Check it out at nordlayer.com slash practicalai.
[972.30 --> 975.84]  Again, nordlayer.com slash practicalai.
[975.84 --> 988.62]  Well, Chung, as we've kind of dived into the show and we've already started making reference to flower quite a bit,
[988.62 --> 996.86]  but we haven't actually really described specifically what flower is in detail as a framework and what it brings and such as that.
[996.86 --> 1008.06]  Could you take a moment, and we probably should have done this before, but maybe kind of express exactly what flower is, what the components are,
[1008.32 --> 1016.06]  and how it kind of helps the user begin to federate their data in terms of what their workflow is.
[1016.14 --> 1018.68]  Could you talk a little about kind of the basics of it?
[1018.68 --> 1019.84]  Yeah, absolutely.
[1020.32 --> 1031.06]  So the flower framework is our flagship open source code that's built on the Apache 2.0 license.
[1031.06 --> 1040.08]  And this framework allows users, any data practitioners, to build a federated learning solution.
[1040.82 --> 1050.20]  So with the framework, what this means is they are able to, I guess, in code terms, install a basic Python distribution of flower
[1050.20 --> 1058.30]  and to build the different apps that allows you to construct the fundamental federated learning architecture.
[1058.52 --> 1063.16]  So what this means is to be able to spin up your server, which aggregates the model parameters,
[1063.60 --> 1066.84]  and to write the code to also do your training on the clients.
[1067.88 --> 1077.42]  The structure that we provide within the framework allows users to follow the same reproducible way to perform their federated learning.
[1077.42 --> 1080.28]  So I think at the essence, this is what it is.
[1080.52 --> 1085.30]  What I also wanted to say that, and one of the appeals of flower for me personally,
[1085.54 --> 1089.64]  is that we really emphasize the user experience.
[1090.22 --> 1094.26]  This is why we always say flower is the friendly federated learning framework.
[1094.66 --> 1100.22]  We want, we prioritize the experience of all our users.
[1100.64 --> 1102.82]  We support them on Slack.
[1102.82 --> 1109.80]  We also have a discourse channel called Flower Discuss, where we actively answer any of the questions from users.
[1110.50 --> 1118.26]  And we also have a fantastic community that has contributed a lot of code improvements to the core framework as well.
[1118.42 --> 1119.62]  So we are completely open.
[1120.22 --> 1127.30]  We build transparency and really accountable for every single line of code that we commit to it, you know, to the highest standards.
[1127.30 --> 1130.34]  Yeah, and I can testify personally.
[1131.32 --> 1139.26]  We, at Prediction Guard, we work with a number of students over time at Purdue University.
[1139.26 --> 1141.28]  They have like capstone projects.
[1141.44 --> 1142.26]  We're in the same town.
[1142.50 --> 1147.32]  So it's natural that we would, you know, work with some of those students.
[1147.52 --> 1149.42]  We've done that a couple times now.
[1149.42 --> 1165.82]  And one of those student groups that we had, I believe it was last year, actually did this sort of capstone project related to federated learning and training language models, translation models, and trying various things.
[1166.00 --> 1173.18]  And they evaluated a bunch of different things, but I think ended up using flower for the reasons that you mentioned.
[1173.18 --> 1177.56]  So they were newbies into this world of federated learning.
[1177.70 --> 1181.70]  Obviously, very smart students, no doubt there.
[1181.70 --> 1196.12]  But they definitely gravitated to the user experience with flower because, you know, they had programmed in Python and it just sort of came naturally to them.
[1196.12 --> 1207.50]  So, yeah, I'm sure that's a common experience that maybe you all hear from others, the sort of natural Pythonic way to kind of approach these topics.
[1208.26 --> 1208.96]  Yeah, yeah, we do.
[1209.04 --> 1209.44]  Absolutely.
[1211.18 --> 1213.58]  I'm very happy that you shared that experience.
[1213.78 --> 1215.86]  This is good to always hear feedback from your community.
[1215.86 --> 1225.16]  But, yes, Python being the really driving language behind machine learning models and deep learning models right now.
[1225.52 --> 1229.46]  So it's a really natural way to provide a Python SDK.
[1229.74 --> 1233.68]  You know, we support it from day one and we will continue to support it for a long time.
[1234.10 --> 1241.26]  I'm curious with the kind of extending that just a little bit beyond being in the language.
[1241.26 --> 1244.66]  I like the notion of the friendly language.
[1244.82 --> 1250.46]  You know, the word friendly appeals to me in terms of that user experience.
[1250.60 --> 1258.26]  Can you talk a little bit more about kind of why you're branding around friendly and what that means from a user experience standpoint?
[1259.12 --> 1261.28]  You know, what other aspects of it make it friendly?
[1261.54 --> 1268.68]  There are so many things out there that are not friendly that that definitely grabs my attention.
[1269.02 --> 1269.54]  Yeah, absolutely.
[1269.54 --> 1281.06]  I think what would be nice to explain is for the past 10 releases, we have dramatically improved the friendliness of our framework.
[1281.32 --> 1284.94]  Hopefully, I hope that's the experience that people will get out of this.
[1285.48 --> 1293.16]  The main point is to reduce the cognitive load of any developers who want to use our framework.
[1293.82 --> 1295.16]  So I'll give one concrete example.
[1295.16 --> 1301.42]  So we introduced the Flower CLIs a couple of releases ago, I think probably late last year.
[1301.92 --> 1318.60]  And what this does is with a simple FLWR space new command, N-E-W, a user is able to navigate these options through the command line and immediately have a templated project to work with for federated learning.
[1318.60 --> 1319.60]  And it runs out of the box.
[1319.60 --> 1324.14]  So after Flower Neo, the user goes through this, just follows the steps.
[1324.58 --> 1329.12]  And then you do FLWR space run, and it runs out of the box.
[1329.12 --> 1333.90]  And we have the core templates that are necessary for users to build on.
[1334.02 --> 1337.20]  We have the PyTorch, the typical ones, and the more exotic ones.
[1337.32 --> 1341.30]  You have Jaxx, and those who want it, they can use NumPy as well.
[1341.94 --> 1349.44]  All of these provides the boiler code for use to get started with, and it reduces so much startup time.
[1349.44 --> 1358.34]  Then with that, once a user has built all their applications, the user can also really monitor their runs.
[1358.64 --> 1362.66]  We also introduced commands like FWR space LS.
[1363.10 --> 1369.58]  It's really like LS in your terminal to just see what runs, what Flower runs are running at the moment.
[1370.02 --> 1374.58]  And also others like FWR space log to see the logs of your code.
[1374.58 --> 1384.52]  So all of these really simple CLI tools really help a user navigate and work with running code much more easily.
[1385.08 --> 1392.50]  Previously, I would say, you know, 2021, 2022, early 2022, the Flower framework was in a different place.
[1392.76 --> 1396.84]  How it worked back then was, it was still friendly.
[1396.84 --> 1404.58]  But the way that a user would need to start the federation would be to start three Python scripts.
[1405.12 --> 1411.12]  And this is not as intuitive or natural if you want to scale up or put into production.
[1411.66 --> 1418.86]  So with the introduction of the Flower CLI and a different way of deploying the architecture, which drives the federation,
[1418.86 --> 1427.14]  it really makes it so much easier for users to start building and then deploy the code.
[1427.92 --> 1432.04]  Well, you were kind of leading into maybe what was going to be my next question.
[1432.18 --> 1435.22]  You mentioned kind of taking things into production.
[1435.58 --> 1442.48]  So some people might hear kind of friendly framework, which is a good thing, as Chris mentioned.
[1442.48 --> 1452.08]  But they might associate that with, you know, prototyping and learning and that sort of thing, not necessarily production usage.
[1452.08 --> 1462.62]  So I'd love if you could kind of help us understand what does a, if I'm implementing a federated learning system with Flower,
[1462.76 --> 1467.28]  what does a production federated learning system look like?
[1467.28 --> 1472.50]  I'm sure there's different sorts of, you know, ways that that could manifest.
[1472.64 --> 1474.54]  But certainly you've seen a lot of use cases.
[1474.66 --> 1477.60]  Maybe you could just highlight some examples for us.
[1477.68 --> 1481.60]  What does that production federated learning system look like?
[1481.60 --> 1492.88]  And what are some of the considerations that you have to think about going from kind of a toy prototype of like this might work to a full scale production rollout?
[1493.58 --> 1494.60]  Yeah, absolutely.
[1494.60 --> 1501.38]  I think it is a nice segue between the fairness aspect and moving to production.
[1501.38 --> 1510.68]  Because what I want to mention here is that I walked through a very simplified workflow of how a user would build out an FL solution.
[1510.96 --> 1511.02]  Okay.
[1512.08 --> 1520.12]  With the Flower Framework, you could build and write the apps that you need for your aggregation, your server aggregation,
[1520.12 --> 1524.26]  and also for the clients which actually train the models at the data sources.
[1525.32 --> 1526.90]  In the first iteration,
[1526.90 --> 1531.88]  a user might actually run it in what we call the simulation runtime.
[1532.68 --> 1538.92]  So without worrying about the actual data sources or to work out the data engineering aspect of it,
[1539.02 --> 1548.26]  you could test the implementation of the basic architecture in the simulation runtime using data sets that are obtained from Hugging Face, for example,
[1548.26 --> 1552.10]  or from data sets that you could just create artificially just for testing purposes.
[1552.10 --> 1558.94]  With the same code that you use to train the models and the clients and the aggregate,
[1559.48 --> 1566.42]  you can then point the code to a different runtime and then execute it in what we call the deployment runtime.
[1566.42 --> 1569.18]  And this brings us one step closer to production.
[1570.26 --> 1577.56]  So once you have this mode of execution, the clients would then be tapped in to the data sources,
[1577.56 --> 1582.64]  and you can then start training your actual federated model.
[1584.08 --> 1587.76]  So what does it take to deploy a production system?
[1588.10 --> 1592.82]  So firstly, there is a nice acronym that I like to use from the TinyML community.
[1593.14 --> 1593.82]  It's Blurb.
[1593.96 --> 1595.72]  I'm not sure if you've come across that before.
[1595.72 --> 1597.38]  Have you come across that before?
[1597.58 --> 1597.76]  Yeah.
[1598.68 --> 1598.80]  Yeah.
[1599.04 --> 1601.42]  But go ahead and explain.
[1602.10 --> 1602.36]  Yeah.
[1602.46 --> 1608.72]  So the TinyML community talks about the bandwidth, latency, efficiency, reliability, and privacy.
[1608.98 --> 1609.50]  I'm not mistaken.
[1609.92 --> 1611.02]  I could be wrong with the last one.
[1611.44 --> 1620.24]  But in the production grid system, what you really want is the reliability of the deployed solution to do the full computation.
[1620.64 --> 1624.02]  It doesn't have to be federated learning, but systems in general.
[1624.02 --> 1637.04]  So with the current version of the flower framework, we have separated what we call the application layer, where users will build apps, and these are the ones that users will modify.
[1637.04 --> 1643.76]  And then we also have the infrastructure layer, which underpins this system.
[1643.76 --> 1660.72]  So this infrastructure layer is responsible for receiving the flower commands from a user and then to distribute all the necessary code to the clients for the clients to actually perform the training.
[1660.72 --> 1667.62]  So in flower terms, you'll come across it, but we call this the superlink to actually host the server.
[1668.24 --> 1669.30]  And the supernodes.
[1669.80 --> 1676.22]  Supernodes are the long-running services which basically orchestrate the clients.
[1676.22 --> 1679.12]  So these two components are long-running.
[1679.74 --> 1692.90]  So with these two components, because they are long-running, the users can then run multiple and execute multiple federations across other systems without worrying about any of these components failing.
[1693.24 --> 1696.34]  So this is where the reliability comes to the picture.
[1696.34 --> 1703.40]  Because the connections are also established, we also handle the bandwidth and the connection.
[1704.16 --> 1708.58]  So we're trying to reduce the latencies between the supernodes and the superlink as well.
[1709.20 --> 1715.24]  So the infrastructure is something that's being deployed once and that will persist for the lifetime of the project.
[1715.88 --> 1720.66]  And this makes it much easier for the users to continue to work with the production grid system.
[1720.66 --> 1722.28]  So it's always there waiting for you.
[1722.68 --> 1731.84]  Anytime a user wants to go in and execute a run and look at the results, it's always there without worrying about any component failing and stopping the run.
[1731.84 --> 1761.82]  Thank you.
[1761.84 --> 1791.82]  Thank you.
[1791.84 --> 1793.84]  Thank you.
[1793.84 --> 1821.82]  Thank you.
[1821.84 --> 1823.84]  Thank you.
[1823.84 --> 1824.84]  Thank you.
[1824.84 --> 1825.84]  Thank you.
[1825.84 --> 1827.84]  Thank you.
[1851.84 --> 1858.84]  Thank you.
[1858.84 --> 1859.84]  There we Allah.
[1859.84 --> 1870.84]  Thank you.
[1871.20 --> 1876.86]  Thank you.
[1876.86 --> 1877.68]  Thank you.
[1877.68 --> 1893.20]  So Chong, I love this idea of the sort of super nodes and super links. And my thought is,
[1893.40 --> 1899.52]  I'm trying to work out in my head kind of, if I was, you know, let's say I'm working in the
[1899.52 --> 1906.22]  healthcare space and my sort of nodes are maybe different hospitals or different facilities in
[1906.22 --> 1913.68]  a network or something like that. And I have a central place where I have my super link and I'm
[1913.68 --> 1919.78]  doing the aggregation. Just from a practical standpoint, as I think Chris mentioned before,
[1919.86 --> 1924.42]  you have these different facilities, you have different maybe stakeholders with different data.
[1924.42 --> 1931.66]  What do I need to do as like, let's say I'm the person that's in charge of running the experiment,
[1931.66 --> 1940.96]  training the model. What do I need to do on the setup side to sort of connect in these super nodes or
[1940.96 --> 1947.98]  wherever the clients are? What sort of needs to exist there? How do I kind of register them and
[1947.98 --> 1955.36]  that setup process to really get going before I'm able to, you know, go in like you say, and from a
[1955.36 --> 1960.36]  user perspective, run experiments or perform runs, training runs and that sort of thing.
[1960.36 --> 1967.82]  Absolutely. So there are many ways to go about it. But I think the cleanest way is to think about two
[1967.82 --> 1976.94]  groups of roles. One is the administrator role. And they are responsible for deploying,
[1976.94 --> 1983.66]  deploying the super nodes in each of these, let's say, healthcare facilities, healthcare centers.
[1983.66 --> 1993.80]  They are responsible for making sure the correct user is registered onto the, to the superlink or the
[1993.80 --> 2001.72]  federation. And also to, you know, coordinate any monitor, basically monitor the usage of the superlink itself.
[2001.72 --> 2016.72]  So that's the administrator role. And then there is a user role or data practitioners, data scientists would then write their apps, you know, their server apps and their client apps, and then run these apps on the superlink,
[2016.72 --> 2044.72]  they are the federation that the administrator. So I think this clear distinction would be an easy way to think about it. So as a start, an administrator would say, say there are five hospitals want to form a federation. An administrator or administrators can go in and deploy the super node with the template. For example, if using a Kubernetes or Docker
[2044.72 --> 2074.22]  Docker containers, you can have Helm charts, you can deploy the super nodes in each of these five hospitals. The superlink can be hosted by a trusted third party server, or it can also be hosted by flower labs, for example, can host a superlink for you because it's just a simple service. And then the users would register or be authenticated on the superlink. So they need to be both authenticated and have the authorization to run the flower commands on the
[2074.72 --> 2081.72]  superlink. And that way, you can get the production system up and running in a cross silo setting.
[2081.72 --> 2101.62]  I'm curious as we're kind of talking through it, and I'm learning a lot from you as you're describing it. And you've kind of made reference to admin roles and client and server apps and, you know, superlinks and supernodes and stuff, which, you know, kind of in the context of federated, there's networking and stuff like that.
[2101.62 --> 2130.06]  So I guess I have a generalized question around that. And that is, is there any set of knowledge or skills that a user can kind of ramp up into or needs to know to use flower effectively? Like, like, like particular, for instance, you know, that maybe they're coming from more of a kind of a, the data science or kind of, you know, deep learning role. And, and maybe they haven't done a lot of networking and stuff like that.
[2130.06 --> 2143.98]  Do they need, are there skills that they need to be able to ramp up into to be most effective at using flower that you would recommend or, you know, what, you know, what, what would the expectation on the user be in that capacity?
[2143.98 --> 2145.98]  Yeah, that's a good question.
[2145.98 --> 2161.98]  Yeah, that's a good question. Actually, it's a fair question as well. In my opinion, what we're trying to convey is that you users do not need to think about the communication aspect of it at all, that everything is handled by the infrastructure.
[2161.98 --> 2177.48]  Of course, if a user starts to run into when, when the federated learning solution becomes a bit more complicated and run through very special cases.
[2177.48 --> 2186.74]  And this is where some understanding of the communication protocols and how these are set up, this could help as well.
[2187.24 --> 2197.54]  And I think for users who are stepping more into sort of administrative role and want to deploy the super nodes or work with the infrastructures, basically the super links and super nodes.
[2197.54 --> 2211.14]  There are the questions of infrastructure slash DevOps. You have to have some familiarity with deploying this in containers or working with ports, things like that.
[2211.14 --> 2222.80]  But fundamentally, when you first start to work with the framework, you can get started with a sort of vanilla production system without worrying too much about the communication or needing to know too much about it.
[2223.30 --> 2228.62]  And then as you, you know, get your feet wetter, then you can learn more along the way.
[2228.62 --> 2251.20]  Well, yeah, that, that line of thought, along with something that you earlier said about kind of how, you know, large language models generative have, have pushed the boundaries of how you do communicate data, you know, weights back and forth, how you can handle, you know, larger models with the more recent versions of flower.
[2251.20 --> 2255.66]  And you're releasing the new version in a couple of weeks, you know, even with, with more.
[2255.66 --> 2270.90]  I'm wondering generally how, you know, certainly that's one aspect of how this sort of boom and generative AI has probably influenced your, you know, roadmap and how you're thinking about things, what people are wanting to do with flower.
[2270.90 --> 2275.78]  I imagine there may be a variety of ways that that's impacting flower.
[2275.78 --> 2290.76]  I was even thinking while you were talking about that as like, wow, it'd be cool if there was a, you know, MCP server or, or something or, or, you know, helpers on top of, on top of flower that I could just, you know, type in natural language.
[2290.76 --> 2296.88]  And, you know, that would be a friendly, friendly interface to, to set up my experiments and that sort of thing.
[2296.88 --> 2319.92]  So, yeah, I mean, as a, as kind of one of the, the folks, you know, core folks working on the framework, how have you seen this kind of boom in interest around generative AI influence kind of the, the roadmap and what you're thinking about at flower, what, what you're, you know, maybe envision for the future of, of the framework, that sort of thing.
[2319.92 --> 2327.96]  Well, when you brought up the model context protocols at a small, my Facebook, there's definitely been some interesting conversations recently as well.
[2327.96 --> 2329.82]  We didn't attend about looking into that.
[2329.82 --> 2330.82]  Yeah.
[2330.82 --> 2338.68]  About the impact of generative, generative models or large language models slash multimodal model, multimodal models.
[2338.68 --> 2346.20]  There, there's been a, it's one of the driving forces for the flower framework as well.
[2346.20 --> 2361.34]  So we really believe that this state of the art LLMs, as we speak, yeah, they're running out of data to train, you know, back in, you know, in December last year, Ilya, co-founder of OpenAI, you were saying that data is running out.
[2361.52 --> 2364.10]  No, data has run out to train these LLMs.
[2364.10 --> 2367.38]  And yes, that's exactly the sentiment that we feel as well.
[2367.38 --> 2368.52]  It's the tip of the iceberg.
[2369.06 --> 2383.68]  There is tons of data locked in silos that could benefit from having a large language models, either pre-trained or fine tuned on in order to be useful, to be made useful.
[2384.60 --> 2388.58]  And, and the way to, to achieve it is, you know, through federative learning.
[2388.58 --> 2393.82]  I think this is one of the key technologies that is driving the framework.
[2393.82 --> 2405.94]  I'm curious kind of to extend that notion a little bit as we're, you know, we, we've been so into kind of the generative AI hype cycle for the last couple of years and stuff.
[2405.94 --> 2421.56]  And, and now we're that, that's kind of moving into combining models in different ways and, and agentic, you know, focus and, and ultimately physical, you know, models going out there in terms of, of interaction.
[2421.56 --> 2433.74]  And so, and I, I know I'm, what I'm seeing out there involves instead of just having one model, you know, people are now putting lots of different combinations of models together to get jobs done.
[2433.74 --> 2446.62]  Does that in any way change kind of how you should think about, about using federated learning is, is like every model that you might have in a solution, just its own one off flower implementation?
[2446.68 --> 2451.30]  Or is there any ways that you guys are thinking about combining models together?
[2451.30 --> 2460.32]  If they're all using data from, you know, different resources and stuff like that, like how, as we're moving into my solution has many models in it.
[2460.32 --> 2467.00]  Does that change in any way how users should think about using flower or architecting a flower based solution?
[2468.14 --> 2471.94]  It's a, it's a very deep question.
[2471.94 --> 2477.52]  I feel that there are a couple of possible futures here.
[2478.18 --> 2491.66]  There is a future where these agentic workflows, where you have models that are sort of chained together to achieve a certain task, could also be used eventually in concept with federated learning.
[2491.66 --> 2500.58]  So I see a future where there is a possibility about that as well, but there needs to be some intimidating steps there.
[2500.58 --> 2512.54]  And then the reason is because these models, when you use them for agentic workflows, they need to be really optimized for the agentic workflows, right?
[2512.60 --> 2519.00]  You have to have, they need to be trained on a certain type of structure and also be optimized for that.
[2519.04 --> 2520.76]  There needs to be some proper evaluations for that.
[2520.76 --> 2531.90]  So sort of the missing, I see the future where, you know, if, if these two sort of pathways of agentic workflows and federated learning come together,
[2532.10 --> 2538.58]  it will be that people should think about like having strong evals for this kind of workflows.
[2538.58 --> 2540.72]  And then knowing that there is a limit to them.
[2540.72 --> 2548.18]  Once you're able to quantify them, then to look for ways you can improve it through distributed learning, such as federated learning.
[2548.18 --> 2552.10]  And this is how you rationalize an improvement over agentic workflows.
[2552.10 --> 2564.60]  Well, Chong, it's been fascinating to hear some of your perspective on, you know, especially production use of federated learning and in flower.
[2564.60 --> 2572.02]  As we kind of draw to a close here, I imagine we'll have flower back on the podcast here in another couple of years or before.
[2572.28 --> 2575.32]  Hopefully this does, does be a recurring one.
[2575.32 --> 2585.80]  But as you look to this sort of next season of, you know, either what you're working on or just the ecosystem sort of more broadly,
[2586.60 --> 2599.48]  what's, what's very, what's exciting for you, interesting for you that kind of is always top of mind or is, is most, most there when you, when you go to, you know,
[2599.48 --> 2603.70]  you're going back from work in the evening with what's on your mind as you look forward.
[2604.30 --> 2604.74]  Yeah, absolutely.
[2604.74 --> 2620.32]  I think I'm very keen to think about this foundation LM that is purely trained on FL on federated learning and has been shown to be both like privacy preserving and also state of the art.
[2620.32 --> 2627.64]  I think if the viewers and also yourselves, if you check out, we are collaborating with Vana as well in the US.
[2628.78 --> 2634.22]  They are looking into a data dials and we are very much working on that.
[2634.40 --> 2643.38]  So I'm really looking forward to seeing the first LM in the world that is trained in FL way with SOTA standards.
[2644.04 --> 2644.22]  Awesome.
[2644.58 --> 2647.10]  Well, yeah, we look forward to that as well.
[2647.10 --> 2651.98]  Certainly come on the show and give us your comments on it when it, when it happens.
[2651.98 --> 2655.58]  But thank you so much for taking time, Chong, to talk with us.
[2655.64 --> 2667.36]  Really appreciate your perspectives and please pass along our, our thanks to the flower team and their continued work, you know, as a team on a great addition to the, to the ecosystem.
[2667.92 --> 2668.10]  I will.
[2668.20 --> 2669.12]  Thank you, Daniel and Chris.
[2669.24 --> 2670.48]  Thanks for having me, having me on the podcast.
[2677.10 --> 2678.80]  All right.
[2679.04 --> 2680.90]  That is our show for this week.
[2681.38 --> 2687.18]  If you haven't checked out our ChangeLog newsletter, head to changelog.com slash news.
[2687.58 --> 2689.68]  There you'll find 29 reasons.
[2689.90 --> 2693.10]  Yes, 29 reasons why you should subscribe.
[2693.66 --> 2695.10]  I'll tell you reason number 17.
[2695.68 --> 2698.46]  You might actually start looking forward to Mondays.
[2698.64 --> 2701.32]  Sounds like somebody's got a case of the Mondays.
[2701.32 --> 2706.28]  28 more reasons are waiting for you at changelog.com slash news.
[2706.52 --> 2712.18]  Thanks again to our partners at fly.io to Breakmaster Cylinder for the beats and to you for listening.
[2712.42 --> 2715.24]  That is all for now, but we'll talk to you again next time.
[2723.24 --> 2724.48]  Game on.
