[0.00 --> 23.42]  Welcome to the ChangeLog, episode 0.1.3. I'm Adam Stachowiak.
[23.42 --> 28.34]  And I'm Wynne Edlin, and this is the ChangeLog, bringing you what's fresh and new in the world of open source.
[28.34 --> 32.18]  We follow the projects and people of open source software.
[32.34 --> 37.96]  You can check us out at thechangelog.com or for a real-time view, tail.thechangelog.com.
[38.04 --> 42.66]  You can also check us out at GitHub, too, as well, at github.com forward slash explore.
[43.10 --> 48.98]  You can check out some training repos there, a la GitHub, or some feature repos from our blog, thechangelog.com.
[49.38 --> 53.92]  And you can also check out some of the latest episodes of the ChangeLog right there if you're listening to pleasure.
[53.92 --> 60.52]  And we're also on the Twitter at changelogshow. And you can follow me personally. I'm Penguin, P-E-N-G-W-Y-N-N.
[60.68 --> 61.80]  And where do you tweet, Adam?
[62.16 --> 65.08]  I'm Adam Stach on Twitter, Adam S-T-A-C.
[65.32 --> 71.52]  Very cool. We've got a good episode this week. Talk to Luigi Montanez and Jeremy Carball from Sunlight Labs.
[71.86 --> 74.32]  Yeah, they're doing some pretty cool stuff in open source, huh?
[74.64 --> 77.60]  They are. A ton of projects out on the GitHub.
[78.00 --> 78.54]  The GitHub.
[78.54 --> 83.14]  The GitHub.com forward slash Sunlight Labs.
[83.34 --> 85.98]  Yeah, they got 63 repos last time I checked.
[86.26 --> 90.26]  And one of the more interesting ones we didn't talk about in the interview. I wish we would have had a chance.
[91.32 --> 94.40]  But 63 repos, you can't talk about all of those in one interview.
[94.92 --> 97.12]  Real Time Congress at realtimecongress.org.
[97.64 --> 105.26]  It's an iPhone app built with Titanium AppCelerator, which we talked about in episode 0.0.8, I believe, with Marshall Culpepper.
[105.26 --> 106.08]  Yeah, yeah.
[106.16 --> 113.16]  Very cool framework to build iPhone apps with technology that you probably already know, web development technologies, HTML, CSS, JavaScript.
[113.42 --> 118.38]  But Real Time Congress allows you to keep tabs on those you've elected and sent to DC.
[118.88 --> 128.58]  Yeah, absolutely. I think it's pretty cool, too, how we mentioned them being a multi-language kind of environment, how they support each other and how they play well together.
[128.86 --> 134.40]  Yeah, could you believe we had a Rubius and a Pythonista on the same show for nearly an hour and no fights?
[134.40 --> 140.58]  No fights. See, that's how it really is out there in the world with Ruby and Python. There's no need for fights.
[140.94 --> 144.96]  I think we probably cut it, but we ended up singing Kumbaya at the end of the episode. It was pretty fun.
[145.06 --> 148.32]  We cracked up the gin and tonic and sang.
[148.52 --> 149.10]  Good times.
[149.56 --> 157.02]  You know, what they do at Sunlight Labs is their mission is to open up government, shine a light on a lot of the data within our government.
[157.02 --> 160.74]  And more and more, this is being exposed via APIs.
[161.06 --> 169.68]  And since we last spoke with these guys, since we recorded the episode, business.gov released an API, we should mention, for small business resources in our own government.
[169.82 --> 174.52]  And this is hot on the heels of data.gov.uk over across the pond.
[174.62 --> 184.30]  So hopefully we're seeing a trend of government transparency and data being exposed so that people in the private sector or even hobbyists can build mashups using this data.
[184.30 --> 195.66]  Yeah, I certainly agree. I think one of the pieces we talked about, too, was the open data initiative and how it relates to just people being able to use and consume and use this data coming from government.
[196.36 --> 199.64]  And also how that relates to human security, which is kind of wild.
[199.86 --> 201.56]  Yeah, it's our government. It should be our data, right?
[201.82 --> 203.34]  Yeah, I suppose so. Why not?
[203.60 --> 205.22]  So we had a great interview. Should we get to it?
[205.38 --> 205.82]  Yeah, why not?
[205.82 --> 219.36]  All right, we're joined today by Luigi Montanez and Jeremy Carbaugh from the Sunlight Foundation.
[219.88 --> 223.20]  Now, Luigi, why don't you introduce yourself and tell the folks who you are and what you do at Sunlight.
[223.98 --> 224.84]  Great. Thanks, Sven.
[225.60 --> 230.60]  My name is Luigi, and I am a software developer at the Sunlight Foundation.
[230.60 --> 237.42]  And I specifically focus on Ruby, but JavaScript and other things like that.
[237.50 --> 239.98]  And we also have Python developers on staff, too.
[240.66 --> 249.60]  At the Sunlight Foundation, we're a nonpartisan, nonprofit organization, and we're based in Washington, D.C.
[249.84 --> 257.34]  And we basically push for open government and government transparency through technology.
[257.34 --> 263.58]  So Jeremy and I are in the technical wing of the foundation.
[263.74 --> 264.92]  We call ourselves the Sunlight Labs.
[265.20 --> 274.08]  But we also have policy experts on staff who kind of advise and lobby Congress or advise the administration.
[274.08 --> 280.32]  We have journalists on staff who do investigative journalism, digging up dirt, digging up stories.
[280.32 --> 295.44]  And we also have some social media folks who kind of reach out to citizens through the Internet and get support for government transparency, our government transparency efforts and things like that.
[296.00 --> 299.18]  All right. How about you, Jeremy? What's your background? And how did you come to join Sunlight?
[299.56 --> 301.20]  Well, I actually came from the dark side.
[301.20 --> 305.54]  I was a government contractor for a number of years and had to repent for my sins.
[305.68 --> 309.34]  So I came to work for the Sunlight Foundation and opened up some government.
[310.12 --> 312.04]  I'm primarily a web developer here.
[312.28 --> 320.62]  I do mainly Python work, specifically Django, and do a lot of some of the more nerdier front-end stuff as well.
[320.76 --> 325.52]  So just JavaScript and help people with CSS issues.
[326.10 --> 328.26]  And, Luigi, you call yourself a Rubius, right?
[328.74 --> 329.48]  Yes, I am.
[329.48 --> 331.04]  And you guys still talk to each other?
[331.20 --> 338.98]  We share the same office, and it's fine. There's no problems.
[340.02 --> 341.32]  We can coexist.
[342.90 --> 350.86]  Well, if you go out to the Sunlight Labs GitHub page, and that's at github.com forward slash Sunlight Labs, quite a number of projects that you guys have.
[350.92 --> 353.88]  Any of these that you'd like to highlight for the listeners?
[354.38 --> 359.50]  Yeah, so I guess a few of the better ones we have, there's a project called Ant Hill.
[359.50 --> 365.62]  We made that to help us create the Sunlight Labs site.
[366.16 --> 373.22]  And what it does is it provides a bunch of views and models in Django for working with community.
[373.22 --> 383.10]  So there's profile pages to create events, to create projects and have people associate themselves with different projects.
[383.10 --> 389.70]  And that one's been pretty good because it's actually been picked up by some other organizations.
[390.70 --> 397.34]  Some within government as well are taking a look at it as ways to create community around their data or their projects.
[397.34 --> 404.60]  One of the other Django specific ones is a personal favorite of mine, Django MediaSync.
[405.30 --> 409.04]  And it's one that we use here on all of our Python projects.
[409.04 --> 418.40]  But what it does is it manages the media locations between development and production.
[419.08 --> 429.18]  So it helps you sync your media to production and intelligently switches all of your paths based on whether you are developing or actually running the application.
[429.18 --> 436.50]  Not really government transparency related, but at least helps us develop all of our stuff here much more quickly.
[437.44 --> 441.20]  How big is your team and what's the breakdown as far as Python and Ruby?
[441.46 --> 443.26]  Any other languages that you guys have as well?
[445.66 --> 447.42]  We are mainly Python and Ruby.
[448.08 --> 451.30]  I think we're about 13 people right now in the labs.
[451.52 --> 452.96]  I think we're actually 16.
[452.96 --> 454.26]  Oh, wow. Okay.
[454.90 --> 459.86]  I think we're somewhere around six or seven Python developers.
[460.58 --> 462.48]  What are we, four Ruby developers now?
[463.16 --> 463.42]  Three.
[463.78 --> 464.98]  Three. Okay. Sorry.
[465.84 --> 467.86]  And then we also have two designers.
[468.24 --> 469.74]  And then, of course, our boss.
[469.94 --> 472.70]  And I'm probably forgetting a few other people here, but that's the rough breakdown.
[472.70 --> 483.82]  And one thing, too, I've noticed is that both of us who work on the Ruby Rails side and those of us who work on the Python and Django side,
[484.28 --> 489.28]  we kind of share a common bond around, I guess, around the web, right?
[489.34 --> 493.48]  So around RESTful APIs and around, of course, JavaScript.
[493.48 --> 503.42]  So, you know, both, it's, you know, I think it's really great that we work in an environment where we have, you know, both Python and Ruby.
[504.48 --> 515.58]  And we really are able to kind of unite around things that we can interoperate, you know, like technology that interoperate well.
[515.58 --> 528.78]  So RESTful APIs and JSON, and we all love JSON here, and we all, you know, like JavaScript, and we're looking into, you know, working with more JavaScript even on the server side.
[528.88 --> 534.18]  And I know that the changelog has been focusing on that stuff a lot recently.
[534.42 --> 543.34]  You know, and that's how I found you, I guess, a couple of years ago, or maybe even 18 months ago or so, was through the Sunlight Labs API that you mentioned.
[543.34 --> 548.24]  And that is at services.sunlightlabs.com forward slash API.
[549.12 --> 553.68]  Talk a bit about what the API does and sort of the technology behind it.
[554.04 --> 554.14]  Sure.
[554.32 --> 563.70]  So it is a Django app, but it's a RESTful API, and it follows pretty good, you know, conventions.
[564.86 --> 567.54]  It speaks both XML and JSON.
[568.32 --> 571.66]  And what it does is it's really about members of Congress.
[571.66 --> 597.66]  So if you ever needed to do things like get, take an address, you know, an unformatted address string or latitude, longitude coordinates and find out, you know, exactly which members of Congress represent this particular spot, you can do that with our API.
[597.66 --> 601.60]  And you can also do things like pass in names.
[601.74 --> 610.18]  And it's pretty good with things like the difference between Jack Murtha and John Murtha.
[610.46 --> 616.62]  Obviously, they're the same person, but it does good nickname standardization.
[616.62 --> 622.24]  So it's, there are, there, I wrote the Ruby wrapper.
[622.68 --> 624.32]  There's a Python wrapper for it.
[624.50 --> 626.86]  And there are also, there's also a Java wrapper.
[627.38 --> 629.30]  And are there any more?
[629.56 --> 630.86]  I think that's about it.
[631.26 --> 631.86]  Said PHP?
[632.44 --> 632.94]  Oh, PHP.
[632.96 --> 633.48]  PHP wrapper.
[633.70 --> 634.78]  There's a PHP wrapper too.
[634.78 --> 637.44]  And it supports JSONP.
[637.76 --> 645.66]  So if you ever need to just use, you know, hit it via client-side JavaScript, it works.
[645.78 --> 646.98]  It works really well that way too.
[647.46 --> 650.64]  And for those that don't know, JSONP is JSON with padding.
[650.64 --> 659.38]  So it's essentially making the same API call that you would normally make to get that JSON formatted JavaScript object notation back.
[659.54 --> 662.54]  But you can pass a callback function and it will wrap it in that.
[662.60 --> 666.50]  So you can do neat cross-site domain calls.
[666.80 --> 668.68]  A lot of APIs are starting to support this.
[669.86 --> 674.24]  So we talked a little bit about the back-end pieces of Python and Ruby.
[674.30 --> 675.72]  And you mentioned a few designers.
[675.72 --> 679.14]  What kind of front-end technologies do you guys dabble in?
[679.72 --> 688.42]  Specifically, are you dealing with any sort of CSS meta frameworks like SAS, Compass, LessCSS, XCSS?
[689.04 --> 692.42]  I'm not sure if any of the Ruby projects have tried it.
[692.60 --> 695.20]  But we've actually tried to stay away from it.
[695.54 --> 698.26]  Our designers really like their CSS and HTML.
[698.68 --> 704.28]  So we've proposed it to them, but they've resisted a little bit.
[704.28 --> 706.76]  Do they leverage any sort of frameworks like Blueprint?
[708.88 --> 709.44]  No.
[709.82 --> 715.34]  I think Eric Meyer had a CSS reset-based stylesheet.
[716.16 --> 717.50]  We tend to use that.
[717.86 --> 719.70]  But otherwise...
[719.70 --> 720.76]  Homegrown CSS?
[721.20 --> 722.06]  Yeah, homegrown CSS.
[722.44 --> 724.52]  JavaScript side, we mainly use jQuery.
[725.76 --> 728.92]  Been using some underscore.js lately, which has been fantastic.
[728.92 --> 735.70]  I was hoping that you might have mentioned Node there, because I thought you were going to say that we mentioned Node quite a bit lately on the changelog.
[735.74 --> 739.46]  I think this is probably like the sixth podcast straight that we've mentioned Node.js.
[739.94 --> 741.40]  You guys dabble in that much at all?
[742.22 --> 743.20]  We've just played with it.
[743.28 --> 744.08]  I've played with it personally.
[744.22 --> 745.54]  I think also Jeremy has.
[747.04 --> 750.58]  It's, you know, the idea of writing end-to-end JavaScript is a great one.
[750.96 --> 754.92]  I think maybe we're all in the same boat where we're just starting to play with it.
[754.92 --> 768.10]  But I personally want to try and write an analytics service using Node, just because I think the evented model would...
[768.10 --> 769.72]  I'm sure that's what Google Analytics uses.
[770.16 --> 774.30]  So it would be really interesting to try that out with Node.
[774.80 --> 778.90]  You guys mentioned earlier that you play well together.
[779.00 --> 781.32]  Ruby, Python, there's no fights.
[781.32 --> 785.76]  And I guess in your world, you're also nonpartisan, so that kind of plays right into it.
[786.28 --> 793.94]  And that's something we hear back from our listener base, that they get really excited when it's not just about Ruby, because Ruby tends to get highlighted quite a bit.
[794.08 --> 804.56]  But it's kind of nice to hear you guys say that you don't fight and you play really well and you have a lot of the synergies between, I guess, your morals, your developer morals, right?
[805.16 --> 805.42]  Right.
[805.42 --> 810.64]  Yeah, I mean, I think both languages, both frameworks have great ideas.
[811.26 --> 826.48]  And I remember a few months ago, there was a post by one of the Django lead developers who kind of said, he was kind of saying, you know, the great things we've learned from and can learn from Rails.
[826.48 --> 840.98]  And at RubyConf this past November in San Francisco, Chris Wonstroth, who I know you guys had on earlier, he gave a talk called Rippin' Off Python to Irving Fool of Rubyists.
[841.40 --> 844.64]  So, yeah, both languages are great.
[844.64 --> 850.68]  And there's no need to have any silly spats or disputes.
[852.24 --> 857.10]  You know, one thing that I love about development is code is more than just code.
[857.78 --> 861.02]  In the case of GitHub, code is sharing, right?
[861.64 --> 863.34]  Many would say code is also art.
[863.46 --> 865.00]  But in your case, code is activism.
[865.96 --> 866.06]  Right.
[866.50 --> 872.30]  Why do you think that developers should apply their skills towards a cause that's close to their heart?
[872.30 --> 885.20]  Well, I think for developers who might not have dabbled into open source as much as they want.
[885.28 --> 893.66]  So maybe they haven't contributed as much or maybe they haven't found the courage yet to just put out their own code out there.
[893.66 --> 919.56]  I think working on open government and what we call civic applications or sometimes I call it civic hacking is a really great first step because not only does it benefit the developer for taking that first step and putting open source out there, it's going to benefit his community, like real people in his community, whether it be some local app.
[919.56 --> 927.04]  So one example of a civic app is a pothole reporter to your local city government, right?
[927.14 --> 937.26]  So if people come across potholes, maybe you can create a really simple interface that will maybe we're dealing with city government.
[937.38 --> 944.02]  So maybe it'll just email some city worker and tell him, hey, there's a pothole on this street or this corner.
[944.02 --> 952.52]  And that's a really simple app that any web developer can slap together really quickly.
[953.40 --> 966.06]  And when you do something like that and you make it open source, that means other people around the country or even around the world can share it or excuse me, can use it for their own purposes and maybe make it better.
[966.06 --> 973.92]  And it also means that you're helping people around you and people in your community with their day-to-day lives.
[974.40 --> 983.70]  So I speak from a Rubyist point of view, there's so many, let's say, Ruby testing frameworks, right?
[983.70 --> 992.78]  So do we really need another Ruby testing framework or do we need something that can really change lives around you?
[993.30 --> 996.50]  And that's why we like talking about civic hacking.
[997.30 --> 1008.40]  And we've also found that you could rely on government transparency organizations to get government data and interpret it for the public.
[1008.64 --> 1011.16]  But it's a very ineffective way of doing it.
[1011.16 --> 1030.44]  But if we can work to make the data available and then work to create a community around that data, there's infinitely more ways that that data can be used and an infinite larger number of applications that can be used to, like Luigi said, make people's lives better.
[1030.92 --> 1032.52]  So you guys are in D.C., right?
[1032.52 --> 1034.98]  So what is your focus?
[1035.18 --> 1038.12]  Is it on the federal, the state, or is it kind of more localized?
[1038.12 --> 1047.26]  So when we started out, we were focused primarily on the legislative branch of the federal government.
[1047.98 --> 1050.86]  We've actually expanded over the past year.
[1051.08 --> 1058.54]  So we've started focusing on the executive branch and also state government as well.
[1059.44 --> 1062.32]  We're not as active in state government yet.
[1062.32 --> 1066.50]  One of our projects that we're working on is the 50 states project.
[1067.24 --> 1076.24]  And what that is is an effort to create parsers to scrape the legislation that every state has.
[1077.20 --> 1085.12]  There's practically no consistency between any of the state governments as to how they publish their legislation, if they publish it at all.
[1085.12 --> 1096.78]  So this project is to scrape it, bring it all in, and present it in a common format so that if you wanted to find out the laws in each state, you would have a consistent mean of doing so.
[1096.78 --> 1101.86]  And Jeremy just brought out a really good point that reminded me.
[1101.96 --> 1107.68]  So another great benefit to a developer doing civic hacking is that I really mean hacking.
[1108.52 --> 1124.16]  So he was talking about the 50-state project where we have to essentially scrape websites of all 50 states and figure out how to get the actual text of their bills into machine-readable formats.
[1124.16 --> 1128.82]  And that's a really great skill for a web developer to have to do scraping.
[1129.60 --> 1136.62]  Another skill you'll probably gain is working with really big data sets and imperfect data sets.
[1137.52 --> 1140.02]  And that's how it is in the real world.
[1140.36 --> 1149.58]  And those are skills that you can market yourself as having after you've done some apps like these.
[1149.58 --> 1154.54]  You know, one of the growing trends has been the government 2.0 space, as it's called.
[1155.84 --> 1162.48]  You know, a lot of what you're doing is having to scrape Web 1.0 websites to get the data that you need for these particular types of applications.
[1162.66 --> 1171.12]  But how do you see the development of technology behind the government firewall changing the landscape for your type of apps going forward?
[1171.12 --> 1184.12]  Well, I think with the Obama administration, they've been very in tune with the needs and the kind of demands of the government 2.0 movements.
[1184.94 --> 1187.98]  And of course, they're not at all perfect.
[1188.16 --> 1190.08]  And we'd love to see much more out of them.
[1191.88 --> 1196.18]  But things like data.gov are a huge step.
[1196.18 --> 1208.52]  So data.gov is a data catalog of not all, but many data sets that the federal executive branch puts out.
[1208.52 --> 1218.06]  So all the departments like the Department of Commerce, the Census Bureau, the EPA, things like that.
[1219.02 --> 1221.10]  They've started publishing their data.
[1221.10 --> 1228.04]  And there was recently something called the Open Government Directive, which came from the White House.
[1228.24 --> 1233.72]  And it was essentially a memo to all heads of all the major agencies that said,
[1234.34 --> 1239.72]  you have to, on your website, have a slash open page.
[1239.72 --> 1245.76]  So, for example, the State Department is at state.gov.
[1245.86 --> 1250.68]  So the State Department is now mandated to have a web page at state.gov slash open.
[1251.10 --> 1253.64]  And I'm actually not sure if they put it up yet.
[1253.82 --> 1261.32]  But that page is to contain links to data sets that you are publishing.
[1261.88 --> 1269.72]  Data sets that should be useful for developers and for researchers to remix and to reuse.
[1269.72 --> 1282.74]  And also have on your slash open page information about how the public should work with your department and how they should communicate with you.
[1283.50 --> 1286.92]  And that's really what we mean when we say transparency, right?
[1286.92 --> 1297.96]  It's just making government more accessible and making it so that citizens can really see the value that they're getting out of government.
[1297.96 --> 1303.92]  When we talk about this openness and we talk about citizens, how do we know it's the right citizens getting a hold of this data?
[1304.10 --> 1306.98]  What kind of data is available and what can you really do with that data?
[1307.16 --> 1311.28]  Like what if somebody from a different country did it for the wrong reasons?
[1311.28 --> 1311.84]  Right.
[1312.02 --> 1324.14]  So when we say open data, we definitely mean – we don't mean anything sensitive intelligence-wise or defense-wise.
[1324.34 --> 1327.34]  And we definitely don't mean anything personally identifiable.
[1327.56 --> 1332.66]  Like we don't want the IRS releasing people's tax returns, things like that.
[1332.66 --> 1338.58]  What we mean is – are things like how – like let's say the federal budget, right?
[1338.62 --> 1341.60]  There's a lot – the federal budget was just released this past week.
[1341.84 --> 1344.50]  There's a lot of data in there.
[1344.70 --> 1346.56]  There's a lot of money being spent.
[1346.78 --> 1351.66]  We'd like to get a really clear picture about how that – where that money is going to, how it's being spent.
[1351.66 --> 1357.16]  Things like campaign contributions to members of Congress.
[1357.70 --> 1378.02]  We want to know who's contributing and how much they're contributing, which industries are giving to which congressional candidates because we can see that based on what money a particular member of Congress might receive for their campaign, they might be inclined to vote one way or the other when it comes to legislation.
[1378.02 --> 1383.70]  We actually had two contests here at the Sunlight Labs.
[1384.18 --> 1385.56]  We call it Apps for America.
[1386.44 --> 1391.46]  And I actually think Wynn was a participant in the first one.
[1392.26 --> 1397.96]  And Apps for America is essentially a – just a development contest, an app development contest.
[1398.48 --> 1399.96]  And we gave away cash prizes.
[1399.96 --> 1413.64]  And it was essentially, you know, use some government data sets that is either from government or is from a transparency group like the Sunlight Foundation that we also have some partner groups out there.
[1414.18 --> 1418.10]  And do something useful with that data.
[1418.10 --> 1436.10]  So if you go to, I believe, sunlightlabs.com slash apps for America, let me just double check that URL, you'll see the results of – you'll see the page and the results of our first contest.
[1436.38 --> 1439.20]  And another event that you guys have is the Great American Hackathon.
[1439.36 --> 1440.82]  Is that an annual event or –
[1440.82 --> 1441.90]  Ah, yes.
[1442.80 --> 1451.06]  So this past December, we had a kind of a distributed nationwide hackathon called the Great American Hackathon.
[1451.48 --> 1453.40]  And it was our first annual hackathon.
[1453.40 --> 1459.84]  So our plan, of course, is to make this a regular – hopefully an annual or even more frequent occurrence.
[1459.84 --> 1473.76]  And the idea was that we wanted to get people who are into open government, who are developers together in one place in the same city and just let them meet each other and start working on some projects.
[1474.44 --> 1476.86]  And we had some pretty good projects that came out of it.
[1476.86 --> 1492.74]  There was a – out in Silicon Valley, there was a NASA – NASA attended – it was an official NASA event, but it was a NASA attended hackathon.
[1493.34 --> 1497.36]  And they worked on things to make NASA better.
[1497.90 --> 1499.36]  And there were employees from NASA there.
[1499.36 --> 1507.02]  And then we had a lot of other hackathons across the country in Chicago, New York, Philly.
[1508.18 --> 1511.60]  And we had a great one in Phoenix.
[1512.34 --> 1516.58]  So, you know, there's definitely people out there.
[1516.78 --> 1525.34]  And I think at this point, I should actually plug our website, sunlightlabs.com, because it's a system where developers can register.
[1525.34 --> 1529.74]  And they can see existing projects or they can make their own projects.
[1529.92 --> 1533.38]  They can find other like-minded developers, people who are into this.
[1533.96 --> 1535.56]  And you can even post events.
[1535.82 --> 1540.56]  So it's a bit like a little social network we built on our website.
[1541.32 --> 1552.14]  And it's really – it's there really to just serve the community and help people find each other and help people get ideas on what to work on.
[1552.14 --> 1565.16]  I was going to ask you also – I guess this probably answers that question, but how are you guys driving awareness about these kinds of events and how to reach out to individuals who might be interested in it but aren't really in that circle quite yet?
[1565.24 --> 1568.02]  How do you reach out and engage developers to get involved?
[1568.74 --> 1571.48]  That's actually a difficult problem that we are trying to solve.
[1571.48 --> 1581.08]  So we do go to local meetups here in the D.C. area, various language-specific or even just general technology groups.
[1582.06 --> 1589.38]  We've sponsored some code sprints at various conferences.
[1591.18 --> 1594.66]  And we've actually tried to get different partners.
[1594.66 --> 1609.56]  So like for the Great American Hackathons, we partnered with Mozilla, Red Hat, and Google, and among a few others, and trying to get them to help or at least advertise some of these events to their community as well.
[1611.22 --> 1617.00]  So we're always looking for ways that we can let the development community know more about what we're working on.
[1617.00 --> 1626.86]  If I could also just mention that I see O'Reilly's name there as a listed sponsor, so I guess having Gov 2.0 conferences every year is a pretty good way to drive awareness as well, right?
[1627.34 --> 1628.66]  Yes, that absolutely helps, yeah.
[1629.32 --> 1640.54]  Yeah, I mean when you have people like the O'Reilly folks that are really spearheading the effort, that always helps to get the tech community to pay attention to it.
[1640.54 --> 1652.26]  You know, on the note of Tim O'Reilly, just going back maybe, I don't know, five years when the term was coined, you know, Web 2.0, I thought it was kind of wild that everybody sort of cloned to that term.
[1652.88 --> 1661.62]  And it was about, you know, Ajax and JavaScript and this asynchronous way of, you know, having your interface taught to the back end and all that good stuff.
[1661.62 --> 1668.62]  But, you know, one of the things that Tim really drove home with that term was just having this connected web, this web as a platform.
[1669.30 --> 1676.58]  And he's always been a proponent for the good side of technology and always helping, you know, people live better lives through technology.
[1677.44 --> 1681.42]  Yeah, he's been a huge supporter of us.
[1681.88 --> 1686.00]  And he came to Transparency Camp.
[1686.58 --> 1688.70]  We have a bar camp-like event.
[1689.18 --> 1690.38]  We had two last year.
[1690.38 --> 1692.34]  And he came to those.
[1693.36 --> 1703.70]  And he's, I think O'Reilly Publishing is publishing a book soon called Open Government, which is kind of an anthology about these topics.
[1704.58 --> 1716.40]  And if you read the O'Reilly Radar blog, they talk about Gov2.0 and transparency topics very often there.
[1716.40 --> 1736.04]  And one of the great analogies that Tim O'Reilly has kind of talked about a lot about this topic is that government, we can't think of government as a vending machine where we kind of just put money in it and expect something to come out.
[1736.04 --> 1743.42]  We just can't maybe shake it a little bit if it doesn't do what we want and expect something to fall out.
[1744.02 --> 1748.54]  We really need to be actively involved in government.
[1748.54 --> 1759.90]  And as technologists, as developers, that means, you know, lending our skills to making kind of, you know, the change that you'd want to see.
[1760.00 --> 1762.62]  And we, you know, we have the skills to do it.
[1762.62 --> 1768.40]  And it's now just a matter of harnessing that energy and, you know, moving forward.
[1769.06 --> 1773.10]  Yeah, actually, the book that you mentioned, we've got a chapter coming out in that book.
[1773.18 --> 1773.96]  I'm not sure if that's one.
[1774.44 --> 1781.34]  I think it's still out later this month about Tweet Congress, a site that we built primarily on top of the Sunlight API.
[1781.34 --> 1790.80]  So it's amazing that you have an idea for a site that, in our case, we just wanted to let folks find their Congress representatives on Twitter.
[1791.70 --> 1796.24]  And, you know, we didn't have to start from scratch because you guys already had excellent seed data.
[1796.34 --> 1806.82]  But the big missing piece you alluded to earlier was to be able to put in a formatted or unformatted address string and get a list of Congress people back was just amazing.
[1806.82 --> 1814.54]  So kudos to you guys for having apps out there like that because, you know, the mashups are just powerful that you can build.
[1814.90 --> 1820.34]  And if you see something's wrong with your government, you can step in and at least try to make it better in some way.
[1821.66 --> 1828.80]  Yeah, and I'd also like to point out that, you know, when we talk a lot about campaign contribution data or earmark data,
[1828.80 --> 1836.72]  it can give the impression that we're out there to do, you know, gotcha journalism or, you know, try to do muckraking.
[1836.82 --> 1843.90]  And, you know, while, of course, that is part of it, you know, it's also about having trust in your government.
[1844.62 --> 1852.76]  And we really feel that when you feel like you're involved, when you can see how your government is working,
[1853.04 --> 1855.80]  when you can see why it's making the decisions that it does,
[1855.80 --> 1864.34]  and, you know, it helps the public have a greater trust and feel more involved with the actions of the government.
[1864.88 --> 1870.10]  And what better way to see how your government is working than the actual data byproducts that it produces?
[1870.78 --> 1874.22]  I guess you really can't hide from, you know, the pure data that comes out of it.
[1874.30 --> 1876.80]  It's analytical. You can comb through it. You can parse it.
[1876.88 --> 1882.66]  You can track it. You can do a bunch of stuff with it that you just can't hide from the truth.
[1882.66 --> 1888.04]  Exactly, yeah. So, you know, if you're looking at why EPA makes the decisions that it does,
[1888.12 --> 1893.88]  when you're able to get access to the raw data that they base their decisions on, you know,
[1894.02 --> 1899.60]  you can see if they made bad decisions or if you see that they've made good decisions.
[1899.84 --> 1906.70]  It does help, you know, make the public trust, you know, the agencies and government more.
[1906.70 --> 1910.06]  You know, one of my favorite applications is Capital Words.
[1910.36 --> 1912.80]  Is this one of your apps or you guys sponsored this in some way?
[1913.38 --> 1918.60]  No, that is one of our apps. One of our developers here, Josh Rulli, he had the idea for it.
[1919.10 --> 1925.84]  We have another application called LewisDB that scrapes the Federal Register and a bunch of other government publications.
[1925.84 --> 1933.22]  And the Federal Register also contains, like, what was said on the House floor.
[1933.46 --> 1937.46]  So Josh had the great idea of wanting to know who said what.
[1937.76 --> 1943.22]  So Capital Words analyzes the Federal Register to see how many times people have used different words.
[1943.32 --> 1944.04]  So you can go on.
[1944.58 --> 1949.54]  You can look at different members of Congress and see what words they most frequently use on the House floor.
[1949.54 --> 1955.84]  You can look up specific words and see who uses them.
[1955.94 --> 1958.52]  You can compare the usage of different words across time.
[1959.48 --> 1960.52]  It's pretty amazing.
[1961.40 --> 1964.90]  Well, as Adam knows, I'm an API junkie and also a political junkie.
[1964.94 --> 1970.68]  So this is kind of a mashup of two things that I really enjoy doing.
[1971.34 --> 1975.52]  Capital words.org forward slash API, and that's capital as in the capital dome with an O.
[1976.10 --> 1976.28]  Right.
[1976.28 --> 1978.54]  You have a cool map there on the right-hand side.
[1978.62 --> 1982.44]  You can see the most vocal states from the congressional record.
[1982.82 --> 1986.04]  And glad that Texas is representing there with the dark red color.
[1988.46 --> 1989.96]  How often is this updated?
[1992.26 --> 1994.66]  I believe that it's updated nightly.
[1995.22 --> 1997.68]  The underlying data is updated every day.
[1998.32 --> 2002.80]  And if I recall correctly, I think the data is processed nightly.
[2002.80 --> 2006.58]  And you also get the list of most used words there.
[2006.70 --> 2012.52]  That's just – it's incredible to see our congressional record just map like this.
[2012.68 --> 2013.14]  It's amazing.
[2013.94 --> 2016.88]  Yeah, it's really interesting to see trends in government.
[2018.20 --> 2019.94]  I can't remember the exact word.
[2020.02 --> 2021.26]  There's some energy-related word.
[2021.32 --> 2021.86]  It might be oil.
[2021.94 --> 2022.72]  It might be something else.
[2023.10 --> 2024.32]  I think price of gas.
[2024.78 --> 2025.24]  Is that it?
[2025.34 --> 2025.92]  Price of gas?
[2026.28 --> 2027.04]  Something like that.
[2027.06 --> 2027.78]  I'd have to look it up.
[2027.78 --> 2033.40]  But it's – you can basically see that pretty much the same time every year these topics are going to come up.
[2033.98 --> 2041.10]  If you search for marriage, you see that there's a huge spike right before congressional elections.
[2041.50 --> 2044.96]  And then it basically falls to the wayside afterwards.
[2044.96 --> 2051.90]  So it can reveal some interesting insights into the politics of what Congress is talking about.
[2052.36 --> 2052.44]  Right.
[2052.52 --> 2067.28]  And also if you search for energy or gas prices, those are much more likely to be said in Congress during the summer months because that's when, of course, gas prices are on everyone's mind.
[2068.86 --> 2072.96]  And so the congressional record is essentially what you see on C-SPAN.
[2072.96 --> 2080.46]  So when you see a member of Congress on the floor of the House or the Senate and they're talking and sometimes it seems like they're talking to an empty room.
[2081.10 --> 2087.82]  But that all gets transcribed and we take all those transcriptions and that's what powers Capital Wars.
[2088.46 --> 2091.48]  So in addition to Capital Wars, you have Open Secrets and MapLight.
[2091.72 --> 2093.34]  Why don't you talk about two of those real quick?
[2094.12 --> 2095.76]  Well, those actually aren't our projects.
[2096.42 --> 2099.10]  We are a great giving organization as well.
[2099.28 --> 2101.48]  So those are two partners that we've worked with.
[2101.48 --> 2108.86]  We've given both of them grants and we also collaborate on various projects and data as well.
[2109.92 --> 2111.12]  But MapLight is great.
[2111.62 --> 2122.04]  They started out in California looking at the different support for bills amongst different corporations and different organizations.
[2122.04 --> 2138.78]  And basically mapping campaign contributions to representatives based on their final vote and the support for or against the bill by the companies that were giving them money.
[2139.30 --> 2142.26]  And they've expanded to some federal data as well.
[2142.26 --> 2144.84]  So that's a really amazing project.
[2146.62 --> 2154.28]  Another really popular site that's a partner of ours is called Open Congress, opencongress.org.
[2154.28 --> 2162.80]  And this site essentially is – I like to think of it as what the Congress's website should be.
[2162.80 --> 2175.70]  So at Open Congress, you can essentially – on their front page, they link you, the full text of the legislation that's being considered for passage in the House or the Senate.
[2175.94 --> 2178.00]  So right there, you can read it.
[2179.14 --> 2181.78]  You can – there's a lot in the news these days.
[2181.78 --> 2187.44]  There's a lot of talk and punditry about what is or is not in bills or what it means.
[2187.68 --> 2190.90]  But here on Open Congress, you can actually read the text for yourself.
[2191.70 --> 2192.64]  It's a really nice UI.
[2193.86 --> 2198.18]  And you can just see just the raw data, right?
[2198.20 --> 2199.82]  Because this is what it is.
[2200.02 --> 2201.58]  And it's unfiltered.
[2202.04 --> 2208.32]  And it lets the citizens access it at the base level.
[2208.32 --> 2211.58]  So this is something you guys do, opencongress.org?
[2211.86 --> 2213.10]  So this is a partner of ours.
[2214.22 --> 2220.00]  And so we give them grants and we help them.
[2220.08 --> 2222.92]  We advise them and things like that.
[2223.00 --> 2225.18]  And this is – I should mention a Rails app.
[2225.52 --> 2226.94]  So a little plug for myself.
[2228.22 --> 2235.04]  And the other really great thing about Open Congress is you're able to go on and not only just comment on the bill itself,
[2235.04 --> 2238.62]  but actually go down to very – like each paragraph of the bill.
[2239.20 --> 2248.48]  And you can have discussions about certain topics as to whether this paragraph is needed, how it could be changed to make the bill better.
[2249.54 --> 2257.92]  So it's – not only is it there to help you get information about bills, but it's a great way for people to actually interact.
[2257.92 --> 2263.88]  Now, if only Congress took that feedback and made changes from it, that would be fantastic.
[2264.18 --> 2265.84]  But that's something we can work on.
[2266.32 --> 2268.40]  It's a fantastic site, absolutely fantastic.
[2269.06 --> 2274.58]  When we launched tweetcongress.org late last year, or I guess the year before last now,
[2275.50 --> 2281.70]  one of the things that surprised us was overseas we had kind of sister sites that cropped up,
[2281.90 --> 2284.36]  people that wanted to do the same thing for their country.
[2284.36 --> 2293.16]  So they sought us out to compare ideas, and a lot of them have created sites that far surpass what tweetcongress does.
[2293.74 --> 2297.30]  To what extent do you guys talk to folks in other governments overseas?
[2297.94 --> 2306.92]  We actually have had some communication with other governments and specifically other groups in other countries that are working to open their governments as well.
[2306.92 --> 2310.62]  So it's really not our focus.
[2311.42 --> 2315.78]  So we don't do any work directly with that.
[2315.94 --> 2327.12]  But we're always looking to cooperate on different methods, tactics, applications, best practices for getting data out of government.
[2327.12 --> 2338.28]  I know that in the UK, for listeners in the UK, there's a really good group called My Society, which does a lot of the same kind of work that we do.
[2339.64 --> 2347.34]  And recently in the UK, they actually released their own site called data.gov.uk.
[2347.34 --> 2356.38]  And that's just really notable because one of the advisors or the main drivers behind that site is Tim Berners-Lee,
[2356.98 --> 2360.68]  who is essentially the inventor of the World Wide Web.
[2360.88 --> 2364.26]  He's the guy who, I think, developed HTTP spec.
[2365.08 --> 2367.28]  And he's now really into the semantic web.
[2367.56 --> 2373.64]  And he's worked a lot with the open government folks in the UK on these things.
[2373.64 --> 2378.94]  And there's also a Canadian group called Visible Government.
[2379.78 --> 2383.76]  I think there's also one in New Zealand called Open New Zealand.
[2384.46 --> 2388.36]  And so these things are popping up all across the world.
[2388.78 --> 2391.20]  At Sunlight, we mainly focus on the US.
[2391.80 --> 2396.76]  But there's starting to be groups like us all over the place now.
[2397.22 --> 2400.04]  Yeah, data.gov.uk is a fantastic resource.
[2400.04 --> 2408.28]  And I think the contrast is this is government-sponsored and government-led as opposed to you guys trying to kind of open up the government.
[2408.42 --> 2418.78]  To what extent does our government here in the States offer traditional what we would call APIs as opposed to just giving you the data in some raw format that you have to parse?
[2418.78 --> 2426.18]  Well, you know, it's not that often that they have APIs for data that we would like to have.
[2427.14 --> 2431.52]  And even if they provide things like bulk downloads, it's often in very arcane formats.
[2432.20 --> 2440.24]  If you try to get campaign finance contribution from the FEC, it's a COBOL fixed-width format.
[2440.24 --> 2446.08]  And each individual record could be in one of over 20 different formats.
[2447.10 --> 2450.06]  And it's really arcane, no documentation.
[2450.38 --> 2456.24]  So even when data is provided, it's not often, you know, very easy to use.
[2457.62 --> 2465.96]  But it's easy to assume that, you know, either government's doing this on purpose to keep things hidden or that they just don't have an interest in it.
[2465.96 --> 2481.58]  And I think one of the main things that we have found is that it's not so much an issue of that, but, you know, government just really doesn't know how to do it or know, you know, what the open government groups want from them.
[2482.40 --> 2489.94]  And a lot of agencies that we've come to talk to have actually been quite open to making some changes.
[2490.38 --> 2493.84]  And, yeah, so it's pretty encouraging.
[2493.84 --> 2496.84]  What do you think will change that landscape?
[2497.70 --> 2505.68]  What has to happen for new projects to be open from the get-go and publish as much data as they present?
[2507.34 --> 2509.78]  I think we just need to keep pushing them.
[2509.78 --> 2526.24]  And the biggest thing, especially what we do at Sunlight, is we give real examples of how data can be useful and how we can make that data relevant to the average citizen.
[2527.18 --> 2533.20]  So at Sunlight, our designers, they do something called redesign the government.
[2533.20 --> 2541.42]  So if you've ever tried to go to a government website, it probably wasn't the nicest user experience.
[2542.48 --> 2556.10]  And so one thing our designers do is they take existing websites and do some mock-ups on how, you know, what a really good user experience for that website would be.
[2556.10 --> 2571.48]  And then on our end, for the developers, the sites we work on, the apps we work on, like Capital Words or the Sunlight API, they all serve, and also all the Apps for America entries, which I talked about earlier,
[2571.48 --> 2577.30]  they all serve as kind of an example as, hey, you know, this stuff can be done.
[2577.36 --> 2588.04]  It can be done by developers who are really essentially, you know, volunteer developers working on something on their own time.
[2588.22 --> 2593.84]  Or, you know, they're in small organizations like Sunlight, where, you know, there's only 15 or 16 of us right now.
[2594.30 --> 2596.48]  They're not in huge government bureaucracies.
[2597.12 --> 2599.16]  They're not in huge consulting firms.
[2599.16 --> 2613.66]  This is something that, you know, the internet and open technologies and open standards are all things that make things a lot more easy to build and a lot quicker to build and a lot cheaper to build.
[2614.44 --> 2627.76]  So once you kind of, you know, make that argument, and it's really just a matter of kind of making the argument over and over again and, you know, just making it very apparent
[2627.76 --> 2637.66]  to those within government and to citizens that, you know, there's a better way with IT and government.
[2638.02 --> 2640.48]  And, you know, we're trying to show them that.
[2641.24 --> 2649.16]  And I think it's also important to realize that government technology is very different from, you know,
[2649.16 --> 2654.58]  the technology that we use on a day-to-day basis or even the communities that we are involved with.
[2657.46 --> 2664.74]  I don't want to generalize, but there are probably quite a few government developers that just have never heard of JSON or REST APIs.
[2664.74 --> 2675.14]  So there also is a process of, you know, helping government learn about new technologies, new ways of providing data,
[2675.64 --> 2679.62]  and, you know, new ways that citizens can interact with government.
[2681.32 --> 2682.98]  How does open source impact this?
[2682.98 --> 2689.72]  Because if you caught the headline recently over at Mashable, there was a headline that said, you know,
[2689.80 --> 2694.80]  why open source in the new software policy or why open source is the new software policy for San Francisco?
[2695.14 --> 2701.48]  And you see, you know, governments start to step up and say open source is more useful and we should really leverage it.
[2701.48 --> 2710.20]  And that obviously helps the communities grow and helps foster new, you know, new communication between different developers.
[2710.20 --> 2712.94]  And it just fosters lots of great stuff.
[2713.54 --> 2718.74]  How does that impact that piece there to help people learn there's different ways to do things
[2718.74 --> 2722.12]  and there's new ways that we should be looking at technologies?
[2723.56 --> 2734.62]  I think the obvious benefit is that open source can be, you know, reused by other governments and other agencies.
[2734.62 --> 2740.62]  So a problem with government bureaucracies a lot of times is that they're very compartmentalized.
[2741.68 --> 2747.36]  So, you know, one department has their way of doing things and another department has their way of doing things.
[2747.48 --> 2750.96]  And, you know, the two don't talk.
[2750.96 --> 2769.56]  And as we've seen with the open source model in, you know, our world, that's, you know, software that can be shared and reused and modified is incredibly beneficial to all of us.
[2769.56 --> 2784.36]  So the idea is that open source software, let's say a transit app for the city of San Francisco, if that's open source, maybe Washington, D.C.
[2784.36 --> 2790.72]  or maybe New York can take that app and modify it slightly for their needs and then release a very similar app.
[2790.90 --> 2794.12]  So it, you know, should benefit everyone.
[2794.12 --> 2801.32]  So it's almost a conversation through code because like Wynn said earlier, you know, open source, you guys use it as activism in your roles.
[2801.42 --> 2805.10]  And it's like, you know, day in and day out, you guys get to use open source as your day jobs.
[2805.32 --> 2806.88]  But it's communicating.
[2807.16 --> 2811.78]  It's, you know, software essentially becomes the means to communicate.
[2812.50 --> 2813.30]  Right. Exactly.
[2813.94 --> 2821.00]  One project that actually comes to my mind, this is also a group we work with.
[2821.40 --> 2822.80]  They're called Code for America.
[2822.80 --> 2822.86]  Code for America.
[2823.86 --> 2826.82]  And Code for America, I think it's codeformerica.org.
[2827.24 --> 2833.78]  They are essentially creating developer teams to drop into cities.
[2834.18 --> 2837.90]  I think they're going to start in 2011 and they're going to start recruiting developers this year.
[2838.66 --> 2849.20]  And essentially these teams of developers are going to live in a particular city for about, for most of the year and just work on open source apps in service of that city.
[2849.20 --> 2858.98]  And they are going to, you know, they're going to talk to each other and they're going to see where they can, where the different teams can collaborate.
[2858.98 --> 2863.04]  And it should be a really great project.
[2863.28 --> 2865.32]  And I look forward to seeing what comes out of it.
[2865.52 --> 2867.96]  That's called Code for America if anyone's interested.
[2867.96 --> 2875.48]  And another way that open source really helps out is also from our perspective looking into government.
[2876.48 --> 2884.24]  Kind of like how Luigi said that the redesigning the government series is a great way to show concrete examples of, you know, this is how it can be done.
[2884.24 --> 2893.58]  You know, I think open source apps that use government data can also be a great example of how things should be done.
[2894.92 --> 2905.52]  And if they are open source, then it actually opens up the possibility that the government could actually reuse these applications at some point in the future, which would be great.
[2905.52 --> 2917.70]  So if someone wants to go to their local meetup, their Ruby meetup, their Python meetup, and get their buddies together and get an idea and they want to work on something, what steps do they need to take?
[2917.78 --> 2921.32]  What kind of support can they get from Sunlight to kind of point them in the right direction?
[2921.80 --> 2924.60]  Well, we have the sunlightlabs.com site.
[2925.38 --> 2931.42]  Up there we have a list of projects that we sponsor and also different projects that the community is working on.
[2931.42 --> 2940.10]  You can also find events in your area and also find other people that have registered as part of the community within your area.
[2941.26 --> 2945.84]  So that's a great way to find people and various projects to work on.
[2946.56 --> 2952.90]  So we also have a Google group and you can see the link to that on our website.
[2953.56 --> 2956.58]  And we also have an IRC channel on Freenode.
[2957.30 --> 2958.86]  It's pound transparency.
[2958.86 --> 2962.82]  And anyone interested can go in that.
[2963.36 --> 2964.86]  And we're on Twitter.
[2965.20 --> 2966.26]  We're on Sunlight Labs.
[2966.72 --> 2974.84]  And if you're interested in any of this, just literally just talk to us and we're going to help you.
[2974.98 --> 2983.58]  I mean, part of our job, more than just developers, is to get other developers engaged and involved in what we do.
[2983.58 --> 2990.98]  And we're more than happy to talk to anyone with any projects, ideas, no matter how kooky you might think it is.
[2991.12 --> 2992.66]  It'll probably be a really good idea.
[2993.30 --> 3001.94]  Have you seen this expand in any way in any of these cities where developers from different backgrounds might be coming together just in having meetups around open government?
[3001.94 --> 3018.08]  I know that from the Great American Hackathon, which we had in December, we had a lot of energy around the Silicon Valley, NASA meetup, or excuse me, the hackathon.
[3018.08 --> 3027.04]  And there's also an organization in New York City called Top Labs, T-O-P-P Labs.
[3027.46 --> 3032.16]  And they do a lot of the kind of same work we do, but at the city level.
[3032.16 --> 3047.10]  And I wouldn't say that our communities are as, I guess, organized as Ruby or Python communities are yet, because those are kind of general language meetups and they attract a broad audience.
[3047.30 --> 3050.06]  But I think it's getting a lot better.
[3050.42 --> 3053.98]  And a lot of people are really being turned on to what we do.
[3054.88 --> 3060.28]  And hopefully throughout this year and the coming years, we're just going to keep growing and growing our community.
[3060.28 --> 3062.50]  You know, they say all politics is local.
[3062.78 --> 3075.84]  And hopefully this will be something that develops into that where we see communities that kind of crop up to tackle some of these problems, especially at the local level, so that we can use our skills and kind of fix some of the problems we're seeing.
[3077.24 --> 3077.64]  Exactly.
[3078.20 --> 3083.12]  So we're probably to the point of this show where we ask you what is on your open source radar.
[3083.28 --> 3085.60]  So we know that you guys create a lot of open source software.
[3085.86 --> 3087.52]  I know you consume a lot of open source software.
[3087.52 --> 3094.58]  What gets you excited and what do you see in the next six months to a year that you really want to tackle and start using?
[3095.44 --> 3105.00]  So for me, something I recently got into over the weekend, really, because have you guys talked about the iPad yet on the show?
[3105.30 --> 3107.40]  I think this show has been iPad free.
[3107.40 --> 3133.04]  So in response to the iPad last week, the next day, I kind of – I don't know if it was subconsciously or consciously, but I got a netbook because I wanted a small computer that I can work on at home and not have to drag my MacBook Pro back and forth on my daily commute.
[3133.04 --> 3142.40]  So I got a little netbook, and I started looking into installing Chromium OS on it.
[3143.06 --> 3151.68]  And so I'm just at the beginning stages of learning about Chromium and the kind of setup they have there.
[3151.68 --> 3170.96]  But I'm really psyched about it, and I think it's a great project, and it's definitely a lower level – it's an OS, of course, so it's a lower level thing than my day job, which is essentially web development.
[3170.96 --> 3177.92]  So it's something that I hope to really get into and learn about in the coming weeks.
[3178.82 --> 3182.08]  Where do you see the sweet spot being for that particular OS?
[3183.24 --> 3186.14]  I think it's really, of course, it's meant for netbooks.
[3186.26 --> 3187.74]  That's what they've pushed it as.
[3188.98 --> 3198.54]  One thing that I was really surprised at was to actually build Chromium, you need to have Ubuntu Karmic on it, the latest Ubuntu.
[3198.54 --> 3208.14]  And so actually I first installed Ubuntu Karmic, and there's actually what they call a netbook remix version of Ubuntu.
[3208.84 --> 3212.56]  And I installed it, and the interface is really interesting.
[3212.74 --> 3215.76]  It's actually – it's an interface that you actually want to touch.
[3216.06 --> 3224.46]  Like it's – they have very big buttons, and it's just the menus are laid out in a way that it seems like, hey, there should be really a touchscreen here.
[3224.46 --> 3240.98]  So it kind of makes me think that both Ubuntu Netbook Remix and maybe Chrome – excuse me, Chromium, they definitely want you to just call it Chromium because Chrome is actually the end product, and Chromium is the open source project name.
[3240.98 --> 3251.98]  So both Ubuntu and Chromium are, I think, are really heading towards the touch tablet market or maybe touchscreen netbooks.
[3252.78 --> 3258.70]  I'm not entirely sure how technology has advanced in regards to that yet.
[3258.70 --> 3277.02]  But I think that something as a developer to really keep your eye on is the kind of natural computing interfaces like touch and even maybe even something like voice.
[3277.02 --> 3288.70]  Because if you've used the voice recognition on the Google Nexus One, it's a pretty nice way to interact with your phone.
[3289.20 --> 3293.84]  You can kind of dictate your tweets, and it works really, really well.
[3293.84 --> 3307.48]  So those – things like that, you know, getting – maybe getting a little bit away from the web world and more into the physical computing world, that's something that's on my radar.
[3307.80 --> 3308.62]  How about you, Jeremy?
[3309.68 --> 3316.02]  Well, one thing that's made my life a whole lot easier over the past few months is it's a Python package called SauceBrush.
[3316.02 --> 3321.26]  And it was actually written by one of our coworkers here in the labs, James Turk.
[3321.80 --> 3333.26]  But it's a very lightweight ETL framework for Python where it lets you create these recipes of, like, input sources and output sources and different filters to apply to your data.
[3334.20 --> 3342.70]  And so if you have a very large data set that you want to process, that you want to transform or change it into a, you know, a different format, insert it into a database,
[3342.70 --> 3350.62]  it's a really, really fantastic framework for just making these simple recipes to manage your data.
[3351.68 --> 3358.62]  Other than that, I've been using Homebrew on the Mac for managing packages and everything, and that has been amazing.
[3359.80 --> 3365.32]  Python has some issues with its database drivers.
[3365.96 --> 3372.68]  They can be notoriously difficult to get installed, but with Homebrew, everything just works.
[3372.70 --> 3374.12]  And it's amazing.
[3374.88 --> 3377.10]  Yeah, we featured Homebrew in the last episode.
[3377.34 --> 3387.80]  It's one of those things that I think it's a pain point that a lot of folks in the Mac OS have, and hopefully it's making a dent in that pain, just making package management simpler.
[3388.08 --> 3396.90]  You know, it's one of the things that when I moved to the Mac from the PC platform because I was kind of straddling Windows and Linux there for a while,
[3396.90 --> 3407.78]  you know, I was just amazed that having a Unix-based OS and OS X, that there was no robust package management like what you found on Ubuntu or some of the other Linux distros.
[3408.42 --> 3417.24]  Yeah, and there is Fink and Mac ports, but they're quite heavy-handed in how they install the packages and how they change your system.
[3417.24 --> 3423.36]  So, I mean, Homebrew is great in how fairly hands-off it is and standalone.
[3424.10 --> 3429.24]  You know, with those, though, it's amazing that they're still not distributing binaries with those.
[3429.32 --> 3429.96]  Right, yeah.
[3430.20 --> 3431.42]  They're still compiling from source.
[3431.42 --> 3439.96]  So, you do, you know, a port install like Zapien or something like that and then leave it for an hour and come back and it's still chewing on the install.
[3440.32 --> 3440.52]  Right.
[3442.12 --> 3443.82]  Well, you guys are doing some exciting work.
[3444.22 --> 3449.54]  We're anxious to see what becomes of the hackathons this year and the Apps for America 3.
[3449.54 --> 3464.06]  I know that I'll be participating in some way in either of both of those, and I know folks listening are probably excited about how they can jump on board and participate in some of these open government initiatives.
[3464.90 --> 3466.46]  Yeah, don't tell me I don't want to get involved, too.
[3467.48 --> 3469.76]  They do need designers and lightweight copywriters.
[3470.14 --> 3471.14]  You know, we didn't get to talk.
[3471.22 --> 3477.44]  I mean, we've gone on pretty long here, but, I mean, that one opencongress.org, that was a beautiful UI.
[3477.44 --> 3486.32]  I just, you know, if we had more time to talk about it, I would have loved to picture guys' brains about, you know, the design process behind some of the applications.
[3486.54 --> 3492.20]  But maybe that's something that maybe you can answer via, like, text or something like that.
[3492.22 --> 3493.94]  We can attach it as a show note or something.
[3494.54 --> 3494.66]  Sure.
[3495.18 --> 3498.50]  And I'd also say just stay tuned to some of our contests.
[3498.86 --> 3505.70]  I can't really talk too much about them just yet, but we are going to try to also get designers involved in the community as well.
[3505.70 --> 3506.48]  That would be awesome.
[3506.48 --> 3513.42]  I mean, I don't have the back-end rail skills like a lot of you guys have, but I certainly have some good front-end skills that could be leveraged.
[3513.62 --> 3516.94]  But you guys also have something called Transparency Camp coming up.
[3517.04 --> 3518.74]  Do you guys want to mention that before we head off?
[3519.26 --> 3519.86]  Yeah, that would be great.
[3520.20 --> 3528.66]  So at Sunlight, we're hosting an unconference called Transparency Camp, much like bar camps that have been around.
[3528.66 --> 3533.04]  And it's at transparencycamp.org.
[3533.84 --> 3537.76]  And it's going to be in late March, March 27th to the 28th.
[3537.76 --> 3539.12]  And it's going to be here in D.C.
[3539.12 --> 3549.16]  And everyone listening who might be in the area or who might even want to make the trip are more than welcome to join us.
[3550.16 --> 3553.80]  It should be a really eye-opening experience.
[3553.80 --> 3560.18]  And I remember at last year's Transparency Camp here in D.C., people like Tim O'Reilly were here.
[3560.52 --> 3562.72]  And Craig Newmark from Craigslist were here.
[3562.88 --> 3565.76]  And people who work in the government come.
[3565.90 --> 3577.02]  And you can really get a sense of what it's going to take to bring government transparency to our governments.
[3577.02 --> 3579.88]  And it's a great and awesome conference.
[3580.16 --> 3581.54]  And I'd recommend it to everyone.
[3582.18 --> 3585.92]  In addition to Transparency Camp, I know that you'll be speaking at Los Angeles RubyConf.
[3585.98 --> 3586.34]  Is that right?
[3586.96 --> 3587.64]  Yes, I am.
[3587.98 --> 3594.10]  I think it's February 19th and 20th is LA RubyConf in Burbank.
[3594.92 --> 3599.46]  And I'll actually be talking about this topic, civic hacking, over there.
[3600.46 --> 3602.00]  And so that should be really fun.
[3602.00 --> 3609.10]  And I look forward to going to LA as here in D.C. it's been snowing and cold and miserable.
[3610.14 --> 3611.10]  What about you, Jeremy?
[3611.26 --> 3611.88]  Heading to PyCon?
[3612.24 --> 3613.36]  I will be there.
[3613.94 --> 3617.36]  Last year we did hold a Sunlight Labs sprint.
[3617.70 --> 3619.40]  But I don't believe we're doing that this year.
[3619.60 --> 3623.76]  So there'll be a contingent of Sunlight Labs developers there.
[3623.86 --> 3624.80]  But just attending.
[3625.62 --> 3631.46]  Luigi, Jeremy, it was really awesome for you guys to take the hour and 18 minutes out of your lives to sit down and chat with me and win.
[3631.46 --> 3633.34]  And I know that our audience certainly appreciates it.
[3633.58 --> 3644.02]  And we open source lovers certainly appreciate what you're doing for our government and keeping it open and making it more open and everything you're doing, especially that it fuels your passion.
[3644.28 --> 3645.22]  The open source is your passion.
[3645.44 --> 3649.28]  It's so awesome that you guys get to do that every day.
[3649.40 --> 3651.02]  I mean that's such an awesome job.
[3651.32 --> 3652.96]  But thank you so much for coming on the show.
[3653.10 --> 3653.84]  It's been a pleasure.
[3654.20 --> 3654.32]  Yeah.
[3654.60 --> 3654.84]  Thanks.
[3654.84 --> 3663.88]  Thank you for listening to this edition of The Change Log.
[3664.94 --> 3671.66]  Point your browser to tale.thechangelog.com to find out what's going on right now in open source.
[3672.86 --> 3681.40]  Also be sure to head to github.com forward slash explore to catch up on trending and feature repos as well as the latest episodes of The Change Log.
[3681.40 --> 3711.38]  The Change Log.
[3711.40 --> 3711.88]  The Change Log.
[3711.96 --> 3716.04]  The Change Log.
[3716.70 --> 3717.26]  The Change Log.
[3717.48 --> 3718.78]  The Change Log.
[3718.78 --> 3719.24]  The Change Log.
[3719.24 --> 3719.76]  Ok.
[3719.88 --> 3720.16]  Thanks.
