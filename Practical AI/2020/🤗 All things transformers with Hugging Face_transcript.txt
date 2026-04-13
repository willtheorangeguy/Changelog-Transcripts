[0.00 --> 6.24]  One thing that we think is really interesting is that unlike generic model hubs like TensorFlow's hub or PyTorch's hub,
[6.38 --> 12.14]  because our models are all of the same form, we can build a lot of tools and machinery around using them.
[12.14 --> 15.90]  So for instance, we have a visualizer that works for all of our models.
[16.20 --> 20.30]  You can just upload your own model and get really interesting visualization of its internal structure.
[20.60 --> 25.82]  Or this open source project called TextAttack built an adversarial attack system,
[25.82 --> 30.14]  and it's able to generically build attacks to any of our models in our hub.
[30.36 --> 31.76]  So because they all have the same interface,
[31.86 --> 37.46]  it allows people to do these really longitudinal research projects across everything that's going on in the hub itself.
[37.60 --> 41.14]  And then I should mention that now we have a kind of an inference API.
[41.60 --> 46.14]  On any of the pages, you can just type in some text and it will run against that model.
[46.44 --> 50.66]  And you can even call that from your own code directly without ever running anything on your machine.
[51.00 --> 52.42]  Just run it on one of these servers.
[52.42 --> 56.38]  And we even have a Twitter bot that we just put up last week where you can tweet at it,
[56.46 --> 58.22]  and it will run a model against your tweet.
[60.96 --> 63.84]  Bandwidth for Changelog is provided by Fastly.
[64.22 --> 66.12]  Learn more at Fastly.com.
[66.36 --> 69.44]  We move fast and fix things here at Changelog because of Rollbar.
[69.56 --> 71.24]  Check them out at Rollbar.com.
[71.50 --> 73.66]  And we're hosted on Linode cloud servers.
[74.02 --> 76.02]  Head to linode.com slash Changelog.
[76.02 --> 81.42]  This episode is brought to you by DigitalOcean.
[81.88 --> 82.32]  Droplets.
[82.66 --> 83.44]  Managed Kubernetes.
[83.80 --> 84.64]  Managed databases.
[85.18 --> 85.76]  Spaces.
[86.02 --> 86.90]  Object storage.
[87.18 --> 88.42]  Volume block storage.
[88.68 --> 92.16]  Advanced networking like virtual private clouds and cloud firewalls.
[92.36 --> 95.60]  Developer tooling like the robust API and CLI
[95.60 --> 98.62]  to make sure you can interact with your infrastructure the way you want to.
[98.98 --> 102.52]  DigitalOcean is designed for developers and built for businesses.
[102.52 --> 109.64]  Join over 150,000 businesses that develop, manage, and scale their applications with DigitalOcean.
[109.94 --> 113.38]  Head to do.co slash Changelog to get started with a $100 credit.
[113.80 --> 115.86]  Again, do.co slash Changelog.
[115.86 --> 131.16]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[131.46 --> 133.22]  productive, and accessible to everyone.
[133.50 --> 137.62]  This is where conversations around AI, machine learning, and data science happen.
[137.98 --> 142.10]  Join the community and Slack with us around various topics of the show at Changelog.com
[142.10 --> 144.00]  slash community and follow us on Twitter.
[144.14 --> 145.78]  We're at Practical AI FM.
[145.86 --> 155.44]  Well, welcome to another episode of Practical AI.
[155.86 --> 157.50]  This is Daniel Whitenack.
[157.66 --> 164.28]  I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson,
[164.60 --> 168.34]  who is a principal AI strategist at Lockheed Martin.
[168.88 --> 169.62]  How are you doing, Chris?
[169.88 --> 170.74]  I'm hanging in there.
[170.92 --> 171.80]  How are you doing, Daniel?
[172.18 --> 173.34]  Doing pretty good.
[173.34 --> 179.08]  As we talked about the last couple of weeks, I've been ordering parts for an AI workstation
[179.08 --> 182.60]  computer, and it's sitting next to me and it's running.
[183.30 --> 184.34]  Oh, nice.
[184.76 --> 190.32]  I am successfully, or at least it appears that I'm successfully overfitting a model on the
[190.32 --> 190.66]  GPU.
[191.38 --> 194.72]  So I'll have to deal with that, you know, after recording.
[194.72 --> 197.70]  But it's running and it's not overheating yet.
[197.86 --> 201.16]  It's kind of stable at a, I think, reasonable temperature.
[201.52 --> 203.18]  So I'm happy on that front.
[203.72 --> 208.34]  So it's funny because, you know, as we're on this call, we're on Zoom and in the video,
[208.34 --> 210.30]  you have the data center in the background.
[210.50 --> 211.82]  So I just find it funny.
[211.94 --> 212.06]  Yeah.
[212.06 --> 214.90]  A bunch of DGX and video machines or whatever.
[215.08 --> 215.24]  Yeah.
[215.30 --> 216.56]  But that's not what you're using.
[216.68 --> 216.78]  No.
[216.78 --> 222.30]  Mine is much smaller, although it's bigger than I thought because after I put the GPU
[222.30 --> 224.22]  in, the case would not close.
[224.56 --> 227.26]  So I guess that just is like airflow.
[227.70 --> 228.02]  Perfect.
[228.24 --> 228.72]  There you go.
[229.04 --> 229.94]  It solved itself.
[230.36 --> 230.60]  Yeah.
[230.94 --> 233.14]  I'm just doing okay.
[233.34 --> 235.02]  I did something really stupid this morning.
[235.18 --> 236.96]  I was reminded that I'm a klutz.
[236.96 --> 241.72]  I fell when I was running and it looks like I broke a rib and you'd think that I'd do
[241.72 --> 242.68]  something about that.
[242.78 --> 243.94]  But I'm lucky.
[244.06 --> 246.38]  I have a fourth year med student for a stepdaughter.
[246.56 --> 250.20]  So I called her up and we agreed because COVID is running rampant.
[250.20 --> 252.50]  We were not going to have me go to the emergency room.
[252.70 --> 255.46]  So she said the treatment would be the same either way.
[255.56 --> 258.30]  So I'm just kind of cranking through the day, doing my thing.
[258.44 --> 259.64]  And we're now we're recording.
[259.78 --> 260.66]  We're having fun, man.
[260.80 --> 264.04]  You're really pushing through the pain for AI podcast.
[264.22 --> 264.70]  There you go.
[264.78 --> 265.52]  You got to be practical.
[265.74 --> 265.92]  Yeah.
[265.96 --> 266.54]  That's something.
[266.96 --> 267.52]  Okay.
[267.82 --> 268.12]  Yeah.
[268.28 --> 273.46]  Feel free to scream yourself and scream a couple of times or whatever you need to do.
[273.54 --> 273.84]  Okay.
[273.96 --> 274.40]  We'll do.
[275.06 --> 279.92]  Well, going from that note to something completely different, as the show might say,
[280.18 --> 286.40]  we're really excited today because we have a follow up on a show that we did quite a while
[286.40 --> 286.60]  ago.
[286.66 --> 288.20]  Actually, this was episode 35.
[288.60 --> 294.10]  So quite a while ago, we had Clem DeLong on from Hugging Face to talk about what they were
[294.10 --> 294.44]  doing.
[294.44 --> 300.50]  And now we're very excited to have Sasha Rush joining us, who is an associate professor
[300.50 --> 306.46]  at Cornell Tech and is also working at Hugging Face on a bunch of different things and involved
[306.46 --> 307.98]  in the Transformers library.
[307.98 --> 312.04]  And so we're really excited to have you, Sasha, to hear more about Hugging Face.
[312.58 --> 313.10]  Oh, thanks.
[313.16 --> 313.76]  Thanks for having me on.
[314.16 --> 314.46]  Yeah.
[314.80 --> 319.92]  Before we jump into all of that, could you just give us a little bit of a sense of your
[319.92 --> 325.90]  background and how you came into the field of AI and eventually into NLP and what you're
[325.90 --> 326.22]  doing now?
[326.98 --> 327.36]  Sure.
[327.54 --> 327.72]  Yeah.
[327.72 --> 330.40]  So I've been at Cornell Tech for the last year.
[330.40 --> 333.82]  And if you don't know about Cornell Tech, it's a new university.
[334.28 --> 335.72]  It's about seven years old.
[336.44 --> 339.58]  But we've had buildings for the last two years.
[339.90 --> 345.28]  Our buildings are right in the center of New York City on an island in the middle of the
[345.28 --> 345.72]  East River.
[345.72 --> 352.08]  So every day we kind of take a little gondola over to the island and teach courses there.
[352.24 --> 353.02]  Ah, how romantic.
[353.36 --> 353.54]  Yeah.
[353.78 --> 354.86]  It's a pretty fun place.
[355.42 --> 357.78]  And yes, I've been a professor here for the last year.
[358.10 --> 362.88]  Before that, I was a professor at Harvard for about four and a half years.
[363.68 --> 368.56]  And before that, I was a postdoc at Facebook AI Research, also in New York.
[369.20 --> 370.98]  So that's my background.
[370.98 --> 377.88]  These days, I have a lab here at Cornell Tech, and I work with the team at Hugging Face, who
[377.88 --> 378.42]  are in Brooklyn.
[379.22 --> 380.12]  So it's nice.
[380.30 --> 382.98]  Everything's kind of centered in New York City.
[383.18 --> 387.40]  Lots of interesting AI and machine learning going around here these days.
[388.12 --> 393.46]  So my background, after graduating college, I worked as a software engineer for about three
[393.46 --> 393.84]  years.
[394.28 --> 397.80]  I'm kind of a person who very much enjoys coding.
[397.80 --> 402.26]  And I kind of have that as kind of the first part of my personality.
[402.50 --> 405.98]  I then went to graduate school to study natural language processing.
[406.32 --> 410.16]  When I got into natural language processing, I think I really got into it because I was
[410.16 --> 414.88]  very interested in language, and particularly kind of the algorithms and data structures
[414.88 --> 418.04]  involved in studying and understanding how language works.
[418.26 --> 420.82]  At that time, I did a lot of machine learning.
[421.32 --> 425.10]  But machine learning wasn't kind of the primary way we studied language.
[425.10 --> 430.22]  There were all sorts of other aspects about kind of how computers and language interacted.
[430.82 --> 436.86]  And actually, my dissertation was much more about, say, the optimization aspects of language
[436.86 --> 443.20]  in a discrete sense, kind of how you construct trees that represent different linguistic phenomena
[443.20 --> 448.48]  and how these interact with kind of classical computer science algorithms.
[448.48 --> 455.20]  And when I graduated my PhD, I kind of graduated right into the beginning of really kind of intense
[455.20 --> 457.74]  deep learning for language.
[458.36 --> 465.74]  And doing my postdoc at Facebook, everyone was kind of intensely interested in how we could
[465.74 --> 472.30]  do translation, how we could do question answering kind of completely from data using deep learning
[472.30 --> 473.06]  based systems.
[473.06 --> 476.76]  So I kind of dived right into that world.
[476.96 --> 481.00]  I sat next to the folks who were working on Torch at the time.
[481.54 --> 483.00]  And then it was written in Lua.
[483.36 --> 487.56]  And a couple of years later, they converted it to Python and it became PyTorch.
[487.80 --> 493.06]  So I've always been very fascinated by kind of the tools and structures that make it possible
[493.06 --> 496.28]  to do these sort of systems in a kind of open source way.
[496.76 --> 498.70]  Some other things I've worked on in the past.
[498.70 --> 505.64]  I worked on a library called OpenNMT, which was an open source translation library written
[505.64 --> 507.02]  in PyTorch and TensorFlow.
[507.80 --> 514.24]  And we worked with a lot of translation companies, particularly in Europe, to try to build open
[514.24 --> 518.70]  source tools to let them build their own kind of custom Google Translate services.
[518.70 --> 521.52]  And that was a really fun project.
[521.52 --> 526.42]  And it kind of tied together the research we were doing in my lab, which was on kind of
[526.42 --> 531.76]  questions of how to improve translation, how to speed it up, how to make it work on devices
[531.76 --> 535.56]  with questions of how in an open source world these were used.
[535.56 --> 542.28]  So I'm kind of curious, since you kind of alluded a little bit to one thing that's kind of happened
[542.28 --> 550.74]  in recent years in terms of how I guess people maybe used to think about NLP and still do for many tasks
[550.74 --> 555.08]  as far as like computational linguists have been thinking about these things for a very long time.
[555.08 --> 563.88]  But now there's been all of this focus on kind of extending these tasks to maybe generalized machine
[563.88 --> 565.26]  learning type problems.
[565.26 --> 570.06]  Could you give your perspective on kind of how that shift has happened and like what that's meant,
[570.20 --> 576.56]  both in terms of momentum in the field and people getting involved in the field and all of that?
[576.76 --> 577.82]  What are your thoughts on that?
[578.48 --> 579.44]  Yeah, let's see.
[579.88 --> 581.80]  So I think there's a couple different perspectives.
[581.80 --> 588.06]  I don't want to make it seem like kind of data-driven or machine learning systems were kind of new to NLP.
[588.50 --> 597.46]  There's a long history of use of learning, both in NLP, but also kind of learning systems developed in NLP being used in other areas.
[597.84 --> 603.64]  So I think it's a field that's always kind of interacted with these methods in a kind of open dialogue.
[604.24 --> 608.86]  I think the phenomenon we're seeing now is kind of more extreme.
[609.30 --> 611.06]  And it's extreme for a couple reasons.
[611.06 --> 614.60]  I mean, one is the sheer growth of all these fields.
[614.84 --> 622.04]  We're seeing kind of exponential growth in conference sizes and paper submissions and kind of usage of this technology,
[622.04 --> 627.82]  which I honestly think is a great problem to have, but it obviously brings with it a lot of challenges.
[628.20 --> 635.26]  So they're kind of organizational questions of kind of running communities or kind of trying to kind of make progress in this world.
[635.26 --> 640.90]  I think the other question is, what does it mean in terms of methods?
[641.40 --> 645.56]  And we're seeing lots of interesting things along those lines.
[645.98 --> 653.30]  I think that people in the field are adapting to the challenges that kind of come kind of from the world around.
[653.30 --> 658.12]  Like as researchers, we're interested in solving the problems that exist now.
[658.12 --> 664.44]  And a lot of the problems in NLP are suddenly kind of data set problems.
[664.58 --> 668.64]  How do we construct interesting, novel, and difficult data sets?
[669.12 --> 677.04]  How do we analyze models to understand what they're doing and how they're structured and what they're learning?
[677.04 --> 684.56]  What kind of societal questions of how do we understand what biases they might have or what issues they might bring?
[684.90 --> 690.08]  Or even how they might learn, like from what signals are they picking up on?
[690.80 --> 693.48]  And so there's no shortage of interesting research going on.
[693.90 --> 702.50]  It's just that what's interesting is maybe less so the kind of how do you make the benchmark problem go up X number of points.
[702.50 --> 710.60]  So I'm kind of curious. I've been thinking about listening to this and, you know, we had Clem back on the show back.
[710.78 --> 712.84]  I think it was episode 35.
[713.20 --> 713.32]  35.
[713.66 --> 714.76]  Yeah, going way back.
[714.92 --> 719.80]  It was before the Transformers library came out, which we'll definitely talk about later.
[720.28 --> 724.82]  Yeah, totally. I think that was what I was thinking about was the fact that when we were talking to Clem,
[724.82 --> 730.90]  we were really kind of focused on like social AI and chatbots and similar tools and approaches.
[730.90 --> 740.62]  And then in that time between talking to you today and talking to Clem, you know, Transformers came out and you guys really created the definitive Transformer library.
[740.96 --> 745.30]  And, you know, we've been talking about Hugging Face in the context of Transformers since then.
[745.38 --> 748.48]  And I guess how did Hugging Face make that transition?
[748.90 --> 750.02]  What caused that?
[750.14 --> 753.74]  And it's an interesting turn for the, you know, for the history of the company.
[754.44 --> 754.58]  Yeah.
[754.78 --> 757.56]  So, I mean, I guess I should give some perspective.
[757.56 --> 760.66]  So, I've actually only worked at Hugging Face for about eight months now.
[761.08 --> 766.02]  And honestly, I ended up working there because I was such a fan.
[766.42 --> 781.56]  I observed them in the same way that you did, which was as an external observer, seeing them make this transition so impressively from kind of working on chatbots to being this kind of open source powerhouse.
[781.56 --> 793.64]  And I guess as someone who, I guess, I mean, who knows what it means in open source, but as a competitor, as someone building his own libraries in this space, they were just doing it so much better than I was.
[793.64 --> 798.14]  And so, I think that that always impressed me.
[798.26 --> 806.90]  Now, I should say, even before Transformers came out as an official library, I have memories of, well, I guess now we're getting into some of the technical terminology.
[807.28 --> 813.44]  When BERT came out as a paper, there was a kind of rush to port BERT to a PyTorch version.
[813.44 --> 817.94]  And I was working a little bit on this at my own pace.
[818.28 --> 825.04]  And Hugging Face very, very quickly put out their own version of this, maybe part of their chatbot library, maybe it was a separate thing.
[825.14 --> 829.40]  And I think it was really useful just to have that immediately right after the research came.
[829.52 --> 832.08]  And so, I was really appreciative of that even at the time.
[832.72 --> 838.42]  What's the state of Hugging Face now in terms of, I know that they raised a round of funding.
[838.42 --> 846.36]  It seems like from what I'm picking up on Twitter that the team is growing a little bit, but from chatting with you before, it seems like it's still also very distributed.
[846.98 --> 852.78]  There might be some kind of creative relationships, like, of course, you're in academia, but you're also with Hugging Face.
[853.04 --> 860.04]  So, what's the state of the Hugging Face team now, and how's it growing to support this really rich ecosystem of tools?
[860.48 --> 863.98]  Yeah, so, we have about 15 to 20 people, depending on how you count.
[863.98 --> 868.82]  We're mainly focused or entirely focused on these open source tool development.
[869.28 --> 875.46]  The main library is Transformers, which we've talked about, and kind of is the center of what we're developing.
[875.90 --> 879.80]  But now there's also several other really interesting open source projects going on.
[879.80 --> 896.04]  So, we have a project based on NLP datasets that now has almost 150 different open datasets that you can easily browse and download and use in a very efficient and kind of easy to extend way.
[896.38 --> 905.74]  We also have a library of tokenizers that's written in Rust, a low-level library that lets you do very fast tokenization and training.
[905.74 --> 913.36]  And then all this is kind of joined together by a kind of hub of different models and structures that people have uploaded.
[914.02 --> 925.36]  And if you go to the website, you can kind of see this kind of really rich ecosystem of different models, of different datasets, and of different tokenizers that kind of build this all together.
[925.96 --> 929.14]  Practically, it is an interesting question of what the company is like.
[929.38 --> 934.02]  I mentioned earlier that I've been there longer now, probably in COVID, than not in COVID.
[934.32 --> 935.58]  Yeah, I guess that's true.
[936.34 --> 938.26]  But it's always been a distributed company.
[938.68 --> 941.00]  There's a team in Paris and a team in New York.
[941.14 --> 942.24]  It's about half and half.
[942.54 --> 947.58]  But now we also have interns in California and some interns in China, some people in different places.
[947.58 --> 953.00]  So, we mostly kind of communicate through Slack and through other distributed means.
[965.74 --> 973.70]  ChangeLog News is the best way to keep up with the fast-moving software world.
[974.04 --> 982.04]  We track, log, and contextualize the coolest projects, the best practices, and the biggest stories each and every week.
[982.48 --> 990.18]  Make changelog.com your daily destination or hit the snooze button and subscribe to our weekly newsletter that hits inboxes on Sunday mornings.
[990.18 --> 993.72]  Join more than 15,000 enthusiastic readers.
[994.00 --> 1000.18]  It'll cost you exactly zero dollars and you can subscribe right now at changelaw.com slash weekly.
[1005.64 --> 1011.02]  So I guess, you know, we've alluded to Transformers several times now and kind of talked around it a little bit.
[1011.02 --> 1016.08]  For those who are new to the topic, could you kind of define what is a Transformer?
[1016.08 --> 1023.42]  I mean, it's been a big, big deal in recent months and has really changed NLP, but a lot of people may not be familiar with it or have not kept up to date.
[1023.84 --> 1027.22]  Could you kind of just give us a basic run through from the way you see it?
[1027.92 --> 1033.78]  Sure. So I think the term Transformer really kind of implicitly applies to different innovations.
[1034.48 --> 1039.98]  And both of these were actually connected to each other, but both pretty transformative in their own right.
[1040.68 --> 1044.80]  I'll start with the first. So the first is the Transformer as an architecture.
[1044.80 --> 1053.06]  So this is the particular kind of development of a very specific type of architecture that came out.
[1053.56 --> 1060.96]  And the kind of dominant architecture in natural language processing for about five years had been recurrent neural networks,
[1061.24 --> 1066.12]  particularly the LSTM network, and was used basically for everything that we did in the field.
[1066.12 --> 1074.94]  And the Transformer proposed a different and in fact kind of simpler architecture that instead of kind of reliant on these recurrent connections,
[1075.12 --> 1085.00]  kind of connections over time, instead used a kind of random addressing style of architecture based on a mechanism called attention.
[1085.00 --> 1091.88]  And the way it works is that you basically have everything you've seen in the past ready to access at every point in time.
[1092.26 --> 1101.16]  And the main kind of neural network step that you take is the kind of soft random addressing over all your previous history.
[1101.16 --> 1106.06]  And you use that in order to compute the next stage in your sequence.
[1106.66 --> 1110.16]  So instead of kind of keeping a fixed length vector that gets transformed over time,
[1110.26 --> 1114.52]  you keep around everything and you basically search through it at every stage in the process.
[1114.52 --> 1122.82]  And this architecture wasn't kind of new on its own right, but kind of demonstrating that it was more effective than recurrent neural networks
[1122.82 --> 1134.46]  and that it particularly could scale to both kind of fast training and also very, very large models better than recurrent neural networks was kind of a big breakthrough in the field.
[1135.22 --> 1139.54]  And the first results showed kind of large improvements on translation accuracy.
[1140.08 --> 1140.74]  Just a quick question.
[1140.74 --> 1148.72]  You mentioned attention and you sort of defined it in the larger thing, but just because it's a kind of a key aspect of that,
[1148.80 --> 1153.26]  could you talk about what part of that was attention just to differentiate it from the larger process?
[1153.74 --> 1154.26]  Sure. Yeah.
[1154.30 --> 1158.90]  And I should say the original transformer paper has the title attention is all you need.
[1159.26 --> 1161.80]  It's kind of the key aspect of what makes a transformer.
[1162.40 --> 1168.50]  Attention itself is actually quite simple and it's actually kind of very kind of intuitively appealing idea.
[1168.50 --> 1172.48]  So imagine you have a set of objects, say five different objects,
[1172.48 --> 1177.22]  and you want to have a neural network decide which one of those objects you want to use.
[1177.80 --> 1183.60]  You might have a softmax layer where the softmax gives you a distribution,
[1183.72 --> 1186.80]  a probability distribution over which aspect you want to pick.
[1186.90 --> 1189.14]  So which of the five things you should choose?
[1189.56 --> 1191.16]  You could just end there.
[1191.50 --> 1194.44]  And if you ended there, we would just call it multi-class classification.
[1194.44 --> 1201.60]  What attention does is it uses that distribution, the probability of each of the five things,
[1201.78 --> 1204.78]  and feeds that probability back into the model itself.
[1205.36 --> 1210.52]  So it would give a weight to each of the five items and then feed them back in with that weight.
[1210.90 --> 1217.66]  So imagine I have a sentence like, the man walked the dog, and I want to predict the next word in that sentence.
[1217.66 --> 1222.24]  Those previous five words would be the five items I'd want to choose from.
[1222.92 --> 1230.68]  And attention would say, how much weight should I give to each of those previous five words when trying to decide on the next word?
[1231.32 --> 1239.74]  So maybe I'll give it 80% to man, 5% to the, et cetera, and use those in the next step of the process.
[1239.74 --> 1249.34]  All the transformer is, is a kind of repeated version of that game for, say, six to 24 different rounds,
[1249.34 --> 1254.84]  where each time you look back at what you've previously decided, use it to feed it back into your network,
[1254.84 --> 1257.70]  and then use that to try to predict the next step along the line.
[1258.10 --> 1264.56]  So you mentioned that this architecture also, in addition to kind of having this new structure,
[1264.82 --> 1268.56]  also allowed some performance benefits and scaling as well.
[1268.56 --> 1273.54]  I was wondering if you could just give a sense of, because I know this is something people see out there.
[1274.04 --> 1282.24]  And in particular, I think there was a thread on Twitter about how many parameters are in the Hugging Face model hub and all of that.
[1282.62 --> 1288.94]  So I was wondering if you could just give us a sense of, you know, what are the sort of scale of models that are out there?
[1289.06 --> 1296.20]  People hear about like BIRD and GPT-2, and now, of course, we're getting flooded with GPT-3 things.
[1296.20 --> 1304.04]  What are the sort of scale of these models, both in terms of like parameters and also like the data needed to actually train them?
[1304.38 --> 1305.06]  It's a good question.
[1305.36 --> 1306.78]  I never know these numbers offhand.
[1307.76 --> 1313.90]  Models range from 50 million parameters to tens of billions of parameters at the top end.
[1313.90 --> 1320.90]  In practice, some of the larger models, it's unclear how you would even use them, say a standard GPU hardware.
[1321.38 --> 1327.24]  But scale has been a big kind of main aspect of kind of Transformers usage.
[1327.74 --> 1332.62]  But actually, maybe let me pick that question to talk a little bit about the second main innovation of the Transformer.
[1332.96 --> 1338.00]  I talked about the architecture, but I think it's important to also get a sense of the second innovation,
[1338.00 --> 1339.62]  because I think it actually matters even more.
[1340.20 --> 1345.86]  This is a kind of innovation that started around the use of a model called ELMO.
[1346.32 --> 1348.94]  There were a couple other variants, one called COVE.
[1349.10 --> 1352.06]  And then this all kind of peaked with the release of a model called BIRT.
[1352.46 --> 1359.28]  And the kind of idea behind these models is to take a neural network, in the case of BIRT, a transformer,
[1359.94 --> 1364.96]  and to train it on a very simple task at a very, very massive data scale.
[1364.96 --> 1369.50]  So in the case of BIRT, the task is similar to the one I described previously.
[1369.88 --> 1375.98]  You're given a bunch of words, and you randomly remove some of the words and try to predict them back.
[1376.42 --> 1380.60]  It's a game that you can play yourself and try to get a sense of how easy or hard it is to do.
[1381.02 --> 1382.12]  Sometimes it's really easy.
[1382.24 --> 1383.26]  Sometimes it's really challenging.
[1383.92 --> 1386.18]  But the point isn't the task itself.
[1386.30 --> 1392.38]  The point is to give the model a task that would require it to know something about language in order to complete,
[1392.38 --> 1395.58]  and then train it at as big a scale as you can.
[1395.88 --> 1397.36]  So it's hard to give you a sense of this.
[1397.48 --> 1402.78]  I mean, one thing that's nice about language is you can store a ton of it in very little space.
[1403.42 --> 1407.08]  So if you have all of Wikipedia, just basically fit it on your computer.
[1407.86 --> 1413.96]  And companies like Google basically have a non-trivial amount of all the text that's ever been produced.
[1413.96 --> 1421.00]  And so you can kind of take all that text, throw it into one of these models, and then train it on this simple task.
[1421.34 --> 1427.24]  And it turns out that in the process of trying to complete this task, the model learns a lot about how language works.
[1427.52 --> 1430.82]  We say it learns very good features for language.
[1431.60 --> 1434.96]  So once you've done that, once you've kind of trained it on all the language that you have,
[1435.68 --> 1441.18]  you can then apply it to a much smaller task that you maybe have a small amount of supervised data for.
[1441.18 --> 1448.88]  So this idea, which people call pre-training, is kind of central to how a lot of NLP works these days,
[1448.92 --> 1451.60]  and also to how the Transformers library is designed.
[1452.62 --> 1457.36]  So yeah, I think that's such a great and important point,
[1457.44 --> 1461.28]  is that people kind of get hung up on the size of these models.
[1461.28 --> 1463.64]  And it's kind of cool to talk about those things,
[1463.64 --> 1467.50]  and in some cases annoying to work with them because they're so large,
[1467.50 --> 1471.08]  and in some cases hard to perform inference with.
[1471.52 --> 1477.42]  But yeah, I guess what you're saying is, you know, that the task that they're trained on
[1477.42 --> 1480.82]  is just intended to help them learn good features.
[1480.82 --> 1488.32]  And then the task that you actually want to use them for involves some like fine tuning or transfer learning.
[1488.48 --> 1489.00]  Is that right?
[1489.40 --> 1493.76]  Yeah, I think, I mean, I don't want to claim that this is finished as an idea.
[1493.76 --> 1494.20]  Right.
[1494.56 --> 1499.06]  I think a lot of the tasks we work on now will have a kind of fine tuning stage,
[1499.06 --> 1502.56]  where you take the model and learn it for a given task.
[1502.90 --> 1505.98]  OpenAI has a slightly different model of what they're trying to achieve,
[1506.20 --> 1508.56]  which is they're not super interested in fine tuning,
[1508.68 --> 1511.26]  they want to kind of just use the model directly,
[1511.68 --> 1514.88]  kind of feed it some more sentences and try to directly predict tasks.
[1514.98 --> 1518.28]  Yeah, so there is this like, because I've seen,
[1518.94 --> 1522.30]  and maybe you could kind of help us through some of this jargon.
[1522.30 --> 1524.58]  And it seems like people talk about some of these models,
[1524.68 --> 1530.36]  they just like they have so much knowledge that you can perform a task that they just write off the bat.
[1530.44 --> 1534.86]  Like, I don't know if it's question answering or information retrieval or whatever it is,
[1534.86 --> 1536.78]  without really much fine tuning.
[1536.92 --> 1538.82]  Is that what you're kind of getting at in that other model?
[1539.22 --> 1541.78]  Well, I do want to distinguish kind of two aspects.
[1541.78 --> 1549.20]  I think that all the kind of state of art models on kind of standard benchmark tasks all use some sort of fine tuning.
[1549.38 --> 1553.34]  That's like become a very standard procedure.
[1553.54 --> 1555.10]  And we kind of understand how that works.
[1555.72 --> 1559.12]  But to do fine tuning, you still need some amount of supervised data.
[1559.70 --> 1561.92]  I guess we would say it's a small to medium amount,
[1562.12 --> 1565.56]  but you need something in domain for the task you're interested in.
[1565.56 --> 1569.84]  And I think there's a lot of recent excitement for kind of a crazier idea,
[1570.04 --> 1577.20]  which is this kind of zero shot or one shot idea of just the model should know how to do your task immediately right off the bat.
[1577.54 --> 1578.90]  Yeah. I think that's where I was going.
[1578.98 --> 1581.28]  Because they throw around this idea of zero shot.
[1581.44 --> 1586.26]  And to some degree, it seems sort of like magical in many ways to people, I think.
[1586.40 --> 1586.64]  Yeah.
[1586.64 --> 1588.80]  I don't want to say anything on record.
[1588.94 --> 1590.14]  It's on the research frontier.
[1590.78 --> 1590.90]  Yeah.
[1591.02 --> 1593.74]  It might turn out that that's the way to do lots of language tasks.
[1593.74 --> 1596.10]  But I think it's still an open question, I would say.
[1596.54 --> 1600.16]  So turning to the Transformer library itself, I'm kind of curious.
[1600.48 --> 1604.52]  So in recognizing that you've only been there at the company for a limited amount of time.
[1604.86 --> 1605.04]  Yeah.
[1605.04 --> 1611.00]  Do you have any insight into kind of the motivation that moved the company into this Transformer library itself?
[1611.12 --> 1613.14]  Was it supporting the other operations?
[1613.52 --> 1616.18]  Or was it just something that was an opportunity that came up?
[1616.18 --> 1618.76]  What kind of took the company there as far as you're familiar?
[1619.26 --> 1619.96]  That's a good question.
[1621.56 --> 1626.28]  The graph of the usage of this library on GitHub kind of blows me away.
[1626.72 --> 1630.22]  Like it went from no users to about 30,000.
[1630.58 --> 1636.78]  So I think they just hit on something that was like, I guess when you have a hit, maybe that changes the mode of thinking.
[1636.78 --> 1637.26]  Yeah.
[1637.40 --> 1647.48]  So maybe you could describe like along with that, what is the sort of main usage pattern that people are kind of grabbing onto Transformers for?
[1647.62 --> 1653.84]  I know that there are multiple, of course, like quite a few different things that you could use the library for.
[1653.84 --> 1660.28]  But what do you see as the sort of like the main thrust of what people are grabbing Transformers for?
[1661.30 --> 1662.46]  What is that?
[1662.58 --> 1665.24]  And, you know, how is that being supported, I guess?
[1665.62 --> 1665.72]  Yeah.
[1665.84 --> 1666.16]  Yeah.
[1666.30 --> 1667.32]  This is a great question.
[1667.32 --> 1672.68]  And I think in some ways you guys maybe have insight into this that I would be also interested to hear about.
[1673.00 --> 1674.16]  Let me start at the high level.
[1674.38 --> 1681.88]  One thing that fascinates me about kind of current usage of deep learning is that you have people who approach it from many different angles.
[1682.76 --> 1686.38]  And in one of our papers, we kind of broke this down into three different classes.
[1686.38 --> 1691.18]  So we talk about there being architects, there being trainers, and then there being end users.
[1692.14 --> 1698.44]  And I think within the ecosystem, Transformers kind of has different meanings to all three of those people.
[1699.08 --> 1713.68]  So if you're a company like OpenAI or like Allen AI, kind of companies at the kind of cutting edge of research training, you use Transformers or kind of related libraries to try to build the next architecture or the next pre-trained model.
[1713.68 --> 1728.92]  And that often means running these very large training jobs on multi-GPUs over many days and then using Transformers as a way to distribute your model through our hub and make it easy for people to use it or to adapt it for their tasks.
[1729.78 --> 1743.36]  If you're like an expert, but maybe not kind of at the kind of front end of the like frontier of research, another common use case is this kind of fine tuning use case where you have data for your company.
[1743.68 --> 1746.06]  Or for a given problem that you want to solve.
[1746.38 --> 1752.82]  And you bring that data into the library, use it in training mode to fine tune on your data set.
[1753.36 --> 1756.38]  It may take a couple hours and require some GPUs.
[1756.56 --> 1761.04]  But out of that, you get a really accurate model for the task you're interested in.
[1761.04 --> 1769.24]  But then at the other end, you have just end users who want to use the library as a way of kind of performing kind of standard NLP tasks.
[1769.56 --> 1776.46]  You might want to use it as a way to do summarization or translation or named entity recognition or question answering.
[1776.82 --> 1787.50]  And you can often just use it completely in inference mode, maybe not even using Python, just kind of taking up pre-trained model, using it directly for your tasks in that kind of setting.
[1787.50 --> 1795.42]  So I think all of these people are within the machine learning ecosystem, but they kind of have different end goals or different use cases.
[1795.70 --> 1800.38]  And I think we're kind of trying to aim to support any of those kind of outcomes.
[1801.40 --> 1810.58]  So I know you have a model hub and was wondering if you could kind of talk about, you know, what users can find there and start incorporating into their own projects.
[1810.80 --> 1812.62]  What does the growth of that hub look like?
[1812.86 --> 1815.22]  You know, just what kind of ecosystem has developed around it?
[1815.22 --> 1820.12]  Yeah. So the model hub is kind of part of the open source library.
[1820.36 --> 1828.78]  If you want to use a model in the library, you say model.load and you pull off, you just pulls it directly down from the model hub.
[1829.32 --> 1831.84]  And you can do that with any of the models that are there.
[1832.00 --> 1837.28]  We have kind of a set of models that kind of have brand names that are very often used.
[1837.28 --> 1845.46]  So those include models like GPT-2 or a variance of BERT or Roberta or new models like this model called BART or a model called T5.
[1845.70 --> 1849.20]  But then it also includes a long tail of other models from the community.
[1849.80 --> 1856.84]  So this includes models that are pre-trained to target, say, biomedical text or extraction from scientific documents.
[1856.84 --> 1864.06]  Or models that are trained in many different languages, kind of by the communities interested in those languages themselves.
[1864.66 --> 1867.44]  Or models that are experimental or try to do other things.
[1867.44 --> 1871.92]  Or one popular aspect is models that are very small, models that you could run on your phone.
[1871.92 --> 1879.42]  So the idea of the model hub is to kind of have all of those have the same API and have the same easy way to use them.
[1880.18 --> 1887.82]  And one thing that we think is really interesting is that unlike kind of generic model hubs like TensorFlow's hub or PyTorch's hub,
[1888.38 --> 1894.78]  because our models are all of the same form, we can build a lot of kind of tools and machinery around using them.
[1895.18 --> 1898.98]  So for instance, we have a visualizer that works for all of our models.
[1898.98 --> 1903.98]  You can just upload your own model and get really interesting visualization of its internal structure.
[1904.94 --> 1911.48]  Or this open source project called, I think it's called TextAttack, built an adversarial attack system.
[1911.76 --> 1916.56]  And it's able to kind of generically build attacks to any of our models in our hub.
[1917.04 --> 1924.84]  So because they all have the same interface, it allows people to do these really kind of longitudinal research projects across everything that's going on in the hub itself.
[1924.84 --> 1930.66]  And then I should mention that now we have a kind of an inference API on any of the pages.
[1930.66 --> 1934.38]  You can just type in some text and it will run against that model.
[1934.82 --> 1939.40]  And you can even call that from your own code directly without ever running anything on your machine.
[1939.58 --> 1941.22]  Just run it on one of these servers.
[1941.84 --> 1948.44]  And we even have a Twitter bot that we just put up last week where you can kind of tweet at it and it will run a model against your tweet.
[1949.12 --> 1949.86]  Yeah, that's great.
[1949.86 --> 1960.60]  I was wondering, before we leave the topic of the open source projects, you also mentioned these other libraries, tokenizers and NLP, which includes the datasets and evaluation metrics.
[1960.96 --> 1965.56]  How do those fit into the puzzle and maybe interact and influence one another?
[1966.14 --> 1966.32]  Yeah.
[1966.48 --> 1970.70]  I mean, at the end of the day, our interest is in building open source NLP.
[1970.70 --> 1978.26]  And I think there will continue to be kind of new variants of transformers and new pre-trained models.
[1978.96 --> 1989.58]  But kind of, as I mentioned earlier, an increasing area of innovation in NLP is to try to find the right datasets to kind of challenge these models in interesting ways.
[1990.36 --> 1999.46]  And so there's a lot of energy in dataset construction these days and a proliferation of really interesting datasets of different sizes and scopes.
[1999.46 --> 2024.06]  And so Tom Wolf, who's our main open source engineer, got a great passion about building up open source datasets and build a library that makes it very easy to use these models in Python and really makes it extremely efficient to use kind of complex datasets directly within your code across kind of many different aspects of NLP.
[2024.06 --> 2032.48]  And so you can, we have a website that you can go to where you can kind of browse through any of these datasets and kind of use them in various tasks.
[2033.52 --> 2037.68]  And one nice aspect of this is that we have a lot of examples of how to use transformers.
[2038.02 --> 2041.40]  And they had a lot of kind of custom dataset code just to run the examples.
[2041.78 --> 2043.84]  But now that code has all kind of been factored out.
[2043.96 --> 2049.24]  You can just kind of pull it in from NLP and then run the examples, kind of focusing on the machine learning parts.
[2049.24 --> 2068.62]  We deserve a better internet and the Brave team has the recipe for bringing it to us.
[2068.76 --> 2069.76]  Start with Google Chrome.
[2070.00 --> 2073.70]  Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[2073.90 --> 2074.78]  Rip out the Google bits.
[2074.92 --> 2075.54]  We don't need them.
[2075.90 --> 2078.42]  Mix in ad and tracker blocking by default.
[2078.42 --> 2081.40]  Quick access to the Tor network for true private browsing.
[2081.76 --> 2086.10]  And an opt-in reward system so you can get paid to view privacy-respecting ads.
[2086.32 --> 2090.06]  Then turn around and use those rewards to support your favorite web creators like us.
[2090.36 --> 2094.98]  Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[2094.98 --> 2118.14]  So to take the conversation in a slightly different direction for a moment, I know from talking before the show that you put together ICLR and you kind of managed that process this morning and for, which is a research conference.
[2118.14 --> 2120.54]  And I'm really interested at this point.
[2120.64 --> 2128.02]  You know, we're in the time of COVID-19 and so much has changed across all of work, but particularly conferences.
[2128.02 --> 2131.30]  Many of them are going online, becoming virtual like that.
[2131.46 --> 2138.74]  Really interested in what that was like and what, you know, what your experience doing it this way was and, you know, what worked, what didn't.
[2138.74 --> 2147.94]  That kind of, I'm just curious because I think a lot of people are kind of waiting to see what conferences are turning into and, you know, do they want to continue to go down that route or something.
[2148.46 --> 2148.62]  Yeah.
[2148.88 --> 2154.78]  This year I was the general chair of ICLR, the International Conference of Learning Representations.
[2154.78 --> 2160.04]  It's a big machine learning conference and really the only one focused completely on deep learning.
[2160.56 --> 2161.70]  And it was interesting.
[2161.84 --> 2166.96]  I had the chance of being the program chair for the conference last year where we had the conference in New Orleans.
[2167.28 --> 2173.80]  And then this year I was the general chair and by about December we were getting prepped.
[2174.10 --> 2180.98]  And then by February, March, it became increasingly clear that we weren't going to be able to have this conference live.
[2180.98 --> 2187.12]  And so I think we were the first AI conference to really have to be completely virtual.
[2187.48 --> 2192.48]  We had about a month and a half before the conference to really come up with something new.
[2193.34 --> 2198.18]  And we had this wonderful team led by the program chair this year, Shakir Mohamed.
[2198.78 --> 2202.14]  And we wanted to do something that kind of fit the spirit of a conference.
[2202.14 --> 2206.28]  And so we sat down and wrote a website for the conference from scratch.
[2206.28 --> 2214.80]  And we built a website that was based around this idea that everyone in the conference would be in kind of a Slack-like chat room.
[2215.62 --> 2218.12]  And we used an open source platform for that.
[2218.38 --> 2226.04]  And that every paper would have its own page with a video of the work and a chat room for that paper.
[2226.56 --> 2231.20]  So people would be able to kind of talk about it or discuss it within that setting itself.
[2231.20 --> 2242.56]  And in addition, we built out kind of a bunch of social gatherings that people could have and a kind of calendar for the whole event.
[2243.22 --> 2248.76]  And the kind of main challenge is how do you run a conference asynchronous in this way?
[2249.36 --> 2253.96]  We didn't really think it was possible to have everyone in the same place at the same time.
[2253.96 --> 2262.10]  And so we wanted it to kind of use things like chat rooms that kind of feel more asynchronous, particularly with kind of international audience.
[2262.62 --> 2265.26]  And the conference itself actually was really fun.
[2265.40 --> 2269.00]  We had actually a pretty large increase in attendance over past years.
[2269.30 --> 2277.70]  We had people from all over the world, particularly from some places that would have been difficult to attend a conference in other years.
[2277.70 --> 2279.78]  And a ton of engagement.
[2280.28 --> 2288.46]  A lot of the posters were viewed a tremendous amount of times and maybe about 100,000 messages over the chat system over a couple of days.
[2289.00 --> 2290.06]  I think there were challenges.
[2290.60 --> 2297.82]  I think it's hard to get the same kind of spirit of having coffee or kind of just chatting informally in this sort of event.
[2298.68 --> 2302.86]  Things like Twitter are helpful but don't have the same kind of intimacy.
[2303.62 --> 2305.48]  But there were also kind of nice things.
[2305.48 --> 2317.40]  We ran these kind of mentorship sessions where one person was able to chat with 10 to 20 folks who were interested in mentorship in a kind of one-to-many model that actually I think might have been difficult at a conference.
[2318.06 --> 2320.66]  But it kind of works actually pretty nicely over Zoom.
[2321.16 --> 2323.08]  Anyway, it was an experimental setup.
[2323.74 --> 2327.50]  Since then, we open-sourced all the tools that we built for the conference.
[2327.64 --> 2330.14]  You can get it online if you search for Minicomp.
[2330.32 --> 2335.06]  And the software has been used for about five or six other major conferences since then.
[2335.48 --> 2338.74]  Including ACL this year, which is the big NLP conference.
[2339.06 --> 2342.70]  And ICML, which is another machine learning conference venue.
[2343.56 --> 2345.36]  I don't think we've cracked it.
[2345.60 --> 2348.82]  But in the meantime, it's nice to have something we build as a community.
[2349.74 --> 2353.50]  Yeah, I attended the conference, iClear.
[2353.50 --> 2358.34]  And I was super impressed with everything that was put together, especially given the time frame.
[2358.34 --> 2365.16]  I know you must have had some very late nights fueled by very much coffee.
[2365.74 --> 2372.74]  So congratulations on in such a short time period putting together something that was so good.
[2372.86 --> 2377.68]  I know one of the things that I appreciated, you know, I've been to other research conferences in person.
[2377.68 --> 2381.70]  And, you know, posters or talks or something like that.
[2381.76 --> 2387.38]  There's just so much going on that it is hard to kind of do that.
[2387.52 --> 2390.08]  Like, you can't go to this talk at the same time as this talk.
[2390.16 --> 2394.96]  And it's hard to find that person afterwards and ask them some questions about their work.
[2395.04 --> 2396.42]  Maybe you walk by their poster or something.
[2396.42 --> 2402.24]  So it was kind of nice to just scroll through and look at the different videos, especially given the time zone differences.
[2402.24 --> 2411.32]  And, you know, shoot the authors a message that they could respond to asynchronously so that that question didn't get lost or something like that.
[2411.42 --> 2413.24]  I found that extremely useful.
[2413.80 --> 2421.76]  What are your thoughts on assuming maybe that at some point in the future, research conferences will have an in-person component again?
[2422.30 --> 2425.58]  Do you see a sort of hybrid scenario developing?
[2425.58 --> 2432.78]  Because I know one of the things that, like with NeurIPS and all of that, was a struggle for so many years, were people getting visas as well.
[2432.94 --> 2446.90]  Which is just such a shame as, like, so many people from Africa or from Asia that were doing amazing work but couldn't actually be at the conference because of visa issues or cost issues or whatever it is.
[2446.98 --> 2448.96]  So how do you see that future happening?
[2449.54 --> 2454.24]  Yeah, it's a question we're talking actually a lot about at ICLR right now.
[2454.24 --> 2455.80]  I don't think we have an answer.
[2455.98 --> 2460.26]  And I think a lot of it will depend on kind of what the world looks like in a couple of years.
[2460.74 --> 2472.30]  So one thing we're committed to at ICLR is having the conference at venues in other locations or kind of locations that have kind of not been visited as much in the past.
[2472.30 --> 2480.46]  So one thing that was very disappointing was that this year's conference for ICLR was supposed to be in Ethiopia in Anas Ababa.
[2480.76 --> 2483.92]  And we were all really disappointed that we couldn't make it out there.
[2484.00 --> 2485.64]  It would have been a really interesting event.
[2485.64 --> 2491.56]  So hopefully we will continue to kind of have conferences in kind of a wider range of locations.
[2491.56 --> 2508.38]  But I think, as I was saying earlier, all these areas are experiencing such kind of hyper growth that kind of ways of kind of dealing with scale that doesn't lose a kind of sense of interaction is a kind of major challenge for the community.
[2508.38 --> 2521.34]  And so I think we need to kind of be creative about ways to handle that problem and ways of kind of maybe giving people the same experience that I think, at least I feel like I had when I was a first graduate student that kind of inspired me to continue in the field.
[2521.84 --> 2523.16]  So I don't know what that would look like.
[2523.34 --> 2526.40]  Maybe it looks like something more distributed with a virtual component.
[2526.40 --> 2531.74]  So kind of wondering and also turning the corner a little bit on just NLP in general.
[2532.08 --> 2532.24]  Yeah.
[2532.36 --> 2534.58]  And, you know, you're doing the work that you're doing.
[2534.66 --> 2537.70]  You're right at the center of the NLP world in that way.
[2538.14 --> 2547.02]  And it's certainly, you know, Daniel and I talk all the time on these episodes about the fact that the last couple of years has felt like, you know, NLP has really come of age.
[2547.44 --> 2550.50]  You know, you might say a golden age of NLP is how it feels like we're in.
[2550.72 --> 2554.86]  And kind of before that, you know, we had seen like CNNs have their moment and stuff.
[2554.86 --> 2560.40]  As we've arrived where we are so far in NLP, you know, what does the future look like to you?
[2560.54 --> 2564.92]  What kind of big challenges are open and should be focused on?
[2565.34 --> 2568.28]  You know, what are your thoughts there on from this point forward?
[2569.00 --> 2570.48]  Ooh, that's a hard question.
[2570.70 --> 2571.06]  Big one.
[2571.52 --> 2571.76]  Yeah.
[2572.12 --> 2576.02]  In some ways, as someone who's been working at NLP for a while, it's been really neat.
[2576.20 --> 2581.22]  I mean, I think it's way better than I could have possibly expected.
[2581.38 --> 2584.80]  Seeing things like translation get to the point where it's at now is just all inspiring to me.
[2584.86 --> 2588.24]  Like it's such a useful thing and have it work the way it does is awesome.
[2588.68 --> 2590.64]  So what are the challenges now?
[2590.76 --> 2591.68]  I think there's a bunch.
[2592.00 --> 2597.22]  I think computer vision for all its successes has also had a lot of issues.
[2598.48 --> 2608.32]  And there's a lot of conversation in NLP about kind of how to avoid some of the issues or to kind of have those conversations earlier rather than later.
[2608.32 --> 2619.24]  Things like what we've seen with facial recognition as a technology and kind of questions about efficacy there is, I think, a kind of challenging point.
[2619.40 --> 2627.58]  And we've somehow managed to solve a lot of the natural language processing questions without solving some of the computational linguistics questions.
[2627.58 --> 2632.56]  Like things work, but we have no real sense of why.
[2633.12 --> 2635.70]  And as a scientist, that can be a little bit frustrating.
[2635.92 --> 2639.86]  Like we don't really know what signals these models are using to make predictions.
[2639.86 --> 2646.92]  And it's very hard to know or to even ask that sort of question in a falsifiable way.
[2647.84 --> 2650.64]  Why did this model classify this sentence in this way?
[2650.78 --> 2652.96]  Why did it decide to choose this decision?
[2653.10 --> 2657.44]  I mean, these models are, at least from a probabilistic sense, completely global.
[2657.44 --> 2663.86]  And so it's kind of challenging to kind of do any sort of analysis along those lines.
[2664.36 --> 2668.94]  But then more kind of practically, I think there's a lot of practical questions that are not solved yet.
[2668.94 --> 2672.92]  You mentioned this idea of dealing with massive, massive models.
[2673.12 --> 2683.46]  It's not clear if we're going to need hardware that is 100 times bigger to run these models or whether you can use pruning and distillation to make them super small.
[2683.46 --> 2685.80]  Or what does it mean to run it locally?
[2685.92 --> 2688.62]  Or does it just make us more reliant on kind of cloud systems?
[2689.02 --> 2692.84]  I think these all become interesting kind of systems research questions in the short term.
[2693.60 --> 2693.62]  Awesome.
[2693.86 --> 2707.12]  Well, we appreciate you taking a stab at the future predictions because I know, I think we said on the podcast before, any of the predictions that we make, I feel like are definitely going to be false because it's always something unexpected that happens.
[2707.12 --> 2721.32]  But I appreciate you giving your perspective, being part of the kind of the center of all of this work and appreciate you taking time to talk with us and kind of explain a bit about the Transformers library and things that are going on in NLP.
[2721.68 --> 2730.54]  Thank you so much for your contributions to the community as well in terms of helping, you know, conferences and really pushing forward open source.
[2730.54 --> 2740.14]  So appreciate you taking time to join us and looking forward to digging into all the great things that Hugging Face is releasing and is doing.
[2740.48 --> 2740.90]  Thanks so much.
[2740.98 --> 2741.62]  Thanks for having me on.
[2745.22 --> 2749.84]  If you're listening to this in the month of July, you've got a shot at some free goodies.
[2750.28 --> 2758.10]  We are doing a giveaway in celebration of our friend and open source whiz, Zeno Rocha's new book, 14 Habits of Highly Productive Developers.
[2758.10 --> 2762.54]  If you don't know Zeno by name, you may have heard of his wildly popular Dracula theme.
[2763.04 --> 2766.26]  It's an awesome dark mode theme for text editors, terminals, etc.
[2766.52 --> 2771.42]  And we have three bundles of Dracula Pro and 14 Habits to give away for absolutely free.
[2771.70 --> 2773.30]  That's a $60 value.
[2773.44 --> 2774.84]  And there are three ways to enter.
[2775.32 --> 2778.44]  You can be the reviewer, the socializer and the recommender.
[2778.72 --> 2780.82]  Hit up the link in your show notes to get started.
[2781.26 --> 2784.10]  There will be three lucky winners and you can be one of them.
[2784.10 --> 2789.14]  Thanks to our longtime sponsors Fastly, Linode and Rollbar for their continued support.
[2789.40 --> 2791.86]  To Breakmaster Cylinder for our amazing beats.
[2792.20 --> 2794.32]  And to you for listening to Practical AI.
[2794.62 --> 2796.14]  We appreciate your time and attention.
[2796.50 --> 2797.34]  That's all for this week.
[2797.58 --> 2798.56]  We'll talk to you next time.
