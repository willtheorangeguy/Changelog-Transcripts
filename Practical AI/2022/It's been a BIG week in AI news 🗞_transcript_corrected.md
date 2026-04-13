[0.00 → 6.96] AI-driven simulation is a huge thing, and maybe not for the reasons that everyone is most often associating.
[6.96 → 15.70] It's less about leisure and recreation and such as that, and more about having digital twins for manufacturing design and things like that,
[15.78 → 22.42] so that you're able to try and experiment on things that would otherwise be too costly in the real world.
[22.42 → 31.74] That's the context, is looking at Omni verse in the context of using GPUs so that we can try some otherwise really hard things to do.
[40.70 → 48.48] Hello friends, Jared here to tell you about Changelog++, our membership program for those of you who want to directly support our work.
[48.48 → 58.70] Your++ membership gets you closer to the metal with extended episodes, makes the ads disappear, and takes our audio to the next level with higher bitrate MP3s.
[58.92 → 62.44] You can join today at changelog.com slash plus.
[62.44 → 81.82] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive, and accessible to everyone.
[82.24 → 86.54] This is where conversations around AI, machine learning, and data science happen.
[86.54 → 92.28] Join us at practicalai.fm slash community, and follow the show on Twitter.
[92.50 → 94.64] We're at practicalai.fm.
[94.88 → 99.52] Thank you to our partners at Vastly for shipping our pods superfast all around the world.
[99.74 → 101.58] Check them out at fastly.com.
[107.78 → 112.78] Welcome to another fully connected episode of the Practical AI podcast.
[112.78 → 119.44] In these episodes, Chris and I keep you fully connected with everything that's happening in the AI community.
[119.70 → 128.40] We'll take some time to discuss the latest AI news, and we'll dig into some learning resources to help you level up your machine learning game.
[128.90 → 129.80] I'm Daniel Eisenach.
[129.88 → 138.70] I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[139.00 → 139.62] How are you doing, Chris?
[139.82 → 141.02] I'm doing great, Daniel.
[141.02 → 142.72] Just been going through the news.
[142.84 → 144.88] There's lots of interesting stuff happening right now.
[145.12 → 152.64] You know, we have to keep doing these FC fully connected episodes because there is just a lot going on.
[152.84 → 158.02] There are a few big things that we'll talk about today, but yeah, it just seems like a lot going on.
[158.42 → 160.78] Lots of cool stuff to talk about.
[161.20 → 164.28] The other big thing in my life is allergy season is here.
[164.28 → 173.64] And so I've been like in Zoom calls, like muting myself and like trying to quickly turn off my video before I sneeze, so I don't look like a fool.
[175.48 → 176.30] It's okay.
[176.38 → 177.44] It's springtime, man.
[177.80 → 182.32] All things are coming out and blooming and birthing and all sorts of stuff.
[182.32 → 186.04] Yeah, including new large language models.
[186.48 → 186.82] Indeed.
[186.82 → 195.06] So, Chris, if you go to the Hugging Face website, just go to the main Hugging Face page.
[195.80 → 199.88] And then what you'll see is a bunch of things.
[200.10 → 204.72] But up in the top right-hand corner, you'll see a little line.
[205.26 → 208.06] And it's sort of going down and to the right.
[208.06 → 214.08] And then there's a thing that says training loss and a thing that says time to completion.
[214.84 → 214.88] Okay.
[214.94 → 227.48] And this is pretty cool because this is the actual training logs of the big science large language model that they're training.
[227.48 → 235.98] The 176 billion parameter model, which the big science research workshop is training.
[235.98 → 245.28] So, I don't know if you remember, I think we talked about this a while back, but there's this group of researchers called the Big Science Workshop or Big Science Research Workshop.
[246.14 → 248.38] It's hundreds of researchers from around the world.
[248.58 → 263.20] And it's kind of the same philosophy of a, you know, like CERN in Switzerland, the big accelerator is a collaboration between a bunch of different researchers, a bunch of different institutions and countries.
[263.20 → 272.22] And the reason that happens is because it's become increasingly hard to do high energy physics research because of the size of the experiments, right?
[272.60 → 281.86] And so, big science was like, well, it's becoming increasingly hard to train these large language models or maybe what some people would call foundation models.
[281.98 → 283.18] We talked about that last time.
[283.40 → 283.70] We did.
[283.70 → 292.12] So, it's becoming increasingly hard for any single researcher or even a team of, a small team of researchers to train these large language models.
[292.42 → 298.36] You might think of things previously like GPT-3 or things like that.
[298.68 → 305.90] So, this big science workshop said, hey, let's get together this like international collaboration, very collaborative and transparent thing,
[305.90 → 312.20] and do the next training of the kind of next big multilingual language model.
[312.68 → 325.30] And so, what you're seeing on that homepage of Hugging Face, at least now in March 2022, is the actual live training of that, which is a pretty cool thing to see.
[325.30 → 326.52] It is indeed.
[326.72 → 333.42] And as we are recording here, and I'm looking at their page, they are already, what, a dozen days into the current model training?
[333.42 → 339.58] Right. But it's only getting started because they estimate time to completion for months.
[340.34 → 347.46] So, now note, if there's people interested in the specifics of this, this model is training.
[347.72 → 357.74] So, it will be training for the next four months, and it's training on 416 A100 GPUs.
[357.74 → 365.60] So, a single model training on over 400 A100 GPUs for greater than four months.
[365.72 → 368.20] That's some serious model training right there.
[368.34 → 372.96] If there was some serious model training, that is definitely it, right?
[373.24 → 376.66] So, we'll link to this in our show notes.
[376.84 → 385.68] But there is a bunch of, one of the things I really appreciate about this whole process is just the transparency and collaborative nature of this project.
[385.68 → 389.74] So, you can go and look at the notes about what the model is.
[389.82 → 393.90] It has 176 billion parameters.
[394.58 → 398.40] And then you can look at the GPT-like architecture.
[398.40 → 412.38] And then it's trained in 46 languages on 341 or 342-ish billion tokens of text.
[412.38 → 412.56] I see that.
[412.56 → 424.32] Which, for those maybe that aren't familiar with the terminology, tokens here, well, depending on how you set up the tokenization, it might be a word or a subword of text.
[424.32 → 434.24] So, there's over 340 billion of those words with a vocabulary size of 250 plus thousand.
[434.70 → 442.68] And the only thing that doesn't seem shocking on the big end of this is actually it's only one and a half terabytes of text data.
[442.96 → 443.12] Yeah.
[443.24 → 445.18] I mean, text data is small in general.
[445.32 → 445.58] Yeah, I know.
[445.64 → 447.94] That's the one advantage of working with text data.
[447.94 → 448.46] I know.
[448.52 → 454.12] I'm just saying we're so busy talking about these massive numbers that terabytes are big.
[454.30 → 459.82] But I guess, you know, it says something about the model when it makes me think of 1.5 terabytes as a small thing.
[459.82 → 460.70] Yeah, yeah.
[460.84 → 468.54] Well, I mean, yeah, if you're doing speech or images or video or even, dare say, 3D data.
[469.08 → 475.16] I don't know if you ever watched Silicon Valley, but they try to compress like a 3D video file.
[475.34 → 478.44] That's like the thing that trips up their compression algorithm.
[479.16 → 480.26] That's why I always think of that.
[480.98 → 481.30] But...
[481.30 → 482.60] A little throwback there.
[482.60 → 483.00] Yeah.
[483.58 → 490.56] Now, I mean, the other thing, like, this is incredibly impressive, just the whole process of putting the data set together.
[490.74 → 493.20] You can read more about that in the notes.
[493.96 → 501.24] But there, you know, it still only includes 46 languages of, you know, 7,000 plus spoken on Earth.
[501.42 → 504.72] So that is, I mean, a drop in the bucket as far as languages.
[504.72 → 519.18] But if you consider this sort of, like, scale that they're approaching, the size of the data and the number of languages, it's still hugely amazing progress in terms of multilingual models.
[519.18 → 531.08] Because GPT-3 or something like that, we're talking about, you know, just supporting English or other versions that might be trained in, like, a single large language like Mandarin or something like that.
[531.08 → 537.80] So 46 languages, pretty cool to see them work on a model at this scale with more languages.
[538.20 → 542.70] I have sort of an aside off the main topic, but you made me wonder.
[542.84 → 543.66] I will permit it.
[543.80 → 544.58] I appreciate that.
[544.58 → 555.88] As someone looking at that long tail of 7,000 languages, do you think that this kind of mega models that we keep looking at, that they ever will eventually include?
[556.10 → 562.54] Or do you think they'll always be outside and there'll be other models that are catching the long tail?
[562.98 → 564.46] How do you think that will be parsed?
[564.80 → 570.46] Yeah, I guess in a very unsatisfying way, it's probably like a both and.
[570.46 → 589.02] I mean, I certainly hope that, like, as data sets become more available, and we work with local language communities to have representation of their language within NLP data sets and other things, certainly that will get better in terms of what's included in this sort of multilingual model.
[589.02 → 610.68] And I guess the other thing to keep in mind is if you have kind of representation of languages across language families, which this, you know, does have definitely more representation across language families, then it's easier to sort of fine tune or adapt that sort of model to something maybe in the same language family or a related language.
[610.68 → 616.98] So it's still helpful for languages maybe that aren't even included potentially.
[617.64 → 628.44] But yeah, I think that there will also be like a continued need for language specific models or maybe language family specific models.
[628.44 → 633.44] I think that that will always, always be a need that that will be there.
[633.62 → 645.20] In fact, I just saw in my recent Twitter feed, there is a new paper at ACL this year from Graham Newbie and company.
[645.94 → 656.46] And they're talking about the title of the paper is expanding pre-trained models to thousands more languages via lexicon based adaption.
[656.46 → 677.26] So I think that the work that their lab is doing is pretty extraordinary in this field where they are doing a lot of creative things that are maybe hybridized, like they're leveraging lexicons or dictionaries to adapt models or to align sort of cross-lingual embeddings or other things like that.
[677.26 → 680.80] And this sort of creative solutions are still going to be needed.
[680.80 → 693.70] So yeah, it'll be both and there'll be big models that will include more languages and there'll be more sort of like trickery in terms of adapting those models to local language scenarios.
[693.94 → 696.94] At least that's my prediction of the future, which is sure to be wrong.
[697.36 → 702.44] So not one model to rule them all, maybe a group of models that are...
[702.44 → 704.62] Yeah, probably that's true.
[704.78 → 708.44] And it'll be a hybridized sort of world I think we'll live in.
[708.44 → 711.44] Now, I'm kind of excited, Chris, because...
[712.22 → 720.58] And I'm proud of the organization that I work for, SIL International, because they had different working groups that you could join as part of this process.
[720.58 → 729.22] And we were able to contribute some of the multilingual data that's actually in the training data set that's being trained right now.
[729.22 → 738.56] So it's just really cool to kind of come full circle where like, you know, at the time in that working group, it seems sort of just like a very...
[738.56 → 757.00] Well, it is kind of a small piece of a much larger puzzle, but all of those pieces are necessary to make this happen, including those that worked on the architecture of the model and the scaling and the compute and the data governance and, you know, data storage and all of those things.
[757.00 → 759.02] You know, there are a lot of people that made it happen.
[759.34 → 764.18] You're in danger of not just analyzing the news here, but becoming the news yourself.
[764.68 → 765.78] A little bit of it.
[766.10 → 768.22] Well, yeah, I don't know about that.
[768.32 → 771.46] Certainly, we're excited to be a part of this.
[771.60 → 776.28] And yeah, I'm just kind of feeling giddy and excited to watch it go down.
[776.62 → 785.56] You can actually, you know, if you're on a Twitter person, they have a Twitter bot where you can get updated with the progress of the training and other things.
[785.56 → 786.56] They have that set up.
[786.68 → 789.26] So, you know, follow it and see what happens.
[789.60 → 793.48] So at the end of the workday is your wife, who is a wonderful person.
[793.62 → 794.08] I agree.
[794.42 → 794.92] I know.
[795.26 → 802.06] Is she having to patiently tell you to put down your phone and stop looking at the Twitter feeds and, you know, actually have dinner with her and things?
[802.34 → 802.62] Yeah.
[802.76 → 809.88] You know, there have been a lot of fun things to be a part of recently, including this that have come across our team.
[809.88 → 813.60] And yeah, it's a fun time to be an AI person.
[813.90 → 814.08] It is.
[814.08 → 817.70] But also, you know, you still need to have dinner with your wife.
[817.86 → 818.62] You still need to.
[818.68 → 819.08] You know what?
[819.20 → 823.04] That's like, yeah, that is the comment right there of the whole show.
[823.24 → 825.46] You still need to have dinner with your wife or your husband.
[825.80 → 826.00] Yeah.
[826.20 → 831.80] Still need to maintain positive vibes like the hugging face emoji would indicate.
[831.98 → 832.24] Gotcha.
[832.24 → 833.90] Okay, Chris.
[834.06 → 842.96] Well, we just talked about this huge training that's going on over 400 A100 GPUs.
[843.08 → 845.82] You know, that's exactly what I was thinking, too, don't you?
[846.06 → 846.36] Yeah.
[846.58 → 846.84] Yeah.
[846.84 → 856.22] So the A there stands for Ampere, which is a certain generation of the NVIDIA platform of GPUs.
[856.96 → 859.84] And big news right now.
[859.84 → 863.40] I mean, we're in the midst of GTC.
[863.64 → 865.22] Wait, is that the right letters?
[865.36 → 865.42] Yeah.
[865.52 → 870.30] GTC season, which is when NVIDIA announces things.
[870.30 → 871.78] And there are some things.
[872.32 → 873.68] There are indeed some things.
[873.68 → 882.02] So they have just announced their new Hopper architecture, which is based on the H100.
[882.28 → 884.46] So we've jumped from A to H for Hopper.
[884.46 → 887.18] The H100 Tensor Core GPU.
[887.96 → 900.14] And the thing that was jumping out, you know, while you were saying that is that they're saying that, you know, for large language models, it's its 30 times faster for training than the previous architecture, the A100.
[900.14 → 902.90] So, yes, that's, you know.
[903.10 → 903.26] Yeah.
[903.42 → 906.34] The big science training just started a little too soon.
[906.78 → 908.58] It just started a little too soon.
[908.64 → 909.56] They needed to wait.
[909.70 → 920.40] They just needed to stand outside NVIDIA headquarters with their hands open asking for just a mere few dozen H100s, you know, instead of the hundreds that they otherwise.
[920.40 → 929.68] You know, like every year the architectures come out, and it's always like 10x or 30x better or whatever it is.
[929.78 → 929.94] Right.
[930.06 → 936.08] So, like, by the time they started this year with the H100, we'd be having the same conversation.
[936.64 → 938.30] I have lots of friends at NVIDIA.
[938.86 → 941.80] And I'm just going to say some of them do actually listen to our podcast.
[941.92 → 943.58] And I'm just going to say hello out there.
[943.88 → 944.28] Great work.
[944.40 → 944.66] Yeah.
[945.18 → 946.04] Great work.
[946.34 → 947.70] But there's a little bit of fatigue.
[947.70 → 950.34] Like, you're just last year's amazing thing.
[950.42 → 951.98] You're obliterating it 30 times.
[952.10 → 952.42] Come on, man.
[952.62 → 955.18] I already bought the A100s.
[955.42 → 957.46] Like, do I get a refund now?
[957.98 → 959.32] I need some relief.
[959.76 → 962.70] We need the A100 upgrade to the H architecture.
[963.16 → 963.44] Yeah.
[963.62 → 965.80] Just to keep sane at this point.
[966.16 → 966.42] Yeah.
[966.68 → 972.32] I will say, like, the A100s as far as usage and our team uses those.
[972.50 → 976.24] We have the great privilege of having some to use.
[976.24 → 981.94] And I will say that they have been really wonderful in terms of our workflow.
[982.30 → 988.34] And one of the things that I was really actually, if you want to know, I went to the H100 page.
[988.60 → 993.42] So I also listened to some of the keynote, GTC keynote announcement stuff.
[993.42 → 995.52] But I went to the H100 page.
[995.64 → 999.90] And the very first thing I look for was the letters M-I-G-MIG.
[1000.56 → 1008.28] Because that, for those that maybe aren't familiar with the most recent architectures from NVIDIA,
[1008.28 → 1021.44] they have this what's called MIG technology, which essentially lets you take your big GPU and then split it into smaller virtual GPUs,
[1021.52 → 1026.78] which can be used, like, in independent, like, training runs or whatever you're doing.
[1026.78 → 1035.04] And I have to say, we have actually, like, loved that because we can have the big card, right?
[1035.30 → 1042.64] But most of our jobs don't require, like, every bit of the memory or every GPU we have.
[1042.76 → 1046.96] And so we have a lot of small jobs that we need to run, maybe, like, fine-tuning language models.
[1047.08 → 1048.78] That's a typical thing we do, right?
[1048.78 → 1052.44] And that doesn't take, like, a long time.
[1052.60 → 1056.08] Our data is smaller because we're doing fine-tuning or transfer learning.
[1056.90 → 1065.54] And so that's perfectly fine to run on, like, half of the A100 or, you know, maybe less of the A100, a third of the A100.
[1065.88 → 1071.94] And so I was really hoping when I went to the page, basically, I just wanted to see that that was still an option.
[1072.20 → 1074.36] And they weren't going away from that, which it is.
[1074.36 → 1075.54] It seems like that's caught on.
[1075.60 → 1077.52] I don't know if you've used that at all.
[1077.52 → 1080.20] Oh, we have, without going into specifics.
[1080.62 → 1085.20] And that was definitely, if I recall, that was introduced with the Empire architecture.
[1085.48 → 1087.30] Yeah, it was not available before.
[1087.52 → 1089.52] Yeah, it was introduced last year.
[1089.76 → 1100.54] And it's been one of those amazing utility things in terms of making what you buy a lot more useful for actual, you know, real-life jobs for most of us.
[1101.06 → 1102.16] So I agree.
[1102.46 → 1106.68] Because at the end of the day, not everybody is producing the largest language model in the world.
[1106.68 → 1108.30] It doesn't happen for most of us.
[1108.42 → 1108.90] Yeah, yeah.
[1108.94 → 1111.52] So, yeah, it's been very useful in that way.
[1111.60 → 1112.52] Yeah, speak for yourself.
[1113.64 → 1115.78] I didn't hit the train button.
[1116.24 → 1120.16] And probably most people in the workshop don't even know I exist.
[1120.68 → 1121.64] But my data is there.
[1121.94 → 1122.60] I've got that.
[1122.70 → 1124.00] Your data is in the process.
[1124.36 → 1124.80] There you go.
[1124.84 → 1125.86] It's training right now, man.
[1125.86 → 1133.28] So the other kind of interesting thing, flavour they added onto this was with the MIG technology.
[1133.28 → 1147.14] I think they've seen that catch on, and they want to make use of it more in kind of the cloud enterprise scenario where you might want more isolation between the virtual GPUs.
[1147.14 → 1156.38] And so they're making this to where you can actually have it, you know, secure end to end and multi-tenant usage of the virtual GPUs.
[1156.44 → 1160.24] Now, for us, really, it's just about like distributing our jobs.
[1160.24 → 1167.48] We don't have a lot of security concerns between like our different users accessing the different queues we're running on.
[1167.88 → 1171.22] But I think that makes a lot of sense in terms of flexibility.
[1171.22 → 1180.12] And if you were lucky enough to have a bunch of these, utilizing them well and managing sort of isolation of users and that sort of thing.
[1180.12 → 1190.54] I mean, that's a great point about the fact that, you know, that all the cloud providers are buying a lot of these, and they're trying to use them effectively within their architecture.
[1190.76 → 1194.34] And that it is certainly a key use case for the for that technology.
[1194.76 → 1197.68] For our friends at NVIDIA, I wasn't actually picking at you.
[1197.74 → 1204.30] I was kind of envious at the fact that you always kind of pull out the superpowers and do these amazing jumps.
[1204.30 → 1213.14] Yeah. So if you still want to send us. Yeah. If if you happen to have a couple spare H100s around, you know, we're here.
[1213.52 → 1216.70] I thought that was implied in what I was saying. I thought that was just there.
[1216.80 → 1219.66] And by the way, Daniel and I have two different addresses, and we can provide both.
[1219.84 → 1222.80] Yes. Yes. We have not been compensated at all.
[1223.32 → 1225.68] Video for this conversation, just to be clear.
[1225.80 → 1231.48] Not at all. But yeah, no, I think that that that will be true going forward.
[1231.48 → 1238.78] Like you mentioned, the only thing I'm wondering is in the cloud, like when I'm selecting my GPU now, like how will they be labelled?
[1239.10 → 1247.26] It's like why I use like fractions like half of H100 or like they're just going to come up with new thing.
[1247.42 → 1247.86] I don't know.
[1248.38 → 1256.58] I'm sure that the cloud providers will be very happy to charge you for a full H100, though, regardless of whether you use, you know,
[1256.58 → 1262.16] a slice compliments of the multi-instance technology that they've that they've now embedded here.
[1262.48 → 1269.92] It is interesting, as you mentioned, Chris, this focus on large language models with the new architecture.
[1270.84 → 1279.48] So in my understanding, they actually have a new set of tensor cores that are part of the processor
[1279.48 → 1286.38] that are specifically geared towards transformer architecture models.
[1286.70 → 1293.24] I mean, it makes sense that it would be a lot faster for transformers if you built something specific for transformers.
[1293.34 → 1294.76] Right. That sort of makes sense.
[1295.00 → 1296.42] Yep. They call it an engine.
[1296.80 → 1298.44] The new transformer engine.
[1298.84 → 1299.34] Vroom, vroom.
[1300.66 → 1303.96] I have like mixed feelings about this, I think.
[1304.22 → 1306.92] So first, it's great because I use a lot of transformer models.
[1306.92 → 1315.50] Like I'm not complaining, but then I do wonder what the implications are in terms of like the research world in general.
[1315.50 → 1323.14] If is the GPUs we're using have their own sort of bias towards a certain architecture type,
[1323.14 → 1332.96] does it sort of penalize people that are exploring new, different, crazy architecture types that might be the next big thing that comes along?
[1332.96 → 1342.50] It seems like, well, let's just keep exploring transformer and not do as much of that, which might be sort of, so there's less flexibility and there's a reason for it.
[1342.54 → 1345.88] But I see like they kind of have that concern a little bit.
[1346.26 → 1347.92] My answer to you is going to depress you.
[1348.00 → 1348.42] Oh, OK.
[1348.86 → 1351.22] Yeah. My answer is, of course it does.
[1351.22 → 1361.76] I mean, there 's's clearly, but that's also the marketplace, the number of true cutting edge researchers compared to the ninety-nine point nine nine nine percent.
[1361.98 → 1364.06] That are just cranking inferences out of a.
[1364.42 → 1364.90] That's right.
[1364.96 → 1368.98] Cranking inferences out all over the place, but not truly doing cutting edge research.
[1369.60 → 1376.02] Yes, it's making its making life easier for the ninety-nine point nine nine nine percent.
[1376.02 → 1384.06] They're not helping you if you happen to be in the pure research, which is funny because I, you know, to your point, that's what I want to see more of.
[1384.16 → 1389.54] I would rather I would love to see just while I'm doing my wish list since we're talking about it.
[1389.60 → 1391.70] We wandered into this, blundered into this.
[1391.96 → 1396.66] I would love to see some new architectures out there in the deep learning space.
[1396.66 → 1402.42] It's been a little while since we've had a major, major shift, and I'm I'm waiting for that.
[1402.76 → 1405.42] So that's my it's on my Christmas list right there.
[1405.42 → 1414.12] Yeah. And if I'm just looking, so I'm this is a lot of interpretation, and sorry for whoever designed the page if this wasn't how it was supposed to be read.
[1414.24 → 1421.62] But I see kind of on the H100 page in order of priority, kind of at the top is the transformer engine thing.
[1421.62 → 1426.12] And then right after that is real time deep learning inference.
[1426.12 → 1434.52] So the speed-ups in inference, which like you're talking about, and I think has been mentioned by multiple guests on the show.
[1434.64 → 1440.30] Right. The bulk of operations in kind of the enterprise AI world are inferences.
[1440.46 → 1442.38] Right. Because you train a model, and then you do it.
[1442.38 → 1445.66] You use it billions and billions of times.
[1445.66 → 1458.20] And so that I think is really cool that you can have more throughput on the inference side and be more efficient maybe with less, you know, fewer cards.
[1458.74 → 1463.86] So, yeah, I can see why that side of things is prioritized for sure.
[1464.08 → 1466.12] Sure. Yeah. It's hitting most of their customers.
[1466.12 → 1470.70] Now, they also they bring in the omni verse to this.
[1471.64 → 1479.86] So I don't know if you saw that reference, but it's like, so obviously there's the metaverse, which is for those.
[1480.36 → 1489.10] I assume a lot of people know what that is out there, but it's like the virtual reality world that Facebook or meta is designing and running.
[1489.28 → 1491.38] I don't know. Have you been in the metaverse, Chris?
[1491.38 → 1495.10] I have not been in the metaverse, but I am quite familiar with omni verse.
[1495.10 → 1508.52] Yeah. So I've been in the metaverse and I think it's cool that like there's this effort to develop like these 3D sort of simulations, 3D worlds, VR, all of that's cool.
[1508.66 → 1512.78] And maybe since you're more familiar with the omni verse, you can talk about that.
[1512.84 → 1519.10] But I am not a computer graphics person, but obviously these are graphical processing units.
[1519.10 → 1527.72] So to support those 3D worlds, I think that is one of the things they're featuring as something that this could enable.
[1527.72 → 1534.70] So it's funny, we're taking a little bit of a tangent here, but AI driven simulation is a huge thing.
[1534.90 → 1540.14] And maybe not for the reasons that everyone is most often associating.
[1540.36 → 1549.48] It's less about leisure and recreation and such as that and more about having digital twins for manufacturing design and things like that.
[1549.48 → 1558.28] So that you're able to try and experiment on things that would otherwise be too costly in the real world to experiment on.
[1558.78 → 1571.18] And so anyway, that's the context is looking at omni verse in the context of using GPUs so that we can try some otherwise really hard things to do.
[1571.18 → 1579.26] Yeah, looking forward to seeing more of that cool 3D stuff, especially where it intersects AI and simulation.
[1579.64 → 1585.06] One more thing that just related to all of this NVIDIA stuff that's happening.
[1585.70 → 1596.54] I don't know if you also saw as part of what was talked about this supercomputer that NVIDIA is working to build Earth 2 supercomputer.
[1596.54 → 1601.34] Now, I don't think there was an Earth 1 supercomputer.
[1602.08 → 1605.00] I think it's Earth 2 supercomputer because it's...
[1605.00 → 1605.64] Where Earth 1?
[1605.74 → 1609.00] Literally, it's running a clone of Earth.
[1609.30 → 1614.14] Like there is a virtual Earth 2 that's in the computer.
[1614.40 → 1615.92] Is that how I'm understanding that?
[1616.10 → 1619.48] I'm actually not super familiar with that, but I'm assuming so.
[1619.56 → 1623.78] I mean, it seems that that would be the natural thing to be working towards.
[1623.86 → 1624.92] So maybe this is it.
[1624.92 → 1626.98] That was the one thing I was not...
[1626.98 → 1628.28] I had not dived into before the show.
[1628.60 → 1632.40] Yeah, I think in my understanding, they've built this supercomputer.
[1633.28 → 1637.32] There's sort of a clone of Earth virtual world.
[1637.60 → 1645.16] And they're doing weather and climate simulations that are not sort of like a random side topic.
[1645.16 → 1656.48] My first job out of college was at NCAR in Boulder, which is the National Centre for Atmospheric Research, where they do have big supercomputers to do climate modelling.
[1656.84 → 1660.48] That's what I did that summer is benchmarking some of that software.
[1660.48 → 1672.98] But those climate models kind of operate around like fluid dynamics and other types of physics simulations and that sort of thing.
[1673.16 → 1675.04] Physics and chemistry simulations.
[1675.04 → 1692.74] This, in my understanding, these weather predictions that they're doing in this Earth 2 supercomputer are driven by, at least partially by AI predictions of weather conditions and climate, which is kind of an interesting...
[1692.74 → 1699.52] It might be a subtle point, but it is very different from sort of how climate models have operated for quite some time.
[1699.52 → 1703.06] So I'm actually somewhat familiar with that, at least lightly.
[1703.46 → 1706.18] It still is computational fluid dynamics.
[1706.36 → 1710.44] CFD is the short, is the lingo that people use in the industry.
[1711.00 → 1723.80] And we are seeing and have been for the last few years and are continuing to see a very large shift from CPU-driven CFD simulations into AI-driven with GPUs.
[1723.80 → 1730.98] And really, the holdup there is usually the software being used as written for older CPU things.
[1731.18 → 1739.04] And so, in general, industry is kind of trying to catch up with the technology at this point in terms of updating their software to do that.
[1739.14 → 1745.90] But yeah, I think that is the future of computational fluid dynamics is this kind of simulation that's GPU-driven.
[1745.90 → 1756.44] Yeah, and they specifically reference in the article, physics-informed neural networks, which I think that would be a great show in and of itself.
[1756.72 → 1762.68] So if you are out there, and you're working on such things, reach out to us, and we'd love to talk about it on the show.
[1762.92 → 1764.06] That would be very interesting.
[1764.48 → 1769.04] Yeah, I would be super interested to hear more about that.
[1769.36 → 1774.16] Yeah, any other things that stood out to you with this NVIDIA stuff, Chris?
[1774.16 → 1781.92] No, but I actually have, believe it or not, I actually have a CFD, a computational fluid dynamics project that I would like to try.
[1782.12 → 1784.40] And it's relating to a real world thing.
[1785.08 → 1787.26] So the two-second backstory.
[1787.50 → 1788.26] Give me the pitch.
[1788.56 → 1789.84] Why a combinatory pitch?
[1789.98 → 1796.38] As longtime listeners may know, I'm a private pilot and I fly in the Great Smoky Mountains on many weekends.
[1796.38 → 1809.08] And that's one of the few places where you have mountains that are high enough to create mountain waves, which are giant waves of atmosphere that hit the mountains, and they go up and then they crash down.
[1809.34 → 1818.42] I actually had a very dangerous moment where I got hit by an invisible mountain wave, flip my plane upside down, and I had to recover over the peaks.
[1818.76 → 1819.94] I didn't even hear about this.
[1820.16 → 1821.08] You about died.
[1821.08 → 1824.36] It was very close or ripping the wings off the plane kind of thing.
[1824.46 → 1828.40] So this happened earlier this year, early in 2022.
[1828.84 → 1834.80] But it made me keenly interested in the fluid dynamics of mountain waves.
[1834.88 → 1841.84] And so if anybody is looking for a CFD toy project, and you want to look at that in the Smoky Mountains, you may save my life later.
[1841.96 → 1843.40] So that's the pitch.
[1843.40 → 1850.76] If you like the podcast, and you want to see it perpetuated, then you got to save my life so that I don't get driven into the ground by a mountain wave.
[1850.82 → 1851.18] How's that?
[1851.26 → 1852.64] Is that exciting enough for you, Daniel?
[1852.86 → 1863.20] If you could inference fast, and you did get the light bulb blinking, the warning that you were about to be overtaken by a mountain wave, would you have time to respond?
[1863.48 → 1864.00] I don't know.
[1864.06 → 1867.46] I guess it depends on how fast the GPU can do this inference.
[1867.46 → 1872.92] I'm going to have to really dig into the Hopper architecture to see if it's going to save my life or not.
[1873.26 → 1879.76] Yeah, maybe you can create a digital twin of yourself in the plane in the Omni verse and run the simulation.
[1880.10 → 1885.42] Oh, I'm frightened, though, that if I do that, and it's really, perfect, I might just not need to fly anymore.
[1885.58 → 1887.92] And I don't know that that's a non-starter right there.
[1888.86 → 1890.74] Do you see how tied all those things together?
[1890.82 → 1891.48] I saw that.
[1891.58 → 1892.10] They don't normally go together.
[1892.30 → 1892.90] There we go.
[1893.02 → 1893.76] Having fun today.
[1894.18 → 1894.86] Yeah, exactly.
[1894.86 → 1912.80] Speaking of tying all things together, we actually not that long ago in the I think, fall of last year, we talked about a few things related to the AI index report, which comes out of Stanford, measures trends and artificial intelligence.
[1913.46 → 1915.66] Actually, the next version of that is out.
[1915.66 → 1927.90] So because we talked about it recently, we won't spend a whole episode on it, but maybe it's worth bringing up here as we close out our fully connected episode just to kind of skim the top takeaways.
[1928.18 → 1931.28] And we'll definitely include it in our show notes, so people can look at it.
[1931.38 → 1940.54] I noticed that one of the top takeaways on theme is language models are more capable than ever, but are also more biased.
[1940.54 → 1942.56] That's one of their key takeaways.
[1942.76 → 1950.70] So big science language models are going to be more capable, but maybe it's worth exploring the bias.
[1950.88 → 1955.88] I think that research workshop has done an amazing job at exploring the data and the bias.
[1956.00 → 1959.16] They even created their own tool to explore such things.
[1959.28 → 1961.40] But yeah, it's still a problem, right?
[1961.64 → 1962.18] It's interesting.
[1962.40 → 1963.12] It is a problem.
[1963.12 → 1971.64] And I think that exploring the bias actually ties into another thing that we're seeing there just to pull two together, and that's the rise of AI ethics everywhere.
[1972.28 → 1975.00] And we're also seeing they have a note on data, data, data.
[1975.52 → 1986.50] And maybe sometimes we need to go back and address some of that because bigger may be better in many cases, but not if it's bigger bias.
[1986.50 → 1987.02] Yeah.
[1987.52 → 1992.08] Also, notice a shout-out to our friends over at ML Commons.
[1992.48 → 2004.92] David, who has been on the show a couple of times, they mentioned that ML Perf task and benchmark related to AI performance in terms of training time and compute.
[2005.56 → 2011.00] Their big takeaway is AI becomes more affordable and higher performing.
[2011.00 → 2013.54] So I think and being the key word there.
[2013.74 → 2028.68] So they give this statistic that since 2018, the cost to train an image classification system has decreased by around 63%, while training times have improved by 94%.
[2028.68 → 2030.24] So pretty cool.
[2030.24 → 2041.36] This sort of like combination of more affordable and higher performing, which is, you know, they talk about driving widespread commercial adoption and blah, blah, blah.
[2041.72 → 2048.98] I mean, in all of this, it's just the field is exploding in terms, you know, exploding positively, not a negative explosion.
[2049.44 → 2053.50] In terms of that, there's so much money flowing into it.
[2053.50 → 2063.96] They are noting, you know, kind of driving that process that private investment is soaring, but that investment is also becoming more and more concentrated as well.
[2064.14 → 2069.90] So you're seeing winners and losers also kind of coming into play there.
[2070.34 → 2073.56] And I frankly think a lot of these topics are interrelated.
[2073.56 → 2080.28] I think that comes back to things like, you know, the ethics of it and where you're going to place investment and what you're getting out of it.
[2080.68 → 2082.40] I really find this an interesting report.
[2082.40 → 2098.00] I know that they always are, but I think the thing that I noticed this time as we've looked through it is we're seeing a lot of direct kind of like one topic directly relates to another one that they have there rather than being all à la carte topics.
[2098.34 → 2100.88] We definitely have some challenges in this space.
[2100.98 → 2106.80] I mean, it's like it's overall perfect news, you know, cheaper training, cheaper inference, more productive.
[2107.12 → 2107.98] It's going everywhere.
[2107.98 → 2110.06] But we're also seeing bias.
[2110.26 → 2112.18] We're seeing concentration of power.
[2112.62 → 2116.36] We're seeing, you know, the challenge of how to tackle AI.
[2116.48 → 2121.76] And there's a whole industry around AI ethics now, which I'm supportive of, but also a little bit.
[2122.10 → 2126.34] I don't think they always capture it very well in terms of getting to the mean.
[2126.40 → 2127.40] It's a business still.
[2127.60 → 2129.10] So nothing against business.
[2129.26 → 2133.08] Just saying that we have some challenging things in front of us to solve.
[2133.08 → 2136.12] Yeah, no, definitely challenging things.
[2136.64 → 2144.08] But apparently one of the challenges is that's disappearing is access to robotic arms.
[2144.28 → 2148.06] I don't know if I was surprised, but it was like, oh, that made a top takeaway.
[2148.38 → 2150.08] Robotic arms becoming cheaper.
[2150.88 → 2151.36] Newsflash.
[2151.72 → 2154.22] That was literally the next thing I was going to bring up.
[2154.22 → 2170.78] And that is, as they are becoming cheaper, we're going to be seeing more and more, you know, for a while, our exposure to AI has been through kind of existing mechanisms, our laptops and, you know, things that have access to cloud providers and stuff like that.
[2170.78 → 2182.50] But if the robotic side is coming down in price so much, then I think more of us will start interacting with AI in new and novel ways that were not previously widely distributed.
[2182.94 → 2186.64] That will be another interesting change in how we live our lives.
[2186.98 → 2189.08] So it's really going to be pervasive.
[2189.62 → 2192.10] So where do you think I'm going to start seeing robot arms?
[2192.48 → 2195.00] Where am I going to start interacting with them, do you think?
[2195.00 → 2202.40] Well, I just know that I am positive they don't have arms on them, but we have these little robotic vacuum cleaners running around.
[2202.66 → 2202.74] Right.
[2202.96 → 2206.54] And we're starting to move into the thing where they're going to have inferences.
[2206.80 → 2211.18] They're going to be able to like reach over and pick up my Coke can and toss it into the trash.
[2211.40 → 2211.60] Yeah.
[2211.74 → 2216.86] I mean, I'm really thinking, was it Fred Flintstones that had the robot made that moved around?
[2216.96 → 2218.56] Am I thinking the right cartoon?
[2218.78 → 2219.04] I don't know.
[2219.04 → 2226.40] There was one that had the old-fashioned 1950s-ish looking robot, and she was running it, Rosie the robot or something like that.
[2226.68 → 2233.36] And I'm just saying, you know, it's taken another century almost, but maybe we're getting awfully close to.
[2233.46 → 2241.18] We're moving from the little disc robot vacuum cleaner scooting around our living rooms and maybe Rosie the robot is right there.
[2241.44 → 2244.98] And I apologize for the implied sexism.
[2244.98 → 2250.20] I'm calling up a character I saw in the past in a more sexist TV world.
[2250.32 → 2251.80] It's not my own thing.
[2252.68 → 2255.36] That little moment of awkwardness right there as I realized that.
[2255.42 → 2255.62] Right.
[2255.82 → 2262.80] As you realize that your language is biased, which is going to be recorded and put in a language model, which will then be biased.
[2263.10 → 2263.32] God.
[2263.66 → 2263.96] Yeah.
[2264.36 → 2268.74] I was merely trying to recall a cartoon from my childhood and look what happened.
[2268.74 → 2281.40] Well, I mean, I'm sure that that cartoon is transcribed somewhere and probably sucked into common crawl from some crawling bot that is producing that in our data sets.
[2281.76 → 2282.84] And it probably is.
[2282.92 → 2290.34] We're going to have to just delete Rosie the robot from the collective, you know, storage of all data out there.
[2290.48 → 2291.34] It's gone.
[2291.66 → 2291.88] Yeah.
[2291.98 → 2297.32] Well, I would recommend we're not going to go over everything in this report for sure.
[2297.32 → 2301.14] We will link it in our show notes, the AI index report.
[2301.50 → 2302.90] It's always a good thing to look at.
[2303.08 → 2306.80] It includes a lot more information than we talked about.
[2306.98 → 2310.20] So take a look at it, you know, keep up with the latest trends.
[2310.34 → 2313.26] That's what we try to do here practically.
[2313.70 → 2318.82] And speaking of practical things, we've highlighted quite a bit of NVIDIA things this episode.
[2318.82 → 2326.56] So just remind people in terms of a learning resource, you can watch a lot of the GTC content online.
[2326.56 → 2330.86] So obviously it is produced by NVIDIA.
[2331.04 → 2333.46] So you're going to see the NVIDIA perspective.
[2333.82 → 2335.90] But NVIDIA is also dominant in the market.
[2335.90 → 2340.72] So you're going to hear a lot of really great things and lots of perfect things to learn there.
[2340.72 → 2355.42] But they also have what's called the NVIDIA Deep Learning Institute, which can help you with online courses in terms of using the latest GPUs and acceleration on GPUs and a bunch of things.
[2355.42 → 2363.80] So in terms of learning resources, I know I've mentioned that one before, but because it's GTC week, it seems relevant to mention it again.
[2363.80 → 2365.06] That's a good call out.
[2365.14 → 2367.40] And those Deep Learning Institute courses are quite good.
[2367.50 → 2370.38] I've taken several of them myself and always enjoyed them.
[2370.82 → 2374.72] Once again, I'm not trying to promote their stuff, but I've just said I have found it useful.
[2375.00 → 2378.90] And they hit a wider range of topics of interest.
[2379.24 → 2380.78] It's okay to mention good things.
[2381.06 → 2381.38] There you go.
[2381.38 → 2384.40] So I appreciated this conversation, Chris.
[2384.48 → 2385.64] It's been fun.
[2385.80 → 2388.18] We'll link to everything in our show notes.
[2388.52 → 2390.56] Please find us online.
[2390.76 → 2394.70] You can engage with us if you go to changelog.com slash community.
[2394.70 → 2397.82] You can find us in Slack or LinkedIn or Twitter.
[2398.72 → 2399.44] Engage with us.
[2399.52 → 2404.20] Let us know your thoughts on this various news stuff.
[2404.84 → 2407.02] And yeah, we'd love to hear from you.
[2407.36 → 2409.40] So thanks for the conversation, Chris.
[2409.44 → 2410.46] We'll talk to you next time.
[2410.46 → 2411.64] Talk to you next time.
[2414.88 → 2415.80] All right.
[2415.92 → 2417.90] That is Practical AI for this week.
[2418.16 → 2424.74] If this is your first time listening, subscribe now at practicalai.fm or just search for Practical
[2424.74 → 2426.50] AI in your favourite podcast app.
[2426.70 → 2427.22] We're in there.
[2427.62 → 2430.72] And if you're a longtime listener, please do share the show with your friends.
[2430.96 → 2433.68] It is the best way you can help Practical AI succeed.
[2434.12 → 2439.08] Thanks again to Vastly for shipping our shows superfast all around the world to Break master
[2439.08 → 2440.04] Cylinder for the Beats.
[2440.22 → 2441.22] And to you for listening.
[2441.46 → 2442.16] We appreciate you.
[2442.56 → 2443.62] That's all for this week.
[2443.76 → 2444.86] We'll talk to you again next time.
[2444.86 → 2445.52] All right.
[2445.52 → 2475.50] Thank you.
[2475.52 → 2476.52] Thank you.
