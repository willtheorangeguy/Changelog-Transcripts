[0.00 --> 3.48]  We were kind of laughing about it and stuff, but I think we're going to see so many of
[3.48 --> 4.98]  these instances in the years ahead.
[5.14 --> 10.54]  And you made a point that I think we sometimes need to respond with a bit of empathy for
[10.54 --> 15.02]  the data scientists and AI engineers that are trying to create these because they're
[15.02 --> 18.78]  trying to do some pretty cutting edge stuff and mistakes are going to be made.
[19.20 --> 22.62]  And in the end, my understanding is nobody was hurt by this.
[23.08 --> 26.18]  Yeah, we need to both be critical and empathetic.
[26.36 --> 26.70]  Indeed.
[27.02 --> 27.50]  Fair enough.
[30.00 --> 31.00]  Fair enough.
[38.08 --> 44.50]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[44.76 --> 45.84]  and accessible to everyone.
[46.22 --> 46.98]  Subscribe now.
[47.14 --> 50.96]  If you haven't already, head to practicalai.fm for all the ways.
[51.34 --> 56.30]  Special thanks to our partners at Fastly for delivering our shows super fast to wherever
[56.30 --> 56.94]  you listen.
[57.28 --> 59.10]  Check them out at fastly.com.
[59.10 --> 61.54]  And to our friends at fly.io.
[61.86 --> 65.50]  We deploy our app servers close to our users and you can too.
[65.82 --> 67.72]  Learn more at fly.io.
[73.86 --> 78.58]  Welcome to another fully connected episode of the Practical AI podcast.
[79.08 --> 84.46]  This is where Chris and I keep you fully connected with everything that's happening in the AI community.
[84.46 --> 93.42]  We'll take some time to discuss the latest AI related news and dig into some learning resources to help you level up your machine learning game.
[93.94 --> 94.94]  I'm Daniel Whitenack.
[95.04 --> 97.60]  I'm a data scientist with SIL International.
[97.98 --> 103.70]  I'm joined as always by my co-host, Chris Benson, who's a tech strategist with Lockheed Martin.
[103.98 --> 104.64]  How you doing, Chris?
[104.86 --> 109.30]  I'm doing fine as we are recording this episode the day before Thanksgiving.
[109.30 --> 111.74]  Yes, U.S. Thanksgiving is tomorrow.
[112.56 --> 113.16]  That's right.
[113.44 --> 117.30]  And I know that we both have our day jobs and we just have nothing to do today, do we?
[117.40 --> 119.00]  We just there's not much going on.
[119.34 --> 119.78]  Right.
[120.00 --> 120.70]  If only.
[121.02 --> 121.62]  If only.
[121.84 --> 126.82]  We were talking beforehand and both of us are like, oh gosh, it's quite a busy day for the day before Thanksgiving.
[127.18 --> 127.78]  But you know what?
[128.18 --> 130.98]  We have a few minutes to talk about some fun stuff here.
[130.98 --> 132.32]  Yeah, exactly.
[132.94 --> 138.60]  I hope you've got your Tofurky or whatever you've got ready for tomorrow.
[138.82 --> 140.16]  I don't know what we'll have.
[140.34 --> 140.94]  Absolutely.
[141.22 --> 142.92]  Got myself some vegan bird here.
[143.24 --> 143.72]  Nice.
[143.96 --> 144.32]  Nice.
[144.52 --> 145.08]  I like it.
[145.20 --> 145.80]  I like it.
[146.76 --> 156.40]  So I'm going to maybe start with a story, Chris, because this is kind of what prompted some of my thoughts around this episode.
[156.40 --> 162.68]  So I live downtown in the town where we live here and there's a barber a couple blocks away.
[162.80 --> 167.16]  I go and get my haircut from this barber and he's big into crypto.
[167.52 --> 177.32]  Like when NFTs was really hot, he was like pouring like thousands of thousands of dollars into NFTs and he's got like all this stuff he's doing.
[177.46 --> 179.36]  Anyway, he lost a bunch of money with NFTs.
[179.36 --> 186.14]  But then the last time I went to go get my haircut, we were talking about this recent controversy around FTX.
[186.62 --> 192.82]  And just a sort of disclaimer, we're not going to be talking about crypto or Bitcoin this episode or blockchain.
[193.58 --> 201.94]  But it sort of prompted my thinking because basically for those that aren't aware, recently there is this crypto exchange, FTX.
[201.94 --> 221.72]  The founder, owner, Sam Bankman Freed, basically he was a kind of industry leader, well respected, but he's kind of turned into industry villain, lost most of his fortune and bankrupted a bunch of things like $32 billion plunge in value of this FTX exchange.
[221.72 --> 240.60]  And I was talking to a couple of people interested in this and like my barber, who maybe I don't know how much he is an expert, but thinking about how this is a major setback to those that are kind of promoting blockchain technology, crypto currencies, crypto, whatever.
[240.60 --> 252.96]  And it got me thinking, what sort of controversy or event could prove to be a major setback to the AI industry?
[253.72 --> 256.62]  Or is such a setback possible?
[257.08 --> 262.60]  So that's my first question to discuss on our day before Thanksgiving.
[263.08 --> 269.78]  I guess we can first give thanks that such an event maybe hasn't happened, although maybe smaller controversies have happened.
[269.78 --> 279.66]  Yeah, although before we kind of move fully over to the AI side from the crypto side, I happen to be staring at Sam Bankman Freed's Wikipedia page and I'm looking at his hair.
[280.16 --> 283.72]  And as you mentioned, the barber and stuff, there's got to be a joke there.
[284.04 --> 284.62]  That's all I'm saying.
[285.40 --> 285.80]  Yeah.
[286.14 --> 287.16]  There's got to be a joke there.
[287.60 --> 289.64]  So moving back over to AI.
[290.28 --> 296.12]  Well, I kind of feel like you've set me up because, you know, you're like, what could possibly go wrong with AI?
[296.12 --> 300.08]  And, you know, that would be a major setback to the industry.
[300.26 --> 300.46]  Yeah.
[300.54 --> 300.72]  Right.
[300.80 --> 302.82]  So not just like a bad thing.
[303.02 --> 306.98]  So there's certainly I think we can both say there's been bad things happen with AI.
[307.14 --> 307.88]  No doubt.
[308.14 --> 308.44]  Right.
[309.04 --> 309.48]  Absolutely.
[309.78 --> 314.78]  I think it would be the degree of badness potentially on a scale of bad things.
[315.10 --> 316.48]  What's the scale of badness?
[316.56 --> 317.24]  Zero to 10.
[317.32 --> 318.12]  What's at the 10?
[318.12 --> 324.92]  Well, a 10 is that you have significant loss of life that's caused by AI inference.
[325.18 --> 332.92]  And that would, and specifically because I work in the industry, I work in, I'm going to say unintentional loss of life by that.
[333.00 --> 334.08]  I'm not saying that there's AI.
[334.28 --> 335.16]  I should be careful.
[335.58 --> 343.34]  We don't have AI that's trying to, I'm just saying in the future sometime as things develop, I'm having to put in all the careful things.
[343.34 --> 353.66]  That yes, if there was AI in some industry and it resulted somehow in unintentional loss of life, then that would be a very bad thing.
[354.24 --> 354.38]  Right.
[354.50 --> 368.08]  So like if all the airlines started flying autonomously and there was an airliner that was flying autonomously and had significant loss of life or something like that.
[368.46 --> 368.60]  Right.
[368.84 --> 369.28]  Indeed.
[369.28 --> 380.20]  And when you really think about it, you know, that is something that people are already, you know, talking about for the future is AI running various types of vehicles, some of which are on the ground, some of which are in the air.
[380.50 --> 384.64]  And there, you know, there may be, there may be instances of that out there in the world.
[385.10 --> 388.24]  So yes, an airliner would be a big thing.
[388.86 --> 397.26]  I have to say, as we're talking about this kind of scenario, though, you know, I'm like totally recognizing the tragedy of that.
[397.26 --> 401.04]  I have always found it very interesting at the perspective.
[401.40 --> 409.04]  So in terms of loss of life, like we react to it depending on what the cause is in a different way.
[409.62 --> 411.48]  And so different, different results.
[411.62 --> 421.26]  There are some things that people look in the news and they hear about people dying and they kind of, it's remote from them and they kind of move on very quickly and go, oh, that's, that's.
[421.36 --> 422.98]  Or it's a story they've heard before.
[422.98 --> 424.96]  Or, yeah, that's a bad thing.
[424.96 --> 427.98]  And I'm sorry to hear that happen, but they kind of move on.
[428.08 --> 432.64]  And then there are other stories where they kind of get very emotional about it.
[432.88 --> 442.60]  I think that my suspicion is that should such a story in the future evolve where it was AI driven, that would, that would get to a whole new level of that.
[442.60 --> 448.34]  And I think the interesting thing for me psychologically is the fact that in all cases, it was the same loss of life.
[448.34 --> 451.66]  But the way we, the way we choose to react to it can vary.
[452.50 --> 457.60]  And so it's just an interesting, you know, psychological point from my standpoint.
[457.60 --> 464.22]  But I do think, I don't think it would stop AI, but I do think such an event would, would create a lot of pause.
[465.00 --> 481.78]  Yeah, I think it's, in my mind, it's not a ceasing of AI research or something like that, but more maybe a slowdown or intense regulation until like more reasonable regulation comes into play.
[481.78 --> 502.56]  We both talked quite extensively on the podcast about how government regulation and laws around, you know, algorithmic decision making and that sort of thing are lagging quite far behind the scale at which people are using this technology, which is sort of a scenario that would kind of create some awkwardness.
[502.56 --> 512.84]  One of the things that I wanted to bring up this episode, as we talk through this issue, is one of those awkwardnesses that has been created.
[513.02 --> 516.40]  And some people might see it as a bigger deal.
[516.52 --> 520.40]  Some people might see it as a really big deal or not a problem at all.
[520.82 --> 529.84]  So I don't think we're necessarily in a, like, we're not lawyers or in a position to, you know, weigh in on how this will all go.
[529.84 --> 535.40]  But I think we can present some sort of things that are happening right now.
[535.54 --> 542.96]  And the one that came to my mind was GitHub Copilot, which I'm actually a huge, I mean, I'm a huge fan of.
[543.06 --> 545.40]  So maybe I'm biased in this discussion.
[545.98 --> 551.48]  You know, we're not, as far as I know, we're not sponsored by GitHub Copilot or Microsoft or anything.
[551.88 --> 554.48]  But I do like the product and I use it.
[554.94 --> 556.88]  And I started, it is interesting.
[556.88 --> 561.94]  So I found this article and the article's title is GitHub Copilot isn't worth the risk.
[561.94 --> 567.44]  And it's sort of geared, I guess, towards like a CTO type.
[567.80 --> 573.96]  And the thought is like, should you allow your engineers to use GitHub Copilot?
[573.96 --> 590.04]  And it was kind of really, I mean, it was really good timing for me to see this article, I think, because literally a couple of the data scientists on my team were asking me, like, I think the week before, is it okay?
[590.24 --> 593.66]  Like, is there a policy against us using GitHub Copilot?
[593.66 --> 598.30]  Or is there any issue with us using GitHub Copilot, like in our day to day work?
[598.30 --> 598.74]  Right.
[598.86 --> 600.66]  So I had already been thinking about this.
[600.82 --> 612.66]  And one thing that struck me is I was already using GitHub Copilot without maybe realizing some of the implications around some of the things brought up in the article.
[612.88 --> 618.86]  But now, you know, people on my team are asking me, should they use GitHub Copilot?
[619.16 --> 622.36]  And so I thought that the timing was really good.
[622.36 --> 642.04]  I mean, one thing to acknowledge, I guess, here is if people aren't familiar with GitHub Copilot, it's sort of an AI enabled assistant that kind of is there in your IDE or your code editor with you and suggests certain blocks of code or converts comments into code.
[642.04 --> 650.72]  Like, you can say, you know, function that, you know, transforms this data into that and it'll kind of draft that out for you.
[650.78 --> 652.36]  And it's quite nifty.
[653.00 --> 661.62]  So, I mean, first acknowledgement is like GitHub Copilot is obviously very powerful and I would argue useful.
[662.42 --> 665.02]  Otherwise, you probably wouldn't be having this conversation.
[665.44 --> 666.20]  I would too.
[666.34 --> 667.48]  I like it personally.
[667.48 --> 680.62]  Like, I'll use it for my personal things and I really like it because especially if I go in and out of coding where I'm coding sometimes, but then I'll go periods of time where I'm not coding and things will slip.
[680.78 --> 686.32]  And it's a great way of kind of getting back into quick productivity by getting those suggestions.
[686.32 --> 690.44]  And often I'll see them and go, oh, yeah, oh, yeah, oh, yeah, do that, you know, select that and all that.
[690.68 --> 692.16]  So it's a great tool.
[692.16 --> 696.02]  Well, I will confess that to this day, I still am.
[696.54 --> 699.02]  I have this kind of discomfort with the idea.
[699.34 --> 706.22]  I think I think it's that open source mentality of like I don't think anyone and I'm not talking about the legality of it.
[706.22 --> 710.80]  I'm talking about the when people submit open source to GitHub.
[710.80 --> 719.06]  And if you look back in the long history of that, they do expect other people to use the code and adopt it and all that.
[719.06 --> 725.22]  But I think that kind of pervasive making a large company's, you know, infrastructure out of it.
[725.36 --> 728.54]  There's a discomfort that I've talked with other people about.
[728.92 --> 735.42]  And everyone kind of has this uneasiness about that, that in these conversations about that aspect of it.
[735.42 --> 737.30]  So I'm guilty of using it.
[737.38 --> 741.16]  I like it, but I'm never quite comfortable with it.
[741.82 --> 742.02]  Yeah.
[742.52 --> 742.72]  Yeah.
[742.72 --> 754.84]  I think that part of it, well, maybe not not feeling guilty, but what what are the what are the implications of it, which I think I've thought about a lot more over the last couple of weeks.
[754.84 --> 759.88]  And to, you know, spoil the ending, I'm still using GitHub Copilot.
[760.40 --> 764.32]  And I guess maybe during this episode, you can tell me if that's a wise decision or not.
[764.32 --> 774.32]  But the controversy or the recent sort of swell of of discussion around this, I think is based.
[774.60 --> 776.08]  I mean, there's a buildup to it.
[776.22 --> 790.52]  But on November 3rd, there was a lawyer that filed a class action lawsuit against GitHub, Microsoft and OpenAI related to GitHub Copilot.
[790.52 --> 804.86]  And the basic charge is that Copilot's suggestions aren't boilerplate or sort of novel, but they bear kind of unmistakable fingerprints of their original authors.
[804.86 --> 823.10]  And according to, you know, a lot of open source licenses, if you're not giving at least attribution to those copyright holders, even if it's an open source license, then you're in violation of the license.
[823.60 --> 823.68]  Right.
[823.78 --> 823.94]  Yeah.
[824.06 --> 825.42]  It's an interesting idea.
[825.42 --> 844.40]  The thing that I wonder when I hear that is that writing code is so structured, you know, that in a lot of cases you can have different programmers coding in a very, very similar style and maybe even selecting the same variable names and stuff like that.
[844.40 --> 859.94]  So, like, does that mean that it's actually pulling from someone's direct copyrighted code or if there are a thousand versions of the same function that all literally are named the same, you know, does that imply the same thing?
[859.98 --> 863.32]  And I don't know the answer to that, but it's an interesting conundrum.
[863.32 --> 885.72]  Yeah, Chris, I think what you were talking about, about when does code show unmistakable fingerprints of its original authors and when is it boilerplate?
[885.72 --> 897.08]  That in and of itself is, to me, it is a hard one to navigate, I think, because, you know, I was just having a discussion with my brother-in-law, Ed.
[897.22 --> 900.10]  Shout out if you're listening, which I don't think you do.
[900.58 --> 909.06]  But if you are listening, he's learning JavaScript and learning some front-end development and that sort of thing.
[909.06 --> 919.74]  And we had this discussion the other day because he's like, well, there's this piece of this app that I've used and I can see the code, right?
[919.88 --> 927.58]  And I'd like to just sort of take that little bit and modify it over here in my little app to do a similar thing.
[927.76 --> 930.72]  But it's basically the same thing, but slightly different.
[930.88 --> 933.80]  But how many ways can you write this for loop?
[933.80 --> 942.04]  I feel like I'm stealing from this guy and taking it, but it's basically the right way to write this loop and do the thing.
[942.22 --> 945.96]  So do I copy that over and modify it?
[946.14 --> 957.98]  I think in a normal sort of open source world, if you were copying things out or like integrating in certain libraries or something like that,
[957.98 --> 963.56]  like I say, there are kind of attribution elements to it.
[963.68 --> 970.46]  And there's like dependencies in terms of like how restrictive your license is versus the source license and all of that.
[970.56 --> 973.22]  And there's all sorts of things around that.
[973.30 --> 984.56]  But as an individual code writer or a programmer, you can navigate those things because it's not like you're taking code maybe from this project, right?
[984.56 --> 989.94]  X project and you can see the license and you do what the license tells you to do, right?
[990.06 --> 992.24]  Like you make that decision actively.
[992.48 --> 999.62]  But in GitHub Copilot, I'm in my VS code and I'm typing along and then boom, there's a block of code.
[1000.44 --> 1010.80]  I have no idea if that's verbatim from someone's repository or if that's like something unique that's like some morphing of various things together, right?
[1010.80 --> 1025.68]  So could that, I'm just curious, could that be solved if they added a feature that either specified it was from a specific source or explicitly disclaimed that it was inferenced code and not from a specific source?
[1025.68 --> 1026.08]  Potentially.
[1026.08 --> 1026.96]  Potentially.
[1027.24 --> 1041.74]  I think one, like the most foolproof workaround, I think, or solution is to train the model that you're using, using only explicitly permissive licensed code, right?
[1041.88 --> 1046.52]  So this is the stance that there's another offering called tab nine.
[1046.52 --> 1058.40]  And tab nine is specifically, in my understanding, trained on permissively licensed code, which would not have some of these same copyright issues.
[1058.66 --> 1060.66]  Like MIT versus GPL.
[1060.86 --> 1061.10]  Yeah.
[1061.30 --> 1067.14]  So I think the one that's been called out a lot with GitHub Copilot is GPL.
[1067.76 --> 1073.86]  So there's, I'm just looking at a tweet here from Tim Davis at Doc Sparse.
[1073.86 --> 1087.90]  He, I think this is one of the ones that originally got a lot of attention where he's saying with public, so Copilot emits large chunks of my copyrighted code with no attribution, no LGPL license.
[1088.32 --> 1093.08]  My code on the left, GitHub on the right, he shows the pictures of the two and he says not okay.
[1093.56 --> 1102.76]  So I think this is what started to get that going is like the mixing of license code within the training data set of GitHub is part of the issue.
[1102.76 --> 1107.72]  And we talked about this a little bit with large language models, right?
[1107.84 --> 1111.10]  Large language models are kind of like stochastic parrots.
[1111.28 --> 1116.28]  They're putting all of these things together from various sources that they found with language, right?
[1116.28 --> 1138.42]  So when you have this weird mix of code that generates this weird mix of a block of code in your editor, it may be quite difficult to, you know, understand or trace back on the inference side what is actually coming out that is copyrighted in certain ways and that sort of thing.
[1138.42 --> 1151.40]  As we're into this kind of swamp of technical mixed with legal considerations on this happening and the expectation that it will continue to happen, you know, across multiple solutions.
[1151.40 --> 1154.78]  What does governance look like for something like this?
[1154.78 --> 1157.30]  You know, I say governance loosely.
[1157.50 --> 1159.68]  It could be legal remedy.
[1160.04 --> 1164.32]  It could be, you know, kind of, you know, we have AI ethics that we like to talk about.
[1164.90 --> 1174.10]  What does the world look like when you have kind of this swamp of a little bit of he said, she said in terms of, you know, is it, was it his code or was it not his code?
[1174.10 --> 1176.64]  And how do you resolve something like that?
[1176.72 --> 1185.78]  How do you find a framework that allows you to have confidence that you're within the boundaries of what is considered reasonable, acceptable and legal?
[1186.62 --> 1188.50]  Yeah, I mean, I think it's an open question.
[1189.04 --> 1195.48]  One of the things I was discussing with my team, we kind of had an open discussion about this because I was really curious on all their input.
[1196.40 --> 1200.92]  You know, what is the actual legal recourse here?
[1200.92 --> 1210.30]  So like the individual maintainer of some random tool on GitHub that's licensed GPL or something like that.
[1210.48 --> 1214.08]  Is that person going to sue GitHub?
[1214.58 --> 1224.48]  Or is more relevantly, is that person going to sue my organization because I use GitHub Copilot and output some like block of their code?
[1224.48 --> 1232.84]  Right. I think the likelihood of that happening is probably very low because, you know, these open source maintainers.
[1233.04 --> 1238.54]  I mean, we love our open source maintainers, but generally they don't have a lot of capacity for extra things.
[1238.54 --> 1246.08]  They're just kind of trying to get along, maintaining their project and keeping up with all the issues right in their spare time, potentially.
[1246.08 --> 1257.24]  So one of the things stressed in the article is probably not the individual maintainers that are going to deal with this legally, but it's some sort of open source advocacy groups.
[1257.24 --> 1265.58]  The one that is called out in the article, which I should mention is from Elaine Atwell, and we'll link that in our show notes.
[1265.58 --> 1274.80]  But the one that she references is the Software Freedom Conservancy or SFC, one of these open source advocacy groups.
[1274.94 --> 1284.84]  So it's likely it's much more likely that like an advocacy group like this would sue certain companies that are using this product.
[1284.84 --> 1298.14]  But even then, they're probably not going to go after, I wouldn't guess, the company that has one developer using GitHub Copilot to write some random like service in their organization.
[1298.14 --> 1308.34]  They would probably target large organizations, maybe with hundreds or even thousands of developers that maybe are all using GitHub Copilot and violating a bunch of things.
[1308.34 --> 1314.22]  So one element of this is, is it a reality that my team is going to get sued?
[1314.74 --> 1321.18]  My guess would be no, but that's a separate issue to whether it's a good idea to use this.
[1321.42 --> 1332.74]  And it's a separate issue like you're talking about as to what is the proper governance around something like this that would prevent or help with responsible usage.
[1332.74 --> 1338.48]  Right. Those are all kind of they have a slightly different nuance to those questions, I feel.
[1339.04 --> 1347.28]  It's not that far from, you know, when you think about those questions that you're raising there, it's very similar to other AI ethics discussions that we've had.
[1347.46 --> 1355.16]  And it kind of comes down to who has responsibility in these cases and who has agency, you know, in these cases.
[1355.16 --> 1359.58]  And then you there's some place you're going to draw a line on what is acceptable.
[1359.84 --> 1369.04]  And this is a thought that hit me right as you were talking about large language models a moment ago is that, you know, once again, you're you're in your and this is outside my my expertise, obviously.
[1369.26 --> 1375.96]  But you're in a body of knowledge that's being worked on, presumably is kind of public and open.
[1375.96 --> 1380.20]  But people are at some point things become copyrightable.
[1380.54 --> 1383.32]  And I'm sure an attorney could clarify that that knows all about that.
[1383.72 --> 1399.42]  But there's almost a need for a guarantee of that if you're going to use the tooling and the new methods that we're talking about, that there is a an assurance of some sort that it is going to fall within what is currently legally accepted use.
[1399.42 --> 1408.56]  And then there's also the question of like, it's what has historically been reasonable, given the new types of technology that people had never thought about.
[1408.68 --> 1410.24]  Does that continue to be reasonable?
[1410.36 --> 1416.82]  Is there you know, we we acknowledge that the legal frameworks have fallen way, way, way behind in these areas for the most part.
[1417.10 --> 1419.12]  So how do you resolve that?
[1419.16 --> 1422.32]  I mean, there's there's kind of a an ethical concern.
[1422.32 --> 1423.72]  There's a legal concern.
[1424.28 --> 1426.64]  There's all the various licenses specifically.
[1426.92 --> 1428.12]  It's quite a mess.
[1428.12 --> 1429.88]  How do you what's the path forward?
[1430.20 --> 1430.36]  Yeah.
[1430.48 --> 1434.14]  And that's why I kind of came to the conclusion with this one.
[1434.28 --> 1441.54]  You know, as much as this is a controversy, it's not going to grind the AI industry to a halt.
[1441.54 --> 1441.98]  Right.
[1442.04 --> 1446.80]  Because it's so messy that it probably won't.
[1447.12 --> 1450.64]  We probably won't understand the implications for years.
[1451.20 --> 1452.50]  That would be my guess.
[1452.52 --> 1456.00]  Like, yeah, like it's going to be years before we understand that.
[1456.00 --> 1465.66]  And by then, you know, I mean, GitHub, I think, is launching the enterprise sort of usage of Copilot if they haven't yet by the time you're listening to this episode.
[1465.66 --> 1467.72]  So there's going to be a lot of people using it.
[1467.80 --> 1470.20]  And that's going to muddy the waters even further.
[1470.64 --> 1471.08]  Right.
[1471.08 --> 1474.36]  The lawsuits will take several years to work themselves through.
[1474.36 --> 1487.50]  And by that time, the risk associated with being sued will have caused, you know, various actors in the process to to go into risk mitigation of various types, probably market based rather than legal.
[1487.50 --> 1508.06]  So, yeah, I think we can probably watch GitHub specifically and Microsoft and OpenAI, the ones involved in Copilot and sort of look at some of the ways in which they modify the service to understand how they're being pressured, maybe to to change what they're doing based on the ongoing proceedings and and all of that.
[1508.06 --> 1523.58]  Right. If they they sort of change how you use Copilot, that's maybe an indication to us that they're being, you know, if it's not a new feature, maybe that's due to some of these restrictions and implications of the legal side of things.
[1523.58 --> 1526.50]  So, yeah, it'll be an interesting one to watch.
[1526.68 --> 1537.28]  I actually got an email even from one of the members of our leadership team who I talk with occasionally about AI things and how the industry is shaping up.
[1537.38 --> 1538.92]  And he that's what he said.
[1538.94 --> 1541.36]  He's like, this is going to be an interesting one to watch.
[1541.36 --> 1546.40]  So definitely going to going to be interesting and we'll keep you updated here on the podcast.
[1553.58 --> 1567.44]  Well, Chris, the the other one, which is kind of in the same the other thing that I wanted to talk about today, which is sort of in the same theme, I guess, is one that also has to do.
[1567.44 --> 1578.96]  I think you use the term like some large body of knowledge or something when we were talking about GitHub and the large body of open source software knowledge, right, that GitHub is leveraging.
[1578.96 --> 1590.86]  There's another thing that has been quite controversial, I should say, quite interesting, I would say quite interesting, but also has generated a lot of controversy in the in the past weeks.
[1590.86 --> 1596.88]  And that's this Galactica model, which you can go to Galactica.org, learn about it.
[1596.96 --> 1598.74]  This is a model from Meta AI.
[1599.78 --> 1607.80]  And the sort of idea behind this model is, hey, we have all of this organized scientific information, right?
[1607.80 --> 1621.22]  We have a body of scientific work of papers, academic papers, which include narrative and theorems and math formulas and tables and all sorts of things.
[1621.22 --> 1621.58]  Right.
[1622.30 --> 1625.84]  And we have this kind of mass of papers.
[1625.84 --> 1642.76]  And what the team did is they released a new large language model trained on 48 million papers, textbooks, reference materials, compounds, proteins, and other sources of scientific knowledge.
[1642.76 --> 1647.90]  So that's what I took from the Galactica.org site, which is pretty cool.
[1647.90 --> 1649.72]  I mean, in the idea of it.
[1649.72 --> 1660.94]  And you can go through, there's an explore page on the Galactica site, although I think the site has been changing quite a bit in the recent weeks.
[1661.22 --> 1665.96]  But there is still at this time, there's an explore site on the Galactica site.
[1666.54 --> 1670.86]  And you can see the examples they give are language models that cite.
[1670.86 --> 1681.82]  So the input prompt example they give is the paper that presented a new computing block given by the formula, and then it gives a math formula, right?
[1682.06 --> 1686.12]  And then the Galactica suggestion is attention is all you need.
[1686.62 --> 1687.74]  Vaswani et al.
[1688.04 --> 1688.68]  2017.
[1688.68 --> 1696.94]  So this is kind of a way to organize scientific knowledge and kind of learn about scientific knowledge.
[1696.94 --> 1706.82]  But also they give this example, which I think is probably the more kind of gets to the more controversial things, which we can talk about here in a second.
[1707.40 --> 1709.26]  Scientific from scratch.
[1709.46 --> 1713.66]  Or I think some people might interpret that like science from scratch or something.
[1713.66 --> 1725.98]  They give the example of translating a math formula into plain English or finding a bug in Python code or simplifying a math formula or something like that.
[1726.44 --> 1739.12]  And so there's all these prompts you can give it, you know, translate this math formula into, you know, into plain English or something like that or into Python code, which seems to be quite useful to me.
[1740.58 --> 1742.94]  I'm not sure how that code was licensed.
[1742.94 --> 1744.88]  That's maybe another separate issue.
[1745.30 --> 1748.88]  But that's not the main controversy that's come about with this.
[1748.98 --> 1754.98]  But in general, maybe just first impressions of this work, Chris, what is your thought?
[1755.40 --> 1757.98]  I think it's a great idea.
[1758.32 --> 1765.24]  And we've seen these kinds of amazing, like we've seen these with proteins, you know, and such.
[1765.44 --> 1769.54]  We've seen amazing work in these different areas for doing that.
[1769.60 --> 1770.36]  And we will continue.
[1770.36 --> 1787.82]  But it's also sometimes in our industry, meaning the larger artificial intelligence industry, we are so busy trying to get the next big thing out and kind of be the thing of the moment that sometimes I think missteps are going to happen.
[1787.82 --> 1793.16]  And I think this is a case of a misstep, you know, where you had a large organization that's trying to get out there.
[1793.76 --> 1796.88]  Because honestly, you know, yes, it's meta.
[1797.00 --> 1799.30]  It's a big, amazing AI capability.
[1799.68 --> 1801.48]  But there's other big ones, too.
[1801.48 --> 1811.20]  And, you know, it may not it doesn't take long, as we've discovered over the last few years, for the for the next amazing thing to replace today's amazing thing.
[1811.92 --> 1816.54]  And so sometimes maybe maybe we need to get it right before we get it all the way out.
[1816.54 --> 1835.26]  Yeah. So before I talk about the the individual observations about Galactica, something just occurred to me, which I don't know if I've kind of distilled in my mind, like to this degree, is that even in my own work in developing AI models and developing AI systems,
[1835.26 --> 1855.84]  I think one of the principles that I've learned is the communication and expectations you set when you do an initial release of an AI system or an AI model really, really drive people's sort of initial perception and their ability to adopt it.
[1855.84 --> 1860.76]  So what I mean with this or I can give an example from my industry.
[1860.98 --> 1864.34]  Right. We do some language translation.
[1864.34 --> 1869.88]  Right. And if I come to a translation team and say, hey, it's awesome.
[1869.88 --> 1872.64]  I've just built this great machine translation system.
[1873.02 --> 1875.68]  You're no longer going to have to do translation system.
[1875.68 --> 1878.90]  Just make a couple of edits here and there and you're good to go.
[1879.32 --> 1880.98]  That's immediately going to.
[1880.98 --> 1892.18]  So what the translation team is going to look for in that system is all of the ways that it doesn't work right and doesn't fulfill the expectations that I've given to them.
[1892.26 --> 1892.46]  Right.
[1892.46 --> 1905.32]  Whereas if I come to that team and I say, hey, you know, I really appreciate what you're doing and I understand that you have pain points and efficiency around your process.
[1905.32 --> 1911.46]  I think that maybe this model or the system that we've created could help you.
[1911.46 --> 1920.80]  Could you all help us understand how this system can best be used in your process and we can kind of give you some suggestions, some prompts of getting started.
[1920.80 --> 1932.66]  Then what they're looking for is not so much why this is bad and is taking over our jobs or encroaching on what we're doing or is really dangerous.
[1932.66 --> 1937.86]  But their thought process is these people are wanting us to tell them how we can use this.
[1937.86 --> 1942.02]  And generally in those cases, I found people do find the positive things, too.
[1942.18 --> 1950.02]  Right. They find like, hey, I didn't expect this to work great in this situation, but it actually produced pretty good output.
[1950.02 --> 1951.60]  Can you do more of that?
[1951.60 --> 1953.96]  But in these other cases, it did really bad.
[1953.96 --> 1955.42]  So don't do that anymore.
[1955.42 --> 1955.84]  Right.
[1955.84 --> 1983.70]  So you get like more useful feedback on the initial release of something if you kind of approach the public or your internal teams or whoever your stakeholders are and ask the community to help you understand the behavior and utility of what you're releasing versus telling them the utility and telling them like this is going to solve this problem when in actuality they find out that it doesn't.
[1983.70 --> 1990.18]  Yeah. I mean, you know, there's the way that you approach that has a big impact on trust for the system.
[1990.34 --> 2005.64]  And as we've seen, you know, over and over through the years here with these with AI is one of those technologies that people have to develop a sense of trust in in terms of what's possible, but then also a validation of trust for any given system.
[2005.64 --> 2015.34]  And as you the way that you're outlining positioning that approach makes a big difference on how people are going to engage from a trust perspective as well.
[2015.48 --> 2022.22]  They'll give it a chance if they position it the way you suggested in the in the second version there versus the first.
[2022.38 --> 2027.40]  So it's it's difficult and it's not always that clear cut when you're in the process.
[2027.66 --> 2028.46]  Yeah. Yeah.
[2028.46 --> 2034.34]  So I don't for those that meta if you're listening, I totally also sympathize with you.
[2034.46 --> 2040.38]  It's very hard to figure out how to communicate these things well and release these things well.
[2040.38 --> 2050.82]  So I think likely this Galactica system is amazingly innovative and a great achievement.
[2051.18 --> 2060.38]  But it also has behavior that could be either non-ideal or or worse, you know, harmful in certain cases.
[2061.08 --> 2069.26]  Right. And so it's part of the I think part of the community, but also the creator's responsibility to anticipate some of those.
[2069.26 --> 2071.04]  So I guess I can give an example.
[2071.04 --> 2076.60]  So the I also found a fun article from or fun or disturbing.
[2076.90 --> 2078.48]  I don't know how I should phrase it.
[2078.62 --> 2085.74]  Article from Janelle Shane Galactica, the AI knowledge base that makes stuff up.
[2086.08 --> 2088.52]  So we'll link that in our show notes.
[2088.92 --> 2089.06]  Thanks.
[2089.18 --> 2090.42]  Pretty harsh there, isn't it?
[2090.50 --> 2092.62]  Yeah. Thanks, Janelle, for writing this.
[2092.62 --> 2094.80]  Basically, she starts with the conclusion.
[2095.06 --> 2096.22]  I've tried Galactica.
[2096.42 --> 2097.28]  It's not helpful.
[2097.28 --> 2100.14]  So the prompts that she gave.
[2100.66 --> 2107.44]  One prompt is the number of giraffes that have flown on a lunar mission is currently.
[2107.88 --> 2120.82]  And then Galactica responds with the number of giraffes that have flown on a lunar mission is currently 28, including 15 on the moon and 13 on Mars.
[2120.82 --> 2127.08]  Of those 28, 17 have flown on the moon and 11 have flown on the Mars.
[2127.68 --> 2134.94]  The first lunar mission was in 1968 when the Luna 13 mission sent a giraffe to the moon.
[2135.36 --> 2142.02]  In 1970, the Soviet lunar probe Luna 15 sent the giraffe to the moon.
[2142.56 --> 2143.52]  I'm sorry.
[2143.52 --> 2145.88]  It's pretty good, right?
[2145.88 --> 2147.32]  It's pretty good stuff right there.
[2147.82 --> 2148.18]  Yeah.
[2148.36 --> 2148.60]  Yeah.
[2148.62 --> 2149.90]  I mean, that's pretty good.
[2149.98 --> 2155.14]  I think I probably don't need to give that many other examples to illustrate.
[2155.28 --> 2157.80]  No, I think you highlighted it quite well.
[2157.80 --> 2165.52]  Well, the funny thing, and I almost feel like I was looking, I'm doing the same thing where I'm just looking at some of the various articles.
[2165.52 --> 2173.14]  And it's Ars Technica says, new meta AI demo writes racist and inaccurate scientific literature.
[2173.62 --> 2186.00]  But I mean, people get the idea as if it's a trust issue and an accuracy issue, one related to the other is for despite the very hard work, I'm sure, of that meta team, no one's going to trust that model.
[2186.00 --> 2196.20]  If they fix it and come back out with it, all the focus is going to be on, is this legit, what I'm getting, the results that I'm getting out of it, which is a shame when you think about it.
[2196.62 --> 2196.72]  Yeah.
[2196.78 --> 2199.54]  And I think about different approaches here that people have taken.
[2199.70 --> 2211.68]  I think on the one side, OpenAI and some of the models they've released in a very controlled way via an API, they have attempted to address part of this release problem where they understand.
[2211.68 --> 2219.66]  And there could be even intentional misuse of this around misinformation, right, or harmful usage.
[2219.94 --> 2224.08]  And they try to anticipate that, create an API with controls around that, et cetera.
[2224.58 --> 2238.14]  The other approach, which I think is a kind of more open source or open approach, something like stability, right, where they release the model, stable diffusion, under an open license.
[2238.14 --> 2243.90]  So it's out in the public, but they very much within the licensing, the open rail license.
[2244.40 --> 2266.04]  First off, try to license and include licensing around restricted use that they could envision, right, using the model, but put it out in the public with the hope that the community can help put some necessary guardrails around usage and provide feedback on how the model can be used and that sort of thing.
[2266.04 --> 2271.84]  The third approach, I think maybe another approach would be to say, well, here's our great model.
[2272.16 --> 2273.60]  It can solve this problem.
[2274.36 --> 2282.04]  And you kind of ignore the fact that maybe it doesn't always solve that problem and maybe it also has harmful use.
[2283.04 --> 2290.62]  So I think it's not necessarily like any one of these is always right or always wrong, probably.
[2290.62 --> 2295.92]  But it is worth considering these release options and what their implications are.
[2296.30 --> 2296.62]  It is.
[2296.74 --> 2306.38]  You know, in fairness, I remember, you know, on that particular release from OpenAI that you're talking about, we were, I remember in our conversation, we were just on the show.
[2306.48 --> 2310.04]  We were a little bit critical, kind of going, you know, they're kind of holding back and all that.
[2310.04 --> 2313.68]  And I don't remember where we ended up on that because things have evolved.
[2313.78 --> 2316.96]  But I do remember having the discussion on whether that's appropriate.
[2317.02 --> 2322.14]  And then we have something like this today and it makes it look a lot more reasonable in retrospect.
[2322.14 --> 2329.22]  So it really depends on the moment that you're in and what's just happened in terms of that perspective there.
[2329.22 --> 2346.40]  I also remember on the, in terms of the licenses, trying to anticipate specifics, I remember thinking whoever wrote a particular clause may not have had great insight into some of the use cases in that clause as well.
[2346.92 --> 2351.52]  So it's a hard nut to crack trying to come up with the right solution here.
[2351.94 --> 2352.32]  For sure.
[2352.32 --> 2366.94]  And granted, I think, you know, some of the response from, from meta individuals, not virtual individuals, I mean, individuals at meta is, well, this, this sort of prompt, right?
[2367.02 --> 2368.12]  The giraffe prompt.
[2368.34 --> 2379.90]  I think one of the phrases that they used to describe that sort of prompt was causally misusing the model, which is, is sort of blaming the people using it.
[2379.90 --> 2396.60]  I think, to be fair, like that prompt is trying to draw something out of the model, which the creators of the model, they would explicitly say, well, this, this is like a, it is an adversarial prompt, right?
[2396.70 --> 2401.34]  Like you already know there's no giraffes that have flown on a lunar mission, right?
[2401.46 --> 2402.24]  You're trying.
[2402.38 --> 2403.90]  So there's that perspective.
[2404.68 --> 2408.80]  So I don't, I think there is an element of truth in that.
[2408.80 --> 2419.76]  But I think generally the community have said, well, you know, how close are, is the sort of goofy, causally misusing the model?
[2420.46 --> 2424.92]  How close is that to the gray area of misinformation, right?
[2424.96 --> 2429.52]  And people intentionally using it to create misinformation, right?
[2429.96 --> 2435.14]  Especially around science or important things like health and, and other things like that.
[2435.14 --> 2435.58]  Yeah.
[2435.58 --> 2435.88]  Yeah.
[2435.98 --> 2441.58]  You know, it's kind of funny starting this conversation specifically about this meta instance.
[2441.82 --> 2446.94]  We were kind of laughing about it and stuff, but I think we're going to see so many of these instances in the years ahead.
[2446.94 --> 2458.20]  And you've, you've, you've made a point that I think we sometimes need to respond with a bit of empathy for the, the data scientists and, and AI engineers that are trying to create these.
[2458.20 --> 2462.68]  Because they're trying to do some pretty cutting edge stuff and mistakes are going to be made.
[2462.68 --> 2466.50]  And in the end, my understanding is nobody was hurt by this.
[2467.50 --> 2469.80]  So yeah, we, we need to be empathetic.
[2469.98 --> 2472.56]  We need to both be critical and empathetic.
[2472.88 --> 2479.70]  So my previous boss would say we need to be tenacious and gracious.
[2480.54 --> 2483.62]  Both of those things aren't mutually exclusive.
[2484.26 --> 2485.98]  So yeah, that's a good point.
[2485.98 --> 2495.30]  Um, as we, as we wrap up here, um, I do want to, uh, share, uh, a new learning resource that I kind of came across, um, in the past couple of weeks.
[2495.70 --> 2505.80]  Um, I don't know if you remember Chris, at one point, I think we shared a learning resource from, uh, Christoph Molnar, his book on, uh, interpretable machine learning, which is really cool.
[2505.90 --> 2513.88]  Well, he's has a new book called, uh, modeling mindsets, the many cultures of learning from data.
[2513.88 --> 2541.96]  And, um, my understanding is that kind of this book goes into various sort of approaches to modeling, whether you think about like Bayesian statistics or other approaches, um, and talks about kind of what can we learn from these different modeling mindsets that could benefit us in our own sort of modeling work, which is, I think quite an interesting proposition.
[2541.96 --> 2548.36]  So his subtitle is becoming a better data scientist by understanding different modeling mindsets.
[2548.48 --> 2557.10]  So understanding these diverse modeling mindsets can help us whatever modeling is modeling problem or, or solution you're trying to come up with.
[2557.24 --> 2558.74]  So modeling mindsets.
[2558.98 --> 2560.92]  I think it's a good time for a book like that as well.
[2560.92 --> 2567.30]  When you think about it and, and, and, and terms of benefiting from the different ways that you can approach a problem.
[2567.30 --> 2573.42]  Cause I've recently seen some engineers very much stuck in a particular mindset trying to solve a problem.
[2573.42 --> 2575.66]  So that, that one hits close to home for me.
[2576.14 --> 2577.14]  A particular lane.
[2577.28 --> 2577.70]  Yeah.
[2577.96 --> 2579.52]  There are other lanes.
[2579.86 --> 2580.86]  Yes, indeed.
[2581.20 --> 2581.50]  Yeah.
[2582.04 --> 2582.34]  Cool.
[2582.66 --> 2585.06]  Well, uh, thanks for the discussion today, Chris.
[2585.08 --> 2587.92]  It was, it was a fun one leading up to Thanksgiving.
[2587.92 --> 2588.40]  Thanksgiving.
[2588.76 --> 2593.42]  I hope you have a great holiday with your family and, uh, look forward to chatting next week.
[2593.54 --> 2594.18]  You too, Daniel.
[2594.28 --> 2595.00]  Have a good holiday.
[2595.18 --> 2595.60]  Talk to you later.
[2604.40 --> 2605.24]  All right.
[2605.38 --> 2606.94]  That is our show for this week.
[2607.18 --> 2609.56]  If you dig it, don't forget to subscribe.
[2609.90 --> 2612.76]  Head to practicalai.fm for all the ways.
[2612.76 --> 2618.66]  And if practical AI has benefited your life, pay it forward by sharing the show with a friend or a colleague.
[2619.02 --> 2621.98]  Word of mouth is the number one way people find shows like ours.
[2622.40 --> 2625.26]  Thanks again to Fastly for fronting our static assets.
[2625.56 --> 2628.00]  To Fly.io for backing our dynamic requests.
[2628.54 --> 2630.10]  To Breakmaster Cylinder for the beats.
[2630.36 --> 2631.24]  And to you for listening.
[2631.50 --> 2632.18]  We appreciate ya.
[2632.48 --> 2633.36]  That's all for now.
[2633.60 --> 2635.06]  We'll talk to you again on the next one.
[2635.06 --> 2649.42]  Game on.
