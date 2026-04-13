[0.00 → 7.08] The definition that we've come up with is if you have a speech-to-text model that performs
[7.08 → 13.28] statistically worse for a certain demographic group, then that model is said to be biased.
[13.80 → 19.64] So using this corpus, the already biased corpus, you can take any off-the-shelf speech recognition
[19.64 → 27.62] model and look at what is its accuracy or word error rate, as we call it, for a certain demographic
[27.62 → 33.04] group. Thanks to Jenny and everybody at Common Voice, we have information from people who opted in
[33.04 → 41.16] to self-identify their gender, their accent, and their age. So along any of those lines,
[41.20 → 46.26] you can look at how well your model performs on every group versus every other group.
[48.30 → 54.88] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[54.88 → 59.44] things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[59.44 → 63.34] on Linde cloud servers. Head to linode.com slash Changelog.
[66.38 → 72.76] Linde is our cloud server of choice. Grab the NATO plan for just $5 a month, just $5. That gets you
[72.76 → 78.50] a gig of RAM, a blazing fast 25 gig SSD, and one terabyte of transfer. Let's be honest, you can go
[78.50 → 84.16] a long ways on that $5. When you do need to scale up, their prices are predictable, so you can put your
[84.16 → 88.58] calculator down. You won't need it. We've been running ChangeLog.com on Linde for years, and we've
[88.58 → 94.18] always impressed by their award-winning support team. Check them out at linode.com slash Changelog.
[94.38 → 97.56] Once again, that's linode.com slash Changelog.
[107.04 → 112.00] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[112.00 → 116.48] productive, productive, and accessible to everyone. This is where conversations around AI,
[116.76 → 121.12] machine learning, and data science happen. Join the community and Slack with us around various
[121.12 → 126.58] topics of the show at ChangeLog.com slash community, and follow us on Twitter. We're at Practical AI FM.
[133.06 → 140.42] Welcome to another episode of Practical AI. This is Daniel Whiten ack. I am a data scientist
[140.42 → 147.26] with SIL International, and I've got Chris Benson with me, who is a principal emerging technology
[147.26 → 151.94] strategist at Lockheed Martin. How are you doing, Chris? I'm doing very well today. Daniel, how's it
[151.94 → 157.18] going? It's going perfect. This last week was a fun week. I've been writing a lot of
[157.18 → 163.86] inferencing API code, which has been fun. It's been one of those weeks that I've got to be,
[163.86 → 170.52] you know, heads down in code a lot, and I always enjoy that bit of it. It's like getting the various
[170.52 → 176.24] pieces plumbed together and working, and then you have your models together, and you actually see it
[176.24 → 181.62] work practically. That's always fun for me. So what about yourself? Last week was pretty
[181.62 → 186.88] interesting. I'll relay really quickly a kind of what for me was a work-related thing, but not in a
[186.88 → 194.60] direct way. So DARPA, the Defense Advanced Research Projects Agency, had a competition, and they had a
[194.60 → 200.88] bunch of autonomy-focused companies, including my, just as we were there too, Lockheed Martin, that were
[200.88 → 207.46] competing in what was called Alpha Dogfight. And so they had gotten, at Johns Hopkins University, they had
[207.46 → 213.90] gotten an F-16 flight simulator, and they had all the teams over the last few months getting their models
[213.90 → 220.94] of their F-16s ready to go into dogfighting mode. And so they had the competition last week, and they
[220.94 → 227.08] live-streamed the entire thing on YouTube. So it was pretty cool to watch. And so in the end, a company
[227.08 → 233.48] called Heron Systems won out overall. Our own team came in second out of eight teams. But it was
[233.48 → 239.42] interesting is that Heron actually went up against a if it was the Navy, it would be a Top Gun instructor.
[239.42 → 245.62] It was the Air Force. The call signs was banger. And within a set of constraints, it was interesting.
[245.82 → 254.96] The AI consistently beat the human pilot instructor. So yeah, it was, nobody was expecting that. So
[254.96 → 259.18] the AI models did very, very well, much better than anyone realized.
[259.66 → 265.90] When you first said that, I was, I was thinking of like Battle Bots, Boston Dynamics, like dogs going
[265.90 → 271.40] against, when you said dogfighting, I guess I'm not around, you know, aeronautics very much. And
[271.40 → 277.76] that seems way more violent. And yeah, no, airplanes in the air, still quite violent in theory, but yes,
[277.76 → 283.14] I guess that's true. Yeah. But not adorable furry little creatures. Definitely. So, but anyway,
[283.14 → 288.08] it was pretty fascinating to watch. It was a moment where people went, hmm, things are definitely
[288.08 → 290.00] changing right now. So that was my week.
[290.00 → 296.98] Interesting. That brings up all sorts of interesting questions and ethical things and all of that,
[297.08 → 300.26] that I'm sure we'll get into as the podcast goes on as well.
[300.40 → 301.18] I'm sure we will.
[301.42 → 306.28] But yeah, I'm, I'm pretty excited about today's episode. As some of our listeners will know,
[306.34 → 310.86] I think I've mentioned a couple of times that I've been getting into speech technology a little bit
[310.86 → 317.48] more for my own work in recent months. And one of the things like if you're going to train a speech
[317.48 → 322.92] recognition model, and you're looking at what, what speech data is out there. One of the things that
[322.92 → 329.32] pops up fairly, you know, prominently in that is Mozilla's common voice project. And Mozilla is doing
[329.32 → 333.28] some really cool things also through their fellowship program with speech technology.
[334.06 → 341.00] And so today we've got Remy Muir, Jenny Zhang, and Josh Meyer with us, who are going to talk a little
[341.00 → 348.18] bit about common voice and other things going on through the Mozilla fellowship program. So welcome,
[348.36 → 350.04] everyone. It's really great to have you here.
[350.40 → 350.68] Thanks, Dan.
[350.86 → 351.94] Thanks. Nice to be here.
[352.22 → 358.02] Yeah. So before we jump into common voice and speech technology and all the wonderful things that
[358.02 → 364.46] you're doing, maybe we could start out by just having a brief discussion about your respective
[364.46 → 370.18] backgrounds. Remy, do you want to start us out and tell us a little bit about your background and how you
[370.18 → 371.74] got involved in speech technology?
[372.22 → 379.44] Thank you, Daniel. Yeah. So I think my background started as a software engineer. So I still actually
[379.44 → 388.12] write codes, but not often. And I also contribute on some open source library in Africa as well with a
[388.12 → 395.48] couple of friends. Yeah. I would say I spent actually six years. This is my year six actually writing codes.
[395.48 → 404.74] And the journey actually started in 2013, learning about C, Python, and JavaScript. And been working in
[404.74 → 412.84] actually a couple of startups in Kigali, especially startup retention technologies. Yeah. And before that,
[412.92 → 421.12] how I actually get into voice technology was a project I tried to actually do with a friend. So which were
[421.12 → 427.88] about actually voice recognition. So how like a NARP would actually help people around speaking
[427.88 → 433.54] actually their native language, actually seeking for information. Yeah. But unfortunately, we couldn't
[433.54 → 443.12] actually move the project since there weren't actually any Kenya Rwanda data sets. And Kenya Rwanda is one of the
[443.12 → 450.80] local languages spoken actually in Rwanda in Kigali. Yeah. Currently working with Mozilla as a community
[450.80 → 457.76] fellow on voice tech. Yeah. Awesome. Yeah, that's great. And I'm really excited to dive into the details
[457.76 → 464.34] of some of that in a bit. Before we do, Jenny, would you let us know the same a little bit about your
[464.34 → 470.18] background? Yeah, thank you. I'm a software engineer primarily, and I have a strong focus in my work on
[470.18 → 475.74] ethical tech, data governance and privacy rights. And so I kind of found my way through common voice and open voice
[475.74 → 482.96] tech via those avenues. So currently, I lead the engineering work on the common voice project, both in terms of the
[482.96 → 487.04] web platform and the data infrastructure around it and kind of help set the technical strategy.
[487.88 → 490.78] Awesome. Yeah. And then Josh, what's your background?
[491.32 → 499.70] Yeah, I got into speech technology from linguistics, actually, I was in academia doing more kind of cognitive
[499.70 → 509.36] science and phonetics, phonology, perception, kind of the acoustic side of things. And I started to learn
[509.36 → 516.14] more about computational linguistics and NLP and speech technology. And, and that really sucked me in
[516.14 → 522.40] because that's something where you can see users actually interacting with what you're doing. And that
[522.40 → 529.44] was really rewarding. So recently, just last year, I finished my PhD on speech recognition for low
[529.44 → 535.26] resource languages. And during that, towards the end of the dissertation, I was working with the
[535.26 → 542.22] machine learning group at Mozilla doing some things with deep speech, trying to make it kind of trying to
[542.22 → 547.10] find an approach that could scale to new languages easily for speech recognition.
[547.64 → 552.88] Yeah. And deep speech, just for those that aren't familiar, that's a project coming out of Mozilla as well?
[552.88 → 561.94] Yes, it's called deep speech. Baidu originally named it. But deep speech is an open source speech to text
[561.94 → 569.62] software stack includes code for training code for inference, and also pre-trained models. And so
[569.62 → 578.30] today I am a fellow at the Mozilla Foundation working on this project for African languages and deep
[578.30 → 588.12] speech and common voice. And also my normal day job is lead scientist for speech technology at a startup in Los Angeles
[588.12 → 589.18] called RD Inc.
[589.70 → 597.36] Very cool. I guess, to get us started, Jenny, I'm wondering, when common voice started, what was the state of speech
[597.36 → 603.02] data in general, at the time? And you know, what were you able to get your hands on? You know, what was the practical
[603.02 → 610.56] aspect of getting started at that point? So common voice started in the summer of 2017. I don't know
[610.56 → 616.76] exactly what the state of open speech data was at the time. But I do know that it was not the norm to
[616.76 → 625.98] have data sets. So for context, you know, Siri came out in 2011, Alexa came out in 2014. So by mid 2017,
[625.98 → 633.22] there really hadn't been a ton of work on speech recognition and voice technology stacks in general
[633.22 → 638.54] that was available to the public. The big companies obviously are not particularly interested
[638.54 → 643.72] either in releasing the training data that they have been working on, or making those stacks open
[643.72 → 649.88] source. And so there have been a few data sets that have been doing a tremendous amount of work trying
[649.88 → 657.58] to find these open data sets and trying to basically look at large corpuses of voice data like audio, like open
[657.58 → 662.72] source audiobooks, and those sorts of things, in order to turn data set that was initially intended for something
[662.72 → 668.96] else for voice recognition. But the as is often the case with open source projects, and as is often the case with
[668.96 → 677.42] sort of internet, volunteer labour, it was heavily focused on English, it was not diverse. And oftentimes, there was not
[677.42 → 685.56] really a good sense of a roadmap to get from, you know, the initial 200 500 hours of English, to a place
[685.56 → 691.90] where the speech data set can actually represent the user base of the internet more broadly. And so that was
[691.90 → 699.08] kind of the initial impetus for common voice, we wanted to experiment with having something that was
[699.08 → 705.42] crowdsourced and decentralized in the best way and look at how we can really democratize tech and bring
[705.42 → 708.34] people into the fold who were traditionally left out.
[708.94 → 714.82] Yeah. And Josh, maybe this is a question for you, since you're working in your PhD, but in terms of state of the
[714.82 → 722.56] art right now, and what people are doing, what is the sort of for something like speech recognition, how much data
[722.56 → 729.62] or how many hours of speech data do you need sort of on general, I know that's difficult, because it's, there are accents
[729.62 → 735.72] in gender and, and it's different for different languages, and all of those things. But what sort of scale are we
[735.72 → 744.00] talking about, in terms of getting something that's functional for speech recognition? What is the sort of scale in
[744.00 → 747.96] terms of numbers of hours of audio that's transcribed that we need?
[747.96 → 754.16] Yeah, this is a very good question. And it's, it's kind of the million-dollar question everybody wants
[754.16 → 760.98] to know, how much data do you need to make an application that's useful, that's based on speech
[760.98 → 771.16] to text? This is, it's really dependent on the application, you can actually get by, in some cases with zero
[771.16 → 776.32] data. I know it sounds kind of crazy. But if you have a really, really low resource language,
[776.32 → 782.76] you can actually take an existing model from a high resource language, you can take an English
[782.76 → 792.10] model, let's say, and basically just transliterate the words that you care about for the target language.
[792.36 → 798.42] And so you can kind of hack an English model to recognize, let's say, Welsh. I know people have
[798.42 → 805.82] done this for Welsh, for example. But that usually works only when you have kind of limited
[805.82 → 812.18] domain tasks when you have a small vocabulary. So if you're, let's say, you're trying to recognize
[812.18 → 818.96] numbers, the single digit numbers from zero to nine, you might be able to do that for a new language
[818.96 → 825.32] just by kind of transliterating what the English model thinks it's hurt. If you want something that's
[825.32 → 833.88] going to be more open-ended, like a really robust speech recognition model that can recognize any
[833.88 → 841.70] phrase, any word in some target language. This is a hard to put a number of hours. People will usually
[841.70 → 849.74] say 2000 hours, but that number comes from some standard English corpora like Libra Speech and
[849.74 → 855.58] Fisher. But that's a number that's, I think, a pretty safe one to say if you want something that's really
[855.58 → 861.76] open domain for some target language, and you're not assuming that you're going to do some kind of
[861.76 → 867.56] transfer learning from a source language model. I think 2000 hours is something people would say,
[867.66 → 871.48] but it really depends on what your target application is.
[871.84 → 877.40] Yeah. And I know that, you know, Jenny, you were saying that the kind of state of speech data,
[877.52 → 883.26] at least how it developed, of course, there was a lot of data available for English and maybe other
[883.26 → 888.20] major languages starting out. And I know that it was hard to put a number on that, Josh,
[888.20 → 893.10] but at least gives us a sort of scale. I'm assuming, maybe Remy, you could speak to this,
[893.10 → 900.40] but I'm assuming that for many, for example, African languages, we might have kind of zero data
[900.40 → 907.48] available, at least in open data. In some cases, we might have some more. In terms of the languages that
[907.48 → 911.28] you're working with, Remy, what is the sort of state of the data?
[911.28 → 918.40] Okay. So, yeah, I think, like, some of the language we're working on, we're currently working on with
[918.40 → 925.86] Kinyarwanda, which is actually a very well-documented language. And so, Kinyarwanda actually has, like,
[925.92 → 933.32] over, like, 12 million speakers, like, in Rwanda. And to give you just, like, a background,
[933.32 → 939.38] most of the administration, administrative, actually, administrative government in Kigali,
[939.38 → 946.16] so use, actually, Kinyarwanda as a very language in their daily operations. So, giving that, like,
[946.16 → 954.26] so, a plenty of resources, like, consulting as well, like, the Bible, which is, the Bible, which is
[954.26 → 962.20] actually very well-documented in Kinyarwanda as well. And so, a lot of newspaper around, yeah. So, I think for
[962.20 → 968.62] Kinyarwanda, we have actually a very useful, actually, discopperity to use with, yeah.
[969.26 → 975.10] So, Jenny, I was kind of wondering, like, at this point, as we're looking at Common Voice today,
[975.58 → 981.52] kind of what is the state of Common Voice currently, and what kind of functionality is available in the
[981.52 → 981.84] platform?
[982.48 → 987.80] Yeah. Common Voice, the platform has, the core platform, which you see when you go to
[987.80 → 994.88] commonvoice.mozilla.org, really focuses on the data collection aspect. So, on one hand,
[995.16 → 1000.08] you go to Common Voice, and you click on Speak, and you will be given any number of randomly selected
[1000.08 → 1005.72] sentences from our available text corpus for you to read out loud. And if you would like to validate,
[1006.00 → 1011.50] you will be given recordings that other contributors have recorded, and you can say,
[1011.50 → 1016.14] this does or does not match the text. And generally speaking, we have a criterion for
[1016.14 → 1020.62] when we consider a recording to have been sufficiently validated by the community.
[1021.28 → 1026.04] And so, the Common Voice platform is really the first step in the pipeline to getting to our dataset.
[1026.48 → 1031.72] And that's just a web app. It's available on all platforms. There's a little bit of stickiness with
[1031.72 → 1039.42] mobile Safari, you know, due to just the vagaries of media recorder API implementation. But we're doing our
[1039.42 → 1045.66] best to make sure it's as widely accessible as possible. And then the Common Voice dataset,
[1046.02 → 1052.88] the output of all of this volunteer effort, the last dataset we released in June had 7,200 recorded
[1052.88 → 1061.52] hours in 54 languages, of which about 5,600 have been validated by volunteers. And so, when, you know,
[1061.58 → 1067.80] this is a constantly growing number, so that dataset had 54 languages, but the current Common Voice
[1067.80 → 1073.38] Corpus overall has 56 languages, and, you know, it's, that number is getting bigger every time.
[1073.84 → 1079.64] So, right now, we're looking at approximately just a little bit under 400,000 unique contributors
[1079.64 → 1087.26] who have either done recording or validation and, you know, over 130,000 unique voices in the dataset.
[1087.94 → 1093.70] And quick follow-up to that, and speaking as probably the non-NLP, you know, person on this
[1093.70 → 1100.38] podcast. When you say validation by volunteers, what exactly does that mean, just for those of us
[1100.38 → 1101.14] who aren't familiar with it?
[1101.74 → 1106.88] Yeah. So, the Common Voice approach to validation, and Josh can correct me if this is wrong,
[1107.00 → 1113.38] is a little bit unorthodox when it comes to how we normally think about NLP annotation. So,
[1113.44 → 1119.70] basically, for the purposes of training, you want to make sure that a piece of audio matches
[1119.70 → 1126.08] matches the transcribed text as much as possible, you know, without the UMS and us of the usual
[1126.08 → 1132.96] speech patterns, without any punctuation, or, you know, any of those sorts of things. And normally,
[1133.08 → 1138.76] how that happens is you're given an audio, and the person who was doing the annotation would
[1138.76 → 1146.58] write down what they thought the audio was, or vice versa. Because all of our contributions are
[1146.58 → 1153.12] community-led, and the scale is such that we can't internally, as a team, do QA on it.
[1153.38 → 1157.98] We're really relying on our community members to listen to the recordings that have come through
[1157.98 → 1163.82] and say, do I think that this recording exactly matches the sentence that it's supposed to match?
[1164.30 → 1171.90] So, you know, if the sentence is, the quick brown fox jumped over the lazy dog, and somebody reads,
[1172.36 → 1176.22] a quick brown fox jumped over the lazy dog, that would be the kind of thing where we would say,
[1176.22 → 1180.24] there is a mismatch between the sentence and the recording that the training model would be
[1180.24 → 1184.76] confused by. And so, this is the kind of thing that we would want to filter out as
[1184.76 → 1188.94] not matching validation exactly. Does that about cover it, Josh?
[1189.54 → 1196.52] Yeah, I would say, actually, that it's not completely unorthodox. I think that,
[1196.78 → 1203.90] in reality, I think with speech technology and NLP, what's orthodox really just comes down to what the
[1203.90 → 1209.98] application is and what the constraints are of the project. So, there are some folks out there who
[1209.98 → 1219.10] would say, you know, the best corpus of speech for training speech-to-text models is conversational
[1219.10 → 1226.16] speech from humans that has then been transcribed. Common Voices is a red corpus. In the past, there have
[1226.16 → 1231.66] been red corpora that people have issues with, rightly so, because they're not seen as applicable
[1231.66 → 1239.82] to most projects' needs at inference time. So, for example, concrete, I'm talking about Litre Speech.
[1239.96 → 1250.60] Litre Speech is a corpus of mostly American English that was taken from, was formatted from open books that
[1250.60 → 1256.86] were recorded from Project Gutenberg. So, people who like to read books out loud for kind of the
[1256.86 → 1261.00] public, a lot of the consumers of these books might be people who are visually impaired.
[1261.28 → 1265.78] There's this giant project, people read books out loud. And then some researchers, I think mostly
[1265.78 → 1273.18] from Johns Hopkins, they took this set of audio, and they're not actually transcripts, it's the book,
[1273.56 → 1279.16] and they did some alignment. And they used that, and that kind of became a benchmark for doing speech
[1279.16 → 1284.98] recognition, especially for English. However, the way that people read books out loud, they try to
[1284.98 → 1288.82] read it in a very quiet room, they try to make sure that there's no echo, they try to make sure there's
[1288.82 → 1296.48] no dogs barking in the background. That kind of audio is not what most developers are expecting
[1296.48 → 1301.66] for their applications that use speech to text. It's better to have actually kind of messy audio.
[1302.02 → 1306.28] It's better to have cars honking in the background and wind blowing and dogs barking,
[1306.28 → 1314.04] because that's a lot of times what you actually get at runtime at inference. So, common voice is read
[1314.04 → 1321.74] speech. However, it's very valuable in the diversity of voices. It's just an enormous diversity of voices.
[1322.00 → 1326.38] And also the diversity of background noises, the diversity of acoustic environments.
[1326.80 → 1332.54] You have people who record common voice just for fun on their morning commute when they're on the train.
[1332.54 → 1340.86] That is really, really valuable data because it's so noisy. So, I think that people who might knock
[1340.86 → 1346.56] on common voice because it's read speech as opposed to conversational are also kind of, I mean, it's valid.
[1346.66 → 1351.84] People do speak differently when you're reading something out loud. That's linguistically proven.
[1352.14 → 1356.90] That's not really debatable. But the kind of noise you get in the background is just so valuable that
[1356.90 → 1360.28] common voice, I think, is going to be, if it's not already becoming,
[1360.28 → 1363.60] the benchmark for speech recognition for all sorts of languages.
[1363.60 → 1377.04] Hi, I'm Matt, and I'd love to tell you about Pace.dev.
[1377.50 → 1382.60] Pace.dev is a minimalist task management and async by default communication tool.
[1382.92 → 1385.20] Our screen recording feature is actually very popular.
[1385.64 → 1389.44] Wherever you can leave a comment, just like how easy it is to upload a file,
[1389.44 → 1395.30] you can record your window or the entire screen and upload it as a video to the team.
[1395.56 → 1399.26] Sometimes a screen recording is the perfect way to explain something.
[1399.60 → 1404.54] You know whether it's a bug that only happens for you or maybe more optimistically,
[1404.74 → 1407.10] a new feature that you can't wait to show off.
[1407.32 → 1411.22] And the showcase feature takes that a step further and lets you highlight progress,
[1411.54 → 1415.84] which is a much more positive experience than trying to make up estimations out of thin air.
[1415.84 → 1419.86] So please learn more and start your free trial at Pace.dev.
[1419.86 → 1439.24] So, Jenny, I'm curious, you know, while we're still on the topic of common voice,
[1439.34 → 1447.06] I was curious in terms of the playbook as you move into the future for expanding the set of languages
[1447.06 → 1452.80] that are available and maybe involving, you know, actively involving local language communities.
[1453.42 → 1459.84] What's the sort of playbook looking to the future for common voice in terms of expanding that
[1459.84 → 1463.70] and making sure you have, you know, more and more language communities getting involved?
[1464.42 → 1465.46] Yeah, thanks for the question.
[1465.76 → 1469.40] It's something that the common voice team spends a lot of time thinking about
[1469.40 → 1472.70] because, you know, as many languages as we share between us,
[1472.76 → 1475.64] we can't cover all the 7,000 languages in the world.
[1475.64 → 1482.10] And so what we really want to do is make common voice as self-serve as possible in terms of a platform
[1482.10 → 1486.46] for really any language community that wants to make use of it.
[1486.64 → 1492.88] And so the pipeline for getting a new language on common voice first starts with being localized.
[1493.48 → 1497.52] You know if the common voice website can't be used by speakers of a language
[1497.52 → 1501.78] because all the website copy is in English and that's not particularly useful.
[1501.78 → 1504.64] And at the same time that this localization is happening,
[1504.92 → 1510.00] the thing that we ask language communities to do is really find a corpus of sentences to be read.
[1510.50 → 1513.32] So our threshold for that is 5,000 sentences.
[1513.68 → 1517.14] That's kind of what we found sets a language community up for success,
[1517.14 → 1522.24] both in terms of having enough sentences to generate a sufficiently large corpus
[1522.24 → 1523.64] to start doing training work with,
[1523.78 → 1528.28] but also so that people who are coming to the site are not all just reading the same sentences
[1528.28 → 1529.24] over and over again.
[1529.82 → 1534.70] And these sentences can be from any source that the community thinks is appropriate
[1534.70 → 1537.58] as long as the licensing is open source.
[1537.68 → 1539.30] So as long as the licensing is CC0.
[1539.94 → 1542.32] And then once the site has been localized and translated,
[1542.32 → 1546.06] and once we have the sentences, 5,000 sentences available,
[1546.42 → 1550.94] then the language gets activated on the common voice site
[1550.94 → 1554.58] and people can just go and go start contributing.
[1554.58 → 1561.18] And so to that end, we've built several satellite tools for making that happen.
[1561.60 → 1563.24] There's a tool called Sentence Collector,
[1563.42 → 1566.78] which is primarily currently maintained by a community contributor, Michael Kohler.
[1567.08 → 1570.52] That is where anybody can go and just,
[1570.86 → 1574.54] if they want to, start typing in sentences to submit for a certain language,
[1574.88 → 1577.40] which will then also go through a community validation process
[1577.40 → 1581.86] to make sure the sentences are correct and appropriate and all of these things.
[1581.86 → 1588.72] We also have a tool that scrapes large open source text sources,
[1588.94 → 1593.56] such as Wikipedia, in order to, you know, automatically put together a corpus
[1593.56 → 1597.20] so that you don't have to come up with 5,000 sentences to read.
[1597.64 → 1602.68] A lot of our largest languages have been compiled by scraping Wikipedia
[1602.68 → 1607.02] and scraping open source encyclopedia type sources.
[1607.32 → 1608.04] I keep saying sources.
[1608.04 → 1613.06] But this could also include things like transcripts from the European Parliament
[1613.06 → 1618.06] or, you know, we're really very open to anything that the community deems
[1618.06 → 1621.70] will help them succeed is something that we're really interested in supporting.
[1622.42 → 1623.30] I appreciate that.
[1623.58 → 1625.32] Hey, Remy, I have a question for you.
[1625.84 → 1630.26] What can technologies like speech recognition enable, for lack of a better word,
[1630.34 → 1633.04] in local language communities in Africa and elsewhere?
[1633.04 → 1635.38] And what are the potential applications?
[1635.88 → 1640.30] And are they different from those that we're finding in places in the West,
[1640.38 → 1641.94] in the U.S. and in Europe and such?
[1642.42 → 1642.84] Yeah.
[1643.06 → 1647.10] I think voice, like voice, like voice technology can actually enable,
[1647.54 → 1652.10] like a unique opportunity to reach out to people who have, like,
[1652.22 → 1656.44] been excluded to the traditional, like to the traditional from digital services.
[1656.44 → 1663.70] And, yeah, I think some of the kind of application would be especially a fintech application
[1663.70 → 1665.38] and regarding healthcare.
[1665.84 → 1668.76] Just to give you an example.
[1669.54 → 1672.38] So two years ago, I was working at this startup,
[1672.54 → 1678.58] and we were actually building a product for people actually to contribute money
[1678.58 → 1680.04] into service groups.
[1680.04 → 1685.48] So those groups were formed, like, with 20 to 30 people.
[1686.22 → 1689.08] So most of those contributors were actually farmers.
[1689.90 → 1694.76] And looking at the literacy level, like, in population in Africa,
[1695.24 → 1702.20] so you actually see that 30% of adults in sub-Saharan Africa are actually illiterate.
[1702.20 → 1708.92] And so it was very, like, difficult for those people actually to use, like,
[1708.98 → 1710.18] this application to contribute.
[1710.96 → 1714.94] And so my thought was, like, if you would actually have, like,
[1715.10 → 1717.58] a Kenya Rwanda language model,
[1717.86 → 1720.56] Kenya Rwanda, which is actually a local language in Rwanda,
[1720.86 → 1723.84] spoken with over 12 million people.
[1723.84 → 1730.10] So this would have actually eased the way those formals contribute on their service group.
[1730.58 → 1730.72] Yeah.
[1730.72 → 1736.84] So there are also a lot of innovation happening, especially in Rwanda.
[1737.36 → 1740.60] Most of the government's offices are being digitalized.
[1741.52 → 1747.42] And so it's not very accessible, actually, by people, especially in rural areas,
[1747.90 → 1753.78] because someone would actually live 30, like, 10 to 30 kilometres from, actually,
[1754.78 → 1759.22] a cyber coffee, a cyber coffee, internet coffee,
[1759.22 → 1762.76] so where actually people go and seek, actually, for, like, services.
[1763.34 → 1767.14] And they always go look for agents.
[1767.54 → 1770.66] Agents, we actually have them actually seek those government services.
[1771.12 → 1774.66] So I think, yeah, voice technology can actually enable a lot of solutions,
[1775.22 → 1779.82] and helping, actually, farmers to actually access digital financial products.
[1779.82 → 1780.22] Yeah.
[1780.62 → 1780.98] Yeah.
[1781.10 → 1782.74] And that's fascinating.
[1783.00 → 1787.52] I wonder, as a follow-up to that, if, so, the language Kenya Rwanda,
[1788.08 → 1791.68] if people in maybe that language community and others,
[1791.80 → 1796.78] do you think that they would find more value in a sort of voice application
[1796.78 → 1800.78] versus a text application in the local language?
[1800.78 → 1803.44] What do you think provides the most value there?
[1804.20 → 1806.54] So, like, yeah, just giving you a context.
[1806.86 → 1809.80] So a lot of people, especially in urban areas,
[1809.92 → 1813.78] communicate, like, with voice over WhatsApp, like, using WhatsApp.
[1814.08 → 1819.08] So they tend to send more voice notes to, actually, people that are chatting with
[1819.08 → 1820.22] in the local language.
[1820.22 → 1825.54] And, yeah, people will actually prefer, actually, communicating through voice
[1825.54 → 1829.70] and, as well, like, seeking for information through voice.
[1829.90 → 1832.02] But just a quick example.
[1832.70 → 1835.54] So people will tend to call, especially call centres,
[1836.14 → 1838.50] like telecommunication call centres, actually, to seek information.
[1839.12 → 1842.38] So recently, we've actually had a crisis.
[1843.22 → 1846.30] There's this institution in Rwanda called RMBC.
[1846.66 → 1848.54] It's actually the Rwanda Biomedical Centre.
[1848.54 → 1852.08] So they've been actually receiving over 1,000 calls, like,
[1852.22 → 1856.98] respected in getting information through COVID, for the coronavirus.
[1857.74 → 1857.88] Yeah.
[1858.10 → 1862.04] And I think people will be seeking more value, like, with voice that actually testing.
[1862.50 → 1862.58] Yeah.
[1862.90 → 1863.70] Yeah, definitely.
[1863.96 → 1866.64] It seems like there's a lot of great potential there.
[1866.92 → 1869.30] And I know that, of course, one of the things, like,
[1869.32 → 1871.48] you were talking about some of the data that's available
[1871.48 → 1873.32] in the language you're working with.
[1873.84 → 1877.48] And I know, Josh, you've worked a little bit with,
[1877.48 → 1879.46] sort of, bias in data sets.
[1879.62 → 1884.46] And it seems like, of course, as data scarcity might be a problem with some of these,
[1884.46 → 1886.32] you know, lower resource languages,
[1886.32 → 1892.42] there's probably a heavy bias in those speech data sets for the lower resource languages
[1892.42 → 1894.78] towards, you know, whatever it is.
[1894.82 → 1897.36] Maybe it's only males in the corpus,
[1897.36 → 1902.78] or only a very small representation of the potential accents in the data.
[1902.78 → 1904.34] You've done some work in this area.
[1904.58 → 1909.88] I remember reading a recent blog post about a data set that you were working with
[1909.88 → 1914.16] to help researchers diagnose bias in speech data sets.
[1914.24 → 1917.94] Could you give us a little bit of an introduction to that work and what you're doing there?
[1918.52 → 1919.48] Yeah, I'd be happy to.
[1919.86 → 1922.96] I think that this question is a really important one.
[1922.96 → 1929.48] And it's one that anybody working in language technology needs to think about,
[1929.58 → 1933.22] needs to face, because whatever language technology you're working with,
[1933.44 → 1935.54] this bias problem is going to be present.
[1935.96 → 1939.74] So the work that you're referring to is the RD bias corpus.
[1940.16 → 1944.00] It's a corpus of English right now.
[1944.00 → 1950.96] It's a subset of the Mozilla common voice corpus that has been kind of filtered
[1950.96 → 1956.36] so that we have demographic data for every audio clip in the speech corpus.
[1956.52 → 1966.98] And also we've done extra steps of validation to really ensure that the transcripts are 100% accurate.
[1967.34 → 1972.32] So this data set is, it's about 1700 audio clips.
[1972.32 → 1978.62] So it's not enough for training, but it's enough for diagnosing, as we call it,
[1978.68 → 1982.22] diagnosing bias in your speech-to-text model.
[1982.48 → 1989.86] So this is, it's a hard problem to kind of get at when we talk about bias to make it really concrete.
[1990.10 → 1997.36] So the definition that we've basically come up with is if you have a speech-to-text model
[1997.36 → 2002.60] that performs statistically worse for a certain demographic group,
[2003.22 → 2005.54] then that model is said to be biased.
[2006.04 → 2012.34] So using this corpus, the RD bias corpus, you can take any off-the-shelf speech recognition model
[2012.34 → 2020.16] and look at what is its accuracy or word error rate, as we call it, for a certain demographic group.
[2020.16 → 2024.40] And we have information, thanks to Jenny and everybody at Common Voice,
[2024.72 → 2033.64] we have information from people who opted in to self-identify their gender, their accent, and their age.
[2034.30 → 2042.56] So yeah, along any of those lines, you can look at how well your model performs on every group versus every other group.
[2042.56 → 2045.60] And it does, the kind of beginning of your question was,
[2046.28 → 2051.46] this problem with more underserved language communities,
[2051.88 → 2055.72] this problem becomes more exaggerated.
[2056.18 → 2060.02] If you have a small sample from any distribution,
[2060.74 → 2066.74] the sample is more likely to be biased, especially if you're collecting it in a kind of biased way.
[2066.86 → 2069.92] So a lot of the language communities we have, they know about these problems,
[2069.92 → 2074.96] and they're working very hard, like Remy and the folks on the ground working at Digital Uganda,
[2075.52 → 2082.68] they have done a lot of work to make sure that the Kinyarwanda dataset is as balanced as possible.
[2082.68 → 2087.80] And they've done some really great things with that, especially for gender diversity.
[2088.26 → 2092.74] It's a hard problem because you want to get data that's balanced,
[2093.06 → 2098.34] but also you want to, you need to be mindful of people's privacy.
[2098.34 → 2104.94] So you don't always have people reporting their demographic status because it's an opt-in project.
[2105.48 → 2111.22] But even given that, Digital Uganda has been able to do some really great things through community recruiting
[2111.22 → 2114.72] to make sure that the corpus is as balanced as possible.
[2115.56 → 2115.68] Yeah.
[2115.82 → 2119.86] Remy, could you talk about that a little bit more in terms of, you know,
[2119.86 → 2127.82] your strategy around data collection and making sure you have this kind of balanced groups
[2127.82 → 2129.54] and involving the right people in the community?
[2130.28 → 2130.52] Yeah.
[2131.20 → 2137.96] So basically, Digital Uganda did actually an incredible job in actually collecting voice datasets.
[2137.96 → 2147.68] And so the strategy was more like hosting like offline events and bringing the awareness to actually contributors.
[2148.60 → 2154.64] Why is actually voice technology very important and especially for underserved languages?
[2155.64 → 2155.94] Yeah.
[2156.14 → 2157.56] They really did a perfect job.
[2157.82 → 2163.90] And so far we have on the platform over a thousand hours of voice collected.
[2163.90 → 2169.34] This is, I've been done by setting up actually a community of commanders.
[2169.88 → 2175.62] So commanders are actually members who actively like organize local events in their areas,
[2175.80 → 2179.94] in their universities, and in order to get people to contribute.
[2180.48 → 2185.50] I was just wondering if you could say this Digital Uganda, is that like a is it a company?
[2185.68 → 2186.60] Is it a for-profit?
[2186.80 → 2187.86] Is it a community thing?
[2188.04 → 2190.54] What, could you describe a little bit of what it is?
[2190.54 → 2197.50] So yeah, Digital Uganda is actually a company which actually work on AI products.
[2197.50 → 2208.16] And especially what they're trying to actually build is actually an AI voice, an AI chatbot in Kenya Rwanda.
[2208.60 → 2217.34] And the AI chatbot will be actually in charge of actually giving information related to COVID and also to other topics.
[2217.86 → 2223.88] So I've been facing the challenge of not having actually a Kenya Rwanda actually dataset.
[2223.88 → 2230.10] They actually started by actually collecting voice data on the common voice platform.
[2230.74 → 2235.24] And the next phase for them will be actually like working the datasets.
[2235.68 → 2242.96] And Josh has been like working on the Kenya Rwanda model, which they can actually now used to integrate with their chatbots.
[2243.90 → 2246.42] I think that's actually answered your question.
[2246.96 → 2247.70] Yeah, it does.
[2247.70 → 2266.04] And I'm kind of curious, kind of going back to what both you and Josh were saying before, really wondering, as you're looking at what impacts performance in terms of getting these recordings from different people, different groups, is it gender, you know, the sound of gender, accent, noise?
[2266.30 → 2269.84] What is it that really affects, you know, what the end product is?
[2270.10 → 2271.40] Josh, could you address that one?
[2271.78 → 2272.06] Yeah.
[2272.06 → 2274.64] This is a great question.
[2275.00 → 2282.32] What kind of demographic factors are going to have the biggest impact on performance for speech recognition systems?
[2282.92 → 2290.10] So I think accent and gender have been just hands down proven to have a huge effect.
[2290.44 → 2301.00] Accent, depending on what we classify as accents versus dialects versus languages, I'm sure Daniels has thoughts on this too.
[2301.00 → 2302.64] Language is a continuum, right?
[2303.06 → 2304.88] Everybody has a different definition.
[2306.52 → 2307.12] Yeah.
[2307.46 → 2307.72] Okay.
[2308.16 → 2318.12] Concrete example, try using Siri or Google Home with a Glaswegian accent or any kind of Scottish accent.
[2318.64 → 2319.88] It might be better now.
[2320.06 → 2324.86] I'm assuming they put more work into it, but pretty famously a few years ago, it was just abysmal.
[2324.86 → 2333.86] And so accent has a huge effect because I think the kind of continuum is so broad.
[2334.20 → 2342.48] And then after accent, gender has been shown to have a big effect, like a very reproducible bias.
[2342.92 → 2347.06] There are lots of different ways to think about why there's bias in a model.
[2347.06 → 2361.78] A lot of times the typical answer is, well, the training data set was not sampled correctly, that there are undersampled majorities, as it's been called, in the data set.
[2362.18 → 2365.22] And that, I think, for gender might be one of the big problems.
[2365.22 → 2377.68] And also on a kind of technical level, speech technologies were developed basically in a way that makes men's voices, because they're lower pitch.
[2377.80 → 2383.30] They have a different kind of frequency range to make it easier to work with those kinds of voices.
[2383.30 → 2389.96] So there's a sampling problem, and there also are problems that could be inherent to the technology itself.
[2391.00 → 2400.54] But at the end of the day, the demographic factors like accent and gender are usually much more pronounced than age.
[2400.60 → 2405.24] Age can also have an effect, but I've seen that less often.
[2413.30 → 2426.36] Changelog News is the best way to keep up with the fast-moving software world.
[2426.36 → 2434.72] We track, log, and contextualize the coolest projects, the best practices, and the biggest stories each and every week.
[2435.24 → 2442.84] Make changelog.com your daily destination, or hit the snooze button and subscribe to our weekly newsletter that hits inboxes on Sunday mornings.
[2443.30 → 2446.40] Join more than 15,000 enthusiastic readers.
[2446.66 → 2452.84] It'll cost you exactly zero dollars, and you can subscribe right now at changelog.com slash weekly.
[2462.36 → 2463.92] All right.
[2463.92 → 2476.36] So as we've gotten to talking a bit about the impacts of these demographic factors in terms of the performance of certain speech technology, like speech recognition,
[2476.36 → 2487.62] I want to kind of circle back and see, you know, to Common Voice and Jenny and ask, like, if this work that Josh has been doing in terms of the demographic factors,
[2487.62 → 2495.62] if that's sort of influencing thought on the Common Voice team in terms of if I may be mistaken about this,
[2495.62 → 2505.60] but I think, like, you have some processing that actually when you download a dataset, actually there's already a segmented out training test dev set.
[2505.60 → 2517.98] Is the work that Josh is doing or maybe other similar efforts, is that influencing your thought process around how you're forming those training datasets for people and segmenting out that data?
[2517.98 → 2527.46] Or maybe it's, you know, making some changes to the collection interface to promote certain diversity.
[2527.78 → 2530.76] What's the sort of feedback from this kind of work?
[2530.76 → 2539.58] Yeah, we work quite closely with Josh and rely a lot on his research and expertise in these matters to guide sort of our technical roadmap.
[2540.08 → 2548.28] So I think from, I would say from the inception of Common Voice until this year, we've really focused a lot on language diversity,
[2548.56 → 2552.76] with the idea that that was the thing that we could bring the most value to,
[2552.76 → 2566.62] especially around being able to mobilize Mozilla's international contributors and, you know, kind of counting on our reps and our local communities to do the kind of organizing that Remy was mentioning as well.
[2567.20 → 2572.08] And so now that we feel like we have a pretty good momentum going on the languages side,
[2572.08 → 2576.40] we're really starting to look more at the demographics inside a language.
[2576.74 → 2581.54] And gender is something that we are very cognizant of as something that we also need to correct.
[2581.54 → 2595.74] The kind of interesting thing about being pretty much the only voice data set out there that releases our demographic stats also means that we are very aware of all the ways in which we could be doing better.
[2596.48 → 2603.70] And so the ways we've thought about remedying that do definitely include the segmentation that you had mentioned.
[2604.00 → 2608.54] Right now, the segmentation optimizes for diversity of speakers,
[2608.54 → 2614.04] but there's certainly post-processing we can do there to, you know, try and optimize for gender as well.
[2614.20 → 2619.70] But some of the other things we are thinking about on the platform side include things like,
[2620.16 → 2627.34] we know open source in general tends to feel less accessible to underrepresented groups and looking at what campaigns we can do,
[2627.54 → 2630.50] what, you know, we could run challenges and events,
[2630.60 → 2637.90] specifically reaching out to underrepresented groups to make it very clear to them that we welcome and actively seek out their contributions.
[2637.90 → 2645.64] But also one of the other features that we haven't been building on the platform is the ability to collect data for a specific segment.
[2645.64 → 2653.54] So the thing that Josh had mentioned earlier on, you know, collecting a data set of just reading out the digits,
[2654.20 → 2658.44] one to 10, and, you know, the words yes and no,
[2658.54 → 2663.68] that's a very specific target segment that we can then, you know, go out into the world and say,
[2663.80 → 2667.66] hey, this is a thing that we want to collect for the specific purpose.
[2667.80 → 2668.58] Can you help us?
[2668.58 → 2675.78] And we're looking at how we can use that segmented campaign ability to then drive other diversity as well.
[2676.38 → 2680.86] I realize there's some good expertise with our guests on, you know,
[2680.88 → 2684.00] the ethical side and data governance side of things.
[2684.14 → 2689.14] And I wonder, like you had mentioned that only certain of the people that contribute to Common Voice,
[2689.28 → 2690.32] they self-identify.
[2690.32 → 2697.42] Of course, it seems like, you know, you could, if you wanted to, create some, you know,
[2697.70 → 2704.32] data augmentation method that would detect, you know, the accent or even the gender
[2704.32 → 2708.50] based on those who did self-identify to then label those who didn't.
[2709.04 → 2716.32] Has this come across your sort of ethical discussions in terms of what you do with people's speech that comes to you
[2716.32 → 2719.18] and what you don't and how you form those principles?
[2719.18 → 2722.64] So the Common Voice as a team, and I think Mozilla more broadly,
[2722.80 → 2726.90] really takes a data minimalist approach wherever possible.
[2727.32 → 2731.00] I personally am a strong believer that the only data you can, you know,
[2731.16 → 2734.88] guarantee to be secure is data you never collect in the first place.
[2734.96 → 2740.78] And so we, as much as possible, want to minimize what we are tracking on our contributors.
[2741.12 → 2742.34] You know, we respect you not track.
[2742.48 → 2746.36] We ensure that if people don't want to be identified, that they are not identified.
[2746.36 → 2750.18] This is also why we allow anonymous contributions to Common Voice.
[2750.92 → 2753.66] So that's kind of the first principles we're operating on.
[2753.66 → 2763.10] In terms of using augmentation methods to gather more information on those demographic pieces from people who are not self-identifying,
[2763.36 → 2769.56] I would say that any augmentation method that is available to us is in self also biased.
[2769.56 → 2780.26] And so I would be very concerned about introducing additional SKU if we're using identification methods that are trained on uneven data sets to then further segment our own data set.
[2780.62 → 2785.22] Right. You might just kind of be propagating a problem that is already there.
[2785.22 → 2786.30] Yeah, totally.
[2786.62 → 2788.18] There's something I'd like to tack on there.
[2788.30 → 2791.18] I definitely echo everything that Jenny said.
[2791.56 → 2803.98] And a little bit, I guess, further, let's say that we do have some kind of gender identification or age identification or accent identification that is 100% accurate.
[2803.98 → 2819.08] Even in that case, I would not want to be using that at all because the fact that this is an opt-in choice means that if the person didn't give you that data, they don't want you to have it.
[2819.18 → 2820.96] It's not that they just don't want to give it to you.
[2821.04 → 2822.64] It's that they don't want you to have it.
[2822.64 → 2828.36] So before I got into speech technology, I spent a lot of time working in kind of psychology labs.
[2828.74 → 2839.78] And if I had folks coming in and doing some kind of cognitive tests, and they have a sheet of paper, and they're filling out demographic information, and they choose not to fill out their gender.
[2840.64 → 2845.34] And then after they leave, I think, oh, well, I saw that she was a woman, so I'm just going to fill in a woman.
[2845.82 → 2848.96] That's something that would set off a lot of alarms.
[2848.96 → 2858.68] And I think that this kind of approach where you're filling in kind of holes in the data after the fact is the same thing.
[2858.86 → 2867.04] If when we're thinking about kind of the ethics of using machine learning models, I think it really helps to make it concrete.
[2867.04 → 2872.52] If you say, OK, if it weren't a machine doing that, if it were a human doing it, would that be OK?
[2873.08 → 2878.14] And I think in this scenario, it's something that I really do not feel comfortable with.
[2878.14 → 2880.42] Because the person doesn't want you to have the data.
[2881.16 → 2883.18] Right. Yeah. And I'm sure this is a problem.
[2883.30 → 2888.86] I think we're going to have a discussion pretty soon as well with one of the major image data set groups that's out there.
[2889.04 → 2898.92] And yeah, I mean, you could identify a lot of things and in images, or you could probably, you know, attempt to identify even people through speech.
[2898.92 → 2910.18] I think I remember when I downloaded some of the data from Common Voice, I had to agree as a user of that data to not try to identify the speakers.
[2910.78 → 2916.02] So I don't know if that's always been there, but I definitely resonate with what you both are saying for sure.
[2916.02 → 2919.28] So a question for Josh and Remy.
[2919.50 → 2927.40] As you were looking at the future of where your Mozilla fellowship can take you at this point, kind of what are you thinking?
[2927.58 → 2929.30] Where do you expect things to go?
[2929.42 → 2931.32] What would you like to get accomplished under that fellowship?
[2931.32 → 2953.00] So I think what I really want to accomplish is actually having making sure we have actually a strong Miranda model, which the local startup ecosystem can actually use and do actually relevant application for people who have been actually left out from the digital world.
[2953.00 → 2965.42] And yeah, I think that would be actually something perfect for me to accomplish as well as making sure like we have actually enough use case where we can actually use voice technology.
[2966.34 → 2967.44] Yeah, that's awesome.
[2967.44 → 2985.84] I really like how you put that because one of the things that really been privileged to sort of learn a little bit more and grow in as I've been doing my own work is just growing in my own desire to have sort of two-way communication in the digital world.
[2985.90 → 2995.24] So not so much that, you know, like we want to have, for example, machine translation models that translate everything that's in English to every other language.
[2995.24 → 3014.26] You know, it's really great to, you know, on the other hand, think about, well, there's so much value and amazing things happening in these language communities around the world, local language communities that we as high resource language speakers are missing out on.
[3014.42 → 3016.82] So that's really great and exciting stuff.
[3016.92 → 3017.64] What about you, Josh?
[3017.70 → 3019.96] What are your thoughts for the future of the fellowship?
[3019.96 → 3027.90] Yeah, so right now for the at least the duration of the fellowship, there are a couple projects that Remy and I are working on.
[3028.00 → 3047.32] There's the one that we've been talking about, the digital Uganda kind of base project that is focused on Kinyarwanda and collecting Kinyarwanda data, engagement, community kind of mobilization, and also model training for deployment and making a product that people actually can use and people care about.
[3047.32 → 3072.26] That's kind of, that's kind of, that's kind of, that's kind of a project that's kind of a project that's keyword spotting for broadcast radio so that folks in the Ministry of Health can know kind of more details on what's going on in the country in regard to coronavirus.
[3072.26 → 3079.38] Because the broadcast radio is a really well-used kind of media to get up-to-date information.
[3079.78 → 3084.52] So these two projects, they're both about data and models and community engagement.
[3085.16 → 3093.78] And right now, these are what's really driving and seeing these to some kind of useful product is the near future.
[3093.78 → 3110.20] But moving forward, what I'm really interested in is leaving a set of kind of best practices, guides, kind of playbooks for how to do all the things we're doing right now, but without me and Remy.
[3110.20 → 3125.92] If a new community wants to start using Common Voice, using Mozilla's Deep Speech, they want to start along this path that ends in a product, how do they do that without needing some kind of expert?
[3126.16 → 3135.64] Like, my hope is that we can make documentation and resources that are useful for developers everywhere so that they can do this at home.
[3135.64 → 3141.60] Common Voice is all about this democratization of data. Deep Speech is about democratization of tech.
[3142.10 → 3148.94] And I think that the work that we're doing right now is about this kind of democratization of expertise.
[3149.48 → 3156.68] Because for every project, you can't get somebody to help you out with voice tech. There's not a ton of us around.
[3157.06 → 3162.08] There's 7,000 languages in the world. And within each of those languages, there are lots of projects.
[3162.08 → 3165.98] And so to make this really open, we need to get the knowledge out there, too.
[3166.58 → 3173.16] So were you always wanting to, like, have products as the end goal here or developer tools that you could use?
[3173.28 → 3182.20] Or you seem to talk a lot about enabling other developers to build things through maybe a speech technology that you put out there.
[3182.26 → 3191.52] Was that always the goal? Or did you ever think about building sort of the end product, like the fintech application or the healthcare-related application directly?
[3191.52 → 3193.66] What's the balance there in your mind?
[3194.24 → 3202.78] So in my mind, these two projects we're working on, there's the Rwandan project and the Ugandan project for the fellowship.
[3203.22 → 3208.82] These are very, each, they're very product-focused or end goal kind of focused.
[3208.82 → 3226.94] But the kind of overarching context, at least for me, is these are two examples of taking an idea and speech and going through the entire pipeline with data collection, data validation, community engagement, making something that can be deployed.
[3227.06 → 3232.50] That whole pipeline for both of these projects is something that's reproducible.
[3232.50 → 3235.68] So it's kind of the answer to your question, I think, is both.
[3236.12 → 3245.12] These are both, in my mind first, important because each of these projects is kind of helping us hone the pipeline.
[3245.34 → 3249.78] And then once we have that honed pipeline, we can communicate that to a broader community.
[3249.78 → 3252.00] So, Jenny, I'm kind of curious.
[3252.32 → 3255.00] You're right at the centre of speech, data gathering, and governance.
[3255.32 → 3257.38] And I guess, are you hopeful?
[3257.88 → 3266.70] And what are your kind of thoughts toward the practicality of being able to expand speech tech to more and larger communities around the world over the next few years?
[3266.70 → 3272.38] And what are you excited about in terms of common voice or speech tech in general, actually?
[3273.38 → 3275.02] That's a very interesting question.
[3275.68 → 3281.56] For common voice, the thing that I – so I've only been with common voice for about a year.
[3281.86 → 3291.54] And in that time, the thing that I've been repeatedly blown away by is the enthusiasm and the dedication of our various communities.
[3291.54 → 3301.90] That says to me that there's really a need for something like this in the world, that common voice is filling a gap in both the marketplace and also just sort of the broader language community.
[3302.16 → 3306.96] You know, we've seen applications of common voice that we hadn't originally intended for.
[3307.06 → 3314.46] We were looking for it, using it to collect voice data for speech text models and those sorts of things.
[3314.66 → 3317.64] But we're also seeing that common voice is being used for language preservation.
[3317.64 → 3321.86] And I think there's potential applications for common voice for doing language acquisition even.
[3322.38 → 3337.56] The thing that I'm the most excited on is just how can we broaden the reach and the diversity of common voice so that people who have ideas that would have never occurred to us internally are empowered to use these tools as much as they can.
[3337.56 → 3346.88] And I think at the same time, because common voice is our collection methodology, as Josh said earlier, is very consent-minded, very privacy-minded.
[3347.64 → 3357.62] And I think there's a lot of opportunity to do leadership in the data governance space around how we think about data licensing for something like this.
[3358.30 → 3362.30] There's – I think to some extent, voice data is inherently biometric.
[3362.30 → 3366.70] You know if somebody downloads a common voice data set and goes, hey, I recognize my friend.
[3366.84 → 3375.02] There's no amount of obscuring or anonymization that we can do for that data set that would prevent that from happening.
[3375.02 → 3391.94] And so I think there are going to need to be some very difficult conversations in the next few years on how we handle that in such a way that, you know, it doesn't get abused, and it doesn't get used to create a deepfake or, you know, any number of nefarious and problematic applications.
[3391.94 → 3406.40] And I think being at the forefront of the governance question before things get to the point where they are now with Clearview AI, just to use an example, is a really powerful way that we can show up in the world.
[3407.34 → 3410.46] Awesome. Yeah, I think that's a great perspective to end with.
[3410.46 → 3426.26] And I just want to thank you all for taking time out of your really, really important work to talk to us about speech tech and data and bias in speech data and you're really exciting work for African languages.
[3426.82 → 3429.58] We're just really thrilled to have this conversation.
[3429.58 → 3441.44] Of course, in our show notes, we'll link to all the things that we've been talking about, about Common Voice and Digital Uganda and the fellowship program and all sorts of things.
[3441.82 → 3443.50] But thank you all for joining us.
[3443.58 → 3447.06] Really appreciate the conversation and hope to chat again soon.
[3447.28 → 3448.06] Thanks for having us.
[3448.30 → 3448.90] Thank you so much.
[3451.90 → 3457.22] Do you have questions, praise or constructive criticism about the conversation you just heard?
[3457.22 → 3462.54] Comment on this and every episode of Practical AI on changelog.com.
[3463.06 → 3468.68] Just open your show notes, follow to discuss on changelog news link and let your voice be heard.
[3470.72 → 3473.92] Practical AI is hosted by Daniel Whiten ack and Chris Benson.
[3474.42 → 3475.82] It's produced by Jared Santo.
[3476.14 → 3476.64] That's me.
[3476.90 → 3479.66] And our music is provided by the mysterious Break master Cylinder.
[3480.52 → 3482.74] We're brought to you by some amazing sponsors.
[3483.00 → 3485.46] Special thanks to Vastly, Linde and Rollbar.
[3485.46 → 3489.86] And a special shout out to those listening on our ad-free changelog++ feed.
[3490.36 → 3491.92] If that's you, you're awesome.
[3492.26 → 3494.38] If that's not you, well, you're awesome too.
[3494.66 → 3497.88] But you can learn all about it at changelog.com slash plus.
[3498.90 → 3499.94] That's all for now.
[3500.24 → 3501.62] We'll talk to you again next week.
[3501.62 → 3503.10] We'll see you soon.
[3503.12 → 3503.52] Bye.
[3503.60 → 3504.02] Bye.
[3504.90 → 3505.46] Bye.
[3509.32 → 3511.58] Bye.
[3518.04 → 3519.10] Bye.
[3519.16 → 3519.24] Bye.
[3519.30 → 3519.92] Bye.
[3520.16 → 3520.38] Bye.
[3521.18 → 3521.24] Bye.
[3521.50 → 3522.58] Bye.
[3522.58 → 3523.24] Bye.
[3523.70 → 3526.14] Bye.
[3526.26 → 3526.48] Bye.
[3526.68 → 3527.46] Bye.
[3527.46 → 3528.56] Bye.
[3529.16 → 3531.20] Bye.
