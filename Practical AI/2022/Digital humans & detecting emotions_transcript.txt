[0.00 --> 5.32]  I think that we're finding the more computing power we can put behind this, then the better
[5.32 --> 10.18]  off we are, the better we are at predicting or understanding someone's emotions.
[10.18 --> 16.86]  You know, there are classic examples of bots misinterpreting information that comes across.
[17.24 --> 22.50]  Let's face it, human beings are very complicated and general artificial intelligence is not
[22.50 --> 23.12]  there yet.
[23.40 --> 28.74]  You know, that's going to take a lot of quantum computing capability, high powered computing
[28.74 --> 29.60]  of all sorts.
[29.60 --> 35.50]  So what we're looking at is what's the best modality for predicting a response or looking
[35.50 --> 38.56]  at an emotional response in a particular situation.
[38.84 --> 44.58]  So it's just depends upon what it is the problem is you're trying to solve and how AI is used
[44.58 --> 45.28]  in that problem.
[45.28 --> 61.78]  Welcome to practical AI, a weekly podcast, making artificial intelligence practical, productive
[61.78 --> 63.42]  and accessible to everyone.
[63.42 --> 68.08]  This is where conversations around AI machine learning and data science happen.
[68.08 --> 73.82]  Join us at practical AI.fm slash community and follow the show on Twitter.
[73.98 --> 76.18]  We're at practical AI.fm.
[76.40 --> 81.04]  Thank you to our partners at Fastly for shipping our pods super fast all around the world.
[81.04 --> 83.10]  Check them out at fastly.com.
[83.10 --> 93.12]  Welcome to another episode of practical AI.
[93.12 --> 95.12]  This is Daniel Whitenack.
[95.24 --> 98.74]  I am a data scientist with SIL International.
[98.74 --> 101.36]  And I'm really excited today.
[101.36 --> 104.44]  We have, I mean, I'm very happy.
[104.64 --> 110.58]  My emotion is happy, I think, to talk about the subject that we have today, which is about
[110.58 --> 111.90]  emotion AI.
[112.80 --> 119.46]  With us today, we have Teresa Kushner, who is data and analytics practice lead at NTT
[119.46 --> 120.40]  data services.
[120.70 --> 121.20]  Welcome, Teresa.
[121.78 --> 122.94]  Oh, thank you, Dan.
[122.94 --> 124.56]  And it's very, very nice to be here.
[125.06 --> 126.52]  I'm looking forward to this discussion.
[126.76 --> 129.30]  Yeah, this is super interesting.
[129.30 --> 136.66]  I know that our listeners probably have, I mean, obviously, they're familiar with emotions.
[136.66 --> 140.72]  They're familiar with AI, if they've been listening to the show.
[140.92 --> 147.86]  And they might have seen certain tasks in the AI world, maybe related to like sentiment
[147.86 --> 149.72]  or something like that.
[149.72 --> 156.96]  I'm wondering if you could kind of help at a higher level, help us understand what you
[156.96 --> 162.16]  mean when you're talking about emotion AI, maybe specifically like what kind of emotions
[162.16 --> 164.92]  are we talking about and how might they be represented?
[165.08 --> 166.10]  I guess we could start there.
[166.50 --> 170.70]  Well, we're talking about the whole entire range of human emotions, but we've been looking
[170.70 --> 172.16]  at this for a very long time.
[172.18 --> 178.18]  And I'm so glad that you mentioned sentiment analysis, because I can remember back in the
[178.18 --> 184.46]  last decade when I was at Cisco, that one of the things that we did constantly was monitor
[184.46 --> 190.52]  the internet for words that people were using that would give us a way of understanding whether
[190.52 --> 194.74]  our messages were being heard or not, or what people thought about us.
[195.16 --> 199.50]  You know, they could be writing one thing on all of the posts that they were sending up
[199.50 --> 203.90]  to us, but they could be feeling something different in other kinds of forums.
[203.90 --> 210.54]  And so we started managing that and it for a while became a way of understanding our press
[210.54 --> 215.28]  relations, which was really important for us because we didn't have a way to measure
[215.28 --> 217.46]  press relations until that point in time.
[217.92 --> 224.42]  So sentiment analysis sort of gave way to this entire world of how do we look at an emotion
[224.42 --> 226.46]  that a human being has?
[226.68 --> 230.06]  And they share that we share our emotions in lots of ways.
[230.06 --> 233.30]  We share it with our voice, the quality, the tone.
[233.54 --> 235.50]  We share it with our facial expressions.
[236.10 --> 237.70]  We share it with our body language.
[238.10 --> 244.84]  So our emotions are out there for people to read, just as data on any subject is out there
[244.84 --> 246.66]  for the computers to read.
[246.96 --> 253.20]  And we're starting to take that information in and to collate it and figure out things about
[253.20 --> 254.10]  the classic.
[254.28 --> 257.56]  When you lie to someone, you look down in a certain direction.
[257.56 --> 261.04]  You know, those kinds of things you can pick up on.
[261.50 --> 268.38]  And as we monitor facial expressions and that data starts to be fed in, we can start to look
[268.38 --> 272.32]  at using artificial intelligence, look at how we could respond.
[272.82 --> 278.94]  Classic example for this might be if we had a digital human who was interfacing with a customer
[278.94 --> 281.78]  in a kiosk at an airport, for example.
[281.78 --> 286.84]  And you could see that the emotion of the person interacting was confused.
[287.36 --> 292.60]  Then the digital human could say, let me sort of explain what you might be able to do at
[292.60 --> 293.48]  this kiosk.
[294.04 --> 300.50]  You know, so there are lots of ways that you can begin to apply this emotional AI capability.
[301.02 --> 302.26]  That's super interesting.
[302.26 --> 309.24]  I'm really intrigued by this side of things, even like digital humans in a physical environment
[309.24 --> 312.58]  that you're in and how people might interact with that.
[312.68 --> 314.80]  That's interesting in and of itself.
[315.12 --> 318.36]  And I think we could come back to that in a bit.
[318.62 --> 326.06]  Before we do, I'm wondering, one of the things that comes to my mind is just how sort of fluid
[326.06 --> 328.66]  and complex emotion is.
[328.66 --> 334.16]  And so I think you've already alluded to the fact that you kind of have multiple modalities
[334.16 --> 341.06]  that represent emotion, whether that be sort of something captured on video or imagery or
[341.06 --> 347.78]  something written down in text or something spoken, facial expression, gesture, all sorts
[347.78 --> 348.30]  of things.
[348.46 --> 354.38]  So you have this sort of range of modalities, but then you also have maybe a like confusing
[354.38 --> 362.10]  set of like fluid, emotional, how do you navigate even just defining the various things that
[362.10 --> 363.12]  you're wanting to detect?
[363.38 --> 368.14]  First of all, you know, it is pretty early time for this kind of emotional AI.
[368.48 --> 371.12]  So we don't have the answers for everything.
[371.62 --> 377.02]  I think that we're finding the more computing power we can put behind this, then the better
[377.02 --> 381.88]  off we are, the better we are at predicting or understanding someone's emotions.
[381.88 --> 389.22]  You know, there are classic examples of bots misinterpreting information that comes across.
[389.66 --> 395.62]  Let's face it, human beings are very complicated and general artificial intelligence is not there
[395.62 --> 395.96]  yet.
[396.34 --> 401.66]  You know, that's going to take a lot of quantum computing capability, high powered computing
[401.66 --> 403.80]  of all sorts in order to do that.
[404.24 --> 408.74]  I love the fact that you mentioned this modality because what we're looking at is what's the best
[408.74 --> 415.14]  modality for predicting a response or looking at an emotional response in a particular situation.
[415.78 --> 422.84]  You know, it's probably fair to say that if you have a contact center cold line of some
[422.84 --> 427.78]  sort, you could actually use voice more effectively than you could visuals.
[428.36 --> 434.00]  So it's just depends upon what the use of what it is the problem is you're trying to solve
[434.00 --> 436.24]  and how AI is used in that problem.
[436.66 --> 440.60]  In fact, the use of AI is always the issue.
[441.10 --> 443.66]  You know, how are we actually going to apply it?
[443.72 --> 447.92]  And that's why I was so excited about talking to you because you guys have this practical
[447.92 --> 448.42]  AI.
[448.84 --> 451.30]  And in my world, that's what makes sense.
[451.50 --> 455.44]  Not the fact that we're exploring all these different because we've got to do that, but
[455.44 --> 460.60]  we also have to get it down to something that's practical so that we can actually do something
[460.60 --> 461.14]  with it.
[461.40 --> 466.02]  As always, every side of technology comes with a yin and a yang.
[466.38 --> 469.40]  You know, there's good things and there are bad things.
[469.40 --> 475.54]  And you can determine how this works based upon how you go forward with your artificial
[475.54 --> 477.66]  applications, AI applications.
[478.14 --> 485.50]  Yeah, I love how you stress that because, you know, one feeling that I have talking about
[485.50 --> 489.34]  this is like that my emotions are a very personal thing.
[490.30 --> 495.54]  And, you know, there's a whole diversity of the way that people express their emotions
[495.54 --> 498.60]  differently from one person to another.
[498.76 --> 505.96]  So I imagine that navigating that is part of the difficulty and that you can see like the
[505.96 --> 507.74]  kiosk example you mentioned.
[508.08 --> 512.28]  There's a real clear benefit to the user there potentially.
[512.28 --> 520.56]  But then in other cases, like I could imagine if I'm on a video interview for a job, right?
[520.74 --> 525.88]  And, you know, something is detecting whether I'm confused in that situation, right?
[525.88 --> 526.18]  Yes.
[526.24 --> 532.94]  Maybe I'm not really confused, but I'm nervous and it reflects poorly on my potential as a
[532.94 --> 537.26]  job candidate or, you know, that sort of thing can, I imagine, get quite tricky.
[537.26 --> 541.40]  Yeah, that's where the ethical AI side of this comes in.
[541.90 --> 545.46]  And also, too, there's cultural issues associated with some of this.
[545.92 --> 551.50]  There are cultures where you don't look people in the eye, where that might be something that
[551.50 --> 554.44]  we would record in North America, something that's really important.
[554.84 --> 558.42]  You're much more honest and straightforward if you're looking someone in the eye.
[558.42 --> 564.18]  So, you know, there are all kinds of implications, all of which have to be managed in this world.
[564.48 --> 568.86]  But again, it comes down to what are you doing with that information?
[569.48 --> 575.48]  And someone this afternoon said to me, which I think is really right, is that all technology
[575.48 --> 582.58]  has got to have permission from the people that are using it in order to keep information.
[582.58 --> 588.38]  In other words, we have got to get used to granting to some of this technology the permission
[588.38 --> 594.18]  to use our facial expressions, the permission to use our emotional content, the permission
[594.18 --> 596.76]  to use our personal data in some way.
[597.50 --> 603.46]  That has got to come back to how we manage all of our data and all of our assets.
[603.70 --> 606.32]  And that's a very important part of what we're trying to do, too.
[606.32 --> 615.28]  Obviously, the data piece of this, I imagine, is really the crux of the problem in a lot of
[615.28 --> 621.32]  ways, because there's all sorts of classification models and advanced models that I'm sure can
[621.32 --> 623.20]  be employed if you have the right data.
[623.44 --> 630.08]  In the cases that you're working with, could you describe maybe some of the kinds of data
[630.08 --> 636.42]  that you're working with, you know, and how, how I guess emotion is annotated within that,
[636.58 --> 642.26]  whether that's, you know, one dimensionally or along a bunch of different facets, or how
[642.26 --> 647.72]  do you kind of think about formulating a data set for emotion AI?
[648.30 --> 649.92]  Oh, that's a really good question.
[650.38 --> 654.94]  I think that the first data set that has to get formulated with any kind of AI application
[654.94 --> 657.28]  like this is one that takes care of the problem.
[657.28 --> 662.98]  And most of the problems that we've seen are handling transactions between humans and
[662.98 --> 664.06]  a machine of some sort.
[664.60 --> 669.54]  So they're transactional, and there's not a lot of emotion related to them.
[670.10 --> 677.12]  However, what we are seeing is that if we can get some of the emotional information in,
[677.54 --> 680.06]  then we can handle the problem better.
[680.46 --> 685.92]  We've all had this experience where we call up and the bot that we interface with doesn't
[685.92 --> 688.96]  understand the thing we're saying, and we get frustrated.
[689.60 --> 695.50]  Well, would that be interesting if that frustration could be recorded as something that gets passed
[695.50 --> 701.06]  on to the person for real that's going to answer the call and hopefully solve your problem?
[701.72 --> 707.88]  You know, so I think that there's places for this, even in the transactional sets that we
[707.88 --> 709.14]  need still to explore.
[709.14 --> 712.56]  But again, this is really new for people.
[713.10 --> 719.30]  And those people that are in industries or with companies where this might be prevalent
[719.30 --> 723.22]  have not really thought about how they can use their existing data.
[723.42 --> 727.86]  For example, one of the things that has to happen if we're going to use transactional data,
[728.04 --> 732.72]  let's just say, I'm not going to tell you customer names, but let's say we have a customer who wants
[732.72 --> 741.98]  to use this in a store environment and they want the avatar or the on-screen AI application
[741.98 --> 745.30]  to actually help them solve their billing problems.
[745.68 --> 750.20]  So that means you've got to have access to all the billing information on this customer,
[750.36 --> 756.56]  and it has to be done pretty quickly, which is something that we've not necessarily had
[756.56 --> 762.20]  to move data that quickly to an individual to answer an on-screen problem.
[762.86 --> 765.82]  So those kinds of things we have to watch.
[766.04 --> 770.38]  In addition, data nowadays streams from a lot of different places.
[770.82 --> 775.76]  So even if I have the transaction for that customer, what additional information should
[775.76 --> 779.10]  I have in that transaction that the avatar needs to have?
[779.24 --> 780.64]  And where is it going to come from?
[780.78 --> 784.64]  Is it going to stream in automatically or is it going to be something that I've previously
[784.64 --> 785.16]  captured?
[785.34 --> 788.28]  Now I'm just making sure it's part of the AI algorithm.
[788.28 --> 793.14]  Those are a lot of data concerns about how you manage this.
[793.24 --> 797.66]  And that's sort of the practical side of this, where you have to get down, find out where
[797.66 --> 799.90]  is that data and what are we doing with it?
[800.16 --> 805.04]  I appreciate you bringing in those sides of things because I think that it's one of the
[805.04 --> 807.18]  purposes of the show, obviously, with the name.
[807.18 --> 813.46]  And it's something that I find people like they get to a project where maybe they're trying
[813.46 --> 818.16]  to implement something sophisticated and all of the blockers that they hit are related
[818.16 --> 825.18]  to moving data from one place to another or latency or deploying a model and like memory
[825.18 --> 830.84]  concerns or like all of these things that are sort of the practicalities of doing this
[830.84 --> 831.98]  sort of problem.
[831.98 --> 835.96]  And let's not forget the most important one, which is the quality of the data that we put
[835.96 --> 836.88]  in there to begin with.
[837.00 --> 837.10]  Yeah.
[837.18 --> 842.98]  And that, I guess, brings me to my next question, which is on that quality of data side.
[843.20 --> 849.84]  And because of the kind of fluidity of feelings and emotions, have you found that working with
[849.84 --> 856.88]  the client very closely to understand like specific emotions that are really important to them
[856.88 --> 864.38]  is key to kind of nailing down the right sorts of annotations and responses?
[864.72 --> 865.74]  Yeah, exactly.
[866.44 --> 871.02]  And again, I just sort of go back to this is one of the things I tell all clients when we
[871.02 --> 877.30]  start AI practices is we really have to be very clear as to what you're going to use AI
[877.30 --> 877.70]  for.
[878.02 --> 885.18]  If you don't have that clearly in your mind, then we will go off on a wild fancies every
[885.18 --> 888.76]  which way and we won't solve the problem that we're trying to solve.
[889.26 --> 895.38]  So from an AI perspective, any AI, whether it's an avatar or whether it's just ordinary
[895.38 --> 900.52]  predictive analysis, you need to know specifically what it is you're trying to accomplish.
[915.18 --> 930.22]  So, Teresa, I think you kind of alluded to some of these things a little bit earlier when
[930.22 --> 934.06]  you brought up the kind of ethical things around this.
[934.38 --> 940.68]  I'm wondering if you could speak to kind of your current thinking around both kind of the
[940.68 --> 947.28]  ethical aspects of emotional AI and maybe the privacy related things too.
[947.46 --> 953.16]  Because if I'm maybe a generally angry person or something, maybe I don't want that, you
[953.16 --> 956.82]  know, publicized too much or, you know, I don't know what it is.
[957.02 --> 960.68]  But yeah, you don't want it as a little icon on your LinkedIn profile.
[960.88 --> 961.42]  That's for sure.
[962.10 --> 962.54]  Exactly.
[962.78 --> 963.06]  Yeah.
[963.06 --> 968.52]  So, like, I guess on the practical side, like, how do you see these things popping up?
[968.58 --> 973.62]  And what is your kind of current thinking in terms of the real lines that you're trying
[973.62 --> 978.20]  to draw and the ways you're trying to practice emotional AI specifically?
[978.58 --> 980.76]  You know, that is such a good question.
[980.88 --> 986.50]  And I just finished a training session with our sales team on trustworthy AI and what that
[986.50 --> 992.56]  means to have a trustworthy AI application or instance in your company.
[992.86 --> 998.30]  And it sort of boils down, and I hate to be so simple, but it boils down to the golden
[998.30 --> 998.80]  rule.
[999.26 --> 1001.90]  Do unto others as you would have them do unto you.
[1002.42 --> 1007.40]  And in artificial intelligence, we don't need to do things that push the line.
[1007.48 --> 1013.08]  Because quite frankly, some of the stuff that we are doing with avatars can be fairly creepy.
[1013.08 --> 1018.70]  You know, I've seen things where we're actually using artificial intelligence to reproduce
[1018.70 --> 1024.56]  Kamala Harris or some of the other, you know, you can actually do sort of deep fakes that have
[1024.56 --> 1026.96]  all of the instances of this around it.
[1027.36 --> 1030.12]  So where does that line get drawn?
[1030.72 --> 1039.32]  And again, I think that line gets drawn with making sure that people understand how you're
[1039.32 --> 1042.00]  using the information you're collecting from them.
[1042.00 --> 1047.18]  Not only have you given them permission, I mean, we've all got these, except this cookie
[1047.18 --> 1052.52]  thing everywhere in our life nowadays, you know, so, but how many people have ever stopped
[1052.52 --> 1056.26]  to read all of the legal language underneath that permission?
[1056.52 --> 1062.66]  And I think that it's going to be the responsibility of those people using artificial intelligence to
[1062.66 --> 1070.46]  make those checkboxes to give me permission to use your data understandable so that people understand
[1070.46 --> 1072.42]  what's going to happen to that information.
[1072.74 --> 1077.52]  You know, it's one thing to collect a whole bunch of emotions around a particular topic
[1077.52 --> 1082.38]  and to direct an avatar to respond based on the majority of responses.
[1082.86 --> 1083.70]  That's one thing.
[1083.98 --> 1089.04]  It's another thing for me to respond specifically to you, Daniel, about your emotion.
[1089.74 --> 1091.24]  That's very different.
[1091.72 --> 1097.34]  And so we kind of need to make sure that we're doing the right things for people.
[1097.34 --> 1104.38]  Yeah, I think that that sort of individual aspect is probably one of the key pieces to
[1104.38 --> 1110.58]  this because I could see, you know, going back to the kiosk example that you're talking about.
[1110.80 --> 1118.28]  In one case, you could have something that is running kind of further out to the edge in
[1118.28 --> 1119.60]  terms of the compute.
[1119.82 --> 1125.84]  It's processing streams of information that are local to that device and providing feedback
[1125.84 --> 1126.86]  to the user.
[1126.86 --> 1133.72]  But then it's a separate thing if you're streaming up all the audio and all the video and maybe
[1133.72 --> 1139.36]  even detected emotions along with timestamps and all of that to the cloud.
[1139.36 --> 1142.80]  That becomes a very different scenario.
[1143.30 --> 1150.54]  So in these cases where you're deploying emotion AI, how have you kind of struck a balance between
[1150.54 --> 1161.30]  making sure you're gathering good data to do well at the task that you're trying to do versus
[1161.30 --> 1166.80]  sort of swinging to the side of privacy and anonymity and that sort of thing?
[1166.80 --> 1170.94]  Yeah, I will tell you some of the places where we've used emotional AI that I think have been
[1170.94 --> 1171.72]  most effective.
[1171.72 --> 1178.00]  And that's with our, we have an application that teaches children to read.
[1178.84 --> 1182.16]  And in that application, there's an avatar of sorts.
[1182.24 --> 1183.44]  It's a comic little thing.
[1183.60 --> 1190.02]  But that avatar actually looks at the child that is engaged in the reading exercise and
[1190.02 --> 1195.88]  can tell when they stumble, when they're getting tired, when they're not paying attention and
[1195.88 --> 1199.30]  recall and have an action for the child.
[1199.30 --> 1203.30]  So it actually says, hey, I see you're sort of lagging there.
[1203.38 --> 1204.66]  Would you like to read a story?
[1205.14 --> 1206.98]  Or can you do this?
[1207.06 --> 1208.98]  No, you missed that particular word.
[1209.14 --> 1212.56]  Can we go back and, oh, I see you're not just totally engaged.
[1213.20 --> 1219.40]  You know, so those are the places where I think that emotional AI plays the best part because
[1219.40 --> 1221.86]  it gives something back to the experience.
[1222.12 --> 1224.00]  And I think that's another key word.
[1224.00 --> 1229.70]  We are all very excited about digital experience and customer experience.
[1229.92 --> 1231.78]  That means it's a two-way street.
[1232.26 --> 1238.54]  We have got to actually have the customer be engaged and excited about engaging with us
[1238.54 --> 1241.96]  or with an avatar or with some sort of application.
[1242.50 --> 1247.78]  That experience has got to be something that's positive for the customer, no matter what.
[1247.78 --> 1255.32]  And quite frankly, I've read statistics that some of our avatars are better received than
[1255.32 --> 1257.08]  human beings on phone lines.
[1257.70 --> 1259.50]  Yeah, that's super interesting.
[1259.76 --> 1264.90]  I know that I've had a similar experience with chatbots, especially internationally.
[1265.18 --> 1270.40]  We've done a bunch of chatbot related things in my own work.
[1270.40 --> 1277.66]  And yeah, it's amazing what people will open up to a bot about and just like engage with
[1277.66 --> 1285.02]  a bot about in a very authentic way that is not how you would sort of maybe naturally
[1285.02 --> 1289.84]  engage with a human virtually on a web call or something like that.
[1289.92 --> 1292.12]  So yeah, that's very interesting.
[1292.52 --> 1293.58]  I'm wondering on this.
[1294.32 --> 1298.56]  So you mentioned this application with helping children learn how to read.
[1298.56 --> 1304.40]  Could you give us a little bit of backstory about kind of how that came about and how
[1304.40 --> 1307.34]  the project kind of got spun up and that sort of thing?
[1307.38 --> 1308.16]  I'd love to learn more.
[1308.62 --> 1312.62]  I believe, and I'm going to tell you, it started with our engagement with MIT.
[1312.90 --> 1317.66]  We have a very robust engagement with the MIT Media Lab.
[1318.12 --> 1323.70]  And some of the work that we were doing with our avatars out of our Denmark business unit
[1323.70 --> 1327.00]  actually engaged with MIT just to do this.
[1327.00 --> 1332.98]  And myself, having worked with MIT over the last 30 years off and on, the Media Lab's
[1332.98 --> 1335.22]  always been a source of education.
[1335.70 --> 1337.66]  That's one of the things that they try for.
[1338.14 --> 1345.06]  And so when you are looking to apply technology that hasn't been applied before, it is really
[1345.06 --> 1349.34]  good to have it in something that kids can understand.
[1349.34 --> 1353.10]  Because if kids can understand it, anybody can.
[1353.84 --> 1357.98]  And that sort of is what happened with this, is that became an application.
[1358.30 --> 1361.46]  If we could teach children to read, wouldn't that be great?
[1361.82 --> 1367.68]  Now what you can do is start to use that same technology to train adults, to train people
[1367.68 --> 1374.10]  on just-in-time training at airports or just-in-time training at any other kind of operational
[1374.10 --> 1374.60]  facility.
[1374.60 --> 1378.54]  So there are lots of broader applications for it.
[1378.66 --> 1381.84]  But getting it right with a kid, that was important.
[1382.52 --> 1382.80]  Interesting.
[1383.06 --> 1383.20]  Yeah.
[1383.30 --> 1389.16]  And could you maybe paint a picture, since this is an audio podcast, just paint?
[1389.60 --> 1392.84]  We'll make sure to link to some really good pictures and stuff.
[1392.92 --> 1395.70]  I will tell you what it sort of reminds me of.
[1395.70 --> 1400.54]  I taught my son to read with an application on the computer called Reader Rabbit.
[1401.24 --> 1401.54]  Okay.
[1401.78 --> 1407.26]  But Reader Rabbit stayed on the computer, and he just had to fill in little things.
[1407.42 --> 1409.94]  It's like fill in the blank or memory sort of thing.
[1409.96 --> 1410.68]  Yeah, exactly.
[1411.18 --> 1414.32]  This one actually is a little avatar.
[1414.52 --> 1420.14]  It's a guy, a cartoon guy, who sits in the corner of the screen and actually talks like
[1420.14 --> 1426.24]  a teacher would to the student so that the student hears what they're saying and then
[1426.24 --> 1428.52]  tries to do whatever they're acting.
[1429.06 --> 1435.12]  And because it can hear what the student says, it understands they're not saying the word right
[1435.12 --> 1438.44]  or they've mispronounced it or they didn't read it right.
[1438.58 --> 1444.44]  So there's all of that interaction that goes on with this particular application that wasn't
[1444.44 --> 1446.18]  in Reader Rabbit for sure.
[1446.18 --> 1454.52]  Yeah, and it sounds like that's something that kids could engage with and kind of spur
[1454.52 --> 1459.04]  on curiosity towards reading, which is really cool.
[1459.78 --> 1464.52]  Has this been kind of deployed in an experimental way?
[1464.66 --> 1466.96]  Are there ways that people can engage with this at all?
[1466.96 --> 1470.06]  Well, it's been employed in an experimental way so far.
[1470.40 --> 1474.12]  It's won all kinds of awards for us for its application.
[1474.12 --> 1477.14]  But I think you'll probably see it picked up.
[1477.56 --> 1480.78]  You know, the technology to do some of this is still fairly expensive.
[1481.42 --> 1486.98]  You know, so having a child read with this instrument might not be the best way right
[1486.98 --> 1487.18]  now.
[1487.26 --> 1491.58]  We've got to figure out a way to get that more practically into the hands of readers.
[1492.10 --> 1498.16]  Yeah, I imagine that the sort of processing of the various streams and the compute associated
[1498.16 --> 1504.34]  with this is maybe not something that, you know, all fits on my on my smartphone.
[1505.04 --> 1506.00]  Not trivial.
[1506.16 --> 1506.76]  That's for sure.
[1506.94 --> 1507.20]  Yeah.
[1507.38 --> 1507.66]  Yeah.
[1507.82 --> 1515.20]  And has it been a challenge with these sorts of like real time applications to kind of deal
[1515.20 --> 1520.84]  with some of those real time and latency aspects in terms of like balancing?
[1520.84 --> 1527.04]  I'm always, again, thinking about the practicalities of balancing these like, oh, I could pull down
[1527.04 --> 1533.08]  a wave to back model off of, you know, hugging face or something, and it's going to run great,
[1533.08 --> 1537.60]  but maybe really slow or it might need to be accelerated in some way.
[1538.04 --> 1542.10]  But then kind of I could swing to the other side where people are really thinking about the
[1542.10 --> 1545.08]  more efficient ways of running these sorts of models.
[1545.32 --> 1548.26]  So is that something a kind of an internal discussion you're having?
[1548.26 --> 1550.44]  That's an internal discussion always.
[1551.02 --> 1553.62]  And every customer's environment is different too.
[1554.12 --> 1558.34]  You know, a lot of customers' environments are not set up to do this kind of data exchange.
[1558.86 --> 1564.34]  And so that's one of the reasons why NTT Data Services looks at that is because that's
[1564.34 --> 1570.04]  what we do is that we help you create those kinds of environments that are data rich and
[1570.04 --> 1573.02]  responsive to all kinds of applications.
[1573.02 --> 1579.40]  And so we're in the throes of trying to make sure that when we release these technologies,
[1579.40 --> 1585.26]  that we get companies that have the backbone in order to do it to begin with.
[1585.54 --> 1587.98]  Because it's just frustrating to companies.
[1588.20 --> 1593.32]  Like you said, you know, the computing power, the capability, a lot of what we do is in the
[1593.32 --> 1593.66]  cloud.
[1593.88 --> 1599.24]  But then again, you have to push our friends from the hyperscalers to do high performance
[1599.24 --> 1603.00]  computing at a cost that's available to ordinary humans.
[1603.60 --> 1607.10]  So that's another area that we look at constantly.
[1607.10 --> 1607.58]  Yeah.
[1607.86 --> 1615.62]  Also, to kind of come back to the MIT work and the literacy or reading application work,
[1615.70 --> 1621.70]  I'm wondering if there were any responses maybe from like non-technical researchers, maybe
[1621.70 --> 1630.56]  more on the sort of linguistics or social sciences or education side even that kind of had any
[1630.56 --> 1631.76]  reactions to this?
[1631.76 --> 1637.84]  I believe that's what MIT itself offered was some of the testing that they had done with
[1637.84 --> 1639.26]  the tool to make sure that it's right.
[1639.36 --> 1641.34]  The Media Lab is pretty famous for that.
[1641.48 --> 1645.82]  My first involvement with the Media Lab was with Logo, like years and years ago.
[1645.94 --> 1649.32]  So I know they are concerned about that.
[1649.32 --> 1654.10]  So there is testing going on with everything that we put out there is testing.
[1654.46 --> 1656.14]  How do customers respond to it?
[1656.36 --> 1658.30]  How do children respond to it?
[1658.34 --> 1659.72]  What kinds of things are we doing?
[1660.08 --> 1665.98]  Because let's face it too, artificial intelligence has this ability to make changes in our life.
[1666.38 --> 1671.32]  And we've seen, just as the internet did, you know, the internet can be used as good for
[1671.32 --> 1672.46]  good or for evil.
[1672.46 --> 1677.80]  And we want to make sure that when we unleash something like this, that we are doing it
[1677.80 --> 1682.92]  for the good part of society, not for something that would have unintended consequences.
[1682.92 --> 1708.92]  Well, Teresa, I have so many questions.
[1708.92 --> 1713.58]  It's hard for me to think of where to go, but I think the one thing that I wanted to follow
[1713.58 --> 1718.18]  up on was some of what you talked about, the sort of digital humans.
[1718.52 --> 1726.10]  I know that you even mentioned sort of the way in which you create avatars or digital representations
[1726.10 --> 1730.20]  of humans can go a whole variety of directions.
[1730.20 --> 1735.52]  I know there's, I forget the famous study where it's like the more human-like avatar looks,
[1735.62 --> 1737.54]  the more creepy it feels.
[1737.54 --> 1739.06]  The creepier it becomes, yes.
[1739.24 --> 1739.88]  Yeah, exactly.
[1740.40 --> 1747.54]  So maybe just stepping back a little bit, could you describe your current kind of, more generally,
[1747.74 --> 1755.28]  your current kind of thought process around digital humans at NTT and like their place
[1755.28 --> 1758.78]  and sort of value in your work?
[1758.78 --> 1761.80]  I'll give you an example, great living example.
[1761.98 --> 1767.60]  If you were to walk into the lobby of NTT in Japan today, the person that greets you is
[1767.60 --> 1768.36]  a digital human.
[1768.74 --> 1768.80]  Interesting.
[1769.26 --> 1771.92]  On a, like a screen or a kiosk or something?
[1772.14 --> 1772.56]  It's a kiosk.
[1772.56 --> 1773.32]  It's a kiosk.
[1773.36 --> 1776.90]  It's a fairly large kiosk and you can ask her anything.
[1777.12 --> 1780.26]  You know, I have an appointment with such and such, where is that?
[1780.38 --> 1782.94]  How do I, oh, and she handles everything.
[1782.94 --> 1785.52]  And that's one of the very first uses.
[1785.52 --> 1793.42]  You know, the avatar was originally created for Kia Motors, who wanted to be able to explain
[1793.42 --> 1797.04]  their electric cars to the general public.
[1797.04 --> 1811.48]  And I love this story because when we first deployed the avatar, we deployed her in an airport where people could just come up and talk about Kia and what we were doing with the car, with a specific car.
[1811.48 --> 1815.28]  And then what they did is that they moved her to the showroom.
[1815.90 --> 1825.76]  Now, one of the things that we would love to be able to do, and we're looking at doing this, I'm not sure with Kia at the moment, but with other manufacturers,
[1826.36 --> 1834.72]  is that because we know that you interface with us at the airport, when you come to the showroom, we should be able to make that connection.
[1834.72 --> 1847.24]  Okay. So the dream, the ultimate further down the line kind of dream is that we take an avatar from an airport, collect information about people there.
[1847.48 --> 1859.24]  When that moves to the showroom, we're able to say, hi, Daniel, I remember you when we talked at the Narita airport six months ago, you know,
[1859.28 --> 1863.40]  and then you can have that particular conversation go forward.
[1863.40 --> 1865.32]  And let's say you purchase a car.
[1865.62 --> 1876.78]  We would love to have the avatar now sit in the car and become your direction giver, your Alexa, so to speak, for that particular car.
[1877.10 --> 1882.20]  So that's kind of, if you can imagine what we can do with a digital human, that would be the ultimate.
[1882.20 --> 1898.88]  Yeah, it's almost like you have, it sounds like there's this sort of, like there is an avatar, which is kind of a representation, but then there's almost like, I don't know how to describe it, like a forking of that avatar,
[1898.88 --> 1910.88]  or like a bunch of sort of parallel universes for that avatar that are created where it responds in a unique way or has a unique sort of relationship with individual people.
[1911.62 --> 1915.18]  That's kind of how, I don't know if that's a good representation.
[1915.18 --> 1924.28]  Every company out there right now is trying to do what is their customer mapping, the roadmap for how a customer experiences their product.
[1924.66 --> 1925.74]  Personalized and dynamic.
[1926.00 --> 1926.58]  Exactly.
[1926.98 --> 1934.18]  And so with the avatar, you can identify the points that are most important to collect and have conversations.
[1934.18 --> 1942.08]  And that creates for you an entirely different customer experience than you would have otherwise.
[1942.32 --> 1957.32]  Yeah, I guess the, in certain ways, like if I went up to a booth at the airport that was, you know, Kia related, I could sign up for something and maybe they would put me in some type of system.
[1957.50 --> 1960.28]  And then they would know me when I come to the dealership.
[1960.28 --> 1968.04]  I'm sure there's like privacy concerns and other things you have to navigate and making sure people, you know, understand what's going on.
[1968.52 --> 1974.70]  But I think also there's this, yeah, like the personalized and dynamic side of things.
[1975.16 --> 1985.50]  People also, I think, probably like in the sense that they don't have to re-explain a lot of things when they get certain places.
[1985.50 --> 1986.06]  Exactly.
[1986.56 --> 1996.20]  If all we did was take away the requirement to tell your phone number and your account number to three people before you get an action, that would be worth it.
[1996.62 --> 1997.28]  Yeah, yeah.
[1997.82 --> 2008.92]  And these digital humans, I see a really great kind of diagram on your website, which we'll link in the show notes, that talks about the emotion piece is actually part of this.
[2008.92 --> 2020.64]  Because like the digital human can, you know, sense certain emotions, but there's a whole lot of other, I guess, signals, you would call them, that the digital human is processing.
[2020.78 --> 2031.30]  Could you describe some of those other things that are a part of the puzzle of like making sure that this digital human is dynamic and responds in the way that you want?
[2031.30 --> 2033.06]  That's kind of a tricky question.
[2033.22 --> 2038.06]  We have, for most of the digital humans, it takes certain kinds of technology.
[2038.50 --> 2040.78]  You have to have microphones that are directed.
[2041.20 --> 2053.88]  Because if you've got a kiosk in the middle of a busy airport and you're talking to it, if the microphone picks up everybody in the airport instead of your particular question and your response, then you have to know that.
[2053.88 --> 2062.18]  And also, you have to make sure that the person is standing in a particular place that they can get the answers back and forth.
[2062.26 --> 2064.66]  So this actually becomes a one-to-one.
[2065.14 --> 2069.24]  And that's fairly interesting and difficult to manage.
[2069.40 --> 2071.96]  We have to make sure that that happens on a one-to-one basis.
[2072.30 --> 2074.66]  Haven't learned yet how to handle a crowd of people.
[2075.12 --> 2079.08]  That's probably something that we should sell to politicians, for example.
[2079.08 --> 2085.02]  But so the technology to do that sort of zeroes in on the individual.
[2085.50 --> 2088.84]  Is there anything else specifically that you were looking for in that question?
[2089.06 --> 2096.36]  Well, I'm wondering, you know, maybe based on that, it is interesting that you're thinking of this sort of one-to-one interaction.
[2096.94 --> 2102.86]  And I wonder, like, this may be more of like an aspirational question, I guess.
[2102.86 --> 2116.94]  But I could see how, like, if certain people walk up to a kiosk and see a certain type of person of a certain age, of a certain gender or height or whatever it might be.
[2117.02 --> 2124.12]  In some cultures, for example, you know, maybe it wouldn't be appropriate for a man of this age to address.
[2124.82 --> 2125.36]  Exactly.
[2125.36 --> 2136.14]  Yeah. So in the sort of long run with this, how dynamic do you expect the kind of avatar itself to be in relation to kind of the one-to-one interactions?
[2136.62 --> 2137.58]  That's a great question.
[2137.74 --> 2143.74]  In fact, that was one of the very first questions that one of our customers asked after we had finished the demo.
[2144.04 --> 2147.64]  It was the fact we had knew we sort of hooked them when they asked that question.
[2147.82 --> 2152.46]  It's because those avatars are very easily changed.
[2152.46 --> 2161.52]  OK, now what we have to do is get the artificial intelligence behind it to be able to say, OK, I need to look like that person.
[2161.88 --> 2166.06]  In other words, I need to mimic whoever is in front of me in some way.
[2166.50 --> 2171.44]  The technology isn't quite there yet, but our team in Denmark is working on it.
[2171.86 --> 2173.10]  Yeah, very, very interesting.
[2173.38 --> 2181.90]  And I think the reading example is really interesting because I was just at ACL a couple weeks ago in Dublin and they were talking.
[2181.90 --> 2193.26]  I had sat in a lot of talks about indigenous languages and language learning, which is like, you know, my own passion and my own organization's passion and work.
[2193.40 --> 2197.02]  And just the importance that they put on sort of language learning.
[2197.02 --> 2218.88]  But also there was an emphasis on like certain language communities wanted not just like an application on their phone, but they wanted a sort of like kiosk or physical thing in a like, for example, one indigenous community talked about they have a language center and they go there to do language related things.
[2218.88 --> 2221.70]  And they didn't want technology on everybody's phone.
[2221.78 --> 2230.80]  They wanted something physically kind of present in that center to build community and for them to experience their language and learn their language.
[2230.80 --> 2244.44]  And so what do you think, you know, I guess the question is, how do you think in the future we'll kind of think about embedding these digital humans in the physical world?
[2244.58 --> 2246.04]  So one thing would be kind of.
[2246.12 --> 2248.08]  So they become a robot almost.
[2248.08 --> 2253.74]  Well, maybe not a physical with like physical arms and such, but where would I choose?
[2253.86 --> 2262.74]  Like you were talking about having one, you know, maybe in a car, but also at the at the airport and the sort of scale of that at the airport.
[2262.74 --> 2267.00]  I could have a really big screen and it could be sort of human size in the car.
[2267.12 --> 2273.08]  Maybe it's like a little screen and it's a little bitty, you know, and that I imagine changes the dynamics.
[2273.08 --> 2283.36]  Like, so how are your clients or how are you kind of thinking about what are the locations, the locations and formats where we would want to embed this sort of digital human?
[2283.58 --> 2285.02]  Well, that's such a good question.
[2285.56 --> 2286.82]  Yeah, that is such a good question.
[2286.82 --> 2291.78]  And every time we engage with the customer, those kinds of questions come up.
[2292.20 --> 2297.26]  But again, I think one of the things that we are doing is spending a lot of time testing these.
[2297.72 --> 2298.40]  Does that work?
[2298.46 --> 2300.42]  In other words, does it work that size?
[2300.58 --> 2302.62]  Is the size the right angle?
[2302.62 --> 2306.40]  Are all of the buttons in the right place that you might want to interact with?
[2306.68 --> 2312.32]  You know, there's a lot of customer and design capability that goes into what we do as well.
[2312.70 --> 2312.84]  Yeah.
[2313.16 --> 2316.68]  That's a great question, though, because that is something that we have to consider.
[2316.82 --> 2322.40]  How do you look at that little person on the screen in your car versus the person that was almost full size at the airport?
[2322.90 --> 2323.06]  Right.
[2323.38 --> 2323.60]  Yeah.
[2323.68 --> 2328.70]  And I guess people are used to viewing, you know, at least heads on screens now.
[2328.94 --> 2329.88]  Yes, they are.
[2329.88 --> 2333.56]  The pandemic and all of those sorts of things.
[2333.56 --> 2342.32]  We do have a couple of robots we've been working on with MIT that are good at collecting information.
[2342.70 --> 2352.76]  I mean, Jibo was one of the ones that we actually worked with MIT on, which they were deploying into children's wards at hospitals.
[2352.76 --> 2357.98]  One of the things that we found is that children love to interact with these robots.
[2358.60 --> 2364.22]  And because they do, they tell them things that the doctors don't always know.
[2364.72 --> 2375.76]  And that information has become very helpful for managing kids with, you know, ailments of undetermined sorts or, you know, really complicated situations.
[2375.76 --> 2377.94]  Yeah, very interesting.
[2378.38 --> 2383.74]  Well, it seems like you have no shortage of exciting things to work on.
[2384.38 --> 2384.82]  Exactly.
[2385.42 --> 2385.68]  Yeah.
[2385.74 --> 2396.88]  I'm wondering, as you look to the future, even kind of out the next couple of years, like when you're kind of laying in bed at night or, you know, on a drive or whatever, what are those things in your mind?
[2396.92 --> 2401.72]  Are the things that are sort of driving you as a practitioner and a leader in this industry?
[2401.72 --> 2405.20]  What are you thinking about and what are you excited about looking forward?
[2405.62 --> 2410.72]  There are no shortage of problems for us to solve in the world with artificial intelligence.
[2411.56 --> 2413.82]  There are issues associated with climate.
[2414.10 --> 2417.42]  There are issues associated with security.
[2417.94 --> 2420.84]  There are all kinds of things that we can go after with AI.
[2420.84 --> 2432.02]  My dream, when I lay in bed at night and think about what we could do, is to make sure that artificial intelligence gets applied ethically to solve problems that help people.
[2432.52 --> 2434.04]  That's my biggest concern.
[2434.62 --> 2439.08]  And so we're trying our darndest to do exactly that.
[2439.38 --> 2442.64]  Yeah, well, I'm very happy to hear that emphasis.
[2442.90 --> 2446.06]  I know it's something that's on a lot of people's minds right now.
[2446.06 --> 2450.72]  So really excited to hear that you're thinking in that direction as well.
[2451.14 --> 2454.04]  Teresa, it's been a real pleasure to have you on the show.
[2454.16 --> 2456.12]  This is really exciting stuff.
[2456.24 --> 2460.48]  I can't wait to dig in a little bit more and explore.
[2460.96 --> 2463.38]  We'll include some links in our show notes.
[2463.50 --> 2471.12]  So everyone make sure and check those out and check out these digital humans and some of the applications that we've talked about on the show.
[2471.24 --> 2472.80]  But really wonderful to talk, Teresa.
[2472.80 --> 2473.90]  Thank you for joining us.
[2473.90 --> 2476.10]  Thank you very much for the opportunity, Daniel.
[2484.98 --> 2485.80]  All right.
[2485.94 --> 2487.94]  That is Practical AI for this week.
[2488.24 --> 2496.50]  If this is your first time listening, subscribe now at practicalai.fm or just search for Practical AI in your favorite podcast app.
[2496.70 --> 2497.22]  We're in there.
[2497.52 --> 2500.72]  And if you're a longtime listener, please do share the show with your friends.
[2500.72 --> 2503.66]  It is the best way you can help Practical AI succeed.
[2503.90 --> 2511.24]  Thanks again to Fastly for shipping our shows super fast all around the world to Breakmaster Cylinder for the Beats and to you for listening.
[2511.48 --> 2512.18]  We appreciate you.
[2512.56 --> 2513.64]  That's all for this week.
[2513.78 --> 2514.88]  We'll talk to you again next time.
[2514.88 --> 2528.46]  artık een suite.
[2528.46 --> 2529.06]  GnAг.
[2529.90 --> 2532.66]  lip empowerment.
[2532.66 --> 2533.24]  conduct odor.
[2533.46 --> 2534.42] splac.com.
[2534.50 --> 2535.46]  Bookmobile.gooku.com.
[2535.70 --> 2536.38]  Come with us.
[2536.38 --> 2536.92]  Hurry up friends, face open space or anywhere.
[2536.92 --> 2537.58]  PFC'd be on their interest.
[2537.72 --> 2538.32]  Tip right now.
[2538.32 --> 2539.48]  Talk to you again next time.
[2539.48 --> 2541.06]  It's영ers coldова.
[2541.06 --> 2541.38]  Azeich月.
[2541.38 --> 2541.94]  Hurry up to screen.
