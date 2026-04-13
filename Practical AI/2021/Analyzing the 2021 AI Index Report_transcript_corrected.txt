[0.00 → 9.40] I would say the generative stuff worries me the most in the short term because it can be taken advantage of so easily, and it's so accessible to such a wide audience.
[9.52 → 15.20] And the output is of such high quality that it can make you question what is real.
[15.58 → 28.74] And when you are shaping the data or the information that gets to people that they are choosing to process, and you can channel that, and you can target people, it can make the whole system fall apart if you let it go far enough.
[28.74 → 37.46] And so that worries me in the short term a lot more than AI becoming sentient and taking over the world.
[40.08 → 42.76] Big thanks to our partners, Linde, Vastly and Launch Darkly.
[43.00 → 43.72] We love Linde.
[43.78 → 45.20] They keep it fast and simple.
[45.34 → 47.70] Check them out at linode.com slash changelog.
[47.92 → 50.00] Our bandwidth is provided by Vastly.
[50.34 → 53.90] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[54.16 → 55.86] Get a demo at LaunchDarkly.com.
[58.74 → 68.14] This episode is brought to you by merit and their upcoming ML Data Ops Summit in partnership with TechCrunch.
[68.30 → 71.30] It's a virtual event happening December 2nd, 2021.
[71.86 → 75.70] Check out the speakers and register at iMerit.net slash Data Ops.
[75.70 → 87.46] The event is gathering more than 700 attendees from top AI and ML companies and feature major speakers, including Facebook AI, Cruise, Zoo, GE Healthcare and more.
[87.46 → 92.38] And I'm here with Ivan Lee, the founder and CEO of Data sore, who's also speaking at the event.
[92.76 → 98.44] Ivan, I know you'll be speaking at the conference on this subject, but can you share a teaser of what's happening right now in the NLP space?
[98.82 → 112.22] If we look at the advances in NLP over the last few years, there have been some really exciting developments, perhaps most notably OpenAI's GPT-3 and their ability to just really start mimicking humans in generating snippets of English language.
[112.22 → 118.10] What we've noticed is that perhaps of all the branches of AI, NLP is one of the most mature.
[118.44 → 121.94] And there were some obvious use cases when we were starting out.
[122.10 → 127.34] There are things like the ability to handle customer support, improve upon chatbots.
[127.64 → 131.32] These were very clear verticals that we wanted to go after.
[131.32 → 138.94] But as we learned more, it turns out there are applications in the legal industry, in healthcare, in financial.
[139.40 → 148.98] There were a number of nonprofit organizations using us to label COVID-19 research and be able to just make sense of all the abundance of research that was coming out.
[149.30 → 153.88] We were kind of astounded by the creativity and the ways in which NLP could be produced.
[153.88 → 159.72] All right, learn more and register to attend for this free virtual event at imerit.net slash data ops.
[159.92 → 166.36] Again, you'll hear from top AI and ML speakers who have successfully deployed machine learning data operations in their organizations.
[166.84 → 169.62] Again, this event is free and it's virtual.
[170.18 → 173.68] Learn more and register at imerit.net slash data ops.
[183.88 → 195.36] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[195.68 → 199.74] This is where conversations around AI, machine learning, and data science happen.
[200.12 → 204.78] Join the community and Slack with us around various topics of the show at changelog.com slash community.
[204.78 → 206.12] And follow us on Twitter.
[206.26 → 207.82] We're at Practical AI Effect.
[213.88 → 218.00] Welcome to another fully connected episode of Practical AI.
[218.32 → 223.50] This is where Chris and I keep you fully connected with everything that's happening in the AI community.
[223.84 → 231.34] We'll take some time to discuss the latest AI news, and we'll dig into learning resources to help you level up your machine learning game.
[231.94 → 232.98] I'm Daniel Whiten ack.
[233.06 → 235.84] I'm a data scientist with SIL International.
[236.10 → 240.96] And I'm joined as always by my co-host, Chris Benson, who is a strategist at Lockheed Martin.
[241.44 → 242.12] How are you doing, Chris?
[242.52 → 243.60] I'm doing very well, Daniel.
[243.60 → 244.46] How's it going today?
[245.42 → 247.24] It's going good.
[247.80 → 256.64] I have some paper deadlines or paper submissions coming up very soon.
[257.12 → 259.30] So here in like a week and a half.
[259.48 → 270.46] So a lot of my life right now is finishing up graphs and writing things and revising things and making sure references are put together and all of that fun stuff.
[270.96 → 271.36] Understood.
[271.36 → 279.02] You know, I work for a big company these days, and we have all the usual PowerPoint and Word documents to navigate ourselves.
[279.80 → 279.98] Yeah.
[280.20 → 280.40] Yeah.
[280.62 → 282.14] Well, sometimes that's more difficult.
[282.22 → 286.64] I feel like my Google Drive, it includes so much.
[286.64 → 296.80] But it's really hard sometimes to navigate and find what I want, which I think actually we talked about on a recent episode, or you talked about with a guest on a recent episode.
[296.92 → 297.00] Yep.
[297.42 → 297.64] Yeah.
[297.64 → 298.64] I feel the pain there.
[298.64 → 299.14] I feel the pain there.
[299.38 → 312.74] But yeah, mostly my life right now is thinking about should this line be coloured, or should I do dashed lines or what font size should this be?
[313.28 → 314.34] All of those fun things.
[314.34 → 316.34] I sympathize with you.
[316.34 → 326.32] I imagine most of the people in our audience sympathize with you as well because we, you know, talking about technology and data science rather than actually doing it.
[326.32 → 342.78] Yeah, it's definitely useful though in terms of communicating what you've been working on helps you yourself also formulate like, oh, this was sort of like a nice story arc that we did.
[342.78 → 345.64] Or maybe there's like gaps in our thinking.
[346.36 → 357.72] Usually it's the latter where you sort of try to formulate, and you're like, oh, I really should have like done that in addition to the other things to sort of fill in the gaps of our thinking.
[358.22 → 360.92] Or at least that's normally how it happens for me.
[360.94 → 360.96] Yeah.
[361.32 → 364.18] And I got to say, you have a great attitude about it.
[364.84 → 370.20] I just hopefully solitarily when I'm doing it, but I just whine.
[370.36 → 371.14] I just complain.
[371.14 → 373.22] I just go, oh, God.
[373.24 → 374.62] Well, I'm not saying I never do that.
[374.62 → 374.94] Oh, God.
[375.02 → 379.44] I got to do a bunch of PowerPoint slides before two o'clock today or whatever.
[379.72 → 380.14] So, yeah.
[380.64 → 381.58] Great attitude, man.
[381.62 → 383.60] You're like, oh, if I do this, I can learn from it.
[383.64 → 384.40] I'm just like grumbling.
[384.72 → 384.88] Okay.
[386.00 → 386.36] Yeah.
[386.54 → 386.80] Yeah.
[386.92 → 391.26] Well, we'll see how I feel tonight after another day of that.
[391.88 → 392.16] Yeah.
[392.26 → 395.42] Well, today we've got a fully connected episode.
[395.42 → 408.04] So, there were a few things that came across our path over the last couple of weeks that I think we were texting to one another and saying, hey, it'd be perfect to chat through some of these things.
[408.04 → 415.66] One was the updated AI index report from Stanford University.
[416.20 → 418.50] Another one, though, so we'll move on to that.
[418.64 → 423.94] Actually, we went to that AI index and discussed it last year.
[423.94 → 429.10] But in this year, there's an updated version, which we want to talk through.
[429.78 → 445.52] But before we do that, maybe there's a quicker one that I had, which is this article that I saw originally in the IEEE spectrum called Machines Learn Good from Common Sense Norm Bank.
[445.96 → 451.40] New moral reference guide for AI draws from advice columns and ethics message boards.
[451.62 → 453.00] Very, very interesting.
[453.00 → 454.04] So, that caught my attention.
[454.20 → 457.66] I don't know if that seems interesting to you, Chris.
[457.66 → 457.68] It did.
[457.78 → 459.12] I thought we might talk about it for a second.
[459.12 → 461.62] I read the article when you brought it up, and it is interesting.
[462.06 → 464.24] And it's funny.
[464.52 → 470.12] There are so many different approaches to AI ethics out there because there's no standard way.
[470.24 → 471.54] We're so early days still.
[472.12 → 481.00] And I like the fact that they were literally like, well, let's just go to the ethics folks and see what they have to say and see if we can train it that way, which is very practical.
[481.00 → 483.50] For practical AI, I thought that hit the mark.
[483.70 → 485.36] So, interesting article.
[485.66 → 486.90] It was interesting for sure.
[487.22 → 494.96] In some sense, it seems a little bit like, I don't know, a little meta for me that we're training models.
[494.96 → 498.36] So, maybe I should describe the premise of the thing.
[498.56 → 498.82] True.
[498.82 → 512.12] So, the premise of the thing is like, okay, we're all talking about like how we need sort of like ethical and moral considerations on how we build AI models and the decisions that they make and all of that stuff.
[512.12 → 513.70] So, a lot of people are talking about this subject.
[513.70 → 529.94] So, in this work, Allen AI or some researchers at the Allen Institute for AI used a bank of sort of common sense moral judgment data to train a model to make moral judgment calls.
[529.94 → 540.26] That's why I mean it's sort of maybe a little bit meta in that like we see that there's a problem that we need to consider ethics around AI.
[540.56 → 545.16] So, let's train an AI to determine certain ethical things.
[545.62 → 546.02] I don't know.
[546.30 → 549.38] Maybe that's like that's one thing that just sort of struck me.
[549.52 → 549.84] It is.
[550.06 → 552.58] But I would argue how can they go wrong?
[552.58 → 558.02] I mean they're actually using Dear Abby, you know, the advice column as one of their bases.
[558.30 → 560.14] So, you know, one of the data inputs that they're using there.
[560.22 → 564.20] I mean, which raises a little tiny side point I just need to raise.
[564.62 → 567.70] I'm in my early 50s and Dear Abby has been around all my life.
[567.80 → 570.48] I'm just saying Abby must be really, ancient at this point.
[571.18 → 571.58] Yeah.
[571.74 → 572.74] Yeah, that's probably true.
[573.10 → 574.34] Maybe Abby is an AI.
[574.58 → 575.38] Oh, wow.
[575.44 → 576.70] Maybe she always has been.
[576.86 → 578.40] Maybe we're living in a simulation.
[578.54 → 579.58] I won't go down that rabbit hole.
[579.86 → 579.98] Okay.
[580.32 → 580.50] Yeah.
[580.62 → 581.06] Okay.
[581.06 → 588.00] On that note, I'm just reading through the data here that they're using.
[588.40 → 597.74] And what it talks about is to train the model, they use this common sense norm bank, which
[597.74 → 605.50] is a collection of 1.7 million examples of people's ethical judgments on a broad spectrum
[605.50 → 607.78] of everyday situations.
[608.28 → 608.98] Very interesting.
[608.98 → 615.70] I'm just looking at one of the things that's highlighted here, which I think is, or I don't
[615.70 → 620.02] know if it's exactly represented like this in the data set, but the sort of highlighted
[620.02 → 625.34] example here they have is killing a bear to please your child is bad.
[625.98 → 628.84] Killing a bear to save your child is okay.
[629.64 → 633.46] Exploding a nuclear bomb to save your child is wrong.
[633.46 → 641.66] So I guess when they say this is ethical judgments on a broad spectrum of everyday situations, I
[641.66 → 644.18] guess everyday situations include nuclear bombs.
[644.30 → 644.84] I guess so.
[645.02 → 648.68] I mean, and we all have access to exploding, apparently.
[649.12 → 650.94] It's a curious example.
[651.74 → 652.28] So I don't know.
[652.44 → 652.72] Yeah.
[652.72 → 659.90] So this is very interesting that there's different sort of aspects of the same kind of entities
[659.90 → 662.56] or things represented in this data set.
[662.56 → 670.36] My understanding, and if anyone from the Allen Institute is listening, they can come on the show and go into more detail.
[670.46 → 674.96] But my understanding is they trained this model on this data set.
[675.16 → 689.50] And then they actually employed some crowd workers using Mechanical Turk to evaluate a thousand examples of example moral judgments from the model.
[689.50 → 706.84] And so doing this, they found that the model, which they called Delphi, achieved 92.1% accuracy compared with lower accuracies for other sort of existing models like GPT-3, which we've talked about before on the show.
[706.84 → 722.20] So, yeah, I mean, I guess nine out of 10 moral judgments from the model, at least on an average from crowd workers seem to be justified or right or, you know, however you want to put it.
[722.48 → 727.50] There is one little side thing I want to hit here since they mentioned, I think you're the right person for me to ask of.
[727.60 → 732.48] And that is GPT-3 with its much lower performance overall.
[732.48 → 734.92] What do you think that says?
[735.02 → 743.48] I mean, GPT-3 was, you know, from a massive, you know, amount of the internet being sucked in as a source and processed.
[744.34 → 749.26] Would that imply that the internet is, you know, the context?
[749.68 → 750.18] Less moral?
[750.28 → 750.74] I don't know.
[751.22 → 761.66] Or at least is the context of ethics largely absent from the internet in terms of how different material out there is presented?
[761.66 → 764.72] Just, you know, on any given website that they happen to pull from?
[765.10 → 772.64] It's interesting that they really, they had to focus on something to give it the context, to give it the specificity of that.
[773.22 → 777.64] Well, I would have to read a little bit more into how they use GPT-3.
[777.64 → 788.34] I mean, certainly I would agree that large portions of the internet are immoral, but that's like separate from my own, any of my views of anything related to AI.
[788.48 → 791.90] But, you know, just based on my own thinking.
[791.90 → 806.12] But when you use GPT-3, typically you're looking at sort of few shot scenario where you have this pre-existing language model and you sort of start feeding it examples of the type of thing that you want it to do.
[806.64 → 808.58] And then it starts doing this action.
[808.58 → 824.84] Now, I don't know exactly how they sort of, how much of the maybe the common sense norm bank they used in terms of fine-tuning GPT-3 or if it was truly, you know, few shot or something like that.
[825.28 → 829.00] So I'd have to read a little bit more there to understand it.
[829.00 → 839.40] But I think that GPT-3 is sort of this general purpose model and the Delphi model was very specifically trained to do this task.
[839.56 → 843.72] So it's not, not incredibly surprising to me that it performed better.
[843.84 → 849.90] And I think, you know, that's good that people are thinking about this, this side of things.
[849.90 → 858.36] It's definitely, there's a lot of sort of common sense, complicated, subtle things that happen with language.
[858.36 → 868.10] And I think the Allen Institute for AI has done a lot of thinking with regard to common sense and, you know, pitfalls that many language models fall in.
[868.22 → 875.44] So I'm glad this seems to be a continuation of some of their thinking with regard to that subject.
[875.44 → 879.14] And that's, you know, that's good from my perspective, I think.
[879.14 → 884.56] I'm looking as you're saying that at one of the other highlights that they have just below.
[884.56 → 893.22] And they note that the system stumbled on time of day judgments is running a blender rude at 3 p.m. or 3 a.m.
[893.74 → 898.86] And unfamiliar topics as well, such as sports and law regarding, you know, what they were doing there.
[899.50 → 907.08] Do you have any thoughts on why some things might be easier or harder than others in NLP models in terms of picking up on that?
[907.08 → 920.04] Yeah, I mean, it's still an open topic of research, probably, because a lot of what happens in these large models is not incredibly interpretable.
[920.04 → 925.04] So I think that's an open area of research.
[925.04 → 938.34] But I know that there have been a lot of well, I don't know about what would people consider a lot, but there's been some work with regard to sort of adversarial NLP examples.
[938.88 → 951.76] And we've talked about those, I think, very briefly in certain times on the show where so like for sentiment analysis, if you're to say, I really love the United States, you know, that might be judged by a model as positive.
[951.76 → 956.50] And then you could say, I really love Turkey.
[957.08 → 968.86] But then all of a sudden, by just changing the United States to Turkey, then it's viewed as a negative because most of the examples in the data set regarding Turkey are probably some sort of like negative examples.
[968.86 → 989.02] And, you know, there's an underlying behaviour of the model that isn't really probed until you do this sort of adversarial examples, which is probably true in this case as well, where there's just, you know, topics or scenarios that aren't well represented in the data or very scarcely represented.
[989.02 → 994.24] And so that might play into the behaviour for sure.
[994.94 → 1000.32] But yeah, I mean, it's interesting to see if others will try similar things to this.
[1000.60 → 1006.62] And maybe, you know, AI models can start writing their own ethics principles for AI models.
[1006.76 → 1007.56] That would be interesting.
[1007.56 → 1020.00] And to that kind of to that point, they also note in the article when you're talking about it writing its own that this particular model tends to reflect the status quo, the cultural norms of today's society.
[1020.00 → 1031.38] And yet we know that with, you know, to tie this into another topic that we've hit a bunch of times with this type of automation becoming more and more pervasive in every aspect of our lives.
[1031.38 → 1041.70] We know that our society, our culture has to change to accommodate, you know, work, you know, humans at work or not at work and others such as that.
[1041.98 → 1057.08] It would be interesting if we could use a model, maybe a next generation of this that can talk about what might be ethical in a different society that's reachable going forward to help us get there and use AI to help us solve the AI at work problem.
[1057.66 → 1060.22] I did just read a little bit further along.
[1060.22 → 1072.52] They do make us, you know, some statement about the explainable and transparent part saying they'd like to grow the data set since at the current stage, it's hard to know why exactly it said what it did.
[1072.84 → 1076.30] So that kind of gets to your gets to your previous point.
[1076.56 → 1078.92] And sounds like they'll have more for us in the future.
[1079.06 → 1079.40] Absolutely.
[1079.88 → 1085.14] And we can put in the show notes, the paper that this is based on is called Delphi Towards Machine Ethics and Norms.
[1085.14 → 1087.96] And we can include that for people to go read as well as the article.
[1090.22 → 1103.38] We deserve a better internet and the Brave team has the recipe for bringing it to us.
[1103.52 → 1104.52] Start with Google Chrome.
[1104.76 → 1108.46] Keep the extensions, the dev tools and the rendering engine that make Chrome great.
[1108.68 → 1109.54] Rip out the Google bits.
[1109.68 → 1110.32] We don't need them.
[1110.68 → 1113.18] Mix in ad and tracker blocking by default.
[1113.18 → 1116.16] Quick access to the Tor network for true private browsing.
[1116.52 → 1120.86] And an opt-in reward system so you can get paid to view privacy respecting ads.
[1121.06 → 1124.82] Then turn around and use those rewards to support your favourite web creators like us.
[1125.16 → 1129.74] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1129.74 → 1142.94] Okay, Chris.
[1143.10 → 1148.28] Well, last year, I don't know if we'd consider this a follow-up fully connected episode.
[1148.28 → 1158.42] But last year, we did talk about the AI Index Report, which came out from the Stanford Institute for Human-centred Artificial Intelligence.
[1159.44 → 1163.10] And we have an updated version of that for this year.
[1163.20 → 1170.14] There's sort of a bit of a summary article, which I think you ran across also in IEEE Spectrum.
[1170.14 → 1178.96] But you can also look directly at the AI Index Annual Report site, and they have some sort of major takeaways as well.
[1179.64 → 1182.04] So, yeah, this is, as always, very interesting.
[1182.30 → 1190.20] I encourage any practitioners who are working in the space to take a look at this and to see what some of the trends are from the past year.
[1190.20 → 1202.58] I'll start off by just mentioning that the number one takeaway that the Stanford site mentions is that AI investment in drug design and discovery increased significantly.
[1203.44 → 1214.52] So there's more than $13.8 billion of investment in this area, apparently, four and a half times higher than in 2019.
[1214.52 → 1220.20] I don't know what possibly could have spurred on that shift.
[1220.96 → 1221.00] Yeah.
[1221.22 → 1222.30] What could it be?
[1222.46 → 1223.56] Hmm, pandemics.
[1223.84 → 1227.00] What sort of health-related thing happened in the past couple years?
[1227.00 → 1229.86] And yet they don't mention that in their lineup.
[1230.34 → 1231.40] But it's interesting.
[1231.60 → 1234.88] It is notable in that it's a very specific use case.
[1235.46 → 1239.14] And the surrounding ones that we'll hit in a moment are a little bit more general than that.
[1239.14 → 1248.36] And that was the very first thing I noticed when we started looking through the article before the show was just how I was like, wow, okay, that's number one.
[1248.54 → 1249.84] They're calling the attention out there.
[1250.26 → 1256.10] So it'll be interesting to see over the next few years when this goes with drug development.
[1256.10 → 1271.82] Yeah, I know that there have been efforts for some time in sort of protein folding and genomics, bioinformatics as related to AI techniques.
[1272.78 → 1275.72] And it sounds like that that's increasing a lot.
[1275.72 → 1284.02] But now sort of in the commercial sector where people are maybe where I heard about it a little bit more was on the academic and research side.
[1284.14 → 1287.14] So it sounds like this is shifting a little bit into industry.
[1287.96 → 1297.50] It's a difficult problem with a lot of data that is also very large and complicated data like genomics data or bioinformatics data.
[1298.56 → 1303.44] And AI is particularly good at those sorts of problems.
[1303.44 → 1308.36] So, yeah, it'll be interesting to see how people apply this.
[1308.54 → 1315.38] And also how one of the things I'm always thinking about is how are the experts going to be involved in the loop with the model?
[1315.82 → 1324.36] So are they giving some hints to the model to as it sort of probes the landscape of drug design?
[1324.62 → 1332.12] I'm guessing that not all the people working in drug design won't be a part of the process moving forward.
[1332.12 → 1337.10] And I'm not in that field, so I don't know exactly what sort of input they might give.
[1337.28 → 1340.82] But I hope that, you know, that's being thought about as well.
[1341.04 → 1341.18] Indeed.
[1341.72 → 1345.20] The next one they mention is the industry shift continues.
[1345.84 → 1355.90] And what they're talking about there is they note that 65% of graduating PhDs in North America in the AI space went into industry instead of staying in academia.
[1355.90 → 1361.44] And that's up fairly substantially from 44.4% a decade ago.
[1361.78 → 1363.72] And when I think about that, I think about you, Daniel.
[1363.88 → 1365.30] You represent that trend.
[1365.68 → 1377.62] And when I think about our guests on the show over the last three years, we've had many, many people with PhDs in either this or related field, or they've migrated into this field.
[1377.98 → 1380.96] And the majority of them have been in industry as opposed to academia.
[1380.96 → 1381.76] We've done both.
[1381.76 → 1384.94] I think the show represents that trend very directly.
[1385.86 → 1386.04] Yeah.
[1386.36 → 1394.74] And I'm a little bit curious as to, and I'll have to do a little bit more reading if, you know, what the category of PhDs in AI quote is.
[1394.74 → 1403.14] I know that, you know, part of my background, like you said, is, you know, from physics and in physics, you know, at the time.
[1403.22 → 1409.06] And I think, I think it continues to today, although I haven't followed it as much as in physics.
[1409.06 → 1426.10] There hasn't been, like, paradigm sort of shifting things happening for the most part, if you look on the whole, you know, since the sort of 20s and 30s, 1920s and 30s and, you know, the huge revolution that happened.
[1426.10 → 1438.96] And certainly there have been advances, but because of that, the sort of investment and the amount of academic positions in physics weren't that many and is very highly competitive, right?
[1438.96 → 1447.72] So you might end up doing, like, three postdoctoral positions, you know, before you end up getting a tenure track position.
[1448.04 → 1455.90] And then, you know, you're still not quite to, like, a stability yet because you've got to go through the, you know, tenure type stuff.
[1455.90 → 1457.92] So, yeah, it's very difficult.
[1458.34 → 1461.70] I'm sure that that impacts other fields as well.
[1462.10 → 1478.82] But when you can, you know, come out of your PhD and still do sort of cutting edge research, but at a cool place, like whether it's Google Brain or the Allen Institute or, you know, a cool startup like Hugging Face or something like that.
[1478.82 → 1490.22] And you're still writing papers, but you're into it, and you can have a little bit more of your own research agenda and participate significantly sort of out of the gate and also not teach.
[1490.44 → 1491.76] A lot of people don't like to teach.
[1493.06 → 1497.32] It's pretty appealing, not to mention that the salaries are higher.
[1497.32 → 1509.00] So it will be interesting to see how much is drained out of academia and if the competition for academic positions changes as a function of this.
[1509.36 → 1509.38] True.
[1509.80 → 1513.30] The next thing they mention is generative everything.
[1513.60 → 1522.94] They talk about the fact that text, audio, images are so high standard at this point that it's pretty hard to tell the difference.
[1523.06 → 1524.04] And that's true.
[1524.04 → 1531.74] I've noticed that on a number of AI driven services with, you know, generative output, you would think a human road.
[1532.14 → 1532.66] Yeah.
[1532.94 → 1534.96] And it's kind of multimodal at this point.
[1535.04 → 1540.08] I mean, used to they had sort of images or images of people or something like that.
[1540.20 → 1552.72] But I know that we've had people on the show thinking when we talked about machine learning for music and generative music or text in the case of GPT-3 or something like that.
[1552.72 → 1564.08] Is that like in your as you think about AI and the know what you worry about in terms of applications of AI?
[1564.22 → 1570.98] Does that factor into like something that weighs on your mind that, you know, generative things are out there?
[1571.06 → 1572.22] It's hard to tell the difference.
[1572.52 → 1574.72] There could be a contribution to fake information.
[1574.72 → 1575.12] Oh, sure.
[1575.12 → 1577.68] Is that that factor up there in your mind?
[1577.74 → 1582.50] I know you do a lot of thinking on sort of ethics, principles and strategy.
[1582.60 → 1586.00] I mean, at the at that level, it's its a huge concern.
[1586.48 → 1587.98] Governments are concerned about it.
[1588.76 → 1590.46] Corporations are concerned about it.
[1590.96 → 1593.12] I think people should be concerned about it.
[1593.38 → 1597.76] It's one of those things we've we've let the genie out of the bottle and the genie is really convincing.
[1597.76 → 1602.40] And yet it is quite difficult to tell the difference between the genie and the human.
[1602.92 → 1616.58] So if you're putting tooling out there with a specific agenda around it that maybe the affected parties might consider nefarious, then if there are a lot of things that we have to sort through.
[1616.58 → 1618.88] I think, you know, that's one thing we've learned.
[1618.96 → 1621.70] We started with the ethical conversation at the beginning of this.
[1621.84 → 1631.76] But there are so many areas in A.I. that we have not figured our way through in terms of how to have a safe, productive, good world with these tools.
[1631.90 → 1638.64] It's not that the tools are bad, but they fall in the hands of people who were out to affect an agenda.
[1638.64 → 1641.82] So it definitely affects all of us.
[1641.94 → 1643.64] And it's definitely something I worry about.
[1643.64 → 1660.94] So in terms of your own just day to day thinking, when you're talking to your families or family or others about A.I., what should be prioritized as maybe the biggest problem that we're facing with A.I.?
[1660.94 → 1667.04] Is it the sort of talent and diversity among that talent within the A.I. community?
[1667.04 → 1670.88] Is it like generated generative things and misinformation?
[1671.52 → 1673.50] Is it bias in data sets?
[1673.50 → 1678.26] Is it A.I. becoming sentient and, you know, taking over the world?
[1678.80 → 1683.56] What what what's on your mind as you're as you're talking to people?
[1683.94 → 1693.12] I would say the generative stuff worries me the most in the short term because of those issues, because it can be taken advantage of so easily.
[1693.12 → 1695.98] And it's so accessible to such a wide audience.
[1695.98 → 1701.54] And the output is of such high quality that it allows us.
[1701.62 → 1709.72] I mean, we've really seen this over the last few years here in the United States, in particular, in our political system, is that it can make you question what is real.
[1709.72 → 1720.86] And I have really, perfect friends here in the American Southeast that see the world in a completely different perspective.
[1721.06 → 1723.20] You know, everything about the world is different to them.
[1723.20 → 1726.88] It's almost like we don't live on the same planet in the same country.
[1727.38 → 1741.92] And when you are shaping the data or the information that gets to people that they are choosing to process, and you can channel that, and you can target people, it can make the whole system fall apart if you let it go far enough.
[1741.92 → 1756.90] And so that worries me in the short term a lot more than AI becoming sentient and taking over the world and eating us all as, you know, Matrix Neo's or whatever, you know, or non Neo's, maybe.
[1757.44 → 1758.90] That may someday become a problem.
[1759.00 → 1759.48] I don't know.
[1759.88 → 1762.62] But it's not the problem that we have today or in the near future.
[1762.62 → 1766.16] But the problem of understanding what our reality is.
[1766.56 → 1771.10] I know that's real because I can talk to some of my very closest friends.
[1771.10 → 1773.42] It's its completely different stuff.
[1773.62 → 1780.54] Well, one of the interesting links that you forwarded along to me, Chris, was so there's the AI index itself.
[1780.54 → 1790.82] But then I triple A spectrum did a sort of take on the index, which is titled 15 graphs you need to see to understand AI in 2021.
[1791.44 → 1796.78] I would recommend people if is they don't want to read the whole index, this is a good.
[1797.28 → 1798.04] Well, I don't know.
[1798.08 → 1800.46] This is pretty much always what I do when I read a paper.
[1800.58 → 1800.76] Right.
[1800.76 → 1805.60] You read out the paper and you sort of like flip through and look at the graphs and see what catches you.
[1806.24 → 1811.42] Maybe, maybe other people aren't as vain as me and just looking at pictures.
[1811.42 → 1813.64] But that's normally what I do there for.
[1814.04 → 1814.64] Yeah, exactly.
[1814.90 → 1818.46] So this is an interesting sort of take on everything.
[1818.46 → 1834.66] One of those graphs that stood out to me, which I think is a fascinating idea with a whole variety of implications and aspects is that they say, number three, faster training equals better AI.
[1834.66 → 1844.52] So in other words, training has become faster based on certain AI training of models has become faster.
[1845.00 → 1852.72] They talk about the standard ImageNet data set and training, training a state-of-the-art model on that data set.
[1852.72 → 1857.44] But in 2018, it took 6.2 minutes to train the best system.
[1857.56 → 1861.42] And in 2020, it took 47 seconds.
[1861.42 → 1874.44] And of course, this is due to a lot of the advancement and sort of accelerator chips and distributed training and, you know, specialized hardware that's designed specifically for AI and machine learning.
[1874.44 → 1896.02] And the implication is that, you know, if you're able to run your experiment in like 30 seconds rather than waiting like three hours, then you can run it a lot of different ways with different parameters and all of that stuff and eventually get to a better model than you would have if you were is your training was slower.
[1896.02 → 1900.68] To me, to some degree, training is getting faster.
[1901.22 → 1915.58] And so that makes me encouraged because we're also having a significant sort of like sustainability problem in AI where like these large language models and other ones, it takes so long to train and it takes so much power.
[1915.58 → 1932.66] So it's great if you can run things faster, but then if is you can run things faster, then maybe you just end up running more things rather than like not needing to run as many things for as long, which, yeah, is kind of the other side of this, I guess.
[1932.66 → 1944.66] Put simply, if you have models that can be trained that much faster, you have a lot more options because it's still humans on a human timescale on a human day at work that are doing that are putting these together.
[1945.26 → 1946.78] We're still filling those hours.
[1946.94 → 1951.86] And if you can train many more times in the given a given span of time, then you get better stuff.
[1952.30 → 1957.36] I thought a lot of the things that were in this made a lot of common sense.
[1957.64 → 1960.46] That being one of them is you have more options.
[1960.46 → 1963.24] And I don't see that slowing down anytime soon.
[1963.60 → 1971.08] So there are also a couple of graphs about citations and some sort of like implications of that.
[1971.22 → 1974.96] The one that they've labelled is we're living in an AI summer.
[1975.10 → 1975.30] Yep.
[1975.56 → 1981.90] Where if you sort of look at the graph and this is what's hard about being on a podcast with only audio.
[1981.90 → 1992.32] But if you look at the graph of sort of citations per year, number of AI citations and journal articles per year, that percentage or number.
[1992.32 → 1996.66] And you look at that graph over the years, it's sort of from 2000.
[1996.66 → 1998.70] It kind of is rising up, rising up.
[1998.76 → 2008.38] And then it kind of maybe plateaus or even goes down a bit to where I remember people were talking about, hey, well, now we're just like the peak has happened.
[2008.38 → 2014.18] And now we're just sort of going back into some type of winter or normality or something like that.
[2014.18 → 2018.18] But then it comes sharply back up again in 2019 and 2020.
[2019.10 → 2023.54] This chart I found really, fascinating because we've had that conversation ourselves.
[2023.54 → 2027.18] And I've been one of those people that was a little bit disappointed.
[2027.18 → 2035.82] But if you look at the dates on it with it rising steadily up to 2013, 14, and then kind of taking a dip over the next few years.
[2035.96 → 2038.88] And then once again, starting that uptrend in 2019.
[2039.34 → 2042.04] It made me realize the perception of what's happening.
[2042.16 → 2045.58] AI trails the publications of the research papers a bit.
[2045.58 → 2059.68] Because if you look at the over three years you and I have been doing the show, a good bit of those early episodes were kind of catching up and us educating ourselves and educating folks in our audience about all the research that had already happened.
[2059.86 → 2062.02] And then we kind of went through that.
[2062.30 → 2065.70] And I was, you know, going back to me at the beginning of the show talking about whining.
[2065.80 → 2066.76] I'll whine a little for a second.
[2067.00 → 2074.24] And I was whining that, wow, we haven't, it hasn't felt like we had big breakthrough things like we used to feel like were happening a lot.
[2074.24 → 2076.22] But I think we have.
[2076.36 → 2080.90] It's just taking us a little while for those to get out in the space and people to take advantage of it.
[2081.14 → 2085.40] At least that's how I'm interpreting the data I'm looking at, given the little bit of time lag.
[2085.54 → 2092.12] So I would say that bodes very well for us continuing to have these great conversations.
[2093.00 → 2094.14] Yeah, yeah, for sure.
[2094.44 → 2102.56] The other trend within the citations that they note is that China takes the top citation honours.
[2102.56 → 2117.12] And one of the things that they highlight about sort of AI research in different geographic locations or countries is that China sort of has a stated policy of getting journal publications.
[2117.12 → 2119.20] They really push for that.
[2119.86 → 2125.96] Whereas in the U.S., maybe a good portion of AI R&D happens in corporations.
[2125.96 → 2140.86] And so if you're in a corporation, and you're doing AI research, generally, you know, this isn't true across the board, but you might have less of an incentive to publish journal articles, especially if the company is wanting to keep trade secrets.
[2140.86 → 2148.26] Or if maybe you're just trying to get the product finished or advance something or whatever.
[2148.50 → 2154.18] Or if there are national security implications, which is something I'm obviously familiar with in my industry.
[2154.18 → 2162.32] Yeah. So this wouldn't maybe be saying that the U.S. isn't doing an increasing amount of AI research.
[2162.32 → 2167.12] But in terms of the publications, China is definitely now dominating.
[2167.98 → 2171.14] And, you know, they've they've put a lot of investment in that area.
[2171.14 → 2173.70] And so it's not, not surprising.
[2173.70 → 2180.12] And they keep their numbers keep rising, and they keep doing more and more AI research.
[2180.12 → 2184.40] So, yeah, it's definitely maybe changing the landscape.
[2184.64 → 2186.64] It is. It is. And we've been watching that trend.
[2186.84 → 2188.62] You know, you know, we've gotten the crossover.
[2188.80 → 2190.16] We've been watching that for a while.
[2190.62 → 2191.42] It was expected.
[2191.90 → 2195.62] The big question mark is with their focus on publishing.
[2196.06 → 2198.66] And yet we know that there's a lot of unpublished research.
[2198.76 → 2203.92] What's the delta between what's published, and what's not on the non-China side?
[2204.14 → 2205.34] I can't help but wonder.
[2205.34 → 2206.92] Yeah. Yeah.
[2207.66 → 2214.38] Another interesting fact that they talk about in this report is the global AI job market.
[2215.04 → 2219.08] So I know a lot of our listeners, you want an AI job.
[2219.36 → 2221.12] Talk to many of you about it.
[2221.54 → 2228.16] And so this, I know, is an interesting, interesting aspect of what people are thinking about and interested in.
[2228.16 → 2238.28] And the AI index talks about Brazil, India, Canada, Singapore, and South Africa as having the highest growth in AI jobs.
[2238.42 → 2247.10] And so we're thinking of strong representation in Asia and Latin America in AI jobs, which is fascinating.
[2247.10 → 2264.02] I remember a few years ago, I visited AI Singapore, which was a really, you know, innovative and great effort that the government and universities in Singapore were behind in terms of, you know, becoming a leader in that area.
[2264.02 → 2279.58] And so, yeah, there's, you know, countries are promoting this and trying to establish AI talent in these places, not just sort of have AI practitioners from those places go to other places to do their AI work.
[2279.58 → 2285.56] Yeah, I agree. There are a couple of points they make, and it's actually in both the IEEE spectrum.
[2285.84 → 2289.28] They highlight, you know, some of this, and it's also in the core article.
[2289.76 → 2295.20] They note that AI continues to have a diversity of challenge in terms of its practitioners.
[2295.92 → 2302.24] And then, you know, relative to diversity, you just now were talking about those different countries where it's really on the rise.
[2302.46 → 2309.04] But they also note that the majority of US AI PhD grads are from abroad and that they're staying in the US.
[2309.58 → 2321.36] It's an interesting mixture of how that all shapes together and looking at it, you know, but I can't help but ask along the way, why do you think that most of our PhD grads are from abroad?
[2321.36 → 2333.48] Any thoughts or opinions or anything on that versus, you know, why are we not attracting here in the United States more students that want PhDs in AI and get out there in industry?
[2333.62 → 2334.56] What do you think is happening with that?
[2335.12 → 2335.78] Yeah, I don't know.
[2335.78 → 2345.32] I mean, there are a lot of things factoring into the makeup of grad students and PhD students.
[2346.02 → 2351.34] And I'm probably not an expert in that area to comment.
[2351.34 → 2362.20] But I think there is a trend sort of for and I don't know if you picked up on this, but it seems a little bit like from the US side of things.
[2362.20 → 2372.70] If you think about and look at some sort of like data science, either data science curriculum or boot camps or content that's out there on the internet.
[2372.70 → 2378.28] Used to, I think it was fairly common for a data scientist to be a PhD.
[2378.28 → 2400.72] But now I think people are promoting more of the path of like data science as a sort of post undergrad career where you can sort of come out of a computer science background and into data science, not necessarily as a researcher, but as a data science practitioner, a non PhD data science practitioner.
[2400.72 → 2407.74] My guess would be that that would have grown, but while maybe the PhDs are staying more static.
[2407.92 → 2409.84] I mean, to some degree, that's me.
[2410.00 → 2416.30] You know, earlier I said something reminded me of you, but I'm not a PhD and I come from a software development background.
[2416.30 → 2425.66] And my perspective was to pick up data science as yet another skill set to add value into the types of activities I was trying to accomplish.
[2426.22 → 2430.04] Speaking empirically, I see that in the people around me a lot.
[2430.28 → 2436.02] And so, yeah, rather than going all the way through on the PhD track to just go ahead and get out there and start doing it.
[2436.02 → 2445.60] But it's one of many things that they're doing, which actually leads me to one other thing that I don't see on either of the article or called out in the report.
[2445.68 → 2449.90] It may be in the report because it's 222 pages and I have not read that whole report.
[2449.96 → 2459.34] I focused on the highlights, but it doesn't call out anything about job concerns and stuff, which is a huge thing on people's mind at this point.
[2459.60 → 2464.26] I have people ask me about that just knowing me from the show and stuff all the time.
[2464.26 → 2468.70] It's one of the most common subjects that people approach me on, but I don't see anything in there.
[2468.84 → 2478.52] Do you think they've they've missed things or maybe that's maybe that would have been the 16th takeaway in the article or the 10th takeaway in the source.
[2478.68 → 2485.18] And by concerns, do you mean like the availability or competition for positions or?
[2485.52 → 2489.60] Yeah, I mean, you have so much automation happening out there.
[2489.96 → 2493.14] Oh, I see the impact of AI on other on jobs.
[2493.14 → 2496.78] And I'm seeing that a lot and in different communities.
[2496.96 → 2516.12] And a lot of times it's pretty subtle now that you now that deep learning deployment has become cheap, if you especially is you have a very specific focus, and you're seeing really common mundane tasks being replaced by automation that has this benefit of deep learning to help drive what its task is.
[2516.12 → 2518.20] I have people ask me about that a lot.
[2518.20 → 2521.70] I'm wondering, but maybe that's you know, maybe it's not a key takeaway.
[2522.04 → 2523.58] Maybe we're not quite there yet.
[2523.72 → 2524.18] What do you think?
[2524.64 → 2537.50] Yeah, it could be that it's a lot of companies that are trying to introduce that automation still need a similar workforce, but maybe just doing slightly different things.
[2537.50 → 2549.26] So there's maybe not as many areas where automation is completely taking away positions, but they're more morphing that position into something else that that might be a guess.
[2549.26 → 2556.72] But maybe it's just not a massive change in the past year with respect to that.
[2556.86 → 2563.56] It's sort of still happening as it was in previous years or something like that and not as much of an acceleration.
[2563.56 → 2569.96] And in sort of the automation of jobs away factor seems to be like something we can make an acronym for.
[2570.76 → 2580.52] Yeah, so I encourage our listeners will post the links to the report and IEEE article, which goes through the different graphs on that.
[2581.12 → 2586.92] I have one thing that I wanted to highlight in these episodes, the fully connected episodes.
[2586.92 → 2606.98] We always like to do a learning resource or two for listeners and something came across my Twitter feed, and I was looking into a little bit more because I'm also helping connect some of our practitioners with some professional development opportunities here at SIL.
[2606.98 → 2613.40] But Hugging Face now has a Hugging Face course for transformer models.
[2613.40 → 2620.80] So the course includes things like an introduction to natural language processing and transformers.
[2620.90 → 2621.80] What can they do?
[2621.90 → 2623.24] How do transformers work?
[2623.40 → 2634.26] Encoder models, decoder models, sequence to sequence models, talking about bias and limitations, using transformers, fine-tuning a pre-trained model and sharing models and tokenizers.
[2634.26 → 2650.24] So this is really, it seems like a great time for this to exist as Hugging Face now has integrations with even sort of multimodal things like speech and image related models.
[2650.48 → 2662.82] And so learning about transformers, learning about how to share models and work with data sets using an open source framework like Hugging Face data sets, all of that seems super relevant and timely.
[2662.82 → 2670.34] So if you're interested, I highly recommend that you check out the Hugging Face course and learn a little bit about that.
[2670.46 → 2672.44] So we'll include a link in our notes.
[2673.06 → 2674.64] I think I'm going to go do that one myself.
[2675.56 → 2675.78] Yeah.
[2675.92 → 2681.74] And it includes some sort of video components, text and images and yeah, check it out.
[2682.52 → 2691.96] Well, Chris, it's been perfect to perfect to chat through some of these things and revisit the AI index this year and talk through some of it.
[2691.96 → 2697.16] Thanks for pointing me to it and for talking through some of the points.
[2697.48 → 2701.34] I'll look forward to talking to you about it again next year.
[2701.48 → 2706.64] It was a good conversation this week and good, interesting material like always this year.
[2706.86 → 2708.32] And I will talk to you next week.
[2708.72 → 2709.30] Sounds good.
[2712.82 → 2713.82] That's our show.
[2714.02 → 2714.66] Thanks for listening.
[2715.18 → 2717.46] For more like this, check out our Master Feed.
[2717.46 → 2721.54] It is all Changelog podcasts in one easy to consume place.
[2721.90 → 2726.78] Let your podcast app snag everything we produce and then pick and choose which ones to listen to.
[2727.06 → 2733.14] Subscribe today at changelog.com slash master or just search for Changelog Master in your podcast app of choice.
[2733.40 → 2733.94] You'll find it.
[2734.46 → 2739.20] Special thanks to Break master Cylinder for providing our music and to our longtime sponsors,
[2739.58 → 2741.44] Vastly, Launch Darkly and Linde.
[2741.96 → 2743.28] That's all for this week.
[2743.54 → 2744.74] We'll talk to you again next time.
[2744.74 → 2774.00] Game on.
