[0.00 --> 17.80]  Welcome to the ChangeLog episode 0.4.9.
[17.98 --> 18.92]  I'm Adam Stachowiak.
[19.14 --> 20.12]  And I'm Wynne Nutherland.
[20.34 --> 21.26]  This is the ChangeLog.
[21.32 --> 22.92]  We cover what's fresh and new in open source.
[23.36 --> 26.24]  If you found us on iTunes, we're also on the web at thechangelog.com.
[26.36 --> 27.32]  We're also up on GitHub.
[27.32 --> 29.40]  Head to github.com slash explore.
[29.50 --> 33.92]  You'll find some trending repos, some feature repos from our blog, as well as the audio podcasts.
[34.66 --> 38.34]  And if you're on Twitter, follow ChangeLog Show, ChangeLog Jobs, and me, Adam Stach.
[38.84 --> 41.22]  And I'm Penguin, P-E-N-G-W-I-N-N.
[41.72 --> 43.70]  This episode is sponsored by GitHub Jobs.
[43.76 --> 46.42]  Head to thechangelog.com slash jobs to get started.
[46.96 --> 52.92]  If you'd like us to feature your job on this show, select Advertise on the ChangeLog when posting your job, and we will take care of the rest.
[52.92 --> 58.00]  First up this week, a great organization, Recruit Military is looking for a Rails 3 dev.
[58.54 --> 65.74]  Familiar with RSpec 2, Cucumber, Sunspot Solar, Rescue, Chef, jQuery, Backbone.js, a number of technologies here.
[66.16 --> 71.12]  Such a great organization that helps find jobs for servicemen and women returning from overseas service.
[71.48 --> 74.74]  If you're interested, lg.gd slash 7Yankee.
[74.74 --> 82.30]  If you're a Houston-based Ruby and Rails developer, the fresh revolutionary marketing agency, Media 3 Creative, is looking to talk with you.
[82.98 --> 84.82]  Actually, it's me who's wanting to talk with you.
[85.28 --> 91.32]  I joined Media 3 Creative a few weeks back, and I'm currently building an awesome dev team to work with.
[91.42 --> 97.44]  So check out lg.gd slash 8v or email me at careers at media3creative.com.
[97.44 --> 110.88]  And if you live to code where the user meets the app on the front side and you're open source friendly, like implementing interfaces in iOS, Android, web, and more, be sure and look up Austin-based, the front side, but you can work anywhere, I understand.
[111.26 --> 114.12]  Short code lg.gd slash 8uniform.
[114.80 --> 115.46]  Fun show this week.
[115.50 --> 121.88]  We talked to Scott Chacon over at GitHub about Git and Showoff and even a little Xbox Connect.
[122.62 --> 123.40]  It's quite the range, huh?
[123.94 --> 124.88]  It is quite the range.
[124.88 --> 127.36]  What was the perspective in terms of what we talked about?
[128.20 --> 128.96]  As far as Git?
[129.44 --> 132.30]  Yeah, like, was it a lot of Git?
[132.40 --> 133.24]  Was it a little bit of Git?
[133.74 --> 142.78]  It was probably 90% Git and not so much GitHub this time, which is a good mix to talk about how Git compares to Mercurial and some other distributed source control systems
[142.78 --> 151.74]  and how Scott kind of sells it to other communities that aren't as entrenched in Git as perhaps the Ruby community is and kind of the heritage that you and I come from.
[151.74 --> 160.24]  And how he sells enterprises on the need to get off tools like Subversion and into a truly distributed source control system.
[161.04 --> 165.34]  He's been a really good guy in terms of promoting Git over the past few years.
[165.34 --> 166.22]  Absolutely.
[166.40 --> 170.12]  I think he's taught a lot of us what we know about the tool.
[170.60 --> 179.90]  Also talked about his Showoff presentation app that looks to be a, he hopes to be a keynote killer where you write your presentations and web technologies.
[180.58 --> 192.44]  And then also one of his hobby projects, ConnectiB, which is Ruby bindings for lib-free Connect that allows you to control the Xbox Connect on your Xbox 360 console from Ruby.
[192.44 --> 193.30]  Really, really cool.
[193.92 --> 198.68]  A quick word on Red Dirt RubyConf taking place in Oklahoma City on April 21st and 22nd.
[198.72 --> 202.18]  We'll be doing a live episode of the Change Log at the end of day one.
[202.82 --> 204.04]  And Wynn's going to talk about day two.
[204.42 --> 207.44]  Day two is action-packed full of training for some experts.
[207.98 --> 212.14]  Ryan Smith from Heroku and Wesley Berry from the Fog Gym will be doing some cloud training.
[212.82 --> 215.20]  Don't miss Optiva doing some JRuby training.
[215.20 --> 222.78]  As well as I will be participating in some Titanium mobile training with the guys at AppCelerator, Marshall and Kevin over there.
[222.82 --> 226.30]  But probably the most important part, catch our bud Eric Michaels over.
[227.00 --> 232.14]  And also Nick Coranto from Gym Cutter doing some open source training.
[232.26 --> 235.22]  So there's a whole track on how to contribute to open source.
[235.22 --> 241.36]  So be sure and catch Red Dirt RubyConf coming up in April in Oklahoma City, April 21st and 22nd.
[241.58 --> 243.58]  And registration is open right now.
[243.70 --> 246.36]  So head to reddirtrubyconf.com.
[247.04 --> 247.66]  It was a fun episode.
[247.76 --> 248.30]  Should we get to it?
[248.74 --> 249.36]  Let's do it.
[258.68 --> 260.46]  Chatting today with Scott Chacon from GitHub.
[260.46 --> 263.54]  So Scott, I think a lot of the listeners probably know who you are.
[263.60 --> 266.20]  But for those that don't, why don't you introduce yourself and your role at GitHub?
[267.04 --> 267.56]  Yeah, yeah.
[267.62 --> 268.42]  My name is Scott Chacon.
[269.08 --> 272.14]  I've been working for GitHub since almost the beginning.
[272.30 --> 277.96]  I started contracting with them when it was still sort of a side project for Tom and Chris and PJ.
[279.18 --> 283.90]  And then we all sort of quit our jobs at the same time and started working full-time about two and a half years ago.
[283.90 --> 287.28]  So, yeah, so I've been working at GitHub for a while.
[287.28 --> 291.74]  And I do a lot of Git documentation stuff.
[291.80 --> 292.64]  I'm not very good at C.
[292.84 --> 298.62]  So to contribute to the Git project, it tends to be more writing and teaching and that sort of thing.
[298.70 --> 304.78]  So I do a lot of training for GitHub and doing a lot of conference talks.
[304.98 --> 314.98]  And I wrote a book called ProGit that was published by A-Press under a Creative Commons license that you can get online and peep code PDF, that sort of thing.
[314.98 --> 322.56]  So I like Git a lot, sort of weird things you can do with it and teaching it and getting people interested in it.
[322.80 --> 324.30]  So that's me.
[324.86 --> 326.86]  So how did you come to discover Git?
[327.90 --> 334.66]  So at my previous job, I worked at a company called Reactrix, which has gone out of business.
[334.92 --> 337.60]  But, well, it went out of business a week after I left.
[337.60 --> 343.76]  So I like to think that I, you know, a business cannot sustain itself without me on its payroll.
[343.90 --> 345.64]  So I sort of took it down.
[346.20 --> 354.36]  But when I left or when I started there, we were using, we were trying to do content distribution for things for these devices.
[355.40 --> 362.32]  And so we were using, we would just create a RPM of the software and we'd, you know, SCP it over.
[362.32 --> 367.00]  And that was very, if we change one file, we'd have to create a whole new thing.
[367.14 --> 368.56]  And so there was no incremental transfer.
[368.74 --> 372.18]  It was very, it was very difficult to do.
[372.40 --> 375.12]  It wasted a lot of time and bandwidth and stuff like that.
[375.18 --> 378.16]  So what we wanted to do was something like rsync.
[379.16 --> 383.24]  And we found out that Git was actually a really good sort of rsync for what we were trying to do.
[383.24 --> 392.50]  So we would put everything in Git and we would create these custom trees of just the content that was needed out of the system and then have the client fetch it.
[392.64 --> 398.94]  And we didn't actually have to have, even though we had hundreds of clients that all had to have different combinations of that content,
[399.32 --> 405.20]  we didn't have to have, you know, hundreds of subdirectories with just the content that each one needed so we could RCP just what it needed.
[405.20 --> 413.94]  What we would do is we'd do it artificially in Git using sort of the index and just say, okay, just these five directories and not everything else and commit it.
[414.04 --> 419.38]  And it would never actually exist on disk, but we could have the client fetch it and it would come over and then be on disk on the client.
[419.52 --> 421.66]  So it was awesome.
[421.78 --> 427.48]  It actually worked really well as sort of this strange rsync sort of replacement.
[427.48 --> 429.66]  So that's how I started using it.
[429.72 --> 438.26]  So everything that I started using was we were actually using Perforce as the RCS, you know, type thing at the time for the software.
[438.48 --> 440.40]  And we were just using Git to do this rsync stuff.
[440.70 --> 443.34]  So I was sort of fascinated with the system.
[443.56 --> 451.06]  And as it became used more, you know, I found that I knew a lot of the sort of underlying, you know, plumbing stuff.
[451.20 --> 452.32]  And not very many people did.
[452.38 --> 453.50]  And I really enjoyed it.
[453.52 --> 454.46]  I thought it was a really cool model.
[454.46 --> 460.30]  So I wrote the Pupacode PDF first, and that's sort of how I got into, you know, being the Git guy.
[460.58 --> 466.54]  I also went to meetups here in San Francisco, which is how I met the other guys, is how I met Tom and Chris and PJ.
[467.60 --> 477.24]  And basically every week that I would come, I'd demonstrate some other language that I'd partially implemented Git in because, you know, it doesn't have a linkable library.
[477.48 --> 479.40]  It does now, but it didn't at the time.
[479.40 --> 486.58]  And so I would be like, hey, look, I've re-implemented the blob writing and reading mechanism of Git in ActionScript.
[486.72 --> 489.20]  And people are like, why would you do that?
[489.24 --> 490.68]  That makes basically no sense.
[491.38 --> 493.12]  And so it was basically every single week.
[493.16 --> 493.90]  It's like I did it in Ruby.
[494.00 --> 494.74]  I did it in ActionScript.
[494.86 --> 497.00]  I did it in, you know, some other language.
[497.46 --> 499.74]  And Erlang, you know, whatever.
[499.74 --> 508.78]  And so people were – I think that's sort of how I got the reputation as the Git guy was just I was obsessed with it at all times and still kind of am, actually.
[509.46 --> 518.56]  So as someone that's recently went back to the corporate scene, a lot of times I'm having to sell folks on why they should throw away subversion and move to distributed source control.
[518.68 --> 525.74]  So as the guy that wrote the book on Git literally, what do you tell people when they are considering a distributed system?
[525.74 --> 529.28]  Well, you know, I tell them that it's faster.
[530.28 --> 532.40]  I tell them that their developers can work better.
[532.46 --> 533.88]  I mean, it depends on who you're asking, right?
[533.90 --> 538.60]  If you're asking a developer, if you're asking somebody that's, you know, making the purchasing decisions or something.
[538.82 --> 542.26]  But, you know, having more efficiency for your developers.
[542.38 --> 543.20]  They can work offline.
[543.30 --> 544.16]  They can work off VPN.
[544.96 --> 546.40]  All of the commands are faster.
[547.00 --> 553.82]  Branching and merging is easy to do, and it's a very common operation, which is not common in basically almost any other version control system,
[553.82 --> 556.08]  especially ones that people are switching from.
[556.68 --> 562.80]  But the offline stuff, I've been to places where, you know, they have ClearCase or they have Perforce or Subversion or something,
[562.90 --> 569.78]  and their system goes, especially like ClearCase, their system, their main server goes down or their network is, you know, goes down for a little while.
[569.82 --> 572.30]  And basically everybody has to stop working completely, right?
[572.30 --> 577.48]  And it's not as bad in Subversion where you can at least keep coding, even though you can't commit and stuff.
[577.70 --> 583.62]  But almost everybody's been bitten by that, you know, or they lose the database and they have to recover it or something.
[583.82 --> 586.28]  And you tell them you can do everything offline in Git.
[586.46 --> 589.46]  Everybody that's working on the project has a full backup of the system.
[589.72 --> 591.12]  There's no single point of failure.
[591.60 --> 595.72]  It's easy to, you know, if the server goes down to put up another one, everybody can keep working off that.
[596.40 --> 597.14]  Branching and merging.
[597.74 --> 603.24]  One of the big ones that I see people light up when I explain it to them is the continuous reintegration.
[603.76 --> 607.98]  You can continuously reintegrate branches in Git, and that's very difficult to do in most other systems,
[607.98 --> 614.78]  especially Subversion, even with, like, the merge tickets that they have recently, is you can create a branch, like, for, you know,
[614.84 --> 619.72]  changing your database backend or adding translations to your system or something that takes a long time.
[620.02 --> 625.48]  And generally would be this merge hell that everybody would have to go through.
[625.62 --> 630.68]  And you can just be on that branch and continuously reintegrate the master branch into it very easily.
[630.68 --> 636.60]  And at the very end, just switch back and do a fast-forward merge from master to whatever the branch is and get all of that stuff.
[636.76 --> 643.00]  And if you're merging every day, you only get, you know, 24 hours worth of merge conflicts at a time and not, you know, this huge.
[643.08 --> 644.62]  There are 50 files that have conflicted.
[644.72 --> 647.06]  It's, you know, if you're good about it, it's impossible to do that.
[647.20 --> 653.18]  So when I demonstrate that sort of stuff, you know, that's when people really embrace it.
[653.18 --> 663.42]  And I think that's how most of us got really interested in the Ruby community about it, which sort of embraced it early and fast, is we would do demos, you know, in the conference, you know,
[663.44 --> 669.98]  in sort of the side rooms of the conferences saying, look how cool this is to create branches and switch back and forth between them real fast and merge them back and forth.
[670.04 --> 678.50]  And it was so ridiculously easy when you're actually watching that that you can't not see how that would, you know, be good for your team and good for your development practices.
[678.50 --> 696.06]  So as you've been going through this training with all these corporate clients and everything, have you found it really difficult to sell the concept of Git for the people who are really fond of having a really federated system where, you know, no one can touch their code unless they're authenticated via, you know, their exchange server and systems like that?
[696.74 --> 698.50]  Well, not really.
[698.66 --> 703.68]  I mean, and that could just be because of the clients that I'm doing, right?
[703.68 --> 708.76]  We're not, GitHub is not sort of selling into corporations and saying you should be using this thing.
[708.88 --> 710.84]  You know, we don't have like salespeople that go out and do stuff.
[710.92 --> 713.60]  It's very, it's always generated from within.
[713.76 --> 719.84]  It's from developers that are using Git for open source projects on GitHub or something, and then they want to use GitHub internally.
[720.44 --> 729.06]  And so they look for, you know, GitHub Enterprise, like our firewall install client, where you can buy it and run it inside your firewall.
[729.06 --> 732.70]  And so they come to us for that because they, you know, they want to do that.
[732.76 --> 735.72]  And then they say, you know, as long as you're doing that, you want to come and do some training as well.
[735.78 --> 737.96]  And so we'll either throw that in with that.
[738.08 --> 740.02]  So they've already embraced it in some way.
[740.06 --> 744.70]  Or the other one that I do a lot is large corporations that do sort of Android development.
[745.18 --> 747.82]  So like big telecom type companies.
[747.98 --> 751.54]  And so they want to be involved in the Android ecosystem and it's using Git.
[751.62 --> 753.64]  So, you know, they sort of have to use Git.
[753.64 --> 760.26]  It's very rare that, you know, we won't really like go in and, you know, schedule a meeting and go in and sell people on the merits of Git.
[760.36 --> 763.86]  It's more of a developers love it and they use it on their off time.
[763.86 --> 767.86]  And then they try and get it into their company because there's a need for it, right?
[769.02 --> 773.12]  It's painful to use another version control system if you're using Git in your spare time.
[774.10 --> 774.38]  That's true.
[774.50 --> 783.56]  You know, one of the ideas that I had last week was, you know, these adopted highway sections of a highway where they have a local group that goes out and just picks up trash on the highway.
[783.64 --> 783.84]  Or whatever.
[784.20 --> 790.10]  I think we should all go out to Google Code and some of these other places and just adopt a repo that's in Subversion and just pull it over to GitHub and mirror it.
[790.78 --> 790.86]  Yeah.
[790.94 --> 794.24]  I mean, we've tried to make it kind of easy to do Subversion imports.
[794.40 --> 803.04]  But the problem with Subversion importing is that, you know, changing from any version control system to another is that it depends on the history of the system, right?
[803.38 --> 804.72]  Like really simple ones aren't that difficult.
[804.72 --> 814.54]  But I've been to a bunch of companies that, you know, have these really complex histories where they even moved from CVS to Subversion and then they've been in Subversion for years and they have hundreds of thousands of commits.
[814.72 --> 820.40]  And, you know, they don't know how they want to split it up or, you know, they've added a large file and then removed it again.
[820.40 --> 824.12]  And so that import, you know, adds the big file into your clone and stuff.
[824.30 --> 827.16]  And so a lot of times that has to be sort of custom.
[827.24 --> 834.54]  I've seen people write custom, you know, importers with like Git fast import, which is, you know, an incredibly time-consuming process.
[834.54 --> 840.64]  And then I've seen other companies where they just take the last snapshot and put it into Git and they're like, screw everything else, let's just go.
[841.38 --> 846.02]  So it's so highly dependent on the team around whatever the project is, you know.
[846.66 --> 852.74]  Yeah, whenever I have to do that, I usually just do get us the end clone and if it's a big tree, it'll take hours and hours and hours.
[852.82 --> 853.18]  It's terrible.
[855.16 --> 857.90]  So how pimped out is your Git config file?
[859.58 --> 860.18]  It's not.
[860.18 --> 861.10]  It's actually not.
[861.10 --> 877.24]  Largely because I do so much training and evangelization and stuff is I don't want to be – I don't want to have a very custom setup locally where I'm typing commands that they can't type or something, you know, if I'm trying to demo something.
[877.74 --> 880.22]  So I've been – for a long time I had no Git aliases.
[881.16 --> 882.94]  I'd have to type out everything all the time.
[883.14 --> 885.12]  And I had no Bash aliases.
[885.12 --> 890.86]  So, you know, it wouldn't actually just – most of the people at GitHub can type like, you know, GCI or something.
[890.86 --> 893.58]  And it does a Git commit with options and things.
[893.70 --> 900.74]  But I try and stay away from that so that I can just use – you know, I have sort of the experience – this sort of new user experience still and I can teach that.
[900.84 --> 902.64]  You know, I remember what all the commands are.
[903.14 --> 908.10]  I have weakened in my resolve recently or, you know, within the last year or so.
[908.18 --> 912.72]  I added a Git LOL which does a Git log graph decorate one line.
[912.72 --> 918.76]  And then, you know, so it gives me a nice sort of visual graph so I don't have to use Git K.
[920.36 --> 928.02]  And Git ST which is – I use for Git status dash S dash B which gives you a short status in the newer versions of Git.
[928.16 --> 933.70]  Sort of like the subversion looking output where it's just like question marks next to each name that's, you know, untracked and things like that.
[934.14 --> 937.10]  And that's a lot nicer looking than the sort of verbose Git status output.
[937.10 --> 938.54]  So those are my two cheats.
[938.68 --> 943.68]  But other than that – and I think I put a custom font in for Git GUI and Git K.
[944.24 --> 948.20]  But other than that, I don't really have very much in there because I don't want to cheat.
[948.76 --> 953.54]  So do you use any – a lot of external tools with Git like TIG or Git X at all?
[953.54 --> 956.34]  No, I don't.
[956.48 --> 961.86]  I use Git GUI every once in a while which is sort of the committing interface for Git on a GUI.
[962.04 --> 971.22]  If I have, you know, a whole bunch of stuff that I've done and I want to break it up into three or four commits and be really specific about it because you can do line level commits.
[972.34 --> 974.48]  Sort of patch, you know, like Git add dash P.
[974.60 --> 979.74]  You can do that but you can do it like on a line by line basis which is a little bit nicer.
[979.84 --> 981.28]  So you can sort of go through that real fast.
[981.28 --> 985.96]  A couple of guys at GitHub use Git X to do the same thing which has a really nice interface for that as well.
[986.78 --> 992.72]  But again, I try and use whatever comes with Git when I can so that I can teach it a little bit more broadly.
[994.08 --> 996.02]  So why Git and not Mercurial?
[997.34 --> 998.64]  Why Git and not Mercurial?
[999.10 --> 1002.12]  So I have done a little bit of work in Mercurial.
[1002.12 --> 1014.02]  I did a plug-in for Mercurial called hggit which allows you to, or I started it, which allows you to commit in Mercurial and then push to a Git server.
[1014.16 --> 1018.72]  So you can use Mercurial and then push to GitHub, for example, to put the code on.
[1019.50 --> 1024.22]  And then people don't, you know, necessarily, it uses Git as the transport port mechanism.
[1024.22 --> 1030.84]  So GitHub doesn't know that you're using Mercurial client for it and it's a one-to-one conversion ratio.
[1031.18 --> 1039.58]  So every object in Git has sort of a, or every commit in Git basically has a one-to-one relationship with a commit in Mercurial.
[1039.86 --> 1040.58]  And they're very similar.
[1040.78 --> 1044.70]  So when I was writing that, I had to learn sort of the back-end systems.
[1044.76 --> 1045.96]  How does it store its data?
[1046.52 --> 1048.56]  What does the actual sort of format look like?
[1048.98 --> 1051.20]  How does it think about the data that you're putting into it?
[1051.20 --> 1052.98]  And it turns out that it's actually incredibly similar.
[1053.48 --> 1057.54]  The main difference is how it actually stores it on disk.
[1057.64 --> 1058.86]  It's not the objects themselves.
[1058.94 --> 1062.86]  The objects themselves are actually incredibly similar and it's not that difficult to go back and forth between them.
[1063.30 --> 1067.40]  Which is why, you know, branching and merging is just about as easy in Mercurial.
[1068.06 --> 1069.56]  You know, a lot of stuff are the same.
[1069.68 --> 1074.32]  So what I like to do is say, you know, use whatever client you feel more comfortable with.
[1074.36 --> 1077.18]  I feel more comfortable with Git because I like the branching model better.
[1077.18 --> 1081.44]  But recently Mercurial has bookmarks, which are very similar to the Git branching model.
[1081.52 --> 1084.00]  So if you want to use bookmarks, then you get sort of the same thing.
[1084.46 --> 1087.04]  But other than that, they're incredibly similar systems.
[1087.58 --> 1094.02]  And so, you know, the HG Git plugin is a nice thing because then we can say, use whatever client you want.
[1094.16 --> 1094.72]  Use Mercurial.
[1094.80 --> 1095.22]  Use Git.
[1095.68 --> 1096.18]  Push to GitHub.
[1096.32 --> 1097.28]  Everybody can work together.
[1097.46 --> 1102.10]  And nobody really needs to know that other people are using, you know, whatever client they're most comfortable with.
[1102.10 --> 1109.80]  But, yeah, I mean, I used Git because the backend system originally, like I was saying, I was using it in a more low-level way.
[1110.04 --> 1111.88]  And the backend system gives you a lot more power in Git.
[1111.96 --> 1113.48]  It's a lot simpler.
[1114.24 --> 1115.98]  The Mercurial one is much more complex.
[1116.16 --> 1119.36]  It's sort of a hybrid between the Subversion model and the Git model.
[1119.68 --> 1121.82]  Where the Git model is just, here's all these objects in a database.
[1122.00 --> 1122.96]  It's sort of a key value store.
[1123.02 --> 1123.38]  I don't care.
[1123.94 --> 1129.46]  And, you know, Subversion has this file-based log system where you have versions of each file in a name of that file.
[1129.46 --> 1131.54]  Or a file named after that file name.
[1131.78 --> 1133.38]  And in Mercurial, it's sort of like that.
[1133.50 --> 1136.82]  Like you have, for every file you've ever had in your system, you have this file.i.
[1137.08 --> 1139.24]  It has a log of every version of that file.
[1139.38 --> 1143.20]  And so it's a lot more, like if you rename a file or remove a file, you still have to have that log there.
[1143.24 --> 1144.96]  And you have to have rename links and all this stuff.
[1145.06 --> 1146.30]  And it's much more complex.
[1146.84 --> 1148.34]  And it gets super simple.
[1148.46 --> 1150.68]  It's just, you know, here's a manifest and a commit.
[1150.86 --> 1152.04]  And here's all the objects.
[1152.18 --> 1153.28]  And we don't really care.
[1153.48 --> 1154.72]  You know, we don't track renames.
[1154.84 --> 1156.54]  We figure it out after the fact.
[1156.54 --> 1160.52]  So that worked for what I was trying to do with the low-level stuff.
[1160.74 --> 1163.02]  And Mercurial, it's basically just a version control system.
[1163.10 --> 1169.60]  Whereas Git, you can use the back end for basically anything that you can think about using for a version POSIX file system.
[1169.68 --> 1171.46]  Because that's basically all that it is.
[1171.82 --> 1174.54]  I really wish that there was a Git HG plugin personally.
[1174.68 --> 1182.42]  Because I have, being involved in the Python community, every once in a while, I find someone real stubborn who's working on Bitbucket.
[1182.42 --> 1183.66]  And I have to push up to it.
[1183.68 --> 1184.50]  And it's very frustrating.
[1185.28 --> 1193.46]  But I actually just watched a talk by you recently where I didn't realize that when you're using HGGit, it actually has a full Git repo inside of it.
[1193.52 --> 1197.40]  And they can just clone off of the bear repo in there and then work with that.
[1197.82 --> 1198.14]  Yeah, yeah.
[1198.26 --> 1201.12]  There are a couple people that are using HGGit to do the opposite.
[1201.12 --> 1212.12]  So HGGit, Augie Fackler and a couple other people have sort of taken that over and made it a lot better than it originally was when I was working on it.
[1212.18 --> 1214.02]  I kind of haven't been working on it for a while.
[1214.10 --> 1214.54]  But it's great.
[1214.62 --> 1215.56]  And a lot of people use it now.
[1216.38 --> 1217.92]  And he made it really, really fast.
[1218.24 --> 1219.70]  A lot faster than it was when I was doing it.
[1219.70 --> 1234.76]  But, yeah, so a lot of people will use it where they'll use it sort of the opposite, where they'll use it to take their Git stuff and put it into Mercurial and push it just via the normal Mercurial thing.
[1234.82 --> 1237.60]  Because it does bidirectional conversions.
[1237.84 --> 1241.06]  I have to, when you clone from Git, I have to turn them all into Mercurial object.
[1241.20 --> 1243.54]  And when you commit in Mercurial, I have to turn them into Git objects.
[1243.64 --> 1244.82]  So it can do both ways.
[1244.82 --> 1247.86]  And it's not that difficult to set it up the other way.
[1247.96 --> 1249.82]  But it's not built in.
[1249.90 --> 1253.14]  It's not super easy like it is with the Mercurial side of it, right?
[1253.74 --> 1255.62]  Sounds like a good contributor could add that, right?
[1257.02 --> 1257.34]  Yeah.
[1257.92 --> 1258.72]  I would look at it.
[1258.72 --> 1259.22]  I don't remember.
[1259.66 --> 1266.82]  There's, I think, a couple of people have added some things to it to make it relatively easy to do that sort of thing.
[1266.88 --> 1269.06]  But it certainly doesn't ship with Git, right?
[1269.92 --> 1272.32]  So we cover quite a broad range of listeners.
[1272.32 --> 1275.18]  Do you want to go over some of the basic differences?
[1276.06 --> 1277.46]  I've heard you talk of this before.
[1278.16 --> 1284.52]  Of why Git is being used by who it's being used by and Mercurial at the same time.
[1284.70 --> 1287.34]  Not that one is superior to the other in any way.
[1287.44 --> 1288.36]  That they're actually quite similar.
[1288.58 --> 1290.88]  And then why one's becoming more popular than the other.
[1291.58 --> 1296.04]  I guess one of the, I kind of consider it a mistake at this point.
[1296.28 --> 1298.16]  But I'm too lazy to go back and redo it.
[1298.38 --> 1300.80]  I made a website called whygitisbetterthanx.com.
[1300.80 --> 1306.78]  And I put a bunch of other version control systems and basically just summarized for people that are saying, why are you using Git?
[1307.00 --> 1309.54]  Especially, you know, a couple years ago, people were like, why are you using Git?
[1309.90 --> 1310.94]  And so I wanted to summarize.
[1311.06 --> 1312.58]  This is why we chose Git.
[1312.68 --> 1314.00]  This is why people that use Git chose Git.
[1314.54 --> 1319.56]  But the problem that I did was I put a lot of different version control systems on there.
[1319.56 --> 1324.82]  I had it comparing to Mercurial and to Bizarre, which are other distributed version control systems.
[1324.82 --> 1331.86]  And since then, you know, all the email I've gotten back is not defending Subversion or Perforce or the other ones that I compared it to.
[1331.94 --> 1335.50]  They're all defending Mercurial and sometimes Bizarre.
[1335.50 --> 1342.64]  And so I've sort of changed my message to be, you know, we don't care what you use.
[1342.72 --> 1355.10]  Everybody should be using distributed version control because there's still a huge, huge, you know, population, especially in the corporate world, that's using Subversion or centralized version control systems for stuff.
[1355.10 --> 1364.82]  And I think in most of those cases, it would do, you know, it would be better for the entire development team there if they were using a distributed version control system.
[1364.86 --> 1370.02]  And the reason why largely, besides just offline work and stuff like that, is branching emerging.
[1370.18 --> 1381.48]  Like if people are using CVS or Subversion or, you know, any of the sort of RCS derivatives, any of the centralized version control systems, I guess I should say,
[1381.48 --> 1385.58]  they have a different mentality of how to develop, right?
[1385.92 --> 1397.76]  And if you're using a distributed version control system because you can sort of craft your commits, you can think about it a little bit more, you can do stuff offline, you can decide when to push and share with people, you can do branching emerging very easily.
[1398.30 --> 1399.40]  And it's very lightweight.
[1399.70 --> 1405.76]  It's something where you say, I'm going to make a branch for every ticket that I'm working on or something.
[1406.12 --> 1410.64]  Somebody in a centralized version control system, like if you're doing Subversion, that would make no sense, basically.
[1410.64 --> 1413.90]  It would be so much overhead that it wouldn't be practical.
[1415.06 --> 1421.16]  And in Git and in Bizarre and in Mercurial, in distributed version control systems, you know, those are sort of the top three.
[1421.66 --> 1422.58]  That makes sense.
[1422.70 --> 1425.50]  And so I want everybody to be doing that.
[1425.64 --> 1432.72]  I want the mentality of the entire development community to be you branch first, you do stuff in branches, you merge it in when it's ready.
[1432.96 --> 1438.20]  And when we can get people from Subversion over to any distributed version control system, that mentality changes.
[1438.20 --> 1442.08]  And I did not have a hard time working in Mercurial, right?
[1442.12 --> 1445.94]  I mean, when I was doing it, when I was writing HGitPlug, and I did everything in Mercurial.
[1446.26 --> 1450.62]  And I thought it was fascinating, but it was not difficult to do.
[1450.72 --> 1458.08]  It was not nearly as difficult as moving from Subversion to Git or from, you know, what was I using before that?
[1458.18 --> 1458.94]  RCS, I guess.
[1459.06 --> 1463.86]  Or, you know, from Subversion to Perforce or something that's sort of really different, right?
[1463.86 --> 1477.34]  And I think once everybody's in that mentality of what they expect their version control system tool set to be and how they expect to work and the efficiencies that they expect to get out of developing and how they expect to collaborate, right?
[1477.34 --> 1483.32]  It doesn't really matter which of the three it is because that's your mentality and you just have to remap that onto something slightly different.
[1483.42 --> 1485.26]  A user interface is slightly different, right?
[1485.26 --> 1494.22]  So that's been the push is not alienating people that are Mercurial users because, you know, I actually like Mercurial to a certain degree.
[1494.36 --> 1500.50]  There's a lot of interesting development decisions that I think were made smarter than Git and a lot of ones that I think were not.
[1500.80 --> 1509.06]  And actually, I love, you know, drinking with people and talking about that for a really long time because I can do it at least to a fair depth, right?
[1509.12 --> 1510.64]  Because I've been doing both of these.
[1510.64 --> 1521.28]  I actually had a lunch one time with Augie who's the guy that has been maintaining the HD Git plugin who's a Mercurial hacker and has always been a Mercurial guy and me and another friend of ours.
[1522.16 --> 1530.06]  And the three of us basically spent the entire time drinking and eating pizza and talking about the differences in the transport protocols between Git and Mercurial.
[1530.42 --> 1538.24]  And I was like, this is a conversation that can only possibly be interesting to basically the three of us on the planet because – but, you know, I love it.
[1538.24 --> 1539.14]  I think it's really interesting.
[1539.38 --> 1545.58]  But the point is that, you know, once you get into distributed version control, I think that that is the future of development.
[1545.84 --> 1555.30]  And the sooner that we get more developers over there, I mean, the better it is for obviously GitHub if people are using – you know, even if people are using Mercurial, that's better than people using Subversion, right?
[1555.94 --> 1562.16]  They're closer to using GitHub or to being involved in an open source community that embraces that development style.
[1562.16 --> 1568.04]  And I feel like that's better for the open source community in general, right, getting off of this.
[1568.98 --> 1570.04]  I mean, that's the other thing.
[1570.12 --> 1570.26]  Sorry.
[1570.44 --> 1573.70]  I'm sort of ricocheting here.
[1573.92 --> 1579.10]  But that's the other interesting thing is that, you know, I mean, our interests are more than just GitHub.
[1579.28 --> 1581.64]  Our interests are the entire open source community.
[1581.76 --> 1586.88]  We want the open source community to be vibrant and to be interesting because that's who we all are.
[1586.96 --> 1590.34]  That's who basically everybody at GitHub came from, right, and how we met each other.
[1590.34 --> 1593.02]  And so we want the open source community to thrive.
[1593.54 --> 1600.38]  And I feel like distributed version control systems, it's much easier to thrive as an open source community using that.
[1600.44 --> 1603.84]  When you're on Subversion, everybody has this sort of read-only thing.
[1604.22 --> 1606.44]  And you can read it, and you can improve it locally.
[1606.96 --> 1612.52]  And if you want to go through everything, you can, you know, extract a patch and mail it to a thing and go through that whole thing.
[1612.66 --> 1614.46]  And it's really heavy weight.
[1614.46 --> 1617.52]  And then if you do that enough times, maybe they'll give you a commit bit.
[1617.66 --> 1620.68]  And then, you know, you can actually push stuff into the repository.
[1620.86 --> 1622.44]  You can actually commit something to the repository.
[1622.60 --> 1623.88]  And everything's so heavy, right?
[1623.90 --> 1625.34]  It's so difficult to get involved.
[1625.94 --> 1631.02]  And in Git, I feel like, or even in Mercurial, but in any of these distributed version control systems,
[1631.02 --> 1638.36]  because you can have these, you know, these sites like GitHub where you can create a fork and have your own write permissions
[1638.36 --> 1645.04]  and share stuff without having to get the sort of blessing of the entire community and craft stuff that's nice and send it back.
[1645.10 --> 1646.34]  And everything's very easy, right?
[1646.38 --> 1651.66]  I mean, that whole process is so much easier, and you have so much more power in it doing that.
[1651.70 --> 1653.72]  And if you don't get it back in, you can still keep it up there, right?
[1653.78 --> 1656.18]  You don't, it's just, it's easier for everybody.
[1656.18 --> 1661.62]  So that's, I feel, a little bit less true in Mercurial than in Git.
[1661.80 --> 1666.78]  I think that it's easier to do forks and stuff in GitHub than trying to do like patch queues or something in Mercurial.
[1666.98 --> 1670.98]  But it's certainly easier than in Subversion, right?
[1671.04 --> 1675.46]  So that's the other push, is we want the open source community to be on one of them,
[1675.58 --> 1680.08]  so that it's easier for us to collaborate, and open source grows faster.
[1680.66 --> 1680.98]  Absolutely.
[1680.98 --> 1685.48]  I think the big thing that GitHub did when they decided to build the system that you guys have
[1685.48 --> 1690.60]  is to take the projects and make the name, the namespace that everyone shares,
[1690.80 --> 1693.56]  your username rather than the project itself.
[1693.66 --> 1697.88]  So there's no GitHub slash, you know, whatever the project name is.
[1697.94 --> 1700.00]  It's username slash project name.
[1700.08 --> 1702.56]  And that's what really enables people to be able to, you know,
[1702.66 --> 1706.36]  it turns it from being a technological problem to a social problem, correct?
[1706.70 --> 1709.76]  And the other nice thing about that is that you don't have squatters, right?
[1709.76 --> 1711.50]  Because you have your own namespace.
[1711.66 --> 1716.88]  You don't need to, you know, try and squat a name that you want like you do on,
[1716.96 --> 1722.58]  even like in the Ruby community, the way that you get gems out is with Gemcutter, right?
[1723.10 --> 1724.76]  And how you used to do it was Rubyforge.
[1725.62 --> 1728.42]  And so if you want a gem name, if you want a project name,
[1728.46 --> 1731.18]  you have to sort of squat it while you're working on it,
[1731.18 --> 1733.94]  unless you sort of work on it in private and put it up there
[1733.94 --> 1736.06]  or put up something that isn't really quite ready yet or something.
[1736.06 --> 1739.74]  But there's still a little bit of squatting, but it wasn't as bad as like SourceForge or something
[1739.74 --> 1744.62]  where, you know, half of the projects are dead because just because they thought of a cool name,
[1745.00 --> 1746.92]  they're like, you know, they're like, backscatter.
[1747.00 --> 1747.76]  That sounds amazing.
[1747.86 --> 1748.52]  Let's do a thing.
[1748.58 --> 1749.42]  And then you put it up there.
[1749.70 --> 1750.84]  You know, like, this is what this will be.
[1750.90 --> 1754.10]  And then like 90% of the time it never happens, right?
[1754.40 --> 1758.52]  And in GitHub, maybe you create a project name, you know,
[1758.54 --> 1759.70]  but you don't have to really squat it.
[1759.72 --> 1762.24]  You're not taking it from somebody else that could do something cool with it, right?
[1762.24 --> 1764.70]  You know, that's so true on RubyGems.
[1764.86 --> 1766.42]  It cracks me up to 404 pages.
[1766.70 --> 1768.66]  Page not found, but then it says, it will be mine.
[1768.72 --> 1769.88]  Oh, yes, it will be mine.
[1771.34 --> 1773.38]  Sounds like me and domain name purchases.
[1775.46 --> 1779.48]  Yeah, well, that's a whole other thing that gets me angry too.
[1780.88 --> 1785.16]  So the whole Git ecosystem right now, is there anything that really gets you excited,
[1785.36 --> 1788.34]  like the development of LibGit2 and other projects like that?
[1788.34 --> 1791.84]  Yeah, well, I mean, the development of LibGit2 certainly gets me excited
[1791.84 --> 1794.12]  because I'm, you know, sort of directly involved in it.
[1794.58 --> 1796.96]  But it's something that the Git community is needed for a long time,
[1797.12 --> 1798.66]  is a linkable Git library.
[1798.74 --> 1804.86]  Because, you know, the library, there is a LibGit.a that is produced by building Git itself,
[1804.90 --> 1806.34]  but it's not re-entrant.
[1806.48 --> 1810.70]  So if you link to it and it gets to a certain point and it does this all over the place,
[1810.72 --> 1812.08]  it was built as sort of a command line tool.
[1812.26 --> 1813.90]  So it'll just call die.
[1813.90 --> 1818.80]  And so your program, whatever it is, will simply die if it gets to that point.
[1819.18 --> 1820.38]  And so you can't really use it.
[1820.38 --> 1823.70]  There's no stable defined API that, you know, won't change.
[1823.88 --> 1825.68]  Everything just sort of changes all over the place.
[1826.18 --> 1827.18]  It's sort of a mess.
[1827.94 --> 1829.24]  And the tool is great.
[1829.50 --> 1831.68]  And there's a ton of really smart people working on it.
[1831.80 --> 1833.92]  But there's no linkable library.
[1834.00 --> 1836.10]  So you can't really build like a GUI on top of it,
[1836.12 --> 1837.68]  which is why they were slower to come.
[1837.68 --> 1845.38]  And so LibGit2, which is the linkable library that's re-entrant and, you know,
[1845.54 --> 1850.60]  has a stable API and all that stuff, has been in the works for years ever since.
[1850.74 --> 1853.80]  I think it sort of started when I went to one of the get-togethers every year
[1853.80 --> 1857.50]  after the Google Summer of Code conference.
[1857.72 --> 1859.18]  A lot of the Git people are around.
[1859.40 --> 1863.20]  So we do a get-together where all the Git developers get together and talk about stuff.
[1863.20 --> 1868.56]  And I was showing – I was basically showing people all of these different implementations
[1868.56 --> 1871.62]  that I was talking about that I had done of Git in all these languages,
[1871.80 --> 1872.88]  like, you know, in Ruby.
[1873.10 --> 1875.40]  And I helped with some of the Python stuff, I think.
[1875.66 --> 1879.58]  And I did one in Erlang or possibly two in Erlang.
[1879.80 --> 1881.54]  And I did one in ActionScript.
[1881.62 --> 1882.34]  And I was showing all this stuff.
[1882.40 --> 1885.20]  And I was like, this is necessary because there is no linkable library, right?
[1886.06 --> 1888.72]  Otherwise, we could be building wrappers and neefs and stuff.
[1888.72 --> 1893.36]  And so the project sort of started, but it never really went anywhere.
[1893.68 --> 1895.82]  And then last year for the Google Summer of Code,
[1896.12 --> 1900.46]  somebody put up a thing that they would be interested in working on it.
[1900.52 --> 1902.40]  And I became the mentor sort of by default.
[1902.54 --> 1904.28]  I wasn't really planning on doing it.
[1904.34 --> 1905.58]  But him and I worked together.
[1905.70 --> 1908.08]  And then he got really, really far with it.
[1908.10 --> 1909.38]  I had a great student, Vison.
[1909.58 --> 1911.32]  And he got really, really far with it.
[1911.34 --> 1912.54]  And it became really usable.
[1912.54 --> 1919.70]  And so GitHub decided to just keep paying him, basically, to keep working on it.
[1919.76 --> 1922.22]  So it's sort of the indefinite Google Summer of Code,
[1922.42 --> 1924.58]  where we took Google out and then replaced it with GitHub.
[1925.06 --> 1926.90]  And then, you know, he's still a student.
[1926.96 --> 1928.18]  And we keep paying him to work on it.
[1928.66 --> 1930.50]  And we've gotten a couple other people.
[1931.44 --> 1934.76]  Jeff King from the Git community is a really huge Git developer.
[1934.88 --> 1937.22]  He's sort of partially working on it as well.
[1937.22 --> 1943.44]  So now GitHub is sort of driving the development of this LibGit2 library,
[1943.88 --> 1947.34]  where we can use it in stuff that we, you know, on our back end and stuff,
[1947.40 --> 1949.48]  which would be really nice for us.
[1949.80 --> 1951.66]  We're doing a Ruby wrapper for it as well.
[1952.14 --> 1957.54]  And we're getting contributions like a Python wrapper and a .NET wrapper
[1957.54 --> 1959.18]  and an Objective-C wrapper and stuff.
[1959.30 --> 1961.12]  So you can use it from all these different languages,
[1961.26 --> 1964.54]  which has, you know, sort of historically been another thing that's nice about Mercurial
[1964.54 --> 1966.74]  is that you can write tools and stuff where it has this nice API.
[1966.74 --> 1967.96]  And you can sort of extend it.
[1968.40 --> 1974.16]  And now I think LibGit2 is getting, it's almost far enough along where, you know,
[1974.16 --> 1977.52]  we'll have wrappers where it's just as easy to write something in Python using Git
[1977.52 --> 1980.48]  as it is using, you know, Mercurial, even though Mercurial is written in Python.
[1981.02 --> 1985.66]  But then you could also do it in Ruby or in Shell Scripts or in Objective-C
[1985.66 --> 1987.42]  or in whatever language you like, right?
[1987.42 --> 1989.28]  I mean, we have like Lua wrappers or something for it.
[1989.34 --> 1991.80]  So that's what I really want to get to,
[1991.80 --> 1998.02]  where there's these nice APIs in almost every language on this nice, fast,
[1998.66 --> 2001.00]  stable reentrant thread-safe library.
[2001.76 --> 2005.56]  So that's one of the things I'm really interested in is not just the development
[2005.56 --> 2008.06]  because that's, you know, I'm not great at C.
[2008.20 --> 2009.56]  I can't really do the code.
[2009.70 --> 2012.40]  In fact, the way that I was doing this Google Summer Code stuff was he would,
[2012.54 --> 2015.46]  I would define what I wanted the API to look like in Ruby, basically.
[2015.84 --> 2017.08]  He would write it all in C.
[2017.08 --> 2020.08]  I would look at the .h files, write the wrappers in Ruby,
[2020.28 --> 2024.48]  and then write the unit tests in Ruby to see if the stuff that he wrote in C worked or not,
[2024.58 --> 2027.42]  which is possibly not the best way to be doing that,
[2027.66 --> 2030.22]  but it was a lot better than me actually trying to look at his C code.
[2031.22 --> 2036.82]  And that's largely kind of how we still do stuff is I make sure the rugged Ruby wrapper works for stuff
[2036.82 --> 2040.22]  and that I can build the things I want to.
[2040.32 --> 2043.84]  But then evangelizing that and saying, you know, when I go to companies
[2043.84 --> 2047.58]  or when I go to talks or something saying, here's this cool library with all these bindings,
[2047.92 --> 2051.10]  write something cool with it because the backend is incredibly flexible, right?
[2051.12 --> 2059.08]  It's basically just this key value store and this, you know, sort of linked list of snapshots,
[2059.08 --> 2061.40]  of manifests, of this file system.
[2061.80 --> 2066.76]  And you can do whatever you want that, you know, that syncs well and easily and incrementally.
[2066.88 --> 2069.94]  And so you can do anything you can think of that would use a structure like that,
[2069.98 --> 2070.78]  you can do and get.
[2070.86 --> 2072.16]  It doesn't just have to be version control.
[2072.16 --> 2076.74]  And so that's what I'm really interested in the next couple of years
[2076.74 --> 2080.72]  because we're going to have, you know, libgit2 and all these nice bindings
[2080.72 --> 2083.90]  so everybody can write all these cool scripts and stuff that do all this custom stuff.
[2084.16 --> 2088.46]  But then also eGit, you're asking about stuff I was excited about in Git.
[2088.62 --> 2091.72]  eGit is the Eclipse Git plugin.
[2091.98 --> 2096.80]  And the Eclipse project has sort of embraced Git as their next version control system,
[2097.10 --> 2098.34]  basically from CVS.
[2098.42 --> 2100.22]  They never really embraced a version that well.
[2100.22 --> 2109.16]  And so they're all working on this eGit plugin for Eclipse that does, you know, everything where you don't have to install Git.
[2109.38 --> 2110.80]  You can simply install this plugin.
[2110.92 --> 2113.96]  It has a pure Java implementation of Git in it.
[2113.96 --> 2116.40]  And you can do everything in there.
[2116.54 --> 2119.18]  NetBeans has a great plugin now as well for their editor.
[2119.40 --> 2121.12]  So, you know, all this stuff is coming online.
[2121.20 --> 2122.52]  All these GUIs are starting to get written.
[2122.70 --> 2129.50]  Git Tower just went 1.0 yesterday, I think, which is a nice professional paid-for Mac app, Git GUI,
[2129.60 --> 2132.34]  that I've seen a lot of people using and liking a lot.
[2132.34 --> 2138.10]  So, yeah, anyways, I mean, as all that stuff happens, as all the GUIs get developed,
[2138.22 --> 2144.48]  and as these scripts get bindings that are fast and capable and have this nice API to them,
[2144.92 --> 2147.70]  I'm really excited to see what people are going to be doing with Git, right?
[2148.04 --> 2151.54]  So my job now is not so much doing sort of the proof-of-concept stuff,
[2151.56 --> 2155.28]  although I do do that a little bit with some things like large file support and things like that,
[2155.36 --> 2159.68]  but mostly telling people what's out there and then seeing what they do with it, you know?
[2162.34 --> 2167.04]  So as GitHub has become more and more popular,
[2167.22 --> 2171.36]  a lot of your users aren't necessarily experienced with source control systems,
[2171.44 --> 2176.24]  and I've found that, you know, a large number of the more, you know, the beginners, you know,
[2176.28 --> 2178.54]  don't understand Git as a concept fully.
[2179.36 --> 2180.86]  It's just a natural thing that happens.
[2180.98 --> 2183.38]  Is there anything that you feel that, you know,
[2183.40 --> 2187.84]  the whole community really needs to take the time to learn in general
[2187.84 --> 2192.28]  that you can think would help them a lot, like, you know, learning what rebase actually is?
[2192.34 --> 2193.52]  And things like that?
[2195.62 --> 2196.80]  I'm sort of split on that.
[2196.88 --> 2197.50]  I'm not really sure.
[2198.04 --> 2202.20]  I mean, what I like to do is teach sort of basic concepts of what Git is trying to do,
[2202.44 --> 2206.30]  because a lot of people, especially from the developer community
[2206.30 --> 2211.14]  and some designers and stuff as well, have come from the subversion world where,
[2211.70 --> 2215.00]  I mean, the interesting thing about version control is that most people for a long time
[2215.00 --> 2216.34]  don't take it seriously.
[2216.54 --> 2220.36]  It's not taught in universities, really, which might be part of the problem.
[2221.14 --> 2224.58]  You know, I was never really taught version control when I was at university,
[2224.64 --> 2225.50]  and that was fairly recently.
[2225.76 --> 2228.76]  You know, I mean, you know, I graduated in 2002, and I went to UCSD,
[2228.86 --> 2231.20]  and they didn't really teach version control anywhere,
[2231.30 --> 2235.76]  and it certainly wasn't, you know, it certainly wasn't sort of presented as a tool, right?
[2235.80 --> 2237.36]  They taught programming.
[2238.04 --> 2238.64]  They taught languages.
[2238.78 --> 2239.32]  They taught assembly.
[2239.44 --> 2241.62]  They taught, you know, all this stuff, but not version control.
[2241.70 --> 2242.34]  That was not really considered.
[2242.40 --> 2243.98]  And even, like, editors and stuff, right?
[2244.04 --> 2247.06]  But version control wasn't really considered a tool set that was important.
[2247.06 --> 2252.20]  And I think that's sort of gone through a lot of the industry is a lot of people don't.
[2252.28 --> 2254.00]  They see it as sort of a necessary evil, right?
[2254.02 --> 2256.78]  You have to have it so that you don't lose everything,
[2257.10 --> 2260.54]  not this is a tool that can make you better at your job, right,
[2260.56 --> 2263.30]  or can make your life easier as a developer.
[2263.50 --> 2265.58]  A lot of people don't see version control that way,
[2265.60 --> 2268.02]  and it may be because it hasn't really been like that as much.
[2268.38 --> 2271.58]  Whereas I feel Git, even though it's sort of complicated.
[2271.64 --> 2272.88]  I mean, it is more complicated.
[2272.88 --> 2274.32]  You can do very complicated things,
[2274.32 --> 2277.86]  but I think it's worth investing the time to learn it, to get a book, to read it.
[2278.06 --> 2282.00]  I mean, you know, I have stuff that's free and online.
[2282.18 --> 2288.32]  I've been trying to do a lot of evangelization for Git itself,
[2288.40 --> 2292.04]  but also, you know, writing stuff down so people can learn it as easy as possible.
[2292.22 --> 2296.40]  But I feel it's worth, like, people think that, you know, subversion,
[2296.52 --> 2299.20]  they're just like, okay, here's the eight commands you need, and that's it.
[2299.20 --> 2300.84]  And they don't really learn it in depth, right?
[2300.84 --> 2302.60]  And they kind of want to approach Git the same way.
[2302.60 --> 2309.60]  And I feel like it's important to learn it, to say this is a tool set that is as important as learning an editor, right?
[2309.66 --> 2313.50]  As learning VI or learning Emacs or learning, you know, Eclipse.
[2313.78 --> 2316.64]  Or, you know, everybody spends hours and hours learning their editor.
[2316.94 --> 2319.38]  Nobody uses Notepad to do programming, right?
[2319.90 --> 2322.34]  And subversion, people use it like Notepad.
[2322.44 --> 2325.44]  They're just, okay, I'm at some point, I'm going to commit, and that's it.
[2325.44 --> 2334.52]  And I feel like there should be more, people should take it seriously as a tool set that gives them power, right?
[2334.56 --> 2335.84]  That gives them a lot of power.
[2335.96 --> 2338.66]  Like learning Emacs as a power user or something gives you a lot of power.
[2339.20 --> 2340.58]  Learning Git gives you a lot of power.
[2340.72 --> 2345.58]  And that should be a focus of places to make sure that people, and even of schools and stuff,
[2345.62 --> 2351.02]  to make sure that people see that as that tool and not as a necessary annoyance, I guess.
[2351.02 --> 2358.14]  I mean, I can do Git in an hour, and I do that a lot, but I like the ones where it's all day,
[2358.24 --> 2361.60]  and I'm teaching a lot more stuff on how to think about version control
[2361.60 --> 2367.00]  and how to use it as a tool that makes you better at what you're actually trying to accomplish, right?
[2367.10 --> 2371.18]  At collaborating with people, at looking through your history, at figuring out what happened,
[2371.44 --> 2377.94]  at peer reviewing code, at doing merges and working independently on different branches at the same time,
[2378.00 --> 2378.84]  that sort of thing.
[2378.84 --> 2386.60]  So, yeah, I mean, I think it's more of a mind shift that people have to see the tool as a different class of tool
[2386.60 --> 2389.02]  than people used to think about version control, I guess.
[2389.88 --> 2393.68]  I'd like to switch gears for a moment and talk about another one of your projects, Showoff.
[2394.30 --> 2398.08]  What's the inspiration behind this, and what's the state of Showoff?
[2400.00 --> 2406.32]  Showoff is, I've been using it for almost all of my, it's a presentation tool.
[2406.32 --> 2412.32]  So, the idea behind Showoff is you write your slides, because I do a lot of talks, I do a lot of training,
[2412.46 --> 2416.20]  I do a lot of conference talks, and so I make a lot of slideshows, basically.
[2417.28 --> 2423.60]  And, you know, I mean, a lot of people do, it's, you know, one of the word processing, slideshows, Excel spreadsheets,
[2423.70 --> 2427.84]  like those are sort of the big sort of three that are in all the office formats, right?
[2427.84 --> 2429.14]  Because everybody uses them for stuff.
[2429.14 --> 2432.30]  So, I was using slideshows a lot.
[2432.62 --> 2434.52]  I used Keynote for a really long time.
[2434.60 --> 2435.28]  It was not bad.
[2435.36 --> 2437.30]  It's actually, you know, it's fairly nice software.
[2437.84 --> 2439.34]  But there's a lot of things I couldn't do with it.
[2439.68 --> 2441.96]  And one of them is version control, right?
[2442.04 --> 2445.36]  As I, you know, as I'm telling people to take version control more seriously,
[2445.36 --> 2449.38]  I try to make sure that all the stuff I'm doing is version controllable,
[2449.50 --> 2451.78]  especially for, like, the training stuff.
[2451.78 --> 2457.98]  Because if you think about it, if you're doing training, you know, every couple weeks or something,
[2458.10 --> 2461.94]  and it's variations on a theme where you have a whole bunch of different sections,
[2462.44 --> 2465.18]  and some companies want some sections and some want others,
[2465.58 --> 2469.40]  and it changes slowly over time or you have to customize stuff for certain companies,
[2469.56 --> 2472.28]  it's very nice to be able to branch and merge your presentation, right?
[2472.28 --> 2473.96]  And you can't do that with Keynote.
[2474.54 --> 2479.02]  It's just not really possible to do it and be able to manage it properly.
[2479.02 --> 2482.40]  And the other thing about presentations, especially the way that I do them,
[2482.84 --> 2487.16]  which is generally a couple of words on a slide, you know,
[2487.20 --> 2492.60]  I have a sort of bare presentation style, is it's just text, right?
[2492.60 --> 2493.88]  I don't have a ton of animations.
[2494.14 --> 2503.60]  Most of the stuff in word processors and in presentation software is 95% of that stuff is never used by anybody, right?
[2503.62 --> 2504.46]  Even if they know it's there.
[2504.54 --> 2508.26]  Just because I'll use it on one or two slides maybe for animation or something like that.
[2508.26 --> 2509.34]  But generally I don't care.
[2509.40 --> 2510.10]  It's just words.
[2510.92 --> 2513.98]  It's, you know, examples, code, things like that.
[2513.98 --> 2517.76]  And so what I wanted to do was have everything in a basic text format.
[2518.34 --> 2519.46]  So I chose Markdown.
[2519.66 --> 2524.22]  So you write everything in Markdown, and then you run a thing, and it creates HTML off of it,
[2524.26 --> 2526.60]  and then it's an HTML-powered presentation, right?
[2527.00 --> 2529.68]  But it's awesome because I can version control everything.
[2529.68 --> 2535.30]  I can have all the different subsections and subdirectories and then move them from slides to slides,
[2535.46 --> 2542.64]  or I have a little showoff.json sort of index file where I can remove lines in and out as I do and don't want different sections.
[2543.64 --> 2548.44]  And it just makes it as easy to write my presentations as it is to write code, right,
[2548.48 --> 2552.60]  and manage them and share them and have people fork them and fix them and send me pull requests,
[2552.66 --> 2553.82]  and all of that stuff works, right?
[2553.82 --> 2560.12]  If it's plain text, anything that you can do in plain text, I like doing in plain text if possible, right?
[2560.12 --> 2564.00]  And my presentations really didn't have that much that I couldn't do in plain text.
[2564.14 --> 2568.00]  It's just that there was no real tools to be able to do it very easily.
[2568.08 --> 2574.28]  There was like Slidy and S5 and stuff, and they didn't really fill my criteria of being simple and fast to write slides.
[2574.86 --> 2577.44]  And mine is just basic Markdown, and it works great.
[2577.80 --> 2581.48]  And then the other cool thing is you can add JavaScript, custom JavaScript, custom CSS.
[2581.48 --> 2588.16]  You can use tools that you use for web development to do custom things in your slideshows, right?
[2588.24 --> 2594.22]  So I put in – I do a lot of git commands, so I'll type a git command on the command line and then show the output.
[2594.76 --> 2600.44]  And it's very difficult to do in Keynote and then show off – I just use a jQuery plug-in that does typing,
[2600.56 --> 2604.06]  so it looks like I'm typing it at the time, and then all the output comes in after that.
[2604.24 --> 2606.42]  And I don't have to program any of that.
[2606.44 --> 2609.36]  I just have to put a style on the slide that says this is a code example.
[2609.36 --> 2612.46]  And it will just type it out for me as I'm hitting the button.
[2612.60 --> 2613.88]  So like that sort of stuff.
[2614.38 --> 2615.40]  You can also do fun stuff.
[2615.52 --> 2621.74]  Like the other week, I've been playing with the Kinect, you know, the Microsoft Kinect device.
[2622.40 --> 2625.90]  I got one of those, and I got the – there's open source drivers for them on GitHub.
[2626.56 --> 2628.24]  And so I was playing with that on the Mac.
[2628.72 --> 2632.60]  And I made it so I could control the presentation with a Kinect.
[2632.60 --> 2635.66]  So I used Firewaiter.
[2636.20 --> 2637.68]  You know, you guys are familiar with Firewaiter.
[2637.76 --> 2638.98]  It's like a browser testing thing.
[2639.16 --> 2639.24]  Right.
[2639.34 --> 2642.46]  So it'll click buttons in your browser basically for you.
[2642.96 --> 2644.32]  So I just hooked that up and made a –
[2644.32 --> 2644.62]  It's like Selenium.
[2644.96 --> 2645.32]  What's that?
[2646.16 --> 2646.84]  It's like Selenium.
[2647.14 --> 2648.34]  Yeah, it's Selenium, right.
[2648.34 --> 2662.62]  And so I made a really simple wrapper that just took input from the camera, cleaned it up, saw when I was doing left to right or right to left movements with my hand, and then hit buttons in the browser basically that made it go back and forth in the thing.
[2662.74 --> 2668.38]  So like that would be difficult to do in Kinect, like to try and send Kinect a signal to go to the next slide programmatically.
[2668.44 --> 2670.78]  And it's very easy to do because I'm using a browser, right?
[2670.82 --> 2674.60]  I mean all of the stuff that already works for browsers you can use with your presentation software.
[2674.60 --> 2677.26]  So that's what Showoff is.
[2677.34 --> 2680.36]  A lot of people are using it because it's fairly easy to do.
[2680.52 --> 2682.96]  It's easy to, you know, get up and running and version control.
[2683.18 --> 2692.94]  And you can say stuff like Showoff Heroku and it'll – you know, Heroku-wise it for you and you can push it to Heroku and then your presentation is on Heroku.
[2693.26 --> 2699.04]  Or now you can say Showoff GitHub and it'll create a GHPages branch.
[2699.12 --> 2702.54]  You can push it to GitHub and we'll serve it statically off of GitHub pages.
[2702.54 --> 2707.88]  So you can share the presentation easily and you can share the source for the presentation easily, which is really nice.
[2708.16 --> 2715.50]  One of the first Showoff presentations that I did, somebody did a presentation of Showoff in Showoff and then I wanted to do one as well.
[2715.64 --> 2718.50]  I had a little lightning talk that, you know, I wanted to do for it.
[2718.54 --> 2724.34]  So instead of creating my own, I forked his, changed it to fit the – you know, a little bit to fit the format of the new presentation.
[2724.46 --> 2728.36]  Then I gave a presentation on Showoff using Showoff, using a forked version of Showoff.
[2728.36 --> 2733.04]  So I was really happy with the metadness of basically that entire experience.
[2734.54 --> 2739.90]  The other cool thing about that is that – so that's – I mean, that's Showoff that you're asking about.
[2740.10 --> 2750.62]  But that's also an interest of mine is making tools for things that don't need huge, heavy, overdone GUIs for them that that's what the entire industry uses, right?
[2750.62 --> 2754.54]  So presentation software is an example. Word processing is another example.
[2754.92 --> 2759.36]  There's a lot of stuff that you need Word for, right, that does really complex stuff.
[2759.72 --> 2762.22]  But there's a lot of stuff, most stuff, that you don't.
[2762.32 --> 2766.64]  So I wrote a book for A-Press, the Pro-Get book I wrote for A-Press.
[2766.96 --> 2771.00]  And basically the process for that was you write everything in Word.
[2771.32 --> 2775.16]  They give you a style sheet that the publishing tools know about.
[2775.16 --> 2777.58]  So you have to stay within these like eight styles, right?
[2777.64 --> 2783.06]  So already you have a lot of constraints on that, right?
[2783.10 --> 2784.78]  So it's not like you can do anything in Word.
[2784.88 --> 2786.48]  You can't really use Word as the full tool.
[2786.70 --> 2788.32]  You can only use these ten styles.
[2788.86 --> 2796.00]  And so I felt that that was really dumb because it's basically just a bunch of words, inserted images, and then everything is constrained within these ten styles.
[2796.00 --> 2807.38]  Why are we not using Markdown, right, or Showoff, or I mean not Showoff, Markdown or ASCII Doc or some structured markup language that is very simple and does this thing simply, right?
[2807.70 --> 2810.92]  So I wrote my book in Markdown.
[2811.40 --> 2820.66]  I had to export everything from Markdown to Word for the copy editing phase and then export everything from Word back into Markdown to publish the website at the end,
[2821.06 --> 2824.82]  which was one of the most horrible experiences of my life generally.
[2824.82 --> 2834.42]  But what I'd really like to see is a tool chain for technical authors for writing books about open source projects,
[2834.54 --> 2842.94]  for writing just normal tech books like ProGit, like normal technical books that all of us read a couple times a year probably.
[2844.40 --> 2851.22]  I'd like that entire process to be much simpler because there's thousands of authors doing these books, and there should be more.
[2851.22 --> 2855.76]  There should be a small manual for every open source project, basically.
[2855.94 --> 2860.68]  I think it would be really helpful to have that, to have a Rails manual for every project.
[2860.98 --> 2865.44]  And it's not really done because the authors have to come up with all this stuff.
[2865.54 --> 2866.84]  They have to create a website for it.
[2866.86 --> 2872.82]  They have to figure out how to generate a PDF or a Mobi file or an EPUB file or all of the different publishing standards.
[2872.82 --> 2875.28]  But if you want to read it on your Kindle or your iPad or something, right?
[2876.32 --> 2882.46]  So that's one of the projects I'm working on right now is trying to do that for not just word processing,
[2882.62 --> 2888.90]  but like writing books or writing manuals or writing novels or anything that doesn't take – it's not a children's book, right?
[2888.96 --> 2897.26]  Anything that has text, a couple of styles, and maybe some code examples or some math formulas and some images, and that's it, right?
[2897.26 --> 2897.74]  That's GetScribe.
[2899.18 --> 2899.62]  What's that?
[2899.74 --> 2900.50]  Yeah, so that's GetScribe.
[2900.80 --> 2901.80]  So I'm working on that right now.
[2902.84 --> 2916.92]  And I'm actually sort of in the process of possibly creating a guide to GitHub book for O'Reilly where I actually use this process to write the book,
[2917.00 --> 2918.60]  so sort of as a pilot project for it.
[2918.60 --> 2922.44]  So I'm doing that and the book simultaneously so that I can make sure that the process is good.
[2922.50 --> 2925.98]  But, I mean, there's a lot of other things for writing technical books, handling translations,
[2926.94 --> 2931.44]  pegging versions of the book to versions of the application that you're trying to document,
[2932.88 --> 2934.88]  you're taking errata, all that stuff.
[2934.88 --> 2938.68]  And every technical book publisher does not do this well, basically.
[2938.94 --> 2943.32]  I mean, they have different variations of how they do this, but a lot of it is doc book,
[2943.32 --> 2948.90]  which is better in that it's text and you can merge it and stuff like that, but not very easily.
[2950.16 --> 2953.46]  Or most of it is Word documents, and that's just awful.
[2953.56 --> 2954.34]  I have to kill that.
[2955.04 --> 2961.02]  My goal in life is to kill Word documents for technical publishing because it's not necessary.
[2961.30 --> 2962.98]  It's so overkill and bad.
[2963.52 --> 2970.94]  You have to lock the chapter sort of one chapter at a time through like soft email locks and say the technical editor has this chapter now.
[2971.06 --> 2972.58]  And that's just horrible, right?
[2972.58 --> 2977.50]  There's no reason that shouldn't be mergeable, and you shouldn't be able to get line-by-line changes.
[2978.04 --> 2978.40]  Absolutely.
[2978.72 --> 2985.52]  We're writing a book on SaaS for Manning, and Jason Williams is writing the RabbitMQ book.
[2986.02 --> 2992.38]  Luckily, it's trailblazed a lot of this for me where I'm writing in Markdown as well, kind of like what you were doing.
[2992.46 --> 2995.56]  But it's a crazy tool chain with Haskell and some other tools in there.
[2995.60 --> 3000.10]  We just need to find some sort of standard that not only for open source books and e-books, but even all the publishers.
[3000.10 --> 3003.74]  Because I think I've done three different publishers, and they all have a different workflow.
[3003.74 --> 3017.12]  Yeah, I mean, eventually, I'd like to see – I think ASCII doc is a fairly good sort of text standard for that because it outputs the doc book, and there's a lot of tool chains that will take doc book and give you nice-looking PDFs and that sort of thing.
[3017.12 --> 3026.46]  So that's what I'm concentrating on is having some Rails-type thing for writing books where you can say, get Scribe init, and it gives you a layout for how to write the book.
[3026.88 --> 3027.86]  Here's where to put images.
[3028.22 --> 3029.60]  Here's what the ASCII doc looks like.
[3029.64 --> 3030.78]  Here's a cheat sheet for ASCII doc.
[3031.38 --> 3032.60]  You just commit there.
[3033.28 --> 3034.02]  You push to GitHub.
[3034.22 --> 3039.14]  We generate EPUB, MOBI, HTML, chunked HTML, that sort of stuff for you.
[3039.14 --> 3043.82]  And you don't have to worry about – the authors don't have to worry about any of that, right?
[3044.46 --> 3047.80]  The author's job should just be writing words and nothing else.
[3048.08 --> 3052.20]  And there's no tool chain for that right now, and everybody makes up their own.
[3052.28 --> 3057.84]  So if you're an author and you go back and forth between different publishers, it's a whole new game of horrible, right?
[3059.48 --> 3062.04]  All right, so one last question before we're running out of time here.
[3062.72 --> 3064.10]  Who is your programming hero?
[3064.10 --> 3070.70]  Everybody that works at GitHub is basically my programming hero.
[3071.76 --> 3081.82]  It's actually really embarrassing because, you know, I've been working – I've been doing computer programming for, what, 10 or 12 years, I guess.
[3082.46 --> 3083.58]  About 10 years, probably.
[3084.20 --> 3093.16]  And, you know, most of the places that I was at, I kind of felt like, you know, a lot of these guys – you know, I had a lot to teach everybody.
[3093.16 --> 3097.30]  And, you know, especially at the beginning when you're sort of the arrogant right out of school guy.
[3097.48 --> 3098.68]  You know, like, you guys are all idiots.
[3098.80 --> 3099.52]  This is how we do it.
[3100.70 --> 3106.56]  But now at GitHub, it's the first place where, you know, I kind of feel like everybody that I work with is smarter than me.
[3107.28 --> 3110.74]  And I think a lot of the other guys kind of feel that as well.
[3110.86 --> 3113.14]  So it's just a high-quality place.
[3113.14 --> 3117.98]  But I'm constantly looking at Chris's code for examples of how to do stuff.
[3118.14 --> 3131.54]  Like if I say – you know, if I'm saying I'm writing some command line thing, I look for something, you know, at RIP or something that Chris has written or Tom or something as a command line tool and say, what are the tools that they were using, you know, to do this?
[3131.54 --> 3135.30]  And because, you know, they're all really, really smart guys.
[3135.72 --> 3140.28]  So – and then everybody that we've been hiring after, I mean, we were all sort of more generalists.
[3141.02 --> 3145.32]  Everybody that we've been hiring since then are so, you know, laser-focused.
[3145.54 --> 3150.60]  I mean, Ryan Tomeko is one of the smartest guys that, you know, I know.
[3150.60 --> 3158.68]  And so it's almost embarrassing to hire these guys because then they go through and look through your code and, you know, you just – you don't want that to happen.
[3159.20 --> 3160.14]  They're like, what were you thinking?
[3160.24 --> 3161.86]  And I'm like, I don't remember.
[3164.22 --> 3172.90]  So, yeah, nowadays it's a lot of the newer guys that, you know, are really, really smart going through my code and telling me what I did wrong in the first place.
[3172.90 --> 3183.84]  But, yeah, so I can basically learn from everybody at GitHub for a long time to come because they all have – they're all different in different ways, right?
[3183.92 --> 3187.74]  Different – I mean, Ryan's – anyways, that's – yeah.
[3189.52 --> 3190.20]  Awesome stuff.
[3190.26 --> 3191.22]  Well, thanks for taking the time.
[3191.62 --> 3192.76]  That was a horrible answer.
[3192.92 --> 3193.44]  I'm so sorry.
[3193.74 --> 3194.54]  That was perfect.
[3194.88 --> 3196.04]  Thanks for taking the time today, Scott.
[3196.08 --> 3196.92]  We surely appreciate it.
[3198.12 --> 3198.62]  Yeah, absolutely.
[3198.72 --> 3199.12]  This is fun.
[3202.90 --> 3217.78]  See it in my eyes
[3217.78 --> 3221.42]  So how could I forget when
[3221.42 --> 3224.58]  I found myself
[3224.58 --> 3227.18]  For the first time
[3227.18 --> 3230.88]  Safe in your arms
[3230.88 --> 3233.52]  And it's all cas compressed
[3233.52 --> 3259.64] 夜
