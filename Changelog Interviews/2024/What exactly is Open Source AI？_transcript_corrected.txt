[0.00 → 18.10] Welcome back friends, this is the Changelog.
[18.38 → 23.02] I'm Adam Stachowiak and this week we're joined by Stefano Moduli, the Executive Director
[23.02 → 26.22] of the Open Source Initiative, the OSI.
[26.22 → 30.94] The Open Source Initiative is responsible for representing the idea and the definition
[30.94 → 32.82] of open source globally.
[33.36 → 39.50] Stefano shares the challenges they face as a US-based organization with a global impact.
[39.76 → 45.56] We discuss the work Stefano and the Open Source Initiative are doing to define open source
[45.56 → 49.44] AI and why we need an accepted and shared definition.
[50.00 → 55.78] Of course, we also talk about the potential impact if a poorly defined open source AI
[55.78 → 57.02] emerges from their efforts.
[57.50 → 61.26] I also want to mention that Stefano was feeling under the weather for this conversation, but
[61.26 → 64.36] he powered through because of how important this topic is.
[64.72 → 71.28] A massive thank you to our friends and our partners at Fly.io, the home of changelog.com.
[71.68 → 73.98] It's simple, launch apps near users.
[74.48 → 79.62] They transform containers into micro VMs that run on their hardware in 30 plus regions on
[79.62 → 80.30] six continents.
[80.96 → 83.56] Launch an app for free at Fly.io.
[83.56 → 83.68] Fly.io.
[94.28 → 95.40] What's up, friends?
[95.52 → 100.12] This episode of the changelog is brought to you by our friends over at Tercel.
[100.48 → 102.90] And I'm here with Lee Robinson, VP of product.
[103.66 → 107.88] Lee, I know you know the tagline for Tercel, develop previous ship, which has been perfect,
[107.88 → 110.40] but now there's more after the ship process.
[110.66 → 116.80] You have to worry about security, observability, and other parts of just running an application
[116.80 → 117.34] production.
[117.64 → 118.38] What's the story there?
[118.52 → 120.68] What's beyond shipping for Tercel?
[121.08 → 121.34] Yeah.
[121.44 → 125.02] You know, when I'm building my side projects or when I'm building my personal site, it
[125.02 → 126.64] often looks like develop preview ship.
[126.74 → 128.30] You know, I try out some new features.
[128.40 → 129.44] I try out a new framework.
[129.44 → 131.90] I'm just hacking around with something on the weekends.
[132.42 → 133.16] Everything looks good.
[133.24 → 133.48] Great.
[133.62 → 134.14] I ship it.
[134.24 → 134.62] I'm done.
[134.96 → 138.74] But as we talk to more customers, as we've grown as a company, as we've added new products,
[139.16 → 144.04] there's a lot more to the product portfolio of Tercel nowadays to help pass that experience.
[144.16 → 148.22] So when you're building larger, more complex products, and when you're working with larger
[148.22 → 150.86] teams, you want to have more features, more functionality.
[151.12 → 155.58] So tangibly, what that means is features like our Tercel Firewall product to help you
[155.58 → 158.04] be safe and to have that layer of security.
[158.04 → 162.74] Features like our logging and observability tools so that you can understand and observe your
[162.74 → 167.14] application and production, understand if there are errors, understand if things are running smoothly
[167.14 → 168.78] and get alerted on those.
[169.20 → 174.32] And also then really an expansion of our integration suite as well, too, because you might already
[174.32 → 179.94] be using a tool like a data dog, or you might already be using a tool at the end of this software
[179.94 → 184.50] development lifecycle that you want to integrate with to continue to scale and secure and observe
[184.50 → 185.32] your application.
[185.32 → 187.82] And we try to fit into those as well, too.
[187.82 → 193.40] So we've kind of continued to bolster and improve the last mile of delivery.
[194.24 → 194.82] That sounds amazing.
[195.00 → 197.36] So who's using the Tercel platform like that?
[197.56 → 198.52] Can you share some names?
[199.14 → 204.22] Yeah, I'm thrilled that we have some amazing customers like Under Armour, Nintendo, Washington
[204.22 → 210.46] Post, Zapier, who use Tercel's running cloud to not only help scale their infrastructure,
[210.68 → 215.08] scale their business and their product, but then also enable their team of many developers
[215.08 → 220.48] to be able to iterate on their products really quickly and take their ideas and build the
[220.48 → 221.14] next great thing.
[221.64 → 221.94] Very cool.
[222.16 → 227.78] With zero configuration for over 35 frameworks, Tercel's running cloud makes it easy for any
[227.78 → 228.88] team to deploy their apps.
[229.22 → 235.12] Today, you can get started with a 14-day free trial of Tercel Pro or get a customized enterprise
[235.12 → 236.30] demo from their team.
[236.30 → 240.40] Visit Vercel.com slash changelog pod to get started.
[240.60 → 245.28] That's V-E-R-C-E-L dot com slash changelog pod.
[266.30 → 274.00] Well, Steph, no, it's been a while.
[274.78 → 277.00] Actually, never, which is a good thing, I suppose.
[277.10 → 277.84] But now we're here.
[278.54 → 278.94] Fantastic.
[279.26 → 284.36] We were at All Things Open recently, and we tried to sync up with you, but we missed the
[284.36 → 284.88] message.
[285.20 → 286.94] And so we were like, we got to get you on the podcast.
[286.94 → 291.46] And obviously, you know, this show, The Change of the World was born around open source.
[291.46 → 298.66] And I kind of find it strange and sad that we've never had anybody from the open source
[298.66 → 299.94] initiative on this podcast.
[300.38 → 302.44] It's, I'm glad you're here to change that.
[302.58 → 303.34] So welcome.
[303.66 → 304.30] Thank you.
[304.54 → 305.62] Thank you for having me.
[305.84 → 306.26] It's a pleasure.
[306.94 → 308.00] Sorry, we missed it.
[308.32 → 311.00] We missed each other in South Carolina.
[311.32 → 312.64] It was a great event.
[312.92 → 313.34] Oh, man.
[313.38 → 314.68] We love All Things Open.
[314.76 → 316.20] We love Todd and their team there.
[316.38 → 320.60] We think All Things Open is the place to be at the end of the year.
[320.60 → 320.92] Oh, for sure.
[320.92 → 325.64] If you're a fan of open source, you're a navigator of open source, and just the way that it's
[325.64 → 327.80] permeating all software, right?
[327.82 → 328.18] It's one.
[328.28 → 329.10] Open source is one.
[329.52 → 333.64] And now we're just living in a hopefully mostly open source world, right?
[335.14 → 335.58] Absolutely.
[335.98 → 336.38] Absolutely.
[336.38 → 343.90] I mean, just last week, it was an article published that estimated the value of open
[343.90 → 345.36] source software as a whole.
[345.74 → 347.70] The numbers are incredible.
[347.70 → 355.08] Like these researchers from Harvard Business School went and looked at the value of open
[355.08 → 361.04] source as it is consumed or produced, and they put dollar numbers on it.
[361.04 → 363.70] I envy those people because I don't know how.
[363.88 → 364.64] I'm not an analyst.
[365.20 → 367.12] Jared, maybe you're like a somewhat of an analyst, right?
[367.18 → 369.60] Like you have an analytical brain from how I know of you.
[369.92 → 370.02] Okay.
[370.12 → 372.32] I don't know how you would quantify the value of open.
[372.36 → 377.06] I mean, I know it's quite valuable, but literally, how do you value, how do you quantify the value
[377.06 → 377.58] of open source?
[377.70 → 378.58] Like what do they do?
[378.64 → 380.48] What are the metrics they key off of?
[380.58 → 380.88] Do you know?
[380.88 → 382.76] They counted lines of code.
[383.08 → 384.70] They counted the hours.
[384.84 → 389.64] They estimated the hours that it would take to rewrite from scratch all the software that
[389.64 → 390.24] is in use.
[390.88 → 397.50] And they used datasets that are available already with some of those counts.
[398.10 → 402.96] And using those two datasets, they estimated the value that it would take to replicate all
[402.96 → 405.42] of the open source software that is available.
[405.72 → 409.02] And they put the numbers around $8.8 trillion.
[409.02 → 409.42] Wow.
[410.46 → 412.84] I would actually just say all the dollars, really.
[413.38 → 414.94] Personally, I would just say all the dollars.
[414.96 → 415.12] Yeah.
[415.18 → 416.26] Well, I mean, it's a huge number.
[416.66 → 417.48] All the dollars.
[417.64 → 417.80] Right.
[417.96 → 421.18] Doesn't every dollar today like really depend on open source at some layer?
[421.72 → 423.70] So like really, couldn't it be just all the dollars?
[424.06 → 424.84] Well, right.
[424.92 → 429.44] It's an impressive number, and it's really hard to picture it, how much, how big it is.
[429.44 → 432.50] I went, I had to go look it up and listen.
[432.82 → 436.54] So it's three times as much as Microsoft market cap.
[436.54 → 441.62] And it's larger than the whole of the United States budget.
[442.12 → 445.66] Like 2023's budget in the United States that includes the military.
[445.66 → 446.28] That's hard to beat.
[446.40 → 446.70] Medicare.
[447.06 → 448.58] 6.3 trillion.
[449.04 → 449.32] Whew.
[449.46 → 449.64] Yeah.
[450.00 → 450.98] That's a lot of trillions there.
[451.32 → 451.60] Right.
[451.80 → 453.26] More trillions than I've got, Jared.
[453.42 → 453.90] Of anything.
[454.64 → 454.78] Right.
[454.84 → 455.98] I don't get trillions of anything really.
[456.08 → 458.06] Maybe not even in cents.
[458.22 → 459.20] Can they get a trillion cents?
[459.62 → 460.42] I don't think so.
[460.90 → 461.96] You don't keep a bucket?
[462.32 → 462.66] I don't know.
[462.66 → 464.20] I almost asked Siri to tell me.
[464.24 → 466.10] You have to go turn those into the bank and see what they'll give you.
[466.58 → 468.72] Well, that's fun to think about, really.
[468.80 → 472.38] Well, I hear a number like 8.8 trillion, and I start to think, why don't you round that
[472.38 → 472.92] up to nine?
[473.60 → 477.48] And then I realized that's like a fifth of a trillion dollars if you're going to round
[477.48 → 477.62] it.
[477.66 → 478.64] That's a lot of money to round.
[479.54 → 483.70] That is a nice rounding error in your favour if it was your own dollars.
[484.12 → 484.40] Right?
[485.16 → 485.44] Oh, yeah.
[485.44 → 486.18] I wouldn't mind that.
[486.90 → 487.48] For sure.
[487.56 → 487.68] Yeah.
[487.68 → 488.22] Round it off.
[488.58 → 489.66] Hand it out to some folks.
[489.72 → 490.68] Hand it out to some maintainers.
[490.80 → 491.48] You know, that'd be nice.
[491.48 → 491.92] Yeah.
[492.44 → 497.36] Well, I don't know if everybody listening to this podcast will be, I think a lot of them
[497.36 → 497.80] will be.
[497.96 → 502.54] But, you know, in light of recent feedback, Jared, I don't want to assume that our listenership
[502.54 → 506.04] is super informed of what the open source initiative is.
[506.36 → 513.22] I can kind of read from the about page, Stefano, but I'd prefer that you kind of give us a taste
[513.22 → 515.38] of what the OSI is really about.
[515.48 → 516.48] What is the organization?
[516.58 → 517.64] It's a 501c3.
[518.38 → 520.62] You know, it's a public benefit corporation in California.
[520.62 → 525.52] But what exactly is the open source initiative for all that value we just talked about?
[525.64 → 526.10] What is it?
[526.36 → 526.62] Oh, yeah.
[526.90 → 530.90] In a nutshell, we are the maintainers of the open source definition.
[531.50 → 537.38] And that's the open source definition is a 10 points checklist that has been used for
[537.38 → 538.60] 26 years.
[538.76 → 541.42] We have celebrated 25 years last year.
[541.42 → 545.44] It's the checklist that has been used to evaluate licenses.
[546.08 → 551.86] That is legal documents that come together with software packages to make sure that the
[551.86 → 558.94] packages, the software comes with freedoms that are written down as can be summarized
[558.94 → 562.00] as four freedoms come from the free software definition.
[562.40 → 567.26] That is the freedom to use the software without having to ask for permissions.
[567.26 → 573.94] The freedom to study and to make sure that you know and to understand what it does and what
[573.94 → 576.60] it's supposed to be doing and nothing else.
[577.28 → 579.58] And for that, you need access to the source code.
[580.16 → 586.76] And then the freedom to modify it and to fix it and increase its capacity or help yourself.
[586.76 → 593.20] And the freedom to make copies that is for yourself or for to help others.
[593.82 → 599.78] And those freedoms were written down in the 80s by the Free Software Foundation.
[599.78 → 606.54] And the open source initiative started a couple of decades after that, picking up the principles
[606.54 → 612.38] and spreading them out a little bit in a more practical way.
[613.02 → 619.60] In a time, at a time when a lot of software was being deployed and powering the internet,
[619.80 → 620.26] basically.
[620.26 → 628.92] This definition and this is a license, licenses gives users and developers clarity about the
[628.92 → 633.86] things that they can do, provides that agency and independence and control.
[634.42 → 641.52] And all of that clarity is what has propelled and generated that huge ecosystem that is worth
[641.52 → 642.96] 8.8 trillions.
[642.96 → 650.22] So who formed the initiative and then how did it sustain and continue?
[650.84 → 655.26] Seems like the definition is pretty set, but like what is the work that goes on continually?
[655.94 → 663.22] Yeah, well, the work that goes on continuously is, especially now recently, it's the policy.
[663.70 → 668.12] The monitoring of policy works and everything that goes around it.
[668.12 → 675.54] The concept of open source seems to be set, but it's constantly under threat because evolution
[675.54 → 681.40] of technology, changes of business models, the rise and the rise of importance and power
[681.40 → 690.32] of new actors constantly shifts and tends to push the definition itself of open source in
[690.32 → 693.56] different directions, the meaning of open source in different directions.
[693.56 → 700.06] And regulation also tends to introduce hurdles that we need to be aware of.
[700.48 → 703.56] The organization, what we do, we have three programs.
[703.92 → 707.84] One is called the legal and licenses program.
[708.36 → 710.68] And that's where we maintain the definition.
[711.04 → 713.14] We review new licenses as they get approved.
[713.66 → 721.34] And we also keep a database of licensing information for packages because often developers don't use
[721.34 → 724.38] the right words or miss some pieces.
[724.60 → 726.64] A lot of packages don't have the right data.
[727.58 → 733.88] And we have, we are maintaining the community that maintains this machine called clearly defined.
[734.40 → 740.02] On the policy front, that's another program, the policy and standards front, we monitor the
[740.02 → 745.70] activity of standard setting organizations and the activity of regulators in the United States
[745.70 → 752.86] Europe mostly to make sure that all the new laws and rules and the standards can be implemented
[752.86 → 753.96] with open source code.
[753.96 → 759.44] And the regulation doesn't stop or doesn't block the development and distribution of open source
[759.44 → 760.26] software.
[760.86 → 765.56] And then a third program is on advocacy and outreach.
[765.56 → 771.76] And that's the activities that we do with maintaining the blog, having the communication, running events.
[772.42 → 780.36] And in this program, we're also hosting the conversations around the funding open source AI, which is a requirement
[780.36 → 788.76] that came out, especially a couple of years ago, very rapidly glowing of hotness at us.
[788.76 → 796.82] So we, you know, we were basically forced to start this process because open AI is a brand-new system.
[797.02 → 808.54] The brand-new activities, it forces us to review the principles to see if they still apply and how to, when they need to be modified in order we can apply to AI systems as a whole.
[809.10 → 810.82] And we are a charity organization.
[810.98 → 811.68] You mentioned that.
[811.68 → 822.04] So our sponsors are individuals who donate to become members, and they can donate any amounts from $50 a year up to what have you.
[822.04 → 825.64] And we have a few hundreds of those, almost a thousand.
[826.16 → 833.32] And then we have corporate sponsors who give us money, also donations to keep this work going.
[833.56 → 838.44] It's in their interest to have an independent organization that maintains the definition.
[838.44 → 845.70] And having multiple of these donors, corporate donors, makes the organization stronger.
[845.86 → 850.20] So we don't depend on anyone individually of them.
[850.76 → 858.76] So despite the fact that we get money from Google or Amazon or Microsoft and GitHub, we don't have to swear our allegiances to them.
[859.48 → 865.88] Do you also defend the license so far as going to court with people who would misuse it or no?
[865.88 → 879.88] It hasn't happened, but we do have, I mean, not under my watch, but we do have experts on our board and in our circle of licensing experts.
[879.88 → 888.12] We do have lawyers who go to court constantly to defend the license, defend trademark, protect users.
[888.66 → 890.16] And they're there as like expert witnesses.
[890.16 → 903.54] Exactly. And we do provide, we have provided briefs for courts, opinion pieces for regulators and responses to requests for information in various legislation.
[903.54 → 921.38] How challenging is it to be a U.S.-based, founded, idea, now organization that represents and defends this definition that really, you know, going back to the trillions, like, I mean, all the money, all the dollars.
[921.96 → 925.58] Like, it's a world problem. It's not just a United States problem.
[925.58 → 928.98] How does this organization operate internationally?
[929.20 → 939.46] What challenges do you face as a U.S.-based nonprofit, but representative of the idea of open source that really impacts everyone globally?
[940.00 → 942.40] Yeah, that's a very good question. In fact, it is challenging.
[942.86 → 948.78] So I started at the organization only a little over two years ago, and I'm Italian.
[948.78 → 953.20] And so I do have connections to Europe and knowledge about Europe.
[953.54 → 958.06] We do have board members that are based in Europe and other board members in the United States.
[958.48 → 968.68] And it is actually quite challenging to be involved into this global conversations because now, a little bit like maybe in the late 90s,
[969.20 → 975.28] open source is becoming increasingly getting at the centre of geopolitical challenges.
[975.28 → 982.06] And not because of open source per se, but because software is so incredibly existing everywhere.
[982.06 → 985.24] And most of that software that exists is open source.
[985.76 → 994.16] So there have been a lot of challenges to, as the relationship, the trade relationship with other actors like Russia, Ukraine,
[994.16 → 1003.30] now with the war in Israel and Gaza, and the trade wars with China, between China and the United States.
[1003.78 → 1007.36] There are a lot of geopolitical issues that we are at the centre of.
[1007.90 → 1010.64] And we're finding it really complicated.
[1011.10 → 1019.28] In fact, we do have, we have raised more money to increase our visibility on the policy front.
[1019.28 → 1027.14] We have right now, at the moment, we have two people working, one in Europe and one is more focused on the United States.
[1027.64 → 1028.84] Both of them are part-time.
[1029.18 → 1040.10] But we do have budget to hire at least another one, if not two policy analysts to help us review the incredible amount of legislation that is coming.
[1040.50 → 1042.44] We're just talking about the United States and Europe.
[1042.44 → 1051.78] I guess even one more layer than that is that, I don't know if it's a self-profession of the defender ship of the term of open source.
[1051.90 → 1054.24] I understand where it came from to some degree, you know.
[1054.50 → 1064.20] And I wonder if, how do you all handle the responsibility of not so much owning the trademark term of open source, but defending it.
[1064.24 → 1068.92] So in a way, you kind of own it by defending it because you have to defend it.
[1068.92 → 1072.92] Like it's some version of responsibility, which is maybe a byproduct of ownership, right?
[1073.62 → 1075.64] There's a pushback happening out there.
[1075.84 → 1084.56] Like there's even a conversation of recent where, you know, they can't describe their software as open source because the term means something.
[1084.72 → 1085.82] And we all agree on that, right?
[1085.84 → 1086.78] We understand that.
[1087.28 → 1093.56] And I'm not trying to defend that, but like how do you operate as an organization that defends this term?
[1093.56 → 1100.36] Yeah, I mean, this is hilarious because we don't have a trademark on the term open source of my software.
[1100.70 → 1112.46] We have a soft power, if you want, that is given to us by all the people who, just like you just said, recognize that the term open source is what we have designed.
[1112.66 → 1113.52] We have defined.
[1113.92 → 1115.46] We maintain the definition.
[1115.46 → 1118.08] And it's kind of recursive if you want.
[1118.58 → 1134.88] But corporations, individual developers, if all their institutions like academia, researchers, they recognize that open source means exactly those 10, the list of licenses, those 10 points, which you want the four freedoms that are listed.
[1134.88 → 1136.66] And we maintain that.
[1137.50 → 1150.16] And this has become quite visible also, even in courts, where they do understand that if someone is like there was a recent case involving the company Neo4j.
[1150.16 → 1156.16] And during that litigation, that is quite complicated with entrenched.
[1157.04 → 1157.76] I'm not a lawyer.
[1157.96 → 1161.50] I'm not going to dive into legal things.
[1161.64 → 1172.88] But the one key takeaway that is easy for me to drop and communicate is that the judge recognized that the value of open source is in the definition that we maintain.
[1172.88 → 1183.08] And calling open source something that is not a license that we have been approved is false advertising.
[1183.66 → 1184.50] And that held up in court.
[1185.40 → 1185.70] Oh, yeah.
[1186.30 → 1196.78] And so is that what you would say to people who are perhaps, maybe nonchalant isn't the best word, but unimpressed by open source as a definition?
[1196.78 → 1200.36] And they think it's stodgy and tight.
[1200.56 → 1202.60] And the thing that they're doing is close enough.
[1202.86 → 1204.36] And they like the term.
[1204.50 → 1205.54] They're going to use the term.
[1205.96 → 1210.86] And they've got OpenSSH code or source available or business source.
[1211.32 → 1217.60] Because there's a lot of people that are kind of pushing not just against the definition itself, but like against the idea that we need a definition.
[1217.82 → 1219.34] Or like you guys get to have the definition.
[1219.84 → 1220.70] What do you say to them?
[1221.00 → 1221.18] Yeah.
[1221.62 → 1223.10] You know, they're self-serving.
[1223.10 → 1227.96] They try to be self-serving, and they're trying to destroy the comments that way.
[1228.38 → 1229.40] Quite visibly.
[1229.62 → 1232.10] I think that users see through them.
[1232.72 → 1234.56] And it's not even in their interest.
[1234.82 → 1236.28] But you know how it works.
[1236.38 → 1242.28] Sometimes corporations, their greed goes up to they care only about the next quarter.
[1243.00 → 1245.42] And who cares about what happens next?
[1245.60 → 1247.68] You know, maybe the next CEO will have to take care.
[1247.76 → 1250.48] Meanwhile, they're just going to laugh all the way to the bank.
[1250.48 → 1261.14] And that is the approach that I see many of these people who complain or who try to redefine open source because it doesn't serve their purpose.
[1261.28 → 1263.52] What we maintain, it doesn't fully serve their purpose.
[1263.96 → 1274.52] So instead of respecting the comments and the shared ideas, they act like bullies and find all sorts of excuses to redesign.
[1274.52 → 1276.40] And we've seen it happening.
[1276.70 → 1281.82] Like I've been in free software and open source most of my career since I was in my 20s.
[1282.24 → 1293.46] And I've seen what was happening with the early days with the proprietary Unix guys that were going around telling us that this Linux thing is never going to work.
[1293.66 → 1294.46] You're joking.
[1294.46 → 1324.44] You're giving away.
[1324.46 → 1328.26] They're around the fact that you could make money sharing your source code.
[1328.48 → 1333.90] But they were forced by the market to show at least a little bit of what was happening behind the scenes.
[1334.12 → 1335.06] They were losing deals.
[1335.06 → 1338.30] So we've seen it already.
[1338.70 → 1340.64] They're going to keep ongoing like this.
[1340.74 → 1351.58] But there is plenty of interest in maintaining plenty more forces on the other side to maintain, then to keep the bar straight, to keep going where we're going.
[1351.58 → 1360.30] Because that clarity is such a powerful instrument to be able to say, I'm open source.
[1360.46 → 1362.98] Therefore, I know what I can do.
[1363.06 → 1364.28] I know what I cannot do.
[1364.50 → 1367.20] And have that collaboration straightened up.
[1367.20 → 1378.56] The legal departments, the compliance departments, the public tenders, they all tend to have very clear and speedy review of processes.
[1378.94 → 1385.44] That instead, if everyone has a different understanding of what open source means, we go back to the brand, right?
[1385.44 → 1392.26] And I'm in Italy now, and I'm surprised to see a lot of Starbucks stores opening.
[1393.06 → 1394.96] And I'm absolutely baffled.
[1395.16 → 1396.22] Why is this happening?
[1396.36 → 1398.66] This country has plenty of bar every quarter.
[1398.82 → 1401.24] There's a café with a decent coffee.
[1401.80 → 1402.74] Why do you need a brand?
[1402.88 → 1405.96] Because people have been going around travelling the world.
[1406.12 → 1406.78] They see the brand.
[1406.88 → 1407.52] They recognize it.
[1407.58 → 1408.52] They know what they can do.
[1408.52 → 1411.32] And they know that they're going to get what they're going to get.
[1411.36 → 1412.58] And they go there.
[1412.96 → 1414.36] And it's the same with open source.
[1414.36 → 1439.66] What's up, friends?
[1439.78 → 1443.60] This episode is brought to you by our friends at Venezia.
[1443.60 → 1452.26] Venezia is helping teams take NAS to the next level via a global, multi-cloud, multi-geo, and extensible service fully managed by Venezia.
[1452.58 → 1461.18] They take care of all the infrastructure, management, monitoring, and maintenance for you so you can focus on building exceptional distributed applications.
[1461.96 → 1464.36] And I'm here with VP of Product and Engineering, Byron Ruth.
[1464.88 → 1471.16] So, Byron, in the NAS versus Kafka conversation, I hear a couple different things.
[1471.16 → 1474.00] One I hear out there, I hate Kafka with a passion.
[1474.24 → 1475.90] That's quoted, by the way, on Hacker News.
[1476.60 → 1478.20] I hear Kafka is dead.
[1478.30 → 1479.42] Long live Kafka.
[1479.86 → 1482.70] And then I hear Kafka is the default, but I hate it.
[1482.98 → 1485.46] So, what's the deal with NAS versus Kafka?
[1486.02 → 1486.20] Yeah.
[1486.30 → 1487.80] So, Kafka is an interesting one.
[1488.22 → 1492.06] I've personally followed Kafka for quite some time ever since the LinkedIn days.
[1492.06 → 1499.70] And I think what they've done in terms of transitioning the landscape to event streaming has been wonderful.
[1499.92 → 1504.62] I think they definitely were the sort of first market for persistent data streaming.
[1505.14 → 1509.08] However, over time, as people have adopted it, they were the first to market.
[1509.08 → 1516.46] They provided a solution, but you don't know what you don't know in terms of you need this solution, you need this capability.
[1516.72 → 1524.42] But inevitably, there's also all this operational pain and overhead that people have come to associate with Kafka deployments.
[1524.42 → 1539.04] Based on our experience and what users and customers have come to us with, they would say, we are spending a ton of money on spend on a team to maintain our Kafka clusters or managed services or something like that.
[1539.28 → 1550.06] The paradigm of how they model topics and how you partition topics and how you scale them is not really in line with what they fundamentally want to do.
[1550.06 → 1564.74] And that's where NATO can provide, as we refer to it, subject-based addressing, which has a much more granular way of addressing messages, sending messages, subscribing to messages and things like that, which is very different from what Kafka does.
[1564.74 → 1579.92] And the second that we introduced persistence with our Jetstream subsystem, as we refer to it a handful of years ago, we literally had a flood of people saying, can I replace my Kafka deployments with this NATO Jetstream alternative?
[1580.50 → 1587.82] And we've been getting constant inbounds, constant customers asking, hey, can you enlighten us with what NATO can do?
[1587.82 → 1602.94] And, oh, by the way, here's all these other dependencies like Regis and other things and some of our services-based things that we could potentially migrate and evolve over time by adopting NATO as a technology, as a core technology to people's systems and platforms.
[1603.56 → 1605.52] So this has been largely organic.
[1605.76 → 1611.92] We never, from day one, with our persistence layered Jetstream, the intention was never to say, we're going to go after Kafka.
[1611.92 → 1628.64] But because of how we layered the persistence on top of this really nice Pub Sub core NATO foundation, and then we promoted it, and we say, hey, now we have the same semantics, same paradigm with these new primitives that introduce persistence in terms of streams and consumers.
[1629.06 → 1641.72] The floodgate just opened and everyone was, frankly, coming to us and wanting to simplify their architecture, reduce costs, operational costs, get all of these other advantages that NATO has to offer that Kafka does not whatsoever.
[1641.92 → 1644.52] Or any of the other similar offerings out there.
[1644.84 → 1647.56] And you get all these other advantages that NATO has to offer.
[1648.16 → 1649.48] So there's someone out there listening to this right now.
[1649.58 → 1655.60] They're the Kafka cluster admin, the person in charge of this cluster going down or not.
[1656.06 → 1659.32] They manage the team, they feel the pain, all the things.
[1659.56 → 1660.24] Give a prescription.
[1660.66 → 1661.22] What should they do?
[1661.36 → 1668.42] What we always recommend is that you can go to the NATO website, download the server, look at the client and model a stream.
[1668.78 → 1670.28] There are some guides on doing that.
[1670.28 → 1680.68] We also have, Sandra provided basically a packet of resources to inform people because we get, again, so many inbound requests about how do you compare NATO and Kafka?
[1680.84 → 1686.38] And we're like, let's actually just put a thing together that can inform people how to compare and contrast them.
[1686.58 → 1692.46] So we have a link on the website that we can share, and you can basically go get those set of resources.
[1692.46 → 1703.98] This includes a very lengthy white paper from an outside consultant that did performance benchmarks and stuff like that and discuss basically the different tradeoffs that are made.
[1703.98 → 1713.48] And they also do a total cost of ownership assessment between people who are organizations running Kafka versus running NATO for comparable workloads.
[1713.48 → 1714.72] Well, there you go.
[1714.98 → 1715.72] You have a prescription.
[1716.26 → 1718.14] Check for a link in the show notes to those resources.
[1718.68 → 1720.52] Yesterday's tech is not cutting it.
[1720.82 → 1726.58] NATO powered by the global multi-cloud, multi-geo, an extensible service that is fully managed by Sandra.
[1727.00 → 1727.90] It's the way of the future.
[1728.32 → 1730.92] Learn more at Sanedia.com slash changelog.
[1731.04 → 1736.94] That's S-Y-N-A-D-I-A dot com slash changelog.
[1736.94 → 1757.42] So last year on this time, Meta released Llama, their large language model, and too much fanfare and applause.
[1757.84 → 1759.88] And they announced it as open source.
[1760.44 → 1762.86] We know a lot has transpired since then.
[1762.86 → 1769.36] But at the time, what was your response to that, even personally or as the executive director of the OSI?
[1769.48 → 1770.24] Like, what were you thinking?
[1770.38 → 1772.70] What were you doing in the wake of that announcement?
[1773.34 → 1777.68] Well, we were already looking at open source AI in general.
[1777.98 → 1788.18] We were trying to understand what this new world meant and what the impact was on the principles of open source as they apply to the new artifacts that are being created in AI.
[1788.18 → 1796.18] And we already had come to the conclusion that open source AI is a different animal than open source software.
[1796.80 → 1799.04] There are many, many differences.
[1799.04 → 1811.82] So we immediately, two years ago, over two years ago, that was one of the first things that it started was to really push the board and to push the community to think about AI as a new artifact.
[1811.82 → 1823.40] That required and deserved also a deep understanding and a deep analysis to see how we could transport the benefits of open source software into this world.
[1823.88 → 1827.52] The release of Llama 2 kind of cemented that idea.
[1827.90 → 1836.18] It is a completely new artifact because they have released, sure, they have released a lot of information, a lot of details.
[1836.18 → 1840.34] But, for example, that we don't know exactly what went into the training data.
[1841.18 → 1849.12] And, well, Llama 2 also came out with a license that really has a lot of restrictions on use.
[1849.54 → 1854.76] So it's having restrictions on use is one of the things that we don't like.
[1855.38 → 1857.18] I mean, the open source definition forbids.
[1857.40 → 1859.22] You cannot have any restrictions on use.
[1859.80 → 1865.72] And, you know, on a surface value, the license for Llama 2 seems innocent, right?
[1865.72 → 1876.56] One of the things says, well, you cannot use Llama 2 for commercial applications if you have more than a few million, I don't remember exactly how many, a few million active users, monthly active users.
[1877.30 → 1880.48] Okay, you know, maybe that's a fair limitation.
[1881.32 → 1886.78] And in my mind, I was like, so what does it mean that the government of India cannot use it?
[1887.38 → 1889.56] The government of Italy, maybe?
[1889.56 → 1892.56] You know if you want to embed this into...
[1892.56 → 1897.58] So that's already an exclusion and starts to have to think about it.
[1897.80 → 1899.44] You know, think about, yeah, I'm a startup.
[1899.62 → 1900.52] You know, I'm a small thing.
[1901.14 → 1908.20] But what happens when you get to the six million users when, you know, all of a sudden you have to lower up and change completely your processes?
[1908.70 → 1914.66] But then there are a couple of other restrictions inside that license that are even more innocent on the surface.
[1914.66 → 1918.64] But when you start diving deeper, like, you cannot do anything illegal with it.
[1919.14 → 1919.52] Okay.
[1919.86 → 1920.28] All right.
[1920.38 → 1938.58] So let me say, if I help someone decide whether they can or they should have an abortion, or, you know, if I want to, if you want to have this tool used in applications to help me, I don't know, get refugees out of war zones into another place.
[1938.58 → 1945.30] And maybe I'm considered a terrorist organization by the government that is using that.
[1945.56 → 1947.34] So are I doing something illegal?
[1947.86 → 1952.10] Depends on whose side, you know, who needs to be evaluating that.
[1952.54 → 1961.94] It's these licensing terms that the Open Source Initiative really doesn't think they're useful, they're valuable, and they should not be part of a license.
[1962.42 → 1965.22] They should not be part of a contract in general.
[1965.80 → 1967.86] And they need to be dealt at a separate level.
[1967.86 → 1969.84] So that's what I was looking at.
[1969.90 → 1972.20] I was like, oh, Lama 2, oh my God.
[1972.36 → 1978.16] It's not open source because clearly this licensing thing would never pass our approval.
[1978.66 → 1982.16] And at the same time, we don't even know exactly what open source means.
[1982.34 → 1983.74] Why are you believing this space?
[1983.84 → 1985.46] So I got, I was really upset.
[1985.94 → 1986.02] Yeah.
[1986.70 → 1988.60] So then do you spring into action?
[1988.76 → 1989.98] Like, what does the OSI do?
[1990.06 → 1991.68] Because you're the defenders of the definition.
[1991.80 → 1994.10] And here's a misuse, a huge public misuse.
[1994.10 → 1995.70] Do you send, do you write a blog post?
[1995.80 → 1999.44] Do you send a letter, you know, from a lawyer?
[1999.56 → 1999.92] What do you do?
[2000.14 → 2000.72] We call up Zuck.
[2000.72 → 2003.18] Luckily, we were already, I call up Zuck.
[2003.48 → 2008.78] Luckily, we were already into this two-year process of defining open source AI.
[2008.78 → 2020.80] So we have, actually, I was already in conversations with Meta to have them join the process and support the process to find the shared definition of open source AI.
[2020.80 → 2029.96] And, in fact, they're part of this conversation, dynamic, with not just corporations like Google, Microsoft, GitHub, Amazon, et cetera.
[2030.58 → 2049.00] But also, we've invited researchers in academia, creators of AI, experts of ethics and philosophy, organizations that deal with open, in general, open knowledge, open data, like Wikimedia, Creative Commons, Open Knowledge Foundation, Mozilla Foundation.
[2049.00 → 2064.12] And we're talking also with a bunch of expert in ethics, but also organizations like digital rights groups, like the ESF and other organizations around the world who have me, you know, helping into this debate.
[2064.26 → 2072.46] Like, we had to first go through an exercise to understand and come to a shared agreement that AI is a different thing than software.
[2072.46 → 2088.12] Then we went through an exercise to find the shared values that we want to have represented and why we want to have the same sort of advantages that we have for software also posted over to the AI system.
[2088.12 → 2093.92] And then we have identified the freedoms that we want to have exercised.
[2093.92 → 2110.40] And now we're at the point where we are trying to make the list of components of AI systems, which is not as simple as binary code, compiler, and source code.
[2110.88 → 2112.26] So it's not as simple as that.
[2112.48 → 2113.78] It's a lot more complicated.
[2113.78 → 2117.78] So we're building this list of components for specific systems.
[2118.56 → 2133.60] And the idea is by the end of the spring, early summer, to have the equivalent of what we have now as a checklist for legal documents for software and have the equivalent for AI systems and their components.
[2133.60 → 2139.14] So that we will know, basically, we have our least candidate for an open source AI definition.
[2139.46 → 2141.56] Yeah, you mentioned that.
[2141.72 → 2144.56] And there's, I think you posted this eight days ago.
[2144.64 → 2149.78] A new draft of the open source AI definition version 0.0.5 is available.
[2150.02 → 2155.02] I'm going to read from, I think, what you might be alluding to, which is this, like, exactly what is open source AI?
[2155.12 → 2160.24] And it says, linked up to the Hacked document, it says, what is open source AI?
[2160.24 → 2170.22] To be open source, an AI system needs to be available under legal terms that grant the freedoms to, one, use the system for any purpose and without having to ask for permission.
[2170.90 → 2173.82] Two, study how the system works and inspect its components.
[2174.58 → 2178.90] Three, modify the system for any purpose, including to change its output.
[2179.54 → 2184.60] And four, share the system for others to use with or without modifications for any purpose.
[2184.60 → 2191.26] So those seem to be the four hinges that this, what is open source AI is hinging upon, at least in its current draft.
[2191.34 → 2195.38] Is that pretty accurate considering it's recent eight days ago?
[2195.72 → 2195.88] Yeah.
[2196.16 → 2200.24] Those are the four principles that we want to have represented.
[2200.78 → 2208.12] Now, the very crucial question is what comes next is what is, if you are familiar with the four freedoms of four software,
[2208.12 → 2217.92] those set by the Frizzled Foundation in the late 80s, they have one, those freedoms have one little sentence attached to it,
[2217.98 → 2220.18] to the freedom to study and the freedom to modify.
[2220.72 → 2227.40] They both say access to the source code is a precondition for this, which really means to clarify,
[2227.90 → 2232.72] it's that little addition, it's meant to clarify that the fact that if you want to study a system,
[2232.72 → 2239.10] if you want to modify it, you need to have a way to make modifications to it that is not just,
[2239.44 → 2243.28] it's the preferred form to make modifications from the human perspective.
[2243.28 → 2250.88] It's not that you give me a binary, and then I have to decompile it or try to figure out from reverse engineering how it works.
[2251.36 → 2252.26] Give me the source code.
[2252.34 → 2253.94] I need the source code in order to study.
[2253.94 → 2268.88] For the AI systems, we haven't really found yet a shared understanding or a shared agreement on what it needs to have access to the preferred form to make modification to an AI system.
[2269.64 → 2273.32] That's the exercise that we're running now and we, yeah.
[2273.54 → 2274.38] Yeah, that's interesting.
[2274.60 → 2280.72] The preferred form of modification is fascinating because, like you said, you don't want to give a binary and expect reverse engineering
[2280.72 → 2283.08] because that's possible, right?
[2283.12 → 2284.62] And that's possible maybe to a small subset.
[2284.76 → 2287.02] It's not the preferred route to get to Rome.
[2287.10 → 2289.18] It's just like, that's not the route I want to go down, right?
[2289.38 → 2290.50] I want a different way.
[2290.68 → 2290.76] Yeah.
[2291.18 → 2292.66] And you want to have a simple way.
[2292.82 → 2301.08] So, you know, even some licenses even have more specific wording around defining what source code actually means.
[2301.08 → 2314.18] Like the GNU and GPL is one of those very clear description and prescriptions about what needs to be given to users in order to exercise those freedoms, their freedoms as a user.
[2314.74 → 2323.08] So for AI, yeah, for AI, it's complicated because there are a few new things for which we don't even have.
[2323.48 → 2325.22] There are no court cases yet.
[2325.60 → 2327.18] You know, I keep repeating the same story.
[2327.18 → 2333.10] When software came out for the first time, it started to come out at the labs, research labs.
[2333.60 → 2338.22] It started to become a commercial artifact that people could just sell.
[2338.72 → 2342.10] There was a conscious decision to apply copyright to it.
[2342.52 → 2349.08] It was not a given fact that it was going to be using copyright, like copyright law.
[2349.56 → 2352.44] So that decision was a lucky one, honestly.
[2353.38 → 2355.44] And it was a well-thought-out.
[2355.44 → 2361.92] I don't know which of the two, because copyright as a legal system is very similar across the world.
[2362.54 → 2370.88] And building the open source definition, the free software definition, the legal documents that go with software for open source software and free software.
[2371.34 → 2379.12] Those legal documents built on top of copyright means that they're very, very similarly applied pretty much everywhere around the world.
[2379.12 → 2387.16] The alternative at the time were conversations around treating software as an invention and therefore covered by patents.
[2387.72 → 2390.70] Patent law is a whole different mess around the world.
[2390.98 → 2392.22] They're all different applications.
[2392.56 → 2396.44] They have all different terms, much more complicated to deal with.
[2396.44 → 2404.10] So for AI, we're pretty much at the same stage where there are some new artifacts, like the model.
[2404.48 → 2417.28] After you train a model and that produces weights and parameters that go into the model, those models, honestly, it's not clear what kind of legal frameworks apply to those things.
[2417.28 → 2440.02] And we might be at the same time in history where we could have to imagine and think and maybe suggest and recommend what the best course of action will be, whether it makes sense to treat them as copyrightable entities, artifacts, or nothing at all, or inventions, or any, you know, some other rights or exclusive rights.
[2440.02 → 2470.00] And the same goes into the same thing.
[2470.02 → 2474.02] Those lawsuits hinge on what's happening.
[2474.30 → 2484.32] Why are these powerful corporations going around and calling the internet, aggregating all of this information and data that we have provided, uploaded?
[2485.02 → 2493.32] We society, some commercial actors, some non-commercial actors, we have created this wealth of data on the internet.
[2493.32 → 2501.12] And they're going around painting it and basically making it proprietary, building models that they have for themselves.
[2501.38 → 2508.96] And on top of that, you can already start seeing like, oh my God, they're going to be eventually making a lot of money out of the things that we have created.
[2508.96 → 2516.72] Or even more scarily, like sometimes I think about this myself, I've been uploading my pictures for many years without thinking too much.
[2517.28 → 2518.76] So there is another base out there.
[2519.22 → 2523.54] I'm sure that someone has built another base out there of my pictures as I was aging.
[2523.54 → 2534.80] And now these pictures are being, can be used, could be used by a needle government or needle actor to recognize me around the streets at any time.
[2535.30 → 2537.24] And I don't have it in a course.
[2537.42 → 2538.20] So is that fair?
[2538.42 → 2539.30] Is that not fair?
[2539.84 → 2541.26] Those are big questions.
[2541.26 → 2543.30] And there is no easy or simple answer.
[2544.14 → 2544.22] Yeah.
[2544.62 → 2555.10] So did you enumerate, and I missed it, or can we enumerate the components that you have decided so far are part of an AI system?
[2555.28 → 2558.42] The code, I heard, the training data, et cetera.
[2558.76 → 2559.04] Yeah.
[2559.40 → 2560.84] There are three main categories.
[2561.22 → 2561.92] So maybe four.
[2562.16 → 2565.42] Like one is the category of data.
[2565.82 → 2567.58] One is in the category of code.
[2567.58 → 2571.06] One is the other category is models.
[2571.84 → 2580.34] And there is a four category that goes into other things like documentation, for example, instructions of how to use or scientific papers.
[2581.00 → 2586.68] In the data parts, some of the components are the training data, the testing data.
[2587.26 → 2594.60] In the code parts go the tooling to like for the architecture, the inference code to run the model.
[2594.60 → 2606.46] Anything that is written by a human in general, you can also have in there the code to filter and set up the data sets and prepare them for the training.
[2607.18 → 2615.78] And then in the models, you have the model architecture, the model parameters, including weights, hyperparameters, and things like that.
[2616.14 → 2619.92] There might be intermediate steps during the training.
[2619.92 → 2625.84] And the last bit is documentation, how to sample, output.
[2626.50 → 2641.62] So there is an initial list of all of these components that have been, I worked, we worked with, or actually the Linux Foundation worked on creating this list for specifically for generative AI and large language models.
[2641.62 → 2671.60] And we're working with them.
[2671.60 → 2673.12] Do I need to use it?
[2673.18 → 2674.44] Do I need it to copy?
[2674.58 → 2676.10] Do I need it to study?
[2676.50 → 2679.04] Do I need this component to modify the system?
[2679.56 → 2681.00] And we're referring to the system.
[2681.36 → 2686.56] This is one of the important things is the open source definition refers to the program.
[2687.06 → 2691.94] And the program is never defined, but a program in pretty much we know what it is.
[2691.94 → 2697.66] AI is, and again, this is a very complicated question.
[2697.78 → 2704.50] It looks very simple on surface, but when you start diving a little bit deeper, it becomes complicated because what is an AI system?
[2705.00 → 2705.12] Right.
[2705.12 → 2712.62] So we started using the definition that has been, it's becoming quite popular in every regulation around the world.
[2712.76 → 2719.02] It's a work done by the Organization for Economic Cooperation and Development, the OECD.
[2719.02 → 2725.48] And they have defined an AI system in very broad terms.
[2725.48 → 2733.28] And this definition is being used in many regulations, like from the United States Executive Order on AI.
[2733.74 → 2735.92] NIST also uses it.
[2736.20 → 2743.52] In Europe, the AI Act uses it, although with a slight, very small, minor variation.
[2743.52 → 2747.36] It seems to be quite popular, but there are detractors.
[2748.38 → 2750.52] Indeed, it is quite generic, too.
[2750.66 → 2755.46] Sometimes when you read it carefully, it may even cover a spreadsheet.
[2755.82 → 2756.46] It's really bizarre.
[2757.58 → 2764.34] So let's say that hypothetically I'm like a medical company that has been working on a large language model,
[2764.60 → 2767.46] and I have proprietary data.
[2767.74 → 2772.78] So I have like readings and reports and stuff that we've accumulated over years.
[2772.78 → 2780.00] And I create an LLM based on that data that ultimately can answer questions about medicine or whatever.
[2780.60 → 2782.22] And I want to open source that.
[2782.66 → 2789.06] I need to be able to make it so it's usable, studiable, modifiable, and shareable.
[2789.42 → 2793.82] And it seems like the training data, even though that's the most proprietary part,
[2794.32 → 2797.94] and perhaps the most difficult part to actually make available, or sometimes impossible,
[2797.94 → 2804.52] is necessary not to use, but to study and modify, it seems like.
[2805.16 → 2812.40] So if I release the model, the code, all the parameters, everything we use to build a model,
[2812.50 → 2817.22] everything except for like the source original data under what you guys are currently working on,
[2817.26 → 2819.12] that would not be open source AI, would it?
[2819.12 → 2828.96] Honestly, that is a very good case, example for why I think we need to carefully reason around
[2828.96 → 2831.40] what exactly do I need to study?
[2831.70 → 2834.36] What kind of access, what sort of access do I need?
[2834.98 → 2836.72] Is that the original data set?
[2837.12 → 2841.80] Because if it is the original data set, then we will never go to have an open source AI.
[2841.96 → 2842.34] Right.
[2842.78 → 2843.86] That's where I'll get into.
[2843.98 → 2844.88] It's not going to happen.
[2845.12 → 2845.84] It's not going to happen.
[2845.84 → 2846.56] Yeah.
[2846.72 → 2851.42] So maybe, and this is my working hypothesis that I threw out there,
[2851.92 → 2856.78] maybe what we need is a very good description of what that data is.
[2857.38 → 2861.74] Maybe samples, maybe instructions on how to replicate it.
[2862.18 → 2865.84] Because, for example, there might be data that is copyrighted.
[2866.26 → 2871.92] You might have the right, under fair use or under different exclusions of copyright,
[2871.92 → 2874.64] you may have the rights to create a copy and create a derivative,
[2874.64 → 2878.42] like I run the training, but not to redistribute it.
[2878.72 → 2880.88] Because if you redistribute it, then you start infringing.
[2881.40 → 2884.64] So I think we need to be carefully thinking about that.
[2884.90 → 2891.66] And the reason why I became more and more convinced that we don't need the original data set
[2891.66 → 2901.12] is because I've seen wonderful mixing, wonderful remixing of models,
[2901.48 → 2906.08] even splitting of models and recombinations of models,
[2906.34 → 2910.96] creating whole new capabilities, new AI capabilities,
[2910.96 → 2914.44] without having to retrain a single thing.
[2914.44 → 2921.58] So I'm starting to believe, really, that the AI weights in machine learning,
[2921.92 → 2923.04] the weights in the architecture,
[2923.78 → 2925.90] has its own, it's not a binary code.
[2926.02 → 2930.34] It's not a binary system that, the binary code that you have to reverse engineer.
[2930.58 → 2934.64] If you have sufficiently detailed instructions on how it's been built
[2934.64 → 2938.38] and what went into it, you should be able,
[2938.48 → 2942.52] you might be able to create new systems, reassemble it,
[2942.66 → 2946.48] study how it works and executing it, modifying.
[2946.86 → 2949.92] So the preferred form to make modifications is not necessarily
[2949.92 → 2954.26] going through the pipeline or rebuilding the whole system from scratch,
[2954.26 → 2957.04] which for many reasons may be impossible.
[2957.04 → 2961.24] I do like the idea of a small subset of the data set,
[2961.58 → 2965.84] you know, that's anonymized or, you know, sanitized in some way, shape, or form.
[2965.90 → 2969.54] That's like, this is the acceptable sample amount
[2969.54 → 2972.78] required for the study portion or the modification portion.
[2973.32 → 2975.78] Yeah. You know, it could be the schema, for example.
[2976.10 → 2977.76] It could be the you know.
[2977.76 → 2980.14] Provide your own data in here if you can,
[2980.48 → 2983.98] which you can obviously find other ways to use artificial intelligence
[2983.98 → 2985.24] to generate more data.
[2985.40 → 2986.84] So that's a whole thing, right?
[2986.84 → 2990.96] But I feel like that's acceptable to me.
[2991.32 → 2991.52] Yeah.
[2991.80 → 2994.06] To provide some sort of sampling or, as you said, the schema.
[2994.22 → 2995.16] I think that makes sense to me.
[2995.48 → 2995.62] Yeah.
[2996.08 → 2998.98] Yeah, the research is going also in this direction
[2998.98 → 3002.58] with data cards and model cards,
[3003.16 → 3005.14] lots of metadata specifications.
[3005.48 → 3007.96] I do think that that might be a valuable option.
[3008.08 → 3009.36] I would love to have, I mean,
[3009.42 → 3011.52] we've seen the next few weeks and months
[3011.52 → 3013.52] how that conversation goes,
[3013.64 → 3015.72] but I do believe that that's one way
[3015.72 → 3019.10] that we can get out of this process
[3019.10 → 3022.18] with a definition that is not just a theoretical,
[3022.62 → 3025.72] something beautiful that you put up in a picture in a museum
[3025.72 → 3028.28] and nobody can do anything with it.
[3028.82 → 3030.00] It needs to be practical.
[3030.00 → 3031.32] I keep repeating,
[3031.32 → 3033.72] the open source definition had success
[3033.72 → 3037.18] because it enabled something practical.
[3037.62 → 3040.72] And it has success because other people have written it.
[3040.80 → 3043.14] Other people have decided to use it.
[3043.84 → 3046.58] If you keep on insisting from your pedestal
[3046.58 → 3049.90] that you shall do this and that,
[3050.56 → 3055.08] you may not be finding enough crowds to follow you.
[3055.08 → 3055.48] Right.
[3056.38 → 3056.66] Yeah.
[3056.72 → 3057.90] And then if no one's using it,
[3057.96 → 3058.82] what's the point, right?
[3058.90 → 3059.28] You kind of,
[3059.36 → 3059.96] what's the point?
[3060.08 → 3061.14] You've lost the thread.
[3061.14 → 3083.24] What's up, friends?
[3083.32 → 3084.72] I'm here with one of my new friends,
[3084.96 → 3086.44] Zane Hamilton from CIQ.
[3086.84 → 3087.16] So Zane,
[3087.20 → 3088.30] we're coming up on a hard deadline
[3088.30 → 3091.84] with the CentOS end of life later this year in July.
[3091.84 → 3093.62] And there are still folks out there
[3093.62 → 3095.46] considering what their next move should be.
[3095.46 → 3096.14] Then last year,
[3096.18 → 3099.42] we had a bunch of change around Red Hat Enterprise Linux
[3099.42 → 3099.88] that makes it,
[3100.06 → 3100.08] quote,
[3100.16 → 3103.14] less open source in the eyes of the community
[3103.14 → 3103.86] with many saying,
[3104.22 → 3105.00] Real's open source,
[3105.12 → 3106.54] but where is the source?
[3106.66 → 3109.30] And why can't I download and install it?
[3109.68 → 3109.84] Now,
[3109.98 → 3111.52] Rocky Linux is fully open source
[3111.52 → 3114.24] and CIQ is a founding support partner
[3114.24 → 3116.46] that offers paid support for migration,
[3116.94 → 3117.40] installation,
[3117.66 → 3118.02] configuration,
[3118.68 → 3119.08] training,
[3119.30 → 3119.70] et cetera.
[3120.10 → 3122.08] But what exactly does an enterprise
[3122.08 → 3124.28] or a Linux sysadmin get
[3124.28 → 3125.76] when they choose the free
[3125.76 → 3127.40] and open source Rocky Linux
[3127.40 → 3129.54] and then ultimately the support from CIQ
[3129.54 → 3130.68] if they need it?
[3130.78 → 3131.72] There's a lot going on
[3131.72 → 3133.04] in the enterprise Linux space today.
[3133.32 → 3135.52] There's a lot of end of life of CentOS.
[3135.68 → 3136.58] People are making decisions
[3136.58 → 3137.42] on where to go next.
[3137.52 → 3138.98] The standard of what enterprise Linux
[3138.98 → 3139.70] looks like tomorrow
[3139.70 → 3140.88] is kind of up in the air.
[3141.30 → 3142.28] What CIQ is doing
[3142.28 → 3144.36] is we're trying to help those people
[3144.36 → 3145.40] that are going through
[3145.40 → 3146.24] these different decisions
[3146.24 → 3147.22] that they're having to make
[3147.22 → 3148.36] and how they go about
[3148.36 → 3149.18] making those decisions.
[3149.34 → 3150.28] And that's where our expertise
[3150.28 → 3151.26] really comes into play.
[3151.50 → 3152.10] A lot of people
[3152.10 → 3152.66] who have been through
[3152.66 → 3154.54] very complex Linux migrations,
[3154.70 → 3156.24] be it from the old days
[3156.24 → 3157.64] of migrating from AIX
[3157.64 → 3159.36] or Polaris onto Linux
[3159.36 → 3160.96] and even going from version to version
[3160.96 → 3161.34] because,
[3161.78 → 3162.16] to be honest,
[3162.26 → 3163.50] enterprise Linux version to version
[3163.50 → 3164.74] has not always been an easy conversion.
[3164.88 → 3165.42] It hasn't been.
[3165.64 → 3166.72] And you will hear that from us.
[3166.78 → 3167.00] Typically,
[3167.06 → 3167.60] the best idea
[3167.60 → 3168.84] is to do an in-place upgrade.
[3169.14 → 3170.82] Not always a real easy thing to do,
[3171.16 → 3172.36] but what we've done
[3172.36 → 3173.86] is we have started looking at
[3173.86 → 3174.90] and securing a path
[3174.90 → 3176.26] of how can we actually go through that?
[3176.34 → 3177.34] How can we help a customer
[3177.34 → 3178.86] who's moving from CentOS 7
[3178.86 → 3179.98] because of the end of life
[3179.98 → 3181.28] in July of this year?
[3181.58 → 3182.86] What does that migration path look like
[3182.86 → 3183.64] and how can we help?
[3183.72 → 3184.92] And that's where we're looking in ways
[3184.92 → 3185.70] to help automate
[3185.70 → 3186.74] from an admin perspective.
[3187.14 → 3187.96] If you're working with us,
[3187.98 → 3188.74] we've been through this,
[3188.78 → 3189.60] we can actually go through
[3189.60 → 3191.08] and build out that new machine
[3191.08 → 3192.24] and do a lot of the
[3192.24 → 3194.58] backend manual work for you
[3194.58 → 3195.84] so that all you really have to do
[3195.84 → 3196.42] at the end of the day
[3196.42 → 3197.50] is validated your applications
[3197.50 → 3198.74] up and running in the new space
[3198.74 → 3199.88] and then we automate this
[3199.88 → 3200.54] to switch over.
[3200.92 → 3201.80] So we've worked through
[3201.80 → 3202.34] a lot of that.
[3202.46 → 3203.22] There's also the decisions
[3203.22 → 3204.18] you're making around
[3204.18 → 3205.64] I'm paying a very large bill
[3205.64 → 3206.82] for something I'm not necessarily
[3206.82 → 3208.60] getting the most value out of.
[3208.70 → 3209.74] I don't want to continue
[3209.74 → 3210.52] down that path.
[3210.82 → 3212.02] We can help you make that shift
[3212.02 → 3213.28] over to an open source
[3213.28 → 3213.94] operating system,
[3214.20 → 3214.68] Rocky Linux,
[3214.86 → 3216.62] and help drive what's next,
[3216.86 → 3218.00] help you be involved
[3218.00 → 3218.90] in a community
[3218.90 → 3220.42] and help make sure
[3220.42 → 3221.02] that that environment
[3221.02 → 3221.88] you have is stable.
[3221.88 → 3223.20] It's going to be validated
[3223.20 → 3224.54] by the actual vendors
[3224.54 → 3225.42] that you're using today.
[3225.78 → 3226.42] And that's really where
[3226.42 → 3227.94] we want to be as a partner
[3227.94 → 3229.94] from not just an end user perspective,
[3229.94 → 3231.14] but as an industry perspective.
[3231.14 → 3232.56] We are working with a lot
[3232.56 → 3233.40] of those top tier vendors
[3233.40 → 3234.92] out there of certifying Rocky,
[3235.28 → 3236.66] making sure that it gets pushed
[3236.66 → 3237.70] back to the RESF,
[3237.82 → 3238.98] making sure that we can validate
[3238.98 → 3239.98] that everything is there
[3239.98 → 3241.70] and secure that needs to be there
[3241.70 → 3242.96] and helping you on that journey
[3242.96 → 3243.44] of moving.
[3243.94 → 3244.62] And that's where we,
[3244.78 → 3245.16] CIQ,
[3245.26 → 3246.38] really show our value
[3246.38 → 3247.60] on top of an open source
[3247.60 → 3248.20] operating system
[3248.20 → 3249.78] is we have the expertise.
[3250.04 → 3250.92] We've done this before.
[3251.08 → 3252.40] We're in the trenches with you
[3252.40 → 3253.70] and we're defining that path
[3253.70 → 3254.52] of how to move forward.
[3255.18 → 3256.80] Okay, ops and sysadmin folks
[3256.80 → 3257.38] out there,
[3257.52 → 3258.22] what are you choosing?
[3258.72 → 3261.04] CentOS is end of life soon.
[3261.14 → 3262.32] You may be using it,
[3262.56 → 3263.64] but if you want a support partner
[3263.64 → 3264.92] in the trenches with you,
[3265.12 → 3267.54] in the open source trenches with you,
[3267.84 → 3268.70] check out CIQ.
[3269.00 → 3270.48] They're the founding support partner
[3270.48 → 3271.74] of Rocky Linux.
[3271.94 → 3273.14] They've stood up the RESF,
[3273.80 → 3274.42] which is the home
[3274.42 → 3276.40] for open source enterprise software,
[3276.84 → 3279.08] the Rocky Enterprise Software Foundation.
[3279.08 → 3279.66] That is,
[3279.90 → 3281.10] they've helped to orchestrate
[3281.10 → 3282.38] the open ELA,
[3282.86 → 3284.22] a collaboration created by
[3284.22 → 3285.56] and upheld by CIQ,
[3285.88 → 3286.22] Oracle,
[3286.68 → 3287.14] and SUSE.
[3287.14 → 3288.72] Check out Rocky Linux
[3288.72 → 3290.64] at RockyLinux.org,
[3290.74 → 3291.90] the RESF
[3291.90 → 3294.28] at RESF.org.
[3294.56 → 3295.26] And of course,
[3295.36 → 3296.34] if you need support,
[3296.48 → 3297.18] check out our friends
[3297.18 → 3298.22] at CIQ
[3298.22 → 3300.48] at CIQ.com.
[3300.48 → 3313.20] Fully acknowledging
[3313.20 → 3314.32] that it's a work in progress
[3314.32 → 3315.64] and you're not done,
[3316.06 → 3317.86] given your current mental model
[3317.86 → 3319.08] of the definition
[3319.08 → 3320.26] as it is working,
[3320.42 → 3321.98] are there systems out there today
[3321.98 → 3323.04] that you would rubber stamp
[3323.04 → 3323.72] and say like,
[3323.80 → 3324.98] this is open source AI?
[3325.46 → 3326.68] I'm thinking of perhaps
[3326.68 → 3327.72] Mistral has a bunch
[3327.72 → 3328.44] of stuff going on
[3328.44 → 3329.08] and they're committed
[3329.08 → 3330.14] to open and transparent,
[3330.24 → 3330.92] but I don't know exactly
[3330.92 → 3331.74] what that means for them.
[3332.48 → 3333.58] Have you looked at anything
[3333.58 → 3334.66] and do you have like
[3334.66 → 3336.10] things you're comparing against
[3336.10 → 3336.76] as you build
[3336.76 → 3337.54] to make sure
[3337.54 → 3338.64] that there's a set of things
[3338.64 → 3339.40] that exist
[3339.40 → 3340.52] or could exist
[3340.52 → 3341.64] that are practical?
[3342.36 → 3342.90] Not yet.
[3343.14 → 3344.18] I know that there is,
[3344.30 → 3346.54] we have an affiliate organization
[3346.54 → 3348.32] called Leather AI.
[3349.00 → 3350.84] They are a group of researchers.
[3351.14 → 3353.10] They recently incorporated
[3353.10 → 3354.78] as a File 1C3
[3354.78 → 3356.40] non-profit in the United States.
[3356.40 → 3358.84] And from the very beginning,
[3359.02 → 3359.66] they've been doing
[3359.66 → 3360.42] a lot of research
[3360.42 → 3361.04] in the open,
[3361.24 → 3362.78] releasing data sets
[3362.78 → 3363.56] and structure
[3363.56 → 3365.60] and then research papers,
[3365.82 → 3366.54] models and weights
[3366.54 → 3368.26] and everything like that.
[3368.40 → 3369.76] So I'm looking,
[3369.84 → 3370.94] I'm really leaning a lot
[3370.94 → 3373.30] on them to shine a light
[3373.30 → 3374.78] on how this can be done,
[3374.94 → 3376.18] but I don't want to be
[3376.18 → 3378.18] too restricted in my mind.
[3378.38 → 3380.04] Like they are very open
[3380.04 → 3382.30] with an open science
[3382.30 → 3383.98] and open research mentality.
[3383.98 → 3386.24] I think that there is
[3386.24 → 3388.62] an open AI
[3388.62 → 3389.90] and open source AI
[3389.90 → 3392.70] that is not as equally open
[3392.70 → 3393.32] necessarily,
[3393.94 → 3395.20] but it can still practically
[3395.20 → 3396.84] have meaningful impact.
[3396.94 → 3397.90] It can generate
[3397.90 → 3399.74] that positive reinforcement
[3399.74 → 3401.16] of innovation,
[3401.50 → 3402.68] permissionless collaboration,
[3403.36 → 3403.78] et cetera.
[3404.48 → 3405.52] So yes,
[3405.70 → 3406.82] I need Leather AI,
[3407.08 → 3408.56] but I'm also daily open
[3408.56 → 3409.82] and I'm sure
[3409.82 → 3410.62] that there will be
[3410.62 → 3411.72] other organizations,
[3411.96 → 3412.50] other groups,
[3412.50 → 3414.30] as we go
[3414.30 → 3415.52] and elaborate more
[3415.52 → 3417.32] on what we actually need
[3417.32 → 3417.56] to,
[3417.98 → 3419.12] what is preferred form
[3419.12 → 3420.00] to make modifications
[3420.00 → 3421.10] to an AI system
[3421.10 → 3421.98] that we're going
[3421.98 → 3422.76] to discover more.
[3423.34 → 3426.44] So no open source AI yet.
[3426.52 → 3427.24] So there's no rubber stamp
[3427.24 → 3428.44] for anything out there currently.
[3428.76 → 3428.98] Well,
[3429.12 → 3429.46] I mean,
[3429.56 → 3430.66] I said,
[3430.82 → 3432.02] I could rubber stamp
[3432.02 → 3432.92] PTA
[3432.92 → 3434.60] and the Leather AI,
[3434.88 → 3436.00] but I don't want to say
[3436.00 → 3437.20] that that's necessarily
[3437.20 → 3438.24] the only thing.
[3438.32 → 3438.54] Right,
[3438.62 → 3439.34] there may be more stuff.
[3439.34 → 3439.74] And again,
[3439.88 → 3440.74] those are the ones,
[3441.04 → 3441.78] the guys that I,
[3441.78 → 3442.54] because I know
[3442.54 → 3443.28] how they work.
[3443.76 → 3445.38] Yesterday or the other day,
[3445.60 → 3446.60] ALMA was released
[3446.60 → 3448.12] by the Allen AI Institute.
[3448.92 → 3449.54] And that seems
[3449.54 → 3450.68] to be also quite
[3450.68 → 3452.08] openly available
[3452.08 → 3453.10] for models,
[3453.22 → 3453.48] weights,
[3453.76 → 3455.00] science behind it,
[3455.10 → 3455.40] et cetera.
[3455.84 → 3456.52] I haven't looked
[3456.52 → 3457.26] at their licenses
[3457.26 → 3458.26] and haven't looked
[3458.26 → 3459.38] at it carefully,
[3459.66 → 3461.10] so I can't really tell.
[3461.38 → 3462.28] It might as well
[3462.28 → 3463.94] be an open source
[3463.94 → 3464.64] AI system.
[3465.52 → 3466.18] I was trying
[3466.18 → 3466.86] to get to a definitive,
[3467.00 → 3467.16] really.
[3467.16 → 3468.28] Is there or is there
[3468.28 → 3469.90] not a stamped
[3469.90 → 3471.50] open source
[3471.50 → 3473.02] AI out there yet?
[3473.36 → 3473.72] You know,
[3473.82 → 3474.88] I can tell you
[3474.88 → 3475.48] what is not.
[3475.80 → 3475.92] I mean,
[3476.00 → 3476.92] Lama 2 is not.
[3477.52 → 3478.82] Open AI is not.
[3478.94 → 3479.20] Touché.
[3479.44 → 3479.92] All right.
[3480.26 → 3481.12] A deny list
[3481.12 → 3482.10] more than a permit list.
[3482.22 → 3482.40] Yeah,
[3482.54 → 3483.48] so I suppose
[3483.48 → 3484.16] one other question,
[3484.34 → 3485.60] which maybe is obvious,
[3486.16 → 3487.18] but I got to ask it,
[3487.92 → 3489.54] is what is the benefit
[3489.54 → 3491.88] if I'm building a model
[3491.88 → 3492.50] and I'm releasing
[3492.50 → 3493.04] a new AI?
[3493.20 → 3493.84] What is the benefit
[3493.84 → 3496.66] to it being open source?
[3497.14 → 3498.14] To meet this
[3498.14 → 3499.50] open source AI definition,
[3499.64 → 3500.38] like what is the benefit
[3500.38 → 3502.38] to its originator
[3502.38 → 3503.34] and then obviously
[3503.34 → 3504.08] to humanity,
[3504.14 → 3504.92] I kind of get that,
[3505.00 → 3505.44] but like,
[3506.00 → 3506.62] what is the benefit?
[3507.12 → 3507.72] It's pretty easy
[3507.72 → 3508.32] to kind of clarify
[3508.32 → 3509.72] that with software,
[3509.96 → 3510.10] right?
[3510.10 → 3511.46] We see how that's working
[3511.46 → 3511.98] because we've got,
[3512.30 → 3512.82] you know,
[3512.88 → 3513.80] 30 years of history
[3513.80 → 3515.64] or more in a lot of cases.
[3515.78 → 3516.24] Like we've got
[3516.24 → 3517.58] a track record there.
[3517.90 → 3518.38] We don't have
[3518.38 → 3519.04] a track record here.
[3519.10 → 3520.04] It's still early
[3520.04 → 3521.40] pioneer days.
[3522.06 → 3522.82] What's the benefit?
[3523.04 → 3525.00] That is a very good question
[3525.00 → 3527.52] and I don't have
[3527.52 → 3528.44] an answer for it.
[3528.58 → 3528.74] I mean,
[3528.82 → 3529.24] I do,
[3529.42 → 3530.56] I know the benefit
[3530.56 → 3531.26] for humanity.
[3531.52 → 3532.22] I know the benefit
[3532.22 → 3533.42] for the science of it
[3533.42 → 3535.86] and this is what really,
[3536.40 → 3537.12] those benefits
[3537.12 → 3537.92] are what trigger
[3537.92 → 3538.98] the internet.
[3539.34 → 3540.24] Like if software
[3540.24 → 3541.66] started to come out
[3541.66 → 3542.28] of the labs
[3542.28 → 3543.78] without the definition
[3543.78 → 3544.60] of true software,
[3544.72 → 3546.04] without the GPN license,
[3546.36 → 3548.60] without the BSD research,
[3549.26 → 3549.82] I don't think
[3549.82 → 3550.46] we would have had
[3550.46 → 3552.28] such a fast evolution
[3552.28 → 3554.26] of software,
[3554.58 → 3555.58] computer science,
[3555.66 → 3556.82] we would not have
[3556.82 → 3557.32] the internet
[3557.32 → 3558.92] that we see today
[3558.92 → 3560.46] if everyone had
[3560.46 → 3561.58] to buy a license
[3561.58 → 3562.74] from Polaris,
[3562.90 → 3563.20] Sun,
[3563.64 → 3564.32] from Oracle,
[3564.76 → 3565.52] et cetera,
[3565.62 → 3565.94] et cetera.
[3566.42 → 3567.32] If a data centre
[3567.32 → 3567.90] would have to,
[3568.26 → 3568.86] you know,
[3568.92 → 3569.76] you would have to go
[3569.76 → 3570.64] and call
[3570.64 → 3572.30] the Sun Microsystems
[3572.30 → 3574.16] or IBM's sales team
[3574.16 → 3575.20] to be before
[3575.20 → 3576.24] you could build
[3576.24 → 3577.46] a data centre
[3577.46 → 3578.22] instead of using
[3578.22 → 3578.96] just boxes
[3578.96 → 3580.50] and slapping Remix
[3580.50 → 3581.48] and Apache Web Server
[3581.48 → 3582.00] on it,
[3582.34 → 3583.10] we would have had
[3583.10 → 3584.64] a completely different
[3584.64 → 3587.30] history of digital world
[3587.30 → 3588.08] or the past,
[3588.28 → 3588.56] I mean,
[3588.64 → 3589.34] completely different.
[3589.60 → 3590.80] So I can see the benefit
[3590.80 → 3592.20] for society and science.
[3592.66 → 3593.80] For some of these corporations,
[3594.14 → 3594.80] I'm assuming
[3594.80 → 3595.76] that they have made
[3595.76 → 3596.04] their,
[3596.16 → 3597.24] some of their calculations
[3597.24 → 3599.14] on stopping
[3599.14 → 3600.02] the competition
[3600.02 → 3601.28] or creating
[3601.28 → 3602.64] competitive advantages.
[3603.30 → 3604.76] Maybe in pure
[3604.76 → 3605.92] Silicon Valley approach,
[3606.04 → 3607.64] like get more users,
[3607.80 → 3608.40] we'll figure out
[3608.40 → 3609.38] the business model later.
[3609.84 → 3611.08] There is some of that
[3611.08 → 3611.76] going on,
[3612.10 → 3612.68] likely,
[3612.86 → 3613.40] most likely,
[3613.90 → 3614.86] but I can't,
[3614.92 → 3615.60] I haven't had
[3615.60 → 3616.82] that conversation yet
[3616.82 → 3617.60] with any
[3617.60 → 3619.06] of the smart people
[3619.06 → 3619.56] I know
[3619.56 → 3620.50] thinking about
[3620.50 → 3621.36] the business models
[3621.36 → 3622.04] behind this
[3622.04 → 3623.20] or the possible ways
[3623.20 → 3624.80] of privatizing
[3624.80 → 3625.00] or,
[3625.18 → 3625.54] I don't know,
[3625.88 → 3627.24] finding revenue streams
[3627.24 → 3628.08] and things like that
[3628.08 → 3628.60] from these
[3628.60 → 3629.78] open source models.
[3630.32 → 3630.36] Yeah.
[3630.64 → 3631.40] Do you think
[3631.40 → 3632.08] that they're becoming
[3632.08 → 3632.86] commoditized
[3632.86 → 3633.70] if we specifically
[3633.70 → 3634.54] talk about
[3634.54 → 3635.76] this large language
[3635.76 → 3636.30] models,
[3636.78 → 3637.76] if we call AI
[3637.76 → 3638.58] that for now,
[3638.84 → 3639.60] recognizing
[3639.60 → 3640.52] there's an umbrella term
[3640.52 → 3641.38] and there are other things
[3641.38 → 3641.96] that also,
[3642.16 → 3643.06] that represents,
[3643.68 → 3644.16] do you think
[3644.16 → 3644.82] that they are
[3644.82 → 3646.46] becoming commoditized
[3646.46 → 3647.38] and will continue to
[3647.38 → 3648.16] enough so that
[3648.16 → 3648.70] open source
[3648.70 → 3649.66] can keep up
[3649.66 → 3650.50] with proprietary
[3650.50 → 3652.12] in terms of quality
[3652.12 → 3654.04] or even surpass
[3654.04 → 3655.66] just because of the
[3655.66 → 3656.54] number of people
[3656.54 → 3657.38] releasing things
[3657.38 → 3658.54] and are they,
[3658.60 → 3658.84] you know,
[3658.90 → 3659.40] I don't know.
[3659.56 → 3660.04] That's why I'm asking
[3660.04 → 3660.46] honestly.
[3660.82 → 3661.70] What are your thoughts
[3661.70 → 3661.98] on it?
[3661.98 → 3662.30] Honestly,
[3662.80 → 3663.82] recently I saw
[3663.82 → 3665.50] this new system
[3665.50 → 3667.16] that it's a text-to-speech
[3667.16 → 3667.62] system
[3667.62 → 3669.08] and they built it,
[3669.20 → 3670.76] this team of developers
[3670.76 → 3672.22] from a company
[3672.22 → 3673.12] called Collaborate.
[3673.32 → 3674.52] They built this system
[3674.52 → 3675.80] by splitting
[3675.80 → 3677.00] a system
[3677.00 → 3677.86] from open AI,
[3678.54 → 3679.58] another from
[3679.58 → 3681.16] either on Tropic
[3681.16 → 3682.06] or now,
[3682.12 → 3683.00] I don't remember exactly,
[3683.54 → 3684.54] but they split
[3684.54 → 3685.60] an AI system.
[3685.60 → 3686.56] they took it
[3686.56 → 3687.92] and they flipped it,
[3688.26 → 3689.60] their input for outputs
[3689.60 → 3690.58] and they attached
[3690.58 → 3691.86] another model
[3691.86 → 3693.34] of their own training
[3693.34 → 3694.50] with small datasets
[3694.50 → 3695.34] and they built
[3695.34 → 3696.20] a brand-new thing.
[3696.80 → 3697.20] I think,
[3697.28 → 3697.46] I mean,
[3697.50 → 3698.38] this is the kind of stuff
[3698.38 → 3699.20] that is inspiring.
[3699.52 → 3699.62] Like,
[3699.70 → 3700.64] at one point
[3700.64 → 3701.60] there's going to be,
[3702.08 → 3702.90] I'm sure
[3702.90 → 3704.16] that the quick evolution
[3704.16 → 3705.48] of this discipline
[3705.48 → 3706.78] would make it so
[3706.78 → 3708.40] that smaller teams
[3708.40 → 3709.58] with smaller amount
[3709.58 → 3710.02] of data
[3710.02 → 3710.64] would be able
[3710.64 → 3711.14] to create
[3711.14 → 3712.46] very powerful machines.
[3713.18 → 3714.26] And maybe
[3714.26 → 3715.62] the advantages
[3715.62 → 3717.18] of these large corporations
[3717.18 → 3717.88] that are now
[3717.88 → 3718.62] deploying,
[3719.18 → 3719.54] delivering,
[3719.90 → 3721.20] and distributing
[3721.20 → 3722.94] openly accessible
[3722.94 → 3724.74] AI models,
[3724.88 → 3726.74] maybe in their mind
[3726.74 → 3727.62] having optimized
[3727.62 → 3728.10] hardware,
[3728.34 → 3729.14] cloud resources
[3729.14 → 3730.28] that they can sell,
[3730.80 → 3731.38] maybe that's
[3731.38 → 3732.22] where they're going
[3732.22 → 3733.20] with one of their
[3733.20 → 3734.64] revenue streams
[3735.30 → 3736.12] they imagined
[3736.12 → 3736.66] that they would
[3736.66 → 3738.10] be coming from.
[3738.62 → 3738.86] Yeah,
[3738.86 → 3739.52] that is exciting.
[3739.52 → 3740.30] I did see,
[3740.38 → 3741.68] I think it was like
[3741.68 → 3742.88] Sodium AI
[3742.88 → 3744.00] just recently
[3744.00 → 3745.66] announced a model
[3745.66 → 3747.38] that beats
[3747.38 → 3748.44] DeepMind on
[3748.44 → 3749.24] code generation,
[3749.64 → 3749.86] you know,
[3750.12 → 3751.14] according to benchmarks
[3751.14 → 3752.06] that I haven't looked at,
[3752.34 → 3753.42] as well as Copilot,
[3753.96 → 3754.78] and that's from
[3754.78 → 3755.66] a smaller player.
[3756.12 → 3756.50] I'm not sure
[3756.50 → 3757.28] if that's open
[3757.28 → 3758.26] or closed or what,
[3758.32 → 3759.10] but it is kind of
[3759.10 → 3760.24] pointing towards like,
[3760.32 → 3760.70] okay,
[3761.60 → 3763.00] there's significant
[3763.00 → 3763.64] competition
[3763.64 → 3764.68] and like you said,
[3764.76 → 3765.40] remixing
[3765.40 → 3766.08] and the ability
[3766.08 → 3767.64] to combine
[3767.64 → 3768.76] and change
[3768.76 → 3770.46] and even in some
[3770.46 → 3771.64] cases swap out
[3771.64 → 3772.46] and take the best
[3772.46 → 3773.08] results,
[3773.34 → 3774.98] that we will have
[3774.98 → 3776.66] a vibrant ecosystem
[3776.66 → 3777.48] of these things
[3777.48 → 3778.44] and I think open
[3778.44 → 3779.78] source is the best
[3779.78 → 3781.38] model for vibrant
[3781.38 → 3781.86] ecosystems.
[3782.84 → 3783.04] So,
[3783.74 → 3784.50] that rings true
[3784.50 → 3784.96] with me.
[3785.52 → 3786.52] Doesn't mean it's right,
[3786.62 → 3787.50] but it sounds right.
[3788.06 → 3788.24] Yeah.
[3788.80 → 3789.80] This is a tough one.
[3790.32 → 3791.20] This is really a tough
[3791.20 → 3791.90] nut to crack,
[3791.98 → 3792.10] really.
[3792.20 → 3792.32] I mean,
[3792.40 → 3793.64] even at the
[3793.64 → 3795.78] forums you have,
[3795.90 → 3796.40] I believe
[3796.40 → 3797.64] you're calling it
[3797.64 → 3798.28] the deep dive,
[3798.38 → 3798.50] right?
[3798.60 → 3799.52] It's deep dive
[3799.52 → 3800.68] colon AI.
[3801.04 → 3801.60] And you,
[3802.02 → 3802.66] this is the place
[3802.66 → 3803.44] where you're hoping
[3803.44 → 3804.84] that many folks
[3804.84 → 3805.86] can come and organize.
[3806.00 → 3806.58] You say it's the
[3806.58 → 3808.62] global multi-stakeholder
[3808.62 → 3809.98] effort to define
[3809.98 → 3811.14] open source AI
[3811.14 → 3811.64] and that you're
[3811.64 → 3812.34] bringing together
[3812.34 → 3813.96] various organizations
[3813.96 → 3814.52] and individuals
[3814.52 → 3815.78] to collaboratively
[3815.78 → 3816.90] write a new document,
[3817.02 → 3817.64] which is what we've
[3817.64 → 3818.34] been talking about,
[3818.78 → 3818.98] you know,
[3819.02 → 3819.78] directly and indirectly.
[3820.40 → 3821.18] Who else has
[3821.18 → 3821.64] invited this?
[3821.70 → 3821.78] Like,
[3821.84 → 3823.06] how does this get
[3823.06 → 3823.72] around?
[3823.72 → 3824.34] How do people
[3824.34 → 3825.20] know about this?
[3825.30 → 3826.48] Who is invited
[3826.48 → 3827.12] to the table
[3827.12 → 3827.90] to define
[3827.90 → 3828.78] or help define?
[3829.40 → 3829.86] Is this,
[3830.04 → 3830.72] you know,
[3830.74 → 3831.40] an open way
[3831.40 → 3832.30] to define it?
[3832.70 → 3833.52] What is happening
[3833.52 → 3833.78] here?
[3833.84 → 3834.68] Who's participating?
[3835.46 → 3836.62] But at this point,
[3836.76 → 3837.70] it's now public,
[3837.92 → 3839.30] so anyone can really
[3839.30 → 3840.40] join the forum
[3840.40 → 3842.04] and can join me
[3842.04 → 3844.30] in the bi-weekly
[3844.30 → 3845.90] town hall meetings.
[3846.46 → 3847.38] So that part
[3847.38 → 3848.22] is public
[3848.22 → 3849.30] and everybody
[3849.30 → 3850.42] is welcome
[3850.42 → 3850.90] to join.
[3851.42 → 3851.90] We're going to
[3851.90 → 3852.86] keep on going
[3852.86 → 3853.96] with public
[3853.96 → 3854.58] reports
[3854.58 → 3856.26] and small
[3856.26 → 3857.02] working groups
[3857.02 → 3858.04] with people
[3858.04 → 3858.84] that we're picking,
[3859.08 → 3860.10] but only because
[3860.10 → 3860.80] of agility
[3860.80 → 3862.24] in the collaborations.
[3862.24 → 3863.24] We want to have,
[3863.80 → 3864.78] we're picking people
[3864.78 → 3866.32] that we know of
[3866.32 → 3867.32] or that we have
[3867.32 → 3868.70] been in touch with
[3868.70 → 3869.70] coming from
[3869.70 → 3870.22] a variety
[3870.22 → 3871.82] of experiences.
[3872.04 → 3872.20] Say,
[3872.30 → 3873.06] we're talking to
[3873.06 → 3873.98] creators of AI
[3873.98 → 3874.68] in academia,
[3875.30 → 3876.22] large corporations,
[3876.48 → 3877.38] small corporations,
[3877.70 → 3878.22] start-up,
[3878.78 → 3879.26] lawyers,
[3879.86 → 3880.60] people who work
[3880.60 → 3881.52] with regulators,
[3881.96 → 3882.58] think tanks,
[3882.58 → 3883.58] and lobbying
[3883.58 → 3884.44] organizations.
[3884.44 → 3885.88] We're talking to
[3885.88 → 3887.36] experts in other
[3887.36 → 3888.98] fields like ethics
[3888.98 → 3890.04] and philosophy.
[3890.58 → 3891.62] We keep on
[3891.62 → 3893.14] chatting with,
[3893.44 → 3894.68] we have identified
[3894.68 → 3896.56] six stakeholders,
[3896.92 → 3897.34] categories,
[3897.68 → 3898.58] and we're trying
[3898.58 → 3899.02] to have our
[3899.02 → 3899.68] presentations
[3899.68 → 3901.94] also geographically
[3901.94 → 3902.64] distributed
[3902.64 → 3903.24] from,
[3903.36 → 3903.82] you know,
[3903.94 → 3904.66] North America,
[3905.38 → 3906.16] South America,
[3906.94 → 3907.62] Asia Pacific,
[3908.10 → 3908.62] Europe,
[3908.62 → 3909.58] Africa.
[3910.16 → 3910.94] Last year,
[3911.36 → 3911.92] we had
[3911.92 → 3913.08] conversations
[3913.08 → 3913.74] with about
[3913.74 → 3914.44] 80 people
[3914.44 → 3915.56] from representatives
[3915.56 → 3916.36] of all these
[3916.36 → 3916.98] categories
[3916.98 → 3918.06] in a private
[3918.06 → 3918.88] group just to
[3918.88 → 3919.44] get things
[3919.44 → 3920.34] kick-started,
[3920.68 → 3921.42] and we have
[3921.42 → 3922.94] had meetings
[3922.94 → 3923.92] in person
[3923.92 → 3925.06] starting in
[3925.06 → 3926.06] June
[3926.06 → 3927.72] in San Francisco
[3927.72 → 3929.56] and in July
[3929.56 → 3930.48] in Portland
[3930.48 → 3932.22] and other
[3932.22 → 3933.24] meetings in
[3933.24 → 3933.66] Bilbao,
[3933.72 → 3934.04] in Europe.
[3934.26 → 3934.82] We had
[3934.82 → 3935.66] meetings in
[3935.66 → 3936.28] person with
[3936.28 → 3936.66] some of
[3936.66 → 3937.62] these people
[3937.62 → 3938.22] going at
[3938.22 → 3938.58] different
[3938.58 → 3939.14] conferences,
[3939.72 → 3940.26] but starting
[3940.26 → 3940.74] this year,
[3940.84 → 3941.08] we're going to
[3941.08 → 3941.34] be,
[3941.34 → 3942.38] this first half
[3942.38 → 3942.66] of the year,
[3942.72 → 3942.94] we're going to
[3942.94 → 3943.32] be super
[3943.32 → 3943.76] public.
[3944.28 → 3944.72] We're going to
[3944.72 → 3945.06] gather,
[3945.80 → 3946.24] we're going to
[3946.24 → 3946.84] be publishing
[3946.84 → 3947.56] all the results
[3947.56 → 3948.12] of the working
[3948.12 → 3948.60] groups,
[3949.44 → 3950.36] and we're going
[3950.36 → 3951.30] to be taking
[3951.30 → 3951.94] comments on
[3951.94 → 3952.40] the forums,
[3952.94 → 3953.46] and then we're
[3953.46 → 3953.98] going to have
[3953.98 → 3954.90] an in-person
[3954.90 → 3955.40] meeting.
[3955.40 → 3956.68] we're aiming
[3956.68 → 3957.56] late May,
[3957.66 → 3958.30] early June,
[3958.76 → 3959.68] with at least
[3959.68 → 3960.58] two representatives
[3960.58 → 3961.24] for each of
[3961.24 → 3961.92] the stakeholder
[3961.92 → 3963.52] categories to
[3963.52 → 3964.56] get in a room
[3964.56 → 3965.72] and produce,
[3965.90 → 3966.12] you know,
[3966.44 → 3967.28] iron out the
[3967.28 → 3969.22] last cases
[3969.22 → 3970.34] in definition,
[3970.68 → 3970.84] you know,
[3970.88 → 3971.46] removing on
[3971.46 → 3972.28] the comments
[3972.28 → 3973.32] and come out
[3973.32 → 3974.08] with other
[3974.08 → 3974.34] that,
[3974.40 → 3974.76] meaning with
[3974.76 → 3975.14] a race
[3975.14 → 3975.50] candidate,
[3975.70 → 3976.48] something that
[3976.48 → 3977.36] we feel like
[3977.36 → 3977.66] there is
[3977.66 → 3978.24] endorsement
[3978.24 → 3979.10] from a dozen
[3979.10 → 3980.04] different
[3980.04 → 3980.78] organizations
[3980.78 → 3981.44] across the
[3981.44 → 3981.90] world and
[3981.90 → 3982.36] across the
[3982.36 → 3982.78] experience.
[3983.36 → 3983.76] Then we're
[3983.76 → 3984.34] going to use,
[3984.70 → 3985.08] and we're
[3985.08 → 3985.68] raising funds
[3985.68 → 3986.10] for it,
[3986.46 → 3987.36] to have at
[3987.36 → 3987.98] least four
[3987.98 → 3989.12] events in
[3989.12 → 3989.70] different parts
[3989.70 → 3990.22] of the world
[3990.22 → 3991.34] between June
[3991.34 → 3992.36] and the end
[3992.36 → 3992.92] of October.
[3993.62 → 3994.38] One of these
[3994.38 → 3994.92] events will
[3994.92 → 3995.80] definitely be
[3995.80 → 3996.52] at All Things
[3996.52 → 3996.80] Open,
[3997.62 → 3997.98] where we're
[3997.98 → 3998.44] going to
[3998.44 → 3999.98] gather more
[3999.98 → 4000.64] potential
[4000.64 → 4001.36] endorsements,
[4001.86 → 4002.38] and as soon
[4002.38 → 4002.94] as we get
[4002.94 → 4003.62] to five
[4003.62 → 4004.44] endorsements
[4004.44 → 4006.14] from each
[4006.14 → 4006.40] of the
[4006.40 → 4006.66] different
[4006.66 → 4007.22] categories,
[4007.84 → 4008.38] I think
[4008.38 → 4008.64] we're going
[4008.64 → 4008.94] to be able
[4008.94 → 4009.28] to say
[4009.28 → 4009.68] this is
[4009.68 → 4010.38] version one.
[4010.78 → 4011.26] We can
[4011.26 → 4012.34] start working
[4012.34 → 4012.74] with it
[4012.74 → 4013.10] and see
[4013.10 → 4013.44] what we'll
[4013.44 → 4013.76] land,
[4014.26 → 4014.56] and maybe
[4014.56 → 4015.34] next year
[4015.34 → 4015.74] we're going
[4015.74 → 4016.18] to have,
[4016.26 → 4016.74] by that
[4016.74 → 4017.10] time,
[4017.16 → 4017.36] I mean,
[4017.42 → 4017.94] by October,
[4018.04 → 4018.32] November,
[4018.90 → 4019.38] the board
[4019.38 → 4019.86] will also
[4019.86 → 4020.72] have a
[4020.72 → 4021.60] process for
[4021.60 → 4022.20] the maintenance
[4022.20 → 4023.38] of this
[4023.38 → 4024.52] definition,
[4024.78 → 4025.60] because most
[4025.60 → 4026.76] likely we're
[4026.76 → 4027.10] going to have
[4027.10 → 4027.48] to think
[4027.48 → 4028.26] about how
[4028.26 → 4028.80] to maintain
[4028.80 → 4029.00] it,
[4029.06 → 4029.56] how to
[4029.56 → 4030.92] respond to
[4030.92 → 4031.72] challenges,
[4031.98 → 4032.48] whether they're
[4032.48 → 4033.06] technological
[4033.06 → 4035.22] or regulatory
[4035.22 → 4036.46] challenges,
[4037.02 → 4037.66] or just we
[4037.66 → 4038.22] missed a lot
[4038.22 → 4039.50] and we
[4039.50 → 4040.30] realize later
[4040.30 → 4040.84] we'll have
[4040.84 → 4041.46] to fix it.
[4042.04 → 4042.14] Yeah.
[4042.80 → 4043.30] Kind of
[4043.30 → 4043.66] want to
[4043.66 → 4044.32] backtrack
[4044.32 → 4045.16] slightly,
[4045.44 → 4045.88] I guess,
[4046.34 → 4046.90] as I hear
[4046.90 → 4047.22] you talk
[4047.22 → 4047.76] about this
[4047.76 → 4048.18] and kind
[4048.18 → 4048.48] of coming
[4048.48 → 4049.68] to a
[4049.68 → 4050.76] version of
[4050.76 → 4051.10] blessed
[4051.10 → 4051.44] sometime
[4051.44 → 4052.02] this year
[4052.02 → 4052.88] based upon
[4052.88 → 4053.68] certain details.
[4053.94 → 4053.98] Like,
[4054.06 → 4054.46] when I asked
[4054.46 → 4054.66] you,
[4054.96 → 4055.34] and I know
[4055.34 → 4055.82] this is your
[4055.82 → 4056.38] response and
[4056.38 → 4056.82] not so much
[4056.82 → 4057.16] a corporate
[4057.16 → 4057.74] response,
[4058.50 → 4059.12] in terms of
[4059.12 → 4059.48] what's the
[4059.48 → 4060.80] benefit of
[4060.80 → 4061.36] being an
[4061.36 → 4061.92] open source
[4061.92 → 4062.32] artificial
[4062.32 → 4062.86] intelligence,
[4063.14 → 4063.22] like,
[4063.30 → 4064.00] what's the
[4064.00 → 4064.34] benefit of
[4064.34 → 4064.66] being open
[4064.66 → 4065.74] source AI?
[4066.44 → 4066.66] Like,
[4066.72 → 4067.10] all this
[4067.10 → 4067.62] effort to
[4067.62 → 4068.38] define it,
[4069.10 → 4069.42] and then
[4069.42 → 4069.82] what if
[4069.82 → 4070.64] there's not
[4070.64 → 4071.00] that many
[4071.00 → 4071.38] people who
[4071.38 → 4071.72] really want
[4071.72 → 4071.88] to be
[4071.88 → 4072.42] defined by
[4072.42 → 4072.60] it?
[4072.74 → 4072.88] Like,
[4072.98 → 4073.38] I guess
[4073.38 → 4074.10] that's an
[4074.10 → 4074.44] interesting
[4074.44 → 4075.20] consideration
[4075.20 → 4075.70] is that
[4075.70 → 4076.16] all this
[4076.16 → 4076.72] effort to
[4076.72 → 4077.26] define it,
[4077.32 → 4078.40] but maybe
[4078.40 → 4079.18] there is
[4079.18 → 4079.52] no real
[4079.52 → 4079.96] benefit,
[4080.36 → 4080.70] or the
[4080.70 → 4081.20] benefit is
[4081.20 → 4081.62] unclear,
[4081.76 → 4082.04] and then
[4082.04 → 4082.76] folks just,
[4083.18 → 4083.64] it's almost
[4083.64 → 4084.22] like saying,
[4084.70 → 4085.22] it's definitely
[4085.22 → 4085.72] a line,
[4085.82 → 4085.92] right?
[4085.94 → 4086.14] It's like,
[4086.18 → 4086.38] okay,
[4086.46 → 4086.92] everything is
[4086.92 → 4087.64] basically not,
[4087.70 → 4088.02] and there's
[4088.02 → 4088.48] very few
[4088.48 → 4088.96] that are,
[4089.12 → 4089.50] basically.
[4089.94 → 4090.26] Or at least
[4090.26 → 4090.60] initially,
[4090.70 → 4091.30] maybe as
[4091.30 → 4092.24] iteration and
[4092.24 → 4092.80] progress happens
[4092.80 → 4093.40] that more and
[4093.40 → 4094.48] more will see
[4094.48 → 4094.88] the benefit,
[4095.00 → 4095.30] and maybe
[4095.30 → 4095.76] that benefit
[4095.76 → 4097.26] permeates more
[4097.26 → 4097.88] clearly than
[4097.88 → 4098.26] we can see
[4098.26 → 4098.70] it now.
[4099.46 → 4099.64] Yeah.
[4100.08 → 4100.68] I don't want
[4100.68 → 4101.14] to think about
[4101.14 → 4101.56] that.
[4101.56 → 4101.96] Okay.
[4103.50 → 4104.20] I don't want
[4104.20 → 4104.48] to think about
[4104.48 → 4104.72] that.
[4104.90 → 4105.12] Yeah,
[4105.32 → 4105.62] no,
[4105.90 → 4106.98] it's one of
[4106.98 → 4107.36] those things,
[4107.46 → 4107.62] like,
[4107.68 → 4108.92] if you start
[4108.92 → 4109.50] any endeavour
[4109.50 → 4110.22] thinking about
[4110.22 → 4110.62] the winner,
[4111.22 → 4111.62] you're probably
[4111.62 → 4112.14] going to fail,
[4112.28 → 4112.50] right?
[4112.56 → 4113.76] So it's not
[4113.76 → 4114.36] one of the
[4114.36 → 4115.30] outcomes that,
[4115.70 → 4116.44] I see
[4116.44 → 4117.38] tremendous amount
[4117.38 → 4117.94] of pressure,
[4118.70 → 4118.98] I mean,
[4119.08 → 4119.72] it's unlikely
[4119.72 → 4120.26] that that's
[4120.26 → 4120.68] going to happen,
[4120.78 → 4121.34] that's what I
[4121.34 → 4122.66] want to say.
[4122.66 → 4124.56] I have had
[4124.56 → 4125.50] a lot of
[4125.50 → 4126.90] pressure from
[4126.90 → 4127.98] corporations,
[4128.68 → 4129.20] regulators,
[4129.60 → 4130.36] like the AI
[4130.36 → 4131.60] Act has a
[4131.60 → 4132.20] provision in
[4132.20 → 4132.56] there,
[4133.10 → 4133.68] a text that
[4133.68 → 4134.38] says that
[4134.38 → 4135.18] provides some
[4135.18 → 4136.90] exclusions to
[4136.90 → 4138.26] the mandates
[4138.26 → 4138.92] of the law
[4138.92 → 4140.06] for open
[4140.06 → 4140.64] source AI.
[4141.16 → 4141.76] There is no
[4141.76 → 4142.48] definition in
[4142.48 → 4142.68] there.
[4142.86 → 4143.02] So,
[4143.26 → 4143.52] you know,
[4143.56 → 4144.50] regulators need
[4144.50 → 4144.78] it,
[4145.40 → 4146.24] the largest bulk
[4146.24 → 4147.26] corporations need
[4147.26 → 4147.48] it,
[4148.00 → 4149.50] researchers need
[4149.50 → 4150.22] some clarity.
[4150.22 → 4150.82] they would,
[4151.40 → 4153.00] I hear a lot
[4153.00 → 4153.60] of researchers,
[4154.24 → 4154.54] they want
[4154.54 → 4155.48] data,
[4156.10 → 4157.16] and they
[4157.16 → 4157.78] want data,
[4158.00 → 4158.50] it doesn't
[4158.50 → 4159.02] mean that they
[4159.02 → 4159.66] want necessarily
[4159.66 → 4160.32] the original
[4160.32 → 4161.24] data,
[4161.82 → 4162.56] some of them
[4162.56 → 4162.96] at least,
[4163.28 → 4163.78] but they do
[4163.78 → 4164.64] want to have
[4164.64 → 4165.78] good data set,
[4165.90 → 4166.60] and that only
[4166.60 → 4167.96] comes if there
[4167.96 → 4168.74] is a clarity
[4168.74 → 4169.68] about what
[4169.68 → 4170.28] are the
[4170.28 → 4171.60] boundaries of
[4171.60 → 4172.50] what is allowed
[4172.50 → 4173.40] for them to
[4173.40 → 4174.50] accumulate data,
[4174.60 → 4175.08] because data
[4175.08 → 4175.92] becomes very,
[4176.00 → 4176.62] very messy
[4176.62 → 4177.44] very quickly.
[4178.06 → 4178.94] Privacy law,
[4178.94 → 4180.34] copyright law,
[4180.68 → 4181.72] trade secrets,
[4182.28 → 4183.24] illegal content,
[4183.56 → 4183.76] you know,
[4183.86 → 4184.46] content is
[4184.46 → 4185.26] illegal in
[4185.26 → 4186.06] some parts of
[4186.06 → 4186.62] the country,
[4186.92 → 4188.00] or in some
[4188.00 → 4188.46] countries,
[4188.56 → 4188.82] and some
[4188.82 → 4189.40] other countries
[4189.40 → 4189.96] is not,
[4190.08 → 4190.30] you know,
[4190.36 → 4190.98] it becomes
[4190.98 → 4191.42] really,
[4191.42 → 4192.58] really messy
[4192.58 → 4193.74] very quickly,
[4193.94 → 4194.48] and researchers
[4194.48 → 4195.88] don't have a way
[4195.88 → 4196.34] to deal with
[4196.34 → 4197.20] it right now.
[4197.80 → 4198.44] They need help.
[4200.02 → 4200.90] I agree that
[4200.90 → 4201.34] you should keep
[4201.34 → 4201.84] doing it.
[4202.12 → 4202.60] I didn't mean
[4202.60 → 4203.04] to sound like
[4203.04 → 4203.38] it should be
[4203.38 → 4203.86] a failure.
[4204.42 → 4205.02] Sometimes I
[4205.02 → 4205.40] think it might
[4205.40 → 4205.90] be beneficial
[4205.90 → 4206.34] to think about
[4206.34 → 4206.82] failure at the
[4206.82 → 4207.02] beginning,
[4207.06 → 4207.40] because it's
[4207.40 → 4207.48] like,
[4207.52 → 4207.70] well,
[4208.32 → 4208.66] you got to
[4208.66 → 4209.06] consider your
[4209.06 → 4209.48] exit before
[4209.48 → 4209.88] you can go
[4209.88 → 4210.12] in,
[4210.20 → 4210.86] in a way.
[4210.94 → 4211.20] I'm not
[4211.20 → 4211.56] saying you
[4211.56 → 4211.84] should do
[4211.84 → 4212.02] that,
[4212.10 → 4212.82] but I'm
[4212.82 → 4213.16] glad you
[4213.16 → 4213.86] are defining it.
[4213.86 → 4214.24] It does
[4214.24 → 4214.74] need to be
[4214.74 → 4215.14] defined.
[4215.30 → 4215.62] I didn't
[4215.62 → 4216.22] mean to be
[4216.22 → 4216.76] necessarily
[4216.76 → 4217.10] like,
[4217.28 → 4217.70] what if,
[4217.84 → 4218.04] but,
[4218.46 → 4218.78] you know,
[4218.86 → 4219.26] there's a lot
[4219.26 → 4219.56] of effort
[4219.56 → 4219.96] going into
[4219.96 → 4220.12] this.
[4220.20 → 4220.60] I can see
[4220.60 → 4221.04] how,
[4221.28 → 4222.00] you know,
[4222.08 → 4222.96] a lot of
[4222.96 → 4224.20] your attention
[4224.20 → 4224.66] is probably
[4224.66 → 4226.08] spent simply
[4226.08 → 4227.06] on defining
[4227.06 → 4227.60] this and
[4227.60 → 4228.00] working with
[4228.00 → 4228.38] all the
[4228.38 → 4228.74] folks,
[4229.34 → 4229.64] all the
[4229.64 → 4230.06] stakeholders,
[4230.36 → 4230.60] all the
[4230.60 → 4231.18] opinion makers,
[4231.36 → 4231.62] et cetera,
[4232.32 → 4233.46] that are
[4233.46 → 4234.28] necessary to
[4234.28 → 4235.20] define what
[4235.20 → 4235.66] it is.
[4236.20 → 4236.46] It's a lot
[4236.46 → 4236.76] of work.
[4236.76 → 4237.42] It's all
[4237.42 → 4237.74] work,
[4237.80 → 4238.06] and you're
[4238.06 → 4238.36] absolutely
[4238.36 → 4238.72] right.
[4238.80 → 4239.10] This is
[4239.10 → 4240.06] taking most
[4240.06 → 4240.38] of my
[4240.38 → 4240.84] attention.
[4241.26 → 4241.68] And yes,
[4241.74 → 4242.72] I do see
[4242.72 → 4243.58] a couple
[4243.58 → 4244.22] of failure
[4244.22 → 4245.16] options.
[4245.46 → 4245.52] Like,
[4245.62 → 4246.10] we can
[4246.10 → 4247.06] fail if
[4247.06 → 4247.66] we're late
[4247.66 → 4248.78] and if
[4248.78 → 4249.06] we get
[4249.06 → 4249.56] it wrong.
[4249.90 → 4250.56] But for
[4250.56 → 4251.28] getting it
[4251.28 → 4251.64] wrong,
[4252.12 → 4252.60] the fact
[4252.60 → 4253.12] that it's
[4253.12 → 4253.92] defined with
[4253.92 → 4254.66] a version
[4254.66 → 4255.08] number,
[4255.68 → 4256.18] I think we
[4256.18 → 4256.64] can fix
[4256.64 → 4257.18] it over
[4257.18 → 4257.54] time,
[4257.70 → 4258.16] and we
[4258.16 → 4258.70] really
[4258.70 → 4259.66] shouldn't
[4259.66 → 4260.30] be expecting
[4260.30 → 4260.76] to have
[4260.76 → 4261.16] a perfect
[4261.16 → 4261.58] the first
[4261.58 → 4261.86] time.
[4261.86 → 4263.68] it's
[4263.68 → 4264.08] changing
[4264.08 → 4264.38] too
[4264.38 → 4264.74] quickly,
[4265.16 → 4265.86] the whole
[4265.86 → 4266.34] landscape.
[4267.14 → 4267.40] And the
[4267.40 → 4267.68] other,
[4268.18 → 4268.72] getting in
[4268.72 → 4269.04] late,
[4269.40 → 4270.22] is also
[4270.22 → 4270.76] part of
[4270.76 → 4271.06] the reason
[4271.06 → 4271.58] why I'm
[4271.58 → 4272.54] pushing to
[4272.54 → 4273.42] get something
[4273.42 → 4274.00] out of the
[4274.00 → 4274.24] door,
[4274.72 → 4275.98] because a
[4275.98 → 4276.46] lot of
[4276.46 → 4276.96] pressure
[4276.96 → 4278.28] exists in
[4278.28 → 4278.72] the market
[4278.72 → 4279.26] to have
[4279.26 → 4279.88] something.
[4280.44 → 4281.58] Everyone is
[4281.58 → 4282.40] calling them
[4282.40 → 4283.62] their models,
[4283.76 → 4284.34] open source
[4284.34 → 4284.76] AI,
[4285.40 → 4286.32] recognizing
[4286.32 → 4286.92] that there
[4286.92 → 4287.46] is value
[4287.46 → 4288.38] in that
[4288.38 → 4288.78] term,
[4288.90 → 4289.98] implicitly,
[4290.08 → 4290.44] but if
[4290.44 → 4290.80] there is
[4290.80 → 4291.38] no clarity,
[4291.60 → 4291.92] it's going
[4291.92 → 4292.12] to be
[4292.12 → 4292.50] diluted
[4292.50 → 4292.84] very,
[4292.90 → 4293.14] very,
[4293.14 → 4293.38] very
[4293.38 → 4293.84] rapidly.
[4294.48 → 4294.88] Before
[4294.88 → 4295.24] Jared and
[4295.24 → 4295.50] I got
[4295.50 → 4295.78] on this
[4295.78 → 4295.98] call,
[4296.06 → 4296.38] one thing
[4296.38 → 4296.86] we had
[4296.86 → 4297.58] a loose
[4297.58 → 4298.06] discussion,
[4298.18 → 4298.36] then I
[4298.36 → 4298.60] quickly
[4298.60 → 4299.06] stopped
[4299.06 → 4299.46] talking
[4299.46 → 4299.82] because
[4299.82 → 4300.02] we
[4300.02 → 4300.18] have
[4300.18 → 4300.30] a
[4300.30 → 4300.56] term.
[4301.34 → 4301.48] I
[4301.48 → 4301.62] think
[4301.62 → 4301.88] it's
[4301.88 → 4302.14] pretty
[4302.14 → 4302.30] well
[4302.30 → 4302.46] known
[4302.46 → 4302.58] in
[4302.58 → 4303.14] broadcasting
[4303.14 → 4303.34] and
[4303.34 → 4303.96] podcasting
[4303.96 → 4304.12] is
[4304.12 → 4304.32] like,
[4304.42 → 4304.58] don't
[4304.58 → 4304.84] waste
[4304.84 → 4305.26] tape,
[4305.46 → 4305.68] right?
[4306.40 → 4306.92] And I
[4306.92 → 4307.06] didn't
[4307.06 → 4307.32] want to
[4307.32 → 4307.68] share
[4307.68 → 4308.32] my
[4308.32 → 4308.56] deep
[4308.56 → 4308.80] sentiment,
[4308.92 → 4309.06] although
[4309.06 → 4309.20] I
[4309.20 → 4309.58] loosely
[4309.58 → 4309.94] mentioned
[4309.94 → 4310.18] it to
[4310.18 → 4310.36] Jared
[4310.36 → 4310.58] in our
[4310.58 → 4310.92] pre-call,
[4311.02 → 4311.16] just
[4311.16 → 4311.36] kind
[4311.36 → 4311.56] of
[4311.56 → 4312.30] 10
[4312.30 → 4312.48] minutes
[4312.48 → 4312.68] before
[4312.68 → 4312.82] we
[4312.82 → 4312.94] met
[4312.94 → 4313.16] up,
[4313.94 → 4314.14] was
[4314.14 → 4314.56] basically
[4314.56 → 4315.48] what
[4315.48 → 4315.62] is
[4315.62 → 4315.76] at
[4315.76 → 4316.14] stake?
[4316.86 → 4317.02] I
[4317.02 → 4317.14] know
[4317.14 → 4317.28] we
[4317.28 → 4317.56] talked
[4317.56 → 4318.48] just
[4318.48 → 4319.00] loosely
[4319.00 → 4319.24] here
[4319.24 → 4319.48] about
[4319.48 → 4319.84] failure
[4319.84 → 4320.06] as
[4320.06 → 4320.18] an
[4320.18 → 4320.50] option
[4320.50 → 4320.86] and
[4320.86 → 4321.46] what
[4321.46 → 4321.62] is
[4321.62 → 4321.90] failure
[4321.90 → 4322.06] and
[4322.06 → 4322.22] is
[4322.22 → 4322.72] iterative
[4322.72 → 4323.04] on
[4323.04 → 4323.16] the
[4323.16 → 4323.40] version
[4323.40 → 4323.64] numbers
[4323.64 → 4323.76] you
[4323.76 → 4323.94] just
[4323.94 → 4324.26] mentioned,
[4324.40 → 4324.50] but
[4324.50 → 4325.22] is
[4325.22 → 4325.40] there
[4325.40 → 4325.60] a
[4325.60 → 4325.88] bigger
[4325.88 → 4326.54] concern
[4326.54 → 4326.90] at
[4326.90 → 4327.22] stake
[4327.22 → 4327.68] if
[4327.68 → 4328.60] the
[4328.60 → 4329.04] definition
[4329.04 → 4329.28] that
[4329.28 → 4329.38] you
[4329.38 → 4329.60] come
[4329.60 → 4329.76] up
[4329.76 → 4330.10] with
[4330.10 → 4330.76] collectively
[4330.76 → 4331.82] is
[4331.82 → 4332.06] not
[4332.06 → 4332.42] perfectly
[4332.42 → 4332.70] suited?
[4332.88 → 4333.34] Does
[4333.34 → 4333.52] the
[4333.52 → 4333.84] term
[4333.84 → 4334.08] open
[4334.08 → 4334.62] source
[4334.62 → 4335.44] in
[4335.44 → 4335.82] software
[4335.82 → 4336.18] now,
[4340.58 → 4340.72] open
[4340.72 → 4341.20] source
[4341.20 → 4342.66] has
[4342.66 → 4342.92] not
[4342.92 → 4343.10] been
[4343.10 → 4343.32] able
[4343.32 → 4343.66] to
[4343.66 → 4344.30] carefully
[4344.30 → 4344.56] and
[4344.56 → 4345.06] accurately
[4345.06 → 4345.64] define
[4345.64 → 4346.46] open
[4346.46 → 4346.76] source
[4346.76 → 4347.04] AI?
[4347.26 → 4347.66] Is
[4347.66 → 4347.82] there
[4347.82 → 4347.98] a
[4347.98 → 4348.20] bigger
[4348.20 → 4348.92] loss
[4348.92 → 4349.46] that
[4349.46 → 4349.58] could
[4349.58 → 4350.00] happen?
[4350.66 → 4350.82] I'm
[4350.82 → 4350.96] sorry
[4350.96 → 4351.20] to have
[4351.20 → 4351.42] to ask
[4351.42 → 4351.52] that
[4351.52 → 4351.88] question,
[4351.98 → 4352.14] but I
[4352.14 → 4352.48] have to.
[4354.36 → 4354.90] You
[4354.90 → 4355.06] don't
[4355.06 → 4355.32] want me
[4355.32 → 4355.72] to sleep
[4355.72 → 4356.02] tonight.
[4356.82 → 4357.28] Sorry
[4357.28 → 4357.72] about that.
[4359.24 → 4359.58] I think
[4359.58 → 4361.26] so far
[4361.26 → 4361.44] we've
[4361.44 → 4361.80] been able
[4361.80 → 4362.30] to
[4362.30 → 4363.20] win
[4363.20 → 4363.54] in
[4363.54 → 4365.30] the
[4365.30 → 4365.64] public
[4365.64 → 4366.40] when we
[4366.40 → 4366.94] push
[4366.94 → 4367.34] back
[4367.34 → 4367.90] on the
[4367.90 → 4368.12] term
[4368.12 → 4368.26] of
[4368.26 → 4368.44] open
[4368.44 → 4368.62] source
[4368.62 → 4369.08] because
[4369.08 → 4370.16] it's
[4370.16 → 4370.38] pretty
[4370.38 → 4370.56] well
[4370.56 → 4370.94] accepted.
[4371.70 → 4371.80] Right?
[4372.02 → 4372.12] Yeah.
[4372.46 → 4372.78] And
[4372.78 → 4373.40] whether
[4373.40 → 4374.38] and I
[4374.38 → 4374.50] want
[4374.50 → 4374.94] to
[4374.94 → 4375.14] say
[4375.14 → 4375.32] this
[4375.32 → 4375.50] but
[4375.50 → 4375.86] whether
[4375.86 → 4375.98] we
[4375.98 → 4376.26] like
[4376.26 → 4376.36] it
[4376.36 → 4376.44] or
[4376.44 → 4376.78] not
[4376.78 → 4377.58] OSI
[4377.58 → 4377.96] has
[4377.96 → 4378.34] been
[4378.34 → 4379.26] the
[4379.26 → 4379.66] guardian
[4379.66 → 4380.14] so to
[4380.14 → 4380.32] speak
[4380.32 → 4380.42] of
[4380.42 → 4380.54] that
[4380.54 → 4380.82] term.
[4381.28 → 4381.58] Some
[4381.58 → 4381.84] say
[4381.84 → 4382.30] you've
[4382.30 → 4382.72] taken
[4382.72 → 4383.24] that
[4383.24 → 4383.56] right.
[4383.94 → 4384.40] I
[4384.40 → 4384.70] think
[4384.70 → 4384.92] you've
[4384.92 → 4385.06] been
[4385.06 → 4385.34] given
[4385.34 → 4385.54] that
[4385.54 → 4385.78] right
[4385.78 → 4386.22] over
[4386.22 → 4387.32] decades
[4387.32 → 4387.82] of
[4387.82 → 4388.32] trust
[4388.32 → 4389.06] and
[4389.06 → 4389.20] in
[4389.20 → 4389.44] some
[4389.44 → 4389.78] cases
[4389.78 → 4390.14] there's
[4390.14 → 4390.46] some
[4390.46 → 4390.96] mistrust
[4390.96 → 4391.10] and
[4391.10 → 4391.32] that's
[4391.32 → 4391.50] not
[4391.50 → 4391.68] so
[4391.68 → 4391.84] much
[4391.84 → 4392.10] me
[4392.10 → 4392.30] it's
[4392.30 → 4392.52] just
[4392.52 → 4392.90] out
[4392.90 → 4393.04] there
[4393.04 → 4393.82] not
[4393.82 → 4394.00] everybody
[4394.00 → 4394.10] has
[4394.10 → 4394.20] been
[4394.20 → 4394.50] happy
[4394.50 → 4394.68] with
[4394.68 → 4394.92] every
[4394.92 → 4395.20] decision
[4395.20 → 4395.32] you
[4395.32 → 4395.48] come
[4395.48 → 4395.58] up
[4395.58 → 4395.68] with
[4395.68 → 4395.76] and
[4395.76 → 4395.94] that's
[4395.94 → 4396.10] going
[4396.10 → 4396.16] to
[4396.16 → 4396.24] be
[4396.24 → 4396.40] the
[4396.40 → 4396.62] case
[4396.62 → 4396.88] right
[4396.88 → 4397.38] if
[4397.38 → 4397.52] you're
[4397.52 → 4397.58] not
[4397.58 → 4397.78] making
[4397.78 → 4397.96] some
[4397.96 → 4398.20] enemies
[4398.20 → 4398.72] you're
[4398.72 → 4399.08] not
[4399.08 → 4399.28] doing
[4399.28 → 4399.56] some
[4399.56 → 4400.36] things
[4400.36 → 4400.78] right
[4400.78 → 4400.94] I
[4400.94 → 4401.20] suppose
[4401.20 → 4401.30] in
[4401.30 → 4401.36] the
[4401.36 → 4401.44] world
[4401.44 → 4401.62] because
[4401.62 → 4402.32] nobody's
[4402.32 → 4402.42] going to
[4402.42 → 4402.54] like
[4402.54 → 4402.70] your
[4402.70 → 4402.98] choices
[4402.98 → 4403.34] right
[4403.34 → 4403.92] right
[4403.92 → 4404.56] but
[4404.56 → 4404.70] I
[4404.70 → 4405.00] think
[4405.00 → 4406.00] I
[4406.00 → 4406.26] wonder
[4406.26 → 4406.52] that
[4406.52 → 4406.72] I
[4406.72 → 4407.14] personally
[4407.14 → 4407.52] wonder
[4407.52 → 4407.88] if
[4407.88 → 4408.08] you
[4408.08 → 4408.34] can't
[4408.34 → 4408.64] define
[4408.64 → 4408.82] this
[4408.82 → 4409.14] well
[4409.14 → 4409.88] does
[4409.88 → 4410.06] the
[4410.06 → 4410.30] term
[4410.30 → 4410.56] open
[4410.56 → 4410.90] source
[4410.90 → 4411.74] change
[4411.74 → 4412.34] or
[4412.34 → 4412.68] is
[4412.68 → 4413.06] becoming
[4413.06 → 4413.44] open
[4413.44 → 4413.64] to
[4413.64 → 4414.16] change
[4414.16 → 4414.96] there
[4414.96 → 4415.12] is
[4415.12 → 4415.28] that
[4415.28 → 4415.74] come
[4415.74 → 4416.12] aware
[4416.12 → 4416.72] but
[4424.68 → 4425.02] chance
[4425.02 → 4425.24] to
[4425.24 → 4425.54] voice
[4425.54 → 4425.70] their
[4425.70 → 4426.04] opinion
[4426.04 → 4426.86] and
[4426.86 → 4427.18] all
[4427.18 → 4427.32] of
[4427.32 → 4427.50] these
[4427.50 → 4427.84] opinions
[4427.84 → 4428.04] are
[4428.04 → 4428.44] recorded
[4428.44 → 4428.96] publicly
[4428.96 → 4429.66] so
[4429.66 → 4429.84] we
[4429.84 → 4430.02] can
[4430.02 → 4430.20] go
[4430.20 → 4430.58] back
[4430.58 → 4431.08] and
[4431.08 → 4431.58] you
[4431.58 → 4431.72] know
[4431.72 → 4432.08] point
[4432.08 → 4432.42] at
[4432.42 → 4432.94] the
[4432.94 → 4433.30] place
[4433.30 → 4433.50] where
[4433.50 → 4433.68] we
[4433.68 → 4433.84] made
[4433.84 → 4433.96] a
[4433.96 → 4434.12] bad
[4434.12 → 4434.58] choice
[4434.58 → 4434.86] and
[4434.86 → 4435.80] you
[4435.80 → 4435.90] know
[4435.90 → 4436.04] be
[4436.04 → 4436.20] able
[4436.20 → 4436.34] to
[4436.34 → 4436.76] correct
[4436.76 → 4437.14] or
[4437.14 → 4437.44] or
[4437.44 → 4437.72] not
[4437.72 → 4438.46] yeah
[4438.46 → 4439.54] Stefano
[4439.54 → 4439.88] real
[4439.88 → 4440.12] quick
[4440.12 → 4440.38] what's
[4440.38 → 4440.52] the
[4440.52 → 4440.74] number
[4440.74 → 4440.96] one
[4440.96 → 4441.28] place
[4441.28 → 4441.56] people
[4441.56 → 4441.74] should
[4441.74 → 4442.16] go
[4442.16 → 4442.66] if
[4442.66 → 4442.76] they
[4442.76 → 4442.86] were
[4442.86 → 4442.96] to
[4442.96 → 4443.12] get
[4443.12 → 4443.64] involved
[4443.64 → 4444.06] like
[4444.06 → 4444.78] the
[4444.78 → 4445.28] URL
[4445.28 → 4446.10] here's
[4446.10 → 4446.18] how
[4446.18 → 4446.26] you
[4446.26 → 4446.36] can
[4446.36 → 4446.46] be
[4446.46 → 4446.64] part
[4446.64 → 4446.72] of
[4446.72 → 4446.92] that
[4446.92 → 4447.46] discussion
[4447.46 → 4448.34] discuss
[4448.34 → 4448.68] the
[4454.68 → 4455.12] if
[4455.12 → 4458.56] you
[4458.56 → 4458.84] want
[4458.84 → 4458.96] to
[4458.96 → 4459.36] listen
[4459.36 → 4459.94] and
[4459.94 → 4460.28] be
[4460.28 → 4461.12] lurking
[4461.12 → 4461.54] and
[4461.54 → 4461.90] watching
[4461.90 → 4462.16] as it
[4462.16 → 4462.28] makes
[4462.28 → 4462.68] progress
[4462.68 → 4463.00] definitely
[4463.00 → 4463.16] hit
[4463.16 → 4463.30] that
[4463.30 → 4463.44] up
[4463.44 → 4463.56] if
[4463.56 → 4463.64] you
[4463.64 → 4463.76] want
[4463.76 → 4463.88] your
[4463.88 → 4464.18] voice
[4464.18 → 4464.48] heard
[4464.48 → 4465.30] and
[4465.30 → 4465.36] you
[4465.36 → 4465.48] want
[4465.48 → 4465.56] to
[4465.56 → 4465.74] help
[4465.74 → 4466.14] Stefano
[4466.14 → 4466.42] and
[4466.42 → 4466.66] his
[4466.66 → 4467.10] team
[4467.10 → 4468.00] make
[4468.00 → 4468.14] this
[4468.14 → 4468.50] definition
[4468.50 → 4468.98] awesome
[4468.98 → 4469.46] and
[4469.46 → 4470.20] encompassing
[4470.20 → 4470.40] and
[4470.40 → 4471.12] successful
[4471.12 → 4472.18] I think
[4472.18 → 4472.60] the more
[4472.60 → 4472.96] voices
[4472.96 → 4473.46] the better
[4473.46 → 4473.98] the earlier
[4473.98 → 4474.22] on
[4474.22 → 4474.56] the better
[4474.56 → 4475.56] so that
[4475.56 → 4475.70] we
[4475.70 → 4476.06] can
[4476.06 → 4476.46] have
[4476.46 → 4476.74] a
[4476.74 → 4477.36] great
[4477.36 → 4477.66] open
[4477.66 → 4477.88] source
[4477.88 → 4478.04] AI
[4478.04 → 4478.48] definition
[4478.48 → 4479.28] thank
[4479.28 → 4479.44] you
[4479.44 → 4480.02] thanks
[4480.02 → 4480.36] Stefano
[4480.36 → 4480.72] appreciate
[4480.72 → 4481.14] your time
[4481.14 → 4481.48] thank
[4481.48 → 4481.64] you so
[4481.64 → 4481.90] much
[4481.90 → 4482.42] thank
[4482.42 → 4482.62] you
[4482.62 → 4486.70] it's
[4486.70 → 4486.90] a big
[4486.90 → 4487.20] question
[4487.20 → 4487.48] mark
[4487.48 → 4487.64] what
[4487.64 → 4487.80] the
[4487.80 → 4488.20] future
[4488.20 → 4488.68] of
[4488.68 → 4488.86] the
[4488.86 → 4489.18] open
[4489.18 → 4489.56] source
[4489.56 → 4489.92] AI
[4489.92 → 4490.56] definition
[4490.56 → 4491.08] will
[4491.08 → 4491.42] be
[4491.42 → 4491.84] well
[4491.84 → 4491.96] the
[4491.96 → 4492.18] first
[4492.18 → 4492.62] draft
[4492.62 → 4492.96] of
[4492.96 → 4493.14] the
[4493.14 → 4493.46] open
[4493.46 → 4493.84] source
[4493.84 → 4494.24] AI
[4494.24 → 4494.88] definition
[4494.88 → 4495.30] is
[4495.30 → 4495.74] linked
[4495.74 → 4496.16] in
[4496.16 → 4496.28] the
[4496.28 → 4496.48] show
[4496.48 → 4496.78] notes
[4496.78 → 4497.24] I
[4497.24 → 4497.52] highly
[4497.52 → 4497.86] encourage
[4497.86 → 4497.96] you
[4497.96 → 4498.08] to
[4498.08 → 4498.22] check
[4498.22 → 4498.42] this
[4498.42 → 4498.64] out
[4498.64 → 4498.96] dig
[4498.96 → 4499.34] in
[4499.34 → 4500.08] learn
[4500.08 → 4500.40] about
[4500.40 → 4500.64] what's
[4500.64 → 4500.98] happening
[4500.98 → 4501.44] here
[4501.44 → 4502.02] voice
[4502.02 → 4502.28] your
[4502.28 → 4502.60] opinion
[4502.60 → 4502.90] if
[4502.90 → 4503.00] you
[4503.00 → 4503.38] have
[4503.38 → 4503.64] a
[4503.64 → 4503.90] strong
[4503.90 → 4504.34] opinion
[4504.34 → 4504.92] but
[4504.92 → 4505.20] definitely
[4505.20 → 4505.42] pay
[4505.42 → 4505.78] attention
[4505.78 → 4506.50] as
[4506.50 → 4506.60] you
[4506.60 → 4506.70] can
[4506.70 → 4506.88] hear
[4506.88 → 4507.02] with
[4507.02 → 4507.16] some
[4507.16 → 4507.24] of
[4507.24 → 4507.34] the
[4507.34 → 4508.08] uncomfortability
[4508.08 → 4508.98] with
[4508.98 → 4509.42] the
[4509.42 → 4509.78] questions
[4509.78 → 4509.98] we
[4509.98 → 4510.30] asked
[4510.30 → 4510.66] about
[4510.66 → 4511.36] what
[4511.36 → 4511.88] happens
[4511.88 → 4512.36] if
[4512.36 → 4512.60] the
[4512.60 → 4512.90] open
[4512.90 → 4513.24] source
[4513.24 → 4513.58] AI
[4513.58 → 4514.22] definition
[4514.22 → 4515.36] falls
[4515.36 → 4515.82] a little
[4515.82 → 4516.28] short
[4516.28 → 4516.92] or what
[4516.92 → 4517.10] the
[4517.10 → 4517.70] ramifications
[4517.70 → 4518.10] are
[4518.10 → 4518.62] or potential
[4518.62 → 4519.10] impact
[4519.10 → 4519.34] might
[4519.34 → 4519.66] be
[4519.66 → 4520.06] I
[4520.06 → 4520.22] think
[4520.22 → 4520.34] we
[4520.34 → 4520.60] all
[4520.60 → 4520.76] need
[4520.76 → 4520.88] to
[4520.88 → 4521.02] pay
[4521.02 → 4521.34] close
[4521.34 → 4521.76] attention
[4521.76 → 4522.50] to
[4522.50 → 4522.74] how
[4522.74 → 4523.02] this
[4523.02 → 4523.64] definition
[4523.64 → 4524.56] evolves
[4524.56 → 4525.10] and
[4525.10 → 4525.58] lands
[4525.58 → 4526.36] links
[4526.36 → 4526.76] are
[4526.76 → 4526.92] in
[4526.92 → 4527.04] the
[4527.04 → 4527.20] show
[4527.20 → 4527.44] notes
[4527.44 → 4527.76] so
[4527.76 → 4527.92] check
[4527.92 → 4528.04] them
[4528.04 → 4528.26] out
[4528.26 → 4528.82] and
[4528.82 → 4529.10] again
[4529.10 → 4529.44] thank
[4529.44 → 4529.62] you
[4529.62 → 4529.86] to
[4529.86 → 4530.28] Stefano
[4530.28 → 4530.62] because
[4530.62 → 4531.26] he
[4531.26 → 4531.52] did
[4531.52 → 4532.02] have
[4532.02 → 4532.50] a
[4532.50 → 4532.88] cold
[4532.88 → 4533.30] during
[4533.30 → 4533.56] this
[4533.56 → 4534.16] conversation
[4534.16 → 4534.86] and
[4534.86 → 4535.00] he
[4535.00 → 4535.26] powered
[4535.26 → 4535.54] through
[4535.54 → 4535.96] because
[4535.96 → 4536.44] he
[4536.44 → 4536.64] knew
[4536.64 → 4536.82] this
[4536.82 → 4536.94] was
[4536.94 → 4537.06] an
[4537.06 → 4537.32] important
[4537.32 → 4537.80] conversation
[4537.80 → 4537.96] to
[4537.96 → 4538.36] have
[4538.36 → 4538.70] here
[4538.70 → 4538.82] on
[4538.82 → 4538.96] this
[4538.96 → 4539.34] podcast
[4539.34 → 4539.82] and
[4539.82 → 4539.96] to
[4539.96 → 4540.08] share
[4540.08 → 4540.22] with
[4540.22 → 4540.48] you
[4540.48 → 4541.02] so
[4541.02 → 4541.24] thank
[4541.24 → 4541.34] you
[4541.34 → 4541.72] Stefano
[4541.72 → 4542.38] up
[4542.38 → 4542.72] next
[4542.72 → 4542.96] on
[4542.96 → 4543.08] the
[4543.08 → 4543.42] pod
[4543.42 → 4543.84] is
[4543.84 → 4544.10] our
[4544.10 → 4544.54] friendly
[4544.54 → 4544.88] turned
[4544.88 → 4545.40] friend
[4545.40 → 4545.84] Jamie
[4545.84 → 4546.24] Tanna
[4546.24 → 4547.02] coming up
[4547.02 → 4547.16] on
[4547.16 → 4547.66] friends
[4547.66 → 4548.36] and
[4548.36 → 4548.60] next
[4548.60 → 4548.82] week
[4548.82 → 4549.08] it's
[4549.08 → 4549.28] about
[4549.28 → 4549.68] making
[4549.68 → 4549.88] your
[4549.88 → 4550.08] shell
[4550.08 → 4550.56] magical
[4550.56 → 4551.16] with
[4551.16 → 4551.56] Ellie
[4551.56 → 4552.08] Huntable
[4552.08 → 4552.66] talking
[4552.66 → 4552.92] about
[4552.92 → 4553.08] a
[4553.08 → 4553.26] two
[4553.26 → 4553.44] in
[4553.44 → 4554.04] check
[4554.04 → 4554.16] it
[4554.16 → 4554.34] out
[4554.34 → 4554.54] at
[4554.54 → 4554.56] a
[4554.56 → 4554.84] two
[4554.84 → 4555.04] in
[4555.04 → 4555.38] dot
[4555.38 → 4555.88] sh
[4555.88 → 4557.10] okay
[4557.10 → 4557.60] once
[4557.60 → 4557.82] again
[4557.82 → 4557.98] a
[4557.98 → 4558.14] big
[4558.14 → 4558.40] thank
[4558.40 → 4558.50] you
[4558.50 → 4558.66] to
[4558.66 → 4558.82] our
[4558.82 → 4559.42] friends
[4559.42 → 4559.66] and
[4559.66 → 4559.76] our
[4559.76 → 4560.04] partners
[4560.04 → 4560.20] at
[4567.06 → 4568.80] century
[4568.80 → 4573.46] dot
[4573.46 → 4573.78] i
[4573.78 → 4574.06] o
[4574.06 → 4574.94] okay
[4574.94 → 4575.36] BMC
[4575.36 → 4575.56] those
[4575.56 → 4575.88] beats
[4575.88 → 4576.14] are
[4576.14 → 4576.50] banging
[4576.50 → 4576.64] we
[4576.64 → 4576.74] have
[4576.74 → 4576.88] that
[4576.88 → 4577.18] album
[4577.18 → 4577.40] out
[4577.40 → 4577.66] there
[4577.66 → 4578.20] dance
[4578.20 → 4578.64] party
[4578.64 → 4578.88] I
[4578.88 → 4578.98] don't
[4578.98 → 4579.06] know
[4579.06 → 4579.22] about
[4579.22 → 4579.38] you
[4579.38 → 4579.56] but
[4579.56 → 4579.80] I've
[4579.80 → 4579.92] been
[4579.92 → 4580.30] dancing
[4580.30 → 4580.62] a lot
[4580.62 → 4580.80] more
[4580.80 → 4581.28] because
[4581.28 → 4582.18] that
[4582.18 → 4582.76] album
[4582.76 → 4583.20] has
[4583.20 → 4583.34] been
[4583.34 → 4583.48] on
[4583.48 → 4583.84] repeat
[4583.84 → 4584.52] on
[4584.52 → 4584.74] all
[4584.74 → 4585.08] my
[4585.08 → 4585.74] places
[4585.74 → 4585.96] that
[4585.96 → 4586.06] I
[4586.06 → 4586.22] listen
[4586.22 → 4586.32] to
[4586.32 → 4586.52] music
[4586.52 → 4586.80] so
[4586.80 → 4587.04] I've
[4587.04 → 4587.12] been
[4587.12 → 4587.42] dancing
[4587.42 → 4587.58] a
[4587.58 → 4587.82] lot
[4587.82 → 4588.50] dance
[4588.50 → 4588.86] party
[4588.86 → 4589.20] is
[4589.20 → 4589.52] out
[4589.52 → 4589.70] there
[4589.70 → 4589.92] check
[4589.92 → 4590.04] it
[4590.04 → 4590.28] out
[4590.28 → 4590.86] at
[4590.86 → 4591.40] changelog
[4591.40 → 4591.56] dot
[4591.56 → 4591.82] com
[4591.82 → 4592.08] slash
[4592.08 → 4592.50] beats
[4592.50 → 4593.32] that's
[4593.32 → 4593.42] it
[4593.42 → 4593.54] the
[4593.54 → 4593.74] show's
[4593.74 → 4594.06] done
[4594.06 → 4594.60] thank
[4597.06 → 4597.50] yeah
[4597.50 → 4606.90] all
[4606.90 → 4608.60] yeah
[4608.60 → 4613.06] all
[4613.06 → 4618.52] the
[4620.64 → 4623.06] all
[4623.58 → 4624.10] oh
[4624.10 → 4626.82] yeah
[4626.82 → 4638.30] Game on.
