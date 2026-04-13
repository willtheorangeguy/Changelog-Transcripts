[0.00 → 11.28] Let's do it. It's Go Time.
[11.70 → 18.42] Welcome to Go Time, your source for wide-ranging discussions from all around the Go community.
[19.04 → 24.06] Big thanks to our partners at Fly.io, the home of changelog.com.
[24.06 → 30.86] Easily launch your app close to your users all around the world. Find out how at Fly.io.
[31.22 → 33.24] Okay, here we go.
[43.56 → 50.62] Well, hello, hello, hello. Welcome, listener. Today, I have a treat of a show for you.
[50.62 → 58.76] So why, you ask? Well, forgive the rather clickbaity how long until I lose my job to AI title.
[58.98 → 65.22] It was either that or we come out and say, don't worry, you won't lose your job to AI, but how boring would that be?
[65.72 → 70.32] The special treat is that I'm here with three special guests.
[70.70 → 75.74] These are folks that I've actually worked with professionally in the past.
[75.74 → 82.92] These are awesome folks. Every time we get together, we get together regularly, even after we've long moved on from the institution that we worked at.
[83.20 → 86.56] We've kept in touch, and we get together, you know, every two or three weeks or so.
[86.70 → 93.10] And we just talk, we chat about the industry, technology, what we had for breakfast.
[93.22 → 96.24] I mean, you name it, you know, we have a good time when we're talking to each other.
[96.30 → 102.54] And we've always joked that, hey, one day we should actually record this stuff because it tends to be hilarious, right?
[102.54 → 110.88] It tends to be hilarious. And it just so happens that we were talking the other day and, you know, AI started coming up in our conversation.
[111.54 → 116.62] And it just gave me the idea that, hey, maybe we should actually take the show on the road, so to speak,
[116.62 → 123.28] and actually have a recording of us, you know, sort of shooting the shit and just, you know, having conversations as we usually do
[123.28 → 130.22] and talk about sort of the impact of AI on our jobs, you know, as they are today and what it might look like in the future.
[130.22 → 136.38] So let me introduce to you my four longtime friends and professional colleagues.
[136.78 → 140.98] First, let's start with Sharon Doris. Sharon, say hi to the people.
[141.22 → 147.44] Hi to the people. I'm currently looking for a job, so I'm going to totally put myself out there.
[147.44 → 158.96] I am a 25-year developer. I have a husband, four kids, a dog, and 14 chickens.
[159.38 → 163.12] I like cooking, knitting, and talking about tech.
[163.62 → 167.28] All right. This sounds like a dating app profile, but okay.
[170.40 → 172.44] All right. All right. Next up, Steve.
[172.44 → 175.42] Yeah. Hi, I'm Steve. I like log walks on the beach and, you know, that sort of thing.
[177.28 → 179.10] Yeah. Hi, I'm Steve.
[179.50 → 191.02] I've also been working in this industry for, yeah, probably about 25 years, too, from C to Java to .NET to back to Java again, you know,
[191.08 → 195.32] and then mostly PHP and Go in the last decade or so.
[195.32 → 198.16] So, yes, thanks to the people on this chat.
[198.66 → 204.42] And, yeah, currently I am a developer and SRE at a little company called Shelter Love.
[204.58 → 207.38] We do software as a service for animal shelters.
[208.08 → 210.88] Wow. Nice. Nice. I didn't know that's what it was called.
[211.12 → 214.36] Yeah, we'll have to talk more about that. That sounds lovely.
[216.16 → 217.58] Kent, last but not least.
[217.96 → 218.26] Yeah.
[218.26 → 224.08] Yeah. I'm slightly reluctant to talk about how many years I've been in the industry, but it's a lot more than 25.
[225.10 → 226.84] No, it's going on 40 now.
[227.48 → 234.98] And I've been around for a bit and date from, you know, the earliest days of PCs and writing assembly code on up through.
[235.34 → 243.34] These days I'm working in Go for a company called Honeycomb, which makes sort of high volume telemetry systems, monitoring systems.
[243.34 → 252.82] And I live in Connecticut with my spouse and have a good, have a beautiful little dog who is fortunately not here today.
[252.88 → 253.80] Otherwise, you'd probably hear it.
[254.76 → 256.36] Yes. Usually by now I'm like, where's Shriner?
[257.10 → 257.36] Yeah.
[258.88 → 259.28] Right.
[259.92 → 263.04] Awesome. Awesome. Well, thank you all for being here again.
[263.04 → 266.84] And, you know, this is, I'm hoping, we have a loose structure.
[267.10 → 273.44] You know, I've got some discussion topics, but as we tend to do, we'll sort of ebb and flow and deviate and come back.
[273.64 → 277.54] But let's open with the hype, right?
[277.86 → 285.42] There is an incredible amount of hype around AI right now.
[285.42 → 295.50] I can measure the hype by how quickly you mention it on social media or in these chats or whatever, because it's like, OK, put that on the hype board.
[295.58 → 296.28] Let's see what happens.
[297.78 → 302.76] I mean, the last time I saw this much hype about anything was around crypto, right?
[302.90 → 305.30] And blockchain and Bitcoin and all that stuff, right?
[305.72 → 307.14] Which I think I'm hearing.
[307.40 → 308.16] You want to see my bullet holes?
[308.16 → 316.32] I'm hearing a little bit less of that right now, maybe because I muted the term on socials and whatnot.
[316.60 → 319.70] But I mean, the hype around AI is just incredible.
[319.78 → 326.90] And whenever there's so much hype about anything, usually the first question I ask myself is, who stands to gain?
[327.72 → 328.42] What do you all think?
[328.86 → 330.80] It's just, yeah, the hype train is in full effect.
[330.80 → 340.74] I mean, everybody, any company that has any kind of business logic that does some sort of transformation or work on data, they just slap the AI label on it.
[340.84 → 343.68] And we've got AI for the marketing purposes.
[344.00 → 346.96] But you've got to find the diamonds on the rough, right?
[347.22 → 349.98] I think, I mean, I've always liked the definition of AI.
[350.12 → 355.58] I hate to say it, but I've been around for several AI cycles now, not to mention other hype cycles.
[356.26 → 357.36] If else, AI.
[357.98 → 358.20] Yeah.
[358.20 → 365.16] Well, and there was a nice thing, like in sometime in the 90s, there was a thing like AI is whatever hasn't been done yet.
[365.56 → 370.18] Like as soon as it becomes accepted capability, then, oh, it's actually not AI.
[370.34 → 371.14] That's just computing.
[371.48 → 377.30] For a while, it was going to be the first, you know, chess champion would be, you know, the dawn of AI.
[377.42 → 379.14] And I was like, no, actually, that's just a big surge.
[379.74 → 381.96] So, yes, it's hyped.
[381.96 → 389.32] I think who stands to benefit, just to get your question right now, is it's the people who have invested in it want number go up.
[389.58 → 392.56] That's usually at least your earliest thing is.
[393.34 → 394.40] I don't know.
[394.48 → 399.58] We can talk more about the hype and who sees the hype and who's getting most excited.
[399.70 → 402.54] Because I do think that's maybe an interesting question for this.
[402.54 → 404.84] Excited about possibilities, not just the money.
[405.20 → 414.90] I mean, if you have yourself a startup these days, and you toss AI in there somewhere, I mean, VCs, you know, presumably are lining up to give you their money.
[415.10 → 416.38] I think that was true a year ago.
[416.52 → 418.62] I'm not as sure it's as true today.
[419.06 → 420.24] There's something to be said for that.
[420.84 → 425.08] I mean, NVIDIA is making a ton of money around AI compute.
[425.82 → 428.46] So, you know, NVIDIA stock is just up and to the right.
[428.46 → 429.26] Oh, I know.
[429.40 → 431.62] My portfolio is very happy right now.
[432.70 → 433.96] So is my partner's.
[436.48 → 436.96] Right?
[437.68 → 442.46] I mean, you have, obviously you have, I think that's more in the nobler end.
[443.20 → 450.12] Even if, you know, some companies, some products are adding AI in sort of gimmicky way, right, just to say they have it.
[450.26 → 456.94] And it seems like, you know, the whole, you know, chat with your doc and whatever, these things seem to be a dime a dozen.
[456.94 → 461.52] And to me, those are sort of the gimmicky implementations, right?
[461.56 → 462.22] Chat with your thing.
[462.26 → 466.28] Not everything I do that could use AI is going to be through chat and things like that.
[466.46 → 476.16] So I think, but because it's the thing that is closest to a regular layperson, right, I think that tends to be sort of the first thing they, you know, that's easy to spot, right?
[476.24 → 479.38] You know, the little, you know, star symbols next to a chat prompt.
[479.50 → 483.10] And, you know, it's, oh, this is, I'm chatting with an AI bot or whatever it is, right?
[483.10 → 492.60] But on the more, say, less noble end of things, you could say there are companies that are laying off in droves, right?
[492.80 → 499.06] Perhaps under the guise that, hey, we don't need as many people to do this job and, you know, because AI.
[499.46 → 508.02] But when really they've just been looking for a reason to lay people off and this is just as good enough of a reason to do so.
[508.32 → 509.74] Am I out of line here?
[509.92 → 511.28] Is that far-fetched?
[511.28 → 525.84] The part about using AI as an excuse or as a lifeboat in the back of their mind, like, oh, if, you know, I have half the people, I can just give them AI to code, and I'll be back to square one.
[526.28 → 527.54] I mean, there's some truth.
[527.68 → 528.52] I mean, we'll get to this, right?
[528.58 → 533.54] I mean, there's some truth to, you know, in terms of productivity gains, right, you can have with AI.
[533.54 → 541.62] I mean, you know, at some point we'll talk about, I mean, even my own workflow as an engineer writing code every day, you know, I benefit from AI.
[541.86 → 544.46] You know, I have been for over six to eight months now.
[544.46 → 556.86] But there is an aspect of this where, like, for example, I read a fun fact from a company that does basically the cut down their customer service workload by like two-thirds or something, right?
[556.86 → 563.48] Because they routed all inquiries and things through, you know, a bot, like an AI agent or something to answer questions.
[563.48 → 571.12] You know, it sort of deals with the most common sets of issues that, you know, users call in about or try to reach an agent, you know, on the website about.
[571.92 → 578.64] And two-thirds of that is not handled by an AI agent, which I think is a great use for, you know, things like that.
[578.86 → 580.30] You know, it's, you know, because...
[580.30 → 582.30] Yeah, unless you're the one on the other end of the conversation.
[582.60 → 583.24] Unless you do.
[583.24 → 596.10] You know, like how much of your, like, you call anybody, or you try to talk to anybody, and you basically have to spend five minutes arguing with an AI to please let me talk to a human because you don't have the answer I need.
[597.44 → 599.50] Well, I mean, that's the thing, though, right?
[599.56 → 605.72] They're saying that the folks are actually closing tickets because they got the answer they wanted.
[605.72 → 618.64] So, you know, this is like, this is not our grandpa's AI, right, where, you know, you're going through the phone tree, pressing all the buttons, trying to press zero or yelling at the thing saying, hey, operator, give me a human, give me it.
[618.68 → 621.12] Like, you know, this is not the same thing at all, right?
[621.36 → 635.06] These days, these things are, I mean, if they have a knowledge base, and you unleash an agent or an LLM or something, right, on that knowledge base, presumably it's the same thing the human, right, that you otherwise would have been chatting with.
[635.06 → 635.98] It's doing, right?
[636.00 → 640.66] They're looking up, you know, a way to give you an answer that is approved by the company.
[640.72 → 641.66] They can't wing it, right?
[641.78 → 643.14] So they have to use a reference.
[643.32 → 651.90] So if you give that reference to an AI bot, presumably it does a much better job, much more accurate and faster job of giving the right answer to the user.
[652.18 → 657.28] And that is one of the sort of use cases which I can appreciate.
[657.68 → 663.08] But the fact that it is still, you know, uses, it still leads to layoffs, right?
[663.08 → 665.56] And these are the kind of jobs that I think are being impacted the most, right?
[666.16 → 666.40] Yeah.
[666.80 → 679.10] So actually, I think that, I guess I feel like when I approach these things, very often the reason I'm trying to get to a human is because I have searched for that information and couldn't find it.
[679.40 → 684.02] And I've searched the knowledge base and know they don't have the answer in their knowledge base, at least not in a form that I can use.
[684.02 → 687.64] And so then the AI is just a delaying tactic for me.
[688.12 → 695.68] However, like, and I think that what's happening here is the AI is perfect at giving you an answer that you can look up.
[695.68 → 706.16] And that is true whether you're using Copilot to write code or talking to, you know, the support bot of your favourite bank.
[706.60 → 717.66] If for average questions, for average commentary, for average code, for things that everybody has already done 2,000 times and there's no innovation involved, the AI is really effective.
[717.96 → 723.78] But when you're talking about, I need to re-architect this system, or I need to...
[723.78 → 725.76] Here's the part where we defend our jobs.
[726.80 → 727.58] There you go.
[727.74 → 728.20] There you go.
[728.78 → 729.26] Sure.
[729.54 → 729.80] Yes.
[729.98 → 736.54] You still need me because I can rewrite the code from scratch and the AI can't.
[737.44 → 742.22] Yeah, I can write the code from your old scratch if it's out there and sucking it up.
[742.52 → 745.52] Well, the problem is, and it's like Johnny, you were saying about, you know, layoffs.
[745.52 → 755.52] But, you know, my fear is that some executive or management someplace is going to be like, oh, we, why are we paying all these expensive developers all this money?
[755.58 → 756.54] We just have an AI do it.
[757.14 → 761.22] And then they have a project or, you know, a huge enterprise thing going on.
[761.32 → 764.70] And then two years later, it fails because they switched to AI.
[765.14 → 767.12] But then it's too late and people have lost their jobs.
[767.38 → 769.16] You know, I think we're trying to avoid that, right?
[769.54 → 772.00] So does everybody here use Copilot?
[773.04 → 773.44] I do.
[773.44 → 773.70] Yeah.
[774.20 → 779.06] So I mean, I use it regularly all the time and it's great.
[779.32 → 783.90] And when I was on a road trip recently and didn't have access to it for a chunk of the time, I missed it.
[784.72 → 794.22] But I also feel like, I don't know, there's some number 10 or 20 percent of the time it writes code that looks right, but is wrong.
[794.70 → 794.96] Oh, yeah.
[795.08 → 800.58] I describe it to people who ask as it's like having a junior developer.
[800.58 → 803.22] You're pairing with a junior developer who types really fast.
[804.44 → 808.38] And most of the time, they're kind of in the right realm.
[808.52 → 810.34] And a lot of time, they even get it right.
[810.42 → 815.28] But then there's that part where it's like, I don't even know where you're going at this one.
[815.28 → 815.82] Mm-hmm.
[815.94 → 817.12] Just like a junior.
[817.54 → 824.40] But you can't, at this point anyway, you can't improve the AI like you can improve the junior.
[825.40 → 827.32] From an end user perspective.
[827.56 → 828.46] And I know there are ways.
[828.66 → 830.32] And actually, we were joking around, Johnny and I.
[830.36 → 832.46] That's how we ended up deciding to do this.
[832.50 → 833.32] We were joking around with.
[833.32 → 840.10] Now, what if I have an AI and I can train it on only certain GitHub repos containing this code?
[840.60 → 841.70] You know, J Briquet.
[841.82 → 842.28] There you go.
[842.66 → 844.74] There's your go-to go code.
[844.94 → 845.90] I mean, it definitely has context.
[846.28 → 851.28] I mean, if I'm writing code in a code base within a repo, it pulls things from the rest of that repo.
[851.68 → 853.06] So it's on the fly.
[853.86 → 855.86] But like, I mean, I was doing one today.
[856.10 → 857.06] And I started the comment.
[857.06 → 857.70] I started the comment.
[857.80 → 858.32] I start typing.
[858.40 → 859.02] I type two words.
[859.10 → 861.10] And it goes, you know, and get the rest of the line.
[862.10 → 865.48] And it's like, that's not what I was going to say.
[865.56 → 866.68] It's not entirely wrong.
[866.88 → 868.12] But it's not what I was going to say.
[868.18 → 869.18] And you just messed me up.
[869.20 → 872.52] And I need to stop and delete that code and rethink what I was trying to say.
[872.56 → 873.52] But not start typing it yet.
[873.52 → 874.96] Because as soon as I do, it's going to fill it in.
[875.72 → 877.46] Just don't pause.
[879.20 → 881.50] Like 500-millisecond delay in your typing.
[881.68 → 882.60] And then it starts to think.
[882.72 → 883.76] It's just like, oh, you're done.
[883.82 → 884.76] Let me pick up something now.
[885.20 → 885.32] Yeah.
[886.84 → 889.10] I'm too much of a machine gun typist.
[889.22 → 890.42] It's like, blip, blip, blip.
[891.10 → 891.40] Yeah.
[891.58 → 892.98] It jumps in all the time.
[893.44 → 899.20] So, I mean, this is sort of a good segue into sort of the impact on the job topic, right?
[899.20 → 916.80] So, I can say with a high degree of certainty that I'd say at least a good 50% of the code I'm writing, or I should say generating right now, is being done so by Copilot, right?
[917.44 → 919.08] But let me qualify that.
[919.08 → 923.42] In the case of Copilot, it's sitting in my workspace.
[923.80 → 925.80] It has access to the entire code base.
[925.94 → 927.60] It can see the patterns I've used before.
[928.00 → 933.28] So, if I'm creating a new handler for my server, well, it knows how I like to write my handlers.
[933.28 → 938.60] So, it can sort of infer that I would want that same consistency, right?
[938.70 → 942.98] So, you know, a new handler, a new route, it just already kind of knows.
[943.30 → 949.10] So, and, you know, I'm just waiting for it to just hit tab and for it to finish, you know, do 90% of the work for me.
[949.14 → 950.24] And I'm like, that's great, right?
[950.24 → 953.42] So, in that sense, my productivity, right?
[954.10 → 958.98] And it has helped me avoid having to type a lot, right?
[959.46 → 961.34] It's a great autocomplete.
[961.34 → 975.14] And this is where I pointed out it might be a situation that a good portion of the code that is out there that is sampling is yours or influenced directly or indirectly by your code.
[975.14 → 980.00] And that's what you're getting the feedback on, which is not accessible to mere mortals.
[980.50 → 986.16] Because I haven't gotten to that point of it kind of knows the way I want to phrase something.
[986.28 → 987.80] And it's probably because I'm phrasing it wrong.
[988.08 → 994.62] But anyway, you know, I haven't gotten to that point where it kind of thought ahead for me most of the time.
[994.82 → 997.64] Like, I think it's fantastic for writing test suites.
[998.00 → 998.26] Yes.
[998.48 → 998.62] Yeah.
[998.72 → 999.00] Yes.
[999.48 → 999.96] Absolutely.
[1000.22 → 1001.72] So, it's so helpful.
[1001.72 → 1003.90] Like, and that's tedious code to write.
[1004.02 → 1005.00] It's so annoying.
[1005.56 → 1013.06] Like, give me that framework and let me type in a couple of, you know, test case values and I don't need to write all that code.
[1013.50 → 1013.98] Yes.
[1014.08 → 1016.00] It's absolutely made me more productive.
[1016.48 → 1016.94] I am.
[1017.18 → 1019.44] I generate useful code faster.
[1020.06 → 1026.82] But somebody who isn't me just trying to hit tab completion would not be able to do that work.
[1026.82 → 1040.08] Because if you haven't prompted it appropriately, by typing the function name you actually want it to write or whatever, it's going to, it's not going to be able to design that thing for you.
[1040.08 → 1045.06] It can help you at the smallest level, but it can't help you with the grand level in my view today.
[1045.06 → 1045.46] Yeah.
[1045.46 → 1053.98] I would say that whenever I use it, what it gives me is syntactically correct, but it's not necessarily what my intent was.
[1054.86 → 1062.14] Like, if I prompt it with such and such a comment, you know, it may create this blob of whatever that's just, it's really fancy.
[1062.28 → 1063.36] It's great, but it's not what I wanted.
[1063.36 → 1068.14] And so it takes, you know, somebody who's done it for a while, like us to-
[1068.14 → 1068.60] Prompt engineering.
[1068.78 → 1068.96] Right.
[1069.08 → 1069.64] And prompt engineering.
[1069.80 → 1069.92] Yeah.
[1070.48 → 1075.26] I mean, I have a couple of, you know, various coworkers who've gotten pretty excited about it.
[1075.62 → 1079.38] And most of the ones who are most excited are the people who do not write code for a living.
[1080.32 → 1087.82] They're salespeople and support people and sales support engineers and all that kind of stuff whose job is to, like, make something work.
[1088.14 → 1092.12] And they sit down with this, and they're very excited because they can make something work very quickly.
[1092.12 → 1096.68] Because what they're trying to do, in my view, is usually something that's been done before.
[1097.18 → 1099.84] And they need that syntactic help.
[1100.26 → 1103.32] And they have the semantics in their heads roughly of what they want.
[1103.50 → 1111.26] So they can say, write me an app to do X because they don't really need the best app in the world, and they're not treading new ground.
[1111.26 → 1117.94] They're doing the thing that's been done before, and they just need to get it on paper or, you know, in their code.
[1118.78 → 1119.50] And that's cool.
[1122.12 → 1127.30] This is a changelog news break.
[1127.96 → 1131.16] Shipping quality software in hostile environments.
[1131.58 → 1133.40] Luca Frederic writes, quote,
[1133.78 → 1139.80] I once had the opportunity to work for a startup that had fallen from tech debt into tech bankruptcy.
[1139.80 → 1143.06] Bankruptcy, Michael, is nature's do-over.
[1143.48 → 1144.52] It's a fresh start.
[1144.64 → 1145.50] It's a clean slate.
[1145.96 → 1147.60] Like the witness protection program.
[1147.98 → 1148.34] Exactly.
[1148.34 → 1148.90] Not at all.
[1149.06 → 1157.36] Although we managed to get it back on the right track, it made me rethink the concept of tech debt and how we ship software, especially in hostile environments.
[1157.74 → 1158.06] End quote.
[1158.06 → 1164.84] He goes on to tell this true story in great detail, which is horrifying, yet echoes so many of our experiences.
[1165.28 → 1168.56] Here's just one of the many horror scenes Luca describes.
[1169.02 → 1169.30] Quote,
[1169.30 → 1193.16] End quote.
[1193.16 → 1200.88] This is a solid essay replete with warnings and a plea at the end to ditch the tech debt concept altogether.
[1200.88 → 1206.52] You just heard one of our five top stories from Monday's changelog news.
[1206.84 → 1219.24] Subscribe to the podcast to get all the week's top stories and pop your email address in at changelog.com slash news to also receive our free companion email with even more developer news worth your attention.
[1219.68 → 1223.14] Once again, that's changelog.com slash news.
[1223.14 → 1236.48] It's one thing to have Jan AI, you know, pump out snippets of code that is part of a larger whole, right?
[1236.54 → 1237.86] Whereby I'm the engineer.
[1238.18 → 1240.10] I am engineering a solution.
[1240.82 → 1245.02] Not just I'm not just a code monkey, just clacking out, you know, syntax.
[1245.28 → 1246.98] I'm trying to fix a problem.
[1247.06 → 1249.58] I'm engineering a solution to a business problem.
[1249.58 → 1253.22] Now I could go, you know, as high level as I can.
[1253.34 → 1257.68] I can just open up, you know, Copilot in chat mode and say, hey, this is what I'm trying to accomplish.
[1258.02 → 1259.96] Start spitting out, you know, files, right?
[1260.36 → 1262.32] Now, maybe today, right?
[1262.36 → 1265.00] It can build somewhat trivial apps.
[1265.10 → 1270.16] I've seen YouTube videos and clips and things of it spitting out entire working React apps and all these things.
[1270.20 → 1271.10] And that's great.
[1271.52 → 1274.56] And I think over time it's going to come even better at doing those things.
[1274.56 → 1282.02] But I have a hard time trying to sort of correlate that or trying to replace solution building.
[1282.20 → 1286.04] Because to me, solutions aren't static, right?
[1286.12 → 1291.18] When a business comes to me and says, hey, I need you to build a solution to this problem.
[1291.94 → 1293.02] I build it.
[1293.50 → 1295.30] They take it into production.
[1295.44 → 1296.28] They do stuff with it.
[1296.32 → 1297.90] And they come back and says, hey, you know what?
[1297.94 → 1298.72] This is great.
[1299.22 → 1301.36] Now I need to change it in this way.
[1301.36 → 1304.38] Or I need to account for this exception.
[1304.62 → 1307.86] Or I need to account for this particular use case or this specific customer.
[1307.98 → 1310.84] Where 90% of the time it works like this way for every customer of this type.
[1311.16 → 1312.58] But for this customer of that type.
[1312.64 → 1314.62] On alternate Thursdays during the phone room.
[1315.06 → 1317.12] It does this completely different thing.
[1317.44 → 1317.70] Exactly.
[1318.30 → 1325.96] So now what am I, like, how are we supposed to treat those, like, entirely made up solutions that, you know,
[1325.96 → 1332.84] am I just feeding that back into the system and saying, hey, so now account for these, you know, alternative approaches.
[1333.22 → 1339.56] Is it going to be like it was when the first generated code frameworks started hitting the scene?
[1339.90 → 1341.86] And you'd go in and there'd be all this code.
[1341.96 → 1343.46] It was like, yes, superfast.
[1343.48 → 1346.86] If you had to do an ORM, it'd ruin all the code for you, et cetera.
[1346.96 → 1348.46] And then you needed to change something.
[1348.46 → 1354.40] And all of a sudden it was like, you know, change management in some of those days was.
[1354.62 → 1354.64] Yeah.
[1354.72 → 1356.76] Or regenerate the whole thing from scratch.
[1356.94 → 1358.62] And, oh, sorry about all your customization.
[1360.78 → 1361.18] Yeah.
[1361.42 → 1366.44] So that'll be another big test that AI has not yet proven it can do.
[1366.62 → 1369.12] Well, so let's talk about art for a second, though.
[1369.16 → 1370.86] Because this is, again, a similar thing.
[1370.94 → 1371.86] Like, everybody's really excited.
[1371.96 → 1375.24] Look at the images I can generate with, you know, mid-journey or whatever.
[1375.70 → 1376.48] With stolen art.
[1376.72 → 1377.40] Well, right.
[1377.40 → 1381.06] But the point is, again, it's going out and giving you the average solution.
[1381.28 → 1387.00] It's going out and going, here are the things that look most like what you described that somebody else has created already.
[1387.52 → 1389.82] And kind of cobble pieces of that together.
[1390.24 → 1395.46] Or here's an opinion formed by the loudest voices out there that I sucked up as source data.
[1395.78 → 1396.82] Hell yeah.
[1397.34 → 1406.52] But, like, I sat in a meeting today where an artist went over her design, basically her design process for a big design project.
[1406.52 → 1410.16] Like, here are the resources I looked at.
[1410.28 → 1413.42] Here's the, you know, the feeling I was going for.
[1413.52 → 1414.52] Here are the things I considered.
[1414.66 → 1415.74] I looked at these typefaces.
[1415.86 → 1421.30] This typeface reminded me of this, you know, building architecture, which is relevant to the site.
[1421.30 → 1432.24] You know, and then that artist proceeded to churn out, over the course of a couple of months, 200 pieces of support art for an event.
[1432.24 → 1447.06] That was a brilliant design exercise by somebody deeply steeped in art and creation who then studied the event and what the event needed and integrated all that.
[1447.78 → 1452.66] And, yes, some random person could have sat down with Mid-Journey and said, make me this stuff.
[1452.66 → 1456.14] And it would have been much less good.
[1457.74 → 1461.62] But people who don't know the difference would have been, sure, it looks fine.
[1461.94 → 1463.64] You know, I mean, we've all seen that, right?
[1463.76 → 1466.66] You know, my document has 37 fonts and 12 colours.
[1466.98 → 1469.12] But it looks fine to me.
[1469.12 → 1475.98] But, like, there's a big difference between, you know, something crafted and something just slapped together.
[1476.50 → 1480.96] And, yeah, I guess I think that AI is going to make it easier to slap together.
[1482.04 → 1484.26] But for most people, though, would you argue?
[1484.50 → 1485.90] So here's what I'm not saying.
[1485.96 → 1489.66] I'm not saying that these things generated by AI.
[1489.66 → 1503.82] Like, if you're a connoisseur of a particular art, you know, you're an architect of a particular kind of application or solution or, you know, or thing, whatever it is, you can critique, right, the output of Gen AI as it stands today.
[1503.96 → 1506.56] Again, arguably, it's going to get better at what it does, right?
[1506.66 → 1510.34] But you can critique the output today and be like, this is subpar, right?
[1510.36 → 1513.10] This is not as good as what I could have come up with.
[1513.40 → 1516.90] But for most people, it's good enough.
[1517.46 → 1518.58] It depends on what they're using it for.
[1518.58 → 1523.04] And so, again, if you're just doing something for yourself, who the hell cares?
[1523.22 → 1526.52] I mean, yeah, I'll slap something together out of two by fours if I'm building it for my garage.
[1526.66 → 1527.16] I don't care.
[1528.02 → 1535.06] But if I'm going to sell it, if I'm going to make a business around it, that's the part where I'm saying I don't think the AI stuff is there.
[1535.18 → 1546.00] If you're just doing a hacky project for personal use, yeah, I mean, maybe you would have had to pay somebody to come in and slap that shelf together in your garage if you didn't have the skills to do it yourself.
[1546.00 → 1552.06] And so now there's this kind of, you know, yes, there are a few things that I couldn't do before that now I can do today for myself.
[1552.56 → 1555.60] Design that invitation for my kid's birthday party.
[1556.08 → 1556.52] Hell yeah.
[1556.52 → 1560.50] I can't draw, but I can use an AI.
[1561.10 → 1562.32] There's nothing wrong with that.
[1562.58 → 1567.96] And yet, you know, so, yeah, there's probably some, you know, the kid next door, you're not paying 20 bucks to do that for you.
[1568.20 → 1568.94] But that's now.
[1569.18 → 1572.90] What happens in, you know, in the future as AI evolves and improves?
[1572.90 → 1578.44] So, you know, did we get to this uncanny valley level of like, oh, now it's not just good enough.
[1578.56 → 1578.86] It's like.
[1578.94 → 1580.02] It's like the standard.
[1580.28 → 1581.58] Now it's building your whole kitchen.
[1581.94 → 1582.20] Right.
[1582.88 → 1584.26] Do we need to worry about that?
[1584.64 → 1591.60] And how much coding out there is most of what's out, you know, how many cruds have we ever created in our lives?
[1592.18 → 1594.00] How many cruds are still being created every day?
[1594.60 → 1594.82] Yeah.
[1594.90 → 1595.22] Okay.
[1595.34 → 1599.20] So that's a problem that's largely been solved greater or lesser degree.
[1599.54 → 1601.26] But yeah, I mean, it's white box, right?
[1601.26 → 1602.72] You make white box easy to do.
[1602.72 → 1603.12] Yeah.
[1603.50 → 1615.96] And tech has always been making things that had gates around them or real or created limited availability or and making them more available.
[1615.96 → 1620.18] Like artisan things that used to be only certain artisans could do that.
[1620.26 → 1623.60] Only musical artists had a studio and an audio engineer.
[1623.84 → 1629.90] And now they can go and, you know, create their own tracks with one app at home.
[1629.90 → 1633.08] For me, that's the part that's like, oh, I can't complain.
[1633.16 → 1641.54] I can't be the curmudgeon complaining about this latest thing that might make something that I do more accessible to other people.
[1641.76 → 1644.74] Like I've benefited from these other things that came along.
[1645.20 → 1646.28] It's time to share the wealth.
[1646.86 → 1647.50] I don't want to.
[1647.76 → 1649.22] I'm really rooting against it.
[1649.22 → 1650.22] Yeah.
[1652.22 → 1653.90] I don't think it's about gatekeeping.
[1654.48 → 1660.70] I mean, I'm not like I feel like a big chunk of my career has been spent trying to help people learn to program.
[1660.70 → 1667.96] And so I'm not thinking that the reason I'm skeptical is that I don't want other people to do what I do.
[1668.10 → 1674.84] I think it's more because I feel like the hype and the reality are distinct.
[1675.14 → 1680.90] That what the reality is producing is mostly devoid of creativity.
[1681.36 → 1686.12] People are confusing knowing what to look up with being creative.
[1686.12 → 1690.96] And I think knowing what to look up is a skill and a lot of us have it.
[1691.20 → 1693.02] And the better engineers, I think, are better at it.
[1693.18 → 1696.66] And so, yes, AI helps to ease that problem.
[1697.16 → 1705.40] But knowing what to even ask about, you know, like or looking at a new solution to a problem,
[1705.40 → 1714.02] that's something that I think is well beyond what AI is capable of now or in the reasonably like the LLM model,
[1714.20 → 1716.94] I think, is fundamentally non-creative.
[1717.32 → 1718.34] That's my take on it.
[1719.26 → 1719.66] Spicy.
[1720.38 → 1724.50] We're not at the unpopular opinions yet.
[1724.50 → 1733.50] So one thing you mentioned, like the whole teaching, like you all remember when maybe it was during maybe first or second Obama term or something,
[1733.64 → 1736.38] but there was this giant push to teach everybody how to code.
[1736.82 → 1737.02] Right.
[1737.30 → 1738.42] Like it was everywhere.
[1738.52 → 1739.34] It was in the media.
[1739.50 → 1740.34] It was in newspapers.
[1740.52 → 1744.04] It was like, you know, we need to teach our young how to program.
[1744.04 → 1754.20] Now I'm looking at a clip from, you know, NVIDIA CEO like three or four days ago or something saying, hey, people shouldn't learn how to program.
[1754.54 → 1757.94] You should now let, you know, the new programming language is a human language.
[1758.08 → 1760.20] And I'm thinking, man, you are sitting here.
[1760.46 → 1764.12] You stand to gain billions of bazillion dollars.
[1764.12 → 1764.56] Right.
[1764.70 → 1769.08] If your wish comes to it, because you're producing, you know, chips and stuff for these things.
[1769.14 → 1770.32] Of course you're going to say that.
[1770.34 → 1770.54] Right.
[1770.54 → 1775.38] So this so I mean, what I'm definitely not on the don't teach people how to program camp.
[1775.60 → 1779.24] No, no, I'm going to I'm going to take a slightly spicy take here.
[1779.96 → 1785.30] I don't think he's completely off now in the time we've all been engineers.
[1785.38 → 1793.02] We've seen waves of different things that are going to come and take our jobs, you know, offshoring and, you know, code generation now AI.
[1793.42 → 1794.70] And they haven't.
[1794.70 → 1801.30] And my theory is that the key thing that an engineer has is the ability to communicate.
[1801.30 → 1812.94] And even when you're supposed to be communicating to people on the other side, product, the business, whatever affectionate term you use for them, aren't always as good at that.
[1813.30 → 1814.76] Although it should be part of their job.
[1814.84 → 1821.46] But having somebody who can think back and forth, there will, I think, always be a need for those people.
[1821.46 → 1825.58] Because every CEO thinks they have the answer to every question.
[1827.42 → 1828.48] That's what they hate to do.
[1829.54 → 1829.90] Right.
[1829.98 → 1831.62] But they really shouldn't.
[1831.68 → 1836.56] If they have a business that's big enough to grow, their biggest skill is finding the people and put in the right place.
[1836.56 → 1848.06] So if your job right now is like doing cruds for a company that can't even explain what they want, I wouldn't worry because they're not going to be able to explain what they want to AI.
[1848.42 → 1848.62] Right.
[1848.92 → 1849.06] Yeah.
[1849.08 → 1850.14] No, it's the thinking logic.
[1850.34 → 1850.68] It's yeah.
[1850.76 → 1854.12] There's the think about break something down into steps and think logically.
[1854.12 → 1863.98] Like I once did have a client very early in my career who was a pretty good business person who really wanted to automate his business.
[1864.14 → 1866.90] And he was able to sit down and explain it to me.
[1867.14 → 1873.42] Like if he had had the tools to program, he could have written his own code because he thought about it really logically.
[1874.00 → 1880.58] And it was just my job to basically take dictation and turn it into Pascal for him back in the day.
[1880.58 → 1884.90] But that's few and far between.
[1885.60 → 1890.82] You know, quite honestly, most people who specialize in business aren't specializing in thinking logically.
[1891.26 → 1894.70] They specialize in thinking about people and like you said about communications.
[1895.40 → 1898.10] So does AI then make you more what you already are?
[1898.44 → 1900.00] If you're a logical thinker, you'll benefit.
[1900.40 → 1902.20] And if you're not, you still struggle.
[1903.74 → 1905.56] And who gets to train the agent?
[1907.08 → 1909.88] I want to be in the training side.
[1909.88 → 1914.00] I want to be the one doing the building of the things that you use.
[1914.42 → 1914.86] That's right.
[1915.06 → 1917.12] That's a good question.
[1917.66 → 1922.28] I think at the point when it comes to like a personal AI where it's just like it's tuned to you.
[1922.94 → 1924.34] Your data doesn't get shared.
[1925.16 → 1928.32] It's just, you know, then it becomes like a superpower, right?
[1928.40 → 1930.66] You can just it's like you're compiling.
[1930.66 → 1932.82] But how would that work?
[1932.82 → 1937.72] If it's only got your data, it's basically replicating to a point you.
[1938.26 → 1941.52] There's a generic it's trained on the universe.
[1941.86 → 1942.38] Right.
[1942.50 → 1943.98] And then specialized for you.
[1943.98 → 1944.24] Right.
[1944.46 → 1946.46] Is the way that we're seeing all of this.
[1946.58 → 1946.72] Yeah.
[1946.98 → 1950.94] It's like creating your own GPT, but it's based on the larger model.
[1951.08 → 1951.34] Right.
[1951.80 → 1952.34] Yeah, exactly.
[1952.34 → 1964.32] So, I mean, like my company, we built we have a query engine that looks like SQL, and then we built an AI where we train that AI.
[1964.32 → 1973.70] Like as part of the part of the prompt, we basically can go out and get your data and all the names of your fields and the data types of your fields.
[1973.70 → 1981.08] And we can plug them into the AI query so that when you say show me my slowest service, it can go.
[1981.22 → 1981.36] All right.
[1981.38 → 1985.60] What are the fields that are named according to, you know, time duration?
[1985.80 → 1987.86] And what are the things that look like a service name?
[1987.86 → 2003.16] And now I can write a query for you so it knows how to query Honeycomb, and then it can write that query for you from your inept prompt because it's been specialized for that particular type of application.
[2003.40 → 2005.02] And I think that's a really cool use of AI.
[2005.60 → 2009.22] That that is a productivity boost for people who are already technical.
[2009.22 → 2013.22] Like, you know, full disclosure, I am my startup is a Honeycomb customer.
[2013.22 → 2018.58] So, you know, I will go in the dashboard and I can formulate those queries.
[2018.90 → 2029.40] But I'm already a highly technical user who knows how to use these kinds of tools to get to and know exactly what kind of data I'm looking for and when I've found it.
[2029.90 → 2040.54] Now, for the layperson, right, who doesn't know, like the layperson, like the more I think about it, the more I'm thinking, OK, if I'm a one end of the spectrum,
[2040.54 → 2055.04] you have the complete layperson who is using perhaps, you know, Chad GPT or something like it to maybe generate copy and not hiring a copyright person like you might traditionally do back in the day.
[2055.34 → 2066.12] Right. I'm sure the copywriters of the world are suffering right now because content creators, you know, like content is like, yeah, content creators are suffering because this stuff is now being generated.
[2066.36 → 2067.68] So are all our Google searches.
[2067.68 → 2073.28] Right. So if that was your job, absolutely, you're impacted.
[2073.60 → 2079.02] Right. And the layperson can now bypass you and get to something that, again, the good enough.
[2079.28 → 2082.40] Right. They can get something good enough to achieve some means.
[2082.48 → 2087.94] Right. On the complete opposite of the spectrum, you have people who engineer software.
[2088.58 → 2094.24] Right. That, again, given the context of the conversation, we're talking about like how safe is our jobs.
[2094.24 → 2105.68] Right. And so when I'm asking this question, I'm not asking, is the layperson going to find ways of reducing their reliance on sort of I don't want to say lower skill, just the different kind of skill.
[2105.68 → 2114.84] Right. I'm thinking like for people like us as software engineers who presumably will be impacted by this to some degree.
[2115.06 → 2122.26] Right. And we already are. Right. For us, there's also the micro spectrum whereby if you're on sort of the lower end of that spectrum.
[2122.26 → 2128.20] And if the only thing we are doing is generating crud, well, I'm sorry, your job is indeed in jeopardy.
[2128.32 → 2143.04] If that's the only thing you've been doing right with your career on the opposite side of it is the highly specialized person who understands a business problem has to debug and troubleshoot and talk to people and integrate different things.
[2143.18 → 2144.46] And institutional knowledge.
[2144.64 → 2145.56] Right. All that stuff.
[2145.56 → 2147.80] I mean, I don't see that skill.
[2148.06 → 2151.82] Right. I don't see that being replaced by AI anytime soon.
[2152.66 → 2153.54] Am I wrong here?
[2154.38 → 2155.48] I don't think so.
[2155.90 → 2156.30] Personally.
[2156.56 → 2158.18] How many of those people do we need?
[2158.54 → 2159.82] And that's the thing, right?
[2160.12 → 2161.78] I mean, is it a game of musical chairs?
[2161.88 → 2163.32] We should be looking for our chair now?
[2163.80 → 2166.82] No. Any business is thinking, do I need a thousand engineers?
[2167.20 → 2169.30] Right. When 500 will do.
[2169.30 → 2179.08] I mean, I think as we've all said, right, it makes us more productive today. So I'm writing more lines of code per day than I was five years ago.
[2179.32 → 2180.68] Right. Right. Right.
[2180.68 → 2187.86] So that's good, you know, but we all kind of expect productivity to continue to rise. So this is a productivity tool.
[2187.86 → 2190.48] Mm-hmm. Not a replacement tool.
[2190.60 → 2205.92] You know, we're also using languages that are more expressive than they were. You know, like the code I write in Go is probably one third the length of the same code I write in C++ or used to write in C++ back in the day.
[2206.40 → 2215.26] So that's also a productivity boost at some level, at least if you believe the old metrics that it's basically you can write the same number of lines of code per day no matter what language you write it in.
[2215.26 → 2238.68] But I think actually knowing how to use it is a skill to put on your resume, but not before too long, or if not now. I mean, even if I didn't want to use it, I would because it's becoming of like, it's going to be a point where like, oh, you know, I use Copilot all the time. Oh, good. You have the point for you to get the job.
[2238.90 → 2241.34] It's prompt engineering I know already in your link in Copilot.
[2242.34 → 2243.32] It's going to be soon.
[2243.32 → 2250.02] No, but if you put it in your interests as AI, it shows up in the keyword searches.
[2250.02 → 2250.98] Oh, there you go. Right?
[2252.72 → 2253.08] Nice.
[2253.52 → 2265.36] I mean, that's a good point. But to me, it's like back to my woodworking thing. It's like, I know how to use a power saw. I know how to use a drill press. I know how to use a lathe. You know, those are kind of expected.
[2265.36 → 2271.92] Today, if I'm going to do woodworking and say I only use hand tools, people are going to look at me like, I don't have time for you.
[2271.92 → 2272.70] Same thing. Yeah.
[2272.70 → 2276.86] And the same is true of like, if you're not using Copilot, what am I paying you per hour?
[2277.04 → 2277.22] What are you doing?
[2277.50 → 2281.04] You know, why are you not as productive as you could be?
[2281.04 → 2281.44] Yeah.
[2281.64 → 2293.52] I think at this point, the only people who really aren't using it are people who are doing like very arcane languages or people who their businesses, they don't allow it. Their company doesn't allow it. I think everybody else has at least tried it.
[2293.52 → 2313.80] I mean, if you're a company that doesn't allow such things, like I understand not bringing sort of open source code into your organization that might be the wrong licensing model for you or something like that. Right. You don't want to be in some hot water. All you have to do is look at, you know, Oracle and Google over the whole Java thing. I think those are the companies involved.
[2313.80 → 2342.22] But if you allow your engineers to use a model where you can control the kinds of things that were used in the model, right, for the training, and you can have maybe you can run your own internal, right, Gen AI for code generation, whatever it is. Right. I think if you're an organization that is afraid of these things, you should at least follow that route as opposed to saying, hey, nobody can use any Gen AI coding tools whatsoever, because I think you're going to lose people if you do that.
[2342.22 → 2356.04] Because I'm going to look at my peers that get to use these things, and they're learning those skills, right? And then now I'm falling behind because everybody's using, you know, some sort of code generation tool, and I'm not, right? I mean.
[2356.44 → 2370.48] This is where I hope somebody reaches out to somebody who hears this and reaches out and can answer that question of like, can you have a copy of Copilot that you train on a specified set of repos and only those repos?
[2370.64 → 2371.44] Private repos.
[2371.44 → 2371.74] Private repos.
[2371.88 → 2378.30] Well, I mean, I would, you know, as we joked, I mean, if I'm a Go developer, I'm training it on Johnny's code.
[2379.38 → 2381.10] Because if I don't like it, I can know Johnny.
[2383.06 → 2383.34] Nice.
[2383.80 → 2384.58] I don't know what I mean.
[2384.64 → 2385.50] There's people out there.
[2385.82 → 2386.74] One neck to choke.
[2386.82 → 2387.22] I get it.
[2387.30 → 2387.74] I get it.
[2387.86 → 2389.96] It doesn't matter what language it is.
[2389.96 → 2394.46] There's people out there that you respect their code, and you'd be like, yes, I would like my code to be more like this.
[2394.50 → 2398.92] I wish it would learn that that's what I was thinking or that's the way this problem should be thought about.
[2398.92 → 2403.42] I mean, yes, there's precious few of those people and those people will probably never lose their jobs.
[2403.42 → 2408.38] But for the rest of them, your mortals that are going to have to work with the tools that are out there.
[2408.52 → 2415.54] And I would love if this is a possibility now that you could train Copilot on what you'd say to train it on and not all of GitHub.
[2415.54 → 2418.44] I think there are companies that are working on that product.
[2419.02 → 2421.82] I feel like I've even seen a product announcement like it.
[2422.28 → 2431.82] But yeah, I mean, you know, the thing about it is you can take one of these LLMs and you can essentially subset it, and you can make a tiny compact LLM that will run in a box that you can actually stand on your desktop.
[2432.38 → 2435.34] And then you can further train that with new information.
[2435.34 → 2438.10] So that's exactly what you want to do here.
[2438.18 → 2446.36] You want to take a coding centric LLM like a Copilot and create the mini version of it and then train it on your repositories.
[2446.82 → 2448.08] And now it knows how to write your code.
[2448.18 → 2450.44] And it's also not talking out to the cloud while you're doing it.
[2450.94 → 2452.74] So there's got to be businesses like that.
[2452.96 → 2456.62] And this is where we redact all of this and put it into our business plan.
[2456.62 → 2461.20] So hang on, hang on.
[2461.58 → 2465.28] I have an actual question here to sort of move us along.
[2465.52 → 2475.16] If you're going to school right now or thinking about going to school for a computer science degree or some technical degree, right, where some form of programming is involved and things of that nature.
[2475.86 → 2479.78] Again, I know for all of us on the school, I know it's been a long time since we've been in school.
[2479.78 → 2491.70] But if you were to go back, right, 30, 40 years, and you're not entering school and thinking about a computer science degree, how are you approaching this decision?
[2492.50 → 2494.08] We probably all have spicy takes.
[2495.32 → 2495.88] Yeah.
[2496.36 → 2498.42] Of whether to use AI or not?
[2498.90 → 2499.40] No.
[2499.88 → 2506.76] Whether to study CS or some other industry that you think is ripe for being overtaken.
[2506.76 → 2514.80] I think, personally, I mean, if you really, if you like computers and want to work in this field, you damn well better know how to use AI.
[2515.34 → 2520.88] I would hope you find a program like there are some fundamentals of computer science that are probably worth knowing.
[2521.36 → 2532.94] But I don't really need you to be able to, like, I've said this for decades now that I don't really care if you can write every possible sort algorithm from the algorithms book or know how they all work.
[2532.94 → 2538.46] Or that kind of stuff is a lot less important because I can just get that off a library that somebody else has written that.
[2538.98 → 2546.46] But you should understand a lot of the basic principles and how to use an AI to achieve them.
[2546.82 → 2550.02] But, like, when I think about, so I spent 15 years in game development.
[2550.44 → 2561.74] If I say to a class, go out and create an original game using words or something like that as a class assignment, that's not something you can type into an AI very easily.
[2561.74 → 2562.98] I mean, you're going to get something, maybe.
[2563.30 → 2565.86] But you've got to, it requires some creativity.
[2566.18 → 2567.76] It requires putting some pieces together.
[2567.98 → 2570.44] It requires using various components.
[2571.20 → 2577.12] And that's the I don't know, that feels like that's something like that.
[2577.16 → 2580.86] And being able to work with people is a better fit.
[2581.36 → 2581.70] Absolutely.
[2582.08 → 2586.68] I mean, so I've had conversations with my kids that are in college right now about this very thing.
[2586.68 → 2593.92] And to me, it's more important to get a broad, generalist, foundational education.
[2594.50 → 2596.46] Not, you know, if you want to do comp side, great.
[2596.86 → 2599.50] If you want to do, like, I was a psych major, right?
[2599.92 → 2608.36] What your major is, I think, is less important than getting a more of a broad set of skills and a broad base of learning.
[2608.92 → 2610.00] And that's what I tell my kids.
[2610.60 → 2611.62] You can pick up the rest later.
[2611.62 → 2615.52] Are we being fair, though, just because we did pick up the rest later?
[2616.22 → 2621.02] We also caught the wave at a time when knowing how to spell HTML got you a job.
[2623.02 → 2624.66] And thank God for that wave.
[2625.30 → 2626.20] Not for me.
[2626.20 → 2633.20] Well, so I've worked with a couple of, you know, with several junior engineers over the last few years.
[2633.46 → 2636.72] And some of them have done very well and some of them haven't.
[2637.26 → 2643.18] And the ones who've done well are mostly the ones who, like, know how to work.
[2643.58 → 2651.04] That know how to, you know, study a problem, figure out what needs to be solved, find the problems that exist within it,
[2651.04 → 2656.02] and then address those things at whatever level they're capable of addressing them.
[2656.20 → 2668.78] So the brilliant computer scientist is less important than being able to, like, have a real conversation and understand the real problem and work with other people.
[2669.14 → 2671.00] So I want you to get that out of college.
[2671.14 → 2677.14] So I want you to be going to a college where a lot of your work is working in teams to make things happen.
[2677.66 → 2678.54] Oh, God.
[2680.84 → 2684.52] I still haven't processed the trauma from working on teams in college.
[2684.52 → 2685.60] I get what you're saying, though.
[2685.60 → 2685.76] Yeah.
[2686.20 → 2687.88] I know what you mean because you get the...
[2687.88 → 2689.16] Yeah, the aspirational.
[2689.38 → 2689.48] Yeah.
[2689.58 → 2697.42] So one of the values, I think, you're supposed to derive out of a college experience is, you know, learning to collaborate.
[2697.60 → 2698.66] Yes, that's definitely part of it.
[2698.72 → 2702.54] But the whole learning how to think thing, right?
[2702.96 → 2703.58] That's...
[2703.58 → 2704.22] Critical thinking?
[2704.46 → 2705.52] Yeah, critical thinking.
[2705.92 → 2706.16] Like...
[2706.16 → 2706.76] Inductive reasoning.
[2706.92 → 2707.64] Deductive reasoning.
[2707.94 → 2708.94] It's one thing...
[2708.94 → 2710.70] Philosophy was actually good for that stuff.
[2710.70 → 2711.14] Yeah.
[2711.52 → 2712.14] I know.
[2712.38 → 2713.66] Like a very underrated...
[2714.32 → 2715.36] Liberal arts degrees.
[2715.74 → 2716.18] Yes, please.
[2717.72 → 2721.24] Philosophy was a very underrated topic in college.
[2721.44 → 2721.92] I'm in college.
[2721.92 → 2723.32] But, you know, I digress.
[2723.32 → 2730.04] So I want somebody coming out of college to know how to ask the right questions, right?
[2730.34 → 2731.36] It's not...
[2731.36 → 2733.08] The difference is to use, again, to use AI.
[2733.46 → 2735.18] It's the difference between saying...
[2735.18 → 2743.42] Going to something like a ChatGPT and saying, hey, I want to use BOGO sort, the worst performing sorting algorithm ever produced.
[2743.66 → 2745.80] I want to use BOGO sort in this data, right?
[2745.80 → 2748.38] And then give me the code sample for it.
[2748.66 → 2750.70] Gen AI will gladly oblige, right?
[2750.90 → 2756.14] It's different to basically say, hey, I have data that is shaped like this.
[2756.44 → 2762.06] What is the best kind of sorting algorithm for this particular objective of mine, right?
[2762.46 → 2765.62] Like, you're trying to solve, right, the problem.
[2765.66 → 2766.98] You're going to get a solution at the end.
[2767.20 → 2773.44] But knowing how to ask the right question, right, to me is the value of a college education.
[2773.44 → 2780.28] So I'm not saying people going to college or thinking about going to college shouldn't because AI, right?
[2780.56 → 2781.58] That's kind of silly.
[2781.70 → 2789.18] That's a very bad reason not to go to school, not to get an education of any kind, whether it's college or, you know, professional development training or buying a course or whatever it is, right?
[2789.66 → 2791.44] You should always be learning, always be learning.
[2791.60 → 2793.96] Regardless of what the hype says, always be learning, right?
[2794.20 → 2801.84] But it's a whole different thing to know enough to be able to ask the right questions, I would say.
[2801.84 → 2809.52] Well, isn't there like a tendency of interviewing where they ask the candidate a really hard ask?
[2809.80 → 2823.84] You know, and I'm not talking about just like elite code hard or something, but like the whole intent of the exercise is to understand how the brain kind of processes the problem and how it seeks more information and how it kind of builds hypotheses and et cetera.
[2823.84 → 2826.24] I don't know where I was going with that.
[2826.96 → 2829.56] I heard politician and question was asked.
[2831.24 → 2832.90] I was like, yep, that checks out.
[2833.52 → 2833.80] Yep.
[2833.80 → 2834.80] Okay.
[2837.00 → 2837.68] Okay.
[2838.08 → 2838.38] Okay.
[2838.70 → 2843.80] So my next question then is basically kind of along the same lines.
[2843.80 → 2849.24] If you are entering the field today as a professional, let's just put it this way.
[2849.44 → 2851.86] All of us here are professionals, many years of experience.
[2852.16 → 2861.10] If you're about to transition into a new job where you know AI might be a requirement or even if it's not explicitly stated, right?
[2861.74 → 2863.28] How are you preparing to make that switch?
[2863.84 → 2865.06] What are you doing right now?
[2865.06 → 2867.78] I'll give a very pragmatic answer.
[2868.24 → 2875.58] I am moving away from front end cred or doing my best to, even though I'll be honest, that's what's on my resume and what I get the most calls for.
[2876.00 → 2880.54] I think the front end cred is going to simplify.
[2881.06 → 2885.00] You know, it's already kind of distilling down to, you know, a handful of frameworks.
[2885.50 → 2889.80] And even those frameworks are used in, you know, even a more prominent way.
[2889.80 → 2893.70] So I'm not seeing that as a growth industry.
[2894.16 → 2899.48] And I'm really sad if you just went through a boot camp, and they told you were going to make a lot of money.
[2900.12 → 2904.88] And, you know, maybe that was the case five years ago, but it's a different world.
[2905.44 → 2908.04] Personally, I'm getting closer to the data again.
[2908.42 → 2909.80] I don't think data is going to go anywhere.
[2910.10 → 2919.68] And I think that they're always going to need people to feed the voracious beast of AI when it comes to analyzing data.
[2919.68 → 2920.58] And understanding data.
[2921.16 → 2936.90] And if you haven't, if you're a front end person who hasn't dealt with a lot of data at any level of the stack other than JSON, I would honestly start looking at what goes into, you know, creating the API responses that you get, for instance.
[2937.44 → 2939.34] Just start looking a little deeper.
[2939.34 → 2951.68] So if you're a front end dev and the only thing you've ever done is consume APIs and send something in, something comes back out the black box, now it's time to start investing.
[2952.36 → 2954.24] It might be time to start, you know.
[2954.38 → 2960.22] And maybe you're doing a bunch of GraphQL and you have experience as an architect in that.
[2960.70 → 2961.10] Fantastic.
[2962.00 → 2963.38] That's a step in the right direction.
[2963.50 → 2964.46] I would still keep going.
[2965.02 → 2966.12] Learn what you can about data.
[2966.22 → 2966.96] It's not going anywhere.
[2966.96 → 2968.96] But you got to go all the way back.
[2969.66 → 2970.06] Maybe.
[2970.84 → 2971.16] Maybe.
[2971.54 → 2972.52] Select star from.
[2976.94 → 2977.90] Got to start somewhere.
[2978.22 → 2979.48] Hey, sequel never goes out of style.
[2979.92 → 2980.46] No matter what they tell you.
[2980.94 → 2981.86] No, it doesn't.
[2983.02 → 2984.56] I rode the Congo away for a while.
[2986.06 → 2986.80] I'm sorry.
[2988.42 → 2989.70] I'll apologize now.
[2989.70 → 2996.80] I like Congo.
[2997.80 → 2998.98] I actually still do.
[2999.24 → 2999.86] It's fine.
[3000.08 → 3000.30] It's fine.
[3000.82 → 3001.82] I'm just being spicy.
[3002.06 → 3005.18] It's just not, shouldn't be used for a lot of the things that it was used for.
[3005.72 → 3009.68] I still think there is plenty of room for new engineers.
[3010.06 → 3013.72] I think there is plenty of work still to be done.
[3013.72 → 3018.00] It's the learning process is probably accelerated.
[3018.16 → 3022.46] You're less about, you know, when you're, when you're a E3 first or second or third year
[3022.46 → 3025.32] engineer trying to like to get stuff done.
[3025.70 → 3031.34] It's less about just figuring out how to write code and more about figuring out how to assemble.
[3031.56 → 3033.54] You're figuring out what questions to ask.
[3033.54 → 3038.90] Like you said, Johnny, it's like what needs to be done and what's the right way to do it.
[3039.22 → 3043.94] That's the stuff you're learning to teach your AI to answer your questions for you.
[3043.98 → 3047.64] Maybe because the questions you're answering are ones that are within the capability of AI
[3047.64 → 3048.82] when you're early on in your career.
[3048.94 → 3053.30] So you need to be able to learn how to manage that system, put it together, be productive with it.
[3054.02 → 3058.44] So there is still, as far as I know, a college premium.
[3058.62 → 3062.88] Like if you don't go to college, you're not going to make less money in your lifetime than if you do go to college.
[3062.88 → 3070.32] I think that premium has been declining in recent years, but I still think it's worth it from what I've been best able to understand.
[3070.98 → 3078.18] You know, so I still an enthusiastic supporter of going to college and getting a good education.
[3078.36 → 3091.00] But I do think ever, even more than I used to think that a liberal arts education is really powerful, and you shouldn't just concentrate on learning the tech of the moment, whether it's AI or Photoshop or whatever it might be.
[3091.00 → 3093.42] Like, you know, learn more than that.
[3093.72 → 3095.64] Learn how to, you know, go to your philosophy class.
[3097.44 → 3098.38] Learn how to write.
[3098.96 → 3099.46] Learn to think.
[3099.48 → 3100.50] Even if it's 8 o'clock in the morning.
[3100.70 → 3101.24] Learn to write.
[3102.66 → 3106.42] Despite AI translators, it's still really useful to be able to speak more than one language.
[3106.74 → 3114.96] You know, like I can't tell you how many people I've met in the game industry, some of the top people in the game industry who all seem to have a linguistics background.
[3115.18 → 3115.74] It's fascinating.
[3116.30 → 3116.66] Interesting.
[3117.08 → 3117.60] And music.
[3118.32 → 3118.68] Interesting.
[3119.36 → 3120.48] I have neither of those backgrounds.
[3121.88 → 3122.76] Bachelor of Fine Arts.
[3124.68 → 3125.38] That's as good.
[3125.50 → 3127.62] I mean, that goes right in that list, in my view.
[3128.14 → 3128.36] Yeah.
[3128.60 → 3131.96] And it turns out my major was actually a very small number of hours required.
[3132.58 → 3135.98] So every other hour I had was like, I had so many electives.
[3136.40 → 3137.48] I was all over the school.
[3137.70 → 3138.72] It was great.
[3139.16 → 3140.60] I highly recommend it if you can do it.
[3140.60 → 3149.52] But there's so many, you know, the push to get job skills and not waste your mom and dad's money on basket weaving.
[3149.78 → 3154.06] And it's like, I'm on team basket weaving.
[3154.30 → 3154.62] Sorry.
[3154.62 → 3160.26] I mean, I went back to get a degree in software engineering afterwards, like halfway through my career.
[3160.72 → 3162.64] But that was later.
[3162.76 → 3164.42] It wasn't really, it was useful.
[3164.54 → 3165.20] I'm glad I did it.
[3165.26 → 3166.80] But it wasn't necessary.
[3166.80 → 3172.54] You know, I'm wondering if that's still going to be the case for this generation.
[3172.90 → 3173.00] Right.
[3173.02 → 3177.26] Because, you know, like you, I actually got my bachelor's degree.
[3177.38 → 3177.80] I have two degrees.
[3177.88 → 3179.80] I have a bachelor's and a master's in science.
[3180.22 → 3184.70] Like my bachelor's came while I was already 10 years out in industry.
[3185.12 → 3185.34] Right.
[3185.80 → 3189.22] And I completed my degree, you know, one class at a time.
[3189.66 → 3195.90] You know, I took my time about it because there was no, I didn't need to do to get a job and be paid.
[3195.90 → 3197.64] So I just took my time about it.
[3197.72 → 3197.84] Right.
[3198.22 → 3205.96] I'm wondering, and the same thing for my master's, like I, online, I'd never showed up ever to a class and I took my time and I did it.
[3205.98 → 3206.12] Right.
[3206.36 → 3211.26] And I'm wondering now if the playing field has changed.
[3211.26 → 3211.62] Right.
[3211.70 → 3216.04] Because you can't just go to a bootcamp or at least from where I'm sitting.
[3216.40 → 3218.54] And again, I'm not knocking boot camps or things like it.
[3218.54 → 3228.96] Because I'm just thinking that it's that much harder now for somebody who's coming out of a bootcamp with no real world experience, right, to get a job.
[3229.06 → 3229.18] Right.
[3229.32 → 3230.60] Well, that's the thing.
[3230.60 → 3244.16] The people I have seen most successful out of boot camps are the people who spent eight years doing something, almost anything else, and then decided to switch and went to bootcamp to learn the skills necessary to make that switch into software engineering.
[3244.16 → 3258.08] The people who go to a bootcamp thinking they're going to learn everything they need to do, but they've never worked a day in their life and don't know even how to attend a meeting or have a useful conversation about what needs to be done.
[3258.76 → 3262.16] Those people aren't successful out of boot camps.
[3262.48 → 3263.62] I've seen some of both.
[3264.46 → 3265.12] I'd agree with that.
[3265.12 → 3270.10] I mean, does that mean to the software developer that it can be learned like anybody could do it?
[3270.24 → 3273.60] Or is it like you got it, or you don't get it?
[3273.92 → 3274.80] I don't agree with that.
[3275.34 → 3277.48] I think it's definitely a scale.
[3277.74 → 3277.86] Yeah.
[3277.96 → 3278.66] Degrees, right?
[3278.96 → 3279.32] Shades.
[3279.52 → 3279.88] Yeah.
[3280.44 → 3283.00] I don't think that there's a line where you draw the line and say.
[3284.54 → 3286.06] I didn't even have my thumb out.
[3286.06 → 3288.04] I don't think Ken.
[3288.76 → 3295.06] Sorry, for those of you guys who can't see, but for some reason a thumb appeared in front of Ken's face, and it was a down thumb.
[3295.22 → 3295.58] And I was like.
[3297.08 → 3297.84] That was weird.
[3299.36 → 3300.28] So what was I saying?
[3300.50 → 3303.40] About the degrees of like, like either you got it or you don't have it.
[3303.60 → 3303.74] Right.
[3304.18 → 3306.14] Sounds like you want to create a new principle.
[3306.28 → 3307.10] You're your principle.
[3307.30 → 3308.36] You don't.
[3309.94 → 3310.34] Right.
[3310.74 → 3315.50] No, I don't believe there's a line that he's like, nope, you go, you don't.
[3315.50 → 3317.36] I believe that I'm not a runner.
[3317.72 → 3319.86] I have tried at various points.
[3320.22 → 3321.34] Could I get better at running?
[3321.50 → 3321.90] Absolutely.
[3322.66 → 3324.20] But I'm a funny shaped.
[3324.20 → 3327.14] I'm a peasant stock and I don't run.
[3327.42 → 3330.88] I'll walk all day, and I'm strong at the plow, but I'm not going to be a runner.
[3331.36 → 3336.78] I think it's that same kind of like if you want it, and you enjoy it, even if you're not naturally quote unquote gifted.
[3337.46 → 3338.86] Yeah, you can make that work.
[3339.02 → 3340.48] I've bumped into plenty of those people.
[3340.48 → 3347.12] And largely those people who are successful, again, are the ones that have done, have industry knowledge or something else to bring to the table.
[3347.12 → 3351.02] But yeah, then there's people that I've met who are just naturally gifted.
[3351.28 → 3353.44] They just see things in code.
[3353.44 → 3364.46] And those people aren't the be all end all either because I've worked with enough of that type that it's like, are they 10x developers or do they just write 10 times the code that nobody else can work with?
[3365.16 → 3365.44] Okay.
[3365.58 → 3367.34] I went way off into the weeds on that one.
[3367.40 → 3367.66] I'm sorry.
[3368.70 → 3370.04] This is what this is for.
[3370.28 → 3370.86] Let it out.
[3371.12 → 3371.52] Let it out.
[3372.48 → 3373.58] This is therapy.
[3374.12 → 3374.72] This is therapy.
[3374.72 → 3378.72] Good, because my therapist doesn't really want to hear me rant about it.
[3380.66 → 3381.06] What?
[3381.18 → 3382.04] Even if you paid him?
[3383.36 → 3383.90] Oh, my gosh.
[3383.90 → 3384.36] I'm bad.
[3384.48 → 3386.30] Listen, I'm going to say a lot of words.
[3386.40 → 3388.18] You may not understand half of them, right?
[3388.54 → 3389.26] But...
[3389.26 → 3390.60] Womb womb womb AI.
[3390.94 → 3391.84] Womb womb womb womb womb.
[3392.84 → 3393.28] Microservices.
[3393.58 → 3394.64] Womb womb womb womb womb.
[3394.92 → 3395.72] You know, like...
[3397.72 → 3399.06] Oh, man.
[3399.70 → 3399.96] Okay.
[3399.96 → 3403.40] So before we transition to Unions, right?
[3403.40 → 3407.84] Any parting advice for old timers like us?
[3408.60 → 3409.32] For old timers?
[3409.64 → 3410.68] You don't like that term?
[3411.06 → 3411.96] Steve's like...
[3411.96 → 3415.04] Stop lumping me in.
[3417.18 → 3418.18] So I got one.
[3418.28 → 3418.76] Oh, gosh.
[3418.86 → 3419.76] You go first, Keith.
[3420.22 → 3421.04] Oh, I was just going to say.
[3421.12 → 3422.60] I mean, it's not just for old timers.
[3422.66 → 3423.38] I think it's for everybody.
[3423.62 → 3426.52] You know, the skill to have is to always be able to adapt.
[3427.38 → 3429.14] You know, everything's going to change.
[3429.40 → 3430.22] It's just...
[3430.22 → 3431.00] That's the constant.
[3431.00 → 3435.64] And as long as you can continue to face up to the new tech or something that's different
[3435.64 → 3439.96] and be able to adapt to it without dealing with it, I think you'll be okay.
[3439.96 → 3446.84] I think what I was going to add there is, I mean, I've done the full pendulum from senior
[3446.84 → 3449.60] management to individual contributor.
[3450.02 → 3453.62] And a few years ago, I swung hard back to IC.
[3454.42 → 3459.14] And I never really let my coding fingers get decayed.
[3459.30 → 3462.12] But, you know, I can be a strong contributor.
[3462.88 → 3464.22] You can come back from management.
[3464.72 → 3467.12] Management doesn't have to be a permanent part of your career, does I guess what I'm saying
[3467.12 → 3470.80] is as you grow, you can move into management, you can experiment with management, you can
[3470.80 → 3471.84] move back out of it again.
[3471.96 → 3473.38] And that's just fine.
[3474.58 → 3481.20] And you shouldn't feel like, oh, the only way up in my career is to, you know, become
[3481.20 → 3483.22] an executive if that's not the thing you love.
[3483.32 → 3487.26] And for me, it turns out that I love writing code a lot more than I love managing
[3487.26 → 3487.60] people.
[3487.60 → 3490.82] I like both, but the code part is more fun.
[3491.74 → 3493.98] Oh, so people are age.
[3494.24 → 3498.32] If you haven't been contributing to your 401k, throw money at that right now.
[3498.32 → 3499.02] You're screwed.
[3499.46 → 3500.06] You're screwed.
[3501.58 → 3501.98] Yeah.
[3504.02 → 3509.34] Seriously, the hardest thing I think as you become a developer who's got more than a couple
[3509.34 → 3511.46] years under your belt is how to unlearn.
[3511.46 → 3516.60] There are patterns that I have carried around with me in a suitcase because they worked for
[3516.60 → 3517.66] me 20 years ago.
[3518.30 → 3521.76] And I keep doing it a certain way because it still works.
[3522.26 → 3527.60] It's just I never thought to question why until somebody always more junior than me says,
[3527.74 → 3529.36] why do you do that?
[3529.66 → 3533.30] And it's like, oh, yeah, that was two languages ago.
[3533.34 → 3534.14] I don't need to do that.
[3536.30 → 3538.34] So, you know, be humble.
[3538.34 → 3542.60] Don't be afraid to let go of some long and green habits.
[3542.86 → 3545.60] And especially before AI starts sucking them up, and they start recycling.
[3546.30 → 3549.22] But bootstrap called it once it's webbed.
[3553.86 → 3555.66] It wants its dollar sign back.
[3556.58 → 3556.82] Yeah.
[3558.94 → 3559.90] Oh, man.
[3560.70 → 3562.62] jQuery, bootstrap.
[3562.88 → 3568.08] That was the back in the day, you know, just like every new project, you know.
[3568.52 → 3570.86] Started with just things, you know, building blocks.
[3571.50 → 3572.20] Lodash, man.
[3572.30 → 3572.90] Oh, Lodash.
[3573.08 → 3574.82] Lodash is still cool, isn't it?
[3578.46 → 3579.28] Sure can't.
[3581.68 → 3584.72] That was like 166 frameworks ago.
[3588.12 → 3589.48] Two dozen frameworks ago.
[3589.48 → 3591.68] I don't worry about seeing whether it's in the language.
[3591.86 → 3592.76] I just use Lodash.
[3592.76 → 3595.94] You just use it.
[3596.48 → 3603.24] Well, my advice would be, you know, it continues to be maybe I'm just stubborn.
[3603.50 → 3604.02] I don't know.
[3604.18 → 3605.14] I'd like to think not.
[3605.28 → 3610.34] I'd like to think I try to stay on top of things and can spot trends and whatnot.
[3610.34 → 3621.34] But one thing that has sort of cut through any hype cycle for me has been the principle of sort of being a T-shaped developer.
[3621.90 → 3622.02] Right.
[3622.50 → 3627.14] Be a sort of knowledgeable in a lot of different things.
[3627.20 → 3628.06] Be a generalist.
[3628.14 → 3628.32] Right.
[3628.48 → 3629.32] Even if you have.
[3629.64 → 3634.56] But have one strong, like your master of one.
[3634.90 → 3635.18] Right.
[3635.18 → 3636.44] What's that old saying?
[3637.82 → 3638.76] Master of one.
[3639.46 → 3640.12] Jack of all trades.
[3640.24 → 3640.68] Jack of all.
[3640.72 → 3640.94] Yeah.
[3641.02 → 3641.68] Jack of all trades.
[3641.82 → 3642.30] Master of.
[3642.48 → 3644.42] I think the joke is master of none.
[3644.64 → 3644.66] Right.
[3644.76 → 3644.92] Right.
[3644.94 → 3646.88] But the actual saying is master of one.
[3647.14 → 3647.36] Right.
[3647.60 → 3649.78] So I've tried to sort of live that.
[3649.84 → 3650.04] Right.
[3650.12 → 3651.92] By being very good at one thing.
[3652.08 → 3655.44] And contrary to popular belief, my one thing is not gone.
[3655.82 → 3656.08] Right.
[3656.16 → 3656.92] I love to go.
[3657.00 → 3658.34] I write go every single day.
[3658.62 → 3660.02] But my one thing.
[3660.08 → 3660.38] Right.
[3660.38 → 3664.84] Is being able to build like a solution based in the cloud.
[3665.30 → 3665.44] Right.
[3665.52 → 3667.84] And whatever language I have to use, whatever thing I have to do.
[3667.92 → 3669.52] Like that's my that's my thing.
[3669.78 → 3669.98] Right.
[3670.30 → 3673.42] So and I use and I happen to be using go.
[3673.54 → 3674.52] That's my favourite language.
[3674.52 → 3678.06] So where whatever opportunity I can get to use it, it has never let me down.
[3678.14 → 3678.84] So I will use that.
[3678.90 → 3680.24] But develop.
[3680.38 → 3680.80] Right.
[3680.98 → 3683.96] Your generalist set of skills.
[3684.30 → 3684.62] Right.
[3685.22 → 3689.48] And if you want AI to be your one thing, then be about it.
[3689.50 → 3690.38] It's fertile ground.
[3690.38 → 3692.50] There are all kinds of ways you can come at this.
[3692.64 → 3692.72] Right.
[3692.72 → 3702.46] Whether you want to be involved in model training or you want to be in fine-tuning, or you want to be a researcher, or you want to be the people that use it to build things.
[3702.46 → 3702.72] Right.
[3703.76 → 3706.66] Find whatever side of it you want and dive deep.
[3707.04 → 3712.28] But don't neglect everything else, because at some point, Gen AI or whatever incarnation.
[3712.28 → 3712.76] Right.
[3712.80 → 3715.94] That AI goes through for the regular everyday person.
[3716.30 → 3719.58] The hype is going to die down and have to make no mistake.
[3719.84 → 3721.88] The high brand AI will die down eventually.
[3721.88 → 3723.42] As with all hype.
[3723.42 → 3723.94] Right.
[3724.34 → 3732.76] When the dust settles and maybe, you know, what we consider new and innovative technology today becomes simply part of life.
[3732.76 → 3733.18] Right.
[3733.24 → 3735.36] Simply becomes part of the way things are built.
[3735.62 → 3735.78] Right.
[3735.78 → 3737.54] The next hype is going to come.
[3738.42 → 3746.10] But your ability to connect with people, your ability to understand business problems and to translate.
[3746.52 → 3746.84] Right.
[3746.90 → 3749.32] Whatever tool you're using, be it AI or something else.
[3749.32 → 3749.52] Right.
[3749.52 → 3754.42] To translate these things into actual working code and solutions.
[3754.94 → 3759.32] However much AI you want to use in the production of that solution is up to you.
[3759.32 → 3759.62] Right.
[3759.94 → 3767.98] But knowing how to translate human problems into working solutions, however much code is involved in that.
[3768.06 → 3768.22] Right.
[3768.52 → 3771.32] That skill set right there never goes out of style.
[3771.32 → 3775.92] So whatever you must do to maintain that sharp edge.
[3776.50 → 3777.68] That's my advice.
[3778.30 → 3778.48] Right.
[3779.46 → 3780.84] I think it's time for Unions.
[3780.96 → 3782.24] Let me play the tune.
[3782.24 → 3791.74] Unpopular opinion.
[3800.74 → 3803.16] You know the drill I want.
[3803.24 → 3804.34] Well, maybe you don't know the drill.
[3804.34 → 3811.14] So for those who don't know, for those who are listening for the show for the first time, because the title caught your attention.
[3811.14 → 3814.00] First, welcome to go time.
[3814.44 → 3817.68] But the way this works is that you can have a spicy take on anything you want.
[3817.78 → 3818.76] It doesn't have to be tech related.
[3819.36 → 3819.48] Right.
[3819.72 → 3823.80] So my guests here were tasked with bringing some spicy Unions.
[3824.02 → 3824.98] Who wants to go first?
[3826.20 → 3827.50] Don't let me start calling out people.
[3828.56 → 3829.12] All right.
[3829.66 → 3830.18] All right.
[3830.52 → 3831.04] I'll go.
[3831.04 → 3831.56] I'll get out of the way.
[3832.14 → 3833.66] And this is going to probably get me kicked off.
[3834.48 → 3834.90] It's fine.
[3834.96 → 3835.38] We're at the end.
[3836.38 → 3836.74] Okay.
[3837.20 → 3837.46] Cool.
[3838.14 → 3839.20] I love Go.
[3839.20 → 3841.28] I try to use it as much as possible.
[3841.48 → 3841.72] Careful.
[3843.82 → 3845.14] Careful what you say next.
[3848.32 → 3850.90] But yes, it's great.
[3851.26 → 3851.64] Go is great.
[3852.00 → 3858.80] But if I'm doing web development, I'm going to go for Laravel on top of PHP almost every time.
[3859.20 → 3859.26] Spicy.
[3859.26 → 3860.32] Listen, listen.
[3860.50 → 3871.18] Have you heard of our new saviour and like HTMX, HTMX, Go plus HTMX and Temple or some other thing?
[3871.42 → 3873.18] Like, yeah, it's the new hotness.
[3873.64 → 3874.80] Have you heard the good news?
[3874.86 → 3875.70] It's the new hotness.
[3875.92 → 3877.36] So you should give it another try.
[3877.86 → 3880.42] So I forgive you for such blasphemy on Go time.
[3880.42 → 3885.54] All right.
[3886.34 → 3887.40] I'll give you another five years.
[3887.46 → 3887.88] You'll catch up.
[3888.02 → 3888.04] Oh.
[3891.68 → 3892.04] Wow.
[3892.58 → 3892.98] Okay.
[3893.10 → 3893.42] All right.
[3893.42 → 3894.06] All right, Steve.
[3894.06 → 3895.80] And now Kent's going to open up a repo this weekend.
[3897.42 → 3899.04] The language coming in hot.
[3903.04 → 3904.82] That wasn't my unpopular opinion, though.
[3904.82 → 3913.62] This won't surprise any of you here, but my unpopular opinion is that cryptocurrency is worthless.
[3914.30 → 3921.72] Having spent two years doing it, I came away convinced in trying to create what we were thinking of was or what I was thinking of was going to be the ethical cryptocurrency.
[3921.72 → 3932.72] I came away with the conclusion that pretty much everyone in cryptocurrency is either a crook or an opportunist who wants to take advantage of the crooks or hopelessly naive.
[3932.72 → 3936.94] And, you know, not paying attention to what's actually going on.
[3937.12 → 3941.04] There is no useful use case for cryptocurrency still.
[3941.22 → 3948.94] All these three years later, Web3 is a disaster and blockchains are not useful tech.
[3949.48 → 3950.40] And so, yeah.
[3950.96 → 3951.92] You can't.
[3952.04 → 3953.10] Did you create an s*** coin?
[3953.48 → 3953.78] Yes.
[3954.34 → 3955.12] I mean, essentially.
[3956.64 → 3957.20] No.
[3958.12 → 3960.48] There were those who would have called it an s*** coin.
[3960.48 → 3965.72] It wasn't based on, you know, it was a new tech s*** coin, but it was still an s*** coin.
[3966.12 → 3966.32] Yes.
[3968.96 → 3969.66] Oh, man.
[3972.48 → 3973.50] I ran away screaming.
[3973.72 → 3973.92] Oh, beautiful.
[3974.02 → 3981.82] Well, I don't think that's as unpopular opinion as you might have thought it was or if you had said that, like, I don't know, three years ago or four or five years ago.
[3982.02 → 3982.38] That's true.
[3982.48 → 3984.58] It's more popular than it used to be, I guess.
[3985.36 → 3986.26] Just ask SPF.
[3986.26 → 3990.86] Your unpopular opinion is gaining popularity, which is how it should go.
[3991.40 → 4001.98] My unpopular opinion is that single letter variables outside a loop should just be omitted, shot on site, dragged out with the trash, shot from space.
[4002.72 → 4002.82] Yeah.
[4003.26 → 4005.40] I feel like you're talking to me again.
[4005.40 → 4009.16] I am definitely calling out every Google offer.
[4012.32 → 4013.38] Oh, man.
[4013.40 → 4018.70] I'm not team, like, like, java file with, like, you know, a paragraph name either.
[4019.18 → 4022.44] I think there's room somewhere in the middle, you know, just like.
[4022.44 → 4025.56] You came on a Go podcast with guns blazing.
[4028.46 → 4030.58] And I will live and die by it.
[4030.68 → 4030.94] Sorry.
[4030.94 → 4033.18] Oh, man.
[4033.36 → 4033.84] All right.
[4033.92 → 4034.30] All right.
[4034.34 → 4034.70] Cool.
[4034.78 → 4034.98] Cool.
[4035.06 → 4036.06] You guys couldn't convince me.
[4036.10 → 4036.88] Nobody's going to.
[4037.04 → 4037.44] Sure.
[4038.24 → 4038.78] Do you?
[4040.12 → 4040.90] Oh, man.
[4041.08 → 4041.44] Yeah.
[4041.64 → 4042.62] Like, definitely.
[4043.52 → 4045.06] All of us on this call.
[4045.66 → 4046.10] Like, some of you.
[4046.32 → 4048.58] Sharon, I'm not sure if you've done a ton of Go recently.
[4048.58 → 4052.54] But, yeah, at least, you know, Kent and Steve and me.
[4052.96 → 4053.92] Take what you say to heart.
[4057.40 → 4058.10] We do.
[4058.22 → 4058.52] We do.
[4058.64 → 4058.80] We do.
[4058.80 → 4059.22] Sure you do.
[4059.22 → 4065.22] I just had a conversation today with one of my teammates about naming return variables,
[4065.96 → 4067.64] which is its own little spicy Go take.
[4068.28 → 4069.68] Hey, that's actually.
[4069.84 → 4075.44] Well, Kent, why don't you spice up the whole return variable conversation?
[4075.44 → 4083.76] So, so Go allows you to have, when you have a function signature, you, you know, normally,
[4084.10 → 4087.96] it'd be idiomatic Go simply names the types of the things that you're returning.
[4088.44 → 4092.38] For normal functions, you return one thing, and it doesn't really matter, but you can return
[4092.38 → 4093.38] multiple values.
[4093.38 → 4097.46] And if you're returning more than one of the same type, then it can get confusing as to,
[4097.54 → 4102.12] like, if your function is trying to return, you know, a book and an error, then you can't
[4102.12 → 4102.82] really mix those up.
[4102.86 → 4108.38] But if you're returning two books, then you might want to give them both names, which you
[4108.38 → 4109.06] can do in Go.
[4109.18 → 4111.38] But doing so implicitly defines them.
[4111.38 → 4114.62] And then they have values, and they get the default zero value.
[4114.86 → 4119.14] And then you can return without decorating the return with the values you're returning,
[4119.40 → 4121.84] which seems to be an antipattern.
[4122.04 → 4127.04] Using blank returns with named return variables is probably not a great pattern, but using blank
[4127.04 → 4131.18] returns with named return variables or non-blank returns with named return variables, you can
[4131.18 → 4134.10] do, you can return X, Y, and that's fine.
[4134.58 → 4139.54] Naming them can be helpful when you're like hovering over them in an editor and shows you what
[4139.54 → 4140.06] they mean.
[4140.06 → 4143.20] And again, if they're different types, it's probably not that big a deal.
[4143.58 → 4145.48] If they're the same type, you probably want to name them.
[4145.98 → 4150.98] But this particular developer was like, I just want to not call this not error, but some
[4150.98 → 4152.98] particular type of, you know, named error.
[4153.22 → 4156.66] And that was maybe I didn't think as helpful as it could have been.
[4157.28 → 4166.34] When I teach Go, I always advise strongly against named return variables and their subsequent
[4166.34 → 4167.42] naked returns.
[4167.42 → 4172.32] Like it is, I think, I'm not sure why the design of the language allowed for that.
[4173.40 → 4180.32] And very, very, I'm not saying I've never seen a good use of it, but it's very rare in my,
[4180.40 → 4181.68] in my, in my opinion.
[4181.68 → 4183.62] Naked returns is the biggest problem.
[4184.00 → 4184.98] And that I think you should avoid.
[4185.06 → 4185.22] Yeah.
[4185.34 → 4185.66] Yeah.
[4185.66 → 4187.18] You should, you should, you should avoid that.
[4187.52 → 4190.54] But the question, the question is, is the AI going to suggest one or the other?
[4192.84 → 4193.74] No, but here's the thing.
[4193.76 → 4197.62] You can always tell it, Hey, do not use naked returns, and it'll give you new code.
[4197.62 → 4197.88] Right.
[4197.92 → 4199.58] Again, you have to know what the right question is to ask.
[4199.64 → 4201.34] You have to know what a naked return is in the first place.
[4201.34 → 4201.56] Right.
[4202.86 → 4203.14] Right.
[4203.24 → 4203.42] Right.
[4203.42 → 4208.64] But actually this is a along the same lines of when initializing structs, if you have,
[4208.68 → 4210.92] you know, multiple fields of the same type, right.
[4211.00 → 4214.46] Do not use the positional way of initializing your structs.
[4214.72 → 4216.36] I always use key value pairs.
[4216.54 → 4216.92] Right.
[4216.96 → 4220.74] Cause if you have two things that are a string, and you change the position of the strings,
[4220.74 → 4223.14] all of a sudden you think you're initializing one thing, but you initialize on the other
[4223.14 → 4223.38] thing.
[4223.38 → 4229.02] So yeah, always use, you know, key value pairs when initializing your structs, not the positional
[4229.02 → 4229.36] arguments.
[4229.88 → 4230.28] Yeah.
[4230.34 → 4234.42] So onto my on pop has nothing to do with tech or anything like that.
[4234.86 → 4241.46] I think if you are on YouTube, if you're a YouTube influencer peddling, actually, this
[4241.46 → 4243.50] is actually going to be a, I have two on pops.
[4243.64 → 4244.42] So here's the first one.
[4244.50 → 4245.32] Here's the first one.
[4245.54 → 4247.10] One actually led to the other.
[4247.40 → 4247.90] Here is.
[4247.98 → 4248.28] Hang on.
[4248.34 → 4250.60] I got to take another drink of my, my scotch.
[4251.22 → 4252.28] Well, I'll unleash this one.
[4252.28 → 4253.66] All right.
[4253.66 → 4254.26] Here's the first one.
[4254.50 → 4259.18] If you are a YouTube influencer peddling AI fear, right?
[4259.26 → 4262.86] I think you should reevaluate your life choices because you, you are, you are part of the
[4262.86 → 4263.30] problem.
[4264.88 → 4267.38] What kind of AI fear are we talking about?
[4267.48 → 4271.58] No, it's going to take our, it's going to take our jobs and, and oh my God, you better,
[4271.72 → 4273.40] you better, you know, you better run for it.
[4273.40 → 4276.38] He says as we kind of profited off of it with our clickbait title.
[4276.44 → 4277.04] Right, right.
[4277.40 → 4278.60] Clicks and views, right?
[4278.70 → 4279.46] Like first in the time.
[4279.86 → 4280.96] We use our powers for good.
[4281.18 → 4281.58] No, no.
[4281.58 → 4281.96] Yeah, of course.
[4281.96 → 4282.48] Of course.
[4282.58 → 4285.68] Like first thing they tell you, like, and subscribe, you know, and hit that bell icon
[4285.68 → 4287.74] so you don't miss the next, the next rant.
[4287.88 → 4288.06] Right.
[4288.20 → 4297.06] So, so yeah, if you are, if you are one, one such, such influencer, you know, I'll take
[4297.06 → 4297.26] it back.
[4297.34 → 4303.84] You don't have to reevaluate your life choices, but I would ask you to not continue to propagandize,
[4303.84 → 4304.44] right?
[4304.44 → 4310.78] AI, what you can do better is to help people level up to help people meet the new challenge
[4310.78 → 4313.44] that this new innovation and technology is bringing.
[4313.64 → 4315.98] Cause at the end of the day, I think it's a net positive, right?
[4316.38 → 4317.82] It's transformative technology.
[4317.82 → 4322.80] I'm sure when farmers saw their, their industry being industrialized with machinery and everything
[4322.80 → 4327.36] else, I'm sure some had the same sort of gut reaction and knee-jerk reaction of, you know,
[4327.36 → 4328.40] trying to push back on that.
[4328.44 → 4328.60] Right.
[4328.60 → 4330.30] So this is just another innovation cycle.
[4330.30 → 4336.70] And all we have to do is, well, may not be simple or easy, but we have to level up, right?
[4336.70 → 4340.80] As professionals, um, and meet the new, the new stage, uh, that we're playing on.
[4340.92 → 4341.12] Right.
[4341.54 → 4342.44] So that's my first UNPO.
[4342.68 → 4347.38] The second UNPO has nothing to do with tech, but rather it has to do with the fitness industry.
[4347.78 → 4349.70] So I've been on a fitness journey.
[4351.64 → 4353.48] I've been on a fitness journey for a little while.
[4354.00 → 4359.12] And, uh, and, and as with all things, whenever I don't know much about, you know, things, I don't
[4359.12 → 4359.86] know much about fit.
[4359.92 → 4361.56] I didn't know much about fitness like a year ago.
[4361.56 → 4365.72] And then I went to YouTube and started, you know, Googling, you know, things and then
[4365.72 → 4371.18] found, found fitness YouTube and lots of influencers, you know, peddling lots of different
[4371.18 → 4373.82] things and approaches and do this exercise.
[4373.92 → 4374.64] Don't do that exercise.
[4374.92 → 4379.06] Like, so, and there's, there's a lot, there's a lot of stuff out there.
[4379.06 → 4383.62] You all I'll tell you, I'll tell you this much, but one thing I've noticed, uh, or rather
[4383.62 → 4389.04] my unpopular opinion is that if you are going into this world, right, a fitness
[4389.04 → 4392.68] YouTube, avoid any influencer, right.
[4392.74 → 4397.26] That is telling you, this is what you can do for, for specifically for your abs.
[4398.26 → 4406.32] Cause there is no such thing as spot reduction of just one area of your body.
[4406.56 → 4407.94] That is not a thing.
[4408.22 → 4408.36] All right.
[4408.76 → 4409.78] You can't work.
[4410.00 → 4413.32] You can't be walking around a six-pack abs with the rest of your body.
[4413.32 → 4415.00] You just, you know, all loose and loose.
[4415.08 → 4415.86] That's not a thing.
[4416.30 → 4416.62] Yeah.
[4417.32 → 4418.96] That's not a thing.
[4419.04 → 4419.42] That's not a thing.
[4419.50 → 4422.72] The body loses weight and proportion and everything works together.
[4423.04 → 4423.98] So, uh, yeah.
[4424.04 → 4428.62] Find yourself some reputable, hopefully people with, you know, like some kind of good
[4428.62 → 4429.40] knowledge, right.
[4429.44 → 4434.30] Some sort of a credential ideally that can give you decent advice.
[4434.76 → 4438.10] Um, it might take you a little while to find, you know, the good ones, but they're out
[4438.10 → 4438.34] there.
[4438.34 → 4442.00] So if that's your, if that's your journey, if you're on a similar journey as me, do a
[4442.00 → 4445.02] little bit of work, do a little bit of research, and you'll find, you'll find the good ones.
[4445.12 → 4448.20] So some stuff is going to sound outlandish and if it sounds outlandish, it's probably
[4448.20 → 4448.88] is.
[4449.06 → 4449.20] Right.
[4449.96 → 4451.74] So watch out there.
[4451.76 → 4454.28] There's a lot of woo and hype in that space.
[4454.44 → 4454.80] Oh yeah.
[4454.86 → 4455.78] Find the ones that aren't either.
[4455.92 → 4456.32] Oh yeah.
[4456.54 → 4456.90] Oh yeah.
[4457.36 → 4457.68] Indeed.
[4457.68 → 4458.50] And it never ends.
[4458.72 → 4460.00] It doesn't follow the hype cycle.
[4460.12 → 4460.50] It never ends.
[4460.62 → 4461.14] Non-stop.
[4461.54 → 4462.10] Non-stop.
[4462.66 → 4463.30] It's non-stop.
[4463.44 → 4464.02] It really is.
[4464.10 → 4464.58] It really is.
[4464.58 → 4468.00] The whole fitness and diet industry, that is fertile ground.
[4468.10 → 4469.46] That is evergreen territory.
[4470.08 → 4473.36] Like, you know, I think I might start a YouTube channel on fitness tomorrow because, you know,
[4473.40 → 4476.66] I'll probably get, I'll probably get subscribers, subscribers and views.
[4476.82 → 4478.04] Using AI and fitness.
[4478.58 → 4480.02] Damn it.
[4480.34 → 4481.46] Using AI and fitness.
[4481.80 → 4482.58] Here I come.
[4483.16 → 4483.66] Here I come.
[4484.06 → 4485.42] This was awesome.
[4485.70 → 4491.42] And again, we don't disappoint when we get on these rent filled, rent filled sessions.
[4491.42 → 4492.98] Now you're wondering what we didn't say.
[4492.98 → 4494.20] Well, we don't know, right?
[4494.54 → 4498.20] We have to keep this podcast still, you know, family friendly.
[4498.82 → 4499.02] Yeah.
[4499.76 → 4502.48] So, you know, but yeah, this was awesome.
[4502.68 → 4504.46] Thank you all for being here as usual.
[4504.90 → 4508.34] We'll chat again with each other and maybe not on a recorded session, but, you know, in
[4508.34 → 4509.16] a couple of weeks and whatnot.
[4509.34 → 4515.44] But yeah, this was fun letting the audience, mostly folks who listen to the podcast, you
[4515.44 → 4518.86] know, kind of get a peek into my world, you know, and what, you know, conversation
[4518.86 → 4519.72] with my friends look like.
[4520.14 → 4520.56] So yeah.
[4520.62 → 4521.68] Thanks you all for being here.
[4521.68 → 4523.76] Steve, Kent, Sharon, always a pleasure.
[4524.04 → 4524.46] It was fun.
[4524.66 → 4524.88] Thank you.
[4524.94 → 4525.24] Thank you.
[4525.40 → 4526.22] Catch you next time.
[4528.40 → 4529.28] All right.
[4529.56 → 4531.34] That is go time for this week.
[4531.76 → 4532.40] Thanks for listening.
[4533.08 → 4538.48] Thanks once again to our friends at fly.io to Break master Cylinder for beat freaking for
[4538.48 → 4540.26] us and to sentry.io.
[4540.60 → 4545.38] Save a hundred bucks off their team plan by using code changelog when you sign up.
[4545.76 → 4549.70] That's all for now, but we'll talk to you again next time on go time.
[4551.68 → 4552.04] Okay.
[4552.04 → 4554.08] So,
[4554.08 → 4561.28] we got a ton.
[4564.82 → 4570.90] Just like the K-9.
[4570.90 → 4571.58] Philips.
