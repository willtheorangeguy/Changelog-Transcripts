[0.00 --> 4.36]  The Change Log is brought to you by Pusher, a service that lets you add real-time features into your app.
[4.66 --> 7.40]  With libraries for JavaScript, Ruby, PHP, and more,
[8.02 --> 11.66]  Pusher makes it super easy to push data from your backend to your connected clients.
[12.20 --> 18.42]  Check out pusher.com slash showcase to see what gauges, cloud app, and many others have already done with the Pusher API.
[19.16 --> 22.88]  Plus, for this week, they wanted us to let you know they're looking for new members of the Pusherati.
[23.52 --> 26.04]  Go to pusher.com slash jobs for more details.
[30.00 --> 44.98]  Welcome to The Change Log, episode 0.7.2.
[45.32 --> 46.26]  I'm Adam Stachowiak.
[46.58 --> 47.42]  And I'm Wynne Netherland.
[47.60 --> 48.52]  This is The Change Log.
[48.58 --> 50.08]  We cover what's fresh and new in open source.
[50.62 --> 53.08]  If you found us on iTunes, we're also on the web at thechangelog.com.
[53.20 --> 54.04]  We're also up on GitHub.
[54.20 --> 58.02]  And if you head to github.com slash explore, you'll find some trending repos,
[58.02 --> 60.82]  some feature repos from our blog, as well as the audio podcast.
[61.74 --> 63.98]  And if you're on Twitter, don't follow Change Log Show.
[64.38 --> 65.52]  Follow The Change Log.
[66.12 --> 66.74]  That's who we are.
[67.02 --> 68.04]  And I'm Adam Stach.
[68.42 --> 70.56]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[70.96 --> 72.36]  The Change Log, big news?
[72.92 --> 73.72]  Big, big news.
[73.96 --> 81.42]  A good Samaritan out there helped us out, Alex Dunney, who is also Mr. Mr. Bug on the Twitter.
[82.14 --> 85.04]  He gave up that prize, Change Log, The Change Log handle.
[85.04 --> 87.84]  So we're excited about being The Change Log on Twitter.
[87.96 --> 89.04]  So thanks again, Alex.
[89.22 --> 94.70]  And if you need web dev work and you're in Canada, check out dialect.ca,
[94.90 --> 98.52]  which is his shop up in the western parts of Canada.
[99.06 --> 103.24]  And speaking of other good news, we've got a new sponsor from the guys over at Pusher.
[103.90 --> 104.86]  Got Pusher on board.
[104.92 --> 106.92]  We're excited about having them back the show.
[107.02 --> 111.92]  We're fans of Pusher and the real-time WebSockets API work that they do.
[111.92 --> 115.36]  We use it at Pure Charity, some of our real-time views.
[115.56 --> 120.52]  Also, Gage's app is a big user of Pusher and some other apps you probably already use.
[120.96 --> 125.82]  We're also looking to hire some folks on the team to be part of what they call the Pusher Riding.
[126.30 --> 127.44]  The Pusher Riding, yeah.
[127.58 --> 133.42]  If you're looking to be on the Pusher team and if you're a Pusher fan, they need some evangelists,
[133.48 --> 135.70]  one in the mobile space, one in the dev space.
[135.70 --> 143.16]  And basically, you get to tour the world and have some fun and talk about cool apps and promote open source and all that fun stuff.
[143.24 --> 148.12]  So check out pusher.com slash jobs or also jobs at pusher.com.
[148.36 --> 149.62]  Sounds like a dream gig.
[149.86 --> 150.90]  Fun episode this week.
[150.94 --> 159.36]  We talked to Mitchell Hashimoto from the Vagrant Project about vagrants and virtual machines and DevOps and all kinds of stuff.
[160.12 --> 162.18]  Distributed virtualized development environments.
[162.26 --> 162.86]  That's a mouthful.
[163.26 --> 163.78]  It is.
[163.78 --> 169.02]  Fun way of saying that you can hydrate virtual machines with little or no work.
[170.16 --> 173.90]  So DevOps, making life easy for the rest of us devs.
[174.00 --> 179.02]  We're always on the lookout for how to spin up new environments more easily.
[179.26 --> 184.12]  This was a fun conversation around virtualized computing and DevOps and some other things.
[184.54 --> 188.18]  And if you go back in time, we actually did a whole entire episode on DevOps.
[188.18 --> 194.40]  So brush up on some Chef and Puppet because you can use those too and learn more about Vagrant in this show.
[194.64 --> 200.56]  Hopefully it won't be the last episodes for all the folks whining about all of the web stuff we're doing on the show.
[200.80 --> 202.12]  This is for you, DevOps.
[202.64 --> 203.26]  There you go.
[203.52 --> 204.22]  You ready to get to it?
[204.48 --> 205.18]  Let's do it.
[205.18 --> 217.22]  Chatting today with Mitchell Hashimoto from the Vagrant Project.
[217.56 --> 221.60]  So Mitchell, why don't you introduce yourself a little bit about your background and what Vagrant is.
[222.00 --> 222.48]  All right.
[222.64 --> 222.88]  Hello.
[223.02 --> 223.84]  Thanks for having me.
[223.84 --> 226.70]  Like I said, my name's Mitchell Hashimoto.
[226.98 --> 231.22]  I've been working on Vagrant in my free time for the past two years.
[231.76 --> 238.84]  And my history is both a web developer and for the past year I've been a full-time operations engineer.
[239.16 --> 242.62]  So hacking the servers from the inside.
[243.44 --> 244.84]  And that's about it.
[245.80 --> 247.42]  So Vagrant, who's it for?
[247.50 --> 247.92]  What's it do?
[247.92 --> 256.38]  Vagrant is for anyone who wants to work in a virtual machine.
[256.76 --> 259.36]  And people, I mean, you might not know whether you want to or not.
[259.42 --> 268.80]  So the general use cases are moving web development into virtual machines, testing like Puppet or Chef scripts in a virtual machine that represents production.
[269.60 --> 277.30]  And the big benefit is just that instead of running a website on your Mac, which isn't very much like how it's going to run in the real world,
[277.30 --> 283.92]  you could run it on a real Ubuntu server virtual machine, which is possibly how it's going to run in production,
[284.22 --> 285.66]  or ideally how it's going to run in production.
[285.94 --> 287.68]  And that minimizes the surprises.
[287.92 --> 291.50]  You're running with the same server configurations, et cetera, et cetera.
[292.46 --> 296.26]  So the install docs for Vagrant, it's a gem to install?
[296.36 --> 297.48]  Is the whole tool chain Ruby?
[298.38 --> 300.30]  It's currently, yeah, it's all Ruby.
[300.50 --> 302.64]  And it's going to stay Ruby, but it's currently a gem.
[302.64 --> 310.60]  With the first official stable release of Vagrant coming out shortly, I'm switching to installers and packages.
[311.14 --> 313.04]  That's going to be the preferred way to install.
[313.46 --> 315.58]  So no more gems soon.
[316.60 --> 318.30]  So you mentioned Oracle's VirtualBox.
[318.38 --> 320.54]  Is it tied just to that particular flavor of VM?
[321.22 --> 322.42]  It is currently, yeah.
[322.74 --> 329.68]  It was a decision I made early on because VirtualBox was the first hypervisor I found with a full API.
[329.68 --> 332.50]  And it's worked out pretty great.
[333.56 --> 335.38]  What are some use cases that you're using it for?
[336.60 --> 342.86]  Every day, the company I work for, all the developers use it to work on the main web application.
[343.24 --> 349.10]  And in my role, I use it to test our chef cookbooks before pushing them out to a staging cluster,
[349.30 --> 351.30]  and then again before pushing them out to production.
[351.80 --> 352.98]  You mentioned chef and puppet.
[353.04 --> 353.56]  Do you have a preference?
[354.78 --> 357.46]  No, I'm not religious about either side.
[357.46 --> 360.94]  I happen to use chef, but puppet's fantastic as well.
[361.10 --> 362.74]  So whichever you feel like learning.
[364.18 --> 366.50]  Anything puppet does better than chef in your opinion?
[368.70 --> 379.06]  I'm a big fan of the declarative nature of puppet's tools because it's kind of harder to grasp your head around while you're programming.
[379.06 --> 386.34]  I think we program more in an imperative way, but there's much less surprise when you run the actual code on your servers,
[386.48 --> 390.66]  whereas chef sometimes surprises you in ways you would not like it to.
[391.96 --> 397.70]  So what can you do with a VirtualBox VM that you can't do with Vagrant yet?
[399.70 --> 400.12]  VirtualBox VM?
[400.12 --> 412.94]  Well, Vagrant really makes it simple for the common cases of working with VirtualBox and provides ways for you to twiddle the knobs a little bit more.
[413.56 --> 418.24]  But VirtualBox is a very, very highly featured virtualization software.
[418.24 --> 423.68]  So Vagrant will do basic things like set up networking for you and stuff like that.
[423.76 --> 433.46]  But if you use VirtualBox by itself, you could really control bandwidth constraints, CPU limitations, hot-plugging CPUs,
[433.50 --> 438.12]  a lot of advanced stuff that I honestly haven't seen used by more than a handful of people.
[438.64 --> 439.90]  But it's there if you want it.
[440.34 --> 442.66]  So pretty much you're wrapping the entire VirtualBox APIs?
[444.26 --> 445.98]  I don't wrap them.
[445.98 --> 451.18]  I give you access through Vagrant's configuration to actually hit them directly if you need that fine-grained control.
[451.50 --> 455.58]  But I put a layer on top that makes it very easy to configure them.
[455.64 --> 460.32]  You just say, you know, I want my virtual machine to have this IP address,
[460.56 --> 465.58]  and I handle all the configuration underneath, including operating system-specific configuration,
[465.74 --> 467.80]  to make it all configured properly.
[468.26 --> 472.24]  You also support multi-box environments, correct?
[472.84 --> 473.64]  Yeah, yeah.
[473.64 --> 477.72]  So you could spin up multiple virtual machines to represent a cluster,
[477.86 --> 479.08]  and they could all communicate to each other.
[480.20 --> 482.44]  Any use cases for using Vagrant in the cloud?
[483.64 --> 485.12]  You mean on a server or something?
[485.38 --> 489.24]  Yeah, pushing these up to somewhere other than your local infrastructure?
[490.04 --> 491.74]  Yeah, there's a couple of use cases.
[492.10 --> 495.92]  A common one is actually a lot of people hook Vagrant into their CI systems,
[496.00 --> 497.54]  like Jenkins or BuildBot or something,
[497.54 --> 501.24]  and they use it to run their tests, which is pretty neat.
[502.32 --> 504.48]  I know folks like LivingSocial do this.
[505.44 --> 509.20]  And then also there's, I'm sure listeners may have heard of Travis CI,
[509.46 --> 512.30]  which is a cloud CI system for Ruby.
[512.54 --> 514.22]  It's a really awesome project,
[514.44 --> 519.02]  and they use Vagrant as a way to isolate all of their test builds
[519.02 --> 521.06]  for projects such as Ruby on Rails.
[523.18 --> 527.08]  And just basically any Ruby project nowadays is tested on Travis CI,
[527.32 --> 529.52]  and they're able to run arbitrary code
[529.52 --> 532.02]  because they're isolating it all in these Vagrant virtual machines.
[532.02 --> 537.24]  So the recent Love Travis CI campaign that launched this week,
[537.26 --> 538.46]  we've been trying to get those guys on the show,
[538.56 --> 540.64]  but they keep saying it's not ready yet.
[540.64 --> 542.90]  I'm not sure what 1.0 looks like to them.
[542.96 --> 545.16]  Looks like you're nearing 1.0 with Vagrant as well.
[545.62 --> 546.92]  Yeah, yeah, I'm excited.
[547.12 --> 548.32]  1.0 should be out next month.
[548.48 --> 551.30]  It's been a long time coming.
[551.64 --> 553.06]  It's almost two years on the project now.
[553.06 --> 557.36]  So what's, I guess, what is the determining factor
[557.36 --> 560.96]  in flipping that bit to 1.0 and quote-unquote production release for you?
[560.96 --> 561.60]  What are you doing today?
[562.36 --> 567.30]  I think, I mean, I'm at the point where I'm ready to make
[567.30 --> 569.32]  some pretty radical changes to Vagrant,
[569.66 --> 573.98]  and I think before doing that I need to have a stable release,
[574.04 --> 577.26]  and there's a large group of companies and organizations
[577.26 --> 579.72]  that have placed their trust in Vagrant as it is now,
[579.72 --> 582.68]  and it's only fair to them to come out with a stable release
[582.68 --> 584.26]  that I'm going to support for some time
[584.26 --> 588.30]  without giving them any surprise backwards incompatibilities or something.
[588.30 --> 592.96]  And for the past, I mean, I'm happy to say, like, in the past year,
[593.04 --> 597.38]  there's been maybe one crashing bug ever reported to Vagrant,
[597.56 --> 598.68]  and so it's been quite stable.
[599.18 --> 601.22]  Most of the bugs are very platform-specific,
[601.48 --> 604.38]  like this specific networking option doesn't work
[604.38 --> 606.52]  when my host is Gen 2 and my guest is Red Hat,
[606.60 --> 607.54]  like weird things like that.
[607.54 --> 611.06]  So I think it's time to just flip the bit, stabilize,
[611.56 --> 615.68]  and really, you know, launch again and show the world
[615.68 --> 618.34]  what I've been up to for the past two years
[618.34 --> 622.48]  and what's stabilized to become a pretty awesome product,
[622.60 --> 623.28]  although I'm biased.
[623.96 --> 626.28]  You mentioned your backgrounds in web development.
[626.54 --> 628.32]  Would you consider yourself, I guess, DevOps now?
[629.24 --> 630.48]  Yeah, yeah, definitely.
[630.68 --> 632.66]  I enjoy talking about DevOps quite a bit
[632.66 --> 635.90]  because I think it's a neat, important movement,
[636.32 --> 640.06]  and I was always full-time dev, and I'm now a full-time ops,
[640.14 --> 642.26]  and I think that's an interesting point of view
[642.26 --> 645.52]  to go in that direction, and it's been fun.
[646.48 --> 648.70]  You see that as a rapidly changing field?
[649.76 --> 653.84]  Yeah, DevOps is, it's, yeah, it's been changing quite a bit.
[653.84 --> 657.22]  I mean, year to year, just with Chef and Puppet coming along,
[657.74 --> 659.54]  and now all these platforms as a service,
[659.98 --> 664.90]  and just the way we're thinking about the cloud in general,
[665.14 --> 667.82]  the way server is built, and there's fault tolerance,
[668.32 --> 671.32]  and how you scale, it just changes so much.
[672.16 --> 673.28]  It's really exciting.
[674.30 --> 676.70]  In your day job, where do you fit in the application lifecycle?
[676.96 --> 679.30]  Are you fully integrated into the project teams,
[679.30 --> 683.16]  or are you lower down on the stream there?
[683.84 --> 686.08]  I work for a pretty small startup company.
[686.48 --> 688.56]  There's only 20 employees overall,
[688.68 --> 690.68]  and the engineering team is only five of us,
[690.78 --> 693.14]  so there's four main application engineers,
[693.40 --> 697.20]  and then I spend around 80% of my time in ops,
[697.26 --> 700.14]  and the other 20 doing various housekeeping
[700.14 --> 701.48]  around the application itself.
[702.88 --> 704.10]  So you mentioned CI.
[704.56 --> 705.66]  I can see the benefit there.
[705.84 --> 707.86]  Are you spinning up any sort of environments around QA
[707.86 --> 712.04]  for human-driven quality assurance?
[712.04 --> 718.32]  No, all our QA is done by our own team,
[718.48 --> 720.54]  and they all run Vagrant instances locally,
[720.88 --> 724.74]  but Vagrant's definitely popular,
[724.96 --> 726.76]  especially for designers, for example,
[726.86 --> 729.16]  because designers need to work with the development site,
[729.24 --> 730.72]  but they don't want to set up the whole environment.
[731.32 --> 732.84]  So just getting Vagrant up and running
[732.84 --> 735.38]  so they can just modify HTML and see it run on their machine
[735.38 --> 737.32]  is a huge productivity boost.
[737.54 --> 738.36]  Same for managers.
[738.36 --> 741.46]  So you can have someone on the team set up the environment,
[741.60 --> 743.48]  and everybody benefits from just cloning that.
[744.14 --> 744.80]  Yep, exactly.
[747.58 --> 751.14]  What was it like going from web development into DevOps?
[751.44 --> 754.26]  What do you miss from just regular application code
[754.26 --> 755.48]  that's not systems-oriented?
[755.48 --> 759.70]  That's a good question.
[762.26 --> 764.54]  I think I'm still in the...
[764.54 --> 766.32]  I mean, it's only been a year that I've been doing Ops,
[766.42 --> 768.48]  so I think I'm still very...
[768.48 --> 770.20]  There's still a lot that's new,
[770.30 --> 771.24]  and I'm still learning a ton,
[771.34 --> 772.62]  so it's all very exciting to me,
[772.66 --> 774.74]  and I haven't really missed too much
[774.74 --> 776.74]  on the web development side yet.
[776.74 --> 780.66]  So I think we'll see in about a year,
[780.86 --> 784.12]  but I mean, I guess...
[784.12 --> 787.68]  I guess I missed some of the problem-solving.
[788.54 --> 790.46]  It's just a different set of problems that you have
[790.46 --> 791.54]  when you're developing an application
[791.54 --> 794.08]  versus when you're worrying all day
[794.08 --> 797.28]  about reliability and monitoring and stuff like that.
[797.44 --> 799.48]  It's kind of a different game,
[799.80 --> 802.28]  but I wouldn't say I miss dev yet.
[802.86 --> 804.96]  One of the things that I enjoy about web development
[804.96 --> 808.28]  is just pleasing users and engaging with users.
[808.40 --> 811.34]  I guess your users are more developer types.
[811.54 --> 814.10]  Is that a blessing or a curse?
[816.46 --> 817.46]  Well, I guess, yeah.
[817.66 --> 821.68]  So I'd say it's a both,
[821.94 --> 823.26]  but more of a blessing
[823.26 --> 824.62]  because when something goes wrong,
[824.86 --> 827.10]  it's very easy to give them technical instructions
[827.10 --> 830.96]  to get assistance, which I like,
[830.96 --> 834.58]  and yeah, I would say it's a blessing overall, actually.
[834.58 --> 837.26]  Are we as developers more demanding as a user base?
[839.34 --> 843.38]  I think a user of anything is demanding,
[843.64 --> 845.34]  but I would say developers are less so
[845.34 --> 847.06]  because they understand the work that's involved
[847.06 --> 847.92]  to make something happen,
[848.48 --> 851.14]  and a lot of times they're willing to make it happen themselves.
[851.38 --> 853.20]  Like Vagrant has almost 100 contributors now,
[853.68 --> 857.34]  and a lot of times when they have an itch,
[857.40 --> 859.20]  they scratch it themselves, which is nice.
[860.12 --> 862.00]  So you just returned from Europe.
[862.22 --> 862.98]  What were you doing over there?
[862.98 --> 866.52]  Yeah, I was in Brussels this past weekend for Fosdom.
[867.14 --> 868.44]  It was the first time I was over there,
[868.66 --> 869.98]  and Brussels is an amazing city,
[870.34 --> 872.26]  and Fosdom is a pretty amazing conference.
[872.44 --> 874.94]  I think they said there was over 5,000 people this year,
[875.38 --> 879.54]  and they covered topics from DevOps to virtualization
[879.54 --> 882.68]  to X-windowing systems, cryptography,
[882.76 --> 883.90]  I mean, like the whole spectrum,
[884.10 --> 886.48]  and it was really neat to just be able to be like,
[886.54 --> 888.86]  well, I'm going to go see a talk on configuration management,
[888.98 --> 890.84]  then I'm going to go see a talk on cryptography,
[890.84 --> 891.54]  because why not?
[893.80 --> 895.72]  But yeah, the weather there sucked.
[895.92 --> 897.84]  It was like negative 10 degrees Celsius.
[898.40 --> 900.44]  I don't think I've ever been that cold in my life,
[900.60 --> 901.70]  having grown up in California.
[902.86 --> 904.60]  So Vagrant's opened some doors for you to speak.
[904.66 --> 906.76]  Is that the highlight so far?
[907.14 --> 908.14]  I've been really lucky.
[908.14 --> 911.04]  When Vagrant was still relatively new,
[911.24 --> 912.72]  I would say in the summer of 2010,
[912.84 --> 914.34]  it was like six months old,
[915.42 --> 918.56]  Engine Yard, specifically Carl Lurch,
[918.78 --> 921.28]  who's on the Rubion Rails Corps and did Bundler.
[921.58 --> 922.36]  Half of Carl Huda?
[922.88 --> 923.98]  Yeah, half of Carl Huda,
[924.94 --> 928.20]  and he discovered Vagrant in a way,
[928.30 --> 929.60]  and he liked what he saw.
[929.78 --> 932.42]  I'm not sure exactly what he thought,
[932.42 --> 935.30]  but he then told Dr. Nick about it,
[935.40 --> 938.18]  who's now VP at Engine Yard,
[938.70 --> 940.74]  and then I was in San Francisco,
[940.90 --> 941.86]  so we kind of met together,
[942.36 --> 945.82]  and they ended up giving me an open source grant,
[946.10 --> 948.76]  which they've been supporting for the past couple of years,
[948.84 --> 952.20]  which has allowed me to travel and speak about Vagrant
[952.20 --> 954.52]  and has given me a few resources,
[954.68 --> 957.20]  such as Windows test machines and CI machines
[957.20 --> 960.28]  that have really helped push Vagrant along.
[960.28 --> 965.36]  I think a lot of my success is in a large part due to them.
[966.14 --> 967.82]  I love how transparent you are about the finances
[967.82 --> 969.80]  here on the finance page.
[970.38 --> 970.70]  Nice.
[971.34 --> 972.48]  So pay for a feature.
[972.72 --> 973.80]  Had many takers on that?
[974.70 --> 975.86]  Very minor features.
[976.56 --> 978.18]  I put it there just really,
[978.94 --> 980.28]  the main reason I put it there
[980.28 --> 982.70]  is because sometimes people will be like,
[982.76 --> 984.60]  well, I want it to support VMware Fusion,
[985.04 --> 987.00]  and then I plan on it,
[987.00 --> 990.20]  but I really do on my own time
[990.20 --> 992.76]  what I feel is most wanted or what I need,
[993.26 --> 995.14]  and I like to have the option where it's like,
[995.20 --> 997.06]  well, if you really want it, you can just pay for it.
[997.14 --> 999.18]  So I haven't had anyone pay for a major one,
[999.30 --> 1001.32]  and I'm actually pretty happy about that,
[1001.62 --> 1004.16]  but it's there just to give people an option.
[1005.10 --> 1007.42]  What has GitHub meant to the project development
[1007.42 --> 1008.24]  in the last two years?
[1008.24 --> 1010.80]  I couldn't, just in general,
[1010.90 --> 1012.86]  I couldn't imagine doing any open source project
[1012.86 --> 1015.80]  without GitHub because, I mean,
[1015.84 --> 1017.44]  it's such a standard workflow now.
[1017.58 --> 1018.94]  Like every developer kind of understands
[1018.94 --> 1020.14]  the pull request system,
[1020.62 --> 1024.72]  and Git is pretty ubiquitous in the community now.
[1024.88 --> 1028.34]  So just being able to say my projects on GitHub
[1028.34 --> 1031.28]  opens the door to thousands of contributions,
[1031.76 --> 1033.74]  and it's been awesome.
[1033.74 --> 1038.72]  Speaking of, 1,200 watchers, almost 250 forks.
[1039.32 --> 1039.48]  Yeah.
[1039.64 --> 1041.72]  Yeah, no open pull requests and only eight issues.
[1041.86 --> 1043.54]  Does that mean you're doing something right,
[1043.64 --> 1045.84]  or is it just quiet on the Western front?
[1046.50 --> 1050.70]  It's, so I actually close handle issues.
[1050.94 --> 1052.90]  Since I'm approaching 1.0,
[1053.28 --> 1056.36]  I've been really firing through those pull requests.
[1056.62 --> 1060.28]  So I get around maybe five issues a day
[1060.28 --> 1062.46]  and maybe two pull requests a day,
[1062.46 --> 1064.42]  and I try to close them
[1064.42 --> 1066.34]  or at least respond to them same day.
[1066.60 --> 1068.00]  But since 1.0 is so close,
[1068.06 --> 1071.66]  I've been really, really blasting through them.
[1071.98 --> 1073.80]  But if you looked about a month ago,
[1073.98 --> 1076.60]  you would have seen 50 issues and 10 pull requests
[1076.60 --> 1078.68]  because I was slower then.
[1080.10 --> 1083.26]  Do you find yourself doing a lot of the enhancements
[1083.26 --> 1084.04]  and patches yourself,
[1084.12 --> 1086.70]  or do you encourage the community to submit a patch?
[1087.80 --> 1090.10]  It matters how serious it is.
[1090.10 --> 1091.72]  If it's a serious bug,
[1091.82 --> 1093.26]  and I know it's affecting quite a few people,
[1093.42 --> 1095.50]  then I'll fix it myself very quickly.
[1095.70 --> 1096.68]  If it's not so serious,
[1096.80 --> 1098.56]  I do ask the person,
[1099.06 --> 1101.62]  could you look into fixing this yourself
[1101.62 --> 1102.60]  because I'm not going to have time.
[1104.14 --> 1105.56]  And it's been pretty successful.
[1105.78 --> 1109.32]  I get maybe two or three outside contributions a week,
[1109.44 --> 1112.90]  which is much more than a year ago,
[1113.02 --> 1114.76]  which is much more than a year before that.
[1114.76 --> 1116.50]  So I think it's on the right track.
[1116.94 --> 1120.24]  Although I'd love to find someone else to work on it,
[1121.30 --> 1125.42]  like a core contributor alongside me.
[1125.96 --> 1129.34]  So you're a brave soul to be supporting a project like this
[1129.34 --> 1131.84]  on Ruby on Windows as well.
[1132.18 --> 1134.46]  Are you squashing those bugs in Windows,
[1134.56 --> 1136.14]  or do you have someone that does that dirty work?
[1136.14 --> 1137.16]  Oh my gosh, Windows.
[1137.16 --> 1137.34]  Windows.
[1138.58 --> 1140.50]  It's, uh...
[1140.50 --> 1142.92]  Every time I think something's going to be easy on Windows,
[1143.18 --> 1146.38]  it always surprises me that it's impossibly hard.
[1147.06 --> 1148.52]  Ever since the beginning of Vagrant,
[1148.60 --> 1150.12]  it's been a challenge to work on Windows.
[1150.40 --> 1151.06]  I have to think,
[1151.64 --> 1153.70]  the person who started Vagrant with me is John Bender,
[1153.90 --> 1156.12]  and he was the first person who was like,
[1156.16 --> 1157.16]  I think this should work on Windows,
[1157.30 --> 1158.62]  and he put in a lot of work
[1158.62 --> 1160.06]  to get the initial versions on Windows.
[1160.86 --> 1162.52]  So since then, it's mostly been incremental,
[1162.52 --> 1165.74]  but yeah, Windows is pretty hard.
[1165.92 --> 1167.68]  But thanks to people in the Ruby community,
[1167.86 --> 1170.24]  like Louis Lavina, who does the Ruby installer,
[1170.96 --> 1174.10]  and he pretty much watches every issue on Vagrant,
[1174.18 --> 1175.04]  and when it's Windows-related,
[1175.16 --> 1177.84]  he almost always responds and helps out.
[1178.02 --> 1179.44]  It's been much smoother,
[1179.88 --> 1182.80]  but definitely, definitely not fun.
[1183.90 --> 1186.34]  What sort of host operating systems
[1186.34 --> 1187.76]  are you running on your VMs?
[1187.76 --> 1191.20]  The host operating systems,
[1191.60 --> 1192.86]  I pretty much...
[1192.86 --> 1193.16]  Oh, yes, I'm sorry.
[1193.58 --> 1194.28]  Guest, okay, Guest.
[1194.34 --> 1196.68]  So Guest, I usually run Ubuntu,
[1196.90 --> 1197.96]  so that's why...
[1197.96 --> 1199.64]  Is that your favorite flavor of Linux?
[1200.40 --> 1202.26]  Yeah, it's the one I'm most comfortable with.
[1203.22 --> 1205.16]  I just never really spent a lot of time with the others,
[1205.30 --> 1207.00]  so that's the main reason,
[1207.30 --> 1210.84]  and yeah, Ubuntu is the only one I use all the time.
[1211.80 --> 1213.92]  What other open-source projects out there
[1213.92 --> 1215.80]  have you excited that you just want to play with?
[1215.80 --> 1219.92]  Ah, I mean, I've been really into...
[1219.92 --> 1221.04]  Just due to my job,
[1221.12 --> 1222.36]  I've been really excited about
[1222.36 --> 1225.16]  some server software popping around,
[1225.40 --> 1227.42]  like React really excites me right now,
[1227.72 --> 1231.80]  but in terms of stuff related to Vagrant, perhaps...
[1232.52 --> 1233.22]  It can be anything.
[1234.32 --> 1235.82]  Well, there is one related to Vagrant,
[1235.86 --> 1237.32]  which is really awesome, called VWi,
[1237.56 --> 1239.02]  and it creates...
[1239.02 --> 1241.36]  You basically give it definitions and ISO files,
[1241.44 --> 1243.48]  and it creates virtual machine images for you.
[1243.48 --> 1245.44]  It could create Vagrant virtual machine images,
[1245.56 --> 1247.44]  but it could also create KVM images
[1247.44 --> 1248.78]  and VMware Fusion images,
[1249.40 --> 1251.32]  and just...
[1251.32 --> 1253.92]  If you ever use it the first time you ever watch it run
[1253.92 --> 1255.72]  and install something
[1255.72 --> 1257.94]  and set up a full system from scratch
[1257.94 --> 1260.28]  without you touching your computer once,
[1260.72 --> 1262.26]  it's like magic happening.
[1262.46 --> 1265.12]  You see things typing inside the VM,
[1265.26 --> 1267.26]  you see things installing,
[1267.40 --> 1268.20]  and then you see packaging.
[1268.20 --> 1269.32]  It's pretty cool.
[1270.16 --> 1272.44]  And it's...
[1272.44 --> 1273.94]  I mean, yesterday was the first day
[1273.94 --> 1277.02]  that I saw a video of a Windows machine
[1277.02 --> 1277.94]  being set up through that,
[1278.04 --> 1279.60]  and that's really crazy to see.
[1279.84 --> 1281.18]  Think that's something that will integrate
[1281.18 --> 1282.22]  into Vagrant at some point?
[1282.96 --> 1283.90]  Definitely, yeah.
[1284.02 --> 1285.16]  So after Vagrant 1.0,
[1285.20 --> 1287.08]  one of the primary things I want to do
[1287.08 --> 1292.04]  is integrate an image creation aspect into Vagrant,
[1292.20 --> 1294.50]  since I think that's a missing half
[1294.50 --> 1295.54]  that everyone needs,
[1295.72 --> 1297.74]  and Vagrant just doesn't do anything about so far.
[1297.74 --> 1299.54]  And VW is awesome about it,
[1299.58 --> 1301.10]  but since we're on different release schedules,
[1301.46 --> 1303.50]  there's sometimes incompatibilities,
[1304.14 --> 1306.60]  sometimes feature differences,
[1307.00 --> 1308.94]  and I want to line that all up.
[1310.48 --> 1311.78]  Do you have a programming hero?
[1313.42 --> 1314.16]  Programming hero?
[1314.38 --> 1315.00]  I used to ask,
[1315.10 --> 1316.02]  who is your programming hero?
[1316.16 --> 1317.76]  And now we've had so many people say,
[1317.84 --> 1318.56]  I don't have one,
[1318.60 --> 1320.16]  and I'm asking if you've got one first.
[1320.24 --> 1320.74]  Okay, so...
[1321.90 --> 1323.46]  Well, the programming hero I have,
[1324.44 --> 1325.72]  no one would have heard about,
[1325.90 --> 1326.90]  but it's definitely...
[1326.90 --> 1327.56]  Well, that's even better.
[1328.14 --> 1328.56]  Sound of light.
[1329.22 --> 1329.54]  It's...
[1329.54 --> 1331.78]  He's not a huge open source guy.
[1331.90 --> 1335.32]  He's just the guy that I worked with at my first job,
[1335.40 --> 1341.12]  and he kind of taught me everything I knew about a lot of things.
[1341.20 --> 1342.62]  I mean, about open source,
[1342.90 --> 1344.22]  which editor to use,
[1345.28 --> 1346.18]  Linux in general,
[1346.38 --> 1349.32]  and I think I'd be a much different person
[1349.32 --> 1350.82]  if I never met him,
[1350.82 --> 1352.40]  and so I have to thank him.
[1352.50 --> 1353.78]  His name's Tim, by the way.
[1355.06 --> 1358.04]  But in terms of open source and people who you would know,
[1358.14 --> 1362.90]  I've always looked up to people like Yehuda Katz and Carl Lurch
[1362.90 --> 1366.22]  and Tender Love,
[1366.22 --> 1368.26]  and all those guys,
[1368.38 --> 1370.34]  because I think it's amazing how much work they do,
[1371.84 --> 1376.30]  how much of a change they make in such a large community,
[1376.30 --> 1378.20]  pretty selflessly,
[1378.20 --> 1381.12]  and that's always been very cool to me.
[1381.12 --> 1384.72]  How long has the Vagrant file been around?
[1385.28 --> 1386.00]  Since the beginning?
[1386.52 --> 1387.46]  Since the beginning, yeah.
[1387.70 --> 1388.72]  I saw a post the other day,
[1388.74 --> 1389.70]  I'm trying to track this down,
[1389.84 --> 1392.38]  where the author lamented the fact
[1392.38 --> 1395.34]  we've got this proliferation of, you know,
[1395.38 --> 1397.20]  rake file-inspired files out there,
[1397.26 --> 1398.38]  and now you have to go into your editor
[1398.38 --> 1400.28]  and tell everyone it's a Ruby file
[1400.28 --> 1401.64]  to get syntax highlighting?
[1402.22 --> 1403.60]  Well, to help with that,
[1403.80 --> 1404.88]  Vagrant does automatically,
[1405.02 --> 1406.00]  when you create a Vagrant file,
[1406.14 --> 1408.58]  put in the Emacs and Vim headers
[1408.58 --> 1410.00]  so they set the right file type.
[1410.34 --> 1411.34]  But yeah, I agree.
[1411.46 --> 1412.34]  It's kind of annoying.
[1412.66 --> 1413.38]  What's your favorite editor?
[1414.38 --> 1418.62]  So, I used Emacs for four years,
[1418.72 --> 1421.08]  and last month I switched to Vim as an experiment,
[1421.48 --> 1423.74]  but I think I'm going to stick with it
[1423.74 --> 1425.12]  because I've liked it.
[1425.72 --> 1428.56]  I'm almost sick to say that I like it a lot.
[1429.94 --> 1431.08]  I'm a recent convert, too.
[1431.08 --> 1433.16]  I've been using it for a few months now.
[1433.26 --> 1434.58]  I couldn't imagine going back.
[1434.64 --> 1435.74]  The other day I had to go into TextMate
[1435.74 --> 1436.26]  to do something.
[1436.34 --> 1436.98]  I forget what it was.
[1437.24 --> 1440.86]  I'm pressing you and I all over the place
[1440.86 --> 1442.72]  trying to get up and down and out of the thing.
[1443.32 --> 1445.60]  I'm extremely stubborn about the fact that I will.
[1446.02 --> 1447.78]  I haven't had TextMate installed in years,
[1447.88 --> 1448.80]  and I refuse to do it,
[1448.84 --> 1450.58]  even though for some things I know it would be easier
[1450.58 --> 1451.78]  just to fire it up,
[1451.86 --> 1453.30]  but I'm just stubborn about it.
[1454.30 --> 1456.08]  So when can we expect 1.0?
[1457.72 --> 1458.62]  In less than a month.
[1458.62 --> 1461.66]  I have an exact date in my mind,
[1461.80 --> 1464.40]  but I don't want to promise anything,
[1464.62 --> 1465.90]  so less than a month.
[1466.28 --> 1467.18]  And with the release,
[1467.34 --> 1468.28]  we're going to have...
[1468.28 --> 1470.96]  I'm going to do a homepage redesign.
[1471.32 --> 1472.94]  The docs are going to be completely redone,
[1473.14 --> 1474.72]  so they're going to be completely up to date.
[1474.84 --> 1476.46]  They're going to cover every configuration option.
[1478.36 --> 1479.36]  Installers are coming out.
[1479.36 --> 1482.36]  I think it should make a pretty big...
[1483.36 --> 1484.90]  It should stabilize everything
[1484.90 --> 1486.30]  and make a pretty big splash overall.
[1487.28 --> 1487.90]  Good deal.
[1488.60 --> 1489.28]  Well, thanks, Mitchell.
[1489.42 --> 1490.50]  Appreciate you chatting with us.
[1490.98 --> 1491.38]  Thanks.
[1491.50 --> 1493.44]  I've been a big fan of the changelog for a while,
[1493.56 --> 1494.70]  so I was excited when you asked.
[1494.96 --> 1495.80]  So thanks for having me.
[1499.42 --> 1500.66]  Thanks again to our sponsor,
[1500.84 --> 1502.64]  Pusher at pusher.com.
[1502.70 --> 1504.40]  They're doing some real fun stuff
[1504.40 --> 1506.50]  around hosted APIs and the real-time web.
[1506.50 --> 1508.78]  We also want to thank you for listening to the show
[1508.78 --> 1509.52]  because without you,
[1509.62 --> 1510.62]  this show would not be possible.
[1511.26 --> 1513.26]  And if you're interested in sponsoring the changelog,
[1513.32 --> 1515.32]  we certainly appreciate your support.
[1515.80 --> 1518.48]  Shoot us an email at sponsor at the changelog.com.
[1518.84 --> 1519.66]  Until next time.
