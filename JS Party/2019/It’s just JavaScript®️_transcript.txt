[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.96]  Check them out at Rollbar.com.
[10.18 --> 12.40]  And we're hosted on Linode cloud servers.
[12.74 --> 14.74]  Head to Linode.com slash Changelog.
[15.48 --> 18.54]  This episode is brought to you by our friends at Rollbar.
[18.66 --> 21.62]  Move fast and fix things like we do here at Changelog.
[21.62 --> 24.38]  Check them out at Rollbar.com slash Changelog.
[24.60 --> 26.96]  Resolve your errors in minutes and deploy with confidence.
[26.96 --> 30.14]  Catch your errors in your software before your users do.
[30.52 --> 33.16]  And if you're not using Rollbar yet or you haven't tried it yet,
[33.30 --> 36.78]  they want to give you $100 to donate to open source via Open Collective.
[36.88 --> 40.22]  And all you got to do is go to Rollbar.com slash Changelog, sign up,
[40.60 --> 41.84]  integrate Rollbar into your app.
[41.92 --> 45.92]  And once you do that, they'll give you $100 to donate to open source.
[46.30 --> 49.14]  Once again, Rollbar.com slash Changelog.
[56.96 --> 63.12]  Welcome to JS Party, a weekly celebration of JavaScript and the web.
[63.28 --> 69.74]  Tune in live on Thursdays at 1 p.m. Eastern, 10 a.m. Pacific at Changelog.com slash live.
[69.74 --> 74.84]  Join the community and Slack with us in real time during the show at Changelog.com slash community.
[75.30 --> 76.04]  Follow us on Twitter.
[76.14 --> 77.66]  We're at JSPartyFM.
[77.78 --> 79.14]  And now on to the show.
[79.14 --> 85.74]  Hello, party people, and welcome back.
[85.86 --> 88.06]  It's JSParty time once again.
[88.10 --> 91.20]  And we have an awesome panel, as we like to do every single week.
[91.86 --> 92.42]  I'm Jared.
[92.52 --> 92.96]  I'm here.
[93.06 --> 94.84]  I'm joined by three amazing people.
[95.00 --> 95.88]  Let's start with Divya.
[95.96 --> 97.56]  Welcome back to JSParty.
[97.94 --> 98.38]  Hello.
[98.84 --> 99.60]  Happy to be here.
[99.96 --> 100.88]  And that's not all.
[100.88 --> 101.78]  We got K-Ball.
[101.96 --> 102.52]  Ooh, that rhymed.
[102.84 --> 103.06]  Nice.
[103.42 --> 103.80]  Not all.
[103.92 --> 104.36]  That's K-Ball.
[104.42 --> 105.84]  K-Ball rhymes with all sorts of stuff.
[106.04 --> 107.52]  Hey, happy to be here.
[107.52 --> 110.58]  And last, but certainly not least, is Nick Neesey.
[110.64 --> 111.02]  What's up, Nick?
[111.42 --> 111.88]  Hoi, hoi.
[111.98 --> 112.52]  Hoi, hoi.
[112.56 --> 114.76]  Is that going to be your call signal from now on?
[114.88 --> 115.44]  Are you starting to think?
[115.54 --> 116.02]  I think so.
[116.32 --> 119.28]  That's what Mr. Burns, that's how Mr. Burns answers the phone.
[119.88 --> 120.66]  Hoi, hoi.
[122.10 --> 122.96]  I like it.
[122.98 --> 125.52]  I actually like it a lot better when you do it with that affectation.
[125.78 --> 129.30]  So I would suggest keeping it, but doing it just like that next time.
[130.00 --> 130.36]  Perfect.
[130.60 --> 134.34]  We should do a JS party where everyone adopts an accent.
[135.04 --> 135.50]  The whole thing.
[135.52 --> 136.12]  Oh, my goodness.
[136.12 --> 136.58]  That'd be hard.
[136.60 --> 137.26]  That would be terrible.
[137.26 --> 139.22]  Just to maintain that for 45 minutes.
[139.88 --> 141.38]  Well, we have awesome segments.
[141.54 --> 145.38]  As always, we're going to start off talking about really the biggest news in our space
[145.38 --> 149.80]  over the last couple of weeks, which is GitHub's announcement of their very own package registry.
[150.16 --> 153.46]  Then we're going to turn to some JavaScript trends.
[153.62 --> 159.20]  There's a nice post put out by the CV compiler folks all about what people are looking for in
[159.20 --> 163.28]  job skills and the trends that are happening there and the JavaScript land in 2019.
[163.28 --> 166.24]  And then finish off with one of our favorite segments, which is shout outs.
[167.10 --> 168.40]  So look forward to all that.
[168.40 --> 175.60]  Let's start off with GitHub, the source of all code, the host of most code and trying to
[175.60 --> 177.88]  be the host of many packages.
[177.88 --> 180.84]  So this was a big announcement that happened last week.
[180.84 --> 184.40]  And it happened kind of in a weird way, if you ask me, Friday afternoon.
[184.62 --> 185.90]  Yeah, exactly.
[186.26 --> 191.16]  I was I only heard about it because I was at a conference and then a fellow speaker was
[191.16 --> 192.90]  like, hey, did you hear about the announcement?
[193.56 --> 195.66]  And he only knew about it because he worked at Microsoft.
[195.66 --> 196.06]  Yeah.
[196.72 --> 203.72]  So, I mean, I'm not a PR person, but I know that a common tactic of PR people is when
[203.72 --> 207.56]  they want to bury a story like it has to come out, but they don't want it to make it a big
[207.56 --> 207.82]  deal.
[208.02 --> 211.76]  They will announce it or put out a press release on a Friday afternoon.
[211.76 --> 219.98]  And famously, back in, what was it, AntennaGate with Apple when Steve Jobs held that event
[219.98 --> 226.14]  on the campus and really wanted AntennaGate just to end back with the iPhone 4, maybe it
[226.14 --> 226.34]  was.
[227.04 --> 230.90]  They had this event on Friday afternoon and it was effective.
[231.08 --> 232.86]  So just the internet, just a strange thing.
[232.96 --> 234.00]  Maybe they're trying to fly under the radar.
[234.10 --> 239.36]  It's hard for GitHub to fly under our radar because, you know, we are so integrated.
[239.36 --> 243.36]  I mean, we not changelog, but we, the developer community.
[244.16 --> 247.20]  So maybe they just thought, hey, let's just do it now and people will find out.
[247.30 --> 250.88]  And maybe, I don't know, what do you guys think about the Friday afternoon live stream?
[251.74 --> 254.46]  I saw a tweet about it like two or three days before.
[254.70 --> 258.56]  And I thought it was very strange because usually I found out about new GitHub features
[258.56 --> 260.50]  like on the homepage, right?
[260.54 --> 264.94]  There'll just be like a little box that says, hey, and it links to their blog and has whatever
[264.94 --> 267.28]  the new feature is, you know, draft PRs or whatever.
[268.16 --> 269.34]  But I saw a tweet and I'm like,
[269.36 --> 273.56]  man, they never, they never pre-announce an announcement like this.
[273.56 --> 278.28]  So I was pretty excited to tune in and I watched the live stream and was excited about it.
[278.92 --> 280.98]  I was there long enough to get the gist of the announcement.
[281.20 --> 282.66]  And then, you know, it was Friday afternoon.
[282.78 --> 285.82]  I had other more relaxing things to be doing.
[285.94 --> 287.96]  So tell us about the stream itself, Nick.
[288.14 --> 290.20]  I know that Nat Friedman was up there.
[290.60 --> 291.56]  They brought up some demos.
[292.06 --> 294.20]  What was the overall feeling of that presentation?
[295.48 --> 296.38]  It looks pretty cool.
[296.38 --> 302.54]  They kept, they did the typical thing with like announcing new things where they're like,
[303.08 --> 308.70]  I can't remember the presenter's name, but he kept saying, you know, nothing up my sleeve
[308.70 --> 310.34]  or no tricks here.
[310.58 --> 314.70]  Like, you know, there's the trying to tell you that it's not magic.
[314.84 --> 317.22]  This is actually working and it's doing what we're saying.
[317.38 --> 317.60]  It's doing.
[317.72 --> 317.78]  This isn't paperwork.
[317.78 --> 318.22]  Yeah.
[319.06 --> 320.24]  Which I thought was kind of funny.
[320.76 --> 323.36]  That was the big takeaway I got from it other than the actual announcement.
[324.18 --> 327.44]  Were they overemphasizing that to the extent where you're like, hmm.
[327.90 --> 328.90]  Maybe this is paperwork.
[330.80 --> 333.08]  Maybe I caught on to that, but no, I don't think so.
[333.62 --> 338.36]  So the details of this you can find in the show notes, of course, you can just go to
[338.36 --> 342.86]  GitHub slash feature slash package dash registry if you want to read it for yourself.
[342.98 --> 345.88]  But it says your packages at home with their code.
[346.46 --> 350.54]  And it says with GitHub package registry, you can safely publish and consume packages
[350.54 --> 353.82]  within your organization or with the entire world.
[354.34 --> 360.28]  They have, I guess you'd call it a limited set or a starter set of supported ecosystems
[360.28 --> 365.80]  and language, NPM, Ruby Gems, Docker, Nougat, Maven.
[366.74 --> 367.80]  And I think that's it.
[367.84 --> 370.32]  There might be a couple of more, but that's at least what they're launching with.
[370.64 --> 373.40]  I was really surprised like Python wasn't on there.
[373.62 --> 374.02]  Yeah, really?
[374.24 --> 376.18]  Like Pip is in there or anything.
[376.36 --> 377.66]  And Python's a huge community.
[377.92 --> 379.24]  And I was like, where's Python?
[379.32 --> 379.48]  Yeah.
[379.52 --> 382.64]  Is that a disk or is that just a MVP, you know, try to get something out there?
[382.64 --> 382.96]  No idea.
[383.46 --> 383.78]  Yeah.
[384.30 --> 385.48]  It makes a lot of sense, right?
[385.52 --> 388.18]  I guess first impressions, maybe, Cable, you've been quiet so far.
[388.18 --> 392.78]  First impressions is just of the concept, okay, now GitHub is going to be a package registry.
[393.02 --> 397.30]  Whether it becomes, you know, the package registry for some of these ecosystems or not,
[397.36 --> 399.48]  I think that's still left to be found out.
[399.64 --> 403.32]  But just that they're moving into this space, what is your initial impressions?
[404.32 --> 404.54]  Yeah.
[404.70 --> 409.18]  So there's two areas of this that I think are super interesting,
[409.74 --> 414.86]  that where GitHub can really make a difference relative to the status quo.
[414.86 --> 422.44]  So one is, I think this makes it far easier to set up internal package registries,
[422.70 --> 425.02]  to share code inside of an organization.
[425.24 --> 429.22]  Because you don't have to figure out anything new.
[429.40 --> 432.86]  You don't have to set up your own server to manage it.
[432.90 --> 434.36]  You don't have to do any of that.
[434.70 --> 436.54]  You just use the tools you're already using.
[436.70 --> 439.72]  And you can make internal packages and set up an internal registry.
[439.72 --> 444.30]  So I think the organizational case for that is really interesting.
[445.82 --> 453.78]  The second piece that I think is a very interesting possibility that we'll see if we can get to,
[454.40 --> 462.00]  is this potentially allows for kind of end-to-end verification of,
[462.00 --> 465.58]  is the code that is in a repository that's visible to the world,
[466.44 --> 468.70]  you know, the code repository, the open source code,
[468.82 --> 472.76]  is that actually what is being used to generate the package?
[473.08 --> 476.14]  Because we ran into situations like the event stream hack,
[476.52 --> 478.60]  where there was discrepancy.
[479.30 --> 481.98]  You know, people were obfuscating what's visible to the world,
[482.14 --> 485.22]  or easily visible, versus what's actually getting pushed into the registry.
[485.34 --> 487.22]  And there's obviously some complications here.
[487.22 --> 490.58]  You know, nobody, almost nobody's shipping raw code.
[490.72 --> 492.46]  You're, you know, at least in the JavaScript world,
[492.52 --> 495.48]  you're probably transpiling it, you're bundling it, you're doing whatever.
[496.14 --> 499.70]  Though actually in things like Ruby and Python and other languages,
[499.70 --> 500.64]  that may be less true.
[502.32 --> 508.72]  But what this enables is at least the potential to do end-to-end validation of,
[508.94 --> 511.98]  is the code I'm looking at as an open source developer reviewing this,
[512.34 --> 514.08]  actually what's getting installed in my system?
[514.58 --> 515.58]  That's really interesting.
[515.58 --> 519.78]  And I think that that's the one main place where they could shine with this.
[520.16 --> 522.24]  I was trying to think of how they might do that.
[522.58 --> 526.50]  And this does work with GitHub Actions right out of the box.
[526.66 --> 530.20]  You can have an action that once you push to master,
[530.42 --> 533.14]  then take that and package it up or something.
[533.26 --> 537.28]  And maybe they could have some kind of badge system
[537.28 --> 541.42]  where if this package was deployed via this specific action,
[541.54 --> 542.72]  it gets this badge.
[542.76 --> 544.96]  And that's like your certified pipeline badge.
[544.96 --> 552.42]  So it's still up to the packages maybe at that point to set up that verification system
[552.42 --> 556.26]  because I'm not sure they could do it in kind of a global way.
[556.92 --> 561.62]  But at least then you know that it went through this automated system
[561.62 --> 564.70]  and not just somebody publishing straight from their desktop.
[564.70 --> 567.48]  So Chris in the chat asking the question,
[567.60 --> 569.00]  is this GitHub or is this Microsoft?
[569.24 --> 570.90]  And what he means, I think, by that is,
[571.42 --> 572.98]  and maybe we can't know,
[573.36 --> 576.82]  but product roadmaps take a long time and huge new.
[577.12 --> 579.44]  I mean, this is a whole other area of their business at this point.
[579.78 --> 584.60]  These things don't spike out in three weeks and then get released.
[584.60 --> 591.80]  And we know Microsoft has purchased GitHub, gosh, probably coming up on a year or 18 months.
[591.92 --> 592.94]  I can't remember the exact time frame.
[593.44 --> 598.30]  But the question is like, was this a thing that was already up and moving
[598.30 --> 601.56]  with the previous GitHub management, you know, with different leadership?
[602.16 --> 607.28]  Or is this a thing that Microsoft came in and said, you know, this is a next step?
[607.28 --> 609.06]  Because this is a huge next step for them branching out.
[609.62 --> 609.76]  Yeah.
[610.20 --> 614.84]  It's also really exciting because with this, it means that like,
[615.40 --> 617.18]  because a lot of the times with package registries,
[617.34 --> 620.42]  like if you think of NPM and RubyGems and so on,
[620.52 --> 622.42]  like it's really hard to find like,
[622.42 --> 625.80]  because there's the package registry and then there's where the code is posted.
[626.66 --> 628.84]  And a lot of the community is in GitHub.
[629.16 --> 632.12]  Like people submit issues, pull requests, like they see the code
[632.12 --> 639.44]  and you kind of gather in one place and not in like the actual like package management place.
[639.76 --> 639.80]  Right.
[640.02 --> 643.82]  And so with this, it's really nice because it seems like a centralized location
[643.82 --> 648.96]  where people can be like, oh, okay, I can easily discover packages in GitHub
[648.96 --> 653.46]  and I can like also see what are the open issues and things like that
[653.46 --> 656.32]  without having to toggle between like, oh, I'm on NPM.
[656.56 --> 659.66]  And then now I have to like go back to GitHub or like do the click,
[659.66 --> 662.98]  the weird click through, which is like, where's the GitHub link?
[662.98 --> 663.84]  The weird click through, yes.
[664.74 --> 667.56]  I always find myself like, I've done it so many times,
[667.62 --> 670.36]  but I'm always like the Git, where's the GitHub link?
[670.54 --> 670.84]  Yes.
[671.30 --> 674.62]  That's like all I do on NPM is just find the GitHub link and then go there.
[674.86 --> 675.14]  Right.
[676.14 --> 676.54]  Exactly.
[676.86 --> 678.98]  And it's really frustrating, but yeah.
[678.98 --> 682.28]  So hopefully this will be like much nicer, like a better workflow.
[683.26 --> 686.74]  And like you're saying, Nick, with the GitHub actions,
[686.86 --> 689.46]  I think that'll be really neat as well because I find like,
[689.66 --> 691.74]  in general, whenever I publish a package,
[691.74 --> 694.42]  I would have to like use like the NPM CLI.
[694.64 --> 697.34]  And then it's basically like two different things I'm doing.
[697.62 --> 701.04]  I'd be like push to GitHub and then from GitHub, I have to version it.
[701.14 --> 702.14]  And then I'd be like, okay,
[702.14 --> 705.78]  let me go publish it on NPM and then figure out what's happening.
[706.78 --> 707.18]  Yeah.
[707.26 --> 709.28]  And I've messed it up a couple of times.
[709.52 --> 711.72]  I'm like, wait, let me roll back, roll back.
[711.72 --> 716.86]  So I have a couple of questions on this that are perhaps less sunny.
[717.68 --> 720.40]  So one question is,
[721.04 --> 724.56]  one of the really nice things about some of the language specific registries
[724.56 --> 728.28]  right now is you don't have to ask about where do I load things from?
[728.40 --> 731.06]  Like I'm not much of a sysadmin person,
[731.06 --> 735.38]  but I know every time I have to muck with Linux and like Ubuntu or whatever,
[735.38 --> 738.40]  I'm like, shoot, where do I load these packages from?
[738.40 --> 740.24]  Some of them are in the default registry.
[740.38 --> 741.38]  Do I have to add registries?
[741.48 --> 742.12]  Do I have to do this?
[742.18 --> 742.90]  Do I have to do that?
[743.22 --> 751.30]  Like it's much more of a headache than with Python or Ruby or NPM or JavaScript
[751.30 --> 753.54]  where I'm just like, okay, there is one registry.
[753.96 --> 756.26]  I'm going to install from there and I'm good.
[757.26 --> 759.76]  So that's like one area where I'm wondering,
[759.76 --> 764.24]  is this like a step towards fragmentation in these language ecosystems?
[764.24 --> 765.16]  Yeah.
[766.28 --> 770.22]  And then the second one, which is almost the inverse problem is...
[770.22 --> 771.16]  Centralization, right?
[771.80 --> 772.56]  Centralization, right?
[772.56 --> 772.96]  I know.
[773.08 --> 773.78]  I was trying as well.
[774.42 --> 778.08]  I kind of like that NPM is a different company than GitHub,
[778.36 --> 782.14]  is a different company than wherever else,
[782.26 --> 784.36]  that there's GitLab and GitHub and whatever.
[784.36 --> 787.20]  Like if everything is going through GitHub, which is Microsoft,
[787.56 --> 790.84]  like are we continuing to consolidate power in our industry
[790.84 --> 792.86]  in those top four companies?
[792.86 --> 797.80]  And this is definitely the embrace and extend part of Microsoft's past history.
[797.80 --> 798.60]  The three-part strategy.
[798.92 --> 799.20]  Yeah.
[799.36 --> 799.54]  Yeah.
[800.00 --> 803.32]  It's such a weird dichotomy because you do have both concerns.
[803.32 --> 807.02]  You have a fragmentation concern and then you have a centralization concern.
[807.22 --> 808.24]  And I think they're both legitimate.
[808.84 --> 809.10]  You know?
[809.42 --> 813.06]  I could see both of them happening in certain ways
[813.06 --> 817.70]  and both of them affecting negatively both the already diverse ecosystems
[817.70 --> 822.80]  and then the kind of the convergent one ecosystem of GitHub.
[822.80 --> 825.00]  It's tough because like inside,
[825.16 --> 827.94]  but well, let's talk about it specifically inside the JavaScript land
[827.94 --> 828.92]  and the front end space.
[829.26 --> 830.76]  It's NPM is the only player in the game.
[830.92 --> 832.98]  I mean, you have other clients, you have the Yarn client.
[833.56 --> 835.42]  When it comes to registries, it is NPM.
[835.42 --> 843.54]  And that has both spurred a lot of flourishment in terms of packages,
[843.78 --> 845.62]  publishing and the ease of use and all that kind of stuff.
[845.96 --> 853.20]  But then could also be lacking competition on the actual hosting
[853.20 --> 854.84]  and the registry side of things.
[854.84 --> 860.66]  So in that regard, GitHub getting into this is basically can put a fire under NPM's butt
[860.66 --> 863.96]  and say, hey, we got features that you don't have
[863.96 --> 867.52]  or we can do things you don't have because we are the source code host as well.
[867.64 --> 869.00]  And so step up your game.
[869.12 --> 871.30]  And that could make everybody better.
[872.24 --> 874.66]  Just to confirm, do we think that this is directly competing
[874.66 --> 878.28]  with NPM's enterprise solutions?
[878.76 --> 879.98]  I assumed it wasn't.
[880.12 --> 882.62]  I just assumed it was like this.
[882.62 --> 886.04]  This was just like a way for making the workflow easier,
[886.28 --> 888.02]  but it wasn't necessarily a competition.
[888.60 --> 888.94]  I don't know.
[889.54 --> 892.88]  I would think it's direct competition myself.
[893.02 --> 894.52]  I mean, it's public or private.
[894.68 --> 898.68]  So I think there's definitely maybe not the on-premise stuff.
[900.10 --> 901.30]  Maybe. I don't know.
[901.54 --> 905.62]  But definitely in terms of where enterprises do their packages,
[906.00 --> 907.40]  I think it's a direct competition.
[908.10 --> 908.54]  I do too.
[908.54 --> 914.42]  Yeah. If we look at what is their pitch at NPM for the enterprise package,
[915.04 --> 920.36]  they have enterprise-grade JavaScript, whatever that means.
[920.96 --> 926.32]  But then they also say deduplicate development.
[926.74 --> 930.84]  So manage your internal stuff in the same way you manage your open source stuff.
[930.84 --> 935.64]  And then there's team management,
[936.10 --> 938.24]  which we also are already doing in GitHub.
[938.36 --> 940.56]  The only thing they have on here that I haven't seen super,
[940.84 --> 942.28]  or I'm not sure is definitely addressed,
[942.36 --> 945.04]  is this security expertise piece.
[945.84 --> 952.10]  But yeah, I think most of the value adds that NPM enterprise have
[952.10 --> 956.96]  are very much challenged by this.
[956.96 --> 960.20]  I just want to comment on that enterprise-grade JavaScript.
[960.40 --> 961.10]  It makes me think of,
[961.16 --> 963.64]  do you guys ever see the enterprise version of FizzBuzz
[963.64 --> 965.40]  that made the rounds a couple of years ago?
[965.86 --> 966.64]  So funny.
[967.20 --> 969.20]  It's like this Java class that does FizzBuzz,
[969.30 --> 970.78]  the programming quiz,
[971.42 --> 973.04]  in the most enterprise-y way possible.
[973.16 --> 974.64]  I'll try to find the code and put in the show notes.
[974.68 --> 975.40]  It's spectacular.
[975.60 --> 976.42]  But that's what I think of.
[976.48 --> 977.58]  Enterprise-grade JavaScript.
[977.72 --> 979.34]  It's like, are you writing the JavaScript for us?
[979.50 --> 981.64]  Or how's the enterprise-grade?
[981.80 --> 983.04]  Is my code magically better
[983.04 --> 985.52]  because I'm using you as an enterprise provider?
[985.52 --> 990.16]  I mean, there is also a sort of de-risking component here
[990.16 --> 991.64]  because I don't know if I'm,
[992.08 --> 993.74]  I'm probably not the only one who's watched
[993.74 --> 995.82]  like all the NPM-related drama on Twitter
[995.82 --> 997.32]  going down over the last few months.
[997.84 --> 998.48]  Oh, definitely.
[999.38 --> 1002.26]  But yeah, with that in the background there,
[1002.38 --> 1002.88]  there's like,
[1003.58 --> 1008.02]  hmm, I depend on this for an awful lot of stuff.
[1008.20 --> 1010.96]  Is this company going to be around in another three years?
[1011.70 --> 1013.80]  Can you summarize that without, you know,
[1014.00 --> 1014.96]  slamming anybody?
[1015.52 --> 1017.24]  Um, yes.
[1017.96 --> 1019.94]  So I'm not on the inside on this.
[1020.06 --> 1023.06]  I have no context over what is right or wrong.
[1023.66 --> 1025.84]  I know that there was one,
[1025.98 --> 1028.82]  some buzz around a set of people being laid off from NPM
[1028.82 --> 1032.88]  and that the assertion made,
[1032.98 --> 1034.06]  as I understand it,
[1034.08 --> 1036.50]  was that this was done very inelegantly
[1036.50 --> 1039.52]  and by a third party coming in
[1039.52 --> 1041.54]  rather than direct conversations with the executives.
[1041.54 --> 1043.64]  And that perhaps this was done to people
[1043.64 --> 1044.96]  who had just recently been hired.
[1045.50 --> 1047.88]  Um, so it was done in a way that left a lot of people
[1047.88 --> 1049.02]  with a bad taste in their mouth.
[1049.02 --> 1051.08]  Uh, following that,
[1051.08 --> 1055.70]  I have seen a number of high profile members of NPM
[1055.70 --> 1058.28]  saying that they are leaving NPM,
[1058.66 --> 1061.26]  often without saying too much more than that.
[1061.46 --> 1062.60]  Um, so I, you know,
[1062.60 --> 1064.82]  not weighing in on the drama and the this and the that.
[1065.24 --> 1066.14]  Um, but you know,
[1066.14 --> 1067.14]  I remember we did a,
[1067.50 --> 1069.12]  I don't remember if it was JS Party or Change Log,
[1069.18 --> 1069.92]  but there was one,
[1070.16 --> 1071.78]  an interview we did with like Jeff Lembeck
[1071.78 --> 1073.38]  about NPM is people.
[1073.62 --> 1073.90]  Yeah.
[1073.90 --> 1075.64]  Well, I saw on Twitter that Jeff is leaving NPM.
[1075.64 --> 1079.32]  And a number of other, uh, folks who have been
[1079.32 --> 1082.34]  at least very visible in the community
[1082.34 --> 1084.12]  representing NPM are,
[1084.30 --> 1086.52]  have announced publicly that they are leaving NPM.
[1086.68 --> 1089.66]  And so it makes me wonder like
[1089.66 --> 1091.60]  what's going on behind the scenes there.
[1091.68 --> 1093.92]  And running a company is bloody hard.
[1094.12 --> 1095.50]  And I don't want to,
[1095.66 --> 1096.58]  without knowing the background,
[1096.72 --> 1097.74]  I don't want to place judgment
[1097.74 --> 1098.90]  on one person or another,
[1098.90 --> 1100.30]  but it definitely seems like
[1100.30 --> 1102.08]  there is a lot of struggle
[1102.08 --> 1103.36]  happening there right now.
[1103.36 --> 1105.78]  Well, if they are in distress,
[1105.78 --> 1108.40]  this will crank up the stress for sure
[1108.40 --> 1110.20]  as they have now a heavyweight competitor.
[1111.10 --> 1113.56]  Um, I guess we'll talk about the state
[1113.56 --> 1114.84]  of the package registry right now.
[1114.92 --> 1115.66]  Sign up for the beta.
[1115.66 --> 1118.06]  So I guess similar to GitHub Actions,
[1118.22 --> 1119.02]  which is, I think,
[1119.12 --> 1120.12]  still sign up for the beta,
[1120.80 --> 1122.50]  um, which has been a long time,
[1122.54 --> 1122.88]  by the way,
[1122.96 --> 1125.18]  maybe showing some signs of,
[1125.18 --> 1127.10]  you know, big ships move slowly.
[1127.86 --> 1128.22]  Um,
[1128.92 --> 1129.56]  Google syndrome.
[1129.78 --> 1131.24]  How long was Gmail in beta?
[1131.40 --> 1132.14]  Like 12 years,
[1132.18 --> 1132.44]  wasn't it?
[1132.50 --> 1132.86]  Something like that.
[1133.36 --> 1134.66]  A couple of other interesting,
[1134.66 --> 1135.28]  uh,
[1135.68 --> 1136.80]  bits on this is that
[1136.80 --> 1139.14]  it does work within the,
[1139.14 --> 1141.12]  the APIs of the existing,
[1141.12 --> 1142.74]  like CLI apps that you would use.
[1142.78 --> 1143.18]  So you could,
[1143.26 --> 1144.84]  you would still use NPM or Yarn
[1144.84 --> 1145.96]  for this.
[1146.34 --> 1146.82]  Uh,
[1146.86 --> 1148.14]  and I assume the same thing
[1148.14 --> 1149.08]  for Docker and Maven
[1149.08 --> 1150.00]  and all of those.
[1150.00 --> 1151.26]  I was more just interested
[1151.26 --> 1152.76]  in the NPM side of it,
[1153.16 --> 1153.58]  obviously.
[1154.26 --> 1154.56]  Um,
[1154.74 --> 1156.34]  but then it also allows you
[1156.34 --> 1158.28]  to have public and private repos.
[1158.28 --> 1159.08]  And I think private
[1159.08 --> 1161.58]  is only for GitHub Pro.
[1161.58 --> 1162.90]  I think it's,
[1163.08 --> 1164.50]  I think it's free for all now.
[1164.56 --> 1165.98]  Like they changed that recently
[1165.98 --> 1167.50]  for repos.
[1167.58 --> 1168.22]  I was wondering about
[1168.22 --> 1169.30]  private packages.
[1169.92 --> 1170.44]  Um,
[1170.52 --> 1170.74]  yeah,
[1170.74 --> 1172.38]  actually it might be pro.
[1172.88 --> 1173.36]  Yeah.
[1173.90 --> 1174.92]  That would make sense
[1174.92 --> 1176.04]  why people go pro.
[1177.04 --> 1177.48]  Yeah.
[1177.88 --> 1178.84]  It was giving incentive
[1178.84 --> 1179.30]  to GoPro,
[1179.30 --> 1180.90]  but yeah,
[1180.90 --> 1181.08]  that,
[1181.14 --> 1181.52]  that's,
[1181.58 --> 1182.30]  that will be interesting.
[1182.30 --> 1183.08]  I think that that,
[1183.08 --> 1183.72]  uh,
[1183.72 --> 1184.60]  coupled with the,
[1184.72 --> 1185.56]  the things that you can
[1185.56 --> 1186.82]  potentially do
[1186.82 --> 1187.96]  with like actions
[1187.96 --> 1189.06]  or with like some kind
[1189.06 --> 1189.88]  of certified pipeline,
[1190.02 --> 1190.80]  uh,
[1190.82 --> 1191.64]  are the things that will
[1191.64 --> 1192.50]  make this stand out
[1192.50 --> 1193.88]  over just NPM
[1193.88 --> 1195.28]  or Ruby gems
[1195.28 --> 1196.12]  or whatever the other,
[1196.12 --> 1197.02]  uh,
[1197.32 --> 1198.24]  package managers are.
[1198.78 --> 1199.26]  Yeah.
[1199.28 --> 1200.74]  Also like totally separately,
[1200.74 --> 1202.36]  but like I found it
[1202.36 --> 1202.92]  really interesting
[1202.92 --> 1203.58]  because when GitHub
[1203.58 --> 1204.14]  announced,
[1204.14 --> 1205.06]  um,
[1205.38 --> 1206.46]  their new registry,
[1206.70 --> 1207.08]  GitLab,
[1207.32 --> 1208.16]  released an article
[1208.16 --> 1208.80]  saying like,
[1208.86 --> 1209.00]  Hey,
[1209.02 --> 1210.08]  we did this before
[1210.08 --> 1210.76]  everyone.
[1210.76 --> 1211.20]  Um,
[1213.84 --> 1214.50]  and it was just like
[1214.50 --> 1215.54]  an article saying like
[1215.54 --> 1216.54]  they did this back
[1216.54 --> 1217.66]  in like 2016
[1217.66 --> 1218.40]  or something.
[1219.14 --> 1219.58]  Um,
[1220.16 --> 1221.10]  and yeah,
[1221.34 --> 1222.52]  I was like,
[1222.62 --> 1222.82]  okay,
[1222.82 --> 1223.18]  cool.
[1223.42 --> 1225.14]  Like nice flex GitLab.
[1225.88 --> 1227.82]  I really want to like GitLab
[1227.82 --> 1229.06]  and every time that I've
[1229.06 --> 1229.82]  tried their UI,
[1230.00 --> 1230.20]  I'm like,
[1230.26 --> 1231.24]  this is so much worse
[1231.24 --> 1232.00]  than GitHub.
[1232.32 --> 1232.58]  They're just,
[1232.70 --> 1233.78]  the focus on
[1233.78 --> 1235.40]  design interaction
[1235.40 --> 1236.56]  and UI isn't there.
[1237.14 --> 1238.30]  And that,
[1238.66 --> 1239.66]  I think they're doing
[1239.66 --> 1240.52]  some really innovative
[1240.52 --> 1241.00]  things.
[1241.00 --> 1241.68]  And I think they've done
[1241.68 --> 1242.36]  some great stuff
[1242.36 --> 1243.06]  for supporting the
[1243.06 --> 1243.82]  open source community
[1243.82 --> 1244.48]  and supporting,
[1244.48 --> 1244.88]  um,
[1244.88 --> 1245.60]  the Vue community,
[1245.60 --> 1246.28]  which I love.
[1246.70 --> 1247.02]  Um,
[1247.18 --> 1248.00]  but the,
[1248.14 --> 1250.44]  their product to me
[1250.44 --> 1251.86]  as a developer
[1251.86 --> 1253.56]  is pretty inferior
[1253.56 --> 1255.16]  relative to GitHub.
[1255.90 --> 1256.92]  GitLab might become
[1256.92 --> 1257.68]  the new dojo.
[1257.82 --> 1258.66]  Wasn't dojo the,
[1259.02 --> 1259.98]  dojo already did that.
[1261.08 --> 1262.02]  I was going to make
[1262.02 --> 1262.56]  that joke.
[1262.92 --> 1263.54]  Teach it to it.
[1264.20 --> 1264.64]  Okay.
[1264.74 --> 1265.94]  Final thoughts on GitHub.
[1266.08 --> 1266.82]  A lot of this I think
[1266.82 --> 1268.00]  is kind of wait and see,
[1268.00 --> 1268.92]  um,
[1268.96 --> 1269.22]  our,
[1269.28 --> 1270.42]  our prognostications
[1270.42 --> 1271.30]  of what might happen,
[1271.36 --> 1271.48]  you know,
[1271.48 --> 1272.00]  our fears,
[1272.12 --> 1272.60]  our desires.
[1272.86 --> 1273.72]  It's compelling.
[1274.30 --> 1275.08]  Integrated products
[1275.08 --> 1275.48]  are compelling.
[1276.08 --> 1276.72]  I think there's an
[1276.72 --> 1278.92]  ideological tug of war
[1278.92 --> 1279.54]  here because,
[1279.74 --> 1279.90]  you know,
[1280.14 --> 1280.98]  Git is distributed
[1280.98 --> 1281.80]  version control
[1281.80 --> 1283.00]  and we've moved
[1283.00 --> 1284.22]  a lot of our stuff
[1284.22 --> 1285.00]  to one centralized,
[1285.14 --> 1285.68]  you know,
[1285.74 --> 1286.62]  for-profit company
[1286.62 --> 1287.52]  and now here's
[1287.52 --> 1288.28]  a whole nother area
[1288.28 --> 1288.92]  which was on a
[1288.92 --> 1290.04]  different for-profit
[1290.04 --> 1290.44]  company.
[1291.18 --> 1292.10]  And now it's like,
[1292.18 --> 1292.38]  well,
[1292.44 --> 1293.18]  maybe everything's,
[1293.32 --> 1294.50]  maybe GitHub will be
[1294.50 --> 1295.50]  decentralized
[1295.50 --> 1297.62]  platform and,
[1297.62 --> 1298.08]  uh,
[1298.08 --> 1298.26]  that,
[1298.26 --> 1299.32]  that usually ends up
[1299.32 --> 1299.58]  bad.
[1299.88 --> 1301.02]  I think over time
[1301.02 --> 1301.96]  it's just like Microsoft
[1301.96 --> 1302.86]  will start owning
[1302.86 --> 1303.32]  everything.
[1303.44 --> 1303.58]  Like,
[1303.72 --> 1303.82]  I,
[1304.00 --> 1305.06]  we use VS Code
[1305.06 --> 1306.66]  and we use GitHub
[1306.66 --> 1308.48]  and now we'll like,
[1308.52 --> 1309.60]  use their registry.
[1310.06 --> 1310.44]  Right.
[1310.44 --> 1311.20]  They'll just own like,
[1311.26 --> 1312.90]  every step of the process.
[1313.56 --> 1314.00]  Well,
[1314.08 --> 1314.82]  and what's interesting,
[1315.38 --> 1315.66]  so,
[1316.22 --> 1316.46]  you know,
[1316.46 --> 1316.86]  there's,
[1317.02 --> 1318.30]  there's like,
[1318.52 --> 1319.82]  four-ish
[1319.82 --> 1321.04]  companies
[1321.04 --> 1322.36]  who are dominating
[1322.36 --> 1323.34]  the industry right now.
[1323.56 --> 1323.66]  Right.
[1323.68 --> 1324.20]  You have Microsoft,
[1324.52 --> 1325.06]  you have Google,
[1325.40 --> 1326.00]  you have Facebook,
[1326.24 --> 1326.76]  you have Apple.
[1327.48 --> 1328.32]  Did I miss any?
[1328.84 --> 1329.46]  And I think that's
[1329.46 --> 1331.40]  pretty much it.
[1331.42 --> 1332.04]  Did you say Amazon?
[1332.88 --> 1333.28]  Oh,
[1333.34 --> 1333.58]  Amazon.
[1333.76 --> 1334.02]  You're right.
[1334.12 --> 1334.98]  100% Amazon.
[1335.64 --> 1335.98]  Um,
[1336.38 --> 1338.22]  of those,
[1338.74 --> 1341.12]  only one
[1341.12 --> 1342.08]  seems to have a bad
[1342.08 --> 1342.94]  reputation among
[1342.94 --> 1343.52]  developers.
[1344.52 --> 1344.84]  Facebook.
[1345.36 --> 1345.66]  That's true.
[1345.66 --> 1345.88]  Everybody,
[1346.10 --> 1346.34]  like,
[1346.82 --> 1347.74]  folks are
[1347.74 --> 1349.92]  kind of jumping
[1349.92 --> 1350.70]  on the bandwagon
[1350.70 --> 1351.24]  of what,
[1351.50 --> 1351.72]  oh,
[1352.14 --> 1353.38]  AWS is so awesome,
[1353.48 --> 1354.18]  all these great things.
[1354.28 --> 1355.26]  Microsoft is so awesome,
[1355.32 --> 1355.90]  all these things to do.
[1356.04 --> 1357.06]  And they are awesome.
[1357.18 --> 1357.30]  Like,
[1357.34 --> 1358.30]  they're doing a great job
[1358.30 --> 1359.12]  of their building
[1359.12 --> 1359.96]  great things.
[1360.56 --> 1361.58]  And we're letting them
[1361.58 --> 1362.56]  continue to consolidate
[1362.56 --> 1363.08]  power.
[1363.50 --> 1363.70]  Yeah.
[1364.00 --> 1365.10]  And consolidate,
[1366.06 --> 1366.26]  you know,
[1366.26 --> 1366.94]  as you say,
[1367.00 --> 1367.18]  Divya,
[1367.26 --> 1368.44]  eventually all of our
[1368.44 --> 1369.24]  stuff on this end
[1369.24 --> 1369.74]  will be,
[1369.74 --> 1370.32]  you know,
[1370.50 --> 1371.60]  using Microsoft products
[1371.60 --> 1372.20]  and we'll be hosting
[1372.20 --> 1373.30]  everything on AWS
[1373.30 --> 1373.90]  and blah,
[1373.90 --> 1374.00]  blah,
[1374.00 --> 1374.14]  blah,
[1374.18 --> 1374.28]  blah,
[1374.28 --> 1374.44]  blah.
[1374.48 --> 1374.88]  And if you're not
[1374.88 --> 1375.84]  hosting on AWS,
[1376.08 --> 1376.88]  you're hosting on Azure
[1376.88 --> 1378.02]  or you're hosting on
[1378.02 --> 1378.88]  Google Cloud.
[1379.10 --> 1380.36]  And it's kind of like,
[1380.70 --> 1381.72]  that's,
[1381.72 --> 1384.18]  that's a very fragile
[1384.18 --> 1385.32]  world to live in.
[1385.54 --> 1386.78]  And it's one where
[1386.78 --> 1389.50]  individuals have
[1389.50 --> 1390.90]  given up a whole
[1390.90 --> 1391.74]  lot of power.
[1391.74 --> 1392.46]  Mm-hmm.
[1392.98 --> 1393.96]  Two last points
[1393.96 --> 1394.74]  that that makes me think of.
[1394.78 --> 1395.50]  The first one is that
[1395.50 --> 1395.98]  Microsoft,
[1396.28 --> 1397.08]  and you just named
[1397.08 --> 1398.18]  Microsoft and said that,
[1398.34 --> 1398.56]  you know,
[1398.60 --> 1399.46]  only one has a bad
[1399.46 --> 1400.64]  reputation with developers
[1400.64 --> 1401.44]  and that it wasn't
[1401.44 --> 1401.78]  Microsoft,
[1401.92 --> 1402.34]  it was Facebook.
[1402.56 --> 1403.38]  And it's true.
[1403.88 --> 1404.82]  Microsoft has been
[1404.82 --> 1405.82]  on a very intentional,
[1406.36 --> 1406.92]  I don't know,
[1406.92 --> 1407.48]  six-year,
[1407.60 --> 1409.44]  five-year process
[1409.44 --> 1410.66]  of mending their
[1410.66 --> 1411.66]  relationship with the
[1411.66 --> 1412.46]  software developers
[1412.46 --> 1413.26]  that are not,
[1414.00 --> 1414.20]  you know,
[1414.24 --> 1415.26]  weren't always inside
[1415.26 --> 1416.02]  of the Microsoft
[1416.02 --> 1417.10]  Windows camp.
[1417.52 --> 1418.14]  And they've done a
[1418.14 --> 1419.06]  heck of a job at it.
[1419.60 --> 1421.98]  And it's evidenced by
[1421.98 --> 1424.38]  everybody using VS Code,
[1424.46 --> 1425.04]  like Divya's saying,
[1425.12 --> 1425.70]  everybody's,
[1425.70 --> 1426.24]  you know,
[1426.24 --> 1427.26]  using GitHub and
[1427.26 --> 1427.94]  loving GitHub and
[1427.94 --> 1428.80]  Microsoft owns that
[1428.80 --> 1429.42]  and it hasn't been
[1429.42 --> 1430.36]  bad for us yet.
[1430.36 --> 1431.96]  So,
[1432.16 --> 1433.14]  it's just interesting
[1433.14 --> 1433.88]  how successful they've
[1433.88 --> 1434.52]  been at changing
[1434.52 --> 1435.12]  their reputation
[1435.12 --> 1436.60]  because public opinion
[1436.60 --> 1437.26]  is a very hard thing
[1437.26 --> 1437.62]  to sway.
[1438.30 --> 1439.24]  The second thought I had
[1439.24 --> 1439.98]  is there's an adage
[1439.98 --> 1442.30]  mostly about robotics
[1442.30 --> 1442.92]  and automation
[1442.92 --> 1445.24]  and AI and whatnot
[1445.24 --> 1446.66]  about Amazon,
[1447.22 --> 1447.88]  which is,
[1447.94 --> 1448.08]  you know,
[1448.08 --> 1448.98]  in the next 10 years,
[1449.12 --> 1450.26]  Amazon is either going
[1450.26 --> 1452.62]  to hire you,
[1452.74 --> 1453.30]  like you'll be either
[1453.30 --> 1454.00]  working for Amazon
[1454.00 --> 1455.56]  or they will put you
[1455.56 --> 1456.44]  completely out of business.
[1456.70 --> 1457.30]  Like that's kind of
[1457.30 --> 1458.20]  the path that Amazon
[1458.20 --> 1458.66]  is on,
[1458.66 --> 1460.92]  just in the more
[1460.92 --> 1461.76]  mainstream space.
[1462.54 --> 1462.76]  And so,
[1462.86 --> 1463.52]  in a lot of ways,
[1463.60 --> 1465.38]  maybe in the software space,
[1465.70 --> 1467.20]  set aside AWS,
[1467.70 --> 1468.40]  Microsoft might be
[1468.40 --> 1469.04]  on that path
[1469.04 --> 1470.68]  where they might be
[1470.68 --> 1471.14]  the player
[1471.14 --> 1471.78]  when it comes to
[1471.78 --> 1472.40]  developer tools
[1472.40 --> 1473.60]  over the next 5,
[1473.64 --> 1474.00]  10 years.
[1475.06 --> 1475.24]  Yeah,
[1475.40 --> 1476.16]  but it's,
[1476.70 --> 1477.66]  I have not,
[1478.04 --> 1479.10]  I think it's only
[1479.10 --> 1480.60]  in the recent few years
[1480.60 --> 1481.42]  where I've heard people
[1481.42 --> 1482.44]  say they would want
[1482.44 --> 1483.56]  to work for Microsoft.
[1484.62 --> 1484.98]  Yeah.
[1485.48 --> 1486.82]  I have not heard that
[1486.82 --> 1488.08]  in a really long time.
[1488.66 --> 1489.34]  And now,
[1489.58 --> 1491.34]  there are lots of developers,
[1491.58 --> 1493.00]  like very talented developers,
[1493.72 --> 1494.88]  or who are like,
[1495.08 --> 1495.28]  you know,
[1495.30 --> 1496.80]  if Microsoft gave me a job,
[1496.84 --> 1497.50]  I would take it.
[1497.90 --> 1498.24]  Right.
[1498.46 --> 1499.16]  And so,
[1499.22 --> 1500.48]  that's like a huge shift.
[1500.96 --> 1501.02]  Like,
[1501.12 --> 1502.26]  and that probably like
[1502.26 --> 1503.54]  moves us to the next segment
[1503.54 --> 1505.24]  on like job skills stuff.
[1505.74 --> 1506.64]  We can talk about that later,
[1506.64 --> 1508.80]  but it's just an interesting way
[1508.80 --> 1510.54]  of like how they position themselves.
[1510.54 --> 1511.68]  So,
[1511.76 --> 1512.86]  in the developer community,
[1513.06 --> 1515.64]  they're seen quite well now.
[1516.38 --> 1517.28]  And they've like,
[1517.42 --> 1518.68]  they've obviously done a good job.
[1518.94 --> 1518.96]  So,
[1519.16 --> 1519.34]  yeah.
[1519.86 --> 1520.16]  Just,
[1520.28 --> 1521.14]  just to close it,
[1521.28 --> 1521.64]  there's,
[1521.76 --> 1522.92]  there's a Twitter account,
[1523.14 --> 1524.12]  NPM parody,
[1524.12 --> 1525.62]  that speculates on what NPM
[1525.62 --> 1526.64]  might actually stand for.
[1526.84 --> 1527.02]  And,
[1527.58 --> 1527.86]  uh,
[1528.14 --> 1528.92]  I saw a tweet from them,
[1528.98 --> 1530.20]  nobody predicted Microsoft.
[1530.20 --> 1533.98]  I believe that NPM account
[1533.98 --> 1535.20]  was created
[1535.20 --> 1537.18]  specifically
[1537.18 --> 1539.58]  when the package manager
[1539.58 --> 1540.16]  was announced.
[1540.46 --> 1540.92]  Oh,
[1540.96 --> 1541.20]  really?
[1541.58 --> 1542.44]  All of their tweets
[1542.44 --> 1543.20]  are May 10th.
[1544.36 --> 1544.58]  Oh,
[1544.70 --> 1545.00]  weird.
[1545.00 --> 1545.26]  Could this be?
[1545.84 --> 1546.36]  Conspiracy.
[1546.78 --> 1547.90]  The new Horse.js.
[1548.82 --> 1550.42]  Horse.js has longevity.
[1551.34 --> 1553.06]  They first tweeted May 10th,
[1553.12 --> 1554.28]  they last tweeted May 10th.
[1554.30 --> 1554.48]  Oh,
[1554.52 --> 1555.66]  it's a one and done kind of thing.
[1556.16 --> 1556.52]  This is,
[1556.60 --> 1557.42]  this is a,
[1557.42 --> 1558.96]  a one hit wonder Twitter account.
[1560.20 --> 1568.72]  This episode is brought to you by Linode,
[1568.82 --> 1569.98]  our cloud server of choice.
[1569.98 --> 1571.06]  And we're excited to share
[1571.06 --> 1571.90]  they've recently launched
[1571.90 --> 1573.24]  dedicated CPU instances.
[1573.88 --> 1574.92]  If you have build boxes,
[1575.20 --> 1575.52]  CI,
[1575.62 --> 1575.88]  CD,
[1576.22 --> 1576.88]  video encoding,
[1577.28 --> 1578.08]  machine learning,
[1578.26 --> 1579.04]  game servers,
[1579.28 --> 1579.88]  databases,
[1580.46 --> 1581.22]  data mining,
[1581.34 --> 1582.82]  or application servers
[1582.82 --> 1584.10]  that need to be full duty,
[1584.48 --> 1586.36]  100% CPU all day,
[1586.48 --> 1587.14]  every day,
[1587.36 --> 1588.56]  then check out Linode's
[1588.56 --> 1590.10]  dedicated CPU instances.
[1590.20 --> 1593.14]  These instances are fully dedicated
[1593.14 --> 1594.80]  and shared with no one else.
[1594.88 --> 1596.18]  There's no CPU steal
[1596.18 --> 1597.84]  or competing for these resources
[1597.84 --> 1598.80]  with other Linodes.
[1599.06 --> 1600.78]  Pricing is very competitive
[1600.78 --> 1602.76]  and starts out at 30 bucks a month.
[1603.10 --> 1604.76]  Learn more and get started
[1604.76 --> 1606.94]  at linode.com slash changelog.
[1607.06 --> 1607.50]  Again,
[1607.64 --> 1609.16]  linode.com slash changelog.
[1609.16 --> 1621.08]  All right,
[1621.12 --> 1621.66]  next up,
[1621.70 --> 1622.86]  we turn our focus
[1622.86 --> 1624.74]  to JavaScript trends.
[1625.10 --> 1627.26]  The fine folks at CV compiler
[1627.26 --> 1629.38]  have a interesting research
[1629.38 --> 1629.98]  and analysis.
[1630.12 --> 1630.40]  They did,
[1630.48 --> 1631.64]  they call it game of frameworks,
[1632.52 --> 1634.08]  JavaScript trends of 2019,
[1634.28 --> 1635.92]  wherein they went out
[1635.92 --> 1636.74]  and surveyed,
[1636.78 --> 1637.74]  I think it was 300
[1637.74 --> 1639.50]  different job postings
[1639.50 --> 1640.68]  in April
[1640.68 --> 1641.86]  from around
[1641.86 --> 1642.78]  AngelList,
[1642.92 --> 1643.60]  Stack Overflow,
[1643.74 --> 1644.02]  LinkedIn,
[1644.28 --> 1644.72]  et cetera.
[1645.62 --> 1647.30]  And they compiled them down
[1647.30 --> 1647.80]  to find out
[1647.80 --> 1649.04]  what companies
[1649.04 --> 1649.92]  are posting about,
[1650.02 --> 1651.18]  which skills specifically
[1651.18 --> 1653.06]  inside the JavaScript space
[1653.06 --> 1655.28]  companies are looking for.
[1655.40 --> 1656.12]  And they produced
[1656.12 --> 1657.08]  a nice chart.
[1658.08 --> 1658.98]  We will link all that
[1658.98 --> 1659.42]  in the show notes
[1659.42 --> 1660.24]  if you want to look at that chart.
[1660.46 --> 1661.06]  I'll tell you right now
[1661.06 --> 1662.56]  that React is numero uno.
[1663.44 --> 1664.80]  So it wins the game of frameworks,
[1664.90 --> 1665.12]  I guess,
[1665.18 --> 1665.50]  even though,
[1665.68 --> 1666.30]  is it a framework?
[1666.64 --> 1667.32]  I don't think it's a framework.
[1667.90 --> 1668.62]  That being said,
[1668.96 --> 1669.94]  how do we define these things?
[1670.02 --> 1670.86]  No JS is on there,
[1670.94 --> 1673.06]  so is it a framework?
[1673.88 --> 1674.40]  I think it's just,
[1674.76 --> 1675.50]  Git is on there.
[1675.64 --> 1676.08]  Is Git a framework?
[1676.58 --> 1676.78]  Yeah,
[1676.84 --> 1677.96]  I think they called it skills.
[1677.96 --> 1678.24]  This is skills,
[1678.38 --> 1678.80]  not frameworks.
[1678.98 --> 1679.32]  I know,
[1679.42 --> 1680.20]  but it was called
[1680.20 --> 1681.28]  Game of Frameworks.
[1681.42 --> 1682.64]  I know it's a Game of Thrones reference,
[1682.80 --> 1683.16]  but it's like,
[1683.22 --> 1683.84]  where are the frameworks?
[1684.40 --> 1684.70]  Anyways,
[1685.06 --> 1685.48]  I'm nitpicking this for it.
[1685.48 --> 1686.20]  Not a good reference.
[1686.20 --> 1686.52]  Yeah,
[1687.08 --> 1687.80]  trying too hard.
[1688.42 --> 1689.30]  The thing that immediately
[1689.30 --> 1691.16]  stuck out to me
[1691.16 --> 1692.52]  was number seven,
[1692.80 --> 1693.04]  Java.
[1693.78 --> 1695.26]  And I'm immediately thinking,
[1695.46 --> 1696.12]  of this,
[1696.20 --> 1697.32]  is it just people spelling it
[1697.32 --> 1698.56]  Java space script?
[1698.84 --> 1699.06]  Oh.
[1700.70 --> 1701.98]  Do people not realize
[1701.98 --> 1703.12]  that Java and JavaScript
[1703.12 --> 1704.06]  are different things?
[1704.24 --> 1704.46]  Like,
[1704.90 --> 1705.62]  those are the two things
[1705.62 --> 1706.60]  that I immediately thought of.
[1706.60 --> 1707.78]  That might be a legit
[1707.78 --> 1709.06]  situation
[1709.06 --> 1709.60]  if they're just,
[1709.66 --> 1709.88]  you know,
[1709.94 --> 1710.74]  going out and
[1710.74 --> 1712.32]  regexing a bunch of
[1712.32 --> 1713.20]  job postings,
[1713.32 --> 1713.54]  you know,
[1713.54 --> 1714.78]  and somebody put a space between.
[1714.78 --> 1715.80]  I mean,
[1715.80 --> 1716.40]  I had to follow up
[1716.40 --> 1716.80]  and ask them on that.
[1716.80 --> 1717.06]  Luckily,
[1717.24 --> 1718.38]  script is not number eight.
[1721.44 --> 1723.38]  We need scripting skills,
[1724.00 --> 1724.78]  nunchuck skills.
[1725.40 --> 1726.84]  You also see things on there
[1726.84 --> 1727.88]  like SQL
[1727.88 --> 1728.66]  and Python
[1728.66 --> 1729.16]  and stuff.
[1729.22 --> 1729.62]  So I think
[1729.62 --> 1730.72]  one of the things
[1730.72 --> 1731.24]  that that
[1731.24 --> 1732.30]  draws to my notice
[1732.30 --> 1732.72]  is like,
[1732.82 --> 1734.00]  folks don't want someone
[1734.00 --> 1734.60]  necessarily
[1734.60 --> 1735.56]  who's only
[1735.56 --> 1736.70]  paying attention
[1736.70 --> 1737.24]  to JavaScript.
[1737.68 --> 1738.88]  You need to understand
[1738.88 --> 1739.64]  some of the back-end
[1739.64 --> 1740.16]  technologies
[1740.16 --> 1740.84]  that you're going
[1740.84 --> 1741.70]  to be interacting with.
[1741.70 --> 1744.08]  jQuery top
[1744.08 --> 1745.02]  in the top 10 there.
[1745.28 --> 1745.54]  Still,
[1745.62 --> 1746.54]  still legitimate.
[1747.10 --> 1747.84]  I'm so,
[1748.28 --> 1748.46]  like,
[1748.62 --> 1749.46]  I'm a little sad
[1749.46 --> 1750.50]  that Vue is like
[1750.50 --> 1751.72]  so low
[1751.72 --> 1752.62]  on that list.
[1753.24 --> 1754.24]  Why is it so low?
[1754.86 --> 1756.00]  It's like below Python.
[1758.12 --> 1759.18]  Python is actually
[1759.18 --> 1760.38]  ridiculously popular,
[1760.64 --> 1761.18]  but yeah,
[1761.24 --> 1762.10]  this is supposedly
[1762.10 --> 1762.54]  JavaScript.
[1762.84 --> 1764.10]  For JavaScript developers.
[1764.48 --> 1764.88]  I mean,
[1765.04 --> 1765.28]  yeah.
[1765.38 --> 1766.24]  At least your framework's
[1766.24 --> 1766.62]  on there.
[1767.08 --> 1767.28]  Oh,
[1767.28 --> 1767.90]  that's true.
[1769.90 --> 1770.14]  Yeah.
[1770.64 --> 1771.88]  Not featured things
[1771.88 --> 1772.72]  like Dojo.
[1773.06 --> 1773.28]  Well,
[1773.38 --> 1774.24]  TypeScript is there,
[1774.52 --> 1774.74]  Nick,
[1774.86 --> 1775.82]  so he's there.
[1775.82 --> 1775.96]  Yeah.
[1777.48 --> 1778.50]  I think it is
[1778.50 --> 1779.56]  kind of interesting
[1779.56 --> 1781.10]  to think about this.
[1781.18 --> 1781.32]  I mean,
[1782.00 --> 1783.40]  it's hard to know
[1783.40 --> 1784.16]  without treadlines,
[1784.46 --> 1784.70]  right,
[1784.80 --> 1785.66]  to how much
[1785.66 --> 1786.76]  we should be
[1786.76 --> 1787.90]  considering this,
[1787.98 --> 1788.12]  but,
[1788.24 --> 1788.36]  you know,
[1788.38 --> 1789.20]  this is an interesting
[1789.20 --> 1789.76]  snapshot
[1789.76 --> 1790.60]  of,
[1790.60 --> 1791.70]  you know,
[1791.74 --> 1792.26]  where,
[1792.90 --> 1793.44]  what are people
[1793.44 --> 1794.02]  looking for?
[1794.02 --> 1795.50]  I do wonder,
[1795.68 --> 1797.54]  it says 300 job listings,
[1798.28 --> 1800.24]  and then it has numbers
[1800.24 --> 1800.74]  next to them,
[1800.76 --> 1801.14]  so I'm wondering,
[1801.26 --> 1801.36]  like,
[1801.40 --> 1804.30]  is this 267 job listings
[1804.30 --> 1805.92]  out of 300 featured React?
[1806.10 --> 1806.64]  And if so,
[1806.74 --> 1808.08]  why does Angular have 195?
[1809.72 --> 1810.90]  Are these saying,
[1811.00 --> 1811.14]  oh,
[1811.26 --> 1812.26]  React or Angular?
[1812.58 --> 1812.74]  Like,
[1812.76 --> 1813.70]  that seems a little off.
[1814.78 --> 1815.94]  I bet they probably are.
[1816.04 --> 1816.18]  I mean,
[1816.22 --> 1817.38]  there's some job listings
[1817.38 --> 1818.06]  out there where they'll
[1818.06 --> 1818.90]  just list off
[1818.90 --> 1820.46]  a laundry list of skills
[1820.46 --> 1821.20]  that you should have
[1821.20 --> 1821.62]  in there,
[1822.22 --> 1823.00]  and it'll be a,
[1823.00 --> 1823.24]  you know,
[1823.24 --> 1824.30]  a comma separated list.
[1824.98 --> 1826.06]  You should know React,
[1826.18 --> 1826.52]  Angular,
[1826.66 --> 1827.18]  Vue.js,
[1827.32 --> 1829.48]  and 14 years of experience
[1829.48 --> 1830.68]  with GraphQL,
[1831.10 --> 1831.34]  you know,
[1831.34 --> 1831.88]  stuff like that.
[1832.12 --> 1832.68]  And there's also
[1832.68 --> 1833.64]  general ones,
[1833.68 --> 1833.96]  which is,
[1834.04 --> 1834.12]  like,
[1834.14 --> 1835.54]  not really tech-specific.
[1835.82 --> 1835.98]  There's,
[1836.08 --> 1836.14]  like,
[1836.20 --> 1836.62]  OOP,
[1837.58 --> 1838.90]  and then I think
[1838.90 --> 1840.44]  there's design patterns
[1840.44 --> 1841.08]  as well,
[1841.30 --> 1841.92]  which I was like,
[1842.12 --> 1843.14]  that's interesting,
[1843.14 --> 1844.76]  because that's very general
[1844.76 --> 1846.68]  and subjective.
[1847.56 --> 1848.98]  The one that's curious,
[1849.44 --> 1850.20]  curiously missing
[1850.20 --> 1851.30]  from here is JavaScript.
[1851.86 --> 1852.76]  It's not on there at all.
[1853.24 --> 1855.30]  Maybe it's presupposed.
[1855.72 --> 1856.04]  Probably,
[1856.36 --> 1856.50]  but,
[1856.62 --> 1856.74]  like,
[1857.36 --> 1857.88]  that is,
[1858.06 --> 1859.36]  that's what we focus on
[1859.36 --> 1860.50]  in our interview process
[1860.50 --> 1862.10]  is fundamental JavaScript.
[1862.34 --> 1862.92]  No framework,
[1863.10 --> 1864.02]  no TypeScript,
[1864.24 --> 1865.18]  no Webpack,
[1865.62 --> 1866.20]  no Java,
[1866.74 --> 1867.14]  JavaScript.
[1867.66 --> 1868.74]  What about in your listings?
[1868.84 --> 1870.06]  Is that how it is as well?
[1870.52 --> 1870.74]  Yeah,
[1870.84 --> 1871.36]  I think so.
[1871.64 --> 1872.98]  I will have to double-check that,
[1873.06 --> 1873.22]  though.
[1873.94 --> 1874.24]  Ooh,
[1874.30 --> 1874.90]  now we get it.
[1874.98 --> 1875.14]  Yeah,
[1875.22 --> 1875.68]  quick look.
[1876.78 --> 1877.50]  It does,
[1877.50 --> 1879.18]  so let's step back a little bit
[1879.18 --> 1880.60]  from making fun of
[1880.60 --> 1882.44]  these folks,
[1882.82 --> 1883.22]  because,
[1883.34 --> 1884.46]  I mean,
[1884.48 --> 1885.24]  I think there are things
[1885.24 --> 1885.76]  to make fun of,
[1885.78 --> 1886.78]  but it's actually
[1886.78 --> 1888.00]  a really hard problem
[1888.00 --> 1890.02]  if you're sort of cross-cutting,
[1890.30 --> 1891.04]  which I think they are,
[1891.16 --> 1892.48]  they cross-industries,
[1892.58 --> 1892.72]  to,
[1892.82 --> 1892.90]  like,
[1892.90 --> 1894.28]  look at what are people
[1894.28 --> 1895.02]  putting in resumes
[1895.02 --> 1896.38]  and use that to derive
[1896.38 --> 1899.18]  something interesting.
[1899.32 --> 1899.38]  Like,
[1899.40 --> 1900.66]  that's a very hard problem.
[1902.66 --> 1903.14]  But,
[1903.46 --> 1904.70]  what do we think
[1904.70 --> 1905.66]  this indicates
[1905.66 --> 1906.30]  about,
[1906.30 --> 1906.98]  you know,
[1907.74 --> 1908.54]  finding a job
[1908.54 --> 1909.36]  right now
[1909.36 --> 1910.08]  in tech
[1910.08 --> 1910.82]  doing JavaScript?
[1911.02 --> 1911.12]  Like,
[1911.16 --> 1911.76]  are there insights
[1911.76 --> 1912.52]  that we can draw
[1912.52 --> 1913.04]  from this
[1913.04 --> 1914.24]  with our additional
[1914.24 --> 1915.26]  industry context?
[1916.20 --> 1916.48]  Mm-hmm.
[1916.80 --> 1917.90]  I think the expectation
[1917.90 --> 1918.86]  is much higher.
[1919.46 --> 1919.92]  So,
[1920.00 --> 1920.20]  like,
[1920.40 --> 1920.62]  yes,
[1920.64 --> 1921.56]  you should know JavaScript,
[1921.90 --> 1922.72]  but there's also,
[1922.94 --> 1923.78]  like,
[1924.48 --> 1924.78]  this,
[1925.44 --> 1926.54]  on this expectation
[1926.54 --> 1927.86]  that you also know
[1927.86 --> 1928.84]  all these frameworks,
[1929.26 --> 1929.70]  you know,
[1930.12 --> 1930.50]  you know,
[1930.58 --> 1930.86]  just,
[1930.86 --> 1931.06]  like,
[1931.16 --> 1931.58]  TypeScript,
[1931.86 --> 1932.36]  or you've worked
[1932.36 --> 1933.14]  with Webpack,
[1933.66 --> 1934.62]  and so,
[1934.94 --> 1935.88]  for someone who might
[1935.88 --> 1936.54]  be newer,
[1937.02 --> 1937.66]  or who has just,
[1937.70 --> 1937.92]  like,
[1938.12 --> 1939.40]  started picking up skills,
[1939.74 --> 1940.90]  it's really overwhelming,
[1940.90 --> 1941.82]  and I've talked to a lot
[1941.82 --> 1942.94]  of people who've gone
[1942.94 --> 1944.20]  through boot camps
[1944.20 --> 1945.80]  or are fresh out of school,
[1946.30 --> 1946.74]  and they're like,
[1946.78 --> 1947.72]  what should I focus on?
[1948.20 --> 1948.64]  I'm like,
[1948.82 --> 1949.06]  uh,
[1949.44 --> 1950.24]  usually,
[1950.56 --> 1951.78]  my answer is just,
[1951.84 --> 1952.02]  like,
[1952.14 --> 1953.14]  just get really good
[1953.14 --> 1953.68]  at JavaScript,
[1953.96 --> 1954.22]  or,
[1954.34 --> 1954.52]  like,
[1954.62 --> 1955.52]  whatever it is
[1955.52 --> 1956.48]  you want to do,
[1956.78 --> 1957.74]  because I think the flavor
[1957.74 --> 1958.56]  has come and go,
[1958.68 --> 1958.90]  like,
[1959.08 --> 1960.24]  there's a lot of frameworks
[1960.24 --> 1961.02]  that come in,
[1961.30 --> 1961.32]  and,
[1961.44 --> 1961.58]  like,
[1961.66 --> 1962.72]  React is popular now,
[1962.82 --> 1962.94]  but,
[1963.04 --> 1963.16]  like,
[1963.24 --> 1964.16]  who knows what will happen
[1964.16 --> 1965.30]  in five years,
[1965.74 --> 1966.22]  and so,
[1966.68 --> 1967.30]  like you were saying,
[1967.40 --> 1967.54]  Nick,
[1967.64 --> 1967.80]  just,
[1967.94 --> 1968.02]  like,
[1968.10 --> 1969.26]  a solid understanding
[1969.26 --> 1969.98]  of one thing,
[1970.02 --> 1970.58]  and then working
[1970.58 --> 1971.50]  your way through,
[1971.88 --> 1973.42]  but I find a lot
[1973.42 --> 1974.34]  of job descriptions
[1974.34 --> 1975.78]  tend to just give you
[1975.78 --> 1976.92]  the laundry list
[1976.92 --> 1977.96]  of everything,
[1977.96 --> 1979.34]  and that's,
[1979.44 --> 1979.50]  like,
[1979.56 --> 1980.46]  really hard for someone
[1980.46 --> 1981.34]  who's looking for a job
[1981.34 --> 1981.80]  to be like,
[1981.86 --> 1982.02]  wait,
[1982.08 --> 1983.18]  I only have one of this
[1983.18 --> 1984.34]  or two out of,
[1984.46 --> 1984.54]  like,
[1984.60 --> 1984.90]  20.
[1985.86 --> 1986.22]  Yeah,
[1986.26 --> 1986.56]  for sure.
[1986.62 --> 1987.30]  I think that if you have
[1987.30 --> 1988.24]  a good,
[1988.44 --> 1988.90]  firm understanding
[1988.90 --> 1989.54]  of the fundamentals,
[1989.72 --> 1990.66]  you can really jump in
[1990.66 --> 1992.62]  and pick up Vue
[1992.62 --> 1993.46]  or React
[1993.46 --> 1995.06]  or anything
[1995.06 --> 1995.88]  pretty quickly.
[1996.92 --> 1997.76]  It's just JavaScript.
[1998.26 --> 1998.94]  It's just JavaScript.
[1998.96 --> 1999.48]  It's just JavaScript.
[2002.78 --> 2003.76]  I've actually been doing
[2003.76 --> 2004.42]  a lot of research
[2004.42 --> 2005.86]  on some of this question
[2005.86 --> 2006.02]  of,
[2006.10 --> 2006.16]  like,
[2006.18 --> 2007.04]  what are the skills
[2007.04 --> 2008.52]  that we expect
[2008.52 --> 2008.90]  of people
[2008.90 --> 2009.60]  at different levels?
[2009.60 --> 2010.40]  Because I'm working
[2010.40 --> 2011.16]  on a new project
[2011.16 --> 2012.26]  focused on
[2012.26 --> 2013.92]  training tech leads,
[2013.98 --> 2014.46]  so people who are
[2014.46 --> 2014.96]  a little further
[2014.96 --> 2016.30]  up in the skill ladder,
[2016.40 --> 2017.20]  but as a part of that,
[2017.50 --> 2017.70]  I'm,
[2017.78 --> 2017.86]  like,
[2017.94 --> 2018.36]  researching
[2018.36 --> 2020.10]  this whole progression.
[2020.66 --> 2021.40]  And I found a really
[2021.40 --> 2022.36]  interesting resource
[2022.36 --> 2024.70]  that I'd like to share
[2024.70 --> 2026.68]  at progression.fyi,
[2027.44 --> 2029.68]  which is
[2029.68 --> 2031.22]  a gentleman in England
[2031.22 --> 2032.46]  who has put together
[2032.46 --> 2034.44]  essentially
[2034.44 --> 2036.38]  a collection
[2036.38 --> 2037.54]  of all these different
[2037.54 --> 2038.62]  sort of
[2038.62 --> 2040.28]  career progression charts
[2040.28 --> 2041.04]  that different companies
[2041.04 --> 2041.58]  have published
[2041.58 --> 2042.26]  for engineering
[2042.26 --> 2043.02]  and for design.
[2044.06 --> 2044.24]  So,
[2044.54 --> 2044.74]  you know,
[2045.46 --> 2046.14]  various companies
[2046.14 --> 2046.84]  have written about
[2046.84 --> 2047.76]  their progression charts,
[2047.84 --> 2048.52]  open source things,
[2048.64 --> 2048.94]  whatever,
[2048.94 --> 2050.80]  and,
[2050.92 --> 2051.06]  you know,
[2051.10 --> 2051.50]  shout out,
[2051.64 --> 2052.00]  by the way,
[2052.08 --> 2053.56]  to Natalie Marlaney
[2053.56 --> 2054.14]  who I met
[2054.14 --> 2055.14]  at React Amsterdam
[2055.14 --> 2055.94]  who pointed me
[2055.94 --> 2057.12]  at progression.fyi,
[2057.42 --> 2059.20]  so it's super cool stuff.
[2059.50 --> 2060.12]  But this guy,
[2060.22 --> 2060.74]  Johnny Birch,
[2060.76 --> 2061.54]  has put this together
[2061.54 --> 2063.04]  and one of the things
[2063.04 --> 2063.48]  I've found
[2063.48 --> 2064.38]  pouring through these
[2064.38 --> 2066.22]  is different companies
[2066.22 --> 2069.02]  call these different levels
[2069.02 --> 2069.96]  different things,
[2070.02 --> 2070.70]  like at one company
[2070.70 --> 2071.18]  they might call it
[2071.18 --> 2071.90]  engineering one
[2071.90 --> 2072.96]  versus junior developer
[2072.96 --> 2073.64]  versus this,
[2073.72 --> 2073.86]  that,
[2073.94 --> 2074.18]  the other,
[2074.26 --> 2075.04]  but there are a lot
[2075.04 --> 2075.88]  of commonalities
[2075.88 --> 2076.66]  across them
[2076.66 --> 2079.56]  and this isn't
[2079.56 --> 2080.14]  going to tell you
[2080.14 --> 2081.74]  which skills
[2081.74 --> 2082.88]  in terms of like
[2082.88 --> 2083.60]  should I be learning
[2083.60 --> 2084.76]  React versus whatever,
[2084.92 --> 2086.02]  but like if you're
[2086.02 --> 2086.68]  entry level
[2086.68 --> 2087.40]  and you're junior,
[2088.06 --> 2089.30]  typically what you're
[2089.30 --> 2089.80]  going to be doing
[2089.80 --> 2090.36]  is you're going to be
[2090.36 --> 2091.40]  working on pretty
[2091.40 --> 2092.48]  well-defined tasks,
[2092.60 --> 2093.32]  doing bug fixes,
[2093.32 --> 2094.52]  and really learning
[2094.52 --> 2095.24]  how to learn.
[2095.56 --> 2096.28]  And so like
[2096.28 --> 2098.44]  your focus
[2098.44 --> 2099.38]  should be kind of
[2099.38 --> 2100.28]  figuring out
[2100.28 --> 2101.12]  how to go deep.
[2101.34 --> 2102.34]  Pick one specialty,
[2102.84 --> 2103.28]  go deep.
[2103.48 --> 2103.62]  You know,
[2103.62 --> 2104.28]  if you're in the front end,
[2104.28 --> 2105.62]  maybe pick React
[2105.62 --> 2106.50]  or something,
[2106.62 --> 2107.60]  pick one framework,
[2108.10 --> 2109.58]  go really deep on that
[2109.58 --> 2111.16]  and don't worry
[2111.16 --> 2111.86]  about all the other stuff
[2111.86 --> 2112.76]  because junior developers
[2112.76 --> 2113.56]  are not being asked
[2113.56 --> 2114.30]  to integrate across
[2114.30 --> 2115.04]  five different things.
[2115.14 --> 2116.08]  They're like focused
[2116.08 --> 2117.08]  within one area
[2117.08 --> 2118.04]  and then as you sort of
[2118.04 --> 2120.32]  go up the hierarchy
[2120.32 --> 2120.82]  a little bit,
[2120.86 --> 2121.80]  you get into mid-level,
[2121.98 --> 2123.64]  two or three years in,
[2124.14 --> 2125.80]  now you should be able
[2125.80 --> 2126.48]  to do something
[2126.48 --> 2127.48]  on your own
[2127.48 --> 2128.06]  within your area
[2128.06 --> 2128.60]  of expertise
[2128.60 --> 2130.64]  and start to get
[2130.64 --> 2131.68]  touching other things.
[2131.74 --> 2132.20]  So that's when you're
[2132.20 --> 2132.96]  going to start to branch
[2132.96 --> 2135.16]  out into other skill areas.
[2135.24 --> 2135.44]  But yeah,
[2135.46 --> 2136.06]  if you're just coming
[2136.06 --> 2136.86]  out of a boot camp,
[2137.28 --> 2137.96]  don't try to do
[2137.96 --> 2138.62]  all the things.
[2138.80 --> 2139.32]  Pick one,
[2139.66 --> 2140.40]  go deep on it.
[2141.00 --> 2141.30]  That's a really
[2141.30 --> 2141.88]  interesting take.
[2141.98 --> 2142.82]  So would you say
[2142.82 --> 2144.20]  in 2019,
[2144.82 --> 2145.68]  if you're going to
[2145.68 --> 2146.52]  pick one to go deep,
[2146.58 --> 2147.38]  it seems like you can't
[2147.38 --> 2148.48]  miss with React right now.
[2148.98 --> 2150.68]  If you are in the front end,
[2151.26 --> 2152.40]  you pretty much like,
[2152.56 --> 2152.94]  and you're looking
[2152.94 --> 2153.66]  for something that's
[2153.66 --> 2154.94]  going to get you a job,
[2155.64 --> 2156.44]  React is probably
[2156.44 --> 2157.22]  your best choice.
[2157.86 --> 2158.62]  Sorry, Vue.js.
[2159.36 --> 2160.06]  Sorry, Divya.
[2160.42 --> 2161.76]  Vue is still cool.
[2161.76 --> 2163.20]  It's still cool.
[2163.98 --> 2164.96]  So Rich Howell
[2164.96 --> 2165.50]  in the chat
[2165.50 --> 2167.12]  is also a Vue developer
[2167.12 --> 2168.02]  and is currently
[2168.02 --> 2168.74]  applying for work
[2168.74 --> 2169.54]  and can confirm
[2169.54 --> 2170.82]  that it's pretty low
[2170.82 --> 2171.72]  on people's list.
[2172.64 --> 2173.10]  He says,
[2173.16 --> 2173.46]  thankfully,
[2173.56 --> 2174.22]  his Vue experience
[2174.22 --> 2174.94]  transfers over
[2174.94 --> 2175.94]  to React pretty well.
[2176.04 --> 2176.50]  So that's one thing
[2176.50 --> 2177.02]  that you'll find
[2177.02 --> 2177.62]  over time
[2177.62 --> 2178.78]  is a lot of the skills
[2178.78 --> 2179.74]  from all these things
[2179.74 --> 2180.54]  transfer over.
[2181.06 --> 2181.76]  There are some like,
[2182.24 --> 2185.06]  if you dove in,
[2185.18 --> 2185.58]  dive in,
[2185.66 --> 2185.98]  I don't know,
[2186.04 --> 2186.48]  if you're deep
[2186.48 --> 2187.18]  into Angular
[2187.18 --> 2187.72]  and you know
[2187.72 --> 2188.92]  the bugs,
[2189.14 --> 2189.68]  the workarounds
[2189.68 --> 2190.28]  for the bugs,
[2190.28 --> 2191.40]  that skill
[2191.40 --> 2192.34]  will not translate.
[2192.56 --> 2192.86]  Like maybe
[2192.86 --> 2193.78]  your process
[2193.78 --> 2194.24]  of finding
[2194.24 --> 2194.88]  those workarounds
[2194.88 --> 2195.62]  absolutely will,
[2196.14 --> 2196.90]  but like you know
[2196.90 --> 2197.48]  how exactly
[2197.48 --> 2197.92]  to interact
[2197.92 --> 2198.66]  with this API
[2198.66 --> 2199.80]  because you've
[2199.80 --> 2200.40]  gotten that deep
[2200.40 --> 2200.76]  into it.
[2201.02 --> 2201.92]  That itself
[2201.92 --> 2202.94]  probably won't
[2202.94 --> 2203.50]  transfer over
[2203.50 --> 2203.98]  to another one
[2203.98 --> 2204.20]  because they're
[2204.20 --> 2204.42]  not going to
[2204.42 --> 2204.88]  have that bug.
[2204.98 --> 2205.22]  They're not going
[2205.22 --> 2205.52]  to have that
[2205.52 --> 2206.22]  specific API.
[2206.94 --> 2207.78]  That being said,
[2208.28 --> 2210.22]  the general themes
[2210.22 --> 2212.92]  and architectural things
[2212.92 --> 2213.70]  in a lot of these
[2213.70 --> 2214.06]  frameworks
[2214.06 --> 2215.16]  will transfer over.
[2215.16 --> 2216.54]  So a lot of
[2216.54 --> 2217.74]  I think what
[2217.74 --> 2218.40]  happens with people
[2218.40 --> 2219.18]  is they just get
[2219.18 --> 2221.32]  analysis paralysis
[2221.32 --> 2222.66]  and it's just like
[2222.66 --> 2223.36]  what do I pick?
[2223.42 --> 2224.18]  What do I do?
[2224.50 --> 2225.52]  I spend most of my time
[2225.52 --> 2227.14]  reading articles like this
[2227.14 --> 2229.12]  of which one
[2229.12 --> 2229.68]  because it's such
[2229.68 --> 2230.50]  a huge decision
[2230.50 --> 2231.86]  and I guess my point
[2231.86 --> 2232.42]  here is
[2232.42 --> 2233.78]  just realize
[2233.78 --> 2235.28]  it's not that huge
[2235.28 --> 2235.76]  of a decision
[2235.76 --> 2237.38]  and maybe just optimize
[2237.38 --> 2238.88]  for something like this.
[2239.04 --> 2239.34]  Like well,
[2239.42 --> 2240.12]  most jobs here,
[2240.20 --> 2240.68]  I'm just going to learn
[2240.68 --> 2241.66]  that one and go from there
[2241.66 --> 2243.26]  and it does seem like
[2243.26 --> 2243.78]  today,
[2243.90 --> 2244.72]  although maybe tomorrow
[2244.72 --> 2245.48]  view will be
[2245.48 --> 2246.76]  higher up,
[2247.26 --> 2247.68]  but if you're going
[2247.68 --> 2248.14]  to just pick one
[2248.14 --> 2248.64]  and dive deep,
[2248.70 --> 2249.40]  it seems like React
[2249.40 --> 2250.60]  is in 2019
[2250.60 --> 2252.52]  your best bet.
[2253.22 --> 2253.30]  Yeah,
[2253.36 --> 2254.14]  there are some
[2254.14 --> 2255.22]  megatrends
[2255.22 --> 2256.62]  that are showing up
[2256.62 --> 2257.30]  across the board
[2257.30 --> 2258.04]  that to your point,
[2258.16 --> 2259.36]  like if you learn
[2259.36 --> 2260.38]  in one example,
[2260.38 --> 2261.42]  it will then be easy
[2261.42 --> 2262.16]  to branch out,
[2262.26 --> 2262.38]  right?
[2262.46 --> 2264.34]  So like staying
[2264.34 --> 2265.18]  in the front end world,
[2265.22 --> 2265.84]  I think there are also
[2265.84 --> 2266.52]  some megatrends
[2266.52 --> 2266.98]  in the back end,
[2267.04 --> 2267.90]  but in the front end world,
[2268.30 --> 2269.38]  component oriented
[2269.38 --> 2269.90]  development,
[2270.24 --> 2271.30]  thinking about things
[2271.30 --> 2272.52]  as a set of components
[2272.52 --> 2273.80]  that can be interact,
[2273.88 --> 2274.06]  you know,
[2274.06 --> 2275.18]  interact and plug and play.
[2275.74 --> 2277.04]  Like React is doing that,
[2277.14 --> 2277.90]  Angular is doing that,
[2278.00 --> 2278.70]  Vue is doing that,
[2278.80 --> 2279.52]  Ember is doing that,
[2279.62 --> 2280.38]  Dojo is doing that,
[2280.46 --> 2281.24]  Mithril is doing that,
[2281.32 --> 2282.10]  Svelte is doing that,
[2282.16 --> 2284.32]  like that is the approach
[2284.32 --> 2285.10]  that we're going.
[2285.24 --> 2286.20]  So start in React
[2286.20 --> 2286.94]  because it's easy
[2286.94 --> 2287.70]  to get a job there,
[2288.38 --> 2288.96]  dive deep,
[2289.16 --> 2290.20]  but have in mind,
[2290.58 --> 2290.84]  okay,
[2290.98 --> 2291.78]  how am I thinking
[2291.78 --> 2293.44]  about components?
[2293.62 --> 2294.36]  What are the boundaries?
[2294.50 --> 2295.12]  How are we doing that?
[2295.18 --> 2296.18]  That understanding,
[2296.34 --> 2296.74]  that knowledge,
[2296.82 --> 2297.30]  that experience
[2297.30 --> 2298.04]  is going to translate
[2298.04 --> 2299.00]  no matter what framework
[2299.00 --> 2300.18]  you end up moving to
[2300.18 --> 2301.30]  in the next job
[2301.30 --> 2301.74]  or whatever.
[2302.54 --> 2302.98]  Similarly,
[2303.18 --> 2304.56]  things like declarative coding,
[2304.84 --> 2305.00]  right?
[2305.02 --> 2306.30]  We are increasingly
[2306.30 --> 2308.12]  moving to a declarative paradigm
[2308.12 --> 2309.32]  for our components.
[2309.46 --> 2310.72]  We're not imperatively
[2310.72 --> 2311.26]  doing things.
[2311.34 --> 2312.08]  We're thinking about,
[2312.40 --> 2312.64]  you know,
[2313.04 --> 2314.24]  here's what this thing
[2314.24 --> 2315.32]  should be
[2315.32 --> 2316.44]  and letting frameworks
[2316.44 --> 2317.80]  handle how and when.
[2317.94 --> 2318.74]  And that's another place
[2318.74 --> 2319.00]  where,
[2319.56 --> 2319.76]  like,
[2320.54 --> 2321.32]  if so long as
[2321.32 --> 2322.24]  what you're working in
[2322.24 --> 2323.08]  is doing that,
[2323.26 --> 2323.80]  which means maybe
[2323.80 --> 2325.06]  not focusing on jQuery,
[2325.28 --> 2325.82]  but, you know,
[2325.84 --> 2326.96]  if you're doing React,
[2327.06 --> 2327.86]  like those skills
[2327.86 --> 2328.38]  are once again
[2328.38 --> 2329.02]  going to translate.
[2329.02 --> 2329.92]  So, like,
[2329.98 --> 2330.58]  there's a lot
[2330.58 --> 2331.60]  of these megatrends.
[2332.50 --> 2334.06]  I identified five
[2334.06 --> 2334.78]  in a blog post
[2334.78 --> 2335.64]  earlier this year,
[2335.76 --> 2336.62]  but, like,
[2336.74 --> 2337.34]  if you look for
[2337.34 --> 2338.68]  the bigger picture questions
[2338.68 --> 2341.82]  and start learning those
[2341.82 --> 2342.94]  within the context
[2342.94 --> 2343.56]  of one thing
[2343.56 --> 2344.44]  you're going deep on,
[2344.70 --> 2345.22]  you're not going
[2345.22 --> 2345.92]  to end up in trouble
[2345.92 --> 2346.60]  when suddenly,
[2346.76 --> 2347.24]  you know,
[2347.26 --> 2347.94]  the flavor of the month
[2347.94 --> 2348.40]  changes.
[2348.66 --> 2349.50]  I'm going to assume
[2349.50 --> 2350.40]  that's what that list
[2350.40 --> 2351.94]  meant by design patterns
[2351.94 --> 2353.66]  to be, like,
[2353.98 --> 2354.46]  general,
[2354.74 --> 2355.00]  like,
[2355.16 --> 2356.36]  declarative versus imperative
[2356.36 --> 2357.34]  and, like,
[2357.60 --> 2358.36]  how you do something
[2358.36 --> 2358.94]  in React,
[2359.12 --> 2359.94]  which is overall,
[2360.04 --> 2360.22]  like,
[2360.30 --> 2360.84]  very specific
[2360.84 --> 2361.54]  to the framework,
[2362.16 --> 2363.20]  but, like,
[2363.36 --> 2364.06]  the pattern
[2364.06 --> 2365.32]  of doing it
[2365.32 --> 2366.36]  can be used
[2366.36 --> 2366.84]  in Angular
[2366.84 --> 2367.72]  and can be used
[2367.72 --> 2368.18]  in Vue
[2368.18 --> 2369.08]  if you just change,
[2369.18 --> 2369.46]  like,
[2369.58 --> 2370.32]  some syntax
[2370.32 --> 2371.06]  and the structure,
[2371.20 --> 2371.70]  but essentially
[2371.70 --> 2372.90]  they all call it
[2372.90 --> 2373.72]  different things,
[2373.78 --> 2374.54]  but they might mean
[2374.54 --> 2374.90]  the same.
[2375.34 --> 2375.54]  So,
[2375.86 --> 2376.56]  it's just kind of,
[2376.64 --> 2376.82]  like,
[2377.18 --> 2377.96]  if you master
[2377.96 --> 2378.88]  one framework
[2378.88 --> 2380.24]  and just know it
[2380.24 --> 2380.88]  really well,
[2381.26 --> 2381.72]  translating
[2381.72 --> 2382.86]  can be frustrating,
[2383.12 --> 2383.92]  but at the same time
[2383.92 --> 2385.04]  you have the tools
[2385.04 --> 2386.46]  and you have those patterns
[2386.46 --> 2387.10]  that you already
[2387.10 --> 2387.84]  are familiar with
[2387.84 --> 2388.86]  and they will probably
[2388.86 --> 2390.54]  translate quite easily
[2390.54 --> 2392.04]  once you get used
[2392.04 --> 2393.04]  to a different syntax
[2393.04 --> 2393.56]  and everything,
[2393.80 --> 2393.98]  so.
[2394.78 --> 2395.02]  Also,
[2395.10 --> 2395.62]  have you seen,
[2395.78 --> 2395.94]  like,
[2395.96 --> 2396.56]  I think I posted
[2396.56 --> 2397.08]  in the chat,
[2397.20 --> 2397.86]  but have you seen
[2397.86 --> 2398.38]  that tweet
[2398.38 --> 2399.10]  that Emma,
[2399.48 --> 2399.80]  like,
[2400.68 --> 2400.94]  tweeted
[2400.94 --> 2402.42]  a couple of days ago
[2402.42 --> 2403.10]  about, like,
[2403.54 --> 2404.78]  React being the kid
[2404.78 --> 2405.62]  who cuts school
[2405.62 --> 2407.04]  and then Vue
[2407.04 --> 2408.24]  being the nice kid
[2408.24 --> 2408.94]  in school?
[2410.20 --> 2410.86]  She was trying
[2410.86 --> 2411.18]  to, like,
[2411.24 --> 2412.00]  immortalize
[2412.00 --> 2413.28]  the different technologies
[2413.28 --> 2413.90]  and I thought
[2413.90 --> 2414.60]  it was really funny
[2414.60 --> 2415.48]  and CSS is,
[2415.58 --> 2415.62]  like,
[2415.64 --> 2416.08]  the flaky
[2416.08 --> 2417.58]  unpredictable one.
[2419.30 --> 2420.22]  It's so funny.
[2420.72 --> 2421.34]  That is funny.
[2421.46 --> 2422.66]  We'll have to include
[2422.66 --> 2423.26]  that one in the notes
[2423.26 --> 2423.66]  as well.
[2424.24 --> 2425.00]  One other thing
[2425.00 --> 2425.64]  that I noticed in here
[2425.64 --> 2426.02]  and then I want
[2426.02 --> 2426.54]  to kick it over
[2426.54 --> 2427.28]  to maybe Nick
[2427.28 --> 2428.46]  to talk about
[2428.46 --> 2429.18]  backend, too,
[2429.28 --> 2429.76]  because, you know,
[2429.78 --> 2430.84]  Node is popular,
[2431.02 --> 2431.66]  but inside of Node,
[2431.70 --> 2431.82]  like,
[2431.86 --> 2432.32]  what do you learn?
[2432.40 --> 2433.00]  What do you dive
[2433.00 --> 2433.52]  into there
[2433.52 --> 2434.20]  if you're thinking
[2434.20 --> 2434.72]  more backend
[2434.72 --> 2435.06]  JavaScript?
[2435.92 --> 2437.32]  Is that there are
[2437.32 --> 2437.98]  a lot of things
[2437.98 --> 2438.64]  on this list.
[2438.70 --> 2438.94]  I'm not sure
[2438.94 --> 2439.56]  how long this list is,
[2439.60 --> 2440.38]  maybe 20 items.
[2440.48 --> 2441.08]  I didn't count them
[2441.08 --> 2442.08]  and they aren't numbered,
[2442.08 --> 2443.82]  but there are lots,
[2443.92 --> 2444.08]  like,
[2444.14 --> 2444.90]  four at least
[2444.90 --> 2445.90]  that I'm just staring at
[2445.90 --> 2447.22]  that have specifically
[2447.22 --> 2448.04]  to do with testing.
[2448.66 --> 2448.80]  So,
[2448.90 --> 2449.84]  unit testing is one,
[2450.56 --> 2451.14]  Mocha,
[2451.64 --> 2452.10]  another one,
[2452.20 --> 2452.68]  obviously,
[2452.82 --> 2453.72]  a very specific
[2453.72 --> 2455.10]  testing library,
[2455.64 --> 2456.70]  continuous integration,
[2457.02 --> 2458.10]  which you can't really
[2458.10 --> 2459.00]  use without tests,
[2459.56 --> 2459.90]  Jest,
[2460.52 --> 2460.88]  TDD,
[2461.20 --> 2461.30]  like,
[2461.36 --> 2461.98]  these are things
[2461.98 --> 2462.32]  in here.
[2462.46 --> 2462.60]  So,
[2462.98 --> 2464.16]  in terms of big trends,
[2464.86 --> 2465.38]  especially in the
[2465.38 --> 2466.40]  dynamic language space,
[2466.46 --> 2466.56]  now,
[2466.62 --> 2467.06]  the typescripts
[2467.06 --> 2467.58]  in there as well,
[2467.64 --> 2468.30]  which might mitigate
[2468.30 --> 2469.00]  some of the tests
[2469.00 --> 2469.62]  that you have to write.
[2470.34 --> 2470.96]  And Nick can probably
[2470.96 --> 2471.60]  gush on that
[2471.60 --> 2472.40]  in a minute,
[2472.58 --> 2474.28]  but learn how to
[2474.28 --> 2476.16]  write automated tests
[2476.16 --> 2476.92]  for code.
[2477.10 --> 2477.42]  Because,
[2478.12 --> 2478.54]  yes,
[2478.66 --> 2479.40]  the specifics
[2479.40 --> 2480.40]  of the way you do it
[2480.40 --> 2480.94]  in this language,
[2481.04 --> 2481.64]  how do you mock
[2481.64 --> 2482.10]  in this language
[2482.10 --> 2482.82]  versus that,
[2483.44 --> 2484.08]  et cetera,
[2484.66 --> 2485.92]  may not transfer over,
[2486.24 --> 2487.52]  but the skill
[2487.52 --> 2488.46]  of being able
[2488.46 --> 2489.46]  to write a test
[2489.46 --> 2491.56]  to fully exercise
[2491.56 --> 2492.34]  a piece of code,
[2492.90 --> 2493.66]  you'll use for the rest
[2493.66 --> 2494.12]  of your career.
[2494.12 --> 2494.40]  So,
[2494.46 --> 2494.90]  absolutely,
[2495.68 --> 2496.22]  that is something
[2496.22 --> 2497.00]  that is trending
[2497.00 --> 2497.86]  and will continue
[2497.86 --> 2498.32]  to trend
[2498.32 --> 2499.50]  until we have
[2499.50 --> 2500.40]  machines that write
[2500.40 --> 2500.86]  all our tests
[2500.86 --> 2501.38]  for us.
[2502.04 --> 2502.62]  But then we have to,
[2502.80 --> 2503.30]  who's going to test
[2503.30 --> 2503.72]  the machine,
[2503.90 --> 2504.14]  you know?
[2505.26 --> 2505.86]  What about the
[2505.86 --> 2506.22]  back-end,
[2506.32 --> 2506.50]  guys?
[2507.28 --> 2507.86]  I think that there's
[2507.86 --> 2509.64]  a core set of skills
[2509.64 --> 2510.46]  that you need to
[2510.46 --> 2511.66]  know about the
[2511.66 --> 2513.12]  back-end as well,
[2513.18 --> 2514.20]  just in a similar way
[2514.20 --> 2514.74]  that there is about
[2514.74 --> 2515.24]  the front-end.
[2515.80 --> 2517.20]  And the primary one
[2517.20 --> 2517.76]  that comes to mind
[2517.76 --> 2518.14]  when I'm thinking
[2518.14 --> 2518.72]  about back-end
[2518.72 --> 2519.24]  JavaScript,
[2519.86 --> 2520.80]  it seems like
[2520.80 --> 2521.44]  everything kind of
[2521.44 --> 2522.02]  stems from
[2522.02 --> 2523.22]  Express in some way,
[2523.22 --> 2524.58]  at least in what
[2524.58 --> 2524.96]  I've seen.
[2527.10 --> 2528.14]  I'm currently using
[2528.14 --> 2528.82]  a project called
[2528.82 --> 2529.78]  NestJS,
[2529.90 --> 2530.78]  which is like a
[2530.78 --> 2531.84]  TypeScript wrapper
[2531.84 --> 2533.32]  around Nest,
[2533.54 --> 2534.30]  or around Express,
[2534.58 --> 2535.14]  but it adds,
[2535.98 --> 2536.68]  it makes it more
[2536.68 --> 2537.46]  Angular-like is the
[2537.46 --> 2538.34]  way I describe it,
[2538.40 --> 2539.22]  but in a good way.
[2539.70 --> 2540.62]  Give the elevator
[2540.62 --> 2541.28]  pitch on Express,
[2541.54 --> 2542.38]  explain what that is.
[2543.30 --> 2544.40]  It's a way to
[2544.40 --> 2545.28]  set up,
[2545.76 --> 2546.38]  a way to handle
[2546.38 --> 2547.36]  routes for
[2547.36 --> 2548.22]  a back-end.
[2548.30 --> 2548.84]  So you can say,
[2548.98 --> 2549.84]  you can define
[2549.84 --> 2550.34]  and say,
[2550.96 --> 2551.64]  you know,
[2551.64 --> 2553.42]  when your server
[2553.42 --> 2554.48]  gets a call
[2554.48 --> 2555.66]  to this request,
[2555.74 --> 2557.26]  like this URL,
[2557.62 --> 2557.96]  effectively,
[2558.56 --> 2560.18]  run this function
[2560.18 --> 2561.14]  and deliver something
[2561.14 --> 2561.46]  back.
[2561.52 --> 2562.20]  But then it gives you
[2562.20 --> 2563.18]  the ability to
[2563.18 --> 2564.36]  add in middleware
[2564.36 --> 2565.48]  and other things
[2565.48 --> 2566.12]  so you can plug in
[2566.12 --> 2566.46]  and say,
[2566.64 --> 2566.84]  like,
[2566.98 --> 2567.16]  you know,
[2567.20 --> 2567.98]  this route is
[2567.98 --> 2569.80]  only available
[2569.80 --> 2570.44]  to administrators.
[2570.66 --> 2571.38]  So before you
[2571.38 --> 2572.14]  actually serve it,
[2572.44 --> 2573.30]  double-check this route
[2573.30 --> 2574.08]  specifically and make
[2574.08 --> 2574.72]  sure that it's,
[2575.26 --> 2576.08]  the user is
[2576.08 --> 2576.72]  authenticated to
[2576.72 --> 2577.46]  be able to see it.
[2577.46 --> 2577.90]  And if not,
[2578.08 --> 2578.80]  throw them back in
[2578.80 --> 2579.00]  error,
[2579.16 --> 2579.84]  otherwise run the
[2579.84 --> 2580.18]  function.
[2580.18 --> 2581.00]  And kind of
[2581.00 --> 2581.98]  abstracting that away
[2581.98 --> 2582.70]  so that you don't
[2582.70 --> 2583.80]  have to think about
[2583.80 --> 2584.64]  it on every single
[2584.64 --> 2585.12]  request.
[2586.16 --> 2587.20]  Anybody have anything
[2587.20 --> 2588.22]  to add on the
[2588.22 --> 2589.72]  back-end space,
[2589.82 --> 2590.28]  trends,
[2590.38 --> 2590.88]  what to learn,
[2591.00 --> 2591.54]  what to avoid,
[2591.60 --> 2591.80]  maybe?
[2592.48 --> 2593.66]  I think one thing
[2593.66 --> 2596.10]  that is tricky
[2596.10 --> 2596.86]  both on the front
[2596.86 --> 2597.56]  end and the back-end
[2597.56 --> 2598.02]  and I think is
[2598.02 --> 2599.60]  something that is
[2599.60 --> 2600.06]  probably,
[2600.42 --> 2601.10]  judging from what
[2601.10 --> 2601.58]  I've seen,
[2601.90 --> 2602.46]  something that you
[2602.46 --> 2603.22]  start to really
[2603.22 --> 2603.74]  wrap your head
[2603.74 --> 2604.28]  around a little
[2604.28 --> 2605.12]  later in the game,
[2606.06 --> 2606.24]  you know,
[2606.44 --> 2607.60]  certainly a year or
[2607.60 --> 2608.18]  two at least
[2608.18 --> 2609.24]  into your career
[2609.24 --> 2609.74]  if you're coming
[2609.74 --> 2610.28]  from bootcamp
[2610.28 --> 2610.96]  and we have
[2610.96 --> 2611.66]  focused very much
[2611.66 --> 2612.52]  on early career
[2612.52 --> 2613.16]  folks for this
[2613.16 --> 2613.72]  conversation,
[2613.94 --> 2616.04]  but this is,
[2616.20 --> 2617.32]  it's data
[2617.32 --> 2618.04]  manipulation and
[2618.04 --> 2618.62]  data management,
[2619.12 --> 2619.34]  right?
[2619.38 --> 2620.32]  How do I
[2620.32 --> 2622.28]  think about
[2622.28 --> 2624.22]  taking data,
[2624.42 --> 2625.28]  transforming it,
[2625.38 --> 2625.90]  using it in
[2625.90 --> 2626.64]  different ways,
[2627.00 --> 2627.92]  whether that's on
[2627.92 --> 2628.50]  the back-end
[2628.50 --> 2629.22]  saying what are
[2629.22 --> 2629.92]  the data stores
[2629.92 --> 2630.46]  that I'm working
[2630.46 --> 2631.22]  with and how do
[2631.22 --> 2632.24]  I, you know,
[2632.28 --> 2633.12]  normalize my data
[2633.12 --> 2633.80]  and doing that
[2633.80 --> 2634.66]  or on the front-end
[2634.66 --> 2635.26]  saying, okay,
[2635.32 --> 2636.02]  I'm loading this
[2636.02 --> 2636.90]  data from APIs,
[2636.90 --> 2637.84]  but it may not
[2637.84 --> 2638.66]  be exactly what
[2638.66 --> 2639.70]  I need for my
[2639.70 --> 2640.48]  UI unless I'm
[2640.48 --> 2641.16]  using GraphQL
[2641.16 --> 2642.00]  or if I'm using
[2642.00 --> 2642.74]  GraphQL thinking
[2642.74 --> 2643.60]  about how do I
[2643.60 --> 2644.14]  generate those
[2644.14 --> 2645.54]  queries and sort
[2645.54 --> 2648.22]  of that way that
[2648.22 --> 2649.32]  data flows through
[2649.32 --> 2650.10]  systems and you
[2650.10 --> 2650.98]  can manipulate it
[2650.98 --> 2651.54]  and, you know,
[2651.90 --> 2652.32]  thinking about
[2652.32 --> 2652.68]  things like
[2652.68 --> 2653.66]  transformations and
[2653.66 --> 2654.70]  mapping and all
[2654.70 --> 2655.22]  that stuff,
[2655.60 --> 2656.52]  like that seems to
[2656.52 --> 2657.26]  be something that
[2657.26 --> 2658.98]  is a little harder
[2658.98 --> 2660.14]  for folks to pick
[2660.14 --> 2661.08]  up than the kind
[2661.08 --> 2663.86]  of sort of first
[2663.86 --> 2665.02]  UI logic or in
[2665.02 --> 2665.84]  the back-end
[2665.84 --> 2666.54]  sort of first
[2666.54 --> 2667.36]  logic around,
[2667.54 --> 2668.02]  okay, I'm setting
[2668.02 --> 2668.66]  up these routes
[2668.66 --> 2669.32]  and this type of
[2669.32 --> 2671.10]  thing, but really
[2671.10 --> 2672.26]  starts to be
[2672.26 --> 2673.88]  important as you
[2673.88 --> 2674.78]  go forward and
[2674.78 --> 2675.92]  that seems like
[2675.92 --> 2677.60]  you're just thinking
[2677.60 --> 2678.66]  about data and how
[2678.66 --> 2679.40]  data flows through
[2679.40 --> 2680.30]  an application is
[2680.30 --> 2680.98]  something that,
[2682.20 --> 2683.14]  it's not really
[2683.14 --> 2685.80]  well captured in
[2685.80 --> 2686.68]  one particular tool
[2686.68 --> 2687.64]  here, but definitely
[2687.64 --> 2688.20]  is something that
[2688.20 --> 2689.00]  I've seen folks
[2689.00 --> 2689.94]  struggle with and
[2689.94 --> 2690.38]  that is really
[2690.38 --> 2691.10]  important as you
[2691.10 --> 2692.06]  start to move from
[2692.06 --> 2693.54]  entry-level to a
[2693.54 --> 2694.00]  little bit more
[2694.00 --> 2695.16]  senior, for sure.
[2695.36 --> 2696.48]  I think especially
[2696.48 --> 2698.36]  since it moves past
[2698.36 --> 2699.32]  just working on
[2699.32 --> 2700.30]  like small features
[2700.30 --> 2701.18]  and you have to
[2701.18 --> 2701.74]  think about the
[2701.74 --> 2702.62]  overall architecture
[2702.62 --> 2704.56]  and like whether
[2704.56 --> 2706.26]  it's scalable and
[2706.26 --> 2707.70]  maintainable and
[2707.70 --> 2708.44]  those are the things
[2708.44 --> 2708.92]  you have to think
[2708.92 --> 2709.70]  about, just like how
[2709.70 --> 2710.52]  does the data flow,
[2711.14 --> 2713.10]  like what is the
[2713.10 --> 2713.74]  architecture of the
[2713.74 --> 2714.38]  back-end and how
[2714.38 --> 2715.16]  does it provide data
[2715.16 --> 2715.86]  to the front-end and
[2715.86 --> 2716.52]  how's the front-end
[2716.52 --> 2717.52]  like liaises with the
[2717.52 --> 2718.56]  back-end and so on
[2718.56 --> 2720.40]  and just understanding
[2720.40 --> 2722.74]  that requires like a
[2722.74 --> 2723.80]  bit of experience I
[2723.80 --> 2724.56]  think, just like
[2724.56 --> 2725.30]  having worked on
[2725.30 --> 2726.64]  different applications,
[2727.42 --> 2728.12]  having played around
[2728.12 --> 2729.42]  with things and just
[2729.42 --> 2730.94]  yeah, that's a
[2730.94 --> 2731.94]  generally like the
[2731.94 --> 2733.02]  more senior you get
[2733.02 --> 2734.58]  the expectation is
[2734.58 --> 2736.20]  that you know these
[2736.20 --> 2737.56]  like how to do that
[2737.56 --> 2738.46]  and how to like work
[2738.46 --> 2739.28]  those problems.
[2739.90 --> 2740.80]  Would you classify
[2740.80 --> 2741.74]  tooling as a
[2741.74 --> 2742.38]  back-end or a
[2742.38 --> 2743.04]  front-end thing,
[2743.46 --> 2744.76]  like webpack and
[2744.76 --> 2746.20]  other tooling like
[2746.20 --> 2746.48]  that?
[2747.28 --> 2748.06]  Almost orthogonal.
[2748.96 --> 2750.00]  Yeah, it depends on
[2750.00 --> 2750.54]  what kind of tooling
[2750.54 --> 2751.22]  you're talking about
[2751.22 --> 2751.66]  I guess, are you
[2751.66 --> 2751.88]  talking about
[2751.88 --> 2752.70]  back-end tooling or
[2752.70 --> 2753.28]  front-end tooling?
[2753.94 --> 2756.48]  I would say version
[2756.48 --> 2758.42]  control, communication
[2758.42 --> 2759.82]  and things like this
[2759.82 --> 2760.94]  across all those
[2760.94 --> 2762.58]  chasms but tooling's
[2762.58 --> 2763.54]  very specific to
[2763.54 --> 2765.10]  I mean Docker I
[2765.10 --> 2765.42]  guess would be
[2765.42 --> 2766.42]  another one that is
[2766.42 --> 2769.68]  general, containers,
[2769.84 --> 2770.44]  that kind of stuff.
[2770.74 --> 2771.58]  I feel like containers
[2771.58 --> 2772.48]  moves into like
[2772.48 --> 2774.60]  DevOps-y space where
[2774.60 --> 2775.02]  it's like...
[2775.02 --> 2775.30]  Well at least to be
[2775.30 --> 2776.28]  able to use them if
[2776.28 --> 2777.10]  not to create them.
[2777.10 --> 2777.78]  Yeah, just like create
[2777.78 --> 2778.98]  a Docker file and
[2778.98 --> 2779.76]  then like okay.
[2779.76 --> 2781.22]  That's very much
[2781.22 --> 2781.94]  where I'm still at
[2781.94 --> 2782.84]  is like I can create
[2782.84 --> 2783.60]  a little Docker file
[2783.60 --> 2784.52]  and I can like do
[2784.52 --> 2785.14]  a thing but...
[2785.14 --> 2786.16]  That's usually where
[2786.16 --> 2786.88]  I'm at, yeah.
[2787.10 --> 2787.74]  And half the time
[2787.74 --> 2788.84]  when Docker like
[2788.84 --> 2790.10]  doesn't like sometimes
[2790.10 --> 2791.12]  it has trouble like
[2791.12 --> 2792.12]  with hot reloading
[2792.12 --> 2792.72]  and then people will
[2792.72 --> 2793.50]  be like oh just like
[2793.50 --> 2794.60]  restart your whatever
[2794.60 --> 2795.44]  and I'm like cool.
[2796.76 --> 2797.72]  Just turn it on and
[2797.72 --> 2798.36]  off again, that's
[2798.36 --> 2799.24]  pretty much mine as
[2799.24 --> 2799.46]  well.
[2800.18 --> 2801.20]  If it doesn't work.
[2801.90 --> 2802.60]  I mean a lot of
[2802.60 --> 2803.36]  tools are like that.
[2803.54 --> 2804.46]  Git, you can get by
[2804.46 --> 2805.30]  on about eight Git
[2805.30 --> 2806.48]  commands for years
[2806.48 --> 2807.66]  and you're just like
[2807.66 --> 2808.24]  do the magic
[2808.24 --> 2809.60]  incantation, right?
[2809.94 --> 2810.30]  100%.
[2810.30 --> 2811.04]  Just write them
[2811.04 --> 2812.00]  down and use them
[2812.00 --> 2813.04]  and eventually you
[2813.04 --> 2813.66]  might figure out.
[2813.80 --> 2814.34]  I still don't know
[2814.34 --> 2815.24]  exactly how Git works.
[2815.32 --> 2815.80]  I know there's a lot
[2815.80 --> 2816.68]  of pointers to
[2816.68 --> 2818.42]  shahs and stuff but
[2818.42 --> 2818.82]  I don't know.
[2818.92 --> 2819.54]  I just have all the
[2819.54 --> 2820.58]  commands memorized and
[2820.58 --> 2821.14]  Yeah, I think
[2821.14 --> 2822.44]  and you don't need to
[2822.44 --> 2823.16]  use all of them.
[2823.38 --> 2824.18]  Like I think I've only
[2824.18 --> 2825.18]  used the Git bisect
[2825.18 --> 2826.50]  like twice ever
[2826.50 --> 2828.36]  and that was like
[2828.36 --> 2829.18]  a mistake.
[2830.02 --> 2830.90]  Yeah, I used it once
[2830.90 --> 2831.48]  and I was like oh
[2831.48 --> 2832.08]  I'm never doing this
[2832.08 --> 2832.36]  again.
[2832.56 --> 2833.32]  Exactly, because
[2833.32 --> 2834.02]  it's just like I
[2834.02 --> 2834.48]  don't know what's
[2834.48 --> 2834.90]  happening.
[2835.34 --> 2836.02]  I just decided to
[2836.02 --> 2836.76]  write less bugs.
[2837.24 --> 2837.48]  Yeah.
[2838.22 --> 2839.24]  I taught an advanced
[2839.24 --> 2840.38]  Git workshop once and
[2840.38 --> 2841.08]  I spent the first
[2841.08 --> 2841.96]  hour and a half going
[2841.96 --> 2842.90]  through the anatomy of
[2842.90 --> 2843.58]  a single commit.
[2844.26 --> 2844.62]  Wow.
[2845.14 --> 2845.70]  You should do that
[2845.70 --> 2846.40]  on the show sometime.
[2847.20 --> 2847.38]  Yeah.
[2848.34 --> 2849.02]  There's a lot of
[2849.02 --> 2849.70]  interesting things in
[2849.70 --> 2849.88]  there.
[2850.36 --> 2850.92]  It does.
[2852.36 --> 2853.70]  When if you choose
[2853.70 --> 2854.66]  to climb that ladder
[2854.66 --> 2855.92]  it does open up a lot
[2855.92 --> 2856.72]  of really interesting
[2856.72 --> 2857.22]  things.
[2858.38 --> 2859.02]  You know, I
[2859.02 --> 2860.34]  definitely have been
[2860.34 --> 2861.26]  called in more than
[2861.26 --> 2862.78]  wants to like sort
[2862.78 --> 2864.18]  of recover like oh
[2864.18 --> 2864.98]  my god I feel like I
[2864.98 --> 2866.02]  lost my code or oh
[2866.02 --> 2866.88]  what happened here.
[2867.12 --> 2867.24]  Yeah.
[2867.36 --> 2868.04]  And just like
[2868.04 --> 2869.06]  understanding how
[2869.06 --> 2870.58]  Git works even if
[2870.58 --> 2871.68]  you don't necessarily
[2871.68 --> 2873.40]  know all of the
[2873.40 --> 2874.24]  different commands but
[2874.24 --> 2874.76]  if you have that
[2874.76 --> 2876.08]  if you're willing to
[2876.08 --> 2876.84]  put in the work to
[2876.84 --> 2878.10]  build that mental
[2878.10 --> 2879.16]  model of like what
[2879.16 --> 2880.20]  actually is happening
[2880.20 --> 2881.12]  and where are these
[2881.12 --> 2881.92]  things and how can
[2881.92 --> 2882.58]  what are the many
[2882.58 --> 2883.54]  ways that I can find
[2883.54 --> 2884.18]  and get to them.
[2884.62 --> 2886.44]  It does have benefits
[2886.44 --> 2887.22]  that flow out.
[2887.96 --> 2888.98]  I think also when
[2888.98 --> 2889.64]  you're starting to have
[2889.64 --> 2890.82]  arguments around whether
[2890.82 --> 2892.22]  you should squash your
[2892.22 --> 2893.88]  commits or do a merge
[2893.88 --> 2894.80]  is when you're like
[2894.80 --> 2896.72]  okay I think I think
[2896.72 --> 2897.54]  I've leveled up my
[2897.54 --> 2899.04]  Git skills to a point
[2899.04 --> 2899.66]  where you can have an
[2899.66 --> 2901.40]  opinion on like one
[2901.40 --> 2902.16]  versus the other.
[2902.42 --> 2903.20]  Even if you're Nick
[2903.20 --> 2903.74]  and you have the wrong
[2903.74 --> 2904.08]  opinion.
[2905.24 --> 2906.30]  What does Nick think?
[2907.72 --> 2908.66]  Squash all the way.
[2909.00 --> 2910.20]  Oh yes I'm team
[2910.20 --> 2911.06]  squash too.
[2912.42 --> 2913.86]  Nick is a pronounced
[2913.86 --> 2915.78]  force pusher so you
[2915.78 --> 2916.90]  know who you're
[2916.90 --> 2917.36]  talking to.
[2917.50 --> 2918.28]  Know who you're
[2918.28 --> 2919.18]  alliancing with right
[2919.18 --> 2919.32]  here.
[2919.32 --> 2920.80]  I think I've had that
[2920.80 --> 2921.96]  opinion on teams before
[2921.96 --> 2922.82]  because I'm like I like
[2922.82 --> 2924.00]  clean history and they're
[2924.00 --> 2925.24]  like well clean history is
[2925.24 --> 2926.32]  like everything and I'm
[2926.32 --> 2927.12]  like that's not clean
[2927.12 --> 2927.96]  then you're like sorting
[2927.96 --> 2928.88]  through the garbage.
[2929.74 --> 2930.14]  Exactly.
[2931.54 --> 2933.02]  But often those are the
[2933.02 --> 2933.64]  people who think that
[2933.64 --> 2934.64]  haven't used get bisect.
[2935.32 --> 2936.68]  Often clean history is
[2936.68 --> 2938.00]  incorrect history.
[2939.30 --> 2940.06]  Yeah but like do you
[2940.06 --> 2940.96]  want to lie to your
[2940.96 --> 2941.86]  friends and family?
[2942.04 --> 2942.44]  Is that what you want to
[2942.44 --> 2942.54]  do?
[2942.54 --> 2944.28]  Most of history most of
[2944.28 --> 2946.08]  world history is not
[2946.08 --> 2946.82]  like raw.
[2947.46 --> 2948.90]  It's been cleaned up and
[2948.90 --> 2949.82]  like it's written by the
[2949.82 --> 2950.08]  winners.
[2950.26 --> 2950.50]  Exactly.
[2950.50 --> 2951.02]  Which is why it can't be
[2951.02 --> 2951.50]  believed.
[2951.68 --> 2952.38]  Yeah exactly it's
[2952.38 --> 2952.92]  untrustworthy.
[2953.58 --> 2954.62]  I want to show things the
[2954.62 --> 2955.42]  way that they should have
[2955.42 --> 2955.70]  gone.
[2956.24 --> 2956.52]  Right.
[2956.76 --> 2957.78]  Which could make it very
[2957.78 --> 2959.02]  hard to track down what
[2959.02 --> 2959.52]  went wrong.
[2960.00 --> 2962.20]  Anyway we're way off the
[2962.20 --> 2963.28]  rails here but it sounds
[2963.28 --> 2964.72]  like Jared and I are on
[2964.72 --> 2965.92]  one side of a holy debate
[2965.92 --> 2968.80]  and a holy war and Divya
[2968.80 --> 2969.68]  and Nick are on another.
[2969.78 --> 2970.70]  We may have just found our
[2970.70 --> 2971.86]  next segment idea.
[2980.86 --> 2982.04]  This episode is brought
[2982.04 --> 2982.98]  to you by Gauge.
[2983.22 --> 2984.98]  Gauge is a free and open
[2984.98 --> 2986.04]  source test automation tool
[2986.04 --> 2986.82]  by ThoughtWorks.
[2986.94 --> 2988.38]  The goal of the tool is to
[2988.38 --> 2989.28]  take the pain out of test
[2989.28 --> 2990.56]  automation and to help
[2990.56 --> 2991.52]  with this Gauge support
[2991.52 --> 2992.92]  specifications of Markdown
[2992.92 --> 2994.36]  which are easy to read and
[2994.36 --> 2995.14]  easy to write.
[2995.54 --> 2996.96]  Reusable specifications to
[2996.96 --> 2998.28]  simplify your code which
[2998.28 --> 2999.90]  makes refactoring easier and
[2999.90 --> 3000.60]  less code.
[3000.70 --> 3002.06]  means less time maintaining
[3002.06 --> 3002.50]  code.
[3002.86 --> 3004.06]  And finally integrations.
[3004.22 --> 3005.22]  Use Gauge with your
[3005.22 --> 3006.04]  favorite tools and your
[3006.04 --> 3007.12]  IDEs and the ecosystem of
[3007.12 --> 3007.72]  your choice.
[3008.20 --> 3010.32]  Selenium, SciHeapro, CIC and
[3010.32 --> 3012.00]  CD tools like GoCD, Jenkins,
[3012.18 --> 3014.14]  Travis and IDE support for
[3014.14 --> 3015.54]  Visual Studio, VS Code,
[3015.66 --> 3016.54]  IntelliJ and more.
[3016.86 --> 3018.50]  Head to gauge.org slash jsparty
[3018.50 --> 3019.32]  to learn more and give it a
[3019.32 --> 3019.66]  try.
[3019.90 --> 3022.32]  Again gauge.org slash jsparty.
[3022.32 --> 3032.34]  Okay folks, one of our favorite
[3032.34 --> 3034.10]  segments is shout outs.
[3034.18 --> 3035.30]  This is a great opportunity for
[3035.30 --> 3038.22]  us to shout out and thank or
[3038.22 --> 3040.76]  give props to a person, people,
[3041.00 --> 3042.90]  a project, anything really that
[3042.90 --> 3045.08]  we think deserves some shout
[3045.08 --> 3046.26]  outs and maybe hasn't got them,
[3046.36 --> 3047.86]  maybe has, but we all like to
[3047.86 --> 3048.28]  take a turn.
[3048.36 --> 3049.30]  So let's start off with K-Ball.
[3049.30 --> 3050.80]  Give us your shout outs.
[3051.32 --> 3051.68]  All right.
[3051.80 --> 3053.36]  So I want to shout out a
[3053.36 --> 3054.68]  category and then I'm going to
[3054.68 --> 3055.62]  shout out three particular
[3055.62 --> 3056.16]  examples.
[3056.50 --> 3057.98]  So the category that I want to
[3057.98 --> 3060.86]  shout out is people who are
[3060.86 --> 3062.80]  doing work to kind of bridge
[3062.80 --> 3065.38]  between design and development
[3065.38 --> 3068.36]  and sort of emphasize UI
[3068.36 --> 3070.46]  centric and design centric
[3070.46 --> 3071.42]  front end development.
[3071.94 --> 3074.08]  Because this is a place where
[3074.08 --> 3077.04]  stuff often goes wrong and
[3077.04 --> 3079.10]  we've had whole conversations
[3079.10 --> 3081.18]  about challenges even within
[3081.18 --> 3082.00]  the front end development
[3082.00 --> 3084.44]  space, the divide and
[3084.44 --> 3085.24]  various other things.
[3085.48 --> 3087.76]  But there's a lot of people
[3087.76 --> 3089.08]  doing yeoman's work here.
[3089.32 --> 3091.38]  So three particular people and
[3091.38 --> 3092.38]  instances I'm going to shout
[3092.38 --> 3092.60]  out.
[3092.98 --> 3094.68]  First, there was a recent
[3094.68 --> 3096.36]  article on Smashing Magazine
[3096.36 --> 3098.44]  by Stefan Kaltenegger.
[3098.96 --> 3100.76]  I probably butchered his name,
[3101.28 --> 3103.72]  but he did this article on
[3103.72 --> 3106.76]  essentially how you can work to
[3106.76 --> 3108.26]  bridge the gap between designers
[3108.26 --> 3108.86]  and developers.
[3108.86 --> 3110.50]  And it's just kind of a nice
[3110.50 --> 3113.26]  kind of walkthrough of things
[3113.26 --> 3115.16]  that you can do as a developer
[3115.16 --> 3116.18]  or as a designer.
[3116.98 --> 3118.96]  I think more focused on the
[3118.96 --> 3120.84]  developer to kind of help
[3120.84 --> 3121.58]  bridge that gap.
[3121.68 --> 3122.94]  And it also referenced out to a
[3122.94 --> 3124.06]  cool resource that I hadn't seen
[3124.06 --> 3125.54]  before called Can't Unsee,
[3125.66 --> 3126.58]  which gives you practice
[3126.58 --> 3128.96]  developing your design eye.
[3130.20 --> 3132.42]  So that's one of the three people
[3132.42 --> 3133.24]  I'm going to shout out on this
[3133.24 --> 3133.54]  subject.
[3133.54 --> 3135.60]  The next one is Ryan Singer,
[3136.14 --> 3139.06]  who wrote an article on the
[3139.06 --> 3141.62]  Signal vs. Noise blog recently
[3141.62 --> 3143.44]  about the place of UX and
[3143.44 --> 3145.42]  looking at alternative ways of
[3145.42 --> 3146.84]  thinking about user experiences,
[3147.04 --> 3148.32]  essentially being the boundary
[3148.32 --> 3149.98]  between any two things that are
[3149.98 --> 3151.34]  supply and demand.
[3151.46 --> 3153.82]  So one was talking about, okay,
[3153.82 --> 3154.86]  between the user and the product,
[3154.86 --> 3155.98]  that's where we usually think about
[3155.98 --> 3156.12]  it.
[3156.12 --> 3158.30]  But actually, this concept of design
[3158.30 --> 3160.40]  is really important at every place
[3160.40 --> 3161.30]  where you have interactions
[3161.30 --> 3162.34]  between different groups.
[3163.48 --> 3166.06]  So I think that was really cool.
[3166.22 --> 3168.12]  And then the final shout out I'm
[3168.12 --> 3170.64]  going to do is for a conference
[3170.64 --> 3172.84]  that my friend Dylan Scheman is
[3172.84 --> 3174.28]  involved with organizing.
[3174.92 --> 3176.66]  So conference organizers in general
[3176.66 --> 3177.38]  deserve shout outs.
[3177.48 --> 3179.60]  But this one in particular is a
[3179.60 --> 3180.64]  conference called HalfStack,
[3180.64 --> 3185.16]  which is focused on UI-centric
[3185.16 --> 3186.44]  front-end development.
[3186.84 --> 3188.60]  And they are expanding from being
[3188.60 --> 3190.10]  only in London to having events
[3190.10 --> 3191.74]  in Vienna, New York, and Phoenix,
[3192.04 --> 3193.18]  and various other things.
[3193.34 --> 3195.68]  So super cool to see this kind of
[3195.68 --> 3197.46]  UI-focused development stuff
[3197.46 --> 3200.84]  growing and being more present
[3200.84 --> 3201.62]  around the world.
[3201.62 --> 3204.44]  So props to those three people,
[3204.62 --> 3207.04]  to Stefan Kaltenegger, Ryan Singer,
[3207.36 --> 3209.22]  and Dylan Scheman, all of whose names
[3209.22 --> 3210.02]  I probably butchered.
[3210.64 --> 3211.38]  K-ball the butcher.
[3212.02 --> 3213.00]  All right, Divya, your turn.
[3213.42 --> 3213.70]  Awesome.
[3214.64 --> 3217.50]  So I'm going to shout out to a conference.
[3218.54 --> 3221.28]  And someone on this panel is organizing it.
[3222.60 --> 3224.62]  NEJS, which is really cool.
[3224.88 --> 3228.54]  And I've spoken at NEJS two years ago.
[3228.74 --> 3230.74]  And it was actually my first conference
[3230.74 --> 3231.18]  talk.
[3232.12 --> 3234.90]  And I feel like the organizers were so cool
[3234.90 --> 3235.56]  and awesome.
[3235.92 --> 3238.00]  And the conference itself was wonderful.
[3238.36 --> 3239.96]  It wasn't at the zoo, which it is going
[3239.96 --> 3243.14]  to be this year, which is super exciting.
[3243.34 --> 3246.00]  Also, the theme I'm so excited about.
[3247.60 --> 3248.08]  Yes.
[3248.52 --> 3250.22]  It's Life Aquatic.
[3250.92 --> 3252.10]  And it's so cool.
[3252.32 --> 3252.60]  Yes.
[3252.60 --> 3254.42]  And I heard someone's going to dress up
[3254.42 --> 3255.52]  as Steve Zissou.
[3257.58 --> 3258.02]  Yes.
[3259.90 --> 3261.48]  Who is this someone you keep referring to?
[3261.52 --> 3261.92]  I don't know.
[3261.98 --> 3262.72]  Could it be Nick Nisi?
[3263.84 --> 3264.70]  Could it be?
[3265.48 --> 3267.14]  I'm more interested in who's going to be
[3267.14 --> 3269.12]  the jaguar shark more than anything.
[3269.80 --> 3270.52]  I want to know.
[3272.88 --> 3274.54]  I feel like we have to get that done now.
[3274.62 --> 3275.88]  I feel like Nick will just come out with
[3275.88 --> 3277.90]  his kids dressed as a jaguar shark.
[3279.08 --> 3280.22]  That'd be so cute.
[3280.60 --> 3281.00]  Perfection.
[3281.00 --> 3283.18]  Baby shark.
[3285.18 --> 3285.50]  Yes.
[3285.58 --> 3285.94]  Yes.
[3286.94 --> 3288.06]  Oh, no, no, no.
[3288.06 --> 3288.92]  Well, thank you, Divi.
[3289.42 --> 3290.32]  Yeah, please don't.
[3290.56 --> 3291.08]  Please don't.
[3291.32 --> 3292.16]  Oh, it's too late.
[3292.38 --> 3293.08]  Yeah, I know.
[3293.22 --> 3294.86]  Once it's in your head, you can't get it out.
[3295.10 --> 3298.06]  And then this is like another shout out
[3298.06 --> 3301.14]  to a tool that Rose Bay mentioned
[3301.14 --> 3303.82]  on the chat, which is like Quokka.js.
[3304.52 --> 3305.98]  And I think so.
[3306.12 --> 3307.96]  It's interesting because this is a tool
[3307.96 --> 3309.28]  that I recently heard about.
[3310.00 --> 3312.02]  And like, it's funny that he posted it as well.
[3312.22 --> 3314.34]  So I was at Nation.js, which is a small conference,
[3314.54 --> 3316.36]  also really great, in D.C.
[3316.98 --> 3320.04]  And Nir Kaufman was one of the speakers.
[3320.42 --> 3323.10]  And he's big in the React community in New York.
[3323.78 --> 3326.16]  And he spoke about Quokka.
[3326.16 --> 3328.18]  And it was so, I had never heard of it.
[3328.22 --> 3329.28]  And I think it's really cool
[3329.28 --> 3331.00]  because it allows you to like prototype.
[3331.24 --> 3332.34]  It's like a scratch pad
[3332.34 --> 3334.34]  for when you're like working on stuff.
[3334.68 --> 3336.98]  And so you're like, oh, wait, I'm looking at,
[3337.24 --> 3338.58]  I'm working with this like library
[3338.58 --> 3339.66]  and I don't know how it works.
[3339.68 --> 3341.34]  And then you can like kind of just use it
[3341.34 --> 3342.30]  as a scratch pad to be like,
[3342.34 --> 3343.52]  let me try different things.
[3343.70 --> 3345.28]  And then like erase it when you're done
[3345.28 --> 3347.32]  without having to like mess up your files.
[3347.98 --> 3350.76]  I think it's so cool and interesting
[3350.76 --> 3354.52]  because like even the way that it was presented to me
[3354.52 --> 3355.52]  was like, oh, like,
[3356.16 --> 3358.04]  most of the time you look at a framework
[3358.04 --> 3359.40]  and you look at the documentation
[3359.40 --> 3361.58]  and then that's how you learn how it works.
[3361.58 --> 3363.30]  Like a library like Lodash, for example.
[3363.84 --> 3364.62]  But with this, it's like,
[3364.64 --> 3367.14]  you can actually work on the thing,
[3367.28 --> 3368.38]  which I've done before.
[3368.52 --> 3372.24]  Like I've used RunKit and like various things,
[3372.24 --> 3374.36]  which is like on NPM where you're like,
[3374.44 --> 3376.52]  okay, I want to like play around with this tool
[3376.52 --> 3378.08]  and see what things are doing.
[3378.18 --> 3379.26]  But I think Quokka allows you
[3379.26 --> 3380.68]  to kind of dig really deep
[3380.68 --> 3382.94]  into a specific library or tool,
[3383.08 --> 3385.06]  which is so interesting and neat.
[3385.06 --> 3386.94]  Just like from a learning perspective,
[3387.18 --> 3388.74]  you want to like going back to the conversation
[3388.74 --> 3389.82]  of like scaling up,
[3390.22 --> 3392.40]  be like, I'm a junior developer to be like,
[3392.48 --> 3393.68]  I want to progress.
[3393.82 --> 3395.94]  I think that's like such a great tool for you
[3395.94 --> 3398.36]  to just like learn about how tools are created,
[3398.70 --> 3400.82]  how libraries are architected, so on.
[3401.34 --> 3402.30]  And then the last thing,
[3402.38 --> 3402.82]  which is like,
[3403.20 --> 3406.26]  so I really like shaders in like just for fun.
[3406.48 --> 3407.90]  They don't really do anything for me
[3407.90 --> 3410.84]  in terms of like getting me money or a job.
[3410.84 --> 3412.98]  They're doing something.
[3413.16 --> 3415.14]  Well, I get excited about them
[3415.14 --> 3416.16]  because I think they're really cool
[3416.16 --> 3417.80]  and interesting and totally different.
[3418.30 --> 3420.02]  Because I also like thinking
[3420.02 --> 3422.78]  and doing things outside of what I normally do.
[3423.46 --> 3425.08]  It's always nice to switch gears.
[3426.10 --> 3428.50]  And so sometimes in my free time,
[3428.56 --> 3430.96]  I work on like WebGL and like GLSL,
[3431.16 --> 3432.74]  which is like the shader language for the web.
[3433.36 --> 3434.08]  Super cool.
[3434.08 --> 3437.44]  And there's a library that I recently heard of
[3437.44 --> 3438.54]  called Blotter.js,
[3439.36 --> 3443.36]  which is a JavaScript API for drawing like text effects.
[3443.72 --> 3444.64]  And it's so cool.
[3445.44 --> 3449.74]  And it's done by someone at this hacker school
[3449.74 --> 3451.40]  that I went to called Recurse Center.
[3451.60 --> 3454.42]  Also a shout out because Recurse Center is awesome.
[3455.18 --> 3456.18]  You've never heard of it.
[3456.48 --> 3459.56]  It's like a retreat for developers.
[3460.16 --> 3463.02]  So if you're just like trying to find your groove,
[3463.02 --> 3465.84]  you need like to be around other people
[3465.84 --> 3468.04]  who are working on really easy things to apply.
[3468.68 --> 3471.06]  And the idea is that you can work on like
[3471.06 --> 3472.30]  a week or a month.
[3472.84 --> 3474.70]  No, actually it's a week, three months,
[3474.96 --> 3476.56]  or I forget the time span.
[3476.64 --> 3477.46]  I did it for a week.
[3478.28 --> 3479.94]  So it's very like low stakes.
[3480.06 --> 3482.18]  You can just take a week off of work, go there,
[3482.26 --> 3484.06]  and you get to work on like a project
[3484.06 --> 3485.24]  that you're really interested in.
[3485.34 --> 3488.66]  So for me, I worked on like WebGL and shaders,
[3488.80 --> 3490.74]  which is like something I don't normally do.
[3490.74 --> 3494.06]  And be surrounded by like super smart people
[3494.06 --> 3495.80]  and like learn about different things.
[3496.00 --> 3496.92]  And yeah.
[3497.26 --> 3500.12]  So that like definitely like Recurse is a huge shout out.
[3500.94 --> 3502.98]  And the community is awesome as well.
[3503.12 --> 3504.76]  If you like want to just plug into like
[3504.76 --> 3506.22]  a community of developers
[3506.22 --> 3508.26]  who are really excited about what they do.
[3508.54 --> 3512.08]  That's like not Twitter because like Twitter has that,
[3512.26 --> 3513.94]  but it's also like you have to like
[3513.94 --> 3515.48]  kind of sort through the garbage
[3515.48 --> 3517.10]  because you can't squash, you know,
[3517.18 --> 3518.24]  on Twitter or whatever.
[3518.24 --> 3521.66]  But yeah, so that those are my shout outs.
[3522.26 --> 3522.52]  Very good.
[3522.56 --> 3524.88]  Well, we appreciate the NEJS shout out.
[3524.96 --> 3526.06]  Nick, give the pitch here.
[3526.10 --> 3527.26]  We got tickets for sale.
[3527.54 --> 3529.14]  Well, what's the situation on NEJS?
[3529.92 --> 3530.76]  Tickets for sale.
[3530.84 --> 3531.80]  It's August 9th.
[3532.26 --> 3534.92]  Our early bird tickets are going right now
[3534.92 --> 3537.62]  and you can pick them up at nejsconf.com.
[3538.14 --> 3541.10]  I would say that our CFP is still open,
[3541.36 --> 3543.56]  but by the time this goes out, it will not be.
[3543.56 --> 3544.12]  Yeah.
[3544.36 --> 3548.16]  But that's okay because we have a lot of awesome proposals
[3548.16 --> 3548.98]  that have been submitted
[3548.98 --> 3552.38]  and we're really looking forward to the painstaking task
[3552.38 --> 3554.50]  of having to say no to so many of them
[3554.50 --> 3556.52]  because that's always the toughest part
[3556.52 --> 3557.74]  of being a conference organizer.
[3558.08 --> 3562.10]  But otherwise, it's August 9th at the Henry Dorley Zoo,
[3562.32 --> 3563.86]  the number one zoo in the world.
[3564.62 --> 3566.46]  And according to many places.
[3566.84 --> 3567.80]  I think so.
[3568.00 --> 3569.24]  At least it was at one point,
[3569.34 --> 3570.84]  but they're constantly...
[3570.84 --> 3571.38]  In the 80s.
[3571.40 --> 3571.82]  No, just kidding.
[3571.82 --> 3574.24]  Yeah, it's really cool.
[3574.44 --> 3575.64]  At least in America, for sure.
[3575.76 --> 3577.22]  Maybe in the world, I believe you, Nick.
[3577.28 --> 3578.42]  But it's a spectacular zoo.
[3579.04 --> 3580.58]  While we're talking conferences real quick,
[3580.68 --> 3581.80]  I'll get over to you here, Nick.
[3581.88 --> 3585.34]  I wanted to mention all things open this fall in October.
[3585.82 --> 3589.40]  There will be a large portion of changelog folks
[3589.40 --> 3590.62]  at that conference.
[3590.78 --> 3592.98]  So if you're going to be there, give us a shout out.
[3593.02 --> 3593.54]  Let us know.
[3593.68 --> 3595.30]  We might organize something like a meetup
[3595.30 --> 3596.56]  or a live show or something.
[3596.64 --> 3598.40]  There'll be a lot of JS Party people there as well.
[3599.00 --> 3600.66]  So just want to give everybody a heads up
[3600.66 --> 3602.02]  that all things open in October.
[3602.16 --> 3602.82]  It's in North Carolina.
[3603.22 --> 3605.28]  It's a thing that we'll have representation.
[3605.62 --> 3607.08]  We'd love to come out and see everybody
[3607.08 --> 3608.76]  and come say hi.
[3608.92 --> 3610.72]  So that's just a quick one there.
[3610.88 --> 3612.30]  Back to you, Nick, on your shout outs.
[3612.92 --> 3615.20]  Wait, I want to chime in on the zoo really quick
[3615.20 --> 3616.74]  as a former San Diego resident.
[3617.60 --> 3620.54]  My gosh, San Diego Zoo is the best.
[3621.00 --> 3621.94]  Sorry, sorry, sorry.
[3622.60 --> 3623.42]  Second best.
[3623.42 --> 3626.90]  I don't know how to judge
[3626.90 --> 3629.44]  because I have not actually been to the Omaha Zoo.
[3629.86 --> 3631.74]  However, I did look up a little bit
[3631.74 --> 3635.00]  of the statistics on them
[3635.00 --> 3638.88]  and it looks like by, when was this?
[3638.98 --> 3641.68]  At least in a number of years back,
[3642.12 --> 3646.20]  by a number of 5 million a year to 1 million a year,
[3646.46 --> 3647.86]  there are a lot more people
[3647.86 --> 3649.94]  who think the San Diego Zoo is a place worth going.
[3649.94 --> 3653.88]  Now we got a new ground war here.
[3654.06 --> 3658.52]  We got get styles and zoos we can go back and forth on.
[3659.00 --> 3660.00]  That might just be a statement
[3660.00 --> 3661.62]  about San Diego versus Omaha.
[3661.96 --> 3662.82]  I think it probably is.
[3662.82 --> 3663.56]  There's a lot more people.
[3664.58 --> 3665.88]  San Diego has pretty nice weather.
[3666.16 --> 3667.64]  But in San Diego, I haven't been to that zoo,
[3667.68 --> 3668.80]  but I've also heard a great zoo.
[3669.52 --> 3671.54]  So there's room in the world
[3671.54 --> 3672.60]  for more than one awesome zoo,
[3672.68 --> 3673.26]  but ours is the best.
[3673.34 --> 3674.02]  All right, Nick, your turn.
[3675.52 --> 3675.88]  Yeah.
[3677.08 --> 3678.58]  So my shout outs,
[3678.58 --> 3679.92]  I'm going to shout out to
[3679.92 --> 3682.10]  Rene Rubelkava,
[3682.34 --> 3683.90]  and I might be mispronouncing his name,
[3684.04 --> 3685.78]  but he's a really cool guy who works at Esri,
[3686.02 --> 3689.74]  and he runs a website called Learn-Dojo,
[3689.94 --> 3690.88]  and he's just putting out
[3690.88 --> 3692.94]  these really cool tutorials
[3692.94 --> 3696.62]  on different parts of using new dojo,
[3696.86 --> 3698.30]  and it's just really great,
[3698.32 --> 3699.62]  really great to see that out in the community,
[3699.90 --> 3701.94]  and they're really great tutorials as well.
[3702.12 --> 3704.86]  So shout out to Rene for doing that.
[3704.86 --> 3710.00]  And then I just have to shout out to Tim Pope,
[3710.46 --> 3712.84]  and specifically for his Vim Fugitive plugin,
[3713.10 --> 3713.64]  it's just,
[3714.32 --> 3717.30]  I just recently learned about the G command.
[3717.78 --> 3719.44]  I don't know when that got added,
[3719.54 --> 3722.34]  but I've been using like Gstatus,
[3722.70 --> 3724.36]  and you know,
[3724.48 --> 3724.86]  Gread,
[3725.08 --> 3726.26]  and all of these commands
[3726.26 --> 3729.48]  to work for the most part with Git,
[3730.02 --> 3731.90]  but then I just go back to the command line for things.
[3731.90 --> 3733.46]  And with G,
[3733.64 --> 3736.62]  you can look at diffs of your commands
[3736.62 --> 3738.78]  and then stage those individual hunks
[3738.78 --> 3739.82]  right from there,
[3739.90 --> 3740.64]  right from within Vim,
[3740.70 --> 3741.60]  and you never have to leave,
[3741.72 --> 3743.42]  and it's just so nice to be able to curate
[3743.42 --> 3745.24]  your Git commits and commit messages
[3745.24 --> 3747.08]  all without ever having to leave Vim.
[3747.22 --> 3748.62]  So thank you, Tim Pope, for that.
[3749.18 --> 3749.78]  All right,
[3749.84 --> 3751.90]  last but not least is my shout outs,
[3752.04 --> 3753.24]  and I want to talk about something
[3753.24 --> 3754.30]  that maybe you know about,
[3754.34 --> 3755.04]  maybe you don't.
[3755.60 --> 3756.80]  It is GoTime.
[3756.92 --> 3758.62]  So you may know that we have another show
[3758.62 --> 3760.46]  that's very similar to this one called GoTime,
[3760.46 --> 3762.38]  and a lot like JS Party,
[3762.46 --> 3763.62]  where we had it going for a while,
[3763.74 --> 3765.16]  and we put JS Party on hiatus,
[3765.38 --> 3766.78]  and we try to change some things,
[3766.84 --> 3767.46]  make things better,
[3768.04 --> 3769.80]  and we relaunched with an expanded panel.
[3770.20 --> 3772.60]  We had a very similar situation with GoTime.
[3772.68 --> 3774.82]  So GoTime went on hiatus for almost a year,
[3775.22 --> 3776.94]  but I'm happy to say it's back now,
[3777.48 --> 3779.14]  and the panel is spectacular.
[3779.50 --> 3780.74]  You may know some of these names,
[3780.82 --> 3781.32]  Matt Reier,
[3781.42 --> 3782.20]  Ashley McNamara,
[3782.64 --> 3783.36]  Johnny Bersico,
[3783.56 --> 3784.44]  Carmen Ando,
[3784.82 --> 3785.40]  JBD,
[3786.12 --> 3787.06]  Yana Bidogan,
[3787.06 --> 3789.04]  and as well as Mark Bates.
[3789.04 --> 3790.62]  And I would just say,
[3790.70 --> 3792.46]  maybe there isn't too much overlap
[3792.46 --> 3794.60]  between JavaScript interest and Go interest,
[3794.76 --> 3796.80]  but the thing about GoTime is,
[3796.90 --> 3798.50]  it's not just about Go.
[3798.56 --> 3798.78]  In fact,
[3798.80 --> 3800.04]  we've rewritten the little blurb,
[3800.92 --> 3801.86]  which says that,
[3802.50 --> 3802.96]  now says,
[3803.04 --> 3804.48]  a diverse panel and special guests
[3804.48 --> 3805.78]  discuss cloud infrastructure,
[3806.14 --> 3806.94]  distributed systems,
[3807.12 --> 3807.68]  microservices,
[3807.88 --> 3808.24]  Kubernetes,
[3808.48 --> 3808.78]  Docker,
[3809.46 --> 3809.64]  oh,
[3809.70 --> 3810.40]  and also Go.
[3810.86 --> 3812.16]  So I am not a Go developer.
[3812.62 --> 3813.66]  I do have vested interest
[3813.66 --> 3814.70]  in GoTime being successful.
[3814.86 --> 3815.46]  That being said,
[3815.52 --> 3817.02]  I don't have much to do with this show at all,
[3817.02 --> 3818.28]  besides I listen to it.
[3818.60 --> 3820.16]  And it's a lot like JS Party now.
[3820.52 --> 3821.64]  It's a ton of fun.
[3822.04 --> 3823.28]  The new panel is spectacular.
[3823.90 --> 3825.42]  And they put out some really,
[3825.80 --> 3826.80]  really good shows.
[3826.88 --> 3828.18]  The last one was Gopher Beginners.
[3828.60 --> 3829.74]  Very similar to conversations
[3829.74 --> 3830.34]  that we're having here
[3830.34 --> 3831.38]  about getting into JavaScript
[3831.38 --> 3832.24]  and learning those things.
[3832.62 --> 3834.02]  But I specifically want to mention
[3834.02 --> 3835.26]  episode 84,
[3835.44 --> 3836.72]  Hardware Hacking with TinyGo
[3836.72 --> 3837.66]  and GopherBot,
[3838.16 --> 3840.96]  in which Matt interviewed Ron Evans,
[3841.50 --> 3842.60]  aka DeadProgram,
[3842.60 --> 3845.16]  who is just a very entertaining guy
[3845.16 --> 3846.42]  and has tons of information
[3846.42 --> 3847.20]  all about robotics.
[3847.84 --> 3849.22]  He started the GoBot project
[3849.22 --> 3850.58]  as well as the,
[3851.00 --> 3851.62]  there was a Ruby
[3851.62 --> 3852.92]  and a JavaScript version as well.
[3854.20 --> 3855.56]  And so that's just a spectacular
[3855.56 --> 3857.52]  way of getting to know that show.
[3857.60 --> 3858.40]  So I just wanted to thank
[3858.40 --> 3859.60]  the new panelists
[3859.60 --> 3861.36]  and say if you haven't heard of GoTime
[3861.36 --> 3863.94]  or you gave it to Alyssa a while ago,
[3864.04 --> 3865.52]  it's now a good time
[3865.52 --> 3866.32]  to check it back out
[3866.32 --> 3868.04]  because it's filled with
[3868.04 --> 3869.06]  very awesome people.
[3869.14 --> 3870.00]  So I want to thank them
[3870.00 --> 3871.68]  and yeah,
[3871.68 --> 3872.86]  excited to have GoTime back.
[3873.52 --> 3875.04]  The logo is so cool.
[3875.64 --> 3875.90]  Like,
[3876.32 --> 3878.26]  I'm just looking at the mesh thing.
[3878.74 --> 3879.62]  So cool.
[3879.94 --> 3880.14]  Yeah.
[3880.64 --> 3881.98]  Yeah, a little gopher hidden in there.
[3882.44 --> 3882.76]  All right.
[3882.78 --> 3883.50]  Any final words
[3883.50 --> 3884.46]  before we call it a day?
[3884.94 --> 3885.46]  There's nothing wrong
[3885.46 --> 3886.02]  with force push.
[3891.36 --> 3892.62]  In certain circumstances.
[3894.22 --> 3895.38]  Why'd I have to ask?
[3896.52 --> 3897.28]  You should have said
[3897.28 --> 3898.18]  everyone but Nick.
[3900.00 --> 3901.54]  I'm going to end the show now
[3901.54 --> 3902.68]  before K-Ball starts talking
[3902.68 --> 3903.98]  about San Diego Zoo again.
[3904.18 --> 3904.32]  Okay.
[3905.14 --> 3906.10]  Thank you everybody
[3906.10 --> 3907.40]  for sticking with us.
[3907.44 --> 3908.64]  This has been a lot of fun.
[3908.96 --> 3909.62]  As always,
[3909.98 --> 3910.90]  more shows like this
[3910.90 --> 3911.90]  at changelaw.com
[3911.90 --> 3912.64]  slash JS Party.
[3912.74 --> 3913.36]  Hey, do us a favor.
[3913.90 --> 3914.68]  If you like this show,
[3914.74 --> 3915.38]  especially for people
[3915.38 --> 3916.58]  who are getting into the space,
[3916.68 --> 3916.92]  learning,
[3917.54 --> 3918.98]  give us a recommendation.
[3919.32 --> 3920.40]  We would really appreciate it.
[3920.70 --> 3922.10]  We love word of mouth.
[3922.32 --> 3923.66]  That means we're doing a good job
[3923.66 --> 3924.74]  putting out good content for you
[3924.74 --> 3926.28]  and that is actually still,
[3926.38 --> 3927.46]  even with all the technology
[3927.46 --> 3928.00]  that we have
[3928.00 --> 3929.06]  and all the social networks,
[3929.06 --> 3930.50]  word of mouth referrals
[3930.50 --> 3931.64]  is still the best way
[3931.64 --> 3932.84]  that people find
[3932.84 --> 3934.02]  and listen to new podcasts.
[3934.24 --> 3935.56]  So we appreciate you doing that.
[3935.62 --> 3936.40]  That's our show this week.
[3936.46 --> 3937.58]  We will see you next time.
[3939.40 --> 3939.92]  All right.
[3939.98 --> 3940.78]  Thank you for tuning in
[3940.78 --> 3941.82]  to JS Party this week.
[3941.94 --> 3942.52]  Tune in live
[3942.52 --> 3943.82]  on Thursdays
[3943.82 --> 3944.90]  at 1 p.m.
[3944.92 --> 3945.82]  U.S. Eastern
[3945.82 --> 3947.26]  at changelaw.com
[3947.26 --> 3947.98]  slash live.
[3948.46 --> 3948.88]  Join the community
[3948.88 --> 3949.58]  and Slack with us
[3949.58 --> 3950.20]  in real time
[3950.20 --> 3950.98]  during the shows.
[3951.14 --> 3952.20]  Head to changelaw.com
[3952.20 --> 3952.80]  slash community
[3952.80 --> 3954.08]  and do us a favor.
[3954.20 --> 3954.74]  Share this show
[3954.74 --> 3955.40]  with a friend.
[3955.72 --> 3956.60]  Read us an Apple podcast.
[3957.04 --> 3958.00]  Go into Overcast
[3958.00 --> 3958.66]  and favorite it.
[3959.14 --> 3960.38]  And thank you to Fastly,
[3960.46 --> 3961.40]  our bandwidth partner.
[3961.76 --> 3962.64]  Head to fastly.com
[3962.64 --> 3963.26]  to learn more.
[3963.66 --> 3964.32]  And we move fast
[3964.32 --> 3965.14]  to fix things around here
[3965.14 --> 3965.52]  at changelaw
[3965.52 --> 3966.28]  because of Rollbar.
[3966.54 --> 3967.18]  Check them out
[3967.18 --> 3968.24]  at rollbar.com.
[3968.48 --> 3969.08]  We're hosted
[3969.08 --> 3970.52]  on Leno cloud servers.
[3970.88 --> 3971.70]  Head to leno.com
[3971.70 --> 3972.48]  slash changelaw.
[3972.56 --> 3973.06]  Check them out
[3973.06 --> 3973.96]  and support this show.
[3974.38 --> 3975.28]  Our music is produced
[3975.28 --> 3976.36]  by Breakmaster Cylinder
[3976.36 --> 3977.84]  and you can find more shows
[3977.84 --> 3978.66]  just like this
[3978.66 --> 3979.82]  at changelaw.com.
[3980.10 --> 3980.94]  Thanks for tuning in.
[3980.94 --> 3982.00]  We'll see you next week.
[3988.00 --> 4017.98]  We'll see you next week.
[4017.98 --> 4018.30]  Curious.
[4018.44 --> 4018.82]  We're exploring
[4018.82 --> 4019.74]  the inner workings
[4019.74 --> 4020.58]  of the human brain
[4020.58 --> 4021.20]  so we can understand
[4021.20 --> 4022.62]  things like behavior change,
[4023.06 --> 4023.92]  habit formation,
[4024.52 --> 4025.24]  mental health,
[4025.44 --> 4026.04]  and this thing
[4026.04 --> 4027.18]  we call the human condition.
[4027.46 --> 4028.50]  It's hosted by myself,
[4028.64 --> 4029.60]  Adam Stachowiak,
[4029.82 --> 4030.68]  and Meryl Reese,
[4030.96 --> 4032.62]  a doctor in clinical psychology.
[4033.10 --> 4034.30]  It's brain science applied
[4034.30 --> 4035.72]  not just how does the brain work,
[4035.94 --> 4036.84]  but how do we apply
[4036.84 --> 4038.26]  what we know about the brain
[4038.26 --> 4039.54]  to better our lives.
[4040.08 --> 4040.48]  Here we go.
[4042.32 --> 4043.26]  As humans,
[4043.36 --> 4044.40]  one of the things
[4044.40 --> 4045.18]  that separates us
[4045.18 --> 4046.86]  from any other animal out there
[4046.86 --> 4048.24]  is the fact
[4048.24 --> 4049.14]  that we have language,
[4049.36 --> 4050.22]  we have words,
[4050.70 --> 4051.94]  and we have super powerful words
[4051.94 --> 4052.80]  that truly change
[4052.80 --> 4053.46]  how we feel
[4053.46 --> 4054.04]  and how we make
[4054.04 --> 4054.94]  other people feel.
[4055.36 --> 4056.86]  If the words we say
[4056.86 --> 4058.32]  have so much potential
[4058.32 --> 4059.82]  to influence ourselves
[4059.82 --> 4061.42]  and the world around us,
[4061.46 --> 4062.04]  how do we begin
[4062.04 --> 4062.56]  to understand
[4062.56 --> 4063.48]  the power of words?
[4063.92 --> 4065.40]  So words really are
[4065.40 --> 4066.60]  the thing that separates us
[4066.60 --> 4068.36]  from all other animals
[4068.36 --> 4070.12]  because, right,
[4070.26 --> 4072.22]  sharks, bats, dogs, lizards,
[4072.28 --> 4073.20]  they don't talk.
[4073.58 --> 4075.98]  And this is really critical
[4075.98 --> 4077.66]  when it comes to managing
[4077.66 --> 4080.40]  our moods and our feelings.
[4080.94 --> 4081.96]  One of the things
[4081.96 --> 4083.80]  that I sort of talk about
[4083.80 --> 4085.08]  or even I mentioned earlier
[4085.08 --> 4086.04]  about the way in which
[4086.04 --> 4087.68]  we file things in our mind
[4087.68 --> 4089.06]  according to feelings,
[4089.26 --> 4090.12]  this is exactly
[4090.12 --> 4091.70]  how we differentiate it too.
[4092.18 --> 4094.26]  Thinking about an example
[4094.26 --> 4096.94]  like with professional athletes,
[4096.94 --> 4098.56]  you might say
[4098.56 --> 4099.44]  that they get anxious
[4099.44 --> 4100.52]  like before a race
[4100.52 --> 4101.92]  or before, you know,
[4102.28 --> 4103.84]  a run or a dive.
[4104.12 --> 4105.60]  But using that word,
[4105.90 --> 4108.14]  it's not really a threat, right?
[4108.22 --> 4109.46]  But their brain would be like,
[4109.54 --> 4110.14]  oh, I'm nervous
[4110.14 --> 4110.86]  and now I start
[4110.86 --> 4112.16]  this whole sequence of events
[4112.16 --> 4113.28]  in my body.
[4113.50 --> 4115.38]  Whereas if I just change the word
[4115.38 --> 4116.88]  to like I'm anticipating
[4116.88 --> 4118.78]  or I'm excited,
[4119.60 --> 4121.54]  it creates a different
[4121.54 --> 4123.96]  sort of rollout of emotions
[4123.96 --> 4125.80]  as well as physiological responses.
[4125.80 --> 4127.60]  I mean, I'm anxious
[4127.60 --> 4129.04]  about going to Disneyland
[4129.04 --> 4131.16]  is not usually what we say, right?
[4131.38 --> 4131.90]  I'm excited.
[4133.12 --> 4133.68]  Exactly.
[4134.30 --> 4134.68]  Exactly.
[4134.84 --> 4136.72]  So it then puts a lid on
[4136.72 --> 4138.40]  or files things differently
[4138.40 --> 4139.74]  in our mind,
[4139.74 --> 4141.22]  which then changes
[4141.22 --> 4142.20]  how we feel about it.
[4142.56 --> 4144.86]  So in my field in psychology,
[4145.10 --> 4145.50]  I would say,
[4145.86 --> 4147.14]  we would say name it to tame it.
[4147.24 --> 4148.50]  The better I can name
[4148.50 --> 4149.54]  different feelings,
[4149.54 --> 4151.22]  the more I can tame
[4151.22 --> 4152.66]  whatever emotion that is.
[4153.14 --> 4154.82]  And so then I'm not really stuck
[4154.82 --> 4156.60]  living in this sort of mammal
[4156.60 --> 4157.58]  and reptile lane
[4157.58 --> 4158.58]  where I'm always just
[4158.58 --> 4159.56]  flipping my lid.
[4159.64 --> 4160.44]  I'm reactive.
[4160.74 --> 4162.48]  I'm angry or I'm sad.
[4162.64 --> 4164.20]  But rather I can go,
[4164.42 --> 4166.86]  I recognize this is how I'm feeling
[4166.86 --> 4168.32]  or like I'm afraid
[4168.32 --> 4170.46]  of some other threat,
[4170.62 --> 4172.04]  like losing my job.
[4172.32 --> 4173.68]  And I can go,
[4173.78 --> 4174.36]  you know what?
[4174.52 --> 4175.80]  Here's the words I can use
[4175.80 --> 4176.74]  to talk to myself
[4176.74 --> 4177.84]  about that fear
[4177.84 --> 4179.58]  so that I'm not just stuck
[4179.58 --> 4181.64]  feeling afraid
[4181.64 --> 4182.96]  of a possible threat,
[4183.02 --> 4184.04]  which has never occurred yet.
[4184.04 --> 4185.90]  You use this concept too
[4185.90 --> 4187.70]  to say customized thinking.
[4189.12 --> 4190.60]  I'm not sure I fully understand
[4190.60 --> 4192.06]  what you mean by customized thinking.
[4192.14 --> 4192.82]  What do you mean by that?
[4193.46 --> 4196.30]  Well, because we are human,
[4196.50 --> 4198.20]  we do have the power of choice,
[4198.28 --> 4200.54]  which is super powerful.
[4200.72 --> 4201.94]  Like nobody has to tell you
[4201.94 --> 4202.84]  how you need to think
[4202.84 --> 4204.52]  or how you need to feel, right?
[4204.62 --> 4206.42]  And like your version of success
[4206.42 --> 4208.58]  might be very different than mine,
[4208.58 --> 4210.12]  which is going to impact
[4210.12 --> 4211.76]  my choices
[4211.76 --> 4213.46]  and the direction I'm headed.
[4214.14 --> 4215.56]  And so when you think
[4215.56 --> 4216.66]  about customized, right?
[4216.74 --> 4218.60]  I mean, you can customize a car,
[4219.14 --> 4219.78]  you can customize
[4219.78 --> 4221.56]  your order at a restaurant.
[4222.16 --> 4224.36]  Like it really is tailored
[4224.36 --> 4225.88]  specifically to you
[4225.88 --> 4226.42]  and going,
[4226.62 --> 4227.98]  how do I want to think
[4227.98 --> 4229.00]  and how do I want to feel?
[4229.86 --> 4232.16]  One example I consider is
[4232.16 --> 4234.70]  I want to always,
[4235.38 --> 4236.58]  I want every day of the week
[4236.58 --> 4238.10]  to feel like I do on the weekend.
[4238.10 --> 4239.76]  Because to me,
[4239.82 --> 4240.78]  the weekend feels great.
[4240.90 --> 4242.22]  I'm with my family.
[4242.54 --> 4242.74]  I don't,
[4242.84 --> 4245.12]  I'm not sort of running things
[4245.12 --> 4246.66]  with such a tight timeline.
[4247.16 --> 4248.48]  And there's just a different
[4248.48 --> 4251.04]  sort of ethereal vibe
[4251.04 --> 4251.94]  to the weekend.
[4252.54 --> 4253.14]  And I think,
[4253.26 --> 4254.82]  why does that only have to exist
[4254.82 --> 4255.26]  on the weekend?
[4256.12 --> 4256.52]  Yeah.
[4256.66 --> 4257.58]  I want that every day.
[4257.60 --> 4258.20]  Why is that?
[4258.78 --> 4259.74]  I want that every day too.
[4261.62 --> 4262.90]  Well, and I think part of it
[4262.90 --> 4264.24]  is really our attitude
[4264.24 --> 4265.32]  and our expectations.
[4265.32 --> 4266.34]  I mean,
[4266.46 --> 4268.48]  there are legitimate threats
[4268.48 --> 4269.38]  all around us,
[4269.46 --> 4271.30]  but it doesn't help me
[4271.30 --> 4273.78]  do me or do my life any better
[4273.78 --> 4276.62]  if I am only focused on threats.
[4276.86 --> 4278.36]  So I want to practice
[4278.36 --> 4279.26]  changing the channel
[4279.26 --> 4280.54]  in my mind that says,
[4280.90 --> 4281.60]  hey, yeah,
[4281.80 --> 4283.36]  I see that potential job loss,
[4283.48 --> 4284.66]  but I also see
[4284.66 --> 4286.46]  I'm with my family right now.
[4286.50 --> 4288.06]  And right now,
[4288.46 --> 4289.56]  nobody can take
[4289.56 --> 4291.52]  sort of what I've been through
[4291.52 --> 4293.76]  and how I feel away from me.
[4293.76 --> 4295.56]  I'm in charge of how I feel.
[4296.16 --> 4297.18]  So I'm going to do things
[4297.18 --> 4298.22]  that actually contribute
[4298.22 --> 4299.80]  to feeling better.
[4300.18 --> 4301.44]  So how do we apply
[4301.44 --> 4303.02]  this name of the tainment idea
[4303.02 --> 4304.30]  to this model then?
[4304.62 --> 4306.36]  Because maybe if you name
[4306.36 --> 4307.08]  the week,
[4307.30 --> 4307.86]  the weekend,
[4308.08 --> 4309.08]  can you change
[4309.08 --> 4310.36]  how you feel about it?
[4310.62 --> 4311.24]  Because that's really
[4311.24 --> 4311.68]  what it's about.
[4311.74 --> 4311.86]  It's like,
[4311.90 --> 4313.32]  how do we take,
[4313.50 --> 4314.14]  you know,
[4314.20 --> 4315.80]  the labels we apply things
[4315.80 --> 4316.54]  to things,
[4317.10 --> 4318.30]  the names we give things,
[4318.40 --> 4319.40]  the words we use,
[4319.46 --> 4319.92]  the choices,
[4320.20 --> 4321.58]  what I think we might call nuance.
[4321.58 --> 4322.46]  I'm not really sure
[4322.46 --> 4325.02]  how you put that into play
[4325.02 --> 4326.00]  with the power of words,
[4326.10 --> 4327.90]  but the difference between,
[4328.18 --> 4329.12]  like you said before,
[4329.12 --> 4329.88]  being anxious
[4329.88 --> 4330.74]  or being excited,
[4332.04 --> 4332.20]  you know,
[4332.30 --> 4332.70]  fundamentally,
[4332.90 --> 4334.34]  it's almost the same feeling,
[4334.66 --> 4335.28]  but, you know,
[4335.32 --> 4336.32]  from a nuance level,
[4336.44 --> 4337.66]  it's very different.
[4337.98 --> 4338.10]  You know,
[4338.14 --> 4340.00]  it's one direction
[4340.00 --> 4341.26]  or the other of excitement,
[4341.76 --> 4341.94]  you know,
[4341.96 --> 4342.82]  negative excitement,
[4343.04 --> 4343.40]  potentially,
[4343.54 --> 4344.70]  or positive excitement.
[4345.02 --> 4345.68]  How do we apply that
[4345.68 --> 4346.82]  to customized thinking?
[4347.42 --> 4347.58]  Well,
[4347.76 --> 4349.08]  I think that's a great way
[4349.08 --> 4349.64]  to say it, Adam.
[4349.70 --> 4350.90]  I really like that nuance
[4350.90 --> 4353.70]  because what we're looking for,
[4354.16 --> 4355.62]  even as I talk about
[4355.62 --> 4356.68]  the different brains,
[4357.04 --> 4358.24]  we want a symphony.
[4358.62 --> 4358.82]  I mean,
[4358.84 --> 4359.84]  I'm not going to fire
[4359.84 --> 4361.04]  the woodwind section
[4361.04 --> 4362.14]  because I don't like a violin,
[4362.70 --> 4362.92]  right?
[4362.94 --> 4363.94]  So I don't want to fire
[4363.94 --> 4365.14]  a certain part of my brain,
[4365.20 --> 4365.40]  like,
[4365.48 --> 4366.30]  you're not really helpful.
[4366.60 --> 4367.74]  I don't need to see that.
[4368.34 --> 4369.46]  But what we need
[4369.46 --> 4372.50]  is a sense of congruence.
[4373.32 --> 4373.80]  And so,
[4374.08 --> 4374.30]  sure,
[4374.40 --> 4375.54]  not every day of the week
[4375.54 --> 4376.78]  can feel exactly
[4376.78 --> 4377.58]  like the weekend.
[4377.58 --> 4379.36]  So I'm not going to say
[4379.36 --> 4381.66]  this is how I feel,
[4381.86 --> 4383.20]  but I have to actually
[4383.20 --> 4383.88]  believe it
[4383.88 --> 4386.00]  for it to impact
[4386.00 --> 4387.98]  my mind,
[4388.30 --> 4388.76]  my brain,
[4388.82 --> 4389.38]  and my body
[4389.38 --> 4389.78]  in the way
[4389.78 --> 4390.98]  in which I desire it to.
[4391.86 --> 4392.92]  And so I might use
[4392.92 --> 4393.48]  the words like
[4393.48 --> 4394.78]  I strive
[4394.78 --> 4396.34]  for every day
[4396.34 --> 4398.20]  to have a feeling
[4398.20 --> 4399.74]  that reminds me
[4399.74 --> 4401.52]  of exactly how I feel
[4401.52 --> 4402.10]  on the weekend
[4402.10 --> 4403.80]  so that I don't lose sight
[4403.80 --> 4404.22]  that, like,
[4404.30 --> 4405.84]  every day really is a gift
[4405.84 --> 4407.20]  and I get to enjoy
[4407.20 --> 4409.04]  every day of my life
[4409.04 --> 4409.78]  to some degree.
[4410.66 --> 4411.12]  And so
[4411.12 --> 4413.12]  another example might be
[4413.12 --> 4414.90]  I'm living out
[4414.90 --> 4415.88]  in the Pacific Northwest.
[4416.14 --> 4417.14]  A lot of people have
[4417.14 --> 4418.22]  negative feelings
[4418.22 --> 4418.96]  about the weather.
[4419.62 --> 4420.30]  Imagine that.
[4421.24 --> 4421.66]  But
[4421.66 --> 4422.50]  so if someone
[4422.50 --> 4423.48]  were to say
[4423.48 --> 4425.14]  that they just need
[4425.14 --> 4426.42]  to learn to love it,
[4426.84 --> 4427.84]  that's going to create
[4427.84 --> 4428.46]  what we call
[4428.46 --> 4429.68]  cognitive dissonance.
[4429.76 --> 4430.52]  It doesn't fit.
[4430.94 --> 4431.58]  So it doesn't matter
[4431.58 --> 4432.32]  how much I'm like,
[4432.68 --> 4434.74]  oh, I do love the gray.
[4434.92 --> 4436.04]  I do love the clouds.
[4436.34 --> 4437.54]  It's not going to
[4437.54 --> 4438.42]  jive with me
[4438.42 --> 4439.58]  and so it won't stick.
[4440.02 --> 4440.66]  So instead,
[4440.92 --> 4441.66]  I can say
[4441.66 --> 4443.00]  I love
[4443.00 --> 4443.80]  the way
[4443.80 --> 4444.50]  in which
[4444.50 --> 4445.58]  the rain
[4445.58 --> 4446.68]  creates the green.
[4446.92 --> 4447.84]  And in the summer,
[4448.08 --> 4448.86]  when it is green,
[4448.96 --> 4449.78]  it is amazing.
[4450.46 --> 4451.60]  This idea of learning
[4451.60 --> 4452.48]  to live with it, though.
[4452.64 --> 4453.46]  Get over it.
[4453.98 --> 4455.32]  It is what it is.
[4455.46 --> 4456.36]  Like, there's so many
[4456.36 --> 4457.90]  phrases we use
[4457.90 --> 4458.70]  to say just that.
[4458.78 --> 4459.36]  Like, just learn
[4459.36 --> 4460.04]  to live with it.
[4460.32 --> 4461.02]  What is it called again?
[4461.64 --> 4462.74]  Cognitive dissonance.
[4463.10 --> 4463.78]  And what does that mean
[4463.78 --> 4464.50]  when you play it out?
[4465.00 --> 4466.16]  It doesn't go together.
[4466.26 --> 4466.46]  Okay.
[4466.52 --> 4467.60]  So that
[4467.60 --> 4468.46]  if you're like,
[4468.58 --> 4469.28]  oh, just
[4469.28 --> 4470.32]  just do it.
[4470.38 --> 4471.48]  You just need to get over it.
[4471.56 --> 4472.52]  Like, that really
[4472.52 --> 4473.52]  isn't helpful either
[4473.52 --> 4474.84]  because your body
[4474.84 --> 4475.76]  is giving you a signal
[4475.76 --> 4476.86]  and your brain
[4476.86 --> 4477.42]  is telling you,
[4477.52 --> 4478.94]  I don't like this sensation.
[4479.20 --> 4480.04]  I don't like
[4480.04 --> 4480.74]  how this feel.
[4480.82 --> 4481.64]  I mean, a lot of people
[4481.64 --> 4482.18]  will say,
[4482.60 --> 4484.28]  oh, I just hate the gray
[4484.28 --> 4484.84]  and the gray
[4484.84 --> 4485.92]  is just overwhelming.
[4486.78 --> 4487.58]  And so
[4487.58 --> 4488.98]  we have to go,
[4488.98 --> 4489.70]  well, what's my
[4489.70 --> 4490.88]  emotional buy-in?
[4491.30 --> 4493.40]  Like, what do I like?
[4493.46 --> 4495.32]  How does that even
[4495.32 --> 4497.06]  allow me to enjoy
[4497.06 --> 4497.86]  something else?
[4497.98 --> 4498.40]  And so
[4498.40 --> 4500.28]  I'm going to look at
[4500.28 --> 4501.68]  going,
[4501.84 --> 4502.20]  you know what?
[4502.22 --> 4502.92]  I really like that
[4502.92 --> 4504.40]  I get to wear warm clothes
[4504.40 --> 4504.84]  or
[4504.84 --> 4506.88]  I really do love my coffee
[4506.88 --> 4507.76]  because it's
[4507.76 --> 4509.30]  for such a long time
[4509.30 --> 4510.12]  it's gray and rainy
[4510.12 --> 4511.08]  I want to be inside
[4511.08 --> 4511.58]  by a fire
[4511.58 --> 4512.50]  drinking my coffee.
[4512.50 --> 4512.94]  Right.
[4513.16 --> 4513.68]  And so
[4513.68 --> 4514.82]  how can I look
[4514.82 --> 4515.16]  for going,
[4515.24 --> 4515.74]  you know what?
[4516.08 --> 4517.44]  If I do these things
[4517.44 --> 4519.38]  I might not want to do
[4519.38 --> 4521.00]  I do get some more
[4521.00 --> 4522.40]  of what I do want to do.
[4522.82 --> 4523.60]  And so it's really
[4523.60 --> 4525.54]  almost like a bartering system
[4525.54 --> 4526.44]  in your brain
[4526.44 --> 4527.32]  of saying
[4527.32 --> 4528.36]  if you do this thing
[4528.36 --> 4529.16]  you don't like
[4529.16 --> 4530.24]  you get this thing
[4530.24 --> 4531.34]  you do like
[4531.34 --> 4532.34]  or
[4532.34 --> 4533.14]  you know,
[4533.22 --> 4533.68]  I know
[4533.68 --> 4534.94]  you don't have to
[4534.94 --> 4536.04]  make yourself
[4536.04 --> 4537.12]  do this thing
[4537.12 --> 4539.00]  unless you can see
[4539.00 --> 4539.70]  a way in which
[4539.70 --> 4541.24]  it actually benefits you
[4541.24 --> 4541.94]  or
[4541.94 --> 4543.36]  speaks to you
[4543.36 --> 4543.96]  emotionally.
[4544.92 --> 4545.40]  Everything
[4545.40 --> 4546.88]  Adam really has to have
[4546.88 --> 4548.20]  this emotional buy-in
[4548.20 --> 4549.06]  and if
[4549.06 --> 4550.00]  there's no
[4550.00 --> 4551.34]  good emotion
[4551.34 --> 4552.18]  no
[4552.18 --> 4552.62]  really
[4552.62 --> 4553.76]  the primary
[4553.76 --> 4554.12]  neuro
[4554.12 --> 4555.36]  neurochemical in our brain
[4555.36 --> 4555.98]  is dopamine
[4555.98 --> 4557.28]  for feeling good
[4557.28 --> 4558.32]  I don't get
[4558.32 --> 4559.36]  some hit of dopamine
[4559.36 --> 4561.08]  my brain's going to be like
[4561.08 --> 4561.90]  it's not worth it
[4561.90 --> 4563.18]  and I'm not going to do it
[4563.18 --> 4563.98]  period.
[4567.30 --> 4568.20]  That's a preview
[4568.20 --> 4569.28]  of Brain Science.
[4569.28 --> 4570.30]  If you love where we're
[4570.30 --> 4571.02]  going with this
[4571.02 --> 4572.16]  send us an email
[4572.16 --> 4573.52]  to get on the list
[4573.52 --> 4574.44]  to be notified
[4574.44 --> 4575.86]  the very moment
[4575.86 --> 4576.94]  this show gets released
[4576.94 --> 4578.02]  email us
[4578.02 --> 4578.82]  at editors
[4578.82 --> 4580.40]  at changelog.com
[4580.40 --> 4581.28]  in the subject line
[4581.28 --> 4582.54]  put in all caps
[4582.54 --> 4583.70]  brain science
[4583.70 --> 4585.10]  with a couple bangs
[4585.10 --> 4585.96]  if you're really excited
[4585.96 --> 4587.36]  you can also subscribe
[4587.36 --> 4588.30]  to our master feed
[4588.30 --> 4589.30]  to get all of our shows
[4589.30 --> 4590.74]  in one single feed
[4590.74 --> 4592.36]  head to changelog.com
[4592.36 --> 4593.22]  slash master
[4593.22 --> 4594.42]  or search
[4594.42 --> 4595.76]  in your podcast app
[4595.76 --> 4596.64]  for changelog master
[4596.64 --> 4597.38]  you'll find it
[4597.38 --> 4597.92]  subscribe
[4597.92 --> 4599.02]  get all of our shows
[4599.02 --> 4600.14]  and even those
[4600.14 --> 4600.92]  that only hit
[4600.92 --> 4601.82]  the master feed
[4601.82 --> 4603.30]  again changelog.com
[4603.30 --> 4603.98]  slash master
[4603.98 --> 4612.50]  Wendy Lewis
[4612.50 --> 4617.66]  music
[4617.66 --> 4619.92]  music
[4619.92 --> 4649.90]  Thank you.
