[0.00 --> 3.26]  I'm Sid C. Brandy, and you're listening to The Change Log.
[12.08 --> 15.70]  Welcome back, everyone. This is The Change Log, and I'm your host, Adam Stachowiak.
[15.80 --> 19.94]  This is episode 220, and today, Jared and I have a huge show for you.
[20.34 --> 25.38]  Sid C. Brandy, CEO of GitLab, joins the show today to unveil the GitLab Master Plan,
[25.38 --> 30.44]  and $20 million Series B funding, which is huge for them to help them go into the future.
[30.86 --> 34.98]  They've got the .com, which is totally free, the open-source version, which everybody knows and loves,
[35.20 --> 38.62]  and also the enterprise on-premise that is funding the future.
[39.00 --> 44.72]  We talked about conversational development, all the tools they're building around this post-agile world development workflow.
[45.12 --> 53.98]  They're focused on enterprise and on-premise Git hosting as the business model to sustain and build GitLab into something modern software teams can rely upon.
[53.98 --> 58.32]  We have three sponsors today, Linode, Rollbar, and CodeSchool.
[59.04 --> 63.92]  Our first sponsor of the show is our friends at Linode, cloud server of choice here at Change Log.
[64.28 --> 66.92]  Get a Linode cloud server up and running in seconds.
[67.20 --> 69.56]  Head to linode.com slash changelog to get started.
[69.94 --> 73.08]  Choose your flavor of Linux, resources, and node location.
[73.60 --> 75.00]  Plan is started at just $10 a month.
[75.32 --> 78.02]  Get full root access, run VMs, run containers.
[78.48 --> 82.70]  You can even manage your Linodes from the comfort of terminal using Linode CLI.
[82.70 --> 90.88]  They've got SDKs in Python, Perl, PHP, Ruby, JavaScript, Node.js, so you can hack away on your Linodes with their API.
[91.40 --> 96.10]  Take advantage of add-ons like backups, node balancers, DNS manager, and more.
[96.48 --> 100.72]  Again, use our code CHANGELOG20 for $20 in credit with unlimited uses.
[100.88 --> 101.64]  Tell your friends.
[102.02 --> 103.90]  Head to linode.com slash changelog.
[104.00 --> 105.40]  And now on to the show.
[105.40 --> 111.24]  All right, we're back with a great show today, Jared.
[111.28 --> 113.18]  We got a show in the making.
[113.38 --> 120.14]  It's been three years and a day basically since we published the last anything on the changelog from GitLab.
[120.34 --> 126.18]  And today we have Sid joining us, the GitLab master plan, a lot of fun stuff around where they came from.
[126.80 --> 129.70]  What do you think is most interesting about GitLab these days, Jared?
[129.70 --> 135.98]  I think everything's interesting about GitLab and, in fact, Git hosting in general is heating up.
[136.04 --> 136.74]  This is a huge week.
[137.22 --> 144.76]  Huge announcements from Sid's team, the GitLab master plan, GitHub universe also going on, and big new features coming out of GitHub.
[145.42 --> 149.88]  And as users of Git and these services, we just get all the goodies.
[150.14 --> 150.74]  We level up.
[150.76 --> 151.86]  We're just going to use them and enjoy them.
[151.90 --> 152.14]  That's right.
[152.18 --> 152.76]  We're going to level up.
[152.92 --> 154.76]  And GitLab level up quite a bit.
[154.92 --> 155.62]  Huge announcement.
[156.24 --> 158.70]  $20 million Series B funding.
[158.70 --> 159.40]  Is that right, Sid?
[159.78 --> 160.46]  That's correct.
[161.06 --> 162.06]  Congratulations on that.
[162.18 --> 162.34]  Yes.
[162.34 --> 163.34]  Thanks for coming on the show.
[163.56 --> 164.26]  Big congrats.
[164.68 --> 164.84]  Yeah.
[164.88 --> 165.82]  Thanks for having me.
[166.08 --> 168.76]  So, Sid, it's been three years.
[168.92 --> 173.34]  So, the last time we had this show, it was, I think, Enterprise Edition was just being announced.
[173.56 --> 175.26]  You were announcing GitLab 6.0.
[175.84 --> 177.38]  This is like September 2013.
[178.16 --> 180.54]  So, that means we recorded it probably a week before that.
[180.62 --> 185.20]  So, it's still early in terms of that timeline you presented yesterday in that live broadcast.
[185.20 --> 190.04]  But, I don't think we know much about you yourself.
[190.34 --> 195.60]  So, I don't know how often you get a chance to share kind of where you began or who you are.
[195.70 --> 198.58]  Kind of introduce yourself to the software development world.
[198.84 --> 207.82]  But, introduce yourself and maybe take us back to maybe where you got some of your first initializations into software development.
[207.82 --> 213.78]  My first computer, I remember vividly, it was an old sendy from my uncle.
[214.60 --> 217.46]  And I had a really hard time finding the on button.
[217.64 --> 218.42]  So, I got the thing.
[218.56 --> 219.34]  I plugged it in.
[219.62 --> 221.76]  It was an integrated thing.
[221.98 --> 225.24]  And it turns out the on and off button was under the keyboard.
[225.44 --> 228.98]  But it's hard to look under the keyboard when you have to lift up the entire thing.
[229.40 --> 234.42]  So, literally, I examined every surface of this computer trying to find out how to turn it on.
[234.42 --> 238.52]  I didn't really get into programming.
[238.86 --> 241.36]  It was too tedious, I thought.
[241.72 --> 245.48]  So, I studied applied physics for a year and then did management science.
[245.94 --> 248.56]  One investor called me an organizational design junkie.
[249.30 --> 251.84]  And I think that's a good way to describe me.
[252.32 --> 258.00]  After my studies, I was the first employee of a submarine company for five years.
[258.00 --> 263.18]  So, we made recreational submarines where people can dive in.
[264.42 --> 273.36]  It's basically, if you have a boat of more than 50 meters, 150 feet, you already have the helicopter or not because they're tedious.
[273.76 --> 274.60]  And then you want something else.
[274.76 --> 276.04]  So, we made the submarines.
[276.54 --> 280.74]  And we totally failed at our price point because we tried to make it for $20,000.
[281.18 --> 282.88]  And they now cost $2 million.
[283.50 --> 285.80]  We really, really tried to make them affordable.
[286.14 --> 286.80]  It's hard.
[286.80 --> 286.86]  It's hard.
[287.54 --> 288.00]  That's funny.
[288.76 --> 289.60]  That sounds hard.
[291.18 --> 291.92]  They're great.
[292.16 --> 297.26]  And Uboat Works is still shipping the most submarines every year, which is a handful.
[297.90 --> 303.44]  Generally, it's a first for us to have somebody on the show that had been applied physics for one.
[303.52 --> 307.42]  And maybe we've never asked that kind of background, but then also to build submarines.
[308.14 --> 310.42]  Well, Sid, give us your best takeaway.
[310.82 --> 315.08]  What you learned building submarines that we can apply to the craft of software development.
[315.08 --> 328.78]  Well, one lesson we had to learn, and I think you can learn that in software as well, is that outsourcing to lower wage countries is not always a good strategy.
[328.78 --> 329.28]  Ah.
[329.28 --> 337.22]  And another thing is that even though there might be no government rules for things, that doesn't mean that there are no rules.
[337.72 --> 339.64]  There are all kinds of implicit rules.
[339.74 --> 347.02]  And we figured out, we had to learn that for submarines, although the government doesn't require anything, the insurance company does require things.
[347.02 --> 350.46]  And people kind of want to be able to insure their submarine.
[350.76 --> 350.96]  Yeah.
[352.00 --> 355.32]  So, yeah, it was a very interesting time.
[355.44 --> 360.72]  I did applied physics only for a year, so I hired one of my friends from college to actually do the mechanics.
[360.84 --> 367.78]  And I focused on the electronics and the automation, building my first basically computer board and programming chip.
[367.78 --> 375.72]  I was really, really beyond joy when that chip booted up the first time because I would have no idea to troubleshoot it.
[375.94 --> 381.32]  But at the end of that, at the end of those five years, I saw Ruby, the programming language.
[381.64 --> 385.54]  And I said, wow, instead of tedious, this looks beautiful.
[385.80 --> 386.60]  This looks great.
[386.72 --> 388.66]  This is what I've always wanted.
[389.06 --> 392.48]  And I started learning Ruby and became a developer.
[392.48 --> 400.78]  And after a few years of consulting for various companies, I saw GitLab and I thought, wow, this is amazing.
[400.92 --> 406.18]  It makes so much sense that a collaboration tool is something you can contribute to, that it's open source.
[406.82 --> 410.30]  And I thought SaaS and dot-coms are the future.
[410.68 --> 411.88]  That's the way to make money.
[412.06 --> 414.40]  So I got started with that.
[415.16 --> 417.94]  So the role you play now is CEO, right?
[419.00 --> 419.72]  Yeah, that's correct.
[419.72 --> 424.72]  So Dimitri, the author of GitLab, and I co-founded the company.
[425.10 --> 427.28]  He is CTO and I'm CEO.
[428.00 --> 433.54]  So would you say that you're business and he's software or would you say you're kind of a mix of both?
[434.30 --> 436.10]  No, I think that's a good characterization.
[436.80 --> 439.26]  So what, I know you built submarines.
[440.58 --> 443.96]  What, you know, what was, what made you want to be an entrepreneur?
[443.96 --> 450.06]  What made you want to be the person like defining a company, leading a company, hiring employees, building a product?
[450.06 --> 455.84]  I think I've always seen stuff where I'm like, wow, that's, that would make a great business.
[456.42 --> 459.24]  And the first one was during my studies.
[459.24 --> 462.04]  I saw someone made an infrared receiver.
[462.20 --> 466.80]  And this was in 99, where everyone was starting to run MP3s on your computer.
[466.98 --> 472.64]  And we'd have these websites that do reviews of how much CPU a different MP3 encoder would take.
[472.64 --> 478.84]  And this infrared receiver allowed you to use the existing remote you have of your stereo to skip to the next song.
[479.10 --> 480.20]  And I thought that's amazing.
[480.62 --> 485.50]  So the code was open source and we ended up, I ended up being the business person selling it.
[485.66 --> 486.88]  And that was in my first year.
[487.18 --> 489.52]  And then applied physics had lots of difficult math.
[490.02 --> 492.96]  So I figured I liked the entrepreneurial side.
[493.14 --> 497.82]  So I switched and I started doing management science.
[497.82 --> 508.12]  And I've, I've always, now that we run GitLab, I, I found out about myself that I have lots of opinions, how, how companies should be run more effectively.
[508.42 --> 512.56]  I've, I've done internships at some like fortune 10 companies.
[513.38 --> 517.06]  And yeah, I saw lots of inefficiencies.
[517.54 --> 524.80]  So now at GitLab, I'm trying to prevent having that and making sure that people can be very effective and get, can get lots of results.
[524.80 --> 528.28]  So I think that's where that business passion is coming in.
[529.28 --> 537.66]  Yesterday on the live event, just to catch up to listeners, GitLab had a live broadcast of their master plan, which aired yesterday.
[537.82 --> 539.48]  That would be September 13th.
[539.48 --> 548.04]  And on that, Sid, you, you said that the start of GitLab, it started off as an open source project and you came to it.
[548.28 --> 552.60]  And remind me the name of your co-founder again, the.
[553.10 --> 553.42]  Dimitri.
[553.42 --> 553.82]  Dimitri.
[553.88 --> 554.28]  Dimitri.
[554.36 --> 559.40]  And you told Dimitri, thank you, that you were going to take this and turn it into software as a service.
[560.56 --> 565.22]  And he said, okay, or I don't recall what he said, but you tried that.
[565.30 --> 567.10]  And then that seemed like it kind of fell flat.
[567.18 --> 571.20]  Can you, can you give us that little bit of a background and what you moved to from there?
[572.04 --> 572.22]  Yeah.
[572.30 --> 575.20]  So I thought all the money is in the SaaS, like Salesforce.
[575.64 --> 577.18]  That's what I read on TechCrunch.
[577.18 --> 579.84]  Um, so I emailed Dimitri.
[580.04 --> 584.02]  So, hey, Dimitri, I'm going to do, I'm going to try, I'm going to make money on this.
[584.32 --> 589.34]  And, uh, well, I'm sorry, but you're probably not going to be part of this.
[589.44 --> 590.54]  I hope you don't mind.
[590.64 --> 592.40]  And he was like, wow, it's so amazing.
[592.44 --> 594.78]  You're doing something with GitLab and making it more popular.
[594.78 --> 596.12]  And of course you go for it.
[596.12 --> 596.92]  It's open source.
[597.06 --> 597.94]  Do whatever you want.
[597.94 --> 599.82]  So that was really nice of him.
[600.28 --> 603.26]  But, uh, a year later, I learned that I was wrong.
[603.38 --> 605.26]  It was really hard to make money on the SaaS.
[605.90 --> 610.46]  But at the same time, there were all these enormous companies like fortune five companies
[610.46 --> 616.54]  that were running GitLab and were asking me for more features because I was easy to find
[616.54 --> 617.28]  on the internet.
[617.96 --> 621.60]  Um, but I wasn't the world's best programmer.
[622.24 --> 627.44]  Um, but at the same time, Dimitri tweeted in a public tweet.
[627.44 --> 629.46]  I want to work on GitLab full time.
[630.62 --> 632.04]  So that was easy.
[632.04 --> 636.72]  I contacted Dimitri and said, well, I can pay you to work on GitLab full time.
[636.96 --> 638.34]  And he started making those features.
[638.80 --> 643.10]  And we spun off some of those features into the enterprise edition in order to have a business
[643.10 --> 645.18]  model because we tried everything.
[645.42 --> 646.92]  We tried donations.
[647.20 --> 648.16]  We tried consulting.
[648.66 --> 650.32]  We tried paid for development.
[651.22 --> 657.22]  Um, but none of these really seemed to work, but being able licensing software, it was very
[657.22 --> 659.54]  easy for users to pay for that.
[659.64 --> 663.80]  It was very easy to just have a, buy a license to use software.
[663.92 --> 665.18]  They were very used to that.
[665.68 --> 670.46]  So, uh, that, that model worked much better than donations, which they didn't have budget
[670.46 --> 670.78]  for.
[670.78 --> 673.10]  Can we pause on the, some of the fails there?
[673.20 --> 675.36]  Like you mentioned consulting and donations.
[675.36 --> 683.72]  How hard is it to maintain vision and trajectory when trying ideas to sort of become sustainably
[683.72 --> 688.36]  sustainable, I guess, in terms of funding, how hard is it to maintain your promises to
[688.36 --> 693.04]  customers, your promises to end users while trying things and experimenting with different
[693.04 --> 693.80]  funding models?
[694.28 --> 696.56]  Uh, and then ultimately those were not work out.
[696.56 --> 698.78]  How do you kind of keep and maintain trajectory on that?
[699.86 --> 700.08]  Yeah.
[700.26 --> 705.30]  Um, you have to keep an open mind, um, donations.
[705.74 --> 707.06]  Dimitri was already doing that.
[707.16 --> 709.88]  So the first thing was, uh, intensifying that.
[710.00 --> 715.18]  And I think the biggest drive we did, we got a thousand dollars in a month, uh, which wouldn't
[715.18 --> 716.16]  even pay for Dimitri.
[716.62 --> 719.24]  Um, and then it was a single drive.
[719.34 --> 721.14]  So keeping that up is super hard.
[721.14 --> 728.24]  I think now with Patreon and stuff, you, you can get like up to $10,000 in subscribers
[728.24 --> 729.90]  so that we'll pay for one or two people.
[730.10 --> 734.68]  So it's becoming a better model, especially because Patreon is recurring, but it's hard
[734.68 --> 737.42]  to like build a serious company and competitor out of it.
[738.34 --> 742.14]  Uh, we also tried consulting, helping people fix their GitLab installation.
[742.78 --> 747.50]  But at the end of a consulting arrangement, we would of course take all the lessons we learned
[747.50 --> 750.64]  and incorporate them in the documentation and the open source project.
[751.14 --> 753.90]  So very quickly people didn't need consulting anymore.
[754.12 --> 755.42]  And of course, this is how it should be.
[755.48 --> 758.90]  It should be very easy to install GitLab and our open source edition.
[759.32 --> 763.12]  It's even easier to install than the paid one because you don't have to add a license,
[763.30 --> 765.80]  but both of them you can set up in a couple of minutes.
[766.68 --> 771.96]  And, um, we wanted, we figured that the project would never become popular if we would make
[771.96 --> 775.60]  it hard to install and then pay us for the consulting that, that didn't make sense to us.
[775.66 --> 776.34]  It's not efficient.
[776.50 --> 778.56]  It's not the way to the world should work.
[778.56 --> 782.18]  And then paying for development, uh, that was hard.
[782.18 --> 787.56]  First, you have to agree on the feature, like a customer, potential customer wants a feature.
[787.76 --> 793.04]  You still have to like agree and negotiate a bit about how exactly it should look.
[793.38 --> 795.18]  Then you have to make an estimate.
[795.46 --> 802.12]  Then they have to purchase it, which sometimes is hard because this in the, for the purchasing
[802.12 --> 804.90]  department, this falls under paid development.
[804.90 --> 808.38]  And they frequently have a preferred vendor for this.
[808.52 --> 812.26]  So then now they need to get out from this preferred vendor agreement.
[812.68 --> 819.18]  And then last but not least, you have some perverse incentives because there are, sometimes
[819.18 --> 823.08]  there are multiple people asking and willing to pay for the same feature.
[823.08 --> 828.02]  And of course you don't want to cheat on them by like making everyone paid a full amount.
[828.66 --> 831.28]  But as soon as you inform them, there are others.
[831.42 --> 836.26]  They're not as likely to agree to paying for it because they figure they just wait.
[836.94 --> 840.44]  And in general, that's the incentive because GitLab was moving so fast.
[840.78 --> 844.72]  If you wanted a feature, it's very likely it will ship in the next few months.
[844.86 --> 848.02]  So why go through all the hassle of purchasing something?
[848.02 --> 851.56]  So this made it really hard to pull off that model.
[852.76 --> 856.58]  Maybe useful at this time to get a lay of the land of GitLab.
[857.30 --> 862.26]  And we'll do a little bit more on the history side, but just what it is in terms of products.
[862.40 --> 866.16]  You have a community edition, there's enterprise, there's your gitlab.com.
[866.74 --> 870.72]  Can you kind of just lay out all the different ways you can go about using or engaging with
[870.72 --> 872.08]  GitLab as a product today?
[872.08 --> 872.52]  Yeah.
[872.52 --> 873.12]  Yeah.
[873.66 --> 880.44]  So GitLab started as a Git hosting and code review tool.
[880.90 --> 883.34]  And that's what it branched out.
[883.50 --> 885.22]  So now it also includes CI.
[885.56 --> 886.50]  It includes CD.
[887.00 --> 890.62]  It comes with a chat client, an open source Slack alternative.
[891.08 --> 892.44]  You can run behind the firewall.
[893.26 --> 897.76]  And we're working to a more complete version.
[897.76 --> 903.18]  We'll probably talk later about doing the whole software development lifecycle.
[904.18 --> 904.82]  So that's it.
[905.84 --> 910.28]  All those parts are in the open source version, which you can run without limitations.
[911.20 --> 914.68]  And over 100,000 organizations run that.
[915.06 --> 922.06]  It's the most installed and the most popular behind the firewall way to use Git.
[922.06 --> 927.42]  And we also have an enterprise edition that contains features that you're more likely to
[927.42 --> 929.16]  need if you're over 100 people.
[929.74 --> 935.54]  And you get these additional features if you pay us a subscription of $39 per user per year.
[935.80 --> 940.96]  Now, we also wanted to offer it as a service, not because the money was there, because that's
[940.96 --> 945.84]  what I learned, but to make it easy to get started and to explore the product.
[945.84 --> 951.98]  So we made a conscious decision to give away everything on .com and make it completely free.
[952.62 --> 957.06]  So on goodlab.com, you get the enterprise edition with all the features and you pay nothing.
[957.64 --> 959.86]  You don't pay for public repositories.
[960.00 --> 961.22]  You don't pay for private ones.
[961.32 --> 962.64]  You don't pay for collaborators.
[963.26 --> 965.38]  And right now, even the CI is free.
[965.80 --> 971.54]  So you can have as many parallel CI runners as you want on your private project and we'll even
[971.54 --> 972.16]  pay for that.
[972.48 --> 974.36]  So those are the three products that we offer.
[974.36 --> 979.58]  So the only difference there is perhaps you want for privacy or security concerns, you
[979.58 --> 981.38]  want the on-premise enterprise version.
[981.66 --> 985.36]  Otherwise, wouldn't everybody just use your free hosted version?
[986.24 --> 986.72]  Yeah, exactly.
[987.16 --> 994.64]  But what I learned in that year was that all large organizations in the world basically
[994.64 --> 995.96]  run it behind the firewall.
[996.94 --> 999.18]  And there are different reasons.
[999.42 --> 1000.94]  Some of them are security related.
[1000.94 --> 1007.40]  They want it behind their VPN service or they want to hook it up with their single sign-on
[1007.40 --> 1010.26]  service or they want to do LDAP group sync.
[1011.32 --> 1012.60]  Some of them are legal.
[1012.94 --> 1014.48]  They need it on their own servers.
[1014.48 --> 1021.32]  They need to know where exactly in what jurisdiction it's located and they want to see when someone
[1021.32 --> 1023.00]  serves them or warrant.
[1023.96 --> 1026.18]  And last but not least, some reasons are technical.
[1026.48 --> 1031.66]  They have a lot of existing infrastructure to integrate with and don't want to poke a lot
[1031.66 --> 1032.64]  of holes in their firewall.
[1032.92 --> 1036.60]  It's more performant if it's on their local network.
[1036.60 --> 1039.34]  And that was a surprising thing to me.
[1039.56 --> 1041.78]  I thought that everyone would be using a SaaS.
[1042.08 --> 1046.56]  And it turns out all the large companies, without exception, are currently using something
[1046.56 --> 1047.18]  on-premises.
[1047.40 --> 1049.10]  So that's where we monetize.
[1049.30 --> 1050.18]  That's our business model.
[1050.18 --> 1057.44]  So basically, the on-premise version is the funding model that funds the free.com, that
[1057.44 --> 1062.06]  funds the host-it-yourself version that is open source.
[1062.94 --> 1066.84]  100,000 people, as you mentioned, use that self-hosted open source version.
[1067.02 --> 1072.04]  But the on-premise is essentially the way you make money, the way you sustain, and essentially
[1072.04 --> 1076.50]  what pays for all the development for the .com and the open source.
[1077.14 --> 1077.62]  Exactly.
[1077.80 --> 1078.50]  That is the model.
[1078.50 --> 1081.94]  And it's 100,000 organizations, so it's millions of developers.
[1082.38 --> 1089.32]  There are some companies using GitLab with over 20,000 people, and some of these are even
[1089.32 --> 1090.66]  using the open source version.
[1091.66 --> 1097.34]  Just curious, I mean, considering there's other code hosts out there, which we know, why is
[1097.34 --> 1099.68]  this model better than the other models?
[1099.72 --> 1103.46]  And I don't think you need to go and speak to their models particularly, but why do you
[1103.46 --> 1104.84]  feel like this is the better model?
[1104.84 --> 1108.02]  Or how did you come to the conclusion that this is the best model for you?
[1108.50 --> 1108.76]  Yeah.
[1108.76 --> 1114.52]  I think what we wanted to do is we wanted an open source version that is not crippled in
[1114.52 --> 1120.22]  any way, that doesn't have any artificial limitations that gives you the complete experience
[1120.22 --> 1127.52]  that allows us to, when someone has a feature that maybe already exists in the Enterprise Edition,
[1127.52 --> 1132.98]  it still allows us to merge that in the open source one without completely destroying our
[1132.98 --> 1134.66]  business model in one go.
[1134.66 --> 1140.46]  So we think the way to do that is that there's some features that larger organizations need.
[1141.12 --> 1148.98]  And the great thing about larger organizations, those are the organizations that make up the majority of all software spending.
[1149.52 --> 1153.28]  So if you can get them to adopt your product, you'll do a lot better.
[1153.86 --> 1155.90]  And GitLab was born in the Enterprise.
[1156.26 --> 1160.50]  Dimitri and Valeri were working in an organization with more than 200 people.
[1160.50 --> 1166.46]  And those customers that were asking for features in our beginning were also enormous organizations.
[1166.68 --> 1170.00]  So from the beginning, we focused on the feature set for done.
[1170.44 --> 1172.74]  And that's why we've become the most popular there.
[1173.00 --> 1175.52]  And the lucky thing is, that's also where the money is.
[1176.46 --> 1178.18]  Well, Sid, we're bumping up against our first break.
[1178.26 --> 1183.50]  Before that, let's talk real quick about your company size and way of catching up.
[1183.50 --> 1186.70]  I think probably when you were on the show last, you were quite small.
[1186.90 --> 1191.96]  I know you mentioned in your timeline, I think it was 2012 or maybe it was 2013 when you had nine employees.
[1192.30 --> 1195.90]  Of course, we just stated that you just raised $20 million Series B.
[1196.30 --> 1198.22]  So that is to support many people.
[1198.36 --> 1205.04]  You now have 104 employees and quite interesting to me, at least, in 103 locations.
[1205.24 --> 1206.08]  Can you tell us about that?
[1206.08 --> 1206.48]  Yeah.
[1206.48 --> 1206.96]  Yeah.
[1207.32 --> 1214.56]  So in March of 2015, one and a half years ago, we graduated from Y Combinator.
[1215.08 --> 1216.76]  And for us, that was an inflection point.
[1217.24 --> 1225.54]  After that, we started growing a lot quicker than we had before because we wanted to make sure that all companies will standardize on GitLab.
[1225.64 --> 1231.84]  And we recognize that it has to be a complete product and that we have to have great marketing and sales to do that.
[1232.32 --> 1235.46]  However, since the beginning, we've been a remote company.
[1235.46 --> 1242.44]  So I anticipated having to hire locally in San Francisco.
[1243.62 --> 1247.56]  We got an office there and the first salespeople came to the office.
[1248.04 --> 1255.92]  Then after a few days, they started working from home because all of our tooling, all of our organization was set up to be able to do that.
[1256.72 --> 1259.26]  And they were making their quota.
[1259.36 --> 1260.12]  They were doing great.
[1260.70 --> 1263.30]  And I figured it's fine.
[1263.38 --> 1264.66]  I like to work from home too.
[1264.66 --> 1266.72]  I like to not be interrupted.
[1267.04 --> 1269.74]  I like to have flexibility in my workday.
[1270.36 --> 1274.50]  I like the ability to travel where I want to travel.
[1274.50 --> 1277.12]  So I never made them.
[1277.12 --> 1278.72]  And we kept that going.
[1278.72 --> 1281.20]  So by now, we're over 100 people.
[1281.20 --> 1282.80]  We're on six continents.
[1282.92 --> 1284.40]  We're in 33 countries.
[1284.72 --> 1291.24]  And basically, everyone works from another location and from the location they want to work from.
[1291.24 --> 1299.14]  The only exception is that sometimes our executive assistant comes to the office here where I also live.
[1299.14 --> 1308.10]  But we found that this remote-only way of working is making us all a lot happier.
[1308.10 --> 1314.24]  There's a much better harmony between work and the rest of your life.
[1314.24 --> 1317.00]  And it's something that we want to keep going.
[1317.20 --> 1319.78]  And it allowed us to hire amazing people.
[1319.78 --> 1323.38]  I bet you'd like to have somebody on that seventh continent, though, wouldn't you?
[1324.38 --> 1324.82]  Yeah.
[1325.20 --> 1328.86]  There's someone who remarked in our company, he just bought a lot of generators.
[1329.10 --> 1330.86]  So maybe he's ready for Antarctica.
[1331.48 --> 1331.90]  There you go.
[1332.60 --> 1336.84]  Go back to your ruse with applied science or applied physics and submarines.
[1336.84 --> 1337.84]  Yeah.
[1337.84 --> 1339.96]  Maybe we should have a station there.
[1340.08 --> 1341.02]  It would be a nice perk.
[1341.48 --> 1346.18]  But no, the hardest thing to make work is time zones.
[1346.56 --> 1350.14]  So its location is nice.
[1350.24 --> 1352.54]  It's also nice to hang out together from time to time.
[1352.94 --> 1355.38]  So we do have a summit every half year.
[1355.52 --> 1360.70]  And we spend a lot of time trying to make remote work so you still feel part of the company.
[1361.08 --> 1363.50]  So we have a call every four times a week.
[1363.50 --> 1369.54]  And more than half of the time is spent with people telling what they did in their private lives.
[1369.80 --> 1374.64]  We have the concept of virtual coffee breaks where you schedule half an hour to talk about
[1374.64 --> 1376.72]  things that don't have to be work related.
[1377.18 --> 1380.78]  We really want to make sure that everyone feels part of a team.
[1381.24 --> 1384.84]  And we're doing, I think, a great job at that.
[1385.00 --> 1389.66]  People feel closely connected, even to people that are living on another continent.
[1390.24 --> 1393.32]  Well, to do remote work, you definitely have to bake it into who you are.
[1393.32 --> 1393.88]  That's for sure.
[1393.96 --> 1399.28]  Because there's companies that have this kind of hybrid version where you have some remote
[1399.28 --> 1400.82]  and some in office.
[1401.30 --> 1408.14]  And you always feel like a divide or how the message has to be distributed through the organization
[1408.14 --> 1411.44]  is always like, well, is this person local or remote?
[1411.50 --> 1414.56]  And it's always this fragmented communication pattern.
[1414.56 --> 1423.76]  And so being all in, having your DNA or being remote working in your DNA has to be the key there.
[1424.40 --> 1428.08]  Yeah, we think doing a hybrid model is the hardest thing.
[1428.68 --> 1430.12]  We think being remote only...
[1430.12 --> 1430.14]  It's impossible, basically.
[1430.42 --> 1430.62]  Yeah.
[1430.66 --> 1431.26]  It does fail.
[1431.48 --> 1432.06]  It will fail.
[1432.40 --> 1435.22]  You always feel like you're a secondary citizen.
[1435.22 --> 1441.42]  And even companies with multiple offices will always have the feeling of either you're in
[1441.42 --> 1444.44]  the main office or you're in the satellite office and you're missing a lot.
[1444.74 --> 1444.86]  Yeah.
[1444.86 --> 1446.86]  And here, everyone is on the same level.
[1447.14 --> 1449.30]  And we really try to over-communicate.
[1449.90 --> 1455.30]  For example, today in our team call, I shared our management notes.
[1455.56 --> 1456.26]  We had a two-day...
[1456.98 --> 1458.50]  We call it the remote off-site.
[1458.64 --> 1463.18]  It basically means we sit a couple of hours in a call with the whole executive team.
[1463.66 --> 1465.70]  And we shared all the notes with the whole company.
[1465.70 --> 1471.74]  We had a fundraising channel, a chat channel, where we kept a score by score of this investor.
[1471.96 --> 1473.36]  We're on to the next meeting.
[1473.46 --> 1474.90]  This one said no for that reason.
[1475.44 --> 1479.94]  People cheering us on, people learning about what it means to invest.
[1480.22 --> 1486.68]  To the point where when I announced we had the second term sheet or the third term sheet,
[1486.80 --> 1489.44]  someone said, yeah, what's the liquidation preference?
[1490.28 --> 1494.10]  And this was coming from a junior developer who recently joined the company.
[1494.10 --> 1501.04]  So really having everyone involved in stuff that normally wouldn't be a formal process.
[1501.26 --> 1503.74]  It will be something you ask during a lunch break.
[1503.86 --> 1510.38]  But we're recognizing that if you're remote, those lunch breaks are spent with your family
[1510.38 --> 1511.16]  and your friends.
[1511.28 --> 1515.14]  So we have to over-communicate in all the formal things.
[1516.12 --> 1516.30]  All right.
[1516.34 --> 1517.56]  Let's take our first break.
[1517.60 --> 1522.36]  On the other side, we will dig into the heart of the conversation around GitLab's
[1522.36 --> 1523.76]  just announced master plan.
[1524.10 --> 1527.68]  And what that means for the present and future of the product.
[1527.82 --> 1528.34]  We'll be right back.
[1528.34 --> 1532.14]  Hey, everyone.
[1532.26 --> 1534.96]  Adam Stikowiak here, editor-in-chief of ChangeLog.
[1535.00 --> 1536.82]  And I'm talking to a Rollbar customer.
[1537.34 --> 1539.52]  Rollbar puts errors in their place.
[1539.90 --> 1541.86]  Rollbar.com slash ChangeLog.
[1542.14 --> 1542.96]  Check them out.
[1543.10 --> 1546.74]  Get 90 days of the bootstrap plan totally for free.
[1547.38 --> 1551.20]  I had a conversation with Paul Bigger, the founder of CircleCI.
[1551.20 --> 1558.08]  He talked deeply about how they use Rollbar and how important that tool is to their developers.
[1558.58 --> 1559.32]  Take a listen.
[1559.82 --> 1564.12]  One of the key parts about doing continuous delivery, you don't just have to test your software,
[1564.22 --> 1565.82]  but you have to constantly keep track of it.
[1565.96 --> 1569.22]  You're going to be doing deploys 10 times a day or 20 times a day.
[1569.32 --> 1571.58]  And you have to know that each deploy works.
[1571.66 --> 1573.90]  And the way to do that is to have really good monitoring.
[1573.90 --> 1580.00]  And Rollbar is literally the thing that you need to do that monitoring.
[1580.24 --> 1585.38]  You need to make sure that every time you deploy, you're going to get an alert if something goes wrong.
[1585.58 --> 1588.30]  And that's exactly what Rollbar does for CircleCI.
[1588.66 --> 1591.50]  So obviously, CircleCI is important to your customers.
[1592.10 --> 1593.16]  You shouldn't have errors.
[1593.30 --> 1594.42]  You shouldn't have bugs.
[1595.12 --> 1598.70]  And the purpose of a CI is continuous delivery, obviously.
[1598.70 --> 1606.04]  But getting your customers' code to production in a fast manner that's tested and all the necessary things a CI provides.
[1606.46 --> 1610.54]  Tell me how important Rollbar is to your team and your organization.
[1610.96 --> 1613.00]  We operate at serious scale.
[1613.42 --> 1618.82]  And literally the first thing we do when we create a new service is we install Rollbar in it.
[1619.04 --> 1621.88]  We need to have that visibility.
[1622.32 --> 1626.82]  And without that visibility, it would be impossible to run at the scale we do.
[1626.82 --> 1628.90]  And certainly with the number of people that we have.
[1629.08 --> 1632.08]  We're a relatively small team operating a major service.
[1632.58 --> 1637.82]  And without the visibility that Rollbar gives us into our exceptions, it just wouldn't be possible.
[1638.30 --> 1638.92]  Well, that's awesome.
[1639.18 --> 1639.60]  Thanks, Paul.
[1639.66 --> 1640.46]  I appreciate your time.
[1640.92 --> 1643.34]  So listeners, we have a special offer for you.
[1643.78 --> 1646.20]  Go to rollbar.com slash change blog.
[1646.72 --> 1647.34]  Sign up.
[1647.58 --> 1650.18]  Get the bootstrap plan for free for 90 days.
[1650.50 --> 1652.94]  That's 300,000 errors tracked.
[1653.20 --> 1654.26]  Totally for free.
[1654.76 --> 1655.96]  Give Rollbar a try today.
[1655.96 --> 1658.86]  Head over to rollbar.com slash change log.
[1666.52 --> 1667.18]  All right.
[1667.22 --> 1672.86]  We are back with Sid C. Brandage talking about GitLab and the just announced master plan.
[1673.16 --> 1675.60]  Sid, you got big plans for the future.
[1676.60 --> 1678.36]  Exciting ones to say the least.
[1679.02 --> 1683.24]  And it's all kind of focused around this idea of conversational development.
[1683.24 --> 1684.66]  So I thought we'd start there.
[1685.06 --> 1690.38]  Talk about what that is and then how GitLab is going to help promote it or provide for it.
[1691.18 --> 1691.88]  Yeah, I'd love to.
[1692.52 --> 1701.08]  I want to take a step back to the evolution of different paradigms in software development processes.
[1701.08 --> 1704.72]  We used to have Waterfall in the 70s.
[1704.72 --> 1707.74]  And it was very rigid and inflexible.
[1708.00 --> 1712.78]  And luckily, it got replaced by Scrum, which was a great improvement.
[1712.78 --> 1716.96]  But you still had to estimate every single issue.
[1716.96 --> 1719.18]  There was a lot of negotiations going on.
[1719.62 --> 1723.16]  Most of that got fixed by agile development, which I love.
[1723.54 --> 1726.64]  And conversational development is an evolution of that.
[1726.64 --> 1732.04]  And what we wanted to evolve is that agile doesn't cover the whole process.
[1732.48 --> 1737.36]  It covers only part of the process, the development one.
[1737.80 --> 1741.70]  For operations, we had to add DevOps to it.
[1742.16 --> 1744.78]  But I think there's still something missing from the beginning.
[1746.18 --> 1750.34]  There's also a process before you decide to start doing something.
[1750.34 --> 1756.46]  And another thing with agile, it focuses really on collaboration in the same location.
[1757.06 --> 1762.36]  And I think with open source, we've seen that you can collaborate effectively even when you're remote.
[1763.04 --> 1770.56]  So we think it's time for a new paradigm or an evolvement of agile.
[1770.70 --> 1772.54]  And we call that conversational development.
[1773.76 --> 1776.18]  And there's five main points in there.
[1776.18 --> 1780.46]  We want to reduce the cycle time to increase effectiveness.
[1781.00 --> 1786.32]  And the cycle time we measure, the time it takes from having an idea to having it in production.
[1787.66 --> 1792.64]  And anything that impedes that should be measured.
[1793.30 --> 1795.76]  And you should try to do it more quickly.
[1796.20 --> 1803.68]  So many large organizations now, they take many months between having an idea and then having the code out there for users.
[1803.68 --> 1805.32]  And we think that should be days.
[1806.18 --> 1808.18]  And to do that, that's the second thing.
[1808.24 --> 1809.60]  You need to monitor the process.
[1809.74 --> 1811.94]  So you need to know how long every step takes.
[1812.96 --> 1816.38]  The third thing is you want to thread the conversation through all stages.
[1817.04 --> 1827.58]  So when you deploy something, when you get something out to users, you want to be able to go back and see where did this idea originate?
[1827.58 --> 1829.14]  You want to make sure all these steps are linked.
[1829.14 --> 1835.86]  You want to make sure all these steps are linked and that you can have a conversation that is supported by your tooling.
[1837.36 --> 1841.36]  Fourth is that gatekeepers become part of the conversation.
[1841.36 --> 1847.40]  Where it used to be that, for example, a security audit was a step that was kind of a holdup.
[1847.82 --> 1850.18]  We think instead these people should be involved.
[1850.60 --> 1853.02]  So they should be invited to contribute.
[1854.02 --> 1861.70]  And by deploying, by doing this more frequently, you can reduce the scope of every iteration.
[1861.70 --> 1863.40]  And it's easier to review.
[1864.84 --> 1870.24]  And fifth, the rest of the organization should be able to contribute.
[1870.74 --> 1879.02]  We're seeing that large organizations are adopting the practices of open source and then call it inner sourcing.
[1879.02 --> 1884.54]  Where if you have a project, by default, you make it open to other teams.
[1884.84 --> 1890.68]  And if they want to reuse your code, they can rest assured that they can fork the project and contribute back to it.
[1890.86 --> 1893.02]  So you can reuse the same code base.
[1894.58 --> 1900.94]  And we think that the biggest benefits are in reducing the cycle time.
[1901.54 --> 1906.22]  It's simply that shipping smaller and simpler changes is more effective.
[1906.70 --> 1908.44]  And it's effective in lots of ways.
[1908.44 --> 1910.14]  It's more in line with expectations.
[1910.76 --> 1912.28]  It's easy to coordinate.
[1913.30 --> 1915.88]  The code review is of a higher quality.
[1916.14 --> 1917.52]  It's easier to troubleshoot.
[1917.70 --> 1920.54]  And it prevents gold plating, like overshooting needs.
[1921.14 --> 1927.18]  Apart from that, if you reduce the cycle time, you have more frequent interactions.
[1927.18 --> 1931.18]  Like more users get exposed to your code and give you feedback.
[1931.60 --> 1933.10]  You're quicker to respond.
[1933.62 --> 1935.02]  There's a higher predictability.
[1935.44 --> 1937.44]  There's more of a sense of progress in your team.
[1937.44 --> 1946.12]  So we think that this is what everyone and especially large organizations need to become more effective.
[1946.12 --> 1953.92]  Well, as you're talking through these, I'm just kind of applying those to our own process here, Adam, because I guess I'm narcissistic or something.
[1953.92 --> 1956.26]  And we're a tiny little team.
[1956.70 --> 1962.74]  But when I think about cycle time, maybe two to three people involved in software development.
[1963.10 --> 1967.26]  And I guess we feel like it's pretty fast cycle time, but we don't really have the monitoring.
[1967.66 --> 1970.74]  Your number two is monitor the process from idea to production.
[1970.74 --> 1974.36]  So it's more of a feeling than something that's been quantified.
[1975.06 --> 1982.92]  But when you got to point three about threading the conversation through all stages, that's where I started to think, OK, this is where a tool.
[1982.92 --> 1985.88]  I mean, I'm sure a tool could help with monitoring, of course, as well.
[1986.36 --> 1996.52]  But a tool, which is kind of part of your plan as you're going to unfold, is this like providing kind of all things that you need to have this style of development.
[1996.52 --> 2005.24]  Whereas right now, if we just look at the tools that Adam and I are using internally, we have Slack, we have GitHub issues, we have Trello.
[2006.24 --> 2008.72]  And, you know, half the time we spend trying to find it.
[2009.18 --> 2009.54]  Envision.
[2009.86 --> 2011.28]  We have Google Docs.
[2011.90 --> 2013.50]  Sometimes it ends up in a Google Doc.
[2015.18 --> 2018.58]  Brainstorming or it's in my notes app, just locally on my computer.
[2019.12 --> 2022.94]  And half the time we spend trying to find things.
[2023.94 --> 2025.38]  Where do we put that idea at?
[2025.38 --> 2027.44]  We say, haven't we had this conversation before?
[2027.80 --> 2031.06]  And we go searching through all of the things and eventually find it.
[2031.68 --> 2037.12]  So I think threading that conversation, that's where I really feel like there's a disconnect in tooling.
[2037.72 --> 2044.38]  I also feel like the second part of that, where you include, you know, the last two points, the gatekeeper and the rest of the organization.
[2044.38 --> 2054.52]  Like how many times, I'm not sure for you, Jared, but I've experienced this when I worked at Pure Charity, where we would invite people in quotes of what we call the business side of things.
[2054.52 --> 2060.30]  And we would invite them into the process and essentially ask them, because we hosted on GitHub.
[2060.30 --> 2066.54]  We would invite them into the GitHub organization to monitor issues and track things.
[2066.54 --> 2069.30]  And, you know, these things have obviously evolved since then.
[2069.34 --> 2077.44]  But we invited them into the what is typically, as Sid is sharing here, like what's typically shown as agile, which is around just the development cycle.
[2077.44 --> 2088.20]  Whereas, Sid, and correct me if I'm wrong, but I think what you're doing is you're sort of like zooming out quite a bit to say, how does product get made from idea to delivery?
[2088.50 --> 2094.88]  And how can we provide the tools necessary for collaborating around that, whether you're a remote team or not?
[2094.92 --> 2096.18]  How do you deal with inner source?
[2096.18 --> 2102.30]  And then ultimately, how do you invite the right kind of people into the conversation so that no one is an outsider?
[2102.78 --> 2104.66]  And that's, to me, that's pretty interesting.
[2105.72 --> 2106.02]  Awesome.
[2106.30 --> 2106.44]  Yeah.
[2106.50 --> 2108.90]  And it's exactly as you described.
[2109.66 --> 2118.64]  And to make that a bit more, to give a practical example of how that could look, many times ideas start in a chat.
[2118.64 --> 2122.94]  Like, we ship with Metamask, but many people use Slack.
[2123.50 --> 2126.82]  And we want to make sure that those ideas don't die.
[2127.26 --> 2133.30]  So we're going to ship with something that allows you to say, create an issue of the last 10 comments I made.
[2133.82 --> 2138.88]  And then that issue should end up on a planning board.
[2139.30 --> 2142.84]  So last month, we shipped an issue board with GitLab.
[2142.84 --> 2156.72]  And then to make it easier to pick up an issue and to start coding on that, we're shipping now with an online IDE, where on any repo, you can say, start my IDE.
[2157.84 --> 2162.78]  And then seconds later, you have a terminal with everything set up.
[2162.78 --> 2167.74]  So maybe that doesn't help you if you've already been working on the same project for a year.
[2168.12 --> 2173.84]  But if you're new to a project or you just want to make a small contribution, that changes a lot of things.
[2173.96 --> 2174.82]  That makes it easier.
[2175.86 --> 2179.90]  And another thing, like Google Docs, we also use it extensively.
[2180.46 --> 2189.48]  I've been thinking I would really love if the description field of issues and MergerQuest was a real-time document.
[2189.48 --> 2192.84]  So I have a Google Doc right there.
[2193.46 --> 2198.02]  Because many times a Google Doc is basically a substitute for an issue in our company.
[2198.80 --> 2200.82]  And we're also looking at that.
[2201.00 --> 2205.18]  We haven't decided whether we'll ship it, but we're actively thinking to make that better.
[2205.48 --> 2208.90]  So that you can have it within one tool chain.
[2209.62 --> 2214.28]  And if you have it within one data store, you can do the threading a lot better.
[2214.56 --> 2215.78]  But you can also do the feedback.
[2216.12 --> 2218.16]  Like where is stuff getting stuck?
[2218.16 --> 2223.90]  You know, I think part of this conversation for us to have you back on the show is kind of three parts.
[2224.08 --> 2225.46]  And this is how I look at it.
[2225.54 --> 2228.32]  Like it's a catch-up show because we haven't had you back on since 2013.
[2228.98 --> 2231.18]  Part of it is also talking about this master plan.
[2231.24 --> 2238.16]  But also part of it is kind of differentiating what GitLab is as a Git code repository code source.
[2238.16 --> 2245.04]  Which in a lot of cases over the years you've been very closely compared to GitHub or even Bitbucket.
[2245.04 --> 2252.64]  And when software developers look at these platforms to choose, they think, well, okay, either one, where's the community?
[2252.96 --> 2254.20]  Or why should I use it?
[2254.26 --> 2255.64]  Or what should my company use?
[2255.66 --> 2257.46]  Or what provides me the better thing here?
[2257.46 --> 2267.34]  And I think what is interesting about what you shared yesterday and the things you're talking about is rather than just saying, hey, we're the best place to host your code.
[2267.76 --> 2270.80]  It's, hey, we're the best place to develop your product.
[2270.80 --> 2276.36]  And it seems like that's what you're saying versus just simply host your code here, basically.
[2277.06 --> 2277.72]  Yeah, exactly.
[2278.00 --> 2281.94]  We want to be the best place to collaborate.
[2282.34 --> 2290.74]  And we think that an integrated software developer lifecycle is way better than using multiple tools.
[2291.04 --> 2293.70]  And it's something that wasn't intuitive to me.
[2293.70 --> 2301.06]  When Dimitri started making GitLab CI a couple of years back, I was like, no, let's focus on the code hosting.
[2301.20 --> 2303.34]  There's so much left to improve.
[2303.98 --> 2309.62]  But he, as a co-founder and original offer, he can do as he pleases.
[2309.98 --> 2310.86]  And he reached the start.
[2311.64 --> 2312.74]  He's got the code editor.
[2313.30 --> 2313.58]  Yeah.
[2314.32 --> 2320.70]  And it turned out he solved, by integrating it closely with GitLab, it was a much better experience.
[2320.94 --> 2322.40]  It was easier to set up.
[2322.40 --> 2324.34]  It was easier to get started with.
[2325.62 --> 2331.76]  And then the push came to, the suggestion came, let's integrate this GitLab CI app with GitLab.
[2332.96 --> 2336.88]  And I was not in favor in the beginning.
[2337.08 --> 2340.00]  I was like, we already have a giant monolithic app.
[2340.12 --> 2341.12]  Like, what are you doing?
[2341.16 --> 2347.76]  You're making a monorail out of this, a monorail as in a huge Rails app.
[2348.32 --> 2351.72]  This is not, this is not, this is against all the best practices.
[2351.72 --> 2352.78]  We shouldn't do this.
[2353.28 --> 2355.52]  And it took a bit of time for me to come around.
[2355.66 --> 2358.26]  But our CI lead also said the same thing.
[2359.16 --> 2361.22]  And we integrated it.
[2361.40 --> 2364.04]  And it's so, it's a so much better experience.
[2364.46 --> 2370.08]  And now, if you look at places like Hacker News, people say, I'm using GitLab.
[2370.08 --> 2376.64]  And I could replace not only our Git hosting tool, I could also replace our CI tool.
[2376.64 --> 2381.12]  I could also replace the Docker registry for private containers.
[2381.12 --> 2385.74]  And not only could I replace it, but it was so much easier to set up.
[2385.96 --> 2388.28]  I spent days setting up all these old products.
[2388.70 --> 2391.84]  And these products, it was a question of minutes.
[2392.34 --> 2397.72]  Because it's integrated, you don't have to ferry credentials around to the private container registry.
[2398.14 --> 2403.34]  No, your CI runner knows it's the CI, it's running their project and can push the containers to there.
[2403.34 --> 2408.58]  And so, it's a better experience.
[2409.36 --> 2412.52]  And that was counterintuitive to me.
[2412.96 --> 2414.98]  I like the Unix philosophy.
[2415.38 --> 2417.40]  You had one tool, there's one thing.
[2417.40 --> 2424.20]  But what I'm seeing more and more is that it is a very complex thing to make software.
[2425.16 --> 2427.68]  And that we're using these collections of tools.
[2428.68 --> 2434.32]  And if we integrate them together, over 1,000 people contributed to GitLab.
[2434.46 --> 2439.26]  So, if we get all the best practices of the best people in the world, and we integrate them into a tool,
[2439.68 --> 2445.38]  we just prevent a whole bunch of needless push-ups that you now have to do.
[2445.38 --> 2451.88]  And I can't compare GitLab to the genius of Ruby on Rails.
[2452.50 --> 2455.78]  But I was greatly inspired by convention over configuration.
[2456.66 --> 2461.28]  And I still think there's a lot of needless configuration in many developer pipelines.
[2461.52 --> 2463.88]  And we want to take that away.
[2464.22 --> 2468.00]  If you want to go fully GitLab, it's going to be an amazing experience.
[2468.16 --> 2470.00]  If you want to use other tools, that's fine too.
[2470.26 --> 2474.04]  We'll play nice with Slack, with great DERA integration.
[2474.04 --> 2476.90]  We have a commit status API for Jenkins.
[2477.20 --> 2478.76]  We'll play nice with other tools.
[2479.14 --> 2485.20]  But we're going to save you a whole bunch of time to make this idea to production happen.
[2485.20 --> 2487.04]  I think that's the key right there.
[2487.04 --> 2493.70]  Because the doubts in my mind as you're talking is whenever you have, when you lose that focus, like you said,
[2493.74 --> 2499.74]  and I do believe in integrated products for sure, when done right, and therein lies the risk,
[2500.36 --> 2505.02]  is providing everything you need for this style of development.
[2505.02 --> 2506.90]  There's many tools involved.
[2506.90 --> 2513.80]  And I know you guys have laid out kind of a 10-stop or a 10-step thing where some things you provide,
[2513.96 --> 2516.74]  some you don't yet, but you're planning on it.
[2516.74 --> 2521.24]  Is that if you have 10 things you need to provide for an integrated solution,
[2521.40 --> 2528.00]  and I'm down with eight of your products, but those other two completely contradict the way that I believe,
[2528.10 --> 2532.12]  or I hate them, or whatever it is, you've lost me.
[2532.28 --> 2535.58]  Because now it's a one-stop shop, so it's all or nothing.
[2535.58 --> 2545.26]  But it sounds like there still is opt-out type of a la carte style planned for this as well.
[2546.24 --> 2552.24]  Yeah, we want to convince you that it's a better experience, but we don't want to force you.
[2552.92 --> 2558.42]  So you can use just GitLab for code hosting and code review, and that will work fine.
[2558.42 --> 2566.62]  But right now we identified 10 stages, and eight of those 10 are now shipping with GitLab.
[2566.82 --> 2567.96]  It ships with Mattermost.
[2568.40 --> 2570.06]  It ships with an issue board.
[2570.56 --> 2571.98]  It ships with an issue tracker.
[2572.28 --> 2574.32]  It ships with coding and online IDE.
[2575.04 --> 2578.68]  It ships with repo management to commit your code.
[2578.82 --> 2579.70]  It ships with CI.
[2580.34 --> 2581.42]  It has the code review.
[2581.82 --> 2583.94]  It has the continuous delivery.
[2583.94 --> 2590.34]  It has many other things we're still working on to improve that.
[2590.46 --> 2593.10]  For example, we want to ship with something called review apps.
[2594.14 --> 2596.72]  And then two things we're still working on.
[2596.94 --> 2597.40]  ChatOps.
[2597.88 --> 2602.24]  We're looking into a Slack bot right now because most of our users are still using Slack.
[2603.14 --> 2606.94]  But long term, we're thinking about integrating cog from Operable.
[2607.64 --> 2609.74]  And then last but not least, the feedback.
[2609.74 --> 2618.20]  This month, we'll ship the first iteration of cycle analytics that will start giving you feedback about how long it took you to get from idea to production.
[2619.16 --> 2621.96]  And so we're very close to shipping all 10.
[2622.28 --> 2625.86]  But that's not where it ends because then we didn't have to raise 20 million.
[2626.34 --> 2633.40]  The hard part is making it a better experience by better integrating them.
[2633.72 --> 2634.62]  So fewer clicks.
[2634.62 --> 2640.24]  Right now, we ship with coding and online IDE, but it's still a couple of clicks to set up the project.
[2640.82 --> 2648.62]  And what we want is if you look at an open source project and you like it and you want to contribute something, you press one button.
[2648.82 --> 2650.48]  You don't have to provide any credentials.
[2651.22 --> 2654.16]  And there you are in the terminal and the product is running.
[2654.16 --> 2660.22]  And to get there, we're going to invest a lot of time and resources to make that an awesome experience.
[2660.80 --> 2668.14]  Let me lay out the 11 points, I guess, is what it ended up being in your talk slash live stream yesterday.
[2668.66 --> 2670.20]  So number one was cycle time.
[2670.30 --> 2671.72]  Number two was review apps.
[2672.20 --> 2675.44]  This is all in terms of your one-stop solution for conversation development.
[2675.44 --> 2677.26]  So point one is cycle time.
[2677.38 --> 2679.18]  Point two is review apps.
[2679.30 --> 2680.92]  Point three is monitoring with Prometheus.
[2681.28 --> 2683.72]  Number four is embracing container schedulers.
[2685.40 --> 2688.32]  Point five is integrated but plays nice with others.
[2688.88 --> 2690.70]  Point six is version control for everything.
[2691.00 --> 2692.60]  Point seven is powerful chatbots.
[2693.12 --> 2694.78]  Point eight was online IDE.
[2694.98 --> 2696.42]  I think you mentioned coding there for that.
[2697.06 --> 2700.60]  Point nine was speed improvements, which who doesn't want things to be faster?
[2701.36 --> 2702.32]  Like no one said make it slower.
[2702.32 --> 2706.24]  Point ten was ease migration from legacy systems.
[2706.40 --> 2709.92]  And point eleven was whatever you contribute and our customers request.
[2710.12 --> 2713.24]  So that was the point you kind of made in terms of this one-stop shop.
[2713.40 --> 2719.04]  But when we break things down like the IDE part, it seems like that was sort of like maybe experimental.
[2719.44 --> 2721.00]  And there was a collaboration there with coding.
[2721.20 --> 2723.54]  Is that something that you'll take over yourself eventually?
[2723.80 --> 2726.02]  Will you acquire them?
[2726.20 --> 2728.08]  Do you plan to make your own thing there?
[2728.62 --> 2730.06]  Can you break that down for me?
[2730.06 --> 2734.98]  Yeah, we want to reuse the best solutions that are out there.
[2735.28 --> 2739.50]  So we have no plans to make something ourself or to do something else.
[2739.92 --> 2742.58]  Coding, we were in a conversation with coding.
[2742.94 --> 2750.96]  And we were so much aligned on the vision for the future that they decided to open source their code base.
[2751.00 --> 2752.38]  So we could ship it in GitLab.
[2752.72 --> 2757.60]  Because any major part of GitLab will also have an open source component to it.
[2757.60 --> 2758.92]  And they did that.
[2759.04 --> 2764.24]  And it's now we've announced it.
[2764.96 --> 2767.58]  But it's not a great experience yet.
[2767.70 --> 2768.84]  It's hard to set up.
[2768.98 --> 2770.72]  There's still screens to click through.
[2771.16 --> 2774.98]  So now the real work has started of making that easier.
[2775.52 --> 2777.18]  And that's where our focus is.
[2777.18 --> 2782.04]  And I think that that also goes for Mattermost.
[2782.20 --> 2785.16]  Although Mattermost is the integration is deeper.
[2785.26 --> 2786.82]  It ships by default with GitLab.
[2787.14 --> 2790.12]  The OAuth authorization is completely integrated.
[2790.96 --> 2792.68]  But there's more we can do.
[2793.22 --> 2796.94]  And it's a project that will never be completely done.
[2797.66 --> 2803.32]  But the things you just outlined are things that are priorities for us for the rest of the year and for next year.
[2803.32 --> 2806.00]  Where we want to make this a better experience.
[2806.60 --> 2808.02]  Something else you said there too.
[2808.18 --> 2809.40]  And I'm not sure if I just heard it right.
[2809.56 --> 2810.58]  Did you say COG?
[2811.00 --> 2812.30]  Was it a product called COG?
[2812.66 --> 2813.44]  Yeah, exactly.
[2813.82 --> 2814.28]  What is that?
[2814.92 --> 2815.52]  C-O-G.
[2816.56 --> 2818.84]  You might have heard of Ubot.
[2820.06 --> 2821.48]  It's a ChatOps client.
[2821.96 --> 2826.74]  And ChatOps is something that allows you to say, for example, deploy staging to production.
[2826.74 --> 2830.28]  It will take whatever is on staging now and deploy it to production.
[2830.28 --> 2835.92]  Um, Ubot, um, was a great innovation there.
[2836.40 --> 2840.52]  Um, but the people of COG try to take it one step further.
[2840.90 --> 2843.70]  And what they're doing, uh, that I think is great.
[2843.80 --> 2850.70]  They have permissions, user-based permissions, uh, at a much deeper level in the product.
[2851.06 --> 2856.22]  Because with many chatbots today, you don't have really have privileges.
[2856.22 --> 2858.90]  As soon as you can access the chatbot, you can do everything.
[2858.90 --> 2863.40]  And for many teams, especially these larger enterprises, that's not acceptable.
[2864.02 --> 2866.82]  Another problem is many scripts can do everything.
[2867.06 --> 2871.42]  So you can have one person making a mistake in a script and then pulling down the entire
[2871.42 --> 2872.34]  production environment.
[2872.72 --> 2874.96]  Many of our customers, that's not acceptable.
[2875.28 --> 2881.06]  So COG splits it up into a coordinator and individual script.
[2881.20 --> 2882.84]  Those run on different containers.
[2883.54 --> 2886.88]  And an additional advantage, you can use the programming language that you like.
[2886.88 --> 2892.16]  Also, they've done some nifty things where you can have, where you can use like comment
[2892.16 --> 2898.42]  line syntax with pipes to stream the output of one script as an input to the other.
[2899.48 --> 2901.68]  So we think they're onto something.
[2902.04 --> 2903.14]  It's still early.
[2903.58 --> 2907.04]  It's still hard to use right now, or it's still hard to set up.
[2907.04 --> 2909.62]  But we think it's the future.
[2910.22 --> 2913.74]  And we're working with them to ship them with GitLab in the future.
[2914.56 --> 2915.24]  COG is very cool.
[2915.30 --> 2919.46]  This had not crossed, I guess I can say, Adam's radar either, but definitely not my own.
[2919.80 --> 2924.90]  And so as you talk, we are linking it up in the show notes and checking it out on their
[2924.90 --> 2925.18]  readme.
[2925.74 --> 2927.14]  You mentioned that it's still early.
[2927.38 --> 2932.16]  Their status actually says it's public alpha and not currently recommended for mission
[2932.16 --> 2933.20]  critical workflows.
[2933.20 --> 2936.76]  So I hope you all know what you're doing as you get this thing integrated.
[2937.32 --> 2939.20]  That's part of that collaboration to make it better.
[2939.84 --> 2939.98]  Yeah.
[2940.58 --> 2946.06]  Sid, one of the points in your focuses for the next year or so is version control for everything.
[2946.90 --> 2949.66]  And I believe that means large files.
[2949.90 --> 2955.68]  But I'm wondering if that also has any vision towards versioning things that are not code
[2955.68 --> 2958.88]  or files like database or data in general.
[2958.88 --> 2966.68]  Yeah, it means making version control more accessible because right now a lot of developers
[2966.68 --> 2970.02]  are using it, but a lot of design teams are not yet using it.
[2970.70 --> 2972.50]  So an example is large files.
[2972.98 --> 2976.46]  We think GitHub did a great job with Git LFS.
[2977.62 --> 2979.28]  Right now that's an extension.
[2979.78 --> 2985.70]  We'd love for it to be included in the Git binaries, basically.
[2985.88 --> 2987.60]  So we're paying someone to work on that.
[2987.60 --> 2993.96]  A thing we shipped ourselves is file locking, where you can lock certain files, binary files,
[2994.12 --> 2999.68]  to prevent other people from working on them at the same time and overriding your changes.
[3000.54 --> 3004.52]  That is something we ship, but we think we can still improve and make better.
[3005.52 --> 3008.82]  And there's also an example that says comments on images.
[3008.82 --> 3017.30]  If you have an image div, you basically want only sometimes you comment about the whole image,
[3017.38 --> 3019.64]  but sometimes you want to comment about a specific part.
[3020.36 --> 3025.28]  And I think we can do a better job of allowing that.
[3025.70 --> 3027.08]  So that's a feature we want to ship.
[3028.08 --> 3028.30]  Very cool.
[3028.34 --> 3031.38]  Any thought on data stores or data in general?
[3031.38 --> 3038.88]  I know Max Ogden has a very interesting project called DAT, which is trying to be version control for data sets.
[3039.04 --> 3045.42]  I know that's popular in scientific communities as well as a few others.
[3045.60 --> 3050.32]  But any thoughts towards that in terms of bringing data into the product development lifecycle?
[3050.32 --> 3053.08]  I think it's a very interesting subject.
[3053.80 --> 3057.42]  And there's a company called Pekider that is doing great work there,
[3057.56 --> 3063.16]  where they're trying to bring the version control of Git to the Hadoop space, basically.
[3063.94 --> 3065.84]  And they're doing amazing work there.
[3066.24 --> 3068.32]  We don't have any plans at the moment.
[3068.82 --> 3073.98]  But what we like is that because GitLab is open source, people can build upon it.
[3073.98 --> 3079.26]  So, for example, there's a site called PenFlip that allows you to write a book collaboratively.
[3079.94 --> 3082.40]  And they base their project on a fork of GitLab.
[3082.72 --> 3086.98]  And we try to do the best things that the community is building on top of GitLab
[3086.98 --> 3089.82]  and learn from that to make GitLab more user-friendly.
[3090.62 --> 3094.96]  It's really interesting to learn a lot about this idea of conversational development.
[3095.12 --> 3101.18]  I know that this is kind of an extension to Agile, and we all know your passion for that, Sid.
[3101.18 --> 3106.34]  So it's just kind of interesting to kind of dive through each of these points and ask a ton of questions.
[3106.46 --> 3109.46]  I'm sure we've got tons more, but we're going to break here real quick.
[3109.66 --> 3112.68]  And when we come back, we're going to dive a little further into some of these points.
[3113.10 --> 3118.30]  We also have some questions around just the Enterprise Edition and the overall ecosystem you're building
[3118.30 --> 3123.56]  and how that begins to continue to play out and how maybe even those who are listening
[3123.56 --> 3128.56]  can start to get involved in what GitLab is doing and moving things forward.
[3128.56 --> 3130.26]  So we'll break and we'll be right back.
[3131.18 --> 3137.04]  If you want to learn something new, a proven method is to learn by doing.
[3137.42 --> 3139.44]  And that's exactly the way CodeSchool works.
[3139.80 --> 3142.94]  You learn to program by doing with hands-on courses.
[3143.36 --> 3148.70]  Their courses are organized into paths based on technologies like HTML, CSS, JavaScript,
[3149.26 --> 3155.74]  with hot topics like React and Angular, Ruby, Python, .NET, iOS, Git, databases,
[3155.74 --> 3158.62]  and even electives that take you off the beaten path.
[3158.62 --> 3165.12]  You can try before you buy with free introductory courses like Git, Ruby, Angular, iOS, and more.
[3165.36 --> 3169.30]  And you get to play full courses with coding challenges so you can get the hang of things.
[3169.66 --> 3171.24]  There's a path for everyone at CodeSchool.
[3171.48 --> 3174.54]  Head to CodeSchool.com to get started and learn by doing.
[3174.54 --> 3185.26]  All right, we're back with Sid and we're talking about the master plan of GitLab.
[3185.50 --> 3188.60]  And Sid, I think it's awesome, too, that you guys did this live stream.
[3188.72 --> 3193.48]  You did it in a pretty good fashion, too, except for the unmuted mic during the demo.
[3194.18 --> 3195.70]  Pretty much a stellar performance.
[3195.98 --> 3197.28]  I think it was pretty awesome.
[3197.28 --> 3202.80]  But it's a great way, too, to communicate to the community what you're doing.
[3203.68 --> 3208.16]  And one of the things that was mentioned there was regarding this idea of ecosystem,
[3208.30 --> 3211.34]  this comparison to Atlassian and the ecosystem of developer tools.
[3211.92 --> 3217.88]  I think you even alluded to it earlier, having this monorail or even monolith idea.
[3218.22 --> 3223.38]  But you mentioned having all the tools have one data store, right?
[3223.38 --> 3228.10]  And you talked earlier about being able to track and the cycle time frame and all this different stuff.
[3228.28 --> 3234.20]  But can you expand on what you mean by cycle analytics and how those who may not be using,
[3234.32 --> 3237.84]  since it's a new paradigm, you're creating this conversational development process,
[3238.26 --> 3242.20]  how they're missing out on the details learned from understanding your cycles?
[3243.20 --> 3243.34]  Yeah.
[3243.58 --> 3245.74]  So GitLab has one data store.
[3246.28 --> 3248.80]  Most of the data is in Postgres.
[3248.80 --> 3255.80]  So even though we ship it matter most as a chat client, they will store the data, too, in Postgres.
[3256.12 --> 3257.76]  So we can do analytics there.
[3259.70 --> 3267.10]  Cycle analytics will show you how long you spend in every part of the process.
[3267.44 --> 3271.96]  So it will show you, OK, you were chatting about something.
[3272.08 --> 3276.02]  How long did it take you to convert that into an issue?
[3276.02 --> 3278.64]  How long did it take you to plan that issue?
[3279.18 --> 3284.34]  How long did it take you, after planning it, to boot up the IDE, start coding on it?
[3284.78 --> 3288.26]  And after you committed it, how much time did the CI take to run?
[3288.76 --> 3290.92]  How much time did it spend in a merge request?
[3291.62 --> 3295.62]  How much time did it spend in an acceptance or a staging environment?
[3296.26 --> 3300.44]  How long did it take you to then deploy it and get it out for real?
[3300.44 --> 3311.12]  So we think that showing this enables a conversation with your team and the rest of the organization about what you can do to improve it.
[3312.10 --> 3319.66]  And this is very new and we'll ship the first iteration of Cycle Analytics this month on the 22nd of September.
[3320.74 --> 3323.22]  But I think it's going to be really interesting.
[3323.22 --> 3330.36]  And I think, for example, that many companies will find they plan something and then it takes a really long while before they can start on it.
[3330.76 --> 3332.64]  And that will open up the conversation.
[3335.74 --> 3337.52]  What's most important to plan when?
[3337.92 --> 3343.08]  Can we just decide a month before we start doing something to do something?
[3343.66 --> 3345.32]  Maybe we're planning too far out.
[3345.58 --> 3349.76]  Why are we building two or three quarters of features?
[3349.76 --> 3355.84]  Don't you know the quarter beforehand much better what you need next quarter than half a year ago?
[3356.58 --> 3362.20]  So those are the types of conversations we want to enable in teams.
[3362.82 --> 3375.40]  And yeah, we look forward to people using that and improving it and starting to reap the benefits of reducing that time and having that sense of progress and getting more information and being able to respond faster.
[3375.40 --> 3383.12]  Can you share a bit about what the interface might be or just sort of like what the user might see in terms of what this is?
[3383.18 --> 3384.10]  Is it reporting?
[3384.40 --> 3387.08]  Is it something that somebody has to be interactive with?
[3387.12 --> 3399.86]  Or is it simply like a, you know, algorithm searching your data set and pulling back some, you know, some pointers basically towards how long things played in certain cycles, as you mentioned in your answer there?
[3399.86 --> 3401.18]  Yeah, of course.
[3401.32 --> 3402.48]  There's a public issue.
[3402.82 --> 3407.12]  And I just chatted it to you and you'll probably include it in the show notes.
[3407.82 --> 3411.64]  And to describe it to the listeners, at the top, you'll see the pipeline health.
[3411.96 --> 3413.80]  How many ideas did get shipped?
[3414.02 --> 3416.30]  How many issues did go close?
[3416.60 --> 3417.80]  How many people collaborated?
[3417.80 --> 3427.10]  And then on the left side, you see all the stages and how, what the median time was, what the 95th percentile time was.
[3427.98 --> 3435.52]  So it took you seven days to plan something on average or median time.
[3435.86 --> 3439.98]  And then on the right side, it will show you of the last deployments.
[3439.98 --> 3445.44]  This is how long ago someone first chatted about this idea.
[3446.06 --> 3450.40]  And that can be anything from a couple of hours to more than a year.
[3450.96 --> 3451.10]  Wow.
[3451.42 --> 3460.38]  I love that too, because I've done that where we've, you know, we're about to ship something or we're actually beginning to plan for it.
[3460.74 --> 3464.08]  You know, planning and talking about something is two different things.
[3464.08 --> 3474.06]  And it would be interesting to see, like, we actually talked about the need for this feature a year and a half ago when we had this issue or this support request or whatever might come from it.
[3474.20 --> 3480.92]  And so it'd be interesting to see that, like, auto-contrasting back to, like, here's when we really talked about it.
[3480.98 --> 3482.14]  Here's when we begin to plan it.
[3482.18 --> 3483.22]  And here's when we shipped it.
[3484.18 --> 3484.34]  Yep.
[3484.44 --> 3488.78]  And I think people will learn that the only way to get it down is to ship smaller things.
[3489.16 --> 3493.68]  So the picture you're looking at will not be our first iteration of cycle analytics.
[3493.68 --> 3500.16]  We'll ship only the minimum, minimum product first and then iterate on it.
[3500.88 --> 3508.32]  And I think that's the big lesson we learned at GitLab and what I saw going wrong in lots of other organizations.
[3508.92 --> 3515.84]  If you just add anything that you think might be useful to an issue, you're probably overbuilding it.
[3516.08 --> 3521.70]  So it's much better to start small and then just listen to the feedback and iterate on that.
[3521.70 --> 3528.38]  And listeners, I was going to say just for the listeners real quick, the issue that we're talking through, it's a little visual.
[3528.62 --> 3532.32]  So if you want to pause and go to the show notes, it's issue 847.
[3532.56 --> 3536.74]  But we have a link in the show notes if you want to go find that, you'll be easily be able to find it.
[3536.84 --> 3539.88]  So if you want to pause, go find that, come back and start listening again, you can.
[3540.00 --> 3540.88]  But go ahead, Sid.
[3540.88 --> 3549.56]  Yeah, I think it's such a better experience if you build the smallest possible thing.
[3550.18 --> 3556.48]  But if you have to wait half a year or two for the next iteration, you're not going to build the minimal thing.
[3556.72 --> 3563.54]  As soon as you got time for your feature, you're going to put everything you can possibly think of in there and request it.
[3563.74 --> 3566.86]  Because it will be half a year before you can request anything else.
[3566.86 --> 3572.66]  So in order to do small iterations, you need to get your cycle time down.
[3572.86 --> 3575.30]  Otherwise, your stakeholders will never agree with it.
[3576.48 --> 3583.22]  So cycle analytics seems like it's very much dependent upon comparing apples to apples.
[3583.36 --> 3587.60]  I mean, we talk about this development style, it's idea to production, right?
[3587.62 --> 3588.30]  There's your cycle.
[3588.72 --> 3590.14]  Some ideas are bigger than others.
[3590.14 --> 3595.24]  And one of the things that I struggle with all the time, of course, we're always trying to deal with the smallest things possible.
[3595.88 --> 3598.36]  But things tend to grow, as we all know.
[3598.96 --> 3601.14]  And it's like defining what is a singular idea.
[3602.04 --> 3603.36]  You know, this is a bug fix.
[3603.46 --> 3605.88]  Are we doing cycle analytics on this bug fix?
[3606.26 --> 3611.74]  And then here's an idea called, you know, a cycle analytics feature, which is a huge idea.
[3613.02 --> 3616.68]  How do we normalize these things so that the analytics are useful?
[3616.68 --> 3622.32]  I think the lesson is that if something is larger, you have to split it up.
[3623.26 --> 3628.16]  And we've never found an instance where we could not make a smaller iteration.
[3629.72 --> 3636.06]  In GitLab right now, many things, basically everything has to ship in the same month you start on it.
[3636.34 --> 3638.60]  So you start on it and you want to ship with that release.
[3638.88 --> 3642.52]  Sometimes it's only one or two weeks that you have left before it ships.
[3642.52 --> 3648.52]  And for example, cycle analytics, I hope it will ship, but it was built in a month.
[3649.06 --> 3652.42]  And that's because we didn't do the whole thing we designed here.
[3652.52 --> 3657.20]  We did just the minimum thing we could ship in those weeks that were left.
[3657.60 --> 3660.30]  And we've seen it even with very complex features.
[3660.56 --> 3663.44]  For example, we did issue boards.
[3663.44 --> 3668.34]  That's like a whole extension of the product.
[3668.60 --> 3670.32]  And that took us two months.
[3670.44 --> 3671.32]  So we're not happy.
[3671.42 --> 3672.74]  We should have done it in one month.
[3672.92 --> 3674.60]  We can learn.
[3675.46 --> 3682.66]  But I think if you add everything in there that you can think of, you're easily spending more than half a year to ship something like that.
[3683.66 --> 3685.44]  The trick is to do the minimum thing.
[3685.64 --> 3687.54]  And we shipped it last month.
[3687.54 --> 3689.36]  And this month, we have all kinds of improvements.
[3689.36 --> 3693.08]  Because people had like, oh, you can do this and that and this and that.
[3694.00 --> 3698.20]  And splitting something up, sometimes it's hard.
[3698.32 --> 3700.22]  It depends on the feature, what it is.
[3700.82 --> 3705.66]  But the thing is that there is an incentive to make it smaller because you want to reduce the time.
[3705.72 --> 3709.78]  Instead of having the incentive to make it bigger because otherwise you have to wait so long.
[3710.22 --> 3714.54]  So if the incentive is right, you can make everything smaller.
[3714.54 --> 3718.54]  And it seems counterintuitive.
[3719.60 --> 3722.18]  But for us, we've always been able to do that.
[3722.38 --> 3728.40]  Even with big things like rewriting, switching JavaScript versions and stuff like that.
[3728.40 --> 3738.80]  The two final aspects of conversational development that you've laid out and that you're trying to achieve ability with GitLab are kind of related.
[3738.92 --> 3741.66]  The gatekeeper is a big part of the conversation.
[3742.32 --> 3745.24]  And the rest of the organization can contribute.
[3745.62 --> 3747.58]  Let's just focus on the gatekeeper for now.
[3750.08 --> 3750.64]  Tools.
[3752.22 --> 3755.72]  Sharp tools are usually very specific uses.
[3755.72 --> 3760.92]  And so when we have a broad range of people using the same tools.
[3761.18 --> 3772.70]  So we go everywhere from the back-end engineer using it to QA using it to product dev or the product designer, even to the stakeholder.
[3773.14 --> 3774.66]  There's somebody in upper management.
[3774.66 --> 3780.26]  And you're trying to bring all those people to the same conversation, to the same place.
[3781.22 --> 3787.10]  There are a lot of challenges there with user interface, with interactions, with workflows.
[3788.82 --> 3794.48]  Do you guys, are you guys actively thinking about how you can build a single tool that works well for all these different stakeholders?
[3795.50 --> 3797.26]  Yeah, we think that's extremely important.
[3797.92 --> 3801.22]  And I'm sure that there's still many things we can still improve.
[3801.22 --> 3810.12]  But I think that companies and higher management are getting more comfortable with using things like this.
[3810.68 --> 3813.30]  I think the popularity of Slack is an indication.
[3814.32 --> 3816.48]  That's not just developers using that.
[3816.62 --> 3818.90]  That is multiple people in the organization.
[3819.74 --> 3819.78]  Right.
[3819.82 --> 3825.12]  For example, in GitLab itself, our marketing team also works from an issue tracker.
[3825.52 --> 3826.58]  It's a public one.
[3826.66 --> 3828.60]  So I encourage you to check it out.
[3828.60 --> 3831.36]  But they've been able to adopt that.
[3831.46 --> 3836.48]  But we've also learned, for example, they insisted that issues would have due dates.
[3836.96 --> 3840.90]  And all the programmers were, yeah, just plan a sprint and assign a due date to a sprint.
[3841.12 --> 3842.66]  And they were like, well, that's not how we work.
[3842.76 --> 3846.34]  We want the due dates also in the individual issues.
[3847.00 --> 3847.92]  So we learned.
[3848.24 --> 3848.92]  We added that.
[3849.18 --> 3854.90]  And I'm sure there's many other things we can improve in GitLab to make it easier to use.
[3854.90 --> 3863.28]  But I think that many people higher up now feel frustrated about the lack of control and the lack of information they have.
[3863.48 --> 3866.32]  They basically throw a whole lot of demands in there.
[3866.42 --> 3869.50]  And then they have to wait half a year before it gets out.
[3869.50 --> 3879.72]  I think they'll be delighted if they can give a big idea, work together to make it smaller, and then have some output a week or two later.
[3879.72 --> 3893.24]  One of the things that I've noticed about you and your team, just as your announcements and products do make their way across Hacker News and other mediums or media, is that you're very receptive to feedback and feature requests.
[3893.24 --> 3901.24]  And you're very quick to add something to your issue tracker or even say, oh, yes, we're actively working on this.
[3901.34 --> 3904.80]  I was thinking about even just your most recent post.
[3904.80 --> 3918.18]  It may have been Dimitri in there saying one of the requests is about on issues on code review, which is a huge aspect for all of us, is better code review tools, which I'm sure you guys are furiously working on.
[3918.64 --> 3926.62]  And one aspect is like, can I just batch up my comments and send a single notification, which is something, Adam, that I've complained about many times.
[3926.80 --> 3927.12]  Yes, you have.
[3927.12 --> 3932.44]  Especially as we use these tools to do editing of prose.
[3932.82 --> 3940.82]  So we have a bunch of feedback on something somebody's written, and I have 17 things to say, and I just feel terrible as I'm going through saying those things.
[3940.96 --> 3946.02]  And I send 17 emails to somebody about specific grammar checks and stuff like that.
[3946.02 --> 3957.34]  And right in there, there was a comment from somebody on your team that said, I just added that to our list of feature requests, or we're tracking that and we'll consider it.
[3958.08 --> 3960.78]  And that is very cool.
[3960.78 --> 3971.68]  And this desire to feed the entire organization a singular place to do the software development and a singular tool or set of tools is very cool.
[3972.14 --> 3973.70]  Do you worry about feature bloat?
[3973.76 --> 3978.94]  Because if you do all the things, surely you may end up with too many things.
[3980.08 --> 3980.24]  Yeah.
[3980.46 --> 3985.08]  So you don't do everything that you have a feature proposal for.
[3985.08 --> 3988.52]  So there is more than a thousand feature proposals.
[3989.78 --> 3994.04]  But what is important is to have a place to track everything.
[3994.70 --> 3995.96]  So we're very liberal.
[3996.54 --> 4001.36]  If you have an idea and it's a good, make an issue so we can discuss it.
[4001.64 --> 4007.16]  And many times from the issue, we try to reduce it.
[4007.34 --> 4009.58]  Like what's the minimum we can do?
[4009.58 --> 4016.12]  And a minimum not in minimum lines of code, but adding minimal technical complexity to the product.
[4016.88 --> 4020.76]  Like can we do something without introducing another database table?
[4020.88 --> 4023.54]  Can we do something without introducing another model?
[4023.76 --> 4027.76]  Can we do something without adding more bloat to the interface?
[4028.60 --> 4031.44]  When it's needed, yeah, make that extra database table, of course.
[4031.76 --> 4037.12]  But what's the minimum we can do so that we make it easy to extend the product in the future?
[4037.12 --> 4039.54]  And to do that, you need to have a conversation.
[4040.12 --> 4048.74]  And not only the initial offer of the idea needs to chime in, also other users with their use cases.
[4049.20 --> 4051.08]  And in our case, also our salespeople.
[4051.32 --> 4057.82]  You'll see comments on the GitLab issue tracker that says potential client with 300 users is interested in this.
[4058.02 --> 4061.42]  And then a Salesforce link that you guys can't access, but we can.
[4062.54 --> 4066.64]  That has more information about the client that wants that.
[4067.12 --> 4073.82]  So that as a community, you can see what was requested, all the different opinions.
[4074.20 --> 4077.70]  And then people start exploring, okay, what's the technical impact?
[4078.18 --> 4085.68]  And depending on the demand and the complexity, the product managers make a decision to schedule it or not.
[4085.68 --> 4090.32]  Or someone makes the code and then we're there.
[4090.40 --> 4094.14]  Then we're forced to do a review, which is a great thing.
[4094.38 --> 4096.06]  And we can take it from there.
[4096.06 --> 4099.44]  Well, let's talk about that batch commenting feature.
[4099.54 --> 4100.46]  What are the odds?
[4100.58 --> 4100.88]  Come on.
[4101.14 --> 4102.52]  Give us a...
[4102.52 --> 4104.08]  Let's get that in there.
[4104.72 --> 4112.94]  I saw that GitHub released transactional merge request comments, or they probably call it something else, today.
[4112.94 --> 4122.04]  So I'm sure that is an inspiration not only to us as a team, but also to our community to start thinking about that.
[4122.04 --> 4126.18]  That actually leads me into the question I was just about to ask next, so thank you.
[4128.08 --> 4131.86]  Somebody mentioned that that specific feature was in Fabricator, and I believe you chimed in.
[4131.96 --> 4140.12]  We'll link to the Hacker News thread because there's a lot of good conversation there around the master plan and whether or not people are bullish or bearish about your odds and all that fun stuff.
[4140.12 --> 4144.92]  But there's a mention of Fabricator, which is another tool that is praise.
[4145.00 --> 4147.00]  I've never used it, but praise for its code review.
[4147.50 --> 4155.82]  And you just mentioned GitHub made announcements, and it's hard to miss those today if you're on Twitter in the software development scene because there was people talking about it.
[4155.82 --> 4163.78]  How closely do you monitor your competitors and think about them in light of your product roadmap?
[4165.78 --> 4171.12]  Well, obviously, when they release new features, we pay attention.
[4171.70 --> 4179.28]  And I try to encourage us to also give a more fair comparison between their product and ours.
[4179.38 --> 4183.44]  So if they have a cool feature that we don't have, we try to add it to our comparison page.
[4183.44 --> 4187.38]  In the end, the feature still has to stand on its own.
[4187.70 --> 4194.64]  So it's input to the conversation, but that is it.
[4195.44 --> 4197.94]  And you're hearing some background noise here.
[4198.56 --> 4208.62]  We have a telepresence robot in the office, and someone just came into the office just right now, unaware, of course, that I'm in the middle of a recording.
[4209.04 --> 4212.36]  So we asked them to check in half an hour from now.
[4213.44 --> 4217.46]  But yeah, I think we look at each other.
[4218.06 --> 4221.66]  And it's great to see the inspiration is hopefully mutual.
[4222.14 --> 4224.50]  And I think we can all learn from one another.
[4224.90 --> 4227.04]  Certainly, Fabricator has been an inspiration.
[4227.78 --> 4231.86]  But it's, for example, we released GitLab issue boards last month.
[4231.86 --> 4237.48]  And now GitHub, who's probably started working on this a long time ago, but they also released it.
[4237.70 --> 4241.80]  So in some parts, we're thinking in the same direction.
[4242.28 --> 4250.86]  I think where we differ is that we clearly see the value of a product that's more integrated and has more convention over configuration.
[4250.86 --> 4255.24]  And it saves you a lot of setup time and clicking between different apps.
[4255.68 --> 4258.42]  So I think that's where we're clearly going in different directions.
[4258.42 --> 4262.82]  So, Sid, I got a hard question for you.
[4263.60 --> 4264.86]  A hard ball, so to speak.
[4264.98 --> 4266.00]  Maybe we'll say that.
[4266.68 --> 4274.40]  And the question is, I'm not exactly sure the best way to ask it, but I'm thinking about the listeners who are listening to this show.
[4274.48 --> 4277.92]  And they're thinking back to what I said earlier, which is, you know, how do I choose?
[4277.92 --> 4288.68]  How do I choose where to host my code, whether I'm an open source developer, I'm a self-run shop, I work on a team, I work in enterprise, I work on open source.
[4289.06 --> 4293.20]  How do I choose between GitHub, GitLab, Bitbucket?
[4293.64 --> 4295.52]  We talked a bit about your business model.
[4296.34 --> 4297.68]  People use the word winning.
[4298.38 --> 4301.28]  And I think what the better word might be is succeeding.
[4301.40 --> 4307.22]  Because I think that you can have an ecosystem of code hosts where you have all three of you and you all win.
[4307.92 --> 4310.58]  So, I don't think it's about, like, you're trying to beat any of these people.
[4310.70 --> 4318.00]  It's just you're trying to succeed at your own mission, which is obviously around this conversational development process and all these tools you're building around that.
[4318.14 --> 4328.42]  But I think the question I'm trying to figure out here is for those listening, and I think it's pretty fair to say that most of the audience that listen to this show is very familiar with GitHub.
[4329.08 --> 4331.36]  A little less familiar with GitLab.
[4331.64 --> 4335.84]  And that's not saying that, obviously, you're not succeeding or winning, so to speak.
[4335.84 --> 4342.94]  And then maybe even a little less familiar with Bitbucket, but very familiar with all three of you as code hosts.
[4343.46 --> 4348.84]  And I think the question, really, I'm trying to ask is, in terms of your mission, in terms of what you're trying to do, are you trying to...
[4349.62 --> 4352.52]  Do you see yourself trying to win developers away from GitHub?
[4353.54 --> 4354.82]  Do you see people...
[4354.82 --> 4357.88]  Are you trying to, like, garner people away from Bitbucket?
[4357.98 --> 4362.32]  Is that how this enterprise game is being played?
[4362.32 --> 4364.74]  Not so much your enterprise product, but just in general.
[4364.86 --> 4367.36]  Is that your plan to win or succeed?
[4367.52 --> 4368.82]  Is it to take people away?
[4369.22 --> 4375.98]  Or is it to have people's idea of how you develop software, evolve, that GitLab is just the better solution?
[4376.96 --> 4377.08]  Yeah.
[4377.24 --> 4378.66]  I think there's a bit of both.
[4379.30 --> 4383.00]  And so many enterprises are still not using Git.
[4383.20 --> 4384.50]  So that's an amazing market.
[4384.78 --> 4384.90]  Right.
[4384.90 --> 4389.16]  But as for our strategy, it's a public page.
[4389.38 --> 4391.72]  It's on aboutgitlab.com slash strategy.
[4392.04 --> 4394.28]  And we have a sequence in there.
[4394.52 --> 4398.52]  And the first step is to become the most popular on-premises.
[4398.72 --> 4399.58]  So behind the firewall.
[4399.88 --> 4400.94]  We succeeded there.
[4401.48 --> 4404.02]  And the next step is to get the most revenue.
[4404.02 --> 4408.46]  So that's why we're expanding marketing and sales.
[4408.70 --> 4415.14]  Because we want to make sure right now 99% of GitLab organizations are using the Community Edition.
[4415.46 --> 4419.34]  And we would like to have a higher percentage being a customer.
[4419.68 --> 4422.92]  So we want to add features to our Enterprise Edition to make it better.
[4423.94 --> 4429.40]  Not without stopping to ship features in the Open Source Edition, obviously.
[4429.40 --> 4435.56]  And then the next step is having a better experience for private repositories.
[4437.08 --> 4444.62]  Because we think that there are people that want to spend less time on integrating their tools and switching between tools.
[4445.36 --> 4455.40]  And you can see in that Hacker News thread, someone saying that it's just awesome to have one tab with your repo, one tab with your Docker containers, one tab with your deployment.
[4455.76 --> 4458.90]  It's a much better experience to have that all in one tool.
[4459.40 --> 4461.92]  So give me a more direct answer to that.
[4462.06 --> 4465.58]  And I think it's really awesome that you have your strategy listed.
[4465.94 --> 4475.92]  And not so much just listed for those who may come to love GitLab and use GitLab as developers or development teams of software and products.
[4476.50 --> 4478.14]  But even your competitors.
[4478.36 --> 4481.90]  I think it's just interesting to put that out there wide open and say, these are our goals.
[4482.04 --> 4483.30]  One is to do this.
[4483.38 --> 4484.28]  The second is revenue.
[4484.86 --> 4486.40]  Or have the most revenue, as you said.
[4486.40 --> 4494.44]  And maybe a bit more direct is winning developers away from GitHub, the open source world.
[4494.54 --> 4497.80]  A lot of the open source community tends to gravitate towards GitHub.
[4497.92 --> 4501.96]  It seems like, and Jared, we can even say this as part of Nightly.
[4502.06 --> 4503.96]  Like we have an email called changelog Nightly.
[4504.40 --> 4506.10]  Everything listed in there is a GitHub repo.
[4506.54 --> 4508.18]  None of them are GitLab repos.
[4508.18 --> 4513.08]  Is that part of your mission to sort of win some of the open source community?
[4514.42 --> 4514.68]  Yes.
[4515.02 --> 4519.80]  So if you look at our strategy, point four is win over the open source repos.
[4520.82 --> 4532.42]  And we're trying to, and we're making improvements already to the way open source projects like FGROID, how we host them on GitLab and making sure that's a great experience.
[4532.42 --> 4537.76]  But I think for the masses, we first want to do point three.
[4538.30 --> 4544.36]  Because there is a big network effect to open source projects hosted on SaaS.
[4545.64 --> 4550.26]  For private repositories on SaaS, that network effect is much reduced.
[4550.48 --> 4552.66]  It doesn't matter that much where you host your own projects.
[4552.66 --> 4563.12]  It doesn't matter if you invite a limited group of people, they can easily create accounts elsewhere or log into GitLab with their GitHub OAuth credentials.
[4564.04 --> 4566.72]  So that's why we have that sequence.
[4567.26 --> 4573.88]  And obviously, those private developers are now hosting their code either on GitHub or on Bitbucket or someplace else.
[4574.30 --> 4575.68]  So we make great importers.
[4576.22 --> 4578.68]  For Bitbucket, but our best importer is for GitHub.
[4578.68 --> 4586.16]  It transfers not only your repos, but also your issues, your pull requests, your labels, your milestones.
[4586.78 --> 4589.14]  And we want to make that an amazing experience.
[4589.84 --> 4598.36]  And we're getting more than a terabyte a day of new repos being created on GitLab.
[4598.50 --> 4600.78]  So we're seeing amazing growth there.
[4601.42 --> 4606.04]  One last question, I guess, on the enterprise side, especially since it's the underpinning to your business model.
[4606.04 --> 4611.36]  So if this fails, it might just be yet another failed experiment.
[4611.70 --> 4613.64]  Or I guess that's probably a bad way to say I shouldn't say it like that.
[4613.88 --> 4618.44]  But earlier in the show, you'd mentioned donations, the early goals of trying to be sustainable.
[4619.20 --> 4624.04]  And so now your enterprise edition is the moneymaker.
[4624.70 --> 4625.44]  It's paving the way.
[4625.60 --> 4631.74]  It's providing the sustainable financing to do what you do for the open source, the .com, the free version.
[4631.74 --> 4643.12]  And what can you share about the lay of the land in terms of enterprise edition or enterprise internal on-premise code stores?
[4643.40 --> 4645.38]  GitHub has their own version.
[4646.04 --> 4648.06]  Atlassian with Bitbucket has their own version.
[4648.24 --> 4650.08]  And obviously you have your enterprise edition.
[4650.78 --> 4652.08]  Is it, you know, who's winning?
[4652.60 --> 4653.86]  What's the goal there for you?
[4653.86 --> 4660.48]  And I guess what can you share with listeners about the, you know, the outlook of the future for you on that front?
[4661.38 --> 4661.58]  Yeah.
[4662.22 --> 4666.96]  I think we managed to become the most popular option there.
[4667.20 --> 4671.04]  So most organizations that hosted there, they use GitLab.
[4671.04 --> 4688.34]  And according to an article in a publication called The Information, where GitHub first focused on individual developers, then focused on the enterprise, they went back to focusing on individual developers again.
[4688.34 --> 4698.74]  So we have high confidence that these organizations will start consolidating on GitLab.
[4700.02 --> 4705.38]  And also previous generation solutions, like for example, Perforce.
[4705.50 --> 4709.00]  Perforce is shipping with GitLab to make that transition easier.
[4709.00 --> 4722.38]  So we think that we should keep listening to what these enterprise customers want, keep accepting and working with them to get their code changes accepted.
[4722.78 --> 4726.96]  And we can do a better job at promoting GitLab to the higher ups.
[4727.26 --> 4728.54]  So that's something we'll do.
[4728.70 --> 4733.72]  Many developers have heard of GitLab, but when you get to the CIO level, we're less known.
[4733.72 --> 4741.56]  So we'll spend more money on marketing to those groups of people.
[4742.82 --> 4743.64]  Well, so that's really...
[4743.64 --> 4746.38]  I'd like to go back to community real quick, if you'd let me.
[4746.56 --> 4747.10]  Do it, yeah.
[4747.70 --> 4747.92]  Cool.
[4748.64 --> 4755.70]  Because I had a thought about that, specifically around the point that Adam made with, you know, individual open source projects.
[4756.36 --> 4760.30]  GitHub is the de facto, you know, host for those things.
[4760.30 --> 4764.20]  We'd love to get GitLab into ChangeLog Nightly, by the way.
[4764.42 --> 4769.40]  We actually tried, but your API doesn't quite expose the data that we need in order to track such things.
[4769.98 --> 4777.56]  And I know you mentioned that your first goal is to get people contributing to GitLab open source, you know, the product, the community edition.
[4777.92 --> 4781.72]  And then after that, it's kind of win the hearts and minds of individual developers.
[4782.66 --> 4785.04]  What are your plans for when you get to that point?
[4785.18 --> 4787.82]  Like, how are you going to get the mind share?
[4787.82 --> 4797.46]  Because what you don't have in the individual space, which like you said, you also don't have quite at the CIO space, but you're working on that, is the mind share of those people.
[4797.66 --> 4806.50]  So amongst the open source world of developers putting their NPM stuff on GitHub or their latest, their .files are on GitHub.
[4806.60 --> 4807.40]  Everything's on GitHub.
[4807.66 --> 4810.52]  So what could possibly turn that tide?
[4810.58 --> 4812.22]  Because it's pretty established at this point.
[4812.22 --> 4815.50]  Yeah, so there's a huge network effect there.
[4815.98 --> 4819.16]  And that's why we're not attacking it head on.
[4819.48 --> 4821.98]  But we first want to convince individual developers.
[4822.62 --> 4829.68]  But I think as we grow more and more of our stack and of the modern software development lifecycle,
[4830.42 --> 4837.42]  I think that open source projects, at some point, they'll see that it's easier for people to contribute via GitLab.
[4837.42 --> 4845.94]  If you can press a button and then have a complete IDE, it makes it a lot easier to do a drive-by commit of a small thing you just found,
[4846.34 --> 4850.28]  instead of having to, dig to the readme, install all kinds of tools.
[4851.36 --> 4853.64]  That's a really good point on drive-by contributions.
[4853.88 --> 4859.40]  We have a show called Request for Commits, where we've talked extensively about onboarding contributors,
[4859.40 --> 4864.86]  graduating those contributors to people who contribute more than just once,
[4864.98 --> 4869.30]  but actually come back again and again and become established community members in that repo.
[4869.96 --> 4877.62]  But also just the allure of and the easy of, you make open source maintainers live so much easier
[4877.62 --> 4883.48]  when you make the drive-by contributions so much lower of a barrier to entry to do that.
[4883.48 --> 4887.58]  Because if I can go there and simply just drop in a readme update, that's great.
[4887.74 --> 4893.56]  But if I can actually launch an IDE, run the program, run the application, or do whatever's necessary,
[4894.26 --> 4901.24]  and drop in my wisdom, then it's a lot more likely for me to potentially become a better drive-by contributor
[4901.24 --> 4903.48]  or even a community member of that project.
[4904.32 --> 4904.36]  Awesome.
[4904.78 --> 4909.92]  And yeah, if there's anything we can do in the meantime, of course, we're not going to do this serially.
[4909.92 --> 4911.98]  There's a bit of parallelism going on.
[4912.30 --> 4918.06]  And if we can extend our API to make it work better with your nightly, then let's talk about that.
[4918.14 --> 4921.12]  And hopefully we can open an issue and discuss it.
[4921.28 --> 4922.48]  Well, we have an open issue.
[4923.00 --> 4926.12]  And we had a couple emails into some people at GitLab.
[4926.18 --> 4930.40]  I'm not calling you out, but we have a desire to make that work.
[4930.46 --> 4932.58]  So just so you know, we definitely have a desire.
[4932.96 --> 4937.52]  We didn't go onto your issue tracker and create an issue, but we've made some steps to make that happen.
[4937.52 --> 4942.08]  And even the readers of Change All Nightly have that same desire.
[4942.24 --> 4945.62]  So let's definitely collaborate and make that happen, because I know it's important to us,
[4945.66 --> 4948.40]  and it's important to the community who reads that email every night.
[4948.98 --> 4949.30]  For sure.
[4950.32 --> 4954.90]  This is how we get all of our feature requests done, Sid, is we bring people on the air,
[4954.94 --> 4958.78]  and then we wait till the right time, and then we shame them for not doing our features.
[4958.78 --> 4958.98]  Yeah.
[4960.86 --> 4971.42]  I mean, we have a lot of open issues, but I see that the people who are patient and that are constructive,
[4971.66 --> 4972.92]  in the end, they get it done.
[4973.34 --> 4979.46]  And a great example was someone contributed an auto-scaling CI runner for Kubernetes.
[4979.46 --> 4986.56]  So if you run a Kubernetes cluster, it will automatically spin up as many runners to run your tests as are needed.
[4987.14 --> 4991.02]  And it took this person a year to get it in.
[4991.22 --> 4995.84]  So we're not always doing great on cycle time, but in the end, they get it in.
[4996.10 --> 5000.26]  And if I review it, I think our team did great.
[5000.38 --> 5001.36]  This person did great.
[5001.36 --> 5007.96]  The only stupid person in that conversation was me not completely understanding Kubernetes a year ago.
[5008.84 --> 5009.68]  It happens.
[5009.92 --> 5011.02]  We all have our moments.
[5011.68 --> 5011.86]  Yep.
[5012.84 --> 5015.12]  One last question as we kind of wrap things up,
[5015.22 --> 5018.12]  and I'm thinking about the end of all software development processes
[5018.12 --> 5020.58]  as we talk about this post-agile world,
[5021.08 --> 5025.18]  and you trying to provide the one-stop shop for everything you need for conversational development.
[5025.86 --> 5029.22]  Cycle time is defined as from idea to production.
[5029.22 --> 5038.28]  And I know that you guys are introducing tools such as CI for testing and for continuous deployment.
[5038.52 --> 5041.48]  But what about the kind of end, the last mile, so to speak?
[5041.56 --> 5044.92]  Have you had thoughts of, you know, just deploy with us?
[5046.00 --> 5046.22]  Yeah.
[5046.42 --> 5048.28]  We want to make the last mile better.
[5048.52 --> 5050.80]  And there's lots of stuff happening in the last mile.
[5051.28 --> 5054.36]  And one of the things that's happening there is monitoring.
[5055.64 --> 5057.38]  And that's getting more and more important.
[5057.38 --> 5063.08]  And we're learning that you cannot do continuous delivery right without also adding some monitoring.
[5063.44 --> 5068.26]  So we're excited to start shipping with Prometheus, working on that,
[5068.44 --> 5071.90]  and allowing you to monitor the apps you deploy with Prometheus.
[5072.40 --> 5076.32]  If you're hinting at that, we also become a deployment platform.
[5076.72 --> 5077.04]  Yes.
[5077.04 --> 5078.82]  That's not our ambition.
[5079.12 --> 5084.62]  I think what we're seeing in the market is that there's great container schedulers.
[5085.34 --> 5087.66]  And for example, we can already deploy to Prometheus.
[5088.10 --> 5091.02]  And that is just a great pathway to deploy your app.
[5091.80 --> 5096.92]  If you look at our scope on the direction page, you'll see also what's not in scope.
[5096.92 --> 5103.48]  So we're doing a lot, but that is the point where we hand it over to a production environment.
[5104.34 --> 5112.34]  And we think that projects like Prometheus, Mesosphere, Terraform, Nomad are doing an amazing job there.
[5112.90 --> 5115.08]  And we want to work with them.
[5115.96 --> 5116.16]  Very cool.
[5116.16 --> 5118.98]  Well, so we have certainly kept you for a while.
[5119.18 --> 5123.16]  And listeners, I know we've gone over probably by a hair on this show.
[5123.24 --> 5125.48]  We had a great outline for this show.
[5125.54 --> 5126.80]  We knew we had a lot of catch up.
[5126.90 --> 5128.74]  We had a lot to cover in terms of the master plan.
[5128.82 --> 5134.66]  But we also had some hard questions for Sid, which he graciously took and answered for us here at the end of the show.
[5134.78 --> 5137.34]  But couldn't wrap the show without doing that.
[5137.34 --> 5141.40]  But Sid, this is a chance, I guess, for you, for us to turn things over to you.
[5141.48 --> 5143.48]  Is there anything that we haven't asked you?
[5143.48 --> 5150.26]  Any way or anything you want to share back to the community right now that is just something that's been on your mind that you have to say before the show wraps up?
[5150.98 --> 5155.88]  Yeah, I think you did a really good job of asking lots of questions.
[5156.14 --> 5159.30]  I hope that people will give GitLab a try.
[5159.30 --> 5168.08]  And then when they find something they don't like, they create an issue or they search for issues and voice their opinion so we can keep improving the product.
[5168.42 --> 5171.64]  Or even better, contribute some code to make it better.
[5171.64 --> 5174.14]  It's over a thousand people contributing.
[5174.70 --> 5176.24]  And I think that's the strength.
[5176.42 --> 5182.44]  And I think as a development community, we can just build a better tool that we can use every day.
[5183.18 --> 5191.76]  So one last quick question for you, which is one of our favorite questions to ask, which is just, you know, for those listening, you know, they hear you say that now and they're thinking, OK, I can contribute.
[5191.76 --> 5203.08]  Can you give a quick guidance towards what's the best way the community can step in and help this mission that you described yesterday, you know, in your grand plan?
[5203.32 --> 5205.44]  What's the best ways for people to step in?
[5205.52 --> 5207.48]  Is it is it stepping into issues?
[5207.54 --> 5212.38]  Is it installing, you know, the their own self-hosted version of it, playing with a container?
[5212.38 --> 5215.00]  Like, how can people best give back to GitLab?
[5215.44 --> 5216.50]  Yeah, use it.
[5216.72 --> 5217.76]  Use it where you want.
[5218.06 --> 5220.32]  Either the .com or install it yourself.
[5220.70 --> 5223.38]  And then you're going to find a rough spot somewhere.
[5223.72 --> 5227.46]  And maybe your documentation is a little off and there should be an example somewhere.
[5227.88 --> 5231.62]  Or maybe there's a feature missing or maybe something doesn't work in Safari.
[5231.62 --> 5235.46]  So create an issue or try to try to make some code.
[5235.80 --> 5240.30]  We have a contributing.md file that walks you to contributing to GitLab.
[5240.44 --> 5248.74]  And we now have Merch request coaches, people whose full time job it is to help to get you over the finish line with your code.
[5249.60 --> 5255.30]  And I hope people will contribute and do all the awesome stuff.
[5255.30 --> 5262.48]  Like, GitLab CI autoscale was contributed by someone external to GitLab.
[5262.68 --> 5266.86]  This new runner on Kubernetes, again, an external contribution.
[5267.50 --> 5269.40]  So they're making all the awesome stuff.
[5269.72 --> 5274.78]  And we'll take care of the boring stuff, the security updates, the performance updates, the packaging.
[5275.88 --> 5275.94]  Awesome.
[5276.62 --> 5277.12]  I'll say it again.
[5277.22 --> 5279.20]  Thank you so much for all you've done.
[5279.32 --> 5281.36]  I know this has been a long road for you.
[5281.36 --> 5290.54]  Everything from applied physics to submarines to now helping teams build better software through conversational development.
[5290.70 --> 5296.08]  I think it's an awesome story that you have personally, but also corporately as your company, GitLab.
[5296.20 --> 5305.18]  I think you've got a really interesting legacy and a really interesting dynasty that we hope to see blossom over these years.
[5305.28 --> 5307.66]  And anyway, we can personally support you as the changelog.
[5307.68 --> 5308.56]  We would love to do that.
[5308.56 --> 5310.74]  So it was great having you on the show today.
[5310.92 --> 5313.18]  But listeners, thank you so much for tuning in.
[5313.80 --> 5315.10]  If you have any questions for Sid.
[5315.20 --> 5319.50]  Sid, where can people reach you at if they have any particular questions directly for you or just in general?
[5319.56 --> 5320.64]  What's the best way to reach out?
[5321.30 --> 5323.50]  Probably the best way is tweeting out.
[5323.98 --> 5330.54]  And feel free to tweet out at both at GitLab and at S-Y-T-S-E-S.
[5332.00 --> 5335.32]  Twitter is mostly the faucet path.
[5335.32 --> 5337.74]  And thanks so much for having me on.
[5337.84 --> 5340.24]  I hope to be back sooner than in three years.
[5340.90 --> 5344.02]  And thanks for all the kind words.
[5344.40 --> 5346.20]  Yeah, sorry that it was actually three years.
[5346.30 --> 5349.02]  I mean, we like doing catch-up shows.
[5349.02 --> 5353.12]  And this is definitely a long overdue catch-up show.
[5353.72 --> 5361.38]  And your unveiling of your master plan yesterday and our email to you last week to kind of coordinate this was just like, this is perfect timing.
[5361.48 --> 5363.16]  Like, we wanted to have you back on the show anyways.
[5363.92 --> 5369.36]  And what better time than when you're sharing such an interesting perspective towards the future of where you're going.
[5369.48 --> 5373.96]  So we definitely thank you for coming on the show so quickly, too, and working with us on that.
[5373.96 --> 5375.66]  I agree.
[5375.92 --> 5376.48]  Good timing.
[5376.60 --> 5377.18]  Good questions.
[5377.50 --> 5378.42]  Yes, that is it.
[5378.50 --> 5380.30]  So one more mention for the listeners.
[5380.46 --> 5382.48]  You might know this already because we say this quite a bit.
[5382.54 --> 5383.36]  But we have two emails.
[5383.48 --> 5384.50]  One we mentioned was Nightly.
[5385.00 --> 5387.28]  And then the other one is our weekly email.
[5387.42 --> 5391.48]  So go to changelog.com slash weekly or changelog.com slash nightly.
[5391.96 --> 5396.40]  Pending some work with Sid here, we might actually get some GitLab projects in there.
[5396.40 --> 5404.06]  So if you have some open source on GitLab that is trending, then we might be including it in changelog nightly sometime in the near future.
[5404.18 --> 5405.82]  But that is it for this show, fellas.
[5405.94 --> 5406.88]  So let's say goodbye.
[5407.50 --> 5407.76]  Goodbye.
[5407.86 --> 5408.26]  Thanks, Sid.
[5408.78 --> 5409.16]  Goodbye.
[5409.28 --> 5409.74]  Thanks, guys.
[5409.74 --> 5409.80]  Bye.
[5409.80 --> 5409.84]  Bye.
[5409.84 --> 5409.90]  Bye.
[5409.90 --> 5409.96]  Bye.
[5409.96 --> 5410.90]  Bye.
[5410.90 --> 5411.90]  Bye.
[5411.90 --> 5412.90]  Bye.
[5412.90 --> 5413.90]  Bye.
[5413.90 --> 5413.96]  Bye.
[5413.96 --> 5414.90]  Bye.
[5414.90 --> 5415.90]  Bye.
[5415.90 --> 5415.96]  Bye.
[5415.96 --> 5416.90]  Bye.
[5416.90 --> 5417.90]  Bye.
[5417.90 --> 5418.90]  Bye.
[5418.90 --> 5419.90]  Bye.
[5419.90 --> 5420.90]  Bye.
[5420.90 --> 5421.90]  Bye.
[5421.90 --> 5422.90]  Bye.
[5422.90 --> 5423.90]  Bye.
[5423.90 --> 5424.40]  Bye.
[5424.40 --> 5424.90]  Bye.
[5424.90 --> 5425.40]  Bye.
[5425.40 --> 5425.90]  Bye.
[5425.90 --> 5426.38]  Bye.
[5426.40 --> 5427.40]  Bye.
