[0.00 → 18.12] Welcome to the Changelog episode 0.4.7.
[18.32 → 19.36] I'm Adam Stachowiak.
[19.58 → 20.48] And I'm Wend Netherlands.
[20.66 → 21.56] This is the Changelog.
[21.60 → 23.20] We cover what's fresh and new in open source.
[23.64 → 26.38] If you found us on iTunes, we're also on the web at thechangelog.com.
[26.66 → 27.66] We're also up on GitHub.
[27.66 → 33.68] Head to GitHub.com. You'll find some training repos, some feature repos from the blog, as well as our audio podcasts.
[34.00 → 37.60] If you're on Twitter, follow Changelog Show and me, Adam Stack.
[37.94 → 40.42] And I'm Penguin, P-E-N-G-W-Y-N-N.
[40.72 → 42.88] This week's episode is sponsored by GitHub Jobs.
[42.96 → 45.36] Head to thechangelog.com to get started.
[45.48 → 51.92] And if you'd like us to feature your job on the show, select advertise on the Changelog when posting your job, and we will take care of the rest.
[51.92 → 60.46] If you're in the New York City area, startup Crowd Tap needs a behaviour-driven development nut who contributes to open source and knows a law of demeanour violation when he sees one.
[60.84 → 63.72] If you're interested, LG.Gd slash 6-6.
[64.38 → 71.44] And if you're looking for the best gig any passionate engineer could ever imagine, you've got to check out the software master gurus at Red Radiant.
[71.44 → 74.70] Check out LG.Gd slash 6-y.
[75.28 → 82.56] And London-based Alpha Sites needs a soup-to-nuts Rails dev familiar with every level of the application from CSS to SQL and all the Tamil and SAS in between.
[83.06 → 87.56] If you're in the Covent Garden area, follow LG.Gd slash 7-1.
[88.22 → 89.52] Not to mention you'll be over there soon.
[89.92 → 90.86] I will be over there soon.
[90.96 → 94.56] If you're a sweep in London, give me a holler on the Twitter.
[95.22 → 95.76] Let's hook up.
[96.14 → 97.10] And that's next week, huh?
[97.32 → 98.08] That is next week.
[98.08 → 99.36] A fun episode this week.
[99.42 → 101.46] We talked to Carl Tasked over at Open Government.
[102.00 → 104.70] Talked about some of the state APIs they've got developing.
[105.26 → 114.56] This is actually, you know, this is probably in your more neck of the woods because of Tweet Congress and your, I guess, deep desire for APIs and whatnot.
[114.68 → 115.62] But this is a fun episode.
[116.04 → 119.66] Yeah, kind of mashup of a lot of passions that I have.
[119.78 → 122.42] I guess politics and APIs and Ruby and Rails.
[122.66 → 123.22] Fun stuff.
[123.62 → 127.06] And I think as devs, too, I mean, this is a real fun subject that you can dive in.
[127.06 → 129.06] They've got needs for front-end designers, too.
[129.12 → 136.66] So don't feel like if you're just a Rails dev or a Rubbish that you can't jump in if you're a Ham or a SAS or just a simple front-end design.
[136.74 → 137.48] Do they need your help?
[137.60 → 138.80] So check out the project.
[139.22 → 139.54] Absolutely.
[139.74 → 141.54] It's the rise of the citizen coder.
[141.70 → 147.00] So if you want to get involved and affect your government, this is a way to do it.
[147.34 → 147.66] Absolutely.
[148.46 → 148.92] Fun episode.
[149.02 → 149.52] Should we get to it?
[149.88 → 150.44] Let's do it.
[150.44 → 150.94] Let's do it.
[150.94 → 151.44] Let's do it.
[151.44 → 152.44] Let's do it.
[152.44 → 153.44] Let's do it.
[153.44 → 154.44] Let's do it.
[154.44 → 155.44] Let's do it.
[155.44 → 156.44] Let's do it.
[156.44 → 157.04] Let's do it.
[157.04 → 187.02] Let's do it.
[187.04 → 190.26] Why don't you give the folks a little bit of background about what those two projects are?
[190.98 → 191.10] Yeah.
[191.16 → 195.26] So Open Congress was sort of our flagship project launched in 2007.
[195.58 → 205.34] It's an open-source Rails application that lets you read bills in Congress and find out sort of what's going on in Congress,
[205.34 → 227.08] and sort of integrate some of the social media stuff with what's happening in Congress, and kind of gives, I think, a better interface than what you get from, you know, Thomas, which is sort of the U.S. government's standard site for that.
[227.08 → 228.08] And open government.
[228.08 → 232.98] And open government brings a lot of that stuff into the state legislatures.
[233.34 → 239.90] So we started with five states, Texas, California, Louisiana, Maryland, and Wisconsin.
[239.90 → 244.14] So I see on your site you're a partner of the Sunlight Foundation.
[244.28 → 248.66] I know when we built TweetCongress.org, we leveraged their APIs heavily.
[249.08 → 252.28] Are you guys using code or just getting some backing from Sunlight?
[252.28 → 254.22] We're definitely using code.
[254.40 → 260.66] They have – so the Open States project is really the core data.
[260.92 → 263.32] They provide the core data for OpenGovernment.org.
[263.70 → 270.24] And they've really – like, they've done the hard work of this project in terms of, you know, they're writing all the scrapers.
[270.80 → 272.62] That's also open source.
[272.62 → 287.70] So they scrape all the state government websites and then provide a consistent API for legislators, bills, committees, you know, and votes and sort of everything that's going on.
[288.66 → 292.92] So as the person who's been directing the project for this past – I don't know how long this project has been going on.
[292.92 → 302.76] But I know when we first blogged about this on the Changelog, it was I guess about three weeks ago, and I got pretty excited about just transparency in government and what that means for us as individuals.
[302.98 → 308.70] But what's the last month been like in terms of not just being open source but also moving to this launch stage?
[309.34 → 310.24] I mean it's been great.
[310.32 → 315.66] It's really rewarding to finally launch something you've been working on for a while.
[315.66 → 321.68] I mean we've been kind of working on this, I guess, on and off since last January.
[322.92 → 336.72] And, you know, I know it's been sort of on David's mind, our executive director for a long time, to really reach down into the states and the local governments with some of the stuff that's been going on with Open Congress.
[337.60 → 345.70] So, yeah, it's been really exciting because we're getting some volunteer developers now and getting some attention for it.
[345.70 → 353.90] And I just love to, you know, finally be getting some real feedback from, you know, all over the country from people using the site.
[354.30 → 360.78] So when you're pulling down news into open government, where are some of these sources coming from?
[360.84 → 365.66] I'm seeing that some are like, you know, Google News and the Money API and Open States API.
[365.90 → 368.52] Tell me about some of the connections and how you're pulling back that data.
[368.52 → 374.36] Yeah, so it's – so Open States API really provides the core data set.
[374.98 → 379.10] That's the official data from the state legislatures.
[379.30 → 384.46] And then we've got scrapers for, you know, Google News, don't tell anybody.
[385.74 → 391.50] And I think we're doing Technical also a little bit.
[391.50 → 395.38] And then we're pulling tweets on the client side.
[395.98 → 401.08] So, you know, if you look up a member of state legislature, you'll see tweets about them.
[402.24 → 411.62] We've got campaign contributions coming in from Follow the Money, which is an amazing organization that gathers and aggregates all this stuff.
[412.34 → 417.04] That actually – so that actually is coming through also – that's coming through another Sunlight API.
[417.04 → 422.34] So Sunlight took a lot of the Follow the Money data and sort of – they sort of reformatted it a little bit.
[422.58 → 424.98] And they've got a site called Transparency Data.
[425.86 → 431.78] And we're pulling the Follow the Money stuff from Transparency Data.
[432.06 → 433.94] I love how this is all a mashup like that.
[434.02 → 438.14] I mean this is intense how, you know, a lot of different services can piggyback off each other.
[438.42 → 441.00] And essentially this is open source, and it's providing such great data.
[441.56 → 444.30] Yeah, and all of these APIs are open source too.
[444.30 → 447.44] Well, a lot of them, definitely all the Sunlight stuff and our stuff.
[447.92 → 451.06] We also have a gem called Gov Kit that's part of this project.
[451.94 → 458.90] So open government relies on – we just wrote a gem to wrap those APIs, the Sunlight APIs and a couple others.
[459.58 → 462.84] That's actually – Gov Kit's in the queue to be covered on the change log.
[462.96 → 464.86] I'm writing a blog post about that one.
[464.90 → 465.76] I discovered that one.
[466.22 → 467.50] I kind of play in the space.
[468.22 → 472.26] Do you know Luigi Montane over at Sunlight?
[472.80 → 473.42] Oh, no, I don't.
[473.42 → 473.82] Okay.
[474.44 → 476.62] Well, I came across Gov Kit the other night.
[476.74 → 487.10] I was looking at the open government GitHub page because he and I teamed up on a transparency data gem that wraps the Sunlight transparency data API.
[487.28 → 489.50] And then I came across Gov Kit and I thought, what a great name.
[489.54 → 493.96] It's kind of like the gem Fog wraps all these cloud service providers.
[494.16 → 499.20] You know, Gov Kit kind of wraps all the different open government space APIs.
[499.34 → 500.00] It's really a cool name.
[500.00 → 502.90] Yeah, that's the – you know, that's what we're looking for.
[504.26 → 505.88] I'd like to see more in there.
[506.04 → 509.30] You know, we just sort of did the ones that we needed for open government.
[509.48 → 513.62] But I hope that it can become a little bit of a hub for those APIs.
[514.16 → 514.32] Yeah.
[514.32 → 519.10] So do you have a political background at all prior to this project?
[520.90 → 521.68] Not really.
[522.00 → 528.48] So I worked at Zip car for about five years and I built a lot of the technology behind Zip car.
[528.48 → 542.72] And then I was freelance for a while and, you know, this opportunity came up and I sort of – I mean, personally, I felt really just disengaged from politics.
[543.20 → 553.26] And it seemed like an opportunity to change that, to see if there was a way I could sort of find a better connection with it and help other people do that.
[553.44 → 554.88] So, yeah.
[554.88 → 554.92] Yeah.
[555.60 → 556.68] That's how I got involved.
[557.68 → 558.70] I really think it's great.
[558.78 → 561.22] You know, a project like this helps with transparency.
[561.88 → 571.34] And do you think that technology or projects like this advance the cause of transparency in any meaningful way?
[571.34 → 573.56] Yeah, I do.
[573.70 → 577.04] I mean, I think it's a long road, and we're sort of toward the beginning of it.
[577.76 → 593.38] This is definitely – I would say open government is a first step because, you know, a lot of – if you start to look at the bills, a lot of the legislation is – if you don't have a law background, it's almost impossible to understand what's actually going on.
[593.38 → 604.50] And I think that – so with Open Congress, we've sort of worked – our fix for that in a way has been editorial content.
[604.68 → 610.42] So we have Donnie Shaw, who's just a fantastic blogger, writing about what's going on in Congress on our Open Congress blog.
[610.42 → 623.78] And I hope we can do some of that with open government as well and maybe have some bloggers in each state or something because I think that this data does need some editorial context around it for most people.
[623.78 → 632.14] You mentioned you guys have been working on this since last January, not this most recent, which was – I guess we're still technically in January, aren't we?
[633.92 → 636.44] I'm trying to advance to February as quick as we can, I guess.
[637.08 → 638.90] So it's been about a year since you've been on this project.
[639.04 → 642.60] What were some of the biggest technical challenges that you've overcome over this past year?
[642.60 → 664.28] I think the big challenge overall is that when you're merging a bunch of large data sets, there's always going to be a lot of sorts of hidden anomalies and things that you've got to work around.
[664.80 → 668.70] And yeah, that's been the challenge is just lining things up.
[668.70 → 673.10] So I've sort of learned a little bit about how to manage that.
[673.20 → 678.96] But it's still something I think we need to work on.
[679.10 → 685.68] Like how do you sync up six different data sets, especially when some of your fields are sort of overlapping?
[685.88 → 694.82] Like we get photos from Sunlight for some – we get like the URLs for photos of legislators for some of the legislators from Sunlight.
[694.82 → 701.10] And then we go back to Vote Smart and get the rest, you know, or a lot more.
[701.38 → 705.08] And then it's sort of now you've got this field that's being updated from two different places.
[705.46 → 709.74] And yeah, those kinds of syncing problems seem to come up a lot.
[710.50 → 713.30] So that's some of the stuff we've been dealing with.
[713.30 → 726.84] Yeah, I think also like, you know, with large data sets, there's always the SQL questions of sort of how do you aggregate things and make the site run fast.
[727.30 → 727.80] So, you know.
[727.80 → 745.16] As you dive into the open states and the data that is coming out of that project, you know, in large corporate settings, you'd be surprised how much of the business actually runs not on the sophisticated high-end servers and things but on CSPs and Excel spreadsheets to get passed around.
[745.52 → 748.70] What's the state of the data that you're finding in the state government level?
[748.70 → 759.62] Yeah, I mean, I think Sunlight deserves so much credit for really making that happen through, making that stuff available through great, like clean APIs.
[760.56 → 762.96] And that's definitely a breakthrough.
[763.20 → 766.72] I think you're totally right about the CSV files and Excel spreadsheets and stuff.
[767.46 → 767.90] Yeah.
[768.44 → 777.32] So when we look at the different data sets that you're kind of bringing together, what is the database backend that you're using, and how are you actually going over some of those problems you just mentioned?
[777.32 → 777.82] Yeah.
[777.82 → 778.42] Yeah.
[778.42 → 790.00] So we've got Postgres backend, and we're also using PostGIS to do some, you know, basic, like, geo stuff.
[790.36 → 797.66] Well, you can type in your zip code on the front page and get a list of all of your representatives from the federal and state level.
[798.74 → 806.52] And we're also using GeoServer on this project, which ties into PostGIS.
[806.52 → 813.22] And that's pretty interesting because we map the geography of any vote in the legislature.
[813.46 → 823.02] So you can actually see, like, you know, red for Republican and blue for Democrats and then sort of different shading depending on whether they voted yes or no or abstain.
[823.02 → 827.10] And that was pretty fun to put together also.
[827.44 → 831.36] So that's the sort of – those are the pieces on the backend.
[831.70 → 840.18] We also have – we also did something with MongoDB, which I'm not sure if I'm going to regret this later because there's sort of no way to join those two databases.
[840.18 → 852.30] But I wanted a fast way to track the page views on the legislators and bills so we could sort of, you know, show people, like, here are the most viewed pages and stuff.
[852.76 → 855.56] And I didn't really want to store all that stuff in Postgres.
[855.56 → 861.92] So we just set up, like, a really simple MongoDB that, you know, stores the pages.
[862.50 → 871.96] And it's recording through a little JavaScript – just a little JavaScript hook on the client side that goes into a Rack app.
[872.20 → 876.68] So it's, like, very basic and pretty much detached from the rest of the application.
[876.68 → 881.92] So that's the other piece, but I think it's pretty minor.
[882.62 → 888.38] You know, Congo's got some nice operators there for increment and decrement to handle large arrays like that.
[889.04 → 889.96] Yeah, absolutely.
[890.22 → 891.52] I mean, it's so fast.
[891.96 → 899.46] And we can really – you know, I think – because it was the kind of thing where we couldn't use an external analytics service for it.
[899.48 → 901.42] We couldn't, like, pull from Google, this kind of stuff.
[901.92 → 903.56] We just really needed to track it locally.
[903.66 → 905.66] But we didn't need to track a lot, you know.
[905.66 → 916.68] We just really wanted page views by – we basically break it down by hour and just make a, you know, an entry in MongoDB for each hour and then how many views were on that object.
[917.52 → 922.18] So when the devs that are listening to this podcast right now, they're actually on GitHub right now.
[922.24 → 923.42] They're about to hit the fork button.
[923.60 → 927.00] When they hit that fork button, what are some of the things they could do to contribute to this project?
[928.18 → 931.12] Oh, well, there are just, like, so many.
[931.20 → 932.38] It depends on sort of the scale.
[932.38 → 936.20] But I think – so we've got some perfect install instructions, so it's easy to get started.
[937.84 → 945.72] I – you know, we've got everything from sort of bug fixes that are needed right now.
[945.82 → 947.84] I think that our test coverage could be a lot better.
[948.88 → 951.40] You know, we're using Spec and Cucumber.
[952.08 → 955.16] And what else?
[955.16 → 960.06] And then on sort of the bigger scale of things, I mean, we've got – I would love to see an API.
[960.34 → 972.44] Like, one of the things that we've got that we pulled together here that I think sort of nobody has – nobody else sort of has right now is this district lookup thing where you can sort of say, here's my zip code or here's my address.
[972.44 → 980.04] And you can get back your legislators from the sort of federal and the state level together and all their contact information.
[980.76 → 983.60] I would love to see that as an API call that we could offer.
[984.76 → 989.18] And, you know, it's a pretty simple project, but that's just an example of something that we have coming up.
[989.90 → 993.40] So we have the guys from Sunlight on early in the life of the show.
[993.58 → 997.76] We're going to be talking to the Code for America guys, I guess, maybe in a couple of weeks.
[997.76 → 1006.70] We love projects like open government that allow just developers to get involved and kind of give back.
[1007.60 → 1016.94] Do you see this as a trend where it's the citizen coder kind of advancing government and improving government around the fringe from the outside in?
[1016.98 → 1023.04] Or do you see the government spaces just improving on their own just as the pace of technology improves?
[1024.12 → 1026.90] I think both are going to happen sort of simultaneously.
[1026.90 → 1041.74] And I think that it's great to see this sort of citizen coder thing because those efforts, I think, can really push the bureaucracy to do more.
[1042.28 → 1048.62] And I think a good example of that is the crime spotting site in the story of the crime spotting site in Oakland,
[1048.62 → 1062.08] where, you know, Stamen made this beautiful site that, you know, that pulled these crime maps, the crime data from the city of Oakland and made it, you know, it was a flash thing.
[1062.22 → 1066.02] This was a couple of years ago, but they were scraping it.
[1066.02 → 1068.90] And then sort of the Oakland Police Department shut them down for a little bit.
[1069.32 → 1079.18] And then I think they had so much support, and they had so much visibility for the project that Oakland just sort of had to cave and say, OK, we'll open it back up again, and we'll work with you.
[1079.24 → 1084.04] And then two years later, San Francisco came and said, yeah, we want crime spotting, too.
[1084.12 → 1085.02] And here's the data.
[1085.02 → 1090.12] And they handed over like a perfect KML file or whatever of, you know, of all the stuff.
[1090.30 → 1094.06] So I think that's my understanding of how that went down.
[1094.12 → 1103.10] And I think that's, you know, that's a great sort of outcome, you know, for that kind of project.
[1103.28 → 1105.04] So I would love to see more of that.
[1105.76 → 1112.56] The piece that I like a lot, at least from a numbers perspective and this view perspective, is the money trail view.
[1112.56 → 1115.34] You can actually see where a lot of your money is going in your state and stuff like that.
[1115.40 → 1120.08] But what I find this view seems to be like it doesn't make complete sense to me.
[1120.14 → 1123.94] So how do you help not only pull back this data but also make sense of it?
[1124.66 → 1126.46] Yeah, I mean, I think that's really the next step.
[1127.10 → 1131.30] We could use more in terms of visualizations of that stuff.
[1131.62 → 1134.58] I think that the money trail, there's a lot of data there.
[1135.18 → 1140.26] And we're aggregating it in the simplest possible way right now.
[1140.26 → 1144.26] We had to make some changes on that kind of at the last minute.
[1145.76 → 1149.92] So, you know, I think that could be made more clear.
[1150.22 → 1160.10] And I think that overall, like, that's the arc of the project is how can we just keep making all this data that we're bringing in more clear and more understandable for people?
[1160.42 → 1162.34] So, I mean, we're really just getting started, you know.
[1163.80 → 1166.16] It reminds me a lot of the Document Cloud project.
[1166.96 → 1168.06] Are you familiar with that one?
[1168.06 → 1168.10] Yeah.
[1170.30 → 1174.06] We actually use Jamie, which is their asset packaging thing.
[1174.80 → 1179.28] And I know that they're – were they a Knight fellow or something?
[1179.48 → 1179.60] Yeah.
[1179.72 → 1179.90] Sure.
[1180.06 → 1188.94] And you know what I love about the project is not only is it helping to, you know, turn documents into data, but at the same time, it's giving so much back to the open source community as byproducts.
[1189.72 → 1190.58] Yeah, that's great.
[1190.64 → 1191.80] And that's what we hope to do too.
[1191.80 → 1192.24] Yeah.
[1193.38 → 1204.06] It's a challenge because when you're running a service – you know, okay, so I think one of the things that makes sort of open government different as an open source project is that it's actually a service, right?
[1204.10 → 1205.56] It's like it's a full Rails app.
[1205.56 → 1208.36] And there aren't a lot of those, right?
[1208.56 → 1211.62] It's like mostly gems that people are contributing to.
[1211.98 → 1213.50] And so it's this tradeoff.
[1214.10 → 1217.02] I think Gov Kit is, you know, we've broken that piece off.
[1217.12 → 1223.64] And I think there's sort of more we could be doing to, you know, maybe some of this Congo analytics stuff could become its own gem, for example.
[1223.64 → 1233.78] So – but on the other hand, like it's interesting to be able – I think if you're just learning Ruby on Rails, to be able to see a whole app and sort of here's how it works.
[1233.78 → 1246.50] And, you know, I would hope that there are some sorts of best practices here that we're using or that we can be using to, you know, exemplify a good Rails app.
[1246.50 → 1269.76] So when you actually mentioned the kind of help that you're looking for, and you said you need more help in the visualization sections of this application, does that mean that somebody like a designer, for example, or someone who's, you know, an infographics nut that just, you know, really gets in can take this large set of data and make it make sense in unique ways that can be viral or communicated well?
[1270.20 → 1273.42] Is that the kind of help you're looking for as well or is it just strictly programming science?
[1273.42 → 1275.58] Yeah, it's – absolutely.
[1275.70 → 1276.68] That would be really helpful.
[1276.80 → 1278.12] And I think they go together.
[1278.28 → 1284.98] You know, I was just looking at that ProtoViz, that great JavaScript library for visualizations and, you know, that kind of thing, right?
[1285.04 → 1287.26] We can – there are a lot of opportunities on the site.
[1287.56 → 1291.76] Now that we have the data in place, I don't think it would be very hard to add in some of those things.
[1292.08 → 1292.42] So –
[1292.42 → 1296.84] So with five states open, plenty of room for opportunity here.
[1297.60 → 1298.58] Absolutely, yeah.
[1298.58 → 1305.12] And the schedule is – so Sunlight is actually working on the scrapers for the other 45.
[1306.76 → 1309.74] And so that's sort of an ongoing project.
[1309.92 → 1316.16] And we will launch, you know, as we can, more states.
[1316.44 → 1320.46] Is that kind of stemming from some of the progress needed on open states as well?
[1320.56 → 1322.90] Because I'm not sure if we talked about that too much.
[1323.66 → 1324.32] Yeah, yeah.
[1324.38 → 1326.00] And they definitely need developers there.
[1326.00 → 1327.60] All those scrapers are in Python.
[1328.22 → 1333.30] And, I mean, that's really – like, as I said before, I think that's the hardest piece of this whole project.
[1333.56 → 1337.94] I mean, they've really made it easy for us because we just sort of pull a data feed from them.
[1338.00 → 1340.84] And it's very – they've made it really consistent over the last few months.
[1342.26 → 1351.40] And, you know, whereas going to these state legislative sites to scrape that stuff just seems like it would be a really tough problem that they've taken on.
[1351.40 → 1359.62] And I don't know if you've looked at it at the state legislatures, but, you know, a lot of these websites are – they're not pretty, you know.
[1359.88 → 1362.12] And the data is not in a consistent format at all.
[1362.96 → 1366.46] Well, I don't think that's their highest priority, I guess.
[1366.82 → 1369.80] But that's a different subject and a different kind of podcast.
[1369.80 → 1372.88] So we have open Congress.
[1373.02 → 1373.88] We have open government.
[1374.00 → 1374.90] We have open states.
[1375.00 → 1376.32] What else are we opening up?
[1378.16 → 1383.10] Yeah, I mean, that's really – those are our projects right now.
[1383.36 → 1383.98] Open treasury?
[1385.14 → 1385.54] Yeah.
[1385.74 → 1387.08] I mean, let's do it.
[1387.54 → 1391.02] I'd like to see that one next because I've seen some – well, here's the thing.
[1391.02 → 1416.82] When we launched this – the blog post to help you guys and start talking about open government and what this means, you know, I arbitrarily linked to this, I guess, pretty heavily viewed YouTube video about how this person could not – in Congress could not answer a simple question, which was, you know, where did this large stack of money go, which was $6 trillion or something like that.
[1416.96 → 1417.10] Yeah.
[1417.10 → 1418.24] It was just a huge amount of money.
[1418.24 → 1426.90] And when I look at scenarios like that, and she's fumbling over her answers, and we can't get clear yes or no, this is what happened or this is who we gave it to or this is how we're tracking this money.
[1427.40 → 1445.64] As a citizen who pays taxes, and who does all the right things and trusts our government, I got to look at our treasury and say how are we putting out these ballots, and how are we – and I understand the reasons, and this is not the state of this podcast, but is open treasury next?
[1445.64 → 1453.84] You know, I don't know for us whether that's – I would love to see it.
[1453.96 → 1455.32] You know, I'd love to see that kind of thing.
[1455.40 → 1461.86] I think that these projects are so critical right now.
[1461.86 → 1466.70] Just as you're saying, there's just so much sort of stuff that's going on behind the scenes.
[1467.80 → 1471.50] And yeah, I mean totally.
[1471.64 → 1483.34] Open treasury, I think there's a lot that can be done around elections too and sort of figuring out how to – I mean I spend hours and hours every time there's an election just trying to make the right choices on the ballot.
[1483.34 → 1486.92] And I still don't feel like I know whether I did or not in the end.
[1487.12 → 1489.02] It's like it's really –
[1489.02 → 1495.48] I think we're always painted into a corner because we – our choices are what we're given, not what we actually truly elect in some cases.
[1495.76 → 1496.14] So I mean –
[1496.14 → 1496.78] Yeah.
[1497.04 → 1499.92] I don't think you ever get to make a right choice when you're at an election booth.
[1500.72 → 1502.72] You know what I love about the open government space though?
[1502.76 → 1504.88] It really cuts across both sides of the aisle.
[1504.88 → 1509.56] When we created Tweet Congress, we were surprised – we got an initial set of seed data from Sunlight.
[1509.64 → 1517.36] We were really surprised to find a two-to-one Republican to Democrat advantage of politicians using Twitter at least at the federal level.
[1518.00 → 1525.26] But what we found was the developers that were interested in that space were just as fervent on both sides of the aisle.
[1525.36 → 1528.16] We met a lot of friends in that space.
[1528.16 → 1535.64] Yeah, because it's really like – it's the objective sort of criteria that everybody is looking for.
[1535.74 → 1539.20] It's the objective information, hopefully, right?
[1540.22 → 1544.38] So Ruby and Rails is the platform behind the open government website.
[1544.54 → 1548.56] So what were some of the decisions around choosing that as a technology?
[1549.26 → 1556.48] Well, we are sort of already invested in it with Open Congress and have been doing that since 2007.
[1556.48 → 1564.34] And, you know, I also – my background is I did freelance Rails development for three years.
[1565.02 → 1566.76] And I really just – I love Rails.
[1566.90 → 1570.14] I think it's a great platform for making web apps.
[1573.10 → 1576.50] I'm curious about – I didn't look at the code base, but I'm curious if they're using SAS.
[1577.42 → 1579.20] We're using Hall, but we're not using SAS.
[1579.84 → 1580.04] Yeah.
[1581.28 → 1582.48] And Hall's been great.
[1582.48 → 1585.26] Yeah, so Open Congress is all, you know, ERA.
[1585.78 → 1590.50] And, I mean, when I just look at the difference in the files, it's just astounding.
[1591.42 → 1596.56] I'm always amazed at the people that pick either – you know, they could either hate both Hall and SAS,
[1596.64 → 1598.54] or they'll say, I love Hall and hate SAS, or vice versa.
[1598.74 → 1604.86] It's always intriguing to me to listen to the I guess, opinions behind that.
[1605.10 → 1606.44] So why Hall and not SAS?
[1606.44 → 1609.98] You know, I don't know yet.
[1610.48 → 1615.76] I think SAS could work for us, and we have just – we're just not there yet with it.
[1617.18 → 1623.96] I guess my only concerns about these things are just, you know, how long does it take to actually serve up the page in the end?
[1625.16 → 1627.42] And I feel pretty good about Hall.
[1627.42 → 1635.08] I think that it's pretty clear now that it's just as fast as ERA in most cases, right?
[1635.30 → 1636.36] Yeah, that's the beauty of SAS.
[1636.64 → 1641.68] I end up pre-compiling all my style sheets and don't even really integrate with the server.
[1641.82 → 1646.40] You know, just spit out the CSS from SAS and link it up like you normally would.
[1646.70 → 1649.12] Yeah, so I think we just got to get that into our workflow.
[1649.82 → 1652.22] It's probably not even a question.
[1652.22 → 1659.60] Yeah, I mean, given how much I love Hall, and we love working with it, it seems like that would be great.
[1660.00 → 1667.18] We've been asking a series of questions here in the last few episodes just to kind of get a better look at the developers that we're profiling.
[1667.38 → 1673.16] So a series of either-or questions, and you can say none of the above if it so fits.
[1673.46 → 1674.96] So Bash or Shell?
[1675.78 → 1676.18] Bash.
[1676.74 → 1679.94] I mean, just know the answer to Hall or ERA.
[1681.00 → 1681.98] Yes, Hall.
[1682.22 → 1685.64] Your terminal font.
[1686.98 → 1688.42] Oh, I've got to look that up.
[1688.66 → 1689.68] I keep changing it.
[1690.26 → 1693.00] Because Kenneth and I are creating a site that's going to help you pick your terminal font.
[1693.14 → 1694.80] We just had this brainstorm about an hour ago.
[1695.14 → 1696.06] That's a great idea.
[1696.24 → 1699.52] We have this debate on whether Meno or Inconsolable.
[1700.44 → 1704.42] I know you're an Inconsolable fan there, Adam, but the serifs are too much for me.
[1704.92 → 1705.34] Am I?
[1705.52 → 1706.76] I thought I switched to Meno.
[1707.02 → 1707.86] Oh, did I get to the switch?
[1707.86 → 1709.06] Because you twisted my arm, yeah.
[1709.24 → 1710.88] I browbeat you into switching to Meno.
[1710.88 → 1711.84] Yeah, I couldn't.
[1712.00 → 1713.54] Well, I used to be an Anonymous Pro user.
[1713.66 → 1714.10] That's why.
[1714.26 → 1714.98] Ah, Anonymous Pro.
[1715.04 → 1715.58] That was the one.
[1716.08 → 1716.28] Yeah.
[1716.28 → 1723.38] Yeah, so I'm using Consoles on TextMate, but then I just looked in my terminal, and I've got Bit stream Versions here.
[1723.56 → 1724.66] I think I need to change that.
[1724.72 → 1725.76] That was going to be my next question.
[1725.90 → 1727.16] TextMate, Emacs, or Vim?
[1727.24 → 1728.56] It sounds like you're a TextMate guy.
[1729.12 → 1730.38] Yeah, yeah, definitely.
[1730.58 → 1733.76] Although I do use Vim a lot and have for a long time.
[1733.76 → 1736.82] So it depends on the circumstances, doesn't it?
[1738.42 → 1743.14] Well, Carl, we're at the point we like to ask the cool question about what you're doing in open source.
[1743.34 → 1748.66] So what in open source right now has got you excited that you want to fork and play with?
[1748.66 → 1755.54] I just love all the stuff that we have incorporated into open government.
[1755.76 → 1768.52] I mean, I think this project wouldn't be possible without not just Rails, but just these gems like Jamie, things like MongoDB.
[1768.52 → 1779.76] I mean, I'm excited about the whole ecosystem of Ruby and Rails, you know, gems.
[1782.30 → 1785.96] Yeah, I guess it's hard for me to choose.
[1786.18 → 1789.10] I like to think about it like whatever.
[1791.04 → 1796.98] I like that there's always sort of an option for whatever I'm working on, you know, whatever the job is.
[1796.98 → 1805.18] It always seems like there is something that's going to help me along the way in the ecosystem right now.
[1805.50 → 1810.92] So let's say you had a long weekend, a four-day weekend, and you had no open government work to do whatsoever.
[1811.02 → 1811.82] You weren't even going to touch it.
[1811.82 → 1812.54] What would you play with?
[1814.30 → 1815.02] Good question.
[1815.02 → 1818.46] That's a loaded question because it assumes that he doesn't have a life like we don't have lives.
[1818.46 → 1828.40] I think that, I mean, I'm kind of going back, I'm getting back into, I'm learning a lot right now.
[1828.56 → 1835.50] Like I think things like MongoDB and sort of document store and a lot of the real-time stuff is really exciting to me right now.
[1835.50 → 1848.48] And, you know, it's hard to kind of keep up with all sides of the web app, the sort of the stuff that's happening for the innovations that are happening sort of in the back end and then the more like client-side stuff.
[1849.16 → 1858.50] And I'm getting excited about the client-side stuff and the sort of the real-time, you know, more stripped-down sites.
[1858.50 → 1866.74] Like there's a part of me that wishes we had been able to use Congo for this project because I think it's exciting.
[1867.22 → 1871.50] I think it's suitable for, somewhat suitable for the data that we're using.
[1873.50 → 1885.50] And, you know, but it was also just like a lot of, like, you know, my background is Oracle from Zip car, and I'm very comfortable with SQL, and I'm very comfortable with that sort of that setup.
[1885.50 → 1888.52] So that's, you know, that's the trade-off.
[1888.94 → 1898.14] And I think there's, it's great what we've got, you know, but I also could totally see this working with more of a document store model.
[1898.96 → 1900.40] Well, thanks for joining us, Carl.
[1900.60 → 1907.44] It's been fun talking about open government, and we'll keep an eye on the GitHub to see what bits you guys are releasing next.
[1907.90 → 1909.08] Yeah, thanks, you guys.
[1909.08 → 1920.34] You know, I love the changelog, and it's just been, it's so important to have a hub for all of these projects and have somebody talking about them.
[1920.48 → 1921.20] So thank you.
[1921.46 → 1922.26] We enjoyed doing it.
[1922.30 → 1922.64] Thank you.
[1922.64 → 1922.70] Thank you.
[1922.70 → 1923.70] Thank you.
[1923.70 → 1924.70] Thank you.
[1939.08 → 1945.26] Thank you.
[1945.30 → 1957.60] Thank you.
