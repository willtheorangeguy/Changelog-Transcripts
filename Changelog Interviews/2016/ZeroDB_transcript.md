[0.00 --> 1.16]  I'm McLean Wilkerson.
[1.52 --> 2.68]  I'm Michael Igorov.
[2.96 --> 4.32]  And you're listening to The Changelog.
[13.16 --> 14.14]  Welcome back, everyone.
[14.28 --> 16.98]  This is The Changelog, and I'm your host, Adam Stachowiak.
[17.10 --> 18.74]  This is episode 190.
[19.34 --> 23.54]  And on today's show, Jared and I are joined by McLean Wilkerson and Michael Igorov,
[23.54 --> 28.86]  the guys behind ZeroDB, an end-to-end encrypted database, and also a protocol.
[29.42 --> 32.74]  We talked about why it's open source, how it's different from other encryption techniques,
[33.16 --> 35.76]  if there's a performance hit for running encrypted queries.
[36.22 --> 39.92]  We also talked about the business side of this thing, and also an interesting topic,
[40.08 --> 43.40]  all in itself, proxy re-encryption, and so much more.
[43.84 --> 47.98]  Three sponsors we have on the show today were CodeShip, TopTile, and DigitalOcean.
[48.34 --> 50.58]  Our first sponsor is CodeShip.
[50.58 --> 53.18]  If it works with Docker, it works with CodeShip.
[53.54 --> 56.12]  For those out there with established Docker workflows,
[56.12 --> 61.76]  or those looking to leverage native Docker support while automating your testing and deployment,
[62.30 --> 67.32]  check out CodeShip's new Docker platform at CodeShip.com slash changelog.
[67.46 --> 72.36]  And for those looking for great resources to automate your development workflows with Docker,
[72.80 --> 78.82]  you should download CodeShip's free e-book covering why consistent environments are so important,
[78.82 --> 84.36]  how a company lost $400 million in 45 minutes due to inconsistent environments,
[84.74 --> 88.92]  and also how to build an app to run inside an isolated Docker container.
[89.46 --> 94.04]  Head to CodeShip.com slash changelog to check out CodeShip's new Docker platform,
[94.52 --> 98.24]  and head to resources.CodeShip.com slash e-books
[98.24 --> 102.86]  to download that free e-book I mentioned on automating your development workflows with Docker.
[102.86 --> 104.68]  And now, on to the show.
[112.38 --> 118.22]  All right, we're back today talking about ZeroDB with McLean Wilkinson and Michael Egarov.
[119.02 --> 122.76]  Talking about an end-to-end encrypted database, also a protocol.
[122.90 --> 124.36]  We'll dive deep into that.
[124.58 --> 125.78]  We've got Jared here as well.
[126.18 --> 127.48]  McLean, Michael, welcome to the show.
[128.42 --> 130.46]  Thanks, guys. It's just exciting to be on here.
[130.46 --> 135.02]  I guess maybe the best way, since we have two guests on the show today, Jared,
[135.10 --> 137.68]  let's maybe kick off real quick with some quick introductions.
[137.94 --> 142.10]  So, just to kind of pinpoint voices, I know when listeners listen to any podcast
[142.10 --> 147.20]  and there's more than a couple of voices, it's hard to kind of put a name or who's speaking to it.
[147.32 --> 149.18]  So, McLean, we'll go with you first.
[149.32 --> 152.60]  So, give an intro to who you are and what you do with ZeroDB.
[153.32 --> 157.96]  Sure. So, again, McLean Wilkinson, one of the co-founders of ZeroDB.
[157.96 --> 163.26]  I'm a software engineer. I also do business stuff now that we're an official company at ZeroDB.
[164.34 --> 169.70]  I have a background both in software engineering as well as more traditional finance.
[169.98 --> 175.28]  I worked in investment banking for a few years and I had a positive conversion from that.
[175.60 --> 180.52]  But during that time, I was covering tech, media, and telecom companies before getting into startups.
[180.88 --> 182.92]  Awesome. And, Mike, what about you?
[182.92 --> 189.20]  Yeah. So, I'm a software engineer and basically I'm the guy behind the tech here,
[189.26 --> 192.72]  even though McLean is also working on the tech in our company.
[193.04 --> 196.38]  And I also have a physics background.
[197.68 --> 200.14]  And how this got on our radar.
[200.26 --> 203.72]  So, I think, Jared, we chime in here on this because I thought this was kind of interesting.
[203.72 --> 208.94]  Before I recall, Jared and I had some sort of sync up, right, to think about, like, you know,
[208.94 --> 209.90]  what is this show going to be about?
[210.24 --> 210.90]  Who's on the show?
[211.00 --> 211.62]  What's their background?
[211.72 --> 212.20]  That kind of thing.
[212.24 --> 214.52]  And Jared said to me, Adam, how did this hit your radar, Jared?
[214.56 --> 215.16]  What did I say?
[215.68 --> 216.88]  I kind of stuttered a little bit.
[216.90 --> 217.74]  I had no idea.
[218.24 --> 219.12]  Yeah, you didn't know.
[219.60 --> 220.64]  You were like, well.
[220.86 --> 221.94]  We had to backtrack a bit.
[222.16 --> 222.96]  It was December.
[223.08 --> 223.74]  I know that.
[223.88 --> 224.10]  Yeah.
[224.20 --> 225.20]  I'm going to guess Hacker News.
[225.84 --> 226.14]  No.
[226.44 --> 226.60]  No.
[226.60 --> 227.76]  You would think Hacker News.
[227.96 --> 229.06]  Now, this is how cool we are.
[229.06 --> 232.72]  This is just a slight pat on the back to us because we've been trying, right?
[233.20 --> 235.26]  So, we have this email called Change All Nightly.
[235.88 --> 238.50]  And that email goes out every single night.
[238.60 --> 243.96]  It's essentially top new repositories, top star repositories every single day from GitHub.
[244.30 --> 249.36]  And that hit Change All Nightly, your repo when it open sourced, on December 7th.
[249.36 --> 251.16]  And so, that hit the top news repos.
[251.90 --> 256.08]  And then the very next day, December 8th, jumped to top star repositories.
[256.08 --> 259.16]  And then days after that, kept trending for several days.
[259.26 --> 260.96]  And that's how we discovered you.
[261.68 --> 262.12]  Gotcha.
[262.44 --> 266.00]  And almost immediately, I was like, this is going to be pretty interesting because it's
[266.00 --> 268.76]  obviously, you know, encryption, database related.
[269.34 --> 274.72]  Sent you a tweet the very next day on December 7th and said, congrats on the launch.
[274.78 --> 276.10]  Let's get you on the show sometime soon.
[276.26 --> 277.62]  So, it took about a month.
[277.78 --> 278.84]  You know, we're after the new year.
[278.96 --> 280.82]  We're here in the new year finally.
[281.08 --> 282.42]  And so, now we have you on the show.
[282.46 --> 283.94]  And that's kind of how this hit our radar.
[284.70 --> 285.02]  Gotcha.
[285.02 --> 285.26]  Yeah.
[285.26 --> 290.42]  When we open sourced it in, I guess, beginning of December, we had a little bit of a positive
[290.42 --> 294.08]  feedback loop or viral effect there for a little while.
[294.16 --> 297.32]  Because I guess it caught some people's attention, got a bunch of stars.
[297.48 --> 300.18]  And then it hit the GitHub trending page.
[300.38 --> 303.70]  And once you get there, it sort of, it feeds on itself for a while.
[303.78 --> 306.60]  So, we had a nice little ride there for a few weeks.
[307.08 --> 307.22]  Yeah.
[307.32 --> 308.96]  Jared, do you want to mention anything about Change All Nightly?
[309.50 --> 310.26]  I love it.
[310.38 --> 310.82]  You love it?
[310.82 --> 314.06]  I mean, the fact that it's our own radar?
[315.30 --> 315.66]  Yeah.
[315.80 --> 319.76]  I mean, there's no secret to how we find awesome stuff.
[319.76 --> 325.16]  Stuff that we put in Changelog Weekly or ends up on the show is, you know, 10 p.m.
[325.18 --> 325.80]  U.S. Central.
[327.22 --> 328.88]  What's interesting on GitHub for the day?
[328.88 --> 333.42]  And like you said, certain things pop into that new repositories list.
[334.04 --> 336.80]  And they pop in and they pop out and you never see them again.
[337.26 --> 339.16]  And then other things will pop into that list.
[339.22 --> 343.52]  And then you'll find them in the bigger global list of top start altogether.
[343.52 --> 351.14]  And, yeah, you can just start to see what is trending, what's interesting, and what's worth clicking through and checking out.
[351.72 --> 354.06]  Well, that's a good example of dog feeding, I guess.
[354.64 --> 358.96]  Well, I wanted to mention that at the top of the show, mostly because of the discussion that Jared and I had earlier.
[359.06 --> 361.70]  Like, normally we don't come on the show and make it about us.
[361.70 --> 372.58]  But I thought just for a second we can talk about that simply because it was literally from our own dog food that, you know, for using that metaphor that we found out about ZeroDB.
[372.84 --> 375.58]  And immediately I was like, we should get in touch with these guys, have them on the show.
[376.52 --> 380.32]  But let's dive deeper into some better interesting things.
[380.58 --> 383.32]  By the way, if you want to subscribe, it's a good transition.
[383.82 --> 385.36]  Changelog.com slash nightly.
[385.46 --> 386.84]  Go ahead and subscribe to that every single night.
[386.84 --> 392.18]  But let's dive in, I guess, to the topic of how you guys got started.
[392.30 --> 397.16]  Obviously, we're going to dive deep into ZeroDB databases, encryption later in the show.
[397.24 --> 398.98]  But let's find out where you came from.
[399.38 --> 401.72]  How did, I guess, you two meet?
[401.84 --> 408.56]  What was your background seemed to cross a bit in terms of, you know, tech and financial and things you've mentioned.
[408.68 --> 409.68]  But how did you guys meet?
[410.94 --> 412.78]  Yes, we're going to go back a little ways.
[412.78 --> 420.30]  And actually, even before ZeroDB, we were doing a lot of blockchain, cryptocurrency stuff, sort of the intersection of our respective backgrounds.
[420.44 --> 425.78]  We actually first met at the SF, San Francisco Bitcoin Users Group.
[427.46 --> 434.92]  And so we met there, sort of hacked on a bunch of different Bitcoin, cryptocurrency, blockchain related stuff for a while.
[434.92 --> 441.18]  And that was sort of the initial meeting and overlap of interest.
[441.42 --> 448.02]  And out of that process, sort of, we had the inspiration for ZeroDB after many different experiments.
[448.62 --> 450.68]  You guys still attend that meetup, that Bitcoin meetup?
[451.38 --> 452.24]  We do, yeah.
[452.32 --> 457.06]  Actually, we are not in Silicon Valley at the moment for the next several months.
[457.34 --> 458.12]  We're in London.
[458.58 --> 459.92]  There's a store there.
[460.52 --> 463.24]  But yeah, we attended it a lot there.
[463.24 --> 465.92]  For some reason, McLean, you got real soft there.
[465.98 --> 466.92]  Did you back up for the mic?
[468.58 --> 469.16]  I'm soft?
[469.56 --> 469.78]  Yeah.
[469.96 --> 471.02]  Did you step away?
[471.10 --> 472.20]  Did you move away or something like that?
[473.28 --> 474.54]  No, I'm actually pretty close.
[474.78 --> 475.70]  Is it still bad?
[476.92 --> 478.14]  No, you sound okay now.
[478.28 --> 480.24]  I don't know if anybody else, if you found it, like...
[480.24 --> 480.92]  I noticed it.
[481.36 --> 482.00]  I haven't noticed yet.
[482.34 --> 482.60]  Yeah.
[482.74 --> 483.82]  You kind of got softer for a second.
[483.88 --> 484.50]  But you're back.
[484.56 --> 485.02]  I can hear you.
[485.02 --> 485.68]  You're just softer.
[486.26 --> 487.30]  Like your volume went down.
[487.80 --> 489.12]  Like you backed up from the mic.
[490.08 --> 490.40]  Yeah.
[490.54 --> 492.92]  I'm not sure what happened there then because I've been pretty close.
[493.24 --> 493.50]  All right.
[494.12 --> 495.20]  Sorry about the glitch there, everybody.
[495.28 --> 496.46]  We'll see if we can edit some of that out.
[496.54 --> 498.18]  But we might just leave it because that's...
[498.18 --> 499.04]  Hey, that's radio.
[499.74 --> 500.08]  All right.
[500.16 --> 501.26]  So, Mike, what about you?
[501.32 --> 504.46]  I mean, what's your story in terms of that meetup?
[504.52 --> 506.38]  Like how did you get attracted to that Bitcoin meetup?
[507.10 --> 507.28]  Yeah.
[507.32 --> 511.72]  So, I've been attracted by Bitcoin even before I came to the US.
[511.72 --> 520.48]  And at the time while I was in Australia and I wanted to go to Silicon Valley to do some startup.
[520.70 --> 521.68]  I don't know which one.
[521.84 --> 528.28]  So, I went there just to work for a tech company for LinkedIn for a while.
[528.28 --> 534.32]  And I started attending these meetups, especially Bitcoin meetups.
[534.84 --> 536.84]  And that's why I've met McLean.
[538.50 --> 539.44]  And yeah.
[539.52 --> 545.38]  So, I've been fascinated by Bitcoin, decentralized applications, things like that.
[545.38 --> 549.58]  And that's what sparkled this 0DB idea.
[550.50 --> 551.38]  At what point did...
[551.94 --> 553.26]  You know, was it that first meetup?
[553.34 --> 554.38]  Or that's when you first met.
[554.46 --> 557.64]  But at what point did this discussion happen?
[557.98 --> 559.48]  What was the problem you guys were solving?
[559.60 --> 560.38]  Was it just like...
[561.02 --> 562.28]  You know, what was the situation there?
[562.62 --> 562.78]  Yeah.
[562.80 --> 567.76]  We didn't really start working on 0DB at all really until, I guess, after a year of working on other stuff.
[567.76 --> 571.44]  Sort of in that blockchain, you know, area.
[571.82 --> 578.52]  We were looking a lot at sort of these newer frameworks like Ethereum or storage with a J.
[579.02 --> 584.40]  And actually, how 0DB came about, we were thinking, okay, if you have a decentralized application,
[584.98 --> 587.86]  presumably like every other application, it's going to need data.
[588.24 --> 591.00]  And some of that data is going to be sensitive or need to be private.
[591.44 --> 595.20]  But if you don't know where that data is sitting, you're not trusting the server necessarily.
[595.20 --> 601.52]  Like, how can you have that data be secure and usable in this decentralized world?
[602.22 --> 606.76]  And that was sort of the original problem that 0DB was solving.
[608.40 --> 610.38]  Although, you know, we've ended up building it for us.
[610.46 --> 612.84]  It was certainly a more traditional client-server architecture.
[614.02 --> 616.90]  But that's the original origin story.
[617.84 --> 620.20]  So from there, like, how did you...
[621.16 --> 622.40]  What was the conversation like?
[622.40 --> 623.92]  It was like, hey, we should create this technology.
[623.92 --> 626.32]  Or, hey, there's these problems and we should open source it.
[626.60 --> 627.72]  We should create a business together.
[627.86 --> 628.72]  Like, how did that happen?
[630.36 --> 634.70]  Well, I think we had, you know, throughout all these different experiments,
[634.70 --> 638.46]  we had been planning on eventually, you know, having something that would become a business.
[638.60 --> 641.10]  I think that was in the back of our minds the entire time.
[641.44 --> 644.72]  While also, you know, having, you know, the flexibility to be able to work on cool stuff.
[644.72 --> 648.10]  And we...
[648.10 --> 652.44]  So originally, when we first had the idea, we didn't really think that it would be...
[652.44 --> 653.04]  That it would work.
[653.74 --> 655.18]  We just thought it would be too slow.
[656.18 --> 660.30]  And eventually, we got around to sort of hacking together a really quick and dirty prototype
[660.30 --> 664.08]  and realized, hey, actually, you know, you can tweak some things and play around with it
[664.08 --> 668.48]  and actually make it performant enough that you can use it for, you know, real-world stuff
[668.48 --> 669.46]  and production applications.
[669.46 --> 674.30]  And at that point, this was back in March of last year, so 2015.
[675.62 --> 679.86]  At that point, we just thought it was kind of an interesting little technical trick.
[680.54 --> 684.86]  But we posted about it on Hacker News and it blew up there and hit the front page twice
[684.86 --> 690.46]  in one week, which for me is a, I would say, very frequent reader of Hacker News was a cool
[690.46 --> 690.82]  thing.
[691.26 --> 695.26]  And that was when we sort of realized, okay, hey, you know, this could be, you know, something
[695.26 --> 696.72]  that could go into an actual business.
[696.72 --> 702.58]  Well, I was just going to ask, you know, where it goes from there.
[702.98 --> 708.00]  I mean, we have more and more of these open source projects that, you know, have a GitHub
[708.00 --> 710.06]  page and they also have an AngelList page.
[710.54 --> 713.32]  And so it's a bit of a newer phenomenon.
[713.62 --> 717.26]  And we're talking to more, you know, co-founders slash open sourcers.
[717.26 --> 726.38]  And so, yeah, I would just wonder is like, okay, so you have this cool technology.
[726.72 --> 730.74]  You obviously both want to do startups or be in a startup or start a startup.
[732.02 --> 737.78]  And you've had something that's interesting on Hacker News, you know, which shows it has
[737.78 --> 739.02]  at least some technical merit.
[739.02 --> 745.02]  But where do you go from there, from there in March to here we are in January of the
[745.02 --> 745.60]  following year?
[746.48 --> 748.62]  And now it's, you know, business.
[749.18 --> 751.58]  So what's the process, the steps?
[751.58 --> 751.76]  Yeah.
[751.76 --> 752.58]  What's that look like?
[753.58 --> 753.98]  Yeah.
[753.98 --> 759.02]  So what happened was we had obviously the little really quick and dirty prototype.
[759.02 --> 763.76]  And once we realized, hey, there's a lot more interest in this beyond just the two of us
[763.76 --> 767.40]  from this Hacker News post, we sort of built it out a little bit more.
[767.88 --> 772.58]  Started, you know, giving access to, you know, some of our friends that were interested in,
[772.58 --> 775.32]  you know, potentially building stuff on top of it.
[777.00 --> 779.50]  And kept sort of on product development for a few months.
[779.50 --> 784.26]  And then I guess the summertime we started reaching out to some banks because we realized,
[784.38 --> 788.38]  you know, beyond decentralized applications, which are really cool in general.
[788.38 --> 791.34]  But I think in reality, it's not clear.
[791.88 --> 793.36]  There's not a whole lot of these in production.
[794.22 --> 799.28]  There's maybe a more immediate opportunity to sell this to industries like financial services
[799.28 --> 803.58]  or healthcare governments that are very security sensitive, have to deal with a lot of regulatory
[803.58 --> 809.58]  and compliance constraints and see, you know, if there's a use case for an end-to-end
[809.58 --> 812.08]  database in that area.
[812.26 --> 817.06]  And obviously, you know, that's where you could potentially build an actual big business as
[817.06 --> 820.94]  opposed to, you know, in this decentralized world, which is, I think, very interesting,
[821.06 --> 824.42]  but still maybe a few years away from actually really taking off.
[826.32 --> 830.70]  So started having those conversations, realized, you know, this could be a tool that could help
[830.70 --> 835.34]  banks move a lot of their on-premise infrastructure to the cloud.
[836.02 --> 840.82]  And so in general, banks have been very late adopters of, you know, cloud infrastructure
[840.82 --> 845.74]  and not a whole lot of clouds that are running infrastructure in AWS or Azure.
[846.38 --> 850.50]  A big reason for that is because they don't want to give up control over their data to a
[850.50 --> 855.96]  cloud provider, which even if they're encrypting their data at rest, if they're actually querying
[855.96 --> 858.62]  it, they're going to have to send the key to the database server at some point.
[859.78 --> 863.50]  But with 0DB, you can have the keys on-premise, still have the data be queryable.
[863.50 --> 867.28]  And so potentially offload a lot of that on-premise infrastructure to the cloud.
[867.54 --> 872.96]  And obviously there's a lot of economic benefits to that, as well as scalability and performance.
[874.52 --> 877.56]  So went through a lot of those conversations.
[877.80 --> 882.78]  Actually, the reason we're here in London today is it actually got announced on Monday of this
[882.78 --> 882.94]  week.
[882.98 --> 884.38]  So I can say it publicly.
[884.56 --> 890.70]  We're in FinTech Innovation Lab out here, which is a really good chance for us to talk with
[890.70 --> 895.88]  the 15 or actually 20 banks that are involved with this program here and potentially help
[895.88 --> 899.38]  them with that long-term cloud strategy.
[900.52 --> 904.46]  Tell us about FinTech Innovation Lab exactly what that is and what it entails for you guys.
[905.24 --> 905.58]  Sure.
[905.74 --> 912.04]  So FinTech Innovation Lab is sort of an accelerator, but not really the way most people think of
[912.04 --> 916.50]  accelerators out in the States, like in a Ycom rate or a tech star so much.
[916.62 --> 917.04]  It's more.
[917.58 --> 919.76]  So it's a consortium of 20 banks.
[919.76 --> 924.48]  There's one actually in London as well as one in New York, where the London one, of
[924.48 --> 924.72]  course.
[924.98 --> 932.08]  And it's really sort of a mentoring slash sourcing mechanism for them to find new interesting
[932.08 --> 939.22]  technology that they can potentially use internally or help go to market.
[939.22 --> 944.70]  So we're working and have the opportunity to work closely with a lot of senior IT executives
[944.70 --> 951.46]  and application developers inside of a lot of the leading global banks and figure out
[951.46 --> 957.58]  where 0DB would potentially fit within their organization, what the other use cases are beyond
[957.58 --> 958.88]  the ones that we've already identified.
[958.88 --> 964.04]  And there's 15 other companies in this program with us.
[964.16 --> 968.40]  It's divided into three different tracks, five companies in each track.
[968.80 --> 971.88]  We're in the tech track, which may be obvious.
[972.08 --> 976.80]  There's a retail banking track and then a commercial and investment banking track as well.
[976.80 --> 979.46]  So you said you're in London.
[979.84 --> 981.02]  Where are you normally at?
[981.32 --> 983.00]  I assume London's foreign to you, right?
[984.00 --> 984.32]  Yep.
[984.48 --> 987.52]  This is the first time I've really spent any time in London.
[988.70 --> 991.70]  We're usually out in the Valley, so we're in Mountain View typically.
[992.00 --> 992.20]  Gotcha.
[992.20 --> 995.68]  I was going to say, you made it this Bitcoin meetup.
[995.94 --> 1000.74]  You're interested in blockchain and decentralized things and obviously security as well.
[1000.94 --> 1007.48]  And then decide to get together and build some technology, start a startup and ends up not
[1007.48 --> 1010.92]  being specifically using the technologies that Bitcoin relies on.
[1012.50 --> 1014.88]  But nonetheless, here you are.
[1015.04 --> 1019.80]  And I guess I'm just curious, going back to the Bitcoin is if you guys, maybe Michael,
[1019.80 --> 1024.70]  you can address this one first is are you guys as bullish on Bitcoin as you were back
[1024.70 --> 1027.18]  when you first started meeting up in San Francisco?
[1029.08 --> 1037.06]  Well, probably not as much bullish as we were initially, but we still strongly believe
[1037.06 --> 1041.22]  in Bitcoin and in decentralized applications and things like that.
[1042.04 --> 1049.68]  So that said, I would say now it's this Bitcoins and Bitcoin infrastructure growth.
[1049.80 --> 1056.76]  It's at much more sustainable rate rather than this explosive craziness.
[1058.92 --> 1067.22]  And have you guys seen any interest from the fintech and the banks about these types of technologies
[1067.22 --> 1071.98]  like the Bitcoin, the blockchain based technologies for infrastructure or anything like that?
[1071.98 --> 1074.84]  Yeah, certainly there is some interest.
[1075.44 --> 1081.64]  Interestingly enough, they recently called blockchain as B-word.
[1083.72 --> 1084.48]  As what?
[1085.10 --> 1086.00]  B-word.
[1086.66 --> 1087.64]  Oh, B-word.
[1087.72 --> 1089.00]  Is it a bad thing or a good thing?
[1090.00 --> 1090.86]  I don't know.
[1091.04 --> 1096.44]  It's pretty much this word is used too often, I guess.
[1096.44 --> 1101.66]  And they jokingly call it B-word just to emphasize that.
[1102.04 --> 1102.62]  That's funny.
[1102.68 --> 1103.68]  People are talking about it so much.
[1103.74 --> 1104.86]  It's become the B-word.
[1104.94 --> 1105.30]  I see.
[1105.70 --> 1105.96]  Gotcha.
[1106.68 --> 1109.68]  Well, I think this might be a good chance to step back, take a break.
[1110.24 --> 1115.28]  Of course, we're here to talk about ZeroDB, which is your guys' startup and your open source project.
[1115.28 --> 1122.60]  We'll probably start with the conversation around the open sourcing of it and why it's open source and all those things.
[1123.08 --> 1131.48]  And then we'll dive deep into not just what it is, but how does it work, but why is it cool, and all those things that developers love to hear about.
[1131.64 --> 1137.34]  So let's step back for a moment, hear from one of our sponsors, and we will talk about all those things on the other side of the break.
[1138.18 --> 1139.78]  We know you listen to other podcasts.
[1140.08 --> 1140.46]  Don't worry.
[1140.52 --> 1141.14]  We're not upset.
[1141.14 --> 1144.70]  We know that ChangeLog isn't the only podcast in your list.
[1144.70 --> 1145.60]  And you know what?
[1145.86 --> 1153.46]  You may have heard advertisements on other shows about other hiring platforms and other places like our friends at TopTow.
[1153.58 --> 1159.76]  But let me tell you, there is no match to how invested TopTow is to both sides of the equation.
[1160.24 --> 1168.78]  You have companies out there who need great engineers, great designers, and you have great designers and great engineers out there needing great opportunities.
[1168.78 --> 1177.72]  And TopTow plays both sides of that fence very well, helping make sure the right kind of opportunities are there and the right kind of developers and designers are there.
[1177.72 --> 1189.80]  And if you're a CTO listening to this or someone on a team who knows you need to expand and add more people to help reach your goals, TopTow is the best place to go and find the best designers and the best engineers out there.
[1189.80 --> 1203.96]  And if you're one of those best engineers or best designers looking for great places to do great work and freelance and travel the world and have a lot of freedom, but also have the same kind of support you would want from working somewhere, TopTow is that place.
[1204.02 --> 1204.92]  You can blog with them.
[1205.16 --> 1206.40]  You can travel the world with them.
[1206.62 --> 1208.24]  They have meetups all around the world.
[1208.24 --> 1218.86]  They absolutely love to encourage and to support and help their developers and the designers that are in their network all around the world grow and be better and do better.
[1219.00 --> 1221.24]  Head to TopTow.com to find out more.
[1221.44 --> 1224.76]  That's T-O-P-T-A-L.com.
[1225.04 --> 1227.74]  Once again, T-O-P-T-A-L.com.
[1227.88 --> 1238.08]  But if you want a personal introduction on either side of the fence, whether it's an introduction to find the best designers and developers, or if you're a designer developer looking for great opportunities,
[1238.24 --> 1239.38]  get in touch with me.
[1239.52 --> 1241.38]  I'd be glad to give you a personal introduction.
[1241.82 --> 1244.98]  Email me at adam at changelaw.com.
[1245.10 --> 1246.38]  And now back to the show.
[1250.82 --> 1251.46]  All right.
[1251.48 --> 1257.24]  We are back speaking with McLean Wilkinson and Michael Egorov of ZeroDB about ZeroDB.
[1257.96 --> 1267.22]  And as we teed up before the break, our first question, as often our first question on a show about open source software is why is ZeroDB?
[1267.22 --> 1268.72]  Open source.
[1269.44 --> 1271.72]  Well, I think it's, I mean, well, there are a lot of reasons.
[1272.12 --> 1273.66]  I mean, fundamentally, obviously, we're developers.
[1273.84 --> 1276.92]  We believe in open source and we want the things we work on to be open source.
[1277.60 --> 1290.28]  But even beyond that, just from a business perspective, I think in 2016, now that it's the new year, it's, it's, I think it's just super hard to have a closed source proprietary business, software business,
[1290.28 --> 1293.50]  particularly when you're dealing with infrastructure tools or dev tools.
[1294.42 --> 1302.18]  And even moreover, when it's, you know, something that's so security focused like ZeroDB, you, of course, don't want your, you know, have security through obscurity.
[1302.30 --> 1310.00]  So obviously, the more eyeballs we can get on ZeroDB, the more we can be sure and confident in its security and in our implementation of it.
[1310.00 --> 1322.76]  And then beyond that, just looking at where the, you know, where software industry has gone, you know, if you're a developer and you're selling to developers, developers' first choice, they're going to look at an open source tool.
[1323.24 --> 1325.72]  And if you're closed source, you're sort of starting behind the eight ball.
[1325.72 --> 1332.24]  So I think it's, it's very difficult to build a closed source tools company today.
[1332.74 --> 1336.24]  Looks like you've selected the AGPL license.
[1336.72 --> 1341.98]  Would one of you speak to that decision and what all that implies as an open source license with ZeroDB?
[1343.18 --> 1343.66]  Sure.
[1343.78 --> 1350.74]  So we, we've looked at very closely at 10Gen and MongoDB as kind of a model for, for what our business could potentially look like.
[1350.74 --> 1354.88]  Um, so with AGPL, um, obviously it's an open source license.
[1355.00 --> 1358.18]  People are free to use ZeroDB, um, for their projects.
[1358.34 --> 1365.92]  The requirement there is if you're building on top of it or making extensions to it, you need to open source what you do on top of it as well.
[1366.68 --> 1368.64]  Um, and for a lot of people, that's fine.
[1368.82 --> 1379.12]  Um, for some people, particularly maybe enterprises that aren't as, you know, into the open source movement quite yet, they prefer to have what they build still be closed and proprietary.
[1379.12 --> 1381.54]  So in that case, you know, we can sell them a commercial license.
[1382.20 --> 1390.62]  Um, and then we're also considering, you know, if we include extra features and potentially like an enterprise edition, um, that we could license as well.
[1390.64 --> 1392.40]  Although we don't, we haven't done that quite yet.
[1392.40 --> 1394.00]  We're still thinking around that.
[1394.74 --> 1402.00]  Um, and then obviously, you know, on the business side, you can, in addition to selling licenses, you can sell support, uh, and things like that.
[1402.00 --> 1411.94]  Um, I'm curious on that, uh, licensing front, like, you know, Jared, I don't know about you, but I still feel like licenses to me, like they run together.
[1411.94 --> 1412.98]  I have a good memory.
[1413.04 --> 1414.72]  I try my best, but it's like documentation.
[1414.72 --> 1416.06]  I have to go back and look it up.
[1416.06 --> 1424.28]  And I'm just wondering, McLean for you, if, if you had any advice from somebody, like, did you have a lawyer step in and sort of walk through that with you?
[1424.28 --> 1433.26]  So as we have people listen to the show, I'm just wondering if there are resources out there aside from say the ones that are known, like choose a license from GitHub, which is really helpful.
[1433.92 --> 1437.46]  What resources did you use to, to, to make the decisions you just made?
[1438.20 --> 1438.66]  Yeah, we did.
[1438.70 --> 1441.54]  We did talk to a lawyer just to sort of sanity check everything we're doing.
[1441.54 --> 1443.70]  I wouldn't say we went to a lawyer to start.
[1444.12 --> 1454.42]  Um, I mean, there's obviously tons of resources online in terms of, you know, advice around building an open source business and what the different models might look like.
[1455.08 --> 1462.88]  Um, of course, even though it's not super fun reading through the actual licenses, particularly the one that you choose, you should probably do that at least once or twice.
[1462.88 --> 1463.98]  So that you actually understand.
[1464.68 --> 1465.16]  Waste of time.
[1465.24 --> 1465.74]  Waste of time.
[1465.98 --> 1466.62]  Nobody reads them.
[1466.62 --> 1475.02]  And then obviously, you know, talking to, talking to people that have done an open source business and have used a particular license.
[1475.24 --> 1481.28]  One, one caution I would say is it's generally better, at least in my opinion, to choose sort of a standard license.
[1481.28 --> 1485.50]  So something that's, that's known and people are relatively familiar with.
[1485.50 --> 1490.00]  Obviously you have the MIT licenses, the Apache licenses, the GPL ones.
[1490.62 --> 1497.66]  Um, as long as it's something standard and not, I think if you, I think where you could potentially get into trouble is you have some sort of bespoke license.
[1498.20 --> 1502.68]  And that just sort of, that makes the hurdle for someone actually using your software that much higher.
[1503.06 --> 1509.10]  Because then particularly if it's, if it's a company, um, they're going to have to have their legal department look at it and understand it.
[1509.10 --> 1513.32]  Right. You involve nothing against lawyers, but you involve those guys, things to get slow.
[1513.58 --> 1518.40]  You have to do things that you wouldn't normally do and you can't quite be quite as agile around decisions.
[1519.10 --> 1530.26]  Yeah. And one of the benefits of having an open source in the first place is, is lowering the adoption hurdle where, you know, if you're, if you're, if you're forcing people to go through the legal department, that sort of defeats that entire purpose.
[1530.26 --> 1541.78]  I like that process of looking at a company that you, you know, that you like their model. You've seen it. It's, it seems to work at least, uh, with regard to the way they're going about building a business or on open source.
[1542.08 --> 1554.52]  And then just saying, well, I like for 10 gen, like you said, that that's the kind of model that we want to follow with our business. And so let's check out what they're doing and use that as a starting point, at least to having conversation with lawyers.
[1554.52 --> 1564.26]  Or if, if you're able to, you know, get somebody's ear at 10 gen, who's, who's in those decisions and ask like, how do they feel about the fact that they have this license and how is it working out for them?
[1564.50 --> 1568.18]  I think that's a great way of going about it as, as opposed to just starting with a blank slate.
[1568.76 --> 1580.48]  Yeah. And I think the interesting thing also in the open source businesses, it's in reality, the entire life cycle of the entire sort of this open source movement is very early, particularly thinking around business models with it.
[1580.48 --> 1592.92]  So I don't think anyone really has the answer quite yet. So everyone's still sort of experimenting and seeing what might work, what doesn't work and, and trying to figure out how you can build, you know, a sustainable business on, on top of open source software.
[1593.70 --> 1600.26]  It's further down our notes. So Jared and I put together notes for each show and it's further down a list than the first question, which was the obvious one, why open source?
[1600.26 --> 1616.20]  But it makes sense to bring up here, which is the, the patent pending algorithm piece. How does that play into and having a patent on software, I guess, or I'm not sure what the exact patent is for, but how does that play into the open source nature of this project?
[1616.20 --> 1625.96]  Yeah. So we have a provisional patent filed and I, we, I think the reason you file a provisional patent is sort of get a date on it.
[1625.98 --> 1630.78]  And so you have like a, up to a year after you filed a provisional to apply for the actual patent.
[1632.06 --> 1641.02]  And I would say that was done out of sort of an abundance of caution. So we don't know, obviously it was open source, the code is available and free for people to use.
[1641.02 --> 1646.96]  And I think also in practice, it's unclear that software patents really work.
[1648.62 --> 1654.64]  You know, and, and so it's sort of an abundance of caution, a little bit of a check the box from an investment perspective.
[1655.46 --> 1661.18]  You know, obviously a big question you get when you're, you're going to raise money is, you know, what does your IP look like?
[1661.18 --> 1662.64]  And is that defensible?
[1662.64 --> 1668.04]  I wouldn't say the patent is really a core piece of our strategy going forward.
[1669.20 --> 1678.14]  But it's, it's something that we did just, just in case, you know, obviously when we're thinking through this, we didn't know exactly what things will look like, you know, a year from now.
[1678.14 --> 1684.94]  So we just wanted to be, have, have that option if it, if it was something that we thought would be valuable for the business going forward.
[1685.94 --> 1686.88]  That makes sense.
[1686.88 --> 1693.34]  Interesting. Well, let's dig down into what 0DB really is and what it's here to offer us as open source developers.
[1694.20 --> 1695.82]  You know, what it does and how it works.
[1696.54 --> 1699.00]  You call it an end-to-end encrypted database.
[1700.46 --> 1706.96]  Michael, could you unpack that for us and tell us what 0DB does and why it's different than stuff that's already out there?
[1706.96 --> 1718.90]  Sure. What it allows you to do is pretty much to use this database to do queries without the database server knowing anything about your data or knowing your keys.
[1719.48 --> 1729.02]  So all the keys always stay with the client and still from this client, you're able to query your data, obviously without pulling the data down to the client.
[1729.02 --> 1735.04]  So for those out there who may be thinking, well, couldn't you just use full disk encryption?
[1735.78 --> 1738.36]  You know, there are offerings out there.
[1738.80 --> 1738.96]  Right.
[1739.04 --> 1742.38]  You know, you have record level or column level encryption, you have full disk encryption.
[1742.84 --> 1743.20]  Sure.
[1744.18 --> 1748.20]  And so I just want to put a stressing point on how this is different than those things.
[1748.32 --> 1752.92]  So could you compare and contrast it to like, well, I'll just encrypt the entire disk on my server and I'm good to go?
[1752.92 --> 1753.36]  Yeah.
[1753.36 --> 1754.00]  Yeah.
[1754.18 --> 1768.24]  So basically when you encrypt your entire disk on the server or use column level encryption, every time you query, at least, you expose your encryption keys to the server.
[1768.58 --> 1771.66]  So these keys are at least in memory.
[1771.66 --> 1783.90]  And any attacker who is sitting on the server can pretty much take a snapshot of memory and figure out where the keys are and decrypt the data.
[1784.74 --> 1792.64]  And it wasn't so much of a problem when the threat was somebody physically stealing your hard drives.
[1792.84 --> 1798.34]  But now in a very networked world, most of attacks are remote.
[1798.34 --> 1804.48]  So if somebody infiltrates into the server, this is actually really a problem.
[1804.80 --> 1808.26]  There's a nice little analogy, which isn't necessarily exactly technically accurate.
[1808.42 --> 1813.24]  But if you compare it to like a physical vault, so you have your valuables inside of the physical vault.
[1813.32 --> 1814.34]  You're going to lock the door.
[1814.94 --> 1818.16]  You're not going to hang the key up on a nail next to that door and go home.
[1819.16 --> 1823.42]  But in a way, not exactly, but in a way, that's what you're doing when you're encrypting data at rest.
[1823.42 --> 1827.78]  So you're still having to send the key over to this database server where your data is.
[1828.66 --> 1831.42]  And that's the window that we're trying to close with 0DB.
[1832.12 --> 1833.90]  I think that's definitely a helpful analogy.
[1834.24 --> 1839.76]  Like you said, probably not exactly 100% accurate, but I think that does help paint the picture a little bit.
[1841.28 --> 1847.58]  One thing that's always advised with security is the defense in depth principle, which is to say,
[1847.58 --> 1852.90]  you know, don't just lock the door, but also don't just have a key, also have a padlock and then also do this.
[1852.98 --> 1860.10]  And I'll just add layers of depth to that security is, would you guys consider 0DB in that case a layer of security?
[1860.10 --> 1863.82]  Or would you say, if you're using 0DB, we don't need the full disk encryption.
[1864.00 --> 1866.82]  You obviously can't really even do column encryption, I would guess.
[1866.92 --> 1869.78]  But are these instead ofs or are these alsos?
[1869.78 --> 1873.82]  Well, I would say with 0DB, we call it encryption in use.
[1874.12 --> 1876.24]  And so by default with encryption in use, you still have it.
[1876.42 --> 1877.60]  It's still encrypted at rest.
[1878.20 --> 1882.22]  It's still encrypted in flight, you know, as the data is moving between client and server.
[1882.72 --> 1887.50]  And of course, you could also layer on top TLS or SSL to that if you liked.
[1887.50 --> 1896.56]  But I would certainly not suggest that someone just use 0DB and totally forget about the rest of their security posture.
[1897.40 --> 1900.24]  That's definitely not what we would advise.
[1900.78 --> 1902.96]  You don't want to go and like what we'd say that, is that what you're saying?
[1903.02 --> 1903.28]  Yeah.
[1903.28 --> 1920.58]  What we tried to do with 0DB was, so if you assume that the database server is compromised, how can you still mitigate the potential for your data to be, the actual underlying unencrypted data to be stolen on the server?
[1921.64 --> 1923.54]  So that's the way that we came at it.
[1924.10 --> 1927.66]  And the answer is your server should never know anything, basically.
[1927.66 --> 1942.20]  Yeah, I mean, if you never send the encryption keys to the server and assuming you're using strong encryption like negaS256, then all an attacker is going to see is just a bunch of encrypted gibberish.
[1943.08 --> 1943.78]  So how does it work?
[1943.88 --> 1946.66]  You got the server's dumb in the sense of the encryption technology.
[1947.76 --> 1950.48]  I'm guessing it's just storing crypto text.
[1952.56 --> 1953.62]  How does it work?
[1954.88 --> 1956.22]  Tell us how it works, guys.
[1957.66 --> 1967.04]  Yeah, so basically, apart from encrypted records, we have encrypted index, and that's what makes the thing working.
[1967.88 --> 1970.80]  And the way it works is really easy.
[1971.42 --> 1976.48]  So the encrypted index is a tree-like structure, pretty much a B-tree.
[1977.24 --> 1985.42]  And it is pieces of this B-tree, the buckets, are encrypted before they go to the server, right?
[1985.42 --> 1989.62]  So the server observes only already encrypted buckets.
[1990.18 --> 2001.42]  And the way we do queries, the major, the key piece in it is that the client traverses this B-tree remotely.
[2001.42 --> 2015.84]  So pretty much it pulls down the root of the tree, decrypts it, figures out what piece of B-tree to request next, requests it, and in several steps it finds what it was looking for.
[2015.84 --> 2030.98]  Of course, it's not all that easy because it becomes a little bit more involved when you need to do some operations like set intersections or things like that.
[2030.98 --> 2036.38]  But the key piece is this traversal of the tree from the client.
[2037.42 --> 2042.78]  So let's talk a little bit about the ergonomics of the database or the kind of database it is.
[2042.90 --> 2049.82]  Because I think you mentioned somewhere that, you know, it's a 0DB, it's an end-to-end encrypted database, and you also have protocol mentioned.
[2049.82 --> 2053.64]  But at the end of the day, it has to be a database, right?
[2053.90 --> 2057.40]  So what kind of database is it?
[2057.46 --> 2059.28]  Is it like an SQL-compliant relational database?
[2059.58 --> 2062.50]  Is it a key value store or, you know, a document store?
[2062.54 --> 2063.46]  What kind of database is it?
[2063.52 --> 2064.94]  How do you work with it?
[2065.98 --> 2070.74]  It's more like an indexed document store, somewhat similar to MongoDB.
[2070.74 --> 2082.88]  Interestingly enough, we base it on something called ZODB, which is a part of ZOB framework, if you remember this thing.
[2084.38 --> 2089.74]  And ZODB wasn't super popular at the time when it was a thing.
[2090.68 --> 2097.26]  The reason, I think, is because it's more like a kit for building databases rather than a database on itself.
[2097.26 --> 2101.34]  So we use that to build 0DB.
[2102.22 --> 2104.76]  The name is similar, as you can recognize.
[2106.20 --> 2112.68]  And from that, we inherit such features as ACT compliance.
[2113.48 --> 2120.10]  We can do replication and things like that, again, inherit it from ZODB.
[2120.10 --> 2128.10]  And, yeah, that pretty much explains how we have all these features.
[2128.34 --> 2132.28]  We just add the end-to-end encryption piece on top of that.
[2132.62 --> 2137.70]  That makes a lot of sense because what I was starting to think when I was reading through what you guys are up to with 0DB is,
[2138.26 --> 2143.78]  at the end of the day, like, wow, there's a lot of stuff you have to build if you're building a database, right?
[2143.88 --> 2144.34]  That's right.
[2144.34 --> 2149.50]  Your key differentiator is the encrypted part of it, but that you're also offering a database, right?
[2149.70 --> 2152.78]  And I was like, they just decided to just redo all these things.
[2153.02 --> 2160.36]  And now I'm finding out ZOB object database, you know, has transactions, history undo, transparently plug-in storage,
[2160.52 --> 2163.90]  all these things that you guys could just build on top of.
[2163.90 --> 2170.68]  And, you know, leave that to somebody else, so to speak, or at least the foundation is there for you,
[2170.76 --> 2172.96]  which looks like it's a Python-based thing.
[2173.70 --> 2175.42]  That's the beauty of open source.
[2175.74 --> 2176.08]  Yeah.
[2176.08 --> 2176.42]  There you go.
[2176.72 --> 2178.52]  So, good idea.
[2178.96 --> 2180.34]  So, is that a fork, though?
[2180.40 --> 2185.74]  I mean, are you using actually ZODB behind the scenes and you're following and tracking that project,
[2185.74 --> 2189.12]  or is this something that you've forked and you're using your own version of it?
[2189.12 --> 2189.52]  Yeah.
[2190.80 --> 2202.60]  Basically, the way ZODB is built, it's super modular, so you can actually use its pieces as a library and you will still be okay.
[2202.78 --> 2204.16]  So, that's how we're using it.
[2204.48 --> 2210.04]  Of course, we could fork it, but it seems like it wasn't necessary so far.
[2210.04 --> 2214.92]  I guess maybe another question on that is, since, Jared, you mentioned it's Python-based,
[2215.40 --> 2216.84]  what made you choose this database?
[2216.98 --> 2221.46]  Why this one and not, you know, some of the other options out there that are available to everyone?
[2222.10 --> 2230.94]  It's actually, being built in Python, it allows us to move pretty quickly, to develop things quickly,
[2231.38 --> 2234.64]  faster than if we would do that in C.
[2234.64 --> 2244.90]  And if you think about performance, well, it seems like performance is good enough.
[2245.02 --> 2253.96]  I mean, all the limitations come not from Python by itself.
[2253.96 --> 2266.78]  You have, like, encryption overhead, things like that, and that pretty much outweighs the fact that the database is written in Python.
[2266.96 --> 2271.72]  And actually, ZODB, if you use that properly, is pretty fast.
[2271.72 --> 2279.36]  Yeah, I think a big piece of it was just, you know, as you said before, we don't want to have to rebuild a new database from scratch.
[2279.44 --> 2284.80]  So, we lean on something that's existing, and ZODB is, as Michael said, a good kit for doing that.
[2285.94 --> 2289.34]  But, you know, as you pointed out, I think before, there's, you know, we had the word protocol there.
[2289.46 --> 2293.46]  So, in principle, you know, you could build a database from scratch that does ZODB.
[2293.46 --> 2300.82]  You could potentially build it on top of another database, on a SQL-based database, for example.
[2301.34 --> 2306.86]  That's what I was thinking about when you said that, was, like, if, is this, you know, obviously, you're at a certain point.
[2307.06 --> 2313.14]  If someone else preferred a different database, could they take the same principles or the same things you've done with the idea of it being a protocol?
[2313.24 --> 2317.60]  Could they apply that to, you know, XYZ database or a different preference, at least?
[2318.56 --> 2319.54]  You certainly could.
[2319.64 --> 2322.16]  And I would say it's not a trivial thing to do.
[2322.16 --> 2340.86]  And one thing we've actually thought about is, is there a way for us to potentially sit alongside of existing databases, particularly when we're talking to a lot of the banks, like, they're running, you know, Oracle, MySQL, Postgres, a lot are still running even DB2 and Sybase stuff.
[2340.92 --> 2343.26]  So, is there a way, potentially, for us to sit alongside of that?
[2343.26 --> 2352.44]  Of course, you know, a large bank isn't going to rip out all of their existing database instances and replace them with 0DB as much as we would like that.
[2353.08 --> 2355.64]  So, in that case, I mean, we don't have this ready today.
[2355.76 --> 2365.10]  But our thinking around there is potentially they can keep using Oracle, for example, for the storage, throw encrypted records in there and have a 0DB index that would sit next to that.
[2365.10 --> 2370.18]  And actually, when they want to go query those encrypted records, they'll go through our index.
[2370.76 --> 2376.22]  So, I would say still forming our thoughts around that piece, but that's a possibility for the future.
[2376.48 --> 2376.50]  Yeah.
[2376.74 --> 2377.32]  Well, let's be honest.
[2377.46 --> 2381.80]  I mean, this is fairly, you know, fairly new, like in this last year.
[2381.96 --> 2385.78]  So, in 2015, this whole entire thing for you guys was born, right?
[2385.78 --> 2393.88]  Like you guys connected in March, it sounded like if I'm painting back the history, and then by the time of December, we had an open source project that was spawned off, now a business.
[2394.00 --> 2399.94]  So, you're still in the forming your ideas innovation stage, to say the least, I'm sure, right?
[2400.94 --> 2401.22]  Yeah.
[2401.50 --> 2411.82]  Certainly still super early days and, you know, working through everything, both from the technical engineering and product development stuff to, you know, thinking through the business model stuff that we talked about earlier.
[2412.60 --> 2412.98]  Gotcha.
[2412.98 --> 2413.10]  Gotcha.
[2414.00 --> 2414.90]  Well, let's take another break.
[2414.96 --> 2421.22]  When we come back from this break, we're going to cover the deeper sides of the client side of this database.
[2421.76 --> 2423.12]  So, stay tuned.
[2423.44 --> 2424.52]  We'll cover that when we come back.
[2425.18 --> 2431.96]  Our friends at DigitalOcean, Simple Cloud Hosting built for developers, launched a new feature recently we absolutely love.
[2432.26 --> 2436.86]  It's called Droplet MultiCreate for easily launching up to 10 servers at once.
[2437.32 --> 2441.96]  You can deploy multiple droplets when you create your droplets with the exact same configuration.
[2441.96 --> 2443.46]  And this is a huge feature.
[2443.52 --> 2444.34]  We absolutely love it.
[2444.34 --> 2446.36]  Head to DigitalOcean.com.
[2446.56 --> 2452.54]  And when you sign up, use our code CHANGELAW to get a $10 hosting credit when you sign up.
[2452.54 --> 2458.30]  All right.
[2458.30 --> 2466.70]  We're here with McLean and Michael talking deeply about 0DB, the protocol, the database, and all the odds and ends of this.
[2466.84 --> 2469.60]  And, you know, the encryption is handled by the client.
[2469.60 --> 2472.36]  And right now, there's only a Python client.
[2472.50 --> 2474.98]  So, it seems like you're bullish on Python, which is a good thing.
[2475.16 --> 2478.52]  And at one point, Michael, you mentioned you could do it faster in Python than you could in C.
[2478.98 --> 2483.92]  But I guess the question we have here is roughly around the clients, will this always be the case?
[2484.02 --> 2485.16]  Are you planning other clients?
[2485.62 --> 2491.10]  And how much work does it take to create a new client, let's say, for Ruby or JavaScript, for example?
[2491.94 --> 2492.32]  All right.
[2492.32 --> 2494.86]  Yeah, that's a very interesting question.
[2495.52 --> 2502.78]  So, obviously, now we support JSON API so that you can interface it from anywhere.
[2503.42 --> 2514.68]  But that means that you have to run this JSON API server on the client machine, which is not always very convenient.
[2514.68 --> 2523.58]  So, and the first thing people are requesting is actually JavaScript client, right?
[2523.98 --> 2527.78]  So, of course, nothing prevents us from writing that.
[2528.50 --> 2537.46]  The easiest way is to port Python code using something like PyPy.js.
[2537.94 --> 2541.06]  And apparently, it can work.
[2541.06 --> 2552.62]  But probably the more proper way would be to actually write a JavaScript client.
[2553.40 --> 2555.78]  And that's, you know, something we are planning.
[2556.40 --> 2567.96]  Another thing is that in this financial world, when banks want to outsource their databases to the cloud and do things like that, they often use Java.
[2567.96 --> 2576.92]  So, and they obviously need some way for their Java code to interact with 0DB.
[2577.48 --> 2581.76]  And for that, we would need some JDBC connector.
[2582.68 --> 2586.66]  And that is possible to do.
[2586.96 --> 2591.28]  And I think with Java, we can go with JITAN, actually.
[2591.28 --> 2607.28]  So, that begs the question of why, at this point, maybe, on the client side at least, maybe a C library that's portable and can be interfaced and wrapped from these other higher-level languages might, in the long term, become faster-moving.
[2607.94 --> 2611.16]  Because it seems like there'd be a lot of smarts in the clients.
[2611.96 --> 2619.66]  And so, you may have, you know, you may end up with six implementations of the same encryption stuff.
[2619.66 --> 2620.06]  Yeah.
[2623.00 --> 2624.16]  Just keep your thoughts on that.
[2624.74 --> 2625.08]  I don't know.
[2626.00 --> 2627.64]  Yeah, we'll see how it goes.
[2627.84 --> 2634.62]  I guess we will start from porting from Python code, which is certainly possible to do.
[2634.72 --> 2636.78]  You can do that with JavaScript.
[2637.24 --> 2638.34]  You can do it with Java.
[2638.48 --> 2642.32]  You can do mobile clients from, like, Python ported to there.
[2642.32 --> 2646.48]  But long term, you quite can be right.
[2647.28 --> 2648.92]  I guess it kind of depends, too, Jared.
[2649.14 --> 2652.38]  I mean, it seems like this is for everyone.
[2652.70 --> 2658.28]  But obviously, financial tech has the most, or financial people have the most initial benefit from this.
[2658.38 --> 2663.74]  But, you know, obviously, other developers are thinking, how can I use this end-to-end encryption on my own account?
[2663.74 --> 2667.88]  It kind of depends maybe on their motivation on who they're focusing on.
[2668.02 --> 2673.62]  So, it might be open source, but it might be focusing on financial tech, and they're kind of happy with Python, for example.
[2674.56 --> 2674.94]  That's right.
[2675.52 --> 2678.24]  Yeah, I mean, I'm just thinking about it in terms of other databases.
[2678.62 --> 2680.76]  Let's take, again, MongoDB as an example.
[2680.76 --> 2692.98]  Like, as a business, it's in MongoDB or 10Gen's best interest of having as many client libraries as possible and keeping those up-to-date and, like, awesome and everything like that.
[2694.06 --> 2699.74]  And as the technology matures, you know, they have to maintain all of those, even though they're open source.
[2699.90 --> 2701.62]  And, of course, the community can do all this stuff.
[2701.74 --> 2703.20]  It's in their best interest to do that.
[2703.62 --> 2707.70]  And similarly, I would think that it's in ZeroDB's best interest to have as many clients as possible.
[2708.84 --> 2709.72]  Is that the case?
[2709.72 --> 2712.80]  Yeah, I mean, I think, is that the case, guys?
[2713.78 --> 2715.36]  Yeah, that's definitely the case.
[2715.80 --> 2716.00]  Yeah.
[2716.28 --> 2719.98]  And so, then my question was, like, your guys' clients have to be really smart, right?
[2720.02 --> 2724.34]  Lots of surface area of code because of all that you're doing client-side.
[2724.86 --> 2731.82]  And so, I just would see that that might be a bottleneck for you, like, you know, software-wise, potentially.
[2732.88 --> 2733.90]  So, is it an issue?
[2734.96 --> 2735.78]  I mean, yeah.
[2735.78 --> 2740.26]  Yeah, obviously, I think you're probably, you're pretty, you know, it's a good insight.
[2740.36 --> 2745.94]  I think, in general, like, it's always a struggle, you know, allocating resources when you're a super early-stage company.
[2746.08 --> 2751.72]  And, you know, what, you know, thinking long-term versus, you know, what are some quick wins?
[2751.72 --> 2758.08]  So, yeah, I mean, that's certainly one of the challenges of doing any business, particularly a software business.
[2758.08 --> 2763.16]  Is that a place where you guys are looking for help from the open-source community?
[2763.36 --> 2765.48]  Or is that more like your bread and butter?
[2766.10 --> 2769.64]  Actually, open-source community already offers some help in that.
[2769.84 --> 2777.42]  So, we've seen some people who want to port 0DB to mobile platforms for their own purposes.
[2778.32 --> 2786.22]  And we are, actually, we are happy to accept this help because this was one of the reasons why we open-source.
[2786.22 --> 2787.24]  Mm-hmm.
[2787.68 --> 2793.20]  Yeah, I mean, if someone wants to build an alternative client, we'd be super happy to see that.
[2793.42 --> 2796.48]  And we definitely support them in that effort.
[2797.00 --> 2797.44]  Cool.
[2797.58 --> 2804.68]  So, speaking just more about the client side of things, since you're putting so much of the smarts in the client,
[2804.82 --> 2807.18]  and you have the decryption is client side, right?
[2807.22 --> 2808.58]  The key handling is client side.
[2808.98 --> 2809.30]  Mm-hmm.
[2809.30 --> 2813.90]  And the server is an encryption store, basically.
[2814.16 --> 2817.92]  There's some smarts in there, but like you said, if it doesn't have the secrets, it can't share the secrets.
[2818.26 --> 2818.64]  That's right.
[2818.90 --> 2822.72]  Are we just kind of, is it just kind of moving the ball around a little bit?
[2822.78 --> 2827.02]  Because now, instead of your server being the source of truth to a certain degree,
[2827.08 --> 2829.38]  and if it gets compromised, you're in big trouble.
[2829.94 --> 2833.24]  If one of your clients gets compromised, is the whole game up?
[2833.24 --> 2838.02]  Or is there something that segregates where if a client gets compromised, it's not a big deal?
[2839.12 --> 2844.34]  Well, even today, you have this problem with the smart server model.
[2844.66 --> 2851.46]  If your client is compromised, you still get your data exposed.
[2852.04 --> 2856.96]  But we just close one window on the server, right?
[2858.14 --> 2861.42]  But this is actually not the only thing we do.
[2861.42 --> 2870.64]  With the client, on the server, you can, of course, throttle the data so that when a client is compromised,
[2872.06 --> 2876.52]  the attacker couldn't steal absolutely everything, just a little bit.
[2877.32 --> 2884.48]  Another thing is we have this sharing or like proxy re-encryption piece.
[2884.48 --> 2895.82]  The way it works, we can enable somebody else, be it third party or yourself using a different device.
[2896.12 --> 2904.48]  We can enable the third party to query your data still without the server knowing anything.
[2904.48 --> 2915.44]  So let's say you can share data with your friend and your friend can still do the queries which you allow him to do.
[2916.58 --> 2926.40]  And the server doesn't know anything, but the server can revoke the access so that your friend with his key cannot access this data after a day or two.
[2926.40 --> 2927.40]  How does that work?
[2927.40 --> 2928.40]  How does that work?
[2928.40 --> 2929.40]  Yeah.
[2929.40 --> 2933.12]  So it's based on a technology called proxy re-encryption.
[2933.12 --> 2938.24]  It's a pretty young family of encryption algorithms.
[2938.24 --> 2943.24]  The first one appeared in 1998.
[2943.24 --> 2951.38]  The way it works is you have, let's say you want to share your data with somebody with a different key pair.
[2951.38 --> 2961.74]  You take their public key, your private key, and calculate a special thing called a transformation key.
[2962.26 --> 2964.42]  And you give this transformation key to the server.
[2964.42 --> 2975.30]  The only thing the server can do with a transformation key, it can transform data from being encrypted to you into being encrypted for the third party you are sharing your data with.
[2975.80 --> 2983.18]  So we combine this encryption primitive with our query algorithm.
[2983.58 --> 2988.56]  And this allows us to pretty much share data on a granular level.
[2988.56 --> 2996.04]  So you can say, I want to share everything matching this query with the guy who has that public key.
[2996.04 --> 3006.80]  And then that guy can pretty much query the data in that subset until this transformation key expires.
[3007.00 --> 3013.44]  When the transformation key expires, the server removes that, and that guy cannot query this data anymore.
[3013.44 --> 3025.04]  So, for example, if you are afraid that the third party can get the key compromised, you limit the time span of it to be very short.
[3025.04 --> 3036.12]  And you don't have to re-encrypt all your data again and again because you are not sharing the key with which actually the data are encrypted.
[3036.92 --> 3038.60]  I mean, that sounds like a real advancement.
[3040.04 --> 3042.46]  Proxy re-encryption, that just sounds cool, right?
[3042.68 --> 3043.12]  It does.
[3043.44 --> 3044.16]  Very cool.
[3044.56 --> 3045.52]  Very impressive.
[3045.64 --> 3046.86]  We support proxy re-encryption.
[3047.58 --> 3047.96]  Of course.
[3050.50 --> 3054.24]  Yeah, it's been around for not a super long time.
[3054.30 --> 3055.14]  It's been around for a while.
[3055.24 --> 3067.28]  And there's actually been a couple of companies that have tried to commercialize it in sort of a file sharing context where, you know, you have files that are sitting up in the cloud that are encrypted under your keys and you want to share them with someone else.
[3067.28 --> 3072.12]  And I wouldn't say that's been super successful or hasn't really taken off.
[3072.12 --> 3084.06]  But I guess what's potentially interesting about proxy re-encryption in the context of 0DB is that we can pair it with a lot of our other query protocols so you can share stuff on a much more granular level.
[3084.06 --> 3089.90]  Yeah, I was going to ask about use cases because it was like incredibly impressive in my mind.
[3089.98 --> 3094.98]  But I kept thinking like, how exactly would somebody use this to like an application advantage?
[3094.98 --> 3099.10]  I think file sharing is, you know, the one that comes to mind.
[3099.22 --> 3106.26]  Are there other ways that you guys see that being used that maybe even isn't currently being used or that can go to market?
[3106.26 --> 3113.90]  Right. So, yeah, I mean, one kind of cool example would be, let's say, a health care app.
[3114.18 --> 3121.28]  So let's say you have a mobile application for storing people's personal medical records.
[3121.94 --> 3123.76]  And obviously those are quite sensitive.
[3124.68 --> 3133.76]  If you're a user of this app, you don't necessarily want that app provider, that service provider to have access to your medical information, your medical data.
[3133.76 --> 3144.14]  So if someone were to build something like that on top of 0DB, they could guarantee to their users that their PHI was totally secure and totally owned by them.
[3144.76 --> 3146.20]  They could control the keys.
[3146.86 --> 3155.24]  And of course, if they need to share it with, let's say, an insurance provider or their hospital or their doctor, they can use the proxy re-encryption piece for that.
[3155.32 --> 3159.76]  So I always think that's a pretty cool example for how something like that could be used.
[3162.18 --> 3163.36]  Yeah, that is very cool.
[3163.36 --> 3168.36]  And that just brings up my thoughts of HIPAA and other such compliance things.
[3168.90 --> 3170.50]  Do you guys run into any of those?
[3170.62 --> 3175.54]  I mean, like you said earlier, your main customer currently is banks.
[3176.18 --> 3178.60]  And so HIPAA is not a thing you guys got to worry about.
[3178.78 --> 3179.58]  Perhaps PCI.
[3179.86 --> 3182.16]  I don't know what other regulations the banking industry is under.
[3182.24 --> 3183.24]  You guys probably do.
[3183.24 --> 3189.38]  But have you come against regulations so far when it comes to 0DB?
[3189.38 --> 3196.02]  So in a way, obviously, a lot of our customers have to deal with these things.
[3196.02 --> 3201.94]  Us ourselves as a company or how we think about our products, we want to be sort of an enabler.
[3202.06 --> 3214.02]  And we're obviously providing infrastructure and developer tool for people to build applications that potentially could be compliant with these types of regulations like HIPAA or Dodd-Frank type stuff in financial services.
[3214.02 --> 3217.26]  And you have a whole other set of regulations over in the EU.
[3218.38 --> 3223.08]  So we don't, you know, we're obviously not building applications ourself at the moment.
[3223.08 --> 3226.92]  So that's not something that we're having to directly deal with.
[3227.04 --> 3234.06]  But obviously, to the extent that our customers could potentially be using 0DB to, you know, be in compliance with these regulations.
[3235.26 --> 3237.44]  That's something that we at least need to be aware of.
[3237.62 --> 3240.14]  I can give you one interesting use case from the EU.
[3240.30 --> 3242.38]  It has to do with data sovereignty laws.
[3243.56 --> 3248.36]  So let's say you're a bank in Europe and you have, you operate in a bunch of different countries.
[3248.36 --> 3250.52]  And then you generate some customer data in Germany.
[3250.52 --> 3259.14]  It's very difficult for you to move that data, that customer data in the clear across country borders, even inside of Europe.
[3260.32 --> 3263.44]  If you encrypt it, and it varies by country by country.
[3263.58 --> 3266.82]  For example, Switzerland is quite strict, so it doesn't work there.
[3266.94 --> 3273.78]  But if you generally, in general, if you encrypt that data, you can, you have more flexibility in terms of what you can do with it, where you can move it.
[3274.22 --> 3278.40]  But of course, historically, the problem has been that once you encrypt it, you can't use it anymore.
[3278.40 --> 3279.20]  You can't query it.
[3279.38 --> 3279.42]  Right.
[3279.42 --> 3286.32]  So a lot of banks actually will just have a data center in every single country that they operate because of this data sovereignty issue.
[3286.94 --> 3295.40]  Whereas if they were to use something like 0DB, they could have the keys in country, encrypt the data in country, ship it off to a data center in Luxembourg, for example.
[3296.52 --> 3301.52]  Still have it be queryable and only ever decrypt it inside in country as well.
[3301.52 --> 3308.58]  So in that scenario, you could consolidate, you know, 25 data centers in 25 countries down to potentially a much more manageable handful.
[3309.42 --> 3313.72]  And that is actually one of the reasons why we are in London at the moment.
[3313.72 --> 3321.22]  We see a bunch of regulations which don't stop us from operating, but actually help us.
[3321.62 --> 3324.68]  So and we are actually exploring that.
[3324.68 --> 3328.56]  So you said you're at the FinTech Innovation Lab in London.
[3328.64 --> 3331.50]  That's what you're doing there now that that's your incubator that you went through, right?
[3331.96 --> 3332.18]  Yep.
[3332.28 --> 3334.00]  That just started actually this Monday.
[3334.14 --> 3337.04]  So we're sort of diving in.
[3337.08 --> 3337.96]  So this is new for you, though.
[3338.36 --> 3338.64]  Like this.
[3338.88 --> 3338.90]  Yeah.
[3339.54 --> 3339.70]  Yeah.
[3339.70 --> 3340.20]  It just started.
[3340.20 --> 3342.64]  We have a few more questions on the tech side of things.
[3342.74 --> 3347.66]  But since this is the topic now, I was just talking to Jared behind the scenes about whether we should bring this back up again.
[3347.74 --> 3349.56]  So what are your goals, I guess, for this?
[3349.68 --> 3352.92]  How long is this process for you to be part of this incubator?
[3353.84 --> 3354.04]  Yeah.
[3354.06 --> 3356.84]  So the FinTech Lab lasts until mid-April.
[3358.22 --> 3360.86]  So we'll be primarily here in London, obviously.
[3361.90 --> 3369.64]  We actually sit in Canary Wharf, which is sort of the one of the banking districts in London where a lot of the banks are located.
[3370.20 --> 3377.64]  We'll be traveling a little bit to the EU to visit some of the banks in Italy, in Germany, for example.
[3378.12 --> 3382.26]  And then occasionally back to the U.S., obviously, because we have things going on there as well.
[3383.50 --> 3388.90]  But it's a standard sort of three-month program that a lot of these accelerators last.
[3389.68 --> 3391.14]  It's actually run by Accenture.
[3391.78 --> 3399.26]  So they're obviously quite helpful from having experience working with a lot of these banks and selling into banks, which, you know, you don't have to get into it.
[3399.26 --> 3407.44]  But that whole enterprise sales process is a whole other bugaboo there is trying to sell into banks, which in general is quite difficult.
[3408.00 --> 3414.02]  I mean, is your goal to move the company forward in this incubator or is your goal to move the technology forward in this incubator?
[3415.54 --> 3416.26]  I mean, that's...
[3416.26 --> 3416.80]  Is it one and the same?
[3416.80 --> 3419.24]  Yeah, they pretty much go hand in hand, I would say.
[3419.94 --> 3431.80]  You know, obviously, it's important for us to make the product better and not only more secure, but a big focus, obviously, for us is performance and limiting the tradeoff that people are making.
[3431.80 --> 3447.50]  So, obviously, you know, you have encryption and decryption overhead and things like that, but you want to make it as dropping as possible so that people aren't really getting hit on the performance side when they're using something like 0DB as opposed to just having data in the clear or just encrypted at rest.
[3447.50 --> 3456.56]  And obviously, when you're dealing with banks that have just massive amounts of data, performance is a pretty big concern for them.
[3456.56 --> 3462.26]  So, yeah, I mean, I think as you improve the product, you're moving the business forward at the same time.
[3463.10 --> 3469.56]  We have a few more questions on the performance stuff, but prior to that, I'm just thinking how...
[3470.42 --> 3482.06]  And maybe the question is really easy to answer, but how do you or how have you been able to financially set yourselves up to be able to take this time off and still live your lives and still do whatever you do?
[3482.06 --> 3485.24]  I have no idea if you guys are families, you know, dads or whatnot.
[3485.24 --> 3488.98]  So, I'm just making assumptions, you know, human beings have lives.
[3489.66 --> 3490.68]  So, how do...
[3490.68 --> 3491.56]  Obviously, we have lives.
[3492.12 --> 3500.20]  But, you know, how are you guys able to take this time to spend to develop the company, you know, away from, you know, Silicon Valley where you're normally at?
[3500.28 --> 3501.38]  Like, what have you done?
[3501.44 --> 3502.44]  Do you have backing?
[3502.54 --> 3503.12]  Do you have funding?
[3503.30 --> 3505.60]  What is that scenario like for your company?
[3506.60 --> 3510.34]  Yeah, so we've actually just been bootstrapped so far and been using our own money.
[3510.46 --> 3514.36]  I'd say it's just the two of us co-founders and developers at the moment.
[3514.36 --> 3521.22]  So, we don't have a ton of expenses, you know, outside of sort of, of course, you have to support yourself and you have to eat and you have to have somewhere to live.
[3521.38 --> 3521.60]  Right.
[3521.74 --> 3523.06]  So, there is some baseline.
[3524.60 --> 3525.80]  Well, it's a sacrifice too.
[3525.88 --> 3527.32]  So, it sounds like you're okay with that.
[3528.22 --> 3528.94]  Yeah, absolutely.
[3528.94 --> 3529.94]  I mean, you're...
[3529.94 --> 3531.16]  I think the reality of being...
[3531.16 --> 3540.24]  Of doing a startup a lot of times is you're gonna go through that ramen stage where you're, of course, not able to spend a lot of money because there's just not a lot of money there.
[3541.30 --> 3551.94]  We are hopefully, you know, fingers crossed in the next couple of weeks going to have a small angel round that'll obviously help quite a bit and help us, you know, potentially hire a third engineer to move even faster.
[3551.94 --> 3557.90]  So, potentially April, May timeframe, that'll happen whenever the incubation stage is over or is that...
[3557.90 --> 3558.18]  Yeah.
[3558.30 --> 3563.74]  So, we would raise around sometime early summer, late spring towards the end of this.
[3563.74 --> 3580.70]  And so, Jared, chime in here wherever you want, but I mean, as we've mentioned before this, we've got this growing trend of, you know, RethinkDB and, you know, we can name a number of others that have come on the show and talk about, you know, building an open source product, but also building a business alongside of that.
[3581.42 --> 3582.68]  Metabase rings a bell as well.
[3582.82 --> 3584.16]  That discussion we had there.
[3584.50 --> 3591.26]  It seems like databases are easy to get, you know, or not so much easy, but it seems like they're prime for this kind of...
[3591.26 --> 3591.52]  Infrastructure.
[3591.52 --> 3593.24]  Yeah, infrastructure, these tools.
[3593.74 --> 3597.38]  So, I guess that's just kind of an interesting take there.
[3597.40 --> 3601.64]  We're seeing, you know, this trend of companies building open source products.
[3601.90 --> 3604.86]  How does that span for you, I guess, moving forward?
[3605.00 --> 3610.86]  Like, what does that look like for, you know, what is, I guess, you're offering to anyone who would want to fund you?
[3610.92 --> 3612.90]  What is their get?
[3613.04 --> 3617.54]  You know, I don't know if you watch Shark Tank or not, but no one gives somebody money thinking they'll never get it back.
[3617.54 --> 3618.14]  Yeah.
[3619.02 --> 3619.34]  Yeah.
[3619.44 --> 3625.54]  And, you know, obviously for us as entrepreneurs and business people from that side, we're, you know, we're obviously doing this.
[3626.08 --> 3632.66]  Obviously, we want to build something cool and awesome that people can use, but also, you know, of course, you need to, you want to build a sustainable business as well.
[3632.66 --> 3646.10]  So, I think in general, I think, you know, if you think about, you know, going back to some of the things we talked about before with banks, moving a lot of their infrastructure from on-premise to the cloud, you know, starting to hit that way.
[3646.10 --> 3651.10]  That's starting to happen over the next, well, now a little bit, and particularly over the next three, five years.
[3652.04 --> 3655.82]  That's something that we can really help them with and accelerate that process.
[3657.28 --> 3669.80]  But even beyond that, you know, I think just in general with all the data breaches that have been happening and, you know, security becoming increasingly sort of top of mind, not only for business people, but for developers and technical people as well.
[3669.80 --> 3677.64]  I mean, you need to think about, you know, how you can build applications that aren't going to lose your customers' data and destroy your business.
[3678.78 --> 3680.52]  That was exactly what Jared and I were talking about.
[3680.58 --> 3684.90]  As I mentioned before every call, we have some sort of sync up, and Jared asked me, he's like, how did this hit your radar?
[3684.94 --> 3687.36]  And he wasn't asking in an argumentative way.
[3687.86 --> 3690.46]  He was like, you know, genuinely, you know, how did this hit your radar?
[3690.52 --> 3691.56]  What was interesting to you, Adam?
[3692.02 --> 3696.34]  And I was like, well, I mean, it hit nightly, so that was one thing, and that was our own radar.
[3696.34 --> 3710.92]  But then also I was thinking, like, over the last four or five years, and I'm sure it's happened lots more that, you know, lots more before those times, but it'd become more and more clear to me that we've had more and more, like, you know, cybercrime, so to speak.
[3711.08 --> 3719.52]  You know, where, you know, Sony was down for, you know, I mean, it's a shame I couldn't play my PlayStation for a month, but, you know, Sony was down, and that was a big one there.
[3719.52 --> 3725.22]  And then you've had lots of different, you know, compromises, so to speak.
[3725.42 --> 3736.08]  Yeah, targets, compromises, and next thing you know, credit card data, all this data, and then not only that, you know, they've got my password if that stuff's not encrypted right or whatever, I don't know.
[3736.16 --> 3738.68]  But then, you know, everyone's not secure at that point.
[3738.78 --> 3742.22]  So it made sense to have this conversation with you guys.
[3742.22 --> 3760.36]  I think over the last year, there happened maybe 13 or 14 big security compromises, and, yeah, that is something which just started popping up again and again, and that's increasingly a problem.
[3760.36 --> 3772.16]  Yeah, and I guess I think also, like, part of the bet of our company is if you look at sort of the last generation of big tech companies like Facebook, Twitter, LinkedIn, a lot of the value that they're creating is based off of their users' data.
[3772.72 --> 3773.98]  So they're monetizing that.
[3774.08 --> 3787.42]  But if you think about potentially what the next wave could look like, and actually, Lawrence Lessig had an interesting post I think a week or so ago about this topic is how companies are now starting to think of customer data actually as a liability.
[3787.42 --> 3790.36]  And not necessarily the source of value.
[3790.48 --> 3802.64]  So if you're, let's say, a financial services company or a new insurance startup, insurance tech startup, and you have data on your customers, that's a potential risk for your company.
[3802.78 --> 3808.52]  If you get hacked and you lose that, particularly when you're just starting to build trust with people, your business is basically dead.
[3808.52 --> 3824.36]  So if someone, you know, if people start to build on tool on top of things like zero DB and other other options, where they're not necessarily having to access that data directly, they remove that liability and that threat to their business.
[3825.64 --> 3826.44]  Well, let's talk about that.
[3826.52 --> 3830.10]  Let's talk about building on top of zero DB.
[3830.10 --> 3838.04]  After the break, our final break, by the way, we will talk to you guys about, let's just imagine we're going to build zero book.
[3838.20 --> 3847.94]  You know, we want to build a huge worldwide social network on top of zero DB technology, scale implications, performance implications, day-to-day management, those type of things.
[3847.94 --> 3850.12]  And then, of course, getting started is a bit of that as well.
[3850.46 --> 3854.54]  So I think that'd be a good place to take this conversation after we hear from this last sponsor.
[3854.70 --> 3855.72]  And then we'll be right back.
[3855.72 --> 3863.02]  Every Saturday morning, we ship out an email called Change Law Weekly that covers everything that hits our open source radar.
[3863.64 --> 3870.18]  It's our curated editorialized take on what you need to pay attention to from this week in open source and software development.
[3870.40 --> 3871.56]  There's no algorithms.
[3871.76 --> 3872.56]  There's no machines.
[3872.56 --> 3876.20]  It's just us paying attention to what we pay attention to.
[3876.32 --> 3880.52]  So you don't have to head to changelaw.com slash weekly to subscribe.
[3880.80 --> 3882.36]  And now back to the show.
[3885.72 --> 3897.06]  All right, we're back and we're ready to talk about using zero DB, practical applications, performance, scale, what have you, getting started.
[3897.06 --> 3902.28]  But let's start with performance because you guys do have some posts on your blog about performance.
[3902.52 --> 3912.10]  And anytime you add a layer to the conversation, which, you know, you're sending encrypted bits down the wire and decrypting them in the client, there are performance implications.
[3912.10 --> 3923.98]  So we'll just kind of lay that on the table and say, if I'm using zero DB versus some other DB, which is exactly like zero minus the encryption stuff, what penalty am I paying?
[3924.86 --> 3925.22]  Right.
[3925.22 --> 3939.48]  So basically, the biggest implication for us is that the way we work is the client talks to the server while doing the query more than once.
[3940.02 --> 3942.96]  So a typical database is sending a query to the server.
[3943.38 --> 3946.28]  The server is doing something and returning a result.
[3946.62 --> 3950.42]  In our case, the client talks to the server a little bit.
[3950.42 --> 3955.38]  So it sends a little bit, gets some information, decrypts it, sends something again.
[3955.38 --> 3957.78]  And that repeats several times.
[3958.34 --> 3964.58]  So what that comes down to is pretty much latency between client and server.
[3965.26 --> 3977.44]  It's you have for each query, you have a performance penalty of this, you know, multiple times this latency.
[3977.44 --> 3984.40]  What helps with that a little bit is client-side caching of the top of the index.
[3985.08 --> 3990.00]  And that makes queries faster by a factor of two about that.
[3992.08 --> 3997.12]  But I would say there is a positive thing as well.
[3997.12 --> 4012.34]  Now, since a lot of logic and encryption-decryption happening on the client, if you have some database server and multiple clients, each client decrypts its own data on its side.
[4012.84 --> 4019.30]  So you have this decryption load parallelized between multiple clients.
[4019.30 --> 4024.26]  And this kind of takes this load of the server.
[4024.40 --> 4031.64]  So in certain cases, you can have actually performance higher than in a typical situation.
[4033.02 --> 4043.68]  It seems like, and I guess this is the same for traditional databases, but a write-heavy application where a lot of clients are writing is going to be busting that client-side cache more often.
[4044.26 --> 4044.72]  Right.
[4044.72 --> 4046.94]  And require, you know, more round trips.
[4047.38 --> 4048.02]  That's true.
[4048.02 --> 4048.30]  Okay.
[4049.26 --> 4050.56]  So there is a penalty.
[4050.80 --> 4054.48]  Sometimes there's, you know, sometimes it's mitigated down to zero or negative.
[4054.76 --> 4059.06]  But something to definitely think about as a concern when going.
[4059.32 --> 4062.04]  And as it is with anything that you're going to adopt, there are trade-offs.
[4063.30 --> 4064.44]  What about scaling?
[4064.64 --> 4068.04]  So, you know, like I mentioned before the break, I'm building this thing.
[4068.10 --> 4068.90]  I don't know if you've ever heard of it.
[4068.96 --> 4069.76]  It's called ZeroBook.
[4070.28 --> 4071.58]  And it's going to be huge.
[4072.66 --> 4075.16]  I've just got my first 5 million users.
[4075.16 --> 4079.00]  I don't know who they are because all their data is encrypted, but I'm sure that they're awesome.
[4079.66 --> 4087.40]  And I'm trying to now expand my server-side infrastructure, my 0DB-based database infrastructure past one machine.
[4087.40 --> 4093.96]  I'm thinking of sharding or replicating or whatever it is these people do at Facebook.
[4095.02 --> 4096.16]  What do I got to do?
[4096.16 --> 4097.22]  Yeah.
[4097.34 --> 4106.02]  So basically replication and sharding, we inherit from ZODB or things built for that.
[4106.50 --> 4111.90]  Pretty much one is called ZRS, which is just replication.
[4112.62 --> 4119.06]  And there is a thing called NEO, which is actually already sharding.
[4119.06 --> 4124.98]  And actually using that, we can scale it up.
[4125.62 --> 4134.38]  So I guess for actually scaling the thing, you need all your data to reside on multiple servers.
[4134.62 --> 4141.80]  So when you get to the situation when all of your customers' data doesn't fit onto one server.
[4141.80 --> 4145.14]  And this is the...
[4145.14 --> 4149.16]  So for this, we can use these things I mentioned, which are already built.
[4149.94 --> 4158.72]  And they are integrating pretty well with 0DB just because we use this existing technology stack.
[4159.30 --> 4169.38]  But of course, there are some scalability thoughts about doing certain queries in end-to-end encrypted manner.
[4169.38 --> 4173.60]  So that is something we are constantly improving.
[4175.06 --> 4181.74]  Are there best practices that are coming about or things that you or your users are learning over time
[4181.74 --> 4185.52]  and kind of gathering together a corpus of knowledge about how to go about it?
[4186.68 --> 4190.36]  You mean about the performance and scalability?
[4191.06 --> 4192.96]  Yeah, just the scalability.
[4193.14 --> 4197.02]  But you said that there are things that you're learning about how to do the queries.
[4197.02 --> 4200.02]  Or is that all internal to the protocol and not to the person who's actually...
[4200.66 --> 4202.42]  Yeah, it is actually internal to the protocol.
[4202.58 --> 4207.04]  So I don't think at the moment developers should worry about that.
[4207.62 --> 4213.84]  If there is something they should worry about, that we will definitely publish that.
[4214.62 --> 4216.48]  And if there are some recommendations.
[4216.48 --> 4217.48]  Cool.
[4218.80 --> 4220.30]  How about the getting started stuff?
[4220.44 --> 4225.02]  So it seems like it's an easier onboard if I'm building a Python client.
[4225.40 --> 4227.30]  Something that can rely upon Python.
[4227.74 --> 4229.10]  So let's just start with that one.
[4229.66 --> 4232.22]  Let's say you sold me on the idea of 0DB.
[4232.38 --> 4233.98]  I'm ready to start coding up 0Book.
[4234.56 --> 4235.18]  How do I get started?
[4235.82 --> 4240.08]  Yeah, so we've got a little quick start tutorial on docs.0DB.io.
[4240.08 --> 4245.88]  And then you just grab 0DB-server from a GitHub repo.
[4246.64 --> 4250.66]  And it's pretty easy just to sort of get around, get started, and start playing with it.
[4251.16 --> 4253.98]  You can populate it with some sort of dummy data.
[4254.40 --> 4260.30]  And we give you an example of how to write your data models and how to query the database.
[4260.30 --> 4267.82]  So pretty easy to at least get a sample of it.
[4268.54 --> 4282.92]  Seeing this as kind of a brave new world of databases, I'm assuming that there's somewhat of a lack in terms of tooling around 0DB and query generators or any sort of thing like that.
[4282.92 --> 4287.52]  Is that an area where you guys are looking to innovate as a company, perhaps?
[4287.52 --> 4296.46]  Or is that something that you just completely open up to the open source community and hope that they would build these kinds of infrastructure around your infrastructure?
[4297.28 --> 4302.50]  Yeah, I mean, there's obviously things that we have in our roadmap for the company itself that we'll plan on doing.
[4302.50 --> 4307.44]  And then to the extent that other people do them first, that's great.
[4307.58 --> 4312.28]  We're happy to support people who are building stuff around 0DB and on top of 0DB.
[4312.66 --> 4316.70]  And even just in the couple weeks that it's been open source, we've seen some of that already.
[4317.34 --> 4323.56]  I know I think in the first week, maybe someone started playing around with Docker and put it into a container.
[4324.72 --> 4329.86]  I think a couple people have written plugins for various web frameworks.
[4329.86 --> 4332.02]  So we're seeing some of that already.
[4332.26 --> 4338.98]  And yeah, obviously, to the extent that that continues or increases, we're very happy to see any activity around 0DB.
[4341.32 --> 4345.54]  What do you say to the person who's not interested in Python at this point?
[4345.80 --> 4350.50]  When you guys still, you know, the JavaScript clients in the works, Python, the client is all that we have.
[4350.62 --> 4353.98]  But they're willing to get involved and actually, you know, do an implementation.
[4353.98 --> 4356.52]  Getting started for that person.
[4356.64 --> 4362.18]  Is the protocol documented or is it open up the Python client and start to, you know, emulate what you see there?
[4363.46 --> 4367.36]  What's the kind of process that you would imagine somebody go through to implement their own?
[4368.02 --> 4371.22]  You mean to implement their own client in a different language?
[4372.42 --> 4372.74]  Yes.
[4372.82 --> 4375.50]  And then also, just like that, you say, you know, it's not just a database.
[4375.58 --> 4376.26]  It's also a protocol.
[4376.50 --> 4380.12]  Is the protocol documented or like, is it out there?
[4380.12 --> 4382.04]  Or how, you know, do you just read the code?
[4382.92 --> 4383.24]  Yeah.
[4383.36 --> 4389.90]  So we're actually publishing a paper, hopefully, in the next week or so, maybe a little bit longer.
[4390.24 --> 4391.12]  Don't hold me to that.
[4391.42 --> 4393.98]  It'll have some more specifics.
[4393.98 --> 4399.18]  And we'll also have sort of more on our threat model and security assumptions as well.
[4399.26 --> 4404.10]  Some of the crypto primitives that we're using and potential sort of future optimization.
[4404.10 --> 4409.68]  So from understanding the protocol in more depth, that'll help quite a bit there.
[4410.12 --> 4419.10]  Actually, the protocol itself is derived from what was internal for ZODB.
[4419.10 --> 4441.36]  And we've talked to the founder of ZODB, Jim Fulton, who pretty much sees the future of ZODB as allowing alternative clients, which are non-Python, to work with that.
[4441.36 --> 4446.52]  So, and since we are based on that, we are pretty much in line with his vision.
[4446.84 --> 4456.66]  So I guess we can pretty much work together with people who work on ZODB to enable these alternative clients.
[4456.66 --> 4467.04]  I guess it's kind of been somewhat the ask here, but not directly, you know, talked about the protocol, you know, if somebody wanted to create their own client.
[4468.10 --> 4469.78]  You guys are in an incubator right now.
[4469.86 --> 4476.64]  You've obviously got the next, you know, three or four months kind of, to the most part, mapped out in terms of what some of your goals are.
[4476.64 --> 4484.80]  But if you had the ear of the open source community and they were thinking, similar to what Jared said earlier, hey, you know, I'm not digging Python, for example.
[4485.38 --> 4486.52]  I'm digging something else.
[4486.78 --> 4492.24]  Not so much just that, but how can the community step in and help you to move the ball along?
[4492.24 --> 4506.06]  If it's not, you know, your financial or your, not your financial goals, but your goals around your business, if it's not that, if it's around this technology and moving it forward, what are the best areas that the open source community can step in and help out?
[4507.00 --> 4511.18]  Yeah, so very much around building alternative clients, writing plugins.
[4511.80 --> 4518.70]  Another thing actually that helped a lot sort of in the first couple weeks after we open sourced it was just having people look at our implementation.
[4518.70 --> 4527.34]  And we had actually a lot of good feedback around things we could potentially do in the future to even make it even more secure.
[4527.76 --> 4531.34]  And, you know, one of the things that we do leak is access patterns.
[4531.68 --> 4538.86]  And what I mean by that is the server can observe obviously which encrypted buckets that are being queried.
[4539.12 --> 4546.98]  And in theory, over time, they could deduce, you know, things like the order of the database from those access patterns.
[4546.98 --> 4553.40]  And so one of the sort of active research areas right now is something called Oblivious RAM or ORAM.
[4553.88 --> 4558.58]  And that's designed to obfuscate these access patterns.
[4558.58 --> 4560.62]  And so that's something that we could potentially add in the future.
[4560.62 --> 4567.44]  So things like that, obviously, that help us sort of map out the roadmap for what 0DB will look like in the future.
[4567.44 --> 4569.28]  So that's helpful as well.
[4570.12 --> 4578.22]  So if someone's out there in their list, okay, well, I'm going to go to the org on GitHub, which is GitHub.com slash zero hyphen DB.
[4578.62 --> 4587.06]  Would it be okay for them to hop into the 0DB repo and just drop an issue there and share some ideas?
[4587.18 --> 4589.42]  Or is there different ways to communicate with you guys?
[4589.42 --> 4596.54]  Yeah, that's certainly an option where, you know, we're actively paying attention to GitHub and you can open a new issue there.
[4596.88 --> 4602.04]  We have a Slack channel, too, that we're on most of the time and can be very responsive there.
[4603.04 --> 4607.00]  I mean, we're pretty much online 24-7, so we're on Twitter, too.
[4607.08 --> 4608.92]  So it's pretty easy to get a hold of us.
[4609.32 --> 4609.50]  Gotcha.
[4609.66 --> 4612.92]  Is that Slack channel mentioned anywhere on 0DB.io?
[4613.34 --> 4615.28]  Oh, I guess it is right there, right there at the top.
[4615.32 --> 4615.80]  I missed it.
[4616.46 --> 4617.36]  It's too obvious.
[4617.36 --> 4618.04]  Yeah, we got it there.
[4618.04 --> 4619.34]  It's so obvious that I missed it.
[4619.40 --> 4620.40]  So you got a mailing list, too.
[4620.48 --> 4621.48]  So you're sending out emails.
[4621.98 --> 4624.16]  How often are you emailing people about what's going on?
[4624.50 --> 4626.80]  We don't email very often.
[4626.92 --> 4631.30]  I think we sent out two emails in the entire life of our mailing list.
[4632.06 --> 4636.38]  So one was, you know, a blog, like back, this was back in March.
[4636.38 --> 4638.08]  One was a follow-up blog post.
[4638.30 --> 4641.04]  We talked about a little bit in more detail how the protocol worked.
[4641.52 --> 4645.32]  And then the second was when we actually open-sourced it in December.
[4645.32 --> 4648.06]  So we're not going to spam you too much.
[4648.80 --> 4655.22]  Well, if you're heading to 0DB.io, you got to link to GitHub there, obviously, which is the org I just mentioned.
[4655.42 --> 4661.74]  It's the Slack channel to sign up to if you want to talk real-time or the mailing list and never get an email, or at least infrequently.
[4662.00 --> 4662.52]  That would be good.
[4663.44 --> 4664.20]  Just throw those cards for fun.
[4664.20 --> 4665.44]  We'll try to send you to important stuff.
[4665.68 --> 4665.88]  Yeah.
[4666.12 --> 4666.94]  Well, that's good, right?
[4666.94 --> 4668.84]  I mean, you didn't promise a weekly email.
[4670.32 --> 4672.10]  But email's really interesting.
[4672.64 --> 4675.88]  So, well, all right, fellas, we don't have many more questions for you.
[4675.92 --> 4677.72]  I know we wanted to talk quite a bit about that.
[4677.80 --> 4679.54]  We're running out of time for our show anyways.
[4679.74 --> 4681.48]  So we'll skip the closing questions.
[4681.88 --> 4682.76]  This is twice in a row.
[4682.82 --> 4686.28]  We did it with Yehuda, and now we're doing it here in this show to skip the closing questions.
[4686.28 --> 4687.74]  So maybe it's becoming a trend.
[4688.30 --> 4688.62]  Crazy.
[4688.82 --> 4689.24]  We're crazy.
[4689.44 --> 4689.84]  We'll see.
[4689.96 --> 4690.46]  I don't know.
[4691.12 --> 4702.36]  But, fellas, I want to thank you guys for taking the time to come on the show and obviously to think proactively about the future of technology and being able to, as you said earlier, McLean, to bet on this technology.
[4702.86 --> 4705.08]  One, to build a company around it, and two, to open source it.
[4706.30 --> 4717.42]  Obviously, you guys will have some financial gains in the future with what you do with it, but it's generous of you to give back so much to open source and trust the process of open source and all that good stuff.
[4717.56 --> 4718.82]  So that's really awesome.
[4718.82 --> 4725.32]  I want to thank our listeners for tuning in and also our members for tuning in to the show this week.
[4725.40 --> 4730.54]  Our sponsors for the episode this week are CodeShip, TopTowel, and DigitalOcean.
[4731.26 --> 4737.14]  And if you're not a member yet, you can join the community for just $20 a year, and we'll give you an all-access pass to everything we do.
[4737.28 --> 4741.58]  Head to changelog.com slash membership to hear more about that.
[4741.58 --> 4744.58]  Our next show is actually already recorded.
[4744.74 --> 4748.78]  It's already in the can, but it's episode 191 with Richard Feldman.
[4749.42 --> 4756.70]  He's from NoRedInc discussing Elm, which is described as the best of functional programming in your browser.
[4756.86 --> 4757.88]  Jared, that was an awesome show, right?
[4758.46 --> 4758.92]  Yeah, it was.
[4758.98 --> 4762.48]  And some awesome news came out of NoRedInc just last week.
[4762.58 --> 4763.32]  Was it this week?
[4763.62 --> 4765.94]  We had a post on it on the website.
[4766.90 --> 4768.06]  You had a conversation with him.
[4768.10 --> 4768.26]  Yeah.
[4768.26 --> 4769.76]  About what's going on there.
[4769.80 --> 4770.44]  You want to talk about that real quick?
[4770.90 --> 4772.30]  Well, they have it announced.
[4772.38 --> 4773.42]  We shared it on our blog.
[4773.72 --> 4783.46]  It's on SoundCloud as well, but we talked to Richard briefly about Evan Joplicki, which I'm not sure that's exactly how you say his last name, so forgive me if that's wrong.
[4783.82 --> 4786.42]  But he's joining NoRedInc, which is a really interesting thing.
[4786.92 --> 4794.26]  They are stepping up to support him, and he's coming out of the work, and he's creating the Elm Foundation, the Elm Software Foundation.
[4794.72 --> 4796.22]  Really interesting to see that happen in there.
[4796.22 --> 4799.18]  So check out the blog, changelog.com, to find that.
[4799.62 --> 4801.08]  There's an audio piece there as well.
[4801.18 --> 4804.32]  It's not in the main podcast feed, so if you're looking there, you're not going to find it there.
[4804.98 --> 4809.12]  But we mentioned both of our emails also in the show, so I'm going to mention that one more time.
[4809.24 --> 4810.84]  ChangeLog Weekly, we ship that every Saturday.
[4812.22 --> 4815.44]  It's our hand-curated editorial take on the week.
[4815.82 --> 4819.84]  And we also ship ChangeLog Nightly, which is our radar as well.
[4819.94 --> 4821.96]  So as you can see, we create new shows from this.
[4821.96 --> 4828.92]  We're constantly watching this, so we ship that every single night at 10 p.m. Central Standard Time, covering the daily trends in open source on GitHub.
[4829.70 --> 4835.80]  You can subscribe to both of those at changelog.com slash weekly and changelog.com slash nightly, respectively.
[4836.56 --> 4838.68]  But, fellas and everyone on the call, that's it.
[4838.80 --> 4840.70]  So let's say goodbye.
[4841.26 --> 4841.50]  Goodbye.
[4841.62 --> 4842.46]  Thanks for coming on, guys.
[4842.96 --> 4843.48]  Thanks, guys.
[4843.62 --> 4844.42]  That was a lot of fun.
[4845.02 --> 4845.30]  Bye.
[4845.30 --> 4845.38]  Bye.
[4845.38 --> 4845.44]  Bye.
[4845.44 --> 4845.48]  Bye.
[4845.48 --> 4845.52]  Bye.
[4845.52 --> 4845.58]  Bye.
[4845.58 --> 4845.60]  Bye.
[4845.60 --> 4845.62]  Bye.
[4845.62 --> 4845.66]  Bye.
[4845.66 --> 4847.58]  Bye.
[4847.58 --> 4847.62]  Bye.
[4847.62 --> 4849.62]  Bye.
[4849.62 --> 4849.66]  Bye.
[4849.66 --> 4849.70]  Bye.
[4849.70 --> 4849.74]  Bye.
[4851.96 --> 4863.68]  Bye.
[4863.72 --> 4874.74]  Bye.
[4878.86 --> 4879.44]  Bye.
[4881.56 --> 4881.68]  Bye.
[4881.68 --> 4881.86]  Bye.
