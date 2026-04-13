[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[42.94 --> 47.24]  Welcome to another Fully Connected episode of Practical AI.
[47.64 --> 53.06]  In these episodes, Chris and I keep you fully connected with everything that's happening
[53.06 --> 54.24]  in the AI community.
[54.24 --> 59.44]  We're going to take some time to discuss the latest AI news, and then we'll share some
[59.44 --> 62.80]  learning resources to help you level up your machine learning game.
[63.32 --> 64.78]  This is Daniel Whitenack.
[64.88 --> 71.00]  I'm a founder and data scientist at Prediction Guard, and I'm joined, as always, by my co-host,
[71.16 --> 74.72]  Chris Benson, who is a tech strategist at Lockheed Martin.
[75.22 --> 75.90]  How are you doing, Chris?
[76.42 --> 77.18]  Doing cool.
[77.30 --> 81.88]  I'm trying to figure out how did we survive before all these great new models and stuff?
[81.88 --> 84.20]  Like, it's changed my...
[84.20 --> 84.50]  Oh.
[84.68 --> 85.86]  Yeah, it's been crazy.
[86.14 --> 86.32]  Yeah.
[86.40 --> 94.44]  I just created a post for LinkedIn, and I was, like, grabbing text, putting it into chat
[94.44 --> 97.14]  GPT, like, getting nice rephrasing.
[97.32 --> 98.72]  And then I'm like, oh, I need an image.
[99.14 --> 102.42]  And in particular, we'll talk about it a little bit in this episode.
[102.42 --> 108.80]  But I was like, oh, there's this free willy model from stable AI, which is, like, whale-themed,
[108.94 --> 109.20]  right?
[109.32 --> 110.86]  And then I've got the llama thing.
[111.12 --> 117.30]  So I just went to stable diffusion Excel on ClipDrop and said, hey, generate me an image
[117.30 --> 119.74]  with a whale and a llama together.
[120.16 --> 125.72]  And, you know, how do I even post to LinkedIn before without these things?
[125.78 --> 126.90]  It's like a different world.
[126.90 --> 127.50]  Yeah.
[127.86 --> 130.70]  2023 versus 2022 is totally different.
[131.24 --> 135.14]  The content generation, the way you code, it's a different world.
[135.68 --> 135.88]  Yeah.
[136.12 --> 146.24]  And this week, as most weeks are, it seems like, in 2023 had some pretty groundbreaking announcements
[146.24 --> 151.30]  and releases, which we're going to dive into a bunch of those things.
[151.30 --> 153.64]  There's just a huge amount to update on.
[153.88 --> 158.90]  And I think it's a good time for one of these episodes between you and I to just parse through
[158.90 --> 162.12]  some of the new stuff that is hitting our feeds.
[162.96 --> 163.54]  So, yeah.
[164.18 --> 166.22]  Well, I mentioned llama.
[166.70 --> 168.78]  One of the big things this week was llama two.
[168.92 --> 175.00]  But I think before we jump into llama two, which I think was maybe the main thing dominating
[175.00 --> 180.36]  at least my world this week, it might be worth just taking a little bit of time to highlight
[180.36 --> 187.46]  something outside of the stream of large language models, which also crossed my desk this week,
[187.48 --> 188.90]  which I thought was really cool.
[189.22 --> 193.22]  It's this latest version of Nerf.
[193.22 --> 199.22]  This is work from Google presented at ICCV 2023.
[199.88 --> 205.48]  So it's called ZIP Nerf, Anti-Alias Grid-Based Neural Radiance Field.
[205.72 --> 206.96]  That's quite a name right there.
[207.30 --> 208.90]  It is quite a name.
[209.20 --> 212.12]  It stands for neural radiance field.
[212.30 --> 218.68]  So Nerf, it's like camel-cased in capital N, small E, and capital RF.
[218.68 --> 227.58]  Nerf, these are fully connected neural networks that create unique novel views of complicated
[227.58 --> 232.28]  3D scenes based on a set of images that are input.
[232.48 --> 235.82]  So I don't know if you've seen that video yet.
[236.16 --> 237.94]  I'm looking at it as we are talking.
[238.16 --> 242.28]  And when you say the video, I know which video you're talking about because it's amazing.
[242.52 --> 243.54]  I've just left it on.
[243.62 --> 244.68]  It's pretty spectacular.
[245.30 --> 245.46]  Yeah.
[245.46 --> 249.82]  So this is a podcast, so it's hard to express some of this for people.
[250.00 --> 256.48]  If you just search for ZIP Nerf, you can go to the page for this paper, which is a great summary.
[256.74 --> 258.46]  But there's a video on the page.
[258.56 --> 265.94]  And just to describe what it is, imagine this kind of complicated house with a bunch of different
[265.94 --> 269.76]  rooms and an outdoor patio sort of garden area.
[269.76 --> 276.56]  And the video is actually this kind of almost like a drone fly through of the house and then
[276.56 --> 277.64]  the outdoor area.
[278.12 --> 283.90]  If you imagine a drone flying through a house, there's hats and coats and toys and couches
[283.90 --> 286.78]  and plants and all sorts of things everywhere.
[286.78 --> 291.52]  But the video is extremely seamless and it's not generated by a drone.
[291.52 --> 300.60]  It's actually just generated by interpolating between a whole bunch of 2D images and then
[300.60 --> 304.30]  interpolating from that the 3D scene.
[305.08 --> 306.02]  So, yeah, I don't know.
[306.08 --> 307.16]  What are your impressions, Chris?
[307.72 --> 312.52]  First of all, from the perspective, the drone flight, if you will, that you have as a perspective
[312.52 --> 315.92]  viewing it is like the best drone operator in the history of the world.
[316.16 --> 316.40]  Yeah.
[316.50 --> 318.60]  It'd probably be hard to get one to do that.
[318.60 --> 324.04]  Yeah, you're not going to get a real drone operator that could fly that amazingly and
[324.04 --> 324.90]  get those things.
[324.90 --> 325.86]  It's just phenomenal.
[326.42 --> 332.10]  And the house is like, for a moment you look at it and I mean, it looks real.
[332.48 --> 339.22]  But I have noticed it's cluttery, but it's immaculately clean at the same time as well.
[340.40 --> 342.98]  The clutter is cleanly distributed and stuff.
[343.12 --> 347.40]  So, I wish when my house was cluttered, it looked as beautiful as this house.
[347.40 --> 348.44]  It doesn't.
[348.98 --> 353.64]  But yeah, I mean, just like if you didn't know, if you weren't listening to the, you
[353.64 --> 357.08]  know, Practical AI podcast to go look at it or something like that and you just stumbled
[357.08 --> 361.02]  upon it, you'd think it was a drone video, you know, if you didn't have the education
[361.02 --> 362.72]  and go, oh my God, this is just really cool.
[362.90 --> 365.12]  I wonder how, you know, wonder what they're doing here.
[365.64 --> 369.28]  But it's indistinguishable from real life for all practical purposes.
[369.28 --> 369.60]  Yeah.
[369.80 --> 376.28]  And so it's based on 2D images and then there are these generated interpolations, which
[376.28 --> 381.54]  maybe gets to, there was something that we were talking about prior to hitting the record
[381.54 --> 389.24]  button, which was this whole field of generative AI is sometimes conflated with large language
[389.24 --> 391.22]  models or chat GPT.
[391.22 --> 397.80]  But there's a whole lot going on in generative AI that's not language related or maybe even
[397.80 --> 399.58]  based on language related prompts.
[399.70 --> 405.84]  So I mentioned that image that I generated for my LinkedIn post that was still a text prompt
[405.84 --> 408.82]  into a model that generated an image.
[408.82 --> 416.14]  But here what we're seeing is we've got static 2D images that are input to a model that's
[416.14 --> 422.38]  actually generating a whole bunch of different perspectives that are synthesized in a 3D scene.
[423.12 --> 432.04]  So this is, I would say, still fitting into our current landscape and world of generative AI,
[432.44 --> 437.52]  but it's not a text in, text out or text in, image out model.
[437.92 --> 438.02]  Right.
[438.02 --> 442.36]  And I think people, there's so much coming at people right now.
[442.60 --> 444.40]  I think, you know, we keep talking about that this year.
[444.56 --> 449.34]  In the five years we've been doing this podcast, we've never had a moment like the last few
[449.34 --> 453.14]  months where things have been coming, new things have been coming at people so fast,
[453.20 --> 456.14]  new terms, new models, and people are trying to distinguish.
[456.32 --> 460.28]  So it's pretty, I think it's pretty fair that people are trying to make sense of how they
[460.28 --> 460.80]  relate together.
[460.80 --> 465.58]  And there's a lot of connecting between, you know, the idea of generative and the idea of large
[465.58 --> 467.88]  language models overlap in a lot of areas.
[468.02 --> 471.58]  And you have models that are both and you have models that are just one and stuff.
[471.68 --> 474.76]  But I think it's a brave new world right now in terms of the amount.
[474.98 --> 478.76]  Every show we're just trying to figure out what matters right now because there's a lot
[478.76 --> 479.30]  we're not hitting.
[479.30 --> 479.84]  Yeah.
[479.84 --> 487.40]  And this side of things, maybe like the 3D or video or image based side of things, I know
[487.40 --> 491.88]  has its own set of kind of transformative use cases that are popping out.
[492.04 --> 498.36]  I even remember a little while ago there was some technology, I think from Shopify, but others
[498.36 --> 504.94]  have done this as well, where maybe you have a room in your house and you want to see how
[504.94 --> 510.04]  you can transform it with new furniture or something that, of course, you could buy.
[510.04 --> 517.94]  This is a real kind of e-commerce or retail sort of use case for some of the scene technology
[517.94 --> 519.44]  of a different kind.
[519.44 --> 526.20]  If you think of this sort of technology that can take 2D things and create these 3D scenes,
[526.44 --> 531.24]  certainly there's use cases within game development, for example.
[531.24 --> 540.04]  But even other cases where maybe AI has never impacted the process as much like in real estate,
[540.12 --> 540.70]  for example.
[540.70 --> 548.00]  You know, how expensive is it to literally have a person come out with specialized camera
[548.00 --> 548.42]  gear?
[548.66 --> 554.38]  I know that we've had this in the past where it takes a special person to come out with
[554.38 --> 559.28]  special camera gear to capture the kind of 3D walkthrough, essentially the street view
[559.28 --> 565.02]  walkthrough of your house and map that onto an actual schematic of your house.
[565.02 --> 573.18]  And here, if you imagine someone, maybe I'm now selling my house myself without a real estate
[573.18 --> 579.92]  agent and I can take an app potentially and go through my house just taking 2D images and
[579.92 --> 585.12]  create this really cool kind of fly around 3D view that's interactive.
[585.54 --> 591.88]  That's really, I think, a powerful transformative change for a number of different industries.
[591.88 --> 596.96]  I came across a company called Luma AI in one of the posts about this technology.
[597.52 --> 602.70]  I don't know exactly how much of the, if they're even using the Zip Nerf stuff, but certainly
[602.70 --> 609.70]  some things related to Nerf to take these 2D images and they have an app that will create
[609.70 --> 615.86]  3D views, which is pretty cool to see some of this kind of hit actual real users.
[616.66 --> 619.66]  We keep talking about the fact that we've hit this inflection point where it's hitting all
[619.66 --> 623.64]  the, you don't have to be in the AI world, you know, for this to have a big impact.
[624.12 --> 631.04]  And so, you know, it's very easy looking at the Zip Nerf video to imagine walking around
[631.04 --> 636.14]  with your cell phone on an app and you're just kind of like walking around and the app takes
[636.14 --> 640.08]  care of whether it's video or whether it's still images or what, and it just uploads it
[640.08 --> 643.68]  to this and produces this, you know, amazing, you know.
[643.68 --> 646.08]  So it's not your walk around that it's doing.
[646.16 --> 649.78]  It takes that as raw video, but then it produces this super high quality thing.
[649.86 --> 654.92]  So yeah, I mean, I think this is another case where there's this one technology with thousands
[654.92 --> 658.24]  of use case possibilities, you know, where it just changes everything.
[658.68 --> 658.76]  Yeah.
[658.86 --> 664.70]  And maybe also in the, it'd be curious to know your reaction to this also with respect to
[664.70 --> 668.46]  kind of the industrial use cases where.
[668.46 --> 674.92]  I've been thinking about, of course, like capturing 3D scenes is very important.
[674.92 --> 682.24]  For example, for simulated environments where you're trying to maybe train an agent or you
[682.24 --> 690.22]  even kind of an industrial training for human sort of sort of scenario where you want to kind
[690.22 --> 696.46]  of take someone into an environment that it's physically hard to bring a lot of people into.
[696.46 --> 696.86]  Yeah.
[696.86 --> 699.04]  Or there could be safety issues and such.
[699.34 --> 699.44]  Yeah.
[699.50 --> 700.36]  Safety issues.
[700.52 --> 702.94]  I don't know if that, that sparks things in your mind.
[703.06 --> 711.72]  I think in the industrial sense, this could have a more B2B sort of impact than just a consumer
[711.72 --> 712.26]  app.
[712.50 --> 712.76]  Sure.
[712.90 --> 716.84]  I mean, a simple thing, and this is, I'm making something up in the next thing I say, but
[716.84 --> 722.72]  it's very easy for me to imagine intelligence agencies that are, you know, like if you go back
[722.72 --> 727.62]  some years to when Osama bin Laden was found and they had, you know, various imagery and
[727.62 --> 727.94]  stuff.
[728.04 --> 732.04]  But with stuff like this, they might take all those images that they're getting from various
[732.04 --> 734.94]  sources and produce, you know, a high.
[735.12 --> 735.98]  Like a flyover.
[736.24 --> 736.96]  A very, yeah.
[737.04 --> 741.14]  A flyover and very photorealistic of certain parts of the compound where that kind of imagery
[741.14 --> 744.42]  and that can be used in a military operation subsequently.
[744.54 --> 745.50]  Now I'm making that up.
[745.50 --> 750.22]  So don't, nobody should take that as a thing, but it's not hard to imagine that.
[750.30 --> 755.42]  It's not hard to imagine a lot of factory uses and other industrial things where you
[755.42 --> 761.30]  have safety issues, you have a limited access kind of concerns where you're trying to convey
[761.30 --> 763.12]  that, but there's a lot of mundane things.
[763.12 --> 767.10]  There's a lot of home-based things and small business-based things, as you pointed out the
[767.10 --> 767.96]  real estate one earlier.
[768.18 --> 772.28]  So this is just one technology that we're talking about so far.
[772.28 --> 779.76]  Yeah, and I think what you're saying, it illustrates how this is impacting very large organizations
[779.76 --> 783.46]  all the way down to small organizations.
[784.00 --> 785.26]  Yeah, sole proprietorships.
[785.66 --> 791.98]  Yeah, and it's interesting how, like if we just take this use case, for example, these
[791.98 --> 800.64]  kind of 3D scenes, kind of large scale organizations that maybe their bread and butter was either the
[800.64 --> 809.22]  compute associated with like rendering videos and 3D scenes or their hardware providers that
[809.22 --> 816.18]  are creating specialized kind of 3D type of equipment, like their whole business model,
[816.18 --> 821.16]  they've got to be thinking similar to other organizations that are dealing with maybe language
[821.16 --> 825.42]  related problems that are thinking about these things with respect to LLMs.
[825.42 --> 830.40]  There's a fundamental shift in maybe how their businesses will operate, but then at the same
[830.40 --> 836.92]  time, it provides an opportunity for the kind of small to medium businesses to embrace this
[836.92 --> 846.38]  technology very quickly and actually make innovative products that can be widely adopted very quickly
[846.38 --> 849.60]  and actually be competitors within an established market.
[849.60 --> 857.56]  So there's an established market for 3D things that has been quite expensive over time in terms
[857.56 --> 859.38]  of access to that technology.
[859.72 --> 862.56]  So now that whole market's going to change.
[862.62 --> 866.66]  I think a lot of the players will be these kind of small to medium sized businesses.
[867.14 --> 867.38]  I agree.
[867.50 --> 872.54]  I think there's a moment here that kind of ironically, because people are so worried about like the
[872.54 --> 875.70]  impact on human creativity because of all these models and stuff like that.
[875.70 --> 880.60]  But on a more positive note, there's this huge opportunity that you're just now alluding
[880.60 --> 885.32]  to for people that if you can connect the dots as things are coming out and you can stay on
[885.32 --> 887.22]  top of it, it's a great equalizer.
[887.80 --> 893.94]  And so it will clearly change many, many markets that are out there and many, many industries.
[894.54 --> 899.34]  And so there's huge opportunities for those who want to surge ahead at this moment and take
[899.34 --> 900.24]  advantage of that.
[900.24 --> 904.70]  And so I think that the message we tend to see in the media tends to be a little bit
[904.70 --> 910.10]  doomy and gloomy on that, but it kind of discounts the fact that change isn't always a bad thing.
[910.56 --> 915.42]  People are afraid of it, but there's huge, huge opportunities here as well.
[915.84 --> 917.88]  If people choose to go find them.
[917.88 --> 937.48]  Well, Chris, there is a new llama in town.
[937.74 --> 938.24]  I know.
[938.78 --> 939.56]  Llama 2.
[939.88 --> 940.84]  Llama 2.
[940.84 --> 941.84]  Llama 2.
[941.84 --> 950.84]  Basically destroyed all of my feeds and concentration this week when it was released because it is
[950.84 --> 959.46]  quite, to me, an encouraging thing, but also another transformative step in what we're doing.
[960.12 --> 967.40]  So Llama 2, for those that maybe lack the context here, Meta or Facebook or however you want to
[967.40 --> 977.40]  refer to it, Meta had released a large language model called Llama, which was extremely useful.
[977.70 --> 982.72]  It was a model where you could host it yourself as opposed to like OpenAI.
[983.16 --> 985.94]  You could get the weights and host it yourself.
[986.22 --> 992.98]  But the original Llama had a very restrictive licensing and access sort of pattern, even though
[992.98 --> 997.10]  you could kind of download the weights from maybe like a BitTorrent link or something like
[997.10 --> 998.84]  that, and those propagated.
[999.62 --> 1006.84]  Technically, if you got those weights, you were still restricted by a license that prevented
[1006.84 --> 1009.38]  commercial use cases specifically.
[1010.24 --> 1016.42]  And now with Llama 2, Meta's released the kind of follow-on to Llama, and we can talk through
[1016.42 --> 1022.50]  some of what the differences are and what it is and some of what went into it.
[1022.50 --> 1029.84]  But I think one of the biggest things, which is, I think, going to create this huge ripple
[1029.84 --> 1034.52]  effect throughout the industry is that they've released it with a commercial license.
[1034.90 --> 1044.90]  As long as on the day that Llama 2 was released, you as a commercial entity don't have greater than
[1044.90 --> 1047.96]  700 million monthly active users.
[1048.62 --> 1050.40]  You can use it for commercial purposes.
[1051.26 --> 1057.34]  So maybe if my company, maybe later on, has 700 million monthly active users, which would
[1057.34 --> 1058.66]  be great, probably never.
[1058.98 --> 1061.12]  But there'll be something past Llama 2 by then, though.
[1061.30 --> 1061.56]  Yes.
[1061.60 --> 1065.40]  If it does, though, I could still actually use it because it's only on the release date.
[1065.40 --> 1071.32]  So on the release date, which was this week, as long as you didn't have greater than
[1071.32 --> 1077.90]  700 million monthly active users, you can use this in your business for commercial use
[1077.90 --> 1078.26]  cases.
[1078.42 --> 1082.74]  And I think that's going to have a huge ripple effect downstream.
[1082.92 --> 1087.40]  And we can talk about the model itself here in a second, but maybe just I'll pause there
[1087.40 --> 1089.18]  to get your reaction on that, Chris.
[1089.30 --> 1093.02]  It made me smile when I heard that because it's kind of like saying, so long as you don't
[1093.02 --> 1095.56]  compete with us at Meta, you can use this for commercial.
[1096.00 --> 1097.26]  Oh, it's totally true.
[1097.36 --> 1097.52]  Yeah.
[1097.56 --> 1098.54]  Like, who is that?
[1098.60 --> 1098.80]  Right.
[1098.80 --> 1100.22]  So that's Snapchat.
[1100.74 --> 1101.08]  Yes.
[1101.66 --> 1102.02]  TikTok.
[1102.80 --> 1103.08]  Right.
[1103.86 --> 1105.42]  Like you can think of.
[1105.62 --> 1107.36]  Yeah, you can think of who this is.
[1107.36 --> 1113.90]  And I guess one way to put this is it's not totally open source, quote unquote.
[1114.34 --> 1120.02]  Like we wouldn't call this maybe open source in the kind of official definition of open
[1120.02 --> 1120.38]  source.
[1120.74 --> 1120.92]  Yes.
[1120.94 --> 1127.18]  But it's certainly commercially available to a very wide set of people.
[1127.64 --> 1127.78]  Yep.
[1127.78 --> 1132.42]  You know, one of the first things I noticed when this came out on their page and they're
[1132.42 --> 1135.68]  taught, you know, there's there's and I'm diving into like the specifics of the model
[1135.68 --> 1142.10]  here is we had an episode not too long ago and you were describing about kind of the I
[1142.10 --> 1145.80]  believe it was the seven billion limit, you know, in terms of hardware usage and stuff.
[1145.80 --> 1152.04]  And having been taught that by you, I immediately locked in on the smallest being seven billion
[1152.04 --> 1153.32]  there as in.
[1153.42 --> 1158.26]  And I thought, oh, this is what Daniel has taught all of us about that limitation on
[1158.26 --> 1159.96]  accessibility and who can do it.
[1160.02 --> 1163.04]  So, you know, it has the 13 billion and the 70 billion size.
[1163.18 --> 1167.92]  But I definitely picked up on the seven billion, which I'm assuming is going back to what you
[1167.92 --> 1169.98]  were teaching us a few episodes back.
[1169.98 --> 1170.58]  Yeah.
[1170.94 --> 1174.44]  And so just to fill in a little bit on that.
[1174.60 --> 1178.20]  So the Llama 2 release includes three sizes.
[1178.80 --> 1185.20]  So, again, thinking back to what are the kind of characteristics of large language models
[1185.20 --> 1188.16]  that kind of matter as you're considering using them?
[1188.22 --> 1188.98]  One is license.
[1189.08 --> 1191.18]  We've already talked about that a little bit here.
[1191.24 --> 1192.78]  We might revisit it here in a second.
[1192.78 --> 1200.48]  Another is size, because that influences both the hardware that you need to run it and also
[1200.48 --> 1202.36]  its kind of ease of deployment.
[1203.16 --> 1208.56]  So Llama 2 is released in seven billion parameter, 13 billion parameter and 70 billion parameter
[1208.56 --> 1209.10]  sizes.
[1209.74 --> 1216.42]  And then there's also, of course, the training data and that sort of thing that's related to
[1216.42 --> 1220.54]  this and how it's fine tuned or instruction tuned.
[1220.54 --> 1230.32]  So Llama 2 is released in these three sizes, both as a base large language model and a chat
[1230.32 --> 1232.02]  fine tuned model.
[1232.36 --> 1237.34]  So there's the seven billion, 13 and 70 billion Llama 2s.
[1237.34 --> 1244.44]  And then there's the seven, 13 and 70 billion Llama 2 chat models, which we can talk about that
[1244.44 --> 1245.56]  fine tuning here in a second.
[1245.64 --> 1248.32]  But yes, you're right, Chris, in that seven billion.
[1248.32 --> 1256.76]  I could reasonably pull that into a collab notebook and maybe with a few tricks, but with certainly
[1256.76 --> 1263.52]  with the great tooling from Hugging Face, including ways to load it in even four bit or other
[1263.52 --> 1264.28]  quantizations.
[1264.72 --> 1271.02]  I can run that, you know, on a T4, for example, and Google Colab with some of the great tooling
[1271.02 --> 1271.86]  that's out there.
[1271.86 --> 1279.62]  So not needing to have a huge cluster, the 70 billion, even with that, that's kind of another
[1279.62 --> 1285.92]  limit where using some of these tricks, I've definitely seen people running the 70 billion
[1285.92 --> 1293.88]  parameter model on an A100, again, loading in four bit with some of the quantization stuff
[1293.88 --> 1294.26]  and all that.
[1294.34 --> 1296.92]  The 70 billion is certainly going to be more difficult to run.
[1296.92 --> 1303.86]  It might require multiple GPUs, but that's kind of that sizing range for people to have
[1303.86 --> 1307.00]  in mind and how accessible things are.
[1307.68 --> 1308.06]  And yeah.
[1308.38 --> 1312.60]  How might you, I'm just curious, if you're looking at these, you're a business out there
[1312.60 --> 1317.98]  or data scientist, and can you make up a couple of use cases that you might target with each
[1317.98 --> 1323.18]  of these where you might say, oh, I want to go 13 on this, not seven, not 70 for something
[1323.18 --> 1323.66]  like this.
[1323.72 --> 1325.04]  Can you imagine something like this?
[1325.04 --> 1325.86]  I'm putting you on the spot.
[1326.22 --> 1331.42]  Yeah, I think, I mean, there's certainly innumerable use cases, but I think maybe two distinctions
[1331.42 --> 1338.88]  that people could have in their mind is if you want like your own private chat GPT, right?
[1338.90 --> 1342.86]  Or like another way you could think about it is a very general purpose model.
[1342.86 --> 1349.16]  Like you could do anything with this model, like any specific prompt, whatever, you're probably
[1349.16 --> 1354.72]  going to look towards that higher end, the 70 billion parameter model for that kind of
[1354.72 --> 1358.28]  almost chat GPT like performance.
[1358.28 --> 1360.06]  You're going to have to go much higher.
[1360.46 --> 1366.80]  But as we've talked about on the show before, most businesses don't need a general purpose
[1366.80 --> 1367.16]  model.
[1367.30 --> 1369.02]  They need a model to do a thing.
[1369.02 --> 1372.62]  And so or a task or a set of tasks.
[1373.34 --> 1380.34]  And so in that case, I think businesses, because this is open and commercially licensed businesses
[1380.34 --> 1387.02]  that could take those seven and 13 billion parameter models and fine tune them for a task in their
[1387.02 --> 1391.96]  business, which also is increasingly has amazing tooling around it.
[1391.96 --> 1397.74]  Again, from from hugging face and others with the peft library parameter efficient fine tuning
[1397.74 --> 1406.26]  and the Laura technique, which is the low rank adapter technique, which basically only adapts
[1406.26 --> 1407.44]  an existing model.
[1407.56 --> 1412.84]  It's kind of an adapter technique rather than retraining a bunch of the the original model.
[1413.64 --> 1419.06]  This opens up fine tuning possibilities in these smaller models where that fine tune for an
[1419.06 --> 1423.88]  organization is going to perform probably better than any general purpose model out there.
[1424.64 --> 1430.22]  And because it's that smaller size, you can run it on a reasonable set of hardware that's not going
[1430.22 --> 1434.72]  to require you to, you know, buy your own GPU cluster to host the thing.
[1434.82 --> 1435.02]  Right.
[1435.10 --> 1439.36]  So that's kind of a maybe a range of use cases that people could have in mind.
[1439.68 --> 1445.62]  I have one more question for you before we abandon this 7 billion to 70 billion being an order
[1445.62 --> 1447.44]  magnitude jump on that.
[1447.84 --> 1452.50]  Why would you have something fairly close to that at 13 billion parameters?
[1452.66 --> 1456.78]  Like what's the difference in 7 and 13 when the next step is all the way up to 70?
[1457.24 --> 1459.24]  Well, what what's the rationale you think?
[1459.40 --> 1459.58]  Yeah.
[1459.72 --> 1466.52]  So it is interesting, actually, if I'm understanding right from some of the sources that I've that
[1466.52 --> 1471.90]  I've been reading, there was actually a I forget if it was 30 or 34 billion parameter
[1471.90 --> 1477.32]  model that they were also had in pre-release and were tuning.
[1477.54 --> 1482.80]  So there was another one that kind of fit in that slot that is kind of missing that gap
[1482.80 --> 1483.70]  like you're talking about.
[1483.70 --> 1490.00]  Like if you think of MPT, MPT has a 30 billion parameter model that fits in that kind of gap.
[1490.62 --> 1496.92]  My understanding and, you know, if our listeners can correct me if I'm wrong, please do.
[1496.92 --> 1502.34]  But my understanding is that they actually did test that size of model and found it to
[1502.34 --> 1510.34]  not pass their kind of safety parameters around harmful, potentially harmful output or not truthful
[1510.34 --> 1511.70]  output, that sort of thing.
[1511.78 --> 1513.86]  So they decided actually to hold that back.
[1514.00 --> 1521.88]  So it could be possible as they instruction tune and get human feedback, potentially more
[1521.88 --> 1524.64]  iterations of reinforcement learning from human feedback.
[1524.64 --> 1528.64]  There may be a model that they released in that parameter range.
[1528.82 --> 1532.04]  So that was one thing that that happened.
[1532.14 --> 1538.04]  I think it is interesting, you know, several different things here that are unique about
[1538.04 --> 1545.62]  this model specifically or maybe the release as well, other than the license is they were
[1545.62 --> 1550.74]  fairly vague on the data that went into the pre-training.
[1550.74 --> 1556.80]  So they talked specifically about some very intense data cleaning and filtering that they
[1556.80 --> 1558.24]  did on public data sets.
[1558.90 --> 1566.10]  And it was trained on more data than the original LAMA, but they're fairly vague on the mix of
[1566.10 --> 1568.24]  that data and all of that.
[1568.40 --> 1574.08]  So that may be related to feedback they got on the data sets that were used in the first
[1574.08 --> 1574.40]  LAMA.
[1574.40 --> 1581.86]  I don't know, but the technical paper was mostly related to the modeling and fine tuning trickery
[1581.86 --> 1585.88]  and methodologies that they used, which was interesting.
[1586.62 --> 1593.56]  And one of those interesting elements of the way that they fine tune this model was, I think,
[1593.62 --> 1595.08]  the reward modeling.
[1595.08 --> 1601.54]  So if you remember, like the GPT family of models, the MPT Falcon, these different models,
[1602.36 --> 1607.98]  one of the things that is often done with these models is this process of reinforcement learning
[1607.98 --> 1612.38]  through human feedback, which is this process.
[1612.38 --> 1616.76]  And we covered this on a previous episode, which we can link in the show notes, but actually
[1616.76 --> 1623.38]  using human preferences to score the output of a model and then actually use reinforcement
[1623.38 --> 1628.82]  learning to correct the model to better align with human preferences or human feedback.
[1629.14 --> 1635.34]  They actually use two separate reward models in this fine tuning of the chat based model,
[1635.52 --> 1641.34]  one that was related to helpfulness and then the other one, which was related to safety.
[1641.72 --> 1648.10]  And one of the interesting things that they talked about in the paper was how sometimes those
[1648.10 --> 1650.76]  things can kind of work against each other.
[1650.76 --> 1653.48]  If you're trying to do both of them at the same time.
[1653.48 --> 1659.14]  So they actually separated out the reward models that they used for the chat fine tuning
[1659.14 --> 1664.82]  into these two reward models, one for helpfulness and one for safety, which is quite interesting,
[1664.82 --> 1665.26]  I think.
[1680.76 --> 1686.42]  So Chris, maybe just a couple other things related to Llama.
[1686.74 --> 1691.58]  And then I want to see your feedback on Code Interpreter as well, because we haven't talked
[1691.58 --> 1692.82]  about that yet on the show.
[1692.96 --> 1695.26]  And maybe Claude 2 if we can get to it.
[1695.48 --> 1698.30]  Yeah, we got to mention Claude 2 as well, because they were both big releases.
[1698.82 --> 1699.02]  Yeah.
[1699.02 --> 1703.98]  So just one maybe other note, which I find quite interesting.
[1703.98 --> 1710.40]  And actually, I love our previous guest Damian's thoughts on this, who was in our last episode
[1710.40 --> 1713.18]  about the legal implications of generative AI.
[1713.18 --> 1719.30]  But one of the interesting things about the Llama license, in addition to it allowing this commercial
[1719.30 --> 1727.88]  usage, is that there is technically a restriction in the Llama license that says you will not
[1727.88 --> 1733.84]  use Llama materials, which includes the model weights and et cetera, or any output or results
[1733.84 --> 1741.30]  of the Llama materials to improve any other large language model, excluding Llama 2 or derivative
[1741.30 --> 1742.04]  works thereof.
[1742.04 --> 1748.50]  So essentially what this means is if you're using Llama 2 and you want to fine tune a model
[1748.50 --> 1755.62]  or you're fine tuning a model off of Llama 2 outputs, you're stuck with Llama 2.
[1755.86 --> 1759.26]  Basically, Llama 2 is your model and that you're going to stick with Llama 2.
[1759.74 --> 1768.44]  So you couldn't, for example, technically take the outputs from Llama 2 and fine tune, say,
[1768.66 --> 1770.72]  Dolly 3 billion, right?
[1770.72 --> 1773.28]  That would not be allowed by the license.
[1773.46 --> 1775.98]  And of course, that's something that people are doing all over the place.
[1776.06 --> 1784.50]  They're taking outputs from GPT-4 and fine tuning a different model or taking outputs from a large
[1784.50 --> 1792.96]  model like, you know, maybe Llama 2 70 billion now and fine tuning another model that's smaller
[1792.96 --> 1796.38]  based on a certain type of prompt or something.
[1796.38 --> 1803.40]  So this is restricting that family of models that you're allowed to do that sort of thing
[1803.40 --> 1805.54]  with, which is the first time I've seen that.
[1805.62 --> 1806.74]  I think it's kind of interesting.
[1806.74 --> 1812.44]  Yes, it strikes me as another Mark Zuckerberg anti-competitiveness, you know, thing, which
[1812.44 --> 1813.82]  he's fairly famous for.
[1813.92 --> 1815.66]  I mean, that's kind of even before this.
[1815.80 --> 1815.92]  Yeah.
[1816.00 --> 1818.18]  And how could you enforce such a thing?
[1818.84 --> 1819.14]  Yeah.
[1819.62 --> 1824.84]  That was my next question to you is, is there any possible way that you could conceive of
[1824.84 --> 1828.20]  to actually know that from an enforceability standpoint?
[1828.54 --> 1829.30]  I have no idea.
[1829.68 --> 1830.34]  I don't either.
[1830.34 --> 1835.58]  So it seems it's like it's a license thing and it will concern the lawyers, but it's hard
[1835.58 --> 1836.12]  to imagine.
[1836.48 --> 1841.74]  I mean, going back to our conversation last week, once you have output and that output
[1841.74 --> 1847.04]  is input to more output and, you know, there's a point where it becomes very, very, very difficult
[1847.04 --> 1849.42]  to know what the sourcing really was.
[1850.34 --> 1855.58]  So and the fine tunes are already appearing off of Llama 2.
[1855.58 --> 1862.74]  So the most notable probably is Free Willy, which is from Stability AI and is a fine tune
[1862.74 --> 1864.84]  of the largest 70 billion model.
[1865.08 --> 1867.78]  But there's other ones coming out as well.
[1868.12 --> 1875.80]  And so I think we're about to see just a huge explosion of these Llama 2 based models for
[1875.80 --> 1877.02]  a whole variety of purposes.
[1877.30 --> 1883.60]  And who knows how they will fit into that licensing restriction or how open people will be about
[1883.60 --> 1883.98]  that.
[1883.98 --> 1886.20]  But it's about to start.
[1886.32 --> 1887.64]  The fine tunes are already coming.
[1888.16 --> 1888.18]  Yeah.
[1888.28 --> 1892.68]  Well, you know, to your point earlier, they weren't terribly clear about the data that
[1892.68 --> 1894.44]  they were sourcing from their own standpoint.
[1895.00 --> 1895.16]  Yeah.
[1895.22 --> 1897.88]  And I find it interesting, a little ironic.
[1898.14 --> 1900.04]  A bit of a double standard, maybe.
[1900.42 --> 1900.68]  Yeah.
[1900.68 --> 1903.72]  A little bit of a double standard right there in terms of like, we're not going to tell you
[1903.72 --> 1905.10]  everything about how we're doing input.
[1905.20 --> 1907.76]  But by the way, you better not use our output for your, you know, for something.
[1908.02 --> 1908.04]  Yeah.
[1908.10 --> 1910.16]  So, yeah, a little interesting.
[1910.16 --> 1915.94]  Do you think there's any risk of a walled garden kind of concept happening in large language
[1915.94 --> 1921.12]  models if others were to follow this lead on anti-competitiveness?
[1921.76 --> 1923.56]  Yeah, it will be interesting.
[1923.86 --> 1929.84]  I think it is a notable trend that the first Llama from Meta was not open for commercial
[1929.84 --> 1930.24]  at all.
[1930.30 --> 1932.32]  And now they're opening it up for commercial purposes.
[1932.32 --> 1937.88]  And, you know, maybe there's a separate trend that will happen with some of these use based
[1937.88 --> 1943.54]  restrictions that people are importing into their licenses and how useful those things
[1943.54 --> 1947.72]  are over time that will may shift and we'll see those things die off.
[1947.76 --> 1952.16]  Or maybe if they're enforced and there's precedent, maybe we'll see something go the other way.
[1952.20 --> 1952.76]  I'm not sure.
[1953.26 --> 1960.16]  But speaking of models that you might get their output and use it to train other models,
[1960.16 --> 1967.88]  that is these large scale proprietary closed models from people like OpenAI and Anthropic
[1967.88 --> 1968.40]  and others.
[1968.56 --> 1973.18]  We've got a couple of things that we haven't talked about on the show yet, which people
[1973.18 --> 1975.10]  should probably have on their radar.
[1976.86 --> 1979.20]  One of those is Claude2.
[1979.94 --> 1982.98]  What do you think about Claude2 from Anthropic?
[1983.42 --> 1986.38]  Yeah, I've been playing around with it a lot in the last week.
[1986.38 --> 1991.14]  Uh, and I kind of have a set of things that I try over and over again.
[1991.20 --> 1993.46]  They're kind of my standard tasks as new models come out.
[1993.96 --> 1997.40]  And some of them are coding and some of them are content generation, which are kind of the
[1997.40 --> 1999.32]  two big things that I use most often.
[1999.48 --> 2000.26]  It was interesting.
[2000.34 --> 2005.62]  You can put, you know, the input size for Claude2 is much larger than the others.
[2005.92 --> 2007.14]  Like much, much larger.
[2007.36 --> 2008.50]  Much, much, much larger.
[2008.62 --> 2010.32]  So a hundred thousand tokens.
[2010.32 --> 2010.80]  Yeah.
[2010.80 --> 2010.92]  Yeah.
[2011.08 --> 2016.22]  And so it's had me kind of change the way I'm approaching it in that by contrast with
[2016.22 --> 2021.16]  like chat GPT and you're trying to figure out with, with the limits that you have both on
[2021.16 --> 2025.70]  input and output, how do you kind of prompt engineer your way to get, you know, where
[2025.70 --> 2029.64]  you're trying to go, which has become this whole skill set we've been talking about, you
[2029.64 --> 2030.60]  know, in recent months.
[2030.60 --> 2035.20]  And yet Claude2 almost kind of wipes that out a little bit in some ways, not, not in
[2035.20 --> 2039.72]  always in that you can hit it with a much larger input space.
[2039.76 --> 2044.42]  And, and so it's changing how I'm thinking about kind of getting to the output that I
[2044.42 --> 2044.76]  want.
[2044.90 --> 2046.82]  And the output is a bit different.
[2046.86 --> 2047.80]  It's not the same.
[2047.86 --> 2050.66]  I'm getting out different outputs from, from all the models.
[2050.88 --> 2052.42]  So yeah, they're not all the same.
[2052.50 --> 2052.86]  Definitely.
[2053.18 --> 2057.18]  I think my biggest thing is with all these new releases, I'm trying to figure out how do
[2057.18 --> 2058.04]  I use each one?
[2058.04 --> 2063.06]  When do I, I'm trying to develop my own strategy on when do I go to chat GPT by default?
[2063.22 --> 2064.44]  Like when's that the right thing?
[2064.62 --> 2068.14]  And that's changing as we'll talk about with things like plugins and stuff that's evolving.
[2068.42 --> 2072.28]  But then Claude2 comes out and then you have, you know, on the open source side, as we just
[2072.28 --> 2073.18]  talked about with Llama2.
[2073.74 --> 2079.52]  So I think trying to understand all the tools in the toolbox in relation to each other has
[2079.52 --> 2080.02]  been interesting.
[2080.14 --> 2086.02]  So Claude2, I'm, I'm really focused right now, primarily on, on large content output is kind
[2086.02 --> 2086.94]  of where I've landed on that.
[2086.94 --> 2094.36]  And the hundred K context length of Claude2 is something I find really compelling as well.
[2094.56 --> 2101.22]  There was also a significant paper that came out that caused a lot of waves in terms of
[2101.22 --> 2107.18]  context length and thinking about that, which showed kind of as you increase context length,
[2107.24 --> 2111.22]  you lose any significance of the middle bit of that context.
[2111.22 --> 2117.98]  So the beginning and end is more important in terms of what makes the output of the, of
[2117.98 --> 2122.06]  the model quality or not in terms of how you would measure that.
[2122.74 --> 2126.00]  And so we'll link to that paper maybe in the show notes as well.
[2126.16 --> 2128.20]  But I've tried some things.
[2128.34 --> 2131.12]  I mean, I don't know exactly all of the details.
[2131.12 --> 2134.16]  Again, Claude is one of these closed models.
[2134.58 --> 2136.94]  So I don't know all of the details of how they're doing things.
[2137.08 --> 2141.48]  And because it's sitting behind an API, it's hard to know how those things evolve over time.
[2142.22 --> 2147.08]  But for example, I, I took one of the things with Claude2 is I just took one of our complete
[2147.08 --> 2148.88]  podcast transcripts.
[2148.88 --> 2152.30]  So a full episode, so 45 minutes of audio transcript.
[2152.68 --> 2158.96]  I took episode 225, which I really enjoyed talking a lot about the things that I'm working
[2158.96 --> 2164.50]  on right now with prediction guard and just asked it to give me a summary of the main takeaways
[2164.50 --> 2167.44]  and, you know, paste it in the whole thing.
[2167.80 --> 2171.34]  And it's like a fairly good comprehensive takeaways.
[2171.34 --> 2175.76]  Like many companies ban usage of certain LLMs, blah, blah, blah.
[2175.76 --> 2181.42]  You know, prediction guard is trying to provide easy access, structuring validation, compliance
[2181.42 --> 2186.40]  features for LLMs, making LLM usage easier, blah, blah, blah.
[2186.48 --> 2187.72]  And it gives these great takeaways.
[2188.48 --> 2195.84]  And then I asked, you know, hey, suggest a few future episodes that we could do that maybe
[2195.84 --> 2200.02]  cover related topics, but things that weren't covered in this episode.
[2200.40 --> 2201.24]  Pretty good.
[2201.36 --> 2204.46]  Some of them are kind of generic, right?
[2204.46 --> 2207.64]  A look at current state of AI agents and automation.
[2207.90 --> 2211.38]  How close are we to no code AI app generation, blah, blah, blah.
[2211.86 --> 2218.18]  So that all kind of off of this large context of the transcript input was quite interesting.
[2218.68 --> 2219.20]  I'm curious.
[2219.42 --> 2221.40]  I'm going to put you on the spot also.
[2221.66 --> 2226.16]  As someone who's working on your own product, and I know this is not a prediction guard episode,
[2226.34 --> 2230.64]  but I'm asking on my own behalf and on behalf of the listener, how do you, as someone who
[2230.64 --> 2234.02]  is looking at these different models, how do you think of those different models?
[2234.54 --> 2237.58]  How do you kind of structure them in your mind in terms of what you're offering?
[2238.06 --> 2241.70]  You've been evolving rapidly over the last few months, and I'm always curious to see kind
[2241.70 --> 2243.56]  of where your head's at on this now as you're looking at them.
[2243.56 --> 2250.48]  Yeah, I think the things consistently that I'm seeing are that I made a post on LinkedIn about
[2250.48 --> 2251.28]  this as well.
[2251.68 --> 2258.22]  Even my own applications that I'm building, LLM-based applications, having access to multiple
[2258.22 --> 2266.88]  models rather than a single model, I think is a really nice usage pattern where if the easier
[2266.88 --> 2267.74]  we can make it.
[2267.74 --> 2272.70]  And there's other people that are doing this as well, other, you know, in prediction guard,
[2272.78 --> 2276.86]  you can query a whole bunch of models at the same time concurrently.
[2277.06 --> 2280.68]  There's other systems that will let you look at that output as well.
[2281.12 --> 2287.60]  So nat.dev and some of the toolbar stuff that Swix is doing.
[2287.88 --> 2290.86]  We had a collaboration with him in the Latent Space podcast.
[2291.20 --> 2296.96]  So the more you can tie these things together and look at the output or automatically analyze
[2296.96 --> 2299.36]  the output of multiple models at the same time.
[2299.36 --> 2305.22]  I think that's really useful because it's hard to generally evaluate these models until
[2305.22 --> 2309.72]  you start evaluating them for your use case and building intuition about them for your
[2309.72 --> 2310.50]  own use case.
[2310.98 --> 2316.50]  So I think the pitfall that people maybe fall into is saying, oh, I'm going to use this
[2316.50 --> 2319.58]  model before they've even tested that for their use case.
[2319.78 --> 2319.92]  Right.
[2320.50 --> 2326.14]  Try creating a set of evaluation examples for your own use case and then try out a bunch of
[2326.14 --> 2332.40]  different models for that and also try out the things that are becoming more standard
[2332.40 --> 2338.28]  kind of operating procedures for building LLM applications, like looking at the consistency
[2338.28 --> 2346.86]  of outputs, running a post generation validity or factuality check on the output.
[2347.06 --> 2352.52]  So checking a language model with a language model, doing input filtering and all these sorts
[2352.52 --> 2354.48]  of more engineering related things.
[2354.68 --> 2356.76]  So those are some of the things that I'm seeing.
[2356.92 --> 2363.12]  But having access to a bunch of models at the same time, I think, is something that can
[2363.12 --> 2364.74]  really boost your productivity.
[2365.48 --> 2366.14]  I appreciate that.
[2366.64 --> 2370.66]  And to our listeners, we're not making it a prediction guard show or episode.
[2370.90 --> 2376.28]  But as a co-host, Daniel's excursion through this and his professional has made him, in my
[2376.28 --> 2381.10]  view, one of the world's true experts in how to look at all these together.
[2381.64 --> 2386.50]  And since we have the benefit of him co-hosting the podcast, I'm going to continue to take
[2386.50 --> 2388.88]  advantage of that expertise for all of us.
[2388.98 --> 2389.36]  Thanks, Chris.
[2389.46 --> 2390.58]  Sorry about that, Daniel.
[2391.10 --> 2392.32]  Sorry for putting you on the spot.
[2392.44 --> 2392.54]  Yeah.
[2392.68 --> 2393.48]  No, no worries.
[2394.08 --> 2400.10]  I think the other thing maybe to highlight with Claude 2 and something that you were talking
[2400.10 --> 2407.10]  about in chat before we jumped into this episode was Claude 2 versus or maybe Anthropic and
[2407.10 --> 2408.64]  their offerings versus OpenAI.
[2408.90 --> 2410.00]  How do we understand that?
[2410.08 --> 2411.90]  Like, how do we categorize these things?
[2412.46 --> 2417.82]  I think one of the interesting things with Claude 2, so we've seen both Anthropic and their
[2417.82 --> 2423.66]  Claude models and OpenAI and their GPT models increase context size over time.
[2424.26 --> 2428.12]  GPT models, not quite as far as Claude, but both have increased.
[2428.12 --> 2434.68]  They've also both added in some of this functionality, which I think is very interesting.
[2435.44 --> 2440.52]  Claude 2, I think, first, if I'm not wrong, the ability to add in your own data.
[2440.86 --> 2447.66]  So in Claude 2, there's a little attachment button and you can upload PDFs or text files or CSVs
[2447.66 --> 2453.72]  and have that inserted into the context of your prompt, which I think is, of course, extremely
[2453.72 --> 2454.22]  powerful.
[2454.22 --> 2459.72]  We've talked about adding in external data into generative models and grounding models
[2459.72 --> 2460.32]  in the past.
[2460.38 --> 2461.14]  It's very powerful.
[2461.84 --> 2465.60]  Now, OpenAI is doing this in a slightly different way.
[2465.70 --> 2470.78]  And I think there's something worth calling out on the podcast is with their new code interpreter
[2470.78 --> 2474.44]  beta feature within ChatGPT.
[2474.44 --> 2482.64]  You can upload data, but it's processed through the code interpreter in a different way than
[2482.64 --> 2483.76]  what Claude is doing.
[2483.90 --> 2489.44]  So we all know that ChatGPT and GPT models can generate really good code and specifically
[2489.44 --> 2490.72]  good Python code.
[2491.18 --> 2500.00]  And so what OpenAI has done for their kind of data processing agent within ChatGPT is said,
[2500.00 --> 2504.32]  well, let's just have our model generate Python code.
[2504.46 --> 2510.98]  Then we'll hook up the ChatGPT interface to a Python interpreter and just go ahead and execute
[2510.98 --> 2514.76]  that code for you over your data and then give you the output.
[2515.06 --> 2518.10]  So this is maybe a distinction that people can have in their mind.
[2518.24 --> 2521.24]  Claude 2, you can upload this huge amount of context.
[2521.42 --> 2523.90]  You can upload files, insert it into the prompt.
[2523.90 --> 2530.34]  As far as I know, they're not running any kind of code interpreter type thing under the hood.
[2531.54 --> 2536.10]  ChatGPT might not be inserting all of that into the prompt, but they're actually saying,
[2536.28 --> 2541.90]  well, what if we decompose what you're wanting me to do with this external data into something
[2541.90 --> 2550.58]  that can be executed by a sort of agent type of workflow where you upload your data and
[2550.58 --> 2552.98]  ask me to like do some analysis over it.
[2552.98 --> 2554.84]  I'm going to generate some code.
[2555.44 --> 2560.72]  So the language model generates some code and then that code is actually executed in the background.
[2561.00 --> 2566.22]  It returns a result, which is then fed back through a model to give you generated output
[2566.22 --> 2568.28]  back in the interface.
[2568.28 --> 2573.00]  So it's actually a multi-stage thing happening in code interpreter in OpenAI.
[2573.54 --> 2578.72]  It effectively produces a no-code solution, you know, where you get an output and you're just
[2578.72 --> 2582.96]  kind of skipping the whole thing, you know, instead of using the language model,
[2582.98 --> 2585.94]  to generate your own code and to be your code assist and all that.
[2586.04 --> 2587.18]  And then you're still doing it.
[2587.40 --> 2589.80]  It's kind of skipping that whole step right there.
[2590.16 --> 2590.24]  Yeah.
[2590.32 --> 2594.16]  And I can give an example I actually ran prior to the show.
[2594.16 --> 2599.64]  So I have Claude and the OpenAI code interpreter side by side open.
[2599.84 --> 2607.62]  I uploaded a file with a bunch of Yoruba, which is a language in Africa, transcriptions out
[2607.62 --> 2613.26]  of audio, which are from the Bible TTS project that we worked with Koki and Masakane on.
[2613.26 --> 2619.38]  And so I uploaded this file, which includes this Yoruba text in a CSV format.
[2619.82 --> 2622.06]  OpenAI said, great, you've uploaded this file.
[2622.32 --> 2625.40]  Let's start by loading and examining the context.
[2625.64 --> 2628.64]  And then it has this sort of show work button.
[2628.64 --> 2635.96]  And you can see the actual code that it generated, which is Panda's code to import the CSV and then
[2635.96 --> 2637.62]  output some examples.
[2637.62 --> 2642.58]  And so you can expand that and actually see the code that it ran under the hood and the
[2642.58 --> 2644.96]  conclusions that the agent came to.
[2645.30 --> 2648.84]  Then I asked it, OK, well, plot the distribution of the transcript links.
[2648.86 --> 2649.88]  Are there any anomalies?
[2650.28 --> 2653.34]  And then again, it says, hey, show work.
[2653.46 --> 2656.56]  And you can see it's importing matplotlib.
[2657.14 --> 2658.72]  It's taking in the CSV.
[2658.92 --> 2664.46]  It's actually creating the plot and actually generates an image out of the transcripts.
[2664.46 --> 2666.24]  It says, I didn't find any anomalies.
[2666.24 --> 2668.82]  They're all kind of within the same distribution.
[2669.06 --> 2670.26]  There's not any anomalies.
[2670.48 --> 2673.44]  Then I asked it, can you translate all the Yoruba to English?
[2673.48 --> 2679.04]  And that's where it ended up stopping because it said, no, I'm not good at doing that.
[2679.68 --> 2683.56]  And Quad actually stopped there as well and said, no, I'm not going to do that.
[2684.16 --> 2686.94]  I also uploaded the Yoruba alignments to Quad.
[2687.40 --> 2690.78]  And it said, hey, sure, let me analyze these transcripts.
[2690.78 --> 2696.28]  And it just output some general, like there are 50 audio links, the transcript links.
[2696.28 --> 2697.88]  There's no Python code there.
[2697.98 --> 2699.98]  It just gave me some takeaways.
[2700.46 --> 2700.58]  Right.
[2700.62 --> 2702.72]  And then I said, are there any anomalies?
[2702.76 --> 2705.38]  And it said, I checked and I can't find any.
[2705.56 --> 2707.30]  And could you translate it?
[2707.34 --> 2708.60]  And it said, unfortunately, I can't.
[2708.60 --> 2710.52]  So it's all still a chat based thing.
[2710.52 --> 2716.66]  So you can see kind of different approaches to this complicated workflow of having almost
[2716.66 --> 2722.78]  an assistant agent executing code for you versus putting more context in the language
[2722.78 --> 2725.34]  model and having it reason over that context.
[2725.74 --> 2731.06]  So they're almost getting their own strengths at different types of approaches to problems.
[2731.06 --> 2731.92]  Would that be fair?
[2732.24 --> 2732.40]  Yeah.
[2732.40 --> 2737.32]  So that's another way of thinking about it is as you start understanding how the different
[2737.32 --> 2743.40]  large language models approach a problem and the tooling that might be better or worse for
[2743.40 --> 2747.58]  a given use case, that also will help you kind of pick which way you want to go in addition
[2747.58 --> 2750.28]  to maybe just using multiple models, as you talked about earlier.
[2750.68 --> 2751.20]  Yeah, exactly.
[2751.42 --> 2756.78]  And there's so much to dive into on all these topics that we've covered today.
[2757.14 --> 2761.44]  I'm going to make sure that we include some really good learning resources for people in
[2761.44 --> 2762.06]  the show notes.
[2762.20 --> 2764.00]  So make sure and click on some of those.
[2764.00 --> 2770.64]  There's a guide from Datagen on the neural radiance field stuff, the NERF stuff that you
[2770.64 --> 2772.00]  can learn a bit more about that.
[2772.52 --> 2778.78]  There's a hugging face post and a Phil Schmidt post on Llama 2 that are both really practical,
[2779.00 --> 2780.20]  kind of how do you run it?
[2780.50 --> 2781.66]  How do you fine tune it?
[2781.88 --> 2782.74]  What does it mean?
[2782.74 --> 2791.50]  And then there's a nice post from the one useful thing, Ethan Mollick blog or newsletter
[2791.50 --> 2795.24]  about Code Interpreter and how to get it set up and some things to try.
[2795.44 --> 2797.26]  So we'll link that in our show notes.
[2797.36 --> 2800.40]  And I think people should dig in, get hands on with this stuff.
[2800.60 --> 2802.40]  Things are updating quickly.
[2802.66 --> 2807.80]  And the only way to really get that intuition about things is to dive in and get hands on.
[2807.80 --> 2808.54]  It is.
[2808.60 --> 2813.80]  It's the most interesting moment we've had in the AI revolution of recent years and just
[2813.80 --> 2815.62]  so much cool stuff right now.
[2816.16 --> 2821.24]  Anyway, thank you for taking us through all the understanding and explanation of these
[2821.24 --> 2821.50]  things.
[2821.96 --> 2822.76]  Yeah, definitely.
[2823.10 --> 2824.62]  It's a good time.
[2824.88 --> 2830.20]  Hopefully people enjoy the rest of their week and maybe go see Oppenheimer or Barbie, depending
[2830.20 --> 2833.56]  on which of those is most interesting to you.
[2833.70 --> 2835.50]  But we'll see you next time, Chris.
[2835.70 --> 2836.26]  See you later.
[2836.26 --> 2836.66]  Thanks.
[2837.80 --> 2842.50]  Thank you for listening to Practical AI.
[2843.00 --> 2846.82]  Your next step is to subscribe now, if you haven't already.
[2847.36 --> 2851.94]  And if you're a longtime listener of the show, help us reach more people by sharing Practical
[2851.94 --> 2853.30]  AI with your friends and colleagues.
[2853.86 --> 2858.68]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Dog podcasts.
[2859.26 --> 2863.04]  Check out what they're up to at Fastly.com and Fly.io.
[2863.04 --> 2867.80]  And to our Beat Freak in residence, Breakmaster Cylinder for continuously cranking out the
[2867.80 --> 2868.78]  best beats in the biz.
[2869.04 --> 2869.96]  That's all for now.
[2870.24 --> 2871.38]  We'll talk to you again next time.
[2871.38 --> 2871.56]  Game Bol Rey.
[2871.56 --> 2877.34]  And to our meeting, everybody.
[2893.66 --> 2893.80]  который lacks podcasts...
