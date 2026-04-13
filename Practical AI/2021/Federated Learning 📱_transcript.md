[0.00 --> 26.46]  Federated learning is not new. This is not a new topic, but we're seeing what I think is a real shift right now into trying to find a better solution into being able to have a central model that is decentrally trained. I think both the need is there. Other approaches are effective in some ways, but also have some deficiencies. And the technology from an implementation standpoint has finally arrived with federated learning.
[26.46 --> 32.02]  So we're starting to see a lot of different implementation paths at this point from vendors and various frameworks.
[56.46 --> 72.00]  And start building smart customer data pipelines. Rudderstack is warehouse first. No more silos. Rudderstack builds your customer data lake on your data warehouse, not theirs, enabling all functionality of a CDP with more security and retaining full ownership of your data.
[72.00 --> 94.38]  It's open source and API first. Rudderstack can be easily integrated into your existing development processes. And because they're open source, you can see all their code. So you don't have to worry about vendor lock in or black boxes. And best of all, they have transparent pricing. Stop paying your CDP a premium to store your data. Rudderstack is free up to 500,000 events and pricing scales transparently from there.
[94.38 --> 103.10]  Learn more and get started at Rudderstack.com. Again, Rudderstack.com. That's R-U-D-D-E-R-S-T-A-C-K.com.
[112.86 --> 119.96]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[119.96 --> 124.38]  This is where conversations around AI, machine learning, and data science happen.
[124.64 --> 132.48]  Join the community and Slack with us around various topics of the show at Cangshaw.com slash community and follow us on Twitter. We're at Practical AI FM.
[138.84 --> 144.40]  Welcome to another fully connected episode of the Practical AI podcast.
[144.40 --> 151.38]  This is where Chris and I keep you fully connected with everything that's happening in the AI community.
[151.58 --> 161.52]  We'll take some time to discuss some of the latest AI topics and news, and then we'll dig into some learning resources to help you level up your machine learning game.
[162.04 --> 172.18]  I'm Daniel Whitenack. I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson, who is a strategist at Lockheed Martin.
[172.60 --> 173.28]  How are you doing, Chris?
[173.28 --> 177.24]  Doing very well, Daniel. Looking forward to having a good conversation between the two of us.
[177.36 --> 181.64]  No guests today, so we're just going to have to do something ourselves here, man.
[181.82 --> 191.26]  No guests. Yeah, and it is, you know, whenever we do these fully connected episodes, we try to take a look at, you know, what's trending in the AI world.
[191.54 --> 200.00]  One of those things is privacy and security concerns as related to AI systems.
[200.00 --> 204.98]  I don't know, before we jump into the topic for today, which impacts those areas.
[205.14 --> 211.00]  So we're going to talk today about federated learning, which is a sort of recent trend that we're seeing.
[211.16 --> 221.22]  Before we jump into that, do you want to say anything about, I know you've done some more deep thinking about some of the kind of ethics concerns and bias and privacy type things.
[221.22 --> 229.28]  What are you seeing in recent days as related to that and how are companies, you know, are companies taking that seriously?
[229.80 --> 232.78]  What are companies thinking about in regard to that?
[232.78 --> 243.82]  Well, I think what I've observed is that, and it's a little bit of a mixture of all these things, so that it's kind of a, there's a whole bunch of influences that are affecting the way companies are thinking.
[244.14 --> 245.64]  And a lot of those are legal.
[245.64 --> 248.18]  It's, you know, where is your data located?
[248.40 --> 255.50]  Moving across national boundaries, even though it's, you know, electronic is a big deal because of the laws.
[255.50 --> 268.14]  Things like the war on terror, the global war on terror created sets of laws to support that, and that's now having unexpected consequences on how different countries want to share data down the road here.
[268.28 --> 280.66]  You know, in 2021, even though we're kind of moving past that era, we have a mix mash of different laws in different countries, some of which have a little bit more thought and strength behind them, some of which don't.
[280.66 --> 290.48]  And here in the U.S. where we are, there are some laws that other countries are very wary of, of having their data here in the U.S. based on what that is.
[290.48 --> 298.54]  And so I've seen there are so many factors now that are playing into this, and many of, some of them you would expect, and some of them were kind of unintentional.
[298.54 --> 313.30]  But it's leaving us in a moment where, you know, going back to the topic, we've seen federated learning on the rise lately as a possible solution to some of these issues, or at least, you know, a good way to tackle it, the best option available right now.
[313.64 --> 319.06]  Yeah, I think everyone that's working in this space is encountering issues around ethics and privacy.
[319.06 --> 342.16]  In my space, in the NLP space recently, one of the AI ethics pioneers, Margaret Mitchell, she joined the Hugging Face team, which is, of course, the sort of darling of the NLP community right now, and is developing sort of a five-year plan around open source AI at Hugging Face and the ethics around that and what privacy and bias and all of those concerns are.
[342.16 --> 371.88]  And we're starting to see more, of course, around the data side as well, and people, as they're releasing their models, and they're putting their results on, like, leaderboards and such, there's a sort of general call to provide, like, model cards and such with those, like, describing a bit more about the model, what data was trained on, and some, you know, more details about the statistics around the data, bias in the data, all of that, which kind of goes along with releasing
[372.16 --> 373.16]  these models.
[373.16 --> 375.16]  So it's definitely, it's definitely a trend.
[375.16 --> 376.16]  Transparency.
[376.16 --> 377.16]  Yeah, transparency.
[377.16 --> 401.38]  And, you know, on the data side, speaking of that, that kind of gets us into our topic today, because most of the time, at least in my experience, most of the time, when I've been tackling an AI problem, my first thought is, let's aggregate all of the data together, you know, do whatever pre-processing and such on it that we need to do.
[401.38 --> 416.28]  And, you know, in an ideal world, if we're acting responsibly, also analyze that data set for biases, make sure that we're not, you know, violating any privacy concerns, all of those things on the front end in terms of the data prep.
[416.78 --> 427.94]  But there is a different approach to this that we're seeing more and more being talked about in the sort of trends of the AI world, and that is federated learning.
[427.94 --> 428.44]  Mm-hmm.
[428.78 --> 430.72]  So that's what we're going to talk about today.
[430.94 --> 432.28]  I'm not an expert, Chris.
[432.54 --> 434.40]  Are you an expert in federated learning?
[434.64 --> 439.48]  I am definitely not an expert in federated learning, but I'm coming across it a lot right now.
[439.58 --> 441.28]  I'm in a lot of different contexts.
[441.28 --> 443.84]  So it's definitely something that's become part of my world.
[443.84 --> 452.00]  So for our listeners, you're listening to two non-experts in federated learning, trying to get a grip on what federated learning is.
[452.42 --> 455.64]  We've done a bit of looking and can discuss some of that today.
[455.82 --> 460.48]  So hopefully as you listen, you learn a little bit of that as well.
[460.58 --> 464.02]  And of course, we'll provide some learning resources about that.
[464.02 --> 475.38]  But federated learning has to do with the kind of main idea behind it is that we want to train a centralized model on decentralized data.
[476.02 --> 478.90]  Now, that's kind of interesting.
[479.08 --> 480.80]  So we still want a centralized model.
[481.06 --> 488.84]  There are other paradigms out there that are sort of privacy-preserving sort of ways of going about machine learning.
[488.84 --> 501.08]  One of those is, hey, we could get our model, train it on some centralized data, and then port it to mobile devices and then sort of update or fine tune it on the device using device data.
[501.34 --> 511.30]  So you could do that with like TensorFlow Lite or like integrations with JavaScript or Swift and other things on mobile devices.
[511.60 --> 515.78]  However, that's not what we're talking about when we're talking about federated learning.
[515.78 --> 519.92]  It's related, but in that case, there's no centralized model, right?
[520.02 --> 528.92]  In that case, you're sort of porting a parent model out to a whole bunch of client devices and then maybe doing some learning on the device.
[529.06 --> 530.74]  So updating the model on the device.
[530.86 --> 537.18]  But all of those changes that are local never get ported back into a centralized model.
[537.76 --> 541.00]  So in that case, there are some advantages to that.
[541.00 --> 555.64]  I don't know, before we jump into how federated learning is different, from your perspective, Chris, what are some of the advantages of that kind of model where you're porting or that sort of framework where you're porting models to devices and kind of updating them on devices?
[555.82 --> 556.24]  Any thoughts?
[556.60 --> 556.68]  Sure.
[556.78 --> 558.52]  Well, for one thing, it's more mature now.
[558.72 --> 562.04]  It's something we've been doing for a little while in terms of having those different models.
[562.56 --> 563.32]  There's a history.
[563.44 --> 565.26]  There's a track record of that at this point.
[565.26 --> 569.34]  But it's also proven itself to be insufficient for a lot of use cases.
[569.74 --> 574.68]  So at this point, I think it's interesting because we've seen this topic evolve over time.
[574.98 --> 576.50]  Federated learning is not new.
[576.78 --> 584.72]  As we are recording this today in late 2021, this is not a new topic, but it's really come into its own.
[584.82 --> 587.66]  I think for a long time, it was a discussion.
[587.98 --> 590.38]  It had limited implementation capability.
[590.38 --> 601.82]  As I was looking around at different things for today's episode, there's talk of federated learning in 2016, 2017, where people are talking about the way forward into that.
[601.96 --> 608.28]  But we haven't in those initial years, with some exceptions that were really kind of edge cases, you didn't see it on the rise.
[608.40 --> 612.48]  You saw these other approaches that you just described there.
[612.48 --> 626.20]  We're seeing what I think is a real shift right now this year into trying to find a better solution into being able to have a central model that is decentrally trained in how it does that.
[626.32 --> 628.18]  So I think this is natural evolution.
[628.52 --> 630.28]  I think both the need is there.
[630.72 --> 636.36]  Other approaches are effective in some ways, but also have some deficiencies.
[636.66 --> 642.24]  And the technology from an implementation standpoint has finally arrived with federated learning.
[642.24 --> 647.80]  So we're starting to see a lot of different implementation paths at this point from vendors and various frameworks.
[648.28 --> 648.38]  Yeah.
[648.56 --> 653.42]  So that previously adopted way of going about things, which is still valuable.
[653.42 --> 661.98]  So having the model on the device, maybe updating the model on the device, but never communicating any model changes back to a central model.
[662.26 --> 663.48]  That has been useful.
[663.62 --> 666.52]  And maybe one advantage is its privacy.
[666.52 --> 671.98]  So if you're using user data to update the model, that data actually never leaves the device.
[672.12 --> 674.02]  It stays on the device with the model.
[674.10 --> 674.98]  The model is updated.
[675.32 --> 685.24]  However, all the other devices out in the world that are updating their models, they never get the benefit of the model updates that are on your own device.
[685.24 --> 701.18]  So if we think of something like, you know, speech recognition or interfaces on phones, if my device is learning how to better recognize my accent of English or whatever it is, and it fine tunes on the device, that's great.
[701.50 --> 707.90]  But then all of those other people out there that have a similar accent of English to me, I don't know how many of them there are.
[707.90 --> 711.16]  You know, they're not getting the benefit of those updates.
[711.36 --> 713.20]  And so they have to do their own training.
[713.32 --> 723.12]  So it's actually, in some cases, it's a lot of duplicated effort as well, potentially, where people aren't gaining the value out of other people's model updates.
[723.36 --> 725.68]  But it does have an advantage for privacy.
[725.68 --> 733.72]  So now that we're talking about federated learning, we're also talking about doing certain things and certain training on client devices.
[733.72 --> 743.44]  So, for example, phones, or it could be people's own computers or their tablets or IoT devices or whatever it might be.
[743.72 --> 745.18]  Yeah, I mean, edge devices.
[745.18 --> 749.22]  And I think that's important at this point to call it out because you're kind of going there anyway.
[749.22 --> 758.80]  And that is that the rise of federated learning in a practical sense is also happening concurrent to the rise of edge computing in a practical sense.
[758.94 --> 762.48]  And that's, you know, tremendously scaled and widely available.
[762.92 --> 763.00]  Yeah.
[763.10 --> 765.80]  And so that is now widely available.
[766.02 --> 771.26]  But we also have learned how to do sort of some training on edge devices.
[771.26 --> 783.36]  And we have the knowledge that, hey, if we gathered a whole bunch of data together centrally or had a central model, it would probably be better than training all of these child models potentially.
[784.02 --> 789.30]  And so federated learning, I think, tries to take the approach of the best of both worlds.
[789.62 --> 789.72]  Yeah.
[789.72 --> 799.90]  So doing some training and operations locally on client devices while still having a centralized model, which can benefit all users.
[799.90 --> 811.38]  So it does that in a way that preserves privacy and distributes the sort of training and compute out to the client devices.
[812.18 --> 818.96]  And so in that sense, you have this sort of decentralized compute and centralized model.
[819.16 --> 822.22]  So this is definitely a very interesting approach.
[822.22 --> 825.02]  So that's what we mean by federated learning.
[825.28 --> 829.78]  And when we say a centralized model on decentralized data.
[829.90 --> 834.44]  Now, the question is sort of how that works.
[834.44 --> 839.36]  And like you say, I think there's been a whole bunch of effort in this direction.
[839.58 --> 843.00]  But before we get there, I want to emphasize what you're talking about.
[843.06 --> 847.88]  I think this has been a topic for that has been in our minds for some time.
[847.88 --> 850.22]  I remember I think it was 2017.
[850.78 --> 856.30]  There was a blog post by Google, which you can still read on their research or AI blog.
[856.30 --> 865.22]  And it had some really cool pictures about phones doing some of the training and communicating things back to a central server.
[865.64 --> 870.60]  But to be honest, I didn't hear a lot of about it in that sort of interim time.
[870.70 --> 872.18]  Like I heard it every once in a while.
[872.18 --> 877.70]  But now, you know, part of the reason why we're doing this episode is we're hearing about it a lot more.
[878.04 --> 879.60]  I'm curious from your perspective.
[879.60 --> 898.32]  Do you think that's mostly driven by the privacy concerns or mostly driven by sort of the desire to, you know, have decentralized compute versus like trying to always have like a big farm of GPUs?
[898.32 --> 902.06]  There's an answer that I want to give, but I don't actually believe it.
[902.14 --> 911.60]  The answer I want to give is that there are such concern for privacy issues out there, you know, in the corporate world that that is driving it.
[911.60 --> 918.86]  I don't, however, you know, this is pure opinion, but I don't, however, think that that's the that that is the driving factor.
[918.86 --> 932.56]  I think that I think it is primarily legal constraints and logistics personally with large organizations that are trying to put products and services into the field and, you know, get those deployed.
[932.56 --> 959.24]  And they are constrained by by those various both legal aspects and technical aspects such as networking and such is that being able to even if you can move data around, if you are working on a large model that is, you know, on highly skilled data that would be trained on trying to get that data in the right place at the right time, especially if you have ongoing training can be really challenging.
[959.24 --> 971.88]  And given that federated learning is is and we'll get into the details later, but basically pushing weights and biases around as opposed to all the data makes it logistically much, much, much better in that sense.
[971.98 --> 980.32]  So I that's what my gut is and that's what conversations and presentations that I see are largely geared around logistics and legalities.
[989.24 --> 1019.22]  Thank you.
[1019.24 --> 1024.16]  Once again, that's change log dot com slash plus plus.
[1025.16 --> 1026.88]  Change log plus plus.
[1026.88 --> 1027.86]  It's better.
[1040.80 --> 1042.06]  Okay, Chris.
[1042.24 --> 1043.98]  Well, this is practical AI.
[1043.98 --> 1049.72]  So let's get into some of the practicalities around federated learning.
[1049.72 --> 1067.56]  First of all, at least based on my understanding, this sort of architecture of federated learning differs from a sort of typical AI training architecture in that there is a centralized server or set of servers, you know, maybe in the cloud, maybe on premise.
[1067.56 --> 1068.56]  It doesn't matter.
[1068.56 --> 1068.58]  It doesn't matter.
[1068.58 --> 1078.72]  But this is centralized, maybe a large, larger server, like what we would normally think about doing training or having as a cloud server.
[1079.00 --> 1080.76]  Sometimes that's called a curator.
[1081.28 --> 1084.88]  And that coordinates all the training activities with all of the clients.
[1084.88 --> 1088.88]  And then, of course, there's a bunch of clients which are edge devices.
[1089.26 --> 1097.36]  And these could be hundreds of devices, thousands of devices, millions of devices if we're thinking about phones.
[1097.36 --> 1107.70]  And that central curator server coordinates the training of a model with all of these edge devices.
[1107.70 --> 1110.84]  Now, you talked a little bit about what's communicated back and forth.
[1110.94 --> 1114.82]  Do you want to go into a little bit more detail based on your understanding there?
[1115.28 --> 1115.42]  Sure.
[1115.68 --> 1118.28]  You know, and we can dive into the detail of this.
[1118.36 --> 1123.06]  But kind of the high level is that you have that model on your central server that you're talking about.
[1123.22 --> 1126.34]  And model, we're meaning like a neural network, for example.
[1126.34 --> 1127.68]  A neural network, correct.
[1127.88 --> 1129.04]  Thanks for clarifying that.
[1129.30 --> 1133.96]  And you are going to put that model out to your client.
[1134.20 --> 1139.80]  We're doing the opposite of what we've historically done where we've pulled the data to where our model is going to be trained.
[1139.90 --> 1143.80]  And now we are pushing the model out to be trained where the data is.
[1144.26 --> 1152.84]  And there does have to be a capability that at that point you have to have hardware and software on the client that can do training at some level.
[1153.02 --> 1155.52]  And so it changes the architecture in that sense.
[1155.52 --> 1158.48]  So you're pushing the model in the beginning.
[1158.48 --> 1163.12]  You're pushing the model with its initial values, the weights and biases and such.
[1163.12 --> 1167.46]  And it's going to train based on the data set that's there.
[1167.56 --> 1169.70]  And there's different ways, which we can dive into later.
[1170.04 --> 1177.40]  There are different ways of evaluating whether or not the data that is available on a particular client supports the training process.
[1177.40 --> 1182.12]  So there are some gateways, if you will, that you can evaluate the data with.
[1182.24 --> 1184.44]  And you do training on the device.
[1184.66 --> 1190.98]  And as we know, we keep talking about our phones being kind of the classical example of this.
[1191.26 --> 1195.48]  All of our phones these days are getting these capabilities for doing that kind of training.
[1195.48 --> 1196.86]  You know, they have the chips on them now.
[1196.86 --> 1199.00]  And so you're doing that.
[1199.24 --> 1203.40]  You get a result within a particular accuracy range.
[1203.50 --> 1208.56]  And then you're passing the resultant weights back up to the server.
[1208.56 --> 1217.86]  And so that centralized server is receiving those from all of those hundreds, thousands or millions of client devices connected to it.
[1218.18 --> 1226.26]  And it has to do a form of aggregation on all of those model weights coming back in, which is referred to as federated averaging.
[1226.26 --> 1228.68]  And we can dive into what that means as we go.
[1229.12 --> 1232.46]  But then it averages those out and it measures that.
[1232.70 --> 1234.52]  And then it does it again for the next iteration.
[1234.52 --> 1247.10]  So without going all the way back through it, you're going to keep going through that process, that cycling over and over again until your centralized model is yielding the level of accuracy that you're you're desiring.
[1247.10 --> 1252.54]  And then at that point, then you are able to finally deploy that model, those weights back out.
[1252.80 --> 1256.98]  And you can run that as a as a production model and all those clients.
[1257.78 --> 1259.38]  So, yeah, great description.
[1259.38 --> 1266.44]  And for my mind, I always try to put that sort of description and pair it with with some example.
[1266.44 --> 1268.90]  So I'm imagining like on my phone.
[1269.34 --> 1275.64]  I don't know about you, but sometimes like when I'm walking or something like that, I don't like type a text message.
[1275.64 --> 1277.84]  I just click the speech recognition thing.
[1277.84 --> 1283.56]  And then awkwardly, while everyone else watches me on the sidewalk, I talk into my phone and it records my voice.
[1283.56 --> 1289.66]  But I always look at what was recognized from my voice before I hit send usually.
[1289.90 --> 1291.42]  And then I like correct it.
[1291.64 --> 1291.84]  Right.
[1291.90 --> 1295.20]  Because sometimes it didn't get a correct word or something like that.
[1295.42 --> 1302.30]  I'm impressed because I'll see people doing this a lot and they just hit send and go and everyone just expects the thing to be off.
[1302.38 --> 1303.02]  But anyway, go ahead.
[1303.36 --> 1303.84]  Yeah.
[1303.96 --> 1304.14]  Yeah.
[1304.16 --> 1308.58]  So let's say that I did that, you know, a hundred times or something like that.
[1308.58 --> 1317.40]  And so I have, you know, my voice, I have what was recognized, then I have what should have been recognized because I have my correction.
[1317.72 --> 1320.16]  And I don't actually know if this is how it works in practice.
[1320.36 --> 1324.18]  I'm not on the voice team at Google or anything like that.
[1324.32 --> 1325.20]  You should be, Daniel.
[1325.88 --> 1327.14]  You know, it would be fun.
[1327.52 --> 1334.10]  If anyone wants to fly me out for like a speech visiting scholar position at Google, you know, I'm open to that.
[1334.24 --> 1334.46]  Okay.
[1334.56 --> 1337.10]  Google, OpenAI, you guys have heard it right there.
[1337.22 --> 1337.88]  Daniel Whitenack.
[1337.88 --> 1339.22]  So let's say I have that set.
[1339.30 --> 1340.54]  It's a small set, right?
[1340.82 --> 1344.32]  It's not enough to train a full speech recognition model.
[1344.46 --> 1350.86]  But let's say that Google then, you know, they have their centralized English speech recognition model.
[1351.10 --> 1356.48]  And they then send that model, an updated version of that up to my phone.
[1356.78 --> 1363.36]  And my phone then in this federated learning scheme would use the data that's just on my phone.
[1363.68 --> 1366.68]  So the data hasn't been transferred back up to Google.
[1366.68 --> 1367.10]  Correct.
[1367.10 --> 1370.44]  It uses that audio and the text from my phone.
[1370.84 --> 1378.94]  Does a training, a retraining of that model or a fine tuning of that model based on the data that I've seen and looks.
[1378.94 --> 1385.54]  So now I'm going to have updated weights and biases or updated parameters from that model right on my phone.
[1385.54 --> 1401.48]  And then my phone can send not the data, but the weights and biases, the parameters of that model, the updated ones, or maybe just the deltas, the changes, back up to the centralized server or curation server.
[1401.48 --> 1409.60]  So if thousands or millions of devices do the same thing, they're going to all be sending their updated weights back.
[1409.60 --> 1411.16]  Which are evaluated before.
[1411.16 --> 1412.30]  They're not just lumped in.
[1412.56 --> 1416.10]  That averaging process scores them based on that.
[1416.44 --> 1425.30]  And it's really, this approach is really cool in that you're getting the benefit of the average weights and values across all the data sets across all clients.
[1425.30 --> 1437.42]  So you're getting a training benefit as though you have access to everything there is while having only that limited data set that you're there, you know, which then gets scored as that goes through the process.
[1437.42 --> 1439.24]  It's pretty cool when you think about it.
[1439.24 --> 1445.34]  Yeah. And I think it's important to emphasize that this is a practical reality now.
[1445.54 --> 1448.72]  So, I mean, people are still doing research in this, no doubt.
[1448.88 --> 1450.58]  This is an active research topic.
[1450.86 --> 1450.94]  Sure.
[1451.02 --> 1456.68]  But there are practical ways to go about that that have been developed.
[1456.98 --> 1461.36]  So we'll list out a few of those a little bit later in the episode.
[1461.36 --> 1465.94]  But I'm just looking at PyGrid, which is one of these that's been released.
[1465.94 --> 1470.24]  And in that, there's just to give you a sense of what this might look like.
[1470.32 --> 1474.04]  There's a couple of Flask based applications.
[1474.32 --> 1482.38]  So Flask is a Python framework that allows you to build web applications like APIs, REST APIs, that sort of thing.
[1482.94 --> 1486.22]  And so there is a Flask application that is like centralized.
[1486.70 --> 1495.86]  I think they call it the network and it manages and monitors and controls routing instructions to various domains or which are, in my understanding,
[1495.94 --> 1497.96]  being hosted on workers.
[1498.18 --> 1499.70]  So PyGrid workers.
[1500.06 --> 1511.56]  And that domain is another Flask-based application that receives instructions and executes a worker application on the device to do ephemeral updates to the model and communicate those back.
[1511.72 --> 1514.64]  So the device receives a request to train a model.
[1515.00 --> 1516.74]  The device will request to train a model.
[1516.74 --> 1522.12]  So the device actually has to sort of opt in to the training bit, which makes sense.
[1522.12 --> 1528.98]  And then the model and some sort of parameters about the training plan will be sent to the device.
[1529.14 --> 1533.18]  The training will take place on that device with the private data.
[1533.74 --> 1540.02]  Once the training is completed, in this case, with this framework, it's the delta or the diff of the parameters.
[1540.02 --> 1543.86]  The original state of the model is communicated back up to the server.
[1544.32 --> 1549.24]  And then that's averaged, like you say, into the centralized model.
[1549.36 --> 1554.78]  So that's a sort of what they call the model-centric federated learning type of technique.
[1554.78 --> 1566.58]  There are other kind of versions or flavors of federated learning that might include some like communication of privacy-preserving data.
[1566.58 --> 1572.42]  But I think the one that we've been mostly emphasizing here is the model-centric version, which is what we're talking about here.
[1572.76 --> 1572.96]  Correct.
[1572.98 --> 1575.50]  Because the data stays on the device.
[1575.50 --> 1581.96]  I mean, that seems practical to me in the sense that I've worked with Flask applications before.
[1582.16 --> 1584.78]  And I've done some AI training a few times.
[1584.96 --> 1587.58]  So it seems like something I could work on.
[1587.60 --> 1590.50]  Although I haven't worked with phones much myself.
[1591.34 --> 1594.66]  So maybe that part's a little bit scary to me in like how that actually works.
[1594.74 --> 1596.20]  I've never developed a mobile app.
[1596.20 --> 1599.64]  I have, but I haven't done it from a deep learning standpoint.
[1600.22 --> 1601.48]  Yeah, yeah.
[1601.76 --> 1609.26]  So I don't know all of the mobile application development pieces that you'd have to tie in.
[1609.36 --> 1620.56]  I know that there's some like JavaScript and Kotlin and Swift libraries for these frameworks that will allow you to kind of build and support that worker capability on the device.
[1620.56 --> 1631.80]  One thing that came up in some of the information that I was reading was like, doesn't this like just suck away all the battery of the device?
[1632.02 --> 1635.14]  Like, what are the implications for the device user?
[1635.14 --> 1647.04]  So like if I'm other than like, you know, because it's maybe useful to talk about the disadvantages for the device user rather than just the advantages, like they get a cool new model, which is good.
[1647.04 --> 1656.42]  But, you know, you kind of what was that program where like it was like citizen science type thing where you could you could register your computer?
[1656.60 --> 1657.80]  Oh, I know what you're talking about.
[1657.80 --> 1665.00]  With like a science lab and they would run like astronomical calculations like in a decentralized way on your computer.
[1665.00 --> 1668.54]  Yeah, there was the SETI program that was doing that with computers.
[1668.64 --> 1671.22]  That was like the earliest one that I can remember.
[1671.54 --> 1672.58]  That's way back now.
[1672.86 --> 1673.74]  And there have been other since.
[1673.92 --> 1675.48]  I mean, it's in the same vein.
[1675.70 --> 1677.90]  That's going to drain your computer power, right?
[1678.08 --> 1678.58]  It can.
[1678.78 --> 1683.10]  But I think our conversation right now is also leaning toward that phone assumption.
[1683.34 --> 1684.68]  And it's not always a phone assumption.
[1685.20 --> 1686.98]  It can be a larger device.
[1687.06 --> 1689.72]  Your edge device might be a might be a mobile platform.
[1689.72 --> 1695.56]  And when I say mobile, I mean like with wheels or wings or rockets or something else.
[1695.66 --> 1696.06]  Oh, right.
[1696.08 --> 1697.86]  Like a car or a car.
[1697.86 --> 1698.00]  It could be a car.
[1698.36 --> 1698.80]  Exactly.
[1699.04 --> 1701.74]  And so it may be going forward.
[1701.74 --> 1704.88]  And I'm this is completely pure speculation.
[1704.88 --> 1715.72]  But if you're going to do a lot of federated learning and doing that processing, maybe there's another battery that's in that car that's, you know, that's there to run your training hardware that's there.
[1715.86 --> 1717.26]  And so it kind of depends.
[1717.26 --> 1722.64]  If it's the phone, yeah, it's probably going to start sucking battery down if you're doing any substantial amount of training.
[1722.64 --> 1730.12]  But if you're in literally a vehicle that it's tremendously benefiting from that over time as use cases get found.
[1730.12 --> 1731.98]  And I think we're still and this goes out.
[1732.06 --> 1733.60]  We can get into use cases in a few minutes.
[1733.60 --> 1738.48]  But I think that we're still at a point where we are exploring use cases.
[1738.48 --> 1743.62]  And where does federated learning give us a strategic advantage to implement for that?
[1743.62 --> 1755.48]  And there may be cases out there where in doing that, then you simply architect in the ability to do on platform learning out there on the edge, so to speak, to accomplish this.
[1755.48 --> 1769.72]  Before we jump into frameworks and some of the use cases that we've seen out there, Chris, one of the things that I think is worth noting as related to this federated learning topic is related to security.
[1769.72 --> 1775.30]  So I remember very clearly in my mind back when I did go to conferences in person.
[1775.84 --> 1779.26]  I think it was an ODSC conference or something like that.
[1779.40 --> 1783.06]  I saw Jim Klukar, who was with Immuta at the time.
[1783.62 --> 1784.10]  Shout out, Jim.
[1784.18 --> 1786.00]  I don't know if you listen, but great guy.
[1786.00 --> 1790.18]  But he talked about privacy in his talk.
[1790.60 --> 1796.88]  And he showed some examples where I think it was facial recognition or I'm pretty sure it was facial recognition.
[1797.06 --> 1800.60]  Anyway, you could take a model because our models are so big now.
[1800.84 --> 1801.06]  Right.
[1801.56 --> 1803.70]  And there's so much encoded into our models.
[1803.70 --> 1810.62]  And you could actually, from a prediction, sort of work back to the original data that was used.
[1810.62 --> 1815.96]  So you could reconstruct people's faces in the training set, right, just from the model parameters.
[1816.52 --> 1828.46]  And so in theory, you could imagine sort of reconstructing the data that's on client devices from what's sent to the central curator server or coordinator server.
[1829.10 --> 1832.88]  So that's one thing to note here about the aggregation.
[1832.88 --> 1836.62]  And I think this is probably what you were getting to when you were talking about the aggregation.
[1837.12 --> 1841.44]  There is a method of securing that aggregation.
[1841.78 --> 1843.06]  So there's two things.
[1843.06 --> 1847.02]  There's encryption when the data is sent back to the central server.
[1847.02 --> 1850.06]  But then there's a way to securely aggregate that.
[1850.56 --> 1852.78]  And that has to do with differential privacy.
[1853.64 --> 1859.54]  So, yeah, any I don't know if that's what you're meaning when you're getting at like averaging some of those results back together.
[1860.30 --> 1860.56]  I do.
[1860.56 --> 1867.42]  And I think that, I mean, that's one of those areas that there's going to be a lot more research on in terms of being able to do that.
[1867.42 --> 1871.68]  Because right now there are some federated averaging algorithms that are in use.
[1872.08 --> 1874.78]  And the most basic one is just called federated averaging.
[1874.78 --> 1876.66]  But there are others that are being built on top of that.
[1876.66 --> 1884.66]  And I think that's going to be one of those areas that people are having to explore as data scientists on the research side are going to have to explore is can you get back to the data?
[1884.92 --> 1888.98]  Because and there's so much that's going to depend on on where that research goes.
[1888.98 --> 1895.02]  Because, you know, going back to our example of national boundaries is that you have laws protecting citizens, rightly so.
[1895.44 --> 1897.32]  But they vary across national boundaries.
[1897.32 --> 1908.94]  And therefore, for you to have a model that is a for you to be able to participate in federated learning in that capacity and to be able to deploy a subsequent model across national boundaries.
[1908.94 --> 1919.28]  That is one of those areas that we need to ensure that even though the data itself will reside on a client and maybe across the national boundary, that you cannot recreate that coming back across.
[1919.40 --> 1921.94]  So I'm expecting to see a lot more on that in the years ahead.
[1922.44 --> 1922.56]  Yeah.
[1922.90 --> 1924.32]  And I agree with that.
[1924.48 --> 1929.52]  And, you know, differential privacy and this sort of aggregation could be a topic in and of itself.
[1929.52 --> 1932.44]  And maybe we'll have a follow up episode on that.
[1932.44 --> 1949.24]  Just a few sort of very brief phrases about differential privacy is that so if we're thinking about phones and them contributing their data or edge devices, it limits how much any single contribution from a phone can contribute to the overall changes in the model.
[1949.44 --> 1961.48]  And in that way, the model isn't sort of overly skewed or memorizing results from a single device, which could lead to sort of reconstruction of rare private data.
[1961.48 --> 1966.78]  And also that noise is added to that sort of rare data.
[1967.02 --> 1974.12]  So that all of those ideas are kind of if you want to learn more about that, you might look up more on differential privacy.
[1974.70 --> 1974.80]  Yeah.
[1975.08 --> 1982.40]  I'm speculating that the more diversity you have in your data set, you know, will help protect you from that as well because it is an averaging function.
[1982.40 --> 1995.00]  And so if your core data that you're training on is close to the average, if the data that's coming back from all of your client devices is very similar, that obviously is something that would have to be addressed in that sense.
[1995.00 --> 2012.04]  So when I was looking up how I might go about implementing some federated learning, I was curious as to the state of the various frameworks and tools that you can use to actually achieve this process.
[2012.38 --> 2018.96]  I was pleasantly surprised with, you know, of course, I haven't run a real experiment with millions of devices.
[2018.96 --> 2020.72]  Maybe that is in my future.
[2020.94 --> 2023.20]  It would definitely be a fun experiment.
[2023.50 --> 2028.14]  But it looks like, for example, one of these frameworks is TensorFlow federated.
[2028.14 --> 2035.90]  So TensorFlow has an open source framework for doing this computation on decentralized data.
[2036.62 --> 2049.92]  And some of what you have to do to your model to enable that is kind of wrap some of your model definitions in classes and helper functions that are provided by the TensorFlow federated framework.
[2050.30 --> 2055.52]  But you do get to sort of preserve your, you know, your Keras model, which you love.
[2055.52 --> 2064.18]  You know, you have your Keras model and you kind of wrap things around it to use it in this federated way, which seems like a nice approach.
[2064.40 --> 2067.36]  You don't have to throw out everything that you did with Keras that you love.
[2067.42 --> 2070.66]  You can kind of wrap it and use it from there.
[2070.98 --> 2077.42]  There's a bunch of other organizations and large organizations that are really contributing to open source frameworks.
[2078.04 --> 2082.22]  Intel has their open federated learning framework.
[2082.22 --> 2088.94]  And Facebook was involved in PySift and PyGrid, which I mentioned before.
[2089.06 --> 2092.98]  PyGrid was the sort of methodology that I talked through before.
[2093.16 --> 2102.92]  And then there's some other ones, too, like Flower, I saw, which is a friendly federated learning framework, which is nice and lots of Fs in there.
[2103.98 --> 2105.42]  But that looked really cool.
[2105.56 --> 2106.68]  And there's other ones, too.
[2106.68 --> 2110.24]  I'm sorry if I'm leaving out your favorite one for those listening out there.
[2110.58 --> 2118.32]  But I guess at this point, you know, I think we're really to a point where I'm really curious to see if anyone in our audience is actually doing this.
[2118.44 --> 2122.56]  I know that the teams at my employer are now into federated learning.
[2122.66 --> 2127.80]  And as we've done, just as we've we love to hear from folks about who is engaging in it.
[2128.14 --> 2131.44]  Have you guys done any federated at the nonprofit that you work at yet?
[2131.44 --> 2133.34]  Or have you not yet had a need to?
[2133.34 --> 2140.64]  We haven't, although I do wonder about that because, you know, one of our use cases is translation.
[2140.92 --> 2146.28]  So we have over a thousand translation projects going on around the world.
[2146.38 --> 2153.06]  And part of what I'm working on is augmented quality assessment types of tools for those translations.
[2153.06 --> 2169.44]  And those will that very much fits in this framework where there's a centralized set of models that are maybe used on all of these client devices and could be improved by data that can be gathered on those client devices.
[2169.44 --> 2186.20]  But also these are people working all around the world on their own translation stuff that oftentimes includes like their own copyright restrictions, for example, where they they might not be able to share that translation data in certain contexts or otherwise.
[2186.44 --> 2191.12]  So there's rights holders and copyright information associated with all those translations.
[2191.12 --> 2194.12]  So it's definitely got me thinking along those lines.
[2194.48 --> 2196.00]  That's a fascinating use case right there.
[2196.00 --> 2203.28]  You could ask the user's permission to be able to do it, because as you pointed out earlier, you're also using some of the power that's available.
[2203.48 --> 2206.92]  And if you're going to do this federated learning, then you're going to be training on the device.
[2207.00 --> 2210.98]  And if their device is capable of doing that, then you're presumably draining the battery faster.
[2211.32 --> 2216.10]  But you also have these other ancillary issues that the end user may or may not know.
[2216.74 --> 2219.78]  And so have you put any thought into how you might address that?
[2219.86 --> 2221.26]  Is there any way of evaluating that?
[2221.74 --> 2223.54]  To be honest, I don't know.
[2223.54 --> 2237.62]  My first thought is that this can be a little bit tricky because for so long, people have been exposed to messages that pop up on their device that say, share data with us and we'll make your experience better.
[2237.96 --> 2238.12]  Right.
[2238.32 --> 2244.92]  That's been a sort of common thing when you accept terms and services or when you like when always you get a new phone.
[2244.92 --> 2245.22]  Right.
[2245.28 --> 2247.68]  It's like or a new phone service.
[2247.68 --> 2255.00]  You're like, share data back to us about like your network usage and we can make the network better for everybody.
[2255.30 --> 2255.56]  Right.
[2256.08 --> 2258.78]  And that's really ingrained in people's minds.
[2258.78 --> 2265.56]  And so if you try to like put some messaging in an app around that, that's probably what people are going to assume at first.
[2265.70 --> 2266.94]  Like, oh, they're collecting our data.
[2267.34 --> 2268.44]  I don't want to share my data.
[2268.82 --> 2268.98]  Right.
[2269.34 --> 2270.98]  So it's very interesting.
[2270.98 --> 2274.64]  Like how and how much do you share with the end user?
[2274.86 --> 2280.20]  And what is the phrasing around that to help them understand what is actually happening?
[2280.88 --> 2281.22]  Yes.
[2281.22 --> 2297.14]  You are sharing something with a centralized server, but in a differentially private way and it may reduce, you know, it may suck away some of your battery or, you know, run certain things on your device that you weren't running before.
[2297.14 --> 2299.28]  And so maybe there's battery issues and other things.
[2299.28 --> 2308.54]  But I think that there's a sort of a lot of assumptions that we'll have to overcome as we do that because people are so used to the fact of like, oh, everybody's just gathering my data.
[2308.54 --> 2313.12]  Right. And when I see one of these pop ups, it's asking me for data and I don't want to share my data.
[2313.54 --> 2318.28]  It makes for a fascinating consideration to have to try to to overcome and mitigate.
[2318.70 --> 2323.24]  I work in the defense industry and governments that are that are interested.
[2323.52 --> 2325.94]  They kind of control their entire environment.
[2325.94 --> 2329.44]  You know, it may be contested by another government, so to speak.
[2329.90 --> 2338.38]  But at the end of the day, you know, any given government that might be interested in that is, you know, they are running both the central server and they also own those.
[2338.54 --> 2341.34]  Endpoints, those those edge devices, whatever those are.
[2341.90 --> 2349.22]  And so there is potentially much less to have to consider from a user rights standpoint, a privacy standpoint.
[2349.22 --> 2352.80]  So it becomes just a logistical thing to some degree.
[2353.12 --> 2354.24]  Fascinating consideration.
[2354.24 --> 2358.72]  And I think that your use case is much closer to what most end users would have to deal with.
[2358.76 --> 2362.44]  They're going to have customers and they're going to have user communities that they're serving.
[2362.44 --> 2363.98]  So, yeah.
[2364.18 --> 2374.32]  And there have been examples of successful uses of this across industry where people have, you know, at least started navigating these concerns.
[2374.32 --> 2380.62]  Google, of course, I mentioned they were investigating this even a few years ago or more.
[2380.62 --> 2391.32]  And they've shown various actual real world applications of this in mobile keyboard sort of development and autocomplete prediction type stuff.
[2391.46 --> 2395.72]  Voice and audio data being used to improve things like Google Assistant.
[2396.62 --> 2400.66]  Also, you know, other tech giants you might expect are investigating this as well.
[2400.66 --> 2413.62]  Facebook is sort of rebuilding, in my understanding, at least from public articles, rebuilding some of their ad infrastructure and models to do things in a more decentralized way with federated learning.
[2413.96 --> 2420.38]  One that I think is really cool, which is dominating the actual applications that I've seen are related to health care.
[2420.38 --> 2434.38]  I don't know if you've seen some of these, Chris, but one I was reading in a Nature article from Harvard Medical School where they actually were predicting sort of clinical outcomes of patients with COVID using federated learning.
[2434.38 --> 2454.12]  So, you know, they had something running presumably on patient devices or at least clinic devices and, you know, preserve the privacy around patients' actual health data while also maybe providing some predicted outcomes to doctors to help them, you know, augment maybe their treatments and that sort of thing.
[2454.52 --> 2457.86]  So, yeah, that was a really interesting example that I ran across.
[2457.86 --> 2461.18]  Another one that I've run across is predictive maintenance.
[2461.54 --> 2465.22]  You have all of these different types, both in the civilian world and the military world, et cetera.
[2465.40 --> 2472.14]  All these vehicles out there, all these devices, factory machines, and they do have their own data set there.
[2472.38 --> 2487.02]  And from just even if privacy is not a concern, just logistically being able to benefit from that diversity of things out there that you can then train on and train toward, that is, I think, I think it lends itself very naturally to federated learning.
[2487.02 --> 2495.24]  So, towards the end of each of these fully connected episodes, we always like to leave you with a few different learning resources.
[2495.90 --> 2512.96]  One of the things we will do is include in the show notes links to all of these different federated learning frameworks and open source projects that we've mentioned, like TensorFlow Federated and Intel Open Federated Learning and others, so that you can go there and actually get hands on and try out a few things.
[2512.96 --> 2535.76]  However, one of the things that I think is really great, you know, if this is a new topic to you and you just want to think about it a little bit more and its implications, Google put out this federated learning comic, which is really good at sort of leading you through both the motivation of federated learning, how it works, maybe some concerns or questions that come out of that.
[2535.76 --> 2546.40]  And you'll see some of the themes that we talked about in this episode represented in that comic, which is a great way, sort of visual and fun way to get introduced to federated learning.
[2546.54 --> 2549.18]  And we'll include the link in our show notes.
[2549.36 --> 2550.36]  What about you, Chris?
[2550.60 --> 2552.66]  What's some of the stuff that you were looking at?
[2553.02 --> 2560.82]  You know, one of the websites that we have talked about with various learning resources over many episodes is one called Towards Data Science.
[2560.82 --> 2567.52]  And Towards Data Science had a good tutorial for stepping into federated learning with TensorFlow.
[2567.76 --> 2571.50]  It's called Federated Learning, a Step-by-Step Implementation in TensorFlow.
[2571.92 --> 2576.34]  It was in April 10th of 2020, so about a year and a half ago.
[2576.74 --> 2582.86]  And it's a really good introduction into the basics of it and doing kind of a toy network to try it out.
[2583.28 --> 2584.30]  So that was a good one.
[2584.30 --> 2590.46]  And then I'll mention, this may be almost funny to say that, but go to the Federated Learning page on Wikipedia.
[2590.82 --> 2593.22]  It has quite a lot of information there.
[2593.56 --> 2595.14]  It's probably not where I would start.
[2595.22 --> 2598.38]  If you're not familiar with federated learning, it's not the first place.
[2598.52 --> 2605.58]  But after you've read a few other things and maybe gone through some of the other resources, it may throw some terms at you that you missed in certain areas.
[2605.88 --> 2607.56]  And you can say, oh, what is this?
[2607.62 --> 2608.18]  What is this?
[2608.28 --> 2609.96]  So I thought I'd mention those to you.
[2610.02 --> 2612.00]  The Towards Data Science is a good beginner.
[2612.00 --> 2614.78]  And then after you've gotten a little bit under your belt, Wikipedia.
[2615.48 --> 2615.64]  Awesome.
[2615.98 --> 2618.80]  Well, we hope that our listeners will explore this.
[2618.92 --> 2623.36]  As Chris said, we're interested to hear how you are exploring this topic.
[2623.90 --> 2625.90]  Connect with us in our Slack community.
[2626.10 --> 2628.84]  You can find that at changelog.com slash community.
[2629.12 --> 2633.96]  We'd love to hear what you're working on and what you would like us to be talking about on the podcast.
[2633.96 --> 2636.28]  We really do value your input.
[2636.78 --> 2640.94]  You can also find us on LinkedIn or on Twitter as well.
[2640.94 --> 2642.54]  So keep in contact.
[2642.68 --> 2647.68]  Let us know what you're learning about as related to federated learning and other things.
[2648.24 --> 2650.08]  And thanks for the conversation today, Chris.
[2650.14 --> 2650.62]  It was fun.
[2651.00 --> 2651.62]  I enjoyed it.
[2651.66 --> 2652.20]  Thanks a lot, Daniel.
[2655.78 --> 2656.80]  That's our show.
[2657.02 --> 2657.66]  Thanks for listening.
[2658.32 --> 2660.48]  For more like this, check out our master feed.
[2660.64 --> 2664.54]  It is all changelog podcasts in one easy to consume place.
[2664.88 --> 2669.76]  Let your podcast app snag everything we produce and then pick and choose which ones to listen to.
[2669.76 --> 2676.12]  Subscribe today at changelog.com slash master or just search for changelog master in your podcast app of choice.
[2676.40 --> 2676.96]  You'll find it.
[2677.46 --> 2684.42]  Special thanks to Breakmaster Cylinder for providing our music and to our longtime sponsors, Fastly, LaunchDarkly, and Linode.
[2684.94 --> 2686.26]  That's all for this week.
[2686.48 --> 2687.74]  We'll talk to you again next time.
[2687.74 --> 2717.72]  We'll talk to you again next time.
