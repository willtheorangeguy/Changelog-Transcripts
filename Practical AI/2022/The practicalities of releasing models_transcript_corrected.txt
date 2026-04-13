[0.00 → 9.36] So there was this idea that the data that we were using, in this case, it was from the
[9.36 → 15.58] Bloom library, which is a product from SIL where people can create their own books online.
[15.78 → 22.58] So each book, the author releases that under a certain creative, well, not all are creative
[22.58 → 25.02] commons, but the majority are creative commons licenses.
[25.02 → 33.28] And so we had to look into whether the models that we were creating off of creative commons
[33.28 → 40.18] data would be subject to the same sort of restrictions as the creative commons data that
[40.18 → 41.10] we were training it on.
[41.48 → 46.56] And so there are various writings, you know, within you can actually look up creative commons
[46.56 → 51.88] has some commentary on this of when certain things are derivative works or adaptations
[51.88 → 53.02] and that sort of thing.
[55.02 → 69.72] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive
[69.72 → 71.04] and accessible to everyone.
[71.42 → 72.22] Subscribe now.
[72.38 → 76.20] If you haven't already headed to practicalai.fm for all the ways.
[76.56 → 81.54] Special thanks to our partners at Vastly for delivering our shows superfast to wherever
[81.54 → 82.20] you listen.
[82.20 → 86.76] Check them out at Fastly.com and to our friends at fly.io.
[87.12 → 90.70] We deploy our app servers close to our users and you can too.
[91.06 → 92.96] Learn more at fly.io.
[98.96 → 103.62] Well, welcome to another fully connected episode of Practical AI.
[103.98 → 109.54] This is where Chris and I keep you fully connected with everything that's happening in the AI community.
[109.54 → 117.88] We'll take some time to discuss the latest AI news and dig into some learning resources to help you level up your machine learning game.
[118.46 → 119.48] I'm Daniel Whiten ack.
[119.58 → 127.52] I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson, who's a tech strategist at Lockheed Martin.
[127.76 → 128.44] How are you doing, Chris?
[128.74 → 129.84] Doing great today, Daniel.
[129.90 → 130.38] How are you?
[130.52 → 131.02] Doing well.
[131.02 → 133.00] It's been a pretty fun week.
[133.32 → 140.64] Last night, got to speak virtually anyway at the Utah ML Ops meetup.
[140.88 → 141.92] So that was pretty fun.
[142.26 → 146.30] Had a few connections there and a lot of good questions and such came out of that.
[146.30 → 154.54] So it's interesting to see meetups happening again, but also still embracing this like bringing in virtual speakers' thing.
[154.78 → 163.92] So it's like a still hybrid in that sense, because if you're a local meetup, you've got to bring in speakers, and it's a lot easier to bring in virtual speakers.
[163.92 → 167.36] And I think if I think it worked out pretty good the way that they had it set up.
[167.62 → 169.48] So that sounds interesting.
[169.48 → 173.38] And since you mentioned it, I'm speaking at a virtual conference next week.
[173.84 → 180.86] I've been taking like through COVID, I had taken more or less a long break after doing way too much conference talking.
[181.26 → 181.46] Right.
[181.56 → 183.64] In the year in the years leading up to it.
[183.74 → 185.66] It's a national security conference.
[185.66 → 192.00] And I'm going in to talk about AI data and software in the context of national security, intelligence and defence.
[192.28 → 193.88] So that'll be exciting.
[194.62 → 194.84] Yeah.
[194.94 → 195.16] Yeah.
[195.16 → 196.10] I'm looking forward to it.
[196.10 → 199.38] It'll be the day after this episode is released.
[199.48 → 199.82] Yeah.
[199.96 → 204.28] So I will put a link in the show notes in case anybody wants to hop in.
[204.32 → 206.04] I believe it's free to attend.
[206.16 → 209.48] So if anybody wants to do that, and we'll see what happens there.
[209.48 → 209.96] Yeah.
[210.62 → 222.34] We're also kind of gearing up quite a bit because in December is EM NLP, which is the sort of biggest natural language processing research conference.
[222.70 → 226.72] One of the main ones, but I think kind of considered the main one.
[226.72 → 230.00] And that's in December in Abu Dhabi.
[230.00 → 232.40] And I'm going to travel there with a couple of colleagues.
[232.40 → 239.72] So that'll be one of the kind of bigger excursions I've taken after COVID time.
[239.80 → 242.12] Excited to be there at EM NLP.
[242.36 → 244.08] And we had a paper accepted.
[244.38 → 249.42] So I'm excited to present that there and also hear from the rest of the community.
[249.42 → 263.82] Actually, it's interesting because some of what we've released with what we did release and what we are releasing with this paper at EM NLP, we had to think a little bit about like licensing around those things.
[263.82 → 268.66] And I don't know if you remember, I forget which episode it was recently.
[268.66 → 272.88] We were talking about these open rail licenses for models.
[273.22 → 281.30] So the idea that, OK, for data, you have, you know, maybe like Creative Commons or licenses like that.
[281.30 → 288.16] For software, you might have Apache or MIT or GPL or whatever it is.
[288.50 → 293.98] But models fit into this weird space where they aren't quite either of those things.
[294.14 → 295.88] So how do you license them?
[296.02 → 299.76] And people at various groups have tried various things.
[299.76 → 304.42] But there's an effort called Rail Responsible AI Licenses.
[304.90 → 310.10] And I think if you just go to licenses.ai, you can learn more about what they're doing.
[310.10 → 315.52] But we made an attempt at some of our benchmark models that go along with our paper.
[315.72 → 322.32] We made an attempt at creating one of these rail licenses for the release of those.
[322.46 → 324.56] And that was quite an interesting experience.
[325.06 → 331.08] I don't know if you remember kind of the tenets of what goes into a rail license at all.
[331.34 → 331.90] Do you remember that?
[332.42 → 334.76] I remember I say this halfway tongue in cheek.
[334.76 → 340.56] I remember thinking I'm in the wrong industry for this because I may need to blow things up with inference.
[341.00 → 341.38] Oh, yes.
[341.52 → 344.16] If I recall, they don't want me to blow things up.
[344.24 → 345.40] So that stuck in my head.
[345.76 → 346.30] Yeah, yeah.
[346.42 → 347.96] So there's really this.
[348.36 → 355.36] I think the biggest thing that people can keep in their mind with these responsible AI licenses is that there's usage restrictions.
[355.36 → 365.94] So, Chris, just because there's a rail license doesn't mean that you couldn't blow things up or, you know, run a drone or something with your model.
[366.76 → 373.54] But it would mean that if they put that in the restricted use clauses of the license, right?
[373.54 → 385.88] So how this works is there's kind of a main bit of the license, and it says various things about, you know, copyright and patent and warranty and all these things that you might see in a normal license.
[386.04 → 396.02] But all of those things are subject to the terms of the license and the terms of the license have been subject to this clause at the end of restricted usage.
[396.02 → 416.98] So, for example, like the recent release of Stable Diffusion used a rail license, an open rail license, and they put in restrictions around like don't use this for misinformation or to harm others or, you know, various things like that.
[417.32 → 421.78] So they recognize there are dangers with these models, and they want to put some barriers around that.
[421.78 → 432.44] So that's kind of the idea with these rail licenses is that it's a way to distribute and make your model available with certain guardrails around usage.
[432.66 → 433.06] I don't know.
[433.14 → 435.14] What are your general thoughts on that?
[435.48 → 437.56] No, I mean, I think we need that.
[437.66 → 439.44] And that's part of the maturing of this industry.
[439.78 → 447.38] And, you know, we had that for a long time with those other types of intellectual property in terms of things like software and such.
[447.38 → 456.40] And so I remember as we did that episode not too long ago, it felt like a good time for that to happen at this point because it was one of those questions people have been having.
[456.88 → 465.68] And by the way, I should just for the sake of being responsible, let people know that I'm not blowing things up, nor is my employer asking me to blow things up.
[466.02 → 466.68] They don't do that.
[466.74 → 467.92] They don't ask me to blow things up.
[468.08 → 470.76] So I sometimes use sarcasm on this show.
[470.86 → 473.14] We use sarcasm on the show from time to time.
[473.14 → 478.82] But I thought maybe I should just specify that I'm not I'm just claiming blowing anything up at all.
[478.90 → 479.64] So there we go.
[479.64 → 498.04] Yeah, I think, though, like in our license, we kind of balanced a couple of things around the restricted use that probably would restrict your usage of our models in certain cases, Chris, not because of like military usage necessarily, but commercial usage.
[498.04 → 509.20] So one of the things that we wanted to do internally because of how we had sourced our data and the fact that this data actually came from local language communities.
[509.20 → 522.44] So it's actually we trained our models on books that were written by local language community members, and they released those books under certain rights, some of those being non-commercial licenses.
[522.44 → 539.70] And so we wanted to make sure that we both honoured that, but we also released the models because what can sometimes happen with language data is like big companies could use language data from language communities to make money without any real benefit going back to those language communities.
[539.94 → 540.06] Right.
[540.46 → 544.52] And so that was partly also in our mind with this license.
[544.52 → 547.92] And so we put in our restricted use two things.
[548.12 → 551.32] One, a restriction around commercial usage.
[551.64 → 557.72] This would be like in our thinking around, you know, what benefit goes back to the language community.
[557.72 → 566.92] But then secondly, putting in there a restricted use around uses that are particularly discriminatory against indigenous peoples.
[567.26 → 573.78] So you could use indigenous language data to discriminate against indigenous peoples.
[573.78 → 574.04] That's a good point.
[574.20 → 574.40] Right.
[574.52 → 574.86] Yeah.
[575.20 → 583.44] And there's actually a nice clause in the UN statement on indigenous people where they talk about discrimination against indigenous people.
[583.44 → 587.24] And so we kind of pulled a reference to that into our restricted use.
[587.34 → 588.24] So I don't know.
[588.32 → 590.12] It's our try at this.
[590.34 → 602.68] It was an interesting exercise to actually try to put this into practice and figure out like, OK, we talked about this on the podcast, but can I actually create one of these licenses for my own models?
[602.68 → 605.04] It was an interesting exercise.
[605.04 → 616.94] So I really like the fact that you were thoughtful enough, for instance, on the question of discriminatory practices against indigenous folks to think about that and make sure that was in.
[616.94 → 626.82] But another thing that I was wondering as you were discussing that was, you know, kind of going back to the start of this particular topic a moment or two ago on the show.
[626.82 → 639.50] So, you know, there's software, there's software, there's data, there's the model, there's all of these intellectual property, you know, overlaps between different types of IP and they're relying on independent.
[639.50 → 650.16] Did you have any question in your mind as you went through the process about whether a license from one type of thing such as software could clash with the model license?
[650.30 → 653.14] And did you have to think about that and kind of resolve that a little bit?
[653.14 → 669.60] Yes. So there was this idea that the data that we were using in this case, it was from the Bloom Library, which is a product from SIL where people can create their own books online.
[670.22 → 674.44] So each book, the author releases that under a certain creative.
[674.70 → 678.90] Well, not all are creative commons, but the majority are creative commons licenses.
[678.90 → 696.24] Sure. And so we had to look into whether the models that we were creating off of creative commons data would be subject to the same sort of restrictions as the creative commons data that we were training it on.
[696.24 → 708.44] And so there are various writings, you know, within you can actually look up creative commons has some commentary on this of when certain things are derivative works or adaptations and that sort of thing.
[708.44 → 717.24] In our case, the models that we trained off of this data, whether it's surprising or not, according to how we read, those were not derivative works.
[717.24 → 722.14] And so wouldn't be restricted to the same sort of license.
[722.68 → 736.12] However, what we tried to do was we tried to match the kind of restrictions of the original data just in good faith to how people might have expected that data to be used.
[736.12 → 740.38] But I think technically we had more latitude there.
[740.80 → 745.14] No, that sounds good. And I'm not surprised that you and your folks were doing that.
[745.42 → 750.68] I would hope that everybody out there in the larger community would be thoughtful in that way about it.
[750.68 → 764.20] It's interesting as we've talked so many times about kind of having these different, you know, these different constructs, you know, blending, you know, having software blending with the data blending with the models now and getting them out.
[764.28 → 770.46] But we just haven't spent a lot of time talking about kind of the legalities of how to do that and how to honour those across the format.
[770.46 → 771.42] So good to hear.
[784.38 → 794.98] So, Chris, I don't know if you remember not that long ago in one of our recent episodes, which we can link in the show notes, we had Josh from Kochi on.
[794.98 → 799.12] And we even made some clones of our voices and that sort of thing.
[799.32 → 800.66] That was a lot of fun.
[800.84 → 807.20] So Kochi's doing amazing things in sort of open source speech technology and really enabling a lot.
[807.28 → 811.66] Actually, we're using a lot of their libraries in our own work.
[811.66 → 829.54] But they had an announcement that I, you know, I thought I'd share in terms of the new side of things, which are you can now join their wait list and get access to what they're calling their like voice studio audio manager advanced editor features within their system.
[829.96 → 832.86] Sorry if I'm not getting the names right, but it's pretty cool.
[832.86 → 850.32] This is I don't know if you remember when he was on the episode, but he talked a little bit about how they were thinking about managing the sort of tone, emotions, expressions of synthesized voices more flexibly.
[850.32 → 857.02] So you don't just get sort of one synthesized voice, and it's kind of either monotone or having the same expression throughout.
[857.14 → 863.98] You can actually match different portions of your content with different kind of expressive qualities.
[864.62 → 866.38] And that's what this talking about it.
[866.48 → 867.92] Yeah, this voice studio does.
[868.14 → 880.30] And there's some pretty cool things where you can actually look at different words and the different phonemes in those words and adjust some of these expressive features, emotion and pitch and mixing.
[880.30 → 886.42] Mixing every mixing different voices together as well, like to create a mix of synthesized voices.
[886.42 → 895.28] You can do all this within this kind of advanced editor, which seems really possible or really powerful is what the word I was looking for.
[895.70 → 906.54] Yeah, I'm really looking forward to using it, but I'm a little dismayed that I'm currently in number 6466 in line to receive it.
[906.54 → 909.50] So it may be a little while before I receive the joys.
[909.50 → 911.42] Well, shout out to Josh.
[911.42 → 915.44] If you're is you're out there listening, you can bump Chris up the waitlist.
[915.44 → 924.04] But yeah, I think it's fascinating where, you know, it's one thing to like to produce a synthesized voice.
[924.04 → 943.30] It's another thing to kind of have multiple voices, maybe in a video that you're mixing down and mix voices together, change the expressive qualities like the sort of almost like working with synthesized voices like people do with like computer production of music.
[943.30 → 944.30] Right. Right.
[944.30 → 948.60] Where you can change things and mix things together and all of that very fluid.
[948.60 → 953.62] So I want to ask you a question that's very specific to the work that you're doing on a day-to-day basis.
[953.62 → 966.68] And for working with indigenous populations and their languages and stuff, what are some of the ways that you think that this will change that going forward or add, you know, add to it that you guys have been talking about?
[966.68 → 970.68] Like, what's the future look like for someone in your line of work on that?
[970.78 → 973.40] I'm I'm just curious about that kind of real world aspect.
[973.40 → 995.40] Well, yeah, I think that there 's's definitely the side of this, which is probably the more commercial side of it, which is, you know, media production and that sort of thing where, like, let's say that you produce a video in one language and, you know, you're wanting to do the dubbing across languages or something like that.
[995.40 → 1002.72] Or maybe even you're using like an avatar and using synthesized voices in your video and the whole thing is synthesized.
[1002.90 → 1005.28] I mean, that's happening quite a bit right now as well.
[1005.28 → 1022.32] And so the ability to bring in multiple voices and do all that without going into a recording studio, of course, that has huge applications for like advertising, marketing, media production, entertainment, all of those different areas, which is where I would guess.
[1022.32 → 1032.92] And I can't speak to Kochi's business model, but I would guess that their tooling is quite applicable across those areas for local language communities.
[1032.92 → 1041.40] I think, of course, they're also involved oftentimes in the production of media or content for their communities so that that's also relevant there.
[1041.50 → 1045.72] But I think there's also unique things that are relevant in those scenarios.
[1045.72 → 1060.16] So imagine that you're part of an indigenous community, a local language community, and you are kind of marginalized by the national government or discriminated against in one way or another.
[1060.16 → 1070.72] It might be a kind of big ask for you to for your community to say, hey, could we put up 100 hours of content with your voice and maybe your likeness?
[1070.96 → 1071.10] Right.
[1071.56 → 1074.80] That's potentially painting a target on yourself.
[1074.80 → 1075.22] Right.
[1075.46 → 1075.70] Yeah.
[1075.78 → 1080.24] When you're associating yourself, and you're the face of that that community.
[1080.24 → 1097.96] So I think it's fascinating that there are tools like this where you could create high quality voice and expressive voice that's maybe synthesized and not someone's maybe even style transferred where it's not someone's voice that can be tracked to a certain person.
[1097.96 → 1102.34] But then if you think about then combining that with the video elements.
[1102.34 → 1108.28] So think about having a video that maybe is recorded with someone talking.
[1108.44 → 1118.10] You can use things like Stable Diffusion and other things now to actually shift that video and obfuscate the identity of the person in that.
[1118.54 → 1124.34] Now, the more nefarious use of that, of course, would be misinformation and of course, fakes and that sort of thing.
[1124.34 → 1133.82] But there is a very positive use of this for these sorts of communities where it is important that they want to produce media content for their community.
[1134.08 → 1150.48] But if you're marginalized or discriminated against, it's interesting now that there are these tools that are accessible to and have really nice user interfaces accessible to community members where they could actually produce some of that content themselves.
[1151.12 → 1151.30] Yeah.
[1151.46 → 1153.08] So it's interesting dynamic.
[1153.08 → 1167.28] To your point, I'm just kind of thinking about in my world a little bit and thinking about the fact that, you know, as we're recording this in the current day and current months, the war in Ukraine, in which the Russian invasion of Ukraine has been going on.
[1167.72 → 1171.98] And Belarus is also part of that Russian effort.
[1171.98 → 1187.70] And I was reading this in the current day, and I was reading this morning an article about some dissidents that are, you know, trying to, A, survive, you know, that situation and, B, escape and, you know, and try to help and do the things that they, that their conscience is dictating.
[1187.70 → 1200.96] And that I kind of going back to, to some of the ideas that you just enumerated about marginalized populations of indigenous populations and, and being able to kind of find some protection while generating content.
[1201.10 → 1203.76] I could, I could imagine that in this as well.
[1203.76 → 1213.62] And so, I mean, you saw it sort of way in the past with online hackers and when they would like hack SeaWorld or whatever, they would release a video.
[1213.96 → 1215.88] We are anonymous or whatever.
[1215.88 → 1218.38] And, and it would all be synthesized voices, right?
[1218.44 → 1221.18] Because you don't want someone, you don't want to put your voice on that.
[1221.40 → 1221.54] Right.
[1221.86 → 1222.32] That's right.
[1222.32 → 1231.16] And don't get me started on animal protection because it will stop being an AI podcast, and we will just go off into a totally different realm.
[1231.16 → 1233.62] So, so be good to your animals folks.
[1233.74 → 1234.74] That's our little sideline.
[1234.96 → 1235.28] Yeah.
[1235.54 → 1235.96] Right here.
[1236.04 → 1246.94] Do you think one question that was actually brought up to me last week, which I think is kind of an interesting question for people like us that do produce content.
[1246.94 → 1258.32] I mean, this is just our voices recording our voices on this podcast, but let's just imagine that, you know, Kochi or whatever their voice studio.
[1258.94 → 1263.04] It's great enough that we can just, I mean, we already have a lot of sample of our voice, right?
[1263.04 → 1268.90] If we can create really nice voices, you and I could just type out a script back and forth.
[1268.90 → 1276.94] And, you know, when we're travelling, quote, record a podcast and just mix our voices together with content and, and release it.
[1277.02 → 1278.86] How does that sort of thing strike you?
[1278.90 → 1289.60] Because I got into this conversation with someone last week and there was some sort of mixed feelings about you, you know, what you lose when you do that or what you gain when you do that.
[1289.92 → 1292.10] So that's a great point that you make there.
[1292.10 → 1300.42] And, and who knows, maybe we both have tough schedules and for listeners who don't know for Daniel and me, this is a passion project.
[1300.42 → 1305.88] And so, you know, who knows, maybe there is a moment of tight schedule for us where we do exactly that.
[1305.88 → 1312.68] I think the thing we would lose is that there is the there is the element of the unexpected in our conversations often.
[1313.16 → 1316.08] And, and a lot of banter back and forth.
[1316.08 → 1318.64] That's not scripted, completely unplanned.
[1318.64 → 1322.08] I know people think that we plan every word out, but we don't.
[1322.68 → 1324.54] And so maybe that would be lost.
[1324.60 → 1330.76] So you might get the information you wanted to share out, but you may lose a little bit of the human element behind it.
[1331.14 → 1331.24] Yeah.
[1331.50 → 1339.64] The context for the conversation I had last week was it was someone who does produce video content specifically.
[1340.32 → 1343.86] And so their face is sort of part of their brand, right?
[1344.10 → 1344.36] Yes.
[1344.36 → 1350.42] And so the question was, well, if we dub your video into another language, it would make sense.
[1350.50 → 1355.64] You know how everyone hates the thing about dubbed video where the lips don't match the voice, right?
[1355.72 → 1358.56] And you can kind of sync it up pretty good in a lot of cases.
[1358.56 → 1367.34] But ultimately the, you know, what you could do is just modify the person's face and lips to match the dubbed.
[1367.34 → 1376.84] You know, they recorded the video in English, but now we're dubbing it to Chinese, and we match up their lips using some sort of video manipulation.
[1376.84 → 1383.74] They reacted very negatively to that because they're like, my face is like my brand, right?
[1383.82 → 1385.56] Like I don't want anyone messing.
[1385.94 → 1396.66] They actually said they prefer the dubbed content because their original like expression of how they express themselves in the video was what was important to them.
[1396.88 → 1398.54] So yeah, it was interesting.
[1398.98 → 1400.16] I'm going to challenge that.
[1400.16 → 1414.10] I'm going to suggest to you that in the not so distant future, not only will that exist, but when you're getting on, you know, we're all through COVID and certainly continuing post COVID, we're all on video calls all the time.
[1414.10 → 1423.12] And so I'm going to suggest that that's going to be one of those killer features that one of the video call providers is going to do.
[1423.26 → 1436.54] And that is not only doing translation in real time, which I think is entirely possible in the, you know, not so distant future, but using some of these technologies we've been talking about in recent episodes to do exactly that.
[1436.54 → 1446.56] Because especially if you're using their service quite a lot, which some of us are, then they also have a thorough data set to train on.
[1446.88 → 1452.34] And I think that with the video and everything, I think, I just think that's going to be very doable, not too far down the road.
[1452.54 → 1455.68] And I think it'll also be able to, to be done live.
[1455.98 → 1458.56] So I think it will be part of what we do.
[1458.86 → 1462.94] I think you and I will find ourselves doing that before long is what I'm, what I'm suggesting.
[1466.54 → 1496.52] I think it will be part of what we do.
[1496.54 → 1514.78] So Chris, one of the things that we had just kind of started talking about before we started recording was you were asking a few questions about graph neural networks, which I've thought have been interesting for quite some time.
[1514.78 → 1519.76] And I think you ran across it in some NVIDIA post or something like that, right?
[1520.08 → 1522.82] So NVIDIA has a blog that's widely read.
[1522.82 → 1525.04] They blogged as we record this.
[1525.18 → 1530.68] It was actually just two days ago on the 24th of October 2022.
[1531.30 → 1535.18] But they had a blog about kind of what are graphed neural networks.
[1535.38 → 1538.08] And it occurred to me, I was kind of glancing through it.
[1538.26 → 1541.60] And there's a fair amount of stuff that I'm familiar with in it.
[1541.62 → 1544.14] And there were a few items there that I hadn't thought about.
[1544.14 → 1552.54] But it occurred to me that we have kind of touched on graph neural networks quite a number of times on the show without ever really diving into it.
[1552.62 → 1558.30] So maybe there is a fully connected episode where we do a full show to dive into the detail.
[1558.30 → 1566.98] But it made me start wondering a little bit about how many of our listeners out there are using graph neural networks and some of the use cases.
[1567.12 → 1572.20] I saw something the other day about starting, and this is very typical for some of our conversations,
[1572.20 → 1578.38] where you're putting together multiple kind of deep learning approaches to try to get something new.
[1578.44 → 1581.36] And we've had a lot of shows talking about that.
[1581.46 → 1586.56] But before I go on, have you had any opportunities to use graph neural networks yourself?
[1586.56 → 1593.52] I recently did train a graph neural network for a question answering task.
[1593.80 → 1599.96] So one of the areas where people have applied this is to this task of automated question answering,
[1600.22 → 1608.52] where there's a text prompt, and you're looking for the answer within some set of documents or something like that.
[1608.86 → 1611.14] So I did dive a little bit into that.
[1611.28 → 1613.80] And to be honest, I'd love to learn more.
[1613.90 → 1616.02] That was definitely an interesting experiment.
[1616.02 → 1623.64] As I was kind of diving into that and learning, you know, what does it mean to have a graph neural network?
[1624.10 → 1626.00] Well, there are certain approaches.
[1626.00 → 1631.42] And for maybe graph neural network people out there that are experts, maybe I'm simplifying this too much.
[1631.42 → 1639.08] But there seems to be a cluster of techniques that are focused on representing graph structure data,
[1639.44 → 1643.54] a sort of flat form or a matrix or tensor form, right?
[1643.54 → 1651.36] And so there are ways to embed a graph or learn an embedding for a graph in a sort of flat form.
[1651.78 → 1659.48] There's also methods that exploit the structure of the graph neural network or the graph itself,
[1659.48 → 1663.18] which I think is what I think of when I think of graph neural networks.
[1663.18 → 1668.88] So one way to, I guess, think about it is if you think about a convolutional layer, right,
[1669.04 → 1675.52] you're running some kernel or filter over your image or your set of inputs.
[1675.70 → 1683.20] But what you're doing is you're always considering like one data point in the context of a fixed number of other data points,
[1683.20 → 1686.66] even if you're running your filter over in some various ways.
[1687.02 → 1690.82] It's sort of one data point in relation to a number of other fixed data points.
[1690.82 → 1698.00] And actually, you know, transformers or recurrent neural networks and this sort of thing also behave similarly, right?
[1698.08 → 1703.88] You're comparing one data point in reference to maybe a sequence of other things,
[1703.88 → 1707.14] but which have a fixed sort of structure.
[1707.14 → 1713.60] And what's interesting, I think, about graph neural networks is that the graph neural networks that I'm thinking,
[1713.80 → 1718.00] which are built around these concepts of message passing,
[1718.52 → 1724.38] consider one data point in reference to sort of arbitrary structure of other data points.
[1724.88 → 1733.54] And what happens in these graph neural networks is that you have a stage where you take an embedding for one node in your graph
[1733.54 → 1739.46] and you look at all the neighbouring nodes or maybe a certain number of neighbouring nodes,
[1739.82 → 1748.00] but all the neighbouring nodes that fit within a certain structure, and you combine or concatenate or perform a function
[1748.00 → 1754.80] over the combination of the embeddings for those nodes and the embeddings for the node that you're considering.
[1755.04 → 1758.66] And so what happens as you apply this across all the nodes of your network,
[1758.66 → 1763.06] you actually pass a lot of information between all the nodes of your network.
[1763.06 → 1769.88] And if you iterate that, then the idea is like all of this messaging and information
[1769.88 → 1777.68] is transferred from all of this different complicated graph structure to the data point under consideration.
[1778.36 → 1782.96] And so oftentimes this involves this sort of message passing and iterative approach,
[1782.96 → 1787.44] which is quite interesting and has been applied in a variety of ways.
[1787.44 → 1796.28] One of the ways, of course, that's maybe very well known is alpha fold, which is one of the protein folding approaches.
[1796.96 → 1799.28] We had a show about that not too long ago.
[1799.66 → 1804.74] So one of the things is you're looking, you know, in your line of work at large language models,
[1804.74 → 1808.84] and we're looking at graph neural networks and how they can merge.
[1808.84 → 1810.20] And you're talking about the flat structure.
[1810.36 → 1817.70] And I know NVIDIA kind of talks about the unstructured nature of the message passing within the graph itself
[1817.70 → 1821.10] compared to other neural networks that are a lot more structured.
[1821.60 → 1827.58] Can you clarify for a moment, like, what does it change in terms of how you're approaching large language models
[1827.58 → 1833.12] when you have this flat, unstructured node approach where you're doing the message passing
[1833.12 → 1835.42] and you have an arbitrary number of them that are there?
[1835.74 → 1841.90] Does it dramatically change the workflow for when you're working on those large language models or is it similar?
[1842.42 → 1853.48] Yes. So, I mean, a lot of times the large language models take a very naive approach to how text is structured.
[1853.48 → 1860.94] So most language models now work around something called subwords, which means I have a piece of text.
[1860.94 → 1866.54] I'm going to split that up into subcomponents, but not necessarily words.
[1866.54 → 1869.40] Like, you could tokenize something into words.
[1869.70 → 1875.58] But the problem with that is, like, how do you know how to tokenize what is a word, and what isn't a word?
[1875.64 → 1877.92] You've got all this sort of weird structures in language.
[1878.46 → 1885.34] The other thing is, if you tokenize into words, what happens when you see an unknown word in your input?
[1885.34 → 1893.22] And so what often happens is you figure out what are the most frequently occurring subwords across my corpus of known language.
[1893.90 → 1901.92] And so maybe, you know, like your name, Chris, there's a subword, you know, C-H-R-I.
[1902.14 → 1907.84] And then you tack on an S subword and that forms your name, right?
[1907.84 → 1914.16] And so if you figure out what are those frequently occurring subwords, that's how you split things apart.
[1914.30 → 1921.36] And that's how you sort of look at the attention across these different subwords in a large language model.
[1921.90 → 1927.60] But that's somewhat, I mean, it's statistical in terms of how you get those subwords.
[1927.80 → 1930.14] And, you know, it's useful.
[1930.40 → 1936.76] But with language in general, language is much more structured in many cases like a graph.
[1936.76 → 1941.58] And so to do this sort of large language model approach works well.
[1941.70 → 1946.98] And it's scalable because you don't have to know as much about the structure of your input.
[1947.18 → 1954.08] But if you do know more about the structure of your input, you can do maybe really powerful things with less data, right?
[1954.44 → 1959.44] So, for example, if you know all the parts of speech of your language, right?
[1959.44 → 1967.68] Like, here's my noun subject, and it's connected with a verb via node in the graph, right?
[1967.72 → 1968.44] In this way.
[1968.52 → 1974.54] And you draw out all the tree structures and the syntax of your language.
[1974.76 → 1983.94] There are tons of information encoded into that structure that you lose when you just treat words like a sequence of subwords, right?
[1983.94 → 1989.28] And I think there are arguments that these large language models do learn some of that structure.
[1989.72 → 1991.74] There's some work out of Stanford on that.
[1992.14 → 2004.56] But the way that language is structured, I think the hope would be that if you're creative about encoding this linguistic information into your model and then maybe using something creative like a graph neural network,
[2004.56 → 2014.62] maybe you can do more things with less data, or you can do really powerful things, or you can be more robust to sort of changes and that sort of thing.
[2014.92 → 2015.98] I see. Good explanation.
[2016.54 → 2024.66] And yeah, if other people have input on graph neural networks or have used them in certain ways, definitely let us know.
[2025.08 → 2032.76] One of the other interesting ones that I know just doing kind of searching when I was looking into graph neural networks is from Pinterest.
[2032.76 → 2047.26] I guess the system that does recommendation of items for users within Pinterest is their real time system for recommendation is built on some sort of graph neural network called Pixie,
[2047.84 → 2053.30] which, yeah, if any of you are on that team out there, and you want to come on the show and talk to us about it, would love to hear more.
[2053.42 → 2054.10] But you can look up.
[2054.16 → 2056.48] They do have a paper about it and all of that.
[2057.20 → 2057.28] Absolutely.
[2057.42 → 2062.10] I know that in the NVIDIA article that we were talking about, they mentioned LinkedIn does the same.
[2062.10 → 2066.58] I would imagine that other social networks do as well, quite honestly.
[2066.92 → 2071.16] It seems like a very logical fit in terms of trying to get that functionality.
[2071.62 → 2071.70] Yeah.
[2072.04 → 2077.96] Well, as we kind of get near the end here, Chris, I mean, we always try to share some sort of learning thing.
[2078.08 → 2084.40] And as I was learning about graph neural networks, I found several interesting resources.
[2084.40 → 2093.64] But one which if you're into sort of paid courses, this one seems to be quite full of great information about graph neural networks.
[2093.78 → 2095.66] So this is from Zach Most.
[2095.84 → 2099.78] He actually has a YouTube channel called Welcome AI Overlords.
[2100.34 → 2103.78] But he's really into graph neural networks.
[2103.78 → 2108.98] I think he works in, has worked in sort of variety of big tech places.
[2109.84 → 2115.18] And he has a full course of, you know, introduction to graph neural networks.
[2115.18 → 2119.78] If you just go to graphneuralnets.com, pretty simple link.
[2119.78 → 2127.76] Then you can see as introduction to graph neural networks, foundational theory of graph neural networks, basics of graph neural networks.
[2128.24 → 2130.98] And the basics of graph neural networks is free.
[2131.22 → 2136.94] So at least you could get like the sense of the graph neural networks from the free version.
[2136.94 → 2142.54] Well, I may very well be a student on that course and maybe some of the other stuff out there as well.
[2142.90 → 2149.70] I have a very specific doing graph database work that I'm working on in my day job without going into specifics.
[2150.18 → 2157.26] And I can totally see how one of the associated problems with that could be solved by graph neural networks.
[2157.72 → 2161.20] And so I think it's time for me to go level up.
[2161.50 → 2165.56] And I encourage our listeners that maybe not already in that to go consider it as well.
[2165.56 → 2166.62] Sounds great, Chris.
[2166.62 → 2168.62] Well, it's been fun as always.
[2168.78 → 2175.88] Good to connect our two nodes via the edge of practical AI, as always.
[2176.30 → 2177.58] So, oh boy.
[2177.84 → 2178.48] Oh boy.
[2178.54 → 2181.88] That was like the AI version of a dad joke right there.
[2182.34 → 2182.82] All right.
[2182.94 → 2186.64] Well, on that note, Chris, we'll see you before I make another joke.
[2187.14 → 2187.50] Okay.
[2187.58 → 2188.08] No worries.
[2188.20 → 2188.92] Have a good one, Daniel.
[2189.12 → 2189.54] Thanks.
[2189.74 → 2189.90] Bye.
[2189.90 → 2189.94] Bye.
[2196.62 → 2199.60] All right.
[2199.60 → 2201.34] That is our show for this week.
[2201.60 → 2203.96] If you dig it, don't forget to subscribe.
[2204.54 → 2207.14] Head to practicalai.fm for all the ways.
[2207.66 → 2213.06] And if practical AI has benefited your life, pay it forward by sharing the show with a friend or a colleague.
[2213.44 → 2216.40] Word of mouth is the number one way people find shows like ours.
[2216.40 → 2225.66] Thanks again to Vastly for fronting our static assets, to Fly.io for backing our dynamic requests, to Break master Cylinder for the beats, and to you for listening.
[2225.90 → 2226.56] We appreciate you.
[2226.80 → 2227.76] That's all for now.
[2227.98 → 2229.46] We'll talk to you again on the next one.
[2229.46 → 2241.84] Take care.
[2241.92 → 2242.38] Take care.
[2242.38 → 2242.50] Hello.
[2242.50 → 2242.66] Take care.
[2242.96 → 2243.04] Take care.
[2243.04 → 2243.22] Take care.
[2243.22 → 2244.06] Take care.
[2244.06 → 2244.12] Take care.
[2244.12 → 2244.22] Take care.
[2244.52 → 2245.18] Oh, my God.
[2245.18 → 2246.14] Take care.
[2246.14 → 2246.48] Take care.
[2246.66 → 2247.22] Welcome to Amy.
[2247.22 → 2248.30] Welcome to the град Andre side of the emergency.
[2248.30 → 2248.84] We will have to go to all the בש.
[2248.84 → 2250.76] Be welcome to LA patients that ice-skate Vaasa sneezed that women do not win with –
[2250.76 → 2251.76] Nobody gives you a much individual, a little bit to be liberal as the Channel-store.
[2251.76 → 2253.08] Bye bye bye.
[2253.08 → 2255.16] Bye bye.
[2255.16 → 2255.76] Bye bye.
[2255.76 → 2256.54] Bye bye.
[2256.54 → 2257.22] Bye bye.
[2257.22 → 2258.18] Bye bye.
[2258.18 → 2258.98] Bye bye.
[2258.98 → 2259.44] Bye bye.
