[0.00 --> 7.28]  Welcome to Practical AI.
[7.70 --> 17.72]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[18.06 --> 20.66]  Thank you to our partners at Fly.io.
[21.16 --> 27.92]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[27.92 --> 30.88]  So you can launch your app near your users.
[31.28 --> 33.26]  Learn more at Fly.io.
[35.40 --> 39.40]  Okay, friends, I'm here with Annie Sexton over at Fly.
[39.54 --> 42.14]  Annie, you know we use Fly here at ChangeLaw.
[42.14 --> 43.18]  We love Fly.
[43.50 --> 46.02]  It is such an awesome platform and we love building on it.
[46.06 --> 51.32]  But for those who don't know much about Fly, what's special about building on Fly?
[51.58 --> 56.38]  Fly gives you a lot of flexibility, like a lot of flexibility on multiple fronts.
[56.38 --> 58.70]  And on top of that, you get...
[58.70 --> 62.32]  So I've talked a lot about the networking and that's obviously one thing.
[62.52 --> 67.40]  But there's various data stores that we partner with that are really easy to use.
[67.90 --> 71.34]  Actually, one of my favorite partners is Tigris.
[71.54 --> 75.10]  I can't say enough good things about them when it comes to object storage.
[75.36 --> 79.46]  I never in my life thought I would have so many opinions about object storage, but I do now.
[79.46 --> 87.58]  Tigris is a partner of Fly and it's S3 compatible object storage that basically seems like it's a CDN, but is not.
[87.64 --> 93.08]  It's basically object storage that's globally distributed without needing to actually set up a CDN at all.
[93.18 --> 95.96]  It's like automatically distributed around the world.
[96.28 --> 99.60]  And it's also incredibly easy to use and set up.
[99.74 --> 101.96]  Like creating a bucket is literally one command.
[101.96 --> 110.64]  So it's partners like that that I think are this sort of extra icing on top of Fly that really makes it sort of the platform that has everything that you need.
[111.08 --> 113.08]  So we use Tigris here at ChangeLog.
[113.18 --> 114.62]  Are they built on top of Fly?
[114.90 --> 118.08]  Is this one of those examples of being able to build on Fly?
[118.50 --> 118.72]  Yeah.
[118.88 --> 123.70]  So Tigris is built on top of Fly's infrastructure and that's what allows it to be globally distributed.
[123.70 --> 132.56]  I do have a video on this, but basically the way it works is whenever, like let's say a user uploads an asset to a particular bucket.
[132.70 --> 136.62]  Well, that gets uploaded directly to the region closest to the user.
[136.72 --> 140.72]  Whereas with a CDN, there's sort of like a centralized place where assets need to get copied to.
[140.80 --> 144.58]  And then eventually they get sort of trickled out to all of the different global locations.
[144.74 --> 148.88]  Whereas with Tigris, the moment you upload something, it's available in that region instantly.
[149.08 --> 152.84]  And then it's eventually cached in all the other regions as well as it's requested.
[152.84 --> 157.44]  In fact, with Tigris, you don't even have to select which regions things are stored in.
[157.52 --> 159.10]  You just get these regions for free.
[159.36 --> 162.54]  And then on top of that, it is so much easier to work with.
[162.80 --> 173.46]  I feel like the way they manage permissions, the way they handle bucket creation, making things public or private is just so much simpler than other solutions.
[174.00 --> 177.68]  And the good news is that you don't actually need to change your code if you're already using S3.
[177.84 --> 178.72]  It's S3 compatible.
[178.72 --> 181.64]  So like whatever SDK you're using is probably just fine.
[181.70 --> 183.18]  And all you got to do is update the credentials.
[183.40 --> 185.04]  So it's super easy.
[185.68 --> 185.98]  Very cool.
[186.04 --> 186.44]  Thanks, Annie.
[186.60 --> 188.88]  So Fly has everything you need.
[189.08 --> 192.78]  Over 3 million applications, including ours here at Changelog.
[192.86 --> 195.44]  Multiple applications have launched on Fly.
[195.44 --> 207.92]  Boosted by global anti-cast load balancing, zero configuration private networking, hardware isolation, instant wire guard VPN connections, push button deployments that scale to thousands of instances.
[208.28 --> 210.22]  It's all there for you right now.
[210.66 --> 211.80]  Deploy your app in five minutes.
[211.96 --> 213.90]  Go to fly.io.
[214.28 --> 216.28]  Again, fly.io.
[216.28 --> 217.28]  Fly.io.
[217.28 --> 218.28]  Fly.io.
[218.28 --> 219.28]  Fly.io.
[219.28 --> 220.28]  Fly.io.
[220.28 --> 221.28]  Fly.io.
[221.28 --> 222.28]  Fly.io.
[222.28 --> 223.28]  Fly.io.
[223.28 --> 223.40]  Fly.io.
[223.40 --> 223.44]  Fly.io.
[223.44 --> 223.88]  Fly.io.
[223.88 --> 224.44]  Fly.io.
[225.44 --> 226.44]  Fly.io.
[226.44 --> 227.44]  Fly.io.
[228.54 --> 229.10]  Fly.io.
[229.10 --> 232.12]  Welcome to another episode of the Practical AI Podcast.
[232.58 --> 233.94]  This is Daniel Whitenack.
[234.10 --> 237.00]  I am founder and CEO at Prediction Guard.
[237.60 --> 246.72]  And I'm really privileged today to have in the Prediction Guard offices one of my good friends, Mike Lewis, who I've known for a little while now in the AI space.
[246.72 --> 256.90]  And I think have been really intrigued to see how Mike as an architect has been able to solution certain AI tools with his customers, with his partners.
[257.28 --> 262.00]  He's currently the chief AI architect at Symphony down in Cincinnati.
[262.00 --> 264.26]  And yeah, it's great to have you here, Mike.
[264.72 --> 265.66]  Thank you, Daniel.
[265.96 --> 269.16]  And I've been looking forward to this for a long time.
[270.28 --> 277.42]  Obviously, a huge fan of the show and have learned so much by listening to you and Chris.
[277.42 --> 281.26]  But I just am so excited to dig in here.
[281.88 --> 297.84]  Well, one of the things that I think is really intriguing is that I've heard a lot recently that there's some disappointment a lot of times and people trying to find value with AI, especially in enterprise corporate environments.
[297.84 --> 301.72]  I've heard things like the tools aren't there yet.
[302.38 --> 309.04]  We have yet to kind of fully realize the value of AI and there's some disillusionment maybe.
[309.66 --> 313.00]  But I've known you for a while now, a couple of years at least.
[313.00 --> 332.44]  And even before we had GPT-4, GPT-3, you were creating and architecting solutions for people that actually led to value and eventually led to your business getting acquired by a company that's engaged with Fortune 50 companies.
[332.70 --> 339.20]  And you continue to prove that you can find solutions with this latest wave of AI technology.
[339.94 --> 342.08]  And so there's a disconnect for me here.
[342.08 --> 352.64]  You know, from your perspective, as that sort of architect, people are talking about this disillusionment, but you've also been finding these solutions with your partners.
[353.14 --> 355.22]  So, yeah, what's your perspective on that?
[355.28 --> 356.76]  Are we not there yet?
[356.90 --> 358.42]  What is the state of these tools?
[358.86 --> 359.54]  That sort of thing.
[360.16 --> 363.04]  Frankly, I've done a lot of head scratching on this topic.
[363.70 --> 365.94]  There are astronomers and there are astronauts.
[366.64 --> 371.16]  And, you know, the astronomers get out their telescopes and they look at the stars and they tell us about all these things.
[371.16 --> 373.76]  And the astronauts get up there and work on the satellites, right?
[374.48 --> 381.60]  And I think you and I both have been up, you know, been up in orbit for a while now.
[381.72 --> 387.66]  And, you know, I tend to not pay too much attention to all the people who tell me the things these tools can't do.
[387.66 --> 396.30]  So most of the time I'll go to a conference or, you know, I wind up in an environment where, you know, there's a lot of talk about the tools.
[396.98 --> 403.96]  And I'm just astonished at the use cases where I will hear that there's no value currently and we're waiting on that.
[403.98 --> 407.32]  And then at the same time, it feels like the same person will tell me all the things it can do.
[407.32 --> 409.74]  And I'm scratching my head on the, well, how'd you get it to do that?
[410.12 --> 416.52]  You know, and so the reality is it's just, I mean, there's a whole universe of problems and solutions.
[416.52 --> 428.34]  And we were talking about it earlier that, you know, to be involved with even just generative AI, you know, not even counting all the stuff going back a decade or decade and a half or since the 50s, I suppose.
[428.52 --> 435.66]  But even just the recent developments, golly, I mean, I don't think any human could really understand it all, right?
[435.66 --> 437.50]  And so we all tend to carve out a niche.
[437.60 --> 440.42]  I know you have a phenomenal niche carved out.
[441.38 --> 449.38]  And mine tends to be, you know, get to know the client, find the low-hanging fruit, prove out value, right?
[449.38 --> 454.60]  And then start making decisions about, you know, is now the time to, you know, put something in production.
[455.24 --> 463.94]  That said, I understand, you know, I mean, if you hadn't been tinkering and you haven't built 150 tools already,
[463.94 --> 467.04]  then it could feel like they don't do a lot.
[467.12 --> 472.78]  Because frankly, I worked really hard to figure out how to solve all those problems, right?
[473.22 --> 475.54]  And it's not like I'm running around telling everyone how I solve them all.
[475.72 --> 477.20]  I hope to do that today.
[477.20 --> 478.74]  A little bit of that.
[479.52 --> 479.96]  Yeah.
[481.14 --> 483.22]  It can't do it until it can.
[484.20 --> 486.20]  And sometimes it's not that the tool can't.
[486.90 --> 490.88]  It's just that the user, you know, hasn't been creative enough yet.
[490.88 --> 491.68]  Yeah.
[491.88 --> 503.02]  And maybe this might be good context for certain people because even before the show, I think it was interesting to talk to you about perceptions in this space.
[503.16 --> 511.68]  There's sort of a perception maybe by larger organizations or teams that don't have kind of data science, AI expertise,
[511.68 --> 519.60]  that we sort of don't have the know-how or the expertise or the skills to be able to adopt this technology in a meaningful way.
[519.60 --> 525.66]  And I think it's interesting that your background, although you have some technical background,
[525.92 --> 531.48]  it's not like decades and decades as an AI researcher at Meta or something like that.
[531.70 --> 542.64]  Can you describe a little bit of your background and kind of how that's influenced maybe how you've come into this space and how you've come into this technology?
[543.04 --> 544.60]  I think that might be relevant for people.
[544.60 --> 551.38]  Yeah. As quick as I can, I'll say initially I aspired to be an industrial designer.
[551.58 --> 557.18]  And so even in high school, I worked when I was 17 years old, I worked as an industrial designer.
[557.38 --> 562.42]  And that might not seem possible, but the reality is I got an internship at a medical device company.
[562.42 --> 569.08]  And I went from like printer, paper, coffee boy to designer within like six months because I knew AutoCAD.
[569.26 --> 573.52]  And the company was hurting for like warm bodies to like draw up, you know, sort of.
[573.92 --> 584.10]  And so I had this amazing mentor who taught me problem solving from just – he just had a great way of explaining how to tackle problems.
[584.10 --> 589.14]  And so that was the framework that I kind of initially, you know, formed professional aspirations.
[589.38 --> 593.32]  I went off to college to become an industrial designer and I got an internship at NASA.
[593.98 --> 595.62]  Aerospace was where I wanted to go.
[595.80 --> 597.22]  And so that was all highly technical.
[598.00 --> 601.10]  And then my career took this massive turn.
[601.72 --> 609.72]  You know, we won't go too deep into it, but essentially I was presented with the opportunity to be a full-time professional portrait artist.
[609.72 --> 613.82]  And it just got really lucky in that my art was taking off.
[614.38 --> 621.80]  I spent the next 20 years essentially just traveling all around the world, painting portraits and, you know, all commissioned works.
[621.80 --> 623.78]  I did about 2,000 of those.
[624.64 --> 626.46]  Stepped away from that in 2016.
[627.88 --> 632.30]  We just completed a successorship and I really didn't know what I was going to do next.
[632.96 --> 637.00]  And I decided to just work with a couple of nonprofits just to keep myself busy.
[637.00 --> 640.08]  One was Homeless Shelter, the biggest one in Cincinnati.
[640.88 --> 644.76]  And then another one was a publishing company that operated a homeless shelter.
[644.90 --> 647.32]  So I was just kind of, I just kind of wanted to do that.
[648.02 --> 652.68]  And the publishing company ended up being bigger than I knew.
[653.14 --> 654.86]  They sort of had a global presence.
[655.44 --> 662.94]  Aside from several book lines, they had a magazine that had similar subscriber base to say like Newsweek or Sports Illustrated.
[663.12 --> 664.50]  So that's how many tables it was on.
[664.58 --> 665.72]  Sort of a niche publication.
[665.72 --> 674.48]  I wound up being asked to be the director of innovation for them, which suddenly I'm the director of innovation for a publishing company.
[674.58 --> 676.76]  You can kind of start to see some overlap.
[677.10 --> 681.14]  I took that job in 2000, probably 16 or 17.
[681.14 --> 681.52]  Yeah.
[681.52 --> 691.06]  Yeah, and it really hit around 19, I think, with the AI stuff when, you know, we started reading about, you know, oh, these tools are, you know, coming for us.
[691.54 --> 696.98]  It might have been 20, around COVID, I think is when some of this stuff started to, you know, the language models were surfacing.
[697.72 --> 700.14]  You know, not only was that going on, so I had that incentive.
[700.22 --> 703.62]  That alone would have been enough to really familiarize myself with the tool.
[703.62 --> 711.62]  At the same time, I'm hearing that there's a tool out there that you just type in words and it can spit out images.
[712.54 --> 714.86]  That's interesting to me because I sell images.
[716.04 --> 718.36]  In fact, we charge design images.
[718.50 --> 719.30]  We charge a lot.
[719.56 --> 721.86]  In fact, I'm uncomfortable with how much we have to charge.
[721.96 --> 727.48]  I feel like it's a deal breaker in a lot of scenarios because I know it takes us a month to land on.
[727.48 --> 733.18]  So I just wondered, is this something that we could leverage as an efficiency in our fine arts business?
[734.06 --> 740.60]  So OpenAI at the time was you could apply to become a beta tester just to get early access to DALI.
[741.10 --> 743.28]  And don't hold me into this.
[743.40 --> 745.68]  The way I remember it, there were three criteria.
[745.96 --> 748.50]  You needed to own a commercial arts business.
[749.30 --> 752.76]  You needed to have a large online following, which we did.
[753.36 --> 755.26]  And you need to have plans to commercialize.
[755.26 --> 756.92]  And, like, I could demonstrate all that.
[756.92 --> 763.86]  And I think I was approved within a week or so to get early access to DALI, which wasn't super impressive.
[764.06 --> 766.00]  Actually, I kind of remember being a little disappointed.
[766.54 --> 771.56]  Like, you know, that got me in sort of their, like, ecosystem really early.
[771.90 --> 774.42]  And so whenever, you know, the API hit, I was in there.
[774.44 --> 776.82]  And I already kind of knew how to code a little bit.
[777.08 --> 780.16]  So the Python, you know, Python pretty much looks like plain English.
[780.68 --> 781.42]  So here we are.
[781.42 --> 781.86]  Awesome.
[782.74 --> 782.92]  Yeah.
[782.92 --> 793.06]  So I guess as you were kind of first starting to develop those solutions, you know, first kind of your interest from the fine arts side.
[793.06 --> 802.46]  But then as you started to get into architecting these solutions with smaller businesses and the medium businesses and larger businesses, what have you found?
[802.46 --> 807.96]  Because I often, well, we sell infrastructure for this sort of thing at PredictionGuard.
[807.96 --> 823.16]  And so oftentimes we hear people that they have found maybe the right infrastructure, but they might not know where really the value at the application layer is unlocked in these models in the functionality that they have.
[823.16 --> 833.08]  So I know you spent a lot of time kind of categorizing certain things that you've seen as trends and commonalities among the solutions that you've developed over time.
[833.08 --> 850.98]  And I really like how you frame these in, you know, earlier today we were at lunch and talking about some of these less from the functional level, maybe a knowledge retrieval or information extraction and more from the kind of task or goal level.
[850.98 --> 857.62]  So like generating new ideas with AI is one of the ones that you mentioned to me, preserving important know-how.
[858.32 --> 863.94]  I think these sorts of ideas that can connect with a less technical audience.
[864.12 --> 872.62]  So how did you come on these trends and anyone that maybe we'll go through a couple, but any one of these that you would want to highlight?
[872.62 --> 875.78]  Yeah, so you're talking about our solution archetypes.
[876.16 --> 886.52]  And I initially, I was asked by my team to identify all of the different archetypes of solutions that I've tackled and sort of solved for.
[886.62 --> 894.42]  So none of the ones that we couldn't figure out, only the ones that we were able to, you know, get the client to sit forward in their seat and say, holy smokes, it can do that.
[894.42 --> 898.38]  Right. And I identified 35 and I brought it back to the team.
[898.44 --> 902.80]  They said, 35 is too many of anything. Get that down. Right.
[902.90 --> 915.80]  And so we got it down to 15. And so inside of each of the 15, what you'll see is like three or four or five examples of like either full blown applications or just a simple script that runs in the background.
[916.00 --> 922.94]  Here's what I'll say for the people who look at these tools, who've spent any time around them and will tell you, nah, they're not there yet.
[922.94 --> 931.82]  They're still baking, you know, whatever. They're probably people who have really only interacted with them in a chat bot kind of environment like chat GPT.
[931.92 --> 947.00]  I realize chat GPT is more than a bot. Right. But I can definitely appreciate how you could come to that conclusion if, you know, you're a business leader and you derp around on chat GPT for an afternoon and you kind of go like, how would I use this? Right.
[947.00 --> 955.54]  Right. It isn't until you start to bake personas or agents or if anyone's listening, you kind of don't fully understand what that means.
[955.66 --> 960.68]  You know, just to say an AI that has an awareness of a discrete task and purpose.
[960.68 --> 964.44]  So it's kind of like I, you know, I do this specific thing.
[964.50 --> 977.60]  Like when you start to learn how to program very good personas and park them in the middle of code where you can kind of automate them and have them, you know, oh, this this file hits this folder, trip off this chain reaction.
[977.60 --> 986.52]  And then this is the moment that used to be unsolvable or would have cost ten million dollars to figure out because there's so many if there are either ends, you know, like forget all that.
[986.76 --> 990.60]  Like, let's just aim this persona at it. Poof. Now we know which direction to go.
[990.78 --> 994.66]  And that's really like the simplest version of, you know, what to say.
[994.78 --> 999.26]  I will say, you know, for those of you who have perked up and thought, yeah, but how can we trust it?
[999.30 --> 1002.84]  It's like, hold on, like hit the brakes.
[1003.38 --> 1005.28]  How do you trust your co-workers? Right.
[1005.28 --> 1010.74]  Like we work with people all day and the same concerns that we have about these AI agents.
[1010.88 --> 1013.88]  I think most of them you could map onto your co-workers.
[1014.06 --> 1015.80]  And the reality is like, how can we trust it?
[1016.24 --> 1018.50]  The answer is because we worked really hard to make it very good.
[1019.88 --> 1026.82]  Or maybe you can't trust it 100 percent of the time, but maybe there are jobs that 90 percent of the time is good enough.
[1026.92 --> 1028.06]  Ninety nine percent of the time is good.
[1028.16 --> 1030.04]  Thirty percent of the time is good enough.
[1030.04 --> 1038.12]  There's all sorts of work where it's just kind of like something is better than nothing or no one was going to do this anyway.
[1038.12 --> 1042.64]  Or this just doesn't even make sense for a human to do because you got to do it 10,000 times a minute.
[1043.40 --> 1045.24]  And we're not going to pay that many, you know.
[1045.64 --> 1046.20]  Yeah.
[1046.20 --> 1062.12]  What's up, friends?
[1062.22 --> 1067.70]  I'm here with a friend of mine, a good friend of mine, Michael Greenwich, CEO and founder of WorkOS.
[1067.70 --> 1079.78]  WorkOS, WorkOS is the all in one enterprise SSO and a whole lot more solution for everyone from a brand new startup to a enterprise and all the AI apps in between.
[1080.28 --> 1085.12]  So, Michael, when is too early or too late to begin to think about being enterprise ready?
[1085.60 --> 1088.84]  It's not just a single point in time where people make this transition.
[1089.06 --> 1090.96]  It occurs at many steps of the business.
[1091.32 --> 1093.66]  Enterprise single sign on like SAML, auth.
[1093.82 --> 1095.98]  You usually don't need that until you have users.
[1095.98 --> 1098.20]  You're not going to need that when you're getting started.
[1098.62 --> 1099.96]  And we call it an enterprise feature.
[1100.24 --> 1105.46]  But I think what you'll find is there's companies when you sell to like a 50 person company, they might want this.
[1105.56 --> 1109.10]  They actually, especially if they care about security, they might want that capability in it.
[1109.24 --> 1112.86]  So it's more of like SMB features even if they're tech forward.
[1113.20 --> 1118.12]  At WorkOS, we provide a ton of other stuff that we give away for free for people earlier in their lifecycle.
[1118.36 --> 1119.36]  We just don't charge you for it.
[1119.36 --> 1125.32]  So that AuthKit stuff I mentioned, that identity service, we give that away for free up to a million users.
[1125.32 --> 1127.18]  One million users.
[1127.72 --> 1132.30]  And this competes with Auth0 and other platforms that have much, much lower free plans.
[1132.48 --> 1134.66]  I'm talking like 10,000, 50,000.
[1134.86 --> 1136.08]  Like we give you a million free.
[1136.32 --> 1140.74]  Because we really want to give developers the best tools and capabilities to build their products faster.
[1141.08 --> 1142.56]  You know, and to go to market much, much faster.
[1142.84 --> 1146.68]  And where we charge people money for the service is on these enterprise things.
[1146.68 --> 1151.02]  If you end up being successful and grow and scale up market, that's where we monetize.
[1151.02 --> 1153.14]  And that's also when you're making money as a business.
[1153.30 --> 1156.42]  So we really like to align, you know, our incentives across that.
[1156.84 --> 1160.32]  So we have people using AuthKit that are brand new apps just getting started.
[1160.82 --> 1164.16]  Companies in Y Combinator, side projects, hackathon things.
[1164.56 --> 1166.56]  You know, things that are not necessarily commercial focused.
[1166.80 --> 1167.94]  But could be someday.
[1168.20 --> 1171.20]  They're kind of future proofing their tech stack by using WorkOS.
[1171.20 --> 1174.68]  On the other side, we have companies much, much later that are really big.
[1175.06 --> 1177.44]  Who typically don't like us talking about them.
[1177.58 --> 1180.90]  Their logos, you know, because they're big, big customers.
[1181.42 --> 1183.32]  But they say, hey, we tried to build this stuff.
[1183.36 --> 1184.78]  Or we have some existing technology.
[1185.08 --> 1186.48]  But we're sort of unhappy with it.
[1186.58 --> 1188.44]  The developer that built it maybe has left.
[1188.74 --> 1192.68]  I was talking last week with a company that does over a billion in revenue each year.
[1192.80 --> 1197.00]  And their SKIM connection, the user provisioning, was written last summer by an intern.
[1197.14 --> 1198.90]  Who's no longer obviously at the company.
[1198.98 --> 1200.10]  And the thing doesn't really work.
[1200.10 --> 1201.72]  And so they're looking for a solution for that.
[1201.84 --> 1203.66]  So there's a really wide spectrum.
[1203.84 --> 1208.22]  We'll serve companies that are in a, you know, their office is in a coffee shop or their living room.
[1208.22 --> 1212.40]  All the way through they have a, you know, their own building in downtown San Francisco or New York or something.
[1212.70 --> 1213.64]  And it's the same platform.
[1213.86 --> 1216.12]  Same technology, same tools on both sides.
[1216.42 --> 1217.52]  The volume is obviously different.
[1217.68 --> 1221.62]  And sometimes the way we support them from a kind of customer support perspective is a little bit different.
[1221.94 --> 1222.60]  Their needs are different.
[1222.80 --> 1224.64]  But same technology, same platform.
[1224.92 --> 1225.98]  Just like AWS, right?
[1226.00 --> 1227.84]  You can use AWS and pay them $10 a month.
[1227.84 --> 1229.98]  You can also pay them $10 million a month.
[1230.30 --> 1230.78]  Same product.
[1230.90 --> 1231.86]  Or more, for sure.
[1231.90 --> 1232.22]  Or more.
[1233.02 --> 1238.98]  Well, no matter where you're at on your enterprise-ready journey, WorkOS has a solution for you.
[1239.32 --> 1245.08]  They're trusted by Perplexity, Copy.ai, Loom, Vercel, Indeed, and so many more.
[1245.50 --> 1249.10]  You can learn more and check them out at WorkOS.com.
[1249.10 --> 1252.32]  That's W-O-R-K-O-S dot com.
[1252.66 --> 1255.14]  Again, WorkOS dot com.
[1255.14 --> 1281.82]  Yeah, I know one of the things, and it's super interesting to me, but I think also it's unlocked a little bit in terms of what you've talked about in our meetings,
[1281.82 --> 1287.48]  is that there's a certain element of operational efficiencies that can be gained with these tools.
[1287.48 --> 1294.10]  If you look at a human process and think, you know, how could we use a Gen.AI tool?
[1294.54 --> 1299.42]  How could we use a language model to improve the efficiency of that process?
[1299.42 --> 1301.72]  So you have like five things in a sequence.
[1301.72 --> 1306.60]  How can it help me do two or three of those things faster or something like that?
[1307.00 --> 1315.52]  That's certainly true, but I love how you've talked a little bit about finding something upstream or going upstream of that to really think about,
[1315.52 --> 1323.36]  and maybe this is part of the thing that people are missing when they're trying to find the real value that AI unlocks in their organization,
[1323.36 --> 1332.02]  is that they have a set process in their mind and they could see, well, yeah, we could do this, you know, 10% faster,
[1332.02 --> 1338.54]  but is that worth the money that they're investing to an LLM system at a certain scale?
[1338.54 --> 1344.26]  So, yeah, could you help maybe talk us through that upstream value and how you think about honing in on that?
[1344.26 --> 1354.94]  The reality is that when you are solutioning, it is often a barrier for the client to visualize a solution
[1354.94 --> 1365.52]  because we tend to map sort of a biomorphic representation of the process onto the problem and the solution,
[1365.52 --> 1373.52]  and we're trying to imagine a robot doing a human's job, and just instantly you give it arms and legs and a head, right?
[1373.52 --> 1382.90]  And so it's like, for instance, you know, if I were to say, Daniel, how long do you think it'll be before robots replace cashiers at the grocery store?
[1382.96 --> 1384.26]  So we have Kroger in Cincinnati.
[1384.40 --> 1385.28]  So at Kroger, how long?
[1385.50 --> 1386.80]  And instantly, where's your mind go?
[1386.84 --> 1392.44]  It's kind of like, well, I'm just trying to imagine, you know, okay, the Tesla Optimist bot or one of these, you know,
[1392.44 --> 1399.34]  just trying to fumble around with your delicate groceries and not crushing it and scanning it,
[1399.34 --> 1405.84]  and it just seems so hard to think through and pull off, and you would just map that so far out into the future.
[1405.92 --> 1410.66]  And what you don't know is that my little brother, who works with the robots for Kroger,
[1411.22 --> 1413.92]  looked nothing like what is popped into your head.
[1413.92 --> 1418.88]  They're like these little square garbage can-looking things that run around on tracks,
[1419.06 --> 1422.28]  and it's like they really operate on the Z-axis.
[1422.64 --> 1425.70]  So it's like they're stacked on top of each other in these grid systems,
[1425.80 --> 1427.78]  and they're dropping products from one to another.
[1428.06 --> 1431.72]  And in the end, in the bottom, you know, a bag of someone's order comes out,
[1431.74 --> 1432.78]  and it loads right onto a truck.
[1432.86 --> 1433.84]  Human doesn't touch it.
[1434.96 --> 1440.86]  And this is an example of, you know, how it's just really hard when you're staring at a problem,
[1440.94 --> 1442.06]  trying to think of a solution.
[1442.06 --> 1445.42]  It's really hard to think way upstream.
[1446.16 --> 1448.98]  But the reality is the solutions tend to live up there.
[1449.56 --> 1451.38]  We start so late.
[1451.82 --> 1456.46]  We often start at letter Z when, like, we should be starting with, like, you know,
[1456.50 --> 1457.22]  what's an alphabet?
[1458.56 --> 1461.10]  And, yeah, why are we using an alphabet?
[1461.20 --> 1462.64]  Yeah, why are we using an alphabet?
[1462.74 --> 1464.56]  And I know that sounds like, oh, that sounds expensive.
[1464.70 --> 1466.02]  What are we going to be talking for days?
[1466.12 --> 1470.24]  Like, no, all I'm saying is, like, the example we used at lunch was, like,
[1470.24 --> 1475.24]  oh, I think that for a developer, you know, these co-pilot tools are handy
[1475.24 --> 1477.26]  because it can kind of double-check their code.
[1477.32 --> 1484.50]  Well, what I'm talking about is what if an organization had been mindful about tagging
[1484.50 --> 1489.94]  and consolidating all of the relevant context for the problem that the developer's been asked to solve.
[1489.94 --> 1497.04]  And it's programmatically, it's just automatically, you know, injected into the context of that co-pilot
[1497.04 --> 1499.38]  so that it's aware of the voice of the client.
[1499.74 --> 1501.74]  It's aware of the complaints online.
[1501.94 --> 1505.36]  I mean, I know this is far down the road, but this is probably going to be built for us pretty soon.
[1505.42 --> 1508.10]  I think it's a new paradigm of work, a new way of working.
[1508.20 --> 1509.48]  The way we work now is legacy.
[1509.48 --> 1515.48]  The new paradigm will be that way upstream of our work, way upstream of our work,
[1515.86 --> 1526.00]  special care has been put into collecting and curating and injecting the appropriate information
[1526.00 --> 1531.76]  into something like a language model or some more sophisticated, maybe multimodal version of that
[1531.76 --> 1534.96]  so that it can augment our workflow.
[1535.72 --> 1538.36]  And I only say that because it's how I work now.
[1538.36 --> 1540.84]  So I don't let anything go to waste.
[1540.96 --> 1542.88]  I mean, use, you know, use it all.
[1543.00 --> 1549.00]  Every scrap of communication, I like to transcribe if I can and make sure it exists in some sort of secure context
[1549.00 --> 1552.40]  so that it's just double checking my work and helping me ideate.
[1552.60 --> 1555.44]  And I find that like it's muscle memory for me now.
[1555.58 --> 1562.30]  But the time requirement to set that up pays off exponentially down the road when the client,
[1562.38 --> 1563.60]  and I need to reopen a case.
[1563.60 --> 1572.96]  And I've got this context that is fully locked in, completely aligned to the who, the what, the when, the where, the why of what we're being asked to do.
[1573.36 --> 1579.60]  And I just I'm really excited for a future where that's just handled for people, you know, who aren't weird like me.
[1579.60 --> 1583.28]  So and yeah, I guess that gets a little bit.
[1583.42 --> 1593.34]  I know one of your passions is thinking about how your work generally, but also the technology and other things impacts people at a at a human level.
[1593.34 --> 1598.66]  Right. And in particular, even vulnerable people or marginalized groups.
[1598.82 --> 1613.80]  And it's interesting for me to hear you talk about that, where a lot of times what people hear is, hey, how can we make this role more efficient so that maybe we have, you know, this focus workforce wise on efficiency?
[1614.76 --> 1617.14]  And, you know, how do we make this role more efficient?
[1617.14 --> 1621.66]  We're going to need less of these people, which is certainly a relevant thing that we need to talk about.
[1622.22 --> 1631.36]  But here, what you're talking about is more of a new paradigm where those people that are working are enabled to do actually net new things.
[1631.92 --> 1636.66]  And I also imagine maybe you could speak to this if you have an idea about it.
[1636.66 --> 1649.34]  But opportunities and things are unlocked for maybe people that are in vulnerable or marginalized situations that maybe could, you know, would be opportunities or things that they would have access to that they didn't before.
[1649.94 --> 1656.54]  And so this is maybe a different paradigm of looking at the workforce impact of AI, I guess.
[1657.22 --> 1658.80]  I love that you've asked me about this.
[1658.80 --> 1670.04]  I've had a few different like big light bulb moments when it comes to just thinking through imagining future products that might exist as a result of this brand new technology is brand new thing to people.
[1670.22 --> 1670.78]  Right.
[1670.92 --> 1683.32]  Like and I imagined once that there might be a vulnerable single mother sitting at home who maybe doesn't realize she's being exploited.
[1683.68 --> 1685.44]  I mean, I'm imagining a fictitious character.
[1685.44 --> 1693.20]  I don't know this person, but, you know, maybe there's a vulnerable single mother sitting who's being exploited and doesn't even know it.
[1693.98 --> 1698.42]  Can you imagine the cost of running these are trending towards zero?
[1698.54 --> 1699.26]  Like we see that.
[1699.34 --> 1699.54]  Right.
[1699.66 --> 1707.46]  So it's not hard to imagine a wearable that like ingests contexts and sort of helps someone navigate life.
[1707.58 --> 1710.34]  Maybe maybe might make them aware of their rights.
[1710.34 --> 1725.40]  Maybe might be willing to able to act agentically on their behalf by maybe filing a complaint somewhere or putting, you know, a situation where some marginalized person is underrepresented in a way.
[1725.40 --> 1744.98]  It excites me when I realize that a primary difference between the forgotten, the neglected, the marginalized, the primary difference between them and others is that the others generally just have someone willing and able to act on their behalf because it makes financial sense.
[1744.98 --> 1761.30]  When the cost of cognitive work and some of these automated or, you know, these agentic type actions are free or could even be ad supported because they're like, you know, one tenth of a penny, you know, to like for that type of help.
[1761.46 --> 1762.76]  That's exciting to me.
[1762.76 --> 1769.72]  And I do look forward to a future where people have access to advocacy, even though there's no real advocate.
[1770.28 --> 1771.98]  Yeah, that's so encouraging.
[1773.06 --> 1779.62]  Certainly, like I say, there's an element of workforce impact of AI that needs to be considered on the negative side.
[1779.80 --> 1787.72]  I guess if you want to consider it that way, but also there's a positive side and opportunities that are unlocked for sure.
[1787.88 --> 1792.54]  I have to say that tool will never exist if no one builds it, Daniel.
[1792.76 --> 1793.20]  Yeah.
[1793.42 --> 1795.90]  And so this is just a challenge.
[1795.90 --> 1808.44]  Like I'm doing this personally and we can unpack how, but like if you've been given gifts that overlap with like an expertise here, it's incumbent on each of us to think through like, how can I make the world just a smidge better?
[1808.44 --> 1808.70]  Right.
[1808.72 --> 1812.56]  Because I didn't just ignore all the need that overlaps with my expertise.
[1812.56 --> 1815.58]  And it's not just about writing a check at Christmas time.
[1816.22 --> 1817.16]  You know, yeah.
[1817.24 --> 1817.90]  Hunt that out.
[1817.90 --> 1833.78]  It's about, yeah, creating that outpost of goodness and beauty in what we create and not just like in your case and your background with art and actual sort of fine art, but also in the technologies and the products and the tools that we're building.
[1833.78 --> 1834.78]  I love that.
[1834.78 --> 1835.04]  I love that.
[1835.04 --> 1845.18]  I'd love to maybe talk, maybe just highlight a couple of these solution archetypes because I think this is also kind of helpful maybe for those in our audience.
[1845.18 --> 1858.60]  Maybe they're on the business side and they would connect with them, but also maybe they're on the technical side and they're just struggling to connect certain ways in which they can communicate the potential of this technology to stakeholders.
[1858.96 --> 1866.00]  So I love the one that you have here of generating new ideas with AI.
[1866.42 --> 1869.64]  How do you think about that as a solution archetype?
[1869.64 --> 1889.12]  Well, the obvious way to do this that anyone would just think of on their own is you could go to something like ChatGPT and say, go a step beyond what a normal sort of ho-hum user would do, which is to use it like Google, but to ask it for help with inspiration.
[1889.66 --> 1894.98]  And so anyone could just lean forward in their chair and open ChatGPT and do that right now.
[1894.98 --> 1905.34]  But the use case that we highlight in our solution archetypes documentation, there are two or three under that specific archetype.
[1905.40 --> 1909.72]  But the one that I'm most proud of and we'll talk about today is the first app I ever built.
[1910.28 --> 1912.56]  And this app was a persona named Andy.
[1913.02 --> 1918.42]  And so Andy is a roundtable discussion, like focus group style facilitator.
[1918.42 --> 1924.80]  So there's essentially it's really just a system command plus some tuned hyperparameters that help Andy do his job well.
[1925.20 --> 1932.66]  But Andy's supported in Python with the ability to synthesize or spawn new personas.
[1933.28 --> 1937.30]  And so what Andy will do is listen to the transcript of a meeting.
[1937.42 --> 1943.64]  What I would love if there was like a low enough latency audio, you know, like the files that OpenAI is kind of working on right now.
[1943.84 --> 1946.86]  I'd love to be able to get Andy like in the whole group participating in real time.
[1946.86 --> 1950.00]  But for right now, the way it works is you can kind of give him a chunk of transcript.
[1950.50 --> 1954.88]  And what Andy will do is kind of look at the problem you're trying to solve and spin up a focus group.
[1955.32 --> 1960.14]  So Andy creates, I think it was six or eight, I think maybe eight additional personas.
[1960.78 --> 1972.04]  So now all that means is in the Python code, there's like eight new things that Andy just created system messages and some hyperparameter tuning.
[1972.04 --> 1982.50]  So that now in the code, the tool has the functionality to summon any of these additional personas to weigh in on the conversation.
[1982.50 --> 1987.24]  And so Andy, as a facilitator, can pick which one has a turn to talk.
[1987.76 --> 1989.76]  And so then Andy opens the group.
[1990.02 --> 1991.92]  And you can use the world knowledge for this bit.
[1991.92 --> 1992.42]  And I did.
[1992.52 --> 1997.98]  And he just understood how to run a focus group, which actually is cool because I didn't know how to do that when I had the idea to do it.
[1998.34 --> 2004.76]  And so Andy will say, you know, like, okay, today we're going to talk about new product ideas for X industry.
[2004.98 --> 2007.78]  We happen to do this for the publishing company where I worked.
[2007.86 --> 2010.36]  So I was still working for them when I made this tool.
[2010.36 --> 2016.10]  And Andy could, I think it was like a fireman, a nurse, a web developer, a doctor, you know, around the table.
[2016.58 --> 2022.52]  And the problem this company had was their new product development team was struggling to come up with new products.
[2022.94 --> 2026.88]  And pretty much at the end of each meeting, it would just be the same product.
[2027.34 --> 2028.74]  And this was a problem.
[2029.30 --> 2034.34]  And so Andy understood my job is to think of new ideas.
[2034.88 --> 2037.68]  But then kick it to the group for discussion.
[2037.68 --> 2041.02]  And it was so fascinating to watch them talk about it.
[2041.34 --> 2051.38]  In this instance, the very first time we ever used it, someone in the group came up with an idea for something that was very close to the products that they had been making but a little different.
[2051.80 --> 2054.96]  And then the nurse piped up and said, that's great.
[2055.02 --> 2057.76]  But that form factor would not work at all for my job.
[2057.80 --> 2063.46]  And if I wanted to bring that to work and benefit from it, it would need to be smaller so they could fit in my pocket or purse.
[2063.70 --> 2067.62]  And so then someone else built on it and said, you're describing a deck of cards.
[2067.68 --> 2068.82]  And this could work.
[2069.04 --> 2073.08]  And then the web developer kicked in behind and said, that's a great idea.
[2073.22 --> 2077.38]  If there was a QR code on the cards, you could then link it to an account that they have.
[2077.72 --> 2079.76]  Here, let me write that right now.
[2080.02 --> 2081.58]  Of course, the code didn't fully work.
[2081.78 --> 2082.34]  But it was cool.
[2082.44 --> 2084.52]  You could see it try to write the code.
[2085.08 --> 2086.84]  And this, we were just letting it run.
[2087.10 --> 2087.30]  Right?
[2087.96 --> 2089.38]  They loved the idea.
[2089.46 --> 2095.28]  It was the freshest, best idea they'd had in the seven-year existence of the new product development team.
[2095.28 --> 2097.80]  It was a brand new product idea.
[2098.00 --> 2099.58]  And it was the first app I'd written.
[2099.72 --> 2101.56]  And it was the first time we ran it.
[2101.76 --> 2104.04]  And that, for me, was a major moment.
[2104.20 --> 2105.62]  And that was on GPT-3.
[2106.26 --> 2106.38]  Yeah.
[2106.54 --> 2122.96]  And there's an element to this solutioning that you've been doing that makes me think about how quickly you're able to get through to a proof of concept or demonstrating the value that you had in mind with a certain AI use case.
[2122.96 --> 2129.96]  And I'm wondering, as you're doing this solution, I'm guessing that there's a balance or maybe potential objections here.
[2130.08 --> 2143.44]  You know, in this scenario, I could see how a company might object to putting in so much product information or IP information into one of these systems for privacy reasons.
[2143.44 --> 2149.72]  Or maybe they're thinking, oh, what you're describing is going to take so many, so many LLM calls.
[2149.80 --> 2155.36]  It's going to be slow or maybe costly, which maybe are relevant concerns.
[2155.36 --> 2165.66]  But also, you kind of need to know what is possible before you get to some of that optimization and also try to get to an end-to-end solution.
[2165.66 --> 2188.10]  So how do you think about, as you're solutioning, balancing this desire to move quickly and get to a solution and end-to-end thing versus privacy, security types of concerns and balancing those things that maybe are optimizations or scale issues or environment issues with the ability to get to an end-to-end solution?
[2188.10 --> 2202.40]  Yeah. Sitting across the table from maybe the best person in the world at this, the best I've ever met, you know, when it comes to, like, thoughtfully considering, you know, security and the risks associated with it, I will say, like, this is not something to ignore.
[2202.60 --> 2203.04]  Like, ever.
[2203.04 --> 2210.12]  And we've learned to start with security when it comes to, like, forming relationships and assurances with a new client.
[2210.94 --> 2212.96]  And we need to be good at that, right?
[2213.78 --> 2219.00]  But you got to start somewhere.
[2219.70 --> 2223.68]  And sometimes what we do is we start with synthetic data.
[2224.12 --> 2232.54]  So it's kind of like, hey, pharma company, we're going to invent a synthetic drug and we're going to make all the synthetic assets that a company would have.
[2232.54 --> 2236.96]  And we're going to, you know, and what's neat about that is these tools do that for you.
[2237.02 --> 2241.80]  So, I mean, if you have a persona, remember I said, like, the new paradigm is having a persona fully aligned.
[2241.98 --> 2251.32]  Well, that persona that I've taken the time to get up to speed on the project can just spit out all this stuff I need to prove to them that what they want to do is possible, right?
[2251.74 --> 2255.80]  There are so many trust me's floating around in this space, right?
[2255.82 --> 2256.78]  Like, it can do it.
[2256.90 --> 2258.56]  We'll get you there in 36 months.
[2258.56 --> 2264.56]  You only need to pay us, you know, X million dollars to build out your – and it's BS.
[2265.52 --> 2275.10]  Maybe that works for a big co who has a metabolism that is the same as a, you know, a 20-ton whale.
[2275.10 --> 2283.18]  But, like, you know, for mid-co, mid-small that has a normal human metabolism and would like to see something before Christmas, right?
[2283.28 --> 2290.60]  Like, you know, there are ways to get to POC, proof of concept, in sometimes hours.
[2290.60 --> 2302.26]  I have had persuasive proof of concept scripts written before the end of meetings where the client is talking about a solution they want.
[2302.46 --> 2303.24]  And how do you do that?
[2303.28 --> 2306.46]  Because I probably went into the meeting with an aligned persona on the goals.
[2306.82 --> 2314.88]  I hear a few little things in the meeting and I have a bot that I've created called Persona Craft that I can just throw in a few things and, you know, bang, bang, bang.
[2314.88 --> 2316.24]  Oh, okay, throw that in Python.
[2317.16 --> 2318.62]  Is this what you're talking about?
[2318.74 --> 2319.86]  Like, holy smokes.
[2320.36 --> 2320.84]  So, yeah.
[2331.12 --> 2332.04]  What's up, friends?
[2332.30 --> 2333.94]  I've got something exciting to share with you today.
[2334.16 --> 2338.28]  A sleep technology that's pushing the boundaries of what's possible in our bedrooms.
[2338.74 --> 2343.56]  Let me introduce you to 8Sleep and their cutting-edge Pod 4 Ultra.
[2343.56 --> 2345.88]  I haven't gotten mine yet, but it's on its way.
[2346.22 --> 2347.68]  I'm literally counting the days.
[2348.16 --> 2350.70]  So, what exactly is the Pod 4 Ultra?
[2351.20 --> 2356.00]  Imagine a high-tech mattress cover that you can easily add to any bed.
[2356.18 --> 2357.74]  But this isn't just any cover.
[2358.06 --> 2361.54]  It is packed with sensors, heating, and cooling elements.
[2361.82 --> 2364.82]  And it's all controlled by sophisticated AI algorithms.
[2365.36 --> 2372.42]  It's like having a sleep lab, a smart thermostat, and a personal sleep coach all rolled into a single device.
[2372.42 --> 2382.58]  It uses a network of sensors to track a wide array of biometrics while you sleep, sleep stages, heart rate variability, respiratory rate, temperature, and more.
[2383.04 --> 2387.28]  It uses precision temperature control to regulate your body's sleep cycles.
[2387.74 --> 2395.52]  It can cool you down to a chilly 55 degrees Fahrenheit or warm you up to a good, nice solar temperature of 110 Fahrenheit.
[2395.52 --> 2399.54]  And it does this separately for each side of the bed.
[2399.88 --> 2403.64]  This means you and your partner can have your own ideal sleep temperatures.
[2404.18 --> 2412.70]  But the really cool part is that the Pod uses AI and it uses machine learning to learn your sleep patterns over time.
[2412.70 --> 2419.22]  And it uses this data to automatically adjust the temperature of your bed throughout the night according to your body's preferences.
[2419.56 --> 2424.70]  Instead of just giving you some stats, it understands them and it does something about it.
[2425.08 --> 2428.22]  Your bed literally gets smarter as you sleep over time.
[2428.62 --> 2432.36]  And all this functionality is accessible through a comprehensive mobile app.
[2432.58 --> 2437.62]  You get sleep analytics, trends over time, and you even get a daily sleep fitness score.
[2437.62 --> 2439.58]  Now, I don't have mine yet.
[2439.72 --> 2440.48]  It is on its way.
[2440.80 --> 2442.56]  Thanks to our friends over at 8sleep.
[2442.96 --> 2445.94]  And I'm literally counting the days I get it because I love this stuff.
[2446.34 --> 2459.72]  But if you're ready to take your sleep and your recovery to the next level, head over to 8sleep.com slash practical AI and use our code practical AI to get 350 bucks off your very own Pod 4 Ultra.
[2460.16 --> 2462.20]  And you can try it free for 30 days.
[2462.46 --> 2465.78]  I don't think you want to send it back, but you can if you want to.
[2465.78 --> 2471.06]  They're currently shipping to the US, Canada, United Kingdom, Europe, and Australia.
[2471.48 --> 2475.00]  Again, 8sleep.com slash practical AI.
[2475.00 --> 2504.44]  Yeah, certainly there's an element of this where you are acting as an architect and a solution developer getting to that proof of concept showing value.
[2504.44 --> 2519.30]  But I know one of the other things that you're particularly passionate about and have been exploring is actually finding kind of individuals in organizations that are champions or could be champions of AI.
[2519.58 --> 2522.82]  Maybe they're not from a kind of technical programming background.
[2522.82 --> 2523.82]  Maybe they are.
[2523.82 --> 2533.02]  But kind of teaching them how to utilize these tools effectively in a sort of crash course kind of way.
[2533.16 --> 2534.94]  So how do you think about that?
[2534.98 --> 2541.60]  And what are some of the things that you're taking people through to help them understand how to use these tools in an effective way?
[2541.60 --> 2549.98]  I just want to preface this bit by saying I am trying to become a master at what I'm about to describe and I'm not there yet.
[2550.12 --> 2553.62]  This has been the hardest thing for me to navigate so far.
[2553.72 --> 2554.40]  Here's the reality.
[2555.42 --> 2557.72]  Companies need more than code.
[2558.44 --> 2569.52]  Like what they really – whether or not they realize it, when they tell me we want to become AI enabled, I think some part of it is they want their people to know and understand this stuff.
[2569.52 --> 2584.72]  And I think if you just kind of trust it to luck that people who have a really demanding job are going to develop an accurate sense for what's going on under the hood, you're going to be disappointed.
[2585.78 --> 2594.54]  And so we have developed – the company that bought my small business happened to be a change management, like an instructional design company.
[2594.54 --> 2600.58]  That they have helped BigCo for decades navigate massive change.
[2601.18 --> 2602.22]  And so it's just kind of lucky.
[2602.62 --> 2605.34]  I mean that's actually part of why I liked the offer.
[2605.58 --> 2614.16]  But I have worked with their experts to develop a pretty well-defined approach with mixed results.
[2614.70 --> 2623.30]  Where I want to get better is I want to get better at identifying the people who are really going to become the super user rock stars.
[2623.30 --> 2628.14]  So we've developed this tool called a fit checker that like essentially is a quiz.
[2628.38 --> 2629.48]  It's like some sliders.
[2629.66 --> 2631.64]  They slide and it helps us kind of score.
[2632.36 --> 2635.12]  I don't even really know if that's going to work great or not.
[2635.38 --> 2642.70]  But what we are doing is letting them get a peek under the hood at what's going on with these tools.
[2642.78 --> 2645.04]  Because we want to demystify it, right?
[2645.42 --> 2649.60]  But they think it's magic or BS or both.
[2649.60 --> 2656.94]  Can I just kind of run you through the beginning of like what it would be like in one of our early sessions with them?
[2657.06 --> 2657.70]  So you can see – okay.
[2658.16 --> 2664.50]  So – and feel free to try this in your organization if you're kind of trying to align with someone on like what's actually happening with these tools.
[2664.64 --> 2670.60]  And so what we'll do in the very beginning is I'll stand in front of the room or one of our other coaches will stand in front of the room and say,
[2670.60 --> 2677.14]  hey, everybody, I'm going to say something and I'm going to say a few words and what I want you to do –
[2677.14 --> 2681.16]  and you can maybe even do this like in your car or like if you're listening to this at home.
[2681.28 --> 2683.68]  Just blurt out what pops in your mind, right?
[2683.76 --> 2687.16]  And so I'm going to say some words and then you're going to blurt out what pops in your mind.
[2687.22 --> 2687.58]  Are you ready?
[2687.72 --> 2688.02]  Ready.
[2688.14 --> 2688.56]  Here we go.
[2689.16 --> 2689.94]  Peanut butter and?
[2690.58 --> 2690.86]  Jelly.
[2691.00 --> 2691.24]  Jelly.
[2691.38 --> 2692.68]  It's jelly every time.
[2692.90 --> 2693.04]  Yeah.
[2693.16 --> 2694.34]  It's always jelly.
[2694.88 --> 2696.26]  And the whole room says jelly.
[2696.40 --> 2699.14]  No one says anything except jelly, right?
[2699.14 --> 2705.64]  And then what we do is we explain to them that they essentially provided a completion to our prompt.
[2706.42 --> 2707.64]  And jelly happens to be a token.
[2708.36 --> 2712.38]  And peanut butter – peanut is if it's a capital P is three tokens.
[2712.96 --> 2715.52]  Butter is a token and is a token.
[2715.56 --> 2716.86]  That's the GPT-4 tokenizer.
[2717.54 --> 2721.38]  And so then we can open up a tokenizer and we can show them those individual tokens.
[2721.50 --> 2724.52]  And we can click on the token IDs and we can show them that those are just numbers.
[2724.52 --> 2735.74]  And that there's this language model that is trained to spot weird patterns to what tends to come next as a number when you give it a string of numbers.
[2735.92 --> 2738.44]  Those were converted to bits or entire words.
[2738.94 --> 2740.98]  And then it just spit back jelly.
[2740.98 --> 2752.34]  And so when you understand that – and then we show them, we tell them like – and look, if it spits a sentence back, it's just kind of a token, token, getting longer, getting longer, getting longer, you know, and it's starting from the beginning.
[2752.80 --> 2756.46]  And they get a sense for the like, oh, it's just mimicking language.
[2757.12 --> 2763.10]  It's mimicking what a next word that a human might say when they heard a thing.
[2763.10 --> 2767.76]  When you understand that it's working that way, it helps you use it better.
[2768.58 --> 2768.76]  Okay.
[2769.46 --> 2778.80]  So then while I'm talking about all that, I might start talking about blues and rock and roll.
[2779.16 --> 2780.86]  I might mention Memphis.
[2781.88 --> 2782.40]  Cadillacs.
[2783.38 --> 2785.50]  Maybe I'll say something about Graceland.
[2786.00 --> 2787.28]  And I'm talking about all this.
[2787.68 --> 2789.12]  And then I'll say, let's try it again.
[2789.86 --> 2791.52]  Peanut butter and – and it's like jelly jelly.
[2791.52 --> 2797.44]  Someone yells banana and behind me on the board, I take a thing off and we've written banana on the board, right?
[2798.12 --> 2804.98]  And then we just have this weird moment because some people in the room are young and they don't even hardly know who Elvis is, right?
[2805.16 --> 2807.52]  And I don't even know if you would have gotten that, Daniel.
[2807.98 --> 2808.68]  Yeah, yeah.
[2808.72 --> 2812.84]  I definitely would have gotten the Elvis, Graceland, et cetera.
[2813.22 --> 2815.48]  But I would have been somewhere there.
[2815.48 --> 2821.58]  Yeah, and so I think it's that – Elvis, like peanut butter and banana sandwiches or something.
[2821.58 --> 2837.66]  And so now we can just unpack the concept of context because by inserting some new ideas, we sort of shifted the probability of that index of potential tokens that – you know, the order that they would be.
[2837.66 --> 2845.18]  And we've shifted it enough so that banana could potentially show up as worth picking.
[2845.74 --> 2847.00]  And someone did.
[2847.64 --> 2852.28]  And that just sort of demonstrates, well, most of you still said jelly, but someone said banana.
[2852.38 --> 2854.24]  I'm just telling you it has never not worked.
[2854.36 --> 2855.20]  Like it always works.
[2855.94 --> 2858.42]  And so then we start talking about, okay, so these are tokens.
[2858.56 --> 2859.24]  They're parts of words.
[2859.30 --> 2859.78]  They're numbers.
[2860.00 --> 2860.92]  They go together.
[2861.06 --> 2864.64]  It can predict the next one to mimic human communication or thought.
[2864.64 --> 2872.62]  And then there's only a certain amount of these that can fit in its brain or its memory, its context window.
[2873.08 --> 2874.24]  And we'll show them on a board.
[2874.34 --> 2877.46]  We just put little hashes for like this is a token, this is a token, this is a token.
[2877.46 --> 2878.70]  Well, what happens when we get to the end?
[2878.72 --> 2882.54]  Because, Daniel, when I started working with these tools, we only had 2,000 to work with.
[2882.74 --> 2884.90]  And now it feels infinite, but not really.
[2885.36 --> 2892.56]  But because you learn early, right, because you learn early, you learn to work within the limitations of the tool and you learn elegant workflow then, right?
[2892.56 --> 2898.18]  Because we appreciate even though it feels big, it's still scarce because they got to pay for what we submit.
[2898.50 --> 2901.92]  And so we show them these are how the tokens stack up.
[2902.14 --> 2907.42]  And then we show them like when you start getting toward the end, if we fill up this 2,000, what's it going to do?
[2907.70 --> 2909.74]  It's chopping off the ones in the beginning.
[2910.36 --> 2915.14]  And then we ask them like have you ever had an experience with chat GPT where it feels like I've already told you that.
[2915.70 --> 2916.58]  Oh, yeah, you see some.
[2916.78 --> 2919.14]  Oh, oh, because it didn't forget it.
[2919.18 --> 2922.38]  It's selectively it deleted it, you know.
[2923.00 --> 2927.84]  And so we just run them through, you know, that's like the first 10 minutes.
[2928.32 --> 2934.22]  And we just build on that and build on that and build on that so that they build good AI usage habits.
[2934.22 --> 2943.54]  And they can interact with the tool in a way that leverages the strength of the tool and with an awareness of what can go wrong.
[2943.54 --> 2944.90]  Yeah, I love this approach.
[2944.90 --> 2961.40]  And in my own workshops, when I start going through some of this of how a generation actually happens, how text is generated, I often see that a number of really important and interesting questions kind of naturally pop out out of that.
[2961.40 --> 2967.72]  Like, hey, if this is just producing these tokens in this way, how could it produce anything meaningful?
[2968.14 --> 2969.90]  And how does it seem so coherent?
[2970.20 --> 2971.90]  Like there's an intent behind it.
[2972.00 --> 2977.58]  Why would it produce anything actually valuable and connected to the to the real world?
[2977.58 --> 2979.76]  So, yeah, I love this.
[2979.76 --> 2988.82]  So because we get all those same questions, we have identified what we call layer one, layer two and layer three knowledge.
[2988.98 --> 2992.22]  We only teach layer one knowledge in our boot camp.
[2992.22 --> 2996.66]  We will address layer two and layer three questions individually, but not as a group.
[2997.12 --> 3004.10]  Because the layer one knowledge is the strict information set that is required to use the tool well.
[3004.58 --> 3008.68]  And so we would never talk about prompt injection attack in the group setting.
[3008.84 --> 3012.68]  Because what we don't want to do is scare off the non-technical person.
[3013.64 --> 3016.56]  And in fact, we target the non-technical people.
[3016.66 --> 3017.82]  This is their moment.
[3018.42 --> 3021.34]  Like, do you finally program computers with plain language, you know?
[3021.34 --> 3022.82]  Yeah, really good points.
[3023.08 --> 3032.46]  And on the data side, I think one of the interesting things is, like you say, not going into some of those details in that context,
[3032.46 --> 3041.90]  but definitely getting to a point where people can realize how data starts to become integrated with these AI systems in a meaningful way.
[3042.38 --> 3046.04]  An example I often give is, you know, I go into a chat interface.
[3046.30 --> 3048.58]  I say, summarize this email for me.
[3048.58 --> 3050.66]  And of course, you haven't pasted in an email.
[3050.66 --> 3055.22]  The model doesn't know how to summarize an email that it's not given, right?
[3055.28 --> 3056.62]  But everyone knows what to do.
[3056.78 --> 3065.54]  They could paste in the email that they want summarized and, you know, ignoring the kind of policy, potentially policy-related things around that.
[3066.14 --> 3072.64]  It immediately makes sense that people can bring the right data to the table, inject it into these existing models,
[3072.64 --> 3077.24]  without having to do complicated fine-tuning and actually produce value.
[3077.24 --> 3081.10]  Can I tell you our five-step process to effective reasoning?
[3081.36 --> 3083.54]  So we have a slide on this and we teach it.
[3083.70 --> 3087.46]  I think, I hope I can remember all five because I just told you there's five.
[3088.10 --> 3093.40]  What we teach when it comes to, like, reasoning over data or just processing information,
[3093.40 --> 3095.20]  it could really be almost any project.
[3095.40 --> 3096.88]  We teach to do it in this order.
[3096.88 --> 3102.28]  So we say what we like to do is teach them to start with end-goal alignment.
[3103.08 --> 3116.34]  And so because we know that, I think it's known, that these models tend to pay a little more attention to what's going on early and late in your context,
[3116.34 --> 3119.80]  we want to get the real end goal articulated very early.
[3119.80 --> 3124.84]  So a neat trick I have for end goal, and so this actually can be fun.
[3124.92 --> 3126.56]  So this is a way you can work from your hot tub.
[3128.14 --> 3130.12]  Maybe you should open this show with that clip.
[3132.50 --> 3134.24]  So this is a way you can work from your hot tub.
[3134.72 --> 3141.74]  I like to put in my AirPods and hit record on my phone and just talk about what I need to get done on this project.
[3141.74 --> 3143.04]  Just talk, talk, talk, talk, talk.
[3143.50 --> 3144.22]  Get it out.
[3144.66 --> 3146.96]  This way I don't have to sit in front of my computer at my desk.
[3146.96 --> 3156.26]  So I might go on a walk or on a treadmill and just talk through this is the who, the what, the when, the where, the why, right, and get it all out there.
[3156.42 --> 3156.66]  Okay.
[3156.92 --> 3159.94]  Now, what we do is we transcribe that.
[3160.34 --> 3161.16]  I use Mac Whisper.
[3161.26 --> 3162.16]  So I'm doing that locally.
[3162.16 --> 3165.36]  So it doesn't matter if this is something for a top secret project.
[3165.50 --> 3167.10]  I can transcribe that locally.
[3167.56 --> 3172.12]  And then I can inject that into essentially my first prompt.
[3172.20 --> 3172.92]  And it might be big.
[3172.92 --> 3178.40]  I've had those go on for three hours or as quick as 10 seconds.
[3179.48 --> 3182.36]  And what we tend to do is try to rush to work.
[3182.46 --> 3185.36]  But there's a bunch of steps before we start working.
[3185.86 --> 3188.42]  So step one is establishing the end goal.
[3189.24 --> 3192.96]  Step two would be to validate the end goal.
[3193.38 --> 3199.00]  So now we can go back to that same model and say, tell me what you think we're going to do.
[3199.00 --> 3201.44]  Like, just lay it all out.
[3201.52 --> 3202.74]  Give me bullet points, you know.
[3202.98 --> 3207.74]  And so it will go through and say, I'm expecting you to do this and you to do this.
[3207.76 --> 3209.80]  And then I'm going to do this and we're going to do this.
[3209.82 --> 3211.18]  And what the client wants is this.
[3211.24 --> 3212.98]  And so we're probably going to do that.
[3213.04 --> 3218.36]  And, you know, and you can look at it and go, actually, this or that is wrong.
[3218.36 --> 3224.80]  Now, what I like to do instead of playing AI whack-a-mole at this point, right?
[3224.90 --> 3235.34]  So anyway, AI nerd knows exactly what I'm talking about is I use this next, these next few bits of conversation to identify where it misunderstands the end goal, if it does at all.
[3235.70 --> 3239.88]  And then what I do is I go back to my source material and I modify my source material to clarify.
[3240.70 --> 3244.00]  And so what we do is we get rid of all those subsequent prompts for validation.
[3244.20 --> 3245.18]  Validation is for me.
[3245.28 --> 3247.44]  It's not anything that needs to linger in the context.
[3247.44 --> 3249.02]  So I delete all that.
[3249.60 --> 3252.10]  So step two was validation of end goal alignment.
[3252.30 --> 3260.12]  Step three is we curate and ingest our assets, our, like you said, the email.
[3260.46 --> 3262.56]  Remember I said curate, and that is big.
[3262.94 --> 3264.98]  You don't always have to do it, but it's helpful.
[3265.54 --> 3267.74]  Remember I said I learned on 2,000 tokens?
[3268.18 --> 3272.66]  This is why I make a habit of curating my content before I put it in there.
[3273.04 --> 3273.58]  What's the least?
[3273.68 --> 3275.10]  Now, there's a balancing act here.
[3275.16 --> 3276.48]  There's a trade-off, cost-benefit.
[3276.48 --> 3278.24]  You don't want to overdo this step.
[3278.30 --> 3281.98]  But it is helpful to trim the fat out of transcripts.
[3282.10 --> 3289.62]  You know, if you've got a transcript saved as VTTs and you look at and you open that up in Notepad, 80% of the tokens are time code.
[3290.14 --> 3294.14]  So, you know, maybe we get a doc X that just has speaker names.
[3294.14 --> 3301.06]  And, you know, so we're just mindful of, like, what are we throwing in next that isn't going to distract the model that's relevant?
[3301.26 --> 3303.36]  Okay, let's pretend like we've done all that work.
[3303.72 --> 3304.52]  What do we do now?
[3304.60 --> 3305.28]  Do we start working?
[3305.52 --> 3305.82]  No.
[3306.12 --> 3307.58]  We validate again.
[3307.58 --> 3311.98]  So we go back and we say, what do you understand that I just gave you?
[3312.02 --> 3315.22]  And how do you understand that it relates to our end goal?
[3315.74 --> 3316.82]  And we'll talk about it.
[3316.88 --> 3321.76]  Usually this part, it gets right if we've done a good job of end goal alignment and curation.
[3321.76 --> 3326.44]  But sometimes you'll spot, oh, it can't see the infographics.
[3326.62 --> 3334.94]  I assumed by attaching these PDFs that, okay, what color is the biggest slice on page 14 of the pie chart?
[3335.12 --> 3338.14]  That's what a validation thing might look like over your data, right?
[3338.58 --> 3340.38]  Okay, you can see that pie chart.
[3340.46 --> 3341.36]  Okay, you see the orange.
[3341.44 --> 3342.44]  Okay, you know what that is.
[3342.48 --> 3343.64]  How does that relate to our project?
[3343.76 --> 3344.38]  Okay, you understand.
[3344.50 --> 3346.14]  Okay, you validate all that.
[3346.20 --> 3347.10]  Now get rid of that.
[3347.48 --> 3348.90]  Because that doesn't need to persist.
[3348.90 --> 3350.30]  But I need to be comfortable.
[3350.44 --> 3352.62]  This model understands the goal.
[3352.84 --> 3353.84]  So it's aligned.
[3354.42 --> 3356.64]  Now it's finally time to start work.
[3357.46 --> 3358.34]  We've done all this work.
[3358.46 --> 3361.74]  And boy, can you burn through a project when you've done those steps?
[3362.30 --> 3367.34]  And it's just, this is the fun part, really, where we just start, okay.
[3367.50 --> 3369.86]  You can almost just say, okay, go at this point.
[3369.90 --> 3371.42]  And it starts to do the work.
[3371.52 --> 3374.70]  And then I think the fifth step, I haven't been numbering them on purpose.
[3375.14 --> 3378.18]  The fifth step is just letting it synthesize assets.
[3378.18 --> 3382.60]  And this can not only be like, if you're using ChatGPT, you can have it create spreadsheets
[3382.60 --> 3383.06]  or whatever.
[3383.24 --> 3389.18]  But you can also, if it understands, hey, I want to use Udeo to make a song about that.
[3389.20 --> 3392.82]  Or I want to use Ideogram 2 to like create slides for that.
[3392.86 --> 3396.98]  Or I want to use, and you can just have it start to create prompts for other things and
[3396.98 --> 3397.74]  go off and do it.
[3397.80 --> 3398.68]  And it's really fun.
[3398.82 --> 3400.20]  Now, so we've done all that.
[3400.24 --> 3402.02]  And we've got that context persistent.
[3402.38 --> 3405.92]  The client sends us an email and complains about whatever.
[3405.92 --> 3406.56]  What do we do?
[3406.76 --> 3408.24]  Copy, paste, boom, done.
[3408.38 --> 3408.54]  Right?
[3408.68 --> 3410.18]  Like, it's just so little work.
[3410.34 --> 3410.38]  Yeah.
[3410.44 --> 3411.40]  That's super encouraging.
[3411.64 --> 3417.12]  I love this example because, you know, oftentimes you might be, you know, I might be in a meeting
[3417.12 --> 3419.90]  and you have to respond very quickly.
[3419.90 --> 3425.80]  But a lot of times it's those slow times where you're able to think about something for me,
[3425.94 --> 3432.32]  like on a walk around the block or, you know, on a hike or something like that, where I'm
[3432.32 --> 3438.00]  really, you know, present and I'm maybe more calm and thinking through things in a slower
[3438.00 --> 3438.54]  fashion.
[3438.54 --> 3441.44]  But I also want to capture that and I want to summarize it.
[3441.52 --> 3445.42]  I want to bring it into conversations in the midst of my workday.
[3445.42 --> 3447.10]  So I love that example.
[3447.28 --> 3451.82]  And I think it also illustrates how you've integrated this technology.
[3452.22 --> 3456.18]  You're practicing what you preach to some degree, kind of integrating this technology
[3456.18 --> 3457.58]  into your daily rhythms.
[3457.58 --> 3465.52]  And that brings me to maybe a last question here as we're starting to wrap up is, as you
[3465.52 --> 3470.56]  look to the future and you're thinking about the new solutions that you're creating for
[3470.56 --> 3474.40]  people, the things that are on your mind, the things that you're architecting, what's
[3474.40 --> 3475.82]  most exciting for you now?
[3475.92 --> 3477.24]  What are you excited to explore?
[3477.38 --> 3482.78]  What are you excited to kind of prototype with the partners and the customers that you're
[3482.78 --> 3483.30]  working with?
[3483.40 --> 3485.06]  What excites you looking forward?
[3485.06 --> 3490.14]  Well, I will stand by what I said initially, that if we never got another innovation, these
[3490.14 --> 3497.46]  tools are good enough as they are to justify going down on the timeline of humanity as a
[3497.46 --> 3499.76]  massive technological revolution.
[3500.44 --> 3506.18]  And the tools that I wish for that are already sort of like they're almost done baking, right?
[3506.34 --> 3513.94]  The tools that I wish for are really low latency, in and out, audio, video, image agents.
[3513.94 --> 3518.44]  And so, you know, I've built so many tools that interact with people.
[3518.92 --> 3522.46]  We call it one class is called like mind mappers, where we're essentially trying to convert
[3522.46 --> 3526.02]  tacit knowledge to documented process, right?
[3526.10 --> 3529.32]  And so like, you know, you've got the single point of failure person in your organization.
[3529.68 --> 3532.48]  How do you map out like their subject matter expertise?
[3532.48 --> 3539.12]  So what would be awesome is if there was a low latency conversant model.
[3539.28 --> 3545.30]  So like what OpenAI kind of has, but it's walled off right now, like an API where I could give
[3545.30 --> 3550.46]  a person an option between an email chain, text messages, a phone call.
[3550.80 --> 3552.82]  And right now I can't do the phone call.
[3552.82 --> 3554.40]  And that bothers me.
[3554.90 --> 3561.42]  And then I think too, just as people start to see the value of the tools that maybe they're
[3561.42 --> 3568.24]  a little less weirded out and fearful of interacting with them.
[3568.68 --> 3572.58]  And so of course, it makes sense that people feel nervous that they're going to lose their
[3572.58 --> 3572.86]  job.
[3572.94 --> 3578.10]  The reality is they are going to lose their job as it exists today.
[3578.10 --> 3585.36]  If there's knowledge work, they should, because that's like continuing to want to farm land
[3585.36 --> 3591.28]  with an ox and whatever the thing behind a plow, I guess, like, you know, like that's wishing
[3591.28 --> 3597.26]  for keeping that, you know, when the tractor dealership just showed up and like, no, we,
[3597.42 --> 3603.20]  we're not going to want to go back to like, you know, the days of like trudging through tedious,
[3603.20 --> 3605.74]  you know, knowledge work that could be automated.
[3605.74 --> 3613.32]  Um, but it is going to be a process that requires empathy on the part of us, the AI engineers,
[3613.44 --> 3618.42]  the architects, the developers, the, you know, the leaders, and to appreciate like, this is
[3618.42 --> 3619.34]  a scary thing.
[3619.56 --> 3624.98]  And so another thing I wish for is just to get past this adolescent phase to where the
[3624.98 --> 3626.92]  tools feel, um, less scary.
[3627.24 --> 3634.54]  And then I, I got to go back to like, I am very excited to see what it means for learners
[3634.54 --> 3639.72]  who maybe their teachers don't have time to go on every curiosity journey with them or
[3639.72 --> 3642.38]  explain, you know, every little lesson.
[3642.88 --> 3645.30]  Uh, and so that's really big.
[3645.36 --> 3647.98]  I could give you such a long list, so I'll just stop there.
[3648.36 --> 3655.08]  I am very excited for how this technology, um, uh, develops, but I will say the good guys
[3655.08 --> 3656.70]  have to have hand on the wheel here, Daniel.
[3656.70 --> 3661.58]  And, you know, if you leave it up to big co, um, we won't have the stuff that really makes
[3661.58 --> 3663.60]  life better for a wide range of people.
[3664.04 --> 3664.10]  Yeah.
[3664.14 --> 3666.72]  Well, I think that's a great note to end on.
[3666.88 --> 3667.60]  Thank you.
[3667.76 --> 3670.08]  Thank you, Mike, so much for, for joining.
[3670.08 --> 3675.22]  And I would definitely encourage you to heed, uh, Mike's, Mike's call, get, get your hands
[3675.22 --> 3675.52]  dirty.
[3675.66 --> 3681.42]  Think about those solutions that are going to create goodness and create new, new paradigms
[3681.42 --> 3682.88]  of, of the way that we work.
[3682.88 --> 3685.20]  So yeah, thank you so much, Mike, for joining.
[3685.50 --> 3685.62]  Yeah.
[3685.80 --> 3686.96]  Uh, thank you.
[3694.08 --> 3695.08]  All right.
[3695.38 --> 3697.78]  That is practical AI for this week.
[3698.40 --> 3699.62]  Subscribe now.
[3699.62 --> 3707.00]  If you haven't already head to practical AI.fm for all the ways and join our free Slack team
[3707.00 --> 3711.20]  where you can hang out with Daniel, Chris, and the entire change log community.
[3711.20 --> 3716.40]  Sign up today at practical AI.fm slash community.
[3717.00 --> 3722.74]  Thanks again to our partners at fly.io to our beat freaking residents, break master cylinder,
[3722.74 --> 3723.92]  and to you for listening.
[3724.20 --> 3726.08]  We appreciate you spending time with us.
[3726.38 --> 3727.58]  That's all for now.
[3727.82 --> 3729.50]  We'll talk to you again next time.
[3729.50 --> 3729.54]  Okay.
[3729.62 --> 3731.90]  Bye-bye.
[3734.90 --> 3735.10]  God.
[3735.30 --> 3737.24]  Bye-bye.
[3737.30 --> 3737.76]  Bye.
[3744.00 --> 3744.18]  Bye-bye.
[3751.66 --> 3752.00]  Bye-bye.
[3752.12 --> 3752.50]  Bye-bye.
[3752.64 --> 3752.68]  Bye-bye.
[3752.68 --> 3753.18]  Bye-bye.
[3753.30 --> 3753.56]  Bye-bye.
[3753.56 --> 3753.86]  Bye-bye.
[3753.90 --> 3754.52]  Bye-bye.
[3754.52 --> 3754.62]  Bye-bye.
[3754.64 --> 3754.84]  Bye-bye.
[3754.84 --> 3755.14]  Bye-bye.
[3755.24 --> 3756.26]  Bye-bye.
[3756.32 --> 3756.92]  Bye-bye.
[3756.98 --> 3757.60]  Bye-bye.
[3757.60 --> 3757.76]  Bye-bye.
[3757.76 --> 3758.76]  Bye-bye.
