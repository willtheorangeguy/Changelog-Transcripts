[0.00 → 26.74] And then the last thing I'll say, because I know this audience is probably deeply familiar with things like GPT-3 and a lot of the issues with natural language generation tech, is that there is a real need to build structure, safety, coherence, and memory into these systems before they can be deployed for any human-facing application, much less one that you're willing to put in front of young people.
[26.74 → 43.98] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted on Linde cloud servers. Head to linode.com slash Changelog.
[43.98 → 49.38] This episode is brought to you by DigitalOcean.
[49.82 → 66.58] Droplets, managed Kubernetes, managed databases, spaces, object storage, volume block storage, advanced networking like virtual private clouds and cloud firewalls, developer tooling like the robust API and CLI to make sure you can interact with your infrastructure the way you want to.
[66.58 → 83.82] DigitalOcean is designed for developers and built for businesses. Join over 150,000 businesses that develop, manage, and scale their applications with DigitalOcean. Head to do.co slash Changelog to get started with a $100 credit. Again, do.co slash Changelog.
[83.82 → 113.24] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone. This is where conversations around AI, machine learning, and data science happen. Join the community and Slack with us around various topics of the show at Changelog.com slash community and follow us on Twitter. We're at Practical AI FM.
[113.82 → 134.94] Welcome to another episode of the Practical AI podcast. We're going to explore today a lot of interesting things in AI in a little bit of a different way. My name is Chris Benson, and with me as always is Daniel Whiten ack, my co-host. How's it going today, Daniel?
[134.94 → 161.86] Oh, it's going great. Other than I woke up this morning, my computer, we had a power outage last night, so my training run abruptly ended at some point in the night. I'm not sure when. So getting that restarted, I guess I'm like learning this sort of things about having an AI workstation locally, whereas most of the time before I just ran stuff in the cloud. So, you know, upsides and downsides, I guess. But yeah.
[161.86 → 177.16] Sounds good. So yeah, I guess for listeners who have been tuning in for a while, there has been Daniel put to get built his own workstation for doing deep learning and has been going through the trials and tribulations. So I'm waiting till he has it all figured out before I try it myself.
[177.46 → 184.76] So that on some fully connected episode, we'll have to chat about fun that has been had through that process.
[184.76 → 189.44] So there you go. Kind of like everyone can learn from your pain on that one.
[190.36 → 191.78] Yes, yes, please do.
[192.30 → 207.48] Well, you know, today we have a bit of a different episode from the usual in that we have someone who's joined us who has done lots of interesting things in the past, which we'll hear about, as well as some things that she is currently engaged in.
[207.48 → 214.64] With us today is Hilary Mason, who is currently the co-founder at Hidden Door. Welcome to the show, Hilary.
[215.08 → 217.80] Thank you. I'm pretty excited to be joining you today.
[218.20 → 230.70] Well, thank you very much. Daniel and I have been familiar with your work for many years, because you've done a lot of stuff that is that within the context of the data science world has been very much in the public eye.
[230.70 → 243.66] And so we are really interested in finding out some of what you've done in the past, some of which our listeners may, those that are familiar with you, may already be familiar with, but also some of the cool stuff that you're doing now.
[244.00 → 253.82] I guess to start off with, would you just kind of give us a little bit of background about yourself, how you got into the field and, you know, highlight some of the stuff that you've done up till now?
[253.82 → 261.06] Sure. So first, that's really kind of you to say. And hopefully we'll talk about some things today that you aren't familiar with.
[261.32 → 262.62] Okay. Looking forward to it.
[263.10 → 271.82] Yeah. So I've been doing this for quite a long time, as you say, and I try to be very prolific, because if you do enough things, at least some of them are likely to be interesting.
[272.38 → 282.42] I started in computer science and machine learning over 20 years ago. It's been a long-term interest of mine. As a kid, I loved science fiction. I still do.
[283.82 → 309.88] I always love thinking about machines that could really be partners to us. And obviously, that wasn't entirely possible in the 90s. And I'd say that it's maybe just now becoming possible. But I started in academia, realized that, you know, I have several personality traits that make me a little bit of a mediocre academic, but I think a pretty good entrepreneur.
[309.88 → 316.78] That's pretty interesting. Could you, like, just give a bit of detail about that? I'm kind of interested.
[316.96 → 317.20] Sure.
[317.34 → 330.02] Because there are a lot of people that, you know, are maybe sitting in academia a bit disillusioned, or maybe they're, like, in industry, they don't know if they should, like, go do research or, you know, all of those things.
[330.02 → 350.36] Yeah. No, it's, and it's a hugely emotional process, whatever side of it you're on, to think about where you might go. And there's definitely, I have a lot of conversations with folks, even now, who are considering whether there are opportunities to use their academic skills in industry, if they'll find something that's nearly as intellectually fulfilling.
[350.36 → 368.36] So, yes, this is something I have a ton of empathy for, especially because I went through it. So, was a, you know, in a faculty role, the things that I was interested in, first in computer science, we still tend to give a little bit more status to theory work than we do to engineering work.
[368.36 → 397.20] But I really like to build things. And, you know, I can force myself to go through and do some proofs. And, you know, math is something that I have, I can get along with, and I do enjoy. But if you give me the choice between spending two weeks, you know, at a chalkboard thinking about math and spending two weeks at a whiteboard and at my keyboard actually trying to build it, I will always choose the latter. So that's one, you know, personality flaw of mine.
[397.20 → 426.16] And then another one is that I have a relatively short attention span, in the sense that, you know, as an academic researcher, I find that some of the best work requires a persistence over, you know, not just months, but over, you know, four, five, 10 years. And I tend to, you know, after one year, something has to change for me to continue to keep up that persistence and interest in it.
[426.16 → 433.28] So I have a relatively short attention span, I like to pay attention to a lot of different things at the same time and try to figure out where they connect.
[434.00 → 449.94] That's also something that, you know, is a real asset in data science, where you're often, you know, facing some sort of problem, you have certain technical tools that you understand certain data assets, maybe a product platform to build on top of.
[449.94 → 454.56] And you need to figure out how to pull all those pieces together in something that will work.
[454.84 → 458.30] And if you're doing it in a startup context, you need to do that quickly.
[458.62 → 461.94] You don't really have the luxury of a year to take the best approach.
[462.62 → 465.62] And so that's another personality trait that I have.
[465.64 → 468.84] And it's also something I look for when I hire folks out of academia.
[468.84 → 476.48] One of my favourite questions to ask is to lay out one of the technical challenges that we're working on and sort of say, how would you approach this?
[476.48 → 478.10] And usually they give a wonderful answer.
[478.22 → 478.84] And I say, great.
[478.92 → 480.94] Now, what if I told you had two weeks to build something?
[481.02 → 481.70] What would you do?
[482.12 → 484.34] And then that, you know, the sweat starts to pour down.
[484.46 → 486.44] And then I say, OK, now you've got two days.
[486.54 → 487.66] Like, what are you going to do?
[487.66 → 491.32] What is the stupid, simple thing you can pull together?
[491.88 → 501.24] And really looking for that kind of agility of thinking and being able to make decisions about where you're going to prioritize that simple thing versus the right thing.
[501.78 → 508.80] And I think, you know, part of that is that I am more of a hacker than I am a perfectionist.
[508.80 → 521.90] And again, these are just things that I've realized that I need to work with people who are perfectionists and who have that other sort of perspective on things because that way we end up building really great things.
[522.48 → 524.48] But those are my personality flaws.
[525.52 → 538.78] No, I yeah, I appreciate you going into detail there because I think there's those are a lot of things that people think internally, but they don't voice them a lot when they're going through that or like ask people like, hey, I feel like I'm going to do that.
[538.80 → 539.38] I feel this way.
[539.38 → 541.88] Like, you know, what where should I go?
[542.00 → 542.84] What should I do?
[543.16 → 547.94] A lot of times people just kind of struggle with that inwardly and don't really voice it.
[548.14 → 548.62] Yeah.
[548.74 → 556.92] And, you know, I spent so many years feeling like there was something wrong with me because I preferred to write code to write math, even though it is ultimately the same thing.
[556.92 → 559.24] And it's easy enough to go from code to math.
[559.24 → 568.62] I thought there was something, you know, wrong with me because I had these particular traits and preferences about the environments I'm working in.
[568.62 → 572.80] But I realized now that I've been doing this for 20 years is a long time.
[573.04 → 577.30] So as you were saying all that, you and I share a bunch of those same characteristics.
[578.44 → 587.84] I have, you know, over my career, I've also had the same thing where I've been like, you know, I'm feeling like I was doing it maybe not the best way in every case.
[587.84 → 595.60] But hearing you doing it and with the successes that you've had over the years, it kind of validated like, oh, maybe things aren't so bad after all.
[595.84 → 604.70] So I think it's a perfect message to get out there because I suspect that if you are, and I am probably quite a few other people out there are experiencing the same.
[604.92 → 605.38] I'm sure.
[605.38 → 606.20] That's great.
[606.50 → 607.70] I'm kind of curious.
[608.08 → 616.06] I know one of the of course, aspects that we've been talking about is kind of jumping into industry and building products and those sorts of things.
[616.06 → 622.42] But how did you get to the point where you really started getting this interest in like data science and data science products?
[622.42 → 623.32] How did that develop?
[623.96 → 625.70] Yeah, it's a good question.
[626.44 → 629.50] So I like I said, I started in academic machine learning.
[629.50 → 634.78] I have always been interested in using that as a tool to build useful things.
[635.38 → 638.50] But I actually learned the product lesson the hard way.
[638.76 → 641.24] So there's a bit of a longer story here.
[641.34 → 647.18] But the short version is that I, you know, left my academic position and came to work for a startup.
[647.86 → 653.92] And the startup at the time, we were building statistical models of career progressions off of millions of resumes.
[654.02 → 655.74] We crawled off the web.
[655.74 → 659.14] This was in 2007, 2008, I think.
[659.14 → 661.74] So it was something that was novel.
[662.28 → 667.18] It was not you couldn't go on LinkedIn and see that kind of analysis done for you.
[667.72 → 674.94] It was obviously something I had a personal need for because I was going through a career crisis myself at the time.
[675.62 → 679.24] And that company ended up failing in nine months.
[679.24 → 681.60] And it failed because of two things.
[681.60 → 688.38] One is that we built some beautiful data science models, put a UI on them, and nobody actually wanted to use them.
[688.38 → 697.82] And the second thing was that everybody thought a website about, you know, data about careers was meant for college students.
[697.82 → 704.74] But the whole idea here was that you could say, you know, okay, I'm a lawyer and I don't want to be a lawyer anymore.
[704.92 → 706.80] What do people like me go on to do?
[707.02 → 709.94] Or you could say, I'm a software engineer and I want to be a CEO.
[710.14 → 710.96] How do I get there?
[711.46 → 716.08] What are the career paths that other people who have made this transition have taken to get there?
[716.08 → 718.06] What are the stages they go through?
[718.14 → 719.44] What other fields do they explore?
[719.90 → 721.88] And college students, of course, have no data.
[722.42 → 724.62] So it actually didn't work for them at all.
[725.30 → 729.42] So there were some flawed business assumptions, some flawed product assumptions.
[730.02 → 731.78] And that was a wonderful lesson.
[731.78 → 744.54] And I learned it, thankfully, on, you know, somebody else's company and somebody else's money in that you really have to build a product that is useful to people, which, of course, sounds so obvious when you say it out loud.
[744.54 → 747.28] But it at least was not obvious to me at the time.
[747.28 → 764.46] And so I went from being primarily interested in the modelling to being primarily interested in building useful things and have spent quite a bit of time studying and practicing and trying to figure out how to do that in the intervening years.
[764.82 → 769.58] And so I'm curious, just to that point, how do you look at that now?
[769.62 → 773.20] Because that's always a hard thing for companies to do.
[773.20 → 782.86] It's, you know, regardless of the industry, people trying to figure out what their customers want and their needs and what do people actually want to use and are willing to commit to.
[783.06 → 785.90] How have you addressed that as you've learned that over the years?
[786.50 → 789.14] That could be, you know, a whole course.
[789.54 → 789.90] It sure could.
[789.90 → 791.54] There's a lot to talk about there.
[791.54 → 803.26] But I think the sort of principles of it are really to clearly identify the problem you're trying to solve and not rush to, like, try to get to the question.
[803.80 → 805.46] Don't rush to the answer.
[806.62 → 815.96] And then, you know, figure out the people who you're answering this question for and figure out what's actually useful to them.
[815.96 → 836.56] And this honestly is a mix of both quantitative analysis and qualitative analysis and really trying to have empathy for the people who you're trying to build for and understanding where this fits into their lives, which are always, you know, interesting and chaotic.
[836.56 → 849.48] And then it comes back to what we were actually talking about before, where you start to build the simple things that can start to potentially address the problem to understand if it's even worth investing in the best things.
[849.48 → 858.74] And so it really is a process that sort of merges the practice of product management and product design with the practice.
[858.96 → 870.24] If you're building something that depends on that, I would call a data product, which is something that really depends on some sort of data science or machine learning capability to build the core feature of the product.
[870.24 → 878.34] So something like a weather prediction, like, you know, Google Maps is always my favourite data product, the navigation stuff.
[878.52 → 882.78] These products could not exist without the underlying representation of the data.
[883.94 → 888.14] And so you're really trying to figure out what decisions are people making in what context?
[888.26 → 891.96] How do I get that information to them in that context so they make a better decision?
[891.96 → 899.92] How accurate, how good does it have to be for them to first get benefit from it, but then second, actually use it?
[900.24 → 907.72] You know if your weather predictor is 1% more accurate than another one, that's not a compelling reason for me to use it if the other ones more convenient.
[908.96 → 910.80] So really thinking about all of that.
[910.80 → 931.18] And one of the gaps I see broadly in our practice right now is that we often have product designers and product managers who are in the position to make the best decisions about the use of data science and machine learning in their products, but they don't have necessarily the background, the knowledge, the access to that talent or tools.
[931.82 → 935.20] They're certainly not going to build their own deep learning rig in their house.
[935.20 → 945.72] And then you have, on the other hand, your data scientists who often are not connected to the customers or to the ultimate, you know, people who will benefit from the work they're doing.
[946.40 → 964.46] And so I think there's, in our field of practice, there's actually a lot for us to figure out about, not just from a, you know, I'm a startup and I want to build something new point of view, but really, you know, from your day-to-day practice as somebody in this field, like, how do you think about doing this work in the organizational structure you're in?
[964.46 → 967.90] And I think it's kind of a mess right now, and that's a big opportunity for us.
[968.80 → 978.48] So I know you and I have met previously and have talked and stuff about business, and you have really become, you know, a powerhouse in developing entrepreneurial opportunities.
[978.82 → 981.36] But before we get too far past that, I am curious.
[981.84 → 983.88] I know, you know, I alluded to it in the beginning.
[983.88 → 991.44] We talked about the fact that our first awareness was when you were producing content and stuff and learning from you as students.
[991.44 → 999.00] And I'm kind of curious, how did you integrate teaching others your expertise, integrate that into your entrepreneurship?
[999.32 → 1000.44] Does it still have a role?
[1000.52 → 1001.96] Has that role evolved or changed?
[1002.12 → 1004.06] Was that just a step along the way?
[1004.28 → 1006.72] I'm just kind of curious about the development there.
[1007.20 → 1012.50] Yeah, it's a good question because I think people take a variety of approaches to this.
[1012.50 → 1019.26] And, you know, the honest truth is that I love teaching and I love talking to people.
[1019.60 → 1021.40] It's why I'm here this morning.
[1021.40 → 1028.58] And I also really like sharing opinions that are useful.
[1029.66 → 1033.18] And the company I founded about six years ago is called Fast Forward Labs.
[1033.36 → 1037.36] And, you know, we met at the Fast Forward Labs office a while back.
[1037.68 → 1044.06] That company was built on the idea of doing independent applied research and sharing as much of it as possible.
[1044.58 → 1049.70] But it's not the sharing piece is not exclusive to my work at Fast Forward Labs.
[1049.70 → 1059.74] It's been a thread through, you know, all the different data science jobs or management jobs I've had or things I've gotten involved in.
[1059.74 → 1069.80] And so I think it's really important in this field to talk about what we do and what works and more importantly, what doesn't work.
[1070.24 → 1072.80] Because the field is so young.
[1073.10 → 1078.86] Like people have only been able to get a degree in data science for maybe four or five years.
[1078.86 → 1080.70] And that still astounds me.
[1080.84 → 1084.56] The fact that you could have a job with that title has been a thing for about a decade.
[1085.36 → 1087.92] There's a lot for us still to figure out.
[1088.06 → 1089.86] And that's why I love it, by the way.
[1090.08 → 1092.02] It is not a solved problem.
[1092.90 → 1096.24] And our technology is also not a solved problem.
[1096.72 → 1097.82] It is really weird.
[1097.82 → 1110.86] So if you look at the change in capabilities of machine learning technology and how you have to manage using them and investing in them, it is completely different from most technologies that folks are familiar with.
[1111.02 → 1116.94] And yet we tend to shoehorn it into existing structures and processes that come from software engineering.
[1116.94 → 1126.20] And so when I talk about the stuff I like to work on, for one thing, I'd say it's a two-directional exchange.
[1126.50 → 1133.22] One is that I and the teams I've been fortunate enough to work with, we try to have a unique or our own point of view.
[1133.22 → 1143.50] And we try to be, and this is really something I can't help, honestly, but deeply pragmatic about what something is, how it works, where we think it's useful.
[1144.40 → 1148.80] This is really important in AI and machine learning because there is so much hype.
[1149.50 → 1150.70] There is so much salesmanship.
[1150.70 → 1158.56] There is so much marketing that is designed to get people who don't themselves have a deep expertise to believe something that's not quite true.
[1159.16 → 1164.10] And because the tech is weird and changing so quickly, it's very easy to believe that stuff.
[1164.56 → 1173.12] And so it's really important, if I can say this, as a technologist to have those pragmatic points of view and then share them where you can.
[1173.12 → 1181.22] Because we need to build a consensus in the community around what is possible, what isn't, the best ways to approach certain kinds of problems.
[1182.04 → 1183.86] And we only do that by sharing.
[1183.98 → 1191.78] The other thing I'll say is that I love working in the data science community because the more that you succeed, the more I succeed.
[1192.32 → 1195.04] We are not directly competing with each other.
[1195.04 → 1201.74] And for the most part, if we're data scientists, or we're machine learning engineers at different companies, I can help you out.
[1201.74 → 1203.96] I can hear about what you're working on.
[1204.02 → 1205.22] I can share what I'm working on.
[1205.28 → 1206.46] We can give each other feedback.
[1207.28 → 1214.16] And within a certain ecosystem, the more one company succeeds, the more another is likely to as well.
[1214.74 → 1224.08] This is really different from if you ever have had the, well, I don't want to be unkind, but if you've ever hung out with a bunch of hedge fund quants.
[1224.42 → 1228.86] I live in New York City, so occasionally I end up, well, not anymore, but I used to end up at those events.
[1228.86 → 1236.52] These folks talk about the weather and about sports because they do work in a community where there is a significant competitive dynamic.
[1237.44 → 1244.32] So I think that one of the things I really appreciate is the ability to share and having that actually be supportive for all of us.
[1244.72 → 1248.76] And then I'll also say it's worth sharing because you will get feedback.
[1249.02 → 1252.36] You will meet people who are interested in the same things you're interested in.
[1252.36 → 1254.40] And I am an introvert.
[1255.22 → 1262.64] It is very hard for me to talk to a lot of people, which may seem a little bit counterintuitive because here I am talking to you.
[1262.92 → 1264.30] That surprises me.
[1264.48 → 1264.72] Yeah.
[1264.72 → 1274.16] But by talking to you once, and now this discussion will be out in the world, folks who are interested in the things that we're talking about today will reach out to me.
[1274.28 → 1280.40] I don't have to go out and talk to a thousand people to find the two or three who are going to share these interests.
[1280.40 → 1287.98] And so it's a good hack also to find the people who, you know, you really can brainstorm with and share with.
[1287.98 → 1304.58] What up, nerds?
[1304.62 → 1306.46] Jared Santo here, your humble producer.
[1307.00 → 1310.78] I'd like to tell you about something new we're beta testing around practical AI.
[1311.20 → 1315.02] It's a membership program, which we think could be really valuable for the whole community.
[1315.02 → 1323.50] We call it Changelog Plus, and it's the best way to directly support practical AI and all the podcasts, videos and other stuff we create here at Changelog.
[1323.90 → 1328.36] We have big plans and ambitions for this, but we are experimenting for now to make sure there's interest.
[1328.82 → 1335.40] That means when you sign up today, you get practical AI and whatever Changelog shows you listen to now, except no ads.
[1335.82 → 1338.48] I guess that means this part you're listening to right now, it'll be gone.
[1338.82 → 1344.70] We also have some extended episodes planned, bonus content, merch store discounts and a lot of ideas.
[1344.70 → 1349.36] But since it's such early days, we are offering memberships at a 40% discount for early adopters.
[1350.00 → 1351.58] That disappears at the end of August.
[1351.80 → 1354.76] So head to Changelog.com slash plus to join today.
[1355.08 → 1358.52] Lock in that discount, get closer to the metal and make the ads disappear.
[1359.00 → 1362.58] Once again, that's Changelog.com slash plus.
[1362.92 → 1365.22] We'd love to have you supporting us as a member.
[1365.22 → 1365.28] Thank you.
[1374.70 → 1387.42] So you were talking quite a bit, used the word community a bunch of times as we were talking through that last section and really interested in a couple of things.
[1387.42 → 1398.32] First, your insight into kind of how to do data science well, because there are, as we know, there are so many ways to go off the rails in a variety of ways.
[1398.32 → 1407.30] But I also want to throw in the fact that as we are talking today, we are still in this world that is dominated by the COVID-19 epidemic.
[1407.60 → 1412.38] And that has completely changed what we have been doing for years as professionals.
[1412.82 → 1414.42] And we've had to adjust workflow.
[1414.54 → 1416.36] We've had to adjust the way we communicate with people.
[1416.80 → 1421.72] What the word community means to us in terms of implementation has adjusted.
[1421.72 → 1431.48] Could you give us some insight into how you're adjusting and how you help people think about doing data science well in this new environment?
[1432.04 → 1432.16] Yeah.
[1432.68 → 1435.40] I actually think this is an unsolved problem.
[1435.64 → 1441.72] And I'm glad we can talk about it because hopefully it'll get someone who is creative and excited about it thinking.
[1442.56 → 1446.60] Because this, you know, we're recording this podcast on Zoom.
[1446.78 → 1448.88] Like, this is not great.
[1449.32 → 1451.06] This is not the end game.
[1451.72 → 1459.78] This is in no way as rewarding or, you know, as helpful as having a personal or in-person connection.
[1460.58 → 1467.02] And our, you know, data science community of practice has, there are a bunch of events people go to.
[1467.40 → 1472.62] And I always find that, you know, if you want to know what somebody did, you read their white papers or their publications.
[1473.16 → 1478.22] If you want to know what they're, you know, doing now, you take them to coffee.
[1478.22 → 1484.26] If you want to know what, you know, ideas they're thinking about, but they haven't quite decided if they're good or bad yet.
[1484.26 → 1489.64] You have to really talk to them in a way where they're comfortable, usually at some sort of event.
[1489.64 → 1491.82] And now we're missing all of that.
[1491.94 → 1494.42] So we've lost that layer of connection.
[1494.42 → 1502.00] And I feel like we're also burning down a lot of the social capital we've built up before the COVID crisis.
[1502.00 → 1516.74] And so I think there is a wide open space for people who can figure out how we do data science together, how we continue to have this sort of open space to share and learn.
[1516.74 → 1524.44] When we're dealing with the fact that we can't travel, and mostly we have to stay apart from each other.
[1524.98 → 1527.34] And I wouldn't claim to have an answer.
[1527.86 → 1532.02] But I think it's an area where I would love to see a lot more attention.
[1533.16 → 1533.84] I agree.
[1534.06 → 1541.58] It's, you know, last year as we were recording and talking about things, I know Daniel and I were always off to conferences.
[1541.58 → 1549.90] I live in Atlanta, but I was in New York often, occasionally meeting with you and moving around and having great conversations.
[1550.52 → 1560.08] And so it has definitely been a challenge trying to bring the same level of quality into the conversation and the same level of sharing insights.
[1560.08 → 1567.54] Because when you're around the conference table, you know, it's so much easier to just hop up and hit the whiteboard and have those ideas sharing.
[1567.54 → 1582.98] If you take that then to the next level, and you're actually talking about, you know, producing, creating data science products and informing other products with your data science and contributing to that whole development effort.
[1583.30 → 1590.34] It's definitely gotten a little bit harder to get to those points quicker since then.
[1590.48 → 1595.98] And I was wondering, you know, as someone who is certainly actively doing that now, you know, how have you adjusted to that?
[1595.98 → 1602.48] How have you tried to ensure that you're able to get there successfully in the same way you have in the years before we got to this point?
[1603.66 → 1605.96] Yeah, I wish I could say I'd solved it.
[1606.06 → 1610.70] But the things I've been thinking about are trying to observe what's missing.
[1611.04 → 1622.02] So, you know, one thing that has come up for me is that, you know, now that I have all of my meetings in this forum through a screen, I've started to forget who I talk to about what.
[1622.02 → 1628.76] And it's because we're missing, at least for me, the physical cues that were tied to the storage of memory.
[1628.98 → 1633.66] So I have a couple of folks that we had a monthly meeting in a diner in Park Slope.
[1633.92 → 1636.20] And I realized I couldn't, now we're doing it on Zoom.
[1636.20 → 1641.44] And I couldn't remember what we talked about last because we didn't have that, you know, the physical cue.
[1641.56 → 1645.70] We were at this table and I had this like diner coffee cup and the eggs were overdone.
[1645.70 → 1647.38] And I love diners.
[1647.54 → 1650.08] So I say that with the biggest amount of affection.
[1651.06 → 1653.80] And so it's trying to say, okay, I've noticed this is missing.
[1653.94 → 1655.50] How do I create that context?
[1655.70 → 1660.26] So can I use different Zoom backgrounds for different groups of people I'm meeting with?
[1660.34 → 1668.68] Can I physically alter the space I'm in, which is always hard in a New York City apartment, but at least turn around or try and find another corner to sit in?
[1668.68 → 1680.62] And when it comes to the work of data science, one thing I've noticed is missing is the casual brainstorming and relationship building.
[1680.92 → 1683.00] And I think these things are tied together.
[1683.00 → 1700.48] But it's really easy to talk about the work that's clear, but it's almost too easy to get caught up in the details of what's obvious and not to spend the time on what isn't obvious or those ideas you have that are just a little weird, and you're not sure if they're the best idea or the worst idea.
[1700.82 → 1701.78] I have a lot of those.
[1702.46 → 1708.90] And you need to share with somebody to get their impression, to really know if it's worth thinking about or exploring further.
[1708.90 → 1720.62] So really trying to create the space for that kind of discussion, which is generally less structured, may involve talking about like, what do you see out your window in Atlanta?
[1721.08 → 1721.40] Rain today.
[1721.56 → 1722.86] Yeah, I can show you what I see.
[1723.18 → 1723.54] Rain.
[1724.08 → 1725.68] It's a beautiful sunny day in Brooklyn.
[1726.32 → 1729.74] Yeah, so I'm trying to be very thoughtful about that.
[1729.74 → 1746.84] And then thinking about, you know, as we move into playtesting some of our new stuff, you know, how we do that in a way that gives us the same kind of information that in prior years you could just get by sitting down next to somebody and watching them try to use the product.
[1747.36 → 1754.72] I don't have an answer, but I think the first step is to be really thoughtful about what's missing and then try to create the space for it.
[1754.72 → 1764.18] Yeah, I really resonate with what you're saying, especially as a person in an organization that doesn't have like a big data science team or something like that.
[1764.36 → 1776.48] I oftentimes feel like I have all of these what to me seem like really great ideas, but I really have no gauge on are they good or are they not?
[1776.54 → 1782.80] And I'm not like now I'm not regularly going to meetups or anything like that in like a physical format.
[1782.80 → 1793.58] There's a guy that works down in Indianapolis that I've known for a while, and we just have like a standing meeting on our calendars like every couple of weeks like labelled ML water cooler.
[1793.90 → 1797.26] And we just like chat about random things like you're talking about.
[1797.36 → 1798.86] So I really resonate with that.
[1798.94 → 1811.80] I think that's even like pre-COVID for people that were in that sort of organization where they're like hired in as maybe the first data scientist or like establishing some sort of data science initiative.
[1811.80 → 1813.68] That can be really tough.
[1814.02 → 1816.26] So, yeah, I resonate with that a lot.
[1816.82 → 1818.40] You're right in that same area.
[1818.66 → 1823.44] And it is definitely something that was an issue before COVID, too.
[1823.58 → 1833.80] I think this has just exacerbated the pain of it because it was a lot easier if you were the only data scientist at a company to go out and have data scientist friends at other companies.
[1833.80 → 1837.20] And now you have to be very deliberate about it.
[1837.68 → 1846.20] And, you know, that raises some of the questions is that, you know, you still have customers, you know, right now that you're developing in your new stuff that we'll talk about.
[1846.20 → 1849.90] And you have done that repeatedly over the years.
[1850.48 → 1852.30] How do you adjust to that right now?
[1852.42 → 1863.78] So your ability to, you know, once upon a time you could go places where your customers would be, and you could engage them in various ways that were familiar that are all gone at this point.
[1863.92 → 1872.64] How do you, as you're trying to build things now, and you've already talked about how critical that customer and user feedback is, how do you achieve that today?
[1872.64 → 1874.40] You get into, like, survey science?
[1874.68 → 1875.24] I don't know.
[1876.30 → 1880.68] I mean, yeah, we're really trying to hack together the closest approximation.
[1881.58 → 1890.42] So, you know, I don't have an answer, but figuring out, like, can I give you something to run in your own environment and then be on video and try and observe you that way?
[1890.42 → 1902.44] You know, can I ask you a bunch of questions that seem adjacent to the thing I'm actually interested in to try and understand the context around, you know, how you think about what you're doing?
[1902.56 → 1907.50] And so, for example, for Hidden Door, we've been asking a lot of families, like, how do you tell stories together?
[1907.92 → 1910.20] Like, how do you feel about it as a parent?
[1910.46 → 1912.82] For kids, it's like, why is this fun for you?
[1912.94 → 1915.24] Like, how many characters do you have?
[1915.34 → 1916.60] Do you always make them new characters?
[1916.60 → 1924.38] And so it's really just trying to develop that empathy through the means we have access to right now.
[1924.50 → 1927.28] But, you know, honestly, it is a challenge.
[1928.44 → 1931.58] So I guess at this point, you started to allude to characters.
[1931.58 → 1937.16] So it might be a good moment here to talk about your current work and the current project you're doing.
[1937.44 → 1942.90] I know that you announced on LinkedIn, which is when I reached back out to you, about Hidden Door.
[1943.12 → 1945.46] Could you tell us a little bit about Hidden Door at this point?
[1945.46 → 1947.26] Yeah, I'm happy to.
[1947.26 → 1964.30] I mean, Hidden Door is a product for using machine learning and AI as a tool for creative assistance, primarily focused on kids and the people who like to tell stories and write with them.
[1964.30 → 1972.98] And what I mean by that is that I think the tools of NLP and natural language generation are tremendously powerful.
[1972.98 → 1984.88] But they're primarily useful to provide the things that are repeated in narrative and to accelerate other human creative efforts.
[1985.08 → 1996.94] And by that, I mean, kids are deeply creative, but they are not necessarily familiar yet with things like the standard narrative arc where you introduce tension, how you manage conflict and narrative.
[1996.94 → 2004.82] In genre writing, they may not understand the things you get for free in a genre versus the things you have to explain.
[2005.28 → 2012.58] They may have the spark of an idea, but find that it's actually a lot of work to create the surrounding story.
[2012.58 → 2026.76] And we believe that the technical tools around NLP and language generation are just now starting to become powerful enough to be supportive tools for that sort of storytelling.
[2026.76 → 2030.12] And by the way, they're really fun.
[2030.68 → 2042.42] And I think anyone who spends time with kids or has kids of their own knows that kids are endlessly creative, and they often demand endless creativity of their parents, too.
[2042.74 → 2046.18] Like so many parents I've talked to, and it's my own experience as well.
[2046.18 → 2057.04] You know, it's like, can we tell yet another story about the wombat who really wants to play basketball or the grape that rolled down the stairs onto the subway and went on an adventure?
[2057.80 → 2065.34] And so we're building essentially tools that can be part of this creative process.
[2065.34 → 2072.50] But there are a couple of things I want to be very clear about, one of which is that I don't expect the technology itself to be creative.
[2072.50 → 2075.44] The creativity comes from people.
[2076.40 → 2081.84] And the second is that this does not do all the work for you.
[2082.16 → 2099.36] It's more of a partner in that as you explore and create and play, it starts to fill in the structures and the gaps and the descriptions and does it in a way that is really fun and is actually more like a game than like a homework assignment.
[2099.36 → 2128.20] And then the last thing I'll say, because I know this audience is probably deeply familiar with things like GPT-3 and a lot of the issues with natural language generation tech, is that there is a real need to build structure, safety, coherence, and memory into these systems before they can be deployed for any human-facing application, much less one that you're willing to put in front of young people.
[2128.20 → 2141.20] And so there is a huge amount of engineering that we're thinking through right now around how you build those systems such that we're confident letting people use them in a way that is unsupervised.
[2142.30 → 2144.00] And I mean that in both senses of the word.
[2144.50 → 2149.74] And the last thing I'll say is that I grew up playing Dungeons & Dragons and a bunch of other role-playing games.
[2149.98 → 2150.54] So did I.
[2150.54 → 2153.96] If you need a metaphor for this, it really is the dungeon master.
[2154.34 → 2166.74] Like finally, can we have our computer system play the role of a dungeon master in structuring and guiding a story without being deterministic about where it starts or where it ends?
[2166.74 → 2196.72] So you mentioned a couple of things that I would really love to dig into.
[2196.72 → 2206.20] One of those is you mentioned how you thought that we were kind of at a point where NLP technology could augment some of these things.
[2206.38 → 2207.78] And so I want to dig into that a little bit.
[2207.88 → 2212.46] And also you mentioned like the safety aspect, which is of course like a big topic.
[2212.46 → 2215.22] But maybe we can dig into that first one first.
[2215.52 → 2228.10] So from your perspective, as you've kind of seen a lot of different kinds of subfields within data science and AI growing, what really catches you, catches your attention about like the growth in NLP right now?
[2228.20 → 2235.70] And, you know, maybe why it's crossing into some areas that can augment more sophisticated workflows like this?
[2235.70 → 2240.84] Yeah. So my last company was Fast Forward Labs, which I mentioned earlier.
[2240.98 → 2243.04] We did a lot of independent applied research.
[2243.30 → 2248.94] Our very first research effort at Fast Forward Labs in 2014 was around natural language generation.
[2249.66 → 2252.36] It's an area I've been interested in following since then.
[2252.36 → 2260.10] And at the time, the state of practice was essentially that you pre-generated template sentences.
[2260.62 → 2263.38] It was more like a pre-generated Mad Libs style thing.
[2263.56 → 2266.76] And then you had a process that would dynamically assemble those sentences.
[2266.76 → 2275.38] And it meant that at the time, the tech was perfect for taking quantitative data.
[2275.56 → 2287.32] So something like a weather report, for example, or, you know, a company's quarterly earnings report or even scores in a sports game and writing an article off of that.
[2287.32 → 2298.70] If you showed it something that it had not seen before, it just did not have the language and did not have like the sentences just didn't exist to be generated.
[2298.70 → 2306.72] And at the time, we built at Fast Forward Labs a system that would take structured data about real estate.
[2306.98 → 2311.36] So apartments in New York City, we crawled 60,000 apartment listings.
[2311.90 → 2318.94] And then we built a little system where you could say, OK, this is a two-bedroom, two-bathroom right by Central Park.
[2319.10 → 2323.62] It has a doorman and washer-dryer, and it would write the ad for you.
[2323.62 → 2327.64] And it worked well enough for things that were common.
[2327.64 → 2330.08] So things like that one I just described.
[2330.18 → 2334.44] But you could also put in things like an 80-bathroom, one-bedroom apartment.
[2335.32 → 2336.10] And it would try.
[2336.36 → 2340.90] Like, it would put a few sentences together, but it would sound like, you know, it wouldn't sound very good.
[2341.16 → 2353.14] What has changed since then is the use of transformers and the ability to build these incredibly large-scale pre-trained models that excel at the token prediction task.
[2353.14 → 2370.38] So that means that you essentially take, at an intuitive level, all the internet that's mostly English, a bunch of books, and kind of whatever other commentary data sets we can throw in there, you know, train a multi-billion parameter model against that.
[2370.38 → 2378.44] And then you use that thing now to, given a prompt or a series of tokens, predict what the next token is going to be.
[2378.80 → 2381.74] Now, there are a couple of things that are fascinating about this, right?
[2381.80 → 2385.14] So one is that these models are huge.
[2385.54 → 2387.18] And this is both a good thing and a bad thing.
[2387.24 → 2388.92] We'll come back to this in your second question.
[2388.92 → 2411.78] The second part of it is that what I actually think is really transformative here is not that it's solving a problem that couldn't be solved before, but rather that before you would have to train, let's say you wanted to do a translation from English to French and classification of something as, you know, I don't even know, what are we classifying these days?
[2412.24 → 2415.00] You know, something that's about everything, right?
[2415.12 → 2415.92] Happy or sad.
[2415.92 → 2419.62] And maybe we have a hope of actually solving sentiment analysis for real now.
[2419.96 → 2421.52] And you want to generate some language.
[2421.84 → 2425.82] Like, you would have to build a system that was custom-built for each one of these applications.
[2426.02 → 2428.32] Now you have a general model that can be used for all of them.
[2428.80 → 2429.60] That's pretty mind-blowing.
[2430.02 → 2436.74] Second thing is that the ability to describe a task with few-shot learning.
[2436.90 → 2444.18] So to give a couple of examples of what you want and then have the predictor be able to actually follow that, that's really amazing.
[2444.18 → 2469.14] It actually says to me that we will likely change our expectations of how we interact with NLP systems in the future, where rather than, you know, sort of building these custom-purpose pipelines for one task, we'll expect the and we'll be able to create this sort of general systems that we can tune for a task locally, sort of at the back end.
[2469.14 → 2472.66] There are a bunch of things implied by that about infrastructure you need.
[2472.88 → 2476.12] Like, I don't think everyone's going to have a deep learning box in their house.
[2476.62 → 2477.56] I do have one.
[2477.76 → 2480.00] It's more of a pain, probably, than it's worth.
[2480.54 → 2482.16] Speaking to my current pain.
[2483.24 → 2483.64] Yeah.
[2484.20 → 2486.64] It looks good on the spreadsheet cost-wise.
[2486.88 → 2491.02] And then you think about the hours you spend trying to get some driver installed for something.
[2491.98 → 2493.40] It's just not fun anymore.
[2493.66 → 2494.32] That's my opinion.
[2494.46 → 2495.78] I'm glad you're having fun with it.
[2495.78 → 2514.38] There's a step function improvement in the capabilities of these NLP systems broadly, which means that, actually, again, this isn't something that's completely new, but the speed of development and the ability to play and use them flexibly in different parts of a product has changed.
[2514.60 → 2516.04] Like, the cost functions changed.
[2516.66 → 2518.52] And so that's really exciting to me.
[2518.52 → 2534.62] And then the ability to think about, like, when you think about what these systems are good for, they aspire to create the most mediocre drivel that humanity would create and put on the internet.
[2534.62 → 2538.62] And that is not what we need for writing brilliant stories.
[2539.38 → 2542.84] And it's not what kids need for learning to write brilliant stories.
[2543.32 → 2555.38] And so I'm also really excited about the opportunity that Building on This Foundation opens up to actually create something that is able to encourage that brilliance.
[2555.38 → 2555.78] Yeah.
[2585.38 → 2590.70] Like, you know, you're mentioning much of the internet, which is mostly English, right?
[2590.72 → 2594.04] And there's, of course, a lot of kids out there that don't speak English.
[2594.04 → 2598.10] So, yeah, I definitely see there are some potential issues.
[2598.10 → 2600.74] And, of course, you can't tackle everything at once.
[2600.74 → 2610.62] But what are some of the main challenges that you're thinking about as you're trying to leverage these models for the particular audience that you have in mind?
[2610.62 → 2619.10] Yeah, I mean, largely, I'm thinking about it as allowing the maximum flexibility and creativity within a constrained problem space.
[2620.00 → 2623.26] And just to be very clear about what it means to be safe.
[2623.38 → 2629.22] Like, it took me two tries to get something deeply misogynist out of GPT-3, and I was not trying.
[2630.00 → 2631.26] And that's not good.
[2631.50 → 2632.04] Like, I...
[2632.04 → 2632.60] It's disturbing.
[2632.60 → 2645.32] As of today, I don't think you can put this in front, the raw output in front of people at all, unless you're constraining the domain in which it's able to produce text.
[2645.76 → 2650.38] So I do think there, you could use it today for things like translating from language to code.
[2650.54 → 2653.74] I built a thing that writes really shitty SQL queries.
[2653.74 → 2657.32] That seems pretty safe, like, maybe.
[2658.04 → 2668.20] But for things that are generating or deliberately inciting the model to hallucinate, you know, fictional worlds, it's not safe now.
[2668.20 → 2681.58] So constraining the problem space, such that we're able to manage, say, descriptions of characters and descriptions of items in a way that we can then run another layer of machine learning classification.
[2682.04 → 2692.32] And even, in many cases, human review and human feedback to ensure that what is coming out of the system beats some notion of content standards.
[2692.62 → 2697.26] We also have, you know, other issues around getting what you expect.
[2697.26 → 2704.02] So, you know, GPT-3 and other models sort of let you dial down or up the randomness of the output.
[2704.60 → 2707.90] But when you dial it down, it actually ends up being quite boring.
[2708.24 → 2713.94] And when you dial it up, it's completely random, and you can't direct it where you want it to go because it doesn't have taste.
[2714.64 → 2715.46] We have taste.
[2715.90 → 2725.70] But as far as the math knows, you're just sort of randomly exploring a space and any particular set of tokens is, you know, just as likely as the next one.
[2725.70 → 2731.44] And so we need to build systems that learn and reflect that taste.
[2731.68 → 2740.24] And I believe, you know, at least for our approach right now, those are systems built on top of, you know, fine-tuned GPT-2 systems in this case.
[2740.24 → 2746.40] And so I also want to be very clear because we're recording this, you know, here in August.
[2746.66 → 2748.58] We're at the beginning of this work.
[2748.66 → 2751.40] So I can't speak to it as if I have solved this problem.
[2751.52 → 2754.58] I don't want anyone to point to this discussion and say, oh, they did it.
[2754.66 → 2755.24] So it's great.
[2755.70 → 2756.66] It should be easy.
[2756.72 → 2757.46] It's not easy.
[2757.68 → 2764.66] And I think there's almost as much work involved in what we have ahead as there is in getting to this point in the first place.
[2764.66 → 2779.28] So I actually want to pull us back a little bit from the technical conversation because if we finish up the conversation in a few minutes without me asking what I need to on behalf of my daughter, I am in deep, deep trouble.
[2779.28 → 2788.10] So I'm curious, totally recognizing that you're still fairly early in the process of building what you're building with Hidden Door.
[2788.26 → 2795.10] The first thing that I know when I go downstairs in a few minutes is she's going to be asking what is it, what's it about?
[2795.34 → 2800.78] And, you know, she has these other games in virtual worlds, and she's going to be kind of trying to compare it with that.
[2800.78 → 2813.14] And so that's kind of what I – if you could kind of from that kid's perspective, what – you know, we've talked about, you know, the ability to use NLP in this, and you've mentioned it kind of being the AI-driven dungeon master.
[2813.54 → 2820.84] But could you tell us for a moment what your vision is for what – when you get to a point where you're ready, what that's like for the kid?
[2821.06 → 2823.04] What you think they're going to experience?
[2823.14 → 2825.24] Maybe give us a little quick example.
[2825.94 → 2826.82] I'm so glad you asked.
[2826.90 → 2830.08] I'm hoping she'll be one of our play testers, too, if she's up for that.
[2830.08 → 2831.94] Oh, she's very up for that.
[2833.04 → 2833.48] Yeah.
[2833.62 → 2837.36] So from the kid's point of view, there are really two different things going on.
[2837.52 → 2844.94] So one is to give them essentially a buddy that is co-writing with them, but where they are in control.
[2845.58 → 2852.84] So, you know, the kid can say today, you know, I want to be a wizard who's getting on a rocket, going to the moon.
[2852.84 → 2859.86] And the system will say, yes, and on the moon, we're going to find, you know, a pizza shack.
[2860.06 → 2863.74] And obviously, I need this help, too, because I'm just making this up off the top of my head.
[2863.74 → 2864.04] That's fine.
[2864.14 → 2864.92] No, it's fine.
[2865.08 → 2865.60] That's good.
[2865.68 → 2866.00] Keep going.
[2866.52 → 2868.50] Then the kid can say, oh, no, it's not pizza.
[2868.58 → 2869.32] I don't like pizza.
[2869.44 → 2874.26] It's spaghetti, you know, or it's, you know, it's porridge, whatever fits in their model.
[2874.26 → 2877.62] And the system will start to generate things that adapt.
[2877.62 → 2889.88] So it's really sort of this partner buddy where they are able to, you know, hit a button or swipe or have something that can support their creativity.
[2890.42 → 2898.08] And it reduces the work of, you know, creative play by providing that support.
[2898.08 → 2899.80] And they can say, oh, yeah, this is great.
[2899.80 → 2904.82] You know, we, you know, I opened the box and I did find, you know, a shard of rainbow inside.
[2905.24 → 2906.90] Or they could say, no, you know, I hate rainbows.
[2907.18 → 2908.06] It was a horseshoe.
[2908.32 → 2910.62] And then the system will adapt to that.
[2910.70 → 2913.24] And then the next thing will be that as well.
[2913.52 → 2921.82] At the same time, this game is encouraging and rewarding creativity and bravery and certain behaviour.
[2921.82 → 2930.34] So you also have it playing the role of a writing coach, sort of helping them think through, you know, what do you think should happen next?
[2930.46 → 2931.88] Where should this character go?
[2933.38 → 2942.02] You know, sort of encouraging them to branch out a bit if they get stuck, giving them that guidance on where they need to go.
[2942.02 → 2945.62] But always leaving them, you know, sort of in the driver's seat.
[2946.20 → 2950.06] I also, you know, as I said, we're still prototyping and playtesting.
[2950.48 → 2963.10] But I think that from the kid's point of view, this is something that helps them explore these worlds that they have in their own minds, and they already want to explore through text.
[2963.10 → 2968.38] And it's something where their characters can represent their individual experience.
[2968.76 → 2974.94] So, you know, every kid has things in their lives that they don't see reflected in media.
[2975.26 → 2981.72] And this is, of course, particularly true for, you know, some people over others.
[2981.72 → 2992.94] Or I have a friend who's an immigrant who said, you know, my kid is not going to see any stories about the clashes of cultures that you see in our family because our family is so unique.
[2993.10 → 2996.50] But she wants to create these stories for herself.
[2997.36 → 3008.78] So I think one of the real exciting things is letting kids sort of show their own experiences through these stories in a way that maybe they're not seeing in traditional media.
[3009.22 → 3016.04] And then also, because this is a dynamic system, these characters can grow with them.
[3016.34 → 3022.24] I know that, you know, especially young kids like, you know, an eight-year-old, they're changing all the time.
[3022.24 → 3023.40] They're learning so much.
[3023.48 → 3026.94] They're having all these, you know, new and amazing experiences.
[3027.44 → 3039.22] And the character that they wanted to play with six months ago, you know, can grow up with them and can have experiences along with them, which I think is something pretty, you see it in video games.
[3039.22 → 3042.12] But it's not something we typically see in books.
[3042.12 → 3046.88] So I'm hopeful they'll be able to create those sorts of experiences.
[3046.88 → 3048.16] It's interesting.
[3048.30 → 3054.96] It sounds like she has kind of single-player games that she does currently, and she has or experiences in all games.
[3055.04 → 3055.80] They can be educational.
[3055.98 → 3057.96] And then there are multiplayers with other kids.
[3058.08 → 3070.84] To some degree, it feels like it's a bit of a hybrid where you kind of have this AI-enabled buddy that creates a multiplayer experience in what would otherwise be a single-player engagement.
[3070.98 → 3072.46] Is that a fair way of representing it?
[3072.46 → 3075.70] It is, though I'll also put a little asterisk on this.
[3075.78 → 3076.00] Okay.
[3076.12 → 3082.38] We're thinking deeply about what this looks like to play with other kids and with your parents as well.
[3082.38 → 3094.76] And so I think, yes, it is having, as we've conceived it right now, the vision is having that AI as a second player, but also not an equal one to you.
[3095.00 → 3098.74] So I don't know if you have an Amazon Echo or Google Home.
[3099.38 → 3099.88] We do both.
[3099.88 → 3108.12] So the way that kids are able to use those devices to play music, to ask questions, they don't think those are people.
[3108.30 → 3109.54] They don't think those are peers.
[3110.60 → 3114.82] They're very much the one who's driving where you go with that interaction.
[3115.06 → 3119.90] I see a very similar interaction here where they have the ownership of the story.
[3120.08 → 3120.96] They're the one creating.
[3120.96 → 3128.08] But this is a tool that they're having a dialogue with that is helping them sort of think through and explore those stories.
[3128.80 → 3128.94] Okay.
[3129.22 → 3133.48] I guess final question is just any thought toward the future about where?
[3133.72 → 3137.36] I'm really interested, especially in this application of NLP.
[3137.56 → 3138.20] We hit it a lot.
[3138.20 → 3144.12] But just kind of where this may take us going forward, you know, what are some of the future visions that you have?
[3144.30 → 3153.70] And maybe not strictly things that you're planning to do, but things that you could see happening in the industry that might affect kids in this positive way to kind of finish out.
[3154.22 → 3154.44] Yeah.
[3154.70 → 3157.22] I mean, I love thinking about these questions broadly.
[3157.22 → 3170.06] I think that machines that can understand language well and can respond to us in language are incredibly powerful because language is the interface we use to talk to each other.
[3170.48 → 3181.50] And the ability to take information and represent it in language, whether it's for children or for anybody, is something that is really powerful.
[3181.50 → 3189.38] And we haven't yet seen what the set of products and interactions, like we haven't seen the end of that yet.
[3189.50 → 3196.34] I don't think chatbots are the height of innovation around interacting with systems through, you know, natural language.
[3196.68 → 3200.68] So that's something where I don't know what exactly it looks like.
[3200.68 → 3208.82] But I do think that a decade from now, it's quite feasible to think that it'll be a commodity to interact with a lot of systems.
[3209.02 → 3212.54] And not just in a like, you know, Alexa, play me the song sort of way.
[3212.80 → 3223.06] But in a, you know, like, can you take a look at this data set and actually tell me something meaningful out of it so that I can make a better decision sort of way.
[3223.06 → 3225.62] So that's something I'm pretty excited about.
[3226.16 → 3233.78] I also think we're seeing this proliferation of sort of ways for people to create with this technology.
[3234.42 → 3237.54] And again, this is actually starting at the professional level.
[3237.54 → 3243.88] So with AutoML tools, but we're seeing much greater democratization of access to the tech.
[3243.88 → 3258.88] And honestly, as much as I love data scientists and I consider myself to be one, I think the most creative applications come when you take that capability, and you give it to people who have some other expertise or some other world they're living in.
[3259.08 → 3270.80] And so I'm pretty excited to see what people are able to do with it when it doesn't take a huge investment or a huge amount of technical skill to actually start to play with this stuff.
[3271.50 → 3271.54] Awesome.
[3271.54 → 3274.08] Well, I think that's a great place to wrap up.
[3274.14 → 3275.28] Perfect perspective.
[3275.54 → 3279.08] I know that there's so much, so much to talk about in these areas.
[3279.42 → 3288.48] There's only so much time to cover, but we're going to for sure put the link to Hidden Door and some of these other things we've discussed in our show notes.
[3288.92 → 3295.94] So if you're curious, and you're listening in on this later, maybe, and curious about Hidden Door, check out those links.
[3296.36 → 3298.06] We really appreciate you joining us, Hillary.
[3298.16 → 3299.82] It's been a great conversation.
[3299.82 → 3300.74] Thank you both.
[3300.74 → 3301.84] This has been a lot of fun.
[3301.84 → 3309.98] Don't forget we have a giveaway going on in celebration of episode 100.
[3311.08 → 3317.80] Enter for your chance to win some awesome AI hardware from NVIDIA, Intel, and Google, plus practical AI and Pachyderm swag.
[3318.08 → 3320.40] We're giving away three bundles, so you have a good shot at them.
[3320.90 → 3324.50] Check your show notes for details on entry you have until the end of the month.
[3324.50 → 3331.48] Speaking of Pachyderm, a little birdie told me they have a big announcement coming soon, and you should join their Slack channel to stay tuned.
[3331.98 → 3334.18] Learn more about that at Pachyderm.com.
[3334.88 → 3337.60] Thanks to our longtime sponsors for their continued support.
[3337.94 → 3343.48] Shout out to Vastly, Linde, and Rollbar, and to the mysterious Brake master Cylinder for these awesome beats.
[3343.98 → 3344.96] That's all for now.
[3345.20 → 3346.50] We'll talk to you again next week.
[3346.50 → 3346.52] We'll talk to you again next week.
[3355.00 → 3358.26] We'll talk to you again next week.
[3358.68 → 3361.00] We'll talk to you again next week.
[3365.16 → 3369.94] We'll talk to you again next week.
