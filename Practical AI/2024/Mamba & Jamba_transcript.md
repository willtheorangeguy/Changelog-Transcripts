[0.00 --> 8.66]  Welcome to Practical AI.
[9.16 --> 16.78]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is
[16.78 --> 19.54]  changing the world, this is the show for you.
[20.24 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 30.94]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions
[30.94 --> 35.44]  on six continents, so you can launch your app near your users.
[35.84 --> 37.86]  Learn more at Fly.io.
[42.56 --> 46.94]  Welcome to another episode of the Practical AI podcast.
[47.42 --> 48.98]  My name is Daniel Whitenack.
[48.98 --> 54.50]  I am CEO and founder at Prediction Guard, and I'm joined as always by my co-host,
[54.50 --> 59.50]  Chris Benson, who is a Principal AI Research Engineer at Lockheed Martin.
[59.76 --> 60.42]  How are you doing, Chris?
[60.72 --> 61.68]  Doing great today, Daniel.
[61.74 --> 62.16]  How's it going?
[62.60 --> 63.38]  It's going great.
[63.52 --> 71.42]  The sun is out and summer is upon us, along with lots of new AI models and excitement going
[71.42 --> 72.36]  on in the space.
[72.68 --> 78.58]  And on that note, specifically as related to large language models, we're really excited
[78.58 --> 87.82]  to have with us today, Joav, who is the co-founder and co-CEO of AI21 and Professor Emeritus at
[87.82 --> 88.26]  Stanford.
[88.82 --> 89.46]  Welcome, Joav.
[89.52 --> 90.00]  How are you doing?
[90.52 --> 91.46]  I'm doing good.
[91.62 --> 93.28]  Really a pleasure to be with you guys.
[93.76 --> 94.52]  Yeah, yeah.
[94.58 --> 96.44]  We're so excited to have you on.
[96.52 --> 100.92]  It's a show we've been wanting to have for some time now.
[100.92 --> 107.96]  I'm wondering if you could kind of give us a little bit of the background of AI21 and
[107.96 --> 117.68]  specifically maybe how you view AI21 as fitting into this wider landscape of LLM companies and
[117.68 --> 118.26]  technology.
[118.86 --> 123.92]  So maybe a good starting point will be to say why we started the company in the first place
[123.92 --> 125.90]  a little over six years ago.
[125.90 --> 132.24]  We started the company because we believe that deep learning, remember at the time LLMs
[132.24 --> 135.56]  were not a thing, but deep learning was mostly applied to vision.
[136.14 --> 139.58]  We believe that modern day AI requires deep learning.
[139.84 --> 141.74]  It's a necessary component, but not sufficient.
[142.20 --> 147.90]  We believe that certain aspects of intelligence, this thing we often call reasoning, will not
[147.90 --> 149.90]  emerge purely from the statistics.
[150.70 --> 154.04]  And it's the sort of thing AI did back in the 80s.
[154.04 --> 159.38]  And we believe that we left money on the table and it's time to bring the two together.
[159.82 --> 161.02]  That's why we started the company.
[161.90 --> 166.82]  Now, fast forward today, what does the landscape look like and where do we fit in?
[167.60 --> 172.26]  So although I said that large language models, so very quickly we fell into LLMs.
[173.12 --> 176.18]  We were the heaviest users of GPT-3 when it came out.
[176.66 --> 178.80]  We decided to roll our own.
[178.80 --> 183.86]  And really language is where the action is because we often say that machine vision is
[183.86 --> 189.62]  a lens into the human eye, but language is a lens into the human mind because there's
[189.62 --> 195.70]  no thought as intricate and nuanced as you want that can't in some way be expressed in
[195.70 --> 196.06]  language.
[196.64 --> 199.38]  Vision is a quote unquote easy problem.
[199.38 --> 204.24]  Of course, it's not easy, but there's something to understand that this is a phone.
[204.98 --> 208.88]  I don't really care what the pixel is way on the side here.
[209.20 --> 212.16]  Always exactly true, but it's really primarily true.
[212.64 --> 213.60]  That's not true with language.
[213.72 --> 215.42]  Language connections matter terribly.
[215.52 --> 218.12]  You change a word here, the whole meaning of the sentence changes.
[218.26 --> 223.00]  In general, you can't escape semantics when you deal with language.
[223.80 --> 224.92]  And so it's harder.
[224.92 --> 226.96]  But if you crack it, that's gold.
[227.58 --> 231.36]  If you look at the enterprise, from the beginning, we were focused on the enterprise.
[231.94 --> 238.30]  80% of the data in the enterprise is text, mostly either not used or way underused.
[238.70 --> 240.62]  And there's a really good opportunity there.
[240.70 --> 242.14]  And that's kind of been our focus.
[242.86 --> 246.96]  So, of course, we're not the only people with large language models.
[246.96 --> 256.00]  We are one of the handful of companies that do really large, very capable language models.
[256.38 --> 258.34]  Our first model was called Jurassic One.
[258.58 --> 259.98]  It was going back a few years.
[260.14 --> 263.46]  It was not a most innovative model, but it was a good workhorse.
[263.64 --> 268.00]  It was a GPT-like, autoregressive left-to-right model.
[268.62 --> 271.40]  And at the time, it was slightly bigger, slightly better than GPT-3.
[271.54 --> 273.96]  Of course, both those models are by now eclipsed.
[273.96 --> 282.26]  We very recently released our most recent model called Jamba, which is very interesting in a number of ways.
[283.12 --> 290.22]  And we can dig deeper, but maybe at 30,000 feet, architecturally, it's different.
[290.40 --> 293.32]  It's not pure transformer model.
[293.46 --> 302.34]  It really is mostly based on structured space state model, SSSM, as they're called.
[302.34 --> 305.52]  And we can speak about the advantages and disadvantages of those.
[305.64 --> 313.44]  But basically, we took that architecture and added elements of transformers, the attention layer, to get the both of both worlds.
[313.58 --> 323.26]  And you get performance that is as good as any model of its size, better than most of its kind of size group, and extremely efficient.
[323.26 --> 326.98]  We have a context length that's larger than any other model of its size.
[327.48 --> 335.20]  The version we released has a 250K context window length, although we trained it up to a million.
[335.82 --> 340.98]  And yet, it all fits onto a single 80 gigabyte GPU.
[341.86 --> 344.64]  And so your show is titled Practical AI.
[344.78 --> 346.02]  This starts to make it practical.
[346.02 --> 346.98]  That's great.
[346.98 --> 352.88]  And speaking of practicalities, you mentioned the focus on enterprise from the beginning.
[353.04 --> 359.98]  You also mentioned that a lot of data in the enterprise is kind of locked up in this unstructured text.
[360.98 --> 369.30]  I remember when I first got into data science, the focus is, oh, we're going to do big data and all of this cool analytics stuff with data warehouses.
[369.30 --> 372.34]  And I think that's sort of waned a little bit.
[372.44 --> 375.62]  I'm wondering if you could talk to that point.
[375.98 --> 383.18]  Like, why are enterprises, what types of value can they get out of this sort of text that's sitting around?
[383.18 --> 392.54]  Because I think maybe a lot of listeners, maybe they've tried these chat interfaces, whether it be ChatGPT or Gemini or whatever.
[392.54 --> 399.80]  But maybe they're less exposed to the workloads that enterprises are doing with LLMs.
[400.14 --> 410.06]  So could you give us a picture of how enterprises are unlocking value with that kind of 80% of text data, maybe just by way of example or at a high level?
[410.48 --> 410.62]  Sure.
[411.08 --> 413.70]  And really, the use cases are quite broad.
[413.86 --> 419.46]  The industries are very broad, whether it's finance or healthcare, education, or, you know, you name it.
[419.46 --> 422.18]  And the use cases are varied.
[422.54 --> 427.20]  But to pick some concrete ones, let's say you have manuals.
[427.40 --> 430.24]  There are companies with thousands of manuals.
[430.42 --> 438.10]  And whether it's the end user wanting to – I recently did – I had a new sort of oven-microwave combination.
[438.46 --> 442.10]  And for the life of me, I couldn't find the relevant information in the manual.
[442.44 --> 444.26]  So I searched online and so on.
[444.44 --> 447.92]  It would be really convenient to go and ask a question and get just the right answer.
[447.92 --> 455.04]  But even if it's not the end user, it could be the tech support person who themselves want to get quick answers.
[455.14 --> 455.90]  So that's an example.
[456.30 --> 458.12]  We call this contextual answers.
[458.68 --> 463.32]  Another would be summarization rather than response to a specific query.
[463.32 --> 466.30]  You have this 10K report that came out.
[466.84 --> 469.72]  And you want a pithy summarization of it.
[469.92 --> 473.08]  Maybe a summarization geared towards an aspect you care about.
[473.32 --> 474.46]  So that would be another use case.
[474.80 --> 478.18]  These are both ways of consuming data.
[478.40 --> 480.92]  There's, of course – Gen AI is a terrible name.
[481.38 --> 483.30]  But we won't find that battle.
[483.30 --> 484.46]  You're stuck with it.
[485.34 --> 487.08]  Well, you know, you'll get me started.
[487.20 --> 490.74]  I'll start complaining about Gen AI, about AGI, and so on.
[491.74 --> 496.52]  But certainly some use cases call for producing information, not only consuming information.
[497.10 --> 500.74]  So, for example, one of our use cases, very successful, are product descriptions.
[500.94 --> 508.68]  You have companies, retailers and e-commerce companies who have thousands of products that come online constantly.
[508.68 --> 515.00]  And writing a product description is labor-intensive, error-prone, expensive, time-consuming.
[515.52 --> 520.08]  And we're able to compress all of that dramatically.
[520.54 --> 521.98]  So these are some use cases.
[522.30 --> 529.92]  I'm kind of curious also, as you're looking at these opportunities in the enterprise and addressing these various use cases,
[530.42 --> 535.80]  as a company who is creating models and putting them out there for enterprises to use,
[535.80 --> 539.96]  for people who have not, you know, are not in the industry itself,
[540.26 --> 546.94]  how do you as a co-founder and CEO see your company as, like, how do you say, let's go do this?
[546.98 --> 551.02]  Like, we see the value in this compared to others that are making models.
[551.14 --> 556.08]  Like, in other words, if you say, I'm going to make a model, what is it about that motivation
[556.08 --> 559.96]  which makes you think you'll make a difference in that enterprise market?
[559.96 --> 563.94]  You know, and you're kind of representing all companies that do so,
[563.98 --> 567.02]  just to shed some insight on how a founder thinks in the space.
[567.68 --> 572.46]  I wouldn't purport to represent the entire industry, so I'll speak for ourselves.
[572.86 --> 573.40]  Fair enough.
[574.00 --> 575.32]  Overshot on my asking.
[575.46 --> 575.86]  No worries.
[576.24 --> 578.06]  But maybe somebody's comment to others.
[578.16 --> 582.64]  So first of all, the baseline is a general purpose, very capable model.
[583.06 --> 583.98]  There's a need for that.
[583.98 --> 588.90]  Now, there are companies who provide services using other people's models,
[589.10 --> 590.20]  and that's totally legit.
[590.40 --> 594.86]  If you actually own the model, you can do things that you wouldn't be able to do otherwise.
[595.50 --> 600.78]  And our emphasis, in addition to the general capability of the model,
[601.28 --> 605.84]  is in order to make it practical, there are two things, especially in the enterprise.
[606.24 --> 613.10]  So if you're using a chatbot to write a homework assignment,
[613.10 --> 614.84]  the stakes are low.
[615.16 --> 619.24]  A mistake doesn't carry a big penalty, and probably won't somebody.
[619.58 --> 620.52]  Nobody would read it anyway.
[621.10 --> 626.32]  But if you're writing a memo to your boss or to your prized client,
[626.78 --> 631.86]  and if you're brilliant 95% of the time and garbage 5% of the time,
[632.18 --> 633.00]  you're dead in the water.
[633.76 --> 635.64]  And so reliability is key.
[635.64 --> 642.04]  And as we know, large language models are these amazing, creative, knowledgeable system,
[642.26 --> 643.64]  but probabilistic.
[644.22 --> 647.30]  And so you will get – I don't like – here's another term I don't like, hallucination.
[647.38 --> 651.94]  But you'll get stuff that either isn't grounded in fact, doesn't make logical sense,
[652.02 --> 652.92]  and so on.
[653.56 --> 654.46]  And so you can't do that.
[654.52 --> 655.56]  You need to get high reliability.
[655.80 --> 656.46]  That's number one.
[656.78 --> 658.14]  I'll tell you in a moment how we do that.
[658.52 --> 661.32]  But the other thing, it needs to be efficient.
[661.32 --> 665.80]  You know, for every customer query, you're going to pay $10 to answer it,
[665.90 --> 668.44]  and it'll take you 20 seconds to answer it.
[668.86 --> 670.00]  That's not no good either.
[670.60 --> 671.72]  And so you need to address that also.
[672.36 --> 675.10]  So we have several things we're doing in this regard.
[675.22 --> 678.06]  The first is what we call task-specific models.
[678.16 --> 681.58]  In addition to our general purpose model, like Jamba that came out,
[682.06 --> 687.98]  we provide language models that are tailored to specific use cases.
[687.98 --> 689.70]  You can think about it as a matrix.
[689.70 --> 692.32]  You have industries and you have use cases.
[692.80 --> 696.54]  And it turns out that while initially some – you know, you might think that,
[696.66 --> 700.30]  oh, I'm going to do a healthcare LLM or a finance,
[700.54 --> 702.90]  that's a little bit boiling the ocean.
[703.40 --> 704.44]  You want to be more specific.
[704.76 --> 707.20]  And one way to be specific is to think about what I'm going to use it for.
[707.28 --> 707.92]  These are the columns.
[708.58 --> 711.22]  So, for example, take summarization.
[712.18 --> 713.70]  That's a specific task.
[714.12 --> 716.58]  And now you can optimize your system.
[716.58 --> 719.56]  And I am deliberately saying system and not language models.
[719.76 --> 720.94]  I'll tell you in a moment why.
[721.32 --> 723.42]  But you can optimize that for that use case.
[723.90 --> 728.32]  So all companies now are experimenting with multiple solutions, as they should.
[728.32 --> 736.46]  And in this particular use case, a very large finance institution took several of their financial documents,
[737.02 --> 740.24]  several hundred, and tested various solutions.
[740.70 --> 747.08]  Our task-specific model and summarization and some of the general purpose models of, you know, other companies.
[747.08 --> 751.44]  And ours were just hands down better in terms of the quality of the answers they got.
[751.72 --> 754.48]  There was no hallucination, if you pardon the expression.
[755.10 --> 760.30]  Very on point, very grounded, and so on, because it optimized for the task.
[760.76 --> 766.36]  But by the way, if the system is a fraction of the size of the general purpose model,
[766.76 --> 771.22]  so you get the answers immediately, and the cost of serving is low.
[771.22 --> 780.98]  And this enables use cases that, this latency and unit economics enable use cases that would just be unrealistic otherwise.
[781.72 --> 786.12]  So our task-specific models are one approach.
[786.40 --> 791.84]  And maybe I won't overload my answer with saying why it's not only models, but we'll get to AI systems.
[792.42 --> 796.10]  The other is, and it's related, having models are highly efficient.
[796.10 --> 802.52]  And that goes to Jamba as an example of a model that's very capable, but not big.
[802.86 --> 806.50]  If I were to jump ahead and, you know, let's think about 2024.
[806.82 --> 808.28]  What are we going to see in this space?
[808.86 --> 816.02]  Among other things, you'll see focus on total cost of ownership of the reality of serving these models.
[816.54 --> 818.46]  You're going to see a focus on reliability.
[818.46 --> 830.22]  And you're also going to see focus on, not the term I hate, agents, but AI systems that are more elaborate than this transactional interaction with a long term.
[830.42 --> 833.38]  Well, tokens in, you know, a few seconds, token back.
[833.64 --> 834.26]  Thank you.
[834.42 --> 835.16]  On to the next one.
[835.52 --> 836.08]  More elaborate.
[836.22 --> 839.46]  So this is, I think, what's going to happen technologically in the industry.
[839.80 --> 847.12]  You're also going to see, correlated with that, the industry move from what today is a mass experimentation to actual deployments.
[847.12 --> 849.82]  We're seeing signs of it now.
[849.90 --> 853.96]  And I think in 2024, you'll see this sort of face shift there also.
[871.72 --> 873.80]  This is a Changelog News Break.
[873.80 --> 883.04]  On April 18th, Meta released the latest version of their open-ish large language model with state-of-the-art performance.
[883.44 --> 885.16]  The Verge rounds it up like this.
[885.76 --> 886.04]  Quote,
[886.04 --> 892.96]  Meta claims both sizes of Llama 3 beat similarly sized models like Google's Gemma and Gemini,
[893.24 --> 897.88]  Mistral 7b, and Anthropics Claude 3 in certain benchmarking tests.
[897.88 --> 908.38]  In the MMLU benchmark, which typically measures general knowledge, Llama 3 8b performed significantly better than both Gemma 7b and Mistral 7b,
[908.58 --> 913.22]  while Llama 3 70b slightly edged Gemini Pro 1.5.
[913.60 --> 913.98]  End quote.
[914.48 --> 921.40]  What followed was your typical X-Bros posting N mind-blowing demos of what Llama 3 can accomplish,
[921.80 --> 925.88]  where N equals the number that a rival X-Bro just posted, plus one.
[925.88 --> 931.68]  Not very interesting, but two things that did stand out as interesting to me about this announcement.
[932.12 --> 940.02]  First, they didn't compare Llama 3 to GPT-4 at all, so we can only assume it still comes up short when compared to OpenAI's best.
[940.34 --> 948.20]  Second, they continue to call Llama open source, even though the license retains the commercial requirement of your business not being too big,
[948.48 --> 951.00]  which is 700 million monthly active users.
[951.00 --> 957.56]  So I guess Llama 3 is open for businesses of all sizes, depending on how you define all, and sizes.
[958.06 --> 963.26]  You just heard one of our five top stories from Monday's Changelog News.
[963.66 --> 966.80]  Subscribe to the podcast to get all of the week's top stories,
[967.10 --> 970.36]  and pop your email address in at changelog.com slash news
[970.36 --> 976.04]  to also receive our free companion email with even more developer news worth your attention.
[976.48 --> 979.80]  Once again, that's changelog.com slash news.
[979.80 --> 991.30]  So, Jov, I love that you bring in this element of thinking about AI systems,
[991.30 --> 993.76]  not just large language models or the model.
[994.44 --> 997.64]  Maybe that ties a little bit into what you were just talking about,
[997.64 --> 1005.62]  about more complicated workloads or automations that are likely coming as part of the solutions that people are building.
[1005.62 --> 1007.56]  But I'm wondering if you could comment on that.
[1007.70 --> 1016.86]  Like, where does systematic thinking and the thinking about architecting AI systems fit within what you're seeing people do now
[1016.86 --> 1021.58]  and what you think needs to happen for them to get value out of these models?
[1022.16 --> 1028.14]  So the part of the answer that I'm comfortable speaking about has to do with what is out there already,
[1028.18 --> 1031.54]  and the others I'll speculate maybe at a little more higher level.
[1031.54 --> 1036.06]  So even if you look at task-specific models, they're really not models.
[1036.56 --> 1038.00]  They're little systems.
[1038.58 --> 1043.42]  So when you, say, want to do summarization and you say, I care about these elements,
[1043.94 --> 1048.42]  there's a little data processing and reasoning goes on before you call the language model.
[1048.68 --> 1049.74]  So you feed it.
[1049.98 --> 1051.46]  You don't just stick it into the context.
[1051.56 --> 1055.94]  You actually do some reasoning so you can steer the model in the right direction.
[1055.94 --> 1059.48]  And then when you get something back, you don't just spit it out.
[1059.62 --> 1062.66]  You don't sort of sample temperature zero and give the top answer.
[1062.94 --> 1066.40]  You get answers and you evaluate them with validators.
[1067.12 --> 1073.02]  And only when you're confident that the answer is legit, you return it to the user.
[1073.56 --> 1080.20]  And it may sound very expensive, but actually the operation of an LLM totally dominates
[1080.20 --> 1084.36]  in terms of the compute resources and time, these other elements.
[1084.36 --> 1087.74]  And that's an example of a system around the language model.
[1087.82 --> 1089.32]  But that's a baby step.
[1089.92 --> 1094.86]  What you're going to see is, and you're already seeing it now, but right now it's people touching
[1094.86 --> 1099.04]  parts of the elephant and doing it in a very ad hoc-y way.
[1099.32 --> 1104.44]  But you're going to see people stitching together multiple calls to a language model because
[1104.44 --> 1106.32]  a task may require multiple things.
[1106.80 --> 1108.36]  And it's not just chaining.
[1108.64 --> 1111.02]  It can be more complicated scripts that you're running.
[1111.58 --> 1113.22]  But you can't just do it.
[1113.22 --> 1122.00]  It's not like writing a scripting language and running it because the computing elements
[1122.00 --> 1123.32]  here are different.
[1123.60 --> 1126.28]  They're expensive and they're error prone.
[1127.12 --> 1131.38]  And if you just, for example, Cascade calls the language model, number one, it can be very
[1131.38 --> 1131.88]  expensive.
[1132.54 --> 1134.82]  And second, these errors compounds.
[1135.50 --> 1138.26]  And you get, at the end, much more noise than signal.
[1138.26 --> 1141.40]  And so you need to worry about that.
[1141.88 --> 1143.08]  You need to execute differently.
[1143.88 --> 1147.10]  And so that's an example of what you'll see.
[1147.18 --> 1151.56]  And there are other aspects of these AI systems that you'll see come into play.
[1152.10 --> 1154.52]  The term orchestration is often used here.
[1154.96 --> 1156.68]  It means different things to different people.
[1156.68 --> 1162.20]  But very much you have these elements that are running either sequentially or in parallel.
[1162.34 --> 1168.64]  Somehow you need to execute this execution, kind of like an operating system, but an operating
[1168.64 --> 1169.88]  system with AI elements.
[1170.58 --> 1173.38]  And so we and other people use the term AI OS.
[1173.90 --> 1177.08]  Again, an overloaded term doesn't mean anything precise.
[1177.32 --> 1178.74]  But that's the spirit of things.
[1178.74 --> 1184.84]  I kind of want to get maybe to the roles that are interacting with this AI OS, because I think
[1184.84 --> 1191.28]  one of the things people are struggling with is how do I put the right talent in place to
[1191.28 --> 1192.14]  build these?
[1192.44 --> 1197.06]  Because you're talking about like programmatic, operational, systematic thinking, which is
[1197.06 --> 1200.12]  kind of like there's an element of engineering there.
[1200.34 --> 1204.70]  But it's not people that are necessarily building their own models.
[1204.70 --> 1210.18]  They're architecting these solutions and putting the right checks, the right validations in
[1210.18 --> 1210.58]  place.
[1210.78 --> 1214.26]  They're creating more than chains, these workflows.
[1215.20 --> 1220.76]  And there's some engineers coming to the table there, but there's also domain experts who
[1220.76 --> 1224.96]  maybe are able to speak into some of how the models are prompted.
[1225.28 --> 1232.50]  So do you have any kind of observations from your experience with how people are putting together
[1232.50 --> 1238.30]  teams to architect these solutions and these systems like you've just described?
[1238.46 --> 1245.58]  Is it, from your perspective, still going to be a heavy kind of engineering dominated type
[1245.58 --> 1247.06]  of process going forward?
[1247.06 --> 1248.36]  Or are you seeing a mix?
[1248.52 --> 1249.98]  What's your observation there?
[1249.98 --> 1255.36]  So my answer won't be based on an observation because the systems don't exist yet.
[1255.94 --> 1262.16]  They're baby solutions right now, but I don't think they represent what we'll see going
[1262.16 --> 1262.54]  forward.
[1263.32 --> 1267.32]  But in answer to your question, it very much will be a mix.
[1267.98 --> 1274.24]  There will be companies such as ours that will put in the foundational infrastructure to
[1274.24 --> 1275.66]  run these complicated flows.
[1276.14 --> 1282.48]  These will have to be extensible systems, and they'll be extensible in a variety of ways.
[1282.58 --> 1287.80]  Some of them, absolutely, you'll be able to have programmers write actual code and insert
[1287.80 --> 1288.62]  the code there.
[1288.62 --> 1295.56]  But there absolutely will be a role for low code or even no code specification of the flow
[1295.56 --> 1298.36]  you want on top of this framework.
[1298.76 --> 1307.80]  There will be a data scientist that will write validations of various kinds and data pipelines
[1307.80 --> 1308.34]  for sure.
[1308.34 --> 1317.82]  And so I think everybody from the developer to the data scientist to the business user who's
[1317.82 --> 1322.72]  somewhat savvy to the end user who just wants a system that works, everybody will have a
[1322.72 --> 1324.06]  role and interaction.
[1324.24 --> 1325.80]  And we haven't mentioned DevOps yet.
[1326.32 --> 1328.30]  DevOps here is going to be very important also.
[1328.30 --> 1333.54]  As we've kind of talked around the ecosystem a little bit and what, you know, about systems
[1333.54 --> 1338.98]  themselves, can we turn a little bit and could you tell us a little bit about as we're leading
[1338.98 --> 1343.72]  toward into Jamba, but I'd like to know a little bit about kind of where the company has been
[1343.72 --> 1348.98]  and some of the models that you have put out there leading into this one and kind of the
[1348.98 --> 1351.26]  heritage of how you've developed that.
[1351.60 --> 1355.56]  We'd really be interested in kind of how you've pursued that since you started the company.
[1355.56 --> 1361.84]  I can divide it into three periods in our long history of six years.
[1362.38 --> 1364.56]  That's an eon in AI these days, you know, that's...
[1365.14 --> 1366.90]  I had a different color hair when we started.
[1368.74 --> 1371.16]  As I said, we started by building Jurassic One.
[1371.70 --> 1375.58]  We just felt like we absolutely had to build it.
[1375.84 --> 1381.68]  And we did, we innovated there, but in a minor way, we, you know, we had a vocabulary that
[1381.68 --> 1384.36]  was five times the size of what was common at the time.
[1384.36 --> 1391.18]  It was rather than 50,000 tokens, we had 250,000, slightly larger than GPT-3, not to make a point
[1391.18 --> 1396.22]  just because it worked out that way, 178 billion parameters, a dense model.
[1396.70 --> 1398.18]  And that served us well.
[1398.90 --> 1403.28]  But the next phase in our sort of, we did many things.
[1403.38 --> 1407.78]  We had our own application called WordTune that had done very well, a reading and writing
[1407.78 --> 1409.74]  assistant using our technology.
[1409.74 --> 1415.76]  But on the models themselves, the next thing we put out are task-specific models, which
[1415.76 --> 1418.82]  basically, it's not really distillation, and it's not just fine-tuning.
[1419.38 --> 1423.06]  Like I said, it's putting a system around it, but at the end of the day, you get something
[1423.06 --> 1426.32]  compact for certain use cases, and that set is growing.
[1426.96 --> 1429.24]  That was our second phase.
[1429.24 --> 1437.00]  And the third phase was really seeking a way to make these models fundamentally more scalable,
[1437.68 --> 1443.86]  more efficient to serve, especially in this era of, you know, RAG kind of solutions.
[1444.52 --> 1451.68]  So you have stuff that you want to kind of bring in at inference time to influence the output
[1451.68 --> 1452.36]  of the system.
[1452.36 --> 1457.58]  And at some point, the system chokes, you know, we had a context window that's 4K, then
[1457.58 --> 1458.88]  8K, then 16K.
[1459.48 --> 1465.90]  Now, although some bigger numbers are thrown out, but most models choke at 32K, maybe 64K.
[1466.18 --> 1467.90]  That's not enough if you want to put it.
[1468.02 --> 1476.30]  So we wanted something that, now, if you were to run it on, you know, 64 H100s, you can do
[1476.30 --> 1478.38]  a lot of things, but that's not realistic.
[1478.38 --> 1484.08]  So the question was how to get something that's efficient, that can run effectively on a small
[1484.08 --> 1484.46]  footprint.
[1484.84 --> 1486.14]  And that's how we got to Jamba.
[1486.94 --> 1493.00]  With Jamba, you mentioned taking some things from kind of the Mamba architecture, the sort
[1493.00 --> 1497.30]  of SSM, and adding in some transformer-based things.
[1497.38 --> 1503.04]  For those that aren't familiar with the kind of background with those types of models, maybe
[1503.04 --> 1507.70]  the kind of non-transformer models that people were exploring.
[1508.24 --> 1513.96]  Could you give a little bit of context to that and why it was important for, I mean, you've
[1513.96 --> 1519.08]  already mentioned efficiency and other things, but why you felt it was kind of important in
[1519.08 --> 1524.14]  this generation of model to pull the trigger in a slightly different architectural direction?
[1524.74 --> 1524.88]  Sure.
[1524.88 --> 1530.38]  And for this, maybe we can double-click a little bit about how these systems are architected.
[1530.38 --> 1537.68]  So at some point, the dominant architecture where the RNN, you know, these, and then LSTMs,
[1537.84 --> 1542.22]  as you go left to right, the system doesn't remember the distant past.
[1542.32 --> 1547.88]  What it does, it carries with it the state that somehow encapsulates everything that it's
[1547.88 --> 1548.56]  seen so far.
[1548.96 --> 1549.94]  That's quite powerful.
[1550.12 --> 1557.62]  But as this path gets long, it gets harder and harder to encode and access that information
[1557.62 --> 1558.38]  that's been encoded.
[1558.38 --> 1565.24]  And it worked fine for vision because this, in vision, object recognition is something
[1565.24 --> 1565.98]  very local.
[1566.42 --> 1567.20]  It's iconic.
[1567.44 --> 1570.40]  Iconic in the sense that what you see is what you get, right?
[1570.42 --> 1571.42]  Like I said, the phone.
[1571.84 --> 1572.44]  This is a phone.
[1572.52 --> 1573.30]  I don't care what's here.
[1573.42 --> 1574.40]  So I go along.
[1574.48 --> 1575.02]  I hit the phone.
[1575.32 --> 1576.24]  So I don't need to remember.
[1576.68 --> 1578.10]  But in language, different.
[1578.58 --> 1582.64]  And in fact, if you looked at the benchmarks, by the way, another pet peeve of mine, benchmarks
[1582.64 --> 1584.06]  are, can be very misleading.
[1584.06 --> 1588.64]  But that aside, if you looked at the national language benchmarks, they kind of puttered
[1588.64 --> 1591.68]  along with not much progress until transformers came in.
[1592.60 --> 1596.08]  And transformers, again, coincidentally, what is it, about six years now?
[1596.48 --> 1601.52]  They changed the architecture and they had the attention mechanism that says, no, I mean,
[1601.54 --> 1605.04]  as I'm going along, I can relate disparate pieces of information.
[1605.04 --> 1609.50]  And that allowed you to do things you couldn't do otherwise.
[1610.14 --> 1610.68]  And that's great.
[1610.80 --> 1612.90]  So the quality answer is, shut up.
[1613.30 --> 1618.80]  You pay a price because the complexity is quadratic now in the context length.
[1619.50 --> 1623.80]  And that kills you, which wasn't the case with RNNs or LSTMs.
[1624.38 --> 1625.22]  There, it's linear.
[1625.58 --> 1626.14]  I mean, you just.
[1627.14 --> 1630.44]  And so the question is, how can you have your cake and eat it too?
[1630.44 --> 1636.06]  You enjoy the benefits of being interrelated disparate kind of pieces of information and
[1636.06 --> 1638.80]  yet have something that's, if not linear, close to linear.
[1639.46 --> 1645.18]  And so Mamba, so first let's say Mamba is a straight kind of left to right what's called
[1645.18 --> 1648.80]  SSM model and the structure safe space.
[1649.28 --> 1654.52]  But its innovation was, it was a version that allows you to actually parallelize the training
[1654.52 --> 1656.26]  and much more efficient.
[1656.26 --> 1660.52]  But it still suffered from the lower quality of answers.
[1661.22 --> 1665.80]  And so what our guys did was say, okay, we'll take this as a basic building block.
[1665.98 --> 1669.06]  And Mamba is all of what, four months old now.
[1669.28 --> 1670.30]  It's just academia recently.
[1670.74 --> 1670.88]  Yeah.
[1671.26 --> 1674.02]  But I said, that seemed like a really good idea.
[1674.46 --> 1679.80]  But let's now take elements of the transformer architecture and put it in.
[1679.80 --> 1685.86]  And so every few, in our case it was every eight or 16, depending on which version, layers,
[1686.30 --> 1687.72]  you put an attention mechanism.
[1688.38 --> 1692.40]  So you take a little performance hit, but not nearly as much as if you had transformers
[1692.40 --> 1692.80]  all the way.
[1693.46 --> 1695.94]  So that's kind of how it led to this particular architecture.
[1695.94 --> 1703.42]  Well, Yoav, you did mention that Mamba is only a recently released architecture and published
[1703.42 --> 1706.54]  architecture, but you've been able to move quite quickly.
[1706.84 --> 1710.58]  And I want to talk a little bit about Jamba and the release and all of that.
[1710.72 --> 1713.48]  But prior to that, it might be interesting for listeners.
[1714.16 --> 1720.86]  Most of our listeners aren't sitting in a company that is trying to be a foundation model builder,
[1721.34 --> 1724.26]  building these kind of more general purpose models.
[1724.26 --> 1729.64]  I'm wondering if you could give a picture a little bit behind the scenes, whatever you
[1729.64 --> 1735.94]  think would be interesting on what does it actually take to go from, hey, this idea we
[1735.94 --> 1742.18]  want to mix, kind of get the best of both worlds with Mamba and transformers all the way to,
[1742.66 --> 1745.38]  hey, here's our blog post releasing a model.
[1745.88 --> 1749.38]  What were some of the challenges in that kind of middle zone?
[1749.38 --> 1755.70]  And what is that process like to determine, you know, from data set to exact architecture
[1755.70 --> 1758.48]  and the sort of final training runs?
[1759.06 --> 1765.34]  So first I'll say that I don't think that everybody needs to be building foundation models.
[1765.64 --> 1773.32]  But as I said to somebody, if somebody, an organization is a technical and wants to remain relevant,
[1773.32 --> 1779.20]  even if they're not building foundation models, they should understand how they're built.
[1779.76 --> 1784.16]  And if they really put their mind to it and their resources, they could build one because
[1784.16 --> 1787.10]  it really gives you a visceral, deep sense of what's going on.
[1787.66 --> 1791.70]  Now, regarding the Jamba, we actually tried to be very transparent.
[1791.70 --> 1795.34]  You know, people, so this is our first open source model.
[1796.08 --> 1801.20]  And the reason we did it was that it is very novel.
[1802.04 --> 1805.42]  And there's lots of more experimentation to be done here.
[1805.72 --> 1812.80]  Optimization, serving the, you know, training these models can't be done on every type of infrastructure.
[1813.52 --> 1814.48]  Serving them similarly.
[1814.48 --> 1821.34]  And where you do serve them right now, we've had several years to optimize the serving of transformers.
[1821.74 --> 1824.78]  We want to enable the community to innovate here.
[1825.58 --> 1832.12]  And so we were quite explicit in our white paper, perhaps unusually so, relative to the industry.
[1832.80 --> 1838.54]  So to the listeners who want to kind of get the nitty gritty, I really encourage them to look at the technical white paper.
[1838.54 --> 1849.72]  But I can tell you there's been a ton of experimentation of ablations that our guys did, trading off very, lots of, people use the term hyperparameters.
[1850.56 --> 1854.10]  It hides a lot of things that are very different from one another.
[1854.58 --> 1856.28]  But how many layers do you want?
[1856.56 --> 1858.50]  And, you know, how many Mamba layers?
[1858.58 --> 1859.60]  How many attention layers?
[1860.06 --> 1860.84]  Batch sizes?
[1861.78 --> 1866.28]  All kinds of stuff that, and what really makes a difference?
[1866.28 --> 1869.00]  It's hard to sometimes understand what makes a difference.
[1869.28 --> 1880.40]  And, again, we try to share the, for example, Mamba, I said that Mamba's performance doesn't compete with the performance of comparably sized transformer models.
[1881.00 --> 1886.68]  But that's at the, when you look at the details, it's actually quite competitive on many of the benchmarks.
[1887.10 --> 1890.32]  But then there are a few that it's really bad at.
[1890.72 --> 1893.02]  And that gives you a clue of why that's the case.
[1893.02 --> 1900.82]  It can latch on to surface formulations and syntax that the transformer is managed to just abstract away from.
[1901.46 --> 1904.76]  And so we describe how, you know, you make this observation, you correct for it.
[1905.02 --> 1908.92]  There's lots of details that go into making these decisions.
[1909.30 --> 1911.96]  And then there's also pragmatic decisions.
[1912.08 --> 1917.82]  For example, we wanted a model that will fit on a single 80 gigabyte GPU.
[1917.96 --> 1919.60]  That was a design decision.
[1919.60 --> 1928.42]  And from that emanated a few things that, you know, we did put a bigger model and, you know, certain contact windows will fit there.
[1928.50 --> 1929.52]  Others won't.
[1929.86 --> 1934.64]  It's still, you know, 256K is humongous compared to the alternative.
[1935.34 --> 1940.28]  But we can also do a million and larger, but not on a single GPU.
[1940.28 --> 1944.30]  And so those are some of the design decisions and the rationale.
[1945.22 --> 1954.22]  Honestly, it is a process, although condensed, a process that involved, you know, hundreds of decisions that led to what we put out.
[1954.62 --> 1957.20]  That was a really great explanation.
[1957.46 --> 1958.68]  I appreciate that.
[1958.68 --> 1969.20]  As you were going through it and I was thinking about the applicability for Jamba in the enterprise and kind of bringing the innovation, I'm curious is why.
[1969.50 --> 1975.60]  I know you had kind of alluded to the fact that Jamba early in the explanation was kind of the first open source model.
[1976.22 --> 1987.12]  And so I was wondering, as you're trying to enable enterprise innovation, what was the change in your thought process that made you decide to go open source with Jamba versus the earlier models?
[1987.12 --> 1988.30]  What was the thinking around that?
[1988.34 --> 1990.64]  I was curious as you said it and wanted to wait till we got to the end.
[1991.28 --> 1994.42]  Yeah, it really was very simple.
[1994.96 --> 2004.38]  We felt like if we were the only ones augmenting and pushing on this model, it wouldn't advance as fast as it could.
[2004.88 --> 2016.94]  And we saw that within days of our putting it out there, there was, I think today, I haven't tracked it, but when I looked at about a week ago, the 30,000 downloads and I forget how many forks, but a large number of forks.
[2017.12 --> 2021.72]  So by the way, very important to say what we put out is a base model, not a fine-tune model.
[2022.24 --> 2031.18]  And we're very clear about it and we caution people for using it for production purposes or for user-facing application.
[2031.78 --> 2040.26]  And of course, we'll be coming up with our, in fact, we've announced that it's available for preview, our aligned model.
[2040.26 --> 2047.04]  But we felt like there's, it was really important for the community to add value to this architecture.
[2047.20 --> 2048.08]  And that's why we did it.
[2048.08 --> 2056.36]  For those that are listening a little bit later on the podcast, so it looks like Jamba, at the time we're recording, this was released, at least on Hugging Face.
[2057.02 --> 2059.46]  Well, it was updated 15 days ago.
[2059.66 --> 2064.06]  And I see the blog post at the end of March, I believe.
[2064.26 --> 2070.10]  But now on Hugging Face, there's sort of 38 models I see with Jamba in the name.
[2070.10 --> 2076.62]  That's sort of not including those maybe that forked and just created their own special name.
[2077.14 --> 2084.82]  So already you're seeing this kind of explosion of a model family, I guess, which is quite interesting.
[2084.82 --> 2095.44]  I'm wondering, over time as a company, you mentioned kind of not being the only ones working on the model family and wanting to see it become more.
[2095.70 --> 2101.90]  Is that observation kind of based on what you've seen in other model families, whether it be Llama 2 or Mistral and others?
[2102.08 --> 2109.24]  And there's sort of, because when I look at a model like that that's released, I almost immediately, and I know people, you mentioned DevOps,
[2109.24 --> 2119.12]  people have automated pipelines in place to create the quantized version of this or fine tune it for that on their data set.
[2119.26 --> 2126.04]  We had the noose research, we had a discussion about noose research and what they're doing in some of this areas as well.
[2126.52 --> 2132.74]  So what is the sort of innovation that you're hoping for with the kind of Jamba model family?
[2132.74 --> 2138.48]  Is it, you mentioned fine tunes or, you know, you're releasing the base model, there could be fine tunes.
[2138.48 --> 2141.60]  But I think also there could be much more than that.
[2141.82 --> 2149.78]  So what are you kind of hoping to see as people get hands on with the model and try to explore various elements of how to use it?
[2150.12 --> 2153.68]  Yeah, fine tuning is happening, will happen.
[2154.18 --> 2158.66]  Like I said, we have our own fine tune or aligned model.
[2159.14 --> 2162.00]  And, but that's not the reason we put it out there.
[2162.00 --> 2169.54]  The reason we put it out there is that people can contribute to the very model so others can benefit from it.
[2169.90 --> 2174.68]  And I think there's at least two areas where a lot of value can be brought.
[2174.82 --> 2176.50]  One is serving efficiency.
[2177.00 --> 2187.72]  For example, when you consume it on Hugging Face, it's less efficient than we consume it on our platform because we have optimized the serving and we'll continue to optimize.
[2187.72 --> 2195.06]  But a lot of smart people out there and we'd love for them to optimize it further and everybody will benefit, including us.
[2195.54 --> 2196.42]  That's one thing.
[2196.94 --> 2210.84]  The other thing is that I think it's a really, we would really value it if this kind of model were able to be trained on multiple types of infrastructure, which currently isn't the case.
[2210.84 --> 2223.46]  And so I think by putting it out there, people now, they can look at the white paper, they can look at the model, and they can now enable further training of such models, which will benefit everybody, including us.
[2224.04 --> 2227.84]  So as we start to wind up here, fascinating discussion.
[2228.10 --> 2230.52]  Thank you very much for taking us through all the insight.
[2230.52 --> 2247.48]  I like to wind up asking kind of where you think things are going and if you could address it potentially at two levels, both kind of where your own organization expects to go, what kind of thinking you have over whatever horizon is on your mind.
[2247.48 --> 2261.20]  But also give us insight into how you think the industry as a whole is progressing and how you expect that kind of servicing the enterprise need to evolve with the strategies that are out there.
[2261.42 --> 2264.56]  We'd love to understand how you're seeing the world in that way.
[2264.82 --> 2269.58]  I think the key notion is reliability, trust and reliability.
[2269.58 --> 2281.66]  You need to have the same kind of trust in the system to be able to predict what they'll do, be able to understand what they did, as you do with other pieces of software.
[2282.20 --> 2288.98]  You know, we always have errors, you know, even the Pentium had a bug, but that's an exception.
[2289.54 --> 2292.18]  Whereas currently it's the rule for language models.
[2292.32 --> 2294.40]  So that can't be in the enterprise.
[2294.40 --> 2300.34]  And everything that I think about what's going to happen in the enterprise orients around that.
[2300.58 --> 2305.58]  I think you'll see special purpose models like our task specific models.
[2305.82 --> 2311.08]  I think you'll see AI systems increasingly sophisticated and robust.
[2311.18 --> 2314.76]  Right now they're not robust, they're experimental, but you'll see more AI system.
[2315.88 --> 2319.86]  And I think this may sound philosophical, so bear with me.
[2319.86 --> 2329.68]  But there's a question within the AI community, do these language models actually understand what they're talking about?
[2330.46 --> 2335.32]  They spit out this incredibly convincing stuff, very smart, something on point.
[2335.78 --> 2337.40]  And how can they not understand?
[2338.00 --> 2339.48]  And it's sometimes they're totally stupid.
[2339.98 --> 2341.80]  And everybody, we all have favorite examples.
[2341.80 --> 2350.26]  And I think we need to get to the point where we believe that the system actually understand what they're talking about.
[2351.04 --> 2355.70]  And what understanding is, is, again, it sounds philosophical.
[2356.26 --> 2358.72]  And there's a philosophical aspect to it, for sure.
[2359.46 --> 2361.56]  But it has very practical ramifications.
[2361.56 --> 2372.08]  And so when I think about the future, all these pragmatic things, task specific models, AI systems, but in the background, this notion of understanding.
[2372.24 --> 2373.80]  These systems need to really understand.
[2374.20 --> 2375.12]  That's what I'm looking at.
[2375.96 --> 2376.78]  Yeah, that's great.
[2376.94 --> 2389.10]  Well, I think as a part of the development towards that, certainly open models and innovation around these model families, like we talked about, I hope, is a key piece of that.
[2389.10 --> 2406.42]  And from a member of the community, I just want to express my thanks to AI21 for being a leader, both in terms of the thinking and infrastructure and innovation in this area, but also a leader in terms of putting things out there for the community to work on as a community.
[2406.70 --> 2409.14]  So thank you for what you've done with Jamba.
[2409.42 --> 2414.22]  And really excited to follow AI21 and where you're headed next.
[2414.32 --> 2416.02]  So thank you so much for joining us, Yav.
[2416.08 --> 2416.74]  It's been a pleasure.
[2417.12 --> 2418.56]  Thanks very much for having me.
[2419.10 --> 2449.08]  Thank you.
[2449.10 --> 2455.80]  Thanks again to our partners at fly.io, to our beat freaking residents, Breakmaster Cylinder, and to you for listening.
[2456.14 --> 2457.92]  We appreciate you spending time with us.
[2458.30 --> 2459.46]  That's all for now.
[2459.70 --> 2461.38]  We'll talk to you again next time.
