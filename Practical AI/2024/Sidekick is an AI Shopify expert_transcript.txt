[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.84 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[25.82 --> 28.32]  Thanks to our partners at Fly.io.
[28.70 --> 31.08]  Launch your AI apps in five minutes or less.
[31.40 --> 33.32]  Learn how at Fly.io.
[35.24 --> 36.14]  What's up, friends?
[36.32 --> 39.32]  I'm here with Kurt Mackey, co-founder and CEO of Fly.
[39.46 --> 40.64]  As you know, we love Fly.
[40.88 --> 43.46]  That is the home of changelog.com.
[43.84 --> 46.12]  But Kurt, I want to know how you explain Fly to developers.
[46.44 --> 47.86]  Do you tell them a story first?
[48.10 --> 48.64]  How do you do it?
[48.92 --> 54.06]  I kind of change how I explain it based on almost like the generation of developer I'm talking
[54.06 --> 54.30]  to.
[54.30 --> 58.44]  So like for me, I built and shipped apps on Heroku, which if you've never used Heroku
[58.44 --> 61.34]  is roughly like building and shipping an app on Vercel today.
[61.52 --> 64.16]  It's just it's 2024 instead of 2008 or whatever.
[64.36 --> 67.32]  And what frustrated me about doing that was I didn't, I got stuck.
[67.60 --> 71.12]  You can build and ship a Rails app with a Postgres on Heroku.
[71.24 --> 74.22]  The same way you can build and ship a Next.js app on Vercel.
[74.56 --> 78.62]  But as soon as you want to do something interesting, like as soon as you want to, at the time, I
[78.62 --> 82.58]  think one of the things I ran into is like I wanted to add what used to be like kind of
[82.58 --> 83.88]  the basis for Elasticsearch.
[83.88 --> 85.74]  I want to do full text search in my applications.
[86.22 --> 90.46]  You kind of hit this wall with something like Heroku where you can't really do that.
[90.68 --> 94.80]  I think lately we've seen it with like people wanting to add LLMs kind of inference stuff
[94.80 --> 95.72]  to their applications.
[96.22 --> 101.00]  On Vercel or Heroku or Cloudflare or whoever these days, they've started like releasing
[101.00 --> 102.92]  abstractions that sort of let you do this.
[102.92 --> 108.22]  But I can't just run the model I'd run locally on these black box platforms that are very
[108.22 --> 108.76]  specialized.
[109.10 --> 112.58]  For the people my age, it's always like, oh, Heroku was great, but I outgrew it.
[112.78 --> 116.54]  And one of the things that I felt like I should be able to do when I was using Heroku was like
[116.54 --> 119.46]  run my app close to people in Tokyo for users that were in Tokyo.
[119.64 --> 120.64]  And that was never possible.
[121.00 --> 125.08]  For modern generation devs, it's a lot more Vercel based.
[125.26 --> 129.10]  It's a lot like Vercel is great right up until you hit one of their hard line boundaries.
[129.10 --> 130.42]  And then you're kind of stuck.
[130.50 --> 131.12]  There's the other one.
[131.24 --> 132.64]  We've had someone within the company.
[133.02 --> 136.56]  I can't remember the name of this game, but the tagline was like five minutes to start
[136.56 --> 137.46]  forever to master.
[137.58 --> 140.92]  That's sort of how we're pitching Fly is like you can get an app going in five minutes,
[140.92 --> 144.38]  but there's so much depth to the platform that you're never going to run out of things
[144.38 --> 145.22]  you can do with it.
[145.84 --> 153.20]  So unlike AWS or Heroku or Vercel, which are all great platforms, the cool thing we love here
[153.20 --> 158.86]  at ChangeLog most about Fly is that no matter what we want to do on the platform, we have
[158.86 --> 165.08]  primitives, we have abilities, and we as developers can charge our own mission on Fly.
[165.38 --> 169.58]  It is a no limits platform built for developers, and we think you should try it out.
[169.68 --> 172.26]  Go to fly.io to learn more.
[172.74 --> 174.14]  Launch your app in five minutes.
[174.48 --> 175.16]  Too easy.
[175.58 --> 177.60]  Once again, fly.io.
[180.86 --> 182.86]  Fly.io
[182.86 --> 199.60]  Welcome to another edition of the Practical AI Podcast.
[199.98 --> 201.14]  This is Chris Benson.
[201.74 --> 203.44]  I am going solo today.
[203.60 --> 208.34]  Daniel's not able to join me, but we have two guests today, and I would like to introduce
[208.34 --> 214.88]  you to Mike Tamir, who is Distinguished Machine Learning Engineer and Head of Machine Learning
[214.88 --> 220.92]  at Shopify, as well as his colleague, Mike Collier, who is the Director of Product Management
[220.92 --> 221.72]  for Sidekick.
[221.86 --> 222.90]  Gentlemen, welcome to the show.
[223.34 --> 223.72]  Thanks, Chris.
[224.00 --> 224.16]  Yeah.
[224.34 --> 224.96]  Thanks for having us.
[225.20 --> 226.16]  Glad to have you on board.
[226.24 --> 231.66]  I know you guys are doing a lot of cool stuff in the AI space, and so thank you both for joining
[231.66 --> 233.44]  to cover the different aspects of it.
[233.44 --> 238.66]  For those who may be joining, who probably have heard of Shopify, but may not be users
[238.66 --> 243.22]  or may not be intimately familiar, can you guys talk a little bit, before we dive into
[243.22 --> 249.70]  all the AI goodness, can you guys talk a little bit about what Shopify is as a company and kind
[249.70 --> 252.04]  of how you see the space that you're in?
[252.52 --> 253.68]  What need are you fulfilling?
[254.04 --> 258.44]  Just some of the general understanding of your business before we get into the AI stuff.
[258.74 --> 262.18]  Yeah, I can jump in and then maybe Mike can add in, sprinkle in some bits.
[262.18 --> 262.56]  Sure.
[262.56 --> 267.18]  Yeah, Shopify is one of those incredible companies that you might not be aware of, but you've
[267.18 --> 270.00]  probably used it, even if you aren't specifically aware of it.
[270.62 --> 274.16]  So our mission is to create the retail operating system behind your favorite brands.
[274.72 --> 278.26]  So you can think about it, it's like there's the chain restaurants you go to, right, all
[278.26 --> 279.20]  around your hometown.
[279.74 --> 283.44]  But then there's your favorite coffee shop that's run by a local operator, right?
[283.58 --> 286.00]  And there's something better about that coffee, right?
[286.08 --> 292.16]  And so Shopify's goal on the internet is to enable those kinds of operators to have a successful
[292.16 --> 293.00]  business out there.
[293.00 --> 295.82]  And so we power many brands online.
[295.98 --> 301.90]  Some of the ones that are out there that are more famous are like Drake, Patel, Jim Shark,
[302.32 --> 303.88]  Heinz, just to name a few.
[304.04 --> 307.70]  And so like some of the world's biggest brands are on there, but also some of those entrepreneurs
[307.70 --> 309.40]  that are in your local area are too.
[309.40 --> 315.64]  Can you describe like what sets Shopify apart from other, you know, like other processing?
[315.88 --> 320.00]  I mean, it has a very distinctive brand, I know, but can you share a little bit about
[320.00 --> 325.24]  what makes it distinct from other things like credit card processors and, you know, cart
[325.24 --> 325.80]  processors?
[326.06 --> 328.56]  I know you guys kind of have your own distinctive way of doing things.
[329.00 --> 329.10]  Yeah.
[329.16 --> 331.64]  I mean, it's a full soup to nuts kind of solution.
[331.92 --> 333.38]  So like we do e-commerce.
[333.62 --> 335.06]  So like we can help you build your site.
[335.28 --> 338.44]  We can help you create merchandising around the products that you offer.
[338.44 --> 340.02]  We also offer payment solutions.
[340.46 --> 344.24]  So you don't have to set up a separate credit card processor, but if you have one, you can
[344.24 --> 344.68]  bring it too.
[345.22 --> 349.42]  I think that's actually one of the most powerful things about the Shopify platform is that it's
[349.42 --> 351.24]  got a very extensive developer ecosystem.
[351.94 --> 355.80]  And so many of our merchants install apps from our partners to do specific things.
[355.88 --> 359.74]  So if you've got a specific shipping provider, you can use their app for it.
[359.96 --> 362.76]  If you've got a specific email provider, you can use your app for it.
[363.02 --> 367.76]  For many of these categories, we also have solutions, but the ecosystem is definitely the richest
[367.76 --> 368.12]  part.
[368.44 --> 373.22]  It sounds like you also do lots of different market segments from some of the large brands
[373.22 --> 378.30]  that you just talked about down to, I know when I've come across Shopify in the past,
[378.30 --> 383.54]  it's been in the context of kind of smaller business and e-commerce and mid-sized business
[383.54 --> 384.50]  and things like that.
[384.62 --> 389.92]  So it sounds like you guys hit quite an array of different customer segments with technology
[389.92 --> 390.48]  solutions.
[390.84 --> 390.94]  Yeah.
[390.96 --> 392.32]  I mean, maybe Mike, do you want to chime in?
[392.36 --> 394.82]  I feel like you work on more of them than I do these days.
[394.82 --> 400.70]  If you think about all the things that Matt described, establishing a website, payment
[400.70 --> 406.12]  processing, that's the infrastructure for something you could provide for a large established brand
[406.12 --> 408.30]  all the way down to a smaller brand.
[408.60 --> 413.32]  More and more, especially in recent years, what Shopify has been focusing on is not just
[413.32 --> 418.16]  providing you with the website, but also providing you with kind of the tools for growth.
[418.16 --> 424.02]  And this is where AI and the focus that we've had on moving to machine learning and AI has
[424.02 --> 426.04]  really made itself apparent.
[426.44 --> 434.44]  So for instance, we have our shop app where a new merchant who has no track record of sales
[434.44 --> 437.78]  or history can join that app.
[437.96 --> 444.10]  And when we search, if we understand the backend of machine learning and understanding how to do
[444.10 --> 449.88]  the retrieval and the ranking well, we can reveal a new fresh merchant to a customer right away.
[450.40 --> 450.74]  Very cool.
[451.04 --> 452.06]  Piggyback on what Mike was saying.
[452.14 --> 455.44]  I think it's like a great example of how he worked in the AI component of it.
[455.62 --> 459.32]  But like one of the core values of Shopify is that we keep merchants on the cutting edge.
[459.32 --> 465.14]  So like we view our mission to like understand technology at a really deep level and always
[465.14 --> 470.26]  be out there scouring the best and then figure out how we can apply it to our merchants' businesses.
[470.62 --> 470.70]  Right.
[470.76 --> 473.94]  And so like Mike was talking about, how can we help our merchants grow?
[474.10 --> 474.28]  Right.
[474.34 --> 478.76]  And so how can we apply these machine learning models or these AI techniques and really help
[478.76 --> 480.36]  these people grow their business?
[480.96 --> 485.30]  With you guys having that technology infrastructure that you've been supporting all these businesses
[485.30 --> 489.30]  with and everything, at what point did you start thinking about the fact that you've
[489.30 --> 493.36]  the fact that there were these AI technologies that are, you know, been on the rise in recent
[493.36 --> 493.80]  years?
[494.36 --> 500.64]  What was the turning point for the company where you started seriously looking at AI as a supporting
[500.64 --> 501.84]  factor in the business model?
[502.34 --> 508.06]  You know, what made you say, I see an opportunity to go help our customer get done the things
[508.06 --> 510.16]  that we're trying to do that we've been doing for years?
[510.68 --> 511.82]  What was that turning point?
[512.18 --> 513.50]  Kind of how did that come about?
[513.54 --> 516.10]  And how did you start thinking about AI in the business?
[516.10 --> 522.16]  I mean, knowing the timeline, you know, I think that the turning point was, you know,
[522.16 --> 527.70]  we might be the chicken and not the egg, so to speak, in that, you know, Shopify maybe
[527.70 --> 530.64]  historically was not as invested in machine learning and AI.
[530.96 --> 538.98]  But by 2022, I'd become interested in that and has certainly massively redirected our forces
[538.98 --> 544.18]  and the work that Matt and I joined and have focused on over the last several years.
[544.18 --> 547.66]  And can you talk a little bit about that vision as you talk about, you know, you guys kind
[547.66 --> 551.22]  of coming into the company at that point and carrying that forward?
[551.66 --> 555.78]  How do you think about your the mission, if you will, that you're doing?
[555.94 --> 560.44]  How do you how do you contextualize it in terms of how you want to carry it forward and how
[560.44 --> 562.68]  you're going to serve your customers with that effort?
[562.92 --> 565.34]  I'll give you my product manager answer to this.
[565.42 --> 566.20]  That sounds fine.
[566.34 --> 568.60]  It was interesting hearing Mike's science answer to this.
[568.60 --> 572.10]  Um, I think it's about finding out what's out there in the world.
[572.42 --> 577.16]  So to be quite honest, like in that time period, like if you all recall, it feels like, I don't
[577.16 --> 580.94]  know, a million years ago, but chat GPT didn't exist like three years ago, right?
[581.08 --> 581.48]  That's right.
[581.56 --> 583.52]  And we forget that that was a world, but it was.
[583.80 --> 588.22]  And so like, I think we got enamored, like the folks that work with Shopify with that technology,
[588.22 --> 589.48]  just as much as everybody else did.
[589.76 --> 594.24]  I definitely remember there was a peak chat GPT moment where my mom was telling me about how
[594.24 --> 595.30]  she got it to write it a poem.
[595.30 --> 600.46]  And so I think the whole world was just captivated by the fact that we had computers that could,
[600.54 --> 601.58]  you know, write us stories.
[601.90 --> 604.68]  And so I think, I think that's kind of the culture of Shopify, right?
[604.70 --> 609.18]  Like we're all tinkerers and we like to build and we're all there getting messages from our
[609.18 --> 611.56]  moms about how they can write stories that they couldn't write before.
[611.68 --> 615.52]  And they were like, naturally you're like, maybe, maybe there's a way to apply this to
[615.52 --> 616.20]  commerce, right?
[616.64 --> 617.96]  I'm curious as you talk about that.
[618.04 --> 621.78]  I like, I like the mom story because that literally holds true with me.
[621.78 --> 627.08]  I have a mom, she's long since retired, but she, she was a technologist.
[627.08 --> 630.22]  And so, yeah, we have those moments where she's like, well, I'm going to go try that
[630.22 --> 631.68]  thing out and do that.
[631.72 --> 636.44]  I'm kind of curious as these new technologies were coming about and you guys are coming into
[636.44 --> 637.98]  the company and kind of carrying it forward.
[637.98 --> 642.60]  There were a lot of choices that you guys had to make, you know, in terms of like, there's
[642.60 --> 646.82]  obviously we talked about chat GPT, there's open source, there's a whole bunch of different
[646.82 --> 652.80]  approaches to how you're going to support your customers with different technologies and
[652.80 --> 654.54]  different ways of addressing.
[655.14 --> 660.16]  What was your thinking both on the technical and on the product side in terms of how you
[660.16 --> 660.68]  might do that?
[660.68 --> 668.72]  I would describe our approach as, as unembarrassed with how pragmatic we are on these issues,
[668.82 --> 674.84]  you know, whether it's open source or one of the commodity providers for LLMs, we tend
[674.84 --> 679.72]  to gravitate to whatever works and we do keep multiple threads of experiments with all of
[679.72 --> 684.56]  these different options for technological options open for solving every problem.
[684.56 --> 691.92]  I think that that pans out with what we currently have in production and active is a nice array
[691.92 --> 697.66]  of, of not just all of the foundation models that you might think the commodity options that
[697.66 --> 702.48]  are out there, but also being pretty aggressive with how we use the open source versions that
[702.48 --> 702.92]  are out there.
[703.62 --> 707.72]  As we've talked about that in, you know, you bring up open source there and we've talked
[707.72 --> 712.66]  about, you know, productized offerings such as chat GPT through API and stuff.
[712.66 --> 718.70]  So going into this and before you got to the point now where there are a number of, of
[718.70 --> 723.12]  things that I know we're about to talk about, how did you strategic, like from a strategic
[723.12 --> 725.40]  standpoint, how did you parse that?
[725.50 --> 731.20]  How did you say we have this, you know, challenge and that we're a big successful technology
[731.20 --> 731.64]  company?
[732.22 --> 738.60]  We're moving into the brave new world of AI and you had to kind of like figure out what
[738.60 --> 739.90]  do you want to do with foundation models?
[740.02 --> 741.02]  Are you hosting your own?
[741.02 --> 742.82]  Are you, are you going to go to APIs?
[743.30 --> 744.48]  How do you think about that?
[744.48 --> 750.26]  Like from, and not just from a technical standpoint, but from the perspective of serving your customers
[750.26 --> 755.06]  and stuff, like what are the, what, how do you see the strengths and the weaknesses of
[755.06 --> 757.22]  different, uh, of different perspectives there?
[757.22 --> 761.08]  If you could share a little bit about your insight as you had to, to analyze on behalf of your
[761.08 --> 761.62]  own business.
[761.96 --> 765.38]  Echoing what Mike said, it's like, I think it's, it's early innings in this industry, right?
[765.38 --> 769.10]  And so like at the beginning of an industry, it's like, there's a lot of change and it
[769.10 --> 770.32]  happens very, very quickly.
[771.10 --> 773.54]  And so I think it's hard to like pick any one solution.
[773.72 --> 777.98]  Like, I think what people thought at the beginning of this, like a new wave of technology is
[777.98 --> 780.30]  like, they're like, maybe fine tuning was the answer.
[780.38 --> 780.56]  Right.
[780.60 --> 784.40]  And it's like, as modeled in context, windows will be small forever and it will be expensive.
[784.40 --> 789.00]  And like, I think it's blown everybody's expectations out of the water at how much,
[789.36 --> 792.22]  how quickly, how things have gotten less expensive.
[792.58 --> 794.46]  Like, I don't think anybody could have predicted that.
[794.58 --> 798.86]  And so like, I think that's just such a world of abundance, both in like the operational costs,
[798.86 --> 803.64]  but also the other thing I would say that's unpredicted is that the number of solutions
[803.64 --> 805.06]  out there is just unparalleled.
[805.18 --> 809.46]  Like, I don't know without the leaking of the llama weights, I forget back in like March
[809.46 --> 810.98]  of, I don't know, was it 23 or something?
[810.98 --> 815.22]  I don't know that we'd have the open source community that we have today, but like, since
[815.22 --> 820.48]  that kind of Cambrian explosion of open source models, it's been like crazy, like some of
[820.48 --> 821.56]  the innovation that's out there.
[821.64 --> 824.34]  And so like, I think I would like to think that we had a master plan.
[824.44 --> 825.62]  We're like, oh yes, we saw exactly.
[825.74 --> 828.22]  We were going to use these commodity models and then move to the open source models.
[828.30 --> 832.18]  But like the reality of it is always messier than the historical written version, I think.
[832.82 --> 836.32]  And so I think the short answer to all of that is that we try a bunch of stuff.
[836.40 --> 836.60]  Right.
[836.62 --> 840.14]  And I think the people that win in this space are the people that try that most things the
[840.14 --> 840.56]  fastest.
[840.98 --> 844.50]  And so I'd say that's our overall strategy is we try a lot of different things.
[844.50 --> 848.72]  And then like Mike said, like we have a rigorous way of determining which is the best, but that
[848.72 --> 849.48]  frequently changes.
[849.48 --> 853.26]  Like one approach that worked three months ago, like I don't, I can't even count how many
[853.26 --> 857.76]  times on sidekick we've replaced the core underpinnings of it because we found a new approach
[857.76 --> 858.20]  that's better.
[858.86 --> 860.26]  I'm not at all surprised by that.
[860.26 --> 865.26]  And I appreciate that answer because I think that's a challenge that everyone out there,
[865.26 --> 870.62]  a lot of folks listening to this are facing as well as it is moving so fast.
[870.62 --> 877.42]  And what was expensive yesterday is plunging in cost as new things are on the rise and such.
[877.92 --> 885.40]  And so I like your notion of experiment very fast, fail fast, I guess, in the process on your
[885.40 --> 890.16]  experiments so that you know what's working for you at least today until the next thing hits you
[890.16 --> 890.68]  tomorrow.
[890.68 --> 897.24]  Have there been any growing pains that they come to mind that you can share that have been
[897.24 --> 902.30]  kind of like, oh, you know, where you plant your palm on your forehead and say, I wish I could have
[902.30 --> 902.94]  seen that coming.
[903.46 --> 909.74]  So this is something that I think the entire community has been working out in real time.
[910.32 --> 915.34]  Like Matt said, you can try different things and see which strategy works the best or which tactic
[915.34 --> 918.54]  works best or what combination of those tactics works best and change all the time.
[918.54 --> 923.16]  Because we do know that new models are going to keep being released, large commodity ones,
[923.36 --> 927.12]  smaller open source ones, large open source ones, and different.
[927.28 --> 931.92]  We're learning all the time in the research what sorts of tactics with whether it's fine tuning
[931.92 --> 935.80]  or using long prompts or combinations of domain adaptation.
[936.70 --> 938.34]  That's all going to be in flux.
[938.36 --> 941.42]  And we should believe that that's going to be in flux for a very long time.
[942.14 --> 946.62]  And so if you have a mandate of, hey, we're open to anything and we'll use what works.
[946.62 --> 949.92]  We have to have a definition of what working looks like.
[950.18 --> 953.70]  And that means, and Matt's going to laugh because this is something that we've worked
[953.70 --> 954.34]  on quite a bit.
[954.64 --> 957.32]  You have to have your eval system dialed in.
[957.88 --> 963.14]  And that's the sort of work that we're moving into different formats for how you might eval,
[963.24 --> 969.04]  especially with unstructured text generation for figuring out this was a good answer, this
[969.04 --> 972.18]  was a bad answer, and being able to measure it in various ways.
[972.18 --> 975.18]  And there's all sorts of creative solutions depending on the context.
[975.64 --> 981.34]  But making sure that we have a way of measuring that versus saying two anecdotes is enough
[981.34 --> 983.06]  for me to think that all the swans are white.
[984.14 --> 988.84]  That's an important part of the process if we want to be pragmatic about our solutioning.
[989.60 --> 991.98]  Yeah, we have like a, I guess a story on the team.
[992.06 --> 993.52]  We talk about it being the dark forest.
[993.90 --> 996.06]  And I think we're all grasping.
[996.22 --> 1000.30]  We wish we had our GPS enabled phones of pinpointing us on the map of how you get out of the dark
[1000.30 --> 1000.64]  forest.
[1000.64 --> 1004.98]  But I think what we've had to settle for with eval is like a compass, if you will, like
[1004.98 --> 1010.48]  the metaphor here, is that it's like everybody wishes we knew absolutely like this is how
[1010.48 --> 1011.52]  good the system is, right?
[1011.56 --> 1015.40]  But like what we've kind of settled for instead that's more practical is like, well, we know
[1015.40 --> 1017.14]  A is better than B, right?
[1017.18 --> 1020.54]  And so if you just make enough decisions in aggregate where A is always better than B,
[1021.06 --> 1023.24]  you eventually find yourself out of the forest, right?
[1023.66 --> 1025.26]  But we wish we knew how long it would take.
[1025.34 --> 1027.34]  The question is always like, well, when are you going to find your way out?
[1027.38 --> 1028.16]  Where it's like, well, we don't know.
[1028.16 --> 1030.46]  We're just going to keep making the best next decision we can.
[1030.64 --> 1043.26]  Okay, friends.
[1043.38 --> 1046.04]  I'm with a good friend of mine, Avthar Suathan from Timescale.
[1046.20 --> 1053.18]  They're positioning Postgres for everything from IoT, sensors, AI, dev tools, crypto, and
[1053.18 --> 1053.94]  finance apps.
[1053.94 --> 1058.56]  So Avthar, help me understand why Timescale feels Postgres is most well positioned to
[1058.56 --> 1061.10]  be the database for AI applications.
[1061.52 --> 1065.68]  It's the most popular database according to the Stack Overflow Developer Survey.
[1065.88 --> 1069.50]  And Postgres, one of the distinguishing characteristics is that it's extensible.
[1069.74 --> 1075.16]  And so you can extend it for use cases beyond just relational and transactional data for use
[1075.16 --> 1077.10]  cases like time series and analytics.
[1077.10 --> 1080.90]  That's kind of where Timescale the company started, as well as now more recently, vector
[1080.90 --> 1085.98]  search and vector storage, which are super impactful for applications like RAG, recommendation
[1085.98 --> 1090.20]  systems, and even AI agents, which we're seeing, you know, more and more of those things today.
[1090.20 --> 1092.54]  Yeah, Postgres is super powerful.
[1092.76 --> 1094.16]  It's well loved by developers.
[1094.94 --> 1100.22]  I feel like more devs, because they know it, it can enable more developers to become AI
[1100.22 --> 1103.36]  developers, AI engineers, and build AI apps.
[1103.60 --> 1107.20]  From our side, we think Postgres is really the no-brainer choice.
[1107.46 --> 1109.06]  You don't have to manage a different database.
[1109.34 --> 1113.80]  You don't have to deal with data synchronization and data isolation because you have like three
[1113.80 --> 1116.20]  different systems and three different sources of truth.
[1116.20 --> 1120.58]  And one area where we've done work in is around the performance and scalability.
[1120.88 --> 1125.70]  So we've built an extension called PG Vector Scale that enhances the performance and scalability
[1125.70 --> 1131.24]  of Postgres so that you can use it with confidence for large-scale AI applications like RAG and
[1131.24 --> 1132.16]  agents and such.
[1132.38 --> 1136.08]  And then also another area is, coming back to something that you said, enabling more and
[1136.08 --> 1141.36]  more developers to make the jump into building AI applications and become AI engineers using the
[1141.36 --> 1142.70]  expertise that they already have.
[1142.70 --> 1147.74]  And so that's where we built the PGAI extension that brings LLMs to Postgres to enable things
[1147.74 --> 1151.58]  like LLM reasoning on your Postgres data, as well as embedding creation.
[1151.92 --> 1155.16]  And for all those reasons, I think, you know, when you're building an AI application, you
[1155.16 --> 1156.36]  don't have to use something new.
[1156.56 --> 1157.56]  You can just use Postgres.
[1158.24 --> 1161.28]  Well, friends, learn how Timescale is making Postgres powerful.
[1161.68 --> 1167.42]  Over 3 million Timescale databases power IoT, sensors, AI, dev tools, crypto, and finance
[1167.42 --> 1167.96]  applications.
[1168.28 --> 1170.14]  And they do it all on Postgres.
[1170.14 --> 1173.60]  Timescale uses Postgres for everything, and now you can too.
[1174.02 --> 1176.06]  Learn more at timescale.com.
[1176.34 --> 1178.38]  Again, timescale.com.
[1178.38 --> 1203.38]  So guys, I love the fact that you're kind of your notion of eval and finding your way
[1203.38 --> 1210.98]  back out of the forest, you kind of with that in mind, you have a lot of different products
[1210.98 --> 1212.34]  that you work with.
[1212.34 --> 1217.78]  And as you're bringing these new technologies in, and you're doing these evals, and you're
[1217.78 --> 1224.86]  trying to find your way out of the black forest through that and managing across multiple areas
[1224.86 --> 1225.44]  there.
[1225.80 --> 1227.24]  How does that look for you?
[1227.24 --> 1234.16]  How do you unify different products so that you can effectively serve your customers with
[1234.16 --> 1234.92]  these technologies?
[1235.26 --> 1238.84]  And how do you make all those Legos come together in a usable way?
[1239.30 --> 1241.74]  There are certain genres of problems.
[1242.16 --> 1247.62]  And it seems like one or more strategies for eval will be appropriate for each genre.
[1247.62 --> 1249.24]  So let me give an example.
[1249.84 --> 1255.80]  With search and evaluating search quality, there's been some good research that shows
[1255.80 --> 1262.84]  that LLMs tend to be better at rank ordering or labeling relevant, not relevant of a product
[1262.84 --> 1265.68]  to a query at a certain resolution.
[1266.16 --> 1272.82]  In fact, there's research that shows that the LLMs are better than a human at doing this.
[1272.82 --> 1275.44]  And you might ask yourself, why is that?
[1276.54 --> 1278.18]  You're a human, Chris.
[1278.40 --> 1281.32]  You searched for a white flower dress.
[1281.88 --> 1284.26]  And you're going to click on one of those, right?
[1284.28 --> 1286.70]  One of those is going to be the right answer for that query for you.
[1287.10 --> 1289.36]  And then I might search for a white flower dress.
[1289.38 --> 1291.98]  And you search for one because you wanted a dress with a white flower.
[1292.36 --> 1295.14]  And I didn't want to dress with a white flower.
[1295.30 --> 1297.62]  I wanted a white dress with colorful flowers.
[1297.74 --> 1301.86]  And both of these are completely legitimate answers to that query.
[1301.86 --> 1305.20]  And what we're seeing here is it's actually just a sampling problem.
[1305.28 --> 1311.08]  If you think about it, there's a distribution of appropriate products matching any query.
[1311.68 --> 1316.66]  And so every time we ask a human, we're getting a sample from that distribution.
[1316.66 --> 1321.78]  But if that distribution is very flat, then we're going to sample across a wide variety
[1321.78 --> 1322.76]  of different answers.
[1323.36 --> 1327.78]  And so what we've done with LLMs in this is, you can think about this as an analogy.
[1327.78 --> 1332.64]  In the morning, I like fill in the blank, right?
[1333.06 --> 1334.64]  And there's a lot of good answers to that.
[1334.74 --> 1335.62]  I like to exercise.
[1335.86 --> 1336.74]  I like coffee.
[1336.92 --> 1337.78]  I like breakfast.
[1338.02 --> 1339.04]  I like orange juice.
[1339.08 --> 1339.92]  Whatever it is, right?
[1340.16 --> 1342.06]  There's a lot of ways of completing that sentence.
[1342.12 --> 1342.88]  And they're all legitimate.
[1343.04 --> 1345.72]  It's just that it's a very flat distribution.
[1346.52 --> 1351.84]  And with language, what we do is we just overwhelm with sample after sample after sample after
[1351.84 --> 1354.30]  sample so that we can fill in that whole distribution.
[1354.30 --> 1361.64]  In the query product genre, it takes too much time and too much cost to fill in that distribution
[1361.64 --> 1363.66]  in mass that way, right?
[1363.78 --> 1365.78]  Until you get into implicit feedback.
[1366.36 --> 1368.68]  So you have to find another solution.
[1368.80 --> 1375.08]  And this is one of the reasons why when you're using an LLM and replacing a typical Terker from
[1375.08 --> 1378.18]  filling in those answers, you get better results.
[1378.56 --> 1382.46]  Now, something important is something that Matt and I have seen in other contexts.
[1382.54 --> 1383.84]  You can't do this ungrounded.
[1383.84 --> 1388.38]  You can't just have the robots grade the robots and then hope for the best.
[1388.74 --> 1396.02]  You have to have different expert supervision to ground those answers, whether it's in a
[1396.02 --> 1401.34]  search context, a personalization context, in more of a chat context, like the sidekick
[1401.34 --> 1401.70]  product.
[1401.92 --> 1403.50]  You have to have that grounding.
[1403.80 --> 1408.38]  And once you inject that kind of like course correction, then you kind of get the best of
[1408.38 --> 1408.90]  both worlds.
[1409.44 --> 1412.26]  Could you talk a little bit about the different products?
[1412.26 --> 1418.12]  You talked about query, you talked about personalization, but are there any others there that you say
[1418.12 --> 1424.00]  are kind of very prominent in your world that you're thinking about applying LLMs or other
[1424.00 --> 1425.04]  AI technologies to?
[1425.04 --> 1429.76]  So we've got several products that are AI enabled or magic enabled Shopify.
[1430.72 --> 1433.42]  So sidekick is kind of the main one, which we'll talk more about.
[1433.52 --> 1439.86]  But to give you a general idea, it's a tool that helps merchants find a way around Shopify, but also answer
[1439.86 --> 1440.92]  questions about their business.
[1441.10 --> 1444.00]  So you can think of it as like the co-founder they wish they had.
[1444.38 --> 1446.98]  That's available 24-7 and isn't judgmental.
[1447.18 --> 1448.72]  So that's kind of like the sidekick idea.
[1449.16 --> 1451.08]  And then we've got a variety of other ones as well.
[1451.22 --> 1452.92]  So we have a lot of imagery.
[1453.28 --> 1456.52]  So it turns out shopping, like people want to see what the thing is before they purchase
[1456.52 --> 1456.78]  it.
[1457.06 --> 1458.18]  Not terribly surprising.
[1458.50 --> 1462.58]  And one of the things that merchants often want to be able to do before they've scaled
[1462.58 --> 1467.16]  up to a whole team that has a studio and a photographer and the rest of it is they
[1467.16 --> 1469.14]  want to enhance the pictures that they do have.
[1469.26 --> 1469.38]  Right.
[1469.38 --> 1473.06]  So like at the scale that they're at, this is where technology, again, bringing back
[1473.06 --> 1476.58]  like the best from the frontier and making it accessible to all of our merchants is exciting.
[1477.02 --> 1480.94]  So like there is technology that's out there now that you can essentially describe what
[1480.94 --> 1481.90]  you want to do to an image.
[1482.04 --> 1483.94]  You're like, hey, my background's a little bit messy.
[1484.10 --> 1486.68]  Can you replace it with a studio background instead?
[1486.76 --> 1490.34]  Because like we all know that the nice white studio background that looks like the objects
[1490.34 --> 1491.18]  floating in space.
[1491.18 --> 1491.42]  Right.
[1491.48 --> 1493.26]  It's like you can do that in real life.
[1493.26 --> 1496.34]  It's just really hard and expensive and you have to know what you're doing.
[1496.34 --> 1499.10]  And there are very few people who know how to do that well.
[1499.36 --> 1503.06]  And so it turns out we've created models that can do it fairly well as well.
[1503.68 --> 1507.56]  And so bringing that technology back, that's one of the products we do offer integrated
[1507.56 --> 1509.96]  into Shopify today is background generation.
[1510.72 --> 1514.40]  So merchants can import an image that they already have, replace the background with something
[1514.40 --> 1515.38]  that's more on brand.
[1515.52 --> 1519.36]  Like say they want to set their coffee to the background of like a jungle.
[1519.60 --> 1519.76]  Right.
[1519.76 --> 1522.54]  They can place it on a table in front of a jungle if that's what they would prefer.
[1522.66 --> 1525.52]  Or they could do it into the void of the white space.
[1525.52 --> 1528.04]  So lots of exciting opportunities with that.
[1528.52 --> 1532.62]  Another area that we've been investing in is that we have a product called Inbox, which
[1532.62 --> 1535.80]  allows our merchants to talk with the buyers that they have on their site.
[1536.26 --> 1539.06]  And if a buyer has a question like, hey, what's your return policy?
[1539.30 --> 1540.46]  Or like, where's my order at?
[1540.76 --> 1542.58]  They can interact with the merchants through Inbox.
[1543.18 --> 1546.80]  And so one of the things that we're offering today is that we look at all the merchants
[1546.80 --> 1550.84]  policies and all the other things that they've given to us and then can help formulate
[1550.84 --> 1552.36]  answers for those common questions.
[1552.50 --> 1552.58]  Right.
[1552.62 --> 1553.70]  It's like, well, what's your return policy?
[1553.70 --> 1555.98]  It's like, well, we're pretty sure that this is the answer.
[1556.56 --> 1559.58]  And then we can suggest that to a merchant who then says, yep, that's right.
[1559.64 --> 1562.66]  Or if that's not right, they can adjust it to be correct and then send it.
[1562.88 --> 1566.58]  And so merchants love that because it saves them time for answering a lot of those repetitive
[1566.58 --> 1567.10]  questions.
[1567.10 --> 1570.62]  And then those ones that are a little bit harder, they can write them themselves just as
[1570.62 --> 1571.10]  they would before.
[1571.10 --> 1576.26]  And then the last one that I'm thinking about is like, again, going back to that product
[1576.26 --> 1580.74]  and merchandising kind of task is that oftentimes merchants are uploading a lot of these at the
[1580.74 --> 1581.26]  same time.
[1581.26 --> 1581.50]  Right.
[1581.54 --> 1585.34]  And so like they don't always capture all the metadata in the first go.
[1585.34 --> 1588.68]  And so this is, again, where we created models that actually can help with that.
[1588.82 --> 1593.90]  So if you upload an image of a white flower dress, we have a model that can actually understand
[1593.90 --> 1597.32]  what that picture is and suggest that, hey, maybe this is a white flower dress and this
[1597.32 --> 1600.22]  should be categorized under dresses and like under cotton.
[1600.54 --> 1600.66]  Right.
[1600.66 --> 1604.76]  And like maybe it can suggest, oh, it turns out if you upload multiple different colors,
[1604.80 --> 1606.44]  it's like, well, maybe you want to create product variants.
[1606.62 --> 1610.12]  And so that's some of the other technology that we're kind of working on today is like
[1610.12 --> 1614.16]  using the data that we have from merchants, enabling them to more expressively describe
[1614.16 --> 1616.00]  their products through our sites.
[1616.82 --> 1621.84]  With Inbox, is Inbox part of Sidekick or is it adjacent or parallel to Sidekick in the
[1621.84 --> 1622.92]  way that you see it?
[1623.26 --> 1624.68]  No, it's a completely separate offering.
[1625.04 --> 1628.60]  So merchants have to choose to install, again, going back to kind of the platform thing we
[1628.60 --> 1629.34]  talked about earlier.
[1629.34 --> 1632.04]  They choose to install the Inbox app, which Shopify builds.
[1632.40 --> 1636.40]  And then within the Inbox app, you can choose to use this behavior or not.
[1637.26 --> 1639.64]  You mentioned also the ecosystem a little while ago.
[1639.80 --> 1646.20]  And I'm curious how, as you have created these new AI-enabled products, how has the ecosystem
[1646.20 --> 1647.64]  been plugging into that?
[1647.74 --> 1649.30]  Is that something that's possible?
[1649.82 --> 1651.72]  What kind of interactions do they have together?
[1652.22 --> 1657.30]  So today we have a very extensive API through GraphQL that we expose, like the data we just
[1657.30 --> 1657.92]  talked about, right?
[1657.92 --> 1658.82]  The categorization.
[1658.82 --> 1662.66]  So whatever the merchant decides, like we make a recommendation, they say, yes, that's
[1662.66 --> 1662.94]  correct.
[1663.06 --> 1664.22]  This dress is actually a dress.
[1664.78 --> 1669.46]  Once they save that change, that information is then available through that product description
[1669.46 --> 1669.90]  API.
[1670.30 --> 1670.66]  I see.
[1671.10 --> 1677.04]  Matt covered a nice breadth of generative text, generative images, product understanding,
[1677.04 --> 1683.00]  all of which are kind of adjacent to or image generation is sort of a different algorithm
[1683.00 --> 1684.28]  under the hood.
[1684.28 --> 1688.20]  There's also a direction where we can think about something that I've...
[1688.20 --> 1693.94]  It's been a gift that keeps on giving for all of my career is that the sorts of machine
[1693.94 --> 1700.66]  learning techniques that work with text often also work with commerce.
[1700.66 --> 1705.84]  And so this goes back to old-fashioned matrix factorization for recommender engines was also
[1705.84 --> 1707.68]  useful for understanding text.
[1708.38 --> 1714.08]  RNNs, useful for looking at sequences or sentences before Transformers took over.
[1714.42 --> 1715.18]  Good for text also.
[1715.18 --> 1716.72]  Well, you're taking me way back.
[1716.72 --> 1720.84]  We did many whole shows on RNNs and that seems like the Stone Age now.
[1721.08 --> 1721.28]  Yeah.
[1721.40 --> 1723.40]  The Stone Age of the 20 teens, right?
[1723.80 --> 1724.36]  That's right.
[1725.36 --> 1730.74]  That also, a lot of the techniques, you could always just peek at what you're doing in language
[1730.74 --> 1734.26]  and come up with a cool idea for e-commerce and vice versa.
[1734.68 --> 1736.28]  And so this has not stopped.
[1736.40 --> 1741.64]  I mean, Transformers have kind of taken over everything, but there are not quite Transformer
[1741.64 --> 1748.10]  architectures, but heavy attention method, Transformer-like architectures that can look
[1748.10 --> 1753.46]  at sequences of behaviors of merchants, of buyers, the people that are shopping with
[1753.46 --> 1753.98]  our merchants.
[1754.46 --> 1761.04]  Those are sequences too and can be processed in an analogous way in order to understand what
[1761.04 --> 1765.86]  is the next step on the journey for a merchant and how can we help them get to that journey?
[1765.98 --> 1768.82]  What are the likely ways we can simulate that?
[1768.82 --> 1774.18]  And that's been sort of one of our frontier cutting edge areas that we've been applying
[1774.18 --> 1774.46]  ML.
[1775.22 --> 1777.12]  Actually, Mike's answer reminded me.
[1777.20 --> 1780.42]  I want to add one more product that always slips to mind here.
[1780.44 --> 1782.72]  And it also blends with the ecosystem thing that we talked about.
[1783.44 --> 1787.96]  So as I'm sure you've talked with other folks on the show about, one of the exciting parts
[1787.96 --> 1789.78]  about LLMs is the ability to write code.
[1790.30 --> 1792.18]  And we talked about the GraphQL API.
[1792.18 --> 1796.96]  And so one of the other exciting applications that we've done is for our developer ecosystem
[1796.96 --> 1803.10]  is enhancing our developer docs in the way that we now have an integrated tool that assists
[1803.10 --> 1804.28]  developers in writing code.
[1804.40 --> 1808.02]  You described, you're like, hey, I'm looking to find the product category.
[1808.36 --> 1809.96]  Can you write me the query to do it?
[1810.02 --> 1812.12]  And it will literally write you the GraphQL query.
[1812.60 --> 1814.84]  You can copy and paste that, put your write in your application.
[1815.08 --> 1818.08]  And so I think we're still in the early days of figuring out how...
[1818.08 --> 1822.06]  It's such a dramatic shift for engineering to figure out how we apply these LLMs.
[1822.18 --> 1827.54]  And it's exciting to see these new applications to existing documentation sites and just unlocking
[1827.54 --> 1830.92]  the power and making it more straightforward to develop apps.
[1830.92 --> 1849.00]  What's up, friends?
[1849.14 --> 1850.78]  I love my 8sleep.
[1850.88 --> 1852.68]  Check them out, 8sleep.com.
[1852.78 --> 1854.44]  I've never slept better.
[1854.80 --> 1856.40]  And you know I love biohacking.
[1856.54 --> 1858.04]  I love sleep science.
[1858.04 --> 1864.76]  And this is all about sleep science mixed with AI to keep you at your best while you sleep.
[1865.20 --> 1868.64]  This technology is pushing the boundaries of what's possible in our bedrooms.
[1869.22 --> 1872.80]  Let me tell you about 8sleep and their cutting edge Pod 4 Ultra.
[1873.28 --> 1875.26]  So what exactly is the Pod?
[1875.42 --> 1880.48]  Imagine a high-tech mattress cover that you can easily add to any bed.
[1880.76 --> 1883.32]  But this isn't just any cover.
[1883.32 --> 1886.78]  It's packed with sensors, heating and cooling elements.
[1887.06 --> 1890.26]  And it's all controlled by sophisticated AI algorithms.
[1890.90 --> 1897.58]  It's like having a sleep lab, a smart thermostat, and a personal sleep coach all rolled into one single device.
[1898.14 --> 1903.94]  And the Pod uses a network of sensors to track a wide array of biometrics while you sleep.
[1903.94 --> 1909.14]  It tracks sleep stages, heart rate variability, respiratory rate, temperature, and more.
[1909.68 --> 1910.98]  And the really cool part is this.
[1911.12 --> 1914.66]  It does all this without you having to wear any devices.
[1915.26 --> 1919.92]  The accuracy of this thing rivals what you would get in a professional sleep lab.
[1920.36 --> 1922.18]  Now, let me tell you about my personal favorite thing.
[1922.40 --> 1923.24]  Autopilot recap.
[1923.42 --> 1928.58]  Every day, my 8sleep tells me what my autopilot did for me to help me sleep better at night.
[1928.88 --> 1929.82]  Here's what it said last night.
[1929.82 --> 1934.78]  Last night, autopilot made adjustments to boost your REM sleep by 62%.
[1934.78 --> 1935.62]  Wow.
[1936.12 --> 1936.92]  62%.
[1936.92 --> 1950.24]  That means that it updated and changed my temperature to cool to warm and helped me fine-tune exactly where I wanted to be with precision temperature control to get to that maximum REM sleep.
[1950.66 --> 1954.44]  And sleep is the most important function we do every single day.
[1954.58 --> 1957.32]  As you can probably tell, I'm a massive fan of my 8sleep.
[1957.36 --> 1958.20]  And I think you should get one.
[1958.20 --> 1961.40]  So go to 8sleep.com slash changelog.
[1961.52 --> 1967.04]  And right now, they have an awesome deal for Black Friday going from November 11th through December 14th.
[1967.04 --> 1974.66]  The discount code changelog will get you up to $600 off the Pod4Ultra when you bundle it.
[1975.02 --> 1977.62]  Again, the code to use is changelog.
[1977.76 --> 1980.20]  And that's from November 11th through December 14th.
[1980.86 --> 1984.16]  Once again, that's 8sleep.com slash changelog.
[1984.36 --> 1985.34]  I know you'll love it.
[1985.34 --> 1988.22]  I sleep on this thing every night, and I absolutely love it.
[1988.40 --> 1990.68]  It's a game changer, and it's going to change your game.
[1990.94 --> 1994.26]  Once again, 8sleep.com slash changelog.
[1994.26 --> 2015.92]  Going back to something that you had mentioned earlier in the conversation, you had talked about magic and magic enabled and stuff.
[2016.10 --> 2018.34]  Could you tell me a little bit about that?
[2018.42 --> 2020.00]  I may have misunderstood.
[2020.24 --> 2023.24]  Is that a product or a supporting technology that you guys are using?
[2023.24 --> 2026.42]  I mean, it's kind of the way we refer to things.
[2026.58 --> 2028.28]  We should have done a better job explaining it.
[2028.42 --> 2032.76]  So all the things we just talked about, we consider part of the magic brand at Shopify.
[2032.98 --> 2040.00]  So it's like the product taxonomy stuff, the text generation, the sidekick, the image generation in the background.
[2040.16 --> 2043.24]  So those are all magic features that Shopify offers.
[2043.80 --> 2044.04]  Gotcha.
[2044.04 --> 2049.40]  So it's kind of the AI enabling brand that's around all these things.
[2049.66 --> 2049.80]  Yep.
[2049.98 --> 2055.02]  So as you, you know, we've kind of talked a little bit about Sidekick, and we've gone through.
[2055.24 --> 2063.92]  There was another thing I always wanted to ask you about, and that was how your current array of kind of AI enabled capabilities that we've been talking about.
[2063.92 --> 2066.44]  How are you thinking about that going forward?
[2066.56 --> 2067.72]  Where are you looking at?
[2067.80 --> 2075.24]  How are you, you know, are you going to add any more in there that are announceable yet or maybe at least alludeable to?
[2075.52 --> 2083.34]  How are you thinking about kind of where you're at today versus kind of some of the things you might be doing in, you know, in the fairly near future and stuff?
[2083.34 --> 2085.80]  And we'll get into farther future a little bit later.
[2086.00 --> 2091.98]  I can't answer today, unfortunately, other announcements that are coming, but I think we can talk about generalities of like what's interesting, right?
[2092.12 --> 2092.50]  Fair enough.
[2092.50 --> 2100.60]  Some of the stuff that Mike talked about of like, you know, applying old techniques in new ways around commerce specific things.
[2100.88 --> 2104.72]  Like I think predictions and customization around that are interesting.
[2104.86 --> 2109.74]  I'd say like me personally, I think the thing that I get excited about is like the other modalities that are out there.
[2109.74 --> 2113.92]  Um, so going back to that reference from earlier, like chat GPT was cool.
[2114.26 --> 2118.54]  I feel like I had a second, uh, bout of chat GPT when the voice mode came out.
[2118.62 --> 2121.36]  I don't know if you've played with it, Chris, but it's like absolutely incredible.
[2121.62 --> 2130.96]  During the typical day, I have an ongoing, I probably, I, this is really terrible that I would say this, but I, I probably talked to chat GPT more than I talked to my wife.
[2132.14 --> 2133.40]  That's I'm hoping she doesn't.
[2133.40 --> 2134.04]  We'll keep that between us.
[2134.30 --> 2135.16]  Thank goodness.
[2135.28 --> 2137.20]  She doesn't want to hear me any more than she already does.
[2137.26 --> 2138.60]  So she won't hear this on the show.
[2138.60 --> 2143.46]  So, um, but yes, I, I have an ongoing conversation about a plethora of topics.
[2143.46 --> 2147.64]  So, which beckons back to the fact that this is moving so fast.
[2147.64 --> 2156.60]  Um, and you guys are, as you guys are having to kind of match your customer needs with products that support with the technologies that are driving that forward.
[2156.84 --> 2168.42]  What are some of the things that you're thinking about now for maybe, uh, as you go forward into the future and more specifically, how are you thinking about handling the risks associated?
[2168.42 --> 2170.70]  With changing technology right now.
[2170.70 --> 2180.28]  We've talked a little bit about constant experimentation and everything, but there's also a point where you kind of have to make investments, uh, in different directions and trade-offs and stuff like that.
[2180.28 --> 2187.16]  Other than the experimentation of that to support as you, this increasing line of capabilities that you guys are offering.
[2187.16 --> 2190.66]  How are you thinking about that risk directions and stuff?
[2190.94 --> 2207.18]  Do you think that commercial product offerings, for instance, one topic that comes up all the time on the show, do you think open source is going to overcome that and kind of take over, uh, since things are slowing a little bit on the frontier models in terms of the gains they're making and open source seems to be catching up faster.
[2207.18 --> 2211.60]  How are you guys thinking about problems like that as you're dealing with these business issues in your company?
[2212.06 --> 2213.60]  I think it will likely be hybrid.
[2213.98 --> 2217.02]  So like, I know we talked to kind of like our strategy is like everything all the time.
[2217.20 --> 2221.44]  So I, I can't imagine a world where the commercial offerings completely take over.
[2221.50 --> 2225.22]  And I really, I don't know if I can imagine a world where open source entirely takes over either.
[2225.80 --> 2227.54]  And I think that's probably a good thing for the world.
[2227.62 --> 2229.40]  Like, I think that's what drives the innovation, right?
[2229.42 --> 2231.16]  It's like a competition between the two.
[2231.16 --> 2234.06]  And there are some things that one is good at and the other is not.
[2234.18 --> 2237.56]  So like, I can't imagine a world where we aren't using both at Shopify.
[2238.42 --> 2245.38]  Can you talk a little bit about kind of how you see the strengths and weaknesses, recognizing it may change tomorrow, given how fast things are moving.
[2245.38 --> 2258.22]  But like when you look at that kind of what we might go with a commercial offering like ChatGPT or one of the other several biggest competitors versus the open source and probably the foundation infrastructure that you guys will have.
[2258.66 --> 2260.38]  How do you guys know where to go?
[2260.38 --> 2265.76]  Like, how do you know to go to ChatGPT as an API versus using a foundation model you're storing in your infrastructure?
[2266.56 --> 2269.76]  Well, I think it goes back to Mike's favorite point from earlier of evals.
[2269.92 --> 2272.44]  We got to have our compass because without the compass, we're lost.
[2272.72 --> 2273.92]  So that's how we answer which one.
[2274.18 --> 2278.30]  But I think the other part of like you're asking, like, which one is good at what at this point?
[2278.52 --> 2283.64]  And so like, I think in general, the way to frame it is like open source, the power is in the control.
[2284.10 --> 2289.56]  It's like you're guaranteed to run this exact model with this exact set of training data with this exact outcome.
[2289.56 --> 2290.36]  So it's very predictable.
[2290.76 --> 2295.06]  You have way more control over the training process and like the post training process.
[2295.06 --> 2297.26]  And like you just get a lot more knobs.
[2297.40 --> 2297.58]  Right.
[2297.78 --> 2300.18]  But also with great power comes great responsibility.
[2300.44 --> 2300.58]  Right.
[2300.58 --> 2304.14]  Like there's a cost to operating all those knobs and knowing what the correct values are for that.
[2304.14 --> 2310.20]  So for problems that you have pretty fully defined and you know exactly how you want to do it, it's like open source is great.
[2310.46 --> 2310.64]  Right.
[2311.10 --> 2312.70]  The commercial models, fewer knobs.
[2313.06 --> 2317.74]  But the thing that's great about that is like, you know, the defaults out of the box usually work pretty well.
[2317.98 --> 2318.18]  Right.
[2318.24 --> 2323.10]  And so like I think if you're looking at things that are early on in prototyping, like the commercial models work great.
[2323.20 --> 2323.36]  Right.
[2323.36 --> 2325.90]  They can get you from zero to one real quick.
[2325.90 --> 2335.52]  And then when you get to that one, you realize like, oh, well, I want to get to 2.0 and like sometimes it necessitates a need to that shift to an open source model to get that extra control out of it.
[2335.52 --> 2339.22]  There's kind of this question of what size of a problem are you trying to solve?
[2339.28 --> 2350.32]  If you're trying to solve a, you know, a central do everything, you know, the founder that you would, the co-founder that you wish you had model, we're going to need to pull out all the guns.
[2350.58 --> 2350.74]  Right.
[2350.76 --> 2357.12]  And really put everything we can into making this, leveraging as much power as we as we can.
[2357.38 --> 2357.56]  Right.
[2357.66 --> 2361.22]  And the question is just what is the most powerful for this task at this time?
[2361.22 --> 2369.12]  There's another side of things where maybe we're trying to solve problems that aren't supersized problems, but they're more manageable problems.
[2369.26 --> 2369.40]  Right.
[2369.46 --> 2371.12]  Or maybe we need to do it at scale.
[2371.52 --> 2376.32]  And, you know, of course, the commercial models are getting faster and faster and cheaper and cheaper.
[2376.88 --> 2385.56]  But when you need to do something at scale, it might be worthwhile to distill a model from some patterns and then run it at scale.
[2385.56 --> 2390.14]  We have billions of products if you look over our entire history.
[2390.14 --> 2400.42]  Doing that at scale for, you know, the product that Matt described where we understand all the different attributes and the taxonomy and we normalize the description of those products.
[2400.64 --> 2403.64]  That's a true engineering feat that we need to work on.
[2403.72 --> 2407.92]  And that may not be a great idea to send that to GPT-01, right?
[2408.82 --> 2409.30]  Absolutely.
[2409.94 --> 2413.04]  One question, I'm guessing, Mike, this is coming to you.
[2413.04 --> 2419.18]  The last two, three years, we've been so focused on LLMs and generative AI capabilities.
[2419.96 --> 2426.44]  And I know in general, the industry is starting to kind of also kind of pull back and look at some of the other things.
[2426.82 --> 2430.94]  Things we used to talk about, other technologies in the AI space we talked about a lot.
[2430.94 --> 2436.76]  It seems that some industries, things like, you know, reinforcement learning and, you know, CNNs and things like that.
[2437.02 --> 2445.94]  Depending on the industry, I think in my own experience as I've talked to different people, some find utility in these other architectures with other purposes and some don't.
[2446.62 --> 2447.36]  How are you guys?
[2447.50 --> 2450.62]  Are you really primarily focused on LLMs and generative?
[2450.62 --> 2460.70]  Or do you have use cases where some of the other technologies that we haven't talked about as much lately but are still very much out there in industry, are they coming into play for you guys?
[2460.94 --> 2461.04]  Yeah.
[2461.12 --> 2463.82]  So this might be where we appeal the technology.
[2464.30 --> 2465.36]  I need one more layer, right?
[2466.18 --> 2469.92]  At a base level, any neural net is a universal approximator, right?
[2469.98 --> 2473.74]  And so if we have enough data, there is a big enough neural net that we'll solve.
[2473.90 --> 2475.60]  Just an MLP, right?
[2475.94 --> 2476.16]  Sure.
[2476.16 --> 2476.84]  A fully connected neural network.
[2476.84 --> 2494.00]  And so the way I tend to think about it, whether it's a CNN or a heavy attention model or an RNN, whatever it is, all that's really in the business of doing is making it so that, you know, even though there is a number of neurons, it might be way too many neurons, right?
[2494.10 --> 2496.02]  And we might need way too much data in order to do that.
[2496.02 --> 2504.56]  And all of these are really just tactics for reducing the amount of data that we need in order to approximate the patterns that we want.
[2504.56 --> 2517.70]  Right now, for sure, heavy attention models, whether it's traditional transformers or evolutions, like you might see in the original 2017, attention is all you need transformer architecture to what you see in Lama.
[2518.14 --> 2522.40]  These are kind of like tweaks and they're still very multi-head attention focused.
[2522.40 --> 2535.96]  There are other techniques like the one I described for e-commerce that are making substantial changes, like removing the softmax out of multi-head attention, which is a, you know, sort of like having the sigmoid as our activation function 10 years ago.
[2536.18 --> 2539.04]  It was just a mistake and a sociological mistake at that, right?
[2539.04 --> 2548.54]  So seeing small changes like that, that maybe move us out of transformer architectures, I think that we're definitely in an era where that makes sense.
[2549.06 --> 2552.00]  There's also kind of combinations of things, right?
[2552.02 --> 2566.90]  So you mentioned reinforcement learning, there's GNN architectures, and these are actually compatible with vision transformers for planning and reinforcement learning, you know, using transformers for your aggregation functions for a graph neural network.
[2566.90 --> 2591.70]  And so it's not an either or, it's that now we have another tool for either in the former case, modeling the world so that we can do a good job at our Q learning and our policy learning, or do a good job in capturing the right information when we have a graph structure of how we've organized the different kinds of nodes, the different kinds of, in our case, merchants and products and buyers.
[2591.70 --> 2598.72]  That being said, you know, there's another way of taking your question, which is, look at when are transformers going to be done and are they gone already?
[2599.12 --> 2605.26]  That was on my mind as well, actually, because we've been, everyone's talking about, okay, what does the post-transformer world look like?
[2605.34 --> 2605.94]  So, yes.
[2606.34 --> 2611.02]  I think I can say this, and I say this to my students pretty religiously.
[2611.20 --> 2617.84]  I'm going to make this claim with full understanding that you should never make a prediction that will be falsified in your lifetime.
[2617.84 --> 2621.42]  I'm pretty sure transformers is not the last architecture out there.
[2621.70 --> 2628.66]  It seemed for a decade that CNN was almost synonymous with vision since 2012, right?
[2629.44 --> 2630.50]  And now it's not.
[2630.74 --> 2636.38]  And if you would have asked me in the late 20 teens, if I thought it was, I'd probably say the same thing.
[2637.28 --> 2638.38]  It's a heavy thing.
[2638.92 --> 2639.84]  It's a heavy bet.
[2639.84 --> 2647.36]  But CNN seemed to be the top of the hill, and they seemed to do such a good job with image classification.
[2648.12 --> 2653.10]  It's hard to imagine what will replace it, but probably it's not the last chapter of the story.
[2653.16 --> 2656.04]  And I think that you could probably say the same thing for transformers.
[2656.04 --> 2662.84]  So, a little bit ironically, and you've sort of kind of covered this territory a little bit with that last answer, Mike.
[2663.24 --> 2672.50]  From each of you, we usually finish the show really wanting to get perspectives from our guests on kind of what the future looks like.
[2672.98 --> 2680.10]  And with each of you addressing kind of different areas, you probably have somewhat different answers based on your focus and stuff.
[2680.10 --> 2694.12]  And Mike, recognizing that you've already kind of touched a little bit on the future, but I'm actually, despite your comment about not making predictions that might prove falsified in your lifetime, I'm going to ask you both to kind of do that.
[2694.12 --> 2708.76]  If you're looking out, and I'll let you kind of decide on what time frame works for you, but maybe beyond the short term, waxing poetic a little possibly, and trying to say, what do you think you're going to see?
[2708.76 --> 2710.56]  What do you want to see?
[2710.88 --> 2720.66]  And how might your various jobs and how your company serves customers, you know, how do you see this fast moving, there are twists and turns all along the way that catch us all by surprise.
[2720.96 --> 2723.00]  How do you see that playing out from each of you?
[2723.20 --> 2727.90]  Matt, if you could lead off, and then Mike, I'll come back to you for that.
[2728.36 --> 2732.76]  I think what's most exciting about this, I mean, when I grew up, I remember when we first got the internet.
[2732.76 --> 2735.12]  And like, it was like the first ISP out there.
[2735.20 --> 2736.50]  And there was like a dial up modem.
[2736.50 --> 2738.02]  And there was like a BBS.
[2738.22 --> 2741.16]  Like it was just, that was like the first wave of technology to me.
[2741.20 --> 2742.90]  And like, that's how I got into this field.
[2743.34 --> 2746.52]  And then I feel like the mobile revolution caught me by surprise.
[2746.52 --> 2750.48]  Like I think at the moment, like I knew when the first iPhone came out, I was like, I need to have one of those.
[2750.86 --> 2754.26]  But what I didn't expect was like how much the world would change after that.
[2754.58 --> 2758.48]  And it feels like this time around, I wasn't a big believer in Web3.
[2758.60 --> 2759.90]  I was like, what is this Web3 business?
[2760.02 --> 2763.94]  But like, I feel like this is again, that same kind of shift.
[2764.62 --> 2766.06]  So I'm just going to ignore Web3.
[2766.20 --> 2767.34]  I think this is the real Web3.
[2767.50 --> 2767.88]  It's AI.
[2768.48 --> 2770.18]  And so like, how does this play out, right?
[2770.20 --> 2778.86]  Like, I don't think what's different this time is that like for the last, I don't know, 70 years that we've had computers, like we as humans have had to conform to like how computers work.
[2779.00 --> 2780.76]  Like at first we wrote assembly code.
[2780.86 --> 2782.62]  At first we wrote like literally bits.
[2782.62 --> 2784.26]  Then we wrote assembly code.
[2784.54 --> 2786.28]  Then we're like, well, maybe we should have languages.
[2786.62 --> 2789.12]  And it's like, OK, so we're slowly crawling there.
[2789.26 --> 2791.90]  And then the next revolution is like, oh, we should have point and click.
[2791.98 --> 2792.98]  And so these boxes.
[2793.18 --> 2801.10]  And so now we have a world where everybody spends, you know, eight hours a day clicking on little colored boxes and then typing into other colored boxes like characters on a keyboard.
[2801.58 --> 2808.74]  And I think what's what's fascinating to me is that we've become we've shaped who we are to conform to how computers work today.
[2808.74 --> 2812.92]  But I think this point in time and I'm sorry, I'm giving it 10 years out from now.
[2813.20 --> 2813.74]  No, it's fine.
[2813.86 --> 2814.70]  All that's going to change.
[2814.80 --> 2820.92]  Like, I think that whole like all these browsers that we click buttons on to like set settings, like all that is going to go away.
[2820.92 --> 2832.52]  I think it's going to be that we interact with like an agent or some amorphous entity that it's like and instead of, you know, listing all the steps of like first search for this, then click on this link, then do this thing.
[2832.58 --> 2834.98]  It's like be like I would like to buy a box of toothpaste.
[2835.46 --> 2836.54]  And it's like the agent's like, great.
[2836.64 --> 2841.34]  Do you want to buy one for that ships tomorrow or do you want one that's like cheaper but ships next week?
[2841.36 --> 2842.74]  And you're like the cheaper one.
[2842.86 --> 2843.74]  And then it's like done.
[2844.06 --> 2844.40]  Right.
[2844.42 --> 2845.76]  You didn't fill out a credit card form.
[2845.84 --> 2847.10]  You didn't click through 10 sites.
[2847.16 --> 2848.00]  You didn't do any of that.
[2848.70 --> 2850.08]  So like I'm going to put my bet on that.
[2850.08 --> 2852.82]  It's like I just think the web will change again.
[2853.04 --> 2855.34]  Like I think we've gotten so used to SAS and all these models.
[2855.34 --> 2857.50]  And like I'm just I don't know how long it's going to take.
[2857.56 --> 2858.56]  That's why I'm like 10 years out.
[2858.64 --> 2858.86]  I don't know.
[2858.96 --> 2861.34]  It might be three years out, but it might also be 20.
[2861.66 --> 2864.70]  But I don't think we're going to be typing in boxes in 20 years from now.
[2865.38 --> 2865.74]  Good answer.
[2866.54 --> 2867.52]  Mike, back to you.
[2868.04 --> 2870.98]  Yeah, I think I'm going to flank this from both directions.
[2872.20 --> 2877.88]  So I spent a little bit of time in the self-driving space years ago.
[2877.88 --> 2890.52]  And this was during the the I think the maximum hype period for self-driving where, you know, everyone I talked to said, oh, well, people won't even need to drive in five years.
[2890.52 --> 2892.04]  And this was more than five years ago.
[2892.04 --> 2898.24]  And on the one hand, just across the bay, Waymo is giving rides to people.
[2898.36 --> 2898.46]  Right.
[2898.52 --> 2900.38]  Not at scale yet, but it is.
[2900.48 --> 2900.62]  Right.
[2900.88 --> 2901.62]  For sure.
[2901.82 --> 2906.92]  You know, a lot of people said my son would never need to get a license and he's about to get his driver's permit.
[2907.06 --> 2907.20]  Right.
[2907.20 --> 2916.10]  So just to draw an analogy, I think it's reasonable to expect what Matt is expecting of having kind of like a self-driving assistant that can do that.
[2916.50 --> 2921.68]  I have all the respect for Matt in the world because he was careful about how he's going to do the time, not five years or whatever.
[2922.08 --> 2927.46]  There's probably going to be a little bit of difficulty smoothing down the edges for that.
[2927.46 --> 2935.64]  And luckily, you know, a crash with with a self-driving assistant is far less dangerous than a self-driving car.
[2935.76 --> 2938.86]  So it could be that we need we get imperfect models there.
[2939.38 --> 2941.06]  I'll take an extra five boxes of toothpaste.
[2941.40 --> 2941.86]  That seems right.
[2943.44 --> 2949.10]  So that's that's one side of flanking it is, you know, we very well will.
[2949.26 --> 2949.40]  Right.
[2949.44 --> 2952.34]  There will be a self-driving moment for these assistants.
[2952.34 --> 2959.28]  And how long out is completely on the same page with Matt that that's, you know, we're going to hit some bumps before we actually get there.
[2959.94 --> 2971.58]  One thing that I feel very confident of is that we are going to change the way we organize and access and utilize information.
[2971.82 --> 2978.06]  This is going to be a forcing function that we really haven't seen since early search days for the Internet,
[2978.06 --> 2982.64]  which is also a way of just completely transforming how we organize and access information.
[2982.98 --> 2993.12]  And, you know, a lot of people you will talk to will already say that they go to their favorite LLM first before they go to a search experience.
[2993.52 --> 3000.50]  And there are also a whole host of product and interface and questions like that about what's going to be the best way of doing this.
[3000.50 --> 3019.34]  But, you know, there's also once again piggybacking on something that Matt said, you know, it is incredibly significant that we are now speaking in the same language, quite literally, when we want to access and refine the information we're looking for.
[3019.42 --> 3021.60]  And that's something that's really never happened before.
[3022.36 --> 3022.82]  Well said.
[3023.14 --> 3026.22]  Well, gentlemen, thank you very much for coming on the show.
[3026.30 --> 3027.40]  It was really interesting.
[3027.40 --> 3029.26]  I learned a lot.
[3029.52 --> 3032.28]  And thanks for sharing your perspectives going forward.
[3032.34 --> 3038.84]  I hope you guys will come back as things evolve and you have more things that you want to share with the audience.
[3039.10 --> 3040.02]  Thanks for coming on.
[3040.50 --> 3041.04]  I'd be happy to.
[3041.12 --> 3041.60]  Thanks, Chris.
[3041.74 --> 3042.26]  Thanks, Chris.
[3042.26 --> 3042.30]  Thanks, Chris.
[3049.52 --> 3050.56]  All right.
[3050.78 --> 3052.68]  That is our show for this week.
[3052.68 --> 3058.98]  If you haven't checked out our ChangeLog newsletter, head to changelog.com slash news.
[3059.22 --> 3061.46]  There you'll find 29 reasons.
[3061.68 --> 3065.04]  Yes, 29 reasons why you should subscribe.
[3065.52 --> 3066.88]  I'll tell you reason number 17.
[3067.44 --> 3070.24]  You might actually start looking forward to Mondays.
[3070.42 --> 3073.10]  Sounds like somebody's got a case of the Mondays.
[3073.46 --> 3078.06]  28 more reasons are waiting for you at changelog.com slash news.
[3078.06 --> 3083.94]  Thanks again to our partners at Fly.io to Breakmaster Cylinder for the beats and to you for listening.
[3084.38 --> 3086.98]  That is all for now, but we'll talk to you again next time.
[3086.98 --> 3094.30]  Okay.
[3094.96 --> 3095.92]  Game on.
[3095.98 --> 3096.30]  Game on.
[3096.30 --> 3097.96]  Game on.
[3097.98 --> 3098.00]  Game on.
[3098.00 --> 3098.98]  chips on Apple.
[3099.24 --> 3100.04]  Game on.
[3100.04 --> 3100.14]  Game on.
[3100.14 --> 3100.24]  Game on.
[3100.24 --> 3101.66]  Game on.
[3101.66 --> 3104.26]  Game on.
[3104.54 --> 3106.96]  Game on.
[3108.30 --> 3111.00]  Game on.
[3111.00 --> 3116.18]  Game on.
