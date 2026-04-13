[0.00 --> 8.64]  Welcome to Practical AI.
[9.04 --> 15.64]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.64 --> 18.44]  are changing the world, this is the show for you.
[18.80 --> 23.88]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[23.88 --> 24.16]  listen.
[24.46 --> 26.30]  Check them out at Fastly.com.
[26.30 --> 31.54]  And to our friends at Fly, deploy your app servers and database close to your users.
[31.96 --> 33.22]  No ops required.
[33.54 --> 35.58]  Learn more at fly.io.
[41.96 --> 43.00]  Well, hello.
[43.20 --> 46.00]  We have a very special episode for you today.
[46.18 --> 51.44]  I got the chance to sit down with the guys from Latent Space, Wix, and Alessio out in
[51.44 --> 52.10]  San Francisco.
[52.10 --> 58.00]  They were kind enough to let me into their podcast recording studio, and we got a chance
[58.00 --> 62.94]  to talk about our favorite episodes of both of our shows and some of the overall takeaways
[62.94 --> 64.80]  we've had from those discussions.
[65.32 --> 70.24]  We cover some of the trends that we've been seeing in AI, and they even get a chance to
[70.24 --> 73.26]  grill me on my opinions about prompt engineering.
[73.56 --> 74.66]  So enjoy the show.
[75.46 --> 76.44]  Hey, everyone.
[76.84 --> 78.38]  Welcome to the Latent Space podcast.
[78.38 --> 82.34]  This is Alessio, partner and CTO in residence at Decibel Partners.
[82.80 --> 86.60]  I'm joined by my co-host, Swix, writer and editor of Latent Space.
[87.02 --> 90.42]  And today, we're very excited to welcome Dan Whitenack to the studio.
[90.56 --> 90.88]  Welcome, Dan.
[91.02 --> 91.92]  What's up, guys?
[91.94 --> 92.74]  It's great to be here.
[93.08 --> 94.48]  This is a podcast crossover.
[94.66 --> 97.38]  If you recognize this voice, Dan is the host of Practical FM.
[97.62 --> 101.72]  He's been in my ear on and off for the past five years, covering the latest and greatest
[101.72 --> 103.24]  in AI before it was cool.
[103.24 --> 104.54]  Yeah, yeah, yeah.
[104.58 --> 110.16]  Before the AI hype back in these weird data science times, whatever that is now.
[110.32 --> 110.62]  Yes.
[110.76 --> 112.18]  Everything is merging and converging.
[112.54 --> 115.84]  So I'll give a little bit of your background, and we can go into a little bit on your personal
[115.84 --> 116.12]  side.
[116.22 --> 119.58]  You got your PhD in mathematical and computational physics.
[120.22 --> 125.58]  And then you spent 10 years as a data scientist, most recently at SIL International, which I
[125.58 --> 127.50]  actually thought it was like an agri-tech thing.
[127.62 --> 128.64]  And then I went to the website.
[128.74 --> 129.76]  It's actually a nonprofit.
[130.10 --> 131.02]  Yeah, it's an international NGO.
[131.02 --> 133.72]  Yeah, so they do language-related work all around the world.
[133.84 --> 139.18]  So I spent the last five years building up a team that's been working on kind of low-resource
[139.18 --> 141.88]  scenarios for AI, if people are familiar with that.
[142.02 --> 146.38]  So doing like machine translation or speech recognition, that sort of thing in languages
[146.38 --> 147.60]  that aren't yet supported.
[147.96 --> 148.14]  Yeah.
[148.44 --> 153.84]  And we'll talk about this later, but I think episode three on Practical AI was already featuring
[153.84 --> 157.02]  the global community that AI has and addresses.
[157.40 --> 158.16]  Yeah, yeah, yeah.
[158.16 --> 162.34]  It's been an important theme throughout the whole time, throughout over 200 episodes.
[162.76 --> 163.48]  Yeah, yeah.
[163.60 --> 168.14]  And you recently left SIL to work on Prediction Guard, which we can talk a little bit more
[168.14 --> 168.52]  about that.
[168.94 --> 173.06]  You are also interim senior operations development director at NT Candle Co.
[173.06 --> 173.50]  Yeah, yeah.
[173.94 --> 176.00]  And yeah, what else should people know about you?
[176.00 --> 183.60]  Yeah, I mean, as probably can be noted from the intro, I love working on various projects
[183.60 --> 185.98]  and having my hands in a lot of things.
[186.20 --> 189.78]  But yeah, I've code on the side for fun.
[189.92 --> 193.20]  And that's how I usually get into these side projects and that sort of thing.
[193.66 --> 196.58]  But outside of that, yeah, I live in Indiana.
[196.82 --> 200.90]  I was telling you guys that I'm trying to coin the term cerebral prairie.
[200.90 --> 203.02]  So we'll see if that catches on.
[203.44 --> 204.26]  Probably not.
[204.60 --> 208.44]  Your second guest in a row from Indiana, Linus from Notion was Indiana.
[208.68 --> 213.24]  They were talking about how there's a surprising number of international students in there.
[213.48 --> 214.50]  Yes, very true.
[214.78 --> 216.02]  Purdue's a strong university.
[216.24 --> 216.60]  Yeah, yeah.
[216.64 --> 217.48]  Very strong university.
[217.62 --> 219.06]  It's a great place to spend time.
[219.26 --> 222.42]  And there's a lot of fun things that happen around that area, too.
[222.42 --> 226.58]  So I'm also very into music, but not any sort of popular music.
[226.96 --> 231.10]  I play like mandolin and banjo and guitar and play folk music.
[231.38 --> 231.70]  Low resource.
[231.98 --> 234.86]  Yeah, low resource music, low resource languages.
[235.16 --> 235.96]  Yeah, all those things.
[236.12 --> 239.18]  Anything low resource is in my territory for sure.
[240.12 --> 241.90]  And maybe we can cover the story of Practical AI.
[242.08 --> 243.56]  How'd you start it?
[243.82 --> 246.32]  Tell us what the early days were like and just fill everyone in.
[246.52 --> 249.26]  Yeah, it was kind of a winding journey.
[249.26 --> 255.98]  Some people might be familiar with the Changelog podcast, which I think they've been going now for like 11 or 12 years.
[256.28 --> 257.82]  It's pretty prolific.
[258.26 --> 260.80]  I think originally around more open source.
[260.96 --> 262.98]  Now it's kind of software development in general.
[263.42 --> 266.38]  But they have a network of podcasts now.
[266.94 --> 269.26]  And at a Go conference, actually.
[269.38 --> 271.52]  So I'm a fan of the Go programming language.
[271.78 --> 272.96]  That's another fun fact.
[273.48 --> 277.74]  But at Go4Con, I think it was in 2016, maybe.
[277.74 --> 281.84]  I met Adam Stachowiak, who is one of the hosts of the Changelog.
[282.20 --> 285.12]  At the time, I was giving a talk about data science something.
[285.40 --> 285.72]  I forget.
[286.20 --> 287.46]  But he kind of pitched me.
[287.58 --> 291.60]  He's like, we've been thinking a lot about doing like a data or data science podcast.
[292.16 --> 294.08]  And at the time he had a name.
[294.14 --> 302.12]  It was like, I think it was hard data or something like that, which never caught on for obvious reasons.
[302.12 --> 303.76]  But I kind of stored that away.
[303.94 --> 305.66]  It didn't really do anything with it.
[305.66 --> 310.64]  But then over the next couple of years, I met Chris Benson, who's my co-host on Practical AI.
[311.44 --> 314.44]  And helped him with a couple of talks at conferences.
[314.44 --> 316.80]  We met through the Go community as well.
[317.38 --> 320.38]  And eventually, he was working at a different company at the time.
[320.46 --> 323.84]  Now he's a strategist with Lockheed Martin, working in AI stuff.
[324.30 --> 329.72]  But he reached out to me and said, hey, would you ever consider doing kind of like a co-host podcast thing?
[329.72 --> 332.68]  And at that point, I remembered my conversation with Adam.
[332.86 --> 334.96]  So I reached back out to Adam with the changelog.
[335.16 --> 337.60]  And then we kind of started working on the idea.
[337.74 --> 339.48]  We wanted it to be practical.
[339.90 --> 345.42]  So at the time, well, there's a lot of people doing things now with AI, like hands on.
[345.58 --> 348.92]  Back then, there were kind of some podcasts that were really hyped AI.
[348.92 --> 352.88]  Like not practical at all, which is why we kind of came to practical AI.
[353.18 --> 355.18]  Something that would actually benefit people.
[355.42 --> 362.68]  And that's like a great thing to hear from people that when they listen to the show, they do actually learn something that's useful for their day-to-day.
[362.84 --> 363.94]  That's kind of the goal.
[364.40 --> 364.50]  Yeah.
[364.90 --> 365.16]  Nice.
[365.26 --> 368.52]  And I think that's one of the things in common with our podcast.
[368.52 --> 375.24]  You know, there's a lot of content out there that can get a lot of clicks with a fear of AI, you know, and all these different things.
[375.38 --> 379.34]  And I think we're all focused on more, yeah, practical and day-to-day usage.
[379.90 --> 380.02]  Yeah.
[380.04 --> 385.00]  Tell us more about PredictionGuard, you know, that kind of fits into making AI practical and usable.
[385.34 --> 385.58]  Yeah.
[385.82 --> 386.04]  Yeah.
[386.10 --> 386.40]  Sure.
[386.62 --> 387.44]  Appreciate that.
[387.86 --> 392.58]  So, yeah, PredictionGuard is what I've been working on since about Christmas time-ish.
[392.92 --> 397.88]  Originally, I was thinking a lot about large language model evaluation and model selection.
[397.88 --> 400.58]  But it's kind of morphed into something else.
[400.74 --> 415.04]  What I've realized is that there's this market pressure, there's internal company pressure for people to implement these kind of generative AI version of models into their workflows because enterprises realize the benefits that they could have.
[415.04 --> 421.02]  But in practice, when they go from like chat GPT, they type in something, it's amazing.
[421.42 --> 428.00]  And then like, how do we do this in our enterprise where we have maybe rules around data privacy or compliance issues?
[428.18 --> 432.84]  And also, like, we want to automate things maybe or we want to do data extraction.
[432.98 --> 436.20]  But I just get like text vomit out of these models.
[436.38 --> 437.28]  Like, what do I do with that?
[437.48 --> 439.18]  In this case, unstructured text.
[439.26 --> 443.36]  How do I build a robust system out of inconsistent text vomit?
[443.36 --> 446.72]  So, PredictionGuard is really focused on those two things.
[446.86 --> 453.18]  One is kind of compliance and running kind of state-of-the-art AI models in a compliant way.
[453.36 --> 459.76]  And then layering on top of that layers of control for structuring output and validating output.
[460.24 --> 464.34]  So, some people might be familiar with projects like guardrails or guidance or these things.
[464.34 --> 468.86]  So, we've integrated kind of some of the best of those things into the platform.
[468.96 --> 477.36]  Plus, some ways to easily do like self-consistency checks and factuality checks and other things on top of large language model output.
[477.62 --> 477.74]  Nice.
[477.86 --> 480.66]  We did have a Shreya Rajpal from GoRails as a guest.
[480.88 --> 480.90]  Yeah.
[481.08 --> 481.24]  Yeah.
[481.34 --> 483.82]  So, yeah, that's another episode that people really like.
[483.82 --> 484.18]  Yeah.
[484.18 --> 489.44]  Maybe, you know, just to give people a sense of what practical AI is as a podcast.
[489.60 --> 493.66]  You want to talk about maybe like the two, three favorite episodes that we have.
[493.68 --> 495.06]  And we can go maybe alternate.
[495.06 --> 495.56]  Back and forth.
[495.64 --> 496.46]  You know, like our favorites.
[496.46 --> 497.80]  We've done some prep for this episode.
[498.12 --> 498.94]  Yes, yes, yeah.
[498.94 --> 507.68]  So, this is kind of like, I think our conception of this is kind of like a review for listeners who are new to us, either of our podcasts, to go back and revisit the favorites.
[507.68 --> 508.54]  Yeah, yeah.
[508.62 --> 514.76]  I think I can talk about some personal favorites of mine and then maybe like favorites from the audience.
[515.16 --> 526.68]  I think some of my personal favorites have actually been, we call them like fully connected episodes where Chris and I actually talk through a subject in detail together without a guest.
[527.22 --> 532.62]  To be honest, those are great episodes just for like me to learn something, like have an excuse to learn something.
[532.62 --> 537.78]  And we've done that recently, like with ChatGPT and instruction tune models.
[537.90 --> 540.56]  We did it with stable diffusion and diffusion models.
[540.88 --> 542.40]  We did it with alpha fold.
[542.64 --> 555.76]  So, all of those are episodes with us two and just talking through like how practically can you like form a mental model for how these models were trained and how they work and what they output.
[556.22 --> 560.00]  Those are some of my favorites just because I learn a lot because I do a little bit of prep.
[560.00 --> 565.90]  We talk through all the details of those and it helps me form my own sort of intuition around those things.
[566.44 --> 571.66]  Another personal favorite for us was that we did a series about AI in Africa.
[571.84 --> 572.72]  That was really cool.
[572.80 --> 574.94]  You mentioned like the global AI community.
[575.22 --> 577.16]  We did actually a series of those.
[577.36 --> 581.32]  They're all labeled AI for Africa, highlighting things like Masakane.
[581.32 --> 591.52]  So, people don't realize that like some of the models that we develop here, like in the West Coast or wherever, they don't work great for all use cases around the world.
[591.58 --> 601.04]  And there's a lot of thriving grassroots communities like Masakane and Turkic Interlingua and other communities that are really building models for themselves.
[601.04 --> 613.16]  Machine translation, speech recognition, models that work for their languages around the world or agriculture, you know, computer vision models that work for their use cases around the world.
[613.26 --> 615.62]  So, those are a couple of highlights on my end.
[616.28 --> 617.86]  Do we go with our personal highlights?
[618.98 --> 619.78]  Yeah, go ahead.
[619.86 --> 620.78]  I think you already picked one out.
[620.78 --> 627.70]  Yeah, I think mine is definitely the episode with Mike Conover from Databricks, who's the person leading the Dahlia first there.
[628.10 --> 631.82]  I think obviously the content is great and Mike is extremely smart and prepared.
[631.94 --> 638.58]  But I think the passion that he had about these things, you know, the red pajama data set came out the morning that we recorded.
[638.84 --> 642.90]  And we're all kind of like nerding out or like, yeah, why is that so interesting?
[643.14 --> 644.74]  Like, he was so excited about it.
[644.74 --> 649.74]  And it's great to see people that have so much excitement about things that they work on.
[649.74 --> 653.48]  You know, it's kind of like an inspiration in a way to do the same for us.
[653.80 --> 661.28]  I think personally, so I tend to drive the news-driven episode ones, like the event-driven ones where something will happen in AI.
[661.68 --> 665.28]  And like, I'll make a snap decision that we'll have an episode recording on Twitter Spaces.
[665.64 --> 667.68]  And we'll have just a bunch of people tune in.
[668.00 --> 672.98]  I think the one that stood out was the Chat2PT app store, the Chat2PT plugins release.
[673.20 --> 673.56]  Oh, yeah.
[673.58 --> 675.54]  Where like 4,000 people tuned in to that one.
[675.84 --> 676.32]  That's crazy.
[676.36 --> 678.80]  And we did like an hour of prep, right?
[678.80 --> 687.92]  And I think it's important for me as a quote-unquote journalist to be the first to report on something major and to provide a perspective on something major.
[688.12 --> 691.88]  But also capture an audio history of how people react at the time.
[692.36 --> 694.68]  Because this is something that we're talking about in the prep.
[695.06 --> 699.38]  Chat2PT plugins have become a disappointment compared to our expectations then.
[699.44 --> 700.28]  But we captured it.
[700.34 --> 702.62]  We captured the excitement back then.
[702.62 --> 708.40]  And we can consider, compare and contrast, like where we thought things were going and where things have actually ended up.
[708.54 --> 711.00]  It's a really nice piece of, I guess, audio journalism.
[711.60 --> 711.76]  Yeah.
[711.90 --> 712.10]  Yeah.
[712.20 --> 714.08]  I mean, it was just last year.
[714.16 --> 715.64]  I mentioned stable diffusion and all that.
[715.70 --> 716.58]  We were talking about this.
[716.58 --> 721.22]  It was like I had in my mind, oh, everything's going to image generation.
[721.22 --> 725.28]  Like, should I quit doing NLP and start thinking about image?
[725.28 --> 728.42]  And now all I do is NLP and language models.
[728.74 --> 732.02]  But at the time, that was, you know, that's what was on our mind.
[732.24 --> 732.62]  Same thing.
[732.72 --> 737.68]  I was working on a web UI for stable diffusion just like a thousand other front-end developers were.
[738.10 --> 741.08]  And yesterday was the first time I opened stable diffusion in six months.
[743.28 --> 744.74]  And a lot has changed.
[744.88 --> 747.46]  And it's still an area that's developing.
[747.92 --> 751.24]  But it's not, yeah, it's not driving thought process at the moment.
[751.24 --> 751.64]  Yeah.
[751.78 --> 756.78]  Well, especially because I think just it depends on what you think you want to do.
[757.26 --> 758.90]  And I'm definitely less visual.
[759.06 --> 760.60]  I'm more of a text-driven person.
[760.80 --> 763.50]  So I naturally lean towards LLMs anyway, like NLP.
[764.00 --> 764.28]  Yeah.
[764.64 --> 767.38]  I can hit some listener favorites maybe.
[767.38 --> 767.58]  Yeah, crowd favorites.
[767.92 --> 774.90]  So we have like one clear favorite, which is actually, I would say it's a surprise to me.
[775.14 --> 780.42]  Not because the guest wasn't good or anything, but just the, so the topic was Metaflow.
[780.42 --> 782.34]  So I don't know if you've heard of Metaflow.
[782.54 --> 790.84]  It's a Python package for kind of full stack data science modeling work developed at Netflix.
[790.84 --> 795.80]  And we had Villa Tools on, who was the creator of that package.
[795.94 --> 803.10]  And that has had, so it's like maybe a 30% more listens than any other episode.
[803.10 --> 810.32]  And I think the title, so we titled it from, I think, from notebooks to production or something
[810.32 --> 810.96]  like that.
[811.10 --> 811.26]  Yeah.
[811.42 --> 818.84]  So it's like this idea of from notebooks to production, there's all sorts of things that
[818.84 --> 823.42]  prevent you from getting the value out of these sorts of methodologies.
[823.42 --> 831.20]  And my guess would be that talking about that is probably like the key feature of that episode.
[831.32 --> 832.54]  And Metaflow is like really cool.
[832.64 --> 833.66]  People should check it out.
[834.06 --> 839.48]  It is one way to kind of do this, both versioning and orchestration and deployment and all of
[839.48 --> 840.70]  these things that are really important.
[841.20 --> 848.58]  But I think a takeaway for me was like practically bringing into the, some people might call it like
[848.58 --> 853.34]  full stack data science or like model life cycle things.
[853.34 --> 856.80]  Like the model life cycle things interest people so much.
[856.92 --> 862.60]  So beyond making like a single inference or beyond doing like a single fine tuning,
[862.92 --> 868.36]  what is the life cycle around a machine learning or an AI project?
[868.48 --> 873.70]  I think that really fascinates people because it's like the struggle of everyday life in actual
[873.70 --> 875.48]  practical usage of these models.
[875.48 --> 881.62]  So it's one thing to go to Hugging Face, try out like a Hugging Face space and like create
[881.62 --> 884.76]  some cool output or even just pull down a model and get output.
[885.04 --> 890.58]  But how do I handle like model versioning and orchestration of that in my own infrastructure?
[890.82 --> 896.42]  How do I tie in my own data set to that and do it in a way that like is fairly robust?
[896.78 --> 902.46]  How do I, you know, take these data scientists who like use all this weird tooling and like
[902.46 --> 909.68]  mash them into an organization that deals with like DevOps and like non AI software and all of that?
[909.76 --> 912.66]  I think those are questions people are just wrestling with all the time.
[913.36 --> 913.46]  Yeah.
[913.64 --> 920.66]  It feels a little bit in conflict with the trends of foundation models where you, the primary appeal
[920.66 --> 924.86]  is you train once and then you never touch it again or you'd release it as a version and
[924.86 --> 927.20]  people kind of just prompts based off of that.
[927.20 --> 933.00]  And I feel like this, I feel this evolution moving from essentially the MLOps era into,
[933.80 --> 935.84]  for lack of a better word, LLMOps.
[936.18 --> 936.42]  Yeah.
[936.46 --> 937.22]  How do you feel about that?
[937.48 --> 940.12]  No, I think you're, I think you're completely right.
[940.28 --> 946.70]  I think there will always be a place for like these models in organizations that are task
[946.70 --> 951.58]  specific models, like scikit-learn models or whatever that solve a particular problem.
[951.58 --> 957.46]  Because organizations like finance organizations or whatever will always have like a need for
[957.46 --> 959.24]  explainability or whatever it might be.
[959.76 --> 964.66]  But I do think we're moving into a period where like I've had to rebuild a lot of my
[964.66 --> 972.04]  own intuition as a data scientist from thinking about gather my data, create like my code for
[972.04 --> 978.76]  training, output my model, serialize it, push it to some hub or something, deploy it, you
[978.76 --> 983.88]  know, handle orchestration to now thinking about, okay, which of these pre-trained models
[983.88 --> 984.74]  do I select?
[984.76 --> 988.00]  And how do I engineer my prompting and my chain?
[988.16 --> 992.58]  Maybe going to fine tuning, like that is still like a really relevant topic.
[993.16 --> 997.32]  But some of these things that like I've been working on with PredictionGuard, I think are
[997.32 --> 1002.74]  the things that have a parallel in MLOps, but they're slightly, like there's just a slightly
[1002.74 --> 1003.52]  different flavor.
[1003.52 --> 1011.82]  I think it's how MLOps is graduating to something else versus like people are still concerned
[1011.82 --> 1012.58]  about ops.
[1012.82 --> 1016.28]  It's just like you say, it's a kind of a different kind of ops.
[1016.86 --> 1016.98]  Yeah.
[1017.06 --> 1020.64]  And I think that's reflected in our most popular episodes too.
[1020.76 --> 1023.64]  So I think all three of our most popular episodes are model-based.
[1023.76 --> 1025.58]  They're not more like infrastructure-based.
[1025.58 --> 1030.60]  So I think number one is the one with Reza Shabani, where we talked about how they train
[1030.60 --> 1035.56]  the replic code model and the Amjad vibes that they used to figure out whether or not
[1035.56 --> 1036.28]  the model was good.
[1036.44 --> 1039.02]  And I think, you know, that makes sense for our community.
[1039.22 --> 1041.58]  It's mostly software engineers and AI engineers.
[1041.78 --> 1044.42]  So code models are obviously a hot topic.
[1044.82 --> 1044.84]  Yeah.
[1044.90 --> 1045.06]  Yeah.
[1045.12 --> 1046.00]  That was really good.
[1046.10 --> 1050.50]  And I think like it was one of the first times where we kind of went beyond just listening
[1050.50 --> 1055.34]  traditional benchmarks, you know, which is why we did a whole thing about Amjad eval.
[1055.58 --> 1060.28]  It's like a lot of companies are using these models and they're using off-the-shelf benchmarks
[1060.28 --> 1060.72]  to do it.
[1060.82 --> 1064.22]  And what, you know, in other episodes that we'll talk about is like the one with Jonathan
[1064.22 --> 1065.66]  Frankel from Mosaic ML.
[1065.80 --> 1071.70]  And he also mentioned a lot of the benchmarks are multiple choice, but most production workloads
[1071.70 --> 1074.06]  are like open-ended text generation questions.
[1074.40 --> 1077.28]  So how do you kind of reconcile the two?
[1077.50 --> 1077.98]  Yeah.
[1077.98 --> 1085.14]  Did you all get into at all, you know, the whole space of LLMs evaluating LLMs and sort
[1085.14 --> 1090.62]  of, this was something on a recent episode we talked to Jerry from Llama Index about in
[1090.62 --> 1097.00]  terms of, on the one hand, generating questions like you're talking about to evaluate LLMs or
[1097.00 --> 1102.10]  using an LLM to look at the context and a response and provide an evaluation.
[1102.44 --> 1107.00]  I think that's definitely something that I think is interesting and has come up in a few
[1107.00 --> 1110.92]  of our episodes recently where people are struggling to evaluate these things.
[1111.10 --> 1117.14]  And so, yeah, we've seen a similar trend in one direction thinking about benchmarks and
[1117.14 --> 1121.78]  in another direction thinking about this sort of on the fly or model based evaluation, which
[1121.78 --> 1123.58]  has existed for some time.
[1123.58 --> 1125.96]  Like in machine translation, it's very common.
[1126.16 --> 1128.50]  So like Unbabel uses a model called Comet.
[1128.50 --> 1134.34]  That's like one of the most popular, highest performing machine translation evaluators as
[1134.34 --> 1134.76]  a model.
[1134.98 --> 1137.90]  It's not a metric and that sort of thing like blue.
[1138.46 --> 1143.42]  So yeah, that's a trend that we've seen is, is evaluation and specifically evaluation for
[1143.42 --> 1145.96]  LLMs, which can kind of get dicey.
[1146.10 --> 1146.18]  Yeah.
[1146.22 --> 1149.90]  We did a benchmarks one-on-one episode that is also well-liked.
[1149.90 --> 1155.04]  And we talked about this concept of like a benchmark driven development, you know, like
[1155.04 --> 1158.96]  the benchmarks used to evolve every like three, four years.
[1159.34 --> 1162.22]  And now the models are catching up every like six months.
[1162.36 --> 1168.30]  So there's kind of this race between the benchmarks creators and like the models developers to find,
[1168.46 --> 1173.66]  okay, the state of the art benchmarks is here and GPT-4 on a lot of them gets like, you
[1173.66 --> 1175.74]  know, 98 percentile results.
[1175.74 --> 1178.40]  So, you know, GPT-4 is not a GI.
[1178.56 --> 1182.00]  Therefore, to get to a GI, we need better evals for these models to start pushing the
[1182.00 --> 1182.28]  boundaries.
[1182.52 --> 1187.52]  And yeah, I think a lot of people are experimenting with using models to generate these things,
[1187.60 --> 1190.40]  but I don't think there's a clear answer yet.
[1190.54 --> 1195.66]  Something that I think we were quite surprised to find was specifically in HelloSwag, where
[1195.66 --> 1200.14]  the benchmarks, instead of being manually generated, were adversarially generated.
[1200.60 --> 1204.62]  And then I was very interested in our, I mean, this is kind of like segueing, we're not
[1204.62 --> 1209.28]  really going in sequence here, segueing into our second most popular episode, which was
[1209.28 --> 1213.34]  one RoboFlow, which covered segment anything from Meta.
[1213.52 --> 1216.18]  I think you guys had a discussion about that too.
[1216.24 --> 1217.72]  Yeah, it's been mentioned on the show.
[1217.76 --> 1219.82]  I don't think we've had a show devoted to it.
[1220.06 --> 1225.82]  Well, the most surprising finding when you read the paper is that something like less than
[1225.82 --> 1230.22]  one percent of the data of the mass that they released were actually human generated.
[1230.54 --> 1231.64]  A lot of it was AI assisted.
[1231.64 --> 1237.48]  So you have essentially models evaluating models, and the models are themselves trained
[1237.48 --> 1239.86]  on model generated data.
[1240.86 --> 1243.20]  We have very many layers in at this point.
[1243.30 --> 1243.76]  Yeah, yeah.
[1244.18 --> 1250.06]  And I know that there's been a few papers recently about the sort of things that were done with
[1250.06 --> 1254.88]  LAMA and other models around model generated output and data sets.
[1255.22 --> 1256.20]  It'll be interesting to see.
[1256.26 --> 1257.82]  I think it's still early days for that.
[1257.82 --> 1264.08]  So I think at the very minimum, what all of these cases show is that models, either evaluating
[1264.08 --> 1266.46]  models or using simulated data.
[1266.60 --> 1272.44]  I think back a few years ago, we would probably call this simulated data, right?
[1272.48 --> 1275.20]  I don't think that term is quite as popular now.
[1275.20 --> 1275.22]  Augmented?
[1275.54 --> 1275.98]  Yeah.
[1276.10 --> 1279.14]  Or augmentation data, augmentation, simulated data.
[1279.14 --> 1284.60]  So I think this has been a topic for some time, but the scale at which we're seeing this done
[1284.60 --> 1292.44]  is kind of shocking now and encouraging that we can do quite flexible things by combining
[1292.44 --> 1297.16]  models together, both at inference time, but also for training purposes.
[1297.40 --> 1300.16]  Well, have you ever come across this term of mode collapse?
[1300.16 --> 1305.02]  What I fear is, especially as someone who cares about low resource stuff, is that stacking
[1305.02 --> 1310.00]  models on top of models on top of models, you just optimize for the median use case or
[1310.00 --> 1310.78]  the modal use case.
[1311.10 --> 1311.24]  Yeah.
[1311.60 --> 1311.98]  Yeah.
[1312.04 --> 1316.56]  I think that one maybe, so yeah, that is a concern.
[1316.74 --> 1317.92]  I would say it's a valid concern.
[1318.22 --> 1324.60]  I do think that these sort of larger models, and this gets, I guess, more into like multilingualism
[1324.60 --> 1331.04]  and the makeup of various data sets of these LLMs, the more that we can have linguistic diversity
[1331.04 --> 1338.54]  represented in these LLMs, which I know, I think Cohere for AI just announced like a community
[1338.54 --> 1343.26]  driven effort to increase multilinguality in LLM data sets.
[1343.50 --> 1349.88]  But I think the more we do that, I think it does benefit the downstream lower resource
[1349.88 --> 1354.84]  languages and lower resource scenarios more because we can still do fine tuning.
[1355.44 --> 1362.80]  I mean, we all love to use pre-trained models now, but like in my previous work, when you were
[1362.80 --> 1368.24]  looking at maybe an Arabic vernacular language rather than standard Arabic, there's so much
[1368.24 --> 1370.12]  standard Arabic in data sets.
[1370.56 --> 1376.96]  Making that leap to an Arabic vernacular is much, much easier if that Arabic is included
[1376.96 --> 1380.62]  in LLM data sets because you can fine tune from those.
[1380.74 --> 1383.64]  So that is encouraging that that can happen more and more.
[1383.78 --> 1386.44]  There's still some major challenges there.
[1386.60 --> 1392.42]  And especially because most of the content that's being generated out of models is not
[1392.42 --> 1396.66]  in, you know, Central Siberian Yupik or one of these languages, right?
[1397.04 --> 1400.06]  So we can't purely rely on those.
[1400.06 --> 1405.80]  But I think my hope would be that the larger foundation models see more linguistic diversity
[1405.80 --> 1406.48]  over time.
[1407.00 --> 1411.68]  And then there's these sort of grassroots organizations, grassroots efforts like Masakane
[1411.68 --> 1416.70]  and others that rise up kind of on the other end and say, OK, well, we'll work with our
[1416.70 --> 1421.08]  language community to develop a data set that can fine tune off of these models.
[1421.72 --> 1425.98]  And hopefully there's benefit both ways in that sense.
[1426.50 --> 1431.42]  Since you mentioned Masakane a couple of times, we'll drop the link in the show notes so people
[1431.42 --> 1431.92]  can find it.
[1432.16 --> 1433.60]  But what exactly do they do?
[1433.88 --> 1435.46]  How big of an impact have they had?
[1435.46 --> 1436.56]  Yeah, I would say so.
[1436.74 --> 1440.46]  If people aren't familiar, if you go to the link, you'll see it.
[1440.74 --> 1447.08]  They talk about themselves as a grassroots organizations of African NLP researchers creating
[1447.08 --> 1448.72]  technology for Africa.
[1448.72 --> 1458.76]  So we have our own kind of biases as people in an English driven sort of literate world of
[1458.76 --> 1462.00]  what technology would be useful for everyone else.
[1462.00 --> 1467.08]  Like it probably makes sense for maybe listeners to say, well, wouldn't it be great if we could
[1467.08 --> 1469.32]  translate Wikipedia into all languages?
[1469.32 --> 1470.32]  Well, maybe.
[1470.32 --> 1471.32]  Well, maybe.
[1471.32 --> 1476.68]  But actually, the reality on the ground is that many language communities don't want Wikipedia
[1476.68 --> 1478.20]  translated into their language.
[1478.20 --> 1480.22]  That's not how they use their language.
[1480.22 --> 1483.62]  Or they're not literate and they're in oral culture.
[1483.62 --> 1485.28]  So they need speech, right?
[1485.66 --> 1487.44]  Text won't do them any good.
[1487.44 --> 1495.98]  So that's why Masakane has started as a sort of grassroots organization of NLP practitioners
[1495.98 --> 1501.72]  who understand the context of the domain that they work in and are able to create models and
[1501.72 --> 1504.42]  systems that work in those contexts.
[1504.42 --> 1505.44]  There's others.
[1505.44 --> 1510.16]  You can hear them on like the AI for Africa episodes that we have that talk about like
[1510.16 --> 1511.68]  agriculture use cases.
[1512.46 --> 1517.52]  Agriculture use cases in the US might look like, you know, John Deere tractor with a cam.
[1517.64 --> 1521.48]  Like, I don't know if people know this, but like John Deere tractors are these big tractors.
[1521.66 --> 1526.42]  They literally they have a Kubernetes cluster on like some of them have a Kubernetes cluster
[1526.42 --> 1527.82]  on the tractor.
[1528.12 --> 1532.36]  It's like a at the edge Kubernetes cluster that runs these models.
[1532.36 --> 1537.44]  And like when you're laying down pesticide, there's cameras that will actually identify
[1537.44 --> 1541.66]  and spray like individual weeds rather than like spraying the whole field.
[1541.66 --> 1546.84]  So that's like at the level that, you know, maybe is useful here in Africa.
[1546.84 --> 1554.26]  Maybe the more useful thing is around disease or drought identification or disaster relief
[1554.26 --> 1555.46]  or other things like that.
[1555.70 --> 1560.48]  And so there's people working in those environments or in those domains that know those domains
[1560.48 --> 1563.50]  that are producing technology for those cases.
[1563.76 --> 1565.02]  And I think that's really important.
[1565.24 --> 1567.18]  So, yeah, I would encourage people to check out Masakane.
[1567.58 --> 1568.80]  And there's other groups like that.
[1568.92 --> 1575.32]  And if you're in like the US or Europe or wherever and you want to get involved, there's
[1575.32 --> 1578.76]  open arms to say, hey, come help us do these things.
[1578.92 --> 1580.28]  So, yeah, get involved, too.
[1581.00 --> 1582.56]  What else is in your top three?
[1582.84 --> 1583.30]  Oh, yeah.
[1583.30 --> 1587.84]  So one recent one from Raj Shah from Hugging Face.
[1588.26 --> 1592.36]  Some people might have seen his really cool videos on LinkedIn or other places.
[1592.58 --> 1595.64]  He makes TikTok videos about AI models, which is awesome.
[1596.46 --> 1600.46]  And his episode is called The Capabilities of LLMs.
[1600.46 --> 1609.36]  And I thought it was really a good way to help me understand the landscape of large language
[1609.36 --> 1614.58]  models and the various features or axes that they're kind of situated in.
[1614.70 --> 1619.36]  So one axis is, for example, closed or open, right?
[1619.40 --> 1620.48]  Can I download the model?
[1620.88 --> 1628.22]  But then on top of that, there's another axis, which is, is it available for commercial use
[1628.22 --> 1629.12]  or is it not?
[1629.12 --> 1635.50]  And then there's other axes like we already talked about multilinguality, but then there's
[1635.50 --> 1637.44]  like task specificity, right?
[1637.46 --> 1640.56]  Like there's code gen models and there's language generation models.
[1640.56 --> 1644.04]  And there's, of course, image generation models and all of those as well.
[1644.58 --> 1651.66]  So, yeah, I think that episode really helps set a good foundation, no pun intended, for language
[1651.66 --> 1654.98]  models to understand where they're situated.
[1654.98 --> 1659.30]  So you can kind of, when you go to Hugging Face and there's, what is there, like 200,000
[1659.30 --> 1659.90]  models now?
[1660.14 --> 1661.92]  Maybe there's, I don't know how many models there are.
[1662.10 --> 1666.16]  How do I like navigate that space and understand what I could pull down?
[1666.30 --> 1670.52]  Or do I fit into one of those use cases where it makes sense for me to just connect to open
[1670.52 --> 1672.54]  AI or Cohere or Anthropic?
[1673.26 --> 1675.60]  Helps kind of situate yourself.
[1675.60 --> 1679.60]  So I think that's why that episode was so popular as he kind of lays all of that out
[1679.60 --> 1680.80]  in an understandable way.
[1681.26 --> 1683.10]  How do you personally stay on top of models?
[1683.34 --> 1685.64]  You know, there's leaderboards, there's Twitter, there's LinkedIn.
[1686.48 --> 1686.92]  Yeah.
[1687.06 --> 1693.88]  I think it's a little bit spread out for me between the sources that you mentioned as podcasters.
[1694.04 --> 1694.98]  I think that's one of the...
[1694.98 --> 1695.30]  Yeah, it's our job.
[1695.64 --> 1695.84]  Yeah.
[1695.84 --> 1698.14]  Well, it's also a benefit for us.
[1698.24 --> 1705.12]  I think if I didn't have every week on Wednesday, I'm going to talk about this topic.
[1705.36 --> 1712.46]  Whether I'm planning to think about a certain thing or not, it kind of helps you prompt and
[1712.46 --> 1714.06]  look at what's going on.
[1714.14 --> 1716.68]  So I think that is an advantage of content creators.
[1716.68 --> 1723.92]  It is kind of a responsibility, but it's also an advantage that we can have to have the
[1723.92 --> 1727.00]  excuse to have great conversations with people every week.
[1727.58 --> 1731.64]  But yeah, I think Twitter is a little bit weird now, as everybody knows, but it's still
[1731.64 --> 1733.66]  a good place to find out that information.
[1734.56 --> 1741.30]  And then sometimes too, to be honest, I go to Hugging Face and I'll search for models, but
[1741.30 --> 1747.52]  I also search and I look at the statistics around the downloads of models, because generally
[1747.52 --> 1752.78]  when people find something useful, then they'll download it and download it over and over.
[1753.10 --> 1756.86]  So sometimes when I hear about a family of models, I'll go there and then I'll look at
[1756.86 --> 1760.44]  some of the statistics on Hugging Face and try a few things.
[1760.82 --> 1761.00]  Yeah.
[1761.30 --> 1765.14]  And some of these forks, I see the download numbers, but I've never heard of them outside
[1765.14 --> 1765.78]  of Hugging Face.
[1765.92 --> 1766.50]  Yeah, it's true.
[1766.68 --> 1767.08]  It's true.
[1767.08 --> 1772.18]  And some of them, there'll be a fork or a fine tune or something.
[1772.48 --> 1777.40]  And you do have to do a little bit of digging around licensing and that sort of thing too.
[1777.78 --> 1779.24]  But it is a useful...
[1779.24 --> 1783.58]  There's tons of people doing amazing stuff out there that aren't getting recognized at
[1783.58 --> 1787.54]  the Falcon or MPT level.
[1787.92 --> 1793.28]  But there's a lot of people doing cool stuff that are releasing models on Hugging Face, maybe
[1793.28 --> 1794.88]  that they've just found interesting.
[1794.88 --> 1797.34]  Any unusual ones that you recently found?
[1797.64 --> 1801.74]  Well, there's one that I'll highlight, which I thought was cool because I don't know if
[1801.74 --> 1806.40]  you all saw the meta released this...
[1806.40 --> 1808.50]  The six modality model?
[1808.74 --> 1809.28]  Yeah, yeah.
[1809.40 --> 1814.20]  And it was interesting because we did this work with Masakane when I was at SIL.
[1814.40 --> 1821.24]  We did this work with Masakane and Koki, which is a speech tech company, to create these
[1821.24 --> 1823.68]  language models in six African languages.
[1824.46 --> 1827.06]  And I was like, okay, that's cool.
[1827.44 --> 1828.02]  We did that.
[1828.10 --> 1829.40]  We formed the data sets.
[1829.58 --> 1830.82]  It was satisfying.
[1831.20 --> 1838.02]  But now I'm learning that then Meta went and found that data on Hugging Face.
[1838.38 --> 1844.00]  And that's kind of incorporated in these new models that Meta has released.
[1844.00 --> 1849.92]  So it's cool to see the full cycle thing happen where there was grassroots organizations seeing
[1849.92 --> 1854.58]  a need for models, gathering data, doing baselines.
[1854.58 --> 1862.24]  And now there's extended functionality in a more influential way, I guess, at that higher
[1862.24 --> 1862.54]  level.
[1862.54 --> 1863.02]  Yeah.
[1863.50 --> 1863.68]  Yeah.
[1863.80 --> 1868.86]  I think, I mean, talking about open and closed models, when we started the podcast, it kind
[1868.86 --> 1875.56]  of looked like a cathedral kind of market where we had Cohere, Anthropic, OpenAI, Stability,
[1875.80 --> 1878.04]  and those were like the hottest companies.
[1878.26 --> 1882.68]  I think now, you know, as you mentioned, you go on Hugging Face, like I just opened it right
[1882.68 --> 1882.84]  now.
[1882.92 --> 1888.90]  There's this other news research 13 billion parameters model that just got released, fine
[1888.90 --> 1890.94]  tuned on over 300,000 instructions.
[1890.94 --> 1895.02]  It's like models are just popping up everywhere, which is great.
[1895.26 --> 1900.48]  And yeah, we had an episode with, as I mentioned, with Jonathan Frankel and Abhinav from Mosaic
[1900.48 --> 1904.18]  ML to introduce MPT 7B and some of the work that they've done there.
[1904.30 --> 1909.94]  And I think like one of their motivation is like keeping the space as open as possible,
[1910.12 --> 1916.72]  like making it easy for anybody to go, obviously, ideally on Mosaic ML's platform and turn their
[1916.72 --> 1918.10]  own models and whatnot.
[1918.30 --> 1920.16]  So that's one that people really liked.
[1920.16 --> 1921.48]  I thought it was really technical.
[1921.80 --> 1923.70]  So I was really a little worried at first.
[1923.84 --> 1926.28]  I was like, is it going to fly over most people's head?
[1926.52 --> 1927.84]  But it was actually super well received.
[1927.84 --> 1928.72]  No, we're going more technical.
[1929.16 --> 1929.58]  Exactly.
[1929.82 --> 1931.72]  Now that was a good learning.
[1931.84 --> 1932.22]  Leaning in.
[1932.72 --> 1933.12]  Exactly.
[1933.12 --> 1936.56]  And Jonathan is super passionate about open source.
[1936.56 --> 1942.02]  He had this rant halfway through the episode about why it's so important to keep models
[1942.02 --> 1942.40]  open.
[1942.54 --> 1947.84]  And I actually edited in a crowd applause into the podcast, which I kind of love.
[1947.90 --> 1951.48]  I love little audio bonuses for people listening along.
[1951.48 --> 1956.30]  And I think the changelog guys do that really well, especially in their newer episodes.
[1956.48 --> 1956.50]  Yeah.
[1956.54 --> 1957.10]  We need to.
[1957.44 --> 1959.96]  There is a way for us to integrate some of those things.
[1960.04 --> 1960.18]  Yeah.
[1960.18 --> 1961.24]  Like the soundboard thing.
[1961.24 --> 1963.30]  And we've never got into it too much.
[1963.34 --> 1965.86]  I need to work with Jared from the changelog and see.
[1966.38 --> 1967.20]  It just spices it up.
[1967.34 --> 1967.74]  Exactly.
[1967.92 --> 1968.28]  Exactly.
[1968.70 --> 1971.66]  You can only have so many hour long conversations about ML.
[1973.72 --> 1974.12]  Yeah.
[1974.12 --> 1977.40]  I keep thinking that, but then we keep going.
[1977.80 --> 1978.60]  Right, right, right, right.
[1979.00 --> 1979.26]  Sorry.
[1979.40 --> 1981.30]  I didn't mean like it was like a...
[1981.30 --> 1982.04]  No, I got you.
[1982.04 --> 1986.48]  It switches it up and makes the audio interesting to add variety.
[1987.08 --> 1987.22]  Cool.
[1987.54 --> 1990.82]  I don't know if there are any other highlights that we want to do for...
[1990.82 --> 1993.06]  I'll just highlight maybe one more.
[1993.78 --> 1995.08]  Kirsten Lum was on.
[1995.22 --> 1998.06]  She had an episode about machine learning at small organizations.
[1998.70 --> 1999.84]  I think that's a great one.
[1999.84 --> 2006.66]  If you're a data scientist or a practitioner or an engineer at either a startup or a mid-sized
[2006.66 --> 2011.82]  company where I think the thing that she emphasized was these different tasks that we
[2011.82 --> 2017.70]  think about, whether it's curating a data set or training a model or fine-tuning a model
[2017.70 --> 2019.78]  or deploying a model.
[2020.36 --> 2024.46]  Sometimes at a larger organization, those are functions in and of themselves.
[2024.64 --> 2029.38]  But when you're in this sort of mid-range organization, that's like a task you do, right?
[2029.38 --> 2037.74]  So to think about those tasks as tasks of your role and time box them and understand how
[2037.74 --> 2043.48]  to do all of those things well without getting sucked down into any one of those things, that
[2043.48 --> 2048.98]  was an insight that I found quite useful in my day-to-day as well as to sort of start to
[2048.98 --> 2055.04]  get a little bit of spidey sense around, hey, I'm spending a lot of time doing this, which
[2055.04 --> 2058.96]  probably means I'm stuck in too much.
[2059.46 --> 2065.52]  I'm making my ML ops too complicated to track versions and tie all this stuff together.
[2065.66 --> 2071.14]  Maybe I should just do a simple thing and paste a number in a Google sheet and move on or something.
[2071.64 --> 2074.42]  I think that's a good segue into some of the other work that you do.
[2074.60 --> 2080.86]  You run the datadan.io website, which is kind of like different types of workshop and advising
[2080.86 --> 2081.46]  that you do.
[2082.04 --> 2086.74]  I think a lot of founders especially are curious about how are companies thinking about using
[2086.74 --> 2087.48]  this technology?
[2087.74 --> 2091.44]  There's a lot of demos on Twitter, a lot of excitement.
[2091.92 --> 2096.20]  But when founders are putting together something that they want to sell, they're like, okay,
[2096.72 --> 2099.18]  what are the real problems that enterprises have?
[2099.38 --> 2101.66]  What are some of the limitations that they have?
[2101.70 --> 2104.36]  We talked about commercial use cases and something like that.
[2104.36 --> 2111.54]  Can you maybe talk a bit about two, three high-level learnings that you had from these workshops
[2111.54 --> 2116.58]  on how these models are actually being brought into companies and how they're being adopted?
[2117.12 --> 2124.62]  Yeah, I think maybe one higher-level comment on this is even though we see all these demos
[2124.62 --> 2126.84]  happening, everybody's using ChatGPT.
[2126.84 --> 2136.40]  The reality in enterprise is most enterprises still don't have LLMs integrated across their
[2136.40 --> 2137.70]  technology stack, right?
[2137.76 --> 2139.82]  So that might be a bummer for some people.
[2139.92 --> 2141.74]  Like, oh, it's not quite as pervasive.
[2141.74 --> 2147.94]  But I actually find it as refreshing, maybe because some of us feel like stuff happens every
[2147.94 --> 2148.20]  week.
[2148.34 --> 2150.24]  It's exhausting to keep up.
[2150.40 --> 2153.70]  Like, oh, if I don't keep up with this stuff, then I'm getting left behind.
[2153.70 --> 2157.04]  But it takes time for these things to trickle down.
[2157.78 --> 2161.86]  And not everything, like we were talking about the stable diffusion use case and others, like
[2161.86 --> 2167.08]  not everything that's hyped at the moment will be a part of your, like, day-to-day life forever,
[2167.34 --> 2167.64]  right?
[2167.68 --> 2169.80]  So you can kind of take some comfort in that.
[2170.28 --> 2175.14]  I think it's really important for people to, if they're interested in these models, to really
[2175.14 --> 2180.58]  dig into more than just kind of a single prompt into these models.
[2180.58 --> 2189.18]  The practical side of using generative text models or LLMs really comes around either what
[2189.18 --> 2194.50]  some people might call prompt engineering, but, you know, understanding things like giving
[2194.50 --> 2201.30]  examples or demonstrations in your prompt, using things like guardrails or regex statements
[2201.30 --> 2209.78]  or prediction guard to structure output, doing like fine tuning for your company's data.
[2209.94 --> 2213.48]  Like these things go, there's kind of a hierarchy of these things.
[2213.64 --> 2215.98]  I think you all know Travis Fisher.
[2216.18 --> 2224.06]  He was a guest on Practical AI and talked about this hierarchy from prompt engineering through
[2224.06 --> 2233.16]  like data augmentation to fine tuning to eventually like training your own generative model.
[2233.66 --> 2239.96]  I've really tried to encourage enterprise users and those that I do workshops with to think
[2239.96 --> 2245.30]  something like that hierarchy with these models, like get hands on, do your prompting.
[2245.46 --> 2250.12]  But then like, if you don't get the answer that you want immediately, I think there's a tendency
[2250.12 --> 2256.12]  for people to say, oh, well, it doesn't work for my use case. But there's so much of a rich
[2256.12 --> 2261.78]  environment underneath that with things like link chain and llama index and, you know, data
[2261.78 --> 2268.96]  augmentation, chaining, customization, fine tuning, like all this stuff that can be combined together.
[2268.96 --> 2275.42]  It's a fun new experience, but I find that enterprise users just haven't explored past that
[2275.42 --> 2280.10]  very most shallow level. So I think, yeah, in terms of the trends that I've seen with
[2280.10 --> 2286.32]  the workshop, I think people have gone to chat GPT or one of these models, they've seen like the value
[2286.32 --> 2294.56]  that's there, but they have a hard time connecting these models to a workflow that they can use to
[2294.56 --> 2300.40]  solve problems. Like before we all had intuition, like I'm going to gather my data. It's going to have
[2300.40 --> 2306.20]  these five features. I'm going to train my scikit learn model or whatever. I'm going to deploy it with
[2306.20 --> 2312.52]  flask and like now I have a cool thing. Now all of that intuition has sort of been shattered a little
[2312.52 --> 2317.88]  bit. So we need to develop a new workflow around these things. And I think that's really the focus
[2317.88 --> 2323.80]  of the workshops is kind of rebuilding that intuition into a practical workflow that you can
[2323.80 --> 2326.84]  think through and solve problems with practically.
[2326.84 --> 2334.06]  You have a live prompt engineering class, prompt engineering, overrated or underrated?
[2334.46 --> 2343.48]  Yeah, I think prompt engineering as like a term is probably too hyped. I think engineering and ops
[2343.48 --> 2350.14]  around large language models though is, is a real thing. And it is sort of what we're transitioning to.
[2350.14 --> 2356.48]  Now, how much you want to say is like, that term gets used in all sorts of different contexts. It
[2356.48 --> 2361.34]  could mean just like, oh, I wrote a good prompt and I'm going to like sell it on Twitter or something.
[2361.86 --> 2366.12]  Prompt base, the marketplace of prompts. I wonder how they're doing, to be honest,
[2366.14 --> 2369.56]  because they get quoted in almost every article about prompt engineering. They got really,
[2369.70 --> 2370.22]  really good PR.
[2370.50 --> 2375.14]  Yeah. Yeah. I mean, if people can sell their prompts, I mean, I'm all for that. That's,
[2375.20 --> 2375.56]  that's cool.
[2375.56 --> 2381.02]  I got, I got prompts right here. You know, but I think it goes like some people might just mean
[2381.02 --> 2386.28]  that. And I think that's maybe overhyped in my view, but I do think there's this whole level
[2386.28 --> 2392.92]  of engineering and operations around prompts and chaining and data augmentation. That is a real
[2392.92 --> 2397.48]  workflow that people can use to solve their problems. And that's more what I mean when I'm
[2397.48 --> 2403.00]  referring to like whatever, however you want to combine the word engineering with prompting and
[2403.00 --> 2403.94]  language models.
[2404.32 --> 2406.30]  Yeah. I've just been calling it AI engineering.
[2406.42 --> 2407.68]  AI engineering. That's good.
[2407.82 --> 2412.44]  Wrangle with the AI APIs, know what to do with them. And that is a skillset that is developing
[2412.44 --> 2414.80]  that is a subspecialty of software engineering.
[2414.94 --> 2415.72]  Yeah. Yeah.
[2415.78 --> 2419.56]  It is what it is. And I think part of something I'm really trying to explore is this,
[2419.62 --> 2425.60]  is this spillover of AI from the traditional ML space, like where you need a machine learning
[2425.60 --> 2429.62]  researcher or machine learning engineer. It's spilling over into the software engineering space.
[2429.62 --> 2434.20]  And there's this rising class of what I'm calling AI engineer that is specialized in
[2434.20 --> 2437.86]  conversion and the research, the tooling, the conversations and themes.
[2438.38 --> 2443.90]  What do you think are the unique challenges that like someone coming from that latter group,
[2444.12 --> 2449.90]  like engineers that are advancing into this AI engineer position versus like probably more like
[2449.90 --> 2454.66]  my background where I was in data science for some time. And now I'm kind of like transitioning
[2454.66 --> 2460.02]  into this world. What do you, what do you think are the unique challenges for both groups of people?
[2460.46 --> 2465.30]  Oh, I mean, so I can speak to the software side and you can speak about the data science side.
[2465.46 --> 2471.16]  It's simply that we are for many of us dealing with a non-deterministic system for the first time
[2471.16 --> 2476.80]  that, by the way, we don't fully control because there's this conversation about did GPT-4
[2476.80 --> 2481.32]  regress in its quality? And we don't know because model drift is not within our control
[2481.32 --> 2487.74]  because it's a black box API from, from open AI. But beyond that, there's this sense that the,
[2487.74 --> 2493.06]  the latent space of, of capabilities is not fully explored yet.
[2493.12 --> 2497.62]  Yeah. Right. Like there, there's 175 billion or 1 trillion parameters in the model.
[2498.06 --> 2503.16]  We're maybe using like 200 of them. It's literally where, where is that meme where like,
[2503.16 --> 2507.86]  we're using 10% of our brain. We are, we've, we're probably using 10% of what is capable in
[2507.86 --> 2512.24]  the model. And it takes some ingeniousness to unlock that.
[2512.80 --> 2520.38]  Yeah. I think from the data science perspective, there's probably a desire to quickly to jump to
[2520.38 --> 2527.40]  these other things around fine tuning or training your own models, where if you really do take this
[2527.40 --> 2534.42]  prompting chaining data augmentation seriously, you can do a lot with models sort of off the shelf
[2534.42 --> 2540.02]  and don't need to like jump immediately into training. So I think that is like a knee jerk
[2540.02 --> 2546.12]  reaction on our end and fine tuning is going to be around for the foreseeable future as far as I can
[2546.12 --> 2551.12]  tell. But, um, data scientists have maybe a different, cause we've been dealing with the
[2551.12 --> 2558.16]  uncertainty or a non-deterministic output for some time and have developed some intuition around that.
[2558.76 --> 2563.44]  But that's mostly when we've been controlling the data sets, when we've been controlling like the
[2563.44 --> 2568.38]  model training and that sort of thing. So to throw some of that out, but still deal with that,
[2568.44 --> 2570.40]  it's a separate kind of challenge for us.
[2570.86 --> 2574.66]  I just remembered another thing that we've been developing on the latent space community,
[2574.66 --> 2576.54]  which is this concept of AI UX.
[2577.02 --> 2577.18]  Yeah.
[2577.18 --> 2581.90]  Right. That the last mile of showing something on the, on the screen and making it consumable,
[2582.06 --> 2587.68]  easily usable by people is perhaps as valuable as the actual training of the model itself.
[2587.82 --> 2588.02]  Yes.
[2588.12 --> 2591.96]  So I don't know if that's an overstatement, to be honest, like obviously you're spending like
[2591.96 --> 2596.06]  hundreds of millions of dollars training models and like, you know, putting it in some kind of
[2596.06 --> 2600.04]  react app. It's not, it's not the biggest innovation in the world, but a lot of people from
[2600.04 --> 2602.82]  OpenAI say like chat GBT was a mostly a UX innovation.
[2602.82 --> 2608.74]  Yeah. I think like leading up to chat, like when I saw the output of chat GBT, it wasn't,
[2608.86 --> 2614.04]  I don't think I had the same earth shattering experience that other people had in believing
[2614.04 --> 2620.62]  like, Oh, this output is coming from a model like that. Sure. It came from a model, but the
[2620.62 --> 2626.64]  reception to like that interface and like the human element of the dialogue, like that was,
[2626.64 --> 2632.20]  so maybe it's both and right. Like it's not like, you're not going to get that experience
[2632.20 --> 2637.50]  if you don't have the innovation under the hood and the modeling and the data set curation and all
[2637.50 --> 2645.04]  of that, but it can totally be ruined by like the UX. I typically give the example, like one day in
[2645.04 --> 2651.60]  Gmail, I logged in and like, I was typing my email and then like had the gray autocomplete. Right.
[2651.60 --> 2658.32]  I did not get like a pop-up that said like, do you want us to start writing your emails with AI?
[2658.66 --> 2664.60]  Like it just like was so smooth and it happened and it made like, it created value for me instantly.
[2664.96 --> 2669.88]  Right. So I think that there is really a sense to that, especially in this area where people have a
[2669.88 --> 2673.86]  lot of like misgivings or fear around the technology itself.
[2674.14 --> 2679.52]  And we're going to have Alex Gravely on in a future episode, but GitHub, when they had the initial
[2679.52 --> 2685.86]  codex model from OpenAI, they spent six months tuning the UX just to get copilot to a point where
[2685.86 --> 2690.04]  it's not a separate pane. It's not a separate text box. It's kind of in your code as you write
[2690.04 --> 2694.62]  the code. And to me, that's traditional, that's more to domain a traditional software engineering
[2694.62 --> 2697.32]  rather than ML engineers or research engineers.
[2697.70 --> 2702.58]  Yeah. Yeah. I would say that is probably, yes. To circle back to what we were talking about,
[2702.58 --> 2707.32]  like challenges that are unique to like engineers coming into this versus like data scientists coming
[2707.32 --> 2712.84]  into this. That's something data scientists, I think have not thought about very much at all.
[2712.98 --> 2718.42]  At the very most, it's data visualization that they've thought about. Right. Whereas engineers
[2718.42 --> 2724.84]  generally like there's some human, I mean, unless you're just a very pure backend systems engineer,
[2724.84 --> 2730.34]  like thinking about UI, UX is maybe a little bit more natural to that group.
[2730.72 --> 2730.78]  Yeah.
[2730.84 --> 2735.10]  You mentioned one thing, which is about data set curation. We're in the middle of preparing this
[2735.10 --> 2740.06]  long overdue episodes on, on, on data sets one-on-one. Any reflections on the evolutions
[2740.06 --> 2743.22]  in natural and NLP data sets that have been happening?
[2743.40 --> 2749.28]  Yeah. Great question. I definitely like, I think, are you all familiar with Label Studio
[2749.28 --> 2755.82]  and that it's one of the most popular kind of open source frameworks for data labeling. And they,
[2755.96 --> 2760.56]  they've been, I think they've been on, we have them on the show. Like we try to have them on the
[2760.56 --> 2765.72]  show every year as like data labeling expert. Maybe it's time for that. It's just reminding me.
[2765.72 --> 2771.14]  So, um, they just released, uh, so Erin McHale is on the, in the late space discord.
[2771.14 --> 2773.46]  I think you had her on at ODSC.
[2773.46 --> 2774.80]  She was at ODSC. Yeah.
[2774.80 --> 2778.62]  Yeah. Um, so they just released new tools for fine tuning generative AI models.
[2778.86 --> 2779.76]  Exactly. Yeah.
[2779.88 --> 2780.44]  It's a good occasion.
[2780.44 --> 2787.82]  I think, um, maybe the, that being an example of this is maybe a trend that we're seeing there is
[2787.82 --> 2796.64]  around augmented tooling or tooling that's really geared towards an approachable way to
[2796.64 --> 2804.48]  fine tune these models with human feedback or with customized data. So like, I know with Label
[2804.48 --> 2810.36]  Studio, a lot of the recent releases had somewhat to do with like putting LLMs in the loop with
[2810.36 --> 2815.38]  humans during the label process, similar to like, I think Prodigy has been doing this for some time,
[2815.46 --> 2821.30]  which is from Spacey. So this sort of human in the loop labeling and update of a model,
[2821.44 --> 2827.08]  they brought some of that in, but now like this new kind of set of tooling around specifically
[2827.08 --> 2835.26]  instruction tuning of models. I think before maybe people, and I've seen actually this misconception,
[2835.26 --> 2841.64]  I was in a advising call with a client and they're really struggling to understand like,
[2842.12 --> 2849.20]  okay, our company has been training or fine tuning models. Now we want to create our own
[2849.20 --> 2856.18]  like instruction tuned model. Like, how is that different from what we've been doing in the past?
[2856.18 --> 2864.88]  And kind of what I tried to help them see is, yes, like some of the workflow that happened around
[2864.88 --> 2870.04]  like reinforcement learning from human feedback is unique, but reinforcement learning is not unique.
[2870.28 --> 2874.52]  There's an element of training in that there's data set curation in that there's pre-training that
[2874.52 --> 2881.94]  happen like before that whole process happened. So the elements that you're familiar with are part of
[2881.94 --> 2888.74]  that they're just not packaged in the same way that you saw them before. Now there's this clear
[2888.74 --> 2895.78]  pre-training stage and then the human feedback stage, and then this reinforcement learning happens.
[2895.96 --> 2901.70]  So I think the more that we can bring that concept and that workflow into tooling, like what Label
[2901.70 --> 2907.10]  Studio is doing to make it more approachable for people to where it's not like this weird,
[2907.52 --> 2911.44]  like reinforcement learning from human feedback sounds very confusing to people.
[2911.44 --> 2917.00]  like PPO and helping people understand like how reinforcement learning works. It's very difficult.
[2917.78 --> 2924.58]  So the more the tooling can just have its own good UI UX around that process, I think the better and
[2924.58 --> 2929.30]  probably Label Studio and others are leading the front on leading the way on that front.
[2929.30 --> 2934.56]  I was thinking like, so labels are one thing. And by the way, okay, I'll take the side tangent on labels
[2934.56 --> 2938.22]  and I'll come back to the main point. I actually presume that scale would win everything.
[2938.72 --> 2938.86]  Yeah.
[2938.86 --> 2940.48]  And it seems like they haven't.
[2940.92 --> 2941.36]  Yeah.
[2941.60 --> 2946.32]  And, and sorry, the scale, the snorkel, there's this generation of labeling companies.
[2946.66 --> 2948.70]  Like data centric AI companies.
[2948.92 --> 2953.04]  Right. Right. What happened? Like, how come there's still new, new companies coming up? There's
[2953.04 --> 2958.30]  LabelBox, there's Label Studio. I don't have a sense of how to think about these companies. Like
[2958.30 --> 2959.26]  obviously labels are important.
[2959.26 --> 2968.18]  Yeah. Yeah. Yeah. I think also, even before that, there was like tool, at least features, even from cloud
[2968.18 --> 2973.70]  providers or whatever, like AutoML, like came before that, like upload your own data, create your own custom
[2973.70 --> 2983.34]  model. So I think that maybe it's that like companies that want to create this sort of custom models, and this is just my
[2983.34 --> 2990.80]  own opinion. I'll preface that. Maybe they don't want, like when they're thinking about that problem, they're not thinking
[2990.80 --> 3000.12]  about, oh, I need a whole platform to create custom models using our data. They're more thinking about like, how do I use these
[3000.12 --> 3008.38]  state of the art models with my data? And so it's still, if those statements are very similar, but if you notice, like one is
[3008.38 --> 3016.12]  more model centric and one is more data centric. So I think enterprises are still thinking like model centric and augmenting
[3016.12 --> 3021.98]  that with their data, whether that be just through augmentation or through fine tuning or training. They're not necessarily
[3021.98 --> 3031.72]  thinking about like a data platform for AI. They're thinking about bringing their AI or their data to the AI
[3031.72 --> 3039.36]  system, which is why I think like APIs like Cohere, OpenAI that offer fine tuning as part of their API.
[3039.70 --> 3044.28]  It's sort of like people love that. It makes sense. Like, okay, I can just upload some examples and it makes
[3044.28 --> 3050.78]  the model better, but it's still like model centric, right? Yeah. I get the sense that OpenAI doesn't want to
[3050.78 --> 3056.44]  encourage that anymore because they don't have fine tuning for 3.5 and 4. And then, so the last
[3056.44 --> 3059.72]  thing I'll do about data sets and we can go into the lightning round is I was actually thinking about
[3059.72 --> 3064.82]  unlapped data sets for unsupervised learning or self-supervised learning, right? Like that is
[3064.82 --> 3070.02]  something that we are trying to wrap our heads around, like common crawl, stack overflow archive,
[3070.12 --> 3074.50]  the books, you know, like, I don't know if you have any perspectives on that, like the trends that are
[3074.50 --> 3080.34]  arising here, the best practices. And like, as far as I can tell, nobody has a straight answer as to
[3080.34 --> 3084.28]  how, what the data mix is and everyone's just kind of experiments.
[3084.94 --> 3089.80]  Yeah. Well, I think that's partly driven by the fact that like the most popular models,
[3089.80 --> 3095.72]  you don't really have a clear picture of what the data mix is, right? So the people that are trying
[3095.72 --> 3101.40]  to recreate that and they're not achieving that like level of performance, right? Then they,
[3101.40 --> 3107.48]  one of the things that they know is, well, what are all the different data mix options that I can try
[3107.48 --> 3113.06]  and try to replicate some of what's going on, right? So I think it's partly driven by that is
[3113.06 --> 3121.12]  like, we don't totally know what the data mix is like sitting behind the curtain of open AI or others.
[3121.82 --> 3127.54]  But I think there's, there's a couple of trends, I guess, which you've already sort of highlighted.
[3127.54 --> 3134.76]  One is like, how can I mix up all of these public data sets and filter them in unique ways to make my
[3134.76 --> 3142.94]  model better? So some, I listened to a talk, I believe it was at last year's ACL and they did
[3142.94 --> 3150.26]  this study of common crawl, right? And they found that actually a significant portion of common crawl
[3150.26 --> 3156.40]  was like mislabeled all over the place, right? Like trash. Yeah. So like, I think it was 100%
[3156.40 --> 3163.52]  of the data that was labeled as Latin character Arabic. So Arabic written in Latin characters
[3163.52 --> 3169.38]  was not Arabic, like a hundred percent of it. And there was like all sorts of other problems and
[3169.38 --> 3177.08]  that sort of thing. So I think there's one side, one group of people or set of experiments that you
[3177.08 --> 3182.04]  could think about as like, how do I take these existing data sets, which I know have data quality
[3182.04 --> 3190.12]  issues or maybe other data biases or problems that I would like to filter out, like not fit for work
[3190.12 --> 3194.94]  data, that sort of thing. So how do I create my own special filtered mix of these and train a model?
[3195.04 --> 3200.86]  So that's one kind of genre. And then there's the other genre, which is like maybe taking those,
[3200.98 --> 3206.50]  but augmenting them with this like simulated or augmented data, right? That's out of a model,
[3206.66 --> 3211.72]  like a GPT model or something like that. So I think you could combine those in all sorts of
[3211.72 --> 3217.08]  unique ways. And I think it is a little bit of like the wild West because we don't totally have
[3217.08 --> 3223.00]  a good grip on what is the winning strategy there. And so I think that's where I would also encourage
[3223.00 --> 3229.82]  people to try a variety of models. So this is maybe a problem with benchmarks in general, right? Like
[3229.82 --> 3236.86]  you can see like the open large language model benchmark on hugging face and like these models are at the top
[3236.86 --> 3243.50]  top. And you could come away with that and say, well, I'm like anything below like the top three,
[3243.60 --> 3249.44]  I'm not even going to use. Right. But the reality is that each of those had a unique sort of flavor of
[3249.44 --> 3255.88]  this data under the hood that might actually work quite well for your use case. So one example that
[3255.88 --> 3263.80]  I've used recently in some work is the Camel 5 billion model from Ryder. You know, it doesn't work
[3263.80 --> 3269.12]  great for a lot of things, but there's certain things around like marketing copy and others that
[3269.12 --> 3275.02]  it does a really good job at. And it's a bit smaller model that I can host and run and I can get good
[3275.02 --> 3280.76]  output out of it if, if I put in some of that workflow and structuring around it, but I wouldn't
[3280.76 --> 3285.80]  use it for other cases, but that has a lot to do with the data and, you know, right. I'm guessing
[3285.80 --> 3292.12]  writers focus on that copy generation and such. So yeah, I would encourage people specifically on this
[3292.12 --> 3297.84]  topic to maybe think about what's going on under the hood and also give some models a try for
[3297.84 --> 3304.50]  different, like gain your own intuition about how a model behavior might change based on like how it
[3304.50 --> 3310.32]  was trained and the mix of data that went in. Awesome. Let's jump into the lightning round. We have
[3310.32 --> 3315.58]  three questions for you. It's lightning, but you can save 30 seconds to answer. All right, cool.
[3315.58 --> 3322.46]  So the first question is around acceleration. What's something that already happened in AI that
[3322.46 --> 3327.18]  you thought would take much longer? Yeah. I think the thing that I was thinking about here was like
[3327.18 --> 3335.04]  how general purpose these large language models are beyond traditional NLP tasks. So it doesn't
[3335.04 --> 3340.36]  surprise me that maybe they could do like sentiment analysis or even like NLI or something like that.
[3340.36 --> 3347.38]  These are things that have been studied for a long time, but the fact that I can like at ODSC,
[3347.54 --> 3353.74]  I was in like a workshop on fraud detection and they were using like some, I forget the models they
[3353.74 --> 3360.00]  were using some statistical models to do fraud detection. I was like, I wonder if I just like do a
[3360.00 --> 3365.72]  bit of chaining and like insert some of the examples of these insurance transactions into my prompts.
[3365.72 --> 3373.32]  If I can get the large language model to detect a fraudulent insurance client. And it seemed to like,
[3373.50 --> 3378.72]  like I got pretty far doing that. So that fact of like, you can do something like that with these
[3378.72 --> 3384.78]  models or that generalizable beyond traditional NLP techniques, I think is surprising to me.
[3385.16 --> 3389.92]  Awesome. Exploration. What are the most interesting unsolved questions in AI?
[3389.92 --> 3399.68]  Yeah. I think there is still such a focus on English and Mandarin. It's like that, like you're kind of
[3399.68 --> 3406.60]  large language model wise. If you look at the drop off and performance after you get past like
[3406.60 --> 3414.18]  English, Mandarin, German, Spanish to some degree, but German is actually better than Spanish because of
[3414.18 --> 3419.84]  how much it's been studied in NLP. And of course, Mandarin has a lot of data. Spanish still does
[3419.84 --> 3426.38]  good, but like there's languages, even in the top hundred languages of the world that are spoken
[3426.38 --> 3431.38]  by millions and millions and millions of people around the world that don't like perform well in
[3431.38 --> 3437.62]  these models. So that's like thing one, but even modality wise, I know there's a lot of work going on
[3437.62 --> 3443.56]  in the research community around sign language, but like there's all of these different modalities
[3443.56 --> 3451.44]  of language. Written text is not, does not equal communication, right? Written text is a synthesis
[3451.44 --> 3459.98]  of communication into a written form that some people consume. But the combination of all of these
[3459.98 --> 3465.36]  modalities along with all of these languages, there's just so much room to explore there and so many
[3465.36 --> 3472.68]  challenges left to explore that will eventually, I think, help us learn a lot about communication in
[3472.68 --> 3478.58]  general and the limitations of these models, but is an exciting area. It's definitely a challenge,
[3478.70 --> 3484.74]  but an exciting area. Awesome, man. So one last takeaway, what's something or a message that you
[3484.74 --> 3489.72]  want everyone to remember today? Yeah, similar to when you were asking about my workshops, I think I
[3489.72 --> 3497.50]  would just encourage people to get hands-on with these models and really dig into the new sets of tooling
[3497.50 --> 3503.48]  that are out there. There's so much good tooling out there to go from like a simple prompt to inject
[3503.48 --> 3510.42]  your own data, to form like a query index, to create like a chain of processing, even like trying
[3510.42 --> 3515.44]  agents and all those things. Like get hands-on and try it. That's the only way that you're going to build
[3515.44 --> 3521.06]  out this intuition. So yeah, that would be my encouragement. Excellent. Well, thanks for coming on.
[3521.06 --> 3523.02]  Yeah. Thank you guys so much. This is awesome.
[3523.02 --> 3539.62]  Thank you for listening to Practical AI. Your next step is to subscribe now, if you haven't already.
[3540.08 --> 3545.24]  And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with
[3545.24 --> 3550.28]  your friends and colleagues. Thanks once again to Fastly and Fly for partnering with us to bring you
[3550.28 --> 3557.22]  all Change Talk podcasts. Check out what they're up to at Fastly.com and Fly.io. And to our Beat Freakin'
[3557.32 --> 3562.32]  residents, Breakmaster Cylinder, for continuously cranking out the best beats in the biz. That's all
[3562.32 --> 3564.18]  for now. We'll talk to you again next time.
