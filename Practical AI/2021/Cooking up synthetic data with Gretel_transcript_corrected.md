[0.00 → 9.94] Synthetic data is the ability to generate data that is almost indistinguishably recognizable from some type of source data set.
[10.20 → 15.46] And it has all the granular elements of the original data set that you would want.
[15.96 → 21.96] However, if you combine those granular elements, you don't have a one for one matching to a record in the source data set.
[22.16 → 28.34] And, you know, it heavily relies on machine learning and artificial intelligence to learn the semantics of the source data set.
[28.34 → 44.50] And at that point, once you learn those semantics and that model is built, you could just continue to generate records that in aggregate tell the same story as the source data, which is kind of like one of the key elements that we always like to talk about is you could still run the same types of aggregate queries and get the same story.
[45.16 → 48.42] It's not about just being able to use the individual records that you synthesize.
[50.50 → 55.22] Bandwidth for Change Log is provided by Vastly. Learn more at Fastly.com.
[55.22 → 59.84] Our feature flags are powered by Launch Darkly. Check them out at LaunchDarkly.com.
[60.08 → 65.82] And we're hosted on Leno cloud servers. Get $100 in hosting credit at Leno.com slash Change Log.
[65.82 → 75.78] Hey, friends, this episode of Practical AI is brought to you by Modish, a podcast from the team at Heroku that explores code, technology, tools, tips, and developer life.
[75.88 → 81.04] There are tons of great conversations on the Modish podcast, so I would encourage you to check it out and subscribe.
[81.04 → 91.32] But in particular, I wanted to bring to your attention two episodes, episode 98 and 99, where Julien Tuque explores the ethical and technical sides of deep fakes.
[91.66 → 100.34] The rise of manipulated pictures and videos and other forms of computer-generated media are able to cause uncertainty and doubt in what we see and hear online.
[100.48 → 104.52] So how are we able to use these tools for good, if at all?
[104.80 → 105.54] Here's a sneak peek.
[105.54 → 113.04] Let's say we want to do a deep fake of my voice, and we train the model, and we have enough data and everything.
[114.04 → 126.74] This will be also able to imitate my accent, for example, like how I pronounce English and the strong pieces of my accent or is not there yet.
[126.74 → 135.16] It really depends. If there would be a person with similar accent on the input, then it would be fine, but it's kind of cheating.
[135.68 → 140.68] You can think it's cheating because we're reusing accent of a different person that's similar to your accent.
[141.12 → 150.46] But if it would be like an American native speaker or a person with a British accent or like whatever other accent,
[150.46 → 154.84] then it will kind of be a mixture on the output.
[155.48 → 158.96] So we're not there yet in terms of converting accents.
[159.68 → 164.38] It's a little bit more difficult than we initially anticipated because when we started the company,
[164.50 → 168.40] we thought it would be, you know, we'll kind of solve it in a year or something.
[168.52 → 172.86] But then it turned out that, oh, no, we're here for much longer.
[172.86 → 182.02] Check these episodes out. Links are in the show notes to both episodes or head to heroku.com slash podcasts to listen and subscribe.
[182.50 → 187.08] Again, check the show notes for links or go to heroku.com slash podcasts.
[187.08 → 207.24] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive and accessible to everyone.
[207.50 → 211.64] This is where conversations around AI, machine learning and data science happen.
[211.64 → 218.02] Join the community and Slack with us around various topics of the show at change.com slash community and follow us on Twitter.
[218.14 → 219.74] We're at Practical AI FM.
[226.22 → 229.56] Welcome to another episode of Practical AI.
[229.96 → 231.56] This is Daniel Whiten ack.
[231.66 → 234.84] I am a data scientist with SIL International,
[235.14 → 238.22] and I'm joined as always by my co-host, Chris Benson,
[238.22 → 242.64] who is a principal emerging technology strategist at Lockheed Martin.
[242.94 → 243.58] How are you doing, Chris?
[243.98 → 244.94] I am doing very well.
[245.00 → 245.84] How's it going today, Daniel?
[246.18 → 246.96] It's going good.
[247.04 → 248.98] It's a nice cold day here in Indiana.
[249.68 → 252.20] We'll have a few more of those before this is all done.
[252.20 → 253.24] Probably so.
[253.80 → 256.44] It's not quite as cold down here in the sunny south.
[256.84 → 257.10] Yeah.
[257.20 → 258.76] Although it's not sunny today, actually.
[260.06 → 260.50] Yeah.
[260.72 → 266.46] And we had a new project funded this year related to some AI work for local languages
[266.46 → 270.72] and trying to get all of that spun up and infrastructure in place
[270.72 → 276.36] and community website up for some shared AI tasks and that sort of thing.
[276.52 → 280.86] So it's a lot of structuring and setup right now for me, I would say.
[281.66 → 283.78] I don't know what big things you've got going,
[283.96 → 286.28] but yeah, it seems like that time of year for me.
[286.74 → 287.14] Absolutely.
[287.52 → 289.86] You know, from my standpoint, I've just been enjoying,
[290.04 → 292.48] you know, just getting out there this weekend,
[292.80 → 293.84] flew around a little bit.
[294.04 → 295.34] I had my first night flight.
[295.34 → 295.66] Right?
[295.70 → 295.96] Yeah.
[296.14 → 296.42] Pleasant.
[296.50 → 298.26] Get back to work here this week, and it's good.
[298.58 → 298.74] Yeah.
[298.84 → 302.10] Chris is getting his pilot's license for any of those out there
[302.10 → 304.20] that are wondering what he's talking about.
[304.34 → 305.86] But yeah, that'll be exciting.
[306.02 → 307.60] I didn't run into anything last night.
[307.60 → 309.20] It was a good story.
[309.52 → 309.66] Yeah.
[309.74 → 314.60] I'm close by Purdue University, and we have an airport at the university.
[314.82 → 316.94] So I told Chris as soon as he gets his license,
[317.20 → 320.18] he can fly up here, and then we can do our recordings in person.
[320.46 → 320.94] There you go.
[320.94 → 325.96] Today, I'm really excited by the topic that we have going.
[326.34 → 329.16] Chris, a lot of times in our past conversations,
[329.16 → 335.08] we've made reference to synthetic data or augmented data
[335.08 → 336.74] or data augmentation methods.
[336.74 → 340.78] We've also talked in various forms about privacy,
[340.78 → 344.12] but I don't think we've really had an episode
[344.12 → 347.42] that has combined those in the great way that we're about to.
[347.42 → 353.16] So today we have with us John Myers, who is CTO and co-founder at Gretel.
[353.38 → 354.24] Welcome, John.
[354.60 → 355.26] Hey, good morning.
[355.48 → 356.18] Happy to be here.
[356.70 → 357.00] Yeah.
[357.20 → 361.84] First, before we dive into all of that good data-related stuff
[361.84 → 363.48] and practical goodness,
[363.86 → 366.82] could you just give us a little bit of an idea about your background
[366.82 → 369.08] and how you ended up working with Gretel?
[369.50 → 370.48] Yeah, absolutely.
[370.92 → 375.80] So I think the way I kind of ended up at Gretel is somewhat accidentally,
[375.80 → 381.20] which I think a lot of folks who ended up in this field ended up that way.
[381.80 → 385.96] So my background is computer science by education.
[386.42 → 390.02] And then I did about 14 years in the Air Force.
[390.60 → 391.90] When I joined the Air Force,
[392.08 → 394.68] I came in as a communications and information officer,
[395.08 → 399.24] which is kind of a fancy word for kind of like network IT leader.
[399.24 → 403.72] And I did a couple of years working in space launch communications
[403.72 → 406.08] out in California at Vandenberg Air Force Base.
[406.84 → 411.94] And then I got an interesting application to go to the National Security Agency
[411.94 → 416.76] and do some really cool hands-on engineering and development work.
[417.36 → 418.18] Sounded really awesome.
[418.52 → 419.76] At that point, you know,
[419.80 → 423.76] my knowledge of the NSA was basically having seen Enemy of the State with Will Smith.
[423.76 → 425.76] And I was like, that sounds...
[425.76 → 427.42] Wait, you mean it's not like that?
[428.26 → 431.58] I wouldn't say it is a documentary of sorts.
[431.80 → 434.48] But I was like, well, it sounds really cool.
[434.74 → 436.04] Loosely based on reality.
[436.30 → 437.36] Yeah, loosely based on reality.
[437.50 → 439.58] I didn't meet Will Smith or anything, so that was a bummer.
[439.80 → 441.26] But it was over in Maryland.
[441.46 → 442.62] I'm from Philly originally.
[442.82 → 443.86] I was like, it's close to home.
[443.92 → 447.28] I can get out there and like kind of just experience something new.
[447.28 → 453.34] So when I got there, I got immersed into the intelligence community and working at NSA.
[453.72 → 456.74] And I still wore the Air Force uniform, but I was kind of in an offshoot program there.
[456.80 → 461.48] And I got to work on really cool stuff, working on like low-level operating system engineering,
[462.30 → 464.48] you know, building exploits, stuff like that.
[464.78 → 468.84] And then I kind of pivoted and doing the big data analysis,
[468.84 → 471.56] which was kind of up-and-coming field at that time.
[471.56 → 475.74] And then I left there, did one more stint with the Air Force,
[475.84 → 478.08] doing a different set of things out in Las Vegas.
[479.22 → 483.90] And at that point, I was kind of at a critical point if I wanted to stay in full-time or do something else.
[484.04 → 486.80] And at that point, I was so hooked on building.
[486.98 → 491.78] I just wanted to build and engineer and building engineering teams that I decided to leave active duty.
[492.04 → 492.70] I joined the reserves.
[492.70 → 498.28] And then when I got out, I did the complete opposite thing you can do when you're part of a 300,000 person organization.
[498.28 → 501.92] And I launched a startup in cybersecurity with like three other people.
[502.30 → 505.06] And then we did an enterprise security startup.
[505.56 → 507.26] And we did that for three years.
[507.32 → 508.40] It was called Efflux Systems.
[508.80 → 516.96] And then we were acquired by a company called Net Scout that kind of is one of the leaders in network performance monitoring
[516.96 → 522.94] and wanted to utilize some of what we had in cybersecurity for some of their upcoming products.
[523.32 → 525.50] When I got there, I was a principal architect.
[525.50 → 530.82] And among a lot of projects I worked on, I worked a lot on a lot of their cloud infrastructure.
[531.88 → 539.50] And they build capabilities that also help enterprises and service providers detect and stop DDoS attacks.
[540.06 → 544.96] And a lot of those devices collect a ton of telemetry from the customer environment
[544.96 → 548.88] and send it up to a cloud repository where it's securely kept.
[548.88 → 555.58] And we wanted to look at how we can do analysis of that data and start pouring through that data.
[555.80 → 558.62] And you start to realize there's a lot of sensitive information in this data.
[558.88 → 562.08] And we should probably pre-process it so we can kind of work on it safely.
[563.08 → 567.16] And I think I spent a lot of time doing that, probably more time than I wanted.
[567.16 → 574.96] And that was kind of like this pivotal transition point where I got into doing kind of engineering to enable me to do engineering.
[575.84 → 581.16] So at the same time, you know, back in my head, it's kind of like one of those like shark tank pitches.
[581.32 → 583.42] I'm like, surely I'm not the only person with this problem.
[583.64 → 585.66] Like, what could we do about it?
[585.66 → 593.16] With some other close colleagues of mine, as we started talking about these stories and we all kind of shared very similar but different pain points,
[593.16 → 600.54] we kind of orbited around this idea of like, what if we could just make data anonymization and being able to make data safe to use,
[600.62 → 605.28] kind of just like a general purpose thing that like engineers everywhere can use and Ada, Ada, Ada.
[605.48 → 606.06] We launched Schedule.
[606.06 → 615.90] So we launched Schedule in the fall of 2019 with myself and our CEO and my other co-founder, Alex Watson,
[615.90 → 622.06] who has, you know, a very heavy machine learning and data science background and was previously the general manager at AWS Macy,
[622.58 → 628.50] which is another product that is very, very successful at AWS for detecting sensitive information in S3 buckets.
[628.78 → 631.04] So he has a whole different slew of stories.
[631.18 → 633.36] Some call them nightmares about data anonymization.
[633.36 → 636.16] And yeah, we've been doing it ever since.
[636.32 → 643.40] And, you know, really our mission is to make data anonymization and creating safe data generally available to engineers everywhere,
[643.58 → 652.84] not just the resourced organizations like the Facebook's and the Googles who have massive resources to kind of experiment with all the techniques to do it.
[653.34 → 654.36] I am kind of struck.
[654.52 → 661.34] I was thinking while you were talking, especially with your background in the Air Force and at the National Security Agency and other places,
[661.34 → 669.20] I was sort of remembering back to our conversations with the founders of Amu ta, which is another company that does sort of,
[669.50 → 675.96] I guess they're more focused on sort of the combination of law and data and governance and all of that sort of thing.
[675.96 → 682.34] But it seems like there's this really strong, whatever it is about, you know, people coming from that sort of background,
[682.34 → 684.60] they had a sort of similar background.
[684.80 → 693.24] It sounded like, you know, really creates some deep thinking around these problems of data anonymization, privacy, governance.
[693.24 → 696.04] I don't know, John, what's your perspective from that side?
[696.12 → 706.82] How do you think like your background with these sorts of agencies or like the military has sort of shaped how you think about data maybe differently than maybe someone like me,
[706.88 → 714.28] who's just always sort of started in startups and just sort of got what data I could and have used it.
[714.58 → 718.58] And Daniel, that was exactly what I was going to ask next, too, just so that you know.
[718.58 → 723.98] Yeah. Well, also, you know, Chris has some experience in that world as well.
[724.26 → 735.00] Gotcha. Yeah. So I think one of the things that I learned a lot about doing intelligence work in the military and working with data is that I learned a lot about the chain of custody of data.
[735.44 → 742.12] And a lot of times when I meet folks that are like yourself, like a data scientist, or they're in the analytics space,
[742.12 → 748.76] a lot of times they are kind of just given data and given some task and say, like, here, go make magic happen.
[749.32 → 756.52] And I don't know how often that kind of like the chain of custody or like how that data was actually generated is thought about.
[756.98 → 759.46] But for me, I always think about like, where was that data?
[759.56 → 760.42] Like, where was it?
[760.80 → 761.42] Where was it born?
[761.86 → 765.78] Like at the moment that data was collected, something happened, and it was written into a database.
[765.78 → 767.90] And I think that way a lot.
[768.04 → 772.70] And so my other co-founders also have a background in intelligence community.
[772.90 → 774.38] And so it was something we're all aware of.
[774.98 → 780.14] And so when we started talking about Gretel, really, we wanted to make consumers safer.
[780.26 → 785.74] Right. So to make their personal data not used as the way it is today,
[785.74 → 790.86] because often when you think about big companies like Google, Facebook, like they build products,
[790.86 → 792.88] but they also look at their users as a product.
[792.88 → 798.88] So we kind of backed into saying, like, what if we could enable engineers to make the data safe at the moment that it's created?
[798.98 → 800.60] So right at that inception of the data.
[800.72 → 803.80] And that's something that we were just really aware of, of where we came from,
[803.84 → 806.08] because that chain of custody of the data is so important.
[806.32 → 809.90] And it's not as much as a governance thing versus more of an engineering problem,
[809.90 → 814.56] because as an engineer, a data engineer, when I'm writing my data into my production database,
[814.86 → 819.04] can I at the same time create a safe version of that data and write it into a staging database
[819.04 → 824.30] that anyone can access with privacy guarantees, so I don't have to go through this whole repetitive process
[824.30 → 830.34] of snapshooting my production database, combing over it, writing some bespoke script to sanitize it?
[830.36 → 833.90] Can we just make it part of the entire pipeline at the point where the data is created?
[834.34 → 835.58] I would like to go back for one second.
[835.78 → 840.62] When you kind of got to that moment where you realized, am I the only one that's dealing with this issue?
[840.62 → 845.90] And you kind of had maybe an aha moment or something there where it was kind of, you kind of realized that.
[846.40 → 847.44] What got you to that?
[847.52 → 853.26] I'm kind of curious about that moment of recognition, because I think other engineers and other data scientists wonder,
[853.64 → 857.44] you know, are they going to have something similar, you know, as they're out there creating?
[857.58 → 863.72] What was it that made you suddenly realize this is something that I'm recognizing not only impacts me,
[863.78 → 868.98] but probably impacts the broader community and I had as well as I have something to contribute toward that solution.
[868.98 → 874.02] And as part of that, was any of the background, you know, we talked about your intelligence background there.
[874.24 → 877.52] Did any of that contribute to that moment and that recognition?
[877.70 → 881.18] If you hadn't had any of those experiences, might you have missed that altogether?
[881.68 → 884.26] I think there's like two big things to answer that.
[884.32 → 885.50] And I'll start with the former.
[885.68 → 891.64] So like when I hit the aha moment, like I had a small team at my previous company, and we were kind of analyzing the data.
[891.90 → 896.08] And, you know, we realized that we needed the right ways to kind of detect the sensitive information that's in it.
[896.08 → 900.72] And the sensitive information is an information that like is the fact of the sensitive information.
[900.72 → 901.92] It's like it's like names.
[902.04 → 902.80] It's company names.
[902.86 → 903.68] It was email addresses.
[903.90 → 904.68] It was IP addresses.
[904.88 → 905.94] It was things that were identified.
[906.02 → 907.50] I can identify our customers.
[907.92 → 908.20] PPI.
[908.86 → 909.22] PPI.
[909.36 → 909.48] Yeah.
[909.54 → 912.34] And so we were like, OK, well, let's just write some detectors for it.
[912.34 → 913.38] We can use a lot of regexes.
[913.54 → 914.68] We could write a custom rules.
[914.68 → 917.44] And then we're like, OK, now we need a way to write a rule really quickly.
[917.58 → 919.62] OK, now we need a framework to put the rule into.
[920.02 → 924.30] And I was like, I can't be the only person who's trying to figure out if an email address slipped into a data stream.
[924.30 → 936.78] And, you know, it's not like some communities have like really specific data structures that are really specific to them, like in health care and stuff like this was just things that are PPI and to a degree PII that identify organizations and people.
[937.82 → 947.50] And there are generic ways to do that where like can you just like to bring a regular expression to the table and like just like some framework kicks in and can scale for you.
[947.50 → 953.00] That was one of the kind of things I kind of turned that was like what we were doing was fairly a repeatable process.
[953.48 → 956.00] And we assumed it was a repeatable process in many industries.
[957.02 → 963.98] And the second part of that was where to apply that detection and where to apply whatever type of transformation or synthesis we want to do.
[964.30 → 970.12] It was kind of a no-brainer that you want to do it as close to the source where the source of the data is itself.
[970.12 → 978.64] You know, you were talking about systems that can collect private information like can you do it on the system before you even think about transmitting it to the cloud, so there's no risk there.
[978.74 → 982.60] Can you do it on the edge as you know people would say these days.
[983.08 → 988.56] That's not even a question for me based off of kind of our backgrounds and being like so kind of in tune with data custody.
[988.56 → 1001.26] So I'm curious as you've built out the set of products which we'll definitely get into the details of those in a bit and talk a lot more about the practicalities of synthetic data and all that.
[1001.38 → 1006.40] But you kind of mentioned that this was like doing engineering so that you could do engineering.
[1006.40 → 1006.90] Yeah.
[1007.08 → 1020.82] As you've like engaged with various companies that are using your product has that story been getting sort of like they sort of immediately understand what you're after.
[1021.00 → 1032.08] Because I remember like, you know, when I was first getting into data science there wasn't a lot of talk about this sort of, you know, rigour and the way we were treating data.
[1032.08 → 1041.88] And probably, you know, people might have seen something like this as maybe a little bit burdensome like something they have to do before they actually get into the work that they really want to do.
[1042.00 → 1052.66] But how have people been like feeling that need in the industry and been, you know, accepting this sort of solution from your perspective?
[1053.30 → 1055.12] Yeah, I think it's been received really well.
[1055.24 → 1057.26] And it's kind of a classic build versus buy problem.
[1057.40 → 1059.04] And a lot of folks are just willing to buy.
[1059.04 → 1066.84] But what they don't want to buy is some type of really difficult to install appliance or virtual appliance that kind of breaks their workflow.
[1067.24 → 1075.34] And so the way that we're targeting this is making it so it is our end user, our developers that can easily integrate it into what they're doing already.
[1075.54 → 1081.66] So making just another API call in their stack of what they're executing on versus saying like, yeah, sure, we can do this.
[1081.70 → 1086.14] But we have to kind of come and install a virtual appliance, and you have to reroute your entire data pipeline through it.
[1086.14 → 1090.60] And so as soon as we kind of explain that, it works right into their existing infrastructure.
[1090.60 → 1100.32] And, you know, we take care of kind of the scale for them where they could just kind of bring, you know, their predictors or bring what they want to actually detect on to the table.
[1100.84 → 1106.90] They'd much rather just kind of buy versus build it because it eats up a ton of cycles for them to kind of build this thing.
[1107.26 → 1109.98] And it's not a build once and deploy type of thing either.
[1110.10 → 1112.54] It's not like they're building a framework that they can deploy once.
[1112.54 → 1119.54] It requires care and feeding because you're constantly adjusting what type of information you're processing and what types of things you want to anonymize on.
[1120.22 → 1124.90] And so we can kind of go on that journey with you and enable you to kind of care and feed a lot faster.
[1124.90 → 1131.82] Have you heard about Knowable?
[1132.06 → 1139.58] It is an awesome new platform for learning from the world's best minds anytime, anywhere, at your own pace through audio.
[1140.12 → 1149.38] Learn about the performance benefits of a plant-based lifestyle from NBA All-Star Chris Paul or how to launch a startup from Reddit co-founder Alexis Ghanian.
[1149.74 → 1153.04] There's even a 10-lesson course from astronaut Scott Kelly.
[1153.42 → 1154.22] Here's a sneak peek.
[1154.22 → 1159.86] We learned a lot up there, but what can you learn from a life in space?
[1160.58 → 1162.06] The answers might surprise you.
[1162.84 → 1167.14] In this Knowable course, I want to share some of the things I've learned that you might not expect.
[1168.34 → 1173.22] Lessons about leadership on a dark night on an aircraft carrier in the middle of a churning sea.
[1174.22 → 1179.30] Lessons about the fear you feel with 7 million pounds of thrust exploding underneath you.
[1179.30 → 1184.60] And most of all, there's an idea out there that astronauts are always perfect.
[1185.36 → 1186.98] Failure is not an option, right?
[1186.98 → 1192.94] That's why I want to take you through some of my life experiences to show you how that's just not true.
[1192.94 → 1202.54] I believe every day, regular human failure, if we handle it right, can be one of our greatest opportunities to learn, grow, and succeed.
[1202.54 → 1206.26] Knowable is accessible on your phone and on the web.
[1206.26 → 1211.08] And each audio course is broken out into individual lessons, usually around 15 minutes long.
[1211.08 → 1216.04] As a Changelog listener, you can get an annual membership to Knowable for 20% off.
[1216.42 → 1219.98] Get unlimited access to every Knowable audio course right now.
[1220.22 → 1227.40] Just download the Knowable app or visit knowable.FYI and use code CHANGELOG for that 20% discount.
[1227.82 → 1230.56] We put a link in your show notes for easy clickings.
[1230.76 → 1235.48] Check out Knowable today and start learning from hundreds of top experts from around the world.
[1235.76 → 1238.72] Once again, that's knowable.FYI, code CHANGELOG.
[1238.72 → 1259.74] So I'm kind of curious.
[1259.86 → 1265.88] I know in the beginning of the conversation when Daniel was introducing you, John, he talked about synthetic data.
[1265.88 → 1276.68] Could you start off by kind of telling us what is synthetic data and kind of give us a little bit of a background before we dive into the specifics of what Gretel does and how it gets there?
[1276.76 → 1280.26] But kind of give us the terms that we need to know to be able to follow.
[1281.16 → 1281.26] Sure.
[1281.52 → 1283.56] So we were at a happy hour or something.
[1283.66 → 1285.44] I'll kind of give you that level of definition.
[1285.72 → 1285.94] Perfect.
[1287.86 → 1294.18] Our podcast is always the happiest of hours in our listeners' week, I'm sure.
[1294.18 → 1296.30] Oh, that was funny.
[1296.84 → 1309.80] So, you know, I would say synthetic data is the ability to generate data that is almost indistinguishably recognizable from some type of source data set.
[1309.80 → 1316.00] And it has all the granular elements of the original data set that you would want.
[1316.50 → 1322.50] However, if you combine those granular elements, you don't have a one-for-one matching to a record in the source data set.
[1322.50 → 1331.28] And it is a, you know, it heavily relies on machine learning and artificial intelligence to learn the semantics of the source data set.
[1331.36 → 1349.68] And at that point, once you learn those semantics and that model is built, you could just continue to generate records that in aggregate tell the same story as the source data, which is kind of like one of the key elements that we always like to talk about is you could still run the same types of aggregate queries and get the same story.
[1349.68 → 1353.60] It's not about just being able to use the individual records that you synthesize.
[1353.90 → 1356.50] I will say there are use cases for using those individual records.
[1356.50 → 1363.42] Like if you have like a development environment, and you're kind of building a system, and you want to look and see how the records fit into your layouts and stuff.
[1363.50 → 1369.56] But for the most part, the idea is to be able to use those records in some type of aggregate feature.
[1369.56 → 1373.26] There's a lot of jargon, of course, in our industry.
[1373.78 → 1377.46] And you've already mentioned as well, like anonymizing data.
[1377.72 → 1385.86] How does like synthetic data complement anonymization techniques or maybe like it's an alternative to it?
[1385.86 → 1390.46] Or how do those two things fit together in terms of anonymization and synthetic data?
[1390.46 → 1398.70] Yeah, I would say it all starts with the core use case, but it could either be a complement, it could be totally separate or it could support and they can support each other.
[1399.06 → 1402.64] So we kind of have two large buckets that we kind of focus on at Gretel.
[1402.86 → 1412.80] And one of them is being able to kind of detect PII, detect PPI, and then apply different transformation techniques to the data in place so that like your data is essentially the same.
[1412.80 → 1416.52] But there's like typical redactions or like character replacements or whatever.
[1417.34 → 1423.40] And that kind of falls in line with a lot of the existing solutions that are out there that fall under kind of like a data loss prevention capability.
[1423.74 → 1434.76] And you'll see a lot of the cloud providers like Azure, AWS, Google, they all kind of have a DLP set of APIs you can apply, except that usually requires like to be bought into their ecosystem and already have your data sitting there.
[1435.20 → 1439.12] In our mind, that's table stakes just to even have a conversation about privacy.
[1439.12 → 1444.86] And we offer a set of APIs that allow you to kind of detect and do those typical transforms.
[1446.14 → 1456.28] And synthetic data for us is a way to kind of take the data set, build a model and kind of let the model generate new records that you can just accumulate and use.
[1456.56 → 1465.94] However, and it doesn't necessarily require you to funnel each record through a certain type of detector and look for PII because we're just going to learn the semantics of the entire data set and generate new records.
[1465.94 → 1470.14] But those records should not be the original records that you had.
[1470.82 → 1471.82] And they play hand in hand.
[1471.96 → 1478.82] It's just like for one example, let's say you have a really sensitive PII, let's say social security numbers in the source data set.
[1478.82 → 1487.88] If you could detect that a certain column or social security numbers, we might go ahead and recommend that you generate new randomized social security numbers, which is very deterministic.
[1488.58 → 1494.10] And then you can have that new column in that data set, then send it into our synthetic capability.
[1494.10 → 1504.68] And that'll just help guarantee that we don't memorize any of the tokens or replay any of those social security numbers, because that is always a risk with synthetic data is that you might memorize and replay some secrets.
[1505.16 → 1511.06] And that's kind of where like that whole field of differential privacy is coming in to address that situation as well.
[1511.06 → 1521.30] So does the synthetic data that's being generated, does it always kind of start with being a replacement for, you know, the actual PII that you're contending with at the time?
[1521.40 → 1524.26] Is it always kind of starting as a replacement factor?
[1524.42 → 1531.92] Or is there ever a use case where you're generating it maybe like what if you're starting with no data, and you wanted to generate it entirely synthetic?
[1532.20 → 1536.12] And just because you don't have something to start with, is that within that or is that something?
[1536.24 → 1538.70] Would that be a separate type of use case, separate product?
[1538.70 → 1550.26] I would say that the synthetic data generation is not just based on doing anonymization, because you can kind of do that type of anonymization without the underlying need for machine learning and AI.
[1550.92 → 1551.08] I see.
[1551.18 → 1561.58] I think the issue that comes up is that you have a lot of different attacks, like re-identification attacks that are completely plausible and possible on data that has been just anonymized in place.
[1561.58 → 1565.54] Right. So just because you're anonymizing names and addresses and phone numbers and email addresses.
[1566.24 → 1571.62] Well, let's say just for argument's sake, you have a bag of customer data, and you have a bunch of records.
[1572.08 → 1578.56] You know, I live in Baltimore and let's say I'm your only customer who is a male in his mid 30s in Baltimore.
[1578.56 → 1586.28] Even if you take all my personal information out, you might be able to join the fact that you have a customer like me in Baltimore, and I'm the only one.
[1586.42 → 1587.62] Well, now you've re-identified me.
[1588.28 → 1595.92] So with synthetic data is how can we actually generate a lot of those other risky fields that are really risky in aggregate.
[1596.06 → 1601.54] Right. So you look at categorical fields like ages, genders, locations.
[1601.54 → 1608.38] How do you actually generate those records so that they can't be recombined to re-identify someone, but they're still useful.
[1608.58 → 1615.78] And when you want to look up, you know, the average amount of revenue you get from people in Baltimore or some type of aggregate question like that.
[1615.96 → 1624.40] And then on the second question, for us to generate synthetic data, you do need some type of training input to learn the underlying semantics.
[1624.40 → 1627.92] And then once you have that model, you can generate any number of records.
[1627.92 → 1629.34] It doesn't have to be like a one-to-one.
[1629.34 → 1633.66] Like if I have like 5,000 training records, you can generate five synthetic records.
[1633.78 → 1635.22] You can generate 20,000.
[1635.90 → 1641.98] And so but once you learn that semantics and the fact that you can generate any number, you can do a lot of interesting things.
[1642.56 → 1644.16] You can do enforcement on what you're generating.
[1644.40 → 1652.00] So let's say I want to generate records, but I only want to accept records that are of a certain category, like a certain age or a gender group.
[1652.00 → 1660.82] So then you can use that to synthesize new records and help balance a data set that might be otherwise biased and not have enough samples of something that you're trying to predict on, for example.
[1661.58 → 1665.84] And so once you have that core model built, you can kind of generate records to meet a lot of those needs.
[1665.84 → 1673.18] We've mostly been talking about use cases around private data and privacy sort of aspects.
[1673.36 → 1677.10] But is this synthetic data generation capability?
[1677.52 → 1685.92] Does it also help people who are working in sort of data scarce scenarios or like imbalanced data set scenarios?
[1685.92 → 1692.42] So let's say that we don't have any sort of personally identifying data in our data set.
[1692.48 → 1696.62] We're not, you know, at least to our knowledge, we're not dealing with that issue.
[1696.78 → 1706.20] But we do either have an imbalanced data set or maybe we're just working in a sort of data scarce domain where we do have some data.
[1706.20 → 1711.78] Like you say, maybe we have 5,000 records, but we really need 25,000 records for our model.
[1711.98 → 1715.50] Is it viable to use synthetic data in that type of scenario?
[1715.92 → 1716.20] Yes.
[1716.40 → 1724.08] And that is actually one of the core use cases that we have experienced where there might be already a situation where data is deemed safe to use.
[1724.22 → 1730.58] I'll use like fraud as an example because fraud is a perfect one where you have so many records that are not fraud.
[1730.86 → 1732.56] You're usually trying to predict the opposite, right?
[1732.56 → 1741.30] So like the field you're trying to predict is an actual fraudulent event, but you might have just not enough records of that fraudulent event.
[1741.30 → 1758.60] And so what we're able to do is kind of guide you through how to synthesize more records that fit into the fraud category so that when you go, and you build your actual machine learning algorithm, that there's enough of those fraudulent records there that it could actually, you know, create a proper decision boundary or whatever.
[1758.60 → 1761.78] So you have a net better model at the end.
[1761.78 → 1791.78] 
[1791.78 → 1821.78] 
[1821.78 → 1826.30] So you have a net better model at the end.
[1826.30 → 1827.30] And then you have a net better model at the end.
[1827.30 → 1828.30] So you have a net better model at the end.
[1828.30 → 1829.30] And then you have a net better model at the end.
[1829.30 → 1831.30] So you have a net better model at the end.
[1831.30 → 1835.72] And so right now our first pluggable back end is a LSTM on TensorFlow.
[1835.72 → 1840.96] So it is kind of a sequential model, which is a lot different from a lot of the other techniques that are out there.
[1841.52 → 1845.46] And what we do is we have the ability to kind of focus on text input.
[1845.72 → 1852.92] And then in the open source package, we also have another module that kind of wraps that entire thing inside of like a data frame.
[1852.92 → 1859.48] And then we can infer different field delimiters, and essentially it will reconstruct those records as a sequence.
[1860.38 → 1862.16] And then exactly that.
[1862.28 → 1863.50] We can do it one of two ways.
[1863.56 → 1866.04] One, you can just say keep generating records with no input.
[1866.46 → 1876.52] Or you could specify what we call a seed where it's like, okay, I only want you to create records that start with, you know, this age group, this gender.
[1876.76 → 1878.52] And then it'll complete those records.
[1878.52 → 1885.32] And that allows you to more efficiently increase a record of a certain type based off of what your requirements are.
[1886.10 → 1892.08] And then what we actually ship as the product is we have a bunch of different layers that work on top of that to do data validation.
[1892.46 → 1903.54] We have separate models that we build that learn and enforce the semantics of individual fields to make sure that when records are generated, they still fit within the constraints that you had before.
[1903.54 → 1912.54] Whether it's the right character sequences, the right structure of the fields, if you have like daytimes, making sure that like categorical fields are always recreated.
[1913.20 → 1916.28] So if you have like, you know, we don't want to invent a new state, right?
[1916.30 → 1921.02] So if there are 50 states that are in a certain column level, we'll make sure we're only generating valid states.
[1921.10 → 1923.00] Those are things that we provide inside the product.
[1923.00 → 1928.96] But the open source package lets you kind of just jump right in to build and train on structured or unstructured data.
[1928.96 → 1945.12] We deserve a better internet and the Brave team has the recipe for bringing it to us.
[1945.12 → 1946.26] Start with Google Chrome.
[1946.50 → 1950.22] Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[1950.42 → 1951.28] Rip out the Google bits.
[1951.42 → 1952.06] We don't need them.
[1952.42 → 1954.92] Mix in ad and tracker blocking by default.
[1954.92 → 1957.90] Quick access to the Tor network for true private browsing.
[1958.26 → 1962.60] And an opt-in reward system so you can get paid to view privacy-respecting ads.
[1962.82 → 1966.56] Then turn around and use those rewards to support your favourite web creators like us.
[1966.88 → 1971.48] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1971.48 → 1988.98] John, I'm curious if some types of data are easier to synthesize than other types of data.
[1988.98 → 1996.60] So you mentioned like dates, you know, categorical variables, categories, labels, you know, numbers.
[1996.78 → 2003.82] But then like we also have things like, you know, audio and imagery and like other things like that.
[2004.00 → 2007.92] What's the sort of current state of the art in terms of synthesized data?
[2007.92 → 2015.72] And what data types or like domains of data maybe are sort of the bread and butter right now?
[2015.76 → 2021.08] And maybe which ones have some challenges in terms of synthesizing data in certain scenarios?
[2021.50 → 2021.60] Yeah.
[2021.68 → 2027.46] So right now, what Gretel ships is really focused around structured and unstructured text.
[2027.46 → 2040.50] So I think about like, you know, records from a database or any type of text input, audio and video and imagery is next that we would probably see in a future iteration of the product.
[2040.56 → 2042.06] And it's something that we're working on now.
[2042.34 → 2054.02] You know, a lot of the state of the art around that is not kind of in our wheelhouse now because we were able to kind of just back into our customer problems via like structured records.
[2054.02 → 2059.28] And yeah, I mean, that's just right now it's just we kind of have to, you know, pick our battles.
[2059.42 → 2067.82] And right now that's kind of the main one that we're focused on is being able to enable people to kind of synthesize new versions of database tables or static data sets so they can more safely share them.
[2068.46 → 2069.56] So I'm curious.
[2069.72 → 2075.56] We've talked a little bit about kind of the product side of things, and also you've made reference to the open source as well.
[2075.56 → 2089.86] Could you differentiate a little bit between kind of what each side of that has to offer to kind of give people a framework in their head about what they would go to for each, and where do they maybe step up from open source to your paid product services, that kind of thing?
[2090.28 → 2090.96] Yeah, absolutely.
[2091.20 → 2094.54] So right now the open source packages and there's two of them.
[2094.54 → 2102.40] One of them allows you to get started with synthetic data and the other one that allows you to get started with kind of our traditional transformers to kind of mutate data in place.
[2103.00 → 2107.98] Those are Python libraries that are available to anyone licensed under Apache 2.0.
[2108.70 → 2112.26] And obviously you go in using those knowing that it's Python.
[2112.68 → 2115.96] And that already is kind of a qualification for a lot of our customers.
[2116.24 → 2116.96] And which isn't a problem.
[2117.06 → 2120.36] We have a ton of researchers and data scientists that live and breathe in Jupyter notebooks.
[2120.36 → 2121.88] And so they're able to plug that right in.
[2122.40 → 2127.54] Last August, we launched a beta of more of our premium features.
[2127.92 → 2134.98] And that beta basically allows you to use our cloud service to test out our labelling capabilities.
[2135.34 → 2142.10] And then what we ended up doing was packaging up a lot of our premium capabilities, which kind of include automatic data validation.
[2142.10 → 2150.38] It does a lot of analysis to make sure that correlations across all your data are held and distributions across your data are held properly.
[2150.90 → 2156.24] We also released those available as an SDK that you can download through our authenticated API.
[2156.76 → 2162.18] We had a great about, you know, several months of going through that beta, getting a ton of feedback from users.
[2162.18 → 2171.54] And then, you know, what we walked away from that knowing is that what we really want to do is make this available to engineers everywhere.
[2171.82 → 2178.52] And engineers everywhere can't necessarily download a Python SDK and incorporate it in their pipeline if, let's say, your entire backend is written in Java.
[2179.24 → 2183.24] And so how do we drastically simplify what these premium SDKs do?
[2183.24 → 2192.44] And so what we're building now is the ability to kind of launch Gretel services as kind of containerized capabilities that are backed by REST APIs.
[2192.82 → 2197.74] So now you can interact with our services purely through a REST API, which is completely language agnostic.
[2198.28 → 2202.28] Every engineer at some point has gone through the process of making API calls to a remote service.
[2202.40 → 2204.76] And so now that is kind of the qualification factor.
[2205.32 → 2210.56] We wouldn't have learned everything that we learned if we didn't have kind of that granular level capability out there through the beta.
[2210.56 → 2215.80] So now the entry point will kind of either be you can run Gretel services in your environment.
[2216.12 → 2220.72] We're also building a hosted service where we can run and kind of scale these capabilities for you.
[2220.94 → 2227.46] What it should be as easy as taking your data set or taking some records, a lightweight configuration, pushing it to an endpoint.
[2227.64 → 2233.36] And that endpoint will then trigger a bunch of backend work to learn, build a model, generate data for you.
[2233.64 → 2239.50] And at that point, we really just want to be a bump in the line in your entire data workflow to be able to call into these APIs.
[2239.50 → 2242.52] And that's what we're working on now is just to really simplify that down.
[2243.14 → 2259.64] Based on what you've seen with your current users and customers, like if I'm a data scientist working on a new project, getting into some new data, do you have any recommendations in terms of workflow with your tools?
[2259.64 → 2262.92] Like, you know, when I get the data, I'm profiling it.
[2263.00 → 2265.58] I'm doing some exploratory analysis.
[2266.16 → 2283.32] Where and when should I be thinking about fitting in some of these, you know, REST calls or Python SDK elements into my workflow so that I can make sure that I'm dealing with maybe both sides of things and anonymity and creating synthetic examples.
[2283.32 → 2286.44] Are you seeing that done maybe more specifically?
[2286.44 → 2294.16] My question would be, are you seeing that done in a workflow like upfront, and they do this on data, and then they use that data moving forward always?
[2294.34 → 2298.50] Or are you seeing this as sort of ongoing part of people's workflow?
[2298.50 → 2304.56] I would say that upfront is not the usual case that we recommend.
[2304.82 → 2314.22] And we recommend that there's usually a little bit of data cleaning you want to do, not down to the granularity of doing a ton of like all the exact feature engineering you would do to build a model.
[2314.22 → 2326.30] But at a minimum, and we have blueprints that help folks go through this process as well, is that you want to identify, you know, for example, columns that you probably don't need to worry about synthesizing because there's not something that your model is going to grab onto.
[2326.46 → 2326.62] Right.
[2326.62 → 2336.18] So if you have records that have maybe like people names in them, typically those people names aren't going to be correlated to a lot of your continuous variables and your other variables in the data set.
[2336.24 → 2341.96] And if you can drop those columns first, you're going to save a lot of time on being able to train a synthetic model for that.
[2341.96 → 2351.10] And so other examples would be, you know, there are a lot of data sets we get from customers that, you know, are highly dimensional, you know, several hundred columns.
[2351.50 → 2357.72] And they're trying to train a model, you know, maybe like XGBoost model on that to predict something.
[2358.16 → 2370.36] And a lot of times, you know, what we recommend is like, look, if you can kind of train your model first, and then you identify what the algorithm themes are, the most valuable columns, just drop a lot of the other columns.
[2370.36 → 2375.76] Because then you're going to get way better performance out of maintaining the correlations on different subsets of the data set.
[2376.38 → 2385.14] And so we do kind of recommend it's like at that point, like maybe right before you would actually think about actually training your model is like once your data is pretty much in that good state around that ballpark.
[2385.22 → 2388.36] But it completely varies based off of use case.
[2388.44 → 2394.12] And we have some customers that the first stop is coming to Gretel because they want to immediately detectives on any PII that they could remove.
[2394.12 → 2396.50] So I'd say it definitely varies.
[2397.06 → 2397.16] Yeah.
[2397.28 → 2402.40] And I found that Gretel's Blueprints repo, which is seems pretty interesting.
[2402.40 → 2410.76] So I see a bunch of these examples boost massively and balance data set, create synthetic data from CSV or data frame, all sorts of examples.
[2410.76 → 2416.46] So if our listeners are interested in that, it looks like there are some notebooks and things in there that they can look at.
[2416.84 → 2420.18] We'll link that in our show notes for sure for people to take a look at.
[2420.18 → 2426.26] But maybe one thing to kind of start us thinking about, you know, things into the future.
[2426.42 → 2437.84] Where do you see are like the current challenges that are unsolved right now in terms of privacy and maybe data augmentation or synthetic data?
[2438.04 → 2443.58] What are some of those problems out there that you still see as open problems that need to be addressed?
[2444.26 → 2449.12] Yeah, I'd say there are a couple of problems and there are some semi-related.
[2449.12 → 2451.88] So one of them is its still a very nascent field.
[2452.78 → 2456.72] And there are a lot of tools out there and there's no magic bullet.
[2456.94 → 2457.08] Right.
[2457.10 → 2464.84] There's no way just to magically take a data set and completely create a version of it that is, you know, perfect and doesn't violate privacy.
[2464.84 → 2465.06] Right.
[2465.06 → 2468.36] There's always going to be a tradeoff between utility and privacy.
[2468.36 → 2472.48] And helping people understand that, I think, is going to be a huge challenge.
[2473.30 → 2479.52] And there's a ton of great research out there into how to kind of do that tradeoff between utility and privacy.
[2479.52 → 2489.72] And that's one of the things that we want to figure out is how to make that more obvious to engineers when they want to anonymize data or make data safe to share.
[2490.40 → 2491.84] It's like all these knobs you can tune.
[2491.98 → 2492.10] Right.
[2492.16 → 2501.62] And like, ideally, you don't want to go to a software engineer whose maybe a full stack engineer, and they have access to a production table, and they want to make a safe version of that data.
[2501.62 → 2509.06] You don't want to ask them to tune a bunch of like hyperparameters for a TensorFlow LSTM because they're like, whoa, I don't know what's going on here.
[2509.56 → 2514.18] But you might want to ask them to say, like, look, what is the tradeoff in utility and privacy that you should have here?
[2514.28 → 2515.54] Like, are you sharing this externally?
[2515.72 → 2516.86] Are you sharing this internally?
[2517.58 → 2519.94] Ask them those levels are.
[2520.08 → 2527.04] And then how can we infer what all those really nitty-gritty knobs are that need to be turned for the underlying model that's being built?
[2527.04 → 2537.22] Which kind of segues into the second problem I see is that making these tools generally available to software engineers everywhere is going to be a massive challenge.
[2537.38 → 2537.52] Right.
[2537.92 → 2549.46] And you can't ask every engineer to download a Python SDK and have like a crash course in machine learning to ask them to kind of build a safe version of their data set.
[2549.46 → 2557.44] And so how do we kind of bundle and package these capabilities in a way that engineers everywhere want to use as part of their day-to-day workflow?
[2557.68 → 2557.82] Right.
[2557.84 → 2564.58] If you look at companies that made things like dead simple, like Stripe made payments less scary because they have a ton of language bindings.
[2564.84 → 2567.02] It's really easy to integrate into your app.
[2567.08 → 2570.04] It's just like another API call that you make, and you don't think about it.
[2570.04 → 2574.22] And they're doing all this heavy lifting of like processing payments, which is a very complex thing.
[2574.76 → 2576.82] How do we kind of generalize down to that level?
[2576.82 → 2581.28] And that's kind of like definitely one of the big visions and missions that we have here at Gretel.
[2581.62 → 2593.88] So I'm kind of curious as you're describing that and like going back to the beginning of that second, you know, challenge that you're looking at in terms of it really strikes me the scale of what needs to happen here.
[2593.88 → 2600.98] So kind of beyond the specific challenges that maybe need to be solved and that maybe Gretel wants to address.
[2600.98 → 2607.54] The scale of this is definitely holding a lot of engineers back, you know, that are contending with this and can't get where they want to go.
[2607.54 → 2625.14] And if you're looking out over the next few years at kind of where this has to go as an industry and the need to broadly at scale be able to increase productivity in AIMS in general and this being such a core tenant of that, where do you see the industry going with that?
[2625.14 → 2637.20] You know, what needs to happen in the large to enable, you know, 10 times, 100 times as many engineers to be able to overcome this kind of problems and get productive with the problems they're trying to solve?
[2637.54 → 2642.08] You really got me thinking as you were answering those last two about how to get there from here.
[2642.20 → 2642.92] How do you get there?
[2642.92 → 2645.36] That is a great question.
[2645.84 → 2664.92] I think in my mind, and this is something that we even do inside of Gretel, is that I think one of the key things that has to get us there is that we just have more of a free form exchange of, I guess, ideas and talent among different types of developers and engineers that are out there.
[2664.92 → 2676.80] And when you look at like a lot of organizations, there's still, I guess, always a lot of segregation between like your platform engineers and your software engineers and your data engineers, and you have your machine learning engineers and your data scientists.
[2676.80 → 2681.56] And really, I think everyone needs to be able to do a little bit of everything.
[2681.56 → 2704.40] And like, how do you kind of build tool sets that allow, you know, a software engineer to easily take a look at the data, even though it's using some complex machine learning capabilities without having to go and request, you know, machine learning engineers spend tons of time doing it when, you know, that MLE should be maybe researching other parts that are like more vital to what the core mission is of that organization.
[2704.40 → 2710.66] And, you know, you see that there's been a lot of acceleration and like micro frameworks are building REST APIs.
[2710.90 → 2715.26] And so like that is, you know, a perfect example for how that allowed a lot of people to operationalize things.
[2715.26 → 2722.86] Right. Even as a data scientist, you could fire up, you know, model training and predictions and back it with a REST API and make it generally available.
[2722.86 → 2732.28] Like what's like the machine learning version of that like micro framework for REST API that allows software engineers to kind of quickly take use of all the capabilities that are out there that are up and coming with synthetic data.
[2732.28 → 2736.62] And we do that at our company now. We have a complete blend of backgrounds.
[2737.14 → 2746.26] And really, it's we don't want the whole like sequential motion of like, well, you know, this person builds the model and hands the model over to this person who builds this.
[2746.32 → 2748.72] Like we just want everyone to be able to kind of plug in and build.
[2749.34 → 2752.14] And so how do organizations move to that kind of methodology?
[2752.84 → 2755.72] Tearing down the walls there, so to speak, of those distinctions.
[2755.72 → 2761.06] Yeah, for sure. Well, John, I'm super excited about what Gretel is doing.
[2761.46 → 2768.40] And I really appreciate your detailed description of why these things are important and how you're solving some of these problems.
[2768.40 → 2775.26] I think it's really important. We'll make sure and link, like I mentioned, some of these links that we talked about in our show notes for people to check out.
[2775.42 → 2782.10] Please go and check these out. Try to generate some synthetic data with their tools and check out their platform.
[2782.10 → 2786.04] And yeah, thank you so much, John. I appreciate you taking time to talk to us.
[2786.46 → 2789.26] Awesome. It's been a pleasure to be on the show. And thanks for having me.
[2792.84 → 2795.22] Thank you for listening to Practical AI.
[2795.88 → 2799.54] If this is your first time, make sure you subscribe so you don't miss a thing.
[2800.08 → 2807.72] Head to practicalai.fm to subscribe or find us in Apple Podcasts, Spotify or wherever you listen to podcasts.
[2807.72 → 2812.68] And if you get value from the show, please do share it with a friend or a colleague.
[2812.86 → 2814.26] We appreciate you spreading the word.
[2815.08 → 2817.98] Practical AI is hosted by Daniel Whiten ack and Chris Benson.
[2818.32 → 2822.08] It's produced by Jared Santo and our music is provided by Break master Cylinder.
[2822.76 → 2824.76] We are brought to you by some awesome sponsors.
[2825.34 → 2827.78] Shout out to Vastly, Linde and Launch Darkly.
[2828.58 → 2832.52] That is our show. We hope you enjoyed it, and we'll talk to you again next week.
[2832.52 → 2862.50] We'll see you again next week.
