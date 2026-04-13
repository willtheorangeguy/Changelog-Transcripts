[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.62 → 20.24] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.36 → 25.00] And we're excited to share they now offer dedicated virtual droplets.
[25.00 → 28.94] And unlike standard droplets, which use shared virtual CPU threads,
[28.94 → 32.78] their two performance plans, general purpose and CPU optimized,
[33.32 → 35.98] they have dedicated virtual CPU threads.
[36.32 → 40.76] This translates to higher performance and increased consistency during CPU intensive processes.
[41.26 → 45.10] So if you have build boxes, CI, CD, video encoding, machine learning, ad serving,
[45.40 → 49.88] game servers, databases, batch processing, data mining, application servers,
[50.08 → 54.82] or active front end web servers that need to be full duty CPU all day every day,
[55.06 → 57.82] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.82 → 61.16] Pricing is very competitive starting at 40 bucks a month.
[61.44 → 65.46] Learn more, get started for free with a $50 credit at do.co slash Changelog.
[65.68 → 68.78] Again, do.co slash Changelog.
[78.48 → 83.88] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[84.32 → 86.06] productive, and accessible to everyone.
[86.06 → 90.96] This is where conversations around AI, machine learning, and data science happen.
[91.44 → 95.70] Join the community and Slack with us around various topics of the show at changelog.com slash community.
[96.24 → 96.86] Follow us on Twitter.
[97.00 → 98.46] We're at Practical AI FM.
[98.66 → 99.78] And now onto the show.
[99.78 → 113.20] Welcome to another fully connected episode of Practical AI, where my co-host Chris and I keep you fully connected
[113.20 → 116.48] with everything that's happening in the AI community.
[117.00 → 122.64] We'll take some time to discuss some of the latest AI news and dig into some learning resources
[122.64 → 125.78] to help you level up your machine learning game.
[125.78 → 134.50] I'm joined today, as usual, by my co-host Chris Benson, who is a principal AI strategist at Lockheed Martin.
[135.04 → 135.98] How are you doing, Chris?
[136.06 → 137.32] Welcome back from vacation.
[137.76 → 138.62] Thank you very much.
[138.64 → 139.40] It's good to be back.
[140.22 → 140.42] Yeah.
[140.88 → 148.08] So our listeners may not know, but you got to have a nice couple of weeks of vacation.
[148.08 → 152.20] And I hope you had some good rest with that.
[152.72 → 153.28] I did.
[153.54 → 157.90] I started as we were recording some previous episodes in the UK.
[158.18 → 161.04] But my wife is British, so she and my daughter joined me there.
[161.06 → 164.14] And we spent two weeks with family and friends and had a great time.
[164.26 → 164.44] Thanks.
[164.70 → 164.94] Thanks.
[165.10 → 165.44] It was good.
[165.62 → 169.38] It was nice just to walk away for two weeks and recharge the batteries.
[169.46 → 170.64] So I'm back, ready to go.
[170.64 → 171.60] Awesome.
[171.98 → 179.98] Well, you may or may not know, but during the last couple of weeks while you were enjoying vacation,
[180.82 → 190.12] the international AI politics world kind of exploded a bit, to say the least.
[190.12 → 195.16] So there's been some developments related to China and AI.
[195.16 → 201.86] AI, and that's definitely been kind of a central point in the news that's intersected the AI community.
[202.12 → 206.12] So I thought that might be good to dig into a bit today.
[206.20 → 206.64] What do you think?
[206.92 → 207.36] Absolutely.
[207.52 → 208.52] Let's jump into it.
[208.84 → 211.78] And I've been largely sequestered from the news.
[212.12 → 216.04] So I'll be coming in with bright-eyed and bushy-tailed hearing it for the first time.
[216.12 → 218.52] So let's dive in with what you got, Daniel.
[219.00 → 220.02] Sounds good.
[220.02 → 235.44] And I should say, I don't think either one of us consider ourselves complete or even semi-experts on international trade and politics and all sorts of things that factor into this.
[235.44 → 245.58] But kind of the bottom line is that AI and tech and this sort of interactions that have been happening between the U.S. and China,
[246.22 → 252.86] they're all kind of intertwined in this really weird and interesting and sometimes disturbing way.
[252.86 → 266.92] And so, yeah, maybe a good way to start out this discussion would just be to give a little bit of background on some of the elements that are coming into this.
[266.92 → 280.86] So we're eventually going to get to a point where we can talk about this AI blacklist that the U.S. came out with that kind of is blacklisting U.S. companies from doing business with certain AI companies in China,
[281.02 → 283.38] which is why we're talking about it on this podcast.
[283.62 → 285.66] But there's a bunch of things factoring into that.
[285.76 → 290.22] One of those is the Uyghur population in China.
[290.40 → 295.36] So the Uyghurs in China are an ethnic minority.
[295.36 → 301.94] They're a Muslim minority group in China, in the western part of China, in Xinjiang.
[302.62 → 307.72] And it's pretty well documented at this point.
[307.80 → 314.14] So we're not speculating here, but it's pretty well documented by the United Nations and others
[314.14 → 323.32] that there's been about a million of these ethnic Uyghurs in China that have been detained by China
[323.32 → 330.52] in re-education camps, what they call re-education camps, essentially detained.
[330.68 → 331.60] Have you heard about this?
[331.78 → 332.34] Totally have.
[332.72 → 336.30] That was, you know, before I went on vacation that had been going on for quite some time.
[336.54 → 343.60] And I think it's tragic as any time that you have a government clamping down on ethnic groups.
[343.96 → 346.86] You know, that's just, it's a sad situation.
[346.86 → 351.72] So, yeah, I think it's definitely something that we should all be aware of if we're not already.
[352.54 → 353.18] Yeah, definitely.
[353.40 → 358.52] I mean, there's, of course, a lot of human rights issues tied up in this.
[358.64 → 365.90] But it is interesting that all of this sort of stuff that's happening with the Uyghurs in China
[365.90 → 369.82] is very connected, actually, to AI and the tech side of things.
[369.82 → 376.78] So, of course, China has been taking kind of a harder line approach to dealing with these Muslim minorities.
[377.56 → 389.74] And part of that has to do with, like, the sophisticated surveillance technology that they're developing and deploying across this region.
[389.74 → 397.50] I think you've probably mentioned a couple of times on the podcast, you know, things related to facial recognition, if I remember right,
[397.68 → 401.02] and some of the ethics things tied into that.
[401.24 → 408.64] Yeah, I mean, China, in terms of surveillance of its own citizens, China, I mean, doesn't just lead the way globally.
[408.84 → 411.52] They are in a classification all by themselves.
[411.52 → 422.94] I recently, for a talk that I was giving that wasn't specifically about this, but I was looking at different cities around the world with surveillance and, you know, that had different –
[422.94 → 424.80] some tie into AI and some didn't and such.
[425.38 → 428.32] But, you know, China just dominated the list.
[428.40 → 434.48] And if you looked at the raw number of cameras in the regions, China just, you know, orders of magnitude more.
[434.76 → 440.04] So there's kind of China and then there's the rest of the world in terms of surveillance of this type.
[440.04 → 442.58] Yeah, it's increased, too.
[442.70 → 457.02] I think it was around, like, spring and June, I started seeing a pretty big surge in academic research papers that, I mean,
[457.86 → 463.42] you could imagine cases where maybe they wouldn't be used for surveillant Muslim minorities,
[463.42 → 476.24] but it was almost, like, completely obvious that these papers from Chinese researchers were geared towards upping the surveillance of these minority groups.
[476.52 → 481.02] I'm just pulling up a couple of those now that I had written down.
[481.12 → 482.52] So this one, it's an article.
[482.78 → 486.70] It's, like, facial feature discovery for ethnicity recognition.
[486.70 → 492.62] So it's not, like, really, like, hidden, you know, at all there.
[492.76 → 501.54] They even talk about constructing a data set, an ethnical group-faced data set, including Chinese, Uyghur, Tibetan, and Korean.
[501.54 → 507.86] And so these papers are not so subtle.
[508.32 → 518.50] And it's pretty clear that there's a lot of AI research that's actually going into this, which is pretty disturbing.
[518.50 → 529.82] I know there were a lot of people at that time kind of calling for peer review journals to up their, you know, ethics part of their review with these things.
[530.06 → 535.76] And I guess that gets into some conversations around censorship and other things with a lot of things factored in here.
[535.76 → 555.30] Yeah, it's kind of, you know, we've talked previously about, you know, the social credit system that is in place in certain parts of China and has been, you know, going through implementation over the last couple of years and continues to be implemented, starting in, you know, major cities such as Beijing and then moving out from there.
[555.30 → 570.22] And this is, you know, what we're seeing with the Uyghurs here is essentially kind of the worst case scenario being realized, you know, where you're specifically targeting an ethnic group, and you're using this advanced technology to enable that targeting.
[570.98 → 579.56] It's the world that we definitely didn't want to see coming about, you know, as lovers of these technologies that we talk about every week.
[579.56 → 585.98] Yep. And on top of that, so this is kind of a first slice of the complication pie.
[586.80 → 596.22] A second slice of that, of course, is the ongoing U.S.-China trade negotiations slash trade war stuff that's happening.
[596.70 → 605.44] I'm sure even while you were on vacation, you probably could not avoid hearing every once in a while someone talking about that at the pub or something like that.
[605.44 → 606.60] Oh, constantly.
[606.60 → 620.18] So it was, I mean, in the UK while I was there, I mean, everyone talks about obviously Brexit, but they also talk about the Americans and the Chinese and Trump and all of that.
[620.34 → 629.70] So, yeah, even though my wife largely tried to ban me from social media, news, you know, anything that was online to try to get me to focus on the family,
[629.70 → 634.20] which I tried to comply with as best as I possibly could, I think I succeeded.
[634.84 → 643.12] I still, you know, we would meet up with friends and family, and they would immediately say, Chris, what does the American take on this and that and the other?
[643.20 → 644.22] And I would try to explain.
[644.22 → 651.60] So, yeah, I mean, the U.S.-China trade war is one of those top things that everyone around the world is talking about right now.
[652.28 → 660.54] Yeah, and it's kind of in a state of going back and forth like, oh, we're going to put tariffs on soybeans and whatever,
[660.86 → 666.14] and then we're going to put tariffs on cranberries, and we're going to put tariffs on X, Y and Z.
[666.14 → 667.74] And so you got this back and forth.
[668.00 → 678.54] I think even today, at least at the time of this recording, there's trade negotiations going on between Trump and his team and the Chinese delegation in Washington.
[678.90 → 679.16] Correct.
[680.02 → 686.42] But, yeah, so that's kind of pie slice of complication, too.
[686.42 → 696.90] Then you've got all of this other stuff that's happening in places like Hong Kong, especially Hong Kong, where there's been these pro-democracy protests going on forever.
[697.12 → 702.76] Of course, facial recognition and surveillance has been, you know, a topic in that as well.
[703.02 → 713.86] I've seen pictures of, you know, protesters taking down this surveillance like polls or like posts that have cameras on them and stuff.
[713.86 → 725.76] So there's a lot of, so there's a pro-democracy protest element going on their tied in with China, but also an AI component as well.
[726.02 → 726.40] There is.
[726.68 → 736.94] Even yesterday, I was reading an article that Apple in the iPhone app store had removed an app that told protesters where police were.
[736.94 → 743.02] And the Hong Kong government, their position was you're putting police lives in danger.
[744.20 → 750.60] I sense, though, that the reality is quite the opposite in terms of who is actually in danger.
[750.90 → 752.54] So, yeah.
[752.82 → 756.78] Yeah, and there's, I mean, there are really a lot of elements of this.
[756.86 → 765.74] There's even the NBA, the Basketball Association, which I'm not a sports person, but the NBA is huge in China.
[765.74 → 766.50] I do know that.
[766.60 → 772.66] So they're involved in this now because of some of the things that a coach or manager had said.
[773.60 → 777.98] You know, the TV show South Park, they're kind of embroiled in this.
[777.98 → 794.06] So there's like all of these different elements where like the U.S. and China and AI and tech and trade are all sorts of coalescing into this weirdness, I guess.
[794.06 → 802.80] Yeah, I mean, it's definitely, you're definitely seeing, you know, we're seeing divided world in so many, so many areas.
[803.00 → 806.30] And this is becoming a rather extreme case of it.
[806.92 → 807.08] Yep.
[807.08 → 817.10] So that brings us to whenever it was, last week, I guess at this point, where we have this blacklist of AI companies coming out.
[817.10 → 827.04] So the U.S. Commerce Department said that it's adding a bunch of Chinese organizations and businesses to this list.
[827.04 → 840.98] But it includes at least eight primarily AI focused companies adding to this list called the Entity List for Acting Against American Foreign Policy Interests.
[840.98 → 861.04] It's a long name, but essentially what this does, like the mechanism or what it results in, are that it bars U.S. companies from selling technologies to these blacklisted entities, which obviously is a type of sort of sanctioned situation.
[861.04 → 881.48] Sure, absolutely. And I think the concern there is probably, you know, first and foremost, security issues on whether information is collected and passed back to China for use by the government or even by commercial entities that are maybe operating on behalf of the government.
[881.48 → 886.96] And then obviously there's intellectual property issues tied to it as well.
[911.48 → 914.62] Browse the web up to eight times faster than Chrome and Safari.
[915.20 → 917.16] Block ads and trackers by default.
[917.50 → 921.26] And reward your favourite creators with the built-in basic attention token.
[921.86 → 925.26] Yes, you heard that right. A real world use case for blockchain.
[925.88 → 931.26] Download Brave for free using the link in the show notes and give tipping a try on changelog.com.
[941.48 → 951.32] Okay, so there's these eight AI-focused companies that have been blacklisted by the U.S. government.
[952.04 → 966.54] And I kind of started, as I was thinking through this, I started thinking, first, I mean, it's probably interesting technology in a variety of ways that these companies are developing, whether it's being used for bad or good.
[966.54 → 973.90] I'm not totally sure. I mean, they are kind of all tied up in this complicated situation.
[974.86 → 991.56] And so I thought maybe, Chris, if you're up for it, maybe what we could do is just try to do a sort of blind taste testing of these companies and see essentially who they are, what they say they're developing,
[991.56 → 1003.94] what news sources are telling us that they're developing and kind of, I guess, get a pulse on, you know, a kind of state of the Chinese AI companies and what they're doing.
[1004.08 → 1013.24] And what is interesting tech-wise, maybe what is cool and positive, what isn't cool and positive, what everybody's saying.
[1013.48 → 1015.30] I don't know. Are you up for that game?
[1015.30 → 1024.88] I'm up for the game. So essentially, here in front of all of our friends listening, we're going to go to their websites and take a look at what they're saying.
[1025.80 → 1039.26] Yeah, definitely. So I'll kind of start us out. I thought maybe, so I'll go to a first one's website and kind of try to tell you what my impression is of what they're developing, what they have.
[1039.26 → 1039.90] Okay.
[1040.14 → 1057.54] And then maybe at the same time, you could look up a couple of news articles that you find, and we can see if they have the same impression of what they're doing or if there's a gap there or whatever we can learn. Sound good?
[1057.64 → 1059.18] It's a deal. What company you want to start with?
[1059.18 → 1076.82] All right. So the first one on my list that I had seen was called Hick Vision or Television. I'm not sure the pronunciation. This demonstrates that I'm really going into this blind. Sorry, I'm mispronouncing your company name. I do apologize.
[1076.82 → 1094.68] But they, so their website that I'm at is us. Hick or heekvision.com. And it looks like, like the big thing that I'm noticing when I go to this website is everything about cameras.
[1094.68 → 1109.04] So there are pages of like network cameras, like product selectors where you can select your camera. It's talking about apertures on cameras and advanced sensors and all sorts of things.
[1109.04 → 1127.76] But I see a kind of tab that's machine vision. And so that seems probably to be what's most relevant for us. So it says Hick Vision success and video surveillance market was established, blah, blah, blah.
[1127.76 → 1146.94] They have fast and accurate positioning guidance, dimension measurement and identification. And this is from the robotics division. They're kind of highlighting here an under vehicle surveillance system and machine vision cameras.
[1146.94 → 1167.88] So it looks like their kind of promoting this, the usage of this technology in a variety of ways, which do seem completely legitimate, right? Like if you're trying to see if there are bombs under your car, you could have this camera system under your car. I'm assuming that's what it's meaning to, to identify certain objects under a car.
[1167.88 → 1187.92] And they're also, to identify certain objects under a car. And they're also emphasizing the machine vision side of things in terms of like manufacturing. So installing these cameras in manufacturing places to trace certain objects through your factory, let's say, or to sort items in your factory.
[1187.92 → 1210.12] And so that's kind of the sense that they're really leading in machine vision, but emphasizing a lot of these industrial applications of the machine vision. I do see one example that's an unmanned aerial vehicle, so a drone.
[1210.12 → 1216.40] And they're emphasizing use of that and managing transportation infrastructure and equipment, so like highways.
[1216.40 → 1229.28] Gotcha. So while you were doing that, I googled and got a Bloomberg article called China's, and I'm probably going to butcher the name too, but heat vision has probably filmed you is what the article title is.
[1229.98 → 1239.68] Starts with a couple of bullets that says cameras are installed at army bases, airports, and schools. And then a second bullet says Trump administration concerned about Chinese spying tactics.
[1239.68 → 1259.38] And as I scanned down through this article while you were talking, there was one paragraph that kind of jumped out. It says, heat vision, which is controlled by the Chinese government and Dahl are leaders in the market for surveillance technology with cameras that can produce sharp full colour images in fog and near total darkness.
[1259.38 → 1289.36] They also use artificial intelligence.
[1289.36 → 1292.22] I don't have any insight into their activities or how they use it.
[1292.22 → 1304.76] But I could certainly understand why any government might be concerned about the potential for another government to be able to use these technologies to gain insight from an intelligence standpoint.
[1304.76 → 1317.72] Yeah, I mean, it is interesting because the sense I get from the website is very much like a manufacturing focus.
[1317.72 → 1334.16] Even, you know, some of the headlines are about industrial area scanning cameras and, of course, the traffic transportation management stuff.
[1335.16 → 1343.06] And so, yeah, at least on the English version of the site, that's kind of what they're emphasizing.
[1343.06 → 1355.28] Which, I mean, to be honest, that seems like a very legitimate use of the technology and probably something that Amazon and others are doing as well, right?
[1355.80 → 1358.18] Yeah, and it's interesting that you raise that.
[1358.18 → 1373.34] But, you know, a few months ago, there was a bit of a scandal with Amazon, specifically AWS, you know, and its services being used by, you know, for facial recognition being used by law enforcement here in the U.S. with our citizens.
[1373.34 → 1374.96] And it was a bit of an uproar.
[1374.96 → 1387.30] And Amazon turned around, I believe the product, by the way, was the recognition with a K product, and they stopped selling it to law enforcement is my understanding, if I recall correctly.
[1387.40 → 1387.96] It's been a few months.
[1388.34 → 1388.36] Right.
[1388.52 → 1394.06] But maybe they're using it in their warehouse for similar things that are being emphasized on this website, right?
[1394.10 → 1399.18] Like traceability or smart logistics is how they kind of term it.
[1399.18 → 1399.66] Totally.
[1399.78 → 1400.30] It's funny.
[1400.36 → 1409.34] As we talk about this, I spend a lot of time on the topic of AI ethics as part of my job and other tangential interests to that.
[1410.18 → 1416.92] And, you know, as I look at this, you know, it's really all about what is your attention here?
[1416.92 → 1425.14] If you're looking at this company, if they're using it for some of the use cases that you outlined, then, you know, that is beneficial.
[1425.38 → 1430.30] That is something that, you know, that increases the capability potentially.
[1430.92 → 1442.02] If they're using it for nefarious purposes, you know, it really comes down to intend and use case, you know, in terms of, you know, whether they're being fairly called out or not.
[1442.02 → 1442.74] Yeah.
[1442.74 → 1442.78] Yeah.
[1442.84 → 1454.62] And I think that, I mean, probably if they're advertising these things, and they have like use case stories around them, I imagine they are using the technology for manufacturing and logistics and those sorts of things.
[1454.62 → 1459.52] I guess the shadiness is probably the connection with the government, right?
[1459.70 → 1464.92] And, you know, what they potentially don't feature on the website.
[1465.48 → 1467.66] I think that's a fair statement.
[1467.66 → 1472.82] The concern, I think, that – and it's different.
[1472.94 → 1473.68] It's not universal.
[1474.10 → 1476.32] It's different between the U.S. and the U.K., I've noticed.
[1476.80 → 1486.88] The U.S. concern is largely on, you know, kind of worrying about the nefarious issues and intent.
[1487.34 → 1494.18] The U.K., on the other hand, has, you know, largely said they are absolutely going to continue to do business with China.
[1494.18 → 1505.12] And, you know, they have, you know, outside China, you know, London in general – London is one of the most survived cities in the world with their CCTV system.
[1505.88 → 1508.82] And they are a lot less worried about it there.
[1509.00 → 1511.16] It's an interesting perspective shift.
[1512.02 → 1512.40] For sure.
[1512.40 → 1512.44] Sure.
[1513.08 → 1522.30] So let's go to candidate number two, company on the blacklist number two that we're going to look into.
[1522.50 → 1525.76] And this one's called fly Tech.
[1526.54 → 1528.90] I'm pretty sure that's the correct pronunciation.
[1529.24 → 1531.04] I don't know how else you would say that.
[1531.18 → 1532.16] So that one's easier.
[1532.54 → 1532.60] Okay.
[1533.24 → 1533.74] fly Tech.
[1533.74 → 1535.86] Do you want to take a look at their website?
[1536.72 → 1545.92] And maybe we can flip-flop, and then I'll kind of see what I can find elsewhere on the internet.
[1546.16 → 1546.42] Okay.
[1546.54 → 1547.64] That is fine.
[1547.86 → 1550.22] So I have found their website.
[1551.00 → 1554.30] This is all in Chinese for the moment.
[1554.54 → 1555.74] All in –
[1555.74 → 1558.56] Ah, you got to get some Google Translate going.
[1558.72 → 1559.12] Yeah.
[1559.30 → 1560.20] You open that in Chrome?
[1560.20 → 1563.86] I did open it in Chrome, but it didn't automatically translate.
[1564.18 → 1567.50] So maybe we'll flip-flop for the moment so we don't waste people's time.
[1567.64 → 1570.84] And then I'll take – I'll do the article Googling.
[1571.00 → 1571.78] Sorry about that.
[1572.22 → 1581.16] And I would like to take this time as a proud data scientist with SIL International to highlight the world's language problems.
[1581.26 → 1581.66] Yes.
[1581.80 → 1584.20] That are still yet to be solved.
[1585.10 → 1585.58] Yeah.
[1585.58 → 1589.58] So I did get the translation option there.
[1590.58 → 1597.22] So I got the translation option, and it's telling me – let's see.
[1597.26 → 1598.16] I'm scrolling down.
[1599.00 → 1610.08] There's a bit about education on the front, and I see this sort of odd-looking robot thing, like a robot guy.
[1610.08 → 1620.22] They're talking about internet plus government affairs, solve the roundup operation between civil affairs departments.
[1620.22 → 1632.10] They're talking about an AI lab, all-around application of government and industry, intelligent business, smart tube business.
[1632.10 → 1638.56] I'm assuming maybe that has to do with trains or something like that.
[1638.56 → 1642.24] But they have this – I don't know.
[1642.30 → 1652.64] They have this thing called Hyperbrain or Hyperbrain Project, which is a laboratory for speech and language information processing.
[1652.80 → 1653.74] That sounds pretty cool.
[1655.12 → 1665.56] Cognitive intelligence system based on a humanoid neural network based on the key projects of the 800 people.
[1665.56 → 1673.64] So this is all a translation, but it seems like they're at least doing something with machine intelligence language.
[1674.50 → 1684.30] Looks like they've got some partnerships with malls and shopping and some developer toolkit sort of stuff.
[1684.60 → 1690.10] So that's pretty much what I'm – I may be butchering all of that because I'm working off of a translation.
[1690.10 → 1694.96] But right at the top it says empower the world with AI.
[1695.50 → 1695.98] Gotcha.
[1696.82 → 1698.06] Seems pretty ambitious.
[1698.42 → 1698.88] It does.
[1699.08 → 1700.86] I found an article here.
[1701.42 → 1703.50] It's technologyreview.com.
[1703.88 → 1707.40] Why 500 million people in China are talking to this AI.
[1707.40 → 1718.92] And it was funny when I pulled in just as you were starting to get into looking over their webpage, when I heard fly Tech, I just assumed it was a drone company.
[1719.86 → 1720.02] Yeah.
[1720.18 → 1721.12] Not being familiar with it.
[1721.26 → 1721.92] You know, fly Tech.
[1722.02 → 1727.38] I just came from the first Alpha Pilot race, you know, going back to a recent episode where we talked about Alpha Pilot.
[1727.50 → 1728.24] So I was thinking that.
[1728.24 → 1731.90] So I was rather surprised to suddenly realize it was language-based.
[1732.60 → 1747.16] They talk in this article about a bunch of things including that they have a developer platform called the fly Tech Open Platform, which provides voice-based AI technologies to over 400,000 developers in various industries.
[1747.88 → 1748.00] Yeah.
[1748.08 → 1750.78] I see that developer tab on the website.
[1751.06 → 1751.20] Yeah.
[1751.20 → 1753.56] They're valued in U.S. dollars.
[1753.72 → 1756.00] They'd be valued as a $12 billion company.
[1757.28 → 1761.90] International operations, you know, looks interesting.
[1762.08 → 1762.82] Looks a lot like.
[1763.00 → 1763.14] Yeah.
[1763.32 → 1772.02] I mean, honestly, a lot of the things that they mentioned are personally interesting to me in terms of the voice and language technology, for sure.
[1772.62 → 1779.88] Which reminds me, and I'll say this out loud so that all of our listeners here, we've got at some point to interview you about that.
[1779.88 → 1784.52] Because for those listeners who don't know, Daniel is quite the expert in that area.
[1784.72 → 1786.12] So upcoming episode.
[1786.26 → 1789.04] I've now committed you to in front of our entire audience.
[1789.18 → 1789.46] All right.
[1789.82 → 1793.26] We can definitely arrange that sometime.
[1794.72 → 1794.94] Yeah.
[1795.34 → 1806.68] Did you see anything in those articles about this whole, like one of the things I see them keep emphasizing here is like education and like these child toy robot things.
[1806.68 → 1807.00] Yeah.
[1807.20 → 1807.60] Yeah.
[1807.70 → 1810.04] There's a picture at the top.
[1810.16 → 1812.08] Let me delve into that here.
[1812.22 → 1814.28] I think that's what we're getting into.
[1814.86 → 1816.00] What do you know about that?
[1816.16 → 1816.40] Well, I.
[1816.60 → 1817.34] I don't know.
[1817.46 → 1819.92] It just says children's intelligence.
[1820.48 → 1824.06] And then I'm trying to open up the page, but it's not letting me go there.
[1824.36 → 1825.02] Hopefully I'm not.
[1825.12 → 1826.14] I'm not blacklisted.
[1826.82 → 1826.94] No.
[1827.32 → 1831.82] It's talking about a lot of different uses, but I haven't seen the children one yet.
[1832.38 → 1832.76] Interesting.
[1832.76 → 1833.10] Yeah.
[1833.18 → 1840.52] I see machine translation, smart office, intelligent transfer, which I'm not sure what that is.
[1840.60 → 1849.50] Audio, children's intelligence, and learning or education.
[1850.26 → 1853.24] They have a voice assistant for drivers.
[1854.06 → 1854.78] And I will not.
[1854.88 → 1860.66] I'm not going to try the Mandarin word for this, but the English translation is little flying fish.
[1861.24 → 1861.72] Nice.
[1861.72 → 1862.40] There you go.
[1862.46 → 1863.12] Very quaint there.
[1863.66 → 1863.88] Cool.
[1864.26 → 1868.72] Well, I mean, it seems like they're involved in a lot of cool stuff.
[1868.86 → 1874.12] I don't know if they're, it seemed like one of the first things that came up with the last one,
[1874.52 → 1879.32] the Hick vision, was the very close connection with the government.
[1879.52 → 1880.80] Yes, it was.
[1880.80 → 1889.72] So just speaking as someone who doesn't know these companies, I could see the possibility
[1889.72 → 1894.00] for ominous overtones on the first company we looked at.
[1894.08 → 1899.04] This one seems a lot friendlier, a lot more child and consumer oriented.
[1899.04 → 1904.50] It certainly doesn't come off with those ominous overtones.
[1905.00 → 1906.50] So who knows?
[1906.50 → 1908.00] Well, let's see.
[1908.52 → 1916.32] Let's see if we continue that trend into company number three, which is Meg vi or Meg vi.
[1917.02 → 1918.06] Maybe one of those.
[1918.22 → 1920.66] It's M-E-G-V-I-I.
[1920.94 → 1921.18] Okay.
[1921.18 → 1924.60] So why don't you take the website this time around?
[1924.96 → 1927.28] So long as it has the English because I don't have the translation button.
[1927.38 → 1928.36] So we'll try it out here.
[1928.96 → 1930.54] See if you got that.
[1930.54 → 1930.94] There we go.
[1931.00 → 1931.64] I do.
[1931.88 → 1933.12] I have an English version.
[1933.82 → 1935.54] Power of Humanity with AI.
[1936.22 → 1936.36] Okay.
[1936.58 → 1937.08] Ambitious.
[1937.26 → 1937.48] There.
[1937.68 → 1938.62] Power of Humanity.
[1938.72 → 1938.98] I know.
[1939.20 → 1940.54] Let's not dream small.
[1942.30 → 1944.56] They have a proprietary deep learning framework.
[1944.56 → 1949.00] They gather top tier AI talent and they integrate.
[1949.10 → 1955.52] So far, this first page is very typical of what you see with companies touting AI stuff.
[1955.52 → 1961.54] Sounds like a, I mean, Google brain open AI sort of feel.
[1961.68 → 1962.48] Yeah, it does.
[1962.80 → 1969.88] They describe themselves just as a world-class AI company with core competency in deep learning.
[1971.72 → 1972.94] Full stack solutions.
[1972.94 → 1978.78] It kind of feels Impish, you know, kind of like a bunch of corporate talk, you know, that.
[1979.16 → 1979.76] Somewhat vague.
[1979.92 → 1980.90] Yeah, somewhat vague.
[1981.00 → 1982.48] I'm so sorry to you Beers.
[1982.54 → 1983.90] I really wasn't trying to insult you.
[1984.06 → 1985.32] I just apologize there.
[1985.38 → 1986.88] IBM is doing a lot of cool stuff.
[1987.14 → 1987.46] They're doing.
[1987.56 → 1990.88] Hopefully we'll have someone from there on soon we're talking to.
[1991.26 → 1991.74] Okay.
[1992.94 → 1996.08] Leadership team of young, they're all men.
[1996.40 → 1997.44] They're all young men.
[1997.44 → 2004.40] Um, they all could be, they look the age of my own grown children.
[2004.72 → 2007.68] So, um, now I'm feeling ancient.
[2007.82 → 2008.18] Okay.
[2008.18 → 2016.66] Um, yeah, well, I'm looking, so I'm looking at a couple articles from Wired and, uh, TechCrunch.
[2017.08 → 2028.70] Um, it looks like one of the big news recently was, um, that the company had an IPO, um, public listing on the Hong Kong stock exchange.
[2028.70 → 2039.40] Um, but both of these articles that, that I'm looking at, um, definitely have the, the more ominous overtone, uh, probably similar to the first one.
[2039.40 → 2045.90] It's a very, uh, very big focus in both articles, um, which we'll link in the show notes for sure.
[2045.90 → 2055.44] All of these things we're talking about, but much more focused on facial recognition, uh, be behind the rise of China's facial recognition giants.
[2055.44 → 2066.48] Um, so, uh, this, this is saying that Meg V, um, is, is one of the four Chinese AI startups specializing in facial recognition.
[2066.48 → 2076.00] So they specifically call that out as their specialty and valued at more than 1 billion, which is, uh, pretty crazy.
[2076.00 → 2082.62] So that would qualify them, this is saying qualifying them as a, as a unicorn in, uh, Silicon Valley speak.
[2082.62 → 2098.70] So a unicorn, uh, obviously, uh, promoting a lot of deep learning technology, but seems like, uh, that 1 billion and their IPO and most of their value is related to facial recognition and surveillance.
[2098.70 → 2099.34] Yep.
[2099.46 → 2106.68] Um, it says Meg V does investors include Alibaba and financial and the Bank of China.
[2106.68 → 2115.46] Um, which I think if, I mean, I'm no expert on those companies, but I think that's a fairly close tie to the Chinese government.
[2115.62 → 2115.90] Yep.
[2116.20 → 2117.66] Um, probably so.
[2118.04 → 2122.76] Interestingly, I don't think the website comes off quite as ominously as I've been scrolling around through it.
[2123.12 → 2127.80] Um, it really does have that very corporate-y, uh, feel to it.
[2127.80 → 2145.62] Um, uh, you know, we're, and, and a little bit, you know, we're rather than, than talking about the applications, they talk about their amazing deep learning capabilities, and they talk about, you know, smart cities and a lot of the normal buzzwords that you find with American, um, Silicon Valley companies.
[2145.62 → 2152.78] So, um, it, it sounds, uh, I mean, they're coming off definitely more research focused.
[2153.14 → 2153.92] They are definitely.
[2154.20 → 2163.60] It seems like the maybe the other two kinds of, uh, to be competitive with like a Google brain or, or open AI or something like that.
[2163.76 → 2163.98] Yep.
[2164.00 → 2164.54] I would agree.
[2165.28 → 2165.84] Cool.
[2165.84 → 2175.32] Well, let's, uh, um, you know, say that Meg V, uh, definitely has some, some interesting, uh,
[2175.32 → 2176.88] interesting things going on.
[2177.02 → 2182.10] Um, but maybe there's, there's a sort of ominous overtone that that's coming through.
[2182.10 → 2183.02] Are you getting that?
[2183.26 → 2184.26] Uh, possibly so.
[2184.32 → 2184.56] Yeah.
[2184.56 → 2186.62] Especially from what you read, from what you mentioned.
[2187.14 → 2187.82] All right.
[2187.82 → 2192.20] So that brings us to our last contestant today.
[2192.90 → 2202.96] Uh, I don't know if I should be, be phrasing this as a, uh, as a game, um, because it's quite serious stuff, but I don't know what else to do.
[2203.06 → 2203.90] Let's have fun with it.
[2204.26 → 2204.72] All right.
[2204.72 → 2205.20] Sounds good.
[2205.20 → 2206.96] I'll, I'll take the website this time around.
[2207.14 → 2215.70] Um, this one is, uh, yeet, uh, yeet, um, not again, not sure, um, on the pronunciation.
[2216.06 → 2217.66] Y-I-T-U.
[2218.16 → 2224.68] Um, hopefully some of our, our listeners maybe correct us on, uh, some of these things that I'm sure we're getting wrong.
[2225.80 → 2227.14] But here, okay.
[2227.28 → 2229.22] So, um, I'm at yeet.
[2229.34 → 2231.42] I actually like their website quite a bit.
[2231.42 → 2238.02] Um, it's much more appealing design-wise to me than the, uh, the previous ones I was looking at.
[2238.02 → 2240.20] Um, so great job there, yeet.
[2240.20 → 2253.56] Um, but it looks like they're also, um, so, seems like a very, uh, similarly Google brainy, um, research type website.
[2253.56 → 2259.64] Um, they say that they're developing technologies that are driving change in the world.
[2259.64 → 2277.46] Um, and those include, uh, proprietary, um, full-stack technology in-depth explorations into fundamental AI technologies, including computer vision, speech recognition, natural language comprehension, and human-machine interactions.
[2277.46 → 2290.88] Um, uh, they talk about being champions in the face recognition vendor test, um, which is apparently a gold standard for global industrial applications.
[2290.88 → 2312.88] Um, they talk about, um, uh, management technologies, uh, hundred million scale data traffic, uh, unlocking multi-industry scenarios for intelligent cities, um, and having world-class technology talent.
[2312.88 → 2329.60] Um, so, there's definitely a, uh, sort of, we're, we're exploring all the AI things feel, plus that sort of, uh, very clear call-out that they are the best in the world at facial recognition.
[2329.90 → 2331.88] Um, there's, there's no hiding that.
[2332.06 → 2332.26] Yeah.
[2332.38 → 2334.58] These are the these are the best.
[2334.86 → 2337.62] And, uh, I, I see that, I, I saw two articles.
[2337.62 → 2340.94] One, they, it talks about that they are seeking an IPO.
[2340.94 → 2341.88] That's from Bloomberg.
[2342.56 → 2346.74] Um, it was a recent one on September 3rd, just over a month ago as we record this.
[2347.12 → 2359.56] Um, and then, but the, the other one is a CNBC article, uh, and the title is, these Chinese facial recognition, this Chinese facial recognition startup can identify a person in seconds.
[2359.56 → 2362.32] And, um, it starts off with key points.
[2362.34 → 2363.44] They're world champions, man.
[2363.52 → 2364.32] Apparently so.
[2364.32 → 2370.60] It starts off with the points that, uh, China plans to be a global leader in AI by 2030, which is, we've all known for a while.
[2370.94 → 2377.22] Uh, and the market for facial recognition alone is expected to be 9.6 billion by 2022.
[2377.96 → 2383.00] Um, it, the next bullet is a little bit scary, but we, it's something we already know.
[2383.04 → 2389.54] It's China's facial recognition database includes nearly every one of China's 1.4 billion citizens.
[2390.22 → 2398.54] Um, and then, um, it just talked about the fact that they had wide recognition, uh, for their facial scan platform.
[2398.54 → 2404.38] Um, and so, uh, a little bit of an ominous overtone before you even get into the article right there.
[2404.38 → 2412.20] Um, now this is CNBC and it, you know, and potentially it's a an American, uh, take, uh, as such on that.
[2412.20 → 2421.30] But, uh, yeah, definitely feels, uh, like, you know, a little bit closer to, uh, supporting government aims, uh, social currency such as that.
[2421.30 → 2421.70] Yeah.
[2421.86 → 2422.34] Yeah.
[2422.44 → 2434.78] One, uh, one interesting thing that I'm noticing here on, on this one is, uh, I, I mean, similar to some of the other ones, they're emphasizing some of the non-facial recognition stuff that they're doing, which sounds amazing.
[2434.78 → 2447.30] I mean, uh, there's like a cancer detection tool, um, improving diagnosis of sick children, pushing the boundaries on Mandarin speech recognition, um, really cool stuff.
[2447.30 → 2455.52] And, and one interesting thing is that some of this, like the sick children one, they talk about, uh, Chinese U.S. um, joint development.
[2455.52 → 2467.54] And so, uh, there's definitely, uh, uh, international flair to, to some of this research, which they're, uh, which they're highlighting, which, um, yeah, a lot of that sounds, sounds really cool.
[2467.54 → 2475.06] And I, I don't doubt that, um, you know, it's not like we can't, I can look at the link to these papers, right?
[2475.06 → 2480.22] They're publishing papers on, on the, uh, cancer stuff and, and other things.
[2480.22 → 2485.66] So it's definitely not like they're, they're just falsifying what they're doing, right?
[2485.74 → 2489.10] But, but facial recognition and that surveillance is a piece of it.
[2489.78 → 2489.88] Yeah.
[2489.98 → 2493.80] And, and, you know, that, that once again comes back to what is their intent?
[2494.00 → 2498.30] You know, what are they trying to, to do with it across their use case spectrum?
[2498.88 → 2510.10] Um, and, you know, are, and probably many are very reasonable use cases, uh, you know, but are they, you know, it's, there are some, this, this article certainly, uh, leaves that almost overtone.
[2510.10 → 2524.36] In terms of, um, how it might be supporting the, the, uh, the social currency system, uh, in China, which, which obviously, you know, there's a there's a value difference right there, uh, you know, between Western values and Eastern values, at least there in China.
[2524.76 → 2529.80] Um, that's the kind of thing that would scare, uh, most Westerners and in a variety of Western countries.
[2529.80 → 2544.00] I think, um, even in, even in places like, like in the UK and London where people expect to be survived, I think they would expect that the way the information is being used is, is not, not so nefarious.
[2544.00 → 2560.32] Um, so, uh, it's, it's, it's interesting to see, uh, as we look at global trade, how we're going to reconcile some of these differences in terms of how we approach, um, society, how we approach, uh, uh, business and trade.
[2560.32 → 2570.76] Um, and I think, uh, some of these, these companies, you know, they, they may be, uh, acting completely appropriately based on, on, uh, an objective standard.
[2571.14 → 2584.82] Um, I think it would, I think one of the scary things certainly for the, uh, the American perspective is just the ability to verify that the ability to understand that they're dealing with a vendor that's, that does not have an ulterior motive and stuff.
[2584.82 → 2592.92] Uh, whether that put, would deserve to put them on the list here or not, I, I have no insight into that, but, um, it's, uh, it's a tough thing.
[2592.92 → 2595.70] And I think, I don't think we're anywhere near, uh, solving that.
[2596.26 → 2596.70] Yeah.
[2596.76 → 2606.54] I think, I mean, if I was to summarize kind of what I think I've seen in going through this exercise, which again, it's just a brief exercise.
[2606.54 → 2614.58] So, you know, I'm sure there are many more elements of this that we don't know about, but if I was to kind of summarize my,
[2614.58 → 2627.02] where my mind is at on it is, you know, on the positive side, these AI companies and researchers in China are without a doubt, top-notch.
[2627.02 → 2627.62] Absolutely.
[2627.94 → 2642.98] And, uh, are doing some amazing things in, in computer vision, but also outside of computer vision in places like language and, and other, uh, areas like chat and dialogue and, and voice.
[2642.98 → 2652.20] Um, and so there's, there's no question that they are producing some, some amazing research findings and advancing those fields.
[2652.20 → 2664.70] Um, but there's kind of always this undertone of like, well, how, how much are these companies involved with the Chinese government?
[2664.70 → 2676.46] And how much of their funding is coming from these projects that are explicitly, um, targeting and marginalizing these, uh, you know, Muslim minority and other communities.
[2676.46 → 2692.36] So there's kind of always like, yes, we know you're innovating in all of these areas, but, um, there's kind of this shadow cast on a lot of that, which is unfortunate in terms of, uh, you know, how much of it is being used for, for those purposes.
[2692.36 → 2695.88] So that, that's kind of where, where my mind is at, I guess.
[2696.40 → 2696.48] Yeah.
[2696.50 → 2713.80] I think there's a there's a real cultural difference in terms of, um, of knowing, you know, you know, as someone who is working in, in the American defence industry, it is, you, you generally know whether a company, uh, in this industry has a direct government die or not.
[2713.80 → 2723.34] You may not know the specifics of the work that they do, but, um, we don't tend to, to leave that, uh, so ambiguous, uh, in terms of your understanding.
[2723.34 → 2725.40] You know, I work for Lockheed Martin.
[2725.94 → 2731.26] Everybody knows that Lockheed Martin does work with the, with the U.S. government and other governments.
[2731.42 → 2731.98] It's not hidden.
[2732.12 → 2733.30] It's in the news all the time.
[2733.30 → 2736.30] And so you kind of know what you're getting there.
[2736.48 → 2752.38] I think the challenge in, in, uh, certainly American minds and maybe, maybe Western minds at large is the fact that the relationships are not, are not so obvious, um, in, in, with China and the companies between the government and the companies that are there.
[2752.38 → 2770.38] Um, and in my very biased viewpoint, I would argue that, that if they were able to establish more clearly, uh, transparently, uh, what their business with their own government is, if any, that would help, uh, that would help alleviate many of the concerns that other countries have.
[2770.38 → 2777.72] Because obviously no, no nation state is going to want to subject itself to potential spying, uh, by any other country.
[2777.72 → 2798.22] And that's not even specific to these cases, but, um, I, I think transparent, this is one of those things where having that relation, if you, whether you have a relationship or don't have a relationship between government and, uh, and business being transparent about the existence or, or, or, or lack of one, uh, would, would certainly alleviate concerns around the world.
[2799.06 → 2799.54] Sure.
[2799.68 → 2800.56] Well, well put.
[2800.74 → 2807.22] And, uh, um, I think that this whole, uh, episode has been a learning experience for me.
[2807.22 → 2809.40] Hopefully it has for our listeners as well.
[2809.62 → 2819.78] Um, we will put all the links that we accessed, um, into our show notes so that you could do, uh, you know, recreate our experiment if you like.
[2820.16 → 2825.32] Um, before we close out for the day, I just wanted to mention on a completely different subject.
[2825.72 → 2829.64] Um, TensorFlow 2.0, uh, that happened.
[2830.20 → 2835.00] And, um, you know, we always like to share a few practical learning resources.
[2835.00 → 2851.16] Hopefully again, this episode has been a learning, uh, resource in, in some ways, but, um, on the practical programming side, um, uh, Francois Chalet, uh, created this really nice, um, uh, TensorFlow 2.0 and Keras overview.
[2851.16 → 2863.82] Um, so, uh, we'll link that in the notes if you're, if you're wanting to keep up with that, uh, TensorFlow 2.0 stuff and, and Keras, um, that's a great place to, to start.
[2864.06 → 2866.10] Um, so I, I definitely want to take a look at that.
[2866.32 → 2866.72] Absolutely.
[2866.72 → 2870.70] And I want to invite all of our listeners, uh, to engage us.
[2870.74 → 2875.96] So many of you already do engage us in our Slack community, engage us on Twitter, uh, on LinkedIn.
[2876.68 → 2880.98] Um, today was an experiment as an episode and, uh, we enjoyed ourselves.
[2881.22 → 2883.02] Uh, let us know whether you liked it.
[2883.14 → 2884.98] If you didn't like it, let us know that too.
[2885.36 → 2888.92] Um, we're going to continue to experiment with the show and try different things.
[2888.94 → 2892.02] Um, and a lot of the things that we try to come from your comments.
[2892.02 → 2897.58] So, uh, don't hesitate to let us know what you think and make suggestions and, uh, thank you for listening again.
[2898.30 → 2898.78] All right.
[2898.84 → 2899.92] We'll talk to you soon, Chris.
[2900.22 → 2900.82] Take care, Daniel.
[2903.28 → 2903.76] All right.
[2903.80 → 2906.42] Thank you for tuning into this episode of Practical AI.
[2906.66 → 2911.78] If you enjoyed this show, do us a favour, go on iTunes, give us a rating, go in your podcast app and favourite it.
[2911.86 → 2917.02] If you are on Twitter or social network, share a link with a friend, whatever you got to do, share the show with a friend if you enjoyed it.
[2917.02 → 2920.00] And bandwidth for Change Log is provided by Vastly.
[2920.12 → 2921.02] Learn more at Fastly.com.
[2921.02 → 2924.96] And we catch our errors before our users do here at Change Log because of Rollbar.
[2925.24 → 2927.54] Check them out at Rollbar.com slash Change Log.
[2927.88 → 2930.38] And we're hosted on Linde Cloud servers.
[2930.72 → 2932.34] Head to Linode.com slash Change Log.
[2932.44 → 2932.88] Check them out.
[2932.96 → 2933.80] Support this show.
[2934.20 → 2937.38] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2937.86 → 2939.90] The music is by Break master Cylinder.
[2940.28 → 2943.74] And you can find more shows just like this at ChangeLog.com.
[2943.74 → 2945.86] When you go there, pop in your email address.
[2946.18 → 2952.18] Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2952.60 → 2953.36] Thanks for tuning in.
[2953.52 → 2954.28] We'll see you next week.
[2954.28 → 2961.22] Albany Attorney
