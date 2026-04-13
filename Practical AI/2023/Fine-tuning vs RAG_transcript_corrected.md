[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.20 → 24.36] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.36 → 24.66] listen.
[24.92 → 26.76] Check them out at Fastly.com.
[26.76 → 32.02] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.04 → 36.10] Learn more at fly.io.
[42.56 → 45.90] Well, welcome to another episode of Practical AI.
[46.32 → 47.92] This is Daniel Whiten ack.
[48.02 → 53.58] I'm the founder at Prediction Guard, and I'm joined as always by my co-host, Chris Benson,
[53.58 → 56.20] who is a tech strategist at Lockheed Martin.
[56.76 → 61.04] And today, Chris, I don't know if you've been listening to the Changelog, our sister
[61.04 → 61.48] podcast.
[61.78 → 67.54] They've been doing these like Changelog and friends episodes where it's not necessarily
[67.54 → 73.30] like a guest interview, but it's like, hey, let's invite one of our friends on and just
[73.30 → 74.68] talk about cool stuff.
[74.68 → 80.44] And I feel like we've a little bit got like practical AI and friends today because we're
[80.44 → 87.64] joined by Demetrius from ML Ops Community, which, you know, you're involved in events and
[87.64 → 89.70] podcasts and reports and surveys.
[89.70 → 92.44] And basically, basically you run the whole AI world.
[92.70 → 94.50] So, you know, welcome.
[94.74 → 97.22] And we're glad to have you back as our friend.
[97.46 → 100.72] He's like the deep state, you know, the deep state.
[100.72 → 102.62] He's like running everything behind the scenes.
[103.66 → 105.78] I am honoured to be considered a friend.
[105.88 → 111.28] First off, I just want to say that because I appreciate the amazing stuff that you all
[111.28 → 111.92] are doing here.
[112.14 → 117.82] And of course, whenever I get the opportunity to come and chat with you folks, I am going
[117.82 → 118.50] to jump at it.
[118.72 → 119.20] Excellent.
[119.20 → 128.50] And I know that last time I saw you, I think was at the one of the recent LLMs in production
[128.50 → 130.46] event, which was super fun.
[130.46 → 138.30] Give us a little sense of like what has the past few months look like in the ML
[138.30 → 142.18] Ops community and some of the events that you've been doing.
[142.46 → 144.82] It seems like, you know, there's so much.
[144.82 → 148.56] I think you had also like in-person things.
[148.94 → 150.58] So like, give us a sense what's happening.
[151.08 → 153.28] Yeah, I appreciate you calling that out.
[153.36 → 158.52] And of course, I appreciate you presenting at the LLMs in production conference.
[158.66 → 159.84] That was a blast.
[160.08 → 160.98] Yeah, it's a good time.
[161.32 → 167.36] That event itself, we had two days and each day had three tracks.
[167.58 → 171.00] So there were two full tracks and then one workshop track.
[171.00 → 175.58] And there were over 82 speakers in the whole event.
[176.16 → 178.86] And man, that was a lot of work.
[178.98 → 179.98] Yeah, I bet so.
[180.38 → 181.22] Add on to that.
[181.30 → 183.38] So that was the virtual part of it.
[183.46 → 187.30] But add on to that, we had in-person parts of it.
[187.42 → 189.90] So in Berlin, there was a hackathon that we did.
[190.44 → 193.02] And in Amsterdam, we had a meetup.
[193.06 → 195.18] And then in London, we had a watch party.
[195.18 → 201.82] In San Francisco, we had a meetup that happened and then a hackathon right after.
[202.16 → 203.38] And then a workshop.
[203.80 → 207.44] So there were all kinds of craziness that was going on.
[207.62 → 210.70] And that was just for the LLM in production event.
[211.08 → 216.48] Later on, I mean, we're in now 37 cities around the globe.
[216.48 → 225.34] So wherever you are, you probably have an Flops community meetup around you unless we're in like North Africa and South Africa.
[225.64 → 228.56] But then also even in Lagos, Nigeria.
[228.94 → 236.78] We're in Australia, which is always awesome because I keep threatening to go out there and just pop up at a meetup.
[237.30 → 237.44] Yeah.
[237.50 → 238.98] So that's the in-person stuff.
[238.98 → 250.92] There's people that have just gotten super excited about it, and they decided to start a community chapter, which is the unbelievable power of community.
[251.14 → 256.68] I am blown away by it every time someone approaches me and says, hey, I want to do something in my city.
[257.30 → 258.28] Yeah, that's so cool.
[258.28 → 266.44] And I've been able to attend a couple in-person events this year related to AI stuff.
[266.44 → 270.02] And I will in the fall as well.
[270.34 → 275.48] I'm curious to know, like, from my perspective, it's cool to see things.
[275.96 → 286.28] I feel transition a little bit from kind of hypothetical stuff, a lot of discussion to people talking about like, hey, we did this.
[286.42 → 288.80] This is how we implemented our workflow.
[289.12 → 290.42] Hey, have you tried this?
[290.78 → 294.82] And so I, of course, love those types of conversations.
[294.82 → 297.54] Do you get a similar vibe or what?
[297.82 → 306.54] How does the community in terms of generative AI and LLMs, how does it seem different now than even like six months ago or something like that?
[307.06 → 307.56] Oh, yeah.
[307.88 → 316.84] That's so good because it does feel like there are use cases that are becoming very clear on what LLMs shine in and what they're not good at.
[316.84 → 320.82] And then there's also the stack that's forming.
[321.36 → 323.18] And we did a survey, probably.
[323.30 → 327.28] That's another thing that we did in the community on top of all the fun other stuff.
[327.46 → 333.28] We did a survey, and we surveyed people that are actually using LLMs or even not using LLMs.
[333.28 → 336.38] And we asked them why you're not using them.
[336.44 → 338.88] And we went through a bunch of stuff or why you are using them.
[338.94 → 340.42] What are some big pain points?
[341.14 → 347.48] And it was becoming very clear that there are certain use cases that people are using LLMs for.
[347.56 → 349.00] And we can get into that in a minute.
[349.00 → 352.02] And then there's also this stack that is forming.
[352.32 → 354.82] And the stack was probably the most interesting.
[354.96 → 359.02] I know you guys mentioned it with the A16Z article.
[359.42 → 361.72] And Rajkot is one of the authors of that.
[361.78 → 365.12] And he helped me with the report when I wrote it, too.
[365.26 → 369.24] So he's behind the scenes, like moving the puppets, the puppeteer.
[369.48 → 376.88] The cool thing with the stack is you kind of have, if I break it down for those who haven't seen the diagram that we put together,
[376.88 → 382.52] it's like you have the foundational model, and then you have some kind of vector database,
[382.52 → 386.64] which is like the hero, the champion in this whole LLM scene.
[386.88 → 393.84] You've got, if you need to do some fine-tuning or model building, you have that component to it.
[393.84 → 395.04] But we can get into that.
[395.18 → 397.66] I'm very opinionated about the fine-tuning part.
[397.98 → 399.74] And I'll tell you why in a bit.
[399.86 → 403.56] And then you have stuff like developer SDKs.
[403.56 → 406.76] And this is, you know, like your Lama Index or Lang Chains.
[407.18 → 413.26] And then on top of that, you have like the monitoring or experiment tracking, prompt tracking,
[413.52 → 418.94] this kind of things like a port key, a optimize, prompt layer.
[419.24 → 421.14] There are all kinds that are coming out.
[421.78 → 429.28] And so what we didn't have at that moment that I think are starting to emerge more now
[429.28 → 438.20] and I'm really excited about is like, how are people actually evaluating these models?
[438.20 → 446.42] And is it coming with your different tools or are you doing extra stuff on top of it?
[446.48 → 452.78] So that was the inspiration behind a whole nother survey that we're doing right now on evaluation.
[453.58 → 453.76] Yeah.
[454.30 → 458.84] I can say personally, I'm doing extra stuff on top.
[459.48 → 464.44] That's my like short and very short answer, which is, of course, much more involved.
[464.74 → 466.24] But yeah, I don't know.
[466.32 → 468.66] What is your sense of that?
[468.72 → 471.12] Am I just intuition wise?
[471.12 → 474.86] Am I out of the norm or in the norm with that?
[475.66 → 477.50] No, you are completely in the norm.
[477.70 → 481.68] And I think the hardest part, and this is why we wanted to do a survey around it, is because
[481.68 → 485.42] this is one thing that is super unclear.
[486.08 → 488.78] And nobody really knows if they're doing it right.
[489.08 → 492.26] And they don't really know what the best practices are.
[492.50 → 496.32] And so you also don't really know what you're evaluating.
[496.32 → 498.26] Are you just evaluating the model?
[498.84 → 499.94] One thing's for sure.
[500.40 → 502.94] All these benchmarks are complete bullshit.
[503.52 → 505.00] That we all know, right?
[505.08 → 506.28] That is very clear.
[506.38 → 507.52] How do you really feel about it?
[509.62 → 510.18] Yeah.
[510.56 → 518.34] And they are interested in certain ways, but the types of evaluations that are going on
[518.34 → 518.92] there.
[518.92 → 526.20] So like, I think they serve a place maybe, but they don't translate into like, OK, now
[526.20 → 527.76] I have this use case, right?
[527.98 → 536.50] If I take the model on the top of that leaderboard, I am very much not guaranteed to have like the
[536.50 → 539.68] quote, the best results for my use case.
[539.82 → 542.58] And I think that's what's confusing to a lot of people.
[543.04 → 543.70] A hundred percent.
[543.70 → 552.02] That's exactly it, is that these models and the use case that you have, who knows how it's
[552.02 → 554.96] going to match up against one another, right?
[554.98 → 561.90] And then it's not only that, but how are you monitoring or evaluating for toxicity or the
[561.90 → 565.50] ability for it to do the one thing that you care about?
[565.60 → 567.04] I mean, I don't care if it's.
[567.04 → 573.14] And also, it just kind of feels like a lot of marketing at the end of the day, when you
[573.14 → 577.76] see the newest model comes out and everybody loves SODA, SODA.
[577.88 → 584.14] This is, you know, state of the art SODA beats ChatGPT on all these different metrics.
[584.14 → 589.08] And I just kind of laugh because it feels like I've desensitized to that these days.
[589.40 → 589.52] Yeah.
[589.52 → 596.92] I think also it's kind of often kind of funny to me that even like ChatGPT is being used
[596.92 → 604.04] as a static baseline for these things when it's not even like ChatGPT isn't a model,
[604.34 → 604.66] right?
[604.66 → 610.58] It's a product that has layers on top of it for, you know, that handles all sorts of things.
[610.58 → 617.38] And so that's another misconception that I've seen is like, well, is it really fair to compare
[617.38 → 626.24] a model's output to the output of a product that has a lot of kinds of functionality built
[626.24 → 627.56] around it and with it?
[628.24 → 628.40] Yeah.
[628.50 → 633.44] And that also kind of lets people know when that's drawn out, it lets people know that,
[633.60 → 636.44] hey, the LLM here is not your application.
[636.44 → 643.50] There is this whole layer on top of it, which I know you were talking about retrieval based
[643.50 → 649.38] augmentation or retrieval augmented generation as we are gearing up for this episode.
[650.02 → 656.68] There's, of course, like whatever your opinion about prompt engineering is, there is an engineering
[656.68 → 660.92] element to how you call these models and chain things together.
[660.92 → 667.70] And like you say, evaluate things, validate things, filter things for whether it be toxicity
[667.70 → 670.54] or factuality or whatever it is.
[670.60 → 679.24] So there's just so much around that that's not the LLM that I think people confuse those
[679.24 → 680.68] concepts a lot of times.
[681.18 → 686.40] You know, just as a little aside here, listening to you guys talking about this, and you guys
[686.40 → 692.28] are experts at this stuff, and I'm just thinking about all the poor people out there who are
[692.28 → 694.46] listening and maybe aren't at your level.
[695.10 → 698.30] It's a tough thing to try to figure out how to navigate this.
[698.78 → 703.26] When you think about it, you guys are debating this and are not completely in alignment yourself.
[703.52 → 707.72] I'm having a lot of empathy for people in the audience who are going, how the hell am I
[707.72 → 708.48] supposed to do this?
[708.58 → 710.66] Well, and then alignments the other thing.
[711.00 → 711.22] Yeah.
[711.22 → 713.08] Oh, yeah.
[713.22 → 714.10] Another buzzword.
[714.30 → 716.28] That tick it off on the buzzword bingo.
[716.48 → 716.94] There you go.
[717.00 → 717.28] There you go.
[718.22 → 725.30] Well, it's funny because when you are trying to figure out your use case and how to get
[725.30 → 730.34] the best performance out of an LLM, there are things that you go through, right?
[730.40 → 731.76] There's like almost stages.
[732.28 → 735.84] And you figure out the debugging is quite difficult.
[735.84 → 739.64] As you were saying, is it the prompt that's giving me the problems?
[739.64 → 747.30] Or is it that something in my retrieval or the way that I'm creating these vector embeddings,
[747.44 → 748.82] are those the problems?
[749.00 → 754.52] Like where exactly is my problem, and how do I isolate that so that I can make the whole
[754.52 → 755.30] system better?
[755.92 → 761.42] And that is, again, it goes back to evaluation and evaluating the whole system.
[761.54 → 767.58] How do you look at what you're doing as a whole as opposed to just like, oh, cool, there's
[767.58 → 773.04] this model and if I go to a hosted version of it and I ask it if the earth is flat, it
[773.04 → 774.50] tells me yes or no.
[774.96 → 777.68] And most of the time they say yes, which is crazy.
[777.76 → 782.64] It's like, oh, you've been trained on one too much flat earth Subreddits.
[782.96 → 785.30] Or they've just seen a lot of answers that are positive.
[786.14 → 787.42] So it seems probable.
[787.42 → 796.76] Yeah, as you're talking, I think one of the things that I've realized is in the A16Z kind
[796.76 → 802.16] of stack, they call this layer orchestration, which I think a lot of these tools are amazing
[802.16 → 805.18] that fit into that layer and the things that they're doing.
[805.32 → 807.98] You know, Lang chain, Llama Index, we've mentioned.
[808.56 → 812.56] Sometimes, though, it's just like how rapidly the field is advancing.
[812.56 → 818.58] Like if you import like whatever chain from Lang chain and then whatever model, right?
[818.62 → 820.56] And then whatever vector database.
[821.16 → 825.60] And then like you put it all together, you run the thing, and then you get like an empty
[825.60 → 827.06] string output, right?
[827.10 → 829.92] Like you're saying, like, where did it go wrong, right?
[830.02 → 833.78] And how do you like to divide and conquer, debug that, right?
[833.88 → 840.04] So I think a lot of what I've just in my own applications that I'm working on for clients
[840.04 → 846.88] and other things, a lot of times, to be honest, for me, it's a lot simpler to write out my
[846.88 → 854.42] chain of my LLM reasoning in just regular Python logic, add like whatever exception handling
[854.42 → 862.18] I want, like make the call to the vector database like manually and like to create some logic around
[862.18 → 862.48] that.
[862.48 → 871.68] So I feel that that sort of Python DIY side, it's like less convenient, but I usually end
[871.68 → 872.94] up getting there still.
[873.42 → 879.92] You know, again, it's part of the maturity of this field, I guess, and partly like how
[879.92 → 881.40] things are advancing quickly.
[881.96 → 883.58] You know, they'll have a fix for that.
[883.66 → 886.68] You know, in the spirit of you may have heard like, you know, when you have a problem with
[886.68 → 887.64] Facebook, what's the answer?
[887.72 → 888.22] More Facebook.
[888.22 → 893.62] Well, in that spirit, I'm sure Meta will put out debug llama for you in no time and it
[893.62 → 895.56] will solve all of your problems right there.
[896.32 → 902.48] It's funny too, because it feels like that just forces you to stay simple.
[902.68 → 903.02] Yes.
[903.06 → 908.48] Again, like going back to the KISS principle and realizing, you know what, maybe I'm trying
[908.48 → 913.94] to over-engineer this, and I can go far with, maybe I don't even need a vector database, which
[913.94 → 915.86] is kind of blasphemy.
[916.24 → 916.86] How dare you?
[916.86 → 920.44] You did call it a hero and a champion a few minutes ago, I want to point out.
[921.72 → 922.12] Yeah.
[922.34 → 928.20] I mean, it is wild that you can go so far.
[928.32 → 934.58] I talk to startups almost every day in my day job, which is not the Flops community, and
[934.58 → 937.74] they are, they have real revenue.
[938.06 → 941.12] And a lot of them, I'm always asking them like, oh, so how are you doing this behind
[941.12 → 941.60] the scenes?
[941.60 → 945.34] And a lot of them aren't even using vector databases.
[945.34 → 950.56] But they're like cashing in, and they have a product that's working, and it's working at
[950.56 → 950.84] scale.
[950.94 → 956.60] And so there is this misconception, I think, sometimes that we need all the bells and whistles
[956.60 → 962.68] and this stack that I just was talking about and saying that the vector databases are the
[962.68 → 968.34] champions that potentially for your use case, like, do you really need it?
[968.34 → 970.18] Because it does add that complexity.
[970.18 → 977.04] And so going back to the tried and true principle, like, just keep it simple.
[977.04 → 994.10] You mentioned that you had some strong opinions related to retrieval and fine-tuning.
[994.54 → 1000.38] I think this is the time for the hot take officially declaring this practical AI and friends episode.
[1000.38 → 1003.82] So it's a safe space to declare your hot take.
[1005.08 → 1006.04] Safe space.
[1006.14 → 1006.72] I love it.
[1007.04 → 1007.92] Well, I know.
[1008.02 → 1011.90] I just think that I hear a lot about fine-tuning.
[1012.60 → 1020.48] And I don't know if people who throw around the idea of fine-tuning something really understand
[1020.48 → 1024.94] what you fine tune a model for, especially like LLMs.
[1025.24 → 1028.34] If it's a Stable Diffusion model, that's a whole different story.
[1028.34 → 1036.60] And I think sometimes these diffusion models, they give us the wrong idea of what fine-tuning
[1036.60 → 1038.00] in LLM will do.
[1038.20 → 1046.72] So undoubtedly, you saw the rise of like Lena or Photo AI or all of these fine-tuning.
[1046.72 → 1062.86] Basically, what these companies were doing in the background is they were running some kind of diffusion model, and you would upload your selfie or your selfie or a picture of your dog, and you would be able to bring it into the world of AI art.
[1062.86 → 1078.94] And if you take that concept over to LLMs, you think, oh, well, if I just fine tune an LLM on all of my emails, then the LLM will know how to write emails like me.
[1078.94 → 1080.32] But it's not like that.
[1080.32 → 1085.02] There's the misconception that it's not like equal in that regard.
[1085.16 → 1085.78] Fine-tuning.
[1085.90 → 1093.58] You don't fine tune something so that it can understand you more, and you can call it out and say, now write like Demetrius.
[1094.06 → 1098.76] Because what you want to fine tune for, for that case, let's just be clear.
[1098.84 → 1101.90] That's where retrieval augmented generation shines.
[1101.90 → 1113.68] Because you just say, hey, here's a database or a vector database of all of Demetrius's emails and the most you can do some few shot prompting and say, write like this.
[1113.72 → 1117.48] Here's like five styles of Demetrius writing a response to this.
[1117.60 → 1118.94] So make a sixth one.
[1119.58 → 1120.72] And you're golden.
[1120.72 → 1131.98] You don't need to go through like burning a lot of cash on GPUs and GPUs are scarce these days to fine tune some model that may or may not work after you fine-tuned it.
[1132.18 → 1139.78] So I think it's worth calling out like when you should be fine-tuning things, because I don't, I don't want to say like never fine tune it.
[1139.78 → 1153.28] I just want to say like I've seen a lot of people talking about it and also a lot of companies starting that will tote how easy it is to fine tune and how you should be fine-tuning and use your company's data to fine tune.
[1153.50 → 1154.70] It's like fine-tuning.
[1154.92 → 1163.18] I think the best way that I heard it talked about was in a recent Flops community podcast that I had with Shall S.
[1163.40 → 1166.94] He created Ragas, which is like an evaluation framework for Rags.
[1167.36 → 1168.84] That's awesome, by the way.
[1168.84 → 1169.48] Go check it out.
[1169.54 → 1171.30] But he's also very big in fine-tuning.
[1171.44 → 1180.10] And he is also one of the main people that does the Open Instruct project, which is a whole open source LLM project.
[1180.10 → 1195.24] And so he was mentioning how you want to fine tune when you have some new function or some way, some new output, something that you need to teach the LLM to do that it doesn't necessarily know how to do.
[1195.24 → 1200.70] So a perfect example of this is OpenAI's functions.
[1200.70 → 1204.16] So like ChatGPT or GPT-4 functions.
[1204.50 → 1212.90] This makes it much easier for you to get very, very clean data or data that's outputted in a certain way.
[1213.06 → 1213.30] Right.
[1213.30 → 1217.20] And it gives you this structure data.
[1217.40 → 1221.38] And that is a whole reason that you would want to fine tune something.
[1221.38 → 1226.86] Or the other example I think is LLM, the code LLM.
[1226.86 → 1239.94] But I think where code LLM falls down is that if the original base model doesn't see a lot of examples of code, then no matter how much you fine tune it, you're not going to get a good coding model out of it.
[1239.94 → 1246.94] And some people who are using code LLM and loving it, like, come tell me because I haven't found anybody yet.
[1247.22 → 1251.42] So that's my rant about fine-tuning versus rags.
[1251.42 → 1272.06] And I have the last thing that I will say is, like, if you're looking at fine-tuning, and you've been brainwashed by the society out there or the community at large, and you think you need to do it, like, let's just remember why ML was so hard before LLMs.
[1272.06 → 1275.34] Like, collecting data is not so easy.
[1275.46 → 1280.22] Labelling data, cleaning data, all of that stuff is quite difficult.
[1280.50 → 1284.18] And you need to do that if you're going to fine tune.
[1284.54 → 1288.74] I just want to say, I want to remind everyone that Daniel likes to clean data.
[1289.58 → 1290.84] That's something I miss.
[1290.94 → 1296.68] I feel like because of LLMs, I'm not doing it quite as much, which is a hole in my life.
[1296.78 → 1299.22] I'm determined to remind our audience of that fact.
[1299.36 → 1300.78] You know, it's just kind of horrifying.
[1300.78 → 1302.74] So I kind of remind everybody once a year.
[1303.12 → 1303.80] It's therapeutic.
[1304.10 → 1304.76] There you go.
[1305.70 → 1321.28] I think along with some of what you've expressed, Demetrius, that there's a general misconception about the data that you would use to fine tune an LLM.
[1321.28 → 1332.62] So I've been in countless conversations where the idea is, oh, well, we're wanting to do, like, question answering on our documents or something like that.
[1332.70 → 1332.88] Right.
[1332.88 → 1341.56] And we would love to fine tune a model on our internal company documents.
[1341.56 → 1344.58] And then it's going to be better at question answering.
[1344.58 → 1362.62] So what I generally tell those people is, like, hey, like when you're fine-tuning one of these models just on that raw unstructured text, in the best case scenario, what you're creating is a better autocomplete model to autocomplete your type of documents.
[1362.98 → 1363.14] Right.
[1363.14 → 1367.88] What you're not doing is creating a better question answering model.
[1368.10 → 1370.76] Those are two-way separate things.
[1370.88 → 1371.02] Right.
[1371.10 → 1378.14] So if you wanted to fine tune a model like that, I'm not like you're saying there may be cases where that's useful.
[1378.30 → 1379.54] Maybe it's a domain thing.
[1379.54 → 1385.40] Maybe it's a very like you want very structured type of output answers like you're talking about.
[1385.96 → 1393.40] But in that case, what you want to do, you actually don't want to fine tune just on that raw text data.
[1393.78 → 1402.48] You want to create your own set of instruction prompts likely that are fed in with various questions.
[1402.48 → 1416.16] And you have the answers, and you have everything like set up, and you have thousands and thousands of these examples, which that I think when you frame it that way, then people are like, oh, so it's like a lot of work to create that sort of data set.
[1416.68 → 1419.94] And yeah, like turns out it still is.
[1420.04 → 1420.26] Right.
[1420.82 → 1422.16] Oh, that's so funny.
[1422.40 → 1423.94] That is so well put, too.
[1424.08 → 1432.46] I love that because that's my rub on fine-tuning is that people don't realize how difficult it is and how much effort and how much work goes out.
[1432.48 → 1439.46] And that's kind of why Mosaic sold for a billion, you know, because it's hard.
[1439.68 → 1446.56] And so companies that actually are doing it, that Mosaic was able to convince they needed to do it.
[1446.64 → 1448.14] They got a lot of money for it.
[1448.14 → 1451.62] But that's a that's a whole different story.
[1452.82 → 1453.34] Yeah.
[1453.42 → 1461.06] And maybe for those that are less familiar in our audience, maybe they've interacted with LLMs.
[1461.06 → 1463.74] They like to understand the concept of fine-tuning.
[1464.40 → 1469.36] Maybe they're not as familiar with retrieval augmented generation.
[1470.38 → 1474.74] I know that one of the things you mentioned is the Flops community.
[1474.74 → 1476.92] You're doing a whole course on this.
[1476.92 → 1478.12] It sounds like.
[1478.74 → 1486.16] So could you just give like the kind of high level pitch for like retrieval augmented generation?
[1486.16 → 1496.70] Like what does that mean to you as a person who is obviously a promoter of this approach and something that people should try as they're getting into these technologies?
[1496.70 → 1498.84] Kind of maybe that general pitch.
[1499.12 → 1503.36] And then and then we can talk about maybe a few more specifics that you'd like to highlight.
[1503.62 → 1504.92] But thank you for bringing that up.
[1505.04 → 1507.56] I mean, this is the first time that we're actually doing a course.
[1507.56 → 1512.22] So it is a little nerve wracking and at the same time, super exciting.
[1512.22 → 1517.56] And so I'm just going to clarify that it is not me leading the course.
[1517.66 → 1524.10] We got an expert, the expert of experts, who is Raul, who created the course for us.
[1524.14 → 1531.46] He is an engineer in San Francisco that's been doing this for a long time, and he's been doing it at some serious scale.
[1531.46 → 1543.74] So he knows what's up, and he goes and does everything from like the Kubernetes clusters to the end prompts and then monitoring the whole system.
[1543.74 → 1547.98] So, again, I'm a big thinking about things in systems.
[1548.24 → 1560.04] But when it comes to like retrieval augmented generation, let's just go back to what is the hero of our story in this case.
[1560.04 → 1561.78] And it's not the vector database.
[1561.94 → 1570.92] I would say that like question answer systems are basically the hello world of working with LLMs these days.
[1570.92 → 1572.48] That's kind of what it feels like to me.
[1572.52 → 1573.66] I don't know about you guys.
[1573.72 → 1587.96] If you have that feeling, too, where you want to get your feet wet with LLMs, you probably are going to do some kind of like talk to your data or, hey, if I ask this a question, what responses do I get?
[1587.96 → 1596.44] And in those use cases, the best way to set up and architect your system is through like retrieval augmented generation.
[1596.68 → 1604.20] Again, going back to what I was saying earlier, not absolutely needed because I've seen viable businesses built without it.
[1604.20 → 1611.96] But if you are at that point where you're like, oh, well, this will add to my tool belt, you know, it's like another tool in my toolkit.
[1611.96 → 1622.26] Then what we created was a course that goes over, and we wanted it to be something that you don't need to spend like six weeks on.
[1622.38 → 1625.12] We wanted it to be that you could level up really quickly.
[1625.12 → 1634.90] And so you go through creating a data pipeline and pre-processing that data, then ingesting that data into a vector database.
[1635.26 → 1643.22] And then you can semantic search for the answers from the questions that you're getting from the end user.
[1643.40 → 1646.92] And then it compiles a response using an LLM.
[1646.92 → 1650.08] So that's like the basics of the course.
[1650.42 → 1655.48] And the reason we wanted to do this was because of a hackathon that we did.
[1655.82 → 1661.32] Actually, funny enough, right before the LLMs in production conference, we did a hackathon in San Francisco.
[1661.32 → 1666.22] And it was all about how bulletproof your LLM stack is.
[1666.78 → 1678.86] And so we created a bunch of questions, and we gave everyone that was part of the hackathon all the data from the Flops community Slack, which this Slack has been around since 2020.
[1678.86 → 1681.56] And there's like 17,000 people and it's very active.
[1681.56 → 1684.76] Like all the channels are going off every day.
[1684.86 → 1686.14] It is very, very active.
[1686.46 → 1690.70] I can't remember how many megabytes there were, but for text data, it was a lot.
[1690.70 → 1694.48] It was people were saying like, oh my God, that's a serious amount of text.
[1694.90 → 1697.52] So everyone had access to that.
[1697.56 → 1708.22] And then we would rate everyone's stack on how accurate the answers were from the questions and answers that we gave them.
[1708.22 → 1715.54] So we basically asked people to build these different QA bots or chatbots, if you would call it that.
[1715.54 → 1723.82] And then at the end of the hackathon, we gave them 100 questions, and we saw how accurate were these responses.
[1724.62 → 1733.20] And so the questions were some things that were from Slack, or they were just random questions about ML and Flops.
[1733.20 → 1742.36] And the best ones were the ones that would give you an accurate answer and then cite, oh, but you know, this is another way of looking at it.
[1742.44 → 1744.04] And here's a thread on it.
[1744.18 → 1746.10] And so it would go back to the Slack thread.
[1747.02 → 1750.84] So all that being said, yeah, we're excited about the course.
[1750.92 → 1752.14] We're excited to do that.
[1752.14 → 1755.56] I mean, there are all kinds of cool stuff that I want to do in the community.
[1755.56 → 1761.50] And the only way that I'm able to do it is that people in the community are participating in this.
[1761.58 → 1764.30] I said Raul is the guy that created this course.
[1764.30 → 1768.38] We've got all kinds of other courses in the mix from other community members.
[1768.38 → 1775.34] So people that are experts on what they feel like they know best, they can propose topics.
[1775.34 → 1777.82] And then we're just putting it on our learning platform.
[1777.82 → 1782.56] And where do people go to find said learning platform?
[1782.76 → 1786.10] Because I need to point a couple of my coworkers to it.
[1787.14 → 1795.60] Well, if you just want rants from me about how you shouldn't fine tune, then you can find us on the Flops community podcast.
[1796.12 → 1803.32] But the easy one is we have learn.flops.community.
[1803.32 → 1807.44] And that should get you to the learning section of our website.
[1807.82 → 1810.30] And yeah, as I said, it's exciting.
[1810.44 → 1815.42] It's a little bit like nerve wracking because we plan on doing two styles.
[1815.42 → 1819.34] This one that we just released is go at your own pace.
[1819.34 → 1829.60] You get it, and then you can go through the lessons, and hopefully you can get your company to pay for it because it's within the learning budget.
[1829.60 → 1831.96] And it actually is for work, right?
[1831.96 → 1833.74] So that should be an easy sell.
[1833.74 → 1843.50] But if your boss is not interested in paying for it, just DM me and I will give you some amazing copy that you can send to your boss.
[1843.74 → 1848.70] A nice little email that will hopefully convince them to change their mind.
[1848.70 → 1855.26] But the other pieces that we're going to start doing like cohort based courses.
[1855.58 → 1864.14] And that is interesting on another level because we've got the whole Flops community, and we've got everyone that is part of the courses.
[1864.14 → 1866.38] They can go into a special Slack channel.
[1866.58 → 1870.48] They can be with the teachers and the teacher's assistants and all that fun stuff.
[1870.48 → 1873.96] I mean, it's not like we're breaking any new ground here.
[1874.08 → 1877.72] Courses are kind of a tried and true method of learning.
[1878.24 → 1881.30] So this is just us having fun with it.
[1881.68 → 1882.38] Yeah, that's awesome.
[1882.66 → 1887.72] And speaking of learning, you already mentioned the surveys that you've been doing.
[1888.46 → 1892.50] And there's a previous survey that it's already published.
[1892.60 → 1895.78] I know you're working on the next survey that will come out.
[1896.32 → 1898.16] But people should look at this survey.
[1898.16 → 1900.50] We'll definitely link it in our show notes.
[1901.08 → 1904.86] And there's a lot of fascinating stuff in the survey.
[1905.68 → 1909.22] And some of the highlights, I'll just call out a few of the highlights here.
[1909.76 → 1915.36] And then I'd be curious to know what stood out to you, Demetrius or Chris, whichever one.
[1915.46 → 1918.58] So some of the highlights just at a high level.
[1919.26 → 1922.68] Company use cases like text generation and summarization are useful.
[1922.68 → 1927.72] But participants are going deeper and exploring a lot of other ways to use LLMs.
[1928.16 → 1934.70] Like data enrichment and data labelling augmentation generation for subject-matter experts and other things.
[1935.08 → 1936.00] It's still unclear.
[1936.28 → 1943.36] The use of large language models in organization is still unclear due to some high costs and unclear ROI.
[1943.94 → 1945.36] They talk about hallucinations.
[1945.36 → 1952.52] The speed of inference with LLMs being potentially a blocker for certain types of use cases.
[1952.94 → 1954.56] You talk about the infrastructure.
[1954.56 → 1957.24] We already talked about that stack a little bit.
[1957.66 → 1962.88] Some of the things around augmentation and consistency of models.
[1963.14 → 1968.90] So those are just some of the highlights from the survey, which people can go into a lot more detail on.
[1968.90 → 1979.14] But I guess one question I would have is, as you were building this report, first off, is the whole report generated using an LLM?
[1979.58 → 1982.26] Because I didn't see that highlighted in the report.
[1982.90 → 1984.88] That would be the most meta thing ever, huh?
[1986.26 → 1989.44] Not the company meta, just the old term for meta.
[1989.44 → 1991.98] So that is classic.
[1992.44 → 1992.66] Yeah.
[1994.10 → 1997.80] And honestly, I tried really hard.
[1997.96 → 2003.52] But one thing that I did, which I'm going to preface this with, I am not Gardner.
[2003.70 → 2008.08] And so I did not know how to create reports before I did this.
[2008.08 → 2009.28] Now I've learned since.
[2009.34 → 2010.30] I learned what was painful.
[2010.48 → 2020.60] And I spent months with this data and just tearing it apart, trying to figure out what are some clear signals here.
[2020.90 → 2023.10] And you can find the signals.
[2023.32 → 2036.20] But the reason that it was so difficult and that it was a blessing and a curse was every single question, instead of having answers given to you, it was just a free-form text box.
[2036.20 → 2038.66] And so this is the report that we created.
[2038.66 → 2044.20] But the actual raw data, it's linked in the report and anybody can see it.
[2044.28 → 2048.28] And so I'm a big fan of that because I have my biases.
[2048.28 → 2059.58] I wrote this report, but the report is for the people that don't have the time or want to go and spend hours upon hours looking through all the raw data.
[2059.92 → 2061.14] Fine-tuning a model on it.
[2061.30 → 2061.58] Yeah.
[2062.10 → 2065.26] They're like, give me the TLDR, and I'm good.
[2065.26 → 2068.44] And so that's kind of what I set out to do.
[2068.58 → 2072.74] And I also wanted to see what are some big things that stood out to me.
[2072.80 → 2082.42] But not only me, every time, I think the reason it took me so long to release this was that I would ask a cohort of friends to review it.
[2082.50 → 2089.42] And they would give me feedback, and I would incorporate that feedback and then be like, okay, I think I can send it off to the designer now and let's get it going.
[2089.42 → 2096.10] And next thing you know, I would ask another cohort of friends to review it or people in the community.
[2096.36 → 2099.28] And boom, I would have all kinds of new feedback.
[2099.60 → 2103.04] And oh, but you know, I noticed that there was this and people were talking about that.
[2103.20 → 2106.28] So I did that probably six or seven times.
[2106.28 → 2116.10] And that gave me the confidence that it's still biased, but it's not like as crazy biased as I think it would have been if I just put it out myself.
[2116.10 → 2118.74] And I got a lot of input from other people.
[2118.84 → 2122.18] So if anything, it's biased from a lot of different people.
[2122.18 → 2124.56] And so there's that piece.
[2124.84 → 2131.16] And what we're doing with, again, like the evaluation survey, I want to do the same exact thing.
[2131.40 → 2132.94] I learned my lesson.
[2133.24 → 2137.00] So it's not only free text form answers that you have now.
[2137.08 → 2146.38] I kind of put a lot of multiple choice and check all boxes that apply and then also the other at the end.
[2146.38 → 2154.10] So hopefully that will help me be able to do more Excel fancy math on it and formulas.
[2154.70 → 2163.82] Because even with LLMs, I was even trying all these new ones that, you know, it was use ChatGPT in your Google Sheets.
[2164.06 → 2164.94] It didn't work.
[2165.12 → 2170.94] I spent days trying to ask it questions, and it just did not work, man.
[2170.94 → 2182.80] And I ended up getting kind of frustrated because I spent more time trying to get the LLM to give me some kind of insight than if I just spent the time with the data and got the insight.
[2182.94 → 2191.64] And I think everybody who has played around with LLMs has probably had that experience once or twice where it's like, I've been prompting this for a really long time.
[2191.64 → 2200.00] I wonder if I just sat down and wrote the report or if I sat down and tried to think of things on my own and create something.
[2200.22 → 2204.50] I could have just done it in the amount of time that I've been prompt tuning this.
[2204.94 → 2205.74] But anyway.
[2206.54 → 2208.30] I get a question as I'm looking at it.
[2208.60 → 2217.34] Like, obviously, it's a population of people like us that are answering the questions because, you know, right off the bat, it's like, how many of you are using LLMs in your company?
[2217.34 → 2221.10] And it's 61%, you know, which is a pretty high number right there.
[2221.30 → 2226.38] But I'm curious, do you go through and like, what constitutes using an LLM?
[2226.62 → 2231.88] Can it be as simple as pulling up a prompt for ChatGPT and, you know, posing prompts to it?
[2231.98 → 2234.96] Or does it need to be like putting in your company data?
[2235.20 → 2235.60] Right.
[2236.14 → 2236.92] There you go.
[2237.26 → 2238.26] Oh, my God.
[2238.42 → 2239.50] Everyone owns it now.
[2239.64 → 2239.92] Yeah.
[2241.04 → 2242.28] Oh, that's so funny.
[2242.28 → 2244.80] I would love to talk about that for a minute, too.
[2245.02 → 2252.38] But yeah, it was there were only a few people that were just like, oh, yeah, I'm just using ChatGPT.
[2252.60 → 2256.34] And I'm going directly to OpenAI's website.
[2256.86 → 2259.16] That was not the majority.
[2259.28 → 2262.04] I think it was like one person, if I remember correctly.
[2262.04 → 2267.36] And don't quote me on that, because it's been probably two months since we put this out.
[2267.36 → 2270.96] And so I can't remember anything since we put it out.
[2271.24 → 2277.34] But it's more people that are trying to set up systems with LLMs.
[2277.60 → 2286.64] And so these systems may be the API calls to OpenAI, or they may be hosting their own open source LLMs.
[2286.64 → 2287.28] Right.
[2287.62 → 2296.12] And what's unique or what questions are you intrigued to find the answers to in the upcoming survey?
[2296.66 → 2302.24] Maybe there are some commonalities that you'd like to see carry through the surveys.
[2302.54 → 2307.32] But what are you most curious about going forward into this next round?
[2307.78 → 2315.14] I'm really fascinated by how many people are using open source versus using OpenAI.
[2315.14 → 2323.18] And one of the most hated visuals of the whole report is this one on like page 10.
[2323.66 → 2326.80] And it's talking about who's using OpenAI and what size they are.
[2327.14 → 2331.46] And people were like, this does not explain anything.
[2331.60 → 2333.26] You're what you're trying to say.
[2333.26 → 2335.12] And the visual do not match up at all.
[2335.18 → 2337.82] And so, again, I am not Gardner.
[2337.82 → 2343.52] I am one random guy who has never written a report, never did a survey.
[2343.64 → 2347.88] But for some reason, I felt compelled to do this three months ago, five months ago now.
[2348.16 → 2350.26] And I almost regret it.
[2350.38 → 2353.64] But seeing the final product, I'm very happy that I did it.
[2353.76 → 2355.18] And so, yeah, you should be proud.
[2355.46 → 2357.28] There's always things to look back on.
[2357.54 → 2358.84] But yeah, it's a nice report.
[2359.00 → 2359.66] It's a good one.
[2359.92 → 2360.40] Exactly.
[2360.40 → 2363.00] And we were able to move fast on it.
[2363.18 → 2366.12] And so I'm sure Gardner is going to put something out soon.
[2366.64 → 2370.96] But that's the beauty of the community that we can move a little bit faster.
[2371.30 → 2374.36] Anyway, back to this visual that people did not like.
[2374.80 → 2377.10] And I mean, like a lot of people did not like it.
[2377.28 → 2381.82] So the whole idea was, are you using OpenAI?
[2381.82 → 2389.98] And we found that there's a bit of a correlation between people that are in tiny startups,
[2390.56 → 2392.84] like zero to 50.
[2393.32 → 2395.26] Zero, I mean, one to 50.
[2395.94 → 2396.82] And so...
[2397.50 → 2398.70] It's an autonomous startup.
[2399.40 → 2400.64] Yeah, exactly.
[2401.14 → 2402.88] It's so starting.
[2403.08 → 2404.98] It's so startup-y.
[2404.98 → 2411.30] So anyway, the one to 50 range, they're not using OpenAI.
[2411.82 → 2415.48] And the 1,000 plus are not using OpenAI.
[2415.74 → 2421.38] But the 500 to 1,000, and the numbers that I'm throwing out here,
[2421.56 → 2425.86] I didn't preface this because I got into the startup thing and the zero to 50.
[2426.10 → 2428.98] The amount of employees that you have at your company,
[2429.44 → 2433.98] so if it's one to 50, then you're not using OpenAI.
[2433.98 → 2436.68] If it's 1,000 plus, you're not using it.
[2436.96 → 2439.78] At least that's the preliminary data that we saw.
[2440.32 → 2442.12] And if you're in the middle, then you are.
[2442.20 → 2443.84] And so we had some theories about this.
[2443.88 → 2447.82] And it was like, hmm, I wonder if it's because if you're a startup,
[2448.50 → 2453.48] you think that you can create a moat by not using it.
[2453.52 → 2459.54] And maybe your whole business is around using some kind of LLM
[2459.54 → 2464.52] and creating some kind of difference than OpenAI.
[2464.52 → 2472.10] And then if you're a larger company, A, this was before the enterprise scam that they've got going on.
[2472.18 → 2474.60] But that's, again, we can get into that in a minute.
[2475.18 → 2480.44] And so if you're a larger company, you probably have resources to figure it out yourself.
[2480.44 → 2484.34] And you don't necessarily need to use OpenAI.
[2484.34 → 2490.38] And you're probably less comfortable with your data going outside your walled garden.
[2490.72 → 2491.78] I think it's the latter.
[2492.18 → 2492.34] Yeah.
[2492.54 → 2495.32] If you're in the middle, it's like, let's just go as fast as we can.
[2495.94 → 2501.14] And so I want to see if that theory, if that holds up in the next one.
[2501.56 → 2501.72] Yeah.
[2501.82 → 2504.88] If you're over 1,000 people, you have a legal department.
[2505.02 → 2505.18] Yeah.
[2505.62 → 2507.12] And that's what's inhibiting you.
[2507.26 → 2508.22] Good point, Chris.
[2508.38 → 2508.78] Good point.
[2508.78 → 2517.68] But now, I mean, Chris, you tell me, man, like, do you think that this enterprise play is going to work out?
[2517.94 → 2519.34] Do you think people are going to trust them?
[2519.34 → 2522.02] In terms of OpenAI's enterprise?
[2522.82 → 2527.14] I do think it will work out from a business standpoint for them.
[2529.54 → 2532.54] I get dangerously close to some conflict of interest here.
[2532.62 → 2534.56] So I'm going to pass on this one.
[2535.42 → 2536.58] You're going to plead the fifth.
[2537.06 → 2538.02] I'm pleading the fifth.
[2538.02 → 2539.76] I'm pleading the fifth.
[2540.00 → 2541.86] So I'm backing away from this question.
[2542.18 → 2546.70] It sounds like you're not on the enterprise hype train, Demetrius.
[2546.90 → 2549.92] I work for a company that's 1,000 plus is what I'm saying.
[2550.02 → 2551.86] So I'm going to back away from that question.
[2551.94 → 2553.10] He's got a legal department.
[2553.46 → 2554.80] We have a legal department.
[2554.98 → 2556.48] Some of them might listen to this podcast.
[2558.28 → 2558.76] Exactly.
[2559.34 → 2560.16] I just wonder.
[2560.30 → 2563.40] I mean, I've been Memling with friends about it.
[2563.40 → 2570.86] And I think it's kind of funny how they do say they specifically call out, we're not going
[2570.86 → 2573.26] to use your data to train any of our models.
[2573.66 → 2575.70] We're not going to know about any of your data.
[2575.70 → 2582.08] And I think that the biggest question is like, oh, yeah, because they have the best track
[2582.08 → 2584.04] record of doing what they say.
[2584.96 → 2588.96] There is a healthy skepticism, I would say, in among large companies on that.
[2589.08 → 2589.44] Definitely.
[2589.44 → 2589.76] Yeah.
[2589.76 → 2590.36] Yeah.
[2590.60 → 2592.34] Well, also, I don't know.
[2592.52 → 2598.62] This is kind of avoiding the question a little bit, but I think that it is related in that
[2598.62 → 2603.22] you brought up the leaderboards earlier, Demetrius.
[2603.56 → 2612.70] And I think any company that goes all in, it's almost like a new version of vendor lock-in,
[2612.70 → 2620.82] like we used to talk about, where now you have model family lock-in, where, hey, these models,
[2621.06 → 2621.74] they're good.
[2622.06 → 2623.10] I'm no doubt.
[2623.72 → 2625.72] GPT models, perfect.
[2626.08 → 2632.52] Are they going to be the models that are going to be best for your use case, either in terms
[2632.52 → 2638.76] of output or in terms of the other things that are highlighted in your survey, right?
[2638.76 → 2645.60] Like latency and resources and a lot of these practicalities and how you can control them
[2645.60 → 2647.08] and all this stuff.
[2647.38 → 2648.54] You know what they need, don't you?
[2649.06 → 2650.02] Yeah, exactly.
[2650.48 → 2655.16] And so I think there is an element here of like, hey, do I want to go all in on a single
[2655.16 → 2656.22] model family?
[2656.86 → 2664.92] Or does my strategy play more to have a bit more of model agnostic approach where I can pivot
[2664.92 → 2669.80] between different models for different uses, maybe fine tune when I need to.
[2669.98 → 2675.96] But even if I don't fine tune, I have a lot of potential options to use and in a privacy
[2675.96 → 2676.92] conserving way.
[2677.10 → 2679.22] So yeah, I think that that's another element.
[2679.88 → 2681.94] However that works out, it will work out.
[2681.94 → 2688.18] But I think there's this kind of side element here, which is how the model landscape is evolving
[2688.18 → 2693.82] versus a single model family is evolving, which is good to highlight.
[2693.82 → 2694.80] So true.
[2695.24 → 2701.84] And actually, you know, it's funny, like, I don't want to say that there is not an immense
[2701.84 → 2710.38] amount of value in ChatGPT and GPT-4 because one thing has become very clear after interviewing
[2710.38 → 2713.56] a ton of people who are using large language models in production.
[2713.56 → 2723.48] They are able to get up and running and proving value with their LLM so quickly.
[2723.98 → 2727.60] And I was just talking to Thibault.
[2727.98 → 2728.62] Thibault.
[2728.82 → 2731.58] I'm going to have to check how I pronounce his name.
[2731.66 → 2732.20] He's French.
[2732.40 → 2735.26] And it's spelled very different from how it's pronounced.
[2735.26 → 2738.60] And he's running the LLMs at AngelList.
[2739.14 → 2745.44] And I asked him, hey, so are you worried about that vendor lock-in type thing because you're
[2745.44 → 2747.34] only on OpenAI?
[2747.72 → 2751.60] Have you messed around with even just Anthropic or Cohere?
[2751.60 → 2757.62] And I thought his answer was fascinating because he told me, look, you know what?
[2758.10 → 2765.02] There are so many other pieces of surface area that I would like to cover, so many other
[2765.02 → 2771.68] features that I would like to implement with these LLMs and be able to use in our product
[2771.68 → 2778.68] that if I'm stuck on one feature and trying to figure out what the best model is, then that's
[2778.68 → 2779.42] going to slow me down.
[2779.42 → 2783.82] I just want to go and get as many features plugged in as possible.
[2783.98 → 2787.36] And I know that ChatGPT works really well.
[2787.88 → 2793.94] And so I'm just going to go as hard as I can and incorporate these features because I have
[2793.94 → 2797.58] a laundry list of them that I want to do.
[2798.08 → 2803.06] And then once I get all of that out of the way, then I can start going back and saying,
[2803.12 → 2805.96] OK, let's figure out, should we bring a model in-house?
[2806.08 → 2808.38] Should we use Claude or something else?
[2808.38 → 2811.48] You know, it's fascinating to hear you say that because that's such a startup
[2811.48 → 2812.04] mentality.
[2812.26 → 2816.48] You know, we just have to run really fast and get as much done as we possibly can in the
[2816.48 → 2817.42] the shortest possible time.
[2817.66 → 2822.06] And then you get to that large organization thing, and they're worried about the lock-in,
[2822.16 → 2825.44] they're worried about where their data is going, and they go much slower, you know,
[2825.44 → 2826.56] as a result of that.
[2826.62 → 2831.46] It's almost like an inverted, you know, approach based on size of the company and maturity.
[2831.46 → 2837.64] And that's what I was trying to show in this horribly positioned visual graph that you see
[2837.64 → 2839.08] on page 10 of the report.
[2839.48 → 2846.22] So we've finally got to the conclusion that the graph, we all agree on the point that the
[2846.22 → 2847.48] graph is showing.
[2848.56 → 2852.58] And to leave the graph out of it, I think that that's good.
[2852.72 → 2852.90] Yeah.
[2853.10 → 2853.88] Don't look at a graph.
[2853.88 → 2858.54] I'm sorry, he's laughing because we can all see each other even though this is audio only
[2858.54 → 2859.72] and he's laughing at himself.
[2860.78 → 2866.48] Not to belabour the point, but I think like you all are exactly right.
[2866.48 → 2874.08] And I think I see this because almost every lead that's coming into prediction guard, just
[2874.08 → 2877.76] in terms of where people are at, regardless of whether they're a good fit for what we're
[2877.76 → 2882.32] doing or not, but almost every lead that's coming in, it's almost laughably predictable
[2882.32 → 2889.84] that they say, hey, we've prototyped out something very quick with open AI that shows like there's
[2889.84 → 2891.46] huge value here.
[2892.12 → 2893.50] Now, what do we do?
[2893.50 → 2897.28] It's almost every conversation is starting like that.
[2897.56 → 2902.10] So yeah, I think that there's even like a temp, you know, we can make your graph.
[2902.26 → 2907.64] I think we should make your graph like sideways and add like a temporal element, make it 3D
[2907.64 → 2908.48] over time.
[2908.58 → 2914.16] People like that more where like, you know, at the beginning of a project, I think a lot
[2914.16 → 2917.72] of people are doing that, whether they're authorized to do it or not in their organization.
[2918.06 → 2922.30] And then they get to that point where like, how do we scale that up, especially if we're
[2922.30 → 2924.66] in this larger organization environment?
[2925.26 → 2927.54] Yeah, it's like, oh, I got to go present this to the C-suite.
[2927.80 → 2933.44] We got to erase any use of sending data outside our company.
[2934.00 → 2935.78] We can't tell anybody about that.
[2936.08 → 2936.82] Yeah, exactly.
[2937.78 → 2945.36] As we're coming close to the end here of our and friends episode, which I hope is only the
[2945.36 → 2949.04] second of many times we'll get to hear from you on the show, Demetrius.
[2949.58 → 2953.74] As you're looking to the next, I don't even feel like we could go to the next year.
[2953.94 → 2960.18] Like as you're looking to the next couple of months of AI life, what are you hyped about?
[2960.42 → 2966.08] Like just generally across the industry, like what positive kind of trends are you seeing
[2966.08 → 2968.46] that give you hope for where things are headed?
[2968.46 → 2971.62] Let's see.
[2971.74 → 2972.94] That is a great question.
[2973.12 → 2975.66] Leading question, but great question.
[2976.20 → 2977.94] It's got to be the positive side, huh?
[2978.02 → 2978.92] We got to stay on.
[2979.36 → 2980.78] End on a positive note.
[2980.96 → 2984.40] You can dip though before you get there if you want to though, just for fun.
[2984.46 → 2985.86] Because I want to hear what he has to say.
[2986.30 → 2989.90] Well, for those that are just listening, I am wearing tie-dye.
[2989.90 → 2992.40] So it is all peace and love here.
[2992.76 → 3002.72] And I am excited because right now, anyone who wants to mess around with machine learning
[3002.72 → 3004.64] and AI, they can.
[3004.82 → 3012.82] I have seen so many scenarios where a product person has said, you know what, let's try and
[3012.82 → 3014.14] throw some AI with this.
[3014.14 → 3021.98] And they've been able to create an enormous amount of value for their company by adding
[3021.98 → 3026.78] some features that just call ChatGPT or Claude or whatever.
[3027.38 → 3035.26] And that for me is really enticing because the barrier to entry has just been destroyed.
[3035.52 → 3040.10] You know, it almost was like the last couple of years, the first couple of years of the
[3040.10 → 3046.26] ML Ops community, we are, I mean, we still are, there's still a lot of traditional machine
[3046.26 → 3052.34] learning where I put it in quotation marks because it's not that old, but there's a lot
[3052.34 → 3057.30] of really hard stuff happening with quote unquote traditional machine learning.
[3057.56 → 3064.74] But with the advent of LLMs, a lot of that has become really easy.
[3064.74 → 3073.32] And so all these NLP tasks that were really hard up until 2022, they're not as hard.
[3073.54 → 3080.28] And so you're seeing the creativity of people being able to put LLMs into their products.
[3080.40 → 3081.28] I love that.
[3081.46 → 3091.14] That is something that now I didn't realize how much I enjoyed product and the idea of speaking
[3091.14 → 3097.64] with product people until ChatGPT came out because now I'm like, oh, I want to talk to
[3097.64 → 3099.04] more product people.
[3099.48 → 3104.68] The product owners are really great people to talk to because they have these wild ideas
[3104.68 → 3109.50] and they know how to figure out if this is actually a success or not.
[3109.68 → 3113.08] So there's that piece and dovetailing on that.
[3113.66 → 3117.32] So we're having another LLMs in production conference on October 3rd.
[3117.32 → 3123.94] I don't know if I told you guys this, but definitely come, and I will explain why.
[3124.00 → 3126.72] I'll try and sell it to you as much as possible right now.
[3126.72 → 3132.78] But I wanted to create as many talks from product people as possible.
[3133.48 → 3139.82] And some of the stuff that we are talking about are like how to build an economical LLM solution
[3139.82 → 3147.20] and how to prioritize LLM use cases and how to put LLMs into your product.
[3147.56 → 3152.80] So those are very much for the product owners and the product engineers.
[3153.96 → 3155.54] And it's because of that.
[3155.66 → 3163.56] It's really like I got really excited now that this whole space has been opened up to the product
[3163.56 → 3163.94] owners.
[3163.94 → 3169.18] And so can I tell you what you can expect in the conference?
[3169.62 → 3170.22] Of course.
[3170.40 → 3170.66] Sure.
[3170.84 → 3174.92] I'm just going to tell you why it is the greatest conference on the internet right now.
[3175.20 → 3176.38] Because where else?
[3176.86 → 3178.60] And Daniel can attest to this, all right?
[3178.74 → 3180.40] Live music interludes?
[3180.72 → 3181.06] Yes.
[3181.18 → 3183.86] Where else can you prompt me?
[3184.24 → 3185.06] Not an LLM.
[3185.14 → 3189.10] You can put in the chat what you want me to sing about.
[3189.10 → 3193.46] And I will sing it in real time, just improvising on my guitar.
[3194.48 → 3198.74] And last time we had a whole song about catastrophic forgetting.
[3199.12 → 3204.34] And for those who do not know, that is where actually, I'm not even sure I fully understand
[3204.34 → 3204.88] what happens.
[3204.98 → 3208.46] But basically, like when you fine tune going, it's all that damn fine-tuning.
[3208.74 → 3216.04] When you fine tune, sometimes a model will forget something because its new data is replaced
[3216.04 → 3221.88] with, it replaces the old data, but the catastrophic forgetting song was a hit.
[3222.22 → 3228.32] You've also got some semi-illegal betting going on during the breaks, and you win swag.
[3229.08 → 3231.78] And then semi-illegal betting?
[3232.16 → 3234.00] There's a gray area, Chris.
[3234.54 → 3234.86] Okay.
[3235.46 → 3237.40] Depends on what country you're in, all right?
[3237.40 → 3243.26] And so that you also can expect.
[3243.52 → 3252.16] I mean, I'm just not sure that I've seen any conference that goes into the amount of technical
[3252.16 → 3254.18] details that we go into.
[3254.48 → 3259.02] And I want to highlight this piece, and we can end with this.
[3259.02 → 3269.54] It is really hard, but it is very important for me to have a fully diverse field of speakers.
[3270.00 → 3274.60] And so I cannot tell you how much work it is.
[3274.72 → 3280.90] And it frustrates me now that I've looked at other conferences and I see it's almost like,
[3281.02 → 3282.60] oh, these organizers were lazy.
[3282.60 → 3290.00] You know, because there are amazing people out there from underrepresented groups that
[3290.00 → 3294.86] are doing some incredible stuff, but you almost have to look a little more because they're
[3294.86 → 3297.48] not necessarily on the conference circuit.
[3297.74 → 3298.72] They're busy shipping.
[3299.28 → 3300.18] Like, let's be honest.
[3300.18 → 3302.94] They're not out there talking about it.
[3303.00 → 3304.24] They're actually just doing it.
[3304.36 → 3311.62] And so I've had to look really hard, but I am very excited about the speakers that we
[3311.62 → 3315.04] have and the diversity of our speakers.
[3315.46 → 3320.96] And I think that that's probably like out of all the things I'm proudest about, that's
[3320.96 → 3322.28] probably what I'm the proudest about.
[3322.74 → 3323.24] That's awesome.
[3323.56 → 3324.52] Yeah, I can't wait.
[3324.76 → 3327.34] And you said it was October 3rd.
[3327.66 → 3328.48] Is that right?
[3328.58 → 3329.38] October 3rd.
[3329.44 → 3329.78] Awesome.
[3331.00 → 3338.12] I'm going to be so we have one sponsor for this event, and they rented a whole studio in
[3338.12 → 3340.92] Amsterdam and Amsterdam is like four hours from where I live.
[3340.92 → 3346.30] And so hopefully, you know, everything goes all right.
[3346.38 → 3350.98] I don't like to eat any mushrooms or anything or smoke too much weed and not show up for
[3350.98 → 3351.98] the actual event.
[3352.76 → 3356.58] But in case that does happen, we have shirts.
[3356.68 → 3357.92] Did you see the shirts, Daniel?
[3358.22 → 3362.36] I think I've only seen the ones I hallucinate more than ChatGPT.
[3362.48 → 3363.00] That is it.
[3363.54 → 3365.72] I may live that in Amsterdam.
[3365.98 → 3366.48] You never know.
[3367.42 → 3368.94] Oh, how can I get one of those?
[3368.94 → 3371.20] Yeah, I'll share the link with you.
[3371.32 → 3372.30] We've got special.
[3372.46 → 3375.44] They only pop up for sale during the conferences.
[3376.08 → 3380.90] So you can't get them now, but hopefully about a week before the conference starts, we'll
[3380.90 → 3382.30] start selling them again.
[3382.74 → 3384.04] And yeah, that's it.
[3384.10 → 3385.14] That's what I've been up to.
[3385.52 → 3389.48] Not too much, you know, just trying to stay relevant.
[3389.74 → 3390.40] Just keeping things chill.
[3390.74 → 3390.88] Yeah.
[3390.96 → 3391.12] Yeah.
[3391.12 → 3394.08] That's awesome.
[3394.20 → 3397.10] Well, thanks so much, Demetrius, for joining us.
[3397.34 → 3401.58] I hope that we see you again here in some number of months.
[3401.78 → 3404.04] Don't stay away too long.
[3404.04 → 3410.64] And we'll look forward to hearing about the results of the survey, the events, and I'm
[3410.64 → 3415.10] sure all the like 15 new things that you're doing next time around that you're not doing
[3415.10 → 3415.82] this time around.
[3416.38 → 3416.52] Totally.
[3416.52 → 3418.20] Dude, I got so many ideas.
[3418.44 → 3419.94] I have so many.
[3420.16 → 3421.20] I mean, yeah.
[3421.30 → 3426.82] I really appreciate you guys letting me come on here and rant about fine-tuning and talk
[3426.82 → 3429.70] about the cool stuff we're doing in the Flops community.
[3429.90 → 3431.18] And I love what you all are doing.
[3431.32 → 3432.02] So thank you.
[3432.16 → 3432.72] It was fun.
[3432.86 → 3433.18] Thanks.
[3433.36 → 3434.04] We'll see you soon.
[3434.04 → 3445.10] Thank you for listening to Practical AI.
[3445.64 → 3449.42] Your next step is to subscribe now, if you haven't already.
[3449.88 → 3454.56] And if you're a longtime listener of the show, help us reach more people by sharing Practical
[3454.56 → 3455.90] AI with your friends and colleagues.
[3456.36 → 3461.28] Thanks once again to Vastly and Fly for partnering with us to bring you all Change Talk podcasts.
[3461.28 → 3465.66] Check out what they're up to at Fastly.com and Fly.io.
[3466.06 → 3470.42] And to our Beat Freakin' residents, Break master Cylinder, for continuously cranking out the
[3470.42 → 3471.38] best beats in the biz.
[3471.66 → 3472.56] That's all for now.
[3472.82 → 3473.98] We'll talk to you again next time.
