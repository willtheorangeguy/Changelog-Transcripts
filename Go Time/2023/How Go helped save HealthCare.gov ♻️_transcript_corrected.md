[0.00 → 16.34] Welcome to Go Time, your source for diverse discussions from all around the Go community.
[16.70 → 20.42] This is a rebroadcast of one of my favourite Go Time episodes.
[20.78 → 23.86] Paul's healthcare.gov rescue story is epic.
[23.86 → 27.42] I drop one of the most unpopular opinions of all times.
[27.42 → 30.68] And Matt channels Captain Jack Sparrow to read some Go docs.
[31.22 → 32.78] I mean, come on, that's pretty good, right?
[33.14 → 35.30] Thanks to our partners at Vastly for their support.
[35.68 → 38.82] Go Time downloads fast globally because Vastly is fast globally.
[39.08 → 40.56] Check them out at Fastly.com.
[40.90 → 45.20] And to our friends at Fly, deploy your app servers and database close to your users.
[45.48 → 46.70] No ops required.
[47.12 → 49.14] Learn more at fly.io.
[49.44 → 50.92] Okay, here we go.
[57.42 → 60.12] Hello there and welcome to Go Time.
[60.52 → 63.96] I'm Matt Ryder, and I've just pushed to production.
[64.64 → 69.46] Today on Go Time, we're talking about caringabouthealthcare.gov.
[69.84 → 76.76] And actually, I think why simplicity matters, especially so as the stakes get higher.
[77.18 → 78.04] Apologies to any vegans.
[78.42 → 81.82] On today's show, we have Johnny Portico.
[82.08 → 82.62] Hello, Johnny.
[83.28 → 84.42] Hello, I'm a carnivore.
[84.42 → 85.96] Fair enough.
[86.48 → 89.04] You don't have to state your preference, but you can.
[89.04 → 89.72] Oh, okay.
[90.78 → 94.20] We're also joined, it's Jared Santo from the Changelog.
[94.28 → 94.76] Hello, Jared.
[94.94 → 95.56] That's correct.
[95.70 → 96.16] Omnivore.
[96.64 → 97.32] I'm an omnivore.
[97.68 → 98.04] Great.
[98.18 → 100.16] Does that mean you eat everything?
[100.82 → 101.48] Just anything.
[101.92 → 102.74] Yeah, great.
[102.82 → 103.42] Happy to be here.
[105.38 → 108.60] You don't care how big the menu is, you will go to that place.
[108.90 → 109.40] That's right.
[109.78 → 110.00] Yeah.
[110.38 → 110.88] Supersize me.
[110.88 → 116.58] And we're also joined by a special guest today, who you may remember from a lightning
[116.58 → 118.46] talk back at Gopher Con 2015.
[119.10 → 120.32] It's Paul Smith.
[120.56 → 121.14] Hello, Paul.
[121.96 → 122.70] Hi, everybody.
[123.22 → 123.84] Glad to be here.
[124.42 → 124.82] Welcome.
[125.02 → 126.28] Thanks for joining us.
[127.06 → 129.24] Yeah, I'm excited to talk with you all.
[129.44 → 130.40] Thanks for inviting me.
[131.06 → 131.26] Yeah.
[131.38 → 135.58] Well, so you've got a very interesting story, but maybe before we jump into it, you could
[135.58 → 137.82] just tell us a little bit about your technical background.
[137.82 → 140.74] How did you first get into computers in the first place?
[141.10 → 141.24] Sure.
[141.84 → 148.92] Well, I think it's actually somewhat of a common story for boys growing up in the 80s, getting
[148.92 → 153.30] a Vic-20, Commodore Vic-20, Commodore 64 kind of plopped in your lap.
[153.88 → 160.28] Sadly, all too not common for girls in that time, which is something of a tragedy.
[160.28 → 167.40] But yeah, typing basic programs in, machine code programs out of magazines, spending a
[167.40 → 168.74] lot of time with my Commodores.
[169.00 → 171.02] I think we had an Amiga at one point, too.
[171.90 → 177.62] And then in high school, I got an internship in the early 90s at a local laboratory.
[177.62 → 182.52] They were studying biology laboratory, and they actually had a mathematical bent to it.
[182.52 → 190.92] So they were studying DNA protein binding sites and the information conservation that occurs
[190.92 → 192.76] there when protein binds to DNA.
[193.70 → 195.80] And kind of molecular machines kind of thing.
[196.08 → 201.62] Anyway, that was my first exposure to Unix, and I wrote Perl and C.
[201.62 → 208.92] And also the nascent web was just getting off the ground around that same time, 94, 95.
[209.76 → 214.42] So yeah, so I've been basically typing into computers most of my life.
[215.00 → 216.74] How much of that's been doing Go?
[217.02 → 219.60] How much actual Go code do you write?
[219.60 → 224.64] Well, I first learned about Go as soon as it launched in, I think, 2009.
[225.48 → 228.02] And it seemed immediately appealing to me.
[228.32 → 232.92] I had been writing Python primarily for work as my job.
[233.10 → 238.38] So at that point, I had been working professionally for about 10 years, mostly web application development.
[238.66 → 240.90] Pretty standard stuff of that era, especially.
[241.56 → 245.56] So database-backed, relational database-backed web applications.
[245.56 → 249.02] And I loved Python, and I still think Python's a great language.
[249.02 → 252.32] But I remember that Go felt perfect right away.
[252.52 → 253.94] It felt like something.
[254.44 → 254.94] And I had that.
[255.02 → 259.62] Remember, I said I had worked with C at that laboratory, and it kind of rekindled some of
[259.62 → 260.54] those feelings, too.
[261.30 → 265.56] I'd also pushed up against some of the limits of Python in my work, especially with performance
[265.56 → 266.14] and scaling.
[266.54 → 266.58] Right.
[266.82 → 268.58] Yeah, it just immediately felt pretty good.
[268.76 → 273.44] So I didn't really have a chance to work professionally with Go until a few years after that.
[273.44 → 280.12] But I would say, yeah, I've definitely been using Go and a fan of Go since the early days.
[281.44 → 286.48] And so were you working in kind of small startups then, kind of originally?
[286.74 → 291.86] Because I think there's something interesting about the mindset of startups and what you have
[291.86 → 294.98] to do in a startup environment that's quite different.
[295.06 → 298.22] It can be very different situations, bigger enterprise companies and things.
[298.28 → 301.52] And I think that probably plays a part a little bit in this story, doesn't it?
[301.92 → 302.58] Yeah, it does.
[302.58 → 309.74] So my first professional web development job was working for a small nonprofit here in
[309.74 → 310.12] Chicago.
[310.84 → 312.96] And we were an environmental nonprofit.
[313.36 → 317.42] And I was basically the one of a few web developers there.
[317.52 → 322.46] And so I had a lot of freedom to pick and choose technologies.
[322.68 → 329.78] I would at the time, I remember using Cold Fusion and PHP, even some early Ruby on Rails in the
[329.78 → 332.12] very, very, very early days of that stack.
[332.32 → 340.10] But I helped co-found a startup with the co-creator of Django, the Django web framework, Adrian Amravati
[340.10 → 342.96] in 2007 called Every Block.
[343.40 → 344.68] And Every Block was a startup.
[345.02 → 346.86] It was a hyper-local news startup.
[346.86 → 353.82] So the idea that we would go out and collect information on the web and different sources
[353.82 → 357.32] about news that was happening near you, like on your block in your neighbourhood.
[357.66 → 360.88] You wouldn't care about it if it was across town, but it's happening on your block.
[361.02 → 362.66] You super care about it a lot.
[362.66 → 368.70] So since obviously Adrian was the creator of Django, we used Django for that.
[369.26 → 371.90] And so that kind of made the choice easy.
[372.10 → 376.96] But I've definitely experienced in my time that there's an interesting set of factors
[376.96 → 379.62] that lead to you picking a different technology or a different stack.
[379.76 → 386.26] But for me, it's been about expressiveness, how productive I can be in it, and does it perform
[386.26 → 386.88] well enough?
[386.88 → 391.32] And Django, Python, you know, checked a lot of those boxes for sure.
[391.56 → 397.32] And Every Block, you know, went on to be a pretty successful, although relatively short-lived startup.
[397.78 → 399.84] Yeah, because you sold it to MSNBC, right?
[400.24 → 403.92] It was acquired by MSNBC in, I think, 2011.
[404.32 → 407.48] It was actually part of NBC News because we had that news angle.
[408.34 → 413.48] And I mean, nowadays, people take, I think, for granted things like Next-door and Facebook,
[413.48 → 416.76] you know, local news about their neighbourhood.
[416.88 → 420.46] But so we were kind of, you know, one of the early pioneers of that.
[420.66 → 423.98] And we sold the company and kept working on it for a little bit.
[423.98 → 426.30] But we did some interesting things on Every Block.
[426.50 → 431.44] In fact, one of the things I'm most proud about is we built our own map stack.
[431.94 → 438.50] So at the time, if you remember back in 2006, 2007, JavaScript engines and browsers were starting
[438.50 → 439.18] to get faster.
[439.96 → 445.28] Google Maps popped on the scene, and it was suddenly like, oh, you can do these native desktop
[445.28 → 448.28] app-like things in your browser for the first time.
[449.10 → 454.48] And in fact, Every Block kind of came out of this idea of sort of like a Google Maps mashup
[454.48 → 459.22] of taking Google Maps and then using its API and slapping data points on it.
[459.78 → 463.28] And when we started the company, we thought it would be great since that's going to be such
[463.28 → 464.50] a central part of this.
[464.50 → 469.80] You want to be able to look at a map of your neighbourhood, drill into your block, see, you
[469.80 → 472.34] know where news is happening.
[473.16 → 478.94] And when I say news, I'm talking about maybe your block is mentioned in the news or maybe
[478.94 → 484.76] a building license has been issued or a restaurant inspection or things like that, public records,
[485.52 → 486.40] crime information.
[486.70 → 489.56] And we would aggregate all that and put that onto a map.
[489.56 → 495.52] So Google Maps was great, but we wanted to have control over the look and feel and the
[495.52 → 496.56] user experience.
[496.98 → 504.32] So we built a map stack from the ground up using sort of open geospatial tools at the
[504.32 → 510.94] time, open layers, Manic, some other tools like that, and then kind of combine that with
[510.94 → 515.52] the Django app server we were using to pull the data out of the database and then present
[515.52 → 516.40] that on the browser.
[516.40 → 521.94] Worked with a great designer, Wilson Miner, to kind of come up with their own palette and
[521.94 → 525.34] design for the maps themselves, which, you know, I thought they looked really beautiful.
[525.64 → 527.86] So it was a way of visualizing the data.
[528.10 → 530.60] And it was really, I think, pretty interesting accomplishment.
[530.82 → 535.14] And now, you know, you've got things like Map box and there's just a lot more flexibility
[535.14 → 541.76] when it comes to the sort of in-browser map, custom map and geospatial experience.
[542.18 → 545.02] Yeah, there are loads of SDKs and things that we can just use.
[545.02 → 549.44] But I guess when you didn't have that, sometimes you do have to build things.
[549.72 → 549.86] Yeah.
[549.98 → 550.72] That's a cool one.
[550.94 → 552.12] We just kind of figured it out.
[552.24 → 555.74] And again, something that, you know, because we were a startup, we could sort of experiment
[555.74 → 557.64] and help differentiate ourselves.
[558.44 → 563.78] I'm trying to map in my mind the path you would take from a startup to government contractor.
[564.28 → 565.36] Curious if you could take us on that walk.
[565.36 → 565.88] Yeah.
[566.08 → 571.40] Well, so after every block, I found myself working to support President Obama's re-election
[571.40 → 575.80] campaign in 2012, which was headquartered here in Chicago.
[576.42 → 579.88] And there was a big technology effort around the campaign.
[580.92 → 586.50] For the first time, well, technology had been a part of his original campaign for office,
[586.70 → 588.82] but they really brought it in-house.
[588.82 → 594.58] We're going to build a lot of our own tools, the software that we use, not just for the
[594.58 → 600.58] website, but how we interact with our volunteers, how we reach out to potential voters, how we
[600.58 → 605.26] sort of organize and coordinate the campaign, writing custom software in-house.
[606.02 → 611.62] So I was the deputy director for technology at the Democratic National Committee during his
[611.62 → 612.06] re-election.
[612.06 → 617.02] And so we were supporting the campaign and coming up with all these tools and building
[617.02 → 619.44] the technology to run the campaign.
[619.94 → 625.92] Actually, that was one of the places where I first had an idea that Go could really do
[625.92 → 627.12] the job at scale.
[627.60 → 631.32] So this is leading to how this all wound up in the government.
[631.48 → 636.68] But we were building tools to support the final days of the election when millions and millions
[636.68 → 637.74] of people are going to turn out.
[637.74 → 643.12] At the time, early voting and mail-in ballots wasn't quite as popular as it is now for obvious
[643.12 → 643.54] reasons.
[644.10 → 648.42] But we were building tools to help with that get out the vote effort.
[648.70 → 650.66] So mainly people looking up their polling place.
[650.72 → 651.56] Where do I go to vote?
[652.00 → 655.42] So that was a very popular page on the BarackObama.com website.
[656.16 → 661.36] And we decided to make a key component of that sort of back-end service that was looking
[661.36 → 667.70] up, kind of translating from your home address into the database of polling locations, where
[667.70 → 668.66] you actually go to vote.
[669.32 → 675.02] There was a key component there that we decided to use Go for to kind of do the middle layer.
[675.58 → 682.46] Because we knew it was going to be high volume, we wanted low latency, and it performed fantastic.
[682.46 → 689.40] So I knew Go at that point was something that you could put into production on mission-critical
[689.40 → 689.90] services.
[690.30 → 693.62] It gave me a lot of confidence about the language itself.
[693.62 → 695.86] So the president's re-elected, obviously.
[697.06 → 703.26] And sort of how I get involved in government technology is about a year later, healthcare.gov
[703.26 → 704.20] is about to launch.
[705.12 → 712.50] And just for your non-US listeners, healthcare in the United States works a little bit differently
[712.50 → 714.72] than it does in a lot of countries.
[714.72 → 719.42] It's mainly about health insurance that your job provides you, right?
[719.46 → 721.86] That's the main way that most people get health insurance.
[721.98 → 724.44] And if you're older, you can get on something called Medicare.
[724.94 → 728.96] And if you're poor or have a disability, you can get something called Medicaid.
[729.36 → 731.26] Medicare and Medicaid being government programs.
[731.48 → 733.44] But by and large, most people get it through their employer.
[734.40 → 740.58] Well, the president passed and Congress passed a law called the Affordable Care Act that did
[740.58 → 741.36] two big things.
[741.70 → 744.70] One, it created a new marketplace for insurance.
[745.02 → 750.96] So people could go buy insurance on this marketplace that it had a subsidy so you could afford it.
[751.20 → 756.00] And there were rules about what the insurance could cover.
[756.38 → 759.28] So it made sure that it wasn't just junk insurance.
[759.28 → 763.70] It was if you actually showed up and needed to get a procedure or something like that,
[763.80 → 766.76] see your doctor, go to the hospital, it would actually cover those things.
[766.76 → 773.90] So it was a regulated market, and it expanded the Medicaid program, the program for the poor
[773.90 → 775.02] and people with disabilities.
[775.72 → 777.32] So it did those two big things.
[777.44 → 782.32] And then healthcare.gov was the way that they were primarily going to deliver it to people.
[783.16 → 788.96] And the president talked about wanting to have this like consumer Amazon, you know,
[789.02 → 792.84] like experience for getting health coverage through the website.
[793.02 → 794.44] So that was the sort of aspiration.
[794.44 → 799.36] But the plot thickens.
[800.04 → 807.84] So October 2013 rolls around and the site launches, and it's immediately clear that it's not working.
[807.96 → 810.08] It's in the news and people are talking about it.
[810.14 → 812.90] It's kind of all anybody is really talking about.
[814.04 → 820.04] And the folks that I worked with on the campaign, that technology team that I talked about,
[820.22 → 823.42] we're, you know, we're texting each other back channelling like what's going on?
[823.42 → 826.48] Like, how did we get it so right on the campaign side?
[826.54 → 832.04] But when it came to the like really critical part of governing, how is it going so wrong?
[832.16 → 834.64] And we're brainstorming, you know, what could possibly be going wrong?
[834.70 → 836.06] We didn't really have visibility into it.
[836.10 → 836.90] Nobody really did.
[836.90 → 840.86] So I get a call in a couple of days after that.
[841.16 → 843.40] This is like mid-October 2013.
[844.48 → 846.50] And it's from Todd Park.
[846.74 → 850.22] He's the at the time, the CTO of the United States.
[850.22 → 854.54] So he works inside the White House as the chief technology officer of the United States.
[854.54 → 857.24] And they're putting together a team.
[857.94 → 869.38] Basically, they want to get some outside folks who have technology experience and figure out what's going wrong because they themselves didn't know what was wrong with the site.
[869.50 → 873.28] They were asking the people who were working on it, the contractors, the government agency.
[873.28 → 877.36] And they didn't know they couldn't get that information up to the White House, believe it or not.
[877.46 → 879.50] So I said yes immediately.
[880.28 → 884.72] And there was a small group of us that joined Todd.
[884.92 → 887.00] I'm talking like single digits of people.
[887.28 → 888.24] It's like the Avengers.
[889.20 → 894.80] You know, we people called us the tech surge because that's how it was characterized to the media.
[895.36 → 898.50] They call you on a red phone like we need you.
[899.10 → 900.00] Report immediately.
[900.00 → 902.12] Instead of Mjölnir, you show up with a keyboard.
[905.06 → 911.16] I mean, honestly, like there's the kind of cliché moment in movies where it's like your country.
[911.30 → 912.72] I mean, it really felt like that, right?
[912.76 → 913.96] Like your country needs you.
[913.96 → 917.78] It felt like that because we knew what the stakes were.
[918.04 → 921.56] It was the stakes were very high, and we could see this thing kind of failing in real time.
[922.22 → 923.78] So, yeah, I said immediately yes.
[923.78 → 933.92] And the very, I think, next day, or maybe it was the day after I'm in front of the West Wing of the White House at six o'clock in the morning meeting the other members of this team that's been put together.
[934.96 → 936.52] And it goes from there.
[936.78 → 937.98] So you all didn't know each other.
[938.40 → 941.44] Well, some of us knew each other from the campaign.
[941.44 → 945.66] So that's kind of how the connection was made to like, how are we going to put this team together?
[945.78 → 950.34] Well, let's start with the people who did a good job on the technology of the campaign, and we'll go from there.
[950.68 → 956.06] But so I knew one other person on the team from the campaign.
[956.06 → 972.32] But we were all relatively new to each other and our backgrounds were software engineers or product managers in technology companies or, you know, just kind of in this, I would say, broader Silicon Valley startup.
[972.76 → 977.84] Although I hadn't worked on a Silicon Valley startup myself, but just that idea of like private sector Silicon Valley startups.
[978.06 → 982.54] That was the kind of tech talent and experience that was being drawn from.
[982.54 → 985.72] So this team is brought in, right?
[985.88 → 987.42] The rescue team, right?
[987.78 → 989.82] The Avengers, if you will.
[990.20 → 991.54] What happened with the other team?
[991.76 → 993.70] Like if things were going wrong, right?
[993.82 → 997.02] So generally speaking, so I have this idea in my head, right?
[997.06 → 1001.54] A crazy idea that if something is going wrong with a project, right?
[1001.64 → 1004.24] You go to the team, and you start asking questions.
[1004.42 → 1005.94] Hey, like what's going on?
[1005.96 → 1006.88] Can you fill me in?
[1006.88 → 1012.36] And you give the chance to team to sort of React and come up with solutions, et cetera, et cetera, right?
[1012.36 → 1018.14] Like things you might expect to do, like, you know, at any other, you know, sort of organization.
[1018.92 → 1028.56] But this sounds like this team is brought in and the team that actually built the tech just gets sort of, you know, jettisoned and just, you know, they're gone.
[1028.70 → 1033.62] So now you just get handed this thing, and they go like fix it?
[1033.70 → 1035.18] Like what is that transition?
[1036.02 → 1037.24] Well, we didn't really know.
[1037.24 → 1039.58] So this is a really important part.
[1039.72 → 1043.36] The team that built healthcare.gov was still there.
[1043.36 → 1056.16] And from what we can understand, I think some important context here is just remember how much pressure there was every single day on this thing, right?
[1056.20 → 1060.62] This like signature, you know, political thing.
[1060.62 → 1064.72] And it's in like literally on the news every single day.
[1064.78 → 1071.60] Like we're walking into, you know, the buildings where this is going on, and it's on CNN on the lobby and the big flat panel screens, right?
[1071.64 → 1073.68] Like the pressure was intense.
[1074.74 → 1079.06] And the people who were working on it, who had built it, right?
[1079.06 → 1079.80] Because we didn't build it.
[1079.84 → 1082.30] We were just showing up there to kind of figure out what was going wrong.
[1082.48 → 1083.18] They're still there.
[1083.18 → 1089.42] The problem was, well, in some ways they didn't know what they didn't know.
[1089.62 → 1091.66] And I'll get to that in a second what I mean by that.
[1091.88 → 1093.96] So they didn't quite know how to fix it.
[1094.76 → 1102.58] And they weren't doing the things that they needed to do to get the right kind of information up to people like the president.
[1102.58 → 1111.80] You know, people in the West Wing, the White House were trying to operationalize this and try to understand what was wrong and communicate, try to prioritize how it would get fixed.
[1112.14 → 1114.26] They weren't doing the right sort of things that.
[1114.94 → 1117.68] So, for example, there wasn't monitoring, right?
[1117.76 → 1119.96] Like or there was, but it wasn't accessible.
[1120.38 → 1123.80] It was maybe hidden behind a VPN that some people had access to.
[1124.56 → 1127.60] But it was really hard to figure out just like, is the site up or down?
[1127.88 → 1129.08] What parts are up or down?
[1129.24 → 1130.94] What is the performance degraded?
[1131.34 → 1132.18] What's the baseline?
[1132.18 → 1134.12] So that didn't exist, right?
[1134.16 → 1135.76] So that's kind of problem one.
[1136.34 → 1138.96] So you didn't have any visibility into really what was going on.
[1139.20 → 1151.14] There was no visibility or there was, but it was so compartmented off and for all intents and purposes, inaccessible to people who were needed to make decisions from that information.
[1151.48 → 1153.92] Sounds like a cultural aspect of things there, too.
[1154.00 → 1154.86] But yeah, keep going.
[1155.52 → 1155.74] Yeah.
[1156.02 → 1157.08] What was next?
[1158.04 → 1160.36] What I was saying about not knowing what they didn't know.
[1160.36 → 1167.68] Now, if I had to sum it up, the fundamental problem with healthcare.gov as it originally launched was they built the wrong thing.
[1168.42 → 1168.54] Okay.
[1168.54 → 1176.00] So they had the wrong model of what they needed in their heads when they architected and designed and built the site.
[1176.00 → 1184.86] And so what I mean is what they needed to launch was high transaction consumer-like web technology, right?
[1184.92 → 1188.16] Like an Amazon or like a piece of consumer technology.
[1188.16 → 1190.64] Lots of people concurrently using it.
[1190.84 → 1192.20] You want low latency.
[1192.64 → 1194.24] You want a good user experience.
[1194.74 → 1199.40] It's transacting a lot of data, a lot of important data to make sure you get that stuff right.
[1199.54 → 1201.32] You know, good data integrity.
[1201.92 → 1203.22] All these sorts of things.
[1203.92 → 1209.64] But fundamentally, a good consumer experience, which is the site interacts with you well, responds well.
[1209.64 → 1213.18] But what they built was enterprise software, right?
[1213.30 → 1229.98] They architected a big, complex machine that had enterprise components that maybe work well if you've got like an analyst sitting at their desk and maybe there are 12 concurrent users ever using this thing, right?
[1230.16 → 1231.12] Maybe that works fine.
[1231.12 → 1240.02] But those were the building blocks and then deploy that into a data centre that didn't have kind of elastic scaling.
[1240.20 → 1241.74] You couldn't add capacity easily.
[1242.32 → 1246.66] Was it merely scale that was the problem or was it that it didn't actually work the way it needed to?
[1246.82 → 1252.52] It both was the wrong conceptual model for a transactional website like it needed to be.
[1252.64 → 1253.68] The wrong model.
[1254.10 → 1255.92] They architected the wrong house.
[1256.18 → 1256.50] Right.
[1256.66 → 1258.04] And then it couldn't scale, right?
[1258.14 → 1260.16] So you could potentially use scale.
[1260.16 → 1264.96] You could throw resources at it to kind of overcome those limitations.
[1265.70 → 1268.42] But the design of it made that really, really hard.
[1268.52 → 1270.22] And then some of the physical realities.
[1270.58 → 1278.00] So being like we take for granted, we can spin up a VM in AWS or Google Cloud or Azure or whatever it is.
[1278.58 → 1282.42] The government was not ready for all of that stuff in 2013.
[1282.42 → 1291.04] So the healthcare.gov was deployed into a data centre that, you know, they had VMware, and they had some tools like that.
[1291.04 → 1294.98] But fundamentally, there were like racks of servers that were like, these are the healthcare.gov racks.
[1295.26 → 1295.40] Right.
[1295.52 → 1296.26] And that's it.
[1296.26 → 1300.54] And like a SAN attached to it for network storage and things like this.
[1300.54 → 1313.68] But like I said, when that traffic starts flowing in and the individual components are not architected in a way for low latency and responsiveness, you start to get these bottlenecks, these pileups, dog pile, just not good caching.
[1313.68 → 1319.90] So all those components get strained and stressed and they sort of cascading fail.
[1320.20 → 1327.38] And then on top of all of that, right, the team that was building it was they were running through the tape.
[1327.50 → 1329.40] They were still building things.
[1329.66 → 1331.40] They were exhausted.
[1331.70 → 1335.22] They were not communicating well across teams.
[1335.22 → 1341.06] So they just had this big, big, complex thing that wasn't quite the right shape for what they needed.
[1341.80 → 1348.04] And it wasn't in a physical place where you could kind of just, you know, turn up the horizontal scaling knob.
[1348.52 → 1352.18] And then there was just this like lack of like communication and coordination.
[1352.44 → 1358.96] So, yeah, we walked into the situation on day one, honestly thinking, oh, maybe we'll be here for a couple of days.
[1359.20 → 1361.18] You know, give them some ideas of what to do next.
[1361.18 → 1368.86] Little did we know we were going to spend the next like two and a half, three months of our lives, like basically seven days a week to get this thing turned around.
[1368.88 → 1371.64] Because we knew that's what it would take given what we walked into.
[1380.28 → 1389.48] So with these people like used to building government websites where relatively low traffic, and they usually just like manual forms, aren't they turned into web?
[1389.48 → 1392.56] And we have that same here, local government, especially.
[1393.02 → 1394.46] They don't feel very modern.
[1395.00 → 1406.56] Is it just literally that, that the experience of the people building it was just for those types of systems, and they'd never really encountered a situation like this sort of high throughput situation?
[1407.22 → 1408.76] Yeah, I think that's exactly right.
[1408.76 → 1419.22] So basically, when time came to build healthcare.gov, the way government contracting works are you sort of work with government contractors.
[1419.22 → 1424.20] You don't really just go out and contract with like, I don't know, Google, right?
[1424.28 → 1428.48] Although Google does have some government work, but that's not how it would normally work.
[1428.56 → 1435.52] You would normally reach out to these companies that have historically worked with the government and like government is their main customer.
[1435.52 → 1452.04] And yes, so for the 10 years or 20 years prior to healthcare.gov, the kinds of companies that were sort of bidding on the healthcare.gov work, their main experience was with building, right, this kind of like more enterprise software stacks.
[1452.04 → 1464.10] And they really didn't have the experience of that consumer web that, right, is kind of a at the time, you know, 2013 was becoming more common and more of a commodity.
[1464.84 → 1473.54] You know, we were, we were understanding about, you know, meccas and, you know, how you scale up an application, how you deliver a good experience in AWS.
[1473.78 → 1474.88] It was becoming more and more common.
[1475.10 → 1477.98] That experience and expertise hadn't made its way over to government.
[1477.98 → 1492.28] Yeah. And so there's something else about the way of working like that when these older companies or bigger companies with all this architecture and hierarchies and things is often you end up isolating by functionality, don't you?
[1492.34 → 1501.78] So you end up having separate out database people are separate from application or business logic people, and they're separate, and it's all kind of divided up like this.
[1501.78 → 1507.54] So that's hard to have a kind of coherent idea about anything I find anyway.
[1508.04 → 1520.88] And then, yeah, when you think about then sort of having those requirements that are written in stone and written in law often, which you can't then deviate from, kind of sucks out a lot of creativity.
[1521.22 → 1529.22] And, you know, in the startup world, for sure, people are more used to being agile, really out of necessity because we don't really know what we're doing.
[1529.22 → 1533.00] We just admit it. Whereas in enterprise, you can't admit that you don't know what you're doing.
[1533.14 → 1537.16] So you have to sort of plan everything out to every in every detail.
[1537.24 → 1541.10] And then your hands are really tied. Did that play a role, you think, in this?
[1541.58 → 1550.98] Yeah, for sure. I mean, you know, what I would say about that is like, I think it's OK that government lags behind the private sector and startup world when it comes to technology.
[1551.48 → 1556.22] Great. Government's not where you want to be taking a bunch of risk and trying out the latest web framework.
[1556.22 → 1559.18] And like, I mean, maybe you could play around with that a little bit.
[1559.24 → 1563.08] But like in the main, right, you want to be a little bit more conservative.
[1563.38 → 1568.64] Let the startups kind of take the risks and figure out like what's the next hot tech stack.
[1568.70 → 1572.78] And then, you know, hopefully that trickles into to everything else.
[1572.78 → 1579.68] What your point about the sort of division of labour is a really important one, because this thing was huge.
[1579.68 → 1588.70] Right. And for what it ultimately was, which was maybe it's helpful to if I just describe health care of really quickly, like what it was actually meant to do.
[1588.80 → 1594.56] So the idea is you first you go to health care of you sign up for an account, which already should tell you something like.
[1594.56 → 1599.16] If you go to Amazon, you can browse and add things to your cart.
[1599.34 → 1606.68] And then if you need to create an account at the end, right, it's the funnel you want to bring people into, and you don't want to push them through the hardest part of the funnel, which is signing up.
[1606.80 → 1610.72] And, you know, that can be laborious and kind of get you off the game.
[1610.94 → 1612.92] In this case, you just want to look for health insurance.
[1613.34 → 1616.70] So we put you through the narrowest part of the funnel up top.
[1616.76 → 1618.52] Right. So you sign up.
[1618.52 → 1631.24] Then you have to apply. So apply means with all my personal information about me and my household, am I eligible to buy this health care with this subsidy or maybe get Medicaid, the expanded version of Medicaid?
[1632.34 → 1641.56] OK, so there's this application part and that involves like there's some business logic there, looking up rules, database interactions a little bit.
[1641.56 → 1644.56] And then you get to the place where you can actually browse health plans.
[1644.82 → 1646.90] And that's basically a database of plans.
[1647.22 → 1655.54] Right. With information about their premiums, their co-pays, their deductibles, the things they cover, what regions of the country they cover, things like that.
[1655.88 → 1657.24] All the things you should have seen first.
[1657.96 → 1659.56] The shopping part, the browsing part.
[1659.68 → 1661.00] Exactly. The shop. Right. That's right.
[1661.36 → 1665.90] You have to like to fight your way through Mordor, and then you get to the Shire.
[1666.02 → 1668.24] Right. Instead of the other way around.
[1668.24 → 1671.36] Well, in the Shires here, we have socialized health care.
[1672.14 → 1673.12] Right. Exactly.
[1673.74 → 1682.06] We used to joke on the rescue that, you know, if we were the health care dot CA web would just be like you have health care and that's it.
[1682.14 → 1682.74] Static page.
[1683.08 → 1684.68] Yeah. Much easier attack.
[1685.24 → 1686.82] That's good reason to do it.
[1686.82 → 1688.16] If no other.
[1689.66 → 1697.88] So, you know, and I have to say, like, I personally believe we should have, you know, affordable universal health care average in this country.
[1697.88 → 1698.82] I think it's a right.
[1699.30 → 1703.70] I'm really proud of the Affordable Care Act for, you know, moving us closer to that goal.
[1703.78 → 1705.66] It expanded coverage tremendously.
[1706.00 → 1714.94] That's what was so important to us and why it was critical that we worked so hard to turn it around was because we didn't want to go backwards.
[1714.94 → 1719.44] Right. We didn't want to lose 20 million people have covered with health care.
[1719.86 → 1721.36] We wanted to lock that in.
[1721.36 → 1722.60] Although now it's upper.
[1722.60 → 1730.50] So it had a kind of political imperative for you as along with the thing that we all have about wanting to make the tech work.
[1730.68 → 1735.26] Did you also have that sort of personal kind of political motivation as well?
[1735.68 → 1736.40] Well, absolutely.
[1736.54 → 1737.26] I mean, absolutely.
[1737.26 → 1747.66] Like just for myself, and I don't think that this is a prerequisite for somebody who believes that government should work at government as a function of something that we do collectively together.
[1748.16 → 1756.04] You don't have to believe that, you know, President Obama was a good president or that you worked on his campaign as a prerequisite to have worked on the health care.gov rescue.
[1756.04 → 1758.78] That was an important aspect for me.
[1759.26 → 1761.92] But I will say that we were hearing all the time.
[1762.34 → 1765.14] So the Affordable Care Act was already the law.
[1765.26 → 1768.22] Health care.gov was sort of the delivery mechanism.
[1768.22 → 1773.40] But we were hearing all the time from people for whom the law had already made their lives better.
[1773.98 → 1781.82] They could stay on their health, their parents' health insurance longer until they were 26, or they couldn't be denied coverage because of a preexisting condition.
[1781.82 → 1785.62] Those stories were filtering up to the White House and then down into the team.
[1786.12 → 1787.94] So it's visceral, right?
[1788.00 → 1795.70] Like this is like it's people's lives, and you have this almost direct connection to them.
[1796.42 → 1801.84] And so, yeah, it gives you like when you're flagging a little bit, it's like, you know, you've worked all day.
[1801.96 → 1804.42] It's nine o'clock on a Saturday, and you'd rather just be done.
[1804.52 → 1809.54] Like it gave us all that extra little bit of like, well, we can't really slag off here.
[1809.64 → 1811.36] We have to take this over the finish line.
[1811.82 → 1813.84] So, yeah, that was definitely an important part.
[1813.84 → 1818.50] I wanted to go back and say that the team that we encountered.
[1818.66 → 1821.98] Right. So we were talking a little bit about how there was some team that built it.
[1822.12 → 1826.38] And this is a combination of government contractors and government agency folks.
[1826.98 → 1836.22] Our mission was and our belief as a team was to have high EQ first, bring our high IQ about Web Stack.
[1836.22 → 1838.60] But we weren't there to blow anything up.
[1838.90 → 1841.50] Like there was like six or seven of us at the beginning.
[1841.98 → 1846.36] We weren't going to rewrite HealthCare.gov in, you know, a couple of weeks or whatever.
[1846.64 → 1847.92] We needed them to succeed.
[1847.92 → 1855.72] So really what we did more than anything was point the way to here's what this thing should be doing.
[1855.94 → 1869.14] Here's how you know you're on a path to success incrementally by adding monitoring, by having a process way which we sort of prioritize bugs and defects and tackle them in sort of reverse order of their impact.
[1869.14 → 1877.54] And here's what the sort of indicators of a successful high traffic website look like and how we can move closer in that direction.
[1877.92 → 1888.94] So really our innovation, if anything, on the rescue itself was bringing one of our team members was Mikey Dickerson, who was a site reliability engineer at Google.
[1888.94 → 1897.12] One of the early people at Google who kind of helped create that culture, bringing some of those ideas to government.
[1897.36 → 1907.00] So having a daily stand-up where we were all the stakeholders could talk about their technical issues, and we could coordinate and communicate and prioritize and plan.
[1907.00 → 1910.54] And which none of that was happening before we showed up on the scene.
[1910.74 → 1912.82] So it created a sense of urgency.
[1912.98 → 1921.02] It created accountability, which is good in not just like a finger pointing or blame, but like, hey, we really need you to do this thing.
[1921.10 → 1925.18] And it's really important because we need this bug to be fixed or whatever.
[1925.68 → 1927.40] And people really rallied to that.
[1927.46 → 1933.22] So we wrote very little code, although we did write some go code that turned out to be pretty load bearing.
[1933.64 → 1935.26] Yeah, let's get into that a little bit.
[1935.26 → 1942.10] So what is the sort of the extent to which go played a role here?
[1942.52 → 1948.82] It sounds like there's some immediate impact, something that you could derive out of involving go.
[1948.90 → 1956.10] I'm curious to sort of hear all the different layers and so where you got a chance to sort of involve going and rescue.
[1956.60 → 1956.82] Sure.
[1957.38 → 1963.76] So the kind of I'll try to put you in the mindset of where we were in like late November of that year,
[1963.76 → 1968.76] which was we had a deadline that we were working towards end of December.
[1969.14 → 1977.76] So if you're an American and you want to use HealthCare.gov, you needed to have signed up by December 23rd to be covered for the subsequent year.
[1978.76 → 1982.80] OK, so that was sort of driving everything we were doing.
[1982.80 → 1988.18] That deadline, the sense that like people may have left HealthCare.gov.
[1988.18 → 1991.14] They tried to use it in the early days, and it was bad experience.
[1991.22 → 1991.82] They couldn't get on.
[1991.88 → 1993.72] They had problems and they went away.
[1993.72 → 2002.98] But through the media and through other signals and just the knowing that this is the deadline, that a bunch of people are going to come back in December all at once.
[2003.36 → 2007.64] And so we had better have this thing be able to handle that surge of traffic.
[2007.64 → 2008.00] Right.
[2008.26 → 2011.04] So everything we were doing is sort of oriented around that.
[2011.04 → 2014.46] And it's how we prioritized what we were going to work on.
[2014.96 → 2018.00] So through November, we had made a lot of improvements.
[2018.20 → 2021.32] I'm talking about things like database configuration tuning.
[2021.52 → 2021.74] Right.
[2021.88 → 2029.22] You know, don't have long timeouts on your connections when you need to recycle them so you can let more throughput through things like that.
[2029.28 → 2030.04] So we were doing a lot of that.
[2030.08 → 2034.26] There's a lot of application level logic fixes and the site had gotten a lot better.
[2034.26 → 2047.56] But we knew that when traffic really peaked and, for example, like the president would come out with like a tweet or something, or he would talk about it on the news and there would be the surge of traffic to HealthCare.gov and the site would fall over.
[2047.68 → 2047.86] Right.
[2048.24 → 2050.90] We knew that we weren't quite there yet.
[2050.94 → 2054.74] So we started to think about, like, how do you manage that peak demand?
[2055.64 → 2059.84] And one of the ideas we had was just smoothing the curve of that peak demand.
[2059.84 → 2069.92] So if the peak is in the middle of the day, if you can flatten the peak and then have it spread out over more hours of the day, you reserve some room at the top to keep the site operational.
[2070.74 → 2078.50] And so our strategy was let's use some sort of mechanism by which we can essentially like shift people in time.
[2078.78 → 2084.32] So if you're coming to the site, and it's a little overloaded right now, we'll invite you back later when the load is less.
[2084.92 → 2088.68] And that's where we came up with this email queue, essentially.
[2088.68 → 2094.70] I thought you meant transport them through time because that's easier than solving the scaling issues.
[2095.02 → 2095.56] Fly them somewhere.
[2095.88 → 2096.34] Probably, yeah.
[2097.86 → 2104.38] Probably a miscalculation on our part would have been an easier route to solve the Schrödinger equation or something like that.
[2104.40 → 2104.62] Yeah.
[2105.48 → 2106.00] So that's it.
[2106.04 → 2109.86] You say like, OK, so you say we're busy now, but here's a ticket almost.
[2109.98 → 2112.92] Come back at this time or between this time or something like that.
[2112.92 → 2114.46] Pretty much exactly that.
[2114.46 → 2125.76] So, you know, super simple idea, but we were trying to think of creative ways to just keep everybody from trying to click reload on the site at the same time in the middle of the day and nobody have a good experience.
[2126.64 → 2128.68] What I like about that idea is it's pragmatic.
[2129.00 → 2129.94] It's not perfect.
[2130.04 → 2130.60] It's a compromise.
[2130.90 → 2133.10] I mean, it's not cool to be like, hey, our website's busy.
[2133.18 → 2133.90] Come back later.
[2133.90 → 2136.26] Like that's not what you would want to have to do.
[2136.52 → 2136.96] Super not cool.
[2136.96 → 2143.62] But it's way better than the alternative, which was like everybody is at this time of day is just not getting what they need.
[2143.70 → 2144.96] So very pragmatic.
[2145.60 → 2145.70] Yeah.
[2145.76 → 2147.84] Amazon's never said come back this time.
[2147.98 → 2150.58] It's just said put your credit card in here right now.
[2151.06 → 2155.50] You can only pull off this whole ticket based come back later thing.
[2155.84 → 2159.82] But sometimes people actually really need it, and they don't have a choice about it.
[2160.04 → 2161.58] I mean, that's the thing, right?
[2161.58 → 2166.08] It's like if you're trying to sign up for health care for your family, you're sufficiently motivated to keep trying.
[2166.08 → 2167.62] Like you're going to come back.
[2167.78 → 2168.88] So, yeah.
[2168.94 → 2169.68] So that's what we did.
[2170.12 → 2170.80] But here's the thing.
[2170.86 → 2180.32] We're still operating in this environment of this like complex site and data centre, which I didn't even talk about like how difficult it was to even just deploy code.
[2180.44 → 2183.98] That was a high risk endeavour just to do a deployment, right?
[2184.02 → 2187.84] Like just to change the code or change the configuration was very, very high risk.
[2188.38 → 2189.50] That's a terrible one, actually.
[2189.50 → 2202.38] And I even see some teams working on far less important tech fall into that same problem where you're either too scared to change and deploy or sometimes it is just really hard to do.
[2202.46 → 2206.12] There's like lots of process or lots of things that have to happen.
[2206.84 → 2214.08] And, yeah, there's something, again, about being able to be iterative and quick because you can be sort of opportunistic and pounce on things.
[2214.14 → 2217.42] You can be more agile in the lowercase agile.
[2217.42 → 2217.78] Right.
[2218.30 → 2218.58] Yeah.
[2219.04 → 2225.42] It was a nervous making event every time we changed the site, whether it was new code, a configuration change.
[2225.64 → 2229.42] We actually had static logic in a business rules engine.
[2229.52 → 2240.88] I don't know if anybody's familiar with these things, but they're like basically outboard brains with if then else statements that, you know, had their own like a lifecycle of change and very, very complex.
[2240.88 → 2249.14] So, yeah, it was just not a good environment in which to introduce something like, hey, this emergency email queue.
[2249.34 → 2249.52] Right.
[2249.52 → 2259.86] So what we did was we just we like made the case that, hey, we're going to requisition these two servers over here that have nothing to do with anything.
[2259.86 → 2265.84] They're not part of the data centre, but they're within the same kind of like general security boundary as the rest of the thing.
[2265.84 → 2267.68] And we're going to run our own code over here.
[2267.80 → 2278.04] And then at the like CDN level, we're going to route everything past healthcare.gov slash email queue or whatever that we're going to route that to those servers.
[2278.22 → 2278.40] OK.
[2278.46 → 2281.54] And so the rest of this infrastructure stays the same.
[2281.60 → 2282.48] We don't touch that.
[2282.48 → 2287.12] And if our thing blows up, you can just get rid of that route and, you know, it's fine.
[2287.52 → 2289.14] So we decided to write this thing.
[2289.34 → 2298.88] And we so we had a couple of design decisions up at the top, which was this thing had to be dead simple because we were going to be the ones to develop it.
[2299.10 → 2304.18] And we were already sleep-deprived and, you know, dealing with a hundred different things.
[2304.42 → 2308.26] So we didn't want to add any more complexity than we absolutely needed to.
[2308.26 → 2312.20] I needed to be dead simple to operate for some of the same reasons.
[2312.82 → 2321.90] And we wanted something that was going to be easy to deploy, easy to operate and then easy to kind of get people back to the site.
[2322.02 → 2326.44] So what we came up with was basically just a loop, right?
[2326.50 → 2336.18] A goat thread or go routine that would pull off a JSON request from the website, the simple form on the website that we injected with JavaScript.
[2336.18 → 2340.06] That grabbed your email and a couple of other bits of metadata.
[2340.54 → 2344.14] And then we just wrote it to a file, and we did that atomically inside a lock.
[2344.46 → 2351.32] And so literally, like all this traffic is just flowing into these files, just text files that we're just like appending rows to.
[2351.98 → 2354.52] Because we didn't want to mess with the database and like separate processes.
[2354.52 → 2364.40] We just wanted a process, like an OS process that we had control over that we could use like text processing tools on the back end to do the actual like email send.
[2364.40 → 2365.48] So that's what we did.
[2365.54 → 2367.78] So we would just collect people's emails all day.
[2367.88 → 2380.94] And then when we saw the load dip under the threshold that we thought it was safe, we would do, you know, this sends to invite them back with a special code that let them sort of bypass the waiting room if that was still a thing.
[2382.40 → 2384.10] And yeah, and we brought them back.
[2384.10 → 2393.78] And I should mention that we had like this throttling mechanism that essentially dialled in whether you got the email waiting room or you could go straight in through the site.
[2393.92 → 2399.94] So it was this sort of like probabilistic thing that was like a function of the load on the site at the time.
[2400.16 → 2404.58] That sounds really low tech in a good way, right?
[2404.92 → 2407.54] Like no more than is needed.
[2407.92 → 2410.54] It was like the least clever thing we could come up with, right?
[2410.54 → 2417.58] You know if I had to convey some like life lessons here, going back to just that last point about deploying code, right?
[2418.06 → 2429.58] I think one of the things you want to do as early on in an endeavour, a project, a startup, whatever it is, a new project, you want to exercise that path to production as early as you possibly can.
[2429.58 → 2437.62] Even if it's just putting a hello world out there, it exercises your DNS, it exercises your hosting, it exercises your CCD pipeline.
[2437.84 → 2451.76] You want to do all of that early instead of finding out when you're, you know, ready to have a big publicity campaign that you forgot to tell so-and-so to turn on, you know, auto-scaling or something like this.
[2452.12 → 2453.02] So that's lesson one.
[2453.02 → 2460.30] The other lesson is like the higher the stakes and the bigger the audience, maybe the less clever you want to be, right?
[2461.20 → 2465.42] Because when things break, they break non-linearly.
[2465.58 → 2468.70] They don't break in just like simple, straightforward ways.
[2468.90 → 2471.96] At scale like that, they kind of catastrophically break.
[2472.16 → 2476.48] And then you have this added pressure to restore service.
[2476.48 → 2484.10] And so you want to make it as easy on yourself as the person who's in operations to recover.
[2484.96 → 2489.28] And the best way you do that is by not being too clever while you're building the software.
[2489.84 → 2491.10] Yeah, I think that's great advice.
[2491.46 → 2495.02] Easier said than done, but that's, you know, kind of good rule of thumb.
[2495.10 → 2495.32] Good goal.
[2495.58 → 2495.80] Yeah.
[2496.10 → 2498.02] I like that things break at scale.
[2498.58 → 2500.94] At scale, they also break at scale.
[2501.26 → 2501.70] Right.
[2501.96 → 2502.66] That's a good lesson.
[2502.66 → 2511.38] They kind of splinter out in ways that are hard to predict, especially when you're talking about a distributed system with a lot of components.
[2512.02 → 2517.38] You know, cascading failure is a real failure mode that is hard to reason about in advance.
[2517.38 → 2531.50] What was the total time that you were on this project?
[2531.66 → 2534.96] And when did you feel like you could, you know, call it quits?
[2535.08 → 2536.24] Like, well, we're no longer needed here.
[2536.30 → 2537.28] Go back to regular life.
[2537.80 → 2539.28] Well, I'm looking at my watch.
[2539.34 → 2540.42] It's been seven years.
[2540.82 → 2541.70] And you're still on it.
[2541.70 → 2550.42] My initial involvement was through that first period of time, right, through that deadline of December 23rd.
[2550.42 → 2551.80] I think it was 2013.
[2552.80 → 2553.78] And people were coming.
[2554.28 → 2565.32] So that rescue team kind of grew and contracted over the next several months because there was the there was a final deadline in 2014, which is March, something like this.
[2565.32 → 2568.02] And so I stepped away from that.
[2568.64 → 2570.82] But the experience was so searing.
[2571.04 → 2572.44] What I mean by that is.
[2573.22 → 2593.04] Having come from that campaign, having come from a startup community and then seeing this critical piece of critical infrastructure, because I think the right way to talk about health care.gov or any kind of government digital service, whether it's a website or something you interact with to get either a service or benefit.
[2593.04 → 2595.14] That's critical infrastructure.
[2595.14 → 2596.42] It's a form of infrastructure.
[2596.70 → 2598.70] It just happens to be through digital channels.
[2598.82 → 2599.24] For sure.
[2599.54 → 2606.42] It's unacceptable to me that somebody could not get their health care because a website didn't work.
[2606.54 → 2606.72] Right.
[2606.76 → 2610.06] Like there's something so viscerally wrong about that.
[2610.14 → 2611.44] Like we know how to make websites work.
[2611.48 → 2611.64] Right.
[2611.66 → 2612.80] We know how to make websites scale.
[2612.88 → 2616.70] We know how to have good user experiences like it is unacceptable.
[2616.70 → 2619.74] And so I felt that really viscerally.
[2619.86 → 2625.82] And it's not just about the technology scaling, too, from the technology hardware and software perspective.
[2625.82 → 2629.68] It's also about, you know, user experience can be an interface.
[2630.14 → 2636.30] The language of the site, the design can also be a way to kind of disenfranchise people or keep them from achieving their goals.
[2636.30 → 2638.82] So that has to be a consideration as well.
[2639.36 → 2640.78] But that visceral feeling.
[2641.14 → 2652.88] So my co-rescue team partner, Greg German, who I met outside the White House that first morning, he was also a software engineer, had been a presidential innovation fellow.
[2652.88 → 2655.68] So he that's how he kind of came into the whole thing.
[2656.24 → 2659.20] We looked at each other like we should really start a company.
[2659.30 → 2672.06] We should start a company that can bring the knowledge and experience that we have about developing modern digital services, web applications, websites with great customer experience, great user experience.
[2672.06 → 2680.62] And offer that to government and say this is a better way of doing the things that you yourself are saying you want to build, but you don't have the talent and experience to do it.
[2681.10 → 2681.86] So that's what we did.
[2681.86 → 2696.00] And we called ourselves ad hoc because we called ourselves the ad hoc team during the rescue, because when you're in a meeting with a bunch of government agencies and contractors, you go around the room and announce, you know, who you're with.
[2696.80 → 2704.66] And since we were kind of assembled just Avenger style, like you said, one of us said, we're the ad hoc team.
[2705.30 → 2706.48] And that kind of stuck.
[2706.82 → 2710.18] So in an homage to that effort, we called the company ad hoc.
[2710.18 → 2716.64] And our first customer was CMS, who is the government agency responsible for health care.gov.
[2716.94 → 2719.88] Around the table, you're like, we're the ad hoc team and no one's interested.
[2720.00 → 2722.12] And you're like, we're actually from the wire.
[2723.70 → 2726.40] Well, you know, that was the thing, right?
[2726.44 → 2732.66] We had to be we didn't want to Bigfoot our way into the situation like that because that's a way to get people to seize up.
[2732.66 → 2738.30] Right. And like we wanted them to open up to us, and we wanted to show them we were in the fight with them.
[2738.56 → 2742.04] We weren't just going to like point fingers and be gone the next week.
[2742.06 → 2742.82] We were there.
[2743.38 → 2749.10] Yeah. And so, yeah, people knew we were from the White House like that word gets around in an instant.
[2749.24 → 2753.42] Right. But we did everything we could to show like, hey, we're just part of the team.
[2753.48 → 2754.66] We just want to get this thing to work.
[2754.80 → 2755.66] Right. That's great.
[2755.66 → 2757.36] This is why Matt didn't get the call.
[2758.42 → 2760.36] Yeah, I'd be like, hi, guy.
[2760.44 → 2763.46] I'm just I'm just like you, although I did arrive in a motorcade.
[2763.90 → 2770.28] So the chief of staff of the White House told me not to screw this up.
[2770.36 → 2771.84] So don't screw it up.
[2772.36 → 2773.20] No pressure.
[2773.60 → 2773.82] Yeah.
[2773.94 → 2774.26] Wow.
[2775.04 → 2777.38] That's what Jared says to me at the start of these shows.
[2777.54 → 2778.06] That's right.
[2778.52 → 2779.10] Doesn't work.
[2779.28 → 2780.60] Did it work for you, though?
[2781.34 → 2783.36] Kind of worked out for you, didn't it?
[2783.36 → 2786.04] Well, I mean, I think we felt like.
[2787.44 → 2790.06] You know, there was this question of should we scrap the site?
[2790.90 → 2794.28] You know, they were that was the question that was being asked is like this thing recoverable.
[2794.60 → 2797.14] And I think, you know, there was a sense that.
[2797.88 → 2802.34] Yeah, maybe they built the wrong thing, but like we can make it good enough to get through this deadline.
[2802.86 → 2812.04] But the challenge is really going to be that people problem of communication and prioritizing and knowing what the right fixes are.
[2812.04 → 2815.08] From our experience of having worked on the high traffic things.
[2815.96 → 2816.58] So, yeah.
[2816.74 → 2817.00] Yeah.
[2817.46 → 2821.62] All of that pressure is there to help keep us focused.
[2822.68 → 2825.90] And it's hard to ever say like failure is not an option.
[2825.90 → 2830.32] It was you just don't quite invite that into your head, you know, at the moment.
[2830.70 → 2831.10] Hmm.
[2831.10 → 2842.64] Well, I usually don't like it when I hear managers of teams saying that because, you know, in a way you need to be free to fail, you know, in an environment where you're building things.
[2843.52 → 2846.28] But yeah, sometimes maybe.
[2846.56 → 2847.22] Yeah, it's just.
[2847.72 → 2849.40] Yeah, we actually can't fail on this one.
[2849.68 → 2849.86] Right.
[2850.44 → 2850.70] Yeah.
[2850.80 → 2851.94] It's just too big a deal.
[2852.10 → 2853.46] And that's that's kind of.
[2853.68 → 2854.08] Yeah.
[2854.10 → 2855.96] Fascinating to hear that perspective.
[2855.96 → 2856.96] Yeah.
[2858.08 → 2861.74] So, well, it's that time we're going to do Unpopular Opinions.
[2861.74 → 2867.14] Unpopular Opinions.
[2867.20 → 2868.04] You what?
[2868.14 → 2869.82] I actually think she'd probably leave.
[2870.60 → 2874.94] Unpopular Opinions.
[2878.66 → 2883.92] So who would like to put forward our first Unpopular Opinion of the evening?
[2884.48 → 2885.24] Can I go first?
[2885.30 → 2889.86] Because I don't know what the history of Unpopular Opinions on the show is.
[2889.86 → 2897.44] So I want to make sure that mine is like, you know, it's like when the figure skaters go first in the order so that the judges are like, yeah, yeah, yeah.
[2897.60 → 2898.80] The real skaters go after them.
[2898.98 → 2899.40] Please do.
[2899.50 → 2899.80] Go ahead.
[2900.04 → 2900.24] OK.
[2901.48 → 2903.16] Because I really don't know what the stakes are.
[2903.24 → 2910.68] So my Unpopular Opinion is that server side generation of websites is superior to static single page applications.
[2911.02 → 2911.50] Ooh.
[2911.90 → 2912.22] I see.
[2912.22 → 2922.96] So you're talking about do all the rendering on the server and just ship the HTML rendered versus ship a big, thick JavaScript client and then use Ajax or something for back and forth.
[2923.42 → 2923.62] Yeah.
[2924.02 → 2925.46] That's a controversial one, I think.
[2925.56 → 2925.72] Yeah.
[2925.74 → 2926.70] I'm with you on that one.
[2926.76 → 2927.56] But Matt is not.
[2927.62 → 2928.10] Are you, Matt?
[2928.26 → 2929.48] I haven't heard that one in a while.
[2929.76 → 2929.94] Yeah.
[2929.94 → 2933.64] Well, I mean, it has a simplicity going for it.
[2934.02 → 2934.80] That's for sure.
[2935.06 → 2945.72] And, you know, in front end dev, front end, especially like if you do have big frameworks working and there are lots of things going on, you can get some really strange, you can get into some strange situations.
[2946.12 → 2949.60] Like, you know, some user will click this first.
[2949.72 → 2952.30] They open this drawer, and then they go and click something else.
[2952.52 → 2956.26] And suddenly that's a state that has never, you know, never entered our minds.
[2956.26 → 2960.32] And so you do kind of control a little bit more doing the server side rendering.
[2960.48 → 2961.60] Why else do you like it, Paul?
[2962.30 → 2964.84] Well, I think there are a couple of big wins.
[2965.14 → 2984.16] One is you can have a better user experience, especially over high latency and low throughput, low bandwidth links, because you can just push a minimal set of HTML versus a big, right, like monolithic JavaScript application payload.
[2984.16 → 2987.94] Now, I know that there's splitting and there's like been some innovation on that front.
[2988.14 → 2997.20] But that kind of like first interactive usability, I think, is still superior on the static sites or the server side sites.
[2997.62 → 2998.22] So that's one.
[2998.34 → 2999.16] Another one is accessibility.
[2999.16 → 2999.80] Accessibility.
[3000.00 → 3003.74] And I know that accessibility has come a long ways on Spas.
[3003.92 → 3022.22] But my experience has been that it's easier to kind of bake that in on the server side of the HTML because you're really leveraging everything that the browser is giving you by default instead of having to essentially like to rebuild up a browser in JavaScript for more, you know, for all intents and purposes in your SPA.
[3022.22 → 3025.38] So those are the two big reasons that I think of.
[3026.10 → 3028.92] And yeah, I mean, definitely has some downsides.
[3029.02 → 3032.14] Like there's another flywheel to go wrong right somewhere.
[3032.44 → 3034.60] So it's not all roses.
[3034.92 → 3036.70] But I think I like the tradeoffs better.
[3037.12 → 3039.10] And I'm not saying no JavaScript at all.
[3039.12 → 3042.64] I'm just saying like the primary rendering should happen on the server.
[3043.38 → 3043.90] Sure.
[3044.40 → 3045.38] What do you think of that one, Johnny?
[3045.38 → 3060.72] I think I've seen sort of this evolution, right, take place over the years of usually those who start out with being sort of, you know, kind of a backend developer where that's really that's where their bread and butter is.
[3061.28 → 3064.98] Once they start doing a little bit of frontend development, they're like, yeah, this is the natural progression, right?
[3065.02 → 3067.84] I'm going to use my server side code to push out, you know, the frontend code.
[3067.96 → 3068.16] Great.
[3068.16 → 3076.58] And eventually, right, they'll either make that transition to doing full on frontend all their sort of stateful JavaScript development, right?
[3077.00 → 3084.08] Or they'll sort of like stick with that sort of server side rendered sort of pages because there's a comfort zone there, right?
[3084.42 → 3089.38] And then you have people that come in from, you know, to it from the other side saying, hey, like I'm a JavaScript developer.
[3089.62 → 3090.94] I'm all about the UI.
[3091.10 → 3092.04] I'm into the CSS.
[3092.34 → 3094.62] I'm into the HTML DOM and all that stuff.
[3094.62 → 3106.88] So, like, they're coming out either from this other side, and then they get to the edge where they're like, okay, I don't really want to go do that backend stuff you're talking about, like Django, like the Rails.
[3107.38 → 3108.50] Maybe not, right?
[3108.88 → 3111.34] And then Node comes along, and it's like, oh, yeah, I can do backend now.
[3112.50 → 3115.46] I'm going to take my JavaScript skills and go do some backend, right?
[3115.58 → 3117.60] So, it depends on where you're coming from, right?
[3117.66 → 3120.00] You're going to have a sort of different approach to it.
[3120.06 → 3122.78] But, yeah, it's not right or wrong.
[3122.86 → 3124.24] It's just different.
[3125.44 → 3127.36] I really think it does depend on what you're building.
[3127.84 → 3131.58] And I know that's kind of like the moderate stance, it depends on stance.
[3131.76 → 3131.86] Yeah.
[3131.98 → 3133.74] You should get a bumper sticker for your car.
[3133.94 → 3137.18] I'm a person that does, I like to differentiate between a website and a web app.
[3137.26 → 3138.54] I think that's a useful distinction.
[3138.70 → 3140.16] I know a lot of people say there's no difference.
[3140.66 → 3143.14] But I think most websites should be server-side rendered.
[3143.58 → 3147.36] And I think most web apps, rich web apps, I would not server-side render Gmail.
[3147.36 → 3149.92] I would not server-side render Slack or Trello.
[3150.54 → 3152.94] Like, those are applications running in a web browser context.
[3152.94 → 3155.70] Especially if you're going to have a multi-client situation.
[3155.70 → 3158.84] Like, if you're building a startup, that's going to be multi-client from the start.
[3159.00 → 3163.14] Like, Slack knew they needed an iOS client, Android client, web client.
[3163.14 → 3166.34] I think an API plus an SPA is a smart move.
[3166.72 → 3168.82] Now, most startups don't make it to that point, right?
[3168.86 → 3170.64] They fail far before they get to that point.
[3171.18 → 3172.16] So, it really does depend.
[3172.30 → 3173.70] But I tend to be with you, Paul.
[3173.84 → 3177.76] Paul, you'll be pleased to know we test these unpopular opinions on our Twitter,
[3178.10 → 3179.28] GoTimeFM.
[3179.46 → 3181.90] So, we'll find out if that's unpopular or popular.
[3182.34 → 3182.72] That's right.
[3183.30 → 3183.52] Yeah.
[3183.90 → 3185.44] Jared, didn't you come with some unpopular opinions?
[3185.44 → 3185.96] I did.
[3186.12 → 3186.72] I brought one.
[3187.10 → 3188.12] Oh, here we go.
[3188.12 → 3193.56] And let me just say that I'm a bit disappointed and impressed, but still disappointed by the
[3193.56 → 3195.54] unpopular opinions that have been represented thus far.
[3195.72 → 3200.36] Because 201 on Twitter, they've all been actually popular.
[3202.38 → 3206.92] I think people on the show, they make a good case and they're quite convincing.
[3207.16 → 3209.22] So, then you put the clip out and ask people to vote.
[3209.36 → 3209.88] They're like, yeah.
[3209.98 → 3210.80] They're like, yeah, yeah.
[3210.80 → 3211.40] I can see that.
[3212.04 → 3213.02] Johnny's right again.
[3213.58 → 3215.32] Well, I'm here to break the streak, okay?
[3215.32 → 3220.42] I came up with what I truly believe will be a nonpopular opinion.
[3220.86 → 3225.50] But is it a firmly, really kind of honestly held opinion of yours?
[3225.58 → 3226.28] Or are you just trolling?
[3226.36 → 3228.24] You're just trying to find one that's the most unpopular?
[3228.60 → 3230.60] Well, let me state it and then you can decide at the end.
[3230.82 → 3231.18] Okay?
[3231.80 → 3236.02] So, I'm not going to come on a podcast about Go and say that JavaScript is a better programming
[3236.02 → 3236.58] language than Go.
[3236.62 → 3237.18] I'm no fool.
[3237.38 → 3238.64] You know, I want to walk out of here alive.
[3238.64 → 3246.98] But I will happily start a proxy war by saying that JS Party is a superior podcast to Go
[3246.98 → 3247.22] time.
[3248.02 → 3248.52] You're off the show.
[3248.88 → 3249.70] You're off the show.
[3249.96 → 3251.60] Let me quantify this a bit, okay?
[3251.74 → 3252.62] I have some evidence.
[3253.12 → 3254.40] So, more is better, okay?
[3254.44 → 3255.34] We have more panellists.
[3255.68 → 3256.92] We have more male panellists.
[3257.02 → 3258.00] We have more female panellists.
[3258.38 → 3259.46] We have more variety.
[3259.90 → 3260.94] We play game shows.
[3261.22 → 3262.62] We host formal debates.
[3263.02 → 3264.34] We write and rehearse poems.
[3264.82 → 3267.22] We explain things to each other like we're five.
[3267.22 → 3269.60] You guys don't explain anything to each other like you're five.
[3270.58 → 3271.98] Go time records on Tuesdays.
[3272.28 → 3273.46] One of the worst days of the week.
[3273.78 → 3275.22] JS Party records on Thursdays.
[3276.12 → 3277.44] Thursday is closer to the weekend.
[3277.60 → 3278.26] Obviously better.
[3278.98 → 3280.24] We cover more topics.
[3280.36 → 3281.38] Go time is about Go.
[3281.84 → 3283.88] JS Party is about JavaScript and the web.
[3284.34 → 3285.34] That's twice as many things.
[3286.00 → 3286.46] That's cheating.
[3286.60 → 3287.54] That's twice as many things.
[3287.58 → 3288.68] And we know the web is huge.
[3288.90 → 3289.62] So, tons of variety.
[3289.78 → 3292.26] You can't take HTTP to a JS Party.
[3294.02 → 3295.34] So, in review.
[3295.42 → 3296.16] See, we do poetry.
[3296.16 → 3297.74] We have more awesome panellists.
[3298.12 → 3299.04] We have more variety.
[3299.22 → 3300.08] It's on a better day.
[3300.66 → 3302.10] And this is the big finale point.
[3302.24 → 3302.88] You're going to like this one.
[3302.96 → 3305.66] JS Party has 100% less Matt Refer.
[3306.12 → 3309.18] Which means we really cut down on those awkward silences.
[3311.28 → 3311.72] Wow.
[3312.40 → 3313.58] That was quite the pitch.
[3314.36 → 3318.92] That was the first time an unpopular opinion has been used to advertise.
[3318.92 → 3319.92] They can't.
[3321.76 → 3323.52] Jenny, have you got any products you want to push?
[3325.22 → 3325.98] Unpopular opinion?
[3326.28 → 3327.56] My book's really unpopular.
[3327.72 → 3328.26] Let me just get it.
[3328.26 → 3329.00] Let me show you more.
[3331.30 → 3331.70] Wow.
[3332.64 → 3335.18] More of an alienating opinion, I'd say.
[3335.20 → 3335.36] I know.
[3337.56 → 3337.96] Goodness.
[3338.36 → 3339.20] But more is better.
[3339.28 → 3343.20] It doesn't sound like you were listening to Paul and his message there.
[3343.20 → 3345.18] Well, I ended up with the less is better.
[3345.32 → 3346.02] Less Matt Refer.
[3346.34 → 3347.90] So, I went on both sides of the equation.
[3348.36 → 3348.78] Good point.
[3349.82 → 3350.08] Goodness.
[3350.08 → 3351.18] I think it's fewer Matt Refer.
[3351.68 → 3352.30] I think it's the point.
[3353.82 → 3355.32] You got me crushing my pearls.
[3355.58 → 3356.60] This is...
[3356.60 → 3360.00] I think maybe I've offended everybody here, but that's...
[3360.00 → 3361.06] I can't be unpopular.
[3361.76 → 3361.96] Yeah.
[3362.40 → 3362.86] It's a challenge.
[3363.02 → 3365.76] You've thrown down a gauntlet, and we're probably not going to pick it up.
[3365.88 → 3367.62] We're quite happy with the way...
[3367.62 → 3368.82] We're quite happy with the show.
[3369.36 → 3370.70] We're not going to mess around.
[3370.84 → 3372.76] We are going to do some game shows and things.
[3372.94 → 3373.82] Mess around a little bit.
[3374.10 → 3374.46] Okay.
[3374.74 → 3374.92] Yeah.
[3374.92 → 3375.26] Yeah.
[3375.34 → 3378.92] I guess we need to add some game shows and...
[3379.70 → 3380.42] Spice it up, guys.
[3380.52 → 3382.46] Have Matt do a little dance or something.
[3382.64 → 3382.92] I don't know.
[3383.04 → 3383.50] I don't know.
[3383.62 → 3385.78] On a podcast, we could all pretend it was good.
[3385.78 → 3387.92] No one would be any of the wiser.
[3388.94 → 3389.96] Matt does do impressions.
[3390.10 → 3390.90] We're going to get those going.
[3391.78 → 3392.06] Yeah.
[3392.12 → 3393.24] I'm going to do...
[3393.24 → 3397.80] I was going to do a series of videos reading the Go documentation as Jack Sparrow.
[3398.12 → 3400.34] If you'd like a preview of that.
[3400.48 → 3400.94] Please do.
[3401.08 → 3401.58] Give us a taste.
[3401.58 → 3404.74] So here's Jack Sparrow reading File Path Walk.
[3406.44 → 3409.10] Walk walks the file tree rooted at root, mate.
[3409.38 → 3412.08] Calling walk fun for each file or directory in the tree.
[3412.90 → 3413.80] Including root.
[3413.80 → 3418.36] All errors that arise visiting files of directories are filtered by walk fun.
[3419.10 → 3420.68] The files are walked in lexical order, mate.
[3421.02 → 3422.80] Which makes the output deterministic.
[3423.32 → 3425.94] But it means for very large directors, walk can be inefficient.
[3427.00 → 3428.96] Walk does not follow symbolic links.
[3428.96 → 3429.58] Is that me?
[3431.12 → 3431.52] Okay.
[3431.62 → 3432.14] I take it back.
[3432.20 → 3432.86] Go time's better.
[3435.38 → 3436.20] Oh, wow.
[3436.32 → 3438.22] That will get cut out, though.
[3438.32 → 3438.66] Don't worry.
[3438.74 → 3439.12] Oh, no.
[3439.88 → 3440.64] That's going in.
[3440.70 → 3441.36] That's in there, baby.
[3441.36 → 3442.38] That might be the cold open.
[3442.90 → 3445.30] I might do that entire standard library as an audiobook.
[3446.64 → 3450.12] I like that last line because you made it sound very eerie and dangerous.
[3450.50 → 3451.46] I was running out of breath.
[3451.62 → 3453.66] And then halfway through, I thought, why am I doing this?
[3453.74 → 3454.48] It's being broadcast.
[3455.18 → 3456.60] So there are a few things going on there.
[3458.02 → 3459.06] Oh, my goodness.
[3459.06 → 3462.38] Well, that's all the time we've got today.
[3464.44 → 3465.90] Yeah, it is.
[3466.60 → 3467.08] It is.
[3467.76 → 3471.00] But, Paul, thank you so much for coming on and sharing your story with us.
[3471.06 → 3472.12] Such an interesting one.
[3472.22 → 3474.86] It's nice to hear Go and making a difference.
[3475.16 → 3477.84] And thanks to all the stuff you're doing, the work you're doing.
[3477.98 → 3479.04] It seems very important.
[3479.38 → 3481.80] So, yeah, please come back anytime and hang out.
[3482.16 → 3482.34] Yeah.
[3482.46 → 3483.42] We'll see you next time.
[3483.76 → 3484.34] I appreciate it.
[3484.42 → 3484.70] Thank you.
[3485.08 → 3485.62] Thanks, everybody.
[3485.62 → 3485.68] Bye.
[3485.68 → 3485.74] Bye.
[3485.74 → 3486.68] Bye.
[3486.68 → 3487.68] Bye.
[3487.68 → 3487.74] Bye.
[3487.74 → 3487.80] Bye.
[3487.80 → 3488.62] Bye.
[3488.62 → 3488.74] Bye.
[3488.74 → 3489.04] Bye.
[3490.02 → 3492.82] Thanks for listening to this classic episode of Go Time.
[3493.40 → 3498.10] In case you're curious, Paul's unpopular opinion was 71% popular,
[3498.34 → 3500.34] and mine was 81% unpopular.
[3500.92 → 3504.52] But it was probably even higher than that because I recruited some JS Party fans
[3504.52 → 3505.80] to vote on the poll too.
[3505.98 → 3507.08] Would you expect anything less?
[3507.76 → 3511.14] If you enjoy Go Time and want to see it continue to thrive into the future,
[3511.34 → 3514.36] consider supporting our work with a Changelog++ membership.
[3514.78 → 3516.96] In addition to directly supporting Go Time's production,
[3516.96 → 3518.48] you get to ditch the ads,
[3518.48 → 3522.24] get closer to the metal with bonuses and extended episodes and more.
[3522.80 → 3525.40] Check it out at ChangeLog.com slash plus.
[3525.90 → 3529.96] Thanks once again to Vastly and Fly for partnering with us to make Go Time possible.
[3530.38 → 3533.04] To our mysterious friend, Break master Cylinder for the beats,
[3533.30 → 3534.08] and to you for listening.
[3534.34 → 3534.98] We appreciate you.
[3534.98 → 3539.18] Next up, tech lawyer Louis Villa returns for part two
[3539.18 → 3542.36] after our excellent episode last year answering the question,
[3542.62 → 3544.02] Who owns our code?
[3544.30 → 3545.26] Stay tuned for that.
[3545.38 → 3547.72] We'll have it ready for your next time on Go Time.
[3547.72 → 3559.28] Game on!
[3559.42 → 3559.46] Game on!
[3559.46 → 3559.62] Game on!
[3559.62 → 3560.08] Game on!
[3560.20 → 3563.34] Game on!
[3563.60 → 3569.42] Game on!
[3571.42 → 3571.56] Game on!
[3571.64 → 3572.22] Game on!
[3572.22 → 3573.46] Game on!
[3573.46 → 3577.44] Game on!
