[0.00 → 6.10] It's interesting. I'll often be in meetings where I have a specialist in a particular thing
[6.10 → 11.02] and a bunch of different specialists, and they have a very particular lens that they're looking
[11.02 → 16.82] at things through. And usually my job is to be in the room, is to fuse all those things together
[16.82 → 23.98] and generate the big ideas from that fusion. That's where I think there is a lot of untapped
[23.98 → 29.66] magic out there in industry at large, where these different things you don't expect come together,
[29.66 → 35.88] and you combine them and go, wow, there are some amazing opportunities there. There needs to be
[35.88 → 41.50] a form of recognition academically for doing fusion of multiple discipline, I think. And I think that
[41.50 → 46.02] would be very valuable to motivate people to learn how to do fusion from multiple areas.
[46.02 → 62.50] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[62.50 → 67.54] and accessible to everyone. This is where conversations around AI, machine learning,
[67.54 → 74.56] and data science happen. Join us at practicalai.fm slash community and follow the show on Twitter.
[74.76 → 81.16] We're at practicalai.fm. Thank you to our partners at Vastly for shipping our pods superfast all
[81.16 → 94.16] around the world. Check them out at fastly.com. Welcome to another fully connected episode of the
[94.16 → 100.20] Practical AI podcast. This is where Chris and I keep you fully connected with everything that's
[100.20 → 106.30] happening in the AI community. We'll take some time to discuss the latest AI news, and we'll dig into
[106.30 → 112.18] learning resources to help you level up your machine learning game. My name is Daniel Whiten ack. I'm a
[112.18 → 118.68] data scientist at SIL International, and I'm joined as always by my co-host, Chris Benson, who is a
[118.68 → 121.76] tech strategist at Lockheed Martin. How are you doing, Chris?
[121.76 → 127.56] Doing fine. There's so much going on these days to talk about and been having deep thoughts about
[127.56 → 128.52] deep mind lately.
[129.14 → 131.42] Deep thoughts about deep mind.
[131.66 → 135.70] My name is not Jack Handy, though, for those in the audience old enough to remember that.
[136.88 → 145.24] Yeah. I mean, there seems to be a lot going on. And to be honest, we haven't talked about this for a
[145.24 → 153.46] while, Chris. How do you keep up with some of the things that are kind of coming across your path in
[153.46 → 160.62] terms of news related to AI and such? Like, where do you see that most? Does it come word of mouth?
[160.94 → 163.20] How does that work in your life these days?
[163.20 → 169.46] It's a little bit of everything. I have some kind of carefully sculpted Google News for different
[169.46 → 176.08] topics that I use as kind of my primary thing. But at work, we talk a lot about AI issues and stuff.
[176.26 → 181.74] And my immediate manager is actually perfect about it. I often hear things from him before I
[181.74 → 186.66] hear him from anywhere else because he stays right on top of stuff. Brent Siegel, in case he's listening.
[187.44 → 191.74] And having said that, just kind of all over the place, I think the harder thing now isn't where
[191.74 → 198.54] to get it. It's kind of how to keep the noise under control because there's so much coming out and
[198.54 → 203.36] across and trying to focus on the interesting things, or at least the things that are interesting
[203.36 → 206.34] to me and the people I work with. Yeah. How about you?
[206.34 → 213.54] Well, I see a good bit of the things that I see on Twitter, I think. I don't really hang out that
[213.54 → 220.56] much on LinkedIn or Facebook or other places. So Twitter is generally where I see things. I've
[220.56 → 228.50] noticed that my feed and Twitter has become increasingly NLP related, which is definitely
[228.50 → 235.46] my zone. So I noticed that recently, and I'm like, I need to kind of search for some more
[235.46 → 243.10] general sources of other things. Because I definitely think that there's a benefit in learning
[243.10 → 250.10] from a variety of even a variety of other disciplines, kind of what's happening and how
[250.10 → 253.12] innovation is happening. I'm getting way off-topic now.
[253.32 → 253.80] No, it's fine.
[253.80 → 262.96] Are there other disciplines outside of computer science and AI that you feel like have influenced
[262.96 → 265.96] some of your own thinking in certain areas?
[266.32 → 273.10] I am very kind of future application focused. Boy, I'll probably upset a lot of people. Things
[273.10 → 281.12] that I get bored with are just the next implementation of a fairly common AI paradigm and stuff like
[281.12 → 286.18] that. And I'm just like, oh, ho-hum. Okay. I've seen a lot of those. The things that I really like
[286.18 → 292.28] are when research comes out, some of the fascinating scientific papers come out, especially
[292.28 → 300.36] if they're very application focused. Because my job is to think about AI and data in the context
[300.36 → 307.22] of the industry that I'm in for 15, 20 years out. And so it's very, we do a lot of work with DARPA,
[307.42 → 315.34] you know, and so I'm very, very future focused. And so I really have a deep interest in finding
[315.34 → 321.64] people who are very forward-thinking and less about today's typical, you know, implementations
[321.64 → 327.70] that you see in a lot of commercial space and more about way out there. And so if anybody hears about
[327.70 → 334.94] things like that in the audience that I love talking and exploring things that are both
[334.94 → 341.46] practical as we are a practical AI, but also very aspirational in terms of where they might go.
[341.76 → 347.02] And that's where I spend a lot of time, but it's not strictly an AI. I've kind of come full circle
[347.02 → 351.90] going back to some of the things that we've talked about. You can't separate the AI from the software
[351.90 → 359.76] infrastructure around it and all the other data concerns. And so autonomy, robotics, a lot of these
[359.76 → 365.84] applications, but less what we're doing now and more where we're trying to get to is the area that
[365.84 → 373.44] I'm keenly interested in. And so hopefully, maybe if some of our listeners have some clues that they
[373.44 → 376.86] can point us toward that might make for some great episodes going forward.
[376.86 → 384.02] Yeah, I think this question was triggered in my mind. I mean, one of the, so I get some things off of
[384.02 → 393.08] Twitter, but also I, you know, I watch YouTube videos related to a number of things, including like, I have a
[393.08 → 403.20] set of channels that I like watching. I'm a fan of like, old time American music of like banjo and, and
[403.20 → 409.14] guitar and all that sort of stuff. So I like watching those sorts of videos. And so I watched a bunch of random
[409.14 → 417.42] things, but somehow I've sort of got gradually subscribed to generally like computer science and other types of
[417.42 → 423.34] videos that are out there. And I just watched one, I'll have to remember what, maybe get the link for our show notes,
[423.34 → 430.34] but it was talking about the importance of kind of getting exposed to various disciplines and how they can
[430.34 → 437.24] influence your, your own thought. Like the example was this guy, and he was generally considered in
[437.24 → 443.68] physics, but, you know, was making contributions in computer science as well. And his sort of knowledge
[443.68 → 450.54] of certain subjects in physics informed how he, like thought about algorithms and, and other things.
[450.54 → 456.60] And he made the point that increasingly, there's like a penalty for doing that in our society,
[456.60 → 464.28] like you, you advance more by being more focused, like in your area. And it's harder to like be
[464.28 → 470.68] recognized in other disciplines outside your area. And so it kind of, it's prohibitive for you
[470.68 → 476.92] to kind of enter into those zones and like to publish both in computer science journals and in physics
[476.92 → 481.10] journals, for example, but it's probably true in industry too, to operate in different zones, right?
[481.42 → 485.52] So you've really hit, you've probably just derailed everything we were going to do.
[485.52 → 487.50] Probably. So I'm good at that.
[487.78 → 494.04] I'll arrest it before it goes too far, but you're hitting on a great point. And that is the fact
[494.04 → 501.06] that the real magic for where you can do practical things going forward in an application sense,
[501.22 → 506.66] in all the cases I work in and see, it's at the intersection of multiple disciplines.
[507.14 → 513.44] It's interesting. I'll often be in meetings where I have a specialist in a particular thing
[513.44 → 518.48] and a bunch of different specialists, and they have a very particular lens that they're looking
[518.48 → 524.48] at things through. And usually my job is to be in the room is to fuse all those things together
[524.48 → 532.66] and generate the big ideas from that fusion. And that's where I think there is a lot of untapped
[532.66 → 538.68] magic out there in industry at large in the world is where these different things you don't expect
[538.68 → 544.86] come together, and you combine them and go, wow, there are some amazing opportunities there
[544.86 → 550.84] to dig into. And that's, that's really where I focus is trying to find those to mine those ideas
[550.84 → 556.84] and do that. And I think that that's not industry specific. I think that anyone out there can do that.
[557.00 → 563.30] But to your point to finish there is I'm often the only person in the room that doesn't have a PhD
[563.30 → 569.56] in something. And so there needs to be a form of recognition academically for doing fusion of
[569.56 → 574.58] multiple discipline. I think it's, it's not, it doesn't really exist today in that capacity.
[574.58 → 579.52] And I think that would be very valuable to motivate people to learn how to do fusion from multiple
[579.52 → 585.30] areas. Yeah. And I think, so one example I'm thinking of recently, we had, you know, this series
[585.30 → 593.28] of episodes on AI for Africa and the sort of discussion about AI applications and agriculture came up.
[593.28 → 601.56] multiple times. And I think it's just by the fact that the applications that they were talking about
[601.56 → 608.34] were not like what popped up immediately in my mind. And it was because they had sort of firsthand
[608.34 → 614.46] experience in the environment, maybe even like growing up in a sort of more agricultural rural
[614.46 → 623.22] setting where they participated in agricultural things. And so like being hands-on in a variety of areas
[623.22 → 629.96] can really spark, like you said, it's, it kind of unlocks where the real value is in a problem
[629.96 → 637.22] and prevents you from kind of building, building these solutions that might be interesting, but not
[637.22 → 644.24] valuable. Right. So I don't know, I don't have a huge desire to like to get into agriculture or gardening,
[644.24 → 651.12] but I think in like, in like my, my own work in NLP, there's like all of these different fields.
[651.12 → 654.86] I've noticed recently, like this has come up a lot. There's all of these different fields,
[654.86 → 661.74] like socko, sociolinguistics or like the more traditional forms of linguistics field kind of
[661.74 → 667.84] study. Like we, we recently interviewed Sarah Moeller about kind of field linguistics and being in the
[667.84 → 673.04] field and being with language communities. And there's so much wisdom to be gained from there.
[673.04 → 680.06] So even though I don't really have the right to like, or the qualifications, I guess you could say
[680.06 → 687.02] to operate in those areas and I should be careful. It's still behooving me to, I want to read more about
[687.02 → 692.94] those things. I want to kind of participate in those discussions and learn what I can to sort of
[692.94 → 697.92] influence my own thinking. But I think people, I don't know, there's a lot of people that maybe
[697.92 → 704.28] struggle with that confidence to operate in areas where they maybe don't have the qualifications to
[704.28 → 708.88] operate, or they feel like they don't have something to offer. Whereas like you said,
[708.92 → 714.60] it's really when you do kind of put forward ideas in a multidisciplinary environment where
[714.60 → 716.96] really valuable work happens.
[717.26 → 722.08] I think that's a form of, of imposter syndrome. You know, when you feel I'm not qualified and all that,
[722.16 → 727.32] I think, you know, you're only limited in this goes for everybody, everybody who's listening to this,
[727.32 → 731.48] you're only limited by what you're going to choose to go do and make the effort on and learn.
[732.14 → 737.56] And so it occurs to me from time to time, as I mentioned before, but not most days, I'll be like,
[737.70 → 743.60] I'm the only person without an advanced degree in here that's a specialist. And for me, it's because
[743.60 → 748.22] I wanted to do stuff and I wouldn't pursue it. And I know other people, including you,
[748.28 → 753.48] who've done that as well. I've seen you work outside, of, of your field and have insights and
[753.48 → 758.86] stuff. And I just encourage people. We're in a moment in history. A lot of people focus on the
[758.86 → 764.24] negatives because there are a lot of challenges in the world, but there's also more opportunity right
[764.24 → 769.90] now at advancing a number of fields than there's ever been before. And there's not enough people
[769.90 → 775.54] to do all those things. And so you're only limited by what you want to go do, convincing people to give
[775.54 → 782.04] you a chance. And so I hope that not too many people are letting a self-perception of not being
[782.04 → 785.32] qualified, get in the way, go get yourself qualified quickly.
[785.32 → 815.30] Well, Chris, I think I let us down the rabbit hole after you initially mentioned deep mind and
[815.30 → 819.74] maybe some things we've been seeing in the, in the news about deep mind. I'm assuming maybe
[819.74 → 823.68] you're mentioning that with reference to their NATO.
[824.18 → 826.56] Might be some big news there.
[826.82 → 833.58] Yeah. Yeah. So we should say that, you know, by no means we're, we're experts on, on all of this
[833.58 → 840.12] work that has been happening, but it is kind of worth, I think there is a, a trend here that's
[840.12 → 845.88] happening and, or a couple of trends that are intersecting this work by deep mind that we could
[845.88 → 853.30] comment on. But first it's the main thrust of this is it's a, a generalist agent. I'm constantly
[853.30 → 860.52] getting made fun of because I'm trying to come up with catchy acronyms and, but NATO is pretty good.
[860.52 → 870.24] A generalist agent. The idea here is that it's a single model that can operate in a multi-modal,
[870.68 → 880.04] multitask, multi embodiment generalization policy. So this is like multiple modes. So you've got like
[880.04 → 888.64] text video, you know, video game environment type of stuff, multitask, uh, related to like text
[888.64 → 895.16] based tasks or moving robot arms or all sorts of things. Basically. I think the reason this
[895.16 → 902.90] is getting a lot of attention is because it can do so such a diverse range of tasks from text and
[902.90 → 910.36] image based things to operating robot arms and that sort of thing. So I don't know what caught your
[910.36 → 915.04] attention about this, but that's sort of what I was seeing. It was that. And I, it's the fact,
[915.04 → 920.32] the thing that, and this is an area that I think you are much more expert in than I am. It's trying
[920.32 → 925.32] to do so many things, you know, going back. That was the thing that caught me when I first looked
[925.32 → 931.68] at it was multimodal, multitask, multi embodiment generalist policy, which I, I hear that in here
[931.68 → 937.02] kind of all things to all people and immediately wonder like, well, what can it do? What's this
[937.02 → 941.44] limitations? What are the practical? And they do have the video on the website, obviously that kind of
[941.44 → 947.36] shows a bunch of tasks lining up, but you know, how do you fit this in? If someone's looking
[947.36 → 952.72] at this, and we've been talking about all these big models with increasing capability over the last
[952.72 → 956.96] few years, well, how do you think about this when you're looking at it, when you read about that?
[957.16 → 962.14] And is it a jump forward? Is it just an iteration? How do you categorize in your mind?
[962.14 → 971.60] Well, I think that the one of the main things or main lines of inquiry that this model follows,
[971.60 → 978.78] that is true of other things that have happened recently is the relationships between this model and
[978.78 → 986.16] recent large language models. So recent large language models have approached the problem of
[986.16 → 995.04] sort of particularly the multitask problems. So in natural language processing, there's a variety of
[995.04 → 1002.84] tasks, right? You could have text as input and then detect like a label, like a sentiment label,
[1002.96 → 1009.48] neutral, positive, negative. You could have text as input and detect certain entities in the text.
[1009.48 → 1015.30] Like here's an organization, you know, that's mentioned, Lockheed Martin is mentioned here. It's an
[1015.30 → 1020.70] organization that's mentioned in the text. You could have text input in one language and text output in
[1020.70 → 1026.96] another language that's translation, right? You could have text input, and then you could parse out
[1026.96 → 1031.90] the semantic structure of the text. There are all sorts of things you can do with text. And these are all
[1031.90 → 1042.38] the tasks of natural language processing. And recently what has been the trend is that initially with
[1042.38 → 1050.84] language models, things were structured in terms of a kind of meta task where like maybe you would
[1050.84 → 1056.74] take out certain words from text and try to fill those in. And that would be the task you would train
[1056.74 → 1061.06] your language model on. And then you would kind of fine tune it downstream for various tasks.
[1061.06 → 1069.04] Recently, the trend has been to train language models on a variety of tasks by using what's called
[1069.04 → 1079.36] prompts. And prompts basically is a text input, but it's specifically formatted text input in the way of
[1079.36 → 1085.58] like there is a prompt that is structured in a certain way for question answering. There's a prompt that's
[1085.58 → 1090.56] structured in a certain way based on certain tags for machine translation. There's a prompt.
[1090.56 → 1098.56] So it's all sort of, it's not completely unstructured text input, I guess is one way to think about it.
[1098.80 → 1103.88] There's actually a prompt engineering or an engineering that goes into constructing this
[1103.88 → 1110.62] input data. But all of that's fed into the same model. And the model learns based on the context
[1110.62 → 1117.96] that's input, what action to take and what to output. So I see that, you know, obviously there's a big
[1117.96 → 1124.82] engineering and research step in this NATO model, but the spirit of it is very much in that same,
[1124.82 → 1132.84] same line of thought with the prompt engineering. So based on what the context that is input,
[1132.84 → 1141.14] it's determining actually what task to complete and what kind of format to output. So whether it's
[1141.14 → 1150.08] outputting, you know, captions of images or it's outputting actions for a robot arm to complete,
[1150.08 → 1157.14] it's based on that kind of formatting of the input text in the kind of contextual prompts,
[1157.14 → 1165.04] I guess, to help it know, help the same model know what tasks to do and what kind of things to output.
[1165.04 → 1172.28] How different is this in your mind? You know, it's transformer based for training, and it references
[1172.28 → 1178.26] that it's similar to other large language models. What are the differences that seem to be there on
[1178.26 → 1182.12] the surface, you know, without having dived deeply into it? Because I know you haven't had a chance yet.
[1182.54 → 1187.26] Can we think of it in the same kind of context as other large models in terms of framing it? Or,
[1187.40 → 1191.34] or do you think it's, have we kind of gone down a different branch is what I'm trying to get at.
[1191.34 → 1197.48] Yeah. I think that this is almost like the in some ways it's like the fulfillment of a lot of
[1197.48 → 1203.58] things that started with large language models. I mean, transformers, you know, were discovered and
[1203.58 → 1210.06] referenced to language, but they've, as it turns out, that sort of has been generalized across a lot
[1210.06 → 1216.58] of modes of, of data. So vision transformers and other things are really popular right now.
[1216.58 → 1222.70] And so I think that this is a natural thing that this sort of idea of prompt engineering and
[1222.70 → 1230.86] multitask sort of things has filtered in, it's sort of gone full circle to, to catch up to like all the
[1230.86 → 1236.14] data and all the types of prompts that we might want to, might want to include. So I think it,
[1236.34 → 1245.44] it is a really bold kind of step to kind of say, well, how far can we push this sort of idea and the
[1245.44 → 1250.88] things that are inspired by these large language models. And certainly there are a lot of modifications
[1250.88 → 1257.74] that need to happen in terms of like how sequences of things are tokenized and organized as input to
[1257.74 → 1265.68] the model. But I think a lot of the threads or, or the foundational blocks that this is built on are
[1265.68 → 1271.86] really kind of building on those things from large language models, which is, you know, really how science
[1271.86 → 1278.72] works, right. It took a lot of pieces. It took the, you know, prompt engineering pieces and the
[1278.72 → 1285.78] reinforcement learning and action type pieces and the transformers type pieces and the like
[1285.78 → 1292.20] computational engineering pieces all to sort of like follow their own paths and development to
[1292.20 → 1297.40] eventually combine into this thing. At least that would be how I would look at it, maybe.
[1297.60 → 1301.66] So the thing that I can't help wondering, I don't know if this is a tangent or if this is kind of on the
[1301.66 → 1307.50] main line of talk is if you keep extending this, this is where so much research is going. So much
[1307.50 → 1312.64] attention is going into the, the continued. No pun intended. Self-attention, maybe.
[1312.88 → 1319.92] Self-attention. Yeah. Yeah. Wasn't intending that, but you know, is this given the amount of effort
[1319.92 → 1326.58] that is going into this and the money and the resources, is this possibly, you know, using the
[1326.58 → 1332.28] words like generalist and using words like multimodal, multitask, possibly a path toward
[1332.42 → 1338.58] AGI in the sense of you're kind of combining all the things together to get to something
[1338.58 → 1345.00] that is, is more generalized that I kind of that that's always AGI, which is artificial generalized
[1345.00 → 1350.30] intelligence has always been fairly aspirational. You know, that kind of, that kind of Holy grail that
[1350.30 → 1356.52] we're moving toward, but this is where the focus, this is where the work is happening. So is there
[1356.52 → 1361.76] any, have you heard any speculation? I mean, is this where people think would be a productive
[1361.76 → 1367.56] pathway to get that way? Yeah. I mean, I guess it, I knew I threw you a curveball on that.
[1368.02 → 1374.12] Yeah. There's a whole variety of thoughts here. I think, I think one thing to note is like typically
[1374.12 → 1380.60] how things have happened is generally people have set a goal, like when we're able to do this with AI,
[1380.60 → 1385.86] then we'll call it intelligent or when we're able to do this, you know, and you sort of keep hitting
[1385.86 → 1391.20] those and then you, the goal line keeps moving out. There's certainly like, you could look at this
[1391.20 → 1396.18] model, and I'm sure that there'll be a variety of studies that come out that show how it's limited
[1396.18 → 1403.28] in certain ways and doesn't scale in the ways that we think it maybe could, but it's, you know,
[1403.28 → 1410.56] it's a stepping stone to a variety of, of, you know, paths forward. Yeah. I mean, as have all the
[1410.56 → 1414.84] models that we've talked about on the show in recent years as we've moved through them.
[1415.04 → 1422.08] Yeah. So I, I mean, I think it's certainly more general, definitely in terms of task and type of
[1422.08 → 1429.70] data. I think kind of circling back to what we started the conversation with today around like
[1429.70 → 1439.18] multidisciplinary things. I think that this is general in the sense of the AI tasks that AI researchers
[1439.18 → 1446.40] have defined over time, right? Like we've defined certain arbitrary tasks that are well-defined in
[1446.40 → 1453.28] terms of a computer and like, you know, like sentiment analysis is like a totally arbitrarily
[1453.28 → 1461.56] defined task for a, you know, it corresponds to reality in some way, right? Like we have a concept
[1461.56 → 1468.16] maybe of how it corresponds to reality, but it's not really like sentiment is so much more complex.
[1468.32 → 1474.38] Emotion is so much more complex than like positive, neutral, negative. Right. So I think that like,
[1474.76 → 1480.76] that's the way I look at it, I guess, is this is general in terms of the types of problems that AI
[1480.76 → 1488.24] researchers have dug into overtime, but that's only a very small amount of the complexity that's
[1488.24 → 1493.74] involved in the world, right? It's general in a sense that AI practitioners and researchers
[1493.74 → 1499.26] have kind of created the world in which we're developing this stuff. And so it's general to
[1499.26 → 1504.68] those set of tasks. Yeah. Yeah. It's, it's general to those set of tasks, and it's certainly more general
[1504.68 → 1514.04] than other things, but I think in relation to the complexity and subtlety of so many things in our
[1514.04 → 1520.86] world, you know, there's, there's still a lot of, you know, it's not like this is like covering all the
[1520.86 → 1527.62] general complexities of our, you know, universe. You realize that 20 years out, we're going to be on
[1527.62 → 1533.88] episode 5,000, and we're going to have long gray beards. And I'm going to say, is this the path to
[1533.88 → 1540.72] AGI, Daniel? Yeah. As we've iterated many times through there. That's probably true, Chris.
[1557.62 → 1570.66] Well, Chris, have you seen the new Top Gun? I have. Everyone but me has seen it in the last few days,
[1570.66 → 1577.50] I think. As we're recording this, this is the Wednesday after Memorial Day weekend, 2022.
[1578.14 → 1586.02] So it just came out, I believe this last Friday, five days ago. And I think I may be the only human
[1586.02 → 1591.54] being in metropolitan Atlanta who has not seen it, but no, I haven't seen it yet, but I've seen all
[1591.54 → 1598.84] the trailers. So maybe for, well, I don't know. I mean, Top Gun seems fairly internationally known,
[1598.84 → 1607.16] but for anyone that isn't aware, Top Gun is a, is a famous fighter pilot movie with Tom Cruise
[1607.16 → 1614.46] and a sequel just hit theatres or theatres and streaming. I'm not sure if it's on streaming.
[1614.46 → 1621.06] I don't think it is, but I could be wrong. Okay. Yeah. So again, you know, fighter pilot stuff,
[1621.22 → 1628.10] which is right up your alley, Chris, being a pilot. I picture you in this sort of Top Gun,
[1628.52 → 1633.40] yeah, Maverick scenes as you're flying your Cessna. I do have the fantasy when I'm flying,
[1633.48 → 1638.84] but yeah, not only am I a pilot, but I work at the largest aerospace company in the world that
[1638.84 → 1643.98] produces fighter planes, obviously. So it is up the alley. Yeah. Well, I mean,
[1643.98 → 1650.86] despite the, the general interest here, maybe there is a there is a point to why I brought this up,
[1650.86 → 1658.64] which is apparently that at least in one place. And I've, again, I haven't seen the movie,
[1658.76 → 1665.96] so I've yet to hear this, but Val Kilmer, who played one of the original characters in the movie,
[1665.96 → 1673.26] in the original movie, they had a scene where they needed his voice for something. And I'm not giving
[1673.26 → 1680.00] any spoilers, particularly because I haven't seen it and I can't, but apparently they used AI models to
[1680.00 → 1689.72] recreate Val Kilmer's voice because he is, you know, is, and has been undergoing throat cancer
[1689.72 → 1694.48] treatment, or I'm not sure if he's still undergoing it, but at least he's in a place where he cannot
[1694.48 → 1702.56] speak and has, has that sort of constraint. So they use the variety of AI models to reconstruct
[1702.56 → 1710.08] his voice and actually produce a voice for Val Kilmer in the Top Gun movie, which is quite interesting.
[1710.36 → 1712.22] What's your, what's your reaction to that?
[1712.42 → 1718.54] I think this is the first of this happening many times. I know that they, they used a lot of his old
[1718.54 → 1726.50] audio from movies to train the model. And not only that, but that the model is very specific
[1726.50 → 1735.00] to his style of talking. So it's not just generating the audio, it's generating audio the way a younger
[1735.00 → 1741.58] Val Kilmer before he was in this particular medical condition would have, would have addressed it. So
[1741.58 → 1747.46] it's, it's supposedly very much right on. And I think this fits in, you know, we've, we've had shows on
[1747.46 → 1753.38] deep fakes and, you know, on the visual side. And I think we're going to enter a time when AI to
[1753.38 → 1761.50] produce all sorts of audio video to consume and other, other medium will be pervasive. So we may
[1761.50 → 1768.26] look back at this and say that kind of kicked off a whole era of movie making. And I know that, of course,
[1768.26 → 1777.00] there's like video based things that have been done as well to like D age actors or like change
[1777.00 → 1784.72] physical appearance and that sort of thing. This one is, is quite interesting to me, especially if,
[1784.88 → 1789.70] you know if you think about like, we've been talking about multitask, multimodal things,
[1789.70 → 1794.20] and there's certainly things that can be done on the video side. There's, this is an example of
[1794.20 → 1801.74] something that can be done on the sound side, but it, you know, makes me think, well, like in the future,
[1801.74 → 1808.18] are they just going to keep having Val Kilmer act in movies with the voice that they've created for
[1808.18 → 1815.44] him and like, you know, a realistic avatar that they can create for him, you know, like what,
[1815.54 → 1821.14] what's stopping that sort of thing from being, you know, widespread, I guess.
[1821.42 → 1826.46] I don't think anything is stopping that. I think that there is, I'm going to reach out on something I
[1826.46 → 1830.74] know very little about and probably folks in the audience can, can educate us on this more,
[1830.90 → 1837.16] but I know that the band ABBA has a show that's been out there for a while where they use some
[1837.16 → 1842.18] sort of avatar. And I don't know the details of that. And I apologize. So it is a young ABBA back in
[1842.18 → 1848.22] their prime that are performing the show. And I'm that may, it probably has nothing to do with AI,
[1848.22 → 1857.50] but what I'm getting at is that idea of being able to, to use technology to present entertainment or,
[1857.66 → 1862.88] or other things outside of entertainment in the way that you would prefer, I think is here. And
[1862.88 → 1868.70] we're seeing that we saw, you know, whatever they happen to do for the ABBA show, we're seeing that
[1868.70 → 1874.98] with Val Kilmer. And we're also seeing the choices of not using technology and not using AI, not using CGI.
[1874.98 → 1881.56] And that going back to the Top Gun Maverick movie for the flying scenes, they decided not to use CGI.
[1881.96 → 1888.08] They could clearly have done a lot of the flying stuff with CGI, but they chose maybe for the last
[1888.08 → 1895.20] time ever to do something strictly without CGI in terms of the flight scenes. And yet they made the
[1895.20 → 1901.72] choice to bring Val Kilmer back into it with, uh, with the AI model. It's, it's interesting. AI models
[1901.72 → 1908.22] are becoming a tool of creative artists going forward in a and you have a whole palette of tools.
[1908.36 → 1910.86] So it's interesting to see how the choices are being made now.
[1910.86 → 1918.70] Yeah. I'm also wondering about the sort of rights related to this. Like, I don't know,
[1918.82 → 1923.88] you know, I don't know the details and I didn't see at least in the articles that I read,
[1923.88 → 1927.86] I didn't see a reference to this, although maybe it is public information. I'm not sure,
[1928.30 → 1934.30] but like, did they pay, like, what is the payment structure around like, well, Val Kilmer,
[1934.44 → 1941.28] we created your voice, right? You got paid for the previous things, right? And I, maybe the studio
[1941.28 → 1947.34] owns those audio clips and the video clips, and they created the voice out of those, right?
[1947.34 → 1954.12] So do they owe Val Kilmer any money for like, I mean, they're certainly representing his likeness
[1954.12 → 1955.74] and his voice, right?
[1955.82 → 1959.92] I do not know the answer. My guess would be yes, that they, they've compensated him.
[1960.06 → 1965.56] Yeah. I, I would sort of assume so, but it brings up the question in my mind, like, well,
[1965.82 → 1974.30] I assume so, but I don't know. And that sort of like makes me wonder, this is certainly a much,
[1974.30 → 1982.34] much lower level, but, you know, we now have 180 episodes or something paired with,
[1982.34 → 1990.92] with voice and, and text, you know, how would I sort of go about it? If someone recreated my voice
[1990.92 → 1998.12] and was posting things on YouTube, for example, it was clearly my voice. Maybe they had my name,
[1998.24 → 2002.90] maybe they had my name, maybe they didn't have my name, but it was sort of obvious what was going on.
[2002.90 → 2008.00] You know what would I do? I, I, I don't know how I would exactly respond.
[2008.58 → 2013.38] If you're thinking in particular, as I do in the industry, I'm in about nefarious intents.
[2013.58 → 2013.76] Yeah.
[2013.90 → 2016.54] You know, we've had many conversations about AI ethics.
[2016.78 → 2018.58] And sort of deep fakes and such.
[2019.04 → 2025.48] Absolutely. It certainly raises a lot of questions about the future and where this might go. As you
[2025.48 → 2029.94] were describing that, the thing that was in my head is I'm a big Gerard Tolkien fan and,
[2029.94 → 2035.78] and have all the books and I, you know, I'm not truly a super fan, but I'm bordering on it.
[2036.02 → 2041.22] And so, you know, that is an estate that's happened. And not only has he passed, but his
[2041.22 → 2048.74] son, Christopher passed. And, and I'm wondering, is that the future, if you have a very marketable
[2048.74 → 2055.86] personality or personality assets, like a voice, does everything become kind of an estate based
[2055.86 → 2062.36] path forward in terms of how you have those assets? Because it would not surprise me if we hear from
[2062.36 → 2068.06] Tom Cruise, you know, 50 years from now, when, when I'm expecting, he probably will not be alive at
[2068.06 → 2073.40] that point. Could be, he's very good at staying young, and he has the, the, the budget to keep
[2073.40 → 2079.96] himself young, but, but I'm assuming he won't be around in 50 years, but I will bet he will be on
[2079.96 → 2085.62] screen, even on new things. A little speculation there, but I don't know. The cruise estate may
[2085.62 → 2088.74] have a may have a few centuries left of bankable filming.
[2089.70 → 2096.16] Yeah, that's, that's true, I guess. Yeah. I mean, I, I guess this is probably true even for text in
[2096.16 → 2102.84] that if there's enough text from a certain, and I know there've been attempts to do this with varied
[2102.84 → 2109.20] levels of success, but like you have enough text from Shakespeare, right? You can write some new,
[2109.62 → 2115.44] you know, some new plays or, or whatever in the same style. And I know that that's, you know,
[2116.08 → 2120.80] kind of, there are some toys out there like that. And it's been kind of fiddled around with,
[2120.80 → 2126.72] with varied levels of success. But the idea I think would be similar as sort of whatever creative
[2126.72 → 2135.48] arts are out there, including music, you know, writing, movies, acting. It's just interesting
[2135.48 → 2143.22] to see this technology infiltrate all of those areas. We, you know, we've had obviously a lot on
[2143.22 → 2149.18] text generation. We've talked about on this show a lot. Furthermore, we've had even the, the show on,
[2149.18 → 2156.46] it may be a couple of shows now on how AI is influencing music creation and production.
[2156.88 → 2162.42] We've had, you know, we're now talking about movies and I think have talked about video at
[2162.42 → 2168.78] other points. So yeah, it's just sort of another example of how pervasive this technology is. And
[2168.78 → 2173.94] it's bringing up new sorts of questions that people haven't had to, to wrestle with yet.
[2174.22 → 2179.02] It was kind of, when we looked back and AI ethics was first coming about, there's a lot of people
[2179.02 → 2184.76] that rolled their eyes at the notion of AI ethics. And we were talking about it very early on because
[2184.76 → 2189.62] it matters a great deal to us. I know that in my personal conversations, I got a lot of pushback
[2189.62 → 2196.44] about it in a variety of venues. And so I think this points out this conversation that it's,
[2196.48 → 2201.54] it's not only crucially important to the present, but will be increasingly so for the future. And that
[2201.54 → 2207.22] intellectual property issues are going to not only be present, but change. The very nature of them
[2207.22 → 2213.32] will change going forward because we're moving into a world where we are, we in our AI will become
[2213.32 → 2217.72] inseparable. And I'm not saying that in a big, mushy aspirational way. I'm saying that we're
[2217.72 → 2223.44] having that now, you know, the child's toys, you know, being able to, whether the presence of a
[2223.44 → 2227.86] person, I'm using the word presence, whether that person is alive or dead, they're, they're still
[2227.86 → 2234.10] involved in, in those interactions. So that idea, the, the, the term we use in my industry is called
[2234.10 → 2240.14] mum tea, which is manned unmanned teaming, but in all industries and all aspects of life, manned
[2240.14 → 2245.10] unmanned teaming will be present. You will be interacting with your AI and just about everything.
[2245.10 → 2250.72] So maybe there's somebody listening out there that will, uh, that will kind of take us to the next
[2250.72 → 2254.92] level on some of these issues. Because we, we're going to need some help to navigate this.
[2255.30 → 2261.54] Yeah, for sure. We need the that creativity. We need multidisciplinary thinking, all those things
[2261.54 → 2268.14] that we've talked about in this, in this episode. And that brings us to a sort of natural way to a
[2268.14 → 2275.42] learning resource that, that I was going to bring up in this fully connected episode, which is talk
[2275.42 → 2281.72] and, and set of, you know, linked tools from the TensorFlow team, which I ran across recently, which
[2281.72 → 2289.18] is around the responsible AI and machine learning type of things. So, um, this includes, you know,
[2289.18 → 2295.16] lessons learned from the TensorFlow and Google teams around these things, but also some relevant
[2295.16 → 2301.92] tooling around, you know, creating things like model cards and data set cards, even Merv from
[2301.92 → 2307.72] hugging face brought this up in our, in our last, one of our last episodes about model cards and, uh,
[2308.08 → 2314.74] maybe even, uh, integrating some of that tooling with, with Keras, but this is more of a sort of in
[2314.74 → 2320.46] that vein from the TensorFlow team. And so if you're thinking about this sort of responsible AI and ML
[2320.46 → 2328.10] things and want it maybe more from the developer perspective and less from the sort of philosophy
[2328.10 → 2336.34] and kind of social science perspective, um, this seems like maybe a good, you know, a good, uh, starting
[2336.34 → 2342.50] place, not covering everything maybe, but a good starting place. So I'll link that, um, that video and,
[2342.50 → 2347.74] and set up tools in our, in our show notes. So people can, can go check it out.
[2348.12 → 2352.76] That sounds good. I'll finish up by saying you, I'm kind of creeped out by the idea that we have
[2352.76 → 2357.66] all that audio out there a little bit. I started thinking, Oh my gosh, that's think about that.
[2357.66 → 2363.18] All of our listeners will now be learning about responsible AI and machine learning practices. So
[2363.18 → 2365.40] maybe we're good there.
[2365.68 → 2369.66] I hope, I hope we're good. We're asking, we're asking the audience to save us from this.
[2369.66 → 2374.98] Yeah. Yeah, for sure. Well, uh, yeah, it's been, it's been fun, Chris. Appreciate, uh,
[2374.98 → 2379.50] catching up with you and look forward to talking in our next episode.
[2379.72 → 2380.58] Sounds good, Daniel.
[2380.58 → 2395.60] All right. That is practical AI for this week. If this is your first time listening, subscribe now
[2395.60 → 2401.64] at practical AI.fm or just search for practical AI in your favourite podcast app. We're in there.
[2401.76 → 2406.60] And if you're a long time listener, please do share the show with your friends. It is the best way you
[2406.60 → 2412.26] can help practical AI succeed. Thanks again to Vastly for shipping our shows superfast all around the
[2412.26 → 2417.46] world to Break master Cylinder for the Beats and to you for listening. We appreciate you. That's all
[2417.46 → 2419.32] for this week. We'll talk to you again next time.
