[0.00 → 8.66] Welcome to Practical AI.
[9.16 → 19.54] If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.24 → 24.92] Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 → 35.44] Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents, so you can launch your app near your users.
[35.84 → 37.84] Learn more at Fly.io.
[42.74 → 47.38] Welcome to another episode of the Practical AI podcast.
[47.38 → 52.28] This is Daniel Whiten ack. I am founder and CEO at Prediction Guard.
[52.28 → 59.70] I'm joined as always by my co-host, Chris Benson, who is a Principal AI Research Engineer at Lockheed Martin.
[59.98 → 60.62] How are you doing, Chris?
[60.94 → 62.78] Doing good, Daniel. How's it going today, man?
[63.10 → 69.64] It's going great. I just landed in Boston and you were texting me, and you're like,
[69.64 → 74.56] Hey, Demetrius from the ML Ops community wants to hop on and record an episode.
[74.56 → 76.90] And I was like, I've got to get out of this train station.
[76.90 → 84.02] So I just found the nearest stop and got out, and I don't have my normal setup, so I probably sound weird.
[84.02 → 87.84] But I was like, these are the best times when we get to have our friend Demetrius on.
[88.18 → 88.80] How's it going, man?
[89.10 → 90.76] You guys can't get away from me.
[90.88 → 94.70] I've blackmailed your boss into letting me come back on here.
[95.56 → 96.76] Standing invitation.
[97.22 → 97.68] Absolutely.
[98.26 → 99.76] What's up, man? How are you doing?
[99.76 → 105.08] I'm so excited because I try not to abuse this standing invitation.
[105.08 → 107.66] I had a great time the last time I was on here.
[107.80 → 115.80] We had a bunch of laughs and a lot of people reached out to me because we had, you know, this rag versus fine-tuning conversation.
[115.80 → 120.24] And I think things have kind of like the pieces have fallen.
[120.48 → 121.42] The cookies have crumbled.
[121.68 → 124.80] It feels like fine-tuning is not as popular as it was.
[124.80 → 129.90] I don't know what you all are seeing out there, but rags are the go-to in these days.
[130.20 → 131.02] Yeah, that's what I'm saying.
[131.14 → 133.06] Everyone's ragging each other all over the place.
[133.90 → 149.76] And I think, yeah, along with that, there's sort of like, in my mind, has developed this category of like, so there was rag, which of course you're augmenting the generative model with data, but not in the way that like people typically think of fine-tuning.
[149.76 → 169.94] You're just doing retrieval, but I think also these other sort of workflows around calling external tools or like the neurosymbolic stuff that we're seeing of like combining a rules-based algorithm or function or traditional quote unquote machine learning algorithm with generative models, maybe to get the inputs.
[169.94 → 186.20] And then like connections to databases, all these different ways, like it kind of seems like people are figuring out that generative models are great at being kind of assistants and automatons, but not necessarily like predictors, right?
[186.28 → 192.00] Or other kind of functions to like analytics types of things and that sort of stuff.
[192.44 → 197.10] I've noticed there's been a new term coined, at least for me, rag as a service.
[197.18 → 198.44] Have you guys run across that?
[198.44 → 202.22] Rag as a service is now like a thing.
[202.48 → 204.42] Is that acronym just rag?
[205.08 → 205.32] Rag.
[205.60 → 206.40] Sort of.
[206.46 → 206.64] Rag.
[208.16 → 209.14] Don't even try.
[209.34 → 211.88] You're just going to strain the vocal cords if you do that, man.
[212.62 → 212.76] Yeah.
[212.80 → 213.92] Rag as a service.
[214.12 → 214.78] We'll rag you.
[215.04 → 216.70] If you bring your thing, we're going to rag you.
[216.74 → 217.74] We're going to rag you all over the place.
[217.78 → 217.90] Yeah.
[218.62 → 228.42] Well, I think what you're saying, Daniel, it really speaks to something that I've been seeing too, which is the maturity in the last, whatever, six months.
[228.44 → 238.90] It's become very clear that there's traditional ML workloads and use cases that are kind of going to always be traditional ML workloads.
[239.00 → 244.56] You think about like your fraud detection models or like the term prediction or the recommender system even.
[244.56 → 250.16] And then you have your generative AI workloads or use cases.
[250.34 → 258.70] And that's something like these like transcription, or you have the LLMs, which are doing all sorts of stuff.
[258.70 → 267.22] But rags are probably the biggest ones in that where you get that copilot or code generation, I think, is a huge one.
[267.70 → 278.44] There's not like such a big overlap where you're saying, OK, the generative AI use cases or the generative AI models are going to dethrone the traditional models.
[278.92 → 279.48] I agree with that.
[279.58 → 279.78] Yeah.
[279.78 → 281.78] Definitely different use cases.
[282.04 → 288.46] I think one thing we had our first Gen AI mastery webinar with the podcast.
[288.78 → 289.78] When was that, Chris?
[289.82 → 291.50] A couple of weeks ago or something like that.
[291.58 → 291.72] Yeah.
[291.80 → 300.48] We were talking about text to SQL specifically and that, you know, analytics like SQL is perfect at doing analytics, right?
[300.48 → 304.24] Especially descriptive analytics and aggregations and all of that.
[304.48 → 316.98] And it just doesn't make any sense for you to take a big table and somehow figure out how to dump its contents in a prompt and have a model reason over it because it's probably going to get it wrong anyway.
[317.24 → 323.56] But also there's this existing tool which can be called, which is really awesome at doing those things.
[323.56 → 343.66] I love the idea and the exploration that's happening right now on how can we merge both of these worlds and how can we see what different parts work well together and which combination of the traditional ML plus the generative AI can go together.
[344.08 → 349.70] And I know that you do a series of surveys with the ML Ops community.
[349.70 → 359.92] I think the last time that we talked, we were talking about some of your survey work and some of the interesting findings, but I think you've gone through other iterations of this, right?
[360.06 → 366.10] So are you seeing interesting things pop up as the community around this technology matures?
[366.84 → 372.80] So 100%, and I just come on here when I got survey insights to share, I guess.
[373.20 → 374.42] That's what I'll be known for.
[374.42 → 380.12] Whenever we have a nice survey of AI, I'll come and share it with you all.
[380.22 → 391.86] But this one is cool because this time, so we did an evaluation survey, and we launched it when we had our virtual conference, which had a huge turnout.
[392.00 → 393.58] It was over two days span.
[393.78 → 394.88] Which was awesome, by the way.
[395.16 → 395.62] It was great.
[395.70 → 397.90] You were part of one of the past ones, right?
[398.24 → 400.46] And Daniel, you had an awesome spot.
[400.46 → 407.16] But the two-day span, we tried something different, and we said, what if we do two days, but since it's virtual, nobody has to fly anywhere.
[407.66 → 416.74] So instead of you trying to watch a live stream for eight hours a day on a Thursday and then a Friday, why don't we just do two Thursdays in a row?
[417.42 → 425.88] And then you don't have to feel like, wow, I just had 20%, 30% of my week eaten up by that eight-hour live stream or 16-hour live stream.
[425.88 → 429.92] Now you can tune in, tune out on a Thursday of your choosing.
[430.22 → 431.36] But we launched it there.
[431.90 → 440.70] And the response has been amazing because normally maybe we'll get like 100, 150 people that will fill out the survey.
[440.84 → 448.38] This time we had 322 is the number of these, which is super cool to see.
[448.38 → 453.22] And so let me give you some of the clear insights.
[453.36 → 457.86] One, there's budget being allocated towards AI these days.
[458.00 → 460.08] I don't think that's going to surprise anybody.
[460.74 → 468.60] The fascinating part is that like 45% of the respondents said that they're using existing budget.
[468.82 → 476.34] And then a whole like whopping 43% here said, no, we're using a whole new budget.
[476.34 → 483.24] So you've got exploration happening in generative AI like never before.
[483.24 → 500.86] But when it comes to that, one other takeaway has been that like the Flops, AI, ML engineers, they're really trying to figure out what the biggest leverage use cases are and how they can explain that.
[500.86 → 506.76] And I think what we're seeing is there are a lot of companies that are open to the exploration right now.
[507.14 → 510.62] And they're open to letting people say, all right, cool.
[510.76 → 515.28] What is the most valuable for our teams and our company?
[515.56 → 518.52] Is it a chatbot that is an internal chatbot?
[518.62 → 520.46] Is it an external chatbot?
[520.62 → 522.20] What does that actually look like?
[522.24 → 523.10] What is the use case?
[523.76 → 524.36] It's kind of funny.
[524.36 → 533.74] We actually talked about that a little bit last week, Daniel and I did, in terms of trying to get non-technical people engaged in it.
[533.94 → 538.16] And I think that there are organizations all over the world right now that are doing exactly that.
[538.26 → 545.70] To your point on the result that you're seeing, there's a lot of effort and a lot of money being thrown at how do we start doing that.
[545.70 → 551.52] And it's all really like the shining star here were just rags.
[551.78 → 553.46] Obviously, it's very clear.
[553.56 → 555.10] Everybody's using rags.
[555.30 → 561.88] And the participants self-identified as being intermediate in rags.
[561.96 → 562.74] That was the majority.
[563.30 → 569.80] So we had like 31% saying that we have some experience with LLMs and rags.
[569.80 → 578.50] And then you only had 6% saying we are at the frontier of LLMs and rag model innovation.
[590.92 → 591.96] What's up, friends?
[592.06 → 594.70] There's a new book out there called The Hacker Mindset.
[594.70 → 604.74] This is a productivity cheat code to unlock new levels of success in your career, in your creative pursuits, and in your personal growth.
[605.14 → 611.54] This book is about leveraging the principles of white-hat hacking and applying those skills to the broader world.
[611.96 → 613.56] It's available for pre-order right now.
[613.80 → 615.92] And it's not your typical productivity guide.
[616.16 → 622.36] This is written by Garrett G., a seasoned white-hat hacker with over 20 years of experience.
[622.36 → 629.20] This book reveals the secrets of hacking and how you can apply those skills to overcome obstacles and achieve your goals.
[629.66 → 633.38] So don't miss your chance to get ahead and get this book, The Hacker Mindset.
[633.74 → 637.36] You can pre-order your copy today at thehackermindset.com.
[638.38 → 642.98] Be among the first of many to tap into this power of hacking for your success.
[643.40 → 646.16] Join the movement and embrace a new way of thinking.
[646.54 → 649.36] Again, that's thehackermindset.com.
[652.36 → 663.22] So let me ask you guys a question.
[663.38 → 665.98] I get some opinions going here on that.
[665.98 → 680.82] Do you think, you know, with all of these assistants and chatbots and all the other kind of, you know, focus things in Gen.AI, with those using RAG, do you think those are for more kind of general use cases having some domain knowledge in?
[681.00 → 693.70] And do you think that maybe going back to the last time we had you on the show when we were talking about fine-tuning, do you think that kind of highly specialized fields will still stick with fine-tuning instead of RAG?
[693.70 → 701.44] Do you think, in other words, the degree of expertise required, if you will, to get a job done productively?
[701.54 → 705.50] Do you think that makes a difference on whether you go RAG or fine-tuning?
[705.68 → 707.08] Or do you think it has nothing to do with that?
[707.56 → 709.80] I would love to hear what Daniel has to say in a minute.
[709.80 → 715.72] But I've heard something said about like fine-tuning is for form.
[715.90 → 730.36] So if you're trying to get a different form on the output, or for example, if you're trying to get functions and the whole basically like GPT functions are a perfect example of this.
[730.36 → 737.18] So if you're trying to get a homegrown model to do that type of thing, then fine-tuning makes sense.
[737.30 → 751.56] Otherwise, it's not necessarily the good call because unless you're using a very small model, I think is the thing there that, okay, what's the trade-off that you're doing?
[751.56 → 771.16] And the other thing that is probably worth talking about when it comes to like the difficulty levels that I've seen is people that want to go and do use a small model, a small like domain specific model that is distilled, or it is very fine-tuned and distilled.
[771.16 → 777.76] And it's on their own in their own infrastructure and in like they need a whole team to support that.
[778.08 → 779.80] That's like hard mode.
[779.92 → 784.78] You're playing on hard mode, and you contrast that with just a GPT for call.
[785.00 → 789.22] That's a whole different level of the game that you're playing.
[789.44 → 792.16] And so I kind of look at it that way.
[792.24 → 799.34] Like how much are you willing to trade off when you're trying to figure out is this the way forward?
[799.76 → 800.54] I would agree with that.
[800.54 → 811.18] I think the only thing I would add is there is still, at least as far as I've seen with our enterprise customers, like an inclination that they need to fine tune.
[811.60 → 816.14] Like that's still a kind of general like, oh, we need to do that at some point.
[816.74 → 825.78] And I think once they kind of solve a few of their use cases without that, they kind of disillusion themselves of that notion in many cases.
[825.78 → 844.60] But the good thing, like you're saying, Demetrius, is like you can probably prove to yourself without a huge amount of effort using an easy-to-use API, whether you'd need fine-tuning and do that in like a day versus like just immediately going to jump to fine-tuning.
[844.60 → 850.12] And how do we get GPUs, and how are we like what model server are we going to use and all of that stuff?
[850.36 → 853.96] Like you say, that gets very much into hard mode very quickly.
[853.96 → 858.06] And you don't sort of need that to validate your use case often.
[858.06 → 873.58] And even if you do fine-tuning, sometimes it may be down the line when you've been running the pre-trained model for quite some time, and you actually have a good prompt data set to fine tune with because most people don't start out with that either.
[874.20 → 875.46] That's a huge point, too.
[875.46 → 890.56] And this is probably like the biggest unlock that happened is that, OK, now that anybody can use the OpenAI API, you can quickly see if there's value in that crazy idea you have.
[890.80 → 897.46] And then you can go down the line like, all right, now I'm going to use an open source model, which is turning the knob to something harder.
[897.46 → 899.70] Or maybe it's not even using an open source model.
[899.80 → 903.94] Maybe it's just like, can we get the same results with a smaller model from OpenAI?
[903.94 → 907.64] So instead of GPT-4, we're going with 3.5 Turbo.
[907.90 → 911.70] Can we then go to an open source model and get the same results?
[911.86 → 919.62] Like I almost look at it like a spectrum of how difficult you want to make your life and how much upkeep you're going to need and all of that.
[919.76 → 925.56] But as with everything, there are benefits if you go to that very small model if you need it.
[925.78 → 930.06] And you just have to really like to play out and see if you actually are going to need it.
[930.06 → 937.92] Speaking of another survey, just to make it an increasingly survey-driven show.
[938.82 → 941.24] I don't know if you saw the...
[941.24 → 942.12] Survey says.
[942.34 → 943.74] Yeah, survey says.
[944.28 → 950.80] The Andersen Horowitz post that they did another sort of survey, which was kind of interesting.
[950.80 → 957.88] And part of what they drew out, I forget the range of participants that participated in the survey.
[958.00 → 959.24] We can link it in our show notes.
[959.68 → 961.70] I was just posted March 21st.
[961.88 → 965.02] We're recording this maybe a little more than a week later.
[965.70 → 967.72] And it was about enterprise.
[968.06 → 972.46] So 16 changes to the way enterprises are building and buying generative AI.
[972.46 → 982.38] And one of the things that they specifically highlight there were enterprises are moving towards a multimodel future.
[982.68 → 989.04] And specifically a multimodel future driven at least partially by open models.
[989.32 → 1001.62] And so I think the other kind of interesting trend that you're seeing is they have like graph with like how many model providers are people using per company or whatever.
[1001.62 → 1005.76] And you see like three, four, five, like in many cases.
[1006.06 → 1009.18] And also a high adoption of open models.
[1009.18 → 1016.06] And I think what they're trying to draw out is like some of that is maybe driven by security, privacy things.
[1016.06 → 1020.20] But I think also it's driven by like control and flexibility.
[1020.98 → 1030.14] And once people start realizing, I also find it still a pretty big misunderstanding that people have that all of these models sort of behave the same.
[1030.14 → 1035.82] And in reality, pretty much every model has a character of its own and a specific behaviour.
[1036.40 → 1049.52] And even just switching from open AI to an open model for like text to SQL, for example, a model that doesn't do other things well, but does that really well can prove to be really useful.
[1049.52 → 1051.90] Or maybe it's a specific language thing.
[1051.90 → 1056.66] Like we're doing a Mandarin chat right now with one of our customers.
[1056.94 → 1071.00] And so whether it's language or whether it's task, people are, I think, finding out that their future is multimodel or multimodel provider or whatever, mainly because of that behaviour thing.
[1071.00 → 1080.12] But also because they can have some control over when they use this model or when they use that model and kind of create the mix that's right for them.
[1080.12 → 1093.88] And that's kind of a way it's like a route around fine-tuning in some ways, because you can kind of assemble these reasoning chains, even with multiple models involved that do very specialized tasks.
[1094.60 → 1104.58] And that can kind of help you avoid spinning up and running your own fine tune that does this very, you know, unique reasoning workflow.
[1105.06 → 1109.48] You can kind of bring all the experts and bring all the expert models and to help you.
[1109.48 → 1114.66] I can't help but wonder, you know, like that's a built-in capability that you have at Prediction Guard.
[1114.82 → 1120.08] But I think that there's a maturity issue there with a lot of organizations on getting to that point.
[1120.28 → 1133.88] And so what I'm seeing is very mature organizations are going exactly to that, having multi-models capabilities, and they have the ability to distinguish between which models they should use for which circumstances.
[1133.88 → 1147.40] I suspect, and maybe there's some survey data on this, but I suspect that that's still a fairly small group of even enterprise organizations that have gotten to that level of understanding of what they can do.
[1147.52 → 1155.48] And I think there's a spectrum falling off from there that the bulk of the world is in right now in terms of trying to figure out how to make it work for them.
[1155.48 → 1158.64] Let me twist some statistics to play in your favour.
[1158.80 → 1159.08] Hold on.
[1159.18 → 1160.38] I'm going to crunch some numbers.
[1160.58 → 1161.06] I love it.
[1161.36 → 1161.76] Live.
[1162.36 → 1164.96] You're probably not using an AI model to do it.
[1165.36 → 1165.42] No.
[1166.42 → 1174.02] I'm going to weave that narrative that you've got, Chris, and I'm going to go with it with the survey data as you were asking for.
[1174.02 → 1187.82] No, but actually, the biggest question, as you guys are talking about this, that goes on in my head is, you know what engineers really do not like, and I think it makes them very anxious, is having a single point of failure.
[1188.42 → 1201.26] And so if you are relying on OpenAI's API and you have a lot riding on that, where does that all go if the CEO gets ousted?
[1201.26 → 1213.92] And so I imagine that a lot of people thought twice after there was that big drama that happened and people started thinking, you know what, maybe we should try and have a few redundancy options just in case.
[1214.10 → 1225.88] Now you do have to have a bit more maturity to say, okay, I can't use the same prompt as I always use, so I have to have this prompt suite or prompt tests or prompt templates.
[1225.88 → 1233.88] And I think that's another thing that's happened since the last time we talked when we had the conference to try and get people to...
[1234.50 → 1236.34] Well, prompt ops is one.
[1236.66 → 1238.06] Agent ops is another one.
[1238.26 → 1241.88] But I created a song called Prompt Templates.
[1243.00 → 1245.30] And I'll put it in the...
[1245.30 → 1246.94] Maybe we could play it real fast.
[1246.94 → 1269.78] Love you, baby.
[1269.78 → 1299.76] As someone who's in kind of the defence industry, I'm for agent ops because it sounds bad, doesn't it?
[1299.76 → 1306.70] Oh, I thought you were going to say you were for prompt songs, which would bring smiles to people in the defence industry.
[1306.70 → 1307.84] That's what I was hoping to do.
[1308.04 → 1308.48] Exactly.
[1309.04 → 1310.24] Missed out on that one.
[1310.60 → 1315.06] But he is, I don't know if people can see this, but he's got a wonderful shirt on.
[1315.32 → 1316.34] That is for sure.
[1316.98 → 1321.28] And being in the defence industry, I don't know how you can get away with that.
[1321.96 → 1322.98] Work from home.
[1323.82 → 1325.80] Work from home is how I get away with it.
[1325.80 → 1334.50] And for those that aren't watching his shirt, it says, I hallucinate more than ChatGPT, which is a classic shirt.
[1334.78 → 1336.76] Which Demerit sent to me, I have to say.
[1336.84 → 1337.74] So thank you very much.
[1337.78 → 1338.44] I love this shirt.
[1338.66 → 1339.66] I love that you wear it.
[1339.72 → 1341.42] That is what I'm very happy with.
[1341.42 → 1348.86] But the other thing that I wanted to mention the survey, and then we can move on and keep talking about other stuff of the day, topical issues.
[1348.86 → 1359.92] But the data that people use and the data with which we evaluate the output, it seems like people just don't know what's going on there.
[1360.18 → 1361.54] We haven't figured that out yet.
[1361.60 → 1362.52] There's no consensus.
[1363.00 → 1364.24] It's not really clear.
[1364.24 → 1373.42] And like the classic data sets or the classic evaluation pieces that you use, they don't really hold up.
[1373.58 → 1381.82] So everyone's got to be having their own data that they've created and that they're testing against the output.
[1382.02 → 1385.94] But it's really hard to do that at scale, right?
[1385.98 → 1388.08] And it's really expensive also.
[1388.08 → 1395.84] So that's what we saw in the evaluation data or the evaluation survey data is that you've got to handpick these.
[1395.96 → 1396.98] You've got to match them up.
[1396.98 → 1398.82] And it's human curated.
[1398.82 → 1410.64] The testing data sets that you create, we had 42% are using data that they've created as their data sets to evaluate if the model is working or not.
[1411.12 → 1411.74] Yeah, that's crazy.
[1412.02 → 1413.60] And you mentioned expensive.
[1413.60 → 1418.66] It could be monetary, but it could also be a sort of iteration time too.
[1419.16 → 1428.94] Typically, like when we were back when we were creating machine learning models, which lots of people still do because it's the thing driving basically all the predictive stuff.
[1429.58 → 1433.34] But, you know, you could run your model and evaluate it.
[1433.82 → 1438.66] Maybe it took a few seconds, but, you know, a couple of minutes.
[1438.66 → 1453.14] But here, when you're thinking about running, especially against an API that has like variable latency or maybe the calls, each execution of your prompt chain is taking like 15 seconds.
[1453.14 → 1464.18] And even if you want to run that over like 100, 200, 300 example reference inputs, all of a sudden your iterations become really, really slow.
[1464.52 → 1476.18] That's something I've noticed that people kind of struggle with is really making their evaluation quick enough that they can iterate, feel like they can try a lot of things.
[1476.18 → 1487.36] Even if they have like a big budget to try a lot of things, this kind of iteration time is really frustrating also because maybe there's other people that are involved that aren't technical.
[1487.86 → 1488.08] Right.
[1488.14 → 1492.36] And they don't want to think about like concurrency and Python.
[1492.74 → 1492.92] Right.
[1492.98 → 1495.98] They just want to go into an interface and like try some stuff.
[1496.72 → 1501.14] And yeah, so you've got all of these things mixed together, which make it a bit of chaos.
[1501.14 → 1502.48] And in many cases.
[1502.48 → 1503.88] That's so true.
[1504.08 → 1511.50] The iteration speed, the time, the mean, we see here that this is crazy.
[1511.70 → 1516.68] 72% of ground truth labels were manually labelled by humans.
[1516.92 → 1523.14] And so to have to go and do that and then also how often are you doing that?
[1523.24 → 1528.22] How like there's so many questions and so many unknowns for what the best practice is.
[1528.22 → 1538.66] That's one thing that came up on the challenges is that it's just like a lot of people called out something that we synthesized into lack of guidance.
[1539.22 → 1541.72] Like nobody's saying this is the best practice.
[1541.82 → 1547.38] This is what we've seen works really well for us because maybe some people say, well, this worked well for us sometimes.
[1547.94 → 1551.60] And you can try it and see if it works well for you too.
[1551.72 → 1553.66] That's kind of the state of the industry right now.
[1553.66 → 1553.70] Yeah.
[1554.18 → 1557.76] There's something I want to tie back into something else that we've been talking about lately.
[1557.76 → 1560.68] And that is the fragmented nature of the community.
[1560.68 → 1566.14] And it's another thing Daniel and I have talked about recently is that we do have communities, but we have multiple communities.
[1566.14 → 1573.04] And in many cases, not in your case, but in many cases, they're very platform dependent, you know, vendor specific.
[1573.68 → 1581.52] And it makes it compared to a lot of programming languages, it makes it harder for people to come in and find specific best practices.
[1582.30 → 1586.78] So I'm actually not at all surprised to hear the survey kind of playing that out.
[1586.88 → 1592.22] I think that that's kind of a natural fallout of the challenges that we're having with community in general.
[1592.22 → 1604.56] So in my understanding this correctly, it's like because a lot of the communities are being built around certain tools, you have the best practices for those tools, but not necessarily for the industry.
[1604.56 → 1607.18] You can't generalize those best practices.
[1607.78 → 1607.88] Yeah.
[1607.92 → 1615.48] And I think also the different channels through which people are communicating kind of naturally develop their own bias.
[1615.48 → 1621.50] I don't mean bias in a bad way necessarily, but just the bias towards like emphasizing certain things, right?
[1621.50 → 1624.90] Like you get into the news research community.
[1625.48 → 1628.36] We had a great conversation about that.
[1628.36 → 1634.14] And like people are talking about, oh, like we're doing all this like activation hacking and representation engineering.
[1634.14 → 1643.92] And like that's, but that's like not really talked about, like if you're over here in the Llama Index Discord or Lanced Discord or like whatever.
[1643.92 → 1650.80] And some of that's driven by the focus on what those tools do, but also like where people are coming from, right?
[1650.80 → 1664.58] Like, and more of the indie hacker building app sort of stuff or the rigorous like academic side or the like enterprise, like I really just want to get something into production side.
[1664.76 → 1667.52] There's like all these different slants people are coming from.
[1668.26 → 1677.18] That is so fascinating to think about like how each of these communities has their main focus.
[1677.18 → 1688.30] And since it is, there is so much surface area and there are so many areas that you can go, different areas to explore that each community is exploring their own area.
[1688.72 → 1698.38] And if you go into that, you can tap into what people are talking about in that area versus if you go into another community, you get, oh, well, what's going on here?
[1698.50 → 1699.92] What's the focus of this community?
[1700.50 → 1703.08] This is a different outcome from what we've seen.
[1703.08 → 1715.08] I mean, if you step out specifically of kind of the AI ML world, and you look at more just computer science, computer programming, communities out there, there's usually kind of a place to go.
[1715.30 → 1721.42] And you kind of learn the same sets of skills and values, you know, around that.
[1721.68 → 1724.06] And that's a little bit different from this.
[1724.26 → 1729.64] It's been one of the challenges, I think, that the AI ML world has struggled with a little bit.
[1729.64 → 1734.12] So I'm not at all, like I said, I think your survey captured that essence.
[1734.44 → 1738.86] And that's thank you for sharing that with me because I'm going to steal it, and I'm going to say it a bunch.
[1739.70 → 1740.78] Hopefully you don't mind.
[1740.96 → 1742.20] You didn't put a trademark on it.
[1742.20 → 1742.82] Say it all you want.
[1744.60 → 1745.70] It's a great insight.
[1745.96 → 1748.62] I've seen it just in the Flops community, right?
[1748.78 → 1753.56] We have people that are really trying to productionize AI.
[1753.56 → 1759.20] And so what people in there are talking about is really like pragmatic and practical.
[1759.20 → 1765.48] How can I get this being used in my company so that I can either save money or make money?
[1765.58 → 1767.16] Like money is the ultimate metric there.
[1767.24 → 1774.00] If you go into, as you were mentioning, like these different communities, if you go into the Lama Index community, there's a lot of talk of rags.
[1774.00 → 1782.08] And actually, we had Jerry on in the conference, and he showed this slide that I thought was so incredibly done.
[1782.34 → 1783.76] It wasn't him that did it.
[1783.86 → 1788.38] I can't remember the person who created it, but it was like the 11 ways that rags fail.
[1788.74 → 1793.16] And so it had all these different ways that you need to be aware of.
[1793.16 → 1803.66] And I think one that's coming to light that people are seeing is so important is how you need to get that retrieval evaluation correct.
[1803.86 → 1812.36] Because if you're not retrieving the right thing from the Vector DB, then it doesn't matter what you give or what the output of the LLM is.
[1812.56 → 1816.76] If you give it some kind of crap, then it's not going to give you anything there.
[1816.76 → 1826.96] And the other piece that I think is fascinating is that, like, how do you make sure that all this data that you've got in the Vector DB is up-to-date?
[1827.58 → 1830.02] And so we've talked about this a bunch.
[1830.18 → 1832.64] And again, this is in the Flops community.
[1832.74 → 1833.86] We're very industry focused.
[1833.86 → 1837.46] And how can we make sure that we are productionizing this?
[1837.86 → 1843.72] So in a production scenario, you've got your HR chatbot that is using a RAG system.
[1843.72 → 1848.34] And you say, all right, cool, we've updated the vacation policy.
[1848.54 → 1852.80] So we went from a European vacation policy to an American vacation policy.
[1853.22 → 1859.48] And you've got Daniel over here saying, all right, HR chatbot, like, how many days of vacation do I have?
[1860.04 → 1867.32] How do you make sure that everywhere in the Vector DB database, it now is updated to the American vacation policy?
[1867.32 → 1869.00] And so, okay, cool.
[1869.30 → 1875.94] In the Vector DB database, maybe you say, you know what, we were able to scrub everything, or we just pull from the most recent documents.
[1876.38 → 1881.42] But then you were a good engineer, and you made sure to pull in a bunch of different data sources.
[1881.82 → 1885.78] So in Slack, turns out that you're grabbing some data from that.
[1885.96 → 1890.06] And people talk about how it still is the European vacation policy.
[1890.24 → 1894.80] And now Daniel's been quoted of having 30 days of vacation when really he only has two.
[1895.22 → 1895.84] That's unfortunate.
[1897.32 → 1897.72] Yeah.
[1899.48 → 1903.56] Actually, this is a conversation we just had the other day with a customer.
[1904.44 → 1919.26] Because also, at least some of these databases, they have, depending on what you go with, if you go, you know, with a plugin to an existing database, maybe there's kind of more traditional updating and upsetting sort of functionality.
[1919.72 → 1923.62] But some of these, it's just like put a document in, get it out, delete it.
[1923.62 → 1929.66] And there has to be a layer of logic on top of these that actually help you do some of that.
[1929.78 → 1936.42] So in their case, it was like, oh, we want to take in all the articles that we've had on our web on this website.
[1936.66 → 1937.64] And that's going to be it.
[1937.64 → 1940.50] And then they're like, well, what if we update those?
[1941.02 → 1944.56] Do we just like blow everything away and redo it?
[1944.56 → 1956.88] And I think my, it ended up my answer, like, with the amount that they had, I was like, probably, like, if you can have something running in the background, honestly, that's probably the safest thing for you.
[1956.88 → 1960.04] And it's going to take, like, a couple of hours or something.
[1960.20 → 1970.42] But then at least you, the going into the making sure everything's synced up is, and in that case, like, they could just version the files of the embedded database.
[1970.42 → 1973.14] But yeah, it's an interesting set of problems.
[1973.68 → 1974.46] It is a fun one.
[1974.46 → 1982.12] And also, you know what I'd love to explore, too, is the idea of, like, RAC or role-based access control.
[1982.54 → 1987.08] How are you seeing people go through that and do it well?
[1987.50 → 1990.86] Because that feels like another one that can be really misused.
[1991.46 → 1993.44] So for RAG is one thing.
[1993.58 → 2003.28] For text to SQL, some of that maybe can be kind of nice because if you're embedding some function in an application that already has RAC on the database,
[2003.28 → 2007.92] then you could use that credential and hopefully that carries through.
[2007.92 → 2017.30] But for the vector database side, we've interacted with people that have maybe, like, an internal chat and an external chat,
[2017.46 → 2025.06] where the external chat is a subset or should use a subset of the documents from your internal chat.
[2025.72 → 2028.40] So in that case, you sort of have, like, two.
[2029.26 → 2031.34] It's bifurcated rather easily.
[2031.34 → 2037.48] And, you know, that's, like, somewhat easy to deal with because you could just have, like, two tables or two collections,
[2037.68 → 2044.30] whatever that is in the vector database and kind of merge the retrieval or use them selectively in certain ways.
[2044.70 → 2051.86] But as soon as then you have, like, many, many different roles or even user-specific things,
[2052.38 → 2059.92] I don't know, like, many vector databases that would be, however you manage that, would be transparent to that vector database.
[2059.92 → 2063.34] So you'd have to somehow manage the metadata associated with it.
[2063.66 → 2066.58] There may be certain people we'll have to follow up.
[2066.88 → 2074.76] Chris, we haven't had a MTA on for a while, but they're always thinking about these role-based access to really sensitive and private data.
[2075.10 → 2080.48] I'm sure there's people doing advanced things, but in terms of the main tooling that people are just grabbing off of the shelf,
[2080.48 → 2083.66] a lot of that logic is just absent.
[2084.30 → 2084.78] Exactly.
[2085.20 → 2090.68] Yeah, I want to hear if anybody is doing RAC, and they've figured it out.
[2090.78 → 2097.66] That's one thing I'm fascinated with because it is a very, again, going to the community that I run with,
[2097.76 → 2102.20] that's something that productionizing kind of, it comes hand in hand with that.
[2102.20 → 2107.92] Yeah, and it could also have to do with the guardrails that you put around the large language model calls,
[2107.92 → 2114.32] because if it's, like, a public-facing chat or something like that,
[2114.82 → 2123.48] that you may want to filter out PII or, like, prompt injections may be a very important thing,
[2123.48 → 2129.24] versus, like, internally, ideally you trust people as long as you know how the data is flowing.
[2129.60 → 2133.14] Like, there might not be as many restrictions in terms of what can go in
[2133.14 → 2136.08] or who's accessing things and that sort of thing.
[2136.22 → 2137.90] But, yeah, it's interesting.
[2153.48 → 2155.88] This is a Changelog News Break.
[2156.40 → 2161.92] Pierre-Karl Longinus announcing the release of Common Corpus on Hugging Face.
[2162.46 → 2162.82] Quote,
[2163.02 → 2166.12] Contrary to what most large AI companies claim,
[2166.30 → 2171.42] the release of Common Corpus aims to show it is possible to train large language models
[2171.42 → 2176.32] on fully open and reproducible corpus without using copyright content.
[2176.64 → 2179.56] This is only an initial part of what we have collected so far,
[2179.56 → 2183.74] in part due to the lengthy process of copyright duration verification.
[2184.18 → 2185.64] In the following weeks and months,
[2185.90 → 2188.38] we'll continue to publish many additional datasets,
[2188.82 → 2190.68] also coming from other open sources,
[2191.10 → 2193.52] such as open data or open science.
[2194.02 → 2194.38] End quote.
[2194.70 → 2197.10] Here is more info about this massive dataset.
[2197.50 → 2202.58] Common Corpus is the largest public domain dataset released for training LLMs.
[2202.88 → 2205.60] Common Corpus includes 500 billion words
[2205.60 → 2208.96] from a wide diversity of cultural heritage initiatives.
[2209.92 → 2213.96] Common Corpus is multilingual and the largest corpus to date in English,
[2214.32 → 2216.46] French, Dutch, Spanish, German, and Italian.
[2217.04 → 2224.02] Common Corpus shows it is possible to train fully open LLMs on sources without copyright concerns.
[2224.52 → 2229.64] You just heard one of our five top stories from Monday's Changelog News.
[2230.02 → 2233.16] Subscribe to the podcast to get all the week's top stories
[2233.16 → 2236.72] and pop your email address in at changelog.com slash news
[2236.72 → 2242.42] to also receive our free companion email with even more developer news worth your attention.
[2242.84 → 2246.32] Once again, that's changelog.com slash news.
[2246.32 → 2256.04] So in addition to this sort of evaluation stuff,
[2256.04 → 2260.90] we've spent a lot of time talking about data and evaluation and retrieval.
[2260.90 → 2264.22] What about on the model side?
[2264.50 → 2269.08] Do you think we'll ever escape the world of Transformers, Demetrius?
[2269.32 → 2272.20] So this is something I've been thinking about a ton, man.
[2272.54 → 2275.64] And I've got some thoughts on this that like,
[2276.10 → 2280.26] is everything that we're doing now in AI a band-aid
[2280.26 → 2285.42] because Transformers just aren't the right tool for the job?
[2285.62 → 2286.48] Have you guys thought about it?
[2286.48 → 2287.94] Like one big workaround?
[2288.44 → 2289.14] Yeah, exactly.
[2289.62 → 2290.84] Am I crazy to think that?
[2291.20 → 2291.94] I don't think so.
[2292.00 → 2294.94] Actually, I was talking to one of our customers about this.
[2294.94 → 2300.62] They have so much logic around double-checking the outputs of models
[2300.62 → 2303.58] or formatting the outputs of models.
[2304.22 → 2307.98] And I'm talking like hundreds and hundreds and hundreds of lines of code,
[2308.18 → 2309.66] thousands of lines of code, I don't know,
[2309.96 → 2312.76] written all around this sort of workaround of like...
[2312.76 → 2315.72] And it's because they're using general purpose model, right?
[2315.72 → 2322.50] That you sort of have to massage into how you want it to behave, right?
[2322.82 → 2324.60] Is it a little bit ironic that, you know,
[2324.94 → 2328.54] you use a rag to clean up the problems with Transformers?
[2328.62 → 2329.68] Is that what we're saying here?
[2330.46 → 2331.24] Oh, I get it.
[2331.38 → 2332.00] The rag.
[2332.32 → 2334.46] What we need is the Lysol wipes.
[2334.84 → 2335.44] There you go.
[2335.44 → 2343.46] Oh, but I often wonder, like, are we having to over-engineer this
[2343.46 → 2347.00] because the core of the problem,
[2347.00 → 2349.30] it's like we're trying to put a Band-Aid on something
[2349.30 → 2352.90] instead of going and fixing the root of the problem.
[2353.66 → 2357.44] And right now it feels like there's nothing out there
[2357.44 → 2361.30] that can even stand a chance against the Transformer architecture.
[2361.30 → 2364.54] So, of course, we can't say,
[2364.78 → 2367.54] well, I would rather use XYZ.
[2367.84 → 2375.12] But I just get the feeling like when we think about AI in 2024
[2375.12 → 2379.58] or like the ChatGPT AI era,
[2379.82 → 2382.92] we're probably going to be laughing
[2382.92 → 2385.90] at the whole idea of Transformers.
[2385.90 → 2387.82] If in 10 years we're looking at that,
[2387.90 → 2389.32] it's going to be like, yeah, okay.
[2389.88 → 2391.74] Transformers were great, but they were a stepping stone.
[2392.18 → 2395.54] I know that there's quite a bit of research going on in general
[2395.54 → 2398.42] about doing different types of architectures.
[2398.58 → 2400.10] I know that there are a number of organizations
[2400.10 → 2403.82] that have been testing alternatives to Transformers
[2403.82 → 2405.12] in the last couple of years,
[2405.26 → 2407.54] but I don't think anyone's gotten there.
[2407.72 → 2410.16] Or if they have, then you should reach out to us
[2410.16 → 2412.44] and let us know so that we can be talking about it here
[2412.44 → 2413.88] on these podcasts.
[2413.88 → 2416.88] So I think there are a lot of folks out there
[2416.88 → 2418.96] that are really wondering what's next
[2418.96 → 2424.28] because we're essentially taking one superset of architecture
[2424.28 → 2427.24] and we're doing everything we could possibly do with it.
[2427.68 → 2430.36] And every big step forward in the last few years
[2430.36 → 2433.64] has been around what else can we do with this architecture.
[2433.96 → 2436.26] So at some point, I agree with you, Demetrius,
[2436.34 → 2437.32] something's going to give
[2437.32 → 2440.38] and we've got to try some new approaches in there.
[2440.80 → 2442.26] Yeah, that's what it feels like to me.
[2442.26 → 2444.32] It's just like, what's the next step?
[2444.70 → 2447.34] And I would love to also hear from whoever.
[2447.34 → 2450.70] If there's something that feels like it's promising,
[2451.04 → 2452.50] it's really exciting to me.
[2452.58 → 2454.40] I don't know enough about that.
[2454.48 → 2457.08] That's very much the research community
[2457.08 → 2459.34] that I don't get to spend a lot of time in.
[2459.56 → 2462.40] And I'm sure there are a bunch of false flags
[2462.40 → 2464.74] and people get excited about something
[2464.74 → 2468.88] and then it turns out that after you throw a bunch of GPUs at it,
[2468.88 → 2471.48] it doesn't work out like we thought it would
[2471.48 → 2473.56] or like we saw a promise,
[2473.74 → 2476.18] but it didn't actually work out when it holds up to scale.
[2476.36 → 2481.30] So I understand that right now we're in the era of transformers.
[2481.42 → 2484.24] I wonder how long we're going to stay in this era.
[2484.24 → 2488.42] Not only around specific architectures in that capacity,
[2488.52 → 2489.58] but almost new approaches.
[2489.90 → 2492.30] For the first time in a while,
[2492.66 → 2495.32] xeromorphic computing is really rising again
[2495.32 → 2496.70] as a topic of interest.
[2497.02 → 2498.14] And it's not there yet.
[2498.22 → 2500.32] You're talking about architectures,
[2500.44 → 2501.92] both on the hardware and the software side,
[2501.98 → 2504.24] that are not specific to either transformers
[2504.86 → 2506.94] or even GPUs underlying it and stuff.
[2507.30 → 2511.40] But it's been interesting to see the maturity that's developing.
[2511.40 → 2514.40] You talked about the exposure to research.
[2514.92 → 2517.32] Even for me, that's the same case is that
[2517.32 → 2519.36] you have all the pure researchers out there,
[2519.48 → 2523.12] but now we're starting to see them expand out in lots of ways
[2523.12 → 2525.76] and trying completely different approaches.
[2526.48 → 2529.24] And I'm pretty excited that we're going to start seeing
[2529.24 → 2532.08] some interesting results over the next few years
[2532.08 → 2534.28] as people are looking for alternatives
[2534.28 → 2537.04] across both hardware and software architectures.
[2537.24 → 2539.62] I think we're pretty close to a turning point.
[2539.62 → 2541.32] Can you break down real fast?
[2541.40 → 2542.86] What was that big word you just used?
[2544.00 → 2544.44] Anthropomorphic?
[2544.52 → 2545.10] What was that?
[2545.14 → 2545.96] I can't even say it.
[2546.04 → 2547.38] I got tongue-tied.
[2548.14 → 2549.36] Xeromorphic computing, I think,
[2549.46 → 2551.10] is what you're talking about.
[2551.80 → 2552.72] Xeromorphic computing.
[2552.90 → 2553.80] That is a big word.
[2553.86 → 2554.54] What does that even mean?
[2554.60 → 2554.98] I don't know.
[2555.08 → 2556.60] I got to Google that real fast.
[2557.40 → 2561.16] And I am the last person on the face of the earth
[2561.16 → 2564.46] that should be trying to explain xeromorphic computing.
[2564.56 → 2565.50] I put you on the spot.
[2565.72 → 2567.14] But haven't, yeah, no worries.
[2567.14 → 2571.36] But having been exposed to that, the short version is almost like,
[2571.36 → 2574.24] you know, in the earlier days of AI,
[2574.42 → 2577.40] and people would say, you know, in the marketing,
[2577.62 → 2580.02] people would talk about, oh, mimicking, you know,
[2580.08 → 2583.20] the neocortex to, you know, the human brain and stuff like that.
[2583.20 → 2588.22] And we all kind of, as this GPU and transformer-based architectures,
[2588.44 → 2590.98] we're like, well, it's not really like the human brain.
[2591.30 → 2594.06] Well, the xeromorphic architecture is actually that.
[2594.40 → 2597.36] It's the legitimately, like, how does that,
[2597.54 → 2599.76] the architecture of a brain, and I'm saying this,
[2599.86 → 2603.18] like there's probably xeromorphic computing scientists out there
[2603.18 → 2605.46] listening to me now going, oh, my God,
[2605.72 → 2607.18] somebody take his mic away.
[2607.28 → 2608.68] That's a terrible explanation.
[2608.68 → 2612.16] But in my fairly primitive understanding,
[2612.52 → 2614.04] that's kind of where it is, you know,
[2614.08 → 2616.66] how do neurons really work in real life,
[2616.68 → 2619.48] and how do you do compute artificially in that capacity?
[2619.86 → 2623.54] So, but I know that there's definite interest in doing that.
[2623.94 → 2628.10] I know Daniel has a relationship with Intel through Prediction Guard,
[2628.16 → 2630.86] and I know Intel has an interest in that field.
[2631.00 → 2632.36] I think they're one of the leaders in it.
[2632.36 → 2635.96] I Googled it, Intel's all over the first page,
[2636.08 → 2641.56] or I perplexity that it was all cited from Intel.
[2641.70 → 2642.94] That is very true.
[2643.30 → 2645.74] I would hesitate to say it out loud because I'm probably wrong,
[2645.78 → 2648.98] but they may very well be the global leader in that space right now.
[2649.30 → 2649.32] So.
[2649.60 → 2650.52] Yeah, makes sense.
[2650.68 → 2651.74] Well, that is awesome.
[2651.88 → 2654.04] I'm glad that you taught me about that.
[2654.14 → 2656.14] I appreciate you for teaching me.
[2657.12 → 2657.56] Xeromorphic.
[2657.62 → 2659.12] Now I can say it properly and everything.
[2659.12 → 2659.82] Well, you know what?
[2659.82 → 2662.76] Now that you say that, we're going to have a show on xeromorphic computing
[2662.76 → 2663.90] coming up pretty soon.
[2664.14 → 2664.82] Yeah, exactly.
[2664.96 → 2666.22] Let's get down into it.
[2666.30 → 2668.08] I want to listen to that for sure.
[2668.18 → 2669.00] We'll dive into that.
[2669.20 → 2672.12] We'll get what Daniel can reach out to his contacts there.
[2672.80 → 2674.06] Oh, that's classic.
[2674.74 → 2679.04] Well, dude, thank you very much for coming on as we wind up here.
[2679.60 → 2680.88] It's always a pleasure.
[2681.20 → 2683.70] Anyone who has been listening to the show long knows that you're,
[2684.40 → 2686.32] join us regularly on the show.
[2686.60 → 2688.04] It's always special for us.
[2688.10 → 2689.38] We have a great time with you.
[2689.38 → 2690.80] So thanks for coming on today.
[2691.38 → 2696.54] We will get the show notes for the survey and some of the other topics that you brought
[2696.54 → 2698.22] up today, so people can join.
[2698.22 → 2704.62] And folks, if you haven't gotten into the Flops community podcast that Demetrius hosts,
[2704.88 → 2706.52] you definitely need to check that out.
[2706.58 → 2707.96] It is an awesome podcast.
[2708.12 → 2710.26] Highly recommended by both myself and Daniel.
[2710.86 → 2712.78] So hope people join you over there.
[2713.28 → 2716.40] Oh, and can I also plug, we're going to have an in-person conference.
[2716.40 → 2719.00] And I'm really excited about that.
[2719.08 → 2725.14] A little bit shaking in my boots because June 25th, it's going to be our first in-person
[2725.14 → 2726.32] conference ever.
[2726.68 → 2729.64] And it's going to be all about AI quality.
[2729.90 → 2733.04] And we've got some super cool speakers coming.
[2733.04 → 2739.66] We managed to get the CTO of Cruise to come and talk about what they've done since their
[2739.66 → 2744.26] little mishap in regard to like making sure that their AI is quality.
[2744.42 → 2747.20] We've also, I mean, there's so many great people.
[2747.28 → 2752.66] You can go to AI quality conference.com, and we'll throw the link there in the show notes
[2752.66 → 2752.94] too.
[2752.94 → 2756.80] I'm very excited for it, but the speakers are going to be awesome.
[2757.16 → 2759.06] The attendees are going to be amazing.
[2759.68 → 2765.70] I think what I'm most excited for though, is that we're going to have all kinds of fun,
[2765.88 → 2766.76] random stuff.
[2766.98 → 2770.40] You can imagine it's going to be a conference, but it's probably going to be more like a festival.
[2770.76 → 2776.70] I may have people riding around in tricycles, giving out coffee, or we'll have a little DJ
[2776.70 → 2777.26] area.
[2777.26 → 2782.54] So, or a jam band, like breakout room, a bunch of Legos hanging around.
[2782.64 → 2783.58] I don't know yet.
[2783.66 → 2789.16] So if anybody has any ideas on how we can make it absolutely unforgettable, I would love to
[2789.16 → 2790.02] hear about that too.
[2790.46 → 2795.62] And I'm going to throw out one last plug for you, is that when you say that, I believe
[2795.62 → 2799.58] you, because I know that you've heard me say this when we were off the air, but just
[2799.58 → 2805.98] in case anyone doesn't know this, Demetrius is the funniest guy in the entire AI world.
[2805.98 → 2807.80] Um, and does hilarious things.
[2807.98 → 2812.94] If you don't follow him on social media, you are missing some really great, great content.
[2813.26 → 2819.44] So, um, anyway, just wanted to say that I, people, people should show up at the conference
[2819.44 → 2821.02] just to see what you're doing.
[2821.02 → 2826.00] If no other reason, even aside from the cool content you have, they'll enjoy it.
[2826.00 → 2827.52] So thanks for coming back.
[2827.72 → 2829.02] I mean, there's going to be great speakers.
[2829.02 → 2833.34] You're going to learn a ton, but there's also going to be some really random stuff that
[2833.34 → 2835.08] you're going to be like, what is going on here?
[2835.08 → 2839.92] And hopefully you really enjoy it because that's kind of what I, that's what I'm going
[2839.92 → 2840.20] for.
[2840.62 → 2840.96] Okay.
[2841.08 → 2842.26] Well, thanks a lot, man.
[2842.32 → 2843.46] I'll talk to you next time.
[2843.74 → 2844.06] Likewise.
[2844.38 → 2844.68] See ya.
[2844.68 → 2852.86] All right.
[2852.86 → 2855.64] That is practical AI for this week.
[2856.42 → 2857.48] Subscribe now.
[2857.64 → 2864.86] If you haven't already headed to practical AI.fm for all the ways and join our free Slack team
[2864.86 → 2869.06] where you can hang out with Daniel, Chris, and the entire change log community.
[2869.06 → 2874.26] Sign up today at practical AI.fm slash community.
[2874.86 → 2880.64] Thanks again to our partners at fly.io to our beat freaking residents, Break master Cylinder,
[2880.88 → 2881.78] and to you for listening.
[2882.06 → 2883.92] We appreciate you spending time with us.
[2884.28 → 2885.44] That's all for now.
[2885.68 → 2887.38] We'll talk to you again next time.
[2887.38 → 2888.38] Bye.
[2888.38 → 2888.70] Bye.
[2888.88 → 2889.44] Bye.
[2893.84 → 2894.02] Bye.
[2894.08 → 2894.42] Bye.
[2896.90 → 2897.86] Bye.
[2897.94 → 2898.36] Bye.
[2898.42 → 2899.14] Bye.
[2899.26 → 2899.38] Bye.
[2899.42 → 2899.92] Bye.
[2899.94 → 2900.54] Bye.
[2900.58 → 2901.00] Bye.
[2901.00 → 2902.60] Bye.
[2902.60 → 2907.10] Bye.
[2907.64 → 2907.70] Bye.
[2907.90 → 2908.72] Bye.
[2908.72 → 2909.84] Bye.
[2910.10 → 2910.34] Bye.
[2910.34 → 2912.50] Bye.
