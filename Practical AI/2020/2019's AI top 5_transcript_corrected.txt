[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[17.64 → 20.50] This episode is brought to you by DigitalOcean.
[20.96 → 24.88] DigitalOcean provides worry-free database hosting with their managed databases.
[25.20 → 29.32] If you need to get data in and out of Postgres, MySQL, or Regis,
[29.32 → 32.02] call on the world-class support teams at DigitalOcean
[32.02 → 35.14] and stop wasting time on setup, backup, and maintenance.
[35.60 → 37.22] Get simple, predictable pricing.
[37.62 → 38.86] Get detailed documentation.
[39.66 → 43.06] Get up and running in minutes so you can get on with your business.
[43.44 → 44.24] What are you waiting for?
[44.38 → 46.42] Head to do.co slash Changelog.
[46.60 → 49.22] Again, that's do.co slash Changelog.
[59.32 → 67.68] Welcome to Practical AI, a weekly podcast about making artificial intelligence
[67.68 → 70.40] practical, productive, and accessible to everyone.
[70.78 → 75.28] This is where conversations around AI, machine learning, and data science happen.
[75.78 → 78.30] Join the community and slack with us around various topics of the show
[78.30 → 80.04] at changelog.com slash community.
[80.36 → 81.20] Follow us on Twitter.
[81.20 → 82.80] We're at Practical AI FM.
[83.30 → 84.12] And now onto the show.
[88.50 → 93.22] Welcome to another Fully Connected episode where Daniel and I keep you fully connected
[93.22 → 95.68] with everything that's happening in the AI community.
[95.84 → 98.46] We'll take some time to discuss the latest AI news,
[98.60 → 102.46] and we'll dig into learning resources to help you level up on your machine learning game.
[103.12 → 104.30] My name is Chris Benson.
[104.30 → 107.16] I am Principal AI Strategist at Lockheed Martin.
[107.28 → 111.72] And with me, as always, is Daniel Whiten ack, who is a data scientist at SIL International.
[111.72 → 112.84] Hey, how's it going today, Daniel?
[113.30 → 114.46] It's going pretty good.
[114.64 → 115.32] It's 2020.
[115.66 → 116.36] Crazy, man.
[116.74 → 117.62] Happy New Year, man.
[117.86 → 118.10] Woo!
[119.00 → 126.92] So, we have just put to bed our first full calendar year of podcasts as we started mid-2018.
[128.12 → 135.44] I think if I do the math right, this is episode 71, unless we switch anything up.
[135.68 → 138.30] But yeah, so 70 plus.
[138.62 → 140.14] It's pretty exciting.
[140.14 → 146.78] I don't know what we'll do when we hit 100, but we'll make sure and have something exciting
[146.78 → 149.56] for listeners when we hit 100, for sure.
[149.80 → 153.54] And if any of the listeners out there have any suggestions for that, let us know.
[154.10 → 160.46] Join us in our Slack channel, where we are on all the time, every day, talking to people,
[160.70 → 163.48] or you can reach us on LinkedIn or Twitter.
[164.18 → 166.88] We are definitely out there having conversations with you guys.
[166.88 → 168.16] Yeah, definitely.
[169.10 → 175.88] And pretty soon, just as a final reminder for people, I think, I might have mentioned this
[175.88 → 182.00] on other episodes, but both of us will be at the Project Voice conference, which I think
[182.00 → 185.82] as far as when this episode airs will be the following week.
[185.94 → 188.74] So, January 13th through the 16th.
[188.74 → 190.94] So, if you're around at Project Voice, come find us.
[191.00 → 198.68] We'll be recording some episodes in the SIL International booth and as well giving a keynote
[198.68 → 200.38] together, both Chris and me.
[200.54 → 206.36] So, it'll be fun to be there and think a little bit about speech and voice and AI and what's
[206.36 → 207.60] going on in that world.
[208.02 → 208.38] Absolutely.
[208.54 → 209.98] That'll be in Chattanooga, Tennessee.
[209.98 → 216.14] I think on the week of the I think it's Monday the 13th, if I'm recalling correctly.
[216.72 → 220.54] So, you know, today we're going to do the same thing we did about this time last year
[220.54 → 221.90] as we got into 2019.
[221.90 → 228.84] We really wanted to kind of look back on a couple of notable points in the AI world in
[228.84 → 235.24] 2019, talk about kind of why we think they were notable, and also kind of assess the current
[235.24 → 239.58] state of AI where we are right now, and then look ahead to 2020.
[240.14 → 244.98] And of course, it would not be a start of your show if we didn't try to make a few predictions,
[245.28 → 247.98] each of us, on where things are going over the next year.
[248.40 → 249.58] It is practical AI.
[249.84 → 254.00] So, I feel like we have to make, predicting has to be a part of it.
[254.10 → 254.88] Of course.
[255.22 → 255.70] Absolutely.
[256.02 → 258.94] And the predictions will be likely wrong.
[258.94 → 265.86] But maybe if after we do this for like 20 years, we'll have a proper test set of predictions
[265.86 → 269.12] that we can really determine what our accuracy was.
[269.32 → 270.84] Oh, I'm not looking forward to that result.
[271.16 → 271.98] I'm not sure if that's good.
[272.26 → 276.34] And I'm not sure if we should call them predictions or inferences, considering the field that we're
[276.34 → 276.70] in here.
[276.84 → 277.96] Maybe that would be better.
[278.22 → 282.74] One of the things that we were talking about before we started recording is just kind of,
[282.86 → 284.42] it's been an amazing ride so far.
[284.42 → 288.40] And that is entirely due to our listeners and our guests.
[288.94 → 294.34] And as you pointed out, we just would not be where we're at with the show being as popular
[294.34 → 300.16] and so many people expressing how helpful it's been for them to get into this field and understand
[300.16 → 300.92] the detail.
[301.38 → 301.48] Yeah.
[301.58 → 303.60] Thank you to our listeners and our guests.
[304.16 → 309.92] I mean, the guests for sure, of course, a lot of the great content comes directly from
[309.92 → 310.16] them.
[310.16 → 315.26] Chris and I are mostly, you know, I feel like a lot of times we're just kind of facilitators
[315.26 → 318.48] and they're to listen to the great content that is there.
[318.60 → 319.60] So thank you to our guests.
[320.28 → 326.68] It has been great to get, you know, feedback on our Slack channel, talk to people on Twitter,
[327.00 → 332.30] talk to people at conferences who are aware of the podcast and are getting value out of
[332.30 → 332.46] it.
[332.84 → 334.78] And a lot of that is because we do get feedback.
[334.98 → 338.40] We hear it would be awesome if you did a show on this, or I'd love to hear about this.
[338.40 → 341.44] And we definitely try to integrate those things in.
[341.88 → 344.16] So thank you to being part of the community.
[344.44 → 348.50] I hope you feel welcome and are excited for 2020 like we are.
[349.50 → 349.54] Absolutely.
[349.90 → 355.08] I think a huge part of the show is the community aspect of it, even more so than the technical.
[355.32 → 357.12] It gives people an ability to connect.
[357.66 → 362.16] So thank you all for constantly talking to us over this past year and a half and making
[362.16 → 364.96] sure that we stay on track on how best to meet your needs.
[364.96 → 370.46] So I guess with that said, I know that on a couple of things looking back, we definitely
[370.46 → 372.82] top things of 2019.
[373.42 → 373.90] Yeah, absolutely.
[374.04 → 376.64] We definitely are in agreement on quite a few of those.
[376.86 → 379.76] You want to kind of one of those big topics is transformers.
[379.92 → 383.68] And you want to kind of jump into that and set that up.
[383.68 → 391.84] So when we were thinking about, you know, the top AI milestones or notable things of 2019,
[391.84 → 398.84] we both kind of drew up our own list of things that we were interested in or thought were notable.
[399.04 → 403.86] There was a little bit of overlap, but the big piece that was overlap was transformers.
[404.38 → 409.60] And we have an episode that talks about this in a lot more detail, specifically related to BERT.
[409.60 → 412.70] And we referenced GPT-2 a couple of times.
[412.88 → 418.98] But if you aren't aware of those episodes or haven't listened to them, 2019 has kind of
[418.98 → 423.14] been the year of the large language models, the year of the transformers.
[423.34 → 429.76] So this kind of got kicked off with BERT and GPT-2 and other models that were really large
[429.76 → 437.82] scale language models that in essence, were able to learn a lot about language in general
[437.82 → 442.22] by being trained on many, many documents.
[442.56 → 445.90] So lots of data scraped from the web or other places.
[446.68 → 453.18] And we're able to transfer to a lot of different NLP tasks.
[453.36 → 459.28] So whether that's machine translation or reading comprehension or named entity recognition,
[459.74 → 461.94] all sorts of things, text classification.
[461.94 → 471.32] These models have allowed us to sort of have a zoo of really large pre-trained models that
[471.32 → 476.60] know a lot about language and transfer those easily to these various tasks.
[476.86 → 482.36] And so we can kind of stand on the shoulders of giants in a sense of OpenAI and Google and
[482.36 → 487.88] others who have trained these large models, have a lot of data, and then allow us to kind
[487.88 → 493.90] of just level up our own NLP game by utilizing these pre-trained models.
[494.02 → 498.56] And that's been a huge boost to NLP this year in particular.
[499.36 → 503.86] I think the thing that really struck me about it is you and I actually come at this from
[503.86 → 504.58] different perspectives.
[504.82 → 506.78] You are a true NLP expert.
[507.04 → 511.60] Anyone who has listened to our episodes very much when we talk about this will know that
[511.60 → 513.58] it's what you do all the time.
[513.84 → 515.58] I observe it, but it's not my specialty.
[515.58 → 518.46] So I'm kind of coming from an outsider's perspective on that.
[518.80 → 524.72] And the thing that really struck me is these new large language models just impacted the
[524.72 → 529.86] entire world of deep learning and industry at large, whether you were neck deep
[529.86 → 533.88] in it the way you are or whether you're really kind of watching this from outside and just
[533.88 → 536.74] being a user of these externally the way I am.
[537.02 → 542.78] And so it was like the big hits just kept on coming through 2019 as we did this.
[542.78 → 550.20] I know I was absolutely, as was probably most people, blown away when OpenAI did their
[550.20 → 554.06] first blog post on GPT-2 early in the year.
[554.20 → 556.70] I think it was February, if I'm recalling correctly.
[557.12 → 563.68] And even as they introduced it, they noted a couple of things that it is, as we have specified,
[563.78 → 565.24] it's a transformer language model.
[565.24 → 571.24] And it's used as a generative model of language where you can essentially give it a sentence
[571.24 → 572.28] to start with.
[572.46 → 577.72] And it will generate a great deal of text, which in many cases is indistinguishable to
[577.72 → 581.84] the casual observer, you know, on whether it came from a computer or from a human.
[582.46 → 584.20] And it was pretty amazing when we saw that.
[584.32 → 589.08] And they did that initial release, which was a scaled down version just to let the world
[589.08 → 589.54] try it.
[589.54 → 594.76] They were kind of recognizing there could be security implications on that.
[594.98 → 597.30] They were slow to release and released in stages.
[597.90 → 603.38] But ultimately, if I'm recalling, the larger model they released later on in the year was
[603.38 → 609.38] trained on web text, which contains over 8 million documents for a total of 40 gigabytes
[609.38 → 613.24] of text, which from, you know, if that was images, it wouldn't be so much.
[613.30 → 614.56] But for text, that's enormous.
[614.56 → 621.28] And they pulled that from URLs on the internet in an unsupervised approach that was from Reddit
[621.28 → 623.80] submissions, in which case they had at least three upvotes.
[623.90 → 627.02] So they had a huge, huge corpus of text to pull from.
[627.36 → 632.80] And I just remember seeing those early examples of what was possible and thinking, okay, we're
[632.80 → 635.04] in a new place on the NLP front at this point.
[635.68 → 636.30] Yeah, definitely.
[636.70 → 642.12] I've talked to many colleagues who have expressed specifically with that blog post that you mentioned
[642.12 → 648.92] that prior to the blog post, if you were to ask them, hey, you know, what's the best that
[648.92 → 655.32] an AI model could do in generating text, regardless of architecture, kind of everything
[655.32 → 657.62] that's been done in the past, what's the best we could do?
[658.06 → 662.66] They would have guessed, you know, a much lower quality than what was published in that
[662.66 → 663.26] blog post.
[663.26 → 663.72] Yeah.
[664.10 → 666.84] And just kind of being blown away by that.
[667.04 → 671.04] And then, of course, that fuelled all sorts of things throughout the year.
[671.16 → 672.08] So I think.
[672.12 → 679.40] These years, kind of 2018, 2019, have been referred to as NLP's ImageNet moment.
[679.66 → 687.02] So if you remember further back when ImageNet came out, which was a challenge around object
[687.02 → 695.02] recognition and computer vision, there was a huge boost in computer vision and AI.
[695.60 → 700.62] And this, I think, is kind of a parallel in what's gone on.
[700.62 → 705.98] And so there's just been an explosion in all sorts of things that build on this technology.
[706.22 → 710.96] So the technology itself, you know, these large language models, again, they're not, they're
[710.96 → 712.96] kind of building blocks in a way.
[713.28 → 719.84] We talked in the blog post about BERT, about how these are structured often into sort of encoding
[719.84 → 734.40] layers and decoding layers and decoding layers and how you can utilize BERT or these other models to create this sort of word embeddings or representations of text that can be used for a variety of tasks.
[734.40 → 745.52] And so that spurred not only innovation in sort of text generation, but innovation in all sorts of NLP tasks, like I mentioned in translation and all sorts of things.
[745.52 → 755.92] And I just saw one of the big indications of this, I think, is I saw that Google search, which is arguably Google's kind of bread and butter, right?
[756.04 → 768.38] They just switched over to actually integrating BERT, which is one of these transformer models, large language models directly into Google search in production, you know, live now.
[768.38 → 775.22] So I don't think Google would be taking that risk if they weren't convinced that this was a transformative technology.
[775.42 → 776.32] So that's pretty cool.
[776.48 → 779.58] It's almost a meta issue around this.
[779.84 → 783.94] There was quite a bit of controversy in how GP2 was released.
[784.06 → 787.68] And, you know, we already talked about the stage release that they did.
[787.86 → 796.14] In that original blog post, they note under release strategy, they say, we're not releasing the data set, the training code or the GP2 model weights.
[796.14 → 806.32] And they specify that we expect that safety and security concerns will reduce our traditional publishing in the future while increasing the importance of sharing safety policy and standards research.
[806.60 → 819.34] And that was really the first time that a major AI research organization had done, you know, everybody up until that moment was just publishing as fast as they could as new stuff came out.
[819.34 → 822.88] And that was the moment where they suddenly said, we have a greater concern.
[822.88 → 828.44] And there was quite a lot of debate about, you know, whether that was the right approach or not.
[828.58 → 835.08] I know we talked about it on the show a little bit, but it was just interesting to see how that policy debate shook out over time.
[835.90 → 848.46] Yeah, I would specifically, you know, like to note and longtime listeners of the show will know that I like to mention this group quite a bit because I really think that they're a big part of what's happening.
[848.46 → 859.42] I specifically don't think that the momentum that's built up this year around Transformers would have been quite as much without Hugging Face's contribution.
[859.92 → 860.36] Absolutely.
[860.36 → 864.08] So we had Clem from Hugging Face on a while back.
[864.18 → 865.64] We'll reference that episode.
[866.08 → 872.22] That was actually before a lot of the stuff I'm about to talk about really built up.
[872.36 → 876.72] But after that episode, Hugging Face, they came out with a few things.
[876.82 → 890.12] One of those was this application called Write with Transformers, which is a really, you know, for non-technical people, you can just go to this app and choose any of these language models you want and just try to generate some text with it.
[890.12 → 894.90] And it's kind of like a Word document where you can kind of integrate these models.
[894.90 → 902.52] And I think that was just like a huge eye-opener for people because not a bunch of non-technical people could go in there and do this.
[902.60 → 907.32] It also forced Hugging Face to really deal with this.
[907.42 → 909.80] Well, how do we productionize these models?
[909.96 → 911.44] How do we integrate them practically?
[911.44 → 924.06] Which led them to release the Transformers library, which is one of the widest used NLP AI libraries, I think, that's been mentioned a lot this year at top conferences.
[924.44 → 932.84] Even all the research conferences, but industry conferences, even TensorFlow Dev Summit, even though Hugging Faces traditionally work with PyTorch, I think.
[933.24 → 935.24] So this is really transformative.
[935.72 → 939.60] I even, in my car, often I listen to NPR.
[940.00 → 940.52] I do too.
[940.52 → 944.66] I was listening to NPR and there was someone on there.
[945.06 → 946.94] I forget the exact topic.
[947.16 → 950.34] I don't remember the context, but they were talking about AI.
[950.86 → 957.84] And they were like, well, I can use an AI model to generate some new NPR show titles for this show.
[958.02 → 965.62] And they used Right with Transformers, the app from Hugging Face, to do that sort of on the show, which was pretty cool.
[965.62 → 969.34] So, you know, I'm looking over what they do.
[969.34 → 978.76] And, you know, they've done such a good job of integrating their Transformers in with the existing tooling as, you know, TensorFlow 2, you know, was out this year and PyTorch.
[978.76 → 986.84] And those two still probably, I know there'll be some people disagreeing with me, but probably the dominant two frameworks and the tight integration.
[987.18 → 992.46] They've really made NLP not only powerful, but incredibly accessible to people.
[992.46 → 998.46] In your view, I know that you follow them very closely, you know, even beyond us having them on the episode.
[998.66 → 1009.22] What do you think Hugging Face has done so well and so right to, you know, they've kind of become, to some degree, it seems that kind of the darlings of the NLP world this year.
[1009.22 → 1011.56] That's at least how that's my own feeling of it.
[1011.70 → 1012.40] Yeah, for sure.
[1012.58 → 1028.50] I mean, I think that a couple of things that maybe can be extracted from that, and we can learn for our own work is that they have focused on making things sort of giving people an immediate satisfaction with using these tools.
[1028.60 → 1034.00] So the Right with Transformers thing, you don't have to even go to GitHub or download any models or anything.
[1034.00 → 1036.22] You just go, and you try it out, right?
[1036.48 → 1048.44] And so that I think is one thing is kind of that we could extract from this is, you know, making AI consumable to all sorts of audiences is something that is incredibly valuable.
[1048.44 → 1059.98] But then also for developers, prior to the Transformers library, it was still rather difficult to integrate these large scale models into a normal workflow.
[1059.98 → 1073.34] And Transformers really gave a standardized API that people could use to pull in these models, utilize them for various tasks, or just utilize them for generating embeddings.
[1073.94 → 1079.32] And so I think that sort of standardization is something that we also saw with Spacey.
[1079.46 → 1081.92] So Spacey, which we had on the show recently.
[1082.32 → 1082.72] That's true.
[1083.10 → 1088.16] It has been, and it still is extremely popular in the space, in the NLP space.
[1088.16 → 1095.38] And I think those are also characteristics that we've seen with Spacey, where they value good design.
[1095.62 → 1098.38] They value a good user experience.
[1098.88 → 1105.24] They have a nice way to standardize the sort of workflow around NLP to these sorts of pipelines.
[1105.36 → 1108.94] So I think those are really key ideas that we could take away.
[1108.94 → 1120.46] And just to give Hugging Face kind of final congrats, they ended the year with an announcement of $15 million in funding to continue development of Transformers and what they're doing.
[1120.68 → 1124.54] So I think it's worth taking time to mention them and always happy to.
[1125.08 → 1125.52] Absolutely.
[1125.92 → 1129.08] They've had such a profound impact on the industry this year.
[1129.32 → 1131.74] It's just been very, very impressed with them.
[1132.18 → 1133.08] It was a great episode.
[1133.08 → 1136.78] So if anyone out there hasn't listened to that episode, you definitely should.
[1149.26 → 1154.88] If you like this show, I bet you'd enjoy listening to Brain Science.
[1155.36 → 1162.64] Join clinical psychologist Muriel Reese and Adam Kodiak as they explore the inner workings of the human brain to understand behaviour change.
[1162.64 → 1165.56] Habit formation, mental health, and being human.
[1165.92 → 1167.58] Here's a quick taste of what you can expect.
[1167.72 → 1170.88] It's from episode four about coping skills and strategies.
[1171.10 → 1171.62] Take a listen.
[1172.50 → 1177.28] I often use this acronym with people when they're trying to cope.
[1177.66 → 1178.42] And it's HALT.
[1178.70 → 1179.90] H-A-L-T.
[1180.04 → 1180.36] HALT.
[1181.00 → 1190.08] Because if we are hungry, angry, lonely, or tired, your coping will invariably look different.
[1190.08 → 1192.46] I don't care if you're 3, 33, 73.
[1193.18 → 1193.52] Right.
[1193.72 → 1202.94] If you are hungry or angry, angry, lonely, or tired, you just have less to be able to navigate it.
[1203.58 → 1205.88] Brain Science is a great podcast.
[1206.14 → 1208.88] Check it out at changelog.com slash brain science.
[1208.88 → 1213.98] Or just search Brain Science in Apple Podcasts, Spotify, or your favourite podcast directory.
[1214.10 → 1214.64] You'll find it.
[1214.90 → 1218.42] While you're at it, upgrade to our master feed at changelog.com slash master.
[1218.60 → 1221.08] And let your podcast app download all the shows we produce.
[1221.28 → 1224.50] Then you can pick and choose the ones you're interested in the most and skip the rest.
[1224.74 → 1225.48] What have you got to lose?
[1225.90 → 1226.22] All right.
[1226.28 → 1226.84] Back to the show.
[1226.84 → 1242.28] So there were a couple of things this past year.
[1242.46 → 1249.72] I don't know that they were the most important things necessarily, but they were certainly events that really captured my imagination.
[1249.72 → 1253.80] And we did have actually episodes on both the things I'm about to mention.
[1253.88 → 1265.98] The first one, people may recall a few months back, OpenAI did some work with robotic dexterity using a robotic hand that where the hand was trying to solve a Rubik's Cube.
[1266.16 → 1276.50] And just to specify, and we had a whole episode talking about this, it wasn't the algorithm of the Rubik's Cube that the AI portions were solving because those are known solutions out there.
[1276.56 → 1277.92] So they just implemented one of those.
[1277.92 → 1289.02] But what they were doing was using reinforcement learning to really get the dexterity and sensitivity of the robotic hand to really a whole new level that had not been doing.
[1289.14 → 1296.06] And they shared some videos out there showing the robot manipulating, the single robot hand manipulating the cube in all sorts of ways.
[1296.06 → 1308.72] And it really inspired me seeing that to see the delicateness of it, the capability of being able to do very minute turns on the cube with digits.
[1309.26 → 1310.44] And it was interesting.
[1310.68 → 1313.16] It would make you hold your breath as you watch the video.
[1313.38 → 1316.96] And at moments, the Rubik's Cube would roll right up onto the fingertips of the robot.
[1317.22 → 1319.44] And it would stop, bounce there, and then spin.
[1319.44 → 1327.96] And it just made me realize that we were at the dawn of a new age for robotics in terms of what AI could do to really supercharge where robotics are right now.
[1328.16 → 1338.74] Not only in more traditional movements and such, but also in these tiny little dexterity things with sensors that are able to capture delicate things.
[1338.74 → 1353.80] And after watching that video, you could easily think of robots, as we've talked about medicine and things, doing incredibly dynamic and precise forms of surgery on humans in that way.
[1354.08 → 1361.20] That if you had all the right sensors and everything, that you could take AI and robotics in medicine to a whole new level.
[1361.46 → 1368.38] And that really had a fairly profound, for just one story, it had a fairly profound impact on my perception of the state of the art.
[1368.38 → 1368.96] How about yourself?
[1369.64 → 1371.30] Yeah, it was interesting.
[1371.30 → 1375.44] And this is a space, you're much more familiar with this space.
[1375.54 → 1386.74] But I think the things that stood out to me with that was their focus on making the models robust against perturbations and sort of new scenarios.
[1387.30 → 1395.18] So they developed these techniques around domain randomization and increasing the randomization during training.
[1395.18 → 1402.24] Such that the hand was able to deal with all sorts of unexpected scenarios.
[1402.80 → 1403.94] And I don't know if it's accurate.
[1404.10 → 1404.96] Maybe you can tell me.
[1405.10 → 1416.38] But it seems like maybe one of the things that's held back AI and robotics a bit is this fact of generalizing to all sorts of different scenarios.
[1416.38 → 1424.54] Like if you're saying with medicine and surgery, people come in all sorts of different shapes and sizes and ages.
[1424.94 → 1432.86] And so having a hand that would perform certain procedures would need to deal with all sorts of scenarios.
[1432.86 → 1435.66] And you can't have all of those in your training set.
[1435.66 → 1443.78] So how do you make sure that your system is able to extend and generalize to different scenarios?
[1444.32 → 1448.26] I think that that focus in the project was fascinating to me.
[1448.58 → 1453.42] If that focus continues, maybe there's a way to kind of push the boundary there.
[1453.42 → 1463.90] Yeah, it's really created a revolution in robotics in terms of, you know, we've had robotics for decades, you know, deployed in various industries, particularly industrial uses.
[1463.90 → 1470.22] And for a long time, everything about, you know, for instance, an assembly line had to be very precisely measured.
[1470.42 → 1475.06] And there could not be variability, substantial variability in those workflows.
[1475.06 → 1492.88] And so we've really seen over the past two or three years at the moment culminating in this robotic dexterity demonstration that we saw is the ability to accommodate some variability and have the ability to make change based on that variability dynamically in real time.
[1492.88 → 1509.52] And so when we're looking forward, and I know we're going to talk about kind of the world ahead, you know, time ahead later on in this episode, but it really starts creating new possibilities in terms of using these in scenarios that it just wasn't practical and realistic before.
[1509.92 → 1511.28] And so it was a neat demo.
[1511.42 → 1514.46] I don't think people should get too hung up on the Rubik's Cube aspect itself.
[1514.56 → 1517.82] I just think that was a tool to show what they were getting to.
[1518.16 → 1520.32] But it was a pretty cool moment.
[1520.32 → 1527.90] The other thing that had a very profound effect on me this last year, and we had an episode on it kind of mid-year, I think it was in June, was on deepfakes.
[1528.34 → 1539.08] And more specifically, the very realistic types of deepfake videos where you're using a generative adversarial network again to generate those deepfake videos.
[1539.08 → 1547.38] And I think the thing that became obvious, not just to us in this field, but to the public at large, you know, we had congressional hearings on it,
[1547.38 → 1554.40] was the fact that you are now entering a moment with this tool, which could be used for both wonderful and nefarious purposes.
[1554.74 → 1555.70] It's not all bad.
[1555.96 → 1561.32] But you're really blurring the lines of what is real and what is not with this capability.
[1561.32 → 1563.34] And there can be fantastic, wonderful things.
[1563.50 → 1568.28] You go to an amusement park where they're able to implement deepfakes, you know, in rides.
[1568.28 → 1572.48] And it could be a lot of fun, you know, where it personalizes the ride in ways, and you could do some pretty cool stuff.
[1573.00 → 1580.64] Or obviously, you could have, you know, things as bad as national security concerns, you know, about elections, the U.S. elections in 2020,
[1580.64 → 1591.44] where we already have had the American FBI and the intelligence community warn us about that it is highly likely that we'll have adversaries and strategic competitors trying to interfere in the elections.
[1591.44 → 1601.30] And then as I've heard some other people talk about, you know, what happens right now as we look at this technology, and we have a little bit of time to assess it in some cases,
[1601.30 → 1606.62] what happens when we get to a situation where there is no time to figure out what is real and what is not.
[1606.62 → 1613.02] If you had a deepfake that showed the President of the United States describing that he had just launched nuclear weapons, you know,
[1613.08 → 1617.38] and you're somebody out there who may be the target of that, you know, and that's not a real video,
[1617.38 → 1622.36] how do you assess in a responsible, appropriate, but expeditious manner to do that?
[1622.44 → 1630.54] So we're in a world that has changed in terms of our ability to know what's real and know it in essentially real time.
[1630.84 → 1631.66] Any thoughts on that?
[1632.64 → 1635.00] Yeah, I mean, I think you're definitely right.
[1635.16 → 1642.48] And along with that, we've seen an increase, I think, in research into detecting fakes, which is encouraging.
[1642.48 → 1644.24] And I hope that continues.
[1644.24 → 1650.80] And then also, I know, in a few of the episodes after we talked about those sorts of things,
[1650.80 → 1654.54] it's come up that there definitely are good uses of this technology.
[1654.78 → 1660.32] We've talked about, you know, generating medical imagery of tumours and that sort of thing,
[1660.32 → 1664.36] which is very expensive to annotate and generate manually.
[1664.36 → 1671.42] But, you know, we can kind of simulate that data and create simulated data using these methods that can improve,
[1671.42 → 1674.60] you know, tumour detection algorithms and that sort of thing.
[1674.74 → 1681.22] So with any technology, I think there's good and bad sides that you could draw from it.
[1681.32 → 1687.06] I think this one, the deep fake things and the videos that came out emphasize the bad ones first.
[1687.06 → 1694.58] And so it'll be interesting to see as GANs are become more and more practical and integrated into different systems,
[1694.58 → 1699.46] what the positives are and how we deal with those other negatives.
[1699.90 → 1706.76] Yeah, there was one website I came across, and it used the deep fakes that were GAN powered to animate the Mona Lisa.
[1706.76 → 1714.96] So it took the, you know, what is the most famous painting in the world and the Mona Lisa was busy gesturing and talking and stuff like that.
[1715.02 → 1715.94] So it was a cute thing.
[1716.02 → 1718.40] And there's, I think we're going to see many good uses.
[1718.74 → 1723.16] Yeah, some of the uses are just kind of interesting in that sense.
[1723.22 → 1729.68] There's nothing, I don't know who uses that sort of animated Mona Lisa for any sort of practical purpose,
[1729.82 → 1732.44] but it is still fun, and it's pushing the boundaries.
[1733.08 → 1735.86] One thing, slight downer, not national security level downer,
[1735.86 → 1742.18] but I think I've heard, I've read some stuff that telecasts, you know, that you get from marketers and things like that,
[1742.46 → 1748.96] that that's supposed to be the next big wave is people scraping social media sites to get images of you and people, you know,
[1748.96 → 1751.78] and then trying to mimic voice or whatever on those.
[1751.98 → 1757.34] So beware of we go forward over the next year or two, that that kind of thing could be at a very personal level.
[1757.42 → 1759.86] It doesn't always have to be this giant end of the world scenarios.
[1760.36 → 1763.80] It can be something that is very immediate and known to you.
[1763.80 → 1764.48] For sure.
[1764.80 → 1765.26] What about you?
[1765.26 → 1768.92] What are some of the things that you noticed in 2019 that were awesome?
[1769.30 → 1774.38] I think one thing that we definitely have to note is TensorFlow 2.0.
[1774.96 → 1782.48] So I think the final official release of TensorFlow 2.0 was November 9th, if I search that right.
[1782.60 → 1783.76] I mean, I use Google search.
[1783.94 → 1787.12] So if that's the wrong date, then I guess they can blame themselves.
[1787.34 → 1789.44] I was going to say, if anyone should know the date, it should be them.
[1790.02 → 1791.68] But yeah, TensorFlow 2.0.
[1791.68 → 1800.50] So for those that aren't aware, with the release of TensorFlow 2.0, TensorFlow made quite a few significant changes,
[1800.50 → 1813.86] especially to the default API to TensorFlow, which is now Keras, and also to the way in which computations happen,
[1814.02 → 1818.28] instead of always generating this static graph that has to be executed later.
[1818.28 → 1829.58] And so I think TensorFlow 2.0 was just an amazing demonstration that the TensorFlow team, this is coming, I guess I should say, this is coming from a PyTorch guy.
[1829.58 → 1833.06] I've used PyTorch way more than I've used TensorFlow.
[1833.56 → 1838.08] And I really enjoy PyTorch and still really enjoy PyTorch and use it a lot.
[1838.42 → 1846.22] But for me, you know, I think it's a great demonstration that the TensorFlow team saw that, oh, we have this really powerful technology,
[1846.22 → 1852.98] but we've gathered feedback that we need to kind of shift some focus in some areas and make it more usable,
[1853.64 → 1856.68] make it more approachable and make it more practical.
[1856.68 → 1862.40] And so I think the sort of usability and practicality of TensorFlow 2.0 is just amazing.
[1862.58 → 1867.56] And I think that they should be given congratulations on an amazing release.
[1867.78 → 1869.38] And I can't wait to see more.
[1869.96 → 1876.14] Yeah, as someone who used both the version 1 and version 2 now, I much prefer version 2.
[1876.28 → 1881.98] And you can use it, you can use the Keras interface for the vast majority of use cases that most people are likely to see.
[1882.06 → 1883.50] Much more user-friendly.
[1883.50 → 1889.24] And it was funny, this past year, a couple of conferences, I tend to keep my skills up.
[1889.32 → 1891.10] I'll go to TensorFlow classes and stuff.
[1891.50 → 1895.72] And I remember it was several months after the TensorFlow 2.0 beta had come out.
[1895.80 → 1899.88] We weren't a final, to be full disclosure, you know, so I can understand.
[1900.04 → 1901.82] But I remember going to a class.
[1901.98 → 1903.14] It was a TensorFlow class.
[1903.14 → 1910.84] The entire class on the beginning of that first day was immensely disappointed that we weren't using the TensorFlow 2 beta in the class instead of TensorFlow 1.
[1911.20 → 1912.46] I felt sorry for the instructor.
[1912.68 → 1914.48] I'm going to keep all the identities out of it.
[1914.56 → 1917.60] But it made that big of a difference in that community.
[1917.84 → 1926.42] And so kudos to the TensorFlow team for listening to user feedback and turning out a great product that made great strides on the first one.
[1926.42 → 1930.54] Yeah, I just tried this to see how easy it was to find.
[1930.66 → 1937.82] And I just searched for TensorFlow 2.0 code lab notebooks because that's probably where I would start if I was trying to find something.
[1937.98 → 1947.22] Or you could probably also search TensorFlow 2.0 quick start because the first two results are TensorFlow 2.0 quick start for experts, TensorFlow 2.0 quick start for beginners.
[1947.22 → 1957.40] And if you go in there, it walks you through the code itself, but also they have nice code lab notebooks that you can open and try things out without even running anything locally.
[1957.68 → 1962.32] So it's super easy to get into and would recommend people to take a look.
[1962.56 → 1964.36] Probably the last thing that I want to mention.
[1964.78 → 1966.54] I mean, there was so much in 2019.
[1966.78 → 1972.82] I'm sure we're so sorry to all of you out there who are leaving out your favourite thing from 2019.
[1972.82 → 1979.32] But the other thing that I wanted to mention in 2019 is something that I detected throughout the year.
[1979.90 → 1994.60] And that was a sort of realization which hadn't been there in 2018, at least the way I felt it this year, was that training AI models is super compute intensive.
[1994.60 → 2004.58] And this year I felt a little bit of pause from the community in saying, hey, how much energy are we expending to train these AI models?
[2004.58 → 2012.20] And what can we do to make that more efficient and more responsible in terms of the environmental impact and all of that?
[2012.20 → 2025.14] So an article was released in 2019, I think, which caught a lot of people's attention that, you know, training a single AI model, one of these larger language models, for example, can admit it.
[2025.24 → 2032.44] Just training at once a single model can emit as much carbon as five cars during their whole lifetime of use.
[2032.44 → 2034.30] And which is pretty staggering.
[2034.30 → 2041.92] And I personally felt like, you know, not everybody took this seriously this year in the community necessarily.
[2041.92 → 2045.64] And it's not like training large models has stopped.
[2045.82 → 2057.66] But I do think there is beginning to be a sense that we need to really pursue technologies that make AI more efficient and responsible in that sense.
[2057.66 → 2063.14] Yeah, I remember us talking, I don't remember which episode it was, but I remember when it came out, we talked a little bit about that.
[2063.38 → 2068.24] And I know that both of us are very environmentally focused in terms of being responsible.
[2068.70 → 2072.98] And so I was very happy to see people taking it seriously as well.
[2073.06 → 2076.54] And I heard a lot of conversations through the year about the topic.
[2076.72 → 2079.96] So I think it's a problem still to be solved.
[2079.96 → 2092.72] I think, you know, when you have very large scale model training you have to do, there are currently not enough, we don't have enough solutions out there yet in terms of having the compute capability and yet still be able to be responsible.
[2092.72 → 2095.82] Because, you know, this technology is here to stay.
[2096.16 → 2097.46] We're going to be computing more and more.
[2097.64 → 2105.30] And so we need to be thinking about those responsible solutions, just as we have in other aspects of AI that have come to pass that we'll be talking about in a few minutes.
[2105.68 → 2108.12] Yeah, there are multiple facets to this.
[2108.12 → 2116.54] So, I mean, there's the side of things, which is, of course, making data centres more efficient and also running those off of sustainable energy sources.
[2116.54 → 2120.14] And I think that's been going on prior to this year.
[2120.30 → 2123.44] And there's been a good amount of effort put into that.
[2124.22 → 2135.80] But also, I think the pieces that I've seen develop this year are much more emphasis in sort of distilling and optimizing models to make them more efficient, make them run faster,
[2135.80 → 2138.98] which is partly driven by just practicality, right?
[2139.02 → 2148.04] If you're using a model in production, and it's smaller, or you're wanting to port it to a mobile device or something like that, it needs to be smaller.
[2148.04 → 2150.76] So some of those things factor in as well.
[2151.22 → 2159.04] But also, I've seen some efforts in sort of envisioning new, more efficient architectures for modelling.
[2159.04 → 2165.56] So not always relying on, let's say, the next larger transformer model.
[2165.72 → 2180.02] But are there other architectures, maybe just regular RNNs that can do this task just as well as using, or almost as well as using, you know, the full large size BERT model,
[2180.02 → 2184.46] and are much smaller and can be trained in much less time.
[2184.84 → 2188.18] So I think, yeah, we need to approach this from various angles.
[2188.18 → 2194.64] But I think it's something that people started hopefully taking seriously in 2019.
[2195.06 → 2203.52] I think we have the benefit of the fact that it doesn't require only a mindset in terms of responsibility toward the environment, but also just sheer performance.
[2203.52 → 2210.40] You know if you're able to find these other approaches that are allowing us to actually get there sooner, it's better for all concerned.
[2210.80 → 2220.22] So, you know, one of the things before we turn to what the future looks like is kind of, let's take a moment and kind of assess where we are right now.
[2220.40 → 2222.42] You know, we've just gotten to the end of 2019.
[2223.10 → 2228.74] We're at the beginning of 2020, not only the beginning of a new year, but the beginning of a whole new decade.
[2228.74 → 2232.86] And so what are your thoughts toward where we are now as we hit this point?
[2232.86 → 2233.90] Any thoughts? Daniel?
[2234.34 → 2234.92] Yeah, sure.
[2235.26 → 2248.74] I think one super positive point of where I think we are and will continue to be in 2020 is really an amazing place in terms of the practical side of AI,
[2248.98 → 2253.20] which is what we're concerned about a lot here on the Practical AI podcast.
[2253.20 → 2258.58] And I say that because you have these things like we already talked about, like transformers,
[2258.58 → 2267.08] but other libraries as well and other toolkits or just code on GitHub, whatever it is, infrastructure pieces, tooling.
[2267.08 → 2284.38] I feel like as compared to where we were at the end of 2018, there are just a lot more ways to be sort of robust and build system AI systems that have a lot of integrity in a much shorter period of time than we used to be.
[2284.38 → 2287.72] It kind of used to be very much the Wild West.
[2287.72 → 2290.34] And maybe we still are a little bit in the Wild West.
[2290.34 → 2305.02] But I think that a lot of the principles from software engineering have kind of come into the AI world, and we're a lot more focused on versioning things, tracking things, monitoring things,
[2305.02 → 2315.24] whether that be with tools like Tensor Board or other things, or it's like infrastructure pieces like Pachyderm and things like that, Below.
[2315.52 → 2321.84] We're just thinking a lot more about the AI systems that we're building rather than just AI models.
[2322.28 → 2330.00] And I think that's really encouraging, and it helps people that are actually trying to build products and be practical and integrate AI.
[2330.00 → 2335.52] I think there's so much opportunity there and there are so many choices available in that regard.
[2336.22 → 2336.52] Agreed.
[2336.82 → 2340.20] Just seeing you called out something a moment ago that really struck me.
[2340.34 → 2347.46] And that is when we talked about this a year ago now, you know, going back to that episode, so much has changed.
[2347.78 → 2354.10] You know, we used to, when we first started this podcast, we were always searching around for good tutorials and examples.
[2354.10 → 2358.62] And sometimes we would struggle a little bit to find them in just that amount of time.
[2358.62 → 2361.94] And especially in the last year, there's so much available out there.
[2362.08 → 2369.50] The open source tools have really matured, great communities, the tutorials enabling people to do that.
[2369.60 → 2375.82] And we're finally seeing some of the surrounding infrastructure and tooling improving.
[2375.98 → 2382.16] I think there's still a struggle there as people really try to productize how they get models,
[2382.24 → 2384.76] not only trained, but deployed in the rest of their environment.
[2385.00 → 2388.22] But I think that's definitely something that's working hard now.
[2388.22 → 2394.70] You know, another thing that I've really noticed, I know at my job at Lockheed Martin,
[2394.86 → 2399.60] I'm very, very involved in our own AI ethics and responsibility initiatives.
[2399.94 → 2402.20] And so I spend a lot of time focusing on that.
[2402.56 → 2407.12] And, you know, over the past year, we've seen pretty much all the major players out there,
[2407.22 → 2410.58] whether they be Google or Microsoft or many others,
[2410.98 → 2415.82] releasing ethical frameworks and their principles and such.
[2415.82 → 2418.70] And I think it's really gotten called out.
[2418.80 → 2422.36] The difference between now and last year at this time,
[2422.36 → 2425.60] where people were starting to talk about ethical AI,
[2425.80 → 2428.10] but the conversation has matured a great deal.
[2428.26 → 2433.52] And the recognition that even with some of the limitations of where we are right now
[2433.52 → 2436.16] in terms of what deep learning can accomplish,
[2436.16 → 2438.62] that the dangers of abuse are very real.
[2438.62 → 2442.12] And we're seeing lots of the significant luminaries in our field,
[2442.12 → 2447.68] kind of calling that out and expressing a need for standardization as we go forward on that.
[2447.68 → 2452.16] So that has been a fairly significant change in the last 12 months.
[2452.16 → 2456.86] I think things like, for example, China's use of facial recognition,
[2457.20 → 2458.98] which we've talked about on the show before,
[2458.98 → 2465.80] and, you know, Russia's use of behavioural modelling and that sort of thing to influence,
[2466.00 → 2469.66] for example, elections, those have hit everybody, right?
[2469.74 → 2473.26] And have been just kind of widespread
[2473.26 → 2483.78] or have been acknowledged in a sort of larger sense that AI isn't sort of something that is really cool and for sci-fi.
[2484.00 → 2487.94] But there's like real uses of it that are going on,
[2487.94 → 2492.42] but not only real uses, but potentially terrible uses as well.
[2493.02 → 2497.58] So, yeah, you know, the, and I know we've also talked about it in previous episodes,
[2497.58 → 2504.10] but, you know, as an example of something that it depends on where you are in the world and your values,
[2504.18 → 2509.02] but I know based on generalized Western values, China has their social credit system.
[2509.02 → 2513.08] And as we have been looking at that and talking about that for some time now,
[2513.22 → 2516.28] you know, they're using AI to not only survey,
[2516.28 → 2522.76] but analyze and monitor their citizens and either reward or punish them accordingly.
[2523.12 → 2527.30] And so, you know, that's such a profound effect upon that particular country
[2527.30 → 2532.14] and the society that it's given us a lot to think about in terms of what do we want.
[2532.32 → 2535.28] If you live in a democracy where you have a say-so
[2535.28 → 2539.84] and how things are implemented, and your one voice of many that can contribute to that voice,
[2540.14 → 2543.46] I certainly hope people are thinking about what is right for you
[2543.46 → 2546.24] and the community that you live in, no matter where you are.
[2546.24 → 2547.34] And where does that make sense?
[2547.44 → 2550.84] And I think so that that has become it's gone from being a fringe conversation
[2550.84 → 2553.78] to becoming a mainstream conversation in this past year, I'd say.
[2554.46 → 2555.00] Sure, sure.
[2555.00 → 2564.60] So one thing that I'll bring up in terms of where we currently are in terms of the state of AI going into 2020
[2564.60 → 2573.06] is I think that as we move forward, it's going to be more and more crucial that if we're really serious
[2573.06 → 2581.78] about using AI to tackle large-scale problems like climate change and the death of languages around the world,
[2581.78 → 2587.78] access to good health care around the world, we're going to have to better involve researchers
[2587.78 → 2590.52] and developers from all over the world.
[2590.82 → 2597.06] So we've had some really encouraging things this past year and things going into next year around that,
[2597.06 → 2603.94] like various workshops being held around the world in Southeast Asia and Africa.
[2604.66 → 2609.22] There have been conferences that have been placed in those areas.
[2609.78 → 2616.50] There's like the deep learning in Data and in Africa that's going on and offices of Google
[2616.50 → 2619.20] and others that are opening in those areas.
[2619.20 → 2622.80] But we're definitely not where we need to be.
[2622.98 → 2628.74] For example, you know, Neurons still this year, there was a huge problem with researchers from
[2628.74 → 2632.76] around the world getting to Neurons and having their visas denied.
[2633.38 → 2640.82] You know if you just look at publishing, we're still pretty driven by the US, by Europe in certain areas.
[2640.82 → 2647.20] And so if there's been one thing that's been clear to me as I've worked more with the NGO I'm a part of,
[2647.32 → 2654.12] and also other NGOs, is that if we really want to make an impact on these sorts of problems,
[2654.12 → 2658.12] we need to have representation from these local communities.
[2658.58 → 2663.62] You know, we can't just take, for example, if we want to extend translation,
[2663.84 → 2666.64] like Google Translate to all sorts of languages,
[2666.64 → 2671.90] we can't involve these communities because there's, you know,
[2671.94 → 2677.08] we can't just publish research papers that say we're studying low resource languages
[2677.08 → 2681.52] and we just under sample English as our low resource language because that leaves out so much.
[2681.66 → 2687.70] It leaves out unique scripts, problems and unique domain issues and cultural things.
[2687.84 → 2691.94] And so I think there's a lot of shifting that needs to happen in this area.
[2691.94 → 2697.12] And I certainly hope that that continues to happen as we move into 2020.
[2697.74 → 2699.98] I think that's a really great point that you make there.
[2700.56 → 2705.90] Before we move on to predictions, the last thing I wanted to mention just about state of where we are right now
[2705.90 → 2710.24] is I also think there's a consensus developing in the industry.
[2710.54 → 2713.02] We're seeing a lot of top luminaries.
[2713.34 → 2720.04] I know the VP of AI at Facebook recently said that we are very, very far from human intelligence.
[2720.04 → 2724.42] And that was in an article, I believe, that Wired had.
[2724.58 → 2729.34] And I think there was another article, ironically, that Wired had where there were some comments about the fact that
[2729.34 → 2736.96] with us hitting kind of some limitations on the types of problems that deep learning is likely to be able to solve.
[2736.96 → 2744.34] And given the fact that it is a technique that is very narrow in terms of you get highly specialized results in a narrow scope,
[2744.70 → 2753.18] that one of the things that at Neurons that was talked about was the fact that we really need to get to biological roots of natural intelligence
[2753.18 → 2757.40] to understand what our next steps are going to be in the AI space.
[2757.40 → 2763.26] So what I think is that you may end up having people trying to reassess as they enter this new year
[2763.26 → 2766.72] about where they want to focus their research on and trying to do that.
[2766.80 → 2770.32] And I guess any thoughts on that before we move into predictions?
[2770.76 → 2772.58] No, I think it's a great point.
[2772.58 → 2781.04] And I've definitely seen I think we'll put some links into the show notes about various luminaries statements on this sort of stuff.
[2781.04 → 2790.72] I've seen those as well. And I think that we can get into pattern that is kind of natural, but can be limiting in that, like, for example,
[2790.72 → 2795.44] we were all about transformer models, and we just do transformer models over and over and over.
[2795.86 → 2800.40] And it breeds this sort of like NLP is transformers.
[2800.56 → 2806.52] But actually, you know, there are a lot of things that have happened historically in AI that we could pull from.
[2806.52 → 2818.80] And there are new things that we could pull from maybe, like you say, that are rooted in other sorts of in other sorts of ideas related to biology or evolutionary algorithms or whatever it is.
[2818.80 → 2825.80] So I think we need to keep keeping our flexibility intact, I think, maybe is a good way to put it.
[2826.24 → 2835.50] I would agree. And I think the industry at large is it would agree with those sentiments based on the sentiment we saw at Neurons and that I think has been building over this past year in general.
[2835.50 → 2837.32] So let's look ahead to 2020.
[2837.68 → 2839.08] All right. Inference time.
[2839.50 → 2842.88] Inference time now. Figure out what we think what we think might happen.
[2843.14 → 2848.58] I will start us off with a couple of them and then and then turn it over to you.
[2848.68 → 2861.48] I think, you know, as we talked about kind of AI ethics and responsibilities, I think we're now at an inflection point where we've had many organizations putting out their principles on what they think should be.
[2861.48 → 2864.72] But we don't have a very good way to execute on that.
[2864.72 → 2870.34] So not everybody is going to be an ethicist, especially in the engineering field.
[2870.34 → 2888.40] And so I think that we're seeing a consensus that the next step now is to turn toward the creation of supporting tools or retrofitting existing tooling that enables non ethicists to appropriately implement the various aspects of ethical AI.
[2888.40 → 2897.40] Everything from eliminating bias from data sets to being able to think about where different types of AI should be applied to different types of solution.
[2898.18 → 2906.26] And so I think we're going to see I'm predicting that we're going to see a surge over the next year and beyond in tooling to support ethical AI.
[2906.78 → 2908.14] Any comments on that?
[2908.30 → 2908.50] I hope so.
[2908.62 → 2909.14] You hope so?
[2909.16 → 2909.30] Yeah.
[2909.38 → 2909.58] Yeah.
[2909.58 → 2911.28] I'll be looking for it.
[2911.64 → 2912.38] That sounds good.
[2912.68 → 2919.30] I think another thing that I think is that is happening already at starting to I see a lot of conversation.
[2919.30 → 2932.14] I've been a part of a lot of conversations about this is the fact that we're getting to a point where instead of being a separate, you know, neural deep learning and neural network development, being a separate little shiny object with dedicated people that only do the modelling.
[2932.14 → 2948.00] You get to the problem of how do you implement this in real life, and you can build a great model, but then people and organizations really struggle to get it deployed into production and getting a kind of DevOps and feedback loop associated with what they're doing and those activities.
[2948.00 → 2964.20] And so I think you're going to see a lot of effort into moving neural network development into existing software development lifecycle and workflows that organizations already have in place and that they'll make adjustments to those workflows to accommodate these new technologies.
[2964.20 → 2971.26] And I think that's really important for them to see a good return on investment about for their efforts in this space.
[2971.26 → 2974.28] Yeah, I'm thinking of we've talked about that a little bit.
[2974.36 → 2982.68] Maybe Joel Ruse's episode on responsible AI development practices would come into play here.
[2982.70 → 2983.84] I'll link that in the show notes.
[2984.08 → 2984.66] Sounds good.
[2984.98 → 2988.12] Another thing I'm saying, and we actually already talked a little bit about it.
[2988.16 → 2992.54] You know, I think Tester flow 2 is an example of this as we're seeing.
[2992.92 → 3000.36] I think we're going to continue to see simplification of neural network tooling and trying to make that learning curve more manageable.
[3000.36 → 3012.52] And I think you'll, you'll see different users and developers within this technology being able to buy in to tool sets that are suitable for them and their own background.
[3012.52 → 3022.18] So I think that you'll see more tooling that is specific to, you know, that may cater to certain types of data scientists versus certain types of software developers.
[3022.18 → 3032.30] And you'll be able to kind of customize that tooling to match your level of knowledge expertise and your background as well so that you can be productive quicker.
[3032.30 → 3052.84] And then I guess my final prediction is that I think that kind of given what we talked about, this acknowledgement at large, this that's developing within the deep learning field, that it's not well suited for certain problems, that it is taking a lot more data to learn than maybe a human might used to learn something.
[3052.84 → 3069.48] And it's less flexible and stuff and overly focused on a particular solution and not able to move like by way of example from one game that you might have a deep learning algorithm that has learned, be able to move to another game and be able to leverage what it learned from the first one.
[3069.48 → 3099.46] So we've seen many examples of that.
[3099.48 → 3101.88] Right now as we're at the beginning of 2020.
[3101.88 → 3107.18] But I think we also we may get to the end of this year and that may not be a true statement anymore.
[3107.18 → 3108.70] And I may have a different answer.
[3108.82 → 3110.90] So I think that is where we're going.
[3111.02 → 3111.94] What about you, Daniel?
[3112.00 → 3112.74] What are some of yours?
[3113.70 → 3116.90] Well, I decided to go the safe route.
[3116.90 → 3134.04] And I'm going to say that I'm going to my prediction is that at least one of the following three things are going to be a huge, a huge player and a huge emphasis in 2020.
[3134.04 → 3140.40] And we'll really pick up steam and maybe all of them or maybe just two of them or one of them.
[3140.40 → 3141.26] I'm not sure.
[3141.66 → 3143.74] So I'm kind of covering my bases there.
[3143.82 → 3148.76] That way, you know, my test scores are better when we look at things after time.
[3148.76 → 3161.60] But the three things that I was thinking of were first multimodal learning, then mobile AI or AI on mobile devices and then federated learning.
[3161.80 → 3170.76] So multimodal learning is where, for example, you make inferences off of multiple modalities of input data.
[3170.76 → 3176.98] Maybe you have an image and text that are input to a model and then you make some inference.
[3176.98 → 3187.98] This was, I think, already emphasized recently by our guests from Etsy in their sort of search technology where they have titles for their products and descriptions.
[3187.98 → 3193.78] But there's also more information in the uploaded pictures of the products.
[3193.90 → 3194.10] Right.
[3194.10 → 3203.54] And so you could take both of those input signals and do much more than you could with just the text or just the imagery alone.
[3203.54 → 3203.84] Right.
[3203.96 → 3217.02] And I think that this is going to be really revolutionary and pick up steam in terms of a lot of things, whether it be chatbots or recommendation like in that Etsy case or whatever it is.
[3217.02 → 3218.42] I think we're going to see a lot more of that.
[3218.42 → 3231.46] In fact, we saw that also with OpenAI's a robot hand Rubik's Cube thing where they were taking signals off of the hand itself, but also using the imagery from cameras and all of that.
[3231.86 → 3232.66] I think you're right.
[3232.74 → 3237.08] I know that at my own company, multimodal learning is a big deal.
[3237.48 → 3245.14] One kind of globally impacting use case that we're seeing it is in humanitarian assistance and disaster relief.
[3245.14 → 3254.38] And that is where you have so, you know, as you're trying to get data sets for a particular disaster scenario, maybe a wildfire.
[3254.70 → 3269.02] If you can get data from lots of different imagery, the various types of radio calls that are occurring and all that, then you can create a model that is much more robust and accurate and able to accommodate many more scenarios.
[3269.54 → 3272.26] So I totally think you're right on that on multimodal learning.
[3272.34 → 3273.80] I think that is going to be huge going forward.
[3273.80 → 3274.50] That was a good call.
[3274.76 → 3274.90] Good.
[3274.90 → 3277.76] Well, hopefully at least that one comes true.
[3278.72 → 3279.98] I have faith in you, man.
[3280.24 → 3280.86] All right, cool.
[3281.06 → 3291.00] The other ones I think are really driven out of my sense that the privacy, of course, is it has been important, but is increasingly important.
[3291.30 → 3296.88] And just the, you know, the scale of AI is extending to all parts of the globe.
[3296.88 → 3303.74] And so I think we're seeing a lot of deployments to mobile devices.
[3303.74 → 3318.98] And a lot more tooling around that, maybe along with deployment to things like browsers and that sort of thing where we're running models on user devices and fine-tuning them on user devices.
[3318.98 → 3322.62] Along with that kind of goes federated learning.
[3322.62 → 3323.62] I think, I think.
[3323.62 → 3333.92] I think we're not really centralizing data from all sorts of users and then running a centralized training and then porting the model back.
[3333.92 → 3344.06] But there is this sort of federated distributed training that's happening where a lot of the data from user devices doesn't have to leave user devices.
[3344.06 → 3351.98] And so there are advantages to that, of course, because of privacy, but also data transfer and all of that.
[3352.30 → 3361.26] I've seen this talked about over the last years, but haven't really seen it, you know, really come about in a widespread way.
[3361.88 → 3364.66] And, you know, possibly this is the year.
[3364.78 → 3365.28] I don't know.
[3366.08 → 3366.78] I think you're right.
[3366.90 → 3368.16] I think that's, I think that's a set.
[3368.18 → 3370.36] You have stuck with safe, but they're very good bets.
[3370.36 → 3373.26] But I think they're bet on all three of those, actually.
[3373.26 → 3376.14] So, yeah, I think you nailed it.
[3376.76 → 3380.70] Well, I probably then have to learn a little bit of, I don't know.
[3380.78 → 3383.06] I need to learn a little bit of mobile development or something.
[3383.38 → 3389.16] Maybe we'll have an episode where we have some learning resources on that.
[3389.66 → 3394.02] But, yeah, I've enjoyed this look back and look ahead, Chris.
[3394.02 → 3404.86] It'll be interesting to look back at this episode at the end of 2020 and see, you know, see what came true and what didn't.
[3405.22 → 3408.82] Yeah, so much has changed in the past year, as we've called out.
[3408.94 → 3411.84] And I suspect we'll have even more so this coming year.
[3411.98 → 3413.62] So it was a good conversation.
[3413.78 → 3414.78] Happy New Year again.
[3414.78 → 3423.48] And looking forward to seeing you in Chattanooga at Project Voice and doing all sorts of cool stuff in the year ahead.
[3424.00 → 3424.28] Awesome.
[3424.54 → 3425.22] Happy New Year.
[3425.22 → 3428.36] All right.
[3428.42 → 3431.02] Thank you for tuning into this episode of Practical AI.
[3431.28 → 3432.74] If you enjoyed this show, do us a favour.
[3432.86 → 3433.46] Go on iTunes.
[3433.58 → 3434.24] Give us a rating.
[3434.52 → 3436.38] Go in your podcast app and favourite it.
[3436.46 → 3439.20] If you are on Twitter or a social network, share a link with a friend.
[3439.28 → 3441.64] Whatever you got to do, share the show with a friend if you enjoyed it.
[3441.92 → 3444.60] And bandwidth for Changelog is provided by Vastly.
[3444.72 → 3446.16] Learn more at Fastly.com.
[3446.16 → 3449.56] And we catch our errors before our users do here at Changelog because of Rollbar.
[3449.76 → 3452.16] Check them out at Rollbar.com slash Changelog.
[3452.50 → 3455.00] And we're hosted on Linde Cloud Servers.
[3455.32 → 3456.94] Head to Linode.com slash Changelog.
[3457.04 → 3457.50] Check them out.
[3457.56 → 3458.40] Support this show.
[3458.80 → 3461.98] This episode is hosted by Daniel Whiten ack and Chris Benson.
[3462.44 → 3464.50] The music is by Break master Cylinder.
[3464.90 → 3468.34] And you can find more shows just like this at Changelog.com.
[3468.42 → 3470.46] When you go there, pop in your email address.
[3470.46 → 3475.78] Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox.
[3475.78 → 3476.78] Every single week.
[3477.16 → 3477.96] Thanks for tuning in.
[3478.10 → 3478.84] We'll see you next week.
