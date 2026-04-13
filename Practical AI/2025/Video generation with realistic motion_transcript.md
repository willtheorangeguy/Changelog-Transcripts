[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.46 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[26.32 --> 28.36]  Thanks to our partners at Fly.io.
[28.36 --> 31.10]  Launch your AI apps in five minutes or less.
[31.40 --> 33.40]  Learn how at Fly.io.
[45.14 --> 49.20]  Welcome to another episode of the Practical AI podcast.
[49.58 --> 51.24]  This is Daniel Whitenack.
[51.36 --> 57.90]  I am CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who
[57.90 --> 61.44]  is a Principal AI Research Engineer at Lockheed Martin.
[61.64 --> 62.34]  How are you doing, Chris?
[62.72 --> 63.38]  Doing great.
[63.48 --> 64.18]  Happy New Year.
[64.30 --> 66.40]  This is our first show of 2025.
[66.84 --> 67.64]  Happy New Year.
[67.72 --> 71.50]  Yeah, this is the first one we're recording for the year.
[71.68 --> 78.58]  First time jumping back on the mics to talk about AI, and definitely something that I think
[78.58 --> 89.54]  will be a theme in 2025, which will be, of course, multimodal AI in general, but I think something
[89.54 --> 96.64]  that a lot of people are wondering where it's going to go, I guess, in 2025, which is video
[96.64 --> 97.32]  generation.
[97.32 --> 97.76]  Yeah.
[97.76 --> 104.50]  So we're very pleased to have Paras Jain with us today, who's CEO at Genmo.
[104.68 --> 105.18]  How are you doing?
[105.54 --> 106.28]  I'm doing great.
[106.40 --> 107.28]  Happy New Year, everyone.
[107.46 --> 108.90]  It's really wonderful to be here.
[109.34 --> 110.16]  Yeah, welcome.
[110.50 --> 114.78]  I know we've been trying to make this one happen for a little while, and I think the timing
[114.78 --> 120.70]  worked out well because, like I say, people are thinking a lot about video generation and
[120.70 --> 123.40]  how that will evolve in 2025.
[123.98 --> 129.40]  Maybe from someone that's working in this area and has been thinking about it deeply,
[130.14 --> 135.26]  maybe a lot of people, listeners, have just started thinking about this topic recently,
[135.46 --> 138.84]  but you've been thinking about it deeply for some time.
[138.84 --> 145.76]  Could you give us a little bit of a sense of what happened, what led up to video generation
[145.76 --> 147.60]  and where it is in 2024?
[147.60 --> 153.78]  And then kind of as we're entering this new year, what's the current state of video generation,
[154.40 --> 159.72]  I guess, more generally in terms of what people can access in actually released systems or
[159.72 --> 160.44]  released models?
[160.88 --> 161.56]  Yeah, absolutely.
[162.10 --> 164.58]  There's been a long path to kind of where we are today.
[164.58 --> 169.88]  I think, you know, given so much excitement in what you might call the left brain of AI,
[170.06 --> 175.24]  that is like language models, reasoning, your O series of models, you know, I think the right
[175.24 --> 177.30]  brain has kind of lagged progress for quite a while.
[177.30 --> 177.70]  Right.
[177.88 --> 182.48]  Like people didn't really widely use kind of creative AI at a huge scale.
[182.50 --> 184.92]  And I think video is the ultimate creative modality here.
[185.02 --> 185.18]  Right.
[185.20 --> 190.00]  If you think about it, so much of how we communicate as humans is through visual mediums and specifically
[190.00 --> 192.06]  just video through motion.
[192.42 --> 197.30]  And so I think it's incredibly exciting in video being this ultimate form of creative
[197.30 --> 198.58]  multimodal synthesis.
[198.92 --> 203.30]  It was always really exciting, but the technology really kind of was far behind, I think, what
[203.30 --> 204.58]  people really wanted from it.
[204.58 --> 205.88]  And so it's interesting.
[205.98 --> 210.72]  My co-founder worked on some of the earliest image generation models and then 3D generation.
[210.72 --> 214.68]  And then video was always this kind of big modality we wanted to target.
[215.14 --> 220.00]  What I think was really interesting in 2023 and 2024 was first the development of the image
[220.00 --> 222.24]  generation, which is kind of a precursor to video.
[222.24 --> 226.58]  But even then, the gap from image generation models to video generation models was always
[226.58 --> 227.02]  really big.
[227.08 --> 231.18]  Because if you think about it, an image might have thousands of pixels and, you know, or
[231.18 --> 232.04]  even a million pixels.
[232.20 --> 236.04]  But a video would have, you know, hundreds of millions or even billion pixels in it in
[236.04 --> 236.92]  just a short clip.
[237.04 --> 238.98]  And so there was a huge gap to cross.
[239.40 --> 243.44]  I mean, so compute has scaled a lot and that has enabled larger models.
[243.66 --> 248.60]  And so I think, you know, top of mind since we, you know, rescheduled this podcast, Sora
[248.60 --> 249.22]  came to market.
[249.22 --> 250.44]  And I think that was really exciting.
[250.54 --> 253.96]  That was a watershed moment for a lot of people to kind of see what was possible with video
[253.96 --> 254.44]  generation.
[254.76 --> 259.24]  And to me, I think this is a really early bellwether of like, you know, what is to come.
[259.32 --> 260.64]  I think we're still really early here.
[260.94 --> 261.06]  Yeah.
[261.12 --> 263.88]  And for those that don't know, Sora is from OpenAI, right?
[264.14 --> 264.74]  Yeah, correct.
[265.20 --> 265.36]  Yeah.
[265.90 --> 273.92]  And I mean, you talk about some of the challenges with video generation being a kind of different
[273.92 --> 274.58]  animal.
[274.58 --> 281.22]  I know that some people might, you know, if they've been longtime listeners of the show,
[281.68 --> 289.38]  we've had episodes talking about kind of stable diffusion and these sorts of models for image
[289.38 --> 290.14]  generation.
[290.80 --> 299.56]  What are the main, I guess, if you want to be a video generation model builder, what do
[299.56 --> 305.88]  you have to think of differently, both in terms of kind of the type of model that you
[305.88 --> 310.66]  would use and also kind of, you know, the process that you'd have to go through in terms
[310.66 --> 313.32]  of of curating data and that sort of thing?
[313.88 --> 314.32]  Yeah.
[314.44 --> 319.22]  I mean, I think first and foremost, video data is really data intensive, right?
[319.22 --> 322.72]  Like you just think about it compared to even images or text like text is tiny.
[322.72 --> 327.52]  Images were more expensive, but video is like 100x more in terms of data volume in a short
[327.52 --> 328.76]  clip than you might have for images.
[328.94 --> 332.60]  And so when you think about training these models, that's really the most important challenge
[332.60 --> 337.54]  is how do you build architectures and then systems that can scale to process large data
[337.54 --> 337.90]  sets?
[338.38 --> 339.88]  That was a big ball neck for the community.
[340.04 --> 343.76]  I mean, again, at Genmo, we've been innovating heavily to actually make that possible.
[343.86 --> 347.60]  But I think this was why progress took a little bit longer than, say, for images or
[347.60 --> 348.56]  language to come to market.
[348.56 --> 352.92]  For companies that are training this, though, like, again, they're having to curate massive
[352.92 --> 357.96]  scale data sets easily in the, you know, petabytes of data, essentially just to pre-train
[357.96 --> 358.50]  these models.
[358.56 --> 359.46]  And that's really intensive.
[359.98 --> 362.20]  Many practitioners are beginning to fine tune these models, too.
[362.24 --> 365.20]  But even that remains more challenging than your stable diffusion, for example.
[366.06 --> 369.30]  That's got to make it hard for new entrants to come into the into the field.
[369.40 --> 375.66]  Just just the sheer volume of what you have to get set up, you know, ahead of time to handle
[375.66 --> 380.74]  that is probably be I would imagine beyond what what most organizations are really able
[380.74 --> 385.28]  to do unless they're, you know, have specific expertise or experience in the area or something.
[385.70 --> 386.26]  Yeah, absolutely.
[386.42 --> 389.00]  I mean, it took us a long time to get ready to pre-train models.
[389.18 --> 392.70]  We'll talk about this more, but we open source to one of the state of VR video generation
[392.70 --> 392.98]  models.
[393.06 --> 396.94]  And part of the goal here was to kind of let other people have a chance, right?
[397.00 --> 399.10]  Let them pick up a model and begin to fine tune it.
[399.10 --> 404.34]  And they're kind of skipping past like a massive volume of technical infrastructure they otherwise
[404.34 --> 405.60]  would have needed to have built.
[406.48 --> 412.38]  And maybe talk a little bit about that data side, because I know that this is one of the
[412.38 --> 417.46]  things that's been I mean, it has been a struggle on the tech side, but I think especially on
[417.46 --> 424.44]  the image and video side where there's a lot of questions about, hey, well, where where can
[424.44 --> 427.20]  you actually source all of this video and imagery?
[427.82 --> 431.74]  And, you know, what are the what are the rights associated with that?
[431.82 --> 438.34]  But I also imagine there's there's definite curation that's needed in terms of like all
[438.34 --> 445.34]  these prompts that that I've seen people do with like, oh, generate this, you know, it's
[445.34 --> 451.58]  shot with a Canon DSLR or whatever, like all all of that sort of thing has to be has to
[451.58 --> 454.16]  be curated on the on the prompt side as well.
[454.36 --> 455.04]  So, yeah.
[455.12 --> 460.90]  Could you could you talk a little bit about that that data curation and what the source
[460.90 --> 466.72]  of that kind of where where you could even get videos and then and then the curation process?
[467.06 --> 471.76]  Yeah, I mean, I think pre training in general, and that's true for image models, text models,
[471.88 --> 476.30]  audio models and videos, they rely on like, you know, large volumes of Internet scale data.
[476.42 --> 480.24]  But I think what's uniquely challenging with video is it's just, you know, it's easy to kind
[480.24 --> 482.00]  of get drowned out in the noise.
[482.20 --> 482.34]  Right.
[482.40 --> 486.22]  And one one angle here that I think is really interesting that we, for example, zeroed in
[486.22 --> 489.36]  on was how do we learn high quality motion with a video model?
[489.40 --> 493.20]  And it turns out the vast majority of video you find on the Internet doesn't move.
[493.30 --> 495.90]  It's like a static object or it's someone talking.
[496.02 --> 499.86]  And if you think about that, that doesn't actually teach a generative model about the
[499.86 --> 500.14]  world.
[500.26 --> 501.26]  It doesn't teach about physics.
[501.30 --> 502.98]  It doesn't teach it about how objects interact.
[503.04 --> 505.14]  And so it's not going to learn strong reasoning.
[505.14 --> 509.32]  And so the way we think about it, it's really the goal with the video model is to learn physics
[509.32 --> 512.98]  and realism and the laws that govern our world.
[513.10 --> 518.40]  And so you might think about inertia, mass, optics, you know, fluid dynamics, all these
[518.40 --> 520.72]  kind of base properties and how they all interact.
[520.86 --> 524.76]  That's really the goal with video generations to learn an engine that can simulate this because
[524.76 --> 527.36]  the output is a video and we can consume it.
[527.42 --> 528.40]  It's creative and it's beautiful.
[528.60 --> 533.50]  But the hard step here is finding data that can really help you learn these base rules of
[533.50 --> 534.62]  kind of of the world.
[534.72 --> 537.32]  And this was one of the most fundamental gaps we had across.
[538.18 --> 539.28]  It's kind of non-trivial.
[539.80 --> 544.78]  I'm kind of curious as you know, as you're describing that, I would imagine that some
[544.78 --> 548.78]  things that you're training for are harder for the model to learn than other areas.
[549.04 --> 553.50]  And that, I mean, if you think about just, you know, narrow it down to just, you know,
[553.56 --> 558.28]  animals and mammals and humans and they move differently and the, you know, the physiology
[558.28 --> 560.84]  and the anatomy is a bit different across those.
[560.84 --> 565.16]  And that all has to somehow be inferred by the model if they're going to make a video
[565.16 --> 565.90]  that's realistic.
[566.68 --> 570.02]  What have you, in your experience, as you, you know, you talked about motion being so
[570.02 --> 570.58]  important stuff.
[570.80 --> 576.20]  What are some of the harder things it's been to get right over time, not just in where
[576.20 --> 580.72]  you're at today, but like for the industry, what is the industry and maybe early on, what
[580.72 --> 581.50]  have you struggled with?
[581.76 --> 585.80]  Yeah, I think it's a really, it's kind of funny that one of the test cases people use
[585.80 --> 588.30]  now to test different video generators is gymnastics.
[588.30 --> 592.86]  And I think the reason for this, there's hilarious videos online you'll see of, of
[592.86 --> 594.92]  Sora or other video generators doing gymnastics.
[595.12 --> 598.30]  And I think one of the answers is video generation models just can't do it now.
[598.68 --> 600.42]  And it's really complex human motion.
[600.68 --> 601.72]  It's really rare.
[601.86 --> 605.62]  Obviously you talk about data curation, for example, like there isn't that much complex
[606.24 --> 606.56]  motion.
[606.62 --> 610.74]  We see people like doing twists and twirls, twirls and backflips and stuff in nature.
[610.74 --> 611.06]  Right.
[611.06 --> 615.32]  And so it's kind of interesting is like, that is, that requires fundamental understanding
[615.32 --> 620.10]  of how human kinematics behave for you to simulate that properly without it feeling disturbing.
[620.34 --> 622.78]  And so this has been one of the challenges for people.
[622.90 --> 626.30]  I mean, for example, early on when we were training, I mean, we've gone through three
[626.30 --> 629.90]  fundamental pre-training foundational models in our history of a company.
[629.90 --> 635.42]  And what's interesting with Mochi, which is our latest model in the prior one replay was
[635.42 --> 638.98]  walking was actually a really basic thing that was really hard to nail.
[639.18 --> 644.90]  It turned out most video generators early in kind of early to mid 2023, they would make
[644.90 --> 647.28]  humans kind of hover as if they're hovercrafts.
[647.34 --> 648.50]  Like their feet would not move.
[648.58 --> 650.48]  They would just kind of levitate off the ground and move.
[650.58 --> 655.06]  And so the models were not capable of synthesizing, forget gymnastics, just walking.
[655.20 --> 658.36]  And so that was one of the critical watershed moments we had to cross, for example, as a
[658.36 --> 658.68]  company.
[658.68 --> 662.50]  I would suggest that might have been some folks that had a little too much bourbon in
[662.50 --> 664.26]  their eggnog over the holidays right there.
[664.38 --> 666.22]  Kind of that floating thing going there.
[666.82 --> 673.92]  I've definitely seen the like Jedi vibe, which is kind of cool in one respect, but not that
[673.92 --> 675.38]  awesome if you don't want it.
[676.26 --> 681.20]  One thing here is I think like we've invested heavily in evaluation infrastructure at Genmo.
[681.28 --> 683.54]  And as part of it's like, how do you benchmark these capabilities?
[683.98 --> 688.46]  Like one of the test cases we have is, you know, you might have a woman drinking a glass of
[688.46 --> 691.66]  water with ice and you want to look at, hey, does the ice move realistically?
[691.66 --> 692.58]  There's a water flow.
[692.68 --> 696.80]  But also like, you know, what's interesting is once in a blue moon, like the character
[696.80 --> 700.36]  will try to drink the water through the side of the glass, which is just not physically
[700.36 --> 701.04]  consistent.
[701.44 --> 703.32]  And you'll actually see this with some of our competitor models.
[703.36 --> 705.18]  It's something we had been trying to develop.
[705.18 --> 709.84]  And I think just that isolated test case alone communicates a lot about the video generation
[709.84 --> 713.24]  models capability to just understand the laws of reality.
[713.50 --> 713.60]  Right.
[713.62 --> 715.22]  Like it's kind of, yeah, it's a Jedi mind trick.
[715.28 --> 718.22]  Like you just cannot, you should not be able to do that.
[718.32 --> 718.54]  Right.
[719.08 --> 726.58]  How, like when you're using those test cases that you've developed, is that a lot of human
[726.58 --> 732.50]  review or how, how does that, like, how do you create kind of the, the tooling around
[732.50 --> 732.78]  that?
[732.78 --> 738.64]  Because I know there's sort of like comparisons between this image and that image, right.
[738.64 --> 743.80]  And, or this frame and that frame, and you can compare closeness and all of that, but
[743.80 --> 749.14]  there could be a lot of sort of closeness in the, in the overall image.
[749.14 --> 754.52]  But if the woman is drinking from the side of the glass, there's kind of a, a major failure
[754.52 --> 758.30]  moment, even though maybe everything around is, is really good.
[758.86 --> 758.98]  Yeah.
[759.02 --> 763.54]  I mean, look, there's a, there's a, there's a lack of external publicly available quantitative
[763.54 --> 764.12]  benchmarks.
[764.12 --> 767.74]  I think one of the ones that are publicly available are there, these leaderboards or artificial
[767.74 --> 769.60]  analysis has a video generation leaderboard.
[769.66 --> 773.32]  I mean, we are the number one open source model and kind of neck and neck with closed
[773.32 --> 773.78]  models there.
[773.80 --> 775.04]  And that's just human preferences.
[775.62 --> 778.38]  Hundreds of thousands of people look at two videos side by side and they say, this one's
[778.38 --> 779.24]  better or this one's better.
[779.36 --> 781.82]  And you kind of get like an chest style ELO rating.
[781.82 --> 785.54]  And I think this has been one of the best or better public benchmarks.
[785.88 --> 789.38]  I'm, you know, internally, one of the ways we think about this though, is as we're measuring
[789.38 --> 793.50]  these capabilities, such as world understanding and physics, it's very hard for a human actually
[793.50 --> 794.28]  to rate by that.
[794.36 --> 797.70]  It turns out like when we as humans look at two videos side by side and you're saying,
[797.78 --> 798.46]  which one do you prefer?
[798.84 --> 802.42]  You often prefer the one that might have slightly higher resolution or more detail.
[802.64 --> 805.38]  But if you actually think about it, if I'm going to use this in actual production application,
[805.38 --> 809.58]  like film production or gaming or something else, like I probably actually care more about
[809.58 --> 810.02]  the motion.
[810.02 --> 815.58]  And so we actually have to override the human intuition, your first order intuition to say,
[815.66 --> 821.32]  select for detail and use these test cases as sort of like functional testing of how
[821.32 --> 822.46]  we can measure these capabilities.
[822.58 --> 825.06]  You know, I, in my career, I started out actually in self-driving.
[825.38 --> 828.56]  I worked at one of the early companies applying deep learning to self-driving perception.
[828.56 --> 832.42]  And, you know, I took a lot, I take a lot of inspiration to how we built functional safety
[832.42 --> 834.56]  testing, for example, for deep learning systems.
[834.56 --> 834.92]  Right.
[834.96 --> 838.06]  And in that way, you're going to enumerate these test cases and use cases.
[838.06 --> 842.02]  And you can actually say yes or no to you kind of pass that, that test case scenario.
[842.02 --> 842.46]  Right.
[842.46 --> 845.96]  And so, you know, whether it's a human has to do that review and we're starting to
[845.96 --> 847.22]  develop more automated metrics.
[847.22 --> 851.18]  I mean, it's just producing more structured forms of valuation, I think are really important
[851.18 --> 854.70]  because otherwise the world is just too intricate for us to test everything.
[854.70 --> 855.02]  Right.
[855.02 --> 857.84]  So we have to kind of go use case by use case and just measure progress.
[857.84 --> 861.90]  And it turns out, as you scale the models and scale the data sets, we begin to see percentage
[861.90 --> 863.14]  completion rates improve.
[863.54 --> 866.58]  And this gives us a semi-quantitative benchmark of progress.
[866.58 --> 883.04]  Well, friends, AI is transforming how we do business, but we need AI solutions that are
[883.04 --> 886.24]  not only ambitious, but practical and adaptable too.
[886.48 --> 889.86]  That's where Domo's AI and data products platform comes into play.
[889.86 --> 893.14]  It's built for the challenges of today's AI landscape.
[893.14 --> 897.80]  With Domo, you and your team can channel AI and data into innovative uses that deliver
[897.80 --> 898.96]  measurable impact.
[899.36 --> 904.10]  While many companies focus on narrow applications or single model solutions, Domo's all-in-one
[904.10 --> 909.88]  platform is more robust with trustworthy AI results without having to overhaul your entire
[909.88 --> 910.70]  data infrastructure.
[911.28 --> 915.64]  Secure AI agents that connect, prepare, and automate your workflows.
[915.64 --> 921.22]  Domo's helping you and your team to gain insights, receive alerts, and act with ease through guided
[921.22 --> 922.78]  apps tailored to your role.
[922.96 --> 925.70]  And the flexibility to choose which AI models you want to use.
[926.08 --> 927.74]  So Domo goes beyond productivity.
[928.30 --> 932.30]  It's designed to transform your processes, helping you make smarter and faster decisions
[932.30 --> 933.60]  that drive real growth.
[933.76 --> 940.46]  And it's all powered by Domo's trust, flexibility, and years of expertise in data and AI innovation.
[940.92 --> 943.80]  And of course, the best companies rely on Domo to make smarter decisions.
[943.80 --> 946.46]  See how Domo can unlock your data's full potential.
[947.00 --> 950.54]  Learn more at ai.domo.com.
[950.60 --> 954.06]  That's ai.domo.com.
[958.44 --> 966.76]  So Paras, I'm wondering, you mentioned this kind of history of pre-training at Genmo and
[966.76 --> 971.60]  the most recent model, which of course we want to talk about, but I'm sure that that most recent
[971.60 --> 977.58]  model is informed by things that you tried in the past and kind of your history there.
[977.78 --> 983.76]  So could you give a little bit of a snapshot of kind of the history of your team and how
[983.76 --> 990.60]  they approached this problem, how you all approached this problem, and the kind of generations that
[990.60 --> 992.02]  you went through with that?
[992.48 --> 992.92]  Absolutely.
[992.92 --> 993.04]  Absolutely.
[993.70 --> 996.30]  So we're just about two years old at this point.
[996.42 --> 999.68]  We actually started working on the company Christmas 2022.
[1000.28 --> 1000.98]  So it was a holiday.
[1001.50 --> 1005.14]  And Jay and I were both the co-founders of the company.
[1005.42 --> 1006.50]  First and foremost, we're brothers.
[1006.74 --> 1007.74]  I think that's really unique.
[1008.20 --> 1008.70]  That's awesome.
[1009.52 --> 1012.00]  And we didn't really plan to start a company with brothers.
[1012.08 --> 1012.76]  I mean, it's a little weird.
[1012.86 --> 1016.12]  I mean, normally you have sibling rivalries and things like that.
[1016.16 --> 1016.50]  I don't know.
[1016.60 --> 1017.44]  We didn't have much of that.
[1017.50 --> 1019.80]  But it turned out our skill sets were super complementary.
[1019.80 --> 1021.92]  Both of us were doing our PhDs in UC Berkeley.
[1022.12 --> 1027.20]  I was working on large-scale distributed systems in the UC Berkeley AMP lab and RISE lab.
[1027.22 --> 1032.98]  And this is the same lab that created Apache Spark and Ray and the AnyScale project.
[1033.16 --> 1037.24]  And so really hardcore machine learning systems for scaling large language models.
[1037.32 --> 1039.28]  That was what my dissertation topic was on.
[1039.46 --> 1043.78]  And concurrent to that, Jay was working on the foundations of modern image generation.
[1044.12 --> 1049.06]  So he had joined Berkeley to work on early image generation models.
[1049.06 --> 1050.64]  This is kind of like in your GAN era.
[1051.64 --> 1057.16]  And I think for him, one deeply unsatisfying thing was a generative adversarial network was like a mirage.
[1057.24 --> 1061.50]  It wasn't actually like a grounded loss objective that was learning real motion or dynamics.
[1062.14 --> 1066.06]  It kind of was like this game, but you got image generation and side artifacts.
[1066.06 --> 1078.72]  So I think his story was really interesting in that he ended up kind of writing his paper, DDPM, or the Denoising Diffusion Propolistic Model paper, which is one of the foundations for how we think about image generation with diffusion today.
[1078.88 --> 1081.32]  It's one of the most highly cited papers in this area.
[1081.38 --> 1093.98]  And that came from, I think, early inclination that how do we build video image models that understand physics and realism instead of just kind of like artificially playing this game that results in image generation, grounding it in real generative pre-training.
[1093.98 --> 1097.48]  And so that's some of the early academic history of the company.
[1097.58 --> 1102.60]  But starting the company, we decided to do video because, like, it seemed impossible back in 2022.
[1103.28 --> 1105.30]  It was just completely outside the frontier.
[1105.30 --> 1108.42]  And we said, fundamentally, we need a new architecture to solve this.
[1108.84 --> 1115.92]  And so let us discover both from a systems perspective and distributed systems perspective, but also machine learning perspective, what the right approach to do that is.
[1116.30 --> 1118.42]  I mean, so, yeah, it's been about two years since founding.
[1118.42 --> 1127.40]  We've gone through three large pre-training runs, and in each time we learn something new about the world and integrate that into our approach and our framework and architecture for how we train these models.
[1127.68 --> 1130.46]  I think the single underpinning thing, though, is motion.
[1130.66 --> 1137.84]  We always joke, like, Genmo doesn't really have an explanation, but we kind of retroactively apply this idea of generative motion, right?
[1137.94 --> 1141.06]  Genmo is like, we care so much about motion and video.
[1141.06 --> 1146.40]  So that's really a core element of our founding history and our framework for how we approach video generation.
[1146.94 --> 1151.98]  I'm wondering, you got me, I had a question for a moment or two as you were talking through it.
[1152.02 --> 1162.52]  You kind of talked about that evolution and, you know, kind of starting with GANs, the generative adversarial networks, and finding your way across kind of the architectural progression that you guys have found.
[1162.52 --> 1172.18]  Could you talk a little bit about that in terms of, like, you know, if you were coming into it during, you know, the age of GANs right there, and that was the thing.
[1172.36 --> 1176.66]  But, you know, what did, I'm kind of curious, like, at high level, what was the problem with that?
[1176.82 --> 1178.26]  Why did that not work for you?
[1178.32 --> 1179.48]  What did you look to next?
[1179.78 --> 1188.12]  You know, could you kind of give us kind of a highlight, skip over the top of a couple of different major architectural twists and turns to give us a sense of what your journey might have been like?
[1188.12 --> 1195.84]  Yeah, so I think the earliest form of image generation models that I think started to work well were autoregressive image generation models.
[1195.98 --> 1197.88]  So this is very similar to a large language model.
[1198.50 --> 1203.82]  You kind of take a, you know, you might take an image and you make it a single vector, a line.
[1203.90 --> 1209.28]  So if it's like, you know, 28 by 28 image, now you have 784 pixels in a straight line.
[1209.28 --> 1212.26]  And you just go one by one by one and decode the next one.
[1212.32 --> 1214.22]  So that was the earliest form of image generation.
[1214.22 --> 1221.62]  There were models like Pixel RNN or Pixel CNN or Image GPT, which were from OpenAI, which were the earliest works here that worked well.
[1222.00 --> 1224.48]  But the problem is, like, images have millions of pixels.
[1224.62 --> 1227.24]  This would never scale to produce high resolution images.
[1227.78 --> 1236.96]  I think what's interesting from when Ajay was working on this, like, early on in 2018, 2019, was I think I remember he trained an autoregressive image generator model.
[1237.00 --> 1241.78]  And the first models he trained were trained on, like, L-Sun, which is a data set of bedrooms, basically.
[1241.78 --> 1246.54]  But what was so interesting is that it would be like a little 5 by 5 or 10 by 10 pixel region.
[1246.74 --> 1250.00]  It would start to put artwork on the background of people's bedrooms.
[1250.62 --> 1252.70]  Why? Because that's just like what nature looks like.
[1252.74 --> 1254.22]  That's what real estate listings look like.
[1254.54 --> 1260.04]  But it was the first indication of AI generated art in some sense with an early image generation model.
[1260.30 --> 1264.16]  The problem is this would not scale, right, because you're kind of going pixel by pixel by pixel.
[1264.48 --> 1266.32]  So it would take hours to make a small image.
[1266.88 --> 1269.34]  I mean, so GANs were the next kind of major approach.
[1269.34 --> 1271.22]  I think that really worked well for this.
[1271.74 --> 1274.92]  And GANs are trained, again, with this, like, general adversarial objective.
[1274.92 --> 1278.24]  It's kind of this, like, dueling game between a generator and a discriminator.
[1278.34 --> 1279.66]  But they were really hard to train.
[1280.16 --> 1286.42]  It turned out they were getting these bad, you know, states where, you know, you might get, like, mode collapse, for example, was one of the biggest issues.
[1286.58 --> 1289.32]  It would mean you could produce images of, like, a single domain.
[1289.32 --> 1292.16]  But you couldn't, like, produce everything in the world with the GAN.
[1292.50 --> 1299.38]  So you could get a really good model for making faces or a really good model for making, you know, bedroom pictures or making a really good model of, like, tigers.
[1299.80 --> 1306.46]  But it was really hard to, say, train a model on all of ImageNet, meaning cover thousands or thousands of different categories, right?
[1306.46 --> 1314.50]  And so diffusion models was a really exciting approach that Jay began to work on because it had the potential to provide that kind of mode coverage.
[1315.14 --> 1322.10]  You could learn diverse representation of the world that generalized beyond just a single domain, like faces or animals, to everything.
[1322.40 --> 1325.80]  And so, you know, that was what kind of resulted in DDPM.
[1325.80 --> 1331.68]  And I think since then, I mean, you've had latent diffusion, the stable diffusion approach, and then video generation is, I think, the next major evolution.
[1331.94 --> 1341.66]  But the learning paradigm has mostly remained similar to this, like, learning through this, like, you know, diffusion setup or kind of iterative denoising, right?
[1341.70 --> 1343.34]  This is the formulation of this diffusion problem.
[1343.34 --> 1354.82]  But, like, it's remarkable to see how far that has scaled, like, literally 10,000x in pixel scale from the earliest diffusion models to kind of where we are with video generation.
[1355.80 --> 1372.22]  I guess on that front, like, how did you decide, I guess, because I know that part of what you've done, and I'm assuming what the intention was with the models that you've created, is to open source them in one way or another.
[1372.48 --> 1379.90]  And as you mentioned earlier, release things into a community where people could experiment and try things and fine tune.
[1379.90 --> 1398.56]  How did you think about kind of size of the model and that sort of, was that kind of purely driven by what was needed to produce kind of a certain size of video or a certain resolution, a certain kind of performance metric that you were after?
[1398.78 --> 1405.40]  How did you make some of those, I guess, trade-off decisions, maybe also the compute that you had access to?
[1405.40 --> 1405.88]  Yeah.
[1405.88 --> 1406.16]  Yeah.
[1406.32 --> 1408.78]  I mean, first of all, pre-training is incredibly GPU intensive.
[1408.94 --> 1413.68]  I mean, we have access to more than 1,000 of H100 grade GPUs.
[1413.76 --> 1415.82]  And so, I mean, that is incredibly GPU intensive.
[1415.82 --> 1419.28]  But I think it's also a question of how you utilize that hardware effectively.
[1419.42 --> 1423.52]  And one of the critical challenges with video is they have really long sequence lengths.
[1423.88 --> 1430.66]  Like, training a video generation model is equivalent to kind of training a million token length kind of context window for a new language model.
[1430.66 --> 1438.58]  And so, this introduces a huge set of challenges that are kind of orthogonal to kind of parameter scalings you might see typically with large language models.
[1439.10 --> 1443.74]  What I think is interesting is, though, certain capabilities only emerge at certain parameter scales.
[1443.88 --> 1445.02]  So, like I talked about walking.
[1445.22 --> 1452.16]  Like, it's very difficult to get walking to work with like a, you know, a one or two billion parameter model or something smaller than that.
[1452.22 --> 1454.64]  It just like, you won't learn that capability.
[1454.84 --> 1457.04]  So, you do need a certain amount of scale for it to work.
[1457.04 --> 1463.82]  But at the same time, you're not seeing models that are like 100 billion or trillion parameter scale, as you see kind of with the frontier grade language model.
[1463.94 --> 1465.54]  So, we open source Mochi1.
[1465.90 --> 1468.38]  It's a 10 or 11 billion parameter scale model.
[1468.50 --> 1472.82]  So, it's a lot bigger than your conventional grade, older grade of video generation models.
[1472.92 --> 1475.82]  But it, again, still is runnable on a consumer grade GPU.
[1476.14 --> 1477.52]  People can access it and they can use it.
[1477.80 --> 1485.02]  That was a very intentional choice by us to kind of right size it for the community while making sure it wasn't too small to limit its capabilities.
[1485.02 --> 1502.76]  And what reasonably, I know one of the things that I've noticed over time as I've experimented with different video generation, either demos or products, there's definitely an element of it to where you can only generate so much.
[1502.76 --> 1513.66]  I'm imagining that there, as you mentioned, there's a sequence that is being generated and in a way similar to a sequence that's generated out of a language model.
[1514.22 --> 1522.12]  There's iteratively or iterations of calling the model, which is more compute intensive the more you generate.
[1522.12 --> 1525.60]  Is that a true assumption about video models?
[1525.80 --> 1537.66]  Or is there, I think people are somewhat familiar, at least if they've been around the podcast or have done their own research in terms of how language models generate tokens, right?
[1537.74 --> 1539.12]  So, I have a prompt.
[1539.34 --> 1541.46]  The model generates a token.
[1542.10 --> 1544.42]  And then that's added to my prompt.
[1544.54 --> 1546.86]  And then I iteratively generate another token.
[1546.86 --> 1552.30]  And so, the model is being called the more that I'm generating.
[1552.70 --> 1557.30]  Is that same thing true for kind of generating these sequences of videos?
[1557.50 --> 1564.60]  What are the kind of concerns around actual compute and usage of these models in a realistic environment?
[1565.06 --> 1569.92]  Yeah, I think video generation models share common elements with large language models, but they also differ in some key ways.
[1570.06 --> 1575.78]  So, first and foremost, a language model decodes tokens autoregressively, one at a time.
[1575.78 --> 1586.20]  So, if you want to generate, you know, a thousand tokens, however many, like whatever, let's say 500 words, you need to do 500 forward passes or a thousand forward passes of the model.
[1586.70 --> 1590.66]  In a video generation model, like every pixel is kind of generated at once.
[1590.66 --> 1596.06]  So, each forward pass produces all of the pixels that you see in your video across space and time.
[1596.06 --> 1598.34]  And we do multiple denoising steps.
[1598.42 --> 1606.90]  So, you start with a kind of a pure noise sample and through maybe 50 or 100 forward passes, all of those pixels eventually become full resolution.
[1607.04 --> 1613.48]  So, you'll actually see if you use our product, we stream those pixels as they're getting denoised in real time to your browser.
[1613.60 --> 1616.40]  So, you'll see a full video, like not just a frame, but a full video.
[1616.40 --> 1617.54]  But it's kind of blurry.
[1618.08 --> 1622.48]  And slowly, the video gets sharper and sharper and the details begin to resolve.
[1622.60 --> 1630.18]  Like you'll see blobs that become more and more detailed and eventually you get fine details like hair or teeth or, you know, plant leaves and so on.
[1630.28 --> 1632.26]  Like that appears in the last stage of this.
[1632.36 --> 1639.30]  And similarly, the motion might start with coarse grain motion, but eventually becomes much more detailed and realistic as the denoising process proceeds.
[1639.30 --> 1644.78]  So, it's kind of a different axis in which we do the compute, like just like you do tokens and decoding.
[1644.96 --> 1646.98]  Like in video models, you have this denoising step.
[1647.38 --> 1653.50]  But one really important thing to talk about architecturally, at least with Mochi as we open source it, is it's kind of a multi-stage model.
[1654.12 --> 1659.96]  There's first what we call this variational autoencoder, or VAE, which refers to essentially video compression.
[1660.44 --> 1664.18]  There's just too many pixels on video for us to learn over natively in the model.
[1664.34 --> 1666.14]  It's just way too expensive.
[1666.14 --> 1677.42]  So, in Mochi, we train this 100x video compression model through the variational autoencoder setup that takes the input video and actually projects and makes that sequence that we talk about.
[1677.94 --> 1687.02]  So, you're going from something that's like, you know, hundreds of millions of pixels or something down to something that ends up effectively taking about, you know, 50,000 tokens equivalent.
[1687.34 --> 1689.92]  50,000 to 100,000 tokens equivalent in a language model.
[1689.92 --> 1696.40]  So, we do that compression stage first, and then in that latent space, that is actually what the diffusion model is learning, right?
[1696.44 --> 1703.50]  So, that 10 billion parameter model is learning to kind of reconstruct, you know, that 100x downsampled or compressed space.
[1704.12 --> 1712.40]  Do you envision that there's ever a point, you know, with compute, you know, growing so fast, is there ever a point where you think compression will no longer be needed?
[1712.40 --> 1721.24]  And you'll be able to do, you know, very large and detailed videos without the need for that, just because compute is so available in the future?
[1721.46 --> 1725.72]  Or do you think that's unlikely and we're going to keep chasing it with compression and doing other things?
[1725.72 --> 1730.60]  So, there was the first diffusion models actually were what we would call pixel space models.
[1730.74 --> 1732.60]  So, they were done at the full resolution of the sequence.
[1733.18 --> 1735.04]  And so, this is actually still doable for images.
[1735.56 --> 1744.36]  I think what's interesting is that this, like, latent diffusion setup has outperformed the pixel space approach, even in images where it is feasible computationally to still do that.
[1744.76 --> 1752.20]  You know, I think it is interesting, though, because, like, there has been a lot of hybridization of architectures between, like, auto-aggressive setups and diffusion setups.
[1752.20 --> 1757.10]  That was one trend that, like, for example, our team went to Neurips this year, in 2024.
[1757.52 --> 1764.44]  And, you know, several people have begun to explore combining different elements of auto-aggressive models, diffusion models, both in pixel space and latent space.
[1764.82 --> 1769.12]  I think it's, like, a really diverse space that, like, is just extremely underexplored.
[1769.46 --> 1773.54]  For example, when we open source Mochi, we actually developed a new architecture.
[1773.54 --> 1775.54]  We called it the Asymdit or Asymmetric Dit.
[1775.70 --> 1778.72]  It was just an evolution on the kind of area that people were in.
[1778.72 --> 1782.34]  I mean, people leveraged this diffusion transformer setup for the architecture.
[1783.12 --> 1784.36]  It's part of why it's so expensive.
[1784.50 --> 1788.18]  But, you know, we began to take some early steps to do architectural exploration.
[1788.32 --> 1795.54]  So I hope we can eventually, long story short, like, find some global optima between compression and the actual generation part.
[1795.94 --> 1797.96]  Today, we kind of factorize it for computational reasons.
[1797.96 --> 1801.56]  And I think it will just get more and more blurry as we kind of combine these different elements.
[1801.56 --> 1801.66]  Thanks.
[1809.16 --> 1812.06]  Well, Peraz, you've mentioned Mochi.
[1812.88 --> 1820.04]  Would, you know, this is the latest wave of what you have created at Genmo.
[1820.48 --> 1826.86]  Could you talk a little bit about Mochi in relation to previous models and also Mochi?
[1826.86 --> 1834.20]  I mean, you mentioned that Mochi is achieving kind of top performance on certain benchmarks.
[1834.38 --> 1847.74]  Could you kind of help us understand where it fits into the ecosystem of video models out there and also kind of what it represents to you all in kind of progression from your last generation to this generation?
[1847.74 --> 1852.20]  First and foremost, before I dig into this, my belief is video generation is super early.
[1852.32 --> 1853.68]  I think we're 1% of the way there.
[1853.82 --> 1856.58]  So I think people look at this stuff and it's really surprising.
[1856.70 --> 1860.82]  But there's a huge gap between reality and where the state of video generation is, right?
[1860.90 --> 1869.68]  And I think that mindset is really important because when we looked at the field of video generation as of, you know, mid-2023, when we kind of had our last generation model.
[1869.68 --> 1878.16]  Sorry, mid-2024, when we had our last generation model replay, was they would synthesize high resolution videos, but they just wouldn't move.
[1878.32 --> 1879.78]  They weren't that interesting, right?
[1879.82 --> 1882.74]  So you would see a video of a person and they would just stand there.
[1882.96 --> 1884.62]  And maybe there was camera motion.
[1884.78 --> 1889.40]  So the camera would kind of orbit the person or pan a little bit, but the subject wouldn't be moving.
[1889.52 --> 1896.30]  And to us, that would indicate some kind of learning failure with the video generation setup as of kind of the last generation of these models.
[1896.30 --> 1903.80]  And so that was, first and foremost, the most important thing we wanted to solve for video generation was solve motion and subject motion specifically.
[1904.58 --> 1914.30]  And so Mochi, one is kind of neck and neck with the latest frontier grade kind of closed source models, your Google Veos or, you know, Sora isn't that way, specifically by motion benchmarks, actually.
[1914.48 --> 1920.10]  And I think this is really important and subtle, but that was kind of the key component we wanted to solve with video generation.
[1920.10 --> 1925.84]  The second one that was really important for us to solve in Mochi was prompt adherence.
[1926.38 --> 1927.32]  It was really common.
[1927.42 --> 1929.26]  I think many people have this experience with video generation.
[1929.26 --> 1931.84]  As you say, I want X, right?
[1932.14 --> 1940.08]  Like you might say, you know, I want, you know, a classic test for this is, you know, like I want a dog wearing a hat holding a teacup.
[1940.30 --> 1945.06]  But it'll make that, but the order of those things and the composition of those elements is wrong, right?
[1945.48 --> 1948.22]  So they might be sitting next to it, but not holding it.
[1948.22 --> 1951.72]  But we talked to a user in user study about video generation.
[1951.86 --> 1956.38]  They described the state of video generation was kind of like pushing on a rope.
[1956.66 --> 1960.34]  You kind of want the rope to go one way, but you just can't get it to go, right?
[1960.38 --> 1961.78]  It's just really hard.
[1961.96 --> 1965.40]  And so with Mochi, we also invested heavily in prompt adherence in addition to motion.
[1965.66 --> 1972.10]  And so prompt following is, I think, a really important element that will be critical to make these systems practically usable.
[1972.48 --> 1977.70]  We'd love to talk about, like, you know, we open source this also because there was no good open model, let alone close.
[1977.70 --> 1984.86]  There were a few of these closed models, you know, Runway and Sora had been kind of previewed in their blog for several months.
[1984.98 --> 1988.44]  But nobody had actually trained and released an open model.
[1988.56 --> 1989.98]  And so that was holding this field back.
[1990.14 --> 2000.08]  And because we're so early, our viewpoint is releasing this model and creating this bedrock foundation for people to actually do the research on aspects like motion and prompt adherence was going to be critical for the field.
[2000.14 --> 2003.68]  And it benefits us as a company because people are building on top of our models, right?
[2003.68 --> 2003.72]  Right.
[2004.20 --> 2007.32]  So what kinds of things are you seeing people want to do with the model?
[2007.54 --> 2012.40]  And what are of the different categories of use cases, you know, that people might be addressing?
[2012.70 --> 2014.58]  What are the ones that are the high value?
[2015.14 --> 2015.34]  Yeah.
[2015.56 --> 2018.02]  I think everyone's first experience is just play.
[2018.14 --> 2021.12]  So, like, people just want to open it up and they want to see something wild, right?
[2021.16 --> 2024.04]  Like a baby riding a dog, right?
[2024.04 --> 2031.22]  And so I think that was always a funny one that was like, you know, you might have these things that just don't happen in the real world that you want to see the model do.
[2031.36 --> 2034.02]  And so people start with that and explore the surface area.
[2034.26 --> 2042.58]  But when we look at actual real use cases, I think what's really interesting is this video generation technology is beginning to work its way into, like, enterprise content creation workflows.
[2042.68 --> 2046.70]  And I think of this as, like, creation and then there's, like, editing, right?
[2046.76 --> 2050.02]  And these are two kind of halves of practical application of video generation.
[2050.02 --> 2057.50]  So creation, I mean, first and foremost, like, many people are starting to begin to explore using video generation as a substitute for stock video.
[2057.98 --> 2064.10]  Like, if you can't find exactly what you want in a stock catalog, you can just go generate it and it's going to come with all the right adequate licenses.
[2064.34 --> 2066.04]  It's exclusive to you, right?
[2066.38 --> 2068.52]  No one else gets that video because you made it, right?
[2068.58 --> 2069.66]  And it's N equals one.
[2070.08 --> 2072.82]  And so that's actually really powerful for a lot of content creation workflows.
[2073.32 --> 2076.30]  Video is just really hard and expensive also to iterate with, right?
[2076.30 --> 2080.96]  You shoot it once and if it's not perfect, you know, you might want to re-prompt and re-edit it.
[2081.04 --> 2087.26]  And so I think that's an exciting application, for example, in the brainstorming and pre-visualization and storyboarding process of content production.
[2087.54 --> 2090.92]  That goes way faster if you have a tool like a video generator in the loop.
[2091.08 --> 2091.82]  And then editing.
[2091.96 --> 2101.28]  Actually, that's exactly where I was about to go was on the editing is kind of how does that, how do you envision that fitting in as that becomes a problem that people are attacking aggressively?
[2101.28 --> 2107.46]  What does it mean to edit video, you know, in the context of video generation?
[2108.00 --> 2112.92]  You know, if you're generating the video from scratch, what does it mean to edit a video like that?
[2113.08 --> 2114.62]  And how might that be done?
[2114.70 --> 2116.58]  Is anyone really thinking about that right now?
[2116.68 --> 2117.90]  Is that on the table?
[2118.46 --> 2120.12]  So we released Mochi 1 as open source.
[2120.22 --> 2121.58]  We didn't know what people would use it for.
[2121.76 --> 2127.26]  And one really exciting thing, within two weeks of open sourcing it, one of the community members built this workflow called Mochi Edit.
[2127.26 --> 2130.62]  It's a full video editing pipeline built on top of our open source model.
[2130.82 --> 2133.66]  And with it, you can add, remove, or change an object.
[2133.82 --> 2134.76]  So it's a crazy video.
[2135.22 --> 2136.86]  You can search up Mochi Edit on GitHub.
[2137.12 --> 2144.16]  And what was the demo that I think he showed me that was really cool is they took a video of a person talking and they said, give him a hat.
[2144.22 --> 2148.56]  And it actually put in a fully realistic, exactly 3D tracked hat on him.
[2148.68 --> 2150.00]  Just look totally realistic.
[2150.00 --> 2159.00]  And I think that full process with the conventional video editing pipeline between tracking and rendering and compositing everything would have taken like, you know, two, three weeks, honestly.
[2159.96 --> 2160.28]  Very cool.
[2160.80 --> 2176.48]  Do you see, I mean, I know there's certain, if I remember right, Coke did like a commercial, Coca-Cola did a commercial for their winter advertisement with Gen AI.
[2176.48 --> 2190.72]  Do you think we'll, this is maybe a wider question, but how do you think people kind of in 2025, you know, how are we going to experience video generation kind of at the general public level?
[2190.82 --> 2198.92]  Do you think it will start to, like, in what ways will it start to filter into people's everyday lives?
[2198.92 --> 2207.86]  Because I, Chris and I, well, everybody remembers, like, we are talking about lots of language models before ChatGPT on the, on the podcast.
[2207.86 --> 2211.96]  But, you know, we weren't talking about them at Thanksgiving dinner, right?
[2212.40 --> 2213.00]  No, not at all.
[2213.26 --> 2220.34]  And so you do have those moments of like the Coca-Cola video where people were talking about this more widely.
[2220.34 --> 2225.70]  But that's probably not like the ChatGPT moment of video generation.
[2226.04 --> 2233.38]  Any thoughts on kind of how general public will kind of start to intersect with this technology in the coming year?
[2234.12 --> 2238.40]  I mean, I think the early adopters are certainly here for video generation.
[2238.58 --> 2242.90]  I mean, our platform has more than, well past more than 2 million users who use it just beyond open source.
[2242.98 --> 2245.66]  And open source is probably some, many multiples of that.
[2245.66 --> 2250.14]  But I think that still represents this, like, drop in the bucket compared to conventional media.
[2250.28 --> 2254.86]  And I think one of the biggest limiters, like I shared, was, like, your ability to control it.
[2254.98 --> 2260.14]  And, like, you know, once you can actually get something out of it, the wow moment is almost instant.
[2260.28 --> 2263.72]  Like, you'll ask it for something that just couldn't exist in the real world and you see it in front of your eyes.
[2263.76 --> 2267.52]  I mean, that is a jaw-dropping experience for most people, right?
[2267.52 --> 2275.28]  But I think the hard part there is the tech has required too much expertise with prompting and understanding of how to actually get good results of the model to make it usable.
[2275.66 --> 2284.54]  I think 2024 is the year that we will see, you know, instruction following and prompted here and solved here that makes this stuff actually follow what you want to say.
[2284.78 --> 2298.16]  And I think of this as, like, going from GPD3, which was just, like, an unaligned language model in some sense, which kind of would ramble about whatever topic at end, but not in a particularly useful way towards chat-based instruction tuning, right?
[2298.16 --> 2300.34]  That was the breakthrough moment for language models.
[2300.44 --> 2307.18]  I think very similarly for video models, it kind of comes to the moment where, like, somebody can pick it up and use it without being an AI expert.
[2307.70 --> 2315.14]  You know, today, many people are already talented and mid-journey or other kind of conventional forms of image generation that kind of translate into video.
[2315.14 --> 2321.24]  And I think this is really one of the critical moments that has to be solved for this to have, like, breakout exposure.
[2321.24 --> 2331.30]  But, I mean, I just imagine a world, like, I think in five years, we're going to hit a point where, you know, there might be a poor kid in Mumbai or Kenya or something who just has a phone and a good idea.
[2331.76 --> 2334.78]  Push the button on their phone and it wins an Academy Award, right?
[2334.84 --> 2336.82]  Like, that's going to change the world.
[2336.92 --> 2338.86]  And I don't think we're that far from that, to be honest.
[2338.86 --> 2347.64]  Yeah, I think that there's, I love how you've framed that in that kind of expanded agency sort of way.
[2347.78 --> 2357.82]  So instead of, like, AI models generally, I think the way people think about them as a bummer is like, oh, these things are going to automate everything.
[2358.00 --> 2364.78]  Every video I'm going to see, I'm never going to see cool videos again because they're all going to be AI generated without creativity.
[2364.78 --> 2375.82]  But I think the fact that, you know, what we're seeing with language models, what we've seen even with image generation is there's so much creativity that the human can bring into that.
[2376.06 --> 2390.48]  But it also democratizes a lot of potential, you know, production and that sort of thing to those that have amazing ideas, but maybe not access to a Hollywood film crew, right?
[2390.48 --> 2404.46]  So I love that there's still that element in kind of your vision of that human agency being expanded upon and even, you know, people getting to tell stories that maybe they wouldn't otherwise.
[2404.76 --> 2406.16]  So I love that.
[2406.60 --> 2407.94]  I've got a question for you.
[2408.02 --> 2411.18]  It's a little bit of a random one, but interesting.
[2411.56 --> 2412.96]  You know, people ask me this a lot.
[2412.96 --> 2420.20]  What does creativity mean as we go forward, as we're having these tools and, you know, human creativity is coming to bear?
[2420.46 --> 2425.22]  You're having these tools that, you know, some people consider them creative in a sense.
[2425.34 --> 2426.30]  Some people don't and all.
[2426.36 --> 2428.20]  But what does that look like?
[2428.26 --> 2434.52]  What is that that person and a tool together going and doing that that thing that Kenyan boy is doing?
[2434.82 --> 2436.46]  How do you think about that?
[2436.54 --> 2438.26]  Like, how do you contextualize that?
[2438.26 --> 2444.12]  You know, I think human ingenuity and creativity is the root of all, like, interesting form of content.
[2444.28 --> 2448.42]  Like, if you have AI, like, I know people are scared, hey, AI is going to automate all this stuff.
[2448.48 --> 2455.36]  But if you if you look at what, like, LLMs will just ramble on about, it's just like the aggregate average of all their training inputs.
[2455.40 --> 2458.06]  And that's not particularly interesting or novel to anybody, right?
[2458.08 --> 2462.92]  Like, I think the greatest films come from someone with a new idea, right?
[2463.00 --> 2464.46]  And a new lens on the world, right?
[2464.46 --> 2468.14]  A new interpretation of what it means to be human, right?
[2468.14 --> 2470.38]  And live in the world that we do.
[2470.52 --> 2473.04]  And and from that, you have great media, right?
[2473.12 --> 2473.86]  There's some some.
[2474.20 --> 2476.88]  And I think that will forever be true.
[2476.96 --> 2479.88]  The human's role here is always going to be pushing the frontier.
[2480.02 --> 2486.36]  I mean, language models learn and video models learn by just averaging and aggregating, compressing all the information around them.
[2486.38 --> 2489.48]  But in some sense, they won't ever be able to really push the frontier alone.
[2489.48 --> 2494.00]  Like a human plus now a video model, though, is something an entirely different beast, right?
[2494.26 --> 2498.02]  Now you have something I like to term creative amplification as possible, right?
[2498.14 --> 2500.38]  Like the human alone is producing the creativity.
[2500.38 --> 2508.74]  But with that video model, it now amplifies in such a way that just wouldn't have ever been possible with this old older older generation media in the older world, right?
[2508.74 --> 2514.98]  Like that iteration cycle might have taken years, an entire lifetime to kind of go through and discover an idea space.
[2514.98 --> 2522.48]  And now somebody can do that, you know, within a matter of like months or weeks, just just iterating on new ideas and testing them out and seeing them visualize for them.
[2523.04 --> 2528.70]  I guess that kind of leads us naturally into that was a great kind of vision wider.
[2528.92 --> 2532.44]  But what is your vision for for Genmo specifically?
[2532.74 --> 2536.12]  What what's kind of what what keeps you up at night?
[2536.12 --> 2542.28]  What are you most excited about kind of as you move into a new year with with a lot of new possibilities?
[2542.90 --> 2548.82]  So I think our vision has been very consistent over a long period of time, which is to build frontier models of video generation.
[2548.82 --> 2552.16]  But the goal was to unlock the right brain of artificial general intelligence.
[2552.48 --> 2553.78]  It's completely neglected.
[2553.78 --> 2557.24]  I mean, open AI and kind of these frontier models have taken over the left brain.
[2557.24 --> 2562.74]  And we said, hey, this this other side is just as capable and just as important as left brain here.
[2562.88 --> 2568.28]  And so, you know, I term that is like thinking imagine AI that can say anything possible or impossible.
[2568.28 --> 2576.48]  Right. And I think the first step here is creativity is media people creating like, you know, you know, like I described this vision of empowering creators.
[2576.48 --> 2583.52]  But like longer term, I actually think this is really interesting in that if we can explore this world of synthetic realities, it'll unlock huge progress.
[2583.52 --> 2589.02]  And, you know, I think like embodied AI, for example, and that's when this text starts to become really powerful.
[2589.02 --> 2591.78]  Right. Like I started in self-driving my career.
[2591.86 --> 2594.40]  And the big problem is there's too many edge cases to simulate.
[2594.98 --> 2599.10]  Right. And then even if you get millions of miles on the road, there's still new things that will happen.
[2599.32 --> 2609.64]  But but I think for the first time, a video model will enable training robust agents that can operate in the real world and actually understand all the possible realities that they can just simulate through that.
[2609.64 --> 2618.08]  Right. Like that's that's an entirely new paradigm that I think we're starting to see explored, even in the reasoning with the 01 style of models as well.
[2618.14 --> 2623.60]  But to me, that's that's one of the most exciting long term tenure potentials that we'll see for video generation.
[2623.60 --> 2626.56]  And and we at Genma are kind of like trying to work towards that future.
[2626.56 --> 2630.74]  Well, thank you for how you're digging in in this space.
[2630.90 --> 2642.40]  It is truly inspirational and really appreciate you taking time to chat with us as you head into head into those innovations and exciting stuff.
[2642.64 --> 2648.12]  Please come back when you release whatever whatever the next the next is.
[2648.22 --> 2650.64]  You're welcome back to to chat about it.
[2650.72 --> 2652.22]  Thank you so much, Paras.
[2652.26 --> 2653.40]  It's great to chat.
[2653.68 --> 2654.28]  Thank you, Daniel.
[2654.28 --> 2654.82]  Thank you, Chris.
[2656.56 --> 2662.86]  All right.
[2663.22 --> 2665.04]  That is our show for this week.
[2665.04 --> 2671.36]  If you haven't checked out our ChangeLog newsletter, head to changelog.com slash news.
[2671.72 --> 2673.82]  There you'll find 29 reasons.
[2674.04 --> 2677.24]  Yes, 29 reasons why you should subscribe.
[2677.80 --> 2679.24]  I'll tell you reason number 17.
[2679.82 --> 2682.60]  You might actually start looking forward to Mondays.
[2682.76 --> 2685.46]  Sounds like somebody's got a case of the Mondays.
[2685.46 --> 2690.42]  28 more reasons are waiting for you at changelog.com slash news.
[2690.66 --> 2696.32]  Thanks again to our partners at Fly.io to Breakmaster Cylinder for the Beats and to you for listening.
[2696.74 --> 2697.84]  That is all for now.
[2698.04 --> 2699.38]  But we'll talk to you again next time.
[2699.38 --> 2699.56]  All right.
[2700.04 --> 2700.36]  OK.
[2700.36 --> 2708.84]  getting more
