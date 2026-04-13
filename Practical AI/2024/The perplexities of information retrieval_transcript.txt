[0.00 --> 8.66]  Welcome to Practical AI.
[9.34 --> 16.78]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is
[16.78 --> 19.54]  changing the world, this is the show for you.
[20.24 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 30.94]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions
[30.94 --> 35.44]  on six continents, so you can launch your app near your users.
[35.82 --> 37.84]  Learn more at Fly.io.
[45.12 --> 46.22]  What's up friends?
[46.38 --> 48.56]  Do you remember when ChatGPT launched?
[48.76 --> 49.22]  I do.
[49.46 --> 53.72]  It felt like the LLM was this magical tool out of the box.
[53.72 --> 57.48]  However, the more you use it, the more you realize that's just not the case.
[57.74 --> 62.60]  The technology is brilliant, don't get me wrong, but it's prone to issues like hallucination
[62.60 --> 64.04]  on its own, but there's hope.
[64.36 --> 65.74]  There is still hope.
[66.14 --> 71.72]  Feed the LLM reliable current data, ground it in the right data and context, then and
[71.72 --> 75.64]  only then can it make the right connections and give the right answers.
[76.02 --> 81.08]  The team at Neo4j has been exploring how to get results by pairing LLMs with knowledge
[81.08 --> 82.74]  graphs and vector search.
[82.74 --> 89.86]  Check out their podcast episode about LLMs and knowledge graphs throughout 2023 at graphstuff.fm.
[89.96 --> 93.82]  They share tips on retrieval methods, prompt engineering, and so much more.
[94.08 --> 94.76]  Don't miss it.
[95.02 --> 96.60]  Find a link in our show notes.
[97.06 --> 97.88]  Yes, check it out.
[98.10 --> 100.96]  Graphstuff.fm, episode 23.
[100.96 --> 113.86]  Welcome to another episode of Practical AI.
[114.20 --> 115.70]  This is Daniel Whitenack.
[115.82 --> 121.42]  I am founder and CEO at Prediction Guard, where we're safeguarding private AI models.
[121.74 --> 128.08]  And I'm joined, as always, by my co-host, Chris Benson, who is a principal AI research engineer
[128.08 --> 129.24]  at Lockheed Martin.
[129.64 --> 130.32]  How are you doing, Chris?
[130.32 --> 131.68]  Doing great today, Daniel.
[131.74 --> 132.14]  How's it going?
[132.62 --> 133.46]  It's going great.
[133.64 --> 140.86]  I am sometimes perplexed throughout my workday, but generally the week has gone well.
[141.14 --> 147.84]  And I'm really excited because hopefully our guests today will provide a lot of ways for
[147.84 --> 149.70]  us to navigate through the perplexity.
[150.04 --> 151.64]  I hope he finds that punny.
[151.64 --> 153.42]  Yes, yes, of course.
[153.92 --> 160.38]  We have with us today Dennis Yarets, who is the CTO and co-founder at Perplexity.
[160.62 --> 161.06]  Welcome.
[161.62 --> 164.00]  Thanks for inviting me, and great to be on the show.
[164.68 --> 165.38]  Yeah, yeah.
[165.38 --> 169.28]  Well, we've been wanting to make this one happen for a good long while.
[169.40 --> 174.08]  Of course, been following the things that Perplexity has been doing.
[174.36 --> 177.22]  Really impressive and inspiring work.
[177.70 --> 181.44]  And yeah, just really excited to hear a little bit about that story.
[181.44 --> 188.26]  And also this kind of space of answering, giving people knowledge with generative AI, with language
[188.26 --> 191.30]  models, search more generally maybe.
[191.30 --> 198.32]  Could you set us up by maybe talking through, of course, people have followed, everyone's
[198.32 --> 203.10]  kind of followed this surge of generative AI over the last couple of years.
[203.10 --> 209.52]  But there's been kind of a segment of that that has focused a lot on kind of answering
[209.52 --> 216.56]  questions, discovering knowledge, curiosity, exploring topics, an intersection with search
[216.56 --> 217.86]  more generally, I guess.
[218.46 --> 224.38]  So could you kind of help us understand maybe that journey, how that's kind of developed and
[224.38 --> 231.40]  how also you and the co-founders of Perplexity kind of came upon your approach to that?
[231.40 --> 235.96]  Yeah, that's definitely been like very fascinating, almost two years, I guess.
[237.38 --> 239.56]  I think like general like web search, right?
[239.56 --> 243.32]  So like what do you want to ultimately get is an answer to your question, right?
[243.40 --> 248.00]  So it's the current iteration that we had like when it was Google and all the other like
[248.00 --> 252.72]  classical search engines is an approximation to get to this point, right?
[252.76 --> 256.96]  So you have your question, you ask it as a form of query, and then you get like a bunch
[256.96 --> 263.14]  of documents that are very relevant, but you have to still do ultimate sort of like you
[263.14 --> 266.36]  have to do like additional work to get to the bottom of it, right?
[266.36 --> 271.24]  So you have to scan through the documents, you have to for yourself understand what is
[271.24 --> 272.60]  this a true answer?
[273.02 --> 277.56]  If it's a not true answer, kind of like have to trust the information.
[277.56 --> 282.80]  And as you can imagine, it's a lot of work, especially if you're trying to search for
[282.80 --> 287.74]  something very complicated, maybe things that are not so obvious.
[288.32 --> 292.50]  And would it be nice to kind of like avoid that step, right?
[292.54 --> 297.40]  Where you just like answer a question, ask the question and you get an answer right away.
[297.48 --> 300.86]  So that's kind of like ultimate destination where we're trying to get.
[300.86 --> 308.34]  Obviously, there has been, it's been tough to get there over last like decade or so.
[308.52 --> 312.24]  It's, you know, there's been like a lot of work, but it never quite work.
[312.34 --> 318.56]  There is a, this like a much higher level of hallucinations, much higher level of maybe
[318.56 --> 320.66]  not perfect synthesis of the information.
[320.66 --> 323.54]  You kind of like basically get like a Frankenstein.
[323.54 --> 330.32]  And so it's like, instead of like a hearing and nice, easily parsable of readable answer,
[330.32 --> 334.16]  you get like some just like basically extracted pieces of the information and you just like
[334.16 --> 335.14]  concatenate it together.
[335.26 --> 336.20]  So like not very pleasant.
[336.74 --> 342.86]  And, you know, it's funny that when we started, so one of our angel investor was Jeff Dean,
[343.36 --> 344.74]  requires like no introduction.
[345.38 --> 351.36]  And he was saying, you know, Google actually wanted to always build something like this,
[351.36 --> 356.86]  but it's just because they have like such high expectations for accuracy because like,
[356.90 --> 359.80]  you know, millions of billions of users using Google, right?
[359.84 --> 364.98]  And like, if you like hallucinate like 1% of the time, you're going to get a lot of unhappy
[364.98 --> 365.34]  people.
[365.34 --> 370.90]  And so they would never able to, because of the models were like not as strong as they
[370.90 --> 371.72]  are right now.
[371.72 --> 375.88]  They were never able to get to just like 99.9% of accuracy.
[376.08 --> 376.20]  Right.
[376.28 --> 379.40]  And that's why kind of like this work never pan out.
[379.40 --> 384.78]  But something great happened, you know, 2022, right?
[384.88 --> 390.42]  So we, when we started our company, we kind of, you know, both myself and Aravind,
[390.62 --> 394.60]  my mic of Cofondren, we come from like academics, right?
[394.62 --> 398.42]  We've been doing like a lot of research on like language modeling, reinforcement learning
[398.42 --> 399.10]  and stuff like that.
[399.48 --> 401.44]  And he was actually at OpenAI at that time.
[401.50 --> 407.54]  Like we've been very like clearly following improvements of GPT models, like GPT-2 and then
[407.54 --> 410.28]  GPT-3, that's where it's actually got very interesting.
[410.98 --> 415.10]  And it was kind of like became obvious and obvious there is going to be something there.
[415.10 --> 415.50]  Right.
[415.60 --> 420.52]  So, and this was the primarily motivation for us to start a company.
[421.02 --> 425.98]  We wanted to do build an answer engine from the get-go, but it was kind of like very ambitious.
[426.46 --> 431.62]  You, like, I remember we would go to the investors and there was a say like, oh, we're going to build
[431.62 --> 435.24]  a search engine and they're like, start like, you know, looking at you like you're crazy,
[435.70 --> 437.04]  which is, makes a lot of sense.
[437.10 --> 438.48]  They were still like, oh, there's Google already.
[438.88 --> 442.92]  And they had like a fair point, but we, we still kind of like weren't like very discouraged
[442.92 --> 443.34]  by that.
[443.46 --> 446.82]  We knew there is like something there and we started like prototyping.
[446.96 --> 451.90]  So we, the first version of Perplexity, we actually created as a Slack bot or like Discord
[451.90 --> 456.56]  bot where kind of like, it was a very primitive combination of a search engine.
[456.56 --> 459.42]  And plus at that point it was like DaVinci 2 models.
[459.58 --> 465.64]  It's still, you know, pre-chat GPT and it's kind of like worked much better than I expected.
[466.00 --> 466.92]  It was like very quick.
[466.96 --> 471.34]  Like we put, put it up this demo, like in a couple of days and it was like, you can already
[471.34 --> 475.08]  see that in certain cases it is very helpful.
[475.08 --> 479.28]  Like we, because this was like very early company, we were like trying to, we were like
[479.28 --> 481.10]  trying to hire like one of our first engineers.
[481.28 --> 486.46]  So we, and we didn't know like how to organize the insurance for him or like what it,
[486.56 --> 490.02]  and so we actually use this bot to like ask those questions about insurance.
[490.02 --> 493.88]  Because if you go to Google and start asking the questions about insurance, you're going
[493.88 --> 500.40]  to get a lot of ads and you just going to get very quickly, you know, disappointed.
[500.82 --> 505.56]  I've appreciated that same thing and founding a company and using these models in that, in
[505.56 --> 506.02]  that way.
[506.10 --> 506.96]  It's very useful.
[507.28 --> 507.78]  Yeah, exactly.
[508.08 --> 509.56]  And then it was kind of like useful.
[509.72 --> 513.30]  So we were kind of like been trying it out and like playing with it.
[513.30 --> 519.44]  But then what really happened, start happening is like, I think it was like a couple of weeks
[519.44 --> 523.32]  before ChatGPT, they, OpenAI released this DaVinci 3 model.
[524.28 --> 529.96]  And I literally remember very clearly like changed the, like literally the model name
[529.96 --> 533.12]  and start asking the same questions that I was asking before.
[533.12 --> 536.16]  And I could see right away, it's just like so much better.
[536.66 --> 539.90]  It's just like so much better at understanding what you, of your intent.
[539.90 --> 545.06]  So much better at like understanding where, like, what should it say, what it should not
[545.06 --> 545.30]  say.
[545.40 --> 547.24]  So much better, like synthesizing the answer.
[547.34 --> 549.20]  And I was just like really like blown away.
[549.90 --> 553.54]  And, you know, I was like, okay, so there is like definitely something there.
[553.62 --> 556.44]  And then obviously ChatGPT happens like a few weeks after and we were like, okay, so we
[556.44 --> 561.52]  have to, like our initial product was actually, because as I mentioned, we came from academic
[561.52 --> 561.86]  background.
[562.08 --> 567.98]  Like our citations were like the core component because it was like very clear to us from the
[567.98 --> 571.28]  beginning, like if you want to get an answer, you want to make sure it's accurate.
[571.58 --> 573.56]  You want to make sure you can verify it.
[574.24 --> 577.74]  And so the citation was like the sort of like first class citizen in our product.
[577.84 --> 582.78]  And then when ChatGPT came out, we was like, okay, so one of the biggest point of feedback
[582.78 --> 587.10]  for them was, okay, so I don't know, like if this is accurate information, if it's not,
[587.18 --> 589.38]  if it's a hallucination, if it's not, how would I verify it?
[589.82 --> 593.20]  And that's why we like recently decided, okay, so this seems like a good opportunity to release
[593.20 --> 593.62]  our product.
[593.72 --> 598.54]  We like literally in a matter of like today's put up a website connected to our like backend
[598.54 --> 604.76]  that we had and just like, obviously did not expect that it's going to be people going
[604.76 --> 607.42]  to use it and like the usage is going to grow as much as possible.
[607.42 --> 611.56]  But coming back to your original question, I think like what happened, it was just like
[611.56 --> 614.32]  literally this in a matter of like days or month.
[614.32 --> 619.08]  I mean, obviously it follows like a lot of years, many years of research, but like it
[619.08 --> 623.36]  was very clear step function in the quality of the generated answers.
[623.64 --> 627.02]  And you can like literally, if you, if you sort of like spend some time playing with it,
[627.02 --> 630.92]  you can clearly see that it's now becomes very, very good.
[631.18 --> 634.66]  We also realized at that time, okay, so like models only going to get better.
[635.10 --> 636.78]  Things only going to get like faster and cheaper.
[636.94 --> 639.20]  So there is something, there is a lot of stuff to build here.
[639.20 --> 644.64]  For those who are still kind of learning about your organization and, and what you're offering,
[644.76 --> 646.26]  could you step back for a second?
[646.52 --> 651.96]  Like if you were talking to Jeff Dean or another investor, kind of giving them the elevator pitch
[651.96 --> 658.32]  about what you're doing specifically and, you know, how it's differentiated from the GPTs
[658.32 --> 660.48]  and stuff out there, how do you define that?
[660.56 --> 665.34]  What, how do you describe yourself in terms of the specific opportunity that you're pursuing?
[665.34 --> 669.42]  The fastest way to get the most accurate answers to your questions.
[669.42 --> 671.98]  I think that that's essentially like answer engine.
[672.08 --> 675.16]  Then we're kind of like one of, one of the first people who coined this term.
[675.68 --> 677.90]  And can you differentiate that from a search engine a little bit there?
[678.28 --> 678.42]  Yeah.
[678.48 --> 678.62]  Yeah.
[678.62 --> 680.24]  So basically in a search engine, right.
[680.30 --> 685.52]  So you, you get like all the way it's like, as I mentioned before, in the search engine,
[685.52 --> 687.82]  you have to search first, you get a documents.
[687.92 --> 692.84]  Let's say you have like top 10 results and you have to scan through all of them and identify
[692.84 --> 694.32]  the information to get your answer.
[694.32 --> 696.76]  Here we kind of like, we do this step for you.
[696.90 --> 702.76]  So we take the first step of the retrieval of the relevant documents, and then we synthesize
[702.76 --> 708.96]  them into a human readable, nicely firmated answer that you can then like, if needed, if
[708.96 --> 713.40]  you want to get more information, then you can click on the citations that are kind of
[713.40 --> 715.16]  like nicely attributed for each sentence.
[715.16 --> 716.80]  And then you can like learn more information.
[717.28 --> 721.22]  And so we kind of like wanted to do things like very simple.
[721.22 --> 722.66]  We were like early on identified.
[722.66 --> 723.02]  identified.
[723.02 --> 724.96]  So there is like two things we care about.
[725.06 --> 727.54]  This is a accuracy and then speed.
[728.06 --> 730.38]  Cause this is, you know, you want to get information fast.
[730.76 --> 734.78]  Google trained us all to get instant results, search results.
[734.96 --> 736.40]  I think that was like very important.
[736.62 --> 740.70]  And early on, it was like, kind of like challenging because those models were like very slow.
[740.70 --> 744.14]  Our like infrastructure was not very advanced to do that.
[744.24 --> 748.18]  So like you, I remember like very first version, you would have to wait for like three seconds
[748.18 --> 749.76]  or like five seconds to get an answer.
[749.94 --> 754.52]  It was like very slow, but because they were like, it was like such a better experience
[754.52 --> 756.94]  than just like looking at the search results at Google.
[757.08 --> 758.60]  So people still would use it.
[758.60 --> 763.84]  But our ultimate goal was like, okay, so can we be as fast as possible?
[764.00 --> 764.86]  So, yeah.
[764.96 --> 768.30]  So the main differentiator is just, we care a lot about quality.
[768.30 --> 773.54]  So we minimize the chance of things being inaccurate or like hallucinate.
[773.86 --> 776.36]  And we want to do it as fast as possible.
[776.50 --> 780.64]  And so that's, that's kind of like distinguish us from Google because, you know, Google doesn't,
[780.72 --> 781.96]  for example, generate the answers.
[781.96 --> 786.18]  Even though like more recently they started doing this, which is kind of like validated
[786.18 --> 792.52]  our idea and chat GPT probably primarily focuses on like different things, you know, but I
[792.52 --> 796.04]  guess also more recently they started doing a web search as well.
[809.24 --> 810.12]  What's up friends?
[810.32 --> 811.42]  I love MacBlaze.
[811.42 --> 813.10]  I'm happy to have them as a sponsor.
[813.50 --> 817.62]  Backblaze makes backing up and accessing your data astonishingly easy.
[818.08 --> 820.36]  This is a service I personally use.
[820.48 --> 823.62]  Go to backblaze.com slash practical AI.
[823.90 --> 829.80]  You get unlimited cloud backups for Macs, PCs, businesses for just $99 a year.
[830.10 --> 834.48]  You can easily protect business data through a centrally managed admin, protect all the
[834.48 --> 839.58]  data on your machines automatically, easily deploy across multiple workstations with various
[839.58 --> 840.64]  deployment options.
[840.64 --> 846.18]  You can add on enterprise control, including granular access permissions, advanced single
[846.18 --> 849.44]  sign on group management controls and compliance support.
[849.44 --> 856.14]  They even offer multiple restore options, including rapid recovery in the event of data loss or ransomware.
[856.14 --> 856.78]  That sucks.
[856.78 --> 862.98]  You can access your backed up data from anywhere in the world using their web app or their iOS or Android app.
[863.34 --> 864.94]  You can even restore by mail.
[864.94 --> 868.58]  They'll give you a hard drive with all your data shipped to your door.
[868.58 --> 873.62]  You buy a hard drive restore, send the hard drive back within 30 days and get a full refund.
[873.62 --> 876.62]  You can get one year file retention and version history.
[876.82 --> 881.48]  Over 55 billion with a B files restored for customers so far.
[881.78 --> 887.10]  Visit backblaze.com slash practically I so they know where you came from and continue to support the show.
[887.10 --> 900.52]  This is a service obviously recommended by me, but also by New York Times, Inc. Magazine, Macworld, PCworld, LifeWire, Wired, Tom's Guide, 9to5Mac, and just so many more.
[901.06 --> 908.08]  You receive a fully featured or no risk trial at backblaze.com slash practical AI.
[908.08 --> 910.10]  Again, there's support in the show.
[910.52 --> 911.50]  Go there, play with it.
[911.76 --> 914.14]  Start protecting yourself from potential bad times.
[914.14 --> 915.10]  Start today.
[938.08 --> 941.10]  So you mentioned a few things there.
[941.24 --> 942.92]  You mentioned web search.
[943.08 --> 944.54]  You mentioned retrieval.
[944.68 --> 946.02]  You mentioned the large language model.
[946.22 --> 960.12]  So at least in kind of how I think about it and maybe others categorize it differently, there's one element of information that you can get from an LLM, which is I'm going to put in a prompt and it's going to generate text.
[960.12 --> 967.04]  And that may contain some facts or made up facts or some text, but it may be informational, right?
[967.04 --> 971.00]  So there's some sort of knowledge that can be gained there.
[971.54 --> 978.44]  And then in a second case, there's a way to retrieve on the fly external data.
[979.06 --> 981.00]  So that could be like from your company's documents.
[981.00 --> 987.16]  It could be from the web, whatever, and then inject that into prompts into the model, which kind of grounds it.
[987.28 --> 989.66]  And like you say, would give you a citation.
[989.66 --> 1012.02]  There's also, you know, more agentic approaches to this where maybe there's multiple ways that you could get knowledge, maybe doing a web search or searching a certain database that you have access to or any handful of sources that you've kind of curated as tools and you call them in a more automated way.
[1012.02 --> 1022.94]  So I'm wondering from your perspective, obviously, you are part of a team that have been exploring this very deeply from very early on, like you say, when these models made that jump.
[1022.94 --> 1034.58]  From your perspective now, both in terms of what you're building with perplexity and also kind of how you generally see the ability to get accurate information from these models.
[1034.72 --> 1043.60]  How do you view those kind of categories in terms of their utility and what you're relying on for the accuracy element specifically?
[1043.60 --> 1051.52]  The way I see it's going to unfold, I think the tools and sort of like agentic behaviors, I think that's where it's going.
[1051.68 --> 1062.78]  I think it's going to be the main bottleneck for this right now is just like models not smart enough yet to take into account and sort of like reason all of the information that is out there.
[1063.00 --> 1065.98]  But I think it's going to be like a main component.
[1066.12 --> 1067.24]  So there's going to be like models.
[1067.46 --> 1069.42]  They're like very powerful already right now.
[1069.42 --> 1072.78]  They're like trained on a lot of data, like basically internet.
[1072.78 --> 1081.32]  They have a lot of internal information, internal knowledge, and they can do like already like very good job of synthesizing information.
[1081.82 --> 1088.34]  There's like certain things that they don't do well and perhaps they never going to do well.
[1088.52 --> 1099.02]  Those things like, for example, like, you know, like computation, like when you need to do like some, maybe around like some code or like do like some sophisticated like math computations.
[1099.02 --> 1105.80]  Like did the LLM architecture or like transformers is like going to struggle at that.
[1106.52 --> 1112.82]  Also, you know, because those models are like so big, sometimes it's going to be very expensive to them update very frequently.
[1112.82 --> 1120.78]  So you need a way to ingest something, some new information that just like happened and it's still not part of the LLM weights.
[1121.24 --> 1124.58]  You have a way to, and this is what we sort of like specialized.
[1124.58 --> 1127.92]  Also some private documents, as you mentioned, right?
[1127.98 --> 1134.52]  So sometimes if it's like enterprise, you know, you have some of the documents that obviously the model was not trained on.
[1134.68 --> 1137.96]  And you kind of like maybe want to reason about those documents, right?
[1138.04 --> 1141.34]  So, and there's like all kinds of other tools that you can, yeah.
[1141.66 --> 1144.18]  Eventually there is going to be like agents that is going to do like actions.
[1144.28 --> 1148.52]  Maybe you're going to like book a ticket, like buy a ticket or something like that and stuff like that.
[1148.52 --> 1152.66]  So I think it definitely where it's going, it's going to be like a synergy.
[1153.10 --> 1154.64]  Everything's going to come together.
[1155.18 --> 1160.94]  We just need a top level, powerful model that's going to kind of reason behind multiple things.
[1160.94 --> 1166.58]  And we'll have to need to have like long context windows, maybe like some memory as well.
[1166.70 --> 1170.40]  And then, you know, just like utilize those tools as much as possible.
[1170.72 --> 1172.78]  How we have perplexed to thinking about it.
[1172.86 --> 1177.10]  We are like, okay, so, and there's like multiple ways and multiple sort of like applications,
[1177.10 --> 1179.86]  multiple use cases of this general approach.
[1180.04 --> 1185.60]  We are primarily focusing on the information retrieval part of it.
[1185.70 --> 1190.90]  So kind of like initially web, web is the main component because there's like lots of things
[1190.90 --> 1198.54]  to instruct from web, but also we're thinking about how to integrate a new different data sources.
[1198.94 --> 1204.62]  Maybe like some of the different databases, maybe there's like some more complicated or like
[1204.62 --> 1207.92]  more specialized documents, like, you know, maybe there's like PDFs or something like that,
[1207.96 --> 1211.06]  or like some financial data, things like that.
[1211.52 --> 1218.46]  The other aspect that I'm very excited about and we're working on is kind of do, you know,
[1218.50 --> 1222.68]  right now we can answer, we can do like a great job of answering like complicated questions
[1222.68 --> 1228.44]  that you can get answers on Google, but like still not something where you can ask expert
[1228.44 --> 1230.06]  and then can get an answer, right?
[1230.06 --> 1234.24]  Like what if I have like a question that is just like requires like multi-step of reasoning.
[1234.24 --> 1238.94]  So it requires like, okay, like searching web multiple times, analyzing information during
[1238.94 --> 1241.78]  the issue retrieval and then like maybe refining the search.
[1242.08 --> 1248.00]  So kind of like those things that may be going to take some time, but like if you do it yourself,
[1248.08 --> 1249.62]  you would spend like, let's say like an hour.
[1249.90 --> 1254.06]  So here maybe the system would spend like 30 seconds and it's going to save you a bunch of
[1254.06 --> 1254.28]  time.
[1254.34 --> 1258.74]  So kind of like those use cases that can answer like very complicated questions.
[1258.74 --> 1261.94]  And we believe that there is a world for those type of questions.
[1262.48 --> 1263.92]  Technology like this is going to be useful.
[1264.52 --> 1268.94]  As people are using, you know, an answer engine like yours more and more often going forward.
[1268.94 --> 1273.86]  And you kind of alluded a moment ago to, to the fact that, you know, LLMs are not the,
[1273.86 --> 1277.84]  the be all, you know, there are things they don't do well, like, like mathematics and such
[1277.84 --> 1281.76]  and, and a variety of other things I'm sure that we could all throw out there, but they're
[1281.76 --> 1283.26]  really powerful at what they do.
[1283.26 --> 1289.58]  But clearly there is a place and a need for both the LLMs, you know, these largest models
[1289.58 --> 1294.20]  that get all the, they kind of suck up all the air in the news cycles, as well as many
[1294.20 --> 1298.96]  smaller models that are specialized, you know, a mathematics model that, you know, that you
[1298.96 --> 1299.62]  plug in.
[1300.08 --> 1306.20]  As we're looking at trying to, to use answer engines to retrieve information and that information
[1306.20 --> 1310.20]  is increasingly multimodal in nature in terms of what you're asking.
[1310.20 --> 1313.24]  How does the architectures of those come together?
[1313.80 --> 1315.12]  This is a space.
[1315.40 --> 1318.52]  It's not the first time we've asked it here, but it's evolving so rapidly.
[1318.88 --> 1320.82]  We're no longer hosting a model.
[1320.96 --> 1325.42]  You're now hosting a whole collection and they may be mixed with models that you're APIing
[1325.42 --> 1326.60]  out to and such.
[1326.80 --> 1330.62]  How does that look to you as you're building this company at this point?
[1331.02 --> 1336.16]  It's going to be always like trade-off between like, if you have like one powerful model,
[1336.16 --> 1342.54]  I mean, yes, it can do like lots of general things like super well, but like it's going
[1342.54 --> 1343.18]  to be slower.
[1343.56 --> 1344.78]  It's going to be more expensive.
[1345.52 --> 1349.50]  One of our like key principle is just like, we want to do things very fast.
[1349.50 --> 1351.84]  So we can get like that answers as fast as possible.
[1351.84 --> 1358.06]  That means you have to design your system, like orchestration system in a way where certain
[1358.06 --> 1361.44]  things will have to rely on like customized models.
[1361.44 --> 1366.72]  Like something that is much smaller, much faster, but it knows it's like a specialist
[1366.72 --> 1367.12]  model.
[1367.24 --> 1370.78]  So it's not a model that like knows how to do everything, but it knows how to do like
[1370.78 --> 1371.32]  one task.
[1372.04 --> 1378.30]  And basically the challenge here is like, how do you balance between this like general
[1378.30 --> 1381.04]  models and this like a specialist models?
[1381.16 --> 1384.66]  And I think we've, we've been doing this like from the very beginning.
[1384.66 --> 1388.30]  So like when you send the request to perplexity, it's just like not one model.
[1388.30 --> 1393.36]  There is like, I don't know, at least like 10 different models trying to do lots of things
[1393.36 --> 1394.44]  with your request.
[1394.80 --> 1399.14]  It's like all kinds of like ranking models, bunch of like embeddings, all different like
[1399.14 --> 1400.82]  classifiers and stuff like that.
[1401.16 --> 1404.90]  And like the other trade-off here is just like, it was general model.
[1405.12 --> 1411.12]  Let's see one of the big, and I think it was like actually very critical component of why
[1411.12 --> 1416.42]  like company like perplexity in the first place became possible is it's like the speed of
[1416.42 --> 1421.28]  iteration, like you literally can change the prompt and you can just get a new product,
[1421.36 --> 1423.20]  like in a matter of like hours.
[1423.34 --> 1427.82]  Like imagine a couple of years ago, if you wanted to build something like, you know, perplexity
[1427.82 --> 1432.60]  or like whatever other like Gen AI product, you have to collect data first, have to train
[1432.60 --> 1435.78]  the model, launch the product, see if this product makes sense.
[1435.86 --> 1437.16]  Does it have market fit or not?
[1437.22 --> 1441.80]  If it has market fit, then you like start collecting data and then, and then you just
[1441.80 --> 1442.60]  like keep improving.
[1443.32 --> 1449.30]  So what being possible is GPT models, like an API is just like this kind of like flipped
[1449.30 --> 1449.60]  over.
[1449.76 --> 1455.48]  So you very quickly can build a product, see if there is any signs of life for this product.
[1455.48 --> 1459.56]  And then you start collecting data, which is, I think, honestly, the most important thing.
[1459.66 --> 1462.12]  And once you collect data, you can like distill it.
[1462.18 --> 1467.02]  You can build like many other like smaller models and kind of like optimize the experience.
[1467.12 --> 1468.60]  So you can make the models faster.
[1468.70 --> 1469.98]  You can specialize them.
[1469.98 --> 1471.18]  I think this is the key.
[1471.30 --> 1476.18]  I think this is the, honestly, it was like one of the most fundamental changes in the
[1476.18 --> 1476.62]  development.
[1477.82 --> 1482.86]  And, and we kind of like took advantage of, of this thing like early on and then still
[1482.86 --> 1485.00]  using, but it's still tricky.
[1485.00 --> 1488.68]  Kind of like imagine like every time you have this like specialized models and you have like,
[1488.76 --> 1494.16]  if you have tons of them, you have to then like treat each model, like care about each
[1494.16 --> 1494.70]  model separately.
[1494.84 --> 1497.98]  So if you want to like retrain this model, so you have to spend some time on it.
[1497.98 --> 1500.12]  So you have to like evaluate it.
[1500.18 --> 1503.10]  So it becomes more difficult to manage.
[1503.46 --> 1507.04]  But on the other hand, you know, you have some great benefits.
[1507.04 --> 1511.00]  So the key is just like, you don't want to go like too overboard with those models.
[1511.00 --> 1516.42]  Like everything is on like customized models, but also you also clearly don't want to have
[1516.42 --> 1518.10]  just like one model that's going to do everything.
[1518.10 --> 1523.12]  So, yeah, I have a question maybe related to that, which I think is a pain point.
[1523.26 --> 1529.40]  A lot of people are feeling, and I'm, I'm guessing your teams have felt, which you even mentioned
[1529.40 --> 1534.18]  this, like you, you can have, make a small change in your prompt or create a new prompt.
[1534.18 --> 1538.84]  And all of a sudden it's almost like you have a new product, which is sort of like amazing
[1538.84 --> 1542.16]  in, in one sense and really frustrating in another sense.
[1542.16 --> 1547.84]  Cause as you were just alluding to, it's like, Oh, maybe I have these like 17 different
[1547.84 --> 1552.30]  things chained together and they all have prompts that I've worked really hard on.
[1552.54 --> 1557.86]  And then like tomorrow, you know, llama 17 comes out or, or something.
[1557.86 --> 1564.16]  And now like it behaves, it has a different character of behavior than the previous model
[1564.16 --> 1565.06]  that I was using.
[1565.06 --> 1568.40]  I'd love to use it, but now I have all of this.
[1568.62 --> 1573.42]  It's almost like AI model debt that I've, that I've got in my system.
[1573.54 --> 1580.36]  Do you have any perspective on that or any, anything that sort of has happened in your
[1580.36 --> 1581.54]  experience in this regard?
[1582.10 --> 1582.22]  Yeah.
[1582.30 --> 1582.42]  Yeah.
[1582.42 --> 1586.96]  This is clearly been a, been a thing and it's been happening quite often.
[1586.96 --> 1591.52]  And if I would guess that's going to continue happening, one thing to be like realized early
[1591.52 --> 1593.42]  on is, okay, so this is going to be the case.
[1593.42 --> 1598.64]  There is going to be like, there is not going to be like one model that, uh, rules them all.
[1598.64 --> 1602.52]  I mean, even though like for some time it was like GPT-4, but like now we can see there's
[1602.52 --> 1608.20]  like particular like anthropic, you know, Gemini, like llama, there is like going to be a future
[1608.20 --> 1610.36]  where there's a several frontier models.
[1610.54 --> 1610.86]  Right.
[1611.28 --> 1617.10]  Because of that, we decided, okay, so like let's design our infrastructure and our system
[1617.10 --> 1619.80]  in such a way that it's going to be model agnostic.
[1620.06 --> 1620.34]  Right.
[1620.34 --> 1625.72]  So, and then that means, okay, so there's like a ways where you can evaluate each component
[1625.72 --> 1626.72]  independently.
[1627.30 --> 1632.50]  There is a way where you can quickly, um, change things up to adapt for like a new model
[1632.50 --> 1633.96]  and stuff like that.
[1633.96 --> 1638.48]  And that's, uh, it took some time to get there, but it's, I feel like it was like very correct
[1638.48 --> 1639.32]  decision for us.
[1639.32 --> 1644.86]  And then, so for example, one of the advantage we have over, let's say like, um, things like
[1644.86 --> 1650.60]  chat GPT or like load or like basically one model providers companies is just like, we can
[1650.84 --> 1653.04]  seamlessly integrate many different models.
[1653.04 --> 1657.92]  And like our users can like, okay, decide this is the, they want to use this model or they, they
[1657.92 --> 1659.00]  wouldn't do that more.
[1659.00 --> 1665.72]  Like later on as we progress, I think we can even like decide based on the complexity of the query
[1665.72 --> 1670.24]  or like the type of the query we can like route to like a particular model that does the better
[1670.24 --> 1671.98]  job for those type of queries.
[1671.98 --> 1676.34]  And like, you know, minimize like maybe like some of the queries, uh, super simple.
[1676.34 --> 1679.72]  You don't need to run like a very large model for those like to answer.
[1679.72 --> 1683.26]  So then you can like, uh, can optimize speed and things like that.
[1683.26 --> 1688.70]  So I feel like you have to just make a system in a way where it's like agnostic to the model.
[1698.70 --> 1699.90]  What's up friends?
[1700.04 --> 1705.98]  Have you ever had trouble accessing that favorite sporting event or that awesome show or that
[1705.98 --> 1709.04]  film even because it's not in your region?
[1709.04 --> 1715.66]  Well, our friends at NordVPN can help you switch to a virtual location to a country where it is
[1715.66 --> 1718.72]  available, unlocking a world of entertainment.
[1719.08 --> 1720.62]  Plus it's not just about streaming.
[1720.92 --> 1725.76]  It's your go-to for online security, protect your bank details, your passwords, and your
[1725.76 --> 1727.18]  entire online identity.
[1727.40 --> 1731.18]  If you're traveling, they can shield your data on public wifi, keeping you safe.
[1731.28 --> 1735.48]  No matter where you're at, they also have this cool feature called threat protection.
[1735.48 --> 1741.82]  That means you can say goodbye to viruses, malware, and phishing sites because NordVPN will protect
[1741.82 --> 1743.38]  you no matter where you're at.
[1743.70 --> 1749.18]  And one of the fastest VPNs globally, they ensure no buffering while streaming and no stops
[1749.18 --> 1751.00]  for your ISP from bandwidth rattling.
[1751.46 --> 1753.10]  It might sound costly, but think again.
[1753.76 --> 1756.90]  NordVPN costs less than a cup of coffee a month.
[1756.90 --> 1763.96]  And you can use one account on up to six devices to get the best discount off your NordVPN plan.
[1764.24 --> 1769.34]  Go to nordvpn.com slash practical AI.
[1769.86 --> 1774.58]  Our link will also give you four extra months on the two-year plan.
[1775.02 --> 1778.30]  There's no risk with our 30-day money-back guarantee.
[1778.30 --> 1784.34]  Once again, go to nordvpn.com slash practical AI.
[1798.74 --> 1803.80]  So to follow up on what we were talking about before the break there, I know that you were
[1803.80 --> 1809.44]  talking about really building around model agnosticism to be able to handle that.
[1809.66 --> 1815.02]  I couldn't help but wonder, occasionally as we get a new model out, it breaks new ground
[1815.02 --> 1819.30]  on modality, you know, being added in, a whole new approach, that kind of thing.
[1819.92 --> 1826.42]  And so how do you, as a business builder who is having to try to accommodate all these different
[1826.42 --> 1833.78]  models, when you have one that jumps out and has a completely new thing added in that was unexpected
[1833.78 --> 1839.02]  prior to the announcement, how do you, in the organization, how do you guys kind of pivot to
[1839.02 --> 1845.46]  accommodate that and keep that, the agnosticism and yet provide that extra, you know, functionality
[1845.46 --> 1846.40]  that's now available?
[1846.56 --> 1847.56]  How do y'all tackle that problem?
[1847.90 --> 1853.58]  The most important thing to be is to not be caught off guard and try to anticipate what's
[1853.58 --> 1854.18]  going to happen.
[1854.18 --> 1856.28]  I think that's very important.
[1856.46 --> 1860.90]  And it's kind of like, for the most part, I wouldn't say it was like too hard to predict
[1860.90 --> 1861.66]  what's going to happen.
[1862.40 --> 1866.92]  But after that, I think it's primarily like product decision, right?
[1867.00 --> 1870.68]  So like, do you, does this new feature benefit your product or not?
[1870.78 --> 1873.22]  Do we want to like build something in product or not?
[1873.26 --> 1877.70]  So for example, one great example was image upload and kind of like multimodality, right?
[1877.74 --> 1882.08]  So we knew, it was like last year, we like knew for sure that this is going to happen at some
[1882.08 --> 1886.44]  point because I mean, there was like already like some smaller models that kind of like
[1886.44 --> 1887.18]  supporting that.
[1887.66 --> 1891.20]  We knew that, you know, much better models going to come out.
[1891.76 --> 1896.56]  And then because of that, we kind of like in advance start first of all, like understood
[1896.56 --> 1898.80]  like, okay, so this is going to be important for our project.
[1898.80 --> 1902.14]  So we can support like this and this and that, those use cases.
[1902.14 --> 1907.12]  And we decided to build infrastructure in advance and kind of like anticipated, obviously,
[1907.32 --> 1912.48]  we didn't fully like predict like how exactly it's going to operate, but it was like very
[1912.48 --> 1912.84]  close.
[1912.92 --> 1915.40]  So it was like required like little, like couple of days to adjust.
[1916.08 --> 1921.52]  And then we were like one of the, you know, very quickly can release it as a product.
[1921.64 --> 1927.70]  So it's having the system that are kind of general enough that can like support those like
[1927.70 --> 1928.44]  new modalities.
[1928.60 --> 1929.56]  It's very important.
[1930.10 --> 1935.46]  Get some great deal of anticipation, but also, you know, like sometimes, you know, like
[1935.46 --> 1938.50]  certain features that maybe come out, maybe they're like not useful for your product.
[1938.60 --> 1942.40]  You don't, you also don't want to like put everything into, okay, so like this is a cool
[1942.40 --> 1942.68]  feature.
[1942.68 --> 1944.12]  Let me just add it to your product.
[1944.12 --> 1947.16]  So like that, that's always not, not that great idea in general.
[1947.28 --> 1949.30]  So only things that make sense.
[1949.34 --> 1953.86]  And if, if those things makes sense for your product, you likely already like thought about
[1953.86 --> 1956.06]  like, how do you, how would you implement them in advance?
[1956.06 --> 1957.72]  So it's just like makes it a bit easier.
[1958.36 --> 1962.20]  While you were talking, I was thinking there's, there's sort of one axes that you have to navigate
[1962.20 --> 1967.22]  here around model releases and functionality and modalities, all of that stuff.
[1967.44 --> 1972.46]  There's sort of another, maybe around UI and user experience.
[1972.46 --> 1978.08]  I is sort of multiple people making the comment, oh, well, like the chat interface came out with
[1978.08 --> 1978.72]  chat GPT.
[1978.84 --> 1981.56]  So everyone's sort of like focused around the chat interface.
[1981.56 --> 1988.06]  Is that the best way to utilize this sort of technology in the long run?
[1988.22 --> 1995.34]  There's probably a lot of exploration that's still open around UI and user experience with
[1995.34 --> 1996.80]  this type of technology.
[1996.80 --> 2001.74]  And certainly chat is, is relevant and you know, we're using it a lot already.
[2001.74 --> 2008.02]  I'm wondering from your perspective, especially as we see this functionality, maybe more embedded
[2008.02 --> 2015.00]  in the physical world around that, whether that be like in our glasses with, with meta glasses
[2015.00 --> 2022.76]  or in like kiosks in airports or whatever, whatever those things are, what is your perspective
[2022.76 --> 2030.84]  on how important it is to explore new types of, of, of UI or user experience with this technology?
[2030.84 --> 2036.66]  I believe like, and I mean, we, we kind of like, we're like very confident early on.
[2036.72 --> 2039.50]  It's just like chat interfaces is a temporary thing.
[2039.62 --> 2040.88]  It's just too limiting.
[2041.24 --> 2042.38]  It has like a lot of constraints.
[2042.38 --> 2047.12]  And that's why like, you know, we didn't follow the usual route.
[2047.18 --> 2049.10]  Like it was all of the like chat boards.
[2049.16 --> 2053.02]  They were like literally copied chat, chat GPT and kind of like, okay, so put like chat
[2053.02 --> 2053.42]  interface.
[2053.54 --> 2057.20]  We kind of like thought a little bit more about this and we designed it.
[2057.20 --> 2061.26]  I feel like ultimately right now we're still in this like early stage where like people
[2061.26 --> 2063.02]  care about the model itself, you know?
[2063.02 --> 2067.42]  So like the model is the thing, but as this thing, they get more advanced, like as more
[2067.42 --> 2071.62]  people start using Gen AI products, I feel like the main thing is going to be product
[2071.62 --> 2071.98]  itself.
[2071.98 --> 2073.96]  Like what kind of things can product do?
[2074.52 --> 2076.38]  Do you do it like better than this?
[2076.42 --> 2077.38]  Do you have like the best UI?
[2077.46 --> 2078.46]  Do you have the best UX?
[2078.46 --> 2082.54]  And that's why we kind of like early on was like been thinking about those things and
[2082.54 --> 2089.40]  we kind of design our product in a way that is the most least suitable for the things that
[2089.40 --> 2090.24]  we wanted to do.
[2090.40 --> 2090.52]  Right.
[2090.54 --> 2092.34]  So if it's like searches, like it doesn't make sense.
[2092.40 --> 2095.24]  We knew that like chat doesn't make sense for search.
[2095.76 --> 2098.16]  It's just like, that's not how people search for information.
[2098.58 --> 2102.70]  That was like a very big factor, I think in our success.
[2102.70 --> 2109.00]  Um, the other thing, I guess we also, even like last year we start like prototyping and
[2109.00 --> 2112.72]  experimenting with this like a concept of a generative UI.
[2113.30 --> 2118.96]  So something where LLM can guide like what kind of like UI elements you can generate.
[2118.96 --> 2122.80]  And then like, sometimes, you know, like one of the things in chat interface, like if you
[2122.80 --> 2126.94]  want to ask like a follow-up question, sometimes it doesn't make sense to, you know, ask it as
[2126.94 --> 2127.72]  a sentence, right?
[2127.76 --> 2132.64]  So maybe you want to like show like a checkbox or like a button or whatever, like.
[2133.06 --> 2136.82]  If there's like a, it's just like a special on the mobile, like everybody uses phones,
[2136.90 --> 2137.08]  right?
[2137.10 --> 2141.88]  It's just like not very convenient to type, especially if you're on the run.
[2141.96 --> 2143.24]  So you would rather like press a button.
[2143.34 --> 2148.46]  That's why like maybe a speech and I guess like voice technology is going to be one of
[2148.46 --> 2151.12]  the interesting modalities for sure.
[2151.12 --> 2156.04]  I feel like an interesting interface because it's kind of, uh, it has a lot of, uh, advantages.
[2156.26 --> 2160.86]  Obviously it has like lots of disadvantages too, but, uh, uh, definitely going to be interesting.
[2160.86 --> 2166.20]  And I think like going forward, as we go towards like agentic behaviors and like more things
[2166.20 --> 2170.88]  going to become possible, I think it's definitely not going to be like chat interface.
[2171.12 --> 2172.40]  It's has to be something else.
[2172.94 --> 2174.62]  I'm really fascinated by this topic.
[2174.62 --> 2179.18]  Again, it's, I think something that, that, uh, both Daniel and I have some passion for
[2179.18 --> 2181.20]  and just in, you know, daily use and stuff.
[2181.76 --> 2185.94]  I'm, I'm wondering with you thinking about that kind of productization, do you think that's
[2185.94 --> 2192.00]  something that perplexity engages in, in a direct way or supports other companies, uh,
[2192.00 --> 2192.52]  through that?
[2192.52 --> 2199.82]  And then there are so many times in the course of a typical day where I'm wishing I had other
[2199.82 --> 2203.54]  ways of interfacing, uh, with these capabilities that we're talking about.
[2203.68 --> 2206.12]  And I'll give you just a, just a trite example.
[2206.28 --> 2209.88]  I, I will take my dog for a walk at a nearby park every day.
[2209.88 --> 2211.40]  And that's my thinking time.
[2211.70 --> 2215.08]  That's where I'm really trying to be creative and I'm walking and I have to keep walking.
[2215.38 --> 2216.78]  You know, I don't want to stand right now.
[2216.84 --> 2221.22]  I have to, I stop and I pull out my phone and it's frustrating and people are going by me and
[2221.22 --> 2224.16]  I'm trying to hold my dog and, but I want this experience.
[2224.16 --> 2229.46]  It might be while driving, might be while walking the dog where this seamless way of
[2229.46 --> 2233.24]  utilizing these capabilities that we've grown accustomed to come about.
[2233.38 --> 2240.24]  Are you a, how do you see yourselves being part of that next journey on the interface side?
[2240.48 --> 2244.44]  And B, um, do you have any ideas on how to get there?
[2244.48 --> 2246.60]  It's just, uh, that's the next thing I want.
[2246.98 --> 2251.16]  Definitely looking into this, I think, uh, and we consider like multiple options.
[2251.22 --> 2255.72]  It's either like certain things I think we can do ourselves for certain other, like things.
[2255.72 --> 2258.20]  We probably have to work with some, some other like partners.
[2258.20 --> 2263.60]  Cause I mean, yeah, but I, I truly share your, um, kind of like experience.
[2263.60 --> 2267.34]  And I think it's, yeah, it's just like, if you sit in front of a computer, I think they
[2267.34 --> 2270.26]  are the, by far the best interface is a keyboard.
[2270.54 --> 2272.16]  I don't think you can do better than that.
[2272.50 --> 2276.48]  But, uh, yeah, if you are, you know, occupied with something else, if you're driving a car,
[2276.54 --> 2278.50]  maybe you're walking you, there has to be something else.
[2278.50 --> 2280.88]  Like even like phone is, you know, it's, it's okay.
[2280.88 --> 2285.54]  Maybe like even like taking notes, maybe you like say a command and something like that,
[2285.54 --> 2291.92]  but when you get the voice back, that's already like something, but it misses like visual information.
[2292.16 --> 2293.72]  So you kind of like want to add that.
[2293.82 --> 2297.72]  So that, that means you probably have to have some sort of like glasses on.
[2297.72 --> 2302.32]  I think it's, it will definitely happen and we, we will try it.
[2302.36 --> 2302.94]  We, for sure.
[2303.00 --> 2310.50]  We like, we spend a lot of time this year improving our mobile app to do a voice to voice and we
[2310.50 --> 2312.52]  can like invest it a lot into like voice generation.
[2312.68 --> 2317.76]  So for example, uh, you can, yeah, ask like various questions and like, you know, like if
[2317.76 --> 2321.86]  you, if you need something quick, like you walk in, you like, I want to have like a quick,
[2321.86 --> 2323.36]  uh, lookup of information.
[2323.36 --> 2330.46]  So we support that there is something, for example, for if you drive a car, we have this, uh, uh,
[2330.46 --> 2335.22]  you can read up like the stories or like discover, uh, from, from perplexity.
[2335.28 --> 2337.24]  That's also like, uh, AI generated voice.
[2337.24 --> 2342.24]  So it's kind of like you listen to a podcast or like, uh, uh, so that's super important.
[2342.42 --> 2342.86]  Yeah.
[2342.90 --> 2344.20]  I think that the next step is vision.
[2344.20 --> 2345.96]  And so like, how do you get there?
[2346.60 --> 2350.76]  Maybe one challenge that I've been thinking about this entire time while we've been talking
[2350.76 --> 2357.92]  relates to definitely a danger that I think people have identified as related to this new
[2357.92 --> 2362.58]  technology, which is you've already mentioned that you're kind of doing web retrieval or
[2362.58 --> 2368.82]  retrieval from certain sources as kind of a primary way of grounding answers of ensuring,
[2368.82 --> 2371.28]  um, accuracy of citations.
[2371.38 --> 2376.16]  But I know a lot of people are concerned about and thinking about this sort of idea of data
[2376.16 --> 2381.98]  poisoning where we're putting out actually a lot of generated content on the web, right?
[2382.08 --> 2387.24]  And that proportion of human and generated content is going to change over time, which
[2387.24 --> 2392.34]  means even for retrieval systems, especially if you're doing web related searches, there's
[2392.34 --> 2397.38]  a potential that you could retrieve generated content itself and get in this kind of weird
[2397.38 --> 2397.74]  loop.
[2397.92 --> 2401.30]  Of course, there's a separate problem for like the models and how they're training.
[2401.30 --> 2407.32]  And I mean, this affects a lot of different areas, but I know probably you, you've been
[2407.32 --> 2413.78]  doing a lot of thinking about this because it's kind of key to how you operate as a system.
[2413.90 --> 2418.66]  Any perspective on that, that you feel like people should keep in mind kind of moving forward
[2418.66 --> 2424.58]  or things that you're thinking about in terms of whether that's data curation or validation,
[2424.58 --> 2431.06]  or I know a lot of people are talking about detecting generated content and that's maybe
[2431.06 --> 2431.62]  hit or miss.
[2431.74 --> 2436.42]  So there's all of this kind of connected stuff, but generally around this idea of data poisoning
[2436.42 --> 2438.54]  or generated content on the web.
[2438.66 --> 2439.22]  Any thoughts?
[2439.74 --> 2442.64]  To me, it's, uh, it's kind of like a technological problem.
[2442.64 --> 2447.86]  I feel like it's very reminiscent of, uh, um, like spam classifiers, right?
[2447.86 --> 2452.26]  Like it just, uh, like whole not another level or like, but let's say like 20 years ago
[2452.26 --> 2456.86]  when you like receive emails, yeah, you, you would receive like a lot of spam and then
[2456.86 --> 2459.46]  eventually people develop technology that can like detect it.
[2459.66 --> 2462.56]  I feel like something like this will happen.
[2462.74 --> 2466.96]  So it's always going to be like a constant battle, like the, between like generators and
[2466.96 --> 2467.68]  discriminators.
[2468.18 --> 2471.44]  So, uh, at some point, like generators, maybe it's going to be better.
[2471.62 --> 2472.72]  It's like fighting malware.
[2473.04 --> 2473.90]  Yeah, yeah, exactly.
[2474.00 --> 2475.62]  It's, it's the same concept.
[2475.82 --> 2478.64]  Um, it's definitely going to be an issue for sure.
[2478.64 --> 2485.24]  But, uh, my hope is that, and my belief that is the good guys, the good generators
[2485.24 --> 2490.44]  is going to be just like, it's a, from machine learning fundamentals, uh, discrimination is
[2490.44 --> 2491.96]  much easier problem than generation.
[2492.06 --> 2495.82]  It's like much easier to tell what is good, what is not than, uh, than generate it.
[2495.82 --> 2500.56]  So, and usually it seems like we've been more successful in like detecting the stuff and
[2500.56 --> 2504.80]  then, and I don't see any reasons why it's not, um, going to continue.
[2504.80 --> 2511.88]  So, uh, this has been really fascinating as, as we wind up here and have you here for an,
[2511.92 --> 2516.28]  uh, you know, one more question as we, we've talked about the future and have been kind
[2516.28 --> 2520.80]  of, you know, talking about what our expectations might be and how those might be fulfilled.
[2521.16 --> 2525.90]  Are there any other areas, um, that we haven't addressed that you're, that you're interested
[2525.90 --> 2531.84]  in and possibly as, as part of that, any way of kind of summarizing your own vision without
[2531.84 --> 2536.26]  it being just answering questions that Daniel and I have thrown at you, but your own vision
[2536.26 --> 2541.56]  for what the future looks like to you and what you want it to be and what perplexity is
[2541.56 --> 2546.92]  trying to realize it as to kind of paint a picture of what we might see over whatever
[2546.92 --> 2548.52]  timeframe you want to address.
[2548.94 --> 2549.02]  Yeah.
[2549.10 --> 2549.24]  Yeah.
[2549.24 --> 2554.30]  So I'm, I'm, I'm very excited basically to get to a point where, you know, I have a,
[2554.46 --> 2559.16]  any question, any, any problem I want, I want to have, and then just like go to perplexity
[2559.16 --> 2563.72]  and like get an answer or like suggestion or even like perform an action for this.
[2564.26 --> 2569.28]  I already mentioned this thing where, uh, kind of like increasing the quality or like
[2569.28 --> 2574.08]  the complexity of the type of questions you can ask and then making sure that the system
[2574.08 --> 2575.70]  will be able to handle those.
[2575.70 --> 2580.76]  I think this is definitely going to be the future and I think we work hard on that.
[2581.24 --> 2583.34]  It kind of like opens up another dimension.
[2583.34 --> 2588.50]  You know, you can just, uh, you can ask like lots of simple, simpler questions, or you
[2588.50 --> 2591.24]  can just like one have like one hard question.
[2591.32 --> 2594.06]  So it's kind of a, you know, complexity versus quality.
[2594.20 --> 2600.20]  And I think ultimately when you get information, you usually use it for some sort of like decision
[2600.20 --> 2600.54]  making.
[2600.54 --> 2600.90]  Right.
[2600.90 --> 2607.44]  And so if we can then take this information that we've retrieved for you and synthesize
[2607.44 --> 2613.04]  in a form of answer, can we also then, uh, do like some decision making for you and can
[2613.04 --> 2614.82]  you perform actions on your behalf?
[2615.42 --> 2619.16]  So like, imagine, I don't know, like you imagine like you're researching something and maybe
[2619.16 --> 2621.86]  you want to like research to buy like best running shoes.
[2622.12 --> 2622.28]  Right.
[2622.32 --> 2627.16]  So it's a pretty painful procedure right now because, uh, there's like so much stuff in the
[2627.16 --> 2628.70]  internet, like you don't know what you trust.
[2628.70 --> 2631.98]  So that, that's why like, you know, if you identify usually like running shoes, you just
[2631.98 --> 2637.44]  like stick with them forever because it's just, you, you, you trust, but like things
[2637.44 --> 2637.82]  like that.
[2637.82 --> 2643.04]  So imagine if you, somebody will do like this, like research for you, like really nails it
[2643.04 --> 2647.94]  down, like weights, all the pros and cons, and then suggest like, it's like, do you want
[2647.94 --> 2649.62]  to, this is the possible like variance.
[2649.62 --> 2650.88]  Do you want to buy this stuff?
[2650.94 --> 2651.82]  And then you say yes.
[2651.82 --> 2654.22]  And then it goes like automatically buys it for you.
[2654.26 --> 2658.52]  And then like two days later it's delivered and you, you only need to type like questions once.
[2658.52 --> 2661.94]  You don't have to push your credit card in and stuff like that.
[2661.94 --> 2663.52]  And there's like tons of examples.
[2663.52 --> 2668.42]  So kind of, I would say the, the, the future is like, first you would have to make sure
[2668.42 --> 2674.28]  that you can nail, um, sort of like the information retrieval part and kind of like generating the
[2674.28 --> 2675.40]  most useful information.
[2675.70 --> 2677.50]  The next step would be like decision-making.
[2677.50 --> 2682.60]  So like make decision based on this information and then third step to actions.
[2682.60 --> 2686.94]  So that's, uh, that's where I think I would be excited to get to that point.
[2686.94 --> 2687.72]  That's great.
[2687.72 --> 2688.12]  Yeah.
[2688.32 --> 2693.48]  Uh, thank you for being willing to take time to dig into a number of topics that I know,
[2693.62 --> 2699.50]  I know our listeners are exploring themselves and also interested in, and, um, certainly
[2699.50 --> 2702.38]  perplexity has been leading in a lot of these areas.
[2702.38 --> 2707.02]  So, um, keep up the good work and, and thank you for, for the work and the perspective and
[2707.02 --> 2708.26]  taking time to talk.
[2708.34 --> 2708.94]  Appreciate it.
[2708.94 --> 2709.38]  Yeah.
[2709.40 --> 2711.72]  Thanks for the great questions and thanks for having me.
[2719.16 --> 2720.12]  All right.
[2720.38 --> 2722.80]  That is practical AI for this week.
[2723.42 --> 2724.62]  Subscribe now.
[2724.62 --> 2732.02]  If you haven't already head to practical AI.fm for all the ways and join our free Slack team
[2732.02 --> 2736.20]  where you can hang out with Daniel, Chris, and the entire change log community.
[2736.20 --> 2741.42]  Sign up today at practical AI.fm slash community.
[2741.96 --> 2747.76]  Thanks again to our partners at fly.io to our beat freaking residents, break master cylinder,
[2747.76 --> 2748.94]  and to you for listening.
[2749.20 --> 2751.08]  We appreciate you spending time with us.
[2751.38 --> 2752.60]  That's all for now.
[2752.82 --> 2754.54]  We'll talk to you next time.
[2754.54 --> 2756.98]  See what hours of the new week and the future.
[2757.50 --> 2766.66]  Well, now at the top Col
[2766.68 --> 2767.68]  Fine辺 website www.saade朋友.com
