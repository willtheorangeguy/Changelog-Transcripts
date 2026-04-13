[0.00 --> 13.90]  Welcome, friends. On this episode, Adam and I are joined by Lee Robinson to talk about his journey in developer relations.
[14.64 --> 24.60]  We discuss what it means to be a DevRel, what orgs they fall under, how he runs his team at Vercel, Lee's three pillars of DevRel, education, community, and product.
[24.60 --> 29.70]  We compare the old days to now, and of course, what makes a DevRel a good DevRel.
[30.40 --> 31.64]  Whew, that's a whole lot of DevRel.
[32.16 --> 38.30]  Special thanks to our partners at Fastly for shipping our shows super fast to wherever you listen.
[38.68 --> 40.62]  Check them out at Fastly.com.
[41.04 --> 43.88]  Okay, Lee Rob on the changelog. Let's go.
[51.56 --> 54.58]  This episode is brought to you by our friends at Square.
[54.84 --> 56.90]  Square is the platform that sellers trust.
[56.90 --> 64.22]  There is a massive opportunity for developers to support Square sellers by building apps for today's business needs.
[64.64 --> 67.38]  And I'm here with Shannon Skipper, head of developer relations at Square.
[67.74 --> 71.80]  Shannon, can you share some details about the opportunity for developers on the Square platform?
[72.10 --> 72.48]  Absolutely.
[72.48 --> 75.44]  So we have millions of sellers who have unique needs.
[75.74 --> 78.82]  And Square has apps like our point of sale app, like our restaurants app.
[78.94 --> 85.20]  But there are so many different sellers, tuxedo shops, florists, who need specific solutions for their domain.
[85.46 --> 96.54]  And so we have a Node SDK written in TypeScript that allows you to access all of the backend APIs and SDKs that we use to power the billions of transactions that we do annually.
[96.54 --> 101.12]  And so there's this massive market of sellers who need help from developers.
[101.66 --> 112.52]  They either need a bespoke solution built for themselves on their own Node stack, where they are working with Square dashboard, working with Square hardware, or with the e-com, you know, what you see is what you get builder.
[112.78 --> 113.80]  And they need one more thing.
[113.88 --> 115.16]  They need an additional build.
[115.46 --> 119.44]  And then finally, we have that marketplace where you can make a Node app and then distribute it.
[119.44 --> 123.56]  So it can get in front of millions of sellers and be an option for them to adopt.
[124.08 --> 124.32]  Very cool.
[124.40 --> 124.64]  All right.
[124.66 --> 132.44]  If you want to learn more, head to developer.squareup.com to dive into the docs, APIs, SDKs, and to create your Square developer account.
[132.74 --> 134.50]  Start developing on the platform, Sellers Trust.
[134.96 --> 137.20]  Again, that's developer.squareup.com.
[149.44 --> 163.40]  All right.
[163.46 --> 165.92]  We have Lee Robinson here from Next.
[166.00 --> 167.06]  JS from Vercel.
[167.40 --> 167.62]  Hey.
[167.94 --> 168.56]  What's up, Lee?
[169.08 --> 169.48]  Hey.
[169.84 --> 170.62]  Thanks for having me.
[170.66 --> 173.36]  I'm really excited to come on and chat.
[173.94 --> 174.90]  We're excited to have you.
[174.90 --> 179.44]  Now, I only ever have known you online as Lee Rob, which is like a bunch of E's.
[179.88 --> 184.74]  And I'm curious if Lee Rob is like your, just your online handle or has it trickled into the real world?
[185.10 --> 185.36]  Yeah.
[186.34 --> 188.06]  It's really funny.
[188.14 --> 192.88]  The first time I heard someone call me Lee Rob in real life was kind of funny.
[193.10 --> 197.42]  It's the breakdown of your online persona to your real persona actually happened.
[197.70 --> 202.08]  But the context there is, you know, my name's Lee Robinson.
[202.08 --> 205.34]  Lee Rob's the combination of first and last name.
[205.54 --> 209.98]  Tried to find some kind of online handle that was unique.
[210.10 --> 212.82]  And it also related back to the domain name I was trying to grab.
[212.96 --> 214.30]  So I have LeeRob.io.
[215.30 --> 217.94]  And yeah, so people, my friends call me Lee.
[218.32 --> 220.06]  My coworkers all call me Lee Rob.
[220.26 --> 221.16]  But I really don't.
[221.52 --> 222.46]  It doesn't matter to me.
[222.52 --> 223.00]  It doesn't matter.
[223.62 --> 225.70]  So Adam, do people call you Adam Stack?
[226.76 --> 228.50]  I think there's a few.
[228.64 --> 228.88]  Yeah.
[229.24 --> 230.70]  I think I've called you that before, probably.
[230.70 --> 230.98]  Yeah.
[231.34 --> 233.52]  They don't often call me Adam Stack.
[233.60 --> 234.96]  They'll call me like Stack.
[235.08 --> 235.80]  Something with Stack.
[235.94 --> 238.10]  Like my nickname will either be Stack or Stacks.
[238.50 --> 240.08]  Like in the military, it was Stacks.
[240.52 --> 241.92]  Does anybody call you Daddy Fat Stacks?
[242.96 --> 243.32]  No.
[244.10 --> 245.22]  I might like that though.
[245.30 --> 246.74]  That's kind of a cool nickname, I think.
[246.76 --> 247.52]  Daddy Fat Stacks.
[247.68 --> 248.68]  I might start calling you that.
[249.12 --> 250.50]  Does that mean I got mad money or what?
[250.92 --> 251.64]  That's the hope.
[251.74 --> 251.88]  Yeah.
[252.26 --> 252.54]  Okay.
[252.58 --> 253.36]  Got Fat Stacks.
[253.62 --> 254.16]  I'll take it.
[254.20 --> 254.40]  Yeah.
[254.62 --> 256.58]  Whatever the stack I'm stacking, it'll be fat.
[256.58 --> 259.80]  But we'll just leave that right there where it sits.
[260.18 --> 262.04]  So Lee Rob is with three E's.
[262.12 --> 262.44]  Is that right?
[262.54 --> 266.88]  So Lee E E E Rob is your Twitter handle at least.
[267.28 --> 269.26]  Lee Rob I O is not three E's.
[269.34 --> 270.10]  It's just two E's.
[270.28 --> 270.34]  Oh.
[270.94 --> 271.28]  Yeah.
[271.46 --> 273.40]  Somebody on Twitter scooped up the...
[273.40 --> 274.36]  There's a chink in the armor.
[274.54 --> 274.78]  Yeah.
[275.12 --> 276.12]  That's the only one.
[276.18 --> 276.86]  I don't have it.
[276.86 --> 282.54]  And the person who has it with two E's, like the account is suspended or something too.
[282.62 --> 283.42]  So I can't even...
[283.42 --> 283.98]  Can't even get it.
[284.00 --> 285.26]  You could petition for that, I'm sure.
[285.74 --> 286.58]  Maybe there's a way.
[286.76 --> 288.56]  You get that blue check mark, you do whatever you want, you know?
[288.60 --> 289.02]  That's right.
[289.40 --> 289.70]  Yeah.
[289.88 --> 290.38]  I don't know.
[290.54 --> 290.88]  We'll see.
[291.04 --> 291.56]  You're on your way.
[291.84 --> 292.18]  Listen up.
[292.22 --> 294.14]  If you're a Twitter employee, hook up Lee.
[294.52 --> 295.40]  Let's get rid of that 30.
[295.54 --> 296.34]  It's just a...
[296.34 --> 296.78]  It's cleaner.
[297.14 --> 297.96]  Let's compress that thing.
[297.98 --> 298.20]  That's right.
[298.30 --> 299.22]  It's like dropping the duh.
[299.58 --> 300.30]  We've been there before.
[300.48 --> 300.68]  Yep.
[301.24 --> 302.16]  Well, we have you here today.
[302.16 --> 305.02]  We should mention that you are not just a DevRel Eversal.
[305.14 --> 306.56]  You're director of DevRel.
[306.86 --> 307.10]  Mm-hmm.
[307.14 --> 308.60]  Which I assume is even cooler.
[308.88 --> 310.24]  And we want to talk about DevRel.
[310.32 --> 312.10]  We had a listener write in.
[312.72 --> 315.62]  Now, I believe his name is Gustav Jorlov.
[316.14 --> 319.58]  But I'm going to give Gustav a little bit of a hard time because, you know, on our form
[319.58 --> 324.32]  where you request a show, we have another section for on-air credit where you can actually
[324.32 --> 326.72]  put the pronunciation of your name.
[327.26 --> 328.88]  And Gustav just put the exact...
[328.88 --> 329.86]  He just put his name twice.
[332.28 --> 333.00]  Don't get it.
[333.22 --> 333.72]  Don't get it.
[333.76 --> 334.16]  Don't worry.
[334.16 --> 336.14]  I will usually apologize for mispronunciations.
[336.14 --> 337.62]  I'm not going to apologize this time, Gustav.
[337.66 --> 339.86]  You had an opportunity to help me out, but you didn't.
[340.00 --> 342.16]  Nonetheless, he asked to have you on the show.
[342.26 --> 343.50]  He wanted us to talk about DevRel.
[343.90 --> 345.84]  We talk to DevRels a lot.
[345.92 --> 347.90]  We talk around DevRel a lot.
[347.96 --> 352.02]  We never talked about developer relations as a thing.
[352.24 --> 353.50]  So that's why you're here, Lee.
[353.72 --> 354.02]  Ever?
[354.20 --> 354.42]  No.
[355.04 --> 355.24]  Ever.
[355.30 --> 355.60]  I mean, ever.
[355.76 --> 356.58]  13 years of history.
[356.74 --> 357.08]  Zero.
[357.32 --> 357.54]  Zero.
[357.54 --> 360.78]  No question of the actual title slash anything.
[361.06 --> 361.62]  I mean, nothing.
[361.96 --> 362.28]  Right.
[362.48 --> 362.70]  Really.
[362.98 --> 364.56]  So we'll ask you, you can open it up.
[364.66 --> 366.04]  What even is a DevRel?
[366.86 --> 367.26]  Yeah.
[367.32 --> 369.68]  The meta conversation of what is DevRel.
[370.00 --> 370.18]  Yeah.
[370.46 --> 370.90]  Yes.
[371.22 --> 371.48]  Yeah.
[371.48 --> 379.64]  So the way that I run my developer relations team focuses on three different things.
[379.92 --> 381.94]  The first is around education.
[382.58 --> 384.36]  The second is around community.
[384.86 --> 387.32]  And the third is around the product.
[387.32 --> 400.84]  Now, the way DevRel teams or organizations are structured at companies kind of depends on where it falls in that company's priorities.
[401.20 --> 410.46]  So for like a developer tooling company, right, where their bread and butter, like their main focus is talking to developers.
[410.88 --> 416.90]  It's probably going to have an elevated position in the company because it's incredibly important to their business and to their community.
[417.32 --> 424.62]  Maybe if the company is just like they have an API as part of their products, but that's not like the main thing they do.
[424.82 --> 431.06]  They might have a developer relations team who's helping with the adoption of the API and ensuring that people are successful with it.
[431.30 --> 433.04]  But it's not the main thing.
[433.46 --> 445.12]  So I like to give that caveat because it's hard to give a singular definition of what DevRel is, but there's multiple flavors we can be inspired from for teams who are trying to figure out,
[445.12 --> 453.12]  okay, how do I want to get into this space or how do I want to structure my organization to support developer communities?
[453.26 --> 459.66]  I talk to a lot of startup founders, early stage companies who are talking to me about when should I hire a DevRel?
[459.82 --> 465.84]  When should I hire these people to build our communities or to help educate developers?
[466.10 --> 469.04]  And it gets tricky because not all companies are the same.
[469.12 --> 472.08]  It requires a little bit of nuance to dive into there.
[472.08 --> 483.68]  So to reel it back just a little bit back to the three pillars I talked about of kind of education, community, and product, I can dive into each one of those independently.
[483.84 --> 485.60]  So let's start with the first one of education.
[486.40 --> 490.52]  Vercel is a company that's like a front-end platform.
[490.78 --> 493.36]  You can deploy your code, build deploy code hosts around the world.
[493.36 --> 498.92]  And because of that, we also have frameworks like Next.js that allow you to write your code.
[499.40 --> 502.90]  So the nature of the products requires education.
[503.18 --> 506.18]  We have to teach developers how to use these tools.
[506.34 --> 511.42]  It's not always immediately obvious how you would build a global application.
[511.76 --> 513.80]  Maybe you need some guidance along the way.
[513.80 --> 520.94]  And I think that education for developers is deeply rooted in basically everything we do.
[521.10 --> 524.50]  As we got started learning how to code, education was important.
[524.72 --> 537.58]  And being a lifelong learner or a continual learner is so rooted in the development journey, especially for web developers where the types of technology go through cycles.
[537.58 --> 543.64]  And you're learning new things over the years and kind of iterating on your knowledge and learning new techniques.
[544.14 --> 554.38]  So it's important that you're helping guide developers along the journey and teaching them the tools and the tricks that they need to be successful with the product.
[554.70 --> 563.16]  The second pillar I think a lot about is community because you can't, it's harder to replicate a community.
[563.16 --> 571.28]  Like you can purchase a product, you can, you know, acquire an audience, but that doesn't automatically mean you have a community.
[571.64 --> 576.24]  Community building requires dedicated effort and attention.
[576.60 --> 582.94]  And I think it's one of the highest leverage things a developer focused company can have.
[582.98 --> 590.10]  If you have a community of developers who love your product, they kind of do the job for you.
[590.16 --> 591.90]  They advocate for your product for you.
[591.90 --> 595.80]  You don't need, like you're, they're your outsourced DevRel team at that point, right?
[595.82 --> 600.12]  Like they're talking to the community about, wow, this product is amazing.
[600.26 --> 601.34]  You should be using it.
[601.44 --> 604.96]  And they love it so much that maybe they go talk to other developers about it.
[605.34 --> 614.10]  And being very intentional about growing that community is a very important part of what a lot of DevRel teams focus on.
[614.10 --> 621.32]  And then the third one, and just a quick summary, like, and then the third one is, is really how it all relates back to the product.
[621.76 --> 629.48]  And I think it's important that developer relations roles or developer experience or developer advocate, there's multiple titles.
[629.48 --> 630.68]  We can get into that nuance.
[630.68 --> 641.64]  All of these roles play some part in giving feedback on what works well and maybe what's not very good on the product.
[641.86 --> 646.38]  And it's, I think it's important to get that feedback internally before you hear it from your customers.
[646.38 --> 666.38]  So, for example, if we're releasing a new product or a new feature, I would rather have some engineers internally who have this critical eye for what a good developer experience looks like, walk through the product, try to figure out how things could be broken, where beginners might struggle, where advanced people might struggle.
[666.38 --> 669.70]  And get that feedback before we release it to everybody.
[670.22 --> 675.22]  And there's this continuous feedback loop of community pain point.
[675.68 --> 676.98]  How do we solve it in the product?
[677.48 --> 678.44]  You know, community struggle.
[678.82 --> 684.22]  How do we better create educational material to help prevent that from happening in the future?
[685.68 --> 694.12]  In a lot of ways, it's a very nuanced dance between how to innovate and iterate and how to, you know, literally educate.
[694.12 --> 706.06]  But then I also take that feedback because, I mean, that feedback assumes and sort of requires this person or many people to have empathy for the direction the community is trying to go.
[706.28 --> 706.40]  Yeah.
[706.72 --> 712.22]  And I think in particular, because we kind of know Vercel's story, and we should also say we have Vercel as a sponsor of JS Party.
[712.76 --> 712.98]  Yeah.
[713.16 --> 714.86]  Not a sponsor of this show in particular.
[715.08 --> 716.26]  That's not why you're on this show.
[716.34 --> 717.86]  We truly are deeply.
[718.66 --> 720.42]  I've known Guillermo for many years.
[720.60 --> 723.46]  Guillermo, I've been recently told that's exactly how you say his name.
[723.46 --> 726.58]  But I've been calling him Guillermo for many, many years, incorrectly, of course.
[727.00 --> 729.04]  Now I'm just going to say Guillermo every single time.
[729.46 --> 730.80]  But I've known him many years.
[730.92 --> 733.04]  Jared, you and I met up with him in San Francisco years ago.
[733.08 --> 737.00]  We went out to just meet up, and we shared early days of our website and the direction.
[737.34 --> 740.56]  So he's been in the community forever, you know, for a very long time.
[740.58 --> 743.22]  And I've been tracking his career, and we have as an organization.
[743.22 --> 751.50]  But when you have, you know, the inertia of Vercel being make the web faster, that's sort of your, you know, the direction of your product, right?
[751.56 --> 757.02]  And so you're going to kind of pull community because you're trying to innovate and iterate the literal web.
[757.06 --> 758.66]  And the way you do it is with your platform.
[758.70 --> 760.06]  And the way you also do it is with your software.
[760.28 --> 760.48]  Yep.
[760.48 --> 761.42]  That enables a platform.
[761.52 --> 763.04]  And the community that wants to build for the web.
[763.32 --> 773.00]  What I'm trying to make, though, is just that, you know, it's pretty interesting how you have to have this dance and this empathy and this sort of middle ground people that care to enable that feedback loop.
[773.00 --> 773.66]  It's necessary.
[774.22 --> 779.28]  What gets challenging is when, and in your case, the organization is set up right.
[779.50 --> 781.00]  The way you're directing it is right.
[781.00 --> 790.78]  What gets, you know, sort of like hard to believe or hard to trust is when there's KPIs and OKRs and sort of like salesy things attached to that organization.
[791.40 --> 792.58]  Where do you sit with that?
[792.58 --> 808.66]  How does that, what has been your experience with other DevRails that have these ambiguous, weird attachments like OKRs and KPIs and like sales related goals attached to that feedback loop that's so necessary for a dev focused organization like Vercel?
[808.66 --> 818.00]  Yeah, going back to the first part of your question around empathy, that's actually one of the most critical things that I look for when I'm trying to hire people.
[818.00 --> 830.86]  And I think is what separates great developer relations teams from maybe those who are just OK, is that you have to really care about the product that you're advocating for and the community that you're a part of.
[830.86 --> 841.16]  Like when I see people struggling with the product, I generally want to know what we can do better and how we could take that feedback and use it to provide a better experience.
[841.16 --> 857.78]  And you have to address that with a empathetic beginner's mindset because not everybody has the context that you might have on, you know, years of using the product or, you know, years of being a front end developer or a back end developer.
[858.02 --> 860.24]  You have to embrace that.
[860.54 --> 862.32]  This is my first time learning how to code.
[862.74 --> 864.54]  Somebody told me I needed to learn Next.js.
[864.84 --> 865.88]  Now I'm reading the docs.
[866.40 --> 867.52]  What is this thing?
[867.54 --> 869.02]  I've never heard this term before.
[869.02 --> 872.34]  And like trying to solve for that case as well, too.
[872.92 --> 881.30]  But then coming back to your question about how do you define and measure success for developer relations?
[881.58 --> 885.52]  There's a few good resources out there right now that I'm fond of.
[885.60 --> 894.74]  And I think part of this question ties back to the organizational structure that sets up a DevRel team for success.
[894.74 --> 908.08]  So, for example, if a DevRel team is under product, if they're under marketing, if they're under sales, if they're under their own organization, those KPIs and metrics might all be a little bit different.
[908.60 --> 914.36]  I think Swix has a good blog post about measuring developer relations that I'd recommend checking out for those listening in.
[914.36 --> 927.10]  My view is that I'm not a big fan of the vanity metrics like this got 10,000 blog post views or this got 200 retweets.
[927.60 --> 932.90]  Those are a byproduct of making a good product and fostering a good community.
[932.90 --> 960.78]  So if you invest in listening to your customers and where they're succeeding and maybe where they're not, taking that negative feedback and incorporating it into building a better product and a better experience for those developers, the byproduct of that is the attribution towards more blog post views, more tweets, more engagement on Facebook or LinkedIn or whatever social platform you want.
[960.78 --> 969.88]  So personally, I don't think it makes as much sense for me as the north star of the metrics to look towards those traditional marketing focused KPIs, I guess.
[970.24 --> 982.44]  I do think it is interesting to think about some of the sales goals because at the end of the day, you're building a community of developers who are excited about a product.
[982.44 --> 986.42]  And that product is probably something that you pay for.
[986.80 --> 993.20]  And I don't think that you should be too abstracted from the reality of this is a product that people pay for.
[993.32 --> 1005.88]  I think if you go too far in the other direction, you're actually doing a disservice to your community because you're almost being disingenuous about the reality of what makes the business sustainable.
[1005.88 --> 1012.04]  So in the context of like a Vercel or a hosting platform, you know, we have a free tier.
[1012.18 --> 1013.28]  There's always a free tier.
[1013.52 --> 1022.78]  It's always going to enable developers to get started, build applications and be able to put content basically online around the globe really fast.
[1022.92 --> 1027.24]  And that works really great for, you know, many, many developers.
[1027.24 --> 1034.82]  But then there's also a part of our business that's catering to teams that pay, whether that's customers on like our pro tier or enterprise customers.
[1035.04 --> 1040.38]  And I think you're also enabling those developers because they're also part of your community.
[1040.38 --> 1048.32]  Just because they're on an enterprise deal doesn't mean that they're not deeply embedded and care a lot about the community's success.
[1048.32 --> 1055.62]  It's interesting to see this role formalized so much so that it's, you know, you have a director of the role.
[1055.76 --> 1058.32]  And so you have a fleet of dev rails.
[1058.42 --> 1062.68]  I'm sure Vercel is not the only organization that has like multiple dev rails, fleets of dev rails.
[1063.00 --> 1063.12]  Yeah.
[1063.48 --> 1065.42]  It feels like a newish thing.
[1065.56 --> 1066.98]  I went to Wikipedia, did some reading.
[1067.12 --> 1070.76]  It turns out, no, like Apple invented this back in the 80s.
[1070.94 --> 1073.12]  They called them software evangelists back then.
[1073.12 --> 1087.06]  And it's kind of this thing that's evolved and changed over time and become more formal, become more obviously valuable for organizations to employ this type of a role or this set of roles, which really is, like you said, community, education and product.
[1087.06 --> 1089.84]  Three distinct things that all work together.
[1089.96 --> 1097.28]  I'm curious, your history, though, like how did you get into dev rail and what made you attracted to this kind of a role and then also good at it?
[1097.36 --> 1101.00]  Like, why would you get moved up to director of dev rail unless you were good at it?
[1101.02 --> 1101.74]  So I assume you are.
[1101.74 --> 1102.18]  Yeah.
[1103.38 --> 1108.10]  So what got me into dev rail was actually a long journey.
[1108.48 --> 1117.64]  So prior to joining dev rail, I had been working as a product engineer for many years and primarily focused on the front end.
[1117.92 --> 1121.48]  And I've always really loved front end development.
[1121.48 --> 1130.50]  When I was learning how to code in college or university, I didn't really enjoy it until we started to use web development.
[1130.50 --> 1138.60]  And that was when I had this light bulb moment of I can put code online and share it with anybody behind this URL.
[1138.60 --> 1148.00]  Like we would even I looked at mobile apps and I was like, well, this process is overly complex versus just deploying and getting a URL and having it out there.
[1148.00 --> 1156.88]  And for the first, you know, good chunk of my career, I was really focused on just becoming the best front end developer I could possibly be.
[1156.88 --> 1164.62]  So that was going from individual contributor to, you know, leading a team of developers working on an e-commerce site.
[1164.62 --> 1178.48]  And at the same time, I've always really enjoyed the intersection between development and everything else that needs to happen at the company, which is ironic because I haven't worked at a startup until I worked at Vercel.
[1178.48 --> 1189.96]  So I had seen some examples of how it doesn't work well when the development team is so siloed away from the other parts of the business.
[1190.20 --> 1204.40]  I get a lot of enjoyment out of the intersection between development and marketing and sales and product and all of these pieces that actually enable an end to end great experience.
[1204.40 --> 1214.52]  So that's some of my history that's led to me exploring what was DevRel before I knew it was DevRel.
[1214.88 --> 1227.64]  So I because of my enjoyment of the intersection between these things and just a general enjoyment of helping teach others, whether that was writing or in person, helping pair with other developers.
[1227.64 --> 1236.86]  I started to kind of just create content and put it out there as my own person, you know, as Lerop.
[1236.96 --> 1244.92]  I put out content online to help developers succeed with, you know, React or front end, CSS, Next.js, whatever they wanted to use.
[1245.80 --> 1250.20]  And it was towards the relative beginning of Next.js.
[1250.20 --> 1261.40]  I think this Next.js was created in 2016 and about 2018 is when I was starting to use Next.js at my previous company to help them, you know, build out their e-commerce experience.
[1262.68 --> 1272.22]  And at the time, you know, with any new tool, there's just not that much information out there or educational material to help developers succeed.
[1272.22 --> 1275.60]  And I thought, well, you know, I enjoy doing this stuff.
[1275.68 --> 1276.30]  I like writing.
[1276.44 --> 1278.90]  I like teaching developers how to succeed with this stuff.
[1279.08 --> 1282.52]  If this content isn't out there, why don't I just make it?
[1282.62 --> 1285.66]  Like, no, that's the great thing about the internet is that it's permissionless.
[1285.76 --> 1287.68]  I can publish that blog post if I want to.
[1287.74 --> 1289.08]  I can create that resource.
[1289.78 --> 1291.16]  And so I did.
[1291.28 --> 1299.16]  So I started making content, YouTube videos, blog posts, all sorts of stuff, courses to enable developers to really succeed.
[1299.16 --> 1308.84]  And eventually that wound its way towards me getting a job at Purcell to kind of further continue that goal.
[1310.06 --> 1323.90]  A key word you've said there a couple of times is succeed, which I think is kind of critical to defining that dev role role well, because like you had said, you can't hide the metrics of, you know, let's say a sales goal or something like that.
[1323.90 --> 1332.00]  Maybe that's where like you can get a little bit tricky, but being able to succeed in terms of helping the developer succeed.
[1332.32 --> 1333.58]  That's kind of key, right?
[1333.76 --> 1333.94]  Yeah.
[1334.00 --> 1338.18]  Which is naturally going to lead to a business success succeed again.
[1338.26 --> 1338.48]  Right.
[1338.56 --> 1338.78]  Right.
[1338.82 --> 1342.50]  Because that's a natural feedback loop to positive outcomes.
[1343.14 --> 1343.50]  You know what I mean?
[1343.52 --> 1345.18]  That's kind of critical to the role.
[1345.18 --> 1356.64]  If you think about it like this, it doesn't matter if you spend millions of dollars on marketing, if the developer goes to the blog post and they say, all right, click here to try it out.
[1356.70 --> 1359.02]  And they go try out the product and it just doesn't work.
[1359.40 --> 1361.26]  Then what are we doing here?
[1361.42 --> 1362.98]  You know, like what was the point of all this?
[1363.20 --> 1363.46]  Precisely.
[1363.48 --> 1364.56]  What was the point of all this work?
[1364.66 --> 1368.96]  It has to be in service of the success of the developer.
[1368.96 --> 1376.98]  And that's a very nuanced thing, too, because it's not always just was I able to get X thing done?
[1377.50 --> 1380.66]  It also might be did I understand what I'm doing?
[1380.80 --> 1382.30]  Do I understand the context of this?
[1382.36 --> 1384.28]  Am I actually using it for the right thing?
[1384.48 --> 1390.46]  Am I providing the right resources to help this developer succeed with what they're trying to get done?
[1391.10 --> 1395.34]  It kind of reminds me, too, of this inspiration of curiosity.
[1395.34 --> 1398.84]  You know, there's times I'll have this really cool tool.
[1399.32 --> 1403.00]  I'll be ambiguous in this case, and I have no idea what to do with it.
[1403.06 --> 1407.28]  Like, I know it's got lots of capabilities, but I've got my own use cases.
[1407.28 --> 1414.14]  But I'm sort of like siloed and and, you know, minimized by my own dreams, I suppose.
[1414.36 --> 1417.36]  I almost need somebody else to help me dream bigger about the possibility.
[1417.92 --> 1420.14]  Oh, did you know this, this and this could enable that?
[1420.30 --> 1420.44]  Yeah.
[1420.44 --> 1425.00]  You know, so you're almost like a curiosity inspirer.
[1425.52 --> 1429.30]  And I almost think of it like a good analogy might be a box of Lego.
[1429.74 --> 1433.88]  You can get a box of Lego and you can watch Lego Masters on TV.
[1434.12 --> 1437.94]  And what they do with Lego may be way different than what you would do with the same box.
[1438.26 --> 1438.36]  Yeah.
[1438.36 --> 1445.84]  And it might be that rail person, the dev rail or the Lego rail or somebody railing in there.
[1446.38 --> 1448.40]  This inspiration, this curiosity.
[1448.56 --> 1451.10]  Here's the possibility of what you could do with this thing.
[1451.10 --> 1455.74]  And then also, and that might be the sort of community content piece of it.
[1456.06 --> 1463.20]  But also, like, how do we learn from what you've done with it and hit those roadblocks or hit those anti-successes, those failures?
[1463.58 --> 1470.10]  And how can we improve the flow so that you don't have that hurdle, that roadblock anymore your next try?
[1470.42 --> 1471.26]  Yeah, absolutely.
[1471.26 --> 1471.38]  Absolutely.
[1471.38 --> 1471.44]  Absolutely.
[1471.44 --> 1472.38]  Absolutely.
[1472.38 --> 1473.38]  Absolutely.
[1473.38 --> 1474.38]  Absolutely.
[1474.38 --> 1475.38]  Absolutely.
[1475.38 --> 1476.38]  Absolutely.
[1476.38 --> 1477.38]  Absolutely.
[1477.38 --> 1480.44]  And then also, and that might be the sort of community content piece of it.
[1480.44 --> 1488.64]  This episode is brought to you by our friends at FireHydrant.
[1488.84 --> 1491.72]  FireHydrant is the reliability platform for every developer.
[1492.12 --> 1495.90]  Incidents, they impact everyone, not just SREs.
[1496.04 --> 1503.78]  They give teams the tools to maintain service catalogs, respond to incidents, communicate through status pages, and learn with retrospectives.
[1503.78 --> 1509.58]  What would normally be manual error-prone tasks across the entire spectrum of responding to an incident,
[1509.58 --> 1513.02]  they can all be automated in every way with FireHydrant.
[1513.02 --> 1518.40]  They have incident tooling to manage incidents of any type with any severity with consistency.
[1518.94 --> 1522.08]  Declare and mitigate incidents all from inside Slack.
[1522.48 --> 1528.78]  Service catalogs allow service owners to improve operational maturity and document all your deploys in your service catalog.
[1528.78 --> 1536.74]  Incident analytics allow you to extract meaningful insights about your reliability over any facet of your incident or the people who respond to them.
[1536.74 --> 1546.54]  And at the heart of it all, incident runbooks, they let you create custom automation rules, convert manual tasks into automated, reliable, repeatable sequences that run when you want.
[1546.90 --> 1550.90]  You can create Slack channels, Jira tickets, Zoom bridges instantly after declaring an incident.
[1550.90 --> 1553.98]  Now your processes can be consistent and automatic.
[1554.44 --> 1556.12]  The next step is to try it free.
[1556.26 --> 1560.64]  Small teams, up to 10 people, can get started for free with all FireHydrant features included.
[1560.98 --> 1562.36]  No credit card is required.
[1562.82 --> 1564.98]  Get started at FireHydrant.io.
[1565.34 --> 1567.20]  Again, FireHydrant.io.
[1567.20 --> 1567.32]  FireHydrant.io.
[1583.98 --> 1587.20]  Let's go back a bit and talk about how this role has evolved.
[1587.40 --> 1596.78]  So, not Wikipedia, 19 whatever, I can't go back that far personally, but we've been around as an organization since 2009, right?
[1597.24 --> 1600.26]  ChangeLog began around then, doing this 13 plus years.
[1600.38 --> 1603.60]  So, our lens is around 13-ish years or more.
[1603.78 --> 1603.98]  Yeah.
[1604.22 --> 1605.50]  Not 25 or more.
[1605.66 --> 1613.50]  So, I would say early dev roles that I'm aware of, the earliest might be, and this is by no means an exhaustive list.
[1613.56 --> 1614.66]  These are just like closer friends.
[1614.66 --> 1617.26]  Steve Klabnick was part of the ChangeLog way back in the day.
[1617.44 --> 1620.64]  He used to be a host, used to be a contributor to the blog.
[1621.20 --> 1626.72]  The same with Kenneth Reitz, who was also a contributor, host on the show, etc., etc.
[1626.72 --> 1634.58]  And my experience with those two in particular was this level of burnout because the role kind of – it did what you said.
[1634.58 --> 1639.60]  It also kind of required a lot of speaking, a lot of like real direct IRL engagement.
[1639.86 --> 1640.00]  Yeah.
[1640.10 --> 1640.86]  That meant flying.
[1640.98 --> 1643.08]  That meant international flying in lots of cases.
[1643.94 --> 1648.04]  And then when JSParty came around, we had Rachel White on the show.
[1648.14 --> 1649.44]  Ojo, as she's called on Twitter.
[1649.88 --> 1651.06]  She's also a dev role.
[1651.18 --> 1652.14]  I don't know if she still is anymore.
[1652.22 --> 1653.12]  I haven't caught up with her in a bit.
[1653.28 --> 1657.96]  But similar, like this sentiment of like burnout, like always going kind of thing.
[1658.40 --> 1663.50]  Let's kind of go back and maybe share what your experience might be with this role and how it's evolved.
[1663.50 --> 1670.18]  It seems to have matured and maybe thanks to – in a spiteful way to COVID that now we don't travel as much.
[1670.24 --> 1671.40]  We're kind of getting back to travel.
[1671.48 --> 1675.26]  This role sort of calmed down a bit and sort of maybe even had a chance to sort of reshuffle.
[1675.52 --> 1680.78]  What is your experience of like old days dev role to like current modern day dev role and how has it changed?
[1680.78 --> 1690.50]  Yeah, so to first set the stage, I have been officially like by my job doing dev role now for two years.
[1690.70 --> 1696.16]  And then unofficially probably since 2016, I guess.
[1696.52 --> 1703.48]  But if we go back to 2011, 2012, so I started to learn how to code in 2011.
[1703.48 --> 1711.78]  And at the time, the dev role that I really remember was from the new API companies.
[1712.02 --> 1727.10]  It felt like a generational change or a big enough shift in the industry that it required education and awareness to tell people about a different way of doing things.
[1727.10 --> 1732.22]  And that was kind of – from my eyes, that was like 2011 to 2015.
[1732.22 --> 1740.34]  I feel like there was a massive rise in the number of API companies or companies providing things as a service.
[1741.00 --> 1747.90]  And to do that, they had these members of their community, whether it was called DevRel or not at the time,
[1747.90 --> 1761.00]  actually go out and go to in-person conferences, go to meetups, go to anywhere around the world and tell people about how the product works, how the thing works, do a workshop on how to actually use the thing.
[1761.50 --> 1770.56]  And at the time, too, another thing I've realized in talking to a lot of teams is a lot of DevRel actually came from founders back in the day.
[1770.56 --> 1778.34]  The early employees at companies were essentially doing the majority of the product and community side of DevRel.
[1778.78 --> 1782.92]  And then eventually it scales to a point where they don't have a full-time job to do that.
[1783.18 --> 1785.30]  At some companies, that actually turns into the product org.
[1785.42 --> 1788.12]  Like the PMs are just very good about that outreach.
[1788.32 --> 1792.22]  And then at some developer-focused companies, they really lean into DevRel for that stuff.
[1792.22 --> 1803.92]  So if we fast forward a little bit and get closer to today, I think the thing that's been really interesting, kind of pre-COVID, post-COVID that I've seen,
[1804.42 --> 1812.90]  was the community understanding that virtual or online has a place if done right.
[1813.62 --> 1820.04]  And I think the distinction there is it has to be done tasteful and respectful of people's time.
[1820.04 --> 1825.08]  So I'll give an example of where it's maybe people are a little burnt out about online.
[1825.32 --> 1834.28]  Of course, everyone was sick of going to many virtual events, many conferences online in the past few years.
[1834.96 --> 1842.02]  And if you were going to do any sort of developer outreach or socializing with your community,
[1842.02 --> 1848.58]  it had to be something unique to make them feel like it was not just another Zoom call, right?
[1848.58 --> 1856.36]  And an interesting side effect of this, looking at purely from like the viewership or the amount of traffic that you got,
[1856.44 --> 1862.12]  a lot of teams realized, wow, we can actually get more traffic by doing this online.
[1862.26 --> 1863.48]  We have a global community.
[1863.48 --> 1868.78]  Instead of doing just this one event in New York or San Francisco or London,
[1868.92 --> 1873.70]  we can actually broadcast this everywhere and be inclusive of our entire global community.
[1873.70 --> 1880.16]  We don't necessarily need to do 57 meetups to get this community activated and engaged.
[1881.06 --> 1888.76]  And also for the, you mentioned burnout, I guess, of developer advocates or people who were traveling for their job.
[1889.10 --> 1897.28]  It could definitely be a strenuous position to have to basically just go around all year living on the road,
[1897.28 --> 1902.22]  giving conference talks, going to meetups, you know, interacting with the community,
[1902.46 --> 1905.18]  especially for those, a lot of those people, I think too,
[1905.76 --> 1911.14]  maybe that was a viable thing for them to do at that point in their life at the 2012 era.
[1911.14 --> 1919.70]  I think a lot of the original DevRel, DevRelians, the DevRel folk have kind of evolved into something else.
[1920.14 --> 1924.52]  A good example, somebody that I look up to a lot is Kelsey Hightower.
[1924.52 --> 1933.26]  I think that he has a very interesting role now where he is kind of like, he's evolved from DevRel.
[1933.52 --> 1936.56]  And, you know, he had obviously done a lot of stuff before doing DevRel work too,
[1937.08 --> 1942.52]  but to a, somebody who really holistically thinks about an incredible product experience.
[1942.88 --> 1948.66]  And I think if you look around the industry, some of the other people who were well-known in DevRel,
[1948.66 --> 1956.24]  a lot of them have transitioned to do other related things still in the same arena, but with a little bit more focus.
[1956.52 --> 1962.06]  So the summary of all this is that when I look at DevRel in 2022,
[1962.62 --> 1966.80]  you don't necessarily have to fly to every conference in the world.
[1966.98 --> 1970.26]  You don't necessarily have to do a hundred meetups.
[1970.26 --> 1975.68]  You can be a little bit more strategic about when and where you want to do those things.
[1976.14 --> 1982.22]  But as we start to now get back to doing in-person events, which I've now spoke at,
[1982.72 --> 1987.50]  I think four this year so far, and I have a few more coming up here in the next couple of months.
[1987.66 --> 1989.74]  So it's, it's definitely picking up.
[1989.74 --> 1995.86]  There is a, a re-appreciation of just getting people in a room together too,
[1996.20 --> 2002.86]  that one, I think people just missed because of not being around others in a, in a setting for some time.
[2002.86 --> 2010.40]  But also there's, there's something to be said about, you know, getting together and just having a casual chat about development stuff.
[2010.40 --> 2013.52]  Like just talking about tech, talking about development.
[2013.52 --> 2022.20]  And, you know, it's sometimes it's hard to recreate that spontaneity when you're in a online event.
[2022.32 --> 2029.98]  So my, I guess my philosophy and where I'm kind of taking our DevRel team is that I want to do both.
[2030.24 --> 2034.32]  I still think there's a place for, you know, when we have a global community of developers,
[2034.32 --> 2041.54]  it's not feasible for me or others on my team to be flying around the world all the time to go to a bunch of events.
[2041.54 --> 2047.98]  And I know that some really large DevRel teams solve this by having lots of employees all around the world.
[2048.08 --> 2054.00]  We're not there yet, but I think there's still a place for in-person as well too.
[2054.12 --> 2057.90]  So we can have online and we can also still go to some events and conferences.
[2059.34 --> 2064.92]  What I, my experience with the online events, I only took part in a handful of them throughout the two years,
[2064.92 --> 2069.72]  you know, starting that lockdown was you get big numbers, you get big signups.
[2069.72 --> 2076.08]  You might even get big numbers in the actual room, but the level of attention and engagement,
[2076.76 --> 2080.44]  even for myself personally, I'm in the room, I signed up, I'm there.
[2080.98 --> 2084.44]  It's just another tab in my browser or it's just another Zoom window.
[2085.20 --> 2087.10]  I'm also playing Wordle or something.
[2087.26 --> 2090.26]  Like I just don't, I don't feel any connection really.
[2090.94 --> 2095.62]  Even less so than this three person call right here because I don't have to participate.
[2095.94 --> 2097.32]  Maybe I can, I can raise a hand.
[2097.32 --> 2097.70]  I don't know.
[2097.94 --> 2102.32]  It was very superficial, but obviously it was necessary.
[2102.68 --> 2107.98]  And the point you spoke to with the accessibility was of everybody, right?
[2107.98 --> 2115.62]  The lower barrier of entry for people who live halfway around the world from where a real life event would be held or whatever reason,
[2115.72 --> 2120.84]  the timing, their life, like it allowed everybody to come, which was awesome.
[2120.84 --> 2124.74]  But once we were all there, for me, it was kind of like, right.
[2125.20 --> 2125.68]  Fell flat.
[2126.04 --> 2128.22]  And so I'm very excited about getting back out.
[2128.34 --> 2128.50]  Yeah.
[2128.66 --> 2132.48]  And I think obviously, I think what we learned is hybrid is awesome.
[2132.84 --> 2139.34]  You know, moving forward, giving, trying to find the best from both circumstances, bring them together for better events.
[2139.34 --> 2143.28]  And then I like your idea of like, hey, make it when you can.
[2143.68 --> 2146.54]  Don't kill yourself to be there at every conference, right?
[2146.78 --> 2157.26]  Because I think that's what really burned out a lot of folks in the before times was like this desire to be at everything and speak at everything and blog all the time.
[2157.26 --> 2161.42]  And there was just no end in their mind of the workload.
[2161.94 --> 2174.36]  I think there's also too, a tricky conversation to understand in the world of DevRel is the distinction between the individuals and the companies.
[2175.00 --> 2175.26]  Yes.
[2175.46 --> 2178.32]  And we can really go in depth further on this.
[2178.32 --> 2188.76]  The way I think DevRel is evolving is the people who are taking these roles are almost like knowledge athletes.
[2189.30 --> 2192.32]  I've heard these analogies made in other places.
[2192.44 --> 2194.76]  I don't really have the best way to describe it.
[2194.82 --> 2198.78]  But basically, they have their own thing going.
[2198.78 --> 2209.32]  They have their own brand or whatever you want to call that of their own community of people who care about what they say and how they act.
[2209.94 --> 2214.26]  And part of that affiliation is also representing a company sometime.
[2214.74 --> 2216.72]  So if you give a sports analogy, right?
[2216.98 --> 2226.38]  Like maybe I am a professional basketball player who happens to play for, you know, the Atlanta team right now.
[2226.38 --> 2231.80]  But then maybe in the future, I get drafted by or I change teams to New York, right?
[2231.84 --> 2233.12]  That happens, right?
[2233.14 --> 2235.34]  That's just the nature of how people change jobs.
[2236.20 --> 2241.56]  And I think it's interesting when you think about DevRel because the role is so public facing.
[2242.34 --> 2245.22]  Like these are people who are advocating for your company.
[2245.22 --> 2247.30]  They're out talking on podcasts.
[2247.30 --> 2249.60]  They're out interacting with communities.
[2249.60 --> 2259.80]  So for that person to be kind of like a professional athlete for a company, it requires a little bit of nuance in how you work.
[2261.26 --> 2263.12]  Because you kind of care about their opinion, right?
[2263.38 --> 2263.66]  Yeah.
[2263.76 --> 2271.48]  Like they're good with Hadoo because they can curate the possibility and whittle it down to a point of focus.
[2271.48 --> 2272.64]  And that's kind of the employment.
[2272.84 --> 2274.78]  The employment is sort of the point of focus.
[2274.78 --> 2282.24]  I care so much about the future of the web that I decided to put my focus and my attention on the Vercel platform as your direct example.
[2282.80 --> 2286.86]  In Kelsey's case, maybe it's Google with GCP or the direction of Kubernetes.
[2287.88 --> 2290.48]  And as you had said, he kind of transcended, and I think he has as well.
[2290.98 --> 2300.50]  What I love most about Kelsey is his ability just to look, like you said, holistically at the scenario and not think like, what should you buy Google or should you buy a direction?
[2300.66 --> 2300.94]  Exactly.
[2300.94 --> 2304.78]  Here's how software is evolving. Here's the way I think it makes sense for you to use it.
[2304.92 --> 2308.50]  And we happen to be putting products in place that help you use it that way kind of thing.
[2309.10 --> 2319.36]  Yeah. And I think what's important about that is when you start to get into situations where like people will ask me my opinion on something because of my experience with the front end.
[2319.98 --> 2325.28]  And sometimes that answer is for sale because it is the best choice for what they want to use.
[2325.34 --> 2326.42]  And sometimes it's not.
[2326.42 --> 2330.50]  And it's disingenuous if I were to not give that response to people.
[2331.00 --> 2337.36]  But I think it's hard for some companies to realize that's the type of role that this position is.
[2337.52 --> 2343.46]  It's not necessarily a paid spokesperson that's going to advocate only good things for the company.
[2343.60 --> 2348.26]  Like I'm very well aware of what's great about our product and what needs improvement.
[2348.26 --> 2354.68]  And I hear that feedback from the community and I take that and I try to translate that into making the best product.
[2354.84 --> 2362.62]  But if somebody asks me what's the best way to do this, this or this, I try to be as honest as I can because that's how you build trust with the community.
[2362.62 --> 2375.76]  Do you personally struggle or wrestle with that relationship where your work is so much tied up into your identity or your personal brand, so to speak?
[2376.10 --> 2376.26]  Yeah.
[2376.26 --> 2381.04]  Because some of us are out there coding for a healthcare company.
[2381.24 --> 2383.98]  It's like I care about my work.
[2384.08 --> 2385.44]  I'm a craftsperson, et cetera.
[2385.94 --> 2387.12]  I'm a software developer.
[2387.28 --> 2390.62]  I do my eight to five or maybe I work harder or whatever it is.
[2390.98 --> 2393.36]  And I care about my work and I take pride in it.
[2394.00 --> 2395.54]  But at the end of the day, it's like a healthcare company.
[2395.78 --> 2398.46]  I want it to do well, but it's not my identity.
[2398.46 --> 2407.24]  And where I think as a DevRel, almost necessarily it gets tied up in your identity because you are promoting this thing.
[2407.32 --> 2407.58]  Yes.
[2407.76 --> 2410.54]  Or representing, I should say, maybe more so than promoting.
[2411.34 --> 2414.72]  And so there's like this, like you said, it's very gray lines.
[2414.74 --> 2420.38]  And I wonder if you struggle, like where does Lee end and the director of DevRel at Vercel begin?
[2420.38 --> 2428.56]  Yeah, I think that this is why DevRel requires a very specific type of person.
[2428.68 --> 2434.58]  And why I also would recommend for anybody listening, thinking about wanting to get into DevRel,
[2434.88 --> 2438.12]  you should be picky about the thing that you want to advocate for.
[2438.34 --> 2448.42]  Like, I don't think that people wanting to get into DevRel will be satisfied trying to advocate for something they don't genuinely care about.
[2448.42 --> 2451.86]  Or for a space that they're not really interested in.
[2452.16 --> 2458.94]  Like, I could probably, like if I went and did developer relations work for, I don't know,
[2459.52 --> 2465.14]  some other kind of unrelated part of the development workflow, I could probably do it.
[2465.18 --> 2467.36]  But I wouldn't have as much enjoyment out of it.
[2467.36 --> 2470.56]  And I wouldn't feel as aligned with the front end.
[2470.66 --> 2471.58]  I just love the front end.
[2471.72 --> 2475.12]  That's what I've always enjoyed doing, the intersection between front end and design.
[2475.12 --> 2490.82]  But to your point about the barrier or the line between, you know, Lee as a person and Lee as a representative of the company can be tricky when people will, you know, send me a tweet asking for something.
[2490.96 --> 2493.60]  Hey, why does this Vercel feature not work?
[2493.64 --> 2495.78]  Or why does this NextGest thing happen?
[2495.98 --> 2497.42]  And can you help me figure that out?
[2497.82 --> 2499.26]  It can be tricky to...
[2499.26 --> 2504.68]  Like, I'm watching Stranger Things, you know, trying to take my dog for a walk or like these other things, right?
[2504.68 --> 2505.00]  Yeah.
[2505.46 --> 2511.92]  Especially with, you know, when I talk, my wife comes home from work and just never thinks about it again.
[2512.14 --> 2514.02]  And I'm like, that's awesome.
[2514.24 --> 2523.52]  Sometimes I'm, you know, thinking about something, maybe right before I go to bed, I'm just like thinking about, hmm, you know, I wonder if we could do this thing better.
[2523.72 --> 2528.16]  It's like, it makes it a little harder to turn off.
[2528.16 --> 2531.46]  So I have to be very intentional about how I do turn off.
[2531.54 --> 2539.06]  I have to make sure that I take time to step away and to close the laptop, close the tweets and just have separation too.
[2539.12 --> 2542.06]  Because you have to be intentional about it so that you don't burn out.
[2542.34 --> 2545.58]  Because having that healthy breakdown is important.
[2545.58 --> 2549.20]  What you sound like right now, Lee, is you sound like a business owner.
[2550.02 --> 2553.30]  Because as a person who's owned businesses, Adam, you can speak to this.
[2553.44 --> 2561.08]  Like, the turning it off part is the part that we all, as business owners, struggle with.
[2561.28 --> 2565.26]  Because just because you're not 9 to 5 doesn't mean you're not thinking about the business.
[2566.20 --> 2569.16]  And that's very much what you're talking about.
[2569.16 --> 2571.70]  Now, as business owners, we also own the business.
[2571.90 --> 2577.34]  And so, in that sense, I mean, I'm sure you have access to part ownership in these companies.
[2577.56 --> 2580.24]  But it sounds like maybe that leads to some of the burnout.
[2580.44 --> 2587.64]  Because there's a lot of the downsides of being attached, first and foremost, or in the front of an entity,
[2588.16 --> 2593.70]  without some of the perks of the ownership, which we could also speak to as well.
[2593.84 --> 2596.78]  But you definitely sound like a business owner when you're talking about this.
[2596.78 --> 2604.94]  That's why I think that the best DevRel for early stage companies has to start with the founder.
[2605.10 --> 2606.08]  It has to start there.
[2606.42 --> 2611.60]  Like, they have to learn, whether they do consulting or they learn themselves,
[2611.66 --> 2617.12]  they have to figure out how to be that person first before they replicate themselves with somebody else.
[2617.22 --> 2620.34]  But to your point, yeah, it would be hard.
[2620.34 --> 2630.98]  It would be harder, in my opinion, to do DevRel, to be a DevRel leader at a company where you didn't have, you know, a stake in its success.
[2631.26 --> 2631.28]  Right.
[2631.30 --> 2634.98]  That's one of the nice things about a startup and getting alignment in that regard.
[2635.14 --> 2637.66]  Granted, sure, you could have a lot of stock in a public company.
[2637.76 --> 2641.78]  But it feels like you have a little bit more say in the startup ownership.
[2641.78 --> 2649.70]  But, I mean, you make a valid point, which is it doesn't always have to be like that for individuals in DevRel.
[2650.00 --> 2655.02]  So maybe not a DevRel leader, but just somebody who is doing advocacy work.
[2655.14 --> 2664.88]  They maybe can, you know, not think about it as much because they're not defining direction for how we talk about our products.
[2665.40 --> 2665.52]  Right.
[2665.52 --> 2672.92]  I've been thinking about your athlete analogy because it definitely lines up to a certain extent where it starts to break down, especially with like an NBA player.
[2673.28 --> 2679.08]  It's like a lot of the places where they play, okay, there's contractual agreements and stuff, but it's like kind of over their head.
[2679.14 --> 2680.38]  And it's like, well, I landed here.
[2680.56 --> 2681.56]  I play here.
[2681.68 --> 2683.58]  I'm going to speak well of the place, maybe.
[2683.94 --> 2686.16]  I'm going to, but it's just like, this is where I play now.
[2686.20 --> 2687.34]  I'm going to go play my best game.
[2687.34 --> 2698.98]  Whereas, as, you know, contracted, self-governed entities, humans, but we are, it's like you, you're there because you want to be there, you know, 100%, et cetera.
[2699.68 --> 2709.76]  And so I think my point there is I think the mobility for a DevRel is even more fraught than it would be for like a professional athlete whose job is to play the game.
[2709.88 --> 2711.74]  Because your job is not just to play the game.
[2711.82 --> 2715.04]  It's actually to like pick what's good and represent what's good.
[2715.04 --> 2719.62]  People trust your opinion, your taste, your curation, your focus.
[2720.48 --> 2726.84]  And so I think mobility is troublesome because like if Lee was at five different businesses in five years.
[2727.12 --> 2727.52]  Yeah.
[2727.76 --> 2732.90]  And it's like, well, you know, are these all amazing or is it just like, you know, it's tough to hold a spotter.
[2733.08 --> 2739.90]  We know that in software, the best way to move up oftentimes is to not go vertically in your same org, but actually switch companies.
[2739.90 --> 2742.12]  You're going to get more money, more benefits, et cetera.
[2742.38 --> 2743.76]  It's the smarter play.
[2743.76 --> 2745.66]  But for DevRels, maybe that backfires.
[2746.34 --> 2747.50]  Well, there's two things there.
[2747.60 --> 2751.40]  One, because DevRel is such a public role, it's kind of hilarious.
[2751.66 --> 2754.78]  I didn't really think about it until I was actually involved with it.
[2755.00 --> 2761.76]  But like it's how would you discreetly talk about your job hiring process?
[2761.88 --> 2763.46]  I've talked to a bunch of people in DevRel.
[2763.82 --> 2764.94]  It's really hard to do.
[2765.20 --> 2767.88]  Like a lot of these companies talk to each other too.
[2767.88 --> 2774.76]  So they're going to know if you're interviewing at another company for the public spokesperson of that role.
[2774.94 --> 2775.10]  Right.
[2775.10 --> 2775.58]  Yeah.
[2775.66 --> 2775.94]  Good point.
[2775.94 --> 2777.60]  It's kind of obvious at that point.
[2777.72 --> 2785.34]  So it does make it tricky, I think, for DevRel leaders who are looking to move around depending on what level they're at at the company.
[2785.56 --> 2786.04]  It's a challenge.
[2786.04 --> 2786.72]  Yeah.
[2786.72 --> 2795.18]  This episode is brought to you by Honeycomb.
[2795.32 --> 2797.70]  Find your most perplexing application issues.
[2798.00 --> 2804.90]  Honeycomb is a fast analysis tool that reveals the truth about every aspect of your application in production.
[2805.36 --> 2808.72]  Find out how users experience your code in complex and unpredictable environments.
[2809.66 --> 2814.56]  Find patterns and outliers across billions of rows of data and definitively solve your problems.
[2814.56 --> 2816.48]  And we use Honeycomb here at Change.
[2816.52 --> 2820.34]  Well, that's why we welcome the opportunity to add them as one of our infrastructure partners.
[2820.88 --> 2828.18]  In particular, we use Honeycomb to track down CDN issues recently, which we talked about at length on the Kaizen edition of the Ship It podcast.
[2828.44 --> 2829.12]  So check that out.
[2829.36 --> 2829.84]  Here's the thing.
[2830.06 --> 2833.32]  Teams who don't use Honeycomb are forced to find the needle in the haystack.
[2833.46 --> 2836.60]  They scroll through endless dashboards playing whack-a-mole.
[2836.84 --> 2839.86]  They deal with alert floods, trying to guess which one matters.
[2839.86 --> 2845.48]  And they go from tool to tool to tool playing sleuth, trying to figure out how all the puzzle pieces fit together.
[2845.88 --> 2852.12]  It's this context switching and tool sprawl that are slowly killing teams' effectiveness and ultimately hindering their business.
[2852.54 --> 2859.30]  With Honeycomb, you get a fast, unified, and clear understanding of the one thing driving your business.
[2859.56 --> 2859.98]  Production.
[2860.50 --> 2862.96]  With Honeycomb, you guess less and you know more.
[2862.96 --> 2868.56]  Join the swarm and try Honeycomb free today at honeycomb.io slash changelog.
[2868.72 --> 2872.18]  Again, honeycomb.io slash changelog.
[2872.46 --> 2874.28]  And by our friends at Retool.
[2874.62 --> 2881.20]  Retool helps teams focus on product development and customer value, not building and maintaining internal tools.
[2881.60 --> 2884.44]  It's a low-code platform built specifically for developers.
[2885.02 --> 2886.14]  No more UI libraries.
[2886.66 --> 2888.16]  No more hacking together data sources.
[2888.52 --> 2890.86]  And no more worrying about access controls.
[2890.86 --> 2899.32]  Start shipping internal apps to move your business forward in minutes with basically zero uptime, reliability, or maintenance burden on your team.
[2899.62 --> 2901.40]  Some of the best teams out there trust Retool.
[2901.52 --> 2908.68]  Brex, Coinbase, Plaid, DoorDash, LegalGenius, Amazon, Allbirds, Peloton, and so many more.
[2909.08 --> 2913.74]  The developers at these teams trust Retool as their platform to build their internal tools.
[2913.90 --> 2915.20]  And that means you can too.
[2915.58 --> 2916.38]  It's free to try.
[2916.38 --> 2918.56]  So head to Retool.com slash changelog.
[2918.70 --> 2922.28]  Again, Retool.com slash changelog.
[2922.28 --> 2946.46]  So, Lee, obviously, it's been a journey for the role.
[2946.62 --> 2947.56]  It's been a journey for you.
[2947.56 --> 2952.28]  And I think, you know, one thing that we're very keyed in on is listeners first.
[2952.64 --> 2954.40]  So listeners, hey, we love you, by the way.
[2954.88 --> 2963.54]  But we do this show because we know our listeners have a curiosity for certain aspects of the process of creating software, the direction it goes in the future, how to innovate, how to iterate.
[2964.26 --> 2966.72]  But we also have to adopt great tooling.
[2967.20 --> 2970.88]  And as part of that, we have to listen to certain people, a.k.a. DevRolls and folks like you.
[2971.28 --> 2974.04]  The question that becomes is how do we trust those people?
[2974.18 --> 2976.18]  How do we trust who we're hearing from?
[2976.76 --> 2979.86]  I don't even know what question to really ask you, but more like just a layer of trust.
[2979.98 --> 2982.34]  How do we trust folks like you?
[2982.70 --> 2984.56]  I mean, how does that work?
[2984.72 --> 2989.54]  Well, when you're hired to say a thing and then you say the thing and then it's like, well, are you just saying that because you're hired?
[2989.88 --> 2990.20]  Precisely.
[2990.34 --> 2990.78]  Or not.
[2990.78 --> 2993.94]  And I think good DevRolls, they earn trust.
[2994.16 --> 2996.50]  And other ones were like, I don't know if I trust this person.
[2996.64 --> 2999.28]  So your angle into that, Lee, let us know what you're thinking.
[2999.84 --> 3000.04]  Yeah.
[3000.26 --> 3008.18]  There's an observed pattern of someone in DevRel where you can kind of get an understanding of, is this somebody that I can trust?
[3008.56 --> 3012.92]  And I think it comes back to, are you willing to admit when you're wrong?
[3013.44 --> 3014.44]  Are you publicly?
[3014.44 --> 3019.48]  Are you willing to admit when your product might not be the best case for something?
[3019.70 --> 3024.50]  And are you willing to advocate for something else if necessary?
[3025.10 --> 3026.80]  And that last one is painful.
[3027.12 --> 3034.76]  Like it's painful for a company to think that you would hire somebody that might not always preach for your product.
[3034.92 --> 3043.06]  But great DevRel teams with great founders who have trust in their DevRel teams understand that the best product should win.
[3043.06 --> 3050.34]  If our product isn't better, I don't want somebody selling me snake oil for something that's supposed to solve all of my problems.
[3050.34 --> 3053.98]  That's disingenuous to the company itself and to the product itself.
[3054.32 --> 3064.48]  So something that I've noticed really great DevRel leaders and teams do is they are very aware of when you should use the product.
[3064.48 --> 3069.02]  And they can also give just as compelling of a pitch of when you should not use the product.
[3069.02 --> 3079.22]  Because so much of software evaluation and purchasing comes down to knowing what trade-offs you're making and knowing the constraints of how you're building your system.
[3079.76 --> 3087.54]  And if you arm developers with the confidence to know when it's the right tool and when it's not the right tool,
[3087.72 --> 3091.58]  you're passing along the knowledge they need to advocate for your tool.
[3091.58 --> 3095.44]  This has been observed with Gishermo in particular.
[3095.72 --> 3096.70]  He's been on Finder's Talk.
[3096.78 --> 3097.66]  He's been on this show before.
[3097.76 --> 3098.84]  He's been on JS Party before.
[3099.22 --> 3102.78]  We've had many conversations with him way before it was even for sale.
[3102.86 --> 3103.66]  Before it was even Zite.
[3104.04 --> 3105.98]  Like LearnBoost days back in the day.
[3106.18 --> 3108.40]  Early tools for Gishermo, for example.
[3108.62 --> 3109.30]  Mongoose, right?
[3109.72 --> 3109.92]  Yeah.
[3110.06 --> 3113.02]  I mean, just lots of different history with Gishermo.
[3113.18 --> 3113.58]  And I think...
[3113.58 --> 3114.38]  Hyperterminal.
[3114.74 --> 3115.14]  Hyperterminal.
[3115.24 --> 3116.52]  Yeah, that was Zite days.
[3117.26 --> 3118.00]  Still around.
[3118.14 --> 3118.70]  Still being used.
[3118.78 --> 3119.30]  Still out there?
[3119.42 --> 3119.70]  Yeah.
[3119.70 --> 3121.68]  I thought that might have been pre-Zite, but okay.
[3121.82 --> 3122.20]  Fair enough.
[3122.32 --> 3122.50]  Yeah.
[3122.86 --> 3125.72]  It was early days of Zite.
[3125.98 --> 3128.06]  I think maybe even early next days even too.
[3128.18 --> 3129.20]  It was a while back.
[3129.72 --> 3133.90]  Point is, I think he's a great example of a founder who has done the role.
[3134.14 --> 3134.46]  Yes.
[3134.74 --> 3135.76]  Just by nature.
[3136.10 --> 3137.02]  He wasn't even dev role.
[3137.06 --> 3138.60]  He was just founder.
[3138.78 --> 3141.08]  He was just idea creator, inspirer.
[3141.36 --> 3141.86]  Follow me.
[3141.96 --> 3142.70]  This is the way to go.
[3142.78 --> 3143.76]  I believe in this way.
[3144.40 --> 3145.50]  You know, that kind of thing.
[3145.50 --> 3150.70]  And many people have obviously followed him through to make Vercel the success it is today,
[3150.96 --> 3153.42]  to employ you and many others to do the role you do.
[3153.60 --> 3155.98]  A lot of engineers making Vercel what it is today.
[3156.54 --> 3161.60]  I think Gishermo is a great example of someone who has done the role by necessity and then
[3161.60 --> 3164.20]  also been able to pass that trust torch on to you all.
[3164.78 --> 3166.18]  That's challenging.
[3166.32 --> 3167.62]  It's not like you get that every day.
[3167.62 --> 3173.72]  But Gishermo began as a developer turned CEO, which is also, I guess, more common these
[3173.72 --> 3174.06]  days.
[3174.32 --> 3179.38]  But I would say that Gishermo is more of a unique individual, let's just say.
[3179.50 --> 3179.70]  Yeah.
[3179.84 --> 3182.96]  Very unique because he's so capable and was so well spoken as well.
[3183.42 --> 3189.02]  A developer to CEO, but also a developer who really understands how to build a great product.
[3189.30 --> 3195.60]  And the core theme of DevRel I talked about of being empathetic, I think he exemplifies as
[3195.60 --> 3196.00]  well too.
[3196.06 --> 3196.28]  Totally.
[3196.28 --> 3199.68]  You'll see him in the trenches talking to customers.
[3199.78 --> 3200.70]  How can we make this better?
[3201.00 --> 3205.62]  We want to know your feedback on how we can make this product the best it possibly can
[3205.62 --> 3205.78]  be.
[3205.84 --> 3208.44]  I think that transcends throughout the entire company.
[3208.60 --> 3213.12]  We want our entire company to be thinking customer first.
[3213.46 --> 3218.46]  How do we do everything at Vercel in the service of our customers being successful?
[3219.02 --> 3220.52]  That word success keeps coming up.
[3220.76 --> 3225.96]  And I think that's kind of core because you said the reason why you got into it was because
[3225.96 --> 3233.34]  you saw lack of documentation, lack of education to enable developers to have success on the front
[3233.34 --> 3233.60]  end.
[3234.14 --> 3236.68]  And that obviously is just sort of part of it.
[3236.72 --> 3238.98]  But this word success means like you care.
[3238.98 --> 3243.22]  And this role is very similar in nature to sales.
[3243.70 --> 3245.82]  If sales is done right, it's to help.
[3246.44 --> 3252.00]  One of the things I get to do here in organization is I get to really help us partner with the right brands.
[3252.12 --> 3254.44]  That means selling ads basically.
[3254.58 --> 3255.66]  It's a very basic premise.
[3255.66 --> 3259.28]  But really, it's like choosing the right horses to attach ourselves to.
[3259.38 --> 3260.22]  It's maybe a bad analogy.
[3260.34 --> 3262.08]  Jared, help me out if I'm butchering this.
[3262.20 --> 3265.96]  But there's certain brands we want to work with and there's certain brands we don't because we see where they're
[3265.96 --> 3270.62]  trying to go, what they're trying to do for developers, the kind of future they care about, the way they involve
[3270.62 --> 3271.46]  themselves in the community.
[3271.72 --> 3272.90]  And we do choose.
[3273.00 --> 3274.72]  We say no often.
[3275.28 --> 3281.76]  And it's back to that, you know, I can trust a dev rel if they know when to tell me it's the right thing to use or not.
[3281.82 --> 3287.50]  But this idea of success really is rooted at desiring to help people, which is crucial.
[3288.22 --> 3289.38]  Crucial to having trust.
[3289.52 --> 3294.48]  If I can trust Lee to be someone who wants to help me, maybe you should make that shirt.
[3294.78 --> 3295.70]  Lee can't help me.
[3296.36 --> 3299.78]  You know, just truly want to help me because that's what it comes down to.
[3299.78 --> 3311.06]  Because like in our business, when I speak to the different folks who want to part with our brand and do what we do and share their brand with our audience and whatnot, it comes down to can we actually help them?
[3311.16 --> 3311.98]  Do we want to help them?
[3312.12 --> 3314.54]  Are they, you know, do they speak the right way?
[3314.64 --> 3316.28]  You know, can we actually truly help them?
[3316.74 --> 3319.84]  And really, it's like if we can help them, I want to help them.
[3320.06 --> 3320.54]  You know what I mean?
[3321.08 --> 3322.80]  And it's I didn't say sell them.
[3322.80 --> 3323.48]  I said help them.
[3323.62 --> 3325.64]  If we can help them, I want to help them.
[3326.20 --> 3328.94]  You know, and the word help and success kind of go hand in hand there.
[3329.32 --> 3329.44]  Yeah.
[3329.78 --> 3330.80]  Help them succeed.
[3331.20 --> 3331.36]  Yeah.
[3331.92 --> 3339.36]  So obviously this desire to, this empathetic desire to help others succeed in a specific domain is key here to being a dev rel, a good dev rel.
[3339.46 --> 3342.00]  What are other things you look for now that you're probably hiring dev rels?
[3342.20 --> 3347.42]  If you're out, if a listener is out there thinking, ah, this sounds like a pretty cool thing to do.
[3347.70 --> 3350.90]  Lots of fame and fortune that we had.
[3351.16 --> 3351.42]  Sure.
[3351.52 --> 3352.64]  Maybe I could be a dev rel.
[3352.72 --> 3353.76]  What are the traits?
[3353.82 --> 3356.20]  I assume some sort of like technical writing skills.
[3356.20 --> 3360.14]  Like give us some of the basics of like, well, you would be a good dev rel if.
[3360.62 --> 3360.90]  Yeah.
[3360.94 --> 3361.38]  I like that.
[3361.44 --> 3362.02]  Jeff Foxworthy.
[3362.16 --> 3363.36]  You might be a dev rel if.
[3363.54 --> 3363.94]  There you go.
[3364.12 --> 3364.34]  Yeah.
[3364.34 --> 3371.42]  You mentioned technical writing and I would rank that up there as, as one of the most important things close to empathy.
[3371.42 --> 3384.16]  Specifically it's writing and communication because so much of our role is interfacing virtually and in person through written communication.
[3384.16 --> 3390.90]  That the more succinctly, the more clear you can deliver your message, the better off you're going to be.
[3391.00 --> 3392.60]  And that's just in the comms.
[3392.66 --> 3394.80]  That's not even talking about the educational material.
[3394.80 --> 3406.94]  Like if you're, if you're creating educational material, courses, blog posts, video scripts, any of this stuff, the more well written and polished and clear that can be, the better your content's going to be.
[3407.12 --> 3420.28]  So the, the written element is extremely important because it usually great writing usually comes from great thinking and good refined thoughts and working through the, the drafts that maybe weren't as good.
[3420.28 --> 3422.56]  So that's something I definitely look for a lot.
[3422.84 --> 3426.32]  An up and coming one is people who are great with video.
[3426.84 --> 3441.58]  I think in the past video didn't play as much of a role in dev rel positions, but video is so important to how the world works today that those who have been involved with some aspect of video succeed pretty well.
[3441.74 --> 3445.76]  It's definitely something that can be learned, but it's, it's something to look for as well too.
[3445.76 --> 3455.26]  I think with engineering and with being a developer, it's a desire to want to learn and explore new tools.
[3455.26 --> 3462.18]  That is a good fit for developers, like in wanting to dive in a little bit further than just the surface level.
[3462.28 --> 3463.80]  You try out some new tool.
[3464.26 --> 3464.44]  Wow.
[3464.48 --> 3468.98]  This seems really interesting, but why did they make this choice?
[3468.98 --> 3471.30]  And like, why is it set up in this way?
[3471.30 --> 3482.18]  Like going a step further so that you have enough understanding that you can relay back the value to others who are curious more than just the tagline, more than just the boilerplate.
[3482.26 --> 3484.06]  Like, tell me really why it matters.
[3484.64 --> 3486.56]  Those are a couple of things I look for.
[3487.42 --> 3493.06]  As you've been talking about this, I was reminded of our conversation with Jessica Kerr, who's dev rel now at Honeycomb.
[3493.06 --> 3498.42]  And she was mentioning some pitfalls or blind spots dev rels have, specifically one that she mentioned.
[3498.52 --> 3499.82]  I'm curious if this resonates with you.
[3499.90 --> 3511.00]  I wonder if you have others as well, is that they rarely go through, for instance, the purchasing process of their product or service because they have staff accounts, right?
[3511.00 --> 3517.34]  And a lot of times your first run experience actually is, like, how do I actually onboard, right?
[3517.34 --> 3522.30]  My onboard experience is my experience first time on, unless we have free trial, et cetera.
[3522.40 --> 3523.18]  Even that's part of it.
[3523.50 --> 3533.76]  And she said people who work in this domain, they should, like, put their credit card into the website and, like, just purchase an account because now they have empathy with the people who have to do that.
[3534.08 --> 3539.26]  Whereas you're used to having this, like, staff account that's kind of, like, goes through this other subsection.
[3539.36 --> 3540.48]  That was one that she mentioned.
[3540.48 --> 3557.44]  The other one that I think happens, but I'm not doing it, but I would imagine happens, is, like, you spend most of your time building toy apps, experiments, examples, and can live in that land of, like, throwaway things versus, like, big products that would be built with a tool.
[3557.98 --> 3559.62]  So those are two that I thought of.
[3559.66 --> 3561.08]  Is there anything, first of all, do those resonate?
[3561.22 --> 3566.52]  And then secondly, are there other areas where dev rels can be blinded to what their customers are actually doing?
[3567.30 --> 3568.98]  Yeah, I love this topic.
[3568.98 --> 3572.44]  And that first one on billing is so accurate.
[3572.76 --> 3578.76]  Like, you just reminded me that after this, I'm going to go spin up a new Vercel account and throw my credit card on there.
[3578.82 --> 3579.18]  There you go.
[3579.18 --> 3588.80]  Because, yeah, it's the little errors you might get with a billing message that can really, really destroy customer trust.
[3589.32 --> 3589.56]  Yeah.
[3589.78 --> 3591.00]  Because that's such a...
[3591.00 --> 3592.34]  Or stop them dead in their tracks.
[3592.58 --> 3592.84]  Yes.
[3592.84 --> 3593.04]  Right.
[3593.56 --> 3593.90]  Yes.
[3594.14 --> 3595.10]  That's a great one.
[3595.18 --> 3596.10]  I love that one.
[3596.10 --> 3610.34]  I think that to combat your point about, you know, maybe some developer advocates are building a lot of Hello World starter applications, not really getting into the larger applications.
[3610.34 --> 3619.26]  A good way to offset this, I've found, is I try to make a point of spending time talking to our largest customers.
[3619.80 --> 3623.32]  And these are people who are building really large applications.
[3623.80 --> 3630.68]  Their needs and pains are quite different than the rest of the customers on our platform.
[3630.68 --> 3635.66]  You know, they're an order of magnitude in difference in how they construct their app.
[3635.74 --> 3639.08]  They might have an order of magnitude more engineers as well, too.
[3639.74 --> 3646.68]  And you just, you uncover different insights that might be rooted back in fundamental product deficiencies elsewhere.
[3647.00 --> 3655.44]  So, for example, maybe one of your really large customers is struggling with a specific way of how they want to organize their code base.
[3655.44 --> 3673.32]  And what you realize in really digging into this customer feedback and getting involved in the actual product experience when you're out in the field talking to these people is that there's a common thread between all of this other feedback you've been hearing about the getting started experience.
[3673.32 --> 3683.20]  But because you weren't paying attention to the day 500 experience and you were only looking at the day two experience, you might have missed that along the journey.
[3683.20 --> 3691.40]  So, you can't take for granted or lose track of those customers who have grown with you and been around for a while.
[3692.04 --> 3701.48]  And part of that is a good relationship between the developer relations team and then what teams, a customer success team or whatever you want to call that in an organization.
[3701.72 --> 3707.30]  But the team responsible for interfacing with the actual customers, the accounts that they manage.
[3707.76 --> 3711.66]  Jared, something you had said there reminded me something else that we talked about Jessica with.
[3711.66 --> 3717.30]  And then, Lee, in the first segment, you mentioned DevRel teams and which org they're under.
[3717.92 --> 3722.76]  And so, something that Jessica talked about was that her org is under marketing.
[3723.06 --> 3733.06]  And then in the first segment, you mentioned how that can kind of play a role in how they are successful, I assume, to some degree with their roles or their mission for the brand.
[3733.56 --> 3736.52]  How do you – it seems like you know what you're talking about, basically.
[3736.52 --> 3738.80]  You know how to operate an organization.
[3738.92 --> 3743.22]  You know how to direct an organization that's doing DevRel for a Vercel or a large organization like that.
[3743.22 --> 3754.90]  When it comes to setting up a DevRel organization, whether it's one person or many, let's just say tech-focused brands because, I mean, obviously healthcare might be different.
[3754.90 --> 3759.30]  But how do you – what are the right ways to organize the hierarchy?
[3759.64 --> 3760.62]  Do you put it under marketing?
[3760.72 --> 3761.48]  Do you put it under sales?
[3761.82 --> 3763.66]  How do you attach OKRs and KPIs?
[3763.76 --> 3774.78]  Like how do you – we talked about metrics a little bit, but how do you set it up right so that listeners of the show do trust them and products can get adopted and be useful and enable success and help in all these fun things we're talking about?
[3774.88 --> 3775.62]  How does that work?
[3775.68 --> 3776.40]  How do you make it work?
[3776.40 --> 3780.46]  Yeah, I wish there was a great, simple answer for this.
[3780.76 --> 3788.02]  Unfortunately, there's not really because I think my next question, if following up to this, would be how large is the company?
[3788.32 --> 3789.88]  What's the current focus?
[3790.42 --> 3794.34]  Like is the current focus they're just getting started with product market fit?
[3794.48 --> 3798.46]  Is the current focus they're just getting into enterprise sales?
[3798.72 --> 3804.42]  Are they already at 100 million ARR and now they're trying to move into the next phase of the company?
[3804.42 --> 3809.76]  Like all those different phases of the company's lifespan might require different outreach.
[3809.92 --> 3816.78]  So for context, when I joined Vercel, I was employee 34 and we were a much different company than we are today.
[3817.08 --> 3822.80]  And the type of outreach I was doing is a little bit different today than it was at the start.
[3822.88 --> 3825.80]  But the core values are all the same.
[3826.08 --> 3826.16]  Yeah.
[3826.16 --> 3830.18]  So if you hire the right people, which that's kind of hand wavy, right?
[3830.22 --> 3849.90]  But if you hire people that are empathetic, that are great writers, that are passionate about tech, then a lot of that can translate back to, well, it doesn't really matter like what org or what KPI, because they're going to thrive in whatever environment or what stage the company is at.
[3849.90 --> 3856.36]  So that's some of the things that organizations can think about with regards to successful DevRel.
[3856.66 --> 3858.90]  What about the content specifically?
[3859.14 --> 3863.00]  Like if you were going to define like what's a good piece of promotional content?
[3863.16 --> 3867.06]  Surely you've had lots of wins, lots of losses, things that have like blown up, things that have been ignored.
[3867.82 --> 3867.88]  Yeah.
[3867.88 --> 3877.46]  Are there attributes of good content that DevRel people can create that's like sticky or interesting or viral that you found is like reproducible?
[3878.36 --> 3886.48]  Yeah, I think I'll segment this into two buckets of content because I've seen DevRel get involved in both buckets.
[3887.06 --> 3891.00]  Let's say on one hand, it's the traditional marketing content.
[3891.36 --> 3892.72]  This is like the press release.
[3892.84 --> 3894.44]  This is the announcement of the thing.
[3894.44 --> 3897.76]  It's more targeted towards a larger audience.
[3898.24 --> 3901.90]  And then there's the engineering developer focused content.
[3902.40 --> 3912.94]  And this is targeted directly at the individual developers, whether some kind of how-to or tutorial or guide or some kind of explainer on how something works.
[3913.84 --> 3919.00]  The separation of audiences there is really important on what makes the content great.
[3919.00 --> 3927.02]  Because if we start talking with the engineering content, developers don't want you to skimp on the details.
[3927.26 --> 3931.64]  They want to know behind the scenes what is making this thing work.
[3931.76 --> 3934.18]  Otherwise, it feels like a sales pitch.
[3934.26 --> 3935.36]  It feels like a marketing pitch.
[3935.50 --> 3940.64]  Like you're telling me about this thing, but you're not giving me any of the underworkings of how the system works.
[3940.76 --> 3941.94]  Now I have questions.
[3942.32 --> 3944.60]  Now I don't feel like you're being truthful with me.
[3944.64 --> 3946.34]  This seems too good to be true, right?
[3946.34 --> 3950.54]  If you read something and it's like, hmm, this feels like a silver bullet.
[3950.66 --> 3954.66]  Like this feels like there were no trade-offs discussed at all.
[3954.72 --> 3955.68]  It's only good.
[3955.76 --> 3958.20]  Then it's probably not a very good engineering blog post.
[3958.62 --> 3963.26]  Like some of the best engineering blog posts actually document that, you know, here's what worked.
[3963.64 --> 3966.58]  Here's what didn't work and why it didn't work.
[3966.66 --> 3969.26]  And here's what we learned from it and actually improved on that.
[3969.54 --> 3972.54]  And that's, I think, how you can do engineering content really well.
[3972.74 --> 3974.14]  Focus for individual developers.
[3974.14 --> 3980.38]  Then there's also the press release announcement style material.
[3980.58 --> 3987.80]  And I think where DevRel can play a role in that is making sure you're doing justice to your community.
[3988.26 --> 3992.14]  So let's say you're announcing a new feature for your product, right?
[3992.70 --> 4000.42]  In how you talk about this feature, you should try to tie it back to the actual customers using it, the community involved around it.
[4000.62 --> 4003.42]  Maybe they've surfaced some feedback that's helped make it successful.
[4003.42 --> 4011.00]  Maybe you've actually surfaced this with them ahead of time so you can get feedback on the announcement or on the feature that you're launching.
[4011.84 --> 4020.76]  And I think the DevRel persona can help bring the lens of maybe this is a first time viewer of the product.
[4020.94 --> 4022.60]  Maybe this is somebody really advanced.
[4022.60 --> 4027.66]  How do we make sure this content lands with all of the developers in our community?
[4029.02 --> 4032.94]  Curious about specific social platforms and what you all are investing in.
[4033.06 --> 4035.10]  Like, is Instagram, you know, we have them.
[4035.18 --> 4036.56]  They're all stealing each other's features.
[4036.92 --> 4037.44]  You know, are you?
[4037.52 --> 4037.74]  So many.
[4038.10 --> 4040.20]  Are you going heavy into TikTok?
[4040.40 --> 4041.46]  Are you ignoring this?
[4041.54 --> 4046.36]  Are you, you know, what as a team do you guys look at and say, here's where we're going to reach our people?
[4046.38 --> 4047.14]  Because you got to reach them.
[4047.14 --> 4047.42]  Yeah.
[4047.64 --> 4048.04]  Yeah.
[4048.24 --> 4048.58]  Yeah.
[4048.58 --> 4049.06]  100%.
[4049.06 --> 4053.78]  I feel like we're involved in, you know, almost all the major social platforms.
[4053.78 --> 4060.48]  And I'll say that I do think that video is just continuing to get more and more popular, which I think is why TikTok is so popular.
[4060.48 --> 4067.62]  It's interesting, though, the type of content that does well on different platforms is quite different.
[4067.78 --> 4072.80]  Like, people don't want to see the YouTube video just copy pasted and reposted on TikTok.
[4072.98 --> 4076.42]  It needs to feel like it's built for that platform.
[4077.06 --> 4087.32]  And strangely enough, I don't know if this is a generational thing, but like some of the content that does best on platforms like TikTok, like it feels like it was just shot on your iPhone.
[4087.54 --> 4087.76]  Right.
[4087.76 --> 4089.50]  It's actually better when it's just shot on your iPhone.
[4089.62 --> 4090.70]  It's not super professional.
[4090.94 --> 4098.68]  It's not like they don't want to see the super polished press release style, like announcement keynote video.
[4098.82 --> 4101.86]  They want to see Lee, you know, doing a dance to a song.
[4102.44 --> 4102.46]  Like.
[4103.32 --> 4103.72]  Gotcha.
[4103.82 --> 4104.56]  You doing that stuff?
[4105.00 --> 4105.40]  No.
[4106.12 --> 4107.84]  They want to see it, but I'm not giving it to them.
[4108.22 --> 4109.70]  Well, I like to see that as well.
[4110.12 --> 4111.88]  Nobody wants to see me doing dances.
[4111.88 --> 4115.42]  I have seen some people do it well.
[4115.62 --> 4121.14]  Some people who use TikTok as an educational tool and just, and I think that's what it comes back down to.
[4121.22 --> 4127.70]  Like find your audience, whether they're on TikTok or LinkedIn or in Facebook, the black hole of developers.
[4127.70 --> 4129.38]  There's so many developers on Facebook.
[4129.38 --> 4131.24]  They're just waiting for you to talk to them.
[4131.34 --> 4134.92]  But a lot of people don't engage with those, with those groups.
[4134.92 --> 4140.46]  And as long as you make educational resources, like they will listen.
[4140.68 --> 4144.10]  Like, cause all developers are always trying to learn something new.
[4144.22 --> 4150.30]  And even experts want to hear something explained like a beginner can understand it.
[4150.80 --> 4151.70]  Wow said.
[4152.18 --> 4156.30]  There's somebody out there that's, that's thinking, uh, I'm a dev rel.
[4156.30 --> 4161.34]  I've got my singular org or I want to evolve my organization.
[4161.34 --> 4165.40]  I want the business side to help me evolve it.
[4165.48 --> 4168.90]  Where do you get, like, what resources do you look to?
[4169.06 --> 4171.40]  Blog posts, YouTubes, whatever it might be.
[4171.88 --> 4172.44]  Talks.
[4173.02 --> 4175.36]  What resources do you use to kind of become wise?
[4175.46 --> 4176.58]  I think you're pretty wise.
[4176.84 --> 4177.66]  Where do you get your wisdom?
[4178.18 --> 4184.76]  Where can you point some of the folks who might want to evolve or upgrade their dev organizations to become a bit more like yours?
[4184.76 --> 4187.26]  Or just have some of the attributes you've been talking about today.
[4188.02 --> 4196.54]  Yeah, I, I'm very fortunate to have people on the Vercel team, uh, who've, who've helped our organization grow and provide a lot of good feedback.
[4197.00 --> 4206.72]  And I think outside of the Vercel team, I try to connect with other, other folks leading dev rel at developer focused companies.
[4206.72 --> 4212.88]  So my recommendation for people wanting to get kind of a pulse on how dev rel is going is to connect with the individuals.
[4212.88 --> 4222.88]  It's, it's more about the people than it is the, the brand or the company, because that's where you're going to gain insights on how their worldview is shaping, how they interface with their communities.
[4223.44 --> 4236.74]  So I would find some of the tools that you're interested in, maybe the tools that you use, uh, that help make your, your life easier and, and see who those developers are who are leading the communities there and DM them.
[4236.74 --> 4241.26]  So, you know, you know, they might be more open to your, uh, your outreach than you might imagine.
[4241.46 --> 4241.88]  There you go.
[4242.30 --> 4243.68]  Are your DMs open?
[4243.86 --> 4244.22]  They are.
[4244.30 --> 4244.44]  Yeah.
[4244.62 --> 4245.00]  There you go.
[4245.26 --> 4251.92]  I, I have people DM me about all different types of stuff and, you know, it's, I, I believe it's, it's helpful.
[4251.92 --> 4261.18]  You know, it's, I, it can be, I acknowledge it can be difficult for certain people to have DMs open just due to the, the way the internet is.
[4261.38 --> 4268.74]  So it doesn't work for everyone, but yeah, it's a good venue for feedback sometimes.
[4269.52 --> 4269.62]  Gotcha.
[4270.28 --> 4272.22]  What about, uh, things unsaid?
[4272.22 --> 4287.92]  I'm sure we've talked a lot about the, the process, the history, you know, the do's and don'ts, you know, code smells for lack of better terms of good and bad organizations slash individuals you can trust or not trust and reasons you can't.
[4288.48 --> 4293.44]  Is there anything we haven't asked you that you're like, man, I really wish I could talk about this before we cool up the show.
[4294.16 --> 4296.44]  Um, I think, I think y'all have done a great job.
[4296.64 --> 4298.18]  This has been, this has been really fun.
[4298.42 --> 4301.38]  Lots of in, uh, thought provoking questions.
[4301.38 --> 4304.26]  I don't usually get to talk about DevRel in the meta sense.
[4304.60 --> 4304.62]  Yeah.
[4304.72 --> 4309.68]  So it's been interesting to reflect on why we do the things we do.
[4309.86 --> 4310.58]  There you go.
[4310.80 --> 4311.14]  Well said.
[4311.52 --> 4320.38]  One thing we didn't talk about, which we want to talk about, but we'll probably have to do it on JS Party is I want to talk more about next JS, where it's at, where it's headed.
[4320.66 --> 4320.94]  Yeah.
[4321.20 --> 4323.38]  And so we completely sideline that.
[4323.48 --> 4324.76]  That's a big part of what you do.
[4325.06 --> 4329.72]  And so we'll have to have you on JS Party where you're going to hit the audience right on the head.
[4329.72 --> 4330.02]  Oh yeah.
[4330.02 --> 4334.52]  Don't actually hit our audience on the head, but you know, metaphorically, the nail and the hammer.
[4334.68 --> 4335.04]  The nail head.
[4335.18 --> 4335.66]  He's a hammer.
[4335.78 --> 4339.82]  And so I'll have to bring you on JS Party to talk about that so we can give it its full, its full time.
[4339.90 --> 4340.18]  Sound good?
[4340.44 --> 4341.16]  Yeah, that'd be great.
[4341.32 --> 4341.96]  I think it'd be fun.
[4342.36 --> 4342.68]  Cool.
[4343.38 --> 4343.62]  Cool.
[4344.64 --> 4349.66]  Well, Lee, thank you so much for your time, your leadership, your wisdom, and just showing up here and just being real.
[4349.76 --> 4350.66]  We really appreciate that.
[4351.00 --> 4351.74]  Thank you so much.
[4352.02 --> 4352.22]  Yeah.
[4352.50 --> 4352.96]  Thank you.
[4353.28 --> 4353.94]  This has been fun.
[4353.94 --> 4357.82]  All right.
[4358.00 --> 4359.50]  That is our show for this week.
[4359.50 --> 4361.84]  Now is a great time to subscribe.
[4362.28 --> 4366.44]  If you're new to the pod, head to changelog.fm for all the ways.
[4367.02 --> 4370.72]  And if you're a longtime listener, do us a solid and share the changelog with a friend.
[4371.18 --> 4377.84]  That is by far the best way you can help us help more people by sharing great stories and conversations like this one with Lee Rob.
[4377.84 --> 4387.62]  Speaking of good combos, I took my producer cap off and joined GoTime recently for a panel discussion on an episode titled The Myth of Incremental Progress.
[4388.10 --> 4391.92]  Here's a quick taste of that one where I'm encouraging cargo culting.
[4392.30 --> 4392.76]  Yes, I am.
[4393.28 --> 4398.76]  Sometimes you just have to follow the other person's path until you realize when it doesn't actually work for you.
[4399.12 --> 4402.30]  So I'm totally fine with like cargo culting, some sort of rule.
[4402.74 --> 4405.54]  I was going to say the law of the demeanor, but that one's too hard to explain.
[4405.60 --> 4406.18]  What's a very simple?
[4406.38 --> 4407.16]  Dry, right?
[4407.16 --> 4408.28]  Everybody can remember that one.
[4408.68 --> 4410.64]  We all get it wrong, but we don't remember the acronym.
[4411.52 --> 4417.32]  All of us here, I think, would all talk about how dry is not the best principle in many cases.
[4417.60 --> 4419.16]  I think I've heard you guys talk about that.
[4419.28 --> 4423.72]  But we didn't realize that until we had tried to dry the crap out of everything for a while.
[4423.92 --> 4425.32]  And then it came back to bite us.
[4425.54 --> 4431.20]  And so I think it's okay to go through that process of like I was saying in the post, go ahead and paint by numbers for a little while.
[4431.62 --> 4432.46]  Don't live there.
[4432.62 --> 4433.46]  Don't stay there.
[4433.46 --> 4441.08]  But until you can start to realize actually blue doesn't look great on the number four, a little bit lighter blue would look nicer there.
[4441.28 --> 4448.56]  You start to develop your taste, your experience, your own history of that working well in this context, not in that context.
[4448.56 --> 4450.64]  Then you don't need it quite as much.
[4450.64 --> 4452.62]  But I think, you know, we do need to start somewhere.
[4453.18 --> 4463.08]  And I think that a lot of these idioms, best practices, rules, clean architecture, whatever that means, those are decent starting places.
[4463.08 --> 4466.56]  That's from episode number 232 of GoTime.
[4467.14 --> 4470.44]  One listener called it the best episode they've heard in a long time.
[4470.70 --> 4472.72]  Another one called it the absolute worst.
[4473.38 --> 4475.56]  Maybe take a listen and let us know what you think.
[4475.96 --> 4479.54]  You can find it at gotime.fm slash 232.
[4480.08 --> 4487.20]  Changelog++ subscribers stick around for a quick bonus on Lego versus Legos that gets surprisingly gruesome.
[4487.20 --> 4491.84]  If you aren't a Plus Plus member, now's a great time to join.
[4492.28 --> 4494.76]  Drop the ads, get fun bonuses like this one.
[4494.90 --> 4499.60]  And we've even thrown in a free pack of Changelog stickers shipped straight to your door.
[4500.12 --> 4500.74]  Not bad, right?
[4501.20 --> 4509.24]  Thanks once again to Fastly for having our CDN back, to Breakmaster Cylinder for keeping our beat supply chain secure, and to you for listening.
[4509.64 --> 4511.58]  We appreciate you spending time with us each week.
[4512.12 --> 4512.92]  Okay, that's it.
[4513.00 --> 4513.76]  This one's done.
[4514.38 --> 4515.42]  We'll talk to you next time.
[4517.20 --> 4547.18]  We'll talk to you next time.
