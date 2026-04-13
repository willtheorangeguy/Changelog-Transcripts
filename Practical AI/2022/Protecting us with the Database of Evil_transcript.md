[0.00 --> 6.78]  What we do is we basically combine this like very, very deep subject matter expertise with our technology.
[6.96 --> 8.04]  So we're a technology company.
[8.62 --> 18.88]  And yeah, we also have sort of experts in the field, in the domain, like experts in the field of researching human trafficking and really understanding that space or in misinformation and different types of misinformation.
[19.10 --> 21.32]  And in hate speech and in terror.
[21.76 --> 28.58]  And so they speak the languages, you know, they research the space, they understand it, they know the key players, they know the different organizations, the keywords.
[28.58 --> 31.24]  And, you know, this is an adversarial space.
[31.36 --> 32.32]  It's constantly changing.
[32.52 --> 34.66]  And so they make sure that they stay up to date.
[35.00 --> 43.22]  And then what that means is that us on the data side, we can basically take their ideas, take their knowledge, and then engineer features out of those.
[43.34 --> 43.44]  Right.
[43.46 --> 46.48]  So really translate the human knowledge into our models.
[46.62 --> 50.24]  So then we can go out and automate that and do it at scale.
[58.58 --> 68.32]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive, and accessible to everyone.
[68.68 --> 69.48]  Subscribe now.
[69.64 --> 73.46]  If you haven't already, head to practicalai.fm for all the ways.
[73.84 --> 79.46]  Special thanks to our partners at Fastly for delivering our shows super fast to wherever you listen.
[79.78 --> 81.62]  Check them out at fastly.com.
[81.62 --> 84.02]  And to our friends at fly.io.
[84.38 --> 87.98]  We deploy our app servers close to our users, and you can too.
[88.32 --> 90.24]  Learn more at fly.io.
[96.32 --> 99.46]  Well, welcome to another episode of Practical AI.
[99.82 --> 101.24]  This is Daniel Whitenack.
[101.34 --> 104.08]  I'm a data scientist with SIL International.
[104.40 --> 109.74]  And I'm joined as always by my co-host, Chris Benson, who's a tech strategist with Lockheed Martin.
[109.74 --> 110.62]  How are you doing, Chris?
[110.62 --> 112.20]  Doing very well today, Daniel.
[112.26 --> 112.70]  How's it going?
[113.26 --> 114.18]  It's going great.
[114.62 --> 118.40]  So yesterday was voting day here in the U.S.
[118.60 --> 118.70]  Indeed.
[118.70 --> 120.72]  And I did go to the voting place.
[120.90 --> 130.32]  And it was interesting because in line, I could hear people talking about cyber threats to the voting machines and other things like that.
[130.32 --> 141.54]  And so my mind was already actually thinking about these things because we have a really interesting topic to talk about today that's in that same vein.
[141.90 --> 148.40]  We're privileged today to have with us Matar Haller, who is VP of data at ActiveFence.
[148.60 --> 149.42]  Welcome, Matar.
[149.70 --> 150.04]  Hi.
[150.04 --> 151.04]  Thanks for having me.
[151.68 --> 152.12]  Yeah.
[152.36 --> 155.74]  And ActiveFence, I've read a bit about it.
[155.82 --> 170.08]  And the sort of website talks about this like barrage of threats that is, you know, online platforms are susceptible to now, which ActiveFence is addressing in various interesting ways, which we'll get into.
[170.08 --> 182.72]  But I'm wondering if you could kind of give us a picture, like if I'm going to run an online platform of some type, maybe it's not even like, you know, I'm likely not going to start and run the next Facebook.
[182.72 --> 191.08]  But I might very well, you know, start and run some type of software company that provides an online platform to do something.
[191.08 --> 200.52]  What should be on my mind and what's the reality of kind of online threats that I might need to be aware of if I'm getting into that space?
[200.88 --> 201.10]  Yeah.
[201.26 --> 217.54]  So first of all, I think there's one thing to think about is that anytime that you have a platform that has any type of user generated content, whether users are uploading photos or they're chatting or they have comments or anything like that, you're going to have tons of data very, very fast.
[217.54 --> 227.34]  And just it's prime for people to, you know, post wonderful things, but also some really, really dark things, which we've all sort of seen and been exposed to.
[227.86 --> 232.22]  And so one thing to keep in mind is that trust and safety, just basically safety online.
[232.32 --> 234.60]  It's not really a nice to have anymore.
[234.74 --> 236.68]  At this point, it's a competitive advantage.
[236.82 --> 238.32]  It's kind of a basic expectation, right?
[238.34 --> 239.64]  So users are expecting it.
[240.12 --> 241.44]  Advertisers are expecting it.
[241.78 --> 243.36]  Parents are expecting it.
[243.42 --> 244.36]  The public expects it.
[244.36 --> 249.04]  So if you're going to spin up a platform, so first of all, best of luck.
[249.24 --> 255.86]  And second of all, you need to keep this in mind, like from the get go before you sort of find yourself down this rabbit hole.
[256.16 --> 266.86]  One thing that I think is really important to keep in mind is that although trust and safety isn't a new industry, really, it's really now finally becoming something that people are aware of.
[266.88 --> 268.66]  Like I said, it's this basic expectation.
[268.66 --> 272.88]  Now it's not only users, but also like regulators and legislators.
[273.32 --> 277.12]  There's new legislation coming in that's making it even more at the forefront.
[277.90 --> 283.60]  And the basic sort of content moderation that is out today doesn't really make the cut.
[284.14 --> 289.64]  To follow up like the second part of your question about sort of like what kind of harms are out there.
[290.12 --> 292.98]  So online harm is really multidimensional.
[293.48 --> 296.26]  We can see it in different media types.
[296.26 --> 309.18]  So we've seen it in games and like merchandise sites, chats, text, you know, video, audio, things like that across many, many different languages and also different types of violations.
[309.18 --> 317.76]  So you have, you know, white supremacists and terrorists and human trafficking and sort of these like really, you know, painful sorts of things.
[318.44 --> 323.98]  Also goes into like misinformation, disinformation, fraud, spam, cyberbullying and so forth.
[323.98 --> 330.96]  And so it's this really, really complex space that you need to have a deep understanding of to understand how to address.
[331.72 --> 345.22]  And in the sort of, I guess, up until this point, you were talking about like content moderation and how it has evolved over time, but is still kind of lacking in the sort of traditional sense.
[345.50 --> 346.58]  What does it look like?
[346.58 --> 352.00]  Like, I mean, is content moderation like people might have in their mind, oh, I have a blog, right?
[352.00 --> 361.98]  And I'm going to choose whether I allow people to like post a comment or I have to approve that comment before it's posted or something like that.
[361.98 --> 372.24]  So this sort of content moderation, is it, in your opinion, kind of as where we sit today, is most content moderation sort of reactive at this point?
[372.40 --> 378.80]  Or how do you view like, you know, how are most people approaching the problem right now maybe?
[379.02 --> 380.26]  And why is that lacking?
[380.26 --> 385.16]  So there's kind of different levels, I would say, of content moderation.
[385.54 --> 392.18]  At this point, to just sit and moderate every single comment gets out of hand really, really fast.
[392.74 --> 397.94]  And so there is some level of automation that, you know, started being introduced, right?
[397.98 --> 402.68]  And so the first sort of basic level is let's go out and look for keywords, right?
[402.68 --> 404.50]  Like, I don't want any slurs on my platform.
[404.64 --> 408.68]  I don't want anyone calling anyone any of the like words, you know?
[408.68 --> 410.38]  I don't want that there.
[410.52 --> 412.10]  So I'm going to ban all those.
[412.56 --> 416.88]  I know that people might have, and then people kind of get a little trickier, right?
[416.92 --> 419.32]  And so they'll say, well, you know, what about if we use an emoji?
[419.96 --> 425.14]  And so there's different kinds of emojis or combinations of them that also can be used in a hateful way.
[425.44 --> 428.08]  And so you can say, okay, well, I'm going to ban those.
[428.78 --> 431.26]  And I'm going to ban like these specific keywords.
[431.56 --> 435.32]  And I'm going to ban these engrams because, you know, these phrases are bad.
[435.32 --> 437.78]  Like, I hate Jews or I hate what, you know?
[437.78 --> 439.04]  So I'll ban that.
[439.50 --> 440.56]  And that works okay.
[440.92 --> 446.54]  But very, very quickly, you get to these cases where keywords are either insufficient.
[447.00 --> 450.06]  So like I said, with emojis or with lead speak.
[450.32 --> 453.12]  So you can write for people that aren't familiar.
[453.28 --> 457.42]  It's basically taking a word and replacing letters with numbers.
[457.64 --> 461.72]  So Adolf Hitler can be written like pretty much all in numbers.
[461.72 --> 466.84]  And so it's kind of to evade detections and only, you know, on a need to know basis sort of thing.
[467.14 --> 470.10]  There's also in the keyword space, you have numbers.
[470.44 --> 474.32]  So like 1488 is a white supremacy number.
[474.82 --> 475.50]  88 for Heil Hitler.
[475.64 --> 479.66]  And 14 is like a phrase that they use, like the number of words in the phrase.
[480.24 --> 482.28]  And so you can say, okay, well, I'll add all these to my dictionary.
[482.28 --> 489.02]  But then you get to the place where you say, well, what about someone that's telling someone else, don't call me, you know, some slur.
[489.24 --> 489.98]  Don't call me that.
[490.46 --> 492.64]  And so now they're using the slur, right?
[493.00 --> 494.90]  Is that something that you want to necessarily ban?
[495.42 --> 503.18]  Maybe in some cases, but in other cases, you're going to need sort of a deeper understanding of how language is being used before you just go out and outright ban it.
[503.18 --> 512.34]  And so you see this sort of like evolution in terms of the ways or the approaches that platforms are taking to moderate the space.
[512.80 --> 519.24]  And sort of looking at the context in which language is used is sort of the first step in that.
[519.66 --> 522.68]  I think I just realized, and that was a great explanation.
[522.68 --> 530.58]  And I just realized how sheltered I am because several of the things you referred to, I just didn't know at all.
[530.90 --> 532.78]  So I guess I'm very sheltered.
[532.78 --> 537.70]  But I'm curious, when we were first starting the conversation a few minutes ago, you also mentioned misinformation.
[538.16 --> 542.74]  And we were just kind of diving into kind of some of those specific use cases on hate speech.
[543.20 --> 547.82]  How does misinformation, because we've seen, you know, we've been dealing with hate speech for a long time now.
[547.94 --> 554.02]  But, you know, misinformation, you know, in the last few election cycles has really become a huge issue.
[554.02 --> 558.08]  And obviously in national security issues and things like that, it's big.
[558.36 --> 559.62]  How does that fit in?
[559.62 --> 564.08]  I think in my mind, I've kind of thought about there's hate speech and there's misinformation and all.
[564.60 --> 566.58]  Is there a connection between them all?
[566.68 --> 568.88]  Are they bound together in some way the way you see it?
[568.96 --> 572.42]  Or are these distinct separate kinds of things?
[572.54 --> 573.56]  How do you think about it?
[573.58 --> 575.34]  How do the folks at your company think about it?
[575.54 --> 577.02]  That's a really interesting question.
[577.02 --> 580.94]  To take sort of these two examples of these two specific violations.
[581.44 --> 584.38]  And there's, I think violations are sort of on this spectrum, right?
[584.42 --> 588.96]  And so you can think about these sort of more like evasive violations.
[589.08 --> 595.44]  So things that are, you know, that kind of are more difficult to find or require subject matter knowledge.
[595.44 --> 596.56]  So hate speech, right?
[596.56 --> 597.74]  You need to know these keywords.
[597.86 --> 598.50]  You need to know these things.
[598.92 --> 604.30]  And then you also have these just sort of more like common violations where some of them are like, well, maybe it's not even a violation.
[604.66 --> 609.20]  Like nudity or profanity or things like that, where it's just more out there.
[609.56 --> 611.84]  And everything kind of lies almost sort of on the spectrum.
[611.84 --> 618.70]  And you can go like spam and fraud and so forth until you get to like the really dark, you know, like child safety and abuse and things like that.
[618.70 --> 623.32]  And with misinformation, it's actually interesting because it's not really trying to evade, right?
[623.38 --> 624.90]  Like that's the whole point.
[625.34 --> 628.72]  On the other hand, it's really tricky to find and to understand.
[629.32 --> 637.08]  And there's lots of organizations that do really wonderful work of fact checking and of, you know, like keeping up on the trends and really identifying misinformation.
[637.72 --> 647.68]  And there's also sort of these techniques that we can use to once we've identified sort of like a specific type of misinformation, then we can use it to find that it's going viral and so forth.
[647.68 --> 659.44]  It's a real struggle to understand like, you know, kind of how to put that in context because you could say things in a misinformation context that are, you know, there's no hate speech in it, you know, explicitly.
[659.74 --> 660.30]  There are no banned.
[660.42 --> 661.72]  There's none of that is there.
[661.88 --> 665.18]  And yet, as we've seen in recent years, it can do great harm.
[665.50 --> 673.16]  So it seems like a very hard target to go after and be able to mitigate it in a sane and reasonable way.
[673.54 --> 673.92]  Absolutely.
[673.92 --> 686.66]  I think that's one thing that's really unique about Act Defense and what we do is that we're, what we do is we basically, we combine this like very, very deep subject matter expertise with our technology.
[686.84 --> 687.94]  So we're a technology company.
[688.54 --> 699.34]  And yeah, we also have sort of experts in the field, in the domain, like, you know, experts in the field of researching human trafficking and really understanding that space or in misinformation and different types of misinformation.
[699.34 --> 701.58]  And hate speech and in terror.
[702.00 --> 703.22]  And so they speak the languages.
[703.66 --> 705.26]  They, you know, they research the space.
[705.32 --> 705.96]  They understand it.
[705.98 --> 706.90]  They know the key players.
[707.02 --> 709.28]  They know the different organizations, the keywords.
[709.82 --> 711.76]  And this is an adversarial space.
[711.80 --> 712.84]  It's constantly changing.
[713.00 --> 715.18]  And so they make sure that they stay up to date.
[715.18 --> 724.70]  And then what that means is that us on the data side, we can basically take their ideas, take their knowledge, and then engineer features out of those, right?
[724.70 --> 727.76]  So really translate the human knowledge into our models.
[727.76 --> 731.52]  So then we can go out and automate that and do it at scale.
[731.82 --> 736.68]  The reason that it's so interesting is because, as you all know, models drift, they decay.
[737.20 --> 741.38]  And so you can go out and you can, you know, retrain your model and get new weights and you're great.
[741.70 --> 748.14]  Except if you're in an adversarial space, then not only are you drifting, but your reality is like, it's so not unstable, like not stationary.
[748.26 --> 750.12]  There's just changing from underneath you.
[750.80 --> 754.48]  So as it's changing from underneath you, you need to like hurry up and re-engineer your features.
[754.48 --> 762.72]  And so we're constantly engineering new features, retraining our models, and also thinking about just like what else can we possibly extract from this data that's coming in, right?
[762.74 --> 767.38]  We're analyzing text, video, audio, everything, basically.
[767.48 --> 771.10]  Anything that we can get our hands on and just really milking whatever we can out of it.
[771.48 --> 772.72]  That's super interesting.
[773.02 --> 774.02]  I have so many questions.
[774.50 --> 777.38]  Really interesting, really interesting technology.
[777.38 --> 782.04]  But also like the infrastructure and management part of that is, I'm sure, a great challenge.
[782.04 --> 784.76]  But I'm glad you brought up the modality thing.
[784.88 --> 796.36]  And I also saw, you know, on your website, you talk about different languages as well, which it seems like this is definitely now in terms of the way people communicate online.
[796.68 --> 798.76]  Like you mentioned emojis.
[798.86 --> 804.38]  I was also thinking of like GIFs or GIFs, depending on who you are.
[804.38 --> 811.16]  Or, you know, posting memes with text, you know, in the image.
[811.50 --> 818.52]  There's also, you know, of course, like you're talking about videos and audio messages, all of that.
[818.52 --> 825.68]  I guess as a more general question is language, but sort of like multimodal language.
[825.68 --> 831.14]  Is that like your like primary area of research?
[831.14 --> 849.04]  Or are there other things like outside of communication in terms of like the threats posed to sort of online platforms where someone's not trying to communicate a certain message messaging or something, but it's still a threat to to the platform in one way or another?
[849.12 --> 853.18]  I guess maybe spam would be spam would be an example of that.
[853.18 --> 860.26]  But I don't know if you have other examples or is it really kind of from your view, a lot of what you focus on is the communication and language piece.
[861.08 --> 862.86]  So the goal, it's not necessarily language.
[863.02 --> 866.60]  And in a second, I'll talk a lot about like contextual AI and what that means.
[866.80 --> 873.80]  But really, our goal is to enable users to be safe online, to have a safe experience.
[873.80 --> 874.82]  Right. I'm a mom.
[874.88 --> 875.60]  I have three kids.
[875.78 --> 880.88]  I started working in ActiveFence and I said, oh, gosh, my daughter is not getting a cell phone until she's 35.
[881.02 --> 881.82]  Like, forget about it.
[881.82 --> 882.04]  Right.
[882.04 --> 883.76]  Because you're suddenly exposed to all this.
[883.82 --> 888.28]  And then you say, but, you know, that's why what we do is so important because that's our whole that's a whole goal.
[888.34 --> 889.42]  It's not only about language.
[889.42 --> 891.08]  And that's just one form of communication.
[891.44 --> 892.76]  There's lots of things out there.
[893.50 --> 896.06]  And like we're a bunch of concerned parents.
[896.06 --> 897.74]  Like, let's really make this a safe.
[897.80 --> 901.20]  Like the fact that Chris is still sort of in this sheltered bubble is amazing.
[901.20 --> 902.90]  Like I want everyone to be in this sheltered bubble.
[902.90 --> 903.20]  Right.
[903.84 --> 905.82]  And so that's that's kind of the idea.
[906.24 --> 907.90]  I think I just need to correct it.
[907.96 --> 908.38]  It depends.
[908.38 --> 910.54]  There's some bubbles I'm sheltered from, I think.
[910.54 --> 912.18]  And there's some I probably am not.
[912.54 --> 912.86]  Probably.
[913.32 --> 913.96]  So, yeah.
[914.04 --> 914.36]  Yeah.
[914.36 --> 917.58]  Like when you were talking about the hate speech, the specific numbers that meant stuff.
[917.62 --> 918.70]  I was like, I didn't know that.
[918.78 --> 920.10]  So I didn't mean to cut in.
[920.26 --> 921.56]  But why would you?
[922.04 --> 922.34]  Yeah.
[922.34 --> 923.34]  Yeah.
[925.48 --> 928.32]  So I mean, so language is only one part of it.
[928.32 --> 930.96]  And I think one thing that we really get into is context.
[931.24 --> 933.42]  And so let me take you on a journey through context.
[933.42 --> 936.14]  And we'll end up at means, which to me is like crazy.
[936.14 --> 936.84]  Sounds great.
[937.34 --> 940.46]  So we were talking about like the language context.
[940.46 --> 940.70]  Right.
[940.74 --> 943.30]  And so how keywords and engrams, they just don't cut it.
[943.32 --> 943.44]  Right.
[943.44 --> 945.48]  You need like language models.
[945.48 --> 949.78]  So, you know, transformers and so forth to really get an understanding of what is being said
[949.78 --> 951.32]  and the context in which it's being said.
[951.68 --> 955.28]  And so those are the kinds of models that we end up training and that we have data for.
[955.50 --> 960.02]  We have, like I said, we have like our subject matter experts and policy experts that are
[960.02 --> 963.88]  able to sort of ensure that we're capturing things that are sort of on the edge and border
[963.88 --> 965.68]  because that's where things get interesting.
[965.90 --> 966.04]  Right.
[966.08 --> 967.38]  And that's that's where I want to be able.
[967.74 --> 973.04]  That's how I'm able to get the difference between, you know, I'm proud of being a whatever
[973.04 --> 978.28]  because I'm like reclaiming that word versus, you know, you are a you're not allowed here.
[978.76 --> 983.30]  And even within the hate speech of language, there's, you know, insulting hate speech,
[983.38 --> 987.86]  not insulting hate speech, you know, like, hey, wasn't that a great KKK rally yesterday?
[987.86 --> 990.58]  I really like your proud boys tattoo.
[990.88 --> 991.12]  Right.
[991.82 --> 993.16]  It's hard to catch those things.
[993.68 --> 995.12]  That's a surreal statement right there.
[995.18 --> 995.76]  That example.
[995.92 --> 996.12]  I just.
[996.42 --> 998.00]  That's never been said on your podcast, right?
[998.32 --> 1000.70]  No, it's never been said.
[1000.70 --> 1004.84]  Just like you said that I was like, I was like, wow, I'm I'm not talking to the people
[1004.84 --> 1005.94]  that are saying things like that.
[1006.00 --> 1008.04]  So anyway, sorry, go ahead.
[1008.10 --> 1011.30]  I just it's it's novel to me to hear some of this perspective.
[1011.88 --> 1017.56]  But then we can sort of go to the level of, OK, so let's say I we're now in the image space.
[1017.56 --> 1017.76]  Right.
[1017.78 --> 1023.04]  And so one thing that we're able to do and again, because we have this like deep subject matter
[1023.04 --> 1025.92]  expertise is we're able to search for logos.
[1025.92 --> 1026.32]  Right.
[1026.40 --> 1032.06]  So logos of terror, you know, like like rare terror groups, you know, small that are hard
[1032.06 --> 1032.46]  to find.
[1032.52 --> 1034.42]  So we know this space.
[1034.48 --> 1037.88]  And so we're able to go out and find, you know, do logo detection, find those particular
[1037.88 --> 1039.54]  logos, identify things.
[1040.02 --> 1041.02]  And then you say, OK, great.
[1041.12 --> 1043.78]  So here's the video found the ISIS logo.
[1043.92 --> 1044.20]  Great.
[1044.48 --> 1045.12]  Check terror.
[1045.72 --> 1046.76]  And they say, well, wait a minute.
[1046.86 --> 1048.60]  But there's also the CNN logo here.
[1048.60 --> 1052.86]  So suddenly, even though it's a snippet from ISIS, it's, you know, the context in which
[1052.86 --> 1056.08]  it's used is not doesn't make it violative.
[1056.18 --> 1057.26]  It's suddenly it's interesting.
[1057.28 --> 1057.72]  It's important.
[1057.82 --> 1058.28]  It's historical.
[1058.36 --> 1058.74]  It's whatever.
[1059.16 --> 1061.54]  You can see the same things with like videos of Nazis marching.
[1061.54 --> 1061.78]  Right.
[1061.78 --> 1064.44]  Like sometimes that's glorified and sometimes that's just like historical.
[1064.70 --> 1065.70]  You know, it is what it is.
[1066.06 --> 1067.40]  So that's another level of context.
[1067.40 --> 1071.76]  We have to sort of look at the context of the, you know, one signal out of the image
[1071.76 --> 1074.04]  isn't enough or out of the video.
[1074.50 --> 1077.24]  Another thing that we like looking at that, you know, it's important to look at is that you
[1077.24 --> 1080.32]  can look at the context in which the image is being used.
[1080.32 --> 1080.48]  Right.
[1080.50 --> 1081.24]  What is the title?
[1081.30 --> 1082.06]  What is the description?
[1082.20 --> 1082.94]  What are the comments?
[1083.28 --> 1088.70]  We have an example that I like using where you see sort of non-violative text.
[1088.76 --> 1089.82]  You know, I love him.
[1090.16 --> 1090.30]  Right.
[1090.34 --> 1091.06]  And you're like, oh, that's fine.
[1091.10 --> 1091.38]  Who cares?
[1091.76 --> 1094.76]  And then when you zoom out, you see, it's like, I love him with a picture of Osama bin
[1094.76 --> 1095.00]  Laden.
[1095.00 --> 1097.42]  And suddenly that's suddenly more interesting.
[1097.60 --> 1097.74]  Right.
[1097.94 --> 1099.94]  Suddenly it becomes violative.
[1100.02 --> 1102.14]  So you can't just take any one piece in isolation.
[1102.14 --> 1108.52]  Or there's an example of like some chef that's like, it's hard to do this on a podcast, but
[1108.52 --> 1112.84]  like showing knives and he's like demonstrating these knives and showing these knives and his
[1112.84 --> 1114.78]  hands are all cut up because he uses knives.
[1115.10 --> 1119.34]  And if you do just object detection, it screams at you like weapon, weapon, weapon.
[1119.34 --> 1121.40]  Like, oh gosh, this is like this terrible video.
[1121.92 --> 1125.36]  And then you analyze, you know, the title and description and the comments and the channel
[1125.36 --> 1126.32]  and everything along with it.
[1126.32 --> 1129.84]  And you're like, no, you know, he's teaching about knives.
[1129.94 --> 1132.36]  It's a chef video, like not really not interesting.
[1133.06 --> 1137.54]  And so looking at things, you know, just as keywords in a sentence aren't enough, also
[1137.54 --> 1143.16]  just, you know, looking at an image by itself isn't going to tell you whether or not something
[1143.16 --> 1143.76]  is problematic.
[1144.46 --> 1148.54]  And so that's sort of this like idea of contextual AI that we're really, that we think about
[1148.54 --> 1151.20]  a lot is like, what is the context in which something is used?
[1151.52 --> 1153.20]  And context can mean lots of things.
[1153.22 --> 1155.88]  It can also mean the policy, right?
[1155.88 --> 1158.08]  So different platforms have different policies.
[1158.74 --> 1163.86]  Some platforms will say baby's first bath is like child abuse.
[1163.96 --> 1166.02]  Like you cannot have it, you know, child nudity.
[1166.20 --> 1168.08]  And others will say not a big deal.
[1168.30 --> 1171.02]  So that's like another level of context that our models need to deal with.
[1171.02 --> 1192.10]  I mean, just knowing about where NLP models or other models fail, like this area of like
[1192.10 --> 1195.00]  sarcasm and humor is so difficult.
[1195.00 --> 1202.44]  And there's like this further distinction that you're drawing out, which is, well, there's
[1202.44 --> 1205.76]  some memes that are jokes and sarcasm, right?
[1206.02 --> 1211.48]  There's some memes that are jokes and sarcasm, like to the point of being very, very harmful.
[1211.48 --> 1219.74]  And also that's kind of tied into the context of where they're, you know, where they're put or
[1219.74 --> 1224.38]  the timing of when they're put somewhere or something like that.
[1224.38 --> 1233.86]  So I'm wondering if you could kind of break down, like as you're stepping into addressing some of
[1233.86 --> 1239.30]  this, you already mentioned like frequently you're updating like new features, like there's new
[1239.30 --> 1242.34]  behaviors that you're seeing that didn't exist before.
[1242.56 --> 1249.18]  So like, let's say that ActiveFence like starts to understand that there's some type of new
[1249.18 --> 1252.32]  behavior that's harmful or something like that.
[1252.32 --> 1258.46]  What is your process and how do you think about going from like knowing this is happening to
[1258.46 --> 1264.00]  detecting that this is happening and in a repeatable sort of way?
[1264.54 --> 1270.18]  So there's sort of a couple of different ways that we're basically staying up to date.
[1270.28 --> 1275.30]  So the first is really, really close contact with subject matter experts that are out there
[1275.30 --> 1282.80]  gathering information, intelligence, researching, collecting data, building like keyword databases,
[1283.36 --> 1289.04]  looking for particular, you know, bad actors that frequently post things sort of they're
[1289.04 --> 1290.12]  really there.
[1290.80 --> 1294.34]  And so we're frequently talking to them and understanding like, what was it that made this
[1294.34 --> 1298.58]  violent of what, you know, or they'll send us a report and be like, hey, this is a new
[1298.58 --> 1301.08]  hate group or, hey, this is a new meme.
[1301.08 --> 1302.74]  And so that's, that's one thing.
[1303.12 --> 1306.76]  The other thing is that even within our models, we're constantly getting feedback.
[1306.76 --> 1312.36]  We have something that we call the database of evil, which is like a great life.
[1312.82 --> 1314.68]  I mean, might as well call it what it is.
[1314.80 --> 1315.14]  Right.
[1315.72 --> 1322.12]  That has to be the best name I've ever heard, you know, for it's the database of evil.
[1322.82 --> 1325.66]  And it's true to its name.
[1326.18 --> 1327.00]  I believe it.
[1327.00 --> 1327.40]  Yeah.
[1328.12 --> 1330.28]  And so we keep that updated, right?
[1330.36 --> 1334.72]  So we have data that's coming in, we score it, you know, we give it a risk score, which
[1334.72 --> 1337.80]  is essentially like the probability that it's violative for some violation.
[1338.38 --> 1343.80]  And then we have trained analysts that review it, review the score and sort of can say, yes,
[1343.84 --> 1344.12]  no, no.
[1344.34 --> 1348.30]  Anything that's verified as being violative, it goes into the database of evil.
[1348.78 --> 1354.88]  The database of evil is sort of used for a few things, one of which is new content that
[1354.88 --> 1356.74]  comes in, we can say like, well, have we seen this before?
[1356.82 --> 1357.54]  Do we know it?
[1357.88 --> 1358.00]  Right.
[1358.06 --> 1362.06]  Things that we've seen a lot, they're more like, you know, versus things that are brand
[1362.06 --> 1362.28]  new.
[1362.66 --> 1366.80]  And it's also used because as we take this feedback, we're constantly, like I said, we're
[1366.80 --> 1367.56]  retraining, right?
[1367.58 --> 1368.40]  We're learning.
[1368.60 --> 1372.20]  And that's like, those are the small adjustments that we can make to our models.
[1372.66 --> 1377.66]  And so it's this idea of like constantly getting feedback, both just, you know, from researchers
[1377.66 --> 1382.04]  that go out and find things from the data that's coming in is being scored.
[1382.18 --> 1384.92]  And then, you know, we're sort of retraining on top of that.
[1385.38 --> 1387.76]  And then, of course, we have our database of evil.
[1389.32 --> 1391.02]  So let me ask a question.
[1391.30 --> 1396.78]  Obviously, as you pointed out, your database of evil has some, has a lot of really explicitly
[1396.78 --> 1397.86]  evil stuff.
[1398.08 --> 1404.52]  But I'm also imagining that there are gray areas that like, you kind of mentioned the
[1404.52 --> 1406.76]  the baby's first bath kind of thing.
[1407.00 --> 1412.56]  And, you know, that would depend kind of on audience on whether that was if a family member
[1412.56 --> 1414.92]  showed me, well, we have a new baby in our family.
[1415.00 --> 1416.06]  My niece has a new baby.
[1416.34 --> 1420.76]  And if she showed me a photo of the new baby having his first bath, that would not be offensive
[1420.76 --> 1421.14]  to me.
[1421.36 --> 1425.90]  But there are contexts where posting it online, it could become offensive and such.
[1425.90 --> 1433.70]  So with these types of gray areas, and the fact that you can have one set of content that
[1433.70 --> 1438.68]  has a bunch of different, I don't know what you would go, you know, acceptable rankings,
[1438.84 --> 1442.70]  if you will, you know, depending on who is viewing it and what the context and all that.
[1443.06 --> 1446.84]  How do you approach making sense of all the gray area?
[1447.02 --> 1452.08]  Like, you know, when you're, when there is everything from perfectly fine to absolutely
[1452.08 --> 1454.66]  not fine, and it's all valid for the same thing.
[1454.66 --> 1455.26]  Right.
[1455.70 --> 1457.72]  That's a really pertinent question.
[1457.86 --> 1459.64]  And it's something that we're dealing with a lot.
[1460.28 --> 1465.16]  Part of it is sort of, and we haven't, I don't think that we've completely cracked it.
[1465.50 --> 1471.62]  But one thing that we do do is that we can also have database of evil, where evil is relative
[1471.62 --> 1473.84]  for the client, right?
[1473.92 --> 1478.80]  And so, which also leads to sort of, you know, this idea of customized models per client based
[1478.80 --> 1484.58]  on the feedback that is coming from them, where basically you can say, okay, so when
[1484.58 --> 1487.84]  we have this now, right, we have two clients, one is baby's first bath is violative, and
[1487.84 --> 1488.40]  one it isn't.
[1488.48 --> 1493.04]  And so we are already are juggling this with different levels of like, of, you know, of
[1493.04 --> 1497.10]  human intervention to get it to sort of really set to perform, because that's what's training
[1497.10 --> 1498.44]  it to get it to that point.
[1498.44 --> 1503.76]  And there's even other examples where, you know, if we take it, you know, baby's first
[1503.76 --> 1507.72]  bath and things like that, people are like, you know, oh, but it's so clear what, you know,
[1507.80 --> 1509.18]  child abuse and pedophilia are.
[1509.34 --> 1510.78]  And clearly it's not.
[1511.08 --> 1515.16]  And even things like asking someone, are your parents home?
[1515.44 --> 1520.54]  So if it's a conversation between two children on a chat room, that's totally fine.
[1520.54 --> 1525.36]  But it can take a much darker turn when you suddenly see that it's, you know, a user that
[1525.36 --> 1530.90]  is also in, you know, adult chat rooms, or it's being posted, like, you know, at around
[1530.90 --> 1534.86]  8.30, 9.10 p.m. when kids are supposed to be starting to go to bed or to be in bed.
[1535.06 --> 1536.34]  I don't know, my kids are going to bed early.
[1536.84 --> 1538.88]  And so, you know, and so you can start.
[1539.00 --> 1541.94]  So even then, like, you can say, well, I have language understanding.
[1542.36 --> 1544.44]  And, you know, this is a kid's chat room.
[1544.70 --> 1549.32]  But suddenly there's like all these other levels that you need to take into account to understand
[1549.32 --> 1551.32]  if a phrase really is just nothing.
[1551.94 --> 1555.36]  Just as kind of setting some, I am living what you just described.
[1555.58 --> 1559.68]  I've grown kids, but I also have a daughter who is just getting to the point where we're
[1559.68 --> 1562.00]  letting her get online and do some of the stuff.
[1562.08 --> 1564.94]  And some of it's in supposedly safe environments.
[1565.30 --> 1571.92]  But then as the nosy dad who's just worrying about keeping his child safe, there are all
[1571.92 --> 1573.52]  sorts of gray areas and stuff.
[1573.52 --> 1575.24]  So it's fast.
[1575.64 --> 1579.12]  And there are also some moments where I'm having a lot of trouble telling.
[1579.32 --> 1584.30]  Whether it is a safe context or not, it's not very clear.
[1584.90 --> 1590.66]  And so I can imagine that that is extremely challenging, you know, to solve as a technical
[1590.66 --> 1595.50]  problem that can be, you know, recreated across a lot of different audiences.
[1595.78 --> 1595.96]  Totally.
[1596.18 --> 1602.28]  And I think that there's always going to be to some, like, at least when we're like training
[1602.28 --> 1602.84]  or whatever, right?
[1602.84 --> 1604.56]  There's always, there has to be a human in the loop.
[1604.56 --> 1606.14]  And for these gray areas.
[1606.68 --> 1610.36]  So we do as much as we can with technology and we bring it there.
[1610.40 --> 1614.36]  But even if as a parent, you're looking at it and you're saying, you know, I don't know.
[1614.82 --> 1617.72]  And so sometimes we can leverage things that you don't have access to, right?
[1617.72 --> 1622.12]  Like we can look at the history of the user or the other chat rooms or other things that
[1622.12 --> 1625.68]  are going on in the space or how this, you know, who has been in this chat room before.
[1625.68 --> 1630.72]  But, you know, sometimes it comes down to you just don't know.
[1631.40 --> 1637.20]  So I have a lot of, Chris always knows I like to ask a lot of practical questions before
[1637.20 --> 1642.18]  I get to those in terms of like some of the things you're doing and how you're doing them.
[1642.44 --> 1649.92]  I am wondering for a company that's using some of ActiveFence's technology, what does that
[1649.92 --> 1650.88]  connection look like?
[1650.88 --> 1656.32]  Like one of the examples I'm thinking in my mind is I'm working on a website for some
[1656.32 --> 1663.54]  of our partners where people can contribute like and list cards for tools that they're
[1663.54 --> 1665.26]  working on, like software tools.
[1665.86 --> 1670.82]  And, you know, technically, like they could submit anything in that description of that
[1670.82 --> 1671.80]  tool, you know.
[1672.14 --> 1677.88]  Now, I think like we have hopefully vetted people that will be submitting content and actually
[1677.88 --> 1679.28]  not everyone has accounts.
[1679.28 --> 1680.94]  And so it's fairly restricted.
[1681.30 --> 1686.80]  But yeah, I'm wondering, like in that situation or a much more scaled up situation, what does
[1686.80 --> 1694.12]  it is working with the right view to be have to have like your software platform and then
[1694.12 --> 1700.36]  you send off content to some API and get a threat score or something and then you figure
[1700.36 --> 1705.14]  out what to do with that threat score in terms of how does this actually practically work
[1705.14 --> 1708.70]  out for a company in terms of because I imagine it's complicated.
[1708.92 --> 1711.42]  Every company has like their different platform.
[1711.42 --> 1711.90]  Right.
[1712.22 --> 1717.84]  And also like, oh, you know, the the format of a Facebook message, you know, going to
[1717.84 --> 1723.78]  a webhook is going to be different than like a blog post being posted to a content management
[1723.78 --> 1724.24]  platform.
[1724.24 --> 1729.42]  So in terms of like data moving around, how does that that work out practically?
[1729.42 --> 1734.90]  Yeah, so there's I think there's kind of two parts to maybe more parts, but two main parts
[1734.90 --> 1735.42]  to the question.
[1735.58 --> 1739.36]  The first is like, how would you as a user interact with us?
[1739.52 --> 1744.68]  And so we have a UI, a platform where you can really, you know, see the content that's
[1744.68 --> 1745.30]  coming in.
[1745.66 --> 1750.58]  You can define sort of codeless workflows where if, you know, something is above a certain
[1750.58 --> 1753.76]  risk score threshold, then, you know, it's automatically filtered out.
[1753.92 --> 1757.38]  If it's below a particular risk score threshold, then you don't even look at it.
[1757.38 --> 1759.98]  And then like, what is your threshold for for human moderation?
[1760.14 --> 1764.86]  That sort of gets between that sort of gets around this sort of like precision recall
[1764.86 --> 1768.02]  conundrum where you're like, well, I set a threshold and I always have to choose, you
[1768.02 --> 1768.96]  know, what am I maximizing?
[1769.00 --> 1773.46]  You can say, well, let's set one threshold where you're maximizing your precision and,
[1773.72 --> 1775.96]  you know, another one where you're comfortable with recall.
[1775.96 --> 1779.54]  And then you look in this sort of band and then you can use that to moderate.
[1779.70 --> 1785.46]  We also have an API you can send, you know, you can do like synchronous calls for
[1785.46 --> 1785.96]  for text.
[1786.22 --> 1787.84]  So like near real time, really, really fast.
[1788.12 --> 1791.56]  So for chat, if you want to try, you know, pre-published and so forth.
[1791.68 --> 1797.76]  And we also have async for text and for images, for video sort of, and, you know, more like
[1797.76 --> 1799.02]  where you can send the full context, right?
[1799.02 --> 1803.00]  So you can send your content and you have your, like the body of the media and the title
[1803.00 --> 1804.06]  and description, whatever you have.
[1804.42 --> 1806.10]  That's for the first part of your question.
[1806.66 --> 1812.48]  And for the second part, I think it's, is maybe like a little bit more interesting kind
[1812.48 --> 1816.12]  of because everyone, you know, you can build an API, whatever, but what we've spent a lot
[1816.12 --> 1820.08]  of time in it and time on is both like optimizing our API.
[1820.22 --> 1823.68]  So making sure that it's, you know, very robust and responsive and so forth.
[1823.68 --> 1825.76]  And then also modeling our data.
[1825.76 --> 1832.38]  And so we have a very rich understanding of the world of platforms of like how we can model
[1832.38 --> 1837.44]  the world of online media or online platforms or user-generated content, pick your favorite
[1837.44 --> 1837.72]  term.
[1837.72 --> 1842.62]  We model it, we have like a very robust and flexible schema where we're able to sort of
[1842.62 --> 1847.44]  model like a user and it's related to post and like the posts that they put and how many
[1847.44 --> 1848.24]  likes they have.
[1848.38 --> 1851.64]  And, you know, it's not always relevant and you don't always need to use it all, but we
[1851.64 --> 1855.00]  have the sort of, you know, we have users and we have, we have contents and we have collections
[1855.00 --> 1856.46]  and each of those are modeled a bit differently.
[1856.98 --> 1861.52]  And so once the data comes in and we ingest the data and it's modeled like this, then we can
[1861.52 --> 1864.12]  go ahead and take it apart and score the different parts of it.
[1864.12 --> 1869.16]  And then through our API, which is able to handle like really high throughput and fast
[1869.16 --> 1872.02]  SLA basically start giving you responses.
[1872.02 --> 1874.66]  And we've done a lot of work on our backend optimizing.
[1874.96 --> 1880.32]  And so we're batching models on GPUs and doing all sorts of, you know, picking the, you know,
[1880.34 --> 1884.46]  we have all kinds of like code that we've run that basically optimizes like what machine
[1884.46 --> 1887.92]  type you want to run and basically to make sure that everything is like runs as smoothly
[1887.92 --> 1891.06]  and as robustly and reliably as possible to get those responses out.
[1891.06 --> 1895.46]  And also we'll be used to Mira riches by defining it as well.
[1895.48 --> 1897.56]  So I'm going toкивase Roman is a mental greenhouse.
[1898.10 --> 1899.78]  To get rid of my body, maybe 15 seconds, and then you go ahead and leave.
[1899.98 --> 1900.62]  So let's begin.
[1900.62 --> 1902.32]  Here we're the two Sveriges and the这么子 protection's club.
[1903.16 --> 1904.16]  You can find yourself in a expamily production field.
[1904.16 --> 1905.26]  And in case we play their own work.
[1905.26 --> 1907.40]  So long as time didn't we go ahead and不知道 as being done in the compost.
[1907.66 --> 1908.94]  Let's look at this room.
[1909.02 --> 1910.06]  Assemblymember Puerto Rico�� podéis.
[1910.06 --> 1912.98] ええ then nous four little thing that together is our core filled.
[1912.98 --> 1915.16]  And each of these two great 하lections for us is what Wonderland is unit.
[1915.16 --> 1916.76]  We always do not have any opportunity to help us.
[1916.76 --> 1919.26]  We make it a lot worse.
[1919.26 --> 1920.92]  Let's look at this window in the 70s.
[1921.06 --> 1935.50]  So, Matar, one of my questions is just in the back of my mind is like, just the practicalities
[1935.50 --> 1940.72]  of running the type of platform that you're building and the service that you're running.
[1940.72 --> 1951.74]  I could imagine, oh, I have this model that is able, like model one is able to detect this
[1951.74 --> 1958.20]  harmful type of meme and model two is able to detect this harmful type of video.
[1958.42 --> 1965.26]  And then all of a sudden you're proliferating hundreds and thousands of models for little
[1965.26 --> 1968.58]  pieces of what you're trying to detect.
[1968.58 --> 1974.28]  And then another sort of scenario is like, oh, I'm going to like try to standardize everything
[1974.28 --> 1980.98]  into more generalized models that, you know, handle multiple modes of data or like try to
[1980.98 --> 1982.86]  synthesize things together.
[1983.12 --> 1989.34]  How just practically as like a development and research team, have you started thinking
[1989.34 --> 1995.46]  about like, when is this something maybe we want to combine together in maybe a larger
[1995.46 --> 2002.72]  model that's trying to, you know, address like multi-task sort of thing or multiple types
[2002.72 --> 2003.22]  of data?
[2003.82 --> 2008.70]  And then the other side of that is like, maybe sometimes it is useful to just like spin up
[2008.70 --> 2013.08]  hundreds of small models and, you know, ensemble them together in some way.
[2013.52 --> 2014.34]  Any thoughts on that?
[2014.76 --> 2014.94]  Yeah.
[2015.10 --> 2017.36]  So, we actually do do that.
[2017.68 --> 2021.04]  Sometimes we have models that are like just really lean and we serve them as is.
[2021.04 --> 2027.34]  And that's sort of for, like I said, for our like near real time responses for when we
[2027.34 --> 2028.12]  do contextual stuff.
[2028.18 --> 2031.94]  So, like I said, we really need to extract information as many different ways as we can.
[2032.08 --> 2036.54]  So, we're looking for logos and we're listening, you know, we're listening to the audio and,
[2036.54 --> 2042.70]  you know, looking for known phrases and keywords and language understanding and what have you.
[2043.18 --> 2046.80]  And all these like smaller models, then we do combine into ensembles.
[2046.80 --> 2053.40]  We have a feature store that we can basically, you know, take from, combine, train the relevant
[2053.40 --> 2059.54]  models and then productionize them and then add, like we call them like indicators, but,
[2059.66 --> 2064.20]  you know, essentially indicators from which then we can get features and then go to a model,
[2064.42 --> 2066.66]  which is an ensemble of these.
[2067.18 --> 2072.12]  And so, we kind of use both approaches based on like the SLA requirements, based on also
[2072.12 --> 2073.40]  the explainability that we need.
[2073.40 --> 2077.86]  We want to be able to explain why something, right?
[2077.94 --> 2083.90]  Like, you know, this particular logo was found because sometimes the moderator may not have
[2083.90 --> 2085.50]  the full knowledge that we have.
[2085.56 --> 2091.64]  And so, a big thing that we deal with is how can we take our intelligence and leverage it
[2091.64 --> 2092.62]  to the fullest extent, right?
[2092.68 --> 2096.04]  So, one way is really to put it in the models and the other way is really to educate the moderators
[2096.04 --> 2097.98]  through explainability of the models.
[2098.08 --> 2102.10]  They can really understand, you know, why things, you know, sometimes things aren't obvious.
[2102.10 --> 2102.56]  Yeah.
[2102.74 --> 2109.26]  And I guess that you started getting to my other question, which is like, how and when
[2109.26 --> 2114.78]  do you bring in the subject matter experts into the loop?
[2114.88 --> 2121.50]  Because I imagine there's like, you know, certain cases where you're highly probable that this
[2121.50 --> 2123.42]  is some type of harmful situation.
[2123.42 --> 2131.64]  And maybe given a restricted set of subject matter experts in an area, maybe they're restricted
[2131.64 --> 2135.68]  to only reviewing, you know, X amount of content per day or something.
[2135.94 --> 2141.04]  So, is that a situation that you run into where, excuse me, where you have to prioritize,
[2141.54 --> 2146.96]  you know, what you're reviewing with subject matter experts based on some predictive measure
[2146.96 --> 2152.06]  that you have and kind of do that in some sort of ranked way?
[2152.06 --> 2156.58]  Or do you handle that in some other way?
[2156.74 --> 2160.42]  Do you mean in terms of like what the analysts are reviewing for us?
[2160.50 --> 2160.84]  Yeah.
[2161.22 --> 2163.44]  For labeling and or like for reviewing the...
[2164.06 --> 2164.30]  Yeah.
[2164.30 --> 2164.60]  Right.
[2164.68 --> 2167.60]  So, I'm assuming that there's a limited number of those people.
[2167.78 --> 2169.42]  There's not infinite of those people.
[2169.54 --> 2169.64]  Right.
[2169.64 --> 2172.16]  So, there's not an infinite number of those people.
[2172.30 --> 2175.34]  And also, we want to be very aware of their well-being.
[2175.66 --> 2178.30]  We care a lot about the well-being of the people that we work with.
[2179.12 --> 2181.14]  Like Act Defense invests a lot in that.
[2181.64 --> 2185.32]  And so, specifically for these analysts, I want to make sure that I prioritize what it
[2185.32 --> 2186.50]  is that they need to review.
[2187.14 --> 2189.84]  I don't always need, you know, I don't need them to review everything.
[2189.84 --> 2190.08]  Right.
[2190.14 --> 2194.02]  I usually like what I would go for is that I want to review the gray zone.
[2194.16 --> 2194.28]  Right.
[2194.28 --> 2198.96]  So, we do, we have implemented active learning, which, you know, is basically to prioritize
[2198.96 --> 2202.02]  what it is that we want to train on.
[2202.54 --> 2205.96]  And so, that also prioritizes what it is that we want to review and to label.
[2206.36 --> 2209.12]  Because I'm always going for the gray zone.
[2209.22 --> 2209.32]  Right.
[2209.36 --> 2212.72]  Like what, like the things that we're not quite sure of, that we don't really know,
[2212.90 --> 2214.20]  that's where it goes to the expert.
[2214.34 --> 2214.42]  Right.
[2214.46 --> 2215.44]  It goes back to Chris's question.
[2215.50 --> 2215.96]  Like, how do you know?
[2216.04 --> 2218.16]  Sometimes you do know, but it's tough.
[2218.16 --> 2220.16]  And those are the things that I want to label.
[2220.50 --> 2224.42]  Because those things that are tough are what is going to feed in.
[2224.92 --> 2227.52]  And to give, like, you know, my discriminator to the, you know,
[2227.52 --> 2229.20]  the maximum power that it needs.
[2229.52 --> 2232.86]  And how much, sorry to steal all the questions, Chris.
[2232.96 --> 2235.28]  I'm just so fascinated by all this.
[2235.46 --> 2236.44]  But no worries.
[2236.90 --> 2241.18]  One thing that is always on my mind and maybe I wrestle with sometimes is
[2241.18 --> 2248.56]  how much do your sort of data science people or the people that are working sort of with
[2248.56 --> 2255.84]  the models directly, interact with the subject matter experts, and kind of share knowledge
[2255.84 --> 2257.84]  across that boundary?
[2258.14 --> 2259.08]  How do you balance that?
[2259.12 --> 2265.06]  Because that's always something I think I struggle with in projects is ultimately it would be great
[2265.06 --> 2271.28]  to kind of bring the subject matter experts in all along the way, like in every step of
[2271.28 --> 2271.84]  everything.
[2271.84 --> 2273.28]  Because you learn so much.
[2273.88 --> 2277.34]  But the fact of the matter is, like, you've got a limited number of those people.
[2277.34 --> 2280.18]  But also, you have to ship things, right?
[2280.18 --> 2287.68]  So you can't necessarily have the luxury of always having a discussion before you make a
[2287.68 --> 2288.76]  development decision.
[2289.16 --> 2293.86]  So how do you balance that, especially because this is such a complicated environment in terms
[2293.86 --> 2294.86]  of the subject matter?
[2294.86 --> 2301.36]  How have you found ways to balance that and any thoughts that you or takeaways that you
[2301.36 --> 2302.98]  have from that experience?
[2303.32 --> 2303.48]  Yeah.
[2303.64 --> 2309.84]  So one thing that we did is we actually embedded subject matter experts like researchers into
[2309.84 --> 2314.54]  our dev teams to sort of be part of the process.
[2314.98 --> 2319.10]  We also have, you know, our analysts that are labelers.
[2319.26 --> 2321.32]  They're, you know, they work really closely.
[2321.40 --> 2322.90]  They're just it's part of the same group.
[2323.02 --> 2324.08]  And so they're not out there.
[2324.08 --> 2326.30]  However, again, it's a limited number.
[2326.54 --> 2329.32]  It's, you know, there's there's and it's a limited number of violations.
[2329.50 --> 2331.94]  There's, you know, we're constantly being exposed to new stuff that we have to handle.
[2332.26 --> 2336.10]  And they're just a matter of, you know, relationship building and of doing, you know, check bases
[2336.10 --> 2337.70]  and constant feedback.
[2337.70 --> 2340.72]  So, hey, this is, you know, like they're kicking off new projects.
[2340.78 --> 2342.62]  We come, we learn, like, what are you guys doing?
[2342.64 --> 2345.02]  Because a lot of times they're learning on the fly, too, right?
[2345.06 --> 2348.00]  They have this new trend, new thing that they're learning about.
[2348.08 --> 2351.40]  And so as they're learning, we're trying to gather as much as we can from them.
[2351.40 --> 2354.94]  And then just a constant, like, feedback, like, you know, how does this look?
[2354.98 --> 2355.46]  How does this look?
[2355.50 --> 2355.88]  Is this there?
[2355.96 --> 2356.34]  Is this not?
[2356.54 --> 2358.92]  But I think, like, the key was embedding them with us.
[2359.26 --> 2365.40]  We did have situations where basically we wanted to develop models for things that we
[2365.40 --> 2367.90]  didn't want to expose our data scientists to.
[2367.90 --> 2374.24]  And that only a very, very few number of people in the company can be exposed to because of
[2374.24 --> 2376.34]  the nature of the violation.
[2377.06 --> 2381.92]  And there, that was much trickier because there, there was like complete dependence of
[2381.92 --> 2382.66]  the data scientists.
[2382.82 --> 2386.52]  Like, how do you, how do you build and train a model without looking at the data?
[2387.30 --> 2391.58]  So I'm kind of curious because it changed my, the question I was about to ask you just a
[2391.58 --> 2392.60]  little bit with what you just said.
[2392.68 --> 2394.34]  So I'm going to kind of combine two things.
[2394.34 --> 2397.98]  The sense that I got, because you keep talking about going to the gray area and stuff, is
[2397.98 --> 2405.90]  that almost the core of your research effort is to kind of replace the human intuition that's
[2405.90 --> 2412.44]  necessary, you know, early on to identify the nuance that's there with more and better
[2412.44 --> 2414.58]  models as you're moving forward into that.
[2414.78 --> 2419.52]  And so I would, almost like a bell curve of difficulty where that gray area is the hardest.
[2419.52 --> 2424.64]  But I am curious and I'm wondering if that's the case, but I'm also curious when you mention
[2424.64 --> 2430.56]  those things, like, it seems like I'm guessing that the things that you really don't want
[2430.56 --> 2433.62]  to expose someone to are almost, they're, they're not in the gray area.
[2433.72 --> 2439.68]  They're way over into the deeply evil side, you know, where it's like, you just, you're
[2439.68 --> 2442.20]  never going to forget having been exposed to that.
[2442.36 --> 2444.80]  If you are, how do those balance out?
[2444.88 --> 2448.44]  You know, you have that gray area that you're focusing on that you've mentioned several times,
[2448.44 --> 2450.64]  and then you have that, those kinds of things.
[2450.72 --> 2456.36]  Are they, when you have something that's so explicitly evil and it will imprint a human's
[2456.36 --> 2461.64]  mind in a very negative way, are those different problems that you're solving from a data, as
[2461.64 --> 2466.50]  a data scientist a little bit in that once it was the gray area, there's so much nuance
[2466.50 --> 2466.70]  there.
[2466.78 --> 2467.50]  Do you see what I'm getting at?
[2467.56 --> 2472.82]  Like, how do you balance the approach to building models to handle one thing that's really obviously
[2472.82 --> 2477.72]  bad and you just, you know, you don't want to get anyone to it versus developing intuition
[2477.72 --> 2480.54]  or an alternative to intuition in the gray area?
[2480.80 --> 2480.88]  Yeah.
[2481.00 --> 2484.94]  So I think, and let me know if this doesn't quite answer your question, but a lot of times
[2484.94 --> 2486.60]  it's, it can be the same model, right?
[2486.60 --> 2490.42]  So you have a model and it knows how to identify it because, you know, it gets the distribution
[2490.42 --> 2493.04]  of, you know, the data is distributed in some way along the space.
[2493.08 --> 2493.22]  Right.
[2493.24 --> 2497.64]  And so the things that are very obvious are going to be on like one side of the discriminator
[2497.64 --> 2498.12]  boundary, right?
[2498.12 --> 2500.60]  Like the really, like pick your favorite violation.
[2500.60 --> 2500.90]  Right.
[2500.92 --> 2504.34]  And I'll give you examples of like things that are like very, very, very clearly violative.
[2504.34 --> 2505.14]  And they're on that line.
[2505.34 --> 2508.42]  And then when you're training your model, you don't only want to give it just like the
[2508.42 --> 2509.56]  really horrible examples.
[2509.56 --> 2511.98]  And then things that are just like, you know, puppies and snowflakes, right.
[2511.98 --> 2515.96]  That are very obviously not because those are so the distribution between them.
[2515.96 --> 2518.68]  They're like, they're so far away that your discriminator is like your decision boundaries
[2518.68 --> 2520.34]  just never going to converge.
[2520.42 --> 2523.06]  It's going to, it can flip, flop back and forth and, you know, you, you'll never know.
[2523.38 --> 2527.22]  And so as we're doing it, we're also trying to find things that are like, you know, on
[2527.22 --> 2531.38]  the borderline because that's, what's going to help us really make sure that we're able
[2531.38 --> 2533.48]  to like find the good decision boundary, right.
[2533.48 --> 2536.02]  Because at the end of the day, it's really important.
[2536.14 --> 2540.46]  Like the base, like the basics is that we have to be able to catch like the ISIS and we
[2540.46 --> 2543.74]  have to be able to catch beheadings and we, you know, all these terrible, terrible things.
[2543.90 --> 2547.84]  But we also want to be able to catch things that are less obvious within that, still within
[2547.84 --> 2548.34]  that space.
[2548.58 --> 2553.00]  And so that's kind of where I'm talking about the gray area, just like, you know, for the
[2553.00 --> 2556.36]  grooming model, you can like, I don't even want to say, but you can think of phrases
[2556.36 --> 2558.96]  that are like very obviously grooming, right.
[2558.96 --> 2563.76]  Where like you're sexually harassing a minor and it's there in like plain text, right.
[2564.20 --> 2567.94]  But that same model, if you want it to be any good, it's, it's sure it's helpful that
[2567.94 --> 2571.58]  it can find the obvious stuff, but you also want to train it on things that are kind of
[2571.58 --> 2576.36]  more on the, like closer to the boundary because that's what'll, that's what'll help you in
[2576.36 --> 2576.74]  the long run.
[2577.30 --> 2581.92]  I have a quick follow-up that as you were talking, it was kind of coming into my mind.
[2582.00 --> 2583.14]  It's a very human question.
[2583.30 --> 2584.18]  I am for a moment.
[2584.18 --> 2589.08]  I want to move you out of the data science bit a little bit and just your organization
[2589.08 --> 2592.16]  is in a little bit of a, of a unique position on that.
[2592.44 --> 2596.88]  You mentioned that there are certain things you want to keep as many of your, of your folks
[2596.88 --> 2602.26]  on your team, not exposed to, but that does leave some people exposed to some pretty awful
[2602.26 --> 2602.74]  stuff.
[2602.86 --> 2608.30]  And that does impact, you know, people we, you know, we know I'm guessing that you're one
[2608.30 --> 2611.40]  of the people that has had to see some of those pretty tough things to see.
[2611.72 --> 2617.80]  How do you cope with that a little bit and keep, you seem to have, be really super grounded
[2617.80 --> 2618.92]  in that.
[2619.30 --> 2623.18]  And I know like, you know, but as part of the job, you're going to have to cope with some
[2623.18 --> 2624.18]  really tough stuff.
[2624.44 --> 2629.50]  And I know there has been things that I have seen myself online that I wish I just had not
[2629.50 --> 2629.80]  seen.
[2629.92 --> 2635.06]  I remember early on in the Al Qaeda period, some time back, and I watched something that
[2635.06 --> 2637.20]  was in the news that happened to be out there.
[2637.20 --> 2639.06]  And I was like, I wish I had never seen that.
[2639.06 --> 2640.98]  And I will never forget that as long as I live.
[2641.20 --> 2646.78]  I'm just curious in a human sense, how do you cope with terrible things and, and keep
[2646.78 --> 2651.48]  it in a healthy, you know, kind of for yourself in a healthy, healthy place, if that makes
[2651.48 --> 2651.78]  sense.
[2652.22 --> 2653.34]  Yeah, that does make sense.
[2653.46 --> 2659.50]  So I think I'm, I'm like a very, um, personally, like I'm a very like mission driven person.
[2659.50 --> 2663.94]  Like it's like, it's very clear to me why it is that we do what we do.
[2663.94 --> 2665.50]  And I really, really believe in it.
[2665.56 --> 2669.80]  Like I said, like a bunch of us are parents and, or, you know, or have nieces and nephews
[2669.80 --> 2674.56]  or whatever, or just care about kids or, you know, care about, care about communities and
[2674.56 --> 2675.12]  environments.
[2675.12 --> 2680.14]  And I just very, very deeply believe in, in what we as at Act Defense do.
[2680.38 --> 2683.52]  And you can really feel that when you're in the office and when you're working with people,
[2683.92 --> 2686.00]  everyone is very, very, is very mission driven.
[2686.22 --> 2693.88]  That being said, we also do our absolute best to support and protect everyone that works with
[2693.88 --> 2694.10]  us.
[2694.44 --> 2700.54]  So whether it's like different, you know, wellness support programs, we have a psychologist
[2700.54 --> 2706.90]  on staff who specializes in resilience and, you know, she's available to everyone and she
[2706.90 --> 2713.16]  does like group and one-on-one and really helps, you know, helps people build this sort of resilience
[2713.16 --> 2715.70]  in the face of what it is that we do.
[2715.70 --> 2721.30]  Um, and for me, what personally works for me is like just understanding why what we do
[2721.30 --> 2721.82]  is so important.
[2721.82 --> 2726.84]  And yeah, I've definitely, definitely seen things that will never leave me never.
[2727.30 --> 2732.32]  And I accept that, you know, because I'm doing my part to make everything just.
[2732.52 --> 2733.94]  You're helping the world in that way.
[2734.14 --> 2734.80]  I get that.
[2735.08 --> 2736.30]  Hopefully I try.
[2736.74 --> 2737.32]  We all try.
[2737.68 --> 2741.90]  I think even though we've talked about hard things this episode, I'm super encouraged and
[2741.90 --> 2745.44]  want to thank you and the team at ActiveFence for what you're doing.
[2745.90 --> 2746.04]  Yeah.
[2746.12 --> 2748.12]  It's something that's desperately needed.
[2748.12 --> 2753.84]  And thank you so much for digging into these problems and doing it with such technical excellence
[2753.84 --> 2754.40]  as well.
[2754.54 --> 2755.64]  And deep insight.
[2755.64 --> 2762.32]  As we close out here and we look to the future, what on the positive side sort of excites you
[2762.32 --> 2767.82]  about where this technology is headed as you look to the future?
[2767.82 --> 2768.18]  Yeah.
[2768.72 --> 2773.24]  So to me, first of all, super exciting that this is no, like I said, like we started off,
[2773.30 --> 2774.56]  it's no longer a nice to have.
[2774.98 --> 2776.28]  It's a basic expectation.
[2776.80 --> 2783.12]  So I think first of all, to me, that's really exciting because people are not taking safety
[2783.12 --> 2783.58]  for granted.
[2783.58 --> 2787.62]  Like they understand how critical it is and it's coming from the users.
[2787.62 --> 2790.50]  It's kind of, you know, it's not just sort of like, oh, well, it is what it is.
[2790.52 --> 2792.04]  Like, this is the price I pay for being online.
[2792.44 --> 2794.50]  No, that shouldn't be the price that you pay.
[2794.82 --> 2795.86]  So to me, that's exciting.
[2795.86 --> 2800.88]  And on the tech side, I think what's cool is that we're seeing a lot of open sourcing
[2800.88 --> 2808.54]  of different models, whether it's data generation or, you know, audio transcription or Z-shots
[2808.54 --> 2811.18]  or like all these things that are just, it's like a candy store, right?
[2811.20 --> 2815.50]  Like you can start thinking about all these things that are used for, you know, technology
[2815.50 --> 2817.10]  is used for completely different things.
[2817.24 --> 2822.30]  And you can say, well, like, how can I take these ideas and use them to just extract more
[2822.30 --> 2825.50]  signal and to look at these things from different angles?
[2825.86 --> 2828.04]  And, you know, it's an adversarial space.
[2828.26 --> 2830.16]  And so it keeps it interesting, at least.
[2830.62 --> 2833.52]  Well, Mattar, that it's very inspirational, the work you're doing.
[2833.72 --> 2837.98]  I know that there's, it's tough work, but thank you very much.
[2837.98 --> 2840.56]  And to your teammates for doing the kind of work that you're doing.
[2840.94 --> 2842.84]  It was great having you on the show.
[2843.20 --> 2848.52]  Looking forward to having you back sometime as you guys surge forward and have some more
[2848.52 --> 2850.62]  stuff that you want to, that you want to share with us.
[2850.68 --> 2852.42]  So thank you very much for your time today.
[2852.42 --> 2853.62]  Thank you so much for having me.
[2853.74 --> 2857.28]  Thank you for caring and for asking really, really interesting questions.
[2857.38 --> 2857.92]  I appreciate it.
[2857.92 --> 2867.50]  All right.
[2867.62 --> 2869.22]  That is our show for this week.
[2869.38 --> 2871.84]  If you dig it, don't forget to subscribe.
[2872.08 --> 2875.02]  Head to practicalai.fm for all the ways.
[2875.54 --> 2880.24]  And if Practical AI has benefited your life, pay it forward by sharing the show with a friend
[2880.24 --> 2880.92]  or a colleague.
[2881.30 --> 2884.28]  Word of mouth is the number one way people find shows like ours.
[2884.28 --> 2889.82]  Thanks again to Fastly for fronting our static assets, to Fly.io for backing our dynamic
[2889.82 --> 2893.54]  requests, to Breakmaster Cylinder for the beats, and to you for listening.
[2893.78 --> 2894.44]  We appreciate you.
[2894.70 --> 2895.64]  That's all for now.
[2895.84 --> 2897.34]  We'll talk to you again on the next one.
