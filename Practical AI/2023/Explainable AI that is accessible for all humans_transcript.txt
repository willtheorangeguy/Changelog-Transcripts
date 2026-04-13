[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[42.52 --> 45.52]  Welcome to another episode of Practical AI.
[45.86 --> 47.22]  This is Daniel Whitenack.
[47.34 --> 52.52]  I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[52.52 --> 55.02]  Benson, who is a tech strategist at Lockheed Martin.
[55.28 --> 56.24]  How are you doing, Chris?
[56.24 --> 57.12]  Doing well.
[57.18 --> 58.06]  How are you today, Daniel?
[58.38 --> 60.58]  Oh, man, so much better than last week.
[60.74 --> 66.50]  As you know, I was sick last week when we were supposed to record, so sorry for the skip of
[66.50 --> 75.22]  the week, but I'm happy to be back here and with a super relevant topic around AI systems
[75.22 --> 79.22]  and explainability, the delivery of AI systems that are explainable.
[79.56 --> 84.22]  We have with us today Beth Rudden, who is CEO at Bast AI.
[84.54 --> 85.14]  Welcome, Beth.
[85.14 --> 86.46]  Thank you for having me.
[86.70 --> 87.60]  Yeah, yeah.
[87.78 --> 93.48]  We were just talking before the show about this craziness that we're experiencing around
[93.48 --> 99.40]  the hype of these AI systems, which maybe are just like a web page that connects to open
[99.40 --> 99.74]  AI.
[99.74 --> 107.36]  But you were talking about how you've been thinking for quite a while about explainability and
[107.36 --> 109.76]  accountability of AI systems.
[109.76 --> 114.32]  I'm wondering if maybe you could start out by just giving us a little bit about the journey
[114.32 --> 118.18]  you took to landing in that space.
[118.18 --> 121.44]  How did you get interested in those topics specifically?
[122.14 --> 127.88]  I think that a really good place to start is understanding 2012.
[128.52 --> 132.56]  The Harvard Business Review said that the data scientist would be the sexiest job of the
[132.56 --> 133.44]  21st century.
[134.06 --> 134.40]  Yes.
[134.40 --> 138.86]  Which is why some of us on the call are data scientists.
[138.86 --> 145.24]  So I was working at IBM and I was a pleaser.
[145.24 --> 149.24]  So I went after the information architect certification.
[149.24 --> 160.54]  But I had a couple of friends that were mathematicians and statisticians and really data engineers and DevOps people and software engineers.
[161.04 --> 164.12]  And they didn't really want to be an information architect.
[164.12 --> 165.70]  They didn't want to be an IT architect.
[165.70 --> 181.76]  So we rinsed and repeated experiential certification to be able to say, well, how can we make sure that we're making data scientists that actually know how to use data in the scientific method to solve business problems?
[182.18 --> 186.14]  And so we started that and it took us about six, seven years.
[186.24 --> 187.60]  It's accredited through Open Group.
[187.76 --> 188.72]  Anybody can get it.
[188.72 --> 206.34]  And it's hard because you actually have to submit, like, you know, depending on your level one, two or three, you have to submit a, you know, several projects that say, you know, here's how I took my problem and put it into a hypothesis that could be tested.
[207.34 --> 211.00]  And then here's how I negotiated with my business stakeholder.
[211.00 --> 214.06]  And then here's how I, like, you know, showed my results.
[214.06 --> 220.06]  And then, you know, as you get further and further along, here's how I integrated my model into production.
[220.38 --> 225.18]  And I think that's when things get a little crazy and people are like, wait, what?
[225.30 --> 226.22]  How do I do that?
[226.34 --> 227.56]  You know, here's my Jupyter notebook.
[227.64 --> 228.30]  Isn't that great?
[228.78 --> 240.34]  But I've been writing or, you know, looking at how to deliver AI, but I've been doing a lot more on the linguistics or the semantic side and for probably about 15, 20 years.
[240.34 --> 251.60]  And if you look at, you know, how the NLP work is really, you know, a lot of people are like, oh, hey, I pulled down this thing from Spacey.
[251.68 --> 252.98]  I can write NLP, right?
[253.06 --> 257.84]  You know, I just call this, like, cosine similarity kind of, you know, model.
[258.02 --> 258.92]  I'm good to go.
[259.50 --> 263.58]  And I was an archaeologist in, you know, the late 90s.
[263.70 --> 265.26]  That's what I actually got my degree in.
[265.34 --> 268.46]  I did Greek and Latin and spent some time in Italy.
[268.46 --> 281.18]  And when you're learning languages, you know, you're learning declensions and you're learning, you know, etymology and you're learning stemming and laminatization and tokenization and, you know, all of the text preprocessing.
[281.38 --> 284.30]  So I was always the squishy human data scientist.
[284.58 --> 287.42]  I was the one that was studying languages and doing semantics.
[287.42 --> 300.48]  So I think it was 2015, Andrew Ng's like, oh, hey, if we use GPUs or graphical processing units, we can process all this structured data, like, really, really fast against these statistical models.
[300.48 --> 309.30]  And so a lot of people, I think, forgot about entity extraction and, you know, ontologies and the semantic web.
[309.72 --> 314.16]  And, you know, I use the OWL, which are formal knowledge graphs.
[314.16 --> 322.74]  And I hopefully am not speaking Greek to a lot of people, but really looking at the language side as opposed to the machine learning side.
[323.50 --> 331.96]  And that understanding of semantics is like it's really put me in a great position now because all of the statistical models.
[332.92 --> 334.10]  NLP has three.
[334.38 --> 336.08]  I kind of chunk them into three things.
[336.26 --> 337.88]  NLU, natural language understanding.
[338.26 --> 340.64]  NLC, which is classification, which is your prediction.
[340.94 --> 343.34]  And then NLG, which is your generation.
[344.32 --> 350.82]  And prior to having access to GPT, we were generating language old school.
[351.64 --> 353.00]  And it's super hard.
[353.26 --> 354.50]  I mean, it's really, really hard.
[354.62 --> 361.90]  Like if you think of like pronouns and, you know, trying to say, you know, John was the guy, you know, who referred to him.
[361.90 --> 365.72]  And then he took the notch or the wrench from Joe, et cetera, et cetera.
[365.84 --> 367.50]  I mean, just it's so complicated.
[367.50 --> 377.88]  But now that we have a really good natural language generator, I'm like kicking butt because I have the semantic side.
[377.88 --> 384.82]  So I have really, really high NLU or natural language understanding because how an ontology works.
[384.82 --> 387.44]  And I try to remind people of this.
[387.66 --> 392.98]  An ontology is the study of the nature of your reality based on the language that you use.
[393.28 --> 397.46]  So when you use language, I'm understanding your reality.
[397.46 --> 405.20]  And so I map that into a knowledge graph and then take that language to understand whatever you're going to say against it.
[405.28 --> 406.12]  So I have a map.
[406.12 --> 430.60]  So when the natural language generator generates all the variation that I need in order to put into my machine learning models, and then I have a map to make sure that I understand what kind of things you actually want to talk about, I can create conversational AI that has lineage and provenance, that has the source of where you're starting from.
[430.60 --> 441.08]  And then I use all of the GPT generators to effectively generate the fluff or the syntax around whatever entities that I extract about whatever you want to talk about.
[441.46 --> 447.00]  If you guys could help me break that down into better English, that's what I've been trying to do for the last couple months.
[447.68 --> 448.20]  That's awesome.
[448.20 --> 464.66]  I would love to, so one reference point in my ontology of this space is people sort of talking, and we even talked about this in our last episode with Brian McCann from you.com about grounding, right?
[464.66 --> 480.06]  Like some people are thinking about, okay, like I can generate text or a response to a user query by looking at some external knowledge and grounding my response in that sort of context.
[480.30 --> 481.98]  How would you compare it?
[481.98 --> 491.72]  So like one way you could do that is to say, okay, I'm going to go, I'm going to pull an article and like insert a paragraph from that article in a prompt, a natural language prompt to a language model.
[491.72 --> 496.44]  And that's the way I'm inserting knowledge into like my response.
[496.44 --> 502.64]  Here you have this sort of concept of a knowledge graph and entities and like ontology.
[502.84 --> 514.10]  Would you consider that grounding or is it slightly different in terms of like what you're talking about with this ontology and kind of bringing that external knowledge into the generation?
[514.28 --> 518.68]  You know, the nice thing about software is it's multidirectional.
[518.68 --> 524.86]  So how the conversational AI, the product in just a quote here.
[525.02 --> 528.58]  So we named our company or I named my company Bast AI.
[528.96 --> 533.86]  It is after the Egyptian cat goddess and we build conversational AI technology.
[534.08 --> 535.00]  So we build cats.
[535.26 --> 536.20]  Ah, nice.
[536.26 --> 538.52]  And we really wanted to distinguish from bots.
[538.82 --> 545.22]  And, you know, having the word cat makes a lot of sense, at least in my mind, because I've been, you know, overriding the bot.
[545.22 --> 550.28]  But the idea is that the conversational AI technology includes a data pipeline.
[550.98 --> 552.74]  So bring your own data.
[553.12 --> 556.12]  Let me take a book that you have written.
[556.72 --> 564.36]  And then the cat through the data pipeline ingests that book and then puts the entities into the ontology.
[564.36 --> 568.12]  And that can be done both supervised and unsupervised.
[568.32 --> 570.30]  I am a big proponent.
[570.72 --> 576.14]  And I hope we can get into this a little bit of AI is is to augment human beings.
[576.14 --> 578.94]  It's really to help us understand.
[579.30 --> 583.60]  And I'm always like, why can't we carry a pocket brain like we carry a pocket GPS?
[583.60 --> 583.88]  Yes.
[584.54 --> 590.48]  So the cat ingests the book and then those entities go into the knowledge graph.
[590.56 --> 595.16]  And then that those entities are in a concept hierarchy and they carry.
[595.16 --> 598.94]  Well, it was from this paragraph on this page in the book.
[598.94 --> 606.58]  So that carries the actual provenance of where that entity was and the understanding of that entity within the concept hierarchy.
[606.58 --> 617.70]  Then when the cat, you are interacting with the cat with the conversational interface, the cat will be able to respond using those entities.
[618.42 --> 622.70]  And so it will show you where it got its response from.
[623.34 --> 629.34]  And so it's predicting the response based on your question because I have that high degree of NLU.
[629.34 --> 637.24]  So I take your question and I do text preprocessing and I match it against the entities in that ontology.
[637.62 --> 646.42]  Or if it's not in that ontology, we have a series of orchestration to send it to a couple of various different places that we had to create.
[647.16 --> 657.10]  The way that we handle toxicity is something that I'd love to talk about, too, just because I think the way that we're handling that is very, very elegant and fun.
[657.10 --> 662.66]  And the idea is that we wanted to have fully explainable AI.
[663.14 --> 679.66]  We wanted to show people how they could ingest a paragraph and then be able to communicate with the conversational or communicate with the AI to understand how that paragraph is being understood in the relation of what the person is asking for.
[679.66 --> 694.38]  Yeah. And maybe just to give an example of this, I love the way that you frame this in terms of like reaching out to ontology that's hierarchical and you can kind of ground citations in that as well.
[694.52 --> 699.54]  So like just to give an example, let's say that I had a book.
[699.54 --> 702.62]  Maybe it's a novel I'm reading right now.
[702.98 --> 706.66]  I don't know if you ever read it, The Cuckoo's Egg by Cliff Stoll.
[706.80 --> 712.40]  It's about like a hacker at the Lawrence Berkeley Labs way back in the day.
[712.44 --> 713.20]  It was really interesting.
[713.36 --> 717.44]  Anyway, like let's say I have that book and I put it through this data pipeline.
[717.64 --> 725.74]  So I've got my ontology and I've forgotten like, oh, did Cliff like reach out to the NSA or was it the CIA when he was talking?
[725.74 --> 730.60]  And I asked the question, you know, did Cliff reach out to the CIA or the NSA?
[731.16 --> 732.72]  What would happen next in that?
[732.80 --> 743.44]  Like how would how would that query, the processing of that query differ in that example as compared to maybe like other types of ways of handling this?
[744.00 --> 754.36]  So instead, I mean, in that case, we would have, you know, the direct path where we could say, OK, well, Cliff is a character in the book and it was the CIA, not the NSA.
[754.36 --> 757.80]  So I know that for a fact in the ontology.
[758.28 --> 762.32]  So then, you know, I could do it two ways where I could answer you directly.
[762.72 --> 766.10]  And we I don't know if you call it cheating a little bit, but we have a corpus.
[766.32 --> 773.42]  So anything that's answerable that is really, really easy answerable, we stick into open search, which is just a form of elastic search.
[773.84 --> 776.56]  So then we just pull that, give you the answer.
[776.74 --> 780.00]  We know with 100 percent certainty that it was a CIA done.
[780.00 --> 787.36]  And all of these scores, we have about 50 ish different models, depending if you how you count them.
[787.44 --> 790.08]  That is run through our orchestration system.
[790.48 --> 792.80]  So each one of those models have scores.
[792.92 --> 794.42]  You have targets, configurability.
[794.68 --> 797.40]  You can expose different hyperparameters, et cetera, et cetera.
[797.40 --> 811.62]  Or we could take the Cliff entity and the CIA and the NSA and we could do prompt engineering and we can give you like if you wanted to say, give me Cliff's reply and tell me was it the CIA or the NSA?
[812.18 --> 816.48]  And then you could go like, you know, ask it to generate a response for you.
[816.48 --> 822.26]  And one of the things that we're really playing around with is conversations should be interactive.
[822.74 --> 825.86]  So we want the cat to also engage the person.
[826.34 --> 833.80]  So we could say, oh, Cliff was part of the CIA and you wanted me to generate like a response that Cliff would give.
[833.92 --> 834.64]  Here you go.
[835.14 --> 836.98]  And what else would you like me to do?
[837.06 --> 841.34]  Would you like me to generate like some books that Cliff would have written in the style of Cliff?
[841.34 --> 846.06]  So, you know, you can kind of really start to do that engagement, too.
[846.94 --> 851.80]  And, you know, I use the word lineage and provenance, but it's really attribution.
[852.38 --> 859.26]  And when you're starting to attribute things to the right to the right source system, everything changes.
[859.62 --> 868.78]  And anytime I like, you know, show some of the cats to people, one of their first responses is like, let me put my own data in it.
[868.78 --> 877.16]  And that's exactly what I want to instigate with humans is not having the black box algorithm do the answering.
[877.50 --> 880.70]  Just have the black box algorithm do the generating.
[881.30 --> 886.64]  And I know that a lot of people are super excited about using them.
[887.16 --> 898.64]  I would really caution about creating them because with the generative AI, it's just going to generate based on syntax, not based on understanding.
[898.78 --> 903.50]  And I think that that's like the biggest thing that I want people to hear.
[904.50 --> 905.52]  There's no sentient.
[905.74 --> 906.54]  There's no sapience.
[906.66 --> 907.42]  There's no consciousness.
[907.42 --> 914.22]  And I think that that's all a distraction for the amount of compute that these models really take.
[914.66 --> 919.64]  So I'm like, can we make it like a utility and everybody uses it sort of like a dictionary?
[919.72 --> 922.94]  And then, you know, we're good to go or like a thesaurus.
[922.94 --> 923.02]  Yes.
[924.86 --> 938.74]  And I just I really do think that when you're using the generative transformer to generate transformations, that's the big difference that I'm trying to get people to see is like with the ontology as the map.
[938.74 --> 951.62]  And actually, GPT gave me this analogy, and it's very good at analogies and metaphors because of how it's built and, you know, clustering and all of the things that happen behind the scenes.
[951.62 --> 966.62]  So when you're using an ontology with our conversational AI or with our cats and you own a toy store, if you want to ask that cat about any toy in your toy store, you'll have that ontology to tell you about any toy in your toy store.
[967.08 --> 972.12]  If you ask the cat about a toy that's not in your toy store, it will tell you it's not in your toy store.
[972.46 --> 976.38]  If you do the same thing to chat GPT, it's going to tell you about a toy that doesn't exist.
[976.38 --> 991.10]  So, Beth, that was a fantastic explanation, and I'm learning a lot.
[991.32 --> 994.08]  Daniel is quite the expert in this area himself, but I'm not.
[994.66 --> 1001.84]  But you, as we were coming into the break, you made a point that has been weighing on me for the last moment or two as you were finishing up.
[1001.84 --> 1021.72]  And that was, as you are a user and you're interacting with this capability, remarkable capability that's really taken all of our attention this year, you pointed out that it's really important for that user not to infer intelligence, not to infer a consciousness in that.
[1022.10 --> 1030.72]  I would argue that that, for the typical user out there, someone who's not in the AI space and doesn't have an understanding of these, that's a really hard ask.
[1030.72 --> 1044.82]  And I'm definitely, you know, with this year, with GPT Everything chat, GPT-4 has been out this last week as we're recording this, and I'm talking to a lot of people, and I think they're really struggling with that.
[1045.02 --> 1049.26]  So, you kind of gave that direction, but I think that's easy for us.
[1049.42 --> 1051.86]  I think that's a tall order for people not in the space.
[1051.86 --> 1056.78]  And a lot of people, a lot of our audience are people kind of coming into this and learning about it.
[1057.30 --> 1068.30]  Can you provide some guidance in how you keep that separate and what it means and how you should use this new capability as people are now engaging?
[1068.40 --> 1072.06]  Because it's changing the way we're all, you know, operating day to day.
[1072.06 --> 1077.64]  Even non-technical people who have never really done any AI are now going to chat GPT and things.
[1077.80 --> 1085.96]  And we're really at a moment where people need to understand how to appropriately engage this brand new technology.
[1086.56 --> 1088.62]  I think that it's a combination of things.
[1088.96 --> 1096.04]  But, you know, I think that TLDR, go out and use it and use it as much as possible and ask it about yourself.
[1096.16 --> 1097.82]  Ask it about things that you know.
[1097.82 --> 1106.58]  And, you know, the way to really understand how something works and, you know, remember we're in the realm of cognitive science.
[1106.58 --> 1110.50]  That binds philosophy, psychology, and computer science.
[1110.96 --> 1119.78]  And I think that really when you understand that it is a generative transformer, it generates transformations.
[1120.48 --> 1127.38]  It does not have the understanding to have consciousness or sentience.
[1127.38 --> 1129.54]  It doesn't understand what you're saying.
[1129.82 --> 1132.12]  It's a stochastic parrot.
[1132.34 --> 1134.22]  It mimics language.
[1134.60 --> 1140.44]  So it mimics what you're saying based on the syntactical rules of that language.
[1140.44 --> 1146.98]  And it's incredibly good because it's been fed a huge amount of data.
[1146.98 --> 1151.90]  So if I'm having a conversation at work with somebody who's not a technologist.
[1152.30 --> 1152.50]  Sure.
[1152.62 --> 1154.98]  They might be in a marketing department or something like that.
[1155.56 --> 1160.96]  How does that change how they're engaging in terms of how they should be thinking about it?
[1161.20 --> 1165.80]  Because I would argue that that's a tall order to actually get.
[1165.90 --> 1167.56]  You can say that to someone and they'll say.
[1168.02 --> 1168.16]  Right.
[1168.32 --> 1168.56]  Yeah.
[1168.58 --> 1171.96]  Ask it about a product that you are not selling, that you're not marketing.
[1171.96 --> 1183.10]  You know, ask it about something you know and you know to be true and ask it to say, you know, I would like you to market a blue tomato.
[1183.52 --> 1184.90]  We have blue tomatoes.
[1185.02 --> 1186.64]  Blue tomatoes grow on trees.
[1186.76 --> 1188.00]  Could you market that for me?
[1188.46 --> 1191.58]  And it will give you marketing for blue tomatoes that grow on trees.
[1192.30 --> 1197.92]  And so I really want people to come from a space of abundance, not scarcity.
[1197.92 --> 1207.26]  I really want people to think about what do they have right now and what every human being has is their own experience.
[1208.04 --> 1218.70]  And what this AI has been trained on is a very small number of people's experience who have been on the Internet and been writing on the Internet.
[1218.70 --> 1226.36]  And so my opinion is that every single human being is already impacted by AI.
[1226.66 --> 1236.68]  They should be using it and they should be using it in a way that, you know, I used it to help my daughter come up with an analogy on reciprocals.
[1236.82 --> 1243.74]  I asked it to come up with a good metaphor in order to explain, you know, what an ontology does.
[1243.74 --> 1248.02]  You know, there's so many different things that you can use it for.
[1248.16 --> 1261.52]  And I really think that the best way that people can do is go out and use it and ask it about things that, you know, many authors are like, oh, so I wrote 10 books, not four.
[1261.72 --> 1261.92]  Ha!
[1262.34 --> 1269.96]  You know, I mean, people are starting to see that it's going to generate the next proper noun, the next predicate,
[1269.96 --> 1279.66]  the next syntactically correct, and I'm, you know, doing it in a sentence, but it's so smart because it has been fed so much data.
[1280.46 --> 1281.70]  But here's a myth.
[1282.16 --> 1291.04]  You know, I talked a lot technically about using ontologies and knowledge graphs and concept hierarchies and, you know, all these things.
[1291.04 --> 1293.08]  But here you go.
[1293.32 --> 1299.22]  All of what I just talked about can run on something that was like the very first iPhone 1.
[1299.58 --> 1305.90]  The myth, you do not need big data and big honking machines to create AI.
[1306.62 --> 1309.32]  And I would ask, who does that myth serve?
[1309.32 --> 1325.46]  And if everyone could understand how to use the data that they have that is special to them, that they understand, that they, like, if you take your grandfather's journals and put them into an AI so that you can have a conversation with your grandfather,
[1326.36 --> 1329.60]  this is what the technology is enabling us to do.
[1329.96 --> 1337.36]  And we want it to be distributed to every human on Earth because every human on Earth is being impacted by AI.
[1337.36 --> 1341.00]  Yeah, and I don't know if you can talk at all.
[1341.16 --> 1353.32]  One of the things, I love how you brought out this element of people being able to bring their own data to the table kind of combined with the fact of them being able to run this maybe even on their own hardware.
[1353.48 --> 1354.48]  How shocking would that be?
[1355.48 --> 1367.34]  And I love that also because, like, I think that there's a real concern that I've been having over time of just how Western and English focused most of this conversation.
[1367.36 --> 1368.98]  Conversational AI is.
[1369.36 --> 1382.28]  And the fact is that, like, we come to the NLP table with these biases that say, like, oh, wouldn't it be great if every language community in the world had a translated version of Wikipedia?
[1382.28 --> 1384.46]  And that concept makes sense to us.
[1384.58 --> 1388.04]  But the reality is some language communities, they don't want that.
[1388.04 --> 1390.50]  It's explicitly not how they use their language.
[1390.50 --> 1397.88]  And they want to use their language in a community setting, maybe for storytelling or maybe for, like, whatever it is.
[1397.88 --> 1401.86]  And they would rather bring a different kind of data to the table.
[1402.00 --> 1405.58]  So I think that that also helps in this regard.
[1405.58 --> 1419.54]  I don't know if you've also seen, like, in the ontology space or the knowledge graph space, how do you think about, like, I guess bias and, like, the availability of data?
[1419.62 --> 1422.34]  Because that's a big topic with these large language models, right?
[1422.42 --> 1428.66]  Is, like, if you're just using them for generation, they come loaded with what they're trained with, right?
[1428.66 --> 1436.32]  You know, I was stunned at how quickly the models are able to statistically generate the language.
[1436.62 --> 1443.62]  And, you know, just we used to make fun of, like, you know, natural language processing, statistically generating language.
[1443.62 --> 1447.52]  Like, you know, it's abhorrent in some – it's such an oxymoron in so many ways.
[1448.04 --> 1455.58]  There's actually a really great article by Karen Hale about the Maori people and what they are doing with artificial intelligence.
[1455.58 --> 1463.48]  And I'd love to link that just because it was from MIT and it was a fantastic review and really speaks to what you were saying about that.
[1464.12 --> 1469.56]  As far as bias, again, I'm going to go back to cognitive science.
[1469.90 --> 1472.22]  You know, philosophy, how do you know what you know?
[1473.56 --> 1478.44]  Psychology, how do you make sure that you are not using your powers to manipulate humans?
[1478.80 --> 1481.32]  Seriously, like, just put some ethics there.
[1481.70 --> 1483.36]  And then computer science.
[1483.36 --> 1493.32]  So when you're talking about bias and, you know, there's a cognitive codex and it's like 188 cognitive biases and counting.
[1494.40 --> 1503.16]  And one of the best ways that I did this when I was still in IBM is I started the Trustworthy AI Center of Excellence.
[1503.72 --> 1509.66]  And many of my peers are still – they're so strong and what they're doing is amazing.
[1509.66 --> 1514.76]  But what I wanted to do with bias is we did some modeling on the Titanic.
[1515.68 --> 1527.78]  And we did some predictions on whether somebody was going to live or die based on their class in order to show the social bias of the time because the person in steerage would never have gotten a life of it.
[1527.78 --> 1532.02]  And I use that explicitly to talk about bias.
[1532.36 --> 1542.68]  And what you said about the very small – you didn't use the word homogeneous, but like Western kind of culture that we're sort of codifying into this AI.
[1543.26 --> 1545.84]  We have got to have a wider variance.
[1546.02 --> 1547.70]  We have got to have more diversity.
[1547.70 --> 1558.92]  And that's why we really need to be able to give everyone the ability to build their own without having to build their own generative model.
[1559.44 --> 1561.34]  Can you talk a little bit about like how to do that?
[1561.38 --> 1565.66]  Because this is a topic that we've talked about in different ways over a number of episodes.
[1566.06 --> 1568.40]  It's very hard to get it out there.
[1568.48 --> 1570.98]  It is definitely not an equal world.
[1571.28 --> 1571.64]  That's right.
[1571.76 --> 1572.10]  Access.
[1572.60 --> 1572.90]  Yeah.
[1572.90 --> 1577.40]  Can you talk a little bit about Access and how you create that and how that becomes possible?
[1578.16 --> 1582.00]  Well, shameless plug, I'm looking for funding and investment.
[1583.06 --> 1594.98]  But, you know, I think that the ability to use the combination of like knowledge graphs and semantics and, you know, being able to access these generative models.
[1594.98 --> 1608.24]  And one of the things that I did with the orchestration and the reason that I use sort of the corpus driven and dump a bunch of stuff into OpenSearch is to make it small enough and accessible by as many people as possible.
[1608.56 --> 1614.12]  So just use the access to the generation to generate all the variance that you need.
[1614.20 --> 1615.42]  But eventually you're done.
[1615.58 --> 1617.26]  You don't need any more.
[1617.54 --> 1622.76]  And you have that stored in a corpus so you can access that as much as you want.
[1622.76 --> 1633.26]  And so it's really about like how do we use the generative AI more as a utility that everybody uses instead of creating.
[1633.54 --> 1645.54]  I call them cheese graters because that's how I think of the generative model is they cheese grate the text and then they sort of glue it back together or stitch it back together with duct tape or, you know, whatever.
[1645.54 --> 1653.16]  But I mean, it's codifying so much of our Western notion of ideas.
[1653.62 --> 1659.70]  If you go to Aboriginal societies, their construct of time is entirely different.
[1660.04 --> 1664.68]  Like if you're facing the West or the North or the East, their concept of time is different.
[1664.92 --> 1667.10]  And that's expressive in their language.
[1667.10 --> 1677.46]  So to think that we have created a generative model that can encompass all of our world is not correct.
[1677.58 --> 1680.66]  We can do so much more if we have a wide variant.
[1681.26 --> 1686.36]  Have you guys heard of the diversity prediction theorem or the wisdom of the crowd?
[1686.84 --> 1687.28]  Yeah.
[1687.60 --> 1689.74]  To me, it's the secret of the universe.
[1689.74 --> 1702.00]  Like the wider your variance, the more standard your mean, like the closer to truth that we want to get to, the more diverse human neocortexes that we need to get there.
[1702.32 --> 1712.08]  So I'm a big proponent of, you know, to really answer your question, Chris, we need to make the generative model something that is is accessible.
[1712.08 --> 1718.12]  And OpenAI has done a really great job of like making it accessible to a wide range of people.
[1718.66 --> 1724.60]  But I was talking to, you know, my parents today and they were like, we don't even know how to access that.
[1724.70 --> 1729.88]  But I think I went to Google and it might have done something because it gave me a weird response.
[1729.88 --> 1732.78]  So I shut it down and then I tried to go to the other thing.
[1732.88 --> 1733.90]  I was like, oh, good.
[1733.90 --> 1743.66]  So we need to be better about really making sure that people understand that they are accessing just a generative model.
[1743.90 --> 1744.44]  That's it.
[1744.56 --> 1750.48]  I think that's one of the one of the challenges I see is we're here in this AI community.
[1750.74 --> 1753.96]  You know, we're a tiny little slice of that in this episode as we talk.
[1754.66 --> 1759.74]  But at the same time, I participate in other communities that are not technical at all.
[1759.74 --> 1762.96]  And the other participants in those communities are not technical.
[1762.96 --> 1771.66]  And I think that's the challenge is trying to do exactly what you said with people who otherwise not just don't have access, don't even know it exists in a lot of cases.
[1772.04 --> 1772.44]  Yeah.
[1772.66 --> 1780.08]  I used to say and a friend of mine reminded me of this a long time ago, but there's no hand waving in math.
[1780.08 --> 1796.80]  So if somebody is not explaining how they got to the prediction or how the model works or saying it's proprietary or shoving a bunch of data into a neural net to have it guess the features, you know, engineering, they're probably hitting the easy button.
[1797.22 --> 1798.70]  They're not doing the work.
[1798.70 --> 1805.46]  And I come by that, honestly, because I think that people need to understand there's no hand waving in math.
[1805.76 --> 1811.44]  We need to stop thinking that just because it's AI or just because it's statistics.
[1812.50 --> 1814.10]  You've heard the Mark Twain quote.
[1814.74 --> 1815.78]  Is it a statistics quote?
[1816.04 --> 1817.32]  I probably should have.
[1817.82 --> 1819.54]  Lies, damn lies and statistics.
[1819.54 --> 1820.70]  Yeah, that's right.
[1820.94 --> 1821.22]  Yes.
[1821.58 --> 1821.90]  Yes.
[1822.20 --> 1829.42]  So it's just statistically 2013-ish, 10 years ago.
[1829.70 --> 1829.94]  Goodness.
[1830.18 --> 1842.58]  Jennifer Goldblatt, social scientist, gets on the TED stage, tells the world that she can statistically predict whether you have done drugs or not based on five of your likes on Facebook.
[1843.22 --> 1844.80]  And I was like, hallelujah.
[1845.36 --> 1846.32]  Everybody understands.
[1846.78 --> 1847.94]  Everybody sees it, right?
[1847.94 --> 1854.72]  Everybody understands that, like, we can now predict these things statistically if we have enough data.
[1855.60 --> 1859.98]  And no, I still don't think that people can get that.
[1860.14 --> 1861.44]  And we need to teach.
[1862.06 --> 1865.16]  Like, I taught my kids probability through poker.
[1865.66 --> 1876.44]  Like, we can teach this to people so that they understand that it's only statistically accurate to a certain probability.
[1876.44 --> 1882.40]  So if it's 97% accurate, what does 3% look like?
[1882.78 --> 1885.46]  What's your test reliability for that 3%?
[1886.06 --> 1891.00]  Is that 3% going to give you that same answer every single time?
[1891.22 --> 1893.94]  And if not, it's not science.
[1893.94 --> 1896.72]  I love so much about this conversation.
[1896.72 --> 1905.80]  And one of the things that I was thinking about in my own context is, like, my own tendency to not give users enough credit.
[1905.80 --> 1921.40]  So, like, one of the things that happens when, like, we anthropomorphize AI and, like, talk about it in these different ways is, you know, there's a tendency to, like, maybe think it's always right or it has more, like, you're talking about more intelligence than it really does have.
[1921.40 --> 1929.16]  But I've also found where it's, whether it's, like, family members in my own life who aren't involved in the AI world and they're using chat GPT.
[1929.36 --> 1941.72]  A lot of times they interact with it more responsibly, I feel, than some colleagues in the AI world in the sense that, like, my brother-in-law, Jack, I don't know if you're listening.
[1941.72 --> 1955.24]  Hey, if out there, like, he, we were talking last night over tacos and he had, like, used chat GPT to write up some, like, speech or something that he was giving at work.
[1955.36 --> 1957.98]  And I'm like, oh, so you, like, wrote that with chat GPT?
[1958.14 --> 1964.16]  And he's like, yeah, like, I used it, but I, what I do is I don't, like, just have it generate it for me.
[1964.20 --> 1969.76]  I'll just, like, type as fast as I can and just have it rephrase it into something good that's grammatically correct.
[1969.76 --> 1972.90]  And I'm like, wow, that's, like, yeah, go for it.
[1972.94 --> 1973.70]  That's really good.
[1973.96 --> 1976.40]  Like, that's awesome because, like, that's a great way.
[1976.48 --> 1981.18]  Or, like, I'm thinking of teams that we work with in India in my day job.
[1981.24 --> 1992.40]  I was talking to someone and, like, some people would say, like, oh, we can't, like, just output machine translations because, like, they won't post-edit them and, like, make them good or, like, look for corrections.
[1992.62 --> 1998.08]  And, in fact, like, you know, translation teams we're working with in India, they know it's a machine translation.
[1998.08 --> 2003.42]  They're just happy they don't have to type as much because typing is really difficult in their language, right?
[2003.50 --> 2004.96]  Like, they're fine to post-edit it.
[2005.36 --> 2009.06]  So, yeah, I'm wondering if you've seen this as well.
[2009.18 --> 2019.04]  And, like, if you have any recommendations specifically after working with users in conversational interfaces, which can seem kind of, like, human-like.
[2019.04 --> 2020.80]  Like, it's like you're having a conversation.
[2021.38 --> 2022.56]  How do you set up an interface?
[2022.86 --> 2031.82]  How do you set up a system such that it, like, produces useful behavior and, like, promotes the right type of usage?
[2032.38 --> 2035.72]  You know, I started playing with very earlier versions of GPT.
[2036.20 --> 2037.78]  And so we strung them up in Slack.
[2038.04 --> 2044.04]  And we did that on purpose because we didn't want to deal with identity access management and all the other stuff.
[2044.04 --> 2046.38]  And Slack's a great interface for plugging things in.
[2047.22 --> 2051.92]  But it's also really something that, you know, I was the anthropologist.
[2052.22 --> 2059.40]  And when we installed Slack in the largest enterprise in IBM, I watched, you know, the people going, oh, my gosh, what's the protocol?
[2060.10 --> 2064.72]  And really when you deal with, like, really senior executives, they're like, wait, this is persistent.
[2064.94 --> 2066.18]  This is kept forever.
[2066.56 --> 2067.58]  You know, what are we doing?
[2067.58 --> 2069.08]  How do I respond to this gift?
[2069.08 --> 2070.96]  That's right.
[2071.04 --> 2071.40]  That's right.
[2071.94 --> 2080.70]  And so, like, you know, I had a lot of what you would call training in trying to get people to understand this new modality of communication.
[2081.50 --> 2085.54]  So we were playing around with the bots and we wanted the bots to talk to each other.
[2086.08 --> 2091.60]  And so we use the cats now to test out what we're doing.
[2091.60 --> 2100.14]  And, you know, we talked a little bit earlier about, like, setting up an iframe or a web page that just, like, you know, strung up to open AI and you can ask it any question you want.
[2100.96 --> 2108.46]  But if that AI doesn't give the answer that you like and it causes your customer to not trust you, that's a big deal.
[2109.04 --> 2111.76]  So you really want it to be tested.
[2111.76 --> 2125.98]  And so we use the we use the cats to test the cats or the cats to make kittens or the cats to test the kittens or the cats to test the intents or, you know, and this is the joy of having some of this automated.
[2125.98 --> 2140.46]  And when we were, you know, back in the day when you used to do, like, conversational AI and that you would do, like, you know, either dialogue flow or corpus driven, it was always the IT group that had to do, like, give me a hundred variations of how somebody would say this.
[2140.78 --> 2143.12]  Give me a thousand variations of how somebody would say that.
[2143.24 --> 2145.06]  Give me 16 synonyms for this.
[2145.18 --> 2146.88]  Give me 17 synonyms for that.
[2147.32 --> 2153.02]  So we're using it all the time because, again, it's great at generating variations.
[2153.02 --> 2164.28]  One of the ways that I used it with teachers and students and I get to work with this amazing university, Maryville University, that is truly transforming education.
[2164.68 --> 2171.04]  And they're doing such amazing things with my friend Phil Comarny, who used to be SVP of innovation at Salesforce.
[2171.76 --> 2173.26]  We're doing great things there.
[2173.74 --> 2179.86]  And I got to do a fantastic workshop with all of the teachers and the faculty.
[2179.86 --> 2183.94]  And they came to my session really kind of skeptical.
[2184.52 --> 2188.70]  And they left my session going, oh, my gosh, I now understand how to use this.
[2189.20 --> 2195.08]  And what I did is I had ChatGPT list out 50 things that a teacher does all day.
[2195.46 --> 2199.84]  And then I had ChatGPT list out 50 things that a student does all day.
[2200.34 --> 2202.42]  And then I had the teachers and the students.
[2202.42 --> 2208.06]  I had 138 people on a Miro board working together for 15 minutes.
[2208.24 --> 2209.92]  And I'm like, what are you going to eliminate?
[2210.34 --> 2211.72]  What are you going to raise up?
[2211.78 --> 2212.48]  What are you going to reduce?
[2212.56 --> 2213.48]  And what are you going to create?
[2214.24 --> 2218.90]  And so give people an understanding of what the technology does.
[2219.16 --> 2225.60]  And then the messy middle between the skills that you have and the title or the role that you have.
[2225.96 --> 2227.32]  It's what do you do all day?
[2227.52 --> 2229.26]  Like, what do people do all day?
[2229.26 --> 2231.66]  I'm like, Richard's scary, 1968.
[2232.38 --> 2235.14]  But like when you're doing that, you're like, wait a second.
[2235.60 --> 2236.18]  I don't.
[2236.58 --> 2243.72]  And gosh, when I was a mom or like a mom of younger kids, I guess I'm still a mom, even though my child is 18 or one of them is.
[2243.90 --> 2244.54]  Anyway, I digress.
[2245.00 --> 2248.24]  Like I would sit there and I'm like, oh, my gosh, my head is hurting.
[2248.36 --> 2249.34]  What do I do for dinner?
[2249.62 --> 2250.38]  ChatGPT.
[2250.50 --> 2252.12]  Give me a recipe with chicken and broccoli.
[2252.12 --> 2264.02]  You know, like it can be so useful for so many people to just generate what the idea needs, especially when you're tired or you're exhausted.
[2264.02 --> 2268.88]  Or I definitely wouldn't want to fire your entire marketing team.
[2268.88 --> 2279.22]  But, you know, because you want to keep it on like on cue, but you really can use it to really augment your business and augment what you're doing.
[2279.50 --> 2282.84]  Just keep it in the realm of fiction and creativity.
[2283.40 --> 2283.58]  Yeah.
[2283.68 --> 2285.18]  You know, those kind of things.
[2285.18 --> 2293.30]  And we haven't even talked about, you know, some of the some of the art and the creative expression.
[2293.30 --> 2298.54]  And then I'm a huge fan of like, you know, especially for people who don't code.
[2298.70 --> 2306.14]  I'm like, go ahead, program in it, like get it to render some code for like a graph is so that you can see like a visualization.
[2306.56 --> 2309.56]  And code's great because it kind of works or not.
[2310.56 --> 2311.08]  True.
[2311.08 --> 2321.82]  We've talked a lot about this sort of idea of knowledge graphs and ontologies as a reference that's domain specific and known in combination with generative models.
[2322.06 --> 2329.42]  Do you think there's a parallel in the sort of image, vision, audio space where like.
[2329.48 --> 2330.08]  I hope so.
[2330.08 --> 2340.40]  I imagine, you know, groups are like, hey, I need to generate a new design for a web page or I need to fill this empty room with furniture.
[2340.40 --> 2350.76]  And, you know, I could generate a couch, but it'd be really nice if I knew that this couch existed and I could order it online and it's an actual couch that exists.
[2351.06 --> 2354.86]  Because otherwise I could sell this design to my client.
[2354.86 --> 2358.60]  And now like I can't source the couch for my room.
[2359.08 --> 2370.66]  What are your thoughts on that in terms of maybe extending some of your ideas about combining knowledge graphs with generative models to more modalities than just text?
[2370.66 --> 2375.48]  We're in the realm of like most human beings can't see the difference between 4K and 8K.
[2375.76 --> 2385.38]  But you ask any artist to kind of look at and I've done a ton of work with my, you know, just playing around to it's like it's kind of off and you don't know why.
[2385.58 --> 2387.96]  So but it will get better and better and better.
[2387.96 --> 2397.60]  So I think that what I hope will become more valuable is attribution and AI that can give actual attribution.
[2398.30 --> 2400.38]  And so you could do that with anything visual.
[2400.56 --> 2401.66]  You could do that with video.
[2402.06 --> 2408.56]  You can do that with, you know, any sort of, you know, as you were doing it with like kind of like a design or shopping.
[2408.56 --> 2422.70]  I was once having a conversation and again, this is the geek in me, but I'm like an AI can produce its own architecture and its own architectural diagrams or its own ERD.
[2423.50 --> 2431.60]  And that's where I think we should be going is for the AI to explain how it works in and of itself.
[2432.44 --> 2436.68]  And, you know, that's where we're going to potentially get to, you know, cognito ergo soon.
[2436.68 --> 2445.58]  But I think that it would be really cool if AI can start to think in terms of that that three dimensionality.
[2445.98 --> 2454.48]  And I think that if you can get the AI to design how it's functioning and how it's working within itself, that's going to be far more valuable.
[2454.48 --> 2460.32]  And again, far more trusted because that's something that you're going to want to actually build a relationship with.
[2460.32 --> 2474.32]  The big problem that I see with the generative transformers that are pre-trained right now is that they're pre-trained on data that was harvested without people's consent, which means that that data was potentially put there.
[2474.56 --> 2480.90]  You know, I've been I thought it was my job to lie to all of the search engines for the last, you know, at least 10 years.
[2480.90 --> 2485.64]  So, I mean, how good is that data?
[2486.46 --> 2504.34]  And my hypothesis, and I've played it out many times, is like when people interact with my cats where it's AI that they trust and AI that they know where the data comes from, it's an entirely different experience than, you know, back to your initial question, Chris.
[2504.34 --> 2512.68]  Like when you're interacting with something that you don't know how it works and you don't know where the data comes from, that is, you know, you're being told that it's fed data.
[2512.80 --> 2513.38]  You're like, what?
[2513.84 --> 2515.22]  You know what?
[2515.68 --> 2519.84]  It's such a different experience when you can interact with something you trust.
[2520.30 --> 2520.40]  Yeah.
[2520.82 --> 2533.32]  It does change your perception coming into an interface knowing like, oh, this is I'm searching against my company's knowledge base or I'm searching against like a PDF of this book or, you know, whatever it is.
[2533.32 --> 2544.60]  And as we kind of draw to a close here, I'd love to hear maybe like you've talked a lot about things that you're actively working on and that's all really exciting.
[2544.60 --> 2557.32]  As you look to the future, or what are you most excited about in terms of maybe what's going to be possible in the coming year that we aren't quite there yet, but that is really on your mind?
[2557.32 --> 2562.16]  It could be something that, you know, you're actively working on or just something in the industry as a whole.
[2562.16 --> 2572.04]  What, as a positive kind of closeout, what are you most excited about in terms of like trends that are happening or things that you're working on or thinking about?
[2572.24 --> 2572.98]  I have a couple.
[2572.98 --> 2585.40]  I do think that with the technology that I have and with an ontology, I can take like a paragraph of your text and understand something about your existing mental model.
[2586.06 --> 2591.00]  So if I can relate new information to your existing mental model, like I found out you live in Indiana.
[2591.00 --> 2600.00]  If I say something about Indiana, that makes you not only trust me, it makes me give you new information in a way that reduces your period of disequilibrium.
[2600.72 --> 2602.56]  We can make people learn faster.
[2602.56 --> 2605.66]  And that's truly exciting to me.
[2606.04 --> 2621.70]  And I think that human beings, given trusted, evidence-based, tested artificial intelligence, if they had that, you know, I think that it opens up this entire world of visual thinkers.
[2621.70 --> 2631.48]  And shout out to Temple Granin and her new book, Visual Thinking, all about how we've been living in a verbally dominant society.
[2631.96 --> 2632.60]  Well, guess what?
[2632.74 --> 2635.80]  Words just became very cheap, very much of a commodity.
[2635.80 --> 2648.10]  So the engineers, the tradesmen, the plumbers, you know, the people who are doing the things with their hands, the artists, the fuzzies, you know, this is our time.
[2648.80 --> 2656.28]  And I think that you're opening up an entirely new market for everyone to be able to create.
[2656.46 --> 2658.42]  And that, to me, is super exciting.
[2658.78 --> 2659.22]  That's awesome.
[2659.42 --> 2662.32]  Yeah, I think that's a great way to close out and a great thought.
[2662.32 --> 2666.34]  And I now know my next book after I finish The Cuckoo's Egg.
[2666.86 --> 2669.52]  So thank you so much for joining us, Beth.
[2669.56 --> 2672.12]  It's been a real pleasure to talk through things.
[2672.62 --> 2675.90]  I recommend people check the show notes for links that we'll include there.
[2676.28 --> 2678.58]  And hope to chat with you again soon, Beth.
[2678.66 --> 2679.36]  Thanks so much.
[2679.60 --> 2679.92]  You're welcome.
[2680.18 --> 2680.54]  Thank you.
[2689.54 --> 2692.10]  Thank you for listening to Practical AI.
[2692.80 --> 2696.40]  Your next step is to subscribe now, if you haven't already.
[2696.86 --> 2702.88]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2703.52 --> 2708.26]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2708.84 --> 2712.64]  Check out what they're up to at Fastly.com and Fly.io.
[2712.84 --> 2718.36]  And to our Beat Freakin' Residence, Breakmaster Cylinder, for continuously cranking out the best beats in the biz.
[2718.66 --> 2719.54]  That's all for now.
[2719.86 --> 2720.96]  We'll talk to you again next time.
[2722.32 --> 2752.30]  We'll talk to you again next time.
