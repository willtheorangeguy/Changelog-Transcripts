[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 → 22.72] on Linde servers. Head to linode.com slash Changelog. Welcome to Practical AI, a weekly
[22.72 → 27.62] podcast about making artificial intelligence practical, productive, and accessible to everyone.
[27.62 → 33.20] This is where conversations around AI, machine learning, and data science happen. Join the
[33.20 → 37.28] community and snag with us around various topics of the show at changelog.com slash community.
[37.46 → 41.38] Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[46.14 → 52.38] Welcome to another episode of Practical AI. This is the podcast where we try to make AI practical,
[52.38 → 57.54] productive, and accessible to everyone. I am Chris Benson, one of your co-hosts. I
[57.54 → 64.44] am the chief AI strategist at Lockheed Martin RMS API Innovations. And with me is my co-host,
[64.62 → 69.28] Daniel Whitelaw, a data scientist with SIL International. How's it going today, Daniel?
[69.48 → 71.00] It's going great. How about with you, Chris?
[71.40 → 73.18] Doing good. What you been up to lately?
[73.50 → 80.22] Well, I finished out my course that I was teaching at Purdue University. So I'm enjoying
[80.22 → 89.10] one grading and then throwing some eggnog in there when I can pair the two. That's working out well.
[89.92 → 95.10] Sounds great. As I mentioned, as we opened up, I actually started this new job at Lockheed Martin.
[95.42 → 100.42] Very excited about it. I've been ramping up on that. And I've never worked for a defence
[100.42 → 105.84] contractor before. So I'm learning all sorts of new things, you know, about how to apply AI. And it
[105.84 → 108.26] has been absolutely fascinating the last couple of weeks doing that.
[108.46 → 113.12] Yeah, it's exciting. Don't share too much, or you'll have to kill us, I'm sure.
[113.62 → 121.96] Yeah, I'll have to kill myself. So there we go. So I wanted to introduce our guest today. Our guest
[121.96 → 129.12] has become a good friend of mine in recent months. Susan Ettinger is an industry analyst with
[129.12 → 136.30] Altimeter, which is a profit company. And Susan and I met at the Adobe AI Think Tank earlier this
[136.30 → 141.90] year in New York City, where she moderated a 90-minute broadcast on Facebook. And I was privileged
[141.90 → 145.08] enough to be one of the people on the panel. How's it going today, Susan?
[145.08 → 149.32] I'm great. Thank you. It made it sound like we spent the entire 90 minutes talking about Facebook,
[149.46 → 150.98] but we actually talked about AI.
[151.82 → 157.14] Very true. I'm glad you said that. Very, very true. Yeah, we had a great panel and talked about AI
[157.14 → 162.46] with a lot of really smart people. They were able to contribute to that conversation. And so it was
[162.46 → 167.54] a great, great time to meet. And I've enjoyed talking to you ever since. And it became obvious
[167.54 → 173.58] really, really early on that I had to try to twist your arm to get to see if you would come on to our
[173.58 → 179.54] podcast, because there is so much about the world of AI that you know. And fortunately for us, you have
[179.54 → 186.54] just I know that you have been working on a report that is fascinating called the maturity model for AI and
[186.54 → 192.08] enterprise where you're talking about AI in enterprise in the industry. And I was wondering
[192.08 → 194.78] if we could start off with you just telling us a bit about that.
[195.20 → 199.80] Yeah, absolutely. Actually, it's just gone live as we're recording this. So by the time this podcast
[199.80 → 204.16] airs, everybody's going to be able to see it. So what I've been trying to do over the course of the
[204.16 → 210.18] past, you know, depends on how you count it, several months to several years is understood a little
[210.18 → 215.28] bit about the way that artificial intelligence is evolving, not just as a technology or as a
[215.28 → 221.42] kind of societal or social impact, but also just in terms of the impact on business, you know,
[221.44 → 226.12] because the impact on business is so different in so many ways, the kind of enterprise impact versus
[226.12 → 231.68] the consumer impact that I wanted to try to get a handle on it. So this report is about two major
[231.68 → 236.56] things. One is kind of what are the four trends that are really affecting the way that enterprises
[236.56 → 241.74] implement AI. And those four trends have to do with how we interact, you know, moving from
[241.74 → 248.80] rules, screens to senses. So moving from URLs to kind of speech and images and that sort of thing.
[249.08 → 254.58] The next is around how we decide. And that is, you know, moving from the old way of programming,
[254.58 → 259.40] if then statements, so, you know, from business rules to probabilities, you know, because AI is,
[259.56 → 265.98] of course, inherently probabilistic. The third is around how we innovate. And, you know, in the past,
[265.98 → 271.32] or actually in the current, in the future, we're going to go to more of a kind of data engineering
[271.32 → 275.78] world where we're actually incorporating data into the engineering process in a much more fluid way
[275.78 → 280.04] than we can do today. And that's something, Chris, that your insights really helped me shape.
[280.66 → 285.34] You know, today we're kind of in many, in many places anyway, we're in a sort of reporting on the
[285.34 → 290.72] past kind of world, and we need to be able to use data in a much more forward, forward-thinking way.
[290.72 → 296.42] And then the last is around how we lead, you know, because we live in a world that's very hierarchical,
[296.70 → 303.00] that's very expertise driven. And of course, data and the ability to get clean data is going to help
[303.00 → 309.14] us make decisions based on data. I've had the ability to go ahead and read this. I know you
[309.14 → 313.92] had quoted me as one of a number of people in the article and let me see a preview. And the big thing
[313.92 → 319.66] that I really was thinking through this process was how much I wish I had had this over the last
[319.66 → 325.88] couple of years as I worked for previous employers and trying to put together the business case and
[325.88 → 333.30] the operational aspects of AI teams. So, you know, we're starting to see organizations like Google
[333.30 → 339.52] and Amazon and stuff offering up some of their internals. But this report, the AI maturity playbook
[339.52 → 345.52] that you've put out is a huge, huge tool to get people started in this. And I wish I'd had it all
[345.52 → 347.32] along. And Daniel, were you going to say something?
[347.32 → 351.32] I was just going to say, it's interesting that the thing that stood out to me when you were talking
[351.32 → 355.08] through that is, is kind of the emphasis on engineering that you were talking about and
[355.08 → 359.48] integration within a company's infrastructure. And I don't know if you've seen this, maybe you can
[359.48 → 365.22] comment on this, but it seems like we've seen a trend, at least when I'm looking at like job postings
[365.22 → 371.16] and people's titles and such. There was kind of a time when we were talking about, oh, everybody needs
[371.16 → 376.84] to be a data scientist, and we're all going to use data for stuff. And then like it kind of moved
[376.84 → 381.96] into everybody needs to be doing like AI and be an AI person or machine learning person,
[382.36 → 388.02] scientist. And then like now it's kind of drifted into, I see a lot of job titles looking for like
[388.02 → 393.80] machine learning engineers or AI engineers or data science engineers, whatever that is. But I think
[393.80 → 399.56] it's like people are gradually coming to the realization that they actually have to do some
[399.56 → 404.86] type of integration of this stuff in their, in their infrastructure. Yeah. And I don't know,
[404.86 → 408.94] are people feeling that pain? What's pushing that side of things forward?
[409.58 → 414.44] Yeah. Well, it's funny because this topic, this issue of sort of data analytics to data science,
[414.44 → 418.36] to data engineering really popped up in my interview with Chris, you know, not to do too
[418.36 → 422.40] much log rolling here, but I mean, it's really where I started to think about it. And so in the
[422.40 → 426.56] subsequent interviews, when I spoke to other people, I asked them, you know, and even just people
[426.56 → 430.02] that I know in the industry who weren't necessarily formally interviewed for the report.
[430.02 → 434.08] And I'd say, so what, you know, how is this working for you? Like if it's a startup,
[434.20 → 437.24] what are you seeing with your clients? Or if it's a big enterprise platform, you know,
[437.28 → 440.80] kind of enterprise platform, what are you seeing? And then in enterprise companies,
[440.80 → 445.42] I was asking them like, kind of, where are you on the spectrum? And they're like, oh yeah,
[445.78 → 450.60] yeah. Because we've brought in all these data scientists who have a very particular way of,
[450.74 → 456.14] of working and the challenges getting to scale, you know, and getting to be able to build,
[456.14 → 460.06] you know, not just models, but products that we can scale across the organization.
[460.48 → 464.90] And that's a whole, you know, not only a technical challenge, but a cultural one as well.
[465.04 → 469.68] And also a recruiting challenge in terms of trying to figure out what are the qualities we should be
[469.68 → 475.52] hiring for in order to be able to build scalable infrastructure. So that's been, you know, that's
[475.52 → 481.02] been kind of a or scalable products. And that's been kind of a big theme really that I wasn't,
[481.26 → 482.58] I didn't really know to expect.
[482.58 → 486.88] When we had that conversation, Susan, and, and we're discussing that it was,
[487.28 → 493.82] I found it in my own experience, as I went into a previous employer and was creating a full AI
[493.82 → 499.82] operation within that organization, that a big surprise for me had been that I was hiring on
[499.82 → 503.24] some new people, and I was pulling people from other parts of the organization. And I had a
[503.24 → 508.90] a mixture of skills there. And some of our team members were just straight data scientists,
[508.90 → 514.52] in a lot of cases, fresh out of school. And that had been their exclusive focus and being this
[514.52 → 522.12] new field of, you know, neural network model creation and such. I think myself and others on
[522.12 → 527.82] the team really expected that to be the strongest skill set. And what we were surprised to find was
[527.82 → 532.32] some of the other members of the team had already been in industry and had created products and
[532.32 → 535.66] services for other companies or previously for the same company.
[535.66 → 540.62] Um, they had been programmers in various other roles, and they had moved in, uh, and maybe gone
[540.62 → 546.46] back to school in some cases for data science and to learn this. And I was surprised that those people
[546.46 → 553.44] were able to apply the after model creation, that they were able to apply that better after the fact.
[553.44 → 559.82] And so in some ways, potentially the people who had focused exclusively on this had, had a leg up,
[559.82 → 564.42] but as soon as some of the others caught up with them, the fact that they knew how to deploy and how
[564.42 → 569.60] to meet a business need from, in terms of products and services was a huge advantage for that crowd.
[569.60 → 571.52] And that was something that surprised us all.
[571.52 → 576.10] Yeah. And, you know, I think what's interesting is that this seems like just part of the evolution,
[576.28 → 581.20] you know if we think back on other technologies and how they became, you know, kind of enterprise ready,
[581.20 → 586.22] you know, you see similar trajectories where you're hiring for a skill and that skill may or may not
[586.22 → 591.30] come with another set of, with another particular set of skills, right? That's a challenge with every
[591.30 → 596.90] technology, but I think particularly with AI, because there is so much hiring that comes, you know,
[596.90 → 601.36] directly out of the academic setting. And that's such a different, it's such a different set of
[601.36 → 601.98] expectations.
[601.98 → 608.52] So I'm curious on your, your opinion on, um, on the following in light, in light of that,
[608.52 → 613.52] and in light of the other things that you mentioned that are changing around how we will be interacting
[613.52 → 619.20] with systems, for example, and how systems will be more dynamic and, and reactive. Do you think,
[619.20 → 624.40] you know, for the software engineers out there that are listening to this podcast that are maybe
[624.40 → 629.80] interested in, in AI, I know that there's like some concern amongst software engineers that they're kind
[629.80 → 636.00] of being like their job will need to drastically change? And that sort of thing as AI is more
[636.00 → 641.60] integrated into, into the products that we're building. Do you, do you see that like software
[641.60 → 648.16] engineering as a whole is going to see a very dramatic shift or will it more be like AI is just
[648.16 → 652.56] going to be something they interact with, but you know, it'll be another layer in the stack or
[652.56 → 653.28] something like that?
[653.70 → 657.44] Yeah. Well, you know, it's funny, Daniel. I mean, I can answer as a non-software engineer,
[657.44 → 662.40] just in terms of what I've observed and what I've observed is I don't think I've ever seen
[662.40 → 667.06] a software engineer who hasn't had to change, you know, who hasn't had to evolve their skills,
[667.20 → 671.76] who hasn't had to figure out something that they weren't expecting. You know, if you think back to
[671.76 → 677.32] the beginnings of the internet, like that was a massive, massive change in the mid-nineties and the
[677.32 → 685.08] early two thousands, you know, and the development of even like social technologies and so, and mobile
[685.08 → 690.28] technologies and all of that, you know, every single time there's a massive shift, there's a massive set
[690.28 → 696.72] of changes that reverberate through the industry. And I just don't ever see that changing, you know,
[696.72 → 702.32] and then in terms of kind of the long view, I do think that learn, you know, intelligent systems,
[702.32 → 707.64] the ability to learn from data, autonomous systems, that's going to be table stakes. I don't know how
[707.64 → 711.52] many years, you know, I can't, I don't have a crystal ball, but it's going to be what we're, what
[711.52 → 715.24] we're thinking of as sort of exotic now is going to be table stakes. And that's really a lot of the
[715.24 → 716.42] thrust of the report too.
[717.16 → 721.76] So I know that having had the advantage of seeing it ahead of time, you started off the report kind
[721.76 → 726.36] of talking about some of the macro trends that would affect AI and stuff. And you were really
[726.36 → 731.22] thoughtful in how you were approaching how kind of the real world would affect this. You talked to,
[731.22 → 736.04] I remember about kind of the interactions that we're having with computing. I remember one of
[736.04 → 740.88] the sections was talking about as we move from screens to different senses that we may not have
[740.88 → 745.96] used historically. And then I believe you went on to kind of how we decide, how we innovate,
[746.16 → 750.34] how we lead. And I was just kind of wondering, you know, what some of those insights were that we
[750.34 → 751.18] could share with our listeners.
[751.80 → 756.56] So, you know, the screen thing, you know, how we interact is fascinating because we're just
[756.56 → 762.68] so used to, you know, if you're older than like, you know, 30, you know, you're used to interacting
[762.68 → 769.94] with a laptop computer or even a desktop computer and a phone. You know, if you're younger than 30,
[770.34 → 775.04] more of your life has been spent, you know, talking to your phone and talking to that weird little
[775.04 → 779.82] cylinder on your dining room table or your thermostat or whatever it is that, you know, that you're
[779.82 → 787.08] talking to, we're certainly becoming much more accepting of things like facial recognition and
[787.08 → 791.82] image recognition, although, you know, obviously that comes with issues. And there are even people
[791.82 → 797.68] who are working on sensory-based interactions based on smell and taste, you know, so like none of our
[797.68 → 803.58] senses is actually, you know, none of our senses is going to be left behind. And of course, touch,
[803.72 → 809.50] you know, using haptics and pinch and Zoom are all very normal to us now, you know, and you go back
[809.50 → 814.98] 10 or 15 years and like, that was just, that was minority report. That was something that lived in
[814.98 → 821.44] science fiction. The biggest shift to me though, of all of these shifts is around how we make decisions
[821.44 → 828.74] because we are so used to living in a world that is based on if then statements. If my balance drops
[828.74 → 836.68] below $500, send me an alert. If I make a transaction more than $300, send me an alert. If I do a transaction,
[836.68 → 843.18] you know if I try to buy something in a in an airport in Berlin, decline my credit card. And now
[843.18 → 849.04] what we're seeing is that the world is a lot more probabilistic. And sometimes that's fantastic,
[849.04 → 854.78] right? And it's really easy to understand, and it's intuitive. And sometimes it actually creates a lot
[854.78 → 861.46] of stress for organizations because, you know, you could say something with an 85 or 87% confidence
[861.46 → 866.26] level is fine for one industry and completely off the table for something else.
[866.72 → 871.26] I mean, I imagine that that creates, I don't know, in my mind, I'm thinking for a lot of people,
[871.36 → 877.56] maybe including myself in, in certain scenarios that create a lot of trust issues, right? It might be
[877.56 → 883.00] harder for me to understand naturally the, the probabilistic way of dealing with all of these
[883.00 → 888.96] complicated scenarios, but I kind of have to put my trust in the modelling at that point, right? And not
[888.96 → 893.60] just kind of in an easily understandable if then statement.
[894.18 → 898.02] Yeah, absolutely. The thing is too, that it's not just about putting your trust in the model,
[898.10 → 903.58] right? It's the engineering and user interface and other kinds of communicative decisions that are
[903.58 → 908.84] made to let you know whether you should trust the data. So I'll give you an example. And this sort of
[908.84 → 914.98] almost kind of is a nice segue into the conversation about ethics. In Turkish, and as in many other
[914.98 → 920.56] languages, there are no gendered pronouns. So the word for he and the word for she is the same. It's
[920.56 → 927.16] actually the word, Oh, but with the letter Oh. And if you take the sentence, she is a doctor on Google
[927.16 → 932.48] translate, you can do this yourself. And you translate it into Turkish, it will come back with
[932.48 → 938.74] Oh beer doctor. Sorry about the pronunciation, Turkish speakers. And then if you take Oh beer doctor,
[938.74 → 946.08] and you translate that back into English, Google will assume and write he is a doctor. Now, this is
[946.08 → 953.70] probabilistic, because if you look at the word to beck data set, we know already that the word doctor,
[953.70 → 961.52] as many other professions is biased toward male humans, because there are more instances in that
[961.52 → 968.72] data of men being doctors than women being doctors. And even if it's 50.5%, you know, it's going to be
[968.72 → 975.10] a man. And so there. So here's the thing, the language, you know, the Turkish language has been
[975.10 → 981.12] around a bit longer than Google. And yet, and it's not likely to change, you know, for Google's sake.
[981.50 → 988.14] And yet, there's no indication when you do Google Translate, that what you're looking at when it
[988.14 → 994.58] says doctor, you'd probably got a 97 98% probability that it's correct. But when you're looking at the Oh,
[994.58 → 1000.96] that signifies the gender of the human being discussed, that, you know, it's way, way,
[1001.10 → 1007.10] way lower. And so what I'm saying is that sometimes we actually need to incorporate into engineering and
[1007.10 → 1012.96] into user interface design, some indication for people that what they're looking at May or may not
[1012.96 → 1019.60] require further analysis. Yeah. And I do think that this leads right into a great discussion on
[1019.60 → 1025.72] ethics, which I'm eager to get into. But before we kind of jump into those details, I'm wondering if
[1025.72 → 1033.08] kind of based on what you're just saying, those are kind of real problems, real biases, real kind of
[1033.08 → 1039.08] dangers, if you want to put it that way, that exists right now in machine learning and AI. I'm wondering,
[1039.08 → 1045.22] like, so much of the conversation around like the danger of AI and other things, people kind of
[1045.22 → 1050.70] naturally go to the scenario of like the Terminator scenario or consciousness or something, right?
[1050.82 → 1057.88] Do you think that, you know, distracts from these real kind of dangers and biases that we're
[1057.88 → 1062.52] experiencing now? And should we even be having that conversation? Or should we as
[1062.52 → 1069.24] practitioners kind of how can we help bring a more balanced view into what we should really be
[1069.24 → 1071.62] talking about in terms of ethics, I guess, is my question.
[1071.62 → 1076.60] Any of us who work in this field, you know, somebody like me, who's an analyst, you know,
[1076.60 → 1081.20] really with a humanities background versus, you know, you guys who have much, you know, deeper
[1081.20 → 1086.36] technology, technological chops than I could ever hope to have, like, you know, you maybe you hang
[1086.36 → 1090.26] out with your family at the holidays, and they ask you what you're working on, you say AI, and they're
[1090.26 → 1095.84] like, one of the robots coming to get us. And that's the conversation really that much of the world is
[1095.84 → 1100.36] having, right, that the trolley problem, you know, if the car is driving down the road, and it has the
[1100.36 → 1105.10] you know, it's going to kill one person or five people, or it's going to kill you or, or a woman
[1105.10 → 1109.94] with a stroller, like all that kind of stuff is where people, people's minds naturally go to.
[1110.02 → 1113.46] And I'm not saying that those are trivial issues, obviously, they're not. And when you get into
[1113.46 → 1118.86] things like autonomous weaponry, I mean, that's a whole other topic. But AI isn't a monolith.
[1119.34 → 1126.48] And so when we think about the both the benefit, you know, the innovation benefit, and the risks of AI,
[1126.48 → 1132.92] we have to think about it in a particular context. And that context could be something like a financial
[1132.92 → 1138.34] services context in which you're trying to manage risk, or it could be a diagnostic context in the
[1138.34 → 1144.22] healthcare industry. And so what I really think is important is for us to understand some of these
[1144.22 → 1151.82] nearer term issues, some of these very pragmatic, practical issues around what happens when we use
[1151.82 → 1158.22] algorithms to kind of abstract humanity. Just, you know, not that, you know, not that that's
[1158.22 → 1164.18] bad, per se, it's just that it has implications that we then have to deal with on the other end.
[1164.28 → 1169.86] And so this is part of responsibly learning to use the technology, just as we would responsibly
[1169.86 → 1174.20] learn to use any other technology that is extremely powerful.
[1174.20 → 1181.66] So Susan, as we are kind of talking about how about what ethics are in AI and how to apply them,
[1181.94 → 1187.02] which is very personal for me, as I've come into a new job in a new company, new industry,
[1187.10 → 1193.70] the defence industry, where we're looking at AI use cases, I think this is the first time in my life
[1193.70 → 1198.92] where I'm almost leading with ethics. And I think, you know, there are many other people that will be
[1198.92 → 1205.32] in similar situations could be because AI has such tremendous capabilities. What types of advice do
[1205.32 → 1212.48] you have for people who are moving into jobs or are now having to face how does AI affect our products
[1212.48 → 1216.44] and services at our company? What kinds of things would you advise them to do in terms of their
[1216.44 → 1218.62] thinking that maybe they haven't had to consider in the past?
[1218.90 → 1223.00] Yeah, I mean, I think there are a few very straightforward things. The first is to understand
[1223.00 → 1227.90] that algorithms are as good as the data, you know, this is like the classic garbage in,
[1227.90 → 1233.00] garbage out, right? The algorithms are only as good as the data and the way the data is modelled.
[1233.46 → 1240.68] And, you know, the data that we have in many cases is simply, it's just absorbed from society,
[1240.82 → 1245.70] right? You know, in the case of the Google Word2Vec or in the case of the Word2Vec data set,
[1245.70 → 1250.34] that includes all that language stuff that I mentioned earlier, you know, it just absorbs
[1250.34 → 1255.62] the reality that we live in. And sometimes you want to perpetuate and amplify that reality.
[1255.62 → 1260.24] And sometimes you maybe don't. So for example, if you're creating a segment, if you're a marketer,
[1260.30 → 1265.26] and you want to do audience segmentation to doctors, you don't want anything assuming that
[1265.26 → 1269.14] all doctors are male, right? You're going to alienate all those female doctors out there,
[1269.14 → 1275.64] and potentially even stifle the potential of younger female, you know, students who maybe want to get
[1275.64 → 1280.54] into the medical profession. So, so we just need to know these things. And we need to actually have
[1280.54 → 1287.74] processes in place to ensure that when we can and can fix and catch bias that we do, we can't change
[1287.74 → 1293.18] society, you know, by changing technology, obviously, but we can be mindful about it.
[1293.84 → 1300.14] The second thing is around explainability. So there's a woman, Rachel Bellamy from IBM,
[1300.14 → 1304.80] I heard her speak in London not too long ago. And she said, explainability is the new user interface
[1304.80 → 1310.36] for AI. And I thought that was a fascinating point. Because one of the things we're not used to
[1310.36 → 1316.88] in probabilistic systems is the idea that you put data in, and then there's the sort of black box,
[1316.88 → 1323.24] and then there's the output. And so in many cases, we do need to understand what some of these,
[1323.54 → 1328.32] you know what some of these decision criteria were, in some cases, it's fairly straightforward.
[1328.32 → 1334.20] You know, maybe there are a few kind of keywords that were determining the outcome or suggesting
[1334.20 → 1339.48] the outcome. And in some cases, for example, maybe with disease diagnosis, or with pharmacological
[1339.48 → 1345.26] types of use cases, it might be very, very complex, you know, or whether, you know, these very complex
[1345.26 → 1350.76] systems. So this idea of trying to understand the, you know, what happened between the input and the
[1350.76 → 1355.66] output is very important. So the people do have a sense of trust. You don't simply say, well, Chris,
[1355.66 → 1360.80] I'm not giving you a mortgage loan, even though you have, you know, financially pretty much the same
[1360.80 → 1366.38] profile as Daniel. And then three months later, you give Daniel the mortgage loan, even though he
[1366.38 → 1370.92] pretty much matched where you match, you have to be able to go back and understand what happened.
[1371.36 → 1377.36] You have to understand a little bit about what caused that action to be taken. So explainability
[1377.36 → 1382.24] is interesting. And it's also become kind of a huge issue in the industry. And I think there's a lot
[1382.24 → 1388.34] of controversy around it. And then the third piece is, you know, there needs to be an understanding
[1388.34 → 1396.24] that ethics in AI are simply just norms of behaviour. And we don't really have norms of behaviour in the
[1396.24 → 1401.10] digital world the way that we do in the physical world. You know not to push in front of somebody
[1401.10 → 1405.94] getting on a bus, you may do it anyway, but you know not to do that. We don't have those same norms
[1405.94 → 1411.84] in the digital world. And so having internal controls, making explicit the decision criteria,
[1412.00 → 1413.54] all those things are really important.
[1414.00 → 1417.76] I'm glad that you addressed that because that was actually going to be my next question is kind of,
[1417.88 → 1422.70] what do you need in place around it in terms of what you're calling internal controls,
[1422.90 → 1428.66] so that the burden isn't entirely on the individual that is trying to figure their way through this and
[1428.66 → 1435.54] apply ethics, you know, as they do that. From an internal control, do you need systems in kind of
[1435.54 → 1442.18] AI implementation that you might not have needed in other environments? And if so, you know, what
[1442.18 → 1445.90] might they need to be thinking about? What might those systems need to be addressing?
[1446.48 → 1452.50] Yeah, we do need systems. In some cases, it's like grandfathering existing processes and controls,
[1453.20 → 1456.98] you know, grandfathering AI into that. In other cases, it's entirely new,
[1456.98 → 1462.48] entirely new types of controls. So for example, some industry examples out there, AI Now,
[1462.58 → 1469.20] which is a really phenomenal organization focused on ethics and AI, they've issued what they're calling
[1469.20 → 1475.26] an algorithmic impact assessment, very similar to like an environmental impact assessment that when
[1475.26 → 1479.24] you're going to build something or excavate something that you need to understand the environmental
[1479.24 → 1483.40] impact. So this is built on that same premise that, you know, if you're going to introduce
[1483.40 → 1489.54] algorithms and algorithmic decision-making into, in this case, it's meant for governments and for
[1489.54 → 1494.36] cities, if you're going to introduce that into kind of civic environment that you need to think
[1494.36 → 1501.66] through some of those potential impacts to vulnerable people, to systems and processes and all those things.
[1501.66 → 1508.86] And so that document lays out kind of a template for assessing the impact of your algorithmic system.
[1509.44 → 1513.96] I think something like that can and should be customized for industry. That's one example.
[1514.34 → 1519.88] IBM has built a couple of things that are quite interesting. One is called a supplier declaration of
[1519.88 → 1526.06] conformity. So imagine, you know, as a defence contractor, or as a retail bank, or as a healthcare
[1526.06 → 1531.66] provider, you're not only using your data, but you're using data and systems from other organizations,
[1532.24 → 1536.02] other companies, you want to make sure that you've gone through the process of understanding
[1536.02 → 1540.94] and holding your systems up to the highest scrutiny. But you also want to make sure that
[1540.94 → 1545.78] your suppliers and vendors and partners have done the same thing. So that's another example.
[1546.14 → 1550.16] They've also built, you know, and this is, again, something that's a bit, I wouldn't say
[1550.16 → 1555.88] controversial, but it's open to scrutiny, this idea of a dashboard that shows kind of a bias
[1555.88 → 1562.66] quotient, right? So, and a confidence quotient. So as a simple example, if you're trying to
[1562.66 → 1567.88] settle a car insurance claims, you should know that the data that you have for 19-year-olds is
[1567.88 → 1573.52] very, very scant. Whereas the data that you have for like 42-year-olds is very, very rich.
[1574.02 → 1579.34] And so if you're settling a car insurance claim on a 19-year-old, you need to dig down into some other
[1579.34 → 1584.80] things and really probably use much more human intervention to understand what the situation was,
[1584.80 → 1591.08] simply because those recommendations are based on just, you know, less rich data. These are just
[1591.08 → 1595.80] some examples of things that people are doing. Microsoft is rolling bias check into Word and
[1595.80 → 1601.46] PowerPoint. So if you use a word that you're maybe not aware has some kind of connotation that is
[1601.46 → 1606.32] hurtful or unpleasant, it will let you know the same way to let you know if you misspelled a word.
[1606.58 → 1611.90] Yeah, that's fascinating. And piggybacking off of that for my own selfish reasons,
[1611.90 → 1616.96] I want to ask the next question because I've taught a few corporate workshops recently and
[1616.96 → 1622.28] we kind of, of course, talk about, you know, oh, you want to make your, you know, maybe you want
[1622.28 → 1627.14] to make your training set as representative of reality as you can. And then you try to optimize
[1627.14 → 1632.88] for accuracy or whatever it is. And then, you know, I bring up a bias and these issues that we're
[1632.88 → 1637.16] talking about. And we, in the midst of those discussions, I think every time I've done this,
[1637.16 → 1642.58] someone somewhere in the audience asked about like, well, if we include,
[1642.64 → 1650.48] you know, gender or zip code or income or whatever it is in our model, and it makes it more accurate,
[1650.48 → 1656.28] why wouldn't we want to do that? Isn't that just the accurate representation of reality,
[1656.28 → 1661.92] even though it produces a bias model? And I know kind of how I've tried to answer that question,
[1661.92 → 1667.84] you know, but I was curious your thoughts on how you would help that sort of person understand why
[1667.84 → 1675.56] they should care maybe about bias in their predictions and why they might want to consider
[1675.56 → 1679.80] that a little bit more seriously and not just talk about accuracy.
[1680.34 → 1684.38] Yeah. Well, Daniel, you've hit on, I think, one of the most crucial issues around algorithmic bias
[1684.38 → 1691.22] we're going to see in 2019. And that is there's a little bit of a storm brewing between some data
[1691.22 → 1697.52] scientists and engineers and sort of people, I'll just be brave here and say people like me who run
[1697.52 → 1703.82] around talking about AI ethics. And here's why it's really complicated. It's not, you know,
[1703.86 → 1708.60] and there is a tendency, and I've had this conversation with some data scientists, you know,
[1708.60 → 1713.92] who work at very well-known companies off the record. There's a tendency, I think, for some folks
[1713.92 → 1719.20] to kind of do a little social justice virtue signalling around, you know, these darn data scientists,
[1719.20 → 1722.82] says they don't understand people, and they don't understand humanity, and they're going to ruin the
[1722.82 → 1726.96] world by allowing bias to creep in. And, you know, then on the other...
[1726.96 → 1727.06] No biggie.
[1727.36 → 1727.98] Pardon me?
[1728.56 → 1729.22] No biggie.
[1729.52 → 1734.62] Yeah, no big, right? And then on the other side, we have data scientists saying, well, okay, so who,
[1734.62 → 1739.64] you know, elected you the arbiter of all that is good and just in the world? And these are both
[1739.64 → 1746.12] completely valid points of view. So here's where I stand on it. We do have to have this conversation
[1746.12 → 1752.42] with precisely the group of people that you're talking about productively. These industry
[1752.42 → 1757.42] conversations need to happen because as somebody who I'm not allowed to quote said to me not too
[1757.42 → 1764.64] long ago, who gets to choose who's the person who puts their finger on the scale? And that is really
[1764.64 → 1771.82] critically important because what we may ameliorate in terms of bias for one group, we may actually
[1771.82 → 1777.80] impact for other people or have unintended consequences that we're not even able to
[1777.80 → 1783.88] forecast. And I'll give you one simple example. Okay. So if you think about what happened with
[1783.88 → 1789.06] Amazon's recognition system, where it incorrectly identified John Lewis and six members of the
[1789.06 → 1795.02] Congressional Black Caucus as criminals, as matching faces in their criminal facial recognition
[1795.02 → 1800.80] database, you know, okay, that's like argue, it's not even arguably, that's unarguably bad,
[1801.04 → 1804.72] like bad, bad, bad, right? You know, we've got John Lewis is one of the greatest, you know,
[1804.78 → 1810.02] civil rights activists ever known to man, who is now basically along with six members of the
[1810.02 → 1814.58] Congressional Black Caucus, been matched to a criminal. If this happens to John Lewis, you know,
[1814.60 → 1816.80] you can only imagine what's happening to other people.
[1817.42 → 1821.32] Yeah. And similar with like the recidivism models and other things that I've seen.
[1821.32 → 1825.78] Okay. So here's the other side. And this is why is this because image recognition and facial
[1825.78 → 1832.86] recognition is really much less accurate at recognizing and understanding people of colour
[1832.86 → 1837.52] than it is in recognizing and understanding Caucasians. Okay. So how do you fix that?
[1837.86 → 1844.54] Do you make facial recognition better so that it better identifies people of colour? How are you
[1844.54 → 1848.70] going to get that data? Do you, do you, you know, start encouraging people? No, no, no, really. It's,
[1848.70 → 1854.92] it'll be great for you. Just, just give us your face data, you know, let us, let us analyze your
[1854.92 → 1860.22] face data, you know, and put you in our system. We promise that will just help in terms of accuracy.
[1860.22 → 1865.66] It won't have any, you know, bad impact on you. Like this is a really, you know, who's going to say
[1865.66 → 1871.30] yes to that. Right. And so this is, you know, some people will say, you know, we're, we're perfectly
[1871.30 → 1877.50] happy, you know, that the false positive rate is so high. Like just let it stay high because, uh,
[1877.50 → 1883.06] we don't want to be included in those systems. And, you know, there are absolutely valid reasons
[1883.06 → 1888.26] for that. So, you know, this stuff is not easy. And one thing I would say is I don't stand on a
[1888.26 → 1894.06] soapbox, you know, trying to say I'm more ethical than anyone else. I am cowed every single day by how
[1894.06 → 1897.64] complicated this stuff is. I just feel like we have to have these conversations.
[1898.48 → 1903.02] Yeah. I appreciate your perspective there. I agree that the discussions are, are complicated
[1903.02 → 1908.18] because oftentimes immediately after I have that conversation and people are like, Oh,
[1908.22 → 1913.12] well, we'll remove the gender column in our data set or whatever. But if there's, you know,
[1913.18 → 1919.34] 1200 other features, who's to say that the, the model can't infer gender from, you know,
[1919.38 → 1926.76] from those other features. So it's not just a like take all the sensitive data out sort of thing.
[1926.96 → 1930.74] Yeah. And zip code, my God. I mean, there's no better predictor of your race than your zip code.
[1930.74 → 1935.92] And there's no better predictor of your health outcome than your zip code, not even your genome.
[1936.78 → 1941.48] So there is a way in which people could say very disingenuously, Oh, well, we just, you know,
[1941.50 → 1945.70] we didn't, you know, we didn't include race. Race isn't a fact. We can't do that. It's a protected
[1945.70 → 1951.62] class. And, you know, and then, but we just chose zip code, you know, like you, so this is why we all
[1951.62 → 1956.32] need to be educated about these things, right? The business people need to be educated about proxy data
[1956.32 → 1963.06] data. And data scientists need to kind of game out and scenario plan some of this stuff,
[1963.06 → 1968.60] or at least be part of that conversation. And we have to get past, you know, virtue signalling and
[1968.60 → 1972.20] actually into some real methodologies that people can get behind.
[1972.20 → 1976.00] Yeah. At least monitoring for bias at the least.
[1976.38 → 1980.52] Yeah. And that's hard too, actually, because, you know, who wants to be liable for that?
[1980.52 → 1986.28] Yeah. So as if this isn't complicated enough, trying to take all this into consideration,
[1986.80 → 1991.26] we now have the reality of regulation and stuff coming into it. Obviously, in Europe,
[1991.26 → 1996.66] you have the general data protection regulation, which we call GDPR for short. And when you throw
[1996.66 → 2002.64] that in the mix with all the other complications of trying to be ethical in your use of AI,
[2003.10 → 2008.22] how does regulation impact that? You know, there's, it seems like there's quite a balancing act that you,
[2008.22 → 2011.62] that a practitioner is trying to manage through this process.
[2011.74 → 2016.92] Yeah. I mean, you know, GDPR is fascinating. Interesting is probably a diplomatic word. I mean,
[2017.16 → 2023.90] I will say I am a huge fan of GDPR as a philosophy, right? Because, and yesterday, as a matter of fact,
[2023.90 → 2028.80] was the 70th anniversary of the UN Declaration of Human Rights that came out of World War II. And,
[2028.80 → 2032.76] you know, Eleanor Roosevelt was involved in crafting that. And the whole point
[2032.76 → 2041.08] really was to protect the civil rights of individuals, protect their rights from unreasonable search and seizure,
[2042.14 → 2047.58] and from discrimination and disenfranchisement and actually, you know, physical harm, all these things, right,
[2047.72 → 2053.74] coming out of the Second World War. And GDPR is really built on the UN Declaration of Human Rights,
[2053.82 → 2058.72] but from a digital standpoint, right, so that we should be in control of our own data. We should know
[2058.72 → 2063.66] when algorithms make decisions about us, why those decisions were made and be able to contest them.
[2063.98 → 2069.50] And so from a philosophical and historical viewpoint, it's critically important. However,
[2069.84 → 2075.88] most of us experienced GDPR in the weeks and months leading up to May 25th of this year,
[2076.06 → 2082.60] as an onslaught of horrific opt-in emails, and like then not being able to get to a couple of,
[2082.66 → 2088.20] you know, websites that we usually frequent, and not a lot more than that. So, you know,
[2088.20 → 2094.68] there's theory and practice. There's the fact that GDPR and its enforceability is a bit of a gray area
[2094.68 → 2099.34] for global company. I mean, if you're global, of course, you have to comply just in case people do
[2099.34 → 2107.36] wander into the EU. But, you know, fundamentally, with regulation around technology, it is always so
[2107.36 → 2113.62] far behind the reality of the technology. You know, we're still literally in the wake of the 2016
[2113.62 → 2119.18] election, we're still literally grappling with, you know, is Facebook a magazine or a magazine stand?
[2119.40 → 2126.72] I mean, that's the law this is based on. And so when you think about it in those terms,
[2127.04 → 2132.66] I mean, yes, there does need to be protection. What protection? I am not an expert on that.
[2132.66 → 2140.12] So I guess as we start to come to the end, I want to pose it, and I'm trying to not scope this final
[2140.12 → 2144.84] question too big. I know in this paper that you've just put out, you kind of finish up by kind of
[2144.84 → 2152.04] taking practitioners through how to build up their playbook. With that in mind, maybe if you could just
[2152.04 → 2157.64] kind of give us some pointers or some starting tips on how you might start that process, recognizing
[2157.64 → 2162.98] that our listeners should definitely go download the playbook that you're offering on how to build
[2162.98 → 2166.66] their own playbook. But what are some good finishing points where you can leave them with
[2166.66 → 2171.12] to get started on that process? Yeah, I mean, what I've published is really a meta playbook,
[2171.20 → 2177.26] right? It's a playbook for a playbook, as you just said. And part of that is that as a, you know,
[2177.30 → 2182.30] as an analyst firm, we publish our research for free as a service to the industry. So this is really
[2182.30 → 2187.28] intended to help people think through the issues that they need to think through in order to do what
[2187.28 → 2191.22] they need to do. And of course, you know, I'd probably be beaten around the head and shoulders
[2191.22 → 2195.86] if I didn't say that I'm more than happy to help with that if people need that. But there are five
[2195.86 → 2200.74] areas that I think are really critically important. The first is looking at your business strategy,
[2200.98 → 2206.66] you know, moving from kind of optimizing existing processes to actually, you know, business model
[2206.66 → 2211.98] innovation, customer experience, and using intelligent systems to enable those things. You know,
[2211.98 → 2216.66] in data science, you know, we're moving from kind of specialty or an exotic, you know,
[2216.70 → 2221.88] an exotic specialty within organizations to the ability to scale. With product and service development,
[2221.88 → 2228.92] we're moving from kind of reactive, you know, taking in all the signals that, you know, about what's
[2228.92 → 2233.20] happened in the past to anticipatory, trying to anticipate what's happening. You know, we're finally
[2233.20 → 2239.36] getting to what we were promising for the last 20 years or an agile enterprise. From an organization and
[2239.36 → 2243.98] culture perspective, we don't talk about this enough. But, you know, we're moving from a hierarchical
[2243.98 → 2249.16] to much more dynamic organizational culture. And when you have agile development in an organization
[2249.16 → 2254.30] and agile mindset, it really changes the way people work together. And some people don't like that very
[2254.30 → 2260.48] much. And some people are highly empowered. And that makes a lot of difference in terms of how
[2260.48 → 2267.18] successful AI can be. So one major piece of that is, you have to have the willingness to fail
[2267.18 → 2273.26] and fail fast. And that doesn't mean move fast and break things because, you know, that's probably
[2273.26 → 2280.30] a relic of the last 10 years. But it does mean actually the ability to move in tandem very quickly,
[2280.82 → 2285.62] learn from mistakes and keep moving because that's just the essence of these systems.
[2286.14 → 2292.52] And then finally, it's around ethics and governments. We're not in the anything goes era anymore. We've seen
[2292.52 → 2297.80] in the last year tremendous stories about what happens when we don't pay attention to these issues.
[2298.16 → 2303.70] We do have to start thinking about the ethics and the customer experience of AI in a much more
[2303.70 → 2309.78] rigorous way. And, you know, as we talked about earlier, that's not the easiest thing to do. But
[2309.78 → 2314.84] at least there's some early thinking in here about how to start to frame those conversations internally.
[2315.50 → 2318.24] I really appreciate it. I love what you've done with this.
[2318.24 → 2324.90] For our listeners, we will have a link to the AI maturity playbook with pillars of enterprise success,
[2324.90 → 2330.68] five pillars of enterprise success in the show notes. And Susan, if people read through that,
[2330.72 → 2334.54] and they want to engage you so that you can come in and help their organization,
[2334.98 → 2337.14] how would they do that? How would you like people to reach out to you?
[2337.42 → 2342.30] Yeah, I'd love to hear from people. You can so most directly, you can email me at Susan at
[2342.30 → 2347.72] altimetergroup.com. You can connect with me on LinkedIn. I'm S. Ettinger on LinkedIn.
[2347.72 → 2352.14] And or I'm sorry, I'm S. Ettinger on Twitter. And obviously, Susan Ettinger on LinkedIn.
[2352.50 → 2353.26] I'm easy to find.
[2353.90 → 2357.50] Bye. Great. Thank you very much for coming on the show. This was a great conversation.
[2357.96 → 2363.14] I so wish I had heard a conversation like this before I was getting started in industry. So I
[2363.14 → 2368.24] think you're really helping some people that are still trying to get in and get their organizations
[2368.24 → 2372.12] involved in this and thinking about it the right way. So thank you so much for coming on the show.
[2372.38 → 2375.16] It's my pleasure. Thank you both so much for having me.
[2375.16 → 2378.76] All right. Well, thank you very much. And Daniel, I will see you in the next show.
[2379.08 → 2380.12] Bye. Bye-bye.
[2380.12 → 2387.02] All right. Thank you for tuning into this episode of Practical AI. If you enjoyed the show, do us a
[2387.02 → 2391.82] favour, go on iTunes, give us a rating, go in your podcast app and favourite it. If you are on Twitter
[2391.82 → 2395.34] or social network, share a link with a friend, whatever you got to do, share the show with a
[2395.34 → 2399.82] friend if you enjoyed it. And bandwidth for changelog is provided by Vastly. Learn more at
[2399.82 → 2404.06] fastly.com. And we catch our errors before our users do here at changelog because of Rollbar.
[2404.06 → 2409.50] Check them out at rollbar.com slash changelog. And we're hosted on Linde cloud servers.
[2409.82 → 2414.86] Head to linode.com slash changelog. Check them out. Support this show. This episode is hosted by
[2414.86 → 2420.28] Daniel Whiten ack and Chris Benson. Editing is done by Tim Smith. The music is by Break master
[2420.28 → 2425.42] Cylinder. And you can find more shows just like this at changelog.com. When you go there,
[2425.50 → 2430.28] pop in your email address, get our weekly email, keeping you up to date with the news and podcasts
[2430.28 → 2435.10] for developers in your inbox every single week. Thanks for tuning in. We'll see you next week.
