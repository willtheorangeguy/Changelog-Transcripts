[0.00 --> 2.58]  Bandwidth for ChangeLog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at ChangeLog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash ChangeLog.
[17.46 --> 20.04]  This episode is brought to you by DigitalOcean.
[20.36 --> 25.14]  DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[25.14 --> 29.14]  They have an intuitive control panel, predictable pricing, team accounts,
[29.14 --> 36.82]  worldwide availability with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[37.06 --> 42.54]  DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[42.90 --> 46.34]  Head to do.co slash ChangeLog to get started with a $100 credit.
[46.64 --> 48.80]  Again, do.co slash ChangeLog.
[59.14 --> 66.00]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[66.44 --> 70.40]  This is where conversations around AI, machine learning, and data science happen.
[70.82 --> 75.42]  Join the community and Slack with us around various topics of the show at ChangeLog.com slash community.
[75.78 --> 76.76]  And follow us on Twitter.
[76.90 --> 78.54]  We're at Practical AI FM.
[78.92 --> 79.20]  Okay.
[79.38 --> 80.24]  Here's Daniel and Chris.
[80.24 --> 88.02]  Welcome to another episode of Practical AI.
[88.36 --> 91.26]  This is Daniel Whitenack, one of your co-hosts.
[91.30 --> 94.20]  I'm a data scientist with SIL International.
[94.80 --> 102.18]  And I've got my co-host with me, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[102.38 --> 103.08]  How are you doing, Chris?
[103.40 --> 104.60]  I am doing okay.
[104.60 --> 106.34]  I'm safe and I'm well.
[106.78 --> 107.76]  And so is my family.
[107.92 --> 109.98]  So that is a good sign for me.
[110.38 --> 111.42]  Yeah, that's great.
[111.62 --> 120.96]  I'm recording in a new location because we've got a bit of a full house at the moment with my brother-in-laws being back from college and living with us.
[121.06 --> 124.86]  And so I've transitioned my studio out into the dining room.
[125.02 --> 128.08]  So it's been an interesting week in that sense as well.
[128.28 --> 130.12]  We're all making adjustments these days.
[130.34 --> 133.20]  The world is an unusual time.
[133.38 --> 134.24]  Yeah, yeah.
[134.24 --> 135.32]  We're all making adjustments.
[135.32 --> 152.28]  But yeah, I've actually, it seems like I've been more busy work-wise since the crisis started than even before because SIL has been making various efforts to contribute in beneficial ways related to COVID-19.
[152.28 --> 158.88]  Including trying to translate the phrase wash your hands into as many languages as we can.
[158.88 --> 161.50]  Part of that is machine generated.
[161.74 --> 164.52]  And then part of that is just crowdsourced translations.
[164.52 --> 169.00]  And I think we're up to 454 in my last check.
[169.32 --> 169.46]  I know.
[169.46 --> 171.66]  I saw you tweet about that a few days ago.
[171.96 --> 175.34]  And so if you're not following Daniel, you definitely should.
[175.44 --> 177.72]  And you can see the work that he did there.
[178.32 --> 178.58]  Yeah.
[178.68 --> 185.28]  And those conversations and that work also led to some other discussions with one of my contacts at Intel.
[185.28 --> 195.98]  And she pointed me to this other project called COVID-QA, which some people at Intel started collaborating with this team from DeepSet AI.
[196.38 --> 205.66]  And I was super fascinated by this project and also interested in potentially contributing because they're looking to up the language support as well.
[206.10 --> 210.04]  But I had a conversation with them and they've agreed to be on the podcast today.
[210.04 --> 215.30]  So we've got Timo from DeepSet and then also Tony from Intel.
[215.54 --> 216.30]  Welcome, guys.
[217.14 --> 217.92]  Hey, welcome.
[218.36 --> 218.92]  Thanks so much.
[219.24 --> 220.18]  Thanks for the introduction.
[220.58 --> 229.82]  It's really been a great week and two weeks, actually, because this is how we started this COVID-QA project.
[229.98 --> 234.44]  But should I talk a little bit about myself first to begin with?
[234.76 --> 235.60]  Yeah, please do.
[235.70 --> 238.68]  If you want to introduce yourself and then we'll ask Tony to do the same.
[239.20 --> 239.48]  Okay.
[239.48 --> 239.88]  Yeah.
[240.04 --> 245.62]  So, hey, I'm Timo and I'm a co-founder of an NLP startup in Berlin.
[245.62 --> 250.22]  And I would say a total NLP, a natural language processing geek.
[250.78 --> 263.06]  I studied data science and computational neuroscience and then co-founded the startup DeepSet two years ago in Berlin, which is actually a really great place for a startup.
[263.06 --> 266.20]  A lot of talent coming here.
[266.20 --> 274.26]  And also a lot of the open source companies are based in Berlin, for example, Spacey or maybe, you know, Rasa.
[274.26 --> 277.06]  Yeah, we had Spacey on.
[277.72 --> 279.98]  Spacey on the podcast a little bit ago.
[280.24 --> 283.46]  And yeah, Berlin sounds like quite a place to be a developer.
[283.98 --> 285.58]  I definitely need to make a trip there.
[285.72 --> 287.72]  I was going to say we need a practical AI road trip.
[287.72 --> 288.64]  Exactly.
[289.44 --> 290.28]  Yes, totally.
[290.48 --> 290.66]  Yeah.
[290.78 --> 291.18]  Yeah.
[291.18 --> 293.10]  It's a totally great, vibrant city.
[293.44 --> 296.48]  Of course, nowadays it's a bit more empty and calm.
[296.48 --> 306.16]  When you go, for example, we have a huge airport that got shut down after the change in government.
[307.04 --> 309.62]  And this field is completely empty nowadays.
[310.06 --> 316.14]  And normally it's full of people and a lot of people doing sports or celebrating there.
[316.14 --> 328.78]  But yeah, so at DeepSet, I'm responsible for innovation because we believe that there has been a lot of advancements in deep learning and also natural language processing.
[328.96 --> 331.08]  And this has to be brought to the industry.
[331.56 --> 337.22]  But also what is really important to us is getting NLP technology to work on German language.
[337.48 --> 341.16]  And for this, we are very deeply rooted in open source technology.
[341.16 --> 347.56]  We train on Birch model, like these language models that got open sourced by Google.
[347.96 --> 352.22]  And we trained these on a lot of German text data and also open source to this.
[352.72 --> 356.00]  And this is giving us a lot of traction from the community.
[356.24 --> 359.46]  A lot of researchers, German researchers are using this.
[359.94 --> 365.20]  And yeah, this is just a really great time to contribute to open source projects.
[365.80 --> 366.40]  Awesome.
[366.72 --> 366.96]  Yeah.
[367.02 --> 367.98]  Thanks for the intro.
[367.98 --> 371.12]  Tony, you want to let us know a little bit about your background?
[371.42 --> 373.48]  And how you eventually ended up where you're at now?
[374.06 --> 374.70]  Yeah, absolutely.
[374.88 --> 375.68]  Thanks for having us.
[375.82 --> 376.64]  So I'm Tony Reyna.
[376.80 --> 378.56]  I'm a medical doctor and data scientist.
[378.98 --> 382.38]  And I'm a chief AI architect for health and life sciences at Intel.
[382.96 --> 393.64]  So my primary role is actually taking artificial intelligence algorithms and trying to make them run faster on, well, on Intel products, obviously.
[393.64 --> 397.28]  A lot of what I've been doing has been in the medical imaging space.
[397.60 --> 400.44]  So CTs, MRIs, you know, things like that.
[400.54 --> 405.08]  But been branching out into genomics and particularly natural language processing.
[405.36 --> 406.26]  So the NLP stuff.
[407.06 --> 413.28]  Timo and I kind of first met with some of the German work that he was doing, which I like the playfulness of NLP.
[413.28 --> 426.86]  They name things after Sesame Street characters like Bert and Ernie and Elmo and things like that, which is kind of a fun group to be working with when you work with researchers that really love to have kind of fun things to do.
[426.98 --> 428.50]  Makes the logos a lot better.
[428.86 --> 430.10]  It makes the logos a lot better.
[430.10 --> 431.66]  Nobody forgets Bert now.
[432.80 --> 433.66]  Poor Bert.
[434.18 --> 434.84]  Poor Bert.
[435.00 --> 440.92]  I mean, but, you know, Bert's now like, you know, a world celebrity now in terms of AI researchers.
[441.72 --> 443.66]  But, yeah, no, it's really great.
[443.92 --> 452.62]  And, you know, I mean, Bert's only been a couple years now, maybe even less, that it's been in existence and has just kind of taken the field by storm.
[452.62 --> 464.74]  So, yeah, this project with Timo that we kind of looked at since we were already connected, he just popped up on my LinkedIn page and said, hey, we're doing this COVID question and answer thing.
[465.12 --> 466.14]  We'd love to get some help.
[466.22 --> 468.66]  And I said, well, let's figure out how to help out.
[468.92 --> 481.44]  So that's what we've been doing is obviously we've been really busy in Intel just working, you know, as everybody is around the planet, basically trying to figure out ways we can help with COVID.
[481.44 --> 484.76]  And obviously we're a tech company, so we're not health care.
[484.92 --> 491.48]  We're not going to, you know, be able to go out there and do, you know, magic like, you know, health care providers are doing.
[491.68 --> 493.42]  But, you know, we're going to do what we can.
[493.52 --> 496.06]  And this is one of the ways we think we can really make a difference.
[496.68 --> 496.76]  Yeah.
[497.00 --> 500.30]  You know, this is just such an unprecedented time.
[500.30 --> 510.08]  And as we just for it's moving so fast that for context, for listeners who who are tuning in, we're actually recording this on Tuesday, March 31st.
[510.08 --> 512.20]  And we don't normally say that when we record episodes.
[512.20 --> 518.14]  But given the topic and given how fast this is evolving, I thought that a point in time was worth having.
[518.46 --> 524.96]  Just to set the context and then kind of I'd like to come back over to you, Tony, for a little level setting for us.
[524.96 --> 531.94]  I know that right now we're at a point where there's 203 countries, areas and territories that have COVID-19 cases.
[532.08 --> 538.36]  As of today, the World Health Organization said 754,000 and change.
[538.46 --> 538.86]  Pardon me.
[538.96 --> 541.38]  I'm just to round out the numbers of cases.
[541.38 --> 546.44]  There's almost 37,000 cases around the world that resulted in death.
[546.56 --> 550.72]  In the U.S., we're at 163,500 cases.
[551.14 --> 561.08]  And we are approaching 3,000 deaths, which we may hit today based on the current run rate, which would here in the U.S., which would put us on the same as 9-11 in terms of that.
[561.20 --> 564.38]  So it's a moment in history that none of us have ever experienced.
[564.38 --> 570.44]  There's nothing, I guess, other than maybe the Spanish flu of 1918 that's comparable in any way.
[570.52 --> 572.36]  And I know that has limited comparisons.
[572.62 --> 580.76]  I'm wondering if you can kind of level set, you know, beyond just the numbers that I called out, you know, that are on the websites everyone is following.
[581.28 --> 587.96]  You know, where we are today, what that looks like from your perspective as a medical doctor that's dealing with this.
[588.04 --> 593.00]  And then obviously we'll talk about how we're using data to start attending to these problems that we're facing.
[593.00 --> 599.38]  Yeah, I mean, I think just from the medical aspect, I mean, I haven't practiced in over 20 years, basically.
[599.60 --> 603.58]  So, I mean, I wouldn't be the best person to answer about kind of the clinical things.
[603.80 --> 615.94]  But this is the strangest part of this whole thing is that when people ask me how is it going, all I know is because we're kind of locked down and stay in place and shelter in place, I can tell you how it's going in my house.
[615.94 --> 621.42]  And everything else I get from reading and from, you know, listening to the news and things like that.
[621.42 --> 630.78]  And I think that's what's just kind of curious about this is I feel like I want to be out there and doing things.
[631.46 --> 634.66]  And even my wife's a retired psychiatrist from the Navy.
[634.86 --> 639.72]  And, you know, she was actually even thinking about, you know, should I kind of lend a hand somewhere?
[639.98 --> 641.04]  You know, what can I do?
[641.04 --> 643.38]  And, you know, and I guess that's a great thing.
[643.50 --> 646.58]  But that's also kind of where we're at is everybody wants to help.
[646.66 --> 657.04]  And yet it's this odd situation where, you know, the best thing for most people is just to shelter in place and make sure that we don't, you know, keep spreading things and trying to get it under control.
[657.52 --> 658.54]  That's a great point right there.
[659.22 --> 659.80]  Yeah, definitely.
[659.80 --> 669.54]  And one of the things you mentioned, which really struck a chord with me is the idea that we're all kind of sheltered in place, at least for the most part, a lot of people are.
[669.80 --> 672.12]  And we're getting information from various sources.
[672.48 --> 674.92]  There's so much information swirling around.
[675.32 --> 676.54]  Some of that's recent.
[676.68 --> 677.80]  Some of that's not recent.
[677.98 --> 679.50]  Some of that's from trusted sources.
[679.70 --> 681.72]  Some of it's not from trusted sources.
[682.08 --> 685.64]  We're hearing anecdotes from our friends and family.
[685.90 --> 688.82]  They're hearing things and things are getting passed secondhand.
[688.82 --> 700.50]  Could you talk a little bit, either one of you, about, you know, what you've seen in terms of the spread of accurate information and the problems related to actually information spread and the virus?
[700.88 --> 705.78]  Yeah, I think Timo should go on that because he's definitely the one that started this on trying to get factual information out there.
[706.16 --> 706.66]  Yeah, exactly.
[706.88 --> 715.20]  So, of course, I mean, social media is quite difficult to disassemble, like, really truthful information.
[715.20 --> 719.40]  And this is exactly how we started the Covert QA project.
[719.70 --> 721.06]  It was two weekends ago.
[721.22 --> 726.56]  There was a hackathon organized by the German government and other authorities.
[727.22 --> 733.00]  It was actually a huge event, 45,000 people in one Slack workspace.
[733.36 --> 733.84]  All virtual.
[734.52 --> 734.74]  Yeah.
[734.84 --> 735.18]  All virtual.
[735.18 --> 735.44]  Yeah.
[735.44 --> 739.78]  And all remote and like a beehive buzzing about.
[740.26 --> 745.88]  And part of this hackathon, we decided to focus on getting factual information.
[746.30 --> 756.10]  And that's why we looked at official government pages and already saw quickly that if you look at a single government page, there's not so much information.
[756.10 --> 761.98]  And that the information needs is actually spread across a lot of official pages.
[762.58 --> 771.76]  And this is exactly the birth hour of Covert QA, where we wanted to aggregate these official sources and make them available and searchable in a meaningful way.
[772.28 --> 775.72]  And, yeah, this was during the hackathon two weekends ago.
[775.92 --> 781.90]  And there were about 25 developers just jumping on to this project.
[781.90 --> 787.80]  We were five core developers from DeepSet, worked basically the whole weekend through.
[788.12 --> 799.26]  And with the support of these external people, it was really fun to develop the UI, to develop the backend, develop scrapers, scrape the sides and bring all pieces together.
[800.02 --> 810.12]  And afterwards, after this hackathon, there's also people now interacting, but also people from external coming and wanting to collaborate, wanting to help.
[810.12 --> 817.34]  And this is exactly how we got in contact with Tony and us following on LinkedIn.
[817.68 --> 832.06]  And I think this is the most great part of this project, to have really like a community that is fast, agile, that is not bound to bureaucracy, that there's no improvement processes, like long improvement processes.
[832.06 --> 835.66]  It's just we have a situation and we need to work on it.
[835.82 --> 841.02]  And this could help people actually saving their lives or the lives of their relatives.
[841.02 --> 848.50]  That was the nice thing about, you know, with Timo's group is that DeepSet was already set up to kind of do NLP and do it at scale.
[848.70 --> 856.32]  And so it was one of these things where I knew coming into it that, A, they had something already in like the first weekend that you could work with.
[856.48 --> 860.84]  And B, they had the engineers and they had the data scientists that could make this thing scale.
[860.84 --> 866.82]  So, you know, they really just needed, you know, resources to kind of come in and help them to make it scale.
[866.96 --> 868.66]  But they had the machinery ready to go.
[869.32 --> 882.18]  So I'm curious before we and I want to dive into that machinery here in just a second in terms of like the end goals of COVID QA and its functionality and kind of some of the things under the hood.
[882.18 --> 902.42]  But before we get into that, maybe we could just kind of set a foundation in terms of, you know, after you've kind of looked at what what sources of data are out there, what sources of information are out there, what they're talking about and what people are asking, what what is the sort of information that people really need to know during this time?
[902.42 --> 903.32]  Is it symptoms?
[903.76 --> 908.36]  Is it, you know, best practices for hygiene and handwashing?
[908.36 --> 914.78]  What are you seeing as kind of some of the main pieces of information that really need to get to as many people as possible?
[915.66 --> 916.24]  It depends.
[916.38 --> 919.36]  So I think it's there's two groups that we're getting at with this.
[919.52 --> 922.50]  The first group is just the layperson that's, you know, out there.
[922.50 --> 933.48]  And they're the ones that are going to hit the tool that's as it exists right now, which is, you know, one that basically will sift through a lot of World Health Organization and the CDC kind of FAQs.
[933.48 --> 946.90]  And they're looking for, you know, what's the best way to disinfect, you know, my house or, you know, what's the best way of, you know, washing my hands or, you know, can I eat this or, you know, will this help?
[946.90 --> 948.00]  That's where it is right now.
[948.08 --> 950.58]  So that's kind of the first group of people that would be using this.
[950.78 --> 959.20]  And then what I thought was interesting was coming in to add the second group, which is going to be the researchers that want to look for new things.
[959.20 --> 969.06]  And these are the data scientists and geneticists and physicians and epidemiologists that want to come in and actually do research on COVID and on coronavirus.
[970.02 --> 982.62]  And so one of the things that Tima and I talked about was there was a data set that was released on Kaggle by the Allen Institute, by the White House, NIH, Georgetown, CZI, MSR.
[982.62 --> 985.32]  It was a whole group that put it out called CORD-19.
[985.64 --> 988.56]  It was the Coronavirus Open Research Data Set Challenge.
[989.20 --> 993.54]  And it's something like, I want to say like 25,000 PubMed articles.
[993.78 --> 1005.96]  So these are peer-reviewed, you know, high-quality articles that they basically just as a search on like coronavirus and virus and, you know, and got all the articles basically.
[1005.96 --> 1018.84]  And so the idea was, well, you know, BERT and all of these great models have, you know, things called like extraction AI, where you get to do a question and answer system for this large body of articles.
[1018.84 --> 1024.82]  And so the question would be, you know, when the Kaggle thing went out, it was like, here's a bunch of data.
[1025.26 --> 1027.14]  Can you find interesting things to do with it?
[1027.54 --> 1035.62]  And I thought, well, the first thing you need with a mountain of data is a way to sift through it for actionable, you know, relative data that's actionable.
[1035.62 --> 1041.46]  And, you know, Timo's group had something called Haystack, which was like, you know, trying to sift through a haystack for a needle.
[1041.46 --> 1070.06]  And I thought, what if we take this, we annotate it using like the Stanford question and answer type of models, the squad models, and be able to actually have researchers give a free tool that researchers can go through the core data set and be able to type in random questions that are, you know, things that are not going to be how to wash your hands, but things that are like the beta subunit of the globulin of the such and such, you know, whatever.
[1070.06 --> 1082.42]  And it will actually give you a relevant answer and a few articles, published articles that you can actually look to and go through these 25,000, you know, articles and get the real meat of the issue.
[1082.96 --> 1087.22]  Yeah, I also, I really like this dual use of this project.
[1087.48 --> 1094.44]  And to come back to the question, I think I looked at quite a lot of FAQs for the general public.
[1094.44 --> 1103.06]  There, the most important information is really informing people how corona spreads and how to prevent the spreading.
[1103.28 --> 1113.18]  I think if this is hitting larger cities where people are crowded together, this information needs to be there in the right way and in a trustable way.
[1113.92 --> 1115.32]  I think this is really important.
[1115.32 --> 1118.54]  And then there's dual use for the general public.
[1118.74 --> 1125.34]  And then, as Tony mentioned, for the researchers, this will be incredibly useful to speed up the innovation process.
[1125.34 --> 1139.86]  Hi there.
[1140.20 --> 1143.36]  This is Daniel Whitenack, one of the co-hosts of Practical AI.
[1143.72 --> 1150.56]  And when I'm not working on Practical AI, I'm developing my own AI applications or I'm training teams at other companies.
[1150.56 --> 1155.08]  I've been doing this for over 10 years now and I've trained more than 1,000 people.
[1155.70 --> 1161.44]  Now I'd like to invite you to my new live online training event called AI Classroom.
[1161.94 --> 1169.10]  In AI Classroom, I'm going to teach the practical skills I've learned over the years using the latest open source AI technology.
[1169.64 --> 1176.48]  You will learn both AI theory along with practical hands-on implementations in both PyTorch and TensorFlow.
[1176.48 --> 1192.14]  After attending AI Classroom, you'll be able to understand the latest models, implement your own models and code, train computer vision and NLP models, create model inference servers, and experiment with state-of-the-art methods like reinforcement learning.
[1192.92 --> 1195.22]  AI Classroom is taking place this May.
[1195.68 --> 1202.06]  It'll be taking place live and completely online in a high-quality virtual classroom, so no travel is required.
[1202.06 --> 1208.62]  There will be two cohorts with convenient time zones for Eastern and Western hemispheres, so don't miss out.
[1209.10 --> 1212.96]  Tickets and more information is available at datadan.io.
[1213.40 --> 1215.34]  That's datadan.io.
[1215.86 --> 1218.58]  And early bird pricing lasts until April 3rd.
[1218.76 --> 1220.74]  See you online in AI Classroom.
[1220.74 --> 1248.16]  So, I guess coming out of that and into kind of looking at the next layer, I'm wondering, we've kind of talked about what COVID QA is, and we've kind of talked about it being based on the Chord 19 dataset.
[1248.16 --> 1261.60]  I'm wondering if, at this point, now that everyone has a kind of a sense of what you're trying to accomplish, if you could kind of dive in into specifically what this is that you're putting out there and making available to the public.
[1261.94 --> 1267.02]  And as we get a sense of that, we'll dive into kind of how it works and what's the technology underlying it.
[1267.02 --> 1270.48]  Yeah, let's maybe also best then separate it.
[1271.12 --> 1281.90]  This dual use one for the general public, explain this, go into more detail, and then also the researcher use where we mainly use extractive technology.
[1282.32 --> 1282.70]  Sounds great.
[1283.02 --> 1283.30]  Exactly.
[1283.44 --> 1293.28]  So, for the general public, it is basically matching user searches, user questions, to the questions we crawled from the official FAQ pages.
[1293.28 --> 1305.90]  And the technology is based on open source technology, PyTorch, Hugging Face Transformers, and also our other framework, Haystack, that can basically do question answering at scale.
[1306.54 --> 1310.72]  And we started off with the question matching in a very simple way.
[1310.72 --> 1322.34]  So, basically, we just indexed the questions in Elasticsearch, and incoming queries were then matched with this Elasticsearch index, which is basically just a rule-based matching.
[1322.84 --> 1330.56]  And we thought this is like a good baseline for people to continue working and developing because it's easily extendable to other languages.
[1331.04 --> 1338.06]  Elasticsearch doesn't really care about the language so much that has been inputted, and it is also super fast.
[1338.06 --> 1345.10]  And during the hackathon and the last days, we experimented a lot with BERT-based embeddings.
[1345.94 --> 1358.28]  And if you would just, so BERT is like a language model where you stick in text and you get then a vector representation of basically like VirtueVec was before for words.
[1358.44 --> 1364.76]  It now works on sentence or document level to get like a document representation of it.
[1364.76 --> 1375.20]  And these models, they really don't work so well when you just take the embedding and you compute similarities, like, for example, with a cosine similarity metric.
[1375.42 --> 1377.30]  They don't work so well out of the box.
[1377.52 --> 1383.66]  So, you need to find ways to adjust these language models to suit your needs.
[1383.66 --> 1387.98]  And there we used a really nice library, sentence transformers.
[1388.10 --> 1392.42]  It's from a German NLP laboratory, UKP lab.
[1393.00 --> 1395.56]  Nils Reimers is also a main contributor there.
[1396.04 --> 1402.94]  And this basically takes a BERT model and creates a clone out of it, like a Siamese network.
[1403.08 --> 1405.38]  So, the weights are totally the same.
[1405.38 --> 1408.74]  You stick in the query that the user types in.
[1409.20 --> 1413.58]  And on the other side, you stick in the questions that you have already crawled.
[1414.30 --> 1417.26]  And then you get representations for both.
[1417.64 --> 1420.14]  And then you can compute a similarity metric.
[1420.32 --> 1427.02]  And this whole network is trained end-to-end with exactly these user questions and the questions you have.
[1427.14 --> 1428.98]  And this works really, really great.
[1429.16 --> 1433.68]  Like, the more data you feed into this network, the better it can match questions.
[1433.68 --> 1439.96]  And we've then also seen over the course of the hackathon that this is the way to go.
[1440.36 --> 1450.36]  And we need to extend this also to other languages because the questions from official FAQ pages are phrased in a very official tone.
[1450.78 --> 1457.50]  And people who want to ask questions more right in a colloquial manner or also that they are spelling mistakes.
[1457.74 --> 1461.22]  And these models cover this by part quite well.
[1461.22 --> 1465.70]  And this is why we are actually trying to push in this direction more and more.
[1466.26 --> 1467.72]  So, I'm pretty curious about that.
[1467.84 --> 1475.18]  And Chris could probably guess that I'm very curious about that because of my interest in languages, which we've talked about a lot.
[1475.42 --> 1481.12]  So, you started talking about the sort of Elk stack or Elasticsearch, you know, matching with the index.
[1481.12 --> 1482.40]  And then talked about BERT.
[1482.40 --> 1483.42]  So, I'm curious.
[1483.74 --> 1489.40]  There's, of course, a lot of marginalized language communities out there that also need this sort of information.
[1489.74 --> 1495.36]  And are only becoming even more marginalized because they don't have access to proper health information.
[1495.74 --> 1496.22]  And I'm curious.
[1496.42 --> 1502.70]  So, with that sort of flow that you talked about, you have a language model, let's say, like BERT or a Transformers model.
[1502.70 --> 1508.04]  So, you could train this sort of model assuming you had data in the language.
[1508.56 --> 1513.50]  And then there's this sentence transformers and matching piece that you talked about.
[1513.70 --> 1524.54]  In terms of transitioning that piece and the training of that piece, you mentioned you have kind of your set of scraped questions and then the set of user questions.
[1524.54 --> 1534.70]  Do you need annotation in terms of, you know, matching known user questions to the properly matched FAQ, you know, scraped data?
[1535.02 --> 1537.18]  Is that what you need for that certain piece?
[1537.54 --> 1537.90]  Exactly.
[1538.04 --> 1538.96]  This is exactly right.
[1539.10 --> 1540.80]  And we created manually.
[1541.06 --> 1545.98]  So, the core team distributed a set of like 30 questions.
[1546.12 --> 1551.16]  And we manually created rephrasing of these questions to basically evaluate the models.
[1551.16 --> 1556.00]  But now, we also implemented a feedback mechanism into the UI.
[1556.24 --> 1557.86]  And also, we have a Telegram bot.
[1557.96 --> 1560.10]  And we can maybe talk about the Telegram bot as well later.
[1560.62 --> 1568.08]  And there, people can actually give positive feedback or negative feedback saying that maybe the content is irrelevant.
[1568.76 --> 1570.38]  It doesn't match the question.
[1570.98 --> 1576.64]  Or the content is outdated, for example, to inform us that we have to adjust our scrapers in a way.
[1576.64 --> 1580.66]  And this, we hope, will scale to other languages.
[1580.98 --> 1585.74]  And all the data that is coming from this will be open sourced in this COVID QA repository.
[1586.04 --> 1592.88]  And we'll make this also available to other researchers that they can improve a question matching for COVID-related questions.
[1593.52 --> 1594.38]  This is super cool.
[1594.60 --> 1596.18]  I love what you're doing on this.
[1596.18 --> 1610.82]  I guess one of the things I wanted to ask is maybe as people focused on these technologies and we're doing this day-to-day in our lives, you know, the efforts that we're engaged in in our own projects are built on these data sets that we have.
[1610.82 --> 1621.66]  And yet, as we look at this crisis and we're looking at the fact that the data set may or may not have everything you need, which you kind of alluded to there, you know, in terms of how applicable it is and getting that feedback.
[1621.66 --> 1632.04]  What kind of strategies are you thinking of in terms of being able to provide the outputs that maybe some users are needing if they're not in the CORD-19 data set inherently?
[1632.22 --> 1633.44]  Is that just a limit?
[1633.56 --> 1635.66]  Is that a hard limit of what you can tackle?
[1635.66 --> 1640.94]  Or have you thought about how to extend beyond the limitations of the data set you're working with?
[1642.20 --> 1656.94]  So exactly like this is in the second stage where we have more an extractive QA that takes some unstructured text database like the CORD-19 data set, for example, and then extracts question.
[1656.94 --> 1668.10]  We think that this will be related to researchers, but we could also envision that more text that the general public would be interested could be searchable with this system.
[1668.56 --> 1676.64]  The only problem there is that this extractive QA mechanisms are incredibly hard to scale to a huge amount of users.
[1676.64 --> 1683.90]  So we would possibly do this for the general public in more like an offline way where we collect questions.
[1684.06 --> 1694.44]  And if a lot of questions come up that cannot be answered, we might need to use these extractive QA models to answer them from different data sources.
[1694.44 --> 1707.60]  Yeah, so just to kind of follow up on that, I think that it's worth noting here that I think it's really cool how you've approached this because there is existing sort of question and answer data out there that's from a trusted source.
[1707.60 --> 1712.74]  So let's say FAQ pages from the World Health Organization or something like that.
[1712.82 --> 1725.20]  So in the first case where you're talking about doing this matching with the transformer models, you're actually matching a user query to a trusted source answer for that question because it was posted on an FAQ site.
[1725.20 --> 1737.34]  But then in the second piece where you're just talking about in terms of extractive QA, really now what we're talking about is saying, OK, well, and correct me if I'm wrong, but I think the goal here would be to say, well,
[1737.60 --> 1749.14]  the user isn't asking exactly what's on the FAQ site or maybe the user isn't sort of general public user, but they're a research user.
[1749.52 --> 1760.56]  And like you said, Tony, they want to know a very specific question that's not on like a FAQ site, but it is in some research article or it is on some trusted source page.
[1760.68 --> 1762.86]  So this is like totally unstructured data.
[1762.96 --> 1763.88]  It's just like an article.
[1764.34 --> 1767.26]  And you want to ask some random question about that article.
[1767.60 --> 1772.44]  And that's where, you know, this extractive QA comes in.
[1772.80 --> 1784.28]  Tony, could you maybe comment a little bit about that and how this sort of extractive QA model is maybe different from the sort of embedding matching that we're talking about in the other case?
[1784.96 --> 1785.40]  Yeah, sure.
[1785.40 --> 1790.24]  So, I mean, the way these models, you know, typically work, they talk about a language model.
[1790.48 --> 1793.86]  You know, I usually think of it, you know, it's learning the statistics of a language.
[1793.86 --> 1817.22]  So, you know, it's effectively like learning I before E except after C or learning that, you know, if the way I kind of go over it is if, you know, if the Dewey decimal system is this random alphanumeric number system, but, you know, you give it to any librarian and they're able to take very different books and be able to basically place them correctly in a library in an ordered kind of structure.
[1817.22 --> 1820.00]  And so a lot of these models are doing the same thing.
[1820.16 --> 1827.12]  They're basically just looking at patterns of word co-occurrences and, you know, the statistics of how words occur.
[1827.12 --> 1839.26]  And what we're trying to do here is for the models that have already been trained, they're usually trained on things like Wikipedia or, you know, English language, German language, text, which is great.
[1839.26 --> 1845.14]  But for these sorts of things, you really want to get into the domain specific terms.
[1845.34 --> 1857.34]  So the medical terms, the genomics terms, the more difficult and more infrequent terms that won't be showing up in Wikipedia and trying to learn the statistics of that data set.
[1857.34 --> 1867.58]  So they have existing things like Cybert and BioBert, which are BERT models that are built using things like the BioASQ data set.
[1868.32 --> 1878.34]  And so, you know, Timo and I kind of had talked and we said, you know, what if we took the CORD-19 data set, which is, you know, supposedly we've looked at it now.
[1878.50 --> 1883.40]  There are mostly coronavirus articles, but there are lots of other articles as well in there.
[1883.40 --> 1888.12]  So the first, you know, rule of data science, the data is always going to be dirty, you know, coming in.
[1888.24 --> 1893.38]  So what we did is we said, I'm an MD and Intel has a lot of, you know, contacts.
[1893.50 --> 1910.82]  And so I contacted people from the American Medical Association and people that I knew and just basically put out a call and said, hey, could we get some domain experts, physicians, nurses, PhDs in biosciences, people that are probably in some cases sitting at home.
[1910.82 --> 1916.34]  And I heard on the radio that third and fourth year medical students, you know, are being told to kind of stay home.
[1916.68 --> 1918.62]  And I was a third year medical student.
[1918.78 --> 1921.46]  I mean, I know how difficult it is.
[1921.52 --> 1922.30]  You want to be there.
[1922.40 --> 1923.48]  You want to be doing something.
[1923.68 --> 1929.46]  You're incredibly intelligent and you have all of these, you know, skills that you've spent the last two years doing.
[1930.14 --> 1932.74]  So I just put out a call and we set up a Slack channel.
[1933.26 --> 1938.04]  And Timo's group had, you know, DeepSet had this annotation server.
[1938.04 --> 1947.50]  So we put up this core data set and it's essentially the Slack channel allows, I think we've got, we've got like 24 on the Slack channel right now.
[1947.60 --> 1949.86]  We just, we just started yesterday on the annotation.
[1950.26 --> 1955.82]  And we've, right now we've got over a hundred question answers off the data set just in the, in the first day.
[1956.42 --> 1961.14]  And so these are things like, you know, I'll read you some of the ones that I'm looking at now from, from the website.
[1961.36 --> 1965.00]  You know, how many amino acids are in the SARS-CoV protein?
[1965.26 --> 1967.34]  And the answer is 76 amino acids.
[1967.34 --> 1971.92]  And so this is something where, you know, Wikipedia is not going to be able to get you there.
[1972.42 --> 1973.98]  These are directly from the articles.
[1974.18 --> 1977.16]  It has a link back to the article that you're, you're talking about.
[1977.32 --> 1982.60]  Things like what does the SARS-CoV protein activate NLRP3 inflammasome?
[1982.78 --> 1994.60]  Again, very, very detailed kind of question and answer things that are either specific to viruses or specific to epidemiology or specific to SARS itself or, or COVID or MERS.
[1994.60 --> 1998.22]  Or any of these kind of similar pandemics that we've, that we've seen.
[1998.52 --> 2004.36]  And the nice thing for the domain experts is they just log into a website.
[2004.52 --> 2007.10]  All they need is a web browser and an internet connection.
[2007.10 --> 2009.92]  And as long as they can highlight some text, they're good to go.
[2009.92 --> 2015.44]  And so we just throw them at it, give them, you know, some walkthrough videos and let them go away and annotate.
[2015.44 --> 2028.38]  I'm kind of curious as you're talking about the specifics of amino acids and such as the, I know that China had done a complete genome of this virus fairly early on and published it.
[2028.56 --> 2029.34]  Have you been using that?
[2029.42 --> 2030.16]  Has that been helpful?
[2030.16 --> 2034.26]  And has that informed any of the work that you guys have been doing in the project here?
[2034.98 --> 2035.72]  Not for us.
[2035.72 --> 2043.16]  So what we've got so far are just the published articles that were on like PubMed that were pushed into the, to the core data set.
[2043.24 --> 2045.78]  But it's certainly something that we could add into, into things.
[2045.78 --> 2054.22]  So kind of the mechanics of how these question and answer systems work is that it's kind of the, the annotator kind of goes backwards from the model.
[2054.36 --> 2056.62]  The annotator reads through the article.
[2056.94 --> 2059.66]  So this is a published, you know, peer reviewed article.
[2059.66 --> 2063.14]  And the annotator comes across a certain fact and they say, that's interesting.
[2063.30 --> 2065.40]  That's something, you know, that's specific.
[2065.64 --> 2066.48]  That might be interesting.
[2066.84 --> 2073.72]  So they highlight it and they click question and they make up a question based off of the highlighted text in the article.
[2073.92 --> 2085.14]  So if they had the genomic sequence or something like that, they could certainly, you know, if that were in the, in the text article, that's something that they could definitely highlight and make up a question to.
[2085.14 --> 2098.28]  And then the great thing about this is, you know, on Timo's side, when he, you know, creates an extractive AI model for it, it can actually extrapolate and then say, okay, I, I understand the context and the statistics.
[2098.28 --> 2111.40]  And so if you threw me a new question that wasn't something that the annotators had ever come up with, it should be able to do a pretty decent job at kind of figuring out what it it's looking for in that article.
[2111.40 --> 2119.58]  So if I put up a brand new article, if I put up a genomics article to this website and ask some questions, it should know where to look for in the text.
[2119.64 --> 2123.24]  And that's what's coming back is the model is not just making up words.
[2123.24 --> 2128.34]  It's identifying, it's highlighting the text and saying, here's the highlighted answer in the text.
[2128.50 --> 2129.78]  Does this seem right to you?
[2129.78 --> 2140.40]  The changelog is deep discussions in and around the world of software.
[2140.40 --> 2142.36]  And it's been going for over a decade.
[2142.62 --> 2145.96]  We interview hackers like Chris Anderson from 3D Robotics.
[2146.42 --> 2150.94]  At the time, drones were like predators and global hawks and military industrial.
[2151.08 --> 2154.86]  And they were classified and super, you know, $10 billion things.
[2154.86 --> 2161.04]  And we had just built a drone with Lego pieces around the dining room table programmed by a nine-year-old.
[2161.26 --> 2163.54]  And it's like, OK, that should not be possible.
[2163.84 --> 2174.82]  You know, when a nine-year-old can do something that is classified, that literally export control as ammunition with Lego, with toy pieces, it was something important in this world has changed.
[2175.92 --> 2177.90]  Leaders like Devin Zugel from GitHub.
[2177.90 --> 2186.52]  In the, like, 10 to 15-year range or 20-year range, what I would really like is for if you have, like, three 12-year-olds hanging out.
[2186.72 --> 2188.54]  And one of them's like, I want to be a firefighter.
[2188.62 --> 2190.18]  Another one's like, I want to be a lawyer.
[2190.32 --> 2192.66]  I want one of them to say that I want to be an open source developer.
[2193.28 --> 2194.94]  And innovators like Amal Hussein.
[2195.48 --> 2198.68]  I've yet to kind of see applications at scale that don't use multiple languages.
[2198.96 --> 2204.74]  That don't have just arcane stories behind why this weirdo thing exists, you know?
[2204.74 --> 2210.16]  Like, all right, when you open this file, you're going to have to turn around three times and tap your nose once.
[2212.66 --> 2215.86]  Like, it's just the most hilarious stories, you know?
[2215.98 --> 2218.12]  But applications are living, breathing.
[2218.46 --> 2219.62]  They have craft.
[2220.00 --> 2221.08]  That's normal.
[2221.34 --> 2227.56]  So I want to normalize weirdness because that's just how applications evolve over time.
[2228.02 --> 2229.74]  Welcome to the changelog.
[2230.06 --> 2234.10]  Please listen to an episode from our catalog that interests you and subscribe today.
[2234.10 --> 2235.68]  We'd love to have you with us.
[2246.76 --> 2253.16]  So we've kind of talked about the QA annotation that Tony has kind of helped spin up
[2253.16 --> 2258.76]  and really utilizing that expert input from doctors, from medical students,
[2258.94 --> 2261.96]  from medical professionals on the CORD-19 dataset.
[2261.96 --> 2268.42]  I was curious to kind of push that back to you, Timo, and see what your thoughts are in terms of,
[2268.76 --> 2272.00]  let's say that Tony was able to get all this annotation in place,
[2272.04 --> 2274.00]  and it sounds like there's a great start on that.
[2274.56 --> 2280.32]  How do you see that being integrated into the COVID QA system itself?
[2280.44 --> 2285.88]  And maybe how do you see, you know, the two sides of the COVID QA system developing?
[2285.88 --> 2287.36]  Yeah, exactly.
[2287.44 --> 2287.96]  Good question.
[2288.18 --> 2293.18]  So I would say it starts with a scale of data that is needed.
[2293.42 --> 2298.92]  So for this question matching, we can either use already pre-existing external data sets,
[2299.08 --> 2303.66]  and then this matched questions, maybe 1,000 or 2,000 per language.
[2303.82 --> 2307.08]  This is enough to get a really good matching system already going.
[2307.08 --> 2312.44]  But for this extractive question answering, there's much, much more help needed.
[2312.68 --> 2320.68]  The scales are there, like this common data sets squad from Stanford is in 150,000 question answer pairs are there.
[2321.12 --> 2325.62]  And that's why we think it's really great to have external help,
[2325.82 --> 2332.18]  because this will be the largest level, getting this data in a format that we can then use in the frameworks.
[2332.18 --> 2340.62]  This framework, we actually use a haystack, which is basically enabling question answering on a larger scale.
[2340.94 --> 2347.92]  So normally, if you just use a language model like BERT, you basically take a paragraph, a small paragraph,
[2348.20 --> 2353.10]  like maybe 2,000 or 3,000 characters, and you ask a question and you compute this.
[2353.56 --> 2357.42]  But for a large document base, this would be very infeasible.
[2357.62 --> 2360.42]  And then you need a two-stage process.
[2360.42 --> 2368.14]  In the first stage, you pre-select documents that could be relevant with a very cheap and very fast solution.
[2368.66 --> 2371.34]  And then you apply more power for models like BERT.
[2371.72 --> 2375.82]  And this is definitely not a real, it's definitely not a new invention.
[2376.34 --> 2379.22]  For example, there's a framework out from Facebook.
[2379.46 --> 2380.82]  It's called Dr. QA.
[2381.14 --> 2385.42]  This is exactly doing this retriever and then reader architecture.
[2385.42 --> 2393.88]  But haystack is doing it in a bit more modular way and modern way with a BERT-based extractive question answering system.
[2394.38 --> 2397.44]  And we think there's a huge gain in performance.
[2397.94 --> 2412.42]  And so we can take these labels that Tony and the collaborators produce and stick them into frameworks to train end-to-end systems that answer questions on this large COD-19 dataset.
[2412.42 --> 2416.02]  So I'm curious, you mentioned kind of the scale of the data.
[2416.36 --> 2422.20]  And, you know, as we've, SIL has been working to get translations in place over the past days.
[2422.30 --> 2427.36]  Definitely, you know, translations in the thousands seem, you know, within reach.
[2428.02 --> 2433.42]  Annotations in the hundreds of thousands is definitely a tough thing, especially when you're relying on experts.
[2433.42 --> 2440.42]  But I was wondering if you could speak to, you know, I know some of these sort of domain-adapted models.
[2441.40 --> 2443.44]  So Cybert's or other ones.
[2443.58 --> 2447.34]  Do I have it right that those are transfer learned from another model?
[2447.42 --> 2453.26]  So, like, if you have a model trained on the SQAID dataset for question and answer, which is totally general domain,
[2453.26 --> 2461.14]  is it possible to then transfer learn a domain-adapted question-answer model with the data that Tony's working on?
[2461.76 --> 2464.44]  So it's a little bit different.
[2464.94 --> 2469.74]  You have to separate a base language model that can just transform text to vectors.
[2469.74 --> 2476.44]  And then you have to take this language model and adjust it to suit your task at hand.
[2476.54 --> 2483.18]  For example, document classification or extraction of named entities like persons and cities.
[2483.76 --> 2485.30]  And also question-answering.
[2485.38 --> 2491.92]  You have to attach a prediction head, so another small neural network on top of this language model,
[2492.10 --> 2496.52]  and then train this whole joint network on this target task.
[2496.52 --> 2503.86]  And models like Cybert or BioBird, they are just pre-trained on a large biomedical corpus.
[2504.30 --> 2510.82]  What we are also doing right now is we took a BIRT on English data and adjusted it,
[2510.96 --> 2517.42]  because this process of adjusting this language model to a domain is not that computationally expensive
[2517.42 --> 2520.00]  as, for example, training the whole network from scratch.
[2520.36 --> 2524.34]  So we took this network, adjusted it to the COD-19 dataset,
[2524.34 --> 2528.54]  and if we take this adjusted COD-19 bird, let's call it like that,
[2528.86 --> 2533.44]  and stick in the data, the labels, the question-answering labels,
[2533.86 --> 2539.16]  it will hopefully perform better than just a plain BIRT trained on English.
[2539.76 --> 2542.00]  So, you know, I guess, how would it be useful?
[2542.12 --> 2545.46]  Would it be useful to get more annotators involved in this?
[2545.46 --> 2552.84]  And if so, what types of skills do you need with annotators to make it useful for them to apply annotations to the dataset?
[2553.18 --> 2556.14]  Who can do that, and how many more people would be helpful?
[2557.10 --> 2558.66]  As many more as possible.
[2559.36 --> 2560.48]  I had a feeling.
[2560.56 --> 2561.16]  It was the simple answer.
[2561.88 --> 2568.14]  What we're primarily looking for are people that are kind of master's level or above in the biomedical sciences.
[2568.14 --> 2571.96]  So, I mean, you don't have to have a PhD to do this,
[2572.08 --> 2576.78]  but I would like to see someone who is comfortable in reading an academic paper
[2576.78 --> 2581.96]  and being able to explain it to someone else or be able to point out the salient points.
[2582.42 --> 2587.20]  Some of the other things that are useful, even if you're not one of those expert annotators
[2587.20 --> 2591.42]  or you're not sure if you're an expert annotator, are just proofreaders.
[2591.74 --> 2595.18]  So we've got on the Slack channel a sub-channel called Second Opinion,
[2595.32 --> 2596.58]  you know, just like the medical jargon.
[2596.58 --> 2601.46]  And so Second Opinion is where we have somebody that just is looking through the current answers
[2601.46 --> 2603.50]  and the current question and answers and going,
[2604.06 --> 2609.66]  hmm, I wonder if that seems quite right because that doesn't seem to make sense to me.
[2609.76 --> 2615.90]  And so they'll put it up and say, hey, you know, question and answer, you know, 234 is kind of weird.
[2616.02 --> 2618.36]  You know, can I talk to the person who annotated that?
[2618.40 --> 2622.10]  Or can I talk to somebody else who might be able to give us a yay or nay,
[2622.28 --> 2624.22]  whether that's a good annotation or not?
[2624.22 --> 2626.20]  So things like that are always useful.
[2626.20 --> 2629.86]  And I'm getting good response so far, but I'd love to always get more.
[2630.32 --> 2635.02]  You know, as we talked in the beginning, just people that are kind of at home trying to figure
[2635.02 --> 2636.00]  out things to do.
[2636.34 --> 2640.66]  Again, you know, we've got geneticists who might not be doing anything right now.
[2640.74 --> 2645.46]  We've got people with, you know, biochemistry degrees that maybe they're not doing anything
[2645.46 --> 2650.30]  right now, you know, or maybe they're grad students or, you know, perfectly, you know,
[2650.34 --> 2652.86]  would love to talk to them and try to onboard them for this.
[2652.86 --> 2655.92]  So if you have an internet connection and know how to use a web browser, you're set.
[2656.58 --> 2659.04]  I have a daughter who's a third year med student.
[2659.30 --> 2659.54]  So I'm definitely going to...
[2659.54 --> 2659.98]  Oh, perfect.
[2660.24 --> 2661.96]  Have her contact me.
[2662.08 --> 2662.40]  Absolutely.
[2662.52 --> 2663.44]  We'll get her going today.
[2663.72 --> 2665.22]  I'm definitely going to bring it to her attention.
[2665.42 --> 2665.48]  Yeah.
[2665.52 --> 2668.52]  We made it 25 at least on this goal.
[2668.52 --> 2668.82]  Excellent.
[2668.92 --> 2669.84]  We made it to 25.
[2670.06 --> 2670.36]  We're good.
[2670.36 --> 2677.34]  And what's the best way for those sorts of people to contact the effort and get onboarded?
[2677.42 --> 2681.80]  Is it the best way through the GitHub repo or is there another way to do that?
[2682.42 --> 2682.60]  Yeah.
[2682.68 --> 2685.24]  So for the programmer, it's the GitHub repo.
[2685.24 --> 2688.28]  And then for the domain expert, it's probably going to be the Slack channel.
[2688.48 --> 2690.90]  And we can put the Slack channel up on the site.
[2690.90 --> 2695.90]  And we're kind of keeping those two communities kind of separated so one doesn't get freaked
[2695.90 --> 2696.66]  out by the other.
[2696.88 --> 2701.90]  So we'll keep the coders on one side and the biologics on the other side.
[2702.00 --> 2705.68]  And we can also add that into the show notes, which I think is what Daniel was about to say
[2705.68 --> 2705.92]  there.
[2706.10 --> 2708.80]  That way it makes it easy for them to slide through to those.
[2709.00 --> 2709.06]  Yeah.
[2709.12 --> 2709.64]  To click on it.
[2709.68 --> 2709.80]  Yeah.
[2710.34 --> 2710.58]  Yeah.
[2710.58 --> 2713.58]  We'll definitely get the Slack team added to the show notes.
[2713.66 --> 2717.00]  So if you're listening and you want to be involved in the annotation, take a look at
[2717.00 --> 2718.90]  those show notes and make sure you reach out.
[2718.90 --> 2721.72]  I was curious on the kind of circling back.
[2721.94 --> 2728.58]  So that's a great way to contribute from the research user side of things in terms of
[2728.58 --> 2733.42]  scaling up the general public use case of COVID QA.
[2733.62 --> 2737.74]  It sounds like there's definitely still some needs there around language support.
[2738.00 --> 2743.18]  And maybe that has to do with, so maybe Timo, you could mention what would be best to add
[2743.18 --> 2747.50]  there in terms, maybe it's scraping more information, more FAQs or adding them.
[2747.50 --> 2753.02]  And then also on the development side, where are your biggest needs right now in terms of
[2753.02 --> 2757.86]  making COVID QA really useful for the general public?
[2758.02 --> 2762.68]  What are some needs that you have, whether that's front end development, maybe not even
[2762.68 --> 2764.78]  AI related, or maybe it is AI related?
[2765.28 --> 2770.52]  I'm really great that we are separating labeling process and developing process because it will
[2770.52 --> 2772.04]  get super complicated.
[2772.04 --> 2780.68]  And I also wanted to thank Tony that he's taking also a lot of initiative for supervising and
[2780.68 --> 2786.78]  pushing the label process because I think I have never heard of an open source labeling
[2786.78 --> 2787.26]  process.
[2787.50 --> 2792.16]  And I think this will be a mess at some point and it will be very complicated to interact
[2792.16 --> 2795.06]  and also to supervise the quality of the labels.
[2795.06 --> 2798.14]  But I think this is the great part of this challenge.
[2798.26 --> 2800.38]  We just have to try and have to make it work.
[2800.72 --> 2803.40]  So this is really great on the labeling part.
[2803.60 --> 2809.38]  On the development part for computer scientists of any sorts, there's a lot of help needed.
[2809.60 --> 2811.90]  So this is just a hackathon project.
[2812.12 --> 2815.84]  It's not like a full-fledged professional industry solution.
[2816.00 --> 2817.12]  So we need a lot of help.
[2817.12 --> 2823.50]  I'm in contact actually with a data scientist also from Intel through a contact from Tony.
[2823.98 --> 2826.76]  And she's working on an intelligent scraper.
[2827.02 --> 2832.74]  So right now we have very manual scraping processes for each page that adjusts to the
[2832.74 --> 2833.80]  HTML structure.
[2834.34 --> 2840.00]  And we would need a more intelligent scraper that you can just point to a FAQ page and it
[2840.00 --> 2843.54]  automatically extracts questions and the answers.
[2843.54 --> 2848.48]  Of course, there will be errors, but I mean, this is a little bit unavoidable.
[2848.62 --> 2851.48]  Maybe we can do a review process there afterwards.
[2851.86 --> 2855.20]  So this intelligent scraping will be extremely helpful.
[2855.86 --> 2861.08]  And then you also mentioned then that bringing this question matching to other languages.
[2861.56 --> 2868.00]  This is something that is personally very important to me because I think this will create
[2868.00 --> 2870.66]  the biggest societal impact.
[2870.66 --> 2877.20]  And there's a lot to do because for now we have the question matching algorithm with sentence
[2877.20 --> 2883.12]  transformers and BERT just implemented for English, but making this work for other languages
[2883.12 --> 2888.66]  with multilingual language models, for example, with this cross-lingual language model open
[2888.66 --> 2890.34]  sourced by Facebook, for example.
[2890.74 --> 2894.44]  This would improve the experience a lot.
[2894.44 --> 2896.72]  And this on the modeling side.
[2896.72 --> 2902.02]  And then also a huge help we need on getting this actually to people.
[2902.40 --> 2906.58]  And after the hackathon, we got contacted by a person.
[2906.80 --> 2910.38]  I don't even know his or her personal name.
[2910.46 --> 2912.18]  It's the Apache 64.
[2912.86 --> 2917.08]  And this person just programmed a Telegram integration.
[2917.08 --> 2923.74]  So this service has an API where it can match questions and you can call this API.
[2924.34 --> 2926.54]  And he integrated this into Telegram.
[2926.74 --> 2929.60]  And this bot is just, yeah, it's working.
[2929.80 --> 2935.52]  Also, he integrated the feedback mechanism to feedback the user information back into our
[2935.52 --> 2935.84]  system.
[2936.04 --> 2938.04]  So this help is really appreciated.
[2938.04 --> 2943.02]  But what I think could be important there would be maybe a WhatsApp integration.
[2943.58 --> 2949.58]  And maybe even if we extend this really to low resource languages where people might not
[2949.58 --> 2955.18]  have access to mobile phones with internet, maybe have like a text message interaction.
[2955.36 --> 2959.90]  But this would be a little bit further away, I would say.
[2959.90 --> 2965.20]  So I guess as we get toward the end here, I want to ask a question.
[2965.50 --> 2969.44]  And I'd like each of you to give me your perspective since you're coming from two different
[2969.44 --> 2970.40]  places on it.
[2970.42 --> 2977.28]  As we look, we're in this global crisis, which is unique and has stressed all of us and forced
[2977.28 --> 2981.24]  us to think creatively in ways that we have just never done before.
[2981.54 --> 2984.24]  It's sort of like living in a science fiction novel to some degree.
[2984.24 --> 2989.46]  And so as you guys are looking at the role of artificial intelligence that the world,
[2989.46 --> 2995.78]  within the world, and we're looking at suddenly we have this crisis upon us, how do you see
[2995.78 --> 3001.80]  artificial intelligence technologies and data technologies impacting our way through this
[3001.80 --> 3006.72]  crisis at large, not just the project that you're in, but its kind of role in the larger
[3006.72 --> 3007.08]  world?
[3007.38 --> 3011.62]  How has your perspective possibly changed over the last few weeks with regard to that?
[3011.62 --> 3016.18]  And what opportunities do you see as the most exciting, you know, in terms of the path
[3016.18 --> 3019.80]  forward now that you are involved in this and seeing the results that you are?
[3020.20 --> 3021.10]  Timo, you want to go first?
[3021.96 --> 3022.60]  Yes, totally.
[3022.86 --> 3031.20]  So I would say this will like large in the way corporates contribute to like a solution
[3031.20 --> 3033.24]  that is helpful for everybody.
[3033.24 --> 3040.02]  For example, DeepMind has announced quite early solution where they basically analyze the
[3040.02 --> 3043.60]  molecular structure with reinforcement learning.
[3043.60 --> 3050.42]  And if basically through interdisciplinary collaboration that is now made much, much more
[3050.42 --> 3056.02]  possible and less bureaucratic and very fast and agile, I think a lot of great solutions
[3056.02 --> 3056.76]  can emerge.
[3057.40 --> 3065.02]  And I also think that a lot of corporations give their employees actually some dedicated time
[3065.02 --> 3066.32]  to work on these solutions.
[3066.32 --> 3072.96]  So like a collective effort of everybody around the world to work on something that is not
[3072.96 --> 3077.94]  directly related to making profits, but to solving this crisis.
[3078.12 --> 3081.84]  And I think this is something unique, as you said, it's like a unique situation.
[3082.42 --> 3088.98]  And yeah, it will hopefully make people collaborate a little bit closer on things that are relevant
[3088.98 --> 3089.70]  for society.
[3090.36 --> 3090.48]  Yeah.
[3090.58 --> 3095.06]  So I love what Timo said about, you know, trying to do things that are relevant to society.
[3095.06 --> 3100.20]  And I'm not an official Intel speaker or so, but I can tell you that, you know, we're very
[3100.20 --> 3104.08]  creative people and we're allowed to do a lot of, you know, things kind of what interests
[3104.08 --> 3107.16]  us in addition to our usual, you know, what pays the bills.
[3107.32 --> 3111.66]  This has actually been kind of interesting that now the things that are interesting, the
[3111.66 --> 3117.12]  whole company and in fact, the whole, you know, world basically now all the extra stuff
[3117.12 --> 3119.40]  is now going toward what can I actually do?
[3119.40 --> 3125.04]  In terms of the AI stuff, I mean, I kind of go back to, you know, we're sheltering in
[3125.04 --> 3129.34]  place and we're trying to get through, you know, kind of the scale without being connected
[3129.34 --> 3134.26]  and somehow AI is kind of helping us to get through the mountain of data that's coming
[3134.26 --> 3139.06]  in and trying to maybe focus us a little bit better.
[3139.22 --> 3143.00]  I mean, it's designed to be a tool, you know, it's not designed to replace anything.
[3143.00 --> 3148.48]  It's just, it's designed to be a really, really nice way of sharpening the edge to figure out
[3148.48 --> 3150.88]  exactly what we want to do and what's possible.
[3151.14 --> 3153.00]  So that's where I see AI coming in.
[3153.82 --> 3153.86]  Awesome.
[3154.04 --> 3157.76]  Well, we appreciate you both taking time to join us today.
[3157.90 --> 3160.90]  I know that especially during this time, there's a lot to work on.
[3161.02 --> 3162.36]  So thank you for taking time.
[3162.52 --> 3168.40]  And definitely if you're listening out there and you are wanting to contribute in a positive
[3168.40 --> 3174.22]  way, using your development skills, using your AI skills, using your health knowledge
[3174.22 --> 3177.52]  and your medical expertise, please check out this project.
[3177.70 --> 3181.04]  The links are in the show notes and reach out as well.
[3181.14 --> 3186.20]  If you're having trouble figuring out how to get connected, there's our Slack team as
[3186.20 --> 3189.38]  well, which you can find at changelog.com slash community.
[3189.46 --> 3194.70]  And we're happy to get you connected to Timo and or Tony and their team.
[3194.82 --> 3197.76]  So just make sure you get connected and contribute.
[3197.76 --> 3200.98]  And thank you both Timo and Tony for joining us.
[3201.04 --> 3201.78]  Really appreciate it.
[3202.02 --> 3202.38]  Thanks, Dan.
[3202.48 --> 3202.90]  Thanks, Chris.
[3203.12 --> 3203.34]  Yeah.
[3203.56 --> 3204.04]  Be safe.
[3204.12 --> 3204.58]  Stay healthy.
[3204.72 --> 3205.64]  Thanks for inviting us.
[3205.90 --> 3206.00]  Yeah.
[3209.48 --> 3212.20]  Thank you for listening to this episode of Practical AI.
[3212.88 --> 3216.54]  More like this at changelog.com slash practical AI.
[3217.06 --> 3221.86]  There you'll find our latest as well as lists of our most popular episodes and the ones we
[3221.86 --> 3222.28]  recommend.
[3222.62 --> 3226.46]  If this show has helped you on your AI journey, please leave us a five-star review on Apple
[3226.46 --> 3231.88]  Podcasts, part us on Spotify, star us on Overcast, and tell a friend what they're missing out
[3231.88 --> 3232.10]  on.
[3232.34 --> 3235.20]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[3235.36 --> 3236.84]  It's produced by me, Jared Santo.
[3237.06 --> 3239.56]  And our music is brought to you by the Beat Freak, Breakmaster Cylinder.
[3240.08 --> 3241.26]  We have awesome sponsors.
[3241.40 --> 3242.12]  Please support them.
[3242.18 --> 3242.84]  They support us.
[3242.84 --> 3245.14]  Thanks again to Fastly, Linode, and Rollbar.
[3245.60 --> 3246.44]  That's all for now.
[3246.76 --> 3247.72]  We'll talk to you next time.
[3247.72 --> 3249.50]  Peace.
[3252.44 --> 3273.48]  Our
