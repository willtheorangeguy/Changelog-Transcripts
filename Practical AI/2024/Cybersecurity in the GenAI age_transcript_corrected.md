[0.00 → 7.28] Welcome to Practical AI.
[7.70 → 15.00] If you work in artificial intelligence, aspire to, or are curious how AI-related tech is
[15.00 → 17.72] changing the world, this is the show for you.
[18.06 → 20.64] Thank you to our partners at Fly.io.
[21.16 → 26.86] Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on
[26.86 → 30.72] six continents, so you can launch your app near your users.
[31.28 → 33.24] Learn more at Fly.io.
[35.46 → 41.44] Well, our friends over at Speakeasy have the complete platform for API developer experience.
[41.60 → 47.10] They can generate SDKs, Terraform providers, API testing, docs, and more.
[47.32 → 53.16] And they just released a new version of their Python SDK generation that's optimized for
[53.16 → 55.60] anyone building an AI API.
[55.60 → 62.20] Every Python SDK comes with Pedantic models for requests and response objects, an HTTP
[62.20 → 69.40] x client for async and synchronous method calls, and support for server-sent events as well.
[69.96 → 75.36] Speakeasy is everything you need to give your Python users an amazing experience integrating
[75.36 → 76.00] with your API.
[76.74 → 80.06] Learn more at speakeasy.com slash Python.
[80.46 → 84.14] Again, speakeasy.com slash Python.
[85.60 → 98.96] Welcome to another episode of Practical AI.
[99.36 → 100.82] This is Daniel Whiten ack.
[100.92 → 104.36] I am the founder and CEO at Prediction Guard.
[104.36 → 111.38] And I am joined, as always, by my co-host, Chris Benson, who is a principal AI research engineer
[111.38 → 112.66] at Lockheed Martin.
[112.90 → 114.92] It's good to record one together, Chris.
[115.00 → 116.68] We've been a couple where we've been apart.
[117.06 → 117.54] That's right.
[118.02 → 118.58] Yeah.
[118.72 → 122.12] It's good to have the band back together, I guess.
[122.46 → 122.94] Absolutely.
[122.94 → 124.80] I took a brief respite.
[124.96 → 127.30] I had some lower back surgery.
[128.00 → 134.52] And since I'm always thinking about technology and AI, I was trying to imagine what the surgery
[134.52 → 139.44] might be like today versus if I had done this, if we were in a slight time warp and gone to
[139.44 → 139.74] the future.
[139.74 → 141.26] Did they have a robot arm?
[141.44 → 141.94] Exactly.
[141.94 → 147.04] If they did, you know, reinforcement learning combined with, you know, kind of chat interface
[147.04 → 148.78] and, you know, the whole thing.
[148.96 → 155.26] So it was kind of a novel mind experiment there that I had about what would it be if I was,
[155.54 → 157.02] you know, this was a little bit different time.
[157.34 → 159.02] But yep, all good for here.
[159.02 → 165.78] Yeah, well, I would hope that in all of our futures, as we have medical procedures done
[165.78 → 174.30] increasingly by AI or AI-assisted and other things like that, that those things are very
[174.30 → 176.42] secure as they happen.
[176.62 → 178.42] That would be very important, I think.
[178.62 → 179.58] Yes, absolutely.
[179.84 → 186.18] And on that front, I'm really excited because, Chris, on this show, actually a couple of times,
[186.18 → 195.94] I referenced the OWASP top 10, Gen AI top 10 sort of risk white paper breaks down security
[195.94 → 201.46] and privacy related risks into sort of different categories and helps people think about it.
[201.56 → 205.76] This is a collaborative thing with multiple organizations involved.
[206.00 → 211.60] But today we've got with us Dennis Cruz, who is a founder at the Cyber Boardroom, but also
[211.60 → 218.26] has been involved in OWASP and in various capacities over the years and is aware of all of this
[218.26 → 220.26] that's going on and contributing to it.
[220.36 → 222.60] So we're just super excited to have you with us.
[222.68 → 225.06] Dennis, this is one I've been really looking forward to.
[225.58 → 226.90] Thanks for inviting me.
[227.00 → 232.96] And this is a topic that I'm very, very interested in, because I think there's a lot of potential.
[233.22 → 234.40] There are a lot of dangers too.
[234.48 → 239.60] But I think it's very exciting times for us as an industry in all sorts of levels.
[239.60 → 244.64] Yeah, well, like I mentioned, you've been involved in OWASP in different capacities.
[245.40 → 251.22] How did the kind of, I guess, give us a little bit of background and how the first off, what
[251.22 → 257.42] OWASP is and what that means for those that aren't familiar, but also as you kind of started
[257.42 → 263.40] seeing this Gen AI stuff come about, how did it strike you from that standpoint of being
[263.40 → 265.64] involved in OWASP over the years?
[265.64 → 269.62] Okay, so OWASP is the Open Web Application Security Project.
[270.04 → 274.84] And you kind of can say that OWASP is the people around the world that kind of cared about
[274.84 → 280.82] application security, that found that sort of intersection of the world moving to apps
[280.82 → 284.10] versus networks and then the security elements of it, right?
[284.16 → 289.62] And I think it's definitely one of those organizations that has grown from nobody really cared about
[289.62 → 293.72] it to, you know, some more people carrying it to now it's been referenced left, right,
[293.72 → 294.88] and centre, right?
[295.04 → 298.86] And has really, you know, changed the world in very, very nice ways.
[298.98 → 302.80] And it's always attracted, I think, the people that want to do better.
[302.96 → 304.32] I think it's a lovely community.
[304.70 → 308.86] It's very open, you know, by its nature, but it's also, I think it's been a great hotbed
[308.86 → 314.30] of innovation, right, in terms of the first OWASP Top 10, the testing guide, a lot of amazing
[314.30 → 315.50] tools come out of it.
[315.78 → 317.64] OWASP, you know, the Pendency Checker.
[317.74 → 318.54] There are billions of tools.
[318.54 → 322.64] I develop a couple too, and it's a great red community, right?
[322.72 → 328.86] And I think Gen AI, it's an interesting evolution on our technology, even from a security point
[328.86 → 333.78] of view, because I think for the first time we have a technology that kind of understands
[333.78 → 335.18] intent, right?
[335.22 → 336.80] And I think that's quite different.
[337.24 → 342.84] Now, I want to say, ah, the bad, but I think what Gen AI is doing, ChatGPT and everything,
[342.84 → 348.72] is actually making most of what we always talked about in OWASP even more important,
[348.88 → 349.08] right?
[349.22 → 353.26] Because if you think about it, you know, Gen AI is an API, right?
[353.32 → 357.14] It's fundamentally an API that you send some data in, you get some outputs out, and in
[357.14 → 358.68] these days you can connect internal systems.
[359.26 → 365.22] And in a way, it's your most vulnerable and your most dangerous API at the same time.
[365.22 → 371.14] And I would say that the most thing that is quite unique with Gen AI is the fact that you're
[371.14 → 374.04] now sending English or Portuguese, right?
[374.04 → 376.18] Or French or whatever language or Klingon, right?
[376.18 → 380.40] Whatever language you want to talk to, that is now code, right?
[380.44 → 381.76] And that's quite different.
[382.00 → 386.06] You know, for the ones who've been doing security for a while, we always talked about securing
[386.06 → 387.38] code and data, right?
[387.38 → 392.04] Like if you can separate code and data, we know what code is, we know what data is, you actually
[392.04 → 393.40] can secure things quite well.
[393.40 → 397.34] Now you're in a world where data is code, right?
[397.50 → 400.58] So that introduces a huge amount of interesting challenges.
[401.08 → 404.94] And I think it's one of those technologies that on one end, it's going to create a lot
[404.94 → 409.76] of problems, but on the other end, I think it has the potential to solve some of the biggest
[409.76 → 414.26] challenges of scale that we always had in security and in engineering, right?
[414.34 → 416.88] And in development with that technology too.
[416.98 → 421.28] So I think it's going to add up to both sides of the universe there.
[421.60 → 421.94] It's interesting.
[421.94 → 425.16] I actually want to go back to something you said right as you were starting off a second
[425.16 → 430.98] ago and build on it a little bit that like your kind of alluded to for a long time, you
[430.98 → 435.28] know, over the years, security was always kind of a, you know, the redheaded stepchild
[435.28 → 437.44] of the of application developer.
[437.88 → 440.56] You know, there were a lot of folks that just didn't care too much.
[440.56 → 445.10] And obviously we've progressed along, and we're talking about Gen AI and things like that,
[445.16 → 445.78] what we're doing now.
[446.18 → 450.98] But going back, I'm just curious as we're talking about security in general in app dev,
[451.18 → 457.06] even before we get to AI being introduced into it, what has motivated people to get into
[457.06 → 459.52] the security side in your view as you've watched this?
[459.52 → 466.52] Because I too have seen that the security concern go from being kind of a backseat thing to being
[466.52 → 469.76] very front and centre and very important in a lot of organizations.
[470.02 → 471.28] And that's been an evolution.
[471.28 → 476.10] And as you've been in the middle of this ecosystem, how have you seen that happen and why?
[476.24 → 478.18] And where's that progression come to?
[478.18 → 483.58] Well, so I would say from personal experience, and I think from most of my peers, there's,
[483.64 → 486.44] you know, there's a thing of, it's nice to make the world safer, right?
[486.48 → 491.60] There's definitely a shag of like, it's nice to do something that the outcome is to make
[491.60 → 492.34] people safe.
[492.40 → 496.62] And I've always liked to stay on the sort of defence, you know, yes, a bit offensive, but
[496.62 → 498.46] like on making things systems secure, right?
[498.76 → 500.92] So I think intellectual is really cool.
[501.10 → 503.02] I think from a technology point is really cool.
[503.36 → 507.62] There is a thing of hacking and breaking into stuff, which is also quite, you know, quite interesting,
[507.62 → 507.92] right?
[508.18 → 512.50] There's a little bit of a James Bond, you know, hacking into the big system and getting
[512.50 → 515.66] there and all that jazz, which I think is part of the evolution, right?
[515.68 → 518.12] So there's, I think is a really cool industry.
[518.32 → 518.96] It's very open.
[519.06 → 520.14] It's very welcoming, right?
[520.16 → 522.22] It's also very pragmatic, right?
[522.28 → 524.40] It's in the beginning, it's like, can you exploit it or not, right?
[524.40 → 524.92] Can you do this?
[524.96 → 525.66] Can you do that, right?
[526.14 → 529.82] And I have to say, we need to also look, you know, be pragmatic to say for a long time,
[529.90 → 531.36] it didn't really matter, right?
[531.36 → 536.24] Like in a way, there was a period where you knew who's being attacked because they were the
[536.24 → 538.00] companies who had the best security teams.
[538.32 → 540.62] Literally, there was a one-to-one correlation.
[541.06 → 542.46] That team does security very well.
[542.86 → 543.06] Cool.
[543.20 → 544.10] They've been attacked, right?
[544.14 → 545.54] They're on the evolution, right?
[545.80 → 547.28] And I've now been a CIO.
[547.42 → 548.52] I've worked a lot of companies.
[549.02 → 552.38] And there's definitely, I tend to break into three different worlds, right?
[552.44 → 556.20] There is the nation state, you know, the high level of espionage.
[556.38 → 558.72] There is the ideology attacks, right?
[558.74 → 559.96] And there's the commercial attacks.
[560.04 → 562.54] The reality is that this one is a completely different level.
[562.96 → 565.08] If you're dealing with nation state, you know about it, right?
[565.08 → 566.20] You have hell of a team.
[566.42 → 567.36] And we can do it, right?
[567.38 → 568.58] But it's a very different game.
[569.00 → 571.72] The ideology, it depends on the industry you're in, right?
[571.76 → 573.04] Some industries are much more toxic.
[573.16 → 574.02] They tend to attract that.
[574.64 → 576.98] Most of it is to do with the business model of the attackers.
[576.98 → 582.94] So what has happened in the last, you know, 10, 15 years is that the more we move our society
[582.94 → 586.74] into digital, the more the business model of the attackers evolve.
[587.10 → 589.88] So in the past, you can get away with a lot of things.
[589.92 → 593.06] You could get away with crazy insecure applications out there.
[593.20 → 595.98] And the probability of you being attacked was quite low, right?
[596.22 → 597.84] Now you kind of can't, right?
[597.94 → 602.50] So I think there's been that evolution of, in a way, the stakes are much higher, right?
[602.50 → 606.42] Now, you know, even the recent CrowdStrike problem, right, you know, which I still think
[606.42 → 607.94] is a security problem, right?
[608.22 → 609.20] We can talk about it if you want.
[609.44 → 613.28] But that just shows how one problem in technologies can bring down, right?
[613.36 → 614.88] Large chunks of society, right?
[615.02 → 617.82] And in the old days, it was the NIDA, right?
[617.86 → 621.12] The ISS worms that brought down a chunk of technology.
[621.32 → 623.56] But at the time, the impact was limited.
[623.84 → 625.82] Now, it really makes a difference, right?
[625.82 → 629.98] Like now a cybersecurity problem in an organization of a medium size can break the company.
[630.10 → 631.80] It can be really severe disruption, right?
[631.80 → 637.24] Even a ransomware incident in one of our suppliers can actually cause a lot of problems in your
[637.24 → 637.52] world.
[637.80 → 642.16] So I think, you know, the application security and OWASP and everything, we have, in a way,
[642.22 → 646.36] matured with the kind of evolution of the market, right?
[646.60 → 651.74] Although I have to say that I still feel that most companies, it's still a marketing exercise.
[651.74 → 659.60] I'm not, it's a controversial view, but I think we still don't have a good way to measure
[659.60 → 662.10] the cybersecurity preparedness of companies.
[662.56 → 668.16] So there are still a lot of companies that kind of roll the dice and go, well, I hope it goes
[668.16 → 669.16] okay, right?
[669.40 → 673.84] Although much less than before, but I still feel there's a lot of maturity that we need
[673.84 → 675.02] in our own industry, right?
[675.06 → 675.62] To do that.
[675.88 → 681.54] And just a final point, the thing I also learned a lot was that cybersecurity is not an isolation.
[682.10 → 686.64] Cybersecurity is a side effect of engineering and business practices, right?
[686.64 → 691.78] So there's a moment where if you want to fix cybersecurity problems, you want to fix application
[691.78 → 695.10] security problems, you have to fix engineering problems, right?
[695.18 → 696.60] And that leads to that, right?
[696.62 → 700.14] If you do perfect engineering, if you do perfect development, perfect practices,
[700.64 → 705.12] half of what we talk about in application security is not needed because you just do it,
[705.28 → 705.46] right?
[705.50 → 706.64] It's just good practices.
[707.42 → 710.42] The problem is a lot of companies, a lot of teams don't do that.
[710.56 → 712.76] So the side effect is the security problems.
[712.76 → 718.24] I'm wondering when you're talking about this, this sort of business practices, the engineering,
[718.64 → 722.86] where these security vulnerabilities pop up and that sort of thing.
[723.18 → 727.90] Part of what comes to my mind on the Gen AI side is the fact that it brings the domain
[727.90 → 735.06] experts a lot closer to the actual technology in the sense that often there are tools or there
[735.06 → 741.70] are interfaces that people are using to create sort of chains of reasoning just with prompts
[741.70 → 743.88] and other things, you know, just with natural language.
[744.06 → 749.26] So they're not, to your point, I think now this sort of natural language is kind of like the code
[749.26 → 750.72] of programming these models.
[751.12 → 756.94] How do you think that that shifts the dynamic between like the engineering side and the
[756.94 → 757.52] business side?
[757.60 → 761.92] Because from my perspective, a lot of these domain experts and business people are coming
[761.92 → 765.84] much closer to the actual kind of core functionality of an application.
[766.46 → 768.40] And I think that's the same opportunity, right?
[768.40 → 773.98] So first, I don't view that the real power of ChatGPT is that it can create things,
[774.48 → 774.62] right?
[774.66 → 777.92] The real power of ChatGPT is that it can understand context.
[778.04 → 779.36] It can understand data.
[779.62 → 782.64] It can create mappings and relationships, right?
[782.84 → 787.96] And what is in practice, you know, the way I visualize what you described is that in the past,
[788.36 → 790.98] everything you want to do had to be coded, right?
[791.08 → 795.90] It had to be solidified in bits of code, which is also where vulnerabilities were created,
[795.90 → 801.66] but also where, in a way, we were locking down the business logic into code, microservices,
[801.92 → 802.60] trucks, et cetera.
[802.80 → 806.26] And then we got bogged down by the complexity of that, right?
[806.34 → 809.60] And then we couldn't understand the side effects and then things ground to a halt.
[810.02 → 814.38] And then, again, security vulnerabilities appear in those gaps, right?
[814.44 → 815.36] It's those gaps.
[815.46 → 821.62] It's those misunderstanding of how APIs work or an API that was created over here in a secure
[821.62 → 823.26] state that is now plugged to the internet.
[823.26 → 825.52] You know, maybe not the best move, right?
[826.12 → 831.04] But I think where we're now entering a phase is that you can have a layer where the business
[831.04 → 833.68] logic is now described in prompts, right?
[833.84 → 838.22] And what happens when you describe the prompt, you start to describe the intent of what you
[838.22 → 839.28] want to see happening.
[839.68 → 844.72] And instead of that intent being locked in code, which is really hard to change, it has
[844.72 → 848.46] a huge amount of things, you know, side effects, you can have that in prompts.
[848.74 → 850.90] Now, we need to be better understanding the prompts.
[850.90 → 856.64] I'm doing a lot of work on provenance, deterministic AI to make sure that we actually have AI outputs
[856.64 → 857.48] that are deterministic.
[857.76 → 862.40] But it's very powerful to be able to start to describe that, right?
[862.88 → 863.82] I'll give an example.
[864.08 → 868.18] Like, if you go to any organization, like when we do threat modelling, so one of the practices
[868.18 → 869.58] in security is threat modelling, right?
[870.12 → 874.04] Threat modelling is just social engineer the other side to give us an architecture diagram,
[874.20 → 874.42] right?
[874.46 → 875.26] That is up-to-date.
[875.46 → 877.58] Because once you have that, you'll find vulnerabilities, right?
[877.58 → 879.70] Because you start asking questions what about this?
[879.76 → 880.22] What about that?
[880.26 → 880.68] What about that?
[880.72 → 881.20] What about that?
[881.24 → 881.36] Right?
[881.66 → 886.22] You know, in a way, the hidden elephant is most organizations have no idea how the app
[886.22 → 887.12] works, right?
[887.16 → 889.90] They have no idea, you know, how actually things connected.
[890.22 → 892.68] The guys who develop it have gone, right?
[892.76 → 897.76] Like, you know, now imagine a world where we start to use Gen.AI to explain how it works.
[897.88 → 902.04] Imagine, you know, a code commit that goes to a Gen.AI layer that I can ask,
[902.04 → 904.62] did this change the attack surface, right?
[904.78 → 908.02] Did the attack surface of my organization change because of this?
[908.30 → 910.86] And they say, oh, if you did, then we need to do a review, right?
[910.94 → 911.84] If you don't, cool.
[912.10 → 913.48] Go all the way to production, right?
[913.80 → 917.72] Now, these questions in the past were impossible to ask, right?
[917.80 → 921.60] Or you had ridiculous static analysis that, you know, just about didn't work.
[921.86 → 927.30] Now we can start to codify a lot of those business logic questions, a lot of those intents
[927.30 → 933.58] of what I want to do, right, in, you know, in basically in simple language instead of
[933.58 → 933.82] code.
[934.14 → 938.62] Because imagine, like, if you say, I want to do a change that allow anybody from the
[938.62 → 943.14] internet to access every record from this company, right?
[943.58 → 944.72] You probably go, oh, hold on.
[944.86 → 947.78] I'm not sure if that's a good idea, right?
[947.90 → 953.24] Or, you know, I want this to allow, you know, an attacker to run and control JavaScript on
[953.24 → 954.06] my clients, right?
[954.16 → 955.42] Oh, maybe not, right?
[955.42 → 958.38] I want my secrets to be put on a source code, right?
[958.54 → 959.12] Maybe not.
[959.48 → 963.54] But at the moment, all those things get locked in to code, right?
[963.82 → 968.66] And it's hard to understand the side effects because nobody arrives one day and says, I'm
[968.66 → 970.14] going to create a security vulnerability, right?
[970.22 → 971.76] They, you know, unless they're malicious, right?
[971.82 → 977.20] But apart from those, right, it just, a lot of times it's just genuine mistakes, right?
[977.24 → 982.98] So I think what Gen.ai gives us is the ability to start thinking a lot more like three-dimensional,
[982.98 → 988.78] right, in our questions, but also in our applications where we start to describe the intent of what
[988.78 → 989.42] we want to do.
[989.68 → 990.96] And that can be analyzed.
[991.06 → 995.10] In fact, that can be analyzed by other Gen.ai's so we can start to get a much better sense of
[995.10 → 996.10] actually what is happening.
[996.10 → 1013.80] Okay, friends, I'm here in the breaks with Annie Sexton over at Fly.
[1014.00 → 1016.58] Annie, you know we use Fly here at Change Law.
[1016.58 → 1017.60] We love Fly.
[1017.92 → 1020.46] It is such an awesome platform, and we love building on it.
[1020.46 → 1025.76] But for those who don't know much about Fly, what's special about building on Fly?
[1026.04 → 1030.82] Fly gives you a lot of flexibility, like a lot of flexibility on multiple fronts.
[1031.24 → 1036.12] And on top of that, you get, so I've talked a lot about the networking and that's obviously
[1036.12 → 1041.38] one thing, but there are various data stores that we partner with that are really easy to
[1041.38 → 1041.84] use.
[1042.30 → 1045.80] Actually, one of my favourite partners is Tigress.
[1045.80 → 1049.54] I can't say enough good things about them when it comes to object storage.
[1049.78 → 1053.34] I've never in my life thought I would have so many opinions about object storage, but
[1053.34 → 1053.90] I do now.
[1054.16 → 1060.70] Tigress is a partner of Fly, and it's S3 compatible object storage that basically seems like it's
[1060.70 → 1062.00] a CDN, but it's not.
[1062.08 → 1066.46] It's basically object storage that's globally distributed without needing to actually set
[1066.46 → 1067.52] up a CDN at all.
[1067.62 → 1070.40] It's like automatically distributed around the world.
[1070.72 → 1074.04] And it's also incredibly easy to use and set up.
[1074.04 → 1076.44] Creating a bucket is literally one command.
[1076.72 → 1081.54] So it's partners like that, that I think are this sort of extra icing on top of Fly that
[1081.54 → 1085.06] really makes it sort of the platform that has everything that you need.
[1085.52 → 1087.50] So we use Tigress here at Changelog.
[1087.62 → 1089.06] Are they built on top of Fly?
[1089.30 → 1092.50] Is this one of those examples of being able to build on Fly?
[1092.92 → 1093.14] Yeah.
[1093.32 → 1098.12] So Tigress is built on top of Fly's infrastructure and that's what allows it to be globally distributed.
[1098.54 → 1103.32] I do have a video on this, but basically the way it works is whenever, like let's say
[1103.32 → 1107.00] a user uploads an asset to a particular bucket.
[1107.12 → 1111.06] Well, that gets uploaded directly to the region closest to the user.
[1111.14 → 1114.66] Whereas with a CDN, there's sort of like a centralized place where assets need to get
[1114.66 → 1115.14] copied to.
[1115.22 → 1119.00] And then eventually they get sort of trickled out to all the different global locations.
[1119.00 → 1123.32] Whereas with Tigress, the moment you upload something, it's available in that region instantly.
[1123.78 → 1127.28] And then it's eventually cached in all the other regions as well as it's requested.
[1127.68 → 1131.86] In fact, with Tigress, you don't even have to select which regions things are stored in.
[1131.86 → 1133.54] You just get these regions for free.
[1133.78 → 1136.98] And then on top of that, it is so much easier to work with.
[1136.98 → 1143.08] I feel like the way they manage permissions, the way they handle bucket creation, making
[1143.08 → 1147.90] things public or private is just so much simpler than other solutions.
[1148.50 → 1151.44] And the good news is that you don't actually need to change your code if you're already
[1151.44 → 1152.12] using S3.
[1152.28 → 1153.16] It's S3 compatible.
[1153.34 → 1156.06] So like whatever SDK you're using is probably just fine.
[1156.10 → 1157.60] And all you got to do is update the credentials.
[1157.82 → 1159.46] So it's super easy.
[1159.46 → 1160.42] Very cool.
[1160.48 → 1160.86] Thanks, Annie.
[1161.04 → 1163.32] So Fly has everything you need.
[1163.52 → 1168.80] Over 3 million applications, including ours here at Changelog, multiple applications have
[1168.80 → 1169.84] launched on Fly.
[1170.30 → 1176.12] Boosted by global any cast load balancing, zero configuration private networking, hardware
[1176.12 → 1181.76] isolation, instant wire guard VPN connections, push button deployments that scale to thousands
[1181.76 → 1182.36] of instances.
[1182.70 → 1184.68] It's all there for you right now.
[1185.08 → 1186.24] Deploy your app in five minutes.
[1186.24 → 1188.36] Go to fly.io.
[1188.82 → 1190.80] Again, fly.io.
[1190.80 → 1217.82] So Dennis, you said something that was pretty intriguing to me, which I think is maybe a
[1217.82 → 1224.88] kind of distinction that is maybe interesting to draw out and get your thoughts on, which
[1224.88 → 1231.46] is this idea that like when you think of kind of the intersection of cybersecurity and AI,
[1231.68 → 1233.82] you could come at it from two perspectives.
[1233.82 → 1242.28] So you could come at it from how can we use AI to help us in our cybersecurity tasks or to
[1242.28 → 1244.48] create new tools for cybersecurity?
[1244.48 → 1250.70] And then the other side would be, well, how do we operate AI systems securely?
[1251.24 → 1254.62] So there's probably some interaction between these two things.
[1254.62 → 1260.72] But could you give us a sense from your perspective as an expert in this field and also seeing a lot
[1260.72 → 1267.90] of things so far, how do you see the kind of maturity of these two sides of that coin?
[1268.38 → 1273.22] Anything you'd want to highlight on either side of that in terms of how both things are progressing,
[1273.22 → 1275.48] at least at the state of where we are now?
[1275.48 → 1281.94] So you're saying that the difference between using AI to sort of build systems and do things
[1281.94 → 1287.56] and then using one of those outputs is the cybersecurity analysis, right, of what you have?
[1287.96 → 1295.20] Yeah, I could imagine there are ways I could use AI to fight cybercrime, for example, or to prevent
[1295.20 → 1298.98] malware or like you just said, to help explain applications.
[1298.98 → 1306.26] So that's using AI to help you create more secure systems, whereas there also could be
[1306.26 → 1311.64] just your AI system is insecure in and of itself, right, in how you've deployed it and run it.
[1311.92 → 1312.04] Yeah.
[1312.14 → 1317.90] And just on the second one, I think if you're not careful, most AI deployments are ridiculously
[1317.90 → 1319.02] insecure, right?
[1319.12 → 1319.66] Like they are.
[1319.84 → 1324.64] In fact, we have to take into account that we still don't have a good understanding for
[1324.64 → 1325.78] how the models work.
[1325.78 → 1330.30] So the reality is there's nobody today that can tell us that these models don't have ridiculous
[1330.30 → 1332.04] backdoors in there.
[1332.26 → 1334.08] They don't, even non-intentional, right?
[1334.14 → 1336.76] Even maybe, you know, just the way it works.
[1336.94 → 1340.28] When we started this, people thought that a string copy was okay, right?
[1340.30 → 1345.18] People thought that, you know, a little catch between a memory copy in the OS was okay.
[1345.24 → 1348.98] And then we realized that you can drive birth overflows, ridiculous exploits through it,
[1349.02 → 1349.14] right?
[1349.14 → 1355.46] So I think we're in a nation state at the moment now, like in early days of understanding everything
[1355.46 → 1356.40] you can do with a model.
[1356.76 → 1362.24] So my kind of view in this is that models that you want to use on that, you know, how
[1362.24 → 1365.96] to use models secure should be read-only, should not learn.
[1366.46 → 1369.46] You don't want them to almost bring any content.
[1369.68 → 1370.88] You want to give you the content.
[1371.20 → 1376.06] You run them in complete isolation, and you assume that whatever you put on it is already
[1376.06 → 1380.36] exposed, and you verify the hell out of what comes out of it, right?
[1380.36 → 1383.94] And I think there are a lot of companies who are rushing into pushing models.
[1384.48 → 1390.12] The problem is that they not take into account that the models themselves are ridiculously
[1390.12 → 1390.72] powerful.
[1391.20 → 1395.52] And this is where you want to imagine that somebody can put a payload that is then executed
[1395.52 → 1396.10] by a model.
[1396.46 → 1401.26] And that model sits now in the middle of your organization, in your cloud, in your environment,
[1401.80 → 1405.30] who probably has access to APIs or other assets, right?
[1405.34 → 1408.04] That is ridiculously dangerous, right?
[1408.04 → 1409.46] And that's what we're doing, right?
[1409.50 → 1414.70] So I think in one hand, I think we need to be very careful in putting models in line
[1414.70 → 1419.74] in how we actually validate the inputs and the outputs, which is kind of why I view them
[1419.74 → 1421.98] in multi-tier sort of flows.
[1422.46 → 1426.94] And on the other hand, when we use them safely, they're ridiculously powerful because
[1426.94 → 1431.68] going to your first form how to use them for cybersecurity, what I really like is that
[1431.68 → 1437.60] I always felt that the way the model for cybersecurity is a model based on the attacker making
[1437.60 → 1438.08] a mistake.
[1438.50 → 1440.84] It's not about you protecting everything.
[1441.40 → 1446.60] It's about you want the attacker to make a mistake, i.e. make a call that was not supposed
[1446.60 → 1451.96] to happen, make a download, make a connectable connection, access the application in ways
[1451.96 → 1457.36] that no user will access it, call web services that are completely out of sequence, right?
[1457.44 → 1460.50] In the past, again, it was impossible to model this, right?
[1460.50 → 1466.48] We tried increasing technologies, even people that we created ridiculous installations of
[1466.48 → 1467.60] seams and technology, et cetera.
[1467.66 → 1468.68] They really struggled that.
[1469.08 → 1470.96] But I think we now have a good chance of doing that.
[1471.04 → 1476.96] So that means that we can now create much more, I would say, hostile environments for attackers
[1476.96 → 1482.20] because we force them to follow the paths of the users, which, by the way, they don't
[1482.20 → 1485.92] know what those paths are unless they're already in your system, right?
[1485.92 → 1491.76] So I think we have a chance of using that, but what we need is we need models that are
[1491.76 → 1493.16] really, really reliable.
[1493.58 → 1499.84] So OWASP has an amazing top 10 for applications, has a perfect top 10 for Gen AI models,
[1499.96 → 1500.08] right?
[1500.26 → 1501.06] Et cetera, LLMs.
[1501.36 → 1507.38] What I think about is most of that is trying to deal with the fact that the models can learn
[1507.38 → 1512.08] and the models can actually be, you know, don't have deterministic outputs.
[1512.08 → 1518.28] And I like the idea of actually turning the tables around and say, hey, I don't want my
[1518.28 → 1519.08] model to learn.
[1519.48 → 1525.24] I want the data that my model has access to be completely determined by the session and
[1525.24 → 1529.60] the state that that request comes in, which is normal App Sec, right?
[1529.74 → 1533.26] And ideally, I don't even want the model to have knowledge, right?
[1533.28 → 1538.48] I want to give the model the knowledge that it's going to use, so I control hallucinations,
[1538.88 → 1539.02] right?
[1539.06 → 1541.62] Like, you know, Chris, you know, you talk about your operation, right?
[1541.62 → 1546.74] Like, you don't want the Gen AI doing the operation on your back to slowly go off-piste,
[1546.82 → 1547.00] right?
[1547.36 → 1550.14] And start doing an operation on your leg, right?
[1550.50 → 1555.66] So in this theory would be that you want, for example, the Gen AI model that is facilitating
[1555.66 → 1561.14] your operation to only know about back stuff or maybe to know general things about the
[1561.14 → 1562.04] body, understand that.
[1562.12 → 1567.34] But the domain knowledge that it has should be laser sharp focus to the situation that
[1567.34 → 1567.88] you're in.
[1567.88 → 1571.54] And then that's how you control hallucinations, right?
[1571.84 → 1577.60] So I think the fundamental problem that we actually went backwards in security is that
[1577.60 → 1581.28] we now don't have a separation between code and data, right?
[1581.36 → 1585.90] And that's, I don't think we speak enough about this because for me, that's a massive
[1585.90 → 1586.62] problem, right?
[1586.72 → 1591.66] It's a massive problem because we really need to be able to distinguish what is code, what
[1591.66 → 1593.72] is data, what's an input, what's a command.
[1593.72 → 1598.68] So I'm doing a lot of stuff where I go from JSON to JSON and the latest model to this better
[1598.68 → 1601.08] where I almost want an API coming in.
[1601.18 → 1606.42] I give that API, which I can form nicely with data validation and stuff to the model.
[1606.56 → 1612.12] And then the model output itself is an API that is completely strongly typed.
[1612.12 → 1615.34] So I understand the output, if that makes sense.
[1615.72 → 1616.22] It does.
[1616.32 → 1616.78] It does.
[1616.78 → 1622.04] And just on the side, I'll just say I might actually need that operation on my leg too,
[1622.16 → 1627.32] but I would prefer it was a separate operation that we planned out just to note it.
[1627.96 → 1633.60] It's funny, as you were taking us through that, I have a bunch of different pages up
[1633.60 → 1638.78] here relating to things we're talking about, including on the OAuth site, that top 10 for
[1638.78 → 1640.26] LLMs and generative AI apps.
[1640.44 → 1642.04] And ironically, you were going through that.
[1642.04 → 1645.82] And I was like, wow, they already have this amazing list, which kind of addresses these
[1645.82 → 1647.08] things you were talking about.
[1647.26 → 1648.94] And then you referenced it explicitly.
[1648.94 → 1653.70] I was wondering, could you kind of take us through how was that generated?
[1654.40 → 1655.30] What's the thinking?
[1655.42 → 1660.00] Because it looks, based on everything you were saying, it looks like almost a roadmap of
[1660.00 → 1664.06] the things that one needs to be thinking about when going through the process.
[1664.30 → 1665.62] Could you take us through that a little bit?
[1665.88 → 1666.76] Well, I think you just nailed it.
[1666.84 → 1669.98] I feel that what you have there is the team who did it.
[1670.02 → 1671.68] And I wasn't very involved in it.
[1671.68 → 1675.10] I was a little bit on the outskirts of that project because I thought they were doing
[1675.10 → 1675.88] amazing work, right?
[1676.22 → 1678.06] Is that they had a used consultation period, right?
[1678.06 → 1679.02] They talked to a lot of people.
[1679.18 → 1682.36] They basically, they listed a lot of the stuff that goes wrong.
[1683.02 → 1687.42] What I think is interesting about that is I think that that whole list has a bias for
[1687.42 → 1690.70] the teams that are kind of deploying their own solutions, right?
[1690.98 → 1693.20] And it kind of covers a lot of those things, right?
[1693.48 → 1698.44] I kind of feel that a lot of that needs to be addressed by the people that provide the
[1698.44 → 1699.44] models, right?
[1699.44 → 1703.68] And I think more and more, I almost, you know, it gets to the point where you don't want to
[1703.68 → 1704.82] build your own cryptography, right?
[1704.82 → 1707.54] You want to use cryptography models that are very robust.
[1707.96 → 1710.48] It gets to the point where somebody's like, you shouldn't be building your own model.
[1710.68 → 1714.68] It's like, look, unless you have a hell of a team, and you really know what you're doing
[1714.68 → 1716.40] on that area, right?
[1716.76 → 1719.84] Most organizations, I don't think should be building models, right?
[1719.84 → 1726.54] Because the big paradigm shift for me was when the prompts are where the action is, right?
[1726.56 → 1729.88] And even if you look at things like Claude and the recent now that people are sharing
[1729.88 → 1734.60] the prompts for those things, you see how much the prompt is actually impacting, right?
[1734.88 → 1735.48] The stuff.
[1735.70 → 1739.64] So going back to the top 10, I think it's a great roadmap for people who are deploying
[1739.64 → 1742.32] their models to go, do I have to care about this?
[1742.40 → 1743.32] Does this apply to me?
[1743.32 → 1747.16] How do I answer this effectively, right?
[1747.28 → 1748.52] Because I think that's very important.
[1765.24 → 1773.14] You know, when we started podcasting back in 2009, an online store was just the furthest
[1773.14 → 1774.22] thing from our minds.
[1774.62 → 1779.72] Now we have merch.changelog.com, and you can go there right now and order some t-shirts
[1779.72 → 1781.44] and that's all powered by Shopify.
[1782.20 → 1783.58] What do we do before Shopify?
[1783.74 → 1784.82] I'll tell you, we did nothing.
[1784.94 → 1785.66] We couldn't sell.
[1785.90 → 1788.92] There were other ways, of course, but they were very hard, very difficult.
[1789.40 → 1795.22] Shopify let us build out an entire front end, obviously branded like changelog is.
[1795.42 → 1796.34] It's amazing.
[1796.60 → 1798.26] Merch.changelog.com.
[1798.26 → 1802.44] And our favourite feature is we use their API to generate a new coupon code,
[1802.44 → 1807.76] a personalized coupon code for every guest that comes on our podcast, and they get a free
[1807.76 → 1809.92] t-shirt from our merch store.
[1810.14 → 1810.90] And that's so cool.
[1811.22 → 1812.32] They choose the shirt they want.
[1812.46 → 1813.84] They use the coupon code.
[1813.92 → 1815.78] It arrives free of charge to them.
[1815.84 → 1817.70] And life is amazing.
[1818.04 → 1824.48] But also you can go there right now to merch.changelog.com and buy some threads yourself.
[1824.60 → 1825.60] And that's awesome as well.
[1825.60 → 1829.62] So upgrade your business and get the same checkout we use with Shopify.
[1830.14 → 1837.72] Sign up for your $1 per month trial period at shopify.com slash practical AI, all lowercase.
[1838.06 → 1841.62] Go to shopify.com slash practical AI to upgrade.
[1841.80 → 1842.82] You're selling today.
[1843.14 → 1846.82] Again, shopify.com slash practical AI.
[1846.82 → 1847.16] Bye.
[1867.64 → 1875.10] Well, Dennis, I'm really fascinated by this concept that you brought up about separating the model
[1875.10 → 1876.02] and the data.
[1876.72 → 1879.22] You phrased that in various ways.
[1879.70 → 1882.56] It sounds like you've been thinking about this concept a lot.
[1883.04 → 1887.34] I'm wondering if you could bring that to a practical level maybe for those out there that are
[1887.34 → 1890.10] kind of wondering, like maybe in both cases.
[1890.10 → 1896.68] So I'm using a closed model provider like OpenAI or Anthropic or something like that.
[1896.80 → 1897.62] There's that scenario.
[1897.78 → 1901.74] There's also people that are hosting their own model or even running it locally on their laptop
[1901.74 → 1904.60] with a local model server.
[1904.60 → 1909.98] From your perspective, what are the interactions between kind of model and data or like, as
[1909.98 → 1916.50] you put it, knowledge and model that are relevant in those scenarios to create either goodness
[1916.50 → 1918.98] or badness in each of those scenarios?
[1919.52 → 1924.84] So I think the first very important thing that is very relevant today that wasn't, I would
[1924.84 → 1929.18] say, six months ago is that we need to move from this idea that you have one model, right?
[1929.18 → 1933.80] What you have now is you have an ecosystem where you have multiple models, right?
[1933.92 → 1939.44] And they will go from probably some of the most commercial, if that fits your model that
[1939.44 → 1944.46] you want to use, to the open source one, but also from the most powerful to the least powerful,
[1944.68 → 1944.84] right?
[1944.94 → 1949.12] Because what you want is this mode where you start with, I want to do X, right?
[1949.36 → 1953.54] And with X, you want to start figuring out what is the best model, and sometimes what is
[1953.54 → 1958.08] the best combination of models that will give me that output, right?
[1958.08 → 1965.28] Because in a weird way, the best deterministic way to do something is code or to have the
[1965.28 → 1967.30] the least amount of moving parts in there.
[1967.72 → 1970.90] So, and because also remember, there's a cost issue here, right?
[1971.10 → 1975.84] So the more you use the models, you want a situation where you're firing this model analysis
[1975.84 → 1976.48] all the time.
[1976.48 → 1982.06] Now, if every one of those is hitting an open AI endpoint, that will get very expensive
[1982.06 → 1984.30] very fast, but it's not just that, right?
[1984.34 → 1986.66] Sometimes you don't want that whole package.
[1986.76 → 1987.86] You don't need all of that.
[1987.92 → 1992.42] If you just want a summary, or you want a validation, you want this, there are now a lot more models
[1992.42 → 1996.76] and there are models who are specializing in specific things who have certain bias that
[1996.76 → 1998.52] you want to have those bias, right?
[1998.60 → 1999.86] In terms of that.
[2000.30 → 2004.52] And so I think it's important to start thinking not just of one model, but the sequence of models,
[2004.52 → 2007.12] but also what is the best model that you have.
[2007.52 → 2010.96] And the open source models, the reason why they're a game changer, right?
[2011.10 → 2017.78] Is because suddenly you can now run models, let's say with Obama, on a desktop CPU with
[2017.78 → 2018.94] distance speed, right?
[2019.06 → 2023.86] And distance speed might not be like, you know, the real time now we now get to ChatGPT and
[2023.86 → 2028.52] Cloud3, et cetera, but maybe even how ChatGPT was a year ago or two years ago.
[2028.76 → 2033.14] But what it means, it means that if that's on your pipeline, you now have a pipeline that is
[2033.14 → 2034.42] one of CPU, right?
[2034.54 → 2036.20] You don't even need GPUs now.
[2036.38 → 2040.52] You can if you can, of course, if you have them, and you can afford them, it fits your model.
[2040.82 → 2047.34] But it's CPU level that can run a model that is completely isolated from the internet.
[2047.58 → 2048.84] And I think it's very important.
[2048.92 → 2053.94] I think it's very important you have a design that has those workflows because you start to
[2053.94 → 2055.80] introduce them as part of your workflows.
[2056.22 → 2061.22] In a way, the key answer to your question is people need to pick up a use case, right?
[2061.22 → 2065.76] It doesn't need to be ridiculously complex, but pick a use case and then try to do that
[2065.76 → 2067.62] with a Gen AI workflow, right?
[2067.86 → 2072.54] And that workflow where in the past you had to code, now is a workflow that has multiple
[2072.54 → 2073.26] LLMs.
[2073.58 → 2075.18] It has multiple sequence.
[2075.50 → 2079.50] I have things where sometimes you create same question to three models, then you use a
[2079.50 → 2082.28] fourth one to analyze it and on that pipeline.
[2082.80 → 2087.02] And what I'm trying to do with the Cyber Boardroom is fundamentally tried to address in cybersecurity
[2087.02 → 2093.06] how to communicate, how to translate cybersecurity knowledge to board members or executives,
[2093.06 → 2098.88] but also how to get those executives to ask good questions and to translate what they care
[2098.88 → 2099.20] about.
[2099.68 → 2104.38] So a really cool use of technology is to think about translation, right?
[2104.54 → 2110.54] So for example, if in the past as a CIO, I produced reports and briefings for a lot of
[2110.54 → 2113.74] people, but I didn't customize them because it didn't scale, right?
[2113.74 → 2118.70] Now I have the ability to create a customized version for Daniel, right?
[2118.80 → 2124.64] And take into account your culture, your language, your context, your level of interest.
[2124.92 → 2125.48] Do you care?
[2125.58 → 2126.12] Don't you care?
[2126.24 → 2127.26] What's your focus?
[2127.62 → 2130.08] And I have another version for Chris, right?
[2130.22 → 2133.38] So maybe Daniel, you're a lot more focused on the financial element.
[2133.78 → 2136.14] Chris might be more focused on the strategic element of it.
[2136.32 → 2143.24] So I now have the ability to translate a bit of knowledge into very specific domains of one,
[2143.24 → 2143.70] right?
[2143.80 → 2145.60] Because I can feed the knowledge.
[2146.02 → 2149.56] I can feed what the background information, I can feed the audience.
[2150.12 → 2156.10] And then I can say ChatGPT or Claude or Llama or, you know, Gemini, translate this, right?
[2156.18 → 2157.76] And they are perfect at that.
[2157.86 → 2162.32] And they don't tend to hallucinate at that level because you create the parameters.
[2162.82 → 2165.20] So that's a good example of a use case, right?
[2165.30 → 2167.68] Which is very laser sharp, but adds a lot of value.
[2168.00 → 2170.44] Because, you know, imagine this is not just execs.
[2170.44 → 2173.54] Imagine you have the project manager, and you have a program manager, and you have the lead
[2173.54 → 2177.00] developer, and you have the QA and you have the marketing person, and you have the executive.
[2177.36 → 2182.86] You can now create briefs for every single one of them that puts into context why they
[2182.86 → 2183.16] care.
[2183.58 → 2184.54] Why is this important?
[2184.94 → 2189.54] Why this, you know, cybersecurity stuff means that when the marketing team does a campaign,
[2189.68 → 2194.16] the website doesn't block your users because you just have 50% more traffic.
[2194.16 → 2195.92] This is a real story, by the way.
[2196.38 → 2201.12] It's like, you know, we were attacked by our marketing department and run a prime-time TV
[2201.12 → 2201.40] ad.
[2201.84 → 2202.12] Great.
[2202.20 → 2203.48] But if you knew about it, right?
[2203.60 → 2205.26] We could have plans, right?
[2205.36 → 2210.18] So there's all this lack of communication that I think is fascinating to do in
[2210.18 → 2210.76] organizations.
[2210.94 → 2213.36] And in the past, this didn't scale, right?
[2213.58 → 2217.84] So if you now take into account that you now have multiple models with different level
[2217.84 → 2221.60] capabilities, you almost want to think, why is the most cost-effective?
[2221.80 → 2227.46] Why is the most deterministic way for me to chain this where, you know, you maybe use
[2227.46 → 2232.18] some cheaper models to do some stuff and then maybe use the last more expensive model to
[2232.18 → 2236.68] actually do some kind of Uber analysis and make sure that you still, it all makes sense,
[2236.72 → 2236.90] right?
[2237.14 → 2241.40] And of course, this should all be calibrated by the humans who start to calibrate the inputs
[2241.40 → 2243.52] and the outputs that go into the system.
[2243.52 → 2248.34] But that's why I feel that it's very, very exciting now that we're having this super
[2248.34 → 2252.64] competitive race between the different models, because we now have a huge amount of models
[2252.64 → 2258.16] to choose from, and you can now start to pick which is better for each capability, right?
[2258.26 → 2262.34] And that's why I want to see models that have no content, right?
[2262.36 → 2266.74] I want to see models that just have understanding and logic, right?
[2266.78 → 2271.66] It's almost like we need to find a way to strip away, you know, some of the content so
[2271.66 → 2274.48] that I can say, this is my policy, right?
[2274.54 → 2275.66] This is what I care about.
[2275.84 → 2276.82] This is my world.
[2277.22 → 2280.00] Because remember now, we now have big context windows, right?
[2280.10 → 2285.60] So you can now feed quite a lot of data in a prompt that goes into the model.
[2286.14 → 2290.86] It's really fascinating, you know, with what you're doing at the cyber boardroom in terms
[2290.86 → 2294.62] of kind of optimizing using the right models in the right way.
[2294.62 → 2297.96] And then I actually want to reach back a little bit to something you said a few minutes ago,
[2297.96 → 2302.76] where you were saying, you know, from a security concern, you wouldn't want most organizations
[2302.76 → 2307.64] to, for instance, build their own models from the ground up, you know, use these foundational
[2307.64 → 2314.88] models for which you have strong security basis in that you can trust and then optimize in the
[2314.88 → 2316.08] way that you were just discussing.
[2316.34 → 2321.28] I think you've really hit on something because I think a lot of organizations are really struggling
[2321.28 → 2327.40] with how to approach the different workflows to maximize their productivity and that output
[2327.40 → 2330.74] while staying secure and not exposing themselves.
[2331.30 → 2337.54] So you seem to have a perfect grasp of this workflow that maximizes the productivity
[2337.54 → 2342.88] and the efficiency for the different audiences while not getting them into trouble by doing
[2342.88 → 2345.40] something they're probably not well suited to do.
[2345.52 → 2346.38] Is that fair?
[2346.46 → 2348.08] Would you say that that's a fair way of...
[2348.08 → 2349.62] Yeah, it's a nice compliment.
[2349.76 → 2350.04] Thank you.
[2350.14 → 2352.10] But that's what I'm trying to do, right?
[2352.14 → 2354.80] I kind of call it deterministic, Gen AI.
[2355.24 → 2357.82] And people go, well, but, you know, it's not supposed to be deterministic.
[2357.94 → 2360.16] I'm like, I'm going, yeah, but that's a problem, right?
[2360.24 → 2363.06] Like, first, there's a cool side of it for creativity.
[2363.50 → 2363.72] Great.
[2364.04 → 2365.94] We already have that, right?
[2366.18 → 2371.44] What I think is interesting is to leverage that ability to understand context and to write
[2371.44 → 2375.88] in English or write in Portuguese or write whatever language you want and to do that
[2375.88 → 2380.46] translation layer, but to be very deterministic, which also means that we need to be much
[2380.46 → 2385.60] better at provenance, which is basically that path of this, quits, that, quits, this, quits,
[2385.70 → 2385.88] this.
[2386.06 → 2387.84] But also it's a way to scale, right?
[2387.84 → 2392.16] Because if you start to have provenance on good sources of information, then you don't
[2392.16 → 2394.10] have to do this all the time, right?
[2394.10 → 2396.70] You can build your knowledge base, right?
[2396.72 → 2399.96] You can build your workflow base, and you can build your confidence.
[2400.58 → 2404.66] And then it's about creating these microservices that do one thing really well.
[2404.66 → 2405.48] Think about it.
[2405.58 → 2410.44] You don't want to microservice that change behaviour next week when a new model comes
[2410.44 → 2410.92] along, right?
[2411.16 → 2414.64] Dude, it's like we want deterministic stuff, right?
[2414.64 → 2416.68] Because we build things on top of that, right?
[2416.74 → 2420.32] So we need to start getting to these building blocks again components, right?
[2420.56 → 2423.54] That they do one thing, they do it really well, they are super reliable.
[2424.00 → 2428.18] Yes, there might be a model in the middle, but that means that the thing has this size
[2428.18 → 2429.74] versus that size, right?
[2429.74 → 2430.84] In terms of the capabilities.
[2431.42 → 2435.98] And more importantly, and I think, Daniel, you mentioned this before, is that this allows
[2435.98 → 2440.58] us to go to the business owners and let them be in a driving seat.
[2440.86 → 2441.78] Because think about it.
[2441.78 → 2443.00] In the past, we had forking.
[2443.14 → 2446.52] If you guys know what that is, when you write stuff in quasi-language.
[2446.90 → 2450.24] If when I do this, then I do that, or given this, given that.
[2450.44 → 2453.78] But that was always a hack because it was like fucking hardcore to the back end.
[2453.78 → 2457.12] Now we can actually have the business describe the intent.
[2457.50 → 2458.98] They can describe the workflows.
[2459.36 → 2463.46] They can describe what the experience they want for the user, for the data, even data
[2463.46 → 2464.16] transformations.
[2464.16 → 2469.32] We can start to describe what I want to get from here to there, right?
[2469.42 → 2475.48] And then it's about how can you lock it down in the most reliable piece of code and system,
[2475.66 → 2477.14] right, that can do that.
[2477.24 → 2480.84] Which is why having models that run offline are very important.
[2480.84 → 2485.72] Because that allows you to lock in, version control that thing, and then know that it
[2485.72 → 2489.72] will still go in two months, two years, five years, it will still do the same thing.
[2490.16 → 2491.34] And I think that's very important.
[2491.34 → 2495.80] So from a security point of view, what I've learned was every time you have a system that
[2495.80 → 2498.68] behaves like a black box, you have vulnerabilities, right?
[2498.72 → 2503.86] Like it's literally, you know, so we're creating an Uber black box, right, for this stuff.
[2504.00 → 2505.86] So what can go wrong, right?
[2505.86 → 2511.74] So in the past, I knew that the less the team tested, the less the team had architecture
[2511.74 → 2516.20] diagrams, the least they understood how a part of the application worked, the more vulnerabilities
[2516.20 → 2516.96] I was going to discover.
[2517.34 → 2518.72] Because they couldn't test it.
[2518.80 → 2523.74] It's almost like, how can the developer understand the side effects of what they're doing if
[2523.74 → 2525.04] they don't see it, right?
[2525.18 → 2529.84] So I think we have to be very careful by creating these black boxes, right, that we don't understand
[2529.84 → 2531.80] the behaviour and how it works.
[2531.80 → 2536.66] Something that is maybe brought into a little bit more clarity for me, as you were just
[2536.66 → 2540.34] describing what you just described with the black boxes.
[2541.08 → 2546.74] We had a few episodes ago, Chris, you remember we had the episode, I chatted with Donate when
[2546.74 → 2548.92] I was in London at With secure.
[2549.54 → 2553.18] And one of the things that he brought up, I'm curious that your perspective on Dennis is
[2553.18 → 2559.76] like these very, very large models, especially the closed ones have a huge attack surface,
[2559.76 → 2562.82] like the vulnerabilities, like they're so general.
[2563.22 → 2569.22] There's so much knowledge kind of embedded that it would be sort of impossible to think
[2569.22 → 2575.90] that you could kind of fully explore the space of behaviour and prevent things like jailbreaks
[2575.90 → 2579.02] or things like prompt injections, that sort of thing.
[2579.14 → 2586.14] Whereas sort of the smaller model you bring the data to is either going to perform really
[2586.14 → 2590.96] good if you bring the right data to the table, because it's not embedded in the model, or
[2590.96 → 2596.34] it's going to be complete trash output, which maybe is better because you're operating in
[2596.34 → 2599.22] a regime where the data distribution isn't what you expect.
[2599.38 → 2600.64] I'm curious if that tracks.
[2600.72 → 2602.02] And you can ask, you can verify.
[2602.44 → 2602.66] Yeah.
[2602.80 → 2603.90] I think that's spot on, right?
[2604.10 → 2609.20] Look, it tells you something that we still, it's almost like somebody had a cool analogy,
[2609.32 → 2611.56] like it feels like we're back in the navigation.
[2611.74 → 2614.62] Like Portuguese has a great history of discovering the world, right?
[2614.62 → 2617.60] So at school, we learned how the Portuguese, right?
[2617.86 → 2620.24] And the Spanish and everybody else were like, what's out there?
[2620.30 → 2621.24] Let's stand a boat, right?
[2621.28 → 2622.78] And then, hey, look, we discovered a country.
[2622.88 → 2624.76] We discovered, you know, something, right?
[2625.08 → 2629.48] It feels a lot of these models are like that, which in a weird way is ridiculously scary.
[2629.88 → 2630.98] Like, imagine like-
[2630.98 → 2631.78] There'd be dragons.
[2631.98 → 2632.44] You know, yeah.
[2632.50 → 2635.10] Imagine you're running an app, you do web service, you ship, and you go, hey, do you
[2635.10 → 2636.08] know that thing knows chemistry?
[2636.32 → 2639.54] It's like, well, well, you know that thing speaks 20 languages?
[2640.24 → 2644.60] Well, I mean, so I think we, we, it's the fact that we still have a lot of
[2644.60 → 2649.68] we talk about emergent properties and the fact that people still talk about what the
[2649.78 → 2652.18] what the models do by probing it, right?
[2652.22 → 2658.22] Like from the outside as a ridiculous black box, that shows you how immature we still are
[2658.22 → 2659.24] in that level, right?
[2659.38 → 2664.04] Like, yes, software is complex, but we can actually understand kind of what it does,
[2664.40 → 2664.58] right?
[2664.62 → 2668.42] Like we can actually, you know, okay, given the time and money, we could actually reverse
[2668.42 → 2672.72] engineer even the most complex piece of software and go, yes, this thing is not going to
[2672.72 → 2673.60] know chemistry, right?
[2673.66 → 2675.86] This thing is not going to do beyond this.
[2676.10 → 2680.02] It might do some bugs, but it has a limited operation space, right?
[2680.32 → 2684.90] I think the models, in a way, it's a good thing in some aspects, but they have all these
[2684.90 → 2689.46] properties because they build these huge three-dimensional or multiple-dimensional
[2689.46 → 2690.32] views of it.
[2690.52 → 2692.92] But that's not what you want for mission-critical systems.
[2693.32 → 2695.06] And that's what I was talking about exploits.
[2695.06 → 2700.50] My prediction is there's going to be a number of exploits, backdoors, and seekers of instructions,
[2701.12 → 2706.72] my crazy ASCII characters, crazy X amount of characters, whatever, math numbers, whatever,
[2706.94 → 2711.56] that will trigger the models to go into a place that they do crazy stuff.
[2711.86 → 2715.26] But we don't know that because we don't understand like the models, right?
[2715.36 → 2717.14] Like people hack a model almost in English.
[2717.28 → 2720.20] Oh, pretend that you're now writing in ASCII art and you do this.
[2720.20 → 2725.34] If you think about it from an exploit point of view, that is very basic, right?
[2725.46 → 2731.34] Like there's going to be way more ridiculous, complex, but interesting, well, I guess from
[2731.34 → 2735.88] a scary point of view, type of exploits that people will have once you start to understand
[2735.88 → 2738.10] how it works inside, right?
[2738.18 → 2743.86] Which is why I think we also need to start measuring almost like what is the behaviour
[2743.86 → 2745.06] of models, right?
[2745.06 → 2750.72] Like how do they arrive at those conclusions and then even have models that can only do
[2750.72 → 2751.34] those bits?
[2751.76 → 2752.82] Does that make sense?
[2753.20 → 2753.36] Right?
[2753.46 → 2755.86] So again, I want deterministic models.
[2756.00 → 2761.68] I want models that I can start to vouch for how they work and how they do, even if maybe
[2761.68 → 2765.40] sometimes they're a little bit less efficient, but you earn the explainability.
[2765.40 → 2772.16] So I want you to actually, as we're starting to wind up here, I would like to ask you to
[2772.16 → 2777.84] even extend that a little bit in terms of kind of where you think that's going to go,
[2777.92 → 2783.06] because you've already touched on, you know, trying to get to more deterministic models and
[2783.06 → 2784.94] some of the things you're expecting.
[2785.20 → 2791.90] If you were to blow that out in a slightly longer time horizon, maybe several years, where
[2791.90 → 2794.76] do you think all this is going to go, and how do you think it might get there?
[2795.48 → 2799.20] Speculatively, like recognizing that we're just doing the crystal ball and asking you
[2799.20 → 2802.48] to tell us kind of when you go to bed at night, and you're thinking about this, what do you
[2802.48 → 2803.08] think is going to happen?
[2803.48 → 2803.64] Okay.
[2803.70 → 2804.62] There are multiple areas, right?
[2804.74 → 2812.52] I think, I feel on the whole fake news creation of crazy content using AI for the attack, that's
[2812.52 → 2813.26] going to grow, right?
[2813.28 → 2814.46] There's business models around it.
[2814.46 → 2819.44] I actually think that's going to force us to have deterministic improvidence on news.
[2819.60 → 2821.10] So I think that's a good thing, right?
[2821.28 → 2824.60] It's going to be bad, but it's going to force us to address that problem, right?
[2824.76 → 2828.84] There is a level here that we're going to have to control it, just like we control nuclear
[2828.84 → 2829.48] weapons, right?
[2829.52 → 2829.96] Other things.
[2830.08 → 2832.84] I think there's a level here that we have to be careful, right?
[2833.00 → 2835.70] Not to create things that go completely out of control.
[2836.06 → 2838.82] And we might have a couple, but that's a bigger problem, right?
[2838.82 → 2839.56] That needs to be addressed.
[2839.96 → 2844.36] Where I think we're going to have the biggest impact is like, I think Kevin Kelly had a great
[2844.36 → 2845.66] phrase in one of his books.
[2845.70 → 2847.96] He talks about AI even before Chats of Petit.
[2848.36 → 2850.94] But he talked about AI will become like electricity, right?
[2850.94 → 2854.58] You'll become embedded in all these little things, but it's not a massive thing.
[2854.66 → 2855.72] It's little bits, right?
[2855.92 → 2860.08] It's little things that you slowly start to have that introduce a level of intelligence
[2860.08 → 2862.10] that we don't have today, right?
[2862.22 → 2866.12] So if you think of most of our interactions, they don't have a lot of intelligence, right?
[2866.22 → 2867.04] They don't learn.
[2867.20 → 2868.22] They don't, you know...
[2868.22 → 2872.62] But I think as, again, the models become small to run in your phones, as the models
[2872.62 → 2877.98] become small to run in microservices, I think what would be very powerful is the creation
[2877.98 → 2882.12] of these little, lots and lots and lots of little use cases that really make a difference.
[2882.38 → 2884.24] And then you start to trust it, right?
[2884.32 → 2887.14] And then you compound them on each other, right?
[2887.26 → 2892.66] And my instinct is that anything that relies on a black box eventually will blow up, right?
[2892.68 → 2896.20] And when it blows up, people push back and going, whoa, whoa, whoa, we can't have that.
[2896.26 → 2899.28] It's okay for proof of concepts, but that cannot be doing stuff.
[2899.28 → 2905.10] Also, because technology now, I think, had got to a point where we would drown in complexity,
[2905.10 → 2905.48] right?
[2905.50 → 2909.36] We would drown in all sorts of things that, you know, we don't fully understand.
[2909.46 → 2912.60] They don't connect the dots and even application systems.
[2912.74 → 2915.36] And they're so complex and companies are so complex, right?
[2915.48 → 2921.36] I think understanding them in the smallest way, that will dramatically change.
[2921.76 → 2923.18] That's how you change society, right?
[2923.18 → 2927.64] You change society by literally introducing something that becomes really powerful, really
[2927.64 → 2928.02] useful.
[2928.74 → 2932.90] And the final point I want to make here is I think there's a ridiculous opportunity for
[2932.90 → 2934.80] reframing education, right?
[2934.80 → 2940.24] And to finally create a learning environment that individuals can be learned in the best
[2940.24 → 2941.56] way for them, right?
[2941.62 → 2944.82] So I think we can change away how we learn, continuous learning.
[2945.02 → 2949.86] It's a big thing, but also how we change the education from being like a memory kind of
[2949.86 → 2951.42] exam-based stuff, right?
[2951.50 → 2953.82] To actually be about learning, right?
[2953.98 → 2958.22] And now it's about creating customized learning paths to the individuals, right?
[2958.22 → 2964.32] And, but also, I guess just the final point is that this means that the human is literally
[2964.32 → 2966.22] the one that is ridiculously important here.
[2966.34 → 2971.74] This is a tool to help, you know, the human to be even more productive the same way that
[2971.74 → 2974.80] we use the internet, the same way that we use the hammer, the same way we use electricity.
[2975.16 → 2977.46] It's just a different one, right?
[2977.50 → 2981.18] That we had before because you can understand language.
[2981.18 → 2983.12] And we never had that before, right?
[2983.12 → 2988.60] So I think it's an insane opportunity, you know, but the attack side, yes, you will go,
[2989.10 → 2993.60] but we didn't need, we didn't need Gen.AI for people to create ridiculous attacks, right?
[2993.74 → 2997.74] But on the defence side, I think it changed the nature of the game, right?
[2997.74 → 2999.14] So I think it's very exciting about that.
[2999.28 → 3001.04] I hope that answered your question.
[3001.40 → 3002.12] It was a great answer.
[3002.36 → 3002.74] It's awesome.
[3002.90 → 3003.06] Yeah.
[3003.06 → 3005.24] Thank you so much for taking time, Dennis.
[3005.30 → 3005.98] This has been great.
[3006.12 → 3011.72] I really have been looking forward to this and love the conversation, love this idea of
[3011.72 → 3016.08] kind of thinking about knowledge and data and model and how those are connected or not
[3016.08 → 3016.46] connected.
[3016.92 → 3018.88] Please continue your great work.
[3018.98 → 3020.30] It's a great contribution.
[3020.64 → 3022.78] And yeah, thank you so much for taking time.
[3022.84 → 3023.40] It's been a pleasure.
[3023.74 → 3024.10] My pleasure.
[3024.48 → 3025.20] Great talking to you guys.
[3028.92 → 3031.74] Thank you for listening to Practical AI.
[3031.74 → 3033.22] You know, what's cool?
[3033.52 → 3034.36] Free stickers.
[3035.02 → 3040.46] During the month of September, we're mailing out changelog sticker packs to everyone who
[3040.46 → 3045.34] leaves us a thoughtful five-star review or blog post about our pods.
[3045.92 → 3052.84] Simply email proof of your review to stickers at changelog.com alongside your address, and we'll
[3052.84 → 3055.30] mail out the goods anywhere in the world.
[3055.66 → 3058.68] Once again, that's stickering at changelog.com.
[3059.02 → 3060.38] Picks, or it didn't happen.
[3060.38 → 3062.22] Only in the month of September.
[3062.56 → 3063.24] Let's do this.
[3063.64 → 3069.76] Thanks again to our partners at Fly.io, to our Beat Freak in residence, the one and only
[3069.76 → 3073.38] Break master Cylinder, and to our longtime sponsors at Sentry.
[3073.84 → 3078.84] Use code changelog when signing up for a new Sentry team plan and save a hundred bucks.
[3079.44 → 3080.60] That's all for now.
[3080.86 → 3082.42] We'll talk to you again next time.
[3082.42 → 3105.66] present
[3105.66 → 3106.94] together.
