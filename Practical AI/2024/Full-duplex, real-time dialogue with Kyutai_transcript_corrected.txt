[0.00 → 10.06] Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 → 11.46] and accessible to all.
[11.84 → 14.48] If you like this show, you will love The Change Log.
[14.70 → 19.52] It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 → 21.38] talk show for your weekend enjoyment.
[21.84 → 25.82] Find us by searching for The Change Log wherever you get your podcasts.
[25.82 → 28.32] Thanks to our partners at Fly.io.
[28.70 → 31.08] Launch your AI apps in five minutes or less.
[31.40 → 33.32] Learn how at Fly.io.
[35.38 → 36.30] What's up, friends?
[36.46 → 39.46] I'm here with Kurt Mickey, co-founder and CEO of Fly.
[39.64 → 40.78] As you know, we love Fly.
[41.04 → 43.62] That is the home of changelog.com.
[43.96 → 46.26] But Kurt, I want to know how you explain Fly to developers.
[46.58 → 48.00] Do you tell them a story first?
[48.28 → 48.78] How do you do it?
[49.06 → 53.96] I kind of change how I explain it based on almost like the generation of developer I'm
[53.96 → 54.46] talking to.
[54.46 → 58.60] So like for me, I built and shipped apps on Heroku, which if you've never used Heroku
[58.60 → 61.52] is roughly like building and shipping an app on Tercel today.
[61.68 → 64.32] It's just it's 2024 instead of 2008 or whatever.
[64.52 → 67.48] And what frustrated me about doing that was I didn't, I got stuck.
[67.76 → 72.48] You can build and ship a Rails app with a Postgres on Heroku, the same way you can build and
[72.48 → 74.38] ship a Next.js app on Tercel.
[74.72 → 78.66] But as soon as you want to do something interesting, like as soon as you want to, at the time,
[78.70 → 82.64] I think one of the things I ran into is like I wanted to add what used to be like kind
[82.64 → 84.04] of the basis for Elasticsearch.
[84.10 → 85.88] I want to do full text search in my applications.
[86.38 → 90.60] You kind of hit this wall with something like Heroku where you can't really do that.
[90.60 → 94.96] I think lately we've seen it with like people wanting to add LLMs kind of inference stuff
[94.96 → 95.88] to their applications.
[96.40 → 101.14] On Tercel or Heroku or Cloudflare or whoever these days, they've started like releasing
[101.14 → 103.08] abstractions that sort of let you do this.
[103.08 → 108.38] But I can't just run the model I'd run locally on these black box platforms that are very
[108.38 → 108.92] specialized.
[109.26 → 112.74] For the people my age, it's always like, oh, Heroku was great, but I outgrew it.
[112.90 → 116.70] And one of the things that I felt like I should be able to do when I was using Heroku was like
[116.70 → 119.60] run my app close to people in Tokyo for users that were in Tokyo.
[119.82 → 120.78] And that was never possible.
[121.16 → 125.22] For modern generation devs, it's a lot more Tercel based.
[125.40 → 129.26] It's a lot like Tercel is great right up until you hit one of their hard line boundaries.
[129.26 → 130.56] And then you're kind of stuck.
[130.66 → 131.28] There's the other one.
[131.40 → 132.80] We've had someone within the company.
[133.18 → 136.72] I can't remember the name of this game, but the tagline was like five minutes to start
[136.72 → 137.62] forever to master.
[137.76 → 141.08] It's sort of how we're pitching Fly is like you can get an app going in five minutes,
[141.08 → 144.52] but there's so much depth to the platform that you're never going to run out of things
[144.52 → 145.38] you can do with it.
[145.98 → 153.04] So unlike AWS or Heroku or Tercel, which are all great platforms, the cool thing we love
[153.04 → 158.42] here at Changelog most about Fly is that no matter what we want to do on the platform,
[158.42 → 164.18] we have primitives, we have abilities, and we as developers can charge our own mission
[164.18 → 165.24] on Fly.
[165.40 → 169.72] It is a no limits platform built for developers, and we think you should try it out.
[169.84 → 172.40] Go to fly.io to learn more.
[172.88 → 174.30] Launch your app in five minutes.
[174.62 → 175.30] Too easy.
[175.74 → 177.78] Once again, fly.io.
[188.42 → 199.94] Welcome to another episode of the Practical AI Podcast.
[200.36 → 201.60] This is Daniel Whiten ack.
[201.60 → 208.26] I'm CEO at Prediction Guard and joined as always by my co-host, Chris Benson, who is a principal
[208.26 → 210.52] AI research engineer at Joaquin Martin.
[210.74 → 211.44] How are you doing, Chris?
[211.80 → 213.06] I'm doing very well today, Daniel.
[213.10 → 213.52] How's it going?
[213.82 → 214.66] It's going great.
[214.66 → 219.24] I think we talked about this a little bit on the last show, but now we're officially
[219.24 → 226.68] up against the Thanksgiving break, so a couple of days off here in the US, which will be nice.
[226.80 → 232.52] Maybe I can catch up on some of the cool AI stuff that I've been meaning to play around
[232.52 → 234.36] with in my spare time.
[234.86 → 241.36] But one of those cool AI things that definitely made its rounds over here at Prediction Guard
[241.36 → 247.64] and we were talking about was the recent kind of advances in real-time speech assistance.
[248.30 → 255.18] And in particular, this sort of, you know, what OpenAI was doing, but then also what a lab
[255.18 → 257.90] in France called Tai released.
[258.34 → 265.54] And today I'm really excited because we finally got the chance to have Alexandre Defuse,
[265.90 → 268.84] who is a scientist and co-founder at Tai with us.
[269.00 → 269.50] Welcome, Alex.
[269.98 → 270.58] Thank you, Daniel.
[270.58 → 272.80] Thank you, Chris, for the invitation.
[273.22 → 275.76] Looking forward to discuss the details about Moshe.
[276.16 → 276.90] Yeah, yeah.
[276.96 → 278.20] We're excited about it.
[278.32 → 284.68] And maybe before we do that, if you could give us a little bit of a background on kind
[284.68 → 287.36] of what Tai is, how it came about.
[287.86 → 288.12] Yes.
[288.62 → 294.98] So Tai is a non-profit lab that we launched a year ago in Paris.
[294.98 → 298.86] We have funding from three donors.
[298.86 → 301.86] So Xavier Neil, Rodolfo Shade, and Eric Schmidt.
[302.04 → 304.22] Eric Schmidt is probably the one you know the best.
[304.76 → 306.90] And Xavier Neil is a tech entrepreneur.
[306.90 → 310.82] I mean, entrepreneur now is a successful one.
[310.82 → 314.86] And then Rodolfo Shade works in logistics.
[314.86 → 322.98] So they gather together to try to fund this effort to bring kind of independent lab with
[322.98 → 331.20] a mission to do open source research at a time when the open source is maybe suffering
[331.20 → 335.72] a bit from the competition between some of the major labs.
[336.66 → 340.30] So that's, I think, a big motivation for everyone on the team.
[341.26 → 346.80] And basically, we have sufficient capacity to be kind of competitive with big labs.
[347.38 → 349.08] We can't really fight every battle.
[349.08 → 357.02] But as we show with Moshe, we can definitely bring interesting ideas and innovation to the
[357.02 → 357.28] table.
[357.78 → 357.90] Yeah.
[358.12 → 365.46] And I find it, I mean, maybe for those here in the US AI ecosystem, we do see a lot of
[365.46 → 370.78] kind of innovation and interesting things happening in France and in Paris.
[370.92 → 376.08] I'm wondering, just out of curiosity, what is the ecosystem like there?
[376.08 → 380.84] And how would you, I mean, you seem to be kind of formed out of part of that.
[381.02 → 383.66] So how has that sort of shaped you?
[383.86 → 385.66] And what is the ecosystem like there?
[385.98 → 390.44] I think the ecosystem kind of starts with the studies with France.
[391.48 → 398.26] Like there's a very strong engineering culture, also very strong emphasis on mathematics, which
[398.26 → 406.06] I think was like giving a good soil that initially attracted a number of big American players.
[406.08 → 409.06] like Facebook that opened.
[409.66 → 415.26] So I think at the time, the Facebook AI lab in Paris was probably the second largest after
[415.26 → 419.12] the Californian one about tie with New York.
[419.72 → 427.08] So I think that kind of says how attractive the city can be because it's not so easy to
[427.08 → 429.38] compete with the attractively of America.
[429.38 → 436.14] So now I think what has changed in recent years is really the kind of independence that's
[436.14 → 438.20] growing from this kind of initial seeding.
[438.40 → 444.40] I think for many years, there weren't a number of like truly French organization where you could
[444.40 → 448.94] have access to a sufficient number of GPUs, like large enough clusters.
[448.94 → 453.52] To develop machine learning model for a number of applications.
[454.20 → 456.90] And that's especially the case with large language models.
[457.60 → 464.52] But there's been a number of events that has kind of led to this diversification of the
[464.52 → 465.56] ecosystem in France.
[466.42 → 466.94] Yes.
[467.08 → 469.80] And so now I guess there's like a number of big startups.
[470.74 → 472.02] There's like Tai.
[472.02 → 475.62] There's and I think that's only going to grow.
[476.22 → 481.76] Also, there's one specificity in France, which I think is very nice, especially for deep learning.
[481.76 → 486.82] And it's the fact that we can do a PhD as a resident in a private company.
[487.50 → 489.88] So for instance, or even like a nonprofit.
[490.06 → 495.38] So at Tai, we're going to have PhD students at Facebook where I partially did my PhD.
[496.16 → 499.54] There were also a number of PhD students.
[499.54 → 507.18] And I think it's such a great opportunity to get to use graphic cards so early during our
[507.18 → 509.80] kind of career and even as students.
[510.46 → 512.46] And I think that's very specific to France.
[512.60 → 515.50] And that's also part of the success we're seeing at the moment.
[515.76 → 520.62] And that I think can only be growing as we train more and more people in such a way.
[521.20 → 528.02] I'm curious, as you were describing the ecosystem there in France and how strong it is, what was
[528.02 → 534.02] the specific dynamic that brought about, you know, with all these for-profit organizations
[534.02 → 537.20] around you that brought about the desire to have the nonprofit?
[537.48 → 541.90] And how did you find yourself in the middle of that as you were in the formative stages?
[542.58 → 549.66] I think for me, there was a growing will to become a bit more independent.
[549.66 → 555.08] I think even though at Meta, for instance, there was a lot of value put on the Paris office,
[555.08 → 560.02] at the same time, an American company always takes decision in its centre.
[560.32 → 562.16] So that would be California.
[562.96 → 568.10] And satellite's office always have to kind of bear the consequences of those, no matter the
[568.10 → 572.44] contribution they will make to the overall value of the lab.
[572.44 → 580.84] So that was kind of the initial desire to be a bit more independent in terms of the decision
[580.84 → 583.32] making, the ability to lead the research.
[583.68 → 585.08] I got the opportunity.
[585.24 → 592.22] So I was contacted by Nelle Guido, who was doing his PhD with me at Facebook, at Meta,
[592.52 → 596.70] and then had been at Google doing very successful research there.
[596.70 → 602.52] So he was part of the first team that was contacted, I think, by Xavier Nelle.
[603.00 → 608.54] And I think the project was initially very appealing because it's like, you know, same
[608.54 → 609.50] business as usual.
[609.72 → 616.48] So doing research, what I love the most, having sufficient resources to do it in a completely
[616.48 → 619.02] independent and French environment.
[619.48 → 622.18] So that was, of course, very appealing.
[622.34 → 623.76] I didn't hesitate very long.
[623.76 → 627.30] I guess even at first, it seems a little bit too good to be true.
[628.00 → 629.18] But so far, so good.
[629.50 → 630.24] So, yeah.
[630.80 → 639.96] Tai kind of promotes this idea of open science and, you know, democratization of AI or artificial
[639.96 → 642.10] general intelligence through open science.
[642.66 → 649.56] Some people in our listeners might be familiar with sort of open source, open source AI, or
[649.56 → 651.60] even like open access models.
[651.60 → 656.42] How would you define and think about open science as a thing?
[656.64 → 662.02] And in particular, how that connects to kind of the way in which you envision the building
[662.02 → 664.82] of AI or AGI?
[665.40 → 665.62] Yes.
[665.80 → 669.18] So I think the two are quite related.
[669.18 → 676.08] Usually, the open science comes really around explaining how you arrived at the final results
[676.08 → 682.30] and kind of what are the mistakes you made, what are the things you tried, what was important
[682.30 → 683.30] and what not.
[683.30 → 690.26] So I would say that's like a first part that we've been doing really well with Moshe.
[690.40 → 696.94] We released like a preprint technical report with a lot of details that actually took us
[696.94 → 697.96] a bit of time.
[698.18 → 700.30] And that's something that's not necessarily...
[700.30 → 705.70] I don't think if we were not with this kind of nonprofit mindset, we would dedicate as
[705.70 → 706.20] much time.
[706.26 → 708.20] But I think on the long run, it's kind of important.
[708.98 → 710.56] And then there are several aspects.
[710.70 → 714.98] The open sourcing can go from just the wait to like full training pipelines.
[715.56 → 720.64] So releasing more code around the training of touch models is also on our roadmap.
[720.64 → 726.92] We didn't get a chance to do it yet because, yeah, the paper already took us a bit of time
[726.92 → 729.12] and we have other things we're working on.
[729.98 → 735.18] But I think that's also part of it, like explaining exactly how you got to the final results and
[735.18 → 740.52] not just having a set of waits for one specific task, but being kind of stuck with it.
[740.70 → 746.56] If you need to adapt it to something else, that's kind of the I think, the vision of open
[746.56 → 746.98] science.
[746.98 → 754.28] Could you talk a little bit about kind of what you're able to do with that model that
[754.28 → 758.98] maybe the commercial labs that you have in the same ecosystem aren't able to do?
[759.60 → 764.86] And maybe also kind of, is it more standard within other nonprofits around the world that
[764.86 → 766.16] are doing similar things?
[766.22 → 771.14] Or do you guys, you know, is there something very, very distinctive compared to you that
[771.14 → 774.70] maybe other nonprofits that you've seen or maybe even modelled after don't have?
[774.70 → 777.62] Yes, that's a good question.
[777.92 → 783.80] So I'm not necessarily familiar with all the nonprofits in the AI ecosystem.
[784.06 → 787.84] I know the Allen Institute, for instance, is one of them.
[789.20 → 793.18] I think it's very, there's also the Falcon team, TIA.
[793.86 → 796.84] Yeah, I think we're kind of serving a similar mission.
[797.12 → 801.28] I don't think there is necessarily a big difference.
[801.28 → 806.86] Some of them might be more around like contribution to science, for instance, like general science
[806.86 → 808.14] or core deep learning.
[808.46 → 811.84] I think for us, we are mostly focused on core deep learning.
[812.48 → 817.92] We don't necessarily want to compete, for instance, on the purely text-based LLM space.
[818.08 → 823.24] There are differences in terms of the choices of the research we're doing.
[823.24 → 826.94] But yeah, fundamentally, I don't think there is a big difference.
[827.18 → 831.56] And then your other question was with respect to like other for-profits.
[831.94 → 838.18] What do you feel is really in your sweet spot, to put it in another way, you know, compared
[838.18 → 839.00] to these competitors?
[839.24 → 844.38] It's very easy to kind of say, recognizing that all the resources that some of the largest
[844.38 → 846.68] companies in the world have, and they'll put into their labs.
[846.88 → 849.60] But there's definitely a place for others out there.
[849.60 → 851.76] And I think that gets missed a lot by the public.
[852.34 → 858.00] And so given the fact that you have this space that you're playing in, just kind of,
[858.34 → 863.42] you know, what sets you apart from those commercial in terms of maybe advantages that, you know,
[863.42 → 866.88] just having, you know, the mass number of GPUs available to them.
[867.30 → 868.94] What are some of those distinct things?
[869.60 → 875.04] Compared to some of the for-profits, if we take the biggest labs, obviously, I guess we
[875.04 → 882.36] have agility that that is not really possible in a like super large company where every action
[882.36 → 885.22] will have consequences in the stock market, for instance.
[885.78 → 888.20] So the decision process can be really fast.
[888.36 → 890.40] That was the case for the release of the model.
[890.48 → 895.70] For instance, we were able to release it under a commercially friendly license, which would
[895.70 → 898.44] be a bit harder in larger structure.
[898.44 → 903.92] Then I think we have a strong, for instance, we have a desire to go more and more towards
[903.92 → 905.76] on-device models.
[906.14 → 908.68] I think so mostly is kind of barely on-device.
[908.80 → 912.94] We demoed it on a MacBook Pro, but it was like top tier MacBook Pro.
[913.06 → 916.72] So it's kind of like proof of concept runs on device, not every device.
[916.86 → 921.64] But I think we definitely have a value there because a number of for-profit are not going
[921.64 → 927.80] to develop really powerful on-device models because that would be a potential threat to
[927.80 → 931.50] their like it's harder to protect in terms of intellectual property.
[932.46 → 937.20] And I think in general, between the bigger players, there is kind of the race to the very
[937.20 → 942.16] top, very best numbers on like the benchmarks, MMU and everything.
[942.42 → 947.28] And so, you know, if it takes like 10 times more inference time to beat the other on the
[947.28 → 951.54] benchmark, they are going to do it because it's either beating the other on the benchmark,
[951.54 → 954.16] or kind of leaving the arena.
[955.02 → 956.86] So we're not really in this mindset.
[957.04 → 961.98] We're more like the on-device, I think, could have a very large number of applications.
[962.40 → 964.62] It definitely cannot solve all issues.
[965.32 → 971.74] But I think as a non-profit, we won't have the kind of reservation other for-profit might
[971.74 → 972.92] have for on-device model.
[981.54 → 987.36] Okay, friends.
[987.48 → 990.08] I'm with a good friend of mine, Akthar Sumatran from Timescale.
[990.26 → 997.24] They're positioning Postgres for everything from IoT, sensors, AI, dev tools, crypto, and
[997.24 → 998.00] finance apps.
[998.00 → 1002.80] So Akthar, help me understand why Timescale feels Postgres is most well-positioned to be
[1002.80 → 1005.12] the database for AI applications.
[1005.84 → 1009.74] It's the most popular database according to the Stack Overflow Developer Survey.
[1009.92 → 1013.54] And Postgres, one of the distinguishing characteristics is that it's extensible.
[1013.80 → 1019.22] And so you can extend it for use cases beyond just relational and transactional data for use
[1019.22 → 1021.14] cases like time series and analytics.
[1021.14 → 1024.94] That's kind of where Timescale the company started, as well as now more recently, vector
[1024.94 → 1030.04] search and vector storage, which are super impactful for applications like RAG, recommendation
[1030.04 → 1033.96] systems, and even AI agents, which we're seeing, you know, more and more of those things
[1033.96 → 1035.42] today.
[1035.42 → 1036.58] Yeah, Postgres is super powerful.
[1036.80 → 1038.20] It's well-loved by developers.
[1039.00 → 1044.26] I feel like more devs, because they know it, it can enable more developers to become AI
[1044.26 → 1047.42] developers, AI engineers, and build AI apps.
[1047.42 → 1051.26] From our side, we think Postgres is really the no-brainer choice.
[1051.52 → 1053.12] You don't have to manage a different database.
[1053.40 → 1057.86] You don't have to deal with data synchronization and data isolation because you have like three
[1057.86 → 1060.28] different systems and three different sources of truth.
[1060.28 → 1064.60] And one area where we've done work in is around the performance and scalability.
[1064.94 → 1069.74] So we've built an extension called PG Vector Scale that enhances the performance and scalability
[1069.74 → 1075.30] of Postgres so that you can use it with confidence for large-scale AI applications like RAG and
[1075.30 → 1076.20] agents and such.
[1076.20 → 1080.14] And then also another area is coming back to something that you said, enabling more and
[1080.14 → 1085.24] more developers to make the jump into building AI applications and become AI engineers using
[1085.24 → 1086.76] the expertise that they already have.
[1086.94 → 1091.80] And so that's where we built the PGA extension that brings LLMs to Postgres to enable things
[1091.80 → 1095.62] like LLM reasoning on your Postgres data, as well as embedding creation.
[1095.98 → 1099.36] And for all those reasons, I think, you know, when you're building an AI application, you don't
[1099.36 → 1100.42] have to use something new.
[1100.62 → 1101.68] You can just use Postgres.
[1101.68 → 1105.36] Well, friends, learn how Timescale is making Postgres powerful.
[1105.74 → 1111.46] Over 3 million Timescale databases power IoT, sensors, AI, dev tools, crypto and finance
[1111.46 → 1114.20] applications, and they do it all on Postgres.
[1114.92 → 1117.64] Timescale uses Postgres for everything, and now you can too.
[1118.08 → 1120.10] Learn more at timescale.com.
[1120.40 → 1122.40] Again, timescale.com.
[1122.40 → 1148.60] So Alex, you've mentioned Moshe a few times now.
[1148.60 → 1156.14] Maybe if you could just give those that haven't heard of this an idea of first, what is Moshe?
[1156.68 → 1162.26] And then maybe if you could then after that step back and describe, well, how did the lab,
[1162.38 → 1167.98] how did Tai start thinking about that sort of model or that sort of research direction
[1167.98 → 1170.74] as a research direction of the lab?
[1170.74 → 1171.54] Yes.
[1171.66 → 1179.36] So Moshe is a speech-based foundation model that also integrates text as a modality.
[1180.04 → 1185.38] So it's especially built for speech-to-speech dialogue and especially real-time dialogue.
[1185.66 → 1193.46] So we put a real emphasis on the model being able to act in a way that's the most fluid as
[1193.46 → 1195.88] possible, like a real conversation with a human being.
[1195.88 → 1201.16] And so on of its characteristics is that it's completely full-duplex, meaning that the
[1201.16 → 1204.44] model can both listen and speak at any time.
[1204.56 → 1211.16] So it's not turn-based like walkie-talkies, which I think is an important feature like when
[1211.16 → 1212.12] us, we communicate.
[1212.38 → 1215.20] So we wanted the model to be able to do the same thing.
[1216.04 → 1219.72] We also, yeah, as I mentioned, that allows us also to have a very low latency.
[1219.72 → 1226.50] So we have like around 200 milliseconds between the time the audio leaves your microphone and
[1226.50 → 1230.06] the time you get a reply that has accounted for that audio.
[1231.14 → 1237.22] And yeah, at the moment, it's kind of like mostly we designed it as a speech agent with
[1237.22 → 1243.88] which you can discuss, ask questions, ask for advice that could potentially serve as a basis
[1243.88 → 1246.12] for a much larger use case.
[1246.12 → 1250.32] That's why we also mentioned it as a kind of foundation model and also a framework for
[1250.32 → 1257.70] a number of tasks that would require kind of reacting to your speech and beyond just
[1257.70 → 1260.00] being like kind of assistant.
[1260.52 → 1264.74] And then the second part of the question was, how did we start working on that?
[1264.74 → 1269.14] So we were two people on the initial team.
[1269.50 → 1273.72] So Nell and I, two have done most of our research on audio modelling.
[1274.80 → 1282.88] And then Eduard Grave had been on the like a core member of the initial team of lamas,
[1283.20 → 1285.36] the very first LAMA at Meta.
[1285.78 → 1288.22] So we kind of had the right tools.
[1288.50 → 1293.38] So I guess the first reason is like, basically, we sat together, and we're like, what can we
[1293.38 → 1296.06] do, and where do we have an edge on the competition?
[1296.58 → 1302.90] And I think on this aspect of like combining the text knowledge and the like top of the
[1302.90 → 1308.36] line audio modelling techniques, we had a real edge compared to other labs.
[1308.54 → 1309.62] So that was important.
[1309.62 → 1314.66] And also there was a sense that like speech was becoming an important modality and what
[1314.66 → 1318.14] had been done in a number of other modalities was still completely lacking.
[1318.14 → 1325.26] So I was back in November at the time, like OpenAI hadn't made any announcements.
[1325.62 → 1331.90] So it was still pretty much a new area, a new area to cover.
[1332.26 → 1335.04] So we kind of immediately started working on that.
[1335.22 → 1336.20] We actually started.
[1336.42 → 1342.38] So both on Helium and in parallel, we worked on the MIMI, the codex that we use with the
[1342.38 → 1349.88] goal of having a really highly compressed representation at 12.5 hertz to get as close as possible to
[1349.88 → 1352.58] the text, which would be around like three hertz.
[1352.90 → 1357.28] Of course, it's not regularly spaced with respect to audio.
[1358.06 → 1358.26] Yes.
[1358.36 → 1363.26] And then we once we were happy with MIMI, we immediately moved on to the kind of aspect
[1363.26 → 1364.78] of how do we model the speech?
[1364.94 → 1367.58] How do we handle the full duplex?
[1367.58 → 1373.24] How do we instruct the model like a number of challenging questions that arise all the
[1373.24 → 1376.32] way to the kind of first demo, public demo in July?
[1376.48 → 1377.28] That's great.
[1377.42 → 1381.16] And just one more kind of background question for those.
[1381.36 → 1386.18] Some people might have seen, I guess, non-real time agents.
[1386.52 → 1391.68] So agents that would take an audio transcribe that, you know, maybe transcribe that with one
[1391.68 → 1397.56] model, use a language model to generate an answer and then use a third model maybe to
[1397.56 → 1398.90] generate speech.
[1399.04 → 1403.36] So that's one kind of way to process this pipeline.
[1403.36 → 1409.10] You're talking about something different here, particularly for this speech to speech models
[1409.10 → 1413.80] or the kind of multiplex models that you're talking about.
[1413.96 → 1415.48] Could you give a little bit of a background?
[1415.68 → 1422.52] Like how long have people sort of been studying this, researching this type of model?
[1422.52 → 1429.00] And has it really only been possible in sort of recent times to make this kind of real time
[1429.00 → 1430.04] speech a reality?
[1430.16 → 1435.44] Because I think some people are, you know, at least public wise, they may have seen things
[1435.44 → 1438.16] like Alexa in the past, right?
[1438.52 → 1440.64] The process of speech in certain ways.
[1440.82 → 1445.36] But this sort of demos, at least that they're seeing from OpenAI, demos that they're seeing
[1445.36 → 1447.72] from Tai, this is a different type of interaction.
[1447.72 → 1450.24] So how long has this sort of been possible?
[1450.56 → 1453.40] And what is the kind of history of research?
[1453.74 → 1456.72] Just I know that's a hard question because there's probably a million things that have
[1456.72 → 1457.22] been done.
[1457.40 → 1459.86] But from an overall perspective, how would you view it?
[1460.30 → 1464.42] So I guess just to put in perspective, so I'm not necessarily entirely familiar with how
[1464.42 → 1470.88] Alexa works, but it's more, I mean, anything that's kind of pre-GPT model would be kind of
[1470.88 → 1476.00] rule-based based on like automatic speech recognition, which is actually a fairly old
[1476.00 → 1476.70] field.
[1476.82 → 1482.74] And even real-time speech recognition has been successful for a while, not necessarily
[1482.74 → 1484.94] with the amount of success we see with deep learning.
[1485.66 → 1489.68] I mean, it was already using some of them deep learning before.
[1490.38 → 1491.66] But then it's kind of rule-based.
[1491.74 → 1495.28] So if you don't formulate a request in quite the right way, it's quickly going to say,
[1495.34 → 1497.18] I don't know, or just do a Google search.
[1497.18 → 1504.10] Then what brought a chain of paradigm was all the GPT model and ChatGPT in particular with
[1504.10 → 1509.46] this ability to perfectly understand human requests, no matter how it is formulated.
[1510.08 → 1514.84] Then to bring that to the audio domain, what you need is the ability for a kind of language
[1514.84 → 1518.54] model like a transformer to process the audio streams.
[1519.04 → 1521.78] Ideally, you would think it's very easy for a GPT model.
[1521.98 → 1526.52] You have text tokens in, and you have text token, you predict the next token, and then you just
[1526.52 → 1529.92] need some special characters to differentiate between the request and the reply.
[1530.16 → 1533.94] And you want to be able to do something similar with audio.
[1534.28 → 1537.22] But things are not quite as easy with audio.
[1537.80 → 1540.20] Audio is not as dense in terms of information.
[1540.38 → 1546.18] You can think of words as being like really the almost information from an information theory
[1546.18 → 1550.34] point of view, like optimal way of transmitting information.
[1550.34 → 1556.34] While audio as recorded by a microphone is just a wave that's oscillating like maybe 40,000
[1556.34 → 1557.18] times per second.
[1557.18 → 1560.44] And if you just look at it with your naked eye, it will make no sense.
[1560.98 → 1566.14] So you need the right representation to be able to fit that into like a transformer model,
[1566.70 → 1569.74] have the transformer understand it and be able to produce the output.
[1569.74 → 1573.02] And that has been quite a challenging task.
[1573.76 → 1578.18] Like just if we talk about audio, like the first much success were, for instance, Wavelet.
[1578.48 → 1584.40] And on top of Wavelet, there was Jukebox by OpenAI that I think was the first like,
[1584.84 → 1588.44] let's use a transformer language model to try to model audio.
[1588.92 → 1594.68] But I think I record from their paper that kind of processing one minute of audio would
[1594.68 → 1599.32] take eight hours on like top of the line GPU at the time.
[1599.80 → 1602.20] So obviously the technology has progressed a lot.
[1602.82 → 1609.04] And I think some of this progress was especially done by New Residue, for instance,
[1609.62 → 1615.44] who's another co-founder at Tai at Google with Sound stream in particular that provided
[1615.44 → 1621.20] this kind of discrete representations at a relatively low sample rate, low frame rate.
[1621.20 → 1627.20] And then already very quickly, New and his team showed that this could be fed into a transformer.
[1627.68 → 1631.78] At the time, they were kind of using a technique where you would still have many more,
[1631.94 → 1636.94] like for one second of audio, you would need to do maybe like a few hundred autoregressive
[1636.94 → 1638.64] steps, which is very costly.
[1639.24 → 1644.18] One second with a transformer of like equivalent information would be maybe three autoregressive
[1644.18 → 1644.56] steps.
[1644.56 → 1652.10] So that naturally put a constraint of both your context and the kind of lens of the sequence
[1652.10 → 1656.12] you can generate and completely rules out the real time aspect.
[1656.82 → 1662.44] Then when I was at Meta, I also worked on similar topic, especially on how to kind of
[1662.44 → 1667.88] not do as many autoregressive steps, but try to predict some of the information in parallel
[1667.88 → 1673.48] and how to organize it in a way that you would have kind of minimal dependency between the
[1673.48 → 1674.92] different aspects you need to predict.
[1675.46 → 1679.02] That maybe, I guess it's a bit hard to say orally, but basically it's like for each time
[1679.02 → 1682.62] step, instead of having just one token, like you would have in text, now you have maybe
[1682.62 → 1685.18] four or eight or 16 tokens.
[1685.96 → 1688.00] And yeah, you need to make sense of that.
[1688.10 → 1693.30] You cannot just flatten everything because that's just not going to work in terms of performance.
[1694.18 → 1695.74] And then there was a number of work.
[1695.74 → 1703.34] I think one we use for Moshe, the RQ transformer that kind of models the dependency between those
[1703.34 → 1708.22] tokens for a given time step with a smaller transformer, I guess was a pretty important
[1708.22 → 1712.28] algorithmic contribution from...
[1712.28 → 1718.24] I'm trying to find back who did that, but I don't have it under my eyes.
[1719.06 → 1723.52] But yeah, so we kind of build, so both on this expertise, the work that Nell had been doing,
[1723.52 → 1727.74] the work that I had been doing, and this kind of RQ transformer paper.
[1728.78 → 1733.36] And that's to solve the aspect of being able to run a big language model.
[1733.52 → 1740.62] So let's say 7 billion parameter to take audio as input and then output audio sufficiently
[1740.62 → 1742.20] fast for real-time processing.
[1743.38 → 1749.72] And yes, then the other aspects, I guess the one where we kind of brought a lot of innovation
[1749.72 → 1754.24] was the full duplex aspect of kind of having multiple audio streams.
[1754.44 → 1758.02] So one audio stream for the user, one audio stream for Moshe.
[1758.70 → 1759.78] And I think that's kind of...
[1759.78 → 1764.66] It's not something you would naturally do with text because you already have one stream.
[1764.78 → 1766.72] So going to two streams, you know, it's kind of a hassle.
[1766.86 → 1771.00] But if you think of it for audio, it's like all this kind of tokens in parallel.
[1771.26 → 1775.00] They already form like up to 16 streams that we already had to handle.
[1775.12 → 1777.54] So it was just like, okay, let's just double the number of streams.
[1777.54 → 1781.32] Then now we have two of them that are clearly separated.
[1782.58 → 1784.20] We do actually...
[1784.20 → 1789.10] The model is trained, for instance, during pre-training to also generate some of the users' reply.
[1789.62 → 1792.10] Even if at that stage of the training, there's no real...
[1792.10 → 1795.42] Like it's just kind of a participant in the conversation that sample randomly.
[1796.10 → 1798.84] Then obviously with the model we released, there's no...
[1798.84 → 1801.58] It only tries to model its own stream.
[1801.58 → 1808.22] But yeah, so that's kind of like the rough line of work that led to Moshe.
[1808.90 → 1812.52] Then of course, in audio modelling, there are many other techniques that I didn't mention.
[1812.68 → 1814.98] In particular, diffusion is very popular.
[1815.26 → 1821.70] So there are many models doing diffusion for music generation, for instance.
[1821.70 → 1824.70] For TTS, for a number of things.
[1825.40 → 1831.82] And obviously that's not compatible or like that's much harder to make compatible with the real-time aspect.
[1831.94 → 1837.76] Where autoregressive language model is still kind of the more natural and dominating paradigm.
[1838.48 → 1842.30] That was really fascinating in terms of like understanding.
[1842.68 → 1845.82] And I definitely learned as you were kind of describing it.
[1845.82 → 1852.32] But I don't think I've heard such an excellent, you know, kind of not just from Moshe, but just kind of how to get there on that.
[1853.02 → 1855.90] What I'm wondering in my head is like what are some of the...
[1855.90 → 1860.22] I can imagine as you're talking so many cool things to do with this technology.
[1860.76 → 1868.24] What are some of the cool things that you've seen already or that you guys have tried specifically that maybe wasn't possible before?
[1868.24 → 1877.44] Or that maybe people could only do at some level with something like a ChatGPT 4.0 kind of, you know, through the API that way.
[1877.54 → 1879.22] But, you know, this is open source.
[1879.32 → 1880.16] It's open science.
[1880.40 → 1881.68] They have a lot more capability.
[1881.92 → 1883.72] There must be some pretty awesome stuff out there.
[1884.20 → 1887.72] I mean, there's like a few things that we've done that were really, hilarious.
[1887.80 → 1894.50] For instance, just training on this old data set from the 90s and like early 2000 of phone calls.
[1894.50 → 1898.62] And then it was not really like an assistant anymore.
[1898.78 → 1903.78] So it's just like you end up on the phone with someone random, and they will tell you their name.
[1903.88 → 1906.76] They will tell you what they think about US politics at the time.
[1907.38 → 1911.84] And it's really, it's kind of a different thing that we try to keep with the final Moshe.
[1911.94 → 1916.50] But obviously, with the phase of instruct tuning, we lost a bit of this.
[1916.50 → 1923.28] I mean, it still quickly falls back to the helpful AI assistant personality.
[1923.88 → 1925.22] That's maybe not as nice.
[1926.22 → 1927.48] But that was a funny thing.
[1927.58 → 1929.30] Like, basically, we can train it on anything.
[1929.96 → 1938.76] And then this is going to act like a kind of actor that would pretend to be a certain person in a very realistic way.
[1938.76 → 1948.24] As there's a number of things that we're exploring with this kind of approach, anything that would be like speech to speech or text to speech or vice versa.
[1948.60 → 1952.84] Some of them we kind of mentioned in the paper or with just this framework.
[1953.10 → 1960.32] Because we also have a text stream that's basically we use only for the model to be able to like output its own words.
[1960.44 → 1964.38] We don't actually represent the word from the user, but the model output its own words.
[1964.38 → 1973.00] And this kind of aspect, by making the text late or early on the audio, we can turn the model from being like a text to speech engine.
[1973.00 → 1975.94] Because if the text is early, then the audio is just going to follow it.
[1976.06 → 1984.62] But if the text is late and you kind of force the audio to some value, and you only sample the text tokens, that now becomes automatic speech recognition.
[1985.02 → 1989.70] So I think that kind of shows how versatile this multi-stream approach is.
[1990.08 → 1992.46] And all of those applications are really streaming.
[1992.46 → 2001.12] So we could actually, something we did for the synthetic data was using this kind of approach to generate long scripts.
[2001.70 → 2005.26] And you could imagine like generating maybe 15 minutes or whatever.
[2005.96 → 2009.32] That's our things that we're working now more independently.
[2009.88 → 2018.32] And in terms of more of the general community, I'm not aware of anything in particular.
[2018.32 → 2025.58] I think one thing we want to do, though, is to release code to allow fine-tuning, maybe with Lora and also make it really easy.
[2025.76 → 2029.90] Obviously, the pipeline is a bit more complex because you need audio.
[2030.20 → 2031.76] Ideally, you need transcripts.
[2031.76 → 2037.28] You need separation between the agent you want to train and the users.
[2037.28 → 2044.76] So we want to help with that regard and try to make it easier to adapt it to new use case.
[2044.76 → 2061.42] Well, friends, I'm here with a friend of mine, Michael Greenwich, co-founder and CEO of Works.
[2062.00 → 2063.92] We're big fans of Works here.
[2064.04 → 2065.60] Michael, tell me about Auth Kit.
[2066.08 → 2066.82] What is this?
[2066.98 → 2067.62] How's it work?
[2067.86 → 2068.54] Why'd you make it?
[2068.80 → 2072.70] Works has been building stuff in authentication for a long time, since the very beginning.
[2072.70 → 2077.74] But we really focused initially on just enterprise auth, single sign on, SAML authentication.
[2078.14 → 2082.22] But a year or two into that, we heard from more people that they wanted all the auth stuff covered.
[2082.52 → 2087.64] Two-factor auth, password auth, you know, with blocking passwords that have been reused.
[2087.76 → 2090.38] They wanted auth with, you know, other third-party systems.
[2090.82 → 2100.26] And they wanted really Works to handle all the business logic around tying together identities, provisioning users, and even more advanced things like role-based access control and permissions.
[2100.26 → 2103.70] So we started thinking about that more, how we could offer it as an API.
[2104.28 → 2114.16] And then we realized we had this amazing experience with Radix, with this API, really the component system for building front-end experiences for developers.
[2114.68 → 2118.54] And Radix is downloaded tens of millions of times every month for doing exactly this.
[2118.74 → 2121.16] So we glued those two things together, and we built Auth Kit.
[2121.16 → 2125.00] So Auth Kit is the easiest way to add auth to any app, not just Next.js.
[2125.16 → 2129.80] If you're building a Rails app or a Django app or a just straight-up Express app or something.
[2130.12 → 2131.92] It comes with a hosted login box.
[2132.12 → 2134.36] So you can customize that, you can style it.
[2134.58 → 2136.14] You can build your own login experience too.
[2136.22 → 2137.22] It's extremely modular.
[2137.44 → 2139.96] You can just use the backend APIs in a headless fashion.
[2140.18 → 2143.64] But out of the box, it gives you everything you need to be able to serve customers.
[2143.86 → 2145.68] And it's tied into the Works platform.
[2145.68 → 2148.98] So you can really, really quickly add any enterprise features you need.
[2149.30 → 2154.18] So we have a lot of companies that start using it because they anticipate they're going to grow up market and want to serve enterprise.
[2154.64 → 2158.32] And they don't want to have to re-architect their auth stack when they do that.
[2158.56 → 2162.80] So it's kind of a way to like future-proof your auth system for your future growth.
[2162.96 → 2164.10] And we had people that have done that.
[2164.30 → 2166.40] People that started off, and they're like, oh, I'm just kicking the tires.
[2166.42 → 2167.10] I'm just doing this.
[2167.12 → 2170.06] And then poof, their app gets a bunch of traction, starts growing.
[2170.18 → 2170.58] It's awesome.
[2171.30 → 2174.76] And they go close Coinbase or Disney or United Airlines.
[2174.76 → 2176.52] It's like a major customer.
[2177.10 → 2182.06] And instead of saying, oh, no, sorry, we don't have any of these enterprise things, and we're going to have to rebuild everything.
[2182.50 → 2185.28] Just go into the Works dashboard and check a box, and you're done.
[2185.84 → 2188.02] Aside from the fact that Auth Kit is just awesome.
[2188.40 → 2193.64] The real awesome thing is that it is free for up to 1 million users.
[2194.44 → 2199.54] Yes, 1 million monthly active users are included in this out of the gate.
[2199.54 → 2201.40] So use it from day one.
[2201.74 → 2204.94] And when you need to scale to enterprise, you're already ready.
[2205.06 → 2205.64] Too easy.
[2206.02 → 2210.56] You can learn more at offkit.com or, of course, workos.com.
[2210.80 → 2211.52] Big fans.
[2211.76 → 2212.32] Check it out.
[2212.70 → 2214.40] 1 million users for free.
[2214.74 → 2215.00] Wow.
[2215.38 → 2218.78] WorkOS.com or offkit.com.
[2218.78 → 2242.70] So, Alex, you touched a little bit on the data side of this and also kind of hopeful future fine-tuning opportunities.
[2242.70 → 2254.36] But I'm wondering if you could go into a little bit in particular because we're able to talk about this sort of thing, which sometimes we're not able to talk about given the nature of the models that we're talking about on the podcast.
[2255.04 → 2269.62] What was the sort of data situation that you had to put together in terms of the specific training data sets or fine-tuning data sets that you put together and curated for the model that you've publicly released as kind of model builder?
[2269.62 → 2276.82] Obviously, we had to put kind of both like a pre-training data set in audio and in text.
[2277.44 → 2286.34] Initially, we had to put the text data set together also because there wasn't necessarily at the time an alternative that we could use in terms of license.
[2286.52 → 2297.54] And also, we wanted to be able to keep training both on text and audio so as not to have a kind of catastrophic forgetting of the knowledge that would come from the text.
[2297.54 → 2307.20] One thing we realized that basically it's much easier to have very wide coverage of human knowledge with text than with audio.
[2307.20 → 2318.22] And then there were a number of other difficulties in particular, the fact that for the last stage of the training, we needed audio with like clearly separated speakers.
[2318.80 → 2321.58] And also, we needed some kind of instruct data set.
[2321.58 → 2334.82] So for the separation, we bootstrapped things from the Fisher data set, which is the data set I mentioned earlier of phone calls that kind of gave us a good enough base to then be able to train TTS model with separate speakers.
[2334.82 → 2337.72] Also, in combination with some recordings.
[2337.90 → 2348.76] So actually, as I talk about like, you know, taking faster decisions and in larger organizations, at one point, we're like, OK, we need like perfect studio quality recordings of people on separate microphones.
[2348.76 → 2351.68] So then we got in contact with a studio in London.
[2351.68 → 2357.98] Then the next day, we were on the Eurostar and just like recording a few people, which I think was really fun.
[2357.98 → 2363.22] It's good to have a break from just launching jobs and crunching numbers now and then.
[2364.10 → 2374.14] And yeah, leveraging that plus the Fisher data set, then we could train a TTS model that we could have follow like specific emotions and have two separate streams as output.
[2374.54 → 2380.70] So for the two speakers, and then we use that to bootstrap an instruct data set.
[2381.22 → 2386.28] Initially, we tried to convert to audio existing instruct data set for text.
[2386.28 → 2392.36] But we quickly realized that a few scripts that were specifically tuned for audio would give much better results.
[2392.78 → 2401.24] And one of the reasons is that if you look into some of those existing instruct data sets, it's very geared toward first the way we're going to use text models.
[2401.40 → 2406.20] So maybe like some people copy and paste the Markdown table, and they ask to comment on it.
[2406.36 → 2412.14] There are a number of entries that are specifically done for kind of benchmark types of questions.
[2412.14 → 2415.94] So it's going to be multiple choice question and the model just answers B.
[2416.28 → 2418.00] But that's not something you're going to do orally.
[2418.10 → 2421.24] You're not going to like to give for choice and the model just answers B.
[2421.80 → 2425.80] We needed like a lot more multi-turn, like also shorter reply.
[2425.96 → 2429.86] You don't want the model to spit out like an entire paragraph for a reply.
[2429.86 → 2435.84] So with that in mind, we had to kind of rebuild everything so that that Edward did a lot about that.
[2435.84 → 2442.82] So some of it was kind of pinging existing LLM being like, OK, what are like 100 different tasks we could do with a speech assistant?
[2442.82 → 2446.82] And then for each task, give me like 100 possible scenarios.
[2446.82 → 2452.70] And then we had another model that we had fine-tuned specifically to follow kind of the oral style.
[2452.80 → 2456.12] So shorter answers, like maybe short change of turns.
[2456.44 → 2460.50] We would like randomly sample topics and have discussions about them.
[2460.60 → 2462.92] So we tried to cover different aspects like that.
[2463.04 → 2464.76] And then we synthesized everything.
[2464.76 → 2469.48] So at the end, the dataset was fairly large.
[2469.72 → 2473.14] I think a few tens of thousands hours.
[2473.56 → 2477.74] And it was kind of sufficient to get like to the state for the demo.
[2477.74 → 2492.48] So even though that was kind of cool that we could bootstrap this entire modality basically from like this, like one or 2000 hours recordings from the early 2000 and a few hundred hours that we had recorded in the studio.
[2492.72 → 2496.68] One thing we noticed is that there is still what we call the modality gap.
[2496.94 → 2500.68] So there is still a gap in knowledge between the text model that we started from.
[2500.68 → 2504.58] And even actually, as we train the model, we can, we still train it on text.
[2504.66 → 2508.14] So we can always switch it to text mode and ask it the question in pure text.
[2508.56 → 2514.84] And the model would be like to get much better replies on trivia QA than it would get with the audio.
[2515.84 → 2522.82] And that's, I think, a really fascinating question of how to make the model understand that it's the same thing.
[2522.92 → 2530.30] At the same time, it's very easy for it to think, oh, it's two different modalities, especially with the pre-training on audio where it gets like kind of random audio.
[2530.68 → 2534.90] Not necessarily a focus on like giving the right answers all the time.
[2535.36 → 2547.98] We could recover some of that with the Inch drug, but I think there's still work to do to be kind of as simple, efficient as a text model into really becoming super useful and factual.
[2548.52 → 2555.30] I'm curious, and you may have mentioned it, you mentioned 7 billion parameters earlier, but is that the size of the model?
[2555.40 → 2557.58] Is it a 7 billion parameter size model?
[2557.58 → 2560.28] Yes, it is 7 billion parameters.
[2561.22 → 2565.88] So as I mentioned, so it's a RQ transformer architecture.
[2566.20 → 2567.84] Actually, I found back the author.
[2568.10 → 2580.44] So it's Joyous Lee and collaborators that published first this model, which has the main backbone transformer and the small transformers that just tries to predict the different acoustic tokens.
[2580.86 → 2582.88] This one is kind of smaller.
[2582.88 → 2589.34] I don't have the weight, the size exactly, but in terms of runtime, inference time, it's negligible.
[2590.00 → 2595.74] Most of the knowledge and decision is done in the big 7 billion transformers.
[2596.30 → 2598.96] How did you pick the model being that size?
[2599.08 → 2607.86] And also as an addendum to that, what is your perspective on relatively smaller models versus the relatively larger models?
[2607.86 → 2609.74] How do you see that?
[2610.28 → 2616.68] Yeah, I guess when we started, 7 billion was kind of the minimum size for large language models.
[2616.96 → 2627.92] Now, I guess 2 billion and 3 billion down to 1 billion, especially with the advance of distillation techniques from bigger transformers have become very efficient.
[2627.92 → 2633.92] They are now as efficient as tech's model at 7 billion parameters from like a year and a half ago.
[2634.40 → 2640.48] But yeah, at the time when we started, we're like, OK, we don't know exactly how much compute, how much capacity it's going to take to solve the task.
[2640.60 → 2642.22] So we don't want to take too many risks.
[2643.32 → 2648.42] 7 billion was a well-charted territory and at the time, like a pretty good balance between the two.
[2648.42 → 2656.90] Now that we know that we can solve the task with 7 billion, obviously, we want to try to go lower than 7 billion.
[2657.44 → 2671.08] And that's something we are exploring because like the way we see things, it's going to be very hard and probably not super useful to try to put all the like thinking capacity and problem-solving capacity into Moshe.
[2671.08 → 2685.64] But we want it to be smart enough to have a direct conversation, understand what the user wants and potentially then access other source for getting like more complex answers that would also allow like a more plug and play aspects.
[2685.84 → 2691.18] And like now you have a new text language model, you don't necessarily want to retrain from scratch the audio part.
[2691.18 → 2702.22] So the way we see it is going towards like smaller model for managing this direct low latency interaction, delegating some of the works to a larger model when needed.
[2702.64 → 2709.96] So for sure, now that we know it works with 7 billion, we would try smaller so that we can run on a much larger number of device.
[2710.12 → 2719.76] I guess you already started kind of talking towards additional things that you want to try with respect to Moshe and these types of models in the future.
[2719.76 → 2736.62] But maybe stepping back a little bit as we get close to the end of the episode here, when you as a researcher in this area look towards the future, it could be work that you all are planning to do internally or just things going on more broadly.
[2736.62 → 2747.96] But what kind of is some of the most exciting things for you as you think about the kind of next year of your work and the things that you're following, the things that you're looking at?
[2748.98 → 2755.60] What's on your radar, and what are you excited to kind of participate in and see happen in the coming months?
[2756.16 → 2760.76] Okay, in the coming months, that's a good question.
[2760.76 → 2768.50] I mean, I think one topic that I'm interested at the moment is whether we're going to be one day in the post-Transformer era.
[2769.06 → 2773.96] Like, I love Transformer and I love not having to wander anymore.
[2774.26 → 2780.06] I mean, if we look at the set of hyperparameters to train those models there, I've been frozen for maybe two years, two years and a half.
[2780.18 → 2787.24] You know, the architecture is frozen, which is good because now we mostly focus on just like making the right data to solve problems.
[2787.24 → 2788.68] And there's a lot we can do.
[2789.10 → 2799.30] At the same time, I think I would be really excited to see advancements that could happen either on the optimization side or the architecture side.
[2799.74 → 2805.30] We've seen a lot of like interesting work in this area, but at the moment we're more on a parity thing.
[2805.30 → 2820.18] Okay, so we've found other ways of doing kind of the same thing, but there is not really something that has won a decisive aspect or feature that would be potentially not sufficiently well done with Transformers.
[2820.84 → 2823.14] There's been like tons of engineering going into it.
[2823.26 → 2832.94] So, you know, each time you think, oh, maybe quadratic cost is bad, but then people are like, no, you can just hardcore optimize your CUBA kernel, and now it's no longer your problem.
[2832.94 → 2839.90] But yeah, that's I think in terms of just the scientific excitement, that's one thing that I want to keep my eye on.
[2840.36 → 2844.98] Obviously, as at the same time, there is a lot of competition going on just applying the current model.
[2845.16 → 2851.12] It's not necessarily easy to free time and mental space to try to think about those issues.
[2851.96 → 2852.96] So that's one aspect.
[2852.96 → 2859.94] And yeah, then I'm also curious about how all the framework aspect is going to evolve.
[2860.92 → 2872.04] Working day to day with those technologies really feels like you're back in the 70s of like pre-C era where you have to think about the CUBA, like the code is different for each architecture.
[2872.76 → 2874.98] There's a lot of leakage, abstraction leakage.
[2875.22 → 2877.36] It's not like you're not going to write a nice function.
[2877.60 → 2879.32] You need to write kind of dirty things.
[2879.32 → 2882.96] You need to do the equivalent of pointer arithmetic all the time.
[2883.62 → 2884.48] So that's another thing.
[2884.58 → 2888.54] So maybe I'm not replying your question of what's coming in the next few months, but longer term.
[2889.12 → 2899.72] Sometimes I just think of myself in 10 years and, you know, you can just write your attention kernel in a few lines of code in a dedicated language, and you get like almost perfect code.
[2900.16 → 2903.82] And I think that would be amazing to just explore more things more easily.
[2903.82 → 2905.52] But we'll see.
[2905.74 → 2908.94] So two, yeah, two big, big potential changes.
[2909.06 → 2911.78] But I think something's going to happen in the coming years.
[2912.50 → 2912.58] Yeah.
[2912.92 → 2913.10] Yeah.
[2913.18 → 2916.80] Well, thank you very much for sharing your perspectives with us.
[2916.80 → 2932.54] And also thank you for the way that you and the Tai team are inspiring many, many people out there that are working on open models, open source, open science, and kind of just generally collaborating in this space.
[2932.66 → 2935.16] Really appreciate kind of what you're doing as part of that.
[2935.26 → 2937.84] And thank you for taking time to chat with us.
[2937.88 → 2938.42] It's been great.
[2938.86 → 2942.20] Thank you very much for the invitation, opportunity to present.
[2942.34 → 2945.12] And hopefully we'll have some others in the future.
[2945.62 → 2946.04] Definitely.
[2946.04 → 2948.10] And enjoy Thanksgiving.
[2948.10 → 2956.50] All right.
[2956.82 → 2958.68] That is our show for this week.
[2959.06 → 2964.98] If you haven't checked out our Changelog newsletter, head to changelog.com slash news.
[2965.22 → 2967.46] There you'll find 29 reasons.
[2967.68 → 2970.88] Yes, 29 reasons why you should subscribe.
[2971.32 → 2972.90] I'll tell you reason number 17.
[2973.28 → 2976.22] You might actually start looking forward to Mondays.
[2976.22 → 2979.10] Sounds like somebody's got a case of the Mondays.
[2979.50 → 2984.06] 28 more reasons are waiting for you at changelog.com slash news.
[2984.28 → 2986.80] Thanks again to our partners at Fly.io.
[2987.18 → 2988.90] To Break master Cylinder for the beats.
[2989.22 → 2989.92] And to you for listening.
[2990.38 → 2991.48] That is all for now.
[2991.64 → 2992.98] But we'll talk to you again next time.
[2992.98 → 2995.84] MAL laugh.
[2995.84 → 3000.94] Vicki Davis.
[3000.94 → 3002.10] ят
