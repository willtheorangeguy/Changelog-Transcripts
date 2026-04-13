[0.00 --> 2.20]  This week's episode is brought to you by Campaign Monitor.
[2.36 --> 5.40]  Campaign Monitor is an email marketing service for the discerning designer.
[5.72 --> 8.52]  With it, you can create and send beautiful email campaigns.
[8.76 --> 11.16]  You can track the results and manage your subscriber lists.
[11.62 --> 15.58]  Campaign Monitor's reporting and analytics tools go beyond opens and clicks.
[16.02 --> 20.86]  The entire application is rebrandable, which allows you to earn profits from the campaigns your clients run.
[21.20 --> 23.62]  You can check it out at CampaignMonitor.com.
[30.00 --> 42.22]  Welcome to the ChangeLog episode 0.6.5.
[42.32 --> 43.38]  I'm Adam Stachowiak.
[43.86 --> 44.76]  And I am Wend Netherland.
[44.90 --> 45.86]  This is the ChangeLog.
[45.92 --> 47.48]  We cover what's fresh and new in open source.
[47.88 --> 51.06]  If you found us on iTunes, we're also on the web at thechangelog.com.
[51.14 --> 52.22]  We're also up on GitHub.
[52.48 --> 54.38]  Head to github.com slash explore.
[54.46 --> 58.70]  You'll find some training repos, some feature repos from our blog, as well as the audio podcasts.
[58.70 --> 62.06]  If you're on Twitter, follow ChangeLog Show and me, Adam Stach.
[62.68 --> 65.04]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[66.30 --> 67.50]  Fun episode this week.
[67.58 --> 73.32]  We talked to the guys over at Code for America, Eric Michaels-Ober and Max Ogden,
[74.22 --> 76.86]  about all of the things that they're doing at Code for America,
[77.22 --> 80.86]  and also Rails Admin and some other open source projects they have going.
[81.08 --> 82.38]  This is a really fun conversation.
[82.50 --> 86.32]  I think that we've talked in and around this space for a while,
[86.32 --> 92.02]  everything from open government to I think it's just the citizen coder is a really fun topic.
[92.94 --> 95.24]  Yeah, it's nice to see how you can apply your skills.
[96.02 --> 99.64]  This is kind of like a Peace Corps for coding, as Eric put it.
[100.06 --> 103.74]  Apply your skills for civic good instead of just a paycheck.
[104.16 --> 104.78]  Instead of just a paycheck.
[105.04 --> 107.26]  And they get to take care of a few cities,
[107.56 --> 110.08]  and they've got Tim O'Reilly's blessing on this thing, too.
[110.12 --> 111.68]  So it's a fun little thing for them.
[112.00 --> 112.84]  Yeah, get some momentum.
[112.84 --> 119.10]  So, speaking of momentum, we're going to be at Lone Star RubyConf next month.
[119.48 --> 119.74]  Yeah.
[120.10 --> 123.94]  Doing a little design eye for the dev guy slash gal down there.
[124.38 --> 127.38]  So if you're going to be in Austin in August, come see us.
[128.20 --> 128.76]  Hope to meet you.
[129.10 --> 130.20]  Hope to meet you, yeah, for sure.
[130.28 --> 134.12]  If you're into the SaaS and the compass thing on the front end,
[134.22 --> 135.90]  that's what we'll be talking about towards the end of the topic.
[136.08 --> 138.78]  And also, a quick little plug for the SaaS way.
[138.96 --> 139.70]  Follow them on Twitter.
[140.50 --> 141.68]  The SaaS way on Twitter.
[141.68 --> 142.86]  Fun episode this week.
[142.90 --> 143.44]  Should we get to it?
[143.76 --> 144.84]  Let's do it.
[153.40 --> 158.42]  We're chatting today with Eric Michaels-Ober and Max Ogden from Code for America.
[158.74 --> 160.28]  So guys, why don't you introduce yourselves
[160.28 --> 162.32]  and a little bit about what you do at Code for America.
[162.96 --> 163.24]  Sure.
[163.44 --> 168.06]  I'm Eric Michaels-Ober, and I'm a Code for America fellow for 2011.
[168.06 --> 171.98]  And I write a lot of open source software, mostly Ruby.
[173.36 --> 174.22]  I'm Max Ogden.
[174.48 --> 175.90]  I'm in a very similar boat.
[176.50 --> 179.80]  I'm a fellow here in 2011 as well at Code for America.
[180.06 --> 185.62]  And I'm continuing to write a lot of open source software this year, mostly in JavaScript.
[186.28 --> 188.82]  So I take it you don't have to be a guy to be a fellow.
[189.32 --> 192.38]  What's a bit about what's a fellow over at Code for America?
[192.38 --> 196.62]  It's basically just a one-year position.
[197.10 --> 202.40]  It's a fellowship, so you have the opportunity to work.
[202.96 --> 206.00]  Code for America's main focus, like what we're all about,
[206.10 --> 213.54]  is basically being something like a Peace Corps or a Teach for America for geeks.
[213.98 --> 215.36]  So it's like a service year.
[215.36 --> 218.96]  You basically get to spend a year giving back to society.
[219.42 --> 221.78]  And so we're working to help government make their,
[222.12 --> 224.54]  basically bringing open source technologies to government
[224.54 --> 228.56]  and making it more transparent through open data and open source software.
[229.28 --> 230.42]  What sort of projects are you doing?
[230.50 --> 232.28]  Is it city-focused or is it anywhere?
[233.58 --> 234.16]  It's both.
[234.26 --> 238.56]  We're working with three cities this year, so Boston, Seattle, and Philadelphia.
[238.78 --> 241.70]  And then there's also a project with the federal government that I'm working on.
[242.62 --> 244.46]  I could talk a little bit more about that if you like.
[244.46 --> 245.26]  Sure.
[246.16 --> 251.30]  So the project that I'm working on this year is with the federal government.
[251.50 --> 256.58]  We're working with the Department of Labor to basically build a website for veterans
[256.58 --> 260.06]  to try to help them find jobs as they come home from Iraq and Afghanistan.
[261.04 --> 266.88]  And it's basically pulling together a number of services from around the web that already exist
[266.88 --> 273.20]  in order to help veterans, but creating a veteran-friendly interface on top of those services.
[273.20 --> 278.42]  So we're actually using the LinkedIn Ruby gem that you created, Wynn.
[279.08 --> 286.90]  And LinkedIn is one of our partners as well as a number of other web services that are job-focused, job-related.
[286.90 --> 289.10]  So, no, Eric, you're a Ruby.
[289.16 --> 289.64]  Yes, Max.
[289.96 --> 291.60]  What sort of languages are you slinging?
[292.44 --> 299.04]  So before Code for America, I was working at a rail shop up in Portland, Oregon, a market research company called Revelation.
[299.04 --> 301.96]  And it was a really good engineering team.
[301.96 --> 311.40]  But I was given the opportunity to kind of, like Eric said, almost take a year off and focus on a bunch of the stuff that was previously side projects for me.
[311.90 --> 315.16]  So at the time, I was getting really into CouchDB.
[315.16 --> 322.18]  There's probably an inside joke around the office that anything that I do, I try to do on CouchDB.
[322.32 --> 323.44]  It's like my hammer for every nail.
[323.56 --> 324.84]  But so far, it's worked out pretty well.
[325.54 --> 335.80]  And as a result, I've kind of taken the deep dive into all the fun HTML5 stuff you can do because all couches is a persistence API for you to use.
[335.80 --> 339.54]  But you have to do all of the fun logic in the browser, which is a challenge.
[339.86 --> 343.76]  But I've kind of not abandoned Rails in Ruby.
[343.94 --> 344.94]  I still like Ruby a lot.
[345.10 --> 348.72]  But I'm basically doing, using, like, Jeremy's underscore JS.
[348.82 --> 354.38]  I'm basically doing all the fun stuff I was doing in Ruby before, all the same paradigms, but trying to do it in the client side now.
[354.88 --> 356.22]  And then getting into Node a bit.
[356.34 --> 359.34]  So I've, like, gotten really into JavaScript the last year.
[360.16 --> 362.90]  Jeremy Ashkenaz's underscore JS.
[362.90 --> 367.48]  So I think Jeremy is the new drinking game, so the Hamel and Sass, it's going to be Ashkenaz.
[367.64 --> 372.66]  So there seems to be some doubt, Max, of whether or not you're on the market for employment looking at your GitHub page.
[373.66 --> 379.52]  I was on Isaac Schloider from Joyent's page a couple weeks ago.
[380.16 --> 384.34]  And he has this thing that's like, recruiters go away.
[384.50 --> 385.44]  I'm happy at my job.
[385.62 --> 387.34]  And it has its occupation at Joyent.
[387.38 --> 388.60]  And he's like, I really like working here.
[388.64 --> 389.52]  Don't ask me for other jobs.
[389.52 --> 395.16]  And there's so many recruiter emails lately that I copied him and put, no more recruiter emails, please.
[395.74 --> 396.10]  So, yeah.
[397.52 --> 402.58]  So we've kind of gone into this a little bit, but not given a good description of exactly what Code for America is.
[402.60 --> 403.74]  It's ran for a couple years now.
[403.78 --> 405.60]  But what exactly is Code for America?
[405.76 --> 406.86]  So to give some clarity there.
[407.38 --> 410.06]  Yeah, this is actually the first year of the program.
[410.30 --> 414.14]  So it's a little bit of a startup and a little bit of an experiment about what it is.
[414.18 --> 415.64]  We're kind of figuring that out as we go.
[415.64 --> 419.44]  But basically, it's a service year program for geeks.
[419.80 --> 430.34]  So, you know, just like Doctors Without Borders, you know, if you're a medical professional and you want to sort of spend a year working for good, there's a program for that.
[430.50 --> 434.42]  And up until Code for America came around last year, there was nothing like that.
[434.42 --> 440.26]  If you were sort of civic-minded and worked in technology, there wasn't really a place for you to give back.
[440.64 --> 442.78]  And so Code for America offers a fellowship.
[443.48 --> 444.36]  There's 20 fellows.
[445.22 --> 446.84]  And next year there'll be even more.
[447.52 --> 449.84]  And applications are actually open now.
[449.84 --> 456.12]  So anyone who's interested in being a fellow, you get to spend basically all your time working on open source software.
[456.30 --> 462.68]  That's part of the mission and charter of our organization, that everything we do is released under an open source license.
[463.18 --> 465.72]  And we hack on a number of existing open source projects.
[466.08 --> 475.94]  So it's a great way to sort of work on open source projects, give back, and just work with some really talented, brilliant engineers from all around the country to do good.
[475.94 --> 485.64]  The other half of that, I think, too, like what our mission is, is to try to test the water in this new kind of civic startup space.
[486.76 --> 496.94]  Our leader, Jen Palka, just gave a talk at the Future of Web Apps Conference in Vegas and had some really interesting statistics on, like, take the size of the iPhone market.
[497.14 --> 499.94]  It's something like $2 billion revenue a year.
[500.58 --> 505.16]  The government IT software market is, like, on the order of hundreds of billions of dollars.
[505.16 --> 514.08]  So, like, if we can tap into the software that's powering the country and make those pieces of software just as competitive as the startup market,
[514.54 --> 521.36]  it will not only create a bunch of better software-run government and make the government work better,
[521.44 --> 525.94]  but it will also allow people who are limited to making, you know, iPhone apps right now.
[526.00 --> 530.56]  You could actually make the software that's helping people find what potholes they should fill in at the city level.
[530.56 --> 538.44]  Or we're basically, like, doing a lot of research and development this year to try to figure out what are the areas that we can actually, like, tap into and start improving
[538.44 --> 542.04]  using the same development processes that we're using in startup land.
[542.66 --> 543.64]  Who backs this?
[543.72 --> 547.84]  I mean, it's got a – you said startup, so somebody must have gotten into this.
[547.92 --> 552.56]  I know we saw a couple names there at the footer that we see off,
[552.56 --> 558.14]  and we had a couple shows already with the Knight Foundation with Jeremy Osborne and us.
[558.20 --> 559.42]  I think that's kind of part of it as well.
[559.48 --> 560.86]  Who's behind Code for America?
[561.62 --> 567.82]  We're not really an incubator, but we're, like, a more traditional nonprofit, I would say, from a funding standpoint.
[567.82 --> 574.22]  So it's about half grant funding and half city funding, so the city governments pay us,
[574.38 --> 577.32]  and then we get a bunch of money from nonprofits and philanthropy.
[578.88 --> 586.52]  And, like I said, like, our goal is to try to prototype out some of these new ways of using technology in a government context.
[587.30 --> 592.96]  But we're not – I use the term startup, but we're not actually – we don't have startups.
[592.96 --> 599.70]  But probably a lot of the fellows this year are going to go on to continue working maybe in the startup space
[599.70 --> 601.70]  or working for governments doing this kind of work in the future.
[602.56 --> 608.88]  You mentioned LinkedIn as a sponsor or a partner, Cameron, which we said I think it's a partner, right?
[609.74 --> 610.00]  Yeah.
[610.88 --> 617.18]  How does that play into – like, companies like LinkedIn, Yahoo, I'm seeing some of the in-kind donors on your donors page.
[617.32 --> 619.60]  Is that – are those the partners you're mentioning?
[620.44 --> 620.64]  Yeah.
[620.64 --> 621.36]  Cisco Systems.
[621.36 --> 623.92]  The corporate world has been very generous to us.
[624.00 --> 627.40]  Cisco, as you mentioned, actually donated our office space to us.
[628.06 --> 632.66]  They made an acquisition last year and moved that company into their main headquarters,
[632.96 --> 636.94]  so they very generously donated that space to us.
[637.30 --> 643.68]  And a number of other partners – a number of other companies have made in-kind donations to us.
[643.78 --> 648.12]  Google has been very generous, especially their Summer of Code program.
[648.12 --> 657.32]  And we actually have 10 Summer of Code interns here for the summer working on civic apps and building open source libraries.
[657.66 --> 659.34]  So that's been a lot of fun.
[659.88 --> 664.82]  I'm surprised to not see Crunchbase's name in your list considering one of your project's names.
[665.02 --> 666.60]  But it's not actually the name.
[666.68 --> 667.30]  It's Shortstack.
[667.30 --> 669.14]  It's inspired by Crunchbase.
[670.76 --> 671.48]  What's that about?
[671.48 --> 672.28]  Sure.
[672.28 --> 679.44]  We thought it would be a good idea to basically have a repository kind of like Crunchbase, inspired by Crunchbase,
[679.84 --> 682.78]  but for governments and government-related software,
[683.14 --> 687.64]  so that if you're a city and you want to select some sort of software,
[687.64 --> 695.08]  you can see what other cities that are similar sized or maybe similar in geography are using to solve that problem
[695.08 --> 702.20]  and reach out to them and ask them questions about it or help that navigate through your selection process.
[703.04 --> 703.94]  I think it's kind of unique.
[704.14 --> 708.64]  I've had a number of desires to do something Crunchbase-like for –
[708.64 --> 710.98]  like, Wynn and I have talked about doing something like that for the open source world,
[710.98 --> 714.48]  but if only we had just a year of Sundays, I think, right, Wynn?
[716.06 --> 717.30]  It's kind of a fun idea, though.
[717.44 --> 719.66]  So it's wiki-based, I'm assuming?
[721.36 --> 725.06]  It's wiki-based in the sense that anyone can update it and edit it.
[725.12 --> 726.76]  It's actually a Rails app on the back end.
[730.48 --> 736.00]  You know, we've worked, I guess, in the startup community and the open source community for a number of years,
[736.00 --> 742.64]  and kind of in this echo chamber, we speak APIs and mashups and JSON and REST architecture and things of that sort.
[742.84 --> 747.58]  What sort of environment do you find when you walk into these government and civic projects?
[747.88 --> 751.08]  Do you have to sell them on concepts that we already speak, or how does that work?
[751.28 --> 752.64]  That's a great question.
[753.58 --> 758.60]  You know, most city governments are sort of Microsoft shops, .NET shops,
[759.00 --> 763.92]  and most of them have outsourced the majority of their IT, and they just work with consultants.
[763.92 --> 768.30]  They don't have a large team in-house doing application development.
[768.62 --> 774.56]  And so coming from sort of San Francisco startup world, open source world, you know,
[774.62 --> 780.54]  you don't see a lot of Linux servers running Apache or Rails or anything like that.
[780.78 --> 787.14]  So it's, you know, it's definitely a little bit of culture shock when we come into these governments,
[787.42 --> 790.60]  but our city partners, that's sort of what they signed up for.
[790.60 --> 796.64]  Are they, a lot of them, you know, cities right now are struggling to meet their financial obligations,
[797.30 --> 805.24]  and maybe they can't afford, you know, the big expensive databases and big expensive, you know,
[805.30 --> 809.30]  technologies that they've been paying for in the past.
[809.30 --> 814.28]  And so open source is sort of meets that need of being very cost efficient.
[814.82 --> 823.18]  But, you know, the problem is they just don't have the in-house expertise to bring those solutions to bear for their citizens.
[823.68 --> 831.80]  So that's sort of what we come in and do and sort of show them the ropes and teach them how to deploy these services in their city
[831.80 --> 836.22]  to make a better, cheaper solution for their citizens.
[836.22 --> 843.74]  Earlier today, actually, we had a really awesome lunchtime speaker, Carl Malamud, who does public.resource.org.
[844.44 --> 848.62]  And, like, Carl's claim, original claim to fame was in the open government world.
[848.70 --> 857.38]  Back in 1994, he got a grant, something like $30,000 to buy the SEC filing database that they were selling on a subscription basis.
[857.38 --> 862.14]  And then he just took one license of the data and put it up online so everybody could see the SEC filings.
[862.14 --> 866.52]  And since then, he's been, like, blazing a trail of taking huge data sets and making them available.
[866.74 --> 874.40]  And he really, I think, really eloquently illustrated a good model, which is any government that wants to build something that people are going to use
[874.40 --> 876.80]  should do it in three steps in this order.
[876.94 --> 883.00]  Like, put all the bulk data up online so that anybody can have access to bulk, raw information, developer-centric information.
[883.00 --> 888.82]  Then refine it into an API and try to make the data useful.
[889.04 --> 891.80]  And then build your website on top of that API and dogfood the API.
[892.30 --> 900.46]  And really, like, do it the complete opposite way that a lot of vendors, giant software vendors and the government are doing it right now,
[900.48 --> 902.00]  which is, like, we're going to build you a website.
[902.26 --> 907.66]  And then if enough people, like, complain to you about not having access to the information, maybe we'll build an API later.
[907.66 --> 910.16]  But you're not going to be able to get the bulk data out of it.
[910.60 --> 915.78]  And that's just one example of, like, an approach we're trying to, like, flip on its head in a bunch of the work that we're doing.
[916.02 --> 920.72]  And that's assuming that the government has digital data that is interesting to people.
[921.46 --> 926.28]  And a lot of our projects are, like, we'll show up at City Hall somewhere and say,
[926.80 --> 934.46]  oh, well, you must have a database of every pothole that's been, like, complained about in the city with a map, right?
[934.46 --> 935.36]  Like, that's an obvious.
[935.50 --> 939.08]  And then sometimes they're like, oh, no, actually, they're, like, locked up.
[939.14 --> 943.46]  Like, they're on paper or they're on another database in another building or there's no way to get it out.
[943.94 --> 946.20]  Or sometimes they do have it and it's not made available.
[946.34 --> 952.26]  And then that's a really kind of juicy scenario where we can take that and then turn it into a public API that a bunch of people can build,
[952.98 --> 957.86]  you know, see how many potholes are reported in your neighborhood or go fill in a pothole because the city is too busy to get to it
[957.86 --> 959.22]  or any of these sort of applications.
[959.22 --> 964.46]  And I think it's really awesome when we can find data that's already there.
[964.56 --> 971.52]  But one of the things we're having a lot of fun with this year is figuring out how we can generate data that the government doesn't have time or money to collect.
[971.74 --> 976.82]  Because sometimes the Venn diagram doesn't overlap of things the government's collecting and things that are interesting to people.
[977.00 --> 980.88]  But if the data were to get collected, it would be really helpful for the government for analytics.
[981.22 --> 985.80]  And it would also be really interesting to people and, like, boost citizen engagement in different areas.
[985.80 --> 994.26]  So we're looking at things like Ushahidi for doing crowdsourcing, that style of getting people to help out to build a data set.
[994.92 --> 995.66]  That's just fascinating.
[995.94 --> 1002.64]  You know, we talked to the Sunlight Foundation folks and they had this concept of a citizen coder.
[1002.70 --> 1006.20]  And you mentioned consultants and kind of the entrenched consultant world.
[1007.34 --> 1013.24]  Do you think this concept of a citizen coder is on the rise and does your organization kind of foster that?
[1013.24 --> 1016.00]  Yeah, we hope so.
[1016.12 --> 1037.40]  I mean, one of the things we want to do is take government data that's, you know, hidden in this either proprietary formats or in some database that nobody has access to or knows where it is or just hasn't been digitized and take that, get it up on the web, make APIs for it, give people access to it so they can be citizen coders if they want to.
[1037.40 --> 1042.40]  The first sort of step in enabling that is having the government's participation.
[1043.10 --> 1046.70]  And all this data, almost by definition, is public data.
[1046.86 --> 1051.62]  It's data that has been paid for by the taxpayers and, you know, should be public.
[1051.86 --> 1061.76]  There's no sort of reason or justification for keeping it behind closed doors other than either nobody's asked for it or technical incompetence.
[1061.76 --> 1063.76]  And so we try to solve both those problems.
[1064.34 --> 1070.48]  I think there's something like 30,000, like, municipalities in the United States, maybe more.
[1070.54 --> 1071.48]  I don't know the number off the top of my head.
[1071.54 --> 1072.78]  Some huge number like that, right?
[1073.08 --> 1076.30]  And we're working in three of them.
[1076.46 --> 1077.26]  They're bigger ones.
[1077.52 --> 1084.66]  But there's so many smaller, you know, like, multi-thousand people, like, 10, 20, 50,000 people cities around the country.
[1084.66 --> 1090.82]  And you forget about all the data we're getting, and you just look at our GitHub projects, for instance.
[1090.94 --> 1095.56]  Like, if you go to github.com slash Code for America, I think there's, like, 100-plus repositories on there.
[1096.04 --> 1098.84]  They're either things we've forked or things that we've made to solve different problems.
[1098.84 --> 1115.58]  Like, any of you listening out there in, like, let's say the Midwest, like, in your city, take one of our projects and clone it, change the title from the Boston Fire Hydrant Mapper to the Kansas City, Missouri Fire Hydrant Mapper and try to set it up.
[1115.58 --> 1130.52]  And what we really want to do at the end of our work, working on these projects, end of the first year and, like, continuing into future use of Code for America is make it super actionable for a single developer living in a city that doesn't have any of this fancy stuff, any of this fancy government technology that we're making.
[1130.90 --> 1136.28]  Like, making it really easy to clone a project and stand it up and start, like, peddling it around the city.
[1136.38 --> 1139.62]  Go and talk to your, like, community groups to start using this stuff.
[1139.62 --> 1152.56]  We want to really, like, kind of kickstart some of this, like, citizen engagement stuff so you can just have a single developer set up a project and then have all the tools that he needs to really get his community involved in it.
[1152.70 --> 1162.22]  Because we can solve the problem in a bunch of big cities, but I don't think that we'll be as successful if we don't get a bunch of, like, the huge long tail of all the small cities working on this stuff.
[1162.26 --> 1163.22]  So there's a lot of opportunity.
[1163.36 --> 1164.76]  All it takes is one person and one city.
[1165.42 --> 1167.42]  So you guys are in San Francisco, right?
[1167.80 --> 1168.02]  Yeah.
[1168.02 --> 1178.36]  And one of the states we hear a lot about with government, especially with budgetary things and deficit and stuff like that, and you mentioned one of the biggest things with government,
[1178.94 --> 1188.16]  is just meeting their revenue needs and having enough money to go around to take care of the technology that they have to do their jobs, I guess.
[1188.78 --> 1195.92]  You guys are in San Francisco, but I see Boston, Washington, Philadelphia, and Seattle on your list.
[1196.12 --> 1197.62]  Why not Cali?
[1198.02 --> 1212.34]  You know, like I said earlier, this was our first year, and we only have 20 fellows, and we sort of wanted to get a sort of select diverse group of cities from all across the country.
[1212.66 --> 1218.82]  And we might be working with some cities in California next year, but our headquarters is in San Francisco,
[1218.82 --> 1224.00]  and we think that makes sense for sort of being at the hub of technology.
[1224.36 --> 1233.54]  But we want to work all across the United States, and next year we're going to be expanding the number of cities that we're working in all across the country,
[1233.86 --> 1235.26]  including smaller cities.
[1235.74 --> 1240.28]  So, for example, Macon, Georgia is going to be one of the cities we're working with next year,
[1240.28 --> 1244.80]  which I'm guessing most of your listeners have never even heard of or don't know quite where that is.
[1245.44 --> 1246.46]  I don't actually know Macon.
[1248.38 --> 1249.58]  Not me either.
[1251.02 --> 1253.88]  So what is the selection process for the cities then?
[1253.88 --> 1262.70]  So the cities can apply to be a code for America city, and there's a proposal process that's actually closed now,
[1262.76 --> 1271.94]  but we go through the city selection process each year and come up with a list of cities that we think have sort of have the right people
[1271.94 --> 1283.08]  to be a little more experimental and try the code for America model and also who have an interesting project,
[1283.24 --> 1290.74]  something ambitious but also that we can take a pretty good crack at in one year because that's the length of the fellowship.
[1291.20 --> 1297.86]  The other half, too, is you don't necessarily need a city's involvement with us for us to have impact.
[1297.86 --> 1304.08]  There's a whole, like, spin-off organization between us and a group called Open Plans called Civic Commons,
[1304.82 --> 1309.58]  and Civic Commons is, the way that I describe it, is going to take all the Code for America projects
[1309.58 --> 1315.88]  and any other projects that we can get that fit a similar pattern and just, like, spread them around to every other city.
[1316.26 --> 1323.28]  So, for instance, if we go into Seattle and we build something that allows Seattle neighborhoods to talk to each other better,
[1323.28 --> 1328.50]  it's not like no other city in the United States has neighborhoods that need to communicate inside of their neighborhoods better.
[1328.90 --> 1335.60]  Like, we're really trying to pick, when a city applies to our program, we look at their problem and say, like,
[1335.62 --> 1338.24]  how generic, how universal of a problem is this?
[1338.38 --> 1340.14]  And most of the time, they're pretty universal problems.
[1340.22 --> 1341.68]  Like, every city could benefit from them.
[1341.68 --> 1349.56]  But at the same time, having somebody on the ground in a city to really, like, integrate the technical solution
[1349.56 --> 1352.08]  into the context of the community is really powerful, too.
[1352.42 --> 1356.06]  So, like I was mentioning earlier, like, it really, like, you have to have some software there
[1356.06 --> 1362.08]  because Rome wasn't built in the day, but you also, like, we can't just copy-paste Rome between all these different cities.
[1362.20 --> 1364.48]  Like, we need to have somebody, like, a team on the ground.
[1364.52 --> 1367.06]  But you don't necessarily need the city's involvement to do these things.
[1367.06 --> 1373.82]  Like, we're not in San Francisco city government, but because we're physically in SOMA,
[1374.30 --> 1378.48]  we've met with the innovation director, Jay Nath, at the city of San Francisco.
[1379.24 --> 1383.28]  And he, for instance, I was in a meeting with the art director for the city of San Francisco
[1383.28 --> 1385.64]  that we just, like, did on a Friday one time.
[1385.76 --> 1390.16]  Jay and I and another fellow, Anna, went over to the art director, his office,
[1390.30 --> 1392.36]  and got all of the art data for the city.
[1392.56 --> 1396.82]  So every location of every statue, like, public mural that the city has commissioned,
[1397.06 --> 1402.32]  and we're putting it into a mobile app and an API that people can help improve the city's art database.
[1402.88 --> 1407.04]  And then similarly, Oakland, right across the bay, we went over there,
[1407.08 --> 1409.18]  and they ran this event called Code for Oakland.
[1409.36 --> 1413.48]  That was the first time that the city had ever taken any data and said,
[1413.60 --> 1416.22]  hey, anybody that lives in Oakland, come and work with our data
[1416.22 --> 1418.08]  and see if there's anything cool you can build.
[1418.34 --> 1420.64]  And one of the projects that came out of that that I've been working on
[1420.64 --> 1424.18]  is a big wiki for social services, like homeless shelters.
[1424.18 --> 1428.06]  And Oakland specifically has a lot of reentry programs.
[1428.58 --> 1432.26]  When you get out of jail and you need to basically, like, rebuild your life,
[1432.66 --> 1434.74]  their government tries to help out a lot with that.
[1434.88 --> 1438.70]  But as you can imagine, like, the government websites for finding out about these services are really bad.
[1438.90 --> 1443.92]  So we're trying to take the data and then put it into a really appealing set of APIs
[1443.92 --> 1446.86]  that we're going to try to get a bunch of people in different cities to go around
[1446.86 --> 1449.50]  and fill out these databases of where all the homeless shelters are,
[1449.50 --> 1452.84]  where all of the food stamps offices are, and make them really actionable.
[1454.00 --> 1461.44]  So that's all stuff that's happened just by virtue of us being in physical proximity to these cities in the Bay Area.
[1461.88 --> 1465.88]  And I think that as more time goes on, hopefully more little projects pop up
[1465.88 --> 1469.28]  because somebody saw a really cool concept on one of our GitHub projects or something,
[1469.40 --> 1472.38]  and they said, whoa, there's a big opportunity in the city that I live in.
[1472.44 --> 1475.36]  Like, I'm just going to start going around and seeing if there's any interest.
[1475.36 --> 1481.02]  I'd like to switch gears for a minute and talk about the personal angle here.
[1481.20 --> 1486.06]  So, Eric, having worked with you, to use the word prolific would be a massive understatement.
[1486.20 --> 1489.68]  And looking at your page, Max, I think the same would be true.
[1489.96 --> 1495.84]  What does it mean career-wise to pursue this sort of position?
[1496.70 --> 1501.38]  I think we had visions of grandeur 10 years ago thinking we had to move out to the Valley
[1501.38 --> 1507.76]  and make a lot of money as a developer, but getting to code on open source can be just as, if not more, rewarding.
[1507.86 --> 1508.74]  What's it meant to you personally?
[1510.42 --> 1511.92]  Yeah, it's incredibly rewarding.
[1512.20 --> 1518.20]  I mean, being a Code for America fellow is definitely a pay cut for just about any developer,
[1518.66 --> 1520.66]  but that's not why you do it, right?
[1520.66 --> 1528.06]  And it's been being a part of the open source community, being able to sort of, you know,
[1528.62 --> 1537.08]  work on projects and go to conferences and have other people who I know and respect use those projects
[1537.08 --> 1538.54]  and contribute back to them.
[1539.36 --> 1541.62]  It's just an incredibly rewarding experience.
[1542.04 --> 1544.10]  And I think, you know, sort of no matter what I do next,
[1544.10 --> 1548.94]  that's always going to be a part of sort of what I do because it's important to me.
[1548.94 --> 1556.04]  And Code for America is basically a chance to go all out on that and spend a year, you know,
[1556.08 --> 1557.82]  just really focused on open source.
[1558.74 --> 1565.76]  You know, there's not a lot of jobs, you know, unless you're sort of a Yehuda Katz or someone like that,
[1565.90 --> 1570.30]  it's really hard to find a job where you get paid to write open source software.
[1571.48 --> 1574.42]  And Code for America, you know, you don't get paid that much,
[1574.42 --> 1580.34]  but again, you get the benefits of doing it, you know, in the community.
[1581.00 --> 1585.44]  And yeah, I think sort of my career prospects going forward are,
[1586.48 --> 1593.66]  I'm very satisfied with the career move, you know, taking a year off to do Code for America.
[1593.98 --> 1596.92]  It's been one of the best experiences of my life.
[1596.92 --> 1601.32]  And I also just, while we're talking about it,
[1601.38 --> 1605.84]  would mention that the deadline to apply for Code for America is coming up real soon.
[1605.94 --> 1607.14]  It's July 31st.
[1607.52 --> 1611.08]  And the URL to do that is codeforamerica.org slash apply.
[1611.30 --> 1614.84]  So I'd encourage anyone listening who's interested in it.
[1614.92 --> 1616.30]  It's been a great experience for me.
[1616.86 --> 1620.04]  And the application doesn't take too long to fill out.
[1620.22 --> 1622.26]  So go do that before the deadline.
[1622.26 --> 1629.92]  I think Wyn and I can both echo, you know, kind of what you said there with working on something that gives you that feel-good feeling.
[1630.14 --> 1635.84]  It's nice to make money, but at the same time, it's really nice to honor your blessings and your talents
[1635.84 --> 1641.78]  and do something that is good for humankind in general in whatever way you see fit.
[1641.96 --> 1647.10]  I actually listened to one of the YouTube videos, Carla Masino, I think is how you say her name? Masino?
[1648.08 --> 1649.22]  Yeah, that's a great video.
[1649.22 --> 1655.82]  Yeah, she talked about, you know, just being able to, I mean, it's like a, it's an opportunity of a lifetime, really.
[1655.92 --> 1660.22]  I mean, you get to be chosen out of, I don't know how many get selected, but, or apply.
[1660.38 --> 1661.98]  But, I mean, it's really a cool thing.
[1662.12 --> 1667.64]  But, and, you know, like Wyn had mentioned, your GitHub profile is not lacking.
[1667.86 --> 1674.62]  And, you know, one of the projects we've actually been eyeing up on your profile, Eric, is Israel's admin.
[1674.62 --> 1680.60]  Have you made any use of that or progressed that in any capacity as kind of part of working with Code for America?
[1681.40 --> 1684.64]  Yeah, it's been, it's been growing incredibly fast.
[1684.98 --> 1690.64]  So for those who don't know, Rails admin is basically an automatic admin interface.
[1691.34 --> 1693.98]  Originally, I started developing it as Merb admin.
[1694.42 --> 1696.86]  I was a big Merb hacker back in the day.
[1696.86 --> 1701.38]  But then Merb and Rails merged into Rails 3.
[1702.30 --> 1711.76]  And as part of the Ruby Summer of Code, I actually mentored Bogdan Gaza, who's a Google Summer, or Ruby Summer of Code intern,
[1712.12 --> 1715.68]  to basically port over Merb admin to Rails 3.
[1716.38 --> 1718.34]  And that project's just taken off.
[1718.40 --> 1722.22]  I think it has over 2,000 watchers on GitHub.
[1722.22 --> 1727.66]  And it's basically just a really easy interface that anyone can use to edit data.
[1727.90 --> 1733.62]  So basically just the CRUD of CRUD applications that you'd perform to any database table.
[1734.22 --> 1736.24]  There's a nice, easy UI on top of that.
[1736.28 --> 1739.20]  And we're definitely using that in Code for America projects.
[1739.20 --> 1742.78]  And I've had a chance to develop that further as a Code for America fella.
[1742.78 --> 1748.42]  I like how open source gets to circle back and feel this, too.
[1748.54 --> 1760.24]  Like some of the initiatives you guys are working on, on just what it says is Code for America slash dot org slash issues is openness, participation, education, and efficiency.
[1760.48 --> 1762.22]  And we're all in this open source world.
[1762.32 --> 1768.30]  We get to contribute a small sliver of a fraction of what is in open source.
[1768.30 --> 1773.74]  But it's nice to see that come back in and still be used and probably get you up and running pretty quickly, too.
[1774.42 --> 1783.64]  I just actually made a graph on the new GitHub API, the v3 API, of the last year, the last 12 months of my life,
[1783.76 --> 1789.94]  and what the number of projects that I've had, like my activity on GitHub, just as an experiment to see.
[1789.94 --> 1799.60]  And last OSCON, last July, so about a year ago exactly, Tim O'Reilly actually recruited me, basically.
[1800.22 --> 1802.18]  And I got really excited about Code for America.
[1802.80 --> 1812.02]  I was still working at the startup I was at for another like four or five months, but then left to come down to San Francisco around December.
[1812.02 --> 1815.76]  But from July, in July I had like nine GitHub repositories.
[1816.38 --> 1823.52]  But then as soon as July hit, like now I'm at like 97 or something, and it was just like the chart just like skyrocketed.
[1823.62 --> 1832.80]  And I remember like I had like a nine to five, and then I would get off work and go in Portland to coffee shops until like nine or 10 or 11.
[1833.14 --> 1838.76]  And I was just like totally excited and like super pumped about all of the stuff in this space.
[1838.76 --> 1842.48]  And a lot of the projects I work on are like data-driven.
[1843.74 --> 1850.38]  Two of the big themes I would say are like getting people out in a community, like taking photos of funny things and putting them on maps.
[1850.60 --> 1852.26]  Like I come back to that concept a lot.
[1852.62 --> 1858.28]  And I started with like mapping smells in a city and making a big like what smells are where.
[1858.36 --> 1863.62]  And then I got into like mapping feral cats and then mapping food trucks in Portland.
[1863.62 --> 1869.52]  And then now I'm like mapping homeless shelters and trying to, you know, like expand upon all of these mapping things.
[1869.62 --> 1876.46]  But then the other stuff that I'm working on, which isn't necessarily Code for America related, but I would say still like philosophically it's in the same category,
[1876.72 --> 1881.96]  is like identity and privacy and social network user-centric.
[1882.26 --> 1888.00]  The whole like there's a really great podcast that Brendan Eich did like yesterday on a minute with Brendan.com,
[1888.00 --> 1892.82]  where he talks about Mozilla's new strategy for we put the user first.
[1893.20 --> 1895.70]  And that's like hit the nail on the head of all the stuff that I'm really passionate about.
[1895.90 --> 1902.04]  So being in an environment that's trying to solve the problem of I'm a citizen in a city.
[1902.30 --> 1907.10]  How do I get more hooked into the way that my community is working?
[1907.60 --> 1912.94]  I heard somebody describe government as a tool that exists to foster communities.
[1912.94 --> 1919.82]  Like that should be the goal of a civic, like a local government is like all it should do is make sure that your communities like blossom.
[1920.22 --> 1922.28]  And I totally believe in that definition.
[1922.56 --> 1932.60]  But either if you're a user online like using Facebook or you're a user online trying to like file your taxes or you're a user online trying to like talk to somebody in line while you're waiting at the coffee shop.
[1932.70 --> 1937.34]  Like I'm really interested in like user-centric design and like what software allows people to do.
[1937.46 --> 1941.10]  And I'm totally, it's like consumed my life the last year.
[1941.10 --> 1941.72]  It's kind of crazy.
[1942.08 --> 1944.24]  Like GitHub is definitely an addiction for me lately.
[1944.66 --> 1947.36]  Well, we're definitely in the generation G, right, Wyn?
[1948.18 --> 1949.06]  That's true.
[1950.34 --> 1956.06]  So Eric, a number of your projects that you're actively working on aren't really your projects.
[1956.26 --> 1966.18]  And I know I'm thankful that you've pitched in on a few of mine where I've started an idea and haven't pushed it as far as I think you and others in the community have.
[1966.18 --> 1973.08]  What sort of satisfaction do you get from, I guess, working on somebody else's project?
[1974.64 --> 1988.84]  Well, I think there's a big tendency among engineers to, you know, look at somebody else's code and sort of get frustrated with it, with some aspect of it, and want to just kind of reinvent the wheel from scratch.
[1988.84 --> 2004.66]  And I think one of the great things about GitHub is that it makes it so easy to look at somebody else's code that, you know, maybe, you know, you think you could improve and actually make it better rather than trying to fork it and compete with it.
[2004.66 --> 2011.12]  And so, you know, there's nothing wrong with healthy competition if two projects have different goals in mind.
[2011.18 --> 2017.62]  But if you're fundamentally trying to do the same thing, then my philosophy is don't reinvent the wheel.
[2017.86 --> 2024.96]  And so Wyn, I think the first project we ever collaborated on was actually John Neunemaker's Twitter gem.
[2025.12 --> 2025.56]  That's right.
[2025.56 --> 2035.18]  Which he had built and then sort of moved on to working on Mongo Mapper and God knows what else he works on.
[2036.00 --> 2038.52]  He has quite the open source resume as well.
[2039.00 --> 2044.60]  But he wasn't investing a lot of time in the Twitter gem and he had sort of handed it over to you.
[2044.60 --> 2051.28]  And I was working on a startup called 140 Proof at the time, which was a Twitter startup.
[2051.48 --> 2056.40]  We used the Twitter API heavily and we needed a Ruby library to interface with Twitter.
[2057.16 --> 2062.94]  And I think it started with I just wanted to make some enhancement to the Twitter gem.
[2062.94 --> 2066.64]  It, I think, didn't upload images correctly.
[2067.04 --> 2074.40]  And, you know, we wanted to be able to update someone's profile icon or background wallpaper programmatically.
[2074.40 --> 2077.44]  And that wasn't supported in the Twitter gem.
[2077.56 --> 2087.24]  So I think the first patch to it I ever made was adding sort of the ability to do a multi-part post to the Twitter API via the Twitter Ruby gem.
[2087.92 --> 2096.68]  And then from there, just kind of like Max said, just kind of got addicted to making improvements to it and polishing things off.
[2096.68 --> 2113.08]  The biggest conversion was switching over from John Nunamaker's HTTP party as the HTTP client library, switching that over to Faraday, which is kind of like a meta HTTP client library.
[2113.08 --> 2120.90]  So you can use NetHTTP or Typhius or EM Synchrony if you want to, if you're on a vent machine.
[2121.90 --> 2129.32]  So that seemed like a refactor worth doing because people wanted to be able to swap in their favorite client library.
[2129.32 --> 2132.08]  And then I just sort of started moving up the stack.
[2132.08 --> 2145.36]  So the more I got into Faraday, the more I wanted to make some changes there and became a core team member of Faraday and started making some contributions to that.
[2145.36 --> 2150.34]  And that's basically been most of my open source.
[2151.66 --> 2153.40]  That's Technowini.
[2153.72 --> 2160.60]  Rick Olson's project started it and now Mislav, also at GitHub, does a lot of work on that project as well.
[2161.48 --> 2164.60]  But, you know, more than probably Rick does these days.
[2165.52 --> 2173.26]  But it's another great open source project that, again, you know, could have tried to reinvent the wheel and start from scratch and do my own thing.
[2173.26 --> 2179.02]  But it just seemed like it was there and it was sort of good enough, a good enough foundation to make better.
[2179.40 --> 2183.52]  So that's sort of my philosophy on open source in general.
[2183.94 --> 2188.04]  It's all about, like, that community and that collaboration and working with other people.
[2188.70 --> 2193.00]  A tech book that had an impact on me a few years ago was Leading Geeks by Paul Glenn.
[2193.00 --> 2204.34]  And he talks about how, you know, as a group, we geeks kind of buck the normal power structure and we all gravitate to the alpha geek in the room.
[2204.64 --> 2208.20]  And I think that's why I love GitHub so much is it automates that process.
[2208.34 --> 2216.20]  It's easy just by looking at open code that's out there to see who's got a better grasp of the language or techniques and things like that.
[2216.20 --> 2226.64]  And we kind of all go through this progression of cargo culting to imitation to, you know, then kind of thinking on our own and, you know, being creative about it.
[2227.20 --> 2232.20]  I've learned an incredible amount just from looking at other people's code on GitHub.
[2232.46 --> 2235.24]  Who are you guys learning from on GitHub these days?
[2235.98 --> 2236.30]  Oh, man.
[2236.42 --> 2239.70]  So drinking game.
[2239.70 --> 2253.52]  So Jeremy, he, I remember I was working at this company, Revelation, and my boss, Dan Herrera, he's Wobot on Twitter, he was telling me that he found this book, Build Your, How to Write Your Own Freaking Awesome Programming Language.
[2254.16 --> 2259.04]  And he was saying, like, it talks about Lexers and Parsers and ASTs.
[2259.08 --> 2263.16]  And it was, like, this really interesting and really approachable way of getting into language design.
[2263.16 --> 2271.18]  And I guess Jeremy wrote, like, read that book and then wrote CoffeeScript as an implementation of the things that he learned in that book.
[2271.40 --> 2278.92]  So if you go to the really early days of the CoffeeScript repository, it's really fascinating to look and, like, see how the language was evolving back then.
[2279.42 --> 2280.82]  And just his style is really cool.
[2281.12 --> 2284.48]  And I love, like, the kind of temporal aspect of GitHub in that way.
[2284.56 --> 2286.80]  And you can go back and see that it started from nothing.
[2286.90 --> 2288.72]  And he just sort of, like, started adding things.
[2288.72 --> 2292.30]  And it really, like, grew and blossomed from, like, the ground up.
[2292.34 --> 2296.14]  And it kind of demystifies this, like, prolific programmer thing.
[2296.22 --> 2308.66]  It's, like, I don't think that, like, you have to be a genius or some sort of, like, whiz kid to be a really active developer or have a successful, like, open source, quote, unquote, presence.
[2308.66 --> 2311.24]  It's just, like, it's time and it's dedication.
[2311.60 --> 2318.74]  And you really just have to, like, have the, like, the ability to follow through with starting something.
[2319.36 --> 2327.26]  So one of my favorite things to do on projects is to go to the very beginning of the commits and just read the commits from the beginning and going forward.
[2327.74 --> 2332.52]  And I also am a big fan of, like, HTTP APIs for everything.
[2332.52 --> 2339.74]  You know that meme, the, like, all the things meme with the little cartoon character with his arms in the air, like, blank all the things?
[2340.20 --> 2343.52]  I made one last week that was REST API for all the things.
[2343.98 --> 2356.58]  And I think that, like, Eric was saying with, like, Faraday and some of these HTTP libraries, like, it's funny that after 20 years of having HTTP libraries or more than that, they're still really bad, in my opinion.
[2356.74 --> 2358.84]  Like, it's a really hard thing.
[2358.84 --> 2372.36]  Like, there's all these abstractions on top of HTTP libraries, and I've been having a lot of fun, like, looking at the ways that different languages do HTTP and which ones have their own weird abstractions on top and which ones are really minimal.
[2373.12 --> 2375.96]  And one of my favorite ones is in Node by Michael Rogers.
[2376.22 --> 2377.04]  It's just called Request.
[2377.82 --> 2382.10]  And it's Michael, M-I-K-E-A-L, Michael slash Request.
[2382.30 --> 2386.20]  And it's just, like, the most straightforward HTTP library you'd ever, ever use.
[2386.20 --> 2390.76]  And when I was, like, learning CouchDB, I was like, oh, it's full HTTP.
[2391.02 --> 2396.10]  Like, I better go find a Couch client library to use with Node or from JavaScript.
[2396.68 --> 2401.54]  And I was like, there has to be some really great library that's designed specifically for Couch that does all the HTTP stuff.
[2401.72 --> 2404.42]  I actually found out that Request was the best library to use.
[2404.76 --> 2407.46]  And you won't find the word Couch anywhere in the Request source code.
[2407.50 --> 2409.80]  It was just, like, it implemented HTTP really well.
[2409.80 --> 2421.12]  So there's always these, like, gems, no pun intended, that are just, like, they make a protocol like HTTP really easy to use and just make it really nice.
[2421.34 --> 2426.42]  And I love when I find systems that just, like, both implement the same contract together.
[2427.00 --> 2430.72]  And, you know, you have, like, the Request library in CouchDB as an example.
[2430.96 --> 2434.74]  They don't know anything about each other, but they work better than anything else.
[2436.02 --> 2437.38]  Anyway, that was kind of a tangent.
[2437.38 --> 2439.18]  No, good stuff.
[2439.48 --> 2441.50]  Eric, you mentioned a couple of folks.
[2441.56 --> 2442.68]  Anybody else you'd want to highlight?
[2443.22 --> 2446.64]  Oh, yeah, there's so many people, so many great people in the community.
[2446.80 --> 2450.44]  I really enjoyed the podcast you guys did last week with Sam Stevenson.
[2451.02 --> 2452.78]  I have so much respect for that guy.
[2452.94 --> 2458.82]  And after listening to it, I just dove in on some of his projects just to check out the code.
[2458.82 --> 2462.00]  And, yes, Sam's awesome.
[2462.78 --> 2463.90]  Really enjoyed that interview.
[2463.90 --> 2475.20]  You know, also, the Rubinius guys, like, specifically Brian Ford and Evan, like, I just think Rubinius is an awesome project.
[2475.70 --> 2481.00]  And I have a lot of respect for those guys as well and the work that they're doing.
[2481.00 --> 2489.06]  So, yeah, there's so many great people in the open source community like that who, you know, you sort of follow them for a while.
[2489.14 --> 2492.88]  And then, you know, you don't really know what they're like in person and then meet them at a conference.
[2492.88 --> 2499.10]  And they're just, like, super down to earth and will answer all your questions and really nice people.
[2499.26 --> 2501.24]  You know, I put Jeremy in that category as well.
[2501.24 --> 2504.50]  So that's great.
[2504.62 --> 2512.74]  You know, for me, that's really the most rewarding thing about working in open sources is the people, you know,
[2512.76 --> 2515.92]  just being able to work with so many talented people as peers.
[2516.22 --> 2519.28]  And, you know, you contribute to their projects.
[2519.28 --> 2520.98]  And if you're lucky, they accept your patches.
[2521.42 --> 2525.62]  And, you know, maybe if you're really lucky, they'll start contributing to yours.
[2525.62 --> 2533.22]  And there's just sort of that give and take component to it that there's nothing like it.
[2533.30 --> 2536.54]  I mean, for me, it really is an addiction.
[2537.22 --> 2543.62]  You know, one of the things that I like about this community is we tend to talk in projects and usernames and logins
[2543.62 --> 2546.44]  and not so much the real names behind a lot of these projects.
[2546.58 --> 2548.56]  And I know that I've been at conferences.
[2549.42 --> 2555.20]  And, for instance, one of the guys that helps us with the Twitter gem introduced himself to me at South by Southwest
[2555.20 --> 2556.46]  is Steve Reichert.
[2556.64 --> 2558.28]  And I just kind of puzzled.
[2558.34 --> 2559.08]  And he said, Laser Lemon.
[2559.24 --> 2560.58]  Oh, Laser Lemon, right?
[2561.10 --> 2566.18]  It's just this whole community around where the projects are almost as big as the personalities behind them.
[2566.72 --> 2570.06]  Yeah, and I definitely give a big shout-out to Steve.
[2571.24 --> 2576.18]  He came in right as we were about to release 1.0 of that gem
[2577.84 --> 2582.60]  and really just completely rewrote some of the interfaces, refactored them,
[2582.60 --> 2586.96]  and made them much, much nicer so that we could have a really solid 1.0.
[2587.20 --> 2594.30]  And he also works on a number of interesting projects, including the simple OAuth gem,
[2594.42 --> 2597.62]  which is like the best gem for doing OAuth and Ruby.
[2598.30 --> 2601.52]  And he also blogs for Collective Idea, where he works.
[2602.00 --> 2606.18]  And I'd highly recommend subscribing to that blog.
[2606.32 --> 2608.04]  He writes some really interesting stuff.
[2608.04 --> 2611.26]  So, yeah, definitely a shout-out to Steve.
[2611.62 --> 2612.98]  One last thing before we get to the radar.
[2614.36 --> 2618.46]  I know that you've been a proponent of folks not needing to know how to code
[2618.46 --> 2619.92]  to contribute to open source.
[2620.34 --> 2623.34]  What are some other ways that folks can get involved?
[2623.88 --> 2624.44]  Yeah, definitely.
[2624.44 --> 2629.54]  So I actually gave a talk on that at Redder RubyConf, which we both attended.
[2629.54 --> 2639.10]  And on almost every repository that I'm active on, I talk about the ways that different people can contribute.
[2640.22 --> 2644.16]  And because I want to set the barrier to entry really low,
[2644.24 --> 2649.30]  because I think writing open source code is sort of this addictive thing.
[2649.82 --> 2656.04]  And once you kind of get your foot in the door and get over that initial hurdle of intimidation,
[2656.16 --> 2658.36]  there's a lot of ways that people can get involved.
[2658.36 --> 2666.16]  And so with Rails Admin, for example, there's over 100 contributors on that project.
[2666.84 --> 2670.70]  And one of my favorite ways for people to contribute without knowing how to code at all
[2670.70 --> 2673.36]  is just translating it into a different language.
[2673.50 --> 2679.98]  And I think Rails Admin now has been translated into 15 or 20 different languages all over the world.
[2680.20 --> 2683.80]  So, you know, that's a great thing for someone to come in and do.
[2684.00 --> 2685.74]  And it really helps.
[2685.74 --> 2687.62]  It's like people are using it all over the world.
[2688.18 --> 2689.38]  And it's great to see that.
[2689.96 --> 2695.98]  Just like using alpha and beta and pre-release versions of software is helpful.
[2696.24 --> 2699.94]  And reporting bugs and issues is great.
[2699.94 --> 2706.52]  You know, suggesting new features, writing documentation, editing existing documentation.
[2707.22 --> 2713.48]  God knows there's tons of typos in open source software documentation all over the place.
[2713.72 --> 2715.52]  And it's just not well written.
[2715.64 --> 2720.94]  A lot of programmers aren't as great at writing prose as they are at writing code.
[2720.94 --> 2727.50]  And somebody with an English background can come in and make a lot of progress there.
[2729.06 --> 2731.04]  You know, also just like really small fixes.
[2731.30 --> 2733.38]  Just like setting the bar really low in your project.
[2733.56 --> 2736.24]  Like I always say, you know, a patch.
[2736.38 --> 2742.82]  I'll always accept patches that add documentation, add comments, clean up inconsistent white space,
[2743.58 --> 2746.24]  alphabetize things that are sort of out of order.
[2746.24 --> 2748.00]  Or just neaten things up.
[2748.86 --> 2754.58]  For me, like those are some of my favorite patches to receive because they're often from people who've never contributed to open source before.
[2754.72 --> 2761.78]  And it is that like that visceral feeling of contributing in the way that they can and at the level that they feel comfortable doing.
[2762.06 --> 2763.20]  Or just removing white space.
[2763.92 --> 2765.00]  Yeah, just removing white space.
[2765.00 --> 2776.20]  Honestly, like as a Vim user, I'm used to jumping between sort of code blocks with shift bracket, like open bracket and close bracket.
[2776.88 --> 2779.14]  And I think it's text mate.
[2779.34 --> 2785.54]  But one of the editors is terrible about if there's an empty line, it indents it to the level of the previous line,
[2785.60 --> 2787.52]  even though there's nothing on that line.
[2787.60 --> 2789.14]  Like there's no reason for it to be indented.
[2789.14 --> 2796.24]  And that actually breaks workflow for a lot of Vim users.
[2796.66 --> 2798.08]  And it also, like Git doesn't like it.
[2798.20 --> 2805.72]  Like Git will highlight it and make it kind of like it will show up as highlighted in Git when you try to commit it.
[2806.18 --> 2809.18]  So just pulling that stuff out is a great contribution.
[2809.38 --> 2813.76]  It's like a little thing that you can do that makes it a little bit better for everyone who's using it.
[2813.98 --> 2815.34]  And that's what open source is all about.
[2815.34 --> 2822.04]  I think it actually might be text mate that does that because I know that whenever I do a return from a new line, it's indented.
[2822.26 --> 2826.28]  It goes to the start point of the next or the previous line.
[2826.84 --> 2834.32]  Yeah, and for people who want to keep using text mate and not piss off Vim users, there's actually a text mate plug-in.
[2834.32 --> 2848.26]  Maybe you can put it in the show notes, but there's like a text mate like before save hook that will go through and clean up all of the terrible white space and indentation that text mate inserts.
[2848.82 --> 2859.16]  So like honestly, just doing that is like a big, if everyone who's listening to this who uses text mate just did that, that would be a big contribution to the open source community.
[2859.40 --> 2860.90]  Especially if you commit to open source.
[2860.90 --> 2864.08]  Yeah, yeah, that's right.
[2864.10 --> 2865.00]  If you're just doing your own code.
[2866.02 --> 2879.92]  Well, but even at work or whatever, I think just writing, it's sort of like the postal principle of writing code that could be accepted by the most editors or whatever.
[2880.16 --> 2880.46]  Right.
[2880.72 --> 2882.54]  That won't break parsing in the most editors.
[2882.54 --> 2890.66]  There's just little things like that that you can do that are a little bit just considerate of other developers.
[2890.66 --> 2891.86]  A good practice to follow.
[2892.64 --> 2901.28]  One of the things that's really fun this year at Code for America is that we have open source projects, but they're not, like the target audience for a lot of them isn't just developers.
[2901.46 --> 2905.12]  It's also like users or people who are going to stand them up in different cities.
[2905.28 --> 2908.14]  So it's really interesting to say, okay, we have GitHub.
[2908.14 --> 2916.08]  How is GitHub going to be our way of managing people who aren't even programmers or even like working with designers?
[2916.20 --> 2923.36]  And I think that like the new GitHub for Mac app is really cool from the like eliminating the command line for people who have never been on the command line anymore.
[2923.36 --> 2928.56]  They can still have, they can still take part in like distributed version control workflows.
[2929.04 --> 2931.14]  And like the GitHub image diffs are really cool.
[2931.40 --> 2936.64]  I was talking with Tom Preston-Werner, TP-Dubs from GitHub about there's this guy who gives this presentation.
[2936.84 --> 2942.96]  We were both there about these mechanical, every piece of machinery you can imagine to run a farm.
[2942.96 --> 2948.70]  He's been designing open source versions of these like systems.
[2949.02 --> 2954.58]  So you could like, you could download the schematics for a tractor and then build it for as cheaply as possible.
[2954.72 --> 2958.72]  And he's trying to build like a hundred machines, a hundred open source machine templates.
[2959.04 --> 2960.58]  And so he has a lot of 3D models.
[2960.96 --> 2964.98]  And he's talking to Tom about like, hey, how do I do 3D models on GitHub?
[2965.16 --> 2966.54]  Like when are you going to implement that feature?
[2966.66 --> 2969.18]  And then Tom was like, well, you know, we could do like WebGL rendering.
[2969.40 --> 2971.02]  And it's like, it's really exciting stuff.
[2971.02 --> 2973.02]  Like the idea that it's not just code anymore.
[2973.18 --> 2978.60]  It's going to be like any sort of, we have a file that we want to collaborate on and use GitHub as the hub for that.
[2979.02 --> 2983.58]  I was reading this book by Ted Nelson, the dude that invented hypertext back in the day.
[2983.76 --> 2985.18]  And it's called Literary Machines.
[2985.26 --> 2989.30]  It's really hard to find for whatever reason, even though it's like the book about the internet before the internet.
[2989.50 --> 2996.24]  And he was describing in Literary Machines like what he thought the internet was going to be back before we had the internet.
[2996.24 --> 3000.22]  And it was like, well, everybody's going to have like their version of a document.
[3000.22 --> 3003.14]  And if they make changes to it, they could submit it into the repository.
[3003.50 --> 3006.92]  And you could see all the forks that somebody, he didn't use any of these terminologies,
[3007.02 --> 3008.60]  but you could see all the forks that somebody's made.
[3008.68 --> 3010.90]  And everybody will be able to collaborate on editing things.
[3011.24 --> 3013.78]  And it's like, here we are 30 years after that book was written.
[3014.04 --> 3015.36]  And what do we have to show for it?
[3015.36 --> 3018.14]  We have Wikipedia, which is like its own universe.
[3018.22 --> 3019.04]  And then we have GitHub.
[3019.84 --> 3023.90]  There's been many source control platforms over the years, of course.
[3023.90 --> 3030.90]  Not to discredit any of them, but I think GitHub has really hit the nail on the head in terms of actually like realizing this vision of like,
[3031.06 --> 3034.70]  let's just make information into this thing that we can all help to build.
[3035.26 --> 3041.04]  And it's a really exciting time, like imagining the uses of this technology for things other than just code.
[3041.04 --> 3051.44]  And from a Code for America standpoint, like with the open211.org project that I'm working on, we contacted, I did a who is on open211.org.
[3051.48 --> 3051.90]  It was taken.
[3052.56 --> 3054.50]  I contacted the woman who was in charge of it.
[3054.96 --> 3055.86]  I sent her an email.
[3055.98 --> 3057.16]  I'm like, hey, we're Code for America.
[3057.32 --> 3060.98]  We're this nonprofit trying to build a big wiki of all of the homeless shelters, basically.
[3061.54 --> 3064.96]  And she was like, oh, my God, I saw Tim O'Reilly give a talk about this once.
[3065.16 --> 3065.98]  I love you guys.
[3066.12 --> 3066.94]  Like, have the domain.
[3067.02 --> 3068.10]  I'm transferring it to you right now.
[3068.14 --> 3069.00]  What else can I do to help?
[3069.06 --> 3075.70]  And I'm like, well, go to GitHub and make an account and then use the fork and edit button and just like clean up any of our copy.
[3076.14 --> 3081.40]  Like, if you go to open211.org, it's supposed to be a page that describes the project.
[3081.76 --> 3087.88]  And I have like a few months ago realized that I should be making screencasts about every project that I do.
[3088.08 --> 3089.74]  I should be doing readme-driven development.
[3090.68 --> 3099.68]  I should, you know, like try to make every project that I do as much of a template for other people to either take and reuse in some other domain or to just make it really easy for people to get involved.
[3100.10 --> 3107.04]  And this woman actually made a GitHub account and was able to like fork and edit our readme, which is really cool.
[3107.32 --> 3109.32]  So I think like the tools are coming a long way.
[3109.32 --> 3115.18]  And like Google Code has had the fork and edit feature in browser for a while.
[3115.42 --> 3117.82]  And like it's just like bridging the gap from developer.
[3117.82 --> 3128.70]  Like I actually, every startup that starts up nowadays, like I'll look at it and be like, well, are those things that developers could do 20 years ago that now only we're getting around to making it accessible to every person?
[3129.18 --> 3130.54]  And that's a really fun game to play.
[3130.54 --> 3136.76]  So like there's IRC cloud now, which is like IRC without having to know how to run a screen session.
[3137.32 --> 3139.94]  Or even you could argue that like Twitter is like IRC for everybody.
[3140.58 --> 3146.36]  Or there's like, I don't know, there's like all these things that we never build for people that aren't developers.
[3146.48 --> 3151.40]  But it's not that non-developers aren't nerdy enough to do these kind of like distributed editing things.
[3151.50 --> 3154.30]  It's just that, anyway, what I'm getting at is it's a really exciting time.
[3154.30 --> 3161.30]  I had that aha moment today too before we got on the call whenever I jumped on the Code for America org on GitHub.
[3161.42 --> 3164.04]  I was like, wow, 118 repos, 51 members.
[3164.92 --> 3172.14]  Like this is the epicenter of everything that you guys are doing revolving around your code bases and your projects.
[3172.38 --> 3180.04]  This is, you know, this is, I mean, this is the, if you had to say a deliverable, this is the deliverable pretty much until you actually get to production.
[3180.04 --> 3181.88]  But it's pretty wild.
[3182.10 --> 3183.76]  But we're almost out of time.
[3183.90 --> 3189.56]  So the last question I'd like to ask is about, you know, what's fun in your world with open source?
[3189.70 --> 3190.38]  What are you playing with?
[3190.46 --> 3193.66]  Max, I know you said you're a big fan of CouchDB.
[3194.42 --> 3197.26]  And Michael, you'd mentioned that, you know, you're Rubyist.
[3197.36 --> 3199.62]  So I imagine that those are probably camps you'd like to play out in.
[3199.74 --> 3204.18]  But if you had to venture out of that camp, what is something fun that you might want to play with in open source?
[3204.18 --> 3211.42]  I've been playing around with Socket.io a little bit recently on Node.
[3211.90 --> 3215.82]  And that seems really cool.
[3216.02 --> 3224.28]  Like it seems like something that was kind of like Max said, like it's something that would have been pretty hard to do just a few years ago.
[3224.28 --> 3231.30]  But now it's becoming mainstream and it's going to enable a lot of new products and new technologies.
[3231.30 --> 3234.04]  So that's kind of my little hobby project these days.
[3234.46 --> 3243.78]  I also, this is within the Ruby realm, but I think one sort of way to be a good open source citizen,
[3243.96 --> 3250.92]  especially if you're doing library development, is to test your library across multiple different versions of Ruby.
[3251.52 --> 3255.42]  And the best way, easiest way I've found to do that is to use Travis CI.
[3256.16 --> 3258.28]  So I definitely want to give those guys a plug.
[3258.28 --> 3259.88]  It's a great product.
[3260.14 --> 3262.24]  It's still new and there's still some bugs in it.
[3262.24 --> 3279.60]  But it's incredibly easy to get set up and basically with one YAML file have free hosted continuous integration for your project on JRuby, Rubinius, 187, 192.
[3279.60 --> 3287.54]  And that way, you know, when you do development, you don't want to run your tests, you know, end times once for each Ruby.
[3287.80 --> 3293.80]  But you want to make sure that it's compatible with every Ruby out there so that the most people can use it as possible.
[3293.80 --> 3299.40]  And that's been an invaluable tool for all the Ruby libraries that I work on.
[3299.84 --> 3307.60]  I've been bugging Josh and those guys to come on the show and they keep saying when we get to a 1.0 and told them now that they're building Rails nightly, they have to come on.
[3307.86 --> 3309.48]  So they'll be in a future episode.
[3310.20 --> 3310.54]  It's cool.
[3310.54 --> 3320.66]  I've been doing a little bit of hacking on GemCutter as well, the rubygems.org site, which is an awesome Rails app.
[3320.90 --> 3331.44]  Like, I would say if people are looking for, like, a high-profile project that they want to work on, Rails project, we're working on getting that up and running on Rails 3.1.
[3331.54 --> 3332.94]  Right now it's on Rails 3.0.
[3332.94 --> 3335.98]  And there's just a bunch of features that you could add there.
[3336.08 --> 3352.80]  It's like if someone wants to sort of get their, earn their chops using a, on a high-scale, you know, high-visibility Rails app, submit some patches to rubygems.org because that's a great project.
[3352.90 --> 3356.34]  We just got that up and running on Travis last night as well.
[3357.06 --> 3359.32]  Travis is great because there's no way I'm going to be running.
[3359.32 --> 3365.54]  Even with RVM, I'm not going to test my test suite against Ruby Enterprise and JRuby and the whole nine yards.
[3365.70 --> 3367.24]  I'll let Travis do that heavy lifting.
[3368.30 --> 3368.70]  Exactly.
[3369.16 --> 3377.86]  Some of the stuff I'm excited about lately, like two weeks ago I found this repository called Substance, and it's by Michael on GitHub.
[3378.46 --> 3380.16]  I'm not going to try to pronounce his last name.
[3380.26 --> 3381.20]  He's a Belgian or Austrian.
[3381.20 --> 3382.80]  Sounds like Michael needs to come on the show.
[3383.48 --> 3384.08]  He's amazing.
[3384.08 --> 3395.16]  Michael, just like the normal way you spell Michael on GitHub, they're at this place called Quasi Particle, which is like an Austrian software development shop.
[3396.18 --> 3398.96]  He has some of the best projects that I've seen in a while.
[3399.04 --> 3408.90]  And basically it's like an HTML5-based document editor, not unlike something like Google Docs or like a WYSIWYG editor.
[3408.90 --> 3414.68]  But it has this really cool, like he has this thing called data.js that's a persistence layer.
[3414.78 --> 3421.02]  So anytime you type in a document into the editor, it's persisting it into a graph document format in JSON in your browser.
[3421.32 --> 3425.60]  And then he has like a replicator that replicates to CouchDB, which I really liked that part.
[3425.96 --> 3434.18]  But basically like he's trying to build this really amazing suite of all GPL or MIT-licensed editing tools that are just like really, really well designed.
[3434.18 --> 3436.84]  I was really blown away by the quality of the work that he's doing.
[3438.04 --> 3440.84]  And so I was like talking with him online the other day.
[3440.88 --> 3442.14]  I'm like, wow, this is really cool stuff.
[3442.22 --> 3447.26]  Like I've been coming at a lot of these problems from a structured data standpoint of like how do we make data better?
[3447.34 --> 3448.18]  How do you clean up data?
[3448.56 --> 3455.46]  But he's coming from like the kind of qualitative, unstructured data standpoint of how do we make like document authoring really easy?
[3455.58 --> 3461.50]  And like build an HTML, like JavaScript, HTML5, like WYSIWYG editor that doesn't suck.
[3461.50 --> 3468.24]  And I don't know, I just got really jazzed by the amount of like design skills that he has.
[3468.28 --> 3470.54]  And a lot of his theories on data were really cool.
[3471.36 --> 3478.40]  Another really amazing like set of projects that I saw, Substack in the Node.js community.
[3479.94 --> 3485.74]  Isaac, who does NPM in Node, called Substack the why of JavaScript.
[3486.44 --> 3487.26]  Why the lucky stiff.
[3487.26 --> 3493.70]  And why the lucky stiff was actually like the guy that got me excited about programming in a kind of artistic way in my spare time.
[3494.44 --> 3496.48]  And Substack, his name is James Halliday.
[3496.58 --> 3497.92]  He has a startup called Browserling.
[3498.38 --> 3503.84]  And like if you go to Browserling.com or you go to Substack on GitHub and you look at any of the repositories from the last few months,
[3504.14 --> 3507.30]  every single one has a hand animated character that represents the repository.
[3507.30 --> 3514.60]  And the other day I was using, he has this thing that you can convert a Node module, server-side JavaScript,
[3514.86 --> 3518.60]  into a requireable module for client-side JavaScript called Browserify.
[3518.96 --> 3525.18]  And you click on the repo and it's like there's a Harry Potter, a hand-drawn Harry Potter character in the repository.
[3525.18 --> 3526.94]  It has nothing to do with Browserify or anything.
[3527.22 --> 3530.42]  But I sent him a pull request because I added an example into the readme.
[3530.42 --> 3535.60]  And I used, he was like making a Voldemort reference.
[3536.06 --> 3542.56]  And he was like, Voldemort is to Node, or is to JavaScript is CommonJS.
[3542.70 --> 3543.08]  I don't know.
[3543.12 --> 3544.56]  It was like this crazy awesome thing.
[3544.60 --> 3546.44]  But now he's going to like add a Voldemort character to his repo.
[3546.52 --> 3549.42]  But if you go to Browserling.com, it's all hand animated by him.
[3549.58 --> 3553.64]  And it's like a cross-environment browser testing tool that you can test your website in different browsers.
[3554.20 --> 3556.90]  But everything, all the UI is like hand animated.
[3557.00 --> 3557.50]  It's amazing.
[3557.50 --> 3560.28]  It's like a totally labor of love.
[3560.42 --> 3562.36]  He has a lot of, he's a very prolific programmer too.
[3562.80 --> 3564.68]  So fork some of his projects and add animations.
[3565.56 --> 3566.34]  Good stuff.
[3566.50 --> 3566.76]  Wow.
[3567.30 --> 3569.28]  Well, I think that about wraps it up.
[3569.36 --> 3575.26]  I know that we certainly appreciate you guys taking the time to come on the show and give us a peek behind the veil of Code for America
[3575.26 --> 3579.34]  and the great stuff that you're doing for civic communities and our cities out there.
[3579.42 --> 3584.22]  I know we certainly appreciate you taking the time out of your careers to do that,
[3584.22 --> 3589.96]  whether it's great for you in your future or if it's just a year of wild coding or whatnot.
[3590.18 --> 3592.02]  But we certainly appreciate the time you've given us today.
[3592.68 --> 3593.08]  Great.
[3593.24 --> 3594.78]  Thanks for having us on.
[3594.84 --> 3595.78]  We really appreciate it.
[3595.84 --> 3600.16]  And I'm going to plug the Code for America Fellowship one more time.
[3600.52 --> 3602.46]  The deadline to apply is July 31st.
[3602.50 --> 3605.72]  So go to codeforamerica.org slash apply and check it out.
[3606.28 --> 3606.68]  Do it.
[3606.76 --> 3607.20]  Do it now.
[3607.54 --> 3609.00]  We'll definitely put that in the show notes.
[3609.14 --> 3609.70]  Thank you, guys.
[3609.70 --> 3610.90]  Bye.
[3611.18 --> 3612.18]  Bye.
[3612.72 --> 3613.32]  Bye.
[3613.82 --> 3613.86]  Bye.
[3615.56 --> 3615.98]  Bye.
[3618.38 --> 3618.44]  Bye.
[3619.76 --> 3620.42]  Bye.
[3621.08 --> 3621.34]  Bye.
[3624.52 --> 3624.70]  Bye.
[3632.78 --> 3636.92]  Bye.
[3637.32 --> 3637.42]  Bye.
