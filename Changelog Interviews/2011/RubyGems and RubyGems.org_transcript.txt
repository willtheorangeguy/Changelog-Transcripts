[0.00 --> 18.78]  Welcome to the ChangeLog episode 0.5.9.
[18.98 --> 20.04]  I'm Adam Stachowiak.
[20.28 --> 21.16]  And I'm Winn Netherland.
[21.32 --> 22.30]  This is the ChangeLog.
[22.36 --> 23.90]  We cover what's fresh and new in open source.
[24.30 --> 27.32]  If you found us on iTunes, we're also on the web at thechangelog.com.
[27.58 --> 28.52]  We're also up on GitHub.
[28.52 --> 32.48]  At GitHub.com slash explore, you'll find some trending reposts,
[32.56 --> 36.70]  some feature reposts from our blog, as well as the audio podcast you're listening to.
[37.18 --> 40.32]  If you're on Twitter, follow ChangeLog Show and me, Adam Stach.
[40.82 --> 43.34]  And I'm Penguin, P-E-N-G-W-I-N-N.
[43.82 --> 45.84]  And this episode is sponsored by GitHub Jobs.
[45.94 --> 48.82]  Head to thechangelog.com slash jobs to get started.
[49.34 --> 52.68]  If you'd like to feature your job on this show, select Advertise on the ChangeLog.
[53.10 --> 54.68]  When you post your job, we'll take care of the rest.
[54.68 --> 58.72]  Asana is looking for a software engineer in San Francisco, California.
[59.30 --> 60.80]  Great perks on this one.
[60.92 --> 65.66]  In-house yoga, executive life coaching, organic home-cooked meals twice a day,
[65.78 --> 68.70]  and the kicker, three 30-inch monitors.
[68.88 --> 73.34]  Actually, they'll let you spend up to 10K on your own rig, however you think best.
[74.00 --> 75.36]  Be sure and check this one out.
[75.46 --> 78.56]  Asana is lg.gd slash aj.
[78.56 --> 81.00]  Next up is CrowdTap.
[81.10 --> 83.20]  CrowdTap is looking for a Rails software engineer.
[83.40 --> 87.74]  They're an exciting NYC startup based in the Union Square area.
[87.84 --> 90.90]  They're looking for Ruby and Ruby on Rails engineers to join their team.
[91.34 --> 96.64]  If you're using jQuery, Rails 3, MongoDB, Redis, the, as Wynn says it,
[96.66 --> 100.30]  the usual suspects, Rescue, RSpec, Cucumber, the list goes on.
[100.66 --> 103.86]  If you're using any of those fun tools, they want to talk to you.
[103.86 --> 108.80]  And if you want to work with them, check out lg.gd slash am.
[109.40 --> 114.34]  Secure Endpoints is looking for software engineers in New York or elsewhere full-time.
[114.68 --> 119.06]  They develop single sign-on identity management and secure data access solutions,
[119.32 --> 123.60]  including Network Identity Manager, Kerberos, Microsoft Windows Platform.
[123.84 --> 127.84]  So they're also looking for folks on Windows, Mac OS, and Linux,
[128.30 --> 130.30]  mobile client development, iOS, and Android.
[130.30 --> 135.76]  If you're interested, be sure and check the shortcode lg.gd slash ak.
[136.78 --> 140.14]  A fun episode this week, an excerpt from our live show at Red Dirt RubyConf.
[140.18 --> 145.04]  We talked to Nick Caranto from Gem Cutter's now, or Gem Cutter now, Ruby Gems,
[145.26 --> 147.80]  and the whole backstory of how that project came about
[147.80 --> 151.38]  and how it morphed into, I guess, Ruby Gems 2.0
[151.38 --> 157.28]  and the philosophy behind what goes into a good Ruby gem, gem spec.
[158.24 --> 161.74]  Intro to creating a Ruby gem if you are new to the process.
[162.44 --> 165.60]  You've got about a zillion gems out there between all the APIs you work with.
[166.10 --> 168.08]  I've got several. You've got a couple.
[168.40 --> 169.10]  Just a couple.
[169.44 --> 171.02]  It's not as hard as you would think, right?
[171.20 --> 172.00]  I don't think so, no.
[172.12 --> 173.76]  I think if you're intimidated, it's your own fault.
[173.84 --> 175.48]  You should just give it a try.
[176.04 --> 177.32]  So easy and Adam can do it.
[177.68 --> 178.42]  There you go.
[179.26 --> 180.38]  Fun episode. Should we get to it?
[180.38 --> 181.10]  Let's do it.
[190.36 --> 192.40]  All right. We're joined by Nick Caranto.
[192.62 --> 192.88]  Yes.
[193.54 --> 194.50]  From Boston.
[195.20 --> 195.52]  Yes.
[195.94 --> 196.26]  Originally?
[196.58 --> 199.06]  No. I'm from Buffalo, New York.
[199.54 --> 202.14]  Known on the interwebs as Q-Rush.
[202.62 --> 203.96]  Crush? I'm not sure how to pronounce that.
[203.96 --> 204.46]  Either works.
[204.74 --> 205.00]  Cool.
[205.50 --> 210.12]  He was just lamenting the fact that we don't have the high-end Dan Benjamin golden microphones.
[210.12 --> 212.66]  We should have that for the next year's podcast.
[212.98 --> 220.34]  So I wanted to talk a bit about your gem cutter project that turned out to be, I guess, RubyGems part deux.
[221.24 --> 221.70]  Basically.
[222.04 --> 222.92]  That's one way to put it.
[222.92 --> 230.52]  Talk us through the background of gem cutter and how, I guess, it progressed without stealing too much thunder from your talk tomorrow.
[231.14 --> 231.40]  Sure.
[232.34 --> 237.08]  So gem cutter started as a little side project of mine at Boston Ruby Group.
[237.08 --> 241.18]  I had just been getting into gems and publishing them.
[241.18 --> 246.40]  I got in around the GitHub area where you had to check a box and you hoped it worked.
[247.10 --> 247.94]  And then it didn't work.
[248.02 --> 248.52]  And then you checked.
[248.62 --> 251.94]  And someone even wrote a site that you went to it and you looked at it.
[252.02 --> 252.76]  Anyone remember this?
[253.02 --> 253.94]  It was like, no?
[254.50 --> 255.28]  I haven't seen something.
[255.44 --> 256.28]  So it was pretty terrible.
[257.86 --> 259.02]  So that was pretty bad.
[259.28 --> 261.94]  And I actually tried to sign up for a RubyForge account.
[262.04 --> 263.28]  And I signed up for a fake gem.
[263.42 --> 264.22]  And then they said no.
[264.22 --> 264.26]  Yeah.
[264.58 --> 266.76]  That's like, I basically typed in a bunch of garbage.
[266.94 --> 270.44]  And they actually had someone going in and saying, oh, yeah, you can publish a gem now.
[270.98 --> 273.40]  So I thought that was really not good.
[273.94 --> 278.74]  So I started talking to Josh Nichols, who wrote the Jula gem, who was in Boston at the time.
[279.48 --> 282.38]  And Tom Preston Werner about what could we do to make this better.
[283.76 --> 285.62]  And we just went from there.
[286.64 --> 292.22]  So basically laid out a few ideas about what the site could look like, what it would provide.
[292.22 --> 295.26]  And just tried to figure it out.
[295.80 --> 300.28]  For a while it was, come listen to Nick's crazy idea of how to kill RubyForge.
[300.84 --> 304.64]  And then realized that wasn't the best marketing term for it.
[305.08 --> 307.18]  But I think it's worked out pretty well.
[308.14 --> 312.06]  Did you have that plan going in to replace RubyForge?
[312.36 --> 314.08]  I mean, kind of.
[314.16 --> 317.14]  The way we were looking at it, it was like, there's no other way.
[317.14 --> 326.86]  So it was either this other weird gem source kind of hanging out that people would be like, well, do I use gemcutter or RubyForge or GitHub?
[327.04 --> 327.86]  Which one do I use?
[328.36 --> 332.08]  So I think the plan was just to improve what we had.
[332.38 --> 334.26]  Because it obviously wasn't ideal.
[335.12 --> 341.64]  So I think that's, besides the prior motivation I just said, which wasn't very nice.
[341.82 --> 342.36]  We're nice here.
[342.36 --> 347.30]  So that was really the driving force was to, it's going to have to be.
[347.84 --> 351.44]  And there's no reason for it, there's no reason for it not to be.
[351.74 --> 353.66]  Especially with the guys that run the RubyGems project.
[353.84 --> 356.96]  I feel that you have to really prove that the code you write works.
[357.42 --> 359.78]  So I had to set out going to that first.
[359.86 --> 363.20]  Like if I was to go to them and say, oh, here's this idea, they would have been like, no.
[363.92 --> 364.64]  That's not going to work.
[365.00 --> 368.00]  So I had to prove it first and then I went to them and that worked.
[368.08 --> 369.56]  So how did that conversation go about?
[369.56 --> 370.80]  Did you approach those guys?
[370.88 --> 371.54]  Did they approach you?
[372.68 --> 380.42]  It got to a point when Peter Cooper wrote a blog post on Ruby Inside about it.
[380.86 --> 386.36]  And this is just after I had gotten it actually working and people could actually download gems from it.
[387.04 --> 392.50]  And he'd be like, oh, here's this new gem hosting service taking on these other sites.
[393.10 --> 394.32]  And that wasn't really the point.
[394.42 --> 396.26]  I just wanted to fix what we had.
[396.26 --> 401.26]  So it was around then where I really started realizing, okay, we need to figure this out.
[401.34 --> 402.72]  We need to figure out what's going to go forward.
[402.88 --> 404.70]  So I drafted up a little plan and showed it to them.
[404.80 --> 407.96]  But before that, I had not really talked to them at all.
[408.04 --> 409.12]  But luckily they've been really cool.
[409.24 --> 412.74]  They've been very nice and open to the ideas we had.
[412.76 --> 413.62]  And they jumped on it.
[414.70 --> 416.22]  I wouldn't say immediately, but very quickly.
[416.22 --> 420.98]  Who here has written and released a gem up on RubyGems?
[421.98 --> 422.80]  Quite a few folks.
[422.94 --> 424.10]  The rest of you, why not?
[425.74 --> 428.52]  So for the uninitiated, what is a gem?
[429.44 --> 429.70]  Okay.
[429.92 --> 434.04]  So a gem is basically a bunch of Ruby code that you can share.
[434.54 --> 435.70]  That's like the simplest thing.
[435.80 --> 437.30]  It's a way to share Ruby code.
[437.30 --> 447.72]  The actual internals of it, it's actually a tarball that has a YAML metadata hunk and then your files.
[448.56 --> 455.38]  So that's what RubyGems handles, sharing that and tossing it around your system and making sure it's in the right place.
[456.22 --> 461.32]  And then it also handles actually requiring all that Ruby code that's in the gem at that time.
[461.32 --> 468.44]  So there's a lot of magic it kind of has, and that's to make your life a lot easier.
[469.50 --> 471.50]  So I hate to use the word manifest, but I will.
[471.58 --> 474.58]  But I guess the gem spec is sort of the manifest of the package.
[474.84 --> 475.94]  What all goes in that?
[475.94 --> 484.54]  Yeah, so the gem spec has everything from the name of the package to the version to the date to the files that's in it to the description to an email.
[484.54 --> 498.68]  If you depend on other gems, if you depend on other software packages, it's a huge sprawling list of things that not everyone fills out, which is very challenging.
[498.90 --> 499.50]  It fills out well.
[499.80 --> 505.02]  You know, an intriguing part about the gem spec is it's actually, you can execute Ruby in it, right?
[505.56 --> 506.20]  Yes and no.
[506.68 --> 507.58]  It shouldn't, maybe?
[507.58 --> 512.22]  So the gem spec, I mean, the spec itself is in Ruby, but it gets saved as YAML.
[512.64 --> 512.76]  Okay.
[512.76 --> 515.78]  And, I mean, that's eventually what it boils down to.
[515.92 --> 523.48]  And you can't, I mean, you can put, like, Ruby code in there, but when you're packaging up a gem, it's going to save the YAML.
[523.56 --> 524.38]  It's not going to save the Ruby.
[524.50 --> 528.96]  Because, I mean, we can't just arbitrarily execute Ruby code on servers.
[529.28 --> 532.84]  So that doesn't work out too well, as time has shown.
[533.56 --> 540.72]  Early in my gem publishing days, you know, I would go back and forth of, somebody would fork the project, submit a patch, but they would mess with the gem spec.
[540.92 --> 541.12]  Yeah.
[541.12 --> 546.58]  Right, and there's this big hubbub around, do you put the gem spec in Git or do you not?
[546.96 --> 551.82]  You know, if you want to be able to use Bundler from GitHub, it's required, right?
[551.88 --> 554.46]  But what is the etiquette, I guess, around the gem spec?
[554.60 --> 558.38]  There's so many, so many different ways to do it.
[558.38 --> 562.54]  I wish, I wish almost Git had a thing that you could say, don't touch these ever.
[562.68 --> 566.26]  And Aaron even mentioned it in his talk, to not touch build systems.
[566.26 --> 575.40]  The way that we tend to do it now is we actually put the gem spec in the rake task, in the rake file.
[575.52 --> 578.46]  So there's a rake gem package task.
[578.72 --> 583.32]  I don't know the exact name of it, but rake provides a way to package gems and generate the gem file.
[583.72 --> 585.50]  And then I'll actually ignore it from Git.
[585.50 --> 586.84]  So I won't even start in Git at all.
[587.30 --> 592.92]  And the actual, like, version will be inside the Ruby gem somewhere, and all the information I need will be in the rake file.
[593.64 --> 594.66]  That's the way we're doing it now.
[594.78 --> 597.16]  I honestly, I don't know what the best way to do it is.
[597.26 --> 600.64]  I think as long as it's in version control, that's good enough.
[600.64 --> 608.62]  It seems like Bundler has, you know, advanced the landscape of gem dependencies, or I guess Ruby library dependencies, to put it another way.
[609.16 --> 611.02]  Are we still advancing that cause?
[611.14 --> 614.82]  Are there problems to be solved, or is this the future?
[615.00 --> 617.12]  As in just managing dependencies, or?
[617.80 --> 623.56]  Managing dependencies and basically versionings of those dependencies and things of that sort.
[624.36 --> 625.62]  Gem sets, the whole nine yards.
[626.00 --> 629.64]  I mean, I'm sure I'm not the only one who's been waiting on fetching source index, right?
[630.40 --> 630.42]  Yeah.
[630.64 --> 632.02]  Does anyone else hate that error message?
[632.06 --> 632.58]  I hate it, too.
[633.14 --> 635.04]  So there's a lot of problems to be solved there.
[635.12 --> 644.42]  And actually, the new Bundler release, 1.1, is using a new API that we wrote in GemCutter to make dependency resolution a lot faster.
[644.78 --> 645.34]  And that's perfect.
[645.42 --> 647.32]  That's the exact reason why GemCutter is there.
[647.32 --> 652.22]  So we can actually, in Ruby, write new APIs that will help out the community and get them out there faster.
[652.86 --> 654.44]  So hopefully that will be released soon.
[655.18 --> 659.62]  We had the endpoint done a while ago, but Bundler is a big project, and it's very complicated.
[659.62 --> 662.72]  It's not easy to mess around with it.
[662.92 --> 665.66]  But it's complicated, and it does a lot of things.
[665.92 --> 668.86]  So the war is definitely not over by any means.
[669.00 --> 670.90]  Who's driving the roadmap of GemCutter?
[671.08 --> 673.84]  Is it totally community-driven, or do you have a vision for it?
[673.84 --> 677.14]  I guess it's...
[677.14 --> 679.92]  I wouldn't say there is a roadmap.
[680.54 --> 681.14]  There should be.
[681.78 --> 682.64]  I should work on that.
[683.12 --> 684.70]  I would say it's more community-driven.
[684.80 --> 687.04]  We do have a lot of features and feature requests.
[687.14 --> 691.50]  I try to get them in as soon as I can, but if I'm not happy with the code quality, I'm not going to bring it in.
[692.50 --> 697.72]  Luckily, though, there's been a lot of contributors, and I want to make it as easy as possible to contribute.
[697.72 --> 704.52]  I think the big things we need, and this is kind of killing some things I'm going to talk about,
[704.96 --> 709.62]  but we need these bigger overarching things we need that is not really part of GemCutter,
[709.72 --> 711.38]  but is part of the RubyGems ecosystem.
[712.08 --> 719.60]  So things like redundancy and mirroring that every other open source community has.
[719.60 --> 723.56]  We get laughed at because we don't have mirrors for RubyGems.
[723.86 --> 725.08]  I get laughed at.
[725.66 --> 730.60]  So there's these problems we need to fix, and it may or may not be within the scope of GemCutter,
[730.70 --> 733.40]  but the nice thing is that we can actually adapt it a lot faster now.
[733.48 --> 739.88]  It's not a huge monolithic PHP site that we are kind of worried to touch.
[740.34 --> 744.84]  So I guess the takeaway is if you do have mirrors, you have to host them on multiple cloud providers for days like today.
[744.84 --> 746.50]  Yeah, I think I know who to talk to.
[746.50 --> 752.20]  So when you go to create a new gem, to the extent that you do,
[752.34 --> 756.70]  so your own personal preference of creating that gem spec, are you close to the metal manual,
[756.86 --> 758.40]  or do you like helper tools?
[758.96 --> 762.82]  Yeah, I mean, I started using Jeweler, so I tend to default to that.
[763.28 --> 764.60]  It's gotten a bad rap lately.
[766.08 --> 766.66]  I don't know.
[766.70 --> 767.04]  There's so many.
[767.12 --> 768.24]  I know a lot of people that use hoe.
[768.36 --> 769.78]  I know a lot of people that hand roll stuff.
[770.10 --> 775.32]  I tend to go to Jeweler by default just because it generates all the junk I usually need,
[775.32 --> 777.20]  like a spec directory and features.
[777.64 --> 779.60]  And it starts complaining at you if you don't write tests.
[779.78 --> 781.06]  So hopefully you're doing that.
[781.68 --> 783.20]  But I mean, I've hand rolled stuff as well.
[783.52 --> 786.90]  I think the problem with hand rolling is I don't even remember what's going on.
[787.10 --> 790.78]  So the nice thing is that Jeweler kind of sets that up and then complains at you until you fix it.
[791.36 --> 796.90]  And it's not like hoe, where hoe will always complain at you if you don't do certain things and follow their way.
[796.90 --> 798.54]  So I don't know.
[798.62 --> 801.66]  I think just use it the best tool that you can and whatever you're familiar with.
[801.76 --> 806.22]  As long as it's not like, as long as it's somehow automated, that's the important thing.
[806.74 --> 808.78]  Who's leading the charge, I guess, in this area?
[808.86 --> 814.16]  Because it seems like it's kind of a lot of falling forward and you're just listening to the other alpha geeks
[814.16 --> 818.30]  when they bark at you and do something that probably they figured out a long time ago.
[818.30 --> 829.00]  So case in point, around the gem spec in the GitHub or in the Git repository and things like that,
[829.06 --> 834.44]  but also like Ryan's post, I guess several years ago now, around not requiring RubyGems.
[834.54 --> 838.16]  It seems like there's no canonical place to go and say, okay, this is how you do.
[838.98 --> 842.20]  No, the RubyGems doc site is not good.
[842.20 --> 848.46]  And one of the things that was brought up really recently is that there's no real community place to go.
[848.58 --> 849.94]  Like, well, here's how we do things.
[850.78 --> 854.74]  And that may not broadly apply, but at least a general set of rules to say, like,
[855.06 --> 857.74]  okay, don't require RubyGems.
[858.44 --> 860.82]  Don't mess with the load path if you don't need to.
[862.60 --> 869.04]  Don't throw constants in weird places, like at the top of files.
[869.04 --> 875.46]  I remember at one point when I was doing the gemcutter gem, which is a gem plugin,
[875.76 --> 878.96]  and the gem plugins get loaded every time you bring in RubyGems.
[879.56 --> 883.74]  And I would put a URL constant in there, this rental URL.
[883.88 --> 889.66]  So anyone that had ever installed that gem had a URL constant defined in their app, always.
[890.00 --> 891.38]  It's like, I had no idea that was the case.
[891.40 --> 892.08]  I just put it there.
[892.14 --> 892.74]  I had no clue.
[893.24 --> 894.86]  So I think that's a huge community problem.
[894.92 --> 896.24]  I don't know who's, no one's leading that.
[896.24 --> 900.30]  So I think there should be more information on where that is.
[900.76 --> 903.20]  And that could be a whole separate site, and I'd love to help out with it.
[903.44 --> 908.06]  What was the transitional gemcutter command that you had to do before the command line,
[908.14 --> 909.56]  before the RubyGems switchover?
[910.20 --> 910.56]  Migrate.
[911.62 --> 912.34]  That was fun.
[913.54 --> 919.80]  So that was, so that command existed, make me think back a little bit.
[919.80 --> 926.18]  So that command existed when RubyForge was still around, because we had to somehow figure out that you owned a gem.
[926.74 --> 934.06]  And the use case I was always thinking of was that, okay, I need to make sure someone like DHH isn't going to come to my house and kill me
[934.06 --> 937.94]  for pushing a new Rails gem, or pushing Rails 3.0 by accident.
[938.48 --> 943.22]  So, because there's a few things in the gem spec that we can't trust, like the email.
[943.22 --> 951.16]  So that command actually would like upload a file to your gem's FTP space on RubyForge, which I had no idea existed,
[951.54 --> 954.16]  and then look for it on the gemcutter side.
[954.20 --> 954.72]  It was a mess.
[954.86 --> 955.54]  That's gone now.
[955.72 --> 956.12]  Thank goodness.
[957.08 --> 960.34]  But it was a weird transition for a little bit.
[960.34 --> 967.76]  So, GitHub is out of the gem building business, right?
[967.76 --> 967.96]  Yes.
[968.14 --> 974.34]  Is there any, I guess, valid reason to have a namespace gem upon gemcutter?
[975.10 --> 975.30]  No.
[976.34 --> 978.22]  Oh, well, yes and no.
[979.28 --> 985.38]  So, I mean, so the namespace gem, so like your GitHub username and then the name of the gem,
[985.58 --> 987.98]  those were there because GitHub couldn't do it any other way.
[987.98 --> 992.18]  And there's been a lot of discussion about how to do forked gems.
[992.82 --> 993.82]  And that's basically what it is.
[993.82 --> 999.40]  If you're forking a gem and you want to publish it, I think now that bundler is around,
[1000.64 --> 1006.16]  which it wasn't when we did the cutover, and that you can specify, you can do a dependency
[1006.16 --> 1008.96]  on a git repository, I think that's perfect.
[1009.10 --> 1009.90]  You should just use that.
[1010.00 --> 1013.10]  You shouldn't waste time pushing a gem when you can just hook it up right there.
[1013.38 --> 1014.94]  And you can even specify a rep.
[1014.94 --> 1019.60]  So if you're going, if you really want to get nutty with it, you can set a tag in your
[1019.60 --> 1022.84]  own repo that isn't going to be in the main repo and that maintainer will never pull it
[1022.84 --> 1023.02]  in.
[1023.24 --> 1025.20]  And then make sure that you're always locked to that one.
[1025.66 --> 1032.14]  So I think that's a lot better than pushing it up, having to wait for it, and then dealing,
[1032.32 --> 1034.78]  like you have to maintain that gem instead of just the repo.
[1035.32 --> 1041.48]  I would imagine just the sheer virtue of creating gemcutter, you see a lot more inbound gems than
[1041.48 --> 1042.58]  the average person.
[1042.58 --> 1047.56]  What's the funniest post-install commit message that you've seen in a gem?
[1048.74 --> 1051.18]  For instance, the HTTP party.
[1051.32 --> 1051.64]  Party.
[1051.82 --> 1052.66]  You know, it's party hard.
[1053.70 --> 1055.62]  I'm surprised more people don't abuse that.
[1056.24 --> 1059.60]  Because that's like the only thing you can do after gem install is you can actually print
[1059.60 --> 1060.28]  the whole message.
[1060.68 --> 1064.82]  So I'm surprised people don't like, it's only a string, but I don't know how long that
[1064.82 --> 1065.64]  string can get.
[1065.64 --> 1066.50]  Right.
[1066.80 --> 1068.24]  So someone...
[1068.24 --> 1068.94]  Well, we...
[1068.94 --> 1071.02]  Eric crammed quite a bit into the...
[1071.02 --> 1072.90]  I'm not sure if this is new and one for the Twitter gem.
[1072.98 --> 1078.34]  It now actually gives you the mailing list and some resources to follow to commit back
[1078.34 --> 1080.52]  to the gem, which I thought was a unique way to use it.
[1080.56 --> 1085.58]  It seems like the humor aspect seems to be the more prevalent use case.
[1085.64 --> 1086.80]  I haven't seen too crazy.
[1086.80 --> 1091.04]  There's definitely been a lot more like silly gems posted because you don't have to wait
[1091.04 --> 1091.82]  a few days.
[1092.00 --> 1095.82]  Like the meme generator gem and a few gems that do terrible things that I won't talk
[1095.82 --> 1096.08]  about.
[1096.64 --> 1098.94]  But there's a few funny gems.
[1099.32 --> 1100.84]  Not so much funny post-install.
[1101.42 --> 1104.40]  But maybe that could be a whole new era of comedy in the Ruby community.
[1104.76 --> 1106.66]  I'll throw the same question at you that I threw at Wes.
[1107.26 --> 1110.16]  You know, gems in the fog library are means to an end.
[1110.50 --> 1111.08]  What's your end?
[1111.14 --> 1111.62]  What are you building?
[1112.58 --> 1113.48]  With gem cutter?
[1113.64 --> 1114.20]  With anything.
[1114.20 --> 1118.46]  Sunday afternoon if you're just coding, if you're lame like me and that's what you
[1118.46 --> 1119.50]  do on a Sunday afternoon.
[1120.32 --> 1122.08]  Believe me, I'm that lame as well.
[1123.48 --> 1124.36]  I'm no different.
[1124.62 --> 1128.32]  So I've been working a lot with Redis lately and I've given a few talks on it.
[1128.78 --> 1132.18]  And I'm in the process of writing a service that uses it, so I've just been knee deep.
[1133.00 --> 1136.16]  This week I've been doing a lot with Event Machine.
[1136.36 --> 1138.58]  I've never used Event Machine before seriously for anything.
[1139.64 --> 1144.06]  Apparently they do timers really well, which is really hard to write and they do it really
[1144.06 --> 1145.86]  well, so I'm going to let Event Machine do that.
[1146.28 --> 1151.08]  So I've been messing around with Redis and Event Machine, trying to wrap my head around
[1151.08 --> 1151.28]  it.
[1152.20 --> 1155.64]  So besides that, not too much outside of the gem cutter world.
[1155.68 --> 1159.86]  There's definitely always a lot of pull requests and bugs that suck up a lot of time.
[1160.90 --> 1161.64]  Thanks for joining us.
[1161.68 --> 1163.42]  We need to clear off the stage for Dr. Nick's keynote.
[1163.78 --> 1163.98]  All right.
[1164.06 --> 1164.50]  Appreciate it.
[1164.56 --> 1164.80]  Thanks.
[1165.06 --> 1165.60]  Thanks, everyone.
[1165.60 --> 1166.06]  Thanks, guys.
[1166.68 --> 1168.44]  Thank you.
[1168.74 --> 1169.36]  Again.
[1169.36 --> 1169.42]  Thanks.
[1169.96 --> 1170.14]  Thanks.
[1170.14 --> 1170.44]  Love you.
[1180.88 --> 1181.52]  Yeah.
[1181.60 --> 1184.06]  And we'll see you next week.
[1185.40 --> 1187.52]  You
[1187.52 --> 1189.64]  You
