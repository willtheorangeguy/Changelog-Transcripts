[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.84 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[25.82 --> 28.32]  Thanks to our partners at Fly.io.
[28.70 --> 31.08]  Launch your AI apps in five minutes or less.
[31.40 --> 33.32]  Learn how at Fly.io.
[37.84 --> 43.40]  Well, friends, I'm here with a friend of mine, Michael Greenwich, co-founder and CEO of WorkOS.
[43.98 --> 45.90]  We're big fans of WorkOS here.
[46.02 --> 47.58]  Michael, tell me about AuthKit.
[48.06 --> 48.80]  What is this?
[48.96 --> 49.60]  How's it work?
[49.84 --> 50.52]  Why'd you make it?
[50.80 --> 54.68]  WorkOS has been building stuff in authentication for a long time, since the very beginning.
[54.68 --> 59.72]  But we really focused initially on just enterprise auth, single sign-on, SAML authentication.
[60.10 --> 63.82]  But a year or two into that, we heard from more people that they wanted all the auth stuff
[63.82 --> 64.18]  covered.
[64.48 --> 69.62]  Two-factor auth, password auth, you know, with blocking passwords that have been reused.
[69.74 --> 72.36]  They wanted auth with, you know, other third-party systems.
[72.80 --> 77.02]  And they wanted really WorkOS to handle all the business logic around tying together identities,
[77.62 --> 82.24]  provisioning users, and even more advanced things like role-based access control and permissions.
[82.24 --> 85.68]  So we started thinking about that more, how we could offer it as an API.
[86.26 --> 93.02]  And then we realized we had this amazing experience with Radix, with this API, really the component
[93.02 --> 96.14]  system for building front-end experiences for developers.
[96.66 --> 100.52]  Radix is downloaded tens of millions of times every month for doing exactly this.
[100.76 --> 103.14]  So we glued those two things together and we built AuthKit.
[103.40 --> 106.98]  So AuthKit is the easiest way to add auth to any app, not just Next.js.
[106.98 --> 111.78]  If you're building a Rails app or a Django app or a just straight up Express app or something,
[112.10 --> 113.90]  it comes with a hosted login box.
[114.10 --> 116.34]  So you can customize that, you can style it.
[116.54 --> 118.12]  You can build your own login experience too.
[118.20 --> 119.20]  It's extremely modular.
[119.42 --> 121.94]  You can just use the backend APIs in a headless fashion.
[122.16 --> 125.62]  But out of the box, it gives you everything you need to be able to serve customers.
[125.84 --> 127.66]  And it's tied into the WorkOS platform.
[127.66 --> 130.96]  So you can really, really quickly add any enterprise features you need.
[131.24 --> 134.28]  So we have a lot of companies that start using it because they anticipate they're going to
[134.28 --> 136.16]  grow up market and want to serve enterprise.
[136.62 --> 140.30]  And they don't want to have to re-architect their auth stack when they do that.
[140.54 --> 144.78]  So it's kind of a way to like future-proof your auth system for your future growth.
[144.94 --> 146.06]  And we have people that have done that.
[146.24 --> 148.36]  People that started off and they're like, oh, I'm just kicking the tires.
[148.40 --> 149.08]  I'm just doing this.
[149.14 --> 152.04]  And then poof, their app gets a bunch of traction, starts growing.
[152.14 --> 152.56]  It's awesome.
[153.28 --> 158.50]  And they go close Coinbase or Disney or United Airlines or, you know, it's like a major customer.
[158.78 --> 162.66]  And instead of saying, oh no, sorry, we don't have any of these enterprise things
[162.66 --> 164.04]  and we're going to have to rebuild everything.
[164.44 --> 167.26]  Just go into the WorkOS dashboard and check a box and you're done.
[167.78 --> 169.98]  Aside from the fact that AuthKit is just awesome.
[170.28 --> 175.62]  The real awesome thing is that it is free for up to 1 million users.
[176.40 --> 181.52]  Yes, 1 million monthly active users are included in this out of the gate.
[181.74 --> 183.38]  So use it from day one.
[183.38 --> 186.92]  And when you need to scale to enterprise, you're already ready.
[187.02 --> 187.64]  Too easy.
[188.00 --> 192.54]  You can learn more at authkit.com or of course, workos.com.
[192.66 --> 193.50]  Big fans.
[193.74 --> 194.30]  Check it out.
[194.68 --> 196.42]  1 million users for free.
[196.72 --> 196.98]  Wow.
[197.32 --> 200.78]  WorkOS.com or authkit.com.
[200.78 --> 222.44]  Welcome to another fully connected episode of the Practical AI podcast.
[222.44 --> 230.42]  In these episodes, Chris and I try to keep you fully connected with everything that's happening in the AI space
[230.42 --> 235.82]  and hopefully share some things that will help you level up your machine learning game.
[236.38 --> 237.34]  I'm Daniel Whitenack.
[237.42 --> 244.44]  I'm CEO at Prediction Guard, where we're deploying a platform for private and secure AI
[244.44 --> 252.32]  and joined as always by my co-host, Chris Benson, who is a Principal AI Research Engineer at Lockheed Martin.
[252.62 --> 253.32]  How are you doing, Chris?
[253.70 --> 254.72]  Doing very well, Daniel.
[254.90 --> 257.10]  I'm podcasting from outside today.
[257.30 --> 257.92]  That's exciting.
[258.22 --> 262.96]  It's a cool November night, but since I just moved house and I don't have a place to sit,
[263.46 --> 267.24]  nothing but boxes here, we're talking about AI outside today.
[267.38 --> 268.66]  This is an outside AI day.
[268.66 --> 275.18]  Yeah, yeah, you live in a place where it's possible to be outside reasonably comfortable in November.
[275.64 --> 276.00]  That's right.
[276.34 --> 277.46]  Right before Thanksgiving.
[278.28 --> 282.62]  Yeah, it's a bit colder up here in the Midwest.
[283.10 --> 291.28]  We're definitely getting to that Midwestern time when the Carhartt jackets come out and the beanies.
[291.52 --> 294.06]  And yeah, it's a good time of year.
[294.54 --> 296.58]  It means Thanksgiving is upon us.
[296.72 --> 297.26]  That's right.
[297.26 --> 299.70]  We got Tofu Turkey coming up here.
[300.00 --> 301.60]  Tofurkey is imminent.
[302.10 --> 303.30]  Yeah, forthcoming.
[303.70 --> 304.88]  So exciting.
[305.14 --> 307.32]  There's better ones than other ones.
[307.54 --> 314.26]  So this isn't a podcast about Tofu Turkey or Tofurkey, but there's some that are better than others.
[314.26 --> 319.64]  And we'll maybe let people hop on their own minds if they're exploring that territory.
[320.20 --> 322.94]  We need some AI-generated Tofurkeys coming at us.
[323.46 --> 325.32]  There's got to be some intersection.
[325.52 --> 325.92]  That's right.
[325.92 --> 326.16]  There's a lot of people that are there.
[326.68 --> 331.76]  Maybe Tofurkey is using AI to generate ad copy this year.
[331.96 --> 341.14]  Which reminds me, I don't know if you've been seeing all the things in the news, Chris, about Coca-Cola's ads, AI-generated ads.
[341.40 --> 343.02]  Have you been seeing any of that?
[343.08 --> 344.40]  Have you seen the actual ads?
[344.40 --> 348.22]  I have not seen the actual ads, but I have seen some of the news talking about it.
[348.22 --> 349.38]  Yeah, yeah.
[349.50 --> 365.16]  So for those that aren't aware, Coca-Cola, you know, every year Coca-Cola kind of creates these iconic Christmas time ads with the Coca-Cola truck and, you know, the polar bear and things like that.
[365.16 --> 370.30]  And this year, at least, I don't know if it's all the ads, but there's at least one ad.
[370.38 --> 382.40]  I haven't been following the exact details, but there's at least one ad that is fully AI-generated or at least driven by AI-generated video clips or images, that sort of thing.
[382.40 --> 385.72]  And I've seen it on the streaming services.
[386.00 --> 394.34]  So on, you know, I forget which ones, whether it's Prime or they sort of all have ads now because it's basically like cable at this point.
[394.50 --> 395.80]  But all of them have ads.
[395.90 --> 399.50]  So I've seen the Coca-Cola ad on the streaming services.
[399.88 --> 406.28]  And yeah, I think maybe those that haven't seen it out there should go watch it.
[406.28 --> 415.32]  I think it's interesting that there's certain elements of it that give you that AI-generated vibe, right, where you could kind of tell.
[415.44 --> 421.22]  But it definitely evokes the character of the sort of Coca-Cola ads.
[422.08 --> 424.76]  And lots of people don't like it.
[425.12 --> 426.66]  Lots of people think it's interesting.
[426.66 --> 439.56]  Some people on LinkedIn I've seen said, well, if AI-generated video is good enough for Coca-Cola's Christmas ads, then who is it not good enough for at this point?
[439.66 --> 442.26]  Which is maybe a hot take.
[442.36 --> 442.72]  I don't know.
[442.82 --> 444.02]  Any thoughts, Chris?
[444.28 --> 447.20]  I'm just kind of amazed that people are surprised by that these days.
[447.46 --> 450.44]  You know, it's like you're going to see this stuff everywhere.
[450.92 --> 453.38]  And so, okay, iconic thing.
[453.46 --> 454.12]  I got it.
[454.12 --> 457.60]  But yeah, I mean, I would have been almost surprised if they hadn't.
[458.00 --> 458.10]  Yeah.
[458.66 --> 471.24]  And yeah, if you just search for Coca-Cola ad, I think it's the Real Magic Holiday ad, which is also a bit ironic that they titled it Real Magic.
[471.24 --> 472.10]  Real Magic.
[472.42 --> 474.62]  When it's definitely not real.
[475.66 --> 477.28]  But yeah, you can watch it.
[477.42 --> 478.36]  It's pretty interesting.
[478.36 --> 484.36]  I think it's whether or not it's really, really good ad material.
[484.36 --> 484.84]  material.
[485.58 --> 491.50]  It's, I think, a sign that for sure AI-generated video is here with us for the future.
[491.96 --> 496.24]  So you had some months back the actors, you know, going on strike.
[496.32 --> 500.38]  But I just think that it's one of those things we have a long way to go.
[500.38 --> 507.88]  You know, not just in entertainment, but in most industries where it's going to, you're going to see corporate videos that are AI-generated.
[508.02 --> 508.92]  I've already seen that.
[509.52 --> 514.66]  I may not have seen the Coke one, but I, you know, I've seen corporations that are doing it.
[514.74 --> 515.64]  It's the way it is now.
[516.08 --> 516.16]  Yeah.
[516.16 --> 526.86]  Certainly companies like Synthesia and HeyGen and these video generation companies for training videos for, you know, multiple languages, all of these sorts of things.
[526.98 --> 528.76]  There's, there's a lot of use of those.
[528.84 --> 529.96]  I've definitely seen it.
[530.38 --> 530.68]  Disruption.
[531.26 --> 531.44]  Yep.
[531.92 --> 533.28]  Speaking of disruption.
[533.46 --> 534.00]  Oh boy.
[534.00 --> 538.32]  We haven't talked about this yet on the show, Chris.
[538.32 --> 551.94]  And I don't think either of us have a desire, nor maybe at least on my part, a, any sort of profound opinion on this topic, other than the fact of what it means for, for AI.
[551.94 --> 559.70]  But I saw an article in, in time about what Donald Trump's when means for AI.
[559.70 --> 572.88]  So if you're, if you're listening to this podcast at a time, sometime in the future, when it's not election season, maybe you're looking back on this and you know what Donald Trump's second term meant for AI.
[573.08 --> 579.24]  But at this point we don't necessarily know, although that we could, you know, make some guesses, which we can talk about.
[579.44 --> 584.72]  But yeah, we're, we're about to go into the second Trump administration.
[584.72 --> 590.40]  Uh, so if you're listening to this at some other time, that's, that's the time that we're talking about this.
[590.88 --> 594.16]  And, uh, and yeah, so interesting.
[594.46 --> 609.10]  Uh, we've seen maybe just as a reminder, we've seen the Biden administration do some things as related to AI, including the executive order on AI, which we did talk about on the show.
[609.10 --> 612.26]  That was, uh, uh, episode two 44.
[612.78 --> 625.84]  So if you're wanting to know if we're referred to that and you want to know which, you know, the details and, and the interesting pieces of that executive order, that's episode two 44, which we'll link in the show notes.
[626.10 --> 627.26]  But yeah, interesting.
[627.26 --> 633.88]  Any, any initial takes on as, as a practitioner, what this means for us?
[633.88 --> 636.06]  I can tell you what I hope it means.
[636.06 --> 642.10]  And I hope, you know, during the first Trump administration, he didn't know very much about it.
[642.22 --> 652.30]  Uh, he brought in some corporate folks to, you know, put together some committees and they, you know, there was a little bit that came out of that, a website and stuff like that.
[652.30 --> 655.72]  But it didn't impact us too much at the time.
[656.30 --> 662.00]  And so I think part of me hopes that it may be, it will be, it will be gentle.
[662.38 --> 667.78]  Um, let him talk about rolling other things back, but maybe he's not aware enough of AI to do it.
[667.82 --> 669.44]  But of course it's been another four years.
[669.68 --> 671.62]  Um, and who knows where that's going.
[672.04 --> 679.90]  So, uh, a little bit, a little bit nervous to see where his, uh, policies take us, but I, I hope he's more or less hands off.
[679.90 --> 680.34]  Yeah.
[680.34 --> 680.82]  Yeah.
[681.10 --> 681.34]  Yeah.
[681.44 --> 694.44]  So in the time article, uh, this is a quote from that article, which we can put in the, in the show notes says, uh, Trump's own pronouncements on AI have fluctuated between awe and apprehension.
[694.44 --> 699.58]  This sort of, you know, describing it as a superpower or very alarming, right?
[699.74 --> 700.94]  Often in the same sentence.
[701.44 --> 701.76]  Yeah.
[702.06 --> 702.58]  Yeah.
[702.58 --> 703.16]  Maybe so.
[703.16 --> 724.58]  So, but one of the things I think that has been kind of promised maybe as a part of just undoing some of the things of the Biden administration, which I think we can expect, you know, more generally is, is a promise to repeal the executive order on AI among, you know, probably other things.
[724.58 --> 733.88]  And I think citing the hindrance of innovation, you know, this kind of anti-regulatory take on a lot of things.
[733.88 --> 759.56]  So there's a promise to, to repeal that I'm not a enough of a lawyer slash politician slash political analyst to know what exactly that undoes because, you know, the executive order, I think kind of has its tentacles in a variety of things that it touches that are maybe not immediately related to the executive order.
[759.56 --> 763.66]  Like the NIST AI risk frameworks and those sorts of things.
[763.88 --> 767.04]  So I don't know exactly how, how that works out.
[767.12 --> 769.68]  Maybe that's a point of confusion on, on my part.
[769.68 --> 770.20]  Yeah.
[770.26 --> 785.44]  My concern is, you know, there are some things that I think if you didn't just have a knee jerk reaction to anti anything that Biden did, that there are actually some things that the current administration and the incoming administration should be able to agree on.
[785.44 --> 796.72]  And one of those that's not AI, just as an example is, is the CHIPS Act, which is kind of trying to bring semiconductor capabilities, you know, back online in the U S.
[796.72 --> 809.30]  And if you are kind of, if you're an administration that's anti China or, you know, in the China, Taiwan concern, then you would think that that's act, which Trump has said he is.
[809.48 --> 818.30]  You would think that that's actually something that both sides of the aisle could agree to, but he's also said he's going to repeal the CHIPS Act as well.
[818.30 --> 826.24]  And I fear that this, uh, that the executive order, since it is something he can repeal with just the stroke of a pen might suffer that.
[826.42 --> 830.96]  And yet I think that he would be making a mistake regarding his own administration.
[830.96 --> 832.30]  I think that would create problems.
[833.36 --> 833.46]  Yeah.
[833.56 --> 843.74]  The article that we're referring to even talks about this, that, uh, there's some statements about, you know, we're going to need more, more chips and more chip production.
[843.74 --> 844.42]  Right.
[844.46 --> 849.80]  But at the same time, the, as you mentioned, the Trump campaign has attacked the CHIPS Act.
[849.80 --> 873.68]  I saw, you know, certain things of course are still, you know, in progress that would, I think, fit the America first, you know, chip production piece of that, including, I just saw in the news that, uh, that Intel was awarded up to 7.9, almost 9 billion.
[873.74 --> 884.96]  Under the CHIPS Act to help build or expand chip plants in Arizona, New Mexico, Ohio, and Oregon, including 1 billion plus later in 2024.
[885.40 --> 892.70]  So some of this, I know, especially the, the Ohio plant and all of that is, I think in progress.
[892.70 --> 898.32]  I don't know the exact details of that, but, um, but yeah, some of this is in motion.
[898.32 --> 901.12]  So it is a bit confusing to me.
[901.12 --> 913.10]  I, I'm sure that, uh, CEOs of large companies are, are on the edge of their seat and trying to get audiences with the right people and understand what, what's going on.
[913.16 --> 922.74]  I, I'm assuming, again, I don't know how all of these things work under the hood, but I'm assuming there's a lot of that shuffling going on to, to get a read on the situation.
[922.74 --> 934.02]  Yeah. I would hope that if there's anyone out there listening, uh, that might be a part of the incoming Trump administration, uh, making America great again is exactly what the CHIPS Act, uh, was intended.
[934.18 --> 937.76]  And frankly, I think the AI executive order, uh, does the same.
[937.76 --> 945.78]  So I think, uh, I'm hoping there's no knee jerk, uh, on those two things, despite the comments that maybe, maybe he'll let them continue.
[946.42 --> 957.20]  Yeah. What is your take on the potential perspectives on open source or, or closed and, uh, the Trump administration?
[957.20 --> 962.04]  Any, any thoughts on that in terms of how that may be influenced one way or the other?
[962.04 --> 970.64]  I don't really know at that point. I think it comes down to, uh, whoever who I, it depends on who's in his, uh, who's in the cabinet potentially.
[970.64 --> 976.84]  And it's more probably more specifically who's working on staff at the white house and what their takes on it are.
[976.88 --> 978.42]  And I, I, I couldn't speak to that.
[979.20 --> 982.02]  Yeah. I've seen a mix of takes on that.
[982.02 --> 989.96]  I think there's one perspective that while China has benefited greatly from open source AI, right?
[989.96 --> 1006.16]  Um, not only have they been model builders and actually producing a lot of technology in the AI space, but they've also benefited a lot from, you know, meta and us, uh, AI technology.
[1006.16 --> 1019.96]  So there's kind of one side of it that would be, well, let's, you know, lock that down in, in the same way that they might try to restrict exports of, of other things or, or that sort of thing.
[1019.96 --> 1036.80]  Um, but I've also seen the other take on the fact that, you know, you're basically anti-regulation and it would be kind of not within the character to be restrictive in terms of the open source AI world.
[1036.80 --> 1053.42]  So I, I think it's a little bit unclear. I, I'm certainly one that kind of views the, the future, even more importantly in, in security, privacy, conscious industries really driven by open self-hosted models.
[1053.42 --> 1058.56]  I think that's, that's really the way that you ensure security, privacy, transparency.
[1059.20 --> 1075.24]  Yeah. I think there's a lot of ambiguity at the moment because if you look at traditional conservatism, you know, uh, if you look at the, you know, Ronald Reagan, you know, because a lot of Republicans really look back to that, uh, open trade is huge, but we're also having Trump talking about tariffs.
[1075.24 --> 1083.90]  That's been the news of the week and, you know, that's kind of the antithesis of that. And so it's kind of hard to, to figure out where the ball is going to land on those.
[1097.24 --> 1104.78]  Okay. Friends. One thing I'm obsessed with now is using notion AI. Yes. I'm a notion user, a power user. I would say.
[1104.78 --> 1114.54]  I use it for myself. I use it for change log and it's just so effective to organize everything. And with the addition of notion AI, it is a single tool that does it all.
[1114.54 --> 1122.12]  It searches across notion, other apps, generates docs of my own style. It analyzes PDFs and images. It can chat with me about anything.
[1122.72 --> 1130.98]  Now you may know notion as the perfect place to organize your tasks, to track your habits, to write beautiful docs and all the things you could do with notion.
[1130.98 --> 1145.82]  But adding notion AI with the context of your work is simply revolutionary. And unlike specialized tools or legacy suites that have you bouncing between six different apps, notion is seamlessly integrated, infinitely flexible.
[1146.40 --> 1155.50]  And yes, it is beautiful on the eyes. And yes, I am obsessed with notion AI because I could pretty much ask it anything. And it's just there for me.
[1155.50 --> 1160.00]  It's super fast and it's relevant to all of the stuff I have inside notion.
[1160.00 --> 1170.70]  You can try notion today for free by going to notion.com slash practical AI. That's all over case letters, notion.com slash practical AI.
[1171.28 --> 1178.82]  Try the powerful, easy to use notion AI today. And when you use our link, you're supporting our show, which is awesome.
[1179.28 --> 1182.88]  Again, notion.com slash practical AI.
[1185.50 --> 1213.66]  One thing that was kind of brought up in the midst of this talk of the Trump administration and AI is this sort of AI and China discussion where there's a thought, you know, AI is kind of thriving in China and maybe China is pulling ahead in AI.
[1213.66 --> 1227.64]  I know we've talked about this on the show before. There's kind of this discussion of China and AI every time policy decisions are discussed on the show and kind of factors in.
[1228.28 --> 1235.76]  And one of those things that I think is relevant is just the dominance of Quinn based models in recent times.
[1235.76 --> 1246.74]  So if people aren't aware, one of the things that I think is interesting to follow recently is Alibaba's Quinn family of models.
[1246.74 --> 1250.84]  That's spelled Q-W-E-N, Quinn.
[1251.36 --> 1256.94]  The latest of these is the Quinn 2.5 model family.
[1256.94 --> 1264.88]  And generally these Quinn 2.5 models are quite impressive.
[1265.38 --> 1272.94]  They generally top the open LLM leaderboards in various categories.
[1273.72 --> 1275.86]  You'll see them in the top spots.
[1276.62 --> 1280.16]  So obviously these are Chinese models.
[1280.46 --> 1285.60]  That is, they're models being built by a Chinese company, Alibaba.
[1285.60 --> 1296.28]  The CEO of Hugging Face, Clem, is quoted in one article I was reading of, you know, Quinn 72B is the king and Chinese models are dominating.
[1296.58 --> 1299.10]  That's a pretty clear statement.
[1299.50 --> 1307.22]  That was earlier in the summer, but I think we've seen continued domination of these models.
[1307.22 --> 1326.94]  Any interesting takes on that, Chris, in terms of how you've seen the model landscape shift from closed model providers to open to maybe more geographically diverse and certainly China being within that?
[1327.40 --> 1328.08]  I'm in an industry.
[1328.22 --> 1331.84]  I'm in defense and intelligence where obviously we're not going to be using Chinese models.
[1332.20 --> 1335.32]  And so we have not been focusing on that.
[1335.32 --> 1340.16]  We, of course, keep track of everything out there, but that's not one word likely to use.
[1340.98 --> 1345.98]  But I'm really curious in kind of outside of the sector that I'm in.
[1346.34 --> 1349.72]  I'd love to get some feedback from people on what they're uptaking.
[1349.86 --> 1353.66]  I think there are a lot of industries where they're not going to care either way on that.
[1353.82 --> 1357.12]  And they're going to go for the best models on the leaderboard.
[1357.38 --> 1359.58]  But I haven't actually talked to anyone who's done uptake.
[1359.72 --> 1360.14]  How about yourself?
[1360.14 --> 1373.76]  Yeah, and maybe this is an interesting little diversion here because I think some people don't understand the potential security risks as associated with this sort of model.
[1373.92 --> 1377.02]  So we say it's a model produced in China.
[1377.56 --> 1384.36]  Some people would be uncomfortable because of China's use of data or ways that they would use this technology.
[1384.36 --> 1393.14]  But if we look at the model itself, so you can go to Hugging Face and just search for Quinn models.
[1393.86 --> 1400.96]  So the Quinn models are open in the sense that you can go to Hugging Face.
[1401.16 --> 1404.26]  It's a repository of models.
[1404.48 --> 1406.86]  You can literally go to the Quinn model.
[1406.86 --> 1414.26]  You can download the weights of the model and load that model into infrastructure that you control.
[1414.62 --> 1422.70]  So this model, when you think of the model, is composed of parameters and model code that runs that model.
[1423.36 --> 1426.52]  And so if you go to the model on Hugging Face, you can download that.
[1426.52 --> 1446.18]  Now, similar to like if you were to go to GitHub and you look at all of the repositories on GitHub, some of those repositories on GitHub will have security considerations or licenses that won't allow you to use them or, you know, sources that you don't trust.
[1446.18 --> 1458.12]  Right. It's a little bit interesting here because these models are kind of loaded into code that is maintained by Hugging Face, the transformers library or other serving frameworks.
[1458.12 --> 1475.26]  Right. So if you're self hosting the model, meaning you're pulling the model down from Hugging Face, the files, and you're loading it into code that can serve that model, that model serving is under your control and you are downloading those files, meaning you can inspect them.
[1475.26 --> 1478.38]  It doesn't mean there's no security vulnerabilities associated with them.
[1478.38 --> 1480.86]  But ultimately, all of that is under your control.
[1481.00 --> 1499.08]  That is a different scenario than if you were to connect to an API that is serving the Quinn model, which there are ones from Alibaba and others that where this model is actually hosted as a product of a Chinese company.
[1499.08 --> 1508.44]  You know, you're sending your data to that API product, which is then, you know, processing your data and giving your response back from the model.
[1508.70 --> 1511.86]  So I just wanted to emphasize there's kind of these two scenarios here.
[1512.02 --> 1519.94]  So one, in one scenario, the security vulnerability is really related to the model files that you're downloaded.
[1519.94 --> 1524.18]  Is there any security vulnerability in those model files, which there could be?
[1524.50 --> 1530.52]  Is there any third party code that's used in when you load those model files, which there could be?
[1530.70 --> 1536.26]  And what serving framework are you using to serve them, which could have security vulnerabilities?
[1536.64 --> 1543.62]  In the other case, you're relying on someone else's infrastructure, which isn't under your control, which might be under Alibaba's control.
[1543.62 --> 1546.30]  So these are just different concerns that you want to weigh.
[1547.00 --> 1556.64]  And I thought that may be good to highlight because some people may even want to experiment with the Quinn model, like in a thing like LM Studio or something like that.
[1556.80 --> 1561.88]  I'm not vouching for all the safety considerations that might be in your mind.
[1561.88 --> 1574.68]  But it's not like I don't think when you use Quinn in LM Studio, there's some sort of phone home to Alibaba going on necessarily in the underlying code that's running that.
[1575.00 --> 1580.60]  I think in like U.S. government circles, just to clarify something, I think it's more policy than necessarily.
[1581.12 --> 1586.94]  So I think you're going to have some agencies that are downloading all the models and reviewing and inspecting and stuff like that.
[1586.94 --> 1600.56]  But I think for typical usage, you're looking at more of I think you're much more likely to see a U.S. agency or corporate that is serving the U.S. government going to be focusing on on meta versus the Alibaba.
[1600.96 --> 1602.48]  I think that's just a policy issue.
[1602.98 --> 1603.94]  Yeah, yeah, yeah, for sure.
[1604.42 --> 1605.74]  I think you're you're right.
[1605.84 --> 1608.86]  I think I've just seen a lot of confusion around this.
[1609.02 --> 1610.48]  It's like no, it's good clarification.
[1610.78 --> 1614.34]  Anytime you use a Quinn model, it's stealing your data.
[1614.34 --> 1619.52]  But there there may be ways to use this in a way that is appropriate for your scenario.
[1620.04 --> 1620.14]  Sure.
[1620.34 --> 1631.72]  Likely, like you say, if you're working in defense or something, that's going to be a different consideration than if you're hacking together a cool AI agent on your side project, you know, for personal purposes.
[1631.72 --> 1635.68]  Those are very, very far apart on the on the spectrum.
[1636.52 --> 1638.48]  So, yeah, very, very interesting, though.
[1638.76 --> 1642.64]  Also, there's there's some recent development.
[1642.64 --> 1648.88]  So as of so we're late in November already, but this is, I think, about a week ago, something like that.
[1649.34 --> 1664.12]  Quinn Turbo one million was released, a sort of new version of this, which extends the context length of the Quinn 2.5 language models from 128K to one million tokens.
[1664.12 --> 1668.08]  So that's to kind of give a context.
[1668.32 --> 1675.48]  Some of what's cited is like 150 hours of transcripts or 30,000 lines of code or or these sorts of things.
[1675.48 --> 1681.26]  So lots of context can be put into these models, you know, which is a trend that has continued.
[1681.26 --> 1686.32]  And I have my own opinions about, but it does seem to be a trend that continues.
[1686.32 --> 1687.48]  Go ahead and share them.
[1687.66 --> 1690.10]  You can't hang that out there and not go there now.
[1690.10 --> 1710.74]  Yeah, well, I just think if you think about the typical the most common enterprise cases that I run across in working with customers, most often these fit these scenarios of what I like to think of as something that could be done by a college level intern.
[1710.74 --> 1716.88]  Right. So you have some very clear instructions to do this sort of workflow.
[1717.00 --> 1718.24]  And it might be multi-step.
[1718.46 --> 1723.38]  It might be a complicated workflow, but it's all like you can break it down in a sequence.
[1723.56 --> 1725.52]  It's there's instructions there.
[1726.02 --> 1738.44]  So anecdotally, if you go to a college level intern and you say, go into the warehouse out back, there's, you know, rows and rows of documents.
[1738.44 --> 1740.58]  Now do this task for me.
[1740.98 --> 1741.14]  Right.
[1741.40 --> 1753.74]  That's a much harder thing with a higher degree of potential failure than if you go to the warehouse and you find generally the section that's relevant to a task.
[1753.74 --> 1760.42]  And you say, hey, you know, look at these couple folders of documents and do the task.
[1760.42 --> 1762.98]  You're much more likely to get a better result.
[1763.18 --> 1767.48]  And I think these models, you know, anecdotally behave similarly.
[1767.48 --> 1776.72]  And there's some evidence for this in terms of the forgetting of what's in the middle of the context, which has been observed, you know, in academic research.
[1776.72 --> 1781.12]  And I'm sure people on this podcast will be like, no, Daniel, that's solved.
[1781.28 --> 1781.98]  You know, whatever.
[1782.18 --> 1790.22]  It's just my own sort of experience and anecdotes in terms of what what has been found to be useful.
[1790.36 --> 1792.98]  It's just, yeah, a million tokens is a lot.
[1793.64 --> 1796.36]  So possibly more than most people are going to need.
[1796.36 --> 1805.44]  And I know people, you know, that have been on this podcast and are peers of mine that totally disagree with what I just said.
[1805.64 --> 1806.56]  So that's OK.
[1807.56 --> 1810.48]  We're all kind of figuring it out as we go along, I guess.
[1810.48 --> 1818.60]  So Quinn 2.5, that intersects with some of our discussion around the China-America debate.
[1818.72 --> 1827.68]  But there's a variety of models that people might be interested in in just taking a quick look at that have popped up over the last weeks.
[1827.84 --> 1836.20]  And I don't think we've it's been a while, Chris, since we've done a here's a buffet of new models type of brief disclosure.
[1837.02 --> 1839.02]  And there's a few interesting ones.
[1839.02 --> 1848.76]  So there's one that is from DeepSeq, which previously released a series of really good coding models.
[1849.02 --> 1868.56]  But they've they've released DeepSeq R1 Lite Preview, which is kind of fitting in this like chat GPT 01 or OpenAI 01 kind of world, which is this going to pause and think about things sort of sort of world.
[1869.02 --> 1874.48]  Where it's trying to solve very complicated, you know, math benchmarks or other things.
[1874.48 --> 1887.12]  And so you see, actually, this DeepSeq model in many cases for certain benchmarks, maybe even doing better than 01 preview in a number of benchmarks.
[1887.12 --> 1898.02]  So I think this is further evidence that this this gap between the closed model providers at the frontier and open model providers is just closing so rapidly.
[1898.02 --> 1909.02]  It's, in my opinion, it's in my opinion, basically not distinguishable anymore in a lot of things that people want to do, whether you want to use an open model or closed model.
[1909.02 --> 1911.92]  So let me ask a couple of questions around that.
[1912.02 --> 1918.56]  Number one is, you know, we've we've seen so much in the news about kind of hitting the limit lately.
[1918.72 --> 1925.96]  You know, OpenAI has come out and talked about delays on on future models because they're kind of hitting practical limit.
[1926.06 --> 1928.46]  People have left the organization as a result of that.
[1928.46 --> 1934.26]  And just in general, we're seeing, you know, that's been the conversation in industry over the last, you know, month or two.
[1934.26 --> 1947.94]  And as we do that, are we do you think that this is kind of the place that we're going to continue to see models evolving into where instead of just getting bigger and, you know, larger context windows and the whole thing, you know, all that, you know, always bigger, always better.
[1948.16 --> 1961.32]  That we're starting to see these kind of, you know, these preview 01s, the 01 preview styles where they are pausing and they're bringing whole new techniques in to tackle certain types of problems.
[1961.32 --> 1964.64]  Is that are we maybe going down that path as well as others?
[1965.50 --> 1966.04]  Yeah, yeah.
[1966.10 --> 1990.32]  I think from my perspective, at least, one thing that's happening is the gains that are being made from more data and larger models have basically plateaued, which has been observed, which means that smaller models that people are doing a lot of work to curate data for and innovate.
[1990.32 --> 1995.30]  And innovate in terms of their efficiency are catching up rapidly to the larger models.
[1995.30 --> 2010.32]  So what would have been only possible by, you know, 70 B model or a 400 B model, even six months ago or three months ago is being done by 7 B models or smaller.
[2010.70 --> 2010.84]  Right.
[2010.90 --> 2018.96]  So you've got this small model trend where these models are actually performing at levels much higher than than what was able to be seen before.
[2018.96 --> 2033.18]  And then you have kind of branching out to various both specializations or domains and kind of unique prompting or or formatting skills.
[2033.18 --> 2039.56]  So domains like document parsing or vision and that sort of thing.
[2039.94 --> 2050.10]  Hugging Face just recently released the small LVM, which is a small model that does sort of vision related activities.
[2050.10 --> 2060.18]  There's the out TTS, which is a really efficient, you know, 350 and 500 million parameter text to speech model.
[2060.42 --> 2068.56]  Both of those, I think, represent these this kind of specialization of smaller models and doing really well at specific things.
[2068.56 --> 2086.60]  And then I think you will see kind of an attempt to continue to develop new types of fine tuning and prompting methodologies for things like this deep thinking and for things like agent related workflows, which I think people are going to be diving into more.
[2086.60 --> 2100.62]  So it may be more about the workflow, the prompting format, the prompting strategy as we move forward for just pure text models than bigger and better models, bigger and better data sets.
[2100.62 --> 2119.64]  Well, I'm here with a good friend of mine, David Shue over at Retool, big fan of Retool, big fan of internal tools built with Retool.
[2119.74 --> 2123.30]  But David, not everybody knows how to use Retool.
[2123.68 --> 2125.80]  What can't you build with Retool?
[2125.80 --> 2137.04]  Yeah, so Retool is really good for building any sort of CRUD application where you care mostly about security, authentication, authorization, sort of internal facing things, basically.
[2137.32 --> 2142.60]  If you're looking to build, let's say, like Google Maps, for example, probably you should not be using Retool for that.
[2142.92 --> 2147.96]  You know, go write some custom JavaScript or React, you know, in order to go build a really complex application like Google Maps.
[2148.16 --> 2150.24]  But if you're looking to build a CRUD app, Retool is great for that.
[2150.24 --> 2158.86]  And what we see especially is that backend engineers who have less experience in the frontend or less interest in the frontend really gravitate towards Retool.
[2159.10 --> 2164.46]  Because for a backend engineer, sometimes all you want to do is you want to get a formal type of database, test that it's working.
[2164.64 --> 2166.32]  You want to go test that API, for example.
[2166.66 --> 2170.48]  And spinning up a quick app in Retool is so much faster.
[2170.68 --> 2177.20]  They're trying to go learn React, learn Redux, learn state management, learn all these different parts of the frontend stack.
[2177.20 --> 2178.52]  And it's kind of so complicated.
[2178.72 --> 2183.70]  And so I think that backend engineers in particular really gravitate towards Retool for building fast-crud apps.
[2184.12 --> 2189.62]  Okay, friends, the best way to build internal software is by going to Retool.com.
[2189.86 --> 2194.90]  You can seamlessly connect databases, build with elegant components, and add your own code on top.
[2194.90 --> 2202.70]  You can accelerate mundane tasks by not learning React, not learning Redux, and freeing up the time you need to work on the things that matters most.
[2203.22 --> 2204.40]  Once again, Retool.com.
[2204.48 --> 2206.06]  Start for free or book a demo.
[2206.06 --> 2207.88]  Retool.com.
[2207.88 --> 2237.86]  Well, Chris, speaking of a couple things that I think are pretty cool and maybe even practical that we could share as people are trying to level up things,
[2237.86 --> 2248.14]  One which is just fun, which is on my list of things to try this week, is something that I found or someone pointed me to, which is called Pickle.
[2248.68 --> 2250.38]  Granted, I haven't tried this yet.
[2250.38 --> 2251.38]  I actually just found it.
[2251.38 --> 2253.42]  I actually just found it today.
[2253.62 --> 2255.56]  But it's not the Pickle.
[2255.70 --> 2261.06]  If you're a Python programmer, Pickle means something very specific, which is a serialization format.
[2261.06 --> 2271.88]  But if you're not a Python programmer, yeah, if you just go to getpickle.ai, this seems like what I've been waiting for for a good long time.
[2271.88 --> 2275.46]  Which is just a pretty good catchphrase.
[2275.70 --> 2277.32]  Join meetings with clone.
[2277.84 --> 2282.24]  That's all I pretty much wanted to do for quite a while.
[2282.24 --> 2293.36]  The idea is basically you would have a kind of professional looking video and you could be laying in your bed without any pants on and your headset on.
[2293.60 --> 2301.82]  And your audio would be going through your clone into a very professional looking person that has joined a Zoom call or whatever call.
[2301.82 --> 2307.02]  But you don't have to ever put any pants on or, you know, that sort of thing.
[2307.06 --> 2310.38]  Or you're driving, but it looks like you're in your office, right?
[2310.82 --> 2312.10]  It looks great to me.
[2312.24 --> 2313.84]  I'm all in on this thing.
[2314.14 --> 2315.66]  Yeah, so super interesting.
[2315.66 --> 2329.06]  I mean, I don't know what this sort of thing, along with other things like AI avatars and all of this, means for kind of the relational elements of work.
[2329.06 --> 2345.34]  What I was kind of thinking when I saw this was, well, can I go a step further and just like generally instruct a language model to generate my responses and only just sit there listening to my clone, right?
[2345.38 --> 2349.50]  I just want to sit there listening to my clone while my clone does the meeting for me.
[2349.50 --> 2361.54]  And then just interject or kind of interrupt my clone and take over my clone's mind in the meeting when I need to correct something or jump in.
[2362.02 --> 2370.74]  And otherwise, because most of the time, I don't know about you, Chris, but most of my meetings are like, hey, we're going to go around and introduce everyone.
[2370.74 --> 2372.44]  So no problem.
[2372.54 --> 2373.84]  My clone can introduce me.
[2374.72 --> 2379.34]  And then you can go around and be like, you know, what's your update on this project?
[2379.96 --> 2382.64]  Paste in a document, have it give an update.
[2382.98 --> 2385.84]  There's really not a lot of things that I do in meetings.
[2386.64 --> 2390.96]  Maybe this is going to get me fired or reduce my value at work.
[2391.16 --> 2392.16]  You're your own boss.
[2392.24 --> 2393.24]  You don't have to worry about that.
[2393.24 --> 2397.82]  Yeah, like what there are important things occasionally.
[2398.44 --> 2401.96]  But yeah, I'm kind of wondering when that happens.
[2402.50 --> 2412.34]  I'm just thinking out there in corporate world, all the status meetings that people go to where you're just bringing your status and you're basically and exactly what you said.
[2412.42 --> 2414.34]  You have your status written down.
[2414.48 --> 2417.80]  You've kind of already pre-trained it to the introduction, all that.
[2417.80 --> 2423.46]  But you can kind of lay there half asleep in bed, let it just handle your turn when that comes.
[2423.98 --> 2430.82]  The only thing you've got to worry about is if somebody starts asking questions outside the context of what you can train.
[2430.98 --> 2434.20]  If someone takes the right turn, you've got to be ready to leap in.
[2434.44 --> 2439.50]  But, you know, I could see lots of my meetings being taken over by this capability.
[2439.68 --> 2440.96]  I would happily do that too.
[2440.96 --> 2452.30]  Well, and I don't know, like I say, what does that, because part of, like, let's take a stand-up, for example, an engineering team stand-up or something like that.
[2452.76 --> 2467.10]  Part of the idea behind such a thing, I think, I'm not a scrum master, but part of the idea would be to, you know, also actually hear, you know, with your ears,
[2467.10 --> 2477.68]  what other people are kind of their update and maybe that influences either they're blocked on something and you can reply or it influences.
[2477.96 --> 2487.50]  So I'm wondering what this does if it creates more potential isolation in an already remote work distributed environment.
[2487.50 --> 2495.30]  And part of me, so I have a friend, Mark Sears, shout out to Mark if you're listening.
[2495.88 --> 2498.44]  He's working on a venture studio called Sprout AI.
[2499.06 --> 2511.56]  And one of the things that is their, one of their theses is that they want to build technologies with AI that drive people relationally together as people.
[2511.56 --> 2519.20]  So the, the idea, just to give an example, would be like, Chris, you and I, maybe we're friends, we're both busy, we're professionals.
[2519.94 --> 2531.10]  And so there's an AI assistant that maybe looks at your calendar and looks at my calendar and looks at events going on in our town or things that fit both of our interests.
[2531.10 --> 2535.72]  And then messages us both and say, hey, you know, Thursday night, you're both free.
[2535.72 --> 2542.30]  And there's this event in your town, you know, are you guys, and that's a sort of thing that is cool.
[2542.40 --> 2546.56]  It kind of drives people relationally together, gets them out of their house, right?
[2546.60 --> 2559.84]  I think this idea of sort of embodied AI that would drive people relationally together is, is very appealing in our day and age and, and something that's needed.
[2560.02 --> 2563.92]  But I also love the idea of joining meetings with my clone.
[2563.92 --> 2574.04]  So I don't know how to bring those together, but, uh, I told you I'm all in, but, you know, going to your talk about kind of driving humans out to, to have real connections and stuff.
[2574.20 --> 2581.28]  I just have this vision of it kind of taking over the, you know, the dating world, you know, and that's, I'm a long way removed from that.
[2581.32 --> 2584.12]  I'm a, you and I are both, you know, happily married.
[2584.12 --> 2586.36]  I didn't think about that, Chris, but, uh, yeah.
[2586.36 --> 2595.54]  But no, I'm just having this vision of like, you know, the single guy and single woman, both are in a bar, but they're not, neither one's very comfortable.
[2595.54 --> 2597.98]  And they send their agents to connect like the agents.
[2598.24 --> 2600.06]  They send their agents to screen.
[2600.28 --> 2600.82]  That's right.
[2600.82 --> 2606.90]  The agents screen each other and decide whether or not it's a green, green or green, red, you know, figuring out.
[2606.90 --> 2611.16]  And it's like, you know, I, I can just imagine I, my daughter is too young to be dating.
[2611.26 --> 2620.96]  She's 12, but I could imagine 10 years down the road, you know, her having one of these agents, you know, and, you know, finding her boyfriend by, by letting the agents check each other out.
[2620.96 --> 2622.62]  So who knows where it's going?
[2623.10 --> 2623.20]  Yeah.
[2623.26 --> 2630.40]  And I guess that in their little video on their, on their site, like I said, they have a picture of a woman holding her baby.
[2630.40 --> 2630.88]  Right.
[2630.94 --> 2635.32]  And she's on the phone, you know, joining the meeting with a clone.
[2635.32 --> 2648.04]  So I could definitely see various lifestyle elements of this where, you know, there could be a stigma with like you joining a meeting, you know, your spouse isn't there.
[2648.04 --> 2652.26]  Like you, you have to deal with your baby at the time you're working from home.
[2652.26 --> 2652.52]  Right.
[2652.52 --> 2660.90]  And that may not be something that either you're comfortable or, or that would be accepted, unfortunately, and in kind of certain scenarios.
[2660.90 --> 2671.10]  And so, yeah, I definitely see, uh, elements of this, but also I wonder about the kind of isolation driving forces of, of all of this.
[2671.10 --> 2672.76]  You raise a really good point there.
[2672.76 --> 2693.26]  And, and just for a moment, stepping back out of, uh, you know, the AI driven meeting, uh, concept, if we step back a few years to when COVID was hitting and we were all kind of just making do, you know, and having remote meetings, we became much more tolerant of one another in terms of, you know, how your business life intersects with your personal life.
[2693.26 --> 2697.76]  And, you know, if the dog was barking in the background, people learn to be just fine with that.
[2697.82 --> 2710.94]  And if there was kids or baby, people learn that there is an element of this, uh, as we're talking about this particular thing about having that, uh, that clone out there of kind of going backwards on that trend.
[2710.94 --> 2722.60]  And us being a little bit less tolerant of one another, uh, because you're once again, projecting that perfect image, uh, whether you're in the car or on the toilet or in the bed or whatever it is that you happen to be doing that you don't want to reveal.
[2723.00 --> 2727.08]  So, um, so, uh, I, this is one of those things.
[2727.08 --> 2730.36]  I, it could be isolating to use it in that way as well.
[2730.84 --> 2730.94]  Yeah.
[2731.10 --> 2731.50]  Interesting.
[2731.50 --> 2738.10]  I think, uh, it will be interesting to see how people leverage these both ways.
[2738.10 --> 2749.38]  And like many things we've seen with this technology, there are opportunities for sort of restorative, positive, redemptive kind of uses of this technology.
[2749.38 --> 2755.76]  And, and there's ways that it can kind of drive us, drive us into isolation or, or create issues.
[2755.76 --> 2767.74]  But, um, yeah, uh, along that front of kind of lifestyle related things happening with AI, I've, I've seen a couple of posts recently related to kind of.
[2768.10 --> 2771.58]  Payments and commerce and shopping and, and AI.
[2771.58 --> 2782.02]  The first of those being a blog post from, uh, Stripe, which talks about adding payments to LLM agentic workflows.
[2782.02 --> 2805.28]  And, uh, I guess there's better tooling now to the Stripe agent toolkit, which is, uh, if you go to GitHub Stripe slash agent toolkit, you can now kind of plug in Stripe as a tool or as a thing that can be leveraged by AI agents.
[2805.28 --> 2812.60]  Uh, including those from Langchain, crew AI for sales, AI SDK, which it's definitely pretty cool.
[2812.60 --> 2814.04]  It's that kind of scenario.
[2814.04 --> 2819.50]  Like, Hey, AI, I need you to book a rental car for me next week.
[2819.88 --> 2820.40]  Right.
[2820.50 --> 2823.82]  And obviously that requires some sort of payment.
[2823.82 --> 2827.98]  I could also see it on the other end being a business owner right now.
[2827.98 --> 2843.02]  I'd love to say, Hey, create an invoice for this, a recurring invoice for this customer for these amount with this line items and, and send it to them with a message saying blah, or, you know, whatever those, those things are.
[2843.02 --> 2854.78]  There's definitely a room for maybe misuse or, or problematic things happening here, but certainly very, very interesting to see this side of things advance.
[2855.34 --> 2855.68]  It is.
[2855.80 --> 2859.28]  And I, I think it's a great thing personally in the concept of an agent.
[2859.46 --> 2862.74]  I know it'll take people time to get to trust it and get used to it.
[2862.88 --> 2870.70]  But I know in our household, we, at this point, we tend to buy our groceries and have them delivered and stuff because we're busy and doing stuff.
[2870.70 --> 2879.76]  And, and a lot of times it's the same stuff as you bought last week, but, uh, maybe with a few changes, cause you're planning a different type of meal at some point during the week.
[2879.76 --> 2888.74]  And I think if you can combine, you know, the agent with the payment capability and have the ability to kind of just smooth your life in that way.
[2888.90 --> 2890.58]  I know our family would love that.
[2890.64 --> 2893.46]  My wife would absolutely, uh, she'd go nuts for it.
[2893.46 --> 2897.38]  If, if that was available, she'd like, yep, I'm offloading that agent gets it all.
[2897.66 --> 2900.62]  There's another, I don't know if they're using the Stripe.
[2900.70 --> 2906.08]  API under the hood, but there's another entrant into this, which is perplexity.
[2906.28 --> 2914.06]  It now offers a sort of shopping assistant with a, an actual experience behind it kind of built in.
[2914.28 --> 2924.06]  So you have the, the ability to put in like, Hey, I'm, I'm doing this project and I'm, you know, wanting to do this and that.
[2924.06 --> 2931.02]  What are the items that I need and help me kind of shop for those that I think is kind of the, the vibe.
[2931.02 --> 2938.66]  And, you know, there's a search that happens obviously, and there's plugged into, uh, various products.
[2938.66 --> 2955.48]  And in this case they have a merchant program, which definitely seems, um, so I don't know whatever happened to kind of, uh, some of the monetization around like plugins and other things with chat GPT.
[2955.48 --> 2969.90]  But this definitely seems like a way to kind of get your product, you know, having a, having a wife that, uh, owns a business in the direct to consumer space and, and sells project products direct to consumer.
[2969.90 --> 2984.06]  There is this element of trying to figure out, well, how do I place my product or how does my product kind of filter up into search results when people are just searching on chat GPT perplexity, whatever.
[2984.94 --> 2991.74]  And so this does seem to be one angle on that where you can increase chances of being a recommended product.
[2991.74 --> 2995.50]  There's payment integrations, API, custom dashboard, et cetera.
[2995.50 --> 3003.20]  So there's a sort of merchant program element of the perplexity AI powered shopping assistant as well.
[3003.36 --> 3003.96]  Pretty interesting.
[3004.52 --> 3004.92]  Very nice.
[3005.10 --> 3006.04]  I'm looking forward to all of it.
[3006.08 --> 3007.48]  Let's just adopt now.
[3007.66 --> 3008.54]  I'm ready for all of it.
[3009.20 --> 3009.68]  Go.
[3010.08 --> 3010.30]  Yep.
[3010.82 --> 3024.04]  Well, as people build out their, their shopping assistants with the APIs from Stripe or others, or, or if you're building your own things, um, here at the end of our show, uh, we normally try to point people to a couple of useful things.
[3024.04 --> 3031.20]  And I'll just mention a couple very seemingly useful things that I ran across in the, in the past couple of weeks.
[3031.20 --> 3032.94]  One of those is called docling.
[3033.24 --> 3038.02]  You can just search for doc, D O C ling, and we'll put it in the show notes as well.
[3038.02 --> 3052.48]  So this seems to be a really nice toolkit that a lot of people I've seen mentioned related to document parsing, uh, which is a really hard thing generally, and a hard thing to get right in a lot of AI workloads.
[3052.48 --> 3060.44]  And there's some custom models that have been built around various complicated document parsing situations.
[3061.14 --> 3072.36]  So this kind of is a standardized way to parse PDFs and PowerPoints and images and Excel documents and other things and get them into a standardized format.
[3072.36 --> 3076.84]  The other one that I saw, which was, was pretty cool is called observers.
[3076.84 --> 3083.60]  I'm a big fan of, uh, duck DB, Argeala, hugging face datasets, all, all of that sort of tooling.
[3083.60 --> 3099.08]  And this is plugged into all of that and allows you to kind of suck in all of the requests that you're making to various AI API providers or your own models and save those in something like duck DB or Argeala or something.
[3099.08 --> 3122.46]  For the future of kind of searching through history of prompts, but also utilizing that either for just observation and transparency and logging and debugging, but also maybe for eventually, um, open source datasets around prompts or, um, even fine tuning datasets in your own context.
[3122.46 --> 3125.94]  So both of those pretty interesting new projects, check them out.
[3126.24 --> 3128.08]  But, um, yeah, this has been fun, Chris.
[3128.42 --> 3128.60]  Good.
[3128.68 --> 3130.02]  I, I learned a lot today.
[3130.20 --> 3131.90]  I appreciate you bringing some of the stuff.
[3132.38 --> 3132.64]  Yeah.
[3132.94 --> 3134.14]  Good to, good to chat.
[3134.28 --> 3135.32]  We'll, we'll talk to you soon.
[3135.68 --> 3136.12]  Take care.
[3136.12 --> 3144.24]  All right.
[3144.56 --> 3146.42]  That is our show for this week.
[3146.80 --> 3152.72]  If you haven't checked out our ChangeLog newsletter, head to changelog.com slash news.
[3152.96 --> 3155.20]  There you'll find 29 reasons.
[3155.42 --> 3155.76]  Yes.
[3156.06 --> 3158.78]  29 reasons why you should subscribe.
[3158.98 --> 3160.64]  I'll tell you reason number 17.
[3161.00 --> 3163.98]  You might actually start looking forward to Mondays.
[3163.98 --> 3166.84]  Sounds like somebody's got a case of the Mondays.
[3167.24 --> 3171.80]  28 more reasons are waiting for you at changelog.com slash news.
[3172.00 --> 3177.70]  Thanks again to our partners at fly.io to Breakmaster Cylinder for the beats and to you for listening.
[3178.12 --> 3180.74]  That is all for now, but we'll talk to you again next time.
